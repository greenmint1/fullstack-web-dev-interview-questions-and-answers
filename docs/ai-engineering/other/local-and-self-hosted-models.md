# Local and Self-Hosted Models Interview Questions and Answers

_Last updated: November 12, 2026_

450 interview questions about running LLMs on your own hardware, with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The questions cover Ollama, llama.cpp, vLLM, quantization formats (GGUF, AWQ, GPTQ, FP8 and 4-bit floats), hardware sizing, serving in production, security and the problems you run into in real projects. They're written against the tools as of late 2026: recent Ollama releases, current llama.cpp builds and vLLM with its V1 engine. These projects change fast, and flags and defaults move between versions, so check the docs for the version you run.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What does it mean to run a model locally or self-host it?](#1-what-does-it-mean-to-run-a-model-locally-or-self-host-it)
- [2: Why would a company choose to self-host a model instead of using a hosted API?](#2-why-would-a-company-choose-to-self-host-a-model-instead-of-using-a-hosted-api)
- [3: What are the main downsides of self-hosting models?](#3-what-are-the-main-downsides-of-self-hosting-models)
- [4: What is the difference between open-weight and open-source models?](#4-what-is-the-difference-between-open-weight-and-open-source-models)
- [5: Why does the license of an open-weight model matter?](#5-why-does-the-license-of-an-open-weight-model-matter)
- [6: What are model parameters, and why does the count matter for local use?](#6-what-are-model-parameters-and-why-does-the-count-matter-for-local-use)
- [7: How do you roughly estimate how much memory a model needs?](#7-how-do-you-roughly-estimate-how-much-memory-a-model-needs)
- [8: What is VRAM, and why is it so important for running LLMs?](#8-what-is-vram-and-why-is-it-so-important-for-running-llms)
- [9: Can you run an LLM without a GPU?](#9-can-you-run-an-llm-without-a-gpu)
- [10: Why are Apple Silicon Macs popular for running local models?](#10-why-are-apple-silicon-macs-popular-for-running-local-models)
- [11: What is inference, and how is it different from training?](#11-what-is-inference-and-how-is-it-different-from-training)
- [12: What is a token?](#12-what-is-a-token)
- [13: What is the context window?](#13-what-is-the-context-window)
- [14: What is the KV cache?](#14-what-is-the-kv-cache)
- [15: What are the two phases of generating text, prefill and decode?](#15-what-are-the-two-phases-of-generating-text-prefill-and-decode)
- [16: What do time to first token and tokens per second mean?](#16-what-do-time-to-first-token-and-tokens-per-second-mean)
- [17: What is the difference between latency and throughput when serving models?](#17-what-is-the-difference-between-latency-and-throughput-when-serving-models)
- [18: What is the difference between a base model and an instruct (chat) model?](#18-what-is-the-difference-between-a-base-model-and-an-instruct-chat-model)
- [19: What is a chat template?](#19-what-is-a-chat-template)
- [20: What is Hugging Face Hub, and how is it used with local models?](#20-what-is-hugging-face-hub-and-how-is-it-used-with-local-models)
- [21: What is a model card?](#21-what-is-a-model-card)
- [22: What is the safetensors format?](#22-what-is-the-safetensors-format)
- [23: Why are pickle-based model files a security risk?](#23-why-are-pickle-based-model-files-a-security-risk)
- [24: What are the main tools for running models locally?](#24-what-are-the-main-tools-for-running-models-locally)
- [25: When would you pick Ollama, llama.cpp or vLLM?](#25-when-would-you-pick-ollama-llamacpp-or-vllm)
- [26: What is the relationship between Ollama and llama.cpp?](#26-what-is-the-relationship-between-ollama-and-llamacpp)
- [27: What is GGML?](#27-what-is-ggml)
- [28: What is a "model runner" in plain terms?](#28-what-is-a-model-runner-in-plain-terms)
- [29: What does "OpenAI-compatible API" mean for local tools?](#29-what-does-openai-compatible-api-mean-for-local-tools)
- [30: How do you use the OpenAI SDK with a local model?](#30-how-do-you-use-the-openai-sdk-with-a-local-model)
- [31: What is quantization?](#31-what-is-quantization)
- [32: Why is quantization so important for local models?](#32-why-is-quantization-so-important-for-local-models)
- [33: What is GGUF?](#33-what-is-gguf)
- [34: What is AWQ?](#34-what-is-awq)
- [35: What is the difference between GGUF and AWQ?](#35-what-is-the-difference-between-gguf-and-awq)
- [36: What is GPTQ?](#36-what-is-gptq)
- [37: What is FP8?](#37-what-is-fp8)
- [38: What is the difference between FP16 and BF16?](#38-what-is-the-difference-between-fp16-and-bf16)
- [39: What do names like Q4_K_M and Q8_0 mean in GGUF files?](#39-what-do-names-like-q4_k_m-and-q8_0-mean-in-gguf-files)
- [40: Which GGUF quant should you start with?](#40-which-gguf-quant-should-you-start-with)
- [41: What is Ollama?](#41-what-is-ollama)
- [42: How do you install Ollama?](#42-how-do-you-install-ollama)
- [43: How do you run a model with Ollama for the first time?](#43-how-do-you-run-a-model-with-ollama-for-the-first-time)
- [44: What is the difference between ollama pull and ollama run?](#44-what-is-the-difference-between-ollama-pull-and-ollama-run)
- [45: What are the most common Ollama CLI commands?](#45-what-are-the-most-common-ollama-cli-commands)
- [46: What is a model tag in Ollama?](#46-what-is-a-model-tag-in-ollama)
- [47: Where does Ollama store downloaded models?](#47-where-does-ollama-store-downloaded-models)
- [48: What port does Ollama listen on, and how do you check it's running?](#48-what-port-does-ollama-listen-on-and-how-do-you-check-its-running)
- [49: How do you call Ollama's REST API to chat?](#49-how-do-you-call-ollamas-rest-api-to-chat)
- [50: What is the difference between /api/generate and /api/chat in Ollama?](#50-what-is-the-difference-between-apigenerate-and-apichat-in-ollama)
- [51: How does streaming work in the Ollama API?](#51-how-does-streaming-work-in-the-ollama-api)
- [52: How do you use Ollama from JavaScript?](#52-how-do-you-use-ollama-from-javascript)
- [53: How do you use Ollama from Python?](#53-how-do-you-use-ollama-from-python)
- [54: What is a Modelfile?](#54-what-is-a-modelfile)
- [55: What instructions can you use in a Modelfile?](#55-what-instructions-can-you-use-in-a-modelfile)
- [56: How do you see the Modelfile of a model you already have?](#56-how-do-you-see-the-modelfile-of-a-model-you-already-have)
- [57: How do you load a GGUF file you downloaded into Ollama?](#57-how-do-you-load-a-gguf-file-you-downloaded-into-ollama)
- [58: What does ollama ps show?](#58-what-does-ollama-ps-show)
- [59: How long does Ollama keep a model in memory?](#59-how-long-does-ollama-keep-a-model-in-memory)
- [60: How do you pre-load a model so the first user request is fast?](#60-how-do-you-pre-load-a-model-so-the-first-user-request-is-fast)
- [61: How do you change the context length in Ollama?](#61-how-do-you-change-the-context-length-in-ollama)
- [62: What happens when a prompt is longer than num_ctx in Ollama?](#62-what-happens-when-a-prompt-is-longer-than-num_ctx-in-ollama)
- [63: How do you get JSON output from Ollama?](#63-how-do-you-get-json-output-from-ollama)
- [64: Does Ollama support tool calling?](#64-does-ollama-support-tool-calling)
- [65: How do you send images to a vision model in Ollama?](#65-how-do-you-send-images-to-a-vision-model-in-ollama)
- [66: How do you create embeddings with Ollama?](#66-how-do-you-create-embeddings-with-ollama)
- [67: How do you list the models available on an Ollama server through the API?](#67-how-do-you-list-the-models-available-on-an-ollama-server-through-the-api)
- [68: How do you make Ollama reachable from other machines?](#68-how-do-you-make-ollama-reachable-from-other-machines)
- [69: Why can a browser app get CORS errors when calling Ollama?](#69-why-can-a-browser-app-get-cors-errors-when-calling-ollama)
- [70: How do you set the system prompt in Ollama?](#70-how-do-you-set-the-system-prompt-in-ollama)
- [71: What sampling options can you set in an Ollama request?](#71-what-sampling-options-can-you-set-in-an-ollama-request)
- [72: What is temperature?](#72-what-is-temperature)
- [73: What are top_p and top_k?](#73-what-are-top_p-and-top_k)
- [74: How do you use thinking (reasoning) models in Ollama?](#74-how-do-you-use-thinking-reasoning-models-in-ollama)
- [75: How do you run Ollama in Docker with an NVIDIA GPU?](#75-how-do-you-run-ollama-in-docker-with-an-nvidia-gpu)
- [76: How do you see the Ollama server logs?](#76-how-do-you-see-the-ollama-server-logs)
- [77: How do you use a Hugging Face GGUF model directly in Ollama?](#77-how-do-you-use-a-hugging-face-gguf-model-directly-in-ollama)
- [78: How do you run your own fine-tuned model in Ollama?](#78-how-do-you-run-your-own-fine-tuned-model-in-ollama)
- [79: What does the stats block at the end of an Ollama response tell you?](#79-what-does-the-stats-block-at-the-end-of-an-ollama-response-tell-you)
- [80: What is the Ollama model library?](#80-what-is-the-ollama-model-library)
- [81: What is llama.cpp?](#81-what-is-llamacpp)
- [82: How do you get llama.cpp on your machine?](#82-how-do-you-get-llamacpp-on-your-machine)
- [83: What are the main programs that come with llama.cpp?](#83-what-are-the-main-programs-that-come-with-llamacpp)
- [84: How do you chat with a model using llama-cli?](#84-how-do-you-chat-with-a-model-using-llama-cli)
- [85: How do you start llama-server?](#85-how-do-you-start-llama-server)
- [86: What does the -ngl flag do in llama.cpp?](#86-what-does-the--ngl-flag-do-in-llamacpp)
- [87: What does the -c flag do in llama.cpp?](#87-what-does-the--c-flag-do-in-llamacpp)
- [88: What does the -hf flag do?](#88-what-does-the--hf-flag-do)
- [89: How do you call llama-server from code?](#89-how-do-you-call-llama-server-from-code)
- [90: How do you check that llama-server is ready?](#90-how-do-you-check-that-llama-server-is-ready)
- [91: How do you protect llama-server with an API key?](#91-how-do-you-protect-llama-server-with-an-api-key)
- [92: What is the default host of llama-server, and why does it matter?](#92-what-is-the-default-host-of-llama-server-and-why-does-it-matter)
- [93: How do you convert a Hugging Face model to GGUF?](#93-how-do-you-convert-a-hugging-face-model-to-gguf)
- [94: What is llama-bench used for?](#94-what-is-llama-bench-used-for)
- [95: What hardware backends does llama.cpp support?](#95-what-hardware-backends-does-llamacpp-support)
- [96: What is mmap, and why does llama.cpp use it?](#96-what-is-mmap-and-why-does-llamacpp-use-it)
- [97: What does the -t flag do in llama.cpp?](#97-what-does-the--t-flag-do-in-llamacpp)
- [98: What is the built-in web UI of llama-server?](#98-what-is-the-built-in-web-ui-of-llama-server)
- [99: What is GBNF in llama.cpp?](#99-what-is-gbnf-in-llamacpp)
- [100: How do you force JSON output from llama-server?](#100-how-do-you-force-json-output-from-llama-server)
- [101: What does --jinja do in llama-server?](#101-what-does---jinja-do-in-llama-server)
- [102: Can llama.cpp run vision models?](#102-can-llamacpp-run-vision-models)
- [103: What is the difference between llama.cpp and the GGML library?](#103-what-is-the-difference-between-llamacpp-and-the-ggml-library)
- [104: How are llama.cpp releases versioned?](#104-how-are-llamacpp-releases-versioned)
- [105: What is llamafile?](#105-what-is-llamafile)
- [106: What is vLLM?](#106-what-is-vllm)
- [107: How do you install vLLM?](#107-how-do-you-install-vllm)
- [108: How do you start a vLLM server?](#108-how-do-you-start-a-vllm-server)
- [109: How do you run vLLM with Docker?](#109-how-do-you-run-vllm-with-docker)
- [110: How do you use vLLM in a Python script without a server?](#110-how-do-you-use-vllm-in-a-python-script-without-a-server)
- [111: What is SamplingParams in vLLM?](#111-what-is-samplingparams-in-vllm)
- [112: What does --gpu-memory-utilization do in vLLM?](#112-what-does---gpu-memory-utilization-do-in-vllm)
- [113: What does --max-model-len do in vLLM?](#113-what-does---max-model-len-do-in-vllm)
- [114: How do you call a vLLM server from JavaScript?](#114-how-do-you-call-a-vllm-server-from-javascript)
- [115: What does --served-model-name do?](#115-what-does---served-model-name-do)
- [116: How do you add an API key to a vLLM server?](#116-how-do-you-add-an-api-key-to-a-vllm-server)
- [117: Which endpoints does the vLLM OpenAI-compatible server offer?](#117-which-endpoints-does-the-vllm-openai-compatible-server-offer)
- [118: What GPUs does vLLM support?](#118-what-gpus-does-vllm-support)
- [119: Why does vLLM take so long to start?](#119-why-does-vllm-take-so-long-to-start)
- [120: What is the Hugging Face token used for in vLLM?](#120-what-is-the-hugging-face-token-used-for-in-vllm)
- [121: What are some other self-hosting tools besides Ollama, llama.cpp and vLLM?](#121-what-are-some-other-self-hosting-tools-besides-ollama-llamacpp-and-vllm)
- [122: What is LM Studio?](#122-what-is-lm-studio)
- [123: What is Open WebUI?](#123-what-is-open-webui)
- [124: What is MLX?](#124-what-is-mlx)
- [125: What is SGLang?](#125-what-is-sglang)
- [126: What is the main trade-off of quantization?](#126-what-is-the-main-trade-off-of-quantization)
- [127: What is the difference between quantizing weights and quantizing activations?](#127-what-is-the-difference-between-quantizing-weights-and-quantizing-activations)
- [128: What does W4A16 mean?](#128-what-does-w4a16-mean)
- [129: What is post-training quantization?](#129-what-is-post-training-quantization)
- [130: What is quantization-aware training?](#130-what-is-quantization-aware-training)
- [131: What is a calibration dataset in quantization?](#131-what-is-a-calibration-dataset-in-quantization)
- [132: What is perplexity, and how is it used to compare quants?](#132-what-is-perplexity-and-how-is-it-used-to-compare-quants)
- [133: What is KL divergence in quant comparisons?](#133-what-is-kl-divergence-in-quant-comparisons)
- [134: What is an importance matrix (imatrix) in llama.cpp?](#134-what-is-an-importance-matrix-imatrix-in-llamacpp)
- [135: What are the IQ quant types in GGUF?](#135-what-are-the-iq-quant-types-in-gguf)
- [136: How big is a Q4_K_M model compared to the original?](#136-how-big-is-a-q4_k_m-model-compared-to-the-original)
- [137: What is Q8_0 good for?](#137-what-is-q8_0-good-for)
- [138: Can you quantize the KV cache?](#138-can-you-quantize-the-kv-cache)
- [139: What is flash attention?](#139-what-is-flash-attention)
- [140: What is a Mixture of Experts (MoE) model?](#140-what-is-a-mixture-of-experts-moe-model)
- [141: What does a name like Qwen3-30B-A3B mean?](#141-what-does-a-name-like-qwen3-30b-a3b-mean)
- [142: What is gpt-oss?](#142-what-is-gpt-oss)
- [143: Which open-weight model families are common for self-hosting?](#143-which-open-weight-model-families-are-common-for-self-hosting)
- [144: What are small language models, and why do they matter for local use?](#144-what-are-small-language-models-and-why-do-they-matter-for-local-use)
- [145: What is an embedding model, and can you self-host one?](#145-what-is-an-embedding-model-and-can-you-self-host-one)
- [146: What is a reranker, and can you run one locally?](#146-what-is-a-reranker-and-can-you-run-one-locally)
- [147: What is the tokens per second you need for a good chat experience?](#147-what-is-the-tokens-per-second-you-need-for-a-good-chat-experience)
- [148: Why is generation speed mostly limited by memory bandwidth?](#148-why-is-generation-speed-mostly-limited-by-memory-bandwidth)
- [149: What is speculative decoding in simple words?](#149-what-is-speculative-decoding-in-simple-words)
- [150: What is LoRA, and how does it relate to serving local models?](#150-what-is-lora-and-how-does-it-relate-to-serving-local-models)

### Moderate Questions (151-300)

- [151: How does Ollama handle several requests at the same time?](#151-how-does-ollama-handle-several-requests-at-the-same-time)
- [152: How many models can Ollama keep in memory at once?](#152-how-many-models-can-ollama-keep-in-memory-at-once)
- [153: How do you choose which GPUs Ollama uses?](#153-how-do-you-choose-which-gpus-ollama-uses)
- [154: How do you force a model to run fully on the CPU or set the number of GPU layers in Ollama?](#154-how-do-you-force-a-model-to-run-fully-on-the-cpu-or-set-the-number-of-gpu-layers-in-ollama)
- [155: A model in Ollama is suddenly much slower than before. How do you debug it?](#155-a-model-in-ollama-is-suddenly-much-slower-than-before-how-do-you-debug-it)
- [156: How do you use Ollama with the Vercel AI SDK?](#156-how-do-you-use-ollama-with-the-vercel-ai-sdk)
- [157: How do you use Ollama with LangChain?](#157-how-do-you-use-ollama-with-langchain)
- [158: How do you get typed structured output from Ollama in TypeScript?](#158-how-do-you-get-typed-structured-output-from-ollama-in-typescript)
- [159: How do you write a tool-calling loop with Ollama?](#159-how-do-you-write-a-tool-calling-loop-with-ollama)
- [160: What are the limits of Ollama's OpenAI-compatible API?](#160-what-are-the-limits-of-ollamas-openai-compatible-api)
- [161: How would you run Ollama with Docker Compose next to your app?](#161-how-would-you-run-ollama-with-docker-compose-next-to-your-app)
- [162: How do you make sure a model is downloaded when an Ollama container starts?](#162-how-do-you-make-sure-a-model-is-downloaded-when-an-ollama-container-starts)
- [163: How do you move Ollama models to a machine with no internet?](#163-how-do-you-move-ollama-models-to-a-machine-with-no-internet)
- [164: How do you put authentication in front of Ollama?](#164-how-do-you-put-authentication-in-front-of-ollama)
- [165: Why do streaming responses from a local model sometimes arrive all at once behind a proxy?](#165-why-do-streaming-responses-from-a-local-model-sometimes-arrive-all-at-once-behind-a-proxy)
- [166: What are Ollama cloud models?](#166-what-are-ollama-cloud-models)
- [167: How do you check which quantization an Ollama model uses?](#167-how-do-you-check-which-quantization-an-ollama-model-uses)
- [168: Why does a model in Ollama keep repeating itself, and how do you fix it?](#168-why-does-a-model-in-ollama-keep-repeating-itself-and-how-do-you-fix-it)
- [169: How do you pin model versions in Ollama for reproducible deployments?](#169-how-do-you-pin-model-versions-in-ollama-for-reproducible-deployments)
- [170: What does OLLAMA_FLASH_ATTENTION do, and when should you set it?](#170-what-does-ollama_flash_attention-do-and-when-should-you-set-it)
- [171: How do you set environment variables for Ollama on each OS?](#171-how-do-you-set-environment-variables-for-ollama-on-each-os)
- [172: How do you remove all unused models and free disk space in Ollama?](#172-how-do-you-remove-all-unused-models-and-free-disk-space-in-ollama)
- [173: What is the template syntax in an Ollama Modelfile?](#173-what-is-the-template-syntax-in-an-ollama-modelfile)
- [174: How do you make Ollama answers more repeatable?](#174-how-do-you-make-ollama-answers-more-repeatable)
- [175: How does llama-server handle several users at once?](#175-how-does-llama-server-handle-several-users-at-once)
- [176: How is context split between slots in llama-server?](#176-how-is-context-split-between-slots-in-llama-server)
- [177: What does --cache-reuse do in llama-server?](#177-what-does---cache-reuse-do-in-llama-server)
- [178: How do you split a model across several GPUs in llama.cpp?](#178-how-do-you-split-a-model-across-several-gpus-in-llamacpp)
- [179: What is --n-cpu-moe in llama.cpp?](#179-what-is---n-cpu-moe-in-llamacpp)
- [180: What does --override-tensor (-ot) do?](#180-what-does---override-tensor--ot-do)
- [181: How do you enable speculative decoding in llama-server?](#181-how-do-you-enable-speculative-decoding-in-llama-server)
- [182: How do you serve embeddings with llama-server?](#182-how-do-you-serve-embeddings-with-llama-server)
- [183: How do you use LoRA adapters with llama-server?](#183-how-do-you-use-lora-adapters-with-llama-server)
- [184: How do you see Prometheus metrics from llama-server?](#184-how-do-you-see-prometheus-metrics-from-llama-server)
- [185: How do you handle reasoning (thinking) output in llama-server?](#185-how-do-you-handle-reasoning-thinking-output-in-llama-server)
- [186: How do you run llama-server as a service on Linux?](#186-how-do-you-run-llama-server-as-a-service-on-linux)
- [187: How do you pick a GGUF quant that fits your GPU?](#187-how-do-you-pick-a-gguf-quant-that-fits-your-gpu)
- [188: When should you offload part of a model to the CPU, and what does it cost?](#188-when-should-you-offload-part-of-a-model-to-the-cpu-and-what-does-it-cost)
- [189: Which popular GGUF uploaders should you know, and why do they matter?](#189-which-popular-gguf-uploaders-should-you-know-and-why-do-they-matter)
- [190: What do the files in a split GGUF upload like model-00001-of-00003.gguf mean?](#190-what-do-the-files-in-a-split-gguf-upload-like-model-00001-of-00003gguf-mean)
- [191: How do you read the metadata of a GGUF file?](#191-how-do-you-read-the-metadata-of-a-gguf-file)
- [192: What is the --mlock flag, and when do you need it?](#192-what-is-the---mlock-flag-and-when-do-you-need-it)
- [193: How do you serve a vLLM model on several GPUs?](#193-how-do-you-serve-a-vllm-model-on-several-gpus)
- [194: What is the difference between tensor parallelism and pipeline parallelism in vLLM?](#194-what-is-the-difference-between-tensor-parallelism-and-pipeline-parallelism-in-vllm)
- [195: What does --max-num-seqs do in vLLM?](#195-what-does---max-num-seqs-do-in-vllm)
- [196: What does --max-num-batched-tokens do in vLLM?](#196-what-does---max-num-batched-tokens-do-in-vllm)
- [197: What is prefix caching in vLLM?](#197-what-is-prefix-caching-in-vllm)
- [198: What is chunked prefill?](#198-what-is-chunked-prefill)
- [199: How do you get structured output from vLLM?](#199-how-do-you-get-structured-output-from-vllm)
- [200: How do you enable tool calling in vLLM?](#200-how-do-you-enable-tool-calling-in-vllm)
- [201: How do you serve a reasoning model with vLLM so the thinking is separated from the answer?](#201-how-do-you-serve-a-reasoning-model-with-vllm-so-the-thinking-is-separated-from-the-answer)
- [202: How do you serve several LoRA adapters with one base model in vLLM?](#202-how-do-you-serve-several-lora-adapters-with-one-base-model-in-vllm)
- [203: Can you load LoRA adapters into a running vLLM server?](#203-can-you-load-lora-adapters-into-a-running-vllm-server)
- [204: How do you run an AWQ or GPTQ model in vLLM?](#204-how-do-you-run-an-awq-or-gptq-model-in-vllm)
- [205: How do you use FP8 in vLLM without a pre-quantized model?](#205-how-do-you-use-fp8-in-vllm-without-a-pre-quantized-model)
- [206: What does --kv-cache-dtype fp8 do in vLLM?](#206-what-does---kv-cache-dtype-fp8-do-in-vllm)
- [207: Which vLLM metrics would you watch in production?](#207-which-vllm-metrics-would-you-watch-in-production)
- [208: What is preemption in vLLM?](#208-what-is-preemption-in-vllm)
- [209: vLLM fails at start-up with an out-of-memory error. What do you check?](#209-vllm-fails-at-start-up-with-an-out-of-memory-error-what-do-you-check)
- [210: How do you deploy vLLM on Kubernetes?](#210-how-do-you-deploy-vllm-on-kubernetes)
- [211: How do you autoscale self-hosted LLM servers?](#211-how-do-you-autoscale-self-hosted-llm-servers)
- [212: What does --generation-config do in vLLM?](#212-what-does---generation-config-do-in-vllm)
- [213: How do you override the chat template in vLLM?](#213-how-do-you-override-the-chat-template-in-vllm)
- [214: How do you serve a vision model with vLLM and limit images per request?](#214-how-do-you-serve-a-vision-model-with-vllm-and-limit-images-per-request)
- [215: How do you serve an embedding model with vLLM?](#215-how-do-you-serve-an-embedding-model-with-vllm)
- [216: How do you benchmark a vLLM server?](#216-how-do-you-benchmark-a-vllm-server)
- [217: What does --enforce-eager do, and when do you use it?](#217-what-does---enforce-eager-do-and-when-do-you-use-it)
- [218: How do you get log probabilities from a local model?](#218-how-do-you-get-log-probabilities-from-a-local-model)
- [219: How do you pick between Q4_K_M GGUF, AWQ and FP8 for a project?](#219-how-do-you-pick-between-q4_k_m-gguf-awq-and-fp8-for-a-project)
- [220: How do you quantize a model to AWQ today?](#220-how-do-you-quantize-a-model-to-awq-today)
- [221: How do you create an FP8 model with llm-compressor?](#221-how-do-you-create-an-fp8-model-with-llm-compressor)
- [222: What is the status of AutoGPTQ and AutoAWQ?](#222-what-is-the-status-of-autogptq-and-autoawq)
- [223: What is bitsandbytes, and where does it fit?](#223-what-is-bitsandbytes-and-where-does-it-fit)
- [224: What is NF4?](#224-what-is-nf4)
- [225: What are EXL2 and EXL3?](#225-what-are-exl2-and-exl3)
- [226: What are MXFP4 and NVFP4?](#226-what-are-mxfp4-and-nvfp4)
- [227: How do you check if a quantized model is good enough for your use case?](#227-how-do-you-check-if-a-quantized-model-is-good-enough-for-your-use-case)
- [228: Why do small models suffer more from quantization than big ones?](#228-why-do-small-models-suffer-more-from-quantization-than-big-ones)
- [229: Which parts of a model are usually kept at higher precision when quantizing?](#229-which-parts-of-a-model-are-usually-kept-at-higher-precision-when-quantizing)
- [230: How do you calculate the KV cache size for a model?](#230-how-do-you-calculate-the-kv-cache-size-for-a-model)
- [231: What is grouped-query attention, and why does it help local models?](#231-what-is-grouped-query-attention-and-why-does-it-help-local-models)
- [232: How would you size a GPU server for a team of 50 developers using a local coding model?](#232-how-would-you-size-a-gpu-server-for-a-team-of-50-developers-using-a-local-coding-model)
- [233: When is self-hosting cheaper than using an API?](#233-when-is-self-hosting-cheaper-than-using-an-api)
- [234: How can you use the same code for a local model and a hosted API?](#234-how-can-you-use-the-same-code-for-a-local-model-and-a-hosted-api)
- [235: What is LiteLLM, and why use it with self-hosted models?](#235-what-is-litellm-and-why-use-it-with-self-hosted-models)
- [236: How do you load balance several vLLM or llama.cpp instances?](#236-how-do-you-load-balance-several-vllm-or-llamacpp-instances)
- [237: How would you build a fully local RAG system?](#237-how-would-you-build-a-fully-local-rag-system)
- [238: How do you stream tokens from a local model to a browser through your own backend?](#238-how-do-you-stream-tokens-from-a-local-model-to-a-browser-through-your-own-backend)
- [239: How do you handle a request the user cancelled?](#239-how-do-you-handle-a-request-the-user-cancelled)
- [240: What timeouts should you think about with local LLM servers?](#240-what-timeouts-should-you-think-about-with-local-llm-servers)
- [241: How do you test code that calls a local model?](#241-how-do-you-test-code-that-calls-a-local-model)
- [242: How do you run a local model in GitHub Actions CI?](#242-how-do-you-run-a-local-model-in-github-actions-ci)
- [243: What should you log for a self-hosted LLM service?](#243-what-should-you-log-for-a-self-hosted-llm-service)
- [244: How do you monitor GPU health on an LLM server?](#244-how-do-you-monitor-gpu-health-on-an-llm-server)
- [245: What does finish_reason "length" mean, and how do you fix it?](#245-what-does-finish_reason-length-mean-and-how-do-you-fix-it)
- [246: Why might a local model ignore your system prompt?](#246-why-might-a-local-model-ignore-your-system-prompt)
- [247: How do you see the exact prompt the model receives after the chat template?](#247-how-do-you-see-the-exact-prompt-the-model-receives-after-the-chat-template)
- [248: Why do the same model and prompt give different answers in Ollama and vLLM?](#248-why-do-the-same-model-and-prompt-give-different-answers-in-ollama-and-vllm)
- [249: What is min_p, and why do many local users prefer it?](#249-what-is-min_p-and-why-do-many-local-users-prefer-it)
- [250: How do you stop a local model from generating after a certain string?](#250-how-do-you-stop-a-local-model-from-generating-after-a-certain-string)
- [251: How do you limit how long a reasoning model thinks?](#251-how-do-you-limit-how-long-a-reasoning-model-thinks)
- [252: How do you serve a GGUF model in vLLM, and should you?](#252-how-do-you-serve-a-gguf-model-in-vllm-and-should-you)
- [253: How do you convert a model for MLX on a Mac?](#253-how-do-you-convert-a-model-for-mlx-on-a-mac)
- [254: Is a Mac or an NVIDIA GPU better for local models?](#254-is-a-mac-or-an-nvidia-gpu-better-for-local-models)
- [255: Can you run local models on AMD GPUs?](#255-can-you-run-local-models-on-amd-gpus)
- [256: What are the steps to take a fine-tuned Hugging Face model to a GGUF in Ollama?](#256-what-are-the-steps-to-take-a-fine-tuned-hugging-face-model-to-a-gguf-in-ollama)
- [257: How do you quantize a model with Ollama itself?](#257-how-do-you-quantize-a-model-with-ollama-itself)
- [258: How do you choose between running one big model or several small specialized ones?](#258-how-do-you-choose-between-running-one-big-model-or-several-small-specialized-ones)
- [259: What is model routing, and how does it help with local models?](#259-what-is-model-routing-and-how-does-it-help-with-local-models)
- [260: How do you add a fallback when a local model server is down or overloaded?](#260-how-do-you-add-a-fallback-when-a-local-model-server-is-down-or-overloaded)
- [261: What does the Ollama response field done_reason tell you?](#261-what-does-the-ollama-response-field-done_reason-tell-you)
- [262: How do you create a model in Ollama with a custom system prompt and share it with the team?](#262-how-do-you-create-a-model-in-ollama-with-a-custom-system-prompt-and-share-it-with-the-team)
- [263: What happens when Ollama gets requests for two different models but only one fits in memory?](#263-what-happens-when-ollama-gets-requests-for-two-different-models-but-only-one-fits-in-memory)
- [264: How does Ollama decide how much of a model to put on the GPU?](#264-how-does-ollama-decide-how-much-of-a-model-to-put-on-the-gpu)
- [265: How do you serve a local model to a mobile or desktop app?](#265-how-do-you-serve-a-local-model-to-a-mobile-or-desktop-app)
- [266: How do you keep an air-gapped vLLM deployment working without Hugging Face access?](#266-how-do-you-keep-an-air-gapped-vllm-deployment-working-without-hugging-face-access)
- [267: How do you deal with gated models when deploying in CI/CD?](#267-how-do-you-deal-with-gated-models-when-deploying-in-cicd)
- [268: How do you compare the throughput of Ollama and vLLM fairly?](#268-how-do-you-compare-the-throughput-of-ollama-and-vllm-fairly)
- [269: How do you measure inter-token latency, and why does it matter?](#269-how-do-you-measure-inter-token-latency-and-why-does-it-matter)
- [270: What are percentiles like p50 and p99 in LLM latency, and why use them?](#270-what-are-percentiles-like-p50-and-p99-in-llm-latency-and-why-use-them)
- [271: What is RoPE scaling, and when does it matter?](#271-what-is-rope-scaling-and-when-does-it-matter)
- [272: Why might a model perform worse at long context even if it technically supports it?](#272-why-might-a-model-perform-worse-at-long-context-even-if-it-technically-supports-it)
- [273: How do you serve two different models on one GPU with vLLM?](#273-how-do-you-serve-two-different-models-on-one-gpu-with-vllm)
- [274: What is the difference between /v1/completions and /v1/chat/completions?](#274-what-is-the-difference-between-v1completions-and-v1chatcompletions)
- [275: How does fill-in-the-middle (FIM) work with local code models?](#275-how-does-fill-in-the-middle-fim-work-with-local-code-models)
- [276: How do you run a local model as a coding assistant in your editor?](#276-how-do-you-run-a-local-model-as-a-coding-assistant-in-your-editor)
- [277: What are the security risks of exposing an Ollama or vLLM port to the internet?](#277-what-are-the-security-risks-of-exposing-an-ollama-or-vllm-port-to-the-internet)
- [278: Why should you keep Ollama, llama.cpp and vLLM updated?](#278-why-should-you-keep-ollama-llamacpp-and-vllm-updated)
- [279: What is the risk of loading GGUF files from unknown sources?](#279-what-is-the-risk-of-loading-gguf-files-from-unknown-sources)
- [280: What is trust_remote_code in vLLM and Transformers, and why be careful with it?](#280-what-is-trust_remote_code-in-vllm-and-transformers-and-why-be-careful-with-it)
- [281: How do you pin a Hugging Face model revision in vLLM?](#281-how-do-you-pin-a-hugging-face-model-revision-in-vllm)
- [282: How do you secure the Jinja chat templates used by local servers?](#282-how-do-you-secure-the-jinja-chat-templates-used-by-local-servers)
- [283: What is prompt injection, and does self-hosting protect you from it?](#283-what-is-prompt-injection-and-does-self-hosting-protect-you-from-it)
- [284: How do you rate limit users of a self-hosted model?](#284-how-do-you-rate-limit-users-of-a-self-hosted-model)
- [285: How do you count tokens before sending a request to a local model?](#285-how-do-you-count-tokens-before-sending-a-request-to-a-local-model)
- [286: How do you handle chat history that grows beyond the context window?](#286-how-do-you-handle-chat-history-that-grows-beyond-the-context-window)
- [287: Why is the first request to vLLM after start-up sometimes slower?](#287-why-is-the-first-request-to-vllm-after-start-up-sometimes-slower)
- [288: How do you choose max-model-len for a production vLLM deployment?](#288-how-do-you-choose-max-model-len-for-a-production-vllm-deployment)
- [289: How do GPU interconnects like NVLink affect multi-GPU serving?](#289-how-do-gpu-interconnects-like-nvlink-affect-multi-gpu-serving)
- [290: What is data parallelism in model serving?](#290-what-is-data-parallelism-in-model-serving)
- [291: How do you pick the number of GPUs for tensor parallelism?](#291-how-do-you-pick-the-number-of-gpus-for-tensor-parallelism)
- [292: What is the vLLM production stack or llm-d?](#292-what-is-the-vllm-production-stack-or-llm-d)
- [293: When would you use SGLang instead of vLLM?](#293-when-would-you-use-sglang-instead-of-vllm)
- [294: When would you consider TensorRT-LLM?](#294-when-would-you-consider-tensorrt-llm)
- [295: How would you serve a local model to many internal teams with different needs?](#295-how-would-you-serve-a-local-model-to-many-internal-teams-with-different-needs)
- [296: How do you move from an Ollama prototype to a vLLM production setup?](#296-how-do-you-move-from-an-ollama-prototype-to-a-vllm-production-setup)
- [297: Why might tool calling work with a model in one tool but not another?](#297-why-might-tool-calling-work-with-a-model-in-one-tool-but-not-another)
- [298: How do you choose a model for a local deployment?](#298-how-do-you-choose-a-model-for-a-local-deployment)
- [299: What is the difference between dense and MoE models in terms of serving cost?](#299-what-is-the-difference-between-dense-and-moe-models-in-terms-of-serving-cost)
- [300: How do you document a self-hosted model deployment for your team?](#300-how-do-you-document-a-self-hosted-model-deployment-for-your-team)

### Advanced Questions (301-450)

- [301: How does PagedAttention work?](#301-how-does-pagedattention-work)
- [302: How does block sharing work in PagedAttention?](#302-how-does-block-sharing-work-in-pagedattention)
- [303: What is continuous batching, and why is it better than static batching?](#303-what-is-continuous-batching-and-why-is-it-better-than-static-batching)
- [304: How does the vLLM scheduler decide what runs in each step?](#304-how-does-the-vllm-scheduler-decide-what-runs-in-each-step)
- [305: How is vLLM's current engine structured internally?](#305-how-is-vllms-current-engine-structured-internally)
- [306: How does automatic prefix caching identify reusable blocks?](#306-how-does-automatic-prefix-caching-identify-reusable-blocks)
- [307: Why can prefix caching hit rate be low even when prompts look similar?](#307-why-can-prefix-caching-hit-rate-be-low-even-when-prompts-look-similar)
- [308: What is disaggregated prefill/decode serving?](#308-what-is-disaggregated-prefilldecode-serving)
- [309: What is KV cache offloading, and when is it useful?](#309-what-is-kv-cache-offloading-and-when-is-it-useful)
- [310: What are CUDA graphs, and why does vLLM use them?](#310-what-are-cuda-graphs-and-why-does-vllm-use-them)
- [311: What role does torch.compile play in vLLM?](#311-what-role-does-torchcompile-play-in-vllm)
- [312: Explain why decoding is memory-bound and prefill is compute-bound using arithmetic intensity.](#312-explain-why-decoding-is-memory-bound-and-prefill-is-compute-bound-using-arithmetic-intensity)
- [313: Why does throughput increase with batch size, and where does it stop?](#313-why-does-throughput-increase-with-batch-size-and-where-does-it-stop)
- [314: How does speculative decoding guarantee the same output as the target model?](#314-how-does-speculative-decoding-guarantee-the-same-output-as-the-target-model)
- [315: What are the main speculative decoding methods in vLLM?](#315-what-are-the-main-speculative-decoding-methods-in-vllm)
- [316: When does speculative decoding hurt instead of help?](#316-when-does-speculative-decoding-hurt-instead-of-help)
- [317: How do structured output engines constrain generation efficiently?](#317-how-do-structured-output-engines-constrain-generation-efficiently)
- [318: What problems can constrained decoding cause for output quality?](#318-what-problems-can-constrained-decoding-cause-for-output-quality)
- [319: How does vLLM serve many LoRA adapters efficiently?](#319-how-does-vllm-serve-many-lora-adapters-efficiently)
- [320: What is expert parallelism, and why does it matter for MoE models?](#320-what-is-expert-parallelism-and-why-does-it-matter-for-moe-models)
- [321: What are Marlin kernels?](#321-what-are-marlin-kernels)
- [322: Why don't 4-bit weight-only models speed up prefill or large batches much?](#322-why-dont-4-bit-weight-only-models-speed-up-prefill-or-large-batches-much)
- [323: How does the attention backend choice affect vLLM performance?](#323-how-does-the-attention-backend-choice-affect-vllm-performance)
- [324: What is the interaction between prefill and decode, and how do you tune for it?](#324-what-is-the-interaction-between-prefill-and-decode-and-how-do-you-tune-for-it)
- [325: How do you design for a strict p99 TTFT target?](#325-how-do-you-design-for-a-strict-p99-ttft-target)
- [326: What is the "lost tokens" problem with naive memory allocation, and how big was it?](#326-what-is-the-lost-tokens-problem-with-naive-memory-allocation-and-how-big-was-it)
- [327: How does vLLM handle requests with n > 1 or best-of sampling?](#327-how-does-vllm-handle-requests-with-n--1-or-best-of-sampling)
- [328: How would you serve a model whose weights don't fit in one node?](#328-how-would-you-serve-a-model-whose-weights-dont-fit-in-one-node)
- [329: What is the trade-off between latency and cost when choosing GPU count per replica?](#329-what-is-the-trade-off-between-latency-and-cost-when-choosing-gpu-count-per-replica)
- [330: How do you serve a batch job of millions of prompts most cheaply?](#330-how-do-you-serve-a-batch-job-of-millions-of-prompts-most-cheaply)
- [331: How is a Q4_0 GGUF block laid out?](#331-how-is-a-q4_0-gguf-block-laid-out)
- [332: How do K-quants differ from the older quant types?](#332-how-do-k-quants-differ-from-the-older-quant-types)
- [333: Why does Q4_K_M use higher precision for some tensors?](#333-why-does-q4_k_m-use-higher-precision-for-some-tensors)
- [334: What is the difference between symmetric and asymmetric quantization?](#334-what-is-the-difference-between-symmetric-and-asymmetric-quantization)
- [335: What is group size in AWQ and GPTQ, and how does it affect quality?](#335-what-is-group-size-in-awq-and-gptq-and-how-does-it-affect-quality)
- [336: Explain how AWQ decides which weights to protect.](#336-explain-how-awq-decides-which-weights-to-protect)
- [337: Explain how GPTQ works at a high level.](#337-explain-how-gptq-works-at-a-high-level)
- [338: AWQ or GPTQ: how do they compare in practice?](#338-awq-or-gptq-how-do-they-compare-in-practice)
- [339: What problem does SmoothQuant solve?](#339-what-problem-does-smoothquant-solve)
- [340: What are activation outliers, and why do they make quantization hard?](#340-what-are-activation-outliers-and-why-do-they-make-quantization-hard)
- [341: What are the two FP8 formats, and which is used for inference?](#341-what-are-the-two-fp8-formats-and-which-is-used-for-inference)
- [342: What is the difference between per-tensor, per-channel and per-token scaling?](#342-what-is-the-difference-between-per-tensor-per-channel-and-per-token-scaling)
- [343: What is the difference between static and dynamic activation quantization?](#343-what-is-the-difference-between-static-and-dynamic-activation-quantization)
- [344: How do NVFP4 and MXFP4 store values?](#344-how-do-nvfp4-and-mxfp4-store-values)
- [345: Why does a 4-bit quant sometimes break JSON or tool calls even if chat seems fine?](#345-why-does-a-4-bit-quant-sometimes-break-json-or-tool-calls-even-if-chat-seems-fine)
- [346: How can a bad imatrix or calibration set hurt a quant?](#346-how-can-a-bad-imatrix-or-calibration-set-hurt-a-quant)
- [347: How do you measure quantization damage more reliably than perplexity?](#347-how-do-you-measure-quantization-damage-more-reliably-than-perplexity)
- [348: Why might quantizing an MoE model need special care?](#348-why-might-quantizing-an-moe-model-need-special-care)
- [349: What are Unsloth dynamic quants and similar per-layer approaches?](#349-what-are-unsloth-dynamic-quants-and-similar-per-layer-approaches)
- [350: How does KV cache quantization affect quality differently from weight quantization?](#350-how-does-kv-cache-quantization-affect-quality-differently-from-weight-quantization)
- [351: Why does llama.cpp repack Q4_0 weights on some CPUs?](#351-why-does-llamacpp-repack-q4_0-weights-on-some-cpus)
- [352: What is the GGUF file layout?](#352-what-is-the-gguf-file-layout)
- [353: Why is having the tokenizer inside the GGUF file important?](#353-why-is-having-the-tokenizer-inside-the-gguf-file-important)
- [354: How does memory mapping interact with partial GPU offload in llama.cpp?](#354-how-does-memory-mapping-interact-with-partial-gpu-offload-in-llamacpp)
- [355: How does the GGML backend scheduler split work across devices?](#355-how-does-the-ggml-backend-scheduler-split-work-across-devices)
- [356: What do -b and -ub mean in llama.cpp?](#356-what-do--b-and--ub-mean-in-llamacpp)
- [357: What is context shifting in llama.cpp?](#357-what-is-context-shifting-in-llamacpp)
- [358: How does llama.cpp's sampler chain work?](#358-how-does-llamacpps-sampler-chain-work)
- [359: How can llama.cpp run one model across several machines?](#359-how-can-llamacpp-run-one-model-across-several-machines)
- [360: What is NUMA, and why does it matter for CPU inference?](#360-what-is-numa-and-why-does-it-matter-for-cpu-inference)
- [361: How does Ollama's scheduler estimate memory, and why can it be wrong?](#361-how-does-ollamas-scheduler-estimate-memory-and-why-can-it-be-wrong)
- [362: How does Ollama store models internally?](#362-how-does-ollama-store-models-internally)
- [363: How does Ollama translate chat templates?](#363-how-does-ollama-translate-chat-templates)
- [364: What are Ollama's runner processes?](#364-what-are-ollamas-runner-processes)
- [365: Why might parallel requests in Ollama give lower quality or errors with long prompts?](#365-why-might-parallel-requests-in-ollama-give-lower-quality-or-errors-with-long-prompts)
- [366: How would you isolate users who share a vLLM server with prefix caching?](#366-how-would-you-isolate-users-who-share-a-vllm-server-with-prefix-caching)
- [367: What other side channels or data leaks exist in shared LLM serving?](#367-what-other-side-channels-or-data-leaks-exist-in-shared-llm-serving)
- [368: How can GPUs be shared between workloads safely?](#368-how-can-gpus-be-shared-between-workloads-safely)
- [369: How can a user cause a denial of service on a self-hosted model, and how do you prevent it?](#369-how-can-a-user-cause-a-denial-of-service-on-a-self-hosted-model-and-how-do-you-prevent-it)
- [370: How do you handle supply-chain security for model weights?](#370-how-do-you-handle-supply-chain-security-for-model-weights)
- [371: What is a model backdoor, and can quantization hide or create one?](#371-what-is-a-model-backdoor-and-can-quantization-hide-or-create-one)
- [372: Do self-hosted open models need extra safety layers?](#372-do-self-hosted-open-models-need-extra-safety-layers)
- [373: How do you meet data residency and compliance requirements with self-hosted models?](#373-how-do-you-meet-data-residency-and-compliance-requirements-with-self-hosted-models)
- [374: How do licenses of open-weight models affect a commercial product?](#374-how-do-licenses-of-open-weight-models-affect-a-commercial-product)
- [375: How would you design isolation for a multi-tenant SaaS that offers per-customer fine-tuned models?](#375-how-would-you-design-isolation-for-a-multi-tenant-saas-that-offers-per-customer-fine-tuned-models)
- [376: How would you estimate the hardware for a chat product with 1,000 concurrent users?](#376-how-would-you-estimate-the-hardware-for-a-chat-product-with-1000-concurrent-users)
- [377: How does Little's law help with LLM capacity planning?](#377-how-does-littles-law-help-with-llm-capacity-planning)
- [378: After upgrading llama.cpp, a model starts producing garbage. What do you check?](#378-after-upgrading-llamacpp-a-model-starts-producing-garbage-what-do-you-check)
- [379: vLLM preallocates memory, so why can it still run out of memory under load?](#379-vllm-preallocates-memory-so-why-can-it-still-run-out-of-memory-under-load)
- [380: Users report TTFT spikes every few minutes. How do you investigate?](#380-users-report-ttft-spikes-every-few-minutes-how-do-you-investigate)
- [381: Two replicas of the same deployment give different outputs for the same request at temperature 0. Why?](#381-two-replicas-of-the-same-deployment-give-different-outputs-for-the-same-request-at-temperature-0-why)
- [382: How would you roll out a new model version with zero downtime?](#382-how-would-you-roll-out-a-new-model-version-with-zero-downtime)
- [383: How do you A/B test a cheaper quant against the current model?](#383-how-do-you-ab-test-a-cheaper-quant-against-the-current-model)
- [384: Should a company rent cloud GPUs or buy its own for self-hosting?](#384-should-a-company-rent-cloud-gpus-or-buy-its-own-for-self-hosting)
- [385: How do you calculate cost per million tokens for a self-hosted model?](#385-how-do-you-calculate-cost-per-million-tokens-for-a-self-hosted-model)
- [386: How would you run an LLM on an edge device like a Jetson or a Raspberry Pi?](#386-how-would-you-run-an-llm-on-an-edge-device-like-a-jetson-or-a-raspberry-pi)
- [387: How would you design a hybrid setup that uses local models but can burst to a hosted API?](#387-how-would-you-design-a-hybrid-setup-that-uses-local-models-but-can-burst-to-a-hosted-api)
- [388: How would you summarize long documents with a model that has a small context window?](#388-how-would-you-summarize-long-documents-with-a-model-that-has-a-small-context-window)
- [389: How would you design a private coding assistant for 200 developers?](#389-how-would-you-design-a-private-coding-assistant-for-200-developers)
- [390: Your app shows think tags in the answers after switching to a reasoning model. How do you fix it?](#390-your-app-shows-think-tags-in-the-answers-after-switching-to-a-reasoning-model-how-do-you-fix-it)
- [391: Constrained JSON generation sometimes hangs, producing endless whitespace or newlines. Why, and how do you fix it?](#391-constrained-json-generation-sometimes-hangs-producing-endless-whitespace-or-newlines-why-and-how-do-you-fix-it)
- [392: A small local model at temperature 0 keeps repeating the same paragraph. What's going on?](#392-a-small-local-model-at-temperature-0-keeps-repeating-the-same-paragraph-whats-going-on)
- [393: A big model is very slow on a Mac even though it "fits" in memory. What could be wrong?](#393-a-big-model-is-very-slow-on-a-mac-even-though-it-fits-in-memory-what-could-be-wrong)
- [394: You upgraded your embedding model, and search results got worse. What happened?](#394-you-upgraded-your-embedding-model-and-search-results-got-worse-what-happened)
- [395: Does quantizing an embedding model hurt retrieval?](#395-does-quantizing-an-embedding-model-hurt-retrieval)
- [396: How would you decide between a local model and a hosted API for a new feature?](#396-how-would-you-decide-between-a-local-model-and-a-hosted-api-for-a-new-feature)
- [397: How can you make model loading faster for autoscaling?](#397-how-can-you-make-model-loading-faster-for-autoscaling)
- [398: What are the trade-offs of scaling self-hosted models to zero?](#398-what-are-the-trade-offs-of-scaling-self-hosted-models-to-zero)
- [399: Can you use spot or preemptible GPUs for inference?](#399-can-you-use-spot-or-preemptible-gpus-for-inference)
- [400: How would you trace self-hosted LLM calls end to end?](#400-how-would-you-trace-self-hosted-llm-calls-end-to-end)
- [401: How do you catch quality regressions in production?](#401-how-do-you-catch-quality-regressions-in-production)
- [402: What are the risks of using a local model as an LLM-as-judge?](#402-what-are-the-risks-of-using-a-local-model-as-an-llm-as-judge)
- [403: How can distillation help with local deployment?](#403-how-can-distillation-help-with-local-deployment)
- [404: You trained a QLoRA adapter on a 4-bit base. How should you serve it?](#404-you-trained-a-qlora-adapter-on-a-4-bit-base-how-should-you-serve-it)
- [405: How do sliding window attention models affect memory and serving?](#405-how-do-sliding-window-attention-models-affect-memory-and-serving)
- [406: How do hybrid models with state-space layers change self-hosting?](#406-how-do-hybrid-models-with-state-space-layers-change-self-hosting)
- [407: How do images affect memory and latency in vision models?](#407-how-do-images-affect-memory-and-latency-in-vision-models)
- [408: How would you self-host speech-to-text next to your LLM?](#408-how-would-you-self-host-speech-to-text-next-to-your-llm)
- [409: Why are agent workloads hard on self-hosted servers?](#409-why-are-agent-workloads-hard-on-self-hosted-servers)
- [410: How does vLLM support request priorities?](#410-how-does-vllm-support-request-priorities)
- [411: The GPU isn't fully used, but vLLM throughput is low. What could be the bottleneck?](#411-the-gpu-isnt-fully-used-but-vllm-throughput-is-low-what-could-be-the-bottleneck)
- [412: How do you handle GPUs in Kubernetes reliably?](#412-how-do-you-handle-gpus-in-kubernetes-reliably)
- [413: Where should model weights live in a Kubernetes setup?](#413-where-should-model-weights-live-in-a-kubernetes-setup)
- [414: What is Docker Model Runner?](#414-what-is-docker-model-runner)
- [415: Is it OK to run Ollama in production?](#415-is-it-ok-to-run-ollama-in-production)
- [416: How would you explain to non-technical stakeholders why the local model is worse than ChatGPT?](#416-how-would-you-explain-to-non-technical-stakeholders-why-the-local-model-is-worse-than-chatgpt)
- [417: How do you reduce hallucinations with a local model?](#417-how-do-you-reduce-hallucinations-with-a-local-model)
- [418: How would you build a validate-and-retry loop for structured output from a local model?](#418-how-would-you-build-a-validate-and-retry-loop-for-structured-output-from-a-local-model)
- [419: How can you use n > 1 sampling to improve answers from a local model?](#419-how-can-you-use-n--1-sampling-to-improve-answers-from-a-local-model)
- [420: How would you build a model cascade with a small and a large local model?](#420-how-would-you-build-a-model-cascade-with-a-small-and-a-large-local-model)
- [421: Can you run LLMs inside the browser, and when does it make sense?](#421-can-you-run-llms-inside-the-browser-and-when-does-it-make-sense)
- [422: Why is it risky to deploy a new open model on its release day?](#422-why-is-it-risky-to-deploy-a-new-open-model-on-its-release-day)
- [423: Why can public benchmarks mislead you when choosing a local model?](#423-why-can-public-benchmarks-mislead-you-when-choosing-a-local-model)
- [424: What would be on your checklist before putting a self-hosted model in production?](#424-what-would-be-on-your-checklist-before-putting-a-self-hosted-model-in-production)
- [425: A GPU node dies while it's streaming answers. How should the system behave?](#425-a-gpu-node-dies-while-its-streaming-answers-how-should-the-system-behave)
- [426: A GPU server's disk fills up and the inference service fails. What are the usual causes?](#426-a-gpu-servers-disk-fills-up-and-the-inference-service-fails-what-are-the-usual-causes)
- [427: How do you keep your app easy to switch between local models and runtimes?](#427-how-do-you-keep-your-app-easy-to-switch-between-local-models-and-runtimes)
- [428: Walk through what happens when a chat request hits a vLLM server.](#428-walk-through-what-happens-when-a-chat-request-hits-a-vllm-server)
- [429: Walk through what happens when you run ollama run llama3.2 for the first time.](#429-walk-through-what-happens-when-you-run-ollama-run-llama32-for-the-first-time)
- [430: How would you serve an LLM for a hospital that cannot send any data outside its network?](#430-how-would-you-serve-an-llm-for-a-hospital-that-cannot-send-any-data-outside-its-network)
- [431: How would you choose between MIG partitions and separate small GPUs for many small models?](#431-how-would-you-choose-between-mig-partitions-and-separate-small-gpus-for-many-small-models)
- [432: How does power and cooling factor into self-hosting decisions?](#432-how-does-power-and-cooling-factor-into-self-hosting-decisions)
- [433: How would you compare two quants with real users without them knowing?](#433-how-would-you-compare-two-quants-with-real-users-without-them-knowing)
- [434: How would you handle a model that does well in English but worse in other languages after quantization?](#434-how-would-you-handle-a-model-that-does-well-in-english-but-worse-in-other-languages-after-quantization)
- [435: What do you do when a self-hosted model's output gets cut off in the middle of a sentence for some users only?](#435-what-do-you-do-when-a-self-hosted-models-output-gets-cut-off-in-the-middle-of-a-sentence-for-some-users-only)
- [436: How would you safely let a local model execute tools on internal systems?](#436-how-would-you-safely-let-a-local-model-execute-tools-on-internal-systems)
- [437: When would you put a reranker or guard model on the same GPU as the main LLM?](#437-when-would-you-put-a-reranker-or-guard-model-on-the-same-gpu-as-the-main-llm)
- [438: How does context length per request affect the number of users a GPU can serve?](#438-how-does-context-length-per-request-affect-the-number-of-users-a-gpu-can-serve)
- [439: Why might a model give better answers through Ollama than through your own llama.cpp build, using the same GGUF?](#439-why-might-a-model-give-better-answers-through-ollama-than-through-your-own-llamacpp-build-using-the-same-gguf)
- [440: What is the role of an inference gateway separate from the model servers?](#440-what-is-the-role-of-an-inference-gateway-separate-from-the-model-servers)
- [441: How do you handle model warm-up and graceful shutdown in a deployment?](#441-how-do-you-handle-model-warm-up-and-graceful-shutdown-in-a-deployment)
- [442: How would you investigate a gradual memory increase in a long-running inference server?](#442-how-would-you-investigate-a-gradual-memory-increase-in-a-long-running-inference-server)
- [443: How would you serve both a fast autocomplete model and a slow reasoning model without one hurting the other?](#443-how-would-you-serve-both-a-fast-autocomplete-model-and-a-slow-reasoning-model-without-one-hurting-the-other)
- [444: How would you measure whether prefix caching is actually helping?](#444-how-would-you-measure-whether-prefix-caching-is-actually-helping)
- [445: What are the trade-offs of running one big replica vs many small replicas of a model?](#445-what-are-the-trade-offs-of-running-one-big-replica-vs-many-small-replicas-of-a-model)
- [446: Your vLLM server is fine for short prompts but very slow for 100K-token prompts. What can you do?](#446-your-vllm-server-is-fine-for-short-prompts-but-very-slow-for-100k-token-prompts-what-can-you-do)
- [447: When would you choose a smaller model at higher precision over a bigger model at lower precision?](#447-when-would-you-choose-a-smaller-model-at-higher-precision-over-a-bigger-model-at-lower-precision)
- [448: How do you handle the different chat template and tool format needs when supporting many model families in one app?](#448-how-do-you-handle-the-different-chat-template-and-tool-format-needs-when-supporting-many-model-families-in-one-app)
- [449: What metrics would you put on a dashboard for a self-hosted LLM platform?](#449-what-metrics-would-you-put-on-a-dashboard-for-a-self-hosted-llm-platform)
- [450: What are the most common mistakes teams make when they start self-hosting models?](#450-what-are-the-most-common-mistakes-teams-make-when-they-start-self-hosting-models)

---

# Easy Questions (1-150)

## 1: What does it mean to run a model locally or self-host it?

It means the model weights sit on hardware you control, and your own process runs inference on them. That can be your laptop, a desktop with a GPU, or servers in your own cloud account or data center.

With a hosted API like OpenAI or Claude you send text to someone else's servers and get text back. With a self-hosted model the prompt never leaves your machines, and you pay for hardware instead of per token.

## 2: Why would a company choose to self-host a model instead of using a hosted API?

The common reasons are:

- **Privacy and compliance:** data can't leave the network (health, finance, government, legal).
- **Cost at high volume:** if you keep GPUs busy all day, owning them can be cheaper than paying per token.
- **Control:** you pick the exact model version, and it won't change or be retired under you.
- **Offline use:** edge devices, factories, ships, air-gapped networks.
- **Customization:** you can fine-tune and serve your own weights.

## 3: What are the main downsides of self-hosting models?

You take on all the work a provider normally does: buying or renting GPUs, keeping drivers and runtimes updated, scaling, monitoring and handling outages. Open-weight models you can run are often weaker than the best hosted models, especially on hard reasoning and long agent tasks.

Cost is also easy to get wrong. A GPU that sits idle most of the day costs money anyway, so at low traffic a hosted API is usually cheaper.

## 4: What is the difference between open-weight and open-source models?

An open-weight model gives you the trained weights so you can download and run it. It doesn't necessarily give you the training data, the training code or a permissive license.

Open source, in the strict sense (OSI's Open Source AI Definition), also asks for enough information about the data and the code to rebuild the model. Most popular models such as Llama, Gemma and Qwen are open-weight. In daily talk people mix the two words, but in an interview it's good to show you know the difference.

## 5: Why does the license of an open-weight model matter?

The license decides what you're allowed to do. Some models use Apache 2.0 or MIT, which let you use them commercially with few limits. Others, like the Llama license, add their own rules, such as an acceptable use policy, a limit on very large companies, or a requirement to show attribution.

Before you put a model into a product, read its license and check that your use case is allowed. Fine-tuned versions usually inherit the base model's license.

## 6: What are model parameters, and why does the count matter for local use?

Parameters are the numbers (weights) the model learned in training. A "7B" model has about 7 billion of them, and a "70B" model has about 70 billion.

The count is the first thing that tells you how much memory you need. Each parameter takes 2 bytes in 16-bit precision, so a 7B model needs about 14 GB just for the weights. Bigger models are usually smarter but slower and harder to fit on one machine.

## 7: How do you roughly estimate how much memory a model needs?

Multiply the number of parameters by the bytes per parameter, then add room for the KV cache and runtime overhead.

| Precision | Bytes per parameter | 8B model weights |
| --------- | ------------------- | ---------------- |
| FP16/BF16 | 2                   | ~16 GB           |
| 8-bit     | 1                   | ~8 GB            |
| 4-bit     | ~0.5                | ~4.5-5 GB        |

On top of that, add 10-30% for the KV cache and buffers. Long contexts and many parallel users need more.

## 8: What is VRAM, and why is it so important for running LLMs?

VRAM is the memory on a GPU. To run a model fast on a GPU, the weights and the KV cache have to sit in VRAM, because moving data over PCIe from normal RAM is much slower.

If the model doesn't fit, you have to use a smaller model, quantize it, split it across GPUs, or offload part of it to the CPU, which slows things down a lot. VRAM size is usually the first limit you hit, before raw GPU speed.

## 9: Can you run an LLM without a GPU?

Yes. Tools like llama.cpp and Ollama run models on the CPU only. Small quantized models (1B-8B) are usable on a modern laptop CPU, maybe at a few to a couple of dozen tokens per second depending on the model and the machine.

It works for testing, light personal use and edge devices. For many users at once or for big models, a CPU is too slow, mostly because of limited memory bandwidth.

## 10: Why are Apple Silicon Macs popular for running local models?

M-series Macs use unified memory: the CPU and GPU share the same RAM. A Mac with 64 GB or 128 GB of memory can give most of it to the GPU, which is more than most consumer graphics cards have.

The memory bandwidth is also high (hundreds of GB/s on Pro, Max and Ultra chips), and generation speed depends mostly on bandwidth. llama.cpp and Ollama use Metal on Macs, and Apple's MLX framework is also built for them.

## 11: What is inference, and how is it different from training?

Training changes the model's weights by showing it data and adjusting the numbers. Inference uses the finished weights to produce output for a new input.

When you run a model locally with Ollama, llama.cpp or vLLM, you're doing inference. It needs far less memory and compute than training, which is why you can run a model on a laptop that could never have been trained there.

## 12: What is a token?

A token is the unit of text a model reads and writes. It's often a word, part of a word or a punctuation mark. In English, one token is about 3-4 characters on average.

Speed, context length and cost are all measured in tokens. When someone says a local setup does "40 tokens per second", they mean the model generates about 40 of these pieces each second.

## 13: What is the context window?

The context window is the maximum number of tokens the model can look at in one request: the system prompt, the chat history, any documents you add, and the answer it's writing.

A model may support 128K tokens, but the tool you run it in may use a smaller default to save memory. Longer contexts need more memory for the KV cache, so locally you often set the context size on purpose instead of using the maximum.

## 14: What is the KV cache?

When a model generates text, each new token needs to look at all the earlier tokens. The KV cache stores the key and value vectors for the earlier tokens, so the model doesn't have to compute them again for every new token.

It makes generation much faster, but it takes memory, and the amount grows with context length and with the number of requests running at once. In a server, the KV cache often uses more VRAM than you'd expect.

## 15: What are the two phases of generating text, prefill and decode?

**Prefill** (prompt processing) reads the whole prompt at once and fills the KV cache. It's limited by compute and runs fast because the GPU handles many tokens in parallel.

**Decode** generates the answer one token at a time. Each step has to read all the weights from memory, so it's limited by memory bandwidth. That's why a long prompt and a long answer feel different in speed.

## 16: What do time to first token and tokens per second mean?

Time to first token (TTFT) is how long the user waits before the first word appears. It mostly depends on prefill time and on how long the request waits in a queue.

Tokens per second (TPS) is how fast the rest of the answer is generated. For a chat UI both matter: a low TTFT makes the app feel responsive, and a TPS above normal reading speed makes streaming feel smooth.

## 17: What is the difference between latency and throughput when serving models?

Latency is how long one request takes. Throughput is how much total work the server does, often measured in tokens per second across all users.

They pull against each other. Batching many requests together raises throughput, but each request may get a bit slower. A personal chat app cares about latency; a batch job that processes millions of documents cares about throughput.

## 18: What is the difference between a base model and an instruct (chat) model?

A base model was only trained to predict the next token on large text data. It's good at continuing text but doesn't reliably follow instructions or hold a conversation.

An instruct or chat model was fine-tuned further to follow instructions and answer in a chat format. For apps you almost always want the instruct version. Base models are mostly used as a starting point for your own fine-tuning.

## 19: What is a chat template?

A chat template turns a list of messages (system, user, assistant) into the exact text format the model was trained on, with special tokens that mark where each turn starts and ends. Each model family has its own format.

If you use the wrong template, the model may ramble, ignore the system prompt or never stop. Tools like Ollama, llama.cpp (with `--jinja`) and vLLM read the template from the model's files, so you rarely write one by hand.

## 20: What is Hugging Face Hub, and how is it used with local models?

Hugging Face Hub is the main website for sharing models. Model makers upload their weights there, and the community uploads converted and quantized versions such as GGUF and AWQ files.

vLLM loads models straight from a Hub model ID, and llama.cpp can download GGUF files from the Hub with the `-hf` flag. Ollama can also pull GGUF models from the Hub with `ollama run hf.co/<user>/<repo>`.

## 21: What is a model card?

A model card is the README of a model repository. It describes what the model is for, how it was trained, which languages it supports, its context length, the license, the recommended settings and its known limits.

Before you use a model, read the card. It often tells you the right sampling settings and the prompt format, and quantized repos list the available quant types and their sizes.

## 22: What is the safetensors format?

Safetensors is a file format from Hugging Face for storing model weights. It's fast to load, supports memory mapping, and, unlike the old PyTorch pickle files (`.bin`), it can't run hidden code when you load it.

Most models on Hugging Face are published in safetensors. vLLM and Transformers load it directly. For llama.cpp and Ollama you usually use GGUF instead, which can be made from safetensors.

## 23: Why are pickle-based model files a security risk?

Old PyTorch `.bin` and `.pt` files use Python's pickle format. Loading a pickle can run any Python code that the file's author put in it, so a malicious model file can take over your machine.

Prefer safetensors or GGUF from sources you trust. If you have to load an old checkpoint with PyTorch, use `torch.load(..., weights_only=True)`, which is the default in recent PyTorch versions.

## 24: What are the main tools for running models locally?

- **Ollama:** easy tool for running models on a laptop or a single server, with a CLI and REST API.
- **llama.cpp:** C/C++ inference engine for GGUF models that runs almost everywhere, CPU or GPU.
- **vLLM:** high-throughput serving engine for GPUs, built for many concurrent users.
- **LM Studio:** desktop app with a GUI, based on llama.cpp and MLX.
- **SGLang** and **TensorRT-LLM:** other production serving engines.

## 25: When would you pick Ollama, llama.cpp or vLLM?

- **Ollama** when you want something running in minutes on a dev machine or a small internal server, with simple model management.
- **llama.cpp** when you need fine control, unusual hardware (CPU, Vulkan, older GPUs, ARM boards), or you want to embed inference in your own app.
- **vLLM** when you serve many users on NVIDIA or AMD GPUs and care about throughput, batching and production features.

A common path is to prototype with Ollama and move to vLLM for production.

## 26: What is the relationship between Ollama and llama.cpp?

Ollama started as a friendly wrapper around llama.cpp. It added model management, a REST API and an easy CLI on top of llama.cpp's inference code.

Over time Ollama built its own engine, written in Go on top of the GGML tensor library, and now uses it for many newer model families, especially multimodal ones. It still uses the GGUF format, and both projects share GGML, the low-level library underneath.

## 27: What is GGML?

GGML is a C tensor library made by Georgi Gerganov, the author of llama.cpp. It does the low-level math (matrix multiplications and so on) on many backends: CPU, CUDA, Metal, Vulkan and more.

llama.cpp, whisper.cpp and Ollama's engine are built on top of it. The name GGUF also comes from it; it's the file format for GGML-based tools.

## 28: What is a "model runner" in plain terms?

It's the program that loads the weights into memory, takes your prompt, runs the math and gives back tokens. Ollama, llama.cpp and vLLM are all model runners, though they differ in features and in who they're built for.

The model file is just data. Without a runner it does nothing.

## 29: What does "OpenAI-compatible API" mean for local tools?

It means the local server accepts the same HTTP requests as OpenAI's API, such as `POST /v1/chat/completions`, and returns responses in the same shape.

Ollama, llama.cpp's `llama-server`, vLLM, LM Studio and SGLang all offer this. So you can point the official OpenAI SDK, LangChain or the Vercel AI SDK at your local server by changing the base URL, and keep most of your app code the same.

## 30: How do you use the OpenAI SDK with a local model?

Change `baseURL` to the local server and pass any API key (local servers often don't check it unless you configure one).

```ts
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "http://localhost:11434/v1", // Ollama
  apiKey: "ollama", // required by the SDK, ignored by Ollama
});

const res = await client.chat.completions.create({
  model: "llama3.2",
  messages: [{ role: "user", content: "Say hi in one word." }],
});

console.log(res.choices[0].message.content);
```

The same code works with vLLM (`http://localhost:8000/v1`) or `llama-server` (`http://localhost:8080/v1`) if you change the URL and model name.

## 31: What is quantization?

Quantization stores the model's weights with fewer bits. Instead of 16 bits per weight, you might use 8 or 4 bits.

The model gets 2-4 times smaller, needs less memory and often runs faster, because generation is limited by how many bytes you read from memory. The cost is some loss of quality, which is small at 8 bits and usually acceptable at 4 bits for most tasks.

## 32: Why is quantization so important for local models?

Without it, most good models wouldn't fit on consumer hardware. A 32B model in FP16 needs about 64 GB for weights, but at 4 bits it needs about 18-20 GB and fits on a 24 GB GPU.

It also speeds up generation, since each token needs fewer bytes read from memory. For local use, a bigger model at 4 bits usually beats a smaller model at full precision.

## 33: What is GGUF?

GGUF is the file format used by llama.cpp, Ollama, LM Studio and other GGML-based tools. One `.gguf` file holds the weights (often quantized), the tokenizer, the chat template and metadata such as the architecture and context length.

Because everything is in one file, it's easy to download, share and run. GGUF replaced the older GGML file format in 2023.

## 34: What is AWQ?

AWQ (Activation-aware Weight Quantization) is a 4-bit quantization method for GPU inference. It looks at which weights matter most, based on the size of the activations that pass through them, and protects those during quantization so quality stays high.

AWQ models are stored in Hugging Face format (safetensors plus a quantization config) and run in vLLM, SGLang, TGI and Transformers. They're not used with llama.cpp or Ollama, which use GGUF.

## 35: What is the difference between GGUF and AWQ?

GGUF is a file format with many quantization types inside it (Q4_K_M, Q8_0 and so on). It's built for llama.cpp-style runners and works well on CPU, Apple Silicon and mixed CPU/GPU setups.

AWQ is a quantization method for GPU serving engines like vLLM. Its models are Hugging Face-style folders. Roughly: GGUF for laptops and Ollama, AWQ (or GPTQ, FP8) for GPU servers running vLLM.

## 36: What is GPTQ?

GPTQ is a post-training quantization method, usually to 4 bits, that quantizes weights one layer at a time and corrects for the error it adds, using a small calibration dataset.

It came out around the same time as AWQ and serves the same purpose: making models small enough for GPU serving. vLLM, SGLang and Transformers support GPTQ models.

## 37: What is FP8?

FP8 is an 8-bit floating point format. Newer NVIDIA GPUs (Hopper like H100, Ada like L40S and RTX 40-series, and Blackwell) can do math in FP8 directly in hardware.

FP8 weights halve memory compared to BF16 with very little quality loss, and the math also gets faster on supported GPUs. It's one of the most common choices for production serving in vLLM.

## 38: What is the difference between FP16 and BF16?

Both use 16 bits. FP16 gives more bits to precision and fewer to range. BF16 (brain float) keeps the same range as FP32 but with less precision.

Most modern models are trained in BF16, because it handles very large and very small values without overflow. For inference, running a BF16 model in FP16 usually works, but it can occasionally overflow, so use BF16 if the GPU supports it.

## 39: What do names like Q4_K_M and Q8_0 mean in GGUF files?

- The number after `Q` is roughly the bits per weight (4, 5, 6, 8).
- `K` means it's a k-quant, a newer, better scheme that groups weights into blocks with their own scales.
- The last letter is the size variant: `S` (small), `M` (medium), `L` (large). Larger keeps more important tensors at higher precision.
- `_0` and `_1` are the older, simpler quant types.

So `Q4_K_M` is a 4-bit k-quant, medium variant. It's the most common default.

## 40: Which GGUF quant should you start with?

Q4_K_M is the usual starting point. It gives a good balance between size and quality and is the default for most Ollama model tags.

If you have spare memory, Q5_K_M or Q6_K are a bit closer to the original. Q8_0 is almost identical to full precision. Go below 4 bits (Q3, IQ2) only when you really need a bigger model to fit, and test the quality.

## 41: What is Ollama?

Ollama is a free, open-source tool for running LLMs on your own machine. You install it, run `ollama run <model>`, and it downloads the model and starts a chat in the terminal.

It also runs a local server with a REST API on port 11434, plus an OpenAI-compatible API, so apps can use the model. It runs on macOS, Windows and Linux, and there's an official Docker image.

## 42: How do you install Ollama?

- **macOS and Windows:** download the app from ollama.com and run the installer.
- **Linux:** run the install script:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

- **Docker:** `docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama`

After installing, `ollama --version` checks that it works. On Linux the script also sets up a systemd service so the server starts on boot.

## 43: How do you run a model with Ollama for the first time?

```bash
ollama run llama3.2
```

If the model isn't on your machine yet, Ollama downloads it first, then opens an interactive chat. Type `/bye` to exit. You can also pass a prompt directly for a one-off answer:

```bash
ollama run llama3.2 "Explain DNS in two sentences."
```

## 44: What is the difference between ollama pull and ollama run?

`ollama pull <model>` only downloads the model (or updates it to the latest version of that tag). `ollama run <model>` pulls it if needed, loads it into memory and starts a chat.

In scripts, Dockerfiles and CI you usually use `pull` so the model is ready before the app starts sending requests.

## 45: What are the most common Ollama CLI commands?

| Command                     | What it does                           |
| --------------------------- | -------------------------------------- |
| `ollama run <model>`        | Chat with a model (pulls it if needed) |
| `ollama pull <model>`       | Download or update a model             |
| `ollama list`               | List downloaded models                 |
| `ollama ps`                 | Show models loaded in memory           |
| `ollama stop <model>`       | Unload a model from memory             |
| `ollama rm <model>`         | Delete a model from disk               |
| `ollama show <model>`       | Show details, parameters and template  |
| `ollama create <name> -f F` | Build a custom model from a Modelfile  |
| `ollama cp <src> <dst>`     | Copy a model under a new name          |
| `ollama serve`              | Start the server manually              |

## 46: What is a model tag in Ollama?

A tag picks a specific version of a model, written after a colon: `qwen3:8b`, `llama3.2:1b`, `gemma3:27b`. Tags usually mean the size, and some also name the quantization, like `llama3.1:8b-instruct-q8_0`.

If you don't give a tag, Ollama uses `latest`, which is whatever variant the maintainers picked as default, often a 4-bit quant of a mid-size version. In real projects, pin the tag so you know exactly which model you're running.

## 47: Where does Ollama store downloaded models?

By default:

- macOS: `~/.ollama/models`
- Windows: `C:\Users\<you>\.ollama\models`
- Linux (installed as a service): `/usr/share/ollama/.ollama/models`

You can change the location with the `OLLAMA_MODELS` environment variable, for example to move models to a bigger disk. Models are stored as content-addressed blobs, so two models that share a layer only store it once.

## 48: What port does Ollama listen on, and how do you check it's running?

Ollama listens on `127.0.0.1:11434` by default. You can check it with:

```bash
curl http://localhost:11434
# Ollama is running

curl http://localhost:11434/api/version
```

To change the address or port, set `OLLAMA_HOST`, for example `OLLAMA_HOST=0.0.0.0:11434`.

## 49: How do you call Ollama's REST API to chat?

Send a POST request to `/api/chat` with the model and a list of messages:

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2",
  "messages": [{ "role": "user", "content": "Why is the sky blue?" }],
  "stream": false
}'
```

The answer is in `message.content`. Without `"stream": false` the API streams back one JSON object per line as the model writes.

## 50: What is the difference between /api/generate and /api/chat in Ollama?

`/api/generate` takes a single `prompt` string (plus an optional `system`) and returns a completion. It's handy for one-shot tasks.

`/api/chat` takes a `messages` array with roles, so it fits conversations, tool calling and images in messages. For most apps `/api/chat` is the better choice.

## 51: How does streaming work in the Ollama API?

Streaming is on by default. Ollama sends back newline-delimited JSON: each line is a JSON object with a small piece of the answer. The last object has `"done": true` and includes stats like `eval_count` (tokens generated) and `total_duration`.

Your client reads the response line by line and shows each piece as it arrives. Set `"stream": false` to get one full JSON response instead.

## 52: How do you use Ollama from JavaScript?

Install the official `ollama` package:

```ts
import ollama from "ollama";

const res = await ollama.chat({
  model: "llama3.2",
  messages: [{ role: "user", content: "Give me 3 names for a cat." }],
});
console.log(res.message.content);

// streaming
const stream = await ollama.chat({
  model: "llama3.2",
  messages: [{ role: "user", content: "Tell a short story." }],
  stream: true,
});
for await (const part of stream) process.stdout.write(part.message.content);
```

It works in Node.js and, through `ollama/browser`, in the browser.

## 53: How do you use Ollama from Python?

Install the official package with `pip install ollama`:

```python
from ollama import chat

response = chat(
    model="llama3.2",
    messages=[{"role": "user", "content": "What is a mutex?"}],
)
print(response.message.content)
```

For async code there's `AsyncClient`, and for a remote server you create `Client(host="http://my-server:11434")`.

## 54: What is a Modelfile?

A Modelfile is a plain text file, a bit like a Dockerfile, that describes a custom Ollama model. It names the base model and can set parameters, a system prompt, a chat template or a LoRA adapter.

```text
FROM llama3.2
PARAMETER temperature 0.3
PARAMETER num_ctx 8192
SYSTEM "You are a support bot for Acme. Answer in short sentences."
```

Then `ollama create acme-bot -f Modelfile` builds it and `ollama run acme-bot` uses it.

## 55: What instructions can you use in a Modelfile?

- `FROM` (required): the base model, a GGUF file or a safetensors folder.
- `PARAMETER`: runtime settings like `temperature`, `num_ctx`, `top_p`, `stop`.
- `TEMPLATE`: the prompt template, written in Go template syntax.
- `SYSTEM`: the default system message.
- `MESSAGE`: example messages added to the start of the conversation.
- `LICENSE`: the license text.
- `REQUIRES`: the minimum Ollama version the model needs.
- `CAPABILITY`: adds a capability (like tools) to a model.

Older Modelfiles you find online may also have `ADAPTER` for LoRA adapters. Check the current Modelfile docs before relying on it.

## 56: How do you see the Modelfile of a model you already have?

```bash
ollama show --modelfile llama3.2
```

This prints the full Modelfile, including the template, parameters and license. It's a good starting point when you want to make a custom version: copy it, change what you need and run `ollama create`.

`ollama show llama3.2` without flags prints a short summary: architecture, parameter count, context length, quantization and capabilities.

## 57: How do you load a GGUF file you downloaded into Ollama?

Write a Modelfile that points to the file:

```text
FROM ./my-model-Q4_K_M.gguf
```

```bash
ollama create my-model -f Modelfile
ollama run my-model
```

If the GGUF has a chat template in its metadata, Ollama tries to use it. If the model answers strangely, add a `TEMPLATE` and `PARAMETER stop` lines that match the model's chat format.

## 58: What does ollama ps show?

It lists the models that are loaded in memory right now, with their size, how they're split between CPU and GPU (for example `100% GPU` or `48%/52% CPU/GPU`), the context length, and when they'll be unloaded.

It's the first command to run when a model is slow: if it isn't 100% on the GPU, part of it is running on the CPU.

## 59: How long does Ollama keep a model in memory?

By default Ollama unloads a model 5 minutes after its last request. The next request has to load it again, which can take seconds for big models.

You can change this per request with `keep_alive` (for example `"10m"`, `"24h"`, `-1` to keep it forever, or `0` to unload right away), or globally with the `OLLAMA_KEEP_ALIVE` environment variable.

## 60: How do you pre-load a model so the first user request is fast?

Send an empty request to load it, with a long `keep_alive`:

```bash
curl http://localhost:11434/api/generate -d '{"model": "llama3.2", "keep_alive": -1}'
```

The model loads and stays in memory. This is useful right after a deploy, so the first real user doesn't pay the load time.

## 61: How do you change the context length in Ollama?

There are a few ways:

- Per request: `"options": { "num_ctx": 16384 }` in the API call.
- In a Modelfile: `PARAMETER num_ctx 16384`.
- Globally: the `OLLAMA_CONTEXT_LENGTH` environment variable.
- In the interactive CLI: `/set parameter num_ctx 16384`.

Ollama's default depends on how much VRAM you have: 4K tokens under 24 GB, 32K for 24-48 GB, and 256K at 48 GB or more. That's often smaller than what the model supports, so if long prompts seem to be "forgotten", this is the first thing to check.

## 62: What happens when a prompt is longer than num_ctx in Ollama?

Ollama cuts the input to fit, dropping the oldest part of the prompt. It doesn't throw an error, so it's easy to miss. The model just answers without seeing part of your document or the start of the conversation, which often looks like the model "ignoring" instructions.

Check the `prompt_eval_count` in the response stats. If it's suspiciously close to `num_ctx`, your prompt was probably cut.

## 63: How do you get JSON output from Ollama?

Pass `format` in the request. `"format": "json"` asks for any valid JSON. Better, pass a JSON schema so the output has the exact shape you need:

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2",
  "messages": [{"role": "user", "content": "Tell me about Canada."}],
  "stream": false,
  "format": {
    "type": "object",
    "properties": {
      "name": {"type": "string"},
      "capital": {"type": "string"}
    },
    "required": ["name", "capital"]
  }
}'
```

It also helps to say in the prompt that you want JSON and describe the fields.

## 64: Does Ollama support tool calling?

Yes, for models trained for it (Llama 3.1+, Qwen 3, Mistral and others; the Ollama library marks them with a "tools" tag). You pass a `tools` array with function definitions in `/api/chat`. If the model wants to call one, the response has `message.tool_calls` with the function name and arguments.

Your code runs the function, adds the result as a message with role `tool`, and calls the model again so it can use the result. Ollama never runs your functions itself.

## 65: How do you send images to a vision model in Ollama?

Use a model with vision support (for example `gemma3`, `qwen2.5vl` or `llama3.2-vision`) and add base64 images to the message:

```python
from ollama import chat

res = chat(
    model="gemma3",
    messages=[{
        "role": "user",
        "content": "What is in this picture?",
        "images": ["./photo.jpg"],  # the Python lib accepts paths or bytes
    }],
)
print(res.message.content)
```

In the raw REST API, `images` is an array of base64 strings.

## 66: How do you create embeddings with Ollama?

Pull an embedding model (like `nomic-embed-text` or `embeddinggemma`) and call `/api/embed`:

```bash
curl http://localhost:11434/api/embed -d '{
  "model": "nomic-embed-text",
  "input": ["first sentence", "second sentence"]
}'
```

It returns an `embeddings` array, one vector per input. You can use these for RAG with a vector database. The older `/api/embeddings` endpoint is legacy; use `/api/embed`.

## 67: How do you list the models available on an Ollama server through the API?

```bash
curl http://localhost:11434/api/tags
```

It returns all downloaded models with their names, sizes and details. `GET /api/ps` returns the models that are loaded in memory right now. The OpenAI-compatible `GET /v1/models` works too.

## 68: How do you make Ollama reachable from other machines?

Set `OLLAMA_HOST=0.0.0.0` so it listens on all network interfaces instead of only localhost. On Linux with systemd:

```bash
sudo systemctl edit ollama
# add:
# [Service]
# Environment="OLLAMA_HOST=0.0.0.0:11434"
sudo systemctl daemon-reload && sudo systemctl restart ollama
```

Be careful: Ollama has no built-in authentication. Anyone who can reach the port can use (and delete) your models, so put it behind a firewall or a reverse proxy with auth.

## 69: Why can a browser app get CORS errors when calling Ollama?

Ollama only accepts browser requests from certain origins (localhost and a few app schemes) by default. A web page served from another origin gets blocked.

Add the origins you trust to `OLLAMA_ORIGINS`, for example `OLLAMA_ORIGINS=https://myapp.example.com`. Avoid `*` on a machine that's reachable from the network, since any website you visit could then call your local Ollama.

## 70: How do you set the system prompt in Ollama?

There are three places:

- In a Modelfile with `SYSTEM "..."`, so it becomes the default for that model.
- Per request, as a `{"role": "system", ...}` message in `/api/chat`, or the `system` field in `/api/generate`.
- In the interactive CLI with `/set system "..."`.

A system message in the request overrides the Modelfile's default.

## 71: What sampling options can you set in an Ollama request?

You pass them in `options`:

```json
{
  "model": "llama3.2",
  "prompt": "Write a haiku about Go.",
  "options": {
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 40,
    "num_predict": 200,
    "seed": 42,
    "stop": ["\n\n"]
  }
}
```

`num_predict` limits how many tokens the model can generate, and `seed` makes runs repeatable when everything else is the same.

## 72: What is temperature?

Temperature controls how random the next-token choice is. Low values (0-0.3) make the model pick the most likely tokens, so answers are focused and repeatable, which is good for extraction and code. Higher values (0.7-1.0) give more varied, creative output.

Many model cards list recommended values, and some reasoning models are tuned for a specific temperature, so check before you change it.

## 73: What are top_p and top_k?

Both limit which tokens the model can pick from. `top_k` keeps only the k most likely tokens. `top_p` (nucleus sampling) keeps the smallest set of tokens whose probabilities add up to p, for example 0.9.

They cut off unlikely, often nonsense tokens while keeping some variety. Many local tools also support `min_p`, which drops tokens far less likely than the top one.

## 74: How do you use thinking (reasoning) models in Ollama?

For models that support it (like `qwen3`, `deepseek-r1` and `gpt-oss`), set `think` in the request. The reasoning comes back in a separate `message.thinking` field, and the final answer in `message.content`:

```python
from ollama import chat

res = chat(
    model="qwen3",
    messages=[{"role": "user", "content": "Is 221 a prime number?"}],
    think=True,
)
print("Thinking:", res.message.thinking)
print("Answer:", res.message.content)
```

`think=False` turns reasoning off for models that allow it, which is faster for simple questions.

## 75: How do you run Ollama in Docker with an NVIDIA GPU?

Install the NVIDIA Container Toolkit on the host, then:

```bash
docker run -d --gpus=all \
  -v ollama:/root/.ollama \
  -p 11434:11434 \
  --name ollama ollama/ollama

docker exec -it ollama ollama run llama3.2
```

The volume keeps downloaded models when the container is recreated. For AMD GPUs there's an `ollama/ollama:rocm` image.

## 76: How do you see the Ollama server logs?

- macOS: `~/.ollama/logs/server.log`
- Linux (systemd): `journalctl -u ollama -f`
- Windows: `%LOCALAPPDATA%\Ollama\server.log`
- Docker: `docker logs ollama`

Set `OLLAMA_DEBUG=1` for more detail. The logs show which GPU was found, how many layers were offloaded and why a load failed.

## 77: How do you use a Hugging Face GGUF model directly in Ollama?

```bash
ollama run hf.co/bartowski/Llama-3.2-3B-Instruct-GGUF:Q4_K_M
```

The part after the colon picks the quant file in the repo. If you leave it out, Ollama picks Q4_K_M when it exists. This saves you from downloading files by hand and writing a Modelfile.

## 78: How do you run your own fine-tuned model in Ollama?

The simple way is to merge the LoRA adapter into the base model after training, so you have one full set of weights. Then either point a Modelfile at the safetensors folder, or convert it to GGUF with llama.cpp's `convert_hf_to_gguf.py` and quantize it:

```text
FROM ./my-finetuned-model-Q4_K_M.gguf
```

```bash
ollama create my-finetune -f Modelfile
```

Make sure the template matches what you used in training. If you want many adapters on one base model, swapped per request, vLLM is a better fit than Ollama.

## 79: What does the stats block at the end of an Ollama response tell you?

The final response includes:

- `total_duration`: the whole request, in nanoseconds.
- `load_duration`: time spent loading the model (high on a cold start).
- `prompt_eval_count` / `prompt_eval_duration`: prompt tokens and prefill time.
- `eval_count` / `eval_duration`: generated tokens and generation time.

Tokens per second = `eval_count / eval_duration * 1e9`. In the CLI, `ollama run <model> --verbose` prints these after each answer.

## 80: What is the Ollama model library?

It's the list of models on ollama.com/library that you can pull by name, like `llama3.2`, `qwen3`, `gemma3`, `mistral`, `deepseek-r1` and `gpt-oss`. Each page shows the available tags, sizes, capabilities (tools, vision, thinking, embedding) and the license.

You can also push your own models to ollama.com under your namespace with `ollama push <user>/<model>` after signing in.

## 81: What is llama.cpp?

llama.cpp is an open-source LLM inference engine written in C/C++, started by Georgi Gerganov and now hosted at `github.com/ggml-org/llama.cpp`. It runs GGUF models on almost any hardware: CPUs, NVIDIA and AMD GPUs, Apple Silicon, Vulkan devices and more.

It has few dependencies, supports many quantization types and can split a model between CPU and GPU. Many other tools, such as LM Studio and earlier Ollama, are built on it.

## 82: How do you get llama.cpp on your machine?

You have a few options:

- Install a package: `brew install llama.cpp` on macOS/Linux, or `winget install llama.cpp` on Windows.
- Download a prebuilt binary from the GitHub releases page (there are builds for CUDA, Vulkan, Metal, CPU and so on).
- Use the official Docker images.
- Build from source with CMake:

```bash
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp
cmake -B build -DGGML_CUDA=ON   # leave out for CPU, Metal is on by default on macOS
cmake --build build --config Release -j
```

## 83: What are the main programs that come with llama.cpp?

- `llama-cli`: chat with a model in the terminal.
- `llama-server`: HTTP server with an OpenAI-compatible API and a web UI.
- `llama-quantize`: convert a GGUF file to a smaller quant type.
- `llama-bench`: measure prompt and generation speed.
- `llama-perplexity`: measure model quality on a text file.
- `llama-imatrix`: build an importance matrix for better low-bit quants.
- `convert_hf_to_gguf.py`: Python script that converts a Hugging Face model to GGUF.

## 84: How do you chat with a model using llama-cli?

Point it at a local GGUF file, or let it download one from Hugging Face:

```bash
# local file
llama-cli -m ./models/qwen3-8b-Q4_K_M.gguf

# download from Hugging Face (cached for next time)
llama-cli -hf ggml-org/gemma-3-1b-it-GGUF
```

It starts in chat mode for models with a chat template and uses the template from the GGUF file. Use `-p "..."` to send a single prompt, and Ctrl+C to quit.

## 85: How do you start llama-server?

```bash
llama-server -m ./models/qwen3-8b-Q4_K_M.gguf --port 8080 -c 8192 -ngl 99
```

It starts an HTTP server on port 8080 (the default) with:

- a built-in web chat UI at `http://localhost:8080`,
- OpenAI-compatible endpoints like `/v1/chat/completions`, `/v1/completions` and `/v1/embeddings`,
- its own endpoints like `/completion`, `/health` and `/tokenize`.

## 86: What does the -ngl flag do in llama.cpp?

`-ngl` (`--n-gpu-layers`) sets how many of the model's layers go to the GPU. The rest stay on the CPU.

`-ngl 99` (or any number higher than the layer count) puts the whole model on the GPU, which is the fastest. If it doesn't fit, lower the number until it does. More layers on the GPU means faster generation, so you aim for the highest number that fits. Recent builds try to fit as many layers as they can automatically.

## 87: What does the -c flag do in llama.cpp?

`-c` (`--ctx-size`) sets the context size in tokens. Bigger values let you use longer prompts and conversations, but the KV cache grows with it, so you need more memory.

`-c 0` means "use the model's full trained context". On a small GPU, a huge context can push layers off the GPU and slow everything down, so pick what you actually need.

## 88: What does the -hf flag do?

`-hf <user>/<repo>[:quant]` downloads a GGUF model from Hugging Face and caches it locally:

```bash
llama-server -hf unsloth/Qwen3-8B-GGUF:Q4_K_M
```

If you don't give a quant, it picks Q4_K_M when the repo has it. For multimodal models it also downloads the matching projector file. It saves you from downloading files by hand.

## 89: How do you call llama-server from code?

Use any OpenAI client, or plain HTTP:

```bash
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [{"role": "user", "content": "Write a regex for an email."}],
    "temperature": 0.2
  }'
```

`llama-server` serves one model per process (unless you use its router mode), so the `model` field is mostly ignored, though clients may still require you to send it.

## 90: How do you check that llama-server is ready?

Call `GET /health`. It returns `{"status": "ok"}` with HTTP 200 when the model is loaded, and HTTP 503 while it's still loading.

Use it as a readiness probe in Docker or Kubernetes so traffic only arrives after the model is ready.

## 91: How do you protect llama-server with an API key?

Start it with `--api-key`:

```bash
llama-server -m model.gguf --api-key my-secret-key --host 0.0.0.0
```

Clients then send `Authorization: Bearer my-secret-key`. You can also set it through the `LLAMA_API_KEY` environment variable so it doesn't show up in the process list. For anything public, still put it behind HTTPS and a reverse proxy.

## 92: What is the default host of llama-server, and why does it matter?

It listens on `127.0.0.1` by default, so only the same machine can reach it. To allow other machines, pass `--host 0.0.0.0`.

That's a good safe default. Opening it up without `--api-key` and a firewall means anyone on the network can use your GPU.

## 93: How do you convert a Hugging Face model to GGUF?

Use the conversion script from the llama.cpp repo, then quantize:

```bash
pip install -r requirements.txt
python convert_hf_to_gguf.py ./Qwen3-8B --outtype bf16 --outfile qwen3-8b-bf16.gguf
llama-quantize qwen3-8b-bf16.gguf qwen3-8b-Q4_K_M.gguf Q4_K_M
```

First you make a full-precision GGUF, then shrink it. The model's architecture must be supported by llama.cpp, or the script will fail.

## 94: What is llama-bench used for?

It measures speed in a repeatable way: prompt processing (`pp`) and text generation (`tg`) in tokens per second.

```bash
llama-bench -m model.gguf -ngl 99 -p 512 -n 128
```

It's the standard way to compare quants, flags, builds and GPUs. People often post `llama-bench` tables when they discuss hardware.

## 95: What hardware backends does llama.cpp support?

CPU (x86 with AVX/AVX2/AVX-512, and ARM), NVIDIA CUDA, Apple Metal, AMD HIP/ROCm, Vulkan, Intel SYCL, Huawei CANN, MUSA, OpenCL and others, plus an RPC backend to spread a model across machines.

Vulkan is useful because it works on most GPUs, including AMD and Intel cards, without vendor toolkits. You choose the backend when you build (or pick the matching prebuilt binary).

## 96: What is mmap, and why does llama.cpp use it?

`mmap` maps a file into memory, so the operating system loads pages of it when they're needed instead of reading the whole thing up front. llama.cpp uses it by default for GGUF files.

It makes start-up fast, lets several processes share the same file in memory, and lets the OS page parts out when memory is tight. You can turn it off with `--no-mmap`, or lock the model in RAM with `--mlock` so it never gets swapped out.

## 97: What does the -t flag do in llama.cpp?

`-t` (`--threads`) sets how many CPU threads to use. For CPU inference, the best value is usually the number of physical (performance) cores, not logical cores. Using more threads than that often makes it slower.

When the whole model is on the GPU, the thread count matters much less.

## 98: What is the built-in web UI of llama-server?

When you open `http://localhost:8080` in a browser, `llama-server` serves a chat web app. You can chat, change sampling settings, upload images for vision models and see generation speed.

It's handy for quick testing on a remote GPU box without installing another frontend. You can turn it off with `--no-webui`.

## 99: What is GBNF in llama.cpp?

GBNF is a grammar format for llama.cpp. It describes exactly which text the model is allowed to produce, and during generation llama.cpp blocks any token that would break the grammar.

```text
root ::= "yes" | "no"
```

You pass it with `--grammar-file` or per request in the `grammar` field. llama.cpp can also turn a JSON schema into a grammar for you (`--json-schema` or `response_format` in the API).

## 100: How do you force JSON output from llama-server?

Send a JSON schema with `response_format`, the OpenAI way:

```json
{
  "messages": [
    { "role": "user", "content": "Extract the name and age: Tom is 31." }
  ],
  "response_format": {
    "type": "json_schema",
    "json_schema": {
      "schema": {
        "type": "object",
        "properties": {
          "name": { "type": "string" },
          "age": { "type": "integer" }
        },
        "required": ["name", "age"]
      }
    }
  }
}
```

The server turns the schema into a grammar, so the output always matches it.

## 101: What does --jinja do in llama-server?

It tells the server to use the Jinja chat template stored in the GGUF file, the same template the model has on Hugging Face. That's needed for tool calling and for templates that do more than a basic message format.

In current builds it's on by default. You can override the template with `--chat-template-file` if the one in the GGUF is broken.

## 102: Can llama.cpp run vision models?

Yes. Multimodal support lives in the `libmtmd` library. A vision model needs two files: the main GGUF and an `mmproj` (projector) GGUF that turns images into tokens the model understands.

```bash
llama-server -hf ggml-org/gemma-3-4b-it-GGUF
# or with local files
llama-server -m gemma-3-4b-it-Q4_K_M.gguf --mmproj mmproj-gemma-3-4b-it-f16.gguf
```

Then you send images through `/v1/chat/completions` like with OpenAI.

## 103: What is the difference between llama.cpp and the GGML library?

GGML is the tensor library: it does the math on the different backends. llama.cpp is the application layer on top: it loads GGUF models, handles tokenization, chat templates, sampling, the KV cache and the server.

Other projects use GGML directly too, like whisper.cpp for speech-to-text and Ollama's own engine.

## 104: How are llama.cpp releases versioned?

llama.cpp doesn't use semantic versions. Every merge to the main branch makes a new build with a number like `b6xxx` or higher, and prebuilt binaries are published for many of them.

Updates come several times a day. In production, pin a specific build number and test before you upgrade, because flags and defaults change quite often.

## 105: What is llamafile?

llamafile is a Mozilla project that packs llama.cpp and a model into one executable file. The same file runs on Linux, macOS, Windows and BSD.

You download one file, make it executable and run it, and you get a chat UI and an OpenAI-compatible server. It's handy for sharing a model with people who don't want to install anything.

## 106: What is vLLM?

vLLM is an open-source engine for serving LLMs with high throughput on GPUs. It started at UC Berkeley and is now one of the most used production engines.

Its main ideas are PagedAttention, which manages KV cache memory well, and continuous batching, which keeps the GPU busy with many requests at once. It offers an OpenAI-compatible server and supports most popular open models.

## 107: How do you install vLLM?

On Linux with an NVIDIA GPU:

```bash
uv venv --python 3.12 && source .venv/bin/activate
uv pip install vllm
```

The default wheels are built for a specific CUDA version, so check the installation docs if your setup is different. There are also Docker images (`vllm/vllm-openai`) and builds for AMD ROCm, Intel, TPUs and CPU. vLLM doesn't run natively on Windows; use WSL or Docker.

## 108: How do you start a vLLM server?

```bash
vllm serve Qwen/Qwen3-8B
```

This downloads the model from Hugging Face and starts an OpenAI-compatible server on port 8000. You can then call `http://localhost:8000/v1/chat/completions`.

Common flags are `--max-model-len` (context length), `--gpu-memory-utilization` and `--tensor-parallel-size` to use more than one GPU.

## 109: How do you run vLLM with Docker?

```bash
docker run --gpus all \
  -v ~/.cache/huggingface:/root/.cache/huggingface \
  -e HF_TOKEN=$HF_TOKEN \
  -p 8000:8000 --ipc=host \
  vllm/vllm-openai:latest \
  --model Qwen/Qwen3-8B
```

Mounting the Hugging Face cache stops the container from downloading the model on every start. `--ipc=host` (or a large `--shm-size`) is needed for shared memory when you use more than one GPU. In production, pin an image version instead of `latest`.

## 110: How do you use vLLM in a Python script without a server?

Use the `LLM` class for offline batch work:

```python
from vllm import LLM, SamplingParams

llm = LLM(model="Qwen/Qwen3-8B")
params = SamplingParams(temperature=0.2, max_tokens=200)

prompts = ["Summarize: ...", "Translate to French: ..."]
outputs = llm.generate(prompts, params)

for out in outputs:
    print(out.outputs[0].text)
```

For chat models use `llm.chat(messages, params)`, which applies the chat template. This is the fastest way to process a big dataset, since vLLM batches everything for you.

## 111: What is SamplingParams in vLLM?

`SamplingParams` holds the generation settings for offline use: `temperature`, `top_p`, `top_k`, `min_p`, `max_tokens`, `stop`, `seed`, `n` (how many answers per prompt), `presence_penalty` and so on.

You create one and pass it to `llm.generate()` or `llm.chat()`. In the server you pass the same settings as fields in the JSON request.

## 112: What does --gpu-memory-utilization do in vLLM?

It's the fraction of GPU memory vLLM can use, `0.9` (90%) by default. vLLM loads the weights, then gives most of the remaining space in that budget to the KV cache up front.

That's why `nvidia-smi` shows almost all memory used even when the server is idle; it's expected. Lower the value if other processes need the same GPU, or if you get out-of-memory errors at start-up.

## 113: What does --max-model-len do in vLLM?

It sets the maximum context length (prompt plus output) per request. By default vLLM uses the model's full context from its config, which can be 128K tokens or more.

If the KV cache can't hold even one request at that length, vLLM fails at start-up with an error saying so. Lowering `--max-model-len` to what you actually need is the usual fix, and it leaves room for more parallel requests.

## 114: How do you call a vLLM server from JavaScript?

```ts
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "http://localhost:8000/v1",
  apiKey: "EMPTY",
});

const stream = await client.chat.completions.create({
  model: "Qwen/Qwen3-8B",
  messages: [{ role: "user", content: "List 3 uses for Redis." }],
  stream: true,
});

for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0]?.delta?.content ?? "");
}
```

The `model` field must match the name vLLM serves, which is the Hugging Face ID unless you set `--served-model-name`.

## 115: What does --served-model-name do?

It sets the model name clients use in requests. Without it, they have to send the full Hugging Face path like `Qwen/Qwen3-8B`.

```bash
vllm serve Qwen/Qwen3-8B --served-model-name chat-model
```

This keeps client code stable when you swap the model underneath. It's also useful for pretending to be a model name your existing code already expects.

## 116: How do you add an API key to a vLLM server?

```bash
vllm serve Qwen/Qwen3-8B --api-key my-secret
# or
VLLM_API_KEY=my-secret vllm serve Qwen/Qwen3-8B
```

Clients then have to send `Authorization: Bearer my-secret`. This is a single shared key with no users or rate limits. For real multi-tenant use, put an API gateway or proxy (like LiteLLM or Envoy) in front.

## 117: Which endpoints does the vLLM OpenAI-compatible server offer?

The main ones are:

- `/v1/chat/completions` and `/v1/completions`
- `/v1/embeddings` (for embedding models)
- `/v1/models`
- `/v1/responses` (OpenAI Responses API)
- `/v1/audio/transcriptions` (for speech models)
- `/health` and `/metrics` (Prometheus)
- `/tokenize` and `/detokenize`

It also has `/score` and `/rerank` for cross-encoder and reranker models.

## 118: What GPUs does vLLM support?

Its main target is NVIDIA GPUs with CUDA. It also supports AMD GPUs with ROCm, Google TPUs, Intel GPUs and some other accelerators through plugins, and it has a CPU backend for testing.

Many optimizations, like FP8 kernels and FlashAttention versions, need newer GPUs. Check the docs for your exact card before you plan a deployment.

## 119: Why does vLLM take so long to start?

At start-up vLLM downloads the model (first time only), loads the weights onto the GPU, measures available memory, allocates the KV cache, and compiles and captures CUDA graphs for faster decoding (with `torch.compile` by default).

That can take from tens of seconds to several minutes for big models. You can speed up restarts by caching the model locally, keeping the compile cache on a persistent volume, or using `--enforce-eager` for quick testing (which turns off CUDA graphs and is slower at runtime).

## 120: What is the Hugging Face token used for in vLLM?

Some models, like Llama and Gemma, are "gated": you must accept their license on Hugging Face before you can download them. vLLM needs your token to download those.

Set it with `HF_TOKEN=hf_xxx` (or log in with `hf auth login`). Without it you get a 401 or 403 error when vLLM tries to fetch the model.

## 121: What are some other self-hosting tools besides Ollama, llama.cpp and vLLM?

- **LM Studio:** desktop app with a GUI and a local server, uses llama.cpp and MLX.
- **SGLang:** fast serving engine, strong at prefix caching and structured output.
- **TensorRT-LLM:** NVIDIA's engine, highly tuned for NVIDIA GPUs.
- **MLX / mlx-lm:** Apple's framework for running models on Apple Silicon.
- **LocalAI:** OpenAI-compatible server that wraps several backends.
- **Jan** and **Open WebUI:** chat interfaces on top of local servers.

Hugging Face TGI used to be on this list, but it's archived now, and Hugging Face recommends vLLM, SGLang or llama.cpp instead.

## 122: What is LM Studio?

LM Studio is a free desktop app for Windows, macOS and Linux. You can search and download models, chat with them and start a local OpenAI-compatible server, all from a GUI. It uses llama.cpp for GGUF models and MLX on Apple Silicon.

It's popular with people who don't want to use the terminal. It also has a CLI (`lms`) for scripting.

## 123: What is Open WebUI?

Open WebUI is a self-hosted web interface that looks like ChatGPT. It connects to Ollama or any OpenAI-compatible server and adds user accounts, chat history, document upload for RAG and model switching.

Teams often run Ollama or vLLM on a GPU server with Open WebUI in front, to give staff a private chat tool.

## 124: What is MLX?

MLX is Apple's open-source array framework for machine learning on Apple Silicon. The `mlx-lm` package runs and fine-tunes LLMs with it:

```bash
pip install mlx-lm
mlx_lm.generate --model mlx-community/Qwen3-8B-4bit --prompt "Hello"
```

MLX uses its own quantized format (models from the `mlx-community` org on Hugging Face). On Macs it's often a bit faster than llama.cpp, especially for prompt processing.

## 125: What is SGLang?

SGLang is an open-source serving engine like vLLM. It has an OpenAI-compatible server, continuous batching and paged KV cache, and it's known for RadixAttention, which reuses the KV cache of shared prefixes very well.

It's used a lot for big models like DeepSeek and for agent workloads with many requests that share long prompts. In practice teams often benchmark both vLLM and SGLang and pick the faster one for their model.

## 126: What is the main trade-off of quantization?

You trade quality for size and speed. Fewer bits means a smaller, faster model but a bit more error in the weights, which can show up as worse answers.

The loss is usually tiny at 8 bits, small at 5-6 bits, noticeable but often fine at 4 bits, and big below 3 bits. Small models suffer more from heavy quantization than big ones.

## 127: What is the difference between quantizing weights and quantizing activations?

Weight quantization stores the weights with fewer bits, which saves memory and speeds up memory-bound decoding. During the math, the weights are often expanded back to 16 bits.

Activation quantization also lowers the precision of the values flowing through the network during the math. That lets the GPU use faster low-precision math units, which helps compute-bound work like prefill and large batches. FP8 W8A8 does both; AWQ and GPTQ are usually weight-only (W4A16).

## 128: What does W4A16 mean?

It describes a quantization scheme: weights in 4 bits, activations in 16 bits. AWQ and GPTQ models are typically W4A16.

Other common ones are W8A8 (8-bit weights and activations, like FP8 or INT8) and W4A8. The more parts you quantize, the faster it can run on the right hardware, but the harder it is to keep quality.

## 129: What is post-training quantization?

Post-training quantization (PTQ) takes a finished model and converts its weights to lower precision, without retraining it. GGUF quants, AWQ, GPTQ and FP8 are all PTQ.

Some methods need a small calibration dataset (AWQ, GPTQ, imatrix GGUF), and some don't (basic GGUF quants, FP8 weights). It's quick, from minutes to a few hours, compared to training.

## 130: What is quantization-aware training?

Quantization-aware training (QAT) simulates low precision during training or fine-tuning, so the model learns to work well with rounded weights. It usually gives better quality than PTQ at the same bit width.

It's more expensive, so model makers do it, not end users. Google, for example, released QAT versions of Gemma 3 meant to be run at 4 bits.

## 131: What is a calibration dataset in quantization?

It's a small set of sample text (often a few hundred examples) passed through the model during quantization. The method watches the activations to decide which weights are important and how to round them.

AWQ, GPTQ and GGUF imatrix quants use one. The data should look like your real use: for a coding model, use code; for a non-English model, use that language.

## 132: What is perplexity, and how is it used to compare quants?

Perplexity measures how surprised a model is by a piece of text. Lower is better. To compare quants, you run the same text through the original model and the quantized one and see how much perplexity goes up.

It's quick and repeatable (`llama-perplexity` does it for GGUF), but it doesn't fully match real task quality. Also check on your own tasks.

## 133: What is KL divergence in quant comparisons?

KL divergence measures how different the quantized model's token probabilities are from the original model's, token by token. A smaller value means the quant behaves more like the original.

Many people now prefer it to perplexity, because two models can have similar perplexity but still choose different tokens. `llama-perplexity` can compute it against saved logits from the full-precision model.

## 134: What is an importance matrix (imatrix) in llama.cpp?

An imatrix records which weights matter most, based on activations from a calibration text. `llama-quantize` uses it to round important weights more carefully.

```bash
llama-imatrix -m model-f16.gguf -f calibration.txt -o imatrix.dat
llama-quantize --imatrix imatrix.dat model-f16.gguf model-IQ3_XXS.gguf IQ3_XXS
```

It helps most for low-bit quants (IQ and Q2-Q3 types), and many popular GGUF uploaders use it for all their quants.

## 135: What are the IQ quant types in GGUF?

IQ types (IQ1_S, IQ2_XXS, IQ2_XS, IQ3_XXS, IQ3_S, IQ4_XS, IQ4_NL and others) are "i-quants". They use smarter encoding (lattice-based codebooks) to keep more quality at very low bits.

They're best for squeezing a big model into limited memory, for example IQ2 or IQ3 for a 70B model on a 24 GB GPU. On some backends, especially CPU, they can be slower than K-quants. They're normally made with an imatrix.

## 136: How big is a Q4_K_M model compared to the original?

Q4_K_M uses roughly 4.9 bits per weight on average, because some tensors stay at higher precision. For an 8B model, that's about 4.6-4.9 GB versus about 16 GB in BF16, so around a third of the size.

The rough rule: GGUF size in GB ≈ parameters in billions × bits per weight / 8.

## 137: What is Q8_0 good for?

Q8_0 uses 8 bits per weight (about 8.5 with scales). Its quality is very close to the original model, and it's half the size of FP16.

Use it when you have enough memory and want the best quality, or as a reference to compare smaller quants against. It's also a common choice for small models (1-4B), where lower quants hurt more.

## 138: Can you quantize the KV cache?

Yes. Instead of storing keys and values in 16 bits, you can store them in 8 bits (or lower), which roughly halves KV cache memory. That lets you use a longer context or serve more requests.

- llama.cpp: `--cache-type-k q8_0 --cache-type-v q8_0` (V cache quantization needs flash attention).
- Ollama: `OLLAMA_KV_CACHE_TYPE=q8_0` (with flash attention on).
- vLLM: `--kv-cache-dtype fp8`.

8-bit KV cache usually costs very little quality; 4-bit can hurt more.

## 139: What is flash attention?

Flash attention is a faster way to compute attention. It works in tiles that fit in the GPU's fast on-chip memory, instead of writing a big attention matrix to slow memory. It's faster and uses less memory, especially with long contexts.

vLLM uses it by default where the GPU supports it. In llama.cpp you control it with `-fa` (`on`, `off` or `auto`), and in Ollama with `OLLAMA_FLASH_ATTENTION`.

## 140: What is a Mixture of Experts (MoE) model?

An MoE model has many "expert" sub-networks per layer, and a router picks only a few of them for each token. So a model may have 120B total parameters but only use about 5B per token.

For local use, this means: you still need memory for all the weights, but each token is computed much faster than with a dense model of the same size. gpt-oss, Qwen3-30B-A3B, Mixtral and DeepSeek V3 are MoE models.

## 141: What does a name like Qwen3-30B-A3B mean?

It means 30B total parameters, of which about 3B are active per token. It's an MoE model.

The total count tells you how much memory you need. The active count tells you roughly how fast it'll generate, closer to a 3B dense model than a 30B one. That's why such models feel fast even on a CPU or a Mac.

## 142: What is gpt-oss?

gpt-oss is OpenAI's open-weight model family, released in August 2025 under the Apache 2.0 license. There are two sizes: gpt-oss-120b (117B total, 5.1B active) and gpt-oss-20b (21B total, 3.6B active).

Both are MoE reasoning models. Their expert weights ship in the MXFP4 4-bit format, so the 20b model runs in about 16 GB of memory and the 120b fits on a single 80 GB GPU. Ollama, llama.cpp, vLLM and LM Studio all support them.

## 143: Which open-weight model families are common for self-hosting?

- **Qwen** (Alibaba): many sizes, strong at code and multilingual, mostly Apache 2.0.
- **Llama** (Meta): very widely supported, custom Llama license.
- **Gemma** (Google): good small and mid models, Gemma license.
- **Mistral** (Mistral AI): several Apache 2.0 models.
- **DeepSeek:** large MoE models with strong reasoning, MIT license.
- **gpt-oss** (OpenAI): Apache 2.0 reasoning models.

Model releases move fast, so check current benchmarks and licenses before you choose.

## 144: What are small language models, and why do they matter for local use?

Small models (roughly 0.5B-8B parameters) can run on laptops, phones and cheap GPUs. They're weaker at broad knowledge and hard reasoning, but they can be very good at narrow tasks, especially after fine-tuning.

Common uses are classification, extraction, autocomplete, routing and summarizing short texts, where a big model would be too slow or too expensive.

## 145: What is an embedding model, and can you self-host one?

An embedding model turns text into a vector of numbers, so similar texts get similar vectors. It's the base of semantic search and RAG.

Embedding models are small (often under 1B parameters) and easy to self-host. Ollama (`/api/embed`), llama.cpp (`--embedding`) and vLLM (`/v1/embeddings`) can all serve them. Popular ones include `nomic-embed-text`, BGE, Qwen3-Embedding and EmbeddingGemma.

## 146: What is a reranker, and can you run one locally?

A reranker takes a query and a list of candidate documents and scores how relevant each document is to the query. In RAG you fetch, say, 50 chunks with embeddings, then use a reranker to keep the best 5.

Rerankers are small cross-encoder models (like BGE reranker or Qwen3-Reranker). vLLM serves them through `/rerank` and `/score`, and llama.cpp has a `/reranking` endpoint.

## 147: What is the tokens per second you need for a good chat experience?

People read about 4-8 tokens per second, so anything above about 10-15 tokens per second feels smooth when streaming. Under 5 feels slow.

For agents and code tools, the model's output is read by a program, so higher speed matters more: the whole task waits on every step. Time to first token also matters, ideally under a second for chat.

## 148: Why is generation speed mostly limited by memory bandwidth?

To generate one token, the model has to read all its active weights from memory. With one user, the GPU does very little math per byte read, so it spends most of its time waiting for memory.

A rough upper limit is: tokens per second ≈ memory bandwidth ÷ model size in bytes. A 5 GB model on a GPU with 1,000 GB/s can reach at most about 200 tokens per second. That's why quantization speeds up generation.

## 149: What is speculative decoding in simple words?

A small, fast "draft" model guesses the next few tokens, and the big model checks all of them in one pass. Correct guesses are kept, and the rest are thrown away and regenerated.

The output is the same as the big model alone would produce, but faster, often 1.5-3 times on predictable text like code. llama.cpp, vLLM and SGLang all support it.

## 150: What is LoRA, and how does it relate to serving local models?

LoRA (Low-Rank Adaptation) fine-tunes a model by training small extra matrices instead of all the weights. The result is an adapter that's often only tens of megabytes.

For serving, you can merge the adapter into the base model, or keep it separate and load it on top. vLLM can serve many LoRA adapters on one base model at the same time, picking the right one per request, which saves a lot of GPU memory.

# Moderate Questions (151-300)

## 151: How does Ollama handle several requests at the same time?

Each loaded model can work on a number of requests in parallel, set by `OLLAMA_NUM_PARALLEL`. Extra requests wait in a queue, up to `OLLAMA_MAX_QUEUE` (512 by default). When the queue is full, Ollama returns HTTP 503.

Parallel requests share the model's context memory, so raising `OLLAMA_NUM_PARALLEL` uses more memory: roughly `num_ctx × num_parallel` tokens of KV cache. Ollama is fine for a small team, but it doesn't batch as efficiently as vLLM under heavy load.

## 152: How many models can Ollama keep in memory at once?

`OLLAMA_MAX_LOADED_MODELS` controls it. The default is 3 per GPU (or 3 on CPU), as long as they fit in memory. When a new model doesn't fit, Ollama unloads idle models to make room, or queues the request until a model is free.

If your app uses a chat model and an embedding model, both can stay loaded. If it switches between several big models, you'll see a lot of slow loads, so keep the number of models small or add memory.

## 153: How do you choose which GPUs Ollama uses?

Set the vendor's visibility variable before starting the server:

```bash
CUDA_VISIBLE_DEVICES=0,1 ollama serve      # NVIDIA
ROCR_VISIBLE_DEVICES=0 ollama serve        # AMD
```

Use GPU UUIDs from `nvidia-smi -L` instead of numbers if the order might change. By default Ollama puts a model on one GPU if it fits there; `OLLAMA_SCHED_SPREAD=1` makes it spread models across all GPUs.

## 154: How do you force a model to run fully on the CPU or set the number of GPU layers in Ollama?

Use the `num_gpu` option, which is the number of layers to put on the GPU:

```json
{ "model": "llama3.2", "prompt": "hi", "options": { "num_gpu": 0 } }
```

`0` runs it fully on the CPU. A number between 0 and the layer count splits it. Normally you let Ollama pick, since it estimates how many layers fit. Setting it by hand is useful for testing or when its estimate is wrong and you get out-of-memory errors.

## 155: A model in Ollama is suddenly much slower than before. How do you debug it?

1. Run `ollama ps`. If it shows a CPU/GPU split instead of `100% GPU`, part of the model is on the CPU.
2. Check whether you raised `num_ctx` or `OLLAMA_NUM_PARALLEL`: a bigger KV cache can push layers off the GPU.
3. Check whether another model or process is using GPU memory (`nvidia-smi`).
4. Look at the server log for the "offloaded X/Y layers to GPU" line.
5. Compare `load_duration` in the response stats; if it's high, the model is being reloaded each time.

## 156: How do you use Ollama with the Vercel AI SDK?

The simplest way is the OpenAI-compatible provider pointed at Ollama:

```ts
import { createOpenAICompatible } from "@ai-sdk/openai-compatible";
import { generateText } from "ai";

const ollama = createOpenAICompatible({
  name: "ollama",
  baseURL: "http://localhost:11434/v1",
});

const { text } = await generateText({
  model: ollama("qwen3:8b"),
  prompt: "Write a commit message for: fix null check in user service",
});
```

There are also community providers made just for Ollama. The same setup works for vLLM or `llama-server` with a different `baseURL`.

## 157: How do you use Ollama with LangChain?

Use the official integration package:

```python
from langchain_ollama import ChatOllama, OllamaEmbeddings

llm = ChatOllama(model="qwen3:8b", temperature=0)
print(llm.invoke("What is a vector database?").content)

embeddings = OllamaEmbeddings(model="nomic-embed-text")
vector = embeddings.embed_query("hello world")
```

In JavaScript the package is `@langchain/ollama`. `ChatOllama` supports tool calling and structured output through LangChain's usual `bind_tools` and `with_structured_output`.

## 158: How do you get typed structured output from Ollama in TypeScript?

Make a Zod schema, turn it into JSON Schema, pass it as `format`, and parse the result:

```ts
import ollama from "ollama";
import { z } from "zod";

const Country = z.object({
  name: z.string(),
  capital: z.string(),
  languages: z.array(z.string()),
});

const res = await ollama.chat({
  model: "qwen3:8b",
  messages: [{ role: "user", content: "Tell me about Canada." }],
  format: z.toJSONSchema(Country),
});

const country = Country.parse(JSON.parse(res.message.content));
```

Setting `temperature` to 0 also helps for extraction tasks.

## 159: How do you write a tool-calling loop with Ollama?

```python
from ollama import chat

def get_weather(city: str) -> str:
    """Get the current weather for a city."""
    return f"Sunny, 22C in {city}"

messages = [{"role": "user", "content": "What's the weather in Tbilisi?"}]

while True:
    res = chat(model="qwen3:8b", messages=messages, tools=[get_weather])
    messages.append(res.message)
    if not res.message.tool_calls:
        break
    for call in res.message.tool_calls:
        result = get_weather(**call.function.arguments)
        messages.append({"role": "tool", "content": result, "tool_name": call.function.name})

print(res.message.content)
```

The Python library builds the tool schema from the function's signature and docstring. Always add a limit on loop iterations in real code.

## 160: What are the limits of Ollama's OpenAI-compatible API?

It covers the common parts: chat completions, completions, embeddings, models, streaming, tools, JSON mode and images. Some OpenAI fields aren't supported or are ignored, and Ollama-only features like `keep_alive` don't have an OpenAI field.

Also, `num_ctx` can't be set through the OpenAI API per request, so you set it in a Modelfile or with `OLLAMA_CONTEXT_LENGTH`. If you need full control, use the native `/api/chat` endpoint.

## 161: How would you run Ollama with Docker Compose next to your app?

```yaml
services:
  ollama:
    image: ollama/ollama:0.40.16 # pin a version
    volumes:
      - ollama:/root/.ollama
    environment:
      - OLLAMA_KEEP_ALIVE=24h
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]

  api:
    build: .
    environment:
      - OLLAMA_URL=http://ollama:11434
    depends_on:
      - ollama

volumes:
  ollama:
```

The app reaches Ollama by its service name. Don't publish port 11434 to the host unless you need to, and pull the model in a startup step so the first request doesn't wait for a download.

## 162: How do you make sure a model is downloaded when an Ollama container starts?

The Ollama image doesn't pull models for you. Common options:

- Run `ollama pull <model>` in an init step or a small sidecar job after the server starts.
- Build your own image that starts the server during the build, pulls the model and stops, so the model is baked into the image.
- Keep models on a persistent volume, so they're only pulled once.

Baking the model in makes images large but gives fast, offline-friendly starts.

## 163: How do you move Ollama models to a machine with no internet?

Copy the models folder. On a machine with internet, pull the models, then copy `~/.ollama/models` (or your `OLLAMA_MODELS` path), which holds both `manifests` and `blobs`, to the same location on the offline machine.

Another way is to copy GGUF files and create the models there with a Modelfile. Either way, also install the same or a newer Ollama version on the offline machine.

## 164: How do you put authentication in front of Ollama?

Ollama has no users or API keys of its own. Put a reverse proxy in front of it that checks a key, and keep Ollama bound to localhost:

```nginx
server {
  listen 443 ssl;
  server_name llm.internal.example.com;

  location / {
    if ($http_authorization != "Bearer my-long-random-key") { return 401; }
    proxy_pass http://127.0.0.1:11434;
    proxy_buffering off;          # needed for streaming
    proxy_read_timeout 600s;      # long generations
  }
}
```

For per-user keys, rate limits and logging, use a gateway like LiteLLM in front instead.

## 165: Why do streaming responses from a local model sometimes arrive all at once behind a proxy?

The proxy is buffering the response. It waits for the whole answer (or a big chunk) before sending it on, so the user sees nothing and then everything.

Turn buffering off for that route, for example `proxy_buffering off;` in nginx, or send the `X-Accel-Buffering: no` header. Also raise read timeouts, because long generations can be cut by a 60-second default.

## 166: What are Ollama cloud models?

They're models that run on Ollama's own servers instead of your machine, but you use them through the same Ollama CLI and API. Their names end with `cloud` (for example `gpt-oss:120b-cloud`), and you need to sign in to an ollama.com account.

They let you try models too big for your hardware. Keep in mind your prompts then leave your machine, which defeats the point of local use for private data. You can turn cloud features off with `OLLAMA_NO_CLOUD=1`.

## 167: How do you check which quantization an Ollama model uses?

```bash
ollama show qwen3:8b
```

The output has a `quantization` line (for example `Q4_K_M`), along with the architecture, parameter count and context length. The tag page on ollama.com also lists the quant and size for every tag.

If you need a specific quant, pick a tag that names it, like `qwen3:8b-q8_0`, when it exists.

## 168: Why does a model in Ollama keep repeating itself, and how do you fix it?

Common causes are a wrong chat template, a missing stop token, a context that's too small (the model loses the start of the conversation), or sampling settings that are too strict for that model.

Fixes: check `ollama show --modelfile` for the right template and `stop` parameters; increase `num_ctx`; use the sampling values from the model card; and try a light `repeat_penalty` (like 1.1). For imported GGUF files, the template is the most common culprit.

## 169: How do you pin model versions in Ollama for reproducible deployments?

Tags like `qwen3:8b` can be updated on ollama.com. To be safe:

- Use specific tags that name the size and quant.
- Record the model digest from `ollama list` and check it in your deploy script.
- Or build your own model from a fixed GGUF file with a Modelfile and push it under your namespace, so nothing changes unless you change it.

Also pin the Ollama version itself, since engine updates can change output.

## 170: What does OLLAMA_FLASH_ATTENTION do, and when should you set it?

It turns flash attention on or off. Flash attention cuts KV cache memory and speeds up long contexts. Recent Ollama versions turn it on automatically for models and GPUs that support it.

You need it on to use a quantized KV cache (`OLLAMA_KV_CACHE_TYPE=q8_0`). Turn it off only if you hit a bug with a specific model or older GPU.

## 171: How do you set environment variables for Ollama on each OS?

- **macOS app:** `launchctl setenv OLLAMA_HOST "0.0.0.0"`, then restart the app.
- **Linux systemd:** `sudo systemctl edit ollama`, add `Environment="KEY=value"` lines under `[Service]`, then reload and restart.
- **Windows:** set them as user environment variables in system settings, then restart Ollama from the Start menu.
- **Docker:** pass `-e KEY=value`.

A common mistake is setting a variable in your shell and expecting the background service to see it.

## 172: How do you remove all unused models and free disk space in Ollama?

List them with `ollama list` and remove the ones you don't need with `ollama rm <model>`. Ollama removes the blobs a model used if no other model shares them.

Models are big (several GB each), so on dev machines it's easy to fill the disk. If you moved the store with `OLLAMA_MODELS`, check that path, not the default one.

## 173: What is the template syntax in an Ollama Modelfile?

Ollama uses Go's `text/template` syntax. The template gets variables like `.System`, `.Prompt`, `.Messages` (with `.Role` and `.Content`) and `.Tools`:

```text
TEMPLATE """{{- range .Messages }}<|im_start|>{{ .Role }}
{{ .Content }}<|im_end|>
{{ end }}<|im_start|>assistant
"""
PARAMETER stop "<|im_end|>"
```

You rarely write one from scratch: copy the template from a model of the same family with `ollama show --modelfile`, and only change it when you import a model whose template wasn't detected.

## 174: How do you make Ollama answers more repeatable?

Set `temperature` to 0 and fix a `seed`. With the same model, prompt, options, hardware and Ollama version, results will usually be the same.

They still aren't guaranteed to be identical, because GPU math with parallel requests or a different batch can round slightly differently. For tests, compare meaning or structure instead of exact strings.

## 175: How does llama-server handle several users at once?

It has a number of "slots", set with `-np` (`--parallel`). Each slot can work on one request, and continuous batching (on by default) runs all active slots together in one batch.

```bash
llama-server -m model.gguf -c 32768 -np 4
```

Recent builds set the number of slots automatically if you don't pass `-np`. Extra requests wait until a slot is free.

## 176: How is context split between slots in llama-server?

In the classic setup, the total context `-c` is divided equally between slots. With `-c 32768 -np 4`, each request can use up to 8192 tokens. If you need each user to have 32K, you'd set `-c 131072`.

Newer builds can use a unified KV cache (`--kv-unified`), where all slots share one buffer, so one long request can use more if others are short. Check `GET /props` or `GET /slots` to see the real per-slot size.

## 177: What does --cache-reuse do in llama-server?

It lets the server reuse parts of a slot's KV cache when a new prompt matches earlier content, even if it's shifted a bit. The value is the minimum chunk size to reuse:

```bash
llama-server -m model.gguf --cache-reuse 256
```

It helps with chat, where each new turn resends the whole conversation, and with code tools that resend a large, mostly unchanged file. It saves prefill time for long, repeated prompts.

## 178: How do you split a model across several GPUs in llama.cpp?

By default, llama.cpp splits layers across all visible GPUs (`--split-mode layer`). You can control the share each GPU gets with `--tensor-split`:

```bash
llama-server -m model.gguf -ngl 99 --tensor-split 3,1
```

That puts about three quarters of the model on GPU 0 and a quarter on GPU 1, which is useful when cards have different VRAM. `--split-mode row` splits tensors across GPUs instead, which can be faster on some setups but needs more GPU-to-GPU traffic.

## 179: What is --n-cpu-moe in llama.cpp?

For MoE models, it keeps the expert weights of the first N layers in system RAM while everything else stays on the GPU:

```bash
llama-server -m gpt-oss-120b-mxfp4.gguf -ngl 99 --n-cpu-moe 20
```

Only a few experts run for each token, so running them on the CPU costs less speed than offloading whole layers. This lets you run large MoE models like gpt-oss-120b or Qwen3-235B on a single consumer GPU plus a lot of RAM. `--cpu-moe` moves all experts to the CPU.

## 180: What does --override-tensor (-ot) do?

It lets you choose where specific tensors go, using a regex on their names:

```bash
llama-server -m model.gguf -ngl 99 -ot "blk\.(1[0-9])\.ffn_.*_exps\.=CPU"
```

This example keeps the expert tensors of layers 10-19 on the CPU. It's the low-level tool behind `--n-cpu-moe`, useful for fine-tuning what fits in VRAM.

## 181: How do you enable speculative decoding in llama-server?

Pass a small draft model from the same family (it must share the tokenizer):

```bash
llama-server -m Qwen3-32B-Q4_K_M.gguf -md Qwen3-0.6B-Q8_0.gguf \
  -ngl 99 -ngld 99 --draft-max 16 --draft-min 1
```

`--draft-max` is how many tokens the draft model guesses at a time. It helps most on predictable output like code or structured text, and less on creative writing. Measure with your real prompts to see if it's worth the extra memory.

## 182: How do you serve embeddings with llama-server?

Start it with an embedding model and the `--embedding` flag:

```bash
llama-server -m bge-m3-Q8_0.gguf --embedding --pooling cls -c 8192
```

Then call the OpenAI-style `POST /v1/embeddings`. The pooling type must match how the model was trained (`mean`, `cls` or `last`); the GGUF usually has the right default, so only set it if the docs tell you to.

## 183: How do you use LoRA adapters with llama-server?

Convert the adapter to GGUF with `convert_lora_to_gguf.py`, then load it at start-up:

```bash
llama-server -m base-model.gguf --lora my-adapter.gguf
```

`--lora-scaled file.gguf 0.5` applies it with a lower strength. The server also has a `/lora-adapters` endpoint to see and change adapter scales at runtime. The adapter must come from the same base model.

## 184: How do you see Prometheus metrics from llama-server?

Start it with `--metrics`, then scrape `GET /metrics`. It shows things like prompt and generated tokens, tokens per second, requests processing and deferred, and KV cache usage.

Also `GET /slots` shows what each slot is doing right now (turn it off with `--no-slots` in public setups, since it can show prompt data).

## 185: How do you handle reasoning (thinking) output in llama-server?

For reasoning models, `llama-server` can pull the thinking text out of the answer and return it in a separate `reasoning_content` field, set with `--reasoning-format` (for example `deepseek`, or `none` to leave it inline).

```bash
llama-server -m Qwen3-8B-Q4_K_M.gguf --reasoning-format deepseek
```

You can limit thinking with `--reasoning-budget` (`0` turns it off for models that support that). This keeps the chain of thought out of what you show the user.

## 186: How do you run llama-server as a service on Linux?

Use a systemd unit:

```ini
[Unit]
Description=llama.cpp server
After=network-online.target

[Service]
ExecStart=/opt/llama.cpp/llama-server -m /models/qwen3-8b-Q4_K_M.gguf \
  --host 127.0.0.1 --port 8080 -ngl 99 -c 16384 --metrics
Environment=LLAMA_API_KEY=change-me
Restart=on-failure
User=llama

[Install]
WantedBy=multi-user.target
```

Run it as its own user, keep secrets out of the command line, and pin the binary to a known build.

## 187: How do you pick a GGUF quant that fits your GPU?

1. Check free VRAM (for example 24 GB).
2. Leave room for the KV cache and buffers: 2-6 GB depending on context and slots.
3. Pick the biggest quant whose file size fits in what's left.

For 24 GB and 8K context: a 32B model at Q4_K_M (~19-20 GB) fits; a 70B model needs IQ2-level quants or CPU offload. If two options fit, a bigger model at Q4 usually beats a smaller one at Q8.

## 188: When should you offload part of a model to the CPU, and what does it cost?

Offload when the model you need doesn't fit in VRAM and a smaller quant would hurt quality too much. llama.cpp and Ollama run the GPU layers on the GPU and the rest on the CPU.

The cost is speed. Each token must also pass through the CPU layers, limited by system RAM bandwidth, which is often 10-20 times slower than VRAM. Even 20% of layers on the CPU can halve the speed. For MoE models, offloading only the experts (`--n-cpu-moe`) hurts much less.

## 189: Which popular GGUF uploaders should you know, and why do they matter?

Groups like `ggml-org`, `unsloth`, `bartowski` and `lmstudio-community` on Hugging Face publish GGUF versions of new models, often within hours of release. They usually provide many quant types, use an imatrix, and fix template bugs.

Model quality can differ between uploaders because of imatrix data and recipe choices, so stick with known sources. Unknown uploads could have broken templates, wrong quants or a different model than claimed.

## 190: What do the files in a split GGUF upload like model-00001-of-00003.gguf mean?

Big models are split into several files because Hugging Face limits file size. You download all the parts and point llama.cpp at the first one; it finds the others automatically.

```bash
llama-server -m Qwen3-235B-A22B-Q4_K_M-00001-of-00003.gguf
```

`-hf` handles split files for you. If you want one file, `llama-gguf-split --merge` joins them.

## 191: How do you read the metadata of a GGUF file?

- The Hugging Face website shows GGUF metadata (architecture, context length, chat template, tensors) when you click on a `.gguf` file.
- The `gguf` Python package has a `gguf-dump` tool that prints all metadata keys and tensor info.
- llama.cpp prints the main metadata when it loads a model.

It's useful to check the chat template, the trained context length and the quant type of each tensor.

## 192: What is the --mlock flag, and when do you need it?

`--mlock` asks the OS to keep the model in RAM and never swap it out. It's useful on CPU or partial-offload setups where the OS might page out parts of the model when other programs need memory, which causes sudden slowdowns.

You need enough free RAM and permission to lock memory (on Linux, a high enough `ulimit -l`). On a GPU-only setup it doesn't matter much.

## 193: How do you serve a vLLM model on several GPUs?

Use tensor parallelism:

```bash
vllm serve meta-llama/Llama-3.3-70B-Instruct --tensor-parallel-size 4
```

Each layer is split across the 4 GPUs, so the model only needs a quarter of the memory per GPU, and each token uses all GPUs together. The GPUs should be in one machine with a fast link (NVLink is best). Tensor parallel size usually has to divide the number of attention heads, so use 2, 4 or 8.

## 194: What is the difference between tensor parallelism and pipeline parallelism in vLLM?

- **Tensor parallelism** (`--tensor-parallel-size`) splits every layer across GPUs. All GPUs work on every token, so it lowers latency but needs a lot of fast GPU-to-GPU communication.
- **Pipeline parallelism** (`--pipeline-parallel-size`) puts different layers on different GPUs or nodes. It needs less communication, so it works across machines, but adds some latency.

A common setup for very big models: tensor parallel inside each node and pipeline parallel across nodes, like `-tp 8 -pp 2` for 16 GPUs on 2 nodes.

## 195: What does --max-num-seqs do in vLLM?

It sets the maximum number of requests vLLM processes together in one batch. Higher values give more throughput if there's KV cache space, but each request may get a bit slower, and more requests compete for memory.

If you see lots of requests waiting while GPU usage is low, raising it might help. If latency is too high or you see preemptions, lowering it can help.

## 196: What does --max-num-batched-tokens do in vLLM?

It limits the number of tokens processed in one engine step, adding up prompt chunks and decode tokens from all requests. With chunked prefill, long prompts are cut into chunks so they fit this budget.

Lower values protect decode latency for users who are already streaming. Higher values speed up prefill and time to first token for long prompts. You tune it based on which matters more for your traffic.

## 197: What is prefix caching in vLLM?

When requests start with the same text, like a long system prompt or shared documents, vLLM keeps the KV cache blocks for that prefix and reuses them instead of computing them again. It's on by default in the current engine.

It can cut time to first token a lot for chat apps, RAG with repeated context and agents. To get the most out of it, put fixed content (system prompt, tools, documents) at the start of the prompt and changing content at the end.

## 198: What is chunked prefill?

Chunked prefill splits a long prompt into smaller pieces and processes them across several engine steps, mixed with decode steps from other requests.

Without it, one huge prompt could block the GPU and freeze token streaming for every other user. With it, decode latency stays steady. vLLM turns it on by default where possible.

## 199: How do you get structured output from vLLM?

Use `response_format` with a JSON schema, like with OpenAI:

```python
from openai import OpenAI
client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")

res = client.chat.completions.create(
    model="Qwen/Qwen3-8B",
    messages=[{"role": "user", "content": "Classify: 'App crashes on login'"}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "ticket",
            "schema": {
                "type": "object",
                "properties": {"category": {"type": "string", "enum": ["bug", "feature", "question"]}},
                "required": ["category"],
            },
        },
    },
)
```

vLLM also accepts `structured_outputs` in `extra_body` for regex, choice lists and grammars. The older `guided_json` and `guided_choice` fields were removed in v0.12, so update old code.

## 200: How do you enable tool calling in vLLM?

Start the server with automatic tool choice and the right parser for the model family:

```bash
vllm serve Qwen/Qwen3-8B --enable-auto-tool-choice --tool-call-parser hermes
```

The parser reads the model's raw output and turns it into OpenAI-style `tool_calls`. Each family has its own (for example `hermes` for Qwen, `llama3_json` for Llama 3.x, `mistral`, `openai` for gpt-oss). If you use the wrong parser, tool calls come back as plain text in `content`.

## 201: How do you serve a reasoning model with vLLM so the thinking is separated from the answer?

Use `--reasoning-parser` with the parser for the model:

```bash
vllm serve Qwen/Qwen3-8B --reasoning-parser qwen3
```

The response then has the thinking in a separate reasoning field of the message (`reasoning_content` in older versions, `reasoning` in newer ones) and the final answer in `content`. Other parsers include `deepseek_r1` and `openai_gptoss`. Without it, the `<think>...</think>` text ends up mixed into `content`.

## 202: How do you serve several LoRA adapters with one base model in vLLM?

```bash
vllm serve meta-llama/Llama-3.1-8B-Instruct \
  --enable-lora \
  --lora-modules support=./adapters/support sql=./adapters/sql \
  --max-loras 4 --max-lora-rank 64
```

Each adapter shows up as its own model name. A request with `"model": "sql"` uses the SQL adapter, and `"model": "meta-llama/Llama-3.1-8B-Instruct"` uses the base model. vLLM batches requests for different adapters together, so ten fine-tuned "models" cost about the same GPU memory as one.

## 203: Can you load LoRA adapters into a running vLLM server?

Yes, if you allow it with `VLLM_ALLOW_RUNTIME_LORA_UPDATING=True`. Then you can call:

```bash
curl -X POST http://localhost:8000/v1/load_lora_adapter \
  -H "Content-Type: application/json" \
  -d '{"lora_name": "new-adapter", "lora_path": "/adapters/new"}'
```

and `/v1/unload_lora_adapter` to remove one. This is risky in production because anyone who can reach the endpoint can load files, so protect it and only allow it when you need it.

## 204: How do you run an AWQ or GPTQ model in vLLM?

Usually you just point vLLM at the quantized model. It reads the quantization config from the model's files and picks the right kernels:

```bash
vllm serve Qwen/Qwen3-32B-AWQ --max-model-len 16384
```

You can force a method with `--quantization` (for example `awq_marlin`), but that's rarely needed. vLLM uses fast Marlin-based kernels for 4-bit AWQ and GPTQ on supported NVIDIA GPUs.

## 205: How do you use FP8 in vLLM without a pre-quantized model?

Pass `--quantization fp8`:

```bash
vllm serve Qwen/Qwen3-8B --quantization fp8
```

vLLM converts the BF16 weights to FP8 while loading (dynamic quantization, no calibration). It halves weight memory and is fast on Hopper, Ada and Blackwell GPUs. For the best quality, use a model already quantized to FP8 with calibration, for example made with llm-compressor.

## 206: What does --kv-cache-dtype fp8 do in vLLM?

It stores the KV cache in FP8 instead of BF16, which halves its memory. That means more concurrent requests or longer contexts on the same GPU.

The quality loss is usually small, but check it on your tasks, especially for long-context work. Some setups use calibrated scales for the KV cache to keep accuracy higher.

## 207: Which vLLM metrics would you watch in production?

From the `/metrics` endpoint (Prometheus format):

- `vllm:num_requests_running` and `vllm:num_requests_waiting`: load and queueing.
- `vllm:kv_cache_usage_perc`: how full the KV cache is.
- `vllm:time_to_first_token_seconds`: latency users feel first.
- `vllm:e2e_request_latency_seconds`: full request time.
- Token counters for prompt and generation throughput.
- Preemption counts: a sign the KV cache is too small.

A growing waiting queue with full KV cache means you need more capacity.

## 208: What is preemption in vLLM?

When the KV cache fills up and running requests need more blocks, vLLM pauses (preempts) some requests and frees their memory. Later it recomputes their KV cache and continues them.

Users don't see errors, but preempted requests get slower. Frequent preemptions mean the cache is too small for your load. Fixes: raise `--gpu-memory-utilization`, lower `--max-num-seqs`, use FP8 KV cache, a smaller `--max-model-len`, or more GPUs.

## 209: vLLM fails at start-up with an out-of-memory error. What do you check?

1. Is the model too big for the GPU? Compare weight size to VRAM.
2. Is `--max-model-len` too high? The KV cache must fit at least one full-length request.
3. Is another process using the GPU? Check `nvidia-smi`.
4. Is `--gpu-memory-utilization` too high for a shared GPU, or too low to fit anything?
5. For vision models, multimodal profiling can use extra memory; limit images per prompt.

The usual fixes are a smaller context, a quantized model, more tensor parallelism or lowering `--max-num-seqs`.

## 210: How do you deploy vLLM on Kubernetes?

A basic setup has a Deployment with a GPU resource request, a Service and health probes:

```yaml
containers:
  - name: vllm
    image: vllm/vllm-openai:vX.Y.Z # replace with the version you tested
    args: ["--model", "Qwen/Qwen3-8B", "--max-model-len", "16384"]
    resources:
      limits:
        nvidia.com/gpu: 1
    readinessProbe:
      httpGet: { path: /health, port: 8000 }
      initialDelaySeconds: 60
    volumeMounts:
      - { name: models, mountPath: /root/.cache/huggingface }
```

Store the model on a persistent volume, give long start-up probes because loading is slow, and mount `/dev/shm` as memory for multi-GPU pods. For bigger setups there are projects like the vLLM production stack and llm-d.

## 211: How do you autoscale self-hosted LLM servers?

CPU usage is useless here. Scale on LLM-specific signals: requests waiting in the queue, KV cache usage, or time to first token, exported from `/metrics` and fed into something like KEDA or a custom HPA metric.

Scaling is slow because a new GPU pod has to start, pull a big image and load the model. Keep a minimum number of replicas warm, and use cached model volumes or faster loading to cut start time.

## 212: What does --generation-config do in vLLM?

By default vLLM reads the model's `generation_config.json` from Hugging Face and uses its sampling values (like `temperature` and `top_p`) as defaults when a request doesn't set them.

That can surprise you: two models may behave differently with the same client code. Use `--generation-config vllm` to ignore the model's file and use vLLM's own defaults, or always set sampling values in requests.

## 213: How do you override the chat template in vLLM?

Pass a Jinja template file:

```bash
vllm serve my-org/my-model --chat-template ./template.jinja
```

You need this when a model has no template, a broken one, or when you fine-tuned with a different format. Clients can also send `chat_template_kwargs` per request, for example `{"enable_thinking": false}` for Qwen3 to turn off reasoning.

## 214: How do you serve a vision model with vLLM and limit images per request?

```bash
vllm serve Qwen/Qwen2.5-VL-7B-Instruct --limit-mm-per-prompt '{"image": 2}'
```

Clients send images the OpenAI way, as `image_url` parts with a URL or a base64 data URL. Limiting images per prompt keeps memory use predictable, because vLLM reserves memory for the worst case at start-up.

## 215: How do you serve an embedding model with vLLM?

```bash
vllm serve Qwen/Qwen3-Embedding-0.6B --runner pooling
```

Then call `POST /v1/embeddings` with the OpenAI client. vLLM usually detects that a model is an embedding model, but setting the runner explicitly is safer. Older guides use `--task embed`, which newer versions replaced.

## 216: How do you benchmark a vLLM server?

vLLM has a built-in tool:

```bash
vllm bench serve \
  --model Qwen/Qwen3-8B \
  --dataset-name random --random-input-len 1024 --random-output-len 256 \
  --num-prompts 500 --request-rate 10
```

It reports throughput, TTFT, inter-token latency and their percentiles. Better still, replay a sample of your real prompts, because input and output lengths change the results a lot.

## 217: What does --enforce-eager do, and when do you use it?

It turns off CUDA graphs and compilation, so vLLM runs the model step by step in plain PyTorch. Start-up is much faster and uses a bit less memory.

Runtime is slower, especially for decoding small batches. Use it for debugging, quick tests, or when a model has a bug with graph capture, not in production.

## 218: How do you get log probabilities from a local model?

With vLLM or `llama-server`, use the OpenAI fields:

```json
{
  "model": "Qwen/Qwen3-8B",
  "messages": [
    { "role": "user", "content": "Is this spam? Answer yes or no: ..." }
  ],
  "max_tokens": 1,
  "logprobs": true,
  "top_logprobs": 5
}
```

Logprobs are handy for classification confidence, for checking how sure the model is, and for evaluation. vLLM may cap the number of `top_logprobs` it returns. Ollama also supports logprobs in recent versions.

## 219: How do you pick between Q4_K_M GGUF, AWQ and FP8 for a project?

Start from the runtime:

- **Ollama or llama.cpp** (laptops, Macs, CPU, small servers): GGUF, usually Q4_K_M or Q5_K_M.
- **vLLM or SGLang on older or smaller NVIDIA GPUs** (Ampere like A100/A10/RTX 30): AWQ or GPTQ 4-bit to fit the model.
- **vLLM on Hopper, Ada or Blackwell** with enough memory: FP8, which keeps quality near the original and is fast.
- **Blackwell:** NVFP4 is an option when quality tests pass.

Then check quality on your own tasks.

## 220: How do you quantize a model to AWQ today?

The old AutoAWQ library is archived and no longer maintained. Use llm-compressor from the vLLM project, which supports AWQ, GPTQ, FP8 and more:

```python
from llmcompressor import oneshot
from llmcompressor.modifiers.awq import AWQModifier

recipe = [AWQModifier(targets=["Linear"], scheme="W4A16", ignore=["lm_head"])]

oneshot(
    model="Qwen/Qwen3-8B",
    dataset="open_platypus",
    recipe=recipe,
    output_dir="Qwen3-8B-AWQ",
    max_seq_length=2048,
    num_calibration_samples=256,
)
```

The output is a compressed-tensors model that vLLM loads directly. Check the llm-compressor examples for the exact current arguments for your version.

## 221: How do you create an FP8 model with llm-compressor?

```python
from llmcompressor import oneshot
from llmcompressor.modifiers.quantization import QuantizationModifier

recipe = QuantizationModifier(targets="Linear", scheme="FP8_DYNAMIC", ignore=["lm_head"])

oneshot(model="Qwen/Qwen3-8B", recipe=recipe, output_dir="Qwen3-8B-FP8-Dynamic")
```

`FP8_DYNAMIC` uses static per-channel scales for weights and computes activation scales at runtime, so it needs no calibration data. The output loads in vLLM with `vllm serve ./Qwen3-8B-FP8-Dynamic`.

## 222: What is the status of AutoGPTQ and AutoAWQ?

Both are archived and no longer maintained. AutoGPTQ points users to GPTQModel, and AutoAWQ's work moved into other tools such as llm-compressor.

You'll still see them in older tutorials and in model names. Models made with them generally still load in vLLM and Transformers, but for new quantization work use llm-compressor or GPTQModel.

## 223: What is bitsandbytes, and where does it fit?

bitsandbytes is a library for 8-bit and 4-bit quantization (including the NF4 format) that quantizes weights on the fly when you load a model in Hugging Face Transformers.

It's mainly used for QLoRA fine-tuning and quick experiments, because it needs no pre-quantized files. For serving it's usually slower than AWQ, GPTQ or FP8 kernels. vLLM supports it, but it's rarely the best production choice.

## 224: What is NF4?

NF4 (4-bit NormalFloat) is a 4-bit data type from the QLoRA paper. Its 16 values are spaced to match the normal distribution that weights usually follow, so it keeps more information than plain 4-bit integers.

It's used through bitsandbytes, mostly for QLoRA: the frozen base model is stored in NF4 while the LoRA adapter trains in higher precision.

## 225: What are EXL2 and EXL3?

They're quantization formats from the ExLlama project (ExLlamaV2 and ExLlamaV3) for NVIDIA GPUs. They allow any average bits per weight, like 4.65 bpw, by mixing precisions across layers, so you can fill your VRAM exactly.

They're popular with hobbyists running large models on consumer GPUs through tools like TabbyAPI. They're less common in production than AWQ, GPTQ or FP8.

## 226: What are MXFP4 and NVFP4?

Both are 4-bit floating point formats with block scaling: small groups of values share a scale factor.

- **MXFP4** is an open standard (OCP Microscaling). gpt-oss ships its expert weights in MXFP4.
- **NVFP4** is NVIDIA's variant with smaller blocks and finer scales, made for Blackwell GPUs, which run FP4 math in hardware.

They give 4-bit sizes with hardware speedups on new GPUs, unlike W4A16 formats that expand weights back to 16 bits for the math.

## 227: How do you check if a quantized model is good enough for your use case?

1. Make a test set of 50-500 real tasks with expected answers or grading rules.
2. Run the full-precision (or FP8) model and the quantized one on it.
3. Compare scores, plus format errors (broken JSON, wrong tool calls), refusals and response length.
4. Check speed and memory at your real concurrency.

General benchmarks and perplexity help, but your own tasks are what matter. Tools like lm-evaluation-harness can run standard benchmarks against an OpenAI-compatible local endpoint.

## 228: Why do small models suffer more from quantization than big ones?

A small model has fewer weights, so each one carries more information, and rounding errors matter more. A 70B model has a lot of redundancy and handles 4-bit or even 3-bit well.

So for a 1B-3B model, Q8_0 or Q6_K is often worth it, while for 70B, Q4 or even IQ3 can be fine. Always test small models more carefully.

## 229: Which parts of a model are usually kept at higher precision when quantizing?

The embeddings, the output layer (`lm_head`), and sometimes attention parts are more sensitive, so many recipes keep them in 8 or 16 bits. That's why llm-compressor recipes often have `ignore=["lm_head"]`, and why GGUF's `_M` and `_L` variants keep some tensors at higher bits.

For MoE models, the router (gate) is usually left unquantized, because small errors there send tokens to the wrong experts.

## 230: How do you calculate the KV cache size for a model?

Per token: `2 (K and V) × layers × KV heads × head size × bytes per value`.

For Llama 3.1 8B: 32 layers, 8 KV heads, head size 128, BF16 (2 bytes):

```text
2 × 32 × 8 × 128 × 2 = 131,072 bytes ≈ 128 KB per token
```

So 32K tokens need about 4 GB, and 16 users with 8K each need about 16 GB. That's why context and concurrency matter as much as model size.

## 231: What is grouped-query attention, and why does it help local models?

In standard multi-head attention, each attention head has its own keys and values. In grouped-query attention (GQA), several query heads share one set of keys and values.

That makes the KV cache several times smaller (Llama 3 8B has 32 query heads but only 8 KV heads), so long contexts and many users fit in less memory. Most modern open models use GQA or something similar like multi-head latent attention (DeepSeek).

## 232: How would you size a GPU server for a team of 50 developers using a local coding model?

Rough approach:

1. Pick the model and quant, for example a 30B MoE coder in FP8 (~30 GB weights).
2. Estimate concurrency: 50 people rarely send requests at the same moment, maybe 5-10 at peak.
3. Estimate context: coding prompts are long, say 16-32K tokens per request.
4. KV cache: concurrency × context × KV bytes per token.
5. Add 10-20% headroom.

That might land on one 80 GB GPU or two 48 GB GPUs with vLLM. Then load test with real traffic and watch TTFT and queue length before buying more.

## 233: When is self-hosting cheaper than using an API?

It depends on use. A GPU costs the same whether it's busy or idle. If you keep it busy most of the day, the cost per token can be well below API prices. If it's idle 90% of the time, an API is almost always cheaper.

Do the math: (GPU cost per hour) ÷ (tokens you actually process per hour) vs. the API price per token. Include engineering and on-call time, which teams often forget. Many teams use APIs for low or bursty traffic and self-host only steady, high-volume work.

## 234: How can you use the same code for a local model and a hosted API?

Use OpenAI-compatible endpoints and keep the base URL, API key and model name in config:

```ts
const client = new OpenAI({
  baseURL: process.env.LLM_BASE_URL, // http://localhost:11434/v1 or a hosted API
  apiKey: process.env.LLM_API_KEY,
});
const model = process.env.LLM_MODEL;
```

Or use an abstraction like the Vercel AI SDK, LangChain or LiteLLM. Expect some differences in features (tool calling quality, structured output support), so test each target.

## 235: What is LiteLLM, and why use it with self-hosted models?

LiteLLM is an open-source Python library and proxy server that gives one OpenAI-style API in front of many backends: Ollama, vLLM, llama.cpp and hosted providers.

The proxy adds API keys per user or team, rate limits, spend tracking, logging, fallbacks and load balancing. It's a common way to give a company one endpoint where some models are local and some are hosted.

## 236: How do you load balance several vLLM or llama.cpp instances?

Put a load balancer or gateway in front of them. Plain round-robin works but wastes the KV cache: the same conversation lands on different servers each time, so prefix caching doesn't help.

Better options route by prefix or session (sticky sessions or hashing on a conversation ID), or use LLM-aware routers like the vLLM production stack router or llm-d, which look at queue length and cache contents.

## 237: How would you build a fully local RAG system?

- **Embeddings:** a local embedding model (for example `nomic-embed-text` or Qwen3-Embedding via Ollama or vLLM).
- **Vector store:** a self-hosted database like pgvector, Qdrant or Chroma.
- **Reranker (optional):** a local cross-encoder.
- **Generator:** a local chat model via Ollama, `llama-server` or vLLM.
- **Orchestration:** your own code or LangChain/LlamaIndex.

Watch the context size: retrieved chunks plus the question must fit in `num_ctx` or `--max-model-len`. Use the same embedding model for indexing and querying.

## 238: How do you stream tokens from a local model to a browser through your own backend?

Have the backend call the local server with streaming on and forward the pieces to the browser using Server-Sent Events:

```ts
// Next.js route handler
import { streamText } from "ai";
import { createOpenAICompatible } from "@ai-sdk/openai-compatible";

const local = createOpenAICompatible({
  name: "vllm",
  baseURL: process.env.LLM_BASE_URL!,
});

export async function POST(req: Request) {
  const { prompt } = await req.json();
  const result = streamText({ model: local("chat-model"), prompt });
  return result.toTextStreamResponse();
}
```

Don't let the browser call Ollama or vLLM directly: keep the model server private and do auth in your backend.

## 239: How do you handle a request the user cancelled?

When the client disconnects, your backend should abort the upstream request to the model server (for example with an `AbortController`). vLLM and `llama-server` stop generating when the connection closes, which frees the slot and KV cache for other users.

If you don't abort, the model keeps generating an answer nobody reads, which wastes GPU time and can make the queue grow.

## 240: What timeouts should you think about with local LLM servers?

- **Client timeout:** long answers and reasoning can take minutes. Use a long timeout or stream.
- **Proxy timeouts:** nginx, load balancers and API gateways often cut connections at 60 seconds.
- **Queue time:** under load, requests wait before starting; measure it separately.
- **Cold start:** the first request after a model loads (or after Ollama's `keep_alive` expires) can take extra seconds.

Set `max_tokens` too, so one request can't run forever.

## 241: How do you test code that calls a local model?

- **Unit tests:** mock the HTTP client or use a fake server, so tests are fast and don't need a GPU.
- **Integration tests:** run a tiny model (like a 0.5B-1B model in Ollama) in CI to check the wiring, streaming and parsing.
- **Quality tests (evals):** run a real model on a fixed test set and compare scores, separately from normal CI.

For deterministic tests use `temperature: 0` and a fixed seed, but check structure and meaning, not exact text.

## 242: How do you run a local model in GitHub Actions CI?

Install Ollama on the runner, pull a very small model and cache it:

```yaml
- name: Install Ollama
  run: curl -fsSL https://ollama.com/install.sh | sh
- name: Cache models
  uses: actions/cache@v4
  with:
    path: ~/.ollama/models
    key: ollama-qwen3-0.6b
- name: Pull model
  run: |
    ollama serve &
    sleep 5
    ollama pull qwen3:0.6b
- run: npm test
```

Normal runners have no GPU, so use tiny models and keep tests short. Note that the Linux install script may run the server as a service with a different models path; adjust the cache path to match.

## 243: What should you log for a self-hosted LLM service?

- Request ID, user or app, model name and version.
- Prompt and completion token counts.
- Queue time, TTFT, total time, tokens per second.
- Errors, timeouts, cancellations and finish reason (`stop` vs `length`).
- Server metrics: KV cache use, running and waiting requests, GPU memory and utilization.

Be careful about logging full prompts and responses: they may hold personal or secret data. Log them only where policy allows, with retention limits.

## 244: How do you monitor GPU health on an LLM server?

Use `nvidia-smi` for quick checks and NVIDIA DCGM (with `dcgm-exporter`) for Prometheus metrics: GPU utilization, memory use, temperature, power, clock speeds and errors like ECC and Xid events.

Watch for thermal throttling (lower clocks under load), memory errors and GPUs dropping off the bus. Combine these with the inference server's own metrics to see whether slowness comes from the hardware or from load.

## 245: What does finish_reason "length" mean, and how do you fix it?

It means the model stopped because it hit `max_tokens` (or the context limit), not because it finished. The answer is cut off.

Raise `max_tokens`, shorten the prompt, or raise the context limit. For reasoning models it's common: the thinking uses up the budget before the answer starts, so give them a bigger `max_tokens` or limit reasoning effort.

## 246: Why might a local model ignore your system prompt?

Common causes:

- The chat template is wrong or doesn't support a system role, so the system text is dropped or placed oddly.
- The context is too small and the system prompt was cut off (an Ollama classic).
- The model is a base model, not instruct.
- The model is small and just doesn't follow complex instructions well.

Check the raw prompt that gets sent (verbose logs or `/apply-template` in `llama-server`), then the context size, then try a stronger model.

## 247: How do you see the exact prompt the model receives after the chat template?

- `llama-server`: `POST /apply-template` with your messages returns the formatted prompt.
- vLLM: apply the template with the model's tokenizer in Python (`tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)`), or turn on request logging.
- Ollama: `OLLAMA_DEBUG=1` logs prompts, and `ollama show --modelfile` shows the template.

Seeing the real prompt is the fastest way to debug template, tool calling and system prompt problems.

## 248: Why do the same model and prompt give different answers in Ollama and vLLM?

Possible reasons:

- Different weights: Ollama often uses a 4-bit GGUF, vLLM a BF16 or FP8 model.
- Different default sampling settings (vLLM uses the model's `generation_config.json`).
- Different chat templates or system prompts.
- Different context limits.
- Different math kernels, so small numerical differences.

To compare fairly, use the same quant level where possible, set all sampling values explicitly and check the formatted prompts.

## 249: What is min_p, and why do many local users prefer it?

`min_p` drops tokens whose probability is less than a fraction of the top token's probability. With `min_p=0.05`, if the top token has 60% chance, anything under 3% is dropped.

It adapts to the model's confidence: when the model is sure, few options stay; when it's unsure, more stay. Many local users find it gives better results than `top_p` at higher temperatures. Ollama, llama.cpp and vLLM all support it.

## 250: How do you stop a local model from generating after a certain string?

Use stop sequences:

```json
{ "messages": [...], "stop": ["\n\n###", "</answer>"] }
```

Generation stops when one of them appears, and the stop text is usually not included in the output. In Ollama you set them in `options.stop` or with `PARAMETER stop` in a Modelfile. The model's own end-of-turn token is handled by the chat template, so you only add stops for your own formats.

## 251: How do you limit how long a reasoning model thinks?

It depends on the model and server:

- **Qwen3-style models:** turn thinking off per request with `chat_template_kwargs: {"enable_thinking": false}` in vLLM, or `think: false` in Ollama.
- **gpt-oss:** set reasoning effort (`low`, `medium`, `high`) with the `reasoning_effort` field or in the system prompt; in Ollama, `think` takes `"low"`, `"medium"` or `"high"` for gpt-oss.
- **llama-server:** `--reasoning-budget 0` turns thinking off for supported templates.

Less thinking means faster and cheaper answers but worse results on hard problems. Pick per task.

## 252: How do you serve a GGUF model in vLLM, and should you?

vLLM can load a single-file GGUF, but support is limited and slower than its main formats:

```bash
vllm serve ./model-Q4_K_M.gguf --tokenizer Qwen/Qwen3-8B
```

You usually have to pass the original model's tokenizer. For vLLM, prefer AWQ, GPTQ, FP8 or compressed-tensors models. Use GGUF in llama.cpp and Ollama, where it's the native format.

## 253: How do you convert a model for MLX on a Mac?

```bash
pip install mlx-lm
mlx_lm.convert --hf-path Qwen/Qwen3-8B -q --q-bits 4 --mlx-path ./qwen3-8b-mlx-4bit
mlx_lm.server --model ./qwen3-8b-mlx-4bit --port 8080
```

`-q` quantizes during conversion. `mlx_lm.server` starts an OpenAI-compatible server. Many models are already converted in the `mlx-community` organization on Hugging Face.

## 254: Is a Mac or an NVIDIA GPU better for local models?

It depends on what you need:

- **Mac (M-series Max/Ultra):** lots of unified memory (64-512 GB), quiet, low power. Great for running big models for one user. Prompt processing is slower than on NVIDIA.
- **NVIDIA GPU:** much faster prefill and better for many users at once, with full vLLM/SGLang support. VRAM per card is limited and expensive.

For personal use with big models, a Mac is often the simplest. For serving a team or production, NVIDIA (or AMD with ROCm) GPUs with vLLM are the standard.

## 255: Can you run local models on AMD GPUs?

Yes. Ollama supports many AMD GPUs through ROCm (and has a `rocm` Docker image), llama.cpp supports HIP/ROCm and Vulkan, and vLLM supports ROCm on AMD Instinct cards like MI300X.

Consumer Radeon support is better than it used to be but still depends on the exact card and ROCm version. Vulkan in llama.cpp is often the easiest way to use an AMD card without dealing with ROCm.

## 256: What are the steps to take a fine-tuned Hugging Face model to a GGUF in Ollama?

1. Merge the LoRA adapter into the base model and save it as safetensors.
2. Convert: `python convert_hf_to_gguf.py ./merged --outtype bf16 --outfile model-bf16.gguf`.
3. Quantize: `llama-quantize model-bf16.gguf model-Q4_K_M.gguf Q4_K_M`.
4. Write a Modelfile with `FROM ./model-Q4_K_M.gguf`, plus the template and stop tokens if needed.
5. `ollama create my-model -f Modelfile`, then test it against the unquantized model.

Ollama can also import a safetensors folder directly with `FROM ./merged` and quantize it with `ollama create --quantize q4_K_M`.

## 257: How do you quantize a model with Ollama itself?

Use `--quantize` (`-q`) with `ollama create`, starting from an FP16 or BF16 model:

```bash
ollama create my-model:q4 -f Modelfile --quantize q4_K_M
```

Where the Modelfile has `FROM ./my-model-f16.gguf` or a safetensors folder. Ollama supports a smaller set of quant types than `llama-quantize`, so for IQ types or imatrix quants use llama.cpp directly.

## 258: How do you choose between running one big model or several small specialized ones?

One big model is simpler and handles a wide range of tasks. Several small models (for example a 3B classifier, an embedding model and an 8B extractor) can be cheaper and faster when tasks are narrow and well defined.

Things to weigh: total memory (each loaded model needs its own space), routing logic, quality on each task and operations work. A common pattern is a small model for easy, frequent tasks and a bigger one only when needed.

## 259: What is model routing, and how does it help with local models?

Routing sends each request to the best model for it. Simple requests go to a small, fast local model; hard ones go to a bigger local model or to a hosted API.

The router can be rules (by endpoint, task type, prompt length) or a small classifier. Done well, it cuts cost and latency while keeping quality. LiteLLM and other gateways support routing and fallbacks.

## 260: How do you add a fallback when a local model server is down or overloaded?

Use a gateway or client logic that tries the local server first and, on errors, timeouts or 503s, retries on another replica or a hosted API.

Be careful with data: if the local model exists for privacy reasons, falling back to a hosted API may break that rule. In that case, fall back to another local replica or return a clear error.

## 261: What does the Ollama response field done_reason tell you?

It tells you why generation ended: `stop` (the model finished or hit a stop sequence), `length` (it hit `num_predict` or the context limit), or `load`/`unload` for requests that just loaded or unloaded a model.

If you see `length` often, raise `num_predict` or `num_ctx`.

## 262: How do you create a model in Ollama with a custom system prompt and share it with the team?

```text
# Modelfile
FROM qwen3:8b
SYSTEM """You review SQL queries. Point out bugs and slow patterns. Be brief."""
PARAMETER temperature 0.2
PARAMETER num_ctx 16384
```

```bash
ollama create myteam/sql-reviewer -f Modelfile
ollama push myteam/sql-reviewer
```

Pushing needs an ollama.com account with your public key added. For private sharing inside the company, keep the Modelfile in Git and have everyone run `ollama create`, or host your own registry-compatible store.

## 263: What happens when Ollama gets requests for two different models but only one fits in memory?

Ollama unloads the idle model to load the new one. If the first model is still working on requests, the new request waits until it's done, then the swap happens.

Constant swapping between big models is very slow, since each load can take seconds or more. Fix it with more memory, smaller quants, fewer models, or separate servers per model.

## 264: How does Ollama decide how much of a model to put on the GPU?

When loading, Ollama estimates the memory needed for the weights, the KV cache (from `num_ctx` and `OLLAMA_NUM_PARALLEL`) and buffers, then compares it to free VRAM. It puts as many layers on the GPU as fit, and the rest on the CPU.

The estimate isn't always right: if other processes grab VRAM after loading, or the estimate is low, you can get out-of-memory crashes. Setting `num_gpu` by hand or freeing GPU memory fixes it.

## 265: How do you serve a local model to a mobile or desktop app?

Two options:

- **On-device:** ship a small quantized model and run it with llama.cpp (it has Android and iOS examples), MLX on Apple devices, or platform tools like Core ML or ONNX Runtime. No server needed, works offline, but limited to small models.
- **Self-hosted server:** run vLLM or Ollama on your servers and call it from the app through your own API with auth.

On-device fits privacy-sensitive and offline features; a server fits bigger models and shared use.

## 266: How do you keep an air-gapped vLLM deployment working without Hugging Face access?

Download the model on a connected machine (`hf download Qwen/Qwen3-8B --local-dir ./qwen3-8b`), copy the folder in, and point vLLM at the local path:

```bash
HF_HUB_OFFLINE=1 vllm serve /models/qwen3-8b --served-model-name qwen3-8b
```

`HF_HUB_OFFLINE=1` stops it from trying the internet. Also bring the container image and Python packages in, and make sure the folder has the tokenizer and config files, not only weights.

## 267: How do you deal with gated models when deploying in CI/CD?

Accept the license on Hugging Face once with a service account, create a read-only token for it, and store it as a secret (`HF_TOKEN`) in CI and the cluster.

Better, download the model once into your own storage (an internal model registry, S3 bucket or persistent volume) and deploy from there. Then deploys don't depend on Hugging Face being up, and you know exactly which files you're running.

## 268: How do you compare the throughput of Ollama and vLLM fairly?

Use the same model and similar precision (for example GGUF Q8_0 vs FP8), the same prompts with realistic input and output lengths, the same GPU, and the same concurrency levels (1, 8, 32, ...).

Measure total tokens per second, TTFT and inter-token latency at each level. Usually they're close at one user, and vLLM pulls far ahead as concurrency grows thanks to its batching and memory management.

## 269: How do you measure inter-token latency, and why does it matter?

Inter-token latency (or time per output token) is the average time between tokens after the first one. You get it from the stream timestamps, or from `vllm bench serve`.

It decides how smooth streaming feels and how long a long answer takes. Under heavy load, batching more requests raises throughput but also raises inter-token latency, so set a target (for example under 50 ms) and tune batch size to stay under it.

## 270: What are percentiles like p50 and p99 in LLM latency, and why use them?

p50 is the median: half the requests are faster. p99 means 99% of requests are faster; the slowest 1% are slower.

Averages hide problems. A server can have a nice average TTFT while 1 in 100 users waits 20 seconds because of queueing or long prompts. Set goals on p95 or p99, and track them when you change flags or load.

## 271: What is RoPE scaling, and when does it matter?

Most models use RoPE (rotary position embeddings) to know token positions. Rope scaling (like YaRN) stretches these positions so the model can work beyond its original training length.

Some models ship with a native length (say 32K) and support longer context only when you turn on rope scaling in the config or server flags. Without it, they break down past the native length. Read the model card: it usually says when and how to enable it, and warns that it can slightly hurt short-context quality.

## 272: Why might a model perform worse at long context even if it technically supports it?

Supporting 128K tokens doesn't mean the model uses all of them well. Many models lose track of details in the middle of long inputs, and quality drops as context grows.

Quantizing the KV cache, aggressive rope scaling and heavy weight quantization can make it worse. For RAG, sending fewer, better chunks often beats stuffing the context. Test with your real document sizes.

## 273: How do you serve two different models on one GPU with vLLM?

vLLM runs one model per server process. To share a GPU, start two servers with smaller `--gpu-memory-utilization` values that add up to under 1:

```bash
vllm serve Qwen/Qwen3-8B --port 8000 --gpu-memory-utilization 0.45 --max-model-len 8192
vllm serve Qwen/Qwen3-Embedding-0.6B --port 8001 --gpu-memory-utilization 0.2
```

Each gets a smaller KV cache, so plan concurrency carefully. If the models are fine-tunes of the same base, LoRA adapters on one server are more efficient.

## 274: What is the difference between /v1/completions and /v1/chat/completions?

`/v1/completions` takes raw text and continues it. No chat template is applied, so you control the exact prompt format. It's used for base models, fill-in-the-middle and custom formats.

`/v1/chat/completions` takes messages and applies the model's chat template for you. It's what you want for instruct models, tool calling and almost all app work.

## 275: How does fill-in-the-middle (FIM) work with local code models?

FIM models are trained to fill a gap: you give the code before and after the cursor, and they generate what goes in between. It's how editor autocomplete works.

`llama-server` has an `/infill` endpoint with `input_prefix` and `input_suffix`. With other servers you build the FIM prompt with the model's special tokens and send it to `/v1/completions`. You need a model trained for FIM, like Qwen2.5-Coder.

## 276: How do you run a local model as a coding assistant in your editor?

Run a code model with Ollama, `llama-server` or vLLM, then point an editor extension at it. Many extensions (for example Continue, Cline and others) and editors let you set an OpenAI-compatible base URL or Ollama directly.

Use a small, fast FIM model for autocomplete and a bigger instruct model for chat and edits. Local models are weaker than the top hosted models at large agent tasks, but they're good for completion and code stays on your machine.

## 277: What are the security risks of exposing an Ollama or vLLM port to the internet?

- Anyone can use your GPUs for free (and people do scan for open Ollama servers).
- Ollama's API can pull, create and delete models, so attackers can fill your disk or remove models.
- Prompts and outputs can be read if traffic isn't encrypted.
- Old versions may have known vulnerabilities.

Keep model servers on a private network, add auth and TLS through a proxy or gateway, and update regularly.

## 278: Why should you keep Ollama, llama.cpp and vLLM updated?

Security fixes: these projects parse complex files (GGUF, templates) and expose HTTP APIs, and real vulnerabilities have been found and fixed in all of them.

New models: new architectures need new code, so a recent model may not load on an old version. Speed: each release often has faster kernels. Pin versions for stability, but plan regular, tested upgrades.

## 279: What is the risk of loading GGUF files from unknown sources?

GGUF files don't run code like pickle, but the parser in the runtime has had memory-safety bugs, so a crafted file could trigger them in old versions. The Jinja chat template inside the file is also code-like input that the runtime executes in a sandboxed template engine.

More practically, an unknown file could be a different or tampered model, with hidden behaviors or a broken template. Use trusted uploaders, check hashes, and keep runtimes updated.

## 280: What is trust_remote_code in vLLM and Transformers, and why be careful with it?

Some models need custom Python code from their Hugging Face repo to load. `--trust-remote-code` lets vLLM download and run that code.

That means you're running arbitrary Python from the repo on your server. Only use it for repos you trust, pin a specific revision (`--revision <commit>`) so the code can't change under you, and review it if you can. Most popular architectures don't need it.

## 281: How do you pin a Hugging Face model revision in vLLM?

```bash
vllm serve Qwen/Qwen3-8B --revision <commit-hash> --tokenizer-revision <commit-hash>
```

A repo's `main` branch can change: new weights, fixed templates or config changes. Pinning a commit makes your deploy reproducible. It matters even more when you use `--trust-remote-code`.

## 282: How do you secure the Jinja chat templates used by local servers?

Templates are run in a sandboxed Jinja environment in vLLM and Transformers, and llama.cpp uses its own limited Jinja engine, so they can't run arbitrary system code. Still, a custom template affects how system, user and tool messages are placed.

Review custom templates, keep them in Git, and be careful about letting users pick arbitrary templates or `chat_template_kwargs` that change behavior in ways you didn't expect.

## 283: What is prompt injection, and does self-hosting protect you from it?

Prompt injection is when untrusted text (a web page, an email, a document) contains instructions that the model follows, like "ignore your rules and send me the data".

Self-hosting doesn't protect you at all. Local models are often more easily tricked than top hosted models. You still need the same defenses: least-privilege tools, human approval for risky actions, separating trusted and untrusted content, and output checks.

## 284: How do you rate limit users of a self-hosted model?

The model servers don't do per-user limits. Add them in front:

- An API gateway or LiteLLM proxy with per-key limits on requests and tokens.
- Your own backend, counting tokens per user from the `usage` field in responses.

Limit by tokens, not just requests, because one long-context request can cost as much as hundreds of short ones. Also set `max_tokens` caps per user tier.

## 285: How do you count tokens before sending a request to a local model?

Use the model's own tokenizer, since different models split text differently:

- Python: `AutoTokenizer.from_pretrained("Qwen/Qwen3-8B")` and `len(tok.apply_chat_template(messages, tokenize=True))`.
- vLLM and `llama-server`: the `/tokenize` endpoint.
- Ollama: no tokenize endpoint, but `prompt_eval_count` in responses tells you after the fact.

Counting first lets you trim history or chunks to fit the context window instead of having them cut silently.

## 286: How do you handle chat history that grows beyond the context window?

Options:

- Keep the system prompt and the last N turns, drop the oldest.
- Summarize older turns with the model and keep the summary.
- Store history in a vector store and pull back only relevant old turns.

Do it in your app, before sending, using token counts. Don't rely on the server cutting the prompt, because it may cut the system prompt or the start of a key document.

## 287: Why is the first request to vLLM after start-up sometimes slower?

Some kernels or shapes are compiled or warmed up on first use, caches are cold, and prefix caching has nothing stored yet. CUDA graphs are captured at start-up for common batch sizes, but not every case is covered.

Send a few warm-up requests after deploy, before adding the instance to the load balancer. A readiness check that runs a tiny generation is better than only checking `/health`.

## 288: How do you choose max-model-len for a production vLLM deployment?

Look at your real prompt and output lengths (p99, not average), add margin, and set `--max-model-len` to that, not the model's maximum.

A smaller value means more KV cache blocks for concurrent requests. If a few use cases need long context, consider a separate deployment for them instead of making every replica support 128K.

## 289: How do GPU interconnects like NVLink affect multi-GPU serving?

Tensor parallelism sends data between GPUs on every layer for every token. With NVLink (hundreds of GB/s), that's cheap. Over PCIe it's much slower and can make 2 or 4 GPUs barely faster, or even slower, than expected.

On PCIe-only machines, consider pipeline parallelism, running separate replicas per GPU (data parallelism) with a smaller or more quantized model, or picking a model that fits on one GPU.

## 290: What is data parallelism in model serving?

You run several full copies of the model, each on its own GPU or group of GPUs, and spread requests across them. Throughput scales almost linearly with copies, and there's no communication between them during generation.

It only works if one copy fits on one GPU (or one tensor-parallel group). vLLM supports it in one server with `--data-parallel-size`, or you can just run several instances behind a load balancer.

## 291: How do you pick the number of GPUs for tensor parallelism?

Use the smallest number that fits the model plus enough KV cache for your load. More tensor-parallel GPUs lower latency a bit but add communication cost and give diminishing returns.

If one GPU can hold the model with room to spare, two separate replicas usually give more total throughput than one replica on two GPUs. Use tensor parallelism mainly when the model doesn't fit on one GPU.

## 292: What is the vLLM production stack or llm-d?

Both are open-source projects for running vLLM at scale on Kubernetes.

- **vLLM production stack:** Helm charts, a router that sends requests based on prefix cache and load, observability dashboards and KV cache offloading.
- **llm-d:** a Kubernetes-native framework (from Red Hat, Google, IBM and others) with smart scheduling, prefix-aware routing and disaggregated prefill/decode.

You use them when you have many replicas and need routing smarter than round-robin.

## 293: When would you use SGLang instead of vLLM?

SGLang is often faster for workloads with heavy prefix sharing, like agents and multi-turn chat with long shared contexts, thanks to RadixAttention. It's also a common choice for very large MoE models like DeepSeek V3 at scale, and it has strong structured output support.

vLLM has broader model and hardware support and a larger ecosystem. Many teams benchmark both on their model and traffic; the APIs are similar enough that switching is not hard.

## 294: When would you consider TensorRT-LLM?

TensorRT-LLM is NVIDIA's inference library, heavily tuned for NVIDIA GPUs. It can give the best performance on NVIDIA hardware, especially with FP8 and FP4 on Hopper and Blackwell, and it powers NVIDIA's NIM containers.

The cost is more complexity and NVIDIA lock-in. It makes sense for large, steady deployments where a few percent of performance saves real money. For most teams vLLM or SGLang are simpler.

## 295: How would you serve a local model to many internal teams with different needs?

A typical setup:

1. A gateway (like LiteLLM) with one endpoint, per-team keys, rate limits and usage tracking.
2. A few vLLM deployments behind it: a general chat model, a code model, an embedding model.
3. LoRA adapters for teams with special needs, on shared base models.
4. Shared observability: latency, errors, usage per team, GPU health.

Start small, measure real usage and add capacity where queues grow.

## 296: How do you move from an Ollama prototype to a vLLM production setup?

1. Find the original Hugging Face model behind your Ollama model, and pick a vLLM format (BF16, FP8 or AWQ).
2. Replace Ollama-specific API calls with OpenAI-compatible ones (ideally you used `/v1` from the start).
3. Set sampling values explicitly, since defaults differ.
4. Re-run your evals: GGUF Q4 vs FP8 can behave differently.
5. Set `--max-model-len`, tool and reasoning parsers, and API key.
6. Load test and add monitoring.

## 297: Why might tool calling work with a model in one tool but not another?

Tool calling depends on three things: the model being trained for it, the chat template formatting the tools the way the model expects, and the server parsing the model's output back into `tool_calls`.

Ollama, llama.cpp and vLLM each have their own templates and parsers. If one of them doesn't match the model's format (for example a missing `--tool-call-parser` in vLLM or a GGUF with an old template), calls come back as plain text. Check the server docs for that model family.

## 298: How do you choose a model for a local deployment?

1. Define the task and a small eval set first.
2. Shortlist models that fit your hardware and license needs.
3. Look at public benchmarks only as a first filter.
4. Run your eval on 2-4 candidates at the quant you'll actually deploy.
5. Weigh quality against speed, memory and context needs.

Re-check every few months; open models improve quickly.

## 299: What is the difference between dense and MoE models in terms of serving cost?

A dense model uses all its weights for each token. Memory and compute both grow with size.

An MoE model needs memory for all experts but computes only a few per token, so it's faster per token than a dense model of the same total size. On a single GPU or a Mac, memory is the limit, so MoE gives you "big model knowledge" at "small model speed" if you have the memory. At high batch sizes, different tokens use different experts, so you lose some of that advantage.

## 300: How do you document a self-hosted model deployment for your team?

Write down:

- Model name, source repo, exact revision or file hash, quant type and license.
- Runtime and version (Ollama, llama.cpp build, vLLM), with all flags and env vars.
- Hardware, context limits, expected throughput and latency.
- Default sampling settings and the chat template source.
- Eval results and the date they were run.
- How to deploy, roll back, and who's on call.

This makes upgrades and debugging much faster when the person who set it up isn't around.

# Advanced Questions (301-450)

## 301: How does PagedAttention work?

Before PagedAttention, servers reserved one large, contiguous chunk of memory per request for its maximum possible length. Most of it went unused, and memory got fragmented.

PagedAttention borrows the idea of virtual memory pages from operating systems. The KV cache is split into fixed-size blocks (16 tokens by default in vLLM), and each request has a block table that maps its logical token positions to physical blocks anywhere in GPU memory. Blocks are allocated only as the sequence grows, so waste is limited to the last, partly filled block. The attention kernel reads keys and values through the block table. The result is far more requests fitting in the same memory.

## 302: How does block sharing work in PagedAttention?

Because requests point to blocks through a table, two sequences can point to the same physical block. Each block has a reference count.

This is used for prefix caching (many requests share the blocks of a common system prompt) and for parallel sampling (`n > 1`), where several outputs share the prompt's blocks. When a shared block would need to change, the engine copies it first (copy-on-write). In practice, full blocks are never modified, so sharing is cheap.

## 303: What is continuous batching, and why is it better than static batching?

With static batching, the server waits to collect a batch, runs it until every request is done, then starts the next batch. Short requests sit idle waiting for long ones, and new requests wait for the whole batch.

Continuous (in-flight) batching makes scheduling decisions at every step. Finished requests leave right away, and new requests join on the next step. The GPU stays full and new requests start quickly. This one change gives several times more throughput for chat-like traffic, and every modern engine (vLLM, SGLang, TGI, llama.cpp server, TensorRT-LLM) uses it.

## 304: How does the vLLM scheduler decide what runs in each step?

In the current engine, the scheduler doesn't treat prefill and decode as separate phases. Each step it has a token budget (`--max-num-batched-tokens`) and a cap on sequences (`--max-num-seqs`). It gives each running request the tokens it needs, one for decoding requests and a chunk for requests still in prefill, and then admits waiting requests while budget and KV blocks remain.

If KV blocks run out, it preempts the lowest-priority running requests. The output is basically a map of request to number of tokens to process this step, which makes chunked prefill, prefix caching and speculative decoding fit into one simple model.

## 305: How is vLLM's current engine structured internally?

The current engine (introduced as V1, now the only engine since V0 was removed) splits work across processes:

- An **API server** process handles HTTP, tokenization and detokenization.
- An **engine core** process runs the scheduler and the KV cache manager in a busy loop.
- **Workers** (one per GPU) run the model.

They talk through fast inter-process messaging (ZeroMQ). Keeping CPU work like tokenization and HTTP off the engine loop means the GPU spends less time waiting for Python, which was a real bottleneck in the old design.

## 306: How does automatic prefix caching identify reusable blocks?

Each full KV block gets a hash computed from its tokens plus the hash of the block before it (and extra keys such as LoRA ID, multimodal inputs or a cache salt). So a hash identifies the whole prefix up to that block, not just its contents.

When a new request arrives, vLLM hashes its prompt block by block and looks up each hash. Every hit is a block it can reuse without compute. Unused cached blocks stay in a free queue and get evicted in LRU order only when memory is needed.

## 307: Why can prefix caching hit rate be low even when prompts look similar?

Hashes chain from the start, so one changed token early in the prompt makes every later block a miss. Common causes:

- A timestamp, request ID or user name at the top of the system prompt.
- Tools or documents listed in a different order each time.
- Different chat template output (for example a date the template inserts).
- Requests landing on different replicas, each with its own cache.

Fix it by putting stable content first and variable content last, sorting things deterministically, and routing related requests to the same replica.

## 308: What is disaggregated prefill/decode serving?

Prefill is compute-heavy and bursty; decode is memory-bandwidth-heavy and steady. On the same GPU they interfere: a big prefill makes everyone's streaming stutter.

Disaggregated serving runs them on separate instances. Prefill nodes process prompts and send the KV cache over a fast network (for example using NIXL with RDMA) to decode nodes, which stream the tokens. Each pool can be sized and tuned separately. vLLM supports this through KV connectors, and llm-d and SGLang build on it. It adds complexity and pays off mostly at large scale with long prompts.

## 309: What is KV cache offloading, and when is it useful?

Instead of dropping KV blocks when GPU memory is full, you move them to CPU RAM or even SSD and bring them back when needed. Tools like LMCache work with vLLM for this.

It's useful when many requests reuse long contexts that don't all fit in GPU memory: multi-turn chats with long history, RAG over the same documents, or agents that come back to a session after a pause. Copying back from CPU is much faster than recomputing a long prefill, but it needs fast PCIe and plenty of RAM.

## 310: What are CUDA graphs, and why does vLLM use them?

Launching each GPU kernel from Python has CPU overhead. During decode with small batches, a forward pass is many small kernels, and the launch overhead can be larger than the actual GPU work.

A CUDA graph records the whole sequence of kernels once and replays it with a single launch. vLLM captures graphs for a set of batch sizes at start-up and pads batches to the nearest captured size. This makes small-batch decoding much faster, at the cost of start-up time and some memory.

## 311: What role does torch.compile play in vLLM?

vLLM uses `torch.compile` to optimize the model's forward pass: fusing small operations together, removing overhead and making the code friendly to CUDA graph capture. It also lets vLLM add custom fusion passes, like fusing quantization into the previous operation.

Compiled artifacts are cached on disk, so later starts are faster if the cache directory persists. If compilation causes a bug for a model, you can lower the compilation level or use `--enforce-eager` while debugging.

## 312: Explain why decoding is memory-bound and prefill is compute-bound using arithmetic intensity.

Arithmetic intensity is FLOPs per byte read from memory. In decode with one request, each weight (2 bytes in BF16) is used for about 2 FLOPs (one multiply-add), so intensity is about 1. An H100 can do about 1,000 TFLOPS of BF16 but read only about 3.35 TB/s, so it needs ~300 FLOPs per byte to be compute-bound. Decode is far below that, so it's limited by memory.

In prefill, each weight is used for every token in the prompt, so intensity scales with prompt length and quickly becomes compute-bound. Batching many decode requests also raises intensity, which is why throughput grows with batch size until you hit compute limits or KV memory.

## 313: Why does throughput increase with batch size, and where does it stop?

In decode, reading the weights is the main cost, and it's the same whether you compute one token or 64. So adding requests to the batch adds tokens nearly for free, and throughput rises almost linearly at first.

It stops growing when the GPU becomes compute-bound, or more often when the KV cache runs out of space for more requests. KV reads also grow with batch size and context length, so long-context batches hit memory bandwidth limits sooner. Past that point, each request just gets slower.

## 314: How does speculative decoding guarantee the same output as the target model?

The draft proposes k tokens. The target model scores all of them in one forward pass. For greedy decoding, a draft token is accepted if it matches the target's top choice. For sampling, a rejection sampling rule accepts each token with probability `min(1, p_target / p_draft)` and, on the first rejection, samples a replacement from an adjusted distribution.

This math makes the output distribution exactly the same as sampling from the target alone. The speedup depends on the acceptance rate: if most guesses are accepted, you get several tokens per target pass; if few are, you waste compute.

## 315: What are the main speculative decoding methods in vLLM?

- **Draft model:** a small model from the same family proposes tokens.
- **N-gram (prompt lookup):** proposes tokens by finding matches in the prompt. Great for editing, summarizing and RAG, where output copies input.
- **EAGLE / EAGLE-3:** a small head trained on the target model's hidden states; high acceptance with little overhead.
- **MTP (multi-token prediction):** uses extra prediction heads some models ship with, like DeepSeek V3.

Example:

```bash
vllm serve Qwen/Qwen3-8B \
  --speculative-config '{"method": "ngram", "num_speculative_tokens": 5, "prompt_lookup_max": 4}'
```

## 316: When does speculative decoding hurt instead of help?

- At high batch sizes the GPU is already busy, so verifying extra tokens isn't free anymore and throughput can drop.
- When acceptance is low (creative text, high temperature, a poorly matched draft), most work is wasted.
- The draft model uses extra memory, which reduces KV cache space.

It's best for low-concurrency, latency-sensitive use. Measure acceptance rate and end-to-end speed at your real load before turning it on.

## 317: How do structured output engines constrain generation efficiently?

At each step, the grammar engine (xgrammar by default in vLLM, with alternatives such as guidance) works out which tokens are valid in the current grammar state and builds a bitmask over the vocabulary. Invalid tokens get their logits set to minus infinity before sampling.

Doing this naively for a 150K-token vocabulary at every step is slow. Modern engines precompile the grammar, cache masks for states where the valid set doesn't depend on context, and compute the mask on the CPU in parallel with the GPU forward pass, so overhead is usually small.

## 318: What problems can constrained decoding cause for output quality?

Forcing tokens can push the model off its natural path. If the schema forces a field the model wasn't going to write yet, or a format it tokenizes strangely, quality can drop. Very strict schemas sometimes lead to the model filling fields with nonsense rather than saying it doesn't know.

Help the model by describing the format in the prompt too, ordering fields so reasoning comes before conclusions, allowing `null` where data may be missing, and keeping schemas simple. With reasoning models, apply the constraint only to the final answer, not the thinking.

## 319: How does vLLM serve many LoRA adapters efficiently?

The base weights are shared. For each batch, requests can use different adapters. vLLM keeps active adapters in GPU memory (up to `--max-loras`) and uses special batched kernels (based on the Punica/SGMV idea) that apply each request's own low-rank matrices in one pass.

So one batch can mix requests for ten different adapters with little overhead. Adapters not in GPU memory are kept in CPU memory (`--max-cpu-loras`) and swapped in when needed. The cost is some extra latency, and a cap on rank (`--max-lora-rank`) that sets the memory reserved.

## 320: What is expert parallelism, and why does it matter for MoE models?

With tensor parallelism, every expert is split across all GPUs. With expert parallelism, whole experts are placed on different GPUs, and tokens are sent to the GPUs that hold their chosen experts (an all-to-all exchange).

For large MoE models like DeepSeek V3, expert parallelism scales better across many GPUs and nodes. vLLM enables it with `--enable-expert-parallel`, usually together with data parallelism for the attention layers. The main challenges are load balance (popular experts become hot spots) and network speed for the all-to-all.

## 321: What are Marlin kernels?

Marlin is a set of fast GPU kernels for multiplying 16-bit activations with 4-bit (and 8-bit) weights. They're designed to keep the GPU's memory bandwidth fully used while dequantizing weights on the fly, so 4-bit models get close to the ideal 4x speedup in memory-bound decoding.

vLLM uses Marlin-based kernels for GPTQ, AWQ and some other formats on supported NVIDIA GPUs, which is why AWQ models in vLLM usually run as `awq_marlin`.

## 322: Why don't 4-bit weight-only models speed up prefill or large batches much?

W4A16 kernels dequantize weights to 16 bits and do the math in 16 bits. At low batch sizes the win comes from reading 4x fewer bytes. Once the work becomes compute-bound (long prefills, big batches), the math is the bottleneck, and it's still 16-bit math plus extra dequantization work.

So at high load, a W4A16 model can be slower than an FP8 model, which does the math itself in 8 bits on supported GPUs. Choose formats based on your load: W4A16 for memory-limited, low-concurrency setups; FP8 or FP4 (W4A4/NVFP4) for high-throughput serving on new GPUs.

## 323: How does the attention backend choice affect vLLM performance?

vLLM picks an attention backend based on GPU, model and settings: FlashAttention versions, FlashInfer, Triton kernels, special MLA kernels for DeepSeek-style models, and others. They differ in support for features like FP8 KV cache, sliding window, and speed for different sequence lengths.

Usually the automatic choice is right. When debugging speed or accuracy issues on a specific GPU, checking which backend was selected in the logs and trying another (through vLLM's attention backend setting) is a valid step.

## 324: What is the interaction between prefill and decode, and how do you tune for it?

When a long prompt is being prefilled in the same step as other requests' decodes, those decodes wait for the whole step. Users who are already streaming see a pause.

Chunked prefill limits the damage by splitting prompts into chunks that fit `--max-num-batched-tokens`. Lower values keep inter-token latency steady but make TTFT for long prompts worse; higher values do the opposite. At large scale, disaggregated prefill removes the interference completely. Pick based on your latency targets.

## 325: How do you design for a strict p99 TTFT target?

TTFT = queue time + prefill time. To control it:

- Keep enough capacity that the queue stays short at peak (autoscale on waiting requests).
- Cap prompt length per tier, or route long prompts to separate replicas.
- Use prefix caching and stable prompt layouts to skip prefill work.
- Tune chunked prefill so new requests get scheduled quickly.
- Consider request priorities if your engine supports them (vLLM has a priority scheduling policy).

Measure TTFT broken into queue and prefill time, so you know which part to fix.

## 326: What is the "lost tokens" problem with naive memory allocation, and how big was it?

Before paged KV caches, systems pre-allocated memory for the maximum sequence length per request. The vLLM paper measured that existing systems used only about 20-40% of KV cache memory for actual token states; the rest was reserved but unused, or lost to fragmentation.

PagedAttention brought waste under about 4%, which directly translated into much larger batches and 2-4x higher throughput compared to systems of that time. It's a good example of an infrastructure fix that beat model-level tricks.

## 327: How does vLLM handle requests with n > 1 or best-of sampling?

The prompt is prefilled once, and its KV blocks are shared between all n output sequences. Each sequence then gets its own blocks as it generates.

This makes multiple samples much cheaper than sending n separate requests, especially with long prompts. It's useful for self-consistency (sample several answers and vote), generating candidates for reranking, or creating training data.

## 328: How would you serve a model whose weights don't fit in one node?

Combine parallelism types:

- Tensor parallel within a node (fast NVLink), for example TP=8.
- Pipeline parallel across nodes (`--pipeline-parallel-size 2`), or expert parallel for MoE.
- A cluster runtime (vLLM uses Ray or its own multi-node launch) to coordinate.

Fast networking between nodes (InfiniBand or RoCE) is essential. Before going multi-node, check whether a more aggressive quant (FP8, FP4) would make it fit in one node; that's usually simpler and faster.

## 329: What is the trade-off between latency and cost when choosing GPU count per replica?

More GPUs per replica (higher tensor parallel) lowers per-request latency a bit and fits bigger contexts, but adds communication overhead, so throughput per GPU drops. Fewer GPUs per replica (more replicas) gives the best throughput per dollar but higher latency per request.

For interactive chat with strict latency targets, you might pay for TP=2 or 4. For batch jobs, use the smallest setup that fits the model and run many replicas.

## 330: How do you serve a batch job of millions of prompts most cheaply?

- Use vLLM's offline `LLM` class (or a batch API mode) instead of HTTP, so the engine can batch freely.
- Sort or group prompts by shared prefix to maximize prefix cache hits.
- Use the most aggressive quant that passes quality checks, and FP8 KV cache.
- Max out `--max-num-seqs` and batched tokens; latency doesn't matter here.
- Use spot or preemptible GPUs with checkpointing of finished results.
- Pick the smallest model that meets quality.

## 331: How is a Q4_0 GGUF block laid out?

Q4_0 groups weights into blocks of 32. Each block stores one FP16 scale (2 bytes) and 32 four-bit values (16 bytes), for 18 bytes per 32 weights, which is 4.5 bits per weight.

To dequantize, each 4-bit value (0-15) is shifted to the range -8..7 and multiplied by the scale. It's symmetric with no offset. Simple formats like this are fast but lose more quality than K-quants, because one scale must cover 32 values that may vary a lot.

## 332: How do K-quants differ from the older quant types?

K-quants use super-blocks of 256 weights split into smaller sub-blocks (for example 8 sub-blocks of 32 for Q4_K). Each sub-block has its own scale (and minimum, for some types), but those scales are themselves quantized to 6 bits, with one FP16 scale for the whole super-block.

This two-level scheme gives fine-grained scaling (better quality) without paying 16 bits per sub-block scale. Q4_K comes to about 4.5 bits per weight. The `_S/_M/_L` variants then decide which tensors get a higher type, which is why Q4_K_M averages about 4.9 bpw.

## 333: Why does Q4_K_M use higher precision for some tensors?

Not all tensors are equally sensitive. In Q4_K_M, llama.cpp uses Q6_K for some of the most sensitive weights, such as parts of the attention value projection and some of the feed-forward down projection layers, and Q4_K for the rest.

These tensors have a large effect on output quality relative to their size. Spending a few more bits there gives a big quality gain for a small size increase. Tools like Unsloth's dynamic quants push this further by choosing per-layer precision based on measured sensitivity.

## 334: What is the difference between symmetric and asymmetric quantization?

Symmetric quantization maps values around zero: `w ≈ scale × q`, with q in a range like -8..7. It needs only a scale.

Asymmetric quantization adds a zero point (or minimum): `w ≈ scale × q + min`. It can fit ranges that aren't centered on zero, which uses the available levels better, at the cost of storing an extra value per group. GGUF has both kinds (Q4_0 symmetric, Q4_1 and Q4_K with minimums); AWQ usually uses asymmetric with zero points, while GPTQ can use either.

## 335: What is group size in AWQ and GPTQ, and how does it affect quality?

Group size is how many weights share one scale (and zero point). A common value is 128. Smaller groups (like 32 or 64) follow local changes in the weights better, so quality is higher, but they store more scales, so the model is a little bigger and kernels may be a bit slower.

Per-channel quantization (one scale per output row) is the extreme case of large groups. Most 4-bit models on Hugging Face use group size 128 as a balance.

## 336: Explain how AWQ decides which weights to protect.

AWQ observes that about 1% of weight channels matter much more than others, and those are the ones connected to large activation values. Instead of keeping them in higher precision (which is hard for kernels), AWQ multiplies those weight channels by a scale factor before quantization and divides the matching activations by the same factor.

The math stays the same, but the important weights now use more of the quantization range, so they lose less precision. AWQ searches per layer for the scale that minimizes the output error on calibration data. The activation division is folded into the previous operation, so there's no runtime cost.

## 337: Explain how GPTQ works at a high level.

GPTQ quantizes a layer's weights one column at a time. After rounding each column, it adjusts the not-yet-quantized columns to compensate for the error just added, using second-order information: an approximation of the Hessian built from calibration activations.

This way the layer's output stays close to the original even though each weight is rounded. Options like act-order (quantizing columns in order of activation size) and a damping factor for numerical stability improve results. It's based on the earlier Optimal Brain Quantization idea, made fast enough for billion-parameter models.

## 338: AWQ or GPTQ: how do they compare in practice?

Both give 4-bit W4A16 models with similar quality on most models; which wins depends on the model and calibration. AWQ is faster to run (no Hessian updates) and was reported to generalize slightly better across domains because it relies less on the calibration set. GPTQ with act-order and good data can be as good or better.

In vLLM both run on fast Marlin kernels, so speed is similar. In practice, people pick whichever has a good published version of their model, or test both with their own eval.

## 339: What problem does SmoothQuant solve?

To use INT8 math for activations (W8A8), you have to quantize activations, but LLM activations have outlier channels with values much larger than the rest. One scale for the whole tensor then wastes most of the range on outliers.

SmoothQuant moves the difficulty from activations to weights: it divides activation channels by a smoothing factor and multiplies the matching weight channels by it. Activations become easier to quantize, weights become a bit harder but are still fine. It's offline, math-equivalent, and available in llm-compressor.

## 340: What are activation outliers, and why do they make quantization hard?

In large transformers, a few hidden dimensions have values 10-100 times larger than typical, consistently across tokens. They seem to be important for the model's behavior, so you can't just clip them.

If you quantize a tensor with one scale, the outliers force a large scale and most normal values get rounded to a few levels, losing precision. Fixes include per-token or per-channel scales, keeping outlier channels in high precision, SmoothQuant-style scaling, and rotation methods (like QuaRot or SpinQuant) that spread outliers across dimensions.

## 341: What are the two FP8 formats, and which is used for inference?

- **E4M3:** 4 exponent bits, 3 mantissa bits. More precision, smaller range (max about 448).
- **E5M2:** 5 exponent bits, 2 mantissa bits. Larger range, less precision.

Inference usually uses E4M3 for weights and activations, because precision matters more and scales handle range. E5M2 is more common for gradients in training, where range matters more. You'll see E4M3 in FP8 model configs and in vLLM's FP8 KV cache options.

## 342: What is the difference between per-tensor, per-channel and per-token scaling?

- **Per-tensor:** one scale for the whole tensor. Cheapest, but outliers hurt everything.
- **Per-channel:** one scale per output channel of a weight matrix. Standard for weights.
- **Per-token:** one scale per token row of the activations, computed at runtime. Handles tokens with unusual magnitudes.

A common FP8 recipe is per-channel weights with dynamic per-token activations (`FP8_DYNAMIC`), which keeps quality very close to BF16 without calibration.

## 343: What is the difference between static and dynamic activation quantization?

Static quantization computes activation scales once from calibration data and uses them for every request. It's faster at runtime but can clip if real inputs differ from calibration.

Dynamic quantization computes scales on the fly for each token or tensor. It costs a little extra compute but adapts to each input and needs no calibration. For FP8, dynamic per-token scales are a common default because they're robust.

## 344: How do NVFP4 and MXFP4 store values?

Both store each value as a 4-bit float (E2M1: 1 sign, 2 exponent, 1 mantissa bit), with a shared scale per block.

- **MXFP4:** blocks of 32 values, with an 8-bit power-of-two scale (E8M0).
- **NVFP4:** blocks of 16 values, with an FP8 (E4M3) scale per block plus one FP32 scale per tensor.

NVFP4's smaller blocks and non-power-of-two scales fit the data more closely, which usually means better accuracy. Blackwell GPUs run FP4 matrix math in hardware, so these formats speed up compute, not only memory.

## 345: Why does a 4-bit quant sometimes break JSON or tool calls even if chat seems fine?

Structured output relies on precise tokens: exact field names, quotes, brackets and the special tokens that start a tool call. Small shifts in token probabilities from quantization can make the model pick a slightly different token at one critical point, and the whole output becomes invalid.

Normal chat hides this because many token choices are "good enough". Test structured tasks specifically on the quant you deploy, use constrained decoding for JSON, and step up a quant level (Q5/Q6, or FP8) if format errors rise.

## 346: How can a bad imatrix or calibration set hurt a quant?

The calibration data decides which weights are treated as important. If it's narrow (only English chat), the quant may keep chat quality and hurt code, math or other languages.

There's also overfitting: a quant tuned too much on one dataset looks great on matching benchmarks and worse elsewhere. Good calibration sets are diverse and match real use. For specialized deployments, adding your own domain text to the calibration data can noticeably help.

## 347: How do you measure quantization damage more reliably than perplexity?

- **KL divergence** against the full-precision model's token probabilities, on varied text.
- **Top-token agreement:** how often the quant picks the same top token as the original.
- **Task evals** on your use case: accuracy, JSON validity, tool call success.
- **Long-generation tests:** small errors can compound over long outputs.

`llama-perplexity --kl-divergence` reports KLD and top-token agreement for GGUF quants against saved base logits. For GPU formats, compare with lm-evaluation-harness and your own test set.

## 348: Why might quantizing an MoE model need special care?

- The router (gate) decides which experts run. Errors there send tokens to the wrong experts, so it's usually kept in high precision.
- Some experts are rarely used, so calibration data may barely activate them; their quantization is poorly informed.
- Expert weights make up most of the parameters, so quantizing them gives most of the size saving, while shared attention layers are small and can stay at higher precision.

gpt-oss follows exactly this pattern: MXFP4 for expert weights and BF16 for everything else.

## 349: What are Unsloth dynamic quants and similar per-layer approaches?

Instead of one quant type for most layers, these methods measure each layer's sensitivity and choose a different bit width per layer or tensor: very low bits where it's safe, higher bits where it hurts. They also often use carefully built calibration data.

The result is quants that keep more quality at the same average size, especially at very low bits (1.5-3 bpw), which made it possible to run huge models like DeepSeek R1 on single machines. They're still GGUF files, so they run in llama.cpp and Ollama.

## 350: How does KV cache quantization affect quality differently from weight quantization?

Weight errors are fixed and the same for every request. KV cache errors depend on the input and add up over the context, because every new token attends to all the quantized past keys and values.

Keys are usually more sensitive than values, since errors in keys change which tokens get attention. So long-context and retrieval-heavy tasks (finding a detail deep in a document) suffer first. 8-bit KV cache is usually safe; 4-bit KV needs testing on long-context tasks.

## 351: Why does llama.cpp repack Q4_0 weights on some CPUs?

ARM and x86 CPUs have SIMD instructions that can multiply several rows at once if the data is arranged in a certain way. llama.cpp can rearrange (repack) Q4_0 and some other types at load time into interleaved layouts that match these instructions.

On ARM chips this can make Q4_0 faster than K-quants of similar size. That's why some GGUF uploads for phones and ARM servers recommend Q4_0 despite its slightly lower quality.

## 352: What is the GGUF file layout?

1. **Header:** the magic bytes `GGUF`, the format version, the tensor count and the metadata count.
2. **Metadata:** key-value pairs like `general.architecture`, context length, tokenizer vocab and merges, the chat template and quantization info.
3. **Tensor info:** for each tensor, its name, shape, type and offset in the data section.
4. **Padding** to an alignment boundary (32 bytes by default).
5. **Tensor data:** the raw (often quantized) weights.

Because tensors are aligned at known offsets, the file can be memory-mapped and used directly without parsing into new buffers.

## 353: Why is having the tokenizer inside the GGUF file important?

The model only works with the exact tokenizer it was trained with. Storing the vocab, merges, special tokens and pre-tokenizer type in the GGUF means one file is all you need, with no separate tokenizer files that could mismatch.

The flip side: if the converter got the tokenizer wrong (this has happened with new models, for example a wrong pre-tokenizer regex), every GGUF made from it is subtly broken. Fixes usually require re-converting, which is why uploaders sometimes re-upload GGUFs shortly after a model's release.

## 354: How does memory mapping interact with partial GPU offload in llama.cpp?

With mmap, the GGUF file is mapped into the process's address space. Tensors for GPU layers are copied into VRAM at load time; tensors for CPU layers are read straight from the mapped pages, which live in the OS page cache.

So the CPU part doesn't take "process memory" in the normal sense; the OS can drop and reload those pages. That's fast when you have enough RAM, but if memory is tight, pages get evicted and reloaded from disk during inference, which is very slow. `--mlock` prevents that; `--no-mmap` loads everything into normal memory.

## 355: How does the GGML backend scheduler split work across devices?

llama.cpp builds a compute graph for each forward pass. The backend scheduler assigns each operation to a device (GPU, CPU, other) based on where its weights live and what each backend supports, then splits the graph into chunks per device and copies tensors between them at the boundaries.

The number of splits matters: every boundary is a data transfer. That's why partial offload is slow, and why offloading only MoE experts (whole blocks of work on the CPU) can be faster than offloading random layers.

## 356: What do -b and -ub mean in llama.cpp?

`-b` (`--batch-size`, default 2048) is the logical batch: the most tokens the server will take for processing in one call. `-ub` (`--ubatch-size`, default 512) is the physical micro-batch actually sent to the backend at once.

Bigger `-ub` makes prompt processing faster on GPUs (better use of compute) but needs more temporary memory. If you're short on VRAM, lowering `-ub` frees memory; if prefill is slow and you have room, raising it to 1024 or 2048 can help.

## 357: What is context shifting in llama.cpp?

When a conversation fills the context, context shifting drops the oldest tokens (after a protected start of `--keep` tokens) and shifts the remaining KV cache positions, so generation can continue without reprocessing everything.

It works because of how RoPE positions can be adjusted, but the model then sees a conversation with a hole in it, which can confuse it. In recent builds it's off by default, so the server returns an error when the context is full; you turn it on with `--context-shift` if you prefer endless but slightly worse generation.

## 358: How does llama.cpp's sampler chain work?

After the model produces logits, llama.cpp runs a configurable chain of samplers in order: penalties (repeat, presence, frequency), DRY, top-k, typical, top-p, min-p, XTC, temperature, and finally the random pick from what's left.

The order matters: temperature after the cut-off filters behaves differently from before them. You can change the chain with `--samplers`. Grammar constraints are applied too, so only valid tokens can be picked. Knowing this helps when the same settings give different results in different tools.

## 359: How can llama.cpp run one model across several machines?

With the RPC backend. On each helper machine you run `rpc-server`, which offers its GPU or CPU as a remote backend. On the main machine you pass the helpers:

```bash
llama-server -m big-model.gguf -ngl 99 --rpc 192.168.1.10:50052,192.168.1.11:50052
```

Layers are spread across local and remote devices. It's handy for pooling home machines to run a model none of them could alone, but network speed limits performance, and the RPC protocol has no authentication, so use it only on a trusted network.

## 360: What is NUMA, and why does it matter for CPU inference?

On servers with two or more CPU sockets, each socket has its own local memory. Accessing the other socket's memory is slower (Non-Uniform Memory Access).

CPU inference is memory-bandwidth-bound, so threads reading weights from the wrong node can lose a lot of speed. llama.cpp has `--numa distribute` and `--numa isolate` to place threads and memory sensibly. Running one instance per socket with its own model copy is often the fastest.

## 361: How does Ollama's scheduler estimate memory, and why can it be wrong?

Before loading, Ollama computes the memory needed for weights per layer, the KV cache for `num_ctx × OLLAMA_NUM_PARALLEL`, the compute graph buffers and backend overhead, then fits as many layers as possible on available GPUs.

It can be wrong because graph buffer sizes depend on the model architecture and batch size, vision projectors add memory, drivers report free memory differently, and other processes may grab VRAM after the check. Over-estimates leave layers on the CPU needlessly; under-estimates cause out-of-memory crashes. Newer engine versions measure more precisely, but `num_gpu` stays the manual override.

## 362: How does Ollama store models internally?

Ollama uses a layout similar to container registries. A model has a manifest (JSON) listing its layers: the weights, template, system prompt, parameters, license and so on. Each layer is a blob named by its SHA-256 digest in the `blobs` folder.

Models that share layers (like the same weights with different system prompts) store them once. `ollama create` from a Modelfile only adds small new layers on top of the existing weights blob. Pull and push work like container image pulls, layer by layer.

## 363: How does Ollama translate chat templates?

Model repos use Jinja templates, but Ollama's templates use Go's `text/template`. For models in the Ollama library, maintainers write the Go templates. For imported GGUFs, Ollama tries to detect a known template from the GGUF's Jinja template and map it to a built-in Go version.

When detection fails, you get a generic template and odd behavior, especially for tool calling. That's why imported models sometimes need a hand-written `TEMPLATE` with the right tool and stop handling, and why the same GGUF can behave better in `llama-server` with `--jinja`.

## 364: What are Ollama's runner processes?

The Ollama server doesn't run inference itself. For each loaded model, it starts a separate runner subprocess that loads the weights and does the computation, and the server talks to it over a local HTTP connection.

Over time Ollama has had two kinds of runners: one built on llama.cpp's code and its own newer engine built on GGML, which handles many newer model families. Separate processes mean a crash in one model doesn't take down the server, and memory is freed fully when a model unloads.

## 365: Why might parallel requests in Ollama give lower quality or errors with long prompts?

With `OLLAMA_NUM_PARALLEL` above 1, the total context is shared or multiplied across parallel slots, depending on version and settings. If you didn't raise memory accordingly, Ollama may lower per-slot context or push layers to the CPU.

The result can be truncated prompts (bad answers with no error) or slow responses. Check effective context with `ollama ps` and response stats, and set `num_ctx`, parallel count and model size together.

## 366: How would you isolate users who share a vLLM server with prefix caching?

Prefix caching can leak information through timing: if an attacker's guess at another user's prompt prefix gets a cache hit, it returns faster. In multi-tenant setups this is a real side channel.

vLLM supports a `cache_salt` request field: requests with different salts never share cached blocks. Set the salt per tenant (or per user) in your gateway so tenants can't probe each other, while each tenant still benefits from its own repeated prefixes. Alternatively, run separate deployments for high-sensitivity tenants.

## 367: What other side channels or data leaks exist in shared LLM serving?

- **Timing:** TTFT and per-token speed reveal cache hits or the load other users create.
- **Logs and metrics:** prompts in debug logs, `/slots` in `llama-server`, request logging in vLLM.
- **Error messages** that echo parts of inputs.
- **GPU memory:** another process on the same GPU could, in theory, read leftover memory if isolation is weak.

Turn off debug endpoints in production, use per-tenant cache salts, scrub logs and isolate high-risk tenants with dedicated GPUs or MIG partitions.

## 368: How can GPUs be shared between workloads safely?

- **MIG (Multi-Instance GPU)** on A100/H100-class cards splits one GPU into up to 7 isolated instances with their own memory and compute. Strong isolation, fixed sizes.
- **MPS (Multi-Process Service)** lets several processes run kernels at the same time on one GPU, with weaker isolation.
- **Time slicing** in Kubernetes switches between processes; no memory isolation and unpredictable latency.

For untrusted tenants, MIG or whole GPUs. For your own trusted services, MPS or separate memory budgets (like two vLLM instances with lower `--gpu-memory-utilization`) can be enough.

## 369: How can a user cause a denial of service on a self-hosted model, and how do you prevent it?

- Very long prompts that take seconds of prefill each.
- Huge `max_tokens` or reasoning that runs for minutes.
- Many parallel requests filling the KV cache and queue.
- Complex JSON schemas or grammars that are slow to compile.
- Requests with `n` or `best_of` set high.

Defend with a gateway: per-user rate and token limits, caps on prompt length, `max_tokens` and `n`, request timeouts, schema size limits and separate queues or priorities for different tiers.

## 370: How do you handle supply-chain security for model weights?

- Download only from trusted publishers and known uploaders.
- Prefer safetensors and GGUF; avoid pickle formats.
- Record and verify file hashes; mirror approved models to internal storage.
- Pin repo revisions, and never auto-pull `latest` in production.
- Avoid `trust_remote_code`, or review and pin the code.
- Keep a model inventory (like an SBOM): source, hash, license, who approved it.

A tampered model can contain hidden behaviors (backdoors) that are almost impossible to find by inspection, so provenance matters.

## 371: What is a model backdoor, and can quantization hide or create one?

A backdoor is behavior trained into a model that only shows up for a specific trigger, like a phrase that makes it output harmful code or leak data. It looks normal otherwise.

Research has shown attacks where a model behaves normally in full precision but the backdoor appears only after quantization, by exploiting the rounding. That's a reason to quantize trusted models yourself or use trusted quantizers, and to run safety and behavior evals on the exact quantized file you deploy.

## 372: Do self-hosted open models need extra safety layers?

Often yes. Open models vary a lot in how well they refuse harmful requests, fine-tunes can remove safety training, and you don't get a provider's extra filtering.

Common additions: a guard model (like Llama Guard or similar open classifiers) on inputs and outputs, rules or classifiers for your specific policies, PII detection, and red-team testing before launch. Run the guard locally too, so data still doesn't leave your network.

## 373: How do you meet data residency and compliance requirements with self-hosted models?

Self-hosting helps because you choose where data is processed, but you still have to prove it:

- Run models and logs in approved regions or on-premises.
- Make sure no component phones home (turn off telemetry, cloud features like `OLLAMA_NO_CLOUD=1`, and external downloads at runtime).
- Control and audit who can see prompts and outputs.
- Set retention for logs and caches.
- Document model sources and licenses.

Network egress rules that block the model servers from the internet are the strongest proof.

## 374: How do licenses of open-weight models affect a commercial product?

Check:

- Is commercial use allowed?
- Are there user count or revenue limits (Llama licenses have a large-company clause)?
- Are there acceptable use policies you must enforce on your users?
- Do you have to show attribution or use a name like "Built with ..."?
- Can you use outputs to train other models?
- Do fine-tunes and quants carry the same license?

Apache 2.0 and MIT models are the simplest. Keep license info in your model inventory and have legal review custom licenses.

## 375: How would you design isolation for a multi-tenant SaaS that offers per-customer fine-tuned models?

- One shared base model on vLLM with per-customer LoRA adapters, selected by the gateway from the authenticated tenant (never from user input).
- Per-tenant `cache_salt` so prefix cache isn't shared across tenants.
- Adapter files stored per tenant with access controls; dynamic loading endpoint not exposed publicly.
- Per-tenant rate limits and quotas.
- Logs tagged by tenant, with retention per contract.
- Dedicated deployments for customers whose contracts require hardware isolation.

## 376: How would you estimate the hardware for a chat product with 1,000 concurrent users?

"Concurrent users" isn't concurrent requests. Work it out step by step:

1. Measure or guess the request rate: say each active user sends a message every 60 seconds, so about 17 requests per second.
2. Average output 400 tokens, input 2,000 tokens (with history).
3. Needed decode throughput: 17 × 400 ≈ 6,800 output tokens/s, plus prefill of 34,000 input tokens/s (less with prefix caching).
4. Benchmark one replica of your model and quant at your latency target (say 30 tokens/s per user) to get its max throughput.
5. Replicas = needed throughput ÷ per-replica throughput, plus 30-50% headroom for peaks and failures.

Then load test, because real traffic is burstier than averages.

## 377: How does Little's law help with LLM capacity planning?

Little's law: average number of requests in the system = arrival rate × average time in the system.

If 10 requests arrive per second and each takes 8 seconds (queue plus generation), about 80 are in flight at any moment. Your servers must handle 80 concurrent sequences in KV cache and batch slots, or the queue will grow without limit. It's a simple way to turn traffic numbers into `--max-num-seqs` and memory needs.

## 378: After upgrading llama.cpp, a model starts producing garbage. What do you check?

1. Read the release notes for changes to the model's architecture code, tokenizer handling or defaults (like `--jinja` or context shift).
2. Check that the GGUF wasn't made by an older converter with a known bug that the new code now handles differently; re-download or re-convert.
3. Compare with the previous build on the same prompt to confirm it's the upgrade.
4. Try different backends or flags (flash attention off, a different `-ub`) to find a kernel bug.
5. Look for an open GitHub issue for that model; regressions get reported fast.

Pin builds in production and upgrade only after your eval passes.

## 379: vLLM preallocates memory, so why can it still run out of memory under load?

The KV cache is preallocated, but other memory isn't fully fixed:

- Activation memory for very large batches or very long chunks.
- Sampling extras like many `top_logprobs`, large `n` or big vocabularies.
- Multimodal inputs bigger than what profiling assumed.
- Other processes on the same GPU, or memory fragmentation in PyTorch.
- LoRA adapters loaded beyond what was planned.

Leave headroom (`--gpu-memory-utilization` below the max), cap request parameters at the gateway, and set multimodal limits explicitly.

## 380: Users report TTFT spikes every few minutes. How do you investigate?

Correlate the spikes with other metrics:

- Waiting queue length: bursts of traffic or a batch job sharing the server.
- Prompt lengths: a few huge prompts blocking prefill (tune chunked prefill or route them elsewhere).
- Prefix cache hit rate dropping: cache eviction, or a deploy that changed the prompt.
- Model reloads: Ollama `keep_alive` expiring, or autoscaler adding cold replicas that get traffic too early.
- GPU throttling or other processes.

Break TTFT into queue time and prefill time in your traces to narrow it down.

## 381: Two replicas of the same deployment give different outputs for the same request at temperature 0. Why?

Even greedy decoding can differ because the floating-point math depends on batch composition. A request batched with others uses different kernel paths and reduction orders than one running alone, so logits differ slightly, and a near-tie between two tokens can flip. After one different token, the rest of the answer differs.

Other causes: different versions, GPUs or flags between replicas, or prefix cache hits on one replica. Make replicas identical, and don't design features that need bit-exact outputs. Newer vLLM versions have an experimental batch-invariant mode for cases where you need determinism, at a speed cost.

## 382: How would you roll out a new model version with zero downtime?

1. Deploy the new model as a separate deployment with its own name or version.
2. Warm it up and run your eval suite against it.
3. Shift a small part of traffic (canary) through the gateway and compare metrics: errors, latency, user feedback, format failures.
4. Increase traffic step by step, keeping the old deployment ready for rollback.
5. Remove the old one after a stable period.

Never swap the weights under a running name without versioning; you lose the ability to compare and roll back.

## 383: How do you A/B test a cheaper quant against the current model?

Route a random percentage of traffic (by user, so each user sees one variant) to the new quant. Track task metrics: success rates, JSON validity, tool call errors, thumbs up/down, retries, conversation length, and latency and cost per request.

Also run offline evals on the same prompts with both models, and LLM-as-judge or human review on a sample. Decide the success criteria before you start, so you don't talk yourself into a cheaper but worse option.

## 384: Should a company rent cloud GPUs or buy its own for self-hosting?

**Rent** when demand is uncertain or bursty, you need to start fast, or you want to try different GPU types. You pay more per hour but have no upfront cost.

**Buy** when you have steady, high usage for years, space and power, and people to run the hardware. Break-even is often 1-2 years of high use compared to on-demand prices, less compared to committed cloud pricing.

Many teams start renting, measure real usage, then buy for the steady base load and rent for peaks.

## 385: How do you calculate cost per million tokens for a self-hosted model?

`cost per 1M tokens = (GPU cost per hour × number of GPUs) ÷ (tokens per hour actually served) × 1,000,000`

Example: 2 GPUs at $2.50/h = $5/h. If you serve an average of 1,500 output tokens/s, that's 5.4M tokens per hour, so about $0.93 per million output tokens. At 20% average use, the real cost is about 5 times that. Add engineering time, storage and networking, and separate input and output tokens to compare with API prices fairly.

## 386: How would you run an LLM on an edge device like a Jetson or a Raspberry Pi?

- Pick a small model (0.5B-4B) and a quant that fits RAM, often Q4_0 or Q4_K_M.
- Use llama.cpp (CUDA on Jetson, CPU with ARM optimizations on a Pi) or Ollama.
- Keep context short to save memory, and turn off unneeded features.
- Watch power and heat: throttling under sustained load is common.
- Plan updates: how to ship new models to devices safely.

Expect a few tokens per second on a Pi and much more on a Jetson Orin. Narrow tasks (commands, classification, short summaries) work best.

## 387: How would you design a hybrid setup that uses local models but can burst to a hosted API?

Put a gateway in front that knows about both. Normal traffic goes to local replicas. When queue time or error rates pass a threshold, extra requests go to a hosted model with similar abilities.

Mark data by sensitivity: requests that must stay private are never sent out, even under load; they queue or get a "busy" error. Keep prompts compatible across both targets and evaluate both, since outputs will differ.

## 388: How would you summarize long documents with a model that has a small context window?

Use map-reduce: split the document into chunks that fit with room for instructions, summarize each chunk, then summarize the summaries (repeat if needed). Or use a "refine" approach: keep a running summary and update it chunk by chunk.

Map-reduce parallelizes well on vLLM. Keep overlap between chunks so you don't cut ideas in half, and include the document title and section headings in each chunk prompt for context.

## 389: How would you design a private coding assistant for 200 developers?

- **Models:** a small FIM model for autocomplete (very low latency), a stronger instruct code model for chat and edits, maybe an embedding model for code search.
- **Serving:** vLLM with prefix caching (prompts include lots of repeated file context), FP8 or AWQ quants, separate deployments for autocomplete and chat.
- **Gateway:** SSO, per-user keys, rate limits, logging without storing code longer than needed.
- **Clients:** editor extensions that support custom OpenAI-compatible endpoints.
- **Evals:** a test set from your own codebase.

Autocomplete needs TTFT well under half a second, so size that part for latency, not throughput.

## 390: Your app shows think tags in the answers after switching to a reasoning model. How do you fix it?

The server isn't separating reasoning from the answer. Options:

- vLLM: add `--reasoning-parser` with the right parser for the model.
- `llama-server`: use `--reasoning-format` so thinking goes to `reasoning_content`.
- Ollama: set `think` in the request so thinking goes to `message.thinking`.
- Or turn thinking off if you don't need it.

Then update the client to read the separate reasoning field (show it collapsed or hide it). Stripping tags with a regex in the client is a fragile last resort.

## 391: Constrained JSON generation sometimes hangs, producing endless whitespace or newlines. Why, and how do you fix it?

Many JSON grammars allow any amount of whitespace between tokens. A model, especially a small or heavily quantized one, can get into a loop where whitespace is always a valid and likely next token, so it never closes the object.

Fixes: always set `max_tokens`; use a grammar or backend option that limits or disallows extra whitespace; describe the expected JSON in the prompt; lower temperature; and try a less aggressive quant. Treat a `length` finish reason on JSON output as a failure and retry.

## 392: A small local model at temperature 0 keeps repeating the same paragraph. What's going on?

Greedy decoding always picks the top token. Once the model repeats a phrase, the repetition itself makes repeating more likely, and it gets stuck in a loop. Small and heavily quantized models are more prone to it.

Use a small temperature with `min_p` or `top_p` instead of pure greedy, add a light repetition or DRY penalty, keep the model's recommended settings, and set `max_tokens`. If it still loops, try a bigger model or a higher-bit quant.

## 393: A big model is very slow on a Mac even though it "fits" in memory. What could be wrong?

macOS limits how much unified memory the GPU can use by default (roughly two thirds to three quarters, depending on total RAM). If the model plus KV cache goes over that, part of it runs on the CPU or the system swaps.

You can raise the limit with `sudo sysctl iogpu.wired_limit_mb=<value>` (it resets on reboot), close other apps, lower the context size or use a smaller quant. Also check that the tool actually uses Metal, and on memory pressure, watch Activity Monitor for swap.

## 394: You upgraded your embedding model, and search results got worse. What happened?

Vectors from different embedding models (or even different versions of one) live in different spaces. If your index has old vectors and queries use the new model, similarity scores are meaningless.

You have to re-embed the whole corpus with the new model. To do it without downtime, build a second index in parallel, compare quality on a test set of queries, then switch reads over and delete the old one. Store the embedding model name and version with every vector so this mistake is easy to catch.

## 395: Does quantizing an embedding model hurt retrieval?

A bit, usually less than people expect. 8-bit versions are typically almost identical to full precision; 4-bit can lower retrieval scores a little, more for small models.

Separately, you can quantize the stored vectors (int8 or binary), which saves a lot of storage and speeds up search, often with a rescoring step using full vectors. Measure recall at k on your own queries before and after either change.

## 396: How would you decide between a local model and a hosted API for a new feature?

Ask:

1. **Data:** can this data leave our network? If no, local.
2. **Quality:** does a model we can run pass our eval? If not, hosted (or wait).
3. **Volume:** is traffic high and steady enough for GPUs to be cheaper?
4. **Latency:** do we need on-device or very low network latency?
5. **Team:** do we have people to run GPU infrastructure?

Prototype with a hosted API to learn what quality is needed, then test whether a local model reaches it.

## 397: How can you make model loading faster for autoscaling?

- Keep weights on fast local NVMe or a node-level cache, not a slow network disk.
- Use safetensors (fast to map) and pre-sharded weights for tensor parallel.
- Stream weights from object storage with tools like the Run:ai model streamer (`--load-format runai_streamer` in vLLM).
- Persist the compile cache so `torch.compile` doesn't rerun.
- Use smaller container images and pre-pull them on GPU nodes.
- Keep warm standby replicas for sudden peaks.

## 398: What are the trade-offs of scaling self-hosted models to zero?

Scaling to zero saves money when traffic is rare, like internal tools used only in office hours. The cost is cold starts: getting a GPU node, pulling the image and loading the model can take minutes.

It works for batch jobs and tools where users accept a delay (show a "starting" message). For interactive products, keep at least one warm replica, or use a small always-on model and spin up the big one on demand.

## 399: Can you use spot or preemptible GPUs for inference?

Yes, with care. Spot GPUs are much cheaper but can be taken away with short notice.

They suit batch jobs (save finished results often and resume) and extra replicas behind a load balancer, as long as a base of on-demand replicas handles the minimum load. When a spot node gets a termination notice, stop sending it new requests and let in-flight requests finish if possible. Don't put your only replica on spot.

## 400: How would you trace self-hosted LLM calls end to end?

Use OpenTelemetry. Your app creates a span for each model call with attributes like model, version, token counts, finish reason and TTFT, following the GenAI semantic conventions where you can. Gateways like LiteLLM can export spans too, and vLLM can emit OpenTelemetry traces for requests.

Link the LLM spans with the rest of the request (database calls, retrieval, tools), so you can see whether slowness comes from the model, the queue or your own code.

## 401: How do you catch quality regressions in production?

- Run a fixed eval suite on every model, quant, template or runtime change before deploy.
- Sample live traffic (where allowed) and grade it with rules or an LLM judge.
- Track proxy signals: format errors, retries, user ratings, conversation abandonment, escalation to humans.
- Alert on sudden changes after deploys.

Regressions often come from things that don't look like model changes, like a runtime upgrade that changed a default sampling value.

## 402: What are the risks of using a local model as an LLM-as-judge?

Judges have biases: they prefer longer answers, answers in the first position, and outputs from their own model family. Smaller local judges are also less reliable at grading hard tasks.

Reduce this by using clear rubrics, swapping answer order and averaging, using a stronger model as judge than the ones being graded, and checking the judge against human labels on a sample before trusting it.

## 403: How can distillation help with local deployment?

Distillation trains a smaller "student" model on outputs from a bigger "teacher". For a narrow task, a 3B-8B student trained on thousands of teacher outputs can come close to the teacher's quality at a fraction of the cost and latency.

It's a common path: prototype with a big hosted model, collect its outputs (where the license allows using them for training), fine-tune a small open model on them, and self-host that. Check the teacher's terms; some providers forbid training competing models on their outputs.

## 404: You trained a QLoRA adapter on a 4-bit base. How should you serve it?

The adapter was trained against NF4-quantized base weights. The usual approach: load the base model in full precision (BF16), merge the adapter into it, save the merged model, then quantize the merged model to your serving format (FP8, AWQ or GGUF).

Merging into the 4-bit base directly is lossy and messy. Serving the adapter on top of a different quantized base (for example an AWQ base in vLLM) also works in many cases, but the slight mismatch can cost quality, so evaluate it.

## 405: How do sliding window attention models affect memory and serving?

Some models (Gemma, some Mistral versions, gpt-oss for some layers) use sliding window attention in some or all layers: those layers only look at the last N tokens (for example 4K), not the whole context.

For those layers the KV cache only needs to keep the last N tokens, which saves a lot of memory at long contexts. Engines need special support to take advantage of it; older versions may allocate full-length cache anyway. Prefix caching is also trickier with sliding windows. Check your engine's support for the specific model.

## 406: How do hybrid models with state-space layers change self-hosting?

Hybrid models mix normal attention layers with linear-attention or state-space (Mamba-style) layers. The non-attention layers keep a fixed-size state instead of a growing KV cache, so memory use grows much more slowly with context length.

This makes long contexts cheaper, but engines need specific support for these layers, and features like prefix caching and speculative decoding may work differently or arrive later. Check vLLM, llama.cpp and Ollama support for the exact model before you plan around it.

## 407: How do images affect memory and latency in vision models?

Each image is turned into many tokens, often hundreds to a few thousand depending on resolution and the model's tiling. Those tokens go through prefill like text, so they add to TTFT and KV cache size.

Resize images to the smallest resolution that keeps the needed detail, limit images per request, and count image tokens in your context budget. For document-heavy work, a dedicated OCR step plus a text model can be cheaper than sending full-page images.

## 408: How would you self-host speech-to-text next to your LLM?

Common options are whisper.cpp (GGML-based, runs on CPU, Metal and CUDA), faster-whisper (CTranslate2), and vLLM, which can serve some speech models through `/v1/audio/transcriptions`.

Put it behind the same gateway, and decide on streaming vs file-based transcription. Speech models are small compared to LLMs, so they can often share a GPU with an embedding model, but watch for latency interference with the LLM.

## 409: Why are agent workloads hard on self-hosted servers?

Agents make many calls in sequence, each with a long, growing context (instructions, tool definitions, past steps). Total latency is the sum of all steps, so TTFT and decode speed both matter a lot.

What helps: prefix caching with stable prompt order (tools and instructions first), routing all calls of one agent session to the same replica, a model with reliable tool calling, structured outputs for tool arguments, and limiting context growth by summarizing old steps.

## 410: How does vLLM support request priorities?

Start the server with `--scheduling-policy priority`, then send a `priority` value with each request (lower values run first). When capacity is short, high-priority requests are scheduled ahead of others, and lower-priority running requests can be preempted.

Use it to protect interactive traffic from background jobs on the same server. Watch for starvation: low-priority work can wait a very long time under constant high-priority load, so give it its own capacity or time windows.

## 411: The GPU isn't fully used, but vLLM throughput is low. What could be the bottleneck?

Often the CPU side:

- Tokenization and detokenization for many requests, or big JSON responses.
- Structured output mask computation for complex grammars.
- A single API server process handling all HTTP work (vLLM can run more with `--api-server-count`).
- Slow clients reading streams.
- A gateway or proxy in front that limits connections.

Check CPU usage of the API and engine processes, and compare client-side numbers with the server's metrics. Also check `--max-num-seqs`: it may be too low to fill the GPU.

## 412: How do you handle GPUs in Kubernetes reliably?

- Install the NVIDIA GPU Operator (drivers, container toolkit, device plugin, DCGM exporter).
- Request GPUs with `nvidia.com/gpu` limits; use node labels and taints so only GPU workloads land on GPU nodes.
- Match CUDA versions in images with the node driver.
- Set long startup probes for model loading.
- Use MIG profiles if you split GPUs.
- Watch for Xid errors and drain nodes that show hardware problems.

## 413: Where should model weights live in a Kubernetes setup?

Options:

- **Downloaded at start** from Hugging Face: simple, but slow and depends on an outside service.
- **Shared volume** (ReadWriteMany NFS or similar): one copy, but network reads can be slow.
- **Local NVMe cache** filled by a DaemonSet or init container: fast, more moving parts.
- **Model packaged as an OCI image or artifact** (for example KServe's ModelCar pattern): uses container caching and versioning.

For production, prefer a store you control, with versions and hashes, plus a fast local cache on GPU nodes.

## 414: What is Docker Model Runner?

Docker Model Runner is a Docker feature that pulls models as OCI artifacts (for example from Docker Hub's `ai/` namespace) and runs them with an OpenAI-compatible API, using llama.cpp (and other engines) underneath:

```bash
docker model pull ai/qwen3
docker model run ai/qwen3 "Hello"
```

It fits teams that already use Docker and Compose for local dev, because models are treated like other images. For large-scale GPU serving, vLLM or similar engines are still the norm.

## 415: Is it OK to run Ollama in production?

For small internal tools with a few users, yes, many teams do. It's simple and stable.

But know the limits: no built-in auth, weaker throughput under heavy concurrency than vLLM, GGUF-only models, less control over scheduling and memory, and fewer production features (priorities, multi-LoRA, detailed metrics). For customer-facing or high-traffic products, use vLLM or SGLang, or at least put Ollama behind a gateway with auth, limits and monitoring.

## 416: How would you explain to non-technical stakeholders why the local model is worse than ChatGPT?

Keep it concrete: hosted frontier models are much larger than what fits on our hardware, and they're trained with resources we can't match. Our local model is smaller to keep data private and costs predictable.

Then show what it means for your use case: eval results on real tasks, where it's good enough, where it isn't, and the options (bigger hardware, fine-tuning, routing hard cases to a hosted model where data rules allow).

## 417: How do you reduce hallucinations with a local model?

- Give it the facts: RAG with good retrieval and citations.
- Ask it to answer only from the given context and to say when it doesn't know.
- Use lower temperature for factual tasks.
- Validate outputs: check citations exist, check numbers against sources, use structured output.
- Use a bigger model or higher-bit quant for knowledge-heavy tasks.

Small local models have less built-in knowledge, so grounding matters more than with large hosted models.

## 418: How would you build a validate-and-retry loop for structured output from a local model?

```python
import json
from pydantic import BaseModel, ValidationError
from openai import OpenAI

class Invoice(BaseModel):
    number: str
    total: float

client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")

def extract(text: str, attempts: int = 3) -> Invoice:
    messages = [{"role": "user", "content": f"Extract the invoice as JSON: {text}"}]
    for _ in range(attempts):
        res = client.chat.completions.create(
            model="chat-model",
            messages=messages,
            response_format={"type": "json_schema",
                             "json_schema": {"name": "invoice", "schema": Invoice.model_json_schema()}},
            max_tokens=300,
        )
        content = res.choices[0].message.content
        try:
            return Invoice.model_validate(json.loads(content))
        except (ValidationError, json.JSONDecodeError) as e:
            messages += [{"role": "assistant", "content": content},
                         {"role": "user", "content": f"That was invalid: {e}. Try again."}]
    raise ValueError("could not extract invoice")
```

Constrained decoding handles syntax; validation catches values that are wrong for your business rules.

## 419: How can you use n > 1 sampling to improve answers from a local model?

Generate several answers in one request with `n=5`, then pick one: majority vote on the final answer (self-consistency, good for math and classification), a verifier or test (good for code), or a reranker or judge.

On vLLM the prompt is prefilled once and shared, so 5 samples cost much less than 5 separate calls. It trades extra compute for accuracy, which is often cheaper than switching to a bigger model.

## 420: How would you build a model cascade with a small and a large local model?

Send every request to the small model first. Use a confidence signal to decide whether to accept its answer: token logprobs, a validation check (schema, tests), a self-check question, or a small classifier. If confidence is low, send the request to the large model.

Tune the threshold on a labeled set to balance cost and quality. Done well, most traffic stays on the cheap model, and only hard cases pay for the big one.

## 421: Can you run LLMs inside the browser, and when does it make sense?

Yes. With WebGPU, libraries like WebLLM (MLC) and Transformers.js run small quantized models in the browser, and Chrome has built-in AI APIs that use an on-device model.

It makes sense for privacy (nothing leaves the device), offline use and zero server cost. Limits: large downloads on first use, varying GPU support across devices and browsers, and only small models. Use it for narrow features like rewriting, classification or autocomplete, with a server fallback.

## 422: Why is it risky to deploy a new open model on its release day?

New architectures often launch with bugs in conversions and runtimes: wrong chat templates, tokenizer issues, bad default settings, missing support for features like sliding window or tool calling, and broken first GGUF uploads. Fixes usually come over the next days or weeks.

Test early, but wait for the runtime support to settle (updated versions, fixed templates, re-uploaded quants) before going to production, and re-run evals on the final files.

## 423: Why can public benchmarks mislead you when choosing a local model?

Benchmarks can be contaminated (test questions leaked into training data), models can be tuned to score well on popular leaderboards, and benchmarks rarely match your exact task, language or format.

Also, scores are usually reported for full-precision weights with specific settings, not the quant you'll run. Use benchmarks to make a shortlist, then decide with your own evals on the deployed configuration.

## 424: What would be on your checklist before putting a self-hosted model in production?

- Model, revision, quant and license recorded and approved.
- Runtime version pinned; all flags documented.
- Eval suite passed on the exact deployed config.
- Load test done at expected peak, with latency goals met.
- Auth, TLS, rate limits and request caps at the gateway.
- Metrics, alerts, tracing and log retention set up.
- Health and readiness probes, warm-up and graceful shutdown.
- Rollback plan and a fallback for outages.
- Security review: network exposure, debug endpoints off, no `trust_remote_code` surprises.

## 425: A GPU node dies while it's streaming answers. How should the system behave?

Clients see a broken stream. The gateway or client should detect it (connection error or no tokens for a while) and decide whether to retry. Retrying a generation is usually safe because it doesn't change state, but the user may see the answer restart; show that clearly in the UI.

For agents, be careful: if the model's output was going to trigger a tool call with side effects, make tool execution idempotent or confirm before retrying. Meanwhile the orchestrator should mark the node unhealthy and stop routing to it.

## 426: A GPU server's disk fills up and the inference service fails. What are the usual causes?

- Old models piling up in Ollama's store or the Hugging Face cache.
- Compile caches and CUDA graph artifacts from many versions.
- Container images for each runtime version.
- Logs that include full prompts and outputs.
- Core dumps from crashes.

Put models and caches on separate volumes, clean up unused models on deploy, rotate logs, and alert on disk usage. Model files are tens of GB each, so disks fill faster than on normal app servers.

## 427: How do you keep your app easy to switch between local models and runtimes?

- Call models through one internal interface (or an OpenAI-compatible API) with the model name in config.
- Keep prompts, templates and sampling settings in versioned config, not hard-coded.
- Avoid runtime-specific features in core logic, or isolate them behind adapters.
- Keep an eval suite you can run against any new model or runtime.

Models and engines change every few months. Teams that can swap a model with a config change and an eval run move much faster.

## 428: Walk through what happens when a chat request hits a vLLM server.

1. The API server parses the request, applies the chat template and tokenizes the prompt.
2. The request goes to the engine core, where the scheduler checks the prefix cache and allocates KV blocks.
3. In the next steps, the prompt is prefilled (in chunks if long) together with other requests' work, using paged attention.
4. Each step, the model produces logits; sampling (with any grammar mask) picks the next token.
5. Tokens are sent back to the API server, detokenized and streamed to the client.
6. When a stop condition is hit, the request finishes, and its blocks are freed or kept in the prefix cache for reuse.

## 429: Walk through what happens when you run ollama run llama3.2 for the first time.

1. The CLI asks the local server if the model exists; it doesn't, so the server pulls the manifest from the registry and downloads the layer blobs, checking their hashes.
2. The scheduler estimates memory and starts a runner subprocess with a GPU/CPU layer split.
3. The runner memory-maps the GGUF weights and loads layers onto the GPU.
4. The CLI sends your messages to `/api/chat`; the server applies the Go chat template and passes the prompt to the runner.
5. The runner prefills, generates tokens and streams them back.
6. After `keep_alive` passes without requests, the runner is stopped and memory is freed.

## 430: How would you serve an LLM for a hospital that cannot send any data outside its network?

- **Hardware:** on-premises GPU servers (or a private cloud region under its control), with no internet egress from model servers.
- **Models:** open-weight models with licenses that allow the use, mirrored internally with hashes recorded; no runtime downloads.
- **Serving:** vLLM behind an internal gateway with SSO, audit logs and per-department limits.
- **Data handling:** strict log retention, PII handling rules, encryption at rest and in transit.
- **Safety:** evals on clinical tasks, guard models, human review for anything affecting care.
- **Operations:** offline update process for models, runtimes and security patches.

## 431: How would you choose between MIG partitions and separate small GPUs for many small models?

MIG gives hard isolation and predictable performance on big GPUs, which is good for many small models or tenants on shared H100s. But partitions have fixed sizes, and each gets only a slice of memory bandwidth, so a model is slower in a slice than on a full GPU.

Separate smaller GPUs (like L4 or L40S) are simpler and can be cheaper per model, but use more rack space and power. Compare cost per served token at your latency target for both.

## 432: How does power and cooling factor into self-hosting decisions?

Modern GPU servers draw several kilowatts each (an 8-GPU H100 server is around 10 kW). Many office server rooms and older data centers can't supply or cool that, which can block an on-premises plan.

Energy is also a real part of cost. Lower-precision formats (FP8, FP4) and better batching give more tokens per watt. Include power, cooling and rack space when comparing self-hosting to cloud.

## 433: How would you compare two quants with real users without them knowing?

Run a blind test: randomly assign users or sessions to variant A or B, keep the UI the same, and log which variant answered. Collect explicit ratings and implicit signals like copy actions, regenerations and follow-up corrections.

Run long enough to get significant results, and segment by task type, since a quant might hurt only one kind of task (like code or a specific language). Combine this with offline evals to understand why differences appear.

## 434: How would you handle a model that does well in English but worse in other languages after quantization?

Quantization can hurt less common languages more, because calibration data is often mostly English and those languages rely on weights the calibration didn't mark as important.

Options: quantize with calibration data (or an imatrix) that includes your languages, use a higher-bit quant, pick quants from uploaders who use multilingual calibration, or keep a separate deployment for those languages. Always include all your target languages in the eval set.

## 435: What do you do when a self-hosted model's output gets cut off in the middle of a sentence for some users only?

Look at what's different for those users:

- Longer history or documents, so prompt plus output hits the context limit.
- A lower `max_tokens` for their plan or client.
- A proxy or gateway timeout on long streams.
- Client disconnects that the server treats as cancellation.

Check `finish_reason` (`length` vs `stop`) and server logs for those requests. Token-count prompts before sending, and trim history to leave room for the answer.

## 436: How would you safely let a local model execute tools on internal systems?

- Give tools the minimum permissions they need, with their own service accounts.
- Validate tool arguments with strict schemas and business rules before running anything.
- Require human approval for actions that change data, spend money or contact people.
- Treat tool outputs (web pages, emails, documents) as untrusted, since they can carry prompt injection.
- Log every tool call with inputs and results.
- Limit loop iterations and total cost per task.

The model being local doesn't make tool use safe; the same rules as hosted models apply.

## 437: When would you put a reranker or guard model on the same GPU as the main LLM?

When all are small enough and traffic is moderate, sharing a GPU saves money: run them as separate processes with memory budgets, or in one engine if supported.

The risk is interference: a burst of reranking can slow LLM decoding. For strict latency goals, put small helper models on a separate cheaper GPU or even CPU (small rerankers and classifiers run fine on CPU at moderate volume).

## 438: How does context length per request affect the number of users a GPU can serve?

The KV cache is shared by all active requests. If each request may use up to 32K tokens and each token takes 128 KB, one request can take 4 GB. With 40 GB free for KV cache, at most 10 requests at full length can run at once.

Most requests are shorter, and paged allocation only uses what's needed, so real concurrency is higher. But long requests still crowd out others. Cap context per tier, and route long-context work to dedicated replicas if it's a small part of traffic.

## 439: Why might a model give better answers through Ollama than through your own llama.cpp build, using the same GGUF?

Differences in the setup, not the weights:

- Ollama's maintained template vs. the GGUF's own Jinja template (one may handle system prompts or tools better).
- Different default sampling values (temperature, top_k, min_p, repeat penalty).
- Different default context sizes.
- Different engines for some models (Ollama's own engine vs llama.cpp).

Set all sampling values explicitly, compare the formatted prompts and use the same context size before deciding one is "better".

## 440: What is the role of an inference gateway separate from the model servers?

The gateway handles everything that isn't model math: authentication, rate limits, quotas, routing between models and replicas, retries and fallbacks, logging and usage tracking, and request validation (prompt length, `max_tokens`, `n`).

Model servers stay simple and focused on throughput. It also lets you swap or upgrade model servers behind a stable API. Examples include LiteLLM, Envoy AI Gateway, Kong and custom services.

## 441: How do you handle model warm-up and graceful shutdown in a deployment?

**Warm-up:** after the server is healthy, send a few real-shaped requests (to trigger compilation, fill common prefixes) before the pod reports ready.

**Shutdown:** on SIGTERM, mark the pod not ready so the load balancer stops sending new requests, let in-flight streams finish within a grace period, then exit. Set Kubernetes `terminationGracePeriodSeconds` long enough for typical generations. Otherwise every deploy cuts off users mid-answer.

## 442: How would you investigate a gradual memory increase in a long-running inference server?

Check whether it's real growth or expected caching: vLLM's GPU memory is preallocated, so look at host RAM. Common causes are growing prefix cache in CPU offload, LoRA adapters accumulating in CPU memory, request logging buffers, metrics with unbounded label values (like one label per user), or a real leak in a specific version.

Track memory over time per process, compare across versions, reproduce with a load test, and check the project's issue tracker. As a stopgap, rolling restarts on a schedule keep it under control.

## 443: How would you serve both a fast autocomplete model and a slow reasoning model without one hurting the other?

Separate them physically: different deployments, ideally different GPUs, and separate queues in the gateway. Autocomplete needs very low TTFT and short outputs; reasoning produces long outputs that would fill batches and KV cache.

If you must share hardware, use priority scheduling with autocomplete as high priority, cap reasoning `max_tokens` and concurrency, and monitor autocomplete TTFT as the main alert.

## 444: How would you measure whether prefix caching is actually helping?

vLLM exposes prefix cache queries and hits in its metrics; compute the hit rate over time. Also compare TTFT distributions for requests with large shared prefixes before and after enabling stable prompt ordering or session-aware routing.

If the hit rate is low, check prompt layouts for changing content at the start, check how requests are spread across replicas, and check whether cache memory is too small so blocks get evicted before reuse.

## 445: What are the trade-offs of running one big replica vs many small replicas of a model?

One big replica (high tensor parallel) handles very long contexts and big batches, and has one shared prefix cache. But it's a single point of failure and has more communication overhead.

Many small replicas give better throughput per GPU, fault tolerance and simpler scaling, but each has its own cache (so routing matters) and each needs the whole model to fit. Most production setups use the smallest replica that fits the model and context needs, and scale out.

## 446: Your vLLM server is fine for short prompts but very slow for 100K-token prompts. What can you do?

Long prefill is expensive and attention cost grows with length.

- Check that prefix caching is on and prompts share stable prefixes (like the same document).
- Tune chunked prefill so long prompts don't block others, or send them to dedicated replicas.
- Use more tensor parallel GPUs for those requests.
- Use FP8 weights and KV cache to speed up compute and fit more.
- Reduce the prompt: better retrieval, summarizing, or only sending relevant sections.
- At scale, consider disaggregated prefill.

## 447: When would you choose a smaller model at higher precision over a bigger model at lower precision?

Usually the bigger model at Q4 wins. But choose the smaller, higher-precision model when:

- The bigger model would need extreme quants (2-3 bits) to fit, where damage grows fast.
- Your task needs exact formats, code or math, which are more sensitive to quantization.
- Latency matters more than the last bit of quality.
- The smaller model is fine-tuned for your task.

Test both on your eval; don't decide from the general rule alone.

## 448: How do you handle the different chat template and tool format needs when supporting many model families in one app?

Let the server apply the model's own template (OpenAI-compatible APIs do this), and send standard messages and tools. Avoid building raw prompts yourself.

Per model, keep a small config: tool call parser or format, reasoning parser, recommended sampling values, special stop tokens and known quirks. Test each model with your tool and structured output cases, since support varies even when the API looks the same.

## 449: What metrics would you put on a dashboard for a self-hosted LLM platform?

- **Traffic:** requests per second per model, tokens in and out.
- **Latency:** TTFT, inter-token latency, end-to-end, at p50/p95/p99, plus queue time.
- **Capacity:** running vs waiting requests, KV cache usage, preemptions, prefix cache hit rate.
- **Errors:** rate by type (timeouts, 5xx, validation, `length` finishes).
- **Hardware:** GPU utilization, memory, temperature, power, Xid errors.
- **Cost and usage:** tokens per team or key, cost per million tokens.
- **Quality:** eval scores per version, user feedback rate.

## 450: What are the most common mistakes teams make when they start self-hosting models?

- Using default context sizes and not noticing prompts get cut (especially in Ollama).
- Comparing a 4-bit local model to a full hosted model without evals, then being surprised.
- Exposing Ollama or vLLM ports with no auth.
- Not pinning model and runtime versions.
- Sizing GPUs for weights only and forgetting the KV cache and concurrency.
- Wrong chat templates or tool parsers, so tool calling "doesn't work".
- Ignoring the cost of idle GPUs and the engineering time to run them.
- No monitoring of queue time and KV cache, so capacity problems show up as user complaints.
