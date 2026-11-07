# React Popular Libraries Interview Questions and Answers

_Last updated: October 28, 2026_

450 interview questions with answers about the libraries people use most with React, split into three levels: 150 easy, 150 moderate and 150 advanced.

The questions cover routing (React Router, TanStack Router), state management (Redux Toolkit, Zustand, Jotai, MobX, XState), data fetching (TanStack Query, SWR, RTK Query, Apollo, tRPC), forms and validation (React Hook Form, Zod), UI kits (MUI, shadcn/ui, Radix, Base UI, Chakra, Mantine, Ant Design, React Aria), styling, animation, tables, charts, i18n, dates, testing (React Testing Library, Vitest, MSW, Playwright, Storybook) and a set of smaller utility libraries. The examples use React 19, React Router v7/v8, TanStack Query v5, Redux Toolkit 2, Zustand 5, Tailwind CSS v4 and Zod 4. Older libraries and APIs are mentioned where you will still see them in real projects.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What do people usually mean by "React libraries"?](#1-what-do-people-usually-mean-by-react-libraries)
- [2: Why does a typical React project use so many third-party libraries?](#2-why-does-a-typical-react-project-use-so-many-third-party-libraries)
- [3: How do you decide if a library is worth adding to a project?](#3-how-do-you-decide-if-a-library-is-worth-adding-to-a-project)
- [4: What is React Router?](#4-what-is-react-router)
- [5: How do you set up React Router in data mode?](#5-how-do-you-set-up-react-router-in-data-mode)
- [6: What is the difference between Link and NavLink in React Router?](#6-what-is-the-difference-between-link-and-navlink-in-react-router)
- [7: How do you read URL params in React Router?](#7-how-do-you-read-url-params-in-react-router)
- [8: How do you navigate from code in React Router?](#8-how-do-you-navigate-from-code-in-react-router)
- [9: What are nested routes and what is Outlet?](#9-what-are-nested-routes-and-what-is-outlet)
- [10: What is a loader in React Router?](#10-what-is-a-loader-in-react-router)
- [11: What is an action in React Router?](#11-what-is-an-action-in-react-router)
- [12: What is TanStack Router?](#12-what-is-tanstack-router)
- [13: What is Redux Toolkit?](#13-what-is-redux-toolkit)
- [14: How do you create a simple Redux Toolkit store?](#14-how-do-you-create-a-simple-redux-toolkit-store)
- [15: How do components read and update Redux state?](#15-how-do-components-read-and-update-redux-state)
- [16: What is Zustand?](#16-what-is-zustand)
- [17: How do you create and use a Zustand store?](#17-how-do-you-create-and-use-a-zustand-store)
- [18: What is Jotai?](#18-what-is-jotai)
- [19: How do you use an atom in Jotai?](#19-how-do-you-use-an-atom-in-jotai)
- [20: What is MobX?](#20-what-is-mobx)
- [21: What was Recoil and should you use it today?](#21-what-was-recoil-and-should-you-use-it-today)
- [22: What is Valtio?](#22-what-is-valtio)
- [23: What is XState?](#23-what-is-xstate)
- [24: What is TanStack Query?](#24-what-is-tanstack-query)
- [25: How do you fetch data with useQuery?](#25-how-do-you-fetch-data-with-usequery)
- [26: What is a query key in TanStack Query?](#26-what-is-a-query-key-in-tanstack-query)
- [27: How do you send data to the server with useMutation?](#27-how-do-you-send-data-to-the-server-with-usemutation)
- [28: What is SWR?](#28-what-is-swr)
- [29: What is Axios?](#29-what-is-axios)
- [30: Should you use Axios or fetch in a React app?](#30-should-you-use-axios-or-fetch-in-a-react-app)
- [31: What is ky?](#31-what-is-ky)
- [32: What is Apollo Client?](#32-what-is-apollo-client)
- [33: What is urql?](#33-what-is-urql)
- [34: What is tRPC?](#34-what-is-trpc)
- [35: What is React Hook Form?](#35-what-is-react-hook-form)
- [36: How do you build a simple form with React Hook Form?](#36-how-do-you-build-a-simple-form-with-react-hook-form)
- [37: What is Formik and is it still a good choice?](#37-what-is-formik-and-is-it-still-a-good-choice)
- [38: What is Zod?](#38-what-is-zod)
- [39: How do you define a schema and get a type from it in Zod?](#39-how-do-you-define-a-schema-and-get-a-type-from-it-in-zod)
- [40: What is Yup?](#40-what-is-yup)
- [41: What is Valibot?](#41-what-is-valibot)
- [42: What is TanStack Form?](#42-what-is-tanstack-form)
- [43: What is MUI?](#43-what-is-mui)
- [44: How do you install and use Material UI?](#44-how-do-you-install-and-use-material-ui)
- [45: What is shadcn/ui?](#45-what-is-shadcnui)
- [46: How is shadcn/ui different from a normal component library?](#46-how-is-shadcnui-different-from-a-normal-component-library)
- [47: What is Radix UI?](#47-what-is-radix-ui)
- [48: What is Base UI?](#48-what-is-base-ui)
- [49: What is Chakra UI?](#49-what-is-chakra-ui)
- [50: What is Mantine?](#50-what-is-mantine)
- [51: What is Ant Design?](#51-what-is-ant-design)
- [52: What is React Bootstrap?](#52-what-is-react-bootstrap)
- [53: What is Headless UI?](#53-what-is-headless-ui)
- [54: What is React Aria?](#54-what-is-react-aria)
- [55: How is Tailwind CSS used in React projects?](#55-how-is-tailwind-css-used-in-react-projects)
- [56: What is clsx?](#56-what-is-clsx)
- [57: What is tailwind-merge?](#57-what-is-tailwind-merge)
- [58: What is class-variance-authority (cva)?](#58-what-is-class-variance-authority-cva)
- [59: What is styled-components?](#59-what-is-styled-components)
- [60: What is Emotion?](#60-what-is-emotion)
- [61: What are CSS Modules?](#61-what-are-css-modules)
- [62: What is vanilla-extract?](#62-what-is-vanilla-extract)
- [63: What is StyleX?](#63-what-is-stylex)
- [64: What is Panda CSS?](#64-what-is-panda-css)
- [65: What is Motion (formerly Framer Motion)?](#65-what-is-motion-formerly-framer-motion)
- [66: How do you animate an element with Motion?](#66-how-do-you-animate-an-element-with-motion)
- [67: What is React Spring?](#67-what-is-react-spring)
- [68: What is AutoAnimate?](#68-what-is-autoanimate)
- [69: What is Recharts?](#69-what-is-recharts)
- [70: How do you create a simple line chart with Recharts?](#70-how-do-you-create-a-simple-line-chart-with-recharts)
- [71: What is Nivo?](#71-what-is-nivo)
- [72: What is visx?](#72-what-is-visx)
- [73: What is react-chartjs-2?](#73-what-is-react-chartjs-2)
- [74: What is TanStack Table?](#74-what-is-tanstack-table)
- [75: What is AG Grid?](#75-what-is-ag-grid)
- [76: What is the MUI X Data Grid?](#76-what-is-the-mui-x-data-grid)
- [77: What is TanStack Virtual?](#77-what-is-tanstack-virtual)
- [78: What is react-window?](#78-what-is-react-window)
- [79: What is react-virtuoso?](#79-what-is-react-virtuoso)
- [80: What is react-i18next?](#80-what-is-react-i18next)
- [81: How do you translate text with react-i18next?](#81-how-do-you-translate-text-with-react-i18next)
- [82: What is react-intl?](#82-what-is-react-intl)
- [83: What is Lingui?](#83-what-is-lingui)
- [84: What is date-fns?](#84-what-is-date-fns)
- [85: What is Day.js?](#85-what-is-dayjs)
- [86: Why do people avoid Moment.js today?](#86-why-do-people-avoid-momentjs-today)
- [87: What is Luxon?](#87-what-is-luxon)
- [88: Do you always need a date library in React?](#88-do-you-always-need-a-date-library-in-react)
- [89: What is lodash and do you still need it?](#89-what-is-lodash-and-do-you-still-need-it)
- [90: What is Immer?](#90-what-is-immer)
- [91: What is dnd-kit?](#91-what-is-dnd-kit)
- [92: What happened to react-beautiful-dnd?](#92-what-happened-to-react-beautiful-dnd)
- [93: What is react-dropzone?](#93-what-is-react-dropzone)
- [94: What is react-select?](#94-what-is-react-select)
- [95: What is Downshift?](#95-what-is-downshift)
- [96: What is react-day-picker?](#96-what-is-react-day-picker)
- [97: What is react-hot-toast?](#97-what-is-react-hot-toast)
- [98: What is Sonner?](#98-what-is-sonner)
- [99: What is react-error-boundary?](#99-what-is-react-error-boundary)
- [100: What is react-helmet-async and do you still need it with React 19?](#100-what-is-react-helmet-async-and-do-you-still-need-it-with-react-19)
- [101: What is Floating UI?](#101-what-is-floating-ui)
- [102: What is react-icons?](#102-what-is-react-icons)
- [103: What is Lucide React?](#103-what-is-lucide-react)
- [104: What is react-markdown?](#104-what-is-react-markdown)
- [105: What is Lexical?](#105-what-is-lexical)
- [106: What is Tiptap?](#106-what-is-tiptap)
- [107: What is Slate?](#107-what-is-slate)
- [108: What is React Three Fiber?](#108-what-is-react-three-fiber)
- [109: What is the difference between react-pdf and @react-pdf/renderer?](#109-what-is-the-difference-between-react-pdf-and-react-pdfrenderer)
- [110: What is React Testing Library?](#110-what-is-react-testing-library)
- [111: What is Vitest?](#111-what-is-vitest)
- [112: What is Jest?](#112-what-is-jest)
- [113: What is user-event?](#113-what-is-user-event)
- [114: What is MSW?](#114-what-is-msw)
- [115: What is Playwright?](#115-what-is-playwright)
- [116: What is Cypress?](#116-what-is-cypress)
- [117: What is Storybook?](#117-what-is-storybook)
- [118: What is eslint-plugin-react-hooks?](#118-what-is-eslint-plugin-react-hooks)
- [119: What is the React Compiler?](#119-what-is-the-react-compiler)
- [120: What is Vite and why is it used for React apps?](#120-what-is-vite-and-why-is-it-used-for-react-apps)
- [121: What happened to Create React App?](#121-what-happened-to-create-react-app)
- [122: What is Next.js?](#122-what-is-nextjs)
- [123: What happened to Remix?](#123-what-happened-to-remix)
- [124: How do you use React components in Astro?](#124-how-do-you-use-react-components-in-astro)
- [125: What is Auth.js (NextAuth)?](#125-what-is-authjs-nextauth)
- [126: What is Clerk?](#126-what-is-clerk)
- [127: What is the Auth0 React SDK?](#127-what-is-the-auth0-react-sdk)
- [128: What is Better Auth?](#128-what-is-better-auth)
- [129: How is Firebase used in React apps?](#129-how-is-firebase-used-in-react-apps)
- [130: What is the Supabase client in React?](#130-what-is-the-supabase-client-in-react)
- [131: What is the Socket.IO client?](#131-what-is-the-socketio-client)
- [132: What is Sentry used for in React apps?](#132-what-is-sentry-used-for-in-react-apps)
- [133: What is React Scan?](#133-what-is-react-scan)
- [134: What is why-did-you-render?](#134-what-is-why-did-you-render)
- [135: What is nuqs?](#135-what-is-nuqs)
- [136: What are usehooks-ts and react-use?](#136-what-are-usehooks-ts-and-react-use)
- [137: Do you need a library like uuid or nanoid to create IDs?](#137-do-you-need-a-library-like-uuid-or-nanoid-to-create-ids)
- [138: What is DOMPurify?](#138-what-is-dompurify)
- [139: What is @hookform/resolvers?](#139-what-is-hookformresolvers)
- [140: What is RTK Query?](#140-what-is-rtk-query)
- [141: What is Redux DevTools?](#141-what-is-redux-devtools)
- [142: How do you read and update query parameters in React Router?](#142-how-do-you-read-and-update-query-parameters-in-react-router)
- [143: What is react-intersection-observer?](#143-what-is-react-intersection-observer)
- [144: What is react-resizable-panels?](#144-what-is-react-resizable-panels)
- [145: Which libraries are popular for carousels in React?](#145-which-libraries-are-popular-for-carousels-in-react)
- [146: What is cmdk?](#146-what-is-cmdk)
- [147: What is React Email?](#147-what-is-react-email)
- [148: What is react-player?](#148-what-is-react-player)
- [149: What is the difference between a UI kit and a headless library?](#149-what-is-the-difference-between-a-ui-kit-and-a-headless-library)
- [150: What types of libraries does a typical React app end up using?](#150-what-types-of-libraries-does-a-typical-react-app-end-up-using)

### Moderate Questions (151-300)

- [151: How do you protect routes that need a logged-in user in React Router?](#151-how-do-you-protect-routes-that-need-a-logged-in-user-in-react-router)
- [152: How do you show a pending state while React Router loads the next page?](#152-how-do-you-show-a-pending-state-while-react-router-loads-the-next-page)
- [153: What is useFetcher in React Router and when do you use it?](#153-what-is-usefetcher-in-react-router-and-when-do-you-use-it)
- [154: How do you handle errors in React Router routes?](#154-how-do-you-handle-errors-in-react-router-routes)
- [155: How do you lazy load routes in React Router?](#155-how-do-you-lazy-load-routes-in-react-router)
- [156: How do you make search params type-safe in TanStack Router?](#156-how-do-you-make-search-params-type-safe-in-tanstack-router)
- [157: How does file-based routing work in TanStack Router?](#157-how-does-file-based-routing-work-in-tanstack-router)
- [158: How do you call an API with createAsyncThunk in Redux Toolkit?](#158-how-do-you-call-an-api-with-createasyncthunk-in-redux-toolkit)
- [159: How do you set up an API with RTK Query?](#159-how-do-you-set-up-an-api-with-rtk-query)
- [160: How does cache invalidation work in RTK Query?](#160-how-does-cache-invalidation-work-in-rtk-query)
- [161: How do you type the Redux hooks in a TypeScript project?](#161-how-do-you-type-the-redux-hooks-in-a-typescript-project)
- [162: What is createSelector and when do you need it?](#162-what-is-createselector-and-when-do-you-need-it)
- [163: What is createEntityAdapter in Redux Toolkit?](#163-what-is-createentityadapter-in-redux-toolkit)
- [164: How do you avoid extra re-renders when selecting several values from a Zustand store?](#164-how-do-you-avoid-extra-re-renders-when-selecting-several-values-from-a-zustand-store)
- [165: How do you persist a Zustand store to localStorage?](#165-how-do-you-persist-a-zustand-store-to-localstorage)
- [166: How do you use Redux DevTools and Immer with Zustand?](#166-how-do-you-use-redux-devtools-and-immer-with-zustand)
- [167: What is the slices pattern in Zustand?](#167-what-is-the-slices-pattern-in-zustand)
- [168: How do you use a Zustand store outside of React components?](#168-how-do-you-use-a-zustand-store-outside-of-react-components)
- [169: How do you write a derived atom that can also be written to in Jotai?](#169-how-do-you-write-a-derived-atom-that-can-also-be-written-to-in-jotai)
- [170: How do async atoms work with Suspense in Jotai?](#170-how-do-async-atoms-work-with-suspense-in-jotai)
- [171: How do you persist an atom in Jotai?](#171-how-do-you-persist-an-atom-in-jotai)
- [172: How do you use MobX with React components?](#172-how-do-you-use-mobx-with-react-components)
- [173: How do you use an XState machine in a React component?](#173-how-do-you-use-an-xstate-machine-in-a-react-component)
- [174: How do you decide between React Context, Zustand, Jotai and Redux Toolkit?](#174-how-do-you-decide-between-react-context-zustand-jotai-and-redux-toolkit)
- [175: What is the difference between staleTime and gcTime in TanStack Query?](#175-what-is-the-difference-between-staletime-and-gctime-in-tanstack-query)
- [176: How do you refresh data after a mutation in TanStack Query?](#176-how-do-you-refresh-data-after-a-mutation-in-tanstack-query)
- [177: How do you do an optimistic update with TanStack Query?](#177-how-do-you-do-an-optimistic-update-with-tanstack-query)
- [178: How do you run a query only when some data is available?](#178-how-do-you-run-a-query-only-when-some-data-is-available)
- [179: How do you keep showing old data while the next page loads in TanStack Query?](#179-how-do-you-keep-showing-old-data-while-the-next-page-loads-in-tanstack-query)
- [180: How do you build infinite scrolling with TanStack Query?](#180-how-do-you-build-infinite-scrolling-with-tanstack-query)
- [181: What is useSuspenseQuery and how is it different from useQuery?](#181-what-is-usesuspensequery-and-how-is-it-different-from-usequery)
- [182: How do you prefetch data with TanStack Query?](#182-how-do-you-prefetch-data-with-tanstack-query)
- [183: What is the queryOptions helper in TanStack Query?](#183-what-is-the-queryoptions-helper-in-tanstack-query)
- [184: How do you use the TanStack Query Devtools?](#184-how-do-you-use-the-tanstack-query-devtools)
- [185: How does TanStack Query handle errors and retries?](#185-how-does-tanstack-query-handle-errors-and-retries)
- [186: How do you update and revalidate data with SWR?](#186-how-do-you-update-and-revalidate-data-with-swr)
- [187: How do you add an auth token to every Axios request?](#187-how-do-you-add-an-auth-token-to-every-axios-request)
- [188: How do you cancel an Axios or fetch request in React?](#188-how-do-you-cancel-an-axios-or-fetch-request-in-react)
- [189: How does the Apollo Client cache work at a basic level?](#189-how-does-the-apollo-client-cache-work-at-a-basic-level)
- [190: How do you update the Apollo cache after a mutation that adds an item?](#190-how-do-you-update-the-apollo-cache-after-a-mutation-that-adds-an-item)
- [191: How does tRPC work with TanStack Query in React?](#191-how-does-trpc-work-with-tanstack-query-in-react)
- [192: How do you use Zod with React Hook Form?](#192-how-do-you-use-zod-with-react-hook-form)
- [193: How do you use a controlled UI component like MUI's TextField or Select with React Hook Form?](#193-how-do-you-use-a-controlled-ui-component-like-muis-textfield-or-select-with-react-hook-form)
- [194: How do you handle a dynamic list of fields in React Hook Form?](#194-how-do-you-handle-a-dynamic-list-of-fields-in-react-hook-form)
- [195: What is the difference between watch and useWatch in React Hook Form?](#195-what-is-the-difference-between-watch-and-usewatch-in-react-hook-form)
- [196: How do you show server-side errors in React Hook Form?](#196-how-do-you-show-server-side-errors-in-react-hook-form)
- [197: Why is React Hook Form fast compared to Formik?](#197-why-is-react-hook-form-fast-compared-to-formik)
- [198: What is the difference between parse and safeParse in Zod?](#198-what-is-the-difference-between-parse-and-safeparse-in-zod)
- [199: How do you validate API responses with Zod?](#199-how-do-you-validate-api-responses-with-zod)
- [200: How do you choose between React Hook Form, TanStack Form and Formik for a new project?](#200-how-do-you-choose-between-react-hook-form-tanstack-form-and-formik-for-a-new-project)
- [201: How do you customize the theme in Material UI?](#201-how-do-you-customize-the-theme-in-material-ui)
- [202: What is the difference between the sx prop and styled() in Material UI?](#202-what-is-the-difference-between-the-sx-prop-and-styled-in-material-ui)
- [203: How do you support dark mode in Material UI?](#203-how-do-you-support-dark-mode-in-material-ui)
- [204: How do you add and customize shadcn/ui components?](#204-how-do-you-add-and-customize-shadcnui-components)
- [205: How does theming work in shadcn/ui?](#205-how-does-theming-work-in-shadcnui)
- [206: How do you build a modal with Radix UI Dialog?](#206-how-do-you-build-a-modal-with-radix-ui-dialog)
- [207: What does the asChild prop do in Radix UI?](#207-what-does-the-aschild-prop-do-in-radix-ui)
- [208: How do you customize components in Chakra UI v3?](#208-how-do-you-customize-components-in-chakra-ui-v3)
- [209: How do you handle forms with Mantine?](#209-how-do-you-handle-forms-with-mantine)
- [210: How do you change the theme in Ant Design?](#210-how-do-you-change-the-theme-in-ant-design)
- [211: When would you use React Aria hooks instead of React Aria Components?](#211-when-would-you-use-react-aria-hooks-instead-of-react-aria-components)
- [212: How do you set up Tailwind CSS v4 in a Vite React project?](#212-how-do-you-set-up-tailwind-css-v4-in-a-vite-react-project)
- [213: How do you build a reusable component with variants using cva and Tailwind?](#213-how-do-you-build-a-reusable-component-with-variants-using-cva-and-tailwind)
- [214: How do you use theming and props in styled-components?](#214-how-do-you-use-theming-and-props-in-styled-components)
- [215: How do you type CSS Modules and share styles between them?](#215-how-do-you-type-css-modules-and-share-styles-between-them)
- [216: What are the trade-offs between runtime and zero-runtime CSS-in-JS?](#216-what-are-the-trade-offs-between-runtime-and-zero-runtime-css-in-js)
- [217: How do you animate a component when it is removed with Motion?](#217-how-do-you-animate-a-component-when-it-is-removed-with-motion)
- [218: What are layout animations in Motion?](#218-what-are-layout-animations-in-motion)
- [219: How do you use variants in Motion?](#219-how-do-you-use-variants-in-motion)
- [220: How do you respect the user's reduced motion setting with Motion?](#220-how-do-you-respect-the-users-reduced-motion-setting-with-motion)
- [221: How do you make a custom tooltip in Recharts?](#221-how-do-you-make-a-custom-tooltip-in-recharts)
- [222: How do you pick a chart library for a React project?](#222-how-do-you-pick-a-chart-library-for-a-react-project)
- [223: How do you set up sorting and filtering with TanStack Table?](#223-how-do-you-set-up-sorting-and-filtering-with-tanstack-table)
- [224: How do you do server-side pagination with TanStack Table?](#224-how-do-you-do-server-side-pagination-with-tanstack-table)
- [225: How do you render a long list with TanStack Virtual?](#225-how-do-you-render-a-long-list-with-tanstack-virtual)
- [226: How do you set up AG Grid in a React app?](#226-how-do-you-set-up-ag-grid-in-a-react-app)
- [227: How do you lazy load translation files with react-i18next?](#227-how-do-you-lazy-load-translation-files-with-react-i18next)
- [228: How do plurals and interpolation work in i18next?](#228-how-do-plurals-and-interpolation-work-in-i18next)
- [229: What is the Trans component in react-i18next used for?](#229-what-is-the-trans-component-in-react-i18next-used-for)
- [230: How do you format numbers, dates and currency with react-intl?](#230-how-do-you-format-numbers-dates-and-currency-with-react-intl)
- [231: How do you work with time zones in date-fns?](#231-how-do-you-work-with-time-zones-in-date-fns)
- [232: How do Day.js plugins work?](#232-how-do-dayjs-plugins-work)
- [233: How do you build a sortable list with dnd-kit?](#233-how-do-you-build-a-sortable-list-with-dnd-kit)
- [234: How do you validate files with react-dropzone?](#234-how-do-you-validate-files-with-react-dropzone)
- [235: How do you load options from an API in react-select?](#235-how-do-you-load-options-from-an-api-in-react-select)
- [236: How do you show toasts for an async action with Sonner?](#236-how-do-you-show-toasts-for-an-async-action-with-sonner)
- [237: How do you reset an error boundary and catch async errors with react-error-boundary?](#237-how-do-you-reset-an-error-boundary-and-catch-async-errors-with-react-error-boundary)
- [238: How do you use error boundaries together with TanStack Query?](#238-how-do-you-use-error-boundaries-together-with-tanstack-query)
- [239: How do you set page titles and meta tags in a React 19 app without a library?](#239-how-do-you-set-page-titles-and-meta-tags-in-a-react-19-app-without-a-library)
- [240: How do you position a tooltip with Floating UI?](#240-how-do-you-position-a-tooltip-with-floating-ui)
- [241: How do you make sure icon libraries don't bloat your bundle?](#241-how-do-you-make-sure-icon-libraries-dont-bloat-your-bundle)
- [242: How do you render Markdown with code highlighting safely in React?](#242-how-do-you-render-markdown-with-code-highlighting-safely-in-react)
- [243: How do you create a basic rich text editor with Tiptap and save its content?](#243-how-do-you-create-a-basic-rich-text-editor-with-tiptap-and-save-its-content)
- [244: How do you set up a basic Lexical editor in React?](#244-how-do-you-set-up-a-basic-lexical-editor-in-react)
- [245: How do you animate something every frame in React Three Fiber?](#245-how-do-you-animate-something-every-frame-in-react-three-fiber)
- [246: Which queries should you prefer in React Testing Library?](#246-which-queries-should-you-prefer-in-react-testing-library)
- [247: What is the difference between getBy, queryBy and findBy in Testing Library?](#247-what-is-the-difference-between-getby-queryby-and-findby-in-testing-library)
- [248: Why should you call userEvent.setup() and await every interaction?](#248-why-should-you-call-usereventsetup-and-await-every-interaction)
- [249: How do you test a component that uses TanStack Query?](#249-how-do-you-test-a-component-that-uses-tanstack-query)
- [250: How do you test components that use a Redux store?](#250-how-do-you-test-components-that-use-a-redux-store)
- [251: How do you reset Zustand stores between tests?](#251-how-do-you-reset-zustand-stores-between-tests)
- [252: How do you write request handlers in MSW?](#252-how-do-you-write-request-handlers-in-msw)
- [253: How do you use MSW in the browser during development?](#253-how-do-you-use-msw-in-the-browser-during-development)
- [254: How do you set up Vitest for testing React components?](#254-how-do-you-set-up-vitest-for-testing-react-components)
- [255: What makes Playwright locators reliable?](#255-what-makes-playwright-locators-reliable)
- [256: When would you use Playwright component testing instead of Vitest with jsdom?](#256-when-would-you-use-playwright-component-testing-instead-of-vitest-with-jsdom)
- [257: How do you write a component test in Cypress?](#257-how-do-you-write-a-component-test-in-cypress)
- [258: How do you write stories with args in Storybook?](#258-how-do-you-write-stories-with-args-in-storybook)
- [259: What are play functions in Storybook?](#259-what-are-play-functions-in-storybook)
- [260: How do you mock API calls in Storybook?](#260-how-do-you-mock-api-calls-in-storybook)
- [261: How do you provide context like a theme, router or QueryClient to Storybook stories?](#261-how-do-you-provide-context-like-a-theme-router-or-queryclient-to-storybook-stories)
- [262: How do you set up ESLint for a React project with flat config?](#262-how-do-you-set-up-eslint-for-a-react-project-with-flat-config)
- [263: How do you enable the React Compiler in a Vite project?](#263-how-do-you-enable-the-react-compiler-in-a-vite-project)
- [264: Can the React Compiler break code that uses some libraries?](#264-can-the-react-compiler-break-code-that-uses-some-libraries)
- [265: How do you use TanStack Query with the Next.js App Router?](#265-how-do-you-use-tanstack-query-with-the-nextjs-app-router)
- [266: How do you use Zustand safely with Next.js and SSR?](#266-how-do-you-use-zustand-safely-with-nextjs-and-ssr)
- [267: How do you get the session in Next.js with Auth.js?](#267-how-do-you-get-the-session-in-nextjs-with-authjs)
- [268: How do you protect pages with Clerk in a React or Next.js app?](#268-how-do-you-protect-pages-with-clerk-in-a-react-or-nextjs-app)
- [269: How do you call a protected API with the Auth0 React SDK?](#269-how-do-you-call-a-protected-api-with-the-auth0-react-sdk)
- [270: How do you listen to auth state changes with Supabase in React?](#270-how-do-you-listen-to-auth-state-changes-with-supabase-in-react)
- [271: How do you write a hook for the current Firebase user?](#271-how-do-you-write-a-hook-for-the-current-firebase-user)
- [272: How do you use Socket.IO correctly inside a React component?](#272-how-do-you-use-socketio-correctly-inside-a-react-component)
- [273: How do you set up Sentry in a React app?](#273-how-do-you-set-up-sentry-in-a-react-app)
- [274: How do you sync filters with the URL using nuqs?](#274-how-do-you-sync-filters-with-the-url-using-nuqs)
- [275: How do you debounce a search input in React?](#275-how-do-you-debounce-a-search-input-in-react)
- [276: How do you build infinite scroll with react-intersection-observer and TanStack Query?](#276-how-do-you-build-infinite-scroll-with-react-intersection-observer-and-tanstack-query)
- [277: How do you safely render HTML from a CMS in React?](#277-how-do-you-safely-render-html-from-a-cms-in-react)
- [278: How do you control an Embla carousel from your own buttons?](#278-how-do-you-control-an-embla-carousel-from-your-own-buttons)
- [279: How do you build a command palette with cmdk and a dialog?](#279-how-do-you-build-a-command-palette-with-cmdk-and-a-dialog)
- [280: How do you combine React 19's useActionState with Zod validation?](#280-how-do-you-combine-react-19s-useactionstate-with-zod-validation)
- [281: How do you render an email template with React Email?](#281-how-do-you-render-an-email-template-with-react-email)
- [282: How do you find out which libraries make your bundle large?](#282-how-do-you-find-out-which-libraries-make-your-bundle-large)
- [283: How do you make sure a library can be tree-shaken?](#283-how-do-you-make-sure-a-library-can-be-tree-shaken)
- [284: How would you replace Moment.js in an existing React app?](#284-how-would-you-replace-momentjs-in-an-existing-react-app)
- [285: How do you set up MUI X Date Pickers?](#285-how-do-you-set-up-mui-x-date-pickers)
- [286: How do you use Immer for complex state in a component?](#286-how-do-you-use-immer-for-complex-state-in-a-component)
- [287: What is the listener middleware in Redux Toolkit?](#287-what-is-the-listener-middleware-in-redux-toolkit)
- [288: Should you still use redux-persist?](#288-should-you-still-use-redux-persist)
- [289: How do you update TanStack Query's cache from WebSocket messages?](#289-how-do-you-update-tanstack-querys-cache-from-websocket-messages)
- [290: What are the main differences between SWR and TanStack Query?](#290-what-are-the-main-differences-between-swr-and-tanstack-query)
- [291: How does React Router compare with TanStack Router?](#291-how-does-react-router-compare-with-tanstack-router)
- [292: How do you add retries and auth headers in ky?](#292-how-do-you-add-retries-and-auth-headers-in-ky)
- [293: What is the difference between Radix's asChild and Base UI's render prop?](#293-what-is-the-difference-between-radixs-aschild-and-base-uis-render-prop)
- [294: How do you use the Mantine hooks package without the rest of Mantine?](#294-how-do-you-use-the-mantine-hooks-package-without-the-rest-of-mantine)
- [295: How do you make a Radix or shadcn component work with React Hook Form?](#295-how-do-you-make-a-radix-or-shadcn-component-work-with-react-hook-form)
- [296: How do you load fonts and global styles with Material UI or other kits in Vite?](#296-how-do-you-load-fonts-and-global-styles-with-material-ui-or-other-kits-in-vite)
- [297: How do you handle dark mode with Tailwind in React?](#297-how-do-you-handle-dark-mode-with-tailwind-in-react)
- [298: How do you add the shadcn/ui Form with React Hook Form and Zod?](#298-how-do-you-add-the-shadcnui-form-with-react-hook-form-and-zod)
- [299: How do you migrate a React app from Create React App to Vite?](#299-how-do-you-migrate-a-react-app-from-create-react-app-to-vite)
- [300: How do you handle auth tokens that expire while using TanStack Query?](#300-how-do-you-handle-auth-tokens-that-expire-while-using-tanstack-query)

### Advanced Questions (301-450)

- [301: How does TanStack Query's cache work internally?](#301-how-does-tanstack-querys-cache-work-internally)
- [302: What is structural sharing in TanStack Query and why does it matter?](#302-what-is-structural-sharing-in-tanstack-query-and-why-does-it-matter)
- [303: How do select and tracked properties reduce re-renders in TanStack Query?](#303-how-do-select-and-tracked-properties-reduce-re-renders-in-tanstack-query)
- [304: How do you design query keys in a large app?](#304-how-do-you-design-query-keys-in-a-large-app)
- [305: How does SSR with TanStack Query work, including streaming?](#305-how-does-ssr-with-tanstack-query-work-including-streaming)
- [306: How do you avoid request waterfalls when using TanStack Query with a router?](#306-how-do-you-avoid-request-waterfalls-when-using-tanstack-query-with-a-router)
- [307: How do you avoid race conditions when fetching data in React?](#307-how-do-you-avoid-race-conditions-when-fetching-data-in-react)
- [308: What problems can happen with optimistic updates when mutations run at the same time?](#308-what-problems-can-happen-with-optimistic-updates-when-mutations-run-at-the-same-time)
- [309: How do you make a TanStack Query app work offline?](#309-how-do-you-make-a-tanstack-query-app-work-offline)
- [310: How do external store libraries like Zustand and Redux connect to React?](#310-how-do-external-store-libraries-like-zustand-and-redux-connect-to-react)
- [311: What is tearing and how do state libraries avoid it?](#311-what-is-tearing-and-how-do-state-libraries-avoid-it)
- [312: How is Zustand built internally?](#312-how-is-zustand-built-internally)
- [313: Why would you put a Zustand store in React context instead of a module-level singleton?](#313-why-would-you-put-a-zustand-store-in-react-context-instead-of-a-module-level-singleton)
- [314: How does Jotai work internally?](#314-how-does-jotai-work-internally)
- [315: What are common performance problems with Redux selectors?](#315-what-are-common-performance-problems-with-redux-selectors)
- [316: How do RTK Query and TanStack Query differ in architecture?](#316-how-do-rtk-query-and-tanstack-query-differ-in-architecture)
- [317: How do you stream updates into an RTK Query cache entry?](#317-how-do-you-stream-updates-into-an-rtk-query-cache-entry)
- [318: How do you split an RTK Query API across many feature folders?](#318-how-do-you-split-an-rtk-query-api-across-many-feature-folders)
- [319: What is the difference between a normalized cache and a document cache?](#319-what-is-the-difference-between-a-normalized-cache-and-a-document-cache)
- [320: How do you handle pagination in Apollo's normalized cache?](#320-how-do-you-handle-pagination-in-apollos-normalized-cache)
- [321: What are Apollo Client's fetch policies and when do you use each?](#321-what-are-apollo-clients-fetch-policies-and-when-do-you-use-each)
- [322: How does tRPC give type safety across the network, and what are its limits?](#322-how-does-trpc-give-type-safety-across-the-network-and-what-are-its-limits)
- [323: How does React Hook Form track form state without re-rendering everything?](#323-how-does-react-hook-form-track-form-state-without-re-rendering-everything)
- [324: How do you keep a very large form fast with React Hook Form?](#324-how-do-you-keep-a-very-large-form-fast-with-react-hook-form)
- [325: What changed in Zod 4 compared to Zod 3?](#325-what-changed-in-zod-4-compared-to-zod-3)
- [326: What is Standard Schema and why do libraries care about it?](#326-what-is-standard-schema-and-why-do-libraries-care-about-it)
- [327: How do you share validation between the client and the server?](#327-how-do-you-share-validation-between-the-client-and-the-server)
- [328: What are the trade-offs of building a design system on a headless library versus a full UI kit?](#328-what-are-the-trade-offs-of-building-a-design-system-on-a-headless-library-versus-a-full-ui-kit)
- [329: How do you type a polymorphic component in TypeScript?](#329-how-do-you-type-a-polymorphic-component-in-typescript)
- [330: How do you type a generic component like a Select or Table that works with any item type?](#330-how-do-you-type-a-generic-component-like-a-select-or-table-that-works-with-any-item-type)
- [331: How do headless libraries make dialogs and menus accessible?](#331-how-do-headless-libraries-make-dialogs-and-menus-accessible)
- [332: What problems happen with portals, z-index and stacking when mixing UI libraries?](#332-what-problems-happen-with-portals-z-index-and-stacking-when-mixing-ui-libraries)
- [333: Why don't runtime CSS-in-JS libraries work well with React Server Components?](#333-why-dont-runtime-css-in-js-libraries-work-well-with-react-server-components)
- [334: What does useInsertionEffect do and why do CSS-in-JS libraries need it?](#334-what-does-useinsertioneffect-do-and-why-do-css-in-js-libraries-need-it)
- [335: How would you migrate a large app from styled-components to another styling solution?](#335-how-would-you-migrate-a-large-app-from-styled-components-to-another-styling-solution)
- [336: What are the costs of tailwind-merge and how do you use it well?](#336-what-are-the-costs-of-tailwind-merge-and-how-do-you-use-it-well)
- [337: How do you keep Material UI apps fast?](#337-how-do-you-keep-material-ui-apps-fast)
- [338: How do you share design tokens across several UI libraries in one app?](#338-how-do-you-share-design-tokens-across-several-ui-libraries-in-one-app)
- [339: How do you keep Motion animations smooth?](#339-how-do-you-keep-motion-animations-smooth)
- [340: How do you reduce Motion's bundle size?](#340-how-do-you-reduce-motions-bundle-size)
- [341: What problems come up when combining animations with virtualized lists?](#341-what-problems-come-up-when-combining-animations-with-virtualized-lists)
- [342: How do virtualization libraries handle items with dynamic heights?](#342-how-do-virtualization-libraries-handle-items-with-dynamic-heights)
- [343: What accessibility and UX trade-offs does virtualization have?](#343-what-accessibility-and-ux-trade-offs-does-virtualization-have)
- [344: How is TanStack Table designed internally?](#344-how-is-tanstack-table-designed-internally)
- [345: How would you build a table that shows 100,000 editable rows?](#345-how-would-you-build-a-table-that-shows-100000-editable-rows)
- [346: How do you choose a rendering approach for charts with lots of data?](#346-how-do-you-choose-a-rendering-approach-for-charts-with-lots-of-data)
- [347: How do you keep i18n from slowing down a React app?](#347-how-do-you-keep-i18n-from-slowing-down-a-react-app)
- [348: How do you handle i18n with Server Components and SSR?](#348-how-do-you-handle-i18n-with-server-components-and-ssr)
- [349: What is the ICU message format and why do libraries use it?](#349-what-is-the-icu-message-format-and-why-do-libraries-use-it)
- [350: What are common date and time zone bugs in React apps, and how do libraries help?](#350-what-are-common-date-and-time-zone-bugs-in-react-apps-and-how-do-libraries-help)
- [351: How do you decide which libraries to load lazily?](#351-how-do-you-decide-which-libraries-to-load-lazily)
- [352: What does a library need so bundlers can tree-shake it?](#352-what-does-a-library-need-so-bundlers-can-tree-shake-it)
- [353: What is the dual package hazard?](#353-what-is-the-dual-package-hazard)
- [354: Why do you get "Invalid hook call" errors from libraries, and how do you fix them?](#354-why-do-you-get-invalid-hook-call-errors-from-libraries-and-how-do-you-fix-them)
- [355: What breaks in libraries when upgrading to React 19?](#355-what-breaks-in-libraries-when-upgrading-to-react-19)
- [356: Which libraries can you use inside React Server Components?](#356-which-libraries-can-you-use-inside-react-server-components)
- [357: How do you wrap a client-only library for use in a Next.js App Router page?](#357-how-do-you-wrap-a-client-only-library-for-use-in-a-nextjs-app-router-page)
- [358: Why do libraries cause hydration mismatches, and how do you fix them?](#358-why-do-libraries-cause-hydration-mismatches-and-how-do-you-fix-them)
- [359: How do useId and useSyncExternalStore's getServerSnapshot help libraries support SSR?](#359-how-do-useid-and-usesyncexternalstores-getserversnapshot-help-libraries-support-ssr)
- [360: What security problems can third-party React libraries introduce?](#360-what-security-problems-can-third-party-react-libraries-introduce)
- [361: How do you protect a React project from npm supply chain attacks?](#361-how-do-you-protect-a-react-project-from-npm-supply-chain-attacks)
- [362: Where should a React app store auth tokens when using auth libraries?](#362-where-should-a-react-app-store-auth-tokens-when-using-auth-libraries)
- [363: How do you choose libraries with license costs in mind?](#363-how-do-you-choose-libraries-with-license-costs-in-mind)
- [364: How do you notice that a library is being abandoned, and what do you do?](#364-how-do-you-notice-that-a-library-is-being-abandoned-and-what-do-you-do)
- [365: Why would you wrap a third-party library behind your own module?](#365-why-would-you-wrap-a-third-party-library-behind-your-own-module)
- [366: How do you handle shared libraries across micro frontends?](#366-how-do-you-handle-shared-libraries-across-micro-frontends)
- [367: How do you split state across different kinds of libraries in a large app?](#367-how-do-you-split-state-across-different-kinds-of-libraries-in-a-large-app)
- [368: How do the mental models of Redux, Zustand, Jotai, MobX and XState differ?](#368-how-do-the-mental-models-of-redux-zustand-jotai-mobx-and-xstate-differ)
- [369: How do you use XState actors for complex flows like a checkout?](#369-how-do-you-use-xstate-actors-for-complex-flows-like-a-checkout)
- [370: How does MobX track dependencies internally?](#370-how-does-mobx-track-dependencies-internally)
- [371: How does Valtio work under the hood?](#371-how-does-valtio-work-under-the-hood)
- [372: What are signals, and why are libraries like Preact Signals or Legend State used with React?](#372-what-are-signals-and-why-are-libraries-like-preact-signals-or-legend-state-used-with-react)
- [373: Why can React Context be slow for frequently changing state, and what do libraries do about it?](#373-why-can-react-context-be-slow-for-frequently-changing-state-and-what-do-libraries-do-about-it)
- [374: What testing strategy works well for a React app with many libraries?](#374-what-testing-strategy-works-well-for-a-react-app-with-many-libraries)
- [375: How does MSW intercept requests in Node and in the browser?](#375-how-does-msw-intercept-requests-in-node-and-in-the-browser)
- [376: Why are tests with async libraries flaky, and how do you fix them?](#376-why-are-tests-with-async-libraries-flaky-and-how-do-you-fix-them)
- [377: How do you test virtualized lists and Radix components in jsdom?](#377-how-do-you-test-virtualized-lists-and-radix-components-in-jsdom)
- [378: How do you set up visual regression testing for a component library?](#378-how-do-you-set-up-visual-regression-testing-for-a-component-library)
- [379: How do you handle authentication in Playwright tests efficiently?](#379-how-do-you-handle-authentication-in-playwright-tests-efficiently)
- [380: How do you keep the frontend in sync with the backend API types?](#380-how-do-you-keep-the-frontend-in-sync-with-the-backend-api-types)
- [381: How does GraphQL Codegen give you typed queries in React?](#381-how-does-graphql-codegen-give-you-typed-queries-in-react)
- [382: What should you think about when setting up error monitoring with Sentry or similar tools?](#382-what-should-you-think-about-when-setting-up-error-monitoring-with-sentry-or-similar-tools)
- [383: How do you measure real user performance in a React app?](#383-how-do-you-measure-real-user-performance-in-a-react-app)
- [384: What problems do feature flag libraries cause in React apps?](#384-what-problems-do-feature-flag-libraries-cause-in-react-apps)
- [385: How do third-party scripts like analytics and chat widgets affect React apps, and how do you limit the damage?](#385-how-do-third-party-scripts-like-analytics-and-chat-widgets-affect-react-apps-and-how-do-you-limit-the-damage)
- [386: How do you build forms from a JSON schema in React?](#386-how-do-you-build-forms-from-a-json-schema-in-react)
- [387: How do rich text editors store content, and why does it matter for your app?](#387-how-do-rich-text-editors-store-content-and-why-does-it-matter-for-your-app)
- [388: How do you add real-time collaboration to a React app?](#388-how-do-you-add-real-time-collaboration-to-a-react-app)
- [389: How do you make drag and drop accessible?](#389-how-do-you-make-drag-and-drop-accessible)
- [390: How do you share code and libraries between React web and React Native?](#390-how-do-you-share-code-and-libraries-between-react-web-and-react-native)
- [391: How do you plan a major version upgrade of a big library?](#391-how-do-you-plan-a-major-version-upgrade-of-a-big-library)
- [392: What were the main breaking changes in TanStack Query v5?](#392-what-were-the-main-breaking-changes-in-tanstack-query-v5)
- [393: How do you upgrade from React Router v6 to v7 and v8?](#393-how-do-you-upgrade-from-react-router-v6-to-v7-and-v8)
- [394: What changed in Redux Toolkit 2.0?](#394-what-changed-in-redux-toolkit-20)
- [395: What changed in Zustand v5?](#395-what-changed-in-zustand-v5)
- [396: What changed in Tailwind CSS v4, and what does it mean for React projects?](#396-what-changed-in-tailwind-css-v4-and-what-does-it-mean-for-react-projects)
- [397: What changed in Chakra UI v3, and why was the upgrade hard for many teams?](#397-what-changed-in-chakra-ui-v3-and-why-was-the-upgrade-hard-for-many-teams)
- [398: How do you build and publish your own React component library?](#398-how-do-you-build-and-publish-your-own-react-component-library)
- [399: How do you support both controlled and uncontrolled usage in a reusable component?](#399-how-do-you-support-both-controlled-and-uncontrolled-usage-in-a-reusable-component)
- [400: How does React 19's ref-as-prop change how libraries are written?](#400-how-does-react-19s-ref-as-prop-change-how-libraries-are-written)
- [401: How do you type TanStack Router so links and navigation are checked everywhere?](#401-how-do-you-type-tanstack-router-so-links-and-navigation-are-checked-everywhere)
- [402: How do routers preload code and data, and what are the trade-offs?](#402-how-do-routers-preload-code-and-data-and-what-are-the-trade-offs)
- [403: What is render-as-you-fetch and how do data libraries support it?](#403-what-is-render-as-you-fetch-and-how-do-data-libraries-support-it)
- [404: How do router navigations work with React transitions?](#404-how-do-router-navigations-work-with-react-transitions)
- [405: How does streaming SSR work in React Router framework mode?](#405-how-does-streaming-ssr-work-in-react-router-framework-mode)
- [406: Should data loading happen in route loaders or in components?](#406-should-data-loading-happen-in-route-loaders-or-in-components)
- [407: How do the different caching layers in a React app interact?](#407-how-do-the-different-caching-layers-in-a-react-app-interact)
- [408: What kinds of memory leaks do libraries cause in React apps?](#408-what-kinds-of-memory-leaks-do-libraries-cause-in-react-apps)
- [409: Scenario: the app got noticeably slower after the team added a global state library. How do you investigate?](#409-scenario-the-app-got-noticeably-slower-after-the-team-added-a-global-state-library-how-do-you-investigate)
- [410: Scenario: you are starting a new internal admin dashboard in React. Which libraries would you pick and why?](#410-scenario-you-are-starting-a-new-internal-admin-dashboard-in-react-which-libraries-would-you-pick-and-why)
- [411: Scenario: your app keeps all API data in Redux with hand-written thunks. How would you migrate to TanStack Query or RTK Query?](#411-scenario-your-app-keeps-all-api-data-in-redux-with-hand-written-thunks-how-would-you-migrate-to-tanstack-query-or-rtk-query)
- [412: Scenario: the main JavaScript bundle is 2 MB. How do you reduce it?](#412-scenario-the-main-javascript-bundle-is-2-mb-how-do-you-reduce-it)
- [413: Scenario: a form with 200 fields lags when typing. How do you fix it?](#413-scenario-a-form-with-200-fields-lags-when-typing-how-do-you-fix-it)
- [414: Scenario: users need to edit a table with 50,000 rows in the browser. What is your approach?](#414-scenario-users-need-to-edit-a-table-with-50000-rows-in-the-browser-what-is-your-approach)
- [415: Scenario: after a user edits an item, some parts of the UI still show the old value. How do you debug it?](#415-scenario-after-a-user-edits-an-item-some-parts-of-the-ui-still-show-the-old-value-how-do-you-debug-it)
- [416: Scenario: you added a date library and now the app has hydration errors. What is going on?](#416-scenario-you-added-a-date-library-and-now-the-app-has-hydration-errors-what-is-going-on)
- [417: Scenario: a security review found XSS in the comments section, which supports Markdown. How do you fix it?](#417-scenario-a-security-review-found-xss-in-the-comments-section-which-supports-markdown-how-do-you-fix-it)
- [418: Scenario: a UI library your app depends on heavily is no longer maintained. What is your plan?](#418-scenario-a-ui-library-your-app-depends-on-heavily-is-no-longer-maintained-what-is-your-plan)
- [419: Scenario: two UI kits are used in the same app and it looks inconsistent. What do you do?](#419-scenario-two-ui-kits-are-used-in-the-same-app-and-it-looks-inconsistent-what-do-you-do)
- [420: Scenario: you need to make an app work for right-to-left languages like Arabic. What is involved with libraries?](#420-scenario-you-need-to-make-an-app-work-for-right-to-left-languages-like-arabic-what-is-involved-with-libraries)
- [421: Scenario: tests using MSW and TanStack Query pass alone but fail when run together. What is wrong?](#421-scenario-tests-using-msw-and-tanstack-query-pass-alone-but-fail-when-run-together-what-is-wrong)
- [422: Scenario: many requests fail at once with 401 because the token expired, and your app sends ten refresh requests. How do you fix it?](#422-scenario-many-requests-fail-at-once-with-401-because-the-token-expired-and-your-app-sends-ten-refresh-requests-how-do-you-fix-it)
- [423: Scenario: you need an offline-first web app for field workers. Which libraries and patterns would you consider?](#423-scenario-you-need-an-offline-first-web-app-for-field-workers-which-libraries-and-patterns-would-you-consider)
- [424: Scenario: you are building a real-time dashboard with live charts. How do you keep it fast?](#424-scenario-you-are-building-a-real-time-dashboard-with-live-charts-how-do-you-keep-it-fast)
- [425: Scenario: you want to upgrade to React 19, but one library blocks you. What are your options?](#425-scenario-you-want-to-upgrade-to-react-19-but-one-library-blocks-you-what-are-your-options)
- [426: Scenario: you enabled the React Compiler and a few components stopped updating. How do you handle it?](#426-scenario-you-enabled-the-react-compiler-and-a-few-components-stopped-updating-how-do-you-handle-it)
- [427: Scenario: a context-based library doesn't work in the Next.js App Router. How do you integrate it?](#427-scenario-a-context-based-library-doesnt-work-in-the-nextjs-app-router-how-do-you-integrate-it)
- [428: Scenario: an accessibility audit fails on your custom dropdowns. How do you fix them?](#428-scenario-an-accessibility-audit-fails-on-your-custom-dropdowns-how-do-you-fix-them)
- [429: Scenario: several apps in your company need a shared design system. How do you build it?](#429-scenario-several-apps-in-your-company-need-a-shared-design-system-how-do-you-build-it)
- [430: Scenario: in development every request is sent twice when a page loads. Is this a bug?](#430-scenario-in-development-every-request-is-sent-twice-when-a-page-loads-is-this-a-bug)
- [431: Scenario: after logout, the next user sees data from the previous user. How do you fix it?](#431-scenario-after-logout-the-next-user-sees-data-from-the-previous-user-how-do-you-fix-it)
- [432: Scenario: a search page shows results for an old query when the user types fast. How do you fix it?](#432-scenario-a-search-page-shows-results-for-an-old-query-when-the-user-types-fast-how-do-you-fix-it)
- [433: Scenario: you need an infinite feed with virtualization that keeps the scroll position when the user goes back. How do you build it?](#433-scenario-you-need-an-infinite-feed-with-virtualization-that-keeps-the-scroll-position-when-the-user-goes-back-how-do-you-build-it)
- [434: Scenario: AG Grid Enterprise would cost a lot for your team. How do you decide whether to pay or build?](#434-scenario-ag-grid-enterprise-would-cost-a-lot-for-your-team-how-do-you-decide-whether-to-pay-or-build)
- [435: Scenario: memory use grows steadily in a single page app that users keep open all day. What do you check?](#435-scenario-memory-use-grows-steadily-in-a-single-page-app-that-users-keep-open-all-day-what-do-you-check)
- [436: Scenario: your team uses Formik and asks whether to migrate to React Hook Form. What do you advise?](#436-scenario-your-team-uses-formik-and-asks-whether-to-migrate-to-react-hook-form-what-do-you-advise)
- [437: Scenario: someone wants to add a package to solve a small problem, like formatting bytes or checking if a value is empty. How do you decide?](#437-scenario-someone-wants-to-add-a-package-to-solve-a-small-problem-like-formatting-bytes-or-checking-if-a-value-is-empty-how-do-you-decide)
- [438: How do you evaluate the bundle cost of a UI kit before adopting it?](#438-how-do-you-evaluate-the-bundle-cost-of-a-ui-kit-before-adopting-it)
- [439: How do you handle global CSS and resets from several libraries without conflicts?](#439-how-do-you-handle-global-css-and-resets-from-several-libraries-without-conflicts)
- [440: How do you write a custom hook library that works well with SSR, StrictMode and concurrent rendering?](#440-how-do-you-write-a-custom-hook-library-that-works-well-with-ssr-strictmode-and-concurrent-rendering)
- [441: How do you keep a large set of third-party dependencies up to date without breaking things?](#441-how-do-you-keep-a-large-set-of-third-party-dependencies-up-to-date-without-breaking-things)
- [442: How do you choose between building a feature with a library or with React and browser APIs only?](#442-how-do-you-choose-between-building-a-feature-with-a-library-or-with-react-and-browser-apis-only)
- [443: How does the React ecosystem handle animations between pages, and what are the options?](#443-how-does-the-react-ecosystem-handle-animations-between-pages-and-what-are-the-options)
- [444: How do you handle images efficiently in React apps with or without a framework?](#444-how-do-you-handle-images-efficiently-in-react-apps-with-or-without-a-framework)
- [445: How do you approach state management in a local-first React app?](#445-how-do-you-approach-state-management-in-a-local-first-react-app)
- [446: How do you design a hooks API for a library you publish?](#446-how-do-you-design-a-hooks-api-for-a-library-you-publish)
- [447: How do you decide whether to use a framework (Next.js, React Router framework mode, TanStack Start) or a plain SPA with libraries?](#447-how-do-you-decide-whether-to-use-a-framework-nextjs-react-router-framework-mode-tanstack-start-or-a-plain-spa-with-libraries)
- [448: What questions would you ask when reviewing a pull request that adds a new dependency?](#448-what-questions-would-you-ask-when-reviewing-a-pull-request-that-adds-a-new-dependency)
- [449: How do you explain the overall React library ecosystem to a new developer joining the team?](#449-how-do-you-explain-the-overall-react-library-ecosystem-to-a-new-developer-joining-the-team)
- [450: What does a healthy library strategy look like for a long-lived React project?](#450-what-does-a-healthy-library-strategy-look-like-for-a-long-lived-react-project)

---

# Easy Questions (1-150)

## 1: What do people usually mean by "React libraries"?

React itself only handles rendering components and managing their state. It has no router, no data fetching layer, no form helpers and no UI components. "React libraries" means the npm packages people add on top: routers, state managers, data fetching tools, form libraries, UI kits, styling tools, charts, tables, testing tools and so on.

Some of them are made by the React team or Meta (React DevTools, the React Compiler, Lexical, StyleX), but most come from the community or from companies (React Router, TanStack, MUI, Zustand and others).

## 2: Why does a typical React project use so many third-party libraries?

React is a library, not a full framework. It leaves a lot of decisions to you: how to route, how to fetch and cache data, how to handle forms, how to style components. Angular, for example, ships most of these in the box.

That gives you freedom, but it also means each team picks its own stack. Frameworks like Next.js and React Router's framework mode fill some of these gaps, but you will still add libraries for forms, UI components, charts and so on.

## 3: How do you decide if a library is worth adding to a project?

Some things to check before adding a package:

- Is it maintained? Look at recent commits, releases and how issues are handled.
- Does it support your React version (React 19 today) and does it work with SSR or Server Components if you need that?
- Does it ship TypeScript types?
- How big is it? Check on bundlephobia or pkg-size.
- How many people use it? Weekly downloads and GitHub stars give a rough idea.
- What is the license? Some grids and chart libraries need a paid license for some features.
- Can you write the same thing yourself in an hour? If yes, you might not need it.

## 4: What is React Router?

React Router is the most used routing library for React. It maps URLs to components, handles links and navigation, reads URL params and supports nested layouts.

It can be used in three ways: as a simple declarative router (`<BrowserRouter>` and `<Routes>`), in data mode (`createBrowserRouter` with loaders and actions), or in framework mode, which is basically what Remix used to be: file-based routes, SSR, and a Vite plugin. Remix was merged into React Router v7, and v8 is the current major version.

## 5: How do you set up React Router in data mode?

You create a router with `createBrowserRouter` and render it with `RouterProvider`:

```tsx
import { createBrowserRouter, RouterProvider } from "react-router";
import { createRoot } from "react-dom/client";
import Root from "./Root";
import Home from "./Home";
import About from "./About";

const router = createBrowserRouter([
  {
    path: "/",
    Component: Root,
    children: [
      { index: true, Component: Home },
      { path: "about", Component: About },
    ],
  },
]);

createRoot(document.getElementById("root")!).render(
  <RouterProvider router={router} />,
);
```

Since v7 everything is imported from `react-router`. The old `react-router-dom` package only re-exports it for backward compatibility.

## 6: What is the difference between Link and NavLink in React Router?

Both render an `<a>` tag and navigate without a full page reload. `NavLink` also knows if its route is active, so you can style the current menu item:

```tsx
import { NavLink } from "react-router";

<NavLink
  to="/settings"
  className={({ isActive }) => (isActive ? "active" : "")}
>
  Settings
</NavLink>;
```

It also sets `aria-current="page"` on the active link by default. Use `Link` for normal links and `NavLink` for navigation menus and tabs.

## 7: How do you read URL params in React Router?

You use the `useParams` hook. For a route like `users/:userId`:

```tsx
import { useParams } from "react-router";

function UserPage() {
  const { userId } = useParams();
  return <h1>User {userId}</h1>;
}
```

Params are always strings (or `undefined`), so convert them yourself if you need a number.

## 8: How do you navigate from code in React Router?

Use the `useNavigate` hook. It returns a function you can call after a form submit, a timeout and so on:

```tsx
import { useNavigate } from "react-router";

function LoginForm() {
  const navigate = useNavigate();

  async function handleSubmit() {
    await login();
    navigate("/dashboard", { replace: true });
  }

  return <button onClick={handleSubmit}>Log in</button>;
}
```

`replace: true` replaces the current history entry, so the back button won't return to the login page. You can also pass a number, like `navigate(-1)`, to go back.

## 9: What are nested routes and what is Outlet?

Nested routes let a parent route render a shared layout, and child routes render inside it. The parent marks the spot where the child goes with `<Outlet />`:

```tsx
import { Outlet, Link } from "react-router";

function DashboardLayout() {
  return (
    <div>
      <nav>
        <Link to="stats">Stats</Link>
        <Link to="settings">Settings</Link>
      </nav>
      <Outlet />
    </div>
  );
}
```

When the URL is `/dashboard/stats`, the layout stays and only the part inside `Outlet` changes.

## 10: What is a loader in React Router?

A loader is a function attached to a route that loads data before the route renders. The component then reads the data with `useLoaderData`:

```tsx
import { useLoaderData } from "react-router";

export async function loader({ params }: { params: { id?: string } }) {
  const res = await fetch(`/api/products/${params.id}`);
  return res.json();
}

export default function Product() {
  const product = useLoaderData() as { name: string };
  return <h1>{product.name}</h1>;
}
```

Loaders run in parallel for all matched routes, which avoids the "fetch in useEffect, then render a child that fetches again" waterfall. In framework mode you get generated types, so you don't need the cast.

## 11: What is an action in React Router?

An action handles data writes for a route, usually form submissions. When a `<Form method="post">` is submitted, React Router calls the route's action, and then reloads loader data so the page shows fresh data.

```tsx
import { Form, redirect } from "react-router";

export async function action({ request }: { request: Request }) {
  const formData = await request.formData();
  await createTodo(String(formData.get("title")));
  return redirect("/todos");
}

export default function NewTodo() {
  return (
    <Form method="post">
      <input name="title" />
      <button type="submit">Add</button>
    </Form>
  );
}
```

## 12: What is TanStack Router?

TanStack Router is a router for React built with TypeScript in mind. Route paths, params and search params are fully typed, so `<Link to="/posts/$postId" params={{ postId: '1' }} />` gives a type error if the route doesn't exist or a param is missing.

It supports file-based or code-based routes, loaders, built-in caching, search param validation and preloading. TanStack Start is the full-stack framework built on top of it.

## 13: What is Redux Toolkit?

Redux Toolkit (RTK) is the official, recommended way to write Redux today. Plain Redux needed a lot of boilerplate: action types, action creators, switch statements and manual immutable updates. RTK removes most of that with helpers like `configureStore`, `createSlice` and `createAsyncThunk`, and it uses Immer so you can write "mutating" code in reducers.

It also includes RTK Query, a data fetching and caching tool. The `react-redux` package connects the store to React components.

## 14: How do you create a simple Redux Toolkit store?

```ts
import {
  configureStore,
  createSlice,
  type PayloadAction,
} from "@reduxjs/toolkit";

const counterSlice = createSlice({
  name: "counter",
  initialState: { value: 0 },
  reducers: {
    increment: (state) => {
      state.value += 1;
    },
    addBy: (state, action: PayloadAction<number>) => {
      state.value += action.payload;
    },
  },
});

export const { increment, addBy } = counterSlice.actions;

export const store = configureStore({
  reducer: { counter: counterSlice.reducer },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
```

`configureStore` sets up Redux DevTools and the thunk middleware for you. You then wrap the app in `<Provider store={store}>`.

## 15: How do components read and update Redux state?

With the `useSelector` and `useDispatch` hooks from `react-redux`:

```tsx
import { useDispatch, useSelector } from "react-redux";
import { increment, type RootState } from "./store";

function Counter() {
  const value = useSelector((state: RootState) => state.counter.value);
  const dispatch = useDispatch();
  return <button onClick={() => dispatch(increment())}>{value}</button>;
}
```

The component re-renders only when the value returned by the selector changes (compared with `===`). In TypeScript projects people usually create typed versions of these hooks once and use them everywhere.

## 16: What is Zustand?

Zustand is a small state management library (around 1 KB gzipped). You create a store with a hook, and any component can use that hook. No provider is needed, no actions or reducers, just state and functions that update it.

It became very popular because it is much simpler than Redux but still handles global state well, and it only re-renders components that use the part of state that changed.

## 17: How do you create and use a Zustand store?

```tsx
import { create } from "zustand";

type CartState = {
  items: string[];
  addItem: (item: string) => void;
  clear: () => void;
};

export const useCartStore = create<CartState>()((set) => ({
  items: [],
  addItem: (item) => set((state) => ({ items: [...state.items, item] })),
  clear: () => set({ items: [] }),
}));

function CartCount() {
  const count = useCartStore((state) => state.items.length);
  return <span>{count}</span>;
}
```

`set` merges the object you give it into the current state (one level deep). Pass a selector to the hook so the component only re-renders when that value changes.

## 18: What is Jotai?

Jotai is an "atomic" state library. Instead of one big store, you create small pieces of state called atoms and combine them. Components use atoms with a hook that looks like `useState`.

It is good when you have many small, independent pieces of state, or state that depends on other state. It works well with Suspense and has utilities for storage, async data and more.

## 19: How do you use an atom in Jotai?

```tsx
import { atom, useAtom, useAtomValue } from "jotai";

const countAtom = atom(0);
const doubleAtom = atom((get) => get(countAtom) * 2);

function Counter() {
  const [count, setCount] = useAtom(countAtom);
  return <button onClick={() => setCount((c) => c + 1)}>{count}</button>;
}

function Double() {
  const double = useAtomValue(doubleAtom);
  return <p>{double}</p>;
}
```

`doubleAtom` is a derived (read-only) atom. It updates automatically when `countAtom` changes.

## 20: What is MobX?

MobX is a state management library based on observables. You mark state as observable, and MobX tracks which components read which values. When a value changes, only the components that used it re-render.

You write normal mutable code (`store.count++`) and MobX handles the updates. React components need to be wrapped with `observer` from `mobx-react-lite`. It is popular in big apps with complex domain models and among teams coming from OOP backgrounds.

## 21: What was Recoil and should you use it today?

Recoil was an atomic state library from Meta, similar in spirit to Jotai. It never reached version 1.0, stopped getting updates for a long time, and the GitHub repo was archived in early 2025. It also has problems with newer React versions.

You should not start a new project with it. Jotai is the usual replacement since the ideas are very close.

## 22: What is Valtio?

Valtio is a proxy-based state library from the same group that made Zustand and Jotai (pmndrs). You create a state object with `proxy()` and change it directly. In components, `useSnapshot` returns an immutable snapshot and re-renders only when the parts you read change.

```tsx
import { proxy, useSnapshot } from "valtio";

const state = proxy({ count: 0 });

function Counter() {
  const snap = useSnapshot(state);
  return <button onClick={() => state.count++}>{snap.count}</button>;
}
```

Read from the snapshot during render, write to the proxy in event handlers.

## 23: What is XState?

XState is a library for state machines and statecharts. You describe all the possible states of something (for example `idle`, `loading`, `success`, `error`), the events it accepts, and the transitions between them. Impossible states like "loading and error at the same time" can't happen.

It is useful for complex flows: multi-step wizards, checkout, media players, auth flows. The `@xstate/react` package gives you hooks like `useMachine`. XState also has a visual editor (Stately) to draw and inspect machines.

## 24: What is TanStack Query?

TanStack Query (formerly React Query) is a library for fetching, caching and updating server data. You tell it how to fetch something and give it a key, and it handles loading and error states, caching, deduplicating requests, background refetching, retries and pagination.

The main idea is that server data is different from client state. It lives on the server, can get stale, and is shared between components, so it should be managed by a cache, not stored in Redux or `useState`.

## 25: How do you fetch data with useQuery?

```tsx
import {
  QueryClient,
  QueryClientProvider,
  useQuery,
} from "@tanstack/react-query";

const queryClient = new QueryClient();

function Todos() {
  const { data, isPending, isError, error } = useQuery({
    queryKey: ["todos"],
    queryFn: () => fetch("/api/todos").then((res) => res.json()),
  });

  if (isPending) return <p>Loading...</p>;
  if (isError) return <p>Error: {error.message}</p>;
  return (
    <ul>
      {data.map((t: { id: number; title: string }) => (
        <li key={t.id}>{t.title}</li>
      ))}
    </ul>
  );
}

export default function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Todos />
    </QueryClientProvider>
  );
}
```

Note that `fetch` does not reject on HTTP errors like 404 or 500. In real code check `res.ok` and throw, so TanStack Query sees the error.

## 26: What is a query key in TanStack Query?

The query key is an array that uniquely identifies a piece of cached data, for example `['todos']` or `['todo', 5]` or `['todos', { status: 'done', page: 2 }]`.

Two components that use the same key share the same cache entry and the same request. When the key changes (say the page number), TanStack Query fetches the new data. Anything your `queryFn` depends on should be in the key, otherwise you'll get stale or wrong data.

## 27: How do you send data to the server with useMutation?

```tsx
import { useMutation, useQueryClient } from "@tanstack/react-query";

function AddTodo() {
  const queryClient = useQueryClient();
  const mutation = useMutation({
    mutationFn: (title: string) =>
      fetch("/api/todos", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title }),
      }),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ["todos"] }),
  });

  return (
    <button
      disabled={mutation.isPending}
      onClick={() => mutation.mutate("New todo")}
    >
      Add
    </button>
  );
}
```

After a successful create, invalidating `['todos']` makes the list refetch.

## 28: What is SWR?

SWR is a data fetching library from Vercel, the company behind Next.js. The name comes from the HTTP cache strategy "stale-while-revalidate": show cached (stale) data right away, then fetch fresh data in the background and update.

```tsx
import useSWR from "swr";

const fetcher = (url: string) => fetch(url).then((r) => r.json());

function Profile() {
  const { data, error, isLoading } = useSWR("/api/user", fetcher);
  if (isLoading) return <p>Loading...</p>;
  if (error) return <p>Failed to load</p>;
  return <p>Hello {data.name}</p>;
}
```

It is smaller and simpler than TanStack Query, with fewer features around mutations and cache control.

## 29: What is Axios?

Axios is an HTTP client for the browser and Node.js. It wraps requests in a promise-based API with some extras: it parses JSON automatically, rejects on non-2xx status codes, supports request and response interceptors, has a simple way to set a base URL and default headers, and supports upload progress.

```ts
import axios from "axios";

const { data } = await axios.get("/api/users", { params: { page: 2 } });
```

## 30: Should you use Axios or fetch in a React app?

`fetch` is built into every browser and Node, so it adds nothing to your bundle. It covers most needs, but you have to check `res.ok` yourself, call `res.json()`, and write your own helpers for things like auth headers.

Axios gives you interceptors, automatic JSON handling and error rejection out of the box. If you only need a few calls, a small wrapper around `fetch` is enough. If you want interceptors for auth and logging across many endpoints, Axios (or a small `fetch` wrapper like `ky`) saves time.

## 31: What is ky?

`ky` is a small HTTP client built on top of `fetch`. It adds the things people usually write wrappers for: throwing on HTTP errors, JSON helpers, retries, timeouts, hooks (similar to interceptors) and a prefix URL.

```ts
import ky from "ky";

const api = ky.create({ prefixUrl: "/api", timeout: 10000 });
const user = await api.get("users/1").json<{ name: string }>();
```

It is much smaller than Axios because it uses the native `fetch`.

## 32: What is Apollo Client?

Apollo Client is the most popular GraphQL client for React. You write GraphQL queries and use hooks like `useQuery` and `useMutation` to run them. It keeps results in a normalized cache, so if two queries return the same object (same `__typename` and `id`), updating it in one place updates it everywhere.

It also supports subscriptions, pagination helpers, local state and works with Suspense.

## 33: What is urql?

urql is a lighter GraphQL client for React. By default it uses a simple document cache (it caches whole query results and clears them when a mutation touches the same types). If you need a normalized cache like Apollo, you add the Graphcache exchange.

It is built around "exchanges", which are small plugins that process each operation, so you can customize auth, retries and caching.

## 34: What is tRPC?

tRPC lets you call backend functions from a TypeScript frontend with full type safety and no code generation. You define procedures on the server, export the router's type, and the client knows every procedure's input and output types.

It works best when the frontend and backend are in the same TypeScript repo (often a monorepo or a Next.js app). In React it integrates with TanStack Query, so you get caching and loading states too.

## 35: What is React Hook Form?

React Hook Form (RHF) is the most popular form library for React. It uses uncontrolled inputs and refs by default, so typing in a field does not re-render the whole form. That makes it fast even with large forms.

It handles values, validation, errors, dirty and touched state, and submit. It also works with schema validators like Zod, Yup and Valibot through `@hookform/resolvers`.

## 36: How do you build a simple form with React Hook Form?

```tsx
import { useForm } from "react-hook-form";

type FormValues = { email: string; password: string };

function LoginForm() {
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>();

  const onSubmit = async (values: FormValues) => {
    await login(values);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register("email", { required: "Email is required" })} />
      {errors.email && <span>{errors.email.message}</span>}
      <input type="password" {...register("password", { minLength: 8 })} />
      <button disabled={isSubmitting}>Log in</button>
    </form>
  );
}
```

`register` returns `name`, `ref`, `onChange` and `onBlur`, which you spread onto the input. `handleSubmit` runs validation and only calls your function if the form is valid.

## 37: What is Formik and is it still a good choice?

Formik was the most popular React form library before React Hook Form. It uses controlled inputs and keeps all values in React state, so every keystroke re-renders the form. It works, but it is slower on big forms.

Formik gets very few updates now. You will still see it in older codebases, and it is fine to maintain, but most new projects choose React Hook Form or TanStack Form.

## 38: What is Zod?

Zod is a TypeScript-first schema validation library. You describe the shape of your data once, and you get both runtime validation and a TypeScript type from the same schema.

People use it to validate forms, API responses, environment variables, URL params and server inputs. The current major version is Zod 4, which is faster and smaller than v3 and also has a smaller `zod/mini` build.

## 39: How do you define a schema and get a type from it in Zod?

```ts
import { z } from "zod";

const UserSchema = z.object({
  name: z.string().min(1),
  email: z.email(),
  age: z.number().int().positive().optional(),
});

type User = z.infer<typeof UserSchema>;

const result = UserSchema.safeParse({ name: "Ana", email: "not-an-email" });
if (!result.success) {
  console.log(result.error.issues);
}
```

In Zod 4, string formats like `z.email()` and `z.url()` are top-level functions. The old `z.string().email()` still works but is deprecated.

## 40: What is Yup?

Yup is a schema validation library that was very common with Formik. It has a chained API similar to Zod (`yup.string().email().required()`), and it can also transform values (cast strings to numbers and so on).

It has TypeScript support through `InferType`, but Zod was designed for TypeScript from the start, so most new TypeScript projects pick Zod or Valibot.

## 41: What is Valibot?

Valibot is a schema validation library similar to Zod, but built from small functions you combine with `pipe` instead of chained methods. Because every check is a separate function, bundlers can drop what you don't use, so the bundle is usually much smaller.

```ts
import * as v from "valibot";

const LoginSchema = v.object({
  email: v.pipe(v.string(), v.email()),
  password: v.pipe(v.string(), v.minLength(8)),
});
```

It is a good choice when bundle size matters a lot, for example in client-heavy apps.

## 42: What is TanStack Form?

TanStack Form is a headless form library from the TanStack team. It is fully typed, works with React and other frameworks, and has fine-grained subscriptions so only the fields that change re-render.

It supports sync and async validation at the field and form level and works with Standard Schema libraries (Zod, Valibot, ArkType) without an adapter. It reached v1 in 2025, so it is newer than React Hook Form and has a smaller community, but it is a solid choice for type-heavy forms.

## 43: What is MUI?

MUI is a company and a set of React libraries. The best known is Material UI (`@mui/material`), a large component library that implements Google's Material Design. It has buttons, inputs, dialogs, tables, menus, tabs, autocomplete and many more.

MUI also has MUI X (advanced components like the Data Grid, Date Pickers and Charts, some paid), Joy UI (another design, now not actively developed) and Base UI (unstyled components, now its own project).

## 44: How do you install and use Material UI?

```bash
npm install @mui/material @emotion/react @emotion/styled
```

```tsx
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";

function SignUp() {
  return (
    <>
      <TextField label="Email" variant="outlined" />
      <Button variant="contained">Sign up</Button>
    </>
  );
}
```

Material UI uses Emotion for styling by default, which is why those two packages are needed. You can wrap the app in a `ThemeProvider` to change colors, fonts and spacing.

## 45: What is shadcn/ui?

shadcn/ui is a collection of React components that you copy into your project instead of installing as a dependency. You run a CLI command like `npx shadcn@latest add button`, and it puts the component's source code in your `components/ui` folder.

The components are built with Tailwind CSS and headless primitives (Radix UI, or Base UI as an option). Since the code is yours, you can change anything without fighting a library's API.

## 46: How is shadcn/ui different from a normal component library?

With MUI or Chakra, you install a package and use its components. You customize them through props and themes, and you get updates by bumping the version.

With shadcn/ui there is no package for the components. The code lives in your repo, so:

- You can change anything directly.
- You don't get automatic updates. If the upstream component gets a fix, you have to pull it in yourself.
- Your team owns the code, its bugs and its tests.

It works best for teams that want their own design system and are comfortable with Tailwind.

## 47: What is Radix UI?

Radix UI (Radix Primitives) is a set of unstyled, accessible React components: Dialog, Dropdown Menu, Popover, Tooltip, Tabs, Select, Accordion and others. They handle keyboard navigation, focus management, ARIA attributes and positioning, and you add all the styles.

Many libraries are built on top of it, including shadcn/ui. Radix is still widely used, but most of its original team now works on Base UI, so new development has slowed.

## 48: What is Base UI?

Base UI (`@base-ui/react`) is an unstyled component library made by people from Radix, Floating UI and Material UI. It reached v1 around the end of 2025. It is similar to Radix: accessible, headless components that you style yourself.

One visible difference is composition. Radix uses an `asChild` prop to render your own element, while Base UI uses a `render` prop. shadcn/ui now supports Base UI as an alternative to Radix.

## 49: What is Chakra UI?

Chakra UI is a component library focused on good defaults, accessibility and an easy styling API through props like `p={4}` or `color="red.500"`. Version 3 was a big rewrite. It is built on Ark UI (state machines from Zag.js) and uses a new styling engine with recipes and design tokens, similar to Panda CSS.

It is popular for dashboards and products where you want something that looks good quickly but is still easy to theme.

## 50: What is Mantine?

Mantine is a full-featured React component library. Besides 100+ components, it ships a lot of extra packages: `@mantine/hooks` (a big set of useful hooks), `@mantine/form`, `@mantine/dates`, `@mantine/notifications`, `@mantine/charts`, a rich text editor and more.

Since v7 it uses plain CSS files and CSS modules instead of runtime CSS-in-JS, so it works well with Server Components and has no runtime styling cost.

## 51: What is Ant Design?

Ant Design (`antd`) is a large component library from Ant Group (Alibaba), very common in enterprise apps and admin panels. It has rich components like tables with filters and sorting, forms with built-in validation, tree selects, cascaders, upload and date pickers.

Version 6 came out at the end of 2025. It needs React 18 or later, uses CSS variables by default and dropped IE support. Most v5 APIs still work.

## 52: What is React Bootstrap?

React Bootstrap rewrites Bootstrap's components as React components. It doesn't use Bootstrap's JavaScript or jQuery, but you still include Bootstrap's CSS.

```tsx
import Button from "react-bootstrap/Button";
import "bootstrap/dist/css/bootstrap.min.css";

<Button variant="primary">Save</Button>;
```

It is a good fit if your project or company already uses Bootstrap styles.

## 53: What is Headless UI?

Headless UI is a set of unstyled, accessible components from the Tailwind CSS team. It covers the common interactive pieces: Menu, Listbox, Combobox, Dialog, Popover, Disclosure, Switch, Tabs and a few form components.

It is smaller than Radix and made to be styled with Tailwind classes. Tailwind's paid UI kits (Tailwind Plus) use it.

## 54: What is React Aria?

React Aria is a library from Adobe for building accessible components. It comes in two forms:

- **React Aria hooks** (`useButton`, `useComboBox` and so on), which give you behavior and ARIA props, and you render all the markup.
- **React Aria Components**, which are ready unstyled components built on those hooks.

It is known for very careful accessibility, internationalization (dates, numbers, right-to-left) and handling of touch, mouse and keyboard input. Adobe's own design system, React Spectrum, is built on it.

## 55: How is Tailwind CSS used in React projects?

Tailwind is a utility-first CSS framework. Instead of writing CSS files, you put small utility classes on elements:

```tsx
function Card({ title }: { title: string }) {
  return (
    <div className="rounded-lg border p-4 shadow-sm hover:shadow-md">
      {title}
    </div>
  );
}
```

Tailwind scans your files and generates only the classes you use. In v4, the setup is a Vite plugin (`@tailwindcss/vite`) and one line in your CSS: `@import "tailwindcss";`. Configuration lives in CSS with `@theme` instead of a `tailwind.config.js` file.

## 56: What is clsx?

`clsx` is a tiny helper for building `className` strings based on conditions:

```tsx
import clsx from "clsx";

<button
  className={clsx(
    "btn",
    { "btn-active": isActive, "btn-disabled": disabled },
    size === "lg" && "btn-lg",
  )}
/>;
```

It skips falsy values and joins the rest with spaces. `classnames` is an older package that does the same thing.

## 57: What is tailwind-merge?

`tailwind-merge` merges Tailwind class strings and removes conflicts, keeping the last one. For example `twMerge('px-2 py-1', 'px-4')` gives `'py-1 px-4'`.

Without it, passing `className="px-4"` to a component that already has `px-2` would leave both classes, and which one wins depends on the CSS order, not on the order in the string. shadcn/ui combines it with `clsx` in a helper usually called `cn`:

```ts
import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
```

## 58: What is class-variance-authority (cva)?

`cva` helps you define component variants as class names. You list a base class string and the classes for each variant, and it returns a function that builds the right string:

```ts
import { cva } from "class-variance-authority";

const button = cva("rounded font-medium", {
  variants: {
    intent: {
      primary: "bg-blue-600 text-white",
      secondary: "bg-gray-100 text-gray-900",
    },
    size: { sm: "px-2 py-1 text-sm", md: "px-4 py-2" },
  },
  defaultVariants: { intent: "primary", size: "md" },
});

button({ intent: "secondary", size: "sm" });
```

It is used a lot with Tailwind and shadcn/ui.

## 59: What is styled-components?

styled-components is a CSS-in-JS library. You write real CSS inside tagged template literals, and it creates a React component with a generated, scoped class name:

```tsx
import styled from "styled-components";

const Button = styled.button<{ $primary?: boolean }>`
  padding: 8px 16px;
  background: ${(p) => (p.$primary ? "royalblue" : "white")};
`;
```

It was one of the most popular styling tools for years. In 2025 the maintainer announced it is in maintenance mode, and it does not work in React Server Components because it injects styles at runtime. Many teams now move to CSS modules, Tailwind or zero-runtime CSS-in-JS.

## 60: What is Emotion?

Emotion is another CSS-in-JS library. It offers a `styled` API (like styled-components) and a `css` prop you can put on any element. Material UI uses Emotion as its default styling engine, so it is installed in many apps.

Like styled-components, it generates styles at runtime, so it has some performance cost and needs client components when used with Server Components.

## 61: What are CSS Modules?

CSS Modules are normal CSS files where class names are scoped to the file by the build tool. You import the file and use the generated class names:

```tsx
import styles from "./Card.module.css";

function Card() {
  return <div className={styles.card}>Hello</div>;
}
```

Vite, Next.js and most bundlers support them with no extra setup. There is no runtime cost, they work with Server Components, and they avoid global class name clashes.

## 62: What is vanilla-extract?

vanilla-extract is a "zero-runtime" CSS-in-TypeScript library. You write styles in `.css.ts` files using TypeScript objects, and at build time they are turned into static CSS files with scoped class names.

```ts
// button.css.ts
import { style } from "@vanilla-extract/css";

export const button = style({
  padding: 8,
  borderRadius: 4,
  ":hover": { opacity: 0.8 },
});
```

You get type-safe styles and themes with no runtime styling cost.

## 63: What is StyleX?

StyleX is Meta's styling library, used on facebook.com and Instagram. You define styles with `stylex.create` and apply them with `stylex.props`. A compiler turns them into atomic CSS classes at build time.

```tsx
import * as stylex from "@stylexjs/stylex";

const styles = stylex.create({
  base: { padding: 8, color: "black" },
  active: { color: "blue" },
});

function Item({ active }: { active: boolean }) {
  return (
    <div {...stylex.props(styles.base, active && styles.active)}>Item</div>
  );
}
```

The last style wins in a predictable way, which makes it easy to pass style overrides between components.

## 64: What is Panda CSS?

Panda CSS is a zero-runtime CSS-in-JS library from the Chakra UI team. You write styles as objects with a `css()` function or with style props on generated JSX components, and Panda extracts them into atomic CSS at build time.

It has design tokens, recipes (variants) and type safety. It works with Server Components because no styles are created at runtime.

## 65: What is Motion (formerly Framer Motion)?

Motion is the most popular animation library for React. It used to be called Framer Motion and was published as `framer-motion`. In 2025 it became an independent project named Motion, and the React API is now imported from `motion/react`.

It gives you `motion.div` style components that animate with props, exit animations, layout animations, gestures (hover, tap, drag) and scroll-based animations.

## 66: How do you animate an element with Motion?

```tsx
import { motion } from "motion/react";

function FadeIn() {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3 }}
    >
      Hello
    </motion.div>
  );
}
```

`initial` is the starting state, `animate` is the target. When values in `animate` change, Motion animates to the new values. `whileHover` and `whileTap` work the same way for gestures.

## 67: What is React Spring?

React Spring is an animation library based on spring physics instead of fixed durations and easing curves. You describe the target values and the spring settings (tension, friction), and the animation feels natural.

```tsx
import { useSpring, animated } from "@react-spring/web";

function Box() {
  const styles = useSpring({ from: { opacity: 0 }, to: { opacity: 1 } });
  return <animated.div style={styles}>Hi</animated.div>;
}
```

It also has packages for React Three Fiber and React Native.

## 68: What is AutoAnimate?

AutoAnimate (`@formkit/auto-animate`) adds simple animations when children are added, removed or moved inside a container, with one line:

```tsx
import { useAutoAnimate } from "@formkit/auto-animate/react";

function List({ items }: { items: string[] }) {
  const [parent] = useAutoAnimate();
  return (
    <ul ref={parent}>
      {items.map((i) => (
        <li key={i}>{i}</li>
      ))}
    </ul>
  );
}
```

It is good for small list or accordion animations when you don't want a full animation library.

## 69: What is Recharts?

Recharts is a popular chart library for React built on top of SVG and D3 modules. You build charts from components like `LineChart`, `BarChart`, `XAxis`, `YAxis`, `Tooltip` and `Legend`.

It is easy to start with and fits well with the React way of writing UI. Since it renders SVG, it gets slow with many thousands of points, so for very large datasets a Canvas-based library is better.

## 70: How do you create a simple line chart with Recharts?

```tsx
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
} from "recharts";

const data = [
  { month: "Jan", sales: 400 },
  { month: "Feb", sales: 300 },
  { month: "Mar", sales: 550 },
];

function SalesChart() {
  return (
    <ResponsiveContainer width="100%" height={300}>
      <LineChart data={data}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="month" />
        <YAxis />
        <Tooltip />
        <Line type="monotone" dataKey="sales" stroke="#2563eb" />
      </LineChart>
    </ResponsiveContainer>
  );
}
```

`ResponsiveContainer` makes the chart resize with its parent. The parent needs a real size, or the chart will render with zero height.

## 71: What is Nivo?

Nivo is a chart library built on D3 with ready components for many chart types: bar, line, pie, heatmap, treemap, sankey, calendar, chord and more. Many charts can render to SVG, Canvas or HTML.

It has good defaults, theming and animations, and an interactive website where you can configure a chart and copy the code.

## 72: What is visx?

visx is a collection of low-level visualization components from Airbnb. It combines D3's math (scales, shapes, layouts) with React rendering. It does not give you ready-made charts. You build your own from pieces like `Group`, `Bar`, `AxisBottom` and `scaleLinear`.

It is a good choice when you need custom charts and full control, and you are fine writing more code.

## 73: What is react-chartjs-2?

`react-chartjs-2` is a React wrapper for Chart.js, a popular Canvas-based chart library. You register the Chart.js parts you need and render components like `<Line>` or `<Bar>`:

```tsx
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Tooltip,
} from "chart.js";
import { Bar } from "react-chartjs-2";

ChartJS.register(CategoryScale, LinearScale, BarElement, Tooltip);

<Bar
  data={{ labels: ["A", "B"], datasets: [{ label: "Votes", data: [12, 19] }] }}
/>;
```

Canvas rendering handles more data points than SVG.

## 74: What is TanStack Table?

TanStack Table (formerly React Table) is a headless table library. It handles the logic of tables: sorting, filtering, pagination, grouping, row selection, column visibility, column resizing and pinning. It does not render any markup, so you write the `<table>` (or divs) yourself.

This gives you full control of the look, which is why many design systems, including shadcn/ui's data table, are built on it.

## 75: What is AG Grid?

AG Grid is a feature-rich data grid for JavaScript with an official React package (`ag-grid-react`). It handles very large datasets with row and column virtualization, and supports sorting, filtering, editing, cell renderers, pinned columns and CSV export.

It has a free Community edition (MIT) and a paid Enterprise edition with things like row grouping, pivoting, Excel export, server-side row model and integrated charts.

## 76: What is the MUI X Data Grid?

The MUI X Data Grid is a data grid from MUI that matches Material UI's style. It comes in three plans:

- **DataGrid** (free, MIT): sorting, filtering, pagination, editing.
- **DataGridPro** (paid): column pinning, tree data, lazy loading, multi-column sorting and more.
- **DataGridPremium** (paid): row grouping, aggregation, Excel export, pivoting.

It is a natural pick if your app already uses Material UI.

## 77: What is TanStack Virtual?

TanStack Virtual is a headless virtualization library. It renders only the rows (or columns) that are visible in a scroll container, plus a few extra, so a list of 100,000 items still renders fast.

It works with fixed, variable and dynamically measured sizes, horizontal and vertical lists, and grids. You render the markup and position items using the values it gives you.

## 78: What is react-window?

`react-window` is a small virtualization library from Brian Vaughn, a former React core team member. It is a lighter rewrite of the older `react-virtualized`. Version 2 has `List` and `Grid` components that render only the visible items.

It works well when items have known sizes. For dynamic heights and more flexibility, people often use TanStack Virtual or react-virtuoso.

## 79: What is react-virtuoso?

react-virtuoso is a virtualization library that handles items of unknown and changing size automatically. You don't need to measure anything. It also supports grouped lists with sticky headers, tables, grids, "load more" at the end, and chat-style lists that start at the bottom.

```tsx
import { Virtuoso } from "react-virtuoso";

<Virtuoso
  style={{ height: 400 }}
  data={messages}
  itemContent={(index, msg) => <div>{msg.text}</div>}
/>;
```

## 80: What is react-i18next?

`react-i18next` is the React binding for i18next, the most popular JavaScript internationalization framework. It gives you the `useTranslation` hook, the `Trans` component for translations with JSX inside, and support for namespaces, plurals, interpolation, language detection and lazy loading of translation files.

## 81: How do you translate text with react-i18next?

First you initialize i18next once:

```ts
import i18n from "i18next";
import { initReactI18next } from "react-i18next";

i18n.use(initReactI18next).init({
  lng: "en",
  fallbackLng: "en",
  resources: {
    en: { translation: { welcome: "Welcome, {{name}}!" } },
    de: { translation: { welcome: "Willkommen, {{name}}!" } },
  },
});
```

Then use the hook in components:

```tsx
import { useTranslation } from "react-i18next";

function Header({ name }: { name: string }) {
  const { t, i18n } = useTranslation();
  return (
    <>
      <h1>{t("welcome", { name })}</h1>
      <button onClick={() => i18n.changeLanguage("de")}>DE</button>
    </>
  );
}
```

## 82: What is react-intl?

`react-intl` is part of FormatJS. It is built around the ICU message format and the browser's `Intl` APIs. It gives you components like `FormattedMessage`, `FormattedNumber` and `FormattedDate`, and the `useIntl` hook.

```tsx
import { FormattedMessage } from "react-intl";

<FormattedMessage
  id="cart.items"
  defaultMessage="{count, plural, one {# item} other {# items}}"
  values={{ count: 3 }}
/>;
```

It is popular in larger companies and works well with translation management systems that support ICU.

## 83: What is Lingui?

Lingui is an i18n library that lets you write messages in your source language directly in the code, using macros like `<Trans>` or `` t`Hello` ``. A CLI extracts the messages into catalog files for translators, and a compile step turns them into small, fast runtime code.

It uses ICU message format and is known for small runtime size and good developer experience.

## 84: What is date-fns?

`date-fns` is a date utility library made of small, separate functions: `format`, `addDays`, `differenceInDays`, `isBefore`, `parseISO` and many more. It works with native `Date` objects and doesn't change them.

```ts
import { format, addDays } from "date-fns";

format(addDays(new Date(), 7), "yyyy-MM-dd");
```

Since each function is its own import, bundlers only include what you use. Version 4 added first-class time zone support through `@date-fns/tz`.

## 85: What is Day.js?

Day.js is a tiny (about 2 KB) date library with an API almost the same as Moment.js. It is popular as a drop-in replacement for Moment.

```ts
import dayjs from "dayjs";

dayjs().add(7, "day").format("YYYY-MM-DD");
```

Extra features like relative time, time zones and custom parsing are added through plugins. Day.js objects are immutable, unlike Moment's.

## 86: Why do people avoid Moment.js today?

Moment.js is in maintenance mode, and its own team recommends using other libraries for new projects. The main problems are:

- It is large and doesn't tree-shake, so the whole library (and often all locales) ends up in the bundle.
- Its objects are mutable, so `date.add(1, 'day')` changes the original date, which causes bugs.

Alternatives are date-fns, Day.js, Luxon, or the native `Intl` APIs and, where available, `Temporal`.

## 87: What is Luxon?

Luxon is a date library made by one of the Moment.js maintainers. It has immutable `DateTime` objects and strong built-in support for time zones and locales through the `Intl` API.

```ts
import { DateTime } from "luxon";

DateTime.now()
  .setZone("Europe/Berlin")
  .plus({ days: 1 })
  .toFormat("yyyy-MM-dd HH:mm");
```

It is a good fit when your app deals with many time zones.

## 88: Do you always need a date library in React?

No. For many apps, the browser's `Intl.DateTimeFormat` and `Intl.RelativeTimeFormat` are enough to format dates and relative times in any locale:

```ts
new Intl.DateTimeFormat("de-DE", { dateStyle: "long" }).format(new Date());
```

For date math and time zones, the new `Temporal` API is being added to JavaScript and is already available in some browsers. Until it is everywhere, libraries like date-fns or Day.js are still useful for date arithmetic and parsing.

## 89: What is lodash and do you still need it?

Lodash is a utility library with helpers for arrays, objects, strings and functions: `debounce`, `throttle`, `groupBy`, `cloneDeep`, `isEqual`, `get` and many more.

Modern JavaScript covers a lot of what it used to be needed for (`Array.prototype.flat`, `Object.groupBy`, optional chaining, `structuredClone`). If you still use it, import single functions (`lodash-es` or `lodash/debounce`) so you don't ship the whole library. `es-toolkit` is a newer, smaller and faster alternative with a lodash compatible layer.

## 90: What is Immer?

Immer lets you write immutable updates as if you were mutating the data. You get a "draft" object, change it, and Immer creates a new object with your changes and structural sharing for the parts you didn't touch.

```ts
import { produce } from "immer";

const next = produce(state, (draft) => {
  draft.user.address.city = "Paris";
  draft.todos.push({ id: 3, done: false });
});
```

Redux Toolkit uses Immer inside `createSlice`. Zustand has an Immer middleware, and `use-immer` gives you a `useImmer` hook as a replacement for `useState`.

## 91: What is dnd-kit?

`dnd-kit` is a modern drag and drop toolkit for React. It is modular (core, sortable, utilities), supports mouse, touch and keyboard, and has accessibility features like screen reader announcements built in.

It is commonly used for sortable lists, kanban boards and dragging items between containers.

## 92: What happened to react-beautiful-dnd?

`react-beautiful-dnd` was a very popular drag and drop library from Atlassian, made for lists and boards. Atlassian deprecated it and archived the repo in 2025, and it does not support newer React versions well.

Options today:

- `@hello-pangea/dnd`, a community fork with the same API, if you want an easy migration.
- `dnd-kit`, for more flexible new work.
- Atlassian's own `@atlaskit/pragmatic-drag-and-drop`, which is framework agnostic.

## 93: What is react-dropzone?

`react-dropzone` gives you a hook to create a drag-and-drop file upload area:

```tsx
import { useDropzone } from "react-dropzone";

function Uploader() {
  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    accept: { "image/*": [] },
    onDrop: (files) => console.log(files),
  });

  return (
    <div {...getRootProps()}>
      <input {...getInputProps()} />
      {isDragActive ? "Drop here" : "Drag files or click to choose"}
    </div>
  );
}
```

It only picks the files. Uploading them is up to you.

## 94: What is react-select?

`react-select` is a flexible select (dropdown) component with search, multi-select, async loading of options, creatable options, grouping and custom rendering. It is used a lot when the native `<select>` is not enough.

It brings its own Emotion-based styles. If you use a UI kit like MUI or Mantine, you'd usually use their Autocomplete or Combobox instead.

## 95: What is Downshift?

Downshift is a set of hooks (`useCombobox`, `useSelect`, `useMultipleSelection`) for building accessible autocomplete and select components. It gives you state and the right props for the input, menu and items, and you write all the markup and styles.

It is a good choice when you need a custom combobox that doesn't fit any UI kit.

## 96: What is react-day-picker?

`react-day-picker` is a flexible date picker component. It supports single, multiple and range selection, disabled dates, custom rendering and localization. Version 9 uses date-fns internally and also supports time zones.

shadcn/ui's Calendar component is built on it.

## 97: What is react-hot-toast?

`react-hot-toast` is a small library for toast notifications. You add a `<Toaster />` once and call `toast()` from anywhere:

```tsx
import toast, { Toaster } from "react-hot-toast";

function App() {
  return (
    <>
      <button onClick={() => toast.success("Saved!")}>Save</button>
      <Toaster />
    </>
  );
}
```

It also has `toast.promise` to show loading, success and error states for a promise.

## 98: What is Sonner?

Sonner is a toast library made by Emil Kowalski with a nice stacked look and smooth animations. The API is similar to react-hot-toast:

```tsx
import { Toaster, toast } from "sonner";

<Toaster richColors />;
toast.success("Profile updated");
```

shadcn/ui uses Sonner as its toast component.

## 99: What is react-error-boundary?

React only supports error boundaries as class components. `react-error-boundary` gives you a ready `ErrorBoundary` component so you don't have to write a class:

```tsx
import { ErrorBoundary } from "react-error-boundary";

function Fallback({
  error,
  resetErrorBoundary,
}: {
  error: Error;
  resetErrorBoundary: () => void;
}) {
  return (
    <div role="alert">
      <p>Something went wrong: {error.message}</p>
      <button onClick={resetErrorBoundary}>Try again</button>
    </div>
  );
}

<ErrorBoundary FallbackComponent={Fallback}>
  <Dashboard />
</ErrorBoundary>;
```

It also has `resetKeys` and a `useErrorBoundary` hook for errors from event handlers or async code.

## 100: What is react-helmet-async and do you still need it with React 19?

`react-helmet-async` lets components set the page `<title>`, `<meta>` tags and links in the document head. It replaced the older `react-helmet`, which didn't work well with SSR.

React 19 supports this natively. You can render `<title>`, `<meta>` and `<link>` tags anywhere in your component tree and React moves them into `<head>`. For many apps you don't need a library anymore. Frameworks like Next.js and React Router framework mode also have their own metadata APIs.

## 101: What is Floating UI?

Floating UI is a library for positioning floating elements like tooltips, popovers and dropdowns next to a reference element. It handles the tricky parts: flipping to the other side when there is no room, shifting to stay in view, arrows, and updating the position on scroll and resize.

The React package (`@floating-ui/react`) also has hooks for interactions (hover, click, focus, dismiss) and focus management. It is the successor of Popper.js, and many UI kits use it internally.

## 102: What is react-icons?

`react-icons` bundles many popular icon sets (Font Awesome, Material Design, Heroicons, Feather, Bootstrap Icons and more) as React components:

```tsx
import { FaGithub } from "react-icons/fa";

<FaGithub size={24} />;
```

Icons are imported one by one from each set's folder, so only the icons you use end up in the bundle.

## 103: What is Lucide React?

Lucide is an open source icon set that started as a fork of Feather Icons. `lucide-react` gives you each icon as a React component:

```tsx
import { Camera } from "lucide-react";

<Camera size={20} strokeWidth={1.5} />;
```

It has over a thousand consistent, clean icons, is tree-shakable, and is the default icon set in shadcn/ui.

## 104: What is react-markdown?

`react-markdown` renders a Markdown string as React elements. It doesn't use `dangerouslySetInnerHTML`, so by default it is safe from XSS (raw HTML in the markdown is ignored unless you add a plugin for it).

```tsx
import Markdown from "react-markdown";
import remarkGfm from "remark-gfm";

<Markdown remarkPlugins={[remarkGfm]}>{content}</Markdown>;
```

It is built on the unified/remark/rehype ecosystem, so you can add plugins for tables, syntax highlighting, math and more.

## 105: What is Lexical?

Lexical is a rich text editor framework from Meta. It is small, fast and extensible, with a core that is framework agnostic and a React package (`@lexical/react`) for building editors with plugins.

It handles the editor state as an immutable tree, supports collaboration through Yjs, and is used for comments, chat inputs and full document editors.

## 106: What is Tiptap?

Tiptap is a headless rich text editor built on ProseMirror. It has a simple API and many extensions: bold, lists, tables, mentions, images, code blocks, placeholders and collaboration.

```tsx
import { useEditor, EditorContent } from "@tiptap/react";
import StarterKit from "@tiptap/starter-kit";

function Editor() {
  const editor = useEditor({
    extensions: [StarterKit],
    content: "<p>Hello</p>",
  });
  return <EditorContent editor={editor} />;
}
```

Because it is headless, you build your own toolbar and styles.

## 107: What is Slate?

Slate is a framework for building rich text editors in React. It gives you a data model (a nested JSON tree of nodes) and a React component to render and edit it. You decide how each element and leaf is rendered.

It is very flexible, but it is still in beta (0.x versions) and you need to write more code than with Tiptap or Lexical.

## 108: What is React Three Fiber?

React Three Fiber (`@react-three/fiber`) is a React renderer for Three.js. You describe a 3D scene with JSX, and it creates and updates Three.js objects:

```tsx
import { Canvas } from "@react-three/fiber";

function Scene() {
  return (
    <Canvas>
      <ambientLight />
      <mesh rotation={[0.5, 0.5, 0]}>
        <boxGeometry />
        <meshStandardMaterial color="orange" />
      </mesh>
    </Canvas>
  );
}
```

`@react-three/drei` adds many helpers like orbit controls, text, model loaders and environment maps.

## 109: What is the difference between react-pdf and @react-pdf/renderer?

They are two different libraries with similar names:

- **react-pdf** (by wojtekmaj) shows existing PDF files in the browser. It uses Mozilla's PDF.js and gives you `Document` and `Page` components.
- **@react-pdf/renderer** creates new PDF files from React components like `Document`, `Page`, `View` and `Text`. You can render it in the browser for download or on the server.

## 110: What is React Testing Library?

React Testing Library (`@testing-library/react`) is the standard way to test React components. It renders components into a DOM (usually jsdom) and lets you query them the way a user would: by role, label, text or placeholder.

```tsx
import { render, screen } from "@testing-library/react";

test("shows the title", () => {
  render(<h1>Welcome</h1>);
  expect(screen.getByRole("heading", { name: "Welcome" })).toBeInTheDocument();
});
```

Its main idea is to test behavior, not implementation details, so tests don't break when you refactor internals.

## 111: What is Vitest?

Vitest is a test runner built on Vite. It has a Jest-compatible API (`describe`, `it`, `expect`, `vi.fn()`), so most Jest tests work with small changes. It reuses your Vite config, supports TypeScript and ESM out of the box, and runs fast with a watch mode that only reruns affected tests.

It is the default choice for new Vite-based React projects. It also has a browser mode that runs tests in a real browser through Playwright.

## 112: What is Jest?

Jest is a test runner and assertion library from Meta, for a long time the default for React projects. It includes mocking, snapshots, coverage and a jsdom environment.

It is still widely used, especially in older projects and React Native. Its ESM and TypeScript support needs more setup (Babel or ts-jest) than Vitest, which is why many Vite projects choose Vitest instead.

## 113: What is user-event?

`@testing-library/user-event` simulates real user interactions in tests. `fireEvent.click` only dispatches one event, while `user.click` fires the full sequence a browser would (pointer down, mouse down, focus, pointer up, click). `user.type` types character by character with keydown, input and keyup events.

```tsx
import userEvent from "@testing-library/user-event";

test("types into the input", async () => {
  const user = userEvent.setup();
  render(<input aria-label="Name" />);
  await user.type(screen.getByLabelText("Name"), "Ana");
  expect(screen.getByLabelText("Name")).toHaveValue("Ana");
});
```

## 114: What is MSW?

Mock Service Worker (MSW) mocks API requests at the network level. In the browser it uses a Service Worker, and in Node (tests) it intercepts requests directly. Your app code calls `fetch` or Axios normally, and MSW returns the mocked response.

Because the same handlers work in tests, Storybook and local development, you don't need to mock `fetch` or your API client in each test.

## 115: What is Playwright?

Playwright is an end-to-end testing tool from Microsoft. It runs tests in real Chromium, Firefox and WebKit browsers, waits for elements automatically, and can run tests in parallel.

```ts
import { test, expect } from "@playwright/test";

test("user can log in", async ({ page }) => {
  await page.goto("/login");
  await page.getByLabel("Email").fill("ana@example.com");
  await page.getByLabel("Password").fill("secret123");
  await page.getByRole("button", { name: "Log in" }).click();
  await expect(page.getByRole("heading", { name: "Dashboard" })).toBeVisible();
});
```

It also has a trace viewer, codegen and a UI mode for debugging.

## 116: What is Cypress?

Cypress is an end-to-end and component testing tool that runs inside the browser. It has an interactive runner where you can see each step, time-travel through commands, and debug with DevTools.

It is very friendly for beginners and popular in many teams. Compared with Playwright, it has more limited support for multiple tabs and browsers, and parallel runs often go through its paid cloud service.

## 117: What is Storybook?

Storybook is a tool for building and documenting UI components in isolation. You write "stories", each showing a component in one state (primary button, disabled button, loading button), and browse them in a separate app.

Teams use it as a living style guide, for visual review, for accessibility checks and for interaction and visual tests. It supports React with Vite and Next.js.

## 118: What is eslint-plugin-react-hooks?

It is the official ESLint plugin from the React team. Its two classic rules are:

- `rules-of-hooks`: hooks must be called at the top level of a component or custom hook, not in conditions or loops.
- `exhaustive-deps`: the dependency arrays of `useEffect`, `useMemo` and `useCallback` must list all values they use.

Newer versions also include rules from the React Compiler that catch code the compiler can't optimize, like mutating props or reading refs during render.

## 119: What is the React Compiler?

The React Compiler is a build-time tool from the React team that automatically memoizes components and hooks. It analyzes your code and adds the equivalent of `useMemo`, `useCallback` and `React.memo` where needed, so you rarely need to write them yourself.

It reached v1.0 in 2025. You add it as a Babel plugin (`babel-plugin-react-compiler`), and it works with React 17, 18 and 19. It requires your code to follow the Rules of React.

## 120: What is Vite and why is it used for React apps?

Vite is a build tool and dev server. In development it serves your source files as native ES modules, so the server starts almost instantly and hot reload is fast. For production it builds an optimized bundle.

You create a React app with `npm create vite@latest` and pick the React template. It is the most common way to start a client-side React app today.

## 121: What happened to Create React App?

Create React App (CRA) was the official tool for starting React apps for many years. It was slow, based on Webpack, and stopped getting updates. In February 2025 the React team officially deprecated it.

The React docs now recommend starting with a framework (Next.js, React Router framework mode, Expo for native) or, for client-only apps, a build tool like Vite or Parcel.

## 122: What is Next.js?

Next.js is a full-stack React framework from Vercel. It gives you file-based routing, server-side rendering, static generation, React Server Components, server actions, API routes, image and font optimization and more.

The App Router (the `app/` folder) is the current way to build Next.js apps and uses Server Components by default. The older Pages Router still works and you'll see it in many projects.

## 123: What happened to Remix?

Remix was a full-stack React framework focused on web standards, loaders and actions. Over time Remix and React Router became almost the same thing, so the team merged Remix's features into React Router v7. If you used Remix v2, you now upgrade to React Router in framework mode.

The Remix name is being used for a new, different project that isn't based on React, so "Remix" in React interviews usually means the old framework that is now React Router.

## 124: How do you use React components in Astro?

Astro is a content-focused web framework that renders pages to HTML on the server. You can use React components inside Astro pages as "islands". By default they render to static HTML with no JavaScript. You add a `client:*` directive to make them interactive:

```astro
---
import Counter from '../components/Counter.tsx';
---
<Counter client:visible />
```

`client:visible` loads the component's JavaScript only when it scrolls into view. This keeps sites like blogs and docs very light.

## 125: What is Auth.js (NextAuth)?

Auth.js is an open source authentication library. It started as NextAuth.js for Next.js and now has adapters for other frameworks. It supports OAuth providers (Google, GitHub and many more), email magic links, credentials login, database adapters and JWT or database sessions.

In Next.js you configure it once in an `auth.ts` file and use `auth()` on the server and `useSession` on the client. The Auth.js project is now maintained by the Better Auth team.

## 126: What is Clerk?

Clerk is a hosted authentication and user management service with React components. You get ready-made `<SignIn />`, `<SignUp />` and `<UserButton />` components, hooks like `useUser` and `useAuth`, and server helpers for Next.js and other frameworks.

It handles social login, multi-factor auth, sessions and organizations. It is quick to set up, but it is a paid service once you go past the free tier, and your users live in Clerk's system.

## 127: What is the Auth0 React SDK?

`@auth0/auth0-react` is the official SDK for using Auth0 in a single page React app. You wrap the app in `Auth0Provider` and use the `useAuth0` hook:

```tsx
import { useAuth0 } from "@auth0/auth0-react";

function LoginButton() {
  const { isAuthenticated, loginWithRedirect, logout, user } = useAuth0();
  if (isAuthenticated)
    return <button onClick={() => logout()}>Log out {user?.name}</button>;
  return <button onClick={() => loginWithRedirect()}>Log in</button>;
}
```

It uses the Authorization Code flow with PKCE, and `getAccessTokenSilently` gets tokens to call your API.

## 128: What is Better Auth?

Better Auth is an open source, framework-agnostic authentication library for TypeScript. It runs inside your own backend and stores users in your own database, so you don't depend on a hosted service.

It supports email and password, social login, sessions, two-factor auth, organizations and passkeys through plugins, and it has a React client with hooks like `useSession`.

## 129: How is Firebase used in React apps?

Firebase is Google's backend-as-a-service. In React you use the modular JavaScript SDK (`firebase` package) for Authentication, Firestore, Realtime Database, Storage and more.

```ts
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

const app = initializeApp({
  apiKey: "...",
  authDomain: "...",
  projectId: "...",
});
export const auth = getAuth(app);
```

The modular SDK is tree-shakable, so import only the functions you need. Some projects use helper libraries like `reactfire`, but many just write their own small hooks.

## 130: What is the Supabase client in React?

Supabase is an open source backend built on Postgres, with auth, storage, realtime updates and edge functions. In React you use `@supabase/supabase-js`:

```ts
import { createClient } from "@supabase/supabase-js";

const supabase = createClient(
  import.meta.env.VITE_SUPABASE_URL,
  import.meta.env.VITE_SUPABASE_ANON_KEY,
);

const { data, error } = await supabase
  .from("todos")
  .select("*")
  .eq("done", false);
```

Access to data is protected with Postgres Row Level Security, so the public key can be used in the browser safely as long as your policies are correct.

## 131: What is the Socket.IO client?

`socket.io-client` connects a browser app to a Socket.IO server for real-time, two-way communication. It uses WebSocket when it can and falls back to HTTP long polling. It adds automatic reconnection, rooms and events with acknowledgements on top.

```ts
import { io } from "socket.io-client";

const socket = io("https://api.example.com");
socket.on("message", (msg) => console.log(msg));
socket.emit("join", "room-1");
```

Note that a Socket.IO client can only talk to a Socket.IO server, not to a plain WebSocket server.

## 132: What is Sentry used for in React apps?

Sentry is an error and performance monitoring service. The `@sentry/react` SDK catches unhandled errors and promise rejections, records breadcrumbs (clicks, navigation, network calls), and sends them to Sentry with stack traces.

It also has an error boundary component, integrations with React Router and TanStack Router for performance tracing, and session replay. Uploading source maps lets you see the original code in stack traces.

## 133: What is React Scan?

React Scan is a tool that highlights components on the page when they re-render. You add a script tag or a package, and you can see which parts of the UI update when you interact with the app, and how often.

It helps you find unnecessary re-renders without opening the React DevTools Profiler. It is meant for development, not production.

## 134: What is why-did-you-render?

`@welldone-software/why-did-you-render` patches React in development and logs a message when a component re-renders even though its props or state didn't really change (for example, a new object with the same values).

It is useful for finding avoidable re-renders. It only runs in development, and with the React Compiler doing automatic memoization it is needed less often than before.

## 135: What is nuqs?

`nuqs` is a library for storing state in the URL query string with a `useState`-like API. It supports Next.js, React Router, TanStack Router and plain React.

```tsx
import { useQueryState, parseAsInteger } from "nuqs";

function Pagination() {
  const [page, setPage] = useQueryState("page", parseAsInteger.withDefault(1));
  return <button onClick={() => setPage(page + 1)}>Next ({page})</button>;
}
```

It handles parsing, types, default values and batching URL updates. URL state is useful for filters, tabs and pagination because users can share and bookmark the page.

## 136: What are usehooks-ts and react-use?

They are collections of common custom hooks so you don't have to write them yourself:

- `usehooks-ts`: typed hooks like `useLocalStorage`, `useDebounceValue`, `useMediaQuery`, `useOnClickOutside`, `useInterval`.
- `react-use`: a very large older collection with hooks for sensors, side effects, lifecycles and state.

Before adding them, check that the hooks you need are maintained and SSR safe. Sometimes copying one small hook into your code is simpler than adding a dependency.

## 137: Do you need a library like uuid or nanoid to create IDs?

It depends on the use case:

- For React element ids (like linking a `<label>` to an `<input>`), use the built-in `useId` hook. It is stable between server and client.
- For random unique IDs in the browser, `crypto.randomUUID()` is built in (in secure contexts).
- `nanoid` is a tiny library for short, URL-friendly random IDs.
- `uuid` is still useful for other UUID versions, like v7 which is time-ordered.

Never use random IDs as `key` values that change on every render.

## 138: What is DOMPurify?

DOMPurify is a library that cleans HTML strings and removes anything that could run scripts (like `<script>` tags, `onerror` attributes and `javascript:` URLs). You use it before passing user-provided HTML to `dangerouslySetInnerHTML`:

```tsx
import DOMPurify from "dompurify";

function Comment({ html }: { html: string }) {
  return <div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(html) }} />;
}
```

React escapes normal text, but `dangerouslySetInnerHTML` skips that, so sanitizing is required to avoid XSS.

## 139: What is @hookform/resolvers?

`@hookform/resolvers` connects React Hook Form to schema validation libraries like Zod, Yup, Valibot, Joi, ArkType and others. Instead of writing validation rules in each `register` call, you pass a resolver:

```tsx
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";

const schema = z.object({ email: z.email(), age: z.number().min(18) });

const form = useForm({ resolver: zodResolver(schema) });
```

The form values are validated against the schema, and errors are mapped to the right fields.

## 140: What is RTK Query?

RTK Query is the data fetching and caching tool included in Redux Toolkit. You define an API with endpoints, and it generates hooks like `useGetPostsQuery` and `useAddPostMutation`. It handles loading states, caching, deduplication, refetching and cache invalidation through tags.

It solves the same problem as TanStack Query, but keeps the cache inside the Redux store. It is a natural choice if your app already uses Redux.

## 141: What is Redux DevTools?

Redux DevTools is a browser extension for inspecting a Redux store. You can see every dispatched action, the state before and after it, a diff of the changes, and you can "time travel" by jumping back to earlier states.

`configureStore` from Redux Toolkit enables it automatically in development. Zustand and Jotai can also connect to it through middleware or utilities.

## 142: How do you read and update query parameters in React Router?

With the `useSearchParams` hook. It works like `useState`, but the state lives in the URL:

```tsx
import { useSearchParams } from "react-router";

function ProductList() {
  const [searchParams, setSearchParams] = useSearchParams();
  const sort = searchParams.get("sort") ?? "name";

  return (
    <select
      value={sort}
      onChange={(e) => setSearchParams({ sort: e.target.value })}
    >
      <option value="name">Name</option>
      <option value="price">Price</option>
    </select>
  );
}
```

Setting new params adds a history entry, so the back button works. Pass `{ replace: true }` as the second argument if you don't want that.

## 143: What is react-intersection-observer?

It is a small wrapper around the browser's `IntersectionObserver` API. The `useInView` hook tells you when an element enters or leaves the viewport:

```tsx
import { useInView } from "react-intersection-observer";

function LazySection() {
  const { ref, inView } = useInView({ triggerOnce: true });
  return <section ref={ref}>{inView ? <HeavyChart /> : null}</section>;
}
```

It is commonly used for lazy loading, infinite scroll triggers and scroll animations.

## 144: What is react-resizable-panels?

`react-resizable-panels` gives you components for a panel group, the panels inside it and the resize handles between them, so you can build resizable split layouts, like an IDE with a sidebar and an editor. It supports horizontal and vertical layouts, min and max sizes, collapsing panels, keyboard resizing and saving the layout to storage.

It was created by Brian Vaughn, and shadcn/ui's Resizable component uses it. The component names changed between major versions, so check the docs for the version you install.

## 145: Which libraries are popular for carousels in React?

The two most common are:

- **Embla Carousel**: small, dependency-free, with a React hook (`useEmblaCarousel`). You write the markup and it handles swiping and scrolling. shadcn/ui's Carousel uses it.
- **Swiper**: a feature-rich slider with many effects, navigation, pagination and modules. It has React components but is heavier.

Before adding a carousel, check if CSS scroll snap (`scroll-snap-type`) is enough. Often it is.

## 146: What is cmdk?

`cmdk` is a command menu component for React, the kind you open with Cmd+K in apps like Linear or Vercel. It handles filtering and sorting items as you type, keyboard navigation, groups and accessibility. You style it yourself.

```tsx
import { Command } from "cmdk";

<Command label="Command menu">
  <Command.Input placeholder="Search..." />
  <Command.List>
    <Command.Empty>No results.</Command.Empty>
    <Command.Item onSelect={() => navigate("/settings")}>Settings</Command.Item>
  </Command.List>
</Command>;
```

## 147: What is React Email?

React Email lets you build HTML emails with React components. Email HTML is hard because email clients support only old HTML and inline styles. React Email gives you components like `Html`, `Button`, `Section` and `Text` that output email-safe markup, and a `render` function that turns your component into an HTML string.

It is often paired with sending services like Resend, SendGrid or Amazon SES.

## 148: What is react-player?

`react-player` is a component that plays media from many sources through one API: YouTube, Vimeo, Twitch, SoundCloud, Wistia, plain video and audio files and HLS or DASH streams.

```tsx
import ReactPlayer from "react-player";

<ReactPlayer src="https://www.youtube.com/watch?v=dQw4w9WgXcQ" controls />;
```

It is useful when users can paste links from different video sites. Recent versions use `src` instead of the old `url` prop, so check the version your project uses.

## 149: What is the difference between a UI kit and a headless library?

A **UI kit** (MUI, Ant Design, Chakra, Mantine) gives you finished components with styles and a theme. You get a working UI fast, but changing the look a lot can be hard.

A **headless library** (Radix, Base UI, React Aria, Headless UI, TanStack Table) gives you behavior and accessibility only: state, keyboard handling, ARIA attributes. You write all the styles, so you get full control of the look but more work.

Many teams use a headless library with Tailwind to build their own design system.

## 150: What types of libraries does a typical React app end up using?

A common modern stack looks something like this:

- Build or framework: Vite, Next.js or React Router framework mode.
- Routing: React Router or TanStack Router (or the framework's router).
- Server data: TanStack Query (or SWR, RTK Query, Apollo).
- Client state: Zustand, Jotai or Redux Toolkit, if `useState` and context aren't enough.
- Forms: React Hook Form with Zod.
- UI and styling: Tailwind with shadcn/ui, or a kit like MUI or Mantine.
- Testing: Vitest, React Testing Library, MSW and Playwright.
- Monitoring: Sentry.

Not every app needs all of these. Smaller apps can skip the state manager and even the data fetching library.

# Moderate Questions (151-300)

## 151: How do you protect routes that need a logged-in user in React Router?

In data mode, the cleanest way is to check auth in a loader (or middleware) and redirect before the page renders:

```tsx
import { redirect, type LoaderFunctionArgs } from "react-router";

export async function requireUser({ request }: LoaderFunctionArgs) {
  const user = await getCurrentUser();
  if (!user) {
    const from = new URL(request.url).pathname;
    throw redirect(`/login?from=${encodeURIComponent(from)}`);
  }
  return user;
}

const router = createBrowserRouter([
  { path: "/login", Component: Login },
  {
    path: "/app",
    loader: requireUser,
    Component: AppLayout,
    children: [/* ... */],
  },
]);
```

In declarative mode, people use a wrapper component that renders `<Navigate to="/login" replace />` when there's no user, or `<Outlet />` otherwise. Remember that this is only a UI check. The API must also check permissions.

## 152: How do you show a pending state while React Router loads the next page?

Use the `useNavigation` hook. Its `state` is `'idle'`, `'loading'` or `'submitting'`:

```tsx
import { Outlet, useNavigation } from "react-router";

function Layout() {
  const navigation = useNavigation();
  return (
    <>
      {navigation.state === "loading" && <div className="progress-bar" />}
      <main style={{ opacity: navigation.state === "loading" ? 0.6 : 1 }}>
        <Outlet />
      </main>
    </>
  );
}
```

During loading, the old page stays on screen until the new loaders finish, so you show a global indicator instead of blank pages.

## 153: What is useFetcher in React Router and when do you use it?

`useFetcher` lets you call a loader or action without navigating. It is good for things like a "like" button, inline edits, or a search box that loads suggestions, where the URL shouldn't change.

```tsx
import { useFetcher } from "react-router";

function LikeButton({ postId, liked }: { postId: string; liked: boolean }) {
  const fetcher = useFetcher();
  const optimisticLiked = fetcher.formData
    ? fetcher.formData.get("liked") === "true"
    : liked;

  return (
    <fetcher.Form method="post" action={`/posts/${postId}/like`}>
      <input type="hidden" name="liked" value={String(!optimisticLiked)} />
      <button>{optimisticLiked ? "Unlike" : "Like"}</button>
    </fetcher.Form>
  );
}
```

Each fetcher has its own state, so several can run at the same time. Reading `fetcher.formData` gives you an easy optimistic UI.

## 154: How do you handle errors in React Router routes?

Each route can have an `ErrorBoundary` (or `errorElement`). If a loader, action or render throws, React Router renders the closest error boundary instead of the route component. Inside it, `useRouteError` gives you the error:

```tsx
import { isRouteErrorResponse, useRouteError } from "react-router";

export function ErrorBoundary() {
  const error = useRouteError();
  if (isRouteErrorResponse(error)) {
    return (
      <h1>
        {error.status} {error.statusText}
      </h1>
    );
  }
  return <h1>Something went wrong</h1>;
}
```

You can throw responses on purpose, like `throw data('Not found', { status: 404 })` from a loader, to show a 404 page.

## 155: How do you lazy load routes in React Router?

In data mode, use the `lazy` property on a route. React Router loads the module only when the route matches, and it can load the code and data in parallel:

```tsx
const router = createBrowserRouter([
  {
    path: "/reports",
    lazy: async () => {
      const { loader, default: Component } = await import("./routes/reports");
      return { loader, Component };
    },
  },
]);
```

In framework mode, every route module is code split automatically. In declarative mode, you use `React.lazy` with `Suspense`.

## 156: How do you make search params type-safe in TanStack Router?

You add `validateSearch` to the route. It parses and validates the raw query string, and then `useSearch` and `Link` are fully typed:

```tsx
import { createFileRoute } from "@tanstack/react-router";
import { z } from "zod";

const productSearch = z.object({
  page: z.number().catch(1),
  sort: z.enum(["name", "price"]).catch("name"),
});

export const Route = createFileRoute("/products")({
  validateSearch: productSearch,
  component: Products,
});

function Products() {
  const { page, sort } = Route.useSearch();
  return (
    <p>
      Page {page}, sorted by {sort}
    </p>
  );
}
```

`.catch()` gives a default when the value in the URL is missing or invalid, so a broken link doesn't crash the page. Zod 4 implements Standard Schema, so TanStack Router accepts the schema directly.

## 157: How does file-based routing work in TanStack Router?

You put route files in a `routes` folder, and the TanStack Router Vite plugin generates a route tree (`routeTree.gen.ts`) with all routes and types. File names map to paths:

- `routes/__root.tsx` is the root layout.
- `routes/index.tsx` is `/`.
- `routes/posts.$postId.tsx` is `/posts/:postId`.
- `routes/_auth.tsx` is a pathless layout that wraps other routes.

Each file exports `Route = createFileRoute('/path')({...})`. You can also write routes in code if you prefer, but file-based routing gives automatic code splitting and less setup.

## 158: How do you call an API with createAsyncThunk in Redux Toolkit?

```ts
import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";

export const fetchUser = createAsyncThunk("user/fetch", async (id: string) => {
  const res = await fetch(`/api/users/${id}`);
  if (!res.ok) throw new Error("Failed to load user");
  return (await res.json()) as { id: string; name: string };
});

const userSlice = createSlice({
  name: "user",
  initialState: {
    data: null as null | { id: string; name: string },
    status: "idle" as "idle" | "loading" | "failed",
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchUser.pending, (state) => {
        state.status = "loading";
      })
      .addCase(fetchUser.fulfilled, (state, action) => {
        state.status = "idle";
        state.data = action.payload;
      })
      .addCase(fetchUser.rejected, (state) => {
        state.status = "failed";
      });
  },
});
```

`createAsyncThunk` dispatches `pending`, `fulfilled` and `rejected` actions for you. For normal API data, RTK Query is usually the better tool because it adds caching.

## 159: How do you set up an API with RTK Query?

```ts
import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

type Post = { id: number; title: string };

export const api = createApi({
  reducerPath: "api",
  baseQuery: fetchBaseQuery({ baseUrl: "/api" }),
  endpoints: (build) => ({
    getPosts: build.query<Post[], void>({ query: () => "posts" }),
    getPost: build.query<Post, number>({ query: (id) => `posts/${id}` }),
  }),
});

export const { useGetPostsQuery, useGetPostQuery } = api;
```

Then add `api.reducer` under `api.reducerPath` and `api.middleware` to the store. In a component, `const { data, isLoading } = useGetPostsQuery()` fetches and caches the data.

## 160: How does cache invalidation work in RTK Query?

Queries "provide" tags and mutations "invalidate" them. When a mutation invalidates a tag, every query that provided it refetches:

```ts
export const api = createApi({
  baseQuery: fetchBaseQuery({ baseUrl: "/api" }),
  tagTypes: ["Post"],
  endpoints: (build) => ({
    getPosts: build.query<Post[], void>({
      query: () => "posts",
      providesTags: (result) =>
        result
          ? [
              ...result.map(({ id }) => ({ type: "Post" as const, id })),
              { type: "Post", id: "LIST" },
            ]
          : [{ type: "Post", id: "LIST" }],
    }),
    addPost: build.mutation<Post, Omit<Post, "id">>({
      query: (body) => ({ url: "posts", method: "POST", body }),
      invalidatesTags: [{ type: "Post", id: "LIST" }],
    }),
  }),
});
```

Using ids in tags lets you refetch only what changed, for example invalidating `{ type: 'Post', id: 5 }` after editing post 5.

## 161: How do you type the Redux hooks in a TypeScript project?

Create pre-typed hooks once with `withTypes` and use them everywhere instead of the plain ones:

```ts
import { useDispatch, useSelector } from "react-redux";
import type { AppDispatch, RootState } from "./store";

export const useAppDispatch = useDispatch.withTypes<AppDispatch>();
export const useAppSelector = useSelector.withTypes<RootState>();
```

This way you don't need to write `(state: RootState)` in every selector, and `dispatch` knows about thunks.

## 162: What is createSelector and when do you need it?

`createSelector` (from Reselect, re-exported by Redux Toolkit) creates memoized selectors. The result is recalculated only when the inputs change.

```ts
import { createSelector } from "@reduxjs/toolkit";

const selectTodos = (state: RootState) => state.todos.items;
const selectFilter = (state: RootState) => state.todos.filter;

export const selectVisibleTodos = createSelector(
  [selectTodos, selectFilter],
  (todos, filter) => todos.filter((t) => (filter === "done" ? t.done : true)),
);
```

You need it when a selector returns a new array or object (like `.filter` or `.map`). Without memoization, `useSelector` would see a new reference every time and re-render the component on every store update.

## 163: What is createEntityAdapter in Redux Toolkit?

`createEntityAdapter` helps you store collections in a normalized shape: `{ ids: [], entities: {} }`. It gives you ready reducers like `addOne`, `upsertMany`, `updateOne`, `removeOne` and selectors like `selectAll` and `selectById`.

```ts
import { createEntityAdapter, createSlice } from "@reduxjs/toolkit";

type Book = { id: string; title: string };
const booksAdapter = createEntityAdapter<Book>({
  sortComparer: (a, b) => a.title.localeCompare(b.title),
});

const booksSlice = createSlice({
  name: "books",
  initialState: booksAdapter.getInitialState(),
  reducers: {
    bookAdded: booksAdapter.addOne,
    booksReceived: booksAdapter.setAll,
  },
});

export const booksSelectors = booksAdapter.getSelectors(
  (state: RootState) => state.books,
);
```

Normalized data makes lookups by id fast and avoids duplicate copies of the same item.

## 164: How do you avoid extra re-renders when selecting several values from a Zustand store?

If your selector returns a new object or array, the component re-renders on every store change, because the reference is always new. Use `useShallow` to compare the result shallowly:

```tsx
import { useShallow } from "zustand/react/shallow";

function Toolbar() {
  const { name, setName } = useUserStore(
    useShallow((s) => ({ name: s.name, setName: s.setName })),
  );
  return <input value={name} onChange={(e) => setName(e.target.value)} />;
}
```

Another simple option is to call the hook once per value: `const name = useUserStore((s) => s.name)`. In Zustand v5, returning a new object without `useShallow` can even cause an infinite loop warning.

## 165: How do you persist a Zustand store to localStorage?

Use the `persist` middleware:

```ts
import { create } from "zustand";
import { persist, createJSONStorage } from "zustand/middleware";

type Settings = {
  theme: "light" | "dark";
  setTheme: (t: "light" | "dark") => void;
};

export const useSettings = create<Settings>()(
  persist(
    (set) => ({
      theme: "light",
      setTheme: (theme) => set({ theme }),
    }),
    {
      name: "settings",
      storage: createJSONStorage(() => localStorage),
      partialize: (state) => ({ theme: state.theme }),
      version: 1,
    },
  ),
);
```

`partialize` decides what is saved, and `version` with `migrate` helps when the stored shape changes. With SSR, the server doesn't have the stored values, so be careful about hydration mismatches.

## 166: How do you use Redux DevTools and Immer with Zustand?

Zustand has middleware for both. You can combine them:

```ts
import { create } from "zustand";
import { devtools } from "zustand/middleware";
import { immer } from "zustand/middleware/immer";

type TodoState = {
  todos: { id: number; done: boolean }[];
  toggle: (id: number) => void;
};

export const useTodos = create<TodoState>()(
  devtools(
    immer((set) => ({
      todos: [],
      toggle: (id) =>
        set((state) => {
          const todo = state.todos.find((t) => t.id === id);
          if (todo) todo.done = !todo.done;
        }),
    })),
    { name: "todos" },
  ),
);
```

The Immer middleware needs `immer` installed. `devtools` should usually be the outermost middleware so it sees all state changes.

## 167: What is the slices pattern in Zustand?

When a store gets big, you split it into "slice" functions, each creating part of the state, and combine them into one store:

```ts
import { create, type StateCreator } from "zustand";

type BearSlice = { bears: number; addBear: () => void };
type FishSlice = { fishes: number; addFish: () => void };

const createBearSlice: StateCreator<
  BearSlice & FishSlice,
  [],
  [],
  BearSlice
> = (set) => ({
  bears: 0,
  addBear: () => set((s) => ({ bears: s.bears + 1 })),
});

const createFishSlice: StateCreator<
  BearSlice & FishSlice,
  [],
  [],
  FishSlice
> = (set) => ({
  fishes: 0,
  addFish: () => set((s) => ({ fishes: s.fishes + 1 })),
});

export const useBoundStore = create<BearSlice & FishSlice>()((...a) => ({
  ...createBearSlice(...a),
  ...createFishSlice(...a),
}));
```

Another common approach is to simply create several small independent stores.

## 168: How do you use a Zustand store outside of React components?

The hook returned by `create` also has `getState`, `setState` and `subscribe` methods:

```ts
const token = useAuthStore.getState().token;
useAuthStore.setState({ token: null });

const unsubscribe = useAuthStore.subscribe((state, prev) => {
  if (state.token !== prev.token) console.log("token changed");
});
```

This is handy in API clients (adding the auth token in an Axios interceptor), in tests and in plain utility code. You can also create a store without React using `createStore` from `zustand/vanilla`.

## 169: How do you write a derived atom that can also be written to in Jotai?

An atom can have both a read function and a write function:

```ts
import { atom } from "jotai";

const celsiusAtom = atom(20);

const fahrenheitAtom = atom(
  (get) => (get(celsiusAtom) * 9) / 5 + 32,
  (get, set, newF: number) => set(celsiusAtom, ((newF - 32) * 5) / 9),
);
```

You can also make write-only atoms (`atom(null, (get, set, arg) => ...)`) that act like actions, updating several atoms at once.

## 170: How do async atoms work with Suspense in Jotai?

If an atom's read function returns a promise, components that read it suspend until it resolves:

```tsx
import { atom, useAtomValue } from "jotai";
import { Suspense } from "react";

const userIdAtom = atom(1);
const userAtom = atom(async (get) => {
  const res = await fetch(`/api/users/${get(userIdAtom)}`);
  return res.json();
});

function UserName() {
  const user = useAtomValue(userAtom);
  return <p>{user.name}</p>;
}

<Suspense fallback={<p>Loading...</p>}>
  <UserName />
</Suspense>;
```

When `userIdAtom` changes, the async atom re-runs. Use `loadable` from `jotai/utils` if you'd rather get `{ state, data, error }` without suspending. For anything bigger than simple cases, `jotai-tanstack-query` adds caching.

## 171: How do you persist an atom in Jotai?

Use `atomWithStorage` from `jotai/utils`:

```ts
import { atomWithStorage } from "jotai/utils";

export const themeAtom = atomWithStorage<"light" | "dark">("theme", "light");
```

It reads and writes `localStorage` by default, and you can pass a custom storage like `sessionStorage`. It also syncs between browser tabs through the `storage` event.

## 172: How do you use MobX with React components?

You create a store class with `makeAutoObservable` and wrap components with `observer`:

```tsx
import { makeAutoObservable } from "mobx";
import { observer } from "mobx-react-lite";

class TimerStore {
  seconds = 0;
  constructor() {
    makeAutoObservable(this);
  }
  tick() {
    this.seconds += 1;
  }
  get minutes() {
    return Math.floor(this.seconds / 60);
  }
}

const timer = new TimerStore();

const TimerView = observer(() => (
  <button onClick={() => timer.tick()}>
    {timer.seconds}s ({timer.minutes}m)
  </button>
));
```

`makeAutoObservable` turns fields into observables, getters into computed values and methods into actions. `observer` makes the component re-render when the observables it read during render change.

## 173: How do you use an XState machine in a React component?

```tsx
import { createMachine } from "xstate";
import { useMachine } from "@xstate/react";

const toggleMachine = createMachine({
  id: "toggle",
  initial: "inactive",
  states: {
    inactive: { on: { TOGGLE: "active" } },
    active: { on: { TOGGLE: "inactive" } },
  },
});

function Toggle() {
  const [snapshot, send] = useMachine(toggleMachine);
  return (
    <button onClick={() => send({ type: "TOGGLE" })}>
      {snapshot.matches("active") ? "On" : "Off"}
    </button>
  );
}
```

In XState v5 the machine runs as an "actor". For real apps you use `setup()` to declare typed actions, guards and actors, and `fromPromise` for async work.

## 174: How do you decide between React Context, Zustand, Jotai and Redux Toolkit?

Rough guidelines:

- **Context + useState/useReducer**: for values that rarely change (theme, current user, locale) or state used by a small subtree. Every consumer re-renders when the value changes.
- **Zustand**: simple global client state with selective re-renders and little boilerplate. Good default for most apps.
- **Jotai**: many small, interdependent pieces of state, or state that should be scoped to a part of the tree.
- **Redux Toolkit**: big apps and teams that want strict patterns, DevTools time travel, middleware and RTK Query in one place.

And for data from the server, use a data fetching library (TanStack Query, RTK Query) rather than any of these.

## 175: What is the difference between staleTime and gcTime in TanStack Query?

- **staleTime** is how long data counts as fresh. While fresh, TanStack Query serves it from cache and won't refetch on mount or window focus. The default is `0`, so data is stale right away.
- **gcTime** is how long unused data stays in the cache after the last component using it unmounts. The default is 5 minutes. After that it is garbage collected.

So `staleTime` controls "when do we refetch", and `gcTime` controls "when do we forget". In v4 `gcTime` was called `cacheTime`.

```ts
const queryClient = new QueryClient({
  defaultOptions: { queries: { staleTime: 60_000 } },
});
```

## 176: How do you refresh data after a mutation in TanStack Query?

The usual way is to invalidate the related queries in `onSuccess` (or `onSettled`). Invalidated queries that are on screen refetch right away, and others refetch the next time they are used:

```ts
const queryClient = useQueryClient();

const updateTodo = useMutation({
  mutationFn: (todo: Todo) => api.updateTodo(todo),
  onSuccess: (updated) => {
    queryClient.setQueryData(["todo", updated.id], updated);
    return queryClient.invalidateQueries({ queryKey: ["todos"] });
  },
});
```

Query keys match by prefix, so invalidating `['todos']` also invalidates `['todos', { page: 2 }]`. Returning the promise keeps the mutation in pending state until the refetch finishes.

## 177: How do you do an optimistic update with TanStack Query?

The simplest way in v5 is to use the mutation's `variables` to show the pending item in the UI:

```tsx
const addTodo = useMutation({
  mutationFn: (text: string) => api.addTodo(text),
  onSettled: () => queryClient.invalidateQueries({ queryKey: ["todos"] }),
});

<ul>
  {todos.map((t) => (
    <li key={t.id}>{t.text}</li>
  ))}
  {addTodo.isPending && <li style={{ opacity: 0.5 }}>{addTodo.variables}</li>}
</ul>;
```

The other way is to update the cache directly in `onMutate`: cancel running queries, save the previous data, write the new data with `setQueryData`, roll back in `onError` and invalidate in `onSettled`. That is more code but updates every place that reads the cache.

## 178: How do you run a query only when some data is available?

Use the `enabled` option. The query waits until it becomes `true`:

```ts
const { data: user } = useQuery({
  queryKey: ["user", email],
  queryFn: () => getUserByEmail(email),
});

const { data: projects } = useQuery({
  queryKey: ["projects", user?.id],
  queryFn: () => getProjects(user!.id),
  enabled: !!user?.id,
});
```

These are called dependent queries. Note that they run one after another, so if you can get both pieces of data in one request or start them in parallel, it'll be faster.

## 179: How do you keep showing old data while the next page loads in TanStack Query?

Set `placeholderData` to `keepPreviousData`:

```ts
import { keepPreviousData, useQuery } from "@tanstack/react-query";

const { data, isPlaceholderData } = useQuery({
  queryKey: ["projects", page],
  queryFn: () => fetchProjects(page),
  placeholderData: keepPreviousData,
});
```

When `page` changes, the previous page stays on screen instead of a loading spinner, and `isPlaceholderData` tells you the shown data is from the old key. You can use it to disable the "Next" button until the new page arrives. In v4 this was the `keepPreviousData: true` option.

## 180: How do you build infinite scrolling with TanStack Query?

Use `useInfiniteQuery`:

```tsx
const { data, fetchNextPage, hasNextPage, isFetchingNextPage } =
  useInfiniteQuery({
    queryKey: ["feed"],
    queryFn: ({ pageParam }) =>
      fetch(`/api/feed?cursor=${pageParam}`).then((r) => r.json()),
    initialPageParam: 0,
    getNextPageParam: (lastPage) => lastPage.nextCursor ?? undefined,
  });

const items = data?.pages.flatMap((p) => p.items) ?? [];

<button
  onClick={() => fetchNextPage()}
  disabled={!hasNextPage || isFetchingNextPage}
>
  Load more
</button>;
```

Returning `undefined` from `getNextPageParam` means there are no more pages. Combine it with an intersection observer to load automatically when the user reaches the end.

## 181: What is useSuspenseQuery and how is it different from useQuery?

`useSuspenseQuery` suspends the component while data loads and throws errors to the nearest error boundary. Because of that, `data` is always defined in the component, so you don't need `if (isPending)` checks:

```tsx
function Profile() {
  const { data } = useSuspenseQuery({ queryKey: ["me"], queryFn: getMe });
  return <h1>{data.name}</h1>;
}

<ErrorBoundary fallback={<p>Error</p>}>
  <Suspense fallback={<p>Loading...</p>}>
    <Profile />
  </Suspense>
</ErrorBoundary>;
```

It doesn't support `enabled` or `placeholderData`. Watch out for waterfalls: two suspense queries in one component run one after the other, so use `useSuspenseQueries` or prefetch.

## 182: How do you prefetch data with TanStack Query?

Call `queryClient.prefetchQuery` before the user needs the data, for example on hover or in a route loader:

```tsx
function PostLink({ id }: { id: number }) {
  const queryClient = useQueryClient();
  return (
    <Link
      to={`/posts/${id}`}
      onMouseEnter={() =>
        queryClient.prefetchQuery({
          queryKey: ["post", id],
          queryFn: () => getPost(id),
          staleTime: 30_000,
        })
      }
    >
      Open
    </Link>
  );
}
```

When the post page mounts and calls `useQuery` with the same key, the data is already in the cache. `ensureQueryData` is a similar method that returns cached data if it exists and fetches only if needed.

## 183: What is the queryOptions helper in TanStack Query?

`queryOptions` lets you define a query's key and function together in one place and reuse them with full type safety:

```ts
import { queryOptions, useQuery } from "@tanstack/react-query";

export const postQuery = (id: number) =>
  queryOptions({
    queryKey: ["post", id],
    queryFn: () => getPost(id),
    staleTime: 60_000,
  });

useQuery(postQuery(5));
queryClient.prefetchQuery(postQuery(5));
const cached = queryClient.getQueryData(postQuery(5).queryKey);
```

Because the key is "tagged" with the data type, `getQueryData` and `setQueryData` know the type too. There is also `infiniteQueryOptions` and `mutationOptions`.

## 184: How do you use the TanStack Query Devtools?

Install `@tanstack/react-query-devtools` and render the component inside the provider:

```tsx
import { ReactQueryDevtools } from "@tanstack/react-query-devtools";

<QueryClientProvider client={queryClient}>
  <App />
  <ReactQueryDevtools initialIsOpen={false} />
</QueryClientProvider>;
```

It shows every query in the cache, its key, status (fresh, stale, fetching, inactive), data and observers. You can refetch, invalidate or reset queries by hand. It is left out of production builds automatically.

## 185: How does TanStack Query handle errors and retries?

By default, a failed query is retried 3 times with exponential backoff before going into the error state. Mutations are not retried by default. You can change this:

```ts
useQuery({
  queryKey: ["report"],
  queryFn: getReport,
  retry: (failureCount, error) =>
    error instanceof HttpError && error.status === 404
      ? false
      : failureCount < 2,
});
```

For global error handling, add an `onError` callback to the `QueryCache` or `MutationCache` when creating the `QueryClient`, for example to show a toast. The `throwOnError` option sends errors to the nearest error boundary instead.

## 186: How do you update and revalidate data with SWR?

SWR gives you a `mutate` function to update the cache and revalidate:

```tsx
import useSWR, { useSWRConfig } from "swr";

function Profile() {
  const { data, mutate } = useSWR("/api/user", fetcher);

  async function rename(name: string) {
    await mutate(updateUserName(name), {
      optimisticData: { ...data, name },
      rollbackOnError: true,
      revalidate: true,
    });
  }
  // ...
}
```

The global `mutate` from `useSWRConfig` lets you update any key from anywhere. SWR also has `useSWRMutation` for remote mutations, and options like `revalidateOnFocus`, `refreshInterval` and `dedupingInterval`.

## 187: How do you add an auth token to every Axios request?

Use a request interceptor on an Axios instance:

```ts
import axios from "axios";

export const api = axios.create({ baseURL: "/api", timeout: 10_000 });

api.interceptors.request.use((config) => {
  const token = useAuthStore.getState().token;
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

api.interceptors.response.use(
  (res) => res,
  (error) => {
    if (error.response?.status === 401) useAuthStore.getState().logout();
    return Promise.reject(error);
  },
);
```

Use your own instance instead of changing the global `axios` defaults, so third-party code that uses Axios isn't affected.

## 188: How do you cancel an Axios or fetch request in React?

Both support `AbortController`. Pass the signal to the request and abort it in the effect cleanup:

```tsx
useEffect(() => {
  const controller = new AbortController();
  api
    .get("/search", { params: { q: query }, signal: controller.signal })
    .then((res) => setResults(res.data))
    .catch((err) => {
      if (!axios.isCancel(err)) setError(err);
    });
  return () => controller.abort();
}, [query]);
```

This avoids race conditions where an old, slow response overwrites a newer one. TanStack Query passes a `signal` into `queryFn` too, so you only need to forward it to `fetch` or Axios.

## 189: How does the Apollo Client cache work at a basic level?

Apollo uses `InMemoryCache`, which normalizes query results. Each object with a `__typename` and `id` (or `_id`) is stored once under a key like `User:42`, and queries point to it.

```ts
import { ApolloClient, HttpLink, InMemoryCache } from "@apollo/client";

const client = new ApolloClient({
  link: new HttpLink({ uri: "/graphql" }),
  cache: new InMemoryCache(),
});
```

So if a mutation returns `User:42` with a new name, every query that shows that user updates automatically. For objects without an `id`, you set `keyFields` in `typePolicies`, or they are stored inside their parent.

## 190: How do you update the Apollo cache after a mutation that adds an item?

When a mutation updates an existing object with its `id`, Apollo updates the cache by itself. When it creates a new item, Apollo doesn't know which lists should include it. You can refetch queries or update the cache by hand:

```ts
const [addTodo] = useMutation(ADD_TODO, {
  update(cache, { data }) {
    cache.modify({
      fields: {
        todos(existingRefs = [], { toReference }) {
          return [...existingRefs, toReference(data.addTodo)];
        },
      },
    });
  },
});
```

`refetchQueries: ['GetTodos']` is simpler but costs an extra request.

## 191: How does tRPC work with TanStack Query in React?

tRPC has an integration where the client gives you typed query and mutation options for TanStack Query:

```tsx
import { useQuery, useMutation } from "@tanstack/react-query";
import { useTRPC } from "./trpc";

function Greeting() {
  const trpc = useTRPC();
  const hello = useQuery(trpc.greeting.queryOptions({ name: "Ana" }));
  const create = useMutation(trpc.post.create.mutationOptions());
  return <p>{hello.data?.text}</p>;
}
```

The input and output types come straight from the server router, so renaming a field on the server shows type errors in the client right away. Older code uses the classic `trpc.greeting.useQuery()` style hooks, which still exist.

## 192: How do you use Zod with React Hook Form?

Use `zodResolver` and infer the form type from the schema:

```tsx
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";

const schema = z
  .object({
    email: z.email("Enter a valid email"),
    password: z.string().min(8, "At least 8 characters"),
    confirm: z.string(),
  })
  .refine((v) => v.password === v.confirm, {
    message: "Passwords do not match",
    path: ["confirm"],
  });

type FormValues = z.infer<typeof schema>;

function SignUp() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<FormValues>({ resolver: zodResolver(schema) });
  return (
    <form onSubmit={handleSubmit((v) => console.log(v))}>
      <input {...register("email")} />
      <p>{errors.email?.message}</p>
      <input type="password" {...register("password")} />
      <input type="password" {...register("confirm")} />
      <p>{errors.confirm?.message}</p>
      <button>Sign up</button>
    </form>
  );
}
```

You can reuse the same schema on the server to validate the request body.

## 193: How do you use a controlled UI component like MUI's TextField or Select with React Hook Form?

Use the `Controller` component (or the `useController` hook). It connects RHF to components that need `value` and `onChange` instead of a ref:

```tsx
import { Controller, useForm } from "react-hook-form";
import { MenuItem, TextField } from "@mui/material";

function RoleForm() {
  const { control, handleSubmit } = useForm({
    defaultValues: { role: "viewer" },
  });
  return (
    <form onSubmit={handleSubmit(console.log)}>
      <Controller
        name="role"
        control={control}
        render={({ field, fieldState }) => (
          <TextField select label="Role" {...field} error={!!fieldState.error}>
            <MenuItem value="viewer">Viewer</MenuItem>
            <MenuItem value="admin">Admin</MenuItem>
          </TextField>
        )}
      />
    </form>
  );
}
```

Always set `defaultValues`, otherwise the controlled component starts as `undefined` and React warns about switching from uncontrolled to controlled.

## 194: How do you handle a dynamic list of fields in React Hook Form?

Use `useFieldArray`:

```tsx
import { useFieldArray, useForm } from "react-hook-form";

type Values = { phones: { number: string }[] };

function Phones() {
  const { control, register } = useForm<Values>({
    defaultValues: { phones: [{ number: "" }] },
  });
  const { fields, append, remove } = useFieldArray({ control, name: "phones" });

  return (
    <>
      {fields.map((field, index) => (
        <div key={field.id}>
          <input {...register(`phones.${index}.number`)} />
          <button type="button" onClick={() => remove(index)}>
            Remove
          </button>
        </div>
      ))}
      <button type="button" onClick={() => append({ number: "" })}>
        Add phone
      </button>
    </>
  );
}
```

Use `field.id` as the key, not the index, so React keeps inputs in the right place when items are removed or moved.

## 195: What is the difference between watch and useWatch in React Hook Form?

Both let you read field values while the user types:

- `watch('field')` from `useForm` re-renders the component that called `useForm`, which is often the whole form.
- `useWatch({ control, name: 'field' })` re-renders only the component that uses it.

So for things like showing a live preview or a conditional field deep in the form, put `useWatch` in a small child component to keep the rest of the form from re-rendering. `getValues()` reads values without subscribing at all, which is good inside event handlers.

## 196: How do you show server-side errors in React Hook Form?

Use `setError` after the submit fails:

```tsx
const {
  register,
  handleSubmit,
  setError,
  formState: { errors },
} = useForm<{ username: string }>();

const onSubmit = handleSubmit(async (values) => {
  const res = await fetch("/api/register", {
    method: "POST",
    body: JSON.stringify(values),
  });
  if (res.status === 409) {
    setError("username", { type: "server", message: "This username is taken" });
    return;
  }
  if (!res.ok) {
    setError("root.server", { message: "Something went wrong, try again" });
  }
});
```

`root.*` errors are for messages that don't belong to one field. They are cleared on the next submit.

## 197: Why is React Hook Form fast compared to Formik?

React Hook Form keeps values in the DOM inputs (through refs) and in an internal store, not in React state. Typing in a field doesn't re-render the form component. It only re-renders when something you subscribed to changes, for example `errors` or `isDirty`.

`formState` is a proxy: RHF tracks which properties you read and only triggers re-renders for those. Formik stores values in React state, so every keystroke re-renders the whole form and its fields unless you add a lot of memoization.

## 198: What is the difference between parse and safeParse in Zod?

- `schema.parse(data)` returns the typed data or throws a `ZodError` if validation fails.
- `schema.safeParse(data)` never throws. It returns `{ success: true, data }` or `{ success: false, error }`.

```ts
const result = UserSchema.safeParse(input);
if (!result.success) {
  console.log(z.flattenError(result.error).fieldErrors);
} else {
  saveUser(result.data);
}
```

Use `safeParse` when invalid data is expected (user input) and `parse` when invalid data is a bug (config, trusted API). `parseAsync` and `safeParseAsync` are needed when the schema has async refinements.

## 199: How do you validate API responses with Zod?

Parse the JSON with a schema at the boundary, so the rest of your code can trust the types:

```ts
const ProductSchema = z.object({
  id: z.number(),
  name: z.string(),
  price: z.number(),
  tags: z.array(z.string()).default([]),
});

export async function getProduct(id: number) {
  const res = await fetch(`/api/products/${id}`);
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return ProductSchema.parse(await res.json());
}
```

If the backend changes the shape, you get a clear error at the fetch, not a random `undefined` crash deep in the UI. For big responses that you fully control, some teams skip it for speed, so it is a trade-off.

## 200: How do you choose between React Hook Form, TanStack Form and Formik for a new project?

- **React Hook Form**: the default choice. Fast, huge community, works with every UI kit and schema library.
- **TanStack Form**: if you want very strong typing for nested fields, framework-agnostic logic or fine-grained reactivity. Smaller community, newer.
- **Formik**: only for existing projects already using it. It gets few updates.

For very simple forms, React 19's form actions with `useActionState` and native validation may be enough with no library at all.

## 201: How do you customize the theme in Material UI?

Create a theme with `createTheme` and pass it to `ThemeProvider`:

```tsx
import { createTheme, ThemeProvider, CssBaseline } from "@mui/material";

const theme = createTheme({
  palette: {
    primary: { main: "#0f766e" },
    secondary: { main: "#f59e0b" },
  },
  typography: { fontFamily: "Inter, sans-serif" },
  shape: { borderRadius: 8 },
  components: {
    MuiButton: {
      defaultProps: { disableElevation: true },
      styleOverrides: { root: { textTransform: "none" } },
    },
  },
});

export function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      {/* ... */}
    </ThemeProvider>
  );
}
```

`components` lets you change default props and styles for every instance of a component. `CssBaseline` adds a CSS reset and the theme's background color.

## 202: What is the difference between the sx prop and styled() in Material UI?

- `sx` is for one-off styles on a single element. It has access to the theme with shortcuts like `p: 2` (spacing), `color: 'primary.main'` and responsive values (`{ xs: 1, md: 3 }`).
- `styled()` creates a reusable styled component, good when the same styles are used in many places.

```tsx
import { Box, styled } from "@mui/material";

const Card = styled("div")(({ theme }) => ({
  padding: theme.spacing(2),
  borderRadius: theme.shape.borderRadius,
}));

<Box sx={{ p: 2, display: "flex", gap: 1, bgcolor: "background.paper" }} />;
```

Both run through Emotion at runtime. Avoid putting large `sx` objects on items in long lists because each one creates styles.

## 203: How do you support dark mode in Material UI?

Define both color schemes in the theme and turn on CSS variables:

```tsx
import {
  createTheme,
  ThemeProvider,
  useColorScheme,
} from "@mui/material/styles";

const theme = createTheme({
  cssVariables: { colorSchemeSelector: "class" },
  colorSchemes: { light: true, dark: true },
});

function ModeToggle() {
  const { mode, setMode } = useColorScheme();
  return (
    <button onClick={() => setMode(mode === "dark" ? "light" : "dark")}>
      Toggle
    </button>
  );
}

<ThemeProvider theme={theme}>
  <ModeToggle />
</ThemeProvider>;
```

With CSS variables, switching modes only swaps variables instead of re-rendering everything. For SSR, MUI provides an `InitColorSchemeScript` that sets the mode before the page paints, which avoids a flash of the wrong theme.

## 204: How do you add and customize shadcn/ui components?

First run `npx shadcn@latest init`, which sets up `components.json`, the `cn` helper and the CSS variables. Then add the components you need:

```bash
npx shadcn@latest add button dialog form
```

The files appear in `components/ui`. To customize, you just edit them. For example, add a new variant to the button's `cva` config:

```ts
variant: {
  default: 'bg-primary text-primary-foreground hover:bg-primary/90',
  success: 'bg-green-600 text-white hover:bg-green-700',
},
```

The CLI can also add blocks, components from other registries, and show a diff when the upstream component changes.

## 205: How does theming work in shadcn/ui?

Colors are CSS variables defined in your global CSS, like `--background`, `--foreground`, `--primary`, `--muted` and `--border`, with a second set under the `.dark` class. Tailwind maps them to utilities like `bg-primary` and `text-muted-foreground`.

```css
:root {
  --primary: oklch(0.55 0.2 260);
  --primary-foreground: oklch(0.98 0 0);
}
.dark {
  --primary: oklch(0.7 0.15 260);
}
```

To change the brand, you edit these variables, and every component updates. Dark mode is usually handled with a library like `next-themes` that toggles the `.dark` class.

## 206: How do you build a modal with Radix UI Dialog?

```tsx
import * as Dialog from "@radix-ui/react-dialog";

function DeleteDialog({ onConfirm }: { onConfirm: () => void }) {
  return (
    <Dialog.Root>
      <Dialog.Trigger asChild>
        <button>Delete</button>
      </Dialog.Trigger>
      <Dialog.Portal>
        <Dialog.Overlay className="fixed inset-0 bg-black/50" />
        <Dialog.Content className="fixed left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 rounded bg-white p-6">
          <Dialog.Title>Delete item?</Dialog.Title>
          <Dialog.Description>This can't be undone.</Dialog.Description>
          <Dialog.Close asChild>
            <button onClick={onConfirm}>Yes, delete</button>
          </Dialog.Close>
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
}
```

Radix takes care of focus trapping, closing on Escape, returning focus to the trigger, `aria-*` attributes and locking page scroll. The Title is required for accessibility.

## 207: What does the asChild prop do in Radix UI?

`asChild` tells a Radix component not to render its own DOM element, but to pass its props and behavior to its single child. It uses a `Slot` component inside that merges props, event handlers and refs.

```tsx
<Tooltip.Trigger asChild>
  <a href="/docs">Docs</a>
</Tooltip.Trigger>
```

Without `asChild`, you'd get a `<button>` wrapping your `<a>`. The child must accept props and forward a ref (in React 19 `ref` is a normal prop, which makes this easier). Base UI solves the same problem with a `render` prop instead.

## 208: How do you customize components in Chakra UI v3?

Chakra v3 uses a system created with `createSystem`, plus "recipes" for component variants:

```tsx
import {
  ChakraProvider,
  createSystem,
  defaultConfig,
  defineConfig,
} from "@chakra-ui/react";

const config = defineConfig({
  theme: {
    tokens: {
      colors: { brand: { 500: { value: "#0f766e" } } },
    },
  },
});

const system = createSystem(defaultConfig, config);

<ChakraProvider value={system}>{/* app */}</ChakraProvider>;
```

v3 also uses "snippets": you run `npx @chakra-ui/cli snippet add` to copy ready-made compositions (like a styled Tooltip or Dialog) into your project, a bit like shadcn/ui. Many v2 props were renamed, so upgrading is real work.

## 209: How do you handle forms with Mantine?

Mantine has its own form library, `@mantine/form`:

```tsx
import { useForm } from "@mantine/form";
import { TextInput, Button } from "@mantine/core";

function Signup() {
  const form = useForm({
    mode: "uncontrolled",
    initialValues: { email: "" },
    validate: { email: (v) => (/^\S+@\S+$/.test(v) ? null : "Invalid email") },
  });

  return (
    <form onSubmit={form.onSubmit((values) => console.log(values))}>
      <TextInput
        label="Email"
        key={form.key("email")}
        {...form.getInputProps("email")}
      />
      <Button type="submit">Submit</Button>
    </form>
  );
}
```

`getInputProps` wires up value, onChange and error. You can also use React Hook Form with Mantine inputs, and many teams do.

## 210: How do you change the theme in Ant Design?

Use `ConfigProvider` with design tokens:

```tsx
import { ConfigProvider, theme, Button } from "antd";

<ConfigProvider
  theme={{
    algorithm: theme.darkAlgorithm,
    token: { colorPrimary: "#0f766e", borderRadius: 6 },
    components: { Button: { controlHeight: 40 } },
  }}
>
  <Button type="primary">Save</Button>
</ConfigProvider>;
```

`token` sets global values, `components` changes tokens for specific components, and `algorithm` switches between default, dark and compact. `ConfigProvider` can be nested to theme part of a page differently. It also sets the locale for built-in texts.

## 211: When would you use React Aria hooks instead of React Aria Components?

React Aria Components are ready-made, unstyled components with a simple API. They are the easiest way to start, and you style them with classes or render props like `className={({ isFocused }) => ...}`.

The hooks (`useButton`, `useListBox`, `useComboBox`) give you lower-level control: you build the DOM structure yourself and spread the props they return. You use them when your markup doesn't fit the components, for example when you build a design system with unusual structure or wrap existing components. Most teams start with the components and use hooks only for special cases.

## 212: How do you set up Tailwind CSS v4 in a Vite React project?

```bash
npm install tailwindcss @tailwindcss/vite
```

```ts
// vite.config.ts
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  plugins: [react(), tailwindcss()],
});
```

```css
/* src/index.css */
@import "tailwindcss";

@theme {
  --color-brand: oklch(0.6 0.15 180);
  --font-display: "Inter", sans-serif;
}
```

v4 finds your source files automatically, so you don't need the `content` array. Theme values go in `@theme` and become both CSS variables and utilities like `bg-brand`.

## 213: How do you build a reusable component with variants using cva and Tailwind?

```tsx
import { cva, type VariantProps } from "class-variance-authority";
import { cn } from "@/lib/utils";

const badge = cva(
  "inline-flex items-center rounded-full px-2 text-xs font-medium",
  {
    variants: {
      tone: {
        neutral: "bg-gray-100 text-gray-800",
        success: "bg-green-100 text-green-800",
        danger: "bg-red-100 text-red-800",
      },
    },
    defaultVariants: { tone: "neutral" },
  },
);

type BadgeProps = React.ComponentProps<"span"> & VariantProps<typeof badge>;

export function Badge({ className, tone, ...props }: BadgeProps) {
  return <span className={cn(badge({ tone }), className)} {...props} />;
}
```

`VariantProps` gives you the prop types from the config, and `cn` lets callers override classes safely.

## 214: How do you use theming and props in styled-components?

Wrap the app in `ThemeProvider` and read the theme in styles. Use `$`-prefixed "transient" props for values that should not be passed to the DOM:

```tsx
import styled, { ThemeProvider } from "styled-components";

const theme = { colors: { primary: "#0f766e" } };

const Button = styled.button<{ $outline?: boolean }>`
  color: ${({ theme, $outline }) => ($outline ? theme.colors.primary : "white")};
  background: ${({ theme, $outline }) => ($outline ? "transparent" : theme.colors.primary)};
`;

<ThemeProvider theme={theme}>
  <Button $outline>Cancel</Button>
</ThemeProvider>;
```

Without the `$` prefix, `outline` would end up as an attribute on the `<button>` and React would warn about it.

## 215: How do you type CSS Modules and share styles between them?

Vite and Next.js give you a generic type, so `styles.card` is a `string` but not checked against the CSS file. For strict checking, you can use a plugin like `typescript-plugin-css-modules` (editor only) or generate `.d.ts` files.

To share styles, use `composes`:

```css
/* Button.module.css */
.base {
  padding: 8px 16px;
  border-radius: 4px;
}
.primary {
  composes: base;
  background: teal;
  color: white;
}
.danger {
  composes: base from "./shared.module.css";
  background: crimson;
}
```

`composes` adds both class names to the element, so the CSS isn't duplicated.

## 216: What are the trade-offs between runtime and zero-runtime CSS-in-JS?

**Runtime** (styled-components, Emotion): styles are created in the browser while rendering. You can use any prop or state value directly in styles. The cost is extra JavaScript, slower renders, and problems with Server Components and streaming SSR.

**Zero-runtime** (vanilla-extract, Panda, StyleX, Pigment CSS): styles are extracted to static CSS at build time. No runtime cost and they work with Server Components, but dynamic values must go through CSS variables or predefined variants, and you need a build plugin.

Plain CSS Modules and Tailwind are also zero-runtime and are the most common choices for new projects.

## 217: How do you animate a component when it is removed with Motion?

Wrap it in `AnimatePresence` and give the `motion` element an `exit` prop:

```tsx
import { AnimatePresence, motion } from "motion/react";

function Toast({ show, message }: { show: boolean; message: string }) {
  return (
    <AnimatePresence>
      {show && (
        <motion.div
          key="toast"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: 20 }}
        >
          {message}
        </motion.div>
      )}
    </AnimatePresence>
  );
}
```

React normally removes elements right away. `AnimatePresence` keeps them in the DOM until the exit animation finishes. Direct children need a stable `key`.

## 218: What are layout animations in Motion?

Adding the `layout` prop makes an element animate smoothly when its size or position changes because of a re-render, for example when a list is reordered or a card expands:

```tsx
<motion.div
  layout
  onClick={() => setOpen(!open)}
  className={open ? "card open" : "card"}
/>
```

Motion measures the element before and after the change and animates the difference using transforms, which is fast. With `layoutId`, two different elements can animate from one to the other, like a thumbnail growing into a full-screen image.

## 219: How do you use variants in Motion?

Variants are named animation states. They help when a parent controls the animation of many children:

```tsx
const list = {
  hidden: { opacity: 0 },
  visible: { opacity: 1, transition: { staggerChildren: 0.05 } },
};
const item = {
  hidden: { opacity: 0, x: -10 },
  visible: { opacity: 1, x: 0 },
};

<motion.ul variants={list} initial="hidden" animate="visible">
  {items.map((i) => (
    <motion.li key={i.id} variants={item}>
      {i.name}
    </motion.li>
  ))}
</motion.ul>;
```

Children with variants inherit the parent's current state name, so you only set `initial` and `animate` on the parent. `staggerChildren` starts each child a bit after the previous one.

## 220: How do you respect the user's reduced motion setting with Motion?

Use the `useReducedMotion` hook, or set it globally with `MotionConfig`:

```tsx
import { MotionConfig, useReducedMotion, motion } from "motion/react";

<MotionConfig reducedMotion="user">
  <App />
</MotionConfig>;

function Hero() {
  const reduce = useReducedMotion();
  return <motion.div animate={{ x: reduce ? 0 : 100, opacity: 1 }} />;
}
```

With `reducedMotion="user"`, Motion turns off transform and layout animations for people who have "reduce motion" on in their OS, but keeps things like opacity. This matters for people who get dizzy from motion.

## 221: How do you make a custom tooltip in Recharts?

Pass your own component to the `content` prop of `Tooltip`:

```tsx
import { Tooltip, type TooltipProps } from "recharts";

function SalesTooltip({
  active,
  payload,
  label,
}: TooltipProps<number, string>) {
  if (!active || !payload?.length) return null;
  return (
    <div className="rounded border bg-white p-2 shadow">
      <p>{label}</p>
      <p>Sales: ${payload[0].value?.toLocaleString()}</p>
    </div>
  );
}

<Tooltip content={<SalesTooltip />} />;
```

The same idea works for custom ticks, labels, legends and dots. The exact prop types changed a bit in Recharts 3, so check the types for your version.

## 222: How do you pick a chart library for a React project?

Questions to ask:

- **How much data?** SVG libraries (Recharts, Nivo SVG, Victory) are fine up to a few thousand points. For more, use Canvas or WebGL (ECharts, Chart.js, uPlot, Nivo canvas).
- **How custom?** For unusual charts, visx or plain D3 gives full control. For standard dashboards, Recharts or MUI X Charts is faster to build.
- **Design system**: if you use MUI or Mantine, their chart packages match your look.
- **SSR and bundle size**: some libraries are large or need the browser.
- **License**: Highcharts and some others need a paid license for commercial use.

## 223: How do you set up sorting and filtering with TanStack Table?

```tsx
import {
  createColumnHelper,
  flexRender,
  getCoreRowModel,
  getFilteredRowModel,
  getSortedRowModel,
  useReactTable,
  type SortingState,
} from "@tanstack/react-table";
import { useState } from "react";

type User = { name: string; age: number };
const col = createColumnHelper<User>();
const columns = [
  col.accessor("name", { header: "Name" }),
  col.accessor("age", { header: "Age" }),
];

function UsersTable({ data }: { data: User[] }) {
  const [sorting, setSorting] = useState<SortingState>([]);
  const [globalFilter, setGlobalFilter] = useState("");

  const table = useReactTable({
    data,
    columns,
    state: { sorting, globalFilter },
    onSortingChange: setSorting,
    onGlobalFilterChange: setGlobalFilter,
    getCoreRowModel: getCoreRowModel(),
    getSortedRowModel: getSortedRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
  });

  return (
    <>
      <input
        value={globalFilter}
        onChange={(e) => setGlobalFilter(e.target.value)}
        placeholder="Search"
      />
      <table>
        <thead>
          {table.getHeaderGroups().map((hg) => (
            <tr key={hg.id}>
              {hg.headers.map((h) => (
                <th key={h.id} onClick={h.column.getToggleSortingHandler()}>
                  {flexRender(h.column.columnDef.header, h.getContext())}
                </th>
              ))}
            </tr>
          ))}
        </thead>
        <tbody>
          {table.getRowModel().rows.map((row) => (
            <tr key={row.id}>
              {row.getVisibleCells().map((cell) => (
                <td key={cell.id}>
                  {flexRender(cell.column.columnDef.cell, cell.getContext())}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </>
  );
}
```

Keep `data` and `columns` stable (defined outside the component or memoized), or the table recalculates on every render.

## 224: How do you do server-side pagination with TanStack Table?

Tell the table that pagination is done outside by setting `manualPagination` and giving it the row count:

```tsx
const [pagination, setPagination] = useState({ pageIndex: 0, pageSize: 20 });

const { data } = useQuery({
  queryKey: ["orders", pagination],
  queryFn: () => fetchOrders(pagination.pageIndex, pagination.pageSize),
  placeholderData: keepPreviousData,
});

const table = useReactTable({
  data: data?.rows ?? [],
  columns,
  rowCount: data?.total ?? 0,
  state: { pagination },
  onPaginationChange: setPagination,
  manualPagination: true,
  getCoreRowModel: getCoreRowModel(),
});
```

`manualSorting` and `manualFiltering` work the same way. The table just keeps the state, and your API does the work.

## 225: How do you render a long list with TanStack Virtual?

```tsx
import { useVirtualizer } from "@tanstack/react-virtual";
import { useRef } from "react";

function BigList({ items }: { items: string[] }) {
  const parentRef = useRef<HTMLDivElement>(null);
  const virtualizer = useVirtualizer({
    count: items.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 36,
    overscan: 5,
  });

  return (
    <div ref={parentRef} style={{ height: 400, overflow: "auto" }}>
      <div style={{ height: virtualizer.getTotalSize(), position: "relative" }}>
        {virtualizer.getVirtualItems().map((v) => (
          <div
            key={v.key}
            style={{
              position: "absolute",
              top: 0,
              left: 0,
              width: "100%",
              transform: `translateY(${v.start}px)`,
              height: v.size,
            }}
          >
            {items[v.index]}
          </div>
        ))}
      </div>
    </div>
  );
}
```

For rows with different heights, add `ref={virtualizer.measureElement}` and `data-index={v.index}` to each row so it measures them.

## 226: How do you set up AG Grid in a React app?

```tsx
import { AgGridReact } from "ag-grid-react";
import {
  AllCommunityModule,
  ModuleRegistry,
  type ColDef,
} from "ag-grid-community";

ModuleRegistry.registerModules([AllCommunityModule]);

type Car = { make: string; model: string; price: number };

const columnDefs: ColDef<Car>[] = [
  { field: "make", filter: true },
  { field: "model" },
  {
    field: "price",
    sortable: true,
    valueFormatter: (p) => `$${p.value.toLocaleString()}`,
  },
];

function CarsGrid({ rows }: { rows: Car[] }) {
  return (
    <div style={{ height: 500 }}>
      <AgGridReact rowData={rows} columnDefs={columnDefs} />
    </div>
  );
}
```

Since v33, AG Grid uses modules (register only what you use, to keep the bundle smaller) and a JavaScript theming API instead of importing CSS theme files. The grid needs a container with a height.

## 227: How do you lazy load translation files with react-i18next?

Use a backend plugin like `i18next-http-backend` to load JSON files on demand, and split translations into namespaces:

```ts
import i18n from "i18next";
import HttpBackend from "i18next-http-backend";
import LanguageDetector from "i18next-browser-languagedetector";
import { initReactI18next } from "react-i18next";

i18n
  .use(HttpBackend)
  .use(LanguageDetector)
  .use(initReactI18next)
  .init({
    fallbackLng: "en",
    ns: ["common"],
    defaultNS: "common",
    backend: { loadPath: "/locales/{{lng}}/{{ns}}.json" },
  });
```

Then a page can ask for its own namespace with `useTranslation('settings')`. By default the hook suspends while loading, so put a `Suspense` boundary around the app.

## 228: How do plurals and interpolation work in i18next?

Interpolation uses `{{name}}`. For plurals, you add keys with suffixes based on the language's plural rules (from `Intl.PluralRules`), and pass `count`:

```json
{
  "inbox_one": "You have {{count}} message",
  "inbox_other": "You have {{count}} messages"
}
```

```tsx
t("inbox", { count: 5 });
```

Languages like Polish or Arabic have more plural forms (`_few`, `_many` and so on), and i18next picks the right key automatically. Values are escaped by default to prevent XSS.

## 229: What is the Trans component in react-i18next used for?

`Trans` is for translations that contain JSX, like links or bold text, without splitting the sentence into pieces:

```tsx
import { Trans } from "react-i18next";

// "agree": "I agree to the <link>terms of service</link>"
<Trans i18nKey="agree" components={{ link: <a href="/terms" /> }} />;
```

Translators see the whole sentence and can move the link to where it makes sense in their language. Use `t` for plain strings and `Trans` only when you need markup inside the text.

## 230: How do you format numbers, dates and currency with react-intl?

Use the `useIntl` hook or the `Formatted*` components. They use the browser's `Intl` APIs with the current locale:

```tsx
import { useIntl, FormattedNumber, FormattedDate } from "react-intl";

function Price({ value, date }: { value: number; date: Date }) {
  const intl = useIntl();
  return (
    <>
      <FormattedNumber value={value} style="currency" currency="EUR" />
      <FormattedDate value={date} dateStyle="medium" />
      <span title={intl.formatRelativeTime(-2, "day")} />
    </>
  );
}
```

The same number shows as `€1,234.50` in English and `1.234,50 €` in German without any extra code.

## 231: How do you work with time zones in date-fns?

date-fns v4 has first-class time zone support through the `@date-fns/tz` package. You create a date in a specific zone with `TZDate`, and the date-fns functions respect it:

```ts
import { TZDate } from "@date-fns/tz";
import { addDays, format } from "date-fns";

const meeting = new TZDate(2026, 2, 28, 9, 0, "America/New_York");
format(addDays(meeting, 1), "yyyy-MM-dd HH:mm zzz");
```

Many functions also take an `in` option to choose the time zone context. Before v4, people used the separate `date-fns-tz` package.

## 232: How do Day.js plugins work?

Day.js keeps the core small and adds features through plugins you register once:

```ts
import dayjs from "dayjs";
import relativeTime from "dayjs/plugin/relativeTime";
import utc from "dayjs/plugin/utc";
import timezone from "dayjs/plugin/timezone";
import "dayjs/locale/de";

dayjs.extend(relativeTime);
dayjs.extend(utc);
dayjs.extend(timezone);

dayjs().subtract(3, "hour").fromNow();
dayjs.tz("2026-03-28 09:00", "Europe/Berlin").locale("de").format("LLLL");
```

Plugins change the global `dayjs`, so register them in one setup file that runs before the app.

## 233: How do you build a sortable list with dnd-kit?

```tsx
import { DndContext, closestCenter, type DragEndEvent } from "@dnd-kit/core";
import {
  SortableContext,
  arrayMove,
  useSortable,
  verticalListSortingStrategy,
} from "@dnd-kit/sortable";
import { CSS } from "@dnd-kit/utilities";
import { useState } from "react";

function Item({ id }: { id: string }) {
  const { attributes, listeners, setNodeRef, transform, transition } =
    useSortable({ id });
  return (
    <li
      ref={setNodeRef}
      style={{ transform: CSS.Transform.toString(transform), transition }}
      {...attributes}
      {...listeners}
    >
      {id}
    </li>
  );
}

function SortableList() {
  const [items, setItems] = useState(["a", "b", "c"]);

  function onDragEnd({ active, over }: DragEndEvent) {
    if (over && active.id !== over.id) {
      setItems((prev) =>
        arrayMove(
          prev,
          prev.indexOf(String(active.id)),
          prev.indexOf(String(over.id)),
        ),
      );
    }
  }

  return (
    <DndContext collisionDetection={closestCenter} onDragEnd={onDragEnd}>
      <SortableContext items={items} strategy={verticalListSortingStrategy}>
        <ul>
          {items.map((id) => (
            <Item key={id} id={id} />
          ))}
        </ul>
      </SortableContext>
    </DndContext>
  );
}
```

Add `useSensors` with `KeyboardSensor` and `sortableKeyboardCoordinates` to support keyboard users. dnd-kit is also working on a newer API (`@dnd-kit/react`), so check which one your project uses.

## 234: How do you validate files with react-dropzone?

Use `accept`, `maxSize`, `maxFiles` and, if needed, a custom `validator`. Rejected files come back in `fileRejections` with error codes:

```tsx
const { getRootProps, getInputProps, fileRejections } = useDropzone({
  accept: { "image/png": [".png"], "image/jpeg": [".jpg", ".jpeg"] },
  maxSize: 5 * 1024 * 1024,
  maxFiles: 3,
  validator: (file) =>
    file.name.length > 100
      ? { code: "name-too-long", message: "File name is too long" }
      : null,
  onDropAccepted: (files) => upload(files),
});
```

This only checks in the browser. The server must also check file type (by content, not extension), size and count, because the client can be bypassed.

## 235: How do you load options from an API in react-select?

Use the `AsyncSelect` component with a `loadOptions` function that returns a promise:

```tsx
import AsyncSelect from "react-select/async";

type Option = { value: string; label: string };

async function loadCities(input: string): Promise<Option[]> {
  const res = await fetch(`/api/cities?q=${encodeURIComponent(input)}`);
  const cities: { id: string; name: string }[] = await res.json();
  return cities.map((c) => ({ value: c.id, label: c.name }));
}

<AsyncSelect<Option> cacheOptions defaultOptions loadOptions={loadCities} />;
```

`cacheOptions` caches results per search string. You should debounce the input yourself if the API is expensive.

## 236: How do you show toasts for an async action with Sonner?

`toast.promise` shows loading, success and error states for one promise:

```tsx
import { toast } from "sonner";

function SaveButton() {
  return (
    <button
      onClick={() =>
        toast.promise(saveSettings(), {
          loading: "Saving...",
          success: "Settings saved",
          error: (err) => `Could not save: ${err.message}`,
        })
      }
    >
      Save
    </button>
  );
}
```

You can also use `toast.custom` for your own markup, `action` for an "Undo" button, and `id` to update an existing toast instead of adding a new one.

## 237: How do you reset an error boundary and catch async errors with react-error-boundary?

Use `resetKeys` to reset automatically when some value changes, and `useErrorBoundary` to send errors from event handlers or promises to the boundary:

```tsx
import { ErrorBoundary, useErrorBoundary } from "react-error-boundary";

function Report({ id }: { id: string }) {
  const { showBoundary } = useErrorBoundary();
  const exportCsv = () => api.export(id).catch(showBoundary);
  return <button onClick={exportCsv}>Export</button>;
}

<ErrorBoundary
  FallbackComponent={Fallback}
  resetKeys={[reportId]}
  onReset={() => queryClient.resetQueries()}
>
  <Report id={reportId} />
</ErrorBoundary>;
```

React error boundaries don't catch errors in event handlers or async code on their own, so `showBoundary` fills that gap.

## 238: How do you use error boundaries together with TanStack Query?

When queries throw to an error boundary (with `useSuspenseQuery` or `throwOnError`), you need to reset the failed queries when the user clicks "Try again". `QueryErrorResetBoundary` does that:

```tsx
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
      <Suspense fallback={<Spinner />}>
        <Orders />
      </Suspense>
    </ErrorBoundary>
  )}
</QueryErrorResetBoundary>;
```

Without the reset, the query would stay in error state and the boundary would show the error again right away.

## 239: How do you set page titles and meta tags in a React 19 app without a library?

Render the tags directly in your component. React 19 hoists them to `<head>`:

```tsx
function ProductPage({
  product,
}: {
  product: { name: string; summary: string };
}) {
  return (
    <>
      <title>{`${product.name} | My Shop`}</title>
      <meta name="description" content={product.summary} />
      <link rel="canonical" href={`https://example.com/p/${product.name}`} />
      <h1>{product.name}</h1>
    </>
  );
}
```

Pass the title as a single string (a template literal), not mixed text and expressions, otherwise React warns. For more advanced needs, like de-duplicating tags across nested routes, you can still use `react-helmet-async` or your framework's metadata API.

## 240: How do you position a tooltip with Floating UI?

```tsx
import {
  useFloating,
  offset,
  flip,
  shift,
  autoUpdate,
  useHover,
  useInteractions,
} from "@floating-ui/react";
import { useState } from "react";

function Tooltip({
  label,
  children,
}: {
  label: string;
  children: React.ReactNode;
}) {
  const [open, setOpen] = useState(false);
  const { refs, floatingStyles, context } = useFloating({
    open,
    onOpenChange: setOpen,
    placement: "top",
    middleware: [offset(8), flip(), shift({ padding: 8 })],
    whileElementsMounted: autoUpdate,
  });
  const hover = useHover(context);
  const { getReferenceProps, getFloatingProps } = useInteractions([hover]);

  return (
    <>
      <span ref={refs.setReference} {...getReferenceProps()}>
        {children}
      </span>
      {open && (
        <div
          ref={refs.setFloating}
          style={floatingStyles}
          {...getFloatingProps()}
          role="tooltip"
        >
          {label}
        </div>
      )}
    </>
  );
}
```

`flip` moves the tooltip to the other side when there's no room, `shift` keeps it inside the viewport, and `autoUpdate` updates the position on scroll and resize.

## 241: How do you make sure icon libraries don't bloat your bundle?

- Import icons by name from an ESM build, like `import { Camera } from 'lucide-react'`, so tree shaking drops the rest.
- Avoid importing the whole icon set as an object (`import * as Icons`) and picking icons by string at runtime. That forces the bundler to include every icon.
- For `@mui/icons-material`, in development some setups are slow with barrel imports, so path imports (`@mui/icons-material/Delete`) can speed up the dev server.
- If you need dynamic icons from a CMS, load them on demand (lazy import or an SVG sprite) instead of bundling all of them.

Check the result with a bundle analyzer.

## 242: How do you render Markdown with code highlighting safely in React?

Use `react-markdown` with plugins and keep raw HTML disabled unless you sanitize it:

```tsx
import Markdown from "react-markdown";
import remarkGfm from "remark-gfm";
import rehypeHighlight from "rehype-highlight";

<Markdown
  remarkPlugins={[remarkGfm]}
  rehypePlugins={[rehypeHighlight]}
  components={{
    a: ({ node, ...props }) => (
      <a {...props} target="_blank" rel="noopener noreferrer" />
    ),
  }}
>
  {userContent}
</Markdown>;
```

If you must allow HTML from users, add `rehype-raw` together with `rehype-sanitize`. The `components` prop lets you replace any element, for example to use your own `Link` or `Code` component.

## 243: How do you create a basic rich text editor with Tiptap and save its content?

```tsx
import { useEditor, EditorContent } from "@tiptap/react";
import StarterKit from "@tiptap/starter-kit";

function NoteEditor({
  initial,
  onSave,
}: {
  initial: object;
  onSave: (json: object) => void;
}) {
  const editor = useEditor({
    extensions: [StarterKit],
    content: initial,
    immediatelyRender: false,
    onUpdate: ({ editor }) => onSave(editor.getJSON()),
  });

  if (!editor) return null;

  return (
    <>
      <button onClick={() => editor.chain().focus().toggleBold().run()}>
        Bold
      </button>
      <EditorContent editor={editor} />
    </>
  );
}
```

Save the JSON (`getJSON()`) rather than HTML when you can, because it is easier to validate and migrate. `immediatelyRender: false` avoids hydration problems with SSR. Debounce `onSave` in real code.

## 244: How do you set up a basic Lexical editor in React?

```tsx
import { LexicalComposer } from "@lexical/react/LexicalComposer";
import { RichTextPlugin } from "@lexical/react/LexicalRichTextPlugin";
import { ContentEditable } from "@lexical/react/LexicalContentEditable";
import { HistoryPlugin } from "@lexical/react/LexicalHistoryPlugin";
import { OnChangePlugin } from "@lexical/react/LexicalOnChangePlugin";
import { LexicalErrorBoundary } from "@lexical/react/LexicalErrorBoundary";

function Editor() {
  return (
    <LexicalComposer
      initialConfig={{ namespace: "notes", onError: console.error }}
    >
      <RichTextPlugin
        contentEditable={<ContentEditable className="editor" />}
        ErrorBoundary={LexicalErrorBoundary}
      />
      <HistoryPlugin />
      <OnChangePlugin
        onChange={(state) => console.log(JSON.stringify(state.toJSON()))}
      />
    </LexicalComposer>
  );
}
```

Features like lists, links and markdown shortcuts are added as more plugins and node types.

## 245: How do you animate something every frame in React Three Fiber?

Use the `useFrame` hook and change the Three.js object through a ref, not through React state:

```tsx
import { Canvas, useFrame } from "@react-three/fiber";
import { useRef } from "react";
import type { Mesh } from "three";

function SpinningBox() {
  const ref = useRef<Mesh>(null);
  useFrame((_, delta) => {
    if (ref.current) ref.current.rotation.y += delta;
  });
  return (
    <mesh ref={ref}>
      <boxGeometry />
      <meshNormalMaterial />
    </mesh>
  );
}

<Canvas>
  <SpinningBox />
</Canvas>;
```

Calling `setState` 60 times per second would re-render React on every frame and be slow. Mutating the object directly skips React entirely.

## 246: Which queries should you prefer in React Testing Library?

The recommended order follows how users and assistive tech find things:

1. `getByRole` (with `name`), the best default: `getByRole('button', { name: 'Save' })`.
2. `getByLabelText` for form fields.
3. `getByPlaceholderText`, `getByText`, `getByDisplayValue`.
4. `getByAltText`, `getByTitle`.
5. `getByTestId` only as a last resort.

Using roles also checks your accessibility a bit. If you can't find a button by role, a screen reader user probably can't either.

## 247: What is the difference between getBy, queryBy and findBy in Testing Library?

- `getBy...` returns the element or throws if it's not there. Use it when the element should exist.
- `queryBy...` returns `null` if not found. Use it to check something is not there: `expect(screen.queryByText('Error')).not.toBeInTheDocument()`.
- `findBy...` returns a promise and waits (1 second by default) for the element to show up. Use it for things that appear after async work.

Each has an `All` version (`getAllBy`, etc.) for multiple elements. `findBy` is basically `waitFor` + `getBy`.

## 248: Why should you call userEvent.setup() and await every interaction?

`userEvent.setup()` creates an instance that shares state between actions, such as which keys are pressed and where the pointer is. All its methods are async because they go through several events and microtasks, so you have to `await` them.

```tsx
test("submits the form", async () => {
  const user = userEvent.setup();
  render(<LoginForm onSubmit={onSubmit} />);
  await user.type(screen.getByLabelText("Email"), "a@b.com");
  await user.click(screen.getByRole("button", { name: "Log in" }));
  expect(onSubmit).toHaveBeenCalled();
});
```

Forgetting `await` leads to flaky tests and `act` warnings. If you use fake timers, pass `advanceTimers: vi.advanceTimersByTime` to `setup`.

## 249: How do you test a component that uses TanStack Query?

Create a new `QueryClient` for each test with retries turned off, and mock the network (MSW is a good fit):

```tsx
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { render, screen } from "@testing-library/react";

function renderWithClient(ui: React.ReactElement) {
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

A new client per test stops cached data from leaking between tests. Without `retry: false`, error tests would wait for 3 retries with backoff and time out.

## 250: How do you test components that use a Redux store?

Write a `renderWithProviders` helper that creates a real store for each test, optionally with preloaded state:

```tsx
import { configureStore } from "@reduxjs/toolkit";
import { Provider } from "react-redux";
import { render } from "@testing-library/react";
import { rootReducer, type RootState } from "./store";

export function renderWithProviders(
  ui: React.ReactElement,
  preloadedState?: Partial<RootState>,
) {
  const store = configureStore({ reducer: rootReducer, preloadedState });
  return { store, ...render(<Provider store={store}>{ui}</Provider>) };
}
```

The Redux docs recommend using a real store instead of mocking `useSelector`. That way you test the component, reducer and selectors together, the way they run in the app.

## 251: How do you reset Zustand stores between tests?

Since Zustand stores are module-level singletons, state from one test can leak into the next. Options:

- Save the initial state and reset it in `beforeEach`: `useStore.setState(initialState, true)` (the `true` replaces the whole state).
- Use the mock from the Zustand docs: put a `__mocks__/zustand.ts` file that wraps `create` and resets every store after each test.
- Create stores with `createStore` and provide them through context, so each test gets a new store.

```ts
const initial = useCartStore.getState();
beforeEach(() => useCartStore.setState(initial, true));
```

## 252: How do you write request handlers in MSW?

MSW v2 uses the `http` namespace and the `HttpResponse` class:

```ts
import { http, HttpResponse } from "msw";
import { setupServer } from "msw/node";

export const handlers = [
  http.get("/api/todos", () =>
    HttpResponse.json([{ id: 1, title: "Buy milk" }]),
  ),
  http.post("/api/todos", async ({ request }) => {
    const body = (await request.json()) as { title: string };
    return HttpResponse.json({ id: 2, ...body }, { status: 201 });
  }),
];

export const server = setupServer(...handlers);

beforeAll(() => server.listen({ onUnhandledRequest: "error" }));
afterEach(() => server.resetHandlers());
afterAll(() => server.close());
```

In a single test you can override a handler with `server.use(http.get('/api/todos', () => new HttpResponse(null, { status: 500 })))` to test error states.

## 253: How do you use MSW in the browser during development?

Generate the worker script once and start it before rendering the app:

```bash
npx msw init public --save
```

```tsx
// main.tsx
async function enableMocking() {
  if (import.meta.env.DEV && import.meta.env.VITE_MOCK_API === "true") {
    const { setupWorker } = await import("msw/browser");
    const { handlers } = await import("./mocks/handlers");
    await setupWorker(...handlers).start({ onUnhandledRequest: "bypass" });
  }
}

enableMocking().then(() => {
  createRoot(document.getElementById("root")!).render(<App />);
});
```

This lets frontend developers work before the backend is ready, and you reuse the same handlers in tests and Storybook. Network calls still show up in the DevTools Network tab.

## 254: How do you set up Vitest for testing React components?

```ts
// vite.config.ts
import { defineConfig } from "vitest/config";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  test: {
    environment: "jsdom",
    globals: true,
    setupFiles: ["./src/test/setup.ts"],
  },
});
```

```ts
// src/test/setup.ts
import "@testing-library/jest-dom/vitest";
import { cleanup } from "@testing-library/react";
import { afterEach } from "vitest";

afterEach(() => cleanup());
```

`jest-dom` adds matchers like `toBeInTheDocument` and `toHaveValue`. With `globals: true` you don't need to import `describe` and `expect` in every file, and Testing Library cleans up automatically.

## 255: What makes Playwright locators reliable?

Playwright locators are lazy and auto-waiting. Every time you act on a locator, Playwright finds the element again and waits until it is visible, enabled, stable and able to receive events. Assertions like `toBeVisible()` and `toHaveText()` also retry until they pass or time out.

```ts
await page.getByRole("button", { name: "Submit" }).click();
await expect(page.getByText("Saved")).toBeVisible();
```

So you almost never need manual `waitForTimeout` sleeps. Prefer user-facing locators (`getByRole`, `getByLabel`, `getByText`) over CSS selectors, which break when markup changes.

## 256: When would you use Playwright component testing instead of Vitest with jsdom?

jsdom is fast but not a real browser. It has no layout (sizes are all 0), no real CSS, no `IntersectionObserver` or `ResizeObserver`, and limited pointer events. Components that depend on these, like virtualized lists, charts, drag and drop or floating elements, are hard to test there.

Playwright component testing (still experimental) or Vitest Browser Mode render components in a real browser. They are slower to run but more realistic. A common split: logic and most components in jsdom, layout-heavy components in a real browser, and full user flows with Playwright E2E.

## 257: How do you write a component test in Cypress?

```tsx
// Counter.cy.tsx
import Counter from "./Counter";

describe("<Counter />", () => {
  it("increments", () => {
    cy.mount(<Counter initial={1} />);
    cy.contains("button", "1").click();
    cy.contains("button", "2").should("be.visible");
  });
});
```

`cy.mount` renders the component in a real browser with your Vite or Webpack config. You get the Cypress runner UI, so you can see the component and step through the test. Use `@testing-library/cypress` if you want `findByRole` style queries.

## 258: How do you write stories with args in Storybook?

Stories use Component Story Format (CSF), an ES module with a default export (meta) and named exports (stories):

```tsx
import type { Meta, StoryObj } from "@storybook/react-vite";
import { Button } from "./Button";

const meta = {
  component: Button,
  args: { children: "Save" },
} satisfies Meta<typeof Button>;

export default meta;
type Story = StoryObj<typeof meta>;

export const Primary: Story = { args: { variant: "primary" } };
export const Disabled: Story = { args: { disabled: true } };
```

Args become editable controls in the Storybook UI. Storybook is also moving to a newer CSF Factories format with better typing, so you may see that in newer projects.

## 259: What are play functions in Storybook?

A play function runs after a story renders and interacts with it, like a small test:

```tsx
import { expect, userEvent, within } from "storybook/test";

export const FilledForm: Story = {
  play: async ({ canvasElement }) => {
    const canvas = within(canvasElement);
    await userEvent.type(canvas.getByLabelText("Email"), "ana@example.com");
    await userEvent.click(canvas.getByRole("button", { name: "Sign up" }));
    await expect(canvas.getByText("Thanks!")).toBeInTheDocument();
  },
};
```

You can watch each step in the Interactions panel. With the Vitest addon, all stories with play functions run as tests in CI.

## 260: How do you mock API calls in Storybook?

The common approach is the `msw-storybook-addon`. You start MSW in the preview file and set handlers per story:

```tsx
// .storybook/preview.ts
import { initialize, mswLoader } from "msw-storybook-addon";
initialize();
export default { loaders: [mswLoader] };

// UserList.stories.tsx
export const Empty: Story = {
  parameters: {
    msw: { handlers: [http.get("/api/users", () => HttpResponse.json([]))] },
  },
};
```

This lets you show loading, empty and error states of components that fetch data without changing their code.

## 261: How do you provide context like a theme, router or QueryClient to Storybook stories?

Use decorators. A decorator wraps every story (or just one component's stories) with providers:

```tsx
// .storybook/preview.tsx
import type { Preview } from "@storybook/react-vite";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { MemoryRouter } from "react-router";

const preview: Preview = {
  decorators: [
    (Story) => (
      <QueryClientProvider client={new QueryClient()}>
        <MemoryRouter>
          <Story />
        </MemoryRouter>
      </QueryClientProvider>
    ),
  ],
};

export default preview;
```

You can also use `globalTypes` and toolbar items to switch themes or locales from the Storybook toolbar.

## 262: How do you set up ESLint for a React project with flat config?

```js
// eslint.config.js
import js from "@eslint/js";
import tseslint from "typescript-eslint";
import reactHooks from "eslint-plugin-react-hooks";
import reactRefresh from "eslint-plugin-react-refresh";
import { defineConfig } from "eslint/config";

export default defineConfig([
  { ignores: ["dist"] },
  {
    files: ["**/*.{ts,tsx}"],
    extends: [
      js.configs.recommended,
      tseslint.configs.recommended,
      reactHooks.configs.flat.recommended,
    ],
    plugins: { "react-refresh": reactRefresh },
    rules: { "react-refresh/only-export-components": "warn" },
  },
]);
```

ESLint 9 and later use flat config (`eslint.config.js`). The React hooks plugin's recommended config includes the classic hook rules and the React Compiler rules. The exact config export names can differ between plugin versions, so check the README.

## 263: How do you enable the React Compiler in a Vite project?

Install the Babel plugin and add it to the React plugin's Babel config:

```bash
npm install -D babel-plugin-react-compiler
```

```ts
// vite.config.ts
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [
    react({
      babel: { plugins: ["babel-plugin-react-compiler"] },
    }),
  ],
});
```

You can roll it out slowly with `compilationMode: 'annotation'` and a `'use memo'` directive in selected components, and turn it off for one component with `'use no memo'`. Next.js has a `reactCompiler` option in `next.config`.

## 264: Can the React Compiler break code that uses some libraries?

Yes, sometimes. The compiler assumes values follow React's rules (immutable props and state, pure renders). Libraries that return the same mutable object every render, with values changing inside it, can confuse the memoization, so the UI doesn't update.

Known examples have included React Hook Form's `watch()` and TanStack Table's `useReactTable` instance. The fixes are using the library's subscription hooks (`useWatch`), upgrading to a compiler-aware version, or adding `'use no memo'` to the affected component. The ESLint rules help catch other problems before you enable the compiler.

## 265: How do you use TanStack Query with the Next.js App Router?

Prefetch on the server in a Server Component, dehydrate the cache, and hydrate it on the client:

```tsx
// app/posts/page.tsx (Server Component)
import {
  dehydrate,
  HydrationBoundary,
  QueryClient,
} from "@tanstack/react-query";
import Posts from "./posts";

export default async function PostsPage() {
  const queryClient = new QueryClient();
  await queryClient.prefetchQuery({ queryKey: ["posts"], queryFn: getPosts });
  return (
    <HydrationBoundary state={dehydrate(queryClient)}>
      <Posts />
    </HydrationBoundary>
  );
}
```

`Posts` is a client component that calls `useQuery({ queryKey: ['posts'], ... })` and gets the data right away. The `QueryClientProvider` lives in a client `providers.tsx` file. Create a new `QueryClient` per request on the server, and set a `staleTime` above 0 so the client doesn't refetch immediately.

## 266: How do you use Zustand safely with Next.js and SSR?

A global store created at module level is shared between all requests on the server, so one user's data could leak to another. The recommended pattern is to create the store per request and provide it through context:

```tsx
"use client";
import { createContext, useContext, useState } from "react";
import { createStore, useStore } from "zustand";

type CounterState = { count: number; inc: () => void };
const createCounterStore = (init = 0) =>
  createStore<CounterState>()((set) => ({
    count: init,
    inc: () => set((s) => ({ count: s.count + 1 })),
  }));

const CounterContext = createContext<ReturnType<
  typeof createCounterStore
> | null>(null);

export function CounterProvider({
  initial,
  children,
}: {
  initial: number;
  children: React.ReactNode;
}) {
  const [store] = useState(() => createCounterStore(initial));
  return (
    <CounterContext.Provider value={store}>{children}</CounterContext.Provider>
  );
}

export function useCounter<T>(selector: (s: CounterState) => T) {
  const store = useContext(CounterContext);
  if (!store) throw new Error("Missing CounterProvider");
  return useStore(store, selector);
}
```

Also, Server Components can't read Zustand stores. Keep stores in client components.

## 267: How do you get the session in Next.js with Auth.js?

After configuring Auth.js in `auth.ts`, you call `auth()` on the server and use `useSession` in client components:

```tsx
// auth.ts
import NextAuth from "next-auth";
import GitHub from "next-auth/providers/github";
export const { handlers, auth, signIn, signOut } = NextAuth({
  providers: [GitHub],
});

// app/dashboard/page.tsx
import { auth } from "@/auth";
import { redirect } from "next/navigation";

export default async function Dashboard() {
  const session = await auth();
  if (!session) redirect("/login");
  return <p>Hello {session.user?.name}</p>;
}
```

Client components need a `SessionProvider` to use `useSession`. Prefer checking on the server, since it avoids a flash of logged-out UI.

## 268: How do you protect pages with Clerk in a React or Next.js app?

In Next.js, add Clerk's middleware to protect routes, and use its components in the UI:

```ts
// middleware.ts
import { clerkMiddleware, createRouteMatcher } from "@clerk/nextjs/server";

const isProtected = createRouteMatcher(["/dashboard(.*)"]);

export default clerkMiddleware(async (auth, req) => {
  if (isProtected(req)) await auth.protect();
});
```

```tsx
import { SignedIn, SignedOut, SignInButton, UserButton } from '@clerk/nextjs';

<SignedOut><SignInButton /></SignedOut>
<SignedIn><UserButton /></SignedIn>;
```

On the server, `auth()` gives you the `userId` and a way to get tokens for your own API. Newer Next.js versions renamed `middleware.ts` to `proxy.ts`, so follow the docs for your version.

## 269: How do you call a protected API with the Auth0 React SDK?

Use `getAccessTokenSilently` to get a token for your API audience, then send it as a Bearer token:

```tsx
import { useAuth0 } from "@auth0/auth0-react";
import { useQuery } from "@tanstack/react-query";

function Orders() {
  const { getAccessTokenSilently } = useAuth0();
  const { data } = useQuery({
    queryKey: ["orders"],
    queryFn: async () => {
      const token = await getAccessTokenSilently();
      const res = await fetch("/api/orders", {
        headers: { Authorization: `Bearer ${token}` },
      });
      return res.json();
    },
  });
  return <pre>{JSON.stringify(data, null, 2)}</pre>;
}
```

The `audience` is set in `Auth0Provider`'s `authorizationParams`. The SDK caches tokens and refreshes them when they expire. Turning on refresh tokens with rotation avoids problems with third-party cookie blocking.

## 270: How do you listen to auth state changes with Supabase in React?

```tsx
import { useEffect, useState } from "react";
import type { Session } from "@supabase/supabase-js";

export function useSession() {
  const [session, setSession] = useState<Session | null>(null);

  useEffect(() => {
    supabase.auth.getSession().then(({ data }) => setSession(data.session));
    const { data } = supabase.auth.onAuthStateChange((_event, session) =>
      setSession(session),
    );
    return () => data.subscription.unsubscribe();
  }, []);

  return session;
}
```

The listener fires on sign in, sign out and token refresh. For SSR frameworks, use `@supabase/ssr`, which stores the session in cookies so the server can read it too.

## 271: How do you write a hook for the current Firebase user?

```tsx
import { onAuthStateChanged, type User } from "firebase/auth";
import { useEffect, useState } from "react";
import { auth } from "./firebase";

export function useFirebaseUser() {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    return onAuthStateChanged(auth, (u) => {
      setUser(u);
      setLoading(false);
    });
  }, []);

  return { user, loading };
}
```

`onAuthStateChanged` returns an unsubscribe function, which is used as the effect cleanup. Show a loading state until the first callback, because Firebase needs a moment to restore the session.

## 272: How do you use Socket.IO correctly inside a React component?

Create the socket once (outside the component or in a context), and add and remove listeners in an effect:

```tsx
import { useEffect, useState } from "react";
import { io } from "socket.io-client";

const socket = io("https://chat.example.com", { autoConnect: false });

function Chat({ room }: { room: string }) {
  const [messages, setMessages] = useState<string[]>([]);

  useEffect(() => {
    socket.connect();
    socket.emit("join", room);
    const onMessage = (msg: string) => setMessages((prev) => [...prev, msg]);
    socket.on("message", onMessage);
    return () => {
      socket.off("message", onMessage);
      socket.emit("leave", room);
      socket.disconnect();
    };
  }, [room]);

  return (
    <ul>
      {messages.map((m, i) => (
        <li key={i}>{m}</li>
      ))}
    </ul>
  );
}
```

Removing the exact listener in cleanup avoids duplicate messages, which you'd otherwise notice right away in StrictMode, where effects run twice in development.

## 273: How do you set up Sentry in a React app?

```tsx
import * as Sentry from "@sentry/react";

Sentry.init({
  dsn: import.meta.env.VITE_SENTRY_DSN,
  environment: import.meta.env.MODE,
  integrations: [
    Sentry.browserTracingIntegration(),
    Sentry.replayIntegration(),
  ],
  tracesSampleRate: 0.1,
  replaysSessionSampleRate: 0,
  replaysOnErrorSampleRate: 1.0,
});

createRoot(document.getElementById("root")!, {
  onUncaughtError: Sentry.reactErrorHandler(),
  onCaughtError: Sentry.reactErrorHandler(),
}).render(<App />);
```

React 19's root error hooks send errors to Sentry, including ones caught by error boundaries. Upload source maps in your build (with the Sentry Vite plugin) so stack traces show your original code, and use the router-specific integration for better page load and navigation traces.

## 274: How do you sync filters with the URL using nuqs?

```tsx
import {
  useQueryStates,
  parseAsString,
  parseAsInteger,
  parseAsArrayOf,
} from "nuqs";

function Filters() {
  const [filters, setFilters] = useQueryStates(
    {
      q: parseAsString.withDefault(""),
      page: parseAsInteger.withDefault(1),
      tags: parseAsArrayOf(parseAsString).withDefault([]),
    },
    { history: "replace" },
  );

  return (
    <input
      value={filters.q}
      onChange={(e) => setFilters({ q: e.target.value || null, page: 1 })}
    />
  );
}
```

Setting a value to `null` removes it from the URL. `history: 'replace'` stops every keystroke from adding a history entry. You need to wrap the app in the nuqs adapter for your router (Next.js, React Router and so on).

## 275: How do you debounce a search input in React?

You can use a hook from a library (`use-debounce`, `usehooks-ts`), or write a small one:

```tsx
import { useEffect, useState } from "react";

function useDebouncedValue<T>(value: T, delay = 300) {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const id = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(id);
  }, [value, delay]);
  return debounced;
}

function Search() {
  const [text, setText] = useState("");
  const query = useDebouncedValue(text);
  const { data } = useQuery({
    queryKey: ["search", query],
    queryFn: () => search(query),
    enabled: query.length > 1,
  });
  return <input value={text} onChange={(e) => setText(e.target.value)} />;
}
```

The input stays responsive because it uses the raw `text`, and only the request waits. `useDeferredValue` is another option when the slow part is rendering, not the network.

## 276: How do you build infinite scroll with react-intersection-observer and TanStack Query?

Put a sentinel element at the end of the list and load the next page when it becomes visible:

```tsx
import { useInView } from "react-intersection-observer";
import { useEffect } from "react";

function Feed() {
  const { data, fetchNextPage, hasNextPage, isFetchingNextPage } =
    useInfiniteQuery(feedQuery);
  const { ref, inView } = useInView({ rootMargin: "200px" });

  useEffect(() => {
    if (inView && hasNextPage && !isFetchingNextPage) fetchNextPage();
  }, [inView, hasNextPage, isFetchingNextPage, fetchNextPage]);

  return (
    <>
      {data?.pages
        .flatMap((p) => p.items)
        .map((item) => (
          <Post key={item.id} post={item} />
        ))}
      <div ref={ref}>{isFetchingNextPage ? "Loading..." : null}</div>
    </>
  );
}
```

`rootMargin: '200px'` starts loading a bit before the user reaches the bottom. For very long feeds, combine this with virtualization.

## 277: How do you safely render HTML from a CMS in React?

Sanitize it with DOMPurify before using `dangerouslySetInnerHTML`, and limit what is allowed:

```tsx
import DOMPurify from "dompurify";

const clean = DOMPurify.sanitize(cmsHtml, {
  ALLOWED_TAGS: ["p", "a", "strong", "em", "ul", "ol", "li", "h2", "h3", "img"],
  ALLOWED_ATTR: ["href", "src", "alt", "title"],
});

<article dangerouslySetInnerHTML={{ __html: clean }} />;
```

On the server (SSR) DOMPurify needs a DOM, so use `isomorphic-dompurify` or sanitize with jsdom. Even if the CMS is "trusted", sanitize anyway, because editor accounts can be compromised. A Content Security Policy adds another layer.

## 278: How do you control an Embla carousel from your own buttons?

`useEmblaCarousel` returns a ref and an API object:

```tsx
import useEmblaCarousel from "embla-carousel-react";
import { useCallback } from "react";

function Gallery({ images }: { images: string[] }) {
  const [emblaRef, emblaApi] = useEmblaCarousel({ loop: true });
  const prev = useCallback(() => emblaApi?.scrollPrev(), [emblaApi]);
  const next = useCallback(() => emblaApi?.scrollNext(), [emblaApi]);

  return (
    <div>
      <div className="overflow-hidden" ref={emblaRef}>
        <div className="flex">
          {images.map((src) => (
            <img
              key={src}
              src={src}
              className="min-w-0 flex-[0_0_100%]"
              alt=""
            />
          ))}
        </div>
      </div>
      <button onClick={prev}>Previous</button>
      <button onClick={next}>Next</button>
    </div>
  );
}
```

The API also has events like `select` for building dot indicators, and plugins for autoplay and fade.

## 279: How do you build a command palette with cmdk and a dialog?

`cmdk` has a `Command.Dialog` that uses Radix Dialog. Open it with a keyboard shortcut:

```tsx
import { Command } from "cmdk";
import { useEffect, useState } from "react";

function CommandMenu() {
  const [open, setOpen] = useState(false);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "k" && (e.metaKey || e.ctrlKey)) {
        e.preventDefault();
        setOpen((o) => !o);
      }
    };
    document.addEventListener("keydown", onKey);
    return () => document.removeEventListener("keydown", onKey);
  }, []);

  return (
    <Command.Dialog open={open} onOpenChange={setOpen} label="Command menu">
      <Command.Input />
      <Command.List>
        <Command.Group heading="Pages">
          <Command.Item onSelect={() => setOpen(false)}>Dashboard</Command.Item>
        </Command.Group>
      </Command.List>
    </Command.Dialog>
  );
}
```

For large result sets from an API, turn off the built-in filtering with `shouldFilter={false}` and filter on the server.

## 280: How do you combine React 19's useActionState with Zod validation?

You can skip a form library for simple forms and validate in the action:

```tsx
import { useActionState } from "react";
import { z } from "zod";

const schema = z.object({ email: z.email(), name: z.string().min(2) });
type State = { errors?: Record<string, string[] | undefined>; ok?: boolean };

async function subscribe(_prev: State, formData: FormData): Promise<State> {
  const parsed = schema.safeParse(Object.fromEntries(formData));
  if (!parsed.success)
    return { errors: z.flattenError(parsed.error).fieldErrors };
  await api.subscribe(parsed.data);
  return { ok: true };
}

function SubscribeForm() {
  const [state, formAction, isPending] = useActionState(subscribe, {});
  return (
    <form action={formAction}>
      <input name="email" />
      {state.errors?.email && <p>{state.errors.email[0]}</p>}
      <input name="name" />
      <button disabled={isPending}>Subscribe</button>
    </form>
  );
}
```

In Next.js the action can be a server action, so the same Zod schema runs on the server. For complex forms with live validation, React Hook Form is still easier.

## 281: How do you render an email template with React Email?

```tsx
import {
  Html,
  Body,
  Container,
  Heading,
  Text,
  Button,
} from "@react-email/components";
import { render } from "@react-email/render";

function WelcomeEmail({ name }: { name: string }) {
  return (
    <Html>
      <Body style={{ fontFamily: "Arial, sans-serif" }}>
        <Container>
          <Heading>Welcome, {name}</Heading>
          <Text>Thanks for signing up.</Text>
          <Button
            href="https://example.com/start"
            style={{
              background: "#0f766e",
              color: "#fff",
              padding: "10px 16px",
            }}
          >
            Get started
          </Button>
        </Container>
      </Body>
    </Html>
  );
}

const html = await render(<WelcomeEmail name="Ana" />);
```

You render the HTML on the server and pass it to your email provider. React Email also has a dev server to preview templates.

## 282: How do you find out which libraries make your bundle large?

Use a bundle analyzer to see what is inside each chunk:

- `rollup-plugin-visualizer` for Vite (it builds a treemap after `vite build`).
- `@next/bundle-analyzer` for Next.js.
- `source-map-explorer` for any build with source maps.

Before adding a library, check its size on bundlephobia or pkg-size. Common big offenders are Moment.js with all locales, the full lodash, icon sets imported the wrong way, chart libraries, rich text editors and PDF tools. Heavy ones that aren't needed on first load should be lazy loaded.

## 283: How do you make sure a library can be tree-shaken?

Tree shaking works when:

- The library ships ES modules (`"module"` or `"exports"` with an `import` condition), not only CommonJS.
- It marks itself as `"sideEffects": false` (or lists only the files with side effects) in `package.json`.
- You import named exports (`import { debounce } from 'lodash-es'`) instead of the default object.

For example, `import _ from 'lodash'` pulls in the whole library, while `import debounce from 'lodash-es/debounce'` or `es-toolkit` gives you only one function. Check the result with a bundle analyzer, not just by trusting the docs.

## 284: How would you replace Moment.js in an existing React app?

1. Find all uses (`grep "moment"`) and group them by what they do: formatting, parsing, math, time zones, relative time.
2. Pick a replacement. Day.js has almost the same API, so it is the fastest migration. date-fns is a good choice if you want functional, tree-shakable code.
3. Write a small wrapper module (`formatDate`, `addDays` and so on) and switch call sites to it, so a future change is easier.
4. Watch the differences: Moment objects are mutable, format tokens differ in date-fns (`yyyy` vs `YYYY`), and time zone handling needs plugins.
5. Add tests around date logic before you change it, especially for edge cases like DST and month ends.

## 285: How do you set up MUI X Date Pickers?

They need a date adapter and a `LocalizationProvider`:

```tsx
import { LocalizationProvider } from "@mui/x-date-pickers/LocalizationProvider";
import { AdapterDateFns } from "@mui/x-date-pickers/AdapterDateFns";
import { DatePicker } from "@mui/x-date-pickers/DatePicker";
import { enGB } from "date-fns/locale";

<LocalizationProvider dateAdapter={AdapterDateFns} adapterLocale={enGB}>
  <DatePicker label="Start date" value={start} onChange={setStart} />
</LocalizationProvider>;
```

Adapters exist for date-fns, Day.js, Luxon and Moment, so the picker works with the date library you already use. The adapter import path depends on the date-fns version you have, so check the docs. Date range pickers are in the paid Pro plan.

## 286: How do you use Immer for complex state in a component?

Use `use-immer`'s `useImmer` (or call `produce` in `setState`):

```tsx
import { useImmer } from "use-immer";

function Kanban() {
  const [board, updateBoard] = useImmer({
    columns: { todo: ["a", "b"], done: [] as string[] },
  });

  function moveToDone(id: string) {
    updateBoard((draft) => {
      draft.columns.todo = draft.columns.todo.filter((x) => x !== id);
      draft.columns.done.push(id);
    });
  }
  // ...
}
```

It makes nested updates much easier to read than spreading every level. Immer is a bit slower than hand-written spreads, which only matters in very hot paths.

## 287: What is the listener middleware in Redux Toolkit?

It lets you run side effects in response to actions or state changes, as a lighter alternative to sagas and observables:

```ts
import { createListenerMiddleware, isAnyOf } from "@reduxjs/toolkit";

export const listener = createListenerMiddleware();

listener.startListening({
  matcher: isAnyOf(todoAdded, todoToggled),
  effect: async (_action, api) => {
    api.cancelActiveListeners();
    await api.delay(500);
    localStorage.setItem("todos", JSON.stringify(api.getState().todos));
  },
});

// configureStore({ ..., middleware: (gDM) => gDM().prepend(listener.middleware) })
```

The `api` object has `getState`, `dispatch`, `delay`, `take`, `condition` and cancellation helpers, so you can write debounce, polling or multi-step flows.

## 288: Should you still use redux-persist?

`redux-persist` saves and restores the Redux store to storage. It still works and is used in many apps (especially React Native), but it gets few updates and adds complexity: migrations, rehydration timing and a `PersistGate`.

Before adding it, check what really needs persisting. Often it is just a few values (theme, a draft, auth info), which a small listener middleware writing to `localStorage` can handle. Server data should be cached by RTK Query or TanStack Query (which has its own persister), not persisted in Redux.

## 289: How do you update TanStack Query's cache from WebSocket messages?

Listen for messages and either update the cache directly or invalidate the related queries:

```tsx
function useLiveOrders() {
  const queryClient = useQueryClient();

  useEffect(() => {
    const ws = new WebSocket("wss://api.example.com/orders");
    ws.onmessage = (event) => {
      const msg = JSON.parse(event.data) as { type: "updated"; order: Order };
      queryClient.setQueryData<Order[]>(["orders"], (old) =>
        old?.map((o) => (o.id === msg.order.id ? msg.order : o)),
      );
      queryClient.invalidateQueries({ queryKey: ["order-stats"] });
    };
    return () => ws.close();
  }, [queryClient]);
}
```

Use `setQueryData` when the message has the full new data, and `invalidateQueries` when it's just a signal that something changed. Remember that `setQueryData` must not mutate the old data.

## 290: What are the main differences between SWR and TanStack Query?

Both cache server data with stale-while-revalidate. Differences:

- **Size**: SWR is smaller.
- **Mutations**: TanStack Query has `useMutation` with lifecycle callbacks and mutation state. SWR has `mutate` and `useSWRMutation`, which are simpler.
- **Cache control**: TanStack Query has `staleTime`, `gcTime`, partial key matching for invalidation, and more fine-grained options.
- **Devtools**: TanStack Query has official devtools.
- **Extras**: TanStack Query has infinite queries with bidirectional paging, offline support, persisters and support for other frameworks.

SWR is great for read-heavy apps with simple needs. TanStack Query is better when you have many mutations and complex cache logic.

## 291: How does React Router compare with TanStack Router?

- **Type safety**: TanStack Router types everything (paths, params, search params, loader data) out of the box. React Router's framework mode generates types per route module; data and declarative modes have less typing.
- **Search params**: TanStack Router treats them as validated, typed state. React Router gives you `URLSearchParams`.
- **Caching**: TanStack Router has a built-in loader cache with stale times. React Router reruns loaders on navigation and relies on HTTP caching or a data library.
- **Full stack**: React Router framework mode (ex-Remix) and TanStack Start both add SSR and server functions.
- **Maturity**: React Router is much older and more widely used.

Both are good. Pick React Router for a common, well-known choice, and TanStack Router if strong typing of URLs matters a lot.

## 292: How do you add retries and auth headers in ky?

Use `ky.create` with `retry` options and `hooks`:

```ts
import ky from "ky";

export const api = ky.create({
  prefixUrl: "/api",
  retry: {
    limit: 2,
    methods: ["get"],
    statusCodes: [408, 429, 500, 502, 503, 504],
  },
  hooks: {
    beforeRequest: [
      (request) => {
        const token = getToken();
        if (token) request.headers.set("Authorization", `Bearer ${token}`);
      },
    ],
    afterResponse: [
      async (_request, _options, response) => {
        if (response.status === 401) await logout();
      },
    ],
  },
});
```

ky retries only safe methods by default and respects `Retry-After` headers.

## 293: What is the difference between Radix's asChild and Base UI's render prop?

They solve the same problem: letting you render your own element (like a router `Link`) with the component's behavior.

```tsx
// Radix
<Dialog.Trigger asChild>
  <MyButton>Open</MyButton>
</Dialog.Trigger>

// Base UI
<Dialog.Trigger render={<MyButton />}>Open</Dialog.Trigger>
```

Base UI's `render` can also be a function that receives props and state, so you can render something based on whether it's open, active and so on. Radix's `asChild` merges props into its one child with a `Slot`. If you move a shadcn project from Radix to Base UI, these call sites are where most of the changes happen.

## 294: How do you use the Mantine hooks package without the rest of Mantine?

`@mantine/hooks` has no dependency on the Mantine components, so you can install it alone:

```tsx
import {
  useDisclosure,
  useDebouncedValue,
  useLocalStorage,
  useClickOutside,
} from "@mantine/hooks";

function Dropdown() {
  const [opened, { toggle, close }] = useDisclosure(false);
  const ref = useClickOutside(close);
  return (
    <div ref={ref}>
      <button onClick={toggle}>Menu</button>
      {opened && <ul>...</ul>}
    </div>
  );
}
```

It's a well-maintained and typed alternative to collections like `react-use`.

## 295: How do you make a Radix or shadcn component work with React Hook Form?

Most Radix inputs (Select, Checkbox, Switch, RadioGroup) are controlled components, not native inputs, so `register` doesn't work. Use `Controller`:

```tsx
<Controller
  name="notifications"
  control={control}
  render={({ field }) => (
    <Switch
      checked={field.value}
      onCheckedChange={field.onChange}
      onBlur={field.onBlur}
      ref={field.ref}
    />
  )}
/>
```

Watch out for different prop names: Radix uses `checked`/`onCheckedChange` and `value`/`onValueChange` instead of `value`/`onChange`. shadcn/ui has form helper components that do this wiring and connect labels, descriptions and error messages with the right ARIA attributes.

## 296: How do you load fonts and global styles with Material UI or other kits in Vite?

Install fonts as npm packages and import them once in your entry file:

```tsx
// main.tsx
import "@fontsource-variable/inter";
import "./index.css";
```

Self-hosting with Fontsource avoids a request to Google Fonts and works offline. Then set the font in your theme (`typography.fontFamily` in MUI) or in Tailwind's `@theme`. Import global CSS (resets, kit styles like `antd/dist/reset.css` or Mantine's `@mantine/core/styles.css`) in the entry file so the order is predictable.

## 297: How do you handle dark mode with Tailwind in React?

The simplest way is to toggle a `dark` class on `<html>` and use `dark:` utilities. In Tailwind v4 you set the class-based variant in CSS:

```css
@import "tailwindcss";
@custom-variant dark (&:where(.dark, .dark *));
```

```tsx
function ThemeToggle() {
  const toggle = () => {
    const isDark = document.documentElement.classList.toggle("dark");
    localStorage.setItem("theme", isDark ? "dark" : "light");
  };
  return <button onClick={toggle}>Toggle theme</button>;
}
```

Add a small inline script in `index.html` that sets the class before React loads, to avoid a flash of the light theme. In Next.js, `next-themes` does all of this for you.

## 298: How do you add the shadcn/ui Form with React Hook Form and Zod?

The common pattern combines all three. The shadcn form components connect labels, descriptions and error messages to RHF:

```tsx
const form = useForm<z.infer<typeof schema>>({
  resolver: zodResolver(schema),
  defaultValues: { username: "" },
});

<Form {...form}>
  <form onSubmit={form.handleSubmit(onSubmit)}>
    <FormField
      control={form.control}
      name="username"
      render={({ field }) => (
        <FormItem>
          <FormLabel>Username</FormLabel>
          <FormControl>
            <Input {...field} />
          </FormControl>
          <FormMessage />
        </FormItem>
      )}
    />
    <Button type="submit">Save</Button>
  </form>
</Form>;
```

`FormMessage` shows the field's error, and `FormControl` adds `aria-invalid` and `aria-describedby`. Newer shadcn versions also offer `Field` components that work with any form library, so you might see either style.

## 299: How do you migrate a React app from Create React App to Vite?

1. Install `vite` and `@vitejs/plugin-react`, add `vite.config.ts`, remove `react-scripts`.
2. Move `public/index.html` to the project root, remove `%PUBLIC_URL%`, and add `<script type="module" src="/src/main.tsx"></script>`.
3. Rename env vars from `REACT_APP_*` to `VITE_*` and replace `process.env.X` with `import.meta.env.VITE_X`.
4. Update scripts: `vite`, `vite build`, `vite preview`.
5. Replace Jest with Vitest (or keep Jest with its own config), and update SVG imports (`vite-plugin-svgr` for `ReactComponent` imports).
6. Rename files with JSX to `.jsx`/`.tsx` if they were `.js`.

Most apps migrate in a day. The tricky parts are usually custom Webpack config from `craco` or ejected setups.

## 300: How do you handle auth tokens that expire while using TanStack Query?

Keep token refresh in your HTTP client, not in each query. For example with an Axios response interceptor that refreshes once and retries:

```ts
let refreshing: Promise<string> | null = null;

api.interceptors.response.use(undefined, async (error) => {
  const original = error.config;
  if (error.response?.status !== 401 || original._retry) throw error;
  original._retry = true;
  refreshing ??= refreshToken().finally(() => (refreshing = null));
  const token = await refreshing;
  original.headers.Authorization = `Bearer ${token}`;
  return api(original);
});
```

Sharing one `refreshing` promise means ten parallel 401s cause only one refresh call. If refresh fails, log out and call `queryClient.clear()` so the next user doesn't see cached data.

# Advanced Questions (301-450)

## 301: How does TanStack Query's cache work internally?

The `QueryClient` holds a `QueryCache`, which is a map from a hashed query key to a `Query` object. Each `Query` keeps the data, error, status and timestamps, and runs the fetch.

Each `useQuery` call creates a `QueryObserver` that subscribes to one `Query`. The observer decides when to fetch (on mount, on focus, when stale) and computes the result your component sees. Components subscribe to the observer through `useSyncExternalStore`, so React re-renders them only when the observer reports a change.

When the last observer unsubscribes, the query becomes inactive and a timer for `gcTime` starts. If no one subscribes again before it fires, the query is removed. Many observers on the same key share one `Query`, which is why requests are deduplicated.

## 302: What is structural sharing in TanStack Query and why does it matter?

When new data arrives, TanStack Query compares it deeply with the old data and keeps the old object references for any part that didn't change. So if you refetch a list of 100 items and only one changed, 99 item objects keep the same reference.

This matters because `React.memo`, `useMemo` and selectors compare by reference. Components showing unchanged items don't re-render. It only works for JSON-compatible data. For huge responses, the deep compare costs CPU, and you can turn it off with `structuralSharing: false` or pass your own function.

## 303: How do select and tracked properties reduce re-renders in TanStack Query?

- `select` transforms or picks part of the data. The component re-renders only when the selected result changes:

```ts
const { data: count } = useQuery({
  ...todosQuery,
  select: (todos) => todos.length,
});
```

- Tracked properties: TanStack Query watches which fields of the result you actually read (`data`, `isFetching`, `error` and so on). If you never read `isFetching`, a background refetch that only changes `isFetching` won't re-render your component.

So don't spread the whole result (`const query = useQuery(...); <Child {...query} />`), because that reads every field and turns this optimization off. Keep `select` functions stable (defined outside the component or memoized), or they run on every render.

## 304: How do you design query keys in a large app?

Use a query key factory per feature, so keys are built in one place and follow a hierarchy from general to specific:

```ts
export const todoKeys = {
  all: ["todos"] as const,
  lists: () => [...todoKeys.all, "list"] as const,
  list: (filters: { status?: string; page?: number }) =>
    [...todoKeys.lists(), filters] as const,
  details: () => [...todoKeys.all, "detail"] as const,
  detail: (id: number) => [...todoKeys.details(), id] as const,
};

queryClient.invalidateQueries({ queryKey: todoKeys.lists() });
```

Because invalidation matches by prefix, you can invalidate all lists without touching details, or everything about todos. Combining this with `queryOptions` keeps keys and fetch functions together, which avoids typos and mismatched types.

## 305: How does SSR with TanStack Query work, including streaming?

The classic flow: on the server, create a `QueryClient`, prefetch the queries the page needs, call `dehydrate(queryClient)` to get a serializable snapshot, and send it with the HTML. On the client, `HydrationBoundary` puts that data into the client cache before components read it.

With streaming and Server Components, you can also dehydrate queries that are still pending. You configure `shouldDehydrateQuery` to include pending queries, and the promise is streamed to the client. Client components use `useSuspenseQuery` and resume when the data arrives, without waiting for every query before sending the first HTML.

Things to watch: create a new client per request on the server, set a `staleTime` so the client doesn't refetch right after hydration, and don't dehydrate sensitive data you don't want in the HTML.

## 306: How do you avoid request waterfalls when using TanStack Query with a router?

A waterfall happens when a parent component fetches, renders, and only then a child starts its own fetch. To avoid it, start all requests as early as possible:

- Prefetch in route loaders: `loader: () => queryClient.ensureQueryData(postQuery(id))`. The fetch starts during navigation, in parallel with loading the route's code.
- Prefetch child data in the parent with `prefetchQuery` if you know the child will need it.
- Use `useSuspenseQueries` instead of several `useSuspenseQuery` calls in one component.
- Use `usePrefetchQuery` to start a fetch before a component that suspends.

The component still calls `useQuery` with the same key and gets cached data. The loader starts the work, and the cache stays the source of truth.

## 307: How do you avoid race conditions when fetching data in React?

A race condition happens when an older, slower response arrives after a newer one and overwrites it. Ways to prevent it:

- With TanStack Query or SWR, keys handle this. Each key has its own cache entry, and the component reads the entry for the current key, so an old response can't show up for a new search.
- Forward the `signal` that TanStack Query gives `queryFn` to `fetch`, so it cancels requests that are no longer needed:

```ts
useQuery({
  queryKey: ["search", q],
  queryFn: ({ signal }) =>
    fetch(`/api/search?q=${q}`, { signal }).then((r) => r.json()),
});
```

- In plain `useEffect` code, use an `ignore` flag or `AbortController` in the cleanup function.

## 308: What problems can happen with optimistic updates when mutations run at the same time?

If two mutations run close together, the first one's `onSettled` can invalidate and refetch while the second is still in flight. The refetch returns data without the second change, so the UI flickers back to an old state before the second mutation finishes.

Ways to handle it:

- In `onMutate`, call `await queryClient.cancelQueries({ queryKey })` so in-progress refetches don't overwrite your optimistic data.
- In `onSettled`, only invalidate when no other mutation with the same key is running: `if (queryClient.isMutating({ mutationKey: ['todo'] }) === 1) invalidate()`.
- Use `scope` on mutations to make them run one after the other.
- For rollback, save the previous value in `onMutate` and restore it in `onError`.

## 309: How do you make a TanStack Query app work offline?

A few pieces work together:

- `networkMode`: by default queries and mutations pause when the browser is offline and resume when it's back online.
- **Persisting the cache**: `persistQueryClient` with `createAsyncStoragePersister` (or a sync persister for `localStorage`) saves the cache, so the app shows data after a reload without network. Use a `buster` string to throw away old caches after a deploy.
- **Paused mutations**: set default mutation functions with `queryClient.setMutationDefaults` so persisted paused mutations can be resumed after reload with `resumePausedMutations()`.
- Increase `gcTime` (for example to 24 hours) so persisted data isn't garbage collected right away.

For real offline-first apps with sync and conflicts, a local database with sync (IndexedDB, or tools like PowerSync or Replicache-style engines) may be a better fit than a query cache.

## 310: How do external store libraries like Zustand and Redux connect to React?

They use `useSyncExternalStore`, a React hook made for subscribing to stores that live outside React:

```ts
const value = useSyncExternalStore(store.subscribe, () =>
  selector(store.getState()),
);
```

React calls `subscribe` to listen for changes, and calls the snapshot function during render. If the snapshot changed (by `Object.is`), the component re-renders. Zustand (`useStore`), react-redux (`useSelector`) and TanStack Query all build on this.

The snapshot function must return the same reference when nothing changed. That's why returning a new object from a selector causes re-renders or even infinite loops, and why Zustand needs `useShallow` for object selectors.

## 311: What is tearing and how do state libraries avoid it?

Tearing happens in concurrent rendering when React renders part of the UI with one version of an external store, pauses, the store changes, and then renders the rest with the new version. The screen ends up showing two different states at once.

`useSyncExternalStore` prevents this. If the store changes during a concurrent render, React detects that the snapshot is different and re-renders synchronously, so everything is consistent. The trade-off is that store updates can't use time slicing like `startTransition` updates can.

Libraries that store state in React itself (`useState`, context, Jotai with its store, Recoil) can work with transitions more naturally. That's one reason there's ongoing work on a concurrent-friendly external store API in React.

## 312: How is Zustand built internally?

Zustand's vanilla core (`createStore`) is very small. It keeps state in a closure and a `Set` of listeners:

```ts
function createStore<T>(
  init: (
    set: (p: Partial<T> | ((s: T) => Partial<T>)) => void,
    get: () => T,
  ) => T,
) {
  let state: T;
  const listeners = new Set<(s: T, prev: T) => void>();
  const setState = (partial: Partial<T> | ((s: T) => Partial<T>)) => {
    const next = typeof partial === "function" ? partial(state) : partial;
    if (!Object.is(next, state)) {
      const prev = state;
      state = Object.assign({}, state, next);
      listeners.forEach((l) => l(state, prev));
    }
  };
  const getState = () => state;
  const subscribe = (l: (s: T, prev: T) => void) => (
    listeners.add(l),
    () => listeners.delete(l)
  );
  state = init(setState, getState);
  return { getState, setState, subscribe };
}
```

The React part (`useStore`) is a thin `useSyncExternalStore` call with your selector. Middleware like `persist` and `devtools` are functions that wrap `set`, `get` and the store API. Knowing this makes it clear why Zustand is fast and why selectors matter.

## 313: Why would you put a Zustand store in React context instead of a module-level singleton?

A module-level store is global. That causes problems in some cases:

- **SSR**: on the server, all requests share the same module, so data leaks between users.
- **Tests**: state leaks between tests unless you reset it.
- **Multiple instances**: if you need two independent instances of a widget (two editors on one page), they would share one store.
- **Initial state from props**: a global store can't easily start with values from a server component or route loader.

Creating the store with `createStore` inside a provider (`useState(() => createStore(...))`) and reading it with `useStore(storeFromContext, selector)` solves all of these, while keeping Zustand's selective re-renders.

## 314: How does Jotai work internally?

An atom is just a config object (`{ read, write, init }`). It doesn't hold a value. Values live in a store, which is a `WeakMap` from atom config to atom state (value, dependencies, dependents, version).

When a derived atom reads others with `get`, the store records those dependencies. When an atom changes, the store marks its dependents as stale and recomputes them when they're read, and notifies subscribed components. Components subscribe through hooks that use `useReducer` and `useEffect` internally.

Because atoms are only keys, the same atom can have different values in different `Provider`s, which scopes state to a subtree. The default store (no Provider) is global.

## 315: What are common performance problems with Redux selectors?

- **New references**: `useSelector((s) => s.todos.filter(...))` returns a new array every time, so the component re-renders on every action. Fix with `createSelector` or `shallowEqual`.
- **Shared memoized selectors with arguments**: a `createSelector` has a cache of size 1 by default (Reselect 5 uses `weakMapMemoize`, which helps). If many components call it with different arguments, it keeps recomputing. Create a selector per component instance with `useMemo`, or rely on `weakMapMemoize`.
- **Selecting too much**: selecting a whole slice causes re-renders when anything in it changes. Select the smallest value you need.
- **Expensive work in the selector input functions**: input selectors run on every action, so keep them as simple property reads.

Redux Toolkit 2 warns in development when a selector returns a different result for the same input, which catches the first issue.

## 316: How do RTK Query and TanStack Query differ in architecture?

- **Where the cache lives**: RTK Query stores data in the Redux store, so it shows up in Redux DevTools and other reducers can react to its actions. TanStack Query has its own `QueryClient`, independent of any state library.
- **API definition**: RTK Query defines all endpoints up front in `createApi` and generates hooks. TanStack Query defines queries where they're used (or in `queryOptions` factories).
- **Invalidation**: RTK Query uses tags (`providesTags`/`invalidatesTags`). TanStack Query uses key prefixes.
- **Normalization**: neither normalizes data by default. Both are document caches.
- **Code generation**: RTK Query has an OpenAPI codegen that creates the whole API slice.

If you already use Redux, RTK Query fits nicely. If not, TanStack Query is lighter and more flexible.

## 317: How do you stream updates into an RTK Query cache entry?

Use `onCacheEntryAdded`. It runs when a component first subscribes to a cache entry, and you can open a WebSocket and update the cached data:

```ts
getMessages: build.query<Message[], string>({
  query: (channel) => `messages/${channel}`,
  async onCacheEntryAdded(channel, { updateCachedData, cacheDataLoaded, cacheEntryRemoved }) {
    const ws = new WebSocket(`wss://chat.example.com/${channel}`);
    try {
      await cacheDataLoaded;
      ws.onmessage = (event) => {
        const msg = JSON.parse(event.data) as Message;
        updateCachedData((draft) => {
          draft.push(msg);
        });
      };
    } catch {}
    await cacheEntryRemoved;
    ws.close();
  },
}),
```

`cacheEntryRemoved` resolves when the last subscriber leaves and `keepUnusedDataFor` (60 seconds by default) passes, so the socket closes automatically.

## 318: How do you split an RTK Query API across many feature folders?

Create one empty base API and inject endpoints from each feature with `injectEndpoints`:

```ts
// api/base.ts
export const baseApi = createApi({
  baseQuery: fetchBaseQuery({ baseUrl: "/api" }),
  tagTypes: ["User", "Order"],
  endpoints: () => ({}),
});

// features/orders/api.ts
export const ordersApi = baseApi.injectEndpoints({
  endpoints: (build) => ({
    getOrders: build.query<Order[], void>({
      query: () => "orders",
      providesTags: ["Order"],
    }),
  }),
});
export const { useGetOrdersQuery } = ordersApi;
```

There is still one reducer and one middleware, but each feature owns its endpoints, and lazy loaded features add their endpoints only when their code loads. Having one API (not several `createApi` calls) matters because tag invalidation only works within the same API.

## 319: What is the difference between a normalized cache and a document cache?

- A **document cache** (TanStack Query, SWR, RTK Query, urql's default) stores each response as-is under its key. If the same user appears in two queries, there are two copies. After a mutation you invalidate or update each affected query.
- A **normalized cache** (Apollo, urql Graphcache, Relay) splits responses into entities by type and id and stores each entity once. Queries point to entities, so updating `User:1` updates every query that contains it.

Normalized caches give consistent data automatically but need ids on everything, are more complex, and adding new items to lists still needs manual work. Document caches are simpler and work with any API, at the cost of more invalidation. For REST APIs, document caches are the common choice. For GraphQL, normalized caches fit naturally.

## 320: How do you handle pagination in Apollo's normalized cache?

By default, `posts(offset: 0)` and `posts(offset: 10)` are stored as separate fields. To merge pages into one list, define a field policy:

```ts
import { InMemoryCache } from "@apollo/client";
import {
  offsetLimitPagination,
  relayStylePagination,
} from "@apollo/client/utilities";

const cache = new InMemoryCache({
  typePolicies: {
    Query: {
      fields: {
        posts: offsetLimitPagination(["category"]),
        feed: relayStylePagination(),
      },
    },
    Product: { keyFields: ["sku"] },
  },
});
```

`keyArgs` (here `['category']`) tells Apollo which arguments create a separate list. Others, like `offset`, are merged. Then `fetchMore` loads the next page and the merge function joins it. `keyFields` changes how an entity is identified when it doesn't have an `id`.

## 321: What are Apollo Client's fetch policies and when do you use each?

- `cache-first` (default): use cached data if it's complete, otherwise request.
- `cache-and-network`: show cached data right away and also request fresh data. Good for lists that change often.
- `network-only`: always request, but still write the result to the cache.
- `no-cache`: always request and don't touch the cache. Good for one-off sensitive data.
- `cache-only`: never request. Used for data you know is cached or local state.
- `standby`: like `cache-first` but doesn't update automatically.

You can set `fetchPolicy` and `nextFetchPolicy` per query, for example `cache-and-network` on first load and `cache-first` after that, to avoid extra requests when the cache updates.

## 322: How does tRPC give type safety across the network, and what are its limits?

The server defines a router, and you export only its type: `export type AppRouter = typeof appRouter`. The client imports this type (not the code), and TypeScript infers inputs and outputs for each procedure. At runtime, the client just sends HTTP requests with JSON. Input validators (usually Zod) check data on the server.

Limits:

- Frontend and backend must share TypeScript types, which usually means a monorepo or the same project.
- It isn't a public API format. Other clients (mobile in another language, third parties) need REST or OpenAPI, although adapters exist.
- Big routers can slow down TypeScript in the editor.
- Output types are trusted from the server code. Without output validation, a bug in the server can still send something that doesn't match.

## 323: How does React Hook Form track form state without re-rendering everything?

RHF keeps the form values, errors and field states in a `control` object outside React state. Native inputs are registered with refs, so their value lives in the DOM and RHF reads it when needed.

`formState` is wrapped in a proxy. When your component reads `formState.errors` or `isDirty`, RHF records that this component is subscribed to those keys. When something changes, RHF only calls `setState` for components subscribed to the changed keys. `useWatch`, `useFormState` and `useController` do the same thing in child components.

That's why reading `formState` in the root component (or destructuring all of it) makes the whole form re-render more often. Read only what you need, as close to where it's used as possible.

## 324: How do you keep a very large form fast with React Hook Form?

- Split the form into section components, and use `useFormContext`, `useWatch` and `useFormState` inside them so only that section re-renders.
- Use uncontrolled native inputs with `register` where you can. `Controller` components re-render on each change.
- Avoid `watch()` in the root component.
- Use `mode: 'onSubmit'` or `'onBlur'` instead of `'onChange'` for validation, so you don't validate the whole schema on every keystroke. With a resolver, every validation runs the full schema.
- For long dynamic lists, virtualize rows and use `shouldUnregister: false` so hidden fields keep their values.
- Memoize heavy child components, or use the React Compiler.

Measure with the React Profiler before and after. Often one `watch` at the top is the whole problem.

## 325: What changed in Zod 4 compared to Zod 3?

Main changes:

- **Performance**: parsing is several times faster and TypeScript compilation is much lighter for big schemas.
- **Smaller bundles**: `zod/mini` offers a functional, tree-shakable API (similar to Valibot) for size-sensitive apps.
- **Top-level formats**: `z.email()`, `z.url()`, `z.uuid()`, `z.iso.datetime()` instead of `z.string().email()` (the old forms are deprecated).
- **Errors**: a single `error` parameter replaces `message`, `invalid_type_error` and `required_error`, and there are helpers like `z.flattenError`, `z.treeifyError` and `z.prettifyError`.
- **New features**: built-in JSON Schema export (`z.toJSONSchema`), metadata and registries, template literal types, and better recursive types.
- Some behavior changes, such as how `.default()` interacts with optional fields.

Most code works with few changes, and there's a codemod for the common ones.

## 326: What is Standard Schema and why do libraries care about it?

Standard Schema is a small shared TypeScript interface that validation libraries implement. It defines a `~standard` property with a `validate` function and type info. Zod, Valibot, ArkType, Effect Schema and others support it.

A library that accepts "any Standard Schema" (TanStack Form, TanStack Router, tRPC, React Hook Form's standard resolver and others) can use whatever validator you prefer, without a separate adapter for each one. For library authors it removes the need to maintain many integrations, and for users it means you can switch validators without changing your form or router code.

## 327: How do you share validation between the client and the server?

Put schemas in a shared package or folder that both sides import:

```ts
// shared/schemas/user.ts
export const CreateUserSchema = z.object({
  email: z.email(),
  password: z.string().min(12),
});
export type CreateUserInput = z.infer<typeof CreateUserSchema>;
```

The form uses it with `zodResolver` for instant feedback, and the API handler uses `safeParse` on the request body. Rules that need the database (unique email) run only on the server, and the error is mapped back to the field with `setError`.

Always validate on the server, even if the client already did. Client validation is only for user experience. Be careful not to put server-only details in the shared schema (like internal field names) if the bundle is public.

## 328: What are the trade-offs of building a design system on a headless library versus a full UI kit?

**On a full UI kit (MUI, Ant Design)**:

- Fast start, lots of complex components ready (data grid, date picker).
- Theming has limits. A very custom brand means fighting overrides and specificity.
- Upgrades can break your overrides.

**On headless primitives (Radix, Base UI, React Aria) plus your own styles**:

- Full control of look and markup. Accessibility handled by the primitive.
- You build and maintain every component, its styles, docs and tests.
- Complex widgets (date range pickers, grids) still need other libraries.

A common middle path is shadcn/ui: start from copied components on top of headless primitives, then change them freely. The decision usually depends on how custom the design is and how many people can maintain the system.

## 329: How do you type a polymorphic component in TypeScript?

A polymorphic component can render as different elements (`as="a"` or `as={Link}`) and should accept that element's props. One common typing:

```tsx
import type { ComponentPropsWithoutRef, ElementType } from "react";

type BoxProps<T extends ElementType> = {
  as?: T;
} & Omit<ComponentPropsWithoutRef<T>, "as">;

export function Box<T extends ElementType = "div">({
  as,
  ...props
}: BoxProps<T>) {
  const Component = as ?? "div";
  return <Component {...props} />;
}

<Box as="a" href="/home">
  Home
</Box>;
```

The `as` pattern gets slow for TypeScript with complex components and has trouble with refs. That's one reason many libraries moved to `asChild` (Radix) or a `render` prop (Base UI), which avoid these generic types.

## 330: How do you type a generic component like a Select or Table that works with any item type?

Make the component a generic function, so the item type flows from `items` to callbacks:

```tsx
type SelectProps<T> = {
  items: T[];
  value: T | null;
  onChange: (item: T) => void;
  getLabel: (item: T) => string;
  getKey: (item: T) => string | number;
};

export function Select<T>({
  items,
  value,
  onChange,
  getLabel,
  getKey,
}: SelectProps<T>) {
  return (
    <select
      value={value ? String(getKey(value)) : ""}
      onChange={(e) => {
        const found = items.find((i) => String(getKey(i)) === e.target.value);
        if (found) onChange(found);
      }}
    >
      {items.map((i) => (
        <option key={getKey(i)} value={String(getKey(i))}>
          {getLabel(i)}
        </option>
      ))}
    </select>
  );
}
```

Wrapping a generic component in `memo` or the old `forwardRef` loses the generic, so you need a type assertion. In React 19, `ref` is a normal prop, which avoids the `forwardRef` problem.

## 331: How do headless libraries make dialogs and menus accessible?

They handle several things you'd otherwise easily get wrong:

- **Focus management**: move focus into the dialog on open, trap Tab inside it, and return focus to the trigger on close.
- **Keyboard support**: Escape to close, arrow keys in menus and listboxes, typeahead, Home/End.
- **ARIA**: `role="dialog"`, `aria-modal`, `aria-labelledby`, `aria-expanded`, `aria-controls`, `aria-activedescendant`.
- **Hiding the rest of the page** from screen readers while modal (`aria-hidden` or `inert` on siblings).
- **Scroll locking** of the page behind a modal.
- **Dismiss** on outside click without breaking nested popovers.

When you override their behavior (for example, stop focus return), you can break accessibility, so test with a keyboard and a screen reader after customizing.

## 332: What problems happen with portals, z-index and stacking when mixing UI libraries?

Popovers, menus and dialogs are usually rendered in a portal at the end of `<body>` so parent `overflow: hidden` doesn't cut them off. Issues appear when:

- Two libraries use different z-index scales, so one library's dropdown opens behind another library's modal.
- A parent creates a new stacking context (`transform`, `filter`, `opacity < 1`, `isolation`) and the portal is inside it.
- A popover inside a modal is portaled outside the modal, and the modal's focus trap or outside-click handling closes the modal when you click in the popover.
- The modal sets `inert` or `aria-hidden` on siblings, including another library's portal.

Solutions: use one library for overlays when possible, align z-index tokens, configure portal containers (most libraries accept a `container` prop), and use the native `<dialog>` and popover API, which use the browser's top layer.

## 333: Why don't runtime CSS-in-JS libraries work well with React Server Components?

Libraries like styled-components and Emotion create styles during render and insert them through React context and hooks (theme context, `useInsertionEffect`). Server Components can't use context or hooks, and they don't run in the browser, so these libraries must run in client components.

That means any component using them must be marked `'use client'`, which removes much of the benefit of Server Components. For streaming SSR, they also need extra setup to collect and flush styles in the right order (a style registry with `useServerInsertedHTML` in Next.js).

That's why the ecosystem moved toward zero-runtime options: CSS Modules, Tailwind, vanilla-extract, StyleX, Panda CSS and MUI's Pigment CSS experiment.

## 334: What does useInsertionEffect do and why do CSS-in-JS libraries need it?

`useInsertionEffect` runs before React makes DOM changes and before any layout effects. CSS-in-JS libraries use it to insert `<style>` rules before the browser reads layout.

If they inserted styles in `useLayoutEffect`, a layout effect in another component could read the DOM (`getBoundingClientRect`) before the styles exist and get wrong values, or force extra style recalculations. Inserting during render (what older versions did) is not safe with concurrent rendering, since a render might be thrown away.

It's meant only for library authors. App code should use `useEffect` or `useLayoutEffect`.

## 335: How would you migrate a large app from styled-components to another styling solution?

1. **Pick the target**: CSS Modules (closest mental model), Tailwind, or a zero-runtime CSS-in-JS like vanilla-extract or Linaria (similar syntax).
2. **Move tokens first**: turn the styled-components theme into CSS variables. Both systems can read them during the migration.
3. **Go component by component**, starting with leaf components and the design system, so app pages pick up the change.
4. **Handle dynamic styles**: replace prop interpolations with variant classes, `data-*` attributes or CSS variables set in `style`.
5. **Remove `createGlobalStyle`** and move global CSS to a normal stylesheet.
6. **Use visual regression tests** (Chromatic or Playwright screenshots) to catch differences.
7. Remove the `ServerStyleSheet` and Babel/SWC plugin when the last usage is gone.

Both systems can live together during the migration, so it doesn't have to be a big bang.

## 336: What are the costs of tailwind-merge and how do you use it well?

`tailwind-merge` parses class strings and resolves conflicts at runtime. It caches results, but on large lists with many unique class combinations, it adds measurable CPU work in render.

Good practices:

- Use it only in components that accept a `className` override (the `cn` helper), not on every element.
- Keep base classes static, so caching works.
- Prefer variants (`cva`) for internal options instead of merging conflicting classes.
- If you use custom utilities or a custom theme scale, configure `extendTailwindMerge`, or it won't know these classes conflict.

Also make sure the version of `tailwind-merge` matches your Tailwind major version, since class names change between versions.

## 337: How do you keep Material UI apps fast?

- **Avoid heavy `sx` and `styled` in big lists**: each unique style creates Emotion work. Move static styles to `styled` components defined once, or to CSS classes.
- **Use the theme's CSS variables** (`cssVariables: true`) so theme switches don't re-render everything.
- **Virtualize long lists and tables** (`DataGrid` already does this).
- **Lazy load heavy components** like the date pickers, charts and rich editors.
- **Avoid unnecessary context re-renders** by keeping `ThemeProvider` stable (create the theme once, outside the component, or with `useMemo`).
- **Check bundle size**: named imports from `@mui/material` are fine in production builds with tree shaking, and path imports can help dev server speed.

Measure with React Profiler and Lighthouse instead of guessing.

## 338: How do you share design tokens across several UI libraries in one app?

Use CSS variables as the single source of truth and map each library's theme to them:

```css
:root {
  --color-primary: #0f766e;
  --radius-md: 8px;
}
```

```ts
// MUI
createTheme({
  cssVariables: true,
  palette: { primary: { main: "#0f766e" } },
  shape: { borderRadius: 8 },
});
// Tailwind v4: @theme { --color-primary: var(--color-primary); }
// Ant Design: ConfigProvider theme token colorPrimary
```

Some libraries need concrete values (not `var(...)`) because they compute shades in JavaScript, so you may need to export tokens from a JSON file with a tool like Style Dictionary to generate CSS, TS and theme files. It's even better to avoid mixing several UI kits, but in migrations shared tokens keep things consistent.

## 339: How do you keep Motion animations smooth?

- Animate `transform` and `opacity`. They run on the compositor and don't trigger layout. Animating `width`, `height`, `top` or `left` causes layout on every frame.
- Use motion values (`useMotionValue`, `useTransform`, `useScroll`) for values that change every frame. They update the DOM directly without re-rendering React.
- Use `layout` animations carefully on big trees. Each layout animation measures elements, which costs time. Scope them with `LayoutGroup`.
- Use `will-change: transform` only on elements that actually animate.
- Prefer hardware-accelerated animations where Motion can use the Web Animations API (`opacity`, `transform`, `filter`, `clipPath`), so they run even if the main thread is busy.

Check performance in the Chrome Performance panel. Long frames during animation usually mean layout thrashing or heavy React renders.

## 340: How do you reduce Motion's bundle size?

Use the `m` component with `LazyMotion` instead of `motion`. `motion` includes all features, while `m` starts small and features are loaded separately:

```tsx
import { LazyMotion, domAnimation, m } from "motion/react";

<LazyMotion features={domAnimation}>
  <m.div animate={{ opacity: 1 }} />
</LazyMotion>;
```

`domAnimation` covers animations, variants, exit and gestures. `domMax` adds layout animations and drag. You can also load features asynchronously: `features={() => import('./features').then((m) => m.default)}`. For simple cases, `motion/mini`'s `animate` function or plain CSS transitions might be all you need.

## 341: What problems come up when combining animations with virtualized lists?

Virtualized lists remove items that scroll out of view and reuse positions, so:

- **Exit animations** (`AnimatePresence`) play when items scroll out, which looks wrong. Exits should only run when items are really removed from the data.
- **Layout animations** measure positions that the virtualizer controls with absolute positioning, so the two fight each other.
- **Measured heights** change during an expand animation, and the virtualizer needs to re-measure (`measureElement` in TanStack Virtual) or it overlaps items.
- **Scroll position jumps** when items above change height.

Approaches: animate only content inside a row (not the row's position), skip enter animations for rows appearing due to scroll, and let the virtualizer measure after the animation ends.

## 342: How do virtualization libraries handle items with dynamic heights?

They start with an estimated size for each item to calculate the total height and which items are visible. When an item renders, they measure its real size (usually with `ResizeObserver`) and save it in a cache.

When a measured size differs from the estimate, positions of the following items shift. If the changed item is above the viewport, the library adjusts the scroll position so the visible content doesn't jump. TanStack Virtual does this with `measureElement` and `shouldAdjustScrollPositionOnItemSizeChange`, and react-virtuoso does it automatically.

Problems appear when the estimate is far off (scrollbar size jumps), with images that load late (height changes after measuring) and with "jump to item N" when items before N haven't been measured yet. Good estimates and reserving image space help.

## 343: What accessibility and UX trade-offs does virtualization have?

Because only visible rows are in the DOM:

- Browser find-in-page (Ctrl+F) can't find off-screen items.
- Screen readers only see the rendered items, so the total count is unknown unless you set `aria-rowcount`/`aria-setsize` and `aria-rowindex`/`aria-posinset`.
- Keyboard focus can be lost when the focused row scrolls out and is removed.
- Printing shows only the visible part.
- Anchor links into the list don't work.

Fixes: add ARIA count and index attributes, keep the focused item rendered, provide search inside the app, and consider pagination or "load more" instead when lists aren't truly huge. For a few hundred simple rows, plain rendering plus `content-visibility: auto` in CSS can be enough.

## 344: How is TanStack Table designed internally?

TanStack Table is a framework-agnostic core plus thin adapters (React, Vue, Solid and others). The core takes your `data`, `columns` and `state`, and builds a pipeline of "row models":

core rows → filtered rows → grouped rows → sorted rows → expanded rows → paginated rows

Each row model is a memoized function you opt into (`getSortedRowModel()` and so on), so features you don't use aren't in the bundle or the calculations. Each step only recalculates when its inputs change.

The React adapter (`useReactTable`) creates the table instance once and keeps it in sync with your options. State can be controlled (you pass `state` and `on*Change`) or left internal. Since the instance is the same object across renders, it doesn't play well with tools that rely on new references, which is why it has had React Compiler issues.

## 345: How would you build a table that shows 100,000 editable rows?

You need to avoid rendering and processing everything in React at once:

- **Virtualize** rows (and columns if there are many). TanStack Table + TanStack Virtual, or AG Grid / MUI X DataGrid, which virtualize by default.
- **Decide where data lives**: if the data comes from a server, use server-side sorting, filtering and pagination (AG Grid's server-side row model or infinite row model), so the browser only holds a window of rows.
- **Keep edits local**: store edits in a map of changed rows rather than copying the whole array on each keystroke, and re-render only the edited cell.
- **Batch saves**: send changes in batches with debounce, and show per-row saving state.
- **Memoize** row and cell components, and keep column definitions stable.
- **Move heavy work off the main thread** (Web Workers for filtering or CSV parsing).

For this size, a dedicated grid like AG Grid is often cheaper than building one.

## 346: How do you choose a rendering approach for charts with lots of data?

- **SVG** (Recharts, Nivo SVG, visx): each point is a DOM node. Easy to style and accessible, but slow beyond a few thousand elements.
- **Canvas** (Chart.js, ECharts, Nivo canvas, uPlot): draws pixels, fine for tens or hundreds of thousands of points. Harder to make accessible, and tooltips need hit-testing.
- **WebGL** (deck.gl, some ECharts modes, regl-based libraries): millions of points, maps, heatmaps. Most complex.

Also consider reducing data before drawing: downsampling (for example the LTTB algorithm), server-side aggregation, or showing summaries and loading detail on zoom. A chart showing 1 million points on a 1000-pixel wide screen can't show more than about 1000 points per line anyway.

## 347: How do you keep i18n from slowing down a React app?

- **Split translations** into namespaces per route or feature and load them lazily, instead of shipping every string in every language.
- **Load only the active language**, and preload the next likely namespace on route intent.
- **Avoid large translation objects in the JS bundle**. Serve JSON from a CDN with good caching (with a hash in the URL for cache busting).
- **Precompile ICU messages** (FormatJS and Lingui support this), so the browser doesn't parse message syntax at runtime.
- **Cache `Intl` formatters**, since creating `Intl.NumberFormat` and `Intl.DateTimeFormat` objects is costly. Libraries do this, but custom code often doesn't.
- **Use Suspense boundaries** so missing namespaces don't block the whole app.

## 348: How do you handle i18n with Server Components and SSR?

- The language must come from the request (URL segment, cookie or `Accept-Language`), not from global state, because the server handles many users at once.
- Create a separate i18n instance or pass the locale explicitly per request. A global i18next instance with `changeLanguage` is a race condition on the server.
- Load messages on the server and pass only what client components need, or use a library built for this. `next-intl` is popular for Next.js, with `getTranslations` on the server and `useTranslations` on the client.
- Make sure the server and client format dates and numbers with the same locale and time zone, or you get hydration mismatches.
- Put the locale in the URL (`/de/products`) for SEO, with `hreflang` links.

## 349: What is the ICU message format and why do libraries use it?

ICU MessageFormat is a standard syntax for messages with variables, plurals and selects, used by FormatJS (react-intl), Lingui, and available as an i18next plugin:

```text
{count, plural, =0 {No messages} one {# message} other {# messages}}
{gender, select, female {She replied} male {He replied} other {They replied}}
```

It keeps the whole sentence in one string, so translators can handle grammar rules (plural forms, gender, word order) in each language. Writing `count + ' message' + (count === 1 ? '' : 's')` in code only works for English. ICU is also supported by most translation management systems, so tools can validate and preview messages.

## 350: What are common date and time zone bugs in React apps, and how do libraries help?

- **Parsing date-only strings**: `new Date('2026-03-01')` is UTC midnight, which shows as February 28 in America. Parse with an explicit time zone or treat date-only values as plain dates.
- **DST**: adding 24 hours is not always "one day". Use `addDays` from a library, which works in calendar days.
- **Server vs client time zone**: SSR in UTC and the browser in local time render different strings, causing hydration mismatches.
- **Storing local times**: store instants in UTC (ISO strings) and the user's time zone separately when it matters (like for meetings).
- **Month math**: January 31 plus one month.

Libraries with time zone support (date-fns with `@date-fns/tz`, Luxon, Day.js plugins) and the new `Temporal` API with `PlainDate`, `ZonedDateTime` and `Instant` types help you be explicit about which kind of date you have.

## 351: How do you decide which libraries to load lazily?

Load something lazily if it's big and not needed for the first screen:

- Rich text editors, PDF viewers and generators, chart libraries, maps, 3D, syntax highlighters, spreadsheet parsers (like `xlsx`), date pickers on secondary pages.
- Code only for some users (admin tools) or some routes.

```tsx
const ReportChart = lazy(() => import("./ReportChart"));

<Suspense fallback={<ChartSkeleton />}>
  <ReportChart data={data} />
</Suspense>;
```

For heavy libraries used inside functions (like CSV export), import them inside the handler: `const { utils, writeFile } = await import('xlsx')`. Preload on hover or when the route is likely. Don't lazy load tiny pieces, because each extra chunk adds a request.

## 352: What does a library need so bundlers can tree-shake it?

- **ES module output**: `import`/`export` syntax. CommonJS (`require`, `module.exports`) can't be statically analyzed well.
- **A proper `exports` map** in `package.json` pointing to ESM files, with separate entry points for big features.
- **`"sideEffects": false`** (or a list of files that have side effects, such as CSS imports). Without it, bundlers keep any module you import in case it changes globals.
- **No top-level side effects**: code like registering plugins or patching prototypes at import time keeps the module alive.
- **Pure annotations**: `/*#__PURE__*/` on top-level calls like `createContext()` so minifiers can drop them if unused.
- **Avoid barrel files that re-export everything** with side effects, which also slow down dev servers.

## 353: What is the dual package hazard?

When a package ships both CommonJS and ESM builds, an app can end up loading both versions: one part of the code `require`s it and gets the CJS copy, another part `import`s it and gets the ESM copy.

Now there are two instances of the module. For React libraries this causes real bugs: two different `createContext` results (so a Provider from one copy doesn't work with hooks from the other), `instanceof` checks failing, or two separate stores.

Fixes for library authors: ship ESM only (more common now that Node supports `require` of ESM), or make the CJS build a thin wrapper around a shared state module. For app developers: check for duplicates with `npm ls` and bundler aliases, and make sure configs resolve the same entry point.

## 354: Why do you get "Invalid hook call" errors from libraries, and how do you fix them?

The most common causes:

1. **Two copies of React** in the bundle. A library listed `react` as a dependency (instead of a peer dependency), or you linked a local library with `npm link` and it uses its own `node_modules/react`. Hooks then run against a React that isn't rendering.
2. **Mismatched `react` and `react-dom` versions**.
3. **Calling a hook outside a component** (in a class component or a regular function).

Check with `npm ls react`. Fix it by making React a peer dependency in libraries, removing duplicates (`npm dedupe`, overrides or resolutions), or aliasing `react` to one path in the bundler config. In monorepos, workspace tools usually hoist React to one copy.

## 355: What breaks in libraries when upgrading to React 19?

Main changes that affect libraries:

- **`element.ref` was removed**: `ref` is now a normal prop. Libraries that read `child.ref` (like some `Slot` implementations) need updates.
- **`propTypes` and `defaultProps` for function components** are removed or ignored. Libraries that relied on `defaultProps` for function components must use default parameters.
- **Legacy APIs removed**: `ReactDOM.render`, `findDOMNode`, string refs, legacy context (`contextTypes`), `react-test-renderer/shallow`.
- **`forwardRef`** still works but is no longer needed. It will be deprecated later.
- **Type changes**: `useRef` requires an argument, `ReactElement` props default to `unknown`, the global `JSX` namespace moved to `React.JSX`.

When upgrading, update UI kits and testing libraries first (most supported React 19 quickly), and use the official codemods for app code.

## 356: Which libraries can you use inside React Server Components?

Server Components can't use state, effects, context or browser APIs. So:

- **Works on the server**: data access (database clients, ORMs, `fetch`), Zod, date libraries, Markdown to HTML converters, syntax highlighters (like Shiki), i18n libraries with server APIs, and components that only render markup (icons, Tailwind or CSS module components).
- **Needs a client component**: anything using hooks or context: TanStack Query hooks, Zustand, Redux, React Hook Form, most UI kits (Radix, MUI interactive parts), Motion, charts, editors.

Libraries mark client entry points with `'use client'`. If a library doesn't, you get errors like "createContext only works in Client Components" and need to wrap it in your own client component file. A good pattern is doing heavy work (Markdown parsing, highlighting) on the server so that code never reaches the browser.

## 357: How do you wrap a client-only library for use in a Next.js App Router page?

Create a small client component file that imports the library and re-exports or wraps it:

```tsx
// components/chart.tsx
"use client";
export { ResponsiveContainer, LineChart, Line, XAxis, YAxis } from "recharts";
```

If the library touches `window` or `document` at import time (common for maps and editors), load it only in the browser:

```tsx
"use client";
import dynamic from "next/dynamic";

const Map = dynamic(() => import("./LeafletMap"), {
  ssr: false,
  loading: () => <p>Loading map...</p>,
});
```

`ssr: false` must be used inside a client component. Keep the client boundary as low in the tree as possible, so the rest of the page stays as Server Components.

## 358: Why do libraries cause hydration mismatches, and how do you fix them?

Hydration fails when the server HTML is different from what the client renders the first time. Library-related causes:

- **Dates and times**: formatting in different time zones or locales on server and client.
- **Random ids**: libraries generating ids with `Math.random()` instead of `useId`.
- **Browser-only state**: reading `localStorage` (persisted Zustand stores, theme libraries) during render, so the client shows different values.
- **Media queries**: `useMediaQuery` returns `false` on the server and `true` on the client.
- **Browser extensions** changing the DOM (not your fault, but it looks similar).

Fixes: render the same thing on both sides first and update in an effect, pass the time zone and locale from the server, use libraries that support SSR (with `useId` and `useSyncExternalStore`'s `getServerSnapshot`), or render browser-dependent parts only on the client. `suppressHydrationWarning` is only for single text nodes you know will differ, like a timestamp.

## 359: How do useId and useSyncExternalStore's getServerSnapshot help libraries support SSR?

- **`useId`** creates ids based on the component's position in the tree, so the server and client generate the same id. UI libraries use it to connect labels, `aria-controls` and `aria-describedby` without hydration mismatches. Before React 18, libraries used counters, which broke with SSR and streaming.
- **`getServerSnapshot`** is the third argument of `useSyncExternalStore`. It returns the value used on the server and during hydration. For example, a media query hook returns a default on the server and the real value after hydration, without a mismatch error.

If you write a library hook that reads browser state, these two APIs are the right tools for making it SSR-safe.

## 360: What security problems can third-party React libraries introduce?

- **XSS**: components that render HTML (`dangerouslySetInnerHTML` in Markdown, rich text, or tooltip libraries), or that put user data into `href`/`src` without checking for `javascript:` URLs.
- **Supply chain attacks**: a compromised package (or a dependency of a dependency) steals tokens or environment variables. This has happened several times in npm, including with popular packages.
- **Typosquatting**: installing `reqct-router` instead of `react-router`.
- **Leaking secrets**: putting API keys in client env vars (`VITE_*`, `NEXT_PUBLIC_*`) to configure SDKs.
- **Old vulnerable versions**: known CVEs in dependencies.
- **Third-party scripts** (analytics, chat widgets) that run with full access to the page.

Mitigations: keep dependencies few, use a lockfile and `npm ci`, review updates, run `npm audit` or tools like Socket or Snyk, enable a Content Security Policy, and sanitize any HTML.

## 361: How do you protect a React project from npm supply chain attacks?

- **Lockfiles and `npm ci`** in CI, so installs are reproducible.
- **Pin or carefully review updates**. Use Renovate or Dependabot with grouped PRs, and consider a minimum release age (wait a few days before taking new versions), which many tools support now.
- **Disable install scripts** where possible (`ignore-scripts`, or pnpm's and Bun's default of not running dependency lifecycle scripts unless allowed).
- **Check provenance**: npm shows provenance attestations for packages built in public CI.
- **Scan dependencies** with `npm audit`, Socket, Snyk or GitHub's alerts.
- **Use scoped tokens with 2FA** for publishing your own packages.
- **Keep secrets out of the frontend** and out of build environments that run untrusted code.
- **Remove unused dependencies** regularly (`knip` and `depcheck` help find them).

## 362: Where should a React app store auth tokens when using auth libraries?

- **httpOnly, Secure, SameSite cookies** set by the server are the safest common choice for web apps. JavaScript can't read them, so XSS can't steal the token directly. You need CSRF protection for state-changing requests (SameSite helps, plus CSRF tokens or checking `Origin`).
- **In memory** (a variable or store) is reasonably safe from theft through storage, but is lost on reload, so you need a refresh flow (usually a refresh token in an httpOnly cookie).
- **localStorage/sessionStorage** is easy but any XSS can read it.

Many teams use a "backend for frontend" (BFF) pattern: the server handles OAuth and keeps tokens, and the browser only gets a session cookie. Libraries like Auth.js and Better Auth work this way. SPA SDKs like Auth0's keep tokens in memory by default with an option for local storage.

## 363: How do you choose libraries with license costs in mind?

Some popular React libraries are "open core": free basics, paid advanced features.

- **AG Grid**: Community (MIT) vs Enterprise (paid per developer).
- **MUI X**: DataGrid and Date Pickers free, Pro and Premium paid.
- **Highcharts**: free for non-commercial, paid for commercial use.
- **Some UI kits and icon sets** have paid "pro" versions.
- **Tiptap**: the editor is MIT, some extensions and collaboration services are paid.

Before choosing, check which features you'll need in a year, not just today. Grouping, pivoting, Excel export and tree data are often paid. Also check that the license fits your distribution (internal app vs SaaS vs redistributed library) and include license checks in your dependency review, for example with `license-checker`.

## 364: How do you notice that a library is being abandoned, and what do you do?

Warning signs: no releases for a long time, many open issues and PRs without answers, no support for the current React version, the maintainer saying they're stepping back, or the repo being archived. Examples from the past few years: Recoil, react-beautiful-dnd, Create React App, Enzyme, and styled-components moving to maintenance mode.

What to do:

1. Check if there's an official successor or a maintained fork (like `@hello-pangea/dnd`).
2. Find out how much code depends on it, ideally through your own wrapper.
3. Plan a migration while it still works, rather than when a React upgrade forces you.
4. For small libraries, copying the code into your repo can be a valid choice.

## 365: Why would you wrap a third-party library behind your own module?

Writing a thin adapter (for example `src/lib/dates.ts`, `src/lib/http.ts`, `src/ui/Button.tsx`) instead of importing the library everywhere gives you:

- **One place to change** when you switch libraries or upgrade a major version.
- **Consistent defaults** (time zone, base URL, error handling, theme).
- **A smaller surface**: the team uses only the features you chose.
- **Easier testing and mocking**.

The downside is extra code and the temptation to wrap everything. Wrap libraries that are used widely and might change (HTTP client, dates, analytics, feature flags, UI primitives), but don't wrap things like React Router or TanStack Query hooks deeply, since their APIs are already the abstraction.

## 366: How do you handle shared libraries across micro frontends?

With Module Federation (Webpack, Rspack, or the Vite plugin), each remote can share dependencies with the host:

```js
shared: {
  react: { singleton: true, requiredVersion: '^19.0.0' },
  'react-dom': { singleton: true, requiredVersion: '^19.0.0' },
  '@tanstack/react-query': { singleton: true },
}
```

`singleton: true` makes sure only one copy loads, which is required for React and for any library that uses context (React Router, TanStack Query, UI kits). Otherwise providers in the host won't work in the remotes.

Problems to plan for: version mismatches (one team upgrades), larger shared bundles, and global CSS from different UI kits clashing. Clear rules about which libraries are shared, and contracts between host and remotes, reduce these issues.

## 367: How do you split state across different kinds of libraries in a large app?

Separate state by where it comes from and who owns it:

- **Server state** (data from APIs): TanStack Query, RTK Query, SWR, Apollo.
- **URL state** (filters, tabs, pagination, selected id): the router or `nuqs`.
- **Form state** (draft values, validation): React Hook Form or TanStack Form.
- **Global client state** (theme, sidebar open, current workspace, multi-step wizard data): Zustand, Jotai, Redux.
- **Local UI state** (open/closed, hover): `useState` in the component.

Most bugs come from mixing these, such as copying API data into Redux and keeping it in sync, or storing filters in a store and the URL. After this split, the "global state" part is usually small.

## 368: How do the mental models of Redux, Zustand, Jotai, MobX and XState differ?

- **Redux**: one store, state changes only through dispatched actions and pure reducers. Very predictable and traceable. More ceremony.
- **Zustand**: one or more simple stores with functions that call `set`. Like a lighter Redux without required actions.
- **Jotai**: many small atoms, bottom-up. Derived state is a graph of atoms. Feels like `useState` that can be shared.
- **MobX**: observable objects you mutate directly. Reactions and components track what they read. Feels like OOP.
- **XState**: explicit states and transitions. Events are only accepted in states that allow them. Great for complex flows, more upfront design.

Choosing is often about your team's habits and the type of state: entity collections (Redux, MobX), small shared values (Zustand, Jotai), or workflows (XState).

## 369: How do you use XState actors for complex flows like a checkout?

In XState v5 everything is an actor: machines, promises, callbacks and observables. A checkout machine can invoke actors for async work and spawn child machines:

```ts
import { setup, fromPromise, assign } from "xstate";

export const checkoutMachine = setup({
  types: { context: {} as { orderId?: string; error?: string } },
  actors: {
    submitOrder: fromPromise(async ({ input }: { input: { cartId: string } }) =>
      api.submit(input.cartId),
    ),
  },
}).createMachine({
  initial: "review",
  context: {},
  states: {
    review: { on: { CONFIRM: "submitting" } },
    submitting: {
      invoke: {
        src: "submitOrder",
        input: { cartId: "c1" },
        onDone: {
          target: "done",
          actions: assign({ orderId: ({ event }) => event.output.id }),
        },
        onError: {
          target: "review",
          actions: assign({ error: "Payment failed" }),
        },
      },
    },
    done: { type: "final" },
  },
});
```

The flow is explicit: double clicks during `submitting` are ignored because there's no `CONFIRM` handler there. You can test the machine without React and visualize it in the Stately tools.

## 370: How does MobX track dependencies internally?

MobX makes observable objects with JavaScript proxies or property getters and setters. When a "derivation" runs (a `computed`, an `autorun`, or an `observer` component's render), MobX records every observable read during that run. Those become its dependencies.

When an observable changes inside an action, MobX marks dependent derivations as stale. At the end of the outermost action (a transaction), it re-runs the stale reactions once, in the right order. Computed values are cached and only recomputed when their inputs change and someone reads them.

`observer` wraps a component's render in a reaction, so it re-renders only when something it actually read changes. Dereferencing values late (passing the store object down instead of primitive values) gives the most precise updates.

## 371: How does Valtio work under the hood?

`proxy()` wraps your object in a JavaScript `Proxy` that tracks writes and bumps a version number on each change (and on parents when nested objects change).

`useSnapshot()` creates an immutable snapshot of the current state and wraps it in another tracking proxy (from `proxy-compare`) that records which properties your component reads during render. When the state changes, Valtio compares the new snapshot with the old one only for the properties you used. If they're the same, the component doesn't re-render.

That's why you must read from the snapshot in render and write to the original proxy in handlers. Writing to the snapshot throws, and reading from the proxy in render doesn't subscribe.

## 372: What are signals, and why are libraries like Preact Signals or Legend State used with React?

Signals are reactive values. When a signal changes, only the code that read it updates, without re-rendering the whole component. Preact Signals (`@preact/signals-react`) and Legend State bring this to React, sometimes updating text nodes directly in the DOM.

People use them for very frequent updates (live dashboards, big forms, local-first apps) where React re-renders are a bottleneck.

Trade-offs: they work around React's rendering model, which can conflict with concurrent features, StrictMode and the React Compiler, and some integrations patch React internals. The React team prefers a different direction (the compiler plus `useSyncExternalStore`). Use them with care and prefer explicit hooks provided by these libraries over the "auto" modes.

## 373: Why can React Context be slow for frequently changing state, and what do libraries do about it?

When a context value changes, every component that calls `useContext` for that context re-renders, even if it only uses a part of the value that didn't change. React has no built-in way to select a slice of context.

Options:

- Split into several contexts (state vs actions, or by domain).
- Memoize the value object so it only changes when needed.
- Use `use-context-selector`, which lets components subscribe to a slice.
- Put the state in an external store (Zustand, Jotai, Redux) and use context only to pass the store instance, not the state. The store's selectors then control re-renders.

This last pattern is why most state libraries put a stable store in context instead of the state itself.

## 374: What testing strategy works well for a React app with many libraries?

A common approach (sometimes called the "testing trophy"):

- **Static checks**: TypeScript and ESLint catch many bugs for free.
- **Unit tests** for pure logic: reducers, selectors, Zod schemas, utility functions, XState machines.
- **Integration tests** (most of your tests): render a feature with real providers (router, QueryClient, store) and MSW for the network, interact with Testing Library, and check what the user sees.
- **Component tests in a real browser** for layout-heavy parts (charts, virtualization, drag and drop).
- **E2E tests** with Playwright for critical flows (login, checkout) against a real or staging backend.
- **Visual regression** for the design system.

Avoid mocking the libraries themselves (mocking `useQuery`, `useSelector`, the router) where you can. Use the real ones with test providers, so tests match production behavior.

## 375: How does MSW intercept requests in Node and in the browser?

- **In the browser**, MSW registers a Service Worker (`mockServiceWorker.js`). The worker receives every `fetch` from the page, sends it to the client side of MSW through a message channel, MSW matches it against handlers, and the worker responds with the mock or lets the request go to the network.
- **In Node**, there's no Service Worker. MSW uses the `@mswjs/interceptors` package, which patches Node's `http`/`https` modules, `ClientRequest`, `XMLHttpRequest` and the global `fetch` so requests are captured before they leave the process.

Because both sides use the same handler format with standard `Request` and `Response` objects, the same handlers work in Vitest, Storybook, Playwright (with the browser worker) and development.

## 376: Why are tests with async libraries flaky, and how do you fix them?

Common causes:

- **Not waiting for async UI**: using `getBy` right after an action that triggers a fetch. Use `findBy` or `waitFor`.
- **Shared state between tests**: QueryClient caches, Zustand stores, MSW handler overrides, or i18n language left over. Reset them in `beforeEach`/`afterEach`.
- **Fake timers mixed with real promises**: TanStack Query, user-event and debounce hooks use timers. Configure `userEvent.setup({ advanceTimers: vi.advanceTimersByTime })` and advance timers explicitly.
- **Retries**: TanStack Query retries failed requests 3 times with delays. Turn off retries in tests.
- **Animations**: Motion's exit animations keep elements in the DOM. Mock them or wait for the element to be removed.
- **Order-dependent handlers**: `onUnhandledRequest: 'error'` in MSW catches requests you forgot to mock.

`act` warnings are usually a sign that a state update happened after the test finished checking.

## 377: How do you test virtualized lists and Radix components in jsdom?

jsdom has no layout, so:

- **Virtualized lists** render zero or very few items because all sizes are 0. Mock the size measurement (for TanStack Virtual, mock `getBoundingClientRect` or `offsetHeight`), use the library's test options (react-virtuoso has `initialItemCount`), or test them in a real browser with Vitest Browser Mode or Playwright.
- **Radix and other headless components** may need APIs jsdom lacks: `ResizeObserver`, `DOMRect`, `PointerEvent`, `hasPointerCapture`, `scrollIntoView`. Add simple polyfills in your setup file.
- **Select and dropdown menus** in Radix open on `pointerdown`, so use `user-event` (which fires pointer events), not `fireEvent.click`.
- **Portals** render outside your component's container, so query with `screen`, not `within(container)`.

## 378: How do you set up visual regression testing for a component library?

- **Chromatic** (from the Storybook team) takes screenshots of every story in the cloud, compares them with the approved baseline, and lets reviewers accept or reject changes in the PR.
- **Playwright screenshots** (`await expect(page).toHaveScreenshot()`) can run against Storybook stories or real pages, with baselines stored in the repo.
- **Storybook's Vitest addon** runs stories as tests, and visual checks can be added through the addon ecosystem.

Tips: run in a consistent environment (same OS, fonts, browser version, usually in Docker), turn off animations, use fixed data and dates, and set thresholds for small anti-aliasing differences. Visual tests catch CSS regressions that functional tests miss, especially during big styling migrations.

## 379: How do you handle authentication in Playwright tests efficiently?

Log in once in a setup project, save the browser storage state, and reuse it in all tests:

```ts
// auth.setup.ts
import { test as setup } from "@playwright/test";

setup("authenticate", async ({ page }) => {
  await page.goto("/login");
  await page.getByLabel("Email").fill(process.env.E2E_USER!);
  await page.getByLabel("Password").fill(process.env.E2E_PASS!);
  await page.getByRole("button", { name: "Log in" }).click();
  await page.waitForURL("/dashboard");
  await page.context().storageState({ path: "playwright/.auth/user.json" });
});
```

```ts
// playwright.config.ts
projects: [
  { name: 'setup', testMatch: /.*\.setup\.ts/ },
  { name: 'chromium', use: { storageState: 'playwright/.auth/user.json' }, dependencies: ['setup'] },
],
```

This saves the login time in every test. For different roles, save one state file per role. Don't commit the auth files.

## 380: How do you keep the frontend in sync with the backend API types?

Generate types and clients from the API's schema instead of writing them by hand:

- **OpenAPI/REST**: `openapi-typescript` (types only, used with `openapi-fetch`), `orval` or `@hey-api/openapi-ts` (generate TanStack Query hooks, Zod schemas or MSW mocks), RTK Query's OpenAPI codegen.
- **GraphQL**: GraphQL Codegen with typed document nodes, or `gql.tada` for inferred types without codegen.
- **TypeScript backend in the same repo**: tRPC, or shared Zod schemas.

Run the generator in CI and fail the build if the generated code is out of date. This turns backend changes into compile errors in the frontend, instead of runtime bugs in production.

## 381: How does GraphQL Codegen give you typed queries in React?

You write queries with the `graphql()` function that Codegen generates. It reads your schema and your queries and creates a `TypedDocumentNode` for each one:

```tsx
import { graphql } from "@/gql";
import { useQuery } from "@apollo/client";

const UserQuery = graphql(`
  query User($id: ID!) {
    user(id: $id) {
      id
      name
      email
    }
  }
`);

function User({ id }: { id: string }) {
  const { data } = useQuery(UserQuery, { variables: { id } });
  return <p>{data?.user?.name}</p>;
}
```

`data` and `variables` are typed from the query itself, and only the fields you asked for exist on the type. Fragment masking (with `useFragment`) makes each component only see the fields from its own fragment, which keeps components independent.

## 382: What should you think about when setting up error monitoring with Sentry or similar tools?

- **Source maps**: upload them in CI and don't serve them publicly if you don't want your code readable. Make sure the release version matches.
- **Sampling**: performance traces and session replays cost money and bandwidth. Sample a small percentage, and record 100% of replays only on errors.
- **Privacy**: scrub PII (emails, tokens, form values). Session replay masks text and inputs by default, keep it that way for sensitive pages.
- **Noise**: filter errors from browser extensions, bots and network failures (`ignoreErrors`, `denyUrls`), or you'll miss real issues.
- **Context**: set user id (not email), release, environment and tags like feature flags, so issues can be grouped and reproduced.
- **Alerts**: alert on new issues and regressions, not on every event.

## 383: How do you measure real user performance in a React app?

Use the `web-vitals` library to collect Core Web Vitals from real users and send them to your analytics:

```ts
import { onCLS, onINP, onLCP, onTTFB } from "web-vitals";

function send(metric: { name: string; value: number; id: string }) {
  navigator.sendBeacon("/analytics", JSON.stringify(metric));
}

onLCP(send);
onINP(send);
onCLS(send);
onTTFB(send);
```

The attribution build (`web-vitals/attribution`) tells you which element or interaction caused a bad score. Monitoring tools like Sentry, Datadog or Vercel Analytics collect these automatically. Lab tools like Lighthouse are useful for debugging, but field data shows what users really experience, especially for INP, which libraries with heavy event handlers often hurt.

## 384: What problems do feature flag libraries cause in React apps?

Feature flag SDKs (LaunchDarkly, GrowthBook, Unleash, Statsig, PostHog and others) usually load flags asynchronously, which causes:

- **Flicker**: the old UI shows first, then switches when flags arrive. Fix it by bootstrapping flags from the server (SSR or inline JSON), or waiting for flags before showing the affected part.
- **Hydration mismatches**: the server and client evaluate flags differently. Evaluate on the server and pass the result down.
- **Performance**: big SDKs and streaming connections. Lazy load where possible.
- **Flag debt**: old flags left in code forever. Track and remove them.
- **Testing**: you need to control flags in tests. Wrap the SDK so tests can provide fixed values.

Avoid putting secrets or the full list of unreleased features in client-side flag payloads, since anyone can read them.

## 385: How do third-party scripts like analytics and chat widgets affect React apps, and how do you limit the damage?

They add JavaScript that competes for the main thread, can slow LCP and INP, set cookies, and run with full access to your page.

Ways to limit the impact:

- Load them after the page is interactive (`defer`, `async`, or `next/script` with `strategy="lazyOnload"`).
- Load chat widgets only when the user clicks "Chat" (show a fake button until then).
- Use a server-side tag manager or send events through your own endpoint.
- Restrict them with a Content Security Policy.
- Run some of them in a web worker (Partytown), if the script is compatible.
- Wrap analytics calls in one module so you can change providers and respect consent settings.

Measure the cost with the Performance panel and by comparing Web Vitals with and without the script.

## 386: How do you build forms from a JSON schema in React?

Libraries like `@rjsf/core` (react-jsonschema-form) render forms from a JSON Schema plus a UI schema, with themes for MUI, Ant Design, Chakra and others. This is useful when forms are defined by the backend or by non-developers (admin tools, surveys, plugin settings).

You can also build your own: map field types from a schema to components and use React Hook Form for state, with Zod schemas generated from JSON Schema (or the other way with `z.toJSONSchema`).

Trade-offs: schema-driven forms are great for many similar forms, but custom layouts, cross-field logic and good UX are harder. Many teams use schema-driven forms for admin screens and hand-written forms for user-facing flows.

## 387: How do rich text editors store content, and why does it matter for your app?

Modern editors (ProseMirror/Tiptap, Lexical, Slate) keep content as a structured document tree (nodes like paragraph, heading, list, text with marks), not as raw HTML. `contenteditable` is used only as the input surface.

For your app this means:

- **Store JSON**, not HTML. It's easier to validate, migrate and render in other places (mobile, email), and it can't contain random HTML.
- **Validate on the server**: check the JSON against your allowed node types, because a malicious client can send anything.
- **Render safely**: when converting to HTML for display, use the editor's serializer with a schema, or sanitize the output.
- **Plan for migrations**: when you add or rename node types, you need to update stored documents.

## 388: How do you add real-time collaboration to a React app?

Collaboration (several people editing the same thing) usually uses CRDTs, which merge concurrent changes without conflicts:

- **Yjs** is the most common CRDT library. It has bindings for Tiptap, Lexical, ProseMirror, Monaco and CodeMirror, and providers to sync over WebSocket (`y-websocket`, Hocuspocus) or WebRTC.
- **Hosted services** like Liveblocks or PartyKit give you presence (cursors, who's online), storage and rooms with React hooks.
- **Automerge** is another CRDT library, with a JSON-like model.

Things to plan: auth per document, persistence of updates on the server, presence that shouldn't be stored, offline edits syncing later, and undo that only undoes your own changes. Building on top of a ready provider is much easier than building sync yourself.

## 389: How do you make drag and drop accessible?

Drag and drop is mouse-centric by nature, so you need alternatives:

- **Keyboard support**: pick up with Space or Enter, move with arrow keys, drop with Space, cancel with Escape. dnd-kit has `KeyboardSensor` with `sortableKeyboardCoordinates`.
- **Screen reader announcements**: tell the user what was picked up, where it is over, and where it was dropped. dnd-kit has `announcements` and `screenReaderInstructions` options.
- **Non-drag alternatives**: "Move up/down" buttons or a "Move to..." menu, which are also easier on touch devices.
- **Focus**: keep focus on the moved item after drop.
- **Touch**: use activation constraints (delay or distance) so scrolling doesn't start a drag.

Test with only a keyboard and with a screen reader.

## 390: How do you share code and libraries between React web and React Native?

- **Shared logic**: business logic, API clients, Zod schemas, TanStack Query hooks, Zustand stores, i18n messages and utilities work on both platforms as long as they don't touch the DOM.
- **UI**: `react-native-web` lets React Native components render on the web. Tamagui, NativeWind (Tailwind for RN) and Gluestack aim to share styled components across both.
- **Navigation**: Expo Router works on native and web with file-based routes.
- **Monorepo**: use workspaces (pnpm, Turborepo, Nx) with packages for shared code and separate apps.

Many teams share logic and design tokens but keep separate UI components, because the best UX on web and mobile is often different. Libraries that use DOM APIs (Radix, MUI, most chart libraries) don't work on native.

## 391: How do you plan a major version upgrade of a big library?

1. **Read the migration guide and changelog**, and list the breaking changes that affect you.
2. **Check codemods**: MUI, React Router, TanStack Query, Next.js and React itself provide them.
3. **Check related packages**: for example, a new MUI major needs matching MUI X, or React 19 needs updated testing libraries.
4. **Upgrade the previous major to its latest minor first** and fix deprecation warnings. Many libraries ship "future flags" to adopt new behavior early (React Router did this before v7).
5. **Upgrade on a branch**, run the codemod, fix type errors, run all tests and visual tests.
6. **Roll out gradually** if possible (feature flag or canary deploy), and watch error monitoring.

Upgrading regularly in small steps is much cheaper than skipping several majors.

## 392: What were the main breaking changes in TanStack Query v5?

- **Single object signature only**: `useQuery({ queryKey, queryFn })`. The `useQuery(key, fn, options)` overloads were removed.
- **Renames**: `cacheTime` became `gcTime`. `isLoading` became `isPending` for "no data yet", and `isLoading` now means `isPending && isFetching`. `useErrorBoundary` became `throwOnError`. `keepPreviousData` became `placeholderData: keepPreviousData`.
- **Callbacks removed from `useQuery`**: `onSuccess`, `onError` and `onSettled` were removed from queries (still available on mutations and the global caches).
- **Infinite queries** require `initialPageParam`.
- **Suspense**: new dedicated hooks `useSuspenseQuery`, `useSuspenseInfiniteQuery`, `useSuspenseQueries`.
- **Requires React 18+** because it uses `useSyncExternalStore`.

A codemod handles most of the API changes, but removed query callbacks need manual refactoring (usually into effects, `select` or the global cache callbacks).

## 393: How do you upgrade from React Router v6 to v7 and v8?

React Router v6 to v7 was designed to be non-breaking if you turned on the v6 "future flags" first (like `v7_startTransition`, `v7_relativeSplatPath`, `v7_fetcherPersist`). The steps:

1. Upgrade to the latest v6 and enable all future flags. Fix any warnings.
2. Install `react-router` v7, replace `react-router-dom` imports with `react-router` (the old package still works as a re-export).
3. Optionally adopt framework mode with the Vite plugin if you want SSR, type generation and file routes. This is also the path for Remix v2 apps.

v8 is a smaller release. It raises the baseline (React 19+, modern Node and Vite, ESM only) and makes some v7 future flags (like middleware) the default. If you already adopted the v7 future flags, moving to v8 is mostly a version bump.

## 394: What changed in Redux Toolkit 2.0?

- **Object syntax removed** for `createSlice.extraReducers` and `createReducer`. You must use the builder callback (`builder.addCase(...)`).
- **ESM and modern builds**: packages ship ESM with an `exports` field, and the UMD build was removed. Some old build setups needed updates.
- **`configureStore` middleware and enhancers** options must be callbacks (`middleware: (gDM) => gDM().concat(...)`).
- **Reselect 5** with `weakMapMemoize` by default and dev checks for selectors that always return new references.
- **`combineSlices`** for lazy loading slices, and `createSlice` can now define `selectors` and async thunks inside `reducers` with `create.asyncThunk`.
- **Redux core 5**: action types must be strings, and `createStore` is marked deprecated (to push people to RTK).

react-redux 9 came out at the same time and requires React 18.

## 395: What changed in Zustand v5?

Zustand v5 was a cleanup release:

- Dropped support for React below 18 and TypeScript below 4.5. It uses React's built-in `useSyncExternalStore`.
- Removed the deprecated default export. Use `import { create } from 'zustand'`.
- Custom equality functions were removed from `create`. For that use `createWithEqualityFn` from `zustand/traditional` (which needs `use-sync-external-store`).
- Selectors that return new references now cause infinite loops instead of just extra renders, so you must use `useShallow` (from `zustand/react/shallow`) or stable selectors.
- The `persist` middleware no longer stores the initial state on creation.

Most apps upgrade with a few import changes plus fixing object-returning selectors.

## 396: What changed in Tailwind CSS v4, and what does it mean for React projects?

- **CSS-first configuration**: no `tailwind.config.js` by default. You use `@import "tailwindcss"` and configure with `@theme`, `@custom-variant`, `@utility` and `@plugin` in CSS.
- **New engine**: much faster builds, automatic source detection (no `content` array).
- **Theme values are CSS variables**, so you can use `var(--color-brand-500)` anywhere, including inline styles in React.
- **First-party Vite plugin** (`@tailwindcss/vite`) and PostCSS plugin moved to `@tailwindcss/postcss`.
- **Modern CSS**: cascade layers, `@property`, `color-mix()`, OKLCH colors. It needs modern browsers (Safari 16.4+, Chrome 111+).
- **Some renamed utilities** (for example the shadow, blur and radius scales shifted, `ring` default width changed).

The `@tailwindcss/upgrade` tool migrates most projects. Libraries like shadcn/ui and `tailwind-merge` have v4-specific versions, so update them together.

## 397: What changed in Chakra UI v3, and why was the upgrade hard for many teams?

Chakra v3 was close to a rewrite:

- **New styling engine** (inspired by Panda CSS) with `createSystem`, tokens, semantic tokens and recipes. The old `extendTheme` is gone.
- **Built on Ark UI** for component logic, so many components became compound components (`Dialog.Root`, `Dialog.Trigger`, `Dialog.Content`) instead of single components with many props.
- **Renamed props**: `isDisabled` → `disabled`, `isOpen` → `open`, `colorScheme` → `colorPalette` and many others.
- **Removed packages and features**: framer-motion dependency removed (animations use CSS), some hooks and components removed, and icons moved out.
- **Snippets**: some pre-built compositions are now copied into your project with a CLI.

The upgrade touches almost every component usage. Teams often migrate page by page or stay on v2 for a while.

## 398: How do you build and publish your own React component library?

- **Build**: use a bundler made for libraries (`tsdown`, `tsup`, Vite library mode or Rollup) to output ESM (and CJS only if you need it), plus `.d.ts` type files.
- **package.json**: set `"type": "module"`, an `exports` map with types and import paths, `"sideEffects"` (list CSS files if any), and `"files"` to publish only `dist`.
- **Peer dependencies**: `react` and `react-dom` (and big shared libs like `@tanstack/react-query`) as `peerDependencies`, not `dependencies`, to avoid duplicates.
- **Client directives**: add `'use client'` to entry points that use hooks, and make sure the bundler keeps it.
- **CSS**: ship plain CSS or CSS variables, not runtime CSS-in-JS, so it works with Server Components.
- **Tooling**: Storybook for docs, Vitest for tests, Changesets for versioning and changelogs, and `publint` and `@arethetypeswrong/cli` to check the package before publishing.

## 399: How do you support both controlled and uncontrolled usage in a reusable component?

Use a "controllable state" pattern: if the parent passes `value`, use it; otherwise keep internal state and start from `defaultValue`:

```tsx
import { useState } from "react";

function useControllableState<T>({
  value,
  defaultValue,
  onChange,
}: {
  value?: T;
  defaultValue: T;
  onChange?: (v: T) => void;
}) {
  const [internal, setInternal] = useState(defaultValue);
  const isControlled = value !== undefined;
  const current = isControlled ? value : internal;

  const setValue = (next: T) => {
    if (!isControlled) setInternal(next);
    onChange?.(next);
  };

  return [current, setValue] as const;
}

export function Toggle(props: {
  pressed?: boolean;
  defaultPressed?: boolean;
  onPressedChange?: (p: boolean) => void;
}) {
  const [pressed, setPressed] = useControllableState({
    value: props.pressed,
    defaultValue: props.defaultPressed ?? false,
    onChange: props.onPressedChange,
  });
  return (
    <button aria-pressed={pressed} onClick={() => setPressed(!pressed)}>
      Toggle
    </button>
  );
}
```

Radix and React Aria follow this convention (`value`/`defaultValue`/`onValueChange`). Don't switch between controlled and uncontrolled during the component's life, and warn in development if that happens.

## 400: How does React 19's ref-as-prop change how libraries are written?

Before React 19, function components couldn't receive `ref` as a prop. Libraries had to wrap components in `forwardRef`, which made TypeScript types harder (especially for generic components) and added nesting in DevTools.

In React 19 you can write:

```tsx
function Input({ ref, ...props }: React.ComponentProps<"input">) {
  return <input ref={ref} {...props} />;
}
```

Ref callbacks can also return a cleanup function. Libraries that support both React 18 and 19 often keep `forwardRef` for now, and libraries that need React 19 can drop it. Code that reads `element.ref` from children (like `Slot` components) had to change to `element.props.ref`.

## 401: How do you type TanStack Router so links and navigation are checked everywhere?

Register your router's type once with module declaration merging:

```ts
import { createRouter } from "@tanstack/react-router";
import { routeTree } from "./routeTree.gen";

export const router = createRouter({ routeTree, defaultPreload: "intent" });

declare module "@tanstack/react-router" {
  interface Register {
    router: typeof router;
  }
}
```

After that, every `Link`, `useNavigate`, `redirect`, `useParams` and `useSearch` in the app knows all routes. A wrong path, a missing param or a wrong search param type becomes a TypeScript error. `Route.useParams()` and `Route.useLoaderData()` give exact types for one route. With very many routes this adds TypeScript work, which TanStack mitigates with generated declarations.

## 402: How do routers preload code and data, and what are the trade-offs?

Both React Router and TanStack Router can preload a route's code and data before the user clicks:

- TanStack Router: `defaultPreload: 'intent'` (on hover or focus), `'viewport'` (when the link is visible) or `'render'`. Preloaded data is cached for `defaultPreloadStaleTime`.
- React Router: `<Link prefetch="intent">` in framework mode adds `<link rel="prefetch">` for the module and data.

Trade-offs: preloading makes navigation feel instant, but it can send many requests the user never needed (lists with many links, mobile data), and it can cause server load if the loaders are heavy. Use `intent` for most links, `viewport` only for a few important ones, and make loaders cache-friendly.

## 403: What is render-as-you-fetch and how do data libraries support it?

There are three common patterns:

- **Fetch-on-render**: the component mounts, then starts fetching in `useEffect`. Children fetch only after parents finish, which creates waterfalls.
- **Fetch-then-render**: fetch everything first, then render. No waterfalls, but nothing shows until all data is ready.
- **Render-as-you-fetch**: start fetching before rendering (in the route loader or event handler), and render immediately with Suspense boundaries that show content as each piece of data arrives.

Route loaders (React Router, TanStack Router), `prefetchQuery`/`ensureQueryData`, and React 19's `use(promise)` with Suspense all support render-as-you-fetch. Server Components with streaming apply the same idea on the server.

## 404: How do router navigations work with React transitions?

React Router (with `v7_startTransition`, the default since v7) and TanStack Router wrap navigation state updates in `startTransition`. This means:

- When the new route suspends (lazy code or `useSuspenseQuery`), React keeps the old page on screen instead of showing a Suspense fallback.
- The router exposes a pending state (`useNavigation`, `useRouterState`) so you show a progress bar.
- Urgent updates like typing aren't blocked by rendering the next page.

If you see the whole page flashing to a Suspense fallback on navigation, something is updating outside a transition, or a Suspense boundary is above the routes. Putting boundaries inside the route layouts gives better results.

## 405: How does streaming SSR work in React Router framework mode?

In a loader you return promises without awaiting them. The critical data is awaited, and slow data is streamed later:

```tsx
export async function loader({ params }: Route.LoaderArgs) {
  const product = await getProduct(params.id);
  const reviews = getReviews(params.id);
  return { product, reviews };
}

export default function Product({ loaderData }: Route.ComponentProps) {
  return (
    <>
      <h1>{loaderData.product.name}</h1>
      <Suspense fallback={<p>Loading reviews...</p>}>
        <Await resolve={loaderData.reviews}>
          {(reviews) => <Reviews items={reviews} />}
        </Await>
      </Suspense>
    </>
  );
}
```

The server sends the HTML with the product immediately, and the reviews arrive later in the same response. In React 19 you can also use the `use(promise)` hook instead of `Await`. Promises that never resolve are cut off by a stream timeout, which you can configure.

## 406: Should data loading happen in route loaders or in components?

**Route loaders**:

- Start fetching before the component code even loads, so there are fewer waterfalls.
- Work well with SSR and preloading on hover.
- Make data needs of a page visible in one place.
- But loaders don't re-run when a component deep down needs different data.

**Component-level fetching (TanStack Query hooks)**:

- Each component declares its own data, which is easier to move and reuse.
- Fine-grained caching, refetching and background updates.
- Risk of waterfalls if nested.

A common combination: loaders call `queryClient.ensureQueryData` to start fetching, components call `useQuery`/`useSuspenseQuery` with the same options to read and subscribe. You get early fetching and component-level caching.

## 407: How do the different caching layers in a React app interact?

A single request can be cached in several places:

1. **Browser HTTP cache** (`Cache-Control`, `ETag`).
2. **CDN or edge cache** for public responses.
3. **Server-side caches** (Redis, the framework's data cache, like Next.js `fetch` caching or `use cache`).
4. **Client query cache** (TanStack Query, SWR, Apollo) with its own `staleTime`.
5. **Persisted client cache** (localStorage, IndexedDB).

Problems appear when they disagree: a mutation invalidates TanStack Query, but the refetch hits a stale CDN or HTTP cache and gets old data. Rules of thumb: don't cache private or frequently changing API responses at the CDN, use `no-cache` with `ETag` for data that must be fresh, and know which layer is the source of truth for each type of data.

## 408: What kinds of memory leaks do libraries cause in React apps?

- **Subscriptions not cleaned up**: WebSocket listeners, store subscriptions or event listeners added in effects without cleanup.
- **Third-party instances**: chart, map or editor instances created in an effect and never destroyed (`chart.destroy()`, `map.remove()`, `editor.destroy()`).
- **Global caches growing forever**: a query cache with `gcTime: Infinity` and unique keys per search, or a custom memo cache without limits.
- **Closures keeping big objects alive**: an interval holding a reference to a large dataset.
- **Detached DOM nodes** held by libraries after unmount.

Find them with the Chrome Memory panel: take heap snapshots before and after repeating an action (open and close a page several times), and look at what keeps growing and who holds the references.

## 409: Scenario: the app got noticeably slower after the team added a global state library. How do you investigate?

1. **Reproduce and measure** with React DevTools Profiler (record a slow interaction) and React Scan to see which components re-render.
2. **Look for broad subscriptions**: components that select the whole store (`useStore()` with no selector), or selectors that return new objects or arrays each time.
3. **Check update frequency**: high-frequency values (mouse position, scroll, timers, input text) going through the global store and notifying every subscriber.
4. **Check derived data**: expensive calculations in selectors that run on every store update without memoization.
5. **Look at context**: if the store state is passed through a React context value, every consumer re-renders.

Fixes: narrow selectors, `useShallow` or `createSelector`, keep fast-changing values local, split stores, and memoize heavy child components. Then measure again to confirm the improvement.

## 410: Scenario: you are starting a new internal admin dashboard in React. Which libraries would you pick and why?

A reasonable default stack, with reasons:

- **Vite + React + TypeScript**: no need for SSR or SEO in an internal tool.
- **TanStack Router** (typed search params are great for filters) or **React Router** if the team knows it.
- **TanStack Query** for API data, with types generated from OpenAPI (orval or hey-api).
- **React Hook Form + Zod** for forms.
- **UI**: MUI or Mantine for speed, since admin tools need many ready components (tables, date pickers, dialogs). Or shadcn/ui if there's a custom design.
- **Tables**: MUI X DataGrid, Mantine with TanStack Table, or AG Grid if you need Excel-like features.
- **Charts**: Recharts or the UI kit's chart package.
- **State**: Zustand only if needed.
- **Testing**: Vitest, Testing Library, MSW, Playwright for the main flows.

I'd explain that the choice depends on team experience, design requirements and license budget, not on what is trendy.

## 411: Scenario: your app keeps all API data in Redux with hand-written thunks. How would you migrate to TanStack Query or RTK Query?

1. **Pick the tool**: RTK Query fits if you keep Redux for client state. TanStack Query fits if you want to shrink Redux a lot.
2. **Start with read-only, simple endpoints**: replace a thunk + slice + selectors with one query hook. Delete the old slice when nothing uses it.
3. **Handle shared data**: if other reducers read the API data from Redux, either let them read from the query cache (RTK Query's `select` helpers) or move that logic into components.
4. **Then mutations**: replace thunks with mutations and invalidation, which usually removes manual "update the list after create" code.
5. **Remove loading and error flags** from slices as you go.
6. **Keep tests green**: with MSW and real providers, most integration tests won't need changes.

At the end, Redux usually contains only a little UI state, and some teams then replace it with Zustand or plain React state.

## 412: Scenario: the main JavaScript bundle is 2 MB. How do you reduce it?

1. **Analyze**: run a bundle analyzer and list the largest modules in the initial chunk.
2. **Remove or replace heavy libraries**: Moment → date-fns or Day.js, lodash → `lodash-es` named imports or `es-toolkit`, big icon imports → per-icon imports.
3. **Code split by route**: lazy load every route, so the first load only has the shell and the first page.
4. **Lazy load heavy features**: charts, editors, PDF, maps, spreadsheet parsing, admin-only screens.
5. **Check for duplicates**: two versions of the same library (`npm ls`, analyzer), or both CJS and ESM builds.
6. **Check polyfills and build target**: target modern browsers to avoid unnecessary transforms.
7. **Move work to the server**: Markdown rendering, syntax highlighting or data processing can run on the server or at build time.

Set a size budget in CI (for example with `size-limit`) so it doesn't grow again.

## 413: Scenario: a form with 200 fields lags when typing. How do you fix it?

1. **Profile** to see what re-renders on each keystroke.
2. If it uses Formik or a big `useState` object, every keystroke re-renders the whole form. Moving to React Hook Form with uncontrolled inputs usually fixes most of it.
3. If it already uses RHF, look for `watch()` at the top, `formState` read in the root, or a `Controller` around every field. Move subscriptions into small child components with `useWatch` and `useFormState`.
4. Change validation mode from `onChange` to `onBlur` or `onTouched`, or validate one field instead of the whole schema.
5. Split the form into sections or steps, and memoize sections (or rely on the React Compiler).
6. For very long repeating rows, virtualize them.

Also check expensive things inside fields, like a big select list with thousands of options that should be virtualized or async.

## 414: Scenario: users need to edit a table with 50,000 rows in the browser. What is your approach?

First ask if they really need all 50,000 rows in the browser, or if server-side filtering and pagination would do. If they do:

- Use a grid built for this (AG Grid, MUI X DataGrid Pro or Premium, or TanStack Table + TanStack Virtual with careful code).
- Keep the full data outside React state (a normalized map or the grid's own store), and only send cell updates through React.
- Make editing local and cheap: update one row object, not the whole array.
- Track changed rows and save in batches with optimistic UI and per-row error display.
- Do sorting and filtering in a Web Worker or on the server.
- Make keyboard navigation and copy/paste work like a spreadsheet, since users will expect that.

Load test with realistic data early. Performance problems in grids are much easier to find in week one than right before launch.

## 415: Scenario: after a user edits an item, some parts of the UI still show the old value. How do you debug it?

1. **Find where each part gets its data**: different query keys, a copy in Redux or local state, or props passed from an old parent.
2. **Check invalidation**: does the mutation invalidate all keys that contain the item (list, detail, search results, counts)? Use the devtools to see which queries are stale or fetching.
3. **Check for copied state**: `useState(props.item)` only uses the initial value, so it won't update when the prop changes. Use the prop directly, or reset with a `key`.
4. **Check caches outside the client**: HTTP or CDN caching can return old data even after a refetch.
5. **Check optimistic update logic**: maybe it updates the list but not the detail cache, or the rollback ran wrongly.

A query key factory plus invalidating by a shared prefix usually fixes this class of bug for good.

## 416: Scenario: you added a date library and now the app has hydration errors. What is going on?

Most likely the server and the browser format dates differently:

- The server runs in UTC and the browser in the user's time zone, so `format(date, 'HH:mm')` gives different strings.
- The server's default locale differs from the browser's (`toLocaleDateString()` without an explicit locale).
- Relative times ("3 minutes ago") are computed with different "now" values.

Fixes: pass the time zone and locale explicitly and use the same values on both sides (for example, the user's time zone from a cookie or profile), format relative times only on the client after mount, or render dates in a client-only component. For a single timestamp where a small difference is fine, `suppressHydrationWarning` on that element is acceptable.

## 417: Scenario: a security review found XSS in the comments section, which supports Markdown. How do you fix it?

1. **Find how Markdown is rendered**. Common causes: a Markdown library that converts to HTML and then `dangerouslySetInnerHTML` without sanitizing, `rehype-raw` turned on, or custom renderers that put user values into `href` without checks.
2. **Fix rendering**: use `react-markdown` without raw HTML, or sanitize the HTML output with DOMPurify or `rehype-sanitize` with a strict allowlist.
3. **Check links and images**: only allow `http`, `https` and `mailto` URLs, and add `rel="noopener noreferrer"` for external links.
4. **Sanitize on the server too** if the HTML is stored or used elsewhere (emails, mobile).
5. **Add a Content Security Policy** without `unsafe-inline` scripts, to limit damage from any future bug.
6. **Add tests** with known XSS payloads (`<img src=x onerror=...>`, `[x](javascript:alert(1))`).
7. **Check for exploitation** in stored comments and clean them.

## 418: Scenario: a UI library your app depends on heavily is no longer maintained. What is your plan?

1. **Assess the risk**: does it block a React upgrade, have known security issues, or just lack new features? If it still works, you have time.
2. **Measure usage**: how many components and files use it. A wrapper layer makes this much easier.
3. **Pick a replacement** that fits your design: a maintained UI kit, or headless primitives with your own styles.
4. **Create wrapper components** with your own API (`<AppSelect>`, `<AppDialog>`), first implemented with the old library. Then switch the implementation inside the wrapper, one component at a time.
5. **Use visual and E2E tests** to catch changes in behavior.
6. **As a stopgap**, fork the library or patch it with `patch-package` for urgent fixes.

Treat it as planned technical work with milestones, not a weekend rewrite.

## 419: Scenario: two UI kits are used in the same app and it looks inconsistent. What do you do?

1. **Understand why**: maybe a team needed a component the main kit didn't have, or a migration was started and never finished.
2. **Choose the target kit** based on coverage, design fit and the team's skills.
3. **Share tokens** (colors, spacing, radius, typography) as CSS variables and configure both kits with them, so they look closer right away.
4. **Fix overlay conflicts**: z-index scales, portals, focus traps, global CSS resets that fight each other.
5. **Plan the migration** page by page or component by component, using wrappers. Block new usage of the old kit with a lint rule (`no-restricted-imports`).
6. **Watch the bundle**: two kits mean two sets of code, often two styling engines.

The key is making one decision and enforcing it in code review and lint, otherwise the mix grows.

## 420: Scenario: you need to make an app work for right-to-left languages like Arabic. What is involved with libraries?

- **Set `dir="rtl"`** on `<html>` (and `lang`) when the locale is RTL.
- **CSS**: use logical properties (`margin-inline-start`, `padding-inline-end`, `text-align: start`) instead of left/right. Tailwind has `ms-*`, `me-*`, `ps-*`, `pe-*` and `rtl:` variants.
- **UI kits**: MUI needs `direction: 'rtl'` in the theme plus an RTL Emotion cache (`stylis-plugin-rtl`). Ant Design has `ConfigProvider direction="rtl"`. Radix and React Aria read `dir` (through a `DirectionProvider` for Radix).
- **Icons**: flip directional icons (arrows, "back") but not others (checkmarks, logos).
- **i18n**: numbers, dates and plurals per locale with `Intl`, and avoid concatenating strings.
- **Charts, carousels, sliders**: check they support RTL direction.

Test with real RTL text, not just mirrored English, and get feedback from native speakers.

## 421: Scenario: tests using MSW and TanStack Query pass alone but fail when run together. What is wrong?

Most likely shared state between tests:

- **One shared QueryClient**: cached data from one test is reused in another. Create a new client per test.
- **MSW handler overrides not reset**: a `server.use()` from one test leaks into the next. Call `server.resetHandlers()` in `afterEach`.
- **Retries**: an error test retries 3 times and overlaps with the next test. Turn off retries.
- **Timers**: fake timers enabled in one test and not restored.
- **Module-level stores** (Zustand, i18n language) not reset.
- **Unhandled requests**: set `onUnhandledRequest: 'error'` to see requests going to unexpected handlers.

Running with `--sequence.shuffle` in Vitest helps find order-dependent tests.

## 422: Scenario: many requests fail at once with 401 because the token expired, and your app sends ten refresh requests. How do you fix it?

Make the refresh "single flight": the first 401 starts the refresh, and every other request waits for the same promise:

```ts
let refreshPromise: Promise<string> | null = null;

async function getFreshToken() {
  refreshPromise ??= refreshAccessToken().finally(() => {
    refreshPromise = null;
  });
  return refreshPromise;
}
```

In the HTTP client's 401 handler, call `getFreshToken()`, retry the original request once with the new token, and log out if the refresh fails. You can also refresh shortly before expiry (based on the token's `exp`) to avoid the 401 storm altogether. Also coordinate across browser tabs (`BroadcastChannel` or a lock with `navigator.locks`), or each tab will refresh separately and may invalidate each other's refresh tokens if rotation is on.

## 423: Scenario: you need an offline-first web app for field workers. Which libraries and patterns would you consider?

- **Local data store**: IndexedDB through Dexie (with `useLiveQuery` for React) or a sync engine (PowerSync, ElectricSQL, RxDB, Replicache-style tools) that syncs a local database with the server.
- **Service worker**: Workbox or `vite-plugin-pwa` to cache the app shell and assets so it loads without network.
- **Mutations queue**: store changes locally with timestamps and ids, sync when back online, handle conflicts (last-write-wins, merge rules, or CRDTs for shared documents).
- **TanStack Query** with a persister and paused mutations can work for simpler cases.
- **UI**: show sync status, pending changes and conflicts clearly.
- **Storage limits**: request persistent storage (`navigator.storage.persist()`) and handle eviction.

Test with the network actually off, on real devices, and with long offline periods.

## 424: Scenario: you are building a real-time dashboard with live charts. How do you keep it fast?

- **Throttle updates**: data may arrive many times per second, but users can't read faster than a few updates per second. Buffer messages and flush every 250-1000 ms.
- **Keep high-frequency data out of React state** where possible. Update charts through their imperative API (ECharts `setOption`, uPlot `setData`) or with refs.
- **Use Canvas-based charts** for many points, and keep a fixed window of data (drop old points).
- **Split state** so one widget's update doesn't re-render the others (separate stores or selectors).
- **Pause updates for hidden tabs** (`document.visibilityState`) and off-screen widgets.
- **Use `startTransition`** for non-urgent re-renders so interactions stay responsive.

Measure with the Performance panel during real load, and watch memory over hours, since dashboards stay open all day.

## 425: Scenario: you want to upgrade to React 19, but one library blocks you. What are your options?

1. **Check for a newer version** or a beta that supports React 19. Many libraries just needed a peer dependency update.
2. **Check if it actually breaks**, or if only the peer dependency range is wrong. You can use `overrides` (npm) or `peerDependencyRules` (pnpm) to test it, then run your tests.
3. **Patch it** with `patch-package` or `pnpm patch` if the fix is small (often removing `defaultProps`, `findDOMNode` or `element.ref` usage), and send the fix upstream.
4. **Replace it** with a maintained alternative, ideally behind a wrapper.
5. **Isolate it**: if it's only used on one page, migrate that page or lazy load an alternative.

Don't hold the whole app on an old React for one dependency for too long, because the gap only gets bigger.

## 426: Scenario: you enabled the React Compiler and a few components stopped updating. How do you handle it?

1. **Identify the components** (the bug reports or tests will show where) and check if they use libraries that return mutable objects (form libraries' `watch`, table instances, some MobX patterns) or code that breaks the Rules of React (mutating props, reading refs in render).
2. **Run the ESLint React Compiler rules** to find violations.
3. **Fix the code**: use subscription hooks (`useWatch`), avoid mutating values that React compares, and don't read `ref.current` during render.
4. **Opt out where needed**: add `'use no memo'` at the top of the component as a temporary fix, with a comment explaining why.
5. **Update libraries**: many have released compiler-compatible versions.

You can also roll out the compiler gradually (annotation mode or per directory) to limit risk.

## 427: Scenario: a context-based library doesn't work in the Next.js App Router. How do you integrate it?

The error is usually "createContext only works in Client Components" or hooks being called in a Server Component. To fix it:

1. Create a `providers.tsx` file with `'use client'` that renders the library's providers.
2. Use it in the root `layout.tsx` to wrap `children`. Server Components can be passed as children to client components, so the rest of the app stays server-rendered.
3. Use the library's hooks only inside client components.
4. If the library touches `window` on import, load it with `dynamic(..., { ssr: false })` inside a client component.
5. If the library has a global singleton (a store), create it per request in the provider, so users don't share state on the server.

Keep the provider as deep in the tree as possible if only some routes need it.

## 428: Scenario: an accessibility audit fails on your custom dropdowns. How do you fix them?

Typical findings: no keyboard support, missing roles, focus lost, screen readers not announcing the selected option.

Options:

1. **Replace the custom code with a headless library** (Radix Select, Base UI, React Aria `Select`/`ComboBox`, Downshift). They implement the WAI-ARIA patterns correctly, and you keep your styles.
2. If you must keep the custom code, follow the ARIA Authoring Practices for listbox or combobox: correct roles, `aria-expanded`, `aria-activedescendant` or roving focus, arrow keys, Home/End, typeahead, Escape, and returning focus to the trigger.
3. **Consider the native `<select>`** for simple cases. It is accessible and works well on mobile, and new CSS (`appearance: base-select`) allows custom styling in supporting browsers.

Add automated checks (axe in tests or Storybook) and manual testing with a screen reader to prevent regressions.

## 429: Scenario: several apps in your company need a shared design system. How do you build it?

- **Foundation**: design tokens (colors, spacing, typography) as the source of truth, generated to CSS variables, Tailwind theme and TS constants.
- **Components**: built on headless primitives (Radix, Base UI or React Aria) for accessibility, styled with zero-runtime CSS (CSS modules, Tailwind or vanilla-extract), so they work in SPAs and Server Components.
- **Packaging**: a monorepo package with ESM output, `react` as peer dependency, `'use client'` where needed, and semantic versioning with Changesets.
- **Docs and tests**: Storybook as the catalog, interaction and accessibility tests, visual regression with Chromatic or Playwright.
- **Adoption**: codemods for breaking changes, a clear deprecation policy, and a contribution process so product teams don't fork it.

Alternatively, a shadcn-style registry lets apps copy and own components, which gives teams more freedom but makes consistency harder to enforce.

## 430: Scenario: in development every request is sent twice when a page loads. Is this a bug?

Probably not. In development, React StrictMode mounts components, unmounts them and mounts them again, to help find effects without proper cleanup. A `fetch` in `useEffect` runs twice. This doesn't happen in production builds.

What to do:

- Don't remove StrictMode. Make effects safe instead: abort the first request in cleanup or ignore its result.
- Better, use a data library. TanStack Query, SWR and RTK Query dedupe requests for the same key, so you only see one network call.
- If you see doubled requests in production, look for real causes: two components fetching the same thing with different keys, a key that changes on every render (like a new object or `Date.now()`), or a refetch triggered by window focus.

## 431: Scenario: after logout, the next user sees data from the previous user. How do you fix it?

Client-side caches and stores live in memory (and sometimes in storage) and don't know about logout. On logout, clear everything:

```ts
async function logout() {
  await api.logout();
  queryClient.clear();
  useAppStore.setState(initialAppState, true);
  store.dispatch(api.util.resetApiState());
  localStorage.removeItem("persisted-cache");
  router.navigate("/login", { replace: true });
}
```

Also include the user id in keys for persisted caches, and for simple apps do a full reload after logout (`window.location.assign('/login')`), which clears all memory. Check service worker caches too if they cache API responses. On the server side, make sure CDN or SSR caches never store per-user responses under shared keys.

## 432: Scenario: a search page shows results for an old query when the user types fast. How do you fix it?

The responses arrive out of order: the request for "rea" finishes after the request for "react" and overwrites it. Fixes:

- **Use a query library** keyed by the search term (`['search', query]`). The UI always reads the entry for the current key, so old responses can't overwrite new ones.
- **Abort old requests** with `AbortController` (TanStack Query passes `signal` to `queryFn`).
- **Debounce** the input so fewer requests are sent.
- **Use `placeholderData: keepPreviousData`** so the list doesn't flash empty between queries.
- In hand-written effects, use an `ignore` flag in the cleanup so stale responses are dropped.

Also cancel on the server if possible (search is often expensive), and consider `useDeferredValue` if rendering the results list is the slow part.

## 433: Scenario: you need an infinite feed with virtualization that keeps the scroll position when the user goes back. How do you build it?

- **Data**: `useInfiniteQuery` keeps all loaded pages in the cache, so coming back shows the same items without refetching (set a reasonable `staleTime`).
- **Virtualization**: TanStack Virtual or react-virtuoso with dynamic measurement.
- **Saving position**: store the scroll offset (or the first visible item index) and measured sizes when leaving, keyed by the route. react-virtuoso has `getState`/`restoreStateFrom`. TanStack Virtual supports `initialOffset` and `initialMeasurementsCache`.
- **Router**: disable the router's own scroll restoration for this page (or let it handle the window scroll if the list uses the window as scroll container).
- **Loading more**: trigger `fetchNextPage` when the last virtual item is near the end.

Test with images that load late, since they change heights and shift the restored position.

## 434: Scenario: AG Grid Enterprise would cost a lot for your team. How do you decide whether to pay or build?

Compare honestly:

- **Which features you need**: row grouping, pivoting, Excel export, server-side row model, tree data, range selection. If you only need sorting, filtering, editing and virtualization, the free Community edition, MUI X DataGrid or TanStack Table may be enough.
- **Build cost**: a grid with keyboard navigation, copy/paste, column resizing, grouping and accessibility is months of work, plus maintenance. Developer time usually costs more than the license.
- **Alternatives**: MUI X Pro/Premium, other commercial grids, or open source options.
- **Risk**: lock-in to a vendor's API versus maintaining your own grid.

Build a small prototype of the hardest requirement with the free tools first. If it gets complicated fast, the license is usually worth it.

## 435: Scenario: memory use grows steadily in a single page app that users keep open all day. What do you check?

- **Query caches**: `gcTime: Infinity` or many unique keys (search terms, timestamps in keys) keep old data forever. Use sensible `gcTime` values.
- **Global stores**: arrays that only grow (logs, notifications, chat messages). Cap them.
- **Subscriptions and intervals** without cleanup, especially in components that mount and unmount often.
- **Library instances** (charts, maps, editors) not destroyed on unmount.
- **Event listeners on `window`/`document`** added repeatedly.
- **Monitoring tools**: session replay or logging libraries buffering a lot of data.

Use the Chrome Memory panel: take a heap snapshot, repeat the suspicious action several times, take another one, and compare. Look at "Detached" DOM nodes and which objects keep growing.

## 436: Scenario: your team uses Formik and asks whether to migrate to React Hook Form. What do you advise?

Things to weigh:

- **Pain level**: if forms are small and fast enough, migrating everything has little value. If big forms lag or the team fights Formik's re-render behavior, migration helps.
- **Maintenance**: Formik gets few updates, so new React features and fixes may not come.
- **Effort**: the APIs are different (`register`/`Controller` vs `Field`/`useField`). Validation schemas (Yup) can be reused through `@hookform/resolvers/yup`.
- **Strategy**: write new forms with React Hook Form, migrate the slowest or most-changed forms first, and leave stable old forms alone until they need work.

A shared set of form field components that hide the library details makes the migration much easier and protects you from the next change.

## 437: Scenario: someone wants to add a package to solve a small problem, like formatting bytes or checking if a value is empty. How do you decide?

Ask:

- **How much code is it?** If it's 10 lines you understand, write it yourself with a test.
- **Is it hard to get right?** Date parsing, sanitizing HTML, CSV parsing, accessibility widgets: use a library. Formatting bytes or `isEmpty`: probably not.
- **Is the package healthy?** Maintained, typed, no huge dependency tree (`npm ls` or `npx why`), reasonable size.
- **Does the platform already do it?** `Intl.NumberFormat` (with `unit: 'byte'`), `structuredClone`, `Object.groupBy`, `crypto.randomUUID()`, `URLSearchParams`.

Every dependency is code you don't control that can break, get compromised or be abandoned. Tiny packages give little value for that risk.

## 438: How do you evaluate the bundle cost of a UI kit before adopting it?

- **Build a small prototype** with the components you'll actually use (buttons, inputs, dialog, select, table) and run a bundle analyzer. Docs and bundlephobia numbers for the whole package are misleading.
- **Check the styling engine**: runtime CSS-in-JS adds a fixed cost (Emotion is around 10+ KB gzipped) plus render-time work.
- **Check tree shaking**: import one component and see if the whole library is included.
- **Check dependencies**: date libraries, icon sets and animation libraries that come along.
- **Check CSS size**: a big global stylesheet can be as costly as JS.
- **Look at real metrics** (LCP, INP) on a mid-range phone, not just bytes.

Compare this cost with the time it saves. For internal tools a bigger kit is often fine; for public, mobile-heavy sites, it matters more.

## 439: How do you handle global CSS and resets from several libraries without conflicts?

- **Use cascade layers**: put library CSS in lower-priority layers and your own styles in higher ones, so you win without `!important`:

```css
@layer reset, vendor, components, utilities;
@import "some-lib/styles.css" layer(vendor);
```

Tailwind v4 already uses layers, and MUI and Mantine can be configured to output into a layer.

- **Load one reset** (CssBaseline, Tailwind preflight or modern-normalize), not one per library.
- **Control import order** in a single entry file.
- **Scope third-party CSS** to a wrapper class when it has global selectors (like `h1` or `button` styles).

When styles look different in production than in development, it's often CSS order changing because of code splitting, so layers make the result predictable.

## 440: How do you write a custom hook library that works well with SSR, StrictMode and concurrent rendering?

- **No side effects during render**: subscribe and start work in effects, or use `useSyncExternalStore` for external sources.
- **SSR-safe defaults**: don't touch `window`, `document` or `localStorage` during render. Use `getServerSnapshot` or return a default and update after mount.
- **Clean up everything**: every subscription, timer and listener returns a cleanup, so StrictMode's double mount doesn't leak.
- **Stable outputs**: return memoized callbacks and objects, so consumers can use them in dependency arrays without loops.
- **Use `useId`** for ids, not counters or random values.
- **Read the latest callbacks without re-subscribing**: store them in a ref updated in an effect, or use `useEffectEvent` (stable in React 19.2) for event-like logic inside effects.
- **Test in StrictMode**, with SSR (`renderToString`) and with the React Compiler enabled.

## 441: How do you keep a large set of third-party dependencies up to date without breaking things?

- **Automate**: Renovate or Dependabot opens PRs. Group related packages (all `@tanstack/*`, all `@mui/*`, all testing libraries) and auto-merge patch updates that pass CI.
- **Good test coverage** is what makes updates safe: unit, integration, E2E and visual tests.
- **Read changelogs for minors and majors**, and plan majors as normal tasks with an owner.
- **Upgrade often** in small steps. Falling several majors behind makes each upgrade a project.
- **Remove unused dependencies** regularly with tools like `knip`.
- **Track deprecations**: watch for warnings in the console and in builds.
- **Lockfile maintenance**: periodically refresh the lockfile to pick up transitive fixes.

## 442: How do you choose between building a feature with a library or with React and browser APIs only?

Modern browsers cover a lot of what libraries used to:

- `<dialog>` and the Popover API for modals and popovers (with the top layer, so no z-index fights).
- CSS scroll snap for carousels, CSS anchor positioning for tooltips (where supported), container queries for responsive components.
- `Intl` for formatting dates, numbers, plurals, lists and relative time.
- View Transitions API (and React's experimental `<ViewTransition>` component) for page transitions.
- Native form validation plus React 19 form actions for simple forms.

Use native features when browser support matches your users and the native behavior is good enough. Use a library when you need consistent behavior everywhere, complex accessibility (comboboxes, date pickers, grids), or features the platform lacks. Check support on caniuse and test on your target browsers.

## 443: How does the React ecosystem handle animations between pages, and what are the options?

- **Motion**: `AnimatePresence` around the routes with a `key` based on the location, so the old page animates out and the new page in. Layout animations with `layoutId` can morph shared elements.
- **View Transitions API**: the browser takes snapshots before and after a DOM change and animates between them. React Router supports it with a `viewTransition` prop on `Link`/`navigate`, and React has an experimental `<ViewTransition>` component that works with transitions and Suspense.
- **CSS only**: simple fade or slide with keyframes on mount.

The View Transitions API is lighter (no JS animation library) and handles cross-page element morphing nicely, but browser support and React integration are still settling. Motion gives more control and works everywhere. Always respect reduced motion settings.

## 444: How do you handle images efficiently in React apps with or without a framework?

- **Frameworks**: Next.js `next/image` handles resizing, modern formats (WebP, AVIF), `srcset`, lazy loading and avoiding layout shift. Other frameworks and image CDNs (Cloudinary, imgix, Vercel or Netlify image services) have similar components.
- **Without a framework**: use `<img loading="lazy" decoding="async" width height>`, `srcset`/`sizes` for responsive images, and `fetchpriority="high"` on the LCP image. Libraries like `@unpic/react` generate the right attributes for many image CDNs.
- **Placeholders**: blurhash or thumbhash libraries, or low-quality placeholders, to avoid empty boxes.
- **Build-time optimization**: Vite plugins like `vite-imagetools` or `vite-plugin-image-optimizer` for static images.

Always set dimensions (or `aspect-ratio`) to prevent layout shift, and never lazy load the LCP image.

## 445: How do you approach state management in a local-first React app?

In local-first apps the main copy of the data lives on the device and syncs with the server in the background. That changes the library choices:

- **Data**: a local database (IndexedDB through Dexie, SQLite through WASM, or a sync engine like Replicache-style tools, PowerSync, ElectricSQL, Zero or Jazz) with reactive queries that update React when data changes.
- **Sync**: the sync engine handles pushing changes, pulling updates and resolving conflicts. CRDT libraries (Yjs, Automerge) for collaborative documents.
- **UI**: reads are instant from the local database, so you rarely need loading states or a server cache library like TanStack Query for that data.
- **Auth and permissions**: the server must still check every change it receives.

The trade-offs are complexity of sync, schema migrations on the device, and storage limits in the browser. It fits best for productivity apps where speed and offline use matter.

## 446: How do you design a hooks API for a library you publish?

- **Small, focused hooks** that do one thing (`useCombobox`, `useMediaQuery`) rather than one huge hook.
- **Prop getters** (`getInputProps()`, `getItemProps({ item })`) that return props to spread and merge the user's own handlers, like Downshift and Floating UI do.
- **Controlled and uncontrolled support** (`value`/`defaultValue`/`onChange`).
- **Stable references** for returned functions and objects.
- **TypeScript generics** so item types flow through.
- **No hidden global state**. Allow a provider or explicit instance when needed (for SSR and tests).
- **SSR safe** and **StrictMode safe** by design.
- **Escape hatches**: expose refs or the underlying instance for advanced use.

Write the docs and examples while designing the API. If an example is hard to explain, the API probably needs work.

## 447: How do you decide whether to use a framework (Next.js, React Router framework mode, TanStack Start) or a plain SPA with libraries?

Use a **framework** when:

- You need SEO, fast first loads on mobile, or social previews (SSR or static generation).
- You want server code next to UI (server functions, Server Components, loaders and actions).
- You want routing, code splitting, data loading and bundling decided for you.

Use a **plain SPA** (Vite + router + data library) when:

- It's an internal tool or a dashboard behind login where SEO doesn't matter.
- You already have a separate backend and want a static deploy (CDN only, no Node server).
- The team prefers fewer moving parts.

Either way, many of the same libraries apply (TanStack Query, React Hook Form, UI kits). The main difference is where data loading and rendering happen.

## 448: What questions would you ask when reviewing a pull request that adds a new dependency?

- **Why** is it needed, and was a built-in or existing dependency considered?
- **Size**: how much does it add to the bundle (show the analyzer diff)? Is it loaded on the critical path?
- **Health**: maintenance activity, number of maintainers, open security issues, download trend.
- **Compatibility**: React version, SSR or Server Components, TypeScript types, ESM.
- **License**: compatible with how we ship the product?
- **Transitive dependencies**: does it pull in a large tree or duplicate something we already have?
- **Exit plan**: is it used behind a wrapper so we could replace it later?
- **Security**: does it run install scripts, touch HTML or need network access?

A short checklist in the PR template makes these questions routine instead of personal.

## 449: How do you explain the overall React library ecosystem to a new developer joining the team?

I'd explain it in layers, from the base up:

1. **React** renders UI and manages local state, nothing more.
2. **Build tool or framework** (Vite, Next.js, React Router framework mode) handles bundling, routing and maybe server rendering.
3. **Data**: a server cache library (TanStack Query here) for anything from the API. We don't copy API data into stores.
4. **Client state**: `useState` first, then a small store (Zustand here) for truly global UI state, and the URL for filters.
5. **Forms**: React Hook Form with Zod schemas shared with the backend.
6. **UI**: our design system components, built on headless primitives and Tailwind.
7. **Testing**: Vitest and Testing Library with MSW, Playwright for main flows.

Then I'd point to our wrappers and conventions, and explain why each choice was made, so they can judge when a different tool makes sense.

## 450: What does a healthy library strategy look like for a long-lived React project?

- **Few, well-chosen dependencies**, each with a clear job and an owner on the team.
- **Use the platform and React first** (native elements, `Intl`, React 19 features), and add libraries for the hard parts.
- **Separate server, URL, form and client state**, each with the right tool.
- **Wrap libraries that are likely to change** (HTTP, dates, analytics, UI primitives) behind your own modules.
- **Prefer libraries that fit the direction of React**: Server Components compatible, zero-runtime styling, `useSyncExternalStore` based stores, Standard Schema support.
- **Keep everything updated** in small steps with automation and good tests.
- **Watch the bundle and Web Vitals** in CI.
- **Review new dependencies** with a checklist covering size, health, license and security.
- **Plan migrations early** when a library loses maintenance, instead of waiting for it to block an upgrade.

The goal is a stack the team understands and can change piece by piece, rather than one that has to be rewritten every few years.
