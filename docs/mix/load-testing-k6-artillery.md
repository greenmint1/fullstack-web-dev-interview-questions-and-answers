# Load Testing (k6, Artillery) Interview Questions and Answers

_Last updated: November 25, 2026_

150 load testing interview questions with answers, split into three levels: 50 easy, 50 moderate and 50 advanced.

The answers target Grafana k6 v1.x and Artillery 2.x. k6 tests are written in JavaScript (or TypeScript) and run on a Go engine, while Artillery tests are mostly YAML with optional Node.js code. Older APIs that you will still see in real projects, like the legacy `k6/ws` module or the `artillery report` command, are marked as legacy.

## Table of Contents

- [Easy Questions (1-50)](#easy-questions-1-50)
- [Moderate Questions (51-100)](#moderate-questions-51-100)
- [Advanced Questions (101-150)](#advanced-questions-101-150)

### Easy Questions (1-50)

- [1: What is load testing?](#1-what-is-load-testing)
- [2: What are the main types of performance tests?](#2-what-are-the-main-types-of-performance-tests)
- [3: What is a smoke test in load testing and why run it first?](#3-what-is-a-smoke-test-in-load-testing-and-why-run-it-first)
- [4: Why should a team load test before a release?](#4-why-should-a-team-load-test-before-a-release)
- [5: What is k6?](#5-what-is-k6)
- [6: What is Artillery?](#6-what-is-artillery)
- [7: How do you install k6 and run your first test?](#7-how-do-you-install-k6-and-run-your-first-test)
- [8: What does a basic k6 script look like?](#8-what-does-a-basic-k6-script-look-like)
- [9: What is a virtual user (VU)?](#9-what-is-a-virtual-user-vu)
- [10: What is an iteration in k6?](#10-what-is-an-iteration-in-k6)
- [11: What do the vus and duration options mean in k6?](#11-what-do-the-vus-and-duration-options-mean-in-k6)
- [12: Why do load tests use sleep or think time?](#12-why-do-load-tests-use-sleep-or-think-time)
- [13: What are stages in k6?](#13-what-are-stages-in-k6)
- [14: What is a check in k6?](#14-what-is-a-check-in-k6)
- [15: What are thresholds in k6?](#15-what-are-thresholds-in-k6)
- [16: What are the main built-in HTTP metrics in k6?](#16-what-are-the-main-built-in-http-metrics-in-k6)
- [17: What does http_req_failed measure?](#17-what-does-http_req_failed-measure)
- [18: Why use percentiles like p95 and p99 instead of the average?](#18-why-use-percentiles-like-p95-and-p99-instead-of-the-average)
- [19: What is throughput in load testing?](#19-what-is-throughput-in-load-testing)
- [20: What is the difference between latency and response time?](#20-what-is-the-difference-between-latency-and-response-time)
- [21: How do you read the k6 end-of-test summary?](#21-how-do-you-read-the-k6-end-of-test-summary)
- [22: What are the lifecycle stages of a k6 test?](#22-what-are-the-lifecycle-stages-of-a-k6-test)
- [23: How do you send a POST request with a JSON body in k6?](#23-how-do-you-send-a-post-request-with-a-json-body-in-k6)
- [24: How do you add headers or an auth token to k6 requests?](#24-how-do-you-add-headers-or-an-auth-token-to-k6-requests)
- [25: How do you use environment variables in a k6 script?](#25-how-do-you-use-environment-variables-in-a-k6-script)
- [26: What are __VU and __ITER in k6?](#26-what-are-__vu-and-__iter-in-k6)
- [27: What is group() in k6?](#27-what-is-group-in-k6)
- [28: Can you use npm packages and Node.js APIs in k6?](#28-can-you-use-npm-packages-and-nodejs-apis-in-k6)
- [29: How do you install Artillery and run your first test?](#29-how-do-you-install-artillery-and-run-your-first-test)
- [30: What does a basic Artillery test file look like?](#30-what-does-a-basic-artillery-test-file-look-like)
- [31: What are phases in Artillery?](#31-what-are-phases-in-artillery)
- [32: What is the difference between arrivalRate and arrivalCount in Artillery?](#32-what-is-the-difference-between-arrivalrate-and-arrivalcount-in-artillery)
- [33: What is a scenario and a flow in Artillery?](#33-what-is-a-scenario-and-a-flow-in-artillery)
- [34: How do you send a POST request with JSON in Artillery?](#34-how-do-you-send-a-post-request-with-json-in-artillery)
- [35: What does think do in Artillery?](#35-what-does-think-do-in-artillery)
- [36: How do you capture a value from a response in Artillery?](#36-how-do-you-capture-a-value-from-a-response-in-artillery)
- [37: How do variables and templates work in Artillery?](#37-how-do-variables-and-templates-work-in-artillery)
- [38: What metrics does Artillery report?](#38-what-metrics-does-artillery-report)
- [39: What is artillery quick?](#39-what-is-artillery-quick)
- [40: How do you load test data from a CSV file in Artillery?](#40-how-do-you-load-test-data-from-a-csv-file-in-artillery)
- [41: What is the weight option in Artillery scenarios?](#41-what-is-the-weight-option-in-artillery-scenarios)
- [42: What is target in the Artillery config?](#42-what-is-target-in-the-artillery-config)
- [43: How do environments work in Artillery?](#43-how-do-environments-work-in-artillery)
- [44: What is the difference between concurrent users and requests per second?](#44-what-is-the-difference-between-concurrent-users-and-requests-per-second)
- [45: Where should you run load tests?](#45-where-should-you-run-load-tests)
- [46: What is a performance baseline?](#46-what-is-a-performance-baseline)
- [47: What are SLA and SLO, and how do they relate to load tests?](#47-what-are-sla-and-slo-and-how-do-they-relate-to-load-tests)
- [48: What kinds of errors do you usually see in load test results?](#48-what-kinds-of-errors-do-you-usually-see-in-load-test-results)
- [49: How do you save raw results to a file in k6 and Artillery?](#49-how-do-you-save-raw-results-to-a-file-in-k6-and-artillery)
- [50: How do k6 and Artillery compare at a high level?](#50-how-do-k6-and-artillery-compare-at-a-high-level)

### Moderate Questions (51-100)

- [51: What are scenarios in k6?](#51-what-are-scenarios-in-k6)
- [52: What executors does k6 have?](#52-what-executors-does-k6-have)
- [53: When would you use constant-vus versus constant-arrival-rate?](#53-when-would-you-use-constant-vus-versus-constant-arrival-rate)
- [54: What are preAllocatedVUs and maxVUs in arrival-rate executors?](#54-what-are-preallocatedvus-and-maxvus-in-arrival-rate-executors)
- [55: What does dropped_iterations mean in k6?](#55-what-does-dropped_iterations-mean-in-k6)
- [56: What is the difference between shared-iterations and per-vu-iterations?](#56-what-is-the-difference-between-shared-iterations-and-per-vu-iterations)
- [57: How do you set thresholds for a specific endpoint or scenario in k6?](#57-how-do-you-set-thresholds-for-a-specific-endpoint-or-scenario-in-k6)
- [58: What do abortOnFail and delayAbortEval do?](#58-what-do-abortonfail-and-delayaborteval-do)
- [59: What custom metric types does k6 support?](#59-what-custom-metric-types-does-k6-support)
- [60: How do you stop dynamic URLs from creating thousands of metric series in k6?](#60-how-do-you-stop-dynamic-urls-from-creating-thousands-of-metric-series-in-k6)
- [61: How do you load test data efficiently in k6?](#61-how-do-you-load-test-data-efficiently-in-k6)
- [62: How do you read a CSV file in k6?](#62-how-do-you-read-a-csv-file-in-k6)
- [63: How do you log in once and share the token with all VUs in k6?](#63-how-do-you-log-in-once-and-share-the-token-with-all-vus-in-k6)
- [64: What is correlation in load testing?](#64-what-is-correlation-in-load-testing)
- [65: How do cookies work in k6?](#65-how-do-cookies-work-in-k6)
- [66: How do you send parallel requests in k6?](#66-how-do-you-send-parallel-requests-in-k6)
- [67: How do you tell k6 that some non-2xx statuses are expected?](#67-how-do-you-tell-k6-that-some-non-2xx-statuses-are-expected)
- [68: How do you make a custom report at the end of a k6 test?](#68-how-do-you-make-a-custom-report-at-the-end-of-a-k6-test)
- [69: What output options does k6 have for sending metrics elsewhere?](#69-what-output-options-does-k6-have-for-sending-metrics-elsewhere)
- [70: What is the k6 web dashboard?](#70-what-is-the-k6-web-dashboard)
- [71: How do you run k6 in a CI pipeline?](#71-how-do-you-run-k6-in-a-ci-pipeline)
- [72: Can you write k6 tests in TypeScript?](#72-can-you-write-k6-tests-in-typescript)
- [73: What built-in modules does k6 have?](#73-what-built-in-modules-does-k6-have)
- [74: How do you organize a large k6 project?](#74-how-do-you-organize-a-large-k6-project)
- [75: How do you give every VU or iteration unique test data in k6?](#75-how-do-you-give-every-vu-or-iteration-unique-test-data-in-k6)
- [76: How do you add custom JavaScript logic to Artillery tests?](#76-how-do-you-add-custom-javascript-logic-to-artillery-tests)
- [77: How do you create custom metrics in Artillery?](#77-how-do-you-create-custom-metrics-in-artillery)
- [78: What is the Artillery expect plugin?](#78-what-is-the-artillery-expect-plugin)
- [79: How do you set pass/fail criteria in Artillery?](#79-how-do-you-set-passfail-criteria-in-artillery)
- [80: How do you get per-endpoint metrics in Artillery?](#80-how-do-you-get-per-endpoint-metrics-in-artillery)
- [81: How do loops and conditions work in Artillery flows?](#81-how-do-loops-and-conditions-work-in-artillery-flows)
- [82: What are before, after, beforeScenario and afterScenario in Artillery?](#82-what-are-before-after-beforescenario-and-afterscenario-in-artillery)
- [83: What does maxVusers do in Artillery?](#83-what-does-maxvusers-do-in-artillery)
- [84: What HTTP settings can you tune in Artillery?](#84-what-http-settings-can-you-tune-in-artillery)
- [85: How do you use secrets and environment variables in Artillery?](#85-how-do-you-use-secrets-and-environment-variables-in-artillery)
- [86: How do you send Artillery metrics to Datadog, Prometheus or other tools?](#86-how-do-you-send-artillery-metrics-to-datadog-prometheus-or-other-tools)
- [87: How do you run Artillery in a CI pipeline?](#87-how-do-you-run-artillery-in-a-ci-pipeline)
- [88: How do you test WebSockets with Artillery?](#88-how-do-you-test-websockets-with-artillery)
- [89: What is Artillery Cloud and how do you view reports?](#89-what-is-artillery-cloud-and-how-do-you-view-reports)
- [90: Why do you ramp up load gradually instead of starting at full load?](#90-why-do-you-ramp-up-load-gradually-instead-of-starting-at-full-load)
- [91: How do you build a realistic workload model?](#91-how-do-you-build-a-realistic-workload-model)
- [92: How do you estimate how many VUs you need?](#92-how-do-you-estimate-how-many-vus-you-need)
- [93: How do you debug a k6 script?](#93-how-do-you-debug-a-k6-script)
- [94: How do you debug an Artillery test?](#94-how-do-you-debug-an-artillery-test)
- [95: How do you know if the load generator is the bottleneck?](#95-how-do-you-know-if-the-load-generator-is-the-bottleneck)
- [96: What should you monitor on the system under test during a load test?](#96-what-should-you-monitor-on-the-system-under-test-during-a-load-test)
- [97: How do caches affect load test results?](#97-how-do-caches-affect-load-test-results)
- [98: How do you load test an API that has rate limiting?](#98-how-do-you-load-test-an-api-that-has-rate-limiting)
- [99: How do you load test a GraphQL API?](#99-how-do-you-load-test-a-graphql-api)
- [100: How do you test file uploads in k6 and Artillery?](#100-how-do-you-test-file-uploads-in-k6-and-artillery)

### Advanced Questions (101-150)

- [101: What is the difference between an open and a closed workload model?](#101-what-is-the-difference-between-an-open-and-a-closed-workload-model)
- [102: What is coordinated omission and how does it affect results?](#102-what-is-coordinated-omission-and-how-does-it-affect-results)
- [103: How does k6 run JavaScript internally?](#103-how-does-k6-run-javascript-internally)
- [104: How do you reduce memory usage in a large k6 test?](#104-how-do-you-reduce-memory-usage-in-a-large-k6-test)
- [105: How do you run k6 across multiple machines?](#105-how-do-you-run-k6-across-multiple-machines)
- [106: What are execution segments in k6?](#106-what-are-execution-segments-in-k6)
- [107: How does Artillery run distributed tests?](#107-how-does-artillery-run-distributed-tests)
- [108: How does Artillery model VUs, and how is that different from k6?](#108-how-does-artillery-model-vus-and-how-is-that-different-from-k6)
- [109: Why can an Artillery load generator distort results, and how do you notice?](#109-why-can-an-artillery-load-generator-distort-results-and-how-do-you-notice)
- [110: What are xk6 extensions and when do you need them?](#110-what-are-xk6-extensions-and-when-do-you-need-them)
- [111: How do you run browser-based load tests in k6?](#111-how-do-you-run-browser-based-load-tests-in-k6)
- [112: How does the Artillery Playwright engine work?](#112-how-does-the-artillery-playwright-engine-work)
- [113: How do you design and run a breakpoint test?](#113-how-do-you-design-and-run-a-breakpoint-test)
- [114: What do you look for in a soak test?](#114-what-do-you-look-for-in-a-soak-test)
- [115: How do you design a spike test?](#115-how-do-you-design-a-spike-test)
- [116: How do you find the bottleneck after a load test shows high latency?](#116-how-do-you-find-the-bottleneck-after-a-load-test-shows-high-latency)
- [117: What does it mean if http_req_blocked or http_req_connecting is high?](#117-what-does-it-mean-if-http_req_blocked-or-http_req_connecting-is-high)
- [118: How does connection reuse affect the realism of a load test?](#118-how-does-connection-reuse-affect-the-realism-of-a-load-test)
- [119: What problems appear when load testing through a load balancer or CDN?](#119-what-problems-appear-when-load-testing-through-a-load-balancer-or-cdn)
- [120: Why can't you average p95 values from several load generators?](#120-why-cant-you-average-p95-values-from-several-load-generators)
- [121: How do you detect performance regressions in CI without flaky results?](#121-how-do-you-detect-performance-regressions-in-ci-without-flaky-results)
- [122: How do you split load tests between pull requests and scheduled runs?](#122-how-do-you-split-load-tests-between-pull-requests-and-scheduled-runs)
- [123: How do you manage test data for large load tests?](#123-how-do-you-manage-test-data-for-large-load-tests)
- [124: How do you handle authentication tokens that expire during a long test?](#124-how-do-you-handle-authentication-tokens-that-expire-during-a-long-test)
- [125: How can you load test safely in production?](#125-how-can-you-load-test-safely-in-production)
- [126: What is special about load testing serverless backends like AWS Lambda?](#126-what-is-special-about-load-testing-serverless-backends-like-aws-lambda)
- [127: How do you recognize database connection pool exhaustion in a load test?](#127-how-do-you-recognize-database-connection-pool-exhaustion-in-a-load-test)
- [128: How do you test autoscaling with a load test?](#128-how-do-you-test-autoscaling-with-a-load-test)
- [129: How do you load test gRPC services with k6?](#129-how-do-you-load-test-grpc-services-with-k6)
- [130: How do you load test WebSockets in k6?](#130-how-do-you-load-test-websockets-in-k6)
- [131: How do you load test an asynchronous, queue-based workflow?](#131-how-do-you-load-test-an-asynchronous-queue-based-workflow)
- [132: How can client timeouts and retries distort load test results?](#132-how-can-client-timeouts-and-retries-distort-load-test-results)
- [133: Why does latency suddenly shoot up at a certain load level?](#133-why-does-latency-suddenly-shoot-up-at-a-certain-load-level)
- [134: What does it mean when throughput stops growing but latency keeps rising?](#134-what-does-it-mean-when-throughput-stops-growing-but-latency-keeps-rising)
- [135: What causes errors that only appear at high load, like 502, 504 or ECONNRESET?](#135-what-causes-errors-that-only-appear-at-high-load-like-502-504-or-econnreset)
- [136: What should you watch on a Node.js server during a load test?](#136-what-should-you-watch-on-a-nodejs-server-during-a-load-test)
- [137: How do you connect load test requests to backend traces?](#137-how-do-you-connect-load-test-requests-to-backend-traces)
- [138: How do you keep load test scripts and runs secure?](#138-how-do-you-keep-load-test-scripts-and-runs-secure)
- [139: How do you build a workload model from production logs?](#139-how-do-you-build-a-workload-model-from-production-logs)
- [140: How do you design a good threshold strategy?](#140-how-do-you-design-a-good-threshold-strategy)
- [141: How do you write a custom Artillery plugin?](#141-how-do-you-write-a-custom-artillery-plugin)
- [142: How do you stop a k6 test from code, and when should you?](#142-how-do-you-stop-a-k6-test-from-code-and-when-should-you)
- [143: What is the externally-controlled executor in k6 used for?](#143-what-is-the-externally-controlled-executor-in-k6-used-for)
- [144: How do you load test one microservice versus the whole system?](#144-how-do-you-load-test-one-microservice-versus-the-whole-system)
- [145: Scenario: p99 latency spikes every few minutes while load is steady. How do you investigate?](#145-scenario-p99-latency-spikes-every-few-minutes-while-load-is-steady-how-do-you-investigate)
- [146: Scenario: the load test passed, but production fell over at lower traffic. What went wrong?](#146-scenario-the-load-test-passed-but-production-fell-over-at-lower-traffic-what-went-wrong)
- [147: Scenario: how would you prepare load tests for a Black Friday sale?](#147-scenario-how-would-you-prepare-load-tests-for-a-black-friday-sale)
- [148: How do you choose between k6 and Artillery for a team?](#148-how-do-you-choose-between-k6-and-artillery-for-a-team)
- [149: How do you make load test results trustworthy?](#149-how-do-you-make-load-test-results-trustworthy)
- [150: What are the most common mistakes in load testing?](#150-what-are-the-most-common-mistakes-in-load-testing)

---

# Easy Questions (1-50)

## 1: What is load testing?

Load testing means sending a planned amount of traffic to a system and watching how it behaves. You check response times, error rates and resource usage (CPU, memory, database connections) while many users hit the app at the same time.

The goal is to answer questions like "Can the API handle 500 requests per second with p95 under 300 ms?" before real users find the answer for you.

## 2: What are the main types of performance tests?

- **Smoke test:** very small load (1-2 users) to check the script and the system work at all.
- **Average load test:** the normal traffic you expect on a typical day.
- **Stress test:** more than normal traffic, to see how the system behaves above its usual limits.
- **Spike test:** a sudden, short jump in traffic, like a flash sale or a push notification.
- **Soak (endurance) test:** normal load for many hours, to find memory leaks and slow resource exhaustion.
- **Breakpoint test:** load keeps growing until the system breaks, to find its maximum capacity.

## 3: What is a smoke test in load testing and why run it first?

A smoke test runs the load script with a tiny load, for example 1 VU for 30 seconds. It checks that the script has no bugs, the endpoints respond, auth works and the checks pass.

Running it first saves time. If the script is broken, a big 30-minute test only produces garbage numbers.

## 4: Why should a team load test before a release?

Functional tests prove that features work for one user. They say nothing about what happens with 1,000 users at once. Load tests find slow queries, missing indexes, small connection pools, memory leaks and bad timeouts before production does.

They also give real numbers for capacity planning: how many instances you need and when you need to scale.

## 5: What is k6?

k6 is an open source load testing tool from Grafana Labs. You write tests in JavaScript (or TypeScript), but the engine itself is written in Go, so one machine can run thousands of virtual users.

It has built-in checks, thresholds, many executors for different traffic shapes, and outputs for Prometheus, InfluxDB, JSON and Grafana Cloud k6. It is a single binary, so there is no `node_modules` to install.

## 6: What is Artillery?

Artillery is an open source load testing tool built on Node.js. Tests are usually written in YAML, and you can add custom logic in JavaScript functions.

It supports HTTP, WebSocket, Socket.IO and real browser tests through Playwright. It can also run distributed tests from your own AWS account (Fargate or Lambda) without extra infrastructure.

## 7: How do you install k6 and run your first test?

On macOS use `brew install k6`, on Windows `winget install k6` or Chocolatey, on Linux the package repo, or the `grafana/k6` Docker image.

```bash
k6 new script.js       # creates a sample script
k6 run script.js       # runs it locally
k6 run --vus 10 --duration 30s script.js
```

## 8: What does a basic k6 script look like?

```javascript
import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
  vus: 10,
  duration: "30s",
};

export default function () {
  const res = http.get("https://test.k6.io");
  check(res, { "status is 200": (r) => r.status === 200 });
  sleep(1);
}
```

`options` sets the load, and the default function is what each virtual user runs again and again until the test ends.

## 9: What is a virtual user (VU)?

A virtual user is a simulated client that runs your script. In k6 each VU is an independent JavaScript runtime that loops over the default function. In Artillery a VU runs one scenario from start to end and then finishes.

VUs are not the same as requests per second. One VU can send many requests, and how many depends on response times and sleep time.

## 10: What is an iteration in k6?

An iteration is one full run of the VU function (usually the default function). If a VU calls three endpoints and then sleeps for one second, that whole sequence is one iteration.

k6 reports `iterations` (total count) and `iteration_duration` (how long each one took).

## 11: What do the vus and duration options mean in k6?

`vus` is how many virtual users run at the same time. `duration` is how long the test runs. With `vus: 50` and `duration: '5m'`, k6 starts 50 VUs and each one keeps running iterations for 5 minutes.

You can also set them from the CLI: `k6 run --vus 50 --duration 5m script.js`. CLI flags override the values in `options`.

## 12: Why do load tests use sleep or think time?

Real users don't click as fast as a loop can run. They read the page, fill in forms and wait. Think time (`sleep()` in k6, `think` in Artillery) adds those pauses.

Without it, 100 VUs act like thousands of very fast bots, and you don't test a realistic traffic pattern. Adding a bit of randomness, like `sleep(Math.random() * 3 + 1)`, makes the traffic even more natural.

## 13: What are stages in k6?

`stages` is a shortcut for ramping the number of VUs up and down over time.

```javascript
export const options = {
  stages: [
    { duration: "2m", target: 100 }, // ramp up to 100 VUs
    { duration: "5m", target: 100 }, // stay at 100
    { duration: "1m", target: 0 }, // ramp down
  ],
};
```

Under the hood k6 turns this into a `ramping-vus` scenario.

## 14: What is a check in k6?

A check is an assertion on a response, like status code or body content. A failed check does not stop the test, it is only counted.

```javascript
check(res, {
  "status is 200": (r) => r.status === 200,
  "has user id": (r) => r.json("id") !== undefined,
});
```

The summary shows the pass rate of each check. To fail the test based on checks, add a threshold on the `checks` metric.

## 15: What are thresholds in k6?

Thresholds are pass/fail rules for metrics. If any threshold fails, k6 marks the test as failed and exits with a non-zero code, which makes it useful in CI.

```javascript
export const options = {
  thresholds: {
    http_req_failed: ["rate<0.01"], // less than 1% errors
    http_req_duration: ["p(95)<500"], // 95% of requests under 500ms
    checks: ["rate>0.99"],
  },
};
```

## 16: What are the main built-in HTTP metrics in k6?

- `http_reqs`: total number of requests.
- `http_req_duration`: total time for the request (sending + waiting + receiving).
- `http_req_failed`: rate of failed requests.
- `http_req_waiting`: time to first byte (TTFB), waiting for the server.
- `http_req_blocked`, `http_req_connecting`, `http_req_tls_handshaking`: time spent before the request could be sent.
- `http_req_sending` and `http_req_receiving`: time to send the body and to download the response.

There are also general ones like `iterations`, `vus`, `data_sent` and `data_received`.

## 17: What does http_req_failed measure?

It is a Rate metric that shows the share of requests that k6 considers failed. By default, any response with status outside 200-399 counts as failed, and so do network errors like timeouts.

You can change what counts as "expected" with `http.setResponseCallback(http.expectedStatuses(...))`, for example when a 404 is a normal response for one endpoint.

## 18: Why use percentiles like p95 and p99 instead of the average?

The average hides the slow requests. If 90 requests take 100 ms and 10 take 3 seconds, the average is 390 ms, which describes nobody's real experience.

p95 means 95% of requests were faster than this value. p99 shows the tail that your unluckiest users see. Most SLOs are written as percentiles, for example "p95 under 300 ms".

## 19: What is throughput in load testing?

Throughput is how much work the system completes per unit of time, usually requests per second (RPS) or transactions per second. In k6 it is shown as `http_reqs` with a per-second rate. In Artillery it is `http.request_rate`.

A healthy system increases throughput as load grows. When throughput stops growing but latency keeps rising, you have hit a limit.

## 20: What is the difference between latency and response time?

In everyday talk people use them as the same thing, but strictly:

- **Latency** is the time waiting for the response to start, often measured as time to first byte (TTFB). In k6 this is close to `http_req_waiting`.
- **Response time** is the full time from sending the request until the whole response is received. In k6 this is `http_req_duration`.

For big responses the difference can be large, because downloading the body takes time.

## 21: How do you read the k6 end-of-test summary?

At the end of a run k6 prints each metric with stats like `avg`, `min`, `med`, `max`, `p(90)` and `p(95)`, plus the pass rate of checks and the state of thresholds (green check or red cross).

Look first at thresholds, then `http_req_failed`, then `http_req_duration` percentiles and `http_reqs` per second. You can add more percentiles with the `summaryTrendStats` option, for example `['avg', 'p(95)', 'p(99)', 'max']`.

## 22: What are the lifecycle stages of a k6 test?

1. **Init:** code outside functions. It runs once per VU and is used for imports, options and loading files.
2. **Setup:** `export function setup()` runs once before the test. Whatever it returns is passed to the VU function and to teardown.
3. **VU code:** the default (or scenario) function, run in a loop by every VU.
4. **Teardown:** `export function teardown(data)` runs once at the end, for cleanup.

You can't make HTTP requests in the init stage.

## 23: How do you send a POST request with a JSON body in k6?

```javascript
import http from "k6/http";

export default function () {
  const payload = JSON.stringify({
    email: "test@example.com",
    password: "secret",
  });
  const params = { headers: { "Content-Type": "application/json" } };
  const res = http.post("https://api.example.com/login", payload, params);
  console.log(res.status);
}
```

If you pass a plain object instead of a string, k6 sends it as form data, not JSON.

## 24: How do you add headers or an auth token to k6 requests?

Pass a `headers` object in the params argument:

```javascript
const params = {
  headers: {
    Authorization: `Bearer ${token}`,
    "Content-Type": "application/json",
  },
};
http.get("https://api.example.com/me", params);
```

For headers that every request needs, keep the params object in one place and reuse it, so you don't repeat yourself.

## 25: How do you use environment variables in a k6 script?

Read them from the global `__ENV` object, and pass them with `-e` or from the system environment:

```bash
k6 run -e BASE_URL=https://staging.example.com script.js
```

```javascript
const BASE_URL = __ENV.BASE_URL || "http://localhost:3000";
```

This way the same script can run against local, staging and production-like environments.

## 26: What are __VU and __ITER in k6?

`__VU` is the number of the current VU (starting at 1, and 0 inside setup and teardown). `__ITER` is the iteration number of that VU, starting at 0.

They are handy for picking unique test data, for example `users[__VU % users.length]`. For more detail, like unique IDs across the whole test, use the `k6/execution` module.

## 27: What is group() in k6?

`group()` puts related requests and checks under a name, like a page or a user step. k6 then reports `group_duration` for each group, and the checks are shown nested in the summary.

```javascript
import { group } from "k6";

group("checkout", function () {
  http.get(`${BASE}/cart`);
  http.post(`${BASE}/orders`, body, params);
});
```

Don't use groups for every single request. For per-request names, tags are a better fit.

## 28: Can you use npm packages and Node.js APIs in k6?

Not directly. k6 does not run on Node.js, so `fs`, `process`, `Buffer` and native Node modules don't exist. You get k6's own modules (`k6/http`, `k6/crypto`, `k6/encoding` and others) plus remote modules from `jslib.k6.io`.

Pure JavaScript npm libraries can work if you bundle them with a tool like esbuild or webpack first. For things that need native code, there are xk6 extensions written in Go.

## 29: How do you install Artillery and run your first test?

Artillery is an npm package, so you need Node.js:

```bash
npm install -g artillery
artillery run test.yml
artillery run test.yml --output report.json
```

You can also add it as a dev dependency and run it with `npx artillery run test.yml`, which keeps the version pinned per project.

## 30: What does a basic Artillery test file look like?

```yaml
config:
  target: "https://api.example.com"
  phases:
    - duration: 60
      arrivalRate: 5
      name: Warm up

scenarios:
  - name: "Browse products"
    flow:
      - get:
          url: "/products"
      - think: 2
      - get:
          url: "/products/1"
```

`config` sets the target and the load, and `scenarios` describe what each virtual user does.

## 31: What are phases in Artillery?

Phases describe how load changes over time. Each phase has a `duration` and a rule for how many VUs arrive.

```yaml
phases:
  - duration: 60
    arrivalRate: 5
    rampTo: 50
    name: Ramp up
  - duration: 300
    arrivalRate: 50
    name: Sustained load
  - pause: 30
```

Phases run one after another. `rampTo` grows the arrival rate gradually, and `pause` sends no new users for a while.

## 32: What is the difference between arrivalRate and arrivalCount in Artillery?

- `arrivalRate: 10` means 10 new VUs start every second for the duration of the phase.
- `arrivalCount: 50` means 50 VUs in total, spread evenly over the phase duration.

So with `duration: 60`, `arrivalRate: 10` creates 600 VUs, while `arrivalCount: 60` creates 60 (one per second).

## 33: What is a scenario and a flow in Artillery?

A scenario is one user journey, for example "log in and buy a product". Its `flow` is the ordered list of steps: requests, think times, loops and function calls.

Each new VU picks one scenario, runs its flow from top to bottom and then exits. If there are several scenarios, Artillery picks one at random based on their weights.

## 34: How do you send a POST request with JSON in Artillery?

```yaml
scenarios:
  - flow:
      - post:
          url: "/login"
          json:
            email: "test@example.com"
            password: "secret"
          headers:
            X-Client: "load-test"
```

`json` sends the body as JSON and sets the `Content-Type` header. For form data use `form`, and for multipart uploads use `formData`.

## 35: What does think do in Artillery?

`think` pauses the VU for a number of seconds, like a user reading a page.

```yaml
flow:
  - get:
      url: "/products"
  - think: 3
  - get:
      url: "/cart"
```

It works the same way as `sleep()` in k6.

## 36: How do you capture a value from a response in Artillery?

Use `capture` with a JSONPath (or XPath, regex or header) and save it under a name:

```yaml
- post:
    url: "/login"
    json:
      email: "user@example.com"
      password: "secret"
    capture:
      - json: "$.token"
        as: "authToken"
- get:
    url: "/me"
    headers:
      Authorization: "Bearer {{ authToken }}"
```

Captured values live only inside that VU.

## 37: How do variables and templates work in Artillery?

Values in double curly braces, like `{{ userId }}`, are replaced at runtime. They can come from captures, from `config.variables`, from CSV payloads, from environment variables (`{{ $env.API_KEY }}`) or from built-in helpers like `{{ $randomNumber(1, 100) }}`.

```yaml
config:
  variables:
    category: ["books", "games", "music"]
scenarios:
  - flow:
      - get:
          url: "/search?c={{ category }}"
```

When a variable is a list, each VU gets one value from it.

## 38: What metrics does Artillery report?

Some of the common ones:

- `http.requests` and `http.request_rate`: how many requests and how many per second.
- `http.codes.200`, `http.codes.500` and so on: count per status code.
- `http.response_time`: min, max, mean, median, p95 and p99.
- `vusers.created`, `vusers.completed`, `vusers.failed`: VU counts.
- `vusers.session_length`: how long each scenario took.
- `errors.ETIMEDOUT`, `errors.ECONNREFUSED` and others: network errors.

Artillery prints these every 10 seconds during the run and a summary at the end.

## 39: What is artillery quick?

`artillery quick` runs a simple test against one URL without a YAML file. It is good for a fast sanity check.

```bash
artillery quick --count 20 --num 10 https://api.example.com/health
```

This creates 20 VUs, and each sends 10 GET requests. For anything real, write a proper test file.

## 40: How do you load test data from a CSV file in Artillery?

Use `config.payload`:

```yaml
config:
  payload:
    path: "users.csv"
    fields:
      - "email"
      - "password"
    order: sequence
    skipHeader: true
scenarios:
  - flow:
      - post:
          url: "/login"
          json:
            email: "{{ email }}"
            password: "{{ password }}"
```

Each VU gets one row. `order: sequence` goes through rows in order, the default picks them at random.

## 41: What is the weight option in Artillery scenarios?

`weight` controls how often a scenario is picked compared to others.

```yaml
scenarios:
  - name: Browse
    weight: 8
    flow: [...]
  - name: Checkout
    weight: 2
    flow: [...]
```

Here about 80% of VUs browse and 20% check out. This helps you copy the real traffic mix from production.

## 42: What is target in the Artillery config?

`target` is the base URL for all requests in the test. Request URLs like `/products` are added to it.

```yaml
config:
  target: "https://staging.example.com"
```

You can override it from the CLI with `--target https://other-host.com`, which is handy when the same test runs against different environments.

## 43: How do environments work in Artillery?

`config.environments` lets you keep different settings (target, phases, variables) for each environment in one file:

```yaml
config:
  target: "http://localhost:3000"
  environments:
    staging:
      target: "https://staging.example.com"
      phases:
        - duration: 300
          arrivalRate: 50
    local:
      phases:
        - duration: 30
          arrivalRate: 2
```

Pick one with `artillery run --environment staging test.yml` (or `-e staging`).

## 44: What is the difference between concurrent users and requests per second?

Concurrent users is how many users are active at the same time. Requests per second is how many requests arrive every second.

They are linked by response time and think time. 100 users who each send a request every 2 seconds give about 50 RPS. If the server slows down, the same 100 users send fewer requests. That is why "we need 1,000 users" is unclear until you also know what those users do.

## 45: Where should you run load tests?

Ideally in an environment that looks like production: same instance sizes, same database size, same config. A tiny staging server gives numbers that don't tell you much about production.

Never point a load test at third-party APIs (payment providers, email services) you don't own. Mock them or use their sandbox with permission. And tell the ops team before a big test so nobody thinks it is an attack.

## 46: What is a performance baseline?

A baseline is a set of results from a known, normal run: RPS, p95, p99 and error rate under a fixed load. Later test runs are compared against it.

Without a baseline you can't say if a new release made things slower. Save results from every run so you can compare them over time.

## 47: What are SLA and SLO, and how do they relate to load tests?

An SLO (service level objective) is an internal target, like "p95 latency under 300 ms and error rate under 0.1%". An SLA (service level agreement) is a promise to customers, often with penalties if broken.

In load tests you turn SLOs into thresholds (k6) or `ensure` checks (Artillery), so the test passes or fails based on the same numbers the business cares about.

## 48: What kinds of errors do you usually see in load test results?

- **HTTP 5xx:** the server failed (500), a proxy couldn't reach it (502), it is overloaded (503) or too slow (504).
- **HTTP 429:** rate limiting kicked in.
- **Timeouts:** the request took longer than the client timeout (`ETIMEDOUT` in Artillery, `request timeout` in k6).
- **Connection errors:** `ECONNREFUSED`, `ECONNRESET`, often when the server or a load balancer drops connections.

Any errors during a test need an explanation. A low error rate is not "fine" until you know why it happens.

## 49: How do you save raw results to a file in k6 and Artillery?

k6:

```bash
k6 run --out json=results.json script.js
k6 run --out csv=results.csv script.js
```

Artillery:

```bash
artillery run --output report.json test.yml
```

The k6 JSON output has every single data point, so the file can get big. The Artillery JSON has aggregated stats for each 10-second period plus the final summary.

## 50: How do k6 and Artillery compare at a high level?

- **Language:** k6 scripts are JavaScript/TypeScript on a Go engine. Artillery is mostly YAML with Node.js functions.
- **Performance:** k6 usually gets more load out of one machine. Artillery is limited by Node.js, but scales out easily on AWS Fargate or Lambda.
- **Ecosystem:** Artillery can use any npm package in its functions. k6 can't use Node APIs but has xk6 extensions.
- **Load model:** k6 supports both VU-based and arrival-rate executors. Artillery is arrival-rate based by design.
- **Browser tests:** k6 has the `k6/browser` module, Artillery has a Playwright engine.

Both are good choices. Teams often pick based on whether they prefer writing code or config.

# Moderate Questions (51-100)

## 51: What are scenarios in k6?

Scenarios let you run several independent workloads in one test, each with its own executor, VU count, timing, function and tags.

```javascript
export const options = {
  scenarios: {
    browse: {
      executor: "constant-vus",
      vus: 50,
      duration: "10m",
      exec: "browse",
    },
    checkout: {
      executor: "constant-arrival-rate",
      rate: 10,
      timeUnit: "1s",
      duration: "10m",
      preAllocatedVUs: 20,
      exec: "checkout",
      startTime: "1m",
    },
  },
};

export function browse() {
  /* ... */
}
export function checkout() {
  /* ... */
}
```

Every metric gets a `scenario` tag, so you can filter and set thresholds per scenario.

## 52: What executors does k6 have?

- `shared-iterations`: a fixed number of iterations shared between VUs.
- `per-vu-iterations`: each VU runs a fixed number of iterations.
- `constant-vus`: a fixed number of VUs for a duration.
- `ramping-vus`: the VU count changes over stages.
- `constant-arrival-rate`: a fixed number of iterations started per time unit.
- `ramping-arrival-rate`: the iteration start rate changes over stages.
- `externally-controlled`: VUs can be changed at runtime with `k6 scale` or the REST API.

The first four are closed models (they control VUs), the arrival-rate ones are open models (they control throughput).

## 53: When would you use constant-vus versus constant-arrival-rate?

Use `constant-vus` when you want to simulate a fixed number of users who wait for each response before doing the next thing, like a fixed pool of logged-in clients.

Use `constant-arrival-rate` when you need a specific throughput, for example "200 requests per second", no matter how slow the server becomes. With VU-based executors, a slow server makes VUs send fewer requests, so you never really reach the target load. Arrival-rate executors keep starting iterations at the planned rate.

## 54: What are preAllocatedVUs and maxVUs in arrival-rate executors?

Arrival-rate executors need free VUs to start each iteration. `preAllocatedVUs` is how many VUs k6 creates before the test starts. `maxVUs` is how many it may add during the test if all of them are busy.

```javascript
scenarios: {
  api: {
    executor: "constant-arrival-rate",
    rate: 200,
    timeUnit: "1s",
    duration: "5m",
    preAllocatedVUs: 100,
    maxVUs: 400,
  },
},
```

Creating VUs mid-test costs CPU and can affect results, so it's better to pre-allocate enough. A rough guess is `rate × expected iteration duration in seconds`.

## 55: What does dropped_iterations mean in k6?

`dropped_iterations` counts iterations that k6 could not start on time because there was no free VU. It shows up with arrival-rate executors (and also with `shared-iterations` when time runs out).

If you see it, either the server got slow and all VUs are stuck waiting, or `preAllocatedVUs`/`maxVUs` is too low. Either way, you did not deliver the load you planned, and you should add a threshold like `dropped_iterations: ['count<1']` if it matters.

## 56: What is the difference between shared-iterations and per-vu-iterations?

With `shared-iterations`, for example `vus: 10, iterations: 100`, all 10 VUs pull from one pool of 100. Fast VUs do more of them.

With `per-vu-iterations`, `vus: 10, iterations: 100` means each VU does exactly 100, so 1,000 in total.

Use `per-vu-iterations` when each VU must process its own fixed set of data, and `shared-iterations` when you just want a total amount of work done as fast as possible.

## 57: How do you set thresholds for a specific endpoint or scenario in k6?

Add a tag filter in curly braces to the metric name:

```javascript
export const options = {
  thresholds: {
    "http_req_duration{name:login}": ["p(95)<400"],
    "http_req_duration{scenario:checkout}": ["p(99)<1000"],
    "http_req_failed{type:api}": ["rate<0.005"],
  },
};

http.post(`${BASE}/login`, body, { tags: { name: "login" } });
```

This creates a sub-metric for only the matching samples. It's how you set a stricter target for a fast endpoint without making the global threshold useless.

## 58: What do abortOnFail and delayAbortEval do?

By default, k6 checks thresholds during the run but only reports the result at the end. With `abortOnFail: true` the test stops as soon as the threshold fails, which saves time and protects the system.

```javascript
thresholds: {
  http_req_failed: [
    { threshold: "rate<0.05", abortOnFail: true, delayAbortEval: "30s" },
  ],
},
```

`delayAbortEval` waits a while before checking, so a few early errors during warm-up don't kill the test.

## 59: What custom metric types does k6 support?

From `k6/metrics`:

- **Counter:** a sum, like number of orders created.
- **Gauge:** the last value, like queue size.
- **Rate:** the share of non-zero values, like percent of successful logins.
- **Trend:** stats (avg, percentiles) for a value, like a business-step duration.

```javascript
import { Trend, Counter } from "k6/metrics";

const checkoutTime = new Trend("checkout_time", true); // true = time values
const orders = new Counter("orders_created");

export default function () {
  const res = http.post(`${BASE}/orders`, body, params);
  checkoutTime.add(res.timings.duration);
  if (res.status === 201) orders.add(1);
}
```

Custom metrics must be created in the init context, and you can put thresholds on them.

## 60: How do you stop dynamic URLs from creating thousands of metric series in k6?

Every unique URL becomes a separate `url` and `name` tag value. If you request `/posts/1`, `/posts/2` and so on, you get a huge number of series, high memory use and messy reports.

Group them under one name, either with a tag or with the `http.url` template:

```javascript
http.get(`${BASE}/posts/${id}`, { tags: { name: "GET /posts/:id" } });

// or
http.get(http.url`${BASE}/posts/${id}`);
```

## 61: How do you load test data efficiently in k6?

Use `SharedArray` from `k6/data` together with `open()` in the init context:

```javascript
import { SharedArray } from "k6/data";

const users = new SharedArray("users", function () {
  return JSON.parse(open("./users.json"));
});

export default function () {
  const user = users[Math.floor(Math.random() * users.length)];
}
```

A normal array is copied into every VU's memory. `SharedArray` keeps one read-only copy shared by all VUs, which matters a lot with big files and many VUs. `open()` only works in the init context.

## 62: How do you read a CSV file in k6?

k6 has no built-in CSV parser in the core API, so the common way is papaparse from jslib inside a `SharedArray`:

```javascript
import papaparse from "https://jslib.k6.io/papaparse/5.1.1/index.js";
import { SharedArray } from "k6/data";

const users = new SharedArray("users", function () {
  return papaparse.parse(open("./users.csv"), { header: true }).data;
});
```

Newer k6 versions also have a `k6/experimental/csv` module that streams CSV files with less memory. Check your version before using it.

## 63: How do you log in once and share the token with all VUs in k6?

Do the login in `setup()` and return the token. k6 passes the returned data to every VU function call.

```javascript
export function setup() {
  const res = http.post(`${BASE}/login`, JSON.stringify(creds), {
    headers: { "Content-Type": "application/json" },
  });
  return { token: res.json("token") };
}

export default function (data) {
  http.get(`${BASE}/me`, {
    headers: { Authorization: `Bearer ${data.token}` },
  });
}
```

The data is serialized to JSON, so you can't return functions or class instances. If every VU should be a different user, log in per VU instead.

## 64: What is correlation in load testing?

Correlation means taking dynamic values from one response and using them in the next request: session IDs, CSRF tokens, order IDs, pagination cursors. Hard-coding them from a recording makes every VU reuse the same stale value, and requests fail or hit caches.

```javascript
const res = http.get(`${BASE}/form`);
const csrf = res.html().find("input[name=_csrf]").attr("value");
http.post(`${BASE}/submit`, { _csrf: csrf, name: "test" });
```

In Artillery you do the same with `capture`.

## 65: How do cookies work in k6?

Each VU has its own cookie jar. Cookies set by the server are stored and sent back automatically, like in a browser. By default the jar is cleared at the start of every iteration, so each iteration acts like a new session. Set `noCookiesReset: true` if you want them to persist.

You can manage cookies by hand too:

```javascript
const jar = http.cookieJar();
jar.set(BASE, "session_id", "abc123");
const res = http.get(BASE, { cookies: { theme: "dark" } });
```

## 66: How do you send parallel requests in k6?

Use `http.batch()`. It sends the requests at the same time, like a browser loading several resources.

```javascript
const responses = http.batch([
  ["GET", `${BASE}/api/user`],
  ["GET", `${BASE}/api/notifications`],
  ["GET", `${BASE}/api/feed`, null, { tags: { name: "feed" } }],
]);
check(responses[0], { "user ok": (r) => r.status === 200 });
```

The `batch` and `batchPerHost` options limit how many run in parallel.

## 67: How do you tell k6 that some non-2xx statuses are expected?

Use `http.setResponseCallback()` for the whole script, or the `responseCallback` param for one request:

```javascript
http.setResponseCallback(
  http.expectedStatuses(200, 201, { min: 300, max: 399 }),
);

// for one request where 404 is normal
http.get(`${BASE}/users/unknown`, {
  responseCallback: http.expectedStatuses(404),
});
```

This changes what counts in `http_req_failed` and also which requests go into the `{expected_response:true}` sub-metric of `http_req_duration`.

## 68: How do you make a custom report at the end of a k6 test?

Export `handleSummary(data)`. It receives all the end-of-test metrics and returns a map of file names (or `stdout`) to content:

```javascript
import { textSummary } from "https://jslib.k6.io/k6-summary/0.1.0/index.js";

export function handleSummary(data) {
  return {
    stdout: textSummary(data, { indent: " ", enableColors: true }),
    "summary.json": JSON.stringify(data, null, 2),
  };
}
```

You can generate JUnit XML for CI, an HTML report, or a short Slack message from the same data.

## 69: What output options does k6 have for sending metrics elsewhere?

With `--out` you can stream metrics while the test runs:

- `json=file.json` and `csv=file.csv` for local files.
- `experimental-prometheus-rw` to push to Prometheus (or Mimir) with remote write.
- `influxdb=http://localhost:8086/k6` for InfluxDB v1.
- `cloud` to stream a local run to Grafana Cloud k6.
- `experimental-opentelemetry` to send to an OpenTelemetry collector.

You can use several at once: `k6 run --out json=r.json --out experimental-prometheus-rw script.js`. Other systems are supported through xk6 output extensions.

## 70: What is the k6 web dashboard?

It's a built-in live dashboard you turn on with an environment variable:

```bash
K6_WEB_DASHBOARD=true k6 run script.js
K6_WEB_DASHBOARD=true K6_WEB_DASHBOARD_EXPORT=report.html k6 run script.js
```

While the test runs you can open `http://localhost:5665` to see charts of requests, latency and VUs. The export option saves a standalone HTML report at the end, which is useful as a CI artifact.

## 71: How do you run k6 in a CI pipeline?

Install k6 and run the script. If any threshold fails, k6 exits with code 99, which fails the job. With GitHub Actions there are official Grafana actions:

```yaml
jobs:
  load-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: grafana/setup-k6-action@v1
      - uses: grafana/run-k6-action@v1
        with:
          path: tests/load/smoke.js
        env:
          BASE_URL: ${{ vars.STAGING_URL }}
```

In CI, usually run a short smoke or average-load test on each merge and keep long tests for nightly or pre-release jobs.

## 72: Can you write k6 tests in TypeScript?

Yes. k6 v1 runs `.ts` files directly, it strips the types before running, so there is no build step. For editor autocomplete, install `@types/k6` as a dev dependency.

```typescript
import http from "k6/http";
import { check } from "k6";
import { Options } from "k6/options";

export const options: Options = { vus: 5, duration: "30s" };

export default function (): void {
  const res = http.get("https://test.k6.io");
  check(res, { "200": (r) => r.status === 200 });
}
```

It does not type-check during the run, so keep `tsc --noEmit` in your lint step if you want that.

## 73: What built-in modules does k6 have?

- `k6`: `check`, `group`, `sleep`, `fail`.
- `k6/http`: HTTP requests.
- `k6/metrics`: custom metrics.
- `k6/data`: `SharedArray`.
- `k6/execution`: info about the current VU, scenario and test, plus `test.abort()`.
- `k6/crypto` and `k6/encoding`: hashing, HMAC, base64.
- `k6/net/grpc`: gRPC.
- `k6/browser`: browser testing.
- `k6/timers`: `setTimeout` and `setInterval`.

On top of that, `jslib.k6.io` hosts helper libraries like `k6-utils` and `papaparse` that you import by URL.

## 74: How do you organize a large k6 project?

Split code into ES modules and import them with relative paths:

```
load-tests/
  lib/auth.js        // login helpers
  lib/config.js      // base URL, headers, thresholds
  flows/browse.js
  flows/checkout.js
  scenarios/smoke.js
  scenarios/peak.js
  data/users.json
```

Keep request logic in reusable functions, keep load shapes (`options`) in separate entry scripts, and share thresholds from one config file. That way smoke, average and stress tests all reuse the same user flows.

## 75: How do you give every VU or iteration unique test data in k6?

Use `k6/execution` for counters that are unique across the whole test:

```javascript
import exec from "k6/execution";
import { SharedArray } from "k6/data";

const users = new SharedArray("users", () => JSON.parse(open("./users.json")));

export default function () {
  // each iteration in the test gets the next user
  const user = users[exec.scenario.iterationInTest % users.length];
  // or one fixed user per VU
  const vuUser = users[(exec.vu.idInTest - 1) % users.length];
}
```

`__VU` and `__ITER` work too, but `__ITER` is only unique per VU, so two VUs can pick the same row.

## 76: How do you add custom JavaScript logic to Artillery tests?

Point `config.processor` to a JS file and call its exported functions from the flow:

```yaml
config:
  processor: "./functions.js"
scenarios:
  - flow:
      - function: "makeUser"
      - post:
          url: "/users"
          json:
            email: "{{ email }}"
          beforeRequest: "signRequest"
          afterResponse: "logErrors"
```

```javascript
module.exports = { makeUser, signRequest, logErrors };

async function makeUser(context, events) {
  context.vars.email = `user_${Date.now()}_${Math.random()}@test.com`;
}

async function signRequest(requestParams, context, events) {
  requestParams.headers = { ...requestParams.headers, "X-Sig": "abc" };
}

async function logErrors(requestParams, response, context, events) {
  if (response.statusCode >= 500) console.log(response.body);
}
```

Artillery 2 supports async functions. Older code uses a `done`/`next` callback as the last argument instead, which still works.

## 77: How do you create custom metrics in Artillery?

Use the `events` emitter in a processor function:

```javascript
async function afterCheckout(requestParams, response, context, events) {
  events.emit("counter", "orders.created", 1);
  events.emit(
    "histogram",
    "orders.total_amount",
    JSON.parse(response.body).total,
  );
  events.emit("rate", "orders.attempts");
}
module.exports = { afterCheckout };
```

Counters are summed, histograms get min, max, median, p95 and p99, and rates show events per second. They appear in the report next to the built-in metrics.

## 78: What is the Artillery expect plugin?

It adds assertions to requests, similar to checks in k6:

```yaml
config:
  plugins:
    expect: {}
scenarios:
  - flow:
      - get:
          url: "/products/1"
          expect:
            - statusCode: 200
            - contentType: json
            - hasProperty: id
```

Failed expectations are counted in the report. Keep in mind that a failed expectation can end that VU's scenario early (depending on the plugin settings), which changes how much load is generated.

## 79: How do you set pass/fail criteria in Artillery?

Use `config.ensure`. If a condition fails, Artillery exits with a non-zero code, so CI fails.

```yaml
config:
  ensure:
    thresholds:
      - http.response_time.p95: 300
      - http.response_time.p99: 800
    conditions:
      - expression: "http.response_time.p95 < 300 and http.request_rate > 50"
    maxErrorRate: 1
```

`thresholds` check a metric against a maximum, `conditions` allow more complex expressions, and `maxErrorRate` is a percentage of failed VUs.

## 80: How do you get per-endpoint metrics in Artillery?

By default Artillery reports response times for all requests together. Enable the `metrics-by-endpoint` plugin to split them:

```yaml
config:
  plugins:
    metrics-by-endpoint:
      useOnlyRequestNames: true
scenarios:
  - flow:
      - get:
          url: "/products/{{ id }}"
          name: "GET /products/:id"
```

With `useOnlyRequestNames`, dynamic URLs are grouped by the `name` you give, so you don't get one metric per product ID.

## 81: How do loops and conditions work in Artillery flows?

```yaml
flow:
  - loop:
      - get:
          url: "/products/{{ $loopElement }}"
    over:
      - 101
      - 102
      - 103
  - loop:
      - get:
          url: "/feed?page={{ $loopCount }}"
    count: 5
  - get:
      url: "/admin"
      ifTrue: "isAdmin"
```

`count` repeats a fixed number of times, `over` iterates a list, and `$loopCount` is the current index. `ifTrue` runs a request only when the expression is true.

## 82: What are before, after, beforeScenario and afterScenario in Artillery?

- Top-level `before` and `after` sections run a flow once, before and after the whole test. A common use is getting one auth token in `before` and making it available to every VU.
- `beforeScenario` and `afterScenario` are hooks on a scenario that call processor functions at the start and end of each VU's run.

```yaml
before:
  flow:
    - post:
        url: "/auth"
        json: { user: "admin", pass: "secret" }
        capture:
          - json: "$.token"
            as: "token"
scenarios:
  - beforeScenario: "pickUser"
    flow:
      - get:
          url: "/me"
          headers:
            Authorization: "Bearer {{ token }}"
```

## 83: What does maxVusers do in Artillery?

Artillery adds new VUs at the arrival rate whether or not old ones are done. If the server slows down, VUs pile up and the load generator can run out of memory. `maxVusers` sets a cap on how many can be active at the same time in a phase:

```yaml
phases:
  - duration: 300
    arrivalRate: 100
    maxVusers: 2000
```

Once the cap is reached, new arrivals are skipped. That protects the generator, but it also means you're no longer sending the planned load, so watch for it in the results.

## 84: What HTTP settings can you tune in Artillery?

Under `config.http`:

```yaml
config:
  http:
    timeout: 10 # seconds before a request fails with ETIMEDOUT
    pool: 50 # share a pool of 50 connections between all VUs
    extendedMetrics: true # report DNS, TCP, TLS and TTFB timings
```

By default each VU opens its own connections, which is realistic for browsers. Setting `pool` makes sense when you simulate a few backend services that reuse connections. There is also `config.tls.rejectUnauthorized: false` for self-signed certificates in test environments.

## 85: How do you use secrets and environment variables in Artillery?

Reference them with `$env` in templates and pass them from the shell or a `.env` file:

```yaml
config:
  target: "{{ $env.TARGET_URL }}"
  defaults:
    headers:
      x-api-key: "{{ $env.API_KEY }}"
```

```bash
API_KEY=xyz artillery run test.yml
artillery run --dotenv .env test.yml
```

Never commit real secrets in the YAML. Older scripts use `$processEnvironment`, which is the legacy name for the same thing.

## 86: How do you send Artillery metrics to Datadog, Prometheus or other tools?

Use the built-in `publish-metrics` plugin:

```yaml
config:
  plugins:
    publish-metrics:
      - type: datadog
        apiKey: "{{ $env.DD_API_KEY }}"
        prefix: "artillery."
        tags:
          - "service:checkout"
      - type: prometheus
        pushgateway: "http://pushgateway:9091"
```

It supports Datadog, Prometheus Pushgateway, CloudWatch, New Relic, Honeycomb, Splunk, Dynatrace and OpenTelemetry. Seeing load test metrics next to your server metrics in one dashboard makes analysis much easier.

## 87: How do you run Artillery in a CI pipeline?

Install it and run the test. A failed `ensure` check makes Artillery exit with a non-zero code.

```yaml
jobs:
  load-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
      - run: npm ci
      - run: npx artillery run --output report.json tests/load/smoke.yml
        env:
          TARGET_URL: ${{ vars.STAGING_URL }}
      - uses: actions/upload-artifact@v4
        with:
          name: artillery-report
          path: report.json
```

Pin the Artillery version in `package.json` so results don't change because of a tool update.

## 88: How do you test WebSockets with Artillery?

Use the `ws` engine on the scenario:

```yaml
config:
  target: "wss://chat.example.com"
  phases:
    - duration: 60
      arrivalRate: 10
scenarios:
  - engine: ws
    flow:
      - send: '{"type":"join","room":"general"}'
      - think: 1
      - loop:
          - send: '{"type":"message","text":"hello"}'
          - think: 2
        count: 10
```

There is also a `socketio` engine for Socket.IO servers, which supports emitting events and waiting for acknowledgments.

## 89: What is Artillery Cloud and how do you view reports?

Artillery Cloud is the hosted dashboard for Artillery results. You send a run to it with `--record`:

```bash
artillery run --record --key $ARTILLERY_CLOUD_API_KEY test.yml
```

It shows charts, compares runs and lets you share results with the team. The old `artillery report report.json` command that made a local HTML file is legacy. It still exists but is no longer the recommended way. Without the cloud, you can push metrics to your own tools with `publish-metrics`.

## 90: Why do you ramp up load gradually instead of starting at full load?

Starting at full load at once creates an artificial spike: caches are cold, connection pools are empty, autoscaling hasn't started and JIT compilers haven't warmed up. The first minute will look terrible for reasons that don't happen in real life.

A ramp-up lets you see at which load level things start to degrade, which is much more useful than a single number. Unless you are running a spike test on purpose, always ramp up.

## 91: How do you build a realistic workload model?

Start from production data: access logs, APM or analytics. Find:

- Which endpoints are called and in what ratio (for example 70% browse, 20% search, 10% checkout).
- Peak RPS and how traffic grows during the day.
- Typical session length and think times.
- Data spread: how many different users, products and search terms.

Then turn that into scenarios with weights (Artillery) or separate k6 scenarios with their own rates. A test that hits only one endpoint with one ID mostly tests your cache.

## 92: How do you estimate how many VUs you need?

Use Little's Law: concurrency = throughput × time in the system.

If you need 200 iterations per second and one iteration takes 0.5 s of requests plus 2 s of think time, you need about `200 × 2.5 = 500` VUs.

For k6 arrival-rate executors, set `preAllocatedVUs` close to that number and `maxVUs` with some headroom, because when the server slows down each iteration takes longer and needs more VUs.

## 93: How do you debug a k6 script?

- Run with one VU and one iteration: `k6 run --vus 1 --iterations 1 script.js`.
- See the full requests and responses: `k6 run --http-debug=full script.js`.
- Use `console.log()` for values like tokens or IDs.
- Check `res.status`, `res.error` and `res.error_code` for network errors.
- Use `k6 inspect script.js` to see the final resolved options.

Fix the script with tiny loads first, then scale up.

## 94: How do you debug an Artillery test?

Turn on debug logs with the `DEBUG` environment variable:

```bash
DEBUG=http artillery run test.yml             # requests
DEBUG=http,http:response artillery run test.yml   # requests and responses
DEBUG=http:capture artillery run test.yml     # capture results
```

Use a tiny phase like `duration: 1, arrivalCount: 1` while debugging, and add `- log: "token is {{ token }}"` steps in the flow to print variables.

## 95: How do you know if the load generator is the bottleneck?

Watch the machine running k6 or Artillery, not just the server. Signs of trouble:

- CPU on the generator is close to 100%.
- Memory keeps growing or the process gets killed.
- Errors like "too many open files" or "cannot assign requested address".
- Artillery prints a high CPU warning.
- `http_req_blocked` or `http_req_connecting` grows while the server looks idle.

Fixes: raise `ulimit -n`, widen the local port range, use a bigger machine, or split the load across several machines.

## 96: What should you monitor on the system under test during a load test?

Load test numbers tell you that something is slow, server metrics tell you why. Watch:

- CPU, memory, GC pauses and event loop lag on app servers.
- Database: active connections, slow queries, locks, CPU, IOPS.
- Cache hit rate, queue depth, thread or connection pool usage.
- Load balancer metrics: 5xx counts, target response time, surge queue.
- Autoscaling events and container restarts.

Put these dashboards next to the load test results, using the same time window.

## 97: How do caches affect load test results?

If every VU requests the same product with the same parameters, you mostly test the CDN or Redis cache, and the results look much better than reality. On the other hand, a test against a freshly started system with empty caches looks much worse than reality.

Use a realistic spread of IDs and search terms, include a warm-up period, and know which layer each request actually reaches. Check cache hit rates on the server during the test.

## 98: How do you load test an API that has rate limiting?

You have two different goals:

1. **Test the app behind the limiter:** ask the ops team to allowlist the load generator IPs, use a special test API key with a higher limit, or turn the limit up in the test environment.
2. **Test the limiter itself:** send traffic above the limit on purpose and check that you get 429 responses with correct `Retry-After` headers and that the backend stays healthy.

Don't mix them. Without a plan, a load test that hits a rate limit just measures how fast your API returns 429.

## 99: How do you load test a GraphQL API?

GraphQL is usually a POST with a JSON body, so it works the same way in both tools:

```javascript
const query = `query Product($id: ID!) { product(id: $id) { id name price } }`;

const res = http.post(
  `${BASE}/graphql`,
  JSON.stringify({ query, variables: { id: "42" } }),
  {
    headers: { "Content-Type": "application/json" },
    tags: { name: "gql:Product" },
  },
);
check(res, { "no errors": (r) => !r.json("errors") });
```

Two things to watch: GraphQL often returns 200 even when the query failed, so check the `errors` field. And all queries go to one URL, so tag each one with the operation name, or all the latency numbers get mixed together.

## 100: How do you test file uploads in k6 and Artillery?

In k6, read the file in the init context and send it with `http.file()`:

```javascript
const img = open("./photo.jpg", "b");

export default function () {
  http.post(`${BASE}/upload`, {
    file: http.file(img, "photo.jpg", "image/jpeg"),
    title: "test",
  });
}
```

In Artillery, use `formData` with `fromFile`:

```yaml
- post:
    url: "/upload"
    formData:
      title: "test"
      file:
        fromFile: "./photo.jpg"
```

Big files use a lot of bandwidth and memory on the generator, so keep an eye on `data_sent` and the network limit of the machine.

# Advanced Questions (101-150)

## 101: What is the difference between an open and a closed workload model?

In a **closed model**, a fixed number of users loop: send a request, wait for the response, think, repeat. New work only starts when old work finishes. k6 `constant-vus` and `ramping-vus` work this way.

In an **open model**, new users arrive at a set rate no matter how the system is doing, like real visitors on a public website. k6 arrival-rate executors and Artillery phases work this way.

The difference matters most when the server slows down. A closed model sends less traffic and hides the problem. An open model keeps the pressure on, so queues grow and you see what real users would see. Public web traffic is usually open. A closed model fits things like a fixed pool of workers or internal clients.

## 102: What is coordinated omission and how does it affect results?

Coordinated omission happens when the load tool waits for slow responses before sending the next request, so it "agrees" with the server to send less traffic exactly when the server struggles. The slow period gets fewer samples, and the percentiles look much better than what users really experienced.

Example: a VU sends a request every second, but one request takes 10 seconds. A real user stream would have sent 9 more requests during that time, all of which would have been slow. The closed-model test simply never sends them.

Using arrival-rate executors in k6, or Artillery's arrival-based phases, avoids most of this. Also watch `dropped_iterations` in k6, because dropped work is a form of the same problem.

## 103: How does k6 run JavaScript internally?

k6 is written in Go. JavaScript runs in Sobek, a pure-Go JS engine (a fork of goja), not in V8 or Node.js. Each VU gets its own separate JS runtime, so VUs share no memory, except through special objects like `SharedArray`.

The JS code looks synchronous, but `http.get()` hands the work to Go's networking code, which is fast and runs in parallel across VUs. Because there's no V8 JIT, heavy JS logic (big JSON parsing, crypto in pure JS) is slower than in Node.js and can make the generator CPU-bound. Keep per-iteration JS work small.

## 104: How do you reduce memory usage in a large k6 test?

- Use `SharedArray` for test data instead of normal arrays.
- Set `discardResponseBodies: true` and only keep bodies where you need them with `responseType: 'text'` on that request.
- Prefer arrival-rate executors so you don't need thousands of idle VUs.
- Group dynamic URLs with a `name` tag so you don't create thousands of metric series.
- For very long soak tests, run with `--no-thresholds --no-summary` and send metrics to an output instead, because k6 keeps trend samples in memory to calculate the end-of-test percentiles.
- Avoid big imported libraries, since each VU loads its own copy.

```javascript
export const options = { discardResponseBodies: true };

export default function () {
  const res = http.get(`${BASE}/me`, { responseType: "text" });
  check(res, { "has id": (r) => r.json("id") });
  http.get(`${BASE}/feed`); // body thrown away
}
```

## 105: How do you run k6 across multiple machines?

There are three common ways:

1. **Grafana Cloud k6:** `k6 cloud run script.js` runs the test on managed infrastructure in different regions.
2. **k6-operator on Kubernetes:** you create a `TestRun` resource with a `parallelism` value, and the operator starts that many k6 pods, each running a part of the load.
3. **By hand:** run k6 on several machines with `--execution-segment` so each one takes a slice of the load.

```yaml
apiVersion: k6.io/v1alpha1
kind: TestRun
metadata:
  name: checkout-peak
spec:
  parallelism: 4
  script:
    configMap:
      name: checkout-test
      file: test.js
```

In every case, send metrics to one central place, because each instance only knows about its own share.

## 106: What are execution segments in k6?

An execution segment tells one k6 instance which fraction of the total load to run. Each instance runs the same script and options but takes only its slice of VUs and iterations.

```bash
# machine 1
k6 run --execution-segment "0:1/3" --execution-segment-sequence "0,1/3,2/3,1" script.js
# machine 2
k6 run --execution-segment "1/3:2/3" --execution-segment-sequence "0,1/3,2/3,1" script.js
# machine 3
k6 run --execution-segment "2/3:1" --execution-segment-sequence "0,1/3,2/3,1" script.js
```

The sequence makes sure the slices split evenly, so 100 VUs across three machines become 34, 33 and 33 without rounding errors. The k6-operator does this for you.

## 107: How does Artillery run distributed tests?

Artillery can run the same test from many workers inside your own AWS account, without any servers to manage:

```bash
artillery run-fargate --region us-east-1 --count 10 test.yml
artillery run-lambda --region eu-west-1 --count 20 test.yml
```

`--count` is the number of workers, and each one runs the full phase configuration. So `arrivalRate: 50` with `--count 10` gives about 500 new VUs per second in total. Artillery collects metrics from all workers and merges them into one report. Fargate suits long and heavy tests. Lambda starts fast but has a 15-minute time limit per function.

## 108: How does Artillery model VUs, and how is that different from k6?

In Artillery, a VU is created by an arrival, picks one scenario, runs it once and then exits. Load is defined by how many VUs arrive per second, not by how many are alive. Concurrency is a result: arrival rate × session length.

In k6 with VU-based executors, a VU is a long-lived worker that loops the same function. So "100 VUs" means very different things in each tool. In Artillery it may be 100 arrivals per second with each staying 30 seconds (3,000 concurrent). In k6 it's 100 loops running in parallel.

When moving a test between the tools, compare request rates and concurrency, not VU counts.

## 109: Why can an Artillery load generator distort results, and how do you notice?

Artillery runs on Node.js. All VUs in a worker share one event loop. If the CPU is busy (parsing large JSON, heavy processor functions, too many VUs), timers fire late and response callbacks wait in the queue. The measured response time then includes time the generator spent busy, not just the server.

Artillery 2 spreads the load across worker threads to use several CPU cores, and it prints a warning when CPU usage gets high. If you see that warning, the numbers are suspect. Lower the load per machine, make processor functions cheaper, or use Fargate or Lambda workers.

## 110: What are xk6 extensions and when do you need them?

xk6 is a tool for building a custom k6 binary with extensions written in Go. They add things the core doesn't have: protocols (Kafka, SQL databases, Redis, MQTT), outputs (other metrics backends) or extra JS APIs.

```bash
xk6 build --with github.com/grafana/xk6-sql --with github.com/grafana/xk6-sql-driver-postgres
./k6 run db-test.js
```

Newer k6 versions can also resolve some official extensions automatically when the script imports them. The trade-off is that you maintain your own binary, have to keep its versions in sync, and community extensions may lag behind k6 releases.

## 111: How do you run browser-based load tests in k6?

Use the `k6/browser` module. It drives a real Chromium browser with a Playwright-like async API and records Web Vitals (`browser_web_vital_lcp`, `browser_web_vital_cls` and others).

```javascript
import { browser } from "k6/browser";
import { check } from "k6";

export const options = {
  scenarios: {
    ui: {
      executor: "shared-iterations",
      vus: 2,
      iterations: 10,
      options: { browser: { type: "chromium" } },
    },
  },
};

export default async function () {
  const page = await browser.newPage();
  try {
    await page.goto("https://test.k6.io/my_messages.php");
    await page.locator('input[name="login"]').type("admin");
    await page.locator('input[name="password"]').type("123");
    await Promise.all([
      page.waitForNavigation(),
      page.locator('input[type="submit"]').click(),
    ]);
    check(await page.locator("h2").textContent(), {
      "logged in": (t) => t === "Welcome, admin!",
    });
  } finally {
    await page.close();
  }
}
```

Browsers are very heavy, so the usual pattern is a hybrid test: most load from a protocol-level HTTP scenario plus a few browser VUs to measure what users see while the backend is under load.

## 112: How does the Artillery Playwright engine work?

You write the user flow as a Playwright function in the processor, and Artillery runs it in real browsers as each VU arrives:

```yaml
config:
  target: "https://shop.example.com"
  phases:
    - duration: 120
      arrivalRate: 1
  engines:
    playwright: {}
  processor: "./flows.js"
scenarios:
  - engine: playwright
    testFunction: "checkoutFlow"
```

```javascript
async function checkoutFlow(page, vuContext, events, test) {
  await test.step("open home page", async () => {
    await page.goto(vuContext.vars.target);
  });
  await test.step("add to cart", async () => {
    await page.getByRole("button", { name: "Add to cart" }).first().click();
  });
}
module.exports = { checkoutFlow };
```

It reports Core Web Vitals and the time of each `test.step`. You can reuse existing Playwright code, but each browser needs a lot of CPU and memory, so this is normally run on Fargate when you need more than a handful of browsers.

## 113: How do you design and run a breakpoint test?

The goal is to find the maximum load before the system fails. Increase load slowly and stop when it breaks:

```javascript
export const options = {
  scenarios: {
    breakpoint: {
      executor: "ramping-arrival-rate",
      startRate: 50,
      timeUnit: "1s",
      preAllocatedVUs: 200,
      maxVUs: 3000,
      stages: [{ duration: "30m", target: 2000 }],
    },
  },
  thresholds: {
    http_req_failed: [{ threshold: "rate<0.05", abortOnFail: true }],
    http_req_duration: [{ threshold: "p(95)<2000", abortOnFail: true }],
  },
};
```

Use an open model so the load really grows, and let thresholds stop the test. Note the RPS at which latency started to climb (the "knee"), not only where it fell over. Don't run it against shared or production systems without a plan, because the point is to break things.

## 114: What do you look for in a soak test?

A soak test runs normal load for several hours. You look for problems that only show up with time:

- Memory that keeps growing (leaks), followed by GC pauses or OOM restarts.
- Latency slowly going up while load stays flat.
- Connection pools, file descriptors or threads running out.
- Disks filling up with logs or temp files.
- Expiring tokens, certificate refresh, daily jobs and log rotation.
- Database tables and indexes growing, making queries slower.

Compare the first hour with the last hour. A flat line is a pass, a slope is a finding even if nothing has failed yet.

## 115: How do you design a spike test?

A spike test checks what happens when traffic jumps fast, for example after a push notification. Use an arrival-rate executor, because you want the rate to jump even if the server slows down:

```javascript
export const options = {
  scenarios: {
    spike: {
      executor: "ramping-arrival-rate",
      startRate: 50,
      timeUnit: "1s",
      preAllocatedVUs: 500,
      maxVUs: 5000,
      stages: [
        { duration: "2m", target: 50 },
        { duration: "10s", target: 1500 },
        { duration: "3m", target: 1500 },
        { duration: "10s", target: 50 },
        { duration: "5m", target: 50 },
      ],
    },
  },
};
```

Watch three things: how bad errors and latency get during the jump, how long autoscaling takes to catch up, and whether the system fully recovers after the spike ends. A system that stays broken after the spike is worse than one that is slow during it.

## 116: How do you find the bottleneck after a load test shows high latency?

Work from the outside in:

1. Split k6 timings: high `http_req_blocked`/`http_req_connecting` points to connection problems, high `http_req_waiting` to the server, high `http_req_receiving` to big responses or network limits.
2. Look at which endpoints are slow (tags or `metrics-by-endpoint`).
3. For each resource, check utilization, saturation and errors: CPU, memory, DB connections, thread pools, queues.
4. Use traces (APM, OpenTelemetry) to see where time goes inside a slow request.
5. Change one thing and re-test.

The first resource that hits 100% or starts queuing is usually the bottleneck, and fixing it often moves the limit to the next one.

## 117: What does it mean if http_req_blocked or http_req_connecting is high?

`http_req_blocked` is time waiting for a free TCP connection slot before the request could start. `http_req_connecting` is TCP connect time, and `http_req_tls_handshaking` is TLS setup time.

If these are high, the problem is often not the application:

- The server or load balancer is slow to accept new connections (backlog full).
- Keep-alive is disabled, so every request opens a new connection and TLS handshake.
- The load generator ran out of ephemeral ports or file descriptors.

Compare them with `http_req_waiting`. If waiting is low but blocked/connecting is high, look at networking and connection reuse before you touch the code.

## 118: How does connection reuse affect the realism of a load test?

By default k6 reuses connections within a VU (keep-alive), and Artillery gives each VU its own connections. Real browsers reuse connections for a while, and backend services usually use long-lived pools.

If your test reuses connections too much, you never test TLS handshakes or the load balancer's new-connection rate. If it reuses too little, you test mostly handshakes. Pick based on the clients you model. In k6 you can use `noConnectionReuse` or `noVUConnectionReuse`, and in Artillery `config.http.pool` changes how connections are shared. Also remember HTTP/2 multiplexes many requests on one connection, which changes the picture again.

## 119: What problems appear when load testing through a load balancer or CDN?

- **Few source IPs:** all traffic comes from one or two machines. Load balancers with IP-based stickiness or hashing can send everything to one backend, so other instances stay idle.
- **DNS caching:** the generator may resolve the hostname once and keep hitting the same IPs while the load balancer scales out. k6 has a `dns` option to control TTL and selection.
- **WAF and DDoS protection:** your test can get blocked or challenged.
- **CDN caching:** you test the CDN, not your origin.

Decide on purpose which layer you want to test, and coordinate allowlists with the team that owns the edge.

## 120: Why can't you average p95 values from several load generators?

Percentiles don't add up. If machine A has p95 = 200 ms with 10,000 requests and machine B has p95 = 800 ms with 100 requests, the average of 500 ms is wrong. The real combined p95 is close to 200 ms.

To get correct percentiles across machines you need the raw samples or mergeable histograms. Grafana Cloud k6 and Artillery's distributed runs handle this for you. When you use your own Prometheus with k6, send trends as native histograms (`K6_PROMETHEUS_RW_TREND_AS_NATIVE_HISTOGRAM=true`) so they can be merged correctly.

## 121: How do you detect performance regressions in CI without flaky results?

- Run against a stable, dedicated environment, not a shared staging that other teams are loading.
- Use a fixed arrival rate, so every run sends the same traffic.
- Run long enough to smooth out noise (several minutes, not 30 seconds).
- Compare with a baseline and allow a margin, like "p95 must not be more than 15% above the last 5 green runs".
- Track trends over time on a dashboard instead of trusting a single run.

Thresholds with fixed numbers catch big breaks. Comparing against history catches slow creep, which is how most regressions really happen.

## 122: How do you split load tests between pull requests and scheduled runs?

Full load tests are slow and need a production-like environment, so running them on every PR doesn't scale. A common setup:

- **On every PR:** a short smoke test (a few VUs, 1 minute) that checks the scripts still work and catches big slowdowns.
- **Nightly or on merge to main:** an average-load test with thresholds, against a stable environment.
- **Before big releases or events:** stress, spike and soak tests, reviewed by people.

Keep all of them in the same repo as the app, so a changed endpoint and its load script are updated together.

## 123: How do you manage test data for large load tests?

- **Uniqueness:** when tests create data (sign-ups, orders), make keys unique, for example `exec.vu.idInTest` plus `exec.scenario.iterationInTest` plus a run ID, so VUs don't collide on unique constraints.
- **Volume:** make the database size close to production. A query that is fast on 1,000 rows may be slow on 50 million.
- **Spread:** use many different users and products so caches and hot rows behave realistically.
- **Cleanup:** tag created data with the run ID and delete it in `teardown()` or with a separate job.
- **Reset:** for repeatable runs, restore the database from a snapshot before each test.

## 124: How do you handle authentication tokens that expire during a long test?

If tokens last 15 minutes and the soak test runs 4 hours, every VU will start failing at some point. Options:

- Check the expiry in the VU code and refresh the token when it's close.
- Log in again at the start of each iteration, if login is part of the real user flow.
- Ask for a longer-lived test token in the test environment.

```javascript
let token;
let expiresAt = 0;

export default function () {
  if (Date.now() > expiresAt - 60000) {
    const res = http.post(`${BASE}/token`, creds);
    token = res.json("access_token");
    expiresAt = Date.now() + res.json("expires_in") * 1000;
  }
  http.get(`${BASE}/orders`, { headers: { Authorization: `Bearer ${token}` } });
}
```

Variables in the init context are per VU, so each VU keeps its own token. Also watch out for the identity provider itself: thousands of logins per minute can hit its rate limits, and that's not what you wanted to test.

## 125: How can you load test safely in production?

Sometimes production is the only realistic environment. To do it safely:

- Start small and ramp slowly, with automatic abort thresholds (`abortOnFail` or `ensure`).
- Run in low-traffic hours, with the on-call team informed and watching.
- Mark test traffic with a header or user agent so it can be filtered in analytics and blocked quickly.
- Use test accounts, and make sure test orders never get charged, shipped or emailed.
- Keep a kill switch, and know how to roll back autoscaling or rate-limit changes.

Read-only flows are much safer than ones that write data.

## 126: What is special about load testing serverless backends like AWS Lambda?

- **Cold starts:** the first requests on new instances are slow, so ramp-up and spike results look different from steady load.
- **Concurrency limits:** accounts and functions have concurrency limits, and going over them gives throttling errors (429 at API Gateway).
- **Downstream limits:** Lambda scales fast, but your database doesn't. Thousands of functions can each open a connection and exhaust the database, which is why RDS Proxy or connection pooling matters.
- **Cost:** load tests on pay-per-request services cost real money, so estimate it first.

Watch platform metrics like throttles, concurrent executions and init duration next to the load test results.

## 127: How do you recognize database connection pool exhaustion in a load test?

Typical signs:

- Latency jumps suddenly at a certain load, while app CPU stays low.
- Errors like "timeout acquiring connection" or "too many clients" in the app logs.
- The database itself is not busy, but the app's pool shows all connections in use and requests waiting.

Fixes include right-sizing the pool (bigger is not always better, the database has its own limit), making slow queries faster so connections are released sooner, adding a pooler like PgBouncer or RDS Proxy, and not holding a connection open during calls to other services.

## 128: How do you test autoscaling with a load test?

Design the test around the scaling rules:

1. Start below the scale-out threshold and record the baseline.
2. Ramp load at a speed similar to real traffic growth.
3. Measure how long it takes for new instances to become healthy and actually take traffic.
4. Look at errors and latency during that gap. This is the window where users suffer.
5. Ramp down and check scale-in doesn't drop active requests.

Typical findings: health checks that pass before the app is warm, cooldowns that are too long, or scaling on CPU when the real limit is memory or connections.

## 129: How do you load test gRPC services with k6?

Use the built-in `k6/net/grpc` module. Load the proto files in the init context and connect once per VU:

```javascript
import grpc from "k6/net/grpc";
import { check } from "k6";
import exec from "k6/execution";

const client = new grpc.Client();
client.load(["./protos"], "hello.proto");

export default function () {
  if (exec.vu.iterationInScenario === 0) {
    client.connect("grpc.example.com:443");
  }
  const res = client.invoke("hello.HelloService/SayHello", { greeting: "k6" });
  check(res, { "status OK": (r) => r && r.status === grpc.StatusOK });
}
```

Connecting in every iteration would mostly test connection setup, since gRPC uses long-lived HTTP/2 connections. If the server has reflection enabled, you can use `client.connect(addr, { reflect: true })` instead of loading proto files.

## 130: How do you load test WebSockets in k6?

Use the event-based `k6/websockets` module (it was `k6/experimental/websockets` in older versions). The legacy `k6/ws` module still works but blocks the VU while the socket is open.

```javascript
import { WebSocket } from "k6/websockets";
import { Counter } from "k6/metrics";
import { setInterval, clearInterval, setTimeout } from "k6/timers";

const received = new Counter("ws_messages_received");

export default function () {
  const ws = new WebSocket("wss://chat.example.com/socket");

  ws.onopen = () => {
    ws.send(JSON.stringify({ type: "join", room: "general" }));
    const id = setInterval(
      () => ws.send(JSON.stringify({ type: "ping" })),
      5000,
    );
    setTimeout(() => {
      clearInterval(id);
      ws.close();
    }, 60000);
  };
  ws.onmessage = () => received.add(1);
}
```

For WebSockets, the important numbers are often how many connections the server can hold open, message delivery time and memory per connection, not requests per second.

## 131: How do you load test an asynchronous, queue-based workflow?

When the API returns `202 Accepted` and the real work happens later in a worker, the HTTP response time tells you almost nothing. You need the end-to-end time.

Options:

- Poll a status endpoint until the job is done, and record the total time in a custom Trend.
- Have the worker store timestamps and analyze them after the test.
- Watch queue depth and consumer lag during the test. A queue that keeps growing means the workers can't keep up, even if the API looks fast.

```javascript
const jobTime = new Trend("job_end_to_end", true);

export default function () {
  const start = Date.now();
  const id = http.post(`${BASE}/reports`, body, params).json("id");
  let status = "pending";
  while (status === "pending" && Date.now() - start < 60000) {
    sleep(1);
    status = http
      .get(`${BASE}/reports/${id}`, { tags: { name: "GET /reports/:id" } })
      .json("status");
  }
  jobTime.add(Date.now() - start);
}
```

## 132: How can client timeouts and retries distort load test results?

If the load tool has a 60-second timeout but real clients give up after 5 seconds, your test counts very slow requests as successes. Match timeouts to real clients (k6 `timeout` param, Artillery `config.http.timeout`).

Retries are the other side. Real apps and SDKs often retry on errors, which multiplies load exactly when the server is struggling (a retry storm). If your test never retries, it won't show this. If it retries silently, the errors get hidden. Model the real retry policy on purpose and report retries as their own metric.

## 133: Why does latency suddenly shoot up at a certain load level?

This is queueing. While utilization of the busiest resource is low, requests barely wait. As it gets close to 100%, waiting time grows very fast, not linearly. Going from 70% to 90% busy can multiply the queue time several times.

On a graph of latency vs load, this shows as a flat line that suddenly bends up like a hockey stick. The bend is your practical capacity. Plan to run production well below it (often 60-70% of that point), because a small traffic increase near the bend causes a big latency jump.

## 134: What does it mean when throughput stops growing but latency keeps rising?

The system has hit its limit. Some resource (CPU, a DB lock, a connection pool, a single-threaded part) is fully used, so it can't finish more work per second. Extra load only makes the queue longer, so each request waits more.

In a closed-model test you see flat RPS and rising latency. In an open-model test you see rising latency, then timeouts and errors, and in k6 maybe `dropped_iterations`. The RPS where the curve goes flat is your max throughput for that setup.

## 135: What causes errors that only appear at high load, like 502, 504 or ECONNRESET?

- **502 Bad Gateway:** the proxy got a broken or no response from the app, often because the app crashed, restarted or closed a keep-alive connection that the proxy was about to reuse. A classic Node.js case is the app's `keepAliveTimeout` being shorter than the load balancer's idle timeout.
- **504 Gateway Timeout:** the app took longer than the proxy's timeout.
- **ECONNRESET:** a side closed the connection, often due to backlog overflow, idle timeouts or the process restarting.
- **EADDRNOTAVAIL / cannot assign requested address:** the load generator ran out of ephemeral ports.

Check proxy, load balancer and app logs at the same timestamps to see which layer dropped the request.

## 136: What should you watch on a Node.js server during a load test?

- **Event loop lag/utilization:** if the loop is busy, every request waits, even simple ones. `perf_hooks.monitorEventLoopDelay()` gives you this.
- **CPU per process:** one Node process uses one core for JS. If you have 8 cores and one process, you're using 1/8 of the machine.
- **Heap usage and GC pauses:** a growing heap points to leaks, and long GC pauses cause latency spikes.
- **Active handles and sockets:** to find connection leaks.
- **libuv thread pool:** `fs`, `crypto` and `dns.lookup` use a pool of 4 threads by default, which can become a hidden queue.

Synchronous work like big `JSON.parse`, `bcrypt` with sync calls or heavy regex shows up as event loop lag and high p99.

## 137: How do you connect load test requests to backend traces?

Send a trace context header with each request so your tracing backend (Tempo, Jaeger, Datadog) links the request to its server-side trace. Then you can jump from a slow k6 request straight to the trace that shows where the time went.

k6 has a jslib for this, or you can add a W3C `traceparent` header yourself:

```javascript
import { instrumentHTTP } from "https://jslib.k6.io/http-instrumentation-tempo/1.0.0/index.js";

instrumentHTTP({ propagator: "w3c" });

export default function () {
  http.get(`${BASE}/orders`); // gets a traceparent header automatically
}
```

Make sure your sampler keeps these traces, for example by sampling all requests with a specific test header.

## 138: How do you keep load test scripts and runs secure?

- Never hard-code tokens, passwords or API keys. Pass them as environment variables from the CI secret store.
- Use dedicated test accounts with minimal permissions, not real user or admin accounts.
- Don't print tokens with `console.log`, because logs end up in CI artifacts.
- Get written approval before testing any system you don't own. To a provider, an unannounced load test looks exactly like a DoS attack.
- Never point a test at third-party services like payment or email APIs without their permission. Mock them instead.
- Clean up test data that may contain fake personal info.

## 139: How do you build a workload model from production logs?

1. Pull access logs or APM data from a peak period.
2. Group requests by endpoint pattern (`/products/:id`, not every ID).
3. Count the share of each endpoint and the peak RPS per endpoint.
4. Look at session data: how many requests per session, in what order, with what gaps.
5. Look at parameter spread: how many distinct users, products, search terms.

Then decide your targets, for example "current peak × 2 for next year's sales event", and turn the ratios into scenario weights or separate arrival rates. Document where the numbers came from so you can update them later.

## 140: How do you design a good threshold strategy?

- Base thresholds on SLOs, not on what the current system happens to do.
- Set them per endpoint or flow with tags, since a search and a report export have very different normal times.
- Use percentiles (p95, p99) plus error rate. Averages and max values are too noisy or too forgiving.
- Exclude warm-up with `delayAbortEval` or by tagging the warm-up stage separately.
- Add thresholds on test health too: `dropped_iterations`, `checks` rate.
- Keep a small set of strict thresholds that fail the build, and look at everything else on dashboards.

```javascript
thresholds: {
  "http_req_duration{name:search}": ["p(95)<400", "p(99)<1000"],
  "http_req_duration{name:checkout}": ["p(95)<800"],
  http_req_failed: ["rate<0.001"],
  checks: ["rate>0.999"],
  dropped_iterations: ["count<10"],
},
```

## 141: How do you write a custom Artillery plugin?

A plugin is an npm package named `artillery-plugin-<name>` that exports a constructor. Artillery calls it with the script config and an event emitter, and you hook into events like `stats` to read metrics.

```javascript
// artillery-plugin-slow-alert/index.js
function SlowAlertPlugin(script, events) {
  const limit = script.config.plugins["slow-alert"].p95 || 500;
  events.on("stats", (stats) => {
    const p95 = stats.summaries?.["http.response_time"]?.p95;
    if (p95 > limit) console.log(`p95 ${p95}ms is above ${limit}ms`);
  });
}
module.exports.Plugin = SlowAlertPlugin;
```

```yaml
config:
  plugins:
    slow-alert:
      p95: 300
```

Plugins are how built-in features like `expect`, `ensure` and `publish-metrics` are implemented, so you can read their source as examples.

## 142: How do you stop a k6 test from code, and when should you?

Use `exec.test.abort()` from `k6/execution`. It stops the whole test right away and marks it as aborted.

```javascript
import exec from "k6/execution";

export function setup() {
  const res = http.get(`${BASE}/health`);
  if (res.status !== 200) {
    exec.test.abort(`target not healthy: ${res.status}`);
  }
}
```

Use it for cases where continuing makes no sense: the target is down at the start, login is broken, or data the test needs is missing. For "stop when errors get too high", use a threshold with `abortOnFail` instead, since that is easier to read and configure.

## 143: What is the externally-controlled executor in k6 used for?

It lets you change the load while the test is running, from the command line or the k6 REST API, instead of having it fixed in the script.

```javascript
export const options = {
  scenarios: {
    manual: {
      executor: "externally-controlled",
      vus: 10,
      maxVUs: 500,
      duration: "1h",
    },
  },
};
```

```bash
k6 run script.js
k6 scale --vus 100   # in another terminal
k6 pause
k6 resume
```

It's useful for exploratory testing, where an engineer slowly turns up load while watching dashboards. It doesn't work in distributed runs and isn't repeatable, so don't use it for CI.

## 144: How do you load test one microservice versus the whole system?

Testing a single service means hitting it directly, with its dependencies either real or mocked (WireMock, a simple stub server). It gives clean numbers about that service and finds its own limits fast.

Testing the whole system through the public API shows how services affect each other: shared databases, network hops, timeouts and retries between services, and which service fails first.

You need both. Single-service tests are cheap and can run often. End-to-end tests are expensive but find the problems that matter most in production. When you mock a dependency, give the mock realistic latency, or the service will look faster than it is.

## 145: Scenario: p99 latency spikes every few minutes while load is steady. How do you investigate?

A regular pattern points to something periodic, not to the load itself. Check:

- **GC pauses:** look at GC logs or heap metrics at the spike times.
- **Scheduled jobs:** cron jobs, cache refreshes, batch imports, backups.
- **Autoscaling:** new instances joining cold, or old ones being removed.
- **Cache expiry:** many keys with the same TTL expiring at once (cache stampede).
- **Connection recycling:** pools or load balancers closing connections on a timer.
- **Database:** checkpoints, vacuum, compaction.

Line up the spike timestamps with server metrics and logs. Once you find something that happens at the same times, you can test the fix by checking whether the pattern goes away.

## 146: Scenario: the load test passed, but production fell over at lower traffic. What went wrong?

Common reasons:

- The test hit cached or repeated data, while real users requested a much wider spread.
- The test database was small, and production queries scan far more rows.
- The traffic mix was wrong, for example the test had no slow search or export calls.
- The test bypassed the CDN, WAF or auth layer that production goes through.
- Production has noisy neighbours, background jobs or third-party calls that the test environment mocked.
- The test used a closed model, so it never pushed hard when things slowed down.

Compare the test with production metrics like requests per endpoint, cache hit rate and DB query patterns, find where they differ, and fix the model before trusting the next run.

## 147: Scenario: how would you prepare load tests for a Black Friday sale?

1. **Gather numbers:** last year's peak RPS per endpoint, conversion rate, marketing forecasts. Plan for a target like 2-3× last year's peak.
2. **Model the flows:** browse, search, product page, add to cart, checkout, with weights from analytics. Include the sale moment as a spike.
3. **Prepare the environment:** production-sized, with realistic catalog and user data, payment provider mocked.
4. **Run in order:** smoke, average load, peak load, spike at the sale start, then a soak for the length of the sale.
5. **Watch and fix:** DB, cache, queues, third-party limits, autoscaling speed. Re-test after every fix.
6. **Prepare for the day:** pre-scale, warm caches, have dashboards and a runbook ready.

The checkout flow gets the strictest thresholds, because that's where failures cost money.

## 148: How do you choose between k6 and Artillery for a team?

Think about the team and the system, not just features:

- **Team skills:** developers comfortable with JS code often like k6. Teams that prefer config files and Node.js like Artillery's YAML plus processors.
- **Scale:** k6 gets more load from one machine. Artillery scales out easily on your own AWS account with Fargate or Lambda.
- **Ecosystem:** Artillery processors can use any npm package. k6 needs bundled pure-JS code or xk6 extensions.
- **Observability stack:** k6 fits naturally with Grafana, Prometheus and Tempo. Artillery has many publish targets, including Datadog.
- **Browser tests:** if you already have Playwright tests, Artillery can reuse them. k6 has its own browser API.

Try both on one real flow for a day. The one your team actually maintains is the right one.

## 149: How do you make load test results trustworthy?

- Run a smoke test first, and make sure checks pass at low load.
- Confirm the generator is not the bottleneck (CPU, memory, ports).
- Confirm you sent the planned load: actual RPS vs target, `dropped_iterations`, `maxVusers` hits.
- Look at errors and understand every one of them.
- Repeat the test. If two runs differ a lot, find out why before reporting.
- Document the environment, versions, data size and config used.

A load test report without this context is easy to misread and can lead to wrong capacity decisions.

## 150: What are the most common mistakes in load testing?

- Testing one endpoint with one ID, so the cache answers everything.
- No think time, or using VU counts without knowing the RPS they produce.
- Using averages instead of percentiles.
- Ignoring errors because the latency "looks fine" (fast errors make latency look great).
- Running the generator on an overloaded laptop or on the same machine as the app.
- Starting at full load with no ramp-up.
- Not monitoring the server, so you know it was slow but not why.
- Testing a small staging environment and assuming production will scale the same way.
- Running a test once and treating the result as a fact.
