# Fine-Tuning LLMs Interview Questions and Answers

_Last updated: November 11, 2026_

450 interview questions about fine-tuning large language models, with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The questions cover when to fine-tune and when not to, preparing data, supervised fine-tuning, LoRA and QLoRA, preference tuning (DPO), reinforcement fine-tuning (GRPO), evaluation, serving and the problems you hit in real projects. Code examples use Hugging Face Transformers, TRL 1.x and PEFT with open-weight models, as of late 2026. Hosted fine-tuning changes often (OpenAI is closing its fine-tuning platform, and the Claude API does not offer fine-tuning), so check the provider docs before you plan around one.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is fine-tuning an LLM?](#1-what-is-fine-tuning-an-llm)
- [2: How is fine-tuning different from pretraining?](#2-how-is-fine-tuning-different-from-pretraining)
- [3: What is a base model?](#3-what-is-a-base-model)
- [4: What is an instruct or chat model?](#4-what-is-an-instruct-or-chat-model)
- [5: Why would a team fine-tune a model?](#5-why-would-a-team-fine-tune-a-model)
- [6: When should you not fine-tune?](#6-when-should-you-not-fine-tune)
- [7: What is the difference between prompt engineering and fine-tuning?](#7-what-is-the-difference-between-prompt-engineering-and-fine-tuning)
- [8: What is the difference between RAG and fine-tuning?](#8-what-is-the-difference-between-rag-and-fine-tuning)
- [9: Can fine-tuning teach a model new facts?](#9-can-fine-tuning-teach-a-model-new-facts)
- [10: What is supervised fine-tuning (SFT)?](#10-what-is-supervised-fine-tuning-sft)
- [11: What does one SFT training example look like?](#11-what-does-one-sft-training-example-look-like)
- [12: What is the conversational or messages format?](#12-what-is-the-conversational-or-messages-format)
- [13: What is JSONL and why is it used for training data?](#13-what-is-jsonl-and-why-is-it-used-for-training-data)
- [14: How many examples do you need to fine-tune?](#14-how-many-examples-do-you-need-to-fine-tune)
- [15: Why does data quality matter more than quantity?](#15-why-does-data-quality-matter-more-than-quantity)
- [16: What are training, validation and test sets?](#16-what-are-training-validation-and-test-sets)
- [17: What is a parameter or weight in a model?](#17-what-is-a-parameter-or-weight-in-a-model)
- [18: What does "8B" or "70B" mean in a model name?](#18-what-does-8b-or-70b-mean-in-a-model-name)
- [19: What is full fine-tuning?](#19-what-is-full-fine-tuning)
- [20: What is parameter-efficient fine-tuning (PEFT)?](#20-what-is-parameter-efficient-fine-tuning-peft)
- [21: What is LoRA?](#21-what-is-lora)
- [22: What is an adapter?](#22-what-is-an-adapter)
- [23: What is QLoRA?](#23-what-is-qlora)
- [24: What is quantization?](#24-what-is-quantization)
- [25: What is the rank in LoRA?](#25-what-is-the-rank-in-lora)
- [26: What is an epoch?](#26-what-is-an-epoch)
- [27: What is batch size?](#27-what-is-batch-size)
- [28: What is the learning rate?](#28-what-is-the-learning-rate)
- [29: What is loss?](#29-what-is-loss)
- [30: What is the difference between training loss and validation loss?](#30-what-is-the-difference-between-training-loss-and-validation-loss)
- [31: What is overfitting?](#31-what-is-overfitting)
- [32: What is underfitting?](#32-what-is-underfitting)
- [33: What is catastrophic forgetting?](#33-what-is-catastrophic-forgetting)
- [34: What is a checkpoint?](#34-what-is-a-checkpoint)
- [35: What is a tokenizer?](#35-what-is-a-tokenizer)
- [36: Why do tokens matter in fine-tuning?](#36-why-do-tokens-matter-in-fine-tuning)
- [37: What is a chat template?](#37-what-is-a-chat-template)
- [38: What is the max sequence length?](#38-what-is-the-max-sequence-length)
- [39: Why do you need a GPU to fine-tune?](#39-why-do-you-need-a-gpu-to-fine-tune)
- [40: What is VRAM and why does it limit fine-tuning?](#40-what-is-vram-and-why-does-it-limit-fine-tuning)
- [41: What is the Hugging Face Hub?](#41-what-is-the-hugging-face-hub)
- [42: What is the Transformers library?](#42-what-is-the-transformers-library)
- [43: What is TRL?](#43-what-is-trl)
- [44: What is the PEFT library?](#44-what-is-the-peft-library)
- [45: What is Unsloth?](#45-what-is-unsloth)
- [46: What is Axolotl?](#46-what-is-axolotl)
- [47: What is LLaMA-Factory?](#47-what-is-llama-factory)
- [48: What are open-weight models?](#48-what-are-open-weight-models)
- [49: Should you fine-tune an open-weight model or a hosted closed model?](#49-should-you-fine-tune-an-open-weight-model-or-a-hosted-closed-model)
- [50: Which hosted services let you fine-tune models in late 2026?](#50-which-hosted-services-let-you-fine-tune-models-in-late-2026)
- [51: Can you fine-tune Claude?](#51-can-you-fine-tune-claude)
- [52: What happened to OpenAI fine-tuning?](#52-what-happened-to-openai-fine-tuning)
- [53: Can you fine-tune Gemini?](#53-can-you-fine-tune-gemini)
- [54: What does a hosted fine-tuning service do for you?](#54-what-does-a-hosted-fine-tuning-service-do-for-you)
- [55: What is instruction tuning?](#55-what-is-instruction-tuning)
- [56: What is alignment?](#56-what-is-alignment)
- [57: What is RLHF?](#57-what-is-rlhf)
- [58: What is a reward model?](#58-what-is-a-reward-model)
- [59: What is DPO?](#59-what-is-dpo)
- [60: What does preference data look like?](#60-what-does-preference-data-look-like)
- [61: Should the system prompt be in the training data?](#61-should-the-system-prompt-be-in-the-training-data)
- [62: How do few-shot prompts relate to fine-tuning?](#62-how-do-few-shot-prompts-relate-to-fine-tuning)
- [63: What is inference?](#63-what-is-inference)
- [64: What is an eval?](#64-what-is-an-eval)
- [65: What is a baseline?](#65-what-is-a-baseline)
- [66: What is a hyperparameter?](#66-what-is-a-hyperparameter)
- [67: What does a fine-tuning run cost?](#67-what-does-a-fine-tuning-run-cost)
- [68: What is mixed precision training?](#68-what-is-mixed-precision-training)
- [69: What is the difference between fp16 and bf16?](#69-what-is-the-difference-between-fp16-and-bf16)
- [70: What is a gradient?](#70-what-is-a-gradient)
- [71: What is backpropagation?](#71-what-is-backpropagation)
- [72: What is an optimizer like AdamW?](#72-what-is-an-optimizer-like-adamw)
- [73: What is learning rate warmup?](#73-what-is-learning-rate-warmup)
- [74: What is a learning rate scheduler?](#74-what-is-a-learning-rate-scheduler)
- [75: What is gradient accumulation?](#75-what-is-gradient-accumulation)
- [76: What is gradient checkpointing?](#76-what-is-gradient-checkpointing)
- [77: What is a model card?](#77-what-is-a-model-card)
- [78: Why does the license matter when fine-tuning?](#78-why-does-the-license-matter-when-fine-tuning)
- [79: What is synthetic data?](#79-what-is-synthetic-data)
- [80: What is distillation?](#80-what-is-distillation)
- [81: What are teacher and student models?](#81-what-are-teacher-and-student-models)
- [82: What is continued pretraining?](#82-what-is-continued-pretraining)
- [83: Can you fine-tune an LLM for classification?](#83-can-you-fine-tune-an-llm-for-classification)
- [84: What does merging an adapter mean?](#84-what-does-merging-an-adapter-mean)
- [85: What is safetensors?](#85-what-is-safetensors)
- [86: What is GGUF?](#86-what-is-gguf)
- [87: Can you run a fine-tuned model in Ollama?](#87-can-you-run-a-fine-tuned-model-in-ollama)
- [88: What is vLLM?](#88-what-is-vllm)
- [89: Can you fine-tune on a Mac?](#89-can-you-fine-tune-on-a-mac)
- [90: Can you fine-tune in Google Colab?](#90-can-you-fine-tune-in-google-colab)
- [91: What is data labeling?](#91-what-is-data-labeling)
- [92: What does "garbage in, garbage out" mean for fine-tuning?](#92-what-does-garbage-in-garbage-out-mean-for-fine-tuning)
- [93: What is PII and why remove it from training data?](#93-what-is-pii-and-why-remove-it-from-training-data)
- [94: What is deduplication and why do it?](#94-what-is-deduplication-and-why-do-it)
- [95: What is data leakage between train and test sets?](#95-what-is-data-leakage-between-train-and-test-sets)
- [96: Does fine-tuning fix hallucinations?](#96-does-fine-tuning-fix-hallucinations)
- [97: Does fine-tuning change temperature or other sampling settings?](#97-does-fine-tuning-change-temperature-or-other-sampling-settings)
- [98: What is the EOS token?](#98-what-is-the-eos-token)
- [99: What is padding?](#99-what-is-padding)
- [100: What is a random seed and why set it?](#100-what-is-a-random-seed-and-why-set-it)
- [101: What is experiment tracking?](#101-what-is-experiment-tracking)
- [102: What is TensorBoard?](#102-what-is-tensorboard)
- [103: How big is a LoRA adapter compared to the full model?](#103-how-big-is-a-lora-adapter-compared-to-the-full-model)
- [104: Can you use more than one LoRA adapter at a time?](#104-can-you-use-more-than-one-lora-adapter-at-a-time)
- [105: What are target modules in LoRA?](#105-what-are-target-modules-in-lora)
- [106: What is lora_alpha?](#106-what-is-lora_alpha)
- [107: What is dropout in LoRA?](#107-what-is-dropout-in-lora)
- [108: What is weight decay?](#108-what-is-weight-decay)
- [109: What is early stopping?](#109-what-is-early-stopping)
- [110: What is perplexity?](#110-what-is-perplexity)
- [111: What is a held-out test set?](#111-what-is-a-held-out-test-set)
- [112: Why is human evaluation still needed?](#112-why-is-human-evaluation-still-needed)
- [113: What is LLM-as-a-judge?](#113-what-is-llm-as-a-judge)
- [114: What is A/B testing a fine-tuned model?](#114-what-is-ab-testing-a-fine-tuned-model)
- [115: Why version datasets and models?](#115-why-version-datasets-and-models)
- [116: Can you fine-tune embedding models?](#116-can-you-fine-tune-embedding-models)
- [117: Can you fine-tune reasoning models?](#117-can-you-fine-tune-reasoning-models)
- [118: What is reinforcement fine-tuning (RFT)?](#118-what-is-reinforcement-fine-tuning-rft)
- [119: What is GRPO?](#119-what-is-grpo)
- [120: What is a reward function or grader?](#120-what-is-a-reward-function-or-grader)
- [121: Can you fine-tune a model to call tools?](#121-can-you-fine-tune-a-model-to-call-tools)
- [122: Can fine-tuning make a model output valid JSON every time?](#122-can-fine-tuning-make-a-model-output-valid-json-every-time)
- [123: What are typical use cases for fine-tuning?](#123-what-are-typical-use-cases-for-fine-tuning)
- [124: Why fine-tune a small model?](#124-why-fine-tune-a-small-model)
- [125: How can a small fine-tuned model beat a big model?](#125-how-can-a-small-fine-tuned-model-beat-a-big-model)
- [126: How long does fine-tuning take?](#126-how-long-does-fine-tuning-take)
- [127: What is a training job?](#127-what-is-a-training-job)
- [128: What does a training config file look like?](#128-what-does-a-training-config-file-look-like)
- [129: What is packing?](#129-what-is-packing)
- [130: What does training only on the completion mean?](#130-what-does-training-only-on-the-completion-mean)
- [131: Can training data have more than one turn?](#131-can-training-data-have-more-than-one-turn)
- [132: What is the prompt-completion format?](#132-what-is-the-prompt-completion-format)
- [133: What is post-training?](#133-what-is-post-training)
- [134: What is the usual order of training steps?](#134-what-is-the-usual-order-of-training-steps)
- [135: Can you fine-tune for multiple languages?](#135-can-you-fine-tune-for-multiple-languages)
- [136: Can you fine-tune a model for code?](#136-can-you-fine-tune-a-model-for-code)
- [137: Can a long system prompt replace fine-tuning?](#137-can-a-long-system-prompt-replace-fine-tuning)
- [138: How do you quickly test a fine-tuned model in Python?](#138-how-do-you-quickly-test-a-fine-tuned-model-in-python)
- [139: How do you upload a fine-tuned model to the Hugging Face Hub?](#139-how-do-you-upload-a-fine-tuned-model-to-the-hugging-face-hub)
- [140: What is the Hugging Face datasets library?](#140-what-is-the-hugging-face-datasets-library)
- [141: Where can you rent GPUs for fine-tuning?](#141-where-can-you-rent-gpus-for-fine-tuning)
- [142: What is Accelerate?](#142-what-is-accelerate)
- [143: What does a web developer need to know to start fine-tuning?](#143-what-does-a-web-developer-need-to-know-to-start-fine-tuning)
- [144: What are the basic steps of a fine-tuning project?](#144-what-are-the-basic-steps-of-a-fine-tuning-project)
- [145: What are common beginner mistakes in fine-tuning?](#145-what-are-common-beginner-mistakes-in-fine-tuning)
- [146: What is a learning curve in fine-tuning?](#146-what-is-a-learning-curve-in-fine-tuning)
- [147: What is the difference between a model ID and an adapter ID?](#147-what-is-the-difference-between-a-model-id-and-an-adapter-id)
- [148: What is SFT data balance?](#148-what-is-sft-data-balance)
- [149: Why should you read your training data by hand?](#149-why-should-you-read-your-training-data-by-hand)
- [150: What does "the model learns the format before the content" mean?](#150-what-does-the-model-learns-the-format-before-the-content-mean)

### Moderate Questions (151-300)

- [151: How do you decide if a task really needs fine-tuning?](#151-how-do-you-decide-if-a-task-really-needs-fine-tuning)
- [152: How do you build a prompting baseline before fine-tuning?](#152-how-do-you-build-a-prompting-baseline-before-fine-tuning)
- [153: How do you collect training data from production logs?](#153-how-do-you-collect-training-data-from-production-logs)
- [154: What does cleaning a fine-tuning dataset involve?](#154-what-does-cleaning-a-fine-tuning-dataset-involve)
- [155: What makes a good training example?](#155-what-makes-a-good-training-example)
- [156: How do you generate synthetic training data with a larger model?](#156-how-do-you-generate-synthetic-training-data-with-a-larger-model)
- [157: How do you filter synthetic data?](#157-how-do-you-filter-synthetic-data)
- [158: How do you handle class imbalance in fine-tuning data?](#158-how-do-you-handle-class-imbalance-in-fine-tuning-data)
- [159: How do you teach a fine-tuned model to refuse or say "I don't know"?](#159-how-do-you-teach-a-fine-tuned-model-to-refuse-or-say-i-dont-know)
- [160: How do you convert raw data into the messages format?](#160-how-do-you-convert-raw-data-into-the-messages-format)
- [161: How do you see what the chat template produces?](#161-how-do-you-see-what-the-chat-template-produces)
- [162: How do you validate a training dataset before a run?](#162-how-do-you-validate-a-training-dataset-before-a-run)
- [163: How do you split a dataset into train and validation sets?](#163-how-do-you-split-a-dataset-into-train-and-validation-sets)
- [164: What does a minimal SFT run with TRL look like?](#164-what-does-a-minimal-sft-run-with-trl-look-like)
- [165: Which SFTConfig settings matter most?](#165-which-sftconfig-settings-matter-most)
- [166: How do you add LoRA to an SFTTrainer run?](#166-how-do-you-add-lora-to-an-sfttrainer-run)
- [167: How do you choose the LoRA rank and alpha?](#167-how-do-you-choose-the-lora-rank-and-alpha)
- [168: Should LoRA target only attention layers or all linear layers?](#168-should-lora-target-only-attention-layers-or-all-linear-layers)
- [169: How do you set up QLoRA?](#169-how-do-you-set-up-qlora)
- [170: How do you choose a learning rate?](#170-how-do-you-choose-a-learning-rate)
- [171: How many epochs should you train?](#171-how-many-epochs-should-you-train)
- [172: How do you choose the batch size?](#172-how-do-you-choose-the-batch-size)
- [173: How do you estimate how much GPU memory you need?](#173-how-do-you-estimate-how-much-gpu-memory-you-need)
- [174: How do you fit training on a single GPU?](#174-how-do-you-fit-training-on-a-single-gpu)
- [175: How do you pick a base model?](#175-how-do-you-pick-a-base-model)
- [176: Should you start from a base model or an instruct model?](#176-should-you-start-from-a-base-model-or-an-instruct-model)
- [177: How do you read a training loss curve?](#177-how-do-you-read-a-training-loss-curve)
- [178: What does it mean if training loss goes almost to zero?](#178-what-does-it-mean-if-training-loss-goes-almost-to-zero)
- [179: What should you do if validation loss starts going up?](#179-what-should-you-do-if-validation-loss-starts-going-up)
- [180: What should you check if the loss doesn't go down at all?](#180-what-should-you-check-if-the-loss-doesnt-go-down-at-all)
- [181: What causes loss spikes or NaN loss?](#181-what-causes-loss-spikes-or-nan-loss)
- [182: How do you fix CUDA out of memory errors?](#182-how-do-you-fix-cuda-out-of-memory-errors)
- [183: Why does a fine-tuned model keep generating and never stop?](#183-why-does-a-fine-tuned-model-keep-generating-and-never-stop)
- [184: Why does the fine-tuned model ignore what it was trained on?](#184-why-does-the-fine-tuned-model-ignore-what-it-was-trained-on)
- [185: What are assistant_only_loss and completion_only_loss in TRL?](#185-what-are-assistant_only_loss-and-completion_only_loss-in-trl)
- [186: What are the pros and cons of packing?](#186-what-are-the-pros-and-cons-of-packing)
- [187: How do you choose max_length and handle long examples?](#187-how-do-you-choose-max_length-and-handle-long-examples)
- [188: How do you build an eval set for a fine-tuned model?](#188-how-do-you-build-an-eval-set-for-a-fine-tuned-model)
- [189: Which metrics fit common fine-tuning tasks?](#189-which-metrics-fit-common-fine-tuning-tasks)
- [190: How do you use LLM-as-a-judge well?](#190-how-do-you-use-llm-as-a-judge-well)
- [191: How do you compare a fine-tuned model fairly with the baseline?](#191-how-do-you-compare-a-fine-tuned-model-fairly-with-the-baseline)
- [192: How do you check that fine-tuning didn't break general skills?](#192-how-do-you-check-that-fine-tuning-didnt-break-general-skills)
- [193: How do you save and load a LoRA adapter?](#193-how-do-you-save-and-load-a-lora-adapter)
- [194: How do you merge a LoRA adapter into the base model?](#194-how-do-you-merge-a-lora-adapter-into-the-base-model)
- [195: How do you keep a fine-tuned model private on the Hub?](#195-how-do-you-keep-a-fine-tuned-model-private-on-the-hub)
- [196: How do you serve a LoRA adapter with vLLM?](#196-how-do-you-serve-a-lora-adapter-with-vllm)
- [197: How do you serve many LoRA adapters from one base model?](#197-how-do-you-serve-many-lora-adapters-from-one-base-model)
- [198: How do you run a fine-tuned model in Ollama via GGUF?](#198-how-do-you-run-a-fine-tuned-model-in-ollama-via-gguf)
- [199: Should you quantize a model after fine-tuning?](#199-should-you-quantize-a-model-after-fine-tuning)
- [200: How do you call a self-hosted fine-tuned model from a Node.js app?](#200-how-do-you-call-a-self-hosted-fine-tuned-model-from-a-nodejs-app)
- [201: How do you use a fine-tuned model with the Vercel AI SDK?](#201-how-do-you-use-a-fine-tuned-model-with-the-vercel-ai-sdk)
- [202: Why must the inference prompt match the training format?](#202-why-must-the-inference-prompt-match-the-training-format)
- [203: How do you create DPO preference pairs?](#203-how-do-you-create-dpo-preference-pairs)
- [204: What does a DPO training run look like in TRL?](#204-what-does-a-dpo-training-run-look-like-in-trl)
- [205: What does the beta parameter in DPO do?](#205-what-does-the-beta-parameter-in-dpo-do)
- [206: When should you use DPO instead of more SFT?](#206-when-should-you-use-dpo-instead-of-more-sft)
- [207: What is KTO and when is it useful?](#207-what-is-kto-and-when-is-it-useful)
- [208: What other preference methods might come up in an interview?](#208-what-other-preference-methods-might-come-up-in-an-interview)
- [209: How do you train a reward model with TRL?](#209-how-do-you-train-a-reward-model-with-trl)
- [210: How do you fine-tune a model for reliable JSON output?](#210-how-do-you-fine-tune-a-model-for-reliable-json-output)
- [211: How do you prepare tool-calling training data?](#211-how-do-you-prepare-tool-calling-training-data)
- [212: When should you use an encoder model instead of an LLM for classification?](#212-when-should-you-use-an-encoder-model-instead-of-an-llm-for-classification)
- [213: How do you fine-tune an embedding model with sentence-transformers?](#213-how-do-you-fine-tune-an-embedding-model-with-sentence-transformers)
- [214: How do you fine-tune a model for RAG answers?](#214-how-do-you-fine-tune-a-model-for-rag-answers)
- [215: What is the workflow for distilling a big model into a small one?](#215-what-is-the-workflow-for-distilling-a-big-model-into-a-small-one)
- [216: What legal issues come with training on model outputs?](#216-what-legal-issues-come-with-training-on-model-outputs)
- [217: How do you search for good hyperparameters without wasting money?](#217-how-do-you-search-for-good-hyperparameters-without-wasting-money)
- [218: How do you track fine-tuning experiments?](#218-how-do-you-track-fine-tuning-experiments)
- [219: How do you make fine-tuning runs reproducible?](#219-how-do-you-make-fine-tuning-runs-reproducible)
- [220: How do you version training data?](#220-how-do-you-version-training-data)
- [221: How do you fine-tune with Unsloth?](#221-how-do-you-fine-tune-with-unsloth)
- [222: How do you run an Axolotl training job?](#222-how-do-you-run-an-axolotl-training-job)
- [223: Can you run TRL from the command line?](#223-can-you-run-trl-from-the-command-line)
- [224: How do you fine-tune with MLX on a Mac?](#224-how-do-you-fine-tune-with-mlx-on-a-mac)
- [225: How does supervised tuning work on Vertex AI for Gemini?](#225-how-does-supervised-tuning-work-on-vertex-ai-for-gemini)
- [226: When should you use a hosted fine-tuning platform instead of training yourself?](#226-when-should-you-use-a-hosted-fine-tuning-platform-instead-of-training-yourself)
- [227: How do you estimate the cost of a fine-tuning run?](#227-how-do-you-estimate-the-cost-of-a-fine-tuning-run)
- [228: What is a checklist for running training on a cloud GPU?](#228-what-is-a-checklist-for-running-training-on-a-cloud-gpu)
- [229: How do you run training on multiple GPUs?](#229-how-do-you-run-training-on-multiple-gpus)
- [230: What are FSDP and DeepSpeed ZeRO in simple terms?](#230-what-are-fsdp-and-deepspeed-zero-in-simple-terms)
- [231: How do you do continued pretraining on domain text?](#231-how-do-you-do-continued-pretraining-on-domain-text)
- [232: How does mixing general data help reduce forgetting?](#232-how-does-mixing-general-data-help-reduce-forgetting)
- [233: Can you fine-tune one model for several tasks at once?](#233-can-you-fine-tune-one-model-for-several-tasks-at-once)
- [234: What should you watch for when fine-tuning for multiple languages?](#234-what-should-you-watch-for-when-fine-tuning-for-multiple-languages)
- [235: How do you handle long documents in fine-tuning?](#235-how-do-you-handle-long-documents-in-fine-tuning)
- [236: How should you handle the system prompt in training data?](#236-how-should-you-handle-the-system-prompt-in-training-data)
- [237: How do you teach a fine-tuned model to stay on topic?](#237-how-do-you-teach-a-fine-tuned-model-to-stay-on-topic)
- [238: What should you test before releasing a fine-tuned model?](#238-what-should-you-test-before-releasing-a-fine-tuned-model)
- [239: How do you roll out a fine-tuned model safely?](#239-how-do-you-roll-out-a-fine-tuned-model-safely)
- [240: What should you monitor for a fine-tuned model in production?](#240-what-should-you-monitor-for-a-fine-tuned-model-in-production)
- [241: How do you use production feedback to improve the next version?](#241-how-do-you-use-production-feedback-to-improve-the-next-version)
- [242: How often should you retrain a fine-tuned model?](#242-how-often-should-you-retrain-a-fine-tuned-model)
- [243: What do you do when a new version of the base model comes out?](#243-what-do-you-do-when-a-new-version-of-the-base-model-comes-out)
- [244: How does fine-tuning compare with prompt caching on cost?](#244-how-does-fine-tuning-compare-with-prompt-caching-on-cost)
- [245: Why can a fine-tuned small model reduce latency?](#245-why-can-a-fine-tuned-small-model-reduce-latency)
- [246: How do you add new special tokens to the tokenizer?](#246-how-do-you-add-new-special-tokens-to-the-tokenizer)
- [247: What problems come from the pad token and padding side?](#247-what-problems-come-from-the-pad-token-and-padding-side)
- [248: What are the trade-offs of gradient checkpointing?](#248-what-are-the-trade-offs-of-gradient-checkpointing)
- [249: How do you pick the attention implementation for training?](#249-how-do-you-pick-the-attention-implementation-for-training)
- [250: Which learning rate scheduler should you use?](#250-which-learning-rate-scheduler-should-you-use)
- [251: How do you evaluate during training?](#251-how-do-you-evaluate-during-training)
- [252: How do you resume a training run that crashed?](#252-how-do-you-resume-a-training-run-that-crashed)
- [253: How do you debug what the model is actually trained on?](#253-how-do-you-debug-what-the-model-is-actually-trained-on)
- [254: What does a label of -100 mean?](#254-what-does-a-label-of--100-mean)
- [255: How do you fix overfitting on a small dataset?](#255-how-do-you-fix-overfitting-on-a-small-dataset)
- [256: How do you find near duplicates in a dataset?](#256-how-do-you-find-near-duplicates-in-a-dataset)
- [257: How do you scrub PII from training data?](#257-how-do-you-scrub-pii-from-training-data)
- [258: What privacy rules apply to training on user data?](#258-what-privacy-rules-apply-to-training-on-user-data)
- [259: How can bias in training data affect a fine-tuned model?](#259-how-can-bias-in-training-data-affect-a-fine-tuned-model)
- [260: Can fine-tuning make a model less safe?](#260-can-fine-tuning-make-a-model-less-safe)
- [261: How do you evaluate the safety of a fine-tuned model?](#261-how-do-you-evaluate-the-safety-of-a-fine-tuned-model)
- [262: Does fine-tuning protect against prompt injection?](#262-does-fine-tuning-protect-against-prompt-injection)
- [263: How do you use fine-tuning to reduce prompt size and cost?](#263-how-do-you-use-fine-tuning-to-reduce-prompt-size-and-cost)
- [264: How do you fine-tune a model to write in a brand voice?](#264-how-do-you-fine-tune-a-model-to-write-in-a-brand-voice)
- [265: How would you fine-tune a model for SQL generation?](#265-how-would-you-fine-tune-a-model-for-sql-generation)
- [266: How would you fine-tune a model for document extraction?](#266-how-would-you-fine-tune-a-model-for-document-extraction)
- [267: What goes wrong when fine-tuning a support chatbot on old tickets?](#267-what-goes-wrong-when-fine-tuning-a-support-chatbot-on-old-tickets)
- [268: How do you combine RAG and fine-tuning?](#268-how-do-you-combine-rag-and-fine-tuning)
- [269: What does a basic GRPO run in TRL look like?](#269-what-does-a-basic-grpo-run-in-trl-look-like)
- [270: How do you write good reward functions?](#270-how-do-you-write-good-reward-functions)
- [271: What is reward hacking?](#271-what-is-reward-hacking)
- [272: What does num_generations do in GRPO?](#272-what-does-num_generations-do-in-grpo)
- [273: What data do you need for reinforcement fine-tuning?](#273-what-data-do-you-need-for-reinforcement-fine-tuning)
- [274: Should you do SFT on chain-of-thought for a reasoning model?](#274-should-you-do-sft-on-chain-of-thought-for-a-reasoning-model)
- [275: How do you handle thinking or reasoning sections in training data?](#275-how-do-you-handle-thinking-or-reasoning-sections-in-training-data)
- [276: How do you fine-tune a vision-language model?](#276-how-do-you-fine-tune-a-vision-language-model)
- [277: Can a fine-tuned model run on device or in the browser?](#277-can-a-fine-tuned-model-run-on-device-or-in-the-browser)
- [278: How do you export a fine-tuned model to ONNX?](#278-how-do-you-export-a-fine-tuned-model-to-onnx)
- [279: How do you choose a serving tool for a fine-tuned model?](#279-how-do-you-choose-a-serving-tool-for-a-fine-tuned-model)
- [280: Where should you store fine-tuned adapters and models?](#280-where-should-you-store-fine-tuned-adapters-and-models)
- [281: What security risks come with loading models?](#281-what-security-risks-come-with-loading-models)
- [282: How do you test output format in CI?](#282-how-do-you-test-output-format-in-ci)
- [283: How do you run evals automatically for each new model version?](#283-how-do-you-run-evals-automatically-for-each-new-model-version)
- [284: How do you write a simple eval harness in Python?](#284-how-do-you-write-a-simple-eval-harness-in-python)
- [285: What is lm-evaluation-harness?](#285-what-is-lm-evaluation-harness)
- [286: What is benchmark contamination?](#286-what-is-benchmark-contamination)
- [287: How do you explain fine-tuning results to non-technical stakeholders?](#287-how-do-you-explain-fine-tuning-results-to-non-technical-stakeholders)
- [288: How do you choose between a 1B, 8B and 70B model?](#288-how-do-you-choose-between-a-1b-8b-and-70b-model)
- [289: What's different about fine-tuning Mixture of Experts (MoE) models?](#289-whats-different-about-fine-tuning-mixture-of-experts-moe-models)
- [290: What are signs of a learning rate that's too high?](#290-what-are-signs-of-a-learning-rate-thats-too-high)
- [291: What is a typical starting config for a LoRA SFT run?](#291-what-is-a-typical-starting-config-for-a-lora-sft-run)
- [292: How do you know if more data will help?](#292-how-do-you-know-if-more-data-will-help)
- [293: How do you decide which examples to label next?](#293-how-do-you-decide-which-examples-to-label-next)
- [294: What is error analysis and why do it after each run?](#294-what-is-error-analysis-and-why-do-it-after-each-run)
- [295: What can go wrong when fine-tuning on very short answers?](#295-what-can-go-wrong-when-fine-tuning-on-very-short-answers)
- [296: How do you handle examples where several answers are correct?](#296-how-do-you-handle-examples-where-several-answers-are-correct)
- [297: How do you keep training and serving prompts in sync?](#297-how-do-you-keep-training-and-serving-prompts-in-sync)
- [298: How do you migrate off OpenAI fine-tuning?](#298-how-do-you-migrate-off-openai-fine-tuning)
- [299: When should you train separate adapters instead of one model?](#299-when-should-you-train-separate-adapters-instead-of-one-model)
- [300: What are signs a fine-tuning project is going well?](#300-what-are-signs-a-fine-tuning-project-is-going-well)

### Advanced Questions (301-450)

- [301: How does LoRA work at the math level?](#301-how-does-lora-work-at-the-math-level)
- [302: Why is the LoRA B matrix initialized to zero?](#302-why-is-the-lora-b-matrix-initialized-to-zero)
- [303: Why does a low-rank update work so well?](#303-why-does-a-low-rank-update-work-so-well)
- [304: What is rsLoRA and why does it exist?](#304-what-is-rslora-and-why-does-it-exist)
- [305: What is DoRA?](#305-what-is-dora)
- [306: How does LoRA compare with full fine-tuning in quality?](#306-how-does-lora-compare-with-full-fine-tuning-in-quality)
- [307: Which layers matter most for LoRA, attention or MLP?](#307-which-layers-matter-most-for-lora-attention-or-mlp)
- [308: How does QLoRA reduce memory, and what are NF4 and double quantization?](#308-how-does-qlora-reduce-memory-and-what-are-nf4-and-double-quantization)
- [309: What uses the memory in full fine-tuning?](#309-what-uses-the-memory-in-full-fine-tuning)
- [310: How does mixed precision training work inside?](#310-how-does-mixed-precision-training-work-inside)
- [311: How do activations grow with sequence length?](#311-how-do-activations-grow-with-sequence-length)
- [312: How does gradient checkpointing work internally?](#312-how-does-gradient-checkpointing-work-internally)
- [313: What are the ZeRO stages?](#313-what-are-the-zero-stages)
- [314: How do you choose between FSDP and DeepSpeed?](#314-how-do-you-choose-between-fsdp-and-deepspeed)
- [315: When do you need tensor or pipeline parallelism?](#315-when-do-you-need-tensor-or-pipeline-parallelism)
- [316: How do you fine-tune with very long contexts?](#316-how-do-you-fine-tune-with-very-long-contexts)
- [317: What can go wrong with packing at the attention level?](#317-what-can-go-wrong-with-packing-at-the-attention-level)
- [318: How do batch size and learning rate interact?](#318-how-do-batch-size-and-learning-rate-interact)
- [319: How do 8-bit and paged optimizers save memory?](#319-how-do-8-bit-and-paged-optimizers-save-memory)
- [320: How does learning rate relate to catastrophic forgetting?](#320-how-does-learning-rate-relate-to-catastrophic-forgetting)
- [321: Why can fine-tuning on new facts increase hallucinations?](#321-why-can-fine-tuning-on-new-facts-increase-hallucinations)
- [322: What is the "superficial alignment" idea?](#322-what-is-the-superficial-alignment-idea)
- [323: How does DPO work under the hood?](#323-how-does-dpo-work-under-the-hood)
- [324: What are common DPO failure modes?](#324-what-are-common-dpo-failure-modes)
- [325: What is the reference model in DPO and how do you handle its memory?](#325-what-is-the-reference-model-in-dpo-and-how-do-you-handle-its-memory)
- [326: What is the difference between online and offline preference training?](#326-what-is-the-difference-between-online-and-offline-preference-training)
- [327: How does PPO-based RLHF work, and why is it expensive?](#327-how-does-ppo-based-rlhf-work-and-why-is-it-expensive)
- [328: How does GRPO differ from PPO?](#328-how-does-grpo-differ-from-ppo)
- [329: What does the KL penalty do in RL fine-tuning?](#329-what-does-the-kl-penalty-do-in-rl-fine-tuning)
- [330: What are real examples of reward hacking, and how do you defend against them?](#330-what-are-real-examples-of-reward-hacking-and-how-do-you-defend-against-them)
- [331: How do you design verifiable rewards?](#331-how-do-you-design-verifiable-rewards)
- [332: What does reinforcement fine-tuning improve that SFT doesn't?](#332-what-does-reinforcement-fine-tuning-improve-that-sft-doesnt)
- [333: Why is generation the bottleneck in GRPO training, and how is it handled?](#333-why-is-generation-the-bottleneck-in-grpo-training-and-how-is-it-handled)
- [334: What is entropy collapse in RL fine-tuning?](#334-what-is-entropy-collapse-in-rl-fine-tuning)
- [335: How do you pick prompt difficulty for RL training?](#335-how-do-you-pick-prompt-difficulty-for-rl-training)
- [336: What is the difference between logit distillation and sequence-level distillation?](#336-what-is-the-difference-between-logit-distillation-and-sequence-level-distillation)
- [337: What is model collapse with synthetic data?](#337-what-is-model-collapse-with-synthetic-data)
- [338: What subtle chat template bugs can break fine-tuning?](#338-what-subtle-chat-template-bugs-can-break-fine-tuning)
- [339: How should embeddings for new tokens be initialized?](#339-how-should-embeddings-for-new-tokens-be-initialized)
- [340: How do you extend a model's context length with fine-tuning?](#340-how-do-you-extend-a-models-context-length-with-fine-tuning)
- [341: What's special about fine-tuning MoE models internally?](#341-whats-special-about-fine-tuning-moe-models-internally)
- [342: What is model merging and when is it useful?](#342-what-is-model-merging-and-when-is-it-useful)
- [343: What problems come from merging LoRA into a quantized model?](#343-what-problems-come-from-merging-lora-into-a-quantized-model)
- [344: How do servers serve many LoRA adapters efficiently?](#344-how-do-servers-serve-many-lora-adapters-efficiently)
- [345: What does unmerged LoRA cost at inference time?](#345-what-does-unmerged-lora-cost-at-inference-time)
- [346: How do post-training quantization methods compare?](#346-how-do-post-training-quantization-methods-compare)
- [347: What is quantization-aware fine-tuning?](#347-what-is-quantization-aware-fine-tuning)
- [348: Why can fine-tuning remove a model's safety training?](#348-why-can-fine-tuning-remove-a-models-safety-training)
- [349: What are data poisoning and backdoor attacks on fine-tuning?](#349-what-are-data-poisoning-and-backdoor-attacks-on-fine-tuning)
- [350: How can a fine-tuned model leak its training data?](#350-how-can-a-fine-tuned-model-leak-its-training-data)
- [351: What is differentially private fine-tuning?](#351-what-is-differentially-private-fine-tuning)
- [352: What licensing traps exist with fine-tuned open-weight models?](#352-what-licensing-traps-exist-with-fine-tuned-open-weight-models)
- [353: What supply chain risks exist when fine-tuning?](#353-what-supply-chain-risks-exist-when-fine-tuning)
- [354: How do you design per-customer fine-tuning in a multi-tenant product?](#354-how-do-you-design-per-customer-fine-tuning-in-a-multi-tenant-product)
- [355: How do you handle data deletion requests for a trained model?](#355-how-do-you-handle-data-deletion-requests-for-a-trained-model)
- [356: How do you design an eval set that catches real regressions?](#356-how-do-you-design-an-eval-set-that-catches-real-regressions)
- [357: How do you know if an eval difference is real or noise?](#357-how-do-you-know-if-an-eval-difference-is-real-or-noise)
- [358: What biases do LLM judges have and how do you reduce them?](#358-what-biases-do-llm-judges-have-and-how-do-you-reduce-them)
- [359: How do you detect contamination between training data and evals?](#359-how-do-you-detect-contamination-between-training-data-and-evals)
- [360: What should a general-capability regression suite include?](#360-what-should-a-general-capability-regression-suite-include)
- [361: How does fine-tuning affect a model's calibration?](#361-how-does-fine-tuning-affect-a-models-calibration)
- [362: A fine-tuned support bot gives answers based on old policies. How do you fix it?](#362-a-fine-tuned-support-bot-gives-answers-based-on-old-policies-how-do-you-fix-it)
- [363: The fine-tuned model scores well offline but worse in production. What could be wrong?](#363-the-fine-tuned-model-scores-well-offline-but-worse-in-production-what-could-be-wrong)
- [364: The model produces valid JSON 97% of the time. How do you get to 100%?](#364-the-model-produces-valid-json-97-of-the-time-how-do-you-get-to-100)
- [365: After fine-tuning, the model got worse at multi-turn conversations. Why, and how do you fix it?](#365-after-fine-tuning-the-model-got-worse-at-multi-turn-conversations-why-and-how-do-you-fix-it)
- [366: You have only 500 labeled examples. What approach would you take?](#366-you-have-only-500-labeled-examples-what-approach-would-you-take)
- [367: How would you plan replacing a frontier model with a fine-tuned small model to cut costs?](#367-how-would-you-plan-replacing-a-frontier-model-with-a-fine-tuned-small-model-to-cut-costs)
- [368: Legal says no data can leave your infrastructure. How do you deliver an LLM feature with fine-tuning?](#368-legal-says-no-data-can-leave-your-infrastructure-how-do-you-deliver-an-llm-feature-with-fine-tuning)
- [369: Your fine-tuned model's base model is being shut down by the provider. What do you do?](#369-your-fine-tuned-models-base-model-is-being-shut-down-by-the-provider-what-do-you-do)
- [370: After DPO, the model's answers became much longer. Why, and how do you fix it?](#370-after-dpo-the-models-answers-became-much-longer-why-and-how-do-you-fix-it)
- [371: Training loss looks normal but the model outputs garbage. What do you check?](#371-training-loss-looks-normal-but-the-model-outputs-garbage-what-do-you-check)
- [372: Training is slow and GPU utilization is low. What could cause it?](#372-training-is-slow-and-gpu-utilization-is-low-what-could-cause-it)
- [373: Training crashes with out-of-memory only at certain steps. Why?](#373-training-crashes-with-out-of-memory-only-at-certain-steps-why)
- [374: Loss becomes NaN in fp16 training. What do you do?](#374-loss-becomes-nan-in-fp16-training-what-do-you-do)
- [375: The adapter loads without errors but the model behaves exactly like the base model. Why?](#375-the-adapter-loads-without-errors-but-the-model-behaves-exactly-like-the-base-model-why)
- [376: The model got worse after merging and quantizing. How do you find out why?](#376-the-model-got-worse-after-merging-and-quantizing-how-do-you-find-out-why)
- [377: You need a custom writing style for 200 business customers. How would you design it?](#377-you-need-a-custom-writing-style-for-200-business-customers-how-would-you-design-it)
- [378: You need to classify 1 million tickets per day cheaply. What would you build?](#378-you-need-to-classify-1-million-tickets-per-day-cheaply-what-would-you-build)
- [379: How would you design an internal fine-tuning platform for a company?](#379-how-would-you-design-an-internal-fine-tuning-platform-for-a-company)
- [380: What does CI/CD for fine-tuned models look like?](#380-what-does-cicd-for-fine-tuned-models-look-like)
- [381: How do you roll back a bad fine-tuned model quickly?](#381-how-do-you-roll-back-a-bad-fine-tuned-model-quickly)
- [382: Which metrics would you watch during a canary of a new fine-tuned model?](#382-which-metrics-would-you-watch-during-a-canary-of-a-new-fine-tuned-model)
- [383: What are the risks of training on your own model's feedback loop?](#383-what-are-the-risks-of-training-on-your-own-models-feedback-loop)
- [384: How do you detect drift after deploying a fine-tuned model?](#384-how-do-you-detect-drift-after-deploying-a-fine-tuned-model)
- [385: How do you calculate the break-even point of fine-tuning versus using a hosted model?](#385-how-do-you-calculate-the-break-even-point-of-fine-tuning-versus-using-a-hosted-model)
- [386: How do you choose GPUs for fine-tuning?](#386-how-do-you-choose-gpus-for-fine-tuning)
- [387: How do you use spot instances for training safely?](#387-how-do-you-use-spot-instances-for-training-safely)
- [388: How do you tune serving throughput for a fine-tuned model?](#388-how-do-you-tune-serving-throughput-for-a-fine-tuned-model)
- [389: How can fine-tuning help with speculative decoding?](#389-how-can-fine-tuning-help-with-speculative-decoding)
- [390: What makes tool-calling fine-tuning data really good?](#390-what-makes-tool-calling-fine-tuning-data-really-good)
- [391: How do you fine-tune an agent on trajectories?](#391-how-do-you-fine-tune-an-agent-on-trajectories)
- [392: Why should tool results be masked from the loss?](#392-why-should-tool-results-be-masked-from-the-loss)
- [393: How do you handle loss masking in multi-turn conversations?](#393-how-do-you-handle-loss-masking-in-multi-turn-conversations)
- [394: What should you keep in mind when fine-tuning reasoning models?](#394-what-should-you-keep-in-mind-when-fine-tuning-reasoning-models)
- [395: How do you combine continued pretraining and SFT?](#395-how-do-you-combine-continued-pretraining-and-sft)
- [396: How do you pick data mixing ratios?](#396-how-do-you-pick-data-mixing-ratios)
- [397: What is a warmup-stable-decay (WSD) schedule?](#397-what-is-a-warmup-stable-decay-wsd-schedule)
- [398: How do you choose LoRA rank empirically, and what happens if it's too high?](#398-how-do-you-choose-lora-rank-empirically-and-what-happens-if-its-too-high)
- [399: When should you train embedding and output layers with LoRA?](#399-when-should-you-train-embedding-and-output-layers-with-lora)
- [400: What alternatives to LoRA exist for partial training?](#400-what-alternatives-to-lora-exist-for-partial-training)
- [401: How do prompt tuning and prefix tuning compare with LoRA?](#401-how-do-prompt-tuning-and-prefix-tuning-compare-with-lora)
- [402: Can you fine-tune across organizations without sharing data?](#402-can-you-fine-tune-across-organizations-without-sharing-data)
- [403: What is machine unlearning, and can you rely on it?](#403-what-is-machine-unlearning-and-can-you-rely-on-it)
- [404: How can you see what fine-tuning changed in a model?](#404-how-can-you-see-what-fine-tuning-changed-in-a-model)
- [405: How does activation steering compare with fine-tuning?](#405-how-does-activation-steering-compare-with-fine-tuning)
- [406: How do you test robustness of a fine-tuned model?](#406-how-do-you-test-robustness-of-a-fine-tuned-model)
- [407: How do you measure hallucinations after fine-tuning?](#407-how-do-you-measure-hallucinations-after-fine-tuning)
- [408: What does an instruction-following regression look like, and how do you test it?](#408-what-does-an-instruction-following-regression-look-like-and-how-do-you-test-it)
- [409: How do you fine-tune embedding models with hard negatives?](#409-how-do-you-fine-tune-embedding-models-with-hard-negatives)
- [410: How do you fine-tune a reranker?](#410-how-do-you-fine-tune-a-reranker)
- [411: How does tokenization affect fine-tuning for code or non-English text?](#411-how-does-tokenization-affect-fine-tuning-for-code-or-non-english-text)
- [412: What problems come with multilingual fine-tuning, and how do you address them?](#412-what-problems-come-with-multilingual-fine-tuning-and-how-do-you-address-them)
- [413: What's different about fine-tuning vision-language models in depth?](#413-whats-different-about-fine-tuning-vision-language-models-in-depth)
- [414: What constraints apply when fine-tuning for on-device use?](#414-what-constraints-apply-when-fine-tuning-for-on-device-use)
- [415: How would you design a synthetic data pipeline at scale?](#415-how-would-you-design-a-synthetic-data-pipeline-at-scale)
- [416: What is rejection sampling fine-tuning?](#416-what-is-rejection-sampling-fine-tuning)
- [417: How do self-improvement loops like STaR work?](#417-how-do-self-improvement-loops-like-star-work)
- [418: What is RLAIF or AI feedback?](#418-what-is-rlaif-or-ai-feedback)
- [419: How do you write good annotation guidelines and measure label quality?](#419-how-do-you-write-good-annotation-guidelines-and-measure-label-quality)
- [420: How does label noise affect fine-tuning, and how do you handle it?](#420-how-does-label-noise-affect-fine-tuning-and-how-do-you-handle-it)
- [421: How do you handle severe class imbalance in LLM classification fine-tuning?](#421-how-do-you-handle-severe-class-imbalance-in-llm-classification-fine-tuning)
- [422: Which hyperparameters matter most in LLM fine-tuning?](#422-which-hyperparameters-matter-most-in-llm-fine-tuning)
- [423: How does performance scale with fine-tuning data size?](#423-how-does-performance-scale-with-fine-tuning-data-size)
- [424: How do you detect overfitting beyond validation loss?](#424-how-do-you-detect-overfitting-beyond-validation-loss)
- [425: What are checkpoint averaging and EMA, and do they help?](#425-what-are-checkpoint-averaging-and-ema-and-do-they-help)
- [426: Why aren't GPU training runs fully deterministic?](#426-why-arent-gpu-training-runs-fully-deterministic)
- [427: How do you debug a distributed training job that hangs?](#427-how-do-you-debug-a-distributed-training-job-that-hangs)
- [428: How do you handle very large fine-tuning datasets?](#428-how-do-you-handle-very-large-fine-tuning-datasets)
- [429: What can go wrong when converting a fine-tuned model to GGUF?](#429-what-can-go-wrong-when-converting-a-fine-tuned-model-to-gguf)
- [430: How do you set the prompt template for a fine-tuned model in Ollama?](#430-how-do-you-set-the-prompt-template-for-a-fine-tuned-model-in-ollama)
- [431: How do you expose a self-hosted fine-tuned model safely to your web app?](#431-how-do-you-expose-a-self-hosted-fine-tuned-model-safely-to-your-web-app)
- [432: How would you design fallbacks for a fine-tuned model?](#432-how-would-you-design-fallbacks-for-a-fine-tuned-model)
- [433: How do model cascades with fine-tuned models work?](#433-how-do-model-cascades-with-fine-tuned-models-work)
- [434: How have the economics of fine-tuning changed by 2026?](#434-how-have-the-economics-of-fine-tuning-changed-by-2026)
- [435: Why have some providers reduced their fine-tuning offerings?](#435-why-have-some-providers-reduced-their-fine-tuning-offerings)
- [436: How do you avoid vendor lock-in with fine-tuned models?](#436-how-do-you-avoid-vendor-lock-in-with-fine-tuned-models)
- [437: What should a model card for an internal fine-tuned model contain?](#437-what-should-a-model-card-for-an-internal-fine-tuned-model-contain)
- [438: What regulatory issues might apply to fine-tuned models?](#438-what-regulatory-issues-might-apply-to-fine-tuned-models)
- [439: How do you red-team a fine-tuned model?](#439-how-do-you-red-team-a-fine-tuned-model)
- [440: How do you check a fine-tuned model for unfair behavior?](#440-how-do-you-check-a-fine-tuned-model-for-unfair-behavior)
- [441: Who should own what in a fine-tuning project team?](#441-who-should-own-what-in-a-fine-tuning-project-team)
- [442: How would you design an experiment to prove fine-tuning beats prompting?](#442-how-would-you-design-an-experiment-to-prove-fine-tuning-beats-prompting)
- [443: What ablations would you run on a fine-tuning setup?](#443-what-ablations-would-you-run-on-a-fine-tuning-setup)
- [444: How would you describe a fine-tuning project in an interview?](#444-how-would-you-describe-a-fine-tuning-project-in-an-interview)
- [445: How do you future-proof a fine-tuning pipeline?](#445-how-do-you-future-proof-a-fine-tuning-pipeline)
- [446: When should you stop investing in fine-tuning for a use case?](#446-when-should-you-stop-investing-in-fine-tuning-for-a-use-case)
- [447: What are common anti-patterns in fine-tuning projects?](#447-what-are-common-anti-patterns-in-fine-tuning-projects)
- [448: What is your checklist before shipping a fine-tuned model?](#448-what-is-your-checklist-before-shipping-a-fine-tuned-model)
- [449: How would you explain why a fine-tuned model is not the same as a "trained-on-our-data" chatbot?](#449-how-would-you-explain-why-a-fine-tuned-model-is-not-the-same-as-a-trained-on-our-data-chatbot)
- [450: How has fine-tuning practice changed in the last few years?](#450-how-has-fine-tuning-practice-changed-in-the-last-few-years)

---

# Easy Questions (1-150)

## 1: What is fine-tuning an LLM?

Fine-tuning means taking a model that is already trained and training it a bit more on your own examples. The model's weights change, so the new behavior is built into the model instead of being written in the prompt each time.

You usually do it to make a model follow a specific format, write in a specific style or do one narrow task well.

## 2: How is fine-tuning different from pretraining?

Pretraining is the first, huge training run. The model reads trillions of tokens of text and learns language, facts and general patterns. It costs millions of dollars and only big labs do it.

Fine-tuning starts from that pretrained model and trains it on a much smaller dataset, often a few hundred to a few hundred thousand examples. It takes hours, not months, and a normal team can do it.

## 3: What is a base model?

A base model is the model right after pretraining. It is good at continuing text, but it does not follow instructions well. If you ask it a question, it may write more questions instead of an answer.

Base models are named things like `Qwen3-8B-Base` or `Llama-3.1-8B`. They are a good starting point when you want full control over the format the model learns.

## 4: What is an instruct or chat model?

An instruct model is a base model that was already fine-tuned by the lab to follow instructions and hold a conversation. It knows about roles like system, user and assistant, and it answers questions instead of just continuing text.

Most teams fine-tune an instruct model, because it already behaves well and needs fewer examples to learn your task.

## 5: Why would a team fine-tune a model?

Common reasons:

- Get a consistent output format or tone that prompting can't hold reliably.
- Make a small, cheap model do one task as well as a big expensive one.
- Cut long prompts, which lowers cost and latency.
- Run the model on your own servers for privacy reasons and still get good quality.
- Teach a skill that is hard to explain in words but easy to show with examples.

## 6: When should you not fine-tune?

Don't fine-tune when good prompting already solves the problem, when you don't have good examples, or when the main need is up-to-date facts. Facts change, and retraining every time a document changes is slow and expensive. RAG is the better tool for that.

Also skip it if you can't measure quality. Without an eval set you won't know if the fine-tuned model is better or worse.

## 7: What is the difference between prompt engineering and fine-tuning?

Prompt engineering changes what you send to the model. Fine-tuning changes the model itself.

Prompting is fast to try, free to change and needs no training. Fine-tuning takes data, time and money, but the behavior sticks without long instructions in every request. Always try prompting first. Fine-tune only when prompting hits a limit.

## 8: What is the difference between RAG and fine-tuning?

RAG (retrieval-augmented generation) looks up relevant documents at request time and puts them in the prompt. The model's weights don't change.

Fine-tuning changes the weights using examples. A simple rule: use RAG to give the model knowledge, and fine-tuning to change how it behaves (format, style, task skill). Many real systems use both.

## 9: Can fine-tuning teach a model new facts?

A little, but badly. The model may remember some facts after seeing them many times, but it often mixes them up, and you can't easily update or remove them later. Research also shows that training on facts the model doesn't know can make it hallucinate more.

If the goal is "the model should know our product docs", use RAG. Fine-tuning is better for teaching how to answer than what to know.

## 10: What is supervised fine-tuning (SFT)?

SFT is the most common type of fine-tuning. You give the model pairs of input and the correct output, and train it to produce that output for that input.

It's called "supervised" because every example has a known right answer that you wrote or picked. Most fine-tuning projects start with SFT.

## 11: What does one SFT training example look like?

For a chat model, one example is a short conversation where the last assistant message is the answer you want the model to learn:

```json
{
  "messages": [
    {
      "role": "system",
      "content": "You extract order IDs from emails. Reply with JSON only."
    },
    { "role": "user", "content": "Hi, my order 48213 never arrived." },
    { "role": "assistant", "content": "{\"order_id\": \"48213\"}" }
  ]
}
```

The model learns to write the assistant part when it sees the system and user parts.

## 12: What is the conversational or messages format?

It is a list of messages, each with a `role` (`system`, `user`, `assistant`, sometimes `tool`) and `content`. Hugging Face TRL, most hosted services and most chat APIs use this shape.

The library turns this list into one long string using the model's chat template, so you don't have to add the special tokens by hand.

## 13: What is JSONL and why is it used for training data?

JSONL (JSON Lines) is a text file where each line is one complete JSON object. Each line is one training example.

It's popular because you can stream it line by line, append new examples easily and spot a broken line quickly. Most fine-tuning tools and services accept it.

## 14: How many examples do you need to fine-tune?

It depends on the task. For a format or style change, 100 to 1,000 good examples often work with LoRA. For a harder skill, you may need tens of thousands.

A practical approach: start with a few hundred, train, measure, then double the data and see if the scores still go up. If they stop going up, more of the same data won't help.

## 15: Why does data quality matter more than quantity?

The model copies what it sees. If 10% of your examples have wrong answers or sloppy formatting, the model learns to be wrong or sloppy 10% of the time.

A small set of clean, consistent examples usually beats a large set of messy ones. Spend time reading your data before you spend money on GPUs.

## 16: What are training, validation and test sets?

- **Training set:** examples the model learns from.
- **Validation set:** examples you check during training to see if the model is improving or overfitting. You use it to pick settings and checkpoints.
- **Test set:** examples you look at only at the end, to get an honest score.

None of these should overlap. A common split is around 80/10/10, but with small datasets people often keep a fixed test set of 100 to 500 examples and use the rest for training.

## 17: What is a parameter or weight in a model?

A parameter (or weight) is one number inside the model. The model is basically billions of these numbers arranged in matrices. During training, the numbers are nudged a little so the model's outputs get closer to the right answers.

Fine-tuning changes these numbers, either all of them or a small extra set.

## 18: What does "8B" or "70B" mean in a model name?

It's the number of parameters: 8 billion or 70 billion. More parameters usually means a smarter model, but also more memory, slower answers and more expensive training.

As a rough guide, each parameter takes 2 bytes in 16-bit precision, so an 8B model needs about 16 GB just to load the weights.

## 19: What is full fine-tuning?

Full fine-tuning updates every weight in the model. It gives the most freedom to change the model, but it needs a lot of GPU memory, because you store gradients and optimizer state for every parameter. The saved result is a full copy of the model.

For most application work, people use LoRA instead, because it's much cheaper and often close in quality.

## 20: What is parameter-efficient fine-tuning (PEFT)?

PEFT is a group of methods that train only a small number of new or chosen parameters and keep the rest of the model frozen. LoRA is the most popular one.

Because only a tiny part is trained, PEFT uses much less memory, trains faster and produces small files. `PEFT` is also the name of the Hugging Face library that implements these methods.

## 21: What is LoRA?

LoRA (Low-Rank Adaptation) freezes the original weights and adds two small matrices next to some of the weight matrices. Only the small matrices are trained. Their product is a small "change" that gets added to the original weights.

The result is that you train maybe 0.1% to 2% of the parameters, use far less memory, and save an adapter file of a few megabytes to a few hundred megabytes instead of a full model.

## 22: What is an adapter?

An adapter is the small set of trained weights that PEFT methods like LoRA produce. You load the base model, then load the adapter on top of it to get the fine-tuned behavior.

Since adapters are small, you can keep many of them (for example, one per customer or task) and share one base model between them.

## 23: What is QLoRA?

QLoRA is LoRA on top of a base model loaded in 4-bit precision. The frozen base weights are stored in 4 bits to save memory, while the LoRA adapters are trained in 16-bit.

This lets you fine-tune much bigger models on one GPU. For example, an 8B model fits easily on a 24 GB card with QLoRA. It's a bit slower than plain LoRA and can lose a little quality.

## 24: What is quantization?

Quantization stores the model's weights with fewer bits, for example 8 or 4 bits instead of 16. The model gets smaller and often faster, but loses some accuracy.

In fine-tuning, quantization is used in QLoRA during training, and often again after training to make the model cheaper to serve.

## 25: What is the rank in LoRA?

The rank, usually called `r`, is the size of the small matrices LoRA adds. A higher rank means more trainable parameters and more room to learn, but also more memory and a bigger adapter.

Common values are 8, 16, 32 and 64. For simple format or style tasks, 8 or 16 is usually enough.

## 26: What is an epoch?

One epoch is one full pass over the whole training set. If you have 1,000 examples and train for 3 epochs, the model sees each example 3 times.

For LLM fine-tuning, 1 to 3 epochs is typical. More epochs on a small dataset quickly leads to overfitting.

## 27: What is batch size?

Batch size is how many examples the model looks at before it updates its weights once. Bigger batches give smoother, more stable updates but need more GPU memory.

When memory is tight, people use a small batch size and gradient accumulation to get the same effect as a bigger batch.

## 28: What is the learning rate?

The learning rate controls how big each weight update is. Too high and training becomes unstable or the model forgets what it knew. Too low and it barely learns.

For LoRA, values around `1e-4` to `2e-4` are common starting points. Full fine-tuning uses much smaller values, around `1e-5` or lower.

## 29: What is loss?

Loss is a number that says how wrong the model's predictions are on the training examples. For LLMs it's usually cross-entropy: how surprised the model is by the correct next token.

Training tries to push the loss down. Lower loss means the model predicts your target answers better.

## 30: What is the difference between training loss and validation loss?

Training loss is measured on the examples the model is learning from. Validation loss is measured on examples it never trains on.

If both go down, the model is learning something general. If training loss keeps going down but validation loss starts going up, the model is memorizing the training set instead of learning the task.

## 31: What is overfitting?

Overfitting is when the model learns the training examples too well, including their quirks, and gets worse on new inputs. Signs are a very low training loss, a rising validation loss, and outputs that copy training answers word for word.

Fixes include fewer epochs, a lower learning rate, more varied data, and stopping at an earlier checkpoint.

## 32: What is underfitting?

Underfitting is when the model hasn't learned the task well enough. Both training and validation loss stay high, and outputs don't follow the format or style you trained for.

Common causes are too few steps, a learning rate that's too low, a LoRA rank that's too small, or a data or template bug that hides the real target from the model.

## 33: What is catastrophic forgetting?

It's when a model loses skills it had before because fine-tuning pushed its weights too far toward the new task. For example, after training on short JSON outputs, the model may get worse at normal conversation or at reasoning.

You reduce it with LoRA, a lower learning rate, fewer epochs and by mixing some general examples into your training data.

## 34: What is a checkpoint?

A checkpoint is a saved copy of the model (or adapter) at a certain step during training. Trainers usually save one every N steps or at the end of each epoch.

Checkpoints let you resume after a crash and pick the best version, which is often not the last one.

## 35: What is a tokenizer?

A tokenizer turns text into tokens (numbers the model understands) and turns tokens back into text. Every model has its own tokenizer, and you must always use the one that matches your base model.

During fine-tuning, the tokenizer also applies the chat template and adds special tokens like the end-of-turn marker.

## 36: Why do tokens matter in fine-tuning?

Training cost and time depend on the total number of tokens, not the number of examples. Ten thousand short examples can be cheaper than one thousand long ones.

Tokens also matter for the max sequence length. Examples longer than the limit get cut off, and the model may never see the end of the answer.

## 37: What is a chat template?

A chat template is a small piece of code, stored with the tokenizer, that turns a list of messages into the exact text format the model was trained on. It adds the special tokens that mark where each role starts and ends.

You must use the same template during fine-tuning and at inference time. A mismatch is one of the most common reasons a fine-tuned model behaves strangely.

## 38: What is the max sequence length?

It's the longest example, in tokens, that you allow during training. Longer examples are cut off (truncated) or dropped.

A longer limit uses more GPU memory. Pick a value that fits almost all your examples, for example the 99th percentile of your token lengths, and check what happens to the few that are longer.

## 39: Why do you need a GPU to fine-tune?

Training means doing a huge number of matrix multiplications. GPUs do these in parallel and are many times faster than CPUs.

You can fine-tune tiny models on a laptop, and Apple Silicon Macs work for small LoRA jobs with MLX. For anything around 7B parameters or bigger, a modern NVIDIA GPU is the normal choice.

## 40: What is VRAM and why does it limit fine-tuning?

VRAM is the GPU's own memory. The model weights, the gradients, the optimizer state and the activations for each batch all have to fit in it.

If they don't fit, you get an "out of memory" error. That's why tricks like LoRA, QLoRA, smaller batches and gradient checkpointing exist: they all reduce how much VRAM training needs.

## 41: What is the Hugging Face Hub?

The Hugging Face Hub is a website and service that hosts models, datasets and demo apps. Most open-weight models are published there.

In fine-tuning you use it to download base models, find datasets, and upload your own adapters or models (public or private).

## 42: What is the Transformers library?

`transformers` is Hugging Face's Python library for loading and running models. It gives you classes like `AutoModelForCausalLM` and `AutoTokenizer` that load almost any open model by name.

Most fine-tuning tools, including TRL, PEFT, Unsloth and Axolotl, are built on top of it.

## 43: What is TRL?

TRL (Transformers Reinforcement Learning) is Hugging Face's library for post-training LLMs. It has trainers for the common methods: `SFTTrainer` for supervised fine-tuning, `DPOTrainer` for preference tuning, `GRPOTrainer` for reinforcement learning, and `RewardTrainer` for reward models.

TRL reached version 1.0 in 2026 and now separates stable trainers from experimental ones.

## 44: What is the PEFT library?

`peft` is Hugging Face's library for parameter-efficient methods like LoRA. You describe the adapter with a config (for example `LoraConfig`), and the library adds the trainable parts to the model.

It also handles saving, loading and merging adapters. TRL accepts a `peft_config` directly, so you rarely call PEFT by hand in simple setups.

## 45: What is Unsloth?

Unsloth is an open-source library that makes LoRA and QLoRA fine-tuning faster and lighter on memory by using custom GPU kernels. It works with Hugging Face models and TRL trainers.

It's popular for fine-tuning on a single GPU or in free notebooks, and it has many ready-made notebooks for common models.

## 46: What is Axolotl?

Axolotl is an open-source tool where you describe the whole fine-tuning run in a YAML file: base model, dataset, LoRA settings, learning rate and so on. Then you run it with one command.

It's useful when you want repeatable runs without writing Python training code, and it supports multi-GPU setups.

## 47: What is LLaMA-Factory?

LLaMA-Factory is another open-source fine-tuning tool. It supports many models and methods (SFT, DPO, LoRA, QLoRA and more) and has both a command line and a web UI.

It's handy for people who want to try fine-tuning through a UI before writing any code.

## 48: What are open-weight models?

Open-weight models are models whose weights you can download and run yourself. Examples include Llama, Qwen, Gemma, Mistral and gpt-oss.

You can fine-tune them however you want, within their license. That's why most hands-on fine-tuning today happens on open-weight models.

## 49: Should you fine-tune an open-weight model or a hosted closed model?

Open-weight fine-tuning gives you full control: any method, your own servers, no vendor shutting down the feature. But you handle GPUs, serving and updates yourself.

Hosted fine-tuning is easier to start, but you get fewer options, you depend on the provider, and the model can only run on their platform. In 2026 several big providers have reduced or closed their fine-tuning offers, which is a strong reason to prefer open weights when fine-tuning is important to you.

## 50: Which hosted services let you fine-tune models in late 2026?

- **Google Vertex AI:** supervised and preference tuning for some Gemini models.
- **OpenAI:** closing. No new users since May 2026, and new training jobs stop on January 6, 2027.
- **Anthropic:** the Claude API doesn't offer fine-tuning.
- **Open-model platforms** such as Together AI, Fireworks AI and others: LoRA or full fine-tuning of open-weight models, and serving of the result.

This changes often, so always check the provider docs before you plan a project.

## 51: Can you fine-tune Claude?

Not through the Claude API. Anthropic's docs say the API doesn't offer fine-tuning. There used to be fine-tuning for Claude 3 Haiku on Amazon Bedrock, but that model has been retired.

If you use Claude, you customize behavior with system prompts, examples in the prompt, prompt caching, tools and RAG instead.

## 52: What happened to OpenAI fine-tuning?

In May 2026 OpenAI announced it's winding down its fine-tuning platform. New organizations can no longer use it, and existing customers can create training jobs only until January 6, 2027, or earlier if the base model is shut down first.

Fine-tuned models keep working until their base model is retired. Teams that relied on it are moving to open-weight models or to better prompting.

## 53: Can you fine-tune Gemini?

Yes, through Google Cloud Vertex AI. It supports supervised fine-tuning on some Gemini models, and also preference tuning. The list of supported models changes, so check the "supported models" section of the Vertex AI tuning docs.

The tuned model runs on Vertex AI and is called through a tuned model endpoint.

## 54: What does a hosted fine-tuning service do for you?

You upload a dataset, pick a base model and a few settings, and the service runs the training on its GPUs. When it's done, you get a model ID you can call through an API.

It saves you from managing GPUs, drivers, distributed training and serving. The trade-off is less control, higher cost per run and being tied to that provider.

## 55: What is instruction tuning?

Instruction tuning is SFT on many different instruction and answer pairs, so the model learns to follow instructions in general. This is how labs turn a base model into an instruct model.

When you fine-tune for your own app, you usually do narrow task tuning on top of an instruct model that already went through instruction tuning.

## 56: What is alignment?

Alignment means training a model to behave the way people want: helpful, honest, safe, and following instructions. It usually happens after pretraining, using SFT and then preference or reinforcement methods.

When you fine-tune, you can weaken the lab's alignment by accident, for example by training on examples that never refuse anything.

## 57: What is RLHF?

RLHF (reinforcement learning from human feedback) is a training method where people compare model answers and pick the better one. Those choices train a reward model, and then reinforcement learning pushes the LLM toward answers the reward model likes.

It was key in making early chat models helpful. Today simpler methods like DPO are often used instead for preference tuning.

## 58: What is a reward model?

A reward model is a model that reads a prompt and an answer and outputs a score for how good the answer is. It's trained on preference data, where people marked which of two answers was better.

In RLHF the reward model acts as an automatic judge during training. TRL has a `RewardTrainer` for training one.

## 59: What is DPO?

DPO (Direct Preference Optimization) trains a model on pairs of answers to the same prompt: a "chosen" (better) one and a "rejected" (worse) one. The model learns to make the chosen answer more likely than the rejected one.

It gets similar results to RLHF but without a separate reward model or a reinforcement learning loop, so it's much simpler to run. TRL has a `DPOTrainer`.

## 60: What does preference data look like?

Each example has a prompt and two answers, one marked as better:

```json
{
  "prompt": [
    { "role": "user", "content": "Summarize this ticket in one line: ..." }
  ],
  "chosen": [
    {
      "role": "assistant",
      "content": "Customer can't log in after password reset."
    }
  ],
  "rejected": [
    {
      "role": "assistant",
      "content": "The customer wrote a long message about several things including..."
    }
  ]
}
```

You can get these pairs from people rating answers, from user thumbs up and down, or from a stronger model acting as judge.

## 61: Should the system prompt be in the training data?

If you'll use a system prompt in production, include the same one (or a very similar one) in your training examples. The model learns to behave a certain way when it sees that prompt.

Many teams use a short system prompt in training so they can drop the long instructions they used before fine-tuning. Whatever you choose, keep training and production consistent.

## 62: How do few-shot prompts relate to fine-tuning?

Few-shot prompting puts a few examples in the prompt to show the model what you want. Fine-tuning is like baking hundreds or thousands of such examples into the weights.

A good test before fine-tuning: if few-shot examples help a lot, fine-tuning on more of the same examples will probably help too.

## 63: What is inference?

Inference means using the model to generate output, as opposed to training it. Every API call to a model is an inference request.

After fine-tuning, inference cost and speed matter a lot, because you pay for inference on every request, but you pay for training only once per version.

## 64: What is an eval?

An eval is a set of test inputs plus a way to score the model's outputs. The score might be exact match, a JSON schema check, a unit test, or a judgment from a person or another model.

You need an eval before you fine-tune, so you can compare the base model, the prompted model and the fine-tuned model on the same tasks.

## 65: What is a baseline?

A baseline is the score you're trying to beat. For fine-tuning, the usual baselines are the base model with a good prompt, and maybe a bigger model with a good prompt.

If the fine-tuned model doesn't clearly beat the baseline on your eval, the fine-tuning wasn't worth it.

## 66: What is a hyperparameter?

A hyperparameter is a setting you choose before training, not something the model learns. Examples are learning rate, number of epochs, batch size, LoRA rank and max sequence length.

Picking good hyperparameters often matters as much as the data. Start with known defaults and change one thing at a time.

## 67: What does a fine-tuning run cost?

The main cost is GPU time: number of GPUs times hours times the hourly price. A LoRA run on an 8B model with a few thousand examples can finish in under an hour on one cloud GPU and cost a few dollars.

Larger models, full fine-tuning and big datasets cost much more. Don't forget the hidden costs: preparing data, running evals and serving the model afterwards.

## 68: What is mixed precision training?

Mixed precision means doing most of the math in 16-bit numbers instead of 32-bit, which saves memory and runs faster on modern GPUs. Some parts that need more accuracy are still kept in 32-bit.

In Hugging Face trainers you turn it on with `bf16=True` (or `fp16=True` on older GPUs).

## 69: What is the difference between fp16 and bf16?

Both are 16-bit number formats. `fp16` has more precision but a small range, so very large or very small values can overflow and break training (you see `NaN` loss). `bf16` has the same range as 32-bit floats but less precision, so it's much more stable.

Use `bf16` on GPUs that support it (NVIDIA Ampere, like the A100, and newer). Use `fp16` only on older cards.

## 70: What is a gradient?

A gradient tells you, for each weight, which direction to change it to make the loss smaller, and how strongly. Training computes gradients and then moves each weight a small step in the right direction.

Storing gradients takes memory, which is one reason full fine-tuning is so memory hungry.

## 71: What is backpropagation?

Backpropagation is how the model computes gradients. It runs the input forward to get a prediction and a loss, then goes backward through the layers to work out how much each weight contributed to the error.

You never write it yourself. PyTorch does it automatically when the trainer calls `loss.backward()`.

## 72: What is an optimizer like AdamW?

The optimizer decides how to update the weights using the gradients. AdamW is the default for LLM training. It keeps a running average of past gradients for each weight, which makes updates smoother.

The downside is memory: AdamW stores two extra values per trained parameter. With LoRA this is small, because few parameters are trained.

## 73: What is learning rate warmup?

Warmup means starting with a very small learning rate and raising it to the target value over the first few steps (for example the first 3% to 10% of training).

It prevents big, unstable updates at the start, when the optimizer hasn't built up its statistics yet.

## 74: What is a learning rate scheduler?

A scheduler changes the learning rate during training. A common pattern is warmup, then slowly lowering the rate until the end. "Cosine" and "linear" decay are the usual choices.

Lowering the rate near the end helps the model settle into a good state instead of bouncing around.

## 75: What is gradient accumulation?

Gradient accumulation adds up gradients over several small batches before doing one weight update. It gives you the effect of a big batch while only keeping a small batch in memory.

For example, `per_device_train_batch_size=2` with `gradient_accumulation_steps=8` behaves like a batch of 16 on one GPU.

## 76: What is gradient checkpointing?

Normally the model stores all intermediate results (activations) from the forward pass so it can use them in the backward pass. Gradient checkpointing throws most of them away and recomputes them when needed.

It saves a lot of memory, especially with long sequences, at the cost of about 20% to 30% slower training. Turn it on with `gradient_checkpointing=True`.

## 77: What is a model card?

A model card is a README for a model. It describes what the model is for, how it was trained, what data was used, how it was evaluated, its limits and its license.

When you publish or share a fine-tuned model, even inside your company, write a model card so others know what they're using.

## 78: Why does the license matter when fine-tuning?

Open-weight models come with licenses that limit what you can do. Some, like Apache 2.0, allow almost anything. Others have extra rules, for example on company size, naming, or acceptable use.

Your fine-tuned model usually inherits the base model's license. Check it before you build a product on top, and check the terms of any data you train on too.

## 79: What is synthetic data?

Synthetic data is training data that a model generates instead of people. For example, you ask a big model to write 5,000 customer questions and good answers, then use them to fine-tune a small model.

It's fast and cheap, but it can be repetitive or contain mistakes, so you need to filter and review it.

## 80: What is distillation?

Distillation means training a smaller model to copy a bigger model's behavior. The big model (the teacher) produces answers, and the small model (the student) is fine-tuned on them.

The goal is to get most of the big model's quality on your task at a fraction of the cost and latency. Check the teacher model's terms of use first, because some providers don't allow using their outputs to train competing models.

## 81: What are teacher and student models?

In distillation, the teacher is the strong, expensive model that produces the target answers. The student is the smaller model you fine-tune to imitate it.

The student usually doesn't reach the teacher's quality in general, but on one narrow task it can get very close.

## 82: What is continued pretraining?

Continued pretraining (also called domain adaptation) means training a model further on a lot of raw text from a specific field, like legal documents or medical papers, before doing SFT.

It helps the model get used to domain words and writing style. It needs much more data than SFT (millions of tokens or more), and it can hurt instruction following, so it's usually followed by SFT.

## 83: Can you fine-tune an LLM for classification?

Yes. You can train it to output a label as text (for example `"refund"` or `"shipping"`), which is just normal SFT.

You can also add a classification head and train it to output label scores directly with `AutoModelForSequenceClassification`. For simple classification, a small encoder model like BERT or ModernBERT is often cheaper and just as accurate.

## 84: What does merging an adapter mean?

Merging adds the LoRA weights into the base model's weights, so you get one normal model with no separate adapter. In PEFT you call `merge_and_unload()`.

A merged model is a bit faster at inference and easier to export to formats like GGUF. The downside is that you lose the small adapter file and need to store a full model per fine-tune.

## 85: What is safetensors?

`safetensors` is a file format for storing model weights. Unlike the old PyTorch pickle format, it can't run code when loaded, so it's safe to load files from strangers. It's also fast to load.

It's the default format on the Hugging Face Hub. Prefer it over `.bin` or `.pt` files.

## 86: What is GGUF?

GGUF is a file format used by llama.cpp and tools built on it, like Ollama and LM Studio. It stores a model, usually quantized, in one file together with its tokenizer and chat template.

After fine-tuning, people often merge the adapter and convert the model to GGUF so it can run on laptops or small servers.

## 87: Can you run a fine-tuned model in Ollama?

Yes. You can convert a merged model to GGUF and import it with a `Modelfile`, or load a LoRA adapter on top of a supported base model using the `ADAPTER` instruction:

```
FROM llama3.1:8b
ADAPTER ./my-lora-adapter
```

Then run `ollama create my-model -f Modelfile` and use it like any other Ollama model.

## 88: What is vLLM?

vLLM is an open-source server for running LLMs fast. It batches many requests together, manages memory well and exposes an OpenAI-compatible HTTP API.

It can serve LoRA adapters on top of a base model, including many adapters at once, which makes it a common choice for serving fine-tuned models in production.

## 89: Can you fine-tune on a Mac?

Yes, for smaller models. Apple's MLX framework and the `mlx-lm` package support LoRA fine-tuning on Apple Silicon:

```bash
pip install mlx-lm
mlx_lm.lora --model Qwen/Qwen3-1.7B --train --data ./data --iters 500
```

It's fine for learning and for small models. For bigger models or serious runs, a cloud NVIDIA GPU is faster.

## 90: Can you fine-tune in Google Colab?

Yes. A free or paid Colab GPU is enough to run QLoRA on small models (roughly up to 8B parameters, depending on the GPU and sequence length). Unsloth and Hugging Face publish many ready-made Colab notebooks.

It's a good place to learn. For real projects, use a machine where runs don't get cut off after a time limit.

## 91: What is data labeling?

Data labeling means attaching the correct answer to each input, for example writing the ideal reply to a customer message or marking the right category.

Labels can come from experts, from your existing system's logs, or from a strong model checked by people. The quality of your labels sets the upper limit for your fine-tuned model.

## 92: What does "garbage in, garbage out" mean for fine-tuning?

It means the model can only be as good as its training data. If your examples have typos, wrong facts, inconsistent formats or lazy answers, the model learns all of that.

Fine-tuning doesn't fix bad data. It copies it, very reliably.

## 93: What is PII and why remove it from training data?

PII (personally identifiable information) is data like names, emails, phone numbers, addresses and ID numbers. Models can memorize parts of their training data and repeat them later to other users.

Remove or mask PII before training, unless you have a clear legal reason and permission to keep it.

## 94: What is deduplication and why do it?

Deduplication removes repeated or nearly repeated examples from your dataset. If the same example appears 50 times, the model overweights it and may memorize it.

It also stops the same example from ending up in both training and test sets, which would make your eval scores look better than they really are.

## 95: What is data leakage between train and test sets?

Leakage happens when test examples, or very similar ones, are also in the training data. The model has basically seen the answers, so the test score is too high and doesn't reflect real performance.

Split your data before you augment or generate variations, and dedupe across the splits.

## 96: Does fine-tuning fix hallucinations?

Not really. Fine-tuning can teach the model to say "I don't know" more often or to stick to provided context, which helps. But it doesn't give the model reliable knowledge, and training on facts it doesn't know can make hallucinations worse.

For factual accuracy, combine fine-tuning with RAG and good evals.

## 97: Does fine-tuning change temperature or other sampling settings?

No. Temperature, top-p and max tokens are settings you choose at inference time. Fine-tuning changes the model's probabilities, but you still control how you sample from them.

A fine-tuned model for structured output often works best with low temperature, because you want the most likely answer every time.

## 98: What is the EOS token?

EOS (end of sequence) is a special token that tells the model to stop generating. Chat models also have end-of-turn tokens that mark where the assistant's message ends.

If your training data doesn't include the right end token after each answer, the fine-tuned model may never stop and keep writing until it hits the max token limit.

## 99: What is padding?

When several examples of different lengths are put in one batch, the short ones are filled with a padding token so they all have the same length. The model is told to ignore the padding.

Padding wastes compute. Packing several short examples into one sequence is one way to avoid it.

## 100: What is a random seed and why set it?

A seed controls the random choices in training, like how data is shuffled and how the new LoRA weights start. Setting the seed (for example `seed=42`) makes runs easier to repeat.

GPU training is still not perfectly deterministic, but a fixed seed reduces the noise when you compare two settings.

## 101: What is experiment tracking?

Experiment tracking means logging every training run: its settings, data version, loss curves and eval scores. Tools like Weights & Biases, MLflow and TensorBoard do this.

Without it, after ten runs you won't remember which settings gave the best model. In Hugging Face trainers, you turn it on with `report_to="wandb"` or a similar value.

## 102: What is TensorBoard?

TensorBoard is a free tool for viewing training logs as charts, such as loss over time and learning rate. It runs locally in your browser.

Set `report_to="tensorboard"` in the training config, then run `tensorboard --logdir <output_dir>`.

## 103: How big is a LoRA adapter compared to the full model?

Much smaller. An 8B model in 16-bit is about 16 GB. A LoRA adapter for it with rank 16 on all linear layers is usually tens of megabytes to a couple hundred megabytes.

That's why you can keep many adapters for different tasks and swap them cheaply.

## 104: Can you use more than one LoRA adapter at a time?

Yes. PEFT can load several adapters on the same base model and switch between them by name. Some setups also combine adapters by adding them together with weights.

Servers like vLLM can serve different adapters to different requests on the same base model at the same time.

## 105: What are target modules in LoRA?

Target modules are the layers where LoRA adds its small matrices, usually the attention projections (`q_proj`, `k_proj`, `v_proj`, `o_proj`) and the MLP layers (`gate_proj`, `up_proj`, `down_proj`).

Targeting all linear layers (`target_modules="all-linear"` in PEFT) usually gives the best quality. Targeting fewer layers saves memory.

## 106: What is lora_alpha?

`lora_alpha` is a scaling factor for the LoRA update. The change added to the weights is multiplied by `lora_alpha / r`.

A common rule is to set `lora_alpha` to `r` or `2 * r`. If you change the rank, keep the ratio about the same so you don't also need to change the learning rate.

## 107: What is dropout in LoRA?

`lora_dropout` randomly turns off part of the LoRA input during training, which helps against overfitting. Typical values are 0 to 0.1.

With large, varied datasets, people often set it to 0. With small datasets, 0.05 or 0.1 can help.

## 108: What is weight decay?

Weight decay slowly pulls the trained weights toward zero during training. It's a simple way to stop weights from growing too big and to reduce overfitting.

Typical values are 0 to 0.1. It matters less for LoRA than for full fine-tuning.

## 109: What is early stopping?

Early stopping means ending training when the validation score stops improving, instead of running all planned epochs. It prevents overfitting and saves GPU time.

In Hugging Face you can use `EarlyStoppingCallback` together with `load_best_model_at_end=True`, or just save checkpoints and pick the best one yourself.

## 110: What is perplexity?

Perplexity is a way to show the loss as an easier number: it's `exp(loss)`. Lower is better. Roughly, it says how many tokens the model is "choosing between" at each step.

It's useful for comparing runs on the same data, but it doesn't tell you if the answers are actually correct or useful. You still need a task eval.

## 111: What is a held-out test set?

It's a set of examples kept completely separate from training and from hyperparameter tuning. You use it only at the end to measure real quality.

If you keep tuning settings against the test set, it slowly turns into a validation set and stops giving an honest score.

## 112: Why is human evaluation still needed?

Automatic metrics miss a lot: tone, helpfulness, subtle errors and whether the answer actually solves the user's problem. Reading outputs yourself catches issues no metric shows.

At minimum, read a random sample of outputs from the base model and the fine-tuned model side by side before shipping.

## 113: What is LLM-as-a-judge?

It means using a strong model to score or compare outputs, for example "Which of these two answers is more accurate? Answer A or B." It's much cheaper and faster than human review.

Judges have biases (they prefer longer answers or the first option), so test the judge against some human labels before you trust it.

## 114: What is A/B testing a fine-tuned model?

You send part of real traffic to the fine-tuned model and part to the current model, then compare real outcomes like resolution rate, user ratings, errors or conversions.

Offline evals tell you if a model is likely better. An A/B test tells you if it's better for real users.

## 115: Why version datasets and models?

When a model starts behaving badly, you need to know exactly which data, base model, code and settings produced it. Versioning lets you reproduce it, compare it and roll back.

A simple setup is enough: store each dataset with a version or hash, and record that version plus the base model ID and config in each run's metadata.

## 116: Can you fine-tune embedding models?

Yes. Embedding models turn text into vectors for search and RAG. Fine-tuning them on pairs of queries and matching documents from your domain can improve retrieval a lot.

The `sentence-transformers` library is the usual tool. It's often a cheaper and bigger win than fine-tuning the chat model.

## 117: Can you fine-tune reasoning models?

Yes, open-weight reasoning models (ones that write a thinking section before the answer) can be fine-tuned. You need to keep their thinking format in your training data, or train them with reinforcement learning where only the final answer is graded.

If you train on answers without the thinking part, you can break the model's reasoning habit.

## 118: What is reinforcement fine-tuning (RFT)?

RFT trains a model by letting it try to answer, scoring each answer with a grader, and pushing the model toward the answers that scored higher. You don't need perfect example answers, just a way to check the result.

It works best for tasks with checkable answers, like math, code that must pass tests, or extraction where you know the right fields.

## 119: What is GRPO?

GRPO (Group Relative Policy Optimization) is a popular reinforcement learning method for LLMs. For each prompt, the model writes several answers, a reward function scores them, and each answer is compared to the group's average. Better-than-average answers are made more likely.

It doesn't need a separate value model, so it's simpler and lighter than PPO. TRL has a `GRPOTrainer`.

## 120: What is a reward function or grader?

It's code (or a model) that gives a score to a model's answer. For example: 1.0 if the JSON is valid and the extracted total matches the real total, 0.0 otherwise.

In reinforcement fine-tuning, the reward function defines what "good" means. If it has a loophole, the model will find and use it.

## 121: Can you fine-tune a model to call tools?

Yes. You train on conversations that include tool definitions, assistant tool calls with arguments, tool results and the final answer. The model learns when to call which tool and how to fill the arguments.

Use the exact tool-call format of the base model's chat template, or the model may produce calls your code can't parse.

## 122: Can fine-tuning make a model output valid JSON every time?

It makes JSON much more reliable, often above 99% on a narrow task. It doesn't guarantee it.

For a real guarantee, combine fine-tuning with structured output or constrained decoding at inference time, plus validation in your code with a retry.

## 123: What are typical use cases for fine-tuning?

- Extracting fields from documents into a fixed JSON shape.
- Classifying tickets, emails or content.
- Writing in a brand voice or a specific format.
- Replacing a large model with a small one for a high-volume task.
- Domain-specific SQL or code generation.
- Teaching a model a tool-calling pattern for an agent.
- Improving search with a fine-tuned embedding model.

## 124: Why fine-tune a small model?

Small models (1B to 8B parameters) are cheap and fast to run and can run on your own hardware or even on devices. Out of the box they're weaker than big models.

On one narrow task, a fine-tuned small model can match or beat a big general model, at a fraction of the cost per request.

## 125: How can a small fine-tuned model beat a big model?

A big model is good at everything but not tuned for your exact task, format and edge cases. A small model trained on thousands of your real examples has seen exactly the patterns it needs.

This works for narrow, repeated tasks. For open-ended reasoning or wide knowledge, the big model usually still wins.

## 126: How long does fine-tuning take?

A LoRA run on a small dataset with a 7B or 8B model can take 10 minutes to a couple of hours on one modern GPU. Bigger models, longer examples, more data or full fine-tuning take longer, from hours to days.

Data preparation and evaluation usually take more of your time than the training itself.

## 127: What is a training job?

A training job is one run of fine-tuning with a fixed dataset, base model and settings. On hosted platforms it has an ID and a status like queued, running, succeeded or failed.

Keep a record of each job: its config, logs, outputs and eval results.

## 128: What does a training config file look like?

Many tools let you write the settings in YAML instead of code. For example, an Axolotl config:

```yaml
base_model: Qwen/Qwen3-8B
datasets:
  - path: ./data/train.jsonl
    type: chat_template
adapter: lora
lora_r: 16
lora_alpha: 32
lora_target_linear: true
sequence_len: 2048
micro_batch_size: 2
gradient_accumulation_steps: 8
num_epochs: 2
learning_rate: 0.0002
output_dir: ./out
```

Keeping configs in git makes runs easy to repeat and compare.

## 129: What is packing?

Packing puts several short examples into one sequence up to the max length, instead of padding each example. It removes wasted padding and can make training much faster.

The downside is that examples can affect each other unless the trainer handles their boundaries correctly. In TRL you turn it on with `packing=True`.

## 130: What does training only on the completion mean?

It means the loss is calculated only on the assistant's answer, not on the system prompt or the user message. The model learns to write good answers, not to predict the user's text.

In TRL's `SFTConfig`, use `assistant_only_loss=True` for chat data or `completion_only_loss=True` for prompt-completion data. It usually gives better results.

## 131: Can training data have more than one turn?

Yes. Multi-turn examples are full conversations with several user and assistant messages. They teach the model how to handle follow-up questions and keep context.

If your app is a chatbot, include multi-turn examples. If you train only on single questions, the model may get worse at longer conversations.

## 132: What is the prompt-completion format?

It's a simpler format with two fields: a prompt and the completion you want.

```json
{
  "prompt": "Classify the sentiment: I love this phone.",
  "completion": " positive"
}
```

TRL also accepts a conversational version where `prompt` and `completion` are lists of messages. It's handy for single-turn tasks.

## 133: What is post-training?

Post-training is everything that happens to a model after pretraining: SFT, preference tuning (DPO, RLHF), reinforcement learning, safety training and so on. It's how labs turn a base model into a useful assistant.

When you fine-tune, you're doing your own small round of post-training.

## 134: What is the usual order of training steps?

A common pipeline is:

1. Start with an instruct model (or a base model plus SFT).
2. Run SFT on your task examples.
3. Optionally run DPO on preference pairs to polish behavior.
4. Optionally run reinforcement learning (like GRPO) for tasks with checkable answers.

Many projects stop after step 2. Add later steps only when you have data for them and a clear eval that shows they help.

## 135: Can you fine-tune for multiple languages?

Yes. Include examples in each language you need, in rough proportion to how important each one is. If you train only in English, quality in other languages may drop.

Check how well the base model and its tokenizer handle your languages before you start. Some models are much better at certain languages than others.

## 136: Can you fine-tune a model for code?

Yes. Code models are fine-tuned for things like your company's internal libraries, a specific SQL dialect, or a code style. Start from a model that's already good at code.

Code is easy to evaluate automatically: run it, run tests, or check that the SQL executes and returns the right rows.

## 137: Can a long system prompt replace fine-tuning?

Often, yes. Modern models follow long, detailed system prompts well, and prompt caching makes long prompts much cheaper. That covers many cases where people used to fine-tune.

Fine-tuning still wins when you need a small, cheap model, very consistent output, or behavior that's hard to describe in words.

## 138: How do you quickly test a fine-tuned model in Python?

Load the base model with the adapter and generate a reply:

```python
from transformers import AutoTokenizer
from peft import AutoPeftModelForCausalLM

model = AutoPeftModelForCausalLM.from_pretrained("./out", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("./out")

messages = [{"role": "user", "content": "Hi, my order 48213 never arrived."}]
inputs = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_tensors="pt", return_dict=True
).to(model.device)
output = model.generate(**inputs, max_new_tokens=100)
print(tokenizer.decode(output[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True))
```

## 139: How do you upload a fine-tuned model to the Hugging Face Hub?

After logging in with `hf auth login`, call `push_to_hub` on the model and tokenizer, or set `push_to_hub=True` in the training config:

```python
model.push_to_hub("my-org/ticket-classifier-lora", private=True)
tokenizer.push_to_hub("my-org/ticket-classifier-lora", private=True)
```

Use `private=True` for anything trained on company data.

## 140: What is the Hugging Face datasets library?

`datasets` is a library for loading and processing training data. It reads JSONL, CSV, Parquet or datasets from the Hub, and it has fast `map`, `filter` and `train_test_split` methods.

```python
from datasets import load_dataset

ds = load_dataset("json", data_files="train.jsonl", split="train")
ds = ds.train_test_split(test_size=0.1, seed=42)
```

TRL trainers accept these datasets directly.

## 141: Where can you rent GPUs for fine-tuning?

The big clouds (AWS, Google Cloud, Azure) and GPU-focused providers like RunPod, Lambda, Vast.ai and others rent GPUs by the hour. Hosted fine-tuning platforms run the training for you.

For learning, a single 24 GB to 80 GB GPU is plenty. Compare price per hour, availability and how easy it is to attach storage for datasets and checkpoints.

## 142: What is Accelerate?

`accelerate` is a Hugging Face library that runs the same training code on one GPU, many GPUs or many machines. The trainers in Transformers and TRL use it under the hood.

You use it with `accelerate config` to describe your hardware and `accelerate launch train.py` to start training.

## 143: What does a web developer need to know to start fine-tuning?

Basic Python, comfort with the command line and JSON, and the core ideas: tokens, chat templates, training vs validation loss, overfitting and evals. You don't need to know the math to get good results with LoRA and TRL.

The skills you already have, like cleaning data, writing tests and building APIs, are very useful for preparing data, building evals and serving the model.

## 144: What are the basic steps of a fine-tuning project?

1. Define the task and how you'll measure success.
2. Build an eval set and measure a prompting baseline.
3. Collect and clean training data.
4. Pick a base model and method (usually LoRA SFT).
5. Train, watch the loss, and evaluate checkpoints.
6. Compare against the baseline and read outputs.
7. Deploy, monitor and collect new data for the next version.

## 145: What are common beginner mistakes in fine-tuning?

- Fine-tuning before trying a good prompt.
- No eval set, so no way to know if it worked.
- Using the wrong chat template or missing the end-of-turn token.
- Training too many epochs on a tiny dataset.
- Trying to teach facts instead of behavior.
- Test examples leaking into the training data.
- Not reading the training data or the model's outputs.

## 146: What is a learning curve in fine-tuning?

A learning curve here usually means a chart of eval score against training set size. You train on, for example, 250, 500, 1,000 and 2,000 examples and plot the score for each.

If the score is still rising at the largest size, more data will likely help. If it's flat, focus on data quality or a different approach.

## 147: What is the difference between a model ID and an adapter ID?

The model ID points to the full base model, such as `Qwen/Qwen3-8B`. The adapter ID points to your LoRA weights, which only work on top of that exact base model.

The adapter's `adapter_config.json` stores the base model name. Loading an adapter on a different base model either fails or gives garbage.

## 148: What is SFT data balance?

Balance means your training data covers the cases you care about in sensible proportions. If 95% of your examples are "no action needed", the model may learn to say that almost always.

Count your examples per category or case and add more for rare but important cases.

## 149: Why should you read your training data by hand?

Reading even 50 to 100 random examples often reveals problems no script finds: wrong answers, inconsistent formats, leftover HTML, cut-off text or examples that contradict each other.

Fixing those before training is the cheapest improvement you can make.

## 150: What does "the model learns the format before the content" mean?

Early in fine-tuning, the model quickly picks up surface things like length, structure and tone. Getting the content right takes more good data and more training.

That's why a fine-tuned model can look right at a glance while still being wrong. Always check correctness, not only format.

# Moderate Questions (151-300)

## 151: How do you decide if a task really needs fine-tuning?

Go step by step and stop as soon as the quality is good enough:

1. Write a clear prompt with a few examples and test it on an eval set.
2. Try a stronger model, structured outputs, or RAG if facts are missing.
3. Look at the failures. If they're about format, style or a narrow skill that examples can show, fine-tuning is a good fit. If they're about missing knowledge, it isn't.
4. Check the business side: is the volume high enough that a cheaper fine-tuned model pays for the training and maintenance?

## 152: How do you build a prompting baseline before fine-tuning?

Write the best prompt you can for the base model you plan to fine-tune, and also for a strong hosted model. Run both on the same eval set and save the scores and outputs.

This gives you two numbers to beat: "same model, just prompted" and "best model money can buy". If the fine-tuned model doesn't beat the first one clearly, the training didn't help. If it doesn't get close to the second one, you may not save as much as you hoped.

## 153: How do you collect training data from production logs?

If you already run an LLM feature, its logs are a great source. Take real inputs, and use outputs that users accepted, people corrected, or that passed your checks.

Then clean them: remove PII, drop failed or low-rated answers, dedupe, and make sure the distribution matches what you expect in the future, not just last month's traffic. Check that your terms and privacy policy allow using that data for training.

## 154: What does cleaning a fine-tuning dataset involve?

- Remove empty, broken or cut-off examples.
- Fix or drop examples with wrong answers.
- Make formatting consistent (same JSON keys, same date format, same tone).
- Remove exact and near duplicates.
- Mask or remove PII and secrets.
- Remove examples that are much longer than your max length, or decide how to handle them.
- Check the label or case balance.

Write these as scripts so you can re-run them on new data.

## 155: What makes a good training example?

A good example looks like a real input from production and has the exact output you'd want, written the way you'd want it every time. It's correct, consistent with other examples, and not longer than it needs to be.

Include hard cases and edge cases, not only easy ones. The model learns most from examples that show decisions it would otherwise get wrong.

## 156: How do you generate synthetic training data with a larger model?

Give a strong model a clear spec and some real examples, then ask it to write new inputs and ideal outputs. Vary the prompts (topics, lengths, difficulty, personas) so the data isn't repetitive.

```python
prompt = f"""Write one realistic customer email about: {topic}.
Tone: {tone}. Length: {length}.
Then write the correct JSON extraction using this schema: {schema}.
Return JSON with keys "email" and "extraction"."""
```

Check the teacher model's terms of use first, and always filter the results before training.

## 157: How do you filter synthetic data?

- Validate the format with code (JSON parses, schema matches, required fields exist).
- Check answers with rules or tests where possible (math is correct, SQL runs).
- Use a judge model to score quality and drop low scores.
- Remove near duplicates so the dataset isn't 100 versions of the same example.
- Read a random sample by hand.

It's normal to throw away 20% to 50% of generated examples.

## 158: How do you handle class imbalance in fine-tuning data?

If one class or case dominates, the model learns to predict it too often. Options:

- Downsample the common cases.
- Add more examples of rare cases, by collecting real ones or generating them.
- Make sure the eval set reports per-class scores, not just overall accuracy.

Don't balance perfectly if the real world isn't balanced. You want the model to see enough rare cases without becoming biased toward them.

## 159: How do you teach a fine-tuned model to refuse or say "I don't know"?

Include examples where the right answer is a refusal or "not enough information", written in the exact style you want. For example, questions outside your product's scope, or extraction inputs where a field is missing.

Keep them in a reasonable share of the data, maybe 5% to 15% depending on how often it happens in production. Too many and the model starts refusing valid requests.

## 160: How do you convert raw data into the messages format?

Write a small script that maps each record to a list of messages and writes JSONL:

```python
import json

SYSTEM = "Extract the order ID and issue type. Reply with JSON only."

with open("raw.jsonl") as src, open("train.jsonl", "w") as out:
    for line in src:
        row = json.loads(line)
        example = {"messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": row["email_body"]},
            {"role": "assistant", "content": json.dumps(
                {"order_id": row["order_id"], "issue": row["issue"]})},
        ]}
        out.write(json.dumps(example, ensure_ascii=False) + "\n")
```

## 161: How do you see what the chat template produces?

Apply the template without tokenizing and print the result:

```python
from transformers import AutoTokenizer

tok = AutoTokenizer.from_pretrained("Qwen/Qwen3-8B")
text = tok.apply_chat_template(example["messages"], tokenize=False)
print(text)
```

You'll see the special tokens around each role. Do this once for every new base model. It catches many template and end-of-turn bugs before you waste a training run.

## 162: How do you validate a training dataset before a run?

Write a quick script that checks each line:

```python
import json

for i, line in enumerate(open("train.jsonl"), 1):
    ex = json.loads(line)
    msgs = ex["messages"]
    assert msgs[-1]["role"] == "assistant", f"line {i}: last message is not assistant"
    assert all(m["content"].strip() for m in msgs), f"line {i}: empty content"
    json.loads(msgs[-1]["content"])  # this task expects JSON answers
```

Also count tokens per example and print the max and the 99th percentile, so you can choose the max length.

## 163: How do you split a dataset into train and validation sets?

With the `datasets` library:

```python
from datasets import load_dataset

ds = load_dataset("json", data_files="all.jsonl", split="train")
splits = ds.train_test_split(test_size=0.1, seed=42)
train_ds, val_ds = splits["train"], splits["test"]
```

If your data has groups (for example several examples from the same customer or document), split by group so similar examples don't end up on both sides.

## 164: What does a minimal SFT run with TRL look like?

```python
from datasets import load_dataset
from trl import SFTConfig, SFTTrainer

dataset = load_dataset("json", data_files="train.jsonl", split="train")

trainer = SFTTrainer(
    model="Qwen/Qwen3-0.6B",
    train_dataset=dataset,
    args=SFTConfig(output_dir="./out", num_train_epochs=2),
)
trainer.train()
trainer.save_model()
```

`SFTTrainer` loads the model and tokenizer from the name, applies the chat template to `messages` and trains. For bigger models, add LoRA.

## 165: Which SFTConfig settings matter most?

- `learning_rate`, `num_train_epochs`: how hard and how long to train.
- `per_device_train_batch_size`, `gradient_accumulation_steps`: effective batch size.
- `max_length`: max tokens per example.
- `assistant_only_loss` or `completion_only_loss`: train only on answers.
- `packing`: combine short examples.
- `gradient_checkpointing`, `bf16`: memory and speed.
- `eval_strategy`, `save_strategy`, `logging_steps`: how often to evaluate, save and log.

Start with the defaults and change one thing at a time.

## 166: How do you add LoRA to an SFTTrainer run?

Pass a `LoraConfig` as `peft_config`:

```python
from peft import LoraConfig
from trl import SFTConfig, SFTTrainer

peft_config = LoraConfig(
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    target_modules="all-linear",
    task_type="CAUSAL_LM",
)

trainer = SFTTrainer(
    model="Qwen/Qwen3-8B",
    train_dataset=train_ds,
    eval_dataset=val_ds,
    peft_config=peft_config,
    args=SFTConfig(
        output_dir="./out",
        learning_rate=2e-4,
        num_train_epochs=2,
        per_device_train_batch_size=2,
        gradient_accumulation_steps=8,
        gradient_checkpointing=True,
        bf16=True,
        assistant_only_loss=True,
    ),
)
trainer.train()
```

Only the adapter is saved to `./out`.

## 167: How do you choose the LoRA rank and alpha?

Start with `r=16` and `lora_alpha=32` on all linear layers. That works for most format, style and narrow-task jobs.

Try a higher rank (32 or 64) if the model underfits and the task is complex or the dataset is large. Try a lower rank (8) if you have little data or want a smaller adapter. Keep `lora_alpha` around `r` to `2 * r`, and remember that changing alpha also changes the effective learning rate.

## 168: Should LoRA target only attention layers or all linear layers?

Early LoRA work targeted only the attention query and value projections. Later results (including the QLoRA paper) showed that targeting all linear layers, including the MLP layers, gives clearly better quality for little extra cost.

So use `target_modules="all-linear"` by default. Target fewer layers only if memory is very tight.

## 169: How do you set up QLoRA?

Load the model in 4-bit with `BitsAndBytesConfig`, then train LoRA on top:

```python
import torch
from transformers import AutoModelForCausalLM, BitsAndBytesConfig

bnb = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
    bnb_4bit_compute_dtype=torch.bfloat16,
)
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen3-14B", quantization_config=bnb, device_map="auto"
)
# then pass model and a LoraConfig to SFTTrainer as usual
```

QLoRA needs the `bitsandbytes` package and an NVIDIA GPU (support for other hardware exists but is less mature).

## 170: How do you choose a learning rate?

Typical starting points:

- LoRA / QLoRA: `1e-4` to `2e-4`.
- Full fine-tuning of a 7B to 8B model: around `1e-5`, sometimes lower.
- DPO: much lower, around `5e-7` to `5e-6` for full fine-tuning, and around `5e-6` to `5e-5` with LoRA.

If loss jumps around or the model forgets basic skills, lower it. If loss barely moves, raise it a bit. Try 2 or 3 values on a short run rather than guessing.

## 171: How many epochs should you train?

For most SFT jobs, 1 to 3 epochs. Large datasets (tens of thousands of examples) often need only 1. Small datasets may need 3, but watch validation loss closely.

Save a checkpoint each epoch and evaluate each one on your task eval. Often epoch 2 is better than epoch 3, even if training loss is lower at epoch 3.

## 172: How do you choose the batch size?

Pick the largest per-device batch that fits in memory, then use gradient accumulation to reach an effective batch of around 16 to 64 examples (or a fixed number of tokens).

Very small effective batches give noisy updates. Very large ones mean fewer updates per epoch, so you may need more epochs or a higher learning rate.

## 173: How do you estimate how much GPU memory you need?

Rough numbers for an 8B model:

- Weights in bf16: about 2 bytes per parameter, so ~16 GB. In 4-bit: ~5 GB.
- Full fine-tuning with AdamW: weights + gradients + optimizer state is about 16 bytes per parameter, so ~130 GB or more. That needs several GPUs.
- LoRA: weights plus a small adapter and its optimizer state, plus activations. Often fits on a 24 GB to 48 GB card.
- QLoRA: often fits on 16 GB to 24 GB.

Activations grow with batch size and sequence length, so long examples change the numbers a lot.

## 174: How do you fit training on a single GPU?

In order of what to try:

1. Use LoRA instead of full fine-tuning.
2. Turn on `gradient_checkpointing=True`.
3. Lower `per_device_train_batch_size` to 1 or 2 and raise gradient accumulation.
4. Lower `max_length` if most examples are shorter.
5. Switch to QLoRA (4-bit base model).
6. Use an optimized attention kernel and a memory-efficient library like Unsloth.
7. Pick a smaller base model.

## 175: How do you pick a base model?

Consider:

- **Size:** the smallest model that reaches your quality target, because inference cost lasts forever.
- **License:** allowed for your use?
- **Languages and domain:** test the base model on your task first.
- **Context length:** enough for your inputs?
- **Tooling support:** works with TRL, vLLM, Ollama and your serving setup.
- **Family:** pick a popular family (Qwen, Llama, Gemma, Mistral, gpt-oss) so you get bug fixes, guides and new versions.

Try two or three candidates with a prompt baseline before choosing.

## 176: Should you start from a base model or an instruct model?

Start from the instruct model in most cases. It already follows instructions, uses a chat template and has safety training, so you need less data.

Start from a base model when you have a large dataset and want full control over format and behavior, or when the instruct model's habits (like extra politeness or long explanations) fight your task. Then you must set up the chat template yourself.

## 177: How do you read a training loss curve?

A healthy SFT loss drops fast in the first steps, then flattens slowly. Small bumps are normal. With several epochs you often see a step down at the start of each new epoch, because the model sees examples again.

Check validation loss next to it. If both flatten together, you're near the limit of the data. If validation loss rises while training loss keeps falling, you're overfitting.

## 178: What does it mean if training loss goes almost to zero?

Usually the model is memorizing the training set. It's common with small datasets and several epochs. The model may still look fine on training-like inputs but fail on new ones.

It can also mean the task is trivial (for example the answer is in the input), or there's a data bug where the loss is computed only on padding or easy tokens. Check validation loss and real outputs.

## 179: What should you do if validation loss starts going up?

That's overfitting. Use the checkpoint from before the rise, or:

- Train fewer epochs.
- Lower the learning rate.
- Add more varied data.
- Increase LoRA dropout or reduce rank.

Also check your task metric. Sometimes validation loss rises a little while the actual task score still improves, because loss and correctness aren't the same thing.

## 180: What should you check if the loss doesn't go down at all?

- The learning rate isn't too low, and warmup isn't taking the whole run.
- The labels aren't all masked (all `-100`), which means no tokens are trained.
- LoRA is actually attached: `model.print_trainable_parameters()` should show a non-zero count.
- The dataset is being read correctly and isn't empty after filtering.
- The base model and tokenizer match.

## 181: What causes loss spikes or NaN loss?

Common causes are a learning rate that's too high, using `fp16` where values overflow, a bad batch (for example extremely long or corrupted examples), or no gradient clipping.

Fixes: lower the learning rate, use `bf16`, keep `max_grad_norm` around 1.0 (the default), and find and remove the bad examples by logging which batch caused the spike.

## 182: How do you fix CUDA out of memory errors?

Lower the memory per step: smaller batch size with more gradient accumulation, shorter `max_length`, gradient checkpointing, LoRA instead of full fine-tuning, QLoRA instead of LoRA.

If it only happens on some steps, a few very long examples are the cause. Drop them, truncate them or sort and group by length. Also make sure no other process is using the same GPU (`nvidia-smi`).

## 183: Why does a fine-tuned model keep generating and never stop?

It didn't learn to produce the end-of-turn or EOS token. Usually the training text was missing that token after the assistant's answer, the token was masked out of the loss, or the pad token was the same as the EOS token and got masked everywhere.

Print a tokenized training example and check that it ends with the right end token and that the token is included in the labels. At inference, check that the generation config uses the same stop tokens.

## 184: Why does the fine-tuned model ignore what it was trained on?

Most often the prompt format at inference doesn't match training. For example, training used the chat template but inference sends plain text, or the system prompt is different, or the adapter isn't actually loaded.

Compare the exact string the model sees at inference with a training example. Also confirm the adapter is active and the base model name is identical.

## 185: What are assistant_only_loss and completion_only_loss in TRL?

They control which tokens count in the loss:

- `completion_only_loss` (prompt-completion data): loss only on the completion. It's on by default for that format.
- `assistant_only_loss=True` (chat data): loss only on assistant messages. It needs a chat template that marks assistant parts with generation markers, which many recent model templates have.

Training only on answers usually gives a better model and avoids teaching it to imitate users.

## 186: What are the pros and cons of packing?

Pros: much less padding, so faster training and more stable throughput, especially when examples have very different lengths.

Cons: if not handled carefully, tokens from one example can attend to another in the same packed sequence. Modern TRL packing with a flash-attention style kernel keeps examples separate. Packing also changes the number of steps per epoch, so recheck your learning rate schedule.

## 187: How do you choose max_length and handle long examples?

Measure token lengths of your examples with the real chat template applied. Set `max_length` just above the length that covers 95% to 99% of examples.

For the long tail, either drop them, shorten the input (for example trim long documents), or split them if it makes sense. Avoid silently truncating the answer. A model trained on cut-off answers learns to stop mid-sentence.

## 188: How do you build an eval set for a fine-tuned model?

Take 100 to 500 real inputs that look like production, including hard and rare cases. Write or verify the correct outputs. Keep it separate from training data and don't change it between runs, so scores stay comparable.

Add a few slices: by category, input length, language or difficulty. Overall averages hide regressions in small but important groups.

## 189: Which metrics fit common fine-tuning tasks?

- **Classification:** accuracy, precision, recall and F1 per class.
- **Extraction / JSON:** valid JSON rate, schema pass rate, per-field exact match.
- **SQL / code:** runs without error, passes tests, returns the right result.
- **Summaries / writing:** judge-model score against a rubric, plus human review.
- **Chat / support:** resolution rate and user rating in production.

Pick a metric that matches what the business cares about, not only what's easy to compute.

## 190: How do you use LLM-as-a-judge well?

- Give the judge a clear rubric and, if possible, a reference answer.
- Ask for a short reason before the score.
- For pairwise comparisons, run both orders (A/B and B/A) to cancel position bias.
- Use a different, strong model as judge, not the model being tested.
- Check the judge against 50 to 100 human-labeled examples and measure how often it agrees.

## 191: How do you compare a fine-tuned model fairly with the baseline?

Run all models on the same eval set with the same settings: same temperature, same max tokens and the same scoring code. Give each model its best prompt (the fine-tuned model usually needs a much shorter one).

Report scores together with cost per request and latency. A model that's 2% better but 10 times cheaper is often the winner.

## 192: How do you check that fine-tuning didn't break general skills?

Keep a small "general" eval next to your task eval: instruction following, simple reasoning, safety refusals, and multi-turn chat if your app uses it. Run it on the base model and the fine-tuned model.

If general scores drop a lot, lower the learning rate, train fewer steps, use a lower rank, or mix some general instruction data into your training set.

## 193: How do you save and load a LoRA adapter?

`trainer.save_model()` saves the adapter files (`adapter_config.json` and `adapter_model.safetensors`). To load:

```python
from transformers import AutoModelForCausalLM
from peft import PeftModel

base = AutoModelForCausalLM.from_pretrained("Qwen/Qwen3-8B", device_map="auto")
model = PeftModel.from_pretrained(base, "./out")
```

Save the tokenizer with the adapter too, especially if you changed it.

## 194: How do you merge a LoRA adapter into the base model?

Load the base model in 16-bit (not 4-bit), load the adapter, merge and save:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

base = AutoModelForCausalLM.from_pretrained("Qwen/Qwen3-8B", dtype=torch.bfloat16)
merged = PeftModel.from_pretrained(base, "./out").merge_and_unload()
merged.save_pretrained("./merged")
AutoTokenizer.from_pretrained("./out").save_pretrained("./merged")
```

The merged folder is a normal model you can serve or convert to GGUF.

## 195: How do you keep a fine-tuned model private on the Hub?

Create the repo as private (`private=True` when pushing) or inside an organization with restricted access. Use fine-grained access tokens with read-only rights for servers that only need to download the model.

For sensitive data, many companies skip the public Hub entirely and keep adapters in their own storage, like S3 or GCS, with normal access controls.

## 196: How do you serve a LoRA adapter with vLLM?

Start vLLM with LoRA enabled and register the adapter by name:

```bash
vllm serve Qwen/Qwen3-8B \
  --enable-lora \
  --lora-modules ticket-extractor=./out \
  --max-lora-rank 16
```

Then call it like the OpenAI API, using the adapter name as the model:

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "ticket-extractor", "messages": [{"role": "user", "content": "..."}]}'
```

## 197: How do you serve many LoRA adapters from one base model?

Load all adapters in one vLLM server with several `--lora-modules name=path` entries, and choose the adapter per request with the `model` field. vLLM batches requests for different adapters together on the same GPU.

Settings like `--max-loras` (how many adapters are active at the same time) and `--max-lora-rank` control memory use. This is much cheaper than running one full model per customer or task.

## 198: How do you run a fine-tuned model in Ollama via GGUF?

1. Merge the adapter into the base model.
2. Convert to GGUF with llama.cpp's `convert_hf_to_gguf.py`, and optionally quantize (for example to Q4_K_M).
3. Write a `Modelfile`:

```
FROM ./my-model-Q4_K_M.gguf
PARAMETER temperature 0.2
```

4. Run `ollama create my-model -f Modelfile` and test with `ollama run my-model`.

Check that the chat template stored in the GGUF matches the one you trained with.

## 199: Should you quantize a model after fine-tuning?

Often yes, to cut serving cost and memory. 8-bit usually loses almost nothing. 4-bit methods (like AWQ, GPTQ or GGUF Q4 variants) lose a bit more.

Always re-run your eval on the quantized model. Fine-tuned behavior, like strict JSON format, can sometimes degrade more than general benchmarks suggest.

## 200: How do you call a self-hosted fine-tuned model from a Node.js app?

vLLM and many other servers expose an OpenAI-compatible API, so you can use the OpenAI SDK with a custom base URL:

```ts
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: process.env.LLM_BASE_URL, // e.g. http://vllm:8000/v1
  apiKey: process.env.LLM_API_KEY,
});

const res = await client.chat.completions.create({
  model: "ticket-extractor",
  messages: [{ role: "user", content: emailBody }],
  temperature: 0,
});
console.log(res.choices[0].message.content);
```

## 201: How do you use a fine-tuned model with the Vercel AI SDK?

Use the OpenAI-compatible provider and point it at your server:

```ts
import { createOpenAICompatible } from "@ai-sdk/openai-compatible";
import { generateText } from "ai";

const myModels = createOpenAICompatible({
  name: "my-vllm",
  baseURL: process.env.LLM_BASE_URL!,
  apiKey: process.env.LLM_API_KEY,
});

const { text } = await generateText({
  model: myModels("ticket-extractor"),
  prompt: emailBody,
});
```

The rest of your app code (streaming, UI hooks) works the same as with hosted models.

## 202: Why must the inference prompt match the training format?

The model learned to respond to a very specific pattern: a certain system prompt, chat template and input style. If production sends something different, for example a longer system prompt or raw text without the template, the model is outside what it learned and quality drops.

Keep the prompt-building code shared between your data preparation and your production code, so the two can't drift apart.

## 203: How do you create DPO preference pairs?

Common ways:

- Generate 2 or more answers per prompt from your SFT model, then have people or a judge pick the best and worst.
- Use real user feedback, like thumbs up vs thumbs down on answers to the same kind of request.
- Take a good answer and write a "rejected" version with the specific flaw you want to remove (too long, wrong format, rude tone).

The pairs should differ mainly in what you want to change. If chosen answers are always longer, the model just learns "be longer".

## 204: What does a DPO training run look like in TRL?

```python
from datasets import load_dataset
from peft import LoraConfig
from trl import DPOConfig, DPOTrainer

dataset = load_dataset("json", data_files="prefs.jsonl", split="train")

trainer = DPOTrainer(
    model="./sft-merged",
    train_dataset=dataset,
    peft_config=LoraConfig(r=16, lora_alpha=32, target_modules="all-linear", task_type="CAUSAL_LM"),
    args=DPOConfig(output_dir="./dpo-out", beta=0.1, learning_rate=5e-6, num_train_epochs=1, bf16=True),
)
trainer.train()
```

The dataset needs `prompt`, `chosen` and `rejected` fields. With LoRA, the frozen base acts as the reference model, so you don't need a second copy in memory.

## 205: What does the beta parameter in DPO do?

`beta` controls how far the model is allowed to move away from the reference (starting) model. A higher beta keeps it closer to the reference. A lower beta lets it change more to match the preferences.

Typical values are 0.05 to 0.5, with 0.1 as a common start. If the model becomes weird or overly verbose after DPO, try a higher beta or fewer steps.

## 206: When should you use DPO instead of more SFT?

Use SFT when you can write the correct answer. Use DPO when it's easier to say which of two answers is better than to write the perfect one, or when the model already does the task but has a specific bad habit (too long, too formal, hedging, small errors).

DPO usually comes after SFT, not instead of it. Starting DPO from a model that can't do the task yet rarely works well.

## 207: What is KTO and when is it useful?

KTO (Kahneman-Tversky Optimization) trains on single answers marked as good or bad, instead of pairs. That fits data like thumbs up and down, where you rarely have two answers to the same prompt.

TRL has a `KTOTrainer`. If you have real pairs, DPO is usually the first choice. If you only have unpaired labels, KTO saves you from building artificial pairs.

## 208: What other preference methods might come up in an interview?

- **ORPO:** combines SFT and preference learning in one step, no reference model.
- **SimPO:** a DPO variant without a reference model that uses length-normalized scores.
- **IPO:** a DPO variant that's less prone to overfitting the preferences.
- **Online DPO / RLOO:** generate new answers during training and score them, instead of using a fixed dataset.

You don't need to memorize the math. Knowing that they're variations on "make preferred answers more likely than rejected ones" is usually enough.

## 209: How do you train a reward model with TRL?

Use preference pairs with `RewardTrainer`. It trains a model with a single score output so that chosen answers score higher than rejected ones:

```python
from trl import RewardConfig, RewardTrainer

trainer = RewardTrainer(
    model="Qwen/Qwen3-0.6B",
    train_dataset=prefs,  # prompt / chosen / rejected
    args=RewardConfig(output_dir="./rm", num_train_epochs=1),
)
trainer.train()
```

Reward models are useful for RL training, for ranking several candidate answers at inference, and as a cheap automated judge.

## 210: How do you fine-tune a model for reliable JSON output?

- Use the exact same schema in every example, with the same key order and formatting.
- Make the assistant answer pure JSON, no extra text, unless you want text.
- Include examples with missing fields set to `null` instead of invented values.
- Validate every training answer with your schema before training.
- At inference, use low temperature and structured output or JSON schema constraints if your server supports them, and validate in code.

## 211: How do you prepare tool-calling training data?

Each example includes the tool definitions and a conversation with the assistant's tool call, the tool result and the final answer:

```json
{
  "messages": [
    { "role": "user", "content": "What's the status of order 48213?" },
    {
      "role": "assistant",
      "tool_calls": [
        {
          "type": "function",
          "function": {
            "name": "get_order",
            "arguments": { "order_id": "48213" }
          }
        }
      ]
    },
    {
      "role": "tool",
      "name": "get_order",
      "content": "{\"status\": \"shipped\"}"
    },
    { "role": "assistant", "content": "Your order 48213 has shipped." }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_order",
        "description": "Look up an order",
        "parameters": {
          "type": "object",
          "properties": { "order_id": { "type": "string" } },
          "required": ["order_id"]
        }
      }
    }
  ]
}
```

TRL passes `tools` to the chat template. Check that the model's template actually supports tools and renders them the way the model expects.

## 212: When should you use an encoder model instead of an LLM for classification?

If the task is a fixed set of labels and you have a few thousand labeled examples, a fine-tuned encoder model (BERT, ModernBERT, DeBERTa) is often as accurate as an LLM and many times cheaper and faster.

```python
from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained(
    "answerdotai/ModernBERT-base", num_labels=5
)
```

Use an LLM when labels need reasoning, change often, need explanations, or when you have very few examples.

## 213: How do you fine-tune an embedding model with sentence-transformers?

Train on pairs of a query and its matching document. In-batch negatives (other documents in the batch) teach the model what doesn't match:

```python
from datasets import load_dataset
from sentence_transformers import SentenceTransformer, SentenceTransformerTrainer
from sentence_transformers.losses import MultipleNegativesRankingLoss

model = SentenceTransformer("BAAI/bge-base-en-v1.5")
train = load_dataset("json", data_files="pairs.jsonl", split="train")  # anchor, positive

trainer = SentenceTransformerTrainer(
    model=model,
    train_dataset=train,
    loss=MultipleNegativesRankingLoss(model),
)
trainer.train()
model.save_pretrained("./my-embedder")
```

Remember to re-embed your whole document store with the new model.

## 214: How do you fine-tune a model for RAG answers?

Train on examples that include retrieved context in the prompt and an answer that uses only that context, with citations if you need them. Include examples where the context doesn't contain the answer and the right reply is "I couldn't find that in the documents".

Also include noisy context (some irrelevant chunks), so the model learns to ignore them. This teaches behavior, not facts, which is exactly what fine-tuning is good at.

## 215: What is the workflow for distilling a big model into a small one?

1. Collect real or realistic inputs for your task.
2. Run the big model with your best prompt to produce outputs.
3. Filter outputs with checks and a judge, and fix or drop bad ones.
4. Fine-tune the small model (usually LoRA SFT) on the cleaned pairs, with a short prompt.
5. Evaluate the student against the teacher on a held-out set.
6. Route traffic to the student, and keep the teacher as a fallback for hard cases.

## 216: What legal issues come with training on model outputs?

Many hosted model providers have terms that limit using their outputs to train models that compete with them. Rules differ between providers and change over time, so read the current terms for the exact model you use.

Also check the base model license, the rights to your input data (customer data, scraped data, copyrighted text), and privacy laws. Get your legal team involved before training on anything sensitive.

## 217: How do you search for good hyperparameters without wasting money?

- Start from known defaults for your method and model size.
- Do short runs on a subset of data to compare a few learning rates.
- Change one setting at a time and track every run.
- Focus on the settings that matter most: learning rate, epochs and data. Rank, batch size and scheduler matter less.
- Evaluate checkpoints on your task eval, not only on loss.

A big automated sweep is rarely worth it for application fine-tuning.

## 218: How do you track fine-tuning experiments?

Turn on a tracker in the training config and add useful metadata:

```python
args = SFTConfig(
    output_dir="./out",
    report_to="wandb",
    run_name="extractor-qwen3-8b-r16-lr2e-4",
    logging_steps=10,
)
```

Also log the dataset version (or hash), base model ID and git commit. Then save your eval results under the same run name, so you can link a score to the exact training setup.

## 219: How do you make fine-tuning runs reproducible?

- Pin library versions (`transformers`, `trl`, `peft`, `torch`) in a lock file or container image.
- Pin the base model to a specific revision (commit hash), not just the name.
- Version your dataset and record its hash.
- Set a seed.
- Keep the config in git.

Results still won't be bit-for-bit identical on GPUs, but they should be close enough to compare.

## 220: How do you version training data?

Simple options:

- Store each dataset version as an immutable file in object storage, with a name like `train-2026-11-01.jsonl`, and record its hash.
- Use a tool like DVC or Hugging Face datasets repos (they're git-based and keep history).

What matters is that every model can point to the exact data it was trained on, and that you never edit a dataset version in place.

## 221: How do you fine-tune with Unsloth?

```python
from unsloth import FastLanguageModel

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/Qwen3-8B",
    max_seq_length=2048,
    load_in_4bit=True,
)
model = FastLanguageModel.get_peft_model(
    model,
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                    "gate_proj", "up_proj", "down_proj"],
)
# then train with TRL's SFTTrainer as usual
```

Unsloth also has helpers for saving merged models and exporting to GGUF.

## 222: How do you run an Axolotl training job?

Write a YAML config (base model, datasets, adapter settings, hyperparameters, output dir) and run:

```bash
axolotl preprocess config.yml   # optional: tokenize and check the data
axolotl train config.yml
```

The preprocess step is useful for checking how your data is tokenized before paying for GPU time. For multi-GPU, Axolotl uses Accelerate with DeepSpeed or FSDP settings in the same config.

## 223: Can you run TRL from the command line?

Yes. TRL ships a CLI that wraps its trainers:

```bash
trl sft \
  --model_name_or_path Qwen/Qwen3-0.6B \
  --dataset_name trl-lib/Capybara \
  --output_dir ./out \
  --use_peft --lora_r 16 --lora_alpha 32
```

You can also put the options in a YAML file and pass `--config sft.yml`. It's good for quick experiments and for scripts in CI.

## 224: How do you fine-tune with MLX on a Mac?

Put `train.jsonl` and `valid.jsonl` (chat or prompt-completion format) in a folder and run:

```bash
mlx_lm.lora --model Qwen/Qwen3-1.7B --train --data ./data \
  --batch-size 4 --iters 600 --adapter-path ./adapters
mlx_lm.generate --model Qwen/Qwen3-1.7B --adapter-path ./adapters \
  --prompt "Hi, my order 48213 never arrived."
```

`mlx_lm.fuse` merges the adapter into the model when you're done. It's a good, cheap way to learn and to prototype with small models.

## 225: How does supervised tuning work on Vertex AI for Gemini?

You upload a JSONL file to Cloud Storage where each line has `contents` with `user` and `model` turns (and optionally a `systemInstruction`), then start a tuning job for a supported Gemini model with the console, the API or the Gen AI SDK.

```json
{
  "systemInstruction": {
    "role": "system",
    "parts": [{ "text": "Reply with JSON only." }]
  },
  "contents": [
    {
      "role": "user",
      "parts": [{ "text": "Hi, my order 48213 never arrived." }]
    },
    { "role": "model", "parts": [{ "text": "{\"order_id\": \"48213\"}" }] }
  ]
}
```

When the job finishes, Vertex AI gives you an endpoint for the tuned model. Check the docs for which Gemini versions currently support tuning.

## 226: When should you use a hosted fine-tuning platform instead of training yourself?

Use a hosted platform when you want results quickly, don't have ML infrastructure people, and are fine with the provider's supported models and methods. It's also simpler when the same platform serves the model.

Train yourself when you need full control (any method, any model), have strict data rules, want to avoid lock-in, or run so many jobs that your own GPUs are cheaper. Many teams start hosted and move in-house later.

## 227: How do you estimate the cost of a fine-tuning run?

Training cost is roughly GPU price per hour times hours. To guess the hours, count total training tokens (examples x average tokens x epochs) and divide by the throughput you measure in a short test run.

Example: 5,000 examples x 800 tokens x 2 epochs = 8M tokens. If a test run shows 3,000 tokens per second on one GPU, that's about 45 minutes. Add time for evals and a few failed or repeated runs.

## 228: What is a checklist for running training on a cloud GPU?

- Use a container image with pinned CUDA, PyTorch and library versions.
- Keep data and checkpoints on persistent storage, not the instance's local disk.
- Save checkpoints often enough to resume after a crash or a spot instance being taken back.
- Log to a tracker you can see from outside the machine.
- Store API tokens as secrets, not in the code.
- Shut the instance down when the job ends. Idle GPUs are the most common surprise bill.

## 229: How do you run training on multiple GPUs?

With Hugging Face trainers, you usually don't change your code. Configure Accelerate and launch:

```bash
accelerate config          # answer questions once
accelerate launch train.py # runs one process per GPU
```

For simple data parallel training, each GPU holds a full model copy and handles different batches. If the model doesn't fit on one GPU, turn on FSDP or DeepSpeed ZeRO in the Accelerate config so the model is split across GPUs.

## 230: What are FSDP and DeepSpeed ZeRO in simple terms?

Both split the model's weights, gradients and optimizer state across GPUs, so each GPU stores only a part instead of a full copy. That lets you train models that wouldn't fit on one GPU.

FSDP (Fully Sharded Data Parallel) is built into PyTorch. DeepSpeed is a Microsoft library with similar "ZeRO" stages. Both work with Accelerate, so the choice is usually about which one your tools and team know better.

## 231: How do you do continued pretraining on domain text?

Collect a large amount of clean domain text (millions of tokens or more), split it into chunks of your sequence length, and train the model to predict the next token on all of it, without any chat template:

```python
from trl import SFTConfig, SFTTrainer

trainer = SFTTrainer(
    model="Qwen/Qwen3-8B-Base",
    train_dataset=text_ds,  # a dataset with a "text" column
    args=SFTConfig(output_dir="./cpt", packing=True, max_length=4096, learning_rate=2e-5),
)
```

Use a lower learning rate than LoRA SFT, mix in some general text, and follow it with instruction SFT so the model still follows instructions.

## 232: How does mixing general data help reduce forgetting?

If the model sees only your narrow task, its weights drift toward that task and it loses other skills. Adding 5% to 30% general instruction data (a public instruction dataset, or outputs from the base model on varied prompts) keeps those skills active during training.

It's especially useful when the fine-tuned model must still chat normally, follow varied instructions, or handle requests outside the main task.

## 233: Can you fine-tune one model for several tasks at once?

Yes, that's multi-task fine-tuning. Mix examples from all tasks and give each task a clear instruction or system prompt, so the model knows which task it's doing.

It works well when the tasks are related and none of them is tiny. Watch per-task evals. If one task gets worse because another dominates the data, rebalance or train separate adapters instead.

## 234: What should you watch for when fine-tuning for multiple languages?

- Check the base model's quality in each language first.
- Don't just machine-translate English data without review. Bad translations teach bad language.
- Keep a separate eval set per language.
- Watch token counts: some languages use many more tokens per word, which affects cost and max length.
- Be careful the model doesn't start answering in the wrong language. Include examples that show the right answer language.

## 235: How do you handle long documents in fine-tuning?

Options:

- Raise `max_length` and use gradient checkpointing and a memory-efficient attention kernel.
- Trim the input to the useful parts (for example only the relevant sections) before training.
- Split the task: one model step finds the relevant part, another extracts or summarizes.

Make sure the inputs at inference are prepared the same way as in training.

## 236: How should you handle the system prompt in training data?

Pick one short, stable system prompt for the task and use it in every training example and in production. Don't include long instructions the model no longer needs. The behavior is learned from the examples.

If you serve several behaviors from one model, use different system prompts per behavior in training and send the matching one at inference.

## 237: How do you teach a fine-tuned model to stay on topic?

Include out-of-scope requests in the training data with short, polite answers that steer back to the task, in your product's tone. Mix in tricky cases that look off-topic but are valid, so the model doesn't refuse too much.

Also keep a separate input check in your app for clearly harmful requests. Don't rely only on the fine-tuned model.

## 238: What should you test before releasing a fine-tuned model?

- Task eval scores beat the current model and the baseline.
- No big regressions in general or safety evals.
- Output format is valid at a high rate with your production settings.
- Latency and cost per request at expected traffic.
- Behavior on edge cases: empty input, very long input, other languages, prompt injection attempts.
- The exact production prompt-building code works with the model.

## 239: How do you roll out a fine-tuned model safely?

Start with a shadow deployment: send real requests to the new model too, but don't show its answers to users. Compare outputs with the current model.

Then do a canary: send a small share of real traffic (like 5%) to the new model, watch errors and business metrics, and increase the share step by step. Keep the old model ready for instant rollback.

## 240: What should you monitor for a fine-tuned model in production?

- Error rates, timeouts and latency.
- Output validity (JSON parse rate, schema pass rate).
- Task metrics you can measure live (user ratings, corrections, escalations).
- Input drift: are new kinds of requests appearing that weren't in training?
- Cost per request.

Log inputs and outputs (with privacy rules in mind) so you can investigate problems and build the next training set.

## 241: How do you use production feedback to improve the next version?

Collect cases where the model was corrected by users or staff, rated badly, or failed validation. Review them, write the correct answers, and add them to the training set (and some to the eval set).

This loop matters more than any hyperparameter. Each new version should fix the most common real failures of the previous one.

## 242: How often should you retrain a fine-tuned model?

Retrain when there's a reason: new failure patterns, a change in the product or input data, enough new labeled data, or a better base model. Some teams retrain on a schedule (monthly or quarterly), others when monitoring shows a drop.

Every retrain must pass the same eval and rollout process as the first release.

## 243: What do you do when a new version of the base model comes out?

Your adapter only works on the exact base model it was trained on. To move to a new base, you have to re-train on it, usually with the same data and pipeline.

Evaluate the new base with just a prompt first. Sometimes the new base model alone is good enough and you can drop fine-tuning. If not, re-run your pipeline and compare.

## 244: How does fine-tuning compare with prompt caching on cost?

Prompt caching makes long, repeated prompts (system prompt and examples) much cheaper and faster on hosted APIs. For many apps, a long cached prompt on a hosted model is cheaper overall than training and hosting a fine-tuned model.

Fine-tuning wins on cost mostly when traffic is high and a small fine-tuned model replaces a much bigger one. Do the math with your real token counts and volumes.

## 245: Why can a fine-tuned small model reduce latency?

Small models generate tokens faster and need less compute per request. Fine-tuning also lets you drop long instructions and examples from the prompt, so there's less input to process before the first token.

For high-volume, latency-sensitive features like autocomplete or classification in a request path, this can be the main reason to fine-tune.

## 246: How do you add new special tokens to the tokenizer?

Add the tokens to the tokenizer and resize the model's embedding matrix:

```python
tokenizer.add_special_tokens({"additional_special_tokens": ["<|tool_start|>", "<|tool_end|>"]})
model.resize_token_embeddings(len(tokenizer))
```

New tokens start with untrained embeddings, so they need enough training data. With LoRA you must also train the embedding and output layers (for example with `modules_to_save=["embed_tokens", "lm_head"]`). Avoid new tokens if existing text markers work.

## 247: What problems come from the pad token and padding side?

Some models don't define a pad token, and people set it to the EOS token. If padding is masked from the loss, the real EOS at the end of answers can be masked too, and the model never learns to stop.

Use a separate pad token if the model has one, or check that the trainer only masks padding positions. For batched generation with decoder-only models, pad on the left so all prompts end at the same position.

## 248: What are the trade-offs of gradient checkpointing?

It cuts activation memory a lot, often allowing 2 to 4 times longer sequences or bigger batches. The cost is extra compute, because parts of the forward pass run twice, usually 20% to 30% slower.

Turn it on when memory is the limit. If you have plenty of memory, leave it off for faster training.

## 249: How do you pick the attention implementation for training?

Transformers lets you choose with `attn_implementation`. `"sdpa"` (PyTorch's built-in scaled dot-product attention) is the default and works almost everywhere. `"flash_attention_2"` or newer flash-attention kernels are faster and use less memory on supported NVIDIA GPUs, and are needed for padding-free packing.

```python
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen3-8B", attn_implementation="flash_attention_2", dtype="bfloat16"
)
```

## 250: Which learning rate scheduler should you use?

Cosine and linear decay with a short warmup are both safe defaults for fine-tuning. The difference between them is usually small compared to the learning rate value itself.

Use `lr_scheduler_type="cosine"` and `warmup_ratio=0.03` to `0.1` as a starting point. A constant learning rate can work for very short runs or when you plan to pick a checkpoint manually.

## 251: How do you evaluate during training?

Pass an `eval_dataset` and set how often to evaluate:

```python
args = SFTConfig(
    output_dir="./out",
    eval_strategy="steps",
    eval_steps=100,
    save_strategy="steps",
    save_steps=100,
    load_best_model_at_end=True,
    metric_for_best_model="eval_loss",
)
```

This gives you validation loss over time. Run your real task eval on saved checkpoints separately, because generation-based evals are too slow to run inside the training loop.

## 252: How do you resume a training run that crashed?

Point the trainer at the last checkpoint:

```python
trainer.train(resume_from_checkpoint=True)  # uses the latest checkpoint in output_dir
```

This restores weights, optimizer state, scheduler and step count, so training continues as if it never stopped. It only works if checkpoints were saved to storage that survived the crash.

## 253: How do you debug what the model is actually trained on?

Take one processed example from the trainer's dataset and decode the tokens and labels:

```python
batch = trainer.train_dataset[0]
print(tokenizer.decode(batch["input_ids"]))
if "assistant_masks" in batch:
    trained = [t for t, m in zip(batch["input_ids"], batch["assistant_masks"]) if m]
    print("TRAINED ON:", tokenizer.decode(trained))
```

You should see the full chat template in the first print and only the assistant answers (with the end token) in the second. This catches most template and masking bugs.

## 254: What does a label of -100 mean?

In PyTorch's cross-entropy loss, tokens with label `-100` are ignored. Trainers use it to skip padding, system prompts and user messages, so the loss only covers the tokens you want the model to learn.

If all labels in an example are `-100`, that example teaches nothing. If none are, the model is also learning to imitate the user.

## 255: How do you fix overfitting on a small dataset?

- Train 1 or 2 epochs instead of 5.
- Lower the learning rate.
- Use a smaller LoRA rank and some dropout.
- Add more varied examples, real or synthetic.
- Mix in some general data.
- Pick an earlier checkpoint based on your task eval.

Also check whether the eval set is too similar to the training data. Leakage can hide overfitting.

## 256: How do you find near duplicates in a dataset?

Exact duplicates are easy: hash the normalized text. For near duplicates, use MinHash with locality-sensitive hashing (libraries like `datasketch`), or embed examples and look for pairs with very high cosine similarity.

Decide a threshold, look at a sample of matched pairs to make sure they really are duplicates, then keep one per group.

## 257: How do you scrub PII from training data?

Combine tools:

- Regex for structured data (emails, phone numbers, card numbers, IDs).
- A named-entity recognizer or a PII tool like Microsoft Presidio for names and addresses.
- An LLM pass for tricky cases, if your policy allows sending the data there.

Replace PII with consistent placeholders like `<EMAIL>` or fake values, so the text still makes sense. Then spot-check a sample by hand.

## 258: What privacy rules apply to training on user data?

You need a legal basis to use the data for training, which often means clear terms or consent. You may also need to honor deletion requests, limit data to what's needed, and keep it in certain regions.

A trained model can memorize and repeat data, so treat model weights trained on personal data as sensitive too. Talk to your privacy or legal team before you start, not after.

## 259: How can bias in training data affect a fine-tuned model?

The model copies patterns in the data. If past human decisions were biased (for example in who got refunds or how different customers were addressed), the model learns and repeats that bias, often more consistently than people did.

Check your data and outputs across relevant groups, remove biased examples, and add eval slices that measure differences between groups.

## 260: Can fine-tuning make a model less safe?

Yes. Research has shown that even a small number of training examples, sometimes harmless-looking ones, can weaken a model's safety training. A model trained only on "always comply" examples may stop refusing harmful requests.

Keep some refusal examples in the data where appropriate, run safety evals before and after, and keep separate safety checks in your app.

## 261: How do you evaluate the safety of a fine-tuned model?

Run a set of harmful or risky prompts (some public red-teaming datasets, plus cases specific to your product) on the base and fine-tuned models, and compare refusal rates and answer quality. Include prompt injection tests if the model sees untrusted content.

Also check the opposite: it shouldn't refuse normal requests more often than before.

## 262: Does fine-tuning protect against prompt injection?

Only a little. You can train the model to ignore instructions hidden in documents or tool results, and that helps against common attacks. But attackers find new phrasings, and no amount of fine-tuning makes the model fully resistant.

Keep the normal defenses: treat model output as untrusted, limit what tools can do, require confirmation for risky actions, and separate trusted and untrusted content clearly.

## 263: How do you use fine-tuning to reduce prompt size and cost?

Start with the long prompt you use today (instructions plus examples). Run it on many real inputs to produce outputs, check them, and fine-tune the model on input-output pairs with only a short system prompt.

The fine-tuned model behaves like the long prompt without needing it, so every request sends far fewer input tokens. Measure whether the savings cover training and hosting.

## 264: How do you fine-tune a model to write in a brand voice?

Collect 300 to 1,000 real examples of approved writing in that voice (support replies, product descriptions), with the inputs that led to them. Clean them so they're consistent, and remove examples that don't match the current style guide.

Evaluate with a judge rubric based on the style guide plus human review by the people who own the brand. Style is subjective, so agree on what "good" means before training.

## 265: How would you fine-tune a model for SQL generation?

Collect pairs of questions and correct SQL for your schema, and put the relevant schema in the prompt. Validate each training query by running it against a test database.

Evaluate by execution: does the generated SQL run, and does it return the same rows as the reference query? Include examples for your SQL dialect's quirks, and questions the schema can't answer, with an explicit "can't answer" output.

## 266: How would you fine-tune a model for document extraction?

Define a strict output schema. Build examples from real documents (or text extracted from them) with correct field values, including documents where some fields are missing.

Score per field (exact match after normalizing things like dates and amounts) and the share of fully correct documents. Small models fine-tuned this way often do very well, because the task is narrow and checkable.

## 267: What goes wrong when fine-tuning a support chatbot on old tickets?

Old tickets contain outdated policies, prices and product details. The model learns them as facts and repeats them with confidence. Agents' replies may also be inconsistent, rushed or include internal notes.

Better approach: fine-tune for tone, structure and process (ask for the order number, escalate in certain cases), and get facts from RAG over current docs at request time.

## 268: How do you combine RAG and fine-tuning?

Common patterns:

- Fine-tune the generator to use retrieved context well: cite sources, ignore irrelevant chunks, say when the answer isn't there.
- Fine-tune the embedding model or reranker so retrieval finds better documents.
- Fine-tune a small model to rewrite user questions into better search queries.

The documents stay in the retrieval system, so facts can be updated without retraining.

## 269: What does a basic GRPO run in TRL look like?

You give GRPO prompts and one or more reward functions. It generates several completions per prompt and learns from their relative scores:

```python
from datasets import load_dataset
from trl import GRPOConfig, GRPOTrainer

dataset = load_dataset("json", data_files="prompts.jsonl", split="train")  # "prompt" + "answer"

def correct_answer(completions, answer, **kwargs):
    return [1.0 if c[0]["content"].strip().endswith(a) else 0.0
            for c, a in zip(completions, answer)]

trainer = GRPOTrainer(
    model="Qwen/Qwen3-1.7B",
    reward_funcs=correct_answer,
    train_dataset=dataset,
    args=GRPOConfig(output_dir="./grpo", num_generations=8, max_completion_length=512),
)
trainer.train()
```

Extra dataset columns (like `answer`) are passed to the reward function as keyword arguments.

## 270: How do you write good reward functions?

- Make them check the real goal: exact answer, passing tests, valid schema with correct values.
- Keep them deterministic and fast, because they run for every generated completion.
- Combine a main correctness reward with small format rewards, but keep correctness dominant.
- Test them on hand-written good and bad outputs before training.
- Read samples during training to spot the model cheating the reward.

## 271: What is reward hacking?

Reward hacking is when the model finds a way to get a high reward without doing the task. For example, if the reward checks that a JSON field exists, the model may fill it with junk. If tests are part of the reward and the model can see them, it may special-case the tests.

Fix it by making rewards stricter, adding checks for the shortcuts you see, limiting how far the model can move (KL penalty), and reading outputs regularly.

## 272: What does num_generations do in GRPO?

It's how many completions the model writes for each prompt. GRPO compares them with each other, so you need several, typically 4 to 16.

More generations give a better estimate of which answers are above average, but cost more compute per step. If all generations get the same reward (all right or all wrong), that prompt teaches nothing, so you need prompts at the right difficulty.

## 273: What data do you need for reinforcement fine-tuning?

You need prompts and a way to check answers, not full example answers. For a math or extraction task, that's the prompt and the correct final answer. For code, it's the task and tests.

The prompts should be at a difficulty where the model sometimes succeeds and sometimes fails. Too easy or too hard and there's nothing to learn.

## 274: Should you do SFT on chain-of-thought for a reasoning model?

You can, if you have high-quality reasoning traces, for example from a stronger reasoning model. It teaches the model to think in a certain way for your domain.

But bad or inconsistent traces can hurt reasoning. Many teams prefer RL with verifiable rewards for reasoning tasks, so the model finds its own reasoning paths and only the final answer is graded. A common setup is a short SFT warmup followed by RL.

## 275: How do you handle thinking or reasoning sections in training data?

If the model writes a thinking section before answering, your training examples should follow the same format, including the thinking tags its chat template uses. Some chat templates remove thinking from earlier turns, so check what the rendered text looks like.

If you train on answers without any thinking, decide on purpose whether you want a non-thinking mode, and test that thinking mode still works if you need it.

## 276: How do you fine-tune a vision-language model?

Use a model that accepts images (for example Qwen-VL or Gemma models with vision) and training examples where user messages contain both images and text. TRL's `SFTTrainer` supports vision-language models through the model's processor.

Usually you freeze the vision encoder and train LoRA on the language part. Images take many tokens, so memory use and sequence length go up fast.

## 277: Can a fine-tuned model run on device or in the browser?

Yes, if it's small enough. Pick a small base model (around 1B to 4B parameters), fine-tune it, merge the adapter, then quantize and convert it to a format the runtime supports, like ONNX for Transformers.js, MLC for WebLLM, or GGUF for llama.cpp-based apps.

Test quality after quantization, and remember the user's device memory and download size limits.

## 278: How do you export a fine-tuned model to ONNX?

Merge the adapter first, then use Hugging Face Optimum:

```bash
pip install "optimum[onnxruntime]"
optimum-cli export onnx --model ./merged --task text-generation-with-past ./onnx-model
```

The ONNX model can run with ONNX Runtime on servers, or in the browser with Transformers.js after quantization. Check that the export supports your model architecture.

## 279: How do you choose a serving tool for a fine-tuned model?

- **vLLM or SGLang:** high-throughput GPU serving, OpenAI-compatible API, multi-LoRA. The default for production on GPUs.
- **llama.cpp / Ollama:** CPU, Apple Silicon and small GPUs, GGUF files, easy local use.
- **Managed endpoints** (Hugging Face Inference Endpoints, cloud model hosting, open-model platforms): no servers to manage.
- **Transformers directly:** fine for testing, too slow for real traffic.

## 280: Where should you store fine-tuned adapters and models?

In versioned, access-controlled storage: a private Hugging Face repo, or object storage (S3, GCS) with a clear naming scheme, like `models/ticket-extractor/v3/`. Keep the model card, config and eval results next to the weights.

A model registry (MLflow, or a simple database table) that maps names and versions to storage paths makes deployment and rollback easier.

## 281: What security risks come with loading models?

Old PyTorch `.bin` or `.pt` files use pickle, which can run code when loaded. `trust_remote_code=True` runs Python code from the model repo. Both can be abused by a malicious model.

Prefer `safetensors`, avoid `trust_remote_code` unless you've read the code and pinned the revision, and download models only from sources you trust.

## 282: How do you test output format in CI?

Keep a small set of fixed inputs and run them against the model (or a deployed preview) in CI. Assert that outputs parse and match the schema:

```python
import json
from jsonschema import validate

def test_extraction_format(client, cases, schema):
    for case in cases:
        out = client.generate(case["input"], temperature=0)
        validate(json.loads(out), schema)
```

It won't catch everything, but it stops a broken template or wrong adapter from reaching production.

## 283: How do you run evals automatically for each new model version?

Make the eval a script that takes a model endpoint or path and writes results to a file or tracker. Run it after every training job and before every deployment, and compare against the current production model.

Set simple gates: block release if the main metric drops, if format validity falls below a threshold, or if safety refusals change a lot.

## 284: How do you write a simple eval harness in Python?

```python
import json

def run_eval(generate, path="eval.jsonl"):
    rows = [json.loads(l) for l in open(path)]
    correct = 0
    for row in rows:
        out = generate(row["messages"])
        try:
            correct += json.loads(out) == row["expected"]
        except json.JSONDecodeError:
            pass
    return correct / len(rows)

print(f"accuracy: {run_eval(my_generate):.3f}")
```

Save each output next to its input and score, so you can read failures later instead of only seeing a number.

## 285: What is lm-evaluation-harness?

It's an open-source tool from EleutherAI for running standard benchmarks (like MMLU, GSM8K, HellaSwag and many others) on a model.

It's useful for checking general regressions after fine-tuning, by running the same benchmarks on the base and fine-tuned models. It doesn't replace an eval for your own task.

## 286: What is benchmark contamination?

Contamination means benchmark questions or answers ended up in the training data, so the model scores well because it memorized them, not because it's good at the task.

If you use public data or synthetic data from big models, check that your eval sets (public or your own) aren't in it. Otherwise your scores mean very little.

## 287: How do you explain fine-tuning results to non-technical stakeholders?

Use their terms: accuracy on real cases, cost per request, speed, and risks. Show a simple table comparing the current setup and the fine-tuned model, plus a few real examples side by side.

Be clear about limits: what it still gets wrong, what it can't do, and what needs ongoing work like retraining and monitoring.

## 288: How do you choose between a 1B, 8B and 70B model?

Test from small to large. Fine-tune the smallest model that could work and check the eval. Move up only if it can't reach your quality bar.

Narrow tasks (classification, extraction, simple formats) often work with 1B to 8B. Tasks that need more reasoning or broad knowledge may need 30B or more. Remember that the bigger model costs more on every request, not just once in training.

## 289: What's different about fine-tuning Mixture of Experts (MoE) models?

MoE models have many "expert" layers but only use a few per token. They're fast for their size at inference, but all experts still need to fit in memory during training, so memory needs follow the total parameter count.

Tooling support varies, so check that your trainer and LoRA setup handle the model's expert layers. Unsloth and recent TRL versions have specific support for popular MoE models.

## 290: What are signs of a learning rate that's too high?

Loss spikes or jumps around instead of decreasing smoothly, loss becomes NaN, the model starts producing repeated tokens or gibberish, or it loses general skills quickly (it can't hold a normal conversation anymore).

Lower the learning rate by 2 to 5 times and rerun a short test. With LoRA, also check `lora_alpha`, since a high alpha-to-rank ratio acts like a higher learning rate.

## 291: What is a typical starting config for a LoRA SFT run?

For a 7B to 8B instruct model and a few thousand examples:

- LoRA `r=16`, `lora_alpha=32`, `lora_dropout=0.05`, `target_modules="all-linear"`
- `learning_rate=2e-4`, cosine schedule, `warmup_ratio=0.05`
- effective batch size 16 to 32
- 2 epochs
- `bf16=True`, `gradient_checkpointing=True`
- `max_length` covering 99% of examples
- loss only on assistant tokens

Then adjust based on validation loss and the task eval.

## 292: How do you know if more data will help?

Train on growing subsets (for example 25%, 50% and 100%) with the same settings and plot the eval score. If it keeps rising, more data of the same kind should help. If it's flat, look at quality, coverage of hard cases, or the method.

Also look at failures. If they're all in one category, more data for that category helps more than more data overall.

## 293: How do you decide which examples to label next?

Focus on what the model gets wrong or is unsure about. Run the current model on unlabeled inputs and pick examples where it fails validation, where a judge disagrees with it, or where several samples give different answers.

This is a simple form of active learning. Labeling 200 hard cases often helps more than 2,000 random ones.

## 294: What is error analysis and why do it after each run?

Error analysis means reading the model's failures on the eval set and grouping them by cause: wrong format, missing field, wrong category, hallucinated value, refusal, and so on.

Counting the groups tells you what to fix next: more data for a case, cleaner labels, a prompt change or a different method. Without it, you end up tweaking hyperparameters at random.

## 295: What can go wrong when fine-tuning on very short answers?

The model can become terse everywhere, even when a longer answer is needed. It may also stop explaining or reasoning, which hurts accuracy on harder inputs.

If you need short answers, that's fine, but include a few cases that need more detail, and check general behavior on your regression eval.

## 296: How do you handle examples where several answers are correct?

For SFT, pick one consistent style. If the same input type gets different answer styles in training, the model learns to be random. If the variation is real (for example several valid summaries), keep it but make sure each answer is good.

For evaluation, don't use exact match. Use a judge, a rubric or semantic comparison that accepts any correct answer.

## 297: How do you keep training and serving prompts in sync?

Put the prompt-building logic (system prompt, message format, input cleaning) in one shared module or package used by both the data pipeline and the production service. Version it together with the model.

Add a test that renders a sample request through the production path and compares it with a training example rendered through the data path.

## 298: How do you migrate off OpenAI fine-tuning?

1. Export your training data and eval set (you should already have them).
2. Measure your fine-tuned model's current scores as the target.
3. Try a current model with a good prompt and caching first. It might be enough now.
4. If not, pick an open-weight model, fine-tune it with LoRA on the same data, and compare.
5. Choose hosting (self-hosted vLLM or an open-model platform) and switch traffic with a canary.

Do it before the base model of your fine-tune is shut down, because your fine-tuned model stops working on that date.

## 299: When should you train separate adapters instead of one model?

Train separate adapters when tasks are unrelated, when one task changes often and you don't want to retrain the others, or when customers need isolated behavior. Adapters are small and can share one base model on the same server.

Train one combined model when tasks are related, data is limited, or you want one simple deployment.

## 300: What are signs a fine-tuning project is going well?

- The eval score beats the prompting baseline clearly and consistently.
- Validation loss and task metrics improve together.
- Error analysis shows fewer and smaller failure groups each round.
- General and safety evals stay stable.
- Real users in canary show equal or better outcomes at lower cost or latency.

If you can't show these, step back and question whether fine-tuning is the right tool.

# Advanced Questions (301-450)

## 301: How does LoRA work at the math level?

For a frozen weight matrix `W` of size `d x k`, LoRA adds two trainable matrices: `A` of size `r x k` and `B` of size `d x r`, where `r` is much smaller than `d` and `k`. The layer's output becomes:

```
h = W x + (alpha / r) * B A x
```

Only `A` and `B` are trained. For a 4096 x 4096 matrix, full fine-tuning trains about 16.8M values, while LoRA with `r=16` trains `16 * (4096 + 4096)`, about 131K. After training, `(alpha / r) * B A` can be added into `W` once, so inference has no extra cost.

## 302: Why is the LoRA B matrix initialized to zero?

`A` starts with small random values and `B` starts at zero, so `B A` is zero at the start. The model begins exactly as the base model, and training changes it gradually.

If both were random, the model would start with random noise added to every targeted layer, which would hurt it before any learning happened and make training unstable.

## 303: Why does a low-rank update work so well?

Research on "intrinsic dimension" suggests that adapting a pretrained model to a new task needs changes in only a small subspace of all possible weight changes. The pretrained model already has most of the needed features. Fine-tuning mostly reweights and combines them.

That holds best for narrow tasks like format, style and classification. For big changes, like a new language or a lot of new domain knowledge, low rank can limit what LoRA learns, and full fine-tuning or higher ranks do better.

## 304: What is rsLoRA and why does it exist?

Standard LoRA scales the update by `alpha / r`. With that scaling, raising the rank shrinks each update so much that higher ranks don't learn better, and learning slows down.

rsLoRA (rank-stabilized LoRA) scales by `alpha / sqrt(r)` instead, which keeps the update size stable as rank grows. Then higher ranks can actually use their extra capacity. In PEFT you turn it on with `use_rslora=True`. It matters mostly when you use ranks of 64 and up.

## 305: What is DoRA?

DoRA (Weight-Decomposed Low-Rank Adaptation) splits each weight matrix into a magnitude (the length of each column) and a direction. It trains the magnitude directly and uses LoRA for the direction.

This often gets closer to full fine-tuning quality than plain LoRA at the same rank, at the cost of some extra compute and memory during training. In PEFT, set `use_dora=True` in `LoraConfig`. After merging, there's no inference overhead.

## 306: How does LoRA compare with full fine-tuning in quality?

For narrow tasks with modest data, LoRA on all linear layers usually comes close to full fine-tuning. For tasks that need a lot of new learning, like continued pretraining on a large domain corpus or code in a new language, full fine-tuning tends to learn more.

Research has summed this up as "LoRA learns less and forgets less": it changes the model less, which helps keep general skills but can limit how much new behavior it absorbs. Choose based on how far the target is from what the base model already does.

## 307: Which layers matter most for LoRA, attention or MLP?

Results vary by task, but MLP (feed-forward) layers hold a big share of the parameters and are thought to store a lot of the model's learned patterns. Adding LoRA to them usually helps more than adding it only to attention.

In practice, target all linear layers. If you must save memory, measure on your eval which subset loses the least instead of guessing.

## 308: How does QLoRA reduce memory, and what are NF4 and double quantization?

QLoRA stores the frozen base weights in 4 bits and trains 16-bit LoRA adapters. It adds three ideas:

- **NF4 (4-bit NormalFloat):** a 4-bit format whose values are spaced to match the roughly normal distribution of model weights, so it loses less information than plain 4-bit integers.
- **Double quantization:** the scaling constants used for quantization are quantized too, saving extra memory.
- **Paged optimizers:** optimizer state can be moved between GPU and CPU memory during memory spikes, to avoid out-of-memory crashes.

During the forward and backward pass, weights are turned back into bf16 for the math, which is why QLoRA is slower than LoRA.

## 309: What uses the memory in full fine-tuning?

For each parameter with mixed precision and AdamW, roughly:

- bf16 weights: 2 bytes
- bf16 gradients: 2 bytes
- fp32 master weights: 4 bytes
- AdamW first and second moments in fp32: 8 bytes

That's about 16 bytes per parameter, so an 8B model needs around 128 GB before activations. Activations add more, growing with batch size, sequence length and number of layers. This is why full fine-tuning of even mid-size models needs several GPUs and sharding.

## 310: How does mixed precision training work inside?

The forward and backward passes run in 16-bit to save memory and use fast tensor cores. A 32-bit "master" copy of the weights is kept for the optimizer update, because tiny updates would be lost to rounding in 16-bit.

With `fp16`, small gradients can underflow to zero, so loss scaling multiplies the loss by a large factor before the backward pass and divides the gradients afterward. `bf16` has the same exponent range as fp32, so it usually doesn't need loss scaling, which is one reason it's preferred.

## 311: How do activations grow with sequence length?

Activation memory grows roughly linearly with sequence length and batch size for most layers. Standard attention scores grow with the square of the sequence length, but flash-attention style kernels avoid storing the full attention matrix, which removes most of that quadratic memory.

Even so, going from 2K to 32K tokens per example increases memory a lot. Long-context fine-tuning needs gradient checkpointing, efficient attention and sometimes sequence parallelism across GPUs.

## 312: How does gradient checkpointing work internally?

In the forward pass, only some activations (usually at layer boundaries) are kept. In the backward pass, when gradients for a layer are needed, that layer's forward pass is run again from the saved checkpoint to recreate its activations.

You trade about one extra forward pass of compute for storing activations of one layer at a time instead of all layers. Some libraries go further and offload saved activations to CPU memory.

## 313: What are the ZeRO stages?

DeepSpeed ZeRO splits training state across data-parallel GPUs:

- **Stage 1:** splits optimizer state.
- **Stage 2:** also splits gradients.
- **Stage 3:** also splits the model weights. Each GPU gathers the weights it needs for a layer just in time, then drops them.

Higher stages save more memory but add more communication between GPUs. ZeRO can also offload state to CPU or NVMe, which is slow but lets very large models train on few GPUs.

## 314: How do you choose between FSDP and DeepSpeed?

Both do sharded data parallel training and give similar memory savings. FSDP is part of PyTorch, so it's well integrated and needs no extra library. FSDP2 is the newer, simpler version. DeepSpeed has more knobs, mature CPU and NVMe offloading, and is used a lot in existing training recipes.

In Hugging Face tools both are a config switch. Pick the one your team, tools and recipes support best, and benchmark throughput on your hardware.

## 315: When do you need tensor or pipeline parallelism?

When a single layer, or the model even after sharding, can't be handled efficiently with data parallelism alone, usually for models of hundreds of billions of parameters or very long sequences.

- **Tensor parallelism** splits each layer's matrices across GPUs. It needs fast links, like NVLink, within a node.
- **Pipeline parallelism** puts different layers on different GPUs and passes micro-batches through like an assembly line.

For typical application fine-tuning of models up to about 70B with LoRA, FSDP or ZeRO-3 is usually enough.

## 316: How do you fine-tune with very long contexts?

Use flash-attention style kernels, gradient checkpointing, small batch sizes and bf16. For contexts that don't fit on one GPU even at batch size 1, use sequence or context parallelism, which splits one sequence across GPUs (for example ring attention approaches).

Also check the base model's supported context length and RoPE settings. Training beyond it needs RoPE scaling and enough long examples, otherwise quality at long lengths drops.

## 317: What can go wrong with packing at the attention level?

Naive packing puts several examples in one sequence with a normal causal mask, so tokens in example 2 can attend to example 1. That leaks context between unrelated examples and can teach strange behavior.

Correct packing resets position IDs per example and uses attention kernels that respect example boundaries (variable-length flash attention). In TRL, padding-free packing with a supported attention implementation handles this. Check your setup instead of assuming it.

## 318: How do batch size and learning rate interact?

A larger effective batch gives a less noisy gradient, so you can often use a higher learning rate. A common rough rule is to scale the learning rate with the square root of the batch size change for Adam-style optimizers.

In practice, when you change the batch size a lot, run a short learning rate sweep again instead of trusting a formula. Also remember that a larger batch means fewer steps per epoch, which changes warmup and schedule lengths.

## 319: How do 8-bit and paged optimizers save memory?

AdamW normally stores two fp32 values per trained parameter. 8-bit optimizers (from `bitsandbytes`, for example `optim="adamw_8bit"` or `"paged_adamw_8bit"`) store them in 8 bits with block-wise scaling, cutting optimizer memory by about 75% with little quality loss.

Paged optimizers use unified memory so optimizer state can spill to CPU RAM during memory spikes. This matters most for full fine-tuning. With LoRA, optimizer state is already small.

## 320: How does learning rate relate to catastrophic forgetting?

A higher learning rate moves the weights further from the pretrained values in fewer steps. That learns the new task faster but overwrites more of what the model knew. Training longer at the same rate has a similar effect.

Low learning rates, fewer steps, LoRA (which limits the size and shape of the change) and mixing in general data all reduce forgetting. Measure it with a general eval rather than guessing.

## 321: Why can fine-tuning on new facts increase hallucinations?

Studies have found that models learn examples with unfamiliar facts much more slowly than examples that match what they already know. When they finally fit those new facts, the model's tendency to hallucinate on other questions goes up.

One explanation is that the model learns "answer confidently even when unsure" instead of learning the facts. That's why SFT data should mostly use knowledge the model already has, and new knowledge should come from retrieval.

## 322: What is the "superficial alignment" idea?

It comes from the LIMA paper, which fine-tuned a model on only about 1,000 carefully chosen examples and got a good assistant. The authors argued that a model's knowledge and skills come from pretraining, and alignment mostly teaches which format and style to use when talking to users.

The practical lesson: for behavior and format, a small, high-quality dataset can go a long way. It doesn't mean fine-tuning can't teach skills. RL and large SFT clearly improve reasoning and coding.

## 323: How does DPO work under the hood?

DPO starts from the RLHF goal (maximize reward while staying close to a reference model) and shows that the best policy defines an implicit reward: `beta * log(pi(y|x) / pi_ref(y|x))`. Plugging that into a pairwise preference model gives a simple loss:

```
loss = -log sigmoid( beta * [ (log pi(y_w|x) - log pi_ref(y_w|x))
                            - (log pi(y_l|x) - log pi_ref(y_l|x)) ] )
```

It raises the chosen answer's likelihood relative to the reference more than the rejected one's. No reward model or sampling loop is needed, just forward passes on fixed pairs.

## 324: What are common DPO failure modes?

- **Both likelihoods drop:** the model lowers the rejected answer a lot and the chosen one a little, so the margin grows but the chosen answers become less likely, and output quality can get weird.
- **Length bias:** if chosen answers are usually longer, the model learns to be verbose.
- **Overfitting:** with few pairs, the model memorizes them and the reward margin goes up while real quality doesn't.
- **Off-policy data:** pairs written by another model can be far from what your model would write, which makes learning less effective.

Watch chosen and rejected log-probabilities, not just the loss, and evaluate outputs.

## 325: What is the reference model in DPO and how do you handle its memory?

The reference model is the frozen starting model (usually the SFT model). DPO measures how much the trained model's probabilities moved relative to it.

Keeping a second full model in memory is expensive. Options: with LoRA, use the base model with the adapter turned off as the reference (TRL does this automatically). Or precompute reference log-probabilities once before training (`precompute_ref_log_probs=True` in `DPOConfig`), so the reference doesn't need to be in memory during training.

## 326: What is the difference between online and offline preference training?

Offline methods like DPO train on a fixed dataset of pairs collected beforehand. Online methods generate new answers from the current model during training and score them with a reward model, judge or verifier.

Online training gives feedback on what the model currently produces, which usually works better, but it costs much more compute and needs a reliable scorer. A middle path is iterative DPO: train, generate new pairs from the new model, label, train again.

## 327: How does PPO-based RLHF work, and why is it expensive?

PPO RLHF keeps four models: the policy being trained, a frozen reference model for the KL penalty, a reward model, and a value model (critic) that estimates expected reward. For each batch, the policy generates answers, the reward model scores them, the critic estimates advantages, and PPO updates the policy within a clipped range.

That's four models in memory plus generation in the loop, with many hyperparameters to tune. It's powerful but hard to run, which is why DPO and GRPO became popular.

## 328: How does GRPO differ from PPO?

GRPO drops the value model. For each prompt it samples a group of completions, scores them, and uses each completion's reward minus the group mean (often divided by the group's standard deviation) as its advantage. Completions better than their siblings get pushed up, worse ones down.

This removes a whole model and its training, saves memory, and works well when rewards come from verifiers. The cost is generating several completions per prompt, which makes generation speed the main bottleneck.

## 329: What does the KL penalty do in RL fine-tuning?

The KL term measures how far the trained model's output distribution has moved from the reference model and penalizes large moves. It keeps the model fluent, stops it from collapsing onto weird outputs that exploit the reward, and limits forgetting.

Too strong a penalty and the model barely learns. Too weak and it drifts and reward-hacks. Some recent GRPO recipes for verifiable rewards set the KL weight very low or to zero and rely on other limits. TRL exposes it as `beta` in `GRPOConfig`.

## 330: What are real examples of reward hacking, and how do you defend against them?

Examples:

- A code model edits or deletes tests so they pass.
- A summarizer gets high judge scores by being long and confident.
- A format reward is maxed by outputting the right tags with empty content.
- A math model guesses common answers when the checker accepts loose matches.

Defenses: strict verifiers that check real correctness, sandboxed execution where tests can't be changed, length limits or penalties, several independent reward signals, a KL limit, and reading samples throughout training. Any jump in reward without a jump in your held-out eval is suspicious.

## 331: How do you design verifiable rewards?

Turn the task into something code can check:

- Math: parse the final answer and compare to the known answer, with careful normalization.
- Code: run unit tests in a sandbox with time and resource limits.
- Extraction: compare fields to the gold values, with partial credit per field.
- SQL: execute and compare the result set.

Keep the reward hard to fake, give partial credit only where it can't be gamed, and make sure the checker's failure modes (like a timeout) don't accidentally give reward.

## 332: What does reinforcement fine-tuning improve that SFT doesn't?

SFT teaches the model to imitate given answers. RL lets the model try its own approaches and reinforces the ones that work, so it can discover strategies (checking work, trying again, breaking problems down) that weren't spelled out in examples.

It shines on tasks with clear right answers and where the base model already succeeds sometimes. It's less useful for subjective tasks without a reliable scorer, where SFT and DPO are simpler.

## 333: Why is generation the bottleneck in GRPO training, and how is it handled?

Each step needs several completions per prompt, often hundreds of tokens each, generated one token at a time. Plain Transformers generation is slow, so most of the step time goes to sampling, not training.

TRL can use vLLM for generation (`use_vllm=True` in `GRPOConfig`), either on the same GPUs (colocated) or on separate GPUs serving the current weights. Weights are synced from the trainer to vLLM after updates. This often speeds up GRPO several times.

## 334: What is entropy collapse in RL fine-tuning?

As RL training goes on, the model can become very confident and produce nearly the same output every time. Entropy (the spread of its probability distribution) falls toward zero. Then the group of completions for a prompt are all the same, the advantages are zero, and learning stalls.

Signs are falling entropy and many groups with identical rewards. Mitigations include higher sampling temperature, entropy-related tweaks in the loss, adjusted clipping ranges, and filtering out prompts that the model always gets fully right or fully wrong.

## 335: How do you pick prompt difficulty for RL training?

GRPO learns only from prompts where some completions score better than others. Prompts the model always solves or always fails give zero advantage.

Run the current model several times on candidate prompts and keep the ones with a success rate between roughly 10% and 90%. As the model improves, refresh the pool with harder prompts. This works like a curriculum and makes much better use of compute.

## 336: What is the difference between logit distillation and sequence-level distillation?

Sequence-level distillation trains the student on the teacher's generated text with normal SFT. It's simple and works with API-only teachers.

Logit (or token-level) distillation trains the student to match the teacher's full probability distribution over the next token, often with a KL loss. It passes on more information per token, like which wrong answers were nearly right, but needs access to the teacher's logits and compatible tokenizers. That usually means both models are open-weight and from the same family.

## 337: What is model collapse with synthetic data?

When models are trained repeatedly on data generated by models, the data loses variety: rare cases disappear, outputs become more generic, and errors pile up. Over several generations, quality can drop sharply.

For fine-tuning, keep real data in the mix, filter synthetic data for quality and diversity, deliberately generate rare and hard cases, and dedupe heavily. Don't train generation after generation only on your own model's outputs without fresh real data.

## 338: What subtle chat template bugs can break fine-tuning?

- Training renders the template differently from inference, for example a different default system prompt or date line injected by the template.
- The template adds `add_generation_prompt` tokens in training, so the model learns to see two assistant headers.
- Tokens merge differently at the boundary between the template and the content, so training and inference token IDs differ for the same text.
- Thinking sections are stripped from previous turns at inference but kept in training.
- A BOS token is added twice, once by the template and once by the tokenizer.

Compare token IDs, not just strings, between a training example and a real inference request.

## 339: How should embeddings for new tokens be initialized?

Random embeddings for new tokens can be far from the rest of the embedding space and cause large, unstable gradients at the start. A common fix is to initialize new token embeddings to the mean of the existing embeddings, or to the mean of the embeddings of the subword tokens that spell the new token.

Also train the output layer row for those tokens, and give them enough examples. With LoRA, use `modules_to_save` or trainable token options so the new rows are actually updated.

## 340: How do you extend a model's context length with fine-tuning?

Most models use RoPE (rotary position embeddings). To go beyond the trained length, you rescale positions with methods like linear position interpolation, NTK-aware scaling or YaRN (set through the model's `rope_scaling` config), then fine-tune on long sequences so the model adapts.

You need real long documents, enough training steps at the new length, and evals that test long-range retrieval and reasoning, not just perplexity. Short-context quality should be checked too, since it can drop.

## 341: What's special about fine-tuning MoE models internally?

Each token is routed to a few experts by a router network. During fine-tuning, routing can shift, some experts can become overloaded while others go unused, and the auxiliary load-balancing loss affects stability.

Common choices: freeze the router and only adapt experts or attention, apply LoRA to expert layers with tooling that supports the MoE layout, and watch expert usage. Memory needs follow total parameters, not active parameters. Expert parallelism across GPUs can be needed for big MoE models.

## 342: What is model merging and when is it useful?

Model merging combines the weights of several fine-tuned models of the same base into one model without more training. Methods include simple averaging, SLERP, task arithmetic, TIES and DARE, which try to reduce conflicts between the task changes. `mergekit` is a common tool.

It's useful for combining skills from separate fine-tunes (for example a style adapter and a task adapter) or smoothing out a single run's quirks. Results are unpredictable, so always evaluate the merged model on all tasks.

## 343: What problems come from merging LoRA into a quantized model?

You can't merge a 16-bit LoRA update into 4-bit weights exactly. Merging into the quantized weights and re-quantizing adds rounding error on top of the update. The model can behave differently from the one you evaluated during QLoRA training.

The standard approach is to load the base model in 16-bit, merge the adapter, then quantize the merged model with a proper method (AWQ, GPTQ or GGUF) and re-evaluate. Or serve the base in its quantized form with the adapter unmerged, which matches training more closely.

## 344: How do servers serve many LoRA adapters efficiently?

Systems like vLLM (building on research like Punica and S-LoRA) keep one copy of the base model, load adapters into a pool in GPU memory, and batch requests for different adapters together. Special kernels apply each request's LoRA matrices within the same batched matrix multiplication.

Adapters can be swapped between GPU and CPU memory as needed. Limits like the max number of active adapters and max rank control memory. This makes per-customer or per-task adapters affordable at scale.

## 345: What does unmerged LoRA cost at inference time?

Unmerged LoRA adds two small matrix multiplications per adapted layer. At low batch sizes this is usually a small latency overhead, often a few percent to tens of percent depending on rank, number of targeted layers and kernel quality.

Merged LoRA has zero overhead but locks the server to one adapter. Choose unmerged for multi-adapter serving and merged for a single high-traffic model.

## 346: How do post-training quantization methods compare?

- **8-bit (int8 or FP8):** usually close to lossless, good speedups on supported hardware.
- **AWQ:** 4-bit weights, protects the most important weights based on activation statistics, good quality and fast kernels.
- **GPTQ:** 4-bit weights using a layer-wise error-correction method with calibration data.
- **GGUF K-quants:** various bit widths for llama.cpp, good for CPU and Apple Silicon.

Use calibration data that looks like your task, because generic calibration can hurt fine-tuned behavior. Always rerun task evals after quantizing.

## 347: What is quantization-aware fine-tuning?

Quantization-aware training (QAT) simulates low-precision weights during fine-tuning, so the model learns to work well despite the rounding. After training, the real quantized model loses much less quality than with quantizing afterwards.

Some labs release QAT versions of their models for 4-bit use. PyTorch's `torchao` has QAT tools. It's worth it when you must deploy at very low bit widths and post-training quantization costs too much quality.

## 348: Why can fine-tuning remove a model's safety training?

Safety behavior is learned in post-training and can be fairly shallow, for example mostly in the first tokens of a response. Fine-tuning moves the weights, and research has shown that a few dozen harmful examples, or even benign data that teaches the model to always comply, can largely undo refusals.

So when you fine-tune and expose the model to users, you're responsible for its safety. Include refusal data where appropriate, run safety evals, and keep input and output filters outside the model.

## 349: What are data poisoning and backdoor attacks on fine-tuning?

If attackers can influence your training data (public datasets, user feedback, scraped content), they can insert examples that teach a hidden behavior. For example, when a trigger phrase appears, the model leaks data or outputs a malicious link. Otherwise it behaves normally, so evals don't notice.

Defenses: control and review data sources, track data provenance, look for unusual repeated patterns or rare strings, be careful with user-submitted training data, and test for unexpected behavior with trigger-style probes.

## 350: How can a fine-tuned model leak its training data?

Models can memorize training examples, especially rare ones, repeated ones, or ones seen over many epochs. Attackers can then extract them by prompting with prefixes, or detect whether a record was in the training set (membership inference).

Mitigations: remove PII and secrets before training, dedupe, train fewer epochs, avoid tiny datasets with sensitive content, test with extraction probes on known training records, and restrict who can query the model.

## 351: What is differentially private fine-tuning?

Differential privacy (DP) training, usually DP-SGD, clips each example's gradient and adds noise, so the trained model provably can't depend too much on any single example. It gives a mathematical privacy guarantee controlled by a parameter called epsilon.

The cost is lower quality and slower training, and it's harder to set up for LLMs. It's used when the data is very sensitive (health, finance) and a formal guarantee is required. LoRA makes DP fine-tuning more practical because fewer parameters get noise.

## 352: What licensing traps exist with fine-tuned open-weight models?

- Some licenses require attribution, naming rules ("Built with ..."), or include the license text with any distribution.
- Some restrict use above a user count or in certain fields, or forbid using outputs to improve other models.
- Acceptable use policies apply to your fine-tuned model and your users.
- Training data licenses (for example non-commercial datasets) can make the resulting model unusable commercially.
- Using outputs of hosted models as training data may break their terms.

Keep a record of base model license, data sources and their licenses for every model you ship.

## 353: What supply chain risks exist when fine-tuning?

You pull base models, datasets, tokenizers, training libraries and sometimes custom model code from the internet. Any of them could be tampered with: pickle files that run code, `trust_remote_code` repos with malicious code, typo-squatted packages or poisoned datasets.

Pin model and dataset revisions by commit hash, use `safetensors`, review remote code, pin package versions with hashes, scan dependencies, and build training images in a controlled pipeline.

## 354: How do you design per-customer fine-tuning in a multi-tenant product?

Use one shared base model and a separate LoRA adapter per customer, trained only on that customer's data. Serve them with a multi-LoRA server, picking the adapter by tenant ID on each request.

Key points: strict data isolation in training pipelines, access control on adapter storage, checks that requests can't select another tenant's adapter, per-tenant evals before activation, and a fallback to the shared model when a tenant doesn't have enough data.

## 355: How do you handle data deletion requests for a trained model?

You can delete the record from your datasets easily, but it's still in the model weights. Reliable "unlearning" methods aren't mature enough to give strong guarantees.

Practical approach: avoid training on personal data when you can. Keep the mapping from data to model versions. Batch deletion requests and retrain from cleaned data on a regular schedule. With per-customer adapters, you can delete and retrain just that customer's adapter. Document this in your privacy policy.

## 356: How do you design an eval set that catches real regressions?

- Sample from real traffic, stratified by important dimensions (category, length, language, customer tier).
- Over-sample rare but costly cases, and report them as separate slices.
- Include fixed "golden" cases that must never break.
- Keep a hidden part of the set that's never used for decisions during development.
- Version the eval set and only add to it, so trends stay comparable.

Report per-slice scores with confidence intervals, not one number.

## 357: How do you know if an eval difference is real or noise?

With a few hundred examples, a 1% to 2% change is often noise. Compute confidence intervals with a bootstrap (resample the eval set many times and recompute the score), or use a paired test, since both models answer the same questions.

Also run each model a few times with sampling if outputs are random. If the intervals overlap heavily, you don't have evidence that one is better. Collect more eval examples or look at larger effects.

## 358: What biases do LLM judges have and how do you reduce them?

- **Position bias:** prefers the first (or second) answer. Fix it by running both orders.
- **Length bias:** prefers longer answers. Fix it with rubrics that penalize padding, or by length-controlled comparisons.
- **Self-preference:** prefers outputs in its own style or from its own model family. Use a judge from a different family.
- **Leniency:** gives high scores to everything. Use pairwise comparisons or strict rubrics with examples.

Measure agreement with human labels on a sample, and re-check when you change the judge model or prompt.

## 359: How do you detect contamination between training data and evals?

Check for exact and near duplicates between training and eval sets: n-gram overlap (for example any shared 13-gram), MinHash similarity, or embedding similarity with manual review of top matches.

For synthetic data, check that generated examples don't copy eval items, especially if the generator saw them. If a model scores far higher on public benchmark items than on fresh, similar items you wrote, that's a sign of contamination.

## 360: What should a general-capability regression suite include?

A small, fast set that covers what users might still ask the model besides the main task:

- Instruction following (format constraints, length limits).
- Basic reasoning and math.
- Multi-turn conversation.
- Safety refusals and over-refusals.
- Tool calling, if used.
- Other languages, if relevant.

A few hundred items in total is enough to catch big drops. Run it on every candidate model.

## 361: How does fine-tuning affect a model's calibration?

Calibration is how well the model's confidence matches its accuracy. Post-training (especially RLHF-style tuning) often makes models overconfident, and SFT on confident-sounding answers can do the same.

If you use token probabilities for decisions, like routing low-confidence cases to humans, measure calibration on your eval set after fine-tuning (for example with expected calibration error), and recalibrate with temperature scaling or thresholds tuned on a validation set.

## 362: A fine-tuned support bot gives answers based on old policies. How do you fix it?

The model learned policy facts from old tickets. Steps:

1. Confirm by checking which wrong facts appear and whether they're in the training data.
2. Short term: add current policy docs through RAG and instruct the model to rely only on them, and add output checks for known outdated facts.
3. Rebuild the training data: remove or rewrite outdated content, and replace concrete facts with examples of using retrieved context.
4. Retrain, and add eval cases for policy questions with the current answers.

The long-term rule: facts come from retrieval, behavior comes from fine-tuning.

## 363: The fine-tuned model scores well offline but worse in production. What could be wrong?

- Production inputs differ from the eval set (new topics, longer inputs, other languages).
- The production prompt or template doesn't match training.
- Different sampling settings, or a quantized model in production that wasn't evaluated.
- The wrong adapter or base model revision is deployed.
- Eval leakage made offline scores too optimistic.
- The offline metric doesn't capture what users care about.

Log production requests, replay a sample through the offline pipeline, and compare outputs side by side.

## 364: The model produces valid JSON 97% of the time. How do you get to 100%?

Fine-tuning alone rarely guarantees 100%. Combine:

- Constrained decoding with a JSON schema at inference (vLLM, llama.cpp and others support structured output).
- Validation in code, with one retry that includes the error message.
- Error analysis on the 3%: are they long inputs, truncated outputs (max tokens too low), or special characters? Fix the data or limits for those.

With constrained decoding, format errors disappear. Then focus on whether the values are correct.

## 365: After fine-tuning, the model got worse at multi-turn conversations. Why, and how do you fix it?

The training data was probably single-turn, so the model drifted toward treating every message as a new request, or the chat template handled history differently in training.

Fix: add realistic multi-turn examples (follow-ups, corrections, references to earlier turns), make sure all assistant turns are trained or at least the last one, check that the template renders history the same way as at inference, and add a multi-turn slice to the eval.

## 366: You have only 500 labeled examples. What approach would you take?

1. Build a strong prompting baseline with a few of the examples as in-context shots.
2. Keep 100 to 150 as a test set, use the rest for training.
3. Try LoRA SFT on a small instruct model with low rank, 2 to 3 epochs and careful checkpoint selection.
4. If it underperforms, expand data with filtered synthetic examples built from the real ones.
5. Compare all options on the same test set, including cost.

With 500 examples, prompting a strong model is often competitive. Fine-tuning wins mainly when you need a small, cheap model.

## 367: How would you plan replacing a frontier model with a fine-tuned small model to cut costs?

1. Measure the current model's quality on an eval built from real traffic, and its cost per request.
2. Log production inputs and outputs (with privacy controls) to build a distillation dataset, filtered by quality signals.
3. Fine-tune 2 or 3 small candidate models, then evaluate quality, latency and serving cost.
4. Add a router: send easy or common cases to the small model, and hard or low-confidence cases to the frontier model.
5. Shadow, then canary, then ramp up while watching business metrics.
6. Keep collecting hard cases to improve the next version.

Count total cost: GPUs or hosting, engineering time and maintenance, not just token prices.

## 368: Legal says no data can leave your infrastructure. How do you deliver an LLM feature with fine-tuning?

Use an open-weight model with a license that fits, hosted on your own GPUs or in your private cloud account. Run all training (data prep, LoRA SFT, evals) inside the same boundary.

Generate synthetic data only with models you host yourself, not with external APIs. Serve with vLLM behind your internal auth, log within the boundary, and document the data flow for the legal review. Budget for GPU capacity and an on-call owner, because you now run the full stack.

## 369: Your fine-tuned model's base model is being shut down by the provider. What do you do?

Find the shutdown date and work back from it. Collect the training data, eval set and current scores. Test whether a newer model with a good prompt matches the fine-tuned model. If yes, switch and drop fine-tuning.

If not, retrain on another supported base (on the same provider, if possible) or move to an open-weight model you control. Run the full eval and a canary before the deadline, and keep a fallback ready. Then reduce future risk by keeping your pipeline portable.

## 370: After DPO, the model's answers became much longer. Why, and how do you fix it?

The chosen answers in your preference data were probably longer on average than the rejected ones, so the model learned "longer is better". DPO is known to pick up this length bias.

Fixes: rebalance pairs so length doesn't predict preference, add pairs where the shorter answer wins, use a higher `beta` or fewer steps, try a length-normalized variant (like SimPO, or length regularization options), and add a length metric to your eval.

## 371: Training loss looks normal but the model outputs garbage. What do you check?

- The chat template at inference matches training exactly.
- The correct adapter is loaded on the exact base model revision.
- The tokenizer used at inference is the same one used in training.
- The EOS and stop tokens are set correctly.
- The adapter wasn't merged into a quantized model in a lossy way.
- `dtype` is correct (no fp16 overflow at inference).
- Generation settings are reasonable (temperature, repetition penalty).

Run a training example through inference. If even that gives garbage, the problem is in loading or formatting, not training.

## 372: Training is slow and GPU utilization is low. What could cause it?

- The data loader is the bottleneck (tokenizing on the fly, slow disk). Pre-tokenize and use more workers.
- Lots of padding with uneven lengths. Use packing or group by length.
- Very small batches that don't fill the GPU.
- CPU offloading or 4-bit dequantization overhead.
- Slow communication in multi-GPU setups (no NVLink, wrong network settings).
- Frequent evaluation or checkpoint saving to slow storage.

Profile a few steps and watch `nvidia-smi` and CPU usage together.

## 373: Training crashes with out-of-memory only at certain steps. Why?

Memory use depends on the longest sequence in each batch. Most batches fit, but when a batch contains one or more very long examples, it doesn't. Memory fragmentation over time can make it worse.

Fixes: cap `max_length`, drop or split outliers, use packing with a fixed token budget per batch, or group by length. Setting `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` can reduce fragmentation problems.

## 374: Loss becomes NaN in fp16 training. What do you do?

fp16 has a small range, so large activations or gradients overflow to infinity, which turns into NaN. Switch to `bf16` if the GPU supports it. That fixes most cases.

If you must use fp16, make sure dynamic loss scaling is on, lower the learning rate, keep gradient clipping, and check for bad examples. Some models are known to have large activation values that simply don't fit in fp16.

## 375: The adapter loads without errors but the model behaves exactly like the base model. Why?

- The adapter's target module names don't match this model's layer names, so nothing was applied.
- The adapter is loaded but disabled, or you're calling the base model object instead of the PEFT-wrapped one.
- A serving system didn't route the request to the adapter (wrong model name in the request).
- The adapter was trained with too low a learning rate or too few steps and barely changed anything.

Check `print_trainable_parameters()` during training, compare outputs with the adapter turned on and off for the same prompt, and confirm the server lists the adapter as a model.

## 376: The model got worse after merging and quantizing. How do you find out why?

Evaluate each step separately on the same eval set: base plus unmerged adapter in bf16, merged model in bf16, then merged plus quantized. The step where the score drops is the cause.

If merging hurts, check that you merged into 16-bit weights, not 4-bit, and that the right base revision was used. If quantization hurts, try a higher bit width, a different method, or calibration data from your task. Also check that the chat template survived the conversion.

## 377: You need a custom writing style for 200 business customers. How would you design it?

First check if a style guide in the prompt per customer is good enough. It's simpler and updates instantly.

If not, use one shared base model with a shared task adapter trained on all customers, plus per-customer adapters for customers with enough examples, served with multi-LoRA. Customers with little data get the shared adapter plus a style prompt. Automate training, eval and activation per customer, and give customers a way to give feedback that feeds the next training run.

## 378: You need to classify 1 million tickets per day cheaply. What would you build?

Start with a strong LLM to label a few thousand tickets, have people check a sample, and use that as training data. Fine-tune a small encoder classifier or a small LLM on it. At this volume, a fine-tuned encoder on a cheap GPU or even CPU is often the cheapest option.

Add a confidence threshold: low-confidence tickets go to a bigger LLM or a person. Track accuracy over time with a small audited sample, and retrain when categories or ticket content change.

## 379: How would you design an internal fine-tuning platform for a company?

Main parts:

- **Data layer:** versioned datasets with lineage, PII scanning and access control.
- **Training service:** job submission with configs (TRL, Axolotl or similar), queued on a GPU pool, with checkpoints in object storage.
- **Eval service:** standard task evals, general regression and safety suites, and reports per run.
- **Model registry:** versions, model cards, base model and data links, approval status.
- **Serving:** multi-LoRA inference servers with routing by model name, plus canary and rollback.
- **Monitoring:** quality, cost and drift dashboards feeding new data back.

Start with templates for the 2 or 3 most common use cases rather than a fully general system.

## 380: What does CI/CD for fine-tuned models look like?

A change to data, config or code triggers a pipeline: validate data, train (or fine-tune from the last version), run evals, compare to production, and generate a report. If the gates pass, the model is registered as a candidate.

Deployment is a separate, gated step: shadow, canary, then full rollout, with automatic rollback if live metrics drop. Every artifact (data version, config, code commit, model weights, eval results) is linked so you can trace any production output back to how the model was made.

## 381: How do you roll back a bad fine-tuned model quickly?

Keep the previous model version deployed or ready to load, and route traffic through a model name or alias you can switch (for example `extractor-prod` pointing to `extractor-v7`). With multi-LoRA serving, both adapters can stay loaded, and rollback is just a routing change.

Practice the rollback before you need it, and make sure downstream systems can handle outputs from either version.

## 382: Which metrics would you watch during a canary of a new fine-tuned model?

- Technical: error rate, latency (p50 and p95), timeouts, output validation failures.
- Quality: automatic checks on outputs, judge scores on sampled traffic, user ratings or corrections.
- Business: conversion, resolution rate, escalations, or whatever the feature drives.
- Cost per request.

Compare canary and control on the same time window, and define in advance what difference triggers a rollback.

## 383: What are the risks of training on your own model's feedback loop?

If you retrain only on outputs users accepted, you inherit selection bias. Users may accept mediocre answers, and cases the model handles badly may be underrepresented because users gave up. Over time the model can narrow and reinforce its own mistakes.

Mix in fresh human-labeled data, sample uniformly from traffic (not just accepted outputs), label failures on purpose, and keep a fixed eval set that isn't built from model outputs.

## 384: How do you detect drift after deploying a fine-tuned model?

Track input distributions (topics, lengths, languages, embedding clusters) and compare them with the training data over time. New clusters with no training coverage are a warning sign.

Also track output signals: validation failure rate, confidence, judge scores on samples, and user feedback. Set alerts on sustained changes, and periodically label a fresh sample to measure real accuracy.

## 385: How do you calculate the break-even point of fine-tuning versus using a hosted model?

Compare monthly totals:

- **Hosted:** requests per month x (input tokens x input price + output tokens x output price), with caching discounts.
- **Fine-tuned:** training runs per month x cost per run + serving cost (GPU hours, or the provider's price for the tuned model) + engineering and maintenance time.

Example: if the hosted option costs $0.004 per request and the fine-tuned small model costs $0.0005 per request plus $3,000 a month in fixed costs, break-even is at about 860,000 requests a month. Below that volume, the hosted model is cheaper.

## 386: How do you choose GPUs for fine-tuning?

- **Consumer cards (24 to 32 GB):** cheap, fine for QLoRA on small and mid-size models.
- **Mid-range data center cards (24 to 48 GB, like L4 or L40S):** good for LoRA and serving smaller models.
- **A100 / H100 / H200 / B200 class (80 GB and more):** for larger models, full fine-tuning, long contexts and multi-GPU jobs with fast interconnects.

Check memory first (does the job fit?), then bf16 and FP8 support, interconnect for multi-GPU, and availability and price. A more expensive GPU that finishes in a third of the time can be cheaper overall.

## 387: How do you use spot instances for training safely?

Spot or preemptible instances are much cheaper but can be taken away with little notice. Save checkpoints often to durable storage, handle the termination signal to save one last checkpoint, and make the job resume automatically from the latest checkpoint on a new instance.

Keep data in object storage, not on the local disk. Use spot for long training runs, and on-demand capacity for urgent jobs or ones with tight deadlines.

## 388: How do you tune serving throughput for a fine-tuned model?

- Use a server with continuous batching and paged KV cache (vLLM, SGLang).
- Turn on prefix caching, especially if requests share a long system prompt.
- Pick quantization that fits your GPU (FP8 or AWQ 4-bit) after checking quality.
- Set max sequence length and max batch size to match real traffic, not the model's maximum.
- Merge the adapter if you serve only one.
- Load test with realistic input and output lengths and measure tokens per second and latency percentiles.

## 389: How can fine-tuning help with speculative decoding?

Speculative decoding uses a small draft model to propose several tokens that the large model checks in one pass. It speeds up generation when the draft guesses well.

Fine-tuning the draft model on outputs of your fine-tuned large model raises the acceptance rate on your traffic, so you get more speedup. Some methods (like EAGLE-style draft heads) train small heads on top of the main model for the same purpose.

## 390: What makes tool-calling fine-tuning data really good?

- Cases where no tool should be called, so the model doesn't call tools for everything.
- Cases where it should ask the user for missing arguments instead of guessing.
- Multiple and parallel tool calls, and chained calls that use earlier results.
- Tool errors and how to recover or explain them.
- Exact argument formats (types, enums, date formats) that pass your validation.
- The same tool definitions and descriptions as in production.

Evaluate tool choice accuracy, argument correctness and end-to-end task success separately.

## 391: How do you fine-tune an agent on trajectories?

Collect full trajectories: the task, each model step (reasoning, tool calls), tool results, and the final outcome. Keep successful ones (verified by tests or outcome checks), or rank trajectories and use preference training.

Train with loss on the model's own steps only, not on tool outputs. Watch for very long sequences, and make sure the tool set and formats match the agent's runtime. RL with outcome rewards in a sandboxed environment is the next step after SFT.

## 392: Why should tool results be masked from the loss?

Tool results come from the outside world, not from the model. If you train on them, the model learns to predict or invent tool outputs, which encourages hallucinating results instead of calling the tool.

Mask tool messages (and user messages) so only assistant turns are trained. Check the rendered and masked tokens of a multi-turn tool example before training.

## 393: How do you handle loss masking in multi-turn conversations?

Options are training on all assistant turns or only the last one. Training on all turns uses the data better, but earlier turns may be weaker or written differently. Training only on the last turn treats earlier ones as context.

Choose based on data quality. If earlier assistant turns are good, train on all of them. If they come from an older model or contain mistakes, mask them. Make sure the masking uses the template's real assistant boundaries, not string search.

## 394: What should you keep in mind when fine-tuning reasoning models?

- Keep the model's thinking format and special tags in training data, or you can break its reasoning mode.
- Thinking traces make examples very long, which raises memory and cost.
- If you only have final answers, consider RL with verifiable rewards rather than SFT without thinking.
- Control reasoning length: very long traces cost latency, very short ones hurt accuracy. Length-aware rewards or curated traces help.
- Check both thinking and non-thinking modes if the model supports both.

## 395: How do you combine continued pretraining and SFT?

Run continued pretraining on domain text first, mixed with some general text (for example 10% to 30%) to reduce forgetting. Use a lower learning rate than SFT and enough tokens for the domain to matter.

Then run SFT on instruction data for your tasks, ideally starting from the continued-pretrained base, or merging a CPT adapter with an instruct model in some setups. Evaluate after each stage: domain knowledge probes after CPT, task and general evals after SFT.

## 396: How do you pick data mixing ratios?

There's no fixed rule. Start with the task data as the majority and add general data at 10% to 30%. Then compare a few ratios on both the task eval and the general eval, and pick the best trade-off.

For multiple tasks, sample by importance and difficulty rather than raw dataset size, so a huge easy dataset doesn't drown a small important one. Temperature-based sampling (raising task sizes to a power below 1) is one common way to balance.

## 397: What is a warmup-stable-decay (WSD) schedule?

WSD warms up the learning rate, keeps it constant for most of training, then decays it quickly at the end. Unlike cosine, you don't need to know the total training length upfront, and you can branch off a decay phase from any point in the stable phase.

It's popular in pretraining and continued pretraining, because you can extend training or try different final data mixes in the decay phase without starting over.

## 398: How do you choose LoRA rank empirically, and what happens if it's too high?

Run the same setup with ranks like 8, 16, 32 and 64 and compare task eval scores and general regression. Often scores flatten after a certain rank. Pick the smallest rank at the flat part.

Too high a rank with standard scaling may not help, because the effective update shrinks. With small datasets it can overfit more and forget more, and it costs more memory and a bigger adapter. If you go high, consider rsLoRA scaling.

## 399: When should you train embedding and output layers with LoRA?

When you add new tokens, or when the domain uses token patterns the model rarely saw (special formats, a new language), training only the inner layers may not be enough. Then include `embed_tokens` and `lm_head` with `modules_to_save` (full copies) or with LoRA on those layers if supported.

This greatly increases adapter size, because these layers are large. Use it only when you've seen that it helps.

## 400: What alternatives to LoRA exist for partial training?

- **Layer freezing:** fully train only the top few layers and freeze the rest.
- **Prefix tuning and prompt tuning:** learn virtual tokens added to the input. Very small, but usually weaker than LoRA on modern LLMs.
- **IA3:** learns scaling vectors for activations. Tiny adapters, decent for some tasks.
- **Adapter layers:** small bottleneck layers inserted between existing layers. They add inference latency.
- **Full fine-tuning with memory tricks:** GaLore-style gradient projection, 8-bit optimizers and sharding.

LoRA and its variants remain the default because of their balance of quality, memory and tooling support.

## 401: How do prompt tuning and prefix tuning compare with LoRA?

Prompt tuning learns a few embedding vectors prepended to the input. Prefix tuning learns key and value vectors added at every layer. Both keep all model weights frozen and produce tiny artifacts.

They work well on very large models for some tasks, but on mid-size models they usually lag behind LoRA, take up context length, and can be harder to train. Today they're mostly used in research or when you need extremely small per-task artifacts.

## 402: Can you fine-tune across organizations without sharing data?

Federated fine-tuning trains on each party's data locally and shares only updates (for example LoRA adapter updates), which are combined centrally. LoRA makes this practical because the updates are small.

It's complex: updates can still leak information unless combined with secure aggregation or differential privacy, data differs between parties, and coordination is hard. It's used in some healthcare and finance settings but is rare in typical web products.

## 403: What is machine unlearning, and can you rely on it?

Unlearning tries to remove the influence of specific data or knowledge from a trained model without retraining from scratch, for example by training against the content to forget or by editing specific weights.

Current methods can reduce how often the model outputs the content, but they often don't fully remove it (it can be recovered with other prompts), and they may damage other abilities. For legal deletion needs, retraining without the data is still the most reliable approach.

## 404: How can you see what fine-tuning changed in a model?

- Compare outputs of base and fine-tuned models on the same prompts, focusing on where they disagree.
- Look at which layers have the largest weight changes (or LoRA update norms).
- Compare token probabilities for key tokens before and after.
- Use interpretability tools (probing, activation comparisons) for deeper research.

For most teams, structured output comparisons and error analysis give the most practical insight.

## 405: How does activation steering compare with fine-tuning?

Activation steering adds a direction vector to the model's hidden states at inference to push behavior (more formal, less verbose, a certain topic). It needs no training run, just a few examples to compute the vector, and can be turned up or down per request.

It's cheaper and more flexible but less precise and less robust than fine-tuning, and supported mainly in research tools and a few serving setups. Fine-tuning is still the reliable way to teach real task skills.

## 406: How do you test robustness of a fine-tuned model?

- Paraphrase eval inputs and check that answers stay consistent.
- Add noise: typos, extra whitespace, different casing, mixed languages.
- Change formatting of inputs (HTML vs plain text, different date formats).
- Adversarial inputs: prompt injection, conflicting instructions, very long inputs.
- Out-of-scope requests.

Narrowly fine-tuned models often overfit to the exact input style in training. Robustness tests show this before users do.

## 407: How do you measure hallucinations after fine-tuning?

For grounded tasks (RAG, extraction), check whether every claim or value in the output is supported by the input. Use rules for structured fields and a judge or entailment model for text. For closed-book questions, use a set with known answers plus questions the model can't know, and measure both wrong answers and appropriate "I don't know" replies.

Compare base and fine-tuned models on the same set. Fine-tuning can quietly raise hallucinations even when the main task score improves.

## 408: What does an instruction-following regression look like, and how do you test it?

After narrow fine-tuning, the model may ignore constraints it used to follow: word limits, "answer in bullet points", "don't mention X", or language requirements. It defaults to the format it was trained on.

Test with a set of prompts that have checkable constraints (public sets like IFEval work, plus your own), and score with code. If scores drop, add varied instruction examples to the training mix.

## 409: How do you fine-tune embedding models with hard negatives?

In-batch negatives are often too easy. Hard negatives are documents that look relevant but aren't the right answer. Mine them by retrieving top results with the current model and removing the true positives, then train with triplets (query, positive, hard negative) using a contrastive loss.

Be careful: some "hard negatives" are actually unlabeled positives, which teaches the model the wrong thing. Filter with a cross-encoder or judge, and use larger batch sizes (or cached losses) so the model also sees many in-batch negatives.

## 410: How do you fine-tune a reranker?

A reranker (cross-encoder) reads the query and a document together and outputs a relevance score. Train it on query-document pairs labeled relevant or not, with hard negatives from your retriever, using binary or listwise losses. `sentence-transformers` supports training cross-encoders.

Evaluate with ranking metrics (NDCG, MRR, recall at k) on real queries, and measure the latency cost, because rerankers run on every candidate document.

## 411: How does tokenization affect fine-tuning for code or non-English text?

If the tokenizer splits your content into many small tokens (for example rare languages, special notation or unusual code), sequences get long, training is more expensive, and the model has a harder time learning patterns.

Check the tokens-per-word ratio on your data. Prefer base models whose tokenizer handles your content efficiently. Extending the tokenizer is possible but needs a lot of training to make the new tokens useful.

## 412: What problems come with multilingual fine-tuning, and how do you address them?

- Low-resource languages are underrepresented and get worse while English gets better.
- The model may switch languages in answers.
- Machine-translated data carries translation errors and unnatural phrasing.
- Cultural and formatting differences (dates, names, politeness) get ignored.

Address them by sampling languages with balancing (upsample low-resource ones), using native-written data where possible, evaluating per language, and including explicit examples of answering in the user's language.

## 413: What's different about fine-tuning vision-language models in depth?

Images become many tokens through the vision encoder and a projector. Fine-tuning choices include freezing the vision encoder (common), training the projector, and adding LoRA to the language model.

Image resolution settings control token count and memory. Data needs consistent image preprocessing between training and inference. Evals should include visual edge cases like low quality scans, rotated images and small text. Also check that text-only quality doesn't drop if the model is used for both.

## 414: What constraints apply when fine-tuning for on-device use?

Model size (memory and download), latency on weak hardware, and battery use limit you to small models, heavily quantized. The fine-tuned behavior must survive 4-bit or lower quantization, so evaluate the final quantized model on device, or use quantization-aware training.

Also plan updates: shipping a new adapter is much smaller than shipping a new model, if the on-device runtime supports adapters.

## 415: How would you design a synthetic data pipeline at scale?

1. **Seeds:** real examples and a taxonomy of topics, difficulty and edge cases.
2. **Generation:** prompt one or more strong models with varied seeds, personas and constraints.
3. **Validation:** schema checks, verifiers (run code, check math), and judge scoring with rubrics.
4. **Diversity control:** dedupe, cluster and rebalance so no cluster dominates.
5. **Human review:** sample from each cluster, and feed failures back into prompts.
6. **Lineage:** record which generator, prompt and version produced each example.

Track the share of synthetic vs real data in every training set.

## 416: What is rejection sampling fine-tuning?

For each prompt, generate several answers from the current model (or a stronger one), score them with a verifier or reward model, keep only the best or correct ones, and run SFT on those. Repeat with the improved model.

It's a simple, stable alternative to full RL. It works well when you have a reliable scorer and the model already solves some prompts. Its weakness is that it learns only from successes, not from the difference between good and bad answers.

## 417: How do self-improvement loops like STaR work?

The model tries to solve problems with reasoning. Solutions that reach the correct answer are kept and used for fine-tuning. For problems it failed, it can be given the answer as a hint to produce a reasoning path ("rationalization"), which is also kept if it's consistent. Then the process repeats with the improved model.

It needs problems with checkable answers. Risks include learning lucky wrong reasoning that reaches the right answer, and narrowing the model's style over iterations.

## 418: What is RLAIF or AI feedback?

RLAIF replaces human preference labels with labels from a model, often guided by a written set of principles (a "constitution"). A judge model compares answers or critiques and revises them, and that feedback trains the model with DPO or RL.

It scales much more cheaply than human labeling. The quality depends on the judge and the principles. Validate against human judgments on a sample, and watch for the judge's biases being copied into your model.

## 419: How do you write good annotation guidelines and measure label quality?

Guidelines should define each label or output rule clearly, with positive and negative examples and rules for edge cases and ties. Run a pilot, find where annotators disagree, and update the guidelines.

Measure inter-annotator agreement (for example Cohen's kappa) on a shared sample. Low agreement means the task or guidelines are unclear, and the model can't be expected to beat that ceiling. Audit a sample of labels regularly.

## 420: How does label noise affect fine-tuning, and how do you handle it?

Noisy labels teach the model wrong answers and cap its accuracy. Large models can also memorize noise, especially over many epochs. Noise that follows patterns (one annotator always wrong on a case) is worse than random noise.

Handle it by finding suspicious labels: train a model, then review examples where the model confidently disagrees with the label. Use agreement between multiple annotators, train fewer epochs, and fix the guidelines that cause systematic errors.

## 421: How do you handle severe class imbalance in LLM classification fine-tuning?

- Upsample rare classes or downsample frequent ones in training, but keep the eval at the real distribution.
- For classification heads, use class weights in the loss.
- Tune decision thresholds per class on validation data.
- Measure per-class recall and precision, and macro-F1, not just accuracy.
- Collect more real examples of rare classes through targeted search or active learning.

If one rare class is critical, consider a separate binary detector for it.

## 422: Which hyperparameters matter most in LLM fine-tuning?

In practice, roughly in this order:

1. Learning rate (and the LoRA alpha-to-rank ratio, which scales it).
2. Number of epochs or training steps.
3. Data quality and mix (not a hyperparameter, but it matters more than any of them).
4. Effective batch size.
5. LoRA rank and target modules.
6. Scheduler and warmup.

Spend tuning effort in that order, and keep the rest at sensible defaults.

## 423: How does performance scale with fine-tuning data size?

For many tasks, quality improves roughly with the logarithm of data size: each doubling gives a similar, smaller gain, until it flattens. Bigger base models usually need fewer examples to reach the same quality.

Studies on fine-tuning scaling suggest the base model size often matters more than the PEFT method, and data quality changes the whole curve. Use your own learning curve to decide whether to buy more data or a bigger model.

## 424: How do you detect overfitting beyond validation loss?

- Check whether outputs copy training answers word for word for similar inputs (n-gram overlap with the training set).
- Compare scores on validation inputs similar to training vs clearly different ones.
- Test robustness with paraphrases. Overfit models are brittle.
- Look at the diversity of outputs: overfit models often reuse the same phrases.
- Watch general regression evals, which drop as the model specializes too much.

## 425: What are checkpoint averaging and EMA, and do they help?

Checkpoint averaging takes the average of weights from several checkpoints near the end of training. EMA (exponential moving average) keeps a running average of weights during training. Both smooth out noise from the last few updates.

They often give a small, free improvement and better stability, especially with noisy training like small batches or RL. With LoRA you can average adapters from several checkpoints. Always confirm on your eval.

## 426: Why aren't GPU training runs fully deterministic?

Many GPU operations (some reductions, atomic additions, certain attention kernels) don't add numbers in a fixed order, and floating-point addition gives slightly different results in different orders. Multi-GPU communication adds more variation. Small differences grow over many steps.

You can force deterministic algorithms in PyTorch at a speed cost, but most teams accept small variation and instead run important comparisons with 2 or 3 seeds.

## 427: How do you debug a distributed training job that hangs?

Common causes: one rank crashed or ran out of memory while others wait, ranks take different code paths (for example a conditional skip on one GPU), mismatched tensor shapes in collective operations, or network and NCCL configuration problems.

Steps: check logs from every rank, not just rank 0. Set `NCCL_DEBUG=INFO` and PyTorch distributed debug settings. Use timeouts so hangs turn into errors. Reproduce on fewer GPUs. Make sure every rank sees the same number of batches.

## 428: How do you handle very large fine-tuning datasets?

Store data in efficient formats like Parquet in object storage, and stream it (`load_dataset(..., streaming=True)`) instead of loading it all into memory. Pre-tokenize and pack ahead of time, so training GPUs don't wait on CPU work.

Shard the data across workers and ranks, keep a deterministic shuffle so you can resume correctly, and log exactly which data shards each run used.

## 429: What can go wrong when converting a fine-tuned model to GGUF?

- The chat template in the GGUF metadata doesn't match the one used in training, so prompts are formatted wrong.
- Special tokens or added tokens aren't carried over correctly.
- The converter doesn't support the architecture or a new feature of it yet.
- Low-bit quantization damages the fine-tuned behavior more than expected.
- RoPE or context-length settings are lost.

After conversion, run the same eval through the GGUF runtime and compare with the original model.

## 430: How do you set the prompt template for a fine-tuned model in Ollama?

If the GGUF doesn't carry the right chat template, define it in the `Modelfile` with `TEMPLATE` (written in Go template syntax) and set stop tokens with `PARAMETER stop`:

```
FROM ./my-model.gguf
TEMPLATE """{{ if .System }}<|im_start|>system
{{ .System }}<|im_end|>
{{ end }}<|im_start|>user
{{ .Prompt }}<|im_end|>
<|im_start|>assistant
"""
PARAMETER stop "<|im_end|>"
```

The template must produce exactly what your training data looked like for that model family.

## 431: How do you expose a self-hosted fine-tuned model safely to your web app?

Put the inference server behind an internal network or API gateway, not directly on the internet. Add authentication (API keys or service identity), rate limits per client, request size limits and timeouts.

Have your backend call the model, never the browser directly. Log requests with privacy controls, validate outputs before using them, and add a fallback path when the model server is down or slow.

## 432: How would you design fallbacks for a fine-tuned model?

- **On error or timeout:** retry once, then fall back to a hosted general model with a longer prompt.
- **On invalid output:** retry with constrained decoding or an error hint, then fall back.
- **On low confidence:** route to a larger model or a human queue.
- **On server overload:** shed load to the fallback model instead of failing requests.

Track how often fallbacks happen. A rising fallback rate is an early sign that the fine-tuned model needs retraining.

## 433: How do model cascades with fine-tuned models work?

A cascade sends each request to a cheap fine-tuned model first and escalates only some to a larger model, based on a confidence score, a verifier check or a learned router. Most requests stay cheap, and hard ones still get high quality.

The key work is the escalation rule. Calibrate it on labeled data so you know the quality and cost at each threshold, and monitor the escalation rate in production.

## 434: How have the economics of fine-tuning changed by 2026?

Frontier models follow long instructions much better, context windows are large, and prompt caching makes long prompts cheap. Many use cases that needed fine-tuning a few years ago now work with prompting and RAG. At the same time, open-weight models got much stronger, and LoRA tooling and multi-LoRA serving made fine-tuning cheap to run.

So the trend is: fewer teams fine-tune hosted frontier models, and more fine-tune small open models for high-volume, narrow tasks, privacy, or on-device use.

## 435: Why have some providers reduced their fine-tuning offerings?

Providers haven't always explained it in detail, but common reasons people point to include: new base models come out so fast that fine-tunes on old models become outdated quickly, each fine-tuned model is costly to host and keep compatible, strong prompting plus caching covers many use cases, and safety review of customer fine-tunes is hard.

The practical lesson for engineers: hosted fine-tuning can disappear. If your product depends on a fine-tuned model, keep your data and pipeline portable to open-weight models.

## 436: How do you avoid vendor lock-in with fine-tuned models?

- Own your training data, eval sets and data pipeline, in provider-neutral formats like messages JSONL.
- Keep prompt building and output parsing behind your own interface.
- Prefer open-weight bases whose weights you can download, or keep a tested open-weight alternative.
- Serve through OpenAI-compatible APIs so switching backends is a config change.
- Rerun your evals on alternatives regularly, so you know your options before you're forced to move.

## 437: What should a model card for an internal fine-tuned model contain?

- Purpose and intended use, plus uses it's not suitable for.
- Base model name, revision and license.
- Training data sources, versions, size and preprocessing (including PII handling).
- Method and key hyperparameters.
- Eval results on task, general and safety suites, with dates.
- Known limitations and failure modes.
- Owner, version history and how to report issues.

## 438: What regulatory issues might apply to fine-tuned models?

Rules depend on where you operate and the use case. For example, the EU AI Act puts obligations on providers of general-purpose AI models, and substantially modifying a model through fine-tuning can, in some cases, make you a provider with your own obligations. Rules for high-risk uses (hiring, credit, health) also apply to fine-tuned models used there.

Privacy laws (like GDPR) apply to personal data in training. Involve legal and compliance early, keep documentation of data and training, and follow current guidance, since this area is still changing.

## 439: How do you red-team a fine-tuned model?

Define what harm looks like for your product (data leaks, unsafe advice, policy violations, brand damage, tool misuse). Test with a mix of public attack prompts, prompts written by your team, and automated attack generation with another model.

Focus on how fine-tuning changed things: compare base and fine-tuned models on the same attacks, test training-data extraction, and try known jailbreak patterns. Turn the findings into regression tests and, where needed, training data.

## 440: How do you check a fine-tuned model for unfair behavior?

Build eval slices that vary only a sensitive attribute (for example names suggesting different genders or origins, or different dialects) while keeping the task the same, and compare outputs and scores. Check approval decisions, tone, refusal rates and quality across groups.

If differences show up, look at the training data for the same pattern, rebalance or relabel, and add fairness checks to the release gates.

## 441: Who should own what in a fine-tuning project team?

- **Product owner:** defines the task, success metrics and acceptable risks.
- **Domain experts:** write guidelines, label and review data, and judge outputs.
- **ML or AI engineer:** data pipeline, training, evaluation and model choice.
- **Platform or backend engineer:** serving, routing, monitoring and fallbacks.
- **Security, privacy and legal:** data use, licensing and safety review.

On small teams one person holds several roles, but each responsibility needs a clear owner.

## 442: How would you design an experiment to prove fine-tuning beats prompting?

Fix the eval set before any work and keep it hidden from both approaches. Give the prompting approach a fair effort (good instructions, examples, a strong model, structured output). Train the fine-tuned model with a reasonable search. Compare on quality, cost per request and latency, with confidence intervals.

Then confirm online with an A/B test on real traffic. Report honestly, including cases where prompting won.

## 443: What ablations would you run on a fine-tuning setup?

Change one thing at a time from your best setup and measure the effect:

- Remove synthetic data, or only use synthetic data.
- Remove general data from the mix.
- Train on all tokens vs assistant-only.
- Lower or raise LoRA rank, or limit target modules.
- Base vs instruct starting model.
- Fewer or more epochs.

Ablations show which parts actually matter, so you keep the pipeline simple and know what to focus on next.

## 444: How would you describe a fine-tuning project in an interview?

Use a clear structure: the problem and why prompting wasn't enough, the data (where it came from, size, how you cleaned it), the method and why you chose it, how you evaluated it (metrics, baseline, slices), results with numbers (quality, cost, latency), problems you hit and how you fixed them, and what happened in production.

Interviewers care most about your decisions and trade-offs, how you measured success, and what you'd do differently.

## 445: How do you future-proof a fine-tuning pipeline?

Keep everything as code and config: data processing, training, eval and deployment. Store data in neutral formats, version everything, and make the base model a parameter. Then moving to a new base model is mostly "change one line and rerun".

Also keep a prompt-only baseline in the eval. Every time a new base model comes out, check whether you still need fine-tuning at all.

## 446: When should you stop investing in fine-tuning for a use case?

Stop or pause when a prompted model reaches the same quality at acceptable cost, when gains per iteration become tiny compared to the effort, when maintenance (retraining, base model upgrades) costs more than it saves, or when the task changes so often that the training data is always outdated.

It's a normal engineering trade-off. Be ready to drop a fine-tuned model when the simpler option catches up.

## 447: What are common anti-patterns in fine-tuning projects?

- Fine-tuning to add knowledge that belongs in RAG.
- Skipping the baseline and the eval set.
- Tuning hyperparameters for days instead of fixing data.
- Trusting loss curves without reading outputs.
- Different prompt formats in training and production.
- No plan for retraining, monitoring or base model shutdowns.
- Training on unreviewed synthetic data from a single prompt.
- Ignoring licenses, privacy and safety until launch.

## 448: What is your checklist before shipping a fine-tuned model?

- Beats the baseline on the task eval, with per-slice results.
- General, safety and robustness evals have no major regressions.
- Tested in the exact production format, quantization and server.
- Latency and cost measured at expected load.
- Model card written, data lineage and license recorded.
- Monitoring, alerts, fallback and rollback ready.
- Shadow or canary plan with clear success and rollback criteria.
- Owner assigned for retraining and incidents.

## 449: How would you explain why a fine-tuned model is not the same as a "trained-on-our-data" chatbot?

Many people expect fine-tuning to make a model "know everything in our documents". In reality fine-tuning mostly teaches behavior and patterns. It doesn't reliably store or update facts, and it can't cite where an answer came from.

A bot that knows your data is usually built with RAG (search your documents and give them to the model), possibly with a fine-tuned model that's better at using those documents. Explaining this early prevents wrong expectations and wasted training runs.

## 450: How has fine-tuning practice changed in the last few years?

- LoRA and QLoRA made fine-tuning possible on one GPU, and they're now the default.
- Preference methods moved from complex PPO RLHF to simpler DPO-style training.
- RL with verifiable rewards (GRPO and similar) became the main way to improve reasoning and agent skills.
- Tooling matured: TRL 1.x, PEFT, Unsloth, Axolotl, and multi-LoRA serving in vLLM.
- Open-weight models got strong enough that most hands-on fine-tuning happens on them.
- Hosted fine-tuning shrank: OpenAI is closing its platform, and the Claude API doesn't offer it, while strong prompting, caching and RAG cover more use cases.

The core skills stay the same: clean data, honest evals and knowing when not to fine-tune.
