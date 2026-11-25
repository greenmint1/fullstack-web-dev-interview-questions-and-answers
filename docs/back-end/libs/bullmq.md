# BullMQ Interview Questions and Answers

_Last updated: November 25, 2026_

This file has 450 BullMQ interview questions and answers: 150 easy, 150 moderate and 150 advanced. The answers target BullMQ 6 for Node.js (6.7 at the time of writing), with notes where older v5 code still looks different. Code examples use JavaScript and Node.js.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is BullMQ?](#1-what-is-bullmq)
- [2: What problems does BullMQ solve?](#2-what-problems-does-bullmq-solve)
- [3: How do you install BullMQ?](#3-how-do-you-install-bullmq)
- [4: What are the main classes in BullMQ?](#4-what-are-the-main-classes-in-bullmq)
- [5: How do you create a queue and add a job?](#5-how-do-you-create-a-queue-and-add-a-job)
- [6: How do you create a worker?](#6-how-do-you-create-a-worker)
- [7: What is a job in BullMQ?](#7-what-is-a-job-in-bullmq)
- [8: What is the difference between a queue and a worker?](#8-what-is-the-difference-between-a-queue-and-a-worker)
- [9: Why does BullMQ need Redis?](#9-why-does-bullmq-need-redis)
- [10: Can BullMQ work without Redis?](#10-can-bullmq-work-without-redis)
- [11: What is a producer in BullMQ?](#11-what-is-a-producer-in-bullmq)
- [12: What is a consumer in BullMQ?](#12-what-is-a-consumer-in-bullmq)
- [13: What is a processor function?](#13-what-is-a-processor-function)
- [14: What are the possible states of a job?](#14-what-are-the-possible-states-of-a-job)
- [15: What happens when a processor throws an error?](#15-what-happens-when-a-processor-throws-an-error)
- [16: What does the job name mean?](#16-what-does-the-job-name-mean)
- [17: How do you pass data to a job?](#17-how-do-you-pass-data-to-a-job)
- [18: How do you get the result of a job?](#18-how-do-you-get-the-result-of-a-job)
- [19: How do you delay a job?](#19-how-do-you-delay-a-job)
- [20: How do you retry failed jobs automatically?](#20-how-do-you-retry-failed-jobs-automatically)
- [21: What is backoff in BullMQ?](#21-what-is-backoff-in-bullmq)
- [22: How does exponential backoff calculate the delay?](#22-how-does-exponential-backoff-calculate-the-delay)
- [23: How do you set a job priority?](#23-how-do-you-set-a-job-priority)
- [24: What is the maximum priority value?](#24-what-is-the-maximum-priority-value)
- [25: What does the lifo option do?](#25-what-does-the-lifo-option-do)
- [26: How do you give a job a custom ID?](#26-how-do-you-give-a-job-a-custom-id)
- [27: How are job IDs created by default?](#27-how-are-job-ids-created-by-default)
- [28: How do you add several jobs at once?](#28-how-do-you-add-several-jobs-at-once)
- [29: How do you get a job by its ID?](#29-how-do-you-get-a-job-by-its-id)
- [30: How do you check the state of a job?](#30-how-do-you-check-the-state-of-a-job)
- [31: How do you report progress from a job?](#31-how-do-you-report-progress-from-a-job)
- [32: How do you add logs to a job?](#32-how-do-you-add-logs-to-a-job)
- [33: What is the default worker concurrency?](#33-what-is-the-default-worker-concurrency)
- [34: What does concurrency mean for a worker?](#34-what-does-concurrency-mean-for-a-worker)
- [35: Can several workers process the same queue?](#35-can-several-workers-process-the-same-queue)
- [36: What happens to a job after it completes?](#36-what-happens-to-a-job-after-it-completes)
- [37: What do removeOnComplete and removeOnFail do?](#37-what-do-removeoncomplete-and-removeonfail-do)
- [38: How do you set default options for all jobs in a queue?](#38-how-do-you-set-default-options-for-all-jobs-in-a-queue)
- [39: What is QueueEvents?](#39-what-is-queueevents)
- [40: What events does a Worker emit?](#40-what-events-does-a-worker-emit)
- [41: What is the difference between Worker events and QueueEvents?](#41-what-is-the-difference-between-worker-events-and-queueevents)
- [42: Why should you listen to the worker error event?](#42-why-should-you-listen-to-the-worker-error-event)
- [43: How do you pause a queue?](#43-how-do-you-pause-a-queue)
- [44: How do you pause a single worker?](#44-how-do-you-pause-a-single-worker)
- [45: How do you close a worker?](#45-how-do-you-close-a-worker)
- [46: How do you close a queue?](#46-how-do-you-close-a-queue)
- [47: How do you count jobs in a queue?](#47-how-do-you-count-jobs-in-a-queue)
- [48: How do you list jobs in a certain state?](#48-how-do-you-list-jobs-in-a-certain-state)
- [49: How do you remove a job?](#49-how-do-you-remove-a-job)
- [50: How do you retry a failed job manually?](#50-how-do-you-retry-a-failed-job-manually)
- [51: How do you empty a queue?](#51-how-do-you-empty-a-queue)
- [52: What does queue.clean do?](#52-what-does-queueclean-do)
- [53: What does queue.obliterate do?](#53-what-does-queueobliterate-do)
- [54: What is the difference between drain, clean and obliterate?](#54-what-is-the-difference-between-drain-clean-and-obliterate)
- [55: What is a delayed job?](#55-what-is-a-delayed-job)
- [56: How do you run a job right away if it is delayed?](#56-how-do-you-run-a-job-right-away-if-it-is-delayed)
- [57: How do you change the delay of a job that is already delayed?](#57-how-do-you-change-the-delay-of-a-job-that-is-already-delayed)
- [58: What is a job scheduler?](#58-what-is-a-job-scheduler)
- [59: What is the difference between every and pattern in a job scheduler?](#59-what-is-the-difference-between-every-and-pattern-in-a-job-scheduler)
- [60: Why is it called upsertJobScheduler?](#60-why-is-it-called-upsertjobscheduler)
- [61: How do you remove a job scheduler?](#61-how-do-you-remove-a-job-scheduler)
- [62: How do you list job schedulers?](#62-how-do-you-list-job-schedulers)
- [63: What were repeatable jobs?](#63-what-were-repeatable-jobs)
- [64: How do you set a timezone for a cron scheduler?](#64-how-do-you-set-a-timezone-for-a-cron-scheduler)
- [65: What is a flow in BullMQ?](#65-what-is-a-flow-in-bullmq)
- [66: How do you create a flow?](#66-how-do-you-create-a-flow)
- [67: How does a parent job read the results of its children?](#67-how-does-a-parent-job-read-the-results-of-its-children)
- [68: What is the waiting-children state?](#68-what-is-the-waiting-children-state)
- [69: What is a sandboxed processor?](#69-what-is-a-sandboxed-processor)
- [70: What does a sandboxed processor file look like?](#70-what-does-a-sandboxed-processor-file-look-like)
- [71: What does useWorkerThreads do?](#71-what-does-useworkerthreads-do)
- [72: What is a stalled job?](#72-what-is-a-stalled-job)
- [73: What is a job lock?](#73-what-is-a-job-lock)
- [74: What is lockDuration?](#74-what-is-lockduration)
- [75: What is maxStalledCount?](#75-what-is-maxstalledcount)
- [76: What is rate limiting in BullMQ?](#76-what-is-rate-limiting-in-bullmq)
- [77: Is the worker limiter per worker or for the whole queue?](#77-is-the-worker-limiter-per-worker-or-for-the-whole-queue)
- [78: What is the default prefix for Redis keys?](#78-what-is-the-default-prefix-for-redis-keys)
- [79: How do you connect to Redis with a password or TLS?](#79-how-do-you-connect-to-redis-with-a-password-or-tls)
- [80: Can you reuse an ioredis instance?](#80-can-you-reuse-an-ioredis-instance)
- [81: Why does a worker need maxRetriesPerRequest set to null?](#81-why-does-a-worker-need-maxretriesperrequest-set-to-null)
- [82: Does a worker use one Redis connection?](#82-does-a-worker-use-one-redis-connection)
- [83: What is the maxmemory-policy setting and why does it matter?](#83-what-is-the-maxmemory-policy-setting-and-why-does-it-matter)
- [84: What is BullMQ Pro?](#84-what-is-bullmq-pro)
- [85: What is the difference between Bull and BullMQ?](#85-what-is-the-difference-between-bull-and-bullmq)
- [86: Is BullMQ written in TypeScript?](#86-is-bullmq-written-in-typescript)
- [87: Can BullMQ be used from other languages?](#87-can-bullmq-be-used-from-other-languages)
- [88: What is the attemptsMade property?](#88-what-is-the-attemptsmade-property)
- [89: What info does a job keep about time?](#89-what-info-does-a-job-keep-about-time)
- [90: How do you update a job's data while it is waiting?](#90-how-do-you-update-a-jobs-data-while-it-is-waiting)
- [91: What does job.failedReason contain?](#91-what-does-jobfailedreason-contain)
- [92: What does the drained event mean?](#92-what-does-the-drained-event-mean)
- [93: What is the completed event payload in QueueEvents?](#93-what-is-the-completed-event-payload-in-queueevents)
- [94: How do you wait for a job to finish from the producer?](#94-how-do-you-wait-for-a-job-to-finish-from-the-producer)
- [95: Should an HTTP request wait for a job to finish?](#95-should-an-http-request-wait-for-a-job-to-finish)
- [96: What is the autorun option on a worker?](#96-what-is-the-autorun-option-on-a-worker)
- [97: What is the difference between job.remove and queue.drain?](#97-what-is-the-difference-between-jobremove-and-queuedrain)
- [98: What happens to jobs if Redis restarts?](#98-what-happens-to-jobs-if-redis-restarts)
- [99: What is a dashboard for BullMQ?](#99-what-is-a-dashboard-for-bullmq)
- [100: How do you add Bull Board to an Express app?](#100-how-do-you-add-bull-board-to-an-express-app)
- [101: What kind of tasks fit well in a BullMQ queue?](#101-what-kind-of-tasks-fit-well-in-a-bullmq-queue)
- [102: What kind of tasks don't fit well in a queue?](#102-what-kind-of-tasks-dont-fit-well-in-a-queue)
- [103: Is job data stored as JSON?](#103-is-job-data-stored-as-json)
- [104: Can you put a Buffer or file into job data?](#104-can-you-put-a-buffer-or-file-into-job-data)
- [105: How does a worker know which queue to listen to?](#105-how-does-a-worker-know-which-queue-to-listen-to)
- [106: Do you need to create a Queue instance before a Worker can process jobs?](#106-do-you-need-to-create-a-queue-instance-before-a-worker-can-process-jobs)
- [107: What was QueueScheduler?](#107-what-was-queuescheduler)
- [108: How do you run a worker as a separate process?](#108-how-do-you-run-a-worker-as-a-separate-process)
- [109: How do you shut down a worker cleanly?](#109-how-do-you-shut-down-a-worker-cleanly)
- [110: What is the job progress value type?](#110-what-is-the-job-progress-value-type)
- [111: How do you see the latest progress of a job from another process?](#111-how-do-you-see-the-latest-progress-of-a-job-from-another-process)
- [112: What is the difference between job.data and job.opts?](#112-what-is-the-difference-between-jobdata-and-jobopts)
- [113: How do you skip retries for a specific error?](#113-how-do-you-skip-retries-for-a-specific-error)
- [114: What replaced job.discard?](#114-what-replaced-jobdiscard)
- [115: What does the active event mean?](#115-what-does-the-active-event-mean)
- [116: What does the waiting event in QueueEvents tell you?](#116-what-does-the-waiting-event-in-queueevents-tell-you)
- [117: Can a job belong to two queues?](#117-can-a-job-belong-to-two-queues)
- [118: Can you change a job's priority after it was added?](#118-can-you-change-a-jobs-priority-after-it-was-added)
- [119: How do you know how many workers are connected to a queue?](#119-how-do-you-know-how-many-workers-are-connected-to-a-queue)
- [120: What does the worker name option do?](#120-what-does-the-worker-name-option-do)
- [121: Can you add jobs to a paused queue?](#121-can-you-add-jobs-to-a-paused-queue)
- [122: What is the deduplication option?](#122-what-is-the-deduplication-option)
- [123: What is the difference between jobId and deduplication?](#123-what-is-the-difference-between-jobid-and-deduplication)
- [124: What does the deduplication ttl do?](#124-what-does-the-deduplication-ttl-do)
- [125: Where are failed jobs kept?](#125-where-are-failed-jobs-kept)
- [126: Can a job be processed twice?](#126-can-a-job-be-processed-twice)
- [127: What does idempotent mean for a job?](#127-what-does-idempotent-mean-for-a-job)
- [128: How do you test a BullMQ worker locally?](#128-how-do-you-test-a-bullmq-worker-locally)
- [129: How do you unit test a processor without Redis?](#129-how-do-you-unit-test-a-processor-without-redis)
- [130: What is a job's returnvalue used for?](#130-what-is-a-jobs-returnvalue-used-for)
- [131: What happens if the processor returns undefined?](#131-what-happens-if-the-processor-returns-undefined)
- [132: Can you use BullMQ with NestJS?](#132-can-you-use-bullmq-with-nestjs)
- [133: How do you add a job from a NestJS service?](#133-how-do-you-add-a-job-from-a-nestjs-service)
- [134: Can you use BullMQ with Express?](#134-can-you-use-bullmq-with-express)
- [135: Should you create a new Queue for every request?](#135-should-you-create-a-new-queue-for-every-request)
- [136: Can you use Redis Cluster with BullMQ?](#136-can-you-use-redis-cluster-with-bullmq)
- [137: Does BullMQ work with Valkey or Dragonfly?](#137-does-bullmq-work-with-valkey-or-dragonfly)
- [138: What are the main parts of BullMQ's architecture?](#138-what-are-the-main-parts-of-bullmqs-architecture)
- [139: Why does BullMQ use Lua scripts?](#139-why-does-bullmq-use-lua-scripts)
- [140: What happens if you add a job with an existing custom jobId?](#140-what-happens-if-you-add-a-job-with-an-existing-custom-jobid)
- [141: What is the stalled event?](#141-what-is-the-stalled-event)
- [142: What is the difference between failed and stalled?](#142-what-is-the-difference-between-failed-and-stalled)
- [143: How do you see why a job failed?](#143-how-do-you-see-why-a-job-failed)
- [144: What is the job.opts.attempts default?](#144-what-is-the-joboptsattempts-default)
- [145: Can a worker process jobs of different names?](#145-can-a-worker-process-jobs-of-different-names)
- [146: Should you use one queue for everything or many queues?](#146-should-you-use-one-queue-for-everything-or-many-queues)
- [147: How do you start BullMQ with Docker Compose?](#147-how-do-you-start-bullmq-with-docker-compose)
- [148: What does queue.getJobLogs return?](#148-what-does-queuegetjoblogs-return)
- [149: Can you process jobs in the same process that adds them?](#149-can-you-process-jobs-in-the-same-process-that-adds-them)
- [150: What is a good first step when jobs are not being processed?](#150-what-is-a-good-first-step-when-jobs-are-not-being-processed)

### Moderate Questions (151-300)

- [151: How do you write a custom backoff strategy?](#151-how-do-you-write-a-custom-backoff-strategy)
- [152: What can a custom backoff strategy return besides a delay?](#152-what-can-a-custom-backoff-strategy-return-besides-a-delay)
- [153: How do you retry a job after a time chosen inside the processor?](#153-how-do-you-retry-a-job-after-a-time-chosen-inside-the-processor)
- [154: Why do you need to throw DelayedError after moveToDelayed?](#154-why-do-you-need-to-throw-delayederror-after-movetodelayed)
- [155: What is the token argument in the processor?](#155-what-is-the-token-argument-in-the-processor)
- [156: How do you build a job that runs in several steps?](#156-how-do-you-build-a-job-that-runs-in-several-steps)
- [157: How do you rate limit by a value the API gives you?](#157-how-do-you-rate-limit-by-a-value-the-api-gives-you)
- [158: Why must the limiter option be set to use manual rate limiting?](#158-why-must-the-limiter-option-be-set-to-use-manual-rate-limiting)
- [159: How do you check if a queue is rate limited?](#159-how-do-you-check-if-a-queue-is-rate-limited)
- [160: What is global concurrency?](#160-what-is-global-concurrency)
- [161: What is the global rate limit on a queue?](#161-what-is-the-global-rate-limit-on-a-queue)
- [162: What is the difference between concurrency and rate limiting?](#162-what-is-the-difference-between-concurrency-and-rate-limiting)
- [163: How do you change a worker's concurrency at runtime?](#163-how-do-you-change-a-workers-concurrency-at-runtime)
- [164: How do you choose the concurrency value?](#164-how-do-you-choose-the-concurrency-value)
- [165: When should you use sandboxed processors?](#165-when-should-you-use-sandboxed-processors)
- [166: What are the downsides of sandboxed processors?](#166-what-are-the-downsides-of-sandboxed-processors)
- [167: What can a sandboxed processor do with the job object?](#167-what-can-a-sandboxed-processor-do-with-the-job-object)
- [168: How do you add a job to a flow child queue with different options?](#168-how-do-you-add-a-job-to-a-flow-child-queue-with-different-options)
- [169: What happens to the parent if a child fails?](#169-what-happens-to-the-parent-if-a-child-fails)
- [170: What does failParentOnFailure do?](#170-what-does-failparentonfailure-do)
- [171: What does ignoreDependencyOnFailure do?](#171-what-does-ignoredependencyonfailure-do)
- [172: What does removeDependencyOnFailure do?](#172-what-does-removedependencyonfailure-do)
- [173: How do you get the whole tree of a flow?](#173-how-do-you-get-the-whole-tree-of-a-flow)
- [174: How do you add a child to an existing parent?](#174-how-do-you-add-a-child-to-an-existing-parent)
- [175: How do you add many flows at once?](#175-how-do-you-add-many-flows-at-once)
- [176: How do you build a parent that adds children while it runs?](#176-how-do-you-build-a-parent-that-adds-children-while-it-runs)
- [177: What does moveToWaitingChildren return?](#177-what-does-movetowaitingchildren-return)
- [178: How do you track job progress in a frontend?](#178-how-do-you-track-job-progress-in-a-frontend)
- [179: How do you count completed and failed jobs over time?](#179-how-do-you-count-completed-and-failed-jobs-over-time)
- [180: How do you keep Redis memory under control?](#180-how-do-you-keep-redis-memory-under-control)
- [181: How do you limit the size of the events stream?](#181-how-do-you-limit-the-size-of-the-events-stream)
- [182: What does keepLogs do?](#182-what-does-keeplogs-do)
- [183: How do you process a job manually without a processor function?](#183-how-do-you-process-a-job-manually-without-a-processor-function)
- [184: When would you use manual job processing?](#184-when-would-you-use-manual-job-processing)
- [185: How do you extend a job's lock when processing manually?](#185-how-do-you-extend-a-jobs-lock-when-processing-manually)
- [186: How does BullMQ handle delayed jobs internally?](#186-how-does-bullmq-handle-delayed-jobs-internally)
- [187: Why might a delayed job run later than its delay?](#187-why-might-a-delayed-job-run-later-than-its-delay)
- [188: What is a deduplication debounce mode?](#188-what-is-a-deduplication-debounce-mode)
- [189: What does keepLastIfActive do in deduplication?](#189-what-does-keeplastifactive-do-in-deduplication)
- [190: How do you clear a deduplication key early?](#190-how-do-you-clear-a-deduplication-key-early)
- [191: How do you find which job holds a deduplication ID?](#191-how-do-you-find-which-job-holds-a-deduplication-id)
- [192: How do you listen to deduplicated jobs?](#192-how-do-you-listen-to-deduplicated-jobs)
- [193: What replaced the debounce option?](#193-what-replaced-the-debounce-option)
- [194: How do you retry all failed jobs after fixing a bug?](#194-how-do-you-retry-all-failed-jobs-after-fixing-a-bug)
- [195: How do you promote all delayed jobs?](#195-how-do-you-promote-all-delayed-jobs)
- [196: How do you get a list of jobs page by page?](#196-how-do-you-get-a-list-of-jobs-page-by-page)
- [197: How do you pass different job options per job name?](#197-how-do-you-pass-different-job-options-per-job-name)
- [198: How do you set up BullMQ in NestJS with a shared connection?](#198-how-do-you-set-up-bullmq-in-nestjs-with-a-shared-connection)
- [199: How do you listen to worker events in NestJS?](#199-how-do-you-listen-to-worker-events-in-nestjs)
- [200: How do you set worker options like concurrency in NestJS?](#200-how-do-you-set-worker-options-like-concurrency-in-nestjs)
- [201: How do you use the PostgreSQL backend?](#201-how-do-you-use-the-postgresql-backend)
- [202: How do you run the PostgreSQL migrations?](#202-how-do-you-run-the-postgresql-migrations)
- [203: How do you make PostgreSQL the default backend for all classes?](#203-how-do-you-make-postgresql-the-default-backend-for-all-classes)
- [204: When would you choose PostgreSQL over Redis as the backend?](#204-when-would-you-choose-postgresql-over-redis-as-the-backend)
- [205: What should you watch out for with the PostgreSQL backend?](#205-what-should-you-watch-out-for-with-the-postgresql-backend)
- [206: How do you get the raw Redis client in v6?](#206-how-do-you-get-the-raw-redis-client-in-v6)
- [207: What changed in BullMQ 6 that affects existing code?](#207-what-changed-in-bullmq-6-that-affects-existing-code)
- [208: How do you migrate a repeatable job to a job scheduler?](#208-how-do-you-migrate-a-repeatable-job-to-a-job-scheduler)
- [209: When does a job scheduler create the next job?](#209-when-does-a-job-scheduler-create-the-next-job)
- [210: Can you choose the job ID for scheduler jobs?](#210-can-you-choose-the-job-id-for-scheduler-jobs)
- [211: How do you update a job scheduler's data or options?](#211-how-do-you-update-a-job-schedulers-data-or-options)
- [212: How many fields does a BullMQ cron pattern have?](#212-how-many-fields-does-a-bullmq-cron-pattern-have)
- [213: What happens if the same scheduler is upserted from many app instances?](#213-what-happens-if-the-same-scheduler-is-upserted-from-many-app-instances)
- [214: How do you run a job once at a specific date and time?](#214-how-do-you-run-a-job-once-at-a-specific-date-and-time)
- [215: How do you cancel a scheduled one-time job?](#215-how-do-you-cancel-a-scheduled-one-time-job)
- [216: How do you handle a job that calls an external API that sometimes times out?](#216-how-do-you-handle-a-job-that-calls-an-external-api-that-sometimes-times-out)
- [217: Does BullMQ have a job timeout option?](#217-does-bullmq-have-a-job-timeout-option)
- [218: How do you send failed jobs to a dead letter queue?](#218-how-do-you-send-failed-jobs-to-a-dead-letter-queue)
- [219: How do you know if a failed event is the final failure?](#219-how-do-you-know-if-a-failed-event-is-the-final-failure)
- [220: How do you use job names for routing in a large worker?](#220-how-do-you-use-job-names-for-routing-in-a-large-worker)
- [221: How do you type job names in TypeScript?](#221-how-do-you-type-job-names-in-typescript)
- [222: How do you share the Redis connection settings across files?](#222-how-do-you-share-the-redis-connection-settings-across-files)
- [223: What is enableOfflineQueue and why turn it off for producers?](#223-what-is-enableofflinequeue-and-why-turn-it-off-for-producers)
- [224: Should a producer use maxRetriesPerRequest null?](#224-should-a-producer-use-maxretriesperrequest-null)
- [225: How do you handle Redis being down when adding a job?](#225-how-do-you-handle-redis-being-down-when-adding-a-job)
- [226: What is the transactional outbox pattern with BullMQ?](#226-what-is-the-transactional-outbox-pattern-with-bullmq)
- [227: How do you avoid adding a job before the database transaction commits?](#227-how-do-you-avoid-adding-a-job-before-the-database-transaction-commits)
- [228: How do you pass a large payload to a job?](#228-how-do-you-pass-a-large-payload-to-a-job)
- [229: What does the sizeLimit job option do?](#229-what-does-the-sizelimit-job-option-do)
- [230: How do you get job counts for a dashboard quickly?](#230-how-do-you-get-job-counts-for-a-dashboard-quickly)
- [231: How do you find jobs by their data, like all jobs for user 5?](#231-how-do-you-find-jobs-by-their-data-like-all-jobs-for-user-5)
- [232: How do you write integration tests for BullMQ?](#232-how-do-you-write-integration-tests-for-bullmq)
- [233: Why do tests with BullMQ sometimes hang?](#233-why-do-tests-with-bullmq-sometimes-hang)
- [234: Why do you need waitUntilReady on QueueEvents in tests?](#234-why-do-you-need-waituntilready-on-queueevents-in-tests)
- [235: How do you mock BullMQ in unit tests?](#235-how-do-you-mock-bullmq-in-unit-tests)
- [236: How do you log every job in a consistent way?](#236-how-do-you-log-every-job-in-a-consistent-way)
- [237: How do you add OpenTelemetry tracing to BullMQ?](#237-how-do-you-add-opentelemetry-tracing-to-bullmq)
- [238: What should you alert on for a BullMQ system?](#238-what-should-you-alert-on-for-a-bullmq-system)
- [239: How do you measure how long jobs wait before running?](#239-how-do-you-measure-how-long-jobs-wait-before-running)
- [240: How do you expose queue stats to Prometheus?](#240-how-do-you-expose-queue-stats-to-prometheus)
- [241: How do you run workers on Kubernetes?](#241-how-do-you-run-workers-on-kubernetes)
- [242: How do you autoscale workers by queue length?](#242-how-do-you-autoscale-workers-by-queue-length)
- [243: How do you run BullMQ workers on serverless platforms like AWS Lambda?](#243-how-do-you-run-bullmq-workers-on-serverless-platforms-like-aws-lambda)
- [244: How do you handle a job that needs a database connection?](#244-how-do-you-handle-a-job-that-needs-a-database-connection)
- [245: How do you make sure a job runs only once per day for a user?](#245-how-do-you-make-sure-a-job-runs-only-once-per-day-for-a-user)
- [246: How do you process jobs in strict order?](#246-how-do-you-process-jobs-in-strict-order)
- [247: Is BullMQ order guaranteed with many workers?](#247-is-bullmq-order-guaranteed-with-many-workers)
- [248: How do you chain jobs so one starts after another?](#248-how-do-you-chain-jobs-so-one-starts-after-another)
- [249: How do you handle jobs for a deleted entity?](#249-how-do-you-handle-jobs-for-a-deleted-entity)
- [250: How do you use QueueEvents with many queues?](#250-how-do-you-use-queueevents-with-many-queues)
- [251: What is the retries-exhausted event?](#251-what-is-the-retries-exhausted-event)
- [252: How do you remove completed jobs but keep failed ones longer?](#252-how-do-you-remove-completed-jobs-but-keep-failed-ones-longer)
- [253: Can you set removeOnComplete on the worker instead of the job?](#253-can-you-set-removeoncomplete-on-the-worker-instead-of-the-job)
- [254: Is age in removeOnComplete in seconds or milliseconds?](#254-is-age-in-removeoncomplete-in-seconds-or-milliseconds)
- [255: How do you show a user the position of their job in the queue?](#255-how-do-you-show-a-user-the-position-of-their-job-in-the-queue)
- [256: How do you cancel a job that is already running?](#256-how-do-you-cancel-a-job-that-is-already-running)
- [257: How do you handle long-running jobs?](#257-how-do-you-handle-long-running-jobs)
- [258: Why do CPU-heavy jobs cause stalled jobs?](#258-why-do-cpu-heavy-jobs-cause-stalled-jobs)
- [259: How do you fix many stalled jobs?](#259-how-do-you-fix-many-stalled-jobs)
- [260: What does stalledInterval do?](#260-what-does-stalledinterval-do)
- [261: How do you handle errors from a worker that aren't job errors?](#261-how-do-you-handle-errors-from-a-worker-that-arent-job-errors)
- [262: Can a worker listen to more than one queue?](#262-can-a-worker-listen-to-more-than-one-queue)
- [263: How do you pause all processing during a deploy?](#263-how-do-you-pause-all-processing-during-a-deploy)
- [264: How do you move a job from failed to delayed for a later retry?](#264-how-do-you-move-a-job-from-failed-to-delayed-for-a-later-retry)
- [265: What is job.getDependencies used for?](#265-what-is-jobgetdependencies-used-for)
- [266: How do you read failed children of a parent?](#266-how-do-you-read-failed-children-of-a-parent)
- [267: Can flows have children in different Redis instances?](#267-can-flows-have-children-in-different-redis-instances)
- [268: How deep can a flow be?](#268-how-deep-can-a-flow-be)
- [269: How do you add a flow where the parent has no work of its own?](#269-how-do-you-add-a-flow-where-the-parent-has-no-work-of-its-own)
- [270: How do you know when a whole flow is done?](#270-how-do-you-know-when-a-whole-flow-is-done)
- [271: How do you set default options for all jobs in a flow?](#271-how-do-you-set-default-options-for-all-jobs-in-a-flow)
- [272: What happens if you remove a parent job?](#272-what-happens-if-you-remove-a-parent-job)
- [273: What is a common way to batch work with BullMQ open source?](#273-what-is-a-common-way-to-batch-work-with-bullmq-open-source)
- [274: What are BullMQ Pro groups?](#274-what-are-bullmq-pro-groups)
- [275: How do you get fair processing per customer without BullMQ Pro?](#275-how-do-you-get-fair-processing-per-customer-without-bullmq-pro)
- [276: How do you rate limit per customer without Pro groups?](#276-how-do-you-rate-limit-per-customer-without-pro-groups)
- [277: How do you handle time zones and daylight saving time in schedulers?](#277-how-do-you-handle-time-zones-and-daylight-saving-time-in-schedulers)
- [278: How do you limit how many times a scheduler runs?](#278-how-do-you-limit-how-many-times-a-scheduler-runs)
- [279: How do you start a scheduler at a later date?](#279-how-do-you-start-a-scheduler-at-a-later-date)
- [280: How do you run a scheduler job right away and then on the interval?](#280-how-do-you-run-a-scheduler-job-right-away-and-then-on-the-interval)
- [281: What is job.parentKey?](#281-what-is-jobparentkey)
- [282: How do you check if a job is part of a flow?](#282-how-do-you-check-if-a-job-is-part-of-a-flow)
- [283: Can you add jobs from a worker to another queue?](#283-can-you-add-jobs-from-a-worker-to-another-queue)
- [284: What problem can happen when you add a job at the end of a processor?](#284-what-problem-can-happen-when-you-add-a-job-at-the-end-of-a-processor)
- [285: How do you set a prefix per environment?](#285-how-do-you-set-a-prefix-per-environment)
- [286: What happens if Queue and Worker use different prefixes?](#286-what-happens-if-queue-and-worker-use-different-prefixes)
- [287: How do you inspect BullMQ keys in Redis?](#287-how-do-you-inspect-bullmq-keys-in-redis)
- [288: How do you migrate jobs from Bull to BullMQ?](#288-how-do-you-migrate-jobs-from-bull-to-bullmq)
- [289: How do you add jobs from a Python service and process them in Node.js?](#289-how-do-you-add-jobs-from-a-python-service-and-process-them-in-nodejs)
- [290: How do you avoid hot keys and noisy neighbors in a shared Redis?](#290-how-do-you-avoid-hot-keys-and-noisy-neighbors-in-a-shared-redis)
- [291: What is the difference between getJobs and getJobCounts in cost?](#291-what-is-the-difference-between-getjobs-and-getjobcounts-in-cost)
- [292: How do you write a worker that processes a CSV import?](#292-how-do-you-write-a-worker-that-processes-a-csv-import)
- [293: How do you send emails in bulk without being blocked by the provider?](#293-how-do-you-send-emails-in-bulk-without-being-blocked-by-the-provider)
- [294: How do you process webhooks you received with BullMQ?](#294-how-do-you-process-webhooks-you-received-with-bullmq)
- [295: How do you send outgoing webhooks reliably?](#295-how-do-you-send-outgoing-webhooks-reliably)
- [296: How do you test retry and backoff logic quickly?](#296-how-do-you-test-retry-and-backoff-logic-quickly)
- [297: What does worker.isRunning tell you?](#297-what-does-workerisrunning-tell-you)
- [298: How do you write a health check for a worker process?](#298-how-do-you-write-a-health-check-for-a-worker-process)
- [299: What does the worker closing property mean?](#299-what-does-the-worker-closing-property-mean)
- [300: How do you upgrade BullMQ to a new major version safely?](#300-how-do-you-upgrade-bullmq-to-a-new-major-version-safely)

### Advanced Questions (301-450)

- [301: Which Redis data structures does BullMQ use for a queue?](#301-which-redis-data-structures-does-bullmq-use-for-a-queue)
- [302: How does a worker wait for jobs without polling?](#302-how-does-a-worker-wait-for-jobs-without-polling)
- [303: What is the marker key and why was it added?](#303-what-is-the-marker-key-and-why-was-it-added)
- [304: What happens step by step when a worker takes a job?](#304-what-happens-step-by-step-when-a-worker-takes-a-job)
- [305: What happens step by step when a job completes?](#305-what-happens-step-by-step-when-a-job-completes)
- [306: Why does moveToCompleted fetch the next job?](#306-why-does-movetocompleted-fetch-the-next-job)
- [307: How does lock renewal work in a worker?](#307-how-does-lock-renewal-work-in-a-worker)
- [308: How does the stalled job checker work?](#308-how-does-the-stalled-job-checker-work)
- [309: What is the difference between attemptsMade and attemptsStarted?](#309-what-is-the-difference-between-attemptsmade-and-attemptsstarted)
- [310: What is stalledCounter on a job?](#310-what-is-stalledcounter-on-a-job)
- [311: What delivery guarantee does BullMQ give?](#311-what-delivery-guarantee-does-bullmq-give)
- [312: How do you make a job's side effects exactly-once in practice?](#312-how-do-you-make-a-jobs-side-effects-exactly-once-in-practice)
- [313: Why is the job ID not always a good idempotency key?](#313-why-is-the-job-id-not-always-a-good-idempotency-key)
- [314: How does BullMQ keep queue operations atomic?](#314-how-does-bullmq-keep-queue-operations-atomic)
- [315: Why does Redis Cluster need a hash tag in the prefix?](#315-why-does-redis-cluster-need-a-hash-tag-in-the-prefix)
- [316: How do you spread load in Redis Cluster with BullMQ?](#316-how-do-you-spread-load-in-redis-cluster-with-bullmq)
- [317: What are the risks of running BullMQ on a Redis replica setup with failover?](#317-what-are-the-risks-of-running-bullmq-on-a-redis-replica-setup-with-failover)
- [318: Which Redis persistence settings fit BullMQ?](#318-which-redis-persistence-settings-fit-bullmq)
- [319: Why is maxmemory-policy noeviction required?](#319-why-is-maxmemory-policy-noeviction-required)
- [320: What happens when Redis runs out of memory with noeviction?](#320-what-happens-when-redis-runs-out-of-memory-with-noeviction)
- [321: How do you estimate Redis memory for BullMQ?](#321-how-do-you-estimate-redis-memory-for-bullmq)
- [322: Why can many workers on many queues use too many Redis connections?](#322-why-can-many-workers-on-many-queues-use-too-many-redis-connections)
- [323: Can you share one ioredis connection between many workers?](#323-can-you-share-one-ioredis-connection-between-many-workers)
- [324: How do you design BullMQ for very high throughput?](#324-how-do-you-design-bullmq-for-very-high-throughput)
- [325: What usually limits BullMQ throughput?](#325-what-usually-limits-bullmq-throughput)
- [326: How do priorities work internally?](#326-how-do-priorities-work-internally)
- [327: Why can priorities be slow with a large queue?](#327-why-can-priorities-be-slow-with-a-large-queue)
- [328: Why are jobs without priority processed before prioritized ones?](#328-why-are-jobs-without-priority-processed-before-prioritized-ones)
- [329: What happens to a job's priority after a retry?](#329-what-happens-to-a-jobs-priority-after-a-retry)
- [330: How do rate limiting internals work?](#330-how-do-rate-limiting-internals-work)
- [331: Why is the worker limiter not exact under high load?](#331-why-is-the-worker-limiter-not-exact-under-high-load)
- [332: How do you combine a global rate limit with group-like limits?](#332-how-do-you-combine-a-global-rate-limit-with-group-like-limits)
- [333: How would you design per-tenant isolation with open source BullMQ?](#333-how-would-you-design-per-tenant-isolation-with-open-source-bullmq)
- [334: How does deduplication work internally?](#334-how-does-deduplication-work-internally)
- [335: What can go wrong if deduplication keys are not removed?](#335-what-can-go-wrong-if-deduplication-keys-are-not-removed)
- [336: How do job schedulers avoid duplicates when many instances run?](#336-how-do-job-schedulers-avoid-duplicates-when-many-instances-run)
- [337: What happens to a scheduler if no worker runs for a few hours?](#337-what-happens-to-a-scheduler-if-no-worker-runs-for-a-few-hours)
- [338: How do you run a cron job on only one machine without BullMQ?](#338-how-do-you-run-a-cron-job-on-only-one-machine-without-bullmq)
- [339: How does the parent-child link in a flow work internally?](#339-how-does-the-parent-child-link-in-a-flow-work-internally)
- [340: Why is a flow added in one atomic call?](#340-why-is-a-flow-added-in-one-atomic-call)
- [341: What happens with a flow when a child is removed by removeOnComplete?](#341-what-happens-with-a-flow-when-a-child-is-removed-by-removeoncomplete)
- [342: How do you build a fan-out and fan-in pipeline with BullMQ?](#342-how-do-you-build-a-fan-out-and-fan-in-pipeline-with-bullmq)
- [343: What are the limits of very large flows?](#343-what-are-the-limits-of-very-large-flows)
- [344: How do you design a saga with BullMQ?](#344-how-do-you-design-a-saga-with-bullmq)
- [345: What happens if a parent job fails after its children succeeded?](#345-what-happens-if-a-parent-job-fails-after-its-children-succeeded)
- [346: What is continueParentOnFailure?](#346-what-is-continueparentonfailure)
- [347: How does BullMQ pass data between a sandboxed processor and the main process?](#347-how-does-bullmq-pass-data-between-a-sandboxed-processor-and-the-main-process)
- [348: How are sandboxed child processes managed?](#348-how-are-sandboxed-child-processes-managed)
- [349: How do you pass startup settings to a sandboxed processor?](#349-how-do-you-pass-startup-settings-to-a-sandboxed-processor)
- [350: What are the memory risks of sandboxed processors?](#350-what-are-the-memory-risks-of-sandboxed-processors)
- [351: How do you handle graceful shutdown with long jobs on Kubernetes?](#351-how-do-you-handle-graceful-shutdown-with-long-jobs-on-kubernetes)
- [352: What happens to active jobs when a pod is killed with SIGKILL?](#352-what-happens-to-active-jobs-when-a-pod-is-killed-with-sigkill)
- [353: How do you reduce the time to recover stalled jobs?](#353-how-do-you-reduce-the-time-to-recover-stalled-jobs)
- [354: What is skipStalledCheck and when would you use it?](#354-what-is-skipstalledcheck-and-when-would-you-use-it)
- [355: What is skipLockRenewal?](#355-what-is-skiplockrenewal)
- [356: How do you debug a job that runs twice?](#356-how-do-you-debug-a-job-that-runs-twice)
- [357: How do you debug jobs stuck in active?](#357-how-do-you-debug-jobs-stuck-in-active)
- [358: Why can a processor promise never resolve?](#358-why-can-a-processor-promise-never-resolve)
- [359: How do you debug jobs stuck in delayed?](#359-how-do-you-debug-jobs-stuck-in-delayed)
- [360: How do clock differences between servers affect BullMQ?](#360-how-do-clock-differences-between-servers-affect-bullmq)
- [361: How do you debug jobs stuck in waiting-children?](#361-how-do-you-debug-jobs-stuck-in-waiting-children)
- [362: How do you handle poison messages?](#362-how-do-you-handle-poison-messages)
- [363: How do you protect against huge job data at the producer side?](#363-how-do-you-protect-against-huge-job-data-at-the-producer-side)
- [364: What security risks exist in BullMQ setups?](#364-what-security-risks-exist-in-bullmq-setups)
- [365: Should you put secrets or tokens in job data?](#365-should-you-put-secrets-or-tokens-in-job-data)
- [366: How do you protect personal data in jobs?](#366-how-do-you-protect-personal-data-in-jobs)
- [367: How do you secure the connection to Redis?](#367-how-do-you-secure-the-connection-to-redis)
- [368: What Redis ACL permissions does BullMQ need?](#368-what-redis-acl-permissions-does-bullmq-need)
- [369: How would you validate job data in the worker?](#369-how-would-you-validate-job-data-in-the-worker)
- [370: How do you version job data when the format changes?](#370-how-do-you-version-job-data-when-the-format-changes)
- [371: Why should you deploy workers before producers when changing a job format?](#371-why-should-you-deploy-workers-before-producers-when-changing-a-job-format)
- [372: How do you rename a queue in production without losing jobs?](#372-how-do-you-rename-a-queue-in-production-without-losing-jobs)
- [373: How do you move jobs from one Redis instance to another?](#373-how-do-you-move-jobs-from-one-redis-instance-to-another)
- [374: How do you replay failed jobs after an outage at a controlled pace?](#374-how-do-you-replay-failed-jobs-after-an-outage-at-a-controlled-pace)
- [375: How do you design a priority system with many levels?](#375-how-do-you-design-a-priority-system-with-many-levels)
- [376: How can low-priority jobs starve and how do you prevent it?](#376-how-can-low-priority-jobs-starve-and-how-do-you-prevent-it)
- [377: What is the cost of changePriority?](#377-what-is-the-cost-of-changepriority)
- [378: How does lifo interact with priority?](#378-how-does-lifo-interact-with-priority)
- [379: How do you implement a delayed retry with jitter by hand?](#379-how-do-you-implement-a-delayed-retry-with-jitter-by-hand)
- [380: How do you implement a circuit breaker with BullMQ?](#380-how-do-you-implement-a-circuit-breaker-with-bullmq)
- [381: When would you pause a queue from inside a worker?](#381-when-would-you-pause-a-queue-from-inside-a-worker)
- [382: What happens to the event stream when no QueueEvents listener is running?](#382-what-happens-to-the-event-stream-when-no-queueevents-listener-is-running)
- [383: How reliable are QueueEvents?](#383-how-reliable-are-queueevents)
- [384: Why should important side effects not happen in a completed event listener?](#384-why-should-important-side-effects-not-happen-in-a-completed-event-listener)
- [385: How do you scale QueueEvents for a WebSocket server with many instances?](#385-how-do-you-scale-queueevents-for-a-websocket-server-with-many-instances)
- [386: How do you track per-user progress for many users efficiently?](#386-how-do-you-track-per-user-progress-for-many-users-efficiently)
- [387: What are the trade-offs of keeping completed jobs?](#387-what-are-the-trade-offs-of-keeping-completed-jobs)
- [388: How do you store job results long term?](#388-how-do-you-store-job-results-long-term)
- [389: How do you design a queue system for multiple regions?](#389-how-do-you-design-a-queue-system-for-multiple-regions)
- [390: How would you compare BullMQ with RabbitMQ?](#390-how-would-you-compare-bullmq-with-rabbitmq)
- [391: How would you compare BullMQ with Kafka?](#391-how-would-you-compare-bullmq-with-kafka)
- [392: How would you compare BullMQ with AWS SQS?](#392-how-would-you-compare-bullmq-with-aws-sqs)
- [393: How would you compare BullMQ with pg-boss or Graphile Worker?](#393-how-would-you-compare-bullmq-with-pg-boss-or-graphile-worker)
- [394: How would you compare BullMQ with Temporal?](#394-how-would-you-compare-bullmq-with-temporal)
- [395: When would you not choose BullMQ?](#395-when-would-you-not-choose-bullmq)
- [396: How do you make a job wait for an external event, like a user confirmation?](#396-how-do-you-make-a-job-wait-for-an-external-event-like-a-user-confirmation)
- [397: How do you handle jobs that need a lock on a shared resource?](#397-how-do-you-handle-jobs-that-need-a-lock-on-a-shared-resource)
- [398: How do you avoid thundering herd effects after a long outage?](#398-how-do-you-avoid-thundering-herd-effects-after-a-long-outage)
- [399: How do you design job retries for payment operations?](#399-how-do-you-design-job-retries-for-payment-operations)
- [400: What happens if two workers run with different processor code during a deploy?](#400-what-happens-if-two-workers-run-with-different-processor-code-during-a-deploy)
- [401: How does the BullMQ v6 backend system work?](#401-how-does-the-bullmq-v6-backend-system-work)
- [402: What is a BackendFactory?](#402-what-is-a-backendfactory)
- [403: How do queues on PostgreSQL take jobs without workers getting in each other's way?](#403-how-do-queues-on-postgresql-take-jobs-without-workers-getting-in-each-others-way)
- [404: How do you size the PostgreSQL pool for BullMQ workers?](#404-how-do-you-size-the-postgresql-pool-for-bullmq-workers)
- [405: Can you run Redis and PostgreSQL backends side by side?](#405-can-you-run-redis-and-postgresql-backends-side-by-side)
- [406: Why did BullMQ 6 make migrations for PostgreSQL explicit?](#406-why-did-bullmq-6-make-migrations-for-postgresql-explicit)
- [407: How would you run BullMQ on a managed Redis service?](#407-how-would-you-run-bullmq-on-a-managed-redis-service)
- [408: What issues can come up with serverless Redis like Upstash?](#408-what-issues-can-come-up-with-serverless-redis-like-upstash)
- [409: What does drainDelay do?](#409-what-does-draindelay-do)
- [410: How do you profile a slow worker?](#410-how-do-you-profile-a-slow-worker)
- [411: How do you detect event loop blocking in a worker?](#411-how-do-you-detect-event-loop-blocking-in-a-worker)
- [412: How do Redis Lua scripts in BullMQ affect Redis latency?](#412-how-do-redis-lua-scripts-in-bullmq-affect-redis-latency)
- [413: Why does obliterate run in batches?](#413-why-does-obliterate-run-in-batches)
- [414: What is the cost of getJobs on a big completed set?](#414-what-is-the-cost-of-getjobs-on-a-big-completed-set)
- [415: How do you safely clean a queue with millions of completed jobs?](#415-how-do-you-safely-clean-a-queue-with-millions-of-completed-jobs)
- [416: How do you handle a sudden spike of a million jobs?](#416-how-do-you-handle-a-sudden-spike-of-a-million-jobs)
- [417: What is backpressure and how do you apply it with BullMQ?](#417-what-is-backpressure-and-how-do-you-apply-it-with-bullmq)
- [418: How would you design a video processing pipeline with BullMQ?](#418-how-would-you-design-a-video-processing-pipeline-with-bullmq)
- [419: How would you design a notification service with BullMQ?](#419-how-would-you-design-a-notification-service-with-bullmq)
- [420: How would you design scheduled reports for thousands of customers?](#420-how-would-you-design-scheduled-reports-for-thousands-of-customers)
- [421: Why avoid thousands of job schedulers?](#421-why-avoid-thousands-of-job-schedulers)
- [422: How would you handle multi-step onboarding emails over days?](#422-how-would-you-handle-multi-step-onboarding-emails-over-days)
- [423: How do you prevent a job from running if its data is outdated?](#423-how-do-you-prevent-a-job-from-running-if-its-data-is-outdated)
- [424: How do you implement a delay queue for retries at specific times?](#424-how-do-you-implement-a-delay-queue-for-retries-at-specific-times)
- [425: Does moving a job to delayed with DelayedError use an attempt?](#425-does-moving-a-job-to-delayed-with-delayederror-use-an-attempt)
- [426: How does BullMQ handle a job whose processor resolves after its lock was lost?](#426-how-does-bullmq-handle-a-job-whose-processor-resolves-after-its-lock-was-lost)
- [427: What does the error "Missing lock for job" mean?](#427-what-does-the-error-missing-lock-for-job-mean)
- [428: What does "job stalled more than allowable limit" mean?](#428-what-does-job-stalled-more-than-allowable-limit-mean)
- [429: Why might a worker log "Connection is closed" errors on shutdown?](#429-why-might-a-worker-log-connection-is-closed-errors-on-shutdown)
- [430: How do you close shared connections in the right order?](#430-how-do-you-close-shared-connections-in-the-right-order)
- [431: What happens if you call queue.add with a very large addBulk array?](#431-what-happens-if-you-call-queueadd-with-a-very-large-addbulk-array)
- [432: How do you choose between many small jobs and fewer big jobs?](#432-how-do-you-choose-between-many-small-jobs-and-fewer-big-jobs)
- [433: How do you keep job order per key with many workers?](#433-how-do-you-keep-job-order-per-key-with-many-workers)
- [434: How does BullMQ Pro groups keep order per group?](#434-how-does-bullmq-pro-groups-keep-order-per-group)
- [435: What are BullMQ Pro observables?](#435-what-are-bullmq-pro-observables)
- [436: How would you implement job cancellation for running jobs in open source BullMQ?](#436-how-would-you-implement-job-cancellation-for-running-jobs-in-open-source-bullmq)
- [437: How do you prevent a hot key in the limiter or meta keys?](#437-how-do-you-prevent-a-hot-key-in-the-limiter-or-meta-keys)
- [438: How do you plan Redis capacity for BullMQ?](#438-how-do-you-plan-redis-capacity-for-bullmq)
- [439: How do you load test BullMQ?](#439-how-do-you-load-test-bullmq)
- [440: What happens to job schedulers if you obliterate a queue?](#440-what-happens-to-job-schedulers-if-you-obliterate-a-queue)
- [441: How do you keep job schedulers in sync with your code?](#441-how-do-you-keep-job-schedulers-in-sync-with-your-code)
- [442: How do you handle backward compatibility for jobs left in a queue after a v5 to v6 upgrade?](#442-how-do-you-handle-backward-compatibility-for-jobs-left-in-a-queue-after-a-v5-to-v6-upgrade)
- [443: Why did v6 remove the paused state from jobs?](#443-why-did-v6-remove-the-paused-state-from-jobs)
- [444: What does ioredis being an optional peer dependency mean for you?](#444-what-does-ioredis-being-an-optional-peer-dependency-mean-for-you)
- [445: How do you avoid memory leaks in long-running workers?](#445-how-do-you-avoid-memory-leaks-in-long-running-workers)
- [446: How do you handle a worker that has to finish its job even during shutdown?](#446-how-do-you-handle-a-worker-that-has-to-finish-its-job-even-during-shutdown)
- [447: How would you investigate a sudden rise in failed jobs?](#447-how-would-you-investigate-a-sudden-rise-in-failed-jobs)
- [448: How do you design for "at least once" delivery in a whole system?](#448-how-do-you-design-for-at-least-once-delivery-in-a-whole-system)
- [449: What are common mistakes teams make with BullMQ in production?](#449-what-are-common-mistakes-teams-make-with-bullmq-in-production)
- [450: How would you explain BullMQ's trade-offs to your team?](#450-how-would-you-explain-bullmqs-trade-offs-to-your-team)

---

# Easy Questions (1-150)

## 1: What is BullMQ?

BullMQ is a Node.js library for job queues and background jobs. You add jobs to a queue from one part of your app, and workers pick them up and process them, often in a different process or on a different machine. By default it stores everything in Redis. Since v6 it can also use PostgreSQL as the storage backend.

## 2: What problems does BullMQ solve?

It moves slow or unreliable work out of the request path. Typical examples are sending emails, resizing images, generating reports, calling third-party APIs and running scheduled tasks. BullMQ gives you retries, delays, priorities, rate limiting, scheduling and job history, so you don't have to build them yourself.

## 3: How do you install BullMQ?

Install the package and the client for the backend you use. Since v6, `ioredis` is an optional peer dependency, so Redis users install it explicitly.

```bash
npm install bullmq ioredis
# for the PostgreSQL backend instead:
npm install bullmq pg
```

## 4: What are the main classes in BullMQ?

- `Queue`: adds jobs and manages the queue.
- `Worker`: takes jobs from the queue and runs your processor function.
- `QueueEvents`: listens to events of a queue from any process.
- `FlowProducer`: adds trees of parent and child jobs.
- `Job`: represents a single job and its data, state and options.

## 5: How do you create a queue and add a job?

```js
import { Queue } from "bullmq";

const emailQueue = new Queue("email", {
  connection: { host: "localhost", port: 6379 },
});

await emailQueue.add("welcome", { to: "ana@example.com" });
```

The first argument of `add` is the job name, the second is the job data.

## 6: How do you create a worker?

```js
import { Worker } from "bullmq";

const worker = new Worker(
  "email",
  async (job) => {
    await sendEmail(job.data.to);
    return { sent: true };
  },
  { connection: { host: "localhost", port: 6379 } },
);
```

The worker listens to the queue with the same name and calls the function for every job. Whatever the function returns is saved as the job's return value.

## 7: What is a job in BullMQ?

A job is one unit of work. It has a name, data (any JSON-serializable value), options (delay, attempts, priority and so on) and an ID. BullMQ also stores info about it, such as its state, progress, return value, failure reason, number of attempts and timestamps.

## 8: What is the difference between a queue and a worker?

The queue is where jobs wait. The `Queue` class is used by producers to add jobs and to inspect or manage them. A `Worker` is a consumer that pulls jobs from the queue and runs them. They usually live in different processes, and they only share the queue name and the connection.

## 9: Why does BullMQ need Redis?

Redis is the default backend. BullMQ keeps jobs, their states and events in Redis data structures (lists, sorted sets, hashes and streams) and changes them with Lua scripts so each step is atomic. Redis is fast and shared, so many producers and workers on different machines can work with the same queue.

## 10: Can BullMQ work without Redis?

Yes, since v6. BullMQ 6 has pluggable backends, and it ships a PostgreSQL backend that runs the same `Queue`, `Worker`, `QueueEvents` and `FlowProducer` API. You pass `createPostgresBackend` to the constructors. Redis is still the default and is usually faster.

## 11: What is a producer in BullMQ?

A producer is any code that adds jobs to a queue, for example an Express route that adds a "send receipt" job after a payment. It only needs a `Queue` instance. It does not wait for the job to finish unless you ask it to.

## 12: What is a consumer in BullMQ?

A consumer is the code that processes jobs. In BullMQ that is a `Worker` with a processor function. You can run as many workers as you want for one queue, and each job is given to only one of them at a time.

## 13: What is a processor function?

It is the async function you pass to `Worker`. It gets the job (and a lock token as the second argument) and does the work. If it returns, the job is completed. If it throws, the job fails and may be retried.

```js
const worker = new Worker(
  "pdf",
  async (job, token) => {
    const file = await buildPdf(job.data.orderId);
    return { file };
  },
  { connection },
);
```

## 14: What are the possible states of a job?

- `waiting`: ready to be picked up.
- `prioritized`: waiting, but with a priority.
- `delayed`: waiting for its delay to pass.
- `active`: being processed by a worker.
- `completed`: finished without errors.
- `failed`: threw an error and has no attempts left.
- `waiting-children`: a parent job waiting for its children in a flow.

In v6 the old `paused` state is gone. Jobs in a paused queue are counted as `waiting`.

## 15: What happens when a processor throws an error?

The job is marked as failed for that attempt. If it still has attempts left, BullMQ retries it, possibly after a backoff delay. If not, it moves to the `failed` state and `job.failedReason` and `job.stacktrace` are saved.

## 16: What does the job name mean?

The name is a label for the kind of job, like `'welcome'` or `'reset-password'`. A single queue can have jobs with different names, and the processor can check `job.name` to decide what to do. Names are also handy in dashboards and logs.

```js
new Worker(
  "email",
  async (job) => {
    if (job.name === "welcome") return sendWelcome(job.data);
    if (job.name === "reset") return sendReset(job.data);
  },
  { connection },
);
```

## 17: How do you pass data to a job?

Use the second argument of `queue.add`. It must be JSON serializable, because it is stored as a string. In the worker you read it from `job.data`.

```js
await queue.add("resize", { imageId: 42, width: 800 });
// in the worker
const { imageId, width } = job.data;
```

## 18: How do you get the result of a job?

The value returned by the processor is stored in `job.returnvalue`. You can read it later by loading the job, or you can wait for it with `job.waitUntilFinished(queueEvents)`. You can also listen to the `completed` event, which includes the return value.

## 19: How do you delay a job?

Use the `delay` option, in milliseconds. The job goes into the `delayed` state and moves to waiting once the delay passes.

```js
await queue.add("reminder", { userId: 7 }, { delay: 60 * 60 * 1000 });
```

## 20: How do you retry failed jobs automatically?

Set `attempts` when adding the job. The default is 1, which means no retries.

```js
await queue.add("charge", { orderId: 1 }, { attempts: 5 });
```

With this, the job can run up to 5 times before it ends up in `failed`.

## 21: What is backoff in BullMQ?

Backoff is the wait time between retries. Without it, a failed job is retried right away. BullMQ has two built-in types: `fixed` (same wait every time) and `exponential` (the wait doubles on every attempt).

```js
await queue.add("call-api", data, {
  attempts: 5,
  backoff: { type: "exponential", delay: 1000 },
});
```

## 22: How does exponential backoff calculate the delay?

The delay is `2 ^ (attemptsMade - 1) * delay`. With `delay: 1000`, retries wait about 1s, 2s, 4s, 8s and so on. You can add `jitter` (a number between 0 and 1) to randomize the delay a bit so many failed jobs don't retry at the exact same moment.

## 23: How do you set a job priority?

Use the `priority` option. 1 is the highest priority, larger numbers are lower. Jobs without a priority are processed before prioritized ones, because priority 0 means "no priority".

```js
await queue.add("report", data, { priority: 10 });
await queue.add("urgent-report", data, { priority: 1 });
```

## 24: What is the maximum priority value?

The allowed range is 1 to 2,097,152 (2^21). Lower numbers are processed first.

## 25: What does the lifo option do?

By default jobs are processed in FIFO order: first in, first out. With `lifo: true` the job is added to the front of the waiting list, so it is processed before older jobs.

```js
await queue.add("refresh", data, { lifo: true });
```

## 26: How do you give a job a custom ID?

Pass `jobId` in the options. If a job with that ID already exists, the new one is ignored. This is a simple way to avoid duplicates.

```js
await queue.add("invoice", { orderId: 99 }, { jobId: "invoice-99" });
```

Custom IDs can't be plain integers and shouldn't contain `:`, because BullMQ uses those for its own IDs and keys.

## 27: How are job IDs created by default?

BullMQ uses an increasing counter stored per queue, so IDs are `'1'`, `'2'`, `'3'` and so on. They are strings. The counter is unique per queue, not across queues.

## 28: How do you add several jobs at once?

Use `addBulk`. It adds all jobs in one atomic operation, which is faster than calling `add` in a loop.

```js
await queue.addBulk([
  { name: "email", data: { to: "a@x.com" } },
  { name: "email", data: { to: "b@x.com" }, opts: { priority: 2 } },
]);
```

## 29: How do you get a job by its ID?

```js
const job = await queue.getJob("123");
if (job) {
  console.log(job.name, job.data, await job.getState());
}
```

You can also use `Job.fromId(queue, '123')`. Both return `undefined` if the job doesn't exist.

## 30: How do you check the state of a job?

Call `await job.getState()`. It returns a string such as `'waiting'`, `'active'`, `'completed'`, `'failed'` or `'delayed'`. There are also helpers like `job.isCompleted()`, `job.isFailed()` and `job.isActive()`.

## 31: How do you report progress from a job?

Call `job.updateProgress()` with a number or an object. Listeners of the `progress` event get the value.

```js
new Worker(
  "import",
  async (job) => {
    for (let i = 0; i < 100; i++) {
      await importRow(i);
      await job.updateProgress(i + 1);
    }
  },
  { connection },
);
```

## 32: How do you add logs to a job?

Use `job.log('message')`. Logs are stored with the job and can be read with `queue.getJobLogs(jobId)` or seen in dashboards. The `keepLogs` option limits how many log lines are kept.

```js
await job.log(`Fetched ${rows.length} rows`);
```

## 33: What is the default worker concurrency?

1. A worker processes one job at a time unless you set the `concurrency` option. For I/O work like HTTP calls you can safely raise it.

```js
new Worker("email", processor, { connection, concurrency: 20 });
```

## 34: What does concurrency mean for a worker?

It is how many jobs one worker instance runs at the same time. All of them run in the same Node.js process, so this helps only when jobs spend time waiting on I/O. CPU-heavy jobs block the event loop, so for those you should use sandboxed processors or more processes.

## 35: Can several workers process the same queue?

Yes. You can start many workers for one queue, in one process or across many machines. BullMQ makes sure each job is taken by only one worker at a time. This is the normal way to scale.

## 36: What happens to a job after it completes?

It moves to the `completed` set, with its return value and finish time. By default BullMQ keeps completed jobs forever, which can fill Redis. Use `removeOnComplete` to clean them up.

## 37: What do removeOnComplete and removeOnFail do?

They control how many finished jobs are kept. `true` removes the job right away, a number keeps only the last N jobs, and an object can limit by age (in seconds) and count.

```js
await queue.add("email", data, {
  removeOnComplete: { age: 3600, count: 1000 },
  removeOnFail: { age: 24 * 3600 },
});
```

## 38: How do you set default options for all jobs in a queue?

Use `defaultJobOptions` on the `Queue`. Options passed to `add` override them.

```js
const queue = new Queue("email", {
  connection,
  defaultJobOptions: {
    attempts: 3,
    backoff: { type: "exponential", delay: 1000 },
    removeOnComplete: 1000,
  },
});
```

## 39: What is QueueEvents?

`QueueEvents` lets you listen to a queue's events (completed, failed, progress, waiting and so on) from any process, even one that has no workers. It reads them from a Redis stream, so events aren't lost if the listener reconnects for a short time.

```js
import { QueueEvents } from "bullmq";

const events = new QueueEvents("email", { connection });
events.on("completed", ({ jobId, returnvalue }) => {
  console.log(jobId, "done", returnvalue);
});
```

## 40: What events does a Worker emit?

The main ones are `completed`, `failed`, `progress`, `active`, `error`, `drained`, `stalled`, `ready` and `closed`. These are local: they only fire for jobs that this worker instance processed.

```js
worker.on("failed", (job, err) => {
  console.error(job?.id, err.message);
});
```

## 41: What is the difference between Worker events and QueueEvents?

Worker events are local to one worker instance and give you the full job object. `QueueEvents` are global for the queue and work across processes, but they only give you IDs and small payloads like `returnvalue` or `failedReason`. Use worker events for logging inside the worker, and `QueueEvents` to watch the queue from elsewhere.

## 42: Why should you listen to the worker error event?

If a worker emits `error` and nobody listens, Node.js may throw an unhandled error. Errors like a lost Redis connection are emitted here. Adding a listener keeps the process alive and lets you log the problem.

```js
worker.on("error", (err) => console.error("worker error", err));
```

## 43: How do you pause a queue?

```js
await queue.pause(); // stops all workers from taking new jobs
await queue.resume();
```

Jobs already running will finish. New jobs can still be added; they just wait. You can check the state with `queue.isPaused()`.

## 44: How do you pause a single worker?

Call `worker.pause()`. Only that worker stops taking new jobs, and other workers keep going. In v6 `worker.resume()` is async, so you have to `await` it.

```js
await worker.pause();
await worker.resume();
```

## 45: How do you close a worker?

Call `await worker.close()`. It stops taking new jobs and waits for active jobs to finish before closing the connections. `worker.close(true)` closes without waiting, so active jobs may later be seen as stalled.

## 46: How do you close a queue?

Call `await queue.close()` when you are done with it, for example on shutdown. It closes the Redis connection that the queue uses. The same goes for `QueueEvents` and `FlowProducer`.

## 47: How do you count jobs in a queue?

```js
const counts = await queue.getJobCounts("waiting", "active", "failed");
// { waiting: 12, active: 3, failed: 1 }
const waiting = await queue.getWaitingCount();
```

Without arguments, `getJobCounts()` returns counts for all states.

## 48: How do you list jobs in a certain state?

Use `getJobs` with the states and a range, or the helper methods like `getWaiting`, `getFailed` and `getCompleted`.

```js
const failed = await queue.getJobs(["failed"], 0, 49);
const delayed = await queue.getDelayed(0, 9);
```

## 49: How do you remove a job?

```js
const job = await queue.getJob("15");
await job?.remove();
// or
await queue.remove("15");
```

You can't remove a job that is locked by a worker (active). It has to finish first.

## 50: How do you retry a failed job manually?

Load the job and call `job.retry()`. It moves the job from `failed` back to `waiting`. To retry many at once, use `queue.retryJobs()`.

```js
const job = await queue.getJob(id);
await job.retry();
await queue.retryJobs({ state: "failed", count: 100 });
```

## 51: How do you empty a queue?

`queue.drain()` removes all waiting jobs. Pass `true` to remove delayed jobs too. Active, completed and failed jobs stay.

```js
await queue.drain(); // waiting jobs
await queue.drain(true); // waiting and delayed jobs
```

## 52: What does queue.clean do?

It removes old jobs in a given state. You give a grace period in milliseconds, a max number of jobs and the state. It returns the IDs of the removed jobs.

```js
// remove completed jobs older than 1 hour, up to 1000 of them
await queue.clean(60 * 60 * 1000, 1000, "completed");
```

## 53: What does queue.obliterate do?

It deletes the whole queue from Redis: all jobs, in every state, and the queue metadata. By default it fails if there are active jobs; `{ force: true }` deletes them anyway. Use it with care, mostly in tests or when retiring a queue.

```js
await queue.obliterate({ force: true });
```

## 54: What is the difference between drain, clean and obliterate?

- `drain` removes jobs that are waiting (and optionally delayed).
- `clean` removes jobs in one state that are older than a grace period.
- `obliterate` deletes everything about the queue.

## 55: What is a delayed job?

A job that should not run before a certain time. It sits in the `delayed` state until its delay is over, then moves to waiting and a worker can pick it up. Delays are a minimum: if all workers are busy, the job may start later.

## 56: How do you run a job right away if it is delayed?

Call `job.promote()`. It moves the job from delayed to waiting. To promote all delayed jobs, use `queue.promoteJobs()`.

```js
const job = await queue.getJob(id);
await job.promote();
```

## 57: How do you change the delay of a job that is already delayed?

```js
await job.changeDelay(10_000); // run 10 seconds from now
```

It only works while the job is in the delayed state.

## 58: What is a job scheduler?

A job scheduler creates jobs on a schedule, for example every 5 minutes or every day at 3 AM. You create it with `queue.upsertJobScheduler`. It is the modern replacement for the old repeatable jobs, which were removed in v6.

```js
await queue.upsertJobScheduler(
  "daily-report",
  { pattern: "0 0 3 * * *" },
  { name: "report", data: { type: "daily" } },
);
```

## 59: What is the difference between every and pattern in a job scheduler?

`every` is a fixed interval in milliseconds, like `{ every: 60000 }` for once a minute. `pattern` is a cron expression, like `'0 */5 * * * *'` for every 5 minutes. Use `every` for simple intervals and `pattern` when the time of day or week matters.

## 60: Why is it called upsertJobScheduler?

Because it creates the scheduler if it doesn't exist and updates it if it does. You can call it every time your app starts with the same scheduler ID, and you will not get duplicates. This makes deploys safe.

## 61: How do you remove a job scheduler?

```js
await queue.removeJobScheduler("daily-report");
```

After this, no new jobs are created by that scheduler.

## 62: How do you list job schedulers?

```js
const schedulers = await queue.getJobSchedulers();
const one = await queue.getJobScheduler("daily-report");
```

Each entry shows the scheduler's ID, its repeat settings and when the next job is due.

## 63: What were repeatable jobs?

In BullMQ v5 and older you could pass a `repeat` option to `queue.add` to make a job repeat. You then managed them with `getRepeatableJobs` and `removeRepeatableByKey`. This was removed in v6. You will still see it in older projects, but new code should use job schedulers.

## 64: How do you set a timezone for a cron scheduler?

Use the `tz` option with an IANA timezone name. The old `utc` option was removed in v6; use `tz: 'UTC'` instead.

```js
await queue.upsertJobScheduler("morning-email", {
  pattern: "0 0 8 * * *",
  tz: "Europe/Berlin",
});
```

## 65: What is a flow in BullMQ?

A flow is a tree of jobs where a parent job waits for all its children to finish before it runs. Children can be in different queues. You create flows with `FlowProducer`. They are useful when one task depends on the results of several others.

## 66: How do you create a flow?

```js
import { FlowProducer } from "bullmq";

const flow = new FlowProducer({ connection });

await flow.add({
  name: "build-report",
  queueName: "reports",
  data: { reportId: 1 },
  children: [
    { name: "sales", queueName: "fetch", data: { part: "sales" } },
    { name: "costs", queueName: "fetch", data: { part: "costs" } },
  ],
});
```

The `build-report` job waits in `waiting-children` until both children complete.

## 67: How does a parent job read the results of its children?

Use `job.getChildrenValues()`. It returns an object where each key is a child job key and each value is the child's return value.

```js
new Worker(
  "reports",
  async (job) => {
    const values = await job.getChildrenValues();
    return combine(Object.values(values));
  },
  { connection },
);
```

## 68: What is the waiting-children state?

It is the state of a parent job in a flow while its children are not done yet. When the last child completes, the parent moves to waiting and can be processed.

## 69: What is a sandboxed processor?

A processor that runs in a separate child process or worker thread instead of the main worker process. You pass a file path instead of a function. If the job crashes or blocks with heavy CPU work, it doesn't freeze the main process.

```js
import { Worker } from "bullmq";
import { fileURLToPath } from "node:url";

const file = fileURLToPath(new URL("./processor.js", import.meta.url));
new Worker("images", file, { connection });
```

## 70: What does a sandboxed processor file look like?

It exports a function that takes the job and returns the result.

```js
// processor.js
export default async function (job) {
  const result = await resizeImage(job.data.path);
  return result;
}
```

In CommonJS you write `module.exports = async (job) => { ... }`.

## 71: What does useWorkerThreads do?

By default sandboxed processors run in child processes. With `useWorkerThreads: true` they run in Node.js worker threads instead, which start faster and use less memory.

```js
new Worker("images", file, { connection, useWorkerThreads: true });
```

## 72: What is a stalled job?

A job that was active but whose worker stopped renewing its lock, for example because the process crashed or the event loop was blocked for too long. BullMQ detects it, moves it back to waiting so another worker can take it, and emits a `stalled` event.

## 73: What is a job lock?

When a worker takes a job, it gets a lock in Redis with a token. The worker keeps renewing the lock while it works. The lock shows other workers that the job is in progress. If the lock expires, the job is treated as stalled.

## 74: What is lockDuration?

It is how long a job lock lasts before it expires, in milliseconds. The default is 30 seconds. The worker renews the lock before it expires, so a job can run much longer than `lockDuration` as long as the worker is healthy.

## 75: What is maxStalledCount?

It is how many times a job may stall before BullMQ fails it instead of moving it back to waiting. The default is 1. After that the job fails with an error saying it stalled more than the allowed limit.

## 76: What is rate limiting in BullMQ?

It limits how many jobs are processed in a time window, for example 10 jobs per second. It is useful when you call an external API with a request limit. You set it with the `limiter` option on the worker.

```js
new Worker("api", processor, {
  connection,
  limiter: { max: 10, duration: 1000 },
});
```

## 77: Is the worker limiter per worker or for the whole queue?

It is for the whole queue. If you have 10 workers with `{ max: 10, duration: 1000 }`, together they still process only 10 jobs per second. Jobs above the limit stay waiting.

## 78: What is the default prefix for Redis keys?

`bull`. A queue named `email` uses keys like `bull:email:wait` and `bull:email:123`. You can change it with the `prefix` option, which must be the same on the queue, workers and events of that queue.

```js
new Queue("email", { connection, prefix: "myapp" });
```

## 79: How do you connect to Redis with a password or TLS?

Pass the usual ioredis options in `connection`.

```js
const connection = {
  host: "redis.example.com",
  port: 6380,
  username: "default",
  password: process.env.REDIS_PASSWORD,
  tls: {},
};
const queue = new Queue("email", { connection });
```

## 80: Can you reuse an ioredis instance?

Yes. Create an `IORedis` instance and pass it as `connection`. For workers, `maxRetriesPerRequest` must be `null`, or BullMQ throws an error.

```js
import IORedis from "ioredis";

const connection = new IORedis({ maxRetriesPerRequest: null });
const queue = new Queue("email", { connection });
const worker = new Worker("email", processor, { connection });
```

## 81: Why does a worker need maxRetriesPerRequest set to null?

Workers use blocking Redis commands to wait for jobs. If ioredis gave up on a command after a few retries during a disconnect, the worker could stop getting jobs. With `null`, ioredis keeps retrying until Redis is back. When you pass plain options instead of an instance, BullMQ sets this for you.

## 82: Does a worker use one Redis connection?

No. A worker uses at least two: one normal connection and one extra for blocking commands. `QueueEvents` also needs its own blocking connection. Keep this in mind when your Redis plan has a connection limit.

## 83: What is the maxmemory-policy setting and why does it matter?

It tells Redis what to do when memory is full. BullMQ needs `noeviction`, so Redis returns errors instead of deleting keys. With any other policy, Redis could silently delete job keys and leave the queue in a broken state.

## 84: What is BullMQ Pro?

A paid version of BullMQ from the same company (Taskforce.sh). It adds features like groups (fair processing and per-group limits), batches and observables. The open source package has everything most projects need.

## 85: What is the difference between Bull and BullMQ?

Bull is the older library by the same authors. BullMQ is a rewrite in TypeScript with a different API: separate `Queue`, `Worker` and `QueueEvents` classes, flows, better rate limiting and more. Bull is in maintenance mode, so new projects should use BullMQ.

## 86: Is BullMQ written in TypeScript?

Yes. It ships with type definitions, and `Queue`, `Worker` and `Job` take generics for data, return value and job name.

```ts
interface EmailData {
  to: string;
}
const queue = new Queue<EmailData>("email", { connection });
const worker = new Worker<EmailData, boolean>(
  "email",
  async (job) => {
    await send(job.data.to);
    return true;
  },
  { connection },
);
```

## 87: Can BullMQ be used from other languages?

Yes. Besides Node.js, there are official versions for Python, Elixir and PHP, and newer ones for Rust and .NET. They share the same Redis format, so for example a Node.js app can add jobs and a Python worker can process them.

## 88: What is the attemptsMade property?

It is the number of times the job has been tried and failed (or completed). It starts at 0. In a retry it tells you which attempt this is. There is also `attemptsStarted`, which counts how many times the job was moved to active, including stalls.

## 89: What info does a job keep about time?

- `job.timestamp`: when it was created.
- `job.processedOn`: when a worker started it.
- `job.finishedOn`: when it completed or failed.
- `job.delay`: its delay in milliseconds.

You can use these to measure wait time and processing time.

## 90: How do you update a job's data while it is waiting?

```js
const job = await queue.getJob(id);
await job.updateData({ ...job.data, email: "new@example.com" });
```

This replaces the data. It is also handy inside a processor to save progress between steps.

## 91: What does job.failedReason contain?

The error message from the last failure. `job.stacktrace` contains the stack traces from failed attempts (limited by the `stackTraceLimit` option). You can see both in dashboards or read them from the job.

## 92: What does the drained event mean?

A worker emits `drained` when the queue has no more waiting jobs for it to take. It doesn't mean all jobs are finished; active jobs may still be running. It is useful in tests or simple scripts.

## 93: What is the completed event payload in QueueEvents?

An object with `jobId` and `returnvalue`. The `failed` event has `jobId` and `failedReason`. The `progress` event has `jobId` and `data`.

```js
events.on("failed", ({ jobId, failedReason }) => {
  console.log(`Job ${jobId} failed: ${failedReason}`);
});
```

## 94: How do you wait for a job to finish from the producer?

Use `job.waitUntilFinished(queueEvents)`. It resolves with the return value, or rejects if the job fails. You can pass a timeout in milliseconds as a second argument.

```js
const events = new QueueEvents("pdf", { connection });
const job = await queue.add("make", { id: 1 });
const result = await job.waitUntilFinished(events, 30_000);
```

## 95: Should an HTTP request wait for a job to finish?

Usually not. The point of a queue is to return fast and do the work in the background. Return a job ID and let the client poll or get a webhook or WebSocket message later. Waiting is OK only for short jobs where you want to limit how many run at once.

## 96: What is the autorun option on a worker?

By default (`autorun: true`) a worker starts taking jobs as soon as it is created. With `autorun: false` it waits until you call `worker.run()`. This helps when you need to set up things like event listeners or a database connection first.

```js
const worker = new Worker("email", processor, { connection, autorun: false });
await connectDb();
worker.run();
```

## 97: What is the difference between job.remove and queue.drain?

`job.remove()` removes one specific job. `queue.drain()` removes all waiting (and optionally delayed) jobs. Neither affects active jobs.

## 98: What happens to jobs if Redis restarts?

It depends on Redis persistence. With AOF or RDB snapshots enabled, jobs survive the restart, though you can lose the last few writes, depending on the settings. Without persistence, all jobs are lost. Workers and queues reconnect on their own.

## 99: What is a dashboard for BullMQ?

A web UI to look at queues and jobs: counts, failed jobs, data, logs and errors, with buttons to retry or remove jobs. Popular choices are the open source Bull Board and the hosted Taskforce.sh.

## 100: How do you add Bull Board to an Express app?

```js
import express from "express";
import { createBullBoard } from "@bull-board/api";
import { BullMQAdapter } from "@bull-board/api/bullMQAdapter";
import { ExpressAdapter } from "@bull-board/express";

const serverAdapter = new ExpressAdapter();
serverAdapter.setBasePath("/admin/queues");

createBullBoard({
  queues: [new BullMQAdapter(emailQueue)],
  serverAdapter,
});

const app = express();
app.use("/admin/queues", serverAdapter.getRouter());
```

Put it behind authentication, because it can remove and retry jobs.

## 101: What kind of tasks fit well in a BullMQ queue?

Work that is slow, can fail and be retried, or doesn't need to finish before you answer the user. Examples: emails and SMS, image and video processing, PDF generation, webhooks to other systems, data imports, search index updates and scheduled cleanups.

## 102: What kind of tasks don't fit well in a queue?

Work that has to finish before you can answer the user, like checking a password. Also very small and fast tasks, where the queue overhead is bigger than the work itself. And huge payloads, such as storing whole files in job data; store the file somewhere else and put a reference in the job.

## 103: Is job data stored as JSON?

Yes. `queue.add` calls `JSON.stringify` on the data. So `Date` objects become strings, `Map`, `Set` and class instances lose their type, and functions are dropped. Pass plain objects and convert types back in the worker.

## 104: Can you put a Buffer or file into job data?

You can, but you shouldn't. A Buffer becomes a large JSON object and fills memory in Redis. Upload the file to storage like S3 and pass only the key or URL in the job.

## 105: How does a worker know which queue to listen to?

By the queue name you pass as the first argument, plus the prefix and connection. The `Queue` and `Worker` must use the same name, prefix and Redis database, or the worker will never see the jobs.

## 106: Do you need to create a Queue instance before a Worker can process jobs?

No. A worker only needs the queue name and connection. The `Queue` instance is used by the code that adds jobs. A process that only runs workers doesn't need a `Queue` at all.

## 107: What was QueueScheduler?

In BullMQ 1.x you had to run a `QueueScheduler` to handle delayed jobs and stalled job checks. Since v2 this work is done by the workers, and the class was removed. You will still see it in old tutorials.

## 108: How do you run a worker as a separate process?

Put the worker in its own file and start it with Node, for example `node worker.js`. In production you run it with a process manager like PM2, systemd, Docker or Kubernetes, separately from the web server.

```js
// worker.js
import { Worker } from "bullmq";

const worker = new Worker("email", async (job) => send(job.data), {
  connection: { host: process.env.REDIS_HOST, port: 6379 },
});
```

## 109: How do you shut down a worker cleanly?

Listen for `SIGTERM` and `SIGINT` and call `worker.close()`. It waits for active jobs to finish, so they are not left half done.

```js
const shutdown = async () => {
  await worker.close();
  process.exit(0);
};
process.on("SIGTERM", shutdown);
process.on("SIGINT", shutdown);
```

## 110: What is the job progress value type?

It can be a number or an object. A number like 0 to 100 is common, but you can store something like `{ step: 'upload', done: 3, total: 10 }`. It is saved with the job, so you can read it later from `job.progress`.

## 111: How do you see the latest progress of a job from another process?

Load the job and read `job.progress`, or listen to the `progress` event in `QueueEvents`.

```js
events.on("progress", ({ jobId, data }) => {
  console.log(jobId, data);
});
```

## 112: What is the difference between job.data and job.opts?

`job.data` is your payload, the input for the work. `job.opts` holds the options the job was added with, like `attempts`, `delay`, `priority` and `backoff`. The processor usually reads `data`, while `opts` controls how BullMQ handles the job.

## 113: How do you skip retries for a specific error?

Throw an `UnrecoverableError`. BullMQ moves the job straight to failed, even if it has attempts left.

```js
import { UnrecoverableError } from "bullmq";

new Worker(
  "charge",
  async (job) => {
    if (!job.data.cardId) {
      throw new UnrecoverableError("Missing card");
    }
  },
  { connection },
);
```

## 114: What replaced job.discard?

`UnrecoverableError`. `job.discard()` was removed from the Node.js API in v6. Throwing `UnrecoverableError` from the processor does the same thing: the job fails and is not retried.

## 115: What does the active event mean?

A worker emits `active` when it starts processing a job. `QueueEvents` also has an `active` event with the `jobId` and the previous state. You can use it to log start times or update a UI.

## 116: What does the waiting event in QueueEvents tell you?

It fires when a job is added to waiting, either as a new job or when a delayed or retried job is moved back. The payload has the `jobId`. It is useful for metrics or to notify other services that work is pending.

## 117: Can a job belong to two queues?

No. Each job lives in exactly one queue. If the same work must happen in two places, add two jobs, or use a flow where one parent has children in different queues.

## 118: Can you change a job's priority after it was added?

Yes, with `job.changePriority`. You can also switch `lifo` with it.

```js
await job.changePriority({ priority: 1 });
```

## 119: How do you know how many workers are connected to a queue?

```js
const workers = await queue.getWorkers();
const count = await queue.getWorkersCount();
```

This uses the Redis client list, and you can give workers a `name` option to make them easier to spot. Some managed Redis services disable the `CLIENT LIST` command, so this may not work there.

## 120: What does the worker name option do?

It sets a name for the worker's Redis connection. The name shows in `queue.getWorkers()` and in dashboards, so you can tell which machine or service a worker is running on.

```js
new Worker("email", processor, {
  connection,
  name: `email-${process.env.HOSTNAME}`,
});
```

## 121: Can you add jobs to a paused queue?

Yes. Adding works as usual, but no worker picks up the jobs until you call `queue.resume()`. This is useful during deploys or maintenance.

## 122: What is the deduplication option?

It stops the same job from being added again while one with the same deduplication ID is still in the queue. The repeated job is ignored and a `deduplicated` event is sent. This replaced the old `debounce` option, which was removed in v6.

```js
await queue.add(
  "sync-user",
  { userId: 5 },
  {
    deduplication: { id: "sync-user-5" },
  },
);
```

## 123: What is the difference between jobId and deduplication?

A custom `jobId` blocks duplicates for as long as the job exists, including after it is completed (until it is removed). Deduplication blocks duplicates only while the job is not finished, or for a set `ttl`. After that, the same ID can be added again as a new job.

## 124: What does the deduplication ttl do?

It sets a time window in milliseconds. During that window, jobs with the same deduplication ID are ignored, even if the first job already finished. This is called throttle mode.

```js
await queue.add("notify", data, {
  deduplication: { id: "notify-42", ttl: 5000 },
});
```

## 125: Where are failed jobs kept?

In the queue's `failed` set in Redis, with their error and stack trace. They stay there until you retry them, remove them, or they are cleaned by `removeOnFail` or `queue.clean`. By default failed jobs are kept forever, which is good for debugging but uses memory.

## 126: Can a job be processed twice?

Yes, in some cases. If a worker crashes or stalls after doing some of the work, the job is moved back and another worker runs it again. BullMQ gives "at least once" processing, so processors should be safe to run more than once (idempotent).

## 127: What does idempotent mean for a job?

Running the job twice gives the same result as running it once. For example, "set user status to active" is idempotent, but "add 10 credits" is not. You can make a job idempotent by checking a unique key in your database before doing the work.

## 128: How do you test a BullMQ worker locally?

Run Redis locally with Docker, add a job and wait for it with `waitUntilFinished`. You can also unit test the processor function by itself, passing a fake job object, without Redis at all.

```bash
docker run -p 6379:6379 redis:7
```

## 129: How do you unit test a processor without Redis?

Keep the processor as a plain exported function and call it with a fake job.

```js
// processor.js
export async function processEmail(job) {
  return { to: job.data.to, ok: true };
}

// processor.test.js
const result = await processEmail({
  data: { to: "a@x.com" },
  updateProgress: async () => {},
});
```

## 130: What is a job's returnvalue used for?

It stores the result of the job so other code can use it later. A parent job in a flow reads its children's return values. A producer can wait for it. Keep it small, because it is stored in Redis with the job.

## 131: What happens if the processor returns undefined?

The job completes with no return value. That is fine for jobs that only do side effects, like sending an email.

## 132: Can you use BullMQ with NestJS?

Yes. The `@nestjs/bullmq` package gives you modules and decorators: `BullModule.forRoot`, `BullModule.registerQueue`, `@InjectQueue` to add jobs and `@Processor` with a class that extends `WorkerHost` to process them.

```ts
@Processor("email")
export class EmailProcessor extends WorkerHost {
  async process(job: Job) {
    return this.mailer.send(job.data);
  }
}
```

## 133: How do you add a job from a NestJS service?

```ts
@Injectable()
export class UsersService {
  constructor(@InjectQueue("email") private emailQueue: Queue) {}

  async register(user) {
    await this.emailQueue.add("welcome", { to: user.email });
  }
}
```

The queue must be registered with `BullModule.registerQueue({ name: 'email' })` in the module.

## 134: Can you use BullMQ with Express?

Yes. BullMQ doesn't depend on any framework. Create the `Queue` once at startup, add jobs inside route handlers, and run workers in a separate process.

```js
app.post("/signup", async (req, res) => {
  const user = await createUser(req.body);
  await emailQueue.add("welcome", { to: user.email });
  res.status(201).json(user);
});
```

## 135: Should you create a new Queue for every request?

No. Each `Queue` opens a Redis connection. Create it once and reuse it for the life of the process. Creating one per request leaks connections and slows things down.

## 136: Can you use Redis Cluster with BullMQ?

Yes, but all keys of a queue must land on the same hash slot, because the Lua scripts use many keys at once. You do that by putting the prefix in curly braces, for example `prefix: '{myapp}'`.

## 137: Does BullMQ work with Valkey or Dragonfly?

Yes. Valkey is a Redis fork and works like Redis. Dragonfly also supports BullMQ, but it needs some special server settings; check the Dragonfly docs before using it.

## 138: What are the main parts of BullMQ's architecture?

Producers add jobs to Redis through `Queue`. Workers take jobs with blocking commands, lock them, run them and move them to completed or failed. Everything that changes state runs in Lua scripts inside Redis, so it is atomic. Events are written to a Redis stream and read by `QueueEvents`.

## 139: Why does BullMQ use Lua scripts?

A job move like "take from waiting, put in active, set a lock" changes several keys. Lua scripts run inside Redis as one atomic step, so no other client can see a half-done state, and it needs only one network round trip.

## 140: What happens if you add a job with an existing custom jobId?

Nothing is added. `queue.add` returns the existing job, and a `duplicated` event is sent. This is true even if the old job is completed, as long as it is still stored.

## 141: What is the stalled event?

It fires when BullMQ finds a job whose lock expired. The job is moved back to waiting (or failed, if it stalled too many times). Many stalled jobs usually mean your processor blocks the event loop or your workers are crashing.

## 142: What is the difference between failed and stalled?

Failed means the processor threw an error or the job ran out of attempts. Stalled means the worker stopped renewing the lock, so BullMQ doesn't know what happened. A stalled job is usually retried without counting as a normal failed attempt, until it hits `maxStalledCount`.

## 143: How do you see why a job failed?

Read `job.failedReason` and `job.stacktrace`, check the logs you added with `job.log`, or look at the job in Bull Board. Listening to the `failed` event and sending it to your logging tool helps you catch problems early.

## 144: What is the job.opts.attempts default?

1. The job runs once, and if it fails it goes straight to failed. Set `attempts` (on the job or in `defaultJobOptions`) to get retries.

## 145: Can a worker process jobs of different names?

Yes. A worker processes every job in its queue, whatever the name. You usually branch on `job.name`, or use a map of handlers.

```js
const handlers = { welcome: sendWelcome, reset: sendReset };
new Worker("email", (job) => handlers[job.name](job.data), { connection });
```

## 146: Should you use one queue for everything or many queues?

Use separate queues for different kinds of work, such as `email`, `images` and `reports`. Then you can scale workers, set concurrency and rate limits, and watch each kind of work on its own. A slow image job then doesn't hold up emails.

## 147: How do you start BullMQ with Docker Compose?

```yaml
services:
  redis:
    image: redis:7
    command:
      [
        "redis-server",
        "--maxmemory-policy",
        "noeviction",
        "--appendonly",
        "yes",
      ]
  worker:
    build: .
    command: node worker.js
    environment:
      REDIS_HOST: redis
```

This runs Redis with the settings BullMQ needs and a separate worker container.

## 148: What does queue.getJobLogs return?

An object with the `logs` array and the total `count` of log lines for the job. You can pass a start and end index to page through long logs.

```js
const { logs, count } = await queue.getJobLogs(jobId, 0, 50);
```

## 149: Can you process jobs in the same process that adds them?

Yes, it works, and it is fine for small apps or local development. In production it's usually better to split them, so heavy jobs don't slow down the web server and you can scale each side on its own.

## 150: What is a good first step when jobs are not being processed?

Check that a worker is running and connected to the same Redis, database and prefix, and with the same queue name. Then check that the queue isn't paused, that the worker isn't rate limited, and that jobs are not stuck in delayed. `queue.getJobCounts()` and a dashboard make this fast.

# Moderate Questions (151-300)

## 151: How do you write a custom backoff strategy?

Set `backoff: { type: 'custom' }` (any name you like) on the job, and add a `backoffStrategy` function in the worker `settings`. It gets the attempts made, the type, the error and the job, and returns the delay in milliseconds.

```js
new Worker("api", processor, {
  connection,
  settings: {
    backoffStrategy: (attemptsMade, type, err, job) => {
      if (err?.status === 429) return 60_000;
      return attemptsMade * 2000;
    },
  },
});

await queue.add("call", data, { attempts: 5, backoff: { type: "custom" } });
```

## 152: What can a custom backoff strategy return besides a delay?

Returning `0` retries the job right away. Returning `-1` stops retrying and moves the job to failed. This lets you decide per error whether a retry makes sense.

## 153: How do you retry a job after a time chosen inside the processor?

Move the job to delayed and throw `DelayedError`. The job will run again later, and it doesn't count as a failed attempt.

```js
import { DelayedError } from "bullmq";

new Worker(
  "poll",
  async (job, token) => {
    const ready = await checkExport(job.data.exportId);
    if (!ready) {
      await job.moveToDelayed(Date.now() + 30_000, token);
      throw new DelayedError();
    }
    return download(job.data.exportId);
  },
  { connection },
);
```

## 154: Why do you need to throw DelayedError after moveToDelayed?

`moveToDelayed` changes the job's state in Redis, but the worker still thinks the job is running. Throwing `DelayedError` tells the worker to stop handling it and not mark it completed or failed.

## 155: What is the token argument in the processor?

It is the lock token for this run of the job. Methods that move the job by hand, like `moveToDelayed`, `moveToWaitingChildren`, `moveToCompleted` or `extendLock`, need it to prove the worker still owns the lock.

## 156: How do you build a job that runs in several steps?

Store the current step in the job data and update it with `updateData`. If the job is retried, it continues from the saved step instead of starting over.

```js
new Worker(
  "order",
  async (job) => {
    let step = job.data.step ?? "charge";
    if (step === "charge") {
      await charge(job.data.orderId);
      step = "ship";
      await job.updateData({ ...job.data, step });
    }
    if (step === "ship") {
      await ship(job.data.orderId);
    }
  },
  { connection },
);
```

## 157: How do you rate limit by a value the API gives you?

When the API says "try again in N ms", call `worker.rateLimit(N)` and throw `Worker.RateLimitError()`. The job goes back to waiting, and the whole queue pauses for that time.

```js
const worker = new Worker(
  "api",
  async (job) => {
    const res = await callApi(job.data);
    if (res.status === 429) {
      await worker.rateLimit(Number(res.headers["retry-after"]) * 1000);
      throw Worker.RateLimitError();
    }
    return res.body;
  },
  { connection, limiter: { max: 50, duration: 1000 } },
);
```

## 158: Why must the limiter option be set to use manual rate limiting?

The worker only checks the rate limit state when `limiter` is configured. Without it, `worker.rateLimit()` sets the key, but the worker won't check it before taking the next job.

## 159: How do you check if a queue is rate limited?

```js
const ttl = await queue.getRateLimitTtl();
if (ttl > 0) console.log(`Rate limited for ${ttl} ms`);
```

To clear the limit early, use `queue.removeRateLimitKey()`.

## 160: What is global concurrency?

It is a limit on how many jobs can be active at once in the whole queue, across all workers. Each worker's `concurrency` still applies, but the total never goes above the global value.

```js
await queue.setGlobalConcurrency(4);
await queue.getGlobalConcurrency();
await queue.removeGlobalConcurrency();
```

## 161: What is the global rate limit on a queue?

It is a rate limit stored on the queue itself, so it applies to all workers without each worker setting a `limiter`. A worker's own limiter doesn't override it.

```js
await queue.setGlobalRateLimit(100, 1000); // 100 jobs per second
const { max, duration } = await queue.getGlobalRateLimit();
await queue.removeGlobalRateLimit();
```

## 162: What is the difference between concurrency and rate limiting?

Concurrency limits how many jobs run at the same time. Rate limiting limits how many jobs start in a time window. With concurrency 10, if each job takes 100 ms, you could do 100 jobs per second. A rate limit of 20 per second would cap that at 20, no matter how fast jobs are.

## 163: How do you change a worker's concurrency at runtime?

Set the `concurrency` property. It takes effect for the next jobs the worker picks up.

```js
worker.concurrency = 50;
```

## 164: How do you choose the concurrency value?

For I/O-bound jobs (API calls, database queries), start with something like 10 to 50 and measure. Watch CPU, memory, event loop lag and the limits of the services you call. For CPU-bound jobs, keep concurrency low and use sandboxed processors or more processes, about one per CPU core.

## 165: When should you use sandboxed processors?

When jobs do heavy CPU work (image processing, PDF rendering, parsing large files), when they might crash the process, or when you want to isolate memory leaks. For normal I/O jobs, a regular in-process function is faster, because there is no cost of passing data between processes.

## 166: What are the downsides of sandboxed processors?

Job data and results must be serialized between processes, which adds overhead. Each child process uses its own memory. You can't share in-memory things like a database pool with the main process. Debugging is a bit harder too.

## 167: What can a sandboxed processor do with the job object?

It gets a wrapped job that supports the common methods, such as `updateProgress`, `log`, `updateData` and reading `data`, `name`, `id` and `opts`. The calls are sent to the parent process, which runs them against Redis.

## 168: How do you add a job to a flow child queue with different options?

Each node in a flow can have its own `opts`, like `attempts`, `priority` or `delay`.

```js
await flow.add({
  name: "parent",
  queueName: "main",
  children: [
    { name: "child", queueName: "fetch", data: {}, opts: { attempts: 3 } },
  ],
});
```

## 169: What happens to the parent if a child fails?

By default the parent stays in `waiting-children` forever, because not all children completed. You choose other behavior with child options such as `failParentOnFailure`, `ignoreDependencyOnFailure` or `removeDependencyOnFailure`.

## 170: What does failParentOnFailure do?

If the child fails (after all its attempts), the parent fails too. This spreads up the tree, so one failure can fail the whole flow. Use it when the parent makes no sense without that child.

```js
{ name: 'fetch', queueName: 'fetch', data, opts: { failParentOnFailure: true } }
```

## 171: What does ignoreDependencyOnFailure do?

If the child fails, the parent continues as if the child was done. The failure is recorded, and the parent can read it with `job.getIgnoredChildrenFailures()`. Use it when some children are optional.

## 172: What does removeDependencyOnFailure do?

If the child fails, it is removed from the parent's list of dependencies, and the parent continues. Unlike `ignoreDependencyOnFailure`, the failure isn't kept on the parent.

## 173: How do you get the whole tree of a flow?

```js
const tree = await flow.getFlow({ id: parentJobId, queueName: "reports" });
console.log(tree.job.id, tree.children?.length);
```

You can pass `depth` and `maxChildren` to limit how much is loaded for big flows.

## 174: How do you add a child to an existing parent?

Use the `parent` option when adding the job. `queue` is the parent's full queue key, which is the prefix plus the queue name.

```js
await childQueue.add("extra", data, {
  parent: { id: parentJob.id, queue: "bull:reports" },
});
```

The parent must still be waiting for children for this to make sense.

## 175: How do you add many flows at once?

Use `flow.addBulk([...])`. All flows are added in one atomic call, so either all of them are created or none.

## 176: How do you build a parent that adds children while it runs?

Add the children with the `parent` option, then move the parent to `waiting-children` and throw `WaitingChildrenError`. When the children finish, the parent runs again, and you use a step in its data to know where to continue.

```js
import { WaitingChildrenError } from "bullmq";

new Worker(
  "batch",
  async (job, token) => {
    if (job.data.step !== "collect") {
      for (const id of job.data.ids) {
        await itemQueue.add(
          "item",
          { id },
          { parent: { id: job.id, queue: job.queueQualifiedName } },
        );
      }
      await job.updateData({ ...job.data, step: "collect" });
      const waiting = await job.moveToWaitingChildren(token);
      if (waiting) throw new WaitingChildrenError();
    }
    return job.getChildrenValues();
  },
  { connection },
);
```

## 177: What does moveToWaitingChildren return?

`true` if the job has pending children and was moved to `waiting-children`. `false` if all children are already done, so the job can continue right away instead of throwing.

## 178: How do you track job progress in a frontend?

Listen to `QueueEvents` in your backend and send updates to the browser through WebSockets or Server-Sent Events. Send only events for the jobs the user cares about, filtered by job ID.

```js
events.on("progress", ({ jobId, data }) => {
  io.to(`job:${jobId}`).emit("progress", data);
});
```

## 179: How do you count completed and failed jobs over time?

Turn on metrics in the worker and read them from the queue.

```js
import { MetricsTime } from "bullmq";

new Worker("email", processor, {
  connection,
  metrics: { maxDataPoints: MetricsTime.ONE_WEEK * 2 },
});

const metrics = await queue.getMetrics("completed");
```

Metrics are stored per minute, so you can see throughput without your own counters.

## 180: How do you keep Redis memory under control?

Set `removeOnComplete` and `removeOnFail` with a count or age, keep job data and return values small, limit `keepLogs` and `stackTraceLimit`, and limit the events stream length. Monitor Redis memory and set alerts. Never use an eviction policy as a fix.

## 181: How do you limit the size of the events stream?

Set `streams.events.maxLen` on the `Queue`. The default is about 10,000 events. You can also trim it with `queue.trimEvents(maxLength)`.

```js
new Queue("email", { connection, streams: { events: { maxLen: 1000 } } });
```

## 182: What does keepLogs do?

It limits how many log lines are kept per job. Without it, a job that logs a lot can use a lot of memory.

```js
await queue.add("import", data, { keepLogs: 100 });
```

## 183: How do you process a job manually without a processor function?

Create a worker with `null` as the processor, get a job with `getNextJob` and finish it yourself with `moveToCompleted` or `moveToFailed`.

```js
const worker = new Worker("manual", null, { connection });
const token = "my-token";
const job = await worker.getNextJob(token);
if (job) {
  try {
    await job.moveToCompleted({ ok: true }, token, false);
  } catch (err) {
    await job.moveToFailed(err, token, false);
  }
}
```

## 184: When would you use manual job processing?

When the processing doesn't fit a single function call, for example when you pull jobs in your own loop, batch them, or hand them to a system that isn't Node.js. With manual processing you must also take care of lock renewal and stalled job checks.

## 185: How do you extend a job's lock when processing manually?

Call `job.extendLock(token, duration)` before the lock expires. In normal workers this happens on its own.

```js
const timer = setInterval(() => job.extendLock(token, 30_000), 15_000);
```

## 186: How does BullMQ handle delayed jobs internally?

Delayed jobs sit in a sorted set with their run time as the score. Workers check for due jobs and move them to waiting atomically. There is no separate scheduler process, so you need at least one worker running for delayed jobs to move.

## 187: Why might a delayed job run later than its delay?

Delays are a minimum, not an exact time. The job only starts when it has moved to waiting and a worker is free. If workers are busy, rate limited, paused or not running, it waits longer.

## 188: What is a deduplication debounce mode?

You combine `delay`, `ttl`, `extend: true` and `replace: true`. Each new job with the same ID replaces the pending job's data and resets the timer, so only the last one runs after things go quiet. This is good for "save after the user stops typing" type of work.

```js
await queue.add(
  "save-draft",
  { text },
  {
    delay: 5000,
    deduplication: {
      id: `draft-${docId}`,
      ttl: 5000,
      extend: true,
      replace: true,
    },
  },
);
```

## 189: What does keepLastIfActive do in deduplication?

If a matching job is already active, BullMQ saves the newest data and creates one follow-up job when the active one finishes. The `ttl` is ignored. It is useful for things like deploys, where you want the latest version to run once more but not queue up many copies.

## 190: How do you clear a deduplication key early?

```js
await queue.removeDeduplicationKey("sync-user-5");
// or from the job that set it
await job.removeDeduplicationKey();
```

The job-level version only removes the key if this job caused the deduplication.

## 191: How do you find which job holds a deduplication ID?

```js
const jobId = await queue.getDeduplicationJobId("sync-user-5");
```

## 192: How do you listen to deduplicated jobs?

```js
events.on("deduplicated", ({ jobId, deduplicationId, deduplicatedJobId }) => {
  console.log(`${deduplicatedJobId} skipped, ${jobId} already exists`);
});
```

## 193: What replaced the debounce option?

The `deduplication` option. In v6 `debounce`, `job.debounceId` and the `debounced` event were removed. Use `deduplication`, `job.deduplicationId` and the `deduplicated` event.

## 194: How do you retry all failed jobs after fixing a bug?

```js
await queue.retryJobs({ state: "failed", count: 1000 });
```

It moves failed jobs back to waiting in batches. You can also retry completed jobs with `state: 'completed'` if you need to run them again.

## 195: How do you promote all delayed jobs?

```js
await queue.promoteJobs({ count: 1000 });
```

Useful after an outage, when you don't want to wait for retry delays to pass.

## 196: How do you get a list of jobs page by page?

`getJobs` takes start and end indexes and an `asc` flag.

```js
const page = 2;
const size = 20;
const jobs = await queue.getJobs(
  ["completed"],
  page * size,
  page * size + size - 1,
  false,
);
```

## 197: How do you pass different job options per job name?

Set common options in `defaultJobOptions` and override them in each `add` call. If you have many job types, keep a small map of options per name in your code.

```js
const opts = {
  welcome: { attempts: 3 },
  invoice: { attempts: 10, backoff: { type: "exponential", delay: 5000 } },
};
await queue.add("invoice", data, opts.invoice);
```

## 198: How do you set up BullMQ in NestJS with a shared connection?

```ts
@Module({
  imports: [
    BullModule.forRoot({ connection: { host: "localhost", port: 6379 } }),
    BullModule.registerQueue({ name: "email" }),
  ],
  providers: [EmailProcessor],
})
export class AppModule {}
```

All queues and processors registered in the app use the root connection unless you give them their own.

## 199: How do you listen to worker events in NestJS?

Use `@OnWorkerEvent` on methods of the processor class.

```ts
@Processor("email")
export class EmailProcessor extends WorkerHost {
  async process(job: Job) {}

  @OnWorkerEvent("failed")
  onFailed(job: Job, err: Error) {
    this.logger.error(`${job.id} failed: ${err.message}`);
  }
}
```

## 200: How do you set worker options like concurrency in NestJS?

Pass them as the second argument of `@Processor`.

```ts
@Processor("email", { concurrency: 10, limiter: { max: 100, duration: 1000 } })
export class EmailProcessor extends WorkerHost {}
```

## 201: How do you use the PostgreSQL backend?

Install `pg`, run the migrations once as a deploy step, and pass `createPostgresBackend` as the last constructor argument.

```js
import { Queue, Worker, createPostgresBackend } from "bullmq";

const connection = "postgres://user:pass@localhost:5432/app";

const queue = new Queue("email", { connection }, createPostgresBackend);
const worker = new Worker(
  "email",
  processor,
  { connection },
  createPostgresBackend,
);
```

## 202: How do you run the PostgreSQL migrations?

BullMQ doesn't run them on its own. Call `runMigrations` with a client from a `pg` pool, usually in a deploy script.

```js
import pg from "pg";
import { runMigrations } from "bullmq";

const pool = new pg.Pool({ connectionString: process.env.DATABASE_URL });
const client = await pool.connect();
try {
  await runMigrations(client);
} finally {
  client.release();
  await pool.end();
}
```

Running it again is safe, and parallel runs are serialized with an advisory lock.

## 203: How do you make PostgreSQL the default backend for all classes?

```js
import { setDefaultBackendFactory, createPostgresBackend } from "bullmq";

setDefaultBackendFactory(createPostgresBackend);
```

After this, `new Queue(...)` and `new Worker(...)` use PostgreSQL without passing the factory each time. For better TypeScript types, you can use `withBackend(createPostgresBackend)`, which returns `Queue`, `Worker` and other classes bound to that backend.

## 204: When would you choose PostgreSQL over Redis as the backend?

When you already run PostgreSQL and don't want to run Redis just for queues, when job volume is moderate, or when you want jobs stored in the same durable database as your data. Redis is the better choice for high throughput. The docs say PostgreSQL is often 1.5 to 2 times slower for processing.

## 205: What should you watch out for with the PostgreSQL backend?

Redis-only features don't apply, such as the raw Redis client, Redis Cluster and `maxmemory-policy`. You need PostgreSQL 13 or newer. Connection count matters, so watch `max_connections`. If you pass your own `pg.Pool`, BullMQ doesn't close it, and the `schema` option doesn't apply; you set `search_path` yourself.

## 206: How do you get the raw Redis client in v6?

`queue.client` was removed in v6. Use the backend instead.

```js
const client = await queue.getBackend().client;
```

This only works when the backend is Redis.

## 207: What changed in BullMQ 6 that affects existing code?

- Legacy repeatable jobs (`repeat`, `getRepeatableJobs`, `removeRepeatableByKey`) were removed. Use job schedulers.
- `debounce` was removed. Use `deduplication`.
- `job.discard()` was removed. Throw `UnrecoverableError`.
- `worker.resume()` is now async.
- The `paused` job state was removed.
- `ioredis` is now an optional peer dependency.
- `queue.client`, `worker.blockingClient` and similar Redis properties were removed.

## 208: How do you migrate a repeatable job to a job scheduler?

Replace `queue.add(name, data, { repeat })` with `upsertJobScheduler` using a stable scheduler ID, and remove the old repeatable entries before upgrading.

```js
// v5
await queue.add("cleanup", {}, { repeat: { pattern: "0 * * * *" } });

// v6
await queue.upsertJobScheduler(
  "cleanup",
  { pattern: "0 0 * * * *" },
  { name: "cleanup" },
);
```

## 209: When does a job scheduler create the next job?

When the current job from that scheduler starts processing. There is always one delayed job waiting for its time. If workers are busy, jobs may run less often than the interval, but they won't pile up.

## 210: Can you choose the job ID for scheduler jobs?

No. BullMQ makes special IDs for them so it can avoid creating duplicates for the same time slot. Use the job name or the scheduler ID to tell them apart.

## 211: How do you update a job scheduler's data or options?

Call `upsertJobScheduler` again with the same ID and the new settings or template. The next jobs use the new values.

```js
await queue.upsertJobScheduler(
  "daily-report",
  { pattern: "0 0 4 * * *" },
  {
    name: "report",
    data: { type: "daily", format: "pdf" },
    opts: { attempts: 3 },
  },
);
```

## 212: How many fields does a BullMQ cron pattern have?

BullMQ uses the `cron-parser` format, which allows 5 fields or 6 fields with seconds first. For example `'0 15 3 * * *'` means 03:15:00 every day. Be careful to count fields, because `'*/5 * * * *'` and `'*/5 * * * * *'` mean every 5 minutes and every 5 seconds.

## 213: What happens if the same scheduler is upserted from many app instances?

Nothing bad. The upsert is atomic and keyed by the scheduler ID, so you still have one scheduler. This is why it's safe to call it on every startup.

## 214: How do you run a job once at a specific date and time?

Calculate the delay from now.

```js
const runAt = new Date("2026-12-24T18:00:00Z");
await queue.add("greeting", data, { delay: runAt.getTime() - Date.now() });
```

## 215: How do you cancel a scheduled one-time job?

Keep its job ID (or give it a custom `jobId`) and remove it before it runs.

```js
await queue.add("reminder", data, { delay, jobId: `reminder-${eventId}` });
// later
await queue.remove(`reminder-${eventId}`);
```

## 216: How do you handle a job that calls an external API that sometimes times out?

Set a timeout on the HTTP call, use `attempts` with exponential backoff, and make the call idempotent (for example with an idempotency key). Throw `UnrecoverableError` for errors that will never succeed, like 400 Bad Request.

```js
new Worker(
  "webhook",
  async (job) => {
    const res = await fetch(job.data.url, {
      method: "POST",
      body: JSON.stringify(job.data.body),
      signal: AbortSignal.timeout(10_000),
    });
    if (res.status >= 400 && res.status < 500)
      throw new UnrecoverableError(`HTTP ${res.status}`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
  },
  { connection },
);
```

## 217: Does BullMQ have a job timeout option?

Not in the open source version. Long jobs keep running as long as the worker renews the lock. Add a timeout in your own code, for example with `AbortSignal.timeout` for HTTP calls or `Promise.race`, and throw an error when it hits.

## 218: How do you send failed jobs to a dead letter queue?

BullMQ doesn't have a built-in dead letter queue, because failed jobs already stay in the `failed` set. If you want a separate queue, listen to `failed` and copy the job when it has no attempts left.

```js
worker.on("failed", async (job, err) => {
  if (job && job.attemptsMade >= (job.opts.attempts ?? 1)) {
    await deadQueue.add(job.name, { original: job.data, error: err.message });
  }
});
```

## 219: How do you know if a failed event is the final failure?

Compare `job.attemptsMade` with `job.opts.attempts`. If they are equal, there are no retries left. In `QueueEvents`, the `retries-exhausted` event tells you this directly.

## 220: How do you use job names for routing in a large worker?

Keep a map from name to handler, and fail clearly if the name is unknown.

```js
const handlers = {
  "user.created": onUserCreated,
  "order.paid": onOrderPaid,
};

new Worker(
  "events",
  async (job) => {
    const handler = handlers[job.name];
    if (!handler) throw new UnrecoverableError(`No handler for ${job.name}`);
    return handler(job.data, job);
  },
  { connection },
);
```

## 221: How do you type job names in TypeScript?

The third generic on `Queue` and `Worker` is the name type.

```ts
type Name = "welcome" | "reset";
const queue = new Queue<{ to: string }, void, Name>("email", { connection });
await queue.add("welcome", { to: "a@x.com" }); // ok
```

## 222: How do you share the Redis connection settings across files?

Put them in one module and import it. Pass the plain options object, so each `Queue`, `Worker` and `QueueEvents` can create the connections it needs.

```js
// connection.js
export const connection = {
  host: process.env.REDIS_HOST ?? "localhost",
  port: Number(process.env.REDIS_PORT ?? 6379),
  password: process.env.REDIS_PASSWORD,
};
```

## 223: What is enableOfflineQueue and why turn it off for producers?

By default ioredis queues commands while disconnected and sends them later. In an HTTP handler that means `queue.add` can hang until Redis is back. With `enableOfflineQueue: false` on the producer's connection, `add` fails fast so you can return an error or fall back.

```js
const queue = new Queue("email", {
  connection: { host: "redis", enableOfflineQueue: false },
});
```

## 224: Should a producer use maxRetriesPerRequest null?

Usually not. A producer in a web request should fail fast, so keep the default (20) or use a lower value. `null` is needed for workers, which should wait for Redis forever.

## 225: How do you handle Redis being down when adding a job?

Catch the error from `queue.add` and decide: return 503, write the job to a database outbox and add it later, or retry a few times. Don't let the request hang. Turning off `enableOfflineQueue` helps you get the error quickly.

## 226: What is the transactional outbox pattern with BullMQ?

You write the business change and an "outbox" row in the same database transaction. A separate process reads outbox rows and adds them as BullMQ jobs, then marks them as sent. This way you never save the order but lose the "send receipt" job because Redis was down at that moment.

## 227: How do you avoid adding a job before the database transaction commits?

Add the job after the commit, not inside the transaction. If the job is added first and the transaction rolls back, the worker will process data that doesn't exist. For full safety, use the outbox pattern.

## 228: How do you pass a large payload to a job?

Store it somewhere else (S3, a database row or a file) and pass the ID. The worker loads it. This keeps Redis small and fast and avoids hitting memory limits.

```js
const key = await uploadToS3(csvBuffer);
await queue.add("import", { s3Key: key });
```

## 229: What does the sizeLimit job option do?

It sets a max size in bytes for the job data. If the data is bigger, `add` throws. It helps catch code that accidentally puts large objects in jobs.

```js
await queue.add("event", payload, { sizeLimit: 64 * 1024 });
```

## 230: How do you get job counts for a dashboard quickly?

Use `getJobCounts()` once for all states instead of many separate calls. Cache it for a few seconds if many users load the dashboard.

## 231: How do you find jobs by their data, like all jobs for user 5?

BullMQ has no query by data. You can scan jobs with `getJobs` and filter in code, which is slow for big queues. A better way is to store the job ID in your own database next to the user, or use a custom `jobId` that contains the user ID.

## 232: How do you write integration tests for BullMQ?

Use a real Redis (Docker or Testcontainers), a unique queue name per test, and clean up with `obliterate` and `close`.

```js
let queue, worker, events;

beforeEach(() => {
  const name = `test-${Date.now()}`;
  queue = new Queue(name, { connection });
  events = new QueueEvents(name, { connection });
  worker = new Worker(name, async (job) => job.data.a + job.data.b, {
    connection,
  });
});

afterEach(async () => {
  await worker.close();
  await events.close();
  await queue.obliterate({ force: true });
  await queue.close();
});

test("adds numbers", async () => {
  const job = await queue.add("sum", { a: 1, b: 2 });
  expect(await job.waitUntilFinished(events)).toBe(3);
});
```

## 233: Why do tests with BullMQ sometimes hang?

Usually because a `Queue`, `Worker` or `QueueEvents` was not closed, so the Redis connection keeps Node.js alive. Close every instance in `afterEach` or `afterAll`. Another cause is `waitUntilFinished` without a timeout on a job that never finishes.

## 234: Why do you need waitUntilReady on QueueEvents in tests?

`QueueEvents` reads the stream from the moment it connects. If the job finishes before the listener is ready, you can miss the event. `await events.waitUntilReady()` before adding jobs avoids this race.

## 235: How do you mock BullMQ in unit tests?

Mock the `Queue` class or your own wrapper around it, and check that `add` was called with the right name, data and options. Test processors as plain functions. Leave real Redis for a smaller set of integration tests.

```js
const add = jest.fn();
const service = new UserService({ add });
await service.register({ email: "a@x.com" });
expect(add).toHaveBeenCalledWith("welcome", { to: "a@x.com" });
```

## 236: How do you log every job in a consistent way?

Wrap your processor in a function that logs the start, end and errors with the job ID, name and timing.

```js
const withLogging = (fn) => async (job, token) => {
  const start = Date.now();
  logger.info({ id: job.id, name: job.name }, "start");
  try {
    const result = await fn(job, token);
    logger.info({ id: job.id, ms: Date.now() - start }, "done");
    return result;
  } catch (err) {
    logger.error({ id: job.id, err }, "failed");
    throw err;
  }
};

new Worker("email", withLogging(sendEmail), { connection });
```

## 237: How do you add OpenTelemetry tracing to BullMQ?

Use the `bullmq-otel` package and pass it as the `telemetry` option to queues and workers. It creates spans for adding and processing jobs and passes the trace context through the job, so a request trace continues into the worker.

```js
import { BullMQOtel } from "bullmq-otel";

const telemetry = new BullMQOtel("my-app");
const queue = new Queue("email", { connection, telemetry });
const worker = new Worker("email", processor, { connection, telemetry });
```

## 238: What should you alert on for a BullMQ system?

- Waiting count growing for a long time (workers can't keep up).
- Failed jobs per minute above normal.
- Stalled events.
- Oldest waiting job age.
- No active workers on a queue.
- Redis memory, connections and errors.

## 239: How do you measure how long jobs wait before running?

Use `job.processedOn - job.timestamp` in the worker (for delayed jobs, subtract the delay too). Send it to your metrics system as a histogram per queue.

```js
worker.on("active", (job) => {
  metrics.observe(
    "queue_wait_ms",
    job.processedOn - job.timestamp - (job.delay ?? 0),
  );
});
```

## 240: How do you expose queue stats to Prometheus?

Run a small loop that calls `getJobCounts()` every few seconds and sets gauges, or use a ready-made exporter. Keep the interval reasonable so you don't load Redis too much.

```js
setInterval(async () => {
  const counts = await queue.getJobCounts();
  for (const [state, n] of Object.entries(counts)) {
    gauge.set({ queue: queue.name, state }, n);
  }
}, 15_000);
```

## 241: How do you run workers on Kubernetes?

Run workers as a separate Deployment from the web app. Set `terminationGracePeriodSeconds` longer than your longest job, and handle `SIGTERM` by calling `worker.close()`. Scale replicas by queue length, for example with KEDA, which has a Redis scaler.

## 242: How do you autoscale workers by queue length?

Read the waiting count (the `bull:<queue>:wait` list length, plus prioritized jobs) and add or remove worker replicas when it passes a threshold. KEDA, or a custom metric for the Horizontal Pod Autoscaler, can do this. Scale down slowly so active jobs can finish.

## 243: How do you run BullMQ workers on serverless platforms like AWS Lambda?

Workers are meant to run for a long time and keep connections open, which doesn't fit Lambda well. Adding jobs from Lambda is fine. For processing, use long-running containers (ECS, Kubernetes, Fly.io and similar), or manual processing with `getNextJob` in a scheduled function if you must.

## 244: How do you handle a job that needs a database connection?

Create the database pool once when the worker process starts and reuse it in every job. Don't open a new connection per job. Close the pool after `worker.close()` on shutdown. Make sure pool size fits your worker concurrency.

## 245: How do you make sure a job runs only once per day for a user?

Use a custom `jobId` that includes the user ID and date. A second add with the same ID is ignored.

```js
const day = new Date().toISOString().slice(0, 10);
await queue.add("digest", { userId }, { jobId: `digest-${userId}-${day}` });
```

Remember that `removeOnComplete` will free the ID again once the job is removed.

## 246: How do you process jobs in strict order?

Use one worker with `concurrency: 1`, or global concurrency of 1, and don't use priorities or delays that change the order. Retries can still break order, because a failed job goes to delayed while others continue. For order per customer, BullMQ Pro groups are a better fit.

## 247: Is BullMQ order guaranteed with many workers?

Jobs are taken in FIFO order, but with several workers or concurrency above 1 they run in parallel, so they can finish in any order. If job B depends on job A, use a flow or chain them instead of counting on order.

## 248: How do you chain jobs so one starts after another?

Either add the next job at the end of the processor, or use a flow where the later step is the parent. Flows run children first, so the job that should run last goes at the top.

```js
await flow.add({
  name: "publish",
  queueName: "video",
  children: [
    {
      name: "encode",
      queueName: "video",
      data: { id },
      children: [{ name: "upload", queueName: "video", data: { id } }],
    },
  ],
});
// order: upload -> encode -> publish
```

## 249: How do you handle jobs for a deleted entity?

Check in the processor if the entity still exists. If it doesn't, return early or throw `UnrecoverableError`, depending on whether you want it to show as failed. Don't retry jobs that can never succeed.

## 250: How do you use QueueEvents with many queues?

You need one `QueueEvents` instance per queue, and each uses its own blocking connection. For many queues, think about whether you really need global events for all of them, or whether worker events are enough.

## 251: What is the retries-exhausted event?

A `QueueEvents` event sent when a job has failed and has no attempts left. The payload includes the `jobId` and `attemptsMade`. It is a clean place to alert or move the job to your own dead letter storage.

## 252: How do you remove completed jobs but keep failed ones longer?

Set different values for the two options.

```js
const queue = new Queue("email", {
  connection,
  defaultJobOptions: {
    removeOnComplete: { count: 500 },
    removeOnFail: { age: 7 * 24 * 3600 },
  },
});
```

This keeps 500 completed jobs and failed jobs for 7 days.

## 253: Can you set removeOnComplete on the worker instead of the job?

Yes. The worker options `removeOnComplete` and `removeOnFail` apply to jobs it finishes, unless the job has its own value. This is handy when you don't control every place that adds jobs.

## 254: Is age in removeOnComplete in seconds or milliseconds?

Seconds. `{ age: 3600 }` keeps jobs for one hour. This is different from most other BullMQ options, such as `delay`, which are in milliseconds.

## 255: How do you show a user the position of their job in the queue?

There's no direct method. You can count jobs in waiting ahead of it, but that is slow for big queues and changes all the time. Most apps show a simple status (queued, processing, done) and progress instead of an exact position.

## 256: How do you cancel a job that is already running?

You can't remove an active job directly. A common way is to set a "cancelled" flag in your database or in Redis, have the processor check it between steps, and stop with an `UnrecoverableError` when it is set. Then the job ends as failed with a clear reason.

## 257: How do you handle long-running jobs?

Split them into smaller jobs or steps if you can. If not, make sure the event loop isn't blocked so the lock gets renewed, report progress, save progress with `updateData` so a retry can continue, and give the shutdown enough time to finish or stop cleanly.

## 258: Why do CPU-heavy jobs cause stalled jobs?

Lock renewal runs on a timer in the same event loop. If your processor does a long synchronous loop, the timer can't run, the lock expires, and BullMQ thinks the worker died. The job is then moved back and may run twice. Use sandboxed processors for this kind of work.

## 259: How do you fix many stalled jobs?

Find out why locks expire. Check for event loop blocking (long sync code, big JSON parsing), process crashes and restarts, memory issues, and network problems to Redis. Move CPU work to sandboxed processors and increase `lockDuration` if needed. Don't just raise `maxStalledCount`, because that hides the problem.

## 260: What does stalledInterval do?

It sets how often a worker checks for stalled jobs, in milliseconds. The default is 30 seconds. Only one worker does the check at a time. Lower values find stalled jobs sooner but add load to Redis.

## 261: How do you handle errors from a worker that aren't job errors?

Listen to the `error` event for things like connection problems. Also add `process.on('unhandledRejection')` and `process.on('uncaughtException')` handlers to log and exit, and let your process manager restart the worker.

## 262: Can a worker listen to more than one queue?

No. A `Worker` is bound to one queue. To process several queues in one process, create one worker per queue. They can share connection settings.

```js
const workers = ["email", "sms", "push"].map(
  (name) => new Worker(name, handlers[name], { connection }),
);
```

## 263: How do you pause all processing during a deploy?

Call `queue.pause()` before you stop the workers and `queue.resume()` after the new workers are up. Producers can keep adding jobs. For most rolling deploys you don't need this, because `worker.close()` already finishes active jobs.

## 264: How do you move a job from failed to delayed for a later retry?

There is no direct method for that. `job.retry()` moves the job to waiting, not delayed. If you need a delayed retry, read the failed job and add a new one with a `delay`, or call `retry()` later from a scheduled task. For automatic retries with waits, use `attempts` with `backoff`.

## 265: What is job.getDependencies used for?

It returns the processed and unprocessed children of a parent job. You can use it to show progress of a flow, for example "7 of 10 parts done".

```js
const { processed, unprocessed } = await parent.getDependencies();
```

There is also `getDependenciesCount()` if you only need numbers.

## 266: How do you read failed children of a parent?

`job.getFailedChildrenValues()` returns the failure reasons of children that failed, keyed by child job key. `job.getIgnoredChildrenFailures()` returns failures of children that had `ignoreDependencyOnFailure`.

## 267: Can flows have children in different Redis instances?

No. All queues in one flow must be on the same Redis (or the same backend). The parent and children are linked with keys that are updated in one script.

## 268: How deep can a flow be?

There is no fixed small limit, so you can nest many levels. But each level and child adds keys and work. Very large flows are slow to add and to load with `getFlow`, so use `depth` and `maxChildren` when reading them, and keep trees reasonable.

## 269: How do you add a flow where the parent has no work of its own?

Give the parent a processor that only collects child results, or just returns. The parent is still a job, so it needs a worker on its queue, or it will stay in waiting after the children are done.

## 270: How do you know when a whole flow is done?

When the top parent job completes. Listen for `completed` on that job's queue in `QueueEvents` and check the job ID, or call `waitUntilFinished` on the parent job returned by `flow.add`.

```js
const { job } = await flow.add(tree);
await job.waitUntilFinished(events);
```

## 271: How do you set default options for all jobs in a flow?

`flow.add` takes a second argument with `queuesOptions`, where you set `defaultJobOptions` per queue name.

```js
await flow.add(tree, {
  queuesOptions: {
    fetch: { defaultJobOptions: { attempts: 3 } },
  },
});
```

## 272: What happens if you remove a parent job?

Removing a parent also removes its children by default, so the whole subtree is cleaned up. Removing a child updates the parent's list of dependencies.

## 273: What is a common way to batch work with BullMQ open source?

Use a flow: one parent and many child jobs, each doing a small piece, with the parent combining the results. Or let each job process a fixed chunk, like 500 rows. BullMQ Pro has a real batches feature that gives a worker several jobs at once.

## 274: What are BullMQ Pro groups?

Groups let you split jobs in one queue by a group ID (for example a customer ID). Workers then rotate between groups, so one big customer can't block the others. You can also set concurrency and rate limits per group. This is a Pro feature.

## 275: How do you get fair processing per customer without BullMQ Pro?

Options include a separate queue per tier or per big customer, limiting how many jobs one customer can add at once, or using priorities so small customers aren't stuck behind a huge import. None of these is as clean as Pro groups, so pick based on how many customers you have.

## 276: How do you rate limit per customer without Pro groups?

There is no per-key limiter in open source BullMQ (the old `groupKey` option was removed in v3). You can do your own check in the processor with a Redis counter, and when the customer is over the limit, move the job to delayed and throw `DelayedError`.

## 277: How do you handle time zones and daylight saving time in schedulers?

Set `tz` to the user's or business's time zone. The cron library then handles DST changes. On the day of the change, a job set at a time that doesn't exist (like 02:30) may be skipped or shifted, so avoid times close to the change if it matters.

## 278: How do you limit how many times a scheduler runs?

Use the `limit` option in the repeat settings, or an `endDate`. After that, no more jobs are created.

```js
await queue.upsertJobScheduler("trial-reminder", {
  every: 24 * 3600 * 1000,
  limit: 7,
});
```

## 279: How do you start a scheduler at a later date?

Use `startDate` in the repeat options. Jobs start being created from that date.

```js
await queue.upsertJobScheduler("campaign", {
  pattern: "0 0 9 * * *",
  startDate: new Date("2027-01-01"),
});
```

## 280: How do you run a scheduler job right away and then on the interval?

With `every`, the first job runs right away by default. With a cron `pattern`, set `immediately: true` if you want the first run now instead of waiting for the next cron time.

## 281: What is job.parentKey?

The Redis key of the parent job, for example `bull:reports:42`. It is set on jobs that belong to a flow. You can use it to load or check the parent.

## 282: How do you check if a job is part of a flow?

Check `job.parent` or `job.parentKey`. If set, the job is a child. For parents, `getDependenciesCount()` returns how many children they have.

## 283: Can you add jobs from a worker to another queue?

Yes, and it's common. Create the other `Queue` once outside the processor, and add jobs from inside it. This is how you build pipelines.

```js
const notifyQueue = new Queue("notify", { connection });

new Worker(
  "orders",
  async (job) => {
    await processOrder(job.data);
    await notifyQueue.add("order-done", { orderId: job.data.orderId });
  },
  { connection },
);
```

## 284: What problem can happen when you add a job at the end of a processor?

If the processor adds the next job and then crashes before it finishes, the job is retried and adds the next job again. Make the add idempotent with a custom `jobId` or use deduplication, so retries don't create duplicates.

## 285: How do you set a prefix per environment?

Use an environment variable in the prefix, or use a different Redis database. This keeps staging and production jobs apart when they share a Redis server.

```js
const prefix = `bull-${process.env.NODE_ENV}`;
new Queue("email", { connection, prefix });
```

## 286: What happens if Queue and Worker use different prefixes?

They talk to different keys, so the worker never sees the jobs. Jobs just pile up in waiting. Always share the prefix in one config module.

## 287: How do you inspect BullMQ keys in Redis?

Use `redis-cli` with `SCAN` and a pattern like `bull:email:*`. Avoid `KEYS` in production because it blocks Redis. You can check types like `LLEN bull:email:wait` or `ZCARD bull:email:failed`.

```bash
redis-cli --scan --pattern 'bull:email:*' | head
redis-cli LLEN bull:email:wait
```

## 288: How do you migrate jobs from Bull to BullMQ?

There is no automatic migration, because the data formats differ. The usual way is to let the Bull queue drain while new jobs go to BullMQ, using a different queue name or prefix. Rewrite processors to the BullMQ API.

## 289: How do you add jobs from a Python service and process them in Node.js?

Use the official Python package with the same Redis, queue name and prefix. The Node.js worker sees the jobs like any other.

```python
from bullmq import Queue

queue = Queue("email", {"connection": "redis://localhost:6379"})
await queue.add("welcome", {"to": "a@x.com"})
```

## 290: How do you avoid hot keys and noisy neighbors in a shared Redis?

Give each app its own prefix or Redis database, set memory alerts, keep job data small, and clean finished jobs. If one queue has very high load, move it to its own Redis instance.

## 291: What is the difference between getJobs and getJobCounts in cost?

`getJobCounts` only reads the size of each set or list, which is cheap. `getJobs` loads each job's hash, which grows with the number of jobs you ask for. Use counts for dashboards and load jobs only page by page.

## 292: How do you write a worker that processes a CSV import?

Pass the file location in the job, stream the file, process rows in chunks, report progress and save the last processed row so a retry can continue.

```js
new Worker(
  "import",
  async (job) => {
    let done = job.data.done ?? 0;
    for await (const chunk of readCsvChunks(job.data.s3Key, {
      skip: done,
      size: 500,
    })) {
      await insertRows(chunk);
      done += chunk.length;
      await job.updateData({ ...job.data, done });
      await job.updateProgress(done);
    }
    return { rows: done };
  },
  { connection },
);
```

## 293: How do you send emails in bulk without being blocked by the provider?

Add one job per email with `addBulk` in chunks, set a worker `limiter` that matches your provider's rate, and use retries with backoff for 429 and 5xx responses. Use `UnrecoverableError` for bad addresses.

## 294: How do you process webhooks you received with BullMQ?

Save the webhook body, add a job and return 200 right away. The worker does the real work with retries. Use the provider's event ID as `jobId` to ignore duplicates, since many providers send the same webhook more than once.

```js
app.post("/webhooks/stripe", async (req, res) => {
  const event = verify(req);
  await queue.add(event.type, event, { jobId: event.id });
  res.sendStatus(200);
});
```

## 295: How do you send outgoing webhooks reliably?

Add a job per delivery with many attempts and exponential backoff, a timeout on the HTTP call, and a signature header. Log responses with `job.log`. After the last failure, mark the endpoint as failing in your database and notify the customer.

## 296: How do you test retry and backoff logic quickly?

Use small backoff delays in tests (like `delay: 10`) and a processor that fails the first N times by checking `job.attemptsMade`. Then wait for completion and check how many attempts were made.

```js
const worker = new Worker(
  name,
  async (job) => {
    if (job.attemptsMade < 2) throw new Error("fail");
    return "ok";
  },
  { connection },
);
```

## 297: What does worker.isRunning tell you?

Whether the worker's main loop is running and taking jobs. `worker.isPaused()` tells you whether it is paused. You can use them in a health check endpoint for the worker process.

## 298: How do you write a health check for a worker process?

Expose a small HTTP endpoint that checks `worker.isRunning()`, that Redis answers a ping, and maybe that the worker processed a job recently. Kubernetes can use it as a liveness probe.

```js
http
  .createServer(async (req, res) => {
    const ok = worker.isRunning() && !worker.closing;
    res.writeHead(ok ? 200 : 503).end();
  })
  .listen(8080);
```

## 299: What does the worker closing property mean?

When `close()` has been called, `worker.closing` holds the promise for the shutdown. It is set while the worker is closing, so you can check it to stop accepting new work in other parts of your code.

## 300: How do you upgrade BullMQ to a new major version safely?

Read the changelog for breaking changes, update the code in a branch, and test with real Redis. Upgrade workers and producers together, or make sure both versions work with the same data during the rollout. Drain or migrate jobs that use removed features, like legacy repeatable jobs in v6.

# Advanced Questions (301-450)

## 301: Which Redis data structures does BullMQ use for a queue?

- `wait`: a list of job IDs ready to run.
- `active`: a list of job IDs being processed.
- `delayed`, `prioritized`, `completed`, `failed`, `waiting-children`: sorted sets.
- Each job is a hash at `<prefix>:<queue>:<id>`, with a `:lock` key while active.
- `meta`: a hash with queue settings (paused flag, global concurrency and so on).
- `id`: a counter for job IDs.
- `events`: a Redis stream of events.
- `marker`: a sorted set used to wake up blocked workers.

## 302: How does a worker wait for jobs without polling?

It uses a blocking command (`BZPOPMIN` on the `marker` key) on its separate blocking connection. When a job is added or a delayed job becomes due, a marker is written and the worker wakes up. Then it runs a Lua script to move the job from wait to active. This keeps Redis load low when the queue is empty.

## 303: What is the marker key and why was it added?

The marker is a sorted set that tells workers "there is something to do now", with a score for when. Older versions used `BRPOPLPUSH` on the wait list, which didn't work well with delayed and prioritized jobs. The marker lets one blocking call cover waiting, prioritized and delayed jobs.

## 304: What happens step by step when a worker takes a job?

1. The worker blocks on the marker until there might be work.
2. A Lua script moves a job ID from `wait` (or `prioritized`) to `active`.
3. It sets the lock key with the worker's token and `lockDuration`.
4. It sets `processedOn`, increases `attemptsStarted` and writes an `active` event.
5. It returns the job data to the worker, which then runs the processor.

## 305: What happens step by step when a job completes?

The worker calls a Lua script that checks the lock token, removes the job from `active`, saves `returnvalue` and `finishedOn`, adds it to `completed` (or deletes it, based on `removeOnComplete`), updates the parent if there is one, writes a `completed` event and can fetch the next job in the same call.

## 306: Why does moveToCompleted fetch the next job?

To save a round trip. Finishing one job and taking the next happen in a single Lua script call. Under high load, this noticeably raises throughput.

## 307: How does lock renewal work in a worker?

The worker runs a timer that renews the locks of all its active jobs in one call, about every `lockDuration / 2` (`lockRenewTime`). If the renewal finds that a lock was lost, the worker emits an error for that job. Renewing in bulk avoids one Redis call per job.

## 308: How does the stalled job checker work?

On every `stalledInterval`, one worker (guarded by a short lock) runs a script. It looks at jobs that were marked as possibly stalled in the last check and still have no lock. Those are moved back to wait, or to failed if they passed `maxStalledCount`. Then it marks all current active jobs as candidates for the next check. So a stalled job is found within one or two intervals.

## 309: What is the difference between attemptsMade and attemptsStarted?

`attemptsStarted` goes up every time the job moves to active, even if it then stalls. `attemptsMade` goes up when an attempt ends with complete or fail. If `attemptsStarted` is much bigger than `attemptsMade`, the job is stalling a lot.

## 310: What is stalledCounter on a job?

It counts how many times the job was found stalled. When it passes `maxStalledCount`, the job is failed instead of moved back. It helps to find jobs that keep crashing workers, like a job with a payload that makes the process run out of memory.

## 311: What delivery guarantee does BullMQ give?

At least once. A job won't be lost while it's in Redis, but it can run more than once if a worker crashes or stalls after doing the work but before marking it completed. Exactly once isn't possible without making the side effects idempotent.

## 312: How do you make a job's side effects exactly-once in practice?

Make them idempotent. Use an idempotency key (like the job ID) when calling payment APIs, store "processed job IDs" in your database with a unique constraint in the same transaction as the work, or use upserts instead of inserts. Then a second run does nothing harmful.

```js
await db.query(
  "INSERT INTO processed_jobs (job_id) VALUES ($1) ON CONFLICT DO NOTHING RETURNING job_id",
  [job.id],
);
```

## 313: Why is the job ID not always a good idempotency key?

If you remove the job and add the same work again, it gets a new ID. Also, two different jobs can carry the same business action. A business key, like `charge-order-123`, is safer than the job ID. Use it as `jobId` or as the key you check in your database.

## 314: How does BullMQ keep queue operations atomic?

Every state change is done by a Lua script. Redis runs one script at a time, so nobody sees a half-moved job. With Redis Cluster, this only works if all keys are in one hash slot, which is why you need a hash tag in the prefix.

## 315: Why does Redis Cluster need a hash tag in the prefix?

In a cluster, keys are spread over slots by hash. A Lua script can only touch keys in the same slot. With `prefix: '{bull}'`, only the part in braces is hashed, so all keys of the queue go to one slot and the scripts work. A downside is that one queue can't be spread over many cluster nodes.

## 316: How do you spread load in Redis Cluster with BullMQ?

Use different hash tags for different queues, like `{email}` and `{images}`. Each queue lives on one node, but different queues can live on different nodes. Very hot single queues may need to be split into several queues by key.

## 317: What are the risks of running BullMQ on a Redis replica setup with failover?

Redis replication is async. On failover, the last writes may not have reached the replica, so a job that was just added or completed may roll back. You can see jobs run twice or disappear. Keep failover rare and make jobs idempotent, so a repeated run does no harm.

## 318: Which Redis persistence settings fit BullMQ?

Turn on AOF with `appendfsync everysec` for a good balance: at most about one second of writes is lost on a crash. RDB snapshots alone can lose minutes. `appendfsync always` is the safest but much slower. Managed services usually have a setting for this.

## 319: Why is maxmemory-policy noeviction required?

With an eviction policy like `allkeys-lru`, Redis deletes keys when memory is full. It might delete a job hash but leave its ID in the wait list, or delete a lock. That breaks the queue in strange ways. With `noeviction`, writes fail with an error, which you see and can fix.

## 320: What happens when Redis runs out of memory with noeviction?

Writes fail with an OOM error. `queue.add` throws, and workers can't move jobs, so they emit errors. Reads still work. You need to free memory (clean old jobs, raise the limit) to recover. Alerts on memory use should fire well before this point.

## 321: How do you estimate Redis memory for BullMQ?

Measure the size of a typical job hash (data, options, return value, logs, stack traces) with `MEMORY USAGE` on a real key. Multiply by how many jobs you keep (waiting plus active plus kept completed and failed), then add the events stream and some headroom.

```bash
redis-cli MEMORY USAGE bull:email:12345
```

## 322: Why can many workers on many queues use too many Redis connections?

Each worker needs at least two connections, each `QueueEvents` one, and each `Queue` one. With 50 queues, 20 pods and a few workers per pod, you quickly hit thousands. Share connections where you can by passing an ioredis instance (blocking connections are still separate), and use fewer `QueueEvents`.

## 323: Can you share one ioredis connection between many workers?

You can pass the same instance, and it is used for normal commands, but each worker still creates its own duplicate for blocking commands. So sharing saves some connections but not all. Never share a connection that is already used for blocking commands.

## 324: How do you design BullMQ for very high throughput?

- Run many workers with fair concurrency, across many processes.
- Use `addBulk` for adds.
- Keep job data small and remove finished jobs fast (`removeOnComplete: true` or a small count).
- Reduce events (smaller stream `maxLen`) and avoid many `QueueEvents`.
- Avoid per-job extra Redis calls like many `updateProgress` calls.
- Split hot queues and put them on separate Redis instances if one is CPU-bound.

## 325: What usually limits BullMQ throughput?

Redis CPU, because Redis runs commands on one thread and BullMQ scripts do real work. Network round trips between workers and Redis come second. Once Redis CPU is near 100 percent, adding workers won't help; you need to reduce work per job or spread queues over more Redis instances.

## 326: How do priorities work internally?

Prioritized jobs go into a sorted set, with a score built from the priority and a counter, so jobs with the same priority keep FIFO order. When taking jobs, the worker first checks the normal wait list, then the prioritized set. Adding a prioritized job is O(log n), compared to O(1) for normal jobs.

## 327: Why can priorities be slow with a large queue?

Older versions stored prioritized jobs in the wait list and had to insert them in the right position, which was O(n). Newer versions use a sorted set, so it's O(log n). Still, changing priority or adding many prioritized jobs costs more than plain FIFO adds.

## 328: Why are jobs without priority processed before prioritized ones?

Because priority 0 means "no priority", and BullMQ checks the wait list before the prioritized set. If you want all jobs ordered by priority, give every job a priority, with your "normal" level set to some middle value.

## 329: What happens to a job's priority after a retry?

The job keeps its options, so it goes back into the prioritized set with the same priority when it moves from delayed back to waiting. A retried job doesn't jump to the front unless you change its priority.

## 330: How do rate limiting internals work?

There is a limiter key in Redis with a counter and an expiry equal to the `duration`. Each time a job is moved to active, the counter goes up. When it hits `max`, the script returns a delay, the worker waits that long, and jobs stay in waiting. Because the key is shared, the limit applies to all workers.

## 331: Why is the worker limiter not exact under high load?

The limit is checked when moving jobs to active, so the count is exact for starts, but jobs run for different times, and retries and stalled jobs count as starts again. Clock drift and network delay also play a role. Treat it as a close limit, and leave some room below the provider's real limit.

## 332: How do you combine a global rate limit with group-like limits?

Use the queue's global rate limit for the provider-wide limit, and do your own per-key check (a Redis counter with expiry) in the processor for the per-customer limit. When the key limit is hit, move the job to delayed with `DelayedError`, so it doesn't use a failed attempt.

## 333: How would you design per-tenant isolation with open source BullMQ?

A queue per tenant gives the strongest isolation, but needs a worker per queue and many connections, which doesn't scale to thousands of tenants. Shared queues with per-tenant limits in the processor scale better, but a big tenant can still fill the wait list. Many teams go with a middle ground: shared queues for small tenants and dedicated queues for big ones, or BullMQ Pro groups.

## 334: How does deduplication work internally?

When a job with a deduplication ID is added, a script tries to set a key like `<prefix>:<queue>:de:<id>` with the job ID, only if it doesn't exist, with the `ttl` if given. If the key exists, the add is skipped (or replaced in debounce mode) and a `deduplicated` event is written. Without a ttl, the key is removed when the job completes or fails.

## 335: What can go wrong if deduplication keys are not removed?

If a job is removed by hand in a way that doesn't clear the key, or something interrupts cleanup, new jobs with that ID keep being ignored. Use `removeDeduplicationKey` to fix it, and prefer a `ttl` for safety in throttle cases.

## 336: How do job schedulers avoid duplicates when many instances run?

The scheduler is stored once in Redis by its ID, and each next job gets an ID made from the scheduler ID and its run time. Creating that job is done in a script, so if two workers try at once, only one job is created. That's why you can't choose the job ID for scheduler jobs.

## 337: What happens to a scheduler if no worker runs for a few hours?

The one delayed job stays there. When a worker comes back, it runs that job once and the scheduler creates the next one for the next future time. Missed runs are not replayed. If you need every run, record the last run time in your data and catch up in the job.

## 338: How do you run a cron job on only one machine without BullMQ?

You'd need a distributed lock or a leader election. With BullMQ you get this for free: the scheduler makes one job per run, and only one worker takes it. This is a common reason to use BullMQ instead of `node-cron` in a multi-instance app.

## 339: How does the parent-child link in a flow work internally?

Each parent has a `dependencies` set with its children's keys. Each child stores its `parentKey`. When a child completes, a script moves it from the parent's dependencies to the `processed` hash with its return value. When the dependencies set is empty, the parent moves from `waiting-children` to wait.

## 340: Why is a flow added in one atomic call?

So you never get a parent without its children or children without a parent. `FlowProducer` builds all jobs in one Redis transaction. If it fails, nothing is added. Adding jobs one by one could leave a parent waiting for children that were never created.

## 341: What happens with a flow when a child is removed by removeOnComplete?

Removing the completed child is fine. Its return value was already copied into the parent's processed data when it completed, so `getChildrenValues` still works. What you lose is the child job itself for debugging.

## 342: How do you build a fan-out and fan-in pipeline with BullMQ?

Fan-out: a parent with many children, one per item. Fan-in: the parent processes after all children finish and combines results with `getChildrenValues`. For very large fan-outs, add children in chunks with `addBulk` and the `parent` option, and use `moveToWaitingChildren` in the parent.

## 343: What are the limits of very large flows?

The parent's dependencies set and processed hash grow with each child. `getChildrenValues` on 100,000 children returns a huge object. Adding a giant flow in one call blocks Redis for a while. Split into several levels (parent, chunk parents, children) to keep each part small.

## 344: How do you design a saga with BullMQ?

Model each step as a job, and on failure run compensating jobs in reverse order (refund the payment, release the stock). Store saga state in your database, not just in job data. BullMQ gives the retries and ordering, while your code owns the business state.

## 345: What happens if a parent job fails after its children succeeded?

The parent goes through its own retries like any job. If it still fails, the children stay completed and their side effects stay. You need idempotent or compensating logic, because BullMQ doesn't roll back children.

## 346: What is continueParentOnFailure?

A child option where, if the child fails, the parent is moved out of `waiting-children` right away and processed, even though other children may still be running. The parent can then check failed children and decide what to do, like cancelling the rest. It is useful when one failure should trigger cleanup early.

## 347: How does BullMQ pass data between a sandboxed processor and the main process?

With child processes, it uses Node.js IPC messages. With worker threads, it uses `postMessage`. Job data and return values are serialized, and calls like `updateProgress` are sent back as messages to the parent, which runs them against Redis.

## 348: How are sandboxed child processes managed?

BullMQ keeps a pool of child processes or threads. A job takes a free one, or a new one is started. When the job ends, the child goes back to the pool. If a child crashes, the job fails and a new child is started for the next job.

## 349: How do you pass startup settings to a sandboxed processor?

Use environment variables, which the child inherits, or read config from a file in the processor module. Code at the top level of the processor file runs once per child, so you can open connections there.

```js
// processor.js
import { createPool } from "./db.js";
const pool = createPool(process.env.DATABASE_URL);

export default async function (job) {
  return pool.query("select 1");
}
```

## 350: What are the memory risks of sandboxed processors?

Each child process has its own heap and loaded modules, so with high concurrency you can use a lot of memory. Worker threads share some memory but still have their own heaps. Keep concurrency in check and watch the total memory of the worker container, not just the main process.

## 351: How do you handle graceful shutdown with long jobs on Kubernetes?

On `SIGTERM`, call `worker.close()` so no new jobs are taken, and let active jobs finish within `terminationGracePeriodSeconds`. If jobs can take longer than that, make them resumable (save progress with `updateData`) so a stalled job picks up where it left off on another pod. Forced kills then cost only a little work.

## 352: What happens to active jobs when a pod is killed with SIGKILL?

The process dies right away and stops renewing locks. After the lock expires and the stalled check runs, the jobs are moved back to wait and another worker runs them again. That can take up to `lockDuration` plus `stalledInterval`. The work done so far may be repeated.

## 353: How do you reduce the time to recover stalled jobs?

Lower `lockDuration` and `stalledInterval`. But shorter locks need more frequent renewals and are more likely to expire during a short event loop block or network hiccup, which causes false stalls. Find a balance based on how fast you need recovery and how stable your workers are.

## 354: What is skipStalledCheck and when would you use it?

It turns off the stalled job check for that worker. You might use it when you run a separate process dedicated to that check, or for workers that do manual processing and handle stalls in their own way. If no worker checks for stalls, crashed jobs stay active forever.

## 355: What is skipLockRenewal?

It stops the worker from renewing locks on its own. You then must call `job.extendLock` yourself. It's mostly used with manual processing. With normal workers, turning it off makes jobs stall after `lockDuration`.

## 356: How do you debug a job that runs twice?

Check for stalled events for that job ID (`stalledCounter`, `attemptsStarted`), worker restarts at that time, Redis failovers, and duplicate adds (missing `jobId` or deduplication). Compare `attemptsStarted` and `attemptsMade`. Logs with job ID and attempt number make this much easier.

## 357: How do you debug jobs stuck in active?

Jobs stuck in active usually belong to a worker that died while no other worker is running the stalled check, or the check is turned off. Make sure at least one normal worker runs on the queue. Also check whether the processor is truly still running, like a promise that never resolves because of a missing `await` or a hung HTTP call with no timeout.

## 358: Why can a processor promise never resolve?

Common causes are an HTTP call without a timeout, waiting on an event that never fires, a callback API that is wrapped badly, or a deadlock with a database pool that's too small for the concurrency. BullMQ keeps renewing the lock, so the job stays active forever. Always add timeouts.

## 359: How do you debug jobs stuck in delayed?

Check that at least one worker runs on the queue, because workers move due delayed jobs. Check the job's `delay` and `timestamp`, and the server clocks. If the queue is rate limited, jobs can also be pushed to later times. `job.promote()` can unblock a single job while you find the cause.

## 360: How do clock differences between servers affect BullMQ?

BullMQ uses timestamps from the client for things like `delay` and some time checks, while Redis has its own clock. Large clock skew between machines can make delayed jobs run early or late, and stalled checks act oddly. Keep all servers in sync with NTP.

## 361: How do you debug jobs stuck in waiting-children?

Load the parent and call `getDependencies()` to see which children are not processed, then check those children's states. A child might be failed without a failure option, sitting in a queue with no worker, or deleted by hand. Fix or remove the child, or use `failParentOnFailure` and the other options to avoid this next time.

## 362: How do you handle poison messages?

A poison message is a job that always crashes the worker, for example by running out of memory. It stalls, is moved back, and crashes the next worker. `maxStalledCount` stops the loop after a few tries by failing the job. Use sandboxed processors for risky input, so a crash only kills the child.

## 363: How do you protect against huge job data at the producer side?

Validate input before adding (with a schema library like Zod), set `sizeLimit` on jobs, and keep large data outside the queue. A single job with many megabytes of data slows Redis for everyone.

## 364: What security risks exist in BullMQ setups?

- Anyone with Redis access can read, change or add jobs, so Redis must not be public and must use a password and TLS.
- Job data may contain personal data or secrets, which stay in Redis and in dashboards.
- Dashboards like Bull Board can retry or delete jobs, so they need authentication.
- Workers trust job data, so a fake job could trigger actions. Validate data in the worker too.

## 365: Should you put secrets or tokens in job data?

No. Job data is stored in plain text in Redis, kept after completion and shown in dashboards and logs. Pass an ID and let the worker load the secret from a vault or the database when it runs.

## 366: How do you protect personal data in jobs?

Store only IDs, not names, emails or addresses, when you can. Remove completed and failed jobs after a short time. Restrict who can open the dashboard. If you must store sensitive data, encrypt it before adding and decrypt it in the worker.

## 367: How do you secure the connection to Redis?

Use TLS (`tls: {}` in connection options), a strong password or ACL user, and a private network. Redis ACLs can limit the user to the needed commands and key patterns, like `~bull:*`. Don't use `FLUSHALL` rights in the app user.

## 368: What Redis ACL permissions does BullMQ need?

It needs to run Lua scripts (`EVALSHA`, `EVAL`, `SCRIPT LOAD`), read and write lists, sets, sorted sets, hashes and streams, blocking commands like `BZPOPMIN`, `XREAD` for events, and `CLIENT` for setting names. Restrict key patterns to your prefix. Test the ACL setup in staging, since a missing command only fails at runtime.

## 369: How would you validate job data in the worker?

Parse it with a schema at the start of the processor and throw `UnrecoverableError` if it doesn't match, so bad data doesn't get retried.

```js
import { z } from "zod";
import { UnrecoverableError } from "bullmq";

const schema = z.object({ userId: z.number(), email: z.string().email() });

new Worker(
  "email",
  async (job) => {
    const parsed = schema.safeParse(job.data);
    if (!parsed.success) throw new UnrecoverableError(parsed.error.message);
    return send(parsed.data);
  },
  { connection },
);
```

## 370: How do you version job data when the format changes?

Add a `version` field to job data. During a deploy, old jobs with the old format may still be in the queue, so the worker must handle both versions until the old ones are gone. Deploy the worker that reads the new format first, then the producer that writes it.

## 371: Why should you deploy workers before producers when changing a job format?

If producers start adding new-format jobs while old workers are still running, the old workers will fail on them. Updating workers first lets them read both formats. Then you update producers. Once old jobs are drained, you can remove support for the old format.

## 372: How do you rename a queue in production without losing jobs?

Start workers on both the old and the new name, switch producers to the new name, wait until the old queue is empty (including delayed jobs and schedulers), then stop the old workers. Move or recreate job schedulers on the new queue.

## 373: How do you move jobs from one Redis instance to another?

There's no built-in migration. Usually you drain: point producers to the new Redis, keep old workers running until the old queue is empty, then turn them off. For delayed jobs or failed jobs you want to keep, write a script that reads them from the old queue and adds them to the new one.

## 374: How do you replay failed jobs after an outage at a controlled pace?

Use `queue.retryJobs({ state: 'failed', count })` in small batches, with a worker limiter or global rate limit so the recovered service isn't flooded. Watch error rates as you go, and stop if they rise again.

## 375: How do you design a priority system with many levels?

Map business levels to a few spaced priorities, like 1, 10, 100 and 1000, and give every job a priority so none bypass the order. With many low-priority jobs and steady high-priority traffic, low jobs can starve, so watch their wait time and use separate queues if needed.

## 376: How can low-priority jobs starve and how do you prevent it?

If high-priority jobs keep coming, workers always take them first and low ones wait forever. Fixes: a separate queue with its own workers for low-priority work, raising a job's priority with `changePriority` after it has waited too long, or limiting how many high-priority jobs can be added.

## 377: What is the cost of changePriority?

It moves the job in the prioritized sorted set, which is O(log n). It's fine for occasional changes. Changing priorities of many jobs in a loop is slower and adds load to Redis, so batch or avoid it if possible.

## 378: How does lifo interact with priority?

`lifo` only affects jobs without priority by pushing them to the front of the wait list. Prioritized jobs follow their priority order. Mixing both makes order hard to predict, so pick one approach per queue.

## 379: How do you implement a delayed retry with jitter by hand?

Add `jitter` to the backoff, or compute the delay in a custom `backoffStrategy`.

```js
new Worker("api", processor, {
  connection,
  settings: {
    backoffStrategy: (attemptsMade) => {
      const base = Math.min(2 ** attemptsMade * 1000, 60_000);
      return Math.round(base / 2 + (Math.random() * base) / 2);
    },
  },
});
```

Jitter spreads retries out so a recovered service isn't hit by all of them at once.

## 380: How do you implement a circuit breaker with BullMQ?

Track failures to the external service in Redis or memory. When too many fail in a short time, pause the queue (`queue.pause()`) or rate limit it with `worker.rateLimit(ms)` for a cool-down period, then let a few jobs through to test. This stops wasting attempts while the service is down.

## 381: When would you pause a queue from inside a worker?

When the processor sees that a dependency is down for everyone, like a 503 from a payment provider. Pausing the whole queue stops all workers, which saves attempts. Make sure some other process (a scheduled health check or an operator) resumes it, or use `rateLimit` with a duration instead, which ends on its own.

## 382: What happens to the event stream when no QueueEvents listener is running?

Events are still written to the stream and trimmed to `maxLen`. When a listener starts, by default it reads only new events. You can set `lastEventId` to read older events, as long as they haven't been trimmed yet.

## 383: How reliable are QueueEvents?

They're good for UI updates and metrics, but not for critical logic. If the listener is down longer than the stream keeps events, you miss some. For actions that must happen, put them in the processor itself or in a follow-up job, not in an event listener.

## 384: Why should important side effects not happen in a completed event listener?

The listener may not run if the process crashes, and if you have many listener processes, it runs in all of them. It also isn't retried on failure. Put important side effects in the job or in a new job added by the job, so BullMQ's retries cover them.

## 385: How do you scale QueueEvents for a WebSocket server with many instances?

Each server instance runs one `QueueEvents` per queue and forwards only events for the sockets connected to it. Every instance gets all events, which is fine at moderate volume. At high volume, have one process read events and publish only the needed ones through Redis pub/sub or your WebSocket layer.

## 386: How do you track per-user progress for many users efficiently?

Store progress with `updateProgress`, but send updates to clients only every few percent or every second, not on every row. Too many progress calls add Redis writes and stream events. Clients can also poll the job's state at intervals instead of listening to events.

## 387: What are the trade-offs of keeping completed jobs?

Keeping them helps debugging, audits and showing results to users. But they use Redis memory, and `getJobs` gets slower. A good middle ground is keeping a fixed count or a short age in Redis, and saving important results in your own database.

## 388: How do you store job results long term?

Have the processor write results to your database or object storage, and keep the BullMQ job only as a short-lived record. Redis is not meant to be your long-term store for job history.

## 389: How do you design a queue system for multiple regions?

Usually each region has its own Redis and workers, and jobs stay in their region. Cross-region Redis adds latency to every command and doesn't work well with blocking calls. For global work, pick one home region per queue, or send work between regions through an API.

## 390: How would you compare BullMQ with RabbitMQ?

BullMQ is a job queue library on top of Redis (or PostgreSQL), with built-in retries, delays, priorities, flows and scheduling, and it's easy to add to a Node.js app. RabbitMQ is a message broker with routing (exchanges, topics), many language clients and its own server. Pick BullMQ for background jobs in Node.js; RabbitMQ for messaging between many services and languages with complex routing.

## 391: How would you compare BullMQ with Kafka?

Kafka is a log for event streaming: messages are kept for a long time, many consumer groups can read the same events, and order is kept per partition. BullMQ is a work queue: each job goes to one worker and is removed or archived after. Use Kafka for event pipelines and replay; use BullMQ for tasks with retries, delays and scheduling.

## 392: How would you compare BullMQ with AWS SQS?

SQS is fully managed, scales almost without limit and has no server to run, but it has limits like a 15 minute max delay, no priorities, and fewer features. BullMQ gives more features (flows, priorities, rate limits, schedulers, progress) but you run and size Redis yourself. Teams on AWS with simple needs often pick SQS.

## 393: How would you compare BullMQ with pg-boss or Graphile Worker?

pg-boss and Graphile Worker are queue libraries that only use PostgreSQL, so there is no Redis to run and jobs can be added in the same transaction as your data. BullMQ is generally faster on Redis and has more features. Since v6 BullMQ also has a PostgreSQL backend, so the choice is more about features and ecosystem.

## 394: How would you compare BullMQ with Temporal?

Temporal is a workflow engine: you write long-running workflows as code, and it keeps their state and history and resumes them after crashes. BullMQ is lighter: jobs, retries and flows, but you manage multi-step state yourself. For complex, long, stateful business processes Temporal fits better. For background jobs, BullMQ is simpler.

## 395: When would you not choose BullMQ?

When you need message routing between many services in many languages (RabbitMQ), event replay and long retention (Kafka), a fully managed queue with no servers (SQS), or long durable workflows with full history (Temporal). Also when you can't run Redis or PostgreSQL in your setup.

## 396: How do you make a job wait for an external event, like a user confirmation?

Don't keep the job active while waiting. Either finish the job and add a new one when the event arrives, or move the job to delayed with `DelayedError` and check again later. For complex waiting logic, keep the state in your database and let the event handler add the next job.

## 397: How do you handle jobs that need a lock on a shared resource?

Use a distributed lock (like a Redis lock with an expiry) inside the processor, or route all jobs for the same resource to a queue with concurrency 1. If the lock isn't free, move the job to delayed and throw `DelayedError` instead of waiting in the processor.

## 398: How do you avoid thundering herd effects after a long outage?

When the service comes back, thousands of retried and delayed jobs may run at once. Use jitter in backoff, a rate limiter, global concurrency, and replay failed jobs in batches. Ramping up slowly gives the service time to recover.

## 399: How do you design job retries for payment operations?

Use an idempotency key from your business data in the payment API call, so a retry can't double charge. Retry only on network errors and 5xx responses, not on declined cards. Store the payment result in your database right after the call, and check it at the start of the job so a retry skips work that already succeeded.

## 400: What happens if two workers run with different processor code during a deploy?

Jobs are taken by whichever worker is free, so some jobs run with the old code and some with the new one. That's fine if both versions are compatible. If the new code needs new data or a new database schema, make the change backward compatible or use a new queue name.

## 401: How does the BullMQ v6 backend system work?

In v6 the `Queue`, `Worker`, `QueueEvents` and `FlowProducer` classes talk to a backend through an interface (`IQueueBackend`), instead of calling Redis directly. A backend factory creates the backend for each instance. Redis is the default, PostgreSQL is built in, and you can pass your own factory. The public API stays the same no matter which backend you use.

## 402: What is a BackendFactory?

A function that BullMQ calls to create the backend for a class instance. You pass it as the last constructor argument, set it globally with `setDefaultBackendFactory`, or bind it with `withBackend`. In v6 it replaced the optional `Connection` constructor argument from v5.

```js
import { withBackend, createPostgresBackend } from "bullmq";

const { Queue, Worker } = withBackend(createPostgresBackend);
const queue = new Queue("email", { connection: process.env.DATABASE_URL });
```

## 403: How do queues on PostgreSQL take jobs without workers getting in each other's way?

Queue systems on PostgreSQL usually rely on row locking with `FOR UPDATE SKIP LOCKED`, so each worker grabs a different row without waiting for others, and on `LISTEN`/`NOTIFY` to wake workers up instead of polling all the time. The details of BullMQ's backend are internal and may change between versions, so treat this as the general idea. In practice, what matters to you is that waiting workers hold connections, so pool size and `max_connections` matter.

## 404: How do you size the PostgreSQL pool for BullMQ workers?

Count the connections each worker needs (normal commands plus waiting for jobs), multiply by the number of workers and processes, and add your app's own usage. Keep it under `max_connections` with some room. A pooler like PgBouncer can help, but test it, because session features like `LISTEN` don't work in transaction pooling mode.

## 405: Can you run Redis and PostgreSQL backends side by side?

Yes. Each class instance can get its own backend factory, so one queue can live in Redis and another in PostgreSQL. A flow, however, has to keep all its jobs on one backend.

## 406: Why did BullMQ 6 make migrations for PostgreSQL explicit?

Running schema changes on app startup can race between many instances and can surprise teams that have strict database change processes. Making `runMigrations` an explicit step lets you run it once in your deploy pipeline and control when the schema changes. It still uses an advisory lock, in case it runs twice.

## 407: How would you run BullMQ on a managed Redis service?

Check that the service lets you set `maxmemory-policy noeviction`, supports Lua scripts and blocking commands, and allows enough connections. Some serverless Redis services bill per command, and BullMQ's blocking and polling can make that expensive. A fixed-size managed Redis (ElastiCache, Memorystore, Azure Cache, Redis Cloud) usually fits better.

## 408: What issues can come up with serverless Redis like Upstash?

Per-request pricing adds up because workers send commands all the time, even when idle. Some features may differ or have limits. It works for small volume, but test the costs and set `drainDelay` and other options to reduce idle traffic.

## 409: What does drainDelay do?

It is how long, in seconds, a worker blocks waiting for a job when the queue is empty before trying again. A longer value means fewer Redis calls while idle. The default is 5 seconds.

## 410: How do you profile a slow worker?

Measure processing time per job name, and split it into time spent in your code, in the database and in external calls (tracing helps a lot here). Check event loop lag. If Redis calls are slow, look at Redis latency and `SLOWLOG`. Often the issue is one slow external call, not BullMQ itself.

## 411: How do you detect event loop blocking in a worker?

Use `perf_hooks.monitorEventLoopDelay()` and log or export the delay. Spikes line up with stalled jobs and slow lock renewals. Fix them by moving CPU work to sandboxed processors or by splitting big sync loops with `await` points.

```js
import { monitorEventLoopDelay } from "node:perf_hooks";

const h = monitorEventLoopDelay();
h.enable();
setInterval(() => console.log("p99 ms", h.percentile(99) / 1e6), 10_000);
```

## 412: How do Redis Lua scripts in BullMQ affect Redis latency?

While a script runs, Redis does nothing else. Most BullMQ scripts are short, but some, like `clean`, `obliterate`, `drain` or `retryJobs` on huge queues, do a lot of work. BullMQ runs those in batches to avoid long blocks. Still, run heavy cleanups at quiet times.

## 413: Why does obliterate run in batches?

A huge queue can have millions of keys. Deleting them all in one script would block Redis for seconds or more. So `obliterate` deletes a batch per call and loops until done. That's also why it can take a while on big queues.

## 414: What is the cost of getJobs on a big completed set?

It reads a range from the sorted set (cheap) and then loads each job hash (one read per job). Asking for 10,000 jobs means 10,000 hash reads and a big response. Page through with small ranges and avoid running it often in dashboards.

## 415: How do you safely clean a queue with millions of completed jobs?

Call `queue.clean(grace, limit, 'completed')` in a loop with a limit like 1000 to 10,000 per call, and wait a bit between calls. Then set `removeOnComplete` so it doesn't build up again.

```js
let removed;
do {
  removed = await queue.clean(0, 5000, "completed");
  await new Promise((r) => setTimeout(r, 100));
} while (removed.length > 0);
```

## 416: How do you handle a sudden spike of a million jobs?

Make sure Redis has memory for them (small job data helps), add them with `addBulk` in chunks, and scale workers up. If downstream services can't keep up, use rate limits and let the queue absorb the spike. That buffering is a main reason to use a queue.

## 417: What is backpressure and how do you apply it with BullMQ?

Backpressure means slowing producers when consumers can't keep up. Check the waiting count before adding and reject or slow down when it is too high, or limit how many jobs a single user can have pending. Otherwise Redis memory grows without bound.

```js
const { waiting } = await queue.getJobCounts("waiting");
if (waiting > 100_000) throw new Error("Queue is full, try later");
await queue.add("import", data);
```

## 418: How would you design a video processing pipeline with BullMQ?

Upload to object storage, then add a flow: a parent "publish" job with children for each output size (encode 1080p, 720p, 480p), each child with its own child for thumbnail or audio steps if needed. Encoding runs in sandboxed processors on CPU-heavy machines with low concurrency. The parent updates the database and notifies the user when all are done.

## 419: How would you design a notification service with BullMQ?

One queue per channel (email, SMS, push) so each has its own rate limits and workers. A router job decides channels based on user settings and adds channel jobs. Use deduplication or custom IDs to avoid double sends, respect provider rate limits, and store delivery status in your database.

## 420: How would you design scheduled reports for thousands of customers?

Don't create one scheduler per customer if there are many. Use one scheduler that runs a "dispatcher" job, which finds customers due now and adds a report job per customer with `addBulk`. Spread them out with small delays so they don't all hit the database at once.

## 421: Why avoid thousands of job schedulers?

Each scheduler keeps data and a delayed job in Redis, and creating, updating and listing them gets heavier as the number grows. A dispatcher pattern with one scheduler and your own data about who is due is easier to manage and change.

## 422: How would you handle multi-step onboarding emails over days?

Add delayed jobs with custom IDs per user and step, like `onboarding-<userId>-day3`. When the user does the action that makes an email useless, remove the pending job by its ID. Or let each job check user state before sending, so outdated emails are skipped.

## 423: How do you prevent a job from running if its data is outdated?

Store a version or `updatedAt` in the job, and in the processor compare it to the current record in the database. If the record has changed since the job was added, skip or reprocess with fresh data. Deduplication in debounce mode can also make sure only the latest change runs.

## 424: How do you implement a delay queue for retries at specific times?

Compute the next time (for example the next business hour), then call `job.moveToDelayed(timestamp, token)` and throw `DelayedError`. The job isn't counted as failed and returns at that time.

```js
if (!isBusinessHours()) {
  await job.moveToDelayed(nextBusinessHour().getTime(), token);
  throw new DelayedError();
}
```

## 425: Does moving a job to delayed with DelayedError use an attempt?

No. It isn't a failure, so `attemptsMade` doesn't go up for it. That's why it's good for "not now" logic. Be careful to avoid moving the same job forever; add your own counter in the data if needed.

## 426: How does BullMQ handle a job whose processor resolves after its lock was lost?

When the worker tries to complete the job, the script checks the lock token. If another worker now owns the job, or the lock is gone, completion fails with a lock error, and the result is thrown away. The job continues under the new owner. This is another reason processors must be idempotent.

## 427: What does the error "Missing lock for job" mean?

The worker tried to finish or move a job but no longer held its lock. Usually the lock expired because the event loop was blocked or Redis was slow, and the job was marked as stalled and maybe taken by another worker. Look for event loop lag and stalled events around that time.

## 428: What does "job stalled more than allowable limit" mean?

The job stalled more times than `maxStalledCount`, so BullMQ failed it. It often points to a job that crashes the worker or blocks it for longer than `lockDuration`. Check that specific job's data and resource usage.

## 429: Why might a worker log "Connection is closed" errors on shutdown?

Something still uses the Redis connection after `close()`, like a progress update after the worker closed, or the connection was closed by you before the worker finished. Close in the right order: workers first (wait for them), then queues and events, then any shared ioredis instance.

## 430: How do you close shared connections in the right order?

```js
await Promise.all(workers.map((w) => w.close()));
await Promise.all([queue.close(), events.close(), flow.close()]);
await sharedRedis.quit();
```

Workers first, so active jobs can still use their connections to finish.

## 431: What happens if you call queue.add with a very large addBulk array?

It runs as one atomic operation, so Redis is busy for the whole insert and the request and response are big. Split into chunks of a few hundred to a few thousand jobs to keep latency low for other clients.

## 432: How do you choose between many small jobs and fewer big jobs?

Small jobs give better retries (only the failed piece repeats), better parallelism and progress. But each job has overhead in Redis and network calls. If per-item work is tiny (like updating one row), group items into chunks of 100 to 1000 per job. If items are heavy, one job per item is fine.

## 433: How do you keep job order per key with many workers?

Without Pro groups, one way is to route jobs by key to N queues (hash of the key mod N), and run each queue with concurrency 1. Jobs for the same key always land on the same queue and run in order, while different queues run in parallel.

## 434: How does BullMQ Pro groups keep order per group?

With group concurrency set to 1, only one job per group runs at a time, so jobs in the same group run in order, while different groups run in parallel. Workers rotate between groups for fairness. It solves the per-key order problem without managing many queues.

## 435: What are BullMQ Pro observables?

A Pro feature where the processor returns an observable instead of a promise. It lets jobs emit values over time and be cancelled cleanly, and it can save state as the job runs. It's useful for long jobs that need clean cancellation.

## 436: How would you implement job cancellation for running jobs in open source BullMQ?

Store a cancel flag (like a Redis key `cancel:<jobId>`) and check it between steps in the processor. Pass an `AbortController` to your HTTP calls and abort it when the flag is set. Then throw an `UnrecoverableError('cancelled')`. You can poll the flag or subscribe to a Redis channel for faster reaction.

## 437: How do you prevent a hot key in the limiter or meta keys?

All workers on a queue touch the same limiter and meta keys, which live on one Redis node. At very high rates this becomes a bottleneck. The fix is to split the work across several queues, each with its own limiter, and divide the rate between them.

## 438: How do you plan Redis capacity for BullMQ?

Look at job rate (adds and completions per second), job size, retention (how many completed and failed jobs you keep) and number of connections. Redis CPU usage grows with the job rate; memory grows with retention. Load test with real job sizes and watch Redis CPU, memory and latency.

## 439: How do you load test BullMQ?

Write a script that adds jobs at a fixed rate with real data sizes, run workers with your normal settings, and measure throughput, wait time, processing time and Redis CPU. Increase the rate until wait time grows without bound. That point is your capacity for this setup.

## 440: What happens to job schedulers if you obliterate a queue?

They are deleted with everything else. If your app calls `upsertJobScheduler` on startup, they come back on the next deploy; otherwise you must recreate them. Keep scheduler definitions in code so they're easy to restore.

## 441: How do you keep job schedulers in sync with your code?

On startup, upsert every scheduler defined in code, then list existing schedulers with `getJobSchedulers` and remove ones that are no longer defined. Run this in one place, like a deploy step, to avoid many instances doing it at once.

```js
const wanted = {
  "daily-report": { pattern: "0 0 3 * * *" },
  cleanup: { every: 3_600_000 },
};

for (const [id, repeat] of Object.entries(wanted)) {
  await queue.upsertJobScheduler(id, repeat, { name: id });
}
for (const s of await queue.getJobSchedulers()) {
  if (!wanted[s.key]) await queue.removeJobScheduler(s.key);
}
```

## 442: How do you handle backward compatibility for jobs left in a queue after a v5 to v6 upgrade?

Before upgrading, list and remove legacy repeatable jobs and replace them with job schedulers. Make sure no code still uses `debounce` or `job.discard()`. Delayed and waiting normal jobs carry over, but test the upgrade on a copy of production Redis data first.

## 443: Why did v6 remove the paused state from jobs?

Jobs in a paused queue were in a separate state, which made counts and logic more complex. In v6, pausing is just a flag on the queue, and the jobs stay in `waiting`. Code that checked for `'paused'` in `getState` or counts must be updated.

## 444: What does ioredis being an optional peer dependency mean for you?

BullMQ 6 doesn't install `ioredis` for you. If you use the Redis backend, add `ioredis` to your own `package.json`. If you only use PostgreSQL, you don't need it. This makes installs smaller for non-Redis setups.

## 445: How do you avoid memory leaks in long-running workers?

Don't keep per-job data in global maps or arrays. Remove event listeners you add per job. Close any per-job resources in `finally`. Watch the heap over time, and for code you can't control, use sandboxed processors so leaks stay in the children, which get replaced.

## 446: How do you handle a worker that has to finish its job even during shutdown?

`worker.close()` already waits for active jobs. Make sure the process manager waits long enough before sending `SIGKILL`, and stop the HTTP server and other parts first. If a job can take longer than the allowed time, make it resumable or split it.

## 447: How would you investigate a sudden rise in failed jobs?

Group failures by job name and `failedReason`, check when they started, and compare with deploys and incidents in services the jobs call. Look at a few failed jobs in detail (data, logs, stack traces). Then fix the cause and use `retryJobs` to replay them once it's safe.

## 448: How do you design for "at least once" delivery in a whole system?

Every consumer must be idempotent, every producer must be safe to retry, and state changes go through a database with unique keys. BullMQ handles retries and recovery from crashes. Your code handles duplicates. Logs with job IDs let you trace what happened when something runs twice.

## 449: What are common mistakes teams make with BullMQ in production?

- No `removeOnComplete`, so Redis memory grows forever.
- Using an eviction policy on Redis.
- CPU-heavy code in normal processors, causing stalls.
- Non-idempotent processors that double charge or double send.
- No `error` listener on workers.
- No timeouts on external calls, so jobs hang.
- Creating a new `Queue` per request.
- Open dashboards without authentication.

## 450: How would you explain BullMQ's trade-offs to your team?

It is easy to start with, has many features out of the box and is fast on Redis. The costs are that you run and size Redis (or PostgreSQL), delivery is at least once so jobs must be idempotent, and some features like groups need the Pro version. For Node.js background jobs, retries and scheduling it's a good default. For cross-service messaging or event replay, use a broker or a log.
