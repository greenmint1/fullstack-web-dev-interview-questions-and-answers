# Mongoose Interview Questions and Answers

_Last updated: October 28, 2026_

450 Mongoose interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers are written for **Mongoose 9** (the latest release at the time of writing is 9.11), which uses the MongoDB Node.js driver 7 and needs Node.js 20.19 or newer. Most answers also apply to Mongoose 8. When something works differently in a recent version, the answer says so.

Code examples use JavaScript with ES modules and `async`/`await`, unless they say TypeScript.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is Mongoose?](#1-what-is-mongoose)
- [2: What is an ODM?](#2-what-is-an-odm)
- [3: What is the difference between Mongoose and the native MongoDB driver?](#3-what-is-the-difference-between-mongoose-and-the-native-mongodb-driver)
- [4: How do you install Mongoose?](#4-how-do-you-install-mongoose)
- [5: How do you connect to MongoDB with Mongoose?](#5-how-do-you-connect-to-mongodb-with-mongoose)
- [6: What does a MongoDB connection string look like?](#6-what-does-a-mongodb-connection-string-look-like)
- [7: What is the default connection in Mongoose?](#7-what-is-the-default-connection-in-mongoose)
- [8: How do you listen to connection events?](#8-how-do-you-listen-to-connection-events)
- [9: How do you close a Mongoose connection?](#9-how-do-you-close-a-mongoose-connection)
- [10: What is a schema in Mongoose?](#10-what-is-a-schema-in-mongoose)
- [11: What is a model?](#11-what-is-a-model)
- [12: What is a document in Mongoose?](#12-what-is-a-document-in-mongoose)
- [13: How does Mongoose pick the collection name for a model?](#13-how-does-mongoose-pick-the-collection-name-for-a-model)
- [14: What schema types does Mongoose support?](#14-what-schema-types-does-mongoose-support)
- [15: What is the difference between the short and long way to define a field?](#15-what-is-the-difference-between-the-short-and-long-way-to-define-a-field)
- [16: What options are available for String fields?](#16-what-options-are-available-for-string-fields)
- [17: What options are available for Number fields?](#17-what-options-are-available-for-number-fields)
- [18: How do Date fields work?](#18-how-do-date-fields-work)
- [19: How does Mongoose cast Boolean values?](#19-how-does-mongoose-cast-boolean-values)
- [20: What is the ObjectId type used for?](#20-what-is-the-objectid-type-used-for)
- [21: How do you define an array field?](#21-how-do-you-define-an-array-field)
- [22: What is the Mixed type?](#22-what-is-the-mixed-type)
- [23: What is the Map type?](#23-what-is-the-map-type)
- [24: When would you use the Buffer type?](#24-when-would-you-use-the-buffer-type)
- [25: What is Decimal128 used for?](#25-what-is-decimal128-used-for)
- [26: Does Mongoose support BigInt?](#26-does-mongoose-support-bigint)
- [27: How does the UUID type work?](#27-how-does-the-uuid-type-work)
- [28: What are the Int32 and Double types?](#28-what-are-the-int32-and-double-types)
- [29: How do you define nested objects in a schema?](#29-how-do-you-define-nested-objects-in-a-schema)
- [30: What is a subdocument?](#30-what-is-a-subdocument)
- [31: How do you create and save a document?](#31-how-do-you-create-and-save-a-document)
- [32: What does Model.create() do?](#32-what-does-modelcreate-do)
- [33: What is the difference between create() and insertMany()?](#33-what-is-the-difference-between-create-and-insertmany)
- [34: What is Model.insertOne()?](#34-what-is-modelinsertone)
- [35: How do you find documents?](#35-how-do-you-find-documents)
- [36: What is the difference between find() and findOne()?](#36-what-is-the-difference-between-find-and-findone)
- [37: How do you find a document by its _id?](#37-how-do-you-find-a-document-by-its-_id)
- [38: How do you use query operators in Mongoose?](#38-how-do-you-use-query-operators-in-mongoose)
- [39: How do you select only some fields?](#39-how-do-you-select-only-some-fields)
- [40: How do you sort results?](#40-how-do-you-sort-results)
- [41: How do you limit and skip results?](#41-how-do-you-limit-and-skip-results)
- [42: How do you count documents?](#42-how-do-you-count-documents)
- [43: How do you get distinct values of a field?](#43-how-do-you-get-distinct-values-of-a-field)
- [44: How do you check if a document exists?](#44-how-do-you-check-if-a-document-exists)
- [45: How do you update one document?](#45-how-do-you-update-one-document)
- [46: How do you update many documents?](#46-how-do-you-update-many-documents)
- [47: What does findOneAndUpdate() do?](#47-what-does-findoneandupdate-do)
- [48: What is findByIdAndUpdate()?](#48-what-is-findbyidandupdate)
- [49: What is the difference between updateOne() and replaceOne()?](#49-what-is-the-difference-between-updateone-and-replaceone)
- [50: How do you delete documents?](#50-how-do-you-delete-documents)
- [51: How do you delete a document and get it back?](#51-how-do-you-delete-a-document-and-get-it-back)
- [52: How do you delete a document you already loaded?](#52-how-do-you-delete-a-document-you-already-loaded)
- [53: What is the _id field?](#53-what-is-the-_id-field)
- [54: What is the id virtual?](#54-what-is-the-id-virtual)
- [55: What is the __v field?](#55-what-is-the-__v-field)
- [56: What does the timestamps option do?](#56-what-does-the-timestamps-option-do)
- [57: How does the required validator work?](#57-how-does-the-required-validator-work)
- [58: How do you validate number ranges?](#58-how-do-you-validate-number-ranges)
- [59: How do you validate string length?](#59-how-do-you-validate-string-length)
- [60: How does the enum validator work?](#60-how-does-the-enum-validator-work)
- [61: How do you validate a string with a regular expression?](#61-how-do-you-validate-a-string-with-a-regular-expression)
- [62: How do you write a custom validator?](#62-how-do-you-write-a-custom-validator)
- [63: When does Mongoose run validation?](#63-when-does-mongoose-run-validation)
- [64: What error do you get when validation fails?](#64-what-error-do-you-get-when-validation-fails)
- [65: Is unique a validator?](#65-is-unique-a-validator)
- [66: How do you set a default value?](#66-how-do-you-set-a-default-value)
- [67: When are default values applied?](#67-when-are-default-values-applied)
- [68: What do lowercase, uppercase and trim do?](#68-what-do-lowercase-uppercase-and-trim-do)
- [69: What is casting in Mongoose?](#69-what-is-casting-in-mongoose)
- [70: What is a CastError?](#70-what-is-a-casterror)
- [71: What does strict mode do?](#71-what-does-strict-mode-do)
- [72: What is strictQuery?](#72-what-is-strictquery)
- [73: Are Mongoose queries promises?](#73-are-mongoose-queries-promises)
- [74: What is exec() for?](#74-what-is-exec-for)
- [75: Do Mongoose methods still accept callbacks?](#75-do-mongoose-methods-still-accept-callbacks)
- [76: What does lean() do?](#76-what-does-lean-do)
- [77: How do you use your own value for _id?](#77-how-do-you-use-your-own-value-for-_id)
- [78: How do you add instance methods to a model?](#78-how-do-you-add-instance-methods-to-a-model)
- [79: How do you add static methods to a model?](#79-how-do-you-add-static-methods-to-a-model)
- [80: What is a virtual?](#80-what-is-a-virtual)
- [81: Can a virtual have a setter?](#81-can-a-virtual-have-a-setter)
- [82: Why are virtuals missing from my JSON response?](#82-why-are-virtuals-missing-from-my-json-response)
- [83: What is a getter?](#83-what-is-a-getter)
- [84: What is a setter?](#84-what-is-a-setter)
- [85: What is middleware in Mongoose?](#85-what-is-middleware-in-mongoose)
- [86: How do you write a pre save hook?](#86-how-do-you-write-a-pre-save-hook)
- [87: How do you write a post hook?](#87-how-do-you-write-a-post-hook)
- [88: What kinds of middleware does Mongoose have?](#88-what-kinds-of-middleware-does-mongoose-have)
- [89: What is populate()?](#89-what-is-populate)
- [90: What does the ref option do?](#90-what-does-the-ref-option-do)
- [91: How do you populate only some fields?](#91-how-do-you-populate-only-some-fields)
- [92: How do you populate more than one field?](#92-how-do-you-populate-more-than-one-field)
- [93: How do you store a list of references?](#93-how-do-you-store-a-list-of-references)
- [94: How do you add an index to a field?](#94-how-do-you-add-an-index-to-a-field)
- [95: What is autoIndex?](#95-what-is-autoindex)
- [96: How do you see the queries Mongoose sends?](#96-how-do-you-see-the-queries-mongoose-sends)
- [97: How do you create an ObjectId by hand?](#97-how-do-you-create-an-objectid-by-hand)
- [98: How do you check if a string is a valid ObjectId?](#98-how-do-you-check-if-a-string-is-a-valid-objectid)
- [99: What is the difference between toObject() and toJSON()?](#99-what-is-the-difference-between-toobject-and-tojson)
- [100: What does isModified() do?](#100-what-does-ismodified-do)
- [101: What is isNew?](#101-what-is-isnew)
- [102: When do you need markModified()?](#102-when-do-you-need-markmodified)
- [103: How do you hide a field by default?](#103-how-do-you-hide-a-field-by-default)
- [104: What is an alias in a schema?](#104-what-is-an-alias-in-a-schema)
- [105: What does orFail() do?](#105-what-does-orfail-do)
- [106: How does query chaining work?](#106-how-does-query-chaining-work)
- [107: How does the where() query builder work?](#107-how-does-the-where-query-builder-work)
- [108: How do you search with a regular expression?](#108-how-do-you-search-with-a-regular-expression)
- [109: How do you push a value into an array?](#109-how-do-you-push-a-value-into-an-array)
- [110: What is the difference between $push and $addToSet?](#110-what-is-the-difference-between-push-and-addtoset)
- [111: How do you get and set values on a document?](#111-how-do-you-get-and-set-values-on-a-document)
- [112: Does save() insert or update?](#112-does-save-insert-or-update)
- [113: What is command buffering?](#113-what-is-command-buffering)
- [114: How do you check the state of the connection?](#114-how-do-you-check-the-state-of-the-connection)
- [115: What is OverwriteModelError?](#115-what-is-overwritemodelerror)
- [116: How do you organize models in a project?](#116-how-do-you-organize-models-in-a-project)
- [117: How do you use Mongoose with ES modules and CommonJS?](#117-how-do-you-use-mongoose-with-es-modules-and-commonjs)
- [118: Where should you keep the connection string?](#118-where-should-you-keep-the-connection-string)
- [119: What are the most used schema options?](#119-what-are-the-most-used-schema-options)
- [120: How do you turn off _id for subdocuments?](#120-how-do-you-turn-off-_id-for-subdocuments)
- [121: What does the minimize option do?](#121-what-does-the-minimize-option-do)
- [122: How do you make an array field required?](#122-how-do-you-make-an-array-field-required)
- [123: When should you embed data and when should you reference it?](#123-when-should-you-embed-data-and-when-should-you-reference-it)
- [124: How do you model a one-to-many relationship?](#124-how-do-you-model-a-one-to-many-relationship)
- [125: How do you model a many-to-many relationship?](#125-how-do-you-model-a-many-to-many-relationship)
- [126: How do you get a plain object from a document?](#126-how-do-you-get-a-plain-object-from-a-document)
- [127: How do you sort by more than one field?](#127-how-do-you-sort-by-more-than-one-field)
- [128: How do you do simple pagination with a total count?](#128-how-do-you-do-simple-pagination-with-a-total-count)
- [129: What are the main Mongoose error types?](#129-what-are-the-main-mongoose-error-types)
- [130: How do you handle a duplicate key error?](#130-how-do-you-handle-a-duplicate-key-error)
- [131: How do you delete all documents in a collection?](#131-how-do-you-delete-all-documents-in-a-collection)
- [132: How do you drop a collection or a database?](#132-how-do-you-drop-a-collection-or-a-database)
- [133: How do you compare two ObjectIds?](#133-how-do-you-compare-two-objectids)
- [134: How do you check if a path is populated?](#134-how-do-you-check-if-a-path-is-populated)
- [135: Does Mongoose support TypeScript?](#135-does-mongoose-support-typescript)
- [136: What is the current version of Mongoose and what does it need?](#136-what-is-the-current-version-of-mongoose-and-what-does-it-need)
- [137: What is a discriminator?](#137-what-is-a-discriminator)
- [138: What is a Mongoose plugin?](#138-what-is-a-mongoose-plugin)
- [139: How do you use Mongoose in an Express app?](#139-how-do-you-use-mongoose-in-an-express-app)
- [140: How do you close the connection when the app stops?](#140-how-do-you-close-the-connection-when-the-app-stops)
- [141: What does Model.find() return when nothing matches?](#141-what-does-modelfind-return-when-nothing-matches)
- [142: How do you query fields inside nested objects?](#142-how-do-you-query-fields-inside-nested-objects)
- [143: How do you update a nested field?](#143-how-do-you-update-a-nested-field)
- [144: How do you increment a number?](#144-how-do-you-increment-a-number)
- [145: What does Model.findOneAndUpdate() do with upsert?](#145-what-does-modelfindoneandupdate-do-with-upsert)
- [146: How do you get the raw MongoDB collection from a model?](#146-how-do-you-get-the-raw-mongodb-collection-from-a-model)
- [147: What are immutable fields?](#147-what-are-immutable-fields)
- [148: Can a field be required only in some cases?](#148-can-a-field-be-required-only-in-some-cases)
- [149: How do you seed a database with Mongoose?](#149-how-do-you-seed-a-database-with-mongoose)
- [150: What are common beginner mistakes with Mongoose?](#150-what-are-common-beginner-mistakes-with-mongoose)

### Moderate Questions (151-300)

- [151: What connection options do you usually set in production?](#151-what-connection-options-do-you-usually-set-in-production)
- [152: How do you connect to more than one database?](#152-how-do-you-connect-to-more-than-one-database)
- [153: What does useDb() do?](#153-what-does-usedb-do)
- [154: How does the connection pool work?](#154-how-does-the-connection-pool-work)
- [155: How do you handle a failed first connection?](#155-how-do-you-handle-a-failed-first-connection)
- [156: What changed about pre middleware in Mongoose 9?](#156-what-changed-about-pre-middleware-in-mongoose-9)
- [157: How do you stop an operation from inside a pre hook?](#157-how-do-you-stop-an-operation-from-inside-a-pre-hook)
- [158: What is this inside query middleware?](#158-what-is-this-inside-query-middleware)
- [159: Why does a pre save hook not run on findOneAndUpdate()?](#159-why-does-a-pre-save-hook-not-run-on-findoneandupdate)
- [160: How do you register a hook for document or query deleteOne?](#160-how-do-you-register-a-hook-for-document-or-query-deleteone)
- [161: What is error handling middleware?](#161-what-is-error-handling-middleware)
- [162: How do you use aggregate middleware?](#162-how-do-you-use-aggregate-middleware)
- [163: Which operations do not run save middleware?](#163-which-operations-do-not-run-save-middleware)
- [164: How do you run validators on updates?](#164-how-do-you-run-validators-on-updates)
- [165: What is this inside an update validator?](#165-what-is-this-inside-an-update-validator)
- [166: How do you write an async validator?](#166-how-do-you-write-an-async-validator)
- [167: What is validateSync()?](#167-what-is-validatesync)
- [168: How do you validate a document without saving it?](#168-how-do-you-validate-a-document-without-saving-it)
- [169: What does doc.invalidate() do?](#169-what-does-docinvalidate-do)
- [170: How do you format validation errors for an API?](#170-how-do-you-format-validation-errors-for-an-api)
- [171: How do you populate nested references?](#171-how-do-you-populate-nested-references)
- [172: What options does populate() take?](#172-what-options-does-populate-take)
- [173: What is the difference between limit and perDocumentLimit in populate?](#173-what-is-the-difference-between-limit-and-perdocumentlimit-in-populate)
- [174: What happens if populate() cannot find a referenced document?](#174-what-happens-if-populate-cannot-find-a-referenced-document)
- [175: What is virtual populate?](#175-what-is-virtual-populate)
- [176: How do you get a count with virtual populate?](#176-how-do-you-get-a-count-with-virtual-populate)
- [177: What is refPath?](#177-what-is-refpath)
- [178: Does populate() work with lean()?](#178-does-populate-work-with-lean)
- [179: How do you populate a document you already loaded?](#179-how-do-you-populate-a-document-you-already-loaded)
- [180: How do you populate across connections?](#180-how-do-you-populate-across-connections)
- [181: How do discriminators store the type?](#181-how-do-discriminators-store-the-type)
- [182: What are embedded discriminators?](#182-what-are-embedded-discriminators)
- [183: How do you work with arrays of subdocuments?](#183-how-do-you-work-with-arrays-of-subdocuments)
- [184: How do you update one item in an array with an update query?](#184-how-do-you-update-one-item-in-an-array-with-an-update-query)
- [185: How do you update many items in an array at once?](#185-how-do-you-update-many-items-in-an-array-at-once)
- [186: What is the difference between a nested path and a single nested subdocument?](#186-what-is-the-difference-between-a-nested-path-and-a-single-nested-subdocument)
- [187: Do subdocuments have their own middleware?](#187-do-subdocuments-have-their-own-middleware)
- [188: How do you hide sensitive fields from JSON output?](#188-how-do-you-hide-sensitive-fields-from-json-output)
- [189: How do you hash passwords and check them with Mongoose?](#189-how-do-you-hash-passwords-and-check-them-with-mongoose)
- [190: How do you run an aggregation with Mongoose?](#190-how-do-you-run-an-aggregation-with-mongoose)
- [191: Does Mongoose cast values in aggregation pipelines?](#191-does-mongoose-cast-values-in-aggregation-pipelines)
- [192: How do you do a join in an aggregation?](#192-how-do-you-do-a-join-in-an-aggregation)
- [193: What helper methods does the Aggregate object have?](#193-what-helper-methods-does-the-aggregate-object-have)
- [194: How do you stream a large result set?](#194-how-do-you-stream-a-large-result-set)
- [195: What does eachAsync() do?](#195-what-does-eachasync-do)
- [196: What is bulkWrite()?](#196-what-is-bulkwrite)
- [197: What does bulkSave() do?](#197-what-does-bulksave-do)
- [198: What does includeResultMetadata do?](#198-what-does-includeresultmetadata-do)
- [199: What does updateOne() return?](#199-what-does-updateone-return)
- [200: What is an update pipeline and why does Mongoose 9 block it?](#200-what-is-an-update-pipeline-and-why-does-mongoose-9-block-it)
- [201: How do timestamps work with update queries?](#201-how-do-timestamps-work-with-update-queries)
- [202: How do you use a custom function for the current time in timestamps?](#202-how-do-you-use-a-custom-function-for-the-current-time-in-timestamps)
- [203: What is query selector injection and how does Mongoose help?](#203-what-is-query-selector-injection-and-how-does-mongoose-help)
- [204: How does trusted() work with sanitizeFilter?](#204-how-does-trusted-work-with-sanitizefilter)
- [205: What does translateAliases do?](#205-what-does-translatealiases-do)
- [206: How do you use virtuals with lean()?](#206-how-do-you-use-virtuals-with-lean)
- [207: What is the "Query was already executed" error?](#207-what-is-the-query-was-already-executed-error)
- [208: How do you check which index a query uses?](#208-how-do-you-check-which-index-a-query-uses)
- [209: How do you force a query to use a specific index?](#209-how-do-you-force-a-query-to-use-a-specific-index)
- [210: What is collation and how do you use it?](#210-what-is-collation-and-how-do-you-use-it)
- [211: How do you add text search?](#211-how-do-you-add-text-search)
- [212: How do you store and query locations?](#212-how-do-you-store-and-query-locations)
- [213: What do syncIndexes() and diffIndexes() do?](#213-what-do-syncindexes-and-diffindexes-do)
- [214: What is the difference between createIndexes() and syncIndexes()?](#214-what-is-the-difference-between-createindexes-and-syncindexes)
- [215: What does Model.init() do?](#215-what-does-modelinit-do)
- [216: How do you create a capped collection?](#216-how-do-you-create-a-capped-collection)
- [217: How do you make documents expire automatically?](#217-how-do-you-make-documents-expire-automatically)
- [218: What schema helper methods are useful for reuse?](#218-what-schema-helper-methods-are-useful-for-reuse)
- [219: What does schema.loadClass() do?](#219-what-does-schemaloadclass-do)
- [220: How do you write a soft delete plugin?](#220-how-do-you-write-a-soft-delete-plugin)
- [221: What are query helpers?](#221-what-are-query-helpers)
- [222: How do you type a model in TypeScript?](#222-how-do-you-type-a-model-in-typescript)
- [223: What is HydratedDocument?](#223-what-is-hydrateddocument)
- [224: How do you add methods and statics in TypeScript?](#224-how-do-you-add-methods-and-statics-in-typescript)
- [225: What TypeScript changes came in Mongoose 9?](#225-what-typescript-changes-came-in-mongoose-9)
- [226: How do you test Mongoose code without a real database server?](#226-how-do-you-test-mongoose-code-without-a-real-database-server)
- [227: Should you mock Mongoose models in unit tests?](#227-should-you-mock-mongoose-models-in-unit-tests)
- [228: How do you run a transaction with Mongoose?](#228-how-do-you-run-a-transaction-with-mongoose)
- [229: How do you pass a session to different operations?](#229-how-do-you-pass-a-session-to-different-operations)
- [230: What is transactionAsyncLocalStorage?](#230-what-is-transactionasynclocalstorage)
- [231: What is the difference between connection.transaction() and session.withTransaction()?](#231-what-is-the-difference-between-connectiontransaction-and-sessionwithtransaction)
- [232: How do you read from secondaries?](#232-how-do-you-read-from-secondaries)
- [233: How do you set the write concern?](#233-how-do-you-set-the-write-concern)
- [234: How do you watch for changes in a collection?](#234-how-do-you-watch-for-changes-in-a-collection)
- [235: What is optimistic concurrency in Mongoose?](#235-what-is-optimistic-concurrency-in-mongoose)
- [236: When does Mongoose increment __v without optimisticConcurrency?](#236-when-does-mongoose-increment-__v-without-optimisticconcurrency)
- [237: How do you do cursor-based pagination?](#237-how-do-you-do-cursor-based-pagination)
- [238: How do you sort and paginate on a non-unique field?](#238-how-do-you-sort-and-paginate-on-a-non-unique-field)
- [239: What does strict: 'throw' do and when is it useful?](#239-what-does-strict-throw-do-and-when-is-it-useful)
- [240: What does Model.castObject() do?](#240-what-does-modelcastobject-do)
- [241: What does Model.hydrate() do?](#241-what-does-modelhydrate-do)
- [242: How do you set global options in Mongoose?](#242-how-do-you-set-global-options-in-mongoose)
- [243: How do you use Mongoose in NestJS?](#243-how-do-you-use-mongoose-in-nestjs)
- [244: How do you use Mongoose in Next.js or serverless functions?](#244-how-do-you-use-mongoose-in-nextjs-or-serverless-functions)
- [245: What does recompileSchema() do?](#245-what-does-recompileschema-do)
- [246: What does Model.applyTimestamps() do?](#246-what-does-modelapplytimestamps-do)
- [247: What is doc.$locals for?](#247-what-is-doclocals-for)
- [248: How can a pre save hook tell which fields changed?](#248-how-can-a-pre-save-hook-tell-which-fields-changed)
- [249: How do you make orFail() throw your own error?](#249-how-do-you-make-orfail-throw-your-own-error)
- [250: What is the difference between exists() and findOne() for checks?](#250-what-is-the-difference-between-exists-and-findone-for-checks)
- [251: How do you migrate pre hooks from Mongoose 8 to 9?](#251-how-do-you-migrate-pre-hooks-from-mongoose-8-to-9)
- [252: What else breaks when you upgrade from Mongoose 8 to 9?](#252-what-else-breaks-when-you-upgrade-from-mongoose-8-to-9)
- [253: What was removed in Mongoose 7 and 8 that old tutorials still use?](#253-what-was-removed-in-mongoose-7-and-8-that-old-tutorials-still-use)
- [254: How do you return Decimal128 values as numbers or strings in JSON?](#254-how-do-you-return-decimal128-values-as-numbers-or-strings-in-json)
- [255: How do you query a date range for a single day?](#255-how-do-you-query-a-date-range-for-a-single-day)
- [256: How do you search safely with user input in a regex?](#256-how-do-you-search-safely-with-user-input-in-a-regex)
- [257: How do you make a case-insensitive unique field?](#257-how-do-you-make-a-case-insensitive-unique-field)
- [258: How do you find slow queries in a Mongoose app?](#258-how-do-you-find-slow-queries-in-a-mongoose-app)
- [259: Why can duplicates get in even with unique: true?](#259-why-can-duplicates-get-in-even-with-unique-true)
- [260: What does Model.listIndexes() return?](#260-what-does-modellistindexes-return)
- [261: How do you add a TTL to a document that expires at a specific time?](#261-how-do-you-add-a-ttl-to-a-document-that-expires-at-a-specific-time)
- [262: How do you exclude deleted or private fields from populate()?](#262-how-do-you-exclude-deleted-or-private-fields-from-populate)
- [263: How do you sort by a field of a populated document?](#263-how-do-you-sort-by-a-field-of-a-populated-document)
- [264: How do you filter parents by a field of a referenced document?](#264-how-do-you-filter-parents-by-a-field-of-a-referenced-document)
- [265: How do you count related documents for many parents at once?](#265-how-do-you-count-related-documents-for-many-parents-at-once)
- [266: How do you keep an array of ids in sync on both sides?](#266-how-do-you-keep-an-array-of-ids-in-sync-on-both-sides)
- [267: How do you rename a field in existing documents?](#267-how-do-you-rename-a-field-in-existing-documents)
- [268: How do you write a data migration with Mongoose?](#268-how-do-you-write-a-data-migration-with-mongoose)
- [269: What is the difference between deleteOne() on a query and on a document?](#269-what-is-the-difference-between-deleteone-on-a-query-and-on-a-document)
- [270: How do you cascade deletes?](#270-how-do-you-cascade-deletes)
- [271: How do you make default values depend on other fields?](#271-how-do-you-make-default-values-depend-on-other-fields)
- [272: What is the timestamps option for subdocuments?](#272-what-is-the-timestamps-option-for-subdocuments)
- [273: How do you limit the size of an array with $push?](#273-how-do-you-limit-the-size-of-an-array-with-push)
- [274: How do you get only matching array elements back?](#274-how-do-you-get-only-matching-array-elements-back)
- [275: How do you return a single field from many documents?](#275-how-do-you-return-a-single-field-from-many-documents)
- [276: How do you run raw MongoDB commands through Mongoose?](#276-how-do-you-run-raw-mongodb-commands-through-mongoose)
- [277: How do you make sure the app does not start before the database is ready?](#277-how-do-you-make-sure-the-app-does-not-start-before-the-database-is-ready)
- [278: What does bufferCommands: false do and when do you want it?](#278-what-does-buffercommands-false-do-and-when-do-you-want-it)
- [279: How do you use Mongoose with Zod or another validation library?](#279-how-do-you-use-mongoose-with-zod-or-another-validation-library)
- [280: How do you get the schema as JSON Schema?](#280-how-do-you-get-the-schema-as-json-schema)
- [281: How do you add MongoDB-level schema validation with Mongoose?](#281-how-do-you-add-mongodb-level-schema-validation-with-mongoose)
- [282: What is the difference between Model.find() with lean() and Model.collection.find()?](#282-what-is-the-difference-between-modelfind-with-lean-and-modelcollectionfind)
- [283: How do you protect against an empty filter in deleteMany() or updateMany()?](#283-how-do-you-protect-against-an-empty-filter-in-deletemany-or-updatemany)
- [284: How do you use findOneAndUpdate() to create or increment a counter?](#284-how-do-you-use-findoneandupdate-to-create-or-increment-a-counter)
- [285: How do you add a field to all existing documents with a default?](#285-how-do-you-add-a-field-to-all-existing-documents-with-a-default)
- [286: How does Mongoose cast the _id in populate()?](#286-how-does-mongoose-cast-the-_id-in-populate)
- [287: How do you use the same schema in several models?](#287-how-do-you-use-the-same-schema-in-several-models)
- [288: How do you set options on a query?](#288-how-do-you-set-options-on-a-query)
- [289: How do you set a query timeout?](#289-how-do-you-set-a-query-timeout)
- [290: How do you get the filter, update and options from a query object?](#290-how-do-you-get-the-filter-update-and-options-from-a-query-object)
- [291: How do you use Map fields in queries?](#291-how-do-you-use-map-fields-in-queries)
- [292: What is the init hook?](#292-what-is-the-init-hook)
- [293: How do you skip middleware for one operation?](#293-how-do-you-skip-middleware-for-one-operation)
- [294: How do you use a Mongoose document with session after loading it?](#294-how-do-you-use-a-mongoose-document-with-session-after-loading-it)
- [295: What is the difference between Model.validate() and doc.validate()?](#295-what-is-the-difference-between-modelvalidate-and-docvalidate)
- [296: What does the schema option id: false change?](#296-what-does-the-schema-option-id-false-change)
- [297: How do you return the document's id as "id" instead of "_id" in API responses?](#297-how-do-you-return-the-documents-id-as-id-instead-of-_id-in-api-responses)
- [298: How do you handle an upsert race that causes a duplicate key error?](#298-how-do-you-handle-an-upsert-race-that-causes-a-duplicate-key-error)
- [299: How do you log every write to an audit collection?](#299-how-do-you-log-every-write-to-an-audit-collection)
- [300: How do you choose between Mongoose and Prisma for MongoDB?](#300-how-do-you-choose-between-mongoose-and-prisma-for-mongodb)

### Advanced Questions (301-450)

- [301: How does Mongoose track changes on a document?](#301-how-does-mongoose-track-changes-on-a-document)
- [302: What update does save() actually send for a changed document?](#302-what-update-does-save-actually-send-for-a-changed-document)
- [303: What are atomic array operations in Mongoose?](#303-what-are-atomic-array-operations-in-mongoose)
- [304: Why can setting an array item by index cause a VersionError?](#304-why-can-setting-an-array-item-by-index-cause-a-versionerror)
- [305: How does the Mongoose middleware system work internally?](#305-how-does-the-mongoose-middleware-system-work-internally)
- [306: How are Mongoose queries built and executed?](#306-how-are-mongoose-queries-built-and-executed)
- [307: How expensive is building Mongoose documents compared to lean?](#307-how-expensive-is-building-mongoose-documents-compared-to-lean)
- [308: What do you lose with lean() and how do you get some of it back?](#308-what-do-you-lose-with-lean-and-how-do-you-get-some-of-it-back)
- [309: How does populate() work internally and what is its cost?](#309-how-does-populate-work-internally-and-what-is-its-cost)
- [310: When should you use $lookup instead of populate()?](#310-when-should-you-use-lookup-instead-of-populate)
- [311: What is the N+1 problem in Mongoose and how do you avoid it?](#311-what-is-the-n1-problem-in-mongoose-and-how-do-you-avoid-it)
- [312: Why do large embedded arrays hurt performance?](#312-why-do-large-embedded-arrays-hurt-performance)
- [313: What is the bucket pattern and how would you model it in Mongoose?](#313-what-is-the-bucket-pattern-and-how-would-you-model-it-in-mongoose)
- [314: How do you use time series collections in Mongoose?](#314-how-do-you-use-time-series-collections-in-mongoose)
- [315: What is the subset pattern?](#315-what-is-the-subset-pattern)
- [316: How do you keep denormalized data in sync?](#316-how-do-you-keep-denormalized-data-in-sync)
- [317: How would you design a multi-tenant app with Mongoose?](#317-how-would-you-design-a-multi-tenant-app-with-mongoose)
- [318: How do you enforce a tenant filter on every query?](#318-how-do-you-enforce-a-tenant-filter-on-every-query)
- [319: What are the risks of useDb() with many tenants?](#319-what-are-the-risks-of-usedb-with-many-tenants)
- [320: How do you size the connection pool?](#320-how-do-you-size-the-connection-pool)
- [321: What problems does Mongoose have in serverless environments?](#321-what-problems-does-mongoose-have-in-serverless-environments)
- [322: How does Mongoose behave when the primary goes down?](#322-how-does-mongoose-behave-when-the-primary-goes-down)
- [323: What are retryable writes and when do they not help?](#323-what-are-retryable-writes-and-when-do-they-not-help)
- [324: How do transactions affect performance?](#324-how-do-transactions-affect-performance)
- [325: What is a TransientTransactionError and how do you handle it?](#325-what-is-a-transienttransactionerror-and-how-do-you-handle-it)
- [326: Why should code inside a transaction be safe to run more than once?](#326-why-should-code-inside-a-transaction-be-safe-to-run-more-than-once)
- [327: What happens if you forget the session on one operation in a transaction?](#327-what-happens-if-you-forget-the-session-on-one-operation-in-a-transaction)
- [328: Why does populate() in a transaction sometimes fail, and what is the ordered option?](#328-why-does-populate-in-a-transaction-sometimes-fail-and-what-is-the-ordered-option)
- [329: How do read and write concerns combine for consistent reads?](#329-how-do-read-and-write-concerns-combine-for-consistent-reads)
- [330: What is snapshot read concern and when would you use it?](#330-what-is-snapshot-read-concern-and-when-would-you-use-it)
- [331: How do you design indexes for Mongoose queries?](#331-how-do-you-design-indexes-for-mongoose-queries)
- [332: What is a covered query and how does lean() help?](#332-what-is-a-covered-query-and-how-does-lean-help)
- [333: How do you build indexes in production without downtime?](#333-how-do-you-build-indexes-in-production-without-downtime)
- [334: Why is syncIndexes() dangerous in production?](#334-why-is-syncindexes-dangerous-in-production)
- [335: How do you change an index that already exists?](#335-how-do-you-change-an-index-that-already-exists)
- [336: How do you detect duplicate or unused indexes?](#336-how-do-you-detect-duplicate-or-unused-indexes)
- [337: What are partial indexes and how do you use them with Mongoose?](#337-what-are-partial-indexes-and-how-do-you-use-them-with-mongoose)
- [338: How do you deal with soft delete and unique indexes?](#338-how-do-you-deal-with-soft-delete-and-unique-indexes)
- [339: What security problems can happen with Mongoose apps?](#339-what-security-problems-can-happen-with-mongoose-apps)
- [340: How do you prevent mass assignment with Mongoose?](#340-how-do-you-prevent-mass-assignment-with-mongoose)
- [341: How do you encrypt fields with Mongoose?](#341-how-do-you-encrypt-fields-with-mongoose)
- [342: How do you avoid leaking data in error messages and logs?](#342-how-do-you-avoid-leaking-data-in-error-messages-and-logs)
- [343: How do you implement field-level access control?](#343-how-do-you-implement-field-level-access-control)
- [344: Why is it dangerous to use strictQuery: false with user-controlled keys?](#344-why-is-it-dangerous-to-use-strictquery-false-with-user-controlled-keys)
- [345: How do custom schema types work?](#345-how-do-custom-schema-types-work)
- [346: How do you change the casting rules for built-in types?](#346-how-do-you-change-the-casting-rules-for-built-in-types)
- [347: How do you set global getters or setters for a type?](#347-how-do-you-set-global-getters-or-setters-for-a-type)
- [348: How do discriminators affect indexes and queries?](#348-how-do-discriminators-affect-indexes-and-queries)
- [349: Discriminators or separate collections: how do you choose?](#349-discriminators-or-separate-collections-how-do-you-choose)
- [350: How do you change the type of an existing document in a discriminator setup?](#350-how-do-you-change-the-type-of-an-existing-document-in-a-discriminator-setup)
- [351: How does Mongoose handle schemas that change over time?](#351-how-does-mongoose-handle-schemas-that-change-over-time)
- [352: How do you implement lazy schema migration on read?](#352-how-do-you-implement-lazy-schema-migration-on-read)
- [353: What is the strictRead option in Mongoose 9?](#353-what-is-the-strictread-option-in-mongoose-9)
- [354: How do you handle the 16 MB document limit?](#354-how-do-you-handle-the-16-mb-document-limit)
- [355: How do you use GridFS with Mongoose?](#355-how-do-you-use-gridfs-with-mongoose)
- [356: How do you handle very large exports without running out of memory?](#356-how-do-you-handle-very-large-exports-without-running-out-of-memory)
- [357: What can go wrong with long-running cursors?](#357-what-can-go-wrong-with-long-running-cursors)
- [358: How do you process millions of documents in a background job?](#358-how-do-you-process-millions-of-documents-in-a-background-job)
- [359: How does bulkWrite() handle errors with ordered: false?](#359-how-does-bulkwrite-handle-errors-with-ordered-false)
- [360: What does throwOnValidationError do in insertMany() and bulkWrite()?](#360-what-does-throwonvalidationerror-do-in-insertmany-and-bulkwrite)
- [361: How do you make insertMany() faster for big imports?](#361-how-do-you-make-insertmany-faster-for-big-imports)
- [362: How does Mongoose handle query casting for nested operators like $elemMatch?](#362-how-does-mongoose-handle-query-casting-for-nested-operators-like-elemmatch)
- [363: Why might a query on a Mixed field not match?](#363-why-might-a-query-on-a-mixed-field-not-match)
- [364: How do you debug "my update did nothing"?](#364-how-do-you-debug-my-update-did-nothing)
- [365: How do you trace Mongoose queries in observability tools?](#365-how-do-you-trace-mongoose-queries-in-observability-tools)
- [366: What is the cost of having many Mongoose hooks?](#366-what-is-the-cost-of-having-many-mongoose-hooks)
- [367: How does Mongoose cast the update in findOneAndUpdate()?](#367-how-does-mongoose-cast-the-update-in-findoneandupdate)
- [368: How are defaults applied on upserts?](#368-how-are-defaults-applied-on-upserts)
- [369: What happens to _id in subdocument arrays when you replace the array?](#369-what-happens-to-_id-in-subdocument-arrays-when-you-replace-the-array)
- [370: How do you avoid lost updates when two users edit the same document?](#370-how-do-you-avoid-lost-updates-when-two-users-edit-the-same-document)
- [371: How do you implement a simple distributed lock with Mongoose?](#371-how-do-you-implement-a-simple-distributed-lock-with-mongoose)
- [372: How do you implement a job queue on MongoDB with Mongoose?](#372-how-do-you-implement-a-job-queue-on-mongodb-with-mongoose)
- [373: How do you implement idempotent API writes?](#373-how-do-you-implement-idempotent-api-writes)
- [374: How do you handle time zones and dates correctly with Mongoose?](#374-how-do-you-handle-time-zones-and-dates-correctly-with-mongoose)
- [375: How do you store money safely?](#375-how-do-you-store-money-safely)
- [376: How do you get the raw document type from a schema in TypeScript?](#376-how-do-you-get-the-raw-document-type-from-a-schema-in-typescript)
- [377: What does Schema.create() add for TypeScript?](#377-what-does-schemacreate-add-for-typescript)
- [378: How do you type the result of lean() queries?](#378-how-do-you-type-the-result-of-lean-queries)
- [379: How do you type populated paths in TypeScript?](#379-how-do-you-type-populated-paths-in-typescript)
- [380: How do you type virtuals and query helpers?](#380-how-do-you-type-virtuals-and-query-helpers)
- [381: How do you write a typed plugin?](#381-how-do-you-write-a-typed-plugin)
- [382: How do you test code that uses transactions?](#382-how-do-you-test-code-that-uses-transactions)
- [383: How do you test that unique indexes work?](#383-how-do-you-test-that-unique-indexes-work)
- [384: How do you run tests in parallel without them clashing on data?](#384-how-do-you-run-tests-in-parallel-without-them-clashing-on-data)
- [385: What happens when you use Node.js cluster or PM2 with Mongoose?](#385-what-happens-when-you-use-nodejs-cluster-or-pm2-with-mongoose)
- [386: How do you shut down cleanly with requests still running?](#386-how-do-you-shut-down-cleanly-with-requests-still-running)
- [387: How do you cache Mongoose results in Redis?](#387-how-do-you-cache-mongoose-results-in-redis)
- [388: How do you use Mongoose with GraphQL without N+1 queries?](#388-how-do-you-use-mongoose-with-graphql-without-n1-queries)
- [389: What is the outbox pattern and how do you build it with Mongoose?](#389-what-is-the-outbox-pattern-and-how-do-you-build-it-with-mongoose)
- [390: How do you resume a change stream after a restart?](#390-how-do-you-resume-a-change-stream-after-a-restart)
- [391: How do you shard a collection used by Mongoose?](#391-how-do-you-shard-a-collection-used-by-mongoose)
- [392: How do you choose a good shard key?](#392-how-do-you-choose-a-good-shard-key)
- [393: How do you use Atlas Search with Mongoose?](#393-how-do-you-use-atlas-search-with-mongoose)
- [394: How do you do vector search with Mongoose?](#394-how-do-you-do-vector-search-with-mongoose)
- [395: When would you drop down from Mongoose to the native driver?](#395-when-would-you-drop-down-from-mongoose-to-the-native-driver)
- [396: When would you not use Mongoose at all?](#396-when-would-you-not-use-mongoose-at-all)
- [397: What causes memory leaks in Mongoose apps?](#397-what-causes-memory-leaks-in-mongoose-apps)
- [398: What are pathsToSave and validateModifiedOnly?](#398-what-are-pathstosave-and-validatemodifiedonly)
- [399: What is the allowNull option added in Mongoose 9?](#399-what-is-the-allownull-option-added-in-mongoose-9)
- [400: How do you take a snapshot of modified paths and restore it?](#400-how-do-you-take-a-snapshot-of-modified-paths-and-restore-it)
- [401: How do you see the changes a document would send?](#401-how-do-you-see-the-changes-a-document-would-send)
- [402: How do you get from a subdocument to its parent?](#402-how-do-you-get-from-a-subdocument-to-its-parent)
- [403: What does forceRepopulate do?](#403-what-does-forcerepopulate-do)
- [404: How do you transform populated documents?](#404-how-do-you-transform-populated-documents)
- [405: What does Query.prototype.transform() do?](#405-what-does-queryprototypetransform-do)
- [406: How does schemaLevelProjections work?](#406-how-does-schemalevelprojections-work)
- [407: How do you move a model to a different connection at runtime?](#407-how-do-you-move-a-model-to-a-different-connection-at-runtime)
- [408: How do you design a shopping cart with Mongoose?](#408-how-do-you-design-a-shopping-cart-with-mongoose)
- [409: How would you model chat messages?](#409-how-would-you-model-chat-messages)
- [410: How would you model threaded comments?](#410-how-would-you-model-threaded-comments)
- [411: How would you build a leaderboard?](#411-how-would-you-build-a-leaderboard)
- [412: An endpoint that lists orders became slow. How do you investigate?](#412-an-endpoint-that-lists-orders-became-slow-how-do-you-investigate)
- [413: Memory spikes when a report runs. What do you check?](#413-memory-spikes-when-a-report-runs-what-do-you-check)
- [414: Users are getting duplicate orders. How do you fix it?](#414-users-are-getting-duplicate-orders-how-do-you-fix-it)
- [415: How do you migrate string ids to ObjectIds in a reference field?](#415-how-do-you-migrate-string-ids-to-objectids-in-a-reference-field)
- [416: How do you split one large collection into two?](#416-how-do-you-split-one-large-collection-into-two)
- [417: How do you handle GDPR "delete my data" with Mongoose?](#417-how-do-you-handle-gdpr-delete-my-data-with-mongoose)
- [418: Can you add custom options to schema paths?](#418-can-you-add-custom-options-to-schema-paths)
- [419: How do you archive old data?](#419-how-do-you-archive-old-data)
- [420: How do you scale reads in a Mongoose app?](#420-how-do-you-scale-reads-in-a-mongoose-app)
- [421: How do you scale writes in a Mongoose app?](#421-how-do-you-scale-writes-in-a-mongoose-app)
- [422: What is the problem with a single hot counter document?](#422-what-is-the-problem-with-a-single-hot-counter-document)
- [423: How do you add schema-level read concern or write concern?](#423-how-do-you-add-schema-level-read-concern-or-write-concern)
- [424: How does Mongoose handle a schema path named like a built-in method?](#424-how-does-mongoose-handle-a-schema-path-named-like-a-built-in-method)
- [425: How do getters and toJSON interact in API responses?](#425-how-do-getters-and-tojson-interact-in-api-responses)
- [426: How do you return ObjectIds as strings in JSON consistently?](#426-how-do-you-return-objectids-as-strings-in-json-consistently)
- [427: How do you write a plugin that adds createdBy and updatedBy?](#427-how-do-you-write-a-plugin-that-adds-createdby-and-updatedby)
- [428: What does Connection.prototype.bulkWrite() do?](#428-what-does-connectionprototypebulkwrite-do)
- [429: How do you run several queries in parallel safely?](#429-how-do-you-run-several-queries-in-parallel-safely)
- [430: How do you deal with clock skew for timestamps across servers?](#430-how-do-you-deal-with-clock-skew-for-timestamps-across-servers)
- [431: How do you query documents created in a time range using only _id?](#431-how-do-you-query-documents-created-in-a-time-range-using-only-_id)
- [432: What happens if two models use the same collection?](#432-what-happens-if-two-models-use-the-same-collection)
- [433: How does Mongoose handle deeply nested updates on subdocument arrays inside arrays?](#433-how-does-mongoose-handle-deeply-nested-updates-on-subdocument-arrays-inside-arrays)
- [434: How do you make a field unique inside an embedded array?](#434-how-do-you-make-a-field-unique-inside-an-embedded-array)
- [435: How do you make expensive virtuals cheap?](#435-how-do-you-make-expensive-virtuals-cheap)
- [436: What should a good Mongoose error handler in Express look like?](#436-what-should-a-good-mongoose-error-handler-in-express-look-like)
- [437: How do you keep a repository layer clean on top of Mongoose?](#437-how-do-you-keep-a-repository-layer-clean-on-top-of-mongoose)
- [438: How do you review a Mongoose schema in a code review?](#438-how-do-you-review-a-mongoose-schema-in-a-code-review)
- [439: What happens if you call mongoose.model() before mongoose.connect()?](#439-what-happens-if-you-call-mongoosemodel-before-mongooseconnect)
- [440: How do you connect to MongoDB with TLS and X.509 or AWS IAM?](#440-how-do-you-connect-to-mongodb-with-tls-and-x509-or-aws-iam)
- [441: How do you rotate database passwords without downtime?](#441-how-do-you-rotate-database-passwords-without-downtime)
- [442: What does a Mongoose app need from MongoDB for change streams and transactions?](#442-what-does-a-mongoose-app-need-from-mongodb-for-change-streams-and-transactions)
- [443: How do you handle "MongooseServerSelectionError: connect ECONNREFUSED ::1:27017"?](#443-how-do-you-handle-mongooseserverselectionerror-connect-econnrefused-127017)
- [444: How do you avoid conflicts between autoIndex and a deploy that changes indexes?](#444-how-do-you-avoid-conflicts-between-autoindex-and-a-deploy-that-changes-indexes)
- [445: How do you work with a database that other services also write to?](#445-how-do-you-work-with-a-database-that-other-services-also-write-to)
- [446: How do you set up read-only access for a reporting service?](#446-how-do-you-set-up-read-only-access-for-a-reporting-service)
- [447: What is autoCreate and why does it matter?](#447-what-is-autocreate-and-why-does-it-matter)
- [448: How would you explain the difference between Mongoose validation and MongoDB schema validation in an interview?](#448-how-would-you-explain-the-difference-between-mongoose-validation-and-mongodb-schema-validation-in-an-interview)
- [449: What are the trade-offs of putting logic in Mongoose middleware?](#449-what-are-the-trade-offs-of-putting-logic-in-mongoose-middleware)
- [450: You join a team with an old Mongoose 5 app. How do you upgrade it to Mongoose 9?](#450-you-join-a-team-with-an-old-mongoose-5-app-how-do-you-upgrade-it-to-mongoose-9)

---

## Easy Questions (1-150)

### 1: What is Mongoose?

Mongoose is an npm package for working with MongoDB from Node.js. It sits on top of the official MongoDB Node.js driver and adds schemas, models, validation, type casting, middleware (hooks), population of references and a query builder.

With the plain driver you work with raw objects. With Mongoose you describe the shape of your data once in a schema, and Mongoose checks and converts data for you every time you read or write.

### 2: What is an ODM?

ODM stands for Object Document Mapper. It maps documents stored in a document database (like MongoDB) to objects in your code. Mongoose is an ODM. It is the document database version of an ORM (Object Relational Mapper), which does the same thing for SQL databases.

### 3: What is the difference between Mongoose and the native MongoDB driver?

The native driver (`mongodb` package) gives you direct access to MongoDB with no schema, no validation and no casting. Mongoose uses the driver internally and adds:

- schemas and models
- validation before saving
- casting (for example the string `"42"` becomes the number `42`)
- middleware (pre and post hooks)
- `populate()` for references
- virtuals, getters and setters

The driver is a bit faster and more flexible. Mongoose gives you more structure and less boilerplate. Many apps use Mongoose for normal work and drop down to the driver for special cases.

### 4: How do you install Mongoose?

```bash
npm install mongoose
```

Mongoose ships its own TypeScript types, so you do not need `@types/mongoose`. Mongoose 9 needs Node.js 20.19.0 or newer.

### 5: How do you connect to MongoDB with Mongoose?

Call `mongoose.connect()` with a connection string. It returns a promise.

```javascript
import mongoose from "mongoose";

await mongoose.connect("mongodb://127.0.0.1:27017/shop");
console.log("Connected");
```

Use `127.0.0.1` instead of `localhost` for local servers. On some systems `localhost` resolves to the IPv6 address `::1`, and MongoDB is often only listening on IPv4.

### 6: What does a MongoDB connection string look like?

A standard one looks like this:

```
mongodb://user:password@host:27017/databaseName?authSource=admin
```

For MongoDB Atlas you usually get an SRV string:

```
mongodb+srv://user:password@cluster0.abcde.mongodb.net/databaseName?retryWrites=true&w=majority
```

The part after the host is the database name. If you leave it out, Mongoose uses the `test` database. Special characters in the password must be URL encoded.

### 7: What is the default connection in Mongoose?

When you call `mongoose.connect()`, Mongoose opens one default connection and stores it on `mongoose.connection`. Every model created with `mongoose.model()` uses this default connection. Most apps only need this one connection.

```javascript
await mongoose.connect(process.env.MONGO_URI);
console.log(mongoose.connection.name); // database name
```

### 8: How do you listen to connection events?

`mongoose.connection` is an event emitter. Common events are `connected`, `open`, `disconnected`, `reconnected`, `error` and `close`.

```javascript
mongoose.connection.on("connected", () => console.log("MongoDB connected"));
mongoose.connection.on("disconnected", () =>
  console.log("MongoDB disconnected"),
);
mongoose.connection.on("error", (err) => console.error("MongoDB error", err));

await mongoose.connect(process.env.MONGO_URI);
```

Register the listeners before calling `connect()` if you want to catch the first `connected` event.

### 9: How do you close a Mongoose connection?

```javascript
await mongoose.disconnect(); // closes all connections
// or
await mongoose.connection.close(); // closes only the default connection
```

You usually do this in tests and when the app shuts down.

### 10: What is a schema in Mongoose?

A schema describes the shape of the documents in a collection: which fields exist, their types, default values and validation rules. It can also hold methods, virtuals, indexes and middleware.

```javascript
import { Schema } from "mongoose";

const userSchema = new Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, lowercase: true },
  age: Number,
  createdAt: { type: Date, default: Date.now },
});
```

MongoDB itself does not need a schema. The schema lives only in your Node.js code.

### 11: What is a model?

A model is a class built from a schema. You use it to create, read, update and delete documents in one collection.

```javascript
import mongoose from "mongoose";

const User = mongoose.model("User", userSchema);

const user = await User.create({ name: "Anna", email: "anna@example.com" });
const users = await User.find({ age: { $gte: 18 } });
```

The first argument is the model name. Mongoose uses it to work out the collection name.

### 12: What is a document in Mongoose?

A document is an instance of a model. It represents one record in the collection. It has the schema fields plus helper methods like `save()`, `validate()`, `toObject()` and `isModified()`.

```javascript
const user = new User({ name: "Anna", email: "anna@example.com" });
user instanceof User; // true
user instanceof mongoose.Document; // true
await user.save();
```

### 13: How does Mongoose pick the collection name for a model?

It takes the model name, makes it lowercase and plural. `User` becomes `users`, `Person` becomes `people`, `Category` becomes `categories`.

You can set the name yourself in three ways:

```javascript
// schema option
const logSchema = new Schema({ message: String }, { collection: "app_logs" });

// third argument of model()
const Log = mongoose.model("Log", logSchema, "app_logs");

// turn off pluralization for all models
mongoose.pluralize(null);
```

### 14: What schema types does Mongoose support?

The built-in types are:

- `String`
- `Number`
- `Date`
- `Boolean`
- `Buffer`
- `ObjectId` (`Schema.Types.ObjectId`)
- `Array`
- `Mixed` (`Schema.Types.Mixed`)
- `Map`
- `Decimal128`
- `BigInt`
- `UUID`
- `Int32`
- `Double`
- `Schema` (a nested subdocument schema)

`Int32` and `Double` were added in Mongoose 8.x. You can also write custom schema types.

### 15: What is the difference between the short and long way to define a field?

The short way only gives the type. The long way uses an object with a `type` key, so you can add options.

```javascript
const schema = new Schema({
  title: String, // short
  price: { type: Number, required: true, min: 0 }, // long
});
```

If you want a field that is itself called `type`, you have to use the long form: `type: { type: String }`.

### 16: What options are available for String fields?

Common ones:

- `lowercase` and `uppercase`: change the case before saving
- `trim`: remove spaces at both ends
- `minLength` and `maxLength`: length validation
- `match`: a regular expression the value must match
- `enum`: list of allowed values

```javascript
const schema = new Schema({
  username: {
    type: String,
    trim: true,
    lowercase: true,
    minLength: 3,
    maxLength: 30,
  },
  role: { type: String, enum: ["user", "admin"], default: "user" },
});
```

### 17: What options are available for Number fields?

- `min` and `max`: range validation
- `enum`: list of allowed numbers

```javascript
const productSchema = new Schema({
  price: { type: Number, min: 0, required: true },
  rating: { type: Number, min: 1, max: 5 },
});
```

Mongoose casts strings like `"12.5"` to numbers. A value like `"abc"` causes a `CastError`.

### 18: How do Date fields work?

A `Date` field stores a JavaScript `Date`. Mongoose casts strings and numbers (milliseconds) to dates. You can use `min` and `max` and also `expires` to create a TTL index.

```javascript
const eventSchema = new Schema({
  startsAt: { type: Date, required: true, min: "2020-01-01" },
  createdAt: { type: Date, default: Date.now },
});

await Event.create({ startsAt: "2026-11-01T10:00:00Z" }); // string cast to Date
```

MongoDB stores dates in UTC.

### 19: How does Mongoose cast Boolean values?

By default these values become `true`: `true`, `'true'`, `1`, `'1'`, `'yes'`. These become `false`: `false`, `'false'`, `0`, `'0'`, `'no'`. Anything else causes a `CastError`.

You can change the lists:

```javascript
mongoose.Schema.Types.Boolean.convertToTrue.add("on");
mongoose.Schema.Types.Boolean.convertToFalse.add("off");
```

### 20: What is the ObjectId type used for?

`ObjectId` is the default type of `_id` and the usual type for references to other documents.

```javascript
const postSchema = new Schema({
  title: String,
  author: { type: Schema.Types.ObjectId, ref: "User" },
});
```

Mongoose casts a 24 character hex string to an `ObjectId` automatically, so you can pass `req.params.id` straight into a query.

### 21: How do you define an array field?

Put the type inside square brackets.

```javascript
const schema = new Schema({
  tags: [String],
  scores: [{ type: Number, min: 0 }],
  comments: [{ text: String, createdAt: Date }],
});
```

Array fields default to an empty array `[]`. You can turn that off with `default: undefined`.

### 22: What is the Mixed type?

`Mixed` means "anything goes". Mongoose does no casting and no validation on it.

```javascript
const schema = new Schema({
  settings: Schema.Types.Mixed,
  other: {}, // an empty object also means Mixed
});
```

The downside: Mongoose cannot see changes inside a Mixed value. If you change a nested property, you must call `doc.markModified('settings')` before `save()`, or the change is not saved.

### 23: What is the Map type?

A `Map` stores keys you do not know ahead of time, while still casting the values to one type.

```javascript
const userSchema = new Schema({
  socialLinks: { type: Map, of: String },
});

const user = new User({ socialLinks: { github: "https://github.com/anna" } });
user.socialLinks.get("github");
user.socialLinks.set("x", "https://x.com/anna");
await user.save();
```

Keys must be strings and cannot contain `.` or start with `$`.

### 24: When would you use the Buffer type?

`Buffer` stores binary data, like small files, hashes or encrypted values. For large files (over a few MB) use GridFS or object storage like S3 instead, because one MongoDB document is limited to 16 MB.

```javascript
const fileSchema = new Schema({ name: String, data: Buffer, mimeType: String });
```

### 25: What is Decimal128 used for?

`Decimal128` stores exact decimal numbers. Normal JavaScript numbers are floating point, so `0.1 + 0.2` is not exactly `0.3`. For money you either use `Decimal128` or store integer cents in a `Number`.

```javascript
const orderSchema = new Schema({
  total: { type: Schema.Types.Decimal128, required: true },
});

const order = await Order.create({ total: "19.99" });
order.total.toString(); // '19.99'
```

When you send a `Decimal128` to JSON, it becomes `{ "$numberDecimal": "19.99" }` unless you add a getter or a transform.

### 26: Does Mongoose support BigInt?

Yes. The `BigInt` type stores JavaScript `bigint` values as 64-bit integers in MongoDB.

```javascript
const statSchema = new Schema({ views: BigInt });
const stat = await Stat.create({ views: 9007199254740993n });
```

Values must fit in a signed 64-bit integer.

### 27: How does the UUID type work?

The `UUID` type stores UUIDs as binary data (subtype 4), which is smaller than storing them as strings. Mongoose casts UUID strings for you.

```javascript
const sessionSchema = new Schema({
  token: { type: "UUID", default: () => crypto.randomUUID() },
});
```

In Mongoose 9, reading the field gives you a `bson.UUID` object. In Mongoose 8 it was converted to a string by a getter. Call `.toString()` if you need a string.

### 28: What are the Int32 and Double types?

They were added in Mongoose 8.x. `Int32` stores a 32-bit integer and `Double` forces the value to be stored as a BSON double. By default a `Number` field may be stored as int or double depending on the value. These types are useful when another system reads the data and expects an exact BSON type.

```javascript
const schema = new Schema({ quantity: "Int32", weight: "Double" });
```

### 29: How do you define nested objects in a schema?

Just nest plain objects.

```javascript
const userSchema = new Schema({
  name: String,
  address: {
    street: String,
    city: String,
    zip: String,
  },
});
```

These are nested paths, not separate subdocuments. They do not get their own `_id`, and `address` is never `undefined` on a document, it is always an object (possibly empty).

### 30: What is a subdocument?

A subdocument is a document inside another document that has its own schema. It gets its own `_id` (by default), validation, middleware and methods.

```javascript
const addressSchema = new Schema({ city: String, zip: String });

const userSchema = new Schema({
  name: String,
  address: addressSchema, // single nested subdocument
  pastAddresses: [addressSchema], // array of subdocuments
});
```

Subdocuments are saved together with the parent. You cannot save them on their own.

### 31: How do you create and save a document?

Create an instance of the model and call `save()`.

```javascript
const user = new User({ name: "Anna", email: "anna@example.com" });
await user.save();
console.log(user._id);
```

`save()` runs validation and middleware, then inserts the document. If the document already exists in the database, `save()` updates only the changed fields.

### 32: What does Model.create() do?

`create()` is a shortcut for `new Model(data).save()`. It accepts one object or an array.

```javascript
const user = await User.create({ name: "Anna", email: "anna@example.com" });
const users = await User.create([{ name: "Ben" }, { name: "Cara" }]);
```

With an array, it calls `save()` for each item, so it runs `save` middleware for each one. For many documents, `insertMany()` is faster.

### 33: What is the difference between create() and insertMany()?

`create()` saves documents one by one and runs `save` middleware for each. `insertMany()` validates all documents and then sends them to MongoDB in one bulk command. It runs `insertMany` middleware, not `save` middleware.

```javascript
await Product.insertMany([
  { name: "Pen", price: 1 },
  { name: "Book", price: 12 },
]);
```

Use `insertMany()` for imports and seeding. Use `create()` when you need `save` hooks, like password hashing.

### 34: What is Model.insertOne()?

`insertOne()` was added in Mongoose 8.x. It inserts a single document, runs validation and returns the saved document. It behaves like `create()` with one object, but it is a clearer name and does not accept an array.

```javascript
const product = await Product.insertOne({ name: "Pen", price: 1 });
```

### 35: How do you find documents?

Use `find()`. It returns an array, which is empty if nothing matches.

```javascript
const all = await User.find();
const admins = await User.find({ role: "admin" });
const adults = await User.find({ age: { $gte: 18 } }, "name email"); // with projection
```

### 36: What is the difference between find() and findOne()?

`find()` returns an array of all matching documents. `findOne()` returns the first match or `null`.

```javascript
const user = await User.findOne({ email: "anna@example.com" });
if (!user) {
  // not found
}
```

Without a sort, "first" means whatever MongoDB returns first, which is not guaranteed to be any specific order.

### 37: How do you find a document by its _id?

Use `findById()`. It is a shortcut for `findOne({ _id: id })`.

```javascript
const user = await User.findById(req.params.id);
```

If `id` is not a valid ObjectId, Mongoose throws a `CastError`. Many apps check the id with `mongoose.isValidObjectId(id)` first, or catch the error and return 400 or 404.

### 38: How do you use query operators in Mongoose?

You use the same operators as in MongoDB: `$eq`, `$ne`, `$gt`, `$gte`, `$lt`, `$lte`, `$in`, `$nin`, `$and`, `$or`, `$not`, `$exists`, `$regex` and others.

```javascript
const products = await Product.find({
  price: { $gte: 10, $lte: 50 },
  category: { $in: ["books", "toys"] },
  $or: [{ stock: { $gt: 0 } }, { preorder: true }],
});
```

Mongoose casts the values inside operators too. `{ price: { $gte: '10' } }` becomes `{ price: { $gte: 10 } }`.

### 39: How do you select only some fields?

Use `select()` or pass a projection as the second argument.

```javascript
await User.find().select("name email"); // include
await User.find().select("-password -__v"); // exclude
await User.find({}, { name: 1, email: 1 }); // object form
```

You cannot mix including and excluding in one projection, except for `_id`, which you can always exclude.

### 40: How do you sort results?

```javascript
await Product.find().sort({ price: 1 }); // ascending
await Product.find().sort({ price: -1 }); // descending
await Product.find().sort("-createdAt name"); // string form
```

In the string form, a `-` in front of the field means descending.

### 41: How do you limit and skip results?

```javascript
const page = 3;
const pageSize = 20;

const products = await Product.find()
  .sort({ createdAt: -1 })
  .skip((page - 1) * pageSize)
  .limit(pageSize);
```

Always sort when you paginate, otherwise pages can show the same document twice or skip some.

### 42: How do you count documents?

Use `countDocuments()` with a filter, or `estimatedDocumentCount()` for a fast count of the whole collection.

```javascript
const active = await User.countDocuments({ active: true });
const total = await User.estimatedDocumentCount();
```

`estimatedDocumentCount()` reads collection metadata, so it is very fast but takes no filter and can be slightly off after an unclean shutdown. The old `count()` method was removed in Mongoose 8.

### 43: How do you get distinct values of a field?

```javascript
const categories = await Product.distinct("category");
const activeCities = await User.distinct("address.city", { active: true });
```

It returns an array of unique values.

### 44: How do you check if a document exists?

Use `exists()`. It returns `{ _id }` if a match is found, or `null`.

```javascript
const taken = await User.exists({ email: "anna@example.com" });
if (taken) {
  throw new Error("Email already used");
}
```

It is cheaper than `findOne()` because it only returns the `_id`.

### 45: How do you update one document?

Use `updateOne()`. It does not return the document, it returns a result object.

```javascript
const result = await User.updateOne(
  { email: "anna@example.com" },
  { $set: { active: false } },
);
console.log(result.matchedCount, result.modifiedCount);
```

If you pass an object without operators, like `{ active: false }`, Mongoose wraps it in `$set` for you.

### 46: How do you update many documents?

```javascript
await Product.updateMany({ category: "books" }, { $inc: { price: 1 } });
```

The filter `{}` updates every document in the collection, so be careful with it.

### 47: What does findOneAndUpdate() do?

It finds one document, updates it and returns it. By default it returns the document **before** the update. Use `returnDocument: 'after'` to get the updated one.

```javascript
const user = await User.findOneAndUpdate(
  { email: "anna@example.com" },
  { $set: { name: "Anna Smith" } },
  { returnDocument: "after" },
);
```

The older `new: true` option still works but is deprecated since Mongoose 9.2 and prints a warning.

### 48: What is findByIdAndUpdate()?

It is `findOneAndUpdate({ _id: id }, ...)` in short form.

```javascript
const product = await Product.findByIdAndUpdate(
  id,
  { price: 25 },
  { returnDocument: "after", runValidators: true },
);
```

It returns `null` if no document has that id.

### 49: What is the difference between updateOne() and replaceOne()?

`updateOne()` changes only the fields you give it. `replaceOne()` replaces the whole document (except `_id`) with the new object. Any field not in the new object is gone.

```javascript
await User.replaceOne({ _id: id }, { name: "Anna", email: "anna@example.com" });
```

### 50: How do you delete documents?

```javascript
await User.deleteOne({ email: "anna@example.com" });
await User.deleteMany({ active: false });
```

Both return `{ acknowledged, deletedCount }`. The old `remove()` method was removed in Mongoose 7.

### 51: How do you delete a document and get it back?

Use `findOneAndDelete()` or `findByIdAndDelete()`. They return the deleted document, or `null`.

```javascript
const deleted = await Post.findByIdAndDelete(id);
if (!deleted) {
  // nothing was deleted
}
```

`findOneAndRemove()` and `findByIdAndRemove()` were removed in Mongoose 8.

### 52: How do you delete a document you already loaded?

Call `deleteOne()` on the document.

```javascript
const post = await Post.findById(id);
await post.deleteOne();
```

This runs document middleware for `deleteOne` if you registered it with `{ document: true }`.

### 53: What is the _id field?

Every MongoDB document has an `_id`, and it must be unique in the collection. Mongoose adds `_id` of type `ObjectId` to every schema by default and creates it when you create a document, even before saving.

```javascript
const user = new User({ name: "Anna" });
console.log(user._id); // already set
```

You can use another type, like `_id: String` or `_id: Number`, but then you must set it yourself.

### 54: What is the id virtual?

Mongoose adds an `id` virtual to each schema. It returns `_id` as a string.

```javascript
user._id; // ObjectId('66f1...')
user.id; // '66f1...'
```

It is not saved in the database. You can turn it off with the schema option `id: false`. By default `id` is not included in `toJSON()` output unless you set `toJSON: { virtuals: true }`.

### 55: What is the __v field?

`__v` is the version key. Mongoose adds it to each document and uses it to avoid conflicts when two processes change the same array at once. It starts at 0.

You can rename it or remove it:

```javascript
new Schema({ name: String }, { versionKey: "_version" });
new Schema({ name: String }, { versionKey: false });
```

### 56: What does the timestamps option do?

It adds `createdAt` and `updatedAt` fields and manages them for you.

```javascript
const postSchema = new Schema({ title: String }, { timestamps: true });
```

`createdAt` is set on insert. `updatedAt` is set on insert and on every `save()`, `updateOne()`, `findOneAndUpdate()` and similar calls. You can rename them:

```javascript
{ timestamps: { createdAt: 'created_at', updatedAt: 'updated_at' } }
```

### 57: How does the required validator work?

`required: true` means the field must have a value. For strings, an empty string `''` also fails.

```javascript
const schema = new Schema({
  email: { type: String, required: [true, "Email is required"] },
});
```

The second item in the array is a custom error message.

### 58: How do you validate number ranges?

Use `min` and `max`.

```javascript
const schema = new Schema({
  age: { type: Number, min: [0, "Age cannot be negative"], max: 130 },
});
```

### 59: How do you validate string length?

Use `minLength` and `maxLength`.

```javascript
const schema = new Schema({
  password: { type: String, minLength: 8, maxLength: 128 },
});
```

The older lowercase spellings `minlength` and `maxlength` also still work.

### 60: How does the enum validator work?

For strings and numbers, `enum` limits the value to a list.

```javascript
const orderSchema = new Schema({
  status: {
    type: String,
    enum: {
      values: ["pending", "paid", "shipped", "cancelled"],
      message: "{VALUE} is not a valid status",
    },
    default: "pending",
  },
});
```

`{VALUE}` is replaced with the bad value in the error message.

### 61: How do you validate a string with a regular expression?

Use `match`.

```javascript
const schema = new Schema({
  phone: { type: String, match: [/^\+?[0-9]{7,15}$/, "Invalid phone number"] },
});
```

### 62: How do you write a custom validator?

Use the `validate` option with a `validator` function. Return `true` if the value is fine.

```javascript
const schema = new Schema({
  tags: {
    type: [String],
    validate: {
      validator: (value) => value.length <= 5,
      message: "A post can have at most 5 tags",
    },
  },
});
```

The validator can also be `async` and return a promise of a boolean.

### 63: When does Mongoose run validation?

Validation runs automatically before `save()` and `create()`, and in `insertMany()`. It does **not** run by default on update methods like `updateOne()` or `findOneAndUpdate()`. For those you need `runValidators: true`.

```javascript
await User.updateOne({ _id: id }, { age: -5 }, { runValidators: true }); // throws
```

You can also run it by hand with `doc.validate()` or `doc.validateSync()`.

### 64: What error do you get when validation fails?

A `ValidationError`. Its `errors` property has one entry per failed path.

```javascript
try {
  await User.create({ email: "" });
} catch (err) {
  if (err instanceof mongoose.Error.ValidationError) {
    for (const [path, e] of Object.entries(err.errors)) {
      console.log(path, e.message);
    }
  }
}
```

### 65: Is unique a validator?

No. `unique: true` only tells Mongoose to build a unique index in MongoDB. Mongoose does not check it before saving. If you insert a duplicate, MongoDB rejects it with a duplicate key error (code `11000`).

```javascript
const userSchema = new Schema({ email: { type: String, unique: true } });
```

Also, the index has to exist before it works. If the collection already has duplicates, the index build fails.

### 66: How do you set a default value?

Use the `default` option. It can be a value or a function.

```javascript
const schema = new Schema({
  role: { type: String, default: "user" },
  createdAt: { type: Date, default: Date.now },
  code: { type: String, default: () => Math.random().toString(36).slice(2, 8) },
});
```

Pass a function (like `Date.now`), not the result of calling it (`Date.now()`). Otherwise every document gets the same date from when the schema was created.

### 67: When are default values applied?

Defaults are applied when you create a new document and the field is `undefined`. They are not applied if the value is `null`. They are also applied when Mongoose loads a document from the database that is missing the field, so old documents get the default in memory (but not in the database until you save).

For upserts, `setDefaultsOnInsert` is on by default since Mongoose 6, so defaults are added when the upsert creates a new document.

### 68: What do lowercase, uppercase and trim do?

They are setters for strings. They change the value before it is stored.

```javascript
const schema = new Schema({
  email: { type: String, lowercase: true, trim: true },
});

const user = new User({ email: "  Anna@Example.COM " });
user.email; // 'anna@example.com'
```

They also run on query filters for that field, so `User.findOne({ email: 'ANNA@example.com' })` finds the right user.

### 69: What is casting in Mongoose?

Casting means converting a value to the type in the schema. Mongoose does it when you create documents, set values and build queries.

```javascript
const product = new Product({ price: "19" });
typeof product.price; // 'number'

await Product.find({ _id: "66f1c2a8e4b0a1b2c3d4e5f6" }); // string cast to ObjectId
```

If the value cannot be converted, Mongoose throws a `CastError`.

### 70: What is a CastError?

A `CastError` happens when Mongoose cannot convert a value to the schema type. The most common case is an invalid id.

```javascript
try {
  await User.findById("not-an-id");
} catch (err) {
  if (err.name === "CastError") {
    // err.path === '_id', err.value === 'not-an-id'
  }
}
```

In an API you usually turn this into a 400 or 404 response.

### 71: What does strict mode do?

With `strict: true` (the default), fields that are not in the schema are ignored when you create or update a document. They are not saved.

```javascript
const user = new User({ name: "Anna", isAdmin: true }); // isAdmin not in schema
await user.save(); // isAdmin is not stored
```

Set `strict: 'throw'` to get an error instead, or `strict: false` to save everything.

### 72: What is strictQuery?

`strictQuery` controls what happens to filter fields that are not in the schema. Since Mongoose 7 the default is `false`, which means unknown fields are kept in the filter and sent to MongoDB.

```javascript
mongoose.set("strictQuery", true); // drop unknown filter fields
```

Be careful with `true`: a typo like `{ emial: 'x' }` turns into an empty filter `{}`, which matches every document.

### 73: Are Mongoose queries promises?

Not exactly. Methods like `find()` return a `Query` object. A query has a `then()` method, so you can `await` it, but it is not a real promise. The query runs only when you call `then()`, `await` it or call `exec()`.

```javascript
const query = User.find({ active: true }); // nothing sent yet
query.sort({ name: 1 }).limit(10);
const users = await query; // runs now
```

### 74: What is exec() for?

`exec()` runs the query and returns a real promise.

```javascript
const users = await User.find({ active: true }).exec();
```

Using `await` without `exec()` works the same way. Some teams prefer `exec()` because the stack traces are a bit better and it is clear the query is being run.

### 75: Do Mongoose methods still accept callbacks?

No. Mongoose 7 removed callback support from almost all methods. You must use promises or `async`/`await`.

```javascript
// Old, no longer works
User.find({}, (err, users) => {});

// Now
const users = await User.find({});
```

Mongoose 9 went further and removed `next()` from pre middleware too.

### 76: What does lean() do?

`lean()` tells Mongoose to return plain JavaScript objects instead of full Mongoose documents.

```javascript
const users = await User.find({ active: true }).lean();
users[0] instanceof mongoose.Document; // false
```

Lean results are faster and use less memory, because Mongoose skips building documents. The downside: no `save()`, no virtuals, no getters, no change tracking. It is a good fit for read-only endpoints.

### 77: How do you use your own value for _id?

Declare `_id` in the schema with the type you want. Mongoose then does not create an ObjectId for you, so you must set it when creating the document.

```javascript
const countrySchema = new Schema({
  _id: { type: String, uppercase: true }, // ISO code like 'DE'
  name: String,
});

const Country = mongoose.model("Country", countrySchema);
await Country.create({ _id: "de", name: "Germany" }); // stored as 'DE'
```

Saving without an `_id` fails with an error saying the document must have an `_id` before saving.

### 78: How do you add instance methods to a model?

Add them to `schema.methods`, or use the `methods` schema option. Inside, `this` is the document. Use a normal `function`, not an arrow function, so `this` works.

```javascript
userSchema.methods.fullName = function () {
  return `${this.firstName} ${this.lastName}`;
};

const user = await User.findOne();
user.fullName();
```

### 79: How do you add static methods to a model?

Add them to `schema.statics`, or use the `statics` schema option. Inside, `this` is the model.

```javascript
userSchema.statics.findByEmail = function (email) {
  return this.findOne({ email: email.toLowerCase() });
};

const user = await User.findByEmail("Anna@example.com");
```

Statics are for logic that is about the collection, not about one document.

### 80: What is a virtual?

A virtual is a property that is not stored in MongoDB. It is computed from other fields when you read it.

```javascript
userSchema.virtual("fullName").get(function () {
  return `${this.firstName} ${this.lastName}`;
});

user.fullName; // 'Anna Smith'
```

You cannot query or sort by a virtual, because it does not exist in the database.

### 81: Can a virtual have a setter?

Yes. A virtual setter lets you set several real fields from one value.

```javascript
userSchema
  .virtual("fullName")
  .get(function () {
    return `${this.firstName} ${this.lastName}`;
  })
  .set(function (value) {
    const [firstName, ...rest] = value.split(" ");
    this.firstName = firstName;
    this.lastName = rest.join(" ");
  });

const user = new User({ fullName: "Anna Smith" });
user.firstName; // 'Anna'
```

### 82: Why are virtuals missing from my JSON response?

By default, `toJSON()` and `toObject()` do not include virtuals. `res.json(doc)` calls `toJSON()`, so the virtuals are left out. Turn them on in the schema options:

```javascript
const userSchema = new Schema(
  { firstName: String, lastName: String },
  { toJSON: { virtuals: true }, toObject: { virtuals: true } },
);
```

Also note that `lean()` results never have virtuals.

### 83: What is a getter?

A getter changes a value when you read it from a document. The stored value stays the same.

```javascript
const productSchema = new Schema(
  {
    priceCents: { type: Number, get: (v) => (v / 100).toFixed(2) },
  },
  { toJSON: { getters: true } },
);

product.priceCents; // '19.99' if stored value is 1999
```

Getters do not run on `lean()` results and are not used in `toJSON()` unless you set `getters: true`.

### 84: What is a setter?

A setter changes a value when you assign it, before it is stored. Built-in options like `lowercase` and `trim` are setters.

```javascript
const userSchema = new Schema({
  username: {
    type: String,
    set: (v) => v.replace(/\s+/g, "").toLowerCase(),
  },
});

const user = new User({ username: "Anna Smith" });
user.username; // 'annasmith'
```

Setters also run on query filters for that path, unless you turn that off.

### 85: What is middleware in Mongoose?

Middleware (also called hooks) are functions that run before (`pre`) or after (`post`) some operation, like `save`, `validate`, `find` or `deleteOne`. You use them for things like hashing passwords, setting fields, logging, or cleaning up related data.

```javascript
userSchema.pre("save", async function () {
  this.email = this.email.toLowerCase();
});
```

Middleware must be added to the schema **before** you call `mongoose.model()`.

### 86: How do you write a pre save hook?

```javascript
import bcrypt from "bcrypt";

userSchema.pre("save", async function () {
  if (!this.isModified("password")) return;
  this.password = await bcrypt.hash(this.password, 12);
});
```

In Mongoose 9 pre hooks do not get a `next` argument. Use an `async` function or return a promise. To stop the save, throw an error.

### 87: How do you write a post hook?

A post hook runs after the operation finishes. It receives the result.

```javascript
userSchema.post("save", function (doc) {
  console.log("Saved user", doc._id);
});

userSchema.post("find", function (docs) {
  console.log("Found", docs.length, "users");
});
```

Post hooks can be `async` too.

### 88: What kinds of middleware does Mongoose have?

Four kinds, based on what `this` refers to:

- **Document middleware**: `this` is the document. For `save`, `validate`, `deleteOne`, `updateOne` (on a document), `init`.
- **Query middleware**: `this` is the query. For `find`, `findOne`, `countDocuments`, `updateOne`, `updateMany`, `deleteOne`, `deleteMany`, `findOneAndUpdate` and others.
- **Aggregate middleware**: `this` is the aggregation. For `aggregate`.
- **Model middleware**: `this` is the model. For `insertMany` and `bulkWrite`.

### 89: What is populate()?

`populate()` replaces a reference (an ObjectId) with the actual document from another collection.

```javascript
const postSchema = new Schema({
  title: String,
  author: { type: Schema.Types.ObjectId, ref: "User" },
});

const post = await Post.findById(id).populate("author");
post.author.name; // the user's name
```

Mongoose does this by running a second query on the `users` collection. It is not a database join.

### 90: What does the ref option do?

`ref` tells Mongoose which model an ObjectId points to, so `populate()` knows where to look.

```javascript
const commentSchema = new Schema({
  text: String,
  post: { type: Schema.Types.ObjectId, ref: "Post", required: true },
  author: { type: Schema.Types.ObjectId, ref: "User" },
});
```

The value of `ref` is the model name, not the collection name.

### 91: How do you populate only some fields?

Pass a second argument, or use the object form with `select`.

```javascript
await Post.find().populate("author", "name avatar");

await Post.find().populate({ path: "author", select: "name -_id" });
```

This keeps responses small and avoids leaking fields like `email` or `password`.

### 92: How do you populate more than one field?

```javascript
await Post.findById(id).populate("author").populate("category");
// or
await Post.findById(id).populate(["author", "category"]);
```

Each path is a separate query on the related collection.

### 93: How do you store a list of references?

Use an array of ObjectIds with `ref`.

```javascript
const userSchema = new Schema({
  name: String,
  followers: [{ type: Schema.Types.ObjectId, ref: "User" }],
});

const user = await User.findById(id).populate("followers", "name");
```

Be careful with arrays that can grow without limit. A document can be at most 16 MB.

### 94: How do you add an index to a field?

Use `index: true` on the field, or `schema.index()`.

```javascript
const userSchema = new Schema({
  email: { type: String, unique: true },
  lastName: { type: String, index: true },
});

userSchema.index({ lastName: 1, firstName: 1 }); // compound index
```

Mongoose creates these indexes when the model is compiled, if `autoIndex` is on.

### 95: What is autoIndex?

`autoIndex` controls whether Mongoose calls `createIndexes()` for each model when the app starts. It is `true` by default.

```javascript
mongoose.connect(uri, { autoIndex: false });
// or per schema
new Schema({}, { autoIndex: false });
```

Many teams turn it off in production, because building indexes on large collections uses a lot of resources. They build indexes with a migration or a script instead.

### 96: How do you see the queries Mongoose sends?

Turn on debug mode.

```javascript
mongoose.set("debug", true);
```

Mongoose then prints every collection call, like `users.find({ active: true }, { projection: { name: 1 } })`. You can also pass a function to log in your own format:

```javascript
mongoose.set("debug", (collection, method, query, doc) => {
  logger.debug({ collection, method, query });
});
```

### 97: How do you create an ObjectId by hand?

```javascript
const id = new mongoose.Types.ObjectId();
const fromString = new mongoose.Types.ObjectId("66f1c2a8e4b0a1b2c3d4e5f6");

id.toString(); // hex string
id.getTimestamp(); // Date the id was created
```

In Mongoose 9, creating an ObjectId from a number throws an error.

### 98: How do you check if a string is a valid ObjectId?

```javascript
mongoose.isValidObjectId("66f1c2a8e4b0a1b2c3d4e5f6"); // true
mongoose.isValidObjectId("hello"); // false
mongoose.isValidObjectId(6); // false in Mongoose 9
```

There is also `mongoose.isObjectIdOrHexString()`, which is stricter: it returns `true` only for ObjectId instances and 24 character hex strings. `isValidObjectId()` also accepts any 12 character string.

### 99: What is the difference between toObject() and toJSON()?

Both turn a document into a plain object. `toJSON()` is called by `JSON.stringify()` and by `res.json()` in Express. You can set different options for each in the schema.

```javascript
const userSchema = new Schema(
  { name: String, password: String },
  {
    toJSON: {
      virtuals: true,
      transform(doc, ret) {
        delete ret.password;
        return ret;
      },
    },
  },
);
```

This is a common way to hide fields in API responses.

### 100: What does isModified() do?

It tells you whether a path has changed since the document was loaded or created.

```javascript
const user = await User.findById(id);
user.isModified("email"); // false
user.email = "new@example.com";
user.isModified("email"); // true
user.modifiedPaths(); // ['email']
```

It is often used in pre save hooks, for example to hash a password only when it changed.

### 101: What is isNew?

`doc.isNew` is `true` when the document has not been saved to the database yet. After `save()` it becomes `false`. Documents loaded with `find()` have `isNew` set to `false`.

```javascript
userSchema.pre("save", async function () {
  if (this.isNew) {
    // first save, send welcome email later
  }
});
```

### 102: When do you need markModified()?

When you change a value that Mongoose cannot track, like a nested property inside a `Mixed` field or a `Date` changed with a method such as `setMonth()`.

```javascript
doc.settings.theme = "dark"; // settings is Mixed
doc.markModified("settings");
await doc.save();

doc.dueDate.setMonth(5);
doc.markModified("dueDate");
await doc.save();
```

Without `markModified()`, `save()` thinks nothing changed and does not send the update.

### 103: How do you hide a field by default?

Use `select: false`. The field is left out of query results unless you ask for it.

```javascript
const userSchema = new Schema({
  email: String,
  password: { type: String, select: false },
});

const user = await User.findOne({ email }).select("+password");
```

The `+` prefix adds a field that is hidden by default.

### 104: What is an alias in a schema?

An alias gives a field a second name in your code, while a shorter name is stored in the database.

```javascript
const schema = new Schema({
  n: { type: String, alias: "name" },
});

const doc = new Model({ name: "Anna" });
doc.name; // 'Anna'
doc.n; // 'Anna', stored as "n"
```

By default aliases do not work in query filters. You can turn that on with the `translateAliases` option.

### 105: What does orFail() do?

`orFail()` makes a query throw if no document is found, instead of returning `null`.

```javascript
const user = await User.findById(id).orFail();
// throws DocumentNotFoundError if nothing matches

const post = await Post.findById(id).orFail(new Error("Post not found"));
```

It saves you from writing `if (!doc) throw ...` everywhere.

### 106: How does query chaining work?

Most query methods return the query itself, so you can chain them before running it.

```javascript
const products = await Product.find({ category: "books" })
  .where("price")
  .gte(10)
  .lte(50)
  .select("name price")
  .sort({ price: 1 })
  .limit(20)
  .lean();
```

### 107: How does the where() query builder work?

`where()` lets you build filters with methods instead of an object.

```javascript
const users = await User.where("age")
  .gte(18)
  .lte(65)
  .where("role")
  .in(["user", "admin"])
  .where("name")
  .regex(/^a/i);
```

This is the same as:

```javascript
await User.find({
  age: { $gte: 18, $lte: 65 },
  role: { $in: ["user", "admin"] },
  name: /^a/i,
});
```

### 108: How do you search with a regular expression?

Pass a regex as the value, or use `$regex`.

```javascript
await User.find({ name: /^ann/i });
await User.find({ name: { $regex: "^ann", $options: "i" } });
```

If the search text comes from the user, escape special characters first. A regex that does not start with `^` (or uses the `i` flag) cannot use an index well and gets slow on big collections.

### 109: How do you push a value into an array?

With an update operator:

```javascript
await Post.updateOne({ _id: id }, { $push: { tags: "mongodb" } });
```

Or on a loaded document:

```javascript
const post = await Post.findById(id);
post.tags.push("mongodb");
await post.save();
```

Mongoose turns `push()` on a document array into a `$push` update.

### 110: What is the difference between $push and $addToSet?

`$push` always adds the value. `$addToSet` adds it only if it is not already in the array.

```javascript
await User.updateOne({ _id: id }, { $addToSet: { roles: "editor" } });
await User.updateOne({ _id: id }, { $pull: { roles: "editor" } }); // remove
```

On a document you can call `doc.roles.addToSet('editor')` and `doc.roles.pull('editor')`.

### 111: How do you get and set values on a document?

You can use normal property access, or `get()` and `set()`, which also accept dotted paths.

```javascript
user.name = "Anna";
user.set("address.city", "Berlin");
user.set({ name: "Anna", age: 30 });

user.get("address.city"); // 'Berlin'
```

### 112: Does save() insert or update?

Both. If `doc.isNew` is `true`, `save()` inserts the document. Otherwise it sends an `updateOne()` with only the changed fields.

```javascript
const user = await User.findById(id);
user.name = "New name";
await user.save(); // sends { $set: { name: 'New name' } }
```

If nothing changed, `save()` does not send anything to the database.

### 113: What is command buffering?

Mongoose lets you call model methods before the connection is open. It keeps the commands in a buffer and sends them once connected.

```javascript
mongoose.connect(uri); // not awaited
const users = await User.find(); // waits in the buffer until connected
```

If the connection does not open within `bufferTimeoutMS` (10 seconds by default), you get an error like `Operation users.find() buffering timed out after 10000ms`. You can turn buffering off with `mongoose.set('bufferCommands', false)`.

### 114: How do you check the state of the connection?

Use `readyState`.

```javascript
mongoose.connection.readyState;
// 0 = disconnected, 1 = connected, 2 = connecting, 3 = disconnecting
```

Health check endpoints often return 503 when the value is not `1`.

### 115: What is OverwriteModelError?

You get it when you call `mongoose.model('User', schema)` twice with the same name. This often happens with hot reload in Next.js or in tests.

A common fix:

```javascript
const User = mongoose.models.User || mongoose.model("User", userSchema);
export default User;
```

### 116: How do you organize models in a project?

A common setup is one file per model in a `models/` folder. Each file defines the schema and exports the model.

```javascript
// models/user.js
import { Schema, model } from "mongoose";

const userSchema = new Schema(
  { name: String, email: String },
  { timestamps: true },
);

export const User = model("User", userSchema);
```

The connection is opened once in a separate file (for example `db.js`) when the app starts.

### 117: How do you use Mongoose with ES modules and CommonJS?

Both work.

```javascript
// ES modules
import mongoose, { Schema, model } from "mongoose";

// CommonJS
const mongoose = require("mongoose");
const { Schema, model } = mongoose;
```

### 118: Where should you keep the connection string?

In an environment variable, not in the code. The connection string often has a password in it.

```javascript
await mongoose.connect(process.env.MONGODB_URI);
```

Use a `.env` file locally (not committed to git) and your host's secret settings in production.

### 119: What are the most used schema options?

- `timestamps`: adds `createdAt` and `updatedAt`
- `collection`: sets the collection name
- `versionKey`: renames or turns off `__v`
- `strict`: what to do with unknown fields
- `toJSON` / `toObject`: output settings
- `id`: turns off the `id` virtual
- `_id`: turns off `_id` (only for subdocuments)
- `autoIndex`: build indexes on startup
- `minimize`: remove empty objects
- `optimisticConcurrency`: version check on every save

```javascript
new Schema(
  { name: String },
  { timestamps: true, versionKey: false, collection: "people" },
);
```

### 120: How do you turn off _id for subdocuments?

Pass `_id: false` in the subdocument schema options.

```javascript
const pointSchema = new Schema({ lat: Number, lng: Number }, { _id: false });

const placeSchema = new Schema({
  name: String,
  location: pointSchema,
});
```

You cannot turn off `_id` for top-level documents, MongoDB needs it.

### 121: What does the minimize option do?

With `minimize: true` (the default), Mongoose removes empty objects when saving.

```javascript
const schema = new Schema({ name: String, settings: {} });
const doc = await Model.create({ name: "x", settings: {} });
// "settings" is not saved
```

Set `minimize: false` if you need empty objects stored.

### 122: How do you make an array field required?

An array always defaults to `[]`, and `required` passes for an empty array. To require at least one item, use a validator.

```javascript
const schema = new Schema({
  tags: {
    type: [String],
    validate: {
      validator: (v) => Array.isArray(v) && v.length > 0,
      message: "At least one tag is required",
    },
  },
});
```

### 123: When should you embed data and when should you reference it?

Embed (use subdocuments) when:

- the data is read together with the parent most of the time
- the child does not make sense on its own
- the list is small and will not grow without limit

Reference (store an ObjectId) when:

- the data is shared between many parents
- the list can grow large
- the child is often read or updated on its own

For example, embed the shipping address in an order. Reference the user from many orders.

### 124: How do you model a one-to-many relationship?

Store the parent's id on the child. This scales better than keeping a big array on the parent.

```javascript
const commentSchema = new Schema({
  post: { type: Schema.Types.ObjectId, ref: "Post", index: true },
  text: String,
});

const comments = await Comment.find({ post: postId }).sort({ createdAt: -1 });
```

### 125: How do you model a many-to-many relationship?

Common options:

1. Arrays of ids on one or both sides, for small lists:

```javascript
const studentSchema = new Schema({
  name: String,
  courses: [{ type: Schema.Types.ObjectId, ref: "Course" }],
});
```

2. A separate "join" collection when the lists are large or the link has extra data, like an `Enrollment` with `student`, `course` and `grade`.

### 126: How do you get a plain object from a document?

Call `toObject()`, or use `lean()` in the query if you never needed the document.

```javascript
const doc = await User.findById(id);
const plain = doc.toObject();

const plain2 = await User.findById(id).lean();
```

### 127: How do you sort by more than one field?

```javascript
await Product.find().sort({ category: 1, price: -1 });
// or
await Product.find().sort("category -price");
```

Results are sorted by `category` first, then by `price` within each category.

### 128: How do you do simple pagination with a total count?

Run the page query and the count together.

```javascript
const filter = { category: "books" };
const [items, total] = await Promise.all([
  Product.find(filter).sort({ _id: 1 }).skip(40).limit(20).lean(),
  Product.countDocuments(filter),
]);
```

Mongoose 9.10 added `Model.findAndCount()`, which does this for you:

```javascript
const [items, total] = await Product.findAndCount(filter, null, {
  sort: { _id: 1 },
  skip: 40,
  limit: 20,
});
```

### 129: What are the main Mongoose error types?

- `ValidationError`: one or more fields failed validation
- `ValidatorError`: one item inside `ValidationError.errors`
- `CastError`: a value could not be cast to the schema type
- `DocumentNotFoundError`: thrown by `orFail()` or when `save()` finds no document
- `VersionError`: version conflict when saving
- `StrictModeError`: unknown field with `strict: 'throw'`
- `MongooseServerSelectionError`: could not reach the server

Errors from MongoDB itself, like duplicate key errors, come through as `MongoServerError`.

### 130: How do you handle a duplicate key error?

Check for code `11000`.

```javascript
try {
  await User.create({ email: "anna@example.com" });
} catch (err) {
  if (err.code === 11000) {
    // err.keyValue => { email: 'anna@example.com' }
    return res.status(409).json({ message: "Email already in use" });
  }
  throw err;
}
```

### 131: How do you delete all documents in a collection?

```javascript
await User.deleteMany({});
```

This keeps the collection and its indexes. To remove the collection itself, use `drop()`.

### 132: How do you drop a collection or a database?

```javascript
await User.collection.drop(); // one collection
await mongoose.connection.dropDatabase(); // the whole database
```

`drop()` throws if the collection does not exist. These are often used in test setup, never against production data.

### 133: How do you compare two ObjectIds?

Do not use `===`, because they are objects. Use `equals()` or compare strings.

```javascript
post.author.equals(req.user._id); // true or false
post.author.toString() === req.user._id.toString(); // also works
```

For documents, `doc1.equals(doc2)` compares their `_id`.

### 134: How do you check if a path is populated?

Use `doc.populated(path)`. It returns the original id(s) if the path was populated, or `undefined` if not.

```javascript
const post = await Post.findById(id).populate("author");
post.populated("author"); // ObjectId of the author

const post2 = await Post.findById(id);
post2.populated("author"); // undefined
```

### 135: Does Mongoose support TypeScript?

Yes. Mongoose ships its own types. It can infer the document type from the schema, so you often do not need a separate interface.

```typescript
import { Schema, model, InferSchemaType } from "mongoose";

const userSchema = new Schema({
  name: { type: String, required: true },
  age: Number,
});

type User = InferSchemaType<typeof userSchema>;
const UserModel = model("User", userSchema);
```

### 136: What is the current version of Mongoose and what does it need?

The current major version is Mongoose 9 (9.0 came out in November 2025, the latest release is 9.11). It uses the MongoDB Node.js driver 7.x and needs Node.js 20.19.0 or newer. Mongoose 8 is still common in existing projects.

### 137: What is a discriminator?

A discriminator lets you store different types of documents in one collection, with a shared base schema and extra fields per type.

```javascript
const eventSchema = new Schema({ time: Date }, { discriminatorKey: "kind" });
const Event = mongoose.model("Event", eventSchema);

const ClickEvent = Event.discriminator("Click", new Schema({ url: String }));
const SignupEvent = Event.discriminator("Signup", new Schema({ plan: String }));

await ClickEvent.create({ time: new Date(), url: "/home" }); // kind: 'Click'
```

`ClickEvent.find()` returns only clicks. `Event.find()` returns all events.

### 138: What is a Mongoose plugin?

A plugin is a function that adds reusable features to a schema, like fields, methods or hooks.

```javascript
function timestampsByUser(schema) {
  schema.add({ createdBy: { type: Schema.Types.ObjectId, ref: "User" } });
}

postSchema.plugin(timestampsByUser);
```

You can apply a plugin to all schemas with `mongoose.plugin(fn)`, as long as you call it before creating models.

### 139: How do you use Mongoose in an Express app?

Connect once at startup, then use models in route handlers.

```javascript
import express from "express";
import mongoose from "mongoose";
import { Product } from "./models/product.js";

const app = express();
app.use(express.json());

app.get("/products/:id", async (req, res) => {
  if (!mongoose.isValidObjectId(req.params.id)) {
    return res.status(400).json({ message: "Invalid id" });
  }
  const product = await Product.findById(req.params.id).lean();
  if (!product) return res.status(404).json({ message: "Not found" });
  res.json(product);
});

await mongoose.connect(process.env.MONGODB_URI);
app.listen(3000);
```

### 140: How do you close the connection when the app stops?

Listen for shutdown signals, stop the HTTP server, then disconnect.

```javascript
process.on("SIGTERM", async () => {
  server.close();
  await mongoose.disconnect();
  process.exit(0);
});
```

This lets running queries finish and closes the pool cleanly.

### 141: What does Model.find() return when nothing matches?

An empty array `[]`, not `null`. `findOne()` and `findById()` return `null` when nothing matches. This is a common source of bugs, so check with `if (!doc)` only for single document methods.

### 142: How do you query fields inside nested objects?

Use dot notation in quotes.

```javascript
await User.find({ "address.city": "Berlin" });
await Order.find({ "items.productId": productId }); // inside an array of subdocuments
```

### 143: How do you update a nested field?

Use dot notation with `$set`, so you do not overwrite the whole object.

```javascript
await User.updateOne({ _id: id }, { $set: { "address.city": "Munich" } });
```

If you write `{ $set: { address: { city: 'Munich' } } }`, the whole `address` object is replaced and `street` and `zip` are lost.

### 144: How do you increment a number?

Use `$inc`. It is atomic, so two requests at the same time do not lose an update.

```javascript
await Post.updateOne({ _id: id }, { $inc: { views: 1 } });
await Product.updateOne({ _id: id }, { $inc: { stock: -2 } });
```

Doing `post.views++; await post.save()` works too, but `$inc` is safer under load.

### 145: What does Model.findOneAndUpdate() do with upsert?

With `upsert: true`, if no document matches, MongoDB creates one from the filter and the update.

```javascript
const setting = await Setting.findOneAndUpdate(
  { key: "theme" },
  { $set: { value: "dark" } },
  { upsert: true, returnDocument: "after" },
);
```

Schema defaults are applied to the new document because `setDefaultsOnInsert` is on by default.

### 146: How do you get the raw MongoDB collection from a model?

Use `Model.collection`. It is a thin wrapper around the driver's collection. Calls on it skip Mongoose casting, validation and middleware.

```javascript
await User.collection.createIndex({ email: 1 }, { unique: true });
const raw = await User.collection.findOne({ email: "anna@example.com" });
```

You can get the driver's `Db` object from `mongoose.connection.db`.

### 147: What are immutable fields?

A field with `immutable: true` cannot be changed after the document is created. Mongoose ignores changes to it (or throws with `strict: 'throw'`).

```javascript
const userSchema = new Schema({
  username: { type: String, immutable: true },
  createdAt: { type: Date, immutable: true, default: Date.now },
});
```

The `createdAt` field added by `timestamps` is immutable by default.

### 148: Can a field be required only in some cases?

Yes. `required` can be a function. `this` is the document.

```javascript
const paymentSchema = new Schema({
  method: { type: String, enum: ["card", "bank"] },
  iban: {
    type: String,
    required: function () {
      return this.method === "bank";
    },
  },
});
```

### 149: How do you seed a database with Mongoose?

Write a script that connects, clears the collections and inserts data.

```javascript
import mongoose from "mongoose";
import { Product } from "./models/product.js";

await mongoose.connect(process.env.MONGODB_URI);
await Product.deleteMany({});
await Product.insertMany([
  { name: "Pen", price: 1 },
  { name: "Notebook", price: 4 },
]);
await mongoose.disconnect();
```

### 150: What are common beginner mistakes with Mongoose?

- Forgetting `await`, so the code continues before the query finishes.
- Expecting `unique: true` to be a validator.
- Expecting update methods to run validators and `save` hooks.
- Using arrow functions in methods or hooks, so `this` is wrong.
- Changing a `Mixed` field without `markModified()`.
- Defining hooks after `mongoose.model()` is called.
- Using `new: true`, which is now deprecated, instead of `returnDocument: 'after'`.
- Sending whole documents to the client and leaking fields like `password`.

## Moderate Questions (151-300)

### 151: What connection options do you usually set in production?

```javascript
await mongoose.connect(process.env.MONGODB_URI, {
  maxPoolSize: 20, // max open sockets (default 100)
  minPoolSize: 2,
  serverSelectionTimeoutMS: 5000, // how long to look for a server (default 30000)
  socketTimeoutMS: 45000, // close idle sockets after this
  appName: "orders-api", // shows up in MongoDB logs
  autoIndex: false,
});
```

Most of these are driver options that Mongoose passes through. `autoIndex` and `bufferCommands` are Mongoose options.

### 152: How do you connect to more than one database?

Use `mongoose.createConnection()`. Each connection has its own models.

```javascript
const mainDb = mongoose.createConnection(process.env.MAIN_URI);
const logsDb = mongoose.createConnection(process.env.LOGS_URI);

const User = mainDb.model("User", userSchema);
const AuditLog = logsDb.model("AuditLog", auditSchema);

await Promise.all([mainDb.asPromise(), logsDb.asPromise()]);
```

Models created with `mongoose.model()` always use the default connection, so with several connections you must call `connection.model()`.

### 153: What does useDb() do?

`useDb()` gives you a connection object for another database on the same cluster, using the same connection pool.

```javascript
const tenantDb = mongoose.connection.useDb(`tenant_${tenantId}`, {
  useCache: true,
});
const Invoice = tenantDb.model("Invoice", invoiceSchema);
```

`useCache: true` makes Mongoose reuse the same connection object for the same name instead of making a new one each time. This is a common pattern for database-per-tenant apps.

### 154: How does the connection pool work?

The driver keeps a pool of open sockets to each server. Each operation borrows a socket and returns it when done. `maxPoolSize` (default 100) limits how many operations can run at the same time per server. If all sockets are busy, new operations wait.

A pool that is too small makes requests wait. A pool that is too large with many app instances can use up the server's connection limit.

### 155: How do you handle a failed first connection?

`mongoose.connect()` rejects if it cannot find a server within `serverSelectionTimeoutMS`. Mongoose does not retry the first connection by itself, so you catch the error and either retry or exit.

```javascript
async function connectWithRetry(retries = 5) {
  for (let i = 1; i <= retries; i++) {
    try {
      await mongoose.connect(process.env.MONGODB_URI, {
        serverSelectionTimeoutMS: 5000,
      });
      return;
    } catch (err) {
      console.error(`Connect attempt ${i} failed`, err.message);
      await new Promise((r) => setTimeout(r, 2000 * i));
    }
  }
  process.exit(1);
}
```

After the first successful connection, the driver reconnects on its own if the connection drops.

### 156: What changed about pre middleware in Mongoose 9?

Pre middleware no longer gets a `next()` callback. You write `async` functions or return a promise. Throwing an error (or rejecting) stops the operation.

```javascript
// Mongoose 8 and older
schema.pre("save", function (next) {
  this.slug = slugify(this.title);
  next();
});

// Mongoose 9
schema.pre("save", async function () {
  this.slug = slugify(this.title);
});
```

The old `isAsync` style, `function (next, done)`, is also gone.

### 157: How do you stop an operation from inside a pre hook?

Throw an error. The operation is not run and the error is returned to the caller.

```javascript
orderSchema.pre("save", async function () {
  if (this.items.length === 0) {
    throw new Error("Order must have at least one item");
  }
});
```

### 158: What is this inside query middleware?

`this` is the `Query` object, not a document. You can read and change the filter, update and options.

```javascript
userSchema.pre("find", function () {
  this.where({ deletedAt: null });
  console.log(this.getFilter());
});

userSchema.pre("findOneAndUpdate", function () {
  this.set({ updatedBy: this.getOptions().userId });
});
```

Use `this.getFilter()`, `this.getUpdate()`, `this.getOptions()` and `this.setUpdate()`.

### 159: Why does a pre save hook not run on findOneAndUpdate()?

Because `save` middleware is document middleware and `findOneAndUpdate()` does not load a document, it sends the update straight to MongoDB. For updates you need query middleware.

```javascript
userSchema.pre("findOneAndUpdate", async function () {
  const update = this.getUpdate();
  if (update.password) {
    update.password = await bcrypt.hash(update.password, 12);
  }
});
```

This is why many teams update users with `findById()` + `save()` when hooks matter.

### 160: How do you register a hook for document or query deleteOne?

`deleteOne` exists both on documents and on queries. By default `schema.pre('deleteOne')` is a query hook. Use options to pick.

```javascript
// runs for doc.deleteOne()
postSchema.pre(
  "deleteOne",
  { document: true, query: false },
  async function () {
    await Comment.deleteMany({ post: this._id });
  },
);

// runs for Post.deleteOne(filter)
postSchema.pre(
  "deleteOne",
  { document: false, query: true },
  async function () {
    console.log("Deleting", this.getFilter());
  },
);
```

The same applies to `updateOne`.

### 161: What is error handling middleware?

A post hook with three arguments `(error, res, next)` runs only when the operation fails. You can turn low level errors into nicer ones.

```javascript
userSchema.post("save", function (error, doc, next) {
  if (error.name === "MongoServerError" && error.code === 11000) {
    next(new Error("Email already exists"));
  } else {
    next(error);
  }
});
```

Error handling post middleware still uses `next` in Mongoose 9. Only pre middleware lost it.

### 162: How do you use aggregate middleware?

`this` is the aggregation object. You can add stages to the pipeline.

```javascript
productSchema.pre("aggregate", function () {
  this.pipeline().unshift({ $match: { deletedAt: null } });
});
```

This is useful for soft delete, so aggregations also skip deleted documents.

### 163: Which operations do not run save middleware?

`save` hooks run only for `save()` and `create()`. They do not run for:

- `insertMany()`
- `updateOne()`, `updateMany()`, `findOneAndUpdate()`, `findByIdAndUpdate()`
- `replaceOne()`
- `bulkWrite()`
- direct calls on `Model.collection`

If you have logic that must always run, put it in a place all write paths use, or add both document and query hooks.

### 164: How do you run validators on updates?

Pass `runValidators: true`.

```javascript
await Product.findByIdAndUpdate(
  id,
  { price: -10 },
  { runValidators: true, returnDocument: "after" },
); // throws ValidationError
```

You can turn it on for all queries with `mongoose.set('runValidators', true)`. Update validators only check paths that are in the update, and only for `$set`, `$unset`, `$push`, `$addToSet`, `$pull` and `$pullAll`. `required` only fails if you `$unset` the field.

### 165: What is this inside an update validator?

When a validator runs on an update, `this` is the query, not a document. Validators that use `this.someOtherField` work in `save()` but break in updates.

```javascript
const schema = new Schema({
  startDate: Date,
  endDate: {
    type: Date,
    validate: {
      validator: function (value) {
        if (this instanceof mongoose.Query) {
          const update = this.getUpdate();
          return !update.$set?.startDate || value > update.$set.startDate;
        }
        return value > this.startDate;
      },
    },
  },
});
```

### 166: How do you write an async validator?

Return a promise or use an `async` function.

```javascript
const userSchema = new Schema({
  username: {
    type: String,
    validate: {
      validator: async function (value) {
        const count = await mongoose.models.User.countDocuments({
          username: value,
          _id: { $ne: this._id },
        });
        return count === 0;
      },
      message: "Username already taken",
    },
  },
});
```

Keep the unique index anyway. An async check like this can still let two requests through at the same time.

### 167: What is validateSync()?

`validateSync()` runs validation without waiting and returns the error (or `undefined`). It skips async validators.

```javascript
const product = new Product({ price: -1 });
const error = product.validateSync();
if (error) {
  console.log(error.errors.price.message);
}
```

It is useful in tests or when you need to validate in a place that cannot wait.

### 168: How do you validate a document without saving it?

```javascript
const order = new Order(req.body);
try {
  await order.validate();
} catch (err) {
  return res.status(400).json(err.errors);
}
```

You can validate only some paths with `order.validate(['email', 'total'])`. You can also validate a plain object with `Model.validate(obj)`.

### 169: What does doc.invalidate() do?

It marks a path as invalid by hand. The next `validate()` or `save()` fails with that error.

```javascript
orderSchema.pre("validate", function () {
  if (this.discount > this.total) {
    this.invalidate(
      "discount",
      "Discount cannot be more than total",
      this.discount,
    );
  }
});
```

### 170: How do you format validation errors for an API?

Map `err.errors` into a simple object.

```javascript
function formatValidationError(err) {
  return Object.fromEntries(
    Object.entries(err.errors).map(([path, e]) => [path, e.message]),
  );
}

app.use((err, req, res, next) => {
  if (err.name === "ValidationError") {
    return res.status(400).json({ errors: formatValidationError(err) });
  }
  if (err.name === "CastError") {
    return res.status(400).json({ message: `Invalid ${err.path}` });
  }
  next(err);
});
```

### 171: How do you populate nested references?

Use `populate` inside `populate`.

```javascript
const post = await Post.findById(id).populate({
  path: "comments",
  populate: { path: "author", select: "name" },
});
```

Each level is a separate query. Deep population chains can get slow, so keep them short.

### 172: What options does populate() take?

The main ones:

- `path`: field to populate
- `select`: which fields to return
- `match`: extra filter for related docs
- `options`: `sort`, `limit` and others
- `perDocumentLimit`: limit per parent document
- `model`: which model to use (overrides `ref`)
- `populate`: nested population

```javascript
await User.find().populate({
  path: "posts",
  match: { published: true },
  select: "title createdAt",
  options: { sort: { createdAt: -1 } },
  perDocumentLimit: 5,
});
```

### 173: What is the difference between limit and perDocumentLimit in populate?

`options.limit` limits the total number of related documents across **all** parents, because Mongoose runs one query for all of them. So with `limit: 5` and 10 users, you get 5 posts total, not 5 each.

`perDocumentLimit: 5` runs a separate query per parent so each one gets up to 5. It is correct but costs more queries.

### 174: What happens if populate() cannot find a referenced document?

The path becomes `null` for single refs. For arrays, missing items are removed from the array.

```javascript
const post = await Post.findById(id).populate("author");
post.author; // null if the user was deleted
```

If you set `match` and a related doc does not match, the same thing happens. Code must handle `null` here.

### 175: What is virtual populate?

Virtual populate lets you populate in the "reverse" direction without storing an array of ids on the parent.

```javascript
const userSchema = new Schema({ name: String }, { toJSON: { virtuals: true } });

userSchema.virtual("posts", {
  ref: "Post",
  localField: "_id",
  foreignField: "author",
});

const user = await User.findById(id).populate("posts");
```

`user.posts` is filled with all posts where `post.author` equals `user._id`. Nothing is stored on the user.

### 176: How do you get a count with virtual populate?

Add `count: true` to the virtual.

```javascript
userSchema.virtual("postCount", {
  ref: "Post",
  localField: "_id",
  foreignField: "author",
  count: true,
});

const user = await User.findById(id).populate("postCount");
user.postCount; // number
```

### 177: What is refPath?

`refPath` lets one field point to different models. Another field holds the model name.

```javascript
const commentSchema = new Schema({
  text: String,
  target: {
    type: Schema.Types.ObjectId,
    refPath: "targetModel",
    required: true,
  },
  targetModel: { type: String, enum: ["Post", "Product"], required: true },
});

const comments = await Comment.find().populate("target");
```

### 178: Does populate() work with lean()?

Yes. The populated fields are also plain objects.

```javascript
const posts = await Post.find().populate("author", "name").lean();
```

Virtual populate also works with `lean()`, but other virtuals on the results do not.

### 179: How do you populate a document you already loaded?

Call `populate()` on the document.

```javascript
const post = await Post.findById(id);
await post.populate("author");
await post.populate([{ path: "category" }, { path: "tags", select: "name" }]);
```

To undo it, use `post.depopulate('author')`, which puts the ids back.

### 180: How do you populate across connections?

Pass the model itself, not just the name, so Mongoose uses the right connection.

```javascript
const Post = mainDb.model("Post", postSchema);
const User = usersDb.model("User", userSchema);

await Post.find().populate({ path: "author", model: User });
```

### 181: How do discriminators store the type?

Mongoose adds a field (default name `__t`) with the discriminator name. Queries on a discriminator model add a filter on that field.

```javascript
const ClickEvent = Event.discriminator("Click", clickSchema);
await ClickEvent.find({});
// sends: events.find({ __t: 'Click' })
```

You can rename it with the `discriminatorKey` schema option, and set a custom value with the third argument of `discriminator()`.

### 182: What are embedded discriminators?

Discriminators can be used on arrays of subdocuments too, so one array can hold different shapes.

```javascript
const blockSchema = new Schema({}, { discriminatorKey: "kind", _id: false });
const pageSchema = new Schema({ blocks: [blockSchema] });

pageSchema.path("blocks").discriminator("text", new Schema({ body: String }));
pageSchema
  .path("blocks")
  .discriminator("image", new Schema({ url: String, alt: String }));

const Page = mongoose.model("Page", pageSchema);
await Page.create({
  blocks: [
    { kind: "text", body: "Hi" },
    { kind: "image", url: "/a.png" },
  ],
});
```

Each item is cast and validated with the schema for its `kind`.

### 183: How do you work with arrays of subdocuments?

Mongoose gives document arrays extra methods.

```javascript
const order = await Order.findById(id);

order.items.push({ product: productId, qty: 2 });
const item = order.items.id(itemId); // find by _id
item.qty = 3;
order.items.pull(otherItemId); // remove by _id
await order.save();
```

`items.id()` works only on arrays of subdocuments that have `_id`.

### 184: How do you update one item in an array with an update query?

Use the positional `$` operator, which points to the first matched array item.

```javascript
await Order.updateOne(
  { _id: orderId, "items._id": itemId },
  { $set: { "items.$.qty": 3 } },
);
```

The array field must appear in the filter for `$` to work.

### 185: How do you update many items in an array at once?

Use `$[]` for all items or `$[name]` with `arrayFilters` for matching items.

```javascript
// all items
await Order.updateOne({ _id: id }, { $set: { "items.$[].shipped": true } });

// only items with qty > 5
await Order.updateOne(
  { _id: id },
  { $set: { "items.$[big].bulk": true } },
  { arrayFilters: [{ "big.qty": { $gt: 5 } }] },
);
```

Mongoose casts values in `arrayFilters` too.

### 186: What is the difference between a nested path and a single nested subdocument?

```javascript
// nested path
new Schema({ address: { city: String } });

// single nested subdocument
new Schema({ address: new Schema({ city: String }) });
```

A nested path is just part of the parent. It is never `undefined` and has no own hooks. A subdocument can be `undefined` or `null`, has its own `_id` (unless turned off), its own validators, methods and middleware, and you can set `required` on it as a whole.

### 187: Do subdocuments have their own middleware?

Yes. Subdocuments support `save` and `validate` middleware, which run when the parent is saved. Subdocument `pre('save')` hooks run after the parent's `pre('validate')` hooks and before the parent's `pre('save')` hooks.

```javascript
itemSchema.pre("save", async function () {
  this.total = this.price * this.qty;
});
```

Subdocuments do not support query middleware, because you never query them alone.

### 188: How do you hide sensitive fields from JSON output?

Use a `toJSON` transform, `select: false`, or both.

```javascript
const userSchema = new Schema(
  {
    email: String,
    password: { type: String, select: false },
    resetToken: String,
  },
  {
    toJSON: {
      transform(doc, ret) {
        delete ret.password;
        delete ret.resetToken;
        delete ret.__v;
        return ret;
      },
    },
  },
);
```

Note that `toJSON` transforms do not run on `lean()` results, so `select: false` is the safer default for secrets.

### 189: How do you hash passwords and check them with Mongoose?

```javascript
import bcrypt from "bcrypt";

userSchema.pre("save", async function () {
  if (!this.isModified("password")) return;
  this.password = await bcrypt.hash(this.password, 12);
});

userSchema.methods.checkPassword = function (plain) {
  return bcrypt.compare(plain, this.password);
};

const user = await User.findOne({ email }).select("+password");
if (!user || !(await user.checkPassword(password))) {
  throw new Error("Wrong email or password");
}
```

### 190: How do you run an aggregation with Mongoose?

Use `Model.aggregate()` with a pipeline.

```javascript
const stats = await Order.aggregate([
  { $match: { status: "paid" } },
  {
    $group: {
      _id: "$customer",
      total: { $sum: "$amount" },
      orders: { $sum: 1 },
    },
  },
  { $sort: { total: -1 } },
  { $limit: 10 },
]);
```

The results are plain objects, not documents.

### 191: Does Mongoose cast values in aggregation pipelines?

No. Mongoose does not cast aggregation stages, because the output shape can be anything. You have to pass the right types yourself.

```javascript
// Wrong: matches nothing, string is not an ObjectId
await Order.aggregate([{ $match: { customer: req.params.id } }]);

// Right
await Order.aggregate([
  { $match: { customer: new mongoose.Types.ObjectId(req.params.id) } },
]);
```

Dates have the same problem. Use `new Date(...)` in `$match`.

### 192: How do you do a join in an aggregation?

Use `$lookup`. Here you use the collection name, not the model name.

```javascript
const posts = await Post.aggregate([
  { $match: { published: true } },
  {
    $lookup: {
      from: "users",
      localField: "author",
      foreignField: "_id",
      as: "author",
    },
  },
  { $unwind: "$author" },
  { $project: { title: 1, "author.name": 1 } },
]);
```

To be safe about the name, use `User.collection.name` for `from`.

### 193: What helper methods does the Aggregate object have?

You can build a pipeline with methods instead of an array.

```javascript
const result = await Order.aggregate()
  .match({ status: "paid" })
  .group({ _id: "$customer", total: { $sum: "$amount" } })
  .sort({ total: -1 })
  .limit(5)
  .option({ allowDiskUse: true });
```

Other helpers include `project()`, `lookup()`, `unwind()`, `facet()`, `count()`, `addFields()` and `pipeline()` (to read the stages).

### 194: How do you stream a large result set?

Use `cursor()`. It reads documents one at a time instead of loading all into memory.

```javascript
const cursor = User.find({ active: true }).lean().cursor();

for await (const user of cursor) {
  await sendNewsletter(user);
}
```

Aggregations also have `.cursor()`.

### 195: What does eachAsync() do?

`eachAsync()` loops over a cursor and waits for your function on each document. You can process several at once with `parallel`.

```javascript
await User.find({ active: true })
  .cursor()
  .eachAsync(
    async (user) => {
      await sendEmail(user.email);
    },
    { parallel: 10 },
  );
```

There is also `batchSize` to receive arrays of documents.

### 196: What is bulkWrite()?

`bulkWrite()` sends many different write operations in one command.

```javascript
await Product.bulkWrite([
  { insertOne: { document: { name: "Pen", price: 1 } } },
  { updateOne: { filter: { name: "Book" }, update: { $inc: { stock: 5 } } } },
  { deleteOne: { filter: { name: "Old item" } } },
]);
```

Mongoose casts the filters and updates and validates the documents in `insertOne` and `replaceOne` operations, but it does not run document middleware like `save` hooks. By default operations are ordered: it stops at the first error. Pass `ordered: false` to continue.

### 197: What does bulkSave() do?

`bulkSave()` takes loaded documents, works out what changed in each one, and sends all changes with one `bulkWrite()`.

```javascript
const products = await Product.find({ category: "books" });
for (const p of products) {
  p.price = Math.round(p.price * 1.1);
}
await Product.bulkSave(products);
```

It validates the documents first, but does not run `save` middleware.

### 198: What does includeResultMetadata do?

For `findOneAndUpdate()` and similar methods, it returns the full driver result instead of only the document. It replaced the old `rawResult` option in Mongoose 8.

```javascript
const res = await User.findOneAndUpdate(
  { email },
  { $set: { name: "Anna" } },
  { upsert: true, returnDocument: "after", includeResultMetadata: true },
);

res.value; // the document
res.lastErrorObject.updatedExisting; // false if it was created by upsert
```

### 199: What does updateOne() return?

An `UpdateResult` object:

```javascript
const result = await User.updateOne({ _id: id }, { name: "Anna" });
// {
//   acknowledged: true,
//   matchedCount: 1,
//   modifiedCount: 1,
//   upsertedId: null,
//   upsertedCount: 0
// }
```

`matchedCount` can be 1 while `modifiedCount` is 0, when the new value equals the old one.

### 200: What is an update pipeline and why does Mongoose 9 block it?

An update pipeline is an array of aggregation stages used as the update, so you can set a field based on other fields.

```javascript
await Product.updateMany(
  {},
  [{ $set: { total: { $multiply: ["$price", "$qty"] } } }],
  { updatePipeline: true },
);
```

Mongoose does not cast update pipelines. In Mongoose 9 they throw an error unless you pass `updatePipeline: true` or set `mongoose.set('updatePipeline', true)`. This makes you opt in on purpose.

### 201: How do timestamps work with update queries?

Mongoose adds `$set: { updatedAt }` to `updateOne()`, `updateMany()`, `findOneAndUpdate()` and `replaceOne()`. For upserts it also adds `$setOnInsert: { createdAt }`.

You can skip it for one call:

```javascript
await Post.updateOne(
  { _id: id },
  { $inc: { views: 1 } },
  { timestamps: false },
);
```

That is useful for counters, where you do not want `updatedAt` to change on every view.

### 202: How do you use a custom function for the current time in timestamps?

Use `currentTime` in the timestamps option.

```javascript
const schema = new Schema(
  { name: String },
  {
    timestamps: { currentTime: () => Math.floor(Date.now() / 1000) },
  },
);
```

This is useful if you store Unix seconds, or in tests where you want a fixed time.

### 203: What is query selector injection and how does Mongoose help?

If you pass user input straight into a filter, an attacker can send an object instead of a string:

```javascript
// body: { "email": "a@b.com", "password": { "$ne": null } }
await User.findOne({ email: req.body.email, password: req.body.password });
```

This matches any user. Mongoose has the `sanitizeFilter` option, which wraps objects that start with `$` in `$eq`, so they are treated as values.

```javascript
mongoose.set("sanitizeFilter", true);
// or per query
await User.findOne(filter).setOptions({ sanitizeFilter: true });
```

Validating input types (for example with Zod) is still the main defense.

### 204: How does trusted() work with sanitizeFilter?

When `sanitizeFilter` is on, your own `$` operators would also be wrapped. Use `mongoose.trusted()` to mark the ones you wrote on purpose.

```javascript
mongoose.set("sanitizeFilter", true);

await Product.find({
  name: req.query.name,
  price: mongoose.trusted({ $gte: 10 }),
});
```

### 205: What does translateAliases do?

It lets you use aliases in filters, projections and updates.

```javascript
const schema = new Schema({ n: { type: String, alias: "name" } });
const Model = mongoose.model("Model", schema);

await Model.find({ name: "Anna" }, null, { translateAliases: true });
// sends { n: 'Anna' }
```

You can set it globally with `mongoose.set('translateAliases', true)`.

### 206: How do you use virtuals with lean()?

Lean results do not have virtuals. Use the `mongoose-lean-virtuals` plugin, or compute the fields yourself. Mongoose 8 also added `Model.applyVirtuals()` to add virtuals to a plain object.

```javascript
const users = await User.find().lean();
users.forEach((u) => User.applyVirtuals(u));
```

### 207: What is the "Query was already executed" error?

A `Query` can run only once. If you `await` the same query object twice, Mongoose throws `MongooseError: Query was already executed`.

```javascript
const q = User.find({ active: true });
await q;
await q; // throws

// fix
await q.clone();
```

This often happens when someone mixes a callback and `await`, or calls `exec()` and then `await`s the query.

### 208: How do you check which index a query uses?

Use `explain()`.

```javascript
const plan = await User.find({ email: "anna@example.com" }).explain(
  "executionStats",
);
console.log(plan.queryPlanner.winningPlan);
console.log(plan.executionStats.totalDocsExamined);
```

If you see `COLLSCAN`, the query is not using an index.

### 209: How do you force a query to use a specific index?

Use `hint()`.

```javascript
await Order.find({ customer: id, status: "paid" }).hint({
  customer: 1,
  status: 1,
});
```

Only do this when you know the planner picks the wrong index. Usually it chooses well.

### 210: What is collation and how do you use it?

Collation sets language rules for comparing strings, for example case-insensitive matching.

```javascript
await User.find({ name: "anna" }).collation({ locale: "en", strength: 2 });
```

`strength: 2` ignores case. To use an index for this, the index must have the same collation:

```javascript
userSchema.index({ name: 1 }, { collation: { locale: "en", strength: 2 } });
```

### 211: How do you add text search?

Create a text index and use `$text`.

```javascript
articleSchema.index(
  { title: "text", body: "text" },
  { weights: { title: 5, body: 1 } },
);

const results = await Article.find(
  { $text: { $search: "mongoose hooks" } },
  { score: { $meta: "textScore" } },
).sort({ score: { $meta: "textScore" } });
```

A collection can have only one text index. For better search on Atlas, use Atlas Search with `$search` in an aggregation.

### 212: How do you store and query locations?

Store GeoJSON points and add a `2dsphere` index.

```javascript
const placeSchema = new Schema({
  name: String,
  location: {
    type: { type: String, enum: ["Point"], required: true },
    coordinates: { type: [Number], required: true }, // [lng, lat]
  },
});
placeSchema.index({ location: "2dsphere" });

const nearby = await Place.find({
  location: {
    $near: {
      $geometry: { type: "Point", coordinates: [13.405, 52.52] },
      $maxDistance: 2000, // meters
    },
  },
});
```

Longitude comes first, then latitude.

### 213: What do syncIndexes() and diffIndexes() do?

`diffIndexes()` compares the indexes in your schema with those in MongoDB and tells you what to create and drop. `syncIndexes()` makes MongoDB match the schema: it drops indexes not in the schema and builds the missing ones.

```javascript
const diff = await User.diffIndexes();
console.log(diff); // { toDrop: [...], toCreate: [...] }

await User.syncIndexes();
```

Be careful in production: `syncIndexes()` drops indexes someone added by hand.

### 214: What is the difference between createIndexes() and syncIndexes()?

`createIndexes()` only builds indexes from the schema that do not exist yet. It never drops anything. `autoIndex` uses it on startup. `syncIndexes()` also drops extra indexes. The old `ensureIndexes()` was removed.

### 215: What does Model.init() do?

`init()` makes sure the collection exists (if `autoCreate` is on) and builds the indexes (if `autoIndex` is on). Mongoose calls it for you when the model is created. It returns a promise you can wait for.

```javascript
await User.init(); // wait until indexes are built
```

This matters in tests that check unique constraints: if you insert duplicates before the unique index is built, MongoDB does not reject them.

### 216: How do you create a capped collection?

Use the `capped` schema option.

```javascript
const logSchema = new Schema(
  { message: String },
  {
    capped: { size: 1024 * 1024 * 10, max: 10000 }, // 10 MB or 10k docs
  },
);
```

A capped collection keeps only the newest documents and drops the oldest when full. The collection must be created as capped, so this only works if Mongoose creates it.

### 217: How do you make documents expire automatically?

Use a TTL index, with `expires` on a date field.

```javascript
const sessionSchema = new Schema({
  token: String,
  createdAt: { type: Date, default: Date.now, expires: "7d" },
});
```

MongoDB removes expired documents with a background job that runs about every 60 seconds, so deletion is not instant. Changing `expires` later does not change an existing index; you must update or rebuild it.

### 218: What schema helper methods are useful for reuse?

- `schema.add(obj)`: add fields
- `schema.remove(path)`: remove a field
- `schema.clone()`: deep copy
- `schema.pick(paths)`: new schema with only some fields
- `schema.omit(paths)`: new schema without some fields
- `schema.path(name)`: get the SchemaType of a field

```javascript
const baseSchema = new Schema({
  name: String,
  email: String,
  password: String,
});
const publicSchema = baseSchema.omit(["password"]);
```

### 219: What does schema.loadClass() do?

It lets you write methods, statics and virtuals as an ES6 class.

```javascript
class UserClass {
  get fullName() {
    return `${this.firstName} ${this.lastName}`;
  }
  static findByEmail(email) {
    return this.findOne({ email });
  }
  greet() {
    return `Hi ${this.firstName}`;
  }
}

userSchema.loadClass(UserClass);
```

Getters become virtuals, static methods become statics and normal methods become instance methods.

### 220: How do you write a soft delete plugin?

```javascript
function softDelete(schema) {
  schema.add({ deletedAt: { type: Date, default: null, index: true } });

  schema.methods.softDelete = function () {
    this.deletedAt = new Date();
    return this.save();
  };

  const hideDeleted = function () {
    if (this.getOptions().withDeleted) return;
    this.where({ deletedAt: null });
  };

  schema.pre(
    ["find", "findOne", "countDocuments", "findOneAndUpdate", "updateMany"],
    hideDeleted,
  );
}

postSchema.plugin(softDelete);

await Post.find({}).setOptions({ withDeleted: true }); // include deleted
```

Remember that `aggregate()` needs its own hook.

### 221: What are query helpers?

Query helpers are chainable methods you add to queries.

```javascript
productSchema.query.inStock = function () {
  return this.where({ stock: { $gt: 0 } });
};

productSchema.query.byCategory = function (category) {
  return this.where({ category });
};

const items = await Product.find().inStock().byCategory("books");
```

You can also use the `query` schema option, and Mongoose 9 added `schema.queryHelper(name, fn)` which is easier to type in TypeScript.

### 222: How do you type a model in TypeScript?

Let Mongoose infer it, or pass your own interface.

```typescript
import { Schema, model, Types, HydratedDocument } from "mongoose";

interface IPost {
  title: string;
  author: Types.ObjectId;
  tags: string[];
}

const postSchema = new Schema<IPost>({
  title: { type: String, required: true },
  author: { type: Schema.Types.ObjectId, ref: "User", required: true },
  tags: [String],
});

export const Post = model<IPost>("Post", postSchema);
export type PostDocument = HydratedDocument<IPost>;
```

Use `Types.ObjectId` in the interface and `Schema.Types.ObjectId` in the schema.

### 223: What is HydratedDocument?

`HydratedDocument<T>` is the type of a full Mongoose document for raw type `T`. It includes the fields plus document methods like `save()` and `isModified()`.

```typescript
async function rename(post: HydratedDocument<IPost>, title: string) {
  post.title = title;
  await post.save();
}
```

The plain data type (what `lean()` returns) is just `IPost` plus `_id`.

### 224: How do you add methods and statics in TypeScript?

Pass them through the schema generics, or use the `methods` and `statics` options so types are inferred.

```typescript
const userSchema = new Schema(
  { firstName: String, lastName: String, email: String },
  {
    methods: {
      fullName() {
        return `${this.firstName} ${this.lastName}`;
      },
    },
    statics: {
      findByEmail(email: string) {
        return this.findOne({ email });
      },
    },
  },
);

const User = model("User", userSchema);
const u = await User.findByEmail("a@b.com");
u?.fullName();
```

### 225: What TypeScript changes came in Mongoose 9?

- `FilterQuery` was renamed to `QueryFilter`, and filters are now checked more strictly. `find({ age: 'abc' })` on a number field is a type error.
- `create()` and `insertOne()` no longer take a generic parameter. They accept `Partial` of the raw document type.
- `doc.id` is now typed as `string`, not `any`.

Code that passed loosely typed filters through generic helpers may need an `as QueryFilter<T>` cast.

### 226: How do you test Mongoose code without a real database server?

A common choice is `mongodb-memory-server`. It downloads a real `mongod` binary and runs it in memory for the tests.

```javascript
import { MongoMemoryServer } from "mongodb-memory-server";
import mongoose from "mongoose";

let mongod;

beforeAll(async () => {
  mongod = await MongoMemoryServer.create();
  await mongoose.connect(mongod.getUri());
});

afterEach(async () => {
  const collections = await mongoose.connection.db.collections();
  await Promise.all(collections.map((c) => c.deleteMany({})));
});

afterAll(async () => {
  await mongoose.disconnect();
  await mongod.stop();
});
```

It is closer to production than mocking, because real queries run.

### 227: Should you mock Mongoose models in unit tests?

You can, for code where the database is not what you are testing, like a service that calls `User.findById()`.

```javascript
import { vi } from "vitest";
import { User } from "../models/user.js";

vi.spyOn(User, "findById").mockReturnValue({
  lean: vi.fn().mockResolvedValue({ _id: "1", name: "Anna" }),
});
```

The downside is that you have to copy the chain shape (`findById().lean()`), and mocks do not catch wrong filters. Many teams prefer an in-memory server for anything that touches queries.

### 228: How do you run a transaction with Mongoose?

Transactions need a replica set or a sharded cluster (Atlas always has one). The easiest way is `connection.transaction()`, which also retries on temporary errors.

```javascript
await mongoose.connection.transaction(async (session) => {
  const from = await Account.findById(fromId).session(session);
  const to = await Account.findById(toId).session(session);

  from.balance -= amount;
  to.balance += amount;

  await from.save(); // uses the session the doc was loaded with
  await to.save();
});
```

Every operation in the transaction must use the session, or it runs outside the transaction.

### 229: How do you pass a session to different operations?

```javascript
const session = await mongoose.startSession();
try {
  await session.withTransaction(async () => {
    await Order.create([{ customer, total }], { session });
    await Product.updateOne(
      { _id: productId },
      { $inc: { stock: -1 } },
      { session },
    );
    await Log.insertMany([{ msg: "order" }], { session });
  });
} finally {
  await session.endSession();
}
```

Note that `create()` needs an array when you pass options. Queries can also use `.session(session)`.

### 230: What is transactionAsyncLocalStorage?

It is a Mongoose option that uses Node's `AsyncLocalStorage` to pass the session to every operation inside `connection.transaction()` for you. Then you do not have to add `{ session }` to each call.

```javascript
mongoose.set("transactionAsyncLocalStorage", true);

await mongoose.connection.transaction(async () => {
  await Order.create({ customer, total }); // in the transaction
  await Product.updateOne({ _id: productId }, { $inc: { stock: -1 } }); // in the transaction
});
```

It only works with `connection.transaction()`, not with `session.withTransaction()`.

### 231: What is the difference between connection.transaction() and session.withTransaction()?

Both retry the callback on transient errors. `connection.transaction()` is a Mongoose helper that also resets document state if the transaction is aborted and retried, for example `isNew` and modified paths. With `session.withTransaction()` (from the driver), a retry may see documents that think they are already saved. Prefer `connection.transaction()` when you use documents and `save()`.

### 232: How do you read from secondaries?

Set the read preference on the connection, schema or query.

```javascript
await Report.find().read("secondaryPreferred");

new Schema({}, { read: "secondaryPreferred" });

mongoose.connect(uri, { readPreference: "secondaryPreferred" });
```

Reads from secondaries can be a bit behind the primary, so do not use them for data the user just wrote.

### 233: How do you set the write concern?

In the connection string, connection options, schema options or per operation.

```javascript
await Payment.create([{ amount: 100 }], {
  writeConcern: { w: "majority", j: true },
});

new Schema({}, { writeConcern: { w: "majority" } });
```

`w: 'majority'` waits until most members of the replica set have the write. It is the default in recent MongoDB versions.

### 234: How do you watch for changes in a collection?

Use `Model.watch()`. It opens a change stream (needs a replica set).

```javascript
const stream = Order.watch([{ $match: { operationType: "insert" } }], {
  fullDocument: "updateLookup",
});

stream.on("change", (change) => {
  console.log("New order", change.fullDocument._id);
});
```

The documents in change events are plain objects. Save the resume token (`change._id`) if you need to continue after a restart.

### 235: What is optimistic concurrency in Mongoose?

With `optimisticConcurrency: true`, every `save()` checks that `__v` in the database still matches the document's `__v`, and increments it. If someone else saved the document in between, you get a `VersionError`.

```javascript
const productSchema = new Schema(
  { name: String, stock: Number },
  { optimisticConcurrency: true },
);

const a = await Product.findById(id);
const b = await Product.findById(id);
a.stock = 5;
await a.save();
b.stock = 7;
await b.save(); // VersionError
```

Without this option, Mongoose only checks the version for some array changes.

### 236: When does Mongoose increment __v without optimisticConcurrency?

Only when you change an array in a way that can conflict with other writes, like replacing the whole array or using `splice()`, or setting an array item by index. Normal `$set` on scalar fields and `$push`/`$pull` do not increment `__v`.

This is why default versioning protects against "I changed item 2 but someone removed item 1 in the meantime", and not against two people changing the same name.

### 237: How do you do cursor-based pagination?

Use the last seen value instead of `skip()`. It stays fast on large collections.

```javascript
async function getPage(after, limit = 20) {
  const filter = after ? { _id: { $lt: after } } : {};
  const items = await Post.find(filter)
    .sort({ _id: -1 })
    .limit(limit + 1)
    .lean();
  const hasMore = items.length > limit;
  if (hasMore) items.pop();
  return { items, next: hasMore ? items.at(-1)._id : null };
}
```

`skip(100000)` makes MongoDB walk past 100,000 entries, which gets slow.

### 238: How do you sort and paginate on a non-unique field?

Add `_id` as a tie breaker, and use both in the cursor.

```javascript
const filter = last
  ? {
      $or: [
        { createdAt: { $lt: last.createdAt } },
        { createdAt: last.createdAt, _id: { $lt: last._id } },
      ],
    }
  : {};

const items = await Post.find(filter)
  .sort({ createdAt: -1, _id: -1 })
  .limit(20);
```

Add an index on `{ createdAt: -1, _id: -1 }` too.

### 239: What does strict: 'throw' do and when is it useful?

It throws a `StrictModeError` when you set a field that is not in the schema, instead of silently ignoring it.

```javascript
const schema = new Schema({ name: String }, { strict: "throw" });
new Model({ name: "a", nmae: "typo" }); // throws
```

It helps catch typos and makes bad API input fail loudly. Some teams prefer to validate input before it reaches Mongoose instead.

### 240: What does Model.castObject() do?

It casts a plain object to the schema types without creating a document or running validation.

```javascript
const raw = { price: "12", createdAt: "2026-01-01" };
const casted = Product.castObject(raw);
// { price: 12, createdAt: Date }
```

It is useful when you build data for `bulkWrite()` or for the driver directly.

### 241: What does Model.hydrate() do?

`hydrate()` turns a plain object (for example from an aggregation or a cache) into a Mongoose document, without saving.

```javascript
const [raw] = await User.aggregate([{ $match: { _id: id } }]);
const user = User.hydrate(raw);
user.name = "New name";
await user.save(); // sends only the change
```

The object is treated as already in the database (`isNew` is false).

### 242: How do you set global options in Mongoose?

Use `mongoose.set()` before creating models.

```javascript
mongoose.set("strictQuery", true);
mongoose.set("runValidators", true);
mongoose.set("sanitizeFilter", true);
mongoose.set("toJSON", { virtuals: true });
mongoose.set("returnDocument", "after");
```

`returnDocument` as a global option was added in Mongoose 9.2. Some options (like `toJSON`) only apply to schemas created after you set them.

### 243: How do you use Mongoose in NestJS?

Use the `@nestjs/mongoose` package. You define schemas with decorators and inject models.

```typescript
@Schema({ timestamps: true })
export class Cat {
  @Prop({ required: true })
  name: string;

  @Prop()
  age: number;
}
export const CatSchema = SchemaFactory.createForClass(Cat);

@Module({
  imports: [
    MongooseModule.forRoot(process.env.MONGODB_URI),
    MongooseModule.forFeature([{ name: Cat.name, schema: CatSchema }]),
  ],
})
export class CatsModule {}

@Injectable()
export class CatsService {
  constructor(@InjectModel(Cat.name) private catModel: Model<Cat>) {}
  findAll() {
    return this.catModel.find().lean();
  }
}
```

### 244: How do you use Mongoose in Next.js or serverless functions?

Cache the connection on `globalThis`, so each warm function call reuses it instead of opening a new pool.

```javascript
import mongoose from "mongoose";

const cached =
  globalThis.mongoose ?? (globalThis.mongoose = { conn: null, promise: null });

export async function connectDb() {
  if (cached.conn) return cached.conn;
  cached.promise ??= mongoose.connect(process.env.MONGODB_URI, {
    maxPoolSize: 5,
  });
  cached.conn = await cached.promise;
  return cached.conn;
}
```

Also use `mongoose.models.X || mongoose.model(...)` to avoid `OverwriteModelError` on hot reload.

### 245: What does recompileSchema() do?

Normally, changes to a schema after `mongoose.model()` is called are ignored. `Model.recompileSchema()` applies them, for example when a plugin adds fields after the model is created.

```javascript
const User = mongoose.model("User", userSchema);
userSchema.add({ nickname: String });
User.recompileSchema();
```

It is rarely needed. Usually you just finish the schema before compiling.

### 246: What does Model.applyTimestamps() do?

It sets `createdAt` and `updatedAt` on a plain object (including subdocuments) the same way Mongoose would. It is useful when you insert data through the driver or `bulkWrite()` and still want timestamps.

```javascript
const obj = { name: "Pen" };
Product.applyTimestamps(obj);
await Product.collection.insertOne(obj);
```

### 247: What is doc.$locals for?

`$locals` is a place to store temporary data on a document. It is not saved and not included in `toJSON()`. It is useful for passing data from a pre hook to a post hook.

```javascript
userSchema.pre("save", function () {
  this.$locals.wasNew = this.isNew;
});

userSchema.post("save", async function (doc) {
  if (doc.$locals.wasNew) {
    await sendWelcomeEmail(doc.email);
  }
});
```

### 248: How can a pre save hook tell which fields changed?

Use `isModified()`, `modifiedPaths()` or `directModifiedPaths()`. For the old value, you need to store it yourself, because Mongoose does not keep it by default.

```javascript
userSchema.post("init", function () {
  this.$locals.originalEmail = this.email;
});

userSchema.pre("save", async function () {
  if (this.isModified("email")) {
    await logEmailChange(this.$locals.originalEmail, this.email);
  }
});
```

`init` hooks are synchronous, so do not make them `async`.

### 249: How do you make orFail() throw your own error?

Pass an error or a function that returns one.

```javascript
class NotFoundError extends Error {
  status = 404;
}

const user = await User.findById(id).orFail(
  () => new NotFoundError("User not found"),
);
```

Your error middleware can then send `err.status`.

### 250: What is the difference between exists() and findOne() for checks?

`exists()` returns `{ _id }` or `null`, and Mongoose adds a projection so only `_id` comes back. `findOne()` loads the whole document and builds a Mongoose document. For "does this exist" checks, `exists()` is cheaper, and with a covering index it can be answered from the index alone.

### 251: How do you migrate pre hooks from Mongoose 8 to 9?

Remove the `next` argument, make the function `async`, and replace `next(err)` with `throw err`.

```javascript
// Mongoose 8
schema.pre("save", function (next) {
  if (!this.slug) return next(new Error("slug required"));
  next();
});

// Mongoose 9
schema.pre("save", async function () {
  if (!this.slug) throw new Error("slug required");
});
```

Check plugins from npm too. Old plugins that call `next()` break in Mongoose 9.

### 252: What else breaks when you upgrade from Mongoose 8 to 9?

- Node.js 20.19+ is required.
- Pre middleware has no `next()`, and `isAsync` hooks are gone.
- Update pipelines throw unless `updatePipeline: true`.
- `new` and `returnOriginal` are deprecated (since 9.2) in favor of `returnDocument`.
- `isValidObjectId()` returns `false` for numbers.
- UUID fields return `bson.UUID` objects, not strings.
- The `background` index option is no longer supported.
- `doc.updateOne()` no longer accepts a callback.
- Hooks on custom methods and statics need those methods to return promises.
- TypeScript filter and `create()` types are stricter.

### 253: What was removed in Mongoose 7 and 8 that old tutorials still use?

- Callbacks on model and query methods (removed in 7).
- `doc.remove()` and `Model.remove()` (removed in 7, use `deleteOne()`/`deleteMany()`).
- `Model.count()` (removed in 8, use `countDocuments()` or `estimatedDocumentCount()`).
- `findOneAndRemove()` and `findByIdAndRemove()` (removed in 8, use `findOneAndDelete()`).
- `rawResult` (removed in 8, use `includeResultMetadata`).
- Options like `useNewUrlParser`, `useUnifiedTopology`, `useFindAndModify` and `useCreateIndex`, which do nothing now.

### 254: How do you return Decimal128 values as numbers or strings in JSON?

Add a getter and turn getters on for `toJSON`.

```javascript
const productSchema = new Schema(
  {
    price: {
      type: Schema.Types.Decimal128,
      get: (v) => (v == null ? v : v.toString()),
    },
  },
  { toJSON: { getters: true } },
);
```

Using `parseFloat()` in the getter gives numbers but can lose precision. For money, a string is safer.

### 255: How do you query a date range for a single day?

Use `$gte` the start of the day and `$lt` the start of the next day. Be clear about the time zone, because dates are stored in UTC.

```javascript
const start = new Date("2026-10-24T00:00:00Z");
const end = new Date("2026-10-25T00:00:00Z");

const orders = await Order.find({ createdAt: { $gte: start, $lt: end } });
```

If your users are in another time zone, compute the start and end in their zone before converting to UTC.

### 256: How do you search safely with user input in a regex?

Escape special regex characters, and limit the input length.

```javascript
function escapeRegex(text) {
  return text.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

const q = String(req.query.q ?? "").slice(0, 50);
const users = await User.find({
  name: new RegExp("^" + escapeRegex(q), "i"),
}).limit(20);
```

Without escaping, a user can send a heavy pattern that makes the query very slow.

### 257: How do you make a case-insensitive unique field?

Two common ways:

1. Store it in lowercase with `lowercase: true` and a normal unique index. Simple and works well for emails.
2. Use a unique index with a case-insensitive collation:

```javascript
userSchema.index(
  { username: 1 },
  { unique: true, collation: { locale: "en", strength: 2 } },
);
```

With option 2, queries must use the same collation to use the index.

### 258: How do you find slow queries in a Mongoose app?

- Turn on `mongoose.set('debug', fn)` and log query time in development.
- Use the MongoDB profiler or Atlas Query Profiler / Performance Advisor.
- Run `.explain('executionStats')` on suspect queries and compare `totalDocsExamined` to `nReturned`.
- Use APM tools. The driver emits command monitoring events (`monitorCommands: true`), and Mongoose 9 added Node.js `TracingChannel` support for APM tools.

### 259: Why can duplicates get in even with unique: true?

Common reasons:

- The unique index was never built (for example `autoIndex: false` and no migration).
- The index build failed because duplicates already existed.
- Tests inserted data before the index finished building.
- The field was added to `unique` later, but the old non-unique index still exists with the same key.

Check with `Model.listIndexes()` or `diffIndexes()`.

### 260: What does Model.listIndexes() return?

The indexes that exist in MongoDB right now for the collection.

```javascript
const indexes = await User.listIndexes();
// [{ v: 2, key: { _id: 1 }, name: '_id_' }, { key: { email: 1 }, name: 'email_1', unique: true }]
```

`schema.indexes()` gives the indexes the schema defines. Comparing both tells you what is missing.

### 261: How do you add a TTL to a document that expires at a specific time?

Store the expiry time and set `expires: 0`. Each document then expires at its own date.

```javascript
const inviteSchema = new Schema({
  email: String,
  expireAt: { type: Date, required: true, expires: 0 },
});

await Invite.create({
  email,
  expireAt: new Date(Date.now() + 48 * 3600 * 1000),
});
```

### 262: How do you exclude deleted or private fields from populate()?

Use `select` with `-` in populate.

```javascript
await Post.find().populate({ path: "author", select: "-password -email -__v" });
```

`select: false` fields in the related schema are also excluded from population by default.

### 263: How do you sort by a field of a populated document?

You cannot sort the parent query by a populated field, because the population happens after the main query. Use an aggregation with `$lookup` and `$sort`, or store (denormalize) the field you need on the parent.

```javascript
await Post.aggregate([
  {
    $lookup: {
      from: "users",
      localField: "author",
      foreignField: "_id",
      as: "author",
    },
  },
  { $unwind: "$author" },
  { $sort: { "author.name": 1 } },
]);
```

### 264: How do you filter parents by a field of a referenced document?

Same problem as sorting. Options:

1. Two queries: find the matching ids first, then filter.

```javascript
const authorIds = await User.find({ country: "DE" }).distinct("_id");
const posts = await Post.find({ author: { $in: authorIds } });
```

2. An aggregation with `$lookup` and `$match`.
3. Denormalize the field onto the parent.

Using `populate({ match })` does not remove parents, it only sets the populated field to `null`.

### 265: How do you count related documents for many parents at once?

Use one aggregation instead of a `countDocuments()` per parent.

```javascript
const counts = await Comment.aggregate([
  { $match: { post: { $in: postIds } } },
  { $group: { _id: "$post", count: { $sum: 1 } } },
]);

const byPost = new Map(counts.map((c) => [c._id.toString(), c.count]));
```

Virtual populate with `count: true` is another option.

### 266: How do you keep an array of ids in sync on both sides?

Update both sides, ideally in a transaction.

```javascript
await mongoose.connection.transaction(async (session) => {
  await Student.updateOne(
    { _id: studentId },
    { $addToSet: { courses: courseId } },
    { session },
  );
  await Course.updateOne(
    { _id: courseId },
    { $addToSet: { students: studentId } },
    { session },
  );
});
```

Often it is simpler to store the link only on one side and use virtual populate for the other.

### 267: How do you rename a field in existing documents?

Use `$rename` in an `updateMany()`, then change the schema.

```javascript
await User.collection.updateMany(
  { fullname: { $exists: true } },
  { $rename: { fullname: "fullName" } },
);
```

Running it on `User.collection` (the driver) means Mongoose does not cast or strip anything from the update, which is what you want for a one-time migration. Deploy code that can read both names first, or do the rename in a maintenance window.

### 268: How do you write a data migration with Mongoose?

Use a migration tool (like `migrate-mongo` or a small script runner) and keep scripts in git. Inside the script:

- use `updateMany()` or `bulkWrite()` for simple changes
- use a cursor with `eachAsync()` and `bulkWrite()` batches for complex ones
- keep the script safe to run twice

```javascript
await User.find({ displayName: { $exists: false } })
  .cursor()
  .eachAsync(
    async (users) => {
      await User.bulkWrite(
        users.map((u) => ({
          updateOne: {
            filter: { _id: u._id },
            update: { $set: { displayName: u.name } },
          },
        })),
      );
    },
    { batchSize: 500 },
  );
```

### 269: What is the difference between deleteOne() on a query and on a document?

`Model.deleteOne(filter)` sends a delete straight to MongoDB and runs **query** middleware. `doc.deleteOne()` deletes that document by `_id` and runs **document** middleware (if registered with `{ document: true }`). Cascading deletes are usually written as document middleware, so they only run when you go through a loaded document.

### 270: How do you cascade deletes?

Mongoose does not do it for you. Write middleware or do it in your service code.

```javascript
postSchema.pre(
  "deleteOne",
  { document: true, query: false },
  async function () {
    await Comment.deleteMany({ post: this._id });
  },
);

postSchema.pre("findOneAndDelete", async function () {
  const post = await this.model.findOne(this.getFilter()).select("_id").lean();
  if (post) await Comment.deleteMany({ post: post._id });
});
```

For data that must stay consistent, run both deletes in a transaction.

### 271: How do you make default values depend on other fields?

Use a function default. `this` is the document.

```javascript
const userSchema = new Schema({
  name: String,
  slug: {
    type: String,
    default: function () {
      return this.name?.toLowerCase().replace(/\s+/g, "-");
    },
  },
});
```

Defaults are applied in the order the fields are defined in the schema, so `name` must come before `slug`.

### 272: What is the timestamps option for subdocuments?

You can turn on `timestamps` in a subdocument schema. Each subdocument then gets its own `createdAt` and `updatedAt`.

```javascript
const commentSchema = new Schema({ text: String }, { timestamps: true });
const postSchema = new Schema(
  { comments: [commentSchema] },
  { timestamps: true },
);
```

When you push a new comment and save, only that comment gets new timestamps, plus the post's `updatedAt`.

### 273: How do you limit the size of an array with $push?

Use `$each` with `$slice`.

```javascript
await User.updateOne(
  { _id: id },
  { $push: { recentSearches: { $each: [term], $position: 0, $slice: 10 } } },
);
```

This keeps only the 10 newest items. It is a good way to avoid unbounded arrays.

### 274: How do you get only matching array elements back?

Use the `$elemMatch` projection or the positional `$` projection.

```javascript
await Order.findOne(
  { _id: id },
  { items: { $elemMatch: { status: "returned" } } },
);
```

Both return only the first matching element. For all matches, use an aggregation with `$filter`.

### 275: How do you return a single field from many documents?

Use `distinct()` for unique values, or select the field with `lean()`.

```javascript
const emails = (
  await User.find({ active: true }).select("email -_id").lean()
).map((u) => u.email);
```

### 276: How do you run raw MongoDB commands through Mongoose?

Use the driver objects that Mongoose exposes.

```javascript
const db = mongoose.connection.db;
const stats = await db.command({ dbStats: 1 });

const result = await mongoose.connection.db.admin().ping();
```

These skip all Mongoose features (casting, hooks, validation).

### 277: How do you make sure the app does not start before the database is ready?

Await `mongoose.connect()` before calling `app.listen()`, and fail fast if it rejects.

```javascript
try {
  await mongoose.connect(process.env.MONGODB_URI, {
    serverSelectionTimeoutMS: 5000,
  });
} catch (err) {
  console.error("Database not reachable", err);
  process.exit(1);
}
app.listen(3000);
```

In Kubernetes, a readiness probe that checks `readyState === 1` keeps traffic away while the database is down.

### 278: What does bufferCommands: false do and when do you want it?

With buffering off, model calls fail right away if there is no connection, instead of waiting up to `bufferTimeoutMS`.

```javascript
mongoose.set("bufferCommands", false);
```

This is useful in serverless code and APIs where you prefer a quick error over a request that hangs for 10 seconds. You then must make sure you connect before using models.

### 279: How do you use Mongoose with Zod or another validation library?

Validate the request body with Zod at the API edge, then pass the clean data to Mongoose. Keep Mongoose validators for rules that protect the data itself (required fields, enums, ranges).

```javascript
const CreateUser = z.object({
  name: z.string().min(1),
  email: z.string().email(),
});

app.post("/users", async (req, res) => {
  const data = CreateUser.parse(req.body);
  const user = await User.create(data);
  res.status(201).json(user);
});
```

Mongoose 9 also lets you use a model as a Standard Schema validator through `Model['~standard']`, so libraries that accept Standard Schema can validate data with your Mongoose schema.

### 280: How do you get the schema as JSON Schema?

Mongoose 8.x added `schema.toJSONSchema()`.

```javascript
const jsonSchema = userSchema.toJSONSchema();
```

You can use the result for MongoDB `$jsonSchema` validation, or for API docs.

### 281: How do you add MongoDB-level schema validation with Mongoose?

Mongoose validation only runs in your app. To protect against writes from other tools, add a `$jsonSchema` validator to the collection. You can create it with `createCollection()` options:

```javascript
await mongoose.connection.createCollection("users", {
  validator: { $jsonSchema: userSchema.toJSONSchema() },
});
```

Or run `collMod` with the driver on an existing collection.

### 282: What is the difference between Model.find() with lean() and Model.collection.find()?

Both return plain objects, but `lean()` still goes through Mongoose: the filter is cast, query middleware runs, `select: false` fields are hidden, and `populate()` works. `Model.collection.find()` goes straight to the driver with none of that.

### 283: How do you protect against an empty filter in deleteMany() or updateMany()?

An empty filter `{}` matches every document. This can happen by mistake, for example when a filter is built from request data and every field is missing, or when `strictQuery: true` strips a field name with a typo.

Recent Mongoose versions have a `requireFilter` option for delete and update methods. With it, an empty filter throws an error instead of touching every document.

```javascript
await User.deleteMany(filter, { requireFilter: true });
// MongooseError: Empty or invalid filter not allowed with requireFilter enabled
```

It is still a good habit to check input before you build filters for writes.

### 284: How do you use findOneAndUpdate() to create or increment a counter?

A common pattern for sequence numbers:

```javascript
const counterSchema = new Schema({
  _id: String,
  seq: { type: Number, default: 0 },
});
const Counter = mongoose.model("Counter", counterSchema);

async function nextInvoiceNumber() {
  const c = await Counter.findOneAndUpdate(
    { _id: "invoice" },
    { $inc: { seq: 1 } },
    { upsert: true, returnDocument: "after" },
  );
  return c.seq;
}
```

The update is atomic, so two requests never get the same number.

### 285: How do you add a field to all existing documents with a default?

Mongoose applies defaults only in memory when loading old documents. To store the default, run an update:

```javascript
await User.updateMany({ plan: { $exists: false } }, { $set: { plan: "free" } });
```

### 286: How does Mongoose cast the _id in populate()?

`populate()` collects all ids from the parents and runs one query like `{ _id: { $in: ids } }` on the related model, then matches the results back to each parent by id. The ids are cast using the related schema's `_id` type, so string ids work too.

### 287: How do you use the same schema in several models?

You can pass the same schema to several `model()` calls, but they share hooks and options. If you need small differences, clone it.

```javascript
const archiveSchema = orderSchema.clone();
archiveSchema.set("collection", "orders_archive");
const OrderArchive = mongoose.model("OrderArchive", archiveSchema);
```

### 288: How do you set options on a query?

Use `setOptions()` or pass them as the third argument.

```javascript
await User.find({ active: true }).setOptions({ lean: true, maxTimeMS: 2000 });
await User.find({ active: true }, null, { sort: { name: 1 }, limit: 10 });
```

`maxTimeMS` tells MongoDB to stop the query after that many milliseconds.

### 289: How do you set a query timeout?

Use `maxTimeMS()`.

```javascript
await Report.find(filter).maxTimeMS(5000);
await Report.aggregate(pipeline).option({ maxTimeMS: 5000 });
```

MongoDB stops the operation and returns an error after the time limit. This protects the database from runaway queries.

### 290: How do you get the filter, update and options from a query object?

```javascript
const q = User.findOneAndUpdate(
  { email },
  { $set: { name } },
  { returnDocument: "after" },
);

q.getFilter(); // { email: '...' }
q.getUpdate(); // { $set: { name: '...' } }
q.getOptions(); // { returnDocument: 'after' }
q.op; // 'findOneAndUpdate'
q.model; // the model
```

These are mostly used in query middleware.

### 291: How do you use Map fields in queries?

Use dot notation with the key.

```javascript
const productSchema = new Schema({ attrs: { type: Map, of: String } });

await Product.find({ "attrs.color": "red" });
await Product.updateOne({ _id: id }, { $set: { "attrs.size": "L" } });
```

In JSON output, Maps become plain objects (with `flattenMaps`, which is on by default for `toJSON()`).

### 292: What is the init hook?

`init` runs when Mongoose loads a document from the database (after `find()` and similar). It is synchronous, so it cannot be `async`.

```javascript
schema.post("init", function (doc) {
  doc.$locals.loadedAt = new Date();
});
```

It is useful for saving original values to compare later.

### 293: How do you skip middleware for one operation?

Mongoose 9 added the `middleware` option.

```javascript
await doc.save({ middleware: false });
await User.updateOne(
  { _id: id },
  { $set: { name: "x" } },
  { middleware: false },
);
```

You can also skip only pre or only post hooks. Use it for scripts and bulk jobs where the hooks are not needed.

### 294: How do you use a Mongoose document with session after loading it?

A document loaded with `.session(session)` remembers it, and `save()` uses it. You can also set it later:

```javascript
const user = await User.findById(id);
user.$session(session);
await user.save(); // runs in the session
```

Be careful not to keep using the session after the transaction ends.

### 295: What is the difference between Model.validate() and doc.validate()?

`doc.validate()` validates a document. `Model.validate(obj, paths)` casts and validates a plain object against the schema without creating a document, and returns the cast object.

```javascript
const clean = await User.validate({ name: "Anna", age: "30" });
// clean.age === 30
```

### 296: What does the schema option id: false change?

It removes the `id` virtual. This is useful if your data has its own `id` field or you do not want `id` in JSON output. If the schema already has an `id` field, Mongoose does not add the virtual anyway.

### 297: How do you return the document's id as "id" instead of "_id" in API responses?

Use a `toJSON` transform.

```javascript
const schema = new Schema(
  { name: String },
  {
    toJSON: {
      virtuals: true,
      versionKey: false,
      transform(doc, ret) {
        delete ret._id;
        return ret;
      },
    },
  },
);
```

With `virtuals: true`, the `id` virtual is included. Then you remove `_id`.

### 298: How do you handle an upsert race that causes a duplicate key error?

Two upserts at the same time can both try to insert. With a unique index, one fails with `11000`. The usual fix is to retry once, because the second try will find the document.

```javascript
async function upsertUser(email, data) {
  try {
    return await User.findOneAndUpdate({ email }, data, {
      upsert: true,
      returnDocument: "after",
    });
  } catch (err) {
    if (err.code !== 11000) throw err;
    return User.findOneAndUpdate({ email }, data, { returnDocument: "after" });
  }
}
```

Without a unique index, both inserts succeed and you get two documents.

### 299: How do you log every write to an audit collection?

Use post hooks for save and the update/delete queries.

```javascript
function audit(schema) {
  schema.post("save", async function (doc) {
    await AuditLog.create({
      model: doc.constructor.modelName,
      docId: doc._id,
      op: "save",
    });
  });
  schema.post(
    ["updateOne", "findOneAndUpdate", "deleteOne"],
    async function () {
      await AuditLog.create({
        model: this.model.modelName,
        filter: this.getFilter(),
        op: this.op,
      });
    },
  );
}

mongoose.plugin(audit);
```

Make sure the `AuditLog` model itself does not get the plugin, or it will log itself forever.

### 300: How do you choose between Mongoose and Prisma for MongoDB?

Mongoose is made only for MongoDB. It supports all MongoDB features, middleware, discriminators and flexible schemas, and is the most common choice in Node.js MongoDB projects. Prisma supports MongoDB too, but has fewer MongoDB-specific features, needs a replica set for some operations, and uses a generated client with its own schema file. Pick Mongoose when you depend on MongoDB features. Pick Prisma when the team already uses it with SQL databases and wants the same tool.

## Advanced Questions (301-450)

### 301: How does Mongoose track changes on a document?

Every document keeps internal state about which paths were changed since it was loaded. When you set a value through a setter (`doc.name = 'x'` or `doc.set()`), Mongoose casts it and marks the path as modified. Arrays are special `MongooseArray` objects that record which operations you did on them (push, pull and so on).

When you call `save()`, Mongoose reads this state, builds an update with only the changed paths, sends it, and then clears the state. This is why changes Mongoose cannot see (like changes inside `Mixed` or `Date.setMonth()`) need `markModified()`.

### 302: What update does save() actually send for a changed document?

It sends `updateOne({ _id, [versionKey if needed] }, delta)`, where `delta` is built from the modified paths.

```javascript
const user = await User.findById(id);
user.name = "Anna";
user.tags.push("a", "b");
user.address.city = "Berlin";
await user.save();
// users.updateOne(
//   { _id: ... },
//   { $set: { name: 'Anna', 'address.city': 'Berlin' }, $push: { tags: { $each: ['a', 'b'] } } }
// )
```

With `debug` on you can see this. If nothing changed, `save()` sends nothing, but still runs middleware.

### 303: What are atomic array operations in Mongoose?

When you call `push()`, `pull()`, `addToSet()` or `pop()` on a `MongooseArray`, Mongoose remembers the operation instead of just the new array. On `save()` it sends `$push`, `$pullAll`, `$addToSet` or `$pop`, so two processes changing the same array do not overwrite each other.

If you mix operations that cannot be combined in one update (like `push()` and then `pull()` on the same array), or you replace the array or set an item by index, Mongoose falls back to `$set` of the whole array and increments `__v`.

### 304: Why can setting an array item by index cause a VersionError?

```javascript
const post = await Post.findById(id);
post.comments[2].text = "edited"; // fine, subdoc path
post.tags[1] = "new"; // $set 'tags.1'
await post.save();
```

When you set `tags.1`, Mongoose adds the version to the filter, because position 1 might point to a different item if someone else changed the array in the meantime. If `__v` in the database no longer matches, MongoDB finds no document and Mongoose throws `VersionError`. The fix is to reload and retry, or use `$pull`/`$push` or update by a stable key (like `_id` of a subdoc).

### 305: How does the Mongoose middleware system work internally?

Mongoose uses a small library called `kareem` for hooks. Each schema has a hooks object with pre and post lists per operation name. When you call a hooked method (like `save()`), Mongoose runs all pre hooks in order, then the real method, then post hooks. If a pre hook throws or rejects, the method does not run and error handling post hooks get the error.

Because the hooks are copied from the schema when the model is compiled, hooks added after `mongoose.model()` have no effect.

### 306: How are Mongoose queries built and executed?

`Model.find()` creates a `Query` object (based on the `mquery` library). Chain calls only change its internal filter, projection, options and update. Nothing is sent until you call `exec()` (directly or through `then()`). On exec, Mongoose:

1. runs pre query middleware
2. casts the filter and update using the schema
3. applies schema options (like `select: false`, `strictQuery`, `sanitizeFilter`)
4. calls the driver
5. builds documents from the results (unless `lean`)
6. runs `populate()` queries
7. runs post middleware

### 307: How expensive is building Mongoose documents compared to lean?

Building a document means creating an object with internal state, running getters, applying defaults, building `MongooseArray`s and subdocuments, and running `init` hooks. For large result sets this can take more time and memory than the database query itself. Lean results skip all of that, so they are often several times faster and use much less memory.

A rule of thumb: use full documents when you will change and save them, use `lean()` for reading and sending to the client.

### 308: What do you lose with lean() and how do you get some of it back?

You lose:

- virtuals (`mongoose-lean-virtuals` or `Model.applyVirtuals()`)
- getters (`mongoose-lean-getters`)
- defaults for missing fields (`mongoose-lean-defaults`)
- document methods like `save()` and `isModified()`
- `toJSON` transforms
- automatic casting on later changes

What you keep: casting of the filter, query middleware, `select: false` handling and `populate()`. If you need a document later, `Model.hydrate(obj)` builds one from a lean object.

### 309: How does populate() work internally and what is its cost?

After the main query returns, Mongoose collects all ids from the populated path, removes duplicates, and runs one query on the related model with `{ _id: { $in: ids } }`. Then it maps results back to each parent in memory. Each populated path (and each nested level) adds one more round trip.

The costs to watch are: the extra round trips, a very large `$in` list when parents have many refs, and building documents for all related results. For large lists, select only needed fields and use `lean()`.

### 310: When should you use $lookup instead of populate()?

Use `$lookup` when:

- you need to filter or sort parents by fields of the related documents
- you need aggregation (counts, sums) over the joined data
- you want one round trip instead of several

Use `populate()` when:

- you just need related data attached to results
- you want Mongoose features on the related docs (casting, `select: false`, getters)
- related docs live on another connection or database

`$lookup` is not free either. Without an index on the foreign field it does a collection scan for each input document.

### 311: What is the N+1 problem in Mongoose and how do you avoid it?

N+1 happens when you load N documents and then run one more query per document.

```javascript
// Bad: 1 + N queries
const posts = await Post.find().lean();
for (const post of posts) {
  post.author = await User.findById(post.author).lean();
}

// Good: 2 queries
const posts2 = await Post.find().populate("author", "name").lean();
```

`populate()` batches the ids into one query. Also watch for `countDocuments()` or virtual populate inside loops, and use one aggregation with `$group` instead.

### 312: Why do large embedded arrays hurt performance?

Problems with large arrays:

- a document can be at most 16 MB
- every read loads the whole array unless you project it out
- updates may rewrite large parts of the document on disk
- multikey indexes on big arrays get large
- with Mongoose, building a document with thousands of subdocs is slow

If an array can grow without limit (comments, logs, events), store items in their own collection with a reference to the parent.

### 313: What is the bucket pattern and how would you model it in Mongoose?

The bucket pattern groups many small items (like sensor readings) into one document per time period, with a fixed size.

```javascript
const bucketSchema = new Schema({
  sensorId: { type: Schema.Types.ObjectId, index: true },
  start: Date,
  count: { type: Number, default: 0 },
  readings: [{ _id: false, t: Date, v: Number }],
});
bucketSchema.index({ sensorId: 1, start: 1 });

await Bucket.updateOne(
  { sensorId, count: { $lt: 200 } },
  {
    $push: { readings: { t: new Date(), v: 21.5 } },
    $inc: { count: 1 },
    $setOnInsert: { start: new Date() },
  },
  { upsert: true },
);
```

This cuts the number of documents and index entries a lot. For new projects, MongoDB time series collections (`timeseries` schema option) do this for you.

### 314: How do you use time series collections in Mongoose?

Use the `timeseries` schema option. Mongoose creates the collection with those settings.

```javascript
const metricSchema = new Schema(
  {
    timestamp: Date,
    meta: { host: String, region: String },
    cpu: Number,
  },
  {
    timeseries: {
      timeField: "timestamp",
      metaField: "meta",
      granularity: "minutes",
    },
    autoCreate: true,
    expireAfterSeconds: 60 * 60 * 24 * 30,
  },
);
```

The collection must be created as a time series collection. If it already exists as a normal collection, the option does nothing.

### 315: What is the subset pattern?

You store a small, often used part of related data inside the parent, and the full data in another collection. For example, a product stores its 10 newest reviews, while all reviews live in a `reviews` collection.

```javascript
await Review.create({ product: productId, text, rating });
await Product.updateOne(
  { _id: productId },
  {
    $push: {
      recentReviews: { $each: [{ text, rating }], $position: 0, $slice: 10 },
    },
  },
);
```

The product page needs one query, and the document stays small.

### 316: How do you keep denormalized data in sync?

When you copy a field (like the author's name) into other documents, you have to update the copies when the source changes. Options:

- update copies in the same service call, ideally in a transaction
- use a post hook on the source model
- use a change stream worker that listens for changes and updates copies
- accept short delays and rebuild with a background job

```javascript
userSchema.post("findOneAndUpdate", async function (doc) {
  if (doc && this.getUpdate().$set?.name) {
    await Post.updateMany(
      { "author._id": doc._id },
      { $set: { "author.name": doc.name } },
    );
  }
});
```

Only copy fields that change rarely.

### 317: How would you design a multi-tenant app with Mongoose?

Three common options:

1. **Shared collections with a `tenantId` field**. Simple and scales to many tenants. Add `tenantId` to every index and filter. A query middleware or a base repository can add the filter.
2. **Database per tenant** with `connection.useDb(name, { useCache: true })`. Better isolation and easy per-tenant backups, but many databases means many collections and indexes.
3. **Cluster per tenant** for large or regulated customers.

With option 1, the biggest risk is a query that forgets the tenant filter, so enforce it in one place and test it.

### 318: How do you enforce a tenant filter on every query?

Use `AsyncLocalStorage` to hold the current tenant and a global plugin that adds it.

```javascript
import { AsyncLocalStorage } from "node:async_hooks";
export const tenantStore = new AsyncLocalStorage();

function tenantPlugin(schema) {
  if (!schema.path("tenantId")) return;
  const addTenant = function () {
    const tenantId = tenantStore.getStore()?.tenantId;
    if (!tenantId) throw new Error("No tenant in context");
    this.where({ tenantId });
  };
  schema.pre(
    [
      "find",
      "findOne",
      "countDocuments",
      "updateOne",
      "updateMany",
      "deleteOne",
      "deleteMany",
      "findOneAndUpdate",
      "findOneAndDelete",
    ],
    addTenant,
  );
  schema.pre("aggregate", function () {
    this.pipeline().unshift({
      $match: { tenantId: tenantStore.getStore()?.tenantId },
    });
  });
}
mongoose.plugin(tenantPlugin);
```

Note that `$match` in the aggregate hook needs a real ObjectId if `tenantId` is an ObjectId, since aggregations are not cast.

### 319: What are the risks of useDb() with many tenants?

Each `useDb()` connection object keeps its own models. Without `useCache: true`, calling `useDb()` on every request creates new objects and leaks memory. Also every new model on a new database may try to build indexes (`autoIndex`), which can flood the server at startup. Use `useCache: true`, turn off `autoIndex`, and manage indexes per tenant with a script.

### 320: How do you size the connection pool?

Think about the total, not per instance: `instances × maxPoolSize` must stay under what the cluster can handle (Atlas tiers have connection limits). Start with the default or something like 10-50, then watch metrics:

- if requests wait for connections (`waitQueue`, high latency with low database load), raise it
- if the server has too many connections or high memory, lower it

Long-running queries hold sockets, so a few slow queries can block the pool. Fix the slow queries before making the pool bigger.

### 321: What problems does Mongoose have in serverless environments?

- Cold starts open new connections, so many cold starts at once can cause a connection storm.
- Functions can freeze between calls, leaving sockets in odd states.
- Each function instance has its own pool.
- Buffering can make a request hang until `bufferTimeoutMS`.
- `autoIndex` on every cold start creates load.

Fixes: cache the connection on `globalThis`, use small `maxPoolSize`, turn off `autoIndex` and `bufferCommands`, set short `serverSelectionTimeoutMS`, and consider a data API layer if the scale is very large.

### 322: How does Mongoose behave when the primary goes down?

The driver notices the primary is gone, waits for a new primary to be elected (usually a few seconds), and then sends operations there. During the election, writes fail or wait up to `serverSelectionTimeoutMS`. With retryable writes (on by default), most single writes are retried once after the new primary is found. Reads with `primary` read preference wait too.

For the app, this means a few seconds of slower or failing requests. Handle `MongooseServerSelectionError` and network errors with a clear 503 response rather than a crash.

### 323: What are retryable writes and when do they not help?

Retryable writes let the driver retry a single write once if it fails because of a network error or a primary change. They are on by default (`retryWrites=true`).

They do not cover:

- `updateMany()` and `deleteMany()` (multi-document writes)
- writes with `w: 0`
- errors that are not transient, like validation or duplicate key errors

`bulkWrite()` with only single-document operations can be retried.

### 324: How do transactions affect performance?

Transactions hold locks and keep a snapshot of the data until commit. Long or large transactions:

- increase memory use on the server (cache pressure)
- cause write conflicts (`WriteConflict`), which force retries
- fail if they run longer than `transactionLifetimeLimitSeconds` (60 seconds by default)

Keep transactions short, touch few documents, do not call slow external APIs inside them, and use them only when you really need several writes to succeed or fail together. Often a single document update with the right schema design is enough.

### 325: What is a TransientTransactionError and how do you handle it?

It is an error label on errors where the whole transaction can safely be retried, like write conflicts or a primary change. `connection.transaction()` and `session.withTransaction()` retry automatically when they see this label (and `UnknownTransactionCommitResult` for the commit).

If you write transactions by hand with `startTransaction()` and `commitTransaction()`, you must check `err.hasErrorLabel('TransientTransactionError')` and retry yourself.

### 326: Why should code inside a transaction be safe to run more than once?

Because the helpers retry the whole callback on transient errors. If the callback sends an email, calls a payment API or pushes to a queue, that side effect can happen two or three times. Do side effects after the transaction commits, or make them idempotent with a unique key.

```javascript
await mongoose.connection.transaction(async (session) => {
  await Order.create([{ _id: orderId, items, total }], { session });
  await Stock.updateOne({ sku }, { $inc: { qty: -1 } }, { session });
});
await sendConfirmationEmail(orderId); // after commit
```

### 327: What happens if you forget the session on one operation in a transaction?

That operation runs outside the transaction. It is committed right away, even if the transaction later aborts. It may also wait on locks held by the transaction, which can cause a write conflict or a deadlock-like timeout. With `transactionAsyncLocalStorage` on and `connection.transaction()`, Mongoose adds the session for you, which removes this class of bugs.

### 328: Why does populate() in a transaction sometimes fail, and what is the ordered option?

Inside a transaction, all operations share one session, and MongoDB does not allow running several operations in parallel on the same session in a transaction. Mongoose normally populates several paths in parallel. The `ordered: true` populate option (added in 8.x) runs them one after another.

```javascript
await Order.findById(id)
  .session(session)
  .populate({ path: "items.product", ordered: true });
```

### 329: How do read and write concerns combine for consistent reads?

For "read your own writes" across a replica set, use causal consistency: a session with `causalConsistency: true` (the default for explicit sessions), `readConcern: 'majority'` and `writeConcern: { w: 'majority' }`. Then a read in the same session, even on a secondary, waits until it sees your earlier writes.

```javascript
const session = await mongoose.startSession({ causalConsistency: true });
await User.updateOne(
  { _id: id },
  { name: "Anna" },
  { session, writeConcern: { w: "majority" } },
);
const user = await User.findById(id)
  .session(session)
  .read("secondary")
  .readConcern("majority");
```

Without a session, a secondary read may return old data.

### 330: What is snapshot read concern and when would you use it?

`readConcern: 'snapshot'` gives you a view of the data from one point in time across several reads. It is the read concern used inside transactions. Outside transactions, MongoDB 5.0+ supports snapshot reads for `find()` and `aggregate()` on a single query, which is useful for reports that must be consistent while data changes.

```javascript
await Order.aggregate(pipeline).option({ readConcern: { level: "snapshot" } });
```

### 331: How do you design indexes for Mongoose queries?

Follow the ESR rule for compound indexes: **E**quality fields first, then **S**ort fields, then **R**ange fields.

```javascript
// query: status = 'paid', sort by createdAt desc, total > 100
orderSchema.index({ status: 1, createdAt: -1, total: 1 });
```

Also:

- index every field used in common filters and as foreign keys for `populate()`/`$lookup`
- avoid too many indexes on write-heavy collections
- check with `explain()` that queries use the index you expect

### 332: What is a covered query and how does lean() help?

A covered query is answered from the index alone, without reading documents. The filter and projection must only use indexed fields, and `_id` must be excluded unless it is in the index.

```javascript
userSchema.index({ email: 1, name: 1 });

await User.find({ email: "anna@example.com" }).select("email name -_id").lean();
```

`lean()` does not make a query covered, but without it Mongoose builds documents and may add defaults, which hides the benefit. `explain()` shows `totalDocsExamined: 0` for a covered query.

### 333: How do you build indexes in production without downtime?

Since MongoDB 4.2, index builds use an optimized process that only locks the collection briefly at the start and end. Still, they use CPU, memory and disk on every node. Good practice:

- turn off `autoIndex` in production
- create indexes with a migration or script during low traffic
- watch replication lag during the build
- for very large collections, consider building on one node at a time (rolling build)

The old `background: true` option does nothing on modern MongoDB, and Mongoose 9 no longer supports it.

### 334: Why is syncIndexes() dangerous in production?

`syncIndexes()` drops every index that is not in the schema. If someone added an index by hand to fix a slow query, or two services share a collection with different schemas, `syncIndexes()` removes those indexes and queries suddenly slow down. Dropping and rebuilding a changed index also leaves a window without it.

Use `diffIndexes()` to see the plan first, and apply changes in a reviewed migration. Mongoose 8 added `hideIndexes` so you can hide indexes first instead of dropping them.

### 335: How do you change an index that already exists?

You usually cannot change an index in place. You create the new one, check queries use it, and then drop the old one.

```javascript
await Order.collection.createIndex(
  { customer: 1, createdAt: -1 },
  { name: "customer_createdAt" },
);
// deploy, check explain()
await Order.collection.dropIndex("customer_1");
```

For a safer switch, first hide the old index (`collMod` with `hidden: true`), watch performance, then drop it.

### 336: How do you detect duplicate or unused indexes?

- Mongoose prints a "Duplicate schema index" warning if you define the same index twice, for example with `unique: true` and `schema.index()` on the same field.
- Use `$indexStats` to see how often each index is used:

```javascript
const stats = await Order.aggregate([{ $indexStats: {} }]);
stats.forEach((s) => console.log(s.name, s.accesses.ops));
```

Indexes with zero ops over a long time are candidates for removal, after checking rare jobs like monthly reports.

### 337: What are partial indexes and how do you use them with Mongoose?

A partial index includes only documents that match a filter, so it is smaller and can enforce rules on a subset.

```javascript
// unique email only for users that are not deleted
userSchema.index(
  { email: 1 },
  { unique: true, partialFilterExpression: { isDeleted: false } },
);
```

Queries must include the same condition (`isDeleted: false`) for MongoDB to use a partial index. `partialFilterExpression` supports only some operators (equality, `$exists: true`, `$gt`/`$lt` style comparisons, `$type`, `$and`, and in newer versions `$or` and `$in`), so a simple boolean flag is the easiest thing to filter on.

### 338: How do you deal with soft delete and unique indexes?

A plain unique index on `email` blocks a new user from using the email of a soft-deleted user. Fixes:

- a partial unique index that only covers active documents (see previous question)
- or change the email on delete (for example `deleted_<id>_<email>`)
- or move deleted documents to an archive collection

Also remember that `find` hooks for soft delete do not cover `aggregate()`, `distinct()` or driver calls unless you add them.

### 339: What security problems can happen with Mongoose apps?

- **Query selector injection**: user input like `{ "$ne": null }` in filters.
- **Mass assignment**: `User.create(req.body)` lets a user set `role: 'admin'`.
- **Leaking fields**: returning whole documents with `password`, tokens or internal flags.
- **Regex DoS**: user-controlled regex patterns.
- **Unbounded queries**: no `limit()`, letting someone fetch millions of documents.
- **Prototype pollution** through crafted keys like `__proto__` (Mongoose has fixes for this, keep it updated).
- **Credentials in code** or in logs (debug mode printing data).

### 340: How do you prevent mass assignment with Mongoose?

Do not pass `req.body` straight to `create()` or `updateOne()`. Pick allowed fields, or validate with a schema library first.

```javascript
const { name, email } = req.body;
const user = await User.create({ name, email });

// or protect fields at schema level
const userSchema = new Schema({
  role: { type: String, default: "user", immutable: true },
});
```

`strict` mode only stops fields that are not in the schema. It does not stop a user from setting `role` if `role` is in the schema.

### 341: How do you encrypt fields with Mongoose?

Options:

1. **MongoDB Queryable Encryption / CSFLE**: the driver encrypts fields before sending them. Mongoose 8.x added support through the `encryptionType` schema option and `encrypt` on fields, with auto encryption configured on the connection. The server never sees plain values.
2. **App-level encryption** with setters/getters or hooks using Node's `crypto`. Simple, but you cannot query encrypted values except by exact match with deterministic encryption.

```javascript
const patientSchema = new Schema(
  {
    name: String,
    ssn: { type: String, encrypt: { keyId: [keyId], queries: "equality" } },
  },
  { encryptionType: "queryableEncryption" },
);
```

Key management (KMS) is the hard part in both cases.

### 342: How do you avoid leaking data in error messages and logs?

- Do not return raw Mongoose errors to clients. `CastError` and `ValidationError` messages include the bad value.
- Turn off `debug` in production, or log only collection names and timings, not the query values.
- Map `11000` errors to a generic "already exists" message. `err.keyValue` contains the value.
- Redact fields like `password` and `token` in log serializers.

### 343: How do you implement field-level access control?

Mongoose has no built-in roles, so you do it in code:

- define projections per role and apply them with `select()`
- use `toJSON` transforms with options passed from the request

```javascript
const fieldsByRole = {
  admin: "",
  user: "-email -lastLoginIp -internalNotes",
};

const users = await User.find().select(fieldsByRole[req.user.role]).lean();
```

Keep the rules in one place and test them. For writes, check which fields a role can change before building the update.

### 344: Why is it dangerous to use strictQuery: false with user-controlled keys?

With `strictQuery: false` (the default since Mongoose 7), unknown keys pass through to MongoDB. If you build a filter from user input like `User.find(req.query)`, a user can filter on any field, including hidden ones such as `resetToken`, and learn values by trying. Never pass `req.query` or `req.body` as a whole filter. Pick known fields and cast them.

### 345: How do custom schema types work?

You extend `mongoose.SchemaType` and implement `cast()`. Then register it on `mongoose.Schema.Types`.

```javascript
class Email extends mongoose.SchemaType {
  constructor(key, options) {
    super(key, options, "Email");
  }
  cast(val) {
    const s = String(val).trim().toLowerCase();
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(s)) {
      throw new Error(`Email: ${val} is not a valid email`);
    }
    return s;
  }
}
mongoose.Schema.Types.Email = Email;

const schema = new Schema({ contact: { type: Email } });
```

For query casting you can also implement `castForQuery()`. Most of the time setters and validators on a `String` are simpler.

### 346: How do you change the casting rules for built-in types?

Each schema type has a static `cast()` you can replace. For example, to stop Mongoose from casting numbers to strings:

```javascript
mongoose.Schema.Types.String.cast((v) => {
  if (typeof v !== "string") throw new Error("Must be a string");
  return v;
});

// or turn off casting for a type: only allow the exact type
mongoose.Schema.Types.Number.cast(false);
```

This is useful when silent casting (like `'1'` becoming `1`) hides bugs in input.

### 347: How do you set global getters or setters for a type?

Use the static `get()` or `set()` on the type.

```javascript
// trim all strings
mongoose.Schema.Types.String.set((v) => (typeof v === "string" ? v.trim() : v));

// return ObjectIds as strings everywhere
mongoose.Schema.Types.ObjectId.get((v) => (v == null ? v : v.toString()));
```

Be careful: a global getter on `ObjectId` changes `doc._id` to a string in your code, which can break `equals()` and other code that expects ObjectIds.

### 348: How do discriminators affect indexes and queries?

All discriminators share one collection, so indexes defined on a discriminator schema are created on the shared collection. Queries on a discriminator add `{ __t: 'Name' }`, so indexes for discriminator-specific queries should start with the discriminator key.

```javascript
clickSchema.index({ __t: 1, url: 1 });
```

Also, a unique index on a field from one discriminator applies to all documents in the collection. Use a partial index with `partialFilterExpression: { __t: 'Click' }` if it should only apply to one type.

### 349: Discriminators or separate collections: how do you choose?

Use discriminators when the types share most fields and you often query them together (like a feed of events, or different payment methods). Use separate collections when the types are mostly different, are queried alone, or grow at very different rates. Discriminators make "all types" queries easy but make indexes and schema changes affect everything in the collection.

### 350: How do you change the type of an existing document in a discriminator setup?

Mongoose does not let you just change `__t` with a normal update, because the update is cast with the current discriminator's schema. You can pass `overwriteDiscriminatorKey: true`:

```javascript
await Event.updateOne(
  { _id: id },
  { __t: "Signup", plan: "pro" },
  { overwriteDiscriminatorKey: true },
);
```

Or update through `Event.collection` and then clean up fields that do not belong to the new type.

### 351: How does Mongoose handle schemas that change over time?

MongoDB stores whatever was written, so old documents keep their old shape. Mongoose applies the current schema when loading: defaults fill missing fields in memory, unknown fields are kept in the document's raw data but not exposed as properties under strict mode, and casting may fail for old values of a different type.

Common approaches:

- add a `schemaVersion` field and migrate documents lazily on read or in a background job
- write migrations for breaking changes
- keep new fields optional until the migration is finished

### 352: How do you implement lazy schema migration on read?

Use a `schemaVersion` field and upgrade in a post `init` hook or a helper, then save when convenient.

```javascript
const CURRENT = 2;

userSchema.post("init", function (doc) {
  if ((doc.schemaVersion ?? 1) < 2) {
    doc.set(
      "fullName",
      `${doc.get("firstName", String)} ${doc.get("lastName", String)}`,
    );
    doc.schemaVersion = CURRENT;
    doc.$locals.needsSave = true;
  }
});
```

The upgraded data is saved the next time the document is saved. It keeps reads fast but means you live with two shapes for a while, and lean queries do not get the upgrade.

### 353: What is the strictRead option in Mongoose 9?

`strictRead` controls what happens to fields in stored documents that are not in the schema when Mongoose loads them. With `true` they are removed from the hydrated document, with `'throw'` loading fails. The default is `false`, which keeps them in the raw data. It helps find old fields that should have been migrated.

```javascript
new Schema({ name: String }, { strictRead: "throw" });
```

### 354: How do you handle the 16 MB document limit?

- Do not store files in documents. Use GridFS or object storage.
- Move unbounded arrays to their own collection.
- Use the bucket or subset pattern.
- Watch document sizes with `$bsonSize` in an aggregation:

```javascript
await Post.aggregate([
  { $project: { size: { $bsonSize: "$$ROOT" } } },
  { $sort: { size: -1 } },
  { $limit: 5 },
]);
```

### 355: How do you use GridFS with Mongoose?

Mongoose does not wrap GridFS, but you can use the driver's `GridFSBucket` with Mongoose's connection.

```javascript
import { GridFSBucket } from "mongodb";
import { pipeline } from "node:stream/promises";
import fs from "node:fs";

const bucket = new GridFSBucket(mongoose.connection.db, {
  bucketName: "uploads",
});

await pipeline(
  fs.createReadStream("./report.pdf"),
  bucket.openUploadStream("report.pdf"),
);
bucket.openDownloadStreamByName("report.pdf").pipe(res);
```

Store the file id on your Mongoose document if you need a link.

### 356: How do you handle very large exports without running out of memory?

Stream with a lean cursor and write as you go.

```javascript
import { Transform } from "node:stream";
import { pipeline } from "node:stream/promises";

const cursor = Order.find({ status: "paid" })
  .lean()
  .cursor({ batchSize: 1000 });

const toCsv = new Transform({
  objectMode: true,
  transform(doc, _, cb) {
    cb(null, `${doc._id},${doc.total},${doc.createdAt.toISOString()}\n`);
  },
});

res.setHeader("Content-Type", "text/csv");
await pipeline(cursor, toCsv, res);
```

Avoid `find()` without a cursor for this, as it loads everything into memory.

### 357: What can go wrong with long-running cursors?

- The server closes idle cursors after 10 minutes by default. Slow processing between batches can cause `CursorNotFound`.
- Documents updated during iteration can be seen twice or missed, unless you sort by `_id` and use snapshot reads.
- An open cursor holds server resources.

Fixes: process faster or in batches, use `noCursorTimeout` carefully (and always close the cursor), or paginate by `_id` in a loop instead of one long cursor.

### 358: How do you process millions of documents in a background job?

Iterate by `_id` ranges and write in `bulkWrite()` batches. This is restartable because you can save the last `_id`.

```javascript
let lastId = await getCheckpoint();
while (true) {
  const docs = await User.find(lastId ? { _id: { $gt: lastId } } : {})
    .sort({ _id: 1 })
    .limit(1000)
    .select("email")
    .lean();
  if (docs.length === 0) break;

  await User.bulkWrite(
    docs.map((d) => ({
      updateOne: {
        filter: { _id: d._id },
        update: { $set: { emailLower: d.email.toLowerCase() } },
      },
    })),
    { ordered: false },
  );

  lastId = docs.at(-1)._id;
  await saveCheckpoint(lastId);
}
```

Throttle it if replication lag grows.

### 359: How does bulkWrite() handle errors with ordered: false?

It tries all operations and collects errors. If any fail, it throws a `MongoBulkWriteError` that contains `writeErrors` and the result for the ones that succeeded.

```javascript
try {
  await Product.bulkWrite(ops, { ordered: false });
} catch (err) {
  console.log(
    err.result.insertedCount,
    err.writeErrors.map((e) => e.index),
  );
}
```

Mongoose casting or validation errors (when `throwOnValidationError` is set) come back as `MongooseBulkWriteError`. Mongoose 8 made `bulkWrite()` results include both validation errors and server errors.

### 360: What does throwOnValidationError do in insertMany() and bulkWrite()?

With `ordered: false`, invalid documents are skipped by default and the valid ones are inserted without throwing. That can hide bad data. `throwOnValidationError: true` makes Mongoose throw a `MongooseBulkWriteError` after the valid writes finish, listing the validation errors.

```javascript
await Product.insertMany(rows, {
  ordered: false,
  throwOnValidationError: true,
});
```

### 361: How do you make insertMany() faster for big imports?

- `ordered: false` so one failure does not stop the rest, and the server can work in parallel
- `lean: true` to skip building documents. This also skips casting, validation and defaults, so only use it when the data is already clean (you can run `Model.castObject()` yourself)
- send batches of a few thousand
- turn off `timestamps` if you set them yourself

```javascript
await Product.insertMany(batch, { ordered: false, lean: true });
```

For the largest imports, `mongoimport` or the driver directly can still be faster.

### 362: How does Mongoose handle query casting for nested operators like $elemMatch?

Mongoose walks the filter and uses the schema type of each path. Inside `$elemMatch` on an array of subdocuments, it uses the subdocument schema to cast fields. For `$and`, `$or` and `$nor` it casts each branch. For `$expr` it casts a few known operators but cannot know types in general. Values in `$where` and aggregation stages are not cast.

So `Order.find({ items: { $elemMatch: { product: '66f1...' , qty: '2' } } })` is cast correctly to an ObjectId and a number.

### 363: Why might a query on a Mixed field not match?

Mongoose does not cast `Mixed` paths. If one document stored `{ meta: { count: 5 } }` and the filter sends `{ 'meta.count': '5' }` from a query string, the string does not match the number. With typed schemas Mongoose would cast it. Avoid `Mixed` for data you query, or cast values yourself.

### 364: How do you debug "my update did nothing"?

Check in this order:

1. Turn on `debug` and look at the actual filter and update sent.
2. Check `matchedCount` and `modifiedCount`.
3. Is the field in the schema? `strict` removes unknown update fields.
4. Was a value `undefined`, so the key was dropped?
5. Aggregation and update pipelines are not cast: are ids strings instead of ObjectIds?
6. For `save()`: was the change on a `Mixed` or `Date` path without `markModified()`?
7. Is a query middleware adding a filter (soft delete, tenant)?

### 365: How do you trace Mongoose queries in observability tools?

- Mongoose 9 publishes events through Node's `diagnostics_channel` `TracingChannel`, so APM tools can create spans for Mongoose operations without patching.
- With `monitorCommands: true`, the driver emits `commandStarted`, `commandSucceeded` and `commandFailed`, and Mongoose bubbles them up to the connection.

```javascript
await mongoose.connect(uri, { monitorCommands: true });
mongoose.connection.on("commandSucceeded", (e) => {
  if (e.duration > 200)
    logger.warn({ cmd: e.commandName, ms: e.duration }, "slow mongo command");
});
```

OpenTelemetry also has a Mongoose instrumentation package.

### 366: What is the cost of having many Mongoose hooks?

Each hook is a function call (often async) on every operation. For hot paths like `find` on a busy endpoint, a few hooks are fine, but hooks that run extra queries (like loading a user for permission checks) double the database work. Hooks also make behavior harder to see when reading code. Keep hooks small, avoid queries inside query hooks, and prefer explicit service code for business logic.

### 367: How does Mongoose cast the update in findOneAndUpdate()?

It walks the update object. Top-level keys without `$` are wrapped in `$set` (unless `overwrite` style replacement is used with `findOneAndReplace()`). For each operator, values are cast to the schema type of the path: `$inc` values to numbers, `$push` values to the array item type, `$set` on subdocument paths with the subdocument schema. Unknown paths are removed in strict mode. Validators do not run unless `runValidators` is set.

### 368: How are defaults applied on upserts?

With `setDefaultsOnInsert` (default `true`), Mongoose adds `$setOnInsert` for every path that has a default and is not in the filter or update. So defaults are only stored when the upsert creates a document, not when it updates an existing one.

```javascript
await User.updateOne({ email }, { $set: { name } }, { upsert: true });
// adds $setOnInsert: { role: 'user', createdAt: ... } for schema defaults
```

Mongoose 9 passes the query as context to default functions in this case.

### 369: What happens to _id in subdocument arrays when you replace the array?

If you assign a new array of plain objects, Mongoose creates new subdocuments with new `_id` values. Any client code that stored the old ids now points at nothing.

```javascript
order.items = req.body.items; // all items get new _ids unless the objects include _id
```

If you want to keep ids, include `_id` in each item, or update items one by one with `items.id()`.

### 370: How do you avoid lost updates when two users edit the same document?

Options:

- **Optimistic concurrency**: `optimisticConcurrency: true`, catch `VersionError`, and ask the user to reload.
- **Atomic updates**: use `$set` on only the changed fields, `$inc` for counters, `$push`/`$pull` for arrays.
- **Conditional updates**: include the old value or `updatedAt` in the filter and check `matchedCount`.

```javascript
const res = await Doc.updateOne(
  { _id: id, updatedAt: clientUpdatedAt },
  { $set: { body } },
);
if (res.matchedCount === 0) throw new ConflictError();
```

### 371: How do you implement a simple distributed lock with Mongoose?

Use a collection with a unique key and an expiry.

```javascript
const lockSchema = new Schema({
  _id: String,
  owner: String,
  expiresAt: { type: Date, expires: 0 },
});
const Lock = mongoose.model("Lock", lockSchema);

async function acquire(name, owner, ttlMs) {
  try {
    await Lock.findOneAndUpdate(
      { _id: name, $or: [{ expiresAt: { $lt: new Date() } }, { owner }] },
      { owner, expiresAt: new Date(Date.now() + ttlMs) },
      { upsert: true },
    );
    return true;
  } catch (err) {
    if (err.code === 11000) return false; // someone else holds it
    throw err;
  }
}
```

The TTL index cleans up old locks, but it is not exact, so the filter also checks `expiresAt`. For strict guarantees, use a tool made for locks.

### 372: How do you implement a job queue on MongoDB with Mongoose?

Use `findOneAndUpdate()` to claim one job atomically.

```javascript
async function claimJob(workerId) {
  return Job.findOneAndUpdate(
    { status: "queued", runAt: { $lte: new Date() } },
    { $set: { status: "running", workerId, startedAt: new Date() } },
    { sort: { priority: -1, runAt: 1 }, returnDocument: "after" },
  );
}
```

Index `{ status: 1, priority: -1, runAt: 1 }`. Add a job that requeues jobs stuck in `running` too long. Libraries like Agenda do this for you.

### 373: How do you implement idempotent API writes?

Store an idempotency key with a unique index, and insert it before doing the work.

```javascript
const requestSchema = new Schema({
  _id: String, // idempotency key from the client
  response: Schema.Types.Mixed,
  createdAt: { type: Date, default: Date.now, expires: "24h" },
});

try {
  await Request.create({ _id: key });
} catch (err) {
  if (err.code === 11000) {
    const prev = await Request.findById(key).lean();
    return res.json(prev.response);
  }
  throw err;
}
const order = await createOrder(req.body);
await Request.updateOne({ _id: key }, { response: order });
res.json(order);
```

A real version also handles the case where the first request is still running.

### 374: How do you handle time zones and dates correctly with Mongoose?

- Store all dates as `Date` (UTC in MongoDB), never as formatted strings.
- Convert to the user's zone only when showing them.
- For "all orders on a local day", compute the UTC start and end of that local day.
- In aggregations, use the `timezone` argument of date operators:

```javascript
await Order.aggregate([
  {
    $group: {
      _id: {
        $dateToString: {
          format: "%Y-%m-%d",
          date: "$createdAt",
          timezone: "Europe/Berlin",
        },
      },
      total: { $sum: "$amount" },
    },
  },
]);
```

### 375: How do you store money safely?

Use integer minor units (cents) in a `Number` or `Int32`/`BigInt` field, or `Decimal128`. Never store money as a float.

```javascript
const invoiceSchema = new Schema({
  amountCents: { type: Number, required: true, validate: Number.isInteger },
  currency: { type: String, enum: ["EUR", "USD"], required: true },
});
```

Integer cents are easy to sum in aggregations. `Decimal128` is better for prices with more than two decimals, but you have to handle it as a string or a decimal library in JavaScript.

### 376: How do you get the raw document type from a schema in TypeScript?

Use `InferRawDocType` with a schema definition, or `InferSchemaType` with a schema. For the hydrated type, use `HydratedDocument`.

```typescript
import { Schema, model, InferSchemaType, HydratedDocument } from "mongoose";

const orderSchema = new Schema(
  {
    total: { type: Number, required: true },
    status: {
      type: String,
      enum: ["pending", "paid"] as const,
      default: "pending",
    },
  },
  { timestamps: true },
);

type Order = InferSchemaType<typeof orderSchema>; // plain data
type OrderDoc = HydratedDocument<Order>; // with methods
const OrderModel = model("Order", orderSchema);
```

Fields without `required: true` and without a default are typed as optional or `null | undefined`.

### 377: What does Schema.create() add for TypeScript?

`Schema.create()` (added in Mongoose 9.0 and 8.20) is a static way to build a schema that gives better type inference than `new Schema()`, for example for the raw document type and virtuals, without passing generics by hand.

```typescript
const userSchema = Schema.create({
  name: { type: String, required: true },
  tags: [String],
});
const User = model("User", userSchema);
```

Behavior at runtime is the same as `new Schema()`.

### 378: How do you type the result of lean() queries?

Mongoose infers lean types from the model. You can also pass a type to `lean<T>()`.

```typescript
const users = await User.find().lean(); // inferred plain types
const names = await User.find()
  .select("name")
  .lean<{ _id: Types.ObjectId; name: string }[]>();
```

When you use `select()`, Mongoose does not narrow the type for you, so passing your own type to `lean<T>()` is a common way to keep types honest.

### 379: How do you type populated paths in TypeScript?

Pass the populated shape as a generic to `populate()`.

```typescript
interface IPost {
  title: string;
  author: Types.ObjectId;
}
interface IUser {
  name: string;
}

const post = await Post.findById(id)
  .populate<{ author: Pick<IUser, "name"> }>("author", "name")
  .orFail();

post.author.name; // string
```

Without the generic, `author` stays typed as `ObjectId`.

### 380: How do you type virtuals and query helpers?

Use the schema generic parameters, or the `virtuals` and `query` schema options so they are inferred.

```typescript
const userSchema = new Schema(
  { firstName: String, lastName: String },
  {
    virtuals: {
      fullName: {
        get() {
          return `${this.firstName} ${this.lastName}`;
        },
      },
    },
    query: {
      byFirstName(name: string) {
        return this.where({ firstName: name });
      },
    },
  },
);
```

Mongoose 9 also added `schema.queryHelper()`, which is easier to type when you add helpers after the schema is built.

### 381: How do you write a typed plugin?

Type the plugin as a function that takes a `Schema` and options.

```typescript
import { Schema } from "mongoose";

export function slugPlugin(schema: Schema, opts: { from: string }) {
  schema.add({ slug: { type: String, index: true } });
  schema.pre("save", async function () {
    if (this.isModified(opts.from)) {
      this.set(
        "slug",
        String(this.get(opts.from)).toLowerCase().replace(/\s+/g, "-"),
      );
    }
  });
}

postSchema.plugin(slugPlugin, { from: "title" });
```

The added fields are not in your schema type automatically. Add them to your interface if you need them typed.

### 382: How do you test code that uses transactions?

Transactions need a replica set, so a plain `MongoMemoryServer` is not enough. Use `MongoMemoryReplSet`.

```javascript
import { MongoMemoryReplSet } from "mongodb-memory-server";

const replSet = await MongoMemoryReplSet.create({
  replSet: { count: 1, storageEngine: "wiredTiger" },
});
await mongoose.connect(replSet.getUri());
```

Also test the rollback path: throw inside the transaction and check that nothing was written.

### 383: How do you test that unique indexes work?

Make sure indexes are built before the test runs.

```javascript
beforeAll(async () => {
  await User.init(); // waits for indexes
});

it("rejects duplicate emails", async () => {
  await User.create({ email: "a@b.com" });
  await expect(User.create({ email: "a@b.com" })).rejects.toMatchObject({
    code: 11000,
  });
});
```

If you clear data with `dropDatabase()` between tests, you drop the indexes too, so call `syncIndexes()` or `init()` again. `deleteMany({})` keeps them.

### 384: How do you run tests in parallel without them clashing on data?

Give each test file (or worker) its own database name.

```javascript
const dbName = `test_${process.env.VITEST_POOL_ID ?? process.env.JEST_WORKER_ID ?? 0}`;
await mongoose.connect(mongod.getUri(), { dbName });
```

The `dbName` option overrides the database in the connection string. Clean up with `dropDatabase()` at the end.

### 385: What happens when you use Node.js cluster or PM2 with Mongoose?

Each worker process has its own Mongoose instance, connection and pool. With 8 workers and `maxPoolSize: 100`, you can open up to 800 connections per server. Set a smaller pool per worker. Also each worker runs `autoIndex` on start, which is another reason to turn it off in production.

### 386: How do you shut down cleanly with requests still running?

1. Stop accepting new requests (`server.close()`).
2. Wait for running requests to finish (with a timeout).
3. Close the Mongoose connection.
4. Exit.

```javascript
process.on("SIGTERM", () => {
  server.close(async () => {
    await mongoose.disconnect();
    process.exit(0);
  });
  setTimeout(() => process.exit(1), 10_000).unref();
});
```

If you disconnect first, running requests fail with "client was closed" errors.

### 387: How do you cache Mongoose results in Redis?

Cache lean objects, not documents, because documents do not serialize well. Rebuild documents with `hydrate()` if you need them.

```javascript
async function getProduct(id) {
  const key = `product:${id}`;
  const cached = await redis.get(key);
  if (cached) return JSON.parse(cached);

  const product = await Product.findById(id).lean();
  if (product) await redis.set(key, JSON.stringify(product), { EX: 300 });
  return product;
}

productSchema.post(
  ["save", "findOneAndUpdate", "deleteOne"],
  async function (res) {
    const id = res?._id ?? this.getFilter?.()._id;
    if (id) await redis.del(`product:${id}`);
  },
);
```

After `JSON.parse`, ObjectIds and dates are strings. Cast them again if you compare them.

### 388: How do you use Mongoose with GraphQL without N+1 queries?

Use DataLoader to batch `findById` calls made by resolvers in one request.

```javascript
import DataLoader from "dataloader";

function createLoaders() {
  return {
    user: new DataLoader(async (ids) => {
      const users = await User.find({ _id: { $in: ids } }).lean();
      const byId = new Map(users.map((u) => [u._id.toString(), u]));
      return ids.map((id) => byId.get(id.toString()) ?? null);
    }),
  };
}

const resolvers = {
  Post: { author: (post, _, ctx) => ctx.loaders.user.load(post.author) },
};
```

Create new loaders per request so data does not leak between users.

### 389: What is the outbox pattern and how do you build it with Mongoose?

When you save data and also need to publish an event (to Kafka, RabbitMQ), you can lose the event if the app crashes between the two. With the outbox pattern you write the event to an `outbox` collection in the same transaction, and a separate worker publishes it.

```javascript
await mongoose.connection.transaction(async (session) => {
  const [order] = await Order.create([{ customer, total }], { session });
  await Outbox.create(
    [{ type: "order.created", payload: { orderId: order._id } }],
    { session },
  );
});

// worker
const event = await Outbox.findOneAndUpdate(
  { publishedAt: null },
  { $set: { publishedAt: new Date() } },
  { sort: { _id: 1 } },
);
```

A change stream on `outbox` can replace polling.

### 390: How do you resume a change stream after a restart?

Save the resume token from each event and pass it as `resumeAfter` (or `startAfter`) when opening the stream again.

```javascript
const last = await Checkpoint.findById("orders-stream").lean();

const stream = Order.watch([], {
  resumeAfter: last?.token,
  fullDocument: "updateLookup",
});

stream.on("change", async (change) => {
  await handle(change);
  await Checkpoint.updateOne(
    { _id: "orders-stream" },
    { token: change._id },
    { upsert: true },
  );
});
```

The token must still be in the oplog. If the app was down longer than the oplog window, resume fails and you need a full resync.

### 391: How do you shard a collection used by Mongoose?

Sharding is set up on the cluster (`sh.shardCollection()`), but Mongoose has a `shardKey` schema option. It makes `save()` include the shard key fields in the update filter, which MongoDB needs to route the write.

```javascript
const eventSchema = new Schema(
  { tenantId: String, createdAt: Date },
  {
    shardKey: { tenantId: 1, createdAt: 1 },
  },
);
```

Also include the shard key in your common queries. Queries without it go to all shards (scatter-gather).

### 392: How do you choose a good shard key?

A good shard key:

- has many distinct values (high cardinality)
- spreads writes across shards (no single "hot" value)
- appears in most queries so they target one shard

`_id` with ObjectId is a bad range shard key for write-heavy collections, because new ids always go to the last chunk. Options are a hashed key (`{ _id: 'hashed' }`) or a compound key like `{ tenantId: 1, _id: 1 }`.

### 393: How do you use Atlas Search with Mongoose?

Define the search index (Mongoose 8 added helpers) and use `$search` in an aggregation.

```javascript
productSchema.searchIndex({
  name: "products_search",
  definition: {
    mappings: {
      dynamic: false,
      fields: { name: { type: "string" }, description: { type: "string" } },
    },
  },
});

await Product.createSearchIndexes();

const results = await Product.aggregate([
  {
    $search: {
      index: "products_search",
      text: { query: "red shoe", path: ["name", "description"], fuzzy: {} },
    },
  },
  { $limit: 20 },
  { $project: { name: 1, score: { $meta: "searchScore" } } },
]);
```

`$search` must be the first stage. Mongoose 8 also has `autoSearchIndex` to create these on startup.

### 394: How do you do vector search with Mongoose?

Store embeddings as an array of numbers, create an Atlas Vector Search index, and query with `$vectorSearch`.

```javascript
const docSchema = new Schema({ text: String, embedding: [Number] });

const hits = await Doc.aggregate([
  {
    $vectorSearch: {
      index: "embedding_index",
      path: "embedding",
      queryVector: await embed("how do I reset my password?"),
      numCandidates: 200,
      limit: 5,
    },
  },
  { $project: { text: 1, score: { $meta: "vectorSearchScore" } } },
]);
```

Do not `select` the embedding in normal queries. It is large and slows everything down. `select: false` on that field helps.

### 395: When would you drop down from Mongoose to the native driver?

- hot paths where hydration overhead matters and `lean()` is still too slow
- features Mongoose does not cast or wrap well (complex update pipelines, some admin commands, GridFS)
- bulk data jobs where you do not want hooks or validation
- libraries that expect a driver `Db` or `Collection`

You can mix both: `Model.collection` and `mongoose.connection.db` give you the driver objects on the same connection.

### 396: When would you not use Mongoose at all?

When the data shape is very dynamic and schemas get in the way, when performance needs are very tight, when you want a thin layer and your team is happy with the driver plus a validation library (like Zod) and TypeScript types, or when the project uses several databases and wants one ORM. Mongoose adds a lot of behavior (casting, hooks, strict mode) that you need to understand to avoid surprises.

### 397: What causes memory leaks in Mongoose apps?

- creating models or `useDb()` connections per request without caching
- adding event listeners to `mongoose.connection` per request
- keeping large arrays of full documents in memory caches
- huge `populate()` graphs
- unclosed cursors and change streams
- storing data on `doc.$locals` and keeping the documents around

Use heap snapshots to find which objects grow. Mongoose objects show up as `model` instances or `InternalCache`.

### 398: What are pathsToSave and validateModifiedOnly?

`save({ pathsToSave: ['status'] })` saves only the listed paths, even if others changed. `save({ validateModifiedOnly: true })` validates only paths that changed, which helps when old documents have fields that would fail current validators.

```javascript
const order = await Order.findById(id);
order.status = "shipped";
await order.save({ validateModifiedOnly: true });
```

Both help with legacy data, but hide data problems, so use them on purpose.

### 399: What is the allowNull option added in Mongoose 9?

`allowNull: false` on a schema type makes `null` an invalid value, without making the field required. So the field may be missing (`undefined`), but if it is present it must not be `null`.

```javascript
const schema = new Schema({
  nickname: { type: String, allowNull: false },
});
```

You cannot use it together with `required: true`, Mongoose throws an error at schema creation.

### 400: How do you take a snapshot of modified paths and restore it?

Mongoose 8 added `$createModifiedPathsSnapshot()` and `$restoreModifiedPathsSnapshot()`. They are useful when a save fails inside a transaction and you want the document to remember which paths still need saving.

```javascript
const snapshot = doc.$createModifiedPathsSnapshot();
try {
  await doc.save({ session });
  await session.commitTransaction();
} catch (err) {
  doc.$restoreModifiedPathsSnapshot(snapshot);
  throw err;
}
```

`connection.transaction()` does this for you.

### 401: How do you see the changes a document would send?

Use `doc.$getChanges()` (Mongoose 9 renamed `getChanges()` to this and deprecated the old name). It returns the update object `save()` would send.

```javascript
const user = await User.findById(id);
user.name = "Anna";
user.tags.push("x");
user.$getChanges();
// { $set: { name: 'Anna' }, $push: { tags: { $each: ['x'] } } }
```

Useful for audit logs and debugging.

### 402: How do you get from a subdocument to its parent?

Use `parent()` for the direct parent and `ownerDocument()` for the top-level document.

```javascript
itemSchema.methods.orderTotal = function () {
  return this.ownerDocument().items.reduce(
    (sum, i) => sum + i.price * i.qty,
    0,
  );
};
```

In a subdocument validator, `this.parent()` lets you compare against fields of the parent.

### 403: What does forceRepopulate do?

By default, calling `populate()` on a path that is already populated runs the query again. The `forceRepopulate` option (added in Mongoose 8.x) changes this. With `forceRepopulate: false`, Mongoose skips paths that are already populated, which saves queries when you populate in several places.

```javascript
await post.populate({ path: "author", forceRepopulate: false });
```

### 404: How do you transform populated documents?

Use the `transform` option of `populate()`. It runs for each populated document.

```javascript
await Post.find().populate({
  path: "author",
  select: "name avatar",
  transform: (doc, id) =>
    doc == null ? { _id: id, name: "Deleted user" } : doc,
});
```

This is handy for showing a placeholder when the referenced document was deleted.

### 405: What does Query.prototype.transform() do?

It adds a function that runs on the result before it is returned.

```javascript
const byId = await User.find({ active: true })
  .lean()
  .transform((docs) => new Map(docs.map((d) => [d._id.toString(), d])));
```

The query still has the normal chain, but the final value is whatever the transform returns.

### 406: How does schemaLevelProjections work?

Normally `select: false` in the schema hides a field for every query. Passing `schemaLevelProjections: false` turns that off for one query, so you get the hidden fields without adding `+field` for each.

```javascript
await User.find({ _id: id }).setOptions({ schemaLevelProjections: false });
```

Use it in admin tools and scripts, never in public endpoints.

### 407: How do you move a model to a different connection at runtime?

Mongoose 8.x added `Model.useConnection(connection)`. It switches the model to another connection, for example in tests or when a module is loaded before the app decides which database to use.

```javascript
const conn = mongoose.createConnection(process.env.REPORTS_URI);
Report.useConnection(conn);
```

For most apps, creating the model on the right connection from the start is clearer.

### 408: How do you design a shopping cart with Mongoose?

Keep the cart as one document per user with an embedded array of items, because it is always read and updated as a whole and stays small.

```javascript
const cartSchema = new Schema(
  {
    user: { type: Schema.Types.ObjectId, ref: "User", unique: true },
    items: [
      {
        _id: false,
        product: { type: Schema.Types.ObjectId, ref: "Product" },
        qty: { type: Number, min: 1 },
        priceAtAdd: Number,
      },
    ],
    expiresAt: { type: Date, expires: 0 },
  },
  { timestamps: true },
);

await Cart.updateOne(
  { user: userId, "items.product": { $ne: productId } },
  { $push: { items: { product: productId, qty: 1, priceAtAdd: price } } },
  { upsert: true },
);
```

Use a separate `Order` collection at checkout, and copy the prices into it, because product prices can change. Note the upsert here fails with a duplicate key error if the product is already in the cart, so handle "increase qty" with a separate update.

### 409: How would you model chat messages?

Messages go in their own collection, never in an array on the conversation.

```javascript
const messageSchema = new Schema(
  {
    conversation: {
      type: Schema.Types.ObjectId,
      ref: "Conversation",
      required: true,
    },
    sender: { type: Schema.Types.ObjectId, ref: "User", required: true },
    body: String,
  },
  { timestamps: { createdAt: true, updatedAt: false } },
);

messageSchema.index({ conversation: 1, _id: -1 });
```

Load history with cursor pagination on `_id`. Keep a `lastMessage` subset on the conversation document for the inbox list.

### 410: How would you model threaded comments?

Store each comment as its own document with `parent` and a materialized path or `ancestors` array, so you can fetch a whole thread with one query.

```javascript
const commentSchema = new Schema(
  {
    post: { type: Schema.Types.ObjectId, index: true },
    parent: { type: Schema.Types.ObjectId, default: null },
    ancestors: [{ type: Schema.Types.ObjectId, index: true }],
    text: String,
  },
  { timestamps: true },
);

// all replies under one comment, any depth
await Comment.find({ ancestors: commentId }).sort({ createdAt: 1 });
```

Building the tree happens in code after the query.

### 411: How would you build a leaderboard?

Store scores with an index on the score, and use `$inc` for updates.

```javascript
const scoreSchema = new Schema({
  user: { type: Schema.Types.ObjectId, unique: true },
  points: { type: Number, default: 0, index: true },
});

await Score.updateOne(
  { user: userId },
  { $inc: { points: 10 } },
  { upsert: true },
);
const top = await Score.find()
  .sort({ points: -1 })
  .limit(10)
  .populate("user", "name")
  .lean();
const rank = (await Score.countDocuments({ points: { $gt: myPoints } })) + 1;
```

For huge leaderboards with real-time ranks, Redis sorted sets are a better fit, with MongoDB as the source of truth.

### 412: An endpoint that lists orders became slow. How do you investigate?

1. Measure: is the time in the database or in Node? Log query duration with `debug` or APM.
2. Run `explain('executionStats')` on the query. Look for `COLLSCAN`, high `totalDocsExamined` vs `nReturned`, and in-memory `SORT`.
3. Check `skip()` on deep pages.
4. Check `populate()`: how many extra queries, how large the `$in` lists are.
5. Check result size: are you loading big fields (arrays, embeddings) you do not need?
6. Check hydration: add `lean()` for read-only results.

Then fix: add or change a compound index, switch to cursor pagination, add `select()`, reduce population.

### 413: Memory spikes when a report runs. What do you check?

Most likely the report loads too much into memory:

- `find()` without `limit()` returning hundreds of thousands of full documents
- `populate()` on all of them
- `aggregate()` returning a huge array instead of using `$group` to reduce data in the database

Fixes: move the heavy work into an aggregation pipeline, use `lean()` and `cursor()` to stream, use `allowDiskUse` for large sorts and groups on the server, and run reports on a secondary or analytics node.

### 414: Users are getting duplicate orders. How do you fix it?

Likely causes: double clicks, client retries, or retries after timeouts where the first request actually succeeded. Fixes:

- an idempotency key from the client, stored with a unique index
- a unique index on a natural key (like `cartId` on orders)
- disable the button on the client (helps, but not enough alone)
- when retrying writes in your code, retry only on errors that are safe

```javascript
orderSchema.index({ cartId: 1 }, { unique: true });
```

### 415: How do you migrate string ids to ObjectIds in a reference field?

1. Add the new field or change the type in a new version of the code that can read both.
2. Run a migration that converts the values in batches:

```javascript
await Post.collection.updateMany({ author: { $type: "string" } }, [
  { $set: { author: { $toObjectId: "$author" } } },
]);
```

3. Rebuild indexes on that field if needed.
4. Remove the code path that handles strings.

Using the driver collection avoids Mongoose's `updatePipeline` check and casting. Test on a copy of the data first, because invalid strings make `$toObjectId` fail.

### 416: How do you split one large collection into two?

For example, moving `user.preferences` into a `preferences` collection:

1. Create the new model and write to both places (dual write).
2. Backfill old data with a batched migration.
3. Switch reads to the new collection, behind a feature flag if possible.
4. Stop writing the old field, then `$unset` it in a migration.

Each step is deployable on its own, so you can roll back.

### 417: How do you handle GDPR "delete my data" with Mongoose?

- Find all collections that store user data (references, denormalized copies, logs).
- Delete or anonymize in one job, in batches, possibly in a transaction for core data.
- Make the job safe to rerun.
- Remember backups, change stream consumers and search indexes.

```javascript
await mongoose.connection.transaction(async (session) => {
  await User.deleteOne({ _id: userId }, { session });
  await Comment.updateMany(
    { author: userId },
    { $set: { author: null, authorName: "Deleted user" } },
    { session },
  );
});
```

Keep a list of personal fields in the schemas (for example a custom `pii: true` option) so the job can be generated rather than written by hand.

### 418: Can you add custom options to schema paths?

Yes. Mongoose keeps unknown options on the schema type, so plugins can read them.

```javascript
const userSchema = new Schema({
  email: { type: String, pii: true },
  name: { type: String, pii: true },
  plan: String,
});

const piiPaths = Object.entries(userSchema.paths)
  .filter(([, type]) => type.options.pii)
  .map(([path]) => path); // ['email', 'name']
```

This is a clean way to drive plugins like encryption, redaction or export.

### 419: How do you archive old data?

Move old documents to an archive collection (or cheaper storage) in batches, then delete them from the main collection.

```javascript
const cutoff = new Date(Date.now() - 365 * 24 * 3600 * 1000);
await Order.aggregate([
  { $match: { createdAt: { $lt: cutoff } } },
  { $merge: { into: "orders_archive", whenMatched: "keepExisting" } },
]);
await Order.deleteMany({ createdAt: { $lt: cutoff } });
```

For huge collections, do it in `_id` ranges. Atlas also offers Online Archive for this.

### 420: How do you scale reads in a Mongoose app?

- Add the right indexes first.
- Use `lean()` and projections to reduce work per query.
- Cache hot data (Redis, in-memory with short TTL).
- Read from secondaries for queries that can be slightly stale (`read('secondaryPreferred')`).
- Pre-compute expensive aggregations into summary collections.
- Shard when one replica set is not enough.

### 421: How do you scale writes in a Mongoose app?

- Batch writes with `insertMany()` and `bulkWrite()` instead of single calls.
- Use atomic updates instead of read-modify-save.
- Avoid hot documents that every request updates (like a global counter). Split them into several counters and sum them.
- Lower write concern only where losing some writes is acceptable (like metrics).
- Shard with a key that spreads writes.

### 422: What is the problem with a single hot counter document?

Every request updates the same document, so writes queue up on it. Spread the load with sharded counters:

```javascript
const SHARDS = 20;
await PageViews.updateOne(
  { page: pageId, shard: Math.floor(Math.random() * SHARDS) },
  { $inc: { count: 1 } },
  { upsert: true },
);

const [{ total } = { total: 0 }] = await PageViews.aggregate([
  { $match: { page: pageId } },
  { $group: { _id: null, total: { $sum: "$count" } } },
]);
```

### 423: How do you add schema-level read concern or write concern?

Use the schema options. Every query and write on that model then uses them unless overridden.

```javascript
const paymentSchema = new Schema(
  { amount: Number },
  {
    readConcern: { level: "majority" },
    writeConcern: { w: "majority", j: true },
  },
);
```

This is useful for critical models in an app where the default is weaker.

### 424: How does Mongoose handle a schema path named like a built-in method?

Some names are reserved because they clash with document methods or internals, like `save`, `validate`, `errors`, `schema`, `collection`, `get`, `init`, `isModified`, `toObject`, `populated` and `emit`. The full list is in `Schema.reserved`. Mongoose prints a warning when you use one of them as a path, because it can break documents in odd ways. Some special names like `__proto__` throw an error.

```javascript
new Schema({ errors: [String] });
// warning: `errors` is a reserved schema pathname and may break some functionality
```

If your data has such a field, store it under another name in the database, or turn the warning off with `suppressReservedKeysWarning` only if you are sure it is safe.

### 425: How do getters and toJSON interact in API responses?

`toJSON()` does not apply getters unless you set `toJSON: { getters: true }`. If you turn getters on, `id` is also added as a virtual (because `getters: true` includes virtuals). And lean queries skip getters altogether. A common bug: a `Decimal128` getter works in `doc.price` but the API still returns `{ $numberDecimal: ... }`, because getters are not on for `toJSON` or the endpoint uses `lean()`.

### 426: How do you return ObjectIds as strings in JSON consistently?

ObjectIds already turn into hex strings in `JSON.stringify()`, because `ObjectId` has a `toJSON()` method. Problems only come when you return `toObject()` results to code that is not JSON, or when you use other serializers. Mongoose 7.x added the `flattenObjectIds` option for `toObject()` and `toJSON()`:

```javascript
doc.toObject({ flattenObjectIds: true }); // _id and refs as strings
```

### 427: How do you write a plugin that adds createdBy and updatedBy?

Use `AsyncLocalStorage` to know the current user in hooks.

```javascript
export const requestContext = new AsyncLocalStorage();

function auditFields(schema) {
  schema.add({
    createdBy: { type: Schema.Types.ObjectId, ref: "User", immutable: true },
    updatedBy: { type: Schema.Types.ObjectId, ref: "User" },
  });

  schema.pre("save", async function () {
    const userId = requestContext.getStore()?.userId;
    if (this.isNew) this.createdBy = userId;
    this.updatedBy = userId;
  });

  schema.pre(
    ["updateOne", "updateMany", "findOneAndUpdate"],
    async function () {
      this.set({ updatedBy: requestContext.getStore()?.userId });
    },
  );
}
```

Wrap each request with `requestContext.run({ userId }, next)` in middleware.

### 428: What does Connection.prototype.bulkWrite() do?

Mongoose 8.x added a connection-level `bulkWrite()` that uses the MongoDB 8.0 client bulk write command. It can write to several collections in one round trip.

```javascript
await mongoose.connection.bulkWrite([
  {
    model: "User",
    name: "updateOne",
    filter: { _id: userId },
    update: { $inc: { orders: 1 } },
  },
  { model: "Order", name: "insertOne", document: { user: userId, total: 50 } },
]);
```

It needs MongoDB server 8.0 or newer. It is not a transaction, so writes can partly succeed.

### 429: How do you run several queries in parallel safely?

Use `Promise.all()` for independent reads. They run on different pool connections.

```javascript
const [user, orders, unread] = await Promise.all([
  User.findById(id).lean(),
  Order.find({ user: id }).sort({ _id: -1 }).limit(5).lean(),
  Notification.countDocuments({ user: id, read: false }),
]);
```

Do not do this inside a transaction (one session cannot run parallel operations), and do not start thousands at once. Use a limit like `p-limit` for big loops.

### 430: How do you deal with clock skew for timestamps across servers?

`timestamps` uses the app server's clock, so documents written by different servers can have slightly different times. If ordering matters:

- sort by `_id` (ObjectIds start with seconds since epoch, plus a counter)
- or set the time on the server with `$currentDate` or `$$NOW` in an update

```javascript
await Event.updateOne({ _id: id }, { $currentDate: { processedAt: true } });
```

Keep servers in sync with NTP anyway.

### 431: How do you query documents created in a time range using only _id?

ObjectIds contain the creation time in seconds, so you can build an ObjectId from a date.

```javascript
function objectIdFromDate(date) {
  return mongoose.Types.ObjectId.createFromTime(
    Math.floor(date.getTime() / 1000),
  );
}

await Log.find({ _id: { $gte: objectIdFromDate(new Date("2026-10-01")) } });
```

This uses the `_id` index, so no extra index is needed. It only works when ids are generated at insert time.

### 432: What happens if two models use the same collection?

It works, MongoDB does not care, but the schemas must agree. Each model only knows its own fields, so with `strict` mode one model can drop fields the other uses when it saves full documents. Indexes from both schemas are built on the same collection, and `syncIndexes()` on one model drops the other's indexes. Use discriminators or one shared schema instead.

### 433: How does Mongoose handle deeply nested updates on subdocument arrays inside arrays?

You can use nested `arrayFilters`.

```javascript
await Course.updateOne(
  { _id: courseId },
  { $set: { "modules.$[m].lessons.$[l].done": true } },
  { arrayFilters: [{ "m._id": moduleId }, { "l._id": lessonId }] },
);
```

On a loaded document it is just `course.modules.id(moduleId).lessons.id(lessonId).done = true; await course.save()`. Deep nesting is often a sign to split data into collections.

### 434: How do you make a field unique inside an embedded array?

A unique index does not stop duplicates inside one document's array; it only works across documents. Use `$addToSet` for simple values, or a filter with `$ne` for subdocuments:

```javascript
await User.updateOne(
  { _id: userId, "emails.address": { $ne: email } },
  { $push: { emails: { address: email } } },
);
```

Add a validator on the array to catch duplicates in `save()` too.

### 435: How do you make expensive virtuals cheap?

Virtuals run every time they are read and on every `toJSON()`. If a virtual is costly (loops over big arrays, date formatting for many docs), either:

- store the computed value as a real field and update it in a pre save hook
- compute it in the aggregation with `$addFields`
- only add it on the endpoints that need it, not in `toJSON` for all

### 436: What should a good Mongoose error handler in Express look like?

```javascript
app.use((err, req, res, next) => {
  if (err instanceof mongoose.Error.ValidationError) {
    return res.status(400).json({
      errors: Object.fromEntries(
        Object.entries(err.errors).map(([k, v]) => [k, v.message]),
      ),
    });
  }
  if (err instanceof mongoose.Error.CastError) {
    return res.status(400).json({ message: `Invalid value for ${err.path}` });
  }
  if (err instanceof mongoose.Error.DocumentNotFoundError) {
    return res.status(404).json({ message: "Not found" });
  }
  if (err instanceof mongoose.Error.VersionError) {
    return res
      .status(409)
      .json({ message: "Document was changed by someone else" });
  }
  if (err.code === 11000) {
    return res.status(409).json({
      message: "Already exists",
      fields: Object.keys(err.keyValue ?? {}),
    });
  }
  if (err.name === "MongooseServerSelectionError") {
    return res.status(503).json({ message: "Database unavailable" });
  }
  next(err);
});
```

### 437: How do you keep a repository layer clean on top of Mongoose?

- Keep Mongoose models inside the data layer. Return plain objects (lean) or domain types from repositories.
- Put business rules in services, not in hooks.
- Use hooks only for cross-cutting data concerns (timestamps, slugs, audit).
- Make all query building go through repository methods, so tenant filters and projections are not forgotten.

This keeps the rest of the app testable without a database and makes it possible to change queries in one place.

### 438: How do you review a Mongoose schema in a code review?

Check:

- required fields, enums and ranges match the business rules
- indexes exist for the queries that the code runs
- no unbounded arrays
- sensitive fields have `select: false`
- `toJSON` hides internal fields
- defaults are functions where they must be (`Date.now`, not `Date.now()`)
- hooks are small and do not hide business logic
- `Mixed` is used only where really needed

### 439: What happens if you call mongoose.model() before mongoose.connect()?

It is fine. Models are bound to the connection object, not to an open socket. Operations are buffered until the connection is open. Index builds also wait until the connection opens. Problems only appear when the connection never opens (buffer timeout errors) or when you meant to use a different connection.

### 440: How do you connect to MongoDB with TLS and X.509 or AWS IAM?

Most of this is driver configuration you pass through Mongoose.

```javascript
// X.509
await mongoose.connect(uri, {
  tls: true,
  tlsCertificateKeyFile: "/etc/certs/client.pem",
  authMechanism: "MONGODB-X509",
});

// AWS IAM on Atlas
await mongoose.connect(
  "mongodb+srv://cluster0.example.mongodb.net/app?authMechanism=MONGODB-AWS&authSource=$external",
);
```

IAM uses the credentials from the environment (role on EC2, ECS or Lambda), so no password is stored in the app.

### 441: How do you rotate database passwords without downtime?

1. Create the new password (or a second user) on the database.
2. Deploy the app with the new connection string, one instance at a time.
3. Old instances keep working with the old password until they are replaced.
4. Remove the old password once all instances use the new one.

Mongoose reads the connection string only at `connect()`, so a restart or redeploy is needed. Using IAM or X.509 auth avoids most of this.

### 442: What does a Mongoose app need from MongoDB for change streams and transactions?

A replica set or a sharded cluster. Standalone servers support neither. For local development you can start a single-node replica set:

```bash
mongod --replSet rs0 --dbpath ./data
mongosh --eval "rs.initiate()"
```

Then connect with `mongodb://127.0.0.1:27017/app?replicaSet=rs0` (or `directConnection=true` in Docker setups).

### 443: How do you handle "MongooseServerSelectionError: connect ECONNREFUSED ::1:27017"?

Node.js 17+ prefers IPv6, so `localhost` can resolve to `::1`, while MongoDB listens on `127.0.0.1`. Fixes:

- use `127.0.0.1` in the connection string
- or pass `family: 4` in the connection options
- or make `mongod` listen on IPv6 too (`--ipv6`)

### 444: How do you avoid conflicts between autoIndex and a deploy that changes indexes?

During a rolling deploy, old and new versions of the app run at the same time with different schemas. If both have `autoIndex` on, the new version builds new indexes while the old version may complain about missing ones, and index option changes (like adding `unique`) fail with "Index already exists with different options". The safe way: turn off `autoIndex`, apply index changes in a migration before the deploy (add new ones first), and drop old indexes after the deploy.

### 445: How do you work with a database that other services also write to?

- Do not trust that data matches your schema. Use `validateModifiedOnly`, careful defaults and `strictRead` checks.
- Agree on one owner per collection for schema and indexes.
- Never run `syncIndexes()` on shared collections.
- Add MongoDB-level `$jsonSchema` validation for rules everyone must follow.
- Use change streams to react to writes from other services instead of polling.

### 446: How do you set up read-only access for a reporting service?

Create a database user with the `read` role on the needed database, and use a separate connection in the reporting service.

```javascript
const reports = mongoose.createConnection(process.env.REPORTS_RO_URI, {
  readPreference: "secondaryPreferred",
  autoIndex: false,
  autoCreate: false,
});
```

Turn off `autoIndex` and `autoCreate`, otherwise Mongoose tries to create indexes and collections and gets permission errors.

### 447: What is autoCreate and why does it matter?

With `autoCreate: true` (default since Mongoose 6), Mongoose calls `createCollection()` for each model on startup. This is needed for capped, time series and clustered collections and collections with collation options, and it avoids errors when the first operation is inside a transaction (older MongoDB versions could not create collections inside transactions). Turn it off for read-only users or when collections are managed by migrations.

### 448: How would you explain the difference between Mongoose validation and MongoDB schema validation in an interview?

Mongoose validation runs in your Node.js process before data is sent, only for writes that go through Mongoose documents (and updates with `runValidators`). It is easy to write, supports async checks and good error messages. MongoDB schema validation (`$jsonSchema`) runs on the server for every write from every client, including the shell and other services, but it is less flexible and gives less friendly errors. In critical systems you use both: Mongoose for friendly errors, MongoDB validation as the last line of defense.

### 449: What are the trade-offs of putting logic in Mongoose middleware?

Pros: runs automatically, keeps code DRY, good for data concerns like timestamps, slugs, hashing and audit fields.

Cons: hidden behavior that is easy to forget, does not run for every write path (`updateMany`, `bulkWrite`, driver calls), harder to test in isolation, can add hidden queries, and order of hooks matters. Keep business logic in services and use middleware for small, data-level rules.

### 450: You join a team with an old Mongoose 5 app. How do you upgrade it to Mongoose 9?

Upgrade one major version at a time and follow each migration guide:

1. **5 to 6**: remove old connection options (`useNewUrlParser` and so on), check `strictQuery` and `strictPopulate` changes.
2. **6 to 7**: remove callbacks everywhere (move to `async`/`await`), replace `remove()` with `deleteOne()`/`deleteMany()`, note `strictQuery` default changed back to `false`.
3. **7 to 8**: replace `count()`, `findOneAndRemove()` and `rawResult`, upgrade to the driver 6 and Node versions it needs.
4. **8 to 9**: remove `next()` from pre hooks, replace `new: true` with `returnDocument: 'after'`, check update pipelines, UUID handling, and Node 20.19+.

Run the test suite at each step, check plugins from npm for compatibility, and turn on `debug` in staging to spot queries that changed.
