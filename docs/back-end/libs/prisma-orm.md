# Prisma ORM Interview Questions and Answers

_Last updated: October 28, 2026_

450 Prisma ORM interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers target Prisma ORM 7 (the current stable major version), with the `prisma-client` generator, driver adapters and `prisma.config.ts`. Older things like the `prisma-client-js` generator, the Rust query engine and `url` in the datasource block are mentioned where they still matter, since you will still see them in real projects. MongoDB is still on Prisma 6, and Prisma 8 is only a release candidate at the time of writing.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is Prisma ORM?](#1-what-is-prisma-orm)
- [2: What is an ORM?](#2-what-is-an-orm)
- [3: What are the main parts of Prisma ORM?](#3-what-are-the-main-parts-of-prisma-orm)
- [4: What is the Prisma schema?](#4-what-is-the-prisma-schema)
- [5: Which databases does Prisma support?](#5-which-databases-does-prisma-support)
- [6: How do you install Prisma in a project?](#6-how-do-you-install-prisma-in-a-project)
- [7: What does prisma init do?](#7-what-does-prisma-init-do)
- [8: What is the prisma.config.ts file?](#8-what-is-the-prismaconfigts-file)
- [9: What is the generator block?](#9-what-is-the-generator-block)
- [10: What is the datasource block?](#10-what-is-the-datasource-block)
- [11: What is a model in Prisma?](#11-what-is-a-model-in-prisma)
- [12: What scalar types does Prisma support?](#12-what-scalar-types-does-prisma-support)
- [13: What do the ? and [] modifiers mean on a field?](#13-what-do-the--and--modifiers-mean-on-a-field)
- [14: What is the @id attribute?](#14-what-is-the-id-attribute)
- [15: What does @default do?](#15-what-does-default-do)
- [16: What is the difference between autoincrement(), uuid() and cuid()?](#16-what-is-the-difference-between-autoincrement-uuid-and-cuid)
- [17: What does @unique do?](#17-what-does-unique-do)
- [18: What does @updatedAt do?](#18-what-does-updatedat-do)
- [19: What do @map and @@map do?](#19-what-do-map-and-map-do)
- [20: What is the difference between field attributes and block attributes?](#20-what-is-the-difference-between-field-attributes-and-block-attributes)
- [21: How do you define an enum?](#21-how-do-you-define-an-enum)
- [22: What is a relation in Prisma?](#22-what-is-a-relation-in-prisma)
- [23: What is the difference between a relation field and a scalar field?](#23-what-is-the-difference-between-a-relation-field-and-a-scalar-field)
- [24: How do you define a one-to-one relation?](#24-how-do-you-define-a-one-to-one-relation)
- [25: How do you define a one-to-many relation?](#25-how-do-you-define-a-one-to-many-relation)
- [26: How do you define a many-to-many relation?](#26-how-do-you-define-a-many-to-many-relation)
- [27: What does prisma generate do?](#27-what-does-prisma-generate-do)
- [28: How do you create a Prisma Client instance in Prisma 7?](#28-how-do-you-create-a-prisma-client-instance-in-prisma-7)
- [29: What is a driver adapter?](#29-what-is-a-driver-adapter)
- [30: How do you read all records of a model?](#30-how-do-you-read-all-records-of-a-model)
- [31: What is the difference between findUnique and findFirst?](#31-what-is-the-difference-between-findunique-and-findfirst)
- [32: What do findUniqueOrThrow and findFirstOrThrow do?](#32-what-do-finduniqueorthrow-and-findfirstorthrow-do)
- [33: How do you create a record?](#33-how-do-you-create-a-record)
- [34: How do you create many records at once?](#34-how-do-you-create-many-records-at-once)
- [35: How do you update a record?](#35-how-do-you-update-a-record)
- [36: How do you update many records?](#36-how-do-you-update-many-records)
- [37: What is an upsert?](#37-what-is-an-upsert)
- [38: How do you delete records?](#38-how-do-you-delete-records)
- [39: How do you count records?](#39-how-do-you-count-records)
- [40: What does select do?](#40-what-does-select-do)
- [41: What does include do?](#41-what-does-include-do)
- [42: Can you use select and include together?](#42-can-you-use-select-and-include-together)
- [43: What does omit do?](#43-what-does-omit-do)
- [44: How do you filter records with where?](#44-how-do-you-filter-records-with-where)
- [45: What filter operators does Prisma have?](#45-what-filter-operators-does-prisma-have)
- [46: How do you use AND, OR and NOT?](#46-how-do-you-use-and-or-and-not)
- [47: How do you sort results?](#47-how-do-you-sort-results)
- [48: How do you paginate with take and skip?](#48-how-do-you-paginate-with-take-and-skip)
- [49: How do you get distinct values?](#49-how-do-you-get-distinct-values)
- [50: How do you filter by a related record?](#50-how-do-you-filter-by-a-related-record)
- [51: How do you create a record together with related records?](#51-how-do-you-create-a-record-together-with-related-records)
- [52: How do you connect a record to an existing related record?](#52-how-do-you-connect-a-record-to-an-existing-related-record)
- [53: How do you remove a relation between records?](#53-how-do-you-remove-a-relation-between-records)
- [54: What is Prisma Migrate?](#54-what-is-prisma-migrate)
- [55: What does prisma migrate dev do?](#55-what-does-prisma-migrate-dev-do)
- [56: What does prisma migrate deploy do?](#56-what-does-prisma-migrate-deploy-do)
- [57: What does prisma db push do?](#57-what-does-prisma-db-push-do)
- [58: What is the difference between migrate dev and db push?](#58-what-is-the-difference-between-migrate-dev-and-db-push)
- [59: What does prisma migrate reset do?](#59-what-does-prisma-migrate-reset-do)
- [60: What is Prisma Studio?](#60-what-is-prisma-studio)
- [61: What is introspection?](#61-what-is-introspection)
- [62: When would you use db pull?](#62-when-would-you-use-db-pull)
- [63: What does prisma format do?](#63-what-does-prisma-format-do)
- [64: What does prisma validate do?](#64-what-does-prisma-validate-do)
- [65: How do you seed a database?](#65-how-do-you-seed-a-database)
- [66: Why should seed scripts use upsert?](#66-why-should-seed-scripts-use-upsert)
- [67: How are environment variables loaded in Prisma 7?](#67-how-are-environment-variables-loaded-in-prisma-7)
- [68: What is the env() helper in prisma.config.ts?](#68-what-is-the-env-helper-in-prismaconfigts)
- [69: What is a migration file?](#69-what-is-a-migration-file)
- [70: What is the _prisma_migrations table?](#70-what-is-the-_prisma_migrations-table)
- [71: What is the migration_lock.toml file?](#71-what-is-the-migration_locktoml-file)
- [72: How do you store JSON data with Prisma?](#72-how-do-you-store-json-data-with-prisma)
- [73: How does Prisma handle dates?](#73-how-does-prisma-handle-dates)
- [74: What is the Decimal type used for?](#74-what-is-the-decimal-type-used-for)
- [75: What is the BigInt type used for?](#75-what-is-the-bigint-type-used-for)
- [76: What is the Bytes type used for?](#76-what-is-the-bytes-type-used-for)
- [77: What are native type attributes?](#77-what-are-native-type-attributes)
- [78: How do you add an index?](#78-how-do-you-add-an-index)
- [79: How do you make a combination of fields unique?](#79-how-do-you-make-a-combination-of-fields-unique)
- [80: How do you define a composite primary key?](#80-how-do-you-define-a-composite-primary-key)
- [81: How do you write comments in the Prisma schema?](#81-how-do-you-write-comments-in-the-prisma-schema)
- [82: What is the Prisma VS Code extension?](#82-what-is-the-prisma-vs-code-extension)
- [83: How do you check which Prisma version you are using?](#83-how-do-you-check-which-prisma-version-you-are-using)
- [84: What are the basic aggregate functions in Prisma?](#84-what-are-the-basic-aggregate-functions-in-prisma)
- [85: What does groupBy do?](#85-what-does-groupby-do)
- [86: How do you count related records?](#86-how-do-you-count-related-records)
- [87: How do you increment a number field?](#87-how-do-you-increment-a-number-field)
- [88: What is the PrismaClient $connect method for?](#88-what-is-the-prismaclient-connect-method-for)
- [89: What is the $disconnect method for?](#89-what-is-the-disconnect-method-for)
- [90: Why should you create only one PrismaClient instance?](#90-why-should-you-create-only-one-prismaclient-instance)
- [91: What is a transaction?](#91-what-is-a-transaction)
- [92: How do you run several queries in one transaction?](#92-how-do-you-run-several-queries-in-one-transaction)
- [93: What is a raw query in Prisma?](#93-what-is-a-raw-query-in-prisma)
- [94: What is the difference between $queryRaw and $executeRaw?](#94-what-is-the-difference-between-queryraw-and-executeraw)
- [95: What is the error code P2002?](#95-what-is-the-error-code-p2002)
- [96: What is the error code P2025?](#96-what-is-the-error-code-p2025)
- [97: What is the Prisma namespace?](#97-what-is-the-prisma-namespace)
- [98: How do you get the TypeScript type of a model?](#98-how-do-you-get-the-typescript-type-of-a-model)
- [99: What are the type safety benefits of Prisma Client?](#99-what-are-the-type-safety-benefits-of-prisma-client)
- [100: Is Prisma Client only for TypeScript?](#100-is-prisma-client-only-for-typescript)
- [101: What is the difference between null and undefined in Prisma queries?](#101-what-is-the-difference-between-null-and-undefined-in-prisma-queries)
- [102: How do you check if a field is null or not null?](#102-how-do-you-check-if-a-field-is-null-or-not-null)
- [103: How do you do a case insensitive search?](#103-how-do-you-do-a-case-insensitive-search)
- [104: What are scalar lists?](#104-what-are-scalar-lists)
- [105: How do you filter on a scalar list?](#105-how-do-you-filter-on-a-scalar-list)
- [106: How do you add a value to a scalar list?](#106-how-do-you-add-a-value-to-a-scalar-list)
- [107: What is the PrismaClient log option?](#107-what-is-the-prismaclient-log-option)
- [108: Where is Prisma Client generated in Prisma 7?](#108-where-is-prisma-client-generated-in-prisma-7)
- [109: Should you commit the generated Prisma Client to git?](#109-should-you-commit-the-generated-prisma-client-to-git)
- [110: What is the difference between prisma-client and prisma-client-js?](#110-what-is-the-difference-between-prisma-client-and-prisma-client-js)
- [111: What is Prisma Accelerate?](#111-what-is-prisma-accelerate)
- [112: What is Prisma Postgres?](#112-what-is-prisma-postgres)
- [113: What is the difference between required and optional relations?](#113-what-is-the-difference-between-required-and-optional-relations)
- [114: What does @relation do?](#114-what-does-relation-do)
- [115: What does onDelete: Cascade do?](#115-what-does-ondelete-cascade-do)
- [116: What referential actions does Prisma support?](#116-what-referential-actions-does-prisma-support)
- [117: What is an explicit many-to-many relation?](#117-what-is-an-explicit-many-to-many-relation)
- [118: What is the difference between implicit and explicit many-to-many relations?](#118-what-is-the-difference-between-implicit-and-explicit-many-to-many-relations)
- [119: What is the Unsupported type?](#119-what-is-the-unsupported-type)
- [120: What do @ignore and @@ignore do?](#120-what-do-ignore-and-ignore-do)
- [121: How do you open the Prisma CLI help?](#121-how-do-you-open-the-prisma-cli-help)
- [122: What does dbgenerated() do?](#122-what-does-dbgenerated-do)
- [123: What does @default(now()) do?](#123-what-does-defaultnow-do)
- [124: How do you return only some fields of related records?](#124-how-do-you-return-only-some-fields-of-related-records)
- [125: How do you filter, sort and limit related records in include?](#125-how-do-you-filter-sort-and-limit-related-records-in-include)
- [126: How do you load nested relations several levels deep?](#126-how-do-you-load-nested-relations-several-levels-deep)
- [127: How do you delete a record and its related records?](#127-how-do-you-delete-a-record-and-its-related-records)
- [128: What does connectOrCreate do?](#128-what-does-connectorcreate-do)
- [129: How do you check if a record exists?](#129-how-do-you-check-if-a-record-exists)
- [130: How do you get the first N records?](#130-how-do-you-get-the-first-n-records)
- [131: What is a shadow database?](#131-what-is-a-shadow-database)
- [132: What is schema drift?](#132-what-is-schema-drift)
- [133: What does prisma migrate status do?](#133-what-does-prisma-migrate-status-do)
- [134: How do you name a migration?](#134-how-do-you-name-a-migration)
- [135: Can you edit a migration before applying it?](#135-can-you-edit-a-migration-before-applying-it)
- [136: Why should you not edit a migration that was already applied?](#136-why-should-you-not-edit-a-migration-that-was-already-applied)
- [137: What is the difference between Prisma ORM and plain SQL?](#137-what-is-the-difference-between-prisma-orm-and-plain-sql)
- [138: What are the main advantages of using Prisma?](#138-what-are-the-main-advantages-of-using-prisma)
- [139: What are some drawbacks of Prisma?](#139-what-are-some-drawbacks-of-prisma)
- [140: What is the fluent API in Prisma?](#140-what-is-the-fluent-api-in-prisma)
- [141: How do you sort by a field of a related model?](#141-how-do-you-sort-by-a-field-of-a-related-model)
- [142: How do you control where null values go when sorting?](#142-how-do-you-control-where-null-values-go-when-sorting)
- [143: What is the difference between update and updateMany?](#143-what-is-the-difference-between-update-and-updatemany)
- [144: What is the difference between delete and deleteMany?](#144-what-is-the-difference-between-delete-and-deletemany)
- [145: Can you run Prisma with SQLite?](#145-can-you-run-prisma-with-sqlite)
- [146: Can you have more than one schema file?](#146-can-you-have-more-than-one-schema-file)
- [147: What is the Prisma CLI command to create the client after cloning a project?](#147-what-is-the-prisma-cli-command-to-create-the-client-after-cloning-a-project)
- [148: What does createManyAndReturn do?](#148-what-does-createmanyandreturn-do)
- [149: Does Prisma work with Express, NestJS and Next.js?](#149-does-prisma-work-with-express-nestjs-and-nextjs)
- [150: What changed in Prisma 7 at a high level?](#150-what-changed-in-prisma-7-at-a-high-level)

### Moderate Questions (151-300)

- [151: How do you set up Prisma 7 in a new TypeScript project from scratch?](#151-how-do-you-set-up-prisma-7-in-a-new-typescript-project-from-scratch)
- [152: What tsconfig settings work well with Prisma 7?](#152-what-tsconfig-settings-work-well-with-prisma-7)
- [153: What options does the prisma-client generator have?](#153-what-options-does-the-prisma-client-generator-have)
- [154: What files does the prisma-client generator create?](#154-what-files-does-the-prisma-client-generator-create)
- [155: Why does the generated client have a browser.ts file?](#155-why-does-the-generated-client-have-a-browserts-file)
- [156: How do you upgrade a project from Prisma 6 to Prisma 7?](#156-how-do-you-upgrade-a-project-from-prisma-6-to-prisma-7)
- [157: Why did Prisma remove the Rust query engine in Prisma 7?](#157-why-did-prisma-remove-the-rust-query-engine-in-prisma-7)
- [158: What happened to binaryTargets in Prisma 7?](#158-what-happened-to-binarytargets-in-prisma-7)
- [159: How do you configure the database URL used by migrations?](#159-how-do-you-configure-the-database-url-used-by-migrations)
- [160: What happened to directUrl in Prisma 7?](#160-what-happened-to-directurl-in-prisma-7)
- [161: How do you use a different .env file per environment?](#161-how-do-you-use-a-different-env-file-per-environment)
- [162: How do you share a single Prisma Client in a Next.js app?](#162-how-do-you-share-a-single-prisma-client-in-a-nextjs-app)
- [163: How do you use Prisma in NestJS?](#163-how-do-you-use-prisma-in-nestjs)
- [164: How do you use Prisma in an Express app?](#164-how-do-you-use-prisma-in-an-express-app)
- [165: How do you do cursor based pagination?](#165-how-do-you-do-cursor-based-pagination)
- [166: When should you use cursor pagination instead of offset pagination?](#166-when-should-you-use-cursor-pagination-instead-of-offset-pagination)
- [167: What is an interactive transaction?](#167-what-is-an-interactive-transaction)
- [168: What options can you pass to an interactive transaction?](#168-what-options-can-you-pass-to-an-interactive-transaction)
- [169: What isolation levels can you set in Prisma transactions?](#169-what-isolation-levels-can-you-set-in-prisma-transactions)
- [170: When should you use a batch $transaction([]) instead of an interactive one?](#170-when-should-you-use-a-batch-transaction-instead-of-an-interactive-one)
- [171: What happens if you use prisma instead of tx inside an interactive transaction?](#171-what-happens-if-you-use-prisma-instead-of-tx-inside-an-interactive-transaction)
- [172: Are nested writes transactional?](#172-are-nested-writes-transactional)
- [173: How do you update a record and its related records in one call?](#173-how-do-you-update-a-record-and-its-related-records-in-one-call)
- [174: What nested write operations are available?](#174-what-nested-write-operations-are-available)
- [175: What is the difference between checked and unchecked inputs?](#175-what-is-the-difference-between-checked-and-unchecked-inputs)
- [176: How do you get the type of a query result with relations?](#176-how-do-you-get-the-type-of-a-query-result-with-relations)
- [177: How do you reuse a select or include object with full type safety?](#177-how-do-you-reuse-a-select-or-include-object-with-full-type-safety)
- [178: What are client extensions?](#178-what-are-client-extensions)
- [179: How do you add a custom method to a model?](#179-how-do-you-add-a-custom-method-to-a-model)
- [180: How do you add a computed field with a result extension?](#180-how-do-you-add-a-computed-field-with-a-result-extension)
- [181: How do you wrap all queries with a query extension?](#181-how-do-you-wrap-all-queries-with-a-query-extension)
- [182: What replaced middleware ($use) in Prisma 7?](#182-what-replaced-middleware-use-in-prisma-7)
- [183: How do you combine multiple extensions?](#183-how-do-you-combine-multiple-extensions)
- [184: How do you implement soft delete with Prisma?](#184-how-do-you-implement-soft-delete-with-prisma)
- [185: How do you add a top level method with a client extension?](#185-how-do-you-add-a-top-level-method-with-a-client-extension)
- [186: How do you log queries as events?](#186-how-do-you-log-queries-as-events)
- [187: How do you catch Prisma errors properly?](#187-how-do-you-catch-prisma-errors-properly)
- [188: What Prisma error classes are there?](#188-what-prisma-error-classes-are-there)
- [189: What does error code P2003 mean?](#189-what-does-error-code-p2003-mean)
- [190: How do you map Prisma errors to HTTP responses?](#190-how-do-you-map-prisma-errors-to-http-responses)
- [191: How do you write a raw query with dynamic parts safely?](#191-how-do-you-write-a-raw-query-with-dynamic-parts-safely)
- [192: What is the danger of $queryRawUnsafe?](#192-what-is-the-danger-of-queryrawunsafe)
- [193: How do you add a type to a raw query result?](#193-how-do-you-add-a-type-to-a-raw-query-result)
- [194: What is TypedSQL?](#194-what-is-typedsql)
- [195: Why do COUNT results in raw queries come back as bigint?](#195-why-do-count-results-in-raw-queries-come-back-as-bigint)
- [196: How do you send BigInt values in a JSON API response?](#196-how-do-you-send-bigint-values-in-a-json-api-response)
- [197: How do you handle Decimal values in API responses?](#197-how-do-you-handle-decimal-values-in-api-responses)
- [198: How do you filter on JSON fields?](#198-how-do-you-filter-on-json-fields)
- [199: What are Prisma.JsonNull, Prisma.DbNull and Prisma.AnyNull?](#199-what-are-prismajsonnull-prismadbnull-and-prismaanynull)
- [200: How do you type the contents of a Json field?](#200-how-do-you-type-the-contents-of-a-json-field)
- [201: How do you rename a field without losing data?](#201-how-do-you-rename-a-field-without-losing-data)
- [202: How do you do a data migration with Prisma?](#202-how-do-you-do-a-data-migration-with-prisma)
- [203: What does prisma migrate resolve do?](#203-what-does-prisma-migrate-resolve-do)
- [204: What is baselining?](#204-what-is-baselining)
- [205: What does prisma migrate diff do?](#205-what-does-prisma-migrate-diff-do)
- [206: How do you run a SQL file against the database with the Prisma CLI?](#206-how-do-you-run-a-sql-file-against-the-database-with-the-prisma-cli)
- [207: How do you run migrations in a CI/CD pipeline?](#207-how-do-you-run-migrations-in-a-cicd-pipeline)
- [208: How do you check for missing migrations in CI?](#208-how-do-you-check-for-missing-migrations-in-ci)
- [209: How do you use Prisma with Docker?](#209-how-do-you-use-prisma-with-docker)
- [210: How do you test code that uses Prisma with unit tests?](#210-how-do-you-test-code-that-uses-prisma-with-unit-tests)
- [211: How do you write integration tests with a real database?](#211-how-do-you-write-integration-tests-with-a-real-database)
- [212: How do you clean the database between tests?](#212-how-do-you-clean-the-database-between-tests)
- [213: How do you seed different data per environment?](#213-how-do-you-seed-different-data-per-environment)
- [214: How do you define a self relation?](#214-how-do-you-define-a-self-relation)
- [215: How do you define two relations between the same two models?](#215-how-do-you-define-two-relations-between-the-same-two-models)
- [216: How do you model a many-to-many self relation, like followers?](#216-how-do-you-model-a-many-to-many-self-relation-like-followers)
- [217: What is relationMode = "prisma"?](#217-what-is-relationmode--prisma)
- [218: How do you use multiple database schemas in PostgreSQL?](#218-how-do-you-use-multiple-database-schemas-in-postgresql)
- [219: How do you map a database view in Prisma?](#219-how-do-you-map-a-database-view-in-prisma)
- [220: How do you enable a preview feature?](#220-how-do-you-enable-a-preview-feature)
- [221: What is relationLoadStrategy?](#221-what-is-relationloadstrategy)
- [222: When is the "query" load strategy better than "join"?](#222-when-is-the-query-load-strategy-better-than-join)
- [223: How do you do full text search with Prisma?](#223-how-do-you-do-full-text-search-with-prisma)
- [224: How do you create a GIN index on a JSON or array column in PostgreSQL?](#224-how-do-you-create-a-gin-index-on-a-json-or-array-column-in-postgresql)
- [225: How do you set the sort order of an index?](#225-how-do-you-set-the-sort-order-of-an-index)
- [226: How do you give an index or constraint a custom name?](#226-how-do-you-give-an-index-or-constraint-a-custom-name)
- [227: What are field references?](#227-what-are-field-references)
- [228: How do you filter by the count of related records?](#228-how-do-you-filter-by-the-count-of-related-records)
- [229: How do you count only some related records?](#229-how-do-you-count-only-some-related-records)
- [230: How do you set omit globally?](#230-how-do-you-set-omit-globally)
- [231: What is the strictUndefinedChecks preview feature?](#231-what-is-the-strictundefinedchecks-preview-feature)
- [232: Why is passing undefined in a deleteMany filter dangerous?](#232-why-is-passing-undefined-in-a-deletemany-filter-dangerous)
- [233: How does upsert work under the hood?](#233-how-does-upsert-work-under-the-hood)
- [234: How do you do a bulk update with different values per row?](#234-how-do-you-do-a-bulk-update-with-different-values-per-row)
- [235: What does updateManyAndReturn do?](#235-what-does-updatemanyandreturn-do)
- [236: How do you configure the connection pool in Prisma 7?](#236-how-do-you-configure-the-connection-pool-in-prisma-7)
- [237: Why might you get connection timeouts after upgrading to Prisma 7?](#237-why-might-you-get-connection-timeouts-after-upgrading-to-prisma-7)
- [238: Why might you get P1010 or SSL errors after upgrading to Prisma 7?](#238-why-might-you-get-p1010-or-ssl-errors-after-upgrading-to-prisma-7)
- [239: How do you connect to Neon with Prisma?](#239-how-do-you-connect-to-neon-with-prisma)
- [240: How do you connect to MySQL or MariaDB in Prisma 7?](#240-how-do-you-connect-to-mysql-or-mariadb-in-prisma-7)
- [241: How do you use Prisma with Cloudflare Workers and D1?](#241-how-do-you-use-prisma-with-cloudflare-workers-and-d1)
- [242: How do you run Prisma in serverless functions without running out of connections?](#242-how-do-you-run-prisma-in-serverless-functions-without-running-out-of-connections)
- [243: How do you use Prisma with PgBouncer?](#243-how-do-you-use-prisma-with-pgbouncer)
- [244: What is the OpenTelemetry tracing support in Prisma?](#244-what-is-the-opentelemetry-tracing-support-in-prisma)
- [245: What happened to the metrics feature?](#245-what-happened-to-the-metrics-feature)
- [246: How do you count queries per request?](#246-how-do-you-count-queries-per-request)
- [247: How do you see the SQL that Prisma generates?](#247-how-do-you-see-the-sql-that-prisma-generates)
- [248: How do you return the created record from a nested create with relations?](#248-how-do-you-return-the-created-record-from-a-nested-create-with-relations)
- [249: What is the difference between findMany with take: 1 and findFirst?](#249-what-is-the-difference-between-findmany-with-take-1-and-findfirst)
- [250: How do you query records created in a date range?](#250-how-do-you-query-records-created-in-a-date-range)
- [251: How do you store and query dates without a time part?](#251-how-do-you-store-and-query-dates-without-a-time-part)
- [252: How do you handle time zones with Prisma?](#252-how-do-you-handle-time-zones-with-prisma)
- [253: How do you change an enum safely?](#253-how-do-you-change-an-enum-safely)
- [254: How do you map enum values to different names in the database?](#254-how-do-you-map-enum-values-to-different-names-in-the-database)
- [255: How do you make a required column from an optional one when the table has data?](#255-how-do-you-make-a-required-column-from-an-optional-one-when-the-table-has-data)
- [256: How do you add a unique constraint to a column that has duplicates?](#256-how-do-you-add-a-unique-constraint-to-a-column-that-has-duplicates)
- [257: How do you work with Prisma in a monorepo?](#257-how-do-you-work-with-prisma-in-a-monorepo)
- [258: How do you avoid Prisma Client being out of date in CI?](#258-how-do-you-avoid-prisma-client-being-out-of-date-in-ci)
- [259: How do you use Prisma with GraphQL?](#259-how-do-you-use-prisma-with-graphql)
- [260: How does Prisma batch findUnique queries?](#260-how-does-prisma-batch-findunique-queries)
- [261: How do you write a repository layer on top of Prisma?](#261-how-do-you-write-a-repository-layer-on-top-of-prisma)
- [262: How do you pass a transaction client to functions?](#262-how-do-you-pass-a-transaction-client-to-functions)
- [263: Can you nest $transaction calls?](#263-can-you-nest-transaction-calls)
- [264: How do you retry a transaction after a write conflict?](#264-how-do-you-retry-a-transaction-after-a-write-conflict)
- [265: How do you lock a row for update in Prisma?](#265-how-do-you-lock-a-row-for-update-in-prisma)
- [266: How do you implement optimistic concurrency control?](#266-how-do-you-implement-optimistic-concurrency-control)
- [267: What is extendedWhereUnique?](#267-what-is-extendedwhereunique)
- [268: How do you check that a user owns a record before updating it?](#268-how-do-you-check-that-a-user-owns-a-record-before-updating-it)
- [269: How do you select a random row?](#269-how-do-you-select-a-random-row)
- [270: How do you query with a LIKE pattern that contains % or _?](#270-how-do-you-query-with-a-like-pattern-that-contains--or-_)
- [271: How do you get the total count and a page of results together?](#271-how-do-you-get-the-total-count-and-a-page-of-results-together)
- [272: How do you load a list of records by a list of ids?](#272-how-do-you-load-a-list-of-records-by-a-list-of-ids)
- [273: How do you write a query that selects users with no posts?](#273-how-do-you-write-a-query-that-selects-users-with-no-posts)
- [274: What is the difference between every and some on an empty relation?](#274-what-is-the-difference-between-every-and-some-on-an-empty-relation)
- [275: How do you count rows per value of a relation in one query?](#275-how-do-you-count-rows-per-value-of-a-relation-in-one-query)
- [276: Can groupBy include relations?](#276-can-groupby-include-relations)
- [277: How do you get the newest post per user?](#277-how-do-you-get-the-newest-post-per-user)
- [278: How do you use Prisma with Zod for input validation?](#278-how-do-you-use-prisma-with-zod-for-input-validation)
- [279: Why should you not pass req.body directly to Prisma?](#279-why-should-you-not-pass-reqbody-directly-to-prisma)
- [280: How do you create records with a known id in a test?](#280-how-do-you-create-records-with-a-known-id-in-a-test)
- [281: How do you use Prisma Studio with a remote database?](#281-how-do-you-use-prisma-studio-with-a-remote-database)
- [282: How do you use Prisma in a script or cron job?](#282-how-do-you-use-prisma-in-a-script-or-cron-job)
- [283: How do you shut down Prisma gracefully in a server?](#283-how-do-you-shut-down-prisma-gracefully-in-a-server)
- [284: Can Prisma use database triggers, functions or check constraints?](#284-can-prisma-use-database-triggers-functions-or-check-constraints)
- [285: How do you add a CHECK constraint?](#285-how-do-you-add-a-check-constraint)
- [286: How do you use PostgreSQL extensions like pgcrypto or citext?](#286-how-do-you-use-postgresql-extensions-like-pgcrypto-or-citext)
- [287: How do you share Prisma model types with a React frontend?](#287-how-do-you-share-prisma-model-types-with-a-react-frontend)
- [288: Why can dates break when you send Prisma results through JSON?](#288-why-can-dates-break-when-you-send-prisma-results-through-json)
- [289: How do you pick between Int and String ids?](#289-how-do-you-pick-between-int-and-string-ids)
- [290: How do you model a polymorphic relation in Prisma?](#290-how-do-you-model-a-polymorphic-relation-in-prisma)
- [291: How do you store an ordered list of related items?](#291-how-do-you-store-an-ordered-list-of-related-items)
- [292: How do you create a record only if it doesn't exist, without updating?](#292-how-do-you-create-a-record-only-if-it-doesnt-exist-without-updating)
- [293: How do you return only the id after a create?](#293-how-do-you-return-only-the-id-after-a-create)
- [294: How do you use the Prisma Client in a worker thread or child process?](#294-how-do-you-use-the-prisma-client-in-a-worker-thread-or-child-process)
- [295: How do you use the same schema for SQLite in tests and PostgreSQL in production?](#295-how-do-you-use-the-same-schema-for-sqlite-in-tests-and-postgresql-in-production)
- [296: How does a unique constraint behave on a nullable column?](#296-how-does-a-unique-constraint-behave-on-a-nullable-column)
- [297: How do you find slow queries in an app that uses Prisma?](#297-how-do-you-find-slow-queries-in-an-app-that-uses-prisma)
- [298: How do you use EXPLAIN with a Prisma query?](#298-how-do-you-use-explain-with-a-prisma-query)
- [299: What does the PrismaClient errorFormat option do?](#299-what-does-the-prismaclient-errorformat-option-do)
- [300: How do you decide when to use raw SQL instead of the Prisma API?](#300-how-do-you-decide-when-to-use-raw-sql-instead-of-the-prisma-api)

### Advanced Questions (301-450)

- [301: How does Prisma Client run a query in Prisma 7?](#301-how-does-prisma-client-run-a-query-in-prisma-7)
- [302: What was the Rust query engine and how did it work?](#302-what-was-the-rust-query-engine-and-how-did-it-work)
- [303: What are the trade-offs of the Rust-free architecture?](#303-what-are-the-trade-offs-of-the-rust-free-architecture)
- [304: What are the N+1 query problems you can hit with Prisma?](#304-what-are-the-n1-query-problems-you-can-hit-with-prisma)
- [305: How many SQL queries does an include generate?](#305-how-many-sql-queries-does-an-include-generate)
- [306: How do you make large IN lists safe?](#306-how-do-you-make-large-in-lists-safe)
- [307: How do you process millions of rows without loading them all in memory?](#307-how-do-you-process-millions-of-rows-without-loading-them-all-in-memory)
- [308: How do you insert a very large number of rows efficiently?](#308-how-do-you-insert-a-very-large-number-of-rows-efficiently)
- [309: How do you design indexes for Prisma queries?](#309-how-do-you-design-indexes-for-prisma-queries)
- [310: Why does the order of fields in a composite index matter?](#310-why-does-the-order-of-fields-in-a-composite-index-matter)
- [311: What are partial indexes and does Prisma support them?](#311-what-are-partial-indexes-and-does-prisma-support-them)
- [312: How do you add an index to a big table without downtime?](#312-how-do-you-add-an-index-to-a-big-table-without-downtime)
- [313: How do you do zero downtime schema changes with Prisma?](#313-how-do-you-do-zero-downtime-schema-changes-with-prisma)
- [314: What can go wrong when migrations run at app start?](#314-what-can-go-wrong-when-migrations-run-at-app-start)
- [315: How do you recover from a failed migration in production?](#315-how-do-you-recover-from-a-failed-migration-in-production)
- [316: How do you write a down migration with Prisma?](#316-how-do-you-write-a-down-migration-with-prisma)
- [317: How do you squash many migrations into one?](#317-how-do-you-squash-many-migrations-into-one)
- [318: How does Prisma Migrate detect what changed?](#318-how-does-prisma-migrate-detect-what-changed)
- [319: How do you handle a team where two people add migrations at the same time?](#319-how-do-you-handle-a-team-where-two-people-add-migrations-at-the-same-time)
- [320: How do you implement multi-tenancy with Prisma?](#320-how-do-you-implement-multi-tenancy-with-prisma)
- [321: How do you enforce a tenant filter on every query?](#321-how-do-you-enforce-a-tenant-filter-on-every-query)
- [322: How do you use PostgreSQL Row Level Security with Prisma?](#322-how-do-you-use-postgresql-row-level-security-with-prisma)
- [323: How do you route reads to a read replica?](#323-how-do-you-route-reads-to-a-read-replica)
- [324: How would you handle sharding with Prisma?](#324-how-would-you-handle-sharding-with-prisma)
- [325: How do you connect to more than one database in one app?](#325-how-do-you-connect-to-more-than-one-database-in-one-app)
- [326: How do you keep data consistent across a database write and a message queue?](#326-how-do-you-keep-data-consistent-across-a-database-write-and-a-message-queue)
- [327: Why should interactive transactions be short?](#327-why-should-interactive-transactions-be-short)
- [328: What happens when an interactive transaction times out?](#328-what-happens-when-an-interactive-transaction-times-out)
- [329: How do you prevent double charging when a payment request is retried?](#329-how-do-you-prevent-double-charging-when-a-payment-request-is-retried)
- [330: How do you handle race conditions on a counter or stock value?](#330-how-do-you-handle-race-conditions-on-a-counter-or-stock-value)
- [331: How do you lock across processes with Prisma, for example for a cron job?](#331-how-do-you-lock-across-processes-with-prisma-for-example-for-a-cron-job)
- [332: What are common security risks when using Prisma?](#332-what-are-common-security-risks-when-using-prisma)
- [333: Is Prisma.raw safe?](#333-is-prismaraw-safe)
- [334: Can users inject operators through Prisma filters?](#334-can-users-inject-operators-through-prisma-filters)
- [335: How do you store passwords with Prisma?](#335-how-do-you-store-passwords-with-prisma)
- [336: How do you limit database permissions for an app that uses Prisma?](#336-how-do-you-limit-database-permissions-for-an-app-that-uses-prisma)
- [337: How do you audit who changed what?](#337-how-do-you-audit-who-changed-what)
- [338: How do you encrypt a column with Prisma?](#338-how-do-you-encrypt-a-column-with-prisma)
- [339: How do the select and include types work internally?](#339-how-do-the-select-and-include-types-work-internally)
- [340: How do you speed up TypeScript when the Prisma schema is huge?](#340-how-do-you-speed-up-typescript-when-the-prisma-schema-is-huge)
- [341: How do you write a generic function that works for any model?](#341-how-do-you-write-a-generic-function-that-works-for-any-model)
- [342: What does Prisma.getExtensionContext do?](#342-what-does-prismagetextensioncontext-do)
- [343: How do you type the client after using $extends?](#343-how-do-you-type-the-client-after-using-extends)
- [344: How do extensions behave inside transactions?](#344-how-do-extensions-behave-inside-transactions)
- [345: Why is the result extension field not available in where or orderBy?](#345-why-is-the-result-extension-field-not-available-in-where-or-orderby)
- [346: How do you mock an extended Prisma client in tests?](#346-how-do-you-mock-an-extended-prisma-client-in-tests)
- [347: What are the limits of mocking Prisma in unit tests?](#347-what-are-the-limits-of-mocking-prisma-in-unit-tests)
- [348: How do you test migrations?](#348-how-do-you-test-migrations)
- [349: How do you handle a column type that Prisma maps poorly?](#349-how-do-you-handle-a-column-type-that-prisma-maps-poorly)
- [350: How do you use PostGIS or pgvector with Prisma?](#350-how-do-you-use-postgis-or-pgvector-with-prisma)
- [351: How do you size the connection pool for a Prisma app?](#351-how-do-you-size-the-connection-pool-for-a-prisma-app)
- [352: What happens when the connection pool is exhausted?](#352-what-happens-when-the-connection-pool-is-exhausted)
- [353: Why can Promise.all over many Prisma queries be a problem?](#353-why-can-promiseall-over-many-prisma-queries-be-a-problem)
- [354: How do you reduce cold start time for Prisma in serverless?](#354-how-do-you-reduce-cold-start-time-for-prisma-in-serverless)
- [355: How do you choose between a TCP driver and an HTTP serverless driver?](#355-how-do-you-choose-between-a-tcp-driver-and-an-http-serverless-driver)
- [356: Why should the database be close to your app servers?](#356-why-should-the-database-be-close-to-your-app-servers)
- [357: How do you cache Prisma query results?](#357-how-do-you-cache-prisma-query-results)
- [358: How do you avoid loading too much data with include?](#358-how-do-you-avoid-loading-too-much-data-with-include)
- [359: When does Prisma generate inefficient queries, and what do you do?](#359-when-does-prisma-generate-inefficient-queries-and-what-do-you-do)
- [360: How does distinct work without nativeDistinct?](#360-how-does-distinct-work-without-nativedistinct)
- [361: How do you design a schema for an e-commerce order system with Prisma?](#361-how-do-you-design-a-schema-for-an-e-commerce-order-system-with-prisma)
- [362: How would you model user roles and permissions?](#362-how-would-you-model-user-roles-and-permissions)
- [363: How would you model a tree, like nested comments or categories?](#363-how-would-you-model-a-tree-like-nested-comments-or-categories)
- [364: How do you load a full tree with a recursive query?](#364-how-do-you-load-a-full-tree-with-a-recursive-query)
- [365: How do you implement soft delete correctly, beyond a simple filter?](#365-how-do-you-implement-soft-delete-correctly-beyond-a-simple-filter)
- [366: What are the pros and cons of using Prisma extensions for cross cutting rules?](#366-what-are-the-pros-and-cons-of-using-prisma-extensions-for-cross-cutting-rules)
- [367: How does Prisma handle cascading deletes, and what are the risks?](#367-how-does-prisma-handle-cascading-deletes-and-what-are-the-risks)
- [368: Why do you need indexes on foreign keys with relationMode = "prisma"?](#368-why-do-you-need-indexes-on-foreign-keys-with-relationmode--prisma)
- [369: How does Prisma map JavaScript types to database types, and where can precision be lost?](#369-how-does-prisma-map-javascript-types-to-database-types-and-where-can-precision-be-lost)
- [370: What happens when two Prisma versions run against the same database?](#370-what-happens-when-two-prisma-versions-run-against-the-same-database)
- [371: How do you share one database between several services that use Prisma?](#371-how-do-you-share-one-database-between-several-services-that-use-prisma)
- [372: What are the main differences between Prisma and Drizzle?](#372-what-are-the-main-differences-between-prisma-and-drizzle)
- [373: What are the main differences between Prisma and TypeORM?](#373-what-are-the-main-differences-between-prisma-and-typeorm)
- [374: When would you choose a query builder like Kysely over Prisma?](#374-when-would-you-choose-a-query-builder-like-kysely-over-prisma)
- [375: When is Prisma not a good choice?](#375-when-is-prisma-not-a-good-choice)
- [376: How does Prisma represent a query internally before it becomes SQL?](#376-how-does-prisma-represent-a-query-internally-before-it-becomes-sql)
- [377: Why does Prisma sometimes run a SELECT after an INSERT or UPDATE?](#377-why-does-prisma-sometimes-run-a-select-after-an-insert-or-update)
- [378: How do nested writes affect performance?](#378-how-do-nested-writes-affect-performance)
- [379: What happens with an update that changes nothing?](#379-what-happens-with-an-update-that-changes-nothing)
- [380: How do you do an "upsert many"?](#380-how-do-you-do-an-upsert-many)
- [381: What is the risk of a long running findMany in a request handler?](#381-what-is-the-risk-of-a-long-running-findmany-in-a-request-handler)
- [382: How do you limit query execution time?](#382-how-do-you-limit-query-execution-time)
- [383: How do you handle deadlocks in Prisma?](#383-how-do-you-handle-deadlocks-in-prisma)
- [384: Why might you see P2028 errors?](#384-why-might-you-see-p2028-errors)
- [385: How do you run a query on a specific connection, like for SET statements?](#385-how-do-you-run-a-query-on-a-specific-connection-like-for-set-statements)
- [386: How do you use Prisma with Supabase?](#386-how-do-you-use-prisma-with-supabase)
- [387: How do you use Prisma with PlanetScale?](#387-how-do-you-use-prisma-with-planetscale)
- [388: How do you deploy Prisma to a platform with read only file systems?](#388-how-do-you-deploy-prisma-to-a-platform-with-read-only-file-systems)
- [389: How do you bundle Prisma with esbuild or a similar bundler?](#389-how-do-you-bundle-prisma-with-esbuild-or-a-similar-bundler)
- [390: How do you run Prisma in Bun or Deno?](#390-how-do-you-run-prisma-in-bun-or-deno)
- [391: What is the role of migration checksums, and what if they don't match?](#391-what-is-the-role-of-migration-checksums-and-what-if-they-dont-match)
- [392: How do you handle migrations for many tenant schemas?](#392-how-do-you-handle-migrations-for-many-tenant-schemas)
- [393: How do you introspect only part of a database?](#393-how-do-you-introspect-only-part-of-a-database)
- [394: What does Prisma do when you rename a model?](#394-what-does-prisma-do-when-you-rename-a-model)
- [395: How do you handle generated or computed columns?](#395-how-do-you-handle-generated-or-computed-columns)
- [396: How do you debug "Prisma Client did not initialize" or "PrismaClient is not a constructor" errors?](#396-how-do-you-debug-prisma-client-did-not-initialize-or-prismaclient-is-not-a-constructor-errors)
- [397: How do you debug "too many connections" errors?](#397-how-do-you-debug-too-many-connections-errors)
- [398: How do you investigate a query that is fast in SQL but slow through Prisma?](#398-how-do-you-investigate-a-query-that-is-fast-in-sql-but-slow-through-prisma)
- [399: What is the impact of returning too many columns?](#399-what-is-the-impact-of-returning-too-many-columns)
- [400: How do you use Prisma with an existing database that has naming conventions you don't like?](#400-how-do-you-use-prisma-with-an-existing-database-that-has-naming-conventions-you-dont-like)
- [401: How would you migrate a large app from TypeORM or Sequelize to Prisma?](#401-how-would-you-migrate-a-large-app-from-typeorm-or-sequelize-to-prisma)
- [402: How do you replace entity lifecycle hooks (like beforeInsert) in Prisma?](#402-how-do-you-replace-entity-lifecycle-hooks-like-beforeinsert-in-prisma)
- [403: How do you keep the Prisma schema and your API types from drifting apart?](#403-how-do-you-keep-the-prisma-schema-and-your-api-types-from-drifting-apart)
- [404: How do you handle schema changes when several app versions run at once?](#404-how-do-you-handle-schema-changes-when-several-app-versions-run-at-once)
- [405: Why can dropping a column break a running Prisma app even if the code no longer uses it?](#405-why-can-dropping-a-column-break-a-running-prisma-app-even-if-the-code-no-longer-uses-it)
- [406: How do you safely change a column type, like Int to BigInt?](#406-how-do-you-safely-change-a-column-type-like-int-to-bigint)
- [407: How do you design for audit and history, like keeping all versions of a document?](#407-how-do-you-design-for-audit-and-history-like-keeping-all-versions-of-a-document)
- [408: How do you build a reliable job queue table with Prisma?](#408-how-do-you-build-a-reliable-job-queue-table-with-prisma)
- [409: How do you use LISTEN/NOTIFY with Prisma?](#409-how-do-you-use-listennotify-with-prisma)
- [410: How would you get real time database changes in a Prisma app?](#410-how-would-you-get-real-time-database-changes-in-a-prisma-app)
- [411: What do you need to know about Prisma and MongoDB today?](#411-what-do-you-need-to-know-about-prisma-and-mongodb-today)
- [412: What are composite types in Prisma?](#412-what-are-composite-types-in-prisma)
- [413: What are the main breaking changes to watch for when upgrading major Prisma versions in general?](#413-what-are-the-main-breaking-changes-to-watch-for-when-upgrading-major-prisma-versions-in-general)
- [414: What is the status of Prisma 8?](#414-what-is-the-status-of-prisma-8)
- [415: How do you run Prisma 7 and Prisma 8 side by side during an upgrade?](#415-how-do-you-run-prisma-7-and-prisma-8-side-by-side-during-an-upgrade)
- [416: What would you check in code review for a Prisma query?](#416-what-would-you-check-in-code-review-for-a-prisma-query)
- [417: What would you check in code review for a Prisma migration?](#417-what-would-you-check-in-code-review-for-a-prisma-migration)
- [418: A deploy failed because a migration timed out on a big table. What do you do?](#418-a-deploy-failed-because-a-migration-timed-out-on-a-big-table-what-do-you-do)
- [419: Users report that a list page is slow. How do you investigate it?](#419-users-report-that-a-list-page-is-slow-how-do-you-investigate-it)
- [420: After moving to serverless, the database hits its connection limit. What do you do?](#420-after-moving-to-serverless-the-database-hits-its-connection-limit-what-do-you-do)
- [421: A deleteMany removed all rows in production. What went wrong and how do you prevent it?](#421-a-deletemany-removed-all-rows-in-production-what-went-wrong-and-how-do-you-prevent-it)
- [422: Two users signed up with the same email at the same time and you got a 500 error. How do you fix it?](#422-two-users-signed-up-with-the-same-email-at-the-same-time-and-you-got-a-500-error-how-do-you-fix-it)
- [423: A report query takes 30 seconds. How would you approach it with Prisma?](#423-a-report-query-takes-30-seconds-how-would-you-approach-it-with-prisma)
- [424: You see "Transaction already closed" errors under load. What is happening?](#424-you-see-transaction-already-closed-errors-under-load-what-is-happening)
- [425: How would you add full text search to a Prisma app on PostgreSQL at scale?](#425-how-would-you-add-full-text-search-to-a-prisma-app-on-postgresql-at-scale)
- [426: How do you design a schema so that queries scale as data grows?](#426-how-do-you-design-a-schema-so-that-queries-scale-as-data-grows)
- [427: Does Prisma support table partitioning?](#427-does-prisma-support-table-partitioning)
- [428: How do you handle very wide tables or JSON heavy rows?](#428-how-do-you-handle-very-wide-tables-or-json-heavy-rows)
- [429: What is the effect of Prisma's dataloader on findUnique with different selects?](#429-what-is-the-effect-of-prismas-dataloader-on-findunique-with-different-selects)
- [430: How do you make Prisma Client work in a browser or React Native?](#430-how-do-you-make-prisma-client-work-in-a-browser-or-react-native)
- [431: How do you restrict which fields an API can sort or filter by?](#431-how-do-you-restrict-which-fields-an-api-can-sort-or-filter-by)
- [432: How do you protect against denial of service through expensive Prisma queries?](#432-how-do-you-protect-against-denial-of-service-through-expensive-prisma-queries)
- [433: How should you store secrets like the database URL for Prisma?](#433-how-should-you-store-secrets-like-the-database-url-for-prisma)
- [434: How do you design error handling for Prisma in a large codebase?](#434-how-do-you-design-error-handling-for-prisma-in-a-large-codebase)
- [435: What happens to the client if the database restarts?](#435-what-happens-to-the-client-if-the-database-restarts)
- [436: How do you implement a health check that uses Prisma?](#436-how-do-you-implement-a-health-check-that-uses-prisma)
- [437: How do you make sure a Prisma based service starts only when the database schema is ready?](#437-how-do-you-make-sure-a-prisma-based-service-starts-only-when-the-database-schema-is-ready)
- [438: How would you test a client extension?](#438-how-would-you-test-a-client-extension)
- [439: What are the trade-offs of putting business logic in database triggers versus Prisma extensions?](#439-what-are-the-trade-offs-of-putting-business-logic-in-database-triggers-versus-prisma-extensions)
- [440: How do you handle time based data like events with high write volume?](#440-how-do-you-handle-time-based-data-like-events-with-high-write-volume)
- [441: How do you handle unique constraints across case variations, like emails?](#441-how-do-you-handle-unique-constraints-across-case-variations-like-emails)
- [442: How do you use Prisma with Next.js Server Components and Server Actions?](#442-how-do-you-use-prisma-with-nextjs-server-components-and-server-actions)
- [443: How do you keep Prisma queries out of the edge middleware in Next.js?](#443-how-do-you-keep-prisma-queries-out-of-the-edge-middleware-in-nextjs)
- [444: How would you explain the difference between Prisma's schema first approach and a code first approach?](#444-how-would-you-explain-the-difference-between-prismas-schema-first-approach-and-a-code-first-approach)
- [445: How do you plan a Prisma 6 to 7 upgrade in a big production app?](#445-how-do-you-plan-a-prisma-6-to-7-upgrade-in-a-big-production-app)
- [446: Why might query results differ slightly after moving to driver adapters?](#446-why-might-query-results-differ-slightly-after-moving-to-driver-adapters)
- [447: What metrics would you monitor for a Prisma based service?](#447-what-metrics-would-you-monitor-for-a-prisma-based-service)
- [448: How would you onboard a team that is new to Prisma?](#448-how-would-you-onboard-a-team-that-is-new-to-prisma)
- [449: What are the most common mistakes developers make with Prisma?](#449-what-are-the-most-common-mistakes-developers-make-with-prisma)
- [450: What is your overall approach to using Prisma well in production?](#450-what-is-your-overall-approach-to-using-prisma-well-in-production)

---

# Easy Questions (1-150)

## 1: What is Prisma ORM?

Prisma ORM is an open source ORM for Node.js and TypeScript. You describe your data in a schema file, and Prisma generates a fully typed client that you use to read and write data. It also has a migration tool that turns schema changes into SQL migrations.

It works with PostgreSQL, MySQL, MariaDB, SQLite, SQL Server, CockroachDB and MongoDB (MongoDB is supported in Prisma 6, not yet in Prisma 7).

## 2: What is an ORM?

ORM stands for Object Relational Mapper. It lets you work with database rows as objects in your programming language instead of writing SQL strings by hand. The ORM turns your method calls into SQL, runs them, and maps the results back to objects.

Prisma is a bit different from classic ORMs like TypeORM or Sequelize. It does not use model classes with methods on them. Queries return plain JavaScript objects, and the types come from the schema file.

## 3: What are the main parts of Prisma ORM?

- **Prisma Client**: the generated, type safe query builder you use in your app code
- **Prisma Migrate**: the migration tool that creates and applies SQL migrations from your schema
- **Prisma Studio**: a GUI in the browser for viewing and editing data
- **Prisma CLI**: the `prisma` command that runs all of the above (`init`, `generate`, `migrate`, `studio`, and so on)

## 4: What is the Prisma schema?

The Prisma schema is a file (usually `prisma/schema.prisma`) where you define your database connection, the client generator, and your data models. It is the single source of truth for both Prisma Client and Prisma Migrate.

```prisma
generator client {
  provider = "prisma-client"
  output   = "../src/generated/prisma"
}

datasource db {
  provider = "postgresql"
}

model User {
  id    Int     @id @default(autoincrement())
  email String  @unique
  name  String?
}
```

## 5: Which databases does Prisma support?

Prisma 7 supports PostgreSQL, MySQL, MariaDB, SQLite, SQL Server and CockroachDB. It also works with hosted services built on these, such as Neon, Supabase, PlanetScale, Turso and Cloudflare D1, through driver adapters.

MongoDB is supported by Prisma 6. Prisma 7 does not support MongoDB yet, so MongoDB projects should stay on version 6 for now.

## 6: How do you install Prisma in a project?

You install two packages: the CLI as a dev dependency and the client as a normal dependency. In Prisma 7 you also install a driver adapter for your database.

```bash
npm install prisma --save-dev
npm install @prisma/client @prisma/adapter-pg dotenv
```

Then run `npx prisma init` to create the starting files.

## 7: What does prisma init do?

`npx prisma init` sets up Prisma in the current folder. It creates:

- `prisma/schema.prisma` with a generator and a datasource block
- a Prisma config file (`prisma.config.ts`, or `prisma7.config.ts` in the newest 7.x CLI) that holds the database URL and paths
- a `.env` file with a `DATABASE_URL` placeholder

You can pick the database with a flag, for example `npx prisma init --datasource-provider postgresql`.

## 8: What is the prisma.config.ts file?

It is a TypeScript config file for the Prisma CLI. It tells the CLI where the schema is, where migrations live, which command seeds the database and which database URL to use for migrations and introspection.

```ts
import "dotenv/config";
import { defineConfig, env } from "prisma/config";

export default defineConfig({
  schema: "prisma/schema.prisma",
  migrations: {
    path: "prisma/migrations",
    seed: "tsx prisma/seed.ts",
  },
  datasource: {
    url: env("DATABASE_URL"),
  },
});
```

In Prisma 7 the database URL moved out of `schema.prisma` and into this file.

## 9: What is the generator block?

The generator block tells Prisma what to generate when you run `prisma generate`. For Prisma Client in Prisma 7 it looks like this:

```prisma
generator client {
  provider = "prisma-client"
  output   = "../src/generated/prisma"
}
```

`provider` picks the generator and `output` sets the folder for the generated code. In Prisma 7 `output` is required, because the client is no longer generated into `node_modules`.

## 10: What is the datasource block?

The datasource block says which database type you use. In Prisma 7 it usually only has the provider:

```prisma
datasource db {
  provider = "postgresql"
}
```

The connection URL now lives in `prisma.config.ts` for the CLI and in the driver adapter for your app. In Prisma 6 and older you will still see `url = env("DATABASE_URL")` inside this block.

## 11: What is a model in Prisma?

A model describes one entity in your app, like a user or a post. In a relational database each model maps to a table, and each field maps to a column (or to a relation).

```prisma
model Post {
  id        Int      @id @default(autoincrement())
  title     String
  published Boolean  @default(false)
  createdAt DateTime @default(now())
}
```

Prisma Client then gets a `prisma.post` property with methods like `findMany` and `create`.

## 12: What scalar types does Prisma support?

- `String`
- `Boolean`
- `Int`
- `BigInt`
- `Float`
- `Decimal`
- `DateTime`
- `Json`
- `Bytes`
- `Unsupported("...")` for database types Prisma does not know about

Each type maps to a default database type, and you can change that with native type attributes like `@db.VarChar(255)`.

## 13: What do the ? and [] modifiers mean on a field?

`?` makes a field optional, so it can be `null`. `[]` makes a field a list.

```prisma
model User {
  id    Int      @id
  name  String?   // can be null
  tags  String[]  // list of strings (PostgreSQL, CockroachDB)
  posts Post[]    // list of related posts
}
```

You cannot combine them. A list field cannot be optional (`String[]?` is not allowed).

## 14: What is the @id attribute?

`@id` marks the field that is the primary key of the model. Every model needs either a field with `@id`, a composite `@@id`, or at least one `@unique` field.

```prisma
model User {
  id Int @id @default(autoincrement())
}
```

## 15: What does @default do?

`@default` sets a default value used when you don't pass one on create. It can be a fixed value or a function.

```prisma
model Post {
  id        String   @id @default(uuid())
  views     Int      @default(0)
  status    Status   @default(DRAFT)
  createdAt DateTime @default(now())
}
```

Common functions are `autoincrement()`, `uuid()`, `cuid()`, `ulid()`, `nanoid()`, `now()` and `dbgenerated("...")`.

## 16: What is the difference between autoincrement(), uuid() and cuid()?

- `autoincrement()` makes the database generate a sequence of integers (1, 2, 3 ...). Short and fast, but easy to guess.
- `uuid()` makes Prisma generate a UUID string. `uuid(7)` gives a time ordered version 7 UUID, which works better for indexes than random v4 UUIDs.
- `cuid()` makes Prisma generate a CUID, a collision resistant string id. `cuid(2)` uses the newer CUID2 format.

`uuid()` and `cuid()` values are generated by Prisma Client, not by the database. If you want the database to create the value, use `@default(dbgenerated("gen_random_uuid()"))` on PostgreSQL.

## 17: What does @unique do?

`@unique` adds a unique constraint to a field, so no two rows can have the same value. Unique fields can also be used in `findUnique`, `update`, `delete` and `upsert` where clauses.

```prisma
model User {
  id    Int    @id @default(autoincrement())
  email String @unique
}
```

## 18: What does @updatedAt do?

`@updatedAt` makes Prisma Client set the field to the current time every time the record is updated through Prisma.

```prisma
model Post {
  id        Int      @id @default(autoincrement())
  updatedAt DateTime @updatedAt
}
```

It is done by Prisma, not by the database. If you update the row with raw SQL or from another tool, the value will not change unless you set it yourself.

## 19: What do @map and @@map do?

They let you use different names in Prisma than in the database. `@map` renames a column and `@@map` renames a table.

```prisma
model User {
  id        Int    @id @default(autoincrement())
  firstName String @map("first_name")

  @@map("users")
}
```

In code you use `prisma.user` and `firstName`, but the table is `users` and the column is `first_name`. This is useful when the database uses snake_case.

## 20: What is the difference between field attributes and block attributes?

Field attributes start with one `@` and apply to a single field, like `@id`, `@unique` or `@default`. Block attributes start with `@@` and apply to the whole model, like `@@id`, `@@unique`, `@@index` and `@@map`.

```prisma
model Like {
  userId Int
  postId Int

  @@id([userId, postId])
  @@index([postId])
}
```

## 21: How do you define an enum?

```prisma
enum Role {
  USER
  ADMIN
}

model User {
  id   Int  @id @default(autoincrement())
  role Role @default(USER)
}
```

On PostgreSQL this creates a real enum type. On MySQL it uses the `ENUM` column type. On SQLite and SQL Server, Prisma checks the values in the client, since those databases have no enum type. In code you can import the enum from the generated client: `import { Role } from "./generated/prisma/enums"`.

## 22: What is a relation in Prisma?

A relation is a link between two models. In the database it is a foreign key. In the Prisma schema it is defined with relation fields on both models and the `@relation` attribute on the side that holds the foreign key.

```prisma
model User {
  id    Int    @id @default(autoincrement())
  posts Post[]
}

model Post {
  id       Int  @id @default(autoincrement())
  author   User @relation(fields: [authorId], references: [id])
  authorId Int
}
```

`authorId` is the real column. `author` and `posts` are relation fields that only exist in Prisma.

## 23: What is the difference between a relation field and a scalar field?

A scalar field maps to a real column, like `authorId Int`. A relation field, like `author User` or `posts Post[]`, does not exist in the database. It only exists in Prisma so you can query and write related records.

## 24: How do you define a one-to-one relation?

You put a unique foreign key on one side.

```prisma
model User {
  id      Int      @id @default(autoincrement())
  profile Profile?
}

model Profile {
  id     Int  @id @default(autoincrement())
  bio    String
  user   User @relation(fields: [userId], references: [id])
  userId Int  @unique
}
```

The `@unique` on `userId` is what makes it one-to-one. Without it, one user could have many profiles. The back relation (`profile Profile?`) must be optional.

## 25: How do you define a one-to-many relation?

The "many" side holds the foreign key, and the "one" side has a list field.

```prisma
model User {
  id    Int    @id @default(autoincrement())
  posts Post[]
}

model Post {
  id       Int  @id @default(autoincrement())
  author   User @relation(fields: [authorId], references: [id])
  authorId Int
}
```

## 26: How do you define a many-to-many relation?

The simplest way is an implicit many-to-many relation. You just add list fields on both sides.

```prisma
model Post {
  id         Int        @id @default(autoincrement())
  categories Category[]
}

model Category {
  id    Int    @id @default(autoincrement())
  posts Post[]
}
```

Prisma creates and manages a join table for you (named `_CategoryToPost`). If you need extra columns on the join table, use an explicit many-to-many relation with your own join model.

## 27: What does prisma generate do?

`npx prisma generate` reads your schema and generates Prisma Client code into the folder set by `output`. You need to run it every time you change the schema, otherwise the client types will be out of date.

In Prisma 7, `migrate dev` and `db push` no longer run `generate` for you, so you run it yourself after a schema change.

## 28: How do you create a Prisma Client instance in Prisma 7?

You import `PrismaClient` from the generated folder and pass it a driver adapter.

```ts
import "dotenv/config";
import { PrismaClient } from "./generated/prisma/client";
import { PrismaPg } from "@prisma/adapter-pg";

const adapter = new PrismaPg({ connectionString: process.env.DATABASE_URL });
export const prisma = new PrismaClient({ adapter });
```

In older versions you imported from `@prisma/client` and created it with `new PrismaClient()` and no adapter.

## 29: What is a driver adapter?

A driver adapter connects Prisma Client to a normal JavaScript database driver, like `pg` for PostgreSQL or `better-sqlite3` for SQLite. Prisma builds the query and the driver sends it to the database.

In Prisma 7 driver adapters are required for SQL databases. Examples:

- `@prisma/adapter-pg` (PostgreSQL with `pg`)
- `@prisma/adapter-neon` (Neon serverless driver)
- `@prisma/adapter-mariadb` (MySQL and MariaDB)
- `@prisma/adapter-better-sqlite3` and `@prisma/adapter-libsql` (SQLite, Turso)
- `@prisma/adapter-mssql` (SQL Server)
- `@prisma/adapter-planetscale` and `@prisma/adapter-d1`

## 30: How do you read all records of a model?

Use `findMany` with no arguments.

```ts
const users = await prisma.user.findMany();
```

It returns an array of plain objects. If there are no rows, you get an empty array, not `null`.

## 31: What is the difference between findUnique and findFirst?

`findUnique` finds one record by a unique field or the primary key. The `where` must contain a unique field.

`findFirst` finds the first record that matches any filter. You can use any fields and also `orderBy`.

```ts
const user = await prisma.user.findUnique({
  where: { email: "ann@example.com" },
});

const latest = await prisma.post.findFirst({
  where: { published: true },
  orderBy: { createdAt: "desc" },
});
```

Both return `null` when nothing is found.

## 32: What do findUniqueOrThrow and findFirstOrThrow do?

They work like `findUnique` and `findFirst`, but instead of returning `null` they throw an error when no record is found. The error is a `PrismaClientKnownRequestError` with code `P2025`.

```ts
const user = await prisma.user.findUniqueOrThrow({ where: { id: 1 } });
```

They replaced the old `rejectOnNotFound` option, which was removed in Prisma 5.

## 33: How do you create a record?

```ts
const user = await prisma.user.create({
  data: {
    email: "ann@example.com",
    name: "Ann",
  },
});
```

`create` returns the new record, including fields that got default values, like `id` and `createdAt`.

## 34: How do you create many records at once?

Use `createMany`. It inserts all rows in one query and returns a count.

```ts
const result = await prisma.user.createMany({
  data: [{ email: "a@example.com" }, { email: "b@example.com" }],
  skipDuplicates: true,
});
console.log(result.count);
```

`skipDuplicates` skips rows that would break a unique constraint. It is not supported on SQLite, SQL Server or MongoDB. If you need the created rows back, use `createManyAndReturn` (PostgreSQL, CockroachDB, SQLite).

## 35: How do you update a record?

Use `update` with a unique `where` and the new `data`.

```ts
const user = await prisma.user.update({
  where: { id: 1 },
  data: { name: "Ann Smith" },
});
```

Only the fields you pass in `data` are changed. If no record matches, it throws a `P2025` error.

## 36: How do you update many records?

```ts
const result = await prisma.post.updateMany({
  where: { authorId: 1 },
  data: { published: false },
});
console.log(result.count);
```

`updateMany` accepts any filter and returns the number of updated rows, not the rows themselves. If you need the rows, use `updateManyAndReturn` (PostgreSQL, CockroachDB, SQLite).

## 37: What is an upsert?

Upsert means "update if it exists, otherwise insert".

```ts
const user = await prisma.user.upsert({
  where: { email: "ann@example.com" },
  update: { name: "Ann" },
  create: { email: "ann@example.com", name: "Ann" },
});
```

The `where` must use a unique field. If a record matches, `update` is applied. If not, `create` is used.

## 38: How do you delete records?

```ts
// delete one by unique field, throws P2025 if not found
await prisma.user.delete({ where: { id: 1 } });

// delete all that match, returns { count }
await prisma.post.deleteMany({ where: { published: false } });

// delete every row of the table
await prisma.post.deleteMany();
```

## 39: How do you count records?

```ts
const total = await prisma.user.count();

const admins = await prisma.user.count({
  where: { role: "ADMIN" },
});
```

## 40: What does select do?

`select` picks which fields come back. Only the selected fields are returned, and the return type changes to match.

```ts
const users = await prisma.user.findMany({
  select: { id: true, email: true },
});
// type: { id: number; email: string }[]
```

Selecting only what you need means less data from the database and over the network.

## 41: What does include do?

`include` loads related records together with the main record.

```ts
const user = await prisma.user.findUnique({
  where: { id: 1 },
  include: { posts: true },
});
// user.posts is an array of posts
```

`include` returns all scalar fields plus the relations you asked for. `select` returns only what you list.

## 42: Can you use select and include together?

Not at the same level. Prisma throws an error if you pass both `select` and `include` in the same object. But you can nest them: use `select` at the top and select a relation inside it, or use `include` at the top and `select` inside a relation.

```ts
const user = await prisma.user.findUnique({
  where: { id: 1 },
  include: {
    posts: { select: { id: true, title: true } },
  },
});
```

## 43: What does omit do?

`omit` is the opposite of `select`. It returns all fields except the ones you list.

```ts
const user = await prisma.user.findUnique({
  where: { id: 1 },
  omit: { password: true },
});
```

It is handy for hiding sensitive fields like password hashes. You can also set `omit` globally when you create the client. It became stable in Prisma 6.2.

## 44: How do you filter records with where?

You pass an object with field names and the values or conditions you want.

```ts
const posts = await prisma.post.findMany({
  where: {
    published: true,
    authorId: 5,
    views: { gt: 100 },
  },
});
```

When you list several fields, they are combined with AND.

## 45: What filter operators does Prisma have?

- `equals`, `not`
- `in`, `notIn`
- `lt`, `lte`, `gt`, `gte`
- `contains`, `startsWith`, `endsWith` (for strings)
- `mode: "insensitive"` for case insensitive search (PostgreSQL and MongoDB)

```ts
const users = await prisma.user.findMany({
  where: {
    email: { endsWith: "@example.com" },
    age: { gte: 18, lt: 65 },
    role: { in: ["ADMIN", "EDITOR"] },
  },
});
```

## 46: How do you use AND, OR and NOT?

```ts
const posts = await prisma.post.findMany({
  where: {
    OR: [
      { title: { contains: "prisma" } },
      { content: { contains: "prisma" } },
    ],
    NOT: { published: false },
  },
});
```

`AND` and `OR` take arrays of conditions. `NOT` takes a condition or an array of conditions.

## 47: How do you sort results?

Use `orderBy`.

```ts
const posts = await prisma.post.findMany({
  orderBy: { createdAt: "desc" },
});

// sort by more than one field
const users = await prisma.user.findMany({
  orderBy: [{ lastName: "asc" }, { firstName: "asc" }],
});
```

## 48: How do you paginate with take and skip?

`take` limits how many records come back, and `skip` skips a number of records. Together they give offset pagination.

```ts
const page = 3;
const pageSize = 20;

const posts = await prisma.post.findMany({
  skip: (page - 1) * pageSize,
  take: pageSize,
  orderBy: { id: "asc" },
});
```

Always add an `orderBy`, otherwise the order of rows is not guaranteed.

## 49: How do you get distinct values?

Use `distinct` with a list of fields.

```ts
const cities = await prisma.user.findMany({
  distinct: ["city"],
  select: { city: true },
});
```

By default Prisma does the distinct step in memory after fetching. With the `nativeDistinct` preview feature it uses `DISTINCT ON` in the database where possible.

## 50: How do you filter by a related record?

For a list relation, use `some`, `every` or `none`. For a single relation, use `is` or `isNot`.

```ts
// users who have at least one published post
const users = await prisma.user.findMany({
  where: { posts: { some: { published: true } } },
});

// posts whose author is an admin
const posts = await prisma.post.findMany({
  where: { author: { is: { role: "ADMIN" } } },
});
```

## 51: How do you create a record together with related records?

This is called a nested write. You put the related data inside the `data` object.

```ts
const user = await prisma.user.create({
  data: {
    email: "ann@example.com",
    posts: {
      create: [{ title: "First post" }, { title: "Second post" }],
    },
  },
  include: { posts: true },
});
```

Prisma runs the whole nested write in one transaction, so either everything is saved or nothing is.

## 52: How do you connect a record to an existing related record?

Use `connect` with a unique field of the existing record.

```ts
const post = await prisma.post.create({
  data: {
    title: "Hello",
    author: { connect: { id: 1 } },
  },
});
```

You can also just set the foreign key directly: `data: { title: "Hello", authorId: 1 }`. Both work, but you cannot mix the two styles in the same `data` object.

## 53: How do you remove a relation between records?

Use `disconnect` for optional relations and `set` to replace a whole list.

```ts
// remove one category from a post (many-to-many)
await prisma.post.update({
  where: { id: 1 },
  data: { categories: { disconnect: { id: 3 } } },
});

// replace all categories
await prisma.post.update({
  where: { id: 1 },
  data: { categories: { set: [{ id: 4 }, { id: 5 }] } },
});
```

`disconnect` does not delete the related record. It only removes the link.

## 54: What is Prisma Migrate?

Prisma Migrate is the tool that keeps your database structure in sync with your schema. When you change the schema, it compares it with the current state, writes a SQL migration file, and applies it.

The migration files are plain SQL in `prisma/migrations`. You commit them to git, so every environment gets the same changes in the same order.

## 55: What does prisma migrate dev do?

`npx prisma migrate dev` is the command you use during development. It:

1. Checks the migration history against the database, using a temporary shadow database.
2. Creates a new migration from your schema changes, if there are any.
3. Applies pending migrations to your development database.

```bash
npx prisma migrate dev --name add_user_role
```

In Prisma 7 it no longer runs `prisma generate` or the seed script, so you run those yourself. Never use `migrate dev` in production.

## 56: What does prisma migrate deploy do?

`npx prisma migrate deploy` applies all pending migrations from `prisma/migrations` to the database. It does not create new migrations, does not reset anything and does not use a shadow database.

This is the command you run in production and CI/CD pipelines.

## 57: What does prisma db push do?

`npx prisma db push` makes the database match your schema directly, without creating migration files. It is good for prototyping and for quick local work.

Because it does not keep a history, it is not a good fit for production. If a change would lose data, it warns you and asks for confirmation.

## 58: What is the difference between migrate dev and db push?

- `migrate dev` creates SQL migration files and keeps a history. Use it when you want versioned, repeatable changes.
- `db push` changes the database directly with no files and no history. Use it for prototypes or throwaway databases.

A common pattern is to use `db push` while you are still figuring out the schema, then switch to `migrate dev` once the design is stable.

## 59: What does prisma migrate reset do?

`npx prisma migrate reset` drops the database (or all its tables), creates it again, and applies all migrations from scratch. All data is lost.

It is only meant for development. In Prisma 7 it no longer runs the seed script automatically, so run `npx prisma db seed` after it if you need data.

## 60: What is Prisma Studio?

Prisma Studio is a visual editor for your data. You open it with:

```bash
npx prisma studio
```

It opens in the browser and lets you browse tables, filter rows, edit values and follow relations. It is useful for checking data while developing.

## 61: What is introspection?

Introspection means reading an existing database and generating Prisma models from it. You run:

```bash
npx prisma db pull
```

Prisma reads the tables, columns, keys and indexes and writes the models into your schema file. It is the usual first step when you add Prisma to a project that already has a database.

## 62: When would you use db pull?

- You are adding Prisma to an existing database.
- Someone else changes the database outside of Prisma (for example a DBA or another service) and you need to update your schema.
- You want to check what the real database looks like compared to your schema.

After `db pull` you usually rename models and fields with `@map` and `@@map` so they follow your naming in code.

## 63: What does prisma format do?

`npx prisma format` formats the schema file (spacing and alignment) and also adds missing back relation fields when it can. It is like Prettier for `schema.prisma`. Many editors run it on save through the Prisma VS Code extension.

## 64: What does prisma validate do?

`npx prisma validate` checks your schema for errors without generating anything or touching the database. It is a quick check you can run in CI.

## 65: How do you seed a database?

You write a seed script and point to it in `prisma.config.ts`.

```ts
// prisma.config.ts
export default defineConfig({
  migrations: {
    path: "prisma/migrations",
    seed: "tsx prisma/seed.ts",
  },
  // ...
});
```

```ts
// prisma/seed.ts
import { prisma } from "../src/db";

async function main() {
  await prisma.user.upsert({
    where: { email: "admin@example.com" },
    update: {},
    create: { email: "admin@example.com", role: "ADMIN" },
  });
}

main().finally(() => prisma.$disconnect());
```

Then run `npx prisma db seed`. In Prisma 6 and older the seed command was set in `package.json` under `"prisma": { "seed": "..." }`.

## 66: Why should seed scripts use upsert?

If the seed uses `create`, running it twice fails on unique constraints or makes duplicate rows. With `upsert`, running the seed again just updates or skips the existing rows. That makes the seed safe to run many times.

## 67: How are environment variables loaded in Prisma 7?

Prisma 7 does not load `.env` files on its own anymore. You load them yourself, usually with `dotenv`:

```ts
import "dotenv/config";
```

You add this at the top of `prisma.config.ts` (for the CLI) and at the entry point of your app. Bun loads `.env` files automatically, so Bun users can skip it.

## 68: What is the env() helper in prisma.config.ts?

`env("DATABASE_URL")` from `prisma/config` reads an environment variable in a type safe way and throws a clear error if it is missing. It does not load the `.env` file. You still need `dotenv` or something similar for that.

## 69: What is a migration file?

A migration is a folder inside `prisma/migrations` with a timestamp and a name, like `20260101120000_add_role`. Inside it is a `migration.sql` file with the SQL that changes the database.

```sql
-- CreateEnum
CREATE TYPE "Role" AS ENUM ('USER', 'ADMIN');

-- AlterTable
ALTER TABLE "User" ADD COLUMN "role" "Role" NOT NULL DEFAULT 'USER';
```

You can read and edit this SQL before applying it.

## 70: What is the _prisma_migrations table?

It is a table that Prisma Migrate creates in your database to track which migrations have been applied. It stores the migration name, a checksum of the SQL file, when it started and finished, and whether it failed.

Prisma uses it to know which migrations are pending and to detect if an applied migration file was changed later.

## 71: What is the migration_lock.toml file?

It is a file in `prisma/migrations` that stores the database provider, for example `provider = "postgresql"`. It stops you from applying migrations made for one database type to another one by mistake. You commit it to git with the migrations.

## 72: How do you store JSON data with Prisma?

Use the `Json` type.

```prisma
model Event {
  id      Int  @id @default(autoincrement())
  payload Json
}
```

```ts
await prisma.event.create({
  data: { payload: { type: "click", x: 10, y: 20 } },
});
```

On PostgreSQL it maps to `jsonb`. On SQLite it is stored as text, and JSON filtering is more limited.

## 73: How does Prisma handle dates?

The `DateTime` type maps to the database's date/time type and comes back as a JavaScript `Date` object. Prisma stores and returns dates in UTC.

```ts
await prisma.post.create({
  data: { title: "Hi", publishAt: new Date("2026-12-01T09:00:00Z") },
});
```

You can pass a `Date` object or an ISO 8601 string.

## 74: What is the Decimal type used for?

`Decimal` is for exact numbers like money, where floating point errors are not acceptable. Prisma returns it as a `Prisma.Decimal` object (based on decimal.js), not as a plain number.

```prisma
model Product {
  id    Int     @id @default(autoincrement())
  price Decimal @db.Decimal(10, 2)
}
```

```ts
const total = product.price.mul(3); // use Decimal methods, not *
```

## 75: What is the BigInt type used for?

`BigInt` is for integers bigger than what a JavaScript `number` can safely hold (more than 2^53 - 1). Prisma returns these values as JavaScript `bigint`.

```ts
const row = await prisma.counter.create({ data: { value: 9007199254740993n } });
```

Watch out: `JSON.stringify` throws on `bigint` values, so you need to convert them before sending them in an API response.

## 76: What is the Bytes type used for?

`Bytes` stores binary data, like small files or hashes. In Prisma 6 and 7 it is returned as a `Uint8Array` (older versions used Node's `Buffer`). For large files it is usually better to store them in object storage like S3 and keep only the URL in the database.

## 77: What are native type attributes?

They let you choose the exact database column type instead of the default one.

```prisma
model User {
  id        String   @id @default(uuid()) @db.Uuid
  name      String   @db.VarChar(100)
  bio       String   @db.Text
  createdAt DateTime @default(now()) @db.Timestamptz(6)
}
```

The `db` prefix is the name of your datasource block. Available types depend on the database provider.

## 78: How do you add an index?

Use `@@index` on the model.

```prisma
model Post {
  id        Int      @id @default(autoincrement())
  authorId  Int
  createdAt DateTime

  @@index([authorId])
  @@index([authorId, createdAt])
}
```

Prisma Migrate creates the index in the next migration. Primary keys and `@unique` fields already have an index.

## 79: How do you make a combination of fields unique?

Use `@@unique`.

```prisma
model Membership {
  id     Int @id @default(autoincrement())
  userId Int
  teamId Int

  @@unique([userId, teamId])
}
```

Now a user can only join the same team once. You can query by it with the generated compound name:

```ts
await prisma.membership.findUnique({
  where: { userId_teamId: { userId: 1, teamId: 2 } },
});
```

## 80: How do you define a composite primary key?

Use `@@id` with the list of fields.

```prisma
model PostTag {
  postId Int
  tagId  Int

  @@id([postId, tagId])
}
```

In queries you refer to it as `postId_tagId`, or you can give it your own name with `@@id(name: "postTagId", [postId, tagId])`.

## 81: How do you write comments in the Prisma schema?

There are two kinds:

```prisma
// normal comment, only for people reading the file

/// doc comment, added to the generated client types as JSDoc
model User {
  /// The user's login email
  email String @unique
}
```

Doc comments (`///`) show up when you hover over fields in your editor.

## 82: What is the Prisma VS Code extension?

It is the official extension for `.prisma` files. It gives syntax highlighting, autocomplete, error checking, formatting on save, and "go to definition" for models. Most teams install it because the schema is much easier to write with it.

## 83: How do you check which Prisma version you are using?

```bash
npx prisma -v
```

It prints the versions of the CLI, the client and other related packages. Keep `prisma` and `@prisma/client` on the same version, otherwise you can get strange errors.

## 84: What are the basic aggregate functions in Prisma?

`aggregate` gives you `_count`, `_avg`, `_sum`, `_min` and `_max`.

```ts
const stats = await prisma.order.aggregate({
  where: { status: "PAID" },
  _sum: { total: true },
  _avg: { total: true },
  _count: true,
});
console.log(stats._sum.total, stats._avg.total, stats._count);
```

## 85: What does groupBy do?

`groupBy` groups rows by one or more fields and lets you run aggregates per group, like `GROUP BY` in SQL.

```ts
const byCountry = await prisma.user.groupBy({
  by: ["country"],
  _count: { _all: true },
  orderBy: { country: "asc" },
});
```

You can filter groups with `having`, for example only countries with more than 10 users.

## 86: How do you count related records?

Use `_count` inside `include` or `select`.

```ts
const users = await prisma.user.findMany({
  include: {
    _count: { select: { posts: true } },
  },
});
// users[0]._count.posts
```

This counts in the database without loading the related posts.

## 87: How do you increment a number field?

Use atomic number operations in `data`.

```ts
await prisma.post.update({
  where: { id: 1 },
  data: { views: { increment: 1 } },
});
```

You also have `decrement`, `multiply`, `divide` and `set`. These run as one SQL statement, so two requests at the same time will not overwrite each other.

## 88: What is the PrismaClient $connect method for?

`$connect()` opens the connection to the database. You usually don't need to call it, because Prisma connects on the first query. Calling it at app start can still be useful to fail fast if the database is not reachable.

## 89: What is the $disconnect method for?

`$disconnect()` closes the database connections. You call it at the end of scripts, seeds and tests so the Node.js process can exit. In a long running server you usually don't call it on every request, only on shutdown.

```ts
main()
  .catch((e) => {
    console.error(e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
```

## 90: Why should you create only one PrismaClient instance?

Each `PrismaClient` has its own connection pool. If you create a new client in every request or file, you open many pools and can run out of database connections. The usual pattern is to create one client in a module and import it everywhere.

## 91: What is a transaction?

A transaction is a group of database operations that either all succeed or all fail. If one step fails, the earlier steps are rolled back. A classic example is a money transfer: taking money from one account and adding it to another must happen together.

## 92: How do you run several queries in one transaction?

The simplest way is to pass an array of queries to `$transaction`.

```ts
const [post, count] = await prisma.$transaction([
  prisma.post.create({ data: { title: "Hi", authorId: 1 } }),
  prisma.post.count(),
]);
```

The queries run in order inside one transaction. If any of them fails, all are rolled back.

## 93: What is a raw query in Prisma?

A raw query lets you write SQL yourself when Prisma's API is not enough.

```ts
const users = await prisma.$queryRaw`
  SELECT id, email FROM "User" WHERE age > ${18}
`;
```

`$queryRaw` returns rows. `$executeRaw` is for statements that change data and returns the number of affected rows. The tagged template syntax turns `${...}` into safe parameters, so it is safe from SQL injection.

## 94: What is the difference between $queryRaw and $executeRaw?

- `$queryRaw` is for `SELECT` and anything that returns rows. It returns an array of results.
- `$executeRaw` is for `INSERT`, `UPDATE`, `DELETE` and DDL. It returns a number: how many rows were affected.

```ts
const affected = await prisma.$executeRaw`
  UPDATE "User" SET active = false WHERE "lastLogin" < ${cutoff}
`;
```

## 95: What is the error code P2002?

`P2002` means a unique constraint failed. For example, you tried to create a user with an email that already exists. You can catch it and return a friendly message.

```ts
import { Prisma } from "./generated/prisma/client";

try {
  await prisma.user.create({ data: { email } });
} catch (e) {
  if (e instanceof Prisma.PrismaClientKnownRequestError && e.code === "P2002") {
    throw new Error("Email is already taken");
  }
  throw e;
}
```

## 96: What is the error code P2025?

`P2025` means a record that the operation needed was not found. You get it from `update`, `delete`, `findUniqueOrThrow`, `findFirstOrThrow` and nested `connect` when the record does not exist. APIs often map it to a 404 response.

## 97: What is the Prisma namespace?

`Prisma` is an object you import from the generated client. It holds helper types and values, such as:

- input types like `Prisma.UserCreateInput` and `Prisma.UserWhereInput`
- error classes like `Prisma.PrismaClientKnownRequestError`
- SQL helpers like `Prisma.sql` and `Prisma.join`
- special values like `Prisma.JsonNull`, `Prisma.DbNull` and `Prisma.Decimal`

```ts
import { Prisma } from "./generated/prisma/client";
```

## 98: How do you get the TypeScript type of a model?

The generated client exports a type for each model with the same name.

```ts
import type { User, Post } from "./generated/prisma/client";

function greet(user: User) {
  return `Hello ${user.name ?? "there"}`;
}
```

This type only has scalar fields. For a type that includes relations, use `Prisma.UserGetPayload<...>`.

## 99: What are the type safety benefits of Prisma Client?

- Every query is checked at compile time. A typo in a field name is a TypeScript error.
- Return types match what you asked for. If you `select` two fields, the result type has only those two fields.
- Your editor autocompletes models, fields, filters and relations.
- When you change the schema and regenerate, TypeScript shows every place in your code that breaks.

## 100: Is Prisma Client only for TypeScript?

No, you can use it from plain JavaScript too, and you still get autocomplete in editors that read the types. But the main benefit of Prisma is type safety, so most projects use it with TypeScript. The new `prisma-client` generator in Prisma 7 outputs TypeScript files, so a JavaScript project needs a build step or a runtime that can run TypeScript.

## 101: What is the difference between null and undefined in Prisma queries?

- `null` is a real value. `where: { name: null }` finds rows where `name` is null, and `data: { name: null }` sets the column to null.
- `undefined` means "do nothing". `where: { name: undefined }` is ignored, and `data: { name: undefined }` leaves the field unchanged.

This matters a lot: if a filter value is accidentally `undefined`, the filter disappears and the query can match many more rows than you expected.

## 102: How do you check if a field is null or not null?

```ts
// name is null
await prisma.user.findMany({ where: { name: null } });

// name is not null
await prisma.user.findMany({ where: { name: { not: null } } });
```

## 103: How do you do a case insensitive search?

On PostgreSQL (and MongoDB) add `mode: "insensitive"`.

```ts
const users = await prisma.user.findMany({
  where: {
    name: { contains: "ann", mode: "insensitive" },
  },
});
```

On MySQL and SQL Server, searches are usually case insensitive already because of the default collation, so `mode` is not available there. On SQLite, `contains` is case insensitive only for ASCII characters.

## 104: What are scalar lists?

A scalar list is a field that holds an array of simple values, like `String[]` or `Int[]`.

```prisma
model Post {
  id   Int      @id @default(autoincrement())
  tags String[]
}
```

They are supported on PostgreSQL, CockroachDB and MongoDB. On MySQL and SQLite you need a separate table or a `Json` field instead.

## 105: How do you filter on a scalar list?

```ts
// posts with the tag "prisma"
await prisma.post.findMany({ where: { tags: { has: "prisma" } } });

// posts with at least one of these tags
await prisma.post.findMany({ where: { tags: { hasSome: ["orm", "sql"] } } });

// posts with all of these tags
await prisma.post.findMany({ where: { tags: { hasEvery: ["orm", "sql"] } } });

// posts with no tags
await prisma.post.findMany({ where: { tags: { isEmpty: true } } });
```

## 106: How do you add a value to a scalar list?

Use `push`.

```ts
await prisma.post.update({
  where: { id: 1 },
  data: { tags: { push: "typescript" } },
});
```

To replace the whole list, pass the new array or use `set`.

## 107: What is the PrismaClient log option?

It makes Prisma print logs for the levels you choose: `query`, `info`, `warn` and `error`.

```ts
const prisma = new PrismaClient({
  adapter,
  log: ["query", "warn", "error"],
});
```

Logging `query` prints every SQL statement, which is very helpful for learning what Prisma does and for finding slow or repeated queries.

## 108: Where is Prisma Client generated in Prisma 7?

In the folder set by `output` in the generator block, for example `src/generated/prisma`. You then import from that folder:

```ts
import { PrismaClient } from "./generated/prisma/client";
```

In Prisma 6 and older, with the `prisma-client-js` generator, the client was generated into `node_modules/.prisma/client` and imported from `@prisma/client`.

## 109: Should you commit the generated Prisma Client to git?

Usually no. The generated folder can be recreated at any time with `prisma generate`, so most teams add it to `.gitignore` and run `prisma generate` in their build or CI step.

```gitignore
src/generated/prisma
```

## 110: What is the difference between prisma-client and prisma-client-js?

- `prisma-client-js` is the old generator. It writes the client into `node_modules` and you import from `@prisma/client`. It is being phased out.
- `prisma-client` is the new generator and the default in Prisma 7. It writes plain TypeScript files into a folder you choose, has no Rust engine binary, and works better with bundlers, ESM and edge runtimes.

## 111: What is Prisma Accelerate?

Prisma Accelerate was a hosted service from Prisma that gave you a global connection pool and query caching in front of your database. You connected through a `prisma://` URL.

According to the Prisma 7 upgrade guide, standalone Accelerate is being retired on December 1, 2026, so new projects should not depend on it, and existing users should move to a direct connection with a driver adapter.

## 112: What is Prisma Postgres?

Prisma Postgres is a managed PostgreSQL database run by Prisma. You can connect to it like any PostgreSQL database with `@prisma/adapter-pg`, or use Prisma's own `@prisma/adapter-ppg` driver. You can quickly create a database to try things with `npx create-db`.

## 113: What is the difference between required and optional relations?

If the foreign key is required (`authorId Int`), every post must have an author. If it is optional (`authorId Int?` and `author User?`), a post can exist without an author.

```prisma
model Post {
  id       Int   @id @default(autoincrement())
  author   User? @relation(fields: [authorId], references: [id])
  authorId Int?
}
```

## 114: What does @relation do?

`@relation` describes how a relation is stored. It tells Prisma which local fields hold the foreign key (`fields`) and which fields on the other model they point to (`references`). It can also name the relation and set referential actions.

```prisma
author   User @relation(fields: [authorId], references: [id], onDelete: Cascade)
authorId Int
```

## 115: What does onDelete: Cascade do?

It tells the database to delete the child rows when the parent row is deleted.

```prisma
model Comment {
  id     Int  @id @default(autoincrement())
  post   Post @relation(fields: [postId], references: [id], onDelete: Cascade)
  postId Int
}
```

Deleting a post now also deletes its comments. Without it, deleting a post that has comments fails with a foreign key error.

## 116: What referential actions does Prisma support?

For `onDelete` and `onUpdate` you can use:

- `Cascade`: delete or update the children too
- `Restrict`: block the change if children exist
- `NoAction`: like Restrict, but checked at the end of the statement (details depend on the database)
- `SetNull`: set the foreign key to null (the field must be optional)
- `SetDefault`: set the foreign key to its default value

Not every action is available on every database.

## 117: What is an explicit many-to-many relation?

It is a many-to-many relation where you define the join table as your own model. You need this when the join table has extra data, like when a tag was added.

```prisma
model Post {
  id   Int       @id @default(autoincrement())
  tags PostTag[]
}

model Tag {
  id    Int       @id @default(autoincrement())
  posts PostTag[]
}

model PostTag {
  post    Post     @relation(fields: [postId], references: [id])
  postId  Int
  tag     Tag      @relation(fields: [tagId], references: [id])
  tagId   Int
  addedAt DateTime @default(now())

  @@id([postId, tagId])
}
```

## 118: What is the difference between implicit and explicit many-to-many relations?

- Implicit: you only add list fields on both models. Prisma creates and hides the join table. Queries are shorter, but you cannot add extra columns to the join table.
- Explicit: you define the join model yourself. You can add extra fields like `addedAt` or `role`, but queries go through the join model, so they are a bit longer.

Implicit relations also require both models to have a single field `@id`.

## 119: What is the Unsupported type?

`Unsupported("type")` is used for database column types that Prisma does not support, like PostGIS `geometry`. It usually appears after `db pull`.

```prisma
model Place {
  id       Int                      @id @default(autoincrement())
  location Unsupported("geography")?
}
```

The field is kept in the schema so migrations know about it, but you cannot read or write it with the normal client API. You use raw SQL for it.

## 120: What do @ignore and @@ignore do?

`@ignore` hides a field and `@@ignore` hides a whole model from Prisma Client. The column or table still exists in the database and is still known to migrations. `db pull` adds `@@ignore` to tables that Prisma cannot fully support, for example tables with no unique identifier.

## 121: How do you open the Prisma CLI help?

```bash
npx prisma --help
npx prisma migrate --help
```

Each command has its own help page with all flags.

## 122: What does dbgenerated() do?

`dbgenerated("...")` puts a raw SQL default expression on the column, so the database creates the value instead of Prisma Client.

```prisma
model User {
  id String @id @default(dbgenerated("gen_random_uuid()")) @db.Uuid
}
```

This is useful when rows are also inserted by other tools or raw SQL, since they get the same default.

## 123: What does @default(now()) do?

It sets the field to the current date and time when the record is created. Unlike `@updatedAt`, it does not change on later updates.

```prisma
createdAt DateTime @default(now())
```

## 124: How do you return only some fields of related records?

Use `select` inside the relation.

```ts
const posts = await prisma.post.findMany({
  select: {
    title: true,
    author: { select: { name: true } },
  },
});
```

## 125: How do you filter, sort and limit related records in include?

You can pass query arguments inside `include`.

```ts
const user = await prisma.user.findUnique({
  where: { id: 1 },
  include: {
    posts: {
      where: { published: true },
      orderBy: { createdAt: "desc" },
      take: 5,
    },
  },
});
```

## 126: How do you load nested relations several levels deep?

Nest `include` or `select`.

```ts
const user = await prisma.user.findUnique({
  where: { id: 1 },
  include: {
    posts: {
      include: { comments: { include: { author: true } } },
    },
  },
});
```

Be careful with deep includes on large data sets. They can load a lot of rows.

## 127: How do you delete a record and its related records?

Either set `onDelete: Cascade` on the relation so the database deletes the children, or delete the children first in a transaction.

```ts
await prisma.$transaction([
  prisma.comment.deleteMany({ where: { postId: 1 } }),
  prisma.post.delete({ where: { id: 1 } }),
]);
```

## 128: What does connectOrCreate do?

It connects to an existing related record if one matches, and creates it if not.

```ts
await prisma.post.create({
  data: {
    title: "Hello",
    categories: {
      connectOrCreate: {
        where: { name: "news" },
        create: { name: "news" },
      },
    },
  },
});
```

The `where` must use a unique field.

## 129: How do you check if a record exists?

There is no `exists` method. The common ways are:

```ts
const exists = (await prisma.user.count({ where: { email } })) > 0;

// or, often a bit cheaper
const found = await prisma.user.findFirst({
  where: { email },
  select: { id: true },
});
const exists2 = found !== null;
```

## 130: How do you get the first N records?

Use `take` with an `orderBy`.

```ts
const newest = await prisma.post.findMany({
  orderBy: { createdAt: "desc" },
  take: 10,
});
```

A negative `take` takes records from the end of the list.

## 131: What is a shadow database?

A shadow database is a temporary database that `prisma migrate dev` creates and drops automatically. Prisma applies all your migrations to it to check that they run cleanly and to detect drift between the migration history and your dev database.

It is only used by `migrate dev`, never in production. On some hosted databases you are not allowed to create databases, so you set a `shadowDatabaseUrl` in `prisma.config.ts` instead.

## 132: What is schema drift?

Drift means the database structure no longer matches the migration history. It happens when someone changes the database by hand, or applies changes with `db push` on a database that also uses migrations.

`prisma migrate dev` detects drift and usually asks to reset the development database. `prisma migrate status` also shows migrations that are out of sync.

## 133: What does prisma migrate status do?

It compares the migration files with the `_prisma_migrations` table and tells you which migrations are applied, which are pending, and if any failed.

```bash
npx prisma migrate status
```

It is useful in CI or before a deploy.

## 134: How do you name a migration?

Pass `--name` to `migrate dev`.

```bash
npx prisma migrate dev --name add_post_slug
```

If you don't pass it, the CLI asks you for a name. Use short, clear names that describe the change.

## 135: Can you edit a migration before applying it?

Yes. Run `migrate dev` with `--create-only`. It creates the SQL file but does not apply it. You edit the SQL and then run `migrate dev` again to apply it.

```bash
npx prisma migrate dev --create-only --name rename_column
```

This is how you handle renames, data changes and SQL features that Prisma cannot express in the schema.

## 136: Why should you not edit a migration that was already applied?

Prisma stores a checksum of every applied migration. If you change the file later, the checksum no longer matches. `migrate dev` will report it and may ask to reset the dev database. Other environments end up with different SQL than the file says. If you need to change something, create a new migration.

## 137: What is the difference between Prisma ORM and plain SQL?

With plain SQL you write the queries as strings and map the results yourself. You get full control and every database feature, but no type checking and more boilerplate.

With Prisma you write queries in TypeScript, get typed results and simple migrations, but you are limited to what the Prisma API supports. For the rest you can still drop down to raw SQL.

## 138: What are the main advantages of using Prisma?

- Strong type safety with autocomplete
- One readable schema file for the whole data model
- Simple migrations generated from the schema
- A query API that is easy to learn, including relations and nested writes
- Good docs and tooling (Studio, VS Code extension)

## 139: What are some drawbacks of Prisma?

- Some SQL features are not part of the API (for example window functions or complex joins), so you need raw SQL for them.
- You have to run a generate step after every schema change.
- Queries with many nested includes can be less efficient than a hand written SQL join.
- Large upgrades (like 6 to 7) can bring breaking changes in setup.

## 140: What is the fluent API in Prisma?

It lets you go from a record to its relations by chaining calls.

```ts
const posts = await prisma.user.findUnique({ where: { id: 1 } }).posts();
```

This returns the posts of user 1. If the user does not exist, it returns `null`.

## 141: How do you sort by a field of a related model?

```ts
const posts = await prisma.post.findMany({
  orderBy: { author: { name: "asc" } },
});
```

This works for to-one relations. For to-many relations you can sort by the count, for example `orderBy: { posts: { _count: "desc" } }`.

## 142: How do you control where null values go when sorting?

Use `sort` with `nulls`.

```ts
const users = await prisma.user.findMany({
  orderBy: { lastLogin: { sort: "desc", nulls: "last" } },
});
```

This only works on optional fields and on relational databases.

## 143: What is the difference between update and updateMany?

- `update` changes one record found by a unique field, returns the updated record, and throws `P2025` if it does not exist. It also supports nested writes.
- `updateMany` changes all records that match any filter, returns `{ count }`, and does not throw when nothing matches. It does not support nested writes.

## 144: What is the difference between delete and deleteMany?

- `delete` removes one record by a unique field, returns it, and throws `P2025` if it is not found.
- `deleteMany` removes all records that match a filter, returns `{ count }`, and does not throw if none match.

## 145: Can you run Prisma with SQLite?

Yes. In Prisma 7 you use a SQLite driver adapter, such as `better-sqlite3`.

```ts
import { PrismaClient } from "./generated/prisma/client";
import { PrismaBetterSqlite3 } from "@prisma/adapter-better-sqlite3";

const adapter = new PrismaBetterSqlite3({ url: "file:./dev.db" });
const prisma = new PrismaClient({ adapter });
```

SQLite is great for local development, tests and small apps.

## 146: Can you have more than one schema file?

Yes. Since Prisma 6.7 you can split the schema into many `.prisma` files in one folder, for example one file per area of your app. You point the config to the folder:

```ts
export default defineConfig({
  schema: "prisma/schema",
});
```

Prisma reads all `.prisma` files in that folder as one schema, and models in different files can relate to each other.

## 147: What is the Prisma CLI command to create the client after cloning a project?

Install packages and generate the client:

```bash
npm install
npx prisma generate
```

Many projects add `prisma generate` to a `postinstall` script or to the build script so nobody forgets it.

## 148: What does createManyAndReturn do?

It inserts many rows like `createMany`, but returns the created records instead of a count. It is available on PostgreSQL, CockroachDB and SQLite.

```ts
const users = await prisma.user.createManyAndReturn({
  data: [{ email: "a@example.com" }, { email: "b@example.com" }],
  select: { id: true, email: true },
});
```

## 149: Does Prisma work with Express, NestJS and Next.js?

Yes. Prisma Client is just a Node.js library, so it works with any server framework. You create one client instance and import it where you need it. Frameworks like NestJS often wrap it in a service, and Next.js projects keep it in a module like `lib/prisma.ts`.

## 150: What changed in Prisma 7 at a high level?

- The new `prisma-client` generator is the default, and `output` is required.
- Prisma Client no longer uses a Rust query engine. It uses a query compiler and a driver adapter.
- Driver adapters are required for SQL databases.
- Database URLs and seed config moved to `prisma.config.ts`.
- `.env` files are not loaded automatically.
- The package is ESM, and it needs Node.js 20.19+ and TypeScript 5.4+.
- Client middleware (`$use`) and the metrics preview were removed.
- MongoDB is not supported yet, so MongoDB projects stay on Prisma 6.

# Moderate Questions (151-300)

## 151: How do you set up Prisma 7 in a new TypeScript project from scratch?

```bash
npm init -y
npm install -D prisma typescript tsx @types/node
npm install @prisma/client @prisma/adapter-pg dotenv
npx prisma init --datasource-provider postgresql
```

Then:

1. Set `"type": "module"` in `package.json`, since Prisma 7 ships as ESM.
2. Put your connection string in `.env` as `DATABASE_URL`.
3. Add models to `prisma/schema.prisma`.
4. Run `npx prisma migrate dev --name init` and then `npx prisma generate`.
5. Create the client with the `PrismaPg` adapter and import it from the generated folder.

## 152: What tsconfig settings work well with Prisma 7?

The Prisma 7 upgrade guide suggests a modern ESM setup:

```json
{
  "compilerOptions": {
    "module": "ESNext",
    "moduleResolution": "bundler",
    "target": "ES2023",
    "strict": true,
    "esModuleInterop": true
  }
}
```

If you use `"module": "NodeNext"` instead, the generator can infer the right module format and import extensions, or you can set `moduleFormat` and `importFileExtension` in the generator block.

## 153: What options does the prisma-client generator have?

```prisma
generator client {
  provider               = "prisma-client"
  output                 = "../src/generated/prisma"
  runtime                = "nodejs"
  moduleFormat           = "esm"
  generatedFileExtension = "ts"
  importFileExtension    = "ts"
}
```

- `output` (required): where the files go
- `runtime`: `nodejs` (default), `deno`, `bun`, `workerd` (Cloudflare), `vercel-edge` or `react-native`
- `moduleFormat`: `esm` or `cjs`
- `generatedFileExtension`: `ts`, `mts` or `cts`
- `importFileExtension`: the extension used in import paths inside the generated code, like `js` or `ts`, or empty for bare imports

## 154: What files does the prisma-client generator create?

```
generated/prisma/
├── client.ts           // PrismaClient, Prisma namespace, model types (server only)
├── browser.ts          // types and enums that are safe for frontend code
├── enums.ts            // enum objects
├── models.ts           // all model types and input types
├── models/User.ts      // types for one model
├── commonInputTypes.ts // shared filter types
└── internal/           // private, do not import from here
```

You import `PrismaClient` from `client`, and only types from `browser`, `models` or `enums` in code that runs in the browser.

## 155: Why does the generated client have a browser.ts file?

`client.ts` includes `PrismaClient` and code that only works on the server. If a frontend file imports a type from it, a bundler can pull server code into the browser bundle.

`browser.ts` exports the same model types and enums without `PrismaClient`, so you can share types like `User` with React components safely.

```ts
import type { User } from "@/generated/prisma/browser";
```

## 156: How do you upgrade a project from Prisma 6 to Prisma 7?

1. Upgrade packages: `npm install @prisma/client@7` and `npm install -D prisma@7`.
2. Change the generator to `provider = "prisma-client"` and add `output`.
3. Move `url`, `directUrl` and `shadowDatabaseUrl` from the datasource block into `prisma.config.ts`.
4. Install a driver adapter and pass it to `new PrismaClient({ adapter })`.
5. Update imports from `@prisma/client` to the generated folder.
6. Load `.env` yourself with `dotenv`.
7. Move to ESM if needed and check Node.js and TypeScript versions.
8. Replace `$use` middleware with client extensions.
9. Add explicit `prisma generate` and `prisma db seed` calls to scripts, since migrate no longer runs them.

## 157: Why did Prisma remove the Rust query engine in Prisma 7?

The Rust engine was a separate binary (or native library) that had to match the OS and CPU. That caused problems with large bundles, cold starts in serverless, edge runtimes that cannot run native code, and Docker images built on a different platform.

Prisma 7 uses a query compiler and runs queries through normal JavaScript database drivers. The result is a smaller client, no platform specific binaries, and easier deployment to serverless and edge platforms.

## 158: What happened to binaryTargets in Prisma 7?

`binaryTargets` was needed with the Rust engine so Prisma could download the right engine for your deploy platform (for example `debian-openssl-3.0.x` or `linux-musl`). With the Rust-free `prisma-client` generator there is no engine binary to download, so you no longer need to set it. You still see it in older projects that use `prisma-client-js`.

## 159: How do you configure the database URL used by migrations?

In Prisma 7 the CLI reads it from the `datasource` section of `prisma.config.ts`.

```ts
export default defineConfig({
  schema: "prisma/schema.prisma",
  datasource: {
    url: env("DATABASE_URL"),
    shadowDatabaseUrl: env("SHADOW_DATABASE_URL"),
  },
});
```

The app itself does not read this file. The app gets its connection through the driver adapter.

## 160: What happened to directUrl in Prisma 7?

`directUrl` was used when the app connected through a pooler (like PgBouncer) but migrations needed a direct connection. In Prisma 7 it was removed from the schema. The CLI now uses the `url` in `prisma.config.ts` for migrations, so you put the direct connection string there and give the pooled connection string to the driver adapter in your app.

## 161: How do you use a different .env file per environment?

Prisma 7 does not load env files itself, so you choose how to load them. Some options:

```ts
// prisma.config.ts
import { config } from "dotenv";
config({ path: process.env.ENV_FILE ?? ".env" });
```

Or use a tool like `dotenv-cli`:

```bash
npx dotenv -e .env.test -- npx prisma migrate deploy
```

Node.js 20.6+ also has a built in `--env-file` flag for app code.

## 162: How do you share a single Prisma Client in a Next.js app?

In development, hot reload re-runs modules, which can create a new client each time and use up connections. The common fix is to keep the client on `globalThis`.

```ts
// lib/prisma.ts
import { PrismaClient } from "@/generated/prisma/client";
import { PrismaPg } from "@prisma/adapter-pg";

const globalForPrisma = globalThis as unknown as { prisma?: PrismaClient };

const adapter = new PrismaPg({ connectionString: process.env.DATABASE_URL });

export const prisma = globalForPrisma.prisma ?? new PrismaClient({ adapter });

if (process.env.NODE_ENV !== "production") globalForPrisma.prisma = prisma;
```

## 163: How do you use Prisma in NestJS?

Create a service that extends `PrismaClient` and register it in a module.

```ts
import { Injectable, OnModuleInit, OnModuleDestroy } from "@nestjs/common";
import { PrismaClient } from "../generated/prisma/client";
import { PrismaPg } from "@prisma/adapter-pg";

@Injectable()
export class PrismaService
  extends PrismaClient
  implements OnModuleInit, OnModuleDestroy
{
  constructor() {
    super({
      adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL }),
    });
  }

  async onModuleInit() {
    await this.$connect();
  }

  async onModuleDestroy() {
    await this.$disconnect();
  }
}
```

Then inject `PrismaService` into other services and call `this.prisma.user.findMany()`.

## 164: How do you use Prisma in an Express app?

Create one client in its own module and import it in routes.

```ts
import express from "express";
import { prisma } from "./db";

const app = express();
app.use(express.json());

app.get("/users/:id", async (req, res, next) => {
  try {
    const user = await prisma.user.findUnique({
      where: { id: Number(req.params.id) },
    });
    if (!user) return res.status(404).json({ error: "Not found" });
    res.json(user);
  } catch (e) {
    next(e);
  }
});

app.listen(3000);
```

## 165: How do you do cursor based pagination?

Pass a `cursor` with a unique field, skip the cursor row itself, and take the next page.

```ts
const page = await prisma.post.findMany({
  take: 20,
  skip: lastId ? 1 : 0,
  ...(lastId && { cursor: { id: lastId } }),
  orderBy: { id: "asc" },
});

const nextCursor = page.length === 20 ? page[page.length - 1].id : null;
```

The client sends back `nextCursor` to get the next page.

## 166: When should you use cursor pagination instead of offset pagination?

Offset pagination (`skip` and `take`) is simple and lets users jump to page 37, but the database still has to walk through all the skipped rows, so deep pages get slow. Rows added or removed between requests can also cause items to repeat or be missed.

Cursor pagination is fast at any depth because it uses an index to start right after the last row. It fits infinite scroll and APIs well. The downside is that you cannot jump to a random page.

## 167: What is an interactive transaction?

It is a transaction where you get a transaction client (`tx`) and can run any code between queries, including reading a value and deciding what to do next.

```ts
await prisma.$transaction(async (tx) => {
  const from = await tx.account.update({
    where: { id: fromId },
    data: { balance: { decrement: amount } },
  });

  if (from.balance.lessThan(0)) {
    throw new Error("Not enough money");
  }

  await tx.account.update({
    where: { id: toId },
    data: { balance: { increment: amount } },
  });
});
```

If the function throws, everything is rolled back. You must use `tx`, not `prisma`, inside the callback.

## 168: What options can you pass to an interactive transaction?

```ts
import { Prisma } from "./generated/prisma/client";

await prisma.$transaction(
  async (tx) => {
    // ...
  },
  {
    maxWait: 5000, // how long to wait to get a connection (default 2000 ms)
    timeout: 10000, // how long the transaction can run (default 5000 ms)
    isolationLevel: Prisma.TransactionIsolationLevel.Serializable,
  },
);
```

You can also set default values for all transactions with the `transactionOptions` option of `PrismaClient`.

## 169: What isolation levels can you set in Prisma transactions?

- `ReadUncommitted`
- `ReadCommitted`
- `RepeatableRead`
- `Serializable`
- `Snapshot` (SQL Server only)

Which ones you can use depends on the database. If you don't set it, the database default is used (for example Read Committed on PostgreSQL and Repeatable Read on MySQL).

## 170: When should you use a batch $transaction([]) instead of an interactive one?

Use the array form when the queries don't depend on each other's results. It is simpler and keeps the transaction short.

Use an interactive transaction when you need to read data, check something in code, and then write based on it. Keep interactive transactions short, because they hold a database connection and locks for the whole time.

## 171: What happens if you use prisma instead of tx inside an interactive transaction?

The query runs outside the transaction on a different connection. It is not rolled back if the transaction fails, and it cannot see uncommitted changes made through `tx`. In some cases it can even deadlock, because it waits for a lock that the transaction holds. Always use the `tx` argument inside the callback.

## 172: Are nested writes transactional?

Yes. A single `create`, `update` or `upsert` with nested `create`, `connect`, `update` and so on runs inside one transaction. If one nested step fails, the whole operation is rolled back. So for "create an order with its items" you often don't need `$transaction` at all.

## 173: How do you update a record and its related records in one call?

Use nested writes in `update`.

```ts
await prisma.user.update({
  where: { id: 1 },
  data: {
    name: "Ann",
    profile: {
      upsert: {
        create: { bio: "Hello" },
        update: { bio: "Hello" },
      },
    },
    posts: {
      updateMany: {
        where: { published: false },
        data: { published: true },
      },
    },
  },
});
```

## 174: What nested write operations are available?

Depending on the relation type you can use:

- `create`, `createMany`
- `connect`, `connectOrCreate`
- `disconnect`, `set`
- `update`, `updateMany`, `upsert`
- `delete`, `deleteMany`

For example, `set` and `createMany` only make sense on to-many relations, and `disconnect: true` is for optional to-one relations.

## 175: What is the difference between checked and unchecked inputs?

Checked inputs (`Prisma.PostCreateInput`) use relation fields, like `author: { connect: { id: 1 } }`. Unchecked inputs (`Prisma.PostUncheckedCreateInput`) let you set foreign key columns directly, like `authorId: 1`.

Prisma accepts either one, but not both in the same object. Unchecked inputs are shorter, while checked inputs allow nested writes.

## 176: How do you get the type of a query result with relations?

Use the `GetPayload` helper.

```ts
import { Prisma } from "./generated/prisma/client";

type UserWithPosts = Prisma.UserGetPayload<{
  include: { posts: true };
}>;
```

Now `UserWithPosts` has all user fields plus `posts: Post[]`.

## 177: How do you reuse a select or include object with full type safety?

Use `satisfies` with the generated type. This keeps the exact shape of the object, so the result type is still correct.

```ts
import { Prisma } from "./generated/prisma/client";

const userPreview = {
  id: true,
  name: true,
  email: true,
} satisfies Prisma.UserSelect;

type UserPreview = Prisma.UserGetPayload<{ select: typeof userPreview }>;

const users = await prisma.user.findMany({ select: userPreview });
```

## 178: What are client extensions?

Client extensions let you add your own behavior to Prisma Client with `$extends`. There are four kinds:

- `model`: add custom methods to models
- `query`: change or wrap queries
- `result`: add computed fields to results
- `client`: add top level methods to the client

`$extends` returns a new client and does not change the original one.

## 179: How do you add a custom method to a model?

```ts
const xprisma = prisma.$extends({
  model: {
    user: {
      async findByEmail(email: string) {
        return prisma.user.findUnique({ where: { email } });
      },
    },
  },
});

const user = await xprisma.user.findByEmail("ann@example.com");
```

For a method that works on any model, put it under `$allModels` and use `Prisma.getExtensionContext(this)` to get the current model.

## 180: How do you add a computed field with a result extension?

```ts
const xprisma = prisma.$extends({
  result: {
    user: {
      fullName: {
        needs: { firstName: true, lastName: true },
        compute(user) {
          return `${user.firstName} ${user.lastName}`;
        },
      },
    },
  },
});

const user = await xprisma.user.findFirst();
console.log(user?.fullName);
```

`needs` tells Prisma which fields to load so the field can be computed. It is calculated when the result is read, not stored in the database.

## 181: How do you wrap all queries with a query extension?

```ts
const xprisma = prisma.$extends({
  query: {
    $allModels: {
      async $allOperations({ model, operation, args, query }) {
        const start = performance.now();
        const result = await query(args);
        console.log(
          `${model}.${operation} took ${performance.now() - start} ms`,
        );
        return result;
      },
    },
  },
});
```

`query(args)` runs the original query. You can change `args` before calling it or change the result after.

## 182: What replaced middleware ($use) in Prisma 7?

Query extensions. `$use` was deprecated for a long time and removed in Prisma 7. The same logic moves into `$extends({ query: ... })`.

```ts
// old
prisma.$use(async (params, next) => {
  return next(params);
});

// new
const xprisma = prisma.$extends({
  query: {
    $allModels: {
      async $allOperations({ args, query }) {
        return query(args);
      },
    },
  },
});
```

Extensions are also type safe and can be scoped to one model or operation.

## 183: How do you combine multiple extensions?

Chain `$extends` calls, or define each extension with `Prisma.defineExtension` and apply them in order.

```ts
import { Prisma } from "./generated/prisma/client";

const logging = Prisma.defineExtension({
  name: "logging",
  query: {
    $allModels: {
      async $allOperations({ args, query }) {
        return query(args);
      },
    },
  },
});

const xprisma = prisma.$extends(logging).$extends(softDelete);
```

The extensions run in order. Later extensions wrap the earlier ones.

## 184: How do you implement soft delete with Prisma?

Add a `deletedAt` field and filter on it. A simple version uses a query extension to hide deleted rows from reads.

```prisma
model Post {
  id        Int       @id @default(autoincrement())
  title     String
  deletedAt DateTime?
}
```

```ts
const xprisma = prisma.$extends({
  query: {
    post: {
      async findMany({ args, query }) {
        args.where = { ...args.where, deletedAt: null };
        return query(args);
      },
    },
  },
  model: {
    post: {
      async softDelete(id: number) {
        return prisma.post.update({
          where: { id },
          data: { deletedAt: new Date() },
        });
      },
    },
  },
});
```

In real projects you also need to cover `findFirst`, `count`, relations and unique constraints, so soft delete needs care.

## 185: How do you add a top level method with a client extension?

```ts
const xprisma = prisma.$extends({
  client: {
    async $healthCheck() {
      await prisma.$queryRaw`SELECT 1`;
      return true;
    },
  },
});

await xprisma.$healthCheck();
```

## 186: How do you log queries as events?

Use `emit: "event"` and subscribe with `$on`.

```ts
const prisma = new PrismaClient({
  adapter,
  log: [{ emit: "event", level: "query" }, "warn", "error"],
});

prisma.$on("query", (e) => {
  console.log(e.query);
  console.log(e.params);
  console.log(`${e.duration} ms`);
});
```

This lets you send query logs to your own logger, or only log slow queries.

## 187: How do you catch Prisma errors properly?

Check the error class and then the code.

```ts
import { Prisma } from "./generated/prisma/client";

try {
  await prisma.user.update({ where: { id }, data });
} catch (e) {
  if (e instanceof Prisma.PrismaClientKnownRequestError) {
    if (e.code === "P2025") return notFound();
    if (e.code === "P2002") return conflict(e.meta);
  }
  if (e instanceof Prisma.PrismaClientValidationError) {
    return badRequest(e.message);
  }
  throw e;
}
```

## 188: What Prisma error classes are there?

- `PrismaClientKnownRequestError`: the database or engine returned a known error with a code like `P2002`
- `PrismaClientUnknownRequestError`: an error without a known code
- `PrismaClientValidationError`: the query is invalid, for example a wrong field type or a missing required field
- `PrismaClientInitializationError`: the client could not start or connect
- `PrismaClientRustPanicError`: a crash in the Rust engine, only relevant to older engine based setups

## 189: What does error code P2003 mean?

`P2003` means a foreign key constraint failed. For example, you created a post with an `authorId` that does not exist, or you tried to delete a user that still has posts and the relation has no cascade. `e.meta` contains details about which constraint failed.

## 190: How do you map Prisma errors to HTTP responses?

Put the mapping in one place, like an error middleware.

```ts
import { Prisma } from "./generated/prisma/client";

export function prismaErrorToHttp(e: unknown) {
  if (e instanceof Prisma.PrismaClientKnownRequestError) {
    switch (e.code) {
      case "P2002":
        return { status: 409, message: "Already exists" };
      case "P2025":
        return { status: 404, message: "Not found" };
      case "P2003":
        return { status: 400, message: "Related record does not exist" };
    }
  }
  return { status: 500, message: "Internal error" };
}
```

Don't send `e.message` to the client in production. It can contain table names and query details.

## 191: How do you write a raw query with dynamic parts safely?

Use `Prisma.sql` to build parts and `Prisma.join` for lists. Values are still sent as parameters.

```ts
import { Prisma } from "./generated/prisma/client";

const ids = [1, 2, 3];
const onlyActive = true;

const users = await prisma.$queryRaw`
  SELECT * FROM "User"
  WHERE id IN (${Prisma.join(ids)})
  ${onlyActive ? Prisma.sql`AND active = true` : Prisma.empty}
`;
```

## 192: What is the danger of $queryRawUnsafe?

`$queryRawUnsafe` takes a normal string, so if you put user input into the string, you get SQL injection.

```ts
// DANGEROUS
await prisma.$queryRawUnsafe(`SELECT * FROM "User" WHERE email = '${email}'`);

// OK: use placeholders and pass values separately
await prisma.$queryRawUnsafe('SELECT * FROM "User" WHERE email = $1', email);
```

Prefer the tagged template `$queryRaw` whenever you can.

## 193: How do you add a type to a raw query result?

Pass a generic type to `$queryRaw`.

```ts
type Row = { id: number; email: string; postCount: bigint };

const rows = await prisma.$queryRaw<Row[]>`
  SELECT u.id, u.email, COUNT(p.id) AS "postCount"
  FROM "User" u LEFT JOIN "Post" p ON p."authorId" = u.id
  GROUP BY u.id
`;
```

Prisma does not check this type. It only trusts you. For checked types, use TypedSQL.

## 194: What is TypedSQL?

TypedSQL lets you write SQL in `.sql` files and get a fully typed function for each query. It is a preview feature (`typedSql`).

```sql
-- prisma/sql/getUsersByAge.sql
-- @param {Int} $1:minAge
SELECT id, email FROM "User" WHERE age >= $1;
```

```bash
npx prisma generate --sql
```

```ts
import { getUsersByAge } from "./generated/prisma/sql";

const users = await prisma.$queryRawTyped(getUsersByAge(18));
```

Prisma connects to the database during generate to work out the parameter and result types.

## 195: Why do COUNT results in raw queries come back as bigint?

On PostgreSQL `COUNT(*)` returns a 64 bit integer, and Prisma maps 64 bit integers to JavaScript `bigint` to avoid losing precision. You can cast it in SQL (`COUNT(*)::int`) or convert it in code with `Number(row.count)` if you know it is small enough.

## 196: How do you send BigInt values in a JSON API response?

`JSON.stringify` throws "Do not know how to serialize a BigInt". Options:

```ts
// convert in the response
res.json({ ...row, total: row.total.toString() });

// or with a replacer
JSON.stringify(data, (_, v) => (typeof v === "bigint" ? v.toString() : v));
```

Some projects patch `BigInt.prototype.toJSON`, but changing a global prototype can surprise other code, so a replacer or explicit conversion is cleaner.

## 197: How do you handle Decimal values in API responses?

`Prisma.Decimal` objects serialize to strings in JSON (for example `"19.99"`). That keeps precision, but the frontend has to treat them as strings or parse them with a decimal library. Avoid converting to `number` for money calculations, because floating point math can give wrong cents.

## 198: How do you filter on JSON fields?

Use `path` and the JSON filters. The syntax is a bit different between PostgreSQL and MySQL.

```ts
// PostgreSQL
const events = await prisma.event.findMany({
  where: {
    payload: { path: ["type"], equals: "click" },
  },
});

// MySQL
const events2 = await prisma.event.findMany({
  where: {
    payload: { path: "$.type", equals: "click" },
  },
});
```

There are also `string_contains`, `array_contains` and similar filters.

## 199: What are Prisma.JsonNull, Prisma.DbNull and Prisma.AnyNull?

A nullable `Json` field can hold two kinds of null: a database `NULL` or a JSON value `null`. Prisma uses special values to tell them apart:

- `Prisma.DbNull`: database NULL
- `Prisma.JsonNull`: the JSON value `null`
- `Prisma.AnyNull`: either one (only for filtering)

```ts
await prisma.event.update({
  where: { id: 1 },
  data: { payload: Prisma.DbNull },
});
await prisma.event.findMany({ where: { payload: { equals: Prisma.AnyNull } } });
```

## 200: How do you type the contents of a Json field?

Prisma types `Json` fields as `JsonValue`, not as your own type. Common options:

- Validate and parse the value with a library like Zod when you read it.
- Use a result extension to return a parsed, typed value.
- Use a community generator like `prisma-json-types-generator` to map JSON fields to your own types.

```ts
import { z } from "zod";

const Settings = z.object({ theme: z.enum(["light", "dark"]) });
const settings = Settings.parse(user.settings);
```

## 201: How do you rename a field without losing data?

If you just rename a field in the schema, Prisma Migrate sees one column removed and one added, and the generated SQL drops the old column with its data.

Two safe options:

- Keep the database column name and only rename in Prisma: `newName String @map("old_name")`.
- Create the migration with `--create-only` and change the SQL to a real rename:

```sql
ALTER TABLE "User" RENAME COLUMN "old_name" TO "new_name";
```

## 202: How do you do a data migration with Prisma?

Prisma Migrate is for schema changes, but you can add data changes in two ways:

- Write SQL in a migration created with `--create-only`, for example an `UPDATE` that fills a new column.
- Run a separate TypeScript script that uses Prisma Client, usually between two schema migrations.

A common flow for a required column: add it as optional, fill it with data, then make it required in a later migration.

## 203: What does prisma migrate resolve do?

It changes the record of a migration in `_prisma_migrations` without running its SQL.

```bash
# mark a failed migration as rolled back so it can run again after a fix
npx prisma migrate resolve --rolled-back 20260101120000_add_index

# mark a migration as already applied (for example, you applied it by hand)
npx prisma migrate resolve --applied 20260101120000_add_index
```

It is mostly used to fix failed migrations in production and for baselining.

## 204: What is baselining?

Baselining means telling Prisma Migrate that an existing database already matches an initial migration, so it doesn't try to create all the tables again. You use it when you add Prisma Migrate to a database that already has data.

```bash
mkdir -p prisma/migrations/0_init
npx prisma migrate diff --from-empty --to-schema prisma/schema.prisma --script > prisma/migrations/0_init/migration.sql
npx prisma migrate resolve --applied 0_init
```

After that, new migrations are applied on top as usual.

## 205: What does prisma migrate diff do?

`migrate diff` compares two states of a schema and prints the difference, either as a summary or as SQL with `--script`. The sources can be an empty schema, a schema file, a migrations folder, or the database from the config.

```bash
# SQL needed to go from the live database to the schema file
npx prisma migrate diff \
  --from-config-datasource \
  --to-schema prisma/schema.prisma \
  --script
```

In Prisma 7 the old `--from-url` and `--to-url` flags were replaced by `--from-config-datasource` and `--to-config-datasource`.

## 206: How do you run a SQL file against the database with the Prisma CLI?

Use `prisma db execute`.

```bash
npx prisma db execute --file ./scripts/fix-data.sql
```

In Prisma 7 the connection comes from `prisma.config.ts`. The old `--url` and `--schema` flags were removed.

## 207: How do you run migrations in a CI/CD pipeline?

A typical deploy job:

```bash
npm ci
npx prisma generate
npx prisma migrate deploy
npm run build
```

Run `migrate deploy` once per deploy, not from every app instance at start up, so several instances don't race. Use a direct database connection for it, not a pooled one.

## 208: How do you check for missing migrations in CI?

You can fail the build if the schema has changes that have no migration. One way is to compare the migrations folder with the schema:

```bash
npx prisma migrate diff \
  --from-migrations prisma/migrations \
  --to-schema prisma/schema.prisma \
  --exit-code
```

`--exit-code` makes the command return a non zero exit code if there is a difference. Comparing against a migrations folder needs a shadow database to be configured.

## 209: How do you use Prisma with Docker?

- Run `prisma generate` during the image build so the generated client is in the image.
- Run `prisma migrate deploy` as a separate step or init container before the app starts.
- Pass `DATABASE_URL` as an environment variable at run time, not baked into the image.

```dockerfile
FROM node:22-slim
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npx prisma generate && npm run build
CMD ["node", "dist/index.js"]
```

With the Rust-free client in Prisma 7 you no longer need to worry about engine binaries and OpenSSL versions in the image.

## 210: How do you test code that uses Prisma with unit tests?

Mock the client so tests don't need a database. With Vitest you can use `vitest-mock-extended`:

```ts
import { mockDeep } from "vitest-mock-extended";
import type { PrismaClient } from "../generated/prisma/client";

const prismaMock = mockDeep<PrismaClient>();

prismaMock.user.findUnique.mockResolvedValue({
  id: 1,
  email: "a@example.com",
  name: null,
});

const user = await getUser(prismaMock, 1);
expect(user.email).toBe("a@example.com");
```

This works best if your functions receive the client as a parameter or through dependency injection.

## 211: How do you write integration tests with a real database?

- Start a test database, for example with Docker or Testcontainers.
- Run `prisma migrate deploy` (or `migrate reset --force`) against it before the tests.
- Clean the data between tests with `deleteMany` or `TRUNCATE ... CASCADE`.
- Point the test run to it with a separate `DATABASE_URL`.

Integration tests catch problems mocks cannot, like wrong constraints, missing indexes and real SQL errors.

## 212: How do you clean the database between tests?

```ts
beforeEach(async () => {
  await prisma.$executeRawUnsafe(
    'TRUNCATE TABLE "Comment", "Post", "User" RESTART IDENTITY CASCADE',
  );
});
```

Or delete in the right order with `deleteMany`, children first. Some teams run each test in a transaction that is rolled back at the end, but that is harder to set up with Prisma, since the code under test has to use the same transaction client.

## 213: How do you seed different data per environment?

Read an environment variable or an argument in the seed script.

```ts
async function main() {
  await seedRoles();
  if (process.env.SEED_DEMO_DATA === "true") {
    await seedDemoUsers();
  }
}
```

Arguments after `--` in `npx prisma db seed -- --demo` are passed to the seed script, so you can read them with `process.argv`.

## 214: How do you define a self relation?

A model that relates to itself, like an employee with a manager.

```prisma
model Employee {
  id        Int        @id @default(autoincrement())
  name      String
  managerId Int?
  manager   Employee?  @relation("Management", fields: [managerId], references: [id])
  reports   Employee[] @relation("Management")
}
```

Both sides use the same relation name so Prisma knows they belong together.

## 215: How do you define two relations between the same two models?

Give each relation a name so Prisma can tell them apart.

```prisma
model User {
  id            Int    @id @default(autoincrement())
  writtenPosts  Post[] @relation("WrittenPosts")
  pinnedPosts   Post[] @relation("PinnedPosts")
}

model Post {
  id         Int   @id @default(autoincrement())
  author     User  @relation("WrittenPosts", fields: [authorId], references: [id])
  authorId   Int
  pinnedBy   User? @relation("PinnedPosts", fields: [pinnedById], references: [id])
  pinnedById Int?
}
```

## 216: How do you model a many-to-many self relation, like followers?

```prisma
model User {
  id         Int    @id @default(autoincrement())
  followers  User[] @relation("Follows")
  following  User[] @relation("Follows")
}
```

This is an implicit relation with a hidden join table. If you need data like "followed at", use an explicit `Follow` model with `followerId` and `followingId`.

## 217: What is relationMode = "prisma"?

By default Prisma creates real foreign keys in the database. With `relationMode = "prisma"` it does not create them and instead checks relations in Prisma Client.

```prisma
datasource db {
  provider     = "mysql"
  relationMode = "prisma"
}
```

It was made for databases that don't support foreign keys, like older PlanetScale setups. The downsides are that the database no longer protects your data, and you need to add `@@index` on foreign key fields yourself, because there is no foreign key index anymore.

## 218: How do you use multiple database schemas in PostgreSQL?

Use the `schemas` field on the datasource and `@@schema` on models. This is stable since Prisma 6.13.

```prisma
datasource db {
  provider = "postgresql"
  schemas  = ["public", "auth"]
}

model User {
  id Int @id @default(autoincrement())

  @@schema("auth")
}

model Post {
  id Int @id @default(autoincrement())

  @@schema("public")
}
```

It works with PostgreSQL, CockroachDB and SQL Server.

## 219: How do you map a database view in Prisma?

Database views are a preview feature (`views`). You create the view with SQL in a migration and describe it with the `view` keyword.

```prisma
generator client {
  provider        = "prisma-client"
  output          = "../src/generated/prisma"
  previewFeatures = ["views"]
}

view UserStats {
  userId    Int @unique
  postCount Int
}
```

```ts
const stats = await prisma.userStats.findMany();
```

Views are read only. Prisma Migrate does not create the view for you, so you write the `CREATE VIEW` statement yourself.

## 220: How do you enable a preview feature?

Add it to `previewFeatures` in the generator block and run `prisma generate` again.

```prisma
generator client {
  provider        = "prisma-client"
  output          = "../src/generated/prisma"
  previewFeatures = ["relationJoins", "fullTextSearchPostgres"]
}
```

Preview features can change between versions, so check the release notes when you upgrade.

## 221: What is relationLoadStrategy?

It picks how Prisma loads relations in `include` and `select`. It needs the `relationJoins` preview feature and works on PostgreSQL and MySQL.

- `"join"` (default when the preview is on): one SQL query with joins (PostgreSQL uses `LATERAL` joins and JSON aggregation).
- `"query"`: one query per table, then Prisma joins the results in the client.

```ts
const users = await prisma.user.findMany({
  relationLoadStrategy: "join",
  include: { posts: true },
});
```

## 222: When is the "query" load strategy better than "join"?

`join` sends one query, which saves round trips and is often faster when the database is far away. But joining a big one-to-many relation repeats or aggregates lots of data, and very deep includes can make heavy queries.

`query` sends simple queries per table, which can be cheaper when parent rows have many children or when the database is close to the app. Measure with your real data before choosing.

## 223: How do you do full text search with Prisma?

On PostgreSQL there is the `fullTextSearchPostgres` preview feature, which adds a `search` filter.

```ts
const posts = await prisma.post.findMany({
  where: { title: { search: "cat & dog" } },
});
```

On MySQL, full text search has been stable since Prisma 6. You add a `@@fulltext([title, content])` index and use the same `search` filter. For serious search needs, many teams use raw SQL with `tsvector` and a GIN index, or a dedicated search engine.

## 224: How do you create a GIN index on a JSON or array column in PostgreSQL?

Use `@@index` with `type: Gin`.

```prisma
model Post {
  id   Int      @id @default(autoincrement())
  tags String[]
  meta Json

  @@index([tags], type: Gin)
  @@index([meta(ops: JsonbPathOps)], type: Gin)
}
```

Other index types on PostgreSQL are `BTree` (default), `Hash`, `Gist`, `SpGist` and `Brin`.

## 225: How do you set the sort order of an index?

```prisma
model Post {
  id        Int      @id @default(autoincrement())
  createdAt DateTime

  @@index([createdAt(sort: Desc)])
}
```

This helps queries that always sort by newest first, especially in composite indexes.

## 226: How do you give an index or constraint a custom name?

Use `map` (for the database name) or `name` (for the Prisma Client name on unique constraints).

```prisma
model Membership {
  userId Int
  teamId Int

  @@unique([userId, teamId], name: "member", map: "membership_user_team_key")
  @@index([teamId], map: "membership_team_idx")
}
```

```ts
await prisma.membership.findUnique({
  where: { member: { userId: 1, teamId: 2 } },
});
```

## 227: What are field references?

Field references let you compare a field to another field of the same model in a filter.

```ts
const lowStock = await prisma.product.findMany({
  where: {
    quantity: { lte: prisma.product.fields.reorderLevel },
  },
});
```

Both fields must have the same type.

## 228: How do you filter by the count of related records?

You cannot filter by `_count` directly in `where`. Common workarounds:

- Use `orderBy: { posts: { _count: "desc" } }` and `take` if you need the top N.
- Use `groupBy` on the child table with `having`, then query the parents by id.
- Use raw SQL with `GROUP BY ... HAVING COUNT(*) > 5`.

```ts
const groups = await prisma.post.groupBy({
  by: ["authorId"],
  _count: { _all: true },
  having: { authorId: { _count: { gt: 5 } } },
});
const ids = groups.map((g) => g.authorId);
const authors = await prisma.user.findMany({ where: { id: { in: ids } } });
```

## 229: How do you count only some related records?

Add a `where` inside `_count`.

```ts
const users = await prisma.user.findMany({
  select: {
    name: true,
    _count: {
      select: { posts: { where: { published: true } } },
    },
  },
});
```

## 230: How do you set omit globally?

Pass `omit` when you create the client. Every query will leave out those fields unless you ask for them.

```ts
const prisma = new PrismaClient({
  adapter,
  omit: {
    user: { password: true },
  },
});

// password is not in the result
const user = await prisma.user.findFirst();

// you can still ask for it when you need it
const withPassword = await prisma.user.findFirst({ omit: { password: false } });
```

## 231: What is the strictUndefinedChecks preview feature?

It makes Prisma throw an error when you pass `undefined` explicitly in a query, instead of silently ignoring it. To skip a field on purpose, you use `Prisma.skip`.

```ts
import { Prisma } from "./generated/prisma/client";

await prisma.user.findMany({
  where: { email: input.email ?? Prisma.skip },
});
```

It protects you from bugs where a filter value is `undefined` by mistake and the query matches every row.

## 232: Why is passing undefined in a deleteMany filter dangerous?

```ts
await prisma.session.deleteMany({ where: { userId: req.body.userId } });
```

If `req.body.userId` is missing, the filter becomes `{ userId: undefined }`, Prisma ignores it, and you delete every session in the table. Validate inputs before using them in write queries, and consider `strictUndefinedChecks`.

## 233: How does upsert work under the hood?

When the query meets certain conditions (one unique field in `where`, no nested writes in `update` or `create`, and the same value in `where` and `create`), Prisma uses a native database upsert like `INSERT ... ON CONFLICT DO UPDATE`.

Otherwise Prisma does a select first and then an insert or update. That version can fail with a `P2002` error if two requests try to create the same row at the same time, so you may need to retry.

## 234: How do you do a bulk update with different values per row?

`updateMany` sets the same values on all matching rows. For different values per row you can:

- Run many `update` calls in one `$transaction([...])`.
- Use raw SQL with `UPDATE ... FROM (VALUES ...)` for large batches.

```ts
await prisma.$transaction(
  items.map((item) =>
    prisma.product.update({
      where: { id: item.id },
      data: { price: item.price },
    }),
  ),
);
```

## 235: What does updateManyAndReturn do?

It updates all matching rows and returns them, like `updateMany` but with the records instead of a count. It came in Prisma 6.2 and is available on PostgreSQL, CockroachDB and SQLite.

```ts
const posts = await prisma.post.updateManyAndReturn({
  where: { authorId: 1 },
  data: { published: true },
  select: { id: true, title: true },
});
```

## 236: How do you configure the connection pool in Prisma 7?

The pool belongs to the driver now, so you set the options on the adapter. With `@prisma/adapter-pg` you pass normal `pg` pool settings:

```ts
const adapter = new PrismaPg({
  connectionString: process.env.DATABASE_URL,
  max: 10,
  connectionTimeoutMillis: 5000,
  idleTimeoutMillis: 300_000,
});
```

In Prisma 6 you set pool size with URL parameters like `?connection_limit=10&pool_timeout=20`. Those are for the old engine and do not apply to driver adapters.

## 237: Why might you get connection timeouts after upgrading to Prisma 7?

Driver adapters use the defaults of the underlying driver, which are different from the old engine. For example, `pg` has no connection timeout by default, while Prisma 6 used 5 seconds, and the default pool size is different. Set the pool options on the adapter to match what you had before.

## 238: Why might you get P1010 or SSL errors after upgrading to Prisma 7?

Prisma 7 uses `node-pg` for PostgreSQL, which checks SSL certificates by default. The old engine was more lenient. If your database has a self signed or unknown certificate, the connection fails. The right fix is to give Node the correct CA (with `NODE_EXTRA_CA_CERTS` or the adapter's `ssl` option). Turning off validation with `ssl: { rejectUnauthorized: false }` works but makes man-in-the-middle attacks possible.

## 239: How do you connect to Neon with Prisma?

You can use the normal `pg` adapter with a Neon connection string, or the Neon serverless driver adapter, which works over HTTP or WebSockets in serverless and edge environments.

```ts
import { PrismaClient } from "./generated/prisma/client";
import { PrismaNeon } from "@prisma/adapter-neon";

const adapter = new PrismaNeon({ connectionString: process.env.DATABASE_URL });
const prisma = new PrismaClient({ adapter });
```

For migrations, use Neon's direct (non pooled) connection string in `prisma.config.ts`.

## 240: How do you connect to MySQL or MariaDB in Prisma 7?

Use `@prisma/adapter-mariadb`. It uses the `mariadb` driver, which also works with MySQL.

```ts
import { PrismaClient } from "./generated/prisma/client";
import { PrismaMariaDb } from "@prisma/adapter-mariadb";

const adapter = new PrismaMariaDb({
  host: "localhost",
  user: "app",
  password: process.env.DB_PASSWORD,
  database: "app",
  connectionLimit: 5,
});
const prisma = new PrismaClient({ adapter });
```

The datasource `provider` stays `"mysql"`.

## 241: How do you use Prisma with Cloudflare Workers and D1?

Set the generator runtime for Workers and use the D1 adapter with the D1 binding.

```prisma
generator client {
  provider = "prisma-client"
  output   = "../src/generated/prisma"
  runtime  = "workerd"
}

datasource db {
  provider = "sqlite"
}
```

```ts
import { PrismaClient } from "./generated/prisma/client";
import { PrismaD1 } from "@prisma/adapter-d1";

export default {
  async fetch(request: Request, env: Env) {
    const prisma = new PrismaClient({ adapter: new PrismaD1(env.DB) });
    const users = await prisma.user.findMany();
    return Response.json(users);
  },
};
```

D1 has its own limits, for example on transactions, so check the D1 adapter docs before using interactive transactions.

## 242: How do you run Prisma in serverless functions without running out of connections?

- Create the client outside the handler so warm invocations reuse it.
- Keep the pool small (often 1 to 5) per function instance.
- Put a connection pooler (PgBouncer, Supavisor, Neon's pooler, RDS Proxy) between the functions and the database.
- Or use an HTTP based serverless driver like Neon's or PlanetScale's.

Each function instance has its own pool, so 100 instances with 10 connections each can open 1000 connections.

## 243: How do you use Prisma with PgBouncer?

Point the app's adapter at the PgBouncer URL and point the CLI (`prisma.config.ts`) at the direct database URL, because migrations need a session level connection.

In Prisma 6 and older you had to add `?pgbouncer=true` to the URL in transaction mode, because the Rust engine used named prepared statements. With `@prisma/adapter-pg`, queries go through `node-pg`, which does not use named prepared statements by default. Still, avoid session level features like `SET` or advisory locks outside a transaction in PgBouncer transaction mode.

## 244: What is the OpenTelemetry tracing support in Prisma?

Prisma can create OpenTelemetry spans for each query, so you see database calls in tools like Jaeger, Honeycomb or Datadog. Tracing became stable in Prisma 6.1.

```ts
import { registerInstrumentations } from "@opentelemetry/instrumentation";
import { PrismaInstrumentation } from "@prisma/instrumentation";

registerInstrumentations({
  instrumentations: [new PrismaInstrumentation()],
});
```

You register it before creating the Prisma Client, together with your normal OpenTelemetry SDK setup.

## 245: What happened to the metrics feature?

The `metrics` preview feature (`prisma.$metrics`) was deprecated in Prisma 6.14 and removed in Prisma 7. To get numbers like query counts and durations, use OpenTelemetry tracing, the metrics of your database driver, or a query extension that counts and times queries.

## 246: How do you count queries per request?

You can use a query extension and `AsyncLocalStorage`.

```ts
import { AsyncLocalStorage } from "node:async_hooks";

export const requestStore = new AsyncLocalStorage<{ queries: number }>();

export const xprisma = prisma.$extends({
  query: {
    $allModels: {
      async $allOperations({ args, query }) {
        const store = requestStore.getStore();
        if (store) store.queries++;
        return query(args);
      },
    },
  },
});
```

Wrap each request in `requestStore.run({ queries: 0 }, ...)` and log the count at the end. A high number is a sign of N+1 queries.

## 247: How do you see the SQL that Prisma generates?

Turn on query logging.

```ts
const prisma = new PrismaClient({ adapter, log: ["query"] });
```

You can also use event based logging to print parameters, or look at the database's own logs (for example `log_statement` in PostgreSQL). Setting the `DEBUG` environment variable to `prisma*` prints more internal debug output from the CLI and client.

## 248: How do you return the created record from a nested create with relations?

Use `include` or `select` on the top level call.

```ts
const order = await prisma.order.create({
  data: {
    customerId: 1,
    items: { create: [{ productId: 5, quantity: 2 }] },
  },
  include: { items: true },
});
```

## 249: What is the difference between findMany with take: 1 and findFirst?

They return almost the same data, but `findFirst` returns one object or `null`, while `findMany({ take: 1 })` returns an array with zero or one item. `findFirst` is clearer when you want a single row. In both cases add an `orderBy` if you care which row comes first.

## 250: How do you query records created in a date range?

```ts
const start = new Date("2026-10-01T00:00:00Z");
const end = new Date("2026-11-01T00:00:00Z");

const orders = await prisma.order.findMany({
  where: {
    createdAt: { gte: start, lt: end },
  },
});
```

Use `lt` on the start of the next period instead of `lte` on the last second, so you don't miss values with milliseconds. Be clear about time zones, because Prisma stores and compares in UTC.

## 251: How do you store and query dates without a time part?

Use `@db.Date` on PostgreSQL or MySQL. Prisma still returns a `Date` object, set to midnight UTC.

```prisma
model Holiday {
  id   Int      @id @default(autoincrement())
  day  DateTime @db.Date
  name String
}
```

```ts
await prisma.holiday.findMany({
  where: { day: new Date("2026-12-25") },
});
```

Be careful when you build the `Date` in local time. `new Date(2026, 11, 25)` in a time zone ahead of UTC can turn into the 24th in UTC.

## 252: How do you handle time zones with Prisma?

Store all timestamps in UTC (Prisma does this) and convert to the user's time zone only when you show them. On PostgreSQL, using `@db.Timestamptz` makes the column time zone aware, which helps when other tools read the database. Avoid storing local times without a zone, because you cannot convert them back correctly later.

## 253: How do you change an enum safely?

Adding a value is safe. Removing or renaming a value is risky, because rows may still use it. A safe flow:

1. Add the new value and deploy.
2. Update the rows from the old value to the new one with a data migration.
3. Remove the old value in a later migration.

On PostgreSQL, `ALTER TYPE ... ADD VALUE` cannot always run inside a transaction together with code that uses the new value, so keep enum changes in their own migration.

## 254: How do you map enum values to different names in the database?

Use `@map` on enum values and `@@map` on the enum.

```prisma
enum OrderStatus {
  PENDING  @map("pending")
  SHIPPED  @map("shipped")

  @@map("order_status")
}
```

In code you still use `OrderStatus.PENDING`, and its value is `"PENDING"`. Prisma 7 had planned to change this so the mapped name would be used in code, but that change was reverted, so it works the same as in Prisma 6.

## 255: How do you make a required column from an optional one when the table has data?

If you change `name String?` to `name String`, the migration fails on rows that have `NULL`. Options:

- Give it a default: `name String @default("")`.
- Create the migration with `--create-only` and add an `UPDATE` before the `ALTER COLUMN ... SET NOT NULL`:

```sql
UPDATE "User" SET "name" = 'Unknown' WHERE "name" IS NULL;
ALTER TABLE "User" ALTER COLUMN "name" SET NOT NULL;
```

## 256: How do you add a unique constraint to a column that has duplicates?

The migration will fail until the duplicates are gone. First find them:

```ts
const dups = await prisma.user.groupBy({
  by: ["email"],
  _count: { email: true },
  having: { email: { _count: { gt: 1 } } },
});
```

Fix or merge those rows, then run the migration that adds `@unique`. On big tables you may prefer to create the unique index with SQL `CREATE UNIQUE INDEX CONCURRENTLY` to avoid locking writes.

## 257: How do you work with Prisma in a monorepo?

A common setup is a shared database package:

- `packages/db` holds `schema.prisma`, migrations, `prisma.config.ts` and an exported client.
- Apps import the client from that package, for example `import { prisma } from "@acme/db"`.
- The package's build runs `prisma generate`.

With the new generator, you set `output` inside the package, so every app uses the same generated code and you don't depend on how `node_modules` is hoisted.

## 258: How do you avoid Prisma Client being out of date in CI?

Run `prisma generate` as part of the build, not only locally. Some options:

```json
{
  "scripts": {
    "postinstall": "prisma generate",
    "build": "prisma generate && tsc"
  }
}
```

If the generated folder is in `.gitignore`, a fresh checkout has no client until `generate` runs, so type checking and tests will fail without it.

## 259: How do you use Prisma with GraphQL?

Prisma is used inside resolvers to load data. Things to watch:

- Use `select` based on the fields the client asked for, so you don't load too much.
- Watch out for N+1 queries in nested resolvers. Prisma batches `findUnique` calls made in the same tick, so the fluent API (`prisma.user.findUnique({ where: { id } }).posts()`) helps with this.
- Libraries like Pothos have a Prisma plugin that builds efficient queries from the GraphQL selection.

## 260: How does Prisma batch findUnique queries?

When several `findUnique` calls on the same model run in the same event loop tick, with the same `select` or `include`, Prisma merges them into one `findMany` with `WHERE id IN (...)` and then gives each caller its own result. This works like a built in DataLoader and helps a lot in GraphQL resolvers. It only works for `findUnique`, not for `findFirst` or `findMany`.

## 261: How do you write a repository layer on top of Prisma?

Many teams wrap Prisma calls in small functions or classes per domain.

```ts
export class UserRepository {
  constructor(private readonly db: PrismaClient) {}

  findByEmail(email: string) {
    return this.db.user.findUnique({ where: { email } });
  }

  create(data: Prisma.UserCreateInput) {
    return this.db.user.create({ data });
  }
}
```

This makes it easy to mock in tests and keeps query details out of controllers. Don't hide everything though. Prisma is already a data access layer, and very generic repositories often just repeat its API.

## 262: How do you pass a transaction client to functions?

Type the parameter so it accepts both the normal client and the transaction client.

```ts
import { Prisma } from "./generated/prisma/client";

async function createOrder(db: Prisma.TransactionClient, input: OrderInput) {
  return db.order.create({ data: input });
}

await prisma.$transaction(async (tx) => {
  const order = await createOrder(tx, input);
  await tx.stock.update({
    where: { id: input.productId },
    data: { quantity: { decrement: 1 } },
  });
});
```

`Prisma.TransactionClient` is the type of `tx`. You can also pass the normal `prisma` client to the same function, since it has the same model methods.

## 263: Can you nest $transaction calls?

No. The transaction client `tx` does not have a `$transaction` method, so you cannot start a transaction inside another one. Instead, write your functions so they accept a client, and pass `tx` down from the outer transaction.

## 264: How do you retry a transaction after a write conflict?

Under `Serializable` isolation, or when there are deadlocks, the database may abort a transaction. Prisma returns error `P2034`. Retry a few times:

```ts
async function withRetry<T>(fn: () => Promise<T>, retries = 3): Promise<T> {
  for (let i = 0; ; i++) {
    try {
      return await fn();
    } catch (e) {
      const conflict =
        e instanceof Prisma.PrismaClientKnownRequestError && e.code === "P2034";
      if (!conflict || i >= retries) throw e;
    }
  }
}

await withRetry(() =>
  prisma.$transaction(
    async (tx) => {
      /* ... */
    },
    { isolationLevel: "Serializable" },
  ),
);
```

## 265: How do you lock a row for update in Prisma?

The Prisma API has no `SELECT ... FOR UPDATE`, so use raw SQL inside an interactive transaction.

```ts
await prisma.$transaction(async (tx) => {
  const [account] = await tx.$queryRaw<{ id: number; balance: number }[]>`
    SELECT id, balance FROM "Account" WHERE id = ${id} FOR UPDATE
  `;
  await tx.account.update({
    where: { id },
    data: { balance: account.balance - amount },
  });
});
```

The row stays locked until the transaction ends, so other transactions that try to lock it wait.

## 266: How do you implement optimistic concurrency control?

Add a `version` field. Update only if the version is still the one you read, and increment it.

```ts
const result = await prisma.document.updateMany({
  where: { id: doc.id, version: doc.version },
  data: { content: newContent, version: { increment: 1 } },
});

if (result.count === 0) {
  throw new Error("Someone else changed this document. Reload and try again.");
}
```

`updateMany` is used because `version` is not a unique field. With extended where unique you could also use `update` with `where: { id, version }`, which throws `P2025` on conflict.

## 267: What is extendedWhereUnique?

It is the feature (stable since Prisma 5) that lets you add non unique fields to the `where` of `findUnique`, `update`, `delete` and `upsert`, as long as at least one unique field is there.

```ts
await prisma.post.update({
  where: { id: 1, authorId: currentUserId },
  data: { title: "New title" },
});
```

This is handy for checks like "only update if this post belongs to the current user".

## 268: How do you check that a user owns a record before updating it?

Put the owner in the `where`, so the check and the update are one query.

```ts
const post = await prisma.post.update({
  where: { id: postId, authorId: userId },
  data: { title },
});
```

If the post doesn't exist or belongs to someone else, Prisma throws `P2025` and you return 404. This avoids a race between a separate "check" query and the update.

## 269: How do you select a random row?

Prisma has no random order option. Options:

```ts
// small tables: count and skip
const count = await prisma.quote.count();
const quote = await prisma.quote.findFirst({
  skip: Math.floor(Math.random() * count),
});

// raw SQL on PostgreSQL
const [q] =
  await prisma.$queryRaw`SELECT * FROM "Quote" ORDER BY random() LIMIT 1`;
```

`ORDER BY random()` scans the whole table, so for big tables use a smarter method like picking a random id range.

## 270: How do you query with a LIKE pattern that contains % or _?

Prisma escapes values in `contains`, `startsWith` and `endsWith`, so `contains: "50%"` searches for the text "50%" and does not treat `%` as a wildcard. If you really need custom patterns, use raw SQL with a parameter:

```ts
await prisma.$queryRaw`SELECT * FROM "Product" WHERE name LIKE ${pattern}`;
```

## 271: How do you get the total count and a page of results together?

Run both queries in one transaction so they see the same data.

```ts
const [total, items] = await prisma.$transaction([
  prisma.post.count({ where }),
  prisma.post.findMany({ where, skip, take, orderBy: { id: "desc" } }),
]);
```

On big tables `count` can be slow, so some APIs return only "has next page" instead of the exact total.

## 272: How do you load a list of records by a list of ids?

```ts
const users = await prisma.user.findMany({
  where: { id: { in: ids } },
});
```

The result is not in the same order as `ids`. If order matters, sort it in code:

```ts
const byId = new Map(users.map((u) => [u.id, u]));
const ordered = ids.map((id) => byId.get(id)).filter(Boolean);
```

## 273: How do you write a query that selects users with no posts?

```ts
const users = await prisma.user.findMany({
  where: { posts: { none: {} } },
});
```

`none: {}` means "no related records at all". In the same way, `some: {}` means "at least one".

## 274: What is the difference between every and some on an empty relation?

`every` is true when there are no related records, because "all zero posts are published" is true. `some` is false when there are none. So `where: { posts: { every: { published: true } } }` also returns users with no posts. Add `some: {}` if you want to exclude them.

## 275: How do you count rows per value of a relation in one query?

Use `groupBy` on the child model.

```ts
const counts = await prisma.post.groupBy({
  by: ["authorId"],
  _count: { _all: true },
  orderBy: { _count: { authorId: "desc" } },
  take: 10,
});
```

This gives you the top 10 authors by post count, with only author ids. Load the user records afterwards if you need names.

## 276: Can groupBy include relations?

No. `groupBy` only works with scalar fields of one model, and you cannot use `include` or `select` relations in it. If you need related data, run a second query with the ids from the groups, or use raw SQL with a join.

## 277: How do you get the newest post per user?

Prisma doesn't have a direct "top 1 per group" helper. Options:

```ts
// load users with their latest post
const users = await prisma.user.findMany({
  include: { posts: { orderBy: { createdAt: "desc" }, take: 1 } },
});

// PostgreSQL: DISTINCT ON with raw SQL
const latest = await prisma.$queryRaw`
  SELECT DISTINCT ON ("authorId") * FROM "Post"
  ORDER BY "authorId", "createdAt" DESC
`;
```

With the `nativeDistinct` preview feature, `distinct: ["authorId"]` plus `orderBy` can also be pushed to the database on PostgreSQL.

## 278: How do you use Prisma with Zod for input validation?

Validate input with Zod before passing it to Prisma, so only allowed fields reach the query.

```ts
import { z } from "zod";

const CreateUser = z.object({
  email: z.string().email(),
  name: z.string().min(1).max(100),
});

app.post("/users", async (req, res) => {
  const data = CreateUser.parse(req.body);
  const user = await prisma.user.create({ data });
  res.status(201).json(user);
});
```

There are also community generators that create Zod schemas from the Prisma schema, but many teams write the API schemas by hand because API input is often different from the database shape.

## 279: Why should you not pass req.body directly to Prisma?

```ts
await prisma.user.update({ where: { id }, data: req.body });
```

A user could send fields you didn't plan for, like `{ "role": "ADMIN" }` or nested writes that connect or delete other records. This is called mass assignment. Always pick or validate the allowed fields first.

## 280: How do you create records with a known id in a test?

Pass the id in `data`, even if it has a default.

```ts
await prisma.user.create({ data: { id: 42, email: "test@example.com" } });
```

On PostgreSQL with `autoincrement()`, setting ids by hand does not move the sequence. Later inserts can then fail with `P2002`. Reset the sequence with `TRUNCATE ... RESTART IDENTITY` or `setval` in test setup.

## 281: How do you use Prisma Studio with a remote database?

Studio uses the database URL from your config, so you can point it at another environment:

```bash
DATABASE_URL="postgresql://..." npx prisma studio
```

Be careful with production data. Studio can edit and delete rows. Use a read only database user if you only want to look.

## 282: How do you use Prisma in a script or cron job?

Create the client, do the work, and always disconnect at the end so the process can exit.

```ts
import { prisma } from "./db";

async function main() {
  const result = await prisma.session.deleteMany({
    where: { expiresAt: { lt: new Date() } },
  });
  console.log(`Deleted ${result.count} sessions`);
}

main()
  .catch((e) => {
    console.error(e);
    process.exitCode = 1;
  })
  .finally(() => prisma.$disconnect());
```

## 283: How do you shut down Prisma gracefully in a server?

Listen for shutdown signals, stop accepting requests, then disconnect.

```ts
const server = app.listen(3000);

async function shutdown() {
  server.close();
  await prisma.$disconnect();
  process.exit(0);
}

process.on("SIGTERM", shutdown);
process.on("SIGINT", shutdown);
```

This lets running queries finish and closes database connections cleanly.

## 284: Can Prisma use database triggers, functions or check constraints?

Prisma schema can't describe them, but you can create them with SQL in a migration made with `--create-only`. Prisma Migrate will keep the SQL in the history and won't remove them. Since the schema doesn't know about them, `db pull` won't show them and Prisma Client won't know the logic exists, so document them for your team.

## 285: How do you add a CHECK constraint?

Add it in a custom migration.

```sql
ALTER TABLE "Product" ADD CONSTRAINT "price_positive" CHECK (price > 0);
```

When the constraint fails, Prisma returns an error you can catch. Keep the same check in your app validation too, so users get a clear message before hitting the database.

## 286: How do you use PostgreSQL extensions like pgcrypto or citext?

The simplest way is to enable them in a migration:

```sql
CREATE EXTENSION IF NOT EXISTS citext;
```

Then use the type in the schema, for example `email String @db.Citext`.

## 287: How do you share Prisma model types with a React frontend?

Import types from the browser-safe entry point of the generated client.

```ts
import type { User } from "@/generated/prisma/browser";

export function UserCard({ user }: { user: Pick<User, "id" | "name"> }) {
  return <p>{user.name}</p>;
}
```

Keep in mind that the API may not return the same shape as the database model (for example dates become strings in JSON), so for API responses it is often better to define separate DTO types.

## 288: Why can dates break when you send Prisma results through JSON?

Prisma returns `Date` objects, but `JSON.stringify` turns them into ISO strings. On the client they are strings, not dates, even if your shared TypeScript type says `Date`. Either convert them back on the client, use a serializer like superjson, or type the API response with strings.

## 289: How do you pick between Int and String ids?

- `Int` with `autoincrement()`: small, fast to index, easy to read, but ids can be guessed and you need the database to create them.
- `String` with `uuid()` or `cuid()`: hard to guess, can be created in the app before saving, and safe to merge between databases. They take more space and random UUIDs (v4) spread inserts across the index.

Time ordered ids like UUID v7 (`uuid(7)`) or ULID (`ulid()`) give you the benefits of string ids with better index locality.

## 290: How do you model a polymorphic relation in Prisma?

Prisma doesn't support polymorphic relations directly (one foreign key that can point to different tables). Common patterns:

- One optional foreign key per target: `postId Int?` and `videoId Int?` on `Comment`, plus a check that exactly one is set.
- A shared parent table, like `Commentable`, that both `Post` and `Video` point to.
- A `targetType` and `targetId` pair without a foreign key, loaded with separate queries.

The first two keep real foreign keys, so the database protects the data.

## 291: How do you store an ordered list of related items?

Add a `position` field and sort by it.

```prisma
model Task {
  id       Int    @id @default(autoincrement())
  listId   Int
  position Int

  @@index([listId, position])
}
```

```ts
const tasks = await prisma.task.findMany({
  where: { listId },
  orderBy: { position: "asc" },
});
```

To move items, update positions in a transaction. Some apps use gaps (10, 20, 30) or fractional values so a move only updates one row.

## 292: How do you create a record only if it doesn't exist, without updating?

Use `upsert` with an empty `update`.

```ts
const tag = await prisma.tag.upsert({
  where: { name: "prisma" },
  update: {},
  create: { name: "prisma" },
});
```

For many rows at once, use `createMany({ data, skipDuplicates: true })` on databases that support it.

## 293: How do you return only the id after a create?

```ts
const { id } = await prisma.user.create({
  data: { email },
  select: { id: true },
});
```

`select` works on all write operations, so you can make write responses smaller too.

## 294: How do you use the Prisma Client in a worker thread or child process?

Each thread or process needs its own `PrismaClient` instance, because clients and their connection pools cannot be shared across threads. Create the client inside the worker file and size the pool so that all workers together stay under the database's connection limit.

## 295: How do you use the same schema for SQLite in tests and PostgreSQL in production?

It is possible for simple schemas, but not recommended. The `provider` is fixed per schema, and many features differ: native types, enums, scalar lists, case sensitivity, JSON filters and `skipDuplicates`. Tests on SQLite can pass while production fails. It is better to run tests against the same database type, for example a PostgreSQL container.

## 296: How does a unique constraint behave on a nullable column?

On PostgreSQL, MySQL and SQLite, a unique column can have many rows with `NULL`, because `NULL` is not equal to `NULL`. So `phone String? @unique` lets many users have no phone, but no two users can share the same phone. SQL Server is different: a normal unique index allows only one `NULL`.

Because of this, you cannot use `findUnique({ where: { phone: null } })`. Use `findFirst` or `findMany` to look up rows with a null value.

## 297: How do you find slow queries in an app that uses Prisma?

- Log queries with their duration using `$on("query")` and print only those above a limit.
- Use OpenTelemetry tracing to see which request made which query.
- Look at the database side: `pg_stat_statements` on PostgreSQL or the slow query log on MySQL.
- Run `EXPLAIN ANALYZE` on the slow SQL to see if indexes are used.

## 298: How do you use EXPLAIN with a Prisma query?

Get the SQL from the query log, then run it with `EXPLAIN ANALYZE` in a SQL client or through raw SQL:

```ts
const plan = await prisma.$queryRawUnsafe(
  'EXPLAIN ANALYZE SELECT * FROM "Post" WHERE "authorId" = $1',
  1,
);
console.log(plan);
```

Look for sequential scans on big tables, which usually mean a missing index.

## 299: What does the PrismaClient errorFormat option do?

It controls how validation errors are printed: `"pretty"` (colors and a code frame), `"colorless"` or `"minimal"`.

```ts
const prisma = new PrismaClient({ adapter, errorFormat: "minimal" });
```

`minimal` is useful in production logs, where colors and long code frames are just noise.

## 300: How do you decide when to use raw SQL instead of the Prisma API?

Use the Prisma API by default, because it is type safe and easy to read. Switch to raw SQL (or TypedSQL) when:

- You need features Prisma doesn't support, like window functions, CTEs, `FOR UPDATE`, or special operators.
- A query generated by Prisma is too slow and a hand written query is clearly better.
- You run bulk operations that would be many separate Prisma calls.

Keep raw SQL in a few well tested places, and use TypedSQL when possible to keep type safety.

# Advanced Questions (301-450)

## 301: How does Prisma Client run a query in Prisma 7?

At a high level:

1. Your call, like `prisma.user.findMany({ include: { posts: true } })`, is turned into an internal JSON description of the query.
2. The query compiler (shipped as WebAssembly, not a native Rust binary) turns that description into a query plan: the SQL statements to run and how to combine the results.
3. The plan is executed in JavaScript. The SQL goes to the database through the driver adapter (for example `pg`).
4. The rows are mapped back into the nested objects and types you asked for.

Before Prisma 7, steps 2 to 4 happened inside a separate Rust query engine that ran as a native library or a binary.

## 302: What was the Rust query engine and how did it work?

In Prisma 6 and older, Prisma Client sent queries to a query engine written in Rust. By default it was loaded as a Node-API library (`libquery_engine`), and there was also a binary mode where it ran as a separate process that the client talked to over HTTP. The engine built the SQL, managed the connection pool and talked to the database.

It was fast, but it needed a platform specific build for each OS and CPU, added tens of megabytes to deployments, and could not run in many edge runtimes.

## 303: What are the trade-offs of the Rust-free architecture?

Good:

- No native binaries, so bundles are smaller and builds are the same everywhere.
- Works in serverless and edge runtimes and with any bundler.
- You control the connection pool and driver settings directly.

Things to keep in mind:

- Behavior now depends on the driver (pool defaults, SSL checks, type parsing), which can differ from the old engine.
- Result mapping runs in JavaScript on the same thread as your app, so very large result sets use your app's CPU.
- You have to install and configure an adapter for each database.

## 304: What are the N+1 query problems you can hit with Prisma?

N+1 happens when you load a list (1 query) and then run one extra query for each item (N queries).

```ts
// N+1
const users = await prisma.user.findMany();
for (const user of users) {
  user.posts = await prisma.post.findMany({ where: { authorId: user.id } });
}
```

Fix it by loading the relation in one go:

```ts
const users = await prisma.user.findMany({ include: { posts: true } });
```

Or collect ids and use one `findMany({ where: { authorId: { in: ids } } })`. In GraphQL, the fluent API and `findUnique` batching help, since Prisma merges those calls.

## 305: How many SQL queries does an include generate?

It depends on the load strategy. With the default `query` strategy (and without the `relationJoins` preview), Prisma runs one query for the main model and then one query per relation level, using `WHERE "authorId" IN (...)`. So `findMany` with `include: { posts: { include: { comments: true } } }` is three queries, no matter how many rows there are. It is not N+1, but it is more than one round trip.

With `relationJoins` and `relationLoadStrategy: "join"` on PostgreSQL or MySQL, it becomes one query with joins.

## 306: How do you make large IN lists safe?

When you load relations or filter with `in: [...]` on thousands of ids, the query can hit the database's parameter limit (for example 65,535 on PostgreSQL, much lower on SQL Server). Prisma splits some of these queries into chunks for you, but very large lists are still slow. Better options:

- Page through the data in smaller batches.
- Use a join or subquery in raw SQL.
- On PostgreSQL, pass an array as one parameter: `WHERE id = ANY(${ids})`.

## 307: How do you process millions of rows without loading them all in memory?

Use cursor based batches.

```ts
let cursor: number | undefined;

while (true) {
  const batch = await prisma.event.findMany({
    take: 1000,
    ...(cursor && { skip: 1, cursor: { id: cursor } }),
    orderBy: { id: "asc" },
  });
  if (batch.length === 0) break;

  await handle(batch);
  cursor = batch[batch.length - 1].id;
}
```

Prisma doesn't stream results, so each `findMany` loads its whole result into memory. Keeping batches small keeps memory stable.

## 308: How do you insert a very large number of rows efficiently?

- Use `createMany` in chunks of a few thousand rows instead of one `create` per row.
- Turn off things you don't need during import, like heavy logging.
- For really large imports, use the database's own bulk tools, for example PostgreSQL `COPY` through `pg-copy-streams`, outside of Prisma.
- Create indexes after the bulk load if the table is new, because updating indexes for every row is slow.

## 309: How do you design indexes for Prisma queries?

Look at the real queries your app runs, then index:

- Foreign keys used in relations and filters (`@@index([authorId])`). PostgreSQL does not index foreign keys automatically.
- Columns used in `where` and `orderBy` together, as composite indexes in the right order, like `@@index([authorId, createdAt(sort: Desc)])`.
- Columns used in cursor pagination.

Don't add indexes you don't use. Each index slows down writes and takes space.

## 310: Why does the order of fields in a composite index matter?

A B-tree index on `[a, b]` can be used for filters on `a`, or on `a` and `b`, but usually not on `b` alone. Put the field you always filter on with equality first, and the field you sort or range filter on second. For example `@@index([tenantId, createdAt])` supports "posts of tenant X, newest first".

## 311: What are partial indexes and does Prisma support them?

A partial index covers only rows that match a condition, like `WHERE "deletedAt" IS NULL`. It is smaller and faster for queries that use the same condition.

Prisma added a `partialIndexes` preview feature in 7.4 for defining these in the schema. Without it, you create them with SQL in a custom migration:

```sql
CREATE UNIQUE INDEX "user_email_active" ON "User" (email) WHERE "deletedAt" IS NULL;
```

That example also shows how to keep emails unique only among non deleted users, which is a common soft delete need.

## 312: How do you add an index to a big table without downtime?

A normal `CREATE INDEX` on PostgreSQL blocks writes to the table while it runs. Use `CONCURRENTLY` instead, in its own migration:

```sql
-- migration.sql (created with --create-only)
CREATE INDEX CONCURRENTLY "Post_authorId_idx" ON "Post"("authorId");
```

`CREATE INDEX CONCURRENTLY` cannot run inside a transaction. Prisma Migrate runs each migration file as a script, so keep that statement alone in its own migration and make sure the index name matches what Prisma expects from `@@index`, otherwise the next diff shows drift.

## 313: How do you do zero downtime schema changes with Prisma?

Use the expand and contract pattern:

1. **Expand**: add the new column or table as optional. Deploy. Old and new code both work.
2. **Migrate**: write to both old and new columns, and backfill old data in batches.
3. **Switch**: deploy code that reads from the new column.
4. **Contract**: remove the old column in a later migration, once no code uses it.

Never rename or drop something in the same deploy that removes the code using it, because during a rolling deploy old instances are still running.

## 314: What can go wrong when migrations run at app start?

If every instance runs `prisma migrate deploy` when it starts, several instances can start at the same time. Prisma uses an advisory lock on PostgreSQL and MySQL to stop two migrations running at once, but you still get slow starts, timeouts in health checks, and confusing logs. A long migration can also make instances fail their readiness checks. It is better to run migrations as a separate step in the pipeline, before the new version starts.

## 315: How do you recover from a failed migration in production?

1. Check what happened with `npx prisma migrate status` and the database logs.
2. Fix the database by hand: either finish the change or undo the parts that were applied, since many databases (like MySQL) cannot roll back DDL.
3. Mark the migration with `npx prisma migrate resolve --rolled-back <name>` if you want to run it again, or `--applied <name>` if you finished it by hand.
4. Fix the migration file if needed (only if it never finished anywhere) and deploy again.

PostgreSQL runs most DDL in a transaction, so a failed migration often leaves no partial changes, but you still have to resolve the failed record.

## 316: How do you write a down migration with Prisma?

Prisma Migrate has no automatic down migrations. If you need a way back, you can generate the SQL for it with `migrate diff`:

```bash
npx prisma migrate diff \
  --from-schema prisma/schema.prisma \
  --to-schema prisma/schema.previous.prisma \
  --script > down.sql
```

You run that SQL with `prisma db execute --file down.sql` and then mark the migration as rolled back. In practice many teams prefer "roll forward": write a new migration that fixes the problem.

## 317: How do you squash many migrations into one?

1. Make sure all environments are up to date.
2. Delete the old migration folders.
3. Create one new migration from an empty database to the current schema with `migrate diff --from-empty --to-schema ... --script`.
4. In existing databases, mark it as applied with `migrate resolve --applied`.

Do this rarely and carefully, because any custom SQL in old migrations (triggers, extensions, data changes) must be added back by hand.

## 318: How does Prisma Migrate detect what changed?

It builds two pictures of the database: the result of applying all existing migrations (in the shadow database) and the target defined by your schema. Then it diffs them and generates SQL for the difference. That is why custom objects like triggers stay safe: they come from migrations, so they are in both pictures. But changes made by hand on the dev database outside migrations show up as drift.

## 319: How do you handle a team where two people add migrations at the same time?

Migrations are ordered by their timestamp folder names. If two branches each add a migration, after merging there are two new folders. Usually it just works, because they touch different things. If they conflict (for example both change the same column), run `migrate dev` after the merge. Prisma will notice the state and may ask you to create a new migration to fix it, or to reset your dev database. Rebasing the later migration and recreating it on top of the merged schema is often the cleanest fix.

## 320: How do you implement multi-tenancy with Prisma?

Common patterns:

- **Shared tables with tenantId**: every table has a `tenantId` column and every query filters on it. Simple and cheap. Use a query extension or PostgreSQL Row Level Security so you can't forget the filter.
- **Schema per tenant**: each tenant has its own PostgreSQL schema. Good isolation, but you need to run migrations for each schema and manage many clients or connection settings.
- **Database per tenant**: the strongest isolation, but the most work and the most connections.

Most SaaS apps start with shared tables and a `tenantId`.

## 321: How do you enforce a tenant filter on every query?

A query extension can add the tenant to reads and writes.

```ts
export function forTenant(tenantId: string) {
  return prisma.$extends({
    query: {
      $allModels: {
        async $allOperations({ args, query, operation }) {
          if (
            [
              "findMany",
              "findFirst",
              "count",
              "updateMany",
              "deleteMany",
            ].includes(operation)
          ) {
            (args as any).where = { ...(args as any).where, tenantId };
          }
          if (operation === "create") {
            (args as any).data = { ...(args as any).data, tenantId };
          }
          return query(args);
        },
      },
    },
  });
}
```

This is a helpful safety net, but it doesn't cover every case (nested writes, raw SQL, `findUnique`). For strong guarantees use database Row Level Security as well.

## 322: How do you use PostgreSQL Row Level Security with Prisma?

Set a session variable in a transaction, then let RLS policies use it.

```ts
export function withUser(userId: string) {
  return prisma.$extends({
    query: {
      $allModels: {
        async $allOperations({ args, query }) {
          const [, result] = await prisma.$transaction([
            prisma.$executeRaw`SELECT set_config('app.user_id', ${userId}, TRUE)`,
            query(args),
          ]);
          return result;
        },
      },
    },
  });
}
```

```sql
ALTER TABLE "Post" ENABLE ROW LEVEL SECURITY;
CREATE POLICY own_posts ON "Post" USING ("authorId" = current_setting('app.user_id'));
```

The `TRUE` makes the setting local to the transaction, which is important with connection pools. The app must connect as a database role that does not bypass RLS.

## 323: How do you route reads to a read replica?

Prisma has an official read replicas extension, `@prisma/extension-read-replicas`. Once set up, read queries like `findMany` go to a replica, while writes and transactions go to the primary. You can force a query to the primary with `prisma.$primary()`.

Keep replication lag in mind. A user who just saved something may not see it if the next read goes to a replica, so read from the primary right after a write when it matters.

## 324: How would you handle sharding with Prisma?

Prisma has no built in sharding for most databases. Options:

- Keep one client per shard and pick the client in code based on a shard key (like tenant id).
- Use a database that shards for you, like CockroachDB, Citus or PlanetScale (Vitess), and connect to it as one database.
- For PlanetScale, there is a `shardKeys` preview feature (added in 6.10) that lets you mark shard key fields with `@shardKey` and `@@shardKey` in the schema so queries can be routed well.

## 325: How do you connect to more than one database in one app?

Use a separate schema and generator output for each database, and create one client per database.

```prisma
// prisma/analytics/schema.prisma
generator client {
  provider = "prisma-client"
  output   = "../../src/generated/analytics"
}
```

```ts
import { PrismaClient as MainClient } from "./generated/main/client";
import { PrismaClient as AnalyticsClient } from "./generated/analytics/client";
```

Each schema has its own migrations and its own config file (or you pass `--config` / `--schema` to the CLI). Transactions cannot span both databases.

## 326: How do you keep data consistent across a database write and a message queue?

A Prisma transaction only covers the database, so "save order, then publish event" can fail half way. The usual fix is the outbox pattern:

```ts
await prisma.$transaction([
  prisma.order.create({ data: order }),
  prisma.outbox.create({ data: { type: "order.created", payload: order } }),
]);
```

A separate worker reads unprocessed rows from `Outbox`, publishes them to the queue, and marks them as sent. The order and the event are saved together or not at all.

## 327: Why should interactive transactions be short?

An interactive transaction holds a database connection for its whole life, and often row locks too. If you call an external API or do slow work inside it:

- Other requests wait for locks or for free connections in the pool.
- The transaction can hit the `timeout` (5 seconds by default) and roll back.
- Under load, the pool runs out and the whole app slows down.

Do slow work before or after the transaction, and keep only database calls inside it.

## 328: What happens when an interactive transaction times out?

Prisma rolls the transaction back and later calls with `tx` fail with an error saying the transaction is closed or expired. Code that was still running in the callback may keep running but its queries fail. That is why you should not catch and ignore errors inside the callback. Let them reach `$transaction` so the rollback is clear.

## 329: How do you prevent double charging when a payment request is retried?

Use an idempotency key with a unique constraint.

```prisma
model Payment {
  id             String @id @default(uuid())
  idempotencyKey String @unique
  amount         Int
}
```

```ts
try {
  return await prisma.payment.create({ data: { idempotencyKey: key, amount } });
} catch (e) {
  if (e instanceof Prisma.PrismaClientKnownRequestError && e.code === "P2002") {
    return prisma.payment.findUniqueOrThrow({ where: { idempotencyKey: key } });
  }
  throw e;
}
```

The database guarantees only one row per key, even if two retries arrive at the same moment.

## 330: How do you handle race conditions on a counter or stock value?

Don't read, change in code, and write back. Two requests can read the same value and one update is lost. Use an atomic update with a condition:

```ts
const result = await prisma.product.updateMany({
  where: { id: productId, stock: { gte: quantity } },
  data: { stock: { decrement: quantity } },
});

if (result.count === 0) throw new Error("Out of stock");
```

The check and the change happen in one SQL statement, so the stock can't go below zero.

## 331: How do you lock across processes with Prisma, for example for a cron job?

On PostgreSQL, use an advisory lock through raw SQL.

```ts
const [{ locked }] = await prisma.$queryRaw<{ locked: boolean }[]>`
  SELECT pg_try_advisory_lock(12345) AS locked
`;
if (!locked) return; // another instance is running

try {
  await runJob();
} finally {
  await prisma.$queryRaw`SELECT pg_advisory_unlock(12345)`;
}
```

Session level advisory locks are tied to one connection. With a pool, the unlock may run on a different connection, so it is safer to use `pg_try_advisory_xact_lock` inside an interactive transaction, which is released when the transaction ends.

## 332: What are common security risks when using Prisma?

- SQL injection through `$queryRawUnsafe` or `Prisma.raw` with user input.
- Mass assignment by passing request bodies directly into `data` or `where`.
- Leaking sensitive fields like password hashes by returning whole models. Use `select` or `omit`.
- Missing ownership checks, so one user can read or change another user's data.
- `undefined` filters removing a `where` condition in `deleteMany` or `updateMany`.
- Logging queries with parameters in production, which can put personal data in logs.

## 333: Is Prisma.raw safe?

No. `Prisma.raw` inserts a string into the SQL as is, without parameters. It is meant for things that can't be parameters, like a table or column name, and only with values you control. If you need a dynamic column name from user input, check it against a list of allowed names first.

```ts
const allowed = ["createdAt", "title"] as const;
const column = allowed.includes(input) ? input : "createdAt";

await prisma.$queryRaw`SELECT * FROM "Post" ORDER BY ${Prisma.raw(`"${column}"`)} DESC`;
```

## 334: Can users inject operators through Prisma filters?

Prisma queries are objects, so if you pass user input straight into `where`, a user can send an object instead of a string. For example `{ "email": { "contains": "" } }` instead of an email, which matches every user. This is like NoSQL injection. Validate that inputs have the expected type (string, number) before you put them into a query.

## 335: How do you store passwords with Prisma?

Prisma just stores what you give it. Hash the password with a slow password hash like argon2 or bcrypt before saving, and never return the hash from your API.

```ts
import argon2 from "argon2";

await prisma.user.create({
  data: { email, passwordHash: await argon2.hash(password) },
  select: { id: true, email: true },
});
```

Using global `omit: { user: { passwordHash: true } }` makes it harder to leak the hash by accident.

## 336: How do you limit database permissions for an app that uses Prisma?

Use different database users:

- A migration user that can change the schema, used only by `prisma migrate deploy` in the pipeline.
- An app user with only `SELECT`, `INSERT`, `UPDATE` and `DELETE` on the app tables, used by Prisma Client at run time.

That way, a bug or attack in the app can't drop tables. With Prisma 7 this split is natural: the CLI uses the URL in `prisma.config.ts` and the app uses the URL given to the adapter.

## 337: How do you audit who changed what?

Options, from simple to strong:

- `createdById` and `updatedById` columns set by the app.
- A query extension that writes an `AuditLog` row for each create, update and delete, in the same transaction.
- Database triggers that copy changes into an audit table, which also catch changes from raw SQL and other tools.

An extension is easy to add, but it doesn't see raw SQL or `updateMany` row details, so for strict audit needs triggers are more reliable.

## 338: How do you encrypt a column with Prisma?

Prisma has no built in field encryption. You can:

- Encrypt and decrypt in your code before writes and after reads.
- Use a query extension or a community extension that does it for specific fields.
- Use database features like `pgcrypto`, or encryption at rest for the whole disk.

Encrypted fields can't be searched or indexed normally, so if you need lookups (like by email), store a separate hash of the value for searching.

## 339: How do the select and include types work internally?

The generated client uses TypeScript generics. Each method takes your arguments as a type parameter (`T extends Prisma.UserFindManyArgs`), and the return type is computed from `T` with conditional and mapped types, like `Prisma.UserGetPayload<T>`. That is why the result type changes when you change `select`. Very large schemas make these types heavy, which can slow down the TypeScript language server.

## 340: How do you speed up TypeScript when the Prisma schema is huge?

- Split code so files don't all import the whole client type.
- Import narrow types from `models/<Model>` instead of everything from `client`.
- Avoid passing huge inferred types around. Give functions explicit return types.
- Keep TypeScript and Prisma up to date. Prisma has worked on reducing type size in recent versions.
- Use `skipLibCheck` in `tsconfig.json`.

## 341: How do you write a generic function that works for any model?

It is hard to type well because each model has different argument types. Common approaches:

- Use `$allModels` in a client extension with `Prisma.getExtensionContext(this)` and the `Prisma.Args` and `Prisma.Result` helper types.
- Accept a delegate (like `prisma.user`) with a simpler structural type for the methods you need.

```ts
const xprisma = prisma.$extends({
  model: {
    $allModels: {
      async exists<T>(
        this: T,
        where: Prisma.Args<T, "findFirst">["where"],
      ): Promise<boolean> {
        const context = Prisma.getExtensionContext(this);
        const result = await (context as any).findFirst({
          where,
          select: { id: true },
        });
        return result !== null;
      },
    },
  },
});

await xprisma.user.exists({ email: "a@example.com" });
```

## 342: What does Prisma.getExtensionContext do?

Inside a model extension method, `this` is the model delegate, but its type is generic. `Prisma.getExtensionContext(this)` gives you that delegate at run time, so you can call `findFirst`, `create` and so on for whichever model the method was called on. It also gives you the model name (`context.$name`).

## 343: How do you type the client after using $extends?

`$extends` returns a new client type. To pass it around, use `typeof`:

```ts
function createClient() {
  return new PrismaClient({ adapter }).$extends(softDelete).$extends(audit);
}

export type ExtendedPrismaClient = ReturnType<typeof createClient>;
export const prisma = createClient();
```

The plain `PrismaClient` type doesn't know about your custom methods, so functions that need them should use `ExtendedPrismaClient`.

## 344: How do extensions behave inside transactions?

If you call `$transaction` on an extended client, the `tx` client inside also has the extensions, so query and result extensions still apply. But extension code that uses the original `prisma` variable inside a model method runs outside the transaction. Use `Prisma.getExtensionContext(this)` instead of the outer client, so the method works on whichever client called it.

## 345: Why is the result extension field not available in where or orderBy?

Result extensions are computed in JavaScript after the data is loaded. The database doesn't know about them, so you can't filter, sort or group by them. If you need that, compute the value in the database instead, for example with a generated column, a view, or raw SQL.

## 346: How do you mock an extended Prisma client in tests?

Mock the extended type instead of `PrismaClient`.

```ts
import { mockDeep } from "vitest-mock-extended";
import type { ExtendedPrismaClient } from "../db";

const prismaMock = mockDeep<ExtendedPrismaClient>();
prismaMock.user.findByEmail.mockResolvedValue(null);
```

Keep in mind that mocks skip the extension logic itself. Test that logic separately with a real database.

## 347: What are the limits of mocking Prisma in unit tests?

Mocks only check that you called the client with certain arguments. They don't check that the query works: wrong filters, missing indexes, constraint errors, transaction behavior and cascade deletes all pass silently. They also break easily when you refactor queries. A good balance is unit tests with mocks for business logic, and integration tests against a real database for the data access code.

## 348: How do you test migrations?

- In CI, start a clean database and run `prisma migrate deploy` to check that all migrations apply in order.
- Use `migrate diff` with `--exit-code` to check the schema and migrations match.
- For risky data migrations, run them against a copy of production data (with personal data removed) and check the results.
- Time the migration on realistic data sizes, so you know if it will lock tables for too long.

## 349: How do you handle a column type that Prisma maps poorly?

Some database types are not a great fit for the default JavaScript types, for example PostgreSQL `interval`, `money`, ranges or `geometry`. Options:

- Use `Unsupported("type")` and read and write it with raw SQL.
- Store it in another form that Prisma supports (for example two `DateTime` columns instead of a range).
- Cast in raw SQL, like `SELECT location::text`.
- Use a view that exposes the value in a simple type.

## 350: How do you use PostGIS or pgvector with Prisma?

Prisma doesn't have native support for these types, so they show up as `Unsupported`.

```prisma
model Document {
  id        Int                    @id @default(autoincrement())
  content   String
  embedding Unsupported("vector(1536)")?
}
```

```ts
const similar = await prisma.$queryRaw`
  SELECT id, content FROM "Document"
  ORDER BY embedding <-> ${vectorString}::vector
  LIMIT 5
`;
```

You enable the extension and create special indexes (like HNSW or GiST) in a custom SQL migration. TypedSQL can give these raw queries proper result types.

## 351: How do you size the connection pool for a Prisma app?

Start from the database limit and work backwards. If PostgreSQL allows 100 connections, keep some for admin tools and migrations, then split the rest across all app instances:

```
pool size per instance = usable connections / number of instances
```

A bigger pool is not always faster. The database has a limited number of CPU cores, and too many active connections cause contention. A small pool (often around `cores * 2` on the database side, shared by all instances) plus a pooler like PgBouncer usually works better than giving every instance a large pool.

## 352: What happens when the connection pool is exhausted?

New queries wait for a free connection. With `pg`, if `connectionTimeoutMillis` is set, the wait fails with a timeout error after that time. If it is not set, queries can wait forever and requests hang. Common causes are long transactions, slow queries, too many parallel queries in a loop (like `Promise.all` over thousands of items), or creating many clients.

## 353: Why can Promise.all over many Prisma queries be a problem?

```ts
await Promise.all(ids.map((id) => prisma.user.update({ where: { id }, data })));
```

With 10,000 ids, this sends 10,000 queries at once. They all compete for a small pool, wait in a queue, and can hit timeouts. It also puts a lot of load on the database. Use `updateMany` when possible, or limit the concurrency with chunks or a library like `p-limit`.

## 354: How do you reduce cold start time for Prisma in serverless?

- Use Prisma 7 (or the `prisma-client` generator), which has no native engine to load and a smaller bundle.
- Create the client outside the handler so warm calls reuse it.
- Bundle your function so only the code you use is included.
- Use an HTTP based driver (Neon, PlanetScale) for edge functions, so there is no TCP connection setup.
- Avoid `$connect()` at start up if the first request doesn't always need the database.

## 355: How do you choose between a TCP driver and an HTTP serverless driver?

- **TCP drivers** (like `pg`) keep a long lived connection and are fastest for servers and long running containers. They need a pooler in serverless setups.
- **HTTP or WebSocket drivers** (like Neon serverless or PlanetScale) work in edge runtimes with no TCP support and don't keep connections open, which fits short lived functions. Each query can have a bit more latency, and interactive transactions may be limited or need WebSockets.

Use TCP for normal servers and HTTP drivers for edge and very bursty serverless loads.

## 356: Why should the database be close to your app servers?

Every Prisma query is at least one network round trip. An `include` with the `query` strategy can be several round trips. If the app is in Europe and the database in the US, each round trip adds around 100 ms, so a page with 10 queries spends a second just waiting on the network. Put the app and database in the same region, and reduce round trips with `include`, `relationLoadStrategy: "join"` or fewer, bigger queries.

## 357: How do you cache Prisma query results?

Prisma itself doesn't cache results in Prisma 7 (Accelerate did, but standalone Accelerate is being retired). Common options:

- An in memory cache (like `lru-cache`) for small, hot, rarely changing data.
- Redis for shared caching across instances.
- Framework caches, like Next.js data caching.

You can wrap this in a model extension, for example `prisma.product.findManyCached(...)`. The hard part is invalidation: clear the cache entries when the data changes.

## 358: How do you avoid loading too much data with include?

- Use `select` instead of `include` and pick only the fields you show.
- Add `take` and `where` inside relations, especially for to-many relations.
- Use `_count` instead of loading a relation just to count it.
- Load big relations on demand in a second query, only when needed.

A user with 50,000 orders and `include: { orders: true }` will load all 50,000 rows.

## 359: When does Prisma generate inefficient queries, and what do you do?

Some cases to watch:

- Deep or wide includes without `relationJoins` cause several round trips.
- Filters on relations (`some`, `every`, `none`) become subqueries that may not use indexes well.
- `distinct` without `nativeDistinct` loads all rows and filters in memory.
- `count` with complex relation filters can be slow on big tables.

Log the SQL, run `EXPLAIN ANALYZE`, add the right indexes, and if needed rewrite the hot query with TypedSQL or raw SQL.

## 360: How does distinct work without nativeDistinct?

Prisma fetches the matching rows and removes duplicates in JavaScript. On big tables this is slow and uses a lot of memory, since all rows are loaded before the distinct step. With the `nativeDistinct` preview feature, Prisma uses `DISTINCT ON` (PostgreSQL) where it can. For counting distinct values, a `groupBy` or raw `COUNT(DISTINCT ...)` is often better.

## 361: How do you design a schema for an e-commerce order system with Prisma?

```prisma
model Order {
  id         String      @id @default(uuid(7))
  customerId String
  customer   Customer    @relation(fields: [customerId], references: [id])
  status     OrderStatus @default(PENDING)
  total      Decimal     @db.Decimal(12, 2)
  items      OrderItem[]
  createdAt  DateTime    @default(now())

  @@index([customerId, createdAt(sort: Desc)])
}

model OrderItem {
  id        String  @id @default(uuid(7))
  orderId   String
  order     Order   @relation(fields: [orderId], references: [id], onDelete: Cascade)
  productId String
  product   Product @relation(fields: [productId], references: [id])
  quantity  Int
  unitPrice Decimal @db.Decimal(12, 2)

  @@index([orderId])
}
```

Key choices: copy the `unitPrice` into the order item (prices change later), use `Decimal` for money, cascade delete items with their order but not products, and index the queries you run most.

## 362: How would you model user roles and permissions?

For simple apps, an enum is enough: `role Role @default(USER)`. For flexible permissions, use tables:

```prisma
model User {
  id    Int        @id @default(autoincrement())
  roles UserRole[]
}

model Role {
  id          Int          @id @default(autoincrement())
  name        String       @unique
  users       UserRole[]
  permissions Permission[]
}

model UserRole {
  userId Int
  roleId Int
  user   User @relation(fields: [userId], references: [id], onDelete: Cascade)
  role   Role @relation(fields: [roleId], references: [id], onDelete: Cascade)

  @@id([userId, roleId])
}

model Permission {
  id    Int    @id @default(autoincrement())
  key   String @unique
  roles Role[]
}
```

Load a user's permissions once per request (or cache them) instead of querying on every check.

## 363: How would you model a tree, like nested comments or categories?

- **Adjacency list**: each row has a `parentId`. Simple to write and easy in Prisma, but loading a whole tree needs many queries or a recursive CTE in raw SQL.
- **Materialized path**: store the path like `"1/4/9"` and query with `startsWith`. Fast for loading subtrees, harder to move nodes.
- **Closure table**: a separate table with every ancestor and descendant pair. Fast queries in all directions, more rows to maintain.

For comments, an adjacency list plus a recursive CTE for loading full threads is common.

## 364: How do you load a full tree with a recursive query?

```ts
const rows = await prisma.$queryRaw<
  { id: number; parentId: number | null; body: string }[]
>`
  WITH RECURSIVE thread AS (
    SELECT id, "parentId", body FROM "Comment" WHERE id = ${rootId}
    UNION ALL
    SELECT c.id, c."parentId", c.body
    FROM "Comment" c JOIN thread t ON c."parentId" = t.id
  )
  SELECT * FROM thread
`;
```

Then build the nested structure in JavaScript from the flat list. This is one query instead of one per level.

## 365: How do you implement soft delete correctly, beyond a simple filter?

Things a simple `deletedAt: null` filter misses:

- `findUnique` can't take a non unique filter in older versions, so use extended where unique or `findFirst`.
- Relations: `include: { posts: true }` still returns deleted posts unless you filter inside the include.
- Unique constraints: a deleted user's email blocks a new user with that email. Use a partial unique index on non deleted rows.
- Cascades: the database won't cascade a soft delete.
- Counts and aggregates also need the filter.

Many teams use a view of active rows or PostgreSQL RLS for strict cases, or decide that hard delete plus an archive table is simpler.

## 366: What are the pros and cons of using Prisma extensions for cross cutting rules?

Pros: one place for rules like soft delete, tenancy, auditing and logging; code stays clean; extensions are typed.

Cons: rules are hidden, so a reader may not know a filter is added; raw SQL and some nested operations skip them; ordering of several extensions matters; and debugging is harder. For security rules, back them up with database level protection.

## 367: How does Prisma handle cascading deletes, and what are the risks?

When you set `onDelete: Cascade`, the database itself deletes children, so it is fast and consistent. With `relationMode = "prisma"`, Prisma emulates cascades in the client by running extra queries, which is slower and not safe if other code writes to the database.

The risk is deleting much more than you expected. One `delete` on a user can remove thousands of posts, comments and likes. For important data, prefer `Restrict` and delete children on purpose, or use soft delete.

## 368: Why do you need indexes on foreign keys with relationMode = "prisma"?

With real foreign keys, many databases (like MySQL) create an index on the foreign key automatically. With `relationMode = "prisma"` there is no foreign key, so there is no index. Queries that load relations or emulate cascades then scan the whole table. Prisma warns about this, and you should add `@@index([authorId])` for each relation scalar.

## 369: How does Prisma map JavaScript types to database types, and where can precision be lost?

- `Int` maps to a 32 bit integer, so values above about 2.1 billion fail. Use `BigInt` for large counters.
- `Float` is a double. Fine for measurements, wrong for money.
- `Decimal` keeps exact precision and comes back as `Prisma.Decimal`.
- `DateTime` precision depends on the column. Prisma uses `timestamp(3)` (milliseconds) by default, so microseconds written by other tools are cut in JavaScript.
- `BigInt` columns come back as `bigint`, which can't be mixed with `number` in math without converting.

## 370: What happens when two Prisma versions run against the same database?

The database doesn't care which Prisma version you use, but there are some risks:

- The schemas may differ. If service A's schema has a column that service B's doesn't, B can't see it, which is fine, but B's migrations may try to remove it.
- Only one service should own migrations for a database. Others should only use `db pull` or share the schema.

Pick one owner of the schema and migrations, and let the other services read from it.

## 371: How do you share one database between several services that use Prisma?

Best practice is to avoid it and give each service its own database. If you must share:

- Keep the schema and migrations in one place (a shared package or the owning service).
- Other services use the same schema package, or use `db pull` to get their own read only view of the tables they need.
- Never run migrations from more than one service.
- Coordinate breaking changes with expand and contract migrations.

## 372: What are the main differences between Prisma and Drizzle?

- **Schema**: Prisma uses its own `.prisma` language. Drizzle defines tables in TypeScript.
- **Query style**: Prisma has a higher level API (`findMany` with `include`). Drizzle stays close to SQL with a query builder (`select().from().where()`) and also has a relational query API.
- **Generation**: Prisma needs `prisma generate`. Drizzle types come straight from your TypeScript schema.
- **SQL control**: Drizzle makes complex SQL easier to express. Prisma needs raw SQL or TypedSQL for those cases.
- **Migrations**: both generate SQL migrations from the schema.

Prisma is often easier for teams new to SQL. Drizzle suits teams that want to think in SQL.

## 373: What are the main differences between Prisma and TypeORM?

TypeORM uses classes with decorators as entities and supports Active Record and Data Mapper patterns. Entities are class instances and can have methods and lazy relations. Its type safety is weaker: many query builder results are not fully typed, and relations can be `undefined` at run time even when typed as present.

Prisma returns plain objects with exact types based on your `select` and `include`. It has no entity classes, no lazy loading, and no identity map. Many teams find Prisma easier to reason about, while TypeORM feels more familiar to people coming from Java or C# ORMs.

## 374: When would you choose a query builder like Kysely over Prisma?

- You need lots of complex SQL (CTEs, window functions, special operators) and still want type safety.
- You want no code generation step for queries.
- You want full control over every query for performance.
- Your team knows SQL well and prefers to write it.

Some teams use both: Prisma for schema, migrations and simple CRUD, and Kysely (there is a community `prisma-kysely` generator) for complex queries.

## 375: When is Prisma not a good choice?

- The app is mostly complex reporting and analytics SQL. You'd be writing raw SQL most of the time.
- You need database features Prisma doesn't model well and rely on them everywhere.
- You need very high throughput on huge result sets, where the extra mapping layer matters.
- You need MongoDB on the newest Prisma version (MongoDB is still on Prisma 6).
- You are in a language other than TypeScript or JavaScript.

## 376: How does Prisma represent a query internally before it becomes SQL?

Prisma Client sends the query as a JSON document: the model, the action (like `findMany`), and the arguments with an explicit selection of fields. This "JSON protocol" became the default in Prisma 5 and replaced an older GraphQL like format, which made queries faster to build and parse. In Prisma 7 the query compiler reads this JSON and produces a query plan.

## 377: Why does Prisma sometimes run a SELECT after an INSERT or UPDATE?

Prisma returns the full written record (or your `select`). On databases that support `RETURNING` (PostgreSQL, SQLite, CockroachDB), it can usually get the data back in the same statement. On MySQL, which has no `RETURNING`, Prisma often has to run an extra `SELECT`. Nested writes and `include` also add queries to load relations. If you don't need the result, using `updateMany` or `createMany` avoids that extra work.

## 378: How do nested writes affect performance?

A nested create with many children turns into several statements: one insert for the parent and inserts for each nested level, all in one transaction. Nested `create` with an array often inserts children one by one. For large child lists, `createMany` inside the nested write (`items: { createMany: { data: [...] } }`) is faster because it uses one bulk insert.

## 379: What happens with an update that changes nothing?

Prisma still runs the update. With `@updatedAt`, the timestamp changes even if no other field changed. If you want to avoid useless writes (for example to keep `updatedAt` meaningful), compare values in code first, or use `updateMany` with a `where` that only matches rows that actually differ.

## 380: How do you do an "upsert many"?

Prisma has no `upsertMany`. Options:

- Many `upsert` calls inside one `$transaction([...])`. Simple, but one statement per row.
- `createMany({ skipDuplicates: true })` if you only need "insert if missing".
- Raw SQL `INSERT ... ON CONFLICT (...) DO UPDATE SET ...` with many rows, for real bulk upserts on PostgreSQL.

```ts
await prisma.$executeRaw`
  INSERT INTO "Product" (sku, price)
  SELECT * FROM UNNEST(${skus}::text[], ${prices}::numeric[])
  ON CONFLICT (sku) DO UPDATE SET price = EXCLUDED.price
`;
```

## 381: What is the risk of a long running findMany in a request handler?

It holds a connection, loads everything into memory, and blocks your event loop while Prisma maps a huge result into objects. Under load this can slow the whole server, not just one request. Always paginate list endpoints and set a maximum `take`, even for admin APIs.

## 382: How do you limit query execution time?

- Set a statement timeout on the database side, for example `statement_timeout` for the app user in PostgreSQL, or on the `pg` pool with the `statement_timeout` option.
- Use `timeout` on interactive transactions.
- Add request level timeouts in your server so slow queries don't pile up.

```ts
const adapter = new PrismaPg({
  connectionString: process.env.DATABASE_URL,
  statement_timeout: 10_000,
});
```

## 383: How do you handle deadlocks in Prisma?

Deadlocks happen when two transactions lock rows in a different order. The database kills one of them, and Prisma 7 maps PostgreSQL deadlocks to error `P2034`. To reduce them:

- Always lock or update rows in the same order (for example sorted by id).
- Keep transactions short.
- Avoid updating many rows in one transaction when you can.

And retry the transaction a few times when you get `P2034`.

## 384: Why might you see P2028 errors?

`P2028` is a transaction API error, for example when a transaction already closed or expired, or when Prisma could not start a transaction in time (`maxWait` reached because the pool was busy). It often points to transactions that run too long, to code using `tx` after the transaction finished, or to a pool that is too small.

## 385: How do you run a query on a specific connection, like for SET statements?

A Prisma client uses a pool, so two queries may run on different connections. If you need a session setting for some queries, put them all in one interactive transaction, because a transaction always uses one connection.

```ts
await prisma.$transaction(async (tx) => {
  await tx.$executeRaw`SET LOCAL statement_timeout = '2s'`;
  return tx.report.findMany();
});
```

Use `SET LOCAL` (PostgreSQL) so the setting ends with the transaction and doesn't leak to other requests through the pool.

## 386: How do you use Prisma with Supabase?

Supabase is PostgreSQL, so you use `@prisma/adapter-pg`.

- Use the pooled connection string (Supavisor) for the app, in the adapter.
- Use the direct connection string for migrations, in `prisma.config.ts`.
- Supabase has its own schemas (`auth`, `storage`). Keep your tables in `public` or your own schema, and don't let Prisma Migrate manage Supabase's schemas.
- If you use Supabase RLS, Prisma connects as a database role that may bypass RLS, so check which role you use.

## 387: How do you use Prisma with PlanetScale?

PlanetScale offers MySQL (Vitess) and PostgreSQL. For MySQL on Vitess, foreign keys used to be unsupported, so many projects used `relationMode = "prisma"`. PlanetScale now supports foreign keys in many setups, so check your database settings.

You can use the PlanetScale serverless driver adapter (`@prisma/adapter-planetscale`) for edge runtimes, or a normal MySQL/MariaDB adapter for servers. PlanetScale also has its own branching and deploy request flow, which often replaces `migrate deploy` with `db push` on dev branches.

## 388: How do you deploy Prisma to a platform with read only file systems?

The generated client must be created at build time, not at run time, because `prisma generate` writes files. Run `prisma generate` in the build step and include the output folder in the deploy bundle. Since Prisma 7 has no engine binaries, there is nothing else to copy, which makes this much simpler than older versions.

## 389: How do you bundle Prisma with esbuild or a similar bundler?

With the `prisma-client` generator, the generated client is normal TypeScript, so the bundler can include it like any other code. The driver (like `pg`) is a normal dependency. Some drivers have optional native parts (`pg-native`), which you mark as external. With the old `prisma-client-js` generator, you had to mark `@prisma/client` as external and copy the engine files, which was a common source of deploy errors.

## 390: How do you run Prisma in Bun or Deno?

Set the generator `runtime` to `bun` or `deno` and use a driver adapter that works in that runtime, such as `@prisma/adapter-pg` for PostgreSQL. Bun loads `.env` files on its own. With Deno you may need permission flags for env and network access. Both can run TypeScript directly, so the generated `.ts` files work without a build step.

## 391: What is the role of migration checksums, and what if they don't match?

Each applied migration's SQL file is hashed and stored in `_prisma_migrations`. On `migrate dev`, Prisma compares the file hash with the stored hash. If someone edited an applied migration, Prisma reports it and asks to reset the dev database. `migrate deploy` warns too. To fix it, restore the original file (from git) and put the change into a new migration.

## 392: How do you handle migrations for many tenant schemas?

For schema per tenant, you run `migrate deploy` once per schema, pointing the URL at each schema (on PostgreSQL with `?schema=tenant_x` in the URL for the CLI). Things to plan:

- A script that loops over all tenants and records failures.
- What happens if migration fails for some tenants but not others, since your app must handle both versions for a while.
- Time: 1,000 tenants times a 10 second migration is almost 3 hours.

This is one of the main reasons many teams prefer a shared schema with `tenantId`.

## 393: How do you introspect only part of a database?

`prisma db pull` reads everything in the schemas it is configured for. To limit it:

- With `multiSchema`, list only the schemas you want in `schemas = [...]`.
- After pulling, add `@@ignore` to models you don't want in the client.
- Use a database user that can only see the tables you need.

Running `db pull` again keeps your `@map`, `@@map` and `@@ignore` changes, but other manual changes can be overwritten, so commit before you run it.

## 394: What does Prisma do when you rename a model?

Like renaming a field, Prisma Migrate sees a dropped table and a new table, so the default SQL deletes the data. To rename safely, either keep the old table name with `@@map("OldName")`, or edit the migration with `--create-only` and use `ALTER TABLE "OldName" RENAME TO "NewName"`. Remember to rename related foreign keys, indexes and sequences too, or the next diff will try to recreate them.

## 395: How do you handle generated or computed columns?

Prisma's schema can't declare database generated columns (`GENERATED ALWAYS AS ...`). You can:

- Add the column with raw SQL in a migration.
- Mark the field as optional in the schema so Prisma Client doesn't require it on create.
- Never write to it from Prisma.

The tricky part is drift. Migrate may see differences it can't express. Check the next `migrate dev` output and keep the generated column SQL in a migration so the shadow database has it too.

## 396: How do you debug "Prisma Client did not initialize" or "PrismaClient is not a constructor" errors?

These usually mean the generated client is missing or you import from the wrong place:

- Run `npx prisma generate` and check the `output` folder exists.
- In Prisma 7 import from the generated path (like `./generated/prisma/client`), not from `@prisma/client`.
- Check that the module format matches (ESM vs CommonJS) and set `moduleFormat` if needed.
- In a monorepo, check that every app points to the same generated folder.

## 397: How do you debug "too many connections" errors?

- Count how many `PrismaClient` instances you create. Look for clients created inside functions or reloaded by hot reload.
- Multiply the pool size by the number of instances, workers and serverless functions.
- Look for leaked connections from long transactions or unclosed scripts.
- Check the database (`SELECT * FROM pg_stat_activity` on PostgreSQL) to see which app and state the connections are in.

Then fix the source: a singleton client, a smaller pool, a pooler, and shorter transactions.

## 398: How do you investigate a query that is fast in SQL but slow through Prisma?

- Compare the SQL Prisma really sends (from the query log) with the one you tested. Prisma may add extra queries for includes or a `SELECT` after a write.
- Check the number of round trips and the network latency.
- Check how much data comes back. Mapping large results into objects takes time in JavaScript.
- Check whether parameters change the plan. A query with bound parameters may use a different plan than one with literal values.
- Check pool wait time. The query may be waiting for a connection, not running.

## 399: What is the impact of returning too many columns?

Selecting all columns means more data read from disk, more network traffic, more memory, and no chance for index only scans. Big `Text` or `Json` columns make this worse. On hot paths, use `select` with only the fields you need. For list pages this often makes a clear difference.

## 400: How do you use Prisma with an existing database that has naming conventions you don't like?

Run `db pull`, then map names in the schema so the code looks clean while the database stays the same:

```prisma
model UserAccount {
  id        Int      @id @default(autoincrement()) @map("user_account_id")
  createdAt DateTime @map("created_at")

  @@map("tbl_user_account")
}
```

Future `db pull` runs keep these mappings. This lets you introduce Prisma without renaming anything in the database.

## 401: How would you migrate a large app from TypeORM or Sequelize to Prisma?

1. Run `prisma db pull` on the existing database to get a schema, then clean up names with `@map` and `@@map`.
2. Baseline the migrations (`0_init` marked as applied) so Prisma Migrate can take over.
3. Stop the old ORM from running migrations or syncing the schema.
4. Move code module by module. Both ORMs can run side by side on the same database for a while.
5. Watch for behavior differences: lazy loading, entity hooks, default values set in code, and transactions that span both ORMs (they can't share one transaction).

Remove the old ORM only when nothing imports it anymore.

## 402: How do you replace entity lifecycle hooks (like beforeInsert) in Prisma?

Prisma has no entity hooks. Use:

- A query extension on `create` or `update` that changes `args.data` before the query.
- Database defaults and triggers for values that must always be set.
- Plain service functions that wrap the write and do the extra work.

```ts
const xprisma = prisma.$extends({
  query: {
    user: {
      async create({ args, query }) {
        args.data.email = args.data.email.toLowerCase();
        return query(args);
      },
    },
  },
});
```

Remember that `createMany`, `upsert` and nested creates are separate operations, so cover them too if needed.

## 403: How do you keep the Prisma schema and your API types from drifting apart?

- Don't expose Prisma models directly as your API contract. Define API types (DTOs) with Zod, OpenAPI or GraphQL.
- Map between the two in one place.
- Let TypeScript catch problems: when the schema changes and you regenerate, the mapping code fails to compile.

This way you can change the database without breaking API users, and you don't leak internal fields.

## 404: How do you handle schema changes when several app versions run at once?

During a rolling deploy, the old and new versions both run against the same database. Every migration must work with both:

- Adding an optional column or a table is safe.
- Adding a required column without a default breaks old code that inserts rows.
- Dropping or renaming a column breaks old code that reads it.

Use expand and contract: add first, deploy code, remove later. Also note that Prisma Client selects all scalar columns it knows about by name, so new columns are ignored by old code, but missing columns cause errors.

## 405: Why can dropping a column break a running Prisma app even if the code no longer uses it?

If the running app was generated from a schema that still has the column, Prisma Client still selects it by name in every query on that model (unless you use `select`). As soon as the column is dropped, those queries fail with a "column does not exist" error. Deploy the code with the column removed from the schema first, then drop the column in a later migration.

## 406: How do you safely change a column type, like Int to BigInt?

Changing the type in place can lock the table and rewrite all rows. On big tables:

1. Add a new column `idNew BigInt?`.
2. Write to both columns in the app.
3. Backfill in batches.
4. Switch reads to the new column.
5. Drop the old column and rename the new one (with `@map` or SQL).

For small tables, a direct `ALTER COLUMN ... TYPE` in a migration is fine.

## 407: How do you design for audit and history, like keeping all versions of a document?

Keep a separate history table and write to it in the same transaction as the main update.

```prisma
model Document {
  id       String            @id @default(uuid(7))
  title    String
  body     String
  version  Int               @default(1)
  versions DocumentVersion[]
}

model DocumentVersion {
  id         String   @id @default(uuid(7))
  documentId String
  document   Document @relation(fields: [documentId], references: [id], onDelete: Cascade)
  version    Int
  body       String
  createdAt  DateTime @default(now())

  @@unique([documentId, version])
}
```

The `@@unique` on `[documentId, version]` also stops two writers from saving the same version.

## 408: How do you build a reliable job queue table with Prisma?

On PostgreSQL, use `SELECT ... FOR UPDATE SKIP LOCKED` so many workers can take jobs without fighting.

```ts
const jobs = await prisma.$transaction(async (tx) => {
  const rows = await tx.$queryRaw<{ id: string }[]>`
    SELECT id FROM "Job"
    WHERE status = 'PENDING' AND "runAt" <= now()
    ORDER BY "runAt"
    LIMIT 10
    FOR UPDATE SKIP LOCKED
  `;
  const ids = rows.map((r) => r.id);
  await tx.job.updateMany({
    where: { id: { in: ids } },
    data: { status: "RUNNING" },
  });
  return ids;
});
```

Each worker gets different jobs. Add a timeout so jobs stuck in `RUNNING` get picked up again.

## 409: How do you use LISTEN/NOTIFY with Prisma?

Prisma Client doesn't support `LISTEN`, because it needs a dedicated long lived connection, and Prisma uses a pool. Use the `pg` driver directly for the listener, and Prisma for normal queries. You can still send `NOTIFY` through Prisma with `$executeRaw`.

```ts
await prisma.$executeRaw`SELECT pg_notify('orders', ${JSON.stringify({ id })})`;
```

## 410: How would you get real time database changes in a Prisma app?

Options:

- Publish events from your app after writes (outbox pattern for reliability).
- Use PostgreSQL logical replication or a change data capture tool like Debezium.
- Use `LISTEN/NOTIFY` with a separate `pg` connection for light use.
- Use a managed service like Supabase Realtime.

Prisma Client itself only runs queries; it does not stream changes.

## 411: What do you need to know about Prisma and MongoDB today?

- MongoDB works with Prisma 6, but Prisma 7 does not support it yet, so stay on 6 for MongoDB.
- You use `prisma db push`, not `prisma migrate`, because MongoDB has no fixed schema.
- Ids are usually `id String @id @default(auto()) @map("_id") @db.ObjectId`.
- MongoDB supports composite types (`type Address { ... }`) for embedded documents.
- Transactions need a replica set.
- There are `$runCommandRaw`, `findRaw` and `aggregateRaw` for raw operations.

## 412: What are composite types in Prisma?

Composite types are embedded objects, only for MongoDB. They describe the shape of a sub document.

```prisma
type Address {
  street String
  city   String
}

model Customer {
  id      String  @id @default(auto()) @map("_id") @db.ObjectId
  address Address
}
```

They are typed in Prisma Client and can be filtered and updated. On relational databases you would use a separate table or a `Json` field instead.

## 413: What are the main breaking changes to watch for when upgrading major Prisma versions in general?

Prisma major versions have changed things like:

- Required Node.js and TypeScript versions.
- Default generators and import paths (Prisma 7).
- How the client connects (driver adapters in Prisma 7).
- Removed APIs (like `rejectOnNotFound` in 5, `$use` and metrics in 7).
- Type changes (like `Buffer` to `Uint8Array` for `Bytes` in 6).
- CLI behavior (like `migrate dev` no longer generating or seeding in 7).

Read the official upgrade guide for each major version, upgrade one major at a time, and run your full test suite against a real database.

## 414: What is the status of Prisma 8?

At the time of writing, Prisma 8 is in the release candidate stage, not a final release. It brings more breaking changes and higher minimum versions (Node.js 22.18+ and TypeScript 5.9+). Prisma 7 is still supported. Prisma 7.10 added a `@prisma/prisma7` package and a `prisma7.config.ts` file name so Prisma 7 and Prisma 8 CLIs can live in the same project during an upgrade. For production apps, stay on Prisma 7 until 8 is stable and you have read its upgrade guide.

## 415: How do you run Prisma 7 and Prisma 8 side by side during an upgrade?

Prisma 7.10 added the `@prisma/prisma7` package. With it, the Prisma 8 CLI is `prisma` and the Prisma 7 CLI is `prisma7` (for example `npx prisma7 generate`). The Prisma 7 CLI looks for `prisma7.config.*` first and falls back to `prisma.config.*`, so each version can have its own config. This is meant for moving step by step, not for running both forever.

## 416: What would you check in code review for a Prisma query?

- Is `select` or `omit` used so we don't return sensitive or unneeded fields?
- Is there a `take` limit on list queries?
- Can a filter value be `undefined` and remove a condition?
- Is the user's ownership or tenant checked in the `where`?
- Is there an index for this `where` and `orderBy`?
- Are related records loaded in one go, not in a loop?
- Are transactions short and using `tx`?
- Is raw SQL parameterized?

## 417: What would you check in code review for a Prisma migration?

- Does it drop or rename columns or tables? Is data kept?
- Does it add a required column to a table with data, without a default?
- Will it lock a large table for a long time (new index, type change)?
- Does it work with the currently deployed code version?
- Is any custom SQL (data fixes, triggers) correct and repeatable?
- Has it been tested on realistic data sizes?

## 418: A deploy failed because a migration timed out on a big table. What do you do?

First check the database: is the migration still running, did it finish, or did it roll back? Then:

1. If it rolled back, mark it with `migrate resolve --rolled-back`.
2. Rewrite the migration to be online: add indexes with `CONCURRENTLY`, add columns without defaults that rewrite the table, backfill in batches with a script.
3. Split it into several smaller migrations if needed.
4. Run it in a quiet time window if it can't be fully online.

Also set a `lock_timeout` in the migration SQL so it fails fast instead of blocking all traffic while it waits for a lock.

## 419: Users report that a list page is slow. How do you investigate it?

1. Turn on query logging with durations for that endpoint, or check traces.
2. Count the queries. Many similar queries mean N+1.
3. Find the slowest query and run `EXPLAIN ANALYZE` on it.
4. Check for missing indexes on filter and sort columns, and for big `skip` values.
5. Check how much data is loaded: deep `include`, big text columns, no `take`.
6. Fix it: add indexes, use `select`, use cursor pagination, use `relationJoins`, or rewrite the hot query in SQL.

## 420: After moving to serverless, the database hits its connection limit. What do you do?

- Make sure the client is created once per function instance, outside the handler.
- Lower the pool size on the adapter, often to 1 or a few connections.
- Add a pooler (PgBouncer, Supavisor, RDS Proxy, Neon pooler) and point the app at it.
- Or switch to an HTTP based driver adapter.
- Keep the direct URL only for migrations in `prisma.config.ts`.
- Check that transactions are short, so connections are returned quickly.

## 421: A deleteMany removed all rows in production. What went wrong and how do you prevent it?

Most likely the filter value was `undefined`, so Prisma dropped the condition and deleted everything. Prevention:

- Validate input before building queries.
- Turn on `strictUndefinedChecks` so explicit `undefined` throws, and use `Prisma.skip` on purpose.
- Add a guard extension that refuses `deleteMany` and `updateMany` with an empty `where`.
- Keep backups and test restores, and use soft delete for important data.

```ts
const guarded = prisma.$extends({
  query: {
    $allModels: {
      async deleteMany({ args, query }) {
        if (!args.where || Object.keys(args.where).length === 0) {
          throw new Error("deleteMany without a filter is not allowed");
        }
        return query(args);
      },
    },
  },
});
```

## 422: Two users signed up with the same email at the same time and you got a 500 error. How do you fix it?

The code probably checked "does the email exist?" and then created the user. Both requests passed the check before either insert. The unique constraint correctly rejected the second insert with `P2002`, but the code didn't handle it.

Fix: rely on the unique constraint, catch `P2002` and return a 409 "email already in use" response. Don't depend on the check query for correctness, only for a nicer message.

## 423: A report query takes 30 seconds. How would you approach it with Prisma?

- Check if it can use existing data better: indexes, a smaller date range, pre filtering.
- Move it to raw SQL or TypedSQL with proper aggregation, CTEs and window functions, instead of loading rows and summing in JavaScript.
- Run it on a read replica so it doesn't slow the main database.
- Precompute: a materialized view refreshed on a schedule, or a summary table updated by a job.
- Cache the result if the data doesn't need to be live.

## 424: You see "Transaction already closed" errors under load. What is happening?

The interactive transaction is running longer than its `timeout` (5 seconds by default), so Prisma closes it, and later `tx` calls fail. Under load it gets worse because queries wait longer for locks and connections. Check:

- Slow work or external API calls inside the transaction. Move them out.
- Pool exhaustion causing waits. Increase the pool or reduce parallel work.
- Missing indexes making queries inside the transaction slow.

Increase `timeout` only after you understand why the transaction is slow.

## 425: How would you add full text search to a Prisma app on PostgreSQL at scale?

1. Add a `tsvector` column (generated column or trigger) with raw SQL in a migration, marked `Unsupported("tsvector")?` in the schema.
2. Add a GIN index on it.
3. Query with TypedSQL or `$queryRaw` using `to_tsquery` and `ts_rank`.

```sql
SELECT id, title, ts_rank(search, q) AS rank
FROM "Post", to_tsquery('english', $1) q
WHERE search @@ q
ORDER BY rank DESC
LIMIT 20;
```

The `fullTextSearchPostgres` preview `search` filter works for simple cases, but it computes the vector on the fly, which doesn't scale to large tables. For more advanced needs, use a search engine like Meilisearch or Elasticsearch.

## 426: How do you design a schema so that queries scale as data grows?

- Index for your real access patterns and check them with `EXPLAIN`.
- Use cursor pagination for large lists.
- Keep hot tables narrow. Move big, rarely read columns (like large JSON or text) to a separate table.
- Use time ordered ids (UUID v7, ULID) or integers for better index locality.
- Plan for archiving or partitioning large, time based tables (partitioning needs raw SQL).
- Avoid storing ever growing arrays or JSON in one row.

## 427: Does Prisma support table partitioning?

Prisma's schema doesn't describe partitions, but you can create a partitioned table with raw SQL in a migration. Prisma Client queries the parent table as normal. Things to watch:

- Primary keys and unique constraints on partitioned tables must include the partition key, so the Prisma schema must match (for example `@@id([id, createdAt])`).
- Migrate may report drift for partition tables, so check diffs carefully and keep partition management (creating new partitions) in SQL or a scheduled job.

## 428: How do you handle very wide tables or JSON heavy rows?

- Use `select` to avoid loading large columns on list queries.
- Split rarely used large fields into a one-to-one side table.
- Index JSON paths you filter on (GIN or expression indexes) with SQL migrations.
- If you filter and sort a lot on fields inside the JSON, move those fields into real columns.

## 429: What is the effect of Prisma's dataloader on findUnique with different selects?

Batching only happens for calls with the same model and the same shape of `select` or `include`. If two resolvers call `findUnique` on the same user but select different fields, Prisma can't merge them into one query, and you get separate queries. In GraphQL, keeping selections consistent (or using the fluent API) helps batching work.

## 430: How do you make Prisma Client work in a browser or React Native?

You don't run Prisma Client against a remote database from the browser, because that would expose your credentials. Prisma Client is for server code. For the browser, you import only types and enums from `browser.ts`. For React Native, the `react-native` runtime option exists for local, on device databases like SQLite inside the app, not for talking to your server database directly.

## 431: How do you restrict which fields an API can sort or filter by?

Never pass user input straight into `orderBy` or `where`. Build them from an allow list.

```ts
const sortable = { createdAt: true, title: true } as const;
type SortField = keyof typeof sortable;

function buildOrderBy(
  field: string,
  dir: string,
): Prisma.PostOrderByWithRelationInput {
  const f: SortField = field in sortable ? (field as SortField) : "createdAt";
  return { [f]: dir === "asc" ? "asc" : "desc" };
}
```

Letting users sort by any field can also cause slow queries on columns without indexes.

## 432: How do you protect against denial of service through expensive Prisma queries?

- Cap `take` on every list endpoint.
- Don't let clients choose arbitrary `include` depth (especially in GraphQL; add query depth and cost limits).
- Avoid unbounded `contains` searches on large tables without indexes, or rate limit them.
- Set statement timeouts on the database user.
- Use a small, fixed pool so one endpoint can't take all connections.

## 433: How should you store secrets like the database URL for Prisma?

Keep `DATABASE_URL` out of git and out of Docker images. Use your platform's secret manager or environment settings. In Prisma 7 you load env vars yourself, so make sure production doesn't rely on a `.env` file that might be missing. Use separate credentials per environment, and different users for migrations and for the app.

## 434: How do you design error handling for Prisma in a large codebase?

- Map Prisma errors to your own domain errors in one place (for example `NotFoundError`, `ConflictError`).
- Don't leak Prisma error messages or `meta` to API clients.
- Log the full error with the code and model on the server.
- Use `P2002` and `P2003` for business responses (409 and 400), and treat unknown errors as 500.
- Handle retryable errors (`P2034`, some connection errors) with limited retries.

## 435: What happens to the client if the database restarts?

The pool's connections break. With a driver adapter, the underlying driver handles this. `pg` removes broken connections and opens new ones on the next query. Queries that were running at that moment fail with a connection error. Your app should handle these errors (retry idempotent reads, return 503 for writes) instead of crashing, and the health check should report the database status.

## 436: How do you implement a health check that uses Prisma?

```ts
app.get("/health/db", async (_req, res) => {
  try {
    await prisma.$queryRaw`SELECT 1`;
    res.json({ db: "ok" });
  } catch {
    res.status(503).json({ db: "down" });
  }
});
```

Keep the check cheap and use a short timeout. Don't run it so often that it adds real load.

## 437: How do you make sure a Prisma based service starts only when the database schema is ready?

- Run `prisma migrate deploy` before starting the new version (separate pipeline step or init container).
- Optionally check `prisma migrate status` in the pipeline and fail if there are pending or failed migrations.
- Make the app's readiness check include a database query, so traffic only comes once it can connect.

Don't make the app run migrations itself in a multi instance setup.

## 438: How would you test a client extension?

Test it against a real database (for example a test container) with a client that has the extension applied.

```ts
it("hides soft deleted posts", async () => {
  const post = await xprisma.post.create({ data: { title: "x" } });
  await xprisma.post.softDelete(post.id);

  const found = await xprisma.post.findMany();
  expect(found.find((p) => p.id === post.id)).toBeUndefined();
});
```

Also test the cases the extension should not touch, like raw queries or other models, so the limits are clear.

## 439: What are the trade-offs of putting business logic in database triggers versus Prisma extensions?

Triggers:

- Run for every write, including raw SQL and other services.
- Are hard to see, test and version for developers who only look at TypeScript.
- Prisma Client doesn't know about them.

Extensions:

- Are easy to read, type and test in your app.
- Only run when the write goes through that extended client.

Use triggers for rules that must always hold (audit, integrity), and extensions for app level behavior.

## 440: How do you handle time based data like events with high write volume?

- Use a time ordered id or `(deviceId, timestamp)` key.
- Insert in batches with `createMany`.
- Index by the time columns you query.
- Partition by time or use an extension like TimescaleDB, set up with raw SQL.
- Archive or delete old data on a schedule.
- Consider whether a dedicated time series or analytics database is a better fit than your main OLTP database.

## 441: How do you handle unique constraints across case variations, like emails?

On PostgreSQL, a normal unique index treats `Ann@x.com` and `ann@x.com` as different. Options:

- Always store lowercase (normalize in a query extension or service code).
- Use `citext` (`@db.Citext`) so the column compares case insensitive.
- Create a unique index on `lower(email)` with raw SQL.

Normalizing in code plus a database level guard is the safest combination.

## 442: How do you use Prisma with Next.js Server Components and Server Actions?

Call Prisma directly in server components and server actions, never in client components.

```tsx
// app/posts/page.tsx (server component)
import { prisma } from "@/lib/prisma";

export default async function Page() {
  const posts = await prisma.post.findMany({
    select: { id: true, title: true },
    take: 20,
  });
  return (
    <ul>
      {posts.map((p) => (
        <li key={p.id}>{p.title}</li>
      ))}
    </ul>
  );
}
```

Use a singleton client, validate inputs in server actions, check authorization there, and only pass plain serializable data to client components (watch for `Date`, `Decimal` and `bigint`).

## 443: How do you keep Prisma queries out of the edge middleware in Next.js?

Next.js middleware runs on the edge runtime by default, where TCP drivers like `pg` don't work. Options:

- Don't query the database in middleware. Check a signed cookie or JWT instead.
- If you must, use an HTTP based driver adapter (like Neon) and the matching generator `runtime`.
- Or switch the middleware to the Node.js runtime where your Next.js version supports it.

Keeping middleware database free is usually the best choice for speed.

## 444: How would you explain the difference between Prisma's schema first approach and a code first approach?

Schema first (Prisma): you write a `.prisma` file, and code (types and client) is generated from it. The schema is easy to read and is the one source of truth, but you need a generate step and a separate language.

Code first (Drizzle, TypeORM, MikroORM): you define tables in TypeScript, and types come from that code. No generate step and no new language, but the schema is spread over code and can be harder to read as a whole.

## 445: How do you plan a Prisma 6 to 7 upgrade in a big production app?

1. Read the upgrade guide and list what affects you (ESM, adapters, imports, `$use`, metrics, env loading, seeding).
2. Upgrade Node.js and TypeScript first if needed.
3. Replace `$use` with extensions while still on Prisma 6.
4. Switch to the `prisma-client` generator with driver adapters on Prisma 6 (both are available there), and test.
5. Then upgrade to 7, move URLs to `prisma.config.ts`, and update CI scripts (explicit `generate` and `db seed`).
6. Load test, since pool and timeout defaults change with adapters.
7. Roll out gradually and watch connection counts, errors and latency.

## 446: Why might query results differ slightly after moving to driver adapters?

The driver now parses some values instead of the Rust engine. Things to check after upgrading:

- Date and time handling, especially `timestamp` without time zone.
- Numeric precision for `Decimal` and big integers in raw queries.
- Raw query result types (for example, how `pg` returns `numeric` or `int8` columns).
- Error codes and messages for constraint violations, which are mapped from driver errors.

Run your integration tests with real data to catch these.

## 447: What metrics would you monitor for a Prisma based service?

- Query latency (p50, p95, p99) per model and operation, from tracing.
- Number of queries per request.
- Error rates by Prisma error code.
- Pool usage: active, idle and waiting connections from the driver.
- Transaction durations and timeouts.
- Database side: CPU, locks, slow queries, connection count.

## 448: How would you onboard a team that is new to Prisma?

- Walk through the schema file and the generated client together.
- Agree on rules: singleton client, `select` on list endpoints, `take` limits, error mapping, no `req.body` in `data`.
- Show the migration workflow: `migrate dev` locally, `migrate deploy` in CI, and never editing applied migrations.
- Turn on query logging in development so people see the SQL.
- Add lint rules or code review checklists for the common mistakes.

## 449: What are the most common mistakes developers make with Prisma?

- Creating a new `PrismaClient` per request.
- Forgetting to run `prisma generate` after a schema change.
- Using `db push` on a database that also uses migrations, and causing drift.
- Renaming fields and losing data because of the generated drop and add SQL.
- Loading huge relations with `include` and no limits.
- Passing `undefined` in filters by accident.
- Using `prisma` instead of `tx` inside interactive transactions.
- Building raw SQL with string concatenation.

## 450: What is your overall approach to using Prisma well in production?

Treat Prisma as a helpful layer over SQL, not a replacement for knowing SQL. Keep one client per process, keep transactions short, select only what you need, and add indexes based on real queries. Use migrations for every change, review them like code, and apply them with `migrate deploy` before the new code goes out. Watch your queries with logging and tracing, drop down to TypedSQL or raw SQL when the API isn't enough, and read the upgrade guide carefully before every major version.
