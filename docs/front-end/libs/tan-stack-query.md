# TanStack Query Interview Questions and Answers

_Last updated: November 25, 2026_

This file has 120 interview questions and answers about TanStack Query: 40 easy, 40 moderate and 40 advanced. The answers target TanStack Query v5 (the `@tanstack/react-query` package, 5.10x releases), and most code examples use React. Where a feature is experimental or comes from an older version, the answer says so.

## Table of Contents

- [Easy Questions (1-40)](#easy-questions-1-40)
- [Moderate Questions (41-80)](#moderate-questions-41-80)
- [Advanced Questions (81-120)](#advanced-questions-81-120)

### Easy Questions (1-40)

- [1: What is TanStack Query?](#1-what-is-tanstack-query)
- [2: What problems does TanStack Query solve?](#2-what-problems-does-tanstack-query-solve)
- [3: What is the difference between server state and client state?](#3-what-is-the-difference-between-server-state-and-client-state)
- [4: How do you install TanStack Query in a React project?](#4-how-do-you-install-tanstack-query-in-a-react-project)
- [5: What is the QueryClient?](#5-what-is-the-queryclient)
- [6: What does QueryClientProvider do?](#6-what-does-queryclientprovider-do)
- [7: What is useQuery?](#7-what-is-usequery)
- [8: What is a query key?](#8-what-is-a-query-key)
- [9: What is a query function?](#9-what-is-a-query-function)
- [10: What does useQuery return?](#10-what-does-usequery-return)
- [11: What are the possible values of status in a query?](#11-what-are-the-possible-values-of-status-in-a-query)
- [12: What is fetchStatus and how is it different from status?](#12-what-is-fetchstatus-and-how-is-it-different-from-status)
- [13: What is the difference between isPending and isLoading in v5?](#13-what-is-the-difference-between-ispending-and-isloading-in-v5)
- [14: What does isFetching mean?](#14-what-does-isfetching-mean)
- [15: How do you show an error from a query?](#15-how-do-you-show-an-error-from-a-query)
- [16: When is data defined in a query result?](#16-when-is-data-defined-in-a-query-result)
- [17: How does caching work in TanStack Query?](#17-how-does-caching-work-in-tanstack-query)
- [18: What does it mean that data is stale?](#18-what-does-it-mean-that-data-is-stale)
- [19: What is staleTime?](#19-what-is-staletime)
- [20: What is gcTime?](#20-what-is-gctime)
- [21: What was cacheTime and why was it renamed?](#21-what-was-cachetime-and-why-was-it-renamed)
- [22: Why is the default staleTime 0?](#22-why-is-the-default-staletime-0)
- [23: When does TanStack Query refetch data automatically?](#23-when-does-tanstack-query-refetch-data-automatically)
- [24: What does refetchOnWindowFocus do?](#24-what-does-refetchonwindowfocus-do)
- [25: What does refetchOnReconnect do?](#25-what-does-refetchonreconnect-do)
- [26: What does refetchOnMount do?](#26-what-does-refetchonmount-do)
- [27: How do you stop a query from running automatically?](#27-how-do-you-stop-a-query-from-running-automatically)
- [28: How do you refetch a query by hand?](#28-how-do-you-refetch-a-query-by-hand)
- [29: How many times does a failed query retry by default?](#29-how-many-times-does-a-failed-query-retry-by-default)
- [30: What is retryDelay?](#30-what-is-retrydelay)
- [31: What is a mutation in TanStack Query?](#31-what-is-a-mutation-in-tanstack-query)
- [32: How do you use useMutation?](#32-how-do-you-use-usemutation)
- [33: What is the difference between mutate and mutateAsync?](#33-what-is-the-difference-between-mutate-and-mutateasync)
- [34: What states can a mutation be in?](#34-what-states-can-a-mutation-be-in)
- [35: What callbacks does useMutation support?](#35-what-callbacks-does-usemutation-support)
- [36: What does invalidateQueries do?](#36-what-does-invalidatequeries-do)
- [37: Why do you usually invalidate queries after a mutation?](#37-why-do-you-usually-invalidate-queries-after-a-mutation)
- [38: Why are query keys arrays?](#38-why-are-query-keys-arrays)
- [39: How do you include variables in a query key?](#39-how-do-you-include-variables-in-a-query-key)
- [40: Does the order of items in a query key matter?](#40-does-the-order-of-items-in-a-query-key-matter)

### Moderate Questions (41-80)

- [41: How do you organize query keys and options in a bigger app?](#41-how-do-you-organize-query-keys-and-options-in-a-bigger-app)
- [42: What does the queryOptions helper do?](#42-what-does-the-queryoptions-helper-do)
- [43: Should you wrap useQuery in custom hooks?](#43-should-you-wrap-usequery-in-custom-hooks)
- [44: How do you write a dependent query?](#44-how-do-you-write-a-dependent-query)
- [45: How do you run several queries in parallel?](#45-how-do-you-run-several-queries-in-parallel)
- [46: What does the select option do?](#46-what-does-the-select-option-do)
- [47: What is the difference between initialData and placeholderData?](#47-what-is-the-difference-between-initialdata-and-placeholderdata)
- [48: How do you build paginated queries without the UI jumping to a loading state?](#48-how-do-you-build-paginated-queries-without-the-ui-jumping-to-a-loading-state)
- [49: How and when do you prefetch data?](#49-how-and-when-do-you-prefetch-data)
- [50: How does useInfiniteQuery work?](#50-how-does-useinfinitequery-work)
- [51: What is maxPages in infinite queries?](#51-what-is-maxpages-in-infinite-queries)
- [52: How do you do a simple optimistic update without touching the cache?](#52-how-do-you-do-a-simple-optimistic-update-without-touching-the-cache)
- [53: How do you do an optimistic update with rollback through the cache?](#53-how-do-you-do-an-optimistic-update-with-rollback-through-the-cache)
- [54: How do you update the cache with the response of a mutation instead of refetching?](#54-how-do-you-update-the-cache-with-the-response-of-a-mutation-instead-of-refetching)
- [55: How do query filters work in invalidateQueries and other methods?](#55-how-do-query-filters-work-in-invalidatequeries-and-other-methods)
- [56: What does refetchType do in invalidateQueries?](#56-what-does-refetchtype-do-in-invalidatequeries)
- [57: Why would you return the invalidation promise from onSuccess?](#57-why-would-you-return-the-invalidation-promise-from-onsuccess)
- [58: What is the difference between callbacks on useMutation and callbacks on mutate?](#58-what-is-the-difference-between-callbacks-on-usemutation-and-callbacks-on-mutate)
- [59: What is useMutationState used for?](#59-what-is-usemutationstate-used-for)
- [60: How do you make mutations run one after another instead of in parallel?](#60-how-do-you-make-mutations-run-one-after-another-instead-of-in-parallel)
- [61: How do you show a global loading indicator?](#61-how-do-you-show-a-global-loading-indicator)
- [62: How do you handle query errors globally, for example with a toast?](#62-how-do-you-handle-query-errors-globally-for-example-with-a-toast)
- [63: Why were onSuccess, onError and onSettled removed from useQuery in v5?](#63-why-were-onsuccess-onerror-and-onsettled-removed-from-usequery-in-v5)
- [64: How do you use error boundaries with TanStack Query?](#64-how-do-you-use-error-boundaries-with-tanstack-query)
- [65: What is useSuspenseQuery?](#65-what-is-usesuspensequery)
- [66: How do you avoid retrying errors that will never succeed?](#66-how-do-you-avoid-retrying-errors-that-will-never-succeed)
- [67: How do you cancel a request in TanStack Query?](#67-how-do-you-cancel-a-request-in-tanstack-query)
- [68: How do you build a search box with TanStack Query?](#68-how-do-you-build-a-search-box-with-tanstack-query)
- [69: How do you poll until a condition is met?](#69-how-do-you-poll-until-a-condition-is-met)
- [70: How do you choose a staleTime?](#70-how-do-you-choose-a-staletime)
- [71: How do you set default options for all queries or for some queries?](#71-how-do-you-set-default-options-for-all-queries-or-for-some-queries)
- [72: What is skipToken?](#72-what-is-skiptoken)
- [73: What is networkMode?](#73-what-is-networkmode)
- [74: What can you do with the devtools when debugging?](#74-what-can-you-do-with-the-devtools-when-debugging)
- [75: What does the TanStack Query ESLint plugin check?](#75-what-does-the-tanstack-query-eslint-plugin-check)
- [76: How does TypeScript work with TanStack Query?](#76-how-does-typescript-work-with-tanstack-query)
- [77: How do you test components that use TanStack Query?](#77-how-do-you-test-components-that-use-tanstack-query)
- [78: What is the difference between refetch, invalidate, reset and remove?](#78-what-is-the-difference-between-refetch-invalidate-reset-and-remove)
- [79: How do you show a detail page instantly using data from a list query?](#79-how-do-you-show-a-detail-page-instantly-using-data-from-a-list-query)
- [80: What changed from TanStack Query v4 to v5?](#80-what-changed-from-tanstack-query-v4-to-v5)

### Advanced Questions (81-120)

- [81: How is TanStack Query built internally?](#81-how-is-tanstack-query-built-internally)
- [82: How does useQuery decide when to re-render a component?](#82-how-does-usequery-decide-when-to-re-render-a-component)
- [83: How are query keys turned into cache entries?](#83-how-are-query-keys-turned-into-cache-entries)
- [84: What is structural sharing and why does it matter?](#84-what-is-structural-sharing-and-why-does-it-matter)
- [85: How does garbage collection work in TanStack Query?](#85-how-does-garbage-collection-work-in-tanstack-query)
- [86: Why does cancelQueries matter in optimistic updates?](#86-why-does-cancelqueries-matter-in-optimistic-updates)
- [87: How do you handle several optimistic mutations running at the same time?](#87-how-do-you-handle-several-optimistic-mutations-running-at-the-same-time)
- [88: How do you keep mutations working when the app goes offline or the page reloads?](#88-how-do-you-keep-mutations-working-when-the-app-goes-offline-or-the-page-reloads)
- [89: How does persisting the query cache work, and what should you watch out for?](#89-how-does-persisting-the-query-cache-work-and-what-should-you-watch-out-for)
- [90: How does server-side rendering work with TanStack Query?](#90-how-does-server-side-rendering-work-with-tanstack-query)
- [91: How do you set up TanStack Query with the Next.js App Router?](#91-how-do-you-set-up-tanstack-query-with-the-nextjs-app-router)
- [92: How can you stream queries from the server instead of awaiting them?](#92-how-can-you-stream-queries-from-the-server-instead-of-awaiting-them)
- [93: What happens when hydrated data meets data that is already in the cache?](#93-what-happens-when-hydrated-data-meets-data-that-is-already-in-the-cache)
- [94: What can go wrong with TanStack Query on the server?](#94-what-can-go-wrong-with-tanstack-query-on-the-server)
- [95: How do you avoid request waterfalls with Suspense?](#95-how-do-you-avoid-request-waterfalls-with-suspense)
- [96: What are the gotchas with Suspense queries?](#96-what-are-the-gotchas-with-suspense-queries)
- [97: What is experimental_prefetchInRender?](#97-what-is-experimental_prefetchinrender)
- [98: What is streamedQuery used for?](#98-what-is-streamedquery-used-for)
- [99: How do you reduce re-renders in components that use queries?](#99-how-do-you-reduce-re-renders-in-components-that-use-queries)
- [100: How would you handle infinite lists with thousands of items?](#100-how-would-you-handle-infinite-lists-with-thousands-of-items)
- [101: A dashboard with 30 widgets sends a burst of requests every time the user switches tabs. How do you fix it?](#101-a-dashboard-with-30-widgets-sends-a-burst-of-requests-every-time-the-user-switches-tabs-how-do-you-fix-it)
- [102: How do you combine TanStack Query with WebSockets?](#102-how-do-you-combine-tanstack-query-with-websockets)
- [103: How do you update an infinite query cache after a mutation?](#103-how-do-you-update-an-infinite-query-cache-after-a-mutation)
- [104: How do you handle expired access tokens with TanStack Query?](#104-how-do-you-handle-expired-access-tokens-with-tanstack-query)
- [105: How do you design query keys so invalidation stays easy?](#105-how-do-you-design-query-keys-so-invalidation-stays-easy)
- [106: How does queryOptions make getQueryData and setQueryData type-safe?](#106-how-does-queryoptions-make-getquerydata-and-setquerydata-type-safe)
- [107: Should you transform data in the queryFn or in select?](#107-should-you-transform-data-in-the-queryfn-or-in-select)
- [108: How can you use TanStack Query outside React components?](#108-how-can-you-use-tanstack-query-outside-react-components)
- [109: How can you react to every change in the query cache?](#109-how-can-you-react-to-every-change-in-the-query-cache)
- [110: How do you keep the cache in sync across browser tabs?](#110-how-do-you-keep-the-cache-in-sync-across-browser-tabs)
- [111: How do you make focus and online refetching work in React Native?](#111-how-do-you-make-focus-and-online-refetching-work-in-react-native)
- [112: How do you test query logic without flaky tests?](#112-how-do-you-test-query-logic-without-flaky-tests)
- [113: How do you use TanStack Query with route loaders?](#113-how-do-you-use-tanstack-query-with-route-loaders)
- [114: When is TanStack Query not the right tool?](#114-when-is-tanstack-query-not-the-right-tool)
- [115: What edge cases do you need to know about setQueryData?](#115-what-edge-cases-do-you-need-to-know-about-setquerydata)
- [116: What are the pitfalls of disabled queries?](#116-what-are-the-pitfalls-of-disabled-queries)
- [117: Is it safe to use query data as a dependency in useEffect or useMemo?](#117-is-it-safe-to-use-query-data-as-a-dependency-in-useeffect-or-usememo)
- [118: How would you clear all data when the user logs out?](#118-how-would-you-clear-all-data-when-the-user-logs-out)
- [119: How does TanStack Query compare to SWR, RTK Query and Apollo Client?](#119-how-does-tanstack-query-compare-to-swr-rtk-query-and-apollo-client)
- [120: How would you design the data layer for an e-commerce front end with TanStack Query?](#120-how-would-you-design-the-data-layer-for-an-e-commerce-front-end-with-tanstack-query)

---

# Easy Questions (1-40)

## 1: What is TanStack Query?

TanStack Query (it used to be called React Query) is a library for fetching, caching and updating server data in front-end apps. You tell it how to get the data and give that data a key. It then stores the result in a cache, shares it between components, refetches it when it gets old and tracks loading and error states for you.

It does not make HTTP requests itself. You can use `fetch`, Axios, a GraphQL client or any function that returns a promise.

## 2: What problems does TanStack Query solve?

Without a library, every component that loads data needs its own `useEffect`, loading flag, error flag and some way to share the result. That code is easy to get wrong. TanStack Query takes care of:

- Caching results and sharing them between components
- Removing duplicate requests for the same data
- Refetching old data in the background
- Retrying failed requests
- Pagination and infinite scrolling
- Updating the cache after mutations
- Freeing memory for data nobody uses anymore

## 3: What is the difference between server state and client state?

Client state lives only in the browser and your app fully owns it: a modal being open, the current theme, form input. Server state lives on a server and you only hold a copy of it: a list of users, a product, an order.

Server state can change without your app knowing, so your copy can get old. It also has to be fetched asynchronously and can fail. TanStack Query is built for server state. For client state you still use `useState`, context, Zustand or similar tools.

## 4: How do you install TanStack Query in a React project?

Install the React adapter:

```bash
npm install @tanstack/react-query
```

The devtools are a separate package:

```bash
npm install @tanstack/react-query-devtools
```

TanStack Query v5 needs React 18 or newer.

## 5: What is the QueryClient?

The `QueryClient` is the main object of TanStack Query. It holds the query cache and the mutation cache, keeps the default options, and has methods for working with the cache directly, such as `invalidateQueries`, `setQueryData` and `prefetchQuery`.

```js
import { QueryClient } from "@tanstack/react-query";

const queryClient = new QueryClient();
```

Usually an app has one `QueryClient` on the client side.

## 6: What does QueryClientProvider do?

`QueryClientProvider` puts a `QueryClient` into React context, so every hook below it (`useQuery`, `useMutation`, `useQueryClient`) uses the same client and cache.

```jsx
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

const queryClient = new QueryClient();

export function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Todos />
    </QueryClientProvider>
  );
}
```

If you call a query hook outside the provider, you get an error saying no QueryClient is set.

## 7: What is useQuery?

`useQuery` is the hook you use to read data. You pass it a query key and a query function. It runs the function, caches the result under the key and returns the data along with status flags.

```jsx
import { useQuery } from "@tanstack/react-query";

function Todos() {
  const { data, isPending, isError, error } = useQuery({
    queryKey: ["todos"],
    queryFn: () => fetch("/api/todos").then((res) => res.json()),
  });

  if (isPending) return <p>Loading...</p>;
  if (isError) return <p>Error: {error.message}</p>;

  return (
    <ul>
      {data.map((todo) => (
        <li key={todo.id}>{todo.title}</li>
      ))}
    </ul>
  );
}
```

## 8: What is a query key?

A query key is an array that uniquely identifies a piece of data in the cache. TanStack Query uses it to store the data, find it again, share it between components and decide which queries to refetch or invalidate.

```js
useQuery({ queryKey: ["todos"], queryFn: fetchTodos });
useQuery({ queryKey: ["todo", 5], queryFn: () => fetchTodo(5) });
useQuery({
  queryKey: ["todos", { status: "done", page: 2 }],
  queryFn: fetchFilteredTodos,
});
```

In v5 the key must be an array. It can hold strings, numbers and plain objects, as long as everything can be turned into JSON.

## 9: What is a query function?

The query function (`queryFn`) is any function that returns a promise. It should resolve with the data or throw an error. TanStack Query calls it when it needs to fetch the data.

```js
async function fetchTodos() {
  const res = await fetch("/api/todos");
  if (!res.ok) throw new Error("Failed to load todos");
  return res.json();
}

useQuery({ queryKey: ["todos"], queryFn: fetchTodos });
```

The function must not resolve with `undefined`. Return `null` if there is no data.

## 10: What does useQuery return?

It returns an object with the data and a lot of state about the query. The most used fields are:

- `data`: the last successfully loaded data
- `error`: the error if the last fetch failed
- `status`: `'pending'`, `'error'` or `'success'`
- `fetchStatus`: `'fetching'`, `'paused'` or `'idle'`
- `isPending`, `isError`, `isSuccess`: shortcuts for `status`
- `isFetching`, `isLoading`, `isRefetching`: shortcuts for fetching states
- `refetch`: a function to fetch again by hand
- `dataUpdatedAt`, `failureCount`, `isStale`, `isPlaceholderData`

## 11: What are the possible values of status in a query?

`status` tells you whether you have data:

- `'pending'`: there is no data yet
- `'error'`: the last attempt failed and there is no successful data to replace it
- `'success'`: the query has data

In v4 the first state was called `'loading'`. v5 renamed it to `'pending'`.

## 12: What is fetchStatus and how is it different from status?

`fetchStatus` tells you whether the query function is running right now:

- `'fetching'`: the query function is running
- `'paused'`: it wanted to fetch but is waiting, usually because the device is offline
- `'idle'`: nothing is happening

`status` is about the data and `fetchStatus` is about the request. A query can be `success` and `fetching` at the same time, which is a background refetch. It can also be `pending` and `idle`, which happens when the query is disabled and has no data.

## 13: What is the difference between isPending and isLoading in v5?

`isPending` is true whenever there is no data yet, even if no request is running. `isLoading` is true only when there is no data and a request is actually running. It equals `isPending && isFetching`.

The difference shows up with disabled queries. A disabled query with no data is `isPending: true` forever, but `isLoading: false`. If you show a spinner on `isPending` for a disabled query, it spins forever.

## 14: What does isFetching mean?

`isFetching` is true whenever the query function is running, including the first load and every background refetch. Use it to show a small "updating" indicator while still showing the old data.

```jsx
const { data, isFetching } = useQuery({
  queryKey: ["todos"],
  queryFn: fetchTodos,
});

return (
  <>
    {isFetching && <span>Refreshing...</span>}
    <TodoList todos={data ?? []} />
  </>
);
```

## 15: How do you show an error from a query?

Check `isError` (or `status === 'error'`) and read `error`. The error is whatever your query function threw.

```jsx
const { data, isError, error } = useQuery({
  queryKey: ["user"],
  queryFn: fetchUser,
});

if (isError) {
  return <p>Could not load the user: {error.message}</p>;
}
```

By default TanStack Query retries 3 times on the client before it sets the error state, so the error shows up after a few seconds, not right away.

## 16: When is data defined in a query result?

`data` is defined when `status` is `'success'`. It stays defined during background refetches and even when a later refetch fails, so you keep showing the last good data. It is `undefined` while the query is pending, unless you pass `initialData` or `placeholderData`.

In TypeScript, checking `isSuccess` or `isPending` first narrows `data` to the right type.

## 17: How does caching work in TanStack Query?

Every query result is stored in the `QueryCache` under its query key. When another component asks for the same key, it gets the cached data right away. If the data is stale, TanStack Query also refetches it in the background and updates every component that uses it.

When no component uses a query anymore, the data stays in the cache for `gcTime` (5 minutes by default) and is then removed.

## 18: What does it mean that data is stale?

Stale data is data that TanStack Query thinks might be out of date. Stale data is still shown, but it gets refetched in the background when certain things happen: a new component mounts with that key, the window gets focus again, or the network reconnects.

Fresh data is never refetched by those triggers. Data turns from fresh to stale after `staleTime` has passed.

## 19: What is staleTime?

`staleTime` is how long, in milliseconds, data stays fresh after it was fetched. The default is `0`, so data is stale right away.

```js
useQuery({
  queryKey: ["countries"],
  queryFn: fetchCountries,
  staleTime: 1000 * 60 * 10, // fresh for 10 minutes
});
```

While data is fresh, new components that use the key get it from the cache with no request. Raising `staleTime` is the main way to cut down on refetches.

## 20: What is gcTime?

`gcTime` (garbage collection time) is how long an unused query stays in the cache. A query becomes unused, or inactive, when no mounted component is using it. After `gcTime` passes, the query and its data are removed. The default is 5 minutes.

```js
useQuery({
  queryKey: ["report", id],
  queryFn: () => fetchReport(id),
  gcTime: 1000 * 60 * 30, // keep for 30 minutes after last use
});
```

## 21: What was cacheTime and why was it renamed?

`cacheTime` is the v4 name for what is now `gcTime`. Many people thought it meant "how long data is cached and fresh", which was wrong, because freshness is controlled by `staleTime`. The option only controls when unused data is removed from memory, so v5 renamed it to `gcTime` to make that clear.

## 22: Why is the default staleTime 0?

The library picks safe defaults. With `staleTime: 0` it assumes the data on the server may have changed at any time, so it refetches whenever it gets a chance (on mount, focus or reconnect). That way users rarely see old data.

The trade-off is more network requests. Most apps should set a sensible `staleTime` for their data, either per query or in `defaultOptions`.

## 23: When does TanStack Query refetch data automatically?

Stale queries are refetched automatically when:

- A new component that uses the query mounts (`refetchOnMount`)
- The browser tab becomes visible again (`refetchOnWindowFocus`)
- The network reconnects (`refetchOnReconnect`)
- A `refetchInterval` you set fires
- You invalidate the query and it is in use

Fresh queries are skipped by the first three triggers.

## 24: What does refetchOnWindowFocus do?

When the user comes back to the tab, stale queries that are in use are refetched. This keeps data fresh when someone leaves a tab open for a long time. It is `true` by default.

```js
useQuery({
  queryKey: ["todos"],
  queryFn: fetchTodos,
  refetchOnWindowFocus: false,
});
```

You can set it to `false`, `true` or `'always'` (refetch even if the data is fresh).

## 25: What does refetchOnReconnect do?

When the browser goes from offline back to online, stale queries that are in use are refetched. The default is `true`. It accepts the same values as `refetchOnWindowFocus`: `true`, `false` or `'always'`.

## 26: What does refetchOnMount do?

When a component that uses a query mounts and the data is stale, the query is refetched. The default is `true`. With `false` the component uses whatever is cached and does not refetch on mount. With `'always'` it refetches on every mount, even if the data is fresh.

## 27: How do you stop a query from running automatically?

Use the `enabled` option. When it is `false`, the query does not fetch on mount, on focus or on any other automatic trigger.

```js
const { data } = useQuery({
  queryKey: ["user", userId],
  queryFn: () => fetchUser(userId),
  enabled: Boolean(userId),
});
```

A common use is waiting for some input, such as an ID, before fetching.

## 28: How do you refetch a query by hand?

Call the `refetch` function returned by `useQuery`.

```jsx
const { data, refetch } = useQuery({
  queryKey: ["todos"],
  queryFn: fetchTodos,
});

<button onClick={() => refetch()}>Reload</button>;
```

If you are outside the component, or want to refetch many queries, use `queryClient.invalidateQueries` or `queryClient.refetchQueries` instead.

## 29: How many times does a failed query retry by default?

On the client, a failed query is retried 3 times before it goes into the error state. On the server the default is 0 retries. You can change this with `retry`:

```js
useQuery({ queryKey: ["todos"], queryFn: fetchTodos, retry: 1 });
useQuery({ queryKey: ["todos"], queryFn: fetchTodos, retry: false });
```

`retry` also accepts a function, so you can decide based on the error.

## 30: What is retryDelay?

`retryDelay` sets how long to wait between retries. The default uses exponential backoff: 1 second, then 2, then 4, and so on, capped at 30 seconds.

```js
useQuery({
  queryKey: ["todos"],
  queryFn: fetchTodos,
  retryDelay: (attempt) => Math.min(1000 * 2 ** attempt, 30000),
});
```

You can also pass a fixed number like `retryDelay: 1000`.

## 31: What is a mutation in TanStack Query?

A mutation is an operation that changes data on the server: creating, updating or deleting something. Queries read data and run automatically. Mutations write data and only run when you call them, for example when a user clicks "Save".

## 32: How do you use useMutation?

Pass a `mutationFn` and call `mutate` when you want to run it.

```jsx
import { useMutation, useQueryClient } from "@tanstack/react-query";

function AddTodo() {
  const queryClient = useQueryClient();

  const mutation = useMutation({
    mutationFn: (title) =>
      fetch("/api/todos", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title }),
      }).then((res) => res.json()),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["todos"] });
    },
  });

  return (
    <button
      disabled={mutation.isPending}
      onClick={() => mutation.mutate("Buy milk")}
    >
      Add
    </button>
  );
}
```

## 33: What is the difference between mutate and mutateAsync?

`mutate` starts the mutation and returns nothing. Errors are handled by the mutation's `onError` and by the `error` field, so you don't need to catch anything.

`mutateAsync` returns a promise that resolves with the result or rejects with the error. It is useful when you need to wait for the result, for example in a form submit handler. You must handle the rejection yourself, or you get an unhandled promise rejection.

```js
try {
  const todo = await mutation.mutateAsync("Buy milk");
  navigate(`/todos/${todo.id}`);
} catch (error) {
  // already available as mutation.error too
}
```

## 34: What states can a mutation be in?

A mutation's `status` is one of:

- `'idle'`: not run yet, or reset
- `'pending'`: running
- `'error'`: failed
- `'success'`: finished

There are matching flags: `isIdle`, `isPending`, `isError`, `isSuccess`. In v4 the running state was called `'loading'`.

## 35: What callbacks does useMutation support?

- `onMutate(variables)`: runs before the mutation function. Whatever it returns is passed to the other callbacks, which is how optimistic updates store rollback data.
- `onSuccess(data, variables, onMutateResult)`: runs when it succeeds.
- `onError(error, variables, onMutateResult)`: runs when it fails.
- `onSettled(data, error, variables, onMutateResult)`: runs after success or failure.

Recent v5 releases also pass a last context argument that includes the `QueryClient`. You can also pass the same callbacks to `mutate` itself, for logic that belongs to one specific call.

## 36: What does invalidateQueries do?

`queryClient.invalidateQueries` marks matching queries as stale. If a matching query is currently used by a component, it is refetched right away. Inactive ones are refetched the next time they are used.

```js
// everything that starts with ['todos']
queryClient.invalidateQueries({ queryKey: ["todos"] });
```

It returns a promise that resolves when the refetches finish.

## 37: Why do you usually invalidate queries after a mutation?

After you change data on the server, the cached copies of that data are out of date. Invalidating the related queries makes TanStack Query refetch them, so the UI shows the new state. It is the simplest way to keep the cache in sync, because you don't have to work out how the change affects each cached list.

```js
useMutation({
  mutationFn: deleteTodo,
  onSuccess: () => queryClient.invalidateQueries({ queryKey: ["todos"] }),
});
```

## 38: Why are query keys arrays?

Arrays let you build keys from parts, which gives you a hierarchy. You can then invalidate or read groups of queries by a prefix.

```js
["todos"];
["todos", "list", { status: "done" }];
["todos", "detail", 5];
```

Invalidating `['todos']` hits all three, while invalidating `['todos', 'detail', 5]` hits only one.

## 39: How do you include variables in a query key?

Put every value the query function depends on into the key. When a value changes, the key changes, and TanStack Query fetches and caches that data separately.

```js
function useTodo(id) {
  return useQuery({
    queryKey: ["todo", id],
    queryFn: () => fetchTodo(id),
  });
}
```

If you leave a variable out of the key, different inputs share one cache entry and you see wrong data.

## 40: Does the order of items in a query key matter?

Yes, for array items. `['todos', 1, 'done']` and `['todos', 'done', 1]` are different keys. The order of properties inside an object does not matter, because keys are hashed with sorted object keys.

```js
// same key
["todos", { status: "done", page: 1 }];
["todos", { page: 1, status: "done" }];
```

# Moderate Questions (41-80)

## 41: How do you organize query keys and options in a bigger app?

Keep keys and query functions in one place per feature instead of typing arrays by hand in every component. A common pattern is a factory object built with the `queryOptions` helper:

```js
import { queryOptions } from "@tanstack/react-query";

export const todoQueries = {
  all: () => ["todos"],
  lists: () => [...todoQueries.all(), "list"],
  list: (filters) =>
    queryOptions({
      queryKey: [...todoQueries.lists(), filters],
      queryFn: () => fetchTodos(filters),
    }),
  detail: (id) =>
    queryOptions({
      queryKey: [...todoQueries.all(), "detail", id],
      queryFn: () => fetchTodo(id),
      staleTime: 30_000,
    }),
};

useQuery(todoQueries.detail(5));
queryClient.invalidateQueries({ queryKey: todoQueries.lists() });
```

You get one source of truth for keys, no typos, and the same options can be passed to `useQuery`, `prefetchQuery` or `ensureQueryData`.

## 42: What does the queryOptions helper do?

At runtime it just returns the object you pass in. Its value is in TypeScript: it lets you define `queryKey`, `queryFn` and other options once and reuse them, and it tags the query key with the data type. Because of that tag, `queryClient.getQueryData(todoQueries.detail(5).queryKey)` knows it returns a `Todo | undefined` without you writing a generic.

There is a matching `infiniteQueryOptions` for infinite queries and a `mutationOptions` helper for mutations.

## 43: Should you wrap useQuery in custom hooks?

Usually yes. A custom hook hides the key and the fetch logic, so components just say what they need.

```js
export function useTodo(id) {
  return useQuery({
    ...todoQueries.detail(id),
    enabled: id != null,
  });
}
```

Return the whole query result instead of picking a few fields, so callers still have access to `isFetching`, `error` and the rest. Many teams now export the `queryOptions` objects as well, because hooks can't be used in loaders, event handlers or `prefetchQuery`.

## 44: How do you write a dependent query?

A dependent query waits for data from another query. Disable it until the value it needs exists.

```js
const { data: user } = useQuery({
  queryKey: ["user", email],
  queryFn: () => getUserByEmail(email),
});

const userId = user?.id;

const { data: projects } = useQuery({
  queryKey: ["projects", userId],
  queryFn: () => getProjectsByUser(userId),
  enabled: !!userId,
});
```

Keep in mind that dependent queries run one after another, which is a request waterfall. If the server can give you both in one call, that is usually faster.

## 45: How do you run several queries in parallel?

If the number of queries is fixed, call `useQuery` several times. They all start at once.

If the number is dynamic, use `useQueries`:

```js
const results = useQueries({
  queries: userIds.map((id) => ({
    queryKey: ["user", id],
    queryFn: () => fetchUser(id),
  })),
  combine: (results) => ({
    users: results.map((r) => r.data).filter(Boolean),
    isPending: results.some((r) => r.isPending),
  }),
});
```

`combine` is optional. Without it you get an array of query results in the same order as `queries`.

## 46: What does the select option do?

`select` transforms or picks part of the data for one component. The cache still holds the full response, and other components using the same key are not affected.

```js
const { data: doneCount } = useQuery({
  queryKey: ["todos"],
  queryFn: fetchTodos,
  select: (todos) => todos.filter((t) => t.done).length,
});
```

The component re-renders only when the selected value changes, which can save renders. Pass a stable function (defined outside the component or wrapped in `useCallback`) so `select` doesn't run again on every render.

## 47: What is the difference between initialData and placeholderData?

`initialData` is real data. It goes into the cache, counts as `success` and is treated like fetched data, so `staleTime` applies to it. Use it when you really have the full data, for example from another query.

`placeholderData` is fake or temporary data. It is shown while the real fetch runs, but it is never written to the cache, and `isPlaceholderData` is `true`. The query always fetches.

```js
useQuery({
  queryKey: ["todo", id],
  queryFn: () => fetchTodo(id),
  placeholderData: () =>
    queryClient.getQueryData(["todos"])?.find((t) => t.id === id),
});
```

## 48: How do you build paginated queries without the UI jumping to a loading state?

Put the page into the key and use `placeholderData: keepPreviousData`. When the page changes, the old page stays on screen until the new one arrives, instead of going back to `pending`.

```jsx
import { keepPreviousData, useQuery } from "@tanstack/react-query";

function Projects() {
  const [page, setPage] = useState(1);
  const { data, isPlaceholderData, isFetching } = useQuery({
    queryKey: ["projects", page],
    queryFn: () => fetchProjects(page),
    placeholderData: keepPreviousData,
  });

  return (
    <>
      <ProjectList projects={data?.items ?? []} dimmed={isPlaceholderData} />
      <button
        disabled={isPlaceholderData || !data?.hasMore}
        onClick={() => setPage((p) => p + 1)}
      >
        Next
      </button>
    </>
  );
}
```

In v4 this was the `keepPreviousData: true` option. v5 removed that option.

## 49: How and when do you prefetch data?

Prefetch when you can guess what the user will need next: on hover over a link, on the page before a detail view, or for the next page of a list.

```jsx
function TodoLink({ id }) {
  const queryClient = useQueryClient();

  return (
    <Link
      to={`/todos/${id}`}
      onMouseEnter={() => queryClient.prefetchQuery(todoQueries.detail(id))}
    >
      Open
    </Link>
  );
}
```

`prefetchQuery` respects `staleTime`, so it does nothing if fresh data is already cached. It never throws and returns nothing, so it is safe to fire and forget. If you need the data back, use `fetchQuery` or `ensureQueryData`.

## 50: How does useInfiniteQuery work?

It loads data in pages and keeps all loaded pages under one key. You give it a starting page param and a function that returns the next page param from the last page.

```jsx
const { data, fetchNextPage, hasNextPage, isFetchingNextPage } =
  useInfiniteQuery({
    queryKey: ["posts"],
    queryFn: ({ pageParam }) => fetchPosts({ cursor: pageParam }),
    initialPageParam: null,
    getNextPageParam: (lastPage) => lastPage.nextCursor ?? undefined,
  });

const posts = data?.pages.flatMap((page) => page.items) ?? [];
```

`data` has two arrays: `pages` and `pageParams`. Returning `undefined` or `null` from `getNextPageParam` sets `hasNextPage` to `false`. In v5 `initialPageParam` is required.

## 51: What is maxPages in infinite queries?

`maxPages` limits how many pages are kept in the cache. When a new page is loaded and the limit is reached, the page at the other end is dropped. This keeps memory use and refetch cost under control for long feeds.

```js
useInfiniteQuery({
  queryKey: ["feed"],
  queryFn: ({ pageParam }) => fetchFeed(pageParam),
  initialPageParam: 0,
  getNextPageParam: (last) => last.next,
  getPreviousPageParam: (first) => first.prev,
  maxPages: 5,
});
```

Define `getPreviousPageParam` as well, so the user can scroll back to the pages that were dropped.

## 52: How do you do a simple optimistic update without touching the cache?

Use the mutation's `variables` while it is pending to show the new item right away. If it fails, the item disappears on its own, because nothing was written to the cache.

```jsx
const addTodo = useMutation({
  mutationFn: createTodo,
  onSettled: () => queryClient.invalidateQueries({ queryKey: ["todos"] }),
});

return (
  <ul>
    {todos.map((t) => (
      <li key={t.id}>{t.title}</li>
    ))}
    {addTodo.isPending && (
      <li style={{ opacity: 0.5 }}>{addTodo.variables.title}</li>
    )}
  </ul>
);
```

This works well when the optimistic UI is shown in one place. If other components need to see it, use `useMutationState` or update the cache.

## 53: How do you do an optimistic update with rollback through the cache?

Change the cache in `onMutate`, keep a snapshot, restore it in `onError`, and refetch in `onSettled`.

```js
useMutation({
  mutationFn: updateTodo,
  onMutate: async (newTodo) => {
    await queryClient.cancelQueries({ queryKey: ["todos"] });
    const previous = queryClient.getQueryData(["todos"]);

    queryClient.setQueryData(["todos"], (old = []) =>
      old.map((t) => (t.id === newTodo.id ? { ...t, ...newTodo } : t)),
    );

    return { previous };
  },
  onError: (_error, _newTodo, onMutateResult) => {
    queryClient.setQueryData(["todos"], onMutateResult.previous);
  },
  onSettled: () => queryClient.invalidateQueries({ queryKey: ["todos"] }),
});
```

`cancelQueries` stops any refetch that is in flight, so an old response can't overwrite your optimistic change.

## 54: How do you update the cache with the response of a mutation instead of refetching?

If the server returns the updated object, write it into the cache with `setQueryData`. This saves a request.

```js
useMutation({
  mutationFn: updateTodo,
  onSuccess: (updatedTodo) => {
    queryClient.setQueryData(["todo", updatedTodo.id], updatedTodo);
  },
});
```

Always update immutably: return a new object or array from the updater, never change `old` in place. Otherwise TanStack Query can't detect the change and components won't re-render.

## 55: How do query filters work in invalidateQueries and other methods?

Methods like `invalidateQueries`, `refetchQueries`, `cancelQueries` and `removeQueries` take filters:

- `queryKey`: matches every key that starts with this prefix
- `exact: true`: matches only the exact key
- `type`: `'active'`, `'inactive'` or `'all'`
- `stale`: only stale or only fresh queries
- `fetchStatus`: for example only queries that are fetching
- `predicate`: a function that gets the query and returns `true` or `false`

```js
queryClient.invalidateQueries({ queryKey: ["todos"], exact: true });

queryClient.invalidateQueries({
  predicate: (query) =>
    query.queryKey[0] === "todos" && query.state.data?.length > 100,
});
```

## 56: What does refetchType do in invalidateQueries?

It controls which of the matching queries are refetched right away. All matching queries are always marked stale.

- `'active'` (default): refetch only queries used by mounted components
- `'inactive'`: refetch only unused ones
- `'all'`: refetch both
- `'none'`: just mark them stale and refetch nothing

```js
queryClient.invalidateQueries({ queryKey: ["todos"], refetchType: "none" });
```

## 57: Why would you return the invalidation promise from onSuccess?

If `onSuccess` returns a promise, the mutation stays in the `pending` state until that promise resolves. So if you return `invalidateQueries`, the button stays disabled and the spinner keeps showing until the fresh data is loaded. That avoids a short moment where the mutation looks done but the list still shows old data.

```js
useMutation({
  mutationFn: addTodo,
  onSuccess: () => queryClient.invalidateQueries({ queryKey: ["todos"] }),
});
```

If you don't want to wait, call it without returning it (for example, wrap the body in braces).

## 58: What is the difference between callbacks on useMutation and callbacks on mutate?

Both run, and the `useMutation` ones run first. The difference is what they are for:

- `useMutation` callbacks are for logic that must always happen, such as invalidating queries. They run even if the component unmounts.
- `mutate` callbacks are for one specific call and its UI, such as closing a dialog or navigating. They do not run if the component unmounted before the mutation finished.

```js
const mutation = useMutation({
  mutationFn: createTodo,
  onSuccess: () => queryClient.invalidateQueries({ queryKey: ["todos"] }),
});

mutation.mutate(newTodo, { onSuccess: () => closeDialog() });
```

If you call `mutate` several times quickly, the `mutate` callbacks only fire for the last call.

## 59: What is useMutationState used for?

It gives you access to mutations from anywhere in the tree, not just the component that called `useMutation`. You usually filter by `mutationKey`.

```js
// in the form
useMutation({ mutationKey: ["addTodo"], mutationFn: createTodo });

// somewhere else, e.g. in the list
const pendingTodos = useMutationState({
  filters: { mutationKey: ["addTodo"], status: "pending" },
  select: (mutation) => mutation.state.variables,
});
```

This is how you show optimistic items in a list when the mutation runs in a different component.

## 60: How do you make mutations run one after another instead of in parallel?

By default, mutations run in parallel. If you give them the same `scope.id`, they run in order: the next one waits until the previous one is done.

```js
useMutation({
  mutationFn: saveDraft,
  scope: { id: "draft" },
});
```

This helps when the server must receive changes in order, for example several quick edits to the same document.

## 61: How do you show a global loading indicator?

`useIsFetching` returns how many queries are fetching right now, and `useIsMutating` does the same for mutations. Both accept filters.

```jsx
import { useIsFetching, useIsMutating } from "@tanstack/react-query";

function GlobalSpinner() {
  const fetching = useIsFetching();
  const mutating = useIsMutating();

  return fetching + mutating > 0 ? <TopBarSpinner /> : null;
}
```

## 62: How do you handle query errors globally, for example with a toast?

Pass callbacks to the `QueryCache` and `MutationCache` when you create the client. They run once per failed query or mutation, not once per component that uses it.

```js
import { MutationCache, QueryCache, QueryClient } from "@tanstack/react-query";

const queryClient = new QueryClient({
  queryCache: new QueryCache({
    onError: (error, query) => {
      // only toast for background refetches, the UI already shows first-load errors
      if (query.state.data !== undefined) {
        toast.error(`Something went wrong: ${error.message}`);
      }
    },
  }),
  mutationCache: new MutationCache({
    onError: (error) => toast.error(error.message),
  }),
});
```

This is also the replacement for the per-query `onError` callback that was removed from `useQuery` in v5.

## 63: Why were onSuccess, onError and onSettled removed from useQuery in v5?

They ran once per component that used the query, not once per fetch, which caused duplicated toasts and confusing bugs. They also did not run when data came from the cache, so people who synced query data into local state with `onSuccess` got out-of-sync UIs.

The replacements are: global callbacks on `QueryCache` for side effects like toasts, the `error` field in render for showing errors, and using the data directly instead of copying it into state. Mutations still have these callbacks.

## 64: How do you use error boundaries with TanStack Query?

Set `throwOnError` so the error is thrown during render and caught by the nearest error boundary. Use `QueryErrorResetBoundary` so a "Try again" button resets the failed queries.

```jsx
import { QueryErrorResetBoundary } from "@tanstack/react-query";
import { ErrorBoundary } from "react-error-boundary";

<QueryErrorResetBoundary>
  {({ reset }) => (
    <ErrorBoundary
      onReset={reset}
      fallbackRender={({ resetErrorBoundary }) => (
        <button onClick={resetErrorBoundary}>Try again</button>
      )}
    >
      <Todos />
    </ErrorBoundary>
  )}
</QueryErrorResetBoundary>;
```

`throwOnError` can be a function, for example `(error) => error.status >= 500`, so only server errors go to the boundary and the rest are shown inline. In v4 this option was called `useErrorBoundary`.

## 65: What is useSuspenseQuery?

It is a version of `useQuery` that works with React Suspense. While the data is loading, the component suspends and the nearest `<Suspense>` fallback is shown. Errors are thrown to the nearest error boundary. When the component renders, `data` is always defined.

```jsx
function Todo({ id }) {
  const { data } = useSuspenseQuery(todoQueries.detail(id));
  return <h1>{data.title}</h1>;
}

<Suspense fallback={<Spinner />}>
  <Todo id={5} />
</Suspense>;
```

It does not accept `enabled` or `placeholderData`. There are also `useSuspenseInfiniteQuery` and `useSuspenseQueries`.

## 66: How do you avoid retrying errors that will never succeed?

Pass a function to `retry`. It receives the failure count and the error, so you can stop on client errors such as 404 or 401.

```js
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      retry: (failureCount, error) => {
        if (error.status >= 400 && error.status < 500) return false;
        return failureCount < 3;
      },
    },
  },
});
```

For this to work, your query function has to throw an error that carries the status code.

## 67: How do you cancel a request in TanStack Query?

The query function receives an `AbortSignal`. Pass it to `fetch` or Axios. TanStack Query aborts it when the query is no longer needed (for example, the component unmounted while fetching or the key changed) or when you call `cancelQueries`.

```js
useQuery({
  queryKey: ["todos", search],
  queryFn: async ({ signal }) => {
    const res = await fetch(`/api/todos?q=${search}`, { signal });
    if (!res.ok) throw new Error("Request failed");
    return res.json();
  },
});

// manual cancel
queryClient.cancelQueries({ queryKey: ["todos"] });
```

If you don't read `signal`, the request still finishes and its result is stored. TanStack Query only aborts when you use it.

## 68: How do you build a search box with TanStack Query?

Debounce the input, put the debounced value in the key, and keep the old results while new ones load.

```jsx
function Search() {
  const [text, setText] = useState("");
  const debounced = useDebounce(text, 300);

  const { data, isFetching } = useQuery({
    queryKey: ["search", debounced],
    queryFn: ({ signal }) => searchProducts(debounced, { signal }),
    enabled: debounced.length > 1,
    placeholderData: keepPreviousData,
    staleTime: 60_000,
  });

  return (
    <>
      <input value={text} onChange={(e) => setText(e.target.value)} />
      {isFetching && <small>Searching...</small>}
      <Results items={data ?? []} />
    </>
  );
}
```

Each search term gets its own cache entry, so going back to an earlier term shows results right away.

## 69: How do you poll until a condition is met?

`refetchInterval` can be a function that receives the query. Return a number to keep polling or `false` to stop.

```js
useQuery({
  queryKey: ["job", jobId],
  queryFn: () => fetchJob(jobId),
  refetchInterval: (query) =>
    query.state.data?.status === "done" ? false : 2000,
});
```

By default polling pauses when the tab is in the background. Set `refetchIntervalInBackground: true` if it must keep going.

## 70: How do you choose a staleTime?

Ask how often the data changes and how bad it is to show an old version.

- Data that changes all the time (stock prices, chat): `0` or a few seconds, maybe with polling
- Typical app data (lists, profiles): something like 30 seconds to a few minutes
- Data that almost never changes (countries, feature config): `Infinity`

Set a reasonable default in `defaultOptions.queries.staleTime` and override it per query. With `Infinity` the data is fresh until you invalidate it. Recent v5 versions also accept `staleTime: 'static'`, which means the data is never refetched, not even by `invalidateQueries`.

## 71: How do you set default options for all queries or for some queries?

Use `defaultOptions` on the client for everything, and `setQueryDefaults` for queries that match a key prefix.

```js
const queryClient = new QueryClient({
  defaultOptions: {
    queries: { staleTime: 60_000, refetchOnWindowFocus: false },
    mutations: { retry: 0 },
  },
});

queryClient.setQueryDefaults(["reports"], {
  staleTime: Infinity,
  gcTime: Infinity,
});
```

Options passed to `useQuery` win over `setQueryDefaults`, which wins over `defaultOptions`.

## 72: What is skipToken?

`skipToken` is a value you pass as `queryFn` to disable a query. It does the same thing as `enabled: false`, but TypeScript understands it better, because you only build the real function when the input exists.

```ts
import { skipToken, useQuery } from "@tanstack/react-query";

function useUser(id: number | undefined) {
  return useQuery({
    queryKey: ["user", id],
    queryFn: id ? () => fetchUser(id) : skipToken,
  });
}
```

One difference: `refetch()` does not work with `skipToken`, because there is no function to run. With `enabled: false`, `refetch()` still runs the query.

## 73: What is networkMode?

It controls how queries and mutations behave when the device is offline.

- `'online'` (default): don't fetch while offline. The query goes to `fetchStatus: 'paused'` and continues when the connection is back.
- `'always'`: fetch anyway and ignore the online status. Useful for local async work like IndexedDB.
- `'offlineFirst'`: run the function once, then pause retries while offline. Useful when a service worker or HTTP cache may answer offline.

```js
useQuery({
  queryKey: ["notes"],
  queryFn: readNotesFromIndexedDb,
  networkMode: "always",
});
```

## 74: What can you do with the devtools when debugging?

Open the devtools panel to see every query in the cache with its key and current state: fresh, stale, fetching, paused or inactive. For each query you can see the data, the number of observers and when it was last updated. You can refetch, invalidate, reset or remove a query, and force it into a loading or error state to check your UI.

```jsx
import { ReactQueryDevtools } from "@tanstack/react-query-devtools";

<QueryClientProvider client={queryClient}>
  <App />
  <ReactQueryDevtools initialIsOpen={false} />
</QueryClientProvider>;
```

Common things it helps catch: two keys that look the same but differ (`'5'` vs `5`), queries that are refetched too often, and queries that never become inactive.

## 75: What does the TanStack Query ESLint plugin check?

`@tanstack/eslint-plugin-query` catches common mistakes. Some of its rules:

- `exhaustive-deps`: every variable used in `queryFn` must be in `queryKey`
- `stable-query-client`: don't create the `QueryClient` inside a component body
- `no-rest-destructuring`: don't use `...rest` on query results, it breaks tracked props
- `no-unstable-deps`: don't put the whole query or mutation result in hook dependency arrays
- `no-void-query-fn`: the query function must return something

## 76: How does TypeScript work with TanStack Query?

Types are inferred from the query function, so you rarely write generics. Type the function's return value and the rest follows.

```ts
async function fetchTodo(id: number): Promise<Todo> {
  const res = await fetch(`/api/todos/${id}`);
  if (!res.ok) throw new Error("Failed");
  return res.json();
}

const { data } = useQuery({
  queryKey: ["todo", 1],
  queryFn: () => fetchTodo(1),
});
// data: Todo | undefined
```

The error type is `Error` by default. If your query functions throw something else, such as `AxiosError`, register it once:

```ts
declare module "@tanstack/react-query" {
  interface Register {
    defaultError: AxiosError;
  }
}
```

## 77: How do you test components that use TanStack Query?

Create a new `QueryClient` for each test so tests don't share a cache, and turn off retries so errors show up quickly. Mock the network with something like MSW.

```jsx
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { render, screen } from "@testing-library/react";

function renderWithClient(ui) {
  const client = new QueryClient({
    defaultOptions: { queries: { retry: false } },
  });
  return render(
    <QueryClientProvider client={client}>{ui}</QueryClientProvider>,
  );
}

test("shows todos", async () => {
  renderWithClient(<Todos />);
  expect(await screen.findByText("Buy milk")).toBeInTheDocument();
});
```

For custom hooks, use `renderHook` with the same wrapper and `waitFor(() => expect(result.current.isSuccess).toBe(true))`.

## 78: What is the difference between refetch, invalidate, reset and remove?

- `refetchQueries` (or `refetch`): fetch now, without changing anything else.
- `invalidateQueries`: mark as stale and refetch the ones that are in use. This is what you want after mutations.
- `resetQueries`: put the queries back to their initial state (their `initialData` or no data) and refetch the active ones. Users see a loading state again.
- `removeQueries`: delete them from the cache. Nothing is refetched until a component asks again.

## 79: How do you show a detail page instantly using data from a list query?

If the list already has everything the detail page needs, use it as `initialData` and tell TanStack Query how old it is.

```js
useQuery({
  queryKey: ["todo", id],
  queryFn: () => fetchTodo(id),
  initialData: () =>
    queryClient.getQueryData(["todos"])?.find((t) => t.id === id),
  initialDataUpdatedAt: () =>
    queryClient.getQueryState(["todos"])?.dataUpdatedAt,
});
```

Without `initialDataUpdatedAt`, the copied data counts as brand new and may not be refetched. If the list only has some fields, use `placeholderData` instead, so the full detail is always fetched.

## 80: What changed from TanStack Query v4 to v5?

The main changes:

- Hooks take only one object argument: `useQuery({ queryKey, queryFn })`
- `cacheTime` is now `gcTime`
- The `loading` status is now `pending`, `isLoading` is now `isPending`, and the new `isLoading` means `isPending && isFetching`
- `keepPreviousData` became `placeholderData: keepPreviousData`
- `useErrorBoundary` became `throwOnError`
- `onSuccess`, `onError` and `onSettled` were removed from queries
- Infinite queries need `initialPageParam`, and `maxPages` was added
- `Hydrate` became `HydrationBoundary`
- New `useSuspenseQuery`, `queryOptions`, `useMutationState` and `combine` in `useQueries`
- Window focus refetch now listens to the `visibilitychange` event only
- React 18 is the minimum

There is a codemod that handles many of the renames.

# Advanced Questions (81-120)

## 81: How is TanStack Query built internally?

The core package (`@tanstack/query-core`) has a few main classes:

- `QueryClient`: the public API. It holds a `QueryCache`, a `MutationCache` and the default options.
- `QueryCache`: a map from query hash to `Query` objects. It also sends cache events.
- `Query`: one cache entry. It holds the state (data, error, status, timestamps), runs the fetch through a retryer, dedupes requests and handles garbage collection.
- `QueryObserver`: connects one consumer (for example one `useQuery` call) to one `Query`. It applies options like `select`, `placeholderData` and `enabled`, decides when to fetch and builds the result object.
- `MutationCache`, `Mutation` and `MutationObserver`: the same idea for mutations.

The framework adapters are thin. In React, `useQuery` creates a `QueryObserver` and subscribes to it with `useSyncExternalStore`.

## 82: How does useQuery decide when to re-render a component?

The `QueryObserver` builds a new result each time the query changes, then compares it with the previous one. By default it uses tracked properties: the result object records which fields your component actually read during render (for example only `data` and `isPending`). The component is notified only when one of those fields changes.

So a component that never reads `isFetching` does not re-render on every background refetch. You can override this with `notifyOnChangeProps`, for example `notifyOnChangeProps: ['data']` or `'all'`. Object rest destructuring (`const { data, ...rest } = useQuery(...)`) reads every field and turns this optimization off.

## 83: How are query keys turned into cache entries?

Each key is turned into a string hash with a deterministic JSON serialization. Plain objects have their keys sorted first, so property order does not matter, but array order does. Two keys with the same hash share one `Query` in the cache.

Because of this, keys must be JSON-serializable. Functions, class instances and `Symbol`s don't hash in a useful way. If you need special handling, you can pass `queryKeyHashFn`, but that is rarely needed. A common bug is mixing types: `['todo', '5']` and `['todo', 5]` are different entries.

## 84: What is structural sharing and why does it matter?

When new data arrives, TanStack Query compares it deeply with the old data and keeps the old object references for every part that did not change. If nothing changed at all, `data` is the exact same reference as before.

This means `useEffect` and `useMemo` that depend on `data` or a part of it only run when the content really changed, and memoized child components don't re-render after a refetch that returned the same JSON.

It only works with JSON-like data. For very large responses the deep compare costs time, so you can turn it off with `structuralSharing: false`, or pass your own function.

## 85: How does garbage collection work in TanStack Query?

Each `Query` counts its observers. When the last observer unsubscribes (for example the last component using the key unmounts), the query becomes inactive and a timer of `gcTime` starts. If a new observer subscribes before the timer ends, the timer is cleared. Otherwise the query is removed from the cache.

Queries that were only prefetched and never observed also get a gc timer. Setting `gcTime: Infinity` keeps data forever, which can grow memory in long sessions. Setting `gcTime: 0` removes data right away, which means going back to a page always shows a loading state.

## 86: Why does cancelQueries matter in optimistic updates?

Suppose a background refetch of `['todos']` started before the user clicked "Done". You update the cache optimistically, and then the refetch finishes with the old server state and overwrites your change. The checkbox flips back for a moment and then forward again when the next refetch runs.

Calling `await queryClient.cancelQueries({ queryKey: ['todos'] })` in `onMutate` stops in-flight fetches for that key. A cancelled fetch puts the query back to its state before the fetch started, so your optimistic data stays.

## 87: How do you handle several optimistic mutations running at the same time?

The usual pattern invalidates in `onSettled`. With several quick mutations (for example toggling many checkboxes), the first one settles and refetches while the others are still running. That refetch can return data that doesn't include the later changes yet, so the UI flickers.

One fix is to invalidate only when this is the last mutation running for that data:

```js
useMutation({
  mutationKey: ["todos", "toggle"],
  mutationFn: toggleTodo,
  onMutate: async (id) => {
    await queryClient.cancelQueries({ queryKey: ["todos"] });
    queryClient.setQueryData(["todos"], (old) =>
      old.map((t) => (t.id === id ? { ...t, done: !t.done } : t)),
    );
  },
  onSettled: () => {
    if (queryClient.isMutating({ mutationKey: ["todos", "toggle"] }) === 1) {
      return queryClient.invalidateQueries({ queryKey: ["todos"] });
    }
  },
});
```

`isMutating` returns `1` here because the current mutation is still counted while its `onSettled` runs.

## 88: How do you keep mutations working when the app goes offline or the page reloads?

With the default `networkMode: 'online'`, mutations made offline are paused and run when the connection comes back. To survive a page reload you also need to persist them:

1. Persist the client with `PersistQueryClientProvider` and a persister.
2. Register the mutation function with `setMutationDefaults`, because functions can't be saved to storage. After a reload, the restored mutation looks up its function by `mutationKey`.
3. Call `queryClient.resumePausedMutations()` after the cache is restored.

```jsx
queryClient.setMutationDefaults(["addTodo"], { mutationFn: createTodo });

<PersistQueryClientProvider
  client={queryClient}
  persistOptions={{ persister }}
  onSuccess={() => queryClient.resumePausedMutations()}
>
  <App />
</PersistQueryClientProvider>;
```

## 89: How does persisting the query cache work, and what should you watch out for?

`@tanstack/react-query-persist-client` saves the dehydrated cache to storage and restores it on load. You pick a persister, for example `createAsyncStoragePersister` from `@tanstack/query-async-storage-persister` for `localStorage`, IndexedDB wrappers or React Native AsyncStorage.

Things to watch:

- Set `gcTime` at least as high as `maxAge`, or restored queries are removed right away.
- Use `buster` (a version string) to throw away old caches after a deploy changes the data shape.
- Use `dehydrateOptions.shouldDehydrateQuery` to skip queries you don't want saved.
- Never persist sensitive data in plain `localStorage`, and clear the storage on logout.

## 90: How does server-side rendering work with TanStack Query?

The basic flow:

1. On the server, create a new `QueryClient` for the request.
2. Prefetch the queries the page needs with `prefetchQuery`.
3. Call `dehydrate(queryClient)` to get a serializable snapshot.
4. Send it to the browser and wrap the page in `HydrationBoundary state={dehydratedState}`.
5. On the client, `useQuery` with the same keys reads the hydrated data, so there is no loading state.

```jsx
export async function getServerSideProps() {
  const queryClient = new QueryClient();
  await queryClient.prefetchQuery(todoQueries.list({}));
  return { props: { dehydratedState: dehydrate(queryClient) } };
}
```

Set a `staleTime` above 0 on the client, or the hydrated data is refetched right after the page loads.

## 91: How do you set up TanStack Query with the Next.js App Router?

Server components prefetch into a per-request client and pass the dehydrated state to client components. The browser keeps one client for the whole session.

```jsx
// get-query-client.js
import {
  QueryClient,
  defaultShouldDehydrateQuery,
  isServer,
} from "@tanstack/react-query";

function makeQueryClient() {
  return new QueryClient({
    defaultOptions: {
      queries: { staleTime: 60_000 },
      dehydrate: {
        shouldDehydrateQuery: (query) =>
          defaultShouldDehydrateQuery(query) ||
          query.state.status === "pending",
      },
    },
  });
}

let browserQueryClient;

export function getQueryClient() {
  if (isServer) return makeQueryClient();
  if (!browserQueryClient) browserQueryClient = makeQueryClient();
  return browserQueryClient;
}
```

```jsx
// app/todos/page.jsx (server component)
export default async function Page() {
  const queryClient = getQueryClient();
  await queryClient.prefetchQuery(todoQueries.list({}));
  return (
    <HydrationBoundary state={dehydrate(queryClient)}>
      <TodoList />
    </HydrationBoundary>
  );
}
```

The provider lives in a `'use client'` component that calls `getQueryClient()`. Don't create the browser client in `useState` there if a Suspense boundary sits above the provider, because React may throw away that state while suspended.

## 92: How can you stream queries from the server instead of awaiting them?

Start the prefetch without `await`, and include pending queries when dehydrating (the `shouldDehydrateQuery` in the previous answer does that). The promise is sent to the client as part of the stream, and a client component using `useSuspenseQuery` with the same key suspends until it resolves.

```jsx
export default function Page() {
  const queryClient = getQueryClient();
  queryClient.prefetchQuery(todoQueries.list({})); // no await

  return (
    <HydrationBoundary state={dehydrate(queryClient)}>
      <Suspense fallback={<Spinner />}>
        <TodoList />
      </Suspense>
    </HydrationBoundary>
  );
}
```

The shell renders right away and the list streams in when ready. If your data contains values JSON can't keep, such as `Date`, set `serializeData` in the dehydrate options and `deserializeData` in the hydrate options, for example with superjson.

## 93: What happens when hydrated data meets data that is already in the cache?

`hydrate` (and `HydrationBoundary`) only writes a query if the incoming data is newer than what the cache has, based on `dataUpdatedAt`. So navigating back to a server-rendered page doesn't overwrite fresher client data with an older server snapshot.

`HydrationBoundary` also adds new queries during render, but it delays overwriting queries that already exist until after render (in an effect), so components that are already showing that data don't change in the middle of a render.

## 94: What can go wrong with TanStack Query on the server?

- Sharing one `QueryClient` across requests leaks one user's data to another user. Always create a client per request.
- On the server, `gcTime` defaults to `Infinity` and `retry` to `0`, because the client is thrown away after the request. Don't change `gcTime` to a timer value there, or timers can keep the process busy.
- Errors are not dehydrated by default, so a failed server prefetch is retried on the client. Decide whether that is what you want.
- Calling `fetchQuery` throws on errors, while `prefetchQuery` never does. Use the one that matches whether the page can render without the data.

## 95: How do you avoid request waterfalls with Suspense?

Each `useSuspenseQuery` in the same component suspends before the next line runs, so two calls in a row load one after the other.

```jsx
// waterfall: the second request starts only after the first finished
const { data: user } = useSuspenseQuery(userQuery(id));
const { data: posts } = useSuspenseQuery(postsQuery(id));
```

Fixes:

- Use `useSuspenseQueries` so both start together.
- Prefetch both earlier, in a route loader, an event handler or a parent component with `usePrefetchQuery`.
- On the server, prefetch everything before rendering.

The same problem happens with nested components where a child only starts its query after the parent's query finished.

## 96: What are the gotchas with Suspense queries?

- Suspense queries use a minimum `staleTime` of 1 second, so a component that suspends and remounts doesn't refetch in a loop.
- `useSuspenseQuery` can't be disabled. If the input may be missing, render the component only when it exists, or use `useQuery` with `enabled`.
- Changing the key suspends again and shows the fallback. Wrap the state update in `startTransition` to keep the old UI on screen while the new data loads.
- An error with existing data in the cache is not thrown by default. Only errors with no data reach the error boundary.

## 97: What is experimental_prefetchInRender?

It is an option on the `QueryClient` that lets you start a fetch from `useQuery` and read it as a promise with React's `use` hook. The result of `useQuery` then has a `promise` field.

```jsx
const queryClient = new QueryClient({
  defaultOptions: { queries: { experimental_prefetchInRender: true } },
});

function Parent() {
  const query = useQuery(todoQueries.list({}));
  return (
    <Suspense fallback={<Spinner />}>
      <List promise={query.promise} />
    </Suspense>
  );
}

function List({ promise }) {
  const todos = React.use(promise);
  return todos.map((t) => <p key={t.id}>{t.title}</p>);
}
```

The parent starts the fetch without suspending, and only the child suspends. It is marked experimental, so the API may still change.

## 98: What is streamedQuery used for?

`experimental_streamedQuery` builds a query function from an async iterable, such as a stream of tokens from an AI chat API. The query goes to `success` as soon as the first chunk arrives, and each new chunk is added to `data` while `fetchStatus` stays `'fetching'` until the stream ends.

```js
import {
  experimental_streamedQuery as streamedQuery,
  useQuery,
} from "@tanstack/react-query";

useQuery({
  queryKey: ["chat", chatId],
  queryFn: streamedQuery({
    streamFn: () => streamChatAnswer(chatId), // returns an AsyncIterable of chunks
    refetchMode: "reset",
  }),
});
```

`refetchMode` decides what happens on refetch: `'reset'` clears the data and starts over, `'append'` adds new chunks to the old ones, and `'replace'` keeps showing the old data until the new stream is done. Newer versions also accept a `reducer` and `initialValue` to build something other than an array. It is experimental, and option names have changed between minor versions, so check the docs for your version.

## 99: How do you reduce re-renders in components that use queries?

- Read only the fields you need, and avoid rest destructuring, so tracked props work.
- Use `select` to subscribe to a small slice. The component re-renders only when the slice changes.
- Keep `select` stable, either outside the component or in `useCallback`, so it doesn't run on every render.
- In `useQueries`, use `combine` with a stable function. The combined result is memoized.
- Don't pass the whole query result to child components or effect dependency arrays. Pass `data` or specific fields.
- Check the setting of `notifyOnChangeProps` if someone set it to `'all'`.

## 100: How would you handle infinite lists with thousands of items?

Rendering is usually the problem, not the cache. Combine `useInfiniteQuery` with a virtual list (for example TanStack Virtual), so only visible rows are in the DOM. Trigger `fetchNextPage` when the user scrolls near the end, and guard it with `hasNextPage && !isFetchingNextPage`.

Also set `maxPages` so the cache doesn't grow without limit, and keep in mind that refetching an infinite query refetches every loaded page one by one, starting from the first. With 50 loaded pages, one focus refetch can mean 50 requests. A larger `staleTime` or `maxPages` keeps that under control.

## 101: A dashboard with 30 widgets sends a burst of requests every time the user switches tabs. How do you fix it?

Every widget query is stale with the default `staleTime: 0`, so each focus event refetches all of them. Options, from simplest:

- Raise `staleTime` for the dashboard queries so a quick tab switch doesn't count as "data may have changed".
- Turn off `refetchOnWindowFocus` for widgets that already poll with `refetchInterval`.
- Merge widgets that use the same endpoint into one query and use `select` in each widget.
- If the backend supports it, add one batch endpoint for the dashboard.

Check the devtools afterwards to see which queries still refetch on focus.

## 102: How do you combine TanStack Query with WebSockets?

Keep TanStack Query as the cache and use the socket only to tell it about changes. There are two common ways:

```js
useEffect(() => {
  const socket = new WebSocket("wss://example.com/updates");

  socket.onmessage = (event) => {
    const message = JSON.parse(event.data);

    if (message.type === "todo-updated") {
      // option 1: write the new data straight into the cache
      queryClient.setQueryData(["todo", message.todo.id], message.todo);
      // option 2: just say what changed and let the query refetch
      queryClient.invalidateQueries({ queryKey: ["todos", "list"] });
    }
  };

  return () => socket.close();
}, [queryClient]);
```

Writing the payload saves requests but needs the full data in the event. Invalidating is simpler and always correct. Because the socket keeps data up to date, you can set `staleTime: Infinity` for those queries so they don't also refetch on focus.

## 103: How do you update an infinite query cache after a mutation?

The cached value has the shape `{ pages, pageParams }`, so the updater has to walk through the pages and keep that shape.

```js
queryClient.setQueryData(["posts"], (old) => {
  if (!old) return old;
  return {
    ...old,
    pages: old.pages.map((page) => ({
      ...page,
      items: page.items.map((post) =>
        post.id === updated.id ? updated : post,
      ),
    })),
  };
});
```

For adds and deletes, cursor-based pages can shift, so it is often safer to invalidate the infinite query. Keep in mind that invalidating refetches every loaded page in order, starting with the first.

## 104: How do you handle expired access tokens with TanStack Query?

Handle token refresh in your HTTP layer, not in each query. For example, an Axios interceptor catches a 401, refreshes the token once (shared between parallel requests), and retries the original request. TanStack Query only sees the final success or failure.

Also stop TanStack Query from retrying 401 errors itself, otherwise you get extra requests:

```js
retry: (count, error) => error.response?.status !== 401 && count < 3,
```

If the refresh fails, log the user out, clear the cache with `queryClient.clear()`, and send them to the login page.

## 105: How do you design query keys so invalidation stays easy?

Go from general to specific, and keep the feature name first:

```js
["todos"];
["todos", "list"];
["todos", "list", { status: "open", page: 2 }];
["todos", "detail", 42];
["todos", "detail", 42, "comments"];
```

Then `['todos']` invalidates everything about todos, `['todos', 'list']` only lists, and `['todos', 'detail', 42]` one todo with its comments. Put filter objects last so prefix matching still works.

If data depends on the user or tenant, put that into the key as well (for example `['org', orgId, 'todos', ...]`), so switching accounts can never show cached data from another account.

## 106: How does queryOptions make getQueryData and setQueryData type-safe?

`queryOptions` returns a `queryKey` with a hidden type tag (`DataTag`) that stores the data type of the query function. `getQueryData`, `setQueryData` and similar methods read that tag.

```ts
const todoQuery = (id: number) =>
  queryOptions({
    queryKey: ["todo", id],
    queryFn: () => fetchTodo(id), // Promise<Todo>
  });

const todo = queryClient.getQueryData(todoQuery(1).queryKey);
// Todo | undefined

queryClient.setQueryData(
  todoQuery(1).queryKey,
  (old) => old && { ...old, done: true },
);
// old is Todo | undefined, a wrong shape is a type error
```

With a plain array key, `getQueryData` returns `unknown` unless you pass a generic, which is easy to get wrong.

## 107: Should you transform data in the queryFn or in select?

In the `queryFn`, the transformed data is what gets stored. Every component sees the same shape, and the transformation runs once per fetch. This is good for things like turning snake_case into camelCase or parsing with a schema.

In `select`, the cache keeps the raw response and each component can pick its own view. The transformation runs per observer, but only when the data or the `select` function changes. This is good for filtering, counting or picking one field.

Avoid putting values that can't be serialized (class instances, `Date` objects) into the cache if you persist it or use SSR, unless you set up serialization for them.

## 108: How can you use TanStack Query outside React components?

The core works without a framework. You can use the `QueryClient` methods directly, for example in a router loader or plain script, and you can subscribe to a query with a `QueryObserver`.

```js
import { QueryClient, QueryObserver } from "@tanstack/query-core";

const queryClient = new QueryClient();
queryClient.mount();

const observer = new QueryObserver(queryClient, {
  queryKey: ["todos"],
  queryFn: fetchTodos,
});

const unsubscribe = observer.subscribe((result) => {
  console.log(result.status, result.data);
});
```

`mount()` connects the client to the focus and online managers. Framework adapters do this for you. This is also how people build adapters for frameworks that don't have one.

## 109: How can you react to every change in the query cache?

`queryClient.getQueryCache().subscribe` calls your listener for every cache event: queries added, removed or updated, and observers added or removed.

```js
const unsubscribe = queryClient.getQueryCache().subscribe((event) => {
  if (event.type === "updated" && event.action.type === "error") {
    reportError(event.query.queryKey, event.query.state.error);
  }
});
```

This is useful for logging, monitoring tools or custom sync logic. Keep the listener cheap, because it runs a lot. For plain error handling, the `onError` option on `QueryCache` is simpler.

## 110: How do you keep the cache in sync across browser tabs?

There is an experimental plugin, `@tanstack/query-broadcast-client-experimental`, that uses the `BroadcastChannel` API to send cache updates to other tabs of the same app.

```js
import { broadcastQueryClient } from "@tanstack/query-broadcast-client-experimental";

broadcastQueryClient({ queryClient, broadcastChannel: "my-app" });
```

A simpler option that is often enough: invalidate on `visibilitychange` (which the default focus refetch already does for stale queries), or send a `BroadcastChannel` message yourself after important mutations and invalidate the related keys in other tabs.

## 111: How do you make focus and online refetching work in React Native?

React Native has no `window` focus events or `navigator.onLine`, so you connect the managers yourself.

```js
import NetInfo from "@react-native-community/netinfo";
import { AppState } from "react-native";
import { focusManager, onlineManager } from "@tanstack/react-query";

onlineManager.setEventListener((setOnline) =>
  NetInfo.addEventListener((state) => setOnline(!!state.isConnected)),
);

AppState.addEventListener("change", (status) => {
  focusManager.setFocused(status === "active");
});
```

After this, queries refetch when the app comes back to the foreground and pause while the phone is offline.

## 112: How do you test query logic without flaky tests?

- Create a new `QueryClient` per test with `retry: false`, and clear it after each test.
- Mock at the network level with MSW instead of mocking `useQuery`, so the real cache logic runs.
- Use `findBy` queries or `waitFor` instead of fixed timeouts.
- For error states with retries you want to keep, set `retryDelay: 0` or use fake timers and advance them.
- Check the cache directly when the result is not visible, for example `queryClient.getQueryData(['todos'])` after a mutation, or `queryClient.getQueryState(['todos']).isInvalidated`.
- With fake timers, remember that `gcTime` and `refetchInterval` timers also run, so clean up the client.

## 113: How do you use TanStack Query with route loaders?

Load data in the loader so it starts before the component renders, and read it with the same options in the component. `ensureQueryData` returns cached data if it exists, and fetches otherwise.

```jsx
// React Router data loader
export const loader =
  (queryClient) =>
  async ({ params }) => {
    await queryClient.ensureQueryData(todoQueries.detail(Number(params.id)));
    return null;
  };

function TodoPage() {
  const { id } = useParams();
  const { data } = useSuspenseQuery(todoQueries.detail(Number(id)));
  return <h1>{data.title}</h1>;
}
```

The loader removes the waterfall, and the hook keeps the page reactive, so background refetches and invalidations still update it. TanStack Router uses the same pattern with `context.queryClient` in its `loader`.

## 114: When is TanStack Query not the right tool?

- Data that only lives in the browser (UI state, form drafts). Use component state or a client state library.
- Apps with heavy, deeply linked data where one change must update many entities everywhere. A normalized cache like Apollo Client or Relay with GraphQL may fit better, because TanStack Query caches by key, not by entity.
- Pages that are fully rendered on the server with React Server Components and never refetch on the client. Plain server data loading is enough there.
- Very simple apps with one or two requests, where a full cache library adds more than it gives.

## 115: What edge cases do you need to know about setQueryData?

- If the key doesn't exist, `setQueryData` creates a new query with that data.
- If the updater returns `undefined`, nothing is changed. That lets you skip updates when `old` is missing.
- The new data is treated as freshly fetched: `dataUpdatedAt` is set to now, so `staleTime` starts again. You can pass `{ updatedAt }` as a third argument to set it yourself.
- Updates must be immutable. Changing `old` in place breaks structural sharing and change detection.
- `setQueryData` does not cancel a running fetch. If one is in flight, its result can overwrite your data, so call `cancelQueries` first when that matters.

## 116: What are the pitfalls of disabled queries?

- A disabled query with no data stays `isPending: true` forever. Show a spinner on `isLoading`, not `isPending`, or you get an endless spinner.
- `refetch()` still runs a query disabled with `enabled: false`. That is the official way to fetch on demand, but it skips any check you put in `enabled`.
- `invalidateQueries` does not refetch disabled queries, it only marks them stale.
- `enabled` can also be a function `(query) => boolean`, so you can decide based on the query's current state.

For on-demand loading triggered by a click, `queryClient.fetchQuery` in the event handler is often clearer than a disabled query plus `refetch`.

## 117: Is it safe to use query data as a dependency in useEffect or useMemo?

Mostly yes, thanks to structural sharing. If a refetch returns the same content, `data` keeps the same reference, so the effect doesn't run again. Nested parts that didn't change keep their references too.

Structural sharing is also applied to the result of `select`, so a `select` that filters into a new array still gives you the same reference when the result is equal. An inline `select` does run again on every render, though, which costs time for big data, so keep it stable. What you should never put in dependencies is the whole query result object: it is a new object on most renders. The ESLint rule `no-unstable-deps` warns about that.

## 118: How would you clear all data when the user logs out?

Call `queryClient.clear()`, which removes every query and mutation from the cache. If the cache is persisted, also remove the persisted copy, for example by calling the persister's `removeClient()`, otherwise the next user may see restored data.

```js
async function logout() {
  await api.logout();
  queryClient.clear();
  await persister.removeClient();
  navigate("/login");
}
```

Putting the user ID into query keys gives an extra safety net, because a new user can never match old keys. Avoid `resetQueries` here, since it refetches active queries with the old session state.

## 119: How does TanStack Query compare to SWR, RTK Query and Apollo Client?

- SWR: same stale-while-revalidate idea and a smaller API. TanStack Query has more built in: mutations with lifecycle callbacks, devtools, infinite query helpers, offline support, persistence and many framework adapters.
- RTK Query: part of Redux Toolkit. You define endpoints up front and get generated hooks, and cache invalidation works with tags. A good fit if the app already uses Redux. TanStack Query has no central API definition and is not tied to Redux.
- Apollo Client: for GraphQL, with a normalized cache by entity ID, so updating one entity updates it everywhere. TanStack Query works with any async source and caches by key, so you invalidate or update related keys yourself.

## 120: How would you design the data layer for an e-commerce front end with TanStack Query?

A reasonable setup:

- One API module per feature (`products`, `cart`, `orders`) with typed fetch functions and `queryOptions` factories with hierarchical keys.
- Different `staleTime` per kind of data: categories and config `Infinity`, product lists a few minutes, cart and stock `0` or short.
- Route loaders or server prefetching for product and category pages, with SSR hydration for SEO.
- `placeholderData: keepPreviousData` for filtered and paginated product lists, with filters stored in the URL and used in the key.
- The cart as server state with optimistic updates through the cache and rollback on error. Use `scope` so quick quantity changes are sent in order.
- Checkout mutations without optimistic updates, because the user must see the real result, and `retry: 0` so payments are never repeated by accident.
- Global error toasts through `QueryCache`, `throwOnError` for 5xx errors on main pages, and `queryClient.clear()` on logout.
