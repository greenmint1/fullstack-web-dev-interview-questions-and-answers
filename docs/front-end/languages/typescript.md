# TypeScript Interview Questions and Answers

_Last updated: October 28, 2026_

A list of 450 TypeScript interview questions with answers and code examples, split into three levels: easy, moderate and advanced.

## Table of Contents

- [Easy Questions (1-150)](#easy)
- [Moderate Questions (151-300)](#moderate)
- [Advanced Questions (301-450)](#advanced)

### Easy Questions (1-150)

- [1: What is TypeScript?](#q1)
- [2: Why would you use TypeScript instead of JavaScript?](#q2)
- [3: Does the browser run TypeScript directly?](#q3)
- [4: How do you install TypeScript?](#q4)
- [5: How do you compile a TypeScript file?](#q5)
- [6: What is tsconfig.json?](#q6)
- [7: What are the basic types in TypeScript?](#q7)
- [8: How do you declare a variable with a type?](#q8)
- [9: What is type inference?](#q9)
- [10: What is the any type?](#q10)
- [11: What is the unknown type?](#q11)
- [12: What is the difference between any and unknown?](#q12)
- [13: What is the void type?](#q13)
- [14: What is the never type?](#q14)
- [15: What is the difference between void and never?](#q15)
- [16: How do you define an array type?](#q16)
- [17: What is a tuple?](#q17)
- [18: What is an enum?](#q18)
- [19: What is the difference between numeric and string enums?](#q19)
- [20: What is an interface?](#q20)
- [21: What is a type alias?](#q21)
- [22: What are optional properties?](#q22)
- [23: What are readonly properties?](#q23)
- [24: How do you add types to a function?](#q24)
- [25: What are optional parameters in functions?](#q25)
- [26: What are default parameters?](#q26)
- [27: What are rest parameters?](#q27)
- [28: What is a union type?](#q28)
- [29: What is an intersection type?](#q29)
- [30: What are literal types?](#q30)
- [31: What is type assertion?](#q31)
- [32: What is the difference between let, const and var in TypeScript?](#q32)
- [33: What is the difference between null and undefined in TypeScript?](#q33)
- [34: What is the strict mode in TypeScript?](#q34)
- [35: What does noImplicitAny do?](#q35)
- [36: What is the object type?](#q36)
- [37: What is the difference between object, Object and {}?](#q37)
- [38: How do you type an object inline?](#q38)
- [39: What is a class in TypeScript?](#q39)
- [40: What are access modifiers in TypeScript?](#q40)
- [41: What is the constructor in a class?](#q41)
- [42: What are parameter properties?](#q42)
- [43: How does inheritance work in TypeScript?](#q43)
- [44: How does a class implement an interface?](#q44)
- [45: What is an abstract class?](#q45)
- [46: What are static members in a class?](#q46)
- [47: What are getters and setters?](#q47)
- [48: What file extensions does TypeScript use?](#q48)
- [49: What is a .d.ts file?](#q49)
- [50: What is a TypeScript Map file?](#q50)
- [51: Is TypeScript a superset of JavaScript?](#q51)
- [52: What are some downsides of TypeScript?](#q52)
- [53: What is the difference between an interface and a type alias?](#q53)
- [54: How do you extend an interface?](#q54)
- [55: Can an interface extend multiple interfaces?](#q55)
- [56: Can a class implement multiple interfaces?](#q56)
- [57: How do you describe a function type?](#q57)
- [58: What is the typeof operator in TypeScript?](#q58)
- [59: What is type narrowing?](#q59)
- [60: How do you use instanceof for narrowing?](#q60)
- [61: How do you use the in operator for narrowing?](#q61)
- [62: What is optional chaining?](#q62)
- [63: What is the nullish coalescing operator?](#q63)
- [64: What is the non-null assertion operator?](#q64)
- [65: How do you export and import in TypeScript?](#q65)
- [66: What is a default export?](#q66)
- [67: How do you export and import only types?](#q67)
- [68: What are generics?](#q68)
- [69: How do you write a generic interface?](#q69)
- [70: How do you write a generic class?](#q70)
- [71: What is the keyof operator?](#q71)
- [72: What is an index signature?](#q72)
- [73: What is the Record utility type?](#q73)
- [74: What is the Partial utility type?](#q74)
- [75: What is the Required utility type?](#q75)
- [76: What is the Readonly utility type?](#q76)
- [77: What is the Pick utility type?](#q77)
- [78: What is the Omit utility type?](#q78)
- [79: How do you make an array read only?](#q79)
- [80: What does as const do?](#q80)
- [81: How do you type a callback function?](#q81)
- [82: How do you type a Promise?](#q82)
- [83: How do you type an async function?](#q83)
- [84: What is the type of the error in a catch block?](#q84)
- [85: What is the declare keyword?](#q85)
- [86: What are @types packages?](#q86)
- [87: What is DefinitelyTyped?](#q87)
- [88: What does the target option do in tsconfig?](#q88)
- [89: What are outDir and rootDir?](#q89)
- [90: How do you run the compiler in watch mode?](#q90)
- [91: What does the noEmit option do?](#q91)
- [92: What does noEmitOnError do?](#q92)
- [93: What is allowJs?](#q93)
- [94: What is ts-node?](#q94)
- [95: What is the TypeScript Playground?](#q95)
- [96: How do you type DOM elements?](#q96)
- [97: How do you type DOM events?](#q97)
- [98: What is the symbol type?](#q98)
- [99: What is the bigint type?](#q99)
- [100: What happens to types after compilation?](#q100)
- [101: Can TypeScript check types at runtime?](#q101)
- [102: What is structural typing?](#q102)
- [103: Can you use instanceof with an interface?](#q103)
- [104: How do you narrow with a truthiness check?](#q104)
- [105: How do you narrow with equality checks?](#q105)
- [106: How do you type an array of objects?](#q106)
- [107: What is the difference between (string | number)[] and string[] | number[]?](#q107)
- [108: How are array methods like map and filter typed?](#q108)
- [109: How do you type object destructuring?](#q109)
- [110: How does the spread operator work with types?](#q110)
- [111: What is the Function type and should you use it?](#q111)
- [112: What is the difference between method and property syntax in an interface?](#q112)
- [113: Can an interface have optional methods?](#q113)
- [114: What is method overriding?](#q114)
- [115: What is the override keyword?](#q115)
- [116: What does super do?](#q116)
- [117: What is the difference between private and #private?](#q117)
- [118: Can a class property be readonly?](#q118)
- [119: What is the difference between an optional property and a property of type T | undefined?](#q119)
- [120: How do you type a Map?](#q120)
- [121: How do you type a Set?](#q121)
- [122: What type does JSON.parse return?](#q122)
- [123: How do you type a fetch response?](#q123)
- [124: What type does setTimeout return?](#q124)
- [125: How do you type Promise.all?](#q125)
- [126: What is the ReturnType utility type?](#q126)
- [127: What is the Parameters utility type?](#q127)
- [128: What is the NonNullable utility type?](#q128)
- [129: What is the Exclude utility type?](#q129)
- [130: What is the Extract utility type?](#q130)
- [131: What is the Awaited utility type?](#q131)
- [132: What is the difference between Omit and Exclude?](#q132)
- [133: What is a const enum?](#q133)
- [134: What is enum reverse mapping?](#q134)
- [135: Should you use an enum or a union of string literals?](#q135)
- [136: What is a template literal type?](#q136)
- [137: Why does Object.keys return string[] and not keyof T?](#q137)
- [138: What does the lib option do in tsconfig?](#q138)
- [139: What does the module option do in tsconfig?](#q139)
- [140: What are include, exclude and files in tsconfig?](#q140)
- [141: What does esModuleInterop do?](#q141)
- [142: What does skipLibCheck do?](#q142)
- [143: What does resolveJsonModule do?](#q143)
- [144: What are baseUrl and paths in tsconfig?](#q144)
- [145: How do you type props in a React component?](#q145)
- [146: How do you type useState in React?](#q146)
- [147: How do you type events in React?](#q147)
- [148: How do you create a custom error class?](#q148)
- [149: Can a class be used as a type?](#q149)
- [150: How do you use ESLint with TypeScript?](#q150)

### Moderate Questions (151-300)

- [151: What are generic constraints?](#q151)
- [152: How do you use keyof with generics to safely read a property?](#q152)
- [153: Can generics have default types?](#q153)
- [154: How does TypeScript infer generic types?](#q154)
- [155: What are indexed access types?](#q155)
- [156: How do you get the type of an array element?](#q156)
- [157: What are mapped types?](#q157)
- [158: How do mapped type modifiers work?](#q158)
- [159: What is key remapping in mapped types?](#q159)
- [160: What are conditional types?](#q160)
- [161: What is the infer keyword?](#q161)
- [162: What are distributive conditional types?](#q162)
- [163: What is a discriminated union?](#q163)
- [164: How do you do exhaustiveness checking?](#q164)
- [165: What is a user-defined type guard?](#q165)
- [166: What are assertion functions?](#q166)
- [167: What is function overloading?](#q167)
- [168: When should you use overloads instead of a union parameter?](#q168)
- [169: How do you type the this parameter in a function?](#q169)
- [170: What is the polymorphic this type?](#q170)
- [171: What is declaration merging?](#q171)
- [172: What is module augmentation?](#q172)
- [173: How do you add a property to the global window object?](#q173)
- [174: What are namespaces?](#q174)
- [175: What is the difference between namespaces and modules?](#q175)
- [176: What are triple-slash directives?](#q176)
- [177: How do you declare types for a JavaScript module that has no types?](#q177)
- [178: How do you import images or CSS files in TypeScript?](#q178)
- [179: What is excess property checking?](#q179)
- [180: What is the satisfies operator?](#q180)
- [181: What is the difference between satisfies, a type annotation and as?](#q181)
- [182: What is type widening?](#q182)
- [183: What is the InstanceType utility type?](#q183)
- [184: What is the ConstructorParameters utility type?](#q184)
- [185: How do you type a class constructor as a parameter?](#q185)
- [186: What is a private constructor and when is it used?](#q186)
- [187: What is the difference between an abstract class and an interface?](#q187)
- [188: What does strictPropertyInitialization do?](#q188)
- [189: What is the definite assignment assertion?](#q189)
- [190: What does noUncheckedIndexedAccess do?](#q190)
- [191: What does exactOptionalPropertyTypes do?](#q191)
- [192: What does strictFunctionTypes do?](#q192)
- [193: Why can a function that returns a value be assigned to a type that returns void?](#q193)
- [194: What are optional and rest elements in tuples?](#q194)
- [195: What are labeled tuple elements?](#q195)
- [196: How do you get the keys of an enum as a type?](#q196)
- [197: What is the difference between `Record<string, T>` and an index signature?](#q197)
- [198: When should you use a Map instead of a plain object?](#q198)
- [199: What are the intrinsic string manipulation types?](#q199)
- [200: How do you write a generic React component?](#q200)
- [201: How do you type useRef in React?](#q201)
- [202: How do you type useReducer in React?](#q202)
- [203: How do you type React Context?](#q203)
- [204: What is the difference between ReactNode, ReactElement and JSX.Element?](#q204)
- [205: How do you make a React component accept all props of a native HTML element?](#q205)
- [206: How do you type Express request handlers?](#q206)
- [207: How do you type environment variables in Node.js?](#q207)
- [208: What are decorators in TypeScript?](#q208)
- [209: What is the difference between experimentalDecorators and the new standard decorators?](#q209)
- [210: How do you write a class decorator?](#q210)
- [211: What does emitDecoratorMetadata do?](#q211)
- [212: How do you type a generator function?](#q212)
- [213: How do you make a class iterable?](#q213)
- [214: How do you type an async generator?](#q214)
- [215: What does isolatedModules do?](#q215)
- [216: What does verbatimModuleSyntax do?](#q216)
- [217: What does moduleResolution do?](#q217)
- [218: What are project references?](#q218)
- [219: What does the incremental option do?](#q219)
- [220: How do you publish a TypeScript library with types?](#q220)
- [221: What is declarationMap?](#q221)
- [222: What is the difference between @ts-ignore and @ts-expect-error?](#q222)
- [223: What do @ts-check and @ts-nocheck do?](#q223)
- [224: Can you use TypeScript types in a JavaScript file?](#q224)
- [225: What do noUnusedLocals and noUnusedParameters do?](#q225)
- [226: What do noImplicitReturns and noFallthroughCasesInSwitch do?](#q226)
- [227: What does noPropertyAccessFromIndexSignature do?](#q227)
- [228: What is a double assertion and when is it needed?](#q228)
- [229: What is PropertyKey?](#q229)
- [230: What properties can you access on a union of object types?](#q230)
- [231: What is the result of keyof on a union and on an intersection?](#q231)
- [232: How does Array.isArray narrow types?](#q232)
- [233: How do you use filter to remove null values with correct types?](#q233)
- [234: Why is narrowing sometimes lost inside callbacks?](#q234)
- [235: How does control flow analysis work?](#q235)
- [236: What is a unique symbol?](#q236)
- [237: Can index signatures use template literal patterns?](#q237)
- [238: Can a getter and setter have different types?](#q238)
- [239: What are static blocks in classes?](#q239)
- [240: What is the accessor keyword?](#q240)
- [241: What is an abstract construct signature?](#q241)
- [242: How do you write generic methods in a class?](#q242)
- [243: How do you type the static side of a class with an interface?](#q243)
- [244: What is a hybrid type?](#q244)
- [245: What are ReadonlyMap and ReadonlySet?](#q245)
- [246: How is a WeakMap typed and when do you use it?](#q246)
- [247: What type does Object.freeze return?](#q247)
- [248: How do you type a rejected Promise?](#q248)
- [249: What does a `Promise<never>` mean?](#q249)
- [250: What happens when you intersect two types that have the same property with different types?](#q250)
- [251: How do unknown and never behave in unions and intersections?](#q251)
- [252: What is contextual typing?](#q252)
- [253: Should you always write return types on functions?](#q253)
- [254: What is a heterogeneous enum?](#q254)
- [255: What are computed and constant enum members?](#q255)
- [256: What is the "as const object" pattern and why use it instead of an enum?](#q256)
- [257: What is the difference between a generic function type and a generic type alias for a function?](#q257)
- [258: How can a generic type have more than one constraint?](#q258)
- [259: How do you type the result of Object.entries?](#q259)
- [260: How do you build an object type from a constant list of keys?](#q260)
- [261: What are mixins in TypeScript?](#q261)
- [262: Why do custom React hooks often return as const?](#q262)
- [263: How do you type forwardRef in React?](#q263)
- [264: How do you write a generic API fetch helper?](#q264)
- [265: Can you have abstract properties in an abstract class?](#q265)
- [266: What does a protected constructor do?](#q266)
- [267: Can an interface extend a class?](#q267)
- [268: Can a class implement a type alias?](#q268)
- [269: What are export = and import = require()?](#q269)
- [270: What are .mts and .cts files?](#q270)
- [271: Why do you need .js extensions in imports with module nodenext?](#q271)
- [272: What are the types and typeRoots options?](#q272)
- [273: How do you use TypeScript with Jest or Vitest?](#q273)
- [274: How do you type a mocked module in Jest?](#q274)
- [275: What are import types?](#q275)
- [276: How are dynamic imports typed?](#q276)
- [277: How do you write an assertNever helper?](#q277)
- [278: Why does keyof on a string index signature give string | number?](#q278)
- [279: What happens when you use a union in an indexed access type?](#q279)
- [280: How is the Partial type implemented?](#q280)
- [281: How are Pick and Omit implemented?](#q281)
- [282: How is ReturnType implemented?](#q282)
- [283: Is a type assertion the same as type casting?](#q283)
- [284: How do you define a recursive type?](#q284)
- [285: How would you write a type for any JSON value?](#q285)
- [286: Can an interface have both an index signature and known properties?](#q286)
- [287: How do you write overloads in an interface?](#q287)
- [288: Why does the order of overloads matter?](#q288)
- [289: What does strictBindCallApply do?](#q289)
- [290: What are ThisParameterType and OmitThisParameter?](#q290)
- [291: How do you type a function that takes a callback with a generic result?](#q291)
- [292: What is the difference between Object.assign and spread for types?](#q292)
- [293: What is a type predicate for this in a class method?](#q293)
- [294: How do generics work with default values in function parameters?](#q294)
- [295: How do you make sure two parameters have the same type?](#q295)
- [296: What is the difference between interface extends and intersection when it comes to errors and performance?](#q296)
- [297: How do you type an object where some keys are known and the rest are dynamic with a different type?](#q297)
- [298: What is the `Uppercase<string>` type?](#q298)
- [299: How do optional chaining and the types of the result work together?](#q299)
- [300: How do you type a function that returns different types based on a boolean flag?](#q300)

### Advanced Questions (301-450)

- [301: What are covariance and contravariance?](#q301)
- [302: What are the in and out variance annotations?](#q302)
- [303: Why are method parameters bivariant in TypeScript?](#q303)
- [304: Why are arrays covariant and why is that unsafe?](#q304)
- [305: What are some known places where TypeScript is not fully sound?](#q305)
- [306: How do you turn a union into an intersection?](#q306)
- [307: Why does infer in a contravariant position produce an intersection?](#q307)
- [308: How do you check if a type is any?](#q308)
- [309: How do you check if a type is never?](#q309)
- [310: How do you check if two types are exactly equal?](#q310)
- [311: How do you write a DeepPartial type?](#q311)
- [312: How do you write a DeepReadonly type?](#q312)
- [313: What are branded types?](#q313)
- [314: How can you make a brand that can't be faked with a string property?](#q314)
- [315: What are phantom types?](#q315)
- [316: What are variadic tuple types?](#q316)
- [317: How do you type a partial application function?](#q317)
- [318: How do you type a curry function?](#q318)
- [319: How do you type a pipe function?](#q319)
- [320: How do you get the length of a tuple as a type?](#q320)
- [321: How do you reverse a tuple type?](#q321)
- [322: How do you do arithmetic at the type level?](#q322)
- [323: How do you turn a tuple into a union?](#q323)
- [324: Why is converting a union to a tuple not a good idea?](#q324)
- [325: How do you parse strings at the type level with template literal types?](#q325)
- [326: How do you write a Trim type?](#q326)
- [327: How do you extract route parameters from a path string?](#q327)
- [328: How do you convert snake_case to camelCase at the type level?](#q328)
- [329: How do you get all dot-notation paths of an object type?](#q329)
- [330: How do you get the type at a dot-notation path?](#q330)
- [331: What is the limit on recursion in conditional types?](#q331)
- [332: What are const type parameters?](#q332)
- [333: How do you make props mutually exclusive (XOR)?](#q333)
- [334: How do you require at least one of several optional properties?](#q334)
- [335: How do you get the keys of an object whose values match a certain type?](#q335)
- [336: How do you find the optional keys of a type?](#q336)
- [337: What is a homomorphic mapped type?](#q337)
- [338: How do you map over a tuple and keep it a tuple?](#q338)
- [339: What does infer with extends do?](#q339)
- [340: Which overload does ReturnType use for an overloaded function?](#q340)
- [341: How do you write a type-safe event emitter?](#q341)
- [342: How do you write a builder that tracks which fields were set?](#q342)
- [343: How do you type a polymorphic "as" prop component in React?](#q343)
- [344: How do you type a higher-order component in React?](#q344)
- [345: How do you type Object.fromEntries so it keeps the keys?](#q345)
- [346: Does TypeScript support higher-kinded types?](#q346)
- [347: Why can a function with fewer parameters be assigned to a type with more parameters?](#q347)
- [348: What is ThisType?](#q348)
- [349: What is the difference between an intersection of functions and a union of functions?](#q349)
- [350: What is the "correlated union" problem?](#q350)
- [351: What are the main parts of the TypeScript compiler?](#q351)
- [352: How do you use the TypeScript Compiler API?](#q352)
- [353: How do you get compile errors programmatically?](#q353)
- [354: What are custom transformers?](#q354)
- [355: What is a language service plugin?](#q355)
- [356: How do you find out why type checking is slow?](#q356)
- [357: What are common causes of slow type checking?](#q357)
- [358: What does "Type instantiation is excessively deep and possibly infinite" mean?](#q358)
- [359: What is isolatedDeclarations?](#q359)
- [360: What does the error "the inferred type of X cannot be named without a reference to Y" mean?](#q360)
- [361: How do you ship a package that supports both CommonJS and ESM with correct types?](#q361)
- [362: What is typesVersions in package.json?](#q362)
- [363: What is export as namespace?](#q363)
- [364: How can a namespace merge with a function, class or enum?](#q364)
- [365: How do you add a method to a built-in type like Array?](#q365)
- [366: What are using declarations?](#q366)
- [367: What is in the context object of a standard decorator?](#q367)
- [368: How does decorator metadata work in standard decorators?](#q368)
- [369: What is a decorator factory?](#q369)
- [370: In what order do decorators run?](#q370)
- [371: Why must assertion functions have an explicit type annotation?](#q371)
- [372: Why doesn't narrowing a generic value change the return type?](#q372)
- [373: What is the difference between T extends {} and an unconstrained T?](#q373)
- [374: Why does TypeScript sometimes infer from the wrong argument?](#q374)
- [375: How do excess property checks work with unions?](#q375)
- [376: How do you create an "exact" type that rejects extra properties?](#q376)
- [377: Why are template literal types sometimes too big to compute?](#q377)
- [378: How does Awaited handle thenables?](#q378)
- [379: How do recursive type aliases work and what are the limits?](#q379)
- [380: How can you get a type from a runtime schema?](#q380)
- [381: How do you share types between a frontend and backend?](#q381)
- [382: How do private class fields make classes nominal?](#q382)
- [383: How do you make sure an object handles every member of a union?](#q383)
- [384: What changed in how the in operator narrows unlisted properties?](#q384)
- [385: Can TypeScript narrow destructured discriminated unions?](#q385)
- [386: What is control flow analysis of aliased conditions?](#q386)
- [387: What do downlevelIteration and importHelpers do?](#q387)
- [388: What does useDefineForClassFields change?](#q388)
- [389: What is the declare modifier on class fields?](#q389)
- [390: What is erasableSyntaxOnly?](#q390)
- [391: What does module preserve do?](#q391)
- [392: What is the native TypeScript compiler (TypeScript 7)?](#q392)
- [393: Why can't a readonly array be passed where a mutable array is expected?](#q393)
- [394: What is the safest "any function" type?](#q394)
- [395: How do you type an empty object?](#q395)
- [396: Why do you sometimes see K & string in template literal types?](#q396)
- [397: How do you validate string formats with template literal types?](#q397)
- [398: How do you add types to a library's theme or config through module augmentation?](#q398)
- [399: What is the difference between declare var, declare let and declare const in a global declaration?](#q399)
- [400: How do you test your types?](#q400)
- [401: What is F-bounded polymorphism?](#q401)
- [402: What is the Prettify (or Simplify) type and why is it useful?](#q402)
- [403: How do you write a type for a deep merge of two objects?](#q403)
- [404: How do you convert all keys of a nested object to camelCase?](#q404)
- [405: How do you compute the length of a string literal type?](#q405)
- [406: How does inference work with multiple infer positions in a template literal?](#q406)
- [407: How does addEventListener know the event type from the event name?](#q407)
- [408: How do you type a Proxy?](#q408)
- [409: How do you build a typed dependency injection container?](#q409)
- [410: How do you type a state machine so only valid transitions are allowed?](#q410)
- [411: How do you get a single member from a discriminated union?](#q411)
- [412: How do you turn a discriminated union into a map of handlers?](#q412)
- [413: How do you type a reducer built from a handler map?](#q413)
- [414: How do you build a type-safe API client from a route map?](#q414)
- [415: Why does includes fail on a readonly array of literals and how do you fix it?](#q415)
- [416: How is Object.groupBy typed?](#q416)
- [417: What is the difference between unknown[] and any[] in generic constraints?](#q417)
- [418: Why can't you pass only some type arguments and let TypeScript infer the rest?](#q418)
- [419: What is higher order function type inference?](#q419)
- [420: How do you write a generic constraint that depends on another type parameter?](#q420)
- [421: How does a conditional type behave when the input is any or boolean?](#q421)
- [422: When does TypeScript defer a conditional type?](#q422)
- [423: Do mapped types with key remapping keep property modifiers?](#q423)
- [424: How do you keep generics when using forwardRef or memo?](#q424)
- [425: What is the difference between a script file and a module file in TypeScript?](#q425)
- [426: What does the moduleDetection option do?](#q426)
- [427: How do you migrate a large JavaScript codebase to TypeScript?](#q427)
- [428: What is "any infection" and how do you prevent it?](#q428)
- [429: What are type-aware lint rules?](#q429)
- [430: Can circular imports between type-only modules cause problems?](#q430)
- [431: How do you set up TypeScript in a monorepo?](#q431)
- [432: What changed with enums in TypeScript 5.0?](#q432)
- [433: What is intersection reduction to never?](#q433)
- [434: How does instanceof narrowing work with Symbol.hasInstance?](#q434)
- [435: What are iterator helper types in TypeScript 5.6?](#q435)
- [436: How do you type a function expression with a given type but keep its inferred return type?](#q436)
- [437: How do you write type-safe translation keys?](#q437)
- [438: How do you require the right parameters for a message with placeholders?](#q438)
- [439: How do you get the type of the whole Redux store state?](#q439)
- [440: Can a discriminated union use more than one discriminant or a boolean discriminant?](#q440)
- [441: Is a tuple assignable to an array and vice versa?](#q441)
- [442: What is the difference between an index signature [key: string] and a mapped type [K in string]?](#q442)
- [443: How do you type a generic factory that creates instances of classes with constructor arguments?](#q443)
- [444: How do you avoid the "excessive stack depth" error when comparing large generic types?](#q444)
- [445: How do you type a function that accepts an object and returns a version with some keys made optional?](#q445)
- [446: How do you write an "Opaque" type that only one module can create?](#q446)
- [447: Why does spreading an object skip the excess property check?](#q447)
- [448: What is the difference between IterableIterator and Generator?](#q448)
- [449: How do you require that a generic type argument is passed explicitly?](#q449)
- [450: How do you type a promisify function?](#q450)

---

<a id="easy"></a>

## Easy Questions (1-150)

<a id="q1"></a>

### 1: What is TypeScript?

TypeScript is a programming language made by Microsoft. It is JavaScript with static types added on top. You write `.ts` files, and the TypeScript compiler turns them into plain JavaScript that runs in the browser or in Node.js.

Any valid JavaScript code is also valid TypeScript code, so you can move a project over step by step.

```ts
let userName: string = "Anna";
let age: number = 30;
```

<a id="q2"></a>

### 2: Why would you use TypeScript instead of JavaScript?

The main reason is catching mistakes before the code runs. Some other reasons:

- Your editor can give better autocomplete and show errors as you type.
- Refactoring is safer because the compiler tells you what broke.
- Types act as documentation, so it is easier to understand what a function expects.
- It works well in big teams and big codebases.

```js
// JavaScript: no error until runtime
function getLength(s) {
  return s.length;
}
getLength(42); // undefined
```

```ts
// TypeScript: error at compile time
function getLength(s: string) {
  return s.length;
}
getLength(42); // Error: Argument of type 'number' is not assignable to parameter of type 'string'.
```

<a id="q3"></a>

### 3: Does the browser run TypeScript directly?

No. Browsers only understand JavaScript. TypeScript code has to be compiled (people often say "transpiled") to JavaScript first. Tools like `tsc`, esbuild, swc, Vite or Babel do this step.

Some newer runtimes like Deno and Bun can run `.ts` files directly, and recent Node.js versions can strip types too, but under the hood the types are still removed before the code runs.

<a id="q4"></a>

### 4: How do you install TypeScript?

Usually with npm:

```bash
# inside a project (recommended)
npm install --save-dev typescript

# or globally
npm install -g typescript
```

After that you can check the version:

```bash
npx tsc --version
```

<a id="q5"></a>

### 5: How do you compile a TypeScript file?

Use the `tsc` command:

```bash
npx tsc app.ts
```

This creates `app.js` next to it. If the project has a `tsconfig.json`, you can just run `npx tsc` and it will compile the whole project using the settings from that file.

<a id="q6"></a>

### 6: What is tsconfig.json?

It is the configuration file for the TypeScript compiler. It tells `tsc` which files to compile and which options to use. You can create one with:

```bash
npx tsc --init
```

A small example:

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "strict": true,
    "outDir": "./dist"
  },
  "include": ["src"]
}
```

<a id="q7"></a>

### 7: What are the basic types in TypeScript?

The most common ones are:

- `string`
- `number`
- `boolean`
- `null`
- `undefined`
- `bigint`
- `symbol`
- `any`
- `unknown`
- `void`
- `never`
- `object`

Plus arrays, tuples, enums and literal types.

```ts
let title: string = "Book";
let price: number = 9.99;
let inStock: boolean = true;
let big: bigint = 100n;
let id: symbol = Symbol("id");
```

<a id="q8"></a>

### 8: How do you declare a variable with a type?

Put a colon after the variable name and then the type:

```ts
let count: number = 0;
const message: string = "Hello";
let isDone: boolean = false;
```

<a id="q9"></a>

### 9: What is type inference?

Type inference means TypeScript figures out the type on its own, so you don't always have to write it.

```ts
let city = "Paris"; // inferred as string
city = 10; // Error: Type 'number' is not assignable to type 'string'.

const nums = [1, 2, 3]; // inferred as number[]
```

A good habit is to let TypeScript infer simple variable types and write types explicitly for function parameters and public APIs.

<a id="q10"></a>

### 10: What is the any type?

`any` turns off type checking for that value. You can do anything with it and the compiler will not complain.

```ts
let data: any = 5;
data = "text";
data.foo.bar(); // no error at compile time, but will crash at runtime
```

It is useful when migrating old JavaScript code, but you should try to avoid it, because it removes the whole point of using TypeScript.

<a id="q11"></a>

### 11: What is the unknown type?

`unknown` is the safe version of `any`. You can assign anything to it, but you can't use it until you check what it is.

```ts
let value: unknown = "hello";

value.toUpperCase(); // Error: 'value' is of type 'unknown'.

if (typeof value === "string") {
  value.toUpperCase(); // OK
}
```

<a id="q12"></a>

### 12: What is the difference between any and unknown?

- With `any` you can do anything, and TypeScript does not check it.
- With `unknown` you must narrow the type first (using `typeof`, `instanceof`, etc.) before using it.

```ts
function useAny(x: any) {
  x.toFixed(); // compiles
}

function useUnknown(x: unknown) {
  x.toFixed(); // Error
  if (typeof x === "number") x.toFixed(); // OK
}
```

Use `unknown` when you really don't know the type, for example data from `JSON.parse` or an API.

<a id="q13"></a>

### 13: What is the void type?

`void` is used as the return type of a function that does not return a value.

```ts
function logMessage(msg: string): void {
  console.log(msg);
}
```

<a id="q14"></a>

### 14: What is the never type?

`never` means a value that never happens. It is used for:

- functions that always throw an error,
- functions with an infinite loop,
- impossible cases after all options were handled.

```ts
function fail(message: string): never {
  throw new Error(message);
}
```

<a id="q15"></a>

### 15: What is the difference between void and never?

A function that returns `void` finishes normally but does not return anything useful. A function that returns `never` never finishes normally, because it throws or loops forever.

```ts
function a(): void {
  console.log("done"); // returns undefined
}

function b(): never {
  while (true) {}
}
```

<a id="q16"></a>

### 16: How do you define an array type?

There are two ways, and both mean the same thing:

```ts
let names: string[] = ["Ann", "Bob"];
let scores: Array<number> = [10, 20, 30];
```

Most people use `string[]` for simple types and `Array<...>` when the inner type is long.

<a id="q17"></a>

### 17: What is a tuple?

A tuple is an array with a fixed number of items, where each position has a known type.

```ts
let person: [string, number] = ["John", 25];

person[0].toUpperCase(); // string
person[1].toFixed(); // number

person = [25, "John"]; // Error: wrong order
```

Tuples are often used for returning more than one value from a function, like React's `useState`.

<a id="q18"></a>

### 18: What is an enum?

An enum is a set of named constants.

```ts
enum Direction {
  Up,
  Down,
  Left,
  Right,
}

let move: Direction = Direction.Up;
console.log(Direction.Up); // 0
console.log(Direction.Left); // 2
```

By default numeric enums start from 0 and go up by one.

<a id="q19"></a>

### 19: What is the difference between numeric and string enums?

In a numeric enum each member has a number value. In a string enum each member must be given a string value.

```ts
enum Status {
  Active, // 0
  Inactive, // 1
}

enum Color {
  Red = "RED",
  Green = "GREEN",
}
```

String enums are easier to debug, because when you log them you see `"RED"` instead of `0`.

<a id="q20"></a>

### 20: What is an interface?

An interface describes the shape of an object: what properties it has and what their types are.

```ts
interface User {
  id: number;
  name: string;
  email: string;
}

const user: User = {
  id: 1,
  name: "Sara",
  email: "sara@example.com",
};
```

If you miss a property or add a wrong type, TypeScript shows an error.

<a id="q21"></a>

### 21: What is a type alias?

A type alias gives a name to any type using the `type` keyword.

```ts
type ID = number | string;

type Point = {
  x: number;
  y: number;
};

let userId: ID = 123;
let p: Point = { x: 1, y: 2 };
```

<a id="q22"></a>

### 22: What are optional properties?

You mark a property as optional with `?`. It means the property may be missing.

```ts
interface Product {
  name: string;
  description?: string;
}

const p1: Product = { name: "Pen" }; // OK
const p2: Product = { name: "Pen", description: "Blue" }; // OK
```

The type of `description` becomes `string | undefined`.

<a id="q23"></a>

### 23: What are readonly properties?

A `readonly` property can be set when the object is created, but cannot be changed later.

```ts
interface Config {
  readonly apiUrl: string;
}

const config: Config = { apiUrl: "https://api.example.com" };
config.apiUrl = "other"; // Error: Cannot assign to 'apiUrl' because it is a read-only property.
```

<a id="q24"></a>

### 24: How do you add types to a function?

You add types to each parameter and, optionally, to the return value.

```ts
function add(a: number, b: number): number {
  return a + b;
}

const multiply = (a: number, b: number): number => a * b;
```

<a id="q25"></a>

### 25: What are optional parameters in functions?

Add `?` after the parameter name. Optional parameters must come after the required ones.

```ts
function greet(name: string, greeting?: string): string {
  return `${greeting ?? "Hello"}, ${name}`;
}

greet("Tom"); // "Hello, Tom"
greet("Tom", "Hi"); // "Hi, Tom"
```

<a id="q26"></a>

### 26: What are default parameters?

A default parameter gets a value if the caller does not pass one. TypeScript infers the type from the default value.

```ts
function createUser(name: string, role = "user") {
  return { name, role };
}

createUser("Ann"); // role is "user"
createUser("Ann", "admin"); // role is "admin"
```

<a id="q27"></a>

### 27: What are rest parameters?

Rest parameters collect any number of arguments into an array.

```ts
function sum(...numbers: number[]): number {
  return numbers.reduce((total, n) => total + n, 0);
}

sum(1, 2, 3); // 6
```

<a id="q28"></a>

### 28: What is a union type?

A union type means a value can be one of several types. You write it with `|`.

```ts
let id: number | string;

id = 10; // OK
id = "abc"; // OK
id = true; // Error
```

<a id="q29"></a>

### 29: What is an intersection type?

An intersection type combines several types into one. The value must have all properties from all types. You write it with `&`.

```ts
type HasName = { name: string };
type HasAge = { age: number };

type Person = HasName & HasAge;

const p: Person = { name: "Lia", age: 22 };
```

<a id="q30"></a>

### 30: What are literal types?

A literal type is a type that allows only one exact value. They are mostly used together with unions.

```ts
type Size = "small" | "medium" | "large";

let shirt: Size = "medium"; // OK
shirt = "huge"; // Error
```

You can also use number and boolean literals, like `1 | 2 | 3`.

<a id="q31"></a>

### 31: What is type assertion?

Type assertion tells the compiler "trust me, I know the type of this value". It does not change anything at runtime.

```ts
const input = document.getElementById("email") as HTMLInputElement;
console.log(input.value);
```

There is also an older syntax using angle brackets, which does not work in `.tsx` files:

```ts
const input2 = <HTMLInputElement>document.getElementById("email");
```

<a id="q32"></a>

### 32: What is the difference between let, const and var in TypeScript?

It works the same as in JavaScript:

- `var` is function scoped and can be redeclared.
- `let` is block scoped and can be reassigned.
- `const` is block scoped and cannot be reassigned.

TypeScript adds one more thing: with `const`, primitive values get a literal type.

```ts
let a = "hello"; // type: string
const b = "hello"; // type: "hello"
```

<a id="q33"></a>

### 33: What is the difference between null and undefined in TypeScript?

- `undefined` means a variable was declared but no value was given.
- `null` means "no value" and is set on purpose.

With `strictNullChecks` turned on, you can't assign `null` or `undefined` to other types unless you say so:

```ts
let name: string = null; // Error with strictNullChecks

let middleName: string | null = null; // OK
```

<a id="q34"></a>

### 34: What is the strict mode in TypeScript?

`"strict": true` in `tsconfig.json` turns on a group of stricter checks, such as:

- `noImplicitAny`
- `strictNullChecks`
- `strictFunctionTypes`
- `strictBindCallApply`
- `strictPropertyInitialization`
- `alwaysStrict`
- `useUnknownInCatchVariables`

It is recommended for all new projects because it catches many more bugs.

<a id="q35"></a>

### 35: What does noImplicitAny do?

When it is on, TypeScript shows an error if it can't figure out a type and would fall back to `any`.

```ts
// with noImplicitAny: true
function log(value) {
  // Error: Parameter 'value' implicitly has an 'any' type.
  console.log(value);
}
```

To fix it you add a type: `function log(value: string)`.

<a id="q36"></a>

### 36: What is the object type?

`object` means any non-primitive value: objects, arrays, functions. It does not allow `string`, `number`, `boolean`, `null`, etc.

```ts
let a: object = { x: 1 }; // OK
let b: object = [1, 2]; // OK
let c: object = "text"; // Error
```

It is rarely used in practice because you can't access any properties on it. Usually you write a specific shape instead.

<a id="q37"></a>

### 37: What is the difference between object, Object and {}?

- `object` is any non-primitive value.
- `Object` (capital O) and `{}` both mean "any value except `null` and `undefined`". Even strings and numbers are allowed.

```ts
let x: {} = "hello"; // OK
let y: Object = 42; // OK
let z: object = 42; // Error
```

In most code you should avoid all three and write the real shape of the object.

<a id="q38"></a>

### 38: How do you type an object inline?

You can write the shape directly without making an interface:

```ts
function printUser(user: { name: string; age: number }) {
  console.log(user.name, user.age);
}

printUser({ name: "Mia", age: 28 });
```

<a id="q39"></a>

### 39: What is a class in TypeScript?

A class is a blueprint for creating objects. TypeScript classes are JavaScript classes with type annotations and some extra features like access modifiers.

```ts
class Car {
  brand: string;

  constructor(brand: string) {
    this.brand = brand;
  }

  drive(): void {
    console.log(`${this.brand} is driving`);
  }
}

const car = new Car("Toyota");
car.drive();
```

<a id="q40"></a>

### 40: What are access modifiers in TypeScript?

There are three:

- `public`: accessible from anywhere. This is the default.
- `private`: accessible only inside the same class.
- `protected`: accessible inside the class and its subclasses.

```ts
class Account {
  public owner: string;
  private balance: number;
  protected type: string;

  constructor(owner: string, balance: number) {
    this.owner = owner;
    this.balance = balance;
    this.type = "basic";
  }
}

const acc = new Account("Ann", 100);
acc.owner; // OK
acc.balance; // Error
```

<a id="q41"></a>

### 41: What is the constructor in a class?

The constructor is a special method that runs when you create a new object with `new`. It is used to set initial values.

```ts
class Point {
  x: number;
  y: number;

  constructor(x: number, y: number) {
    this.x = x;
    this.y = y;
  }
}

const p = new Point(3, 4);
```

<a id="q42"></a>

### 42: What are parameter properties?

It is a shortcut. If you add an access modifier (or `readonly`) to a constructor parameter, TypeScript creates and assigns the property for you.

```ts
// long version
class User {
  name: string;
  constructor(name: string) {
    this.name = name;
  }
}

// short version
class User2 {
  constructor(
    public name: string,
    private age: number,
  ) {}
}

const u = new User2("Tom", 30);
console.log(u.name); // "Tom"
```

<a id="q43"></a>

### 43: How does inheritance work in TypeScript?

Use the `extends` keyword. The child class gets all properties and methods of the parent. Call `super()` in the constructor to run the parent constructor.

```ts
class Animal {
  constructor(public name: string) {}
  move() {
    console.log(`${this.name} moves`);
  }
}

class Dog extends Animal {
  bark() {
    console.log("Woof!");
  }
}

const d = new Dog("Rex");
d.move(); // "Rex moves"
d.bark(); // "Woof!"
```

<a id="q44"></a>

### 44: How does a class implement an interface?

Use the `implements` keyword. The class must have all the members from the interface.

```ts
interface Printable {
  print(): void;
}

class Invoice implements Printable {
  print() {
    console.log("Printing invoice...");
  }
}
```

If the class misses `print`, you get a compile error.

<a id="q45"></a>

### 45: What is an abstract class?

An abstract class is a base class that can't be created with `new`. It can have normal methods and abstract methods. Abstract methods have no body and must be written in the child class.

```ts
abstract class Shape {
  abstract getArea(): number;

  describe() {
    console.log(`Area is ${this.getArea()}`);
  }
}

class Square extends Shape {
  constructor(private side: number) {
    super();
  }
  getArea() {
    return this.side * this.side;
  }
}

new Shape(); // Error
new Square(4).describe(); // "Area is 16"
```

<a id="q46"></a>

### 46: What are static members in a class?

Static members belong to the class itself, not to its instances. You access them using the class name.

```ts
class MathHelper {
  static PI = 3.14;

  static circleArea(r: number) {
    return MathHelper.PI * r * r;
  }
}

MathHelper.circleArea(2); // 12.56
```

<a id="q47"></a>

### 47: What are getters and setters?

They let you run code when a property is read or written.

```ts
class Temperature {
  private _celsius = 0;

  get fahrenheit(): number {
    return this._celsius * 1.8 + 32;
  }

  set fahrenheit(value: number) {
    this._celsius = (value - 32) / 1.8;
  }
}

const t = new Temperature();
t.fahrenheit = 212;
console.log(t.fahrenheit); // 212
```

<a id="q48"></a>

### 48: What file extensions does TypeScript use?

- `.ts`: normal TypeScript files.
- `.tsx`: TypeScript files that contain JSX (React).
- `.d.ts`: declaration files that only contain types.
- `.mts` / `.cts`: TypeScript files that are compiled to ES modules (`.mjs`) or CommonJS (`.cjs`).

<a id="q49"></a>

### 49: What is a .d.ts file?

A `.d.ts` file is a declaration file. It contains only type information and no real code. It is used to describe the types of JavaScript code, for example a library written in plain JS.

```ts
// math.d.ts
export declare function add(a: number, b: number): number;
```

When you set `"declaration": true` in `tsconfig.json`, the compiler creates `.d.ts` files for your own code.

<a id="q50"></a>

### 50: What is a TypeScript Map file?

A map file (`.js.map`) is a source map. It connects the compiled JavaScript back to the original TypeScript code. Because of it, when you debug in the browser or in VS Code, you see your `.ts` code and correct line numbers instead of the generated JS.

You enable it in `tsconfig.json`:

```json
{
  "compilerOptions": {
    "sourceMap": true
  }
}
```

<a id="q51"></a>

### 51: Is TypeScript a superset of JavaScript?

Yes. Every JavaScript program is also a TypeScript program (it may have type errors, but the syntax is valid). TypeScript only adds things on top: type annotations, interfaces, enums, generics, access modifiers and so on.

<a id="q52"></a>

### 52: What are some downsides of TypeScript?

- You need a build step to turn TS into JS.
- There is a learning curve, especially for advanced types.
- Some third party libraries have poor or missing types.
- Types only exist at compile time, so they don't protect you from bad data at runtime (for example a wrong API response).
- Writing very complex types can make code hard to read.

<a id="q53"></a>

### 53: What is the difference between an interface and a type alias?

They are very similar, and for describing objects you can use either one. The main differences:

- An interface can only describe object shapes. A type alias can describe anything: unions, primitives, tuples, functions.
- Interfaces with the same name are merged together. Type aliases with the same name give an error.
- Interfaces use `extends`, type aliases use `&` to combine.

```ts
interface A {
  x: number;
}
interface A {
  y: number;
} // merged: A has x and y

type B = { x: number };
type B = { y: number }; // Error: Duplicate identifier 'B'.

type Id = string | number; // only possible with type
```

<a id="q54"></a>

### 54: How do you extend an interface?

Use `extends`. The new interface gets all properties of the old one.

```ts
interface Animal {
  name: string;
}

interface Dog extends Animal {
  breed: string;
}

const myDog: Dog = { name: "Max", breed: "Beagle" };
```

<a id="q55"></a>

### 55: Can an interface extend multiple interfaces?

Yes, separate them with commas.

```ts
interface CanFly {
  fly(): void;
}
interface CanSwim {
  swim(): void;
}

interface Duck extends CanFly, CanSwim {
  quack(): void;
}
```

<a id="q56"></a>

### 56: Can a class implement multiple interfaces?

Yes.

```ts
interface Walker {
  walk(): void;
}
interface Talker {
  talk(): void;
}

class Robot implements Walker, Talker {
  walk() {
    console.log("walking");
  }
  talk() {
    console.log("talking");
  }
}
```

A class can only `extend` one class, though.

<a id="q57"></a>

### 57: How do you describe a function type?

You can use a type alias or an interface.

```ts
type MathOp = (a: number, b: number) => number;

const add: MathOp = (a, b) => a + b;
const sub: MathOp = (a, b) => a - b;

interface Formatter {
  (value: string): string;
}

const upper: Formatter = (v) => v.toUpperCase();
```

<a id="q58"></a>

### 58: What is the typeof operator in TypeScript?

There are two uses of `typeof`:

1. In normal code it is the JavaScript operator that returns a string like `"string"` or `"number"`.
2. In a type position it gets the TypeScript type of a variable.

```ts
const settings = { theme: "dark", fontSize: 14 };

type Settings = typeof settings;
// { theme: string; fontSize: number }

if (typeof settings.fontSize === "number") {
  // JavaScript typeof
}
```

<a id="q59"></a>

### 59: What is type narrowing?

Narrowing is when TypeScript makes a type more specific inside a block of code, based on checks you write.

```ts
function format(value: string | number) {
  if (typeof value === "string") {
    return value.trim(); // value is string here
  }
  return value.toFixed(2); // value is number here
}
```

Common ways to narrow: `typeof`, `instanceof`, `in`, equality checks, truthiness checks and custom type guards.

<a id="q60"></a>

### 60: How do you use instanceof for narrowing?

`instanceof` checks if an object was created by a certain class.

```ts
class Cat {
  meow() {}
}
class Dog {
  bark() {}
}

function speak(pet: Cat | Dog) {
  if (pet instanceof Cat) {
    pet.meow();
  } else {
    pet.bark();
  }
}
```

<a id="q61"></a>

### 61: How do you use the in operator for narrowing?

The `in` operator checks if a property exists on an object.

```ts
type Fish = { swim: () => void };
type Bird = { fly: () => void };

function move(animal: Fish | Bird) {
  if ("swim" in animal) {
    animal.swim();
  } else {
    animal.fly();
  }
}
```

<a id="q62"></a>

### 62: What is optional chaining?

Optional chaining `?.` stops and returns `undefined` if the value before it is `null` or `undefined`, instead of throwing an error.

```ts
type User = { address?: { city?: string } };

const user: User = {};
console.log(user.address?.city); // undefined, no crash

const fn: (() => void) | undefined = undefined;
fn?.(); // only called if fn exists
```

<a id="q63"></a>

### 63: What is the nullish coalescing operator?

`??` returns the right side only when the left side is `null` or `undefined`.

```ts
const input: number | null = 0;

const a = input ?? 10; // 0
const b = input || 10; // 10, because 0 is falsy
```

It is safer than `||` when `0`, `""` or `false` are valid values.

<a id="q64"></a>

### 64: What is the non-null assertion operator?

The `!` after a value tells TypeScript "this is not null or undefined". It removes `null` and `undefined` from the type.

```ts
const button = document.querySelector("button")!;
button.addEventListener("click", () => {});
```

Be careful: if the value is actually `null`, the code will crash at runtime. Use it only when you are sure.

<a id="q65"></a>

### 65: How do you export and import in TypeScript?

TypeScript uses the same ES module syntax as JavaScript.

```ts
// math.ts
export function add(a: number, b: number) {
  return a + b;
}
export const PI = 3.14;

// app.ts
import { add, PI } from "./math";
```

<a id="q66"></a>

### 66: What is a default export?

Each module can have one default export. When you import it, you can give it any name.

```ts
// logger.ts
export default function log(msg: string) {
  console.log(msg);
}

// app.ts
import log from "./logger";
import myLogger from "./logger"; // same thing, different name
```

<a id="q67"></a>

### 67: How do you export and import only types?

You can use `export type` and `import type`. These imports are always removed from the compiled JavaScript.

```ts
// types.ts
export type User = { id: number; name: string };

// app.ts
import type { User } from "./types";

// or mixed
import { type User as U, someFunction } from "./types";
```

<a id="q68"></a>

### 68: What are generics?

Generics let you write code that works with many types while keeping type safety. You pass the type as a parameter, usually named `T`.

```ts
function identity<T>(value: T): T {
  return value;
}

identity<string>("hi"); // returns string
identity(42); // T inferred as number
```

Without generics you would have to use `any` and lose the type information.

<a id="q69"></a>

### 69: How do you write a generic interface?

```ts
interface ApiResponse<T> {
  data: T;
  status: number;
}

const res: ApiResponse<string[]> = {
  data: ["a", "b"],
  status: 200,
};
```

<a id="q70"></a>

### 70: How do you write a generic class?

```ts
class Box<T> {
  constructor(private value: T) {}

  getValue(): T {
    return this.value;
  }
}

const numberBox = new Box(10); // Box<number>
const stringBox = new Box("hello"); // Box<string>
```

<a id="q71"></a>

### 71: What is the keyof operator?

`keyof` gives you a union of the keys of a type.

```ts
interface Person {
  name: string;
  age: number;
}

type PersonKeys = keyof Person; // "name" | "age"

let key: PersonKeys = "name"; // OK
key = "email"; // Error
```

<a id="q72"></a>

### 72: What is an index signature?

An index signature is used when you don't know the property names in advance, but you know the types of keys and values.

```ts
interface Dictionary {
  [key: string]: number;
}

const wordCount: Dictionary = {
  hello: 2,
  world: 5,
};

wordCount["new"] = 1;
```

<a id="q73"></a>

### 73: What is the Record utility type?

`Record<K, V>` creates an object type with keys of type `K` and values of type `V`.

```ts
type Role = "admin" | "user" | "guest";

const permissions: Record<Role, string[]> = {
  admin: ["read", "write", "delete"],
  user: ["read", "write"],
  guest: ["read"],
};
```

If you miss one of the roles, TypeScript gives an error.

<a id="q74"></a>

### 74: What is the Partial utility type?

`Partial<T>` makes all properties of `T` optional. It is often used for update functions.

```ts
interface Todo {
  title: string;
  done: boolean;
}

function updateTodo(todo: Todo, changes: Partial<Todo>): Todo {
  return { ...todo, ...changes };
}

updateTodo({ title: "Shop", done: false }, { done: true });
```

<a id="q75"></a>

### 75: What is the Required utility type?

`Required<T>` makes all properties required, even the optional ones.

```ts
interface Options {
  host?: string;
  port?: number;
}

const full: Required<Options> = {
  host: "localhost",
  port: 3000,
}; // both must be present
```

<a id="q76"></a>

### 76: What is the Readonly utility type?

`Readonly<T>` makes all properties of `T` read only.

```ts
interface Point {
  x: number;
  y: number;
}

const origin: Readonly<Point> = { x: 0, y: 0 };
origin.x = 5; // Error
```

Note that it is shallow. Nested objects can still be changed.

<a id="q77"></a>

### 77: What is the Pick utility type?

`Pick<T, K>` creates a new type with only the chosen keys from `T`.

```ts
interface User {
  id: number;
  name: string;
  email: string;
  password: string;
}

type PublicUser = Pick<User, "id" | "name">;
// { id: number; name: string }
```

<a id="q78"></a>

### 78: What is the Omit utility type?

`Omit<T, K>` creates a new type with all keys from `T` except the ones you list.

```ts
interface User {
  id: number;
  name: string;
  password: string;
}

type SafeUser = Omit<User, "password">;
// { id: number; name: string }
```

<a id="q79"></a>

### 79: How do you make an array read only?

Use `readonly` before the array type, or `ReadonlyArray<T>`.

```ts
const nums: readonly number[] = [1, 2, 3];
nums.push(4); // Error: Property 'push' does not exist on type 'readonly number[]'.
nums[0] = 10; // Error

const names: ReadonlyArray<string> = ["a", "b"];
```

<a id="q80"></a>

### 80: What does as const do?

`as const` tells TypeScript to use the most specific type possible. Strings become literal types, arrays become read only tuples and object properties become `readonly`.

```ts
const colors = ["red", "green"]; // string[]
const colors2 = ["red", "green"] as const; // readonly ["red", "green"]

const config = { mode: "dark" } as const;
// { readonly mode: "dark" }
```

It is useful for lists of fixed values.

<a id="q81"></a>

### 81: How do you type a callback function?

Write the function type for the parameter.

```ts
function fetchData(callback: (data: string, error?: Error) => void) {
  callback("result");
}

fetchData((data) => {
  console.log(data.toUpperCase());
});
```

<a id="q82"></a>

### 82: How do you type a Promise?

Use `Promise<T>`, where `T` is the type of the value it resolves with.

```ts
function wait(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function getNumber(): Promise<number> {
  return Promise.resolve(42);
}
```

<a id="q83"></a>

### 83: How do you type an async function?

An async function always returns a Promise, so its return type is `Promise<T>`.

```ts
interface Post {
  id: number;
  title: string;
}

async function getPost(id: number): Promise<Post> {
  const res = await fetch(`/api/posts/${id}`);
  return res.json();
}
```

<a id="q84"></a>

### 84: What is the type of the error in a catch block?

By default it is `any`. If `useUnknownInCatchVariables` is on (included in `strict`), it is `unknown`. So you need to check it before using it.

```ts
try {
  JSON.parse("bad json");
} catch (err) {
  if (err instanceof Error) {
    console.log(err.message);
  } else {
    console.log("Unknown error", err);
  }
}
```

<a id="q85"></a>

### 85: What is the declare keyword?

`declare` tells TypeScript that something exists, but its code is somewhere else (for example a global variable added by a script tag). No JavaScript is generated for it.

```ts
declare const API_KEY: string;

console.log(API_KEY); // TypeScript knows the type, no error
```

<a id="q86"></a>

### 86: What are @types packages?

Many JavaScript libraries are not written in TypeScript. The community writes type definitions for them, and they are published on npm under the `@types` scope.

```bash
npm install lodash
npm install --save-dev @types/lodash
```

After installing, TypeScript automatically picks up the types.

<a id="q87"></a>

### 87: What is DefinitelyTyped?

DefinitelyTyped is a big GitHub repository with type definitions for thousands of JavaScript libraries. All the `@types/...` packages on npm come from it.

<a id="q88"></a>

### 88: What does the target option do in tsconfig?

`target` sets which version of JavaScript the compiler outputs. For example `ES5` will turn arrow functions and classes into older code, while `ES2022` keeps modern syntax.

```json
{
  "compilerOptions": {
    "target": "ES2020"
  }
}
```

<a id="q89"></a>

### 89: What are outDir and rootDir?

- `rootDir` is the folder where your source `.ts` files live.
- `outDir` is the folder where the compiled `.js` files go.

```json
{
  "compilerOptions": {
    "rootDir": "./src",
    "outDir": "./dist"
  }
}
```

<a id="q90"></a>

### 90: How do you run the compiler in watch mode?

Use the `--watch` (or `-w`) flag. The compiler keeps running and recompiles when files change.

```bash
npx tsc --watch
```

<a id="q91"></a>

### 91: What does the noEmit option do?

With `noEmit`, `tsc` only checks types and does not create any JavaScript files. This is common when another tool (Vite, esbuild, Babel, Next.js) does the actual compiling.

```bash
npx tsc --noEmit
```

<a id="q92"></a>

### 92: What does noEmitOnError do?

By default TypeScript still creates JavaScript files even if there are type errors. With `noEmitOnError: true`, it won't output anything when there are errors.

```json
{
  "compilerOptions": {
    "noEmitOnError": true
  }
}
```

<a id="q93"></a>

### 93: What is allowJs?

`allowJs` lets you include `.js` files in a TypeScript project. This is useful when you migrate a project slowly from JavaScript to TypeScript.

```json
{
  "compilerOptions": {
    "allowJs": true,
    "checkJs": true
  }
}
```

`checkJs` also reports type errors in those `.js` files.

<a id="q94"></a>

### 94: What is ts-node?

`ts-node` is a tool that runs TypeScript files directly in Node.js without compiling them first by hand.

```bash
npx ts-node src/index.ts
```

Similar tools are `tsx` and the newer built-in type stripping in Node.js.

<a id="q95"></a>

### 95: What is the TypeScript Playground?

It is an online editor at typescriptlang.org/play. You can write TypeScript, see the compiled JavaScript, see errors and try different compiler options. It is great for testing small ideas or sharing examples.

<a id="q96"></a>

### 96: How do you type DOM elements?

TypeScript ships with types for the DOM, like `HTMLElement`, `HTMLInputElement`, `HTMLButtonElement`.

```ts
const input = document.querySelector<HTMLInputElement>("#name");

if (input) {
  console.log(input.value);
}
```

`querySelector` returns `Element | null`, so you need to check for `null` or use a generic as above.

<a id="q97"></a>

### 97: How do you type DOM events?

Use event types like `MouseEvent`, `KeyboardEvent`, `Event`.

```ts
const button = document.querySelector("button");

button?.addEventListener("click", (event: MouseEvent) => {
  console.log(event.clientX, event.clientY);
});

document.addEventListener("keydown", (e) => {
  console.log(e.key); // e is inferred as KeyboardEvent
});
```

<a id="q98"></a>

### 98: What is the symbol type?

`symbol` is a primitive type for unique values. Every `Symbol()` call creates a new value that is not equal to any other.

```ts
const id1 = Symbol("id");
const id2 = Symbol("id");

console.log(id1 === id2); // false

const obj = { [id1]: 123 };
```

<a id="q99"></a>

### 99: What is the bigint type?

`bigint` is used for very large integers that `number` can't store safely. You create them with `n` at the end or with `BigInt()`.

```ts
const big: bigint = 9007199254740993n;
const other = BigInt(100);

const sum = big + other; // OK
const mix = big + 1; // Error: can't mix bigint and number
```

You need `target` of `ES2020` or later.

<a id="q100"></a>

### 100: What happens to types after compilation?

They are removed. This is called type erasure. The compiled JavaScript has no interfaces, no type aliases and no type annotations.

```ts
// TypeScript
interface User {
  name: string;
}
const u: User = { name: "Ann" };
```

```js
// Compiled JavaScript
const u = { name: "Ann" };
```

Because of this, you can't check an interface at runtime.

<a id="q101"></a>

### 101: Can TypeScript check types at runtime?

No. TypeScript only checks types at compile time. If you get data from an API or user input, TypeScript can't know if it really matches your type. For runtime checks you write your own validation or use a library like Zod, Yup, io-ts or Valibot.

```ts
import { z } from "zod";

const User = z.object({ name: z.string(), age: z.number() });

const data = User.parse(JSON.parse(input)); // throws if the shape is wrong
```

<a id="q102"></a>

### 102: What is structural typing?

TypeScript compares types by their shape, not by their name. If two types have the same properties, they are compatible. This is sometimes called "duck typing".

```ts
interface Point {
  x: number;
  y: number;
}

class Coordinate {
  constructor(
    public x: number,
    public y: number,
  ) {}
}

const p: Point = new Coordinate(1, 2); // OK, same shape
```

Languages like Java or C# use nominal typing, where the names must match.

<a id="q103"></a>

### 103: Can you use instanceof with an interface?

No. Interfaces don't exist at runtime, so there is nothing to check against.

```ts
interface Animal {
  name: string;
}

function check(x: unknown) {
  if (x instanceof Animal) {
  } // Error: 'Animal' only refers to a type
}
```

You need a type guard that checks the properties instead, or use a class.

<a id="q104"></a>

### 104: How do you narrow with a truthiness check?

If you check a value in an `if`, TypeScript removes `null` and `undefined` (and other falsy types) inside the block.

```ts
function printName(name: string | null) {
  if (name) {
    console.log(name.toUpperCase()); // name is string
  } else {
    console.log("No name");
  }
}
```

Be careful, an empty string `""` is also falsy.

<a id="q105"></a>

### 105: How do you narrow with equality checks?

Comparing values with `===` or `!==` also narrows types.

```ts
function compare(a: string | number, b: string | boolean) {
  if (a === b) {
    // the only common type is string
    console.log(a.toUpperCase(), b.toUpperCase());
  }
}

function check(value: string | null) {
  if (value !== null) {
    value.length; // string
  }
}
```

<a id="q106"></a>

### 106: How do you type an array of objects?

```ts
interface Product {
  id: number;
  name: string;
}

const products: Product[] = [
  { id: 1, name: "Phone" },
  { id: 2, name: "Laptop" },
];

// inline version
const tags: { label: string; color: string }[] = [];
```

<a id="q107"></a>

### 107: What is the difference between (string | number)[] and string[] | number[]?

- `(string | number)[]` is one array that can hold strings and numbers mixed together.
- `string[] | number[]` is either an array of only strings or an array of only numbers.

```ts
let a: (string | number)[] = [1, "two", 3]; // OK
let b: string[] | number[] = [1, "two"]; // Error
let c: string[] | number[] = [1, 2]; // OK
```

<a id="q108"></a>

### 108: How are array methods like map and filter typed?

TypeScript knows the types of built-in array methods, so the result types are inferred for you.

```ts
const nums = [1, 2, 3];

const doubled = nums.map((n) => n * 2); // number[]
const asText = nums.map((n) => `#${n}`); // string[]
const evens = nums.filter((n) => n % 2 === 0); // number[]
const total = nums.reduce((sum, n) => sum + n, 0); // number
```

<a id="q109"></a>

### 109: How do you type object destructuring?

Put the type after the whole destructuring pattern, not after each variable.

```ts
function showUser({ name, age }: { name: string; age: number }) {
  console.log(name, age);
}

const { x, y }: { x: number; y: number } = { x: 1, y: 2 };
```

A common mistake is writing `{ name: string }` and thinking it's a type. Inside a destructuring pattern, that syntax means renaming.

<a id="q110"></a>

### 110: How does the spread operator work with types?

TypeScript understands spread and combines the types.

```ts
const base = { id: 1, name: "Ann" };
const extra = { admin: true };

const user = { ...base, ...extra };
// { admin: boolean; id: number; name: string }

const arr1 = [1, 2];
const arr2 = ["a"];
const mixed = [...arr1, ...arr2]; // (string | number)[]
```

<a id="q111"></a>

### 111: What is the Function type and should you use it?

`Function` is a built-in type that matches any function. It is not recommended because it doesn't say anything about parameters or return value, and calls return `any`.

```ts
let fn: Function = () => 42;
fn("anything", 1, 2); // no error, returns any

// better
let fn2: () => number = () => 42;
```

<a id="q112"></a>

### 112: What is the difference between method and property syntax in an interface?

Both describe a function, but they are written differently.

```ts
interface Counter {
  increment(): void; // method syntax
  decrement: () => void; // property syntax
}
```

In most cases they work the same. With `strictFunctionTypes`, the property syntax is checked more strictly for parameter types, so some people prefer it.

<a id="q113"></a>

### 113: Can an interface have optional methods?

Yes, the same way as optional properties.

```ts
interface Plugin {
  name: string;
  init(): void;
  destroy?(): void;
}

function unload(p: Plugin) {
  p.destroy?.(); // must check, since it may not exist
}
```

<a id="q114"></a>

### 114: What is method overriding?

A child class can replace a method of its parent class with its own version.

```ts
class Animal {
  speak() {
    console.log("Some sound");
  }
}

class Cat extends Animal {
  speak() {
    console.log("Meow");
  }
}

new Cat().speak(); // "Meow"
```

<a id="q115"></a>

### 115: What is the override keyword?

`override` marks that a method replaces a parent method. If the parent method does not exist (for example it was renamed), you get an error. Turn on `noImplicitOverride` to require it.

```ts
class Base {
  greet() {}
}

class Child extends Base {
  override greet() {} // OK
  override hello() {} // Error: This member cannot have an 'override' modifier because it is not declared in the base class.
}
```

<a id="q116"></a>

### 116: What does super do?

`super` refers to the parent class. You use it to call the parent constructor or a parent method.

```ts
class Person {
  constructor(public name: string) {}
  intro() {
    return `I am ${this.name}`;
  }
}

class Employee extends Person {
  constructor(
    name: string,
    public role: string,
  ) {
    super(name); // must be called before using "this"
  }

  intro() {
    return `${super.intro()} and I work as ${this.role}`;
  }
}
```

<a id="q117"></a>

### 117: What is the difference between private and #private?

- `private` is a TypeScript keyword. It is only checked at compile time. After compiling, the property is a normal public property in JavaScript.
- `#name` is a JavaScript private field. It is really private at runtime too.

```ts
class A {
  private secret = 1;
  #realSecret = 2;
}

const a = new A();
(a as any).secret; // works at runtime: 1
(a as any).#realSecret; // syntax error, not reachable at all
```

<a id="q118"></a>

### 118: Can a class property be readonly?

Yes. A `readonly` property can only be set where it is declared or inside the constructor.

```ts
class Order {
  readonly id: number;

  constructor(id: number) {
    this.id = id; // OK
  }

  change() {
    this.id = 5; // Error
  }
}
```

<a id="q119"></a>

### 119: What is the difference between an optional property and a property of type T | undefined?

With `?` the property can be left out completely. With `| undefined` the property must be written, but its value can be `undefined`.

```ts
interface A {
  name?: string;
}
interface B {
  name: string | undefined;
}

const a: A = {}; // OK
const b: B = {}; // Error: Property 'name' is missing
const b2: B = { name: undefined }; // OK
```

<a id="q120"></a>

### 120: How do you type a Map?

Use `Map<KeyType, ValueType>`.

```ts
const scores = new Map<string, number>();

scores.set("Ann", 90);
scores.set("Bob", "high"); // Error

const annScore = scores.get("Ann"); // number | undefined
```

<a id="q121"></a>

### 121: How do you type a Set?

Use `Set<T>`.

```ts
const ids = new Set<number>();

ids.add(1);
ids.add("2"); // Error

const tags = new Set(["a", "b"]); // Set<string> inferred
```

<a id="q122"></a>

### 122: What type does JSON.parse return?

It returns `any`. This means TypeScript will not check what you do with the result. It is better to give it a type, and ideally validate it.

```ts
interface Config {
  port: number;
}

const config = JSON.parse('{"port": 3000}') as Config;

// safer: treat it as unknown and check it
const raw: unknown = JSON.parse(text);
```

<a id="q123"></a>

### 123: How do you type a fetch response?

`response.json()` returns `Promise<any>`, so you add the type yourself.

```ts
interface Todo {
  id: number;
  title: string;
  completed: boolean;
}

async function getTodo(id: number): Promise<Todo> {
  const res = await fetch(`https://jsonplaceholder.typicode.com/todos/${id}`);
  if (!res.ok) throw new Error("Request failed");
  return (await res.json()) as Todo;
}
```

Remember this is not checked at runtime.

<a id="q124"></a>

### 124: What type does setTimeout return?

In the browser it returns a `number`. In Node.js it returns a `Timeout` object. To write code that works in both, use `ReturnType`:

```ts
let timer: ReturnType<typeof setTimeout>;

timer = setTimeout(() => {}, 1000);
clearTimeout(timer);
```

<a id="q125"></a>

### 125: How do you type Promise.all?

TypeScript infers it for you. The result is a tuple with the types in the same order.

```ts
const [user, posts] = await Promise.all([
  fetchUser(), // Promise<User>
  fetchPosts(), // Promise<Post[]>
]);
// user: User, posts: Post[]
```

<a id="q126"></a>

### 126: What is the ReturnType utility type?

`ReturnType<T>` gets the return type of a function type.

```ts
function createUser() {
  return { id: 1, name: "Ann", active: true };
}

type User = ReturnType<typeof createUser>;
// { id: number; name: string; active: boolean }
```

<a id="q127"></a>

### 127: What is the Parameters utility type?

`Parameters<T>` gets the parameter types of a function as a tuple.

```ts
function sendEmail(to: string, subject: string, urgent: boolean) {}

type EmailArgs = Parameters<typeof sendEmail>;
// [to: string, subject: string, urgent: boolean]

type FirstArg = EmailArgs[0]; // string
```

<a id="q128"></a>

### 128: What is the NonNullable utility type?

`NonNullable<T>` removes `null` and `undefined` from a type.

```ts
type MaybeName = string | null | undefined;

type Name = NonNullable<MaybeName>; // string
```

<a id="q129"></a>

### 129: What is the Exclude utility type?

`Exclude<T, U>` removes from the union `T` all members that can be assigned to `U`.

```ts
type Status = "active" | "inactive" | "banned";

type AllowedStatus = Exclude<Status, "banned">;
// "active" | "inactive"
```

<a id="q130"></a>

### 130: What is the Extract utility type?

`Extract<T, U>` keeps only the members of union `T` that can be assigned to `U`. It is the opposite of `Exclude`.

```ts
type Mixed = string | number | boolean;

type OnlyText = Extract<Mixed, string>; // string

type Event = "click" | "scroll" | "keydown" | "keyup";
type KeyEvents = Extract<Event, "keydown" | "keyup" | "focus">; // "keydown" | "keyup"
```

<a id="q131"></a>

### 131: What is the Awaited utility type?

`Awaited<T>` gives you the type a Promise resolves to. It also unwraps nested promises.

```ts
type A = Awaited<Promise<string>>; // string
type B = Awaited<Promise<Promise<number>>>; // number

async function load() {
  return { ok: true };
}

type LoadResult = Awaited<ReturnType<typeof load>>; // { ok: boolean }
```

<a id="q132"></a>

### 132: What is the difference between Omit and Exclude?

- `Omit` works on object types and removes properties.
- `Exclude` works on union types and removes members.

```ts
type User = { id: number; name: string; age: number };
type NoAge = Omit<User, "age">; // { id: number; name: string }

type Letters = "a" | "b" | "c";
type NoC = Exclude<Letters, "c">; // "a" | "b"
```

<a id="q133"></a>

### 133: What is a const enum?

A `const enum` is removed completely at compile time. Every place where it is used gets replaced by the actual value. This makes the output smaller.

```ts
const enum Level {
  Low = 1,
  High = 2,
}

const l = Level.High;
// compiled: const l = 2;
```

The downside is that some build tools (like Babel or esbuild with `isolatedModules`) don't handle them well across files.

<a id="q134"></a>

### 134: What is enum reverse mapping?

For numeric enums, TypeScript creates a mapping both ways: from name to value and from value to name.

```ts
enum Color {
  Red,
  Green,
}

console.log(Color.Red); // 0
console.log(Color[0]); // "Red"
```

String enums do not have reverse mapping.

<a id="q135"></a>

### 135: Should you use an enum or a union of string literals?

Both work. Many teams prefer string literal unions because:

- they have no runtime code,
- they are plain strings, so they are easy to use with JSON and APIs,
- they work well with all build tools.

```ts
// union
type Theme = "light" | "dark";
function setTheme(t: Theme) {}
setTheme("dark");

// enum
enum ThemeEnum {
  Light = "light",
  Dark = "dark",
}
function setTheme2(t: ThemeEnum) {}
setTheme2(ThemeEnum.Dark);
```

Enums are handy when you want a named object of values to loop over or to share between files.

<a id="q136"></a>

### 136: What is a template literal type?

It builds string types using the same backtick syntax as JavaScript template strings.

```ts
type Size = "sm" | "md" | "lg";
type ClassName = `btn-${Size}`;
// "btn-sm" | "btn-md" | "btn-lg"

let cls: ClassName = "btn-md"; // OK
cls = "btn-xl"; // Error
```

<a id="q137"></a>

### 137: Why does Object.keys return string[] and not keyof T?

Because of structural typing, an object can have more properties than its type says. So TypeScript can't promise that the keys are only the ones in the type.

```ts
interface Point {
  x: number;
  y: number;
}

const p: Point = { x: 1, y: 2 };
const keys = Object.keys(p); // string[]

// if you are sure, you can cast
const typedKeys = Object.keys(p) as (keyof Point)[];
```

<a id="q138"></a>

### 138: What does the lib option do in tsconfig?

`lib` tells TypeScript which built-in type definitions to include, for example DOM types or newer JavaScript features.

```json
{
  "compilerOptions": {
    "lib": ["ES2022", "DOM", "DOM.Iterable"]
  }
}
```

If you write Node.js code, you usually leave out `DOM` and install `@types/node`.

<a id="q139"></a>

### 139: What does the module option do in tsconfig?

`module` controls what kind of module code the compiler outputs, for example `commonjs` (`require`/`module.exports`) or `esnext` (`import`/`export`). For modern Node.js projects `nodenext` is common.

```json
{
  "compilerOptions": {
    "module": "nodenext"
  }
}
```

<a id="q140"></a>

### 140: What are include, exclude and files in tsconfig?

They control which files are part of the project.

```json
{
  "include": ["src/**/*"],
  "exclude": ["node_modules", "**/*.test.ts"],
  "files": ["src/global.d.ts"]
}
```

- `files`: an exact list of files.
- `include`: patterns of files to add.
- `exclude`: patterns to skip from `include`.

<a id="q141"></a>

### 141: What does esModuleInterop do?

It makes importing CommonJS modules with default import syntax work correctly.

```ts
// without esModuleInterop
import * as express from "express";

// with esModuleInterop: true
import express from "express";
```

It is turned on by default when you run `tsc --init`.

<a id="q142"></a>

### 142: What does skipLibCheck do?

`skipLibCheck: true` skips type checking of all `.d.ts` files, including those in `node_modules`. It makes compiling faster and avoids errors coming from library types that you can't fix.

<a id="q143"></a>

### 143: What does resolveJsonModule do?

It allows you to import `.json` files and get types for them.

```ts
// tsconfig: "resolveJsonModule": true
import config from "./config.json";

console.log(config.port); // typed based on the JSON content
```

<a id="q144"></a>

### 144: What are baseUrl and paths in tsconfig?

They let you create import aliases instead of long relative paths.

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@utils/*": ["src/utils/*"]
    }
  }
}
```

```ts
import { formatDate } from "@utils/date"; // instead of "../../../utils/date"
```

Note that `tsc` does not rewrite these paths in the output, so your bundler or runtime also needs to know about them.

<a id="q145"></a>

### 145: How do you type props in a React component?

Write an interface or type for the props and use it in the function parameters.

```tsx
interface ButtonProps {
  label: string;
  onClick: () => void;
  disabled?: boolean;
}

function Button({ label, onClick, disabled = false }: ButtonProps) {
  return (
    <button onClick={onClick} disabled={disabled}>
      {label}
    </button>
  );
}
```

<a id="q146"></a>

### 146: How do you type useState in React?

Most of the time the type is inferred from the initial value. When the initial value is `null` or an empty array, pass the type yourself.

```tsx
const [count, setCount] = useState(0); // number

const [user, setUser] = useState<User | null>(null);

const [items, setItems] = useState<string[]>([]);
```

<a id="q147"></a>

### 147: How do you type events in React?

React has its own event types, like `React.ChangeEvent` and `React.MouseEvent`.

```tsx
function SearchBox() {
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    console.log(e.target.value);
  };

  const handleClick = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault();
  };

  return (
    <>
      <input onChange={handleChange} />
      <button onClick={handleClick}>Search</button>
    </>
  );
}
```

<a id="q148"></a>

### 148: How do you create a custom error class?

Extend the built-in `Error` class.

```ts
class NotFoundError extends Error {
  constructor(public resource: string) {
    super(`${resource} not found`);
    this.name = "NotFoundError";
  }
}

try {
  throw new NotFoundError("User");
} catch (e) {
  if (e instanceof NotFoundError) {
    console.log(e.resource); // "User"
  }
}
```

<a id="q149"></a>

### 149: Can a class be used as a type?

Yes. When you declare a class, you also get a type with the same name that describes its instances.

```ts
class Book {
  constructor(public title: string) {}
}

function printBook(book: Book) {
  console.log(book.title);
}

printBook(new Book("Dune"));
printBook({ title: "Dune" }); // also OK, same shape
```

<a id="q150"></a>

### 150: How do you use ESLint with TypeScript?

Use `typescript-eslint`. It provides a parser for TypeScript syntax and many TypeScript-specific rules.

```bash
npm install --save-dev eslint typescript-eslint
```

```js
// eslint.config.js
import tseslint from "typescript-eslint";

export default tseslint.config(...tseslint.configs.recommended);
```

TSLint, the older tool, is deprecated.

[Back to top](#table-of-contents)

<a id="moderate"></a>

## Moderate Questions (151-300)

<a id="q151"></a>

### 151: What are generic constraints?

A constraint limits which types can be used for a generic. You write it with `extends`.

```ts
function getLength<T extends { length: number }>(item: T): number {
  return item.length;
}

getLength("hello"); // OK
getLength([1, 2, 3]); // OK
getLength(42); // Error: number has no 'length'
```

<a id="q152"></a>

### 152: How do you use keyof with generics to safely read a property?

You can make a second generic that must be one of the keys of the first.

```ts
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

const user = { name: "Ann", age: 30 };

getProperty(user, "name"); // string
getProperty(user, "age"); // number
getProperty(user, "email"); // Error
```

The return type `T[K]` is exactly the type of that property.

<a id="q153"></a>

### 153: Can generics have default types?

Yes, like default values for function parameters.

```ts
interface ApiResponse<T = unknown> {
  data: T;
  error?: string;
}

const a: ApiResponse = { data: 123 }; // T is unknown
const b: ApiResponse<string> = { data: "hello" }; // T is string
```

<a id="q154"></a>

### 154: How does TypeScript infer generic types?

It looks at the arguments you pass and picks the type that fits.

```ts
function pair<A, B>(a: A, b: B): [A, B] {
  return [a, b];
}

const p = pair("x", 10); // [string, number]
```

If inference picks something too wide or too narrow, you can pass the types yourself: `pair<string, number>("x", 10)`.

<a id="q155"></a>

### 155: What are indexed access types?

You can get the type of a property using square brackets, the same way you read a property value.

```ts
interface User {
  id: number;
  profile: {
    email: string;
    tags: string[];
  };
}

type Profile = User["profile"]; // { email: string; tags: string[] }
type Email = User["profile"]["email"]; // string
type Tag = User["profile"]["tags"][number]; // string
```

<a id="q156"></a>

### 156: How do you get the type of an array element?

Use `[number]` as an indexed access.

```ts
const roles = ["admin", "editor", "viewer"] as const;

type Role = (typeof roles)[number]; // "admin" | "editor" | "viewer"

type Item = string[][number]; // string
```

This is a common trick to create a union type from a constant array.

<a id="q157"></a>

### 157: What are mapped types?

A mapped type creates a new type by going over the keys of another type.

```ts
type Flags<T> = {
  [K in keyof T]: boolean;
};

interface Features {
  darkMode: string;
  beta: number;
}

type FeatureFlags = Flags<Features>;
// { darkMode: boolean; beta: boolean }
```

Built-in types like `Partial`, `Readonly` and `Record` are written with mapped types.

<a id="q158"></a>

### 158: How do mapped type modifiers work?

You can add or remove `readonly` and `?` with `+` and `-`. If you write just `readonly` or `?`, it means `+`.

```ts
type Mutable<T> = {
  -readonly [K in keyof T]: T[K];
};

type AllRequired<T> = {
  [K in keyof T]-?: T[K];
};

type Frozen = { readonly a: number; b?: string };

type M = Mutable<Frozen>; // { a: number; b?: string }
type R = AllRequired<Frozen>; // { readonly a: number; b: string }
```

<a id="q159"></a>

### 159: What is key remapping in mapped types?

With `as` you can change key names in a mapped type.

```ts
type Getters<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};

interface Person {
  name: string;
  age: number;
}

type PersonGetters = Getters<Person>;
// { getName: () => string; getAge: () => number }
```

If you map a key to `never`, that key is removed. This is how you can filter keys.

<a id="q160"></a>

### 160: What are conditional types?

A conditional type picks one of two types based on a condition. The syntax looks like the ternary operator.

```ts
type IsString<T> = T extends string ? "yes" : "no";

type A = IsString<"hello">; // "yes"
type B = IsString<42>; // "no"
```

They are mostly used with generics to build types that depend on other types.

<a id="q161"></a>

### 161: What is the infer keyword?

`infer` is used inside a conditional type to pull out a type from another type and give it a name.

```ts
type ElementType<T> = T extends (infer U)[] ? U : never;

type A = ElementType<string[]>; // string
type B = ElementType<number>; // never

type GetReturn<T> = T extends (...args: any[]) => infer R ? R : never;

type C = GetReturn<() => boolean>; // boolean
```

<a id="q162"></a>

### 162: What are distributive conditional types?

When a conditional type is used on a union and the checked type is a plain type parameter, the condition runs for each member of the union separately.

```ts
type ToArray<T> = T extends any ? T[] : never;

type Result = ToArray<string | number>;
// string[] | number[]   (not (string | number)[])
```

To stop this, wrap both sides in square brackets:

```ts
type ToArrayNoDist<T> = [T] extends [any] ? T[] : never;

type Result2 = ToArrayNoDist<string | number>; // (string | number)[]
```

<a id="q163"></a>

### 163: What is a discriminated union?

It is a union of object types where each type has a common property with a literal value (the "discriminant" or "tag"). TypeScript uses this property to narrow the type.

```ts
type Shape =
  | { kind: "circle"; radius: number }
  | { kind: "square"; size: number }
  | { kind: "rectangle"; width: number; height: number };

function area(shape: Shape): number {
  switch (shape.kind) {
    case "circle":
      return Math.PI * shape.radius ** 2;
    case "square":
      return shape.size ** 2;
    case "rectangle":
      return shape.width * shape.height;
  }
}
```

<a id="q164"></a>

### 164: How do you do exhaustiveness checking?

Use `never` in the default branch. If someone adds a new member to the union and forgets to handle it, the code won't compile.

```ts
type Status = "loading" | "success" | "error";

function message(status: Status): string {
  switch (status) {
    case "loading":
      return "Loading...";
    case "success":
      return "Done!";
    case "error":
      return "Something went wrong";
    default: {
      const check: never = status;
      return check;
    }
  }
}
```

If you add `"idle"` to `Status`, you get an error: `Type 'string' is not assignable to type 'never'`.

<a id="q165"></a>

### 165: What is a user-defined type guard?

It is a function whose return type is `value is SomeType`. When it returns `true`, TypeScript narrows the value to that type.

```ts
interface Fish {
  swim(): void;
}
interface Bird {
  fly(): void;
}

function isFish(pet: Fish | Bird): pet is Fish {
  return (pet as Fish).swim !== undefined;
}

function move(pet: Fish | Bird) {
  if (isFish(pet)) {
    pet.swim();
  } else {
    pet.fly();
  }
}
```

TypeScript trusts you here. If your check is wrong, the types will be wrong too.

<a id="q166"></a>

### 166: What are assertion functions?

An assertion function throws if a condition is false. Its return type uses `asserts`. After calling it, TypeScript narrows the type.

```ts
function assertIsString(value: unknown): asserts value is string {
  if (typeof value !== "string") {
    throw new Error("Not a string");
  }
}

function assert(condition: unknown, msg?: string): asserts condition {
  if (!condition) throw new Error(msg);
}

function handle(input: unknown) {
  assertIsString(input);
  input.toUpperCase(); // input is string here
}
```

<a id="q167"></a>

### 167: What is function overloading?

Overloading lets one function have several call signatures. You write the signatures first and then one implementation that handles all cases.

```ts
function format(value: string): string;
function format(value: number, decimals: number): string;
function format(value: string | number, decimals?: number): string {
  if (typeof value === "number") {
    return value.toFixed(decimals);
  }
  return value.trim();
}

format("  hi  "); // OK
format(3.1415, 2); // OK
format(3.1415); // Error: no overload matches
```

The implementation signature is not visible to callers.

<a id="q168"></a>

### 168: When should you use overloads instead of a union parameter?

Use overloads when the return type depends on the input type, or when certain parameters only make sense together. If the return type is the same for all inputs, a union is simpler.

```ts
// union is enough
function len(x: string | any[]): number {
  return x.length;
}

// overloads give better return types
function parse(x: string): number;
function parse(x: string[]): number[];
function parse(x: string | string[]) {
  return Array.isArray(x) ? x.map(Number) : Number(x);
}

const n = parse("5"); // number
const arr = parse(["1", "2"]); // number[]
```

<a id="q169"></a>

### 169: How do you type the this parameter in a function?

You can add a fake first parameter named `this`. It is removed in the compiled code and only used for type checking.

```ts
interface Counter {
  count: number;
}

function increment(this: Counter) {
  this.count++;
}

const c = { count: 0, increment };
c.increment(); // OK

const fn = c.increment;
fn(); // Error: The 'this' context of type 'void' is not assignable
```

<a id="q170"></a>

### 170: What is the polymorphic this type?

Using `this` as a return type means "the type of the current instance". It is useful for method chaining in classes that will be extended.

```ts
class QueryBuilder {
  protected parts: string[] = [];

  where(cond: string): this {
    this.parts.push(`WHERE ${cond}`);
    return this;
  }
}

class MySqlBuilder extends QueryBuilder {
  limit(n: number): this {
    this.parts.push(`LIMIT ${n}`);
    return this;
  }
}

new MySqlBuilder().where("id > 1").limit(10); // works, where() returns MySqlBuilder
```

<a id="q171"></a>

### 171: What is declaration merging?

When TypeScript sees several declarations with the same name, it can merge them into one. The most common case is interfaces.

```ts
interface Box {
  height: number;
}

interface Box {
  width: number;
}

const b: Box = { height: 10, width: 20 };
```

Namespaces can also merge with classes, functions and enums.

<a id="q172"></a>

### 172: What is module augmentation?

Module augmentation lets you add types to an existing module, for example a library.

```ts
// express.d.ts
import "express";

declare module "express" {
  interface Request {
    user?: { id: string; role: string };
  }
}
```

```ts
app.get("/me", (req, res) => {
  res.json(req.user?.id); // no error now
});
```

<a id="q173"></a>

### 173: How do you add a property to the global window object?

Use `declare global` inside a module file.

```ts
// global.d.ts
export {};

declare global {
  interface Window {
    analytics: {
      track(event: string): void;
    };
  }
}
```

```ts
window.analytics.track("page_view"); // typed
```

The `export {}` makes the file a module, which is required for `declare global`.

<a id="q174"></a>

### 174: What are namespaces?

Namespaces are TypeScript's older way to group code under one name. They compile into a JavaScript object.

```ts
namespace Validation {
  export function isEmail(s: string) {
    return s.includes("@");
  }
}

Validation.isEmail("a@b.com");
```

Today ES modules are the recommended way to organize code. Namespaces are still seen in declaration files and old codebases.

<a id="q175"></a>

### 175: What is the difference between namespaces and modules?

- A module is a file with `import` or `export`. Each file has its own scope. It is the standard JavaScript way.
- A namespace is a TypeScript feature that groups code inside a file (or across files) into one global object.

Use modules for new code. Namespaces are mostly useful to describe types of old global libraries in `.d.ts` files.

<a id="q176"></a>

### 176: What are triple-slash directives?

They are special comments at the top of a file that give instructions to the compiler.

```ts
/// <reference types="node" />
/// <reference path="./globals.d.ts" />
/// <reference lib="es2022" />
```

They were common before ES modules. Today they are mainly used in declaration files.

<a id="q177"></a>

### 177: How do you declare types for a JavaScript module that has no types?

Create a `.d.ts` file and use `declare module`.

```ts
// types/legacy-lib.d.ts
declare module "legacy-lib" {
  export function doSomething(input: string): number;
  export const version: string;
}
```

If you just want the error to go away and don't care about types:

```ts
declare module "legacy-lib";
// everything imported from it will be any
```

<a id="q178"></a>

### 178: How do you import images or CSS files in TypeScript?

TypeScript doesn't know what an `.svg` or `.css` import returns, so you declare it with a wildcard module.

```ts
// assets.d.ts
declare module "*.svg" {
  const src: string;
  export default src;
}

declare module "*.module.css" {
  const classes: Record<string, string>;
  export default classes;
}
```

Tools like Vite and Next.js already include these declarations.

<a id="q179"></a>

### 179: What is excess property checking?

When you pass an object literal directly to something with a known type, TypeScript reports extra properties that are not in the type.

```ts
interface Options {
  color: string;
}

function paint(o: Options) {}

paint({ color: "red", size: 10 }); // Error: Object literal may only specify known properties

const opts = { color: "red", size: 10 };
paint(opts); // OK, not a fresh literal
```

The check only happens for fresh object literals. This catches typos like `colour` instead of `color`.

<a id="q180"></a>

### 180: What is the satisfies operator?

`satisfies` checks that a value matches a type, but keeps the more specific type that TypeScript inferred.

```ts
type Colors = Record<string, string | [number, number, number]>;

const palette = {
  red: [255, 0, 0],
  green: "#00ff00",
} satisfies Colors;

palette.green.toUpperCase(); // OK, TypeScript knows it's a string
palette.red[0]; // OK, tuple

const palette2: Colors = { red: [255, 0, 0], green: "#00ff00" };
palette2.green.toUpperCase(); // Error: could be a tuple
```

<a id="q181"></a>

### 181: What is the difference between satisfies, a type annotation and as?

- `const x: T = value` checks the value and the variable gets type `T`. Extra details are lost.
- `const x = value satisfies T` checks the value, and the variable keeps the inferred type.
- `const x = value as T` does not really check. It just tells the compiler to use `T`, which can hide mistakes.

```ts
type User = { name: string };

const a: User = { name: "x" }; // type User
const b = { name: "x" } satisfies User; // type { name: string }
const c = {} as User; // compiles, but name is missing
const d = {} satisfies User; // Error
```

<a id="q182"></a>

### 182: What is type widening?

Widening is when TypeScript picks a more general type than the literal value. It happens with `let` and with mutable object properties.

```ts
const a = "hi"; // "hi"
let b = "hi"; // string (widened)

const obj = { mode: "dark" }; // { mode: string } (widened)

function setMode(m: "dark" | "light") {}
setMode(obj.mode); // Error: string is not assignable to "dark" | "light"
```

Fix it with `as const`, an explicit type, or `satisfies`.

<a id="q183"></a>

### 183: What is the InstanceType utility type?

`InstanceType<T>` gets the type of the object that a class constructor creates.

```ts
class Logger {
  log(msg: string) {}
}

type LoggerInstance = InstanceType<typeof Logger>; // Logger

function create<T extends new (...args: any[]) => any>(C: T): InstanceType<T> {
  return new C();
}

const l = create(Logger); // Logger
```

<a id="q184"></a>

### 184: What is the ConstructorParameters utility type?

It gets the constructor parameter types of a class as a tuple.

```ts
class Point {
  constructor(
    public x: number,
    public y: number,
  ) {}
}

type PointArgs = ConstructorParameters<typeof Point>; // [x: number, y: number]
```

<a id="q185"></a>

### 185: How do you type a class constructor as a parameter?

Use a construct signature: `new (...args) => Type`.

```ts
interface Animal {
  speak(): string;
}

class Dog implements Animal {
  speak() {
    return "woof";
  }
}

function makeAnimal(ctor: new () => Animal): Animal {
  return new ctor();
}

makeAnimal(Dog);
```

<a id="q186"></a>

### 186: What is a private constructor and when is it used?

A private constructor means the class can't be created with `new` from outside. It is used for the singleton pattern or for classes with factory methods.

```ts
class Database {
  private static instance: Database;

  private constructor() {}

  static getInstance(): Database {
    if (!Database.instance) {
      Database.instance = new Database();
    }
    return Database.instance;
  }
}

const db = Database.getInstance();
new Database(); // Error
```

<a id="q187"></a>

### 187: What is the difference between an abstract class and an interface?

- An interface only describes a shape. It has no code and does not exist at runtime.
- An abstract class can have real code (method bodies, properties, constructor) and exists at runtime. It can also have abstract members that subclasses must implement.
- A class can implement many interfaces but extend only one class.

Use an interface for a contract. Use an abstract class when you want to share code between subclasses.

<a id="q188"></a>

### 188: What does strictPropertyInitialization do?

It makes sure every class property is set in the constructor or has a default value.

```ts
class User {
  name: string; // Error: Property 'name' has no initializer
  age = 0; // OK
  email: string;

  constructor() {
    this.email = "a@b.com"; // OK
  }
}
```

<a id="q189"></a>

### 189: What is the definite assignment assertion?

Writing `!` after a property or variable name tells TypeScript that it will be assigned, even if TypeScript can't see it.

```ts
class Component {
  element!: HTMLElement; // set later in init()

  init() {
    this.element = document.createElement("div");
  }
}

let value!: number;
setup();
console.log(value * 2);

function setup() {
  value = 10;
}
```

<a id="q190"></a>

### 190: What does noUncheckedIndexedAccess do?

It adds `undefined` to the type when you read from an index signature or array by index. Without it, TypeScript assumes the value is always there.

```ts
const list: string[] = [];
const first = list[0];
// without the option: string
// with the option:    string | undefined

const map: Record<string, number> = {};
map["x"].toFixed(); // with the option: Error, object is possibly undefined
```

It is not part of `strict`, but many teams turn it on.

<a id="q191"></a>

### 191: What does exactOptionalPropertyTypes do?

With this option, an optional property can be missing, but you can't explicitly set it to `undefined` unless the type says so.

```ts
interface Settings {
  theme?: "light" | "dark";
}

const s: Settings = { theme: undefined };
// with exactOptionalPropertyTypes: Error
// fix: theme?: "light" | "dark" | undefined
```

<a id="q192"></a>

### 192: What does strictFunctionTypes do?

It checks function parameter types contravariantly. In simple words, you can't assign a function that accepts a narrower type where a function that accepts a wider type is expected.

```ts
type Handler = (x: string | number) => void;

const onlyString = (x: string) => x.toUpperCase();

const h: Handler = onlyString; // Error with strictFunctionTypes
// h(5) would crash because onlyString can't handle numbers
```

Methods declared with method syntax are not checked this way, for backward compatibility.

<a id="q193"></a>

### 193: Why can a function that returns a value be assigned to a type that returns void?

A `void` return type in a function type means "the return value will be ignored", not "must return nothing". This lets you pass functions like `push` to `forEach`.

```ts
const result: number[] = [];

[1, 2, 3].forEach((n) => result.push(n)); // push returns number, still OK

type Fn = () => void;
const f: Fn = () => 42; // OK
```

But if you write `function f(): void { return 42; }` directly, that is an error.

<a id="q194"></a>

### 194: What are optional and rest elements in tuples?

Tuples can have optional elements with `?` and rest elements with `...`.

```ts
type Point = [number, number, number?];
const p2: Point = [1, 2];
const p3: Point = [1, 2, 3];

type StringThenNumbers = [string, ...number[]];
const a: StringThenNumbers = ["sum", 1, 2, 3];
```

<a id="q195"></a>

### 195: What are labeled tuple elements?

You can give names to tuple positions. The names don't change the type, but they make code and editor hints easier to read.

```ts
type Range = [start: number, end: number];

function createRange(...args: Range) {}
// editor shows: createRange(start: number, end: number)
```

<a id="q196"></a>

### 196: How do you get the keys of an enum as a type?

Use `keyof typeof` with the enum.

```ts
enum Color {
  Red = "RED",
  Blue = "BLUE",
}

type ColorKey = keyof typeof Color; // "Red" | "Blue"

function fromKey(key: ColorKey): Color {
  return Color[key];
}
```

<a id="q197"></a>

### 197: What is the difference between `Record<string, T>` and an index signature?

They mean almost the same thing. `Record<string, T>` is just a shorter way to write `{ [key: string]: T }`.

The difference is that `Record` also works with a union of literal keys, which makes all of them required:

```ts
type Grades = Record<"math" | "art", number>;
// { math: number; art: number }

type Any = { [key: string]: number };
// any string key is allowed, none are required
```

An index signature, on the other hand, can be mixed with known properties in the same type.

<a id="q198"></a>

### 198: When should you use a Map instead of a plain object?

Use `Map` when:

- keys are not strings (objects, numbers you don't want converted),
- you add and remove keys a lot,
- you need to know the size quickly or keep insertion order for any key type.

```ts
const cache = new Map<object, string>();
const key = { id: 1 };
cache.set(key, "data");
```

Use a plain object (or `Record`) for fixed shapes and data that will be turned into JSON.

<a id="q199"></a>

### 199: What are the intrinsic string manipulation types?

TypeScript has four built-in types for changing string literal types:

```ts
type A = Uppercase<"hello">; // "HELLO"
type B = Lowercase<"HELLO">; // "hello"
type C = Capitalize<"hello">; // "Hello"
type D = Uncapitalize<"Hello">; // "hello"

type EventName<T extends string> = `on${Capitalize<T>}`;
type Click = EventName<"click">; // "onClick"
```

<a id="q200"></a>

### 200: How do you write a generic React component?

Add a type parameter to the function and use it in props.

```tsx
interface ListProps<T> {
  items: T[];
  renderItem: (item: T) => React.ReactNode;
}

function List<T>({ items, renderItem }: ListProps<T>) {
  return (
    <ul>
      {items.map((item, i) => (
        <li key={i}>{renderItem(item)}</li>
      ))}
    </ul>
  );
}

<List items={[{ id: 1, name: "A" }]} renderItem={(u) => u.name} />;
// u is inferred as { id: number; name: string }
```

In an arrow function inside a `.tsx` file, write `<T,>` so it's not mistaken for JSX.

<a id="q201"></a>

### 201: How do you type useRef in React?

It depends on how you use it.

```tsx
// DOM element: pass null, React sets it later
const inputRef = useRef<HTMLInputElement>(null);
inputRef.current?.focus();

// mutable value you change yourself
const timerRef = useRef<number | undefined>(undefined);
timerRef.current = window.setTimeout(() => {}, 1000);
```

<a id="q202"></a>

### 202: How do you type useReducer in React?

Type the state and the actions. A discriminated union works well for actions.

```tsx
type State = { count: number };

type Action =
  | { type: "increment" }
  | { type: "decrement" }
  | { type: "set"; value: number };

function reducer(state: State, action: Action): State {
  switch (action.type) {
    case "increment":
      return { count: state.count + 1 };
    case "decrement":
      return { count: state.count - 1 };
    case "set":
      return { count: action.value };
  }
}

const [state, dispatch] = useReducer(reducer, { count: 0 });
dispatch({ type: "set", value: 5 }); // OK
dispatch({ type: "set" }); // Error: value is missing
```

<a id="q203"></a>

### 203: How do you type React Context?

Give the type to `createContext`. A common pattern is to use `null` as the default and write a hook that checks it.

```tsx
interface AuthContextValue {
  user: string | null;
  login: (name: string) => void;
}

const AuthContext = createContext<AuthContextValue | null>(null);

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used inside AuthProvider");
  return ctx; // AuthContextValue, no null
}
```

<a id="q204"></a>

### 204: What is the difference between ReactNode, ReactElement and JSX.Element?

- `ReactNode` is anything React can render: elements, strings, numbers, `null`, `undefined`, booleans, arrays of these. Use it for `children`.
- `ReactElement` is an object created by JSX or `React.createElement`.
- `JSX.Element` is basically `ReactElement<any, any>`.

```tsx
interface CardProps {
  title: string;
  children: React.ReactNode;
}

function Card({ title, children }: CardProps) {
  return (
    <div>
      <h2>{title}</h2>
      {children}
    </div>
  );
}
```

<a id="q205"></a>

### 205: How do you make a React component accept all props of a native HTML element?

Use `React.ComponentProps<"button">` (or `ComponentPropsWithoutRef`) and extend it.

```tsx
interface ButtonProps extends React.ComponentProps<"button"> {
  variant?: "primary" | "secondary";
}

function Button({ variant = "primary", ...rest }: ButtonProps) {
  return <button className={variant} {...rest} />;
}

<Button type="submit" disabled onClick={() => {}} />; // all native props work
```

<a id="q206"></a>

### 206: How do you type Express request handlers?

Express types are in `@types/express`. `Request` takes generics for params, response body, request body and query.

```ts
import express, { Request, Response } from "express";

interface CreateUserBody {
  name: string;
  email: string;
}

const app = express();

app.post("/users", (req: Request<{}, {}, CreateUserBody>, res: Response) => {
  const { name, email } = req.body; // typed
  res.status(201).json({ name, email });
});

app.get("/users/:id", (req: Request<{ id: string }>, res) => {
  res.send(req.params.id); // string
});
```

<a id="q207"></a>

### 207: How do you type environment variables in Node.js?

Extend the `ProcessEnv` interface from `@types/node`.

```ts
// env.d.ts
declare global {
  namespace NodeJS {
    interface ProcessEnv {
      NODE_ENV: "development" | "production" | "test";
      DATABASE_URL: string;
    }
  }
}
export {};
```

This only helps with types. The variables can still be missing at runtime, so it is a good idea to validate them on startup.

<a id="q208"></a>

### 208: What are decorators in TypeScript?

Decorators are functions that you attach to classes, methods, properties or accessors with `@`. They can change or add behavior. Frameworks like Angular and NestJS use them a lot.

```ts
function logged(originalMethod: any, context: ClassMethodDecoratorContext) {
  const name = String(context.name);
  return function (this: any, ...args: any[]) {
    console.log(`Calling ${name} with`, args);
    return originalMethod.call(this, ...args);
  };
}

class Calculator {
  @logged
  add(a: number, b: number) {
    return a + b;
  }
}

new Calculator().add(2, 3); // logs: Calling add with [2, 3]
```

<a id="q209"></a>

### 209: What is the difference between experimentalDecorators and the new standard decorators?

- `experimentalDecorators` is the old TypeScript-only version. Angular, NestJS, TypeORM and others were built on it. It also supports parameter decorators and `emitDecoratorMetadata`.
- Since TypeScript 5.0, standard decorators (based on the TC39 proposal) work without any flag. They have a different signature: they receive the value and a `context` object.

```ts
// old style (experimentalDecorators: true)
function OldLog(target: any, key: string, descriptor: PropertyDescriptor) {}

// new style
function NewLog(value: Function, context: ClassMethodDecoratorContext) {}
```

The two styles are not compatible, so check what your framework expects.

<a id="q210"></a>

### 210: How do you write a class decorator?

A class decorator receives the class. It can return a new class to replace it.

```ts
function sealed<T extends new (...args: any[]) => any>(
  target: T,
  context: ClassDecoratorContext,
) {
  Object.seal(target);
  Object.seal(target.prototype);
}

@sealed
class Report {
  title = "Q1";
}
```

<a id="q211"></a>

### 211: What does emitDecoratorMetadata do?

Together with `experimentalDecorators`, it makes the compiler save type information (like constructor parameter types) as metadata. Libraries read it with `reflect-metadata`. This is how NestJS and Angular know what to inject into a constructor.

```ts
@Injectable()
class UserService {
  constructor(private repo: UserRepository) {}
  // the framework reads metadata to know it needs a UserRepository
}
```

It does not work with the new standard decorators.

<a id="q212"></a>

### 212: How do you type a generator function?

Use `Generator<YieldType, ReturnType, NextType>`. Often TypeScript infers it.

```ts
function* idGenerator(): Generator<number, void, unknown> {
  let id = 1;
  while (true) {
    yield id++;
  }
}

const ids = idGenerator();
ids.next().value; // number | void
```

<a id="q213"></a>

### 213: How do you make a class iterable?

Implement `[Symbol.iterator]()` that returns an iterator.

```ts
class NumberRange implements Iterable<number> {
  constructor(
    private start: number,
    private end: number,
  ) {}

  *[Symbol.iterator](): Iterator<number> {
    for (let i = this.start; i <= this.end; i++) {
      yield i;
    }
  }
}

for (const n of new NumberRange(1, 3)) {
  console.log(n); // 1, 2, 3
}
```

<a id="q214"></a>

### 214: How do you type an async generator?

Use `AsyncGenerator<T>`, and loop over it with `for await`.

```ts
async function* fetchPages(): AsyncGenerator<string[]> {
  let page = 1;
  while (page <= 3) {
    const res = await fetch(`/api/items?page=${page}`);
    yield (await res.json()) as string[];
    page++;
  }
}

for await (const items of fetchPages()) {
  console.log(items.length);
}
```

<a id="q215"></a>

### 215: What does isolatedModules do?

It makes sure every file can be compiled on its own, without knowing about other files. Tools like Babel, esbuild and swc compile one file at a time, so they need this.

With it on, TypeScript reports code that can't work this way, for example re-exporting a type without `export type`:

```ts
import { User } from "./types";
export { User }; // Error with isolatedModules if User is only a type

export type { User } from "./types"; // OK
```

<a id="q216"></a>

### 216: What does verbatimModuleSyntax do?

With this option, TypeScript keeps your imports and exports exactly as you wrote them, except the ones marked with `type`. So you must use `import type` for types.

```ts
import { type User, createUser } from "./user"; // User import is removed, createUser stays
import type { Config } from "./config"; // removed completely
```

It replaces the older options `importsNotUsedAsValues` and `preserveValueImports`.

<a id="q217"></a>

### 217: What does moduleResolution do?

It decides how TypeScript finds the file for an import like `import x from "lib"`. Common values:

- `node10` (older `node`): the old Node.js CommonJS way.
- `node16` / `nodenext`: follows modern Node.js rules, including `package.json` `exports` and the need for file extensions in ESM.
- `bundler`: for projects using Vite, webpack, esbuild and similar. Supports `exports` but doesn't require file extensions.

```json
{
  "compilerOptions": {
    "module": "esnext",
    "moduleResolution": "bundler"
  }
}
```

<a id="q218"></a>

### 218: What are project references?

Project references let you split a big codebase into smaller TypeScript projects that depend on each other. Each one has its own `tsconfig.json` and can be built separately, which makes builds faster.

```json
// tsconfig.json at the root
{
  "files": [],
  "references": [{ "path": "./packages/core" }, { "path": "./packages/app" }]
}
```

```json
// packages/core/tsconfig.json
{
  "compilerOptions": { "composite": true, "outDir": "dist" }
}
```

Build everything with `tsc --build` (or `tsc -b`).

<a id="q219"></a>

### 219: What does the incremental option do?

`incremental: true` saves information about the last build into a `.tsbuildinfo` file. Next time, TypeScript only rechecks files that changed, which makes builds faster.

```json
{
  "compilerOptions": {
    "incremental": true,
    "tsBuildInfoFile": "./.cache/tsbuildinfo"
  }
}
```

<a id="q220"></a>

### 220: How do you publish a TypeScript library with types?

Compile with `declaration: true` so `.d.ts` files are created, and point to them in `package.json`.

```json
{
  "name": "my-lib",
  "main": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "default": "./dist/index.js"
    }
  }
}
```

In `exports`, the `types` condition should come first.

<a id="q221"></a>

### 221: What is declarationMap?

`declarationMap: true` creates `.d.ts.map` files. With them, "Go to Definition" in the editor jumps to the original `.ts` source instead of the `.d.ts` file. Very useful in monorepos.

<a id="q222"></a>

### 222: What is the difference between @ts-ignore and @ts-expect-error?

Both hide the error on the next line.

- `@ts-ignore` hides it silently, even if there is no error.
- `@ts-expect-error` hides it, but if there is no error, TypeScript reports that the comment is not needed.

```ts
// @ts-expect-error: testing a wrong argument on purpose
add("1", 2);
```

`@ts-expect-error` is safer because you will notice when the problem is fixed and the comment can be removed.

<a id="q223"></a>

### 223: What do @ts-check and @ts-nocheck do?

- `// @ts-check` at the top of a `.js` file turns on type checking for that file.
- `// @ts-nocheck` at the top of a file turns off type checking for the whole file.

```js
// @ts-check
let count = 0;
count = "a"; // Error reported in the JS file
```

<a id="q224"></a>

### 224: Can you use TypeScript types in a JavaScript file?

Yes, with JSDoc comments. TypeScript understands them when `checkJs` or `// @ts-check` is on.

```js
// @ts-check

/**
 * @param {string} name
 * @param {number} [age]
 * @returns {string}
 */
function greet(name, age) {
  return `${name} ${age ?? ""}`;
}

/** @type {import("./types").User} */
const user = { id: 1, name: "Ann" };
```

Some libraries, like Svelte, use this approach to avoid a build step.

<a id="q225"></a>

### 225: What do noUnusedLocals and noUnusedParameters do?

They report variables and function parameters that are declared but never used.

```ts
function calc(a: number, b: number) {
  // Error on b with noUnusedParameters
  const temp = 5; // Error with noUnusedLocals
  return a * 2;
}
```

If you need to keep a parameter, start its name with `_` and it will be ignored: `(_b: number)`.

<a id="q226"></a>

### 226: What do noImplicitReturns and noFallthroughCasesInSwitch do?

- `noImplicitReturns` reports an error when some code paths of a function return a value and others don't.
- `noFallthroughCasesInSwitch` reports an error when a `case` in a `switch` has code but no `break` or `return`.

```ts
function getLabel(n: number) {
  // Error: Not all code paths return a value
  if (n > 0) return "positive";
}

switch (x) {
  case 1:
    doA(); // Error: Fallthrough case in switch
  case 2:
    doB();
    break;
}
```

<a id="q227"></a>

### 227: What does noPropertyAccessFromIndexSignature do?

It forces you to use bracket notation for properties that come from an index signature. This makes it clear in code that the property may not exist.

```ts
interface Env {
  NODE_ENV: string;
  [key: string]: string | undefined;
}

declare const env: Env;

env.NODE_ENV; // OK, declared property
env.API_KEY; // Error with the option on
env["API_KEY"]; // OK
```

<a id="q228"></a>

### 228: What is a double assertion and when is it needed?

TypeScript won't let you assert between two types that are clearly unrelated. You can get around it by going through `unknown` first.

```ts
const n = 42;
const s = n as string; // Error: conversion may be a mistake
const s2 = n as unknown as string; // compiles
```

It is a sign that something is wrong. Use it only in special cases, like tests or when working around a bad library type.

<a id="q229"></a>

### 229: What is PropertyKey?

`PropertyKey` is a built-in type alias for `string | number | symbol`, which are all the types that can be used as object keys.

```ts
function hasKey(obj: object, key: PropertyKey): boolean {
  return key in obj;
}

type K = keyof any; // also string | number | symbol
```

<a id="q230"></a>

### 230: What properties can you access on a union of object types?

Only properties that exist on every member of the union.

```ts
type Car = { wheels: number; brand: string };
type Boat = { sails: number; brand: string };

function info(v: Car | Boat) {
  v.brand; // OK, on both
  v.wheels; // Error: not on Boat
}
```

To use the other properties, narrow the type first (with `in` or a discriminant).

<a id="q231"></a>

### 231: What is the result of keyof on a union and on an intersection?

- `keyof (A | B)` gives only the keys that are in both. It's the common keys.
- `keyof (A & B)` gives all keys from both.

```ts
type A = { a: 1; shared: 1 };
type B = { b: 2; shared: 2 };

type K1 = keyof (A | B); // "shared"
type K2 = keyof (A & B); // "a" | "b" | "shared"
```

<a id="q232"></a>

### 232: How does Array.isArray narrow types?

`Array.isArray` is a built-in type guard. It narrows the value to an array type.

```ts
function toList(value: string | string[]): string[] {
  if (Array.isArray(value)) {
    return value; // string[]
  }
  return [value]; // string
}
```

<a id="q233"></a>

### 233: How do you use filter to remove null values with correct types?

Since TypeScript 5.5, simple filter callbacks are inferred as type guards automatically. In older versions, you write the type predicate yourself.

```ts
const items = ["a", null, "b", undefined];

// TS 5.5+
const clean = items.filter((x) => x != null); // string[]

// older versions
const clean2 = items.filter((x): x is string => x != null);
```

<a id="q234"></a>

### 234: Why is narrowing sometimes lost inside callbacks?

TypeScript can't be sure that a mutable variable didn't change between the check and the moment the callback runs.

```ts
let value: string | null = getValue();

if (value) {
  setTimeout(() => {
    value.length; // Error in older versions: value is possibly null
  });
}
```

Fixes: copy it to a `const` first, or use `const` from the start. TypeScript 5.4 improved this, and keeps narrowing in closures created after the last assignment.

```ts
const v = value;
if (v) {
  setTimeout(() => v.length); // OK
}
```

<a id="q235"></a>

### 235: How does control flow analysis work?

TypeScript follows your code line by line and tracks what type each variable has at each point, based on assignments, `if` checks, `return`, `throw` and so on.

```ts
function process(input: string | number | null) {
  if (input === null) return;
  // input: string | number

  if (typeof input === "number") {
    input = input.toString();
  }
  // input: string

  return input.toUpperCase();
}
```

<a id="q236"></a>

### 236: What is a unique symbol?

`unique symbol` is a subtype of `symbol` that stands for one specific symbol value. It is only allowed on `const` declarations and `readonly static` properties. It lets you use symbols as typed object keys.

```ts
const ID: unique symbol = Symbol("id");

interface Entity {
  [ID]: number;
}

const e: Entity = { [ID]: 1 };
e[ID]; // number
```

<a id="q237"></a>

### 237: Can index signatures use template literal patterns?

Yes, since TypeScript 4.4. You can also use `symbol` as the key type.

```ts
interface DataAttributes {
  [key: `data-${string}`]: string;
}

const attrs: DataAttributes = {
  "data-id": "1",
  "data-role": "button",
  "aria-label": "x", // Error
};
```

<a id="q238"></a>

### 238: Can a getter and setter have different types?

Yes, since TypeScript 5.1 they can be unrelated. Before that the getter type had to be assignable to the setter type.

```ts
class Field {
  #value = "";

  get value(): string {
    return this.#value;
  }

  set value(v: string | number) {
    this.#value = String(v);
  }
}

const f = new Field();
f.value = 42; // OK
f.value.length; // string
```

<a id="q239"></a>

### 239: What are static blocks in classes?

A `static { }` block runs once when the class is defined. It is used for more complex setup of static properties.

```ts
class Config {
  static values: Record<string, string>;

  static {
    Config.values = {};
    for (const [k, v] of Object.entries(process.env)) {
      if (k.startsWith("APP_") && v) Config.values[k] = v;
    }
  }
}
```

<a id="q240"></a>

### 240: What is the accessor keyword?

`accessor` creates a getter and setter with a hidden private field behind it. It was added for the standard decorators, which can then hook into get and set.

```ts
class Person {
  accessor name = "Ann";
}

// roughly the same as:
class Person2 {
  #name = "Ann";
  get name() {
    return this.#name;
  }
  set name(v) {
    this.#name = v;
  }
}
```

<a id="q241"></a>

### 241: What is an abstract construct signature?

`abstract new (...) => T` describes a constructor of an abstract class. A normal `new () => T` type does not accept an abstract class.

```ts
abstract class Shape {
  abstract area(): number;
}

function register(ctor: abstract new () => Shape) {}

register(Shape); // OK

function create(ctor: new () => Shape) {}
create(Shape); // Error: Cannot assign an abstract constructor type
```

<a id="q242"></a>

### 242: How do you write generic methods in a class?

A method can have its own type parameters, separate from the class.

```ts
class Collection<T> {
  constructor(private items: T[]) {}

  map<U>(fn: (item: T) => U): Collection<U> {
    return new Collection(this.items.map(fn));
  }

  toArray(): T[] {
    return this.items;
  }
}

const names = new Collection([1, 2]).map((n) => `#${n}`).toArray(); // string[]
```

<a id="q243"></a>

### 243: How do you type the static side of a class with an interface?

`implements` only checks the instance side. To check static members, describe the constructor in a separate interface and check the class against it.

```ts
interface Shape {
  area(): number;
}

interface ShapeConstructor {
  new (size: number): Shape;
  fromJSON(json: string): Shape;
}

class Square implements Shape {
  constructor(private size: number) {}
  area() {
    return this.size ** 2;
  }
  static fromJSON(json: string) {
    return new Square(JSON.parse(json).size);
  }
}

const ctor: ShapeConstructor = Square; // checks static side too
```

<a id="q244"></a>

### 244: What is a hybrid type?

An object that can be called like a function and also has properties.

```ts
interface Counter {
  (): number;
  count: number;
  reset(): void;
}

function createCounter(): Counter {
  const fn = (() => ++fn.count) as Counter;
  fn.count = 0;
  fn.reset = () => {
    fn.count = 0;
  };
  return fn;
}

const c = createCounter();
c(); // 1
c.count; // 1
c.reset();
```

<a id="q245"></a>

### 245: What are ReadonlyMap and ReadonlySet?

They are read only views of `Map` and `Set` with no `set`, `add`, `delete` or `clear` methods.

```ts
function printAll(users: ReadonlyMap<string, number>) {
  users.forEach((age, name) => console.log(name, age));
  users.set("x", 1); // Error
}

const tags: ReadonlySet<string> = new Set(["a", "b"]);
```

<a id="q246"></a>

### 246: How is a WeakMap typed and when do you use it?

`WeakMap<K, V>` keys must be objects (or non-registered symbols). Entries don't stop the key from being garbage collected, so it's good for caching data linked to objects.

```ts
const metadata = new WeakMap<object, { createdAt: Date }>();

function track(obj: object) {
  metadata.set(obj, { createdAt: new Date() });
}

metadata.set("key", { createdAt: new Date() }); // Error: string is not an object
```

<a id="q247"></a>

### 247: What type does Object.freeze return?

It returns `Readonly<T>`. For arrays it returns `readonly T[]`. It is shallow, both at runtime and in types.

```ts
const config = Object.freeze({ host: "localhost", db: { port: 5432 } });

config.host = "x"; // Error
config.db.port = 1; // allowed, nested object is not frozen
```

<a id="q248"></a>

### 248: How do you type a rejected Promise?

You can't. `Promise<T>` only describes the success value. The error in `.catch` or `try/catch` is `any` or `unknown`, because any code could throw anything.

```ts
async function load(): Promise<string> {
  throw new Error("fail");
}

load().catch((err) => {
  // err: any
});
```

If you want typed errors, return them as values instead, for example with a `Result` type:

```ts
type Result<T, E> = { ok: true; value: T } | { ok: false; error: E };
```

<a id="q249"></a>

### 249: What does a `Promise<never>` mean?

It is a promise that never resolves with a value. It either rejects or stays pending forever. You see it for functions that always throw.

```ts
async function failAlways(): Promise<never> {
  throw new Error("Always fails");
}
```

<a id="q250"></a>

### 250: What happens when you intersect two types that have the same property with different types?

The property type becomes the intersection of both. For primitives that can't overlap, it becomes `never`, and you can't create a valid object.

```ts
type A = { id: string };
type B = { id: number };

type C = A & B; // { id: never }

const c: C = { id: 1 }; // Error
```

With interfaces and `extends`, you get an error right away instead, which is easier to notice:

```ts
interface D extends A {
  id: number;
} // Error: Types of property 'id' are incompatible
```

<a id="q251"></a>

### 251: How do unknown and never behave in unions and intersections?

- `unknown` absorbs everything in a union and disappears in an intersection.
- `never` disappears in a union and absorbs everything in an intersection.

```ts
type A = string | unknown; // unknown
type B = string & unknown; // string
type C = string | never; // string
type D = string & never; // never
```

A simple way to remember: `unknown` is the "all values" set, `never` is the "empty" set.

<a id="q252"></a>

### 252: What is contextual typing?

Contextual typing is when TypeScript figures out a type from where the value is used, not from the value itself. It's common with callbacks.

```ts
window.addEventListener("click", (e) => {
  e.clientX; // e is MouseEvent because of the "click" event
});

const names = ["a", "b"];
names.forEach((n) => n.toUpperCase()); // n is string

type Handler = (id: number) => void;
const h: Handler = (id) => id.toFixed(); // id is number
```

<a id="q253"></a>

### 253: Should you always write return types on functions?

It's a matter of style. Return type inference works well, but writing the return type has benefits:

- You get an error inside the function if you return the wrong thing, instead of an error somewhere else.
- It documents public APIs.
- Large projects compile a bit faster, and `isolatedDeclarations` requires it for exported functions.

Many teams write return types for exported functions and let TypeScript infer them for small internal ones.

<a id="q254"></a>

### 254: What is a heterogeneous enum?

An enum that mixes string and number values. It is allowed but rarely a good idea.

```ts
enum Answer {
  No = 0,
  Yes = "YES",
}
```

<a id="q255"></a>

### 255: What are computed and constant enum members?

Enum values can be literal values, expressions based on other members, or values computed at runtime.

```ts
enum FileAccess {
  None = 0,
  Read = 1 << 1,
  Write = 1 << 2,
  ReadWrite = Read | Write, // constant, computed at compile time
  Length = "abc".length, // computed at runtime
}
```

Numeric enums with bit flags like the one above are a common use case.

<a id="q256"></a>

### 256: What is the "as const object" pattern and why use it instead of an enum?

You create a plain object with `as const` and then build a type from its values. You get named constants like an enum, but it's plain JavaScript.

```ts
const Status = {
  Active: "active",
  Inactive: "inactive",
} as const;

type Status = (typeof Status)[keyof typeof Status]; // "active" | "inactive"

function setStatus(s: Status) {}

setStatus(Status.Active); // OK
setStatus("inactive"); // also OK
```

With a string enum, passing `"inactive"` directly would be an error.

<a id="q257"></a>

### 257: What is the difference between a generic function type and a generic type alias for a function?

The position of `<T>` matters.

```ts
// The function itself is generic. T is chosen on every call.
type Identity = <T>(x: T) => T;
const id: Identity = (x) => x;
id("a"); // string
id(1); // number

// The type alias is generic. T is chosen when you use the type.
type IdentityOf<T> = (x: T) => T;
const idNum: IdentityOf<number> = (x) => x;
idNum("a"); // Error
```

<a id="q258"></a>

### 258: How can a generic type have more than one constraint?

Use an intersection in the constraint.

```ts
interface HasId {
  id: number;
}
interface HasName {
  name: string;
}

function label<T extends HasId & HasName>(item: T): string {
  return `${item.id}: ${item.name}`;
}

label({ id: 1, name: "Pen", price: 2 }); // OK
label({ id: 1 }); // Error
```

<a id="q259"></a>

### 259: How do you type the result of Object.entries?

`Object.entries` returns `[string, T][]`, where `T` is the value type. Keys are always `string` for the same reason `Object.keys` returns `string[]`.

```ts
const prices = { apple: 1, banana: 2 };

for (const [name, price] of Object.entries(prices)) {
  // name: string, price: number
}
```

If you are sure about the keys, you can write a small helper:

```ts
function typedEntries<T extends object>(obj: T) {
  return Object.entries(obj) as [keyof T, T[keyof T]][];
}
```

<a id="q260"></a>

### 260: How do you build an object type from a constant list of keys?

Turn the array into a union and use `Record` or a mapped type.

```ts
const fields = ["name", "email", "phone"] as const;

type Field = (typeof fields)[number];

type FormValues = Record<Field, string>;
// { name: string; email: string; phone: string }

type FormErrors = Partial<Record<Field, string>>;
```

<a id="q261"></a>

### 261: What are mixins in TypeScript?

A mixin is a function that takes a class and returns a new class that extends it with extra features. It is a way to combine behavior from several sources, since a class can only extend one class.

```ts
type Constructor<T = {}> = new (...args: any[]) => T;

function Timestamped<TBase extends Constructor>(Base: TBase) {
  return class extends Base {
    createdAt = new Date();
  };
}

function Activatable<TBase extends Constructor>(Base: TBase) {
  return class extends Base {
    active = false;
    activate() {
      this.active = true;
    }
  };
}

class User {
  constructor(public name: string) {}
}

const SmartUser = Timestamped(Activatable(User));
const u = new SmartUser("Ann");
u.activate();
u.createdAt;
```

<a id="q262"></a>

### 262: Why do custom React hooks often return as const?

If a hook returns an array, TypeScript infers a normal array with a union type, not a tuple. `as const` keeps each position's type.

```ts
function useToggle(initial = false) {
  const [on, setOn] = useState(initial);
  const toggle = () => setOn((v) => !v);

  return [on, toggle]; // (boolean | (() => void))[]
  // return [on, toggle] as const; // readonly [boolean, () => void]
}
```

Another option is to return an object, which doesn't have this problem.

<a id="q263"></a>

### 263: How do you type forwardRef in React?

Pass the element type and the props type as generics. Note that the order is ref first, then props.

```tsx
interface InputProps {
  label: string;
}

const TextInput = React.forwardRef<HTMLInputElement, InputProps>(
  ({ label }, ref) => (
    <label>
      {label}
      <input ref={ref} />
    </label>
  ),
);
```

In React 19, `ref` is a normal prop, so you can just add `ref?: React.Ref<HTMLInputElement>` to the props instead.

<a id="q264"></a>

### 264: How do you write a generic API fetch helper?

Make the response type a generic parameter.

```ts
async function api<T>(url: string, init?: RequestInit): Promise<T> {
  const res = await fetch(url, init);
  if (!res.ok) {
    throw new Error(`HTTP ${res.status}`);
  }
  return res.json() as Promise<T>;
}

interface User {
  id: number;
  name: string;
}

const user = await api<User>("/api/users/1");
user.name; // string
```

Libraries like axios do the same: `axios.get<User>(url)`.

<a id="q265"></a>

### 265: Can you have abstract properties in an abstract class?

Yes. Subclasses must define them.

```ts
abstract class Report {
  abstract readonly title: string;

  print() {
    console.log(`== ${this.title} ==`);
  }
}

class SalesReport extends Report {
  readonly title = "Sales";
}
```

<a id="q266"></a>

### 266: What does a protected constructor do?

The class can't be created with `new` from outside, but it can be extended. It is similar to an abstract class without abstract members.

```ts
class BaseService {
  protected constructor(protected url: string) {}
}

class UserService extends BaseService {
  constructor() {
    super("/api/users");
  }
}

new BaseService("/x"); // Error
new UserService(); // OK
```

<a id="q267"></a>

### 267: Can an interface extend a class?

Yes. The interface gets all members of the class, including private and protected ones. Then only that class or its subclasses can implement the interface.

```ts
class Control {
  private state: any;
}

interface SelectableControl extends Control {
  select(): void;
}

class Button extends Control implements SelectableControl {
  select() {}
}

class Image implements SelectableControl {
  // Error: missing private 'state'
  select() {}
}
```

<a id="q268"></a>

### 268: Can a class implement a type alias?

Yes, as long as the type alias describes an object type. It can't implement a union type.

```ts
type Speaker = { speak(): string };

class Person implements Speaker {
  speak() {
    return "hi";
  }
}

type Pet = { bark(): void } | { meow(): void };
class Cat implements Pet {} // Error: can only implement an object type
```

<a id="q269"></a>

### 269: What are export = and import = require()?

They describe CommonJS modules that do `module.exports = something`.

```ts
// old-lib.d.ts
declare function parse(text: string): object;
export = parse;
```

```ts
// usage
import parse = require("old-lib");
// or, with esModuleInterop:
import parse from "old-lib";
```

<a id="q270"></a>

### 270: What are .mts and .cts files?

They tell TypeScript which module format a file uses, no matter what `package.json` says.

- `.mts` compiles to `.mjs` and is always an ES module.
- `.cts` compiles to `.cjs` and is always CommonJS.

This is mostly used in Node.js projects with `module: nodenext`.

<a id="q271"></a>

### 271: Why do you need .js extensions in imports with module nodenext?

In Node.js ESM, imports must include the file extension. TypeScript does not rewrite import paths, so you write the path of the output file, which is `.js`.

```ts
// src/app.ts
import { helper } from "./utils.js"; // points to utils.ts during type checking
```

It looks strange at first, but it is correct. TypeScript 5.7 added `rewriteRelativeImportExtensions`, which lets you write `.ts` and have it changed to `.js` in the output.

<a id="q272"></a>

### 272: What are the types and typeRoots options?

- `typeRoots` sets the folders where TypeScript looks for global type packages. The default is `node_modules/@types`.
- `types` limits which of those packages are included automatically.

```json
{
  "compilerOptions": {
    "types": ["node", "vitest/globals"]
  }
}
```

This is useful to avoid conflicts, for example between Jest and Mocha global types.

<a id="q273"></a>

### 273: How do you use TypeScript with Jest or Vitest?

For Jest you usually use `ts-jest` or a Babel/swc transform, plus `@types/jest`. Vitest supports TypeScript out of the box.

```ts
import { describe, it, expect, vi } from "vitest";
import { sum } from "./sum";

describe("sum", () => {
  it("adds numbers", () => {
    expect(sum(1, 2)).toBe(3);
  });
});

const mockFn = vi.fn<(id: number) => string>();
mockFn.mockReturnValue("ok");
```

Keep in mind that test runners often only remove types and don't check them. Run `tsc --noEmit` separately to catch type errors.

<a id="q274"></a>

### 274: How do you type a mocked module in Jest?

Use `jest.Mocked` or `jest.mocked()` to get mock methods with the correct types.

```ts
import { getUser } from "./api";
jest.mock("./api");

const mockedGetUser = jest.mocked(getUser);

mockedGetUser.mockResolvedValue({ id: 1, name: "Ann" }); // checked against the real return type
```

<a id="q275"></a>

### 275: What are import types?

You can refer to a type from another file without a normal import statement, using `import("...")` inside a type position.

```ts
let user: import("./models").User;

type Config = import("./config").default;
```

This is common in JSDoc comments and in `.d.ts` files.

<a id="q276"></a>

### 276: How are dynamic imports typed?

`import()` returns a Promise of the module, and TypeScript knows the module's types.

```ts
async function loadChart() {
  const { Chart } = await import("./chart");
  return new Chart(); // fully typed
}

type ChartModule = typeof import("./chart");
```

<a id="q277"></a>

### 277: How do you write an assertNever helper?

It's a function that takes `never` and throws. Use it in switch defaults to check that all cases are handled.

```ts
function assertNever(value: never): never {
  throw new Error(`Unexpected value: ${JSON.stringify(value)}`);
}

type Method = "GET" | "POST";

function handle(m: Method) {
  switch (m) {
    case "GET":
      return "read";
    case "POST":
      return "write";
    default:
      return assertNever(m);
  }
}
```

<a id="q278"></a>

### 278: Why does keyof on a string index signature give string | number?

In JavaScript, number keys are turned into strings (`obj[1]` is the same as `obj["1"]`). So if a type allows any string key, number keys are allowed too.

```ts
type Dict = { [key: string]: boolean };
type K = keyof Dict; // string | number

type NumDict = { [key: number]: boolean };
type K2 = keyof NumDict; // number
```

If you only want strings, use `Extract<keyof T, string>` or `keyof T & string`.

<a id="q279"></a>

### 279: What happens when you use a union in an indexed access type?

You get a union of the property types.

```ts
interface User {
  id: number;
  name: string;
  active: boolean;
}

type IdOrName = User["id" | "name"]; // number | string
type AllValues = User[keyof User]; // number | string | boolean
```

`T[keyof T]` is a common way to get a union of all value types.

<a id="q280"></a>

### 280: How is the Partial type implemented?

It's a mapped type that adds `?` to every property.

```ts
type MyPartial<T> = {
  [K in keyof T]?: T[K];
};
```

`Required` uses `-?` and `Readonly` uses `readonly` the same way.

<a id="q281"></a>

### 281: How are Pick and Omit implemented?

```ts
type MyPick<T, K extends keyof T> = {
  [P in K]: T[P];
};

type MyOmit<T, K extends keyof any> = Pick<T, Exclude<keyof T, K>>;
```

Notice that `Omit` accepts any key, even one that doesn't exist on `T`, so a typo will not cause an error:

```ts
type U = { id: number; name: string };
type X = Omit<U, "nmae">; // no error, nothing removed
```

Some codebases define a stricter version with `K extends keyof T`.

<a id="q282"></a>

### 282: How is ReturnType implemented?

With a conditional type and `infer`.

```ts
type MyReturnType<T extends (...args: any) => any> = T extends (
  ...args: any
) => infer R
  ? R
  : any;
```

`Parameters` is similar, but it infers the arguments: `T extends (...args: infer P) => any ? P : never`.

<a id="q283"></a>

### 283: Is a type assertion the same as type casting?

No. In languages like Java or C#, casting can convert a value at runtime. In TypeScript, an assertion only changes what the compiler thinks. Nothing happens at runtime.

```ts
const input = "42";
const n = input as unknown as number;

console.log(typeof n); // "string" - it's still a string!

const real = Number(input); // this is an actual conversion
```

<a id="q284"></a>

### 284: How do you define a recursive type?

A type can refer to itself. This is used for trees, nested menus, linked lists and similar structures.

```ts
interface TreeNode {
  value: string;
  children: TreeNode[];
}

type LinkedList<T> = {
  value: T;
  next: LinkedList<T> | null;
};

const tree: TreeNode = {
  value: "root",
  children: [{ value: "child", children: [] }],
};
```

<a id="q285"></a>

### 285: How would you write a type for any JSON value?

With a recursive union.

```ts
type JSONValue =
  string | number | boolean | null | JSONValue[] | { [key: string]: JSONValue };

const data: JSONValue = {
  name: "Ann",
  tags: ["a", "b"],
  meta: { active: true, score: null },
};

const bad: JSONValue = { date: new Date() }; // Error
```

<a id="q286"></a>

### 286: Can an interface have both an index signature and known properties?

Yes, but the known properties must have types that fit the index signature.

```ts
interface Headers {
  "content-type": string;
  [name: string]: string;
}

interface Bad {
  count: number; // Error: number is not assignable to string index type
  [key: string]: string;
}

interface Good {
  count: number;
  [key: string]: string | number;
}
```

<a id="q287"></a>

### 287: How do you write overloads in an interface?

List several call signatures, or several method signatures with the same name.

```ts
interface Converter {
  (input: string): number;
  (input: number): string;
}

interface Storage {
  get(key: "count"): number;
  get(key: "name"): string;
  get(key: string): unknown;
}
```

<a id="q288"></a>

### 288: Why does the order of overloads matter?

TypeScript checks overloads from top to bottom and uses the first one that matches. So put the more specific overloads first.

```ts
function find(x: string): string; // specific
function find(x: unknown): unknown; // general
function find(x: unknown) {
  return x;
}

const r = find("a"); // string

// if the order was reversed, find("a") would return unknown
```

<a id="q289"></a>

### 289: What does strictBindCallApply do?

It makes `bind`, `call` and `apply` check the argument types against the original function.

```ts
function greet(name: string, age: number) {
  return `${name} is ${age}`;
}

greet.call(undefined, "Ann", 30); // OK
greet.call(undefined, "Ann", "30"); // Error
greet.apply(undefined, ["Ann"]); // Error: missing age

const bound = greet.bind(undefined, "Ann");
bound(30); // OK, bound is (age: number) => string
```

<a id="q290"></a>

### 290: What are ThisParameterType and OmitThisParameter?

- `ThisParameterType<F>` gets the type of `this` declared on a function.
- `OmitThisParameter<F>` removes the `this` parameter from a function type.

```ts
function toHex(this: number) {
  return this.toString(16);
}

type T = ThisParameterType<typeof toHex>; // number

const fn: OmitThisParameter<typeof toHex> = toHex.bind(255);
fn(); // "ff"
```

<a id="q291"></a>

### 291: How do you type a function that takes a callback with a generic result?

Let the generic come from the callback's return type.

```ts
function withRetry<T>(fn: () => Promise<T>, retries = 3): Promise<T> {
  return fn().catch((err) => {
    if (retries <= 0) throw err;
    return withRetry(fn, retries - 1);
  });
}

const data = await withRetry(() =>
  fetch("/api").then((r) => r.json() as Promise<string[]>),
);
// data: string[]
```

<a id="q292"></a>

### 292: What is the difference between Object.assign and spread for types?

Both merge objects. `Object.assign` returns an intersection type `A & B`, while spread computes a new object type where later properties replace earlier ones.

```ts
const a = { id: 1, name: "x" };
const b = { name: 2 };

const r1 = Object.assign({}, a, b); // { id: number; name: string } & { name: number }
const r2 = { ...a, ...b }; // { id: number; name: number }
```

The spread result is more accurate, so it's usually preferred.

<a id="q293"></a>

### 293: What is a type predicate for this in a class method?

A method can return `this is SomeType` to narrow the object itself.

```ts
class FileItem {
  isFolder(): this is Folder {
    return this instanceof Folder;
  }
}

class Folder extends FileItem {
  children: FileItem[] = [];
}

function walk(item: FileItem) {
  if (item.isFolder()) {
    item.children; // item is Folder
  }
}
```

<a id="q294"></a>

### 294: How do generics work with default values in function parameters?

TypeScript doesn't infer a generic from a default value in a way you'd expect, because the default must fit any `T` the caller could pass.

```ts
function wrap<T>(value: T = "x") {} // Error: '"x"' is not assignable to 'T'

// fix with overloads or a default type
function wrap2<T = string>(value?: T) {}
```

<a id="q295"></a>

### 295: How do you make sure two parameters have the same type?

Use one generic for both. If inference picks a union, you can block the second parameter from affecting inference with `NoInfer` (TypeScript 5.4+).

```ts
function same<T>(a: T, b: T) {}
same(1, 2); // OK
same(1, "a"); // Error in most cases

function pick<T extends string>(options: T[], initial: NoInfer<T>) {}
pick(["red", "blue"], "red"); // OK
pick(["red", "blue"], "green"); // Error
```

<a id="q296"></a>

### 296: What is the difference between interface extends and intersection when it comes to errors and performance?

- `interface A extends B` checks right away that the new properties are compatible and reports a clear error. Interfaces are also cached by name, which helps compiler speed in big projects.
- `type A = B & C` never reports a conflict at the point of declaration. Conflicting properties silently become `never`.

The official TypeScript performance guide recommends interfaces with `extends` over intersections when you can choose.

<a id="q297"></a>

### 297: How do you type an object where some keys are known and the rest are dynamic with a different type?

An index signature must fit all known properties, so a direct approach often fails. Use an intersection instead.

```ts
type Translations = { defaultLocale: string } & {
  [locale: string]: Record<string, string> | string;
};

// or keep them separate, which is usually cleaner
interface I18n {
  defaultLocale: string;
  messages: Record<string, Record<string, string>>;
}
```

<a id="q298"></a>

### 298: What is the `Uppercase<string>` type?

Intrinsic string types also work with `string`, not only with literals. `Uppercase<string>` means "any string that is all upper case".

```ts
let code: Uppercase<string> = "ABC"; // OK
code = "abc"; // Error

type Prefixed = `ID_${Uppercase<string>}`;
const id: Prefixed = "ID_XYZ";
```

<a id="q299"></a>

### 299: How do optional chaining and the types of the result work together?

If any part of an optional chain may be `undefined`, the result type includes `undefined`.

```ts
interface Company {
  ceo?: { name: string; address?: { city: string } };
}

declare const c: Company;

const name = c.ceo?.name; // string | undefined
const city = c.ceo?.address?.city; // string | undefined
const len = c.ceo?.name.length; // number | undefined
```

Note `c.ceo?.name.length`: once `ceo` exists, `name` is a required string, so no second `?.` is needed.

<a id="q300"></a>

### 300: How do you type a function that returns different types based on a boolean flag?

Use overloads with literal types, or a conditional type.

```ts
function getItems(asString: true): string;
function getItems(asString: false): string[];
function getItems(asString: boolean): string | string[] {
  const items = ["a", "b"];
  return asString ? items.join(",") : items;
}

const s = getItems(true); // string
const a = getItems(false); // string[]
```

[Back to top](#table-of-contents)

<a id="advanced"></a>

## Advanced Questions (301-450)

<a id="q301"></a>

### 301: What are covariance and contravariance?

They describe how subtyping of a type affects subtyping of something built from it.

- Covariant: if `Dog` is a subtype of `Animal`, then `Producer<Dog>` is a subtype of `Producer<Animal>`. Return types and read only properties work this way.
- Contravariant: the direction flips. `Consumer<Animal>` is a subtype of `Consumer<Dog>`. Function parameters work this way.

```ts
interface Animal {
  name: string;
}
interface Dog extends Animal {
  bark(): void;
}

type Getter<T> = () => T; // covariant
type Setter<T> = (v: T) => void; // contravariant

const getDog: Getter<Dog> = () => ({ name: "Rex", bark() {} });
const getAnimal: Getter<Animal> = getDog; // OK

const setAnimal: Setter<Animal> = (a) => console.log(a.name);
const setDog: Setter<Dog> = setAnimal; // OK
const setAnimal2: Setter<Animal> = setDog; // Error with strictFunctionTypes
```

A type that is both read and written (like a mutable property) should be invariant.

<a id="q302"></a>

### 302: What are the in and out variance annotations?

Since TypeScript 4.7 you can mark a type parameter as `out` (covariant), `in` (contravariant) or `in out` (invariant). TypeScript then checks that the annotation is correct and can skip some expensive work when comparing types.

```ts
interface Producer<out T> {
  get(): T;
}

interface Consumer<in T> {
  accept(value: T): void;
}

interface Box<in out T> {
  value: T;
}
```

Most of the time TypeScript measures variance on its own. Annotations are mainly useful for performance in very large or recursive types, and to make the intent clear.

<a id="q303"></a>

### 303: Why are method parameters bivariant in TypeScript?

Parameters declared with method syntax are checked both ways (bivariantly), even with `strictFunctionTypes`. This was kept on purpose so common patterns, like arrays, keep working.

```ts
interface Animal {
  name: string;
}
interface Dog extends Animal {
  bark(): void;
}

interface Handler {
  handle(a: Animal): void; // method syntax: bivariant
}

const dogHandler: Handler = {
  handle(d: Dog) {
    d.bark();
  }, // allowed, but unsafe
};

dogHandler.handle({ name: "cat" }); // crashes at runtime: bark is not a function
```

If you write `handle: (a: Animal) => void` instead, the assignment above is an error.

<a id="q304"></a>

### 304: Why are arrays covariant and why is that unsafe?

TypeScript lets you assign `Dog[]` to `Animal[]`. This is convenient, but it allows you to push a non-dog into a dog array.

```ts
const dogs: Dog[] = [];
const animals: Animal[] = dogs; // allowed

animals.push({ name: "Tom the cat" }); // allowed
dogs[0].bark(); // runtime error
```

Using `readonly Animal[]` in function parameters avoids this, since you can't push into a read only array.

<a id="q305"></a>

### 305: What are some known places where TypeScript is not fully sound?

TypeScript chooses being practical over being 100% correct. Some known holes:

- Method parameter bivariance.
- Covariant arrays (shown above).
- `any` turns off checking anywhere it appears.
- Type assertions (`as`) and `!` are trusted without checks.
- Index access without `noUncheckedIndexedAccess` assumes the value exists.
- Optional properties can be "forgotten" through assignment to a wider type and then reassigned with the wrong type.
- Narrowing is not reset when a function you call changes an object.

```ts
function reset(obj: { value: string | number }) {
  obj.value = 42;
}

const o = { value: "text" as string | number };
if (typeof o.value === "string") {
  reset(o);
  o.value.toUpperCase(); // TypeScript still thinks it's a string. Crashes.
}
```

<a id="q306"></a>

### 306: How do you turn a union into an intersection?

This uses the fact that inferring from a contravariant position (function parameters) gives an intersection.

```ts
type UnionToIntersection<U> = (
  U extends any ? (arg: U) => void : never
) extends (arg: infer I) => void
  ? I
  : never;

type R = UnionToIntersection<{ a: 1 } | { b: 2 }>; // { a: 1 } & { b: 2 }
```

Step by step:

1. The first conditional distributes and builds `((arg: {a:1}) => void) | ((arg: {b:2}) => void)`.
2. Inferring `I` from the parameter of a union of functions gives an intersection, because a function that can accept both must accept `A & B`.

<a id="q307"></a>

### 307: Why does infer in a contravariant position produce an intersection?

When TypeScript has several candidates for an `infer` variable:

- From covariant positions (return types, properties) it combines them with a union.
- From contravariant positions (parameters) it combines them with an intersection.

```ts
type Co<T> = T extends { a: infer U; b: infer U } ? U : never;
type A = Co<{ a: string; b: number }>; // string | number

type Contra<T> = T extends { a: (x: infer U) => void; b: (x: infer U) => void }
  ? U
  : never;
type B = Contra<{ a: (x: string) => void; b: (x: number) => void }>; // string & number = never
```

<a id="q308"></a>

### 308: How do you check if a type is any?

`any` is the only type where `0 extends 1 & T` is true, because `1 & any` is `any`.

```ts
type IsAny<T> = 0 extends 1 & T ? true : false;

type A = IsAny<any>; // true
type B = IsAny<unknown>; // false
type C = IsAny<string>; // false
```

<a id="q309"></a>

### 309: How do you check if a type is never?

You can't use `T extends never ? ...` directly, because a distributive conditional over `never` returns `never` (it's an empty union). Wrap it in a tuple to stop distribution.

```ts
type IsNeverWrong<T> = T extends never ? true : false;
type A = IsNeverWrong<never>; // never (not true!)

type IsNever<T> = [T] extends [never] ? true : false;
type B = IsNever<never>; // true
type C = IsNever<string>; // false
```

<a id="q310"></a>

### 310: How do you check if two types are exactly equal?

A simple `A extends B` check is not enough because of subtyping and `any`. The common trick compares two generic functions, which forces TypeScript to use its internal "identical" check.

```ts
type Equals<X, Y> =
  (<T>() => T extends X ? 1 : 2) extends <T>() => T extends Y ? 1 : 2
    ? true
    : false;

type A = Equals<string, string>; // true
type B = Equals<{ a: 1 }, { readonly a: 1 }>; // false
type C = Equals<any, unknown>; // false
```

This is used in type testing libraries.

<a id="q311"></a>

### 311: How do you write a DeepPartial type?

Use a recursive mapped type, and be careful with functions and arrays.

```ts
type DeepPartial<T> = T extends (...args: any[]) => any
  ? T
  : T extends readonly (infer U)[]
    ? DeepPartial<U>[]
    : T extends object
      ? { [K in keyof T]?: DeepPartial<T[K]> }
      : T;

interface Config {
  server: { host: string; port: number };
  features: { name: string; enabled: boolean }[];
}

const patch: DeepPartial<Config> = {
  server: { port: 8080 },
};
```

<a id="q312"></a>

### 312: How do you write a DeepReadonly type?

```ts
type DeepReadonly<T> = T extends (...args: any[]) => any
  ? T
  : T extends Map<infer K, infer V>
    ? ReadonlyMap<DeepReadonly<K>, DeepReadonly<V>>
    : T extends Set<infer U>
      ? ReadonlySet<DeepReadonly<U>>
      : T extends object
        ? { readonly [K in keyof T]: DeepReadonly<T[K]> }
        : T;

type State = DeepReadonly<{ user: { tags: string[] } }>;

declare const s: State;
s.user.tags.push("x"); // Error
```

Homomorphic mapped types on arrays produce read only arrays, so `string[]` becomes `readonly string[]` here.

<a id="q313"></a>

### 313: What are branded types?

Branded (or nominal) types make two types with the same structure incompatible. You add a fake property that only exists in the type system.

```ts
type Brand<T, B extends string> = T & { readonly __brand: B };

type UserId = Brand<string, "UserId">;
type OrderId = Brand<string, "OrderId">;

function toUserId(id: string): UserId {
  return id as UserId;
}

function getUser(id: UserId) {}

const uid = toUserId("u_1");
getUser(uid); // OK
getUser("u_1"); // Error
getUser("o_1" as OrderId); // Error
```

It is useful for IDs, validated strings (email, URL), units like `Meters` vs `Feet`, and so on.

<a id="q314"></a>

### 314: How can you make a brand that can't be faked with a string property?

Use a `unique symbol` declared but not exported. Nobody outside the module can write that key.

```ts
declare const emailBrand: unique symbol;

export type Email = string & { readonly [emailBrand]: true };

export function parseEmail(input: string): Email {
  if (!input.includes("@")) throw new Error("Invalid email");
  return input as Email;
}
```

The only way to get an `Email` is through `parseEmail`, which validates the input.

<a id="q315"></a>

### 315: What are phantom types?

A phantom type is a type parameter that is not used in the value itself, only to track some state at compile time.

```ts
type Unvalidated = { readonly _state: "unvalidated" };
type Validated = { readonly _state: "validated" };

interface Form<State> {
  data: Record<string, string>;
  readonly __phantom?: State;
}

function validate(form: Form<Unvalidated>): Form<Validated> {
  // check fields...
  return form as Form<Validated>;
}

function submit(form: Form<Validated>) {}

const raw: Form<Unvalidated> = { data: {} };
submit(raw); // Error
submit(validate(raw)); // OK
```

<a id="q316"></a>

### 316: What are variadic tuple types?

Since TypeScript 4.0, you can spread generic tuple types inside other tuples. This lets you type functions that work on argument lists of any length.

```ts
type Concat<A extends unknown[], B extends unknown[]> = [...A, ...B];

type R = Concat<[1, 2], ["a"]>; // [1, 2, "a"]

function concat<A extends unknown[], B extends unknown[]>(
  a: [...A],
  b: [...B],
): [...A, ...B] {
  return [...a, ...b];
}

const c = concat([1, "x"], [true]); // [number, string, boolean]
```

<a id="q317"></a>

### 317: How do you type a partial application function?

Use variadic tuples to split the parameters into the ones given now and the rest.

```ts
function partial<A extends unknown[], B extends unknown[], R>(
  fn: (...args: [...A, ...B]) => R,
  ...first: A
): (...rest: B) => R {
  return (...rest) => fn(...first, ...rest);
}

function greet(greeting: string, name: string, punct: string) {
  return `${greeting}, ${name}${punct}`;
}

const hello = partial(greet, "Hello");
hello("Ann", "!"); // OK
hello("Ann"); // Error: expected 2 arguments
```

<a id="q318"></a>

### 318: How do you type a curry function?

A curried function takes arguments one by one. A recursive type can describe it.

```ts
type Curried<Args extends unknown[], R> = Args extends [
  infer First,
  ...infer Rest,
]
  ? (arg: First) => Rest extends [] ? R : Curried<Rest, R>
  : R;

declare function curry<Args extends unknown[], R>(
  fn: (...args: Args) => R,
): Curried<Args, R>;

const add3 = (a: number, b: string, c: boolean) => `${a}${b}${c}`;

const curried = curry(add3);
const result = curried(1)("x")(true); // string
curried(1)(2); // Error
```

<a id="q319"></a>

### 319: How do you type a pipe function?

The usual approach is overloads, because a fully generic version for any number of functions is hard to infer well.

```ts
function pipe<A, B>(a: A, ab: (a: A) => B): B;
function pipe<A, B, C>(a: A, ab: (a: A) => B, bc: (b: B) => C): C;
function pipe<A, B, C, D>(
  a: A,
  ab: (a: A) => B,
  bc: (b: B) => C,
  cd: (c: C) => D,
): D;
function pipe(value: unknown, ...fns: Array<(x: any) => any>) {
  return fns.reduce((acc, fn) => fn(acc), value);
}

const r = pipe(
  "  42 ",
  (s) => s.trim(),
  (s) => Number(s),
  (n) => n * 2,
); // number
```

Libraries like fp-ts, Effect and RxJS use this same overload approach.

<a id="q320"></a>

### 320: How do you get the length of a tuple as a type?

Read its `length` property. For tuples it's a number literal type.

```ts
type Length<T extends readonly unknown[]> = T["length"];

type A = Length<[1, 2, 3]>; // 3
type B = Length<string[]>; // number
```

<a id="q321"></a>

### 321: How do you reverse a tuple type?

With a recursive conditional type.

```ts
type Reverse<T extends unknown[]> = T extends [infer Head, ...infer Tail]
  ? [...Reverse<Tail>, Head]
  : [];

type R = Reverse<[1, "a", true]>; // [true, "a", 1]
```

<a id="q322"></a>

### 322: How do you do arithmetic at the type level?

TypeScript has no number operations in types, but you can build tuples of a certain length and read their `length`.

```ts
type BuildTuple<
  N extends number,
  T extends unknown[] = [],
> = T["length"] extends N ? T : BuildTuple<N, [...T, unknown]>;

type Add<A extends number, B extends number> = [
  ...BuildTuple<A>,
  ...BuildTuple<B>,
]["length"];

type Subtract<A extends number, B extends number> =
  BuildTuple<A> extends [...BuildTuple<B>, ...infer Rest]
    ? Rest["length"]
    : never;

type X = Add<3, 4>; // 7
type Y = Subtract<10, 3>; // 7
```

It only works for small non-negative integers, because recursion has limits. It's mostly a puzzle, but it shows how flexible the type system is.

<a id="q323"></a>

### 323: How do you turn a tuple into a union?

Index it with `number`.

```ts
type TupleToUnion<T extends readonly unknown[]> = T[number];

type U = TupleToUnion<["a", "b", 1]>; // "a" | "b" | 1
```

<a id="q324"></a>

### 324: Why is converting a union to a tuple not a good idea?

Unions have no reliable order. TypeScript may order union members differently depending on the order types were created in the program. A union-to-tuple type is possible with tricks (using overload inference), but the result order is not stable and it is slow for big unions. If you need an ordered list, start from a tuple (an `as const` array) and derive the union from it.

<a id="q325"></a>

### 325: How do you parse strings at the type level with template literal types?

Use `infer` inside a template literal pattern.

```ts
type Split<
  S extends string,
  D extends string,
> = S extends `${infer Head}${D}${infer Tail}`
  ? [Head, ...Split<Tail, D>]
  : [S];

type Parts = Split<"a,b,c", ",">; // ["a", "b", "c"]

type Join<T extends string[], D extends string> = T extends [
  infer F extends string,
  ...infer R extends string[],
]
  ? R extends []
    ? F
    : `${F}${D}${Join<R, D>}`
  : "";

type Joined = Join<["a", "b", "c"], "-">; // "a-b-c"
```

<a id="q326"></a>

### 326: How do you write a Trim type?

```ts
type Whitespace = " " | "\n" | "\t";

type TrimLeft<S extends string> = S extends `${Whitespace}${infer R}`
  ? TrimLeft<R>
  : S;
type TrimRight<S extends string> = S extends `${infer R}${Whitespace}`
  ? TrimRight<R>
  : S;
type Trim<S extends string> = TrimLeft<TrimRight<S>>;

type T = Trim<"   hello  ">; // "hello"
```

<a id="q327"></a>

### 327: How do you extract route parameters from a path string?

This is the trick used by typed routers (Express types, Hono, TanStack Router and others).

```ts
type RouteParams<Path extends string> =
  Path extends `${string}:${infer Param}/${infer Rest}`
    ? { [K in Param | keyof RouteParams<`/${Rest}`>]: string }
    : Path extends `${string}:${infer Param}`
      ? { [K in Param]: string }
      : {};

type P = RouteParams<"/users/:userId/posts/:postId">;
// { userId: string; postId: string }

function link<P extends string>(path: P, params: RouteParams<P>) {}

link("/users/:id", { id: "1" }); // OK
link("/users/:id", { uid: "1" }); // Error
```

<a id="q328"></a>

### 328: How do you convert snake_case to camelCase at the type level?

```ts
type CamelCase<S extends string> = S extends `${infer Head}_${infer Tail}`
  ? `${Head}${Capitalize<CamelCase<Tail>>}`
  : S;

type A = CamelCase<"user_first_name">; // "userFirstName"

type CamelKeys<T> = {
  [K in keyof T as K extends string ? CamelCase<K> : K]: T[K];
};

type Api = { user_id: number; created_at: string };
type Model = CamelKeys<Api>; // { userId: number; createdAt: string }
```

<a id="q329"></a>

### 329: How do you get all dot-notation paths of an object type?

```ts
type Paths<T> = T extends object
  ? {
      [K in keyof T & string]: T[K] extends object
        ? K | `${K}.${Paths<T[K]>}`
        : K;
    }[keyof T & string]
  : never;

interface Settings {
  theme: { color: string; font: { size: number } };
  lang: string;
}

type P = Paths<Settings>;
// "theme" | "theme.color" | "theme.font" | "theme.font.size" | "lang"
```

Libraries like react-hook-form use this idea for field names like `register("address.city")`.

<a id="q330"></a>

### 330: How do you get the type at a dot-notation path?

```ts
type Get<T, P extends string> = P extends `${infer Head}.${infer Rest}`
  ? Head extends keyof T
    ? Get<T[Head], Rest>
    : never
  : P extends keyof T
    ? T[P]
    : never;

type FontSize = Get<Settings, "theme.font.size">; // number

declare function get<T, P extends Paths<T>>(obj: T, path: P): Get<T, P>;
```

<a id="q331"></a>

### 331: What is the limit on recursion in conditional types?

TypeScript limits how deep type instantiation can go. If you go too deep you get: `Type instantiation is excessively deep and possibly infinite`.

Since TypeScript 4.5, conditional types that are tail recursive (the recursive call is the whole result of a branch) are optimized and can go about 1000 levels deep. Non tail recursive types hit the limit much sooner (around 50 to 100 levels).

```ts
// not tail recursive: the result wraps the recursive call
type LenSlow<S extends string> = S extends `${string}${infer R}`
  ? [0, ...LenSlow<R>]
  : [];

// tail recursive: uses an accumulator
type LenFast<
  S extends string,
  Acc extends unknown[] = [],
> = S extends `${string}${infer R}` ? LenFast<R, [...Acc, 0]> : Acc["length"];
```

<a id="q332"></a>

### 332: What are const type parameters?

Since TypeScript 5.0 you can write `const` before a type parameter. Then TypeScript infers the most specific type, as if the caller wrote `as const`.

```ts
function routes<T extends readonly string[]>(paths: T) {
  return paths;
}
const a = routes(["/home", "/about"]); // string[]

function routes2<const T extends readonly string[]>(paths: T) {
  return paths;
}
const b = routes2(["/home", "/about"]); // readonly ["/home", "/about"]
```

Note: the constraint should use `readonly` arrays, otherwise the literal inference may fall back to the constraint.

<a id="q333"></a>

### 333: How do you make props mutually exclusive (XOR)?

Use `?: never` to forbid the props of the other option.

```ts
type Without<T, U> = { [K in Exclude<keyof T, keyof U>]?: never };
type XOR<T, U> = (T & Without<U, T>) | (U & Without<T, U>);

type ByEmail = { email: string };
type ByPhone = { phone: string };

type Contact = XOR<ByEmail, ByPhone>;

const a: Contact = { email: "a@b.com" }; // OK
const b: Contact = { phone: "123" }; // OK
const c: Contact = { email: "a@b.com", phone: "123" }; // Error
```

<a id="q334"></a>

### 334: How do you require at least one of several optional properties?

```ts
type RequireAtLeastOne<T, Keys extends keyof T = keyof T> = Omit<T, Keys> &
  {
    [K in Keys]-?: Required<Pick<T, K>> & Partial<Pick<T, Exclude<Keys, K>>>;
  }[Keys];

interface Search {
  limit?: number;
  name?: string;
  email?: string;
}

type SearchQuery = RequireAtLeastOne<Search, "name" | "email">;

const q1: SearchQuery = { name: "Ann" }; // OK
const q2: SearchQuery = { limit: 10 }; // Error
```

<a id="q335"></a>

### 335: How do you get the keys of an object whose values match a certain type?

Map each key to itself or `never`, then index with `keyof`.

```ts
type KeysOfType<T, V> = {
  [K in keyof T]-?: T[K] extends V ? K : never;
}[keyof T];

interface User {
  id: number;
  name: string;
  email: string;
  age?: number;
}

type StringKeys = KeysOfType<User, string>; // "name" | "email"

// or with key remapping
type PickByType<T, V> = { [K in keyof T as T[K] extends V ? K : never]: T[K] };
type OnlyStrings = PickByType<User, string>; // { name: string; email: string }
```

<a id="q336"></a>

### 336: How do you find the optional keys of a type?

A key is optional if `{}` is assignable to an object with only that key.

```ts
type OptionalKeys<T> = {
  [K in keyof T]-?: {} extends Pick<T, K> ? K : never;
}[keyof T];

type RequiredKeys<T> = Exclude<keyof T, OptionalKeys<T>>;

type U = { id: number; nick?: string; bio?: string };

type O = OptionalKeys<U>; // "nick" | "bio"
type R = RequiredKeys<U>; // "id"
```

<a id="q337"></a>

### 337: What is a homomorphic mapped type?

A mapped type of the form `{ [K in keyof T]: ... }` is called homomorphic. It has special behavior:

- It keeps the `readonly` and `?` modifiers of the original properties.
- When `T` is an array or tuple, the result is also an array or tuple.
- When `T` is a union, it distributes over the members.
- When `T` is a primitive, the result is that primitive.

```ts
type Stringify<T> = { [K in keyof T]: string };

type A = Stringify<{ readonly a: number; b?: number }>; // { readonly a: string; b?: string }
type B = Stringify<[number, boolean]>; // [string, string]
```

A mapped type like `{ [K in "a" | "b"]: ... }` is not homomorphic and doesn't do any of that.

<a id="q338"></a>

### 338: How do you map over a tuple and keep it a tuple?

Use a homomorphic mapped type. This is how `Promise.all` keeps the position of each type.

```ts
type AwaitedAll<T extends readonly unknown[]> = {
  -readonly [K in keyof T]: Awaited<T[K]>;
};

declare function all<T extends readonly unknown[] | []>(
  values: T,
): Promise<AwaitedAll<T>>;

const r = await all([Promise.resolve(1), "x", Promise.resolve(true)]);
// [number, string, boolean]
```

The `| []` in the constraint is a hint that makes TypeScript infer a tuple instead of an array.

<a id="q339"></a>

### 339: What does infer with extends do?

Since TypeScript 4.7 you can add a constraint directly to an `infer` variable. If it doesn't match, the conditional goes to the false branch.

```ts
type FirstString<T> = T extends [infer S extends string, ...unknown[]]
  ? S
  : never;

type A = FirstString<["a", 1]>; // "a"
type B = FirstString<[1, "a"]>; // never

type ToNumber<S> = S extends `${infer N extends number}` ? N : never;
type C = ToNumber<"42">; // 42
```

<a id="q340"></a>

### 340: Which overload does ReturnType use for an overloaded function?

The last one. Conditional types with `infer` match only the last signature (usually the most general one).

```ts
declare function parse(x: string): number;
declare function parse(x: number): string;

type R = ReturnType<typeof parse>; // string
type P = Parameters<typeof parse>; // [x: number]
```

If you need all overloads, there are tricks that match up to a fixed number of signatures, but there's no clean built-in way.

<a id="q341"></a>

### 341: How do you write a type-safe event emitter?

Use a map of event names to payload types and generics with `keyof`.

```ts
type Listener<T> = (payload: T) => void;

class TypedEmitter<Events extends Record<string, unknown>> {
  private listeners: { [E in keyof Events]?: Listener<Events[E]>[] } = {};

  on<E extends keyof Events>(event: E, fn: Listener<Events[E]>) {
    (this.listeners[event] ??= []).push(fn);
  }

  emit<E extends keyof Events>(event: E, payload: Events[E]) {
    this.listeners[event]?.forEach((fn) => fn(payload));
  }
}

const bus = new TypedEmitter<{
  login: { userId: string };
  logout: undefined;
}>();

bus.on("login", (p) => console.log(p.userId));
bus.emit("login", { userId: "1" }); // OK
bus.emit("login", { id: 1 }); // Error
```

<a id="q342"></a>

### 342: How do you write a builder that tracks which fields were set?

Each method returns a new builder type with the field added. The `build` method is only allowed when required fields are present.

```ts
class RequestBuilder<T extends object = {}> {
  private data: Partial<{ url: string; method: string; body: unknown }> = {};

  url(u: string): RequestBuilder<T & { url: string }> {
    this.data.url = u;
    return this as any;
  }

  method(m: "GET" | "POST"): RequestBuilder<T & { method: string }> {
    this.data.method = m;
    return this as any;
  }

  build(this: RequestBuilder<{ url: string; method: string }>) {
    return this.data;
  }
}

new RequestBuilder().url("/a").method("GET").build(); // OK
new RequestBuilder().url("/a").build(); // Error: method is missing
```

The trick is the `this` parameter on `build`.

<a id="q343"></a>

### 343: How do you type a polymorphic "as" prop component in React?

The component accepts an `as` prop with an element type, and its other props change based on it.

```tsx
type PolymorphicProps<E extends React.ElementType, P = {}> = P & {
  as?: E;
} & Omit<React.ComponentPropsWithoutRef<E>, keyof P | "as">;

function Text<E extends React.ElementType = "span">({
  as,
  ...props
}: PolymorphicProps<E, { size?: "sm" | "lg" }>) {
  const Component = as ?? "span";
  return <Component {...props} />;
}

<Text as="a" href="/home">
  Link
</Text>; // href allowed
<Text as="button" onClick={() => {}}>
  Hi
</Text>;
<Text href="/home">Bad</Text>; // Error: span has no href
```

<a id="q344"></a>

### 344: How do you type a higher-order component in React?

The HOC takes a component with props `P` that include the injected props, and returns a component that doesn't require them anymore.

```tsx
interface WithUserProps {
  user: { name: string };
}

function withUser<P extends WithUserProps>(Component: React.ComponentType<P>) {
  return function Wrapped(props: Omit<P, keyof WithUserProps>) {
    const user = { name: "Ann" }; // from context in real code
    return <Component {...(props as P)} user={user} />;
  };
}

function Profile({ user, size }: WithUserProps & { size: number }) {
  return <div style={{ fontSize: size }}>{user.name}</div>;
}

const ProfileWithUser = withUser(Profile);
<ProfileWithUser size={14} />; // user is not needed
```

The `as P` is needed because TypeScript can't prove that `Omit<P, K> & Pick<P, K>` equals `P` for a generic `P`.

<a id="q345"></a>

### 345: How do you type Object.fromEntries so it keeps the keys?

The built-in typing returns `{ [k: string]: T }`. You can write a stricter helper for tuples of known entries.

```ts
type FromEntries<E extends readonly (readonly [PropertyKey, unknown])[]> = {
  [Entry in E[number] as Entry[0]]: Entry[1];
};

function fromEntries<
  const E extends readonly (readonly [PropertyKey, unknown])[],
>(entries: E): FromEntries<E> {
  return Object.fromEntries(entries) as FromEntries<E>;
}

const obj = fromEntries([
  ["a", 1],
  ["b", "x"],
]);
// { a: 1; b: "x" }
```

<a id="q346"></a>

### 346: Does TypeScript support higher-kinded types?

Not directly. You can't write `F<T>` where `F` itself is a type parameter. Libraries work around it with an interface registry, where each "type constructor" is registered under a string key.

```ts
interface URItoKind<A> {
  Array: A[];
  Promise: Promise<A>;
}

type URIS = keyof URItoKind<any>;
type Kind<F extends URIS, A> = URItoKind<A>[F];

interface Functor<F extends URIS> {
  map<A, B>(fa: Kind<F, A>, f: (a: A) => B): Kind<F, B>;
}

const arrayFunctor: Functor<"Array"> = {
  map: (fa, f) => fa.map(f),
};
```

This is the approach used by fp-ts. Libraries like Effect use a similar trick with `this` types.

<a id="q347"></a>

### 347: Why can a function with fewer parameters be assigned to a type with more parameters?

In JavaScript it's normal to ignore extra arguments, so TypeScript allows it.

```ts
type Callback = (item: string, index: number, all: string[]) => void;

const cb: Callback = (item) => console.log(item); // OK

["a", "b"].forEach((x) => console.log(x)); // forEach passes 3 args, we use 1
```

The other way around is an error, because the function would expect arguments that are never passed.

<a id="q348"></a>

### 348: What is ThisType?

`ThisType<T>` is a marker interface. Inside an object literal typed with it, `this` has type `T`. It requires `noImplicitThis`. It's used for APIs like Vue's options API.

```ts
type ObjectDescriptor<D, M> = {
  data: D;
  methods: M & ThisType<D & M>;
};

function makeObject<D, M>(desc: ObjectDescriptor<D, M>): D & M {
  return { ...desc.data, ...desc.methods } as D & M;
}

const obj = makeObject({
  data: { x: 0, y: 0 },
  methods: {
    moveBy(dx: number, dy: number) {
      this.x += dx; // this is { x: number; y: number } & methods
      this.y += dy;
    },
  },
});
```

<a id="q349"></a>

### 349: What is the difference between an intersection of functions and a union of functions?

- An intersection of functions acts like an overloaded function. You can call it with any of the signatures.
- A union of functions can only be called with arguments that work for all members, so the parameters become an intersection.

```ts
type F1 = (x: string) => string;
type F2 = (x: number) => number;

declare const both: F1 & F2;
both("a"); // string
both(1); // number

declare const either: F1 | F2;
either("a"); // Error: string & number is never
```

<a id="q350"></a>

### 350: What is the "correlated union" problem?

It happens when you pick values from two places using the same union key, and TypeScript doesn't know they belong together.

```ts
type Events = {
  click: { x: number };
  key: { code: string };
};

const handlers: { [K in keyof Events]: (e: Events[K]) => void } = {
  click: (e) => console.log(e.x),
  key: (e) => console.log(e.code),
};

function dispatchBad(type: keyof Events, event: Events[keyof Events]) {
  handlers[type](event); // Error: the handler could be for click and the event for key
}
```

The fix (since TypeScript 4.6) is to make the function generic over the key and write the handler map as a mapped type over that same key:

```ts
function dispatch<K extends keyof Events>(type: K, event: Events[K]) {
  const handler: (e: Events[K]) => void = handlers[type];
  handler(event); // OK
}
```

<a id="q351"></a>

### 351: What are the main parts of the TypeScript compiler?

The compiler works in stages:

1. **Scanner**: turns source text into tokens.
2. **Parser**: builds an Abstract Syntax Tree (AST) from the tokens.
3. **Binder**: creates symbols for declarations and connects names to them. It also builds the control flow graph used for narrowing.
4. **Checker**: does the type checking. This is by far the largest part.
5. **Emitter**: writes `.js`, `.d.ts` and `.map` files. Before emitting, transformers remove types and downlevel syntax for the chosen `target`.

The language service (used by editors) is built on top of the same pieces.

<a id="q352"></a>

### 352: How do you use the TypeScript Compiler API?

The `typescript` package exposes the compiler as a library. You can parse code, walk the AST and ask the type checker questions.

```ts
import ts from "typescript";

const program = ts.createProgram(["src/index.ts"], { strict: true });
const checker = program.getTypeChecker();

for (const file of program.getSourceFiles()) {
  if (file.isDeclarationFile) continue;

  ts.forEachChild(file, function visit(node) {
    if (ts.isFunctionDeclaration(node) && node.name) {
      const type = checker.getTypeAtLocation(node);
      console.log(node.name.text, checker.typeToString(type));
    }
    ts.forEachChild(node, visit);
  });
}
```

Tools like ts-morph wrap this API to make it easier to use.

<a id="q353"></a>

### 353: How do you get compile errors programmatically?

Use `ts.getPreEmitDiagnostics` and format them.

```ts
import ts from "typescript";

const program = ts.createProgram(["src/index.ts"], {
  noEmit: true,
  strict: true,
});
const diagnostics = ts.getPreEmitDiagnostics(program);

const host: ts.FormatDiagnosticsHost = {
  getCanonicalFileName: (f) => f,
  getCurrentDirectory: ts.sys.getCurrentDirectory,
  getNewLine: () => ts.sys.newLine,
};

console.log(ts.formatDiagnosticsWithColorAndContext(diagnostics, host));
```

<a id="q354"></a>

### 354: What are custom transformers?

Transformers are functions that change the AST during emit. TypeScript uses them internally, and you can pass your own through the API (`program.emit(..., { before: [...] })`) or with tools like `ts-patch`.

```ts
import ts from "typescript";

const removeConsole: ts.TransformerFactory<ts.SourceFile> = (context) => {
  return (sourceFile) => {
    const visitor = (node: ts.Node): ts.Node | undefined => {
      if (
        ts.isExpressionStatement(node) &&
        ts.isCallExpression(node.expression) &&
        node.expression.expression.getText(sourceFile).startsWith("console.")
      ) {
        return undefined; // remove the statement
      }
      return ts.visitEachChild(node, visitor, context);
    };
    return ts.visitNode(sourceFile, visitor) as ts.SourceFile;
  };
};

program.emit(undefined, undefined, undefined, false, {
  before: [removeConsole],
});
```

Plain `tsc` does not support custom transformers through `tsconfig.json`.

<a id="q355"></a>

### 355: What is a language service plugin?

It is a plugin that changes how the editor experience works (completions, errors, quick fixes) without changing compilation. You add it in `tsconfig.json`:

```json
{
  "compilerOptions": {
    "plugins": [{ "name": "typescript-styled-plugin" }]
  }
}
```

Examples: plugins for CSS-in-JS, GraphQL tags, Next.js and Vue. They only run in the editor (tsserver), not when you run `tsc`.

<a id="q356"></a>

### 356: How do you find out why type checking is slow?

Some tools:

- `tsc --extendedDiagnostics` shows time spent in each phase, number of types, memory used.
- `tsc --generateTrace ./trace` creates a trace you can open in `chrome://tracing` or analyze with `@typescript/analyze-trace` to find slow files and types.
- `tsc --listFiles` or `--explainFiles` shows which files are included and why. Often a slow build is caused by pulling in too many files.

```bash
npx tsc --noEmit --extendedDiagnostics
npx tsc --noEmit --generateTrace ./trace
npx @typescript/analyze-trace ./trace
```

<a id="q357"></a>

### 357: What are common causes of slow type checking?

- Huge unions (thousands of members), especially from template literal types that multiply.
- Deeply recursive conditional types.
- Large intersections instead of interfaces with `extends`.
- Missing return type annotations on complex exported functions, so TypeScript has to infer and print huge types into `.d.ts` files.
- Including more files than needed (for example tests or `node_modules` sources).
- Using libraries with very complex types (some ORMs, schema libraries, styled-system types).

Fixes often include adding explicit types, splitting the project with project references and simplifying generic types.

<a id="q358"></a>

### 358: What does "Type instantiation is excessively deep and possibly infinite" mean?

TypeScript stops when a type needs too many nested instantiations (the limit is around 50 for some cases, 100 for others, and about 1000 for tail-recursive conditional types). It usually means a recursive type has no clear end, or the input is too big.

Ways to fix:

- Make the recursive type tail recursive (use an accumulator).
- Add a depth counter to stop recursion early.
- Break the problem into smaller pieces or simplify the type.

```ts
type Paths<T, Depth extends unknown[] = []> = Depth["length"] extends 5
  ? never
  : T extends object
    ? {
        [K in keyof T & string]: K | `${K}.${Paths<T[K], [...Depth, 0]>}`;
      }[keyof T & string]
    : never;
```

<a id="q359"></a>

### 359: What is isolatedDeclarations?

Added in TypeScript 5.5. It requires that `.d.ts` files can be produced from each file alone, without running the type checker. In practice, exported functions, variables and class members need explicit types when they can't be trivially inferred.

```ts
// Error with isolatedDeclarations
export function getUser() {
  return { id: 1, name: "Ann" };
}

// OK
export function getUser2(): { id: number; name: string } {
  return { id: 1, name: "Ann" };
}
```

The benefit is that fast tools (like esbuild, swc, oxc) can generate declaration files in parallel, which speeds up builds in large monorepos.

<a id="q360"></a>

### 360: What does the error "the inferred type of X cannot be named without a reference to Y" mean?

When creating `.d.ts` files, TypeScript must write the type of every export. If the inferred type comes from a module that your package can't reference directly (for example a nested dependency not in your own `package.json`), it can't write a valid import for it.

```ts
// error TS2742 in a library build
export const store = createStore(); // type lives deep in some internal package
```

Fixes:

- Add an explicit type annotation using a type that is exported publicly.
- Add the dependency directly to your `package.json`.
- Re-export the needed type from the library's public entry point.

<a id="q361"></a>

### 361: How do you ship a package that supports both CommonJS and ESM with correct types?

Each format should have its own declaration file, because the module format affects how types are read.

```json
{
  "name": "my-lib",
  "type": "module",
  "exports": {
    ".": {
      "import": {
        "types": "./dist/esm/index.d.ts",
        "default": "./dist/esm/index.js"
      },
      "require": {
        "types": "./dist/cjs/index.d.cts",
        "default": "./dist/cjs/index.cjs"
      }
    }
  }
}
```

Tools like `tsup` or `tshy` handle this setup. You can check the result with the "Are The Types Wrong?" tool (`@arethetypeswrong/cli`).

<a id="q362"></a>

### 362: What is typesVersions in package.json?

It lets a package serve different type files depending on the TypeScript version of the user. It was also used before `exports` existed to support subpath imports.

```json
{
  "types": "./index.d.ts",
  "typesVersions": {
    "<4.7": { "*": ["ts4.6/*"] }
  }
}
```

<a id="q363"></a>

### 363: What is export as namespace?

It is used in declaration files for UMD libraries, which can be used both as a module and as a global variable (from a script tag).

```ts
// math-lib.d.ts
export function add(a: number, b: number): number;
export as namespace MathLib;
```

```ts
// in a module
import { add } from "math-lib";

// in a script without imports
MathLib.add(1, 2);
```

<a id="q364"></a>

### 364: How can a namespace merge with a function, class or enum?

You can add static-like members to a function or class, or helper functions to an enum.

```ts
function format(value: number) {
  return format.prefix + value.toFixed(format.decimals);
}

namespace format {
  export let prefix = "$";
  export let decimals = 2;
}

enum Color {
  Red,
  Green,
}

namespace Color {
  export function parse(s: string): Color {
    return Color[s as keyof typeof Color];
  }
}

Color.parse("Red");
```

This is mostly seen in declaration files for libraries like jQuery, where `$` is both a function and an object.

<a id="q365"></a>

### 365: How do you add a method to a built-in type like Array?

Augment the global interface, and add the runtime code separately.

```ts
// array-extensions.ts
export {};

declare global {
  interface Array<T> {
    last(): T | undefined;
  }
}

Array.prototype.last = function () {
  return this[this.length - 1];
};
```

Changing built-in prototypes can cause conflicts with other libraries or future JavaScript features, so it's usually better to write a helper function.

<a id="q366"></a>

### 366: What are using declarations?

Added in TypeScript 5.2 (explicit resource management). A `using` variable is disposed automatically when it goes out of scope, by calling its `[Symbol.dispose]()` method. `await using` calls `[Symbol.asyncDispose]()`.

```ts
class TempFile implements Disposable {
  constructor(public path: string) {
    console.log("created", path);
  }
  [Symbol.dispose]() {
    console.log("deleted", this.path);
  }
}

function work() {
  using file = new TempFile("/tmp/a.txt");
  // use file...
} // "deleted /tmp/a.txt" is printed here, even if an error was thrown

async function query() {
  await using conn = await db.connect(); // conn has [Symbol.asyncDispose]
}
```

It's similar to `using` in C#, `with` in Python or `try-with-resources` in Java. You may need a polyfill and `lib: ["esnext.disposable"]`.

<a id="q367"></a>

### 367: What is in the context object of a standard decorator?

The second argument of a standard decorator describes what is being decorated:

- `kind`: `"class"`, `"method"`, `"getter"`, `"setter"`, `"field"` or `"accessor"`.
- `name`: the member name.
- `static` and `private`: booleans.
- `access`: an object with `get` / `set` to read or write the member.
- `addInitializer(fn)`: run code when the class or instance is set up.
- `metadata`: a shared object for storing metadata (TypeScript 5.2+).

```ts
function bound(method: any, context: ClassMethodDecoratorContext) {
  context.addInitializer(function (this: any) {
    this[context.name] = this[context.name].bind(this);
  });
}

class Button {
  label = "OK";

  @bound
  click() {
    console.log(this.label);
  }
}

const { click } = new Button();
click(); // "OK", this is still bound
```

<a id="q368"></a>

### 368: How does decorator metadata work in standard decorators?

Every decorator gets `context.metadata`, an object shared by all decorators of the class. It's later available on the class as `Class[Symbol.metadata]`.

```ts
function column(name: string) {
  return (_: undefined, context: ClassFieldDecoratorContext) => {
    const cols = (context.metadata.columns ??= []) as string[];
    cols.push(name);
  };
}

class User {
  @column("user_id") id = 0;
  @column("user_name") name = "";
}

console.log(User[Symbol.metadata]?.columns); // ["user_id", "user_name"]
```

You may need a polyfill for `Symbol.metadata`.

<a id="q369"></a>

### 369: What is a decorator factory?

A function that takes options and returns the actual decorator.

```ts
function retry(times: number) {
  return function <This, Args extends unknown[], R>(
    target: (this: This, ...args: Args) => Promise<R>,
    context: ClassMethodDecoratorContext<
      This,
      (this: This, ...args: Args) => Promise<R>
    >,
  ) {
    return async function (this: This, ...args: Args): Promise<R> {
      for (let i = 0; ; i++) {
        try {
          return await target.call(this, ...args);
        } catch (e) {
          if (i >= times) throw e;
        }
      }
    };
  };
}

class Api {
  @retry(3)
  async fetchData(id: number) {
    return id;
  }
}
```

The generics keep the original method signature, so wrong uses are type errors.

<a id="q370"></a>

### 370: In what order do decorators run?

- Decorator expressions (like `@retry(3)`) are evaluated top to bottom.
- The decorators themselves are applied bottom to top (closest to the declaration first).
- Member decorators are applied before the class decorator.

```ts
@first
@second
class A {}
// second is applied first, then first
```

<a id="q371"></a>

### 371: Why must assertion functions have an explicit type annotation?

For `asserts` to work, TypeScript needs to know about it during control flow analysis, which happens before it fully infers types. So the function must be declared with an explicit type. Arrow functions assigned to a `const` without a type annotation will not narrow.

```ts
const assertString = (v: unknown): asserts v is string => {
  if (typeof v !== "string") throw new Error();
};

function test(x: unknown) {
  assertString(x); // Error: Assertions require every name in the call target to be declared with an explicit type annotation
}

// fix
const assertString2: (v: unknown) => asserts v is string = (v) => {
  if (typeof v !== "string") throw new Error();
};
```

<a id="q372"></a>

### 372: Why doesn't narrowing a generic value change the return type?

If a function returns a conditional type based on `T`, TypeScript can't check the return statements against it, because narrowing a value of type `T` doesn't narrow `T` itself.

```ts
type Result<T> = T extends string ? number : string;

function convert<T extends string | number>(x: T): Result<T> {
  if (typeof x === "string") {
    return x.length; // Error: number is not assignable to Result<T>
  }
  return String(x); // Error
}
```

Common fixes are overloads, or a cast on the return:

```ts
function convert2(x: string): number;
function convert2(x: number): string;
function convert2(x: string | number) {
  return typeof x === "string" ? x.length : String(x);
}
```

<a id="q373"></a>

### 373: What is the difference between T extends {} and an unconstrained T?

An unconstrained `T` can be anything, including `null` and `undefined`. `T extends {}` excludes `null` and `undefined`. Since TypeScript 4.8, `NonNullable<T>` is simply `T & {}`.

```ts
function a<T>(x: T) {
  x.toString(); // Error: x may be null or undefined
}

function b<T extends {}>(x: T) {
  x.toString(); // OK
}

b(null); // Error
```

<a id="q374"></a>

### 374: Why does TypeScript sometimes infer from the wrong argument?

TypeScript infers generics in rounds. Arguments that are not "context sensitive" (for example, functions with typed parameters, or plain values) are used first. Then context sensitive functions (arrow functions without parameter types) are checked using what was already inferred.

```ts
declare function create<T>(opts: {
  init: () => T;
  update: (value: T) => void;
}): void;

create({
  init: () => 0,
  update: (v) => v.toFixed(), // v is number, inferred from init
});
```

In older versions, the order of properties inside the object mattered. TypeScript 4.7 improved this for object literal methods and properties.

<a id="q375"></a>

### 375: How do excess property checks work with unions?

For a non-discriminated union, an object literal is only checked against the union as a whole. A property is "excess" only if it exists in none of the members, which can let mixed objects through.

```ts
type A = { a: number };
type B = { b: string };

const x: A | B = { a: 1, b: "x" }; // OK: each property exists in some member

type C = { kind: "c"; c: number };
type D = { kind: "d"; d: string };

const y: C | D = { kind: "c", c: 1, d: "x" }; // Error: discriminated unions are checked per member
```

<a id="q376"></a>

### 376: How do you create an "exact" type that rejects extra properties?

TypeScript doesn't have exact types, but you can block extra keys with a generic.

```ts
type Exact<T, Shape> = T & { [K in Exclude<keyof T, keyof Shape>]: never };

interface User {
  name: string;
}

function save<T extends User>(user: Exact<T, User>) {}

const u = { name: "Ann", admin: true };
save(u); // Error: admin is not allowed
save({ name: "Ann" }); // OK
```

<a id="q377"></a>

### 377: Why are template literal types sometimes too big to compute?

A template literal with unions inside produces every combination (cross product). TypeScript limits a union to 100,000 members and reports `Expression produces a union type that is too complex to represent`.

```ts
type Digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9";

type TwoDigits = `${Digit}${Digit}`; // 100 members, fine
type FiveDigits = `${Digit}${Digit}${Digit}${Digit}${Digit}`; // 100,000, too much
```

Use `${number}` or a branded type when the set is huge.

<a id="q378"></a>

### 378: How does Awaited handle thenables?

`Awaited` unwraps any object with a `then` method, not just `Promise`, following what `await` does at runtime. It also unwraps recursively.

```ts
type Thenable = { then(onfulfilled: (value: string) => void): void };

type A = Awaited<Thenable>; // string
type B = Awaited<Promise<Promise<number>>>; // number
type C = Awaited<number>; // number
```

<a id="q379"></a>

### 379: How do recursive type aliases work and what are the limits?

Since TypeScript 3.7, type aliases can refer to themselves inside object types, arrays, tuples and some other places, because those references are evaluated lazily.

```ts
type Json = string | number | boolean | null | Json[] | { [k: string]: Json };
```

But a type alias can't directly refer to itself at the top level without some kind of wrapping:

```ts
type Bad = Bad | string; // Error: circularly references itself
```

<a id="q380"></a>

### 380: How can you get a type from a runtime schema?

Libraries like Zod, Valibot and ArkType let you define a schema once and infer the TypeScript type from it, so the runtime check and the type are always in sync.

```ts
import { z } from "zod";

const UserSchema = z.object({
  id: z.number(),
  email: z.string().email(),
  role: z.enum(["admin", "user"]),
  tags: z.array(z.string()).optional(),
});

type User = z.infer<typeof UserSchema>;
// { id: number; email: string; role: "admin" | "user"; tags?: string[] }

const user = UserSchema.parse(await res.json()); // user: User, validated
```

<a id="q381"></a>

### 381: How do you share types between a frontend and backend?

Some options:

- A shared package in a monorepo with common types (or schemas).
- Generating types from an API spec, for example OpenAPI with `openapi-typescript`, or GraphQL with GraphQL Code Generator.
- End-to-end typed RPC like tRPC, where the client imports only the type of the server router.

```ts
// server
export const appRouter = router({
  getUser: publicProcedure
    .input(z.string())
    .query(({ input }) => db.user.find(input)),
});
export type AppRouter = typeof appRouter;

// client
import type { AppRouter } from "../server";
const trpc = createTRPCClient<AppRouter>({/* ... */});
const user = await trpc.getUser.query("1"); // fully typed, no codegen
```

<a id="q382"></a>

### 382: How do private class fields make classes nominal?

Classes with `private` or `#private` members are only compatible with the same class (or subclasses), even if the shape is the same.

```ts
class USD {
  private readonly __currency = "USD";
  constructor(public amount: number) {}
}

class EUR {
  private readonly __currency = "EUR";
  constructor(public amount: number) {}
}

function payInUsd(m: USD) {}

payInUsd(new EUR(10)); // Error
payInUsd({ amount: 10 } as any); // only possible with any
```

<a id="q383"></a>

### 383: How do you make sure an object handles every member of a union?

Use `satisfies Record<Union, ...>`. You get an error for missing keys and extra keys, while keeping the exact type of each value.

```ts
type Status = "draft" | "published" | "archived";

const statusLabels = {
  draft: "Draft",
  published: "Published",
  archived: "Archived",
} satisfies Record<Status, string>;

// adding "deleted" to Status will now cause an error here
```

<a id="q384"></a>

### 384: What changed in how the in operator narrows unlisted properties?

Since TypeScript 4.9, `"key" in obj` narrows `obj` to have that key even if the type didn't mention it. The property type becomes `unknown`.

```ts
function getId(data: object) {
  if ("id" in data && typeof data.id === "string") {
    return data.id; // string
  }
}
```

Before 4.9, `data.id` was an error after the `in` check.

<a id="q385"></a>

### 385: Can TypeScript narrow destructured discriminated unions?

Yes, since TypeScript 4.6, when the variables are `const` (or parameters that are not reassigned).

```ts
type Action =
  { kind: "add"; payload: number } | { kind: "rename"; payload: string };

function handle({ kind, payload }: Action) {
  if (kind === "add") {
    payload.toFixed(); // number
  } else {
    payload.toUpperCase(); // string
  }
}
```

<a id="q386"></a>

### 386: What is control flow analysis of aliased conditions?

Since TypeScript 4.4, you can store a type check in a `const` and still get narrowing when you use it later.

```ts
function format(value: string | number) {
  const isString = typeof value === "string";

  if (isString) {
    return value.toUpperCase(); // value is string
  }
  return value.toFixed(2);
}
```

This only works if the checked variable is `const` or a `readonly` property, or a parameter that's never reassigned.

<a id="q387"></a>

### 387: What do downlevelIteration and importHelpers do?

- `downlevelIteration` makes `for...of`, spread and destructuring follow the full iteration protocol when compiling to ES5. Without it, they only work correctly with arrays.
- `importHelpers` imports helper functions (like `__awaiter`, `__extends`) from the `tslib` package instead of copying them into every file. This makes output smaller.

```json
{
  "compilerOptions": {
    "target": "ES5",
    "downlevelIteration": true,
    "importHelpers": true
  }
}
```

<a id="q388"></a>

### 388: What does useDefineForClassFields change?

It decides how class fields are created at runtime:

- `true` (default when `target` is ES2022 or later): fields use `Object.defineProperty` semantics, matching the JavaScript standard.
- `false`: fields are set with simple assignment in the constructor (old TypeScript behavior).

The difference matters with inheritance and accessors:

```ts
class Base {
  set value(v: number) {
    console.log("setter called", v);
  }
}

class Child extends Base {
  value = 10;
}

new Child();
// useDefineForClassFields: false -> "setter called 10"
// useDefineForClassFields: true  -> setter is NOT called, a new own property is defined
```

It also breaks code that redeclares a parent property just to change its type. Use `declare` for that: `declare value: number;`.

<a id="q389"></a>

### 389: What is the declare modifier on class fields?

It tells TypeScript about a property's type without creating a field at runtime. Useful when a parent class or a framework sets the property, and you only want a more specific type.

```ts
class Animal {
  sound: string = "...";
}

class Dog extends Animal {
  declare sound: "woof"; // no runtime field, so the parent's value is not overwritten
}
```

<a id="q390"></a>

### 390: What is erasableSyntaxOnly?

Added in TypeScript 5.8. It reports an error for TypeScript features that need code generation, not just type removal:

- `enum` (non-`declare`)
- `namespace` with runtime code
- parameter properties (`constructor(private x: number)`)
- `import x = require()` and `export =`

It exists because Node.js (since v22.6 / v23.6) can run `.ts` files by only stripping types. Those features can't be stripped, so they don't work there.

```ts
// Errors with erasableSyntaxOnly
enum Color {
  Red,
}
class A {
  constructor(public x: number) {}
}
```

<a id="q391"></a>

### 391: What does module preserve do?

`"module": "preserve"` (TypeScript 5.4+) keeps `import` and `export` statements as written, including mixing ESM and `require`. It's meant for projects where a bundler or a runtime like Bun handles modules. It implies `moduleResolution: bundler` and `esModuleInterop`.

```json
{
  "compilerOptions": {
    "module": "preserve",
    "noEmit": true
  }
}
```

<a id="q392"></a>

### 392: What is the native TypeScript compiler (TypeScript 7)?

The TypeScript team is porting the compiler from TypeScript to Go. The new compiler is known as "TypeScript 7" (the project was called Corsa, and the preview is published as `@typescript/native-preview` with the `tsgo` command). The goal is around 10 times faster builds and faster editor startup, with the same type checking behavior. TypeScript 6 is the last version based on the JavaScript codebase and acts as a bridge, deprecating old options that the Go version doesn't support.

```bash
npm install -D @typescript/native-preview
npx tsgo --noEmit
```

<a id="q393"></a>

### 393: Why can't a readonly array be passed where a mutable array is expected?

A mutable array type has methods like `push`. A readonly array doesn't promise them, so it isn't assignable to the mutable type. The other direction is fine.

```ts
function sum(nums: number[]) {}
function sumSafe(nums: readonly number[]) {}

const list = [1, 2, 3] as const;

sum(list); // Error: readonly is not assignable to mutable
sumSafe(list); // OK
sumSafe([1]); // OK, mutable arrays are accepted too
```

That's why library functions should accept `readonly` arrays when they don't modify them.

<a id="q394"></a>

### 394: What is the safest "any function" type?

It depends on what you need:

- `Function`: too loose, calls return `any`.
- `(...args: any[]) => any`: accepts any function, but calling it is unchecked.
- `(...args: never[]) => unknown`: any function is assignable to it (because `never` is assignable to every parameter type), but you can't call it with real arguments by mistake.

```ts
type AnyFn = (...args: never[]) => unknown;

function isFn(x: unknown): x is AnyFn {
  return typeof x === "function";
}

const f: AnyFn = (a: string, b: number) => a + b; // OK
```

Use `(...args: any[]) => any` in generic constraints like `T extends (...args: any[]) => any` because it works better with `infer`.

<a id="q395"></a>

### 395: How do you type an empty object?

`{}` means "any non-null value", not "empty object". To really require an empty object, use `Record<string, never>` or `Record<PropertyKey, never>`.

```ts
const a: {} = { x: 1 }; // OK, surprising
const b: Record<string, never> = {}; // OK
const c: Record<string, never> = { x: 1 }; // Error
```

<a id="q396"></a>

### 396: Why do you sometimes see K & string in template literal types?

`keyof T` can include `number` and `symbol`, and symbols can't be used inside a template literal. Intersecting with `string` keeps only string keys.

```ts
type Getters<T> = {
  [K in keyof T as `get${Capitalize<K & string>}`]: () => T[K];
};

// without "& string": Error: Type 'symbol' is not assignable to type 'string'
```

`Extract<keyof T, string>` does the same thing.

<a id="q397"></a>

### 397: How do you validate string formats with template literal types?

You can use primitive types inside templates, like `${number}`, to describe patterns.

```ts
type Px = `${number}px`;
type Version = `${number}.${number}.${number}`;
type HexColor = `#${string}`;

const w: Px = "100px"; // OK
const bad: Px = "100"; // Error
const v: Version = "1.2.3"; // OK
```

The checks are limited: `${number}` accepts anything that `Number()` would parse, like `"1e3"`.

<a id="q398"></a>

### 398: How do you add types to a library's theme or config through module augmentation?

Many libraries expose an empty interface for you to fill in. For example styled-components and Emotion use `DefaultTheme`:

```ts
// styled.d.ts
import "styled-components";

declare module "styled-components" {
  export interface DefaultTheme {
    colors: { primary: string; text: string };
    spacing: (n: number) => string;
  }
}
```

```ts
const Title = styled.h1`
  color: ${({ theme }) => theme.colors.primary}; /* typed */
`;
```

Vue (`ComponentCustomProperties`), Pinia, i18next and others use the same pattern.

<a id="q399"></a>

### 399: What is the difference between declare var, declare let and declare const in a global declaration?

Inside `declare global`, only `var` declarations become properties of `globalThis` (and `window`). `let` and `const` create global variables that are not on `globalThis`, which matches JavaScript.

```ts
declare global {
  var __APP_VERSION__: string;
  let __DEBUG__: boolean;
}

globalThis.__APP_VERSION__; // OK
globalThis.__DEBUG__; // Error
__DEBUG__; // OK
```

<a id="q400"></a>

### 400: How do you test your types?

Types can break just like code, especially in libraries. Common ways to test them:

- `@ts-expect-error` to check that something does not compile.
- An `Equals` helper with a compile-time assertion.
- Libraries like `expect-type`, `tsd`, or Vitest's built-in `expectTypeOf`.

```ts
import { expectTypeOf, test } from "vitest";

test("getUser types", () => {
  expectTypeOf(getUser).parameter(0).toEqualTypeOf<string>();
  expectTypeOf(getUser).returns.resolves.toMatchTypeOf<{ id: string }>();
});

// without a library
type Expect<T extends true> = T;
type Equals<X, Y> =
  (<T>() => T extends X ? 1 : 2) extends <T>() => T extends Y ? 1 : 2
    ? true
    : false;

type Test1 = Expect<Equals<ReturnType<typeof parseNum>, number>>;

// @ts-expect-error - should not accept a number
parseNum(123);
```

Type tests run when `tsc` runs, so add `tsc --noEmit` to CI.

<a id="q401"></a>

### 401: What is F-bounded polymorphism?

It's when a type parameter is constrained by a type that uses the parameter itself. It lets a base type refer to "the actual subtype".

```ts
interface Comparable<T extends Comparable<T>> {
  compareTo(other: T): number;
}

class Money implements Comparable<Money> {
  constructor(public cents: number) {}
  compareTo(other: Money) {
    return this.cents - other.cents;
  }
}

function max<T extends Comparable<T>>(items: T[]): T {
  return items.reduce((a, b) => (a.compareTo(b) >= 0 ? a : b));
}

max([new Money(5), new Money(10)]); // Money
```

<a id="q402"></a>

### 402: What is the Prettify (or Simplify) type and why is it useful?

When you combine types with `&`, Omit and Pick, the editor tooltip shows the raw formula, which is hard to read. `Prettify` forces TypeScript to flatten it into a plain object type.

```ts
type Prettify<T> = { [K in keyof T]: T[K] } & {};

type A = { id: number } & Omit<{ name: string; secret: string }, "secret">;
// hover: { id: number } & Omit<{ name: string; secret: string }, "secret">

type B = Prettify<A>;
// hover: { id: number; name: string }
```

The `& {}` part helps make sure the editor shows the expanded result.

<a id="q403"></a>

### 403: How do you write a type for a deep merge of two objects?

Properties from the second object win. When both values are plain objects, merge them recursively.

```ts
type IsObject<T> = T extends object
  ? T extends any[] | Function
    ? false
    : true
  : false;

type DeepMerge<A, B> = {
  [K in keyof A | keyof B]: K extends keyof B
    ? K extends keyof A
      ? IsObject<A[K]> extends true
        ? IsObject<B[K]> extends true
          ? DeepMerge<A[K], B[K]>
          : B[K]
        : B[K]
      : B[K]
    : K extends keyof A
      ? A[K]
      : never;
};

type Defaults = { server: { port: number; host: string }; debug: boolean };
type Overrides = { server: { port: string } };

type Merged = DeepMerge<Defaults, Overrides>;
// { server: { port: string; host: string }; debug: boolean }
```

<a id="q404"></a>

### 404: How do you convert all keys of a nested object to camelCase?

Combine a recursive mapped type with key remapping.

```ts
type CamelCase<S extends string> = S extends `${infer H}_${infer T}`
  ? `${H}${Capitalize<CamelCase<T>>}`
  : S;

type DeepCamelKeys<T> = T extends readonly (infer U)[]
  ? DeepCamelKeys<U>[]
  : T extends object
    ? {
        [K in keyof T as K extends string ? CamelCase<K> : K]: DeepCamelKeys<
          T[K]
        >;
      }
    : T;

type ApiUser = {
  user_id: number;
  home_address: { zip_code: string };
  past_orders: { order_id: string }[];
};

type User = DeepCamelKeys<ApiUser>;
// { userId: number; homeAddress: { zipCode: string }; pastOrders: { orderId: string }[] }
```

<a id="q405"></a>

### 405: How do you compute the length of a string literal type?

Split it into characters with recursion, collect them in a tuple, and read `length`.

```ts
type StrLength<
  S extends string,
  Acc extends unknown[] = [],
> = S extends `${string}${infer Rest}`
  ? StrLength<Rest, [...Acc, 0]>
  : Acc["length"];

type L = StrLength<"hello">; // 5
```

`${string}${infer Rest}` matches exactly one character for the first part, because a leading `string` placeholder followed by `infer` takes the shortest match.

<a id="q406"></a>

### 406: How does inference work with multiple infer positions in a template literal?

Each `infer` placeholder that is followed by another placeholder matches as little as possible (one character for the first placeholder, or up to the first delimiter). The last one takes the rest.

```ts
type FirstChar<S> = S extends `${infer F}${infer _}` ? F : never;
type A = FirstChar<"abc">; // "a"

type BeforeDot<S> = S extends `${infer H}.${infer T}` ? [H, T] : never;
type B = BeforeDot<"a.b.c">; // ["a", "b.c"] - split at the first dot
```

To split at the last dot, you have to recurse.

<a id="q407"></a>

### 407: How does addEventListener know the event type from the event name?

The DOM types use an event map interface and overloads with `keyof`.

```ts
// simplified from lib.dom.d.ts
interface HTMLElementEventMap {
  click: MouseEvent;
  keydown: KeyboardEvent;
  input: Event;
}

interface MyElement {
  addEventListener<K extends keyof HTMLElementEventMap>(
    type: K,
    listener: (ev: HTMLElementEventMap[K]) => void,
  ): void;
  addEventListener(type: string, listener: (ev: Event) => void): void;
}
```

You can use the same pattern for your own APIs: a map interface plus `K extends keyof Map`.

<a id="q408"></a>

### 408: How do you type a Proxy?

`new Proxy<T>(target, handler)` returns `T`. If the proxy adds behavior not in the target, describe the result type yourself.

```ts
function createLogger<T extends object>(target: T): T {
  return new Proxy(target, {
    get(obj, prop, receiver) {
      console.log(`read ${String(prop)}`);
      return Reflect.get(obj, prop, receiver);
    },
  });
}

type Api = { [K in `get${Capitalize<string>}`]: () => Promise<unknown> };

const api = new Proxy({} as Api, {
  get: (_, prop: string) => () => fetch(`/api/${prop.slice(3).toLowerCase()}`),
});

api.getUsers(); // typed by the Api type
```

<a id="q409"></a>

### 409: How do you build a typed dependency injection container?

Use tokens that carry the type of the value as a phantom type.

```ts
class Token<T> {
  declare readonly _type: T; // phantom, no runtime value
  constructor(public readonly name: string) {}
}

class Container {
  private providers = new Map<Token<any>, () => any>();

  register<T>(token: Token<T>, factory: () => T) {
    this.providers.set(token, factory);
  }

  resolve<T>(token: Token<T>): T {
    const factory = this.providers.get(token);
    if (!factory) throw new Error(`No provider for ${token.name}`);
    return factory();
  }
}

const LOGGER = new Token<{ log(msg: string): void }>("Logger");

const c = new Container();
c.register(LOGGER, () => console);
c.resolve(LOGGER).log("hi"); // typed
c.register(LOGGER, () => 42); // Error
```

Angular's `InjectionToken<T>` works the same way.

<a id="q410"></a>

### 410: How do you type a state machine so only valid transitions are allowed?

Describe the transitions as a type and look up the allowed next states.

```ts
type Transitions = {
  idle: "loading";
  loading: "success" | "error";
  success: "idle";
  error: "idle" | "loading";
};

type State = keyof Transitions;

class Machine<S extends State> {
  constructor(public state: S) {}

  to<N extends Transitions[S]>(next: N): Machine<N> {
    return new Machine(next);
  }
}

new Machine("idle").to("loading").to("success"); // OK
new Machine("idle").to("success"); // Error
```

<a id="q411"></a>

### 411: How do you get a single member from a discriminated union?

Use `Extract` with the discriminant.

```ts
type Action =
  | { type: "add"; item: string }
  | { type: "remove"; id: number }
  | { type: "clear" };

type RemoveAction = Extract<Action, { type: "remove" }>;
// { type: "remove"; id: number }

type ActionType = Action["type"]; // "add" | "remove" | "clear"
```

<a id="q412"></a>

### 412: How do you turn a discriminated union into a map of handlers?

Use a mapped type with key remapping over the union members.

```ts
type Action = { type: "add"; item: string } | { type: "remove"; id: number };

type Handlers<U extends { type: string }> = {
  [M in U as M["type"]]: (action: M) => void;
};

const handlers: Handlers<Action> = {
  add: (a) => console.log(a.item),
  remove: (a) => console.log(a.id),
};
```

Here `M` goes over each member of the union, not over keys. This is allowed because of the `as` clause.

<a id="q413"></a>

### 413: How do you type a reducer built from a handler map?

Combine the handler map with a generic dispatch function.

```ts
type Events = {
  deposit: { amount: number };
  withdraw: { amount: number };
  close: {};
};

type State = { balance: number; open: boolean };

const reducers: { [K in keyof Events]: (s: State, p: Events[K]) => State } = {
  deposit: (s, p) => ({ ...s, balance: s.balance + p.amount }),
  withdraw: (s, p) => ({ ...s, balance: s.balance - p.amount }),
  close: (s) => ({ ...s, open: false }),
};

function reduce<K extends keyof Events>(
  state: State,
  type: K,
  payload: Events[K],
): State {
  return reducers[type](state, payload);
}

reduce({ balance: 0, open: true }, "deposit", { amount: 10 }); // OK
reduce({ balance: 0, open: true }, "deposit", {}); // Error
```

<a id="q414"></a>

### 414: How do you build a type-safe API client from a route map?

Describe each route once, then derive the client's types from it.

```ts
interface Routes {
  "GET /users": { query: { page: number }; response: { id: string }[] };
  "GET /users/:id": {
    params: { id: string };
    response: { id: string; name: string };
  };
  "POST /users": { body: { name: string }; response: { id: string } };
}

type RequestOptions<R> = Omit<R, "response">;

declare function request<K extends keyof Routes>(
  route: K,
  options: RequestOptions<Routes[K]>,
): Promise<Routes[K]["response"]>;

const user = await request("GET /users/:id", { params: { id: "1" } });
user.name; // string

await request("POST /users", { body: { title: "x" } }); // Error
```

<a id="q415"></a>

### 415: Why does includes fail on a readonly array of literals and how do you fix it?

`includes` on `readonly ("a" | "b")[]` only accepts `"a" | "b"`, so passing a general `string` is an error. That's exactly the case where you want to check.

```ts
const ROLES = ["admin", "user"] as const;
type Role = (typeof ROLES)[number];

function isRole(value: string): value is Role {
  return ROLES.includes(value); // Error: string is not assignable to "admin" | "user"
}
```

Fixes:

```ts
function isRole2(value: string): value is Role {
  return (ROLES as readonly string[]).includes(value);
}

// or a reusable helper
function includes<T extends U, U>(list: readonly T[], value: U): value is T {
  return list.includes(value as T);
}
```

<a id="q416"></a>

### 416: How is Object.groupBy typed?

`Object.groupBy` (ES2024, TypeScript 5.4+) returns `Partial<Record<K, T[]>>`, because some groups may have no items.

```ts
const people = [
  { name: "Ann", age: 17 },
  { name: "Bob", age: 30 },
];

const groups = Object.groupBy(people, (p) => (p.age >= 18 ? "adult" : "minor"));
// Partial<Record<"adult" | "minor", { name: string; age: number }[]>>

groups.adult?.length; // must use ?. since the group might be missing
```

`Map.groupBy` returns `Map<K, T[]>`.

<a id="q417"></a>

### 417: What is the difference between unknown[] and any[] in generic constraints?

Both accept any array, but they behave differently in conditional types and with function parameters.

```ts
type Fn1 = (...args: unknown[]) => void;
type Fn2 = (...args: any[]) => void;

const f = (x: string) => {};

const a: Fn1 = f; // Error: unknown is not assignable to string
const b: Fn2 = f; // OK
```

So for "any function" constraints, use `any[]` (or `never[]`). For "any array of values" like `T extends unknown[]`, `unknown[]` is safer.

<a id="q418"></a>

### 418: Why can't you pass only some type arguments and let TypeScript infer the rest?

TypeScript doesn't support partial type argument inference. If you pass one type argument explicitly, the others use their defaults (or `unknown`), not inference.

```ts
declare function create<T, K extends keyof T>(key: K): T[K];

create<{ a: string }>("a"); // Error: Expected 2 type arguments
```

A common workaround is currying: one function takes the explicit type, and it returns another function where the rest is inferred.

```ts
function create2<T>() {
  return <K extends keyof T>(key: K): T[K] => undefined as any;
}

const value = create2<{ a: string; b: number }>()("b"); // number
```

<a id="q419"></a>

### 419: What is higher order function type inference?

Since TypeScript 3.4, when you pass a generic function to another generic function, the result can stay generic instead of being fixed to `unknown`.

```ts
function compose<A extends unknown[], B, C>(
  f: (...args: A) => B,
  g: (b: B) => C,
) {
  return (...args: A) => g(f(...args));
}

const toArray = <T>(x: T): T[] => [x];
const first = <T>(arr: T[]): T => arr[0];

const identity = compose(toArray, first);
// <T>(x: T) => T  - still generic

identity("a"); // string
identity(1); // number
```

<a id="q420"></a>

### 420: How do you write a generic constraint that depends on another type parameter?

Type parameters can refer to earlier ones in their constraints and defaults.

```ts
function setField<T, K extends keyof T, V extends T[K]>(
  obj: T,
  key: K,
  value: V,
): void {
  obj[key] = value;
}

const user = { name: "Ann", age: 30 };
setField(user, "age", 31); // OK
setField(user, "age", "old"); // Error

interface Paginated<T, K extends keyof T = keyof T> {
  items: T[];
  sortBy: K;
}
```

<a id="q421"></a>

### 421: How does a conditional type behave when the input is any or boolean?

- `boolean` is really `true | false`, so a distributive conditional runs for both.
- `any` produces the union of both branches.

```ts
type Check<T> = T extends true ? "yes" : "no";

type A = Check<boolean>; // "yes" | "no"
type B = Check<any>; // "yes" | "no"
type C = Check<never>; // never
```

This can be surprising when you write helpers like `IsTrue<T>`.

<a id="q422"></a>

### 422: When does TypeScript defer a conditional type?

If the checked type is still a generic that isn't known yet, TypeScript can't decide which branch to pick, so it leaves the conditional type unresolved.

```ts
type IsString<T> = T extends string ? true : false;

function f<T>(x: T) {
  const r: IsString<T> = true; // Error: true is not assignable to IsString<T>
}
```

Inside the function `T` is unknown, so `IsString<T>` stays as it is. It only resolves when the function is called with a real type.

<a id="q423"></a>

### 423: Do mapped types with key remapping keep property modifiers?

Yes, if the mapping is over `keyof T`. The modifiers come from the original property, even if the key gets a new name.

```ts
type Prefix<T> = {
  [K in keyof T as `_${K & string}`]: T[K];
};

type R = Prefix<{ readonly id: number; name?: string }>;
// { readonly _id: number; _name?: string }
```

<a id="q424"></a>

### 424: How do you keep generics when using forwardRef or memo?

`forwardRef` and `memo` return a non-generic component type, so the generic is lost. A common fix is to cast the result to a generic function signature.

```tsx
interface SelectProps<T> {
  options: T[];
  getLabel: (o: T) => string;
}

function SelectInner<T>(
  props: SelectProps<T>,
  ref: React.ForwardedRef<HTMLSelectElement>,
) {
  return (
    <select ref={ref}>
      {props.options.map((o) => (
        <option key={props.getLabel(o)}>{props.getLabel(o)}</option>
      ))}
    </select>
  );
}

export const Select = React.forwardRef(SelectInner) as <T>(
  props: SelectProps<T> & { ref?: React.Ref<HTMLSelectElement> },
) => React.ReactElement;
```

With React 19, `ref` is a normal prop, so you can just write a generic function component without `forwardRef`.

<a id="q425"></a>

### 425: What is the difference between a script file and a module file in TypeScript?

A file with any top-level `import` or `export` is a module. Its declarations are local to the file. A file without them is a script, and its top-level declarations are global.

```ts
// globals.d.ts - script, everything is global
declare const VERSION: string;

// other.d.ts - module, needs declare global for globals
export {};
declare global {
  const BUILD_ID: string;
}
```

This is why adding one `import` to a `.d.ts` file can suddenly make its global types disappear.

<a id="q426"></a>

### 426: What does the moduleDetection option do?

It controls how TypeScript decides if a file is a module.

- `auto` (default): a file is a module if it has `import`/`export`, or if `package.json` has `"type": "module"`, or the file is `.mts`/`.cts`, or it's JSX with the `react-jsx` setting.
- `force`: every non-declaration file is a module. This avoids accidental global declarations.
- `legacy`: only `import`/`export` count.

```json
{
  "compilerOptions": {
    "moduleDetection": "force"
  }
}
```

<a id="q427"></a>

### 427: How do you migrate a large JavaScript codebase to TypeScript?

A common plan:

1. Add `tsconfig.json` with `allowJs: true` and `strict: false`. Get the build working.
2. Rename files from `.js` to `.ts` one by one, starting with leaf modules (utilities with no dependencies).
3. Install `@types/...` for libraries.
4. Turn on `noImplicitAny`, fix errors, then move to `strictNullChecks` and finally `strict`.
5. Use `// @ts-expect-error` or temporary `any` to unblock, and track them so they get removed.
6. Add `tsc --noEmit` to CI so new errors can't be added.

Tools like `ts-migrate` (from Airbnb) can automate much of the renaming and annotations. For strict mode in a huge codebase, some teams use a plugin that only enforces `strict` on files listed in an allowlist.

<a id="q428"></a>

### 428: What is "any infection" and how do you prevent it?

Once a value is `any`, everything you get from it is also `any`, so type checking silently disappears through the code.

```ts
const data: any = JSON.parse(input);
const name = data.user.name; // any
const upper = name.toUpperCase(); // any
sendEmail(upper); // no check at all
```

To prevent it:

- Use `unknown` instead of `any` for untrusted data.
- Turn on `typescript-eslint` rules like `no-explicit-any`, `no-unsafe-assignment`, `no-unsafe-member-access`, `no-unsafe-call` and `no-unsafe-return`.
- Wrap untyped libraries in small typed functions.

<a id="q429"></a>

### 429: What are type-aware lint rules?

Some `typescript-eslint` rules use the type checker to find bugs that syntax alone can't. They need `parserOptions.projectService` (or `project`) to be set.

Useful ones:

- `no-floating-promises`: a Promise that isn't awaited or handled.
- `no-misused-promises`: passing an async function where a sync callback is expected.
- `await-thenable`: awaiting something that isn't a Promise.
- `switch-exhaustiveness-check`: missing cases for a union.
- `strict-boolean-expressions`: unclear truthiness checks.

```ts
async function save() {}

function onClick() {
  save(); // no-floating-promises: errors here are lost
}
```

<a id="q430"></a>

### 430: Can circular imports between type-only modules cause problems?

Type-only imports (`import type`) are removed in the output, so they never cause runtime cycles. Circular references between types are fine for TypeScript too.

The problems come from circular imports of values, like classes and constants, which can be `undefined` when a module is evaluated. Using `import type` for imports that are only types helps keep the runtime graph clean.

```ts
// user.ts
import type { Post } from "./post";
export class User {
  posts: Post[] = [];
}

// post.ts
import type { User } from "./user";
export class Post {
  author!: User;
}
```

<a id="q431"></a>

### 431: How do you set up TypeScript in a monorepo?

A common setup:

- A shared base config, for example `tsconfig.base.json`, with common `compilerOptions`.
- Each package has its own `tsconfig.json` that `extends` the base and sets `composite: true`.
- The root `tsconfig.json` lists packages in `references`, and you build with `tsc -b`.
- Packages depend on each other through the package manager workspace (`"@acme/utils": "workspace:*"`), not through relative paths.

```json
// packages/app/tsconfig.json
{
  "extends": "../../tsconfig.base.json",
  "compilerOptions": { "composite": true, "outDir": "dist", "rootDir": "src" },
  "references": [{ "path": "../utils" }]
}
```

Some teams skip building internal packages and point `exports` directly to `.ts` sources, letting the app's bundler compile them.

<a id="q432"></a>

### 432: What changed with enums in TypeScript 5.0?

All enums became union enums. Before 5.0, a numeric enum accepted any number. Now assigning a number literal that isn't a member is an error.

```ts
enum Level {
  Low = 1,
  High = 2,
}

let l: Level = 5; // Error in 5.0+, allowed before
```

Enum members can also now be computed from other constants, and each member gets its own type.

<a id="q433"></a>

### 433: What is intersection reduction to never?

Since TypeScript 3.9, an intersection of object types with conflicting discriminant properties is reduced to `never` as a whole, not just the property.

```ts
type A = { kind: "a"; value: string };
type B = { kind: "b"; value: number };

type C = A & B; // never (not { kind: never; value: ... })
```

This makes errors clearer and helps when intersecting unions.

<a id="q434"></a>

### 434: How does instanceof narrowing work with Symbol.hasInstance?

Since TypeScript 5.3, if a class defines a static `[Symbol.hasInstance]` method that is a type predicate, `instanceof` uses it for narrowing.

```ts
interface PointLike {
  x: number;
  y: number;
}

class Point {
  static [Symbol.hasInstance](value: unknown): value is PointLike {
    return (
      typeof value === "object" &&
      value !== null &&
      "x" in value &&
      "y" in value
    );
  }
}

function f(v: unknown) {
  if (v instanceof Point) {
    v.x; // v is PointLike
  }
}
```

<a id="q435"></a>

### 435: What are iterator helper types in TypeScript 5.6?

TypeScript 5.6 added `IteratorObject` and types for the new ES iterator helpers like `map`, `filter`, `take` and `toArray`, which work directly on iterators.

```ts
function* naturals() {
  let n = 0;
  while (true) yield n++;
}

const evens = naturals()
  .filter((n) => n % 2 === 0)
  .map((n) => n * 10)
  .take(3)
  .toArray(); // number[] -> [0, 20, 40]
```

Built-in iterators like `Map.prototype.entries()` now return `MapIterator<T>` instead of `IterableIterator<T>`. You need `lib: ["esnext"]` and a runtime that supports these helpers.

<a id="q436"></a>

### 436: How do you type a function expression with a given type but keep its inferred return type?

Using a type annotation fixes the return type to what the annotation says. Using `satisfies` checks it against the type but keeps the details.

```ts
type Loader = (id: string) => Promise<unknown>;

const loadUser = (async (id: string) => ({ id, name: "Ann" })) satisfies Loader;

const u = await loadUser("1");
u.name; // string - not unknown
```

<a id="q437"></a>

### 437: How do you write type-safe translation keys?

Derive the keys from the default language file with a recursive paths type.

```ts
const en = {
  home: { title: "Welcome", subtitle: "Hello {name}" },
  errors: { notFound: "Not found" },
} as const;

type Leaves<T> = {
  [K in keyof T & string]: T[K] extends string ? K : `${K}.${Leaves<T[K]>}`;
}[keyof T & string];

type TranslationKey = Leaves<typeof en>;
// "home.title" | "home.subtitle" | "errors.notFound"

declare function t(key: TranslationKey): string;

t("home.title"); // OK
t("home.titel"); // Error
```

You can go further and parse `{name}` placeholders with template literal types to require the right parameters.

<a id="q438"></a>

### 438: How do you require the right parameters for a message with placeholders?

Extract `{name}` style placeholders from a string literal type.

```ts
type Params<S extends string> = S extends `${string}{${infer P}}${infer Rest}`
  ? { [K in P | keyof Params<Rest>]: string | number }
  : {};

declare function format<S extends string>(
  template: S,
  params: Params<S>,
): string;

format("Hello {name}, you have {count} messages", { name: "Ann", count: 3 }); // OK
format("Hello {name}", {}); // Error
```

<a id="q439"></a>

### 439: How do you get the type of the whole Redux store state?

Infer it from the store or root reducer instead of writing it by hand.

```ts
import { configureStore } from "@reduxjs/toolkit";

export const store = configureStore({
  reducer: { user: userReducer, cart: cartReducer },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

// typed hooks
export const useAppSelector = useSelector.withTypes<RootState>();
export const useAppDispatch = useDispatch.withTypes<AppDispatch>();
```

When reducers change, the types update automatically.

<a id="q440"></a>

### 440: Can a discriminated union use more than one discriminant or a boolean discriminant?

Yes. Any property with literal types (including `true`/`false`) can be a discriminant, and you can narrow by several.

```ts
type Result<T> = { ok: true; value: T } | { ok: false; error: Error };

function unwrap<T>(r: Result<T>): T {
  if (r.ok) return r.value;
  throw r.error;
}

type Shape =
  | { kind: "circle"; filled: true; color: string }
  | { kind: "circle"; filled: false }
  | { kind: "square"; size: number };

function draw(s: Shape) {
  if (s.kind === "circle" && s.filled) {
    s.color; // OK
  }
}
```

<a id="q441"></a>

### 441: Is a tuple assignable to an array and vice versa?

A tuple is assignable to an array of the union of its element types. An array is not assignable to a tuple, because the array might have a different length.

```ts
const t: [string, number] = ["a", 1];
const arr: (string | number)[] = t; // OK

const arr2: string[] = ["a", "b"];
const t2: [string, string] = arr2; // Error: Target requires 2 elements but source may have fewer
```

<a id="q442"></a>

### 442: What is the difference between an index signature [key: string] and a mapped type [K in string]?

They result in the same type. A mapped type over `string` produces an index signature.

```ts
type A = { [key: string]: number };
type B = { [K in string]: number };
// A and B are the same
```

The difference is that mapped types can do things index signatures can't, like using the key in the value type or mapping over a union of literal keys.

<a id="q443"></a>

### 443: How do you type a generic factory that creates instances of classes with constructor arguments?

Combine a construct signature with `ConstructorParameters` and `InstanceType`.

```ts
function make<C extends new (...args: any[]) => any>(
  Ctor: C,
  ...args: ConstructorParameters<C>
): InstanceType<C> {
  return new Ctor(...args);
}

class Point {
  constructor(
    public x: number,
    public y: number,
  ) {}
}

const p = make(Point, 1, 2); // Point
make(Point, "1", 2); // Error
```

<a id="q444"></a>

### 444: How do you avoid the "excessive stack depth" error when comparing large generic types?

This error (`Excessive stack depth comparing types`) happens when TypeScript compares two deep recursive types. Some ways to fix it:

- Add explicit type annotations so TypeScript doesn't need to compare deeply inferred types.
- Use `interface` instead of type aliases for recursive object types, because interfaces are compared by name and cached.
- Add variance annotations (`in`/`out`) on generic interfaces so TypeScript can skip structural comparison.
- Reduce the depth of the recursive types.

<a id="q445"></a>

### 445: How do you type a function that accepts an object and returns a version with some keys made optional?

Combine `Omit`, `Pick` and `Partial`.

```ts
type PartialBy<T, K extends keyof T> = Omit<T, K> & Partial<Pick<T, K>>;

interface User {
  id: string;
  name: string;
  createdAt: Date;
}

type NewUser = PartialBy<User, "id" | "createdAt">;
// { name: string; id?: string; createdAt?: Date }

function createUser(input: NewUser): User {
  return { id: crypto.randomUUID(), createdAt: new Date(), ...input };
}
```

<a id="q446"></a>

### 446: How do you write an "Opaque" type that only one module can create?

Combine a brand with a module-private `unique symbol`, and export only a parse function and the type.

```ts
// money.ts
declare const brand: unique symbol;

export type Cents = number & { readonly [brand]: "Cents" };

export function cents(value: number): Cents {
  if (!Number.isInteger(value)) throw new Error("Cents must be an integer");
  return value as Cents;
}

export function add(a: Cents, b: Cents): Cents {
  return (a + b) as Cents;
}
```

```ts
// other.ts
import { cents, add, type Cents } from "./money";

add(cents(100), cents(50)); // OK
add(100, 50); // Error
```

Since `brand` is not exported, other modules can't create a `Cents` value without going through `cents()`.

<a id="q447"></a>

### 447: Why does spreading an object skip the excess property check?

Excess property checks only apply to properties written directly in an object literal. Properties that come from a spread are not checked.

```ts
interface Point {
  x: number;
  y: number;
}

const extra = { x: 1, y: 2, z: 3 };

const p1: Point = { x: 1, y: 2, z: 3 }; // Error
const p2: Point = { ...extra }; // OK, z is not checked
```

<a id="q448"></a>

### 448: What is the difference between IterableIterator and Generator?

- `Iterator<T>` has a `next()` method.
- `IterableIterator<T>` is an iterator that also has `[Symbol.iterator]()`, so it works with `for...of`.
- `Generator<T, TReturn, TNext>` is what generator functions return. It is an iterable iterator with `return()` and `throw()`, and it also types the return value and the value passed to `next()`.

```ts
function* counter(): Generator<number, string, boolean> {
  const reset = yield 1; // reset: boolean (from next(value))
  return reset ? "reset" : "done";
}

const g = counter();
g.next(); // { value: 1, done: false }
g.next(true); // { value: "reset", done: true }
```

<a id="q449"></a>

### 449: How do you require that a generic type argument is passed explicitly?

If a type parameter can't be inferred from the arguments, it falls back to its default (or `unknown`). Give it a default of `never` so that forgetting it causes an error as soon as the result is used.

```ts
function fetchJson<T = never>(url: string): Promise<T> {
  return fetch(url).then((r) => r.json());
}

const a = await fetchJson("/api");
a.id; // Error: Property 'id' does not exist on type 'never'

const b = await fetchJson<{ id: number }>("/api");
b.id; // number
```

<a id="q450"></a>

### 450: How do you type a promisify function?

`promisify` turns a Node.js style callback function into a function that returns a Promise. Variadic tuples and `infer` let you pull the argument list and result type out of the callback signature.

```ts
type Callback<T> = (err: Error | null, result: T) => void;

function promisify<Args extends unknown[], T>(
  fn: (...args: [...Args, Callback<T>]) => void,
): (...args: Args) => Promise<T> {
  return (...args) =>
    new Promise((resolve, reject) => {
      fn(...args, (err, result) => (err ? reject(err) : resolve(result)));
    });
}

function readConfig(path: string, cb: Callback<{ port: number }>) {
  cb(null, { port: 3000 });
}

const readConfigAsync = promisify(readConfig);
const config = await readConfigAsync("app.json"); // { port: number }
readConfigAsync(42); // Error
```

[Back to top](#table-of-contents)
