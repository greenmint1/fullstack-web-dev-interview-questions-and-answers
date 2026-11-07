# LLM Cost & Latency Interview Questions and Answers

_Last updated: November 5, 2026_

450 interview questions with answers about the cost and latency of LLM apps, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers cover what you need when you build on hosted APIs (OpenAI, Anthropic, Google Gemini and others) and when you run open models yourself (vLLM, SGLang, TensorRT-LLM). Prices and limits change often, so the numbers in the examples are made up to show the math. Always check the provider's pricing page for real numbers.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is a token?](#1-what-is-a-token)
- [2: Why do LLM providers charge per token and not per request?](#2-why-do-llm-providers-charge-per-token-and-not-per-request)
- [3: What is the difference between input tokens and output tokens?](#3-what-is-the-difference-between-input-tokens-and-output-tokens)
- [4: Why are output tokens usually more expensive than input tokens?](#4-why-are-output-tokens-usually-more-expensive-than-input-tokens)
- [5: How do you calculate the cost of a single LLM request?](#5-how-do-you-calculate-the-cost-of-a-single-llm-request)
- [6: What does "price per 1M tokens" mean?](#6-what-does-price-per-1m-tokens-mean)
- [7: What is latency in the context of LLMs?](#7-what-is-latency-in-the-context-of-llms)
- [8: What is Time to First Token (TTFT)?](#8-what-is-time-to-first-token-ttft)
- [9: What is Time Per Output Token (TPOT)?](#9-what-is-time-per-output-token-tpot)
- [10: How do you estimate the total latency of a response?](#10-how-do-you-estimate-the-total-latency-of-a-response)
- [11: What is throughput?](#11-what-is-throughput)
- [12: What is the difference between latency and throughput?](#12-what-is-the-difference-between-latency-and-throughput)
- [13: What is tokens per second (TPS)?](#13-what-is-tokens-per-second-tps)
- [14: What is a context window?](#14-what-is-a-context-window)
- [15: How does prompt length affect cost?](#15-how-does-prompt-length-affect-cost)
- [16: How does prompt length affect latency?](#16-how-does-prompt-length-affect-latency)
- [17: How does output length affect latency?](#17-how-does-output-length-affect-latency)
- [18: What is max_tokens and why does it matter?](#18-what-is-max_tokens-and-why-does-it-matter)
- [19: What happens when a response hits the max_tokens limit?](#19-what-happens-when-a-response-hits-the-max_tokens-limit)
- [20: Why is streaming useful for LLM apps?](#20-why-is-streaming-useful-for-llm-apps)
- [21: Does streaming reduce the cost of a request?](#21-does-streaming-reduce-the-cost-of-a-request)
- [22: How do you enable streaming with the OpenAI SDK?](#22-how-do-you-enable-streaming-with-the-openai-sdk)
- [23: How do you enable streaming with the Anthropic SDK?](#23-how-do-you-enable-streaming-with-the-anthropic-sdk)
- [24: What is perceived latency?](#24-what-is-perceived-latency)
- [25: Why do bigger models usually cost more?](#25-why-do-bigger-models-usually-cost-more)
- [26: Why are bigger models usually slower?](#26-why-are-bigger-models-usually-slower)
- [27: What is a "small" or "mini" model and when should you use it?](#27-what-is-a-small-or-mini-model-and-when-should-you-use-it)
- [28: What is the cost and quality trade-off when choosing a model?](#28-what-is-the-cost-and-quality-trade-off-when-choosing-a-model)
- [29: How do you count tokens before sending a request?](#29-how-do-you-count-tokens-before-sending-a-request)
- [30: How do you count tokens with the Anthropic API?](#30-how-do-you-count-tokens-with-the-anthropic-api)
- [31: Where do you see how many tokens a request actually used?](#31-where-do-you-see-how-many-tokens-a-request-actually-used)
- [32: Why does the same text have a different token count on different models?](#32-why-does-the-same-text-have-a-different-token-count-on-different-models)
- [33: Why do non-English languages often use more tokens?](#33-why-do-non-english-languages-often-use-more-tokens)
- [34: Does code use more tokens than plain text?](#34-does-code-use-more-tokens-than-plain-text)
- [35: What is a system prompt and how does it affect cost?](#35-what-is-a-system-prompt-and-how-does-it-affect-cost)
- [36: Why does chat history make requests more expensive over time?](#36-why-does-chat-history-make-requests-more-expensive-over-time)
- [37: What is prompt caching?](#37-what-is-prompt-caching)
- [38: What does "prefix" mean in prompt caching?](#38-what-does-prefix-mean-in-prompt-caching)
- [39: How should you order your prompt to get good cache hits?](#39-how-should-you-order-your-prompt-to-get-good-cache-hits)
- [40: Does OpenAI prompt caching need any code changes?](#40-does-openai-prompt-caching-need-any-code-changes)
- [41: How do you use prompt caching with Anthropic?](#41-how-do-you-use-prompt-caching-with-anthropic)
- [42: How long does a prompt cache usually last?](#42-how-long-does-a-prompt-cache-usually-last)
- [43: What is a cache write and a cache read?](#43-what-is-a-cache-write-and-a-cache-read)
- [44: What is a batch API?](#44-what-is-a-batch-api)
- [45: When should you use a batch API?](#45-when-should-you-use-a-batch-api)
- [46: What is a rate limit?](#46-what-is-a-rate-limit)
- [47: What is RPM?](#47-what-is-rpm)
- [48: What is TPM?](#48-what-is-tpm)
- [49: What does an HTTP 429 error mean?](#49-what-does-an-http-429-error-mean)
- [50: What is exponential backoff?](#50-what-is-exponential-backoff)
- [51: Do the official SDKs retry failed requests automatically?](#51-do-the-official-sdks-retry-failed-requests-automatically)
- [52: Why should you set a timeout on LLM calls?](#52-why-should-you-set-a-timeout-on-llm-calls)
- [53: What is a reasoning model?](#53-what-is-a-reasoning-model)
- [54: What are reasoning tokens and are they billed?](#54-what-are-reasoning-tokens-and-are-they-billed)
- [55: How can you control how much a reasoning model thinks?](#55-how-can-you-control-how-much-a-reasoning-model-thinks)
- [56: When should you avoid using a reasoning model?](#56-when-should-you-avoid-using-a-reasoning-model)
- [57: What is an embedding and how is it priced?](#57-what-is-an-embedding-and-how-is-it-priced)
- [58: Why are embedding calls much cheaper than chat completions?](#58-why-are-embedding-calls-much-cheaper-than-chat-completions)
- [59: What is RAG and how does it affect cost?](#59-what-is-rag-and-how-does-it-affect-cost)
- [60: How does the number of retrieved chunks affect cost and latency?](#60-how-does-the-number-of-retrieved-chunks-affect-cost-and-latency)
- [61: What is a semantic cache?](#61-what-is-a-semantic-cache)
- [62: What is the difference between an exact cache and a semantic cache?](#62-what-is-the-difference-between-an-exact-cache-and-a-semantic-cache)
- [63: What is the difference between prompt caching and response caching?](#63-what-is-the-difference-between-prompt-caching-and-response-caching)
- [64: How does temperature affect cost and latency?](#64-how-does-temperature-affect-cost-and-latency)
- [65: Does a lower temperature make caching responses safer?](#65-does-a-lower-temperature-make-caching-responses-safer)
- [66: What is model routing?](#66-what-is-model-routing)
- [67: What is a fallback model?](#67-what-is-a-fallback-model)
- [68: What is a cold start in LLM serving?](#68-what-is-a-cold-start-in-llm-serving)
- [69: What are p50, p95 and p99 latency?](#69-what-are-p50-p95-and-p99-latency)
- [70: Why is average latency not enough to measure performance?](#70-why-is-average-latency-not-enough-to-measure-performance)
- [71: What is network latency and how does it affect LLM calls?](#71-what-is-network-latency-and-how-does-it-affect-llm-calls)
- [72: Why does region matter for LLM latency?](#72-why-does-region-matter-for-llm-latency)
- [73: What are the main cost drivers in an LLM app?](#73-what-are-the-main-cost-drivers-in-an-llm-app)
- [74: Why should you log token usage for every request?](#74-why-should-you-log-token-usage-for-every-request)
- [75: What is a cost per user or cost per feature?](#75-what-is-a-cost-per-user-or-cost-per-feature)
- [76: How do you put a spending limit on an LLM API?](#76-how-do-you-put-a-spending-limit-on-an-llm-api)
- [77: Why should you use separate API keys or projects per environment?](#77-why-should-you-use-separate-api-keys-or-projects-per-environment)
- [78: What is prompt compression?](#78-what-is-prompt-compression)
- [79: How can you make a system prompt shorter without losing quality?](#79-how-can-you-make-a-system-prompt-shorter-without-losing-quality)
- [80: How do you ask the model for shorter answers?](#80-how-do-you-ask-the-model-for-shorter-answers)
- [81: What is structured output?](#81-what-is-structured-output)
- [82: How does structured output help with cost?](#82-how-does-structured-output-help-with-cost)
- [83: What is a tool call and how does it add cost?](#83-what-is-a-tool-call-and-how-does-it-add-cost)
- [84: Why do tool definitions cost tokens?](#84-why-do-tool-definitions-cost-tokens)
- [85: What is an AI agent and why can it be expensive?](#85-what-is-an-ai-agent-and-why-can-it-be-expensive)
- [86: How do you limit the cost of an agent?](#86-how-do-you-limit-the-cost-of-an-agent)
- [87: What is a multi-turn conversation's "token growth" problem?](#87-what-is-a-multi-turn-conversations-token-growth-problem)
- [88: How do you trim chat history to save tokens?](#88-how-do-you-trim-chat-history-to-save-tokens)
- [89: What is conversation summarization?](#89-what-is-conversation-summarization)
- [90: What is a "token budget"?](#90-what-is-a-token-budget)
- [91: What is the difference between a hosted API and self-hosting a model?](#91-what-is-the-difference-between-a-hosted-api-and-self-hosting-a-model)
- [92: What is an open-weight model?](#92-what-is-an-open-weight-model)
- [93: What is an inference provider?](#93-what-is-an-inference-provider)
- [94: What is GPU memory and why does it matter for LLMs?](#94-what-is-gpu-memory-and-why-does-it-matter-for-llms)
- [95: What is quantization?](#95-what-is-quantization)
- [96: How does quantization reduce cost?](#96-how-does-quantization-reduce-cost)
- [97: What is a prompt token vs a completion token?](#97-what-is-a-prompt-token-vs-a-completion-token)
- [98: Why should you not send the full document when only part is needed?](#98-why-should-you-not-send-the-full-document-when-only-part-is-needed)
- [99: What is a long-context price tier?](#99-what-is-a-long-context-price-tier)
- [100: What is a cancellation and why does it matter for cost?](#100-what-is-a-cancellation-and-why-does-it-matter-for-cost)
- [101: What are images priced like in multimodal models?](#101-what-are-images-priced-like-in-multimodal-models)
- [102: How can you reduce the cost of image inputs?](#102-how-can-you-reduce-the-cost-of-image-inputs)
- [103: How is audio priced in LLM APIs?](#103-how-is-audio-priced-in-llm-apis)
- [104: What is a "free tier" and why should you not rely on it in production?](#104-what-is-a-free-tier-and-why-should-you-not-rely-on-it-in-production)
- [105: What is a usage tier?](#105-what-is-a-usage-tier)
- [106: What is the difference between a flagship model and a budget model?](#106-what-is-the-difference-between-a-flagship-model-and-a-budget-model)
- [107: Why should you test with real data before choosing a model?](#107-why-should-you-test-with-real-data-before-choosing-a-model)
- [108: What is an evaluation set (eval) and why does it matter for cost work?](#108-what-is-an-evaluation-set-eval-and-why-does-it-matter-for-cost-work)
- [109: What does "cost per 1,000 requests" mean and why is it useful?](#109-what-does-cost-per-1000-requests-mean-and-why-is-it-useful)
- [110: How do you estimate monthly LLM costs for a new feature?](#110-how-do-you-estimate-monthly-llm-costs-for-a-new-feature)
- [111: What is the "N+1" problem in LLM calls?](#111-what-is-the-n1-problem-in-llm-calls)
- [112: Why is it often better to process several items in one prompt?](#112-why-is-it-often-better-to-process-several-items-in-one-prompt)
- [113: What is parallel request execution?](#113-what-is-parallel-request-execution)
- [114: What is sequential chaining and why is it slow?](#114-what-is-sequential-chaining-and-why-is-it-slow)
- [115: What is the difference between synchronous and asynchronous LLM processing?](#115-what-is-the-difference-between-synchronous-and-asynchronous-llm-processing)
- [116: What is a queue and how does it help with LLM workloads?](#116-what-is-a-queue-and-how-does-it-help-with-llm-workloads)
- [117: What is an LLM gateway?](#117-what-is-an-llm-gateway)
- [118: What is LLM observability?](#118-what-is-llm-observability)
- [119: What is a trace in LLM observability?](#119-what-is-a-trace-in-llm-observability)
- [120: What basic metrics should you track for an LLM feature?](#120-what-basic-metrics-should-you-track-for-an-llm-feature)
- [121: What is the difference between a model alias and a pinned model version?](#121-what-is-the-difference-between-a-model-alias-and-a-pinned-model-version)
- [122: Why can a model upgrade change your costs?](#122-why-can-a-model-upgrade-change-your-costs)
- [123: What does "deprecation" of a model mean for cost planning?](#123-what-does-deprecation-of-a-model-mean-for-cost-planning)
- [124: What is a stop sequence and how can it save tokens?](#124-what-is-a-stop-sequence-and-how-can-it-save-tokens)
- [125: What is a few-shot prompt and how does it affect cost?](#125-what-is-a-few-shot-prompt-and-how-does-it-affect-cost)
- [126: What is the cost difference between zero-shot and few-shot prompts?](#126-what-is-the-cost-difference-between-zero-shot-and-few-shot-prompts)
- [127: What is fine-tuning and how can it lower cost?](#127-what-is-fine-tuning-and-how-can-it-lower-cost)
- [128: What is distillation?](#128-what-is-distillation)
- [129: What is a "serverless" inference endpoint?](#129-what-is-a-serverless-inference-endpoint)
- [130: What is a dedicated or provisioned deployment?](#130-what-is-a-dedicated-or-provisioned-deployment)
- [131: What is the difference between pay-as-you-go and reserved capacity pricing?](#131-what-is-the-difference-between-pay-as-you-go-and-reserved-capacity-pricing)
- [132: What is a priority or service tier?](#132-what-is-a-priority-or-service-tier)
- [133: What is OpenAI's Flex processing?](#133-what-is-openais-flex-processing)
- [134: Why does the time of day affect LLM latency?](#134-why-does-the-time-of-day-affect-llm-latency)
- [135: What is a "429 vs 529 vs 503" error from an LLM provider?](#135-what-is-a-429-vs-529-vs-503-error-from-an-llm-provider)
- [136: What is "tokens per word" and why does it matter for estimates?](#136-what-is-tokens-per-word-and-why-does-it-matter-for-estimates)
- [137: How does JSON formatting affect token count?](#137-how-does-json-formatting-affect-token-count)
- [138: Why should you remove HTML before sending web pages to a model?](#138-why-should-you-remove-html-before-sending-web-pages-to-a-model)
- [139: What is the difference between a chat model and a completion model for cost?](#139-what-is-the-difference-between-a-chat-model-and-a-completion-model-for-cost)
- [140: What is a "warm-up" request?](#140-what-is-a-warm-up-request)
- [141: Can you cache embeddings?](#141-can-you-cache-embeddings)
- [142: Why do you need to re-embed data when changing the embedding model?](#142-why-do-you-need-to-re-embed-data-when-changing-the-embedding-model)
- [143: What are embedding dimensions and how do they affect cost?](#143-what-are-embedding-dimensions-and-how-do-they-affect-cost)
- [144: What is a vector database cost driver?](#144-what-is-a-vector-database-cost-driver)
- [145: What is an SLA in the context of LLM APIs?](#145-what-is-an-sla-in-the-context-of-llm-apis)
- [146: What is "time to last token"?](#146-what-is-time-to-last-token)
- [147: Why should background jobs use cheaper models or batch APIs?](#147-why-should-background-jobs-use-cheaper-models-or-batch-apis)
- [148: What does "good enough" mean when picking a model?](#148-what-does-good-enough-mean-when-picking-a-model)
- [149: What is a cost alert?](#149-what-is-a-cost-alert)
- [150: What are the first three things you would check if an LLM bill suddenly went up?](#150-what-are-the-first-three-things-you-would-check-if-an-llm-bill-suddenly-went-up)

### Moderate Questions (151-300)

- [151: How do you build a model cascade?](#151-how-do-you-build-a-model-cascade)
- [152: What is the downside of a cascade?](#152-what-is-the-downside-of-a-cascade)
- [153: How do you decide which requests go to which model in a router?](#153-how-do-you-decide-which-requests-go-to-which-model-in-a-router)
- [154: How do you measure TTFT in code?](#154-how-do-you-measure-ttft-in-code)
- [155: How do you measure TPOT or output speed in code?](#155-how-do-you-measure-tpot-or-output-speed-in-code)
- [156: How do you load test an LLM endpoint?](#156-how-do-you-load-test-an-llm-endpoint)
- [157: Why must load tests use realistic prompt and output lengths?](#157-why-must-load-tests-use-realistic-prompt-and-output-lengths)
- [158: How do you measure your prompt cache hit rate?](#158-how-do-you-measure-your-prompt-cache-hit-rate)
- [159: How do you keep dynamic content from breaking the prompt cache?](#159-how-do-you-keep-dynamic-content-from-breaking-the-prompt-cache)
- [160: How many cache breakpoints can you set with Anthropic and why use more than one?](#160-how-many-cache-breakpoints-can-you-set-with-anthropic-and-why-use-more-than-one)
- [161: Is there a minimum prompt size for caching?](#161-is-there-a-minimum-prompt-size-for-caching)
- [162: How do you work out if Anthropic's 5-minute cache pays off?](#162-how-do-you-work-out-if-anthropics-5-minute-cache-pays-off)
- [163: When is the 1-hour cache worth it?](#163-when-is-the-1-hour-cache-worth-it)
- [164: What does prompt_cache_key do in the OpenAI API?](#164-what-does-prompt_cache_key-do-in-the-openai-api)
- [165: What is the difference between implicit and explicit caching in Gemini?](#165-what-is-the-difference-between-implicit-and-explicit-caching-in-gemini)
- [166: Is the prompt cache shared between different customers?](#166-is-the-prompt-cache-shared-between-different-customers)
- [167: How do you choose the similarity threshold for a semantic cache?](#167-how-do-you-choose-the-similarity-threshold-for-a-semantic-cache)
- [168: How do you handle stale answers in a response cache?](#168-how-do-you-handle-stale-answers-in-a-response-cache)
- [169: Why is response caching hard for personalized answers?](#169-why-is-response-caching-hard-for-personalized-answers)
- [170: How does the OpenAI Batch API work?](#170-how-does-the-openai-batch-api-work)
- [171: How does the Anthropic Message Batches API work?](#171-how-does-the-anthropic-message-batches-api-work)
- [172: Can you combine batch discounts with prompt caching?](#172-can-you-combine-batch-discounts-with-prompt-caching)
- [173: How do you handle partial failures in a batch job?](#173-how-do-you-handle-partial-failures-in-a-batch-job)
- [174: How do you read rate limit headers?](#174-how-do-you-read-rate-limit-headers)
- [175: How do you build a client-side rate limiter for LLM calls?](#175-how-do-you-build-a-client-side-rate-limiter-for-llm-calls)
- [176: How do you limit concurrency when calling an LLM for many items?](#176-how-do-you-limit-concurrency-when-calling-an-llm-for-many-items)
- [177: How do you spread load across several providers or regions?](#177-how-do-you-spread-load-across-several-providers-or-regions)
- [178: How do you add a fallback when the main model fails?](#178-how-do-you-add-a-fallback-when-the-main-model-fails)
- [179: What are hedged requests?](#179-what-are-hedged-requests)
- [180: Why should you use separate timeouts for TTFT and total time?](#180-why-should-you-use-separate-timeouts-for-ttft-and-total-time)
- [181: How do you stream LLM output from your backend to the browser?](#181-how-do-you-stream-llm-output-from-your-backend-to-the-browser)
- [182: Why might streaming not work in production even though it works locally?](#182-why-might-streaming-not-work-in-production-even-though-it-works-locally)
- [183: How do you stream structured output like JSON?](#183-how-do-you-stream-structured-output-like-json)
- [184: How does streaming work with tool calls?](#184-how-does-streaming-work-with-tool-calls)
- [185: What are UI techniques to hide LLM latency?](#185-what-are-ui-techniques-to-hide-llm-latency)
- [186: How does reranking help with RAG cost?](#186-how-does-reranking-help-with-rag-cost)
- [187: How does chunk size affect RAG cost and quality?](#187-how-does-chunk-size-affect-rag-cost-and-quality)
- [188: Is it cheaper to put the whole document in the context or use RAG?](#188-is-it-cheaper-to-put-the-whole-document-in-the-context-or-use-rag)
- [189: What is query rewriting in RAG and what does it cost?](#189-what-is-query-rewriting-in-rag-and-what-does-it-cost)
- [190: What is contextual compression in RAG?](#190-what-is-contextual-compression-in-rag)
- [191: Should you cache retrieval results?](#191-should-you-cache-retrieval-results)
- [192: How do you embed many documents cheaply?](#192-how-do-you-embed-many-documents-cheaply)
- [193: How do you reduce the token cost of tool results in an agent?](#193-how-do-you-reduce-the-token-cost-of-tool-results-in-an-agent)
- [194: How do parallel tool calls reduce latency?](#194-how-do-parallel-tool-calls-reduce-latency)
- [195: What is the plan-and-execute pattern and how does it save money?](#195-what-is-the-plan-and-execute-pattern-and-how-does-it-save-money)
- [196: How do you detect and stop an agent stuck in a loop?](#196-how-do-you-detect-and-stop-an-agent-stuck-in-a-loop)
- [197: How do sub-agents help with cost?](#197-how-do-sub-agents-help-with-cost)
- [198: Why is clearing old tool results from the context useful?](#198-why-is-clearing-old-tool-results-from-the-context-useful)
- [199: Why can connecting many MCP servers make each request more expensive?](#199-why-can-connecting-many-mcp-servers-make-each-request-more-expensive)
- [200: Does structured output make requests slower?](#200-does-structured-output-make-requests-slower)
- [201: What is the difference between JSON mode and schema-based structured output?](#201-what-is-the-difference-between-json-mode-and-schema-based-structured-output)
- [202: How can you cut output tokens without hurting answer quality?](#202-how-can-you-cut-output-tokens-without-hurting-answer-quality)
- [203: Why is asking for IDs instead of full text a good trick?](#203-why-is-asking-for-ids-instead-of-full-text-a-good-trick)
- [204: Why should code assistants output diffs instead of whole files?](#204-why-should-code-assistants-output-diffs-instead-of-whole-files)
- [205: What is the verbosity parameter?](#205-what-is-the-verbosity-parameter)
- [206: How do you choose the right reasoning effort for a task?](#206-how-do-you-choose-the-right-reasoning-effort-for-a-task)
- [207: How do you see how many reasoning tokens were used?](#207-how-do-you-see-how-many-reasoning-tokens-were-used)
- [208: When is a non-reasoning model with a "think step by step" prompt better than a reasoning model?](#208-when-is-a-non-reasoning-model-with-a-think-step-by-step-prompt-better-than-a-reasoning-model)
- [209: What are Predicted Outputs?](#209-what-are-predicted-outputs)
- [210: How do you attribute LLM costs to features and customers?](#210-how-do-you-attribute-llm-costs-to-features-and-customers)
- [211: What should a basic LLM cost dashboard show?](#211-what-should-a-basic-llm-cost-dashboard-show)
- [212: How do you implement per-user token quotas?](#212-how-do-you-implement-per-user-token-quotas)
- [213: How do LLM costs affect how you price your own product?](#213-how-do-llm-costs-affect-how-you-price-your-own-product)
- [214: What is gross margin and why does it matter for AI products?](#214-what-is-gross-margin-and-why-does-it-matter-for-ai-products)
- [215: How do you stop free users from running up large LLM costs?](#215-how-do-you-stop-free-users-from-running-up-large-llm-costs)
- [216: What is a "denial of wallet" attack?](#216-what-is-a-denial-of-wallet-attack)
- [217: How can prompt injection increase your costs?](#217-how-can-prompt-injection-increase-your-costs)
- [218: What should a response cache key include?](#218-what-should-a-response-cache-key-include)
- [219: Why should you version your prompts?](#219-why-should-you-version-your-prompts)
- [220: How do you catch cost regressions before deploy?](#220-how-do-you-catch-cost-regressions-before-deploy)
- [221: How do you A/B test a cheaper model?](#221-how-do-you-ab-test-a-cheaper-model)
- [222: What is LLM-as-a-judge and what does it cost?](#222-what-is-llm-as-a-judge-and-what-does-it-cost)
- [223: How do you keep evaluation costs under control?](#223-how-do-you-keep-evaluation-costs-under-control)
- [224: Why can the same open model have different prices and speeds on different providers?](#224-why-can-the-same-open-model-have-different-prices-and-speeds-on-different-providers)
- [225: How can provider quantization affect quality?](#225-how-can-provider-quantization-affect-quality)
- [226: What are the pros and cons of using a model through a cloud platform (Bedrock, Azure, Vertex AI) instead of directly?](#226-what-are-the-pros-and-cons-of-using-a-model-through-a-cloud-platform-bedrock-azure-vertex-ai-instead-of-directly)
- [227: What is cross-region inference?](#227-what-is-cross-region-inference)
- [228: How do you size provisioned throughput?](#228-how-do-you-size-provisioned-throughput)
- [229: What is spillover in provisioned deployments?](#229-what-is-spillover-in-provisioned-deployments)
- [230: What is vLLM?](#230-what-is-vllm)
- [231: How do you start an OpenAI-compatible server with vLLM?](#231-how-do-you-start-an-openai-compatible-server-with-vllm)
- [232: What GPUs are common for LLM inference?](#232-what-gpus-are-common-for-llm-inference)
- [233: How do you estimate how much GPU memory a model needs for its weights?](#233-how-do-you-estimate-how-much-gpu-memory-a-model-needs-for-its-weights)
- [234: Why is GPU memory left after the weights important?](#234-why-is-gpu-memory-left-after-the-weights-important)
- [235: How should you autoscale a self-hosted LLM service?](#235-how-should-you-autoscale-a-self-hosted-llm-service)
- [236: What are the trade-offs of scaling a GPU deployment to zero?](#236-what-are-the-trade-offs-of-scaling-a-gpu-deployment-to-zero)
- [237: Can you use spot or preemptible GPUs for LLM work?](#237-can-you-use-spot-or-preemptible-gpus-for-llm-work)
- [238: What are Ollama and llama.cpp good for?](#238-what-are-ollama-and-llamacpp-good-for)
- [239: When does running a model on the user's device make sense?](#239-when-does-running-a-model-on-the-users-device-make-sense)
- [240: What is a checklist for lowering TTFT?](#240-what-is-a-checklist-for-lowering-ttft)
- [241: What is a checklist for lowering total generation time?](#241-what-is-a-checklist-for-lowering-total-generation-time)
- [242: What is a latency budget?](#242-what-is-a-latency-budget)
- [243: How does a voice assistant pipeline affect latency?](#243-how-does-a-voice-assistant-pipeline-affect-latency)
- [244: When are speech-to-speech realtime APIs worth their cost?](#244-when-are-speech-to-speech-realtime-apis-worth-their-cost)
- [245: How can you precompute LLM answers to cut latency?](#245-how-can-you-precompute-llm-answers-to-cut-latency)
- [246: How can splitting a long answer into parallel calls help?](#246-how-can-splitting-a-long-answer-into-parallel-calls-help)
- [247: Why should you reuse your SDK client instead of creating a new one per request?](#247-why-should-you-reuse-your-sdk-client-instead-of-creating-a-new-one-per-request)
- [248: What should you watch for when streaming from serverless functions?](#248-what-should-you-watch-for-when-streaming-from-serverless-functions)
- [249: Should you use SSE or WebSockets for LLM streaming?](#249-should-you-use-sse-or-websockets-for-llm-streaming)
- [250: Does using stored conversation state (like previous_response_id) save tokens?](#250-does-using-stored-conversation-state-like-previous_response_id-save-tokens)
- [251: What is context compaction?](#251-what-is-context-compaction)
- [252: How does a long-term memory system save tokens?](#252-how-does-a-long-term-memory-system-save-tokens)
- [253: When can you replace an LLM call with embeddings?](#253-when-can-you-replace-an-llm-call-with-embeddings)
- [254: When should you not use an LLM at all?](#254-when-should-you-not-use-an-llm-at-all)
- [255: How do moderation and guardrail checks affect latency and cost?](#255-how-do-moderation-and-guardrail-checks-affect-latency-and-cost)
- [256: How do validation retries affect cost?](#256-how-do-validation-retries-affect-cost)
- [257: Why compare models by cost per task and not cost per token?](#257-why-compare-models-by-cost-per-task-and-not-cost-per-token)
- [258: Where can you find independent data on model speed and price?](#258-where-can-you-find-independent-data-on-model-speed-and-price)
- [259: How do you monitor LLM latency from your users' point of view?](#259-how-do-you-monitor-llm-latency-from-your-users-point-of-view)
- [260: What is an SLO for an LLM feature?](#260-what-is-an-slo-for-an-llm-feature)
- [261: What is a circuit breaker and why use it with LLM providers?](#261-what-is-a-circuit-breaker-and-why-use-it-with-llm-providers)
- [262: What is request deduplication for LLM calls?](#262-what-is-request-deduplication-for-llm-calls)
- [263: Why does idempotency matter when retrying agent steps?](#263-why-does-idempotency-matter-when-retrying-agent-steps)
- [264: Can you put LLM-generated content behind a CDN?](#264-can-you-put-llm-generated-content-behind-a-cdn)
- [265: How do you keep the prompt cache warm when you run many app servers?](#265-how-do-you-keep-the-prompt-cache-warm-when-you-run-many-app-servers)
- [266: How do you design prompts for multi-tenant apps so caching works?](#266-how-do-you-design-prompts-for-multi-tenant-apps-so-caching-works)
- [267: How are image tokens calculated, roughly?](#267-how-are-image-tokens-calculated-roughly)
- [268: How are PDF inputs priced?](#268-how-are-pdf-inputs-priced)
- [269: How is video input usually priced?](#269-how-is-video-input-usually-priced)
- [270: What is map-reduce summarization and what does it cost?](#270-what-is-map-reduce-summarization-and-what-does-it-cost)
- [271: What is the "refine" method for long documents and how does it compare to map-reduce?](#271-what-is-the-refine-method-for-long-documents-and-how-does-it-compare-to-map-reduce)
- [272: What is "extract then reason"?](#272-what-is-extract-then-reason)
- [273: How can you choose the number of RAG chunks dynamically?](#273-how-can-you-choose-the-number-of-rag-chunks-dynamically)
- [274: How do hosted tools like web search add cost?](#274-how-do-hosted-tools-like-web-search-add-cost)
- [275: What storage costs come with hosted vector stores and file search?](#275-what-storage-costs-come-with-hosted-vector-stores-and-file-search)
- [276: Should you log every full prompt and response?](#276-should-you-log-every-full-prompt-and-response)
- [277: How do you get token usage when streaming with OpenAI?](#277-how-do-you-get-token-usage-when-streaming-with-openai)
- [278: How do you get token usage when streaming with Anthropic?](#278-how-do-you-get-token-usage-when-streaming-with-anthropic)
- [279: Why should you check prompt size before sending a request?](#279-why-should-you-check-prompt-size-before-sending-a-request)
- [280: How do you trim input to fit a token budget?](#280-how-do-you-trim-input-to-fit-a-token-budget)
- [281: What is the "lost in the middle" problem and why does it matter for cost?](#281-what-is-the-lost-in-the-middle-problem-and-why-does-it-matter-for-cost)
- [282: What are common examples of the cost vs latency trade-off?](#282-what-are-common-examples-of-the-cost-vs-latency-trade-off)
- [283: How would you approach cutting the cost of an existing LLM feature in half?](#283-how-would-you-approach-cutting-the-cost-of-an-existing-llm-feature-in-half)
- [284: How do you split tokens in a request to see where the cost comes from?](#284-how-do-you-split-tokens-in-a-request-to-see-where-the-cost-comes-from)
- [285: What is the cost of tokens that are never cached because they change each time?](#285-what-is-the-cost-of-tokens-that-are-never-cached-because-they-change-each-time)
- [286: How do you handle very long user inputs in a chat app?](#286-how-do-you-handle-very-long-user-inputs-in-a-chat-app)
- [287: How does the Vercel AI SDK help with cost and latency work?](#287-how-does-the-vercel-ai-sdk-help-with-cost-and-latency-work)
- [288: What is OpenRouter and how does it relate to cost?](#288-what-is-openrouter-and-how-does-it-relate-to-cost)
- [289: How do you compare TTFT across providers fairly?](#289-how-do-you-compare-ttft-across-providers-fairly)
- [290: How can you make tool descriptions cheaper without breaking tool use?](#290-how-can-you-make-tool-descriptions-cheaper-without-breaking-tool-use)
- [291: What is a tool search or dynamic tool loading feature?](#291-what-is-a-tool-search-or-dynamic-tool-loading-feature)
- [292: How do you budget the context window in a RAG chat app?](#292-how-do-you-budget-the-context-window-in-a-rag-chat-app)
- [293: Why do you need a price table in your code or config?](#293-why-do-you-need-a-price-table-in-your-code-or-config)
- [294: How do you calculate cost when some input tokens are cached?](#294-how-do-you-calculate-cost-when-some-input-tokens-are-cached)
- [295: Why might your cost dashboard not match the provider's invoice?](#295-why-might-your-cost-dashboard-not-match-the-providers-invoice)
- [296: How do you forecast LLM costs for next quarter?](#296-how-do-you-forecast-llm-costs-for-next-quarter)
- [297: When does it make sense to use a different model for each step of a pipeline?](#297-when-does-it-make-sense-to-use-a-different-model-for-each-step-of-a-pipeline)
- [298: How do you safely move a feature to a cheaper model?](#298-how-do-you-safely-move-a-feature-to-a-cheaper-model)
- [299: What are good defaults for a new LLM feature to avoid cost surprises?](#299-what-are-good-defaults-for-a-new-llm-feature-to-avoid-cost-surprises)
- [300: What questions should you ask before choosing between real-time and batch processing?](#300-what-questions-should-you-ask-before-choosing-between-real-time-and-batch-processing)

### Advanced Questions (301-450)

- [301: What are the prefill and decode phases of LLM inference?](#301-what-are-the-prefill-and-decode-phases-of-llm-inference)
- [302: Why is prefill compute-bound and decode memory-bandwidth-bound?](#302-why-is-prefill-compute-bound-and-decode-memory-bandwidth-bound)
- [303: What is arithmetic intensity and why does it matter for LLM serving?](#303-what-is-arithmetic-intensity-and-why-does-it-matter-for-llm-serving)
- [304: What is the KV cache?](#304-what-is-the-kv-cache)
- [305: How do you estimate the size of the KV cache?](#305-how-do-you-estimate-the-size-of-the-kv-cache)
- [306: How do Grouped-Query Attention (GQA) and Multi-Query Attention (MQA) reduce cost?](#306-how-do-grouped-query-attention-gqa-and-multi-query-attention-mqa-reduce-cost)
- [307: What is Multi-head Latent Attention (MLA)?](#307-what-is-multi-head-latent-attention-mla)
- [308: What is sliding window attention and how does it affect cost?](#308-what-is-sliding-window-attention-and-how-does-it-affect-cost)
- [309: Why does attention cost grow faster than linearly with context length?](#309-why-does-attention-cost-grow-faster-than-linearly-with-context-length)
- [310: What is FlashAttention?](#310-what-is-flashattention)
- [311: What is the difference between static batching and continuous batching?](#311-what-is-the-difference-between-static-batching-and-continuous-batching)
- [312: What is PagedAttention?](#312-what-is-pagedattention)
- [313: What is automatic prefix caching in self-hosted engines?](#313-what-is-automatic-prefix-caching-in-self-hosted-engines)
- [314: What is chunked prefill?](#314-what-is-chunked-prefill)
- [315: What is prefill-decode interference?](#315-what-is-prefill-decode-interference)
- [316: What is disaggregated prefill and decode serving?](#316-what-is-disaggregated-prefill-and-decode-serving)
- [317: What is speculative decoding?](#317-what-is-speculative-decoding)
- [318: What decides how much speculative decoding helps?](#318-what-decides-how-much-speculative-decoding-helps)
- [319: What are EAGLE, Medusa and n-gram speculation?](#319-what-are-eagle-medusa-and-n-gram-speculation)
- [320: When can speculative decoding make throughput worse?](#320-when-can-speculative-decoding-make-throughput-worse)
- [321: What is tensor parallelism?](#321-what-is-tensor-parallelism)
- [322: What is pipeline parallelism?](#322-what-is-pipeline-parallelism)
- [323: What is a Mixture of Experts (MoE) model and how does it affect cost?](#323-what-is-a-mixture-of-experts-moe-model-and-how-does-it-affect-cost)
- [324: What is expert parallelism?](#324-what-is-expert-parallelism)
- [325: Why do MoE models need large batch sizes to be cost-efficient?](#325-why-do-moe-models-need-large-batch-sizes-to-be-cost-efficient)
- [326: What quantization formats are common for inference?](#326-what-quantization-formats-are-common-for-inference)
- [327: What is the difference between weight-only and weight-and-activation quantization?](#327-what-is-the-difference-between-weight-only-and-weight-and-activation-quantization)
- [328: What is KV cache quantization?](#328-what-is-kv-cache-quantization)
- [329: How do you check if quantization hurt quality?](#329-how-do-you-check-if-quantization-hurt-quality)
- [330: How do you estimate the upper limit of decode speed for one request?](#330-how-do-you-estimate-the-upper-limit-of-decode-speed-for-one-request)
- [331: How does batch size affect TPOT and throughput in self-hosted serving?](#331-how-does-batch-size-affect-tpot-and-throughput-in-self-hosted-serving)
- [332: What is goodput?](#332-what-is-goodput)
- [333: What vLLM settings affect latency and throughput the most?](#333-what-vllm-settings-affect-latency-and-throughput-the-most)
- [334: What happens when the KV cache runs out of memory during serving?](#334-what-happens-when-the-kv-cache-runs-out-of-memory-during-serving)
- [335: Why is long-context serving expensive even with a good engine?](#335-why-is-long-context-serving-expensive-even-with-a-good-engine)
- [336: What are CUDA graphs and why do serving engines use them?](#336-what-are-cuda-graphs-and-why-do-serving-engines-use-them)
- [337: How do vLLM, SGLang and TensorRT-LLM compare?](#337-how-do-vllm-sglang-and-tensorrt-llm-compare)
- [338: How do you serve many LoRA fine-tunes cheaply?](#338-how-do-you-serve-many-lora-fine-tunes-cheaply)
- [339: How does constrained decoding for structured output affect speed?](#339-how-does-constrained-decoding-for-structured-output-affect-speed)
- [340: How do you calculate the cost per million tokens when self-hosting?](#340-how-do-you-calculate-the-cost-per-million-tokens-when-self-hosting)
- [341: How do you decide if self-hosting is cheaper than an API?](#341-how-do-you-decide-if-self-hosting-is-cheaper-than-an-api)
- [342: Why is utilization the most important number in self-hosting economics?](#342-why-is-utilization-the-most-important-number-in-self-hosting-economics)
- [343: What hidden costs come with self-hosting LLMs?](#343-what-hidden-costs-come-with-self-hosting-llms)
- [344: What is KV-cache-aware routing?](#344-what-is-kv-cache-aware-routing)
- [345: Why does session affinity help self-hosted chat performance?](#345-why-does-session-affinity-help-self-hosted-chat-performance)
- [346: How do you speed up model loading for autoscaling?](#346-how-do-you-speed-up-model-loading-for-autoscaling)
- [347: Can you run several models on one GPU?](#347-can-you-run-several-models-on-one-gpu)
- [348: When is CPU inference a reasonable choice?](#348-when-is-cpu-inference-a-reasonable-choice)
- [349: Why are some providers, like Groq and Cerebras, much faster per request?](#349-why-are-some-providers-like-groq-and-cerebras-much-faster-per-request)
- [350: What other accelerators besides NVIDIA GPUs are used for inference?](#350-what-other-accelerators-besides-nvidia-gpus-are-used-for-inference)
- [351: Why are cached input tokens so much cheaper for providers to serve?](#351-why-are-cached-input-tokens-so-much-cheaper-for-providers-to-serve)
- [352: Why can providers offer batch processing at about half price?](#352-why-can-providers-offer-batch-processing-at-about-half-price)
- [353: Why do providers charge more for very long contexts?](#353-why-do-providers-charge-more-for-very-long-contexts)
- [354: Why do providers have rate limits even for paying customers?](#354-why-do-providers-have-rate-limits-even-for-paying-customers)
- [355: What causes tail latency in hosted LLM APIs?](#355-what-causes-tail-latency-in-hosted-llm-apis)
- [356: What are the costs and risks of hedged requests at scale?](#356-what-are-the-costs-and-risks-of-hedged-requests-at-scale)
- [357: How would you design a latency budget for a RAG chatbot with a 1.5-second TTFT target?](#357-how-would-you-design-a-latency-budget-for-a-rag-chatbot-with-a-15-second-ttft-target)
- [358: Scenario: your chatbot's TTFT is 6 seconds. How do you find and fix the cause?](#358-scenario-your-chatbots-ttft-is-6-seconds-how-do-you-find-and-fix-the-cause)
- [359: Scenario: each agent task costs $2 and needs to cost $0.30. What do you do?](#359-scenario-each-agent-task-costs-2-and-needs-to-cost-030-what-do-you-do)
- [360: Scenario: you need to classify 10 million documents once. What is the cheapest reliable approach?](#360-scenario-you-need-to-classify-10-million-documents-once-what-is-the-cheapest-reliable-approach)
- [361: Scenario: a code autocomplete feature must respond in under 200 ms. How do you design it?](#361-scenario-a-code-autocomplete-feature-must-respond-in-under-200-ms-how-do-you-design-it)
- [362: Scenario: a voice agent must start speaking within 800 ms after the user stops talking. How?](#362-scenario-a-voice-agent-must-start-speaking-within-800-ms-after-the-user-stops-talking-how)
- [363: Scenario: in a multi-tenant SaaS, one tenant uses 60% of your LLM budget. What do you do?](#363-scenario-in-a-multi-tenant-saas-one-tenant-uses-60-of-your-llm-budget-what-do-you-do)
- [364: Scenario: your prompt cache hit rate is only 10% even though all requests share a long system prompt. Why?](#364-scenario-your-prompt-cache-hit-rate-is-only-10-even-though-all-requests-share-a-long-system-prompt-why)
- [365: Scenario: your main provider's latency suddenly doubles. How should your system respond?](#365-scenario-your-main-providers-latency-suddenly-doubles-how-should-your-system-respond)
- [366: Scenario: users ask many questions about the same 500-page contract. How do you keep it cheap and fast?](#366-scenario-users-ask-many-questions-about-the-same-500-page-contract-how-do-you-keep-it-cheap-and-fast)
- [367: Scenario: one user sends thousands of requests per hour. How do you protect the system?](#367-scenario-one-user-sends-thousands-of-requests-per-hour-how-do-you-protect-the-system)
- [368: Scenario: you want to move from a closed flagship model to a self-hosted open model. What is your plan?](#368-scenario-you-want-to-move-from-a-closed-flagship-model-to-a-self-hosted-open-model-what-is-your-plan)
- [369: Scenario: a nightly batch job sometimes does not finish before the morning. What can you change?](#369-scenario-a-nightly-batch-job-sometimes-does-not-finish-before-the-morning-what-can-you-change)
- [370: Scenario: a structured extraction job fails validation 15% of the time. How do you lower cost?](#370-scenario-a-structured-extraction-job-fails-validation-15-of-the-time-how-do-you-lower-cost)
- [371: Scenario: a support app summarizes long chat threads for agents. How do you keep cost and latency low?](#371-scenario-a-support-app-summarizes-long-chat-threads-for-agents-how-do-you-keep-cost-and-latency-low)
- [372: Scenario: you want an AI summary at the top of every search results page. How do you make it affordable?](#372-scenario-you-want-an-ai-summary-at-the-top-of-every-search-results-page-how-do-you-make-it-affordable)
- [373: Scenario: you must generate descriptions for 2 million products. How do you plan cost?](#373-scenario-you-must-generate-descriptions-for-2-million-products-how-do-you-plan-cost)
- [374: Scenario: you need to answer questions over a 2-million-token codebase. Long context or RAG?](#374-scenario-you-need-to-answer-questions-over-a-2-million-token-codebase-long-context-or-rag)
- [375: Scenario: a translation app is much more expensive for some languages. How do you handle it?](#375-scenario-a-translation-app-is-much-more-expensive-for-some-languages-how-do-you-handle-it)
- [376: Scenario: a document pipeline processes scanned invoices with images. How do you reduce cost?](#376-scenario-a-document-pipeline-processes-scanned-invoices-with-images-how-do-you-reduce-cost)
- [377: Scenario: you must moderate every message in a busy chat app in real time. What is the setup?](#377-scenario-you-must-moderate-every-message-in-a-busy-chat-app-in-real-time-what-is-the-setup)
- [378: Scenario: an email assistant must handle millions of emails a day on a small budget. How?](#378-scenario-an-email-assistant-must-handle-millions-of-emails-a-day-on-a-small-budget-how)
- [379: How can you estimate a model's confidence to drive a cascade?](#379-how-can-you-estimate-a-models-confidence-to-drive-a-cascade)
- [380: How can log probabilities help with cost?](#380-how-can-log-probabilities-help-with-cost)
- [381: How do learned routers work?](#381-how-do-learned-routers-work)
- [382: What are failure modes of model routing?](#382-what-are-failure-modes-of-model-routing)
- [383: What security risks does a semantic cache add?](#383-what-security-risks-does-a-semantic-cache-add)
- [384: How does a semantic cache scale to millions of entries?](#384-how-does-a-semantic-cache-scale-to-millions-of-entries)
- [385: How do you keep cached answers correct when the underlying RAG data changes?](#385-how-do-you-keep-cached-answers-correct-when-the-underlying-rag-data-changes)
- [386: What is KV cache offloading?](#386-what-is-kv-cache-offloading)
- [387: Why would you keep KV cache for a conversation across turns?](#387-why-would-you-keep-kv-cache-for-a-conversation-across-turns)
- [388: How do providers implement prompt caching, roughly?](#388-how-do-providers-implement-prompt-caching-roughly)
- [389: Why are LLM outputs sometimes not the same even at temperature 0?](#389-why-are-llm-outputs-sometimes-not-the-same-even-at-temperature-0)
- [390: When is fine-tuning cheaper than prompting, in numbers?](#390-when-is-fine-tuning-cheaper-than-prompting-in-numbers)
- [391: What are the risks of replacing a big model with a small fine-tuned one?](#391-what-are-the-risks-of-replacing-a-big-model-with-a-small-fine-tuned-one)
- [392: Should you use a bigger model quantized or a smaller model at full precision?](#392-should-you-use-a-bigger-model-quantized-or-a-smaller-model-at-full-precision)
- [393: What is pruning and does it help inference cost?](#393-what-is-pruning-and-does-it-help-inference-cost)
- [394: How does tokenizer vocabulary size affect cost?](#394-how-does-tokenizer-vocabulary-size-affect-cost)
- [395: What is multi-token prediction and how can it speed up inference?](#395-what-is-multi-token-prediction-and-how-can-it-speed-up-inference)
- [396: How do reasoning models change capacity planning?](#396-how-do-reasoning-models-change-capacity-planning)
- [397: What is test-time compute scaling and what does it cost?](#397-what-is-test-time-compute-scaling-and-what-does-it-cost)
- [398: How can sampling several answers in parallel be cheaper than it looks?](#398-how-can-sampling-several-answers-in-parallel-be-cheaper-than-it-looks)
- [399: Why is predicting output length useful for scheduling?](#399-why-is-predicting-output-length-useful-for-scheduling)
- [400: How do you give fair service to many tenants on a self-hosted LLM?](#400-how-do-you-give-fair-service-to-many-tenants-on-a-self-hosted-llm)
- [401: What is admission control and load shedding for LLM services?](#401-what-is-admission-control-and-load-shedding-for-llm-services)
- [402: How do you design backpressure for an LLM pipeline?](#402-how-do-you-design-backpressure-for-an-llm-pipeline)
- [403: How do you enforce a rate limit across many app servers?](#403-how-do-you-enforce-a-rate-limit-across-many-app-servers)
- [404: How do you rate limit by tokens when you do not know the output length in advance?](#404-how-do-you-rate-limit-by-tokens-when-you-do-not-know-the-output-length-in-advance)
- [405: How do you account correctly for cached, reasoning and batch tokens in cost reports?](#405-how-do-you-account-correctly-for-cached-reasoning-and-batch-tokens-in-cost-reports)
- [406: How do you reconcile your internal cost tracking with provider invoices?](#406-how-do-you-reconcile-your-internal-cost-tracking-with-provider-invoices)
- [407: What is FinOps for AI, and what are showback and chargeback?](#407-what-is-finops-for-ai-and-what-are-showback-and-chargeback)
- [408: How can you negotiate lower LLM prices?](#408-how-can-you-negotiate-lower-llm-prices)
- [409: What are the trade-offs of a multi-provider strategy?](#409-what-are-the-trade-offs-of-a-multi-provider-strategy)
- [410: How do guardrails interact with streaming?](#410-how-do-guardrails-interact-with-streaming)
- [411: How can prompt injection be combined with cost attacks against agents?](#411-how-can-prompt-injection-be-combined-with-cost-attacks-against-agents)
- [412: How do data residency and privacy rules affect cost and latency?](#412-how-do-data-residency-and-privacy-rules-affect-cost-and-latency)
- [413: How do you benchmark LLM serving performance correctly?](#413-how-do-you-benchmark-llm-serving-performance-correctly)
- [414: What are common mistakes in LLM performance benchmarks?](#414-what-are-common-mistakes-in-llm-performance-benchmarks)
- [415: How can Little's Law help with LLM capacity planning?](#415-how-can-littles-law-help-with-llm-capacity-planning)
- [416: How do you estimate how many GPUs you need for a self-hosted model?](#416-how-do-you-estimate-how-many-gpus-you-need-for-a-self-hosted-model)
- [417: Why does more context often not mean better answers?](#417-why-does-more-context-often-not-mean-better-answers)
- [418: What are the trade-offs of on-device models like Chrome's built-in AI?](#418-what-are-the-trade-offs-of-on-device-models-like-chromes-built-in-ai)
- [419: How do you design a hybrid on-device and cloud setup?](#419-how-do-you-design-a-hybrid-on-device-and-cloud-setup)
- [420: How do energy use and carbon fit into LLM cost decisions?](#420-how-do-energy-use-and-carbon-fit-into-llm-cost-decisions)
- [421: How would you implement compaction for a long-running agent?](#421-how-would-you-implement-compaction-for-a-long-running-agent)
- [422: How should you design tool outputs to be token-efficient?](#422-how-should-you-design-tool-outputs-to-be-token-efficient)
- [423: Why should agent history be append-only for good caching?](#423-why-should-agent-history-be-append-only-for-good-caching)
- [424: How does changing the tool list mid-conversation affect caching?](#424-how-does-changing-the-tool-list-mid-conversation-affect-caching)
- [425: How do you decide between a cheaper model with more retries and a stronger model with fewer?](#425-how-do-you-decide-between-a-cheaper-model-with-more-retries-and-a-stronger-model-with-fewer)
- [426: How does the choice between streaming and non-streaming affect server resources?](#426-how-does-the-choice-between-streaming-and-non-streaming-affect-server-resources)
- [427: How do you handle the cost of failed or cancelled streams?](#427-how-do-you-handle-the-cost-of-failed-or-cancelled-streams)
- [428: How does the HTTP layer affect LLM latency at scale?](#428-how-does-the-http-layer-affect-llm-latency-at-scale)
- [429: What is speculative or eager execution in an LLM app (not speculative decoding)?](#429-what-is-speculative-or-eager-execution-in-an-llm-app-not-speculative-decoding)
- [430: How do you serve the same prompt to many users with minimal cost, like a daily digest?](#430-how-do-you-serve-the-same-prompt-to-many-users-with-minimal-cost-like-a-daily-digest)
- [431: How do you set max_tokens correctly for reasoning models?](#431-how-do-you-set-max_tokens-correctly-for-reasoning-models)
- [432: What metrics would you alert on for an LLM platform?](#432-what-metrics-would-you-alert-on-for-an-llm-platform)
- [433: How do you run a cost and latency review of a new LLM feature before launch?](#433-how-do-you-run-a-cost-and-latency-review-of-a-new-llm-feature-before-launch)
- [434: How do you explain cost and latency trade-offs to a product manager?](#434-how-do-you-explain-cost-and-latency-trade-offs-to-a-product-manager)
- [435: What is the cost impact of a bigger context window on a self-hosted server even if prompts are short?](#435-what-is-the-cost-impact-of-a-bigger-context-window-on-a-self-hosted-server-even-if-prompts-are-short)
- [436: Why might you run separate deployments for short and long requests?](#436-why-might-you-run-separate-deployments-for-short-and-long-requests)
- [437: How do LLM costs scale with users for a chat product, and what grows faster than expected?](#437-how-do-llm-costs-scale-with-users-for-a-chat-product-and-what-grows-faster-than-expected)
- [438: What is the role of a "small model first" architecture in large systems?](#438-what-is-the-role-of-a-small-model-first-architecture-in-large-systems)
- [439: How do you handle provider price drops or new cheaper models?](#439-how-do-you-handle-provider-price-drops-or-new-cheaper-models)
- [440: Why can a cheaper per-token model increase total cost in agent workflows?](#440-why-can-a-cheaper-per-token-model-increase-total-cost-in-agent-workflows)
- [441: How do you set a per-request cost limit in an agent framework?](#441-how-do-you-set-a-per-request-cost-limit-in-an-agent-framework)
- [442: How does output streaming interact with structured output and tool calls for latency?](#442-how-does-output-streaming-interact-with-structured-output-and-tool-calls-for-latency)
- [443: What are typical latency differences between provider tiers of the same model family?](#443-what-are-typical-latency-differences-between-provider-tiers-of-the-same-model-family)
- [444: How would you reduce the cost of an LLM evaluation pipeline that runs on every pull request?](#444-how-would-you-reduce-the-cost-of-an-llm-evaluation-pipeline-that-runs-on-every-pull-request)
- [445: How do you approach latency for a multi-step RAG agent that calls the LLM 5 times?](#445-how-do-you-approach-latency-for-a-multi-step-rag-agent-that-calls-the-llm-5-times)
- [446: What is the effect of system prompt changes on a large, cached production workload?](#446-what-is-the-effect-of-system-prompt-changes-on-a-large-cached-production-workload)
- [447: How can you use offline precomputation to lower RAG query costs?](#447-how-can-you-use-offline-precomputation-to-lower-rag-query-costs)
- [448: How do you know if your optimizations are worth the engineering time?](#448-how-do-you-know-if-your-optimizations-are-worth-the-engineering-time)
- [449: What are the most effective cost levers, in rough order of impact?](#449-what-are-the-most-effective-cost-levers-in-rough-order-of-impact)
- [450: What are the most effective latency levers, in rough order of impact?](#450-what-are-the-most-effective-latency-levers-in-rough-order-of-impact)

---

# Easy Questions (1-150)

## 1: What is a token?

A token is the unit of text a model reads and writes. It is usually a piece of a word, a whole short word, a number or a punctuation mark. In English, one token is about 4 characters or about three quarters of a word on average. Providers count and bill everything in tokens, so tokens are the base unit for both cost and latency.

## 2: Why do LLM providers charge per token and not per request?

The work the model does grows with the number of tokens it reads and writes. A request with 50 tokens and one with 50,000 tokens use very different amounts of GPU time. Charging per token ties the price to the real compute used.

## 3: What is the difference between input tokens and output tokens?

Input tokens are everything you send to the model: system prompt, chat history, documents, tool definitions. Output tokens are what the model generates back. They are counted and priced separately.

## 4: Why are output tokens usually more expensive than input tokens?

The model processes all input tokens in parallel in one pass, which uses the GPU well. Output tokens are generated one at a time, and each one needs its own pass through the model. That makes each output token much more expensive to produce, so providers usually charge 3 to 5 times more for them.

## 5: How do you calculate the cost of a single LLM request?

Multiply the input tokens by the input price and the output tokens by the output price, then add them. Prices are usually given per 1 million tokens.

```ts
// example prices, not real ones
const INPUT_PER_M = 3.0; // $ per 1M input tokens
const OUTPUT_PER_M = 15.0; // $ per 1M output tokens

function requestCost(inputTokens: number, outputTokens: number) {
  return (
    (inputTokens / 1_000_000) * INPUT_PER_M +
    (outputTokens / 1_000_000) * OUTPUT_PER_M
  );
}

requestCost(2000, 500); // 0.006 + 0.0075 = $0.0135
```

## 6: What does "price per 1M tokens" mean?

It is the price you pay for one million tokens of a given type. If the input price is $2 per 1M tokens, then 1,000 input tokens cost $0.002. Most providers publish prices this way because single tokens cost tiny fractions of a cent.

## 7: What is latency in the context of LLMs?

Latency is how long the user or the calling system waits for a result. For LLMs it is usually split into the time until the first token shows up and the time to generate the rest of the answer. Total latency is the time from sending the request to getting the last token.

## 8: What is Time to First Token (TTFT)?

TTFT is the time from sending a request to receiving the first output token. It includes network time, time waiting in the provider's queue and the time the model needs to read the whole prompt. For chat apps it is the number that decides whether the app "feels" fast.

## 9: What is Time Per Output Token (TPOT)?

TPOT is the average time between output tokens after the first one. It is also called inter-token latency (ITL). If TPOT is 20 ms, the model produces about 50 tokens per second for that request.

## 10: How do you estimate the total latency of a response?

A simple formula is: total latency = TTFT + TPOT × (number of output tokens - 1). For example, with a TTFT of 500 ms, a TPOT of 20 ms and 400 output tokens, total latency is about 0.5 + 0.02 × 399 ≈ 8.5 seconds. This shows why long answers are slow even when TTFT is good.

## 11: What is throughput?

Throughput is how much work a system does per unit of time. For LLMs it is usually measured as tokens per second or requests per second across all users. A server can have high throughput and still feel slow for one user, because it is serving many users at once.

## 12: What is the difference between latency and throughput?

Latency is about one request: how long it takes. Throughput is about the whole system: how many tokens or requests it handles per second. Often you trade one for the other. Putting more requests in one batch raises throughput but makes each request a bit slower.

## 13: What is tokens per second (TPS)?

TPS is how many tokens are generated per second. Per request, it tells you how fast the text appears for the user. Per server, it tells you the total capacity. Always say which one you mean, because the numbers are very different.

## 14: What is a context window?

The context window is the maximum number of tokens a model can handle in one request, input and output together. Some models support hundreds of thousands or even millions of tokens. A large window does not mean you should fill it, because every token you send costs money and adds latency.

## 15: How does prompt length affect cost?

Every input token is billed, so a longer prompt costs more on every single call. A 10,000-token system prompt sent with 100,000 requests per day adds up to a billion input tokens per day. Cutting the prompt is often the easiest way to lower the bill.

## 16: How does prompt length affect latency?

The model has to read the whole prompt before it can produce the first token. Longer prompts make TTFT higher. For very long prompts (tens of thousands of tokens) the prompt processing time can be several seconds.

## 17: How does output length affect latency?

Output tokens are generated one by one, so total time grows almost linearly with the number of output tokens. Doubling the answer length roughly doubles the generation time. That is why limiting output length is one of the best ways to make responses faster.

## 18: What is max_tokens and why does it matter?

`max_tokens` (or `max_output_tokens`, depending on the API) is the upper limit on how many tokens the model can generate. It protects you from runaway answers that cost a lot and take a long time. It does not make the model write shorter answers on purpose; it just cuts the answer off when the limit is reached.

## 19: What happens when a response hits the max_tokens limit?

The model stops in the middle of its answer and the API reports a stop reason like `length` or `max_tokens`. You still pay for all generated tokens. Your code should check the stop reason and handle the cut-off answer, for example by asking for a shorter answer or continuing.

## 20: Why is streaming useful for LLM apps?

With streaming, the API sends tokens as soon as they are generated instead of waiting for the full answer. The total time is the same, but the user starts reading after the first token instead of staring at a spinner. It makes the app feel much faster.

## 21: Does streaming reduce the cost of a request?

No. You pay for the same input and output tokens whether you stream or not. Streaming only changes how the result is delivered. It can save money indirectly if users stop a bad answer early and you cancel the request.

## 22: How do you enable streaming with the OpenAI SDK?

Pass `stream: true` and read the events as they arrive.

```ts
import OpenAI from "openai";

const client = new OpenAI();

const stream = await client.responses.create({
  model: "gpt-5-mini",
  input: "Explain HTTP caching in two sentences.",
  stream: true,
});

for await (const event of stream) {
  if (event.type === "response.output_text.delta") {
    process.stdout.write(event.delta);
  }
}
```

## 23: How do you enable streaming with the Anthropic SDK?

Use `client.messages.stream()` and listen to the text events.

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

const stream = client.messages.stream({
  model: "claude-sonnet-4-5",
  max_tokens: 512,
  messages: [
    { role: "user", content: "Explain HTTP caching in two sentences." },
  ],
});

stream.on("text", (text) => process.stdout.write(text));
const final = await stream.finalMessage();
console.log(final.usage);
```

## 24: What is perceived latency?

Perceived latency is how slow the app feels to the user, which is not always the same as the real latency. Streaming, showing progress, and showing partial results all lower perceived latency without changing the real processing time. For user-facing apps, perceived latency is often what matters most.

## 25: Why do bigger models usually cost more?

Bigger models have more parameters, so every token needs more math and more GPU memory. They need more or bigger GPUs to run. Providers pass that cost on, so larger models have higher prices per token.

## 26: Why are bigger models usually slower?

For each output token, the GPU has to read all the model's weights from memory. More parameters means more data to read per token, so each token takes longer. Bigger models also often need several GPUs, which adds communication time.

## 27: What is a "small" or "mini" model and when should you use it?

Small models (often called mini, flash, nano or haiku tiers) are cheaper and faster versions of a provider's main models. They are good for simple tasks like classification, extraction, short summaries and routing. Use them by default and only move to a bigger model when testing shows the small one is not good enough.

## 28: What is the cost and quality trade-off when choosing a model?

Better models usually cost more and are slower. The goal is to pick the cheapest and fastest model that is still good enough for the task. You find that by testing several models on real examples, not by picking the most powerful one by default.

## 29: How do you count tokens before sending a request?

Use the provider's tokenizer or a token counting endpoint. For OpenAI models you can use the `tiktoken` library. Anthropic and Google have token counting API endpoints. Counting first lets you estimate cost and check you fit in the context window.

```python
import tiktoken

enc = tiktoken.get_encoding("o200k_base")
tokens = enc.encode("How many tokens is this sentence?")
print(len(tokens))
```

## 30: How do you count tokens with the Anthropic API?

Call the `count_tokens` endpoint with the same body you would send to `messages.create`.

```ts
const result = await client.messages.countTokens({
  model: "claude-sonnet-4-5",
  system: "You are a helpful assistant.",
  messages: [{ role: "user", content: "Hello!" }],
});

console.log(result.input_tokens);
```

## 31: Where do you see how many tokens a request actually used?

The API response contains a usage object. It has the number of input tokens, output tokens and often cached tokens and reasoning tokens. Log this for every request; it is the most reliable source for your cost tracking.

```ts
const res = await client.responses.create({ model: "gpt-5-mini", input: "Hi" });
console.log(res.usage);
// { input_tokens, output_tokens, input_tokens_details: { cached_tokens }, ... }
```

## 32: Why does the same text have a different token count on different models?

Each model family uses its own tokenizer with its own vocabulary. One tokenizer may split a word into two tokens while another keeps it as one. So token counts, and therefore costs, are not directly comparable across providers for the same text.

## 33: Why do non-English languages often use more tokens?

Tokenizers are trained mostly on English text, so common English words are usually one token. Words in other languages, especially ones with different scripts, are often split into more pieces. The same message can cost 1.5 to 3 times more in some languages.

## 34: Does code use more tokens than plain text?

Often yes. Code has a lot of symbols, indentation and unusual names, and these can split into many small tokens. Whitespace like long runs of spaces can also cost tokens. Minifying or trimming code you send as context can save tokens.

## 35: What is a system prompt and how does it affect cost?

The system prompt is the instructions you send at the start of a conversation to set the model's behavior. It is sent again with every request, so its tokens are billed every time. A long system prompt is a fixed cost added to every call.

## 36: Why does chat history make requests more expensive over time?

LLM APIs are stateless, so you usually resend the whole conversation on every turn. Turn 10 includes all of turns 1 to 9. The input size, and the cost per turn, keeps growing as the chat gets longer.

## 37: What is prompt caching?

Prompt caching lets the provider reuse the work it already did for a prompt prefix it has seen recently. If many requests start with the same long text (system prompt, documents, tools), the cached part is billed at a big discount and processed faster. It lowers both cost and TTFT.

## 38: What does "prefix" mean in prompt caching?

Caching works on the start of the prompt. The cache can only be reused if the beginning of the new prompt is exactly the same as a cached one, token for token. Once something differs, everything after that point is processed again.

## 39: How should you order your prompt to get good cache hits?

Put the parts that never change first and the parts that change last. A good order is: tool definitions, system prompt, static documents and examples, then chat history, then the new user message. If you put a timestamp or user name at the top, you break the cache for everything after it.

## 40: Does OpenAI prompt caching need any code changes?

No. OpenAI applies caching automatically for prompts that are long enough (1024 tokens or more). You can check how many tokens were cached in `usage.input_tokens_details.cached_tokens`. You can also pass a `prompt_cache_key` to help requests with the same prefix land on the same cache.

## 41: How do you use prompt caching with Anthropic?

You mark the end of the part you want cached with a `cache_control` block. Everything before that point becomes the cached prefix.

```ts
const res = await client.messages.create({
  model: "claude-sonnet-4-5",
  max_tokens: 1024,
  system: [
    {
      type: "text",
      text: longCompanyHandbook, // thousands of tokens that never change
      cache_control: { type: "ephemeral" },
    },
  ],
  messages: [{ role: "user", content: "What is our refund policy?" }],
});

console.log(
  res.usage.cache_creation_input_tokens,
  res.usage.cache_read_input_tokens,
);
```

## 42: How long does a prompt cache usually last?

Caches are short lived. The common default is about 5 minutes since the last use, and each hit resets the timer. Some providers offer a longer option, like Anthropic's 1-hour cache, at a higher write price. If traffic is rare, the cache will often expire between requests.

## 43: What is a cache write and a cache read?

A cache write is the first request that stores the prefix in the cache. A cache read is a later request that reuses it. On Anthropic, writes cost a bit more than normal input (1.25x for the 5-minute cache) and reads cost much less (0.1x). So caching only pays off if the prefix is reused.

## 44: What is a batch API?

A batch API lets you send many requests at once in a file and get results later, usually within 24 hours. In return you get a big discount, often 50%. OpenAI, Anthropic and Google all have one.

## 45: When should you use a batch API?

Use it for work that does not need an answer right away: nightly reports, tagging a large dataset, generating embeddings for a backfill, running evaluations. Do not use it for anything a user is waiting for.

## 46: What is a rate limit?

A rate limit is the cap the provider puts on how much you can use the API in a time window. It is usually measured as requests per minute (RPM) and tokens per minute (TPM). If you go over, you get an HTTP 429 error.

## 47: What is RPM?

RPM means requests per minute. It limits how many API calls you can make, no matter how large they are. Many small requests can hit the RPM limit before the token limit.

## 48: What is TPM?

TPM means tokens per minute. It limits the total number of tokens you can process in a minute. A few large requests with long documents can hit the TPM limit even if your RPM is low.

## 49: What does an HTTP 429 error mean?

It means "Too Many Requests". You have hit a rate limit, or the provider is overloaded. The right response is to wait and retry, ideally using the `retry-after` header if the API sends one.

## 50: What is exponential backoff?

It is a retry strategy where you wait longer after each failed attempt: for example 1 s, 2 s, 4 s, 8 s. Adding random "jitter" stops many clients from retrying at the same moment. It is the standard way to handle 429 and 5xx errors.

```ts
async function withRetry<T>(fn: () => Promise<T>, maxAttempts = 5): Promise<T> {
  for (let attempt = 0; ; attempt++) {
    try {
      return await fn();
    } catch (err: any) {
      const retryable = err.status === 429 || err.status >= 500;
      if (!retryable || attempt === maxAttempts - 1) throw err;
      const delay =
        Math.min(2 ** attempt * 1000, 30_000) * (0.5 + Math.random());
      await new Promise((r) => setTimeout(r, delay));
    }
  }
}
```

## 51: Do the official SDKs retry failed requests automatically?

Yes. The official OpenAI and Anthropic SDKs retry some errors (connection errors, 408, 409, 429 and 5xx) a couple of times with backoff by default. You can change this with the `maxRetries` option. Know this before you add your own retry loop, or you may retry far more than you planned.

```ts
const client = new OpenAI({ maxRetries: 3, timeout: 30_000 });
```

## 52: Why should you set a timeout on LLM calls?

LLM calls can sometimes hang or take much longer than usual. Without a timeout, a stuck call holds a connection and leaves the user waiting forever. Set a timeout that fits the task, and handle the error with a retry or a fallback.

## 53: What is a reasoning model?

A reasoning model "thinks" before it answers by generating hidden or summarized reasoning tokens. This helps on hard tasks like math, planning and code. The downside is more tokens, so more cost and more latency.

## 54: What are reasoning tokens and are they billed?

Reasoning tokens are the tokens the model generates while thinking, before the final answer. They are billed as output tokens, even if you cannot see all of them. A short visible answer can still cost a lot if the model thought for thousands of tokens.

## 55: How can you control how much a reasoning model thinks?

Most APIs give you a setting for it. OpenAI uses `reasoning.effort` (for example `minimal`, `low`, `medium`, `high`). Anthropic uses a thinking budget (`budget_tokens`) or an effort setting, and Gemini uses a thinking budget or thinking level. Lower settings are cheaper and faster.

```ts
const res = await client.responses.create({
  model: "gpt-5",
  reasoning: { effort: "low" },
  input: "Classify this ticket as billing, bug or other: ...",
});
```

## 56: When should you avoid using a reasoning model?

Avoid it for simple tasks where thinking does not help: classification, extraction, formatting, simple Q&A, chit-chat. It also does not fit well where you need very low latency, like autocomplete. In those cases a small non-reasoning model, or reasoning turned off, is cheaper and faster.

## 57: What is an embedding and how is it priced?

An embedding is a list of numbers that represents the meaning of a text. It is used for search, RAG and similarity. Embedding models are priced per input token only (there is no output text), and they are much cheaper than chat models.

## 58: Why are embedding calls much cheaper than chat completions?

Embedding models are usually small and only do one pass over the input. They do not generate tokens one by one. That makes them fast and cheap, so they are good for processing large amounts of text.

## 59: What is RAG and how does it affect cost?

RAG (retrieval-augmented generation) means you search your own data and add the best results to the prompt. It costs embeddings for indexing, vector search for each query, and extra input tokens for the retrieved chunks. Sending fewer, better chunks keeps the cost down.

## 60: How does the number of retrieved chunks affect cost and latency?

Each chunk you add is more input tokens, so more cost and a higher TTFT. Sending 20 chunks of 500 tokens is 10,000 extra tokens per request. Often 3 to 5 good chunks give the same or better answers than 20 average ones.

## 61: What is a semantic cache?

A semantic cache stores past questions and answers and returns a saved answer when a new question means the same thing, even if the words are different. It uses embeddings to compare meaning. A cache hit skips the LLM call completely, so it is very cheap and very fast.

## 62: What is the difference between an exact cache and a semantic cache?

An exact cache only matches if the input is exactly the same, usually by hashing it. A semantic cache matches on similar meaning using embeddings and a similarity threshold. Exact caching is safe and simple; semantic caching gets more hits but can return a wrong answer if two questions look similar but are not.

## 63: What is the difference between prompt caching and response caching?

Prompt caching is done by the provider: it reuses work on a shared prompt prefix, but the model still generates a new answer. Response caching is done by you: you store the final answer and return it without calling the model at all. Response caching saves more, but only works when the same answer is fine for the same question.

## 64: How does temperature affect cost and latency?

Temperature changes how random the output is, not how much work is done per token. It has no direct effect on cost or speed. It can have an indirect effect, because different settings can lead to longer or shorter answers.

## 65: Does a lower temperature make caching responses safer?

Somewhat. With low or zero temperature the model gives more consistent answers, so storing and reusing an answer is closer to what the model would say anyway. But even at temperature 0, outputs are not always exactly the same across calls. Many newer reasoning models also do not let you change temperature at all.

## 66: What is model routing?

Model routing means choosing which model should handle each request. Easy requests go to a cheap, fast model and hard ones go to a strong, expensive model. Done well, it cuts cost a lot without hurting quality.

## 67: What is a fallback model?

A fallback model is a second model you call when the main one fails, is too slow, or is rate limited. It can be a different model from the same provider or a model from another provider. It keeps your app working during outages.

## 68: What is a cold start in LLM serving?

A cold start is the extra delay when a model has to be loaded before it can answer, for example on a serverless GPU that was scaled to zero. Loading tens of gigabytes of weights can take from seconds to minutes. Hosted APIs mostly hide this, but it matters a lot when you self-host.

## 69: What are p50, p95 and p99 latency?

They are percentiles. p50 (the median) is the latency that half of requests are faster than. p95 means 95% of requests are faster, and p99 means 99% are. p95 and p99 show the slow "tail" that some users hit, which averages hide.

## 70: Why is average latency not enough to measure performance?

Averages hide outliers. If most requests take 1 second but 5% take 20 seconds, the average looks fine while many users have a bad time. LLM latency has a long tail because output length varies, so always track percentiles.

## 71: What is network latency and how does it affect LLM calls?

Network latency is the time data takes to travel between your server and the provider. It adds to TTFT on every request. It is usually tens of milliseconds, which is small next to model time, but it matters for very fast models and for chains of many calls.

## 72: Why does region matter for LLM latency?

If your servers are far from the provider's data center, every request travels farther. Calling a model hosted in the same region as your backend saves round trip time. Some providers and cloud platforms (Azure, Bedrock, Vertex AI) let you pick the region, and data residency rules may also force a region.

## 73: What are the main cost drivers in an LLM app?

The main ones are: input tokens per request, output tokens per request, number of requests, model price, and how many LLM calls one user action triggers. Hidden drivers are retries, long chat histories, big tool definitions and reasoning tokens. Infrastructure like vector databases and logging adds more on top.

## 74: Why should you log token usage for every request?

Without logs you cannot know where the money goes. Logging input, output and cached tokens with the feature name, user and model lets you find the expensive parts of your app. It also helps you spot bugs like a prompt that suddenly doubled in size.

## 75: What is a cost per user or cost per feature?

It is the total LLM spend divided by users or broken down by feature. It tells you which features are worth their price and whether your pricing plan covers your costs. You get it by tagging every request with the user and feature in your logs.

## 76: How do you put a spending limit on an LLM API?

Most provider consoles let you set monthly budgets, alerts and hard limits per project or API key. In your app, you can also add per-user daily token budgets and stop or slow down users who go over. Use both: provider limits as a last safety net and app limits for fair use.

## 77: Why should you use separate API keys or projects per environment?

So you can see and limit spend for each environment and feature on its own. A bug in staging should not use up the production budget. It also makes it easy to find which service is causing a cost spike.

## 78: What is prompt compression?

Prompt compression means making the prompt shorter while keeping the information the model needs. You can do it by hand (remove filler words, repeated rules, unused examples) or with tools that drop less important tokens. Fewer tokens means lower cost and faster TTFT.

## 79: How can you make a system prompt shorter without losing quality?

Remove repeated instructions, long explanations of things the model already does, and examples that do not change results. Use short bullet points instead of long paragraphs. Then run your evaluation set again to check that quality did not drop.

## 80: How do you ask the model for shorter answers?

Tell it directly in the prompt, for example "Answer in at most 3 sentences" or "Return only the JSON". Set a sensible `max_tokens` as a hard limit. Some APIs also have a verbosity setting, like OpenAI's `text.verbosity` for GPT-5 models.

## 81: What is structured output?

Structured output means the model returns data in a fixed format, usually JSON that matches a schema you provide. Most major APIs can enforce this. It avoids broken output and saves money on retries caused by parsing errors.

## 82: How does structured output help with cost?

The model writes only the fields you need, without extra explanation, so you get fewer output tokens. You also do not need retries to fix bad JSON. Keep the schema small, though, because the schema itself is sent as input tokens.

## 83: What is a tool call and how does it add cost?

A tool call (function call) is when the model asks your code to run a function, like a search or a database query. You run it and send the result back, which needs another model call. Each round trip adds input tokens (the history and the tool result) and latency.

## 84: Why do tool definitions cost tokens?

The names, descriptions and JSON schemas of all your tools are added to the prompt on every call. With many tools this can be thousands of tokens per request, even if no tool is used. Only send the tools that are needed for the current task.

## 85: What is an AI agent and why can it be expensive?

An agent is an LLM in a loop that plans, calls tools and repeats until the task is done. Each step is a full model call that resends the growing history. A single user request can turn into 10 to 50 model calls, so costs and latency can grow fast.

## 86: How do you limit the cost of an agent?

Set a maximum number of steps, a token budget and a time limit for each run. Use a cheaper model for simple steps, keep tool results short, and trim or summarize old history. Stop the loop when the budget runs out and return what you have.

## 87: What is a multi-turn conversation's "token growth" problem?

Because the whole history is sent each turn, the total tokens over a conversation grow roughly with the square of the number of turns. A 50-turn chat can cost far more than 50 times a single turn. Summarizing or trimming old messages keeps this under control.

## 88: How do you trim chat history to save tokens?

Common ways are: keep only the last N messages, drop old tool results, or replace old turns with a short summary. Keep the system prompt and the most recent messages in full. Test that the model still has enough context to answer well.

## 89: What is conversation summarization?

It means using a model (often a cheap one) to write a short summary of older messages, then sending that summary instead of the full text. It keeps long chats affordable. The risk is losing details, so keep key facts like names, IDs and decisions in the summary.

## 90: What is a "token budget"?

A token budget is a planned limit on how many tokens a request, user, feature or agent run is allowed to use. For a single prompt, it is how you split the context window between system prompt, retrieved data, history and output. Budgets make cost predictable.

## 91: What is the difference between a hosted API and self-hosting a model?

With a hosted API you pay per token and the provider runs the hardware. With self-hosting you run an open model on your own GPUs and pay for the machines whether they are busy or not. Hosted is simpler and cheaper at low volume; self-hosting can be cheaper at high, steady volume or needed for privacy.

## 92: What is an open-weight model?

An open-weight model is one whose weights you can download and run yourself, like Llama, Mistral, Qwen, DeepSeek, Gemma or OpenAI's gpt-oss. You can run it on your own hardware or pay a hosting company per token. It gives you more control over cost, latency and data.

## 93: What is an inference provider?

An inference provider is a company that runs models and sells access to them, usually per token. Examples are Together AI, Fireworks, Groq, Cerebras, DeepInfra, plus cloud platforms like AWS Bedrock, Azure and Google Vertex AI. Prices and speed for the same open model can differ a lot between them.

## 94: What is GPU memory and why does it matter for LLMs?

GPU memory (VRAM) holds the model weights and the KV cache for active requests. If the model does not fit, you need more GPUs or a smaller or quantized model. How much memory is left after the weights decides how many requests you can serve at once.

## 95: What is quantization?

Quantization stores model weights (and sometimes activations or the KV cache) with fewer bits, for example 8-bit or 4-bit numbers instead of 16-bit. The model uses less memory and often runs faster. The trade-off is a small, sometimes noticeable, drop in quality.

## 96: How does quantization reduce cost?

A smaller model fits on fewer or cheaper GPUs and leaves more memory for serving more requests at once. Generation is also faster because less data is read per token. Together this means more tokens per dollar.

## 97: What is a prompt token vs a completion token?

These are older names for input and output tokens. "Prompt tokens" are what you send, and "completion tokens" are what the model generates. The Chat Completions API still uses `prompt_tokens` and `completion_tokens` in its usage object.

## 98: Why should you not send the full document when only part is needed?

Every extra token costs money and adds latency, and too much unrelated text can also make answers worse. Extract or retrieve only the sections that matter. For example, send the relevant table instead of the full 80-page PDF.

## 99: What is a long-context price tier?

Some providers charge a higher price per token when a prompt goes over a certain size, for example above 200,000 tokens. The whole request may then be billed at the higher rate. Check this before sending huge prompts, because the cost can jump.

## 100: What is a cancellation and why does it matter for cost?

Cancelling means stopping a request before it finishes, for example when the user clicks "stop" or leaves the page. If you abort the stream, the provider stops generating and you usually do not pay for tokens that were never generated. Wire up cancellation so you do not pay for answers nobody reads.

```ts
const controller = new AbortController();
stopButton.onclick = () => controller.abort();

const stream = await client.responses.create(
  { model: "gpt-5-mini", input: question, stream: true },
  { signal: controller.signal },
);
```

## 101: What are images priced like in multimodal models?

Images are turned into tokens too. The number of tokens depends on the image size and the detail setting. A large high-resolution image can cost more than a page of text, so resize images to the smallest size that still works for the task.

## 102: How can you reduce the cost of image inputs?

Resize or crop images before sending them, and use a low detail setting when fine detail is not needed. Send one image instead of many when possible. For documents, extracting the text with OCR first can be cheaper than sending page images.

## 103: How is audio priced in LLM APIs?

Speech-to-text is often priced per minute of audio, while audio-capable chat models price audio as tokens, usually at higher rates than text. Text-to-speech is priced per character or per audio token. Real-time voice APIs can get expensive because both input and output are audio.

## 104: What is a "free tier" and why should you not rely on it in production?

A free tier gives limited usage at no cost, but with low rate limits and sometimes with your data used for training. It is fine for learning and prototypes. Production apps need paid tiers for higher limits, better reliability and clear data terms.

## 105: What is a usage tier?

Many providers put accounts into tiers based on how much you have spent and how long you have been a customer. Higher tiers get higher rate limits. If you are hitting rate limits, moving up a tier may be easier than changing your code.

## 106: What is the difference between a flagship model and a budget model?

A flagship model is the provider's strongest model, with the best quality and the highest price. A budget model is smaller, much cheaper and faster, but weaker on hard tasks. The price gap can be 10 to 50 times per token.

## 107: Why should you test with real data before choosing a model?

Benchmarks and marketing do not tell you how a model does on your task. A cheap model might be just as good for your data, or an expensive one might not help at all. A small set of real examples with expected answers lets you compare cost and quality fairly.

## 108: What is an evaluation set (eval) and why does it matter for cost work?

An eval set is a list of example inputs with expected outputs or grading rules. Every time you change a model, prompt or setting to save money, you run the eval to make sure quality did not drop. Without it, cost cutting is guesswork.

## 109: What does "cost per 1,000 requests" mean and why is it useful?

It is the average cost of a request times 1,000. It is easier to think about than per-token prices, and it is easy to compare between models. For example, $0.0135 per request is $13.50 per 1,000 requests.

## 110: How do you estimate monthly LLM costs for a new feature?

Estimate the average input and output tokens per request, the number of requests per user per day, and the number of users. Multiply it all by the model's prices and by 30 days. Add a buffer for retries and growth.

```ts
const users = 10_000;
const requestsPerUserPerDay = 5;
const avgInput = 1500,
  avgOutput = 300;
const inPrice = 0.4,
  outPrice = 1.6; // example $ per 1M tokens

const perRequest = (avgInput * inPrice + avgOutput * outPrice) / 1_000_000;
const monthly = perRequest * users * requestsPerUserPerDay * 30;
console.log(monthly.toFixed(2)); // ~162.00
```

## 111: What is the "N+1" problem in LLM calls?

It is when you call the model once per item in a loop instead of handling many items in one call. 100 product descriptions as 100 calls means 100 times the fixed prompt cost and 100 round trips. Grouping items into one request, when the task allows it, saves both cost and time.

## 112: Why is it often better to process several items in one prompt?

The fixed part of the prompt (instructions, examples) is paid once instead of once per item. You also make fewer network round trips. The risk is that quality can drop or one bad item ruins the batch, so keep groups at a reasonable size.

## 113: What is parallel request execution?

It means sending several independent LLM calls at the same time instead of one after another. Total time becomes roughly the time of the slowest call, not the sum. Cost stays the same, but watch your rate limits.

```ts
const [summary, tags, sentiment] = await Promise.all([
  summarize(text),
  extractTags(text),
  classifySentiment(text),
]);
```

## 114: What is sequential chaining and why is it slow?

Sequential chaining means each call waits for the one before it, because it needs its output. Latencies add up, so five 2-second calls take 10 seconds. Only chain steps that really depend on each other, and run the rest in parallel.

## 115: What is the difference between synchronous and asynchronous LLM processing?

Synchronous means the user or caller waits for the answer in the same request. Asynchronous means the work goes to a queue or background job and the result is delivered later, for example by email, webhook or polling. Async lets you use cheaper batch APIs and handle spikes better.

## 116: What is a queue and how does it help with LLM workloads?

A queue holds jobs until workers are free to handle them. It smooths out traffic spikes so you stay under rate limits, and it lets you retry failed jobs safely. Tools like SQS, RabbitMQ, BullMQ or Kafka are commonly used.

## 117: What is an LLM gateway?

An LLM gateway is a proxy between your app and the model providers. It gives you one API for many models and adds features like logging, caching, rate limiting, retries, fallbacks and cost tracking. Examples are LiteLLM, Portkey, Helicone, Cloudflare AI Gateway and Vercel AI Gateway.

## 118: What is LLM observability?

LLM observability means recording what happens in each LLM call: prompt, response, tokens, cost, latency, errors and user feedback. Tools like Langfuse, LangSmith, Helicone and OpenTelemetry-based tracing do this. It helps you find slow and expensive parts and debug bad answers.

## 119: What is a trace in LLM observability?

A trace is the full record of one user action, made of spans for each step: retrieval, each LLM call, each tool call. It shows where time and tokens are spent. For agents and RAG, traces are the easiest way to see which step is slow or costly.

## 120: What basic metrics should you track for an LLM feature?

Track TTFT, total latency (p50, p95, p99), input tokens, output tokens, cached tokens, cost per request, error rate and rate limit errors. Group them by model, feature and prompt version. Add a quality signal like user ratings or eval scores so you see the effect of cost changes.

## 121: What is the difference between a model alias and a pinned model version?

An alias (like `gpt-5-mini` or `claude-sonnet-4-5`) may point to newer snapshots over time. A pinned version (with a date in the name) stays the same. Pinning keeps cost, speed and behavior stable; aliases can change all three without warning.

## 122: Why can a model upgrade change your costs?

A new model may have different prices, a different tokenizer (so different token counts for the same text), or a habit of writing longer answers. Reasoning models may also use many more hidden tokens. Always check cost and latency on your eval set before switching.

## 123: What does "deprecation" of a model mean for cost planning?

Providers retire old models after a notice period. You will have to move to a newer model, which may cost more or less and behave differently. Track deprecation notices and plan time to test the replacement.

## 124: What is a stop sequence and how can it save tokens?

A stop sequence is a string that makes the model stop generating when it appears. For example, you can stop at `"\n\n"` if you only want the first paragraph. The model stops early, so you pay for fewer output tokens and get the answer faster. Not all models support it, especially some reasoning models.

## 125: What is a few-shot prompt and how does it affect cost?

A few-shot prompt includes example inputs and outputs to show the model what you want. The examples improve quality but add input tokens to every request. Use as few as you need, and put them in the cached prefix.

## 126: What is the cost difference between zero-shot and few-shot prompts?

Zero-shot has no examples, so it is cheaper. Few-shot can add hundreds or thousands of tokens per call. If a stronger model gets it right zero-shot, it can sometimes be cheaper than a weaker model with many examples, so compare both.

## 127: What is fine-tuning and how can it lower cost?

Fine-tuning trains a model further on your own examples. A small fine-tuned model can sometimes match a large general model on a narrow task, and it needs shorter prompts because the behavior is learned. That can lower cost per request a lot, but training and hosting have their own costs.

## 128: What is distillation?

Distillation means using a big, expensive model to create training data, then fine-tuning a small, cheap model on it. The small model learns to do that specific task almost as well. It is a common way to cut costs for high-volume tasks.

## 129: What is a "serverless" inference endpoint?

It is a hosted model you pay for per token or per second of use, with no machines to manage. It scales down when idle, so you do not pay when no one is using it. It may have cold starts and less control over speed than a dedicated deployment.

## 130: What is a dedicated or provisioned deployment?

It is model capacity reserved only for you, paid by the hour or by month instead of per token. Examples are provisioned throughput on Azure OpenAI, Bedrock and Vertex AI. It gives steady latency and high limits, and it becomes cheaper than pay-per-token when you use it heavily.

## 131: What is the difference between pay-as-you-go and reserved capacity pricing?

Pay-as-you-go charges for each token you use, so cost follows traffic. Reserved capacity charges a fixed amount for a set amount of throughput, whether you use it or not. Pay-as-you-go is better for low or unpredictable traffic; reserved is better for high, steady traffic.

## 132: What is a priority or service tier?

Some providers let you pay more for faster, more reliable processing or pay less for slower processing. For example, OpenAI has a `service_tier` parameter with options like `flex` (cheaper, slower, may be unavailable) and `priority` (more expensive, faster). Use cheap tiers for background work and priority tiers for critical paths.

## 133: What is OpenAI's Flex processing?

Flex processing is a service tier where requests are cheaper (about batch prices) but can be slower and may sometimes fail because no capacity is available. You still get answers in the normal request/response flow. It fits jobs that are not urgent but where you do not want the full batch API workflow.

## 134: Why does the time of day affect LLM latency?

Providers share hardware among many customers. During busy hours, queues are longer and you may see higher TTFT and more overload errors. Background jobs can be scheduled for quieter times.

## 135: What is a "429 vs 529 vs 503" error from an LLM provider?

429 means you went over your rate limit. 503 means the service is unavailable. Anthropic uses 529 to mean the API is overloaded across all users. All three are usually worth retrying with backoff.

## 136: What is "tokens per word" and why does it matter for estimates?

It is the average number of tokens per word in your text. For English it is about 1.3. It lets you turn word counts into rough token and cost estimates, but measure with a real tokenizer for anything important.

## 137: How does JSON formatting affect token count?

JSON has many quotes, braces and repeated keys, which all cost tokens. Pretty-printed JSON adds whitespace tokens too. Send compact JSON, short key names, or a simpler format like CSV for large tables you feed into a prompt.

## 138: Why should you remove HTML before sending web pages to a model?

HTML tags, scripts, styles and attributes can be most of a page's tokens while the useful text is small. Converting to plain text or Markdown can cut tokens by 80% or more. The model also understands clean text better.

## 139: What is the difference between a chat model and a completion model for cost?

Old-style completion models took raw text. Chat models take a list of messages and add some formatting tokens for each message. The difference in cost is small; today almost everything uses chat-style APIs.

## 140: What is a "warm-up" request?

A warm-up request is a dummy call made to load a model or fill a cache before real traffic arrives. For self-hosted models it avoids cold start delays. For prompt caching it pre-loads the shared prefix so the first real user gets a cache hit.

## 141: Can you cache embeddings?

Yes, and you should. If the same text appears again, reuse the stored embedding instead of calling the API. Store embeddings with a hash of the text and the model name, because embeddings from different models are not compatible.

## 142: Why do you need to re-embed data when changing the embedding model?

Vectors from different embedding models live in different spaces, so you cannot compare them. Switching models means you must re-embed all your documents. For large datasets that is a real cost, so pick the embedding model carefully.

## 143: What are embedding dimensions and how do they affect cost?

Dimensions are the length of the embedding vector, like 768, 1536 or 3072. Larger vectors take more storage and make vector search slower. Some models let you ask for fewer dimensions, which saves storage and search time with only a small quality loss.

## 144: What is a vector database cost driver?

The main drivers are the number of vectors, their dimensions, how often you query, and the index type. Keeping everything in memory is fast but expensive. Some databases offer disk-based or compressed indexes that cost less but are a bit slower.

## 145: What is an SLA in the context of LLM APIs?

An SLA (service level agreement) is the provider's promise about uptime and sometimes latency. Many standard API plans do not have strong latency SLAs. Enterprise and provisioned plans often do, and they cost more.

## 146: What is "time to last token"?

It is the time from sending the request until the full response has arrived. It is the same as total latency. It matters most when the answer is used by code, like JSON that you can only parse when it is complete.

## 147: Why should background jobs use cheaper models or batch APIs?

Nobody is waiting for the answer, so speed does not matter much. Batch APIs and flex tiers often cut the price in half. Over millions of calls, that is a big saving with no impact on users.

## 148: What does "good enough" mean when picking a model?

It means the model meets your quality bar on your eval set for the task, not that it is the best model possible. If a cheap model scores 95% and an expensive one 96%, the cheap one may be the right choice. Decide the bar first, then pick the cheapest model that passes it.

## 149: What is a cost alert?

A cost alert is a notification when spend goes over a set amount, or grows much faster than normal. You can set them in the provider dashboard, your cloud billing tools or your observability platform. They help you catch bugs like infinite agent loops before the bill gets huge.

## 150: What are the first three things you would check if an LLM bill suddenly went up?

First, which feature, API key or model the extra spend comes from. Second, whether request count went up (more traffic or a retry loop) or tokens per request went up (a prompt change or longer history). Third, whether the cache hit rate dropped, for example because a prompt change broke the cached prefix.

# Moderate Questions (151-300)

## 151: How do you build a model cascade?

A cascade sends a request to a cheap model first and only moves to a stronger model if the first answer is not good enough. You need a check in between: a schema validation, a confidence score, a rule, or a small grader model. If most requests pass at the first step, you pay flagship prices only for the hard ones.

```ts
async function answer(question: string) {
  const cheap = await callModel("small-model", question);
  if (await isGoodEnough(cheap, question)) return cheap;
  return callModel("large-model", question);
}
```

## 152: What is the downside of a cascade?

Hard requests now take two calls, so they cost more and take longer than going straight to the big model. The check itself also costs time and money. A cascade only pays off when most requests are handled by the cheap step, so measure the pass rate.

## 153: How do you decide which requests go to which model in a router?

Start with simple rules: request type, input length, user plan, or a keyword. Next step is a small classifier (a small LLM or an embedding-based model) that predicts if the request is easy or hard. Check the router on labeled data, because sending a hard request to a weak model hurts quality.

## 154: How do you measure TTFT in code?

Record the time when you send the request and the time the first content chunk arrives in the stream. Measure on the client side, so the number includes network and queue time.

```ts
const start = performance.now();
let ttft: number | null = null;

const stream = await client.responses.create({ model, input, stream: true });
for await (const event of stream) {
  if (event.type === "response.output_text.delta" && ttft === null) {
    ttft = performance.now() - start;
  }
}
const total = performance.now() - start;
console.log({ ttft, total });
```

## 155: How do you measure TPOT or output speed in code?

Take the total time minus TTFT and divide it by the number of output tokens minus one. Use the output token count from the usage object, not the number of stream chunks, because one chunk can have several tokens. Note that hidden reasoning tokens make visible output look slower than the real decode speed.

## 156: How do you load test an LLM endpoint?

Send traffic with realistic prompt and output lengths at different concurrency levels and record TTFT, TPOT, total latency, throughput and errors. Tools like k6, Locust, LLMPerf, NVIDIA GenAI-Perf and `vllm bench serve` can do this. Increase concurrency step by step until latency gets too high; that point is your real capacity.

## 157: Why must load tests use realistic prompt and output lengths?

Cost and speed depend heavily on token counts. A test with 50-token prompts and 20-token answers will look much faster than real traffic with 5,000-token prompts and 800-token answers. Use samples from your production logs to build the test data.

## 158: How do you measure your prompt cache hit rate?

Read the cached token fields from each response: `cached_tokens` on OpenAI, `cache_read_input_tokens` and `cache_creation_input_tokens` on Anthropic, `cached_content_token_count` on Gemini. Hit rate is cached input tokens divided by total input tokens. Track it over time and per prompt version.

## 159: How do you keep dynamic content from breaking the prompt cache?

Put dynamic content (date, user name, retrieved data, the question) after all the static parts. If the system prompt needs something dynamic, move it to a later message instead. Also keep the order of tools and JSON keys stable, because even small changes in the prefix cause a miss.

```ts
// Bad: date at the top breaks the cache every day (or every second)
const system = `Today is ${new Date().toISOString()}.\n${bigStaticInstructions}`;

// Better: static first, dynamic later
const system2 = bigStaticInstructions;
const messages = [{ role: "user", content: `Today is ${today}. ${question}` }];
```

## 160: How many cache breakpoints can you set with Anthropic and why use more than one?

You can set up to 4 `cache_control` breakpoints in one request. Using several lets you cache layers that change at different rates, for example tools and system prompt (rarely change), then a document (changes per session), then the chat history (grows each turn). A change in a later layer does not throw away the earlier ones.

## 161: Is there a minimum prompt size for caching?

Yes. Providers only cache prefixes above a minimum length. OpenAI starts at 1024 tokens. Anthropic's minimum depends on the model (from about 1024 to a few thousand tokens). Shorter prompts are processed normally and get no discount.

## 162: How do you work out if Anthropic's 5-minute cache pays off?

With a write at 1.25x and reads at 0.1x the normal input price, the first call costs 25% extra and each hit saves 90%. So one hit within the cache lifetime already more than pays for the write. If the prefix is almost never reused within 5 minutes, caching just adds 25% to the cost.

## 163: When is the 1-hour cache worth it?

The 1-hour cache costs more to write (2x the base input price on Anthropic) but survives longer gaps. It makes sense when the same prefix is used every 10 to 30 minutes, for example in agent sessions where the user steps away, or for low-traffic features where the 5-minute cache keeps expiring. If traffic is high, the 5-minute cache stays warm anyway and is cheaper.

## 164: What does prompt_cache_key do in the OpenAI API?

It is an optional string you send to group requests that share a prefix. OpenAI uses it, with the prefix, to route those requests to the same machines, which raises the chance of a cache hit. Use a value like the tenant ID or prompt template name; do not give each request a unique value.

## 165: What is the difference between implicit and explicit caching in Gemini?

Implicit caching is automatic on newer Gemini models: if a request starts with the same prefix as a recent one, you get the discount without doing anything, but hits are not guaranteed. Explicit caching lets you create a cache object with your content and a TTL, then refer to it in later requests. Explicit caching gives a guaranteed discount but you also pay for storage per hour.

## 166: Is the prompt cache shared between different customers?

No. Providers isolate caches per organization or account, so another company cannot get a hit on your prompts. Within your own organization, different users can share a cache hit if their prompts start with the same prefix, which is what you want for a shared system prompt.

## 167: How do you choose the similarity threshold for a semantic cache?

Collect real pairs of questions, label which ones should share an answer, and test different thresholds. A high threshold gives few wrong answers but few hits; a low one gives many hits but more wrong answers. Pick the value where the error rate is acceptable for your domain, and be stricter for things like prices, medical or legal answers.

## 168: How do you handle stale answers in a response cache?

Give cache entries a TTL that fits how fast the data changes. Include the model, prompt version and data version in the cache key so a change creates new entries. When the source data changes, delete or ignore the related entries.

```ts
const key = sha256(
  JSON.stringify({ model, promptVersion: "v7", docsVersion, question }),
);
```

## 169: Why is response caching hard for personalized answers?

If the answer depends on the user's data, account or history, one user's answer is wrong (or a privacy leak) for another. You either include the user or tenant in the cache key, which lowers the hit rate, or only cache the general parts. Never share cached answers across tenants unless the content is truly public.

## 170: How does the OpenAI Batch API work?

You write requests to a JSONL file, one per line, each with a `custom_id`. You upload the file, create a batch, wait for it to finish (up to 24 hours), then download the output file and match results by `custom_id`. Prices are about half of the normal ones.

```jsonl
{"custom_id": "doc-1", "method": "POST", "url": "/v1/responses", "body": {"model": "gpt-5-mini", "input": "Summarize: ..."}}
{"custom_id": "doc-2", "method": "POST", "url": "/v1/responses", "body": {"model": "gpt-5-mini", "input": "Summarize: ..."}}
```

## 171: How does the Anthropic Message Batches API work?

You send a list of requests, each with a `custom_id` and normal `messages.create` params, in one call. You then poll the batch status, and when it ends you read the results. Most batches finish within an hour, the max is 24 hours, and the price is 50% of normal.

```ts
const batch = await client.messages.batches.create({
  requests: docs.map((doc) => ({
    custom_id: doc.id,
    params: {
      model: "claude-haiku-4-5",
      max_tokens: 300,
      messages: [{ role: "user", content: `Summarize:\n${doc.text}` }],
    },
  })),
});
```

## 172: Can you combine batch discounts with prompt caching?

It depends on the provider. Anthropic lets you use prompt caching inside batches and the discounts stack, though hits are best-effort because requests run at different times. Rules are different for other providers and models, so check the docs. Putting the shared prefix in every request still helps where caching is supported.

## 173: How do you handle partial failures in a batch job?

Some requests in a batch can fail or expire while others succeed. Read the result for each `custom_id`, collect the failed ones, and resubmit only those in a new batch or as normal calls. Make your processing idempotent so a request that runs twice does not cause problems.

## 174: How do you read rate limit headers?

Providers send headers that show your limits and what is left, for example `x-ratelimit-remaining-tokens` and `x-ratelimit-reset-requests` on OpenAI or `anthropic-ratelimit-tokens-remaining` on Anthropic. Reading them lets you slow down before you hit a 429. On a 429, use the `retry-after` header to know how long to wait.

## 175: How do you build a client-side rate limiter for LLM calls?

Use a token bucket that tracks both requests and estimated tokens per minute, and wait before sending when the bucket is empty. For one process an in-memory limiter is fine. For many servers, keep the counters in a shared store like Redis so all instances respect the same limit.

## 176: How do you limit concurrency when calling an LLM for many items?

Use a concurrency limiter so only N calls run at the same time. This keeps you under rate limits and avoids a flood of 429 errors.

```ts
import pLimit from "p-limit";

const limit = pLimit(8);
const results = await Promise.all(
  items.map((item) => limit(() => summarize(item))),
);
```

## 177: How do you spread load across several providers or regions?

Put a gateway or a small routing layer in front of your calls and send requests to several deployments of the same or similar models. Route by health, latency or remaining rate limit. Tools like LiteLLM, Portkey or cloud-native load balancers can do this. Remember that outputs can differ a bit between models, so test each one.

## 178: How do you add a fallback when the main model fails?

Wrap the call, catch errors like timeouts, 429 and 5xx, and call a backup model. Keep the prompt compatible with both models.

```ts
async function generate(input: string) {
  try {
    return await callWithTimeout(() => primary(input), 15_000);
  } catch (err) {
    log.warn("primary failed, using fallback", err);
    return await fallback(input);
  }
}
```

## 179: What are hedged requests?

A hedged request is a second copy of a request sent if the first one has not answered within a set time, for example the p95 latency. You use whichever answer comes first and cancel the other. It cuts tail latency but costs extra tokens for the requests you hedge.

## 180: Why should you use separate timeouts for TTFT and total time?

A stream that has not started after 10 seconds is probably stuck, while a stream that is producing tokens may need 60 seconds to finish a long answer. One global timeout either kills good long answers or waits too long on stuck ones. Use a short timeout for the first token and a longer one, or an idle timeout between tokens, for the rest.

## 181: How do you stream LLM output from your backend to the browser?

The usual way is Server-Sent Events (SSE) or a streaming HTTP response. Your server reads the provider's stream and writes each chunk to the client as it arrives. Libraries like the Vercel AI SDK handle this on both sides.

```ts
// Next.js route handler
export async function POST(req: Request) {
  const { question } = await req.json();
  const stream = await client.responses.create({
    model,
    input: question,
    stream: true,
  });

  const body = new ReadableStream({
    async start(controller) {
      for await (const event of stream) {
        if (event.type === "response.output_text.delta") {
          controller.enqueue(new TextEncoder().encode(event.delta));
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

## 182: Why might streaming not work in production even though it works locally?

Something between the server and the browser is buffering the response: a reverse proxy like Nginx, a load balancer, a CDN, or compression middleware. The user then gets the whole answer at the end. Turn off buffering for those routes (for example `proxy_buffering off;` in Nginx or the `X-Accel-Buffering: no` header) and make sure compression does not hold chunks.

## 183: How do you stream structured output like JSON?

The JSON is incomplete until the end, so you use a partial JSON parser that can read unfinished objects, and you update the UI as fields fill in. Libraries like the Vercel AI SDK (`streamObject`) and some provider SDKs support this. It lets you show the first items of a list while the rest is still being generated.

## 184: How does streaming work with tool calls?

The model streams the tool name and arguments as chunks, and you collect them until the tool call is complete. Then you run the tool and start a new call with the result. To keep the UI responsive, show a status like "Searching..." while tools run.

## 185: What are UI techniques to hide LLM latency?

Stream text, show a typing or progress indicator, show the steps an agent is taking, and render partial results as soon as possible. You can also start the LLM call earlier, for example when the user focuses the input or picks an option. Skeleton screens and optimistic updates help too.

## 186: How does reranking help with RAG cost?

You retrieve many candidates cheaply (say 50) and then use a reranker model to pick the best few (say 5) to send to the LLM. The LLM sees fewer tokens, so cost and TTFT go down, and answers often get better. The reranker adds some latency and cost, so measure the net effect.

## 187: How does chunk size affect RAG cost and quality?

Big chunks give more context per hit but send more unrelated text, which costs tokens. Small chunks are more precise but can miss context and need more of them. A common start is 300 to 800 tokens with some overlap, then tune based on evals.

## 188: Is it cheaper to put the whole document in the context or use RAG?

For a one-off question on a short document, putting it in the context is simple and fine. For many questions over large or many documents, RAG sends far fewer tokens per question and is usually much cheaper and faster. Long context plus prompt caching is a middle option when the same document is asked about many times in a short period.

## 189: What is query rewriting in RAG and what does it cost?

Query rewriting uses an LLM to turn the user's question into a better search query, or several queries. It can improve retrieval a lot, but it adds an LLM call before the main one, which adds latency. Use a small, fast model for it, and skip it when the question is already clear.

## 190: What is contextual compression in RAG?

It means trimming retrieved chunks to only the sentences that matter for the question before sending them to the main model. It can be done with a small LLM, an extractive model or simple rules. It saves tokens in the main call but adds a step, so it pays off mostly when the main model is expensive.

## 191: Should you cache retrieval results?

Yes, for repeated or similar queries. Cache the query embedding and the list of document IDs returned by the vector search. It saves embedding calls and search time. Clear or version the cache when the index is updated.

## 192: How do you embed many documents cheaply?

Send texts in batches to the embedding endpoint (most accept a list of inputs per call), use the batch API for large backfills, and skip texts whose hash already has an embedding. Use a smaller embedding model if quality is fine. Run it as a background job with a concurrency limit.

## 193: How do you reduce the token cost of tool results in an agent?

Return only the fields the model needs, cut long lists, and summarize large outputs before sending them back. For example, return the top 10 search results with titles and short snippets instead of full pages. Big tool results stay in the history and are paid for again on every later step.

## 194: How do parallel tool calls reduce latency?

Many models can ask for several tool calls in one turn. If you run them at the same time instead of one by one, the step takes as long as the slowest tool. It also saves model round trips because the model gets all results together.

## 195: What is the plan-and-execute pattern and how does it save money?

A strong model makes a plan once, and a cheaper model (or plain code) carries out each step. You pay for the expensive model only for planning and maybe a final check. It works well when steps are simple but the planning is hard.

## 196: How do you detect and stop an agent stuck in a loop?

Set a hard limit on steps and tokens. Also detect repeats, for example the same tool with the same arguments called several times in a row, and stop or change strategy. Log these cases, because loops are one of the most common causes of surprise bills.

```ts
const seen = new Map<string, number>();
function checkLoop(toolName: string, args: unknown) {
  const key = toolName + JSON.stringify(args);
  const count = (seen.get(key) ?? 0) + 1;
  seen.set(key, count);
  if (count >= 3) throw new Error("Agent loop detected");
}
```

## 197: How do sub-agents help with cost?

A sub-agent does a focused task in its own fresh context and returns only a short result to the main agent. The main agent's history does not fill up with all the raw tool output from that task. This keeps later main-agent calls smaller. The sub-agent's own calls still cost money, so use it for tasks that produce a lot of noise.

## 198: Why is clearing old tool results from the context useful?

In long agent runs, old tool outputs (file contents, search results) are often no longer needed but are sent again on every step. Removing or replacing them with a short note cuts input tokens a lot. Some APIs have built-in context management features for this; otherwise you can do it in your own code.

## 199: Why can connecting many MCP servers make each request more expensive?

Each MCP server adds its tools, and every tool's name, description and schema is sent to the model. With many servers this can be tens of thousands of tokens before the user says anything. Only enable the servers a task needs, or use tool search features that load tool definitions on demand.

## 200: Does structured output make requests slower?

Usually only a little. With strict schema enforcement, the first request with a new schema can take longer because the provider has to prepare the grammar, and later requests with the same schema are faster. Large or deeply nested schemas also add input tokens, so keep them simple.

## 201: What is the difference between JSON mode and schema-based structured output?

JSON mode only makes sure the output is valid JSON, but not that it has the right fields. Schema-based structured output (like OpenAI's `json_schema` with `strict: true`, or strict tool definitions) makes the output match your schema. The schema version saves you from validation failures and retries, which saves tokens.

## 202: How can you cut output tokens without hurting answer quality?

Ask the model to skip the intro and the recap, give it a short format to follow, and ask only for the fields you need. Have it return IDs or labels instead of copying long text. For edits, ask for changes only, not the whole rewritten document.

## 203: Why is asking for IDs instead of full text a good trick?

If you want the model to pick items from a list, give each item a short ID and ask for the IDs back. The model writes 5 tokens instead of 500. Your code then looks up the full items. This is faster and also avoids small copy mistakes.

```text
Here are the products:
[1] Red cotton t-shirt, size M ...
[2] Blue denim jacket ...
[3] ...

Return the IDs of products that match "summer clothes" as a JSON array, for example [1, 3].
```

## 204: Why should code assistants output diffs instead of whole files?

Rewriting a 500-line file to change two lines costs hundreds of output tokens, and output tokens are slow and expensive. Asking for a diff, a search-and-replace block or an edit tool call writes only the changed parts. It is much faster and cheaper.

## 205: What is the verbosity parameter?

Some newer models, for example OpenAI's GPT-5 family, accept a verbosity setting (`low`, `medium`, `high`) that changes how long and detailed answers are. Low verbosity gives shorter answers, so fewer output tokens. It is easier than tuning the prompt for length, but you should still check quality.

```ts
const res = await client.responses.create({
  model: "gpt-5",
  input: "Explain what a CDN does.",
  text: { verbosity: "low" },
});
```

## 206: How do you choose the right reasoning effort for a task?

Run your eval set with each effort level and record quality, cost and latency. Pick the lowest level where quality is still good enough. Often simple tasks work just as well with minimal or low effort, and you save a lot of tokens and seconds.

## 207: How do you see how many reasoning tokens were used?

The usage object reports them. On OpenAI they are in `usage.output_tokens_details.reasoning_tokens`. On Anthropic, thinking tokens are included in `output_tokens`. Log them separately when you can, so you know how much of your spend is thinking.

## 208: When is a non-reasoning model with a "think step by step" prompt better than a reasoning model?

When the task needs only a little reasoning and you want control over cost and speed. A fast model with a short instruction to reason first can be enough and much cheaper. For hard multi-step problems, real reasoning models usually do better.

## 209: What are Predicted Outputs?

Predicted Outputs is an OpenAI feature for some models (like the GPT-4o and GPT-4.1 series) where you pass text you expect most of the answer to look like, for example the current file when asking for a small edit. Matching parts are produced much faster, so latency drops. You are still billed for prediction tokens that were not used, so it costs a bit more.

## 210: How do you attribute LLM costs to features and customers?

Tag every call with metadata like feature name, tenant ID, user ID and prompt version. Save the usage numbers with those tags in your logs or observability tool, and compute cost from the token counts and your price table. Then you can group spend by any of those tags.

## 211: What should a basic LLM cost dashboard show?

Total spend per day, spend per feature and per model, spend per customer, average and p95 tokens per request, cache hit rate, and error or retry rate. Add latency charts (TTFT and total, p50 and p95) next to it. Put the deploy markers on the charts so you can link changes to cost jumps.

## 212: How do you implement per-user token quotas?

Count each user's tokens in a fast store like Redis with a key per user per day or month. Check the count before a request, and add the real usage after it finishes. When a user goes over the limit, block, slow down or switch them to a cheaper model.

```ts
async function checkAndTrack(userId: string, tokensUsed: number) {
  const key = `tokens:${userId}:${new Date().toISOString().slice(0, 10)}`;
  const total = await redis.incrby(key, tokensUsed);
  await redis.expire(key, 60 * 60 * 48);
  return total;
}
```

## 213: How do LLM costs affect how you price your own product?

LLM calls are a real cost per action, unlike most normal software features that cost almost nothing per use. You need to know the cost per active user and the heavy-user cost, then make sure your plans cover it. Common answers are usage limits, credits, higher tiers for heavy users, or charging per use.

## 214: What is gross margin and why does it matter for AI products?

Gross margin is revenue minus direct costs, as a share of revenue. For AI products, model costs can be a big part of direct costs, so margins can be much lower than classic SaaS. Tracking cost per user helps you see if a plan is losing money.

## 215: How do you stop free users from running up large LLM costs?

Give free users strict quotas, a cheaper model, shorter context and lower output limits. Add rate limiting, bot protection and signup checks so people cannot create many free accounts. Watch for single users with unusual usage.

## 216: What is a "denial of wallet" attack?

It is when someone uses your app to make you spend a lot of money, for example by sending huge prompts, triggering long agent runs, or scripting thousands of requests. The app may stay up, but the bill goes through the roof. Defenses are auth, rate limits, input size limits, per-user budgets and alerts.

## 217: How can prompt injection increase your costs?

Injected instructions in a document or web page can tell an agent to loop, call expensive tools many times, or write very long outputs. This burns tokens and maybe paid tool calls. Hard limits on steps, tool calls and output length protect you even if the model gets tricked.

## 218: What should a response cache key include?

At minimum: the model name and version, the prompt template version, the normalized input, and any settings that change the output (like temperature or schema). For per-user data, add the user or tenant ID. Leaving something out means you may return an answer created under different conditions.

## 219: Why should you version your prompts?

A prompt change can change cost, latency and quality, and you need to know which version caused what. Store prompts with a version ID and log it with every call. Then you can compare versions and roll back if a new one is more expensive or worse.

## 220: How do you catch cost regressions before deploy?

Run your eval set in CI and record average input tokens, output tokens and cost per example. Fail the build or post a warning if cost goes up by more than a set amount compared with the main branch. This catches things like an accidentally duplicated system prompt.

## 221: How do you A/B test a cheaper model?

Send a share of real traffic (say 10%) to the new model and the rest to the current one. Compare quality signals (user ratings, task success, eval scores on sampled outputs), latency and cost. Only switch fully if quality holds within the range you decided before the test.

## 222: What is LLM-as-a-judge and what does it cost?

It is using an LLM to grade the outputs of another LLM. It is cheaper than human review but still costs tokens for every graded item, and a strong judge model can be expensive. Grade a sample instead of everything, use a cheaper judge where it agrees with humans, and use the batch API for offline evals.

## 223: How do you keep evaluation costs under control?

Use a fixed, small but well-chosen eval set for quick checks and a larger one only before big releases. Cache model outputs for unchanged inputs and prompts. Run offline evals with the batch API, and sample production traffic instead of grading all of it.

## 224: Why can the same open model have different prices and speeds on different providers?

Providers use different hardware, serving software, quantization levels and batch sizes. One may run the model in FP8 on fast GPUs with speculative decoding, another in full precision on older GPUs. Compare price, speed and also quality, because heavier quantization can reduce quality a bit.

## 225: How can provider quantization affect quality?

Some providers serve open models in lower precision (FP8, INT4) to save cost. Usually the quality drop is small, but on some tasks like math, code or long structured outputs it can be noticeable. Run your eval set on each provider before picking the cheapest one.

## 226: What are the pros and cons of using a model through a cloud platform (Bedrock, Azure, Vertex AI) instead of directly?

Pros: one bill with your other cloud costs, private networking, region choice, existing compliance and committed spend discounts. Cons: new models and features may arrive later, prices and limits can differ, and APIs may be slightly different. Latency can be better if your app runs in the same cloud and region.

## 227: What is cross-region inference?

Some cloud platforms can send your request to another region when the local region is busy. It gives you higher limits and fewer errors. It can add some network latency and may not be allowed if you have strict data residency rules.

## 228: How do you size provisioned throughput?

Look at your peak traffic in tokens per minute, split into input and output, and the latency you need. Providers give guidance on how many tokens per minute one unit handles for each model. Buy enough units for normal peaks and send the extra (spillover) to pay-as-you-go.

## 229: What is spillover in provisioned deployments?

Spillover means that when your provisioned capacity is full, extra requests go to a standard pay-as-you-go deployment instead of failing. It lets you buy capacity for normal load instead of the absolute peak. Spillover traffic may be slower and is billed at normal per-token prices.

## 230: What is vLLM?

vLLM is a popular open source engine for serving LLMs. It has continuous batching, PagedAttention for memory management, prefix caching, quantization support and an OpenAI-compatible API server. It is one of the standard ways to self-host open models with high throughput.

## 231: How do you start an OpenAI-compatible server with vLLM?

Install vLLM and run `vllm serve` with a model name. Then call it with any OpenAI client by changing the base URL.

```bash
pip install vllm
vllm serve Qwen/Qwen3-8B --max-model-len 16384 --gpu-memory-utilization 0.9
```

```ts
const local = new OpenAI({
  baseURL: "http://localhost:8000/v1",
  apiKey: "none",
});
const res = await local.chat.completions.create({
  model: "Qwen/Qwen3-8B",
  messages: [{ role: "user", content: "Hello" }],
});
```

## 232: What GPUs are common for LLM inference?

Common data center GPUs are NVIDIA L4 and L40S (smaller models, lower cost), A100 and H100 (the standard for larger models), H200 (more memory), and the newer Blackwell B200 and GB200. AMD MI300X and MI325X are also used. The main things to compare are memory size, memory bandwidth and price per hour.

## 233: How do you estimate how much GPU memory a model needs for its weights?

Multiply the number of parameters by the bytes per parameter. 16-bit is 2 bytes, 8-bit is 1 byte, 4-bit is about 0.5 bytes. A 70B model in 16-bit needs about 140 GB just for weights, about 70 GB in 8-bit, and about 35 GB in 4-bit. You also need extra memory for the KV cache and runtime.

## 234: Why is GPU memory left after the weights important?

That memory holds the KV cache for active requests. More free memory means you can serve more requests at once and longer contexts. If the weights barely fit, the server works but handles only a few users, so the cost per token is high.

## 235: How should you autoscale a self-hosted LLM service?

CPU usage is a bad signal for GPU workloads. Scale on metrics like queue length, number of running and waiting requests, KV cache usage, or TTFT. Account for slow startup (loading weights can take minutes), so scale up early and keep some spare capacity.

## 236: What are the trade-offs of scaling a GPU deployment to zero?

You pay nothing when there is no traffic, which is great for rare or internal tools. But the first request after idle hits a cold start that can take tens of seconds or minutes. It fits batch jobs and low-traffic tools, not user-facing features that need fast answers.

## 237: Can you use spot or preemptible GPUs for LLM work?

Yes, for work that can be stopped and restarted, like batch inference, evals and data processing. Spot GPUs can be much cheaper than on-demand. They can be taken away with little notice, so use a queue and retries, and do not rely on them for real-time traffic.

## 238: What are Ollama and llama.cpp good for?

They make it easy to run open models on a laptop or a single machine, including CPU and Apple Silicon. They are great for local development, testing prompts without API costs, offline use and small internal tools. For high-traffic production serving, engines like vLLM, SGLang or TensorRT-LLM usually give much better throughput.

## 239: When does running a model on the user's device make sense?

When tasks are simple (short summaries, autocomplete, classification), privacy matters, or you want zero per-request cost and offline support. Examples are Chrome's built-in AI APIs, Apple's on-device models and small models via WebGPU. The limits are smaller models, device differences and download size.

## 240: What is a checklist for lowering TTFT?

Shorten the prompt, use prompt caching for the static part, pick a smaller or faster model, lower reasoning effort, call a region close to your servers, reuse HTTP connections, and avoid extra LLM calls before the main one. If you self-host, look at queue time, prefix caching and chunked prefill settings.

## 241: What is a checklist for lowering total generation time?

Ask for shorter outputs and set `max_tokens`, use a faster model or provider, lower reasoning effort, return IDs or diffs instead of long text, and split independent parts into parallel calls. Use structured output to avoid retries. If you self-host, use speculative decoding and quantization.

## 242: What is a latency budget?

A latency budget is the total time you allow for a user action, split across each step. For example: 100 ms network, 200 ms retrieval, 500 ms until the LLM's first token, then streaming. It helps you see which step needs work and stops one slow step from eating the whole time.

## 243: How does a voice assistant pipeline affect latency?

A classic voice pipeline has speech-to-text, then the LLM, then text-to-speech. If each step waits for the previous one to finish completely, delays add up to several seconds. You stream every step: transcribe while the user speaks, start the LLM as soon as they stop, and start speaking the first sentence while the rest is still being generated.

## 244: When are speech-to-speech realtime APIs worth their cost?

Realtime APIs that take and return audio directly can respond faster and sound more natural, because there is no separate STT and TTS step. Audio tokens are usually priced higher than text tokens, so long calls can get expensive. They make sense for live voice agents; for anything that is not live, a cheaper text pipeline often works.

## 245: How can you precompute LLM answers to cut latency?

If you can guess what users will ask, generate the answers ahead of time in a batch job and serve them from a cache or database. Examples are product summaries, FAQ answers and daily reports. The user gets an instant answer, and batch pricing cuts the cost.

## 246: How can splitting a long answer into parallel calls help?

If a long document has independent sections, generate each section in its own call at the same time. Total time is about the time of the longest section instead of all of them added together. The downside is that sections may be less consistent, and you pay for the shared context in every call.

## 247: Why should you reuse your SDK client instead of creating a new one per request?

The client keeps a pool of HTTP connections. Creating a new one each time means new TCP and TLS handshakes, which add latency on every call. Create one client when the app starts and reuse it.

```ts
// good: one shared client per process
export const openai = new OpenAI();

// bad: new client (and new connections) on every request
async function handler() {
  const client = new OpenAI();
  // ...
}
```

## 248: What should you watch for when streaming from serverless functions?

Serverless platforms have time limits, and some buffer responses by default. Use runtimes and settings that support streaming (for example streaming responses on Vercel, or AWS Lambda response streaming) and set the max duration high enough for long answers. Long agent runs may be better as background jobs.

## 249: Should you use SSE or WebSockets for LLM streaming?

SSE is simpler and enough for most chat apps, since data goes from server to client and it works over normal HTTP. WebSockets make sense when both sides send data all the time, like realtime voice or collaborative editing. Both stream tokens at the same speed; the model is the slow part.

## 250: Does using stored conversation state (like previous_response_id) save tokens?

Not on its own. With features like OpenAI's `previous_response_id` or the Conversations API, you do not have to resend the history, but the model still reads it and you are still billed for those input tokens. The win is simpler code and usually good cache hits, not free history.

## 251: What is context compaction?

Compaction means replacing a long conversation or agent history with a shorter version when it gets close to a size limit. Usually a model summarizes the old part and keeps the recent turns in full. Some APIs and tools now do this for you; you can also build it yourself with a cheap model.

## 252: How does a long-term memory system save tokens?

Instead of keeping the full history in every prompt, you store important facts (user preferences, past decisions) in a database. For each new request you retrieve only the few facts that matter. The prompt stays small even after months of use.

## 253: When can you replace an LLM call with embeddings?

For tasks like classification into fixed categories, finding duplicates, or matching a question to an FAQ, you can compare embeddings instead of calling a chat model. Embeddings are much cheaper and faster. Keep an LLM fallback for the cases where the similarity score is not clear.

## 254: When should you not use an LLM at all?

When normal code can do the job reliably: regex for emails and dates, a parser for structured files, a database query for exact lookups, simple rules for routing. That code is faster, free per call and easier to test. Use LLMs for the parts that really need language understanding.

## 255: How do moderation and guardrail checks affect latency and cost?

Every check adds a step. If you run input moderation, then the main call, then output checks one after another, latency adds up. Run input checks in parallel with the main call and cancel the main call if the check fails, and use small fast models or free endpoints (like OpenAI's moderation endpoint) for the checks.

```ts
const mainController = new AbortController();

const [check, answer] = await Promise.allSettled([
  moderate(input).then((r) => {
    if (r.flagged) mainController.abort();
    return r;
  }),
  generate(input, { signal: mainController.signal }),
]);
```

## 256: How do validation retries affect cost?

If you validate the output and retry on failure, every retry is a full new call. A 10% failure rate means about 10% extra cost and much higher latency for those requests. Lower the failure rate with structured output and clearer prompts, and when you retry, send only the error to fix instead of starting from scratch when you can.

## 257: Why compare models by cost per task and not cost per token?

A model with cheaper tokens might use more of them (longer answers, more reasoning, different tokenizer) or need retries, so it can cost more per finished task. Measure the full cost to complete a task on your eval set, including retries and tool calls. That is the number that matters.

## 258: Where can you find independent data on model speed and price?

Sites like Artificial Analysis and OpenRouter publish measurements of price, TTFT and output speed for many models and providers. They are good for a first shortlist. Your own tests matter more, because your prompt lengths, region and traffic pattern change the results.

## 259: How do you monitor LLM latency from your users' point of view?

Measure on the client or at your edge, not only at the provider call. Record TTFT and total time per request with the region and feature, and add synthetic checks that call your endpoint every few minutes. This catches problems in your own stack, like slow retrieval or proxy buffering, not only provider slowness.

## 260: What is an SLO for an LLM feature?

An SLO (service level objective) is a target you set for your service, for example "p95 TTFT under 2 seconds and 99.5% success rate over 30 days". It turns "fast enough" into a number you can watch. When you are close to missing it, you act: switch to a faster model, scale up, or turn on a fallback.

## 261: What is a circuit breaker and why use it with LLM providers?

A circuit breaker stops sending requests to a provider after many failures in a row, and sends traffic to a fallback instead. After a while it tries the provider again. It stops your app from waiting on timeouts during an outage and avoids wasting money on retries that will fail.

## 262: What is request deduplication for LLM calls?

If several identical requests come in at the same time (for example many users opening the same page), you make one LLM call and share the result with all of them. This is sometimes called request coalescing or "singleflight". It saves money and protects rate limits during spikes.

```ts
const inFlight = new Map<string, Promise<string>>();

function dedupe(key: string, fn: () => Promise<string>) {
  if (!inFlight.has(key)) {
    inFlight.set(
      key,
      fn().finally(() => inFlight.delete(key)),
    );
  }
  return inFlight.get(key)!;
}
```

## 263: Why does idempotency matter when retrying agent steps?

If an agent step calls a tool that changes something (sends an email, charges a card) and you retry after a timeout, the action may run twice. Use idempotency keys for side effects and make retries safe. Otherwise you trade a latency problem for a correctness problem.

## 264: Can you put LLM-generated content behind a CDN?

Yes, if the content is the same for everyone, like a generated product description or a public article summary. Generate it once, store it and serve it from the CDN. Users get it in milliseconds and you pay for the generation only once.

## 265: How do you keep the prompt cache warm when you run many app servers?

The provider's cache is on their side, so which of your servers sends the request does not matter much. What matters is that all servers send the exact same prefix: same tool order, same system prompt text, no per-server values. Using the same `prompt_cache_key` for the same template also helps on OpenAI.

## 266: How do you design prompts for multi-tenant apps so caching works?

Put the parts shared by all tenants first (general instructions, tools), then the tenant-specific part (their settings or knowledge), then the user message. Requests from the same tenant then share a longer prefix. Do not mix tenant data into the shared part at the top.

## 267: How are image tokens calculated, roughly?

Most providers split the image into tiles or patches and charge a number of tokens per tile, so the cost grows with the resolution. Many also resize large images down before processing. Check the provider's formula, and test with your real images to see the token count in the usage object.

## 268: How are PDF inputs priced?

Providers that accept PDFs often convert each page into both text and an image, so you pay for text tokens plus image tokens per page. A 100-page PDF can easily be 100,000+ tokens. If you only need the text, extract it yourself first and send that.

## 269: How is video input usually priced?

Video is usually sampled into frames (for example 1 frame per second) plus the audio track, and each frame is billed like an image. A few minutes of video can be a lot of tokens. Lower the frame rate or cut the video to the part you need.

## 270: What is map-reduce summarization and what does it cost?

You split a long document into parts, summarize each part (map), then summarize the summaries (reduce). The map step can run in parallel, so it is fast. It costs a bit more than one long-context call because of the extra summary step, but it works with cheaper models and very long inputs.

## 271: What is the "refine" method for long documents and how does it compare to map-reduce?

Refine goes through the parts in order and updates a running summary with each new part. It keeps more connection between parts, but it is sequential, so it is slow, and the running summary is resent each step. Map-reduce is faster because of parallel calls.

## 272: What is "extract then reason"?

First use a cheap model to pull out only the relevant facts from large inputs, then send that short list of facts to a strong model for the hard reasoning. The expensive model sees far fewer tokens. It works well when most of the input is noise.

## 273: How can you choose the number of RAG chunks dynamically?

Instead of always sending the top 10, look at the similarity or reranker scores and only send chunks above a threshold, with a minimum and maximum. Easy questions may need 2 chunks and broad ones 8. This lowers the average cost without hurting hard questions.

## 274: How do hosted tools like web search add cost?

Built-in tools such as web search, file search or code execution often have their own fees, for example a price per 1,000 searches or per container session. The results they return are also added to the context as input tokens. Check both when you estimate costs for an agent.

## 275: What storage costs come with hosted vector stores and file search?

Hosted vector stores often charge per GB per day for stored data, on top of query and token costs. Small amounts are cheap or free, but large document sets kept for a long time add up. Delete old stores and files you no longer need.

## 276: Should you log every full prompt and response?

Full logs are very useful for debugging, but they cost storage and can hold sensitive data. Many teams log token counts and metadata for every request, and full text only for a sample, for errors, or with user consent. Set retention limits and remove personal data where needed.

## 277: How do you get token usage when streaming with OpenAI?

In the Responses API, the final `response.completed` event has the full response with `usage`. In the Chat Completions API, you pass `stream_options: { include_usage: true }` and the last chunk has the usage.

```ts
const stream = await client.chat.completions.create({
  model: "gpt-5-mini",
  messages,
  stream: true,
  stream_options: { include_usage: true },
});

for await (const chunk of stream) {
  if (chunk.usage) console.log(chunk.usage);
}
```

## 278: How do you get token usage when streaming with Anthropic?

The `message_start` event has the input token count and the `message_delta` events near the end have the output token count. With the SDK helper, you can just read `usage` from `finalMessage()`.

```ts
const stream = client.messages.stream({ model, max_tokens: 1024, messages });
const final = await stream.finalMessage();
console.log(final.usage.input_tokens, final.usage.output_tokens);
```

## 279: Why should you check prompt size before sending a request?

Very large prompts can be rejected for being over the context window, which wastes time, or they can cost far more than expected. Count or estimate tokens first and reject, trim or route them before calling the model. This also protects you from users pasting huge texts.

## 280: How do you trim input to fit a token budget?

Decide what is most important and cut from the least important parts first: oldest chat messages, lowest-ranked RAG chunks, then long tool results. Never cut the system instructions or the user's question. Count tokens after trimming to be sure it fits.

## 281: What is the "lost in the middle" problem and why does it matter for cost?

Models often pay less attention to information in the middle of a very long prompt than at the start or end. So sending more context does not always mean better answers; you may pay for tokens the model mostly ignores. Send less but more relevant context, and put the most important parts near the start or end.

## 282: What are common examples of the cost vs latency trade-off?

Batch APIs and flex tiers are cheaper but slower. Priority tiers are faster but more expensive. Hedged requests lower tail latency but cost extra. Parallel calls are faster but can repeat shared context in each call. Bigger models may need fewer retries but are slower per token.

## 283: How would you approach cutting the cost of an existing LLM feature in half?

First measure: tokens per request split by prompt parts, cache hit rate, model, retries. Then go for the big wins: switch to a cheaper model where evals allow, fix the prompt order for caching, trim prompts and history, limit output length and move background work to the batch API. Check quality with evals after each change.

## 284: How do you split tokens in a request to see where the cost comes from?

Count tokens for each part of the prompt separately: system prompt, tool definitions, examples, retrieved context, history, user message. Log these counts along with the output and reasoning tokens. Often one part, like tools or history, turns out to be most of the cost.

## 285: What is the cost of tokens that are never cached because they change each time?

Those are billed at the full input price on every call. If your prompt is 10,000 tokens and only the last 500 change, then 9,500 can be cached and the cost is low. If something near the top changes each time, all 10,000 are billed at full price. That is why prompt order matters so much.

## 286: How do you handle very long user inputs in a chat app?

Set a max input size in the UI and on the server. For big pasted texts or files, either summarize or chunk them and use retrieval, or ask the user what part matters. Show the user the limit instead of failing silently.

## 287: How does the Vercel AI SDK help with cost and latency work?

It gives one API for many providers, so switching or adding fallback models is easy. It handles streaming to the UI (`streamText`, `streamObject`, `useChat`), returns token usage in a common format, and works with gateways for routing and caching. You still have to design prompts and caching well yourself.

```ts
import { streamText } from "ai";

const result = streamText({
  model: "openai/gpt-5-mini",
  prompt: "Write a short product tagline for a water bottle.",
  onFinish({ usage }) {
    console.log(usage.inputTokens, usage.outputTokens);
  },
});
```

## 288: What is OpenRouter and how does it relate to cost?

OpenRouter is a service that gives one API for hundreds of models from many providers. It can route to the cheapest or fastest provider for an open model and fall back when one is down. You pay their prices (often close to the provider's own) plus any fees, in exchange for less integration work.

## 289: How do you compare TTFT across providers fairly?

Use the same prompt, same output length, same region for your client, at the same time of day, many times. Report p50 and p95, not one run. Also check if prompt caching is warm or cold, because it changes TTFT a lot.

## 290: How can you make tool descriptions cheaper without breaking tool use?

Keep descriptions short and clear, remove unused parameters, and use enums instead of long text explanations. Merge tools that do almost the same thing. Test that the model still picks the right tool after trimming.

## 291: What is a tool search or dynamic tool loading feature?

Instead of sending all tool definitions every time, the model first gets a small search tool, or a short list, and only loads full tool definitions when it needs them. This keeps the prompt small when you have hundreds of tools. Some providers and agent frameworks now support this.

## 292: How do you budget the context window in a RAG chat app?

Decide fixed shares of tokens: for example 1,500 for the system prompt, 4,000 for retrieved chunks, 2,000 for history, 500 for the question and 1,000 for the answer. Fill each part up to its limit and trim the rest. This keeps cost per request stable and predictable.

## 293: Why do you need a price table in your code or config?

Usage responses give token counts, not dollar amounts. To show cost per request, you multiply tokens by prices, so you need a table of prices per model, including cached, cache write, batch and reasoning rates. Keep it in config so you can update it when prices change.

```ts
const PRICES: Record<
  string,
  { input: number; cachedInput: number; output: number }
> = {
  "small-model": { input: 0.25, cachedInput: 0.025, output: 2.0 }, // example $ per 1M
  "large-model": { input: 1.25, cachedInput: 0.125, output: 10.0 },
};
```

## 294: How do you calculate cost when some input tokens are cached?

Split input into non-cached and cached tokens, and price each at its own rate. Add cache write tokens at the write rate if the provider charges one. Then add output tokens, which include reasoning tokens.

```ts
function cost(
  u: { input: number; cached: number; cacheWrite: number; output: number },
  p: any,
) {
  const uncached = u.input - u.cached - u.cacheWrite;
  return (
    (uncached * p.input +
      u.cached * p.cachedInput +
      u.cacheWrite * p.cacheWrite +
      u.output * p.output) /
    1_000_000
  );
}
```

Watch out: on OpenAI, `input_tokens` includes cached tokens, while on Anthropic, `input_tokens` only counts the uncached part and cache reads and writes are reported separately.

## 295: Why might your cost dashboard not match the provider's invoice?

Common reasons: an old price table, missing cache write or long-context rates, not counting reasoning tokens, counting cached tokens twice, missing calls from other services using the same key, or extra fees for tools and storage. Compare your numbers with the provider's usage export each month and fix the gaps.

## 296: How do you forecast LLM costs for next quarter?

Take current cost per active user or per action, multiply by expected growth, and add planned features. Include known changes like moving to a new model or new prices. Review the forecast monthly, because usage per user often grows as people find new ways to use AI features.

## 297: When does it make sense to use a different model for each step of a pipeline?

Almost always, if the steps are different. A small model can classify, extract or rewrite queries, a mid-size model can draft, and a strong model can handle the final hard reasoning. Each step uses the cheapest model that is good enough for that step.

## 298: How do you safely move a feature to a cheaper model?

Run the eval set on both models and compare quality, cost and latency. Look at the failures, not just the score. Then roll out slowly with an A/B test or a canary, watch quality metrics and user feedback, and keep a quick way to switch back.

## 299: What are good defaults for a new LLM feature to avoid cost surprises?

Start with a small or mid-size model, set `max_tokens`, put static content first for caching, limit chat history, add per-user rate limits, log usage with feature tags and set a budget alert. Add retries with backoff and a timeout. Then measure real usage before optimizing further.

## 300: What questions should you ask before choosing between real-time and batch processing?

Is a user waiting for the result? How fresh does it need to be? How many items are there? Can the work be retried later if it fails? If nobody is waiting and a delay of minutes or hours is fine, batch is usually much cheaper.

# Advanced Questions (301-450)

## 301: What are the prefill and decode phases of LLM inference?

Prefill is when the model processes all prompt tokens in one go and builds the KV cache; it ends with the first output token, so it decides TTFT. Decode is when the model generates the rest of the tokens one at a time, each step reading the KV cache; it decides TPOT. The two phases have very different hardware needs, which shapes most serving optimizations.

## 302: Why is prefill compute-bound and decode memory-bandwidth-bound?

In prefill, thousands of tokens are processed together, so each weight read from memory is used in many calculations and the GPU's math units are busy. In decode, each request adds only one token per step, so the GPU reads all the weights and the KV cache to do a small amount of math. The limit becomes how fast memory can be read, not how fast the GPU can compute.

## 303: What is arithmetic intensity and why does it matter for LLM serving?

Arithmetic intensity is the number of math operations per byte read from memory. If it is low, the GPU waits on memory; if it is high, it waits on compute. Decode with batch size 1 has very low intensity, and batching many requests together raises it, which is why batching makes GPUs so much more efficient.

## 304: What is the KV cache?

During attention, every token produces key and value vectors in every layer. The KV cache stores them so the model does not recompute them for earlier tokens on every new step. It makes decode fast, but it uses a lot of GPU memory and grows with context length and the number of active requests.

## 305: How do you estimate the size of the KV cache?

Per token, the size is: 2 (keys and values) × number of layers × number of KV heads × head dimension × bytes per value. Multiply by the number of tokens and the number of concurrent requests.

```python
def kv_cache_bytes(layers, kv_heads, head_dim, tokens, batch, bytes_per_value=2):
    return 2 * layers * kv_heads * head_dim * bytes_per_value * tokens * batch

# Example: 80 layers, 8 KV heads (GQA), head_dim 128, FP16
per_token = kv_cache_bytes(80, 8, 128, 1, 1)        # 327,680 bytes ≈ 0.31 MB
total = kv_cache_bytes(80, 8, 128, 32_000, 16)      # ≈ 168 GB for 16 requests of 32k tokens
```

## 306: How do Grouped-Query Attention (GQA) and Multi-Query Attention (MQA) reduce cost?

In standard multi-head attention, each query head has its own key and value heads. MQA shares one key/value head across all query heads, and GQA shares each key/value head across a group of query heads. This makes the KV cache several times smaller, so a server can fit more requests and longer contexts, with little quality loss.

## 307: What is Multi-head Latent Attention (MLA)?

MLA, used in DeepSeek models, compresses keys and values into a small latent vector and stores that in the cache instead of full keys and values. The KV cache becomes much smaller than with standard attention or even GQA. That allows bigger batches and longer contexts on the same hardware.

## 308: What is sliding window attention and how does it affect cost?

With sliding window attention, each token only attends to the last N tokens instead of the whole sequence. The KV cache for those layers stops growing past the window size, and attention cost per token stays fixed. Many models mix sliding window layers with some full attention layers to keep long-range understanding.

## 309: Why does attention cost grow faster than linearly with context length?

In full attention, each token looks at every earlier token. Processing a prompt of N tokens needs work that grows with N², and each decode step reads a KV cache of size N. Doubling the context more than doubles prefill time for long prompts, which is one reason long-context requests are priced higher.

## 310: What is FlashAttention?

FlashAttention is an optimized way to compute attention that splits the work into tiles that fit in the GPU's fast on-chip memory. It avoids writing the large attention matrix to slow GPU memory. The result is the same math with much less memory traffic, so it is faster and uses less memory, especially for long sequences.

## 311: What is the difference between static batching and continuous batching?

With static batching, a group of requests starts together and the batch finishes only when the longest one is done, so short requests wait and GPU slots sit idle. With continuous (in-flight) batching, the scheduler adds new requests and removes finished ones at every decode step. GPU use stays high, and throughput can be many times better.

## 312: What is PagedAttention?

PagedAttention, introduced by vLLM, stores the KV cache in small fixed-size blocks instead of one big continuous area per request, similar to memory pages in an operating system. It removes most wasted memory from reserving space for the max length. More requests fit in memory, and blocks can be shared between requests with the same prefix.

## 313: What is automatic prefix caching in self-hosted engines?

Engines like vLLM and SGLang can keep KV cache blocks from earlier requests and reuse them when a new request starts with the same tokens. The shared part skips prefill, which cuts TTFT and GPU work. SGLang's RadixAttention stores prefixes in a tree so many requests with partly shared prefixes can reuse them.

## 314: What is chunked prefill?

Chunked prefill splits a long prompt's prefill into smaller chunks and runs them mixed in with decode steps of other requests. Without it, one huge prompt can block the GPU and make all other users' token streams pause. It gives smoother TPOT for everyone, at the cost of a slightly higher TTFT for the long request.

## 315: What is prefill-decode interference?

When prefill and decode run on the same GPU, a big prefill job slows down the decode steps of all running requests, and many decode requests can delay new prefills. This hurts both TTFT and TPOT under mixed load. Chunked prefill and separate prefill and decode servers are the main fixes.

## 316: What is disaggregated prefill and decode serving?

Prefill and decode run on separate groups of GPUs. Prefill workers process prompts and send the KV cache over a fast network to decode workers, which generate tokens. Each group can be sized and tuned for its own job, which helps meet strict TTFT and TPOT targets at scale. Frameworks like NVIDIA Dynamo, llm-d and SGLang support this.

## 317: What is speculative decoding?

A small, fast draft model (or another cheap method) guesses the next several tokens, and the big model checks all of them in one forward pass. Correct guesses are accepted; at the first wrong one, the big model's own token is used. The output is the same as without it, but you get several tokens per big-model step, so decode is faster.

## 318: What decides how much speculative decoding helps?

The acceptance rate (how often draft tokens are right), how cheap the draft is compared with the target model, and how many tokens are drafted per step. Predictable text like code or structured output gets high acceptance. If the draft is often wrong, you pay for drafting and checking with little gain.

## 319: What are EAGLE, Medusa and n-gram speculation?

They are speculative decoding methods that do not need a fully separate draft model. Medusa adds extra prediction heads to the main model, and EAGLE trains a small head that uses the main model's hidden states to predict future tokens. N-gram or prompt lookup speculation copies likely continuations from the prompt itself, which works well for editing and summarizing.

## 320: When can speculative decoding make throughput worse?

At large batch sizes the GPU is already busy, so the extra work of drafting and checking rejected tokens takes compute away from other requests. Speculative decoding helps most when the server is lightly loaded and decode is memory-bound. Many engines let you turn it off above a certain load, or tune it per workload.

## 321: What is tensor parallelism?

Tensor parallelism splits each layer's weight matrices across several GPUs, so each GPU does part of every layer's math. It lets models that do not fit on one GPU run, and it lowers per-token latency because work is shared. It needs very fast links between GPUs (like NVLink) because GPUs exchange data in every layer.

## 322: What is pipeline parallelism?

Pipeline parallelism puts different layers on different GPUs or nodes, and data flows from one stage to the next. It needs less communication bandwidth than tensor parallelism, so it works across nodes. The downside is that stages can wait on each other, which adds latency unless many requests are in flight.

## 323: What is a Mixture of Experts (MoE) model and how does it affect cost?

An MoE model has many "expert" feed-forward blocks, and a router picks only a few of them for each token. So a model may have hundreds of billions of total parameters but use only a fraction per token. Compute per token is low, which makes it cheap to run per token, but all experts must still be in memory.

## 324: What is expert parallelism?

Expert parallelism puts different experts of an MoE model on different GPUs. Tokens are sent to the GPUs that hold their chosen experts and the results come back. It allows serving very large MoE models, but the all-to-all communication and uneven expert load must be managed carefully to keep latency low.

## 325: Why do MoE models need large batch sizes to be cost-efficient?

With small batches, each expert gets only a few tokens, so the GPU reads an expert's weights to do very little math. With large batches, each expert gets enough tokens to use the GPU well. That is why MoE models are very cheap at big-provider scale but can be less efficient to self-host with low traffic.

## 326: What quantization formats are common for inference?

Common ones are FP8 (well supported on H100 and newer, small quality loss), INT8, and 4-bit weight formats like AWQ and GPTQ. Newer GPUs support FP4 formats such as NVFP4 and MXFP4; OpenAI's gpt-oss models ship with MXFP4 weights for their MoE layers. Lower bits mean less memory and faster decode, with more risk to quality.

## 327: What is the difference between weight-only and weight-and-activation quantization?

Weight-only quantization (like 4-bit AWQ) stores weights in low precision but does the math in higher precision. It mostly speeds up memory-bound decode. Quantizing both weights and activations (like FP8 W8A8) also makes the math itself cheaper, which helps compute-bound prefill and large batches.

## 328: What is KV cache quantization?

It stores the KV cache in lower precision, for example FP8 instead of FP16. The cache takes about half the memory, so you can fit more concurrent requests or longer contexts. Quality impact is usually small but should be tested, especially for long-context tasks.

## 329: How do you check if quantization hurt quality?

Run your task-specific eval set on both the full and quantized models, not just general benchmarks. Look closely at math, code, long outputs, rare languages and strict format tasks, since those break first. Compare cost and speed gains with the quality drop to decide.

## 330: How do you estimate the upper limit of decode speed for one request?

At batch size 1, each token needs the GPU to read all active weights once. So max tokens per second ≈ memory bandwidth / bytes of active weights. For example, a GPU with about 3.35 TB/s of bandwidth running a 70B model in FP8 (about 70 GB) can do at most about 48 tokens per second for one request. Real numbers are lower, but this shows why bandwidth and model size decide speed.

## 331: How does batch size affect TPOT and throughput in self-hosted serving?

As batch size grows, total throughput rises a lot because the weight reads are shared across more requests. TPOT for each request also rises, slowly at first and faster once the GPU becomes compute-bound or the KV cache reads dominate. You pick the batch size where throughput is high and TPOT still meets your target.

## 332: What is goodput?

Goodput is the number of requests per second that meet your latency targets (for example TTFT under 1 s and TPOT under 50 ms). Raw throughput can look high while many requests are too slow to be useful. Tuning for goodput instead of raw throughput gives better real-world results.

## 333: What vLLM settings affect latency and throughput the most?

Important ones are `--max-num-seqs` (max concurrent requests), `--max-num-batched-tokens` (tokens per scheduler step, important with chunked prefill), `--gpu-memory-utilization` (how much memory goes to weights plus KV cache), `--max-model-len`, tensor parallel size, quantization and prefix caching. Raising concurrency gives more throughput but higher TPOT.

## 334: What happens when the KV cache runs out of memory during serving?

The engine must free space. Engines like vLLM preempt some running requests: they either drop their KV cache and recompute it later or swap it to CPU memory. Preemption keeps the server alive but causes latency spikes for the preempted requests. Frequent preemption means you are overloaded or your limits are set too high.

## 335: Why is long-context serving expensive even with a good engine?

Each long request needs a large KV cache, so fewer requests fit at once, and the throughput per GPU drops. Prefill of long prompts takes a lot of compute, and each decode step reads a large cache. Prefix caching, KV quantization, sliding window models and offloading help, but long contexts still cost more per request.

## 336: What are CUDA graphs and why do serving engines use them?

A CUDA graph records a sequence of GPU kernel launches once and replays it with low overhead. In decode, each step is small, so the CPU time to launch many kernels can be a big share of the step time. Replaying graphs cuts this overhead and lowers TPOT, especially at small batch sizes.

## 337: How do vLLM, SGLang and TensorRT-LLM compare?

All three support continuous batching, prefix caching, quantization and parallelism. vLLM is very popular and supports many models and hardware types. SGLang is strong at prefix reuse (RadixAttention) and structured generation. TensorRT-LLM is NVIDIA's engine with heavily tuned kernels for NVIDIA GPUs, often the fastest there but with more setup.

## 338: How do you serve many LoRA fine-tunes cheaply?

Load one base model and many small LoRA adapters, and apply the right adapter per request. Engines like vLLM support multi-LoRA serving, and requests for different adapters can share a batch. You avoid running a separate full model for each customer or task, which saves a lot of GPU memory.

## 339: How does constrained decoding for structured output affect speed?

The engine uses a grammar (from a JSON schema or regex) to block tokens that would break the format at each step. Building the grammar and checking tokens adds some overhead, and complex schemas can slow decode. Modern libraries like XGrammar and llguidance make this overhead small, and caching compiled grammars helps.

## 340: How do you calculate the cost per million tokens when self-hosting?

Divide the hourly cost of the hardware by the number of tokens it produces per hour at your real load. Use real throughput at your latency target and real utilization, not the peak benchmark number.

```python
gpu_cost_per_hour = 4 * 3.00        # 4 GPUs at $3/hr (example)
tokens_per_second = 2500            # output tokens/s at target latency
utilization = 0.5                   # share of hours with real traffic

tokens_per_hour = tokens_per_second * 3600 * utilization
cost_per_million = gpu_cost_per_hour / tokens_per_hour * 1_000_000
print(round(cost_per_million, 2))   # ≈ 2.67 $ per 1M output tokens
```

## 341: How do you decide if self-hosting is cheaper than an API?

Compare the API cost per million tokens with your self-hosted cost per million at your real utilization, plus the cost of people to run it. Self-hosting usually wins only with high, steady volume, a model that fits well on your hardware, and a team that can run GPU infra. Low or spiky traffic almost always favors the API.

## 342: Why is utilization the most important number in self-hosting economics?

You pay for GPUs every hour, whether they are busy or idle. A GPU that is busy 20% of the time costs five times more per token than one busy 100% of the time. Providers have high utilization because they mix traffic from many customers, which is hard to match on your own.

## 343: What hidden costs come with self-hosting LLMs?

Engineering time to set up and tune the engine, on-call and monitoring, model updates and testing, spare capacity for peaks, storage and network for model weights, security work and failed experiments. GPU availability can also be a problem in some regions. These often cost more than the GPUs themselves for small teams.

## 344: What is KV-cache-aware routing?

When you run several model replicas, a smart router sends requests to the replica that already has the matching prefix in its KV cache. That gives more prefix cache hits, lower TTFT and less GPU work. Tools like llm-d, NVIDIA Dynamo and the vLLM production stack router have this feature; a plain round-robin load balancer spreads prefixes randomly and loses most of the benefit.

## 345: Why does session affinity help self-hosted chat performance?

In a chat, each new turn starts with the full previous conversation. If it goes to the same replica as the last turn, the earlier tokens are likely still in that replica's prefix cache. Sticky routing by conversation ID gives many cache hits; the trade-off is less even load across replicas.

## 346: How do you speed up model loading for autoscaling?

Store weights in `safetensors` format, keep them on fast local NVMe or a node-level cache instead of downloading from the internet each time, and use parallel or streaming loaders. Prebuilt container images and keeping warm standby replicas help too. The goal is to bring cold start from minutes down to seconds.

## 347: Can you run several models on one GPU?

Yes, if they fit in memory together, for example small models or LoRA adapters on one base model. Tools like NVIDIA MIG split a GPU into isolated parts, and some engines can host several models. It improves utilization for low-traffic models, but the models compete for memory bandwidth, so latency can suffer under load.

## 348: When is CPU inference a reasonable choice?

For small models (a few billion parameters or less) that are quantized, low traffic, and tasks where a few tokens per second is fine, like background tagging. CPUs are cheap and easy to get. For larger models or user-facing chat speed, GPUs or other accelerators are much more cost-effective per token.

## 349: Why are some providers, like Groq and Cerebras, much faster per request?

They use custom chips designed to avoid the memory bandwidth bottleneck, for example by keeping model weights in large amounts of very fast on-chip memory (SRAM) spread across many chips. That gives very high tokens per second for a single request. The trade-offs can be model choice, context length limits and price.

## 350: What other accelerators besides NVIDIA GPUs are used for inference?

Google TPUs (used for Gemini and available on Google Cloud), AWS Inferentia and Trainium, AMD Instinct GPUs, and custom chips from companies like Groq, Cerebras and SambaNova. They can offer better price per token for some models. The trade-off is software support, since most open source tools are tuned for NVIDIA first.

## 351: Why are cached input tokens so much cheaper for providers to serve?

A cache hit means the provider can reuse the KV cache it already computed for that prefix, so it skips most of the prefill work for those tokens. Prefill is the compute-heavy part, so skipping it saves real GPU time. The provider still pays to keep the cache in memory or fast storage, which is why caches expire and why some charge for writes or storage.

## 352: Why can providers offer batch processing at about half price?

With batch jobs, the provider can run the work whenever they have free capacity, for example at night or between traffic peaks. GPUs that would otherwise sit idle get used, and they can pack batches more fully. You give up speed and they give you part of the savings.

## 353: Why do providers charge more for very long contexts?

Long prompts need more prefill compute (attention grows faster than linearly), a much larger KV cache per request, and they reduce how many other requests can share the GPU. So each long request uses a bigger share of the hardware. Higher long-context prices reflect that.

## 354: Why do providers have rate limits even for paying customers?

GPU capacity is limited and shared. Rate limits stop one customer from using so much capacity that others get slow or fail, and they protect against bugs and abuse. Limits also let providers plan capacity; if you need more, you can usually move up a tier or buy provisioned capacity.

## 355: What causes tail latency in hosted LLM APIs?

Common causes are queueing when the provider is busy, very long outputs, cache misses on long prompts, preemption on the provider side, routing to a far or busy region, retries after errors and slow tool calls in agents. Reasoning models add more variation because thinking length changes per request. Look at what the slow requests have in common in your logs.

## 356: What are the costs and risks of hedged requests at scale?

Each hedge is an extra request that you pay for in full, even if you cancel it, at least for the tokens generated so far. If you hedge at the p95, you add about 5% more requests but cut the worst tail. If you hedge too early, or during a provider overload, you can double your load and make the overload worse, so add a cap on the hedge rate.

## 357: How would you design a latency budget for a RAG chatbot with a 1.5-second TTFT target?

Measure each step and give it a budget, for example: 50 ms auth and setup, 150 ms query embedding, 100 ms vector search, 200 ms reranking, and about 1 second for the LLM's TTFT including network. If query rewriting is needed, it must fit in the same budget, so use a tiny model or skip it for simple questions. Run independent steps like history loading and embedding in parallel and keep the prompt prefix cacheable.

## 358: Scenario: your chatbot's TTFT is 6 seconds. How do you find and fix the cause?

First break down the 6 seconds with tracing: time before the LLM call (auth, retrieval, extra LLM calls), network, and the provider's TTFT. Common causes are a chain of LLM calls before the main one, a huge prompt with no cache hits, a reasoning model with high effort, or proxy buffering that hides streaming. Fix the biggest part first: parallelize pre-steps, reorder the prompt for caching, trim context, lower reasoning effort, or switch to a faster model.

## 359: Scenario: each agent task costs $2 and needs to cost $0.30. What do you do?

Look at a few traces and split the cost by step, tool results, history and reasoning. Typical fixes are: a cheaper model for most steps with the strong model only for planning or hard steps, smaller tool outputs, clearing old tool results, keeping the prefix stable for caching, lower reasoning effort, and a step limit. Measure task success on an eval set after each change, because the goal is cost per successful task.

## 360: Scenario: you need to classify 10 million documents once. What is the cheapest reliable approach?

Use the batch API with the smallest model that passes your eval, or a fine-tuned small model, with a short prompt and an output of just the label. Put the shared instructions in a cacheable prefix, and send only the parts of each document needed for the decision. If categories are simple, try embeddings with a small classifier first and send only the unclear cases to an LLM.

## 361: Scenario: a code autocomplete feature must respond in under 200 ms. How do you design it?

Use a small, fast model trained for code completion, hosted close to users or on fast hardware. Send only the nearby code context, keep a stable prefix for caching, limit the output to a short completion and stop early with stop sequences. Cancel requests when the user keeps typing, and debounce input so you do not send a request for every keystroke.

## 362: Scenario: a voice agent must start speaking within 800 ms after the user stops talking. How?

Stream every stage: streaming speech-to-text, fast end-of-speech detection, a fast LLM with a short cached prompt, and streaming text-to-speech that starts on the first phrase. Keep the response short and avoid tool calls in the first reply, or play a short filler while a tool runs. A speech-to-speech realtime model can cut stages entirely, at a higher price per minute.

## 363: Scenario: in a multi-tenant SaaS, one tenant uses 60% of your LLM budget. What do you do?

Check if it is legitimate use or a bug, for example an integration in a retry loop. Add per-tenant quotas and rate limits so one tenant cannot block others, and route their traffic through a fair-share queue. If the use is legitimate, move them to a usage-based plan or a higher tier that covers the cost.

## 364: Scenario: your prompt cache hit rate is only 10% even though all requests share a long system prompt. Why?

Something at the start of the prompt changes per request: a timestamp, request ID, user name, random example order, or tools added in a different order. JSON serialization with unstable key order can also do it. Diff the exact prompts of two requests, move the changing parts to the end, and check the cached token counts again. Also check that traffic is frequent enough that the cache does not expire between requests.

## 365: Scenario: your main provider's latency suddenly doubles. How should your system respond?

Monitoring should alert on p95 TTFT and total latency per provider. A circuit breaker or latency-based router should move part or all of the traffic to a backup model or region when latency stays over the threshold. Lower non-critical traffic (background jobs, optional features) to protect the main user flow, and switch back slowly when the provider recovers.

## 366: Scenario: users ask many questions about the same 500-page contract. How do you keep it cheap and fast?

Options: RAG over the contract so each question sends only the relevant clauses, or long context with explicit or provider prompt caching so the full contract is paid at the full price only once per cache period. For many questions over hours or days, RAG is usually cheaper; for deep reasoning across the whole document in one session, long context with caching gives better answers. You can also precompute a structured summary of key terms.

## 367: Scenario: one user sends thousands of requests per hour. How do you protect the system?

Apply per-user and per-IP rate limits at the edge, input size limits and per-user token budgets. Detect automation with patterns like constant timing or identical prompts, and require stronger auth or captchas. Log and alert on users whose usage is far above normal, and make sure limits are checked before the LLM call, not after.

## 368: Scenario: you want to move from a closed flagship model to a self-hosted open model. What is your plan?

Build an eval set from real traffic and compare candidate open models on quality, speed and estimated cost at your volume. Load test the chosen model on your target hardware and engine with real prompt lengths to get real throughput at your latency target. Roll out with shadow traffic, then a small share of real traffic, keep the old model as a fallback, and compare the full cost including operations.

## 369: Scenario: a nightly batch job sometimes does not finish before the morning. What can you change?

Split the work into smaller batches and submit them earlier or spread through the night. Check for retries and failed items that block completion. If batch APIs are too slow at times, send the most urgent part through normal or flex APIs with a concurrency limit, and keep the rest in batch. Also check if some items can be skipped because they did not change.

## 370: Scenario: a structured extraction job fails validation 15% of the time. How do you lower cost?

Switch to strict schema-based structured output so format errors go away. Look at the failing cases: if they are content errors, make the instructions clearer, add one or two targeted examples, or use a stronger model only for retries. When you retry, send the validation error with the previous output instead of running the full task again from scratch.

## 371: Scenario: a support app summarizes long chat threads for agents. How do you keep cost and latency low?

Summarize incrementally: keep a running summary per thread and update it with only the new messages instead of reprocessing the full thread every time. Use a small model and a fixed output format. Run the update in the background when new messages arrive, so the summary is ready when an agent opens the ticket.

## 372: Scenario: you want an AI summary at the top of every search results page. How do you make it affordable?

Most search traffic repeats the same popular queries, so cache summaries per normalized query and result set, with a TTL. Only generate for queries with enough results, use a small model with short output, and stream it in after the normal results so the page is not blocked. For the long tail of rare queries, generate on demand or skip.

## 373: Scenario: you must generate descriptions for 2 million products. How do you plan cost?

Estimate tokens per product from a sample, multiply by 2 million and by batch prices for a few candidate models. Test quality on a sample of a few hundred products first. Use the batch API, a short prompt with shared instructions in the prefix, and only the product fields that matter. Generate again only when product data changes.

## 374: Scenario: you need to answer questions over a 2-million-token codebase. Long context or RAG?

It does not fit in most context windows, and even if it did, sending it on every question would be slow and expensive. Use retrieval: code search, symbol indexes, file summaries and embeddings, plus an agent that can open files on demand. Cache stable parts like the repo overview and coding rules in the prompt prefix.

## 375: Scenario: a translation app is much more expensive for some languages. How do you handle it?

Some languages need many more tokens for the same text because of the tokenizer. Measure tokens per character per language, choose models with tokenizers that handle those languages better, and consider a model with lower prices for those language pairs. Price your product per character or per word, not per request, so the user's cost follows yours.

## 376: Scenario: a document pipeline processes scanned invoices with images. How do you reduce cost?

Resize and crop images to the needed area, and use lower detail settings when the text is large and clear. Try OCR first and send text to a cheaper text model, falling back to a vision model only when OCR confidence is low. Use the batch API since invoices rarely need instant results.

## 377: Scenario: you must moderate every message in a busy chat app in real time. What is the setup?

Use a free or cheap dedicated moderation model or classifier for every message, not a big LLM. Only send borderline cases to a larger model or a human. Run checks asynchronously when possible, showing the message right away and hiding it if flagged, if your policy allows that.

## 378: Scenario: an email assistant must handle millions of emails a day on a small budget. How?

Filter first with rules and cheap classifiers to skip spam, newsletters and emails that need no action. Use a small model for triage and a stronger one only for drafting replies on the important ones. Trim emails to the latest message and strip quoted history, signatures and HTML. Batch non-urgent work like daily digests.

## 379: How can you estimate a model's confidence to drive a cascade?

Options include: token log probabilities (when the API exposes them), asking the model to rate its own confidence, checking agreement between several cheap samples, running a validator or a small judge model, or rule-based checks like schema validity and required fields. Calibrate on labeled data, because raw model confidence is often not reliable.

## 380: How can log probabilities help with cost?

Logprobs show how sure the model is about each token. For classification you can read the probability of the label tokens and only escalate low-confidence cases to a bigger model or a human. Not all models or APIs return logprobs, especially reasoning models, so check support first.

## 381: How do learned routers work?

A learned router is a small model trained to predict whether a cheap model will answer a request well enough. It is trained on examples where both cheap and strong models answered and the answers were graded. Research projects like RouteLLM showed big cost savings at similar quality, but the router needs retraining when models or traffic change.

## 382: What are failure modes of model routing?

The router can send hard requests to the weak model and hurt quality without anyone noticing. It can drift as user behavior changes. It adds its own latency and cost. Users may also get inconsistent answers depending on which model they hit. Monitor quality per route and keep a sample of routed traffic for regular evaluation.

## 383: What security risks does a semantic cache add?

Cache poisoning: a user crafts a question so a bad answer is stored and served to others. Data leaks: one user's private answer is returned to another user with a similar question. Fix this by scoping caches per tenant or user for private data, caching only reviewed or public answers across users, and validating what goes into the cache.

## 384: How does a semantic cache scale to millions of entries?

It uses an approximate nearest neighbor index (like HNSW) in a vector database or Redis to find similar questions fast. Old and rarely used entries are evicted with TTLs or LRU rules. Lookups add a few milliseconds and an embedding call, which is small next to an LLM call, but only worth it if the hit rate is high enough.

## 385: How do you keep cached answers correct when the underlying RAG data changes?

Store which source documents and versions each cached answer used. When a document changes, invalidate the answers that used it, or include a data version in the cache key. For fast-changing data, use short TTLs or skip caching.

## 386: What is KV cache offloading?

It moves KV cache blocks that are not in use right now from GPU memory to CPU memory or SSD, and brings them back when needed. It lets a server keep many more prefixes and conversations cached than GPU memory allows. Tools like LMCache work with vLLM to do this, trading some transfer time for much less recompute.

## 387: Why would you keep KV cache for a conversation across turns?

Between turns, the user reads and types, which can take minutes. If the conversation's KV cache is kept (in GPU, CPU or SSD), the next turn only needs prefill for the new message. This cuts TTFT and GPU work for long chats and agent sessions a lot.

## 388: How do providers implement prompt caching, roughly?

Prompts are split into fixed-size blocks of tokens, each block is hashed together with everything before it, and the KV cache for those blocks is stored. Requests are routed so that matching prefixes land on machines that have the cache. That is why caching works only on exact prefixes, has a minimum length, and works in steps of a block size.

## 389: Why are LLM outputs sometimes not the same even at temperature 0?

On shared servers, your request is batched with others, and the batch size changes the order of floating point math in the GPU kernels. Tiny numeric differences can change which token is picked when two tokens are almost tied, and then the rest of the output differs. This matters for caching, testing and evals, since you cannot rely on exact repeats.

## 390: When is fine-tuning cheaper than prompting, in numbers?

Compare the cost of the long prompt on a general model with the cost of a short prompt on a fine-tuned model, plus training and any hosting fees. For example, if fine-tuning removes 3,000 tokens of instructions and examples from 1 million requests a month, that saves 3 billion input tokens a month. If the fine-tuned model's per-token price is not much higher, training pays off quickly at that volume.

## 391: What are the risks of replacing a big model with a small fine-tuned one?

The small model may handle the common cases well but fail on rare inputs, new topics or changes in the task. It needs retraining when your data or rules change, and you have to maintain the training pipeline. Keep a fallback to the big model for low-confidence cases and keep evaluating on fresh data.

## 392: Should you use a bigger model quantized or a smaller model at full precision?

For the same memory, a larger model at 8-bit or even 4-bit often beats a smaller model at 16-bit on quality. Very low bit widths (3-bit or less) can hurt badly, though. The answer depends on the task, so test both on your evals at the same cost and speed.

## 393: What is pruning and does it help inference cost?

Pruning removes weights, heads or whole layers that matter least, making the model smaller. Structured pruning (removing whole parts) gives real speedups on normal hardware; unstructured pruning (random zeros) needs special support to be faster. Pruned models usually need extra training to recover quality, and it is less common in practice than quantization or distillation.

## 394: How does tokenizer vocabulary size affect cost?

A larger vocabulary can encode text in fewer tokens, especially for code and non-English languages, so fewer decode steps and lower per-request cost. The trade-off is a bigger embedding and output layer. When comparing models, measure tokens per task on your own data, because tokenizers differ a lot.

## 395: What is multi-token prediction and how can it speed up inference?

Some models are trained to predict several future tokens at once using extra heads. At inference time, these extra predictions can be used as built-in drafts for speculative decoding. DeepSeek-V3 used multi-token prediction this way to speed up decoding.

## 396: How do reasoning models change capacity planning?

Output length becomes much less predictable, because the model may think for 200 or 20,000 tokens depending on the question. That makes cost and latency per request vary a lot, and long thinking holds GPU memory longer. Plan with percentiles, set thinking budgets or effort levels, and watch reasoning token counts per feature.

## 397: What is test-time compute scaling and what does it cost?

It means spending more compute at inference time to get better answers: longer reasoning, sampling several answers and picking the best (best-of-n), or voting between answers (self-consistency). Quality can improve, but cost grows roughly with the number of samples or reasoning tokens. Use it only for tasks where the extra accuracy is worth the price.

## 398: How can sampling several answers in parallel be cheaper than it looks?

When you ask for n answers to the same prompt (for example with an `n` parameter or parallel requests to a self-hosted engine), the prompt prefill can be done once and shared. Engines with prefix caching reuse the KV cache, so you mostly pay for the extra output tokens. On hosted APIs, check whether input is billed once or per sample.

## 399: Why is predicting output length useful for scheduling?

Short jobs stuck behind long jobs wait a long time. If the scheduler can estimate output length, it can run short jobs first or place requests more evenly, which lowers average and tail latency. Research systems do this with small predictor models; in practice, `max_tokens` and request type give a rough guess.

## 400: How do you give fair service to many tenants on a self-hosted LLM?

Use a scheduler with per-tenant queues and fair-share or weighted rules, so one tenant's flood of requests does not starve others. Set per-tenant concurrency and token limits. Some engines support request priorities; otherwise you can put a fair queue in front of the engine.

## 401: What is admission control and load shedding for LLM services?

Admission control decides whether to accept a new request based on current load, for example queue length or KV cache usage. When the system is overloaded, load shedding rejects or downgrades some requests (with a 429 or a cheaper model) instead of letting everything get slow. It protects latency for the requests you do accept.

## 402: How do you design backpressure for an LLM pipeline?

Put a bounded queue between producers and LLM workers. When the queue is full, producers slow down, wait or get a clear "try later" error instead of piling up work. Size workers to your rate limits, and expose queue length as a metric so you can scale or shed load early.

## 403: How do you enforce a rate limit across many app servers?

Keep the counters in a shared store like Redis and update them atomically, for example with a Lua script implementing a token bucket or sliding window. Each server checks and takes tokens before calling the model. Leave some headroom below the provider's limit, because counts are estimates until the response arrives.

```ts
// sliding window per minute with Redis (simplified)
async function allow(key: string, cost: number, limit: number) {
  const now = Date.now();
  const windowKey = `${key}:${Math.floor(now / 60_000)}`;
  const used = await redis.incrby(windowKey, cost);
  await redis.expire(windowKey, 120);
  return used <= limit;
}
```

## 404: How do you rate limit by tokens when you do not know the output length in advance?

Reserve tokens before the call using input tokens plus `max_tokens` (or a typical output length), then correct the count with the real usage after the call. This is close to how providers count against TPM limits too. It stops a burst of large requests from going far past the limit.

## 405: How do you account correctly for cached, reasoning and batch tokens in cost reports?

Store raw usage for every call: uncached input, cache reads, cache writes (with TTL type), output, reasoning, and whether it was batch or a special service tier. Apply the matching price for each part. Do not mix providers' field meanings, since they report cached tokens differently. Recompute history when you fix a price table mistake.

## 406: How do you reconcile your internal cost tracking with provider invoices?

Pull the provider's usage and cost exports regularly and compare them by day, model and project against your own numbers. Investigate gaps above a small threshold. Common gaps are untracked services, tool fees, storage fees and price changes. Agreed numbers let you trust per-feature and per-customer reports.

## 407: What is FinOps for AI, and what are showback and chargeback?

FinOps for AI is the practice of tracking, sharing and managing AI spend across teams. Showback means showing each team or feature what it spends. Chargeback means actually billing that cost to the team's budget. Both make teams care about efficiency instead of treating LLM calls as free.

## 408: How can you negotiate lower LLM prices?

At high volume, providers and cloud platforms offer committed spend discounts, enterprise agreements and provisioned capacity deals. Data on your current and forecast usage gives you a strong position. Having a working second provider also helps you negotiate, since you can move traffic.

## 409: What are the trade-offs of a multi-provider strategy?

Pros: better uptime with failover, the ability to pick the cheapest or best model per task, and more negotiating power. Cons: more integration and testing work, prompts that may need tuning per model, different features and caching rules, and harder cost tracking. A gateway and a shared eval set lower the cost of supporting several providers.

## 410: How do guardrails interact with streaming?

If you check the output only at the end, you lose the benefit of streaming or show text you might have to take back. Common approaches are checking the stream in chunks (sentences or every N tokens) and stopping if something bad appears, or buffering a short window before showing it. Pick based on risk: high-risk domains may need full checks before showing anything.

## 411: How can prompt injection be combined with cost attacks against agents?

Hidden instructions in a web page or file can tell an agent to fetch huge pages, call paid tools in a loop, or start sub-agents again and again. Each step costs tokens and maybe tool fees. Defenses are hard budgets per run, limits on tool calls per type, size limits on tool outputs, and stricter permissions for tools that cost money.

## 412: How do data residency and privacy rules affect cost and latency?

They may force you to use a specific region, a specific cloud platform or a zero-data-retention setup. Those may cost more, have fewer models, lower limits, or limit features like stored conversations or some caching options. Find out these rules early, because they change which providers you can use at all.

## 413: How do you benchmark LLM serving performance correctly?

Fix the prompt and output length distributions (taken from real traffic), the concurrency or request rate, and run long enough to reach a steady state. Report TTFT and TPOT percentiles, throughput and goodput together, with the hardware, engine version and settings. Warm up first and note whether prefix caching was on.

## 414: What are common mistakes in LLM performance benchmarks?

Using tiny prompts, testing only at concurrency 1, reporting only averages, measuring on the server instead of the client, ignoring cache effects, ignoring errors and timeouts, and comparing different output lengths. Also, tokens per second numbers from vendors often show best-case peak throughput, not latency at a realistic load.

## 415: How can Little's Law help with LLM capacity planning?

Little's Law says: requests in the system = arrival rate × time each request spends in the system. If you get 20 requests per second and each takes 8 seconds, about 160 requests are active at once. That tells you how much concurrency and KV cache memory you need, or how many concurrent API calls your rate limits must allow.

## 416: How do you estimate how many GPUs you need for a self-hosted model?

Measure the throughput of one replica at your latency target with real prompt and output lengths. Estimate your peak demand in tokens per second (input and output) from traffic forecasts. Divide peak demand by per-replica throughput, add headroom (often 20-30%) and at least one spare replica for failures.

```python
peak_output_tps = 6000          # output tokens/s at peak
replica_tps_at_slo = 1800       # measured per replica at target TPOT
gpus_per_replica = 2

replicas = -(-peak_output_tps * 1.3 // replica_tps_at_slo) + 1  # 30% headroom + 1 spare
print(int(replicas), int(replicas * gpus_per_replica))           # 6 replicas, 12 GPUs
```

## 417: Why does more context often not mean better answers?

Models get worse at finding and using the right information as the context fills with unrelated text, sometimes called "context rot". Extra tokens cost money and slow TTFT, and they can also lower quality. Well-chosen, smaller context is often both cheaper and more accurate.

## 418: What are the trade-offs of on-device models like Chrome's built-in AI?

They have zero per-request cost for you, keep data on the device and work offline, and have no network latency. But they are small models, availability depends on the browser, device and hardware, the first use may need a large model download, and speed varies by device. Use them for light tasks and fall back to a server model when not available.

## 419: How do you design a hybrid on-device and cloud setup?

Try the on-device model first for simple tasks and check if the result is good enough with simple rules. Send complex requests, or requests where the device model is missing or failed, to a cloud model. Keep the same interface for both so the UI does not care which one answered.

## 420: How do energy use and carbon fit into LLM cost decisions?

Energy use follows compute: bigger models, longer prompts and more output tokens all use more power. Smaller models, caching, shorter outputs and batching lower both your bill and energy use. Some companies track this for sustainability goals, and for self-hosting it is a real part of the bill.

## 421: How would you implement compaction for a long-running agent?

Watch the token count of the context. When it passes a threshold (say 70% of the window), ask a model to summarize older steps into a short state: goal, decisions, open tasks, key facts and file names. Replace the old messages with that summary, keep the latest steps in full, and continue. Test that the agent does not forget important details, and save the full history elsewhere for debugging.

## 422: How should you design tool outputs to be token-efficient?

Return compact, structured data with only the needed fields, cap list sizes and support pagination. Use short, clear error messages that tell the model what to try next. For large data, return a handle or summary and let the model request details only if needed.

## 423: Why should agent history be append-only for good caching?

Prompt caching works on the prefix. If you change or remove earlier messages, everything after the change becomes a cache miss and is billed at full price again. Appending new messages keeps the earlier part identical, so each step only pays full price for the new part. When you do need to compact, do it rarely and in big steps, not a little on every turn.

## 424: How does changing the tool list mid-conversation affect caching?

Tool definitions are usually at the very start of the prompt. Adding, removing or reordering a tool changes the prefix, so the whole conversation after it is a cache miss. Keep the tool list stable during a session, and if tools must change, prefer approaches that add them later in the context.

## 425: How do you decide between a cheaper model with more retries and a stronger model with fewer?

Calculate the expected cost per successful result: cost per attempt divided by success rate, plus the cost of checking each attempt. Do the same for latency. A model that is three times cheaper but succeeds only half as often, with extra validation calls, may end up costing the same and being slower.

```python
def cost_per_success(cost_per_call, success_rate, check_cost=0.0):
    return (cost_per_call + check_cost) / success_rate

cost_per_success(0.002, 0.60, 0.0005)  # cheap model: ≈ 0.00417
cost_per_success(0.006, 0.97, 0.0005)  # strong model: ≈ 0.00670
```

## 426: How does the choice between streaming and non-streaming affect server resources?

Streaming keeps a connection open for the whole generation and sends many small writes, so each request holds server resources longer on your side. Non-streaming holds the connection too, but with fewer writes. For many concurrent users, make sure your servers use async I/O and that proxies and serverless platforms allow long-lived connections.

## 427: How do you handle the cost of failed or cancelled streams?

You are billed for tokens processed before the stream stopped. Log usage for cancelled and failed requests too, because they are real spend. If many users cancel, that is a sign answers are too slow, too long or not useful, which is worth fixing.

## 428: How does the HTTP layer affect LLM latency at scale?

TLS handshakes, DNS lookups and new TCP connections add tens to hundreds of milliseconds if not reused. Use keep-alive and connection pools, HTTP/2 where supported, and keep a healthy number of open connections per provider. At high load, connection pool limits in your HTTP client can become a hidden queue.

## 429: What is speculative or eager execution in an LLM app (not speculative decoding)?

It means starting work before you are sure it is needed, for example starting retrieval and the LLM call while the user is still typing, or running the likely next step of an agent early. If the guess is right, the user saves time; if wrong, you cancel and pay for the wasted tokens. Use it where guesses are usually right and the latency gain is large.

## 430: How do you serve the same prompt to many users with minimal cost, like a daily digest?

Generate shared content once and store it, then add only small personal parts per user. If personalization is needed, put the shared content first in the prompt so it is cached, and generate only the short personalized section per user. Use batch processing ahead of the delivery time.

## 431: How do you set max_tokens correctly for reasoning models?

For reasoning models, the output limit covers both thinking and the visible answer. If you set it too low, the model can use all tokens thinking and return an empty or cut-off answer while you still pay. Set it high enough for thinking plus answer, and control cost with effort or thinking budget settings instead.

## 432: What metrics would you alert on for an LLM platform?

Alert on spend per hour vs normal, sudden rises in tokens per request, cache hit rate drops, p95 TTFT and total latency, error and 429 rates per provider, agent runs hitting step limits, and queue length for async jobs. Use relative thresholds (compared with last week) as well as absolute ones to catch unusual changes.

## 433: How do you run a cost and latency review of a new LLM feature before launch?

Check: expected traffic and token use, chosen model and why, prompt structure for caching, max tokens and timeouts, retry and fallback plan, rate limits and quotas, streaming and UI handling, logging and cost tags, eval results, load test results and a budget alert. Write down the expected cost per user and compare it with the real number after launch.

## 434: How do you explain cost and latency trade-offs to a product manager?

Show options with real numbers: for example "Model A: $0.002 per answer, 1.2 s, 92% correct; Model B: $0.02, 3 s, 95% correct". Explain what the difference means for users and for the monthly bill at expected traffic. Let product decide based on value, and agree on what to monitor after launch.

## 435: What is the cost impact of a bigger context window on a self-hosted server even if prompts are short?

Setting a large `max-model-len` makes the engine plan for possible long requests, which can lower the max batch size or cause memory pressure when a few long prompts arrive. With PagedAttention the waste is smaller, but long requests still take a big share of KV cache. Set the max length to what you really need and route long-context requests to a separate deployment.

## 436: Why might you run separate deployments for short and long requests?

Short and long requests have very different memory and compute needs. Mixed on one server, long prompts cause latency spikes for short ones. Separate pools let you tune batch size, max length and hardware for each, which gives better latency and cost for both.

## 437: How do LLM costs scale with users for a chat product, and what grows faster than expected?

Cost grows with users, messages per user, and tokens per message, and tokens per message grow with conversation length. Heavy users and long conversations often grow faster than user count, and new features like file upload and agents add a lot per user. Track cost per active user over time, not just total cost.

## 438: What is the role of a "small model first" architecture in large systems?

Most requests in many products are simple: greetings, FAQs, short lookups, formatting. A small model, cache or rules engine handles those, and big models are reserved for the hard tail. This keeps average cost low and latency fast, while still giving strong answers when needed.

## 439: How do you handle provider price drops or new cheaper models?

Have your eval set and price table ready so you can test a new model within days. Track your quality, cost and latency on it, and switch features where it is good enough. Prices for the same quality level have been dropping fast, so regular review often saves more than deep optimization of an old setup.

## 440: Why can a cheaper per-token model increase total cost in agent workflows?

A weaker model may take more steps, call tools more often, make more mistakes that need fixing, or fail tasks and need restarts. Each extra step resends the growing context. Measure cost per completed task end to end before switching agents to a cheaper model.

## 441: How do you set a per-request cost limit in an agent framework?

Track tokens and tool costs as the agent runs, using usage from each response and a price table. Before each new step, check the running total against the budget and stop or switch to a cheaper path if it would go over. Return a partial result with a clear message instead of failing silently.

```ts
let spent = 0;
const BUDGET = 0.5; // dollars

for (let step = 0; step < 20; step++) {
  const res = await runStep(state);
  spent += priceOf(res.usage, res.model);
  if (spent > BUDGET) {
    return { status: "budget_exceeded", partial: state.result };
  }
  if (res.done) break;
}
```

## 442: How does output streaming interact with structured output and tool calls for latency?

With JSON or tool call outputs, the client often cannot act until the full object is ready, so total time matters more than TTFT. Keep these outputs small, put the most needed fields first, and use partial parsing when the UI can show fields as they arrive. For tool calls, the model's text before the call can be streamed while arguments are still being written.

## 443: What are typical latency differences between provider tiers of the same model family?

Smaller models are usually several times faster in tokens per second and have lower TTFT than the flagship of the same family. Priority tiers can also lower latency and make it more stable compared to standard tiers, while flex or batch tiers are slower. Measure these yourself, because they change with load and new releases.

## 444: How would you reduce the cost of an LLM evaluation pipeline that runs on every pull request?

Run a small, fast smoke eval on each PR and the full eval only on main or before release. Cache outputs for examples whose prompt and model did not change. Use cheaper judge models where they agree with humans, use batch APIs for nightly full runs, and only run evals for PRs that touch prompts or model code.

## 445: How do you approach latency for a multi-step RAG agent that calls the LLM 5 times?

Draw the call graph and find which calls depend on others. Run independent calls in parallel, merge small steps into one call, use small models for routing and query rewriting, and stream the final answer. Show progress to the user during the earlier steps so the wait feels shorter.

## 446: What is the effect of system prompt changes on a large, cached production workload?

Every change creates a new prefix, so the first requests after a deploy are cache misses billed at full price (and with cache write fees). With many deployments a day or per-user variants, you may pay this cost often. Group prompt changes into fewer releases and check cache hit rate after each deploy.

## 447: How can you use offline precomputation to lower RAG query costs?

Precompute document summaries, questions each chunk answers, keywords and metadata during indexing. At query time you can retrieve by these, rank better and send short summaries instead of long chunks. You pay once at indexing time, often in batch, instead of on every query.

## 448: How do you know if your optimizations are worth the engineering time?

Estimate the monthly saving or latency gain and compare it with the time to build and maintain it. A change that saves $50 a month is not worth weeks of work, while trimming a prompt used a million times a day might save thousands. Start with the biggest cost drivers from your dashboard.

## 449: What are the most effective cost levers, in rough order of impact?

Usually: picking the right model size for each task, prompt caching with a stable prefix, cutting input tokens (context, history, tools), limiting output and reasoning tokens, batch or flex processing for background work, and response caching for repeated questions. Self-hosting and fine-tuning can save more at large scale but take much more work.

## 450: What are the most effective latency levers, in rough order of impact?

Usually: streaming the response, using a smaller or faster model, cutting output length and reasoning effort, removing or parallelizing extra calls before the main one, prompt caching for long prefixes, and a provider or region close to your servers. For self-hosting, add continuous batching, prefix caching, speculative decoding and quantization.
