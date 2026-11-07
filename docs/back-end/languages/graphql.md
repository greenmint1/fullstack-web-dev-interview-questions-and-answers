# GraphQL Interview Questions and Answers

_Last updated: October 28, 2026_

450 GraphQL interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers follow the September 2025 edition of the GraphQL spec and current JavaScript tools: graphql-js 16 and 17, Apollo Server 5, Apollo Client 4, GraphQL Yoga 5, graphql-ws and Apollo Federation 2. Older things like Apollo Server 4, Apollo Client 3 and `subscriptions-transport-ws` are pointed out where they matter, since you will still see them in real projects.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is GraphQL?](#1-what-is-graphql)
- [2: Who created GraphQL and who maintains it now?](#2-who-created-graphql-and-who-maintains-it-now)
- [3: What problems does GraphQL solve compared to REST?](#3-what-problems-does-graphql-solve-compared-to-rest)
- [4: What is over-fetching?](#4-what-is-over-fetching)
- [5: What is under-fetching?](#5-what-is-under-fetching)
- [6: What is a GraphQL schema?](#6-what-is-a-graphql-schema)
- [7: What is SDL?](#7-what-is-sdl)
- [8: What are the three root operation types?](#8-what-are-the-three-root-operation-types)
- [9: What is a query?](#9-what-is-a-query)
- [10: What is a mutation?](#10-what-is-a-mutation)
- [11: What is a subscription?](#11-what-is-a-subscription)
- [12: What is a resolver?](#12-what-is-a-resolver)
- [13: What arguments does a resolver receive?](#13-what-arguments-does-a-resolver-receive)
- [14: What are the built-in scalar types?](#14-what-are-the-built-in-scalar-types)
- [15: What is the ID type?](#15-what-is-the-id-type)
- [16: What is an object type?](#16-what-is-an-object-type)
- [17: What is a field in GraphQL?](#17-what-is-a-field-in-graphql)
- [18: What does the exclamation mark mean in a type?](#18-what-does-the-exclamation-mark-mean-in-a-type)
- [19: How do you define a list type?](#19-how-do-you-define-a-list-type)
- [20: What is the difference between `[String]`, `[String!]`, `[String]!` and `[String!]!`?](#20-what-is-the-difference-between-string-string-string-and-string)
- [21: What is an enum type?](#21-what-is-an-enum-type)
- [22: What is an input type?](#22-what-is-an-input-type)
- [23: Why can't you use an object type as an argument?](#23-why-cant-you-use-an-object-type-as-an-argument)
- [24: What is an interface?](#24-what-is-an-interface)
- [25: What is a union type?](#25-what-is-a-union-type)
- [26: What is the difference between an interface and a union?](#26-what-is-the-difference-between-an-interface-and-a-union)
- [27: How do arguments work on fields?](#27-how-do-arguments-work-on-fields)
- [28: How do you give an argument a default value?](#28-how-do-you-give-an-argument-a-default-value)
- [29: What are variables in GraphQL?](#29-what-are-variables-in-graphql)
- [30: Why should you use variables instead of building the query string yourself?](#30-why-should-you-use-variables-instead-of-building-the-query-string-yourself)
- [31: What is an operation name and why should you use it?](#31-what-is-an-operation-name-and-why-should-you-use-it)
- [32: What is an alias?](#32-what-is-an-alias)
- [33: What is a fragment?](#33-what-is-a-fragment)
- [34: What is an inline fragment?](#34-what-is-an-inline-fragment)
- [35: What is `__typename`?](#35-what-is-__typename)
- [36: What are directives?](#36-what-are-directives)
- [37: How do `@include` and `@skip` work?](#37-how-do-include-and-skip-work)
- [38: What does `@deprecated` do?](#38-what-does-deprecated-do)
- [39: What does `@specifiedBy` do?](#39-what-does-specifiedby-do)
- [40: What is introspection?](#40-what-is-introspection)
- [41: How do you query the schema with introspection?](#41-how-do-you-query-the-schema-with-introspection)
- [42: What does a GraphQL response look like?](#42-what-does-a-graphql-response-look-like)
- [43: What does the `errors` array contain?](#43-what-does-the-errors-array-contain)
- [44: Can a response have both `data` and `errors`?](#44-can-a-response-have-both-data-and-errors)
- [45: Which HTTP method does GraphQL usually use?](#45-which-http-method-does-graphql-usually-use)
- [46: Is GraphQL tied to HTTP?](#46-is-graphql-tied-to-http)
- [47: What does a GraphQL request body look like?](#47-what-does-a-graphql-request-body-look-like)
- [48: How do you send a GraphQL query with `fetch`?](#48-how-do-you-send-a-graphql-query-with-fetch)
- [49: Why does a GraphQL API usually have one endpoint?](#49-why-does-a-graphql-api-usually-have-one-endpoint)
- [50: What is the GraphQL over HTTP specification?](#50-what-is-the-graphql-over-http-specification)
- [51: What HTTP status code does a GraphQL server return when something fails?](#51-what-http-status-code-does-a-graphql-server-return-when-something-fails)
- [52: What is GraphiQL?](#52-what-is-graphiql)
- [53: What other tools can you use to explore a GraphQL API?](#53-what-other-tools-can-you-use-to-explore-a-graphql-api)
- [54: What is Apollo Server?](#54-what-is-apollo-server)
- [55: How do you create a simple server with Apollo Server?](#55-how-do-you-create-a-simple-server-with-apollo-server)
- [56: What is GraphQL Yoga?](#56-what-is-graphql-yoga)
- [57: What is graphql-js?](#57-what-is-graphql-js)
- [58: What is Apollo Client?](#58-what-is-apollo-client)
- [59: What other GraphQL clients are there?](#59-what-other-graphql-clients-are-there)
- [60: What is the context object?](#60-what-is-the-context-object)
- [61: What is the `parent` argument in a resolver?](#61-what-is-the-parent-argument-in-a-resolver)
- [62: What is the `info` argument used for?](#62-what-is-the-info-argument-used-for)
- [63: What is a default resolver?](#63-what-is-a-default-resolver)
- [64: Can resolvers be async?](#64-can-resolvers-be-async)
- [65: What is a resolver map?](#65-what-is-a-resolver-map)
- [66: What is the difference between schema-first and code-first?](#66-what-is-the-difference-between-schema-first-and-code-first)
- [67: Which libraries are used for code-first schemas?](#67-which-libraries-are-used-for-code-first-schemas)
- [68: How are nested fields resolved?](#68-how-are-nested-fields-resolved)
- [69: Are fields executed in parallel or one after another?](#69-are-fields-executed-in-parallel-or-one-after-another)
- [70: Should a mutation take many arguments or a single input object?](#70-should-a-mutation-take-many-arguments-or-a-single-input-object)
- [71: What should a mutation return?](#71-what-should-a-mutation-return)
- [72: Can you put several operations in one document?](#72-can-you-put-several-operations-in-one-document)
- [73: Can one query ask for several root fields?](#73-can-one-query-ask-for-several-root-fields)
- [74: What is a selection set?](#74-what-is-a-selection-set)
- [75: What is a leaf field?](#75-what-is-a-leaf-field)
- [76: How do you write comments in GraphQL?](#76-how-do-you-write-comments-in-graphql)
- [77: What are descriptions in a schema?](#77-what-are-descriptions-in-a-schema)
- [78: Are commas required in GraphQL?](#78-are-commas-required-in-graphql)
- [79: What is a GraphQL document?](#79-what-is-a-graphql-document)
- [80: What is the query shorthand?](#80-what-is-the-query-shorthand)
- [81: What naming conventions are common in GraphQL schemas?](#81-what-naming-conventions-are-common-in-graphql-schemas)
- [82: Do the root types have to be named `Query`, `Mutation` and `Subscription`?](#82-do-the-root-types-have-to-be-named-query-mutation-and-subscription)
- [83: What is a custom scalar?](#83-what-is-a-custom-scalar)
- [84: Which custom scalars are commonly used?](#84-which-custom-scalars-are-commonly-used)
- [85: How does GraphQL handle dates?](#85-how-does-graphql-handle-dates)
- [86: Why are fields nullable by default?](#86-why-are-fields-nullable-by-default)
- [87: What happens when a non-null field resolves to `null`?](#87-what-happens-when-a-non-null-field-resolves-to-null)
- [88: What steps does a server go through to answer a request?](#88-what-steps-does-a-server-go-through-to-answer-a-request)
- [89: What is an AST in GraphQL?](#89-what-is-an-ast-in-graphql)
- [90: What is the `gql` tag?](#90-what-is-the-gql-tag)
- [91: Why would you keep queries in `.graphql` files?](#91-why-would-you-keep-queries-in-graphql-files)
- [92: How is pagination done in GraphQL?](#92-how-is-pagination-done-in-graphql)
- [93: How does offset pagination work?](#93-how-does-offset-pagination-work)
- [94: How does cursor pagination work?](#94-how-does-cursor-pagination-work)
- [95: What is the Relay connection specification?](#95-what-is-the-relay-connection-specification)
- [96: How do you add filtering and sorting to a list field?](#96-how-do-you-add-filtering-and-sorting-to-a-list-field)
- [97: How are subscriptions sent over the network?](#97-how-are-subscriptions-sent-over-the-network)
- [98: What is the `graphql-ws` library?](#98-what-is-the-graphql-ws-library)
- [99: What is `subscriptions-transport-ws`?](#99-what-is-subscriptions-transport-ws)
- [100: What is schema stitching?](#100-what-is-schema-stitching)
- [101: What is Apollo Federation?](#101-what-is-apollo-federation)
- [102: What is a GraphQL gateway or router?](#102-what-is-a-graphql-gateway-or-router)
- [103: What is GraphQL Code Generator?](#103-what-is-graphql-code-generator)
- [104: Why generate TypeScript types from a schema?](#104-why-generate-typescript-types-from-a-schema)
- [105: What is the N+1 problem?](#105-what-is-the-n1-problem)
- [106: What is DataLoader?](#106-what-is-dataloader)
- [107: What is `InMemoryCache` in Apollo Client?](#107-what-is-inmemorycache-in-apollo-client)
- [108: What is a normalized cache?](#108-what-is-a-normalized-cache)
- [109: How do you use `useQuery` in Apollo Client?](#109-how-do-you-use-usequery-in-apollo-client)
- [110: How do you use `useMutation` in Apollo Client?](#110-how-do-you-use-usemutation-in-apollo-client)
- [111: How do you pass variables to `useQuery`?](#111-how-do-you-pass-variables-to-usequery)
- [112: How do you refetch a query in Apollo Client?](#112-how-do-you-refetch-a-query-in-apollo-client)
- [113: What is a fetch policy?](#113-what-is-a-fetch-policy)
- [114: How do you return an error from a resolver?](#114-how-do-you-return-an-error-from-a-resolver)
- [115: What is `GraphQLError`?](#115-what-is-graphqlerror)
- [116: What is the `extensions` field in an error used for?](#116-what-is-the-extensions-field-in-an-error-used-for)
- [117: Which error codes does Apollo Server use?](#117-which-error-codes-does-apollo-server-use)
- [118: How do you authenticate requests to a GraphQL API?](#118-how-do-you-authenticate-requests-to-a-graphql-api)
- [119: Where should authorization checks go?](#119-where-should-authorization-checks-go)
- [120: Why don't GraphQL APIs usually have versions like `/v1` and `/v2`?](#120-why-dont-graphql-apis-usually-have-versions-like-v1-and-v2)
- [121: How do you deprecate a field?](#121-how-do-you-deprecate-a-field)
- [122: Can you deprecate arguments and input fields?](#122-can-you-deprecate-arguments-and-input-fields)
- [123: What is a breaking change in a GraphQL schema?](#123-what-is-a-breaking-change-in-a-graphql-schema)
- [124: Which schema changes are safe?](#124-which-schema-changes-are-safe)
- [125: What is a persisted query?](#125-what-is-a-persisted-query)
- [126: Is GraphQL a database or a query language for databases?](#126-is-graphql-a-database-or-a-query-language-for-databases)
- [127: Which programming languages can you use GraphQL with?](#127-which-programming-languages-can-you-use-graphql-with)
- [128: Can GraphQL sit in front of existing REST APIs?](#128-can-graphql-sit-in-front-of-existing-rest-apis)
- [129: When is REST a better choice than GraphQL?](#129-when-is-rest-a-better-choice-than-graphql)
- [130: How does GraphQL compare to gRPC?](#130-how-does-graphql-compare-to-grpc)
- [131: What does `buildSchema` do in graphql-js?](#131-what-does-buildschema-do-in-graphql-js)
- [132: What does `printSchema` do?](#132-what-does-printschema-do)
- [133: What is `makeExecutableSchema`?](#133-what-is-makeexecutableschema)
- [134: How do you mock a GraphQL schema?](#134-how-do-you-mock-a-graphql-schema)
- [135: How do you test a simple resolver?](#135-how-do-you-test-a-simple-resolver)
- [136: What is `executeOperation` in Apollo Server?](#136-what-is-executeoperation-in-apollo-server)
- [137: Can a field return a list of union or interface types?](#137-can-a-field-return-a-list-of-union-or-interface-types)
- [138: Can input types contain other input types?](#138-can-input-types-contain-other-input-types)
- [139: What does `extend type` do?](#139-what-does-extend-type-do)
- [140: What is a OneOf input object?](#140-what-is-a-oneof-input-object)
- [141: Why use a GraphQL client library instead of plain `fetch`?](#141-why-use-a-graphql-client-library-instead-of-plain-fetch)
- [142: What is the `extensions` key in a request?](#142-what-is-the-extensions-key-in-a-request)
- [143: What is the GraphQL specification?](#143-what-is-the-graphql-specification)
- [144: What is `graphql-config`?](#144-what-is-graphql-config)
- [145: Can variables have default values in an operation?](#145-can-variables-have-default-values-in-an-operation)
- [146: How do you pass a list as an argument?](#146-how-do-you-pass-a-list-as-an-argument)
- [147: Can you use fragments in mutations and subscriptions?](#147-can-you-use-fragments-in-mutations-and-subscriptions)
- [148: What are meta fields?](#148-what-are-meta-fields)
- [149: What does it mean that GraphQL is strongly typed?](#149-what-does-it-mean-that-graphql-is-strongly-typed)
- [150: How would you explain how a GraphQL request works in a few sentences?](#150-how-would-you-explain-how-a-graphql-request-works-in-a-few-sentences)

### Moderate Questions (151-300)

- [151: Why should DataLoader instances be created per request?](#151-why-should-dataloader-instances-be-created-per-request)
- [152: What rules must a DataLoader batch function follow?](#152-what-rules-must-a-dataloader-batch-function-follow)
- [153: How do you write a DataLoader batch function for a SQL database?](#153-how-do-you-write-a-dataloader-batch-function-for-a-sql-database)
- [154: When should you clear or prime the DataLoader cache?](#154-when-should-you-clear-or-prime-the-dataloader-cache)
- [155: How do you implement cursor pagination with a SQL database?](#155-how-do-you-implement-cursor-pagination-with-a-sql-database)
- [156: How should you encode cursors?](#156-how-should-you-encode-cursors)
- [157: Should a connection include `totalCount`?](#157-should-a-connection-include-totalcount)
- [158: What is the Node interface and global object identification?](#158-what-is-the-node-interface-and-global-object-identification)
- [159: How do you design mutation input and payload types?](#159-how-do-you-design-mutation-input-and-payload-types)
- [160: What is the user errors pattern in mutations?](#160-what-is-the-user-errors-pattern-in-mutations)
- [161: How do you model errors as data with unions?](#161-how-do-you-model-errors-as-data-with-unions)
- [162: When should you throw an error and when should you return it as data?](#162-when-should-you-throw-an-error-and-when-should-you-return-it-as-data)
- [163: How do you hide internal error details from clients in production?](#163-how-do-you-hide-internal-error-details-from-clients-in-production)
- [164: How do you create your own error classes for a GraphQL server?](#164-how-do-you-create-your-own-error-classes-for-a-graphql-server)
- [165: How does the error `path` help with partial data?](#165-how-does-the-error-path-help-with-partial-data)
- [166: How do you use Apollo Server 5 with Express?](#166-how-do-you-use-apollo-server-5-with-express)
- [167: How do you authenticate WebSocket subscriptions?](#167-how-do-you-authenticate-websocket-subscriptions)
- [168: How do you write an authorization directive?](#168-how-do-you-write-an-authorization-directive)
- [169: How do you hide a single field from some users?](#169-how-do-you-hide-a-single-field-from-some-users)
- [170: What are Apollo Server plugins?](#170-what-are-apollo-server-plugins)
- [171: How do you write a simple logging plugin for Apollo Server?](#171-how-do-you-write-a-simple-logging-plugin-for-apollo-server)
- [172: How do you configure CORS for a GraphQL server?](#172-how-do-you-configure-cors-for-a-graphql-server)
- [173: How do you set response headers or cookies from a resolver?](#173-how-do-you-set-response-headers-or-cookies-from-a-resolver)
- [174: How do you handle file uploads with GraphQL?](#174-how-do-you-handle-file-uploads-with-graphql)
- [175: What is CSRF prevention in Apollo Server?](#175-what-is-csrf-prevention-in-apollo-server)
- [176: What should you put in the context, and what should you avoid?](#176-what-should-you-put-in-the-context-and-what-should-you-avoid)
- [177: How do you split a large schema into modules?](#177-how-do-you-split-a-large-schema-into-modules)
- [178: How do you merge type definitions and resolvers from many files?](#178-how-do-you-merge-type-definitions-and-resolvers-from-many-files)
- [179: How do you build a schema code-first with Pothos?](#179-how-do-you-build-a-schema-code-first-with-pothos)
- [180: How do you build a GraphQL API with NestJS?](#180-how-do-you-build-a-graphql-api-with-nestjs)
- [181: How do you set up GraphQL Code Generator for a front end?](#181-how-do-you-set-up-graphql-code-generator-for-a-front-end)
- [182: How do you get typed resolvers with GraphQL Code Generator?](#182-how-do-you-get-typed-resolvers-with-graphql-code-generator)
- [183: What is fragment colocation?](#183-what-is-fragment-colocation)
- [184: What is fragment masking?](#184-what-is-fragment-masking)
- [185: How do you set up Apollo Client 4 in a React app?](#185-how-do-you-set-up-apollo-client-4-in-a-react-app)
- [186: How does Apollo Client choose cache IDs, and how do you change it?](#186-how-does-apollo-client-choose-cache-ids-and-how-do-you-change-it)
- [187: What are type policies and field policies in Apollo Client?](#187-what-are-type-policies-and-field-policies-in-apollo-client)
- [188: How do you update the cache after a mutation?](#188-how-do-you-update-the-cache-after-a-mutation)
- [189: What is the difference between `cache.modify`, `cache.writeQuery` and `cache.updateQuery`?](#189-what-is-the-difference-between-cachemodify-cachewritequery-and-cacheupdatequery)
- [190: How do you implement optimistic UI with Apollo Client?](#190-how-do-you-implement-optimistic-ui-with-apollo-client)
- [191: When would you use each fetch policy?](#191-when-would-you-use-each-fetch-policy)
- [192: How do you run a query on demand, like when a button is clicked?](#192-how-do-you-run-a-query-on-demand-like-when-a-button-is-clicked)
- [193: How do you implement infinite scroll with Apollo Client?](#193-how-do-you-implement-infinite-scroll-with-apollo-client)
- [194: How do you poll a query?](#194-how-do-you-poll-a-query)
- [195: What does `errorPolicy` do in Apollo Client?](#195-what-does-errorpolicy-do-in-apollo-client)
- [196: What is Apollo Link?](#196-what-is-apollo-link)
- [197: How do you add an auth header to every request in Apollo Client?](#197-how-do-you-add-an-auth-header-to-every-request-in-apollo-client)
- [198: How do you handle errors globally in Apollo Client?](#198-how-do-you-handle-errors-globally-in-apollo-client)
- [199: How do you retry failed requests in Apollo Client?](#199-how-do-you-retry-failed-requests-in-apollo-client)
- [200: How do you use subscriptions with Apollo Client?](#200-how-do-you-use-subscriptions-with-apollo-client)
- [201: How do you add subscriptions to an Apollo Server app?](#201-how-do-you-add-subscriptions-to-an-apollo-server-app)
- [202: What is PubSub, and why shouldn't you use the in-memory one in production?](#202-what-is-pubsub-and-why-shouldnt-you-use-the-in-memory-one-in-production)
- [203: How do you filter subscription events per client?](#203-how-do-you-filter-subscription-events-per-client)
- [204: How can you use Server-Sent Events for subscriptions instead of WebSockets?](#204-how-can-you-use-server-sent-events-for-subscriptions-instead-of-websockets)
- [205: What is the difference between subscriptions and live queries?](#205-what-is-the-difference-between-subscriptions-and-live-queries)
- [206: Why is HTTP caching harder with GraphQL than with REST?](#206-why-is-http-caching-harder-with-graphql-than-with-rest)
- [207: How can you cache GraphQL responses with a CDN?](#207-how-can-you-cache-graphql-responses-with-a-cdn)
- [208: How do Automatic Persisted Queries work?](#208-how-do-automatic-persisted-queries-work)
- [209: What are trusted documents?](#209-what-are-trusted-documents)
- [210: How do cache control hints work in Apollo Server?](#210-how-do-cache-control-hints-work-in-apollo-server)
- [211: How do you cache whole responses on the server?](#211-how-do-you-cache-whole-responses-on-the-server)
- [212: How do you limit query depth?](#212-how-do-you-limit-query-depth)
- [213: What is query cost analysis?](#213-what-is-query-cost-analysis)
- [214: How do you rate limit a GraphQL API?](#214-how-do-you-rate-limit-a-graphql-api)
- [215: Should you disable introspection in production?](#215-should-you-disable-introspection-in-production)
- [216: What are field suggestions, and why can they be a problem?](#216-what-are-field-suggestions-and-why-can-they-be-a-problem)
- [217: What is query batching, and what are the trade-offs?](#217-what-is-query-batching-and-what-are-the-trade-offs)
- [218: How do you add timeouts to slow resolvers?](#218-how-do-you-add-timeouts-to-slow-resolvers)
- [219: What should you log for GraphQL requests?](#219-what-should-you-log-for-graphql-requests)
- [220: How do you monitor resolver performance per field?](#220-how-do-you-monitor-resolver-performance-per-field)
- [221: How do you write integration tests for a GraphQL API?](#221-how-do-you-write-integration-tests-for-a-graphql-api)
- [222: How do you mock GraphQL requests in front-end tests?](#222-how-do-you-mock-graphql-requests-in-front-end-tests)
- [223: How do you test React components that use Apollo Client?](#223-how-do-you-test-react-components-that-use-apollo-client)
- [224: How do you lint GraphQL schemas and operations?](#224-how-do-you-lint-graphql-schemas-and-operations)
- [225: How do you catch breaking schema changes in CI?](#225-how-do-you-catch-breaking-schema-changes-in-ci)
- [226: What is a schema registry?](#226-what-is-a-schema-registry)
- [227: How should you name mutations?](#227-how-should-you-name-mutations)
- [228: How do you decide whether a field should be nullable?](#228-how-do-you-decide-whether-a-field-should-be-nullable)
- [229: How do you validate input in a GraphQL API?](#229-how-do-you-validate-input-in-a-graphql-api)
- [230: How do you implement a custom scalar?](#230-how-do-you-implement-a-custom-scalar)
- [231: How do you map enum values to different internal values?](#231-how-do-you-map-enum-values-to-different-internal-values)
- [232: How does the server know which type an interface or union value is?](#232-how-does-the-server-know-which-type-an-interface-or-union-value-is)
- [233: What does "Abstract type must resolve to an Object type at runtime" mean?](#233-what-does-abstract-type-must-resolve-to-an-object-type-at-runtime-mean)
- [234: Can an interface implement another interface?](#234-can-an-interface-implement-another-interface)
- [235: How do you query tree-shaped data like comments with replies?](#235-how-do-you-query-tree-shaped-data-like-comments-with-replies)
- [236: What are some validation rules that every GraphQL server checks?](#236-what-are-some-validation-rules-that-every-graphql-server-checks)
- [237: How do you write a custom validation rule?](#237-how-do-you-write-a-custom-validation-rule)
- [238: How should you represent money in a GraphQL schema?](#238-how-should-you-represent-money-in-a-graphql-schema)
- [239: What are the trade-offs of a `JSON` scalar?](#239-what-are-the-trade-offs-of-a-json-scalar)
- [240: How do you use an ORM like Prisma in resolvers?](#240-how-do-you-use-an-orm-like-prisma-in-resolvers)
- [241: How can a resolver load only the columns the query asked for?](#241-how-can-a-resolver-load-only-the-columns-the-query-asked-for)
- [242: What is `RESTDataSource`?](#242-what-is-restdatasource)
- [243: How do you handle a failing downstream service in a resolver?](#243-how-do-you-handle-a-failing-downstream-service-in-a-resolver)
- [244: Where should business logic live in a GraphQL server?](#244-where-should-business-logic-live-in-a-graphql-server)
- [245: How do you make mutations safe to retry?](#245-how-do-you-make-mutations-safe-to-retry)
- [246: How do you design bulk mutations?](#246-how-do-you-design-bulk-mutations)
- [247: If a request has two mutation fields, do they run in one transaction?](#247-if-a-request-has-two-mutation-fields-do-they-run-in-one-transaction)
- [248: What should a delete mutation return?](#248-what-should-a-delete-mutation-return)
- [249: How do you stop clients from asking for huge pages?](#249-how-do-you-stop-clients-from-asking-for-huge-pages)
- [250: How do you add search across several types?](#250-how-do-you-add-search-across-several-types)
- [251: How do you return localized content from a GraphQL API?](#251-how-do-you-return-localized-content-from-a-graphql-api)
- [252: How do you handle multi-tenancy in a GraphQL server?](#252-how-do-you-handle-multi-tenancy-in-a-graphql-server)
- [253: How do you run a GraphQL server in a Next.js route handler?](#253-how-do-you-run-a-graphql-server-in-a-nextjs-route-handler)
- [254: How do you use Apollo Client with the Next.js App Router?](#254-how-do-you-use-apollo-client-with-the-nextjs-app-router)
- [255: What is urql and how is it different from Apollo Client?](#255-what-is-urql-and-how-is-it-different-from-apollo-client)
- [256: What is Relay and what makes it different?](#256-what-is-relay-and-what-makes-it-different)
- [257: How do you use GraphQL with TanStack Query?](#257-how-do-you-use-graphql-with-tanstack-query)
- [258: What is a `TypedDocumentNode`?](#258-what-is-a-typeddocumentnode)
- [259: What is gql.tada?](#259-what-is-gqltada)
- [260: How do you use persisted documents with GraphQL Code Generator?](#260-how-do-you-use-persisted-documents-with-graphql-code-generator)
- [261: How do you refresh an expired access token in Apollo Client?](#261-how-do-you-refresh-an-expired-access-token-in-apollo-client)
- [262: Does Apollo Client send the same query twice if two components ask for it at the same time?](#262-does-apollo-client-send-the-same-query-twice-if-two-components-ask-for-it-at-the-same-time)
- [263: How do you manage local state with Apollo Client?](#263-how-do-you-manage-local-state-with-apollo-client)
- [264: How do you clear the Apollo cache when a user logs out?](#264-how-do-you-clear-the-apollo-cache-when-a-user-logs-out)
- [265: How do you use React Suspense with Apollo Client?](#265-how-do-you-use-react-suspense-with-apollo-client)
- [266: How do you change the Apollo Server landing page?](#266-how-do-you-change-the-apollo-server-landing-page)
- [267: How do you add a health check to a GraphQL server?](#267-how-do-you-add-a-health-check-to-a-graphql-server)
- [268: How do you shut down a GraphQL server without dropping requests?](#268-how-do-you-shut-down-a-graphql-server-without-dropping-requests)
- [269: What is Envelop?](#269-what-is-envelop)
- [270: What is Mercurius?](#270-what-is-mercurius)
- [271: How do you choose a GraphQL server library for Node.js?](#271-how-do-you-choose-a-graphql-server-library-for-nodejs)
- [272: How does GraphQL compare to tRPC?](#272-how-does-graphql-compare-to-trpc)
- [273: What guidelines would you follow when designing a public GraphQL API?](#273-what-guidelines-would-you-follow-when-designing-a-public-graphql-api)
- [274: How do you document a GraphQL schema?](#274-how-do-you-document-a-graphql-schema)
- [275: What is a good workflow for removing a deprecated field?](#275-what-is-a-good-workflow-for-removing-a-deprecated-field)
- [276: How should clients handle new enum values or new union members?](#276-how-should-clients-handle-new-enum-values-or-new-union-members)
- [277: Is changing an argument's default value a breaking change?](#277-is-changing-an-arguments-default-value-a-breaking-change)
- [278: How do you rename a field without breaking clients?](#278-how-do-you-rename-a-field-without-breaking-clients)
- [279: How do you add computed fields to a type?](#279-how-do-you-add-computed-fields-to-a-type)
- [280: Where should arguments go, on root fields or on nested fields?](#280-where-should-arguments-go-on-root-fields-or-on-nested-fields)
- [281: Should relationships be exposed in both directions?](#281-should-relationships-be-exposed-in-both-directions)
- [282: Should you expose your database IDs in the API?](#282-should-you-expose-your-database-ids-in-the-api)
- [283: How do you handle "not sent" versus "set to null" in update inputs?](#283-how-do-you-handle-not-sent-versus-set-to-null-in-update-inputs)
- [284: What is the `me` or `viewer` pattern?](#284-what-is-the-me-or-viewer-pattern)
- [285: How do you design fields that need formatting options, like image sizes?](#285-how-do-you-design-fields-that-need-formatting-options-like-image-sizes)
- [286: How should you handle time zones in a GraphQL API?](#286-how-should-you-handle-time-zones-in-a-graphql-api)
- [287: What happens if a query asks for the same response key with different arguments?](#287-what-happens-if-a-query-asks-for-the-same-response-key-with-different-arguments)
- [288: How do you handle errors for individual items in a list?](#288-how-do-you-handle-errors-for-individual-items-in-a-list)
- [289: What is the difference between per-request caching and cross-request caching in resolvers?](#289-what-is-the-difference-between-per-request-caching-and-cross-request-caching-in-resolvers)
- [290: How do you cache a slow field across requests?](#290-how-do-you-cache-a-slow-field-across-requests)
- [291: How do you avoid request waterfalls on the client?](#291-how-do-you-avoid-request-waterfalls-on-the-client)
- [292: What does `useFragment` do in Apollo Client?](#292-what-does-usefragment-do-in-apollo-client)
- [293: How do you alert on GraphQL errors when the HTTP status is 200?](#293-how-do-you-alert-on-graphql-errors-when-the-http-status-is-200)
- [294: How do you deploy Apollo Server on AWS Lambda?](#294-how-do-you-deploy-apollo-server-on-aws-lambda)
- [295: When should you send GraphQL queries with `GET`?](#295-when-should-you-send-graphql-queries-with-get)
- [296: How do you handle numbers larger than 32 bits?](#296-how-do-you-handle-numbers-larger-than-32-bits)
- [297: Should GraphiQL or Apollo Sandbox be available in production?](#297-should-graphiql-or-apollo-sandbox-be-available-in-production)
- [298: What are `@defer` and `@stream`, and are they standard?](#298-what-are-defer-and-stream-and-are-they-standard)
- [299: How do servers know which client app sent a request?](#299-how-do-servers-know-which-client-app-sent-a-request)
- [300: How would you debug a slow GraphQL query?](#300-how-would-you-debug-a-slow-graphql-query)

### Advanced Questions (301-450)

- [301: Walk through how graphql-js executes an operation.](#301-walk-through-how-graphql-js-executes-an-operation)
- [302: How does field collection handle fragments and duplicates?](#302-how-does-field-collection-handle-fragments-and-duplicates)
- [303: How would you use nullability to create error boundaries in a schema?](#303-how-would-you-use-nullability-to-create-error-boundaries-in-a-schema)
- [304: How does graphql-js handle a mix of sync and async resolvers?](#304-how-does-graphql-js-handle-a-mix-of-sync-and-async-resolvers)
- [305: What is the performance cost of resolvers, and how can you reduce it?](#305-what-is-the-performance-cost-of-resolvers-and-how-can-you-reduce-it)
- [306: Why should you cache parsed and validated documents?](#306-why-should-you-cache-parsed-and-validated-documents)
- [307: What is graphql-jit?](#307-what-is-graphql-jit)
- [308: How does introspection work under the hood?](#308-how-does-introspection-work-under-the-hood)
- [309: How do you get a usable schema object from a running server?](#309-how-do-you-get-a-usable-schema-object-from-a-running-server)
- [310: How do you walk and change a GraphQL AST?](#310-how-do-you-walk-and-change-a-graphql-ast)
- [311: What is `TypeInfo` used for?](#311-what-is-typeinfo-used-for)
- [312: What is the difference between executable directives and type system directives?](#312-what-is-the-difference-between-executable-directives-and-type-system-directives)
- [313: What are directive locations and repeatable directives?](#313-what-are-directive-locations-and-repeatable-directives)
- [314: How do you write a schema directive that changes field results?](#314-how-do-you-write-a-schema-directive-that-changes-field-results)
- [315: What rules apply to OneOf input objects?](#315-what-rules-apply-to-oneof-input-objects)
- [316: What are the rules when a type implements an interface?](#316-what-are-the-rules-when-a-type-implements-an-interface)
- [317: What are the input coercion rules in GraphQL?](#317-what-are-the-input-coercion-rules-in-graphql)
- [318: What are the result coercion rules?](#318-what-are-the-result-coercion-rules)
- [319: When can a nullable variable be used for a non-null argument?](#319-when-can-a-nullable-variable-be-used-for-a-non-null-argument)
- [320: What denial of service risks are specific to GraphQL?](#320-what-denial-of-service-risks-are-specific-to-graphql)
- [321: How can aliases be used for brute-force attacks?](#321-how-can-aliases-be-used-for-brute-force-attacks)
- [322: Why do field duplication and directive overloading cause problems?](#322-why-do-field-duplication-and-directive-overloading-cause-problems)
- [323: How does GraphQL protect against circular fragments?](#323-how-does-graphql-protect-against-circular-fragments)
- [324: How can introspection be used for denial of service?](#324-how-can-introspection-be-used-for-denial-of-service)
- [325: How do injection attacks happen in GraphQL APIs?](#325-how-do-injection-attacks-happen-in-graphql-apis)
- [326: Why is authorization easy to get wrong with GraphQL?](#326-why-is-authorization-easy-to-get-wrong-with-graphql)
- [327: What is an IDOR, and how does it show up in GraphQL?](#327-what-is-an-idor-and-how-does-it-show-up-in-graphql)
- [328: How can error messages leak information, and how do you prevent it?](#328-how-can-error-messages-leak-information-and-how-do-you-prevent-it)
- [329: Why must mutations never run over `GET`?](#329-why-must-mutations-never-run-over-get)
- [330: What does using trusted documents protect against, and what doesn't it protect against?](#330-what-does-using-trusted-documents-protect-against-and-what-doesnt-it-protect-against)
- [331: How would you implement a simple query cost calculation?](#331-how-would-you-implement-a-simple-query-cost-calculation)
- [332: What happens to a running query when the client disconnects?](#332-what-happens-to-a-running-query-when-the-client-disconnects)
- [333: How do you limit the size of incoming documents?](#333-how-do-you-limit-the-size-of-incoming-documents)
- [334: Explain the architecture of Apollo Federation.](#334-explain-the-architecture-of-apollo-federation)
- [335: What are entities and the `@key` directive?](#335-what-are-entities-and-the-key-directive)
- [336: What does `__resolveReference` do?](#336-what-does-__resolvereference-do)
- [337: What do `@shareable`, `@external`, `@requires` and `@provides` do?](#337-what-do-shareable-external-requires-and-provides-do)
- [338: How do you move a field from one subgraph to another with Federation?](#338-how-do-you-move-a-field-from-one-subgraph-to-another-with-federation)
- [339: What is a query plan in Federation?](#339-what-is-a-query-plan-in-federation)
- [340: What changed between Federation 1 and Federation 2?](#340-what-changed-between-federation-1-and-federation-2)
- [341: What are composition errors, and how do you avoid them?](#341-what-are-composition-errors-and-how-do-you-avoid-them)
- [342: What is the difference between Apollo Router and Apollo Gateway?](#342-what-is-the-difference-between-apollo-router-and-apollo-gateway)
- [343: What alternatives are there to Apollo's federation tools?](#343-what-alternatives-are-there-to-apollos-federation-tools)
- [344: How does schema stitching compare to Federation?](#344-how-does-schema-stitching-compare-to-federation)
- [345: What is the GraphQL Composite Schemas specification?](#345-what-is-the-graphql-composite-schemas-specification)
- [346: How do you decide where to split subgraphs?](#346-how-do-you-decide-where-to-split-subgraphs)
- [347: How does the router fetch entities from a subgraph?](#347-how-does-the-router-fetch-entities-from-a-subgraph)
- [348: How do you trace a request across a router and its subgraphs?](#348-how-do-you-trace-a-request-across-a-router-and-its-subgraphs)
- [349: How do subscriptions work with Federation?](#349-how-do-subscriptions-work-with-federation)
- [350: How do you scale GraphQL subscriptions?](#350-how-do-you-scale-graphql-subscriptions)
- [351: What happens when a subscription produces events faster than a client can receive them?](#351-what-happens-when-a-subscription-produces-events-faster-than-a-client-can-receive-them)
- [352: How do you handle an access token that expires during a long WebSocket connection?](#352-how-do-you-handle-an-access-token-that-expires-during-a-long-websocket-connection)
- [353: How does `@defer` work on the wire?](#353-how-does-defer-work-on-the-wire)
- [354: When is `@defer` worth using, and when is it not?](#354-when-is-defer-worth-using-and-when-is-it-not)
- [355: How do you invalidate a server-side response cache correctly?](#355-how-do-you-invalidate-a-server-side-response-cache-correctly)
- [356: What can go wrong when caching GraphQL responses in a CDN?](#356-what-can-go-wrong-when-caching-graphql-responses-in-a-cdn)
- [357: Why does Apollo Client sometimes warn "Cache data may be lost when replacing the field"?](#357-why-does-apollo-client-sometimes-warn-cache-data-may-be-lost-when-replacing-the-field)
- [358: What is a cache redirect in Apollo Client?](#358-what-is-a-cache-redirect-in-apollo-client)
- [359: What problems come up with paginated lists in a normalized cache?](#359-what-problems-come-up-with-paginated-lists-in-a-normalized-cache)
- [360: What can go wrong with optimistic updates when several mutations run at once?](#360-what-can-go-wrong-with-optimistic-updates-when-several-mutations-run-at-once)
- [361: How do you keep the Apollo Client cache from growing forever?](#361-how-do-you-keep-the-apollo-client-cache-from-growing-forever)
- [362: What does it mean to design a schema from the client's needs?](#362-what-does-it-mean-to-design-a-schema-from-the-clients-needs)
- [363: What are the trade-offs of generating a GraphQL API directly from a database?](#363-what-are-the-trade-offs-of-generating-a-graphql-api-directly-from-a-database)
- [364: How do you model a state machine, like order status, in a schema?](#364-how-do-you-model-a-state-machine-like-order-status-in-a-schema)
- [365: How do you handle cursor pagination when new items keep being added?](#365-how-do-you-handle-cursor-pagination-when-new-items-keep-being-added)
- [366: How do you implement backward pagination with `last` and `before`?](#366-how-do-you-implement-backward-pagination-with-last-and-before)
- [367: How do you paginate by a column that isn't unique?](#367-how-do-you-paginate-by-a-column-that-isnt-unique)
- [368: How would you design global IDs so they can change later?](#368-how-would-you-design-global-ids-so-they-can-change-later)
- [369: How do you model polymorphic data that's stored in one database table?](#369-how-do-you-model-polymorphic-data-thats-stored-in-one-database-table)
- [370: How do you expose different parts of a schema to different audiences?](#370-how-do-you-expose-different-parts-of-a-schema-to-different-audiences)
- [371: How do you collect field usage data, and what do you use it for?](#371-how-do-you-collect-field-usage-data-and-what-do-you-use-it-for)
- [372: How do you manage a GraphQL schema across many teams?](#372-how-do-you-manage-a-graphql-schema-across-many-teams)
- [373: How would you set up code generation in a monorepo with a GraphQL server and several clients?](#373-how-would-you-set-up-code-generation-in-a-monorepo-with-a-graphql-server-and-several-clients)
- [374: What does a schema-first design process look like for a new feature?](#374-what-does-a-schema-first-design-process-look-like-for-a-new-feature)
- [375: How do you find what's slow inside a Node.js GraphQL server?](#375-how-do-you-find-whats-slow-inside-a-nodejs-graphql-server)
- [376: How do you benchmark a GraphQL server?](#376-how-do-you-benchmark-a-graphql-server)
- [377: How does DataLoader decide when to run a batch?](#377-how-does-dataloader-decide-when-to-run-a-batch)
- [378: How do you use DataLoader with composite keys?](#378-how-do-you-use-dataloader-with-composite-keys)
- [379: How do you batch a paginated relation, like the first 5 posts of each user?](#379-how-do-you-batch-a-paginated-relation-like-the-first-5-posts-of-each-user)
- [380: What should you watch out for when DataLoader batches get very large?](#380-what-should-you-watch-out-for-when-dataloader-batches-get-very-large)
- [381: How do database connection pools interact with GraphQL concurrency?](#381-how-do-database-connection-pools-interact-with-graphql-concurrency)
- [382: How can `AsyncLocalStorage` help in a GraphQL server?](#382-how-can-asynclocalstorage-help-in-a-graphql-server)
- [383: How can Postgres row-level security work together with a GraphQL API?](#383-how-can-postgres-row-level-security-work-together-with-a-graphql-api)
- [384: What are the trade-offs of running a GraphQL server on serverless functions?](#384-what-are-the-trade-offs-of-running-a-graphql-server-on-serverless-functions)
- [385: Can you run GraphQL on edge runtimes like Cloudflare Workers?](#385-can-you-run-graphql-on-edge-runtimes-like-cloudflare-workers)
- [386: How do you reduce the size of GraphQL responses?](#386-how-do-you-reduce-the-size-of-graphql-responses)
- [387: How do you make sure client operations stay valid against the server schema?](#387-how-do-you-make-sure-client-operations-stay-valid-against-the-server-schema)
- [388: What is a schema snapshot test, and why use one?](#388-what-is-a-schema-snapshot-test-and-why-use-one)
- [389: How would you migrate an existing REST API to GraphQL?](#389-how-would-you-migrate-an-existing-rest-api-to-graphql)
- [390: When would you use GraphQL as a backend-for-frontend instead of one company-wide graph?](#390-when-would-you-use-graphql-as-a-backend-for-frontend-instead-of-one-company-wide-graph)
- [391: How would you migrate from schema stitching to Federation?](#391-how-would-you-migrate-from-schema-stitching-to-federation)
- [392: What changes when you upgrade from Apollo Server 4 to Apollo Server 5?](#392-what-changes-when-you-upgrade-from-apollo-server-4-to-apollo-server-5)
- [393: What are the main changes when moving from Apollo Client 3 to Apollo Client 4?](#393-what-are-the-main-changes-when-moving-from-apollo-client-3-to-apollo-client-4)
- [394: How do you migrate from `subscriptions-transport-ws` to `graphql-ws`?](#394-how-do-you-migrate-from-subscriptions-transport-ws-to-graphql-ws)
- [395: What should you know about upgrading from graphql-js 16 to 17?](#395-what-should-you-know-about-upgrading-from-graphql-js-16-to-17)
- [396: What is in the September 2025 edition of the GraphQL spec?](#396-what-is-in-the-september-2025-edition-of-the-graphql-spec)
- [397: What are fragment arguments?](#397-what-are-fragment-arguments)
- [398: What proposals exist for changing how errors and nullability work?](#398-what-proposals-exist-for-changing-how-errors-and-nullability-work)
- [399: How do you handle schema changes when old mobile app versions stay in use for months?](#399-how-do-you-handle-schema-changes-when-old-mobile-app-versions-stay-in-use-for-months)
- [400: What race conditions can happen between subscription events and mutation responses?](#400-what-race-conditions-can-happen-between-subscription-events-and-mutation-responses)
- [401: A list screen in the mobile app takes 4 seconds to load. How would you investigate?](#401-a-list-screen-in-the-mobile-app-takes-4-seconds-to-load-how-would-you-investigate)
- [402: One query brought the production API down. What do you do now and later?](#402-one-query-brought-the-production-api-down-what-do-you-do-now-and-later)
- [403: A client reports that a field is `null` and the response has errors. How do you debug it?](#403-a-client-reports-that-a-field-is-null-and-the-response-has-errors-how-do-you-debug-it)
- [404: Design a GraphQL schema for a shopping cart.](#404-design-a-graphql-schema-for-a-shopping-cart)
- [405: Design a chat feature with GraphQL subscriptions.](#405-design-a-chat-feature-with-graphql-subscriptions)
- [406: A developer wants to add `ssn` to the `User` type. What do you think about?](#406-a-developer-wants-to-add-ssn-to-the-user-type-what-do-you-think-about)
- [407: After a mutation, the UI still shows old data. How do you fix it?](#407-after-a-mutation-the-ui-still-shows-old-data-how-do-you-fix-it)
- [408: Users see duplicate items in an infinite scroll list. What's going on?](#408-users-see-duplicate-items-in-an-infinite-scroll-list-whats-going-on)
- [409: A security review found that users can read other users' orders through `node(id:)`. How do you fix it and prevent it again?](#409-a-security-review-found-that-users-can-read-other-users-orders-through-nodeid-how-do-you-fix-it-and-prevent-it-again)
- [410: Tracing shows 300 database queries for a single request. What do you do?](#410-tracing-shows-300-database-queries-for-a-single-request-what-do-you-do)
- [411: You need to rename a type in a public schema. How do you do it?](#411-you-need-to-rename-a-type-in-a-public-schema-how-do-you-do-it)
- [412: How would you design rate limiting for a public GraphQL API?](#412-how-would-you-design-rate-limiting-for-a-public-graphql-api)
- [413: You're starting a new product. How do you decide between REST and GraphQL?](#413-youre-starting-a-new-product-how-do-you-decide-between-rest-and-graphql)
- [414: Five teams want to contribute to one GraphQL API. How do you set it up?](#414-five-teams-want-to-contribute-to-one-graphql-api-how-do-you-set-it-up)
- [415: One subgraph is down. What happens to queries, and how do you make it fail better?](#415-one-subgraph-is-down-what-happens-to-queries-and-how-do-you-make-it-fail-better)
- [416: All GraphQL traffic is `POST /graphql` with status 200. What problems does this cause with API gateways and WAFs, and how do you deal with it?](#416-all-graphql-traffic-is-post-graphql-with-status-200-what-problems-does-this-cause-with-api-gateways-and-wafs-and-how-do-you-deal-with-it)
- [417: The front-end team says the schema is hard to use. How do you approach it?](#417-the-front-end-team-says-the-schema-is-hard-to-use-how-do-you-approach-it)
- [418: How do you model a mutation that takes minutes to finish, like generating a report?](#418-how-do-you-model-a-mutation-that-takes-minutes-to-finish-like-generating-a-report)
- [419: A user wants to export 2 million rows as CSV. Should that go through GraphQL?](#419-a-user-wants-to-export-2-million-rows-as-csv-should-that-go-through-graphql)
- [420: A dashboard has 20 widgets, each with its own query. How would you improve it?](#420-a-dashboard-has-20-widgets-each-with-its-own-query-how-would-you-improve-it)
- [421: Subscription clients connect fine but never receive events. How do you debug it?](#421-subscription-clients-connect-fine-but-never-receive-events-how-do-you-debug-it)
- [422: With Apollo Client and SSR, the page renders, then flickers and refetches on the client. Why?](#422-with-apollo-client-and-ssr-the-page-renders-then-flickers-and-refetches-on-the-client-why)
- [423: What would you check in a code review of a schema change?](#423-what-would-you-check-in-a-code-review-of-a-schema-change)
- [424: What would you check in a code review of resolvers?](#424-what-would-you-check-in-a-code-review-of-resolvers)
- [425: What mistakes do teams commonly make when adopting GraphQL?](#425-what-mistakes-do-teams-commonly-make-when-adopting-graphql)
- [426: How would you explain GraphQL to a back-end developer who knows REST well?](#426-how-would-you-explain-graphql-to-a-back-end-developer-who-knows-rest-well)
- [427: Design the schema for a multi-step checkout.](#427-design-the-schema-for-a-multi-step-checkout)
- [428: How would you implement profile picture uploads end to end?](#428-how-would-you-implement-profile-picture-uploads-end-to-end)
- [429: A query is fast for most users but very slow for admins. What might cause it?](#429-a-query-is-fast-for-most-users-but-very-slow-for-admins-what-might-cause-it)
- [430: Memory usage of the GraphQL server grows until it crashes. Where do you look?](#430-memory-usage-of-the-graphql-server-grows-until-it-crashes-where-do-you-look)
- [431: The web app and the mobile app need different shapes of the same data. What do you do?](#431-the-web-app-and-the-mobile-app-need-different-shapes-of-the-same-data-what-do-you-do)
- [432: How do you change a field from `String` to an enum without breaking clients?](#432-how-do-you-change-a-field-from-string-to-an-enum-without-breaking-clients)
- [433: You want to make a field non-null, but old records in the database have `null` there. What do you do?](#433-you-want-to-make-a-field-non-null-but-old-records-in-the-database-have-null-there-what-do-you-do)
- [434: A partner company wants access to your GraphQL API. What do you set up?](#434-a-partner-company-wants-access-to-your-graphql-api-what-do-you-set-up)
- [435: How do you add audit logging for mutations?](#435-how-do-you-add-audit-logging-for-mutations)
- [436: How do you handle soft-deleted records in a GraphQL API?](#436-how-do-you-handle-soft-deleted-records-in-a-graphql-api)
- [437: The design needs page numbers, but you use cursor pagination. What can you do?](#437-the-design-needs-page-numbers-but-you-use-cursor-pagination-what-can-you-do)
- [438: The app sends 200 GraphQL queries at startup. How do you fix it?](#438-the-app-sends-200-graphql-queries-at-startup-how-do-you-fix-it)
- [439: Error rates spike right after a deploy that changed the schema. What do you do?](#439-error-rates-spike-right-after-a-deploy-that-changed-the-schema-what-do-you-do)
- [440: The iOS app crashes because a field the client thought was non-null returned `null`. How do you prevent this?](#440-the-ios-app-crashes-because-a-field-the-client-thought-was-non-null-returned-null-how-do-you-prevent-this)
- [441: After adding a federation router, response times went up. Where would you look?](#441-after-adding-a-federation-router-response-times-went-up-where-would-you-look)
- [442: Thousands of people are viewing a product page and you need to show live stock levels. How would you do it?](#442-thousands-of-people-are-viewing-a-product-page-and-you-need-to-show-live-stock-levels-how-would-you-do-it)
- [443: How would you expose feature flags through GraphQL?](#443-how-would-you-expose-feature-flags-through-graphql)
- [444: For a new public API, would you use error unions or a `userErrors` list in mutation payloads?](#444-for-a-new-public-api-would-you-use-error-unions-or-a-usererrors-list-in-mutation-payloads)
- [445: Someone found internal fields like `internalNotes` and `costPrice` through introspection. What do you do?](#445-someone-found-internal-fields-like-internalnotes-and-costprice-through-introspection-what-do-you-do)
- [446: A developer adds `allUsers: [User!]!` to the schema with no arguments. What feedback do you give?](#446-a-developer-adds-allusers-user-to-the-schema-with-no-arguments-what-feedback-do-you-give)
- [447: How do you make a GraphQL API easy for LLM agents to use?](#447-how-do-you-make-a-graphql-api-easy-for-llm-agents-to-use)
- [448: What are the main strengths and weaknesses of GraphQL?](#448-what-are-the-main-strengths-and-weaknesses-of-graphql)
- [449: What would you include in a GraphQL style guide for your team?](#449-what-would-you-include-in-a-graphql-style-guide-for-your-team)
- [450: Walk through what happens, step by step, when a client sends a query to Apollo Server with DataLoader.](#450-walk-through-what-happens-step-by-step-when-a-client-sends-a-query-to-apollo-server-with-dataloader)

---

## Easy Questions (1-150)

### 1: What is GraphQL?

GraphQL is a query language for APIs and a runtime on the server that answers those queries. The server describes all the data it can return in a typed schema, and the client sends a query that says exactly which fields it wants. The response has the same shape as the query.

```graphql
query {
  user(id: "1") {
    name
    email
  }
}
```

```json
{ "data": { "user": { "name": "Ana", "email": "ana@example.com" } } }
```

### 2: Who created GraphQL and who maintains it now?

Facebook built GraphQL in 2012 for its mobile apps and made it public in 2015. In 2018 it moved to the GraphQL Foundation, which is part of the Linux Foundation. The foundation looks after the specification and the reference implementation, graphql-js.

### 3: What problems does GraphQL solve compared to REST?

With REST you often call several endpoints to build one screen, and each endpoint returns a fixed shape that may have too much or too little data. GraphQL lets the client get everything for a screen in one request and pick only the fields it needs. You also get a typed schema that works as documentation, and tools can check queries against it before they run.

### 4: What is over-fetching?

Over-fetching is getting more data than you need. For example, `GET /users/1` returns 30 fields but the page only shows the name and avatar. In GraphQL the client asks only for `name` and `avatarUrl`, so the extra fields are not sent.

### 5: What is under-fetching?

Under-fetching is when one request doesn't return enough data, so you need more calls. A common case is loading a user, then their posts, then the comments for each post. In GraphQL you can ask for the nested data in one query:

```graphql
query {
  user(id: "1") {
    name
    posts {
      title
      comments {
        text
      }
    }
  }
}
```

### 6: What is a GraphQL schema?

The schema is the contract between the client and the server. It lists every type, every field on those types, the arguments fields take and what they return. The server checks every incoming query against the schema, so a query for a field that doesn't exist is rejected before any code runs.

### 7: What is SDL?

SDL stands for Schema Definition Language. It is the text syntax for writing a GraphQL schema.

```graphql
type User {
  id: ID!
  name: String!
  posts: [Post!]!
}

type Post {
  id: ID!
  title: String!
}

type Query {
  user(id: ID!): User
}
```

### 8: What are the three root operation types?

`Query` for reading data, `Mutation` for changing data and `Subscription` for getting updates pushed from the server. Only `Query` is required. Every operation a client sends starts at one of these root types.

### 9: What is a query?

A query is a read operation. It starts at the `Query` type and selects fields from it. Queries should not change data on the server, which also lets the server run the top-level fields in parallel.

```graphql
query GetProducts {
  products(first: 10) {
    id
    name
    price
  }
}
```

### 10: What is a mutation?

A mutation is an operation that changes data, like creating, updating or deleting something. It usually returns the changed object so the client can update its view without another request.

```graphql
mutation AddTodo {
  addTodo(text: "Buy milk") {
    id
    text
    done
  }
}
```

### 11: What is a subscription?

A subscription is a long-lived operation. The client subscribes once, and the server sends a new result every time a certain event happens, such as a new chat message. It usually runs over WebSockets or Server-Sent Events.

```graphql
subscription OnMessage {
  messageAdded(roomId: "42") {
    id
    text
    author {
      name
    }
  }
}
```

### 12: What is a resolver?

A resolver is a function that returns the value for one field. When a query runs, the server calls the resolver for each field in the query. Resolvers can read from a database, call another API or just return a value from the parent object.

```js
const resolvers = {
  Query: {
    user: (parent, args, context) => context.db.users.findById(args.id),
  },
};
```

### 13: What arguments does a resolver receive?

A resolver gets four arguments:

- `parent` (also called `root` or `source`): the value returned by the parent field's resolver.
- `args`: the arguments passed to this field in the query.
- `context`: an object shared by all resolvers in one request, often holding the logged-in user, database clients and loaders.
- `info`: details about the current execution, like the field name, the path and the schema.

```js
const resolvers = {
  User: {
    posts: (parent, args, context, info) =>
      context.db.posts.findByAuthor(parent.id, { limit: args.first }),
  },
};
```

### 14: What are the built-in scalar types?

There are five: `Int` (signed 32-bit integer), `Float` (double-precision number), `String` (UTF-8 text), `Boolean` and `ID`. Scalars are the leaves of a query, which means they have no subfields.

### 15: What is the ID type?

`ID` is a scalar for unique identifiers. It is serialized as a string, even if the value in your database is a number. Using `ID` instead of `String` tells clients and caching tools that this field identifies an object and is not meant to be shown to users.

### 16: What is an object type?

An object type is a type with named fields, each with its own type. Most of a schema is made of object types.

```graphql
type Book {
  id: ID!
  title: String!
  author: Author!
  publishedYear: Int
}
```

### 17: What is a field in GraphQL?

A field is a named piece of data on a type. It has a return type and can take arguments. In a query, you choose fields to get their values. Fields can return scalars, enums, objects, lists or abstract types like interfaces and unions.

### 18: What does the exclamation mark mean in a type?

`!` means non-null. `String!` means the field always returns a string and never `null`. Without `!`, the field is nullable. On arguments and input fields, `!` means the client must provide a value.

### 19: How do you define a list type?

Wrap the type in square brackets.

```graphql
type User {
  tags: [String!]!
  friends: [User!]
}
```

`tags` always returns a list (maybe empty) and none of its items are null. `friends` can be `null`, but if it's a list, the items are never null.

### 20: What is the difference between `[String]`, `[String!]`, `[String]!` and `[String!]!`?

- `[String]`: the list can be null, and items can be null.
- `[String!]`: the list can be null, but items can't.
- `[String]!`: the list can't be null, but items can.
- `[String!]!`: neither the list nor its items can be null.

`[String!]!` is the most common choice for lists, because clients don't have to check for null in two places.

### 21: What is an enum type?

An enum is a type that allows only a fixed set of values. The values are usually written in uppercase.

```graphql
enum OrderStatus {
  PENDING
  PAID
  SHIPPED
  CANCELLED
}

type Order {
  id: ID!
  status: OrderStatus!
}
```

If a client sends or the server returns a value that is not in the list, it's an error.

### 22: What is an input type?

An input type is an object type used for arguments. It groups several values so you can pass them as one argument, which is common in mutations.

```graphql
input CreateUserInput {
  name: String!
  email: String!
  role: Role = USER
}

type Mutation {
  createUser(input: CreateUserInput!): User!
}
```

### 23: Why can't you use an object type as an argument?

Object types can have fields with arguments, can point to interfaces and unions, and can form cycles that are resolved lazily. None of that makes sense for data the client sends. Input types are kept separate so they can only contain scalars, enums, lists and other input types, which the server can validate easily.

### 24: What is an interface?

An interface is an abstract type that lists fields other types must have. Any type that implements it must include those fields with compatible types.

```graphql
interface Node {
  id: ID!
}

type User implements Node {
  id: ID!
  name: String!
}

type Product implements Node {
  id: ID!
  title: String!
}
```

A field that returns `Node` can return a `User` or a `Product`.

### 25: What is a union type?

A union is an abstract type that can be one of several object types. Unlike an interface, the types don't need to share any fields.

```graphql
union SearchResult = User | Product | Article

type Query {
  search(text: String!): [SearchResult!]!
}
```

### 26: What is the difference between an interface and a union?

An interface defines shared fields, so you can query those fields directly without knowing the exact type. A union has no shared fields, so you must use fragments to select anything except `__typename`. Use an interface when the types really have something in common, and a union when they are unrelated but can show up in the same place, like search results.

### 27: How do arguments work on fields?

Any field can take arguments, not only root fields. That's one of the big differences from REST, where you only have query parameters on the URL.

```graphql
query {
  user(id: "1") {
    name
    avatar(size: 64)
    posts(first: 5, orderBy: NEWEST) {
      title
    }
  }
}
```

### 28: How do you give an argument a default value?

Put `= value` after the type in the schema. If the client leaves the argument out, the server uses the default.

```graphql
type Query {
  products(first: Int = 20, sort: SortOrder = ASC): [Product!]!
}
```

### 29: What are variables in GraphQL?

Variables let you pass dynamic values to an operation without changing the query text. You declare them in the operation with a `$` and a type, use them in arguments, and send their values in a separate JSON object.

```graphql
query GetUser($id: ID!) {
  user(id: $id) {
    name
  }
}
```

```json
{ "id": "1" }
```

### 30: Why should you use variables instead of building the query string yourself?

If you build the string by hand, you need to escape values yourself, and a bad value can break the query or change it. With variables, the query text stays the same and only the values change. That also means the server and client can cache the parsed query, and tools like persisted queries work because the text never changes.

### 31: What is an operation name and why should you use it?

The operation name is the name after `query`, `mutation` or `subscription`, like `GetUser` in `query GetUser { ... }`. It's optional for a single operation, but you should always add one. It shows up in server logs, tracing and dev tools, so you can tell which screen sent which request.

### 32: What is an alias?

An alias renames a field in the response. You need it when you ask for the same field twice with different arguments, because the response keys would clash otherwise.

```graphql
query {
  small: avatar(size: 32)
  large: avatar(size: 256)
}
```

```json
{ "data": { "small": "https://...32.png", "large": "https://...256.png" } }
```

### 33: What is a fragment?

A fragment is a reusable set of fields for a type. You define it once and spread it with `...` wherever you need those fields.

```graphql
fragment UserCard on User {
  id
  name
  avatarUrl
}

query {
  me {
    ...UserCard
  }
  user(id: "2") {
    ...UserCard
  }
}
```

### 34: What is an inline fragment?

An inline fragment is a fragment without a name, written directly in the query. It is mostly used to select fields on a specific type when the field returns an interface or union.

```graphql
query {
  search(text: "graphql") {
    __typename
    ... on User {
      name
    }
    ... on Product {
      title
      price
    }
  }
}
```

### 35: What is `__typename`?

`__typename` is a meta field you can ask for on any object. It returns the name of the object's type as a string, like `"User"`. Clients use it to tell union and interface members apart, and normalized caches like Apollo Client add it to queries automatically to build cache keys.

### 36: What are directives?

Directives are annotations that start with `@`. They can be used in queries to change how execution works, or in the schema to add metadata. Built-in ones include `@include`, `@skip`, `@deprecated`, `@specifiedBy` and `@oneOf`. Servers and tools can also define their own.

### 37: How do `@include` and `@skip` work?

Both take a `Boolean` argument named `if`. `@include(if: true)` keeps the field, `@skip(if: true)` removes it. They are usually used with variables.

```graphql
query GetUser($id: ID!, $withPosts: Boolean!) {
  user(id: $id) {
    name
    posts @include(if: $withPosts) {
      title
    }
  }
}
```

### 38: What does `@deprecated` do?

It marks a field, enum value, argument or input field as deprecated, with an optional reason. It still works, but introspection shows it as deprecated and tools like GraphiQL and IDE plugins warn developers who use it.

```graphql
type User {
  name: String!
  fullName: String @deprecated(reason: "Use `name` instead.")
}
```

### 39: What does `@specifiedBy` do?

It is used on custom scalars to point to a document that describes how the scalar works. It doesn't change anything at runtime, but tools and developers can see what format to expect.

```graphql
scalar DateTime
  @specifiedBy(url: "https://scalars.graphql.org/andimarek/date-time")
```

### 40: What is introspection?

Introspection is the ability to query the schema itself. Every GraphQL server supports special fields like `__schema` and `__type` that return information about types, fields and directives. Tools like GraphiQL, code generators and IDE plugins use it to get the schema.

### 41: How do you query the schema with introspection?

You use the `__schema` or `__type` fields.

```graphql
query {
  __type(name: "User") {
    name
    fields {
      name
      type {
        name
        kind
      }
    }
  }
}
```

In graphql-js you can get the full introspection query text from `getIntrospectionQuery()`.

### 42: What does a GraphQL response look like?

A response is a JSON object with up to three top-level keys: `data` with the result, `errors` with a list of errors if any happened, and `extensions` for extra information like tracing or cost. If there are no errors, the `errors` key is left out.

```json
{
  "data": { "user": { "name": "Ana" } }
}
```

### 43: What does the `errors` array contain?

Each error has a `message`, and usually `locations` (line and column in the query) and `path` (the field in the response where it happened). Servers can add more details in `extensions`, like an error `code`.

```json
{
  "errors": [
    {
      "message": "User not found",
      "locations": [{ "line": 2, "column": 3 }],
      "path": ["user"],
      "extensions": { "code": "NOT_FOUND" }
    }
  ],
  "data": { "user": null }
}
```

### 44: Can a response have both `data` and `errors`?

Yes. If one field fails, the server sets that field to `null`, adds an error and still returns the other fields. This is called a partial response. The client should check both keys and not assume that an error means no data.

### 45: Which HTTP method does GraphQL usually use?

Most requests use `POST` with a JSON body. Queries can also be sent with `GET`, where the query and variables go in the URL. Mutations should never be sent with `GET`, and most servers reject that.

### 46: Is GraphQL tied to HTTP?

No. The spec only describes the language, the type system and how execution works. HTTP is the most common transport, but GraphQL also runs over WebSockets, Server-Sent Events or even directly in code without any network, for example by calling `graphql()` from graphql-js in a test.

### 47: What does a GraphQL request body look like?

A JSON object with `query`, and optionally `variables`, `operationName` and `extensions`.

```json
{
  "query": "query GetUser($id: ID!) { user(id: $id) { name } }",
  "variables": { "id": "1" },
  "operationName": "GetUser"
}
```

### 48: How do you send a GraphQL query with `fetch`?

You don't need a library for a simple request. Send a `POST` with a JSON body.

```js
const res = await fetch("/graphql", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    query: "query GetUser($id: ID!) { user(id: $id) { name } }",
    variables: { id: "1" },
  }),
});

const { data, errors } = await res.json();
```

### 49: Why does a GraphQL API usually have one endpoint?

All operations go to the same URL, like `/graphql`, because the query itself says what data you want. There is no need for a URL per resource. This makes routing simple, but it also means you can't rely on URL-based caching, logging or rate limiting the way you would with REST.

### 50: What is the GraphQL over HTTP specification?

It's a separate spec from the GraphQL Foundation that describes how to send GraphQL over HTTP: which methods to use, how to encode `GET` requests, which content types to accept and which status codes to return. It introduced the `application/graphql-response+json` media type, which lets servers use proper HTTP status codes for errors. Most modern servers, like Apollo Server and GraphQL Yoga, follow it.

### 51: What HTTP status code does a GraphQL server return when something fails?

It depends. With the classic `application/json` response type, servers often return `200 OK` even if the `errors` array is not empty, because part of the request may have worked. Requests that can't run at all, like a syntax error or a failed validation, usually get a `400`. With the newer `application/graphql-response+json` type from the GraphQL over HTTP spec, servers return a 4xx status when the request fails before execution, so HTTP tools can see the problem.

### 52: What is GraphiQL?

GraphiQL is an in-browser IDE for GraphQL, maintained by the GraphQL Foundation. It reads the schema with introspection and gives you autocomplete, error highlighting, a docs explorer and a place to run queries. Many servers, like GraphQL Yoga, serve it at the GraphQL endpoint in development.

### 53: What other tools can you use to explore a GraphQL API?

- Apollo Sandbox and Apollo Explorer, which Apollo Server shows as its landing page in development.
- Postman and Insomnia, which both support GraphQL requests with schema autocomplete.
- Altair, a desktop and browser GraphQL client.
- IDE plugins like the GraphQL extension for VS Code, which give autocomplete and validation inside `.graphql` files and `gql` tags.

### 54: What is Apollo Server?

Apollo Server is a popular open-source GraphQL server for Node.js, made by Apollo. You give it type definitions and resolvers (or a ready schema), and it handles parsing, validation, execution, error formatting and plugins. The current major version is Apollo Server 5, published as the `@apollo/server` package.

### 55: How do you create a simple server with Apollo Server?

```js
import { ApolloServer } from "@apollo/server";
import { startStandaloneServer } from "@apollo/server/standalone";

const typeDefs = `#graphql
  type Query {
    hello(name: String): String!
  }
`;

const resolvers = {
  Query: {
    hello: (_, { name }) => `Hello, ${name ?? "world"}!`,
  },
};

const server = new ApolloServer({ typeDefs, resolvers });
const { url } = await startStandaloneServer(server, { listen: { port: 4000 } });
console.log(`Server ready at ${url}`);
```

`startStandaloneServer` is the quickest way to start. In Apollo Server 5 it runs on Node's built-in HTTP server. For Express or other frameworks you use an integration package instead.

### 56: What is GraphQL Yoga?

GraphQL Yoga is a GraphQL server from The Guild. It is built on the Fetch API (`Request` and `Response`), so the same code runs on Node.js, Bun, Deno, Cloudflare Workers and serverless platforms. It supports subscriptions over Server-Sent Events out of the box and uses the Envelop plugin system.

```js
import { createServer } from "node:http";
import { createSchema, createYoga } from "graphql-yoga";

const yoga = createYoga({
  schema: createSchema({
    typeDefs: `type Query { hello: String! }`,
    resolvers: { Query: { hello: () => "Hello from Yoga" } },
  }),
});

createServer(yoga).listen(4000);
```

### 57: What is graphql-js?

graphql-js is the reference implementation of GraphQL in JavaScript, published as the `graphql` npm package. It has the parser, validator, executor, type system classes and utilities like `buildSchema` and `printSchema`. Most JavaScript servers and tools, including Apollo Server and Yoga, are built on top of it. Version 16 is still very common, and version 17 was released in 2026.

### 58: What is Apollo Client?

Apollo Client is a GraphQL client for JavaScript, mostly used with React. It sends queries, keeps results in a normalized cache, and gives you hooks like `useQuery` and `useMutation`. The current major version is Apollo Client 4, where the React hooks are imported from `@apollo/client/react`.

### 59: What other GraphQL clients are there?

- **Relay**: Meta's client for React, strict about fragments and built around a compiler.
- **urql**: a smaller, flexible client with a simple document cache by default and an optional normalized cache (Graphcache).
- **graphql-request**: a tiny client that just sends requests, often used with TanStack Query.
- Plain `fetch` works too, since a GraphQL request is just an HTTP request.

### 60: What is the context object?

The context is an object created once per request and passed to every resolver as the third argument. It's where you put things that all resolvers need: the current user, database clients, DataLoader instances, request headers or a logger.

```js
await startStandaloneServer(server, {
  context: async ({ req }) => ({
    user: await getUserFromToken(req.headers.authorization),
    db,
  }),
});
```

### 61: What is the `parent` argument in a resolver?

It's the value returned by the resolver of the parent field. For a root field like `Query.user`, it's the root value, which is usually `undefined`. For `User.posts`, it's the user object returned by `Query.user`, so you can use `parent.id` to load that user's posts.

```js
const resolvers = {
  Query: { user: (_, { id }, { db }) => db.users.findById(id) },
  User: { posts: (user, _, { db }) => db.posts.findByAuthor(user.id) },
};
```

### 62: What is the `info` argument used for?

`info` has details about the current field and the whole operation: `fieldName`, `returnType`, `parentType`, `path`, `schema`, `fragments`, `operation` and `variableValues`. Most resolvers never use it. It's useful for advanced things like looking ahead at which subfields were requested, so you can select only those columns from the database.

### 63: What is a default resolver?

If you don't write a resolver for a field, graphql-js uses a default one. It looks for a property with the same name on the parent object and returns it. If that property is a function, it calls it. That's why a `User` type with `id` and `name` usually needs no resolvers when the database row already has those properties.

### 64: Can resolvers be async?

Yes. A resolver can return a plain value or a promise. The server waits for the promise before it resolves the child fields. Resolvers for sibling fields can run at the same time, which is why GraphQL works well with async data sources.

```js
const resolvers = {
  Query: {
    weather: async (_, { city }) => {
      const res = await fetch(`https://api.example.com/weather?city=${city}`);
      return res.json();
    },
  },
};
```

### 65: What is a resolver map?

A resolver map is a plain object where the keys are type names and the values are objects of field resolvers. Apollo Server, Yoga and graphql-tools all use this format.

```js
const resolvers = {
  Query: {
    books: (_, __, { db }) => db.books.findAll(),
  },
  Mutation: {
    addBook: (_, { input }, { db }) => db.books.create(input),
  },
  Book: {
    author: (book, _, { db }) => db.authors.findById(book.authorId),
  },
};
```

### 66: What is the difference between schema-first and code-first?

In schema-first, you write the schema in SDL and then write resolvers that match it. The schema is easy to read and review, but you have to keep the SDL and resolvers in sync, usually with code generation. In code-first, you build the schema in your programming language with classes or builder functions, and the SDL is generated from the code. Types and resolvers live in one place, which works well with TypeScript.

### 67: Which libraries are used for code-first schemas?

In TypeScript, the common ones are Pothos, TypeGraphQL, Nexus (less active now) and the code-first mode of NestJS GraphQL. In other languages there are Strawberry for Python, gqlgen for Go (schema-first with code generation), Hot Chocolate for .NET and DGS or Spring for GraphQL in Java.

### 68: How are nested fields resolved?

Execution goes from top to bottom. The server first resolves the root fields, then for each result it resolves the selected child fields, passing the parent's result into each child resolver. This continues until it reaches scalar or enum fields. The result is built in the same shape as the query.

### 69: Are fields executed in parallel or one after another?

For queries, the top-level fields and sibling fields at any level can run at the same time. For mutations, the top-level fields run one after another in the order they appear in the document, so the second mutation sees the effect of the first. Fields below the top level of a mutation run like normal query fields.

### 70: Should a mutation take many arguments or a single input object?

Most teams use a single input object, like `createUser(input: CreateUserInput!)`. It's easier to add new optional fields later, the client sends one variable, and the input type can be reused. For very simple mutations, like `deleteTodo(id: ID!)`, a plain argument is fine.

### 71: What should a mutation return?

It should return the data that changed, so the client can update its cache without another request. A common pattern is a payload type with the changed object and maybe a list of user-facing errors.

```graphql
type UpdateProfilePayload {
  user: User
  errors: [UserError!]!
}

type Mutation {
  updateProfile(input: UpdateProfileInput!): UpdateProfilePayload!
}
```

### 72: Can you put several operations in one document?

Yes, but then you must send `operationName` to say which one to run, otherwise the server returns an error. Only one operation is executed per request. Fragments defined in the document can be shared by all the operations in it.

### 73: Can one query ask for several root fields?

Yes, and that's one of the main reasons to use GraphQL. One query can load unrelated data for a whole page.

```graphql
query HomePage {
  me {
    name
  }
  featuredProducts(first: 4) {
    id
    title
  }
  notifications(unreadOnly: true) {
    id
    text
  }
}
```

### 74: What is a selection set?

A selection set is the list of fields inside curly braces. Every field that returns an object, interface or union needs its own selection set, so the query always says exactly which fields come back.

```graphql
{
  user(id: "1") {
    # selection set of Query
    name # selection set of User
    address {
      city
    }
  }
}
```

### 75: What is a leaf field?

A leaf field returns a scalar or an enum, so it has no subfields. A query must end in leaf fields on every branch. If you ask for an object field without a selection set, like `{ user(id: "1") }`, validation fails because the server doesn't know which fields to return.

### 76: How do you write comments in GraphQL?

Use `#`. Everything after it on the same line is ignored by the parser.

```graphql
query GetUser {
  # only load what the header needs
  me {
    name
  }
}
```

### 77: What are descriptions in a schema?

Descriptions are strings placed before a type, field, argument or enum value. Unlike comments, they are part of the schema and show up in introspection, so tools like GraphiQL display them as documentation.

```graphql
"""
A registered user of the app.
"""
type User {
  "The display name, not unique."
  name: String!
}
```

### 78: Are commas required in GraphQL?

No. Commas are treated like whitespace, so you can use them or leave them out. Most people use them between arguments on one line and leave them out between fields on separate lines.

### 79: What is a GraphQL document?

A document is the full text sent to the server. It can contain one or more operations (queries, mutations, subscriptions) and fragment definitions. A schema file written in SDL is also a document, but with type system definitions instead of operations.

### 80: What is the query shorthand?

If a document has only one query, with no name and no variables, you can drop the `query` keyword.

```graphql
{
  me {
    name
  }
}
```

It's fine for quick tests, but in real code you should name your operations.

### 81: What naming conventions are common in GraphQL schemas?

Types, interfaces, unions, enums and input types use PascalCase (`OrderItem`). Fields and arguments use camelCase (`createdAt`). Enum values use SCREAMING_SNAKE_CASE (`IN_PROGRESS`). Input types often end with `Input` and mutation results with `Payload`. None of this is required by the spec, but almost every public API follows it.

### 82: Do the root types have to be named `Query`, `Mutation` and `Subscription`?

No. Those are the default names, but you can pick others with a `schema` definition. It's rare in practice.

```graphql
schema {
  query: RootQuery
  mutation: RootMutation
}
```

### 83: What is a custom scalar?

A custom scalar is a scalar type you define yourself, like `DateTime` or `Email`. In SDL it's one line, and on the server you write code that says how to send it to clients and how to read it from input.

```graphql
scalar DateTime

type Event {
  startsAt: DateTime!
}
```

### 84: Which custom scalars are commonly used?

`DateTime`, `Date`, `JSON`, `URL`, `Email`, `UUID`, `BigInt` and `Decimal` are the most common. The `graphql-scalars` package from The Guild has ready implementations of many of them, so you don't need to write your own.

### 85: How does GraphQL handle dates?

There's no built-in date type. Most APIs add a custom `DateTime` scalar and send dates as ISO 8601 strings, like `"2026-10-23T14:30:00Z"`. Some APIs use a plain `String` or a Unix timestamp as an `Int` or `Float`, but a custom scalar is clearer and can validate the format.

### 86: Why are fields nullable by default?

Because things fail. If a field is nullable and its resolver throws, the server can return `null` for that one field and still send the rest of the data. If every field were non-null, one failing field could wipe out a big part of the response. Making nullable the default makes partial results possible.

### 87: What happens when a non-null field resolves to `null`?

The server adds an error, and because the field can't be `null`, the `null` moves up to the nearest nullable parent field. If all parents are non-null up to the root, the whole `data` becomes `null`. That's why you should only mark fields as non-null when you are sure they can always be returned.

### 88: What steps does a server go through to answer a request?

1. **Parse**: turn the query text into an AST. Syntax errors stop here.
2. **Validate**: check the AST against the schema, for example that fields exist and variable types match.
3. **Execute**: call resolvers, starting at the root type, and build the result.

The parse and validate results can be cached for the same query text, so repeated queries only pay for execution.

### 89: What is an AST in GraphQL?

AST stands for Abstract Syntax Tree. It's an object tree that represents the query, with nodes for operations, fields, arguments, fragments and so on. graphql-js creates it with `parse()`. Tools work on the AST instead of the raw text, for example to validate a query, add `__typename` or count its depth.

```js
import { parse } from "graphql";

const ast = parse("{ me { name } }");
console.log(ast.definitions[0].kind); // "OperationDefinition"
```

### 90: What is the `gql` tag?

`gql` is a template literal tag that parses a GraphQL string into an AST (a `DocumentNode`). Apollo Client and graphql-tag export it. It also tells editor plugins and code generators that the string contains GraphQL.

```js
import { gql } from "@apollo/client";

const GET_USER = gql`
  query GetUser($id: ID!) {
    user(id: $id) {
      name
    }
  }
`;
```

### 91: Why would you keep queries in `.graphql` files?

Separate files get syntax highlighting, validation and autocomplete from editor plugins, and code generators can read them easily. Some teams import them with a bundler loader or let GraphQL Code Generator turn them into typed documents. Others prefer queries inside components with `gql` or `graphql()` so the data needs sit next to the UI.

### 92: How is pagination done in GraphQL?

The spec doesn't define pagination, so it's up to the schema. The two common styles are offset pagination with `limit` and `offset` arguments, and cursor pagination with `first`, `after`, `last` and `before`. Many APIs follow the Relay connection pattern for cursor pagination.

### 93: How does offset pagination work?

The client sends how many items it wants and how many to skip.

```graphql
type Query {
  products(limit: Int = 20, offset: Int = 0): [Product!]!
}
```

It's simple and lets you jump to page 7 directly. The downside is that if items are added or deleted while the user pages, items can be skipped or shown twice, and large offsets are slow in most databases.

### 94: How does cursor pagination work?

Each item has a cursor, an opaque string that marks its position. The client asks for `first: 20` items `after` a cursor, and the server returns items after that point. It stays correct when items are added or removed, and the database can use an index instead of skipping rows. You can't jump to a random page, though.

### 95: What is the Relay connection specification?

It's a convention for cursor pagination. A list field returns a `Connection` type with `edges` and `pageInfo`. Each edge has a `node` (the item) and a `cursor`.

```graphql
type ProductConnection {
  edges: [ProductEdge!]!
  pageInfo: PageInfo!
}

type ProductEdge {
  cursor: String!
  node: Product!
}

type PageInfo {
  hasNextPage: Boolean!
  hasPreviousPage: Boolean!
  startCursor: String
  endCursor: String
}

type Query {
  products(
    first: Int
    after: String
    last: Int
    before: String
  ): ProductConnection!
}
```

It's used by GitHub, Shopify and many others, and clients like Relay and Apollo Client have helpers for it.

### 96: How do you add filtering and sorting to a list field?

Use arguments, usually with input types and enums.

```graphql
input ProductFilter {
  category: String
  minPrice: Float
  inStock: Boolean
}

enum ProductSort {
  PRICE_ASC
  PRICE_DESC
  NEWEST
}

type Query {
  products(
    filter: ProductFilter
    sort: ProductSort = NEWEST
    first: Int = 20
  ): [Product!]!
}
```

### 97: How are subscriptions sent over the network?

The spec doesn't say. The two common transports are WebSockets, using the `graphql-transport-ws` protocol from the `graphql-ws` library, and Server-Sent Events, using the `graphql-sse` protocol or a server's own SSE support. Some setups also use multipart HTTP responses.

### 98: What is the `graphql-ws` library?

`graphql-ws` is the standard library for GraphQL over WebSockets in JavaScript. It has a client and a server and uses the `graphql-transport-ws` subprotocol. Apollo Client, urql and most servers support it.

### 99: What is `subscriptions-transport-ws`?

It's the old WebSocket library for GraphQL subscriptions, using the `graphql-ws` subprotocol (confusingly the same name as the new library). It's no longer maintained, and new projects should use `graphql-ws` instead. You'll still see it in older Apollo projects.

### 100: What is schema stitching?

Schema stitching combines several GraphQL schemas into one gateway schema, so clients can query them as one API. The gateway forwards each part of a query to the right service. `@graphql-tools/stitch` is the main library for it. It's an alternative to Apollo Federation.

### 101: What is Apollo Federation?

Apollo Federation is a way to build one GraphQL API out of several smaller GraphQL services called subgraphs. Each team owns a subgraph, and a router combines them into a supergraph that clients query as one schema. Types can be shared across subgraphs, so the Users service can define `User` and the Orders service can add an `orders` field to it.

### 102: What is a GraphQL gateway or router?

It's a server that sits in front of several GraphQL services. It receives the client's query, splits it into smaller queries for each service, sends them, and merges the results into one response. Examples are Apollo Router (written in Rust), Hive Gateway, WunderGraph Cosmo Router and a schema stitching gateway built with graphql-tools.

### 103: What is GraphQL Code Generator?

GraphQL Code Generator (graphql-codegen) is a CLI from The Guild that reads your schema and operations and generates code from them. The most common use is generating TypeScript types for query results, variables and resolvers, but it has plugins for many other languages and libraries.

### 104: Why generate TypeScript types from a schema?

Writing the types by hand is slow and they get out of sync with the schema. Generated types match the schema exactly, so if someone removes a field, the TypeScript build fails in every place that used it. You also get autocomplete for query results and resolver arguments.

### 105: What is the N+1 problem?

It happens when you load a list of N items with one query and then run one more query for each item to load a related field. For example, loading 50 posts and then calling the database 50 times to get each post's author. In GraphQL it's easy to hit because each field resolver runs separately for each object.

```js
// runs once per post, so 1 + N queries
const resolvers = {
  Post: {
    author: (post, _, { db }) => db.users.findById(post.authorId),
  },
};
```

### 106: What is DataLoader?

DataLoader is a small library that fixes the N+1 problem. It collects all the `load(id)` calls made in the same tick of the event loop and calls your batch function once with all the IDs. It also caches results for the lifetime of the loader, so the same ID isn't loaded twice in one request.

```js
import DataLoader from "dataloader";

const userLoader = new DataLoader(async (ids) => {
  const users = await db.users.findByIds(ids);
  return ids.map((id) => users.find((u) => u.id === id) ?? null);
});

const resolvers = {
  Post: {
    author: (post, _, { loaders }) => loaders.user.load(post.authorId),
  },
};
```

### 107: What is `InMemoryCache` in Apollo Client?

`InMemoryCache` is Apollo Client's default cache. It stores query results in a normalized form, so each object is stored once by its ID. When a query or mutation returns an object that's already in the cache, Apollo updates it, and every component showing that object re-renders with the new data.

### 108: What is a normalized cache?

A normalized cache splits responses into separate objects and stores each one under a unique key, usually `__typename` plus `id`, like `User:1`. Other objects point to it by reference instead of holding a copy. If two queries return the same user, they share one cache entry, so updating it in one place updates it everywhere.

### 109: How do you use `useQuery` in Apollo Client?

```jsx
import { gql } from "@apollo/client";
import { useQuery } from "@apollo/client/react";

const GET_DOGS = gql`
  query GetDogs {
    dogs {
      id
      breed
    }
  }
`;

function Dogs() {
  const { data, loading, error } = useQuery(GET_DOGS);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error.message}</p>;

  return (
    <ul>
      {data.dogs.map((dog) => (
        <li key={dog.id}>{dog.breed}</li>
      ))}
    </ul>
  );
}
```

The query runs when the component mounts, and the result is saved in the cache.

### 110: How do you use `useMutation` in Apollo Client?

`useMutation` returns a function to run the mutation and an object with its state. The mutation doesn't run until you call the function.

```jsx
import { gql } from "@apollo/client";
import { useMutation } from "@apollo/client/react";

const ADD_TODO = gql`
  mutation AddTodo($text: String!) {
    addTodo(text: $text) {
      id
      text
      done
    }
  }
`;

function AddTodo() {
  const [addTodo, { loading, error }] = useMutation(ADD_TODO);

  return (
    <button
      disabled={loading}
      onClick={() => addTodo({ variables: { text: "Buy milk" } })}
    >
      Add
    </button>
  );
}
```

### 111: How do you pass variables to `useQuery`?

Use the `variables` option. When a variable changes, Apollo runs the query again with the new value (or reads it from the cache if it's already there).

```jsx
function DogPhoto({ breed }) {
  const { data, loading } = useQuery(GET_DOG_PHOTO, {
    variables: { breed },
  });

  if (loading) return null;
  return <img src={data.dog.displayImage} alt={breed} />;
}
```

### 112: How do you refetch a query in Apollo Client?

`useQuery` returns a `refetch` function. You can call it with no arguments to use the same variables, or pass new variables.

```jsx
const { data, refetch } = useQuery(GET_DOGS)

<button onClick={() => refetch()}>Refresh</button>
```

After a mutation you can also use the `refetchQueries` option to refetch specific queries.

### 113: What is a fetch policy?

A fetch policy tells Apollo Client whether to use the cache, the network or both. The default for `useQuery` is `cache-first`: return cached data if all the fields are there, otherwise go to the network. Other options are `cache-and-network`, `network-only`, `no-cache`, `cache-only` and `standby`.

### 114: How do you return an error from a resolver?

Throw an error. The server catches it, sets the field to `null` and adds an entry to the `errors` array. Throwing a `GraphQLError` lets you add an error code and other details.

```js
import { GraphQLError } from "graphql";

const resolvers = {
  Query: {
    user: async (_, { id }, { db }) => {
      const user = await db.users.findById(id);
      if (!user) {
        throw new GraphQLError("User not found", {
          extensions: { code: "NOT_FOUND" },
        });
      }
      return user;
    },
  },
};
```

### 115: What is `GraphQLError`?

`GraphQLError` is the error class from graphql-js. It holds the message plus `locations`, `path` and `extensions`, which are the fields that end up in the response. When a resolver throws a normal `Error`, the executor wraps it in a `GraphQLError` and keeps the original in `originalError`.

### 116: What is the `extensions` field in an error used for?

The spec reserves `extensions` for any extra information a server wants to add. The most common use is a machine-readable `code`, like `UNAUTHENTICATED` or `BAD_USER_INPUT`, so clients can react to the error without parsing the message. Servers also put things like validation details or a request ID there.

### 117: Which error codes does Apollo Server use?

Apollo Server adds a `code` in `extensions` for errors it creates. The built-in codes include `GRAPHQL_PARSE_FAILED`, `GRAPHQL_VALIDATION_FAILED`, `BAD_USER_INPUT`, `BAD_REQUEST`, `PERSISTED_QUERY_NOT_FOUND`, `PERSISTED_QUERY_NOT_SUPPORTED`, `OPERATION_RESOLUTION_FAILURE` and `INTERNAL_SERVER_ERROR`. They are available in the `ApolloServerErrorCode` enum from `@apollo/server/errors`. Codes like `UNAUTHENTICATED` and `FORBIDDEN` are not built in anymore, so you throw a `GraphQLError` with your own code.

### 118: How do you authenticate requests to a GraphQL API?

The usual way is the same as for REST: the client sends a token in the `Authorization` header or a session cookie. The server reads it when it builds the context, finds the user and puts it in the context. Resolvers then check `context.user`.

```js
await startStandaloneServer(server, {
  context: async ({ req }) => {
    const token = req.headers.authorization?.replace("Bearer ", "");
    const user = token ? await verifyToken(token) : null;
    return { user };
  },
});
```

### 119: Where should authorization checks go?

The GraphQL docs recommend putting them in your business logic layer, not spread across resolvers. That way the same rule applies whether the data is loaded through GraphQL, a REST endpoint or a background job. Resolvers stay thin and call services that check permissions. Some teams also use schema directives or middleware for simple checks like "must be logged in".

### 120: Why don't GraphQL APIs usually have versions like `/v1` and `/v2`?

Because clients only get the fields they ask for, you can add new fields and types without affecting anyone. When something needs to change, you add the new field, mark the old one with `@deprecated`, and remove it once no clients use it. This is called schema evolution. Versioning is still possible, but most GraphQL APIs avoid it.

### 121: How do you deprecate a field?

Add the `@deprecated` directive with a reason that says what to use instead.

```graphql
type Product {
  price: Money!
  priceInCents: Int
    @deprecated(
      reason: "Use `price` instead. Will be removed after 2027-01-01."
    )
}
```

The field keeps working, but tools warn about it. Track whether clients still use it before you remove it.

### 122: Can you deprecate arguments and input fields?

Yes. Since the October 2021 spec, `@deprecated` also works on arguments and input fields, not only on fields and enum values. A required (non-null without a default) argument or input field can't be deprecated, because clients have no way to stop sending it.

```graphql
type Query {
  products(
    sortBy: String @deprecated(reason: "Use `sort`.")
    sort: ProductSort
  ): [Product!]!
}
```

### 123: What is a breaking change in a GraphQL schema?

A change that can make existing queries fail or return something clients don't expect. Examples:

- Removing or renaming a field, type or enum value.
- Changing a field's type, like `String` to `Int`.
- Making an output field nullable when it was non-null.
- Adding a required argument or required input field.
- Making an argument or input field required when it was optional.

### 124: Which schema changes are safe?

- Adding a new type, field, or query.
- Adding an optional argument or optional input field.
- Making a nullable output field non-null.
- Making a required argument optional.
- Deprecating something.

Adding a new enum value or a new union member is safe for the server, but it can break clients that don't handle unknown values, so treat those with care.

### 125: What is a persisted query?

A persisted query is a query saved on the server ahead of time with an ID, usually a hash of its text. The client sends only the ID instead of the full query text. This makes requests smaller and lets you send them with `GET` so CDNs can cache them. If the server only accepts known IDs, it also blocks any query you didn't approve.

### 126: Is GraphQL a database or a query language for databases?

No. GraphQL is a query language for APIs, not for databases. It doesn't store data and doesn't know where data comes from. Resolvers can read from SQL, MongoDB, other APIs, files or memory. Some tools, like Hasura or PostGraphile, generate a GraphQL API from a database, but that's a tool feature, not part of GraphQL.

### 127: Which programming languages can you use GraphQL with?

Almost any. There are servers and clients for JavaScript and TypeScript, Python (Strawberry, Graphene, Ariadne), Java and Kotlin (Spring for GraphQL, DGS, graphql-java), Go (gqlgen), Ruby (graphql-ruby), PHP (webonyx/graphql-php, Lighthouse), .NET (Hot Chocolate), Rust (async-graphql, Juniper) and more. The client and server don't need to use the same language.

### 128: Can GraphQL sit in front of existing REST APIs?

Yes, this is very common. The resolvers just call the REST endpoints and return the data. It lets front-end teams use GraphQL without rewriting the back end. Apollo has `RESTDataSource` for this, and GraphQL Mesh can generate a GraphQL schema from OpenAPI specs.

```js
const resolvers = {
  Query: {
    user: async (_, { id }) => {
      const res = await fetch(`https://api.example.com/users/${id}`);
      if (!res.ok) throw new Error("Failed to load user");
      return res.json();
    },
  },
};
```

### 129: When is REST a better choice than GraphQL?

- Simple CRUD APIs with one or two clients, where the extra setup doesn't pay off.
- Public APIs where HTTP caching by URL matters a lot.
- File downloads and uploads, streaming and other binary data.
- Teams with no GraphQL experience and a tight deadline.
- Webhooks and server-to-server APIs where the response shape is fixed anyway.

### 130: How does GraphQL compare to gRPC?

gRPC uses Protocol Buffers over HTTP/2, has fixed request and response messages, and is fast and compact. It's mostly used for communication between back-end services. GraphQL uses JSON (usually), lets the client choose fields and is mostly used between front ends and back ends. Many systems use both: gRPC between services and GraphQL at the edge for clients.

### 131: What does `buildSchema` do in graphql-js?

It turns an SDL string into a `GraphQLSchema` object. It doesn't take resolvers, so it's mostly used for tests, tools or very simple servers with a root value.

```js
import { buildSchema, graphql } from "graphql";

const schema = buildSchema(`type Query { hello: String }`);
const result = await graphql({
  schema,
  source: "{ hello }",
  rootValue: { hello: () => "world" },
});
console.log(result); // { data: { hello: 'world' } }
```

### 132: What does `printSchema` do?

`printSchema` takes a `GraphQLSchema` object and returns it as SDL text. It's useful with code-first libraries when you want to save the schema to a file, review changes in pull requests or give it to code generators.

```js
import { printSchema } from "graphql";
import { writeFileSync } from "node:fs";

writeFileSync("schema.graphql", printSchema(schema));
```

### 133: What is `makeExecutableSchema`?

It's a function from `@graphql-tools/schema` that takes SDL type definitions and a resolver map and returns an executable `GraphQLSchema`. Apollo Server does this for you when you pass `typeDefs` and `resolvers`, but you need it when you want to work with the schema directly, for example to apply schema directives or use it with another server.

```js
import { makeExecutableSchema } from "@graphql-tools/schema";

const schema = makeExecutableSchema({ typeDefs, resolvers });
```

### 134: How do you mock a GraphQL schema?

`@graphql-tools/mock` can add fake resolvers to a schema, returning random or custom values for every type. Front-end developers can then work against the schema before the real resolvers exist.

```js
import { makeExecutableSchema } from "@graphql-tools/schema";
import { addMocksToSchema } from "@graphql-tools/mock";

const schema = addMocksToSchema({
  schema: makeExecutableSchema({ typeDefs }),
  mocks: { String: () => "Hello", Int: () => 42 },
});
```

### 135: How do you test a simple resolver?

A resolver is just a function, so you can call it directly with fake arguments.

```js
import { test, expect } from "vitest";
import { resolvers } from "./resolvers";

test("Query.user returns the user", async () => {
  const db = { users: { findById: async (id) => ({ id, name: "Ana" }) } };
  const user = await resolvers.Query.user({}, { id: "1" }, { db });
  expect(user.name).toBe("Ana");
});
```

### 136: What is `executeOperation` in Apollo Server?

It runs an operation against the server without starting an HTTP server. It goes through parsing, validation, plugins and execution, so it's good for integration tests.

```js
const response = await server.executeOperation(
  {
    query: "query GetUser($id: ID!) { user(id: $id) { name } }",
    variables: { id: "1" },
  },
  { contextValue: { user: testUser, db } },
);

expect(response.body.kind).toBe("single");
expect(response.body.singleResult.data?.user.name).toBe("Ana");
```

### 137: Can a field return a list of union or interface types?

Yes. A field can return `[SearchResult!]!` where `SearchResult` is a union, or `[Node!]!` where `Node` is an interface. Each item in the list can be a different type, and the client uses fragments and `__typename` to handle each one.

### 138: Can input types contain other input types?

Yes. Input types can have fields that are other input types or lists of them. They can even refer to themselves, as long as the cycle goes through a nullable field or a list, so a valid finite value is still possible.

```graphql
input AddressInput {
  street: String!
  city: String!
}

input CreateOrderInput {
  items: [OrderItemInput!]!
  shippingAddress: AddressInput!
}
```

### 139: What does `extend type` do?

It adds fields to a type that was defined somewhere else. It's handy for splitting a schema into files by feature, where each file adds its own fields to `Query` or `Mutation`.

```graphql
# users.graphql
type Query {
  me: User
}

# products.graphql
extend type Query {
  products: [Product!]!
}
```

### 140: What is a OneOf input object?

A OneOf input object is an input type marked with `@oneOf`, where the client must provide exactly one field and it can't be `null`. It was added in the September 2025 edition of the spec. It's useful when there are several ways to find something.

```graphql
input UserBy @oneOf {
  id: ID
  email: String
  username: String
}

type Query {
  user(by: UserBy!): User
}
```

`user(by: { email: "ana@example.com" })` is valid. Sending two fields, or none, is a validation error.

### 141: Why use a GraphQL client library instead of plain `fetch`?

A plain `fetch` works for one-off requests. A client library adds a cache, so data isn't loaded twice and different components stay in sync. It also handles loading and error states, refetching, pagination, optimistic updates, subscriptions and deduplication of identical requests. For a small app with a few queries, `fetch` or graphql-request may be enough.

### 142: What is the `extensions` key in a request?

It's an optional object in the request body for anything outside the normal query, variables and operation name. The best-known use is Automatic Persisted Queries, where the client sends the query hash in `extensions.persistedQuery`. Servers ignore extensions they don't understand.

```json
{
  "variables": { "id": "1" },
  "extensions": {
    "persistedQuery": {
      "version": 1,
      "sha256Hash": "ecf4edb46db40b5132295c0291d62fb65d6759a9eedfa4d5d612dd5ec54a6b38"
    }
  }
}
```

### 143: What is the GraphQL specification?

It's the document that defines the GraphQL language, type system, validation rules and how execution works. It's published in editions. The October 2021 edition was the standard for years, and the September 2025 edition is the latest, adding things like OneOf input objects. Implementations in each language follow the spec, which is why a client in one language can talk to a server in another.

### 144: What is `graphql-config`?

It's a shared configuration format for GraphQL tools, usually a `graphql.config.ts`, `.graphqlrc.yml` or similar file. You set the schema location and where your documents live, and tools like the VS Code GraphQL extension, graphql-eslint and GraphQL Code Generator can read it.

```yaml
schema: ./schema.graphql
documents: ./src/**/*.{ts,tsx}
```

### 145: Can variables have default values in an operation?

Yes. You set the default after the type in the variable declaration. If the client doesn't send the variable, the default is used.

```graphql
query GetProducts($first: Int = 10, $sort: ProductSort = NEWEST) {
  products(first: $first, sort: $sort) {
    id
    title
  }
}
```

### 146: How do you pass a list as an argument?

Declare the argument as a list type, and send a JSON array as the variable value.

```graphql
query GetUsers($ids: [ID!]!) {
  users(ids: $ids) {
    id
    name
  }
}
```

```json
{ "ids": ["1", "2", "3"] }
```

If the argument is a list and you pass a single value, GraphQL coerces it into a list with one item.

### 147: Can you use fragments in mutations and subscriptions?

Yes. Fragments work in any operation. It's common to use the same fragment in a query and in the mutation that changes that data, so the mutation returns everything the cache needs to update the UI.

```graphql
mutation UpdateUser($input: UpdateUserInput!) {
  updateUser(input: $input) {
    ...UserCard
  }
}
```

### 148: What are meta fields?

Meta fields start with two underscores and are added by GraphQL itself. `__typename` works on any object type. `__schema` and `__type(name:)` are available on the query root type and are used for introspection. You can't define your own fields or types that start with `__`, because that prefix is reserved.

### 149: What does it mean that GraphQL is strongly typed?

Every field, argument and variable has a declared type, and the server checks queries against those types before running them. If you pass a string where an `Int` is expected, or ask for a field that doesn't exist, you get an error before any resolver runs. Clients can also use the types to generate code and check queries at build time.

### 150: How would you explain how a GraphQL request works in a few sentences?

The client sends a query that lists the fields it wants, usually as a `POST` to one endpoint. The server parses the query, checks it against the schema, then calls a resolver for each field, starting from the root and going down into nested fields. Each resolver gets its data from wherever it lives, and the server puts the results together into a JSON response with the same shape as the query.

## Moderate Questions (151-300)

### 151: Why should DataLoader instances be created per request?

DataLoader caches every key it loads. If you share one loader across all requests, user A's data can be served to user B, permission checks can be skipped because the cached value comes back without going through them, and the cache grows forever and serves stale data. Create new loaders in the context function so each request starts with an empty cache.

```js
await startStandaloneServer(server, {
  context: async ({ req }) => {
    const user = await getUser(req);
    return {
      user,
      loaders: {
        user: new DataLoader((ids) => batchUsers(ids)),
        postsByAuthor: new DataLoader((ids) => batchPostsByAuthor(ids)),
      },
    };
  },
});
```

### 152: What rules must a DataLoader batch function follow?

It gets an array of keys and must return a promise of an array with the same length, in the same order as the keys. If a key has no result, put `null` (or an `Error`) in its place. Databases don't return rows in the order you asked for, so you almost always have to reorder the results before returning them.

### 153: How do you write a DataLoader batch function for a SQL database?

Load all the rows with one `IN` (or `ANY`) query, put them in a map by ID, then map the keys back to rows in order.

```js
import DataLoader from "dataloader";

export function createUserLoader(sql) {
  return new DataLoader(async (ids) => {
    const rows = await sql`SELECT * FROM users WHERE id = ANY(${ids})`;
    const byId = new Map(rows.map((row) => [String(row.id), row]));
    return ids.map((id) => byId.get(String(id)) ?? null);
  });
}
```

For one-to-many relations, like posts by author, group the rows into arrays and return an empty array for keys with no rows.

### 154: When should you clear or prime the DataLoader cache?

Clear a key with `loader.clear(id)` after a mutation changes that object, so later fields in the same request don't read the old value. Prime the cache with `loader.prime(id, value)` when you already loaded an object some other way, like a list query, so a later `load(id)` doesn't hit the database again. Since loaders are per request, this only matters inside one request.

```js
const updated = await db.users.update(id, input);
loaders.user.clear(id).prime(id, updated);
```

### 155: How do you implement cursor pagination with a SQL database?

Sort by a unique, stable column (or a pair like `created_at, id`), and use the cursor to remember the last row the client saw. Ask for one extra row to know if there's a next page.

```js
async function productsConnection({ first = 20, after }, sql) {
  const afterId = after ? decodeCursor(after) : 0;
  const rows = await sql`
    SELECT * FROM products
    WHERE id > ${afterId}
    ORDER BY id
    LIMIT ${first + 1}
  `;
  const hasNextPage = rows.length > first;
  const nodes = rows.slice(0, first);

  return {
    edges: nodes.map((node) => ({ node, cursor: encodeCursor(node.id) })),
    pageInfo: {
      hasNextPage,
      hasPreviousPage: Boolean(after),
      startCursor: nodes.length ? encodeCursor(nodes[0].id) : null,
      endCursor: nodes.length ? encodeCursor(nodes.at(-1).id) : null,
    },
  };
}
```

Strictly, the Relay spec allows `hasPreviousPage` to be `false` when paging forward if checking it is expensive.

### 156: How should you encode cursors?

Cursors should be opaque to clients, so they don't build them by hand or depend on their format. A common approach is base64 of a small string or JSON, like `base64("product:42")` or `base64('{"createdAt":"...","id":42}')`. Base64 isn't security, so the server must still validate the decoded value. If the cursor contains anything sensitive, sign or encrypt it.

```js
const encodeCursor = (id) => Buffer.from(`cursor:${id}`).toString("base64url");
const decodeCursor = (cursor) =>
  Number(Buffer.from(cursor, "base64url").toString().split(":")[1]);
```

### 157: Should a connection include `totalCount`?

It's useful for showing "120 results" or page numbers, but a `COUNT(*)` on a big filtered table can cost more than the page itself. Put it on the connection as a separate field, so it's only computed when the client asks for it. For very large tables you can return an estimate or cap the count.

```graphql
type ProductConnection {
  edges: [ProductEdge!]!
  pageInfo: PageInfo!
  totalCount: Int!
}
```

### 158: What is the Node interface and global object identification?

It's a Relay convention. Every type that can be fetched by ID implements `Node`, and the ID is globally unique across all types. A root `node(id:)` field can then load any object.

```graphql
interface Node {
  id: ID!
}

type Query {
  node(id: ID!): Node
  nodes(ids: [ID!]!): [Node]!
}
```

The ID usually encodes the type and the database ID, like `base64("User:42")`, so the server knows which table to look in. Clients use it to refetch any object without knowing which root field loads it.

### 159: How do you design mutation input and payload types?

Give each mutation its own input type and its own payload type, even if they look small at first. That way you can add fields later without breaking anything.

```graphql
input CreatePostInput {
  title: String!
  body: String!
  tags: [String!]
}

type CreatePostPayload {
  post: Post
  errors: [UserError!]!
}

type Mutation {
  createPost(input: CreatePostInput!): CreatePostPayload!
}
```

Reusing one `PostInput` for create and update looks tidy, but the two usually need different required fields.

### 160: What is the user errors pattern in mutations?

Instead of throwing for validation problems, the mutation returns them as normal data in the payload. Each error has a message and the input field it relates to, so the form can show it next to the right input.

```graphql
type UserError {
  message: String!
  field: [String!]
  code: String
}
```

```js
const resolvers = {
  Mutation: {
    createPost: async (_, { input }, { services }) => {
      if (input.title.trim().length === 0) {
        return {
          post: null,
          errors: [{ message: "Title is required", field: ["title"] }],
        };
      }
      const post = await services.posts.create(input);
      return { post, errors: [] };
    },
  },
};
```

Shopify uses this pattern with a `userErrors` field on every mutation payload.

### 161: How do you model errors as data with unions?

Make the field return a union of the success type and the expected error types. The client is forced to handle each case, and the schema documents which errors can happen.

```graphql
type NotFoundError {
  message: String!
}

type PermissionError {
  message: String!
  requiredRole: Role!
}

union UserResult = User | NotFoundError | PermissionError

type Query {
  user(id: ID!): UserResult!
}
```

```graphql
query {
  user(id: "1") {
    ... on User {
      name
    }
    ... on NotFoundError {
      message
    }
    ... on PermissionError {
      message
      requiredRole
    }
  }
}
```

Many teams add an `Error` interface with a `message` field that all error types implement, so clients can handle unknown errors generically.

### 162: When should you throw an error and when should you return it as data?

Throw for unexpected problems the user can't fix: a database is down, a bug, a timeout, a missing login. These go into the `errors` array. Return errors as data for expected business outcomes the UI should handle: invalid input, out of stock, a username already taken. A simple rule: if a designer would draw a screen for it, it belongs in the schema.

### 163: How do you hide internal error details from clients in production?

Unexpected errors can leak database messages, file paths or stack traces. In Apollo Server, stack traces are only included when `NODE_ENV` isn't `production`, and you can use `formatError` to replace messages for errors you didn't create on purpose.

```js
import { unwrapResolverError } from "@apollo/server/errors";
import { GraphQLError } from "graphql";

const server = new ApolloServer({
  typeDefs,
  resolvers,
  formatError: (formattedError, error) => {
    const original = unwrapResolverError(error);
    if (original instanceof GraphQLError) return formattedError;
    logger.error(original);
    return {
      message: "Internal server error",
      extensions: { code: "INTERNAL_SERVER_ERROR" },
    };
  },
});
```

GraphQL Yoga does this by default with its `maskedErrors` option: any error that isn't a `GraphQLError` is shown as "Unexpected error."

### 164: How do you create your own error classes for a GraphQL server?

Extend `GraphQLError` and set a fixed code in `extensions`. Resolvers then throw meaningful errors, and clients get consistent codes.

```js
import { GraphQLError } from "graphql";

export class UnauthenticatedError extends GraphQLError {
  constructor(message = "You must be logged in") {
    super(message, {
      extensions: { code: "UNAUTHENTICATED", http: { status: 401 } },
    });
  }
}

export class ForbiddenError extends GraphQLError {
  constructor(message = "Not allowed") {
    super(message, { extensions: { code: "FORBIDDEN" } });
  }
}
```

In Apollo Server, `extensions.http.status` sets the HTTP status code, and the `http` key is removed from the response.

### 165: How does the error `path` help with partial data?

`path` lists the response keys and list indexes that lead to the field that failed, like `["user", "posts", 2, "author"]`. The client can match it to the `null` in `data` and show an error only for that part of the UI, while the rest of the page renders normally.

### 166: How do you use Apollo Server 5 with Express?

Install `@as-integrations/express5` (or `express4` for older apps) and mount `expressMiddleware`. You need to start the server first and add JSON body parsing.

```js
import express from "express";
import cors from "cors";
import http from "node:http";
import { ApolloServer } from "@apollo/server";
import { expressMiddleware } from "@as-integrations/express5";
import { ApolloServerPluginDrainHttpServer } from "@apollo/server/plugin/drainHttpServer";

const app = express();
const httpServer = http.createServer(app);

const server = new ApolloServer({
  typeDefs,
  resolvers,
  plugins: [ApolloServerPluginDrainHttpServer({ httpServer })],
});
await server.start();

app.use(
  "/graphql",
  cors({ origin: ["https://app.example.com"] }),
  express.json(),
  expressMiddleware(server, {
    context: async ({ req }) => ({
      user: await getUser(req.headers.authorization),
    }),
  }),
);

httpServer.listen(4000);
```

In Apollo Server 4 the Express integration lived inside `@apollo/server/express4`. In version 5 it's a separate package.

### 167: How do you authenticate WebSocket subscriptions?

Browsers can't set custom headers on a WebSocket, so the token is usually sent in the connection init message. With `graphql-ws`, the client passes `connectionParams`, and the server checks them in `onConnect` and builds the context from them.

```js
// client
import { createClient } from "graphql-ws";

const wsClient = createClient({
  url: "wss://api.example.com/graphql",
  connectionParams: () => ({ authorization: `Bearer ${getToken()}` }),
});
```

```js
// server
import { useServer } from "graphql-ws/use/ws";

useServer(
  {
    schema,
    onConnect: async (ctx) => {
      const user = await verifyToken(ctx.connectionParams?.authorization);
      if (!user) return false; // closes the connection
    },
    context: async (ctx) => ({
      user: await verifyToken(ctx.connectionParams?.authorization),
    }),
  },
  wsServer,
);
```

Cookies also work, since the browser sends them with the WebSocket handshake. In graphql-ws v5 the import path was `graphql-ws/lib/use/ws`.

### 168: How do you write an authorization directive?

Declare the directive in the schema, then use `mapSchema` from `@graphql-tools/utils` to wrap the resolver of every field that has it.

```graphql
directive @auth(requires: Role = USER) on FIELD_DEFINITION

enum Role {
  USER
  ADMIN
}

type Query {
  me: User @auth
  allUsers: [User!]! @auth(requires: ADMIN)
}
```

```js
import { mapSchema, getDirective, MapperKind } from "@graphql-tools/utils";
import { defaultFieldResolver, GraphQLError } from "graphql";

export function authDirective(schema) {
  return mapSchema(schema, {
    [MapperKind.OBJECT_FIELD]: (fieldConfig) => {
      const auth = getDirective(schema, fieldConfig, "auth")?.[0];
      if (!auth) return fieldConfig;

      const resolve = fieldConfig.resolve ?? defaultFieldResolver;
      fieldConfig.resolve = (source, args, context, info) => {
        if (!context.user) {
          throw new GraphQLError("Not authenticated", {
            extensions: { code: "UNAUTHENTICATED" },
          });
        }
        if (auth.requires === "ADMIN" && context.user.role !== "ADMIN") {
          throw new GraphQLError("Forbidden", {
            extensions: { code: "FORBIDDEN" },
          });
        }
        return resolve(source, args, context, info);
      };
      return fieldConfig;
    },
  });
}
```

### 169: How do you hide a single field from some users?

Check the permission in the field's resolver (or the service it calls) and either throw or return `null`. The field must be nullable if you return `null`.

```js
const resolvers = {
  User: {
    email: (user, _, { user: viewer }) => {
      if (!viewer) return null;
      if (viewer.id === user.id || viewer.role === "ADMIN") return user.email;
      return null;
    },
  },
};
```

Returning `null` quietly is friendlier for UIs. Throwing makes it clear that access was denied. Pick one approach and use it everywhere.

### 170: What are Apollo Server plugins?

Plugins are objects with hooks that run at points in the server and request lifecycle. Server hooks include `serverWillStart`. Request hooks are returned from `requestDidStart` and include `didResolveOperation`, `executionDidStart`, `didEncounterErrors` and `willSendResponse`. `executionDidStart` can return `willResolveField`, which runs for every field. Plugins are used for logging, metrics, tracing, caching and changing responses.

### 171: How do you write a simple logging plugin for Apollo Server?

```js
const loggingPlugin = {
  async requestDidStart({ request }) {
    const start = Date.now();
    return {
      async didEncounterErrors({ errors }) {
        for (const err of errors)
          logger.warn({ op: request.operationName, err: err.message });
      },
      async willSendResponse() {
        logger.info({ op: request.operationName, ms: Date.now() - start });
      },
    };
  },
};

const server = new ApolloServer({
  typeDefs,
  resolvers,
  plugins: [loggingPlugin],
});
```

### 172: How do you configure CORS for a GraphQL server?

It's the same as any HTTP server: allow your front-end origins and the headers you use. With `startStandaloneServer` in Apollo Server, CORS is open to all origins by default. With Express, use the `cors` middleware. If you use cookies, set `credentials: true` and a specific origin list, because `*` doesn't work with credentials.

```js
app.use(
  "/graphql",
  cors({ origin: ["https://app.example.com"], credentials: true }),
  express.json(),
  expressMiddleware(server),
);
```

GraphQL Yoga has a `cors` option in `createYoga`.

### 173: How do you set response headers or cookies from a resolver?

Put the response object, or a helper, into the context, and use it in the resolver. With the Express integration you can pass `res` in the context.

```js
expressMiddleware(server, {
  context: async ({ req, res }) => ({ req, res }),
});

const resolvers = {
  Mutation: {
    login: async (_, { email, password }, { res, services }) => {
      const session = await services.auth.login(email, password);
      res.cookie("sid", session.id, {
        httpOnly: true,
        secure: true,
        sameSite: "lax",
      });
      return session.user;
    },
  },
};
```

In Apollo Server plugins you can also set headers with `requestContext.response.http.headers.set(...)`.

### 174: How do you handle file uploads with GraphQL?

There are two common options. The first is the GraphQL multipart request spec, used by libraries like `graphql-upload` and supported by GraphQL Yoga, where files are sent as `multipart/form-data` next to the operation. The second, which Apollo recommends, is to keep files out of GraphQL: a mutation returns a signed upload URL (for example an S3 presigned URL), the client uploads directly to storage, and then calls another mutation with the file key. The second option is simpler to scale and avoids the CSRF risks of multipart requests.

### 175: What is CSRF prevention in Apollo Server?

Browsers can send some cross-site requests without a CORS preflight, like a `GET` or a `POST` with `text/plain` or `multipart/form-data`. An attacker's page could use that to run a mutation with the victim's cookies. Apollo Server's `csrfPrevention` option, on by default since v4, rejects requests that could be "simple" unless they have a `Content-Type` that triggers a preflight, like `application/json`, or a non-empty `x-apollo-operation-name` or `apollo-require-preflight` header. Normal JSON `POST` requests from Apollo Client pass without changes.

### 176: What should you put in the context, and what should you avoid?

Put per-request things there: the authenticated user, DataLoaders, a request ID, a logger with request info, and service objects or database clients. Avoid putting mutable shared state that changes between requests, heavy objects created for every request when they could be shared, or anything that does slow work for every request even if no resolver needs it. Keep the context typed, so resolvers know what's available.

### 177: How do you split a large schema into modules?

Organize by feature, not by kind. Each module has its own SDL and resolvers, and extends `Query` and `Mutation` with its fields.

```
src/
  modules/
    users/
      users.graphql
      users.resolvers.ts
    orders/
      orders.graphql
      orders.resolvers.ts
  schema.ts
```

Then merge all type definitions and resolvers into one schema. GraphQL Modules from The Guild and NestJS's module system are frameworks built around this idea.

### 178: How do you merge type definitions and resolvers from many files?

Use `@graphql-tools/load-files` to find the files and `@graphql-tools/merge` to combine them.

```js
import path from "node:path";
import { loadFilesSync } from "@graphql-tools/load-files";
import { mergeTypeDefs, mergeResolvers } from "@graphql-tools/merge";
import { makeExecutableSchema } from "@graphql-tools/schema";

const typeDefs = mergeTypeDefs(
  loadFilesSync(path.join(import.meta.dirname, "modules/**/*.graphql")),
);
const resolvers = mergeResolvers(
  loadFilesSync(path.join(import.meta.dirname, "modules/**/*.resolvers.*")),
);

export const schema = makeExecutableSchema({ typeDefs, resolvers });
```

`mergeTypeDefs` also merges repeated type definitions, so two files can both define `type Query`.

### 179: How do you build a schema code-first with Pothos?

```ts
import SchemaBuilder from "@pothos/core";

const builder = new SchemaBuilder<{ Context: { userId?: string } }>({});

const User = builder.objectRef<{ id: string; name: string }>("User");

User.implement({
  fields: (t) => ({
    id: t.exposeID("id"),
    name: t.exposeString("name"),
  }),
});

builder.queryType({
  fields: (t) => ({
    user: t.field({
      type: User,
      nullable: true,
      args: { id: t.arg.id({ required: true }) },
      resolve: (_, { id }) => findUser(String(id)),
    }),
  }),
});

export const schema = builder.toSchema();
```

Pothos infers TypeScript types from the definitions, so resolver arguments and return values are checked without code generation.

### 180: How do you build a GraphQL API with NestJS?

NestJS has the `@nestjs/graphql` package with Apollo or Mercurius drivers. In code-first mode, you write classes with decorators and Nest generates the schema.

```ts
import { Field, ID, ObjectType, Resolver, Query, Args } from "@nestjs/graphql";

@ObjectType()
export class Recipe {
  @Field(() => ID)
  id: string;

  @Field()
  title: string;
}

@Resolver(() => Recipe)
export class RecipesResolver {
  constructor(private readonly recipes: RecipesService) {}

  @Query(() => Recipe, { nullable: true })
  recipe(@Args("id") id: string) {
    return this.recipes.findById(id);
  }
}
```

Nest also supports schema-first mode, where you write SDL and it generates TypeScript types.

### 181: How do you set up GraphQL Code Generator for a front end?

The `client` preset is the recommended setup. It generates a typed `graphql()` function, so every document you write gets typed results and variables.

```ts
// codegen.ts
import type { CodegenConfig } from "@graphql-codegen/cli";

const config: CodegenConfig = {
  schema: "http://localhost:4000/graphql",
  documents: ["src/**/*.{ts,tsx}"],
  ignoreNoDocuments: true,
  generates: {
    "./src/gql/": { preset: "client" },
  },
};

export default config;
```

```tsx
import { graphql } from "./gql";
import { useQuery } from "@apollo/client/react";

const GetUser = graphql(`
  query GetUser($id: ID!) {
    user(id: $id) {
      id
      name
    }
  }
`);

const { data } = useQuery(GetUser, { variables: { id: "1" } }); // data is typed
```

Run `graphql-codegen --watch` during development so types update as you edit queries.

### 182: How do you get typed resolvers with GraphQL Code Generator?

Use the `typescript` and `typescript-resolvers` plugins, and set `mappers` so parent types match your database models instead of the GraphQL types.

```ts
const config: CodegenConfig = {
  schema: "src/**/*.graphql",
  generates: {
    "src/generated/resolvers-types.ts": {
      plugins: ["typescript", "typescript-resolvers"],
      config: {
        contextType: "../context#Context",
        mappers: { User: "../models#UserModel" },
      },
    },
  },
};
```

```ts
import type { Resolvers } from "./generated/resolvers-types";

export const resolvers: Resolvers = {
  User: {
    // parent is UserModel, return type must match [Post!]!
    posts: (user, _, { loaders }) => loaders.postsByAuthor.load(user.id),
  },
};
```

The Guild's newer Server Preset (`@eddeee888/gcg-typescript-resolver-files`) generates resolver files and types per module for bigger projects.

### 183: What is fragment colocation?

Each component declares a fragment with the fields it needs, right next to the component code. The parent query spreads the child fragments. When a component needs a new field, you change only that component's fragment, and you can't forget to update a query somewhere else.

```tsx
export const UserAvatarFragment = graphql(`
  fragment UserAvatar on User {
    name
    avatarUrl
  }
`);

const ProfilePageQuery = graphql(`
  query ProfilePage($id: ID!) {
    user(id: $id) {
      id
      ...UserAvatar
    }
  }
`);
```

This is the core idea in Relay, and Apollo Client and the codegen client preset support it too.

### 184: What is fragment masking?

With fragment masking, a component can only read the fields from its own fragment, even if the parent query loaded more. The parent passes a masked reference, and the child "unmasks" it with a helper. It stops components from depending on fields they didn't ask for, which would break silently when someone else edits a query.

```tsx
import { FragmentType, useFragment } from "./gql";

function UserAvatar(props: { user: FragmentType<typeof UserAvatarFragment> }) {
  const user = useFragment(UserAvatarFragment, props.user);
  return <img src={user.avatarUrl} alt={user.name} />;
}
```

Relay always masks data, the codegen client preset does it with `useFragment` (a plain function, not a React hook), and Apollo Client supports it through its data masking feature.

### 185: How do you set up Apollo Client 4 in a React app?

```tsx
import { ApolloClient, HttpLink, InMemoryCache } from "@apollo/client";
import { ApolloProvider } from "@apollo/client/react";

const client = new ApolloClient({
  link: new HttpLink({ uri: "https://api.example.com/graphql" }),
  cache: new InMemoryCache(),
});

createRoot(document.getElementById("root")!).render(
  <ApolloProvider client={client}>
    <App />
  </ApolloProvider>,
);
```

In Apollo Client 4 you pass a link explicitly, the React parts come from `@apollo/client/react`, and RxJS is a peer dependency. Apollo Client 3 code often passes `uri` directly to the constructor and imports everything from `@apollo/client`.

### 186: How does Apollo Client choose cache IDs, and how do you change it?

By default it uses `__typename` plus `id` (or `_id`), like `Product:42`. If an object has no ID, it's stored inside its parent instead of as a separate entry. When a type uses a different key, set `keyFields` in `typePolicies`.

```js
const cache = new InMemoryCache({
  typePolicies: {
    Product: { keyFields: ["sku"] },
    Book: { keyFields: ["isbn", "edition"] },
    UserSettings: { keyFields: false }, // never normalize, keep inside parent
  },
});
```

Always request the ID fields in your queries, or the cache can't normalize the objects.

### 187: What are type policies and field policies in Apollo Client?

Type policies configure how a type is stored in the cache, like its `keyFields`. Field policies configure a single field with a `read` function (how to return it from the cache) and a `merge` function (how to combine incoming data with existing data).

```js
const cache = new InMemoryCache({
  typePolicies: {
    Product: {
      fields: {
        displayPrice: {
          read(_, { readField }) {
            return `$${(readField("priceInCents") / 100).toFixed(2)}`;
          },
        },
      },
    },
  },
});
```

Field policies are used for pagination, local-only fields, computed values and cache redirects.

### 188: How do you update the cache after a mutation?

There are three main ways:

1. **Automatic**: if the mutation returns the changed object with its `id` and the changed fields, Apollo updates the normalized entry by itself. This covers most updates.
2. **`refetchQueries`**: refetch the queries that might be affected. Simple, but it costs extra requests.
3. **`update` function**: change the cache yourself, which you need for adding or removing items from lists.

```js
const [addTodo] = useMutation(ADD_TODO, {
  update(cache, { data }) {
    cache.modify({
      fields: {
        todos(existing = []) {
          const ref = cache.writeFragment({
            data: data.addTodo,
            fragment: gql`
              fragment NewTodo on Todo {
                id
                text
                done
              }
            `,
          });
          return [...existing, ref];
        },
      },
    });
  },
});
```

### 189: What is the difference between `cache.modify`, `cache.writeQuery` and `cache.updateQuery`?

`cache.modify` changes specific fields of a cache entry directly, without a query, and works with references. `cache.writeQuery` writes data in the shape of a query, replacing what's there for those fields. `cache.updateQuery` reads a query from the cache, passes the result to your function and writes back what you return, which is often the easiest for list updates.

```js
cache.updateQuery({ query: GET_TODOS }, (data) => ({
  todos: data.todos.filter((t) => t.id !== deletedId),
}));
```

To remove an object completely, use `cache.evict({ id: cache.identify(obj) })` and then `cache.gc()`.

### 190: How do you implement optimistic UI with Apollo Client?

Pass an `optimisticResponse` that looks like the expected server result. Apollo writes it to the cache right away, so the UI updates immediately. When the real response arrives, it replaces the optimistic data. If the mutation fails, the optimistic data is rolled back.

```js
toggleTodo({
  variables: { id: todo.id },
  optimisticResponse: {
    toggleTodo: { __typename: "Todo", id: todo.id, done: !todo.done },
  },
});
```

The optimistic object needs the `__typename` and `id`, so Apollo knows which cache entry to update.

### 191: When would you use each fetch policy?

- `cache-first` (default): data that rarely changes, like a product page.
- `cache-and-network`: show cached data right away but also refresh it, like a feed.
- `network-only`: always fetch fresh data, but still save it in the cache, like a checkout total.
- `no-cache`: fetch and don't save, for one-off or sensitive data.
- `cache-only`: never touch the network, for data you know is already loaded or local state.
- `standby`: like `cache-first`, but doesn't update automatically when the cache changes.

### 192: How do you run a query on demand, like when a button is clicked?

Use `useLazyQuery`. It returns a function that runs the query and the result state.

```jsx
import { useLazyQuery } from "@apollo/client/react";

function Search() {
  const [search, { data, loading }] = useLazyQuery(SEARCH_PRODUCTS);

  return (
    <>
      <button onClick={() => search({ variables: { text: "shoes" } })}>
        Search
      </button>
      {loading && <p>Searching...</p>}
      {data?.search.map((p) => (
        <p key={p.id}>{p.title}</p>
      ))}
    </>
  );
}
```

You can also use `client.query()` directly from an event handler if you don't need the result in render state.

### 193: How do you implement infinite scroll with Apollo Client?

Use `fetchMore` from `useQuery` to load the next page, and a field policy that merges pages together. For Relay-style connections there's a ready helper.

```js
import { InMemoryCache } from "@apollo/client";
import { relayStylePagination } from "@apollo/client/utilities";

const cache = new InMemoryCache({
  typePolicies: {
    Query: { fields: { products: relayStylePagination(["filter"]) } },
  },
});
```

```jsx
const { data, fetchMore } = useQuery(GET_PRODUCTS, {
  variables: { first: 20 },
});

const loadMore = () =>
  fetchMore({ variables: { after: data.products.pageInfo.endCursor } });
```

The argument to `relayStylePagination` is the list of `keyArgs`: arguments that create separate lists in the cache. `offsetLimitPagination` is the helper for offset pagination.

### 194: How do you poll a query?

Set `pollInterval` in milliseconds. You can also start and stop polling with the functions `useQuery` returns.

```jsx
const { data, startPolling, stopPolling } = useQuery(GET_ORDER_STATUS, {
  variables: { id },
  pollInterval: 5000,
});
```

Polling is easy and works through any proxy, so it's often good enough instead of subscriptions for data that changes every few seconds.

### 195: What does `errorPolicy` do in Apollo Client?

It controls what happens when the response has GraphQL errors.

- `none` (default): the result is treated as an error, and `data` is `undefined`.
- `all`: you get both `data` (partial) and `error`, so you can show the parts that worked.
- `ignore`: errors are ignored, and you get whatever `data` came back.

```js
const { data, error } = useQuery(GET_DASHBOARD, { errorPolicy: "all" });
```

Use `all` for pages built from many independent fields, where one failing widget shouldn't blank the whole page.

### 196: What is Apollo Link?

Apollo Link is the request pipeline of Apollo Client. Each link can change the operation, add headers, log, retry, or send it over the network. You chain them with `ApolloLink.from`, and the last link in the chain, usually `HttpLink`, sends the request.

```js
import {
  ApolloClient,
  ApolloLink,
  HttpLink,
  InMemoryCache,
} from "@apollo/client";

const client = new ApolloClient({
  link: ApolloLink.from([
    errorLink,
    authLink,
    retryLink,
    new HttpLink({ uri: "/graphql" }),
  ]),
  cache: new InMemoryCache(),
});
```

### 197: How do you add an auth header to every request in Apollo Client?

Use a link that sets headers on the operation context. In Apollo Client 4 it's the `SetContextLink` class.

```js
import { SetContextLink } from "@apollo/client/link/context";

const authLink = new SetContextLink((prevContext) => {
  const token = localStorage.getItem("token");
  return {
    headers: {
      ...prevContext.headers,
      authorization: token ? `Bearer ${token}` : "",
    },
  };
});
```

Apollo Client 3 code uses the `setContext((operation, prevContext) => ...)` function from the same package. Note that the order of the arguments is different between the two.

### 198: How do you handle errors globally in Apollo Client?

Add an error link at the start of the chain. In Apollo Client 4 the error is one object, and you check its type with helper classes.

```js
import { CombinedGraphQLErrors } from "@apollo/client";
import { ErrorLink } from "@apollo/client/link/error";

const errorLink = new ErrorLink(({ error, operation }) => {
  if (CombinedGraphQLErrors.is(error)) {
    for (const err of error.errors) {
      if (err.extensions?.code === "UNAUTHENTICATED") redirectToLogin();
    }
  } else {
    console.error(`Network error in ${operation.operationName}:`, error);
  }
});
```

In Apollo Client 3 you used `onError(({ graphQLErrors, networkError }) => ...)`, and query errors had `graphQLErrors` and `networkError` properties. Apollo Client 4 replaced those with error classes like `CombinedGraphQLErrors` and `ServerError`.

### 199: How do you retry failed requests in Apollo Client?

Use `RetryLink`. By default it retries network errors a few times with exponential backoff and jitter. It doesn't retry GraphQL errors, because those usually aren't temporary.

```js
import { RetryLink } from "@apollo/client/link/retry";

const retryLink = new RetryLink({
  delay: { initial: 300, max: 5000, jitter: true },
  attempts: { max: 3, retryIf: (error, operation) => !!error },
});
```

Be careful with retrying mutations. If the first request reached the server but the response was lost, a retry can create a duplicate.

### 200: How do you use subscriptions with Apollo Client?

Add a `GraphQLWsLink` and split the traffic so subscriptions go over WebSockets and everything else over HTTP.

```js
import {
  ApolloClient,
  ApolloLink,
  HttpLink,
  InMemoryCache,
} from "@apollo/client";
import { GraphQLWsLink } from "@apollo/client/link/subscriptions";
import { getMainDefinition } from "@apollo/client/utilities";
import { createClient } from "graphql-ws";

const httpLink = new HttpLink({ uri: "/graphql" });
const wsLink = new GraphQLWsLink(
  createClient({ url: "wss://api.example.com/graphql" }),
);

const link = ApolloLink.split(
  ({ query }) => {
    const def = getMainDefinition(query);
    return (
      def.kind === "OperationDefinition" && def.operation === "subscription"
    );
  },
  wsLink,
  httpLink,
);

const client = new ApolloClient({ link, cache: new InMemoryCache() });
```

Then use `useSubscription(MESSAGE_ADDED, { variables: { roomId } })` in a component, or `subscribeToMore` to add events to an existing query's result.

### 201: How do you add subscriptions to an Apollo Server app?

Apollo Server handles HTTP only, so you run a `graphql-ws` server on the same HTTP server and give both the same schema.

```js
import http from "node:http";
import express from "express";
import { WebSocketServer } from "ws";
import { useServer } from "graphql-ws/use/ws";
import { makeExecutableSchema } from "@graphql-tools/schema";
import { ApolloServer } from "@apollo/server";
import { expressMiddleware } from "@as-integrations/express5";
import { ApolloServerPluginDrainHttpServer } from "@apollo/server/plugin/drainHttpServer";

const schema = makeExecutableSchema({ typeDefs, resolvers });
const app = express();
const httpServer = http.createServer(app);

const wsServer = new WebSocketServer({ server: httpServer, path: "/graphql" });
const wsCleanup = useServer({ schema }, wsServer);

const server = new ApolloServer({
  schema,
  plugins: [
    ApolloServerPluginDrainHttpServer({ httpServer }),
    {
      async serverWillStart() {
        return {
          async drainServer() {
            await wsCleanup.dispose();
          },
        };
      },
    },
  ],
});
await server.start();

app.use("/graphql", express.json(), expressMiddleware(server));
httpServer.listen(4000);
```

### 202: What is PubSub, and why shouldn't you use the in-memory one in production?

PubSub is the mechanism that connects "something happened" to subscription resolvers. Mutations publish events, and subscription resolvers listen to them.

```js
import { PubSub } from "graphql-subscriptions";

const pubsub = new PubSub();

const resolvers = {
  Mutation: {
    addPost: async (_, { input }, { db }) => {
      const post = await db.posts.create(input);
      await pubsub.publish("POST_ADDED", { postAdded: post });
      return post;
    },
  },
  Subscription: {
    postAdded: {
      subscribe: () => pubsub.asyncIterableIterator(["POST_ADDED"]),
    },
  },
};
```

The built-in `PubSub` keeps events in the memory of one process. If you run two server instances, a mutation handled by instance A never reaches subscribers connected to instance B. In production use a shared broker, like Redis (`graphql-redis-subscriptions`), Kafka, NATS or Postgres `LISTEN/NOTIFY`. In graphql-subscriptions v2 the method was called `asyncIterator`.

### 203: How do you filter subscription events per client?

Use `withFilter`, which runs a function for each event and only sends it to clients where the function returns `true`.

```js
import { withFilter } from "graphql-subscriptions";

const resolvers = {
  Subscription: {
    messageAdded: {
      subscribe: withFilter(
        () => pubsub.asyncIterableIterator(["MESSAGE_ADDED"]),
        (payload, variables, context) =>
          payload.messageAdded.roomId === variables.roomId &&
          context.user.rooms.includes(variables.roomId),
      ),
    },
  },
};
```

For high traffic, it's better to publish to a topic per room, like `MESSAGE_ADDED.42`, so the server doesn't run the filter for every event and every subscriber.

### 204: How can you use Server-Sent Events for subscriptions instead of WebSockets?

SSE is a one-way stream from server to client over normal HTTP. That's all subscriptions need, and it works better with proxies, load balancers, HTTP/2 and existing auth headers. GraphQL Yoga supports SSE subscriptions without any extra setup. For other servers there's the `graphql-sse` library, which has both a server handler and a client. WebSockets are still the better choice when you need two-way messaging over the same connection.

### 205: What is the difference between subscriptions and live queries?

A subscription sends an event when something specific happens, like "a message was added", and the client decides how to update its data. A live query is a normal query that the server re-sends whenever its result changes, so the client always has the current data without handling events. Live queries are not in the spec, but some tools support them, for example with an `@live` directive in The Guild's `graphql-live-query`.

### 206: Why is HTTP caching harder with GraphQL than with REST?

REST caching works by URL: `GET /products/42` can be cached by the browser, CDNs and proxies. GraphQL usually uses `POST` to one URL, and HTTP caches don't cache `POST`. Also, one response can mix public data with private user data, and each field can change at a different rate, so there's no single right `Cache-Control` value. That's why GraphQL clients cache in the app, and servers need extra tools for HTTP caching.

### 207: How can you cache GraphQL responses with a CDN?

1. Send queries with `GET`, so the URL includes the query (or its hash) and variables.
2. Use persisted queries so URLs are short and stable.
3. Have the server set `Cache-Control` headers based on what was queried.
4. Make sure private data is marked `private` or isn't cached at all.

With Apollo Client, `HttpLink` has a `useGETForQueries` option, and the persisted queries link can send hashed queries with `GET`.

### 208: How do Automatic Persisted Queries work?

1. The client sends only the SHA-256 hash of the query in `extensions.persistedQuery`.
2. If the server has the hash, it runs that query.
3. If not, it returns a `PERSISTED_QUERY_NOT_FOUND` error, and the client sends the hash again with the full query text.
4. The server saves the query under that hash for next time.

It makes requests smaller and works with `GET` caching, but any client can still register any query, so it isn't a security feature. Apollo Server supports APQ by default, and Apollo Client has a `PersistedQueryLink`.

### 209: What are trusted documents?

Trusted documents, also called persisted operations or an operation allowlist, means only queries known at build time can run. The build step extracts every operation from the client code, stores them on the server with their hashes, and the server rejects any request that isn't on the list. This blocks attackers from sending expensive or unusual queries. It works well for first-party apps, but not for public APIs where anyone can write queries.

### 210: How do cache control hints work in Apollo Server?

You mark types and fields with a `@cacheControl` directive (or set hints in resolvers). Apollo works out the policy for the whole response, using the smallest `maxAge` of all fields and `PRIVATE` if any field is private, and sets the `Cache-Control` header.

```graphql
enum CacheControlScope {
  PUBLIC
  PRIVATE
}

directive @cacheControl(
  maxAge: Int
  scope: CacheControlScope
  inheritMaxAge: Boolean
) on FIELD_DEFINITION | OBJECT | INTERFACE | UNION

type Product @cacheControl(maxAge: 300) {
  id: ID!
  name: String!
  stock: Int! @cacheControl(maxAge: 10)
}

type Query {
  me: User @cacheControl(maxAge: 0, scope: PRIVATE)
}
```

```js
const resolvers = {
  Query: {
    product: (_, { id }, ctx, info) => {
      info.cacheControl.setCacheHint({ maxAge: 60 });
      return ctx.db.products.findById(id);
    },
  },
};
```

Root fields and object fields without a hint default to `maxAge: 0`, which means not cacheable.

### 211: How do you cache whole responses on the server?

Apollo has `@apollo/server-plugin-response-cache`, which uses the cache hints to store full responses in memory, Redis or Memcached. GraphQL Yoga has `useResponseCache` from `@graphql-yoga/plugin-response-cache`, which can also invalidate entries automatically when a mutation returns a type and ID that a cached response contains. Response caching helps most for public, popular queries. For per-user data you need a session ID in the cache key, or it isn't worth it.

### 212: How do you limit query depth?

Add a validation rule that rejects queries nested deeper than a limit. It stops queries like `user { friends { friends { friends { ... } } } }` from asking for millions of objects.

```js
import depthLimit from "graphql-depth-limit";

const server = new ApolloServer({
  typeDefs,
  resolvers,
  validationRules: [depthLimit(10)],
});
```

GraphQL Armor (`@escape.tech/graphql-armor`) bundles depth, cost, alias and token limits for Apollo Server, Yoga and Envelop.

### 213: What is query cost analysis?

It gives each field a cost and adds them up before the query runs. Lists multiply the cost of their children by the requested page size, so `products(first: 100) { reviews(first: 50) { author } }` costs much more than its depth suggests. If the total is over a limit, the query is rejected. Depth limiting alone misses wide queries, so cost analysis is the better protection. Libraries like `graphql-query-complexity` and GraphQL Armor implement it, and the `@cost` and `@listSize` directives from IBM's cost specification, which Apollo Federation also supports, are a common way to annotate costs in the schema.

### 214: How do you rate limit a GraphQL API?

Counting requests per minute isn't enough, because one GraphQL request can be tiny or huge. Better options are limiting by query cost per time window (GitHub gives each client a budget of points per hour), limiting specific expensive fields or mutations with a directive like `@rateLimit`, and keeping a normal request limit at the gateway as a backstop. Return the remaining budget in `extensions` or headers so clients can slow down.

### 215: Should you disable introspection in production?

For a private API used only by your own apps, many teams turn it off so attackers can't easily list all types and fields. Apollo Server disables it by default when `NODE_ENV` is `production`. It's not real security, since the schema can often be guessed from client code or error messages, so it doesn't replace auth and cost limits. Public APIs keep it on, because developers need it.

```js
const server = new ApolloServer({
  typeDefs,
  resolvers,
  introspection: process.env.NODE_ENV !== "production",
});
```

### 216: What are field suggestions, and why can they be a problem?

When a query has a typo, graphql-js adds hints like `Cannot query field "emial" on type "User". Did you mean "email"?`. This is useful in development, but with introspection off, an attacker can use these hints to discover the schema one field at a time. Apollo Server has a `hideSchemaDetailsFromClientErrors` option to remove them, graphql-js 17 has a `hideSuggestions` option, and GraphQL Armor has a plugin that blocks them.

### 217: What is query batching, and what are the trade-offs?

Batching means sending several operations in one HTTP request, as a JSON array. Apollo Client has `BatchHttpLink` for it, and Apollo Server supports it if you set `allowBatchedHttpRequests: true`. It cuts down the number of requests, but the response waits for the slowest operation, caching gets harder, and attackers can use batches to get around per-request rate limits. With HTTP/2 the request overhead is small anyway, so batching is less useful than it used to be.

### 218: How do you add timeouts to slow resolvers?

Set timeouts on the things resolvers call, like HTTP requests and database queries, rather than on the resolver itself. For `fetch`, use `AbortSignal.timeout()`.

```js
const resolvers = {
  Product: {
    reviews: async (product) => {
      const res = await fetch(
        `https://reviews.internal/products/${product.id}`,
        {
          signal: AbortSignal.timeout(2000),
        },
      );
      if (!res.ok) throw new Error("Reviews service failed");
      return res.json();
    },
  },
};
```

If `reviews` is nullable, a timeout only empties that one field and the rest of the product still loads. Also set an overall request timeout on the HTTP server or load balancer.

### 219: What should you log for GraphQL requests?

Log the operation name, operation type, a hash of the query, the client name and version (from headers like `apollographql-client-name`), duration, error codes and the user or tenant ID. Since every request goes to `POST /graphql`, URL-based logs tell you nothing, so the operation name is your main way to group requests. Don't log variables by default, because they often contain passwords, tokens or personal data.

### 220: How do you monitor resolver performance per field?

Use tracing that records how long each resolver takes. Apollo GraphOS collects field-level traces through the usage reporting plugin. OpenTelemetry instrumentation, like `@opentelemetry/instrumentation-graphql` or Envelop's OpenTelemetry plugin, creates spans for parsing, validation, execution and resolvers. Tracing every field adds overhead, so sample a part of the requests or only trace non-trivial resolvers.

### 221: How do you write integration tests for a GraphQL API?

Start the server in the test (or use `executeOperation`), point it at a real test database, and send real operations. Check the `data` and `errors` of the response, and the state of the database after mutations.

```js
import { beforeAll, afterAll, test, expect } from "vitest";

let server;

beforeAll(async () => {
  await resetTestDatabase();
  server = new ApolloServer({ typeDefs, resolvers });
});

afterAll(() => server.stop());

test("createPost saves the post", async () => {
  const res = await server.executeOperation(
    {
      query: `mutation ($input: CreatePostInput!) {
        createPost(input: $input) { post { id title } errors { message } }
      }`,
      variables: { input: { title: "Hi", body: "First post" } },
    },
    { contextValue: buildTestContext({ userId: "u1" }) },
  );

  expect(res.body.kind).toBe("single");
  expect(res.body.singleResult.errors).toBeUndefined();
  expect(await db.posts.count()).toBe(1);
});
```

For HTTP-level tests, like headers, CORS or cookies, use `supertest` against the real Express app.

### 222: How do you mock GraphQL requests in front-end tests?

Mock Service Worker (MSW) intercepts requests and lets you answer them by operation name. Your app uses its real GraphQL client, so the test is close to production.

```js
import { graphql, HttpResponse } from "msw";
import { setupServer } from "msw/node";

const server = setupServer(
  graphql.query("GetUser", ({ variables }) =>
    HttpResponse.json({
      data: { user: { __typename: "User", id: variables.id, name: "Ana" } },
    }),
  ),
  graphql.mutation("UpdateUser", () =>
    HttpResponse.json({ errors: [{ message: "Not allowed" }] }),
  ),
);
```

### 223: How do you test React components that use Apollo Client?

Wrap them in `MockedProvider` with a list of expected requests and their responses. In Apollo Client 4 it's imported from `@apollo/client/testing/react`.

```jsx
import { render, screen } from "@testing-library/react";
import { MockedProvider } from "@apollo/client/testing/react";

const mocks = [
  {
    request: { query: GET_DOG, variables: { name: "Buck" } },
    result: {
      data: {
        dog: { __typename: "Dog", id: "1", name: "Buck", breed: "bulldog" },
      },
    },
  },
];

test("shows the dog", async () => {
  render(
    <MockedProvider mocks={mocks}>
      <Dog name="Buck" />
    </MockedProvider>,
  );
  expect(await screen.findByText("Buck is a bulldog")).toBeInTheDocument();
});
```

The query and variables in the mock must match exactly, or the test gets a "no more mocked responses" error. Many teams prefer MSW because it doesn't need exact matching.

### 224: How do you lint GraphQL schemas and operations?

Use `@graphql-eslint/eslint-plugin`. It runs ESLint rules on `.graphql` files and on GraphQL inside code. There are rules for operations, like "no unused fragments", "require IDs for cache normalization" and "no deprecated fields", and for schemas, like naming conventions, "require descriptions" and "no unreachable types". It reads `graphql-config` to know where the schema is.

### 225: How do you catch breaking schema changes in CI?

Compare the new schema with the one in production on every pull request. GraphQL Inspector (`graphql-inspector diff old.graphql new.graphql`) lists breaking, dangerous and safe changes. Apollo's `rover subgraph check` and Hive's `hive schema:check` go further and check the change against real client usage, so removing a field that nobody uses passes, but removing one that a mobile app still queries fails.

### 226: What is a schema registry?

It's a service that stores every published version of your schema, often with usage data from production. Teams use it to check schema changes against real traffic, see which clients use which fields, keep a change history and, with federation, compose subgraphs into the supergraph. Examples are Apollo GraphOS, GraphQL Hive and WunderGraph Cosmo.

### 227: How should you name mutations?

Use a verb and the object, in a way that reads like an action in your domain: `createPost`, `publishPost`, `addItemToCart`, `cancelOrder`. Prefer specific actions over generic ones like `updateOrder(status: CANCELLED)`, because specific mutations can have their own inputs, rules and errors. Some APIs put the object first (`postCreate`, `postPublish`) so related mutations sort together, which Shopify does. Either is fine if you're consistent.

### 228: How do you decide whether a field should be nullable?

Ask whether the field can ever be missing or fail on its own. IDs and fields stored in the same row as the parent are usually safe to make non-null. Fields loaded from another service or table, or that depend on permissions, are usually better nullable, so a failure only blanks that field. Lists are usually `[Item!]!`. Remember that changing nullable to non-null later is safe for outputs, but the reverse is a breaking change, so when unsure, many teams start nullable.

### 229: How do you validate input in a GraphQL API?

GraphQL already checks types, required fields and enum values. For everything else, like string length, email format, ranges or business rules, you have a few options: custom scalars for formats (`EmailAddress`), validation libraries like Zod in the resolver or service layer, or validation directives. Return problems as user errors in the payload for things the user can fix.

```js
import { z } from "zod";

const CreateUser = z.object({
  name: z.string().min(1).max(100),
  email: z.email(),
});

const resolvers = {
  Mutation: {
    createUser: async (_, { input }, { services }) => {
      const parsed = CreateUser.safeParse(input);
      if (!parsed.success) {
        return {
          user: null,
          errors: parsed.error.issues.map((i) => ({
            message: i.message,
            field: i.path.map(String),
          })),
        };
      }
      return { user: await services.users.create(parsed.data), errors: [] };
    },
  },
};
```

### 230: How do you implement a custom scalar?

Create a `GraphQLScalarType` with three functions: `serialize` turns the server value into JSON for the response, `parseValue` reads the value from variables, and `parseLiteral` reads it when it's written inline in the query.

```js
import { GraphQLScalarType, GraphQLError, Kind } from "graphql";

export const DateTime = new GraphQLScalarType({
  name: "DateTime",
  description: "ISO 8601 date-time string",
  serialize(value) {
    if (!(value instanceof Date))
      throw new GraphQLError("DateTime must be a Date");
    return value.toISOString();
  },
  parseValue(value) {
    const date = new Date(value);
    if (typeof value !== "string" || Number.isNaN(date.getTime())) {
      throw new GraphQLError("Invalid DateTime");
    }
    return date;
  },
  parseLiteral(ast) {
    if (ast.kind !== Kind.STRING)
      throw new GraphQLError("DateTime must be a string");
    return this.parseValue(ast.value);
  },
});

const resolvers = { DateTime, Query: {/* ... */} };
```

This is the graphql-js 16 API. graphql-js 17 renames these methods to `coerceOutputValue`, `coerceInputValue` and `coerceInputLiteral`, and keeps the old names as deprecated aliases.

### 231: How do you map enum values to different internal values?

By default, the internal value of an enum is its name as a string. In Apollo Server and graphql-tools you can map them in the resolver map, so resolvers work with your database values while clients see the enum names.

```graphql
enum Priority {
  LOW
  MEDIUM
  HIGH
}
```

```js
const resolvers = {
  Priority: { LOW: 1, MEDIUM: 2, HIGH: 3 },
  Query: {
    tasks: (_, { priority }, { db }) => db.tasks.findAll({ priority }), // priority is 1, 2 or 3
  },
};
```

### 232: How does the server know which type an interface or union value is?

You tell it with a `__resolveType` function on the abstract type, which returns the type name. Another option is an `isTypeOf` function on each object type.

```js
const resolvers = {
  SearchResult: {
    __resolveType(obj) {
      if (obj.email) return "User";
      if (obj.price !== undefined) return "Product";
      return "Article";
    },
  },
};
```

Checking for fields is fragile. It's safer to return objects with a type tag from your data layer, like `{ __typename: 'User', ... }` or a `kind` property, and read that.

### 233: What does "Abstract type must resolve to an Object type at runtime" mean?

It means a field returned an interface or union, but the server couldn't work out the concrete type of the value. Usually there's no `__resolveType`, it returned `undefined`, or it returned a name that isn't a member of the union. Fix the `__resolveType` function so it always returns one of the valid type names, or set `__typename` on the objects you return.

### 234: Can an interface implement another interface?

Yes, since the October 2021 spec. A type that implements the child interface must also list the parent interface.

```graphql
interface Node {
  id: ID!
}

interface Resource implements Node {
  id: ID!
  url: String!
}

type Image implements Resource & Node {
  id: ID!
  url: String!
  width: Int!
}
```

It helps when you have layers of shared fields, so you don't need to repeat fragments for each concrete type.

### 235: How do you query tree-shaped data like comments with replies?

Fragments can't refer to themselves, so you can't write a query that goes to any depth. You have three options: query a fixed depth (repeat the nesting a few levels), load children on demand when the user expands a node, or return a flat list with `parentId` and build the tree on the client. The flat list is often the simplest and works with any depth.

```graphql
type Comment {
  id: ID!
  parentId: ID
  text: String!
}

type Post {
  comments: [Comment!]! # all comments, flat
}
```

### 236: What are some validation rules that every GraphQL server checks?

The spec defines a set of rules that graphql-js exports as `specifiedRules`. Examples:

- Fields must exist on the type they're selected from.
- Leaf fields can't have selection sets, and object fields must have one.
- Every variable must be declared, used and of a compatible type.
- Required arguments must be given.
- Fragment names must be unique, and every fragment must be used.
- Fragments can't form cycles.
- Operation names must be unique in a document.
- Fields with the same response name must be mergeable.

### 237: How do you write a custom validation rule?

A validation rule is a function that gets a `ValidationContext` and returns AST visitors. Call `context.reportError` when something is wrong.

```js
import { GraphQLError } from "graphql";

export function NoDeprecatedFieldsRule(context) {
  return {
    Field(node) {
      const field = context.getFieldDef();
      if (field?.deprecationReason) {
        context.reportError(
          new GraphQLError(
            `Field "${field.name}" is deprecated: ${field.deprecationReason}`,
            { nodes: [node] },
          ),
        );
      }
    },
  };
}

const server = new ApolloServer({
  typeDefs,
  resolvers,
  validationRules: [NoDeprecatedFieldsRule],
});
```

Validation runs on every new query text, so keep rules cheap.

### 238: How should you represent money in a GraphQL schema?

Never use `Float`, because floating point can't store values like 0.1 exactly. Use an integer amount in the smallest unit (cents) or a decimal string, together with the currency.

```graphql
type Money {
  amount: String! # "19.99", decimal as string
  currencyCode: CurrencyCode!
}

type Product {
  price: Money!
}
```

Shopify uses this pattern. `Int` in cents also works, but remember that `Int` is 32-bit, so large totals can overflow.

### 239: What are the trade-offs of a `JSON` scalar?

A `JSON` scalar lets a field hold any value, which is handy for truly dynamic data like user-defined settings or metadata from another system. The cost is that you lose everything typed: clients can't select subfields, there's no validation, no documentation and no code generation, and normalized caches treat it as one opaque value. Use it only when the shape really is unknown, not to avoid modeling types.

### 240: How do you use an ORM like Prisma in resolvers?

Call the ORM from resolvers or, better, from a service layer, and still use DataLoader for relations. ORMs make it easy to write `include` for nested data in the root resolver, but that loads relations even when the query didn't ask for them.

```ts
const resolvers = {
  Query: {
    post: (_, { id }, { prisma }) => prisma.post.findUnique({ where: { id } }),
  },
  Post: {
    author: (post, _, { loaders }) => loaders.user.load(post.authorId),
  },
};
```

Prisma also batches some `findUnique` calls on its own when they run in the same tick, which helps with N+1 in simple cases.

### 241: How can a resolver load only the columns the query asked for?

Look at the selection set through the `info` argument. A library like `graphql-parse-resolve-info` handles fragments and aliases for you.

```js
import { parseResolveInfo } from "graphql-parse-resolve-info";

const resolvers = {
  Query: {
    users: (_, args, { sql }, info) => {
      const parsed = parseResolveInfo(info);
      const requested = Object.keys(parsed.fieldsByTypeName.User);
      const columns = requested.filter((f) => USER_COLUMNS.has(f));
      return sql`SELECT ${sql(["id", ...columns])} FROM users`;
    },
  },
};
```

It saves database work for wide tables, but it couples resolvers to the query shape, so use it only where it matters. Always add the columns that child resolvers need, like foreign keys.

### 242: What is `RESTDataSource`?

It's a class from `@apollo/datasource-rest` for calling REST APIs from resolvers. You extend it with methods for each endpoint. It deduplicates identical `GET` requests within one request and can cache responses based on their HTTP cache headers.

```js
import { RESTDataSource } from "@apollo/datasource-rest";

class MoviesAPI extends RESTDataSource {
  baseURL = "https://movies-api.example.com/";

  getMovie(id) {
    return this.get(`movies/${encodeURIComponent(id)}`);
  }
}

await startStandaloneServer(server, {
  context: async () => ({
    dataSources: { movies: new MoviesAPI({ cache: server.cache }) },
  }),
});
```

Create a new data source per request, just like DataLoaders.

### 243: How do you handle a failing downstream service in a resolver?

Decide whether the field is critical. For non-critical data, like recommendations, make the field nullable, catch or let the error bubble to that field, and log it, so the rest of the page loads. For critical data, let the error propagate, maybe with a clear code like `SERVICE_UNAVAILABLE`. Add timeouts, and consider a circuit breaker so a dead service doesn't slow every request down while you wait.

### 244: Where should business logic live in a GraphQL server?

In a service or domain layer, not in resolvers. Resolvers should read arguments, call a service, and map the result to the schema. This keeps rules like "only the author can edit a post" in one place, so they apply no matter which resolver, REST endpoint or job calls them, and makes them easy to test without GraphQL.

```js
const resolvers = {
  Mutation: {
    publishPost: (_, { id }, { services, user }) =>
      services.posts.publish({ id, actor: user }),
  },
};
```

### 245: How do you make mutations safe to retry?

Accept an idempotency key from the client, like `clientMutationId` or `idempotencyKey`, and store it with the result. If the same key comes in again, return the saved result instead of doing the work twice. This matters for payments and orders, where mobile clients on bad networks often retry.

```graphql
input PlaceOrderInput {
  idempotencyKey: ID!
  cartId: ID!
}
```

Mutations that set a value, like `setDisplayName`, are naturally idempotent. Mutations that add or charge are not.

### 246: How do you design bulk mutations?

Take a list in the input and return a result per item, so the client knows which ones failed.

```graphql
input UpdateProductPriceInput {
  id: ID!
  price: String!
}

type BulkUpdatePricesPayload {
  updated: [Product!]!
  errors: [BulkItemError!]!
}

type BulkItemError {
  index: Int!
  message: String!
}

type Mutation {
  bulkUpdatePrices(input: [UpdateProductPriceInput!]!): BulkUpdatePricesPayload!
}
```

Set a maximum list size, and decide whether the operation is all-or-nothing (one transaction) or best effort.

### 247: If a request has two mutation fields, do they run in one transaction?

No. Top-level mutation fields run one after another, but each one is independent. If the second fails, the first is not rolled back. If several changes must succeed or fail together, make one mutation that does all of them in one database transaction.

### 248: What should a delete mutation return?

At least the ID of the deleted object, so the client can remove it from its cache. Returning the deleted object or a payload type is also common.

```graphql
type DeletePostPayload {
  deletedPostId: ID
  errors: [UserError!]!
}
```

On the client, call `cache.evict({ id: cache.identify({ __typename: 'Post', id }) })` and `cache.gc()` after the mutation. Apollo doesn't remove deleted objects from lists on its own.

### 249: How do you stop clients from asking for huge pages?

Validate the page size argument and reject or cap anything over a maximum.

```js
const MAX_PAGE_SIZE = 100;

const resolvers = {
  Query: {
    products: (_, { first = 20, after }, { services }) => {
      if (first < 0 || first > MAX_PAGE_SIZE) {
        throw new GraphQLError(`first must be between 0 and ${MAX_PAGE_SIZE}`, {
          extensions: { code: "BAD_USER_INPUT" },
        });
      }
      return services.products.connection({ first, after });
    },
  },
};
```

GitHub requires `first` or `last` on every connection and limits it to 100. Without a limit, cost analysis can't estimate the size of lists.

### 250: How do you add search across several types?

Return a union or interface list from one search field, and let the client use fragments for each type.

```graphql
union SearchResult = User | Repository | Issue

type Query {
  search(
    query: String!
    types: [SearchType!]
    first: Int = 20
  ): [SearchResult!]!
}
```

On the server, query your search engine (like Elasticsearch or Postgres full-text search), and tag each hit with its type so `__resolveType` can pick it.

### 251: How do you return localized content from a GraphQL API?

Read the user's language from the `Accept-Language` header (or a user setting) when building the context, and let resolvers use it. Some APIs also add a `locale` argument to text fields for cases like an admin page that edits several languages.

```js
await startStandaloneServer(server, {
  context: async ({ req }) => ({
    locale:
      pickLocale(req.headers["accept-language"], ["en", "de", "ka"]) ?? "en",
  }),
});

const resolvers = {
  Product: {
    title: (product, _, { locale }) =>
      product.translations[locale]?.title ?? product.translations.en.title,
  },
};
```

If you use response caching or a CDN, the locale must be part of the cache key.

### 252: How do you handle multi-tenancy in a GraphQL server?

Work out the tenant once per request, from the subdomain, a header or the user's token, and put it in the context. Every service and data loader then filters by `context.tenantId`. Never take the tenant ID from query arguments without checking that the user belongs to it, and make loaders per request so cached rows from one tenant can't leak to another.

### 253: How do you run a GraphQL server in a Next.js route handler?

GraphQL Yoga works well here because it speaks the Fetch API.

```ts
// app/api/graphql/route.ts
import { createSchema, createYoga } from "graphql-yoga";

const { handleRequest } = createYoga({
  schema: createSchema({
    typeDefs: `type Query { greeting: String! }`,
    resolvers: { Query: { greeting: () => "Hello from Next.js" } },
  }),
  graphqlEndpoint: "/api/graphql",
  fetchAPI: { Response },
});

export {
  handleRequest as GET,
  handleRequest as POST,
  handleRequest as OPTIONS,
};
```

Apollo Server can also run in Next.js with the community `@as-integrations/next` package.

### 254: How do you use Apollo Client with the Next.js App Router?

Use `@apollo/client-integration-nextjs` (earlier called `@apollo/experimental-nextjs-app-support`). In Server Components you get a client per request with `registerApolloClient`. In Client Components you wrap the app in `ApolloNextAppProvider`, which handles streaming SSR and moves data from the server to the browser cache.

```ts
// lib/apollo-client.ts
import { HttpLink } from "@apollo/client";
import {
  registerApolloClient,
  ApolloClient,
  InMemoryCache,
} from "@apollo/client-integration-nextjs";

export const { getClient, query, PreloadQuery } = registerApolloClient(
  () =>
    new ApolloClient({
      cache: new InMemoryCache(),
      link: new HttpLink({ uri: "https://api.example.com/graphql" }),
    }),
);
```

```tsx
// app/page.tsx (Server Component)
export default async function Page() {
  const { data } = await query({ query: GET_PRODUCTS });
  return <ProductList products={data.products} />;
}
```

Don't share one client between server requests. It would mix users' data in one cache.

### 255: What is urql and how is it different from Apollo Client?

urql is a smaller GraphQL client built around "exchanges", which are like Apollo links. Its default cache is a document cache: it caches whole results by query and variables and refetches queries that include a `__typename` returned by a mutation. That's simpler but less precise than Apollo's normalized cache. If you need normalization, you add the Graphcache exchange.

```jsx
import { Client, Provider, cacheExchange, fetchExchange, useQuery } from "urql";

const client = new Client({
  url: "/graphql",
  exchanges: [cacheExchange, fetchExchange],
});

function Todos() {
  const [{ data, fetching, error }] = useQuery({ query: TodosQuery });
  if (fetching) return <p>Loading...</p>;
  if (error) return <p>{error.message}</p>;
  return (
    <ul>
      {data.todos.map((t) => (
        <li key={t.id}>{t.text}</li>
      ))}
    </ul>
  );
}
```

### 256: What is Relay and what makes it different?

Relay is Meta's GraphQL client for React. Every component declares its data as a fragment, the Relay compiler checks all GraphQL at build time and generates types and optimized artifacts, and data masking is always on. It expects the server to follow Relay conventions: the `Node` interface with global IDs and connections for pagination. It's very fast and scales to large apps, but it has a steeper learning curve and more rules than Apollo or urql.

```jsx
import { graphql, useFragment } from "react-relay";

function UserName({ user }) {
  const data = useFragment(
    graphql`
      fragment UserName_user on User {
        name
      }
    `,
    user,
  );
  return <span>{data.name}</span>;
}
```

### 257: How do you use GraphQL with TanStack Query?

Use a small request library like `graphql-request` (or `fetch`) inside `queryFn`. TanStack Query gives you caching, refetching and loading states, but its cache is keyed by query key, not normalized by object ID.

```tsx
import { useQuery } from "@tanstack/react-query";
import { request } from "graphql-request";
import { graphql } from "./gql";

const allFilms = graphql(`
  query AllFilms {
    allFilms {
      films {
        id
        title
      }
    }
  }
`);

function Films() {
  const { data, isPending } = useQuery({
    queryKey: ["films"],
    queryFn: () =>
      request("https://swapi-graphql.netlify.app/graphql", allFilms),
  });
  if (isPending) return <p>Loading...</p>;
  return (
    <ul>
      {data.allFilms.films.map((f) => (
        <li key={f.id}>{f.title}</li>
      ))}
    </ul>
  );
}
```

This works well for apps that mostly read data and don't need Apollo's cache updates.

### 258: What is a `TypedDocumentNode`?

It's a `DocumentNode` type that also carries the result type and the variables type as generics, from `@graphql-typed-document-node/core`. When you pass it to `useQuery`, `request()` or `client.query()`, TypeScript infers `data` and checks `variables` without you writing any generics. GraphQL Code Generator's client preset and gql.tada both produce typed document nodes, and most clients accept them.

### 259: What is gql.tada?

gql.tada is a TypeScript library that infers types for GraphQL documents directly from the query string, using the schema's introspection data. You write `graphql('query { ... }')`, and the result type is computed by TypeScript itself, with no code generation step to run. A TypeScript plugin adds autocomplete and validation in the editor. It's a good alternative to codegen if you want types to update instantly while typing.

### 260: How do you use persisted documents with GraphQL Code Generator?

Turn on `persistedDocuments` in the client preset. Codegen then writes a JSON file that maps hashes to documents, and the generated documents carry their hash.

```ts
const config: CodegenConfig = {
  schema: "./schema.graphql",
  documents: ["src/**/*.tsx"],
  generates: {
    "./src/gql/": {
      preset: "client",
      presetConfig: { persistedDocuments: true },
    },
  },
};
```

You upload `persisted-documents.json` to your server or registry during deploy, and the client sends only the hash. This is how you set up trusted documents.

### 261: How do you refresh an expired access token in Apollo Client?

Catch the `UNAUTHENTICATED` error in an error link, refresh the token and retry the operation with `forward`. Put the error link before the auth link, so the retry gets the new header.

```js
import { from, switchMap } from "rxjs";
import { CombinedGraphQLErrors } from "@apollo/client";
import { ErrorLink } from "@apollo/client/link/error";

let refreshing = null;

const errorLink = new ErrorLink(({ error, operation, forward }) => {
  const expired =
    CombinedGraphQLErrors.is(error) &&
    error.errors.some((e) => e.extensions?.code === "UNAUTHENTICATED");

  if (!expired) return;

  refreshing ??= refreshAccessToken().finally(() => {
    refreshing = null;
  });
  return from(refreshing).pipe(switchMap(() => forward(operation)));
});
```

Sharing one `refreshing` promise stops ten failing queries from refreshing the token ten times. If the refresh itself fails, log the user out.

### 262: Does Apollo Client send the same query twice if two components ask for it at the same time?

No. Query deduplication is on by default: if an identical query with the same variables is already in flight, Apollo waits for that one instead of sending a second request. You can turn it off per operation with `context: { queryDeduplication: false }`, for example when you really want a fresh request.

### 263: How do you manage local state with Apollo Client?

For small client-only values, use reactive variables. They live outside the cache, and any query that reads them updates when they change.

```js
import { makeVar, InMemoryCache, gql } from "@apollo/client";
import { useReactiveVar } from "@apollo/client/react";

export const cartOpenVar = makeVar(false);

const cache = new InMemoryCache({
  typePolicies: {
    Query: { fields: { cartOpen: { read: () => cartOpenVar() } } },
  },
});

const GET_CART_OPEN = gql`
  query {
    cartOpen @client
  }
`;

// in a component
const cartOpen = useReactiveVar(cartOpenVar);
cartOpenVar(true);
```

Fields with `@client` are resolved locally and never sent to the server. In Apollo Client 4, local resolvers are configured with the `LocalState` class. For most UI state, plain React state or a library like Zustand is simpler than putting it in the Apollo cache.

### 264: How do you clear the Apollo cache when a user logs out?

Call `client.clearStore()` to empty the cache without refetching, or `client.resetStore()` to empty it and refetch all active queries. On logout you usually want `clearStore()` and then a redirect, because `resetStore()` would refetch queries as an anonymous user and may show errors. Also stop any open subscriptions so they don't keep using the old token.

```js
async function logout() {
  await api.logout();
  await client.clearStore();
  router.push("/login");
}
```

### 265: How do you use React Suspense with Apollo Client?

Use `useSuspenseQuery` instead of `useQuery`. The component suspends while loading, so you show a `<Suspense>` fallback higher up, and errors go to an error boundary. `data` is always defined when the component renders.

```jsx
import { Suspense } from "react";
import { useSuspenseQuery } from "@apollo/client/react";

function Profile({ id }) {
  const { data } = useSuspenseQuery(GET_USER, { variables: { id } });
  return <h1>{data.user.name}</h1>;
}

export function ProfilePage({ id }) {
  return (
    <Suspense fallback={<p>Loading profile...</p>}>
      <Profile id={id} />
    </Suspense>
  );
}
```

To start loading before the component renders, for example in a router loader, use `createQueryPreloader` together with `useReadQuery`.

### 266: How do you change the Apollo Server landing page?

By default, Apollo Server shows Apollo Sandbox in development and a simple splash page in production. You change it with landing page plugins.

```js
import {
  ApolloServerPluginLandingPageLocalDefault,
  ApolloServerPluginLandingPageProductionDefault,
} from "@apollo/server/plugin/landingPage/default";
import { ApolloServerPluginLandingPageDisabled } from "@apollo/server/plugin/disabled";

const server = new ApolloServer({
  typeDefs,
  resolvers,
  plugins: [
    process.env.NODE_ENV === "production"
      ? ApolloServerPluginLandingPageDisabled()
      : ApolloServerPluginLandingPageLocalDefault({ embed: true }),
  ],
});
```

### 267: How do you add a health check to a GraphQL server?

Apollo Server 4 and 5 don't have a built-in health check endpoint. The docs suggest sending a tiny query like `{ __typename }` as a `GET` request with an `apollo-require-preflight: true` header, which checks that the server can parse and run operations. Many teams also add a separate `/healthz` route in Express that checks the database connection, since a load balancer usually needs a plain HTTP check.

```bash
curl -H 'apollo-require-preflight: true' 'http://localhost:4000/graphql?query=%7B__typename%7D'
```

### 268: How do you shut down a GraphQL server without dropping requests?

Stop taking new connections, let in-flight requests finish, close WebSockets, then close database pools. In Apollo Server, `ApolloServerPluginDrainHttpServer` drains the HTTP server when `server.stop()` is called, and Apollo Server calls `stop()` on `SIGINT` and `SIGTERM` by default (outside of tests). Add a `drainServer` hook for WebSocket servers, as in the subscriptions setup.

### 269: What is Envelop?

Envelop is a plugin system for GraphQL execution from The Guild. It wraps parse, validate, context building and execute, and plugins can hook into any of them. GraphQL Yoga is built on it, and there are plugins for response caching, depth limits, error masking, persisted operations, OpenTelemetry, auth and more. Plugins work with any server that uses Envelop, not only Yoga.

### 270: What is Mercurius?

Mercurius is a GraphQL server plugin for Fastify. It has built-in support for loaders (batching per field), subscriptions, JIT compilation of queries with graphql-jit, caching and federation. It's a good choice if you already use Fastify or care about raw speed. NestJS can use it as a driver instead of Apollo.

```js
import Fastify from "fastify";
import mercurius from "mercurius";

const app = Fastify();
app.register(mercurius, { schema: typeDefs, resolvers, graphiql: true });
await app.listen({ port: 4000 });
```

### 271: How do you choose a GraphQL server library for Node.js?

- **Apollo Server**: well known, lots of docs, good fit with Apollo GraphOS and Federation.
- **GraphQL Yoga**: runs on any JavaScript runtime, SSE subscriptions built in, large plugin set through Envelop.
- **Mercurius**: best if you're on Fastify and want speed.
- **NestJS GraphQL**: if your app is already NestJS, it gives you decorators and DI on top of Apollo or Mercurius.

The schema and resolvers look almost the same in all of them, so switching later isn't very hard.

### 272: How does GraphQL compare to tRPC?

tRPC shares TypeScript types between a TypeScript server and a TypeScript client directly, with no schema language or code generation. It's very fast to work with in a full-stack TypeScript monorepo. GraphQL has a language-independent schema, lets clients choose fields, supports many client types (mobile, third parties) and has a big tooling ecosystem. Pick tRPC for an internal TypeScript app with one front end, and GraphQL when you have several clients, several languages or a public API.

### 273: What guidelines would you follow when designing a public GraphQL API?

- Model your domain, not your database tables.
- Use clear, specific names and add descriptions to everything.
- Use connections with required page size limits for every list.
- Use input and payload types for mutations, with user errors.
- Use global IDs and the `Node` interface.
- Never remove things without deprecation and a long notice period.
- Put cost limits and rate limits in place from day one.
- Keep nullability on purpose, not by accident.

The public APIs of GitHub and Shopify are good examples to learn from.

### 274: How do you document a GraphQL schema?

Add descriptions with `"""` to every type, field, argument and enum value. These show up in GraphiQL, Apollo Sandbox, IDE tooltips and generated docs. Explain what the field means, units, formats, and edge cases like "null when the user has hidden their email". Tools like SpectaQL or GraphQL Hive's schema explorer can turn the schema into a static docs site. Add guides with example queries for common tasks, because a schema alone doesn't show how things fit together.

### 275: What is a good workflow for removing a deprecated field?

1. Add the replacement field.
2. Mark the old field `@deprecated` with a reason that names the replacement.
3. Track usage of the old field per client through your schema registry or logs.
4. Contact the teams or clients still using it.
5. Remove it once usage is zero (or after the announced date for public APIs).
6. Let the CI schema check confirm that nobody uses it anymore.

Mobile apps are the slow part, since old versions stay installed for months.

### 276: How should clients handle new enum values or new union members?

Assume the server can add new values later. In client code, always have a default branch when you switch on an enum or `__typename`, and show something reasonable for unknown values instead of crashing. In TypeScript, codegen can add a `%future added value` member (the `futureProofEnums` and `futureProofUnions` options) so the compiler forces you to handle it.

```ts
switch (order.status) {
  case "PAID":
    return "Paid";
  case "SHIPPED":
    return "On the way";
  default:
    return "Processing";
}
```

### 277: Is changing an argument's default value a breaking change?

It's not reported as breaking by most tools, because queries still validate. But it changes behavior for every client that relied on the old default, like `first` going from 50 to 10, so in practice it can break clients. Treat it as a dangerous change: announce it, or add a new argument instead.

### 278: How do you rename a field without breaking clients?

Add the new field next to the old one, make both use the same resolver, and deprecate the old one.

```graphql
type User {
  displayName: String!
  name: String! @deprecated(reason: "Use `displayName`.")
}
```

```js
const displayName = (user) => user.display_name;

const resolvers = {
  User: { displayName, name: displayName },
};
```

Once nobody uses `name`, remove it. Renaming a type is harder, because type names show up in fragments and `__typename` checks, so avoid it unless you really need to.

### 279: How do you add computed fields to a type?

Add the field to the type and write a resolver that calculates it from the parent. The client doesn't know or care whether it's stored or computed.

```graphql
type Order {
  items: [OrderItem!]!
  itemCount: Int!
  isOverdue: Boolean!
}
```

```js
const resolvers = {
  Order: {
    itemCount: (order) => order.items.length,
    isOverdue: (order) => order.status !== "PAID" && order.dueDate < new Date(),
  },
};
```

If a computed field is expensive, it only runs when a query asks for it, which is a nice side effect of field resolvers.

### 280: Where should arguments go, on root fields or on nested fields?

Put arguments where they describe the data. Filtering and paging a user's posts belongs on `User.posts(first:, status:)`, not on `Query.user`. This keeps each field reusable: `posts` works the same whether you reach the user from `me`, `user(id:)` or `post.author`. Root fields usually only take arguments to find the starting object.

### 281: Should relationships be exposed in both directions?

Usually yes, if clients need them. `Post.author` and `User.posts` let clients start from either side, which is one of the main benefits of a graph. Each direction is its own resolver, so it costs nothing until it's queried. Watch out for cycles that let clients build very deep queries, and keep depth and cost limits in place.

### 282: Should you expose your database IDs in the API?

It's common and fine for many apps, but there are downsides. Sequential IDs reveal how many records you have and make guessing other records easy, and they tie the API to one database. Opaque IDs, like base64 of `Type:id` or UUIDs, hide this and let you change storage later. Whatever you use, never rely on the ID being hard to guess for security. Always check permissions.

### 283: How do you handle "not sent" versus "set to null" in update inputs?

In a patch-style update, `{ bio: null }` means "clear the bio" and leaving `bio` out means "don't change it". GraphQL keeps this difference: in JavaScript, an omitted input field is missing from the object, while an explicit null is present with the value `null`.

```js
const resolvers = {
  Mutation: {
    updateProfile: (_, { input }, { services, user }) => {
      const changes = {};
      if ("bio" in input) changes.bio = input.bio; // may be null, meaning clear it
      if (input.name !== undefined) changes.name = input.name;
      return services.users.update(user.id, changes);
    },
  },
};
```

Don't use `input.bio ?? existing.bio`, because that treats "clear it" as "leave it". Some languages don't keep this difference by default, so check how your server library handles it.

### 284: What is the `me` or `viewer` pattern?

A root field that returns the currently logged-in user, like `me: User` or `viewer: User`. Everything the user can see hangs off it, like `me { orders { ... } notifications { ... } }`. It avoids passing the user ID from the client, which is both simpler and safer, because the server always uses the authenticated user from the context.

### 285: How do you design fields that need formatting options, like image sizes?

Give the field arguments, so the client asks for exactly what it needs.

```graphql
type Image {
  url(width: Int, height: Int, format: ImageFormat = WEBP): String!
  altText: String
}
```

A client can then ask for several sizes in one query using aliases. Prefer formatting options that the client can't easily do itself, like resized images. For dates, it's usually better to return ISO strings and let the client format them for the user's locale.

### 286: How should you handle time zones in a GraphQL API?

Store and return timestamps in UTC with an ISO 8601 `DateTime` scalar, like `"2026-10-23T09:00:00Z"`, and let clients convert to local time. For values that are not moments in time, like a birthday or "store opens at 09:00", use separate `Date` and `LocalTime` scalars without a time zone. If the time zone matters for the business, like an event in Tbilisi, return it as its own field (`timeZone: "Asia/Tbilisi"`).

### 287: What happens if a query asks for the same response key with different arguments?

Validation fails with an error that the fields "conflict because they have differing arguments". The executor can't put two different values under one key in the response. Use aliases to give them different keys.

```graphql
# invalid
{
  user(id: "1") {
    name
  }
  user(id: "2") {
    name
  }
}

# valid
{
  first: user(id: "1") {
    name
  }
  second: user(id: "2") {
    name
  }
}
```

The same rule applies when the conflict comes from fragments spread in the same place.

### 288: How do you handle errors for individual items in a list?

If the item type is nullable, like `[Product]!`, a failing item becomes `null` and the others still show. If it's `[Product!]!`, one failing item turns the whole list into `null` (or goes further up). So for lists where items can fail independently, like items loaded from another service, either make the items nullable or return a result union per item. For lists from one database query, items rarely fail alone, so `[Product!]!` is fine.

### 289: What is the difference between per-request caching and cross-request caching in resolvers?

Per-request caching, like DataLoader, only lives for one request. It's safe, because it can't serve another user's data or data older than the request. Cross-request caching, like Redis or an in-memory LRU, is shared between requests and users. It's much faster for hot data, but you need cache keys that include anything that changes the result (user, tenant, locale, permissions) and a plan for invalidation.

### 290: How do you cache a slow field across requests?

Cache the data the resolver loads, not the GraphQL response, using a key that includes all inputs.

```js
const resolvers = {
  Product: {
    reviewSummary: async (product, _, { redis, services }) => {
      const key = `review-summary:${product.id}`;
      const cached = await redis.get(key);
      if (cached) return JSON.parse(cached);

      const summary = await services.reviews.summary(product.id);
      await redis.set(key, JSON.stringify(summary), "EX", 300);
      return summary;
    },
  },
};
```

Clear the key when a new review is added, or accept that the data can be up to five minutes old.

### 291: How do you avoid request waterfalls on the client?

A waterfall happens when a parent component's query finishes, then a child renders and starts its own query, then its child does the same. Fix it by building one query per page from colocated fragments, so everything loads in one request. If parts are slow, load them separately but start them at the same time, not one after another, for example with preloading in the router. `@defer` is another option where it's supported.

### 292: What does `useFragment` do in Apollo Client?

It reads a fragment's data for one object directly from the cache, without sending a request. The component re-renders only when the fields in that fragment change, which helps performance in big lists. It's how Apollo supports fragment colocation: the parent query loads the data, and each child reads its own part.

```jsx
import { useFragment } from "@apollo/client/react";

function TodoItem({ id }) {
  const { data, complete } = useFragment({
    fragment: TODO_ITEM_FRAGMENT,
    from: { __typename: "Todo", id },
  });
  if (!complete) return null;
  return <li>{data.text}</li>;
}
```

### 293: How do you alert on GraphQL errors when the HTTP status is 200?

Status-based alerts miss GraphQL errors, because many responses with errors still return `200`. Count errors inside the server, for example in a plugin's `didEncounterErrors` hook, and send metrics tagged by operation name and error code. Then alert on the error rate per operation, and treat `INTERNAL_SERVER_ERROR` differently from expected codes like `BAD_USER_INPUT`. Using the `application/graphql-response+json` response type also gives you real 4xx statuses for requests that fail before execution.

### 294: How do you deploy Apollo Server on AWS Lambda?

Use the `@as-integrations/aws-lambda` package, which turns the server into a Lambda handler.

```js
import { ApolloServer } from "@apollo/server";
import {
  startServerAndCreateLambdaHandler,
  handlers,
} from "@as-integrations/aws-lambda";

const server = new ApolloServer({ typeDefs, resolvers });

export const graphqlHandler = startServerAndCreateLambdaHandler(
  server,
  handlers.createAPIGatewayProxyEventV2RequestHandler(),
  { context: async ({ event }) => ({ token: event.headers.authorization }) },
);
```

Create the server outside the handler, so warm invocations reuse it. Subscriptions don't fit Lambda well, since there are no long-lived connections.

### 295: When should you send GraphQL queries with `GET`?

Use `GET` for queries you want HTTP caches or CDNs to store, usually together with persisted queries so the URL stays short. The query, variables (as JSON) and operation name go in URL parameters. Keep `POST` for mutations, large queries and anything with sensitive variables, because URLs end up in logs and browser history.

```
GET /graphql?query=query%20GetProduct($id:ID!){product(id:$id){name}}&variables={"id":"1"}
```

### 296: How do you handle numbers larger than 32 bits?

The built-in `Int` is a signed 32-bit integer, so values above about 2.1 billion fail. For larger numbers, like IDs from a big table, byte counts or amounts in cents, use a custom `BigInt` or `Long` scalar, or return them as `String` or `ID`. JSON numbers in JavaScript lose precision above `2^53 - 1`, so a string is the safest way to send big integers.

### 297: Should GraphiQL or Apollo Sandbox be available in production?

For private APIs, usually not, or only behind authentication. It's not dangerous on its own, but it makes exploring your API easy, and with introspection off it won't work well anyway. Public APIs often keep an explorer available, because it helps developers use the API, like GitHub's GraphQL Explorer.

### 298: What are `@defer` and `@stream`, and are they standard?

`@defer` lets the server send part of a query later, so the fast fields arrive first. `@stream` sends list items one by one as they're ready. They are described in the incremental delivery RFC but are not in the September 2025 spec yet. Apollo Client and Apollo Router support `@defer`, GraphQL Yoga supports both through a plugin, and graphql-js 17 has them behind an experimental flag. The response is sent as a multipart HTTP response or over SSE.

```graphql
query ProductPage($id: ID!) {
  product(id: $id) {
    name
    price
    ... @defer {
      reviews(first: 10) {
        text
        rating
      }
    }
  }
}
```

### 299: How do servers know which client app sent a request?

Clients send their name and version in headers, like `apollographql-client-name: web` and `apollographql-client-version: 3.4.1`, which Apollo's tools understand. The server reads them for logs, metrics and schema usage reports, so you can see that an old iOS version still uses a deprecated field.

```js
const link = new HttpLink({
  uri: "/graphql",
  headers: {
    "apollographql-client-name": "web",
    "apollographql-client-version": import.meta.env.VITE_APP_VERSION,
  },
});
```

### 300: How would you debug a slow GraphQL query?

1. Find the operation name in logs or traces and get the exact query and variables.
2. Look at the resolver timings in a trace to see which fields take the time.
3. Check for N+1: many small database calls for one list usually means a missing DataLoader.
4. Check the database queries for missing indexes or loading too much data.
5. Check calls to other services and whether they run one after another when they could run in parallel.
6. Check the query itself. Maybe it asks for huge pages or deep nesting that the UI doesn't need.
7. Fix the biggest cost first, then measure again.

## Advanced Questions (301-450)

### 301: Walk through how graphql-js executes an operation.

1. It picks the operation to run (by `operationName` if there are several) and coerces the variables against their declared types.
2. It gets the root type (`Query`, `Mutation` or `Subscription`) and the root value.
3. `collectFields` flattens the selection set: it applies `@skip` and `@include`, expands fragments that match the type and groups fields by response key.
4. For each response key, it calls the field's resolver (or the default resolver) with `parent`, `args`, `context` and `info`.
5. `completeValue` handles the result: it waits for promises, checks non-null, walks lists item by item, picks the concrete type for interfaces and unions, serializes scalars and enums, and for objects goes back to step 3 with the child selection set.
6. Errors are caught per field, the field becomes `null`, and the null bubbles up to the nearest nullable parent if needed.
7. The final result is `{ data, errors }`.

For queries, sibling fields are started together. For mutations, root fields run one at a time.

### 302: How does field collection handle fragments and duplicates?

`collectFields` goes through the selection set in order. Fields with `@skip(if: true)` or `@include(if: false)` are dropped. Fragment spreads and inline fragments are expanded only if their type condition matches the current object type (or is an interface or union that includes it), and each named fragment is only expanded once per selection set. Fields with the same response key are grouped into one list of field nodes, and their sub-selections are merged when the child value is resolved. That's why `{ me { name } me { email } }` returns one `me` object with both fields, and why the validation rule that checks overlapping fields can be merged has to exist.

### 303: How would you use nullability to create error boundaries in a schema?

Null propagation stops at the first nullable field, so nullable fields act like error boundaries. Put them where a failure should be contained: around data from other services, around fields that depend on permissions, and on list items that load independently. Keep fields non-null inside a unit that always loads together, like the scalar fields of a row. For example, `Product.reviews` nullable means a reviews-service outage blanks only the reviews section, while `Product.name` being non-null is fine because it comes from the same row as `Product.id`.

### 304: How does graphql-js handle a mix of sync and async resolvers?

The executor checks whether each resolver returned a promise. If all resolvers in a selection set return plain values, it builds the result synchronously and doesn't create promises at all. As soon as one field returns a promise, the containing object becomes a promise that resolves when all its fields are done. That's why returning plain values from cheap resolvers, instead of marking every resolver `async`, can make a measurable difference for large responses.

### 305: What is the performance cost of resolvers, and how can you reduce it?

Every field of every object calls a function, even the default resolver, and adds work for value completion. A list of 10,000 objects with 10 fields means 100,000 resolver calls before any I/O. You can reduce it by:

- Avoiding `async` on resolvers that don't do async work.
- Keeping middleware that wraps every resolver (tracing, auth) only on fields that need it.
- Not returning huge lists. Paginate instead.
- Using a JIT executor like graphql-jit for hot queries.
- Caching parse and validate results.

### 306: Why should you cache parsed and validated documents?

Parsing and validation depend only on the query text and the schema, not on the variables. For apps that send the same few hundred queries again and again, redoing them every time wastes CPU. Apollo Server keeps an LRU cache of parsed and validated documents by default, and Yoga and Envelop have a parser cache plugin. Persisted operations make this even better, because the set of documents is fixed.

### 307: What is graphql-jit?

graphql-jit compiles a query into a JavaScript function specialized for that query and schema, instead of walking the AST on every request with the generic executor. Compiled queries can be much faster, especially for large responses. It's used by Mercurius and available as an Envelop plugin. The trade-offs are a compile step per new query (so it needs a cache), less support for some newer features, and small differences from graphql-js behavior in edge cases.

### 308: How does introspection work under the hood?

Introspection is part of the schema. Every schema has hidden meta fields on the query root type: `__schema: __Schema!` and `__type(name: String!): __Type`. The `__Type` type has a `kind` (`SCALAR`, `OBJECT`, `INTERFACE`, `UNION`, `ENUM`, `INPUT_OBJECT`, `LIST`, `NON_NULL`), plus `fields`, `interfaces`, `possibleTypes`, `enumValues`, `inputFields` and `ofType`. Wrapper types like `[User!]!` are represented as nested `NON_NULL` and `LIST` types linked with `ofType`. graphql-js resolves these fields from the `GraphQLSchema` object, so introspection always matches the running schema.

### 309: How do you get a usable schema object from a running server?

Send the standard introspection query, then turn the result into a schema with `buildClientSchema`. The result has types but no resolvers, which is enough for validation, code generation and tools.

```js
import { getIntrospectionQuery, buildClientSchema, printSchema } from "graphql";

const res = await fetch("https://api.example.com/graphql", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ query: getIntrospectionQuery() }),
});
const { data } = await res.json();
const schema = buildClientSchema(data);
console.log(printSchema(schema));
```

Introspection doesn't include custom schema directives on types and fields, so directive-based metadata is lost. That's one reason teams publish the SDL to a registry instead.

### 310: How do you walk and change a GraphQL AST?

Use `visit` from graphql-js. You pass visitor functions per node kind. Returning a new node replaces it, returning `null` deletes it, and returning `undefined` leaves it unchanged.

```js
import { parse, print, visit, Kind } from "graphql";

const ast = parse("query { me { name email } }");

const withoutEmail = visit(ast, {
  Field(node) {
    if (node.name.value === "email") return null;
  },
});

console.log(print(withoutEmail)); // query { me { name } }
```

Tools use this to add `__typename`, strip `@client` fields, compute query cost or rewrite queries in gateways.

### 311: What is `TypeInfo` used for?

When you visit a query AST, the nodes don't know their types. `TypeInfo` tracks the current parent type, field definition, argument and input type as you walk, so you can ask "what type is this field?" at any node. Combine it with `visitWithTypeInfo`. Validation rules use the same idea through `ValidationContext`.

```js
import { TypeInfo, visit, visitWithTypeInfo } from "graphql";

const typeInfo = new TypeInfo(schema);
visit(
  ast,
  visitWithTypeInfo(typeInfo, {
    Field() {
      const parent = typeInfo.getParentType();
      const field = typeInfo.getFieldDef();
      console.log(`${parent?.name}.${field?.name}`);
    },
  }),
);
```

### 312: What is the difference between executable directives and type system directives?

Executable directives are used in queries, at locations like `QUERY`, `FIELD`, `FRAGMENT_SPREAD` and `INLINE_FRAGMENT`. `@skip`, `@include` and `@defer` are examples. Type system directives are used in the schema, at locations like `OBJECT`, `FIELD_DEFINITION`, `ARGUMENT_DEFINITION` and `INPUT_OBJECT`. `@deprecated`, `@oneOf`, `@key` and custom `@auth` are examples. graphql-js doesn't run type system directives for you. Tools read them from the SDL and act on them, for example by wrapping resolvers.

### 313: What are directive locations and repeatable directives?

When you define a directive, you list where it may be used with `on`, and validation rejects it anywhere else. Adding `repeatable` allows using it more than once at the same location.

```graphql
directive @tag(name: String!) repeatable on FIELD_DEFINITION | OBJECT

type Product @tag(name: "public") @tag(name: "catalog") {
  id: ID!
}
```

Without `repeatable`, using the same directive twice on one element is a validation error.

### 314: How do you write a schema directive that changes field results?

Use `mapSchema` to wrap the resolver of every field that has the directive. Here's a `@lowercase` directive.

```js
import { mapSchema, getDirective, MapperKind } from "@graphql-tools/utils";
import { defaultFieldResolver } from "graphql";

const typeDefs = `
  directive @lowercase on FIELD_DEFINITION
  type Query { hello: String @lowercase }
`;

function lowercaseDirective(schema) {
  return mapSchema(schema, {
    [MapperKind.OBJECT_FIELD]: (fieldConfig) => {
      if (!getDirective(schema, fieldConfig, "lowercase")?.[0])
        return fieldConfig;
      const { resolve = defaultFieldResolver } = fieldConfig;
      fieldConfig.resolve = async (...args) => {
        const result = await resolve(...args);
        return typeof result === "string" ? result.toLowerCase() : result;
      };
      return fieldConfig;
    },
  });
}

let schema = makeExecutableSchema({
  typeDefs,
  resolvers: { Query: { hello: () => "HELLO" } },
});
schema = lowercaseDirective(schema);
```

Note that this makes the resolver async, so it adds a promise for every call. For hot fields, keep the sync path when the original result isn't a promise.

### 315: What rules apply to OneOf input objects?

- Every field of a `@oneOf` input must be nullable and can't have a default value.
- The client must provide exactly one field, and its value can't be `null`.
- If the value comes from a variable, like `{ id: $id }`, that variable must be declared non-null (`ID!`), so it can never be null at runtime.
- Introspection exposes it through `__Type.isOneOf`.

This lets the schema express "exactly one of these" instead of making everything optional and checking in the resolver.

### 316: What are the rules when a type implements an interface?

The type must have every field of the interface with the same name. Each field's return type must be the same or a subtype (covariant): a non-null version, a type that implements the returned interface, or a member of the returned union. It must accept every argument of the interface field with exactly the same type, and any extra arguments it adds must be optional. If the interface implements other interfaces, the type must list those too.

```graphql
interface Owner {
  pets: [Pet]
}

type Person implements Owner {
  pets: [Dog!]! # valid if Dog implements Pet
}
```

### 317: What are the input coercion rules in GraphQL?

- An `Int` value can be used where a `Float` is expected, but a float can't be used for an `Int`.
- `ID` accepts both strings and integers and turns them into strings.
- Strings are not converted to numbers or booleans: `"5"` for an `Int` is an error.
- A single value is wrapped into a list when a list is expected: `ids: "1"` becomes `["1"]`.
- Input object fields that aren't in the type are an error, and missing required fields are an error.
- Omitted fields with a default get the default value. Omitted fields without one are left out entirely, which is different from `null`.

### 318: What are the result coercion rules?

When a resolver returns a value for a scalar, the server serializes it to the declared type. Some compatible values are converted, like a number to `"1"` for `String` or an integer-valued float to `Int`. Values that can't be represented are a field error: `1.5` for `Int`, a number outside the 32-bit range, or an object for `String`. For enums, the value must map to a defined enum value. Errors here are field errors, so they null out the field and propagate like any other error.

### 319: When can a nullable variable be used for a non-null argument?

Normally a variable used in a non-null position must be declared non-null. There's one exception: if the variable has a non-null default value, or the argument itself has a default value, a nullable variable is allowed. If the client then sends an explicit `null` for that variable, the server raises an error at execution time.

```graphql
type Query {
  products(first: Int! = 10): [Product!]!
}
```

```graphql
query ($first: Int) {
  products(first: $first) {
    id
  }
} # allowed, the argument has a default
```

### 320: What denial of service risks are specific to GraphQL?

- **Deep nesting**: following cycles like `user.friends.friends.friends`.
- **Wide queries**: large page sizes multiplied at several levels.
- **Alias overloading**: the same expensive field repeated hundreds of times with aliases.
- **Field duplication**: the same field repeated many times, which can slow validation.
- **Fragment tricks**: huge documents built from fragments.
- **Directive overloading**: thousands of directives on one field.
- **Batching**: many operations in one HTTP request.
- **Introspection abuse**: very deep introspection queries.

Defend with depth, cost, alias, token and batch limits, timeouts, and trusted documents for first-party clients.

### 321: How can aliases be used for brute-force attacks?

Rate limiters that count HTTP requests see one request, but the query can contain hundreds of attempts.

```graphql
mutation {
  a1: login(email: "ana@example.com", password: "123456") {
    token
  }
  a2: login(email: "ana@example.com", password: "password") {
    token
  }
  a3: login(email: "ana@example.com", password: "qwerty") {
    token
  }
  # ... 500 more
}
```

Defend by limiting the number of aliases (or root fields) per operation, rate limiting sensitive mutations per field and per account in the business layer, and adding things like account lockout and CAPTCHAs that don't depend on the transport.

### 322: Why do field duplication and directive overloading cause problems?

Some validation rules, like the one that checks overlapping fields, can take a lot of time on documents with many repeated fields, because they compare fields with each other. A tiny query with thousands of copies of the same field, or thousands of directives, can make the server burn CPU before any resolver runs. Parsers and validators have gotten better, but you should still cap the document size, the number of tokens and the number of directives.

### 323: How does GraphQL protect against circular fragments?

Validation has a rule that fragments can't form cycles, directly or indirectly. Without it, `fragment A on User { friends { ...B } }` and `fragment B on User { ...A }` would expand forever. The executor also expands each fragment only once per selection set. Make sure you never skip the standard validation rules, for example by executing documents without validating them first.

### 324: How can introspection be used for denial of service?

The introspection schema has cycles too: `__Type.fields` returns fields, whose `type` returns `__Type` again, and so on. A query that nests `fields { type { fields { type { ... } } } }` many levels deep can produce a very large response from a big schema. Recent graphql-js 16 versions include a validation rule that limits introspection depth, and depth limits or disabling introspection also help. Make sure your depth limit rule doesn't skip introspection fields.

### 325: How do injection attacks happen in GraphQL APIs?

GraphQL validates types, but a `String` argument can still hold anything. If resolvers build SQL, NoSQL filters, shell commands or URLs from arguments, the usual injection attacks apply. A `JSON` argument passed straight into a MongoDB filter can let an attacker inject operators like `$ne`. Use parameterized queries, never pass client objects straight into database filters, and validate formats with custom scalars or schema validation.

### 326: Why is authorization easy to get wrong with GraphQL?

The same object can be reached through many paths: `order(id:)`, `node(id:)`, `me.orders`, `product.orders`, `customer.lastOrder`, and maybe through federation. If the permission check is written in one resolver, the other paths skip it. Put checks in the data access layer, ideally where the object is loaded (for example in the DataLoader or service that loads orders), so every path goes through the same rule. Test the `node` field specifically, since it's a common way around field-level checks.

### 327: What is an IDOR, and how does it show up in GraphQL?

IDOR (Insecure Direct Object Reference) is when a user can access another user's object just by changing an ID. In GraphQL it often looks like `invoice(id: "123")` returning any invoice, or a mutation like `updateAddress(id:)` not checking ownership. Global IDs that look random don't fix it, because they're just encoded. Always check that the current user may access the specific object, and write tests that try to access other users' IDs.

### 328: How can error messages leak information, and how do you prevent it?

Different errors for "user doesn't exist" and "wrong password" let attackers find valid emails. Differences in response time can do the same. Internal error messages can reveal table names, file paths or library versions. Return the same message and similar timing for failed logins, mask unexpected errors in production, avoid putting internal details in `extensions`, and log the full error on the server with a request ID that the client can report.

### 329: Why must mutations never run over `GET`?

`GET` requests can be triggered by any website through an image tag or a link, so a mutation over `GET` is an easy CSRF attack. Browsers, proxies and crawlers may also prefetch or repeat `GET` requests, which shouldn't change data. The GraphQL over HTTP spec says servers must not run mutations from `GET` requests, and Apollo Server and Yoga reject them. Make sure any custom transport or gateway does the same.

### 330: What does using trusted documents protect against, and what doesn't it protect against?

With only pre-registered operations allowed, attackers can't send their own queries, so deep queries, alias attacks, introspection and field guessing are blocked. It doesn't protect against abuse of the allowed operations themselves: an attacker can still call `login` a thousand times, page through data with the allowed `products` query, or change variables to access other users' data. You still need authorization, rate limiting and limits on variables like page size.

### 331: How would you implement a simple query cost calculation?

Walk the operation with `TypeInfo`, give each field a base cost, and multiply child costs by the requested list size.

```js
import {
  TypeInfo,
  visit,
  visitWithTypeInfo,
  getNamedType,
  isListType,
  getNullableType,
  isCompositeType,
} from "graphql";

export function estimateCost(schema, document, variables, maxCost = 1000) {
  const typeInfo = new TypeInfo(schema);
  const multipliers = [1];
  let cost = 0;

  visit(
    document,
    visitWithTypeInfo(typeInfo, {
      Field: {
        enter(node) {
          const field = typeInfo.getFieldDef();
          if (!field) return;
          const current = multipliers.at(-1);
          if (isCompositeType(getNamedType(field.type))) cost += current;

          let size = 1;
          if (isListType(getNullableType(field.type))) {
            const arg = node.arguments?.find((a) => a.name.value === "first");
            if (arg?.value.kind === "Variable")
              size = variables[arg.value.name.value] ?? 10;
            else if (arg?.value.kind === "IntValue")
              size = Number(arg.value.value);
            else size = 10;
          }
          multipliers.push(current * size);
        },
        leave() {
          multipliers.pop();
        },
      },
    }),
  );

  if (cost > maxCost)
    throw new Error(`Query cost ${cost} is over the limit of ${maxCost}`);
  return cost;
}
```

This is simplified: a real version also handles fragments spread across types and connection `edges`, and uses per-field costs from directives. In practice, use a library like `graphql-query-complexity` or GraphQL Armor and tune the settings.

### 332: What happens to a running query when the client disconnects?

By default, many servers keep running resolvers until the operation finishes, even though nobody will read the result. For expensive queries that wastes database and CPU time. You can listen for the request `close` event and pass an `AbortSignal` in the context, then pass that signal to `fetch` calls and database drivers that support it. graphql-js 17 supports this directly: you pass an `AbortSignal` to execution, it stops running further resolvers when the signal is aborted, and resolvers can read it with `info.getAbortSignal()`.

```js
context: async ({ req, res }) => {
  const controller = new AbortController();
  res.on("close", () => {
    if (!res.writableEnded) controller.abort();
  });
  return { signal: controller.signal };
};
```

### 333: How do you limit the size of incoming documents?

Limit the HTTP body size (for example `express.json({ limit: '100kb' })`), and limit the number of tokens the parser will accept. graphql-js's `parse` has a `maxTokens` option, and GraphQL Armor has a max tokens plugin for Apollo Server and Yoga. A token limit stops huge documents before validation runs, which is cheaper than depth or cost checks. With trusted documents, you can skip this for known hashes.

```js
import { parse } from "graphql";

const document = parse(source, { maxTokens: 2000 });
```

### 334: Explain the architecture of Apollo Federation.

- **Subgraphs**: independent GraphQL services, each owning part of the schema and using federation directives like `@key`.
- **Composition**: a tool (Rover or GraphOS) combines all subgraph schemas into one supergraph schema and checks that they fit together.
- **Router**: receives client queries, builds a query plan from the supergraph schema, sends sub-queries to the subgraphs (in parallel where possible), and merges the results.

Clients see one schema and don't know that several services answer their query. Each team can deploy its subgraph separately, as long as composition still works.

### 335: What are entities and the `@key` directive?

An entity is a type that can be resolved by more than one subgraph. `@key` says which fields uniquely identify it, so the router can pass a reference from one subgraph to another.

```graphql
# users subgraph
extend schema
  @link(url: "https://specs.apollo.dev/federation/v2.3", import: ["@key"])

type User @key(fields: "id") {
  id: ID!
  name: String!
}
```

```graphql
# orders subgraph
extend schema
  @link(url: "https://specs.apollo.dev/federation/v2.3", import: ["@key"])

type User @key(fields: "id") {
  id: ID!
  orders: [Order!]!
}
```

The router can now query `me { name orders { total } }` by getting `name` from users and `orders` from the orders subgraph. A type can have several keys, and keys can have several fields, like `@key(fields: "sku region")`.

### 336: What does `__resolveReference` do?

It's the resolver a subgraph uses to load an entity when the router only has its key fields. The router sends a representation like `{ __typename: "User", id: "1" }`, and the subgraph turns it into a full object.

```js
import { buildSubgraphSchema } from "@apollo/subgraph";

const resolvers = {
  User: {
    __resolveReference(ref, { loaders }) {
      return loaders.user.load(ref.id);
    },
  },
};

const server = new ApolloServer({
  schema: buildSubgraphSchema({ typeDefs, resolvers }),
});
```

The router sends many representations in one `_entities` request, so `__resolveReference` is called once per entity. Use a DataLoader there, or you get N+1 inside the subgraph.

### 337: What do `@shareable`, `@external`, `@requires` and `@provides` do?

- `@shareable`: the field (or all fields of a type) can be resolved by more than one subgraph. In Federation 2, non-key fields can only be defined in one subgraph unless they're shareable.
- `@external`: the field is defined in another subgraph, and this subgraph only refers to it.
- `@requires(fields: "...")`: to resolve this field, the subgraph needs some external fields first. The router fetches them and passes them in the representation.
- `@provides(fields: "...")`: when this field returns an entity, it also returns some of that entity's external fields, so the router can skip a fetch.

```graphql
type Product @key(fields: "id") {
  id: ID!
  weight: Float @external
  shippingCost: Float @requires(fields: "weight")
}
```

### 338: How do you move a field from one subgraph to another with Federation?

Use `@override`. Add the field to the new subgraph with `@override(from: "OldSubgraph")`, deploy it, and the router starts sending that field to the new subgraph. Then remove the field from the old subgraph. Federation 2.7 added progressive override with a `label` like `"percent(10)"`, so you can send a share of traffic to the new subgraph first (this is an enterprise router feature).

```graphql
type Product @key(fields: "id") {
  id: ID!
  inStock: Boolean! @override(from: "products")
}
```

### 339: What is a query plan in Federation?

It's the router's plan for running one client operation across subgraphs: which subgraphs to call, in what order, which calls can run in parallel and which depend on others (for example, fetching `weight` before calling the shipping subgraph). The router builds it from the supergraph schema and caches it per operation. You can view query plans in Apollo Sandbox or router logs, which helps when a query is slow because it needs many sequential fetches.

### 340: What changed between Federation 1 and Federation 2?

Federation 2 made sharing types between subgraphs much easier. Value types and fields can be shared with `@shareable` instead of special rules, `extend type` and `@key` on the "owning" subgraph aren't needed anymore, composition gives better error messages, and new directives like `@override`, `@inaccessible`, `@tag` and `@interfaceObject` were added. Subgraphs opt in with `extend schema @link(url: "https://specs.apollo.dev/federation/v2.x")`. New projects should always use Federation 2.

### 341: What are composition errors, and how do you avoid them?

Composition fails when subgraph schemas don't fit together. Examples: two subgraphs define the same non-shareable field, a field has different types in different subgraphs, an `@external` field doesn't exist anywhere, or a query path can't be satisfied by any subgraph. Run composition checks in CI for every subgraph change (`rover subgraph check` or `hive schema:check`) against the current production schemas, so errors are caught before deploy instead of breaking the router.

### 342: What is the difference between Apollo Router and Apollo Gateway?

Apollo Gateway (`@apollo/gateway`) is the older router, written in Node.js and run inside Apollo Server. Apollo Router (also called GraphOS Router) is written in Rust, runs as its own binary or container, and is much faster with lower memory use. It's configured with YAML and extended with Rhai scripts or external coprocessors. Apollo recommends the Router for new setups, and the Gateway is in maintenance.

### 343: What alternatives are there to Apollo's federation tools?

- **GraphQL Hive** from The Guild: schema registry and Hive Gateway, open source, supports the Apollo Federation spec.
- **WunderGraph Cosmo**: open source router and registry, also federation compatible.
- **Grafbase Gateway**: a Rust gateway with federation support.
- **GraphQL Mesh**: combines GraphQL, REST, gRPC and other sources into one schema.
- **Schema stitching** with `@graphql-tools/stitch`.

Most of these implement the Apollo Federation directives, so subgraphs can usually be moved between them.

### 344: How does schema stitching compare to Federation?

In stitching, the gateway owns the logic for merging schemas: you configure in the gateway how types from different services relate. In Federation, subgraphs declare the relations themselves with directives, and the gateway is generic. Federation fits better when many teams own their own services, because no one team has to maintain gateway configuration. Stitching is more flexible for combining services you don't control, like third-party GraphQL APIs that can't add directives.

### 345: What is the GraphQL Composite Schemas specification?

It's a spec being developed by a GraphQL Foundation working group, with people from Apollo, The Guild, ChilliCream, WunderGraph, Grafbase and others. The goal is a vendor-neutral standard for building one schema out of many source schemas, based on what was learned from Federation, stitching and similar tools. It's still in progress, so production systems today use Apollo Federation directives, but it's worth knowing about as the likely future standard.

### 346: How do you decide where to split subgraphs?

Split by domain and team ownership, not by database table. Each subgraph should own a coherent area, like accounts, catalog, orders or reviews, and be owned by the team that knows that area. Avoid splits where almost every query needs data from many subgraphs in sequence, because each hop adds latency. Start with fewer, larger subgraphs and split when a team or domain clearly needs independence.

### 347: How does the router fetch entities from a subgraph?

It calls the special `_entities` root field on the subgraph, passing all the representations it needs in one request.

```graphql
query ($representations: [_Any!]!) {
  _entities(representations: $representations) {
    ... on User {
      name
    }
  }
}
```

```json
{
  "representations": [
    { "__typename": "User", "id": "1" },
    { "__typename": "User", "id": "2" }
  ]
}
```

So at the router level, entity loading is batched. Inside the subgraph, `__resolveReference` runs once per representation, so you need a DataLoader to turn that into one database query.

### 348: How do you trace a request across a router and its subgraphs?

Use distributed tracing with OpenTelemetry. The router creates a trace for the client request, starts a span for each subgraph fetch and passes the trace context in headers (W3C `traceparent`). Each subgraph continues the trace with its own spans for parsing, execution and resolvers. In a tool like Jaeger, Tempo or Datadog you then see the whole request: query planning, each subgraph call, and the slow resolver inside one subgraph.

### 349: How do subscriptions work with Federation?

Apollo Router supports subscriptions in its GraphOS (enterprise) version. The client subscribes through the router, the router subscribes to the subgraph that owns the subscription field, and for each event it can fetch extra fields from other subgraphs using entity resolution. The router can talk to subgraphs over WebSockets or with HTTP callbacks. Since every event can trigger subgraph fetches, keep event payloads rich enough to avoid many extra calls.

### 350: How do you scale GraphQL subscriptions?

- Use a shared pub/sub broker (Redis, Kafka, NATS) so any server instance can deliver any event.
- Plan for many open connections: tune file descriptor limits and memory per connection.
- Load balancers must support WebSockets or long-lived SSE, and you may need sticky sessions for some setups.
- Publish to fine-grained topics (per room or per user) instead of filtering every event on every server.
- Consider moving subscriptions to a separate service, so long-lived connections don't affect the normal HTTP API.
- Handle reconnects: clients should resubscribe and refetch to catch up on missed events.

### 351: What happens when a subscription produces events faster than a client can receive them?

Events pile up in server memory, in the socket buffer or in the client, and a slow client can make the server run out of memory. Ways to deal with it: throttle or debounce events per subscription (for example, send a price at most once per second), merge several events into one, drop old events when only the latest value matters, set a maximum buffer size and close the connection when it's exceeded, and watch the `bufferedAmount` of the socket. For very high-volume data, a subscription that says "something changed" followed by a normal query is often better than pushing full payloads.

### 352: How do you handle an access token that expires during a long WebSocket connection?

The token was checked only on connect, so an hour later the socket is still open with an expired token. Options: store the token's expiry in the connection context and close the socket (with a code like `4401` or `4403`) when it expires, so the client reconnects with a fresh token; check permissions on each event in the subscription resolver, not just once; and on the client, make `connectionParams` a function so reconnects always use the current token. Also close sockets when a user logs out or their permissions change.

### 353: How does `@defer` work on the wire?

The server sends the response in several parts, usually as a `multipart/mixed` HTTP response or over SSE. The first part has the data that isn't deferred and `hasNext: true`. Later parts carry the deferred data with information about where it belongs (a path, or an ID that points to a pending entry announced earlier), and the last part has `hasNext: false`. The payload format changed between versions of the RFC: graphql-js 17 uses `pending`, `incremental` and `completed` entries, while older implementations used a `path`-based format. The client and server must agree on the format, which is why clients like Apollo send an `Accept` header with the spec version they support.

### 354: When is `@defer` worth using, and when is it not?

It helps when a page has a fast main part and slow secondary parts, like a product page where reviews or recommendations come from a slow service. It's not worth it when all the data is fast anyway, because incremental responses add overhead, complicate caching and make clients handle partial states. It also doesn't make the slow part faster: the total time stays the same, only the first paint is earlier. Measure first, and use it for the few fields that really hold up the page.

### 355: How do you invalidate a server-side response cache correctly?

Time-based expiry is the simplest: set a short `maxAge` and accept slightly stale data. For more precision, tag each cached response with the entities it contains (like `Product:42`), and when a mutation changes `Product:42`, purge all responses with that tag. GraphQL Yoga's response cache does this automatically from the types and IDs in responses. CDNs like Fastly and Cloudflare support tag-based purging with surrogate keys. Changes made outside GraphQL, like a background job updating prices, must also trigger purges, which is the part teams most often forget.

### 356: What can go wrong when caching GraphQL responses in a CDN?

The worst case is caching a response with private data and serving it to other users. This happens when a query mixes public and private fields but the cache policy is computed wrong, when the cache key ignores the `Authorization` header or cookies, or when a resolver reads the user from context without marking the hint as `PRIVATE`. Other problems are caching error responses, caching different locales under one key and serving stale data after a deploy that changed the schema. Only cache operations you've checked, keep private data uncacheable at the CDN, and include anything that changes the result in the cache key.

### 357: Why does Apollo Client sometimes warn "Cache data may be lost when replacing the field"?

You get it when a field holds objects that can't be normalized (no `id`, or no `keyFields`) and a new response replaces them. Apollo doesn't know whether the old and new objects are the same, so it overwrites them, and fields only the old query asked for are lost. Fix it by adding IDs to the objects, by setting `keyFields`, or by writing a `merge` function for the field. If the objects really belong to the parent, `merge: true` tells Apollo to merge them as one object.

```js
const cache = new InMemoryCache({
  typePolicies: {
    Book: { fields: { author: { merge: true } } },
  },
});
```

### 358: What is a cache redirect in Apollo Client?

When a list query already loaded an object, a detail query for the same object would still go to the network, because Apollo doesn't know that `book(id: "5")` points to `Book:5`. A `read` function can tell it, so the detail view shows the cached data right away.

```js
const cache = new InMemoryCache({
  typePolicies: {
    Query: {
      fields: {
        book: {
          read(_, { args, toReference }) {
            return toReference({ __typename: "Book", id: args.id });
          },
        },
      },
    },
  },
});
```

If the cached object doesn't have all the fields the detail query needs, Apollo still goes to the network for the rest.

### 359: What problems come up with paginated lists in a normalized cache?

- Without the right `keyArgs`, lists with different filters overwrite each other, or each page is stored as a separate list.
- Without a `merge` function, `fetchMore` replaces the list instead of appending.
- A new item created by a mutation doesn't appear in any list until you update the cache by hand, because Apollo can't know which lists it belongs to or where.
- Deleted items stay in lists until you evict them.
- Offset pagination plus inserts gives duplicates, so merge functions should dedupe by reference.

Use `relayStylePagination` or `offsetLimitPagination` with explicit `keyArgs`, and write `update` functions for mutations that change list membership.

### 360: What can go wrong with optimistic updates when several mutations run at once?

Apollo keeps each optimistic response as a separate layer on top of the cache and removes it when that mutation finishes. With several mutations on the same object, like toggling a like quickly three times, responses can arrive out of order, and the UI can flicker as layers are removed and real results applied. Mutations that depend on the current value, like `count + 1`, can also produce wrong optimistic values. Make mutations set absolute values (`setLiked(true)`) instead of toggles, disable the button while a mutation is running, or queue mutations for the same object.

### 361: How do you keep the Apollo Client cache from growing forever?

In long-running single-page apps, every query adds objects, and nothing is removed by default. Evict data you don't need anymore with `cache.evict` and run `cache.gc()` to remove objects that are no longer reachable from any root. Clear the cache on logout. Avoid putting large, rarely reused data in the cache (use `no-cache` for it). Apollo Client also has limits on its internal memoization caches, which you can tune if needed.

### 362: What does it mean to design a schema from the client's needs?

It means starting from what the screens and use cases need and shaping types around that, instead of copying database tables into types. For example, a `User` type might have `displayName` and `avatarUrl(size:)` even though the database has `first_name`, `last_name` and `avatar_key`. The schema becomes a stable product interface that can outlive the database design. It doesn't mean one field per screen, though: types should still model the domain so they can be reused across screens.

### 363: What are the trade-offs of generating a GraphQL API directly from a database?

Tools like Hasura, PostGraphile and Supabase's `pg_graphql` give you a full API with filtering, pagination and subscriptions in minutes. The downside is that the schema mirrors your tables, so changing the database changes the API, and business rules have to live in database permissions, views, functions or extra services. It works well for internal tools, prototypes and data-heavy apps. For a long-lived public API, a hand-designed schema is usually easier to keep stable.

### 364: How do you model a state machine, like order status, in a schema?

Expose the state as an enum, and expose transitions as specific mutations instead of letting clients set the status directly.

```graphql
enum OrderStatus {
  DRAFT
  PLACED
  PAID
  SHIPPED
  DELIVERED
  CANCELLED
}

type Order {
  id: ID!
  status: OrderStatus!
  availableActions: [OrderAction!]!
}

enum OrderAction {
  PAY
  CANCEL
  SHIP
}

type Mutation {
  payOrder(input: PayOrderInput!): PayOrderPayload!
  cancelOrder(input: CancelOrderInput!): CancelOrderPayload!
  shipOrder(input: ShipOrderInput!): ShipOrderPayload!
}
```

The server checks that the transition is allowed from the current state. A field like `availableActions` lets the UI show only valid buttons without copying the rules to the client.

### 365: How do you handle cursor pagination when new items keep being added?

With a cursor based on a stable sort key, like `(createdAt, id)`, new items added at the top don't shift the pages a user is reading, so there are no duplicates or skipped items while scrolling down. To show new items, the client either refetches the first page, queries with `before` the first cursor it has, or gets them through a subscription and adds them to the top of the cached list. Avoid sorting by values that change often, like a score, because items move between pages while the user pages.

### 366: How do you implement backward pagination with `last` and `before`?

Reverse the sort, fetch `last + 1` rows before the cursor, then reverse the result back into normal order.

```js
async function productsBackward({ last, before }, sql) {
  const beforeId = decodeCursor(before);
  const rows = await sql`
    SELECT * FROM products
    WHERE id < ${beforeId}
    ORDER BY id DESC
    LIMIT ${last + 1}
  `;
  const hasPreviousPage = rows.length > last;
  const nodes = rows.slice(0, last).reverse();

  return {
    edges: nodes.map((node) => ({ node, cursor: encodeCursor(node.id) })),
    pageInfo: {
      hasPreviousPage,
      hasNextPage: true,
      startCursor: nodes.length ? encodeCursor(nodes[0].id) : null,
      endCursor: nodes.length ? encodeCursor(nodes.at(-1).id) : null,
    },
  };
}
```

The Relay spec discourages using `first` and `last` together, and many servers reject it.

### 367: How do you paginate by a column that isn't unique?

Add a unique tie-breaker, usually the primary key, to both the sort and the cursor. Otherwise rows with the same value can be skipped or repeated across pages.

```sql
SELECT * FROM products
WHERE (price, id) > ($1, $2)
ORDER BY price, id
LIMIT 21;
```

The cursor encodes both values, like `{"price":"19.99","id":42}`. Add a composite index on `(price, id)` so the query stays fast on later pages.

### 368: How would you design global IDs so they can change later?

Make them opaque and include a type and maybe a version, like `base64("v1:Product:42")`. Clients must treat them as plain strings. Because the format is hidden, you can change the encoding later, for example when moving to UUIDs, as long as the server still accepts old IDs that clients have saved. Shopify, for example, uses readable IDs like `gid://shopify/Product/123`. Readable is fine too, as long as you document that clients must not parse them.

### 369: How do you model polymorphic data that's stored in one database table?

Use an interface for the shared fields and one object type per kind, and pick the type in `__resolveType` from a discriminator column.

```graphql
interface Notification {
  id: ID!
  createdAt: DateTime!
  read: Boolean!
}

type CommentNotification implements Notification {
  id: ID!
  createdAt: DateTime!
  read: Boolean!
  comment: Comment!
}

type FollowNotification implements Notification {
  id: ID!
  createdAt: DateTime!
  read: Boolean!
  follower: User!
}
```

```js
const resolvers = {
  Notification: {
    __resolveType: (row) =>
      ({ comment: "CommentNotification", follow: "FollowNotification" })[
        row.kind
      ],
  },
};
```

Clients that don't know a new notification type can still show the shared fields through the interface.

### 370: How do you expose different parts of a schema to different audiences?

Keep one schema and filter it per audience. In Apollo Federation you tag elements with `@tag(name: "public")` and create contracts, which are filtered variants of the supergraph that include or exclude tags. `@inaccessible` hides a field from the public API while still letting the router use it internally. Without federation, you can build filtered schemas with `filterSchema` from `@graphql-tools/utils` and serve each on its own endpoint. This beats maintaining two separate schemas that slowly drift apart.

### 371: How do you collect field usage data, and what do you use it for?

The server records which fields each operation uses, grouped by client name and version. Apollo's usage reporting plugin and Hive's client do this by sending operation signatures and per-field counts to their registries. You use the data to know when a deprecated field can be removed, to block schema changes that would break active clients, to find fields nobody uses and to focus performance work on hot fields. You can also compute it yourself by walking each operation's AST with `TypeInfo` and counting `Type.field` pairs.

### 372: How do you manage a GraphQL schema across many teams?

- Define ownership: each type or subgraph has a clear owning team.
- Publish design guidelines (naming, pagination, errors, nullability) and enforce what you can with linting.
- Run schema checks in CI against production usage, so breaking changes are blocked automatically.
- Use a schema registry as the single source of truth.
- Review new types and big changes in a lightweight design review, with someone who sees the whole graph.
- Use deprecation with dates, and track usage before removing anything.

### 373: How would you set up code generation in a monorepo with a GraphQL server and several clients?

Have the server generate and commit its schema file (or publish it to a registry) as part of its build. Each client runs codegen against that schema with its own documents, producing typed operations. Server resolvers get their own generated types from the same schema. In CI, regenerate everything and fail if the result differs from what's committed, and validate every client's operations against the new schema, so a server change that breaks a client fails before merge. Tools like Turborepo or Nx can run codegen only for packages affected by a change.

### 374: What does a schema-first design process look like for a new feature?

1. Front-end and back-end developers write the schema changes together, based on the UI designs.
2. The proposal goes through a design review, often as a pull request with just SDL.
3. Once agreed, the back end implements resolvers, while the front end builds against mocked data from the schema.
4. Both meet at the schema, which was agreed in advance, so integration is usually small.

This takes some time up front but avoids building the wrong API and changing it later.

### 375: How do you find what's slow inside a Node.js GraphQL server?

First, look at traces to see whether time is spent in resolvers waiting for I/O or in CPU work. For I/O, the fix is usually batching, caching or better queries. For CPU, take a CPU profile with `node --cpu-prof` or Clinic.js Flame under realistic load, and look at the flame graph. Common hotspots are validation of huge documents, resolver middleware wrapping every field, creating many promises for large lists, JSON serialization of big responses and expensive custom scalars or logging.

### 376: How do you benchmark a GraphQL server?

Use a load testing tool like k6, autocannon or Gatling with real operations taken from production logs, not just a trivial query. Include a realistic mix of queries and variables, run against a production-like database with realistic data sizes, and measure latency percentiles (p50, p95, p99), throughput and error rate. Warm up first, so caches and JIT compilation settle. Compare one change at a time, like adding a DataLoader or switching executors, and watch database load too, since the server is rarely the bottleneck alone.

### 377: How does DataLoader decide when to run a batch?

When you call `load()` for the first time, DataLoader schedules the batch to run after the current work finishes. In Node.js it uses `process.nextTick` after waiting for pending promise callbacks, so all the `load()` calls made by resolvers at the same level of the query get into the same batch. Calls made after an `await` that hits real I/O end up in a later batch. That's why loaders work best when resolvers call `load()` directly instead of after other awaits. You can change the timing with the `batchScheduleFn` option, for example to wait a few milliseconds and collect bigger batches.

### 378: How do you use DataLoader with composite keys?

Use objects as keys and give DataLoader a `cacheKeyFn` that turns them into strings, because by default it compares keys by reference.

```js
const priceLoader = new DataLoader(
  async (keys) => {
    const rows = await db.prices.findMany(keys); // [{ productId, region, amount }]
    const map = new Map(rows.map((r) => [`${r.productId}:${r.region}`, r]));
    return keys.map((k) => map.get(`${k.productId}:${k.region}`) ?? null);
  },
  { cacheKeyFn: (k) => `${k.productId}:${k.region}` },
);

priceLoader.load({ productId: "1", region: "EU" });
```

Loaders can also be created per argument combination, like one loader per `region`, if the set of combinations is small.

### 379: How do you batch a paginated relation, like the first 5 posts of each user?

A plain `IN` query returns all posts of all users, and `LIMIT` applies to the whole result, not per user. In Postgres you can use a window function or a `LATERAL` join to get the top N per parent in one query.

```sql
SELECT * FROM (
  SELECT p.*, ROW_NUMBER() OVER (PARTITION BY author_id ORDER BY created_at DESC) AS rn
  FROM posts p
  WHERE author_id = ANY($1)
) t
WHERE rn <= $2;
```

The loader key must include the page arguments (like `{ authorId, first: 5 }`), and the batch function groups keys with the same arguments. Cursor arguments make it harder, which is one reason nested paginated lists are expensive.

### 380: What should you watch out for when DataLoader batches get very large?

A list of 5,000 items can produce a single `IN` query with 5,000 IDs, which some databases handle badly or reject because of parameter limits. Set `maxBatchSize` so DataLoader splits big batches into several queries. Also watch the memory used by the per-request cache in requests that load a lot of objects, and consider `cache: false` for loaders where reuse within one request is rare.

```js
const userLoader = new DataLoader(batchUsers, { maxBatchSize: 500 });
```

### 381: How do database connection pools interact with GraphQL concurrency?

One GraphQL request can run many resolvers in parallel, and each might take a connection from the pool. A few complex queries can use up the whole pool and make other requests wait, or even deadlock if a resolver holds a connection while waiting for another one. Use DataLoaders to reduce the number of queries, keep transactions short and never hold a connection across resolver boundaries, set a sensible pool size and a timeout for getting a connection, and use cost limits so single requests can't fan out without limit.

### 382: How can `AsyncLocalStorage` help in a GraphQL server?

`AsyncLocalStorage` from `node:async_hooks` keeps a value across all async calls that start from one point, like a request. You can store the request ID, the current user or a logger in it, and deep code like a database wrapper or an HTTP client can read it without passing the context down by hand. It's useful for logging and tracing. For things resolvers need, like loaders and the user, passing them in the GraphQL context is still clearer and easier to test.

```js
import { AsyncLocalStorage } from "node:async_hooks";

export const requestStore = new AsyncLocalStorage();

app.use("/graphql", (req, res, next) => {
  requestStore.run({ requestId: crypto.randomUUID() }, next);
});

export const log = (msg) =>
  console.log(`[${requestStore.getStore()?.requestId}] ${msg}`);
```

### 383: How can Postgres row-level security work together with a GraphQL API?

Row-level security (RLS) makes Postgres itself filter rows by policies, for example "a user can only see rows where `tenant_id` matches". The GraphQL server sets the current user or tenant on the database connection at the start of each request (for example with `SET LOCAL app.user_id = ...` inside a transaction), and every query is filtered automatically. It's a strong safety net against missing checks in resolvers. PostGraphile and Supabase rely on it heavily. The cost is more complex connection handling and policies that are harder to debug than application code.

### 384: What are the trade-offs of running a GraphQL server on serverless functions?

Good: automatic scaling, no servers to manage, and you pay per request. Less good: cold starts, made worse by large schemas and heavy dependencies; per-request caches like DataLoader still work, but in-memory caches across requests don't survive between invocations; database connections need a pooler like RDS Proxy or PgBouncer; and subscriptions don't fit, so you need a separate service such as AWS AppSync or API Gateway WebSockets. Keep the bundle small and build the schema once per container, outside the handler.

### 385: Can you run GraphQL on edge runtimes like Cloudflare Workers?

Yes. Servers built on the Fetch API, like GraphQL Yoga, run on Cloudflare Workers, Vercel Edge Functions and Deno Deploy. It lowers latency for users far from your main region. The problem is that data usually lives in one region, so an edge server that calls a far-away database for every resolver can be slower overall. Edge GraphQL makes the most sense with edge-friendly data (KV stores, read replicas, caches) or as a caching layer in front of the main API.

### 386: How do you reduce the size of GraphQL responses?

- Turn on gzip or Brotli compression, which works very well on repetitive JSON.
- Don't over-fetch on the client: remove unused fields, which lint rules and codegen tools can help find.
- Paginate lists instead of returning everything.
- Avoid returning the same large nested object many times in a list. Return an ID and load details once.
- Use persisted queries to shrink requests.

Response size matters most on mobile, so check the payload sizes of your main screens from time to time.

### 387: How do you make sure client operations stay valid against the server schema?

Validate every client operation against the schema in CI. GraphQL Inspector (`graphql-inspector validate`), graphql-eslint, codegen and the Relay compiler all fail on invalid operations. For the other direction, register client operations (or their usage) in a schema registry, so the server's schema check knows which fields active clients use. Together these act like contract tests: the server can't remove what clients use, and clients can't use what the server doesn't have.

### 388: What is a schema snapshot test, and why use one?

The test prints the schema with `printSchema` and compares it with a committed `schema.graphql` file. When someone changes resolvers or code-first types, the snapshot changes, and the diff shows up in the pull request. Reviewers see the exact API change instead of having to read code, and accidental changes, like a field becoming nullable because of a type change, are easy to spot.

```js
import { printSchema } from "graphql";
import { readFileSync } from "node:fs";

test("schema matches the committed SDL", () => {
  expect(printSchema(schema)).toBe(readFileSync("schema.graphql", "utf8"));
});
```

### 389: How would you migrate an existing REST API to GraphQL?

Do it step by step instead of a big rewrite. Add a GraphQL layer whose resolvers call the existing REST endpoints or services. Start with one screen or feature, preferably one that suffers from many requests or over-fetching. Move clients over one feature at a time, while REST keeps working for everyone else. Later, resolvers can call services or the database directly for better performance. Keep REST for things GraphQL handles badly, like file downloads and webhooks.

### 390: When would you use GraphQL as a backend-for-frontend instead of one company-wide graph?

A BFF is a GraphQL server built for one client app, owned by that app's team, and shaped exactly for its screens. It's quick to change and doesn't need cross-team agreement. A unified graph is one schema for the whole company that all clients share, which avoids duplicated logic but needs governance and usually federation. Small companies or teams with very different clients often start with BFFs. Larger organizations with many clients reusing the same data tend to move toward a unified graph.

### 391: How would you migrate from schema stitching to Federation?

1. Make sure each service's schema is valid on its own and owned by a team.
2. Turn each service into a subgraph: add `@link` to Federation 2, mark entity types with `@key` and add `__resolveReference` resolvers.
3. Replace the stitching configuration, like merged type resolvers, with federation directives.
4. Compose the supergraph and compare its schema with the stitched schema, so clients see no difference.
5. Run the router side by side with the old gateway, mirror or split traffic and compare results.
6. Switch traffic over and remove the stitching gateway.

Hive Gateway can serve both styles, which can make the switch gradual.

### 392: What changes when you upgrade from Apollo Server 4 to Apollo Server 5?

- Apollo Server 5 needs Node.js 20 or newer and `graphql` 16.11 or newer.
- The Express integration moved out of `@apollo/server`. Import `expressMiddleware` from `@as-integrations/express4` or `@as-integrations/express5` instead of `@apollo/server/express4`.
- `startStandaloneServer` no longer uses Express internally. It runs directly on Node's HTTP server.
- Options and APIs deprecated in version 4 were removed.

For most apps, the main work is changing the Express import and checking the Node version. The migration guide lists the smaller changes.

### 393: What are the main changes when moving from Apollo Client 3 to Apollo Client 4?

- React hooks and `ApolloProvider` are imported from `@apollo/client/react`, not from `@apollo/client`.
- You pass a link explicitly, like `new HttpLink({ uri })`, instead of a `uri` option on the client.
- Links are classes (`SetContextLink`, `ErrorLink`, `HttpLink`), and RxJS replaces `zen-observable`, so custom links use RxJS observables.
- Errors were redesigned: `ApolloError` with `graphQLErrors` and `networkError` is gone, and you check error types with classes like `CombinedGraphQLErrors` and `ServerError`.
- TypeScript types for results got stricter, with a `dataState` value that tells you whether data is complete, partial or empty.

Apollo provides a codemod that does most of the import changes automatically.

### 394: How do you migrate from `subscriptions-transport-ws` to `graphql-ws`?

The two libraries use different WebSocket subprotocols (`graphql-ws` for the old library and `graphql-transport-ws` for the new one), so a client and server must use the same one. Since you can't update all clients at once, the server can support both for a while: look at the `Sec-WebSocket-Protocol` header in the handshake and pass the connection to the matching library. Then update clients to `graphql-ws` and `GraphQLWsLink`, watch the traffic on the old protocol, and remove the old server once it's gone. Note that `onConnect`, `connectionParams` and the context function have slightly different signatures in the new library.

### 395: What should you know about upgrading from graphql-js 16 to 17?

Version 17 is the first major release since 2021. It removes APIs that were deprecated in v16 and renames the custom scalar methods: `serialize` becomes `coerceOutputValue`, `parseValue` becomes `coerceInputValue` and `parseLiteral` becomes `coerceInputLiteral`, with the old names kept as deprecated aliases. It adds `AbortSignal` support (resolvers can call `info.getAbortSignal()`), a `hideSuggestions` option, `findSchemaChanges()` for comparing schemas, and experimental features like `@defer` and `@stream` through `experimentalExecuteIncrementally()` and fragment arguments. Since most servers depend on `graphql` as a peer dependency, check that your server library, codegen and other tools support v17 before upgrading. The official v16 to v17 upgrade guide lists every change.

### 396: What is in the September 2025 edition of the GraphQL spec?

It's the first edition since October 2021. The main additions are OneOf input objects (`@oneOf`), schema coordinates (a standard way to refer to schema elements, like `User.email` or `Query.user(id:)`), descriptions on operations and fragments, wider deprecation support, full Unicode support in the language, and clearer wording around execution, errors and request `extensions`. Most of these were already in graphql-js and other implementations before the edition was published.

### 397: What are fragment arguments?

It's a proposal that lets fragments declare their own variables, so the same fragment can be used with different values in one query.

```graphql
fragment UserAvatar($size: Int! = 64) on User {
  avatarUrl(size: $size)
}

query {
  me {
    ...UserAvatar(size: 128)
  }
  friends {
    ...UserAvatar
  }
}
```

Today, every variable must be declared at the operation level, which breaks fragment colocation when a component needs its own argument. Relay solves this with its own `@arguments` and `@argumentDefinitions` directives. graphql-js 17 supports fragment arguments as an experimental feature, but they're not in the spec yet.

### 398: What proposals exist for changing how errors and nullability work?

Many teams mark fields nullable only so errors don't wipe out parents, even though those fields are never null in normal cases. That makes clients write null checks for values that can't really be null. The working group has been exploring fixes: letting clients turn off null propagation for a request (an `onError` behavior, where errored fields are just `null` and the error is listed), and marking fields as "semantically non-null", meaning null only when there's an error. graphql-js 17 has an experimental `@experimental_disableErrorPropagation` directive along these lines. None of this is in the spec yet, but clients like Relay and Apollo already have ways to throw on field errors when reading data.

### 399: How do you handle schema changes when old mobile app versions stay in use for months?

Assume every field a released app uses must keep working for as long as that version is supported. Track usage by client name and version, deprecate instead of removing, and set a minimum supported app version so you can eventually remove old fields. Build apps to handle unknown enum values and union members. Feature flags in the API, like returning new fields that old apps simply ignore, are safer than changing the meaning of existing fields. A forced update screen is the last resort for security problems or truly breaking changes.

### 400: What race conditions can happen between subscription events and mutation responses?

A client sends a mutation, and the server publishes an event to subscribers, including the same client. The event can arrive before the mutation response, so the client might add the same item twice (once from the event and once from the mutation `update`), or apply an older state after a newer one. Fix it by deduplicating by ID when adding items, making cache updates idempotent (with a normalized cache, writing the same object twice is harmless), including a version or `updatedAt` value and ignoring older data, and sometimes filtering out events caused by the client's own mutations.

### 401: A list screen in the mobile app takes 4 seconds to load. How would you investigate?

1. Find the operation behind the screen and look at its traces in production, not just locally.
2. Check whether the time is on the server or the client. Big payloads on a slow network or slow JSON parsing on old phones are common.
3. On the server, look at resolver timings. A list with a slow per-item field (N+1, or a call to another service per item) is the usual cause.
4. Check the page size. The app may ask for 200 items when the screen shows 15.
5. Check for request waterfalls: does the screen fire several queries one after another?
6. Fix the biggest problem first. Typical fixes are a DataLoader, a smaller page size with infinite scroll, removing unused fields, or deferring a slow field.

### 402: One query brought the production API down. What do you do now and later?

Right now: find the operation in logs (by operation name, client and query hash), block it at the gateway or with a quick validation rule, and scale up or restart the affected services. Then find out whether it was a real client doing something unexpected or an attacker. Later: add cost analysis and depth limits, cap page sizes, add timeouts, move first-party clients to trusted documents, and add alerts on query cost and resolver latency so you catch it earlier next time. Write a short postmortem so the fixes actually happen.

### 403: A client reports that a field is `null` and the response has errors. How do you debug it?

Read the `errors` array first: the `path` tells you which field failed, and the `message` and `extensions.code` say why. If the message is masked, use the request ID or trace ID to find the full error in server logs. Check whether the null is the field itself or a parent that got nulled by propagation from a non-null child. Then reproduce it with the same operation, variables and user, because permission-based errors often only happen for some users. Common causes are a downstream service failing, a resolver returning `undefined` for a non-null field, and data in the database that doesn't match the schema, like a missing required value.

### 404: Design a GraphQL schema for a shopping cart.

```graphql
type Cart {
  id: ID!
  lines(first: Int = 50, after: String): CartLineConnection!
  totalQuantity: Int!
  cost: CartCost!
  checkoutUrl: String!
}

type CartLine {
  id: ID!
  quantity: Int!
  merchandise: ProductVariant!
  cost: CartLineCost!
}

type CartCost {
  subtotal: Money!
  tax: Money
  total: Money!
}

input CartLineInput {
  variantId: ID!
  quantity: Int!
}

type CartUserError {
  field: [String!]
  message: String!
  code: CartErrorCode!
}

enum CartErrorCode {
  OUT_OF_STOCK
  INVALID_QUANTITY
  VARIANT_NOT_FOUND
}

type CartPayload {
  cart: Cart
  userErrors: [CartUserError!]!
}

type Mutation {
  cartCreate(lines: [CartLineInput!]): CartPayload!
  cartLinesAdd(cartId: ID!, lines: [CartLineInput!]!): CartPayload!
  cartLinesUpdate(cartId: ID!, lines: [CartLineUpdateInput!]!): CartPayload!
  cartLinesRemove(cartId: ID!, lineIds: [ID!]!): CartPayload!
}
```

Every mutation returns the full cart, so the client cache updates in one step. Costs are computed on the server, money uses a `Money` type, and expected problems like "out of stock" are user errors, not exceptions. This is close to how Shopify's Storefront API does it.

### 405: Design a chat feature with GraphQL subscriptions.

```graphql
type Message {
  id: ID!
  room: Room!
  author: User!
  text: String!
  createdAt: DateTime!
}

type Query {
  room(id: ID!): Room
}

type Room {
  id: ID!
  messages(last: Int = 50, before: String): MessageConnection!
}

type Mutation {
  sendMessage(input: SendMessageInput!): SendMessagePayload!
}

type Subscription {
  messageAdded(roomId: ID!): Message!
  typing(roomId: ID!): TypingEvent!
}
```

History loads with a normal paginated query (backward pagination, newest at the bottom). New messages arrive through `messageAdded`, and the client appends them to the cached connection, deduplicating by ID so its own messages aren't added twice. The server checks room membership on subscribe and on each event, publishes to a per-room topic in Redis so it works with many instances, and the client refetches recent messages after a reconnect to fill any gap. `sendMessage` takes a client-generated ID for idempotency and optimistic UI.

### 406: A developer wants to add `ssn` to the `User` type. What do you think about?

First, whether any client really needs it, because the safest sensitive field is one that isn't exposed. If it's needed: restrict it with a strict authorization check in the data layer (only the user themself and specific roles), make it nullable so unauthorized access returns `null`, maybe expose only a masked version (`ssnLast4`), keep it out of logs, traces and error messages, make sure response caching marks it private, and add audit logging when it's read. Also consider putting it in a separate type or query that's only reachable from an admin schema, so it isn't next to fields that many clients query.

### 407: After a mutation, the UI still shows old data. How do you fix it?

Check what the mutation returns. If it returns the changed object with its `id` and all the fields the screen shows, Apollo updates it automatically. Often it returns only `id` or a boolean, so nothing in the cache changes. If the change affects a list (an item added, removed or moved), the cache can't know that on its own, so you need an `update` function or `refetchQueries`. Also check the type has an ID field that Apollo can use, the fetch policy isn't `cache-only` or `standby` on that screen, and the query and mutation ask for the same object with the same key.

### 408: Users see duplicate items in an infinite scroll list. What's going on?

Typical causes: offset pagination while new items are added at the top, so the next page starts with items already shown; a sort on a non-unique column without a tie-breaker; a `merge` function that just concatenates pages without checking for existing references; or `fetchMore` being called twice for the same cursor because of a scroll event firing twice. Fix it by switching to cursor pagination with a unique sort key, deduplicating in the merge function by cache reference, and guarding `fetchMore` while a request is in flight.

### 409: A security review found that users can read other users' orders through `node(id:)`. How do you fix it and prevent it again?

Short term: add the ownership check to the `node` resolver for `Order` and deploy. Real fix: move the check into the code that loads orders (the service or DataLoader), so every path, including `node`, `order(id:)`, nested fields and federation entity resolution, goes through it. Then search for other types with the same problem, since `node` usually covers every type. Add tests that log in as one user and try to read another user's objects through every root field. Also check logs to see if the hole was used.

### 410: Tracing shows 300 database queries for a single request. What do you do?

That's almost always N+1. Look at the trace to find which resolver repeats, usually a field on list items like `Order.customer` or `Product.inventory`. Add a DataLoader for it, created per request in the context, and make the resolver call `loader.load()`. Check the batch function returns results in the same order as the keys. Then check the trace again: 300 queries should become a handful. If the repeated calls are to another service, ask for a batch endpoint, or at least cache within the request.

### 411: You need to rename a type in a public schema. How do you do it?

You can't do it in place, because type names appear in clients' fragments (`... on OldName`), `__typename` checks and cache configuration. The usual way is to add the new type alongside the old one, add new fields that return the new type, deprecate the old fields, and remove the old type when usage is zero. If the old type is returned in unions or interfaces, this takes time and coordination. For internal APIs where you control all clients, you can sometimes do it in one coordinated release instead. Often the honest answer is that a bad name isn't worth the cost of renaming.

### 412: How would you design rate limiting for a public GraphQL API?

Give each API key a budget of points per hour, where each query costs points based on its computed cost (like GitHub's model). Reject queries that cost too much on their own, before running them. Return the current cost, remaining points and reset time in the response `extensions` or headers, and let clients ask for the cost of a query without running it. Add a separate, simpler request-per-second limit at the gateway to stop floods, and stricter per-field limits on sensitive mutations. Document all of it, because clients need to know how to stay under the limits.

### 413: You're starting a new product. How do you decide between REST and GraphQL?

Look at the clients and the data. GraphQL makes sense if there are several clients (web, iOS, Android) with different needs, screens that combine lots of related data, a front-end team that changes UI often, or plans for a public API that third parties will query in many ways. REST, or tRPC for a TypeScript-only stack, makes sense for a single simple client, mostly CRUD data, heavy reliance on HTTP caching, or a team without GraphQL experience on a tight timeline. Team skills matter as much as the technology.

### 414: Five teams want to contribute to one GraphQL API. How do you set it up?

Use Federation (or a similar composition tool) so each team owns a subgraph and deploys on its own schedule. Set up a schema registry with checks in CI that run composition and breaking change detection against production usage. Agree on shared conventions (naming, pagination, errors, IDs) and enforce what you can with linting. Have a small group that reviews schema changes for consistency across the graph. Give each team observability into their own subgraph's performance and errors.

### 415: One subgraph is down. What happens to queries, and how do you make it fail better?

The router still calls the other subgraphs. Fields from the failing subgraph come back as errors, and they become `null` with propagation up to the nearest nullable parent. If those fields or their parents are non-null, much more of the response disappears. Make fields that come from other subgraphs nullable where it makes sense, set timeouts on subgraph calls so a slow subgraph doesn't hold up the whole request, and use the router's retry settings carefully. Clients should use an error policy that shows partial data.

### 416: All GraphQL traffic is `POST /graphql` with status 200. What problems does this cause with API gateways and WAFs, and how do you deal with it?

URL- and status-based tools can't tell operations apart: rate limits, caching rules, dashboards and alerts all see one endpoint. WAFs may also flag GraphQL bodies as suspicious, or miss attacks hidden in queries. Fixes: put the operation name in the URL or a header (some clients add `?op=GetUser`) so gateways can route and measure by operation, use GraphQL-aware gateways or plugins for limits, return real HTTP status codes using the `application/graphql-response+json` media type, and move monitoring from status codes to GraphQL error metrics.

### 417: The front-end team says the schema is hard to use. How do you approach it?

Ask for concrete examples: which screens need too many queries, which fields have confusing names, where they have to transform data a lot, which nullability forces pointless checks. Often the schema mirrors the database instead of the domain, mutations don't return what the UI needs, or lists lack the filters the UI uses. Fix the worst cases by adding better fields and deprecating the old ones, and change the process so front-end developers take part in schema design from the start.

### 418: How do you model a mutation that takes minutes to finish, like generating a report?

Don't keep the HTTP request open. Return a job object right away and let the client follow its progress.

```graphql
type ReportJob {
  id: ID!
  status: JobStatus!
  progress: Float
  result: Report
  error: String
}

enum JobStatus {
  QUEUED
  RUNNING
  SUCCEEDED
  FAILED
}

type Mutation {
  generateReport(input: GenerateReportInput!): ReportJob!
}

type Query {
  reportJob(id: ID!): ReportJob
}

type Subscription {
  reportJobUpdated(id: ID!): ReportJob!
}
```

The mutation puts the work on a queue, and the client polls `reportJob` or subscribes to updates. Because `ReportJob` has an ID, Apollo's cache updates the status everywhere it's shown.

### 419: A user wants to export 2 million rows as CSV. Should that go through GraphQL?

Usually not as a GraphQL response. A response that big uses a lot of memory on the server, blocks the event loop while it's serialized, and is the wrong format anyway. Use GraphQL to start the export (a job-style mutation), generate the file in a background worker by streaming rows from the database, store it in object storage, and return a signed download URL when it's done. GraphQL stays the control layer, while the bulk data goes through tools made for it.

### 420: A dashboard has 20 widgets, each with its own query. How would you improve it?

20 queries on load means 20 requests, 20 rounds of auth and parsing, and often repeated data. Options: combine the widgets' fragments into one dashboard query, so one request loads everything (with `errorPolicy: 'all'` and nullable widget fields, so one failing widget doesn't break the rest); `@defer` the slow widgets; cache stable widgets longer with a better fetch policy; and lazy load widgets below the fold. If widgets update on their own schedule, keep separate queries for those but load them in parallel, not one after another.

### 421: Subscription clients connect fine but never receive events. How do you debug it?

1. Check the event is published at all: log in the mutation where `publish` is called.
2. Check topic names match exactly between `publish` and `subscribe`.
3. Check the payload shape: the published object must have a key matching the subscription field name, like `{ messageAdded: message }`, unless you have a `resolve` function.
4. If you run several instances, check you're not using the in-memory PubSub, since events published on one instance never reach another.
5. Check `withFilter` conditions, like comparing a number ID to a string ID.
6. Check the client and server use the same protocol (`graphql-ws` versus the old `subscriptions-transport-ws`), and look at the WebSocket frames in browser dev tools.

### 422: With Apollo Client and SSR, the page renders, then flickers and refetches on the client. Why?

The data loaded on the server isn't reaching the client cache, so the client starts empty and refetches. Possible causes: the server cache isn't serialized into the page, or it's restored after the client has already queried; the client uses a `network-only` or `cache-and-network` policy on first render; variables differ between server and client (like a date computed with `new Date()` or a different locale); or one Apollo Client instance is shared between server requests, so the data doesn't match. With Next.js App Router, using `@apollo/client-integration-nextjs` handles the data transfer for you.

### 423: What would you check in a code review of a schema change?

- Is it a breaking change? Did the schema check pass against real usage?
- Do names follow the conventions and describe the domain, not the database?
- Is nullability chosen on purpose for each field?
- Do new lists have pagination and a max page size?
- Do mutations have input and payload types, and return what clients need for cache updates?
- Are expected errors modeled, and are descriptions written?
- Are there authorization concerns for new fields?
- Could the new fields be expensive, and are cost hints set?

### 424: What would you check in a code review of resolvers?

- Any N+1: per-item database or HTTP calls without a DataLoader.
- Authorization done in the right layer, covering all paths to the data.
- Business logic in services, not stuffed into resolvers.
- Errors: expected ones returned as data, unexpected ones not leaking details.
- Input validated and page sizes limited.
- No shared state between requests (loaders and caches created per request).
- Timeouts on calls to other services.
- Tests for both success and permission-denied cases.

### 425: What mistakes do teams commonly make when adopting GraphQL?

- Exposing the database schema one-to-one instead of designing for clients.
- Ignoring N+1 until production is slow.
- No limits on depth, cost or page size.
- Authorization checks scattered in resolvers, missing on some paths.
- Making everything non-null, so one error wipes out whole pages.
- Huge generic mutations like `updateUser(data: JSON)`.
- Treating GraphQL as a reason to drop HTTP caching without a replacement plan.
- No schema registry or breaking change checks, so clients break silently.

### 426: How would you explain GraphQL to a back-end developer who knows REST well?

Think of it as one endpoint where the client sends a description of the data it wants, and the server answers with exactly that shape. Instead of designing endpoints, you design a typed schema of your domain, and instead of controllers you write small functions, called resolvers, for each field. The client decides how much to fetch. You decide what's possible, what's allowed and what it costs. Auth, validation, databases and services stay the same. GraphQL only changes the layer between the client and your code.

### 427: Design the schema for a multi-step checkout.

Keep one `Checkout` object that the client changes step by step, and let the server validate each step and report what's still missing.

```graphql
type Checkout {
  id: ID!
  lines: [CheckoutLine!]!
  email: String
  shippingAddress: Address
  availableShippingRates: [ShippingRate!]!
  selectedShippingRate: ShippingRate
  cost: CheckoutCost!
  readyToComplete: Boolean!
  missingInfo: [CheckoutRequirement!]!
}

enum CheckoutRequirement {
  EMAIL
  SHIPPING_ADDRESS
  SHIPPING_RATE
  PAYMENT
}

type Mutation {
  checkoutSetEmail(id: ID!, email: String!): CheckoutPayload!
  checkoutSetShippingAddress(id: ID!, address: AddressInput!): CheckoutPayload!
  checkoutSelectShippingRate(id: ID!, rateId: ID!): CheckoutPayload!
  checkoutComplete(
    id: ID!
    payment: PaymentInput!
    idempotencyKey: ID!
  ): CheckoutCompletePayload!
}
```

Each mutation returns the updated checkout with user errors. `availableShippingRates` depends on the address, so it updates automatically after that step. `checkoutComplete` requires an idempotency key because it charges money.

### 428: How would you implement profile picture uploads end to end?

1. The client calls `createAvatarUpload(contentType: "image/png", size: 123456)`.
2. The server checks the type and size limits and returns a presigned upload URL plus a file key.
3. The client uploads the file directly to object storage with that URL.
4. The client calls `setAvatar(fileKey: "...")`.
5. The server checks the file exists and belongs to this user, starts image processing (resizing, removing metadata) and saves it on the user.
6. The mutation returns the user with the new `avatarUrl(size:)`, and the cache updates the avatar everywhere.

This keeps big files away from the GraphQL server and avoids multipart and CSRF problems.

### 429: A query is fast for most users but very slow for admins. What might cause it?

Admins often see much more data: all tenants, all orders, no filters, so lists are larger and permissions don't cut them down. Permission checks can also be slow: a check that queries the database per item, which only runs fully for admins who pass the first check. Admin-only fields may call slow internal services. Look at traces for an admin request, check list sizes and look for per-item permission queries. Batch permission checks the same way you batch data loading.

### 430: Memory usage of the GraphQL server grows until it crashes. Where do you look?

Common GraphQL-related causes:

- A DataLoader or cache created once at module level instead of per request, so it keeps every object ever loaded.
- Subscription iterators or PubSub listeners that aren't cleaned up when clients disconnect.
- An unbounded in-memory cache of documents, responses or query plans.
- Very large responses built in memory.
- Context objects kept alive by closures stored somewhere global.

Take heap snapshots a few minutes apart under load and compare which objects grow. Retainer paths usually point straight to the module-level cache or listener list.

### 431: The web app and the mobile app need different shapes of the same data. What do you do?

Usually nothing special: that's what GraphQL is for. Each client queries the fields it needs, and arguments like `avatarUrl(size:)` cover formatting differences. If the needs really diverge, like mobile needing a pre-computed summary for battery or network reasons, add fields that serve that use case, as long as they make sense in the domain. Avoid client-specific types like `MobileUser`. If one client's needs are very different, a separate BFF for that client may be cleaner than bending the shared schema.

### 432: How do you change a field from `String` to an enum without breaking clients?

Changing the type in place is breaking. Add a new field with the enum type, like `statusCode: OrderStatus!`, next to the old `status: String!`, deprecate the old one, and remove it when no one uses it. Before you do that, check the existing data: the string field may contain values that don't fit the enum, and the server must map or clean them, or the new field will throw errors. Plan for future values too, since clients must handle enum values they don't know.

### 433: You want to make a field non-null, but old records in the database have `null` there. What do you do?

Making an output field non-null is safe for the schema, but if any record still has `null`, those queries will now fail with an error that propagates up. First fix the data: backfill old records with a sensible value or compute one in the resolver. Add a database constraint so new nulls can't appear. Then deploy the schema change, and watch error rates for that field. If you can't fix all the data, keep the field nullable and document when it's null.

### 434: A partner company wants access to your GraphQL API. What do you set up?

- API keys or OAuth client credentials, with scopes that limit what each partner can read or change.
- A schema variant or contract that only exposes partner-facing types and fields.
- Cost-based rate limits per key, and reporting so partners can see their usage.
- Documentation, example queries and a changelog with a deprecation policy.
- Monitoring per partner, so one partner's traffic can't hurt others, and you can contact them about deprecated fields.
- A clear commitment about stability, since you can't update partner code yourself.

### 435: How do you add audit logging for mutations?

Log in the service layer, where the business action happens, not only in a GraphQL plugin, so actions from other entry points are logged too. Record who did it (user, impersonator, API key), what they did (action name, target object IDs), when, from where (IP, client name) and the result. Store a filtered version of the input, without passwords and secrets. A GraphQL plugin that logs the operation name, the user and the request ID is still useful as a second layer and for connecting audit entries to traces.

### 436: How do you handle soft-deleted records in a GraphQL API?

By default, don't show them: filter `deleted_at IS NULL` in the data layer, so every resolver and loader gets it for free. For admin tools, add an explicit argument like `includeDeleted: Boolean = false`, with an authorization check, or a separate admin query. Think about references too: if a post's author was soft-deleted, `post.author` should probably return `null` or a placeholder "Deleted user" object instead of failing, so make that field nullable or model the case in the schema.

### 437: The design needs page numbers, but you use cursor pagination. What can you do?

Options: add offset arguments alongside cursors for that list (fine for small datasets or admin tables), return a list of page cursors (some APIs return the cursor for each page so the UI can jump), or change the UI to "load more" or next/previous buttons, which work well with cursors. You can also encode the offset in the cursor itself, which keeps the Relay connection shape while allowing jumps. Be honest about the cost: deep offsets on large tables are slow, so put a limit on how far users can jump.

### 438: The app sends 200 GraphQL queries at startup. How do you fix it?

Find out why. Usually each small component runs its own query on mount, or a list renders items that each query their own details. Fix it with fragment colocation, so the page builds one query out of child fragments, and by loading details as part of the list query instead of per item. Deduplicate identical queries (Apollo does this by default if the queries and variables really match). Load data needed later lazily. Batching can reduce the number of HTTP requests, but it hides the real problem rather than fixing it.

### 439: Error rates spike right after a deploy that changed the schema. What do you do?

Roll back first, then investigate. Check which operations started failing and with what error codes. Validation errors (`GRAPHQL_VALIDATION_FAILED`) mean the schema change broke existing queries, maybe a field was removed or renamed, or an argument became required. Execution errors on non-null fields mean the new resolver returns nulls. Then find out why CI didn't catch it: maybe the schema check didn't have usage data from that client, or the change looked safe but wasn't (like a new enum value an old app crashes on). Fix the process, not just the field.

### 440: The iOS app crashes because a field the client thought was non-null returned `null`. How do you prevent this?

The client's types must come from the real schema, through codegen, not from hand-written models that assume fields always exist. On the server, don't change a field from non-null to nullable, since that's a breaking change, and schema checks should block it. If a field is nullable in the schema, the client must handle `null`, even if it's rare. Partial responses with errors are another source: if the client reads `data` while ignoring `errors`, it may see `null`s it didn't expect, so handle errors explicitly.

### 441: After adding a federation router, response times went up. Where would you look?

Look at query plans for the slow operations. Sequential fetches across subgraphs (fetch user, then orders, then products) add a network round trip each. Check whether entity fetches are batched and whether `__resolveReference` uses DataLoaders inside subgraphs. Check the network between the router and subgraphs: different regions or a missing keep-alive add a lot. Make sure query plans are cached and not rebuilt on every request. Fixes include `@provides` to avoid extra hops, moving fields to the subgraph that already has the data, and colocating the router and subgraphs.

### 442: Thousands of people are viewing a product page and you need to show live stock levels. How would you do it?

Pushing a GraphQL subscription per viewer means thousands of connections and lots of work on every stock change. Options, from simplest: poll stock every 10 to 30 seconds with a tiny cached query (a CDN or response cache can serve all viewers from one cached result); use one subscription topic per product and send only the stock number, not the full product; or put a dedicated real-time service (or SSE through a CDN that supports it) in front for the hot products. Throttle updates, since nobody needs to see every single change, and always recheck stock when someone adds to cart.

### 443: How would you expose feature flags through GraphQL?

Add a field on `Query` or `viewer` that returns the flags relevant to the current user, evaluated on the server.

```graphql
type Query {
  featureFlags: FeatureFlags!
}

type FeatureFlags {
  newCheckout: Boolean!
  recommendationsV2: Boolean!
}
```

Using typed fields instead of a `JSON` blob gives clients types and lets you deprecate flags cleanly. For fields that only exist behind a flag, return `null` or hide them per user rather than changing the schema per user, since the schema must be the same for everyone. Some teams use a generic `isEnabled(flag: String!): Boolean!` field instead for flexibility.

### 444: For a new public API, would you use error unions or a `userErrors` list in mutation payloads?

Both work, and the most important thing is to pick one and use it everywhere. A `userErrors: [UserError!]!` list is simple, handles several validation errors at once (like a form with three invalid fields) and is familiar to people who know the Shopify API. Error unions make each error type explicit with its own fields and force clients to handle each case, but they're more verbose and adding a new member to a union can surprise clients. For form-like mutations, `userErrors` is usually more practical. For queries where "not found" or "no access" are real outcomes, unions work nicely.

### 445: Someone found internal fields like `internalNotes` and `costPrice` through introspection. What do you do?

First check whether those fields are actually protected. Introspection only shows they exist, so the real question is whether a normal user can query their values. If not protected, fix authorization right away. Then reduce what's visible: move internal fields to a separate admin schema or endpoint, use schema filtering or federation contracts with `@inaccessible`, turn off introspection on the public endpoint if it's not a public API, and hide field suggestions. Hiding fields is extra protection on top of authorization, never a replacement for it.

### 446: A developer adds `allUsers: [User!]!` to the schema with no arguments. What feedback do you give?

It works fine with 50 users in development and breaks when there are 500,000 in production: huge responses, slow database queries and an easy target for abuse. Ask for pagination (a connection with `first` and `after` and a max page size), the filters the UI actually needs, and an authorization check, since listing all users is usually an admin-only action. Also ask whether the client really needs all users, or a search field would serve the use case better.

### 447: How do you make a GraphQL API easy for LLM agents to use?

Agents use the schema the way developers do, so a well-designed schema helps a lot. Write clear descriptions on types, fields and arguments, including units, formats and examples. Use specific names and enums instead of free strings. Keep mutations specific (`cancelOrder`) instead of generic. Return helpful error messages that say how to fix the input. Give agents a limited schema or a set of trusted operations instead of the full API, apply the same authorization and cost limits as for any client, and require confirmation for mutations that change important data. The September 2025 spec's descriptions on operations are useful here, since predefined operations can carry their own documentation.

### 448: What are the main strengths and weaknesses of GraphQL?

Strengths: clients get exactly the data they need in one request, a typed schema that serves as documentation and contract, strong tooling (codegen, autocomplete, linting, schema checks), easy schema evolution without versions, and a good fit for combining many back-end services behind one API.

Weaknesses: harder HTTP caching, new performance problems like N+1 and expensive queries that need deliberate protection, authorization that's easy to miss on some paths, more setup and concepts than simple REST, awkward handling of files and binary data, and monitoring that needs GraphQL-aware tools because everything goes to one endpoint.

### 449: What would you include in a GraphQL style guide for your team?

- Naming rules for types, fields, enums, inputs and payloads.
- The pagination standard (connections, max page size).
- How errors work: which ones are thrown with which codes and which are returned as data.
- Nullability guidelines.
- Mutation design: one input, one payload, specific actions, idempotency for risky actions.
- ID format and the `Node` interface.
- Deprecation policy and how long fields stay after deprecation.
- Rules for custom scalars (dates, money).
- Description requirements.
- Security basics: where authorization lives, cost hints, limits.

### 450: Walk through what happens, step by step, when a client sends a query to Apollo Server with DataLoader.

1. The client sends `POST /graphql` with `{ query, variables, operationName }`.
2. The HTTP layer parses the body. Apollo Server's CSRF check confirms the request has a safe content type or header.
3. The context function runs: it reads the auth token, loads the user and creates new DataLoaders for this request.
4. Plugins' `requestDidStart` hooks run.
5. Apollo looks up the query text in its document cache. If it's not there, it parses it into an AST and validates it against the schema (plus custom rules like depth limits), then caches the result.
6. Execution starts at the `Query` type. Root resolvers run, for example `Query.posts` loads 20 posts with one database query.
7. For each post, `Post.author` calls `loaders.user.load(post.authorId)`. All 20 calls are collected in the same tick.
8. DataLoader calls the batch function once with the unique author IDs, which runs one `SELECT ... WHERE id = ANY(...)`, and returns users in key order.
9. Each `author` promise resolves, and the executor continues with the author's scalar fields using default resolvers.
10. Errors in any field are caught, that field becomes `null` (propagating to a nullable parent if needed), and the error is added to `errors`, formatted by `formatError`.
11. The cache control plugin computes the response cache policy and sets `Cache-Control`.
12. `willSendResponse` hooks run, the result is serialized to JSON and sent back.
13. The DataLoaders and the context are thrown away with the request, so no data leaks to the next one.
