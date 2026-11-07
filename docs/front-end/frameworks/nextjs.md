# Next.js Interview Questions and Answers

_Last updated: October 28, 2026_

450 Next.js interview questions with answers, split into three levels: easy, moderate and advanced. The answers are written for Next.js 16 and the App Router, with notes on the Pages Router where it still matters.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is Next.js?](#1-what-is-nextjs)
- [2: What are the main features of Next.js?](#2-what-are-the-main-features-of-nextjs)
- [3: What is the difference between React and Next.js?](#3-what-is-the-difference-between-react-and-nextjs)
- [4: How do you create a new Next.js project?](#4-how-do-you-create-a-new-nextjs-project)
- [5: What is the latest major version of Next.js and what does it require?](#5-what-is-the-latest-major-version-of-nextjs-and-what-does-it-require)
- [6: What scripts are in a default Next.js `package.json`?](#6-what-scripts-are-in-a-default-nextjs-packagejson)
- [7: What is the App Router?](#7-what-is-the-app-router)
- [8: What is the Pages Router?](#8-what-is-the-pages-router)
- [9: Can you use the App Router and Pages Router in the same project?](#9-can-you-use-the-app-router-and-pages-router-in-the-same-project)
- [10: How does file-based routing work in the App Router?](#10-how-does-file-based-routing-work-in-the-app-router)
- [11: What is `page.tsx`?](#11-what-is-pagetsx)
- [12: What is `layout.tsx`?](#12-what-is-layouttsx)
- [13: What is the root layout and why is it required?](#13-what-is-the-root-layout-and-why-is-it-required)
- [14: What are nested layouts?](#14-what-are-nested-layouts)
- [15: What is the `public` folder used for?](#15-what-is-the-public-folder-used-for)
- [16: How do you navigate between pages in Next.js?](#16-how-do-you-navigate-between-pages-in-nextjs)
- [17: Why use `Link` instead of a normal `<a>` tag?](#17-why-use-link-instead-of-a-normal-a-tag)
- [18: What is prefetching in Next.js?](#18-what-is-prefetching-in-nextjs)
- [19: How do you create a dynamic route?](#19-how-do-you-create-a-dynamic-route)
- [20: Why is `params` a Promise?](#20-why-is-params-a-promise)
- [21: How do you read query string values (search params) in a page?](#21-how-do-you-read-query-string-values-search-params-in-a-page)
- [22: What are Server Components?](#22-what-are-server-components)
- [23: What are Client Components?](#23-what-are-client-components)
- [24: What does `"use client"` do?](#24-what-does-use-client-do)
- [25: When should you use a Server Component and when a Client Component?](#25-when-should-you-use-a-server-component-and-when-a-client-component)
- [26: Can you use `useState` in a Server Component?](#26-can-you-use-usestate-in-a-server-component)
- [27: What is server-side rendering (SSR)?](#27-what-is-server-side-rendering-ssr)
- [28: What is static site generation (SSG)?](#28-what-is-static-site-generation-ssg)
- [29: What is client-side rendering (CSR)?](#29-what-is-client-side-rendering-csr)
- [30: What is hydration?](#30-what-is-hydration)
- [31: What is a hydration error?](#31-what-is-a-hydration-error)
- [32: How do you add global CSS?](#32-how-do-you-add-global-css)
- [33: What are CSS Modules?](#33-what-are-css-modules)
- [34: How do you use Tailwind CSS in Next.js?](#34-how-do-you-use-tailwind-css-in-nextjs)
- [35: Does Next.js support Sass?](#35-does-nextjs-support-sass)
- [36: How do you add an image in Next.js?](#36-how-do-you-add-an-image-in-nextjs)
- [37: What are the benefits of the `next/image` component?](#37-what-are-the-benefits-of-the-nextimage-component)
- [38: Why do you need `width` and `height` on `next/image`?](#38-why-do-you-need-width-and-height-on-nextimage)
- [39: How do you use a remote image with `next/image`?](#39-how-do-you-use-a-remote-image-with-nextimage)
- [40: What is the `fill` prop on `next/image`?](#40-what-is-the-fill-prop-on-nextimage)
- [41: How do you load an important image right away instead of lazy loading it?](#41-how-do-you-load-an-important-image-right-away-instead-of-lazy-loading-it)
- [42: How do you add fonts in Next.js?](#42-how-do-you-add-fonts-in-nextjs)
- [43: How do you use a local font file?](#43-how-do-you-use-a-local-font-file)
- [44: What is the benefit of `next/font`?](#44-what-is-the-benefit-of-nextfont)
- [45: How do you set the page title and description?](#45-how-do-you-set-the-page-title-and-description)
- [46: How do you add a favicon?](#46-how-do-you-add-a-favicon)
- [47: What is `loading.tsx`?](#47-what-is-loadingtsx)
- [48: What is `error.tsx`?](#48-what-is-errortsx)
- [49: What is `not-found.tsx`?](#49-what-is-not-foundtsx)
- [50: How do you show a 404 page from code?](#50-how-do-you-show-a-404-page-from-code)
- [51: How do you redirect a user in a Server Component?](#51-how-do-you-redirect-a-user-in-a-server-component)
- [52: What is the difference between `redirect()` and `permanentRedirect()`?](#52-what-is-the-difference-between-redirect-and-permanentredirect)
- [53: How do you navigate from code in a Client Component?](#53-how-do-you-navigate-from-code-in-a-client-component)
- [54: What methods does `useRouter` provide?](#54-what-methods-does-userouter-provide)
- [55: What is the difference between `next/router` and `next/navigation`?](#55-what-is-the-difference-between-nextrouter-and-nextnavigation)
- [56: How do you get the current path in a Client Component?](#56-how-do-you-get-the-current-path-in-a-client-component)
- [57: How do you read search params in a Client Component?](#57-how-do-you-read-search-params-in-a-client-component)
- [58: How do you read route params in a Client Component?](#58-how-do-you-read-route-params-in-a-client-component)
- [59: What are environment variables in Next.js?](#59-what-are-environment-variables-in-nextjs)
- [60: What does the `NEXT_PUBLIC_` prefix do?](#60-what-does-the-next_public_-prefix-do)
- [61: What `.env` files does Next.js support, and in what order are they loaded?](#61-what-env-files-does-nextjs-support-and-in-what-order-are-they-loaded)
- [62: What is a Route Handler?](#62-what-is-a-route-handler)
- [63: Which HTTP methods do Route Handlers support?](#63-which-http-methods-do-route-handlers-support)
- [64: Can `route.ts` and `page.tsx` be in the same folder?](#64-can-routets-and-pagetsx-be-in-the-same-folder)
- [65: What are API Routes in the Pages Router?](#65-what-are-api-routes-in-the-pages-router)
- [66: What is `next.config.ts`?](#66-what-is-nextconfigts)
- [67: What is Turbopack?](#67-what-is-turbopack)
- [68: How do you use webpack instead of Turbopack?](#68-how-do-you-use-webpack-instead-of-turbopack)
- [69: Does Next.js support TypeScript?](#69-does-nextjs-support-typescript)
- [70: What is the `src` folder in a Next.js project?](#70-what-is-the-src-folder-in-a-nextjs-project)
- [71: What is the `@/` import alias?](#71-what-is-the--import-alias)
- [72: What is a route segment?](#72-what-is-a-route-segment)
- [73: What special files can a route segment have?](#73-what-special-files-can-a-route-segment-have)
- [74: In what order are the special files rendered?](#74-in-what-order-are-the-special-files-rendered)
- [75: What is a route group?](#75-what-is-a-route-group)
- [76: Can you have more than one root layout?](#76-can-you-have-more-than-one-root-layout)
- [77: What is a private folder?](#77-what-is-a-private-folder)
- [78: Can you put non-route files inside the `app` folder?](#78-can-you-put-non-route-files-inside-the-app-folder)
- [79: What is a catch-all route?](#79-what-is-a-catch-all-route)
- [80: What is an optional catch-all route?](#80-what-is-an-optional-catch-all-route)
- [81: How do you add a link to a dynamic route?](#81-how-do-you-add-a-link-to-a-dynamic-route)
- [82: Can you pass an object to `href` in `Link`?](#82-can-you-pass-an-object-to-href-in-link)
- [83: How do you stop `Link` from scrolling to the top after navigation?](#83-how-do-you-stop-link-from-scrolling-to-the-top-after-navigation)
- [84: What does the `replace` prop on `Link` do?](#84-what-does-the-replace-prop-on-link-do)
- [85: How do you link to a section on a page?](#85-how-do-you-link-to-a-section-on-a-page)
- [86: What is `next/script`?](#86-what-is-nextscript)
- [87: What loading strategies does `next/script` support?](#87-what-loading-strategies-does-nextscript-support)
- [88: How do you run code after a script loads?](#88-how-do-you-run-code-after-a-script-loads)
- [89: What is `@next/third-parties`?](#89-what-is-nextthird-parties)
- [90: How do you fetch data in a Server Component?](#90-how-do-you-fetch-data-in-a-server-component)
- [91: Can you query a database directly in a Server Component?](#91-can-you-query-a-database-directly-in-a-server-component)
- [92: How do you fetch data in a Client Component?](#92-how-do-you-fetch-data-in-a-client-component)
- [93: Is `fetch` cached by default in the App Router?](#93-is-fetch-cached-by-default-in-the-app-router)
- [94: What is a Server Action?](#94-what-is-a-server-action)
- [95: What does `"use server"` mean?](#95-what-does-use-server-mean)
- [96: Can Server Actions be in a separate file?](#96-can-server-actions-be-in-a-separate-file)
- [97: How do you refresh the page data after a Server Action?](#97-how-do-you-refresh-the-page-data-after-a-server-action)
- [98: What is `template.tsx`?](#98-what-is-templatetsx)
- [99: How do you run the production build locally?](#99-how-do-you-run-the-production-build-locally)
- [100: How do you change the port of the dev server?](#100-how-do-you-change-the-port-of-the-dev-server)
- [101: What is the `.next` folder?](#101-what-is-the-next-folder)
- [102: What does the build output mean?](#102-what-does-the-build-output-mean)
- [103: How do you deploy a Next.js app?](#103-how-do-you-deploy-a-nextjs-app)
- [104: Do you need Vercel to run Next.js?](#104-do-you-need-vercel-to-run-nextjs)
- [105: What is the `metadata` object used for?](#105-what-is-the-metadata-object-used-for)
- [106: Can you export `metadata` from a Client Component?](#106-can-you-export-metadata-from-a-client-component)
- [107: What is a title template?](#107-what-is-a-title-template)
- [108: What is the `viewport` export?](#108-what-is-the-viewport-export)
- [109: How do you add a `robots.txt` file?](#109-how-do-you-add-a-robotstxt-file)
- [110: How do you create a sitemap?](#110-how-do-you-create-a-sitemap)
- [111: How do you add an Open Graph image?](#111-how-do-you-add-an-open-graph-image)
- [112: What is Proxy in Next.js?](#112-what-is-proxy-in-nextjs)
- [113: Why was Middleware renamed to Proxy?](#113-why-was-middleware-renamed-to-proxy)
- [114: What is the `matcher` in Proxy?](#114-what-is-the-matcher-in-proxy)
- [115: How do you read cookies in a Server Component?](#115-how-do-you-read-cookies-in-a-server-component)
- [116: How do you read request headers in a Server Component?](#116-how-do-you-read-request-headers-in-a-server-component)
- [117: Can you set a cookie in a Server Component?](#117-can-you-set-a-cookie-in-a-server-component)
- [118: What is `next/dynamic`?](#118-what-is-nextdynamic)
- [119: How do you load a component only in the browser?](#119-how-do-you-load-a-component-only-in-the-browser)
- [120: What is code splitting?](#120-what-is-code-splitting)
- [121: What is Fast Refresh?](#121-what-is-fast-refresh)
- [122: What does `reactStrictMode` do?](#122-what-does-reactstrictmode-do)
- [123: How do you add redirects in `next.config.ts`?](#123-how-do-you-add-redirects-in-nextconfigts)
- [124: What is a rewrite?](#124-what-is-a-rewrite)
- [125: What is the difference between a redirect and a rewrite?](#125-what-is-the-difference-between-a-redirect-and-a-rewrite)
- [126: How do you add custom headers to responses?](#126-how-do-you-add-custom-headers-to-responses)
- [127: What is a static export?](#127-what-is-a-static-export)
- [128: Which features don't work with a static export?](#128-which-features-dont-work-with-a-static-export)
- [129: How do you add a global "loading" bar or progress indicator on navigation?](#129-how-do-you-add-a-global-loading-bar-or-progress-indicator-on-navigation)
- [130: What is the `<Form>` component from `next/form`?](#130-what-is-the-form-component-from-nextform)
- [131: What is the difference between `next build` and `next dev`?](#131-what-is-the-difference-between-next-build-and-next-dev)
- [132: What does `next info` do?](#132-what-does-next-info-do)
- [133: How do you upgrade Next.js?](#133-how-do-you-upgrade-nextjs)
- [134: What are codemods?](#134-what-are-codemods)
- [135: How do you set up ESLint in Next.js 16?](#135-how-do-you-set-up-eslint-in-nextjs-16)
- [136: What is the `children` prop in a layout?](#136-what-is-the-children-prop-in-a-layout)
- [137: Do layouts receive `searchParams`?](#137-do-layouts-receive-searchparams)
- [138: Can a Server Component import a Client Component?](#138-can-a-server-component-import-a-client-component)
- [139: Can a Client Component import a Server Component?](#139-can-a-client-component-import-a-server-component)
- [140: What is the difference between static and dynamic rendering?](#140-what-is-the-difference-between-static-and-dynamic-rendering)
- [141: What is incremental static regeneration (ISR)?](#141-what-is-incremental-static-regeneration-isr)
- [142: What does `revalidate` mean?](#142-what-does-revalidate-mean)
- [143: What is `generateStaticParams`?](#143-what-is-generatestaticparams)
- [144: How do you read a file from the file system in a page?](#144-how-do-you-read-a-file-from-the-file-system-in-a-page)
- [145: Does Next.js support MDX?](#145-does-nextjs-support-mdx)
- [146: What is `getStaticProps`?](#146-what-is-getstaticprops)
- [147: What is `getServerSideProps`?](#147-what-is-getserversideprops)
- [148: What is `getStaticPaths`?](#148-what-is-getstaticpaths)
- [149: What are `_app.tsx` and `_document.tsx` in the Pages Router?](#149-what-are-_apptsx-and-_documenttsx-in-the-pages-router)
- [150: How do you add a custom 404 page in the Pages Router?](#150-how-do-you-add-a-custom-404-page-in-the-pages-router)

### Moderate Questions (151-300)

- [151: How does Next.js decide if a route is static or dynamic?](#151-how-does-nextjs-decide-if-a-route-is-static-or-dynamic)
- [152: What are the route segment config options?](#152-what-are-the-route-segment-config-options)
- [153: What does `export const dynamic = 'force-dynamic'` do?](#153-what-does-export-const-dynamic--force-dynamic-do)
- [154: What does `dynamicParams` do?](#154-what-does-dynamicparams-do)
- [155: What are the caching layers in Next.js?](#155-what-are-the-caching-layers-in-nextjs)
- [156: What is request memoization?](#156-what-is-request-memoization)
- [157: How do you dedupe calls that don't use `fetch`?](#157-how-do-you-dedupe-calls-that-dont-use-fetch)
- [158: What is the difference between React `cache` and `"use cache"`?](#158-what-is-the-difference-between-react-cache-and-use-cache)
- [159: What is the Router Cache?](#159-what-is-the-router-cache)
- [160: What does `router.refresh()` do?](#160-what-does-routerrefresh-do)
- [161: What is `revalidatePath`?](#161-what-is-revalidatepath)
- [162: What is `revalidateTag`?](#162-what-is-revalidatetag)
- [163: What is `updateTag` and how is it different from `revalidateTag`?](#163-what-is-updatetag-and-how-is-it-different-from-revalidatetag)
- [164: What does `refresh()` from `next/cache` do?](#164-what-does-refresh-from-nextcache-do)
- [165: How do you use `useActionState` with a form?](#165-how-do-you-use-useactionstate-with-a-form)
- [166: What is `useFormStatus`?](#166-what-is-useformstatus)
- [167: What is `useOptimistic`?](#167-what-is-useoptimistic)
- [168: How do you pass extra arguments to a Server Action?](#168-how-do-you-pass-extra-arguments-to-a-server-action)
- [169: Can you call a Server Action without a form?](#169-can-you-call-a-server-action-without-a-form)
- [170: What is progressive enhancement in Server Actions?](#170-what-is-progressive-enhancement-in-server-actions)
- [171: How do you validate form data in a Server Action?](#171-how-do-you-validate-form-data-in-a-server-action)
- [172: How do you redirect after a Server Action?](#172-how-do-you-redirect-after-a-server-action)
- [173: Are Server Actions secure by default?](#173-are-server-actions-secure-by-default)
- [174: What is the default body size limit for Server Actions and how do you change it?](#174-what-is-the-default-body-size-limit-for-server-actions-and-how-do-you-change-it)
- [175: How do you handle errors in Server Actions?](#175-how-do-you-handle-errors-in-server-actions)
- [176: What is streaming?](#176-what-is-streaming)
- [177: How do you stream part of a page with Suspense?](#177-how-do-you-stream-part-of-a-page-with-suspense)
- [178: What is the difference between `loading.tsx` and `<Suspense>`?](#178-what-is-the-difference-between-loadingtsx-and-suspense)
- [179: What is a data waterfall and how do you avoid it?](#179-what-is-a-data-waterfall-and-how-do-you-avoid-it)
- [180: How do you pass data from a Server Component to a Client Component without waiting for it?](#180-how-do-you-pass-data-from-a-server-component-to-a-client-component-without-waiting-for-it)
- [181: What are parallel routes?](#181-what-are-parallel-routes)
- [182: What is `default.tsx` in parallel routes?](#182-what-is-defaulttsx-in-parallel-routes)
- [183: What are intercepting routes?](#183-what-are-intercepting-routes)
- [184: How do you build a modal with parallel and intercepting routes?](#184-how-do-you-build-a-modal-with-parallel-and-intercepting-routes)
- [185: What are `useSelectedLayoutSegment` and `useSelectedLayoutSegments`?](#185-what-are-useselectedlayoutsegment-and-useselectedlayoutsegments)
- [186: Why does `useSearchParams` need a Suspense boundary?](#186-why-does-usesearchparams-need-a-suspense-boundary)
- [187: How do you update a search param without losing the others?](#187-how-do-you-update-a-search-param-without-losing-the-others)
- [188: How do you build a search page where results update as the user types?](#188-how-do-you-build-a-search-page-where-results-update-as-the-user-types)
- [189: How do you use `generateMetadata`?](#189-how-do-you-use-generatemetadata)
- [190: What is `metadataBase`?](#190-what-is-metadatabase)
- [191: How do you generate an Open Graph image with code?](#191-how-do-you-generate-an-open-graph-image-with-code)
- [192: How is metadata merged between layouts and pages?](#192-how-is-metadata-merged-between-layouts-and-pages)
- [193: How does Next.js stream metadata?](#193-how-does-nextjs-stream-metadata)
- [194: How do you create an API endpoint with a dynamic segment in a Route Handler?](#194-how-do-you-create-an-api-endpoint-with-a-dynamic-segment-in-a-route-handler)
- [195: How do you read query params in a Route Handler?](#195-how-do-you-read-query-params-in-a-route-handler)
- [196: Are `GET` Route Handlers cached?](#196-are-get-route-handlers-cached)
- [197: What is `NextResponse`?](#197-what-is-nextresponse)
- [198: What is `NextRequest`?](#198-what-is-nextrequest)
- [199: How do you set cookies in a Route Handler?](#199-how-do-you-set-cookies-in-a-route-handler)
- [200: How do you handle CORS in a Route Handler?](#200-how-do-you-handle-cors-in-a-route-handler)
- [201: How do you stream a response from a Route Handler?](#201-how-do-you-stream-a-response-from-a-route-handler)
- [202: When should you use a Route Handler instead of a Server Action?](#202-when-should-you-use-a-route-handler-instead-of-a-server-action)
- [203: How do you handle a webhook in Next.js?](#203-how-do-you-handle-a-webhook-in-nextjs)
- [204: What can you do in `proxy.ts`?](#204-what-can-you-do-in-proxyts)
- [205: What runtime does Proxy use?](#205-what-runtime-does-proxy-use)
- [206: How do you set a request header in Proxy so your pages can read it?](#206-how-do-you-set-a-request-header-in-proxy-so-your-pages-can-read-it)
- [207: How do you use advanced matching in the Proxy `matcher`?](#207-how-do-you-use-advanced-matching-in-the-proxy-matcher)
- [208: Should you do authentication only in Proxy?](#208-should-you-do-authentication-only-in-proxy)
- [209: How do you protect a page so only logged-in users can see it?](#209-how-do-you-protect-a-page-so-only-logged-in-users-can-see-it)
- [210: Why shouldn't you do auth checks only in a layout?](#210-why-shouldnt-you-do-auth-checks-only-in-a-layout)
- [211: What libraries are commonly used for authentication in Next.js?](#211-what-libraries-are-commonly-used-for-authentication-in-nextjs)
- [212: What is the `server-only` package?](#212-what-is-the-server-only-package)
- [213: What happens if a Server Component reads a non-public env variable that is used in a Client Component?](#213-what-happens-if-a-server-component-reads-a-non-public-env-variable-that-is-used-in-a-client-component)
- [214: When are environment variables read: at build time or at runtime?](#214-when-are-environment-variables-read-at-build-time-or-at-runtime)
- [215: How do you use `generateStaticParams` with multiple dynamic segments?](#215-how-do-you-use-generatestaticparams-with-multiple-dynamic-segments)
- [216: How do you prerender only some pages and render the rest on demand?](#216-how-do-you-prerender-only-some-pages-and-render-the-rest-on-demand)
- [217: How do you implement internationalization (i18n) in the App Router?](#217-how-do-you-implement-internationalization-i18n-in-the-app-router)
- [218: How was i18n handled in the Pages Router?](#218-how-was-i18n-handled-in-the-pages-router)
- [219: What is `next/image` `sizes` and why does it matter?](#219-what-is-nextimage-sizes-and-why-does-it-matter)
- [220: How do you show a blur placeholder on images?](#220-how-do-you-show-a-blur-placeholder-on-images)
- [221: What changed in the default image settings in Next.js 16?](#221-what-changed-in-the-default-image-settings-in-nextjs-16)
- [222: How do you use a custom image loader?](#222-how-do-you-use-a-custom-image-loader)
- [223: How do you use CSS variables with `next/font`?](#223-how-do-you-use-css-variables-with-nextfont)
- [224: How do you use CSS-in-JS libraries like styled-components in the App Router?](#224-how-do-you-use-css-in-js-libraries-like-styled-components-in-the-app-router)
- [225: How do you share state, like a theme, across Client Components in the App Router?](#225-how-do-you-share-state-like-a-theme-across-client-components-in-the-app-router)
- [226: How do you use a third-party component that uses hooks but has no `"use client"`?](#226-how-do-you-use-a-third-party-component-that-uses-hooks-but-has-no-use-client)
- [227: What is the difference between `error.tsx` and `global-error.tsx`?](#227-what-is-the-difference-between-errortsx-and-global-errortsx)
- [228: What is the `digest` property on errors?](#228-what-is-the-digest-property-on-errors)
- [229: What does `reset()` do in an error boundary?](#229-what-does-reset-do-in-an-error-boundary)
- [230: Can you use `try/catch` around `redirect()` or `notFound()`?](#230-can-you-use-trycatch-around-redirect-or-notfound)
- [231: What are `forbidden()` and `unauthorized()`?](#231-what-are-forbidden-and-unauthorized)
- [232: What is the `after()` function?](#232-what-is-the-after-function)
- [233: What is `connection()`?](#233-what-is-connection)
- [234: How do you enable Cache Components?](#234-how-do-you-enable-cache-components)
- [235: What is the `"use cache"` directive?](#235-what-is-the-use-cache-directive)
- [236: What is `cacheLife`?](#236-what-is-cachelife)
- [237: What is `cacheTag`?](#237-what-is-cachetag)
- [238: What is Partial Prerendering (PPR)?](#238-what-is-partial-prerendering-ppr)
- [239: What happens if you access dynamic data outside `<Suspense>` with Cache Components on?](#239-what-happens-if-you-access-dynamic-data-outside-suspense-with-cache-components-on)
- [240: Can you use `cookies()` inside a `"use cache"` function?](#240-can-you-use-cookies-inside-a-use-cache-function)
- [241: How does the Pages Router `getStaticProps` `revalidate` compare to App Router revalidation?](#241-how-does-the-pages-router-getstaticprops-revalidate-compare-to-app-router-revalidation)
- [242: How do you do on-demand revalidation in the Pages Router?](#242-how-do-you-do-on-demand-revalidation-in-the-pages-router)
- [243: What does `fallback` mean in `getStaticPaths`?](#243-what-does-fallback-mean-in-getstaticpaths)
- [244: How do you share data between layouts and pages without prop drilling?](#244-how-do-you-share-data-between-layouts-and-pages-without-prop-drilling)
- [245: How do you use the `preload` pattern?](#245-how-do-you-use-the-preload-pattern)
- [246: How do you create a typed link with typed routes?](#246-how-do-you-create-a-typed-link-with-typed-routes)
- [247: What are `PageProps` and `LayoutProps` helpers?](#247-what-are-pageprops-and-layoutprops-helpers)
- [248: How do you test Next.js apps?](#248-how-do-you-test-nextjs-apps)
- [249: How do you set up Jest with Next.js?](#249-how-do-you-set-up-jest-with-nextjs)
- [250: How do you set up Vitest with Next.js?](#250-how-do-you-set-up-vitest-with-nextjs)
- [251: How do you mock `next/navigation` in unit tests?](#251-how-do-you-mock-nextnavigation-in-unit-tests)
- [252: What is `instrumentation.ts`?](#252-what-is-instrumentationts)
- [253: What is `onRequestError` in `instrumentation.ts`?](#253-what-is-onrequesterror-in-instrumentationts)
- [254: What is `instrumentation-client.ts`?](#254-what-is-instrumentation-clientts)
- [255: How do you measure Web Vitals in Next.js?](#255-how-do-you-measure-web-vitals-in-nextjs)
- [256: What is draft mode?](#256-what-is-draft-mode)
- [257: What is `output: 'standalone'`?](#257-what-is-output-standalone)
- [258: What does a basic Dockerfile for Next.js look like?](#258-what-does-a-basic-dockerfile-for-nextjs-look-like)
- [259: What is `basePath`?](#259-what-is-basepath)
- [260: What is `assetPrefix`?](#260-what-is-assetprefix)
- [261: What does `trailingSlash` do?](#261-what-does-trailingslash-do)
- [262: What is `transpilePackages`?](#262-what-is-transpilepackages)
- [263: What is `serverExternalPackages`?](#263-what-is-serverexternalpackages)
- [264: What is `optimizePackageImports`?](#264-what-is-optimizepackageimports)
- [265: How do you configure Turbopack?](#265-how-do-you-configure-turbopack)
- [266: What happens if you have a custom `webpack` config and run `next build` in Next.js 16?](#266-what-happens-if-you-have-a-custom-webpack-config-and-run-next-build-in-nextjs-16)
- [267: How do you analyze bundle size?](#267-how-do-you-analyze-bundle-size)
- [268: What is the difference between `useRouter().push` and `redirect()`?](#268-what-is-the-difference-between-userouterpush-and-redirect)
- [269: What does `RedirectType` do in `redirect()`?](#269-what-does-redirecttype-do-in-redirect)
- [270: How do you show a different UI based on the user's device?](#270-how-do-you-show-a-different-ui-based-on-the-users-device)
- [271: How do you add a loading state when submitting a form that navigates?](#271-how-do-you-add-a-loading-state-when-submitting-a-form-that-navigates)
- [272: How do you prevent a component from being included in the static shell?](#272-how-do-you-prevent-a-component-from-being-included-in-the-static-shell)
- [273: How do you handle file uploads in a Server Action?](#273-how-do-you-handle-file-uploads-in-a-server-action)
- [274: What is the `onNavigate` prop on `Link`?](#274-what-is-the-onnavigate-prop-on-link)
- [275: What is the `prefetch` prop on `Link` and what values does it accept?](#275-what-is-the-prefetch-prop-on-link-and-what-values-does-it-accept)
- [276: What improvements did Next.js 16 make to navigation and prefetching?](#276-what-improvements-did-nextjs-16-make-to-navigation-and-prefetching)
- [277: What is the React Compiler and how do you enable it in Next.js?](#277-what-is-the-react-compiler-and-how-do-you-enable-it-in-nextjs)
- [278: How do you add security headers to every response?](#278-how-do-you-add-security-headers-to-every-response)
- [279: How do you redirect based on a database lookup?](#279-how-do-you-redirect-based-on-a-database-lookup)
- [280: How do you build a multi-tenant app with subdomains?](#280-how-do-you-build-a-multi-tenant-app-with-subdomains)
- [281: How do you read the current pathname in a Server Component?](#281-how-do-you-read-the-current-pathname-in-a-server-component)
- [282: How do you scroll to the top or keep the scroll position after a Server Action?](#282-how-do-you-scroll-to-the-top-or-keep-the-scroll-position-after-a-server-action)
- [283: How do you upload images from the browser and show them with `next/image`?](#283-how-do-you-upload-images-from-the-browser-and-show-them-with-nextimage)
- [284: What is the `useServerInsertedHTML` hook?](#284-what-is-the-useserverinsertedhtml-hook)
- [285: How do you run a cron job in a Next.js app?](#285-how-do-you-run-a-cron-job-in-a-nextjs-app)
- [286: How do you use `generateImageMetadata`?](#286-how-do-you-use-generateimagemetadata)
- [287: How do you create multiple sitemaps for a large site?](#287-how-do-you-create-multiple-sitemaps-for-a-large-site)
- [288: How do you create a web app manifest?](#288-how-do-you-create-a-web-app-manifest)
- [289: How do you add JSON-LD structured data?](#289-how-do-you-add-json-ld-structured-data)
- [290: How do you set canonical URLs and alternate languages?](#290-how-do-you-set-canonical-urls-and-alternate-languages)
- [291: How do you stop search engines from indexing a page?](#291-how-do-you-stop-search-engines-from-indexing-a-page)
- [292: What is the difference between `useEffect` data fetching and Server Component data fetching?](#292-what-is-the-difference-between-useeffect-data-fetching-and-server-component-data-fetching)
- [293: How do you poll for new data in the App Router?](#293-how-do-you-poll-for-new-data-in-the-app-router)
- [294: How do you migrate a page from the Pages Router to the App Router?](#294-how-do-you-migrate-a-page-from-the-pages-router-to-the-app-router)
- [295: How do you replace `next/head` in the App Router?](#295-how-do-you-replace-nexthead-in-the-app-router)
- [296: How do you use the `Link` component with a custom component?](#296-how-do-you-use-the-link-component-with-a-custom-component)
- [297: What does `export const maxDuration` do?](#297-what-does-export-const-maxduration-do)
- [298: How do you get the `params` of a page in `generateMetadata` and in the page without fetching twice?](#298-how-do-you-get-the-params-of-a-page-in-generatemetadata-and-in-the-page-without-fetching-twice)
- [299: What is the difference between `force-cache`, `no-store` and the default in `fetch`?](#299-what-is-the-difference-between-force-cache-no-store-and-the-default-in-fetch)
- [300: How do you set different revalidate times for different fetches on one page?](#300-how-do-you-set-different-revalidate-times-for-different-fetches-on-one-page)

### Advanced Questions (301-450)

- [301: What is the RSC payload?](#301-what-is-the-rsc-payload)
- [302: How does a client-side navigation work in the App Router step by step?](#302-how-does-a-client-side-navigation-work-in-the-app-router-step-by-step)
- [303: Why do shared layouts not re-render on navigation, and what are the consequences?](#303-why-do-shared-layouts-not-re-render-on-navigation-and-what-are-the-consequences)
- [304: What can be passed as props from a Server Component to a Client Component?](#304-what-can-be-passed-as-props-from-a-server-component-to-a-client-component)
- [305: How does the server/client boundary work in the module graph?](#305-how-does-the-serverclient-boundary-work-in-the-module-graph)
- [306: Why would a component render as both a Server and a Client Component?](#306-why-would-a-component-render-as-both-a-server-and-a-client-component)
- [307: How do you keep secrets from leaking into Client Components?](#307-how-do-you-keep-secrets-from-leaking-into-client-components)
- [308: What are the React Taint APIs?](#308-what-are-the-react-taint-apis)
- [309: What is a Data Access Layer (DAL) and why is it recommended?](#309-what-is-a-data-access-layer-dal-and-why-is-it-recommended)
- [310: How are closure variables in inline Server Actions protected?](#310-how-are-closure-variables-in-inline-server-actions-protected)
- [311: Why do you need `NEXT_SERVER_ACTIONS_ENCRYPTION_KEY` when self-hosting with multiple servers?](#311-why-do-you-need-next_server_actions_encryption_key-when-self-hosting-with-multiple-servers)
- [312: How does Next.js protect Server Actions from CSRF?](#312-how-does-nextjs-protect-server-actions-from-csrf)
- [313: How are Server Action IDs created and why does it matter?](#313-how-are-server-action-ids-created-and-why-does-it-matter)
- [314: Are Server Actions run in parallel?](#314-are-server-actions-run-in-parallel)
- [315: What happens to the UI after a Server Action finishes?](#315-what-happens-to-the-ui-after-a-server-action-finishes)
- [316: What was CVE-2025-29927 and what does it teach about Middleware/Proxy?](#316-what-was-cve-2025-29927-and-what-does-it-teach-about-middlewareproxy)
- [317: What was the "React2Shell" vulnerability in December 2025?](#317-what-was-the-react2shell-vulnerability-in-december-2025)
- [318: How do you implement a Content Security Policy with nonces?](#318-how-do-you-implement-a-content-security-policy-with-nonces)
- [319: How does the cache key for `"use cache"` work?](#319-how-does-the-cache-key-for-use-cache-work)
- [320: How does `"use cache"` handle `children` and other non-serializable props?](#320-how-does-use-cache-handle-children-and-other-non-serializable-props)
- [321: Where is `"use cache"` data stored by default, and what are `"use cache: remote"` and `"use cache: private"`?](#321-where-is-use-cache-data-stored-by-default-and-what-are-use-cache-remote-and-use-cache-private)
- [322: How do you configure a custom cache handler for `"use cache"`?](#322-how-do-you-configure-a-custom-cache-handler-for-use-cache)
- [323: How do you define custom `cacheLife` profiles?](#323-how-do-you-define-custom-cachelife-profiles)
- [324: What happens when you nest cached functions with different `cacheLife` values?](#324-what-happens-when-you-nest-cached-functions-with-different-cachelife-values)
- [325: Why can a short `cacheLife` make a component dynamic?](#325-why-can-a-short-cachelife-make-a-component-dynamic)
- [326: How do you use `Date.now()` or `Math.random()` with Cache Components?](#326-how-do-you-use-datenow-or-mathrandom-with-cache-components)
- [327: How does Next.js 16 use React's `<Activity>` with Cache Components?](#327-how-does-nextjs-16-use-reacts-activity-with-cache-components)
- [328: How do you use View Transitions in Next.js?](#328-how-do-you-use-view-transitions-in-nextjs)
- [329: What is `useEffectEvent` and why is it useful in Next.js apps?](#329-what-is-useeffectevent-and-why-is-it-useful-in-nextjs-apps)
- [330: How does streaming affect the HTTP status code?](#330-how-does-streaming-affect-the-http-status-code)
- [331: How does the Data Cache behave across deployments?](#331-how-does-the-data-cache-behave-across-deployments)
- [332: How do you self-host ISR with multiple instances?](#332-how-do-you-self-host-isr-with-multiple-instances)
- [333: What is `deploymentId` and version skew?](#333-what-is-deploymentid-and-version-skew)
- [334: What are Build Adapters?](#334-what-are-build-adapters)
- [335: What are the differences between the Node.js and Edge runtimes?](#335-what-are-the-differences-between-the-nodejs-and-edge-runtimes)
- [336: How do you trace performance with OpenTelemetry?](#336-how-do-you-trace-performance-with-opentelemetry)
- [337: How do you log `fetch` requests and cache hits in development?](#337-how-do-you-log-fetch-requests-and-cache-hits-in-development)
- [338: What is the Next.js DevTools MCP server?](#338-what-is-the-nextjs-devtools-mcp-server)
- [339: How do you debug a Next.js app on the server side?](#339-how-do-you-debug-a-nextjs-app-on-the-server-side)
- [340: How do you build a large app with multiple Next.js apps under one domain?](#340-how-do-you-build-a-large-app-with-multiple-nextjs-apps-under-one-domain)
- [341: How do you set up Next.js in a monorepo?](#341-how-do-you-set-up-nextjs-in-a-monorepo)
- [342: What is output file tracing?](#342-what-is-output-file-tracing)
- [343: How does Turbopack's file system cache work?](#343-how-does-turbopacks-file-system-cache-work)
- [344: Why might code that works with webpack fail with Turbopack?](#344-why-might-code-that-works-with-webpack-fail-with-turbopack)
- [345: How do you debug why a route became dynamic?](#345-how-do-you-debug-why-a-route-became-dynamic)
- [346: Why is `searchParams` on a page a common cause of dynamic rendering, and how do you avoid it?](#346-why-is-searchparams-on-a-page-a-common-cause-of-dynamic-rendering-and-how-do-you-avoid-it)
- [347: Explain how `generateStaticParams` works with Cache Components.](#347-explain-how-generatestaticparams-works-with-cache-components)
- [348: What is the difference between the `revalidatePath` `'page'` and `'layout'` types?](#348-what-is-the-difference-between-the-revalidatepath-page-and-layout-types)
- [349: When does `revalidatePath` in a Server Action update the current page instantly?](#349-when-does-revalidatepath-in-a-server-action-update-the-current-page-instantly)
- [350: How do you invalidate the client Router Cache?](#350-how-do-you-invalidate-the-client-router-cache)
- [351: What are `staleTimes`?](#351-what-are-staletimes)
- [352: How would you build an e-commerce product page with fast static content and personalized parts?](#352-how-would-you-build-an-e-commerce-product-page-with-fast-static-content-and-personalized-parts)
- [353: How do you avoid passing large data to Client Components?](#353-how-do-you-avoid-passing-large-data-to-client-components)
- [354: How do you make a list of items interactive without making the whole list a Client Component?](#354-how-do-you-make-a-list-of-items-interactive-without-making-the-whole-list-a-client-component)
- [355: How do you render a Server Component inside a Client Component that depends on client state?](#355-how-do-you-render-a-server-component-inside-a-client-component-that-depends-on-client-state)
- [356: How does Suspense on the server work together with hydration?](#356-how-does-suspense-on-the-server-work-together-with-hydration)
- [357: How do you handle errors inside a streamed Suspense boundary?](#357-how-do-you-handle-errors-inside-a-streamed-suspense-boundary)
- [358: What is `unstable_rethrow` and when do you need it?](#358-what-is-unstable_rethrow-and-when-do-you-need-it)
- [359: How do you prevent hydration mismatches for theme or time-based UI?](#359-how-do-you-prevent-hydration-mismatches-for-theme-or-time-based-ui)
- [360: How do you handle `window` and `localStorage` safely in Client Components?](#360-how-do-you-handle-window-and-localstorage-safely-in-client-components)
- [361: How do you design a Next.js app to reduce JavaScript sent to the browser?](#361-how-do-you-design-a-nextjs-app-to-reduce-javascript-sent-to-the-browser)
- [362: How does Next.js handle `fetch` request deduplication vs caching in Route Handlers?](#362-how-does-nextjs-handle-fetch-request-deduplication-vs-caching-in-route-handlers)
- [363: How do you cache data from a database query when not using Cache Components?](#363-how-do-you-cache-data-from-a-database-query-when-not-using-cache-components)
- [364: What are the trade-offs of using Cache Components?](#364-what-are-the-trade-offs-of-using-cache-components)
- [365: How do you migrate `export const revalidate = 3600` to Cache Components?](#365-how-do-you-migrate-export-const-revalidate--3600-to-cache-components)
- [366: How does `revalidateTag` with a profile differ from immediate expiry?](#366-how-does-revalidatetag-with-a-profile-differ-from-immediate-expiry)
- [367: How do you implement optimistic UI with rollback using `useOptimistic` and Server Actions?](#367-how-do-you-implement-optimistic-ui-with-rollback-using-useoptimistic-and-server-actions)
- [368: How do you implement infinite scroll with Server Components?](#368-how-do-you-implement-infinite-scroll-with-server-components)
- [369: Can Server Actions return JSX?](#369-can-server-actions-return-jsx)
- [370: How do you keep a Server Action from running for unauthorized users who call it directly?](#370-how-do-you-keep-a-server-action-from-running-for-unauthorized-users-who-call-it-directly)
- [371: How do you rate limit Server Actions or Route Handlers?](#371-how-do-you-rate-limit-server-actions-or-route-handlers)
- [372: What happens if a Server Component throws during prerendering at build time?](#372-what-happens-if-a-server-component-throws-during-prerendering-at-build-time)
- [373: How do you handle a database that isn't reachable during `next build`?](#373-how-do-you-handle-a-database-that-isnt-reachable-during-next-build)
- [374: How do you share code between Server and Client Components safely?](#374-how-do-you-share-code-between-server-and-client-components-safely)
- [375: Why can't you use a Context Provider directly in a Server Component layout, and what is the pattern?](#375-why-cant-you-use-a-context-provider-directly-in-a-server-component-layout-and-what-is-the-pattern)
- [376: How does Next.js decide what to prefetch for a dynamic route without `loading.tsx`?](#376-how-does-nextjs-decide-what-to-prefetch-for-a-dynamic-route-without-loadingtsx)
- [377: How do you build a route that renders differently for logged-in and logged-out users but stays fast?](#377-how-do-you-build-a-route-that-renders-differently-for-logged-in-and-logged-out-users-but-stays-fast)
- [378: How do you implement A/B testing without making pages dynamic?](#378-how-do-you-implement-ab-testing-without-making-pages-dynamic)
- [379: How do you make `generateMetadata` not slow down the page?](#379-how-do-you-make-generatemetadata-not-slow-down-the-page)
- [380: How do you handle `notFound()` inside `generateMetadata`?](#380-how-do-you-handle-notfound-inside-generatemetadata)
- [381: How would you implement role-based access control (RBAC) in Next.js?](#381-how-would-you-implement-role-based-access-control-rbac-in-nextjs)
- [382: How do you store sessions: stateless cookies vs database sessions?](#382-how-do-you-store-sessions-stateless-cookies-vs-database-sessions)
- [383: How do you refresh a session cookie on activity?](#383-how-do-you-refresh-a-session-cookie-on-activity)
- [384: What are the risks of putting heavy logic in Proxy?](#384-what-are-the-risks-of-putting-heavy-logic-in-proxy)
- [385: How do you return a JSON error from Proxy?](#385-how-do-you-return-a-json-error-from-proxy)
- [386: How do you use `waitUntil` in Proxy?](#386-how-do-you-use-waituntil-in-proxy)
- [387: What is `skipProxyUrlNormalize` and `skipTrailingSlashRedirect`?](#387-what-is-skipproxyurlnormalize-and-skiptrailingslashredirect)
- [388: How does Next.js decide the order of routing logic?](#388-how-does-nextjs-decide-the-order-of-routing-logic)
- [389: What are `beforeFiles`, `afterFiles` and `fallback` rewrites?](#389-what-are-beforefiles-afterfiles-and-fallback-rewrites)
- [390: How does `has` / `missing` matching work in redirects and rewrites?](#390-how-does-has--missing-matching-work-in-redirects-and-rewrites)
- [391: How do you handle large static sites with thousands of pages and keep build times low?](#391-how-do-you-handle-large-static-sites-with-thousands-of-pages-and-keep-build-times-low)
- [392: How do you generate static pages in parallel faster during build?](#392-how-do-you-generate-static-pages-in-parallel-faster-during-build)
- [393: How do you use `generateStaticParams` with `fetch` deduplication during build?](#393-how-do-you-use-generatestaticparams-with-fetch-deduplication-during-build)
- [394: What is the static shell and how is it served?](#394-what-is-the-static-shell-and-how-is-it-served)
- [395: How does Next.js 16 resume a prerendered shell at request time?](#395-how-does-nextjs-16-resume-a-prerendered-shell-at-request-time)
- [396: How do you serve a prerendered shell from a CDN while the dynamic parts come from your server?](#396-how-do-you-serve-a-prerendered-shell-from-a-cdn-while-the-dynamic-parts-come-from-your-server)
- [397: Explain the difference between `prefetch` and `preload` for images and links.](#397-explain-the-difference-between-prefetch-and-preload-for-images-and-links)
- [398: How do you reduce Largest Contentful Paint (LCP) in a Next.js app?](#398-how-do-you-reduce-largest-contentful-paint-lcp-in-a-nextjs-app)
- [399: How do you reduce Interaction to Next Paint (INP)?](#399-how-do-you-reduce-interaction-to-next-paint-inp)
- [400: How do you avoid Cumulative Layout Shift (CLS)?](#400-how-do-you-avoid-cumulative-layout-shift-cls)
- [401: How does `next/font` avoid layout shift technically?](#401-how-does-nextfont-avoid-layout-shift-technically)
- [402: What happens to `next/font` font files at build time?](#402-what-happens-to-nextfont-font-files-at-build-time)
- [403: How does the image optimizer work when self-hosting?](#403-how-does-the-image-optimizer-work-when-self-hosting)
- [404: Why did Next.js 16 restrict image qualities and local IPs?](#404-why-did-nextjs-16-restrict-image-qualities-and-local-ips)
- [405: How do you serve AVIF images?](#405-how-do-you-serve-avif-images)
- [406: How do you handle images in a static export?](#406-how-do-you-handle-images-in-a-static-export)
- [407: What is the difference between `unoptimized` on a single image and the global setting?](#407-what-is-the-difference-between-unoptimized-on-a-single-image-and-the-global-setting)
- [408: Why does `next/image` not optimize SVGs by default?](#408-why-does-nextimage-not-optimize-svgs-by-default)
- [409: How do you handle authentication for API clients like mobile apps?](#409-how-do-you-handle-authentication-for-api-clients-like-mobile-apps)
- [410: How do you share business logic between Server Actions and Route Handlers?](#410-how-do-you-share-business-logic-between-server-actions-and-route-handlers)
- [411: How do you handle long-running tasks that exceed request time limits?](#411-how-do-you-handle-long-running-tasks-that-exceed-request-time-limits)
- [412: How do you implement Server-Sent Events (SSE) with a Route Handler?](#412-how-do-you-implement-server-sent-events-sse-with-a-route-handler)
- [413: Why doesn't Next.js support WebSockets in Route Handlers?](#413-why-doesnt-nextjs-support-websockets-in-route-handlers)
- [414: What is a custom server and when should you avoid it?](#414-what-is-a-custom-server-and-when-should-you-avoid-it)
- [415: How do you handle graceful shutdown in a self-hosted Next.js app?](#415-how-do-you-handle-graceful-shutdown-in-a-self-hosted-nextjs-app)
- [416: How do you set `Cache-Control` headers when self-hosting behind a CDN?](#416-how-do-you-set-cache-control-headers-when-self-hosting-behind-a-cdn)
- [417: Why must a CDN respect the `Vary` header for Next.js routes?](#417-why-must-a-cdn-respect-the-vary-header-for-nextjs-routes)
- [418: How do you run Next.js on serverless platforms other than Vercel?](#418-how-do-you-run-nextjs-on-serverless-platforms-other-than-vercel)
- [419: How do you migrate from `getServerSideProps` with `context.res.setHeader` caching to the App Router?](#419-how-do-you-migrate-from-getserversideprops-with-contextressetheader-caching-to-the-app-router)
- [420: How do you handle a Pages Router `_app` global data fetch in the App Router?](#420-how-do-you-handle-a-pages-router-_app-global-data-fetch-in-the-app-router)
- [421: How do you test Server Actions?](#421-how-do-you-test-server-actions)
- [422: How do you test Proxy logic?](#422-how-do-you-test-proxy-logic)
- [423: How do you use Playwright to test a Next.js app?](#423-how-do-you-use-playwright-to-test-a-nextjs-app)
- [424: How do you mock external APIs used by Server Components in E2E tests?](#424-how-do-you-mock-external-apis-used-by-server-components-in-e2e-tests)
- [425: How does `next build` handle TypeScript errors?](#425-how-does-next-build-handle-typescript-errors)
- [426: How do you type `params` in Route Handlers with the generated helpers?](#426-how-do-you-type-params-in-route-handlers-with-the-generated-helpers)
- [427: What is the difference between `next dev`, `next build` and `next start` with Cache Components errors?](#427-what-is-the-difference-between-next-dev-next-build-and-next-start-with-cache-components-errors)
- [428: How do you use environment variables at runtime in a Docker image built once?](#428-how-do-you-use-environment-variables-at-runtime-in-a-docker-image-built-once)
- [429: How do you load environment variables outside of the Next.js runtime (for example in a seed script or ORM config)?](#429-how-do-you-load-environment-variables-outside-of-the-nextjs-runtime-for-example-in-a-seed-script-or-orm-config)
- [430: Why can't a Server Component be rendered inside a `"use cache"` function that reads cookies via a child?](#430-why-cant-a-server-component-be-rendered-inside-a-use-cache-function-that-reads-cookies-via-a-child)
- [431: How do you implement a "stale while loading" search UI with `useTransition` and the router?](#431-how-do-you-implement-a-stale-while-loading-search-ui-with-usetransition-and-the-router)
- [432: How do you persist state across navigations without global state libraries?](#432-how-do-you-persist-state-across-navigations-without-global-state-libraries)
- [433: How do you implement a "Back" button in an intercepted modal that works on direct visits too?](#433-how-do-you-implement-a-back-button-in-an-intercepted-modal-that-works-on-direct-visits-too)
- [434: Why does an intercepting route not work after a page refresh?](#434-why-does-an-intercepting-route-not-work-after-a-page-refresh)
- [435: How do you conditionally render parallel routes based on auth?](#435-how-do-you-conditionally-render-parallel-routes-based-on-auth)
- [436: How do you handle `default.tsx` for nested parallel routes?](#436-how-do-you-handle-defaulttsx-for-nested-parallel-routes)
- [437: How do you build a resilient layout where one widget's failure doesn't break the page?](#437-how-do-you-build-a-resilient-layout-where-one-widgets-failure-doesnt-break-the-page)
- [438: How does Next.js handle a Server Action called from a page that has since been redeployed?](#438-how-does-nextjs-handle-a-server-action-called-from-a-page-that-has-since-been-redeployed)
- [439: How do you profile React rendering in a Next.js app?](#439-how-do-you-profile-react-rendering-in-a-nextjs-app)
- [440: How do you diagnose memory leaks in a Next.js server?](#440-how-do-you-diagnose-memory-leaks-in-a-nextjs-server)
- [441: Why is storing per-request data in module-level variables dangerous in Next.js?](#441-why-is-storing-per-request-data-in-module-level-variables-dangerous-in-nextjs)
- [442: How does React `cache` know the current request?](#442-how-does-react-cache-know-the-current-request)
- [443: How do you use `AsyncLocalStorage` in a Next.js app?](#443-how-do-you-use-asynclocalstorage-in-a-nextjs-app)
- [444: How do you implement feature flags that work with static pages?](#444-how-do-you-implement-feature-flags-that-work-with-static-pages)
- [445: How do you upgrade a large app from Next.js 15 to 16?](#445-how-do-you-upgrade-a-large-app-from-nextjs-15-to-16)
- [446: What was removed in Next.js 16?](#446-what-was-removed-in-nextjs-16)
- [447: How do you choose between ISR, Cache Components and full dynamic rendering for a new project?](#447-how-do-you-choose-between-isr-cache-components-and-full-dynamic-rendering-for-a-new-project)
- [448: How would you design caching for a news site with breaking news updates?](#448-how-would-you-design-caching-for-a-news-site-with-breaking-news-updates)
- [449: What are common performance mistakes in Next.js apps?](#449-what-are-common-performance-mistakes-in-nextjs-apps)
- [450: What questions would you ask before choosing Next.js for a project?](#450-what-questions-would-you-ask-before-choosing-nextjs-for-a-project)

---

# Easy Questions (1-150)

## 1: What is Next.js?

Next.js is a React framework made by Vercel. React gives you the tools to build UI components, and Next.js adds the parts you need to build a full application: routing, server rendering, data fetching, caching, image and font optimization, bundling, and a production server.

You can build anything from a static marketing site to a large app with a database, all in one project.

## 2: What are the main features of Next.js?

- File-system based routing (App Router and Pages Router)
- React Server Components and Client Components
- Server-side rendering (SSR), static generation (SSG) and incremental static regeneration (ISR)
- Server Actions for handling mutations
- Route Handlers for building API endpoints
- Built-in image, font and script optimization
- Metadata API for SEO
- Turbopack as the default bundler
- Proxy (formerly Middleware) for running code before a request finishes
- Support for CSS Modules, Tailwind CSS, Sass and global CSS
- TypeScript support out of the box

## 3: What is the difference between React and Next.js?

React is a library for building user interfaces. It doesn't decide how you do routing, how you fetch data, or how you render on the server.

Next.js is a framework built on top of React. It makes those decisions for you and gives you a router, a build system, server rendering, caching and a server to run your app. In short, you write React components, and Next.js handles everything around them.

## 4: How do you create a new Next.js project?

Use `create-next-app`:

```bash
npx create-next-app@latest my-app
```

It asks a few questions (TypeScript, ESLint or Biome, Tailwind CSS, `src/` folder, App Router, import alias). You can accept the recommended defaults. Then:

```bash
cd my-app
npm run dev
```

The app runs at `http://localhost:3000`.

## 5: What is the latest major version of Next.js and what does it require?

The current major version is Next.js 16. It requires:

- Node.js 20.9 or newer
- React 19.2 (the App Router uses the latest React canary features that Next.js ships with)
- TypeScript 5.1 or newer if you use TypeScript

Next.js 16 made Turbopack the default bundler, renamed `middleware.ts` to `proxy.ts`, added Cache Components and the `"use cache"` directive, and removed the `next lint` command.

## 6: What scripts are in a default Next.js `package.json`?

```json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  }
}
```

- `next dev` starts the development server with hot reloading.
- `next build` creates an optimized production build.
- `next start` runs the production build.

Older projects also had a `"lint": "next lint"` script. That command was removed in Next.js 16, so now you run `eslint` directly (for example `"lint": "eslint ."`).

## 7: What is the App Router?

The App Router is the router that lives in the `app` directory. It was introduced in Next.js 13 and is the recommended way to build Next.js apps today. It is built on React Server Components and supports layouts, nested routing, loading states, error handling, streaming, and Server Actions.

## 8: What is the Pages Router?

The Pages Router is the original Next.js router that lives in the `pages` directory. Each file in `pages` becomes a route. It uses functions like `getStaticProps` and `getServerSideProps` for data fetching. It is still supported, but new features are built for the App Router.

## 9: Can you use the App Router and Pages Router in the same project?

Yes. Both can live in one project, which helps when you migrate step by step. But one route can't be defined in both. If `app/about/page.tsx` and `pages/about.tsx` both exist, the build fails with a conflict error.

## 10: How does file-based routing work in the App Router?

Folders define the URL path, and a special `page` file makes that path public.

```
app/
  page.tsx            -> /
  about/
    page.tsx          -> /about
  blog/
    page.tsx          -> /blog
    [slug]/
      page.tsx        -> /blog/my-post
```

A folder without a `page.tsx` (or `route.ts`) is not reachable as a URL.

## 11: What is `page.tsx`?

`page.tsx` is the file that defines the UI for a route. It must export a React component as the default export.

```tsx
// app/about/page.tsx
export default function AboutPage() {
  return <h1>About us</h1>;
}
```

## 12: What is `layout.tsx`?

A layout is UI that is shared between several pages. It wraps its child pages and stays mounted when you move between them, so its state is kept and it doesn't re-render.

```tsx
// app/dashboard/layout.tsx
export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <section>
      <nav>Dashboard menu</nav>
      {children}
    </section>
  );
}
```

## 13: What is the root layout and why is it required?

The root layout is `app/layout.tsx`. It is required and it must contain the `<html>` and `<body>` tags, because Next.js doesn't add them for you.

```tsx
// app/layout.tsx
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
```

If you create a page without a root layout, Next.js creates one for you when you run `next dev`.

## 14: What are nested layouts?

Every folder can have its own `layout.tsx`. Layouts nest inside each other following the folder structure.

```
app/
  layout.tsx           (root layout)
  dashboard/
    layout.tsx         (dashboard layout)
    settings/
      page.tsx
```

When you visit `/dashboard/settings`, the page is wrapped by the dashboard layout, which is wrapped by the root layout.

## 15: What is the `public` folder used for?

The `public` folder holds static files like images, `robots.txt`, or a favicon. Files are served from the root of your site.

```
public/logo.png  ->  https://example.com/logo.png
```

```tsx
<img src="/logo.png" alt="Logo" />
```

Don't put files there that you want to keep private. Everything in `public` is accessible to anyone.

## 16: How do you navigate between pages in Next.js?

Use the `Link` component from `next/link`. It does client-side navigation, so the browser doesn't reload the whole page.

```tsx
import Link from "next/link";

export default function Nav() {
  return (
    <nav>
      <Link href="/">Home</Link>
      <Link href="/about">About</Link>
    </nav>
  );
}
```

## 17: Why use `Link` instead of a normal `<a>` tag?

A plain `<a>` tag makes the browser load a new page from scratch. `Link`:

- Navigates on the client without a full reload
- Keeps shared layouts and their state
- Prefetches the route when the link is visible in the viewport (in production)

`Link` still renders an `<a>` tag, so it works for SEO and accessibility.

## 18: What is prefetching in Next.js?

Prefetching means loading a route in the background before the user clicks on it. When a `Link` enters the viewport, Next.js fetches the data needed for that route. When the user clicks, the page shows up almost instantly.

Prefetching only runs in production. You can turn it off for a single link:

```tsx
<Link href="/heavy-page" prefetch={false}>
  Heavy page
</Link>
```

## 19: How do you create a dynamic route?

Wrap the folder name in square brackets.

```
app/blog/[slug]/page.tsx  ->  /blog/hello-world, /blog/another-post
```

```tsx
// app/blog/[slug]/page.tsx
export default async function BlogPost({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  return <h1>Post: {slug}</h1>;
}
```

## 20: Why is `params` a Promise?

Since Next.js 15, `params` and `searchParams` are Promises. In Next.js 16 the old synchronous access was removed completely, so you must `await` them (or use React's `use()` in a Client Component).

The reason is that Next.js can start rendering the parts of the page that don't depend on the URL before the request-specific values are known. This helps with streaming and with prerendering more of the page.

```tsx
export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  return <p>{id}</p>;
}
```

## 21: How do you read query string values (search params) in a page?

Pages get a `searchParams` prop, which is a Promise.

```tsx
// app/search/page.tsx  ->  /search?q=shoes
export default async function SearchPage({
  searchParams,
}: {
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>;
}) {
  const { q } = await searchParams;
  return <p>Searching for: {q}</p>;
}
```

Using `searchParams` makes the page render at request time, because the value is only known when the request comes in.

## 22: What are Server Components?

Server Components are React components that run only on the server. Their code is never sent to the browser. In the App Router, every component is a Server Component by default.

They can be `async`, so you can fetch data directly inside them:

```tsx
export default async function Users() {
  const res = await fetch("https://api.example.com/users");
  const users = await res.json();

  return (
    <ul>
      {users.map((u: { id: number; name: string }) => (
        <li key={u.id}>{u.name}</li>
      ))}
    </ul>
  );
}
```

## 23: What are Client Components?

Client Components are rendered on the server for the first HTML, and then they hydrate and run in the browser. You need them for interactivity: state, effects, event handlers, and browser APIs.

You mark a file as a Client Component with `"use client"` at the top.

```tsx
"use client";

import { useState } from "react";

export default function Counter() {
  const [count, setCount] = useState(0);
  return (
    <button onClick={() => setCount(count + 1)}>Clicked {count} times</button>
  );
}
```

## 24: What does `"use client"` do?

It marks a boundary between server and client code. The file with `"use client"`, and all modules it imports, become part of the client bundle. You only need to add it to the entry point of the client part, not to every file.

It must be at the very top of the file, before any imports.

## 25: When should you use a Server Component and when a Client Component?

Use a Server Component when you:

- Fetch data or read from a database
- Use secrets like API keys
- Want to send less JavaScript to the browser

Use a Client Component when you:

- Use state (`useState`, `useReducer`)
- Use effects (`useEffect`)
- Add event handlers like `onClick` or `onChange`
- Use browser APIs like `localStorage` or `window`
- Use hooks that depend on these, or libraries that need them

A good habit is to keep most components on the server and move only the interactive parts to the client.

## 26: Can you use `useState` in a Server Component?

No. Server Components don't have state or lifecycle. They render once on the server per request (or at build time). If you try to use `useState`, `useEffect` or event handlers, you get an error. Move that part into a Client Component.

## 27: What is server-side rendering (SSR)?

SSR means the HTML for a page is generated on the server for every request. The user gets a fully rendered page right away, which is good for SEO and first load. Then React hydrates the page in the browser to make it interactive.

In the App Router, a route is rendered on each request when it uses request-time data such as `cookies()`, `headers()`, `searchParams`, or uncached data.

## 28: What is static site generation (SSG)?

SSG means the HTML is generated once at build time and then served to every user. It is very fast because the server doesn't have to render anything per request, and the files can be served from a CDN.

In the App Router, a route is prerendered at build time when it doesn't use any request-time data.

## 29: What is client-side rendering (CSR)?

CSR means the browser downloads JavaScript and renders the page in the browser. The first HTML is mostly empty. This is how a plain React app with Vite works.

In Next.js you get CSR for parts of a page when you fetch data in a Client Component, for example with `useEffect` or a library like SWR or TanStack Query.

## 30: What is hydration?

Hydration is the step where React takes the HTML that came from the server and attaches event handlers and state to it, so the page becomes interactive. The HTML is visible before hydration, but buttons won't respond until hydration is done.

## 31: What is a hydration error?

A hydration error happens when the HTML rendered on the server doesn't match what React renders on the first pass in the browser. Common causes:

- Using `Date.now()`, `Math.random()` or `new Date()` during render
- Checking `typeof window !== 'undefined'` to render different content
- Invalid HTML nesting like a `<div>` inside a `<p>`
- Browser extensions that change the HTML

To fix it, make the first render the same on both sides, and move browser-only logic into `useEffect`.

## 32: How do you add global CSS?

Create a CSS file and import it in the root layout.

```css
/* app/globals.css */
body {
  margin: 0;
  font-family: system-ui, sans-serif;
}
```

```tsx
// app/layout.tsx
import "./globals.css";
```

## 33: What are CSS Modules?

CSS Modules are CSS files ending with `.module.css`. Class names in them are scoped to the component, so they don't clash with other files.

```css
/* app/components/button.module.css */
.primary {
  background: blue;
  color: white;
}
```

```tsx
import styles from "./button.module.css";

export function Button() {
  return <button className={styles.primary}>Save</button>;
}
```

## 34: How do you use Tailwind CSS in Next.js?

`create-next-app` can set it up for you. If you add it manually with Tailwind v4:

```bash
npm install tailwindcss @tailwindcss/postcss
```

```js
// postcss.config.mjs
export default {
  plugins: {
    "@tailwindcss/postcss": {},
  },
};
```

```css
/* app/globals.css */
@import "tailwindcss";
```

Then import `globals.css` in your root layout and use classes like `className="p-4 text-lg"`.

## 35: Does Next.js support Sass?

Yes. Install the `sass` package and you can import `.scss` and `.sass` files, including Sass modules like `styles.module.scss`.

```bash
npm install --save-dev sass
```

You can pass options with `sassOptions` in `next.config.ts`.

## 36: How do you add an image in Next.js?

Use the `Image` component from `next/image`.

```tsx
import Image from "next/image";

export default function Avatar() {
  return <Image src="/me.png" alt="My photo" width={200} height={200} />;
}
```

## 37: What are the benefits of the `next/image` component?

- Serves smaller images in modern formats like WebP or AVIF
- Creates different sizes for different screens
- Lazy loads images by default, so images below the fold load only when needed
- Prevents layout shift because the space is reserved from `width` and `height`
- Can show a blurred placeholder while the image loads

## 38: Why do you need `width` and `height` on `next/image`?

So the browser knows the aspect ratio before the image loads and can reserve space for it. That prevents layout shift.

You don't need them when:

- You import a local image statically (Next.js reads the size from the file)
- You use the `fill` prop, where the image fills its parent

## 39: How do you use a remote image with `next/image`?

You must allow the domain in `next.config.ts` with `remotePatterns`.

```ts
// next.config.ts
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: "https",
        hostname: "images.example.com",
        pathname: "/uploads/**",
      },
    ],
  },
};

export default nextConfig;
```

The older `images.domains` option is deprecated. Use `remotePatterns` instead.

## 40: What is the `fill` prop on `next/image`?

`fill` makes the image take the full size of its parent element. The parent must have `position: relative` (or `fixed` / `absolute`). It is useful when you don't know the image size ahead of time.

```tsx
<div style={{ position: "relative", width: "100%", height: 300 }}>
  <Image
    src="/banner.jpg"
    alt="Banner"
    fill
    style={{ objectFit: "cover" }}
    sizes="100vw"
  />
</div>
```

## 41: How do you load an important image right away instead of lazy loading it?

For the main image at the top of the page (often the Largest Contentful Paint element), use the `preload` prop in Next.js 16. The older `priority` prop is deprecated.

```tsx
<Image src="/hero.jpg" alt="Hero" width={1200} height={600} preload />
```

You can also use `loading="eager"` or `fetchPriority="high"` depending on what you need.

## 42: How do you add fonts in Next.js?

Use `next/font`. It downloads Google fonts at build time and serves them from your own domain, so there are no requests to Google from the browser.

```tsx
// app/layout.tsx
import { Inter } from "next/font/google";

const inter = Inter({ subsets: ["latin"] });

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={inter.className}>
      <body>{children}</body>
    </html>
  );
}
```

## 43: How do you use a local font file?

Use `next/font/local`.

```tsx
import localFont from "next/font/local";

const myFont = localFont({
  src: "./fonts/MyFont.woff2",
  display: "swap",
});

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={myFont.className}>
      <body>{children}</body>
    </html>
  );
}
```

## 44: What is the benefit of `next/font`?

- Fonts are self-hosted, so no extra connection to a font provider
- No layout shift, because Next.js adjusts the fallback font to match the size of the real font
- Fonts are preloaded and only the subsets you ask for are included
- Better privacy, because the user's browser doesn't talk to Google

## 45: How do you set the page title and description?

Export a `metadata` object from a `page.tsx` or `layout.tsx`. This only works in Server Components.

```tsx
// app/about/page.tsx
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "About us",
  description: "Learn more about our team.",
};

export default function Page() {
  return <h1>About</h1>;
}
```

## 46: How do you add a favicon?

Put a `favicon.ico` file in the `app` folder. Next.js adds the right `<link>` tag automatically. You can also add `icon.png` or `apple-icon.png` in the `app` folder for other icons.

## 47: What is `loading.tsx`?

`loading.tsx` shows a fallback UI while the content of a route segment is loading. Next.js wraps the page in a React `<Suspense>` boundary and shows this file as the fallback.

```tsx
// app/dashboard/loading.tsx
export default function Loading() {
  return <p>Loading dashboard...</p>;
}
```

## 48: What is `error.tsx`?

`error.tsx` catches errors that happen while rendering a route segment and shows a fallback UI instead of crashing the whole app. It must be a Client Component.

```tsx
// app/dashboard/error.tsx
"use client";

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  return (
    <div>
      <h2>Something went wrong</h2>
      <button onClick={() => reset()}>Try again</button>
    </div>
  );
}
```

## 49: What is `not-found.tsx`?

It is the UI that shows when a route doesn't exist or when you call the `notFound()` function. The root `app/not-found.tsx` handles all unknown URLs in your app.

```tsx
// app/not-found.tsx
import Link from "next/link";

export default function NotFound() {
  return (
    <div>
      <h2>Page not found</h2>
      <Link href="/">Go home</Link>
    </div>
  );
}
```

## 50: How do you show a 404 page from code?

Call `notFound()` from `next/navigation`.

```tsx
import { notFound } from "next/navigation";

export default async function Post({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  const post = await getPost(id);

  if (!post) {
    notFound();
  }

  return <h1>{post.title}</h1>;
}
```

`notFound()` throws a special error, so the code after it doesn't run.

## 51: How do you redirect a user in a Server Component?

Use `redirect()` from `next/navigation`.

```tsx
import { redirect } from "next/navigation";

export default async function Profile() {
  const user = await getUser();

  if (!user) {
    redirect("/login");
  }

  return <h1>Hello {user.name}</h1>;
}
```

## 52: What is the difference between `redirect()` and `permanentRedirect()`?

- `redirect()` sends a temporary redirect (307, or 303 when used in a Server Action).
- `permanentRedirect()` sends a permanent redirect (308). Use it when a URL has moved for good, for example after a user changes their username.

## 53: How do you navigate from code in a Client Component?

Use the `useRouter` hook from `next/navigation`.

```tsx
"use client";

import { useRouter } from "next/navigation";

export default function LoginButton() {
  const router = useRouter();

  return (
    <button onClick={() => router.push("/dashboard")}>Go to dashboard</button>
  );
}
```

## 54: What methods does `useRouter` provide?

- `router.push(href)` navigates and adds a history entry
- `router.replace(href)` navigates without adding a history entry
- `router.refresh()` re-fetches the current route from the server without losing client state
- `router.back()` goes back in history
- `router.forward()` goes forward in history
- `router.prefetch(href)` prefetches a route

## 55: What is the difference between `next/router` and `next/navigation`?

- `next/router` is for the Pages Router.
- `next/navigation` is for the App Router.

In the App Router, always import `useRouter`, `usePathname`, `useSearchParams` and `useParams` from `next/navigation`. Importing `useRouter` from `next/router` in the `app` folder throws an error.

## 56: How do you get the current path in a Client Component?

Use `usePathname`.

```tsx
"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

export function NavLink({
  href,
  children,
}: {
  href: string;
  children: React.ReactNode;
}) {
  const pathname = usePathname();
  const isActive = pathname === href;

  return (
    <Link href={href} className={isActive ? "font-bold" : ""}>
      {children}
    </Link>
  );
}
```

## 57: How do you read search params in a Client Component?

Use `useSearchParams`.

```tsx
"use client";

import { useSearchParams } from "next/navigation";

export function SortLabel() {
  const searchParams = useSearchParams();
  const sort = searchParams.get("sort") ?? "newest";
  return <span>Sorted by {sort}</span>;
}
```

The returned object is read-only. To change it, build a new URL and call `router.push` or `router.replace`.

## 58: How do you read route params in a Client Component?

Use the `useParams` hook.

```tsx
"use client";

import { useParams } from "next/navigation";

export function PostId() {
  const params = useParams<{ slug: string }>();
  return <p>Slug: {params.slug}</p>;
}
```

## 59: What are environment variables in Next.js?

Next.js loads environment variables from `.env` files into `process.env`.

```
# .env.local
DATABASE_URL=postgres://...
NEXT_PUBLIC_API_URL=https://api.example.com
```

Variables are only available on the server, unless their name starts with `NEXT_PUBLIC_`.

## 60: What does the `NEXT_PUBLIC_` prefix do?

It makes an environment variable available in the browser. Next.js replaces `process.env.NEXT_PUBLIC_...` with the actual value at build time and puts it into the JavaScript bundle.

Never put secrets in `NEXT_PUBLIC_` variables, because anyone can read them in the browser.

## 61: What `.env` files does Next.js support, and in what order are they loaded?

Next.js looks for these files, from highest to lowest priority:

1. `process.env` (variables already set in the environment)
2. `.env.$(NODE_ENV).local` (for example `.env.development.local`)
3. `.env.local` (not loaded when `NODE_ENV` is `test`)
4. `.env.$(NODE_ENV)` (for example `.env.production`)
5. `.env`

`.env*.local` files should be in `.gitignore`, because they usually contain secrets.

## 62: What is a Route Handler?

A Route Handler lets you create an API endpoint in the App Router. You create a `route.ts` file and export functions named after HTTP methods.

```ts
// app/api/hello/route.ts
export async function GET() {
  return Response.json({ message: "Hello" });
}

export async function POST(request: Request) {
  const body = await request.json();
  return Response.json({ received: body }, { status: 201 });
}
```

## 63: Which HTTP methods do Route Handlers support?

`GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD` and `OPTIONS`. If a method is not exported, Next.js returns `405 Method Not Allowed`. If you don't export `OPTIONS`, Next.js handles it for you and sets the `Allow` header.

## 64: Can `route.ts` and `page.tsx` be in the same folder?

No. A route segment can have either a page or a route handler, not both. For example, `app/api/users/route.ts` is fine, but adding `app/api/users/page.tsx` next to it causes an error.

## 65: What are API Routes in the Pages Router?

In the Pages Router, any file in `pages/api` is an API endpoint.

```ts
// pages/api/hello.ts
import type { NextApiRequest, NextApiResponse } from "next";

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  res.status(200).json({ message: "Hello" });
}
```

In the App Router, you use Route Handlers instead.

## 66: What is `next.config.ts`?

It is the configuration file for Next.js. It sits in the root of the project. Next.js supports `next.config.js`, `next.config.mjs` and `next.config.ts`.

```ts
// next.config.ts
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  reactStrictMode: true,
  images: {
    remotePatterns: [{ protocol: "https", hostname: "cdn.example.com" }],
  },
};

export default nextConfig;
```

## 67: What is Turbopack?

Turbopack is a bundler written in Rust and built by the Next.js team. It replaces webpack. Since Next.js 16, it is the default for both `next dev` and `next build`. It makes the dev server start faster and updates faster when you change code.

## 68: How do you use webpack instead of Turbopack?

Pass the `--webpack` flag.

```json
{
  "scripts": {
    "dev": "next dev --webpack",
    "build": "next build --webpack"
  }
}
```

You may need this if your project depends on a custom webpack config or plugin that Turbopack doesn't support.

## 69: Does Next.js support TypeScript?

Yes. If you add a `.ts` or `.tsx` file, Next.js sets up `tsconfig.json` for you. Next.js also creates a `next-env.d.ts` file with type references. You shouldn't edit that file and it is fine to add it to `.gitignore`.

`create-next-app` uses TypeScript by default.

## 70: What is the `src` folder in a Next.js project?

It is optional. You can put `app`, `pages` and other code inside a `src` folder to keep your app code apart from config files in the project root.

```
src/
  app/
    page.tsx
  components/
next.config.ts
package.json
```

The `public` folder and config files still stay in the root.

## 71: What is the `@/` import alias?

It is a path alias set in `tsconfig.json` (or `jsconfig.json`), so you don't have to write long relative paths.

```json
{
  "compilerOptions": {
    "paths": {
      "@/*": ["./src/*"]
    }
  }
}
```

```tsx
// instead of '../../../components/button'
import { Button } from "@/components/button";
```

## 72: What is a route segment?

Each folder in the URL path is a route segment. For `/dashboard/settings/profile`, the segments are `dashboard`, `settings` and `profile`. Each segment can have its own `layout`, `loading`, `error` and `page` files.

## 73: What special files can a route segment have?

- `layout.tsx` shared UI for the segment and its children
- `page.tsx` the UI of the route
- `loading.tsx` loading UI (Suspense fallback)
- `error.tsx` error UI (error boundary)
- `not-found.tsx` UI for 404
- `template.tsx` like a layout, but re-mounts on navigation
- `route.ts` an API endpoint
- `default.tsx` fallback for parallel routes
- `forbidden.tsx` and `unauthorized.tsx` (experimental) for 403 and 401

## 74: In what order are the special files rendered?

From outside to inside:

```tsx
<Layout>
  <Template>
    <ErrorBoundary fallback={<Error />}>
      <Suspense fallback={<Loading />}>
        <NotFoundBoundary fallback={<NotFound />}>
          <Page />
        </NotFoundBoundary>
      </Suspense>
    </ErrorBoundary>
  </Template>
</Layout>
```

Because the error boundary is inside the layout, `error.tsx` in a segment can't catch errors thrown by the `layout.tsx` of the same segment.

## 75: What is a route group?

A folder with its name in parentheses, like `(marketing)`. It groups routes without adding anything to the URL.

```
app/
  (marketing)/
    about/page.tsx      -> /about
    pricing/page.tsx    -> /pricing
  (shop)/
    cart/page.tsx       -> /cart
```

You use route groups to organize files or to give different groups different layouts.

## 76: Can you have more than one root layout?

Yes, by using route groups. Remove the top-level `app/layout.tsx` and add a `layout.tsx` inside each group. Each one must have its own `<html>` and `<body>` tags.

```
app/
  (marketing)/
    layout.tsx
    page.tsx
  (app)/
    layout.tsx
    dashboard/page.tsx
```

Moving between pages that use different root layouts causes a full page load.

## 77: What is a private folder?

A folder whose name starts with an underscore, like `_components`. Next.js ignores it for routing, so nothing inside it becomes a route. It is a clean way to keep helper files next to your routes.

```
app/
  blog/
    _components/
      post-card.tsx
    page.tsx
```

## 78: Can you put non-route files inside the `app` folder?

Yes. Only `page` and `route` files make a route public. You can put components, styles and tests inside route folders and they won't be accessible as URLs. This is called colocation.

## 79: What is a catch-all route?

A dynamic segment with three dots, `[...slug]`. It matches the segment and everything after it.

```
app/docs/[...slug]/page.tsx
```

| URL         | params                 |
| ----------- | ---------------------- |
| `/docs/a`   | `{ slug: ['a'] }`      |
| `/docs/a/b` | `{ slug: ['a', 'b'] }` |
| `/docs`     | no match (404)         |

## 80: What is an optional catch-all route?

The same as catch-all, but with double brackets: `[[...slug]]`. It also matches the route without any extra segments.

```
app/docs/[[...slug]]/page.tsx
```

| URL         | params                 |
| ----------- | ---------------------- |
| `/docs`     | `{}`                   |
| `/docs/a`   | `{ slug: ['a'] }`      |
| `/docs/a/b` | `{ slug: ['a', 'b'] }` |

## 81: How do you add a link to a dynamic route?

Build the URL as a string.

```tsx
import Link from "next/link";

export function PostList({
  posts,
}: {
  posts: { slug: string; title: string }[];
}) {
  return (
    <ul>
      {posts.map((post) => (
        <li key={post.slug}>
          <Link href={`/blog/${post.slug}`}>{post.title}</Link>
        </li>
      ))}
    </ul>
  );
}
```

## 82: Can you pass an object to `href` in `Link`?

Yes. You can pass a URL object with `pathname` and `query`.

```tsx
<Link href={{ pathname: "/search", query: { q: "next" } }}>Search</Link>
// renders /search?q=next
```

## 83: How do you stop `Link` from scrolling to the top after navigation?

By default, Next.js scrolls to the top of the new page. You can turn this off with `scroll={false}`.

```tsx
<Link href="/products?page=2" scroll={false}>
  Next page
</Link>
```

The same option exists on the router: `router.push('/products?page=2', { scroll: false })`.

## 84: What does the `replace` prop on `Link` do?

It replaces the current history entry instead of adding a new one. When the user presses the back button, they skip the replaced page.

```tsx
<Link href="/step-2" replace>
  Continue
</Link>
```

## 85: How do you link to a section on a page?

Add a hash to the URL.

```tsx
<Link href="/docs#installation">Installation</Link>
```

Next.js scrolls to the element with `id="installation"`.

## 86: What is `next/script`?

A component for loading third-party scripts, like analytics or chat widgets, with control over when they load.

```tsx
import Script from "next/script";

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <>
      {children}
      <Script src="https://example.com/widget.js" strategy="lazyOnload" />
    </>
  );
}
```

## 87: What loading strategies does `next/script` support?

- `beforeInteractive` loads before any Next.js code and before hydration. Use it only for scripts that must run early, like bot detection. It must be placed in the root layout.
- `afterInteractive` (default) loads after some hydration has happened. Good for analytics and tag managers.
- `lazyOnload` loads when the browser is idle. Good for chat widgets and social embeds.
- `worker` (experimental) loads the script in a web worker using Partytown.

## 88: How do you run code after a script loads?

Use `onLoad` (or `onReady`). These callbacks only work in Client Components.

```tsx
"use client";

import Script from "next/script";

export function Maps() {
  return (
    <Script
      src="https://maps.example.com/api.js"
      onLoad={() => console.log("Maps script loaded")}
    />
  );
}
```

## 89: What is `@next/third-parties`?

It is a package with ready-made components for popular third-party services. They are tuned for performance.

```tsx
import { GoogleAnalytics } from "@next/third-parties/google";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
      <GoogleAnalytics gaId="G-XXXXXXX" />
    </html>
  );
}
```

It also has `GoogleTagManager`, `GoogleMapsEmbed` and `YouTubeEmbed`.

## 90: How do you fetch data in a Server Component?

Make the component `async` and use `await`.

```tsx
export default async function Page() {
  const res = await fetch("https://api.example.com/posts");
  const posts: { id: number; title: string }[] = await res.json();

  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
}
```

You can also query a database or use an ORM directly, since this code only runs on the server.

## 91: Can you query a database directly in a Server Component?

Yes. Server Components run on the server, so you can use any database client or ORM.

```tsx
import { db } from "@/lib/db";

export default async function Page() {
  const users = await db.user.findMany();
  return <p>{users.length} users</p>;
}
```

The database code and credentials are never sent to the browser.

## 92: How do you fetch data in a Client Component?

You can use `useEffect`, but a data fetching library like SWR or TanStack Query is usually better because it handles caching, loading states and refetching.

```tsx
"use client";

import useSWR from "swr";

const fetcher = (url: string) => fetch(url).then((r) => r.json());

export function Profile() {
  const { data, error, isLoading } = useSWR("/api/user", fetcher);

  if (error) return <p>Failed to load</p>;
  if (isLoading) return <p>Loading...</p>;
  return <p>Hello {data.name}</p>;
}
```

You can also pass a Promise from a Server Component and read it with React's `use()` hook.

## 93: Is `fetch` cached by default in the App Router?

No. Since Next.js 15, `fetch` requests are not cached by default. To cache a request, pass `cache: 'force-cache'` or set a revalidate time.

```ts
// cached
await fetch("https://api.example.com/posts", { cache: "force-cache" });

// cached and refreshed at most every 60 seconds
await fetch("https://api.example.com/posts", { next: { revalidate: 60 } });
```

In Next.js 13 and 14 the default was to cache, so older tutorials may say otherwise.

## 94: What is a Server Action?

A Server Action is an async function that runs on the server, and you can call it from a form or from client code. You mark it with `"use server"`. It is the usual way to handle form submissions and data changes in the App Router.

```tsx
// app/todos/page.tsx
export default function Page() {
  async function addTodo(formData: FormData) {
    "use server";
    const title = formData.get("title") as string;
    await db.todo.create({ data: { title } });
  }

  return (
    <form action={addTodo}>
      <input name="title" />
      <button type="submit">Add</button>
    </form>
  );
}
```

## 95: What does `"use server"` mean?

It marks a function, or every exported function in a file, as a Server Function that can be called from the client. When the client calls it, Next.js sends a POST request to the server, runs the function there, and sends the result back.

It does not mean "this is a Server Component". Server Components don't need any directive.

## 96: Can Server Actions be in a separate file?

Yes, and that is the common way to share them. Put `"use server"` at the top of the file. Every exported function becomes a Server Action.

```ts
// app/actions.ts
"use server";

export async function createPost(formData: FormData) {
  const title = formData.get("title");
  // save to the database
}
```

Client Components can import Server Actions only from files like this, not define them inline.

## 97: How do you refresh the page data after a Server Action?

Call `revalidatePath` or `revalidateTag` from `next/cache`, or `refresh()` when you only need to refresh the current page.

```ts
"use server";

import { revalidatePath } from "next/cache";

export async function addComment(formData: FormData) {
  await db.comment.create({ data: { text: formData.get("text") as string } });
  revalidatePath("/posts");
}
```

## 98: What is `template.tsx`?

A template is like a layout because it wraps its children, but it creates a new instance every time the user navigates. State is reset and effects run again. You might use it for enter animations or for logging page views on every navigation.

```tsx
// app/template.tsx
export default function Template({ children }: { children: React.ReactNode }) {
  return <div className="fade-in">{children}</div>;
}
```

## 99: How do you run the production build locally?

```bash
npm run build
npm run start
```

`next build` creates the optimized build in the `.next` folder, and `next start` serves it on port 3000. Use `-p` to change the port: `next start -p 4000`.

## 100: How do you change the port of the dev server?

```bash
next dev -p 4000
```

You can also set the `PORT` environment variable.

## 101: What is the `.next` folder?

It is the output folder created by `next dev` and `next build`. It contains compiled code, cache, and build files. You shouldn't edit it or commit it to git. In Next.js 16, `next dev` writes to `.next/dev`, so you can run the dev server and a build at the same time.

## 102: What does the build output mean?

After `next build`, you see a list of routes with symbols:

- `○ (Static)` prerendered as static content
- `● (SSG)` prerendered as static HTML using `generateStaticParams`
- `◐ (Partial Prerender)` a static shell with parts that stream in at request time
- `ƒ (Dynamic)` rendered on the server for each request

This helps you check which routes are static and which are dynamic.

## 103: How do you deploy a Next.js app?

Common options:

- **Vercel**: connect your git repo and it deploys automatically.
- **Node.js server**: run `next build` and `next start` on any server.
- **Docker**: build an image using `output: 'standalone'` for a smaller image.
- **Static export**: use `output: 'export'` and host the files on any static host (with some features not available).
- **Other platforms**: Netlify, Cloudflare, AWS Amplify and others have Next.js support.

## 104: Do you need Vercel to run Next.js?

No. Next.js is open source and can run anywhere Node.js runs. Vercel makes deployment easy, but features like SSR, ISR, image optimization and Server Actions all work with `next start` on your own server.

## 105: What is the `metadata` object used for?

It sets tags in the `<head>` of the page, like title, description, Open Graph and Twitter cards.

```tsx
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "My blog",
  description: "Posts about web development",
  openGraph: {
    title: "My blog",
    images: ["/og.png"],
  },
};
```

## 106: Can you export `metadata` from a Client Component?

No. The `metadata` object and `generateMetadata` only work in Server Components. If your page needs to be a Client Component, move the interactive part into a separate component and keep the page itself as a Server Component.

## 107: What is a title template?

A title template lets child pages add their own title to a shared pattern. You set it in a layout.

```tsx
// app/layout.tsx
export const metadata: Metadata = {
  title: {
    template: "%s | Acme",
    default: "Acme",
  },
};
```

```tsx
// app/about/page.tsx
export const metadata: Metadata = {
  title: "About", // becomes "About | Acme"
};
```

## 108: What is the `viewport` export?

Viewport and theme color settings are exported separately from `metadata`.

```tsx
import type { Viewport } from "next";

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  themeColor: "#000000",
};
```

Putting `themeColor` or `viewport` inside `metadata` is deprecated.

## 109: How do you add a `robots.txt` file?

You can add a static `app/robots.txt` file, or generate it with `app/robots.ts`.

```ts
// app/robots.ts
import type { MetadataRoute } from "next";

export default function robots(): MetadataRoute.Robots {
  return {
    rules: { userAgent: "*", allow: "/", disallow: "/admin/" },
    sitemap: "https://example.com/sitemap.xml",
  };
}
```

## 110: How do you create a sitemap?

Create `app/sitemap.ts` and return a list of URLs.

```ts
// app/sitemap.ts
import type { MetadataRoute } from "next";

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const posts = await getPosts();

  return [
    { url: "https://example.com", lastModified: new Date() },
    ...posts.map((post) => ({
      url: `https://example.com/blog/${post.slug}`,
      lastModified: post.updatedAt,
    })),
  ];
}
```

## 111: How do you add an Open Graph image?

Put an `opengraph-image.png` (or `.jpg`) in a route folder. Next.js adds the right meta tags. You can also generate it with code in `opengraph-image.tsx` using `ImageResponse` from `next/og`.

```
app/
  opengraph-image.png
  blog/
    opengraph-image.png
```

## 112: What is Proxy in Next.js?

Proxy is code that runs before a request is finished. You can use it to redirect, rewrite, change headers, or check cookies. It lives in `proxy.ts` in the project root (or in `src`).

```ts
// proxy.ts
import { NextResponse, type NextRequest } from "next/server";

export function proxy(request: NextRequest) {
  if (!request.cookies.has("session")) {
    return NextResponse.redirect(new URL("/login", request.url));
  }
  return NextResponse.next();
}

export const config = {
  matcher: ["/dashboard/:path*"],
};
```

## 113: Why was Middleware renamed to Proxy?

In Next.js 16, `middleware.ts` was renamed to `proxy.ts` and the exported function is now called `proxy`. The name "middleware" made people think it worked like Express middleware and they put too much logic in it. "Proxy" better describes what it does: it sits in front of your app and can redirect, rewrite or change requests. `middleware.ts` still works for now but it is deprecated. You can move to the new name with a codemod:

```bash
npx @next/codemod@canary middleware-to-proxy .
```

## 114: What is the `matcher` in Proxy?

It decides which paths the proxy runs on. Without it, the proxy runs on every request, including static files.

```ts
export const config = {
  matcher: [
    // run on everything except static files and images
    "/((?!api|_next/static|_next/image|favicon.ico).*)",
  ],
};
```

## 115: How do you read cookies in a Server Component?

Use `cookies()` from `next/headers`. It is async.

```tsx
import { cookies } from "next/headers";

export default async function Page() {
  const cookieStore = await cookies();
  const theme = cookieStore.get("theme")?.value ?? "light";
  return <p>Theme: {theme}</p>;
}
```

## 116: How do you read request headers in a Server Component?

Use `headers()` from `next/headers`. It is async and read-only.

```tsx
import { headers } from "next/headers";

export default async function Page() {
  const headerList = await headers();
  const userAgent = headerList.get("user-agent");
  return <p>{userAgent}</p>;
}
```

## 117: Can you set a cookie in a Server Component?

No. A Server Component renders after the response headers may already be sent, so it can't set cookies. You can set cookies in:

- Server Actions
- Route Handlers
- Proxy

```ts
"use server";

import { cookies } from "next/headers";

export async function setTheme(theme: string) {
  const cookieStore = await cookies();
  cookieStore.set("theme", theme);
}
```

## 118: What is `next/dynamic`?

It lets you load a component lazily, so its code is split into a separate chunk and only loaded when it is needed.

```tsx
"use client";

import dynamic from "next/dynamic";

const Chart = dynamic(() => import("./chart"), {
  loading: () => <p>Loading chart...</p>,
});

export default function Dashboard() {
  return <Chart />;
}
```

## 119: How do you load a component only in the browser?

Use `next/dynamic` with `ssr: false`. This only works inside a Client Component.

```tsx
"use client";

import dynamic from "next/dynamic";

const Map = dynamic(() => import("./map"), { ssr: false });

export function Location() {
  return <Map />;
}
```

This is useful for libraries that use `window` when they load.

## 120: What is code splitting?

Code splitting means breaking the JavaScript into smaller chunks so the browser only loads what it needs for the current page. Next.js does this automatically per route. You can split further with `next/dynamic` or `React.lazy`.

## 121: What is Fast Refresh?

Fast Refresh is the hot reloading feature in development. When you save a file, the change shows in the browser in about a second without losing component state. If you edit a file that is not a component, Next.js reloads the modules that depend on it.

## 122: What does `reactStrictMode` do?

It turns on React Strict Mode, which helps you find bugs in development. For example, it runs effects twice to show missing cleanup. In the App Router it is on by default. In the Pages Router you enable it in `next.config.ts`:

```ts
const nextConfig = {
  reactStrictMode: true,
};
```

## 123: How do you add redirects in `next.config.ts`?

Use the `redirects` function.

```ts
const nextConfig = {
  async redirects() {
    return [
      {
        source: "/old-blog/:slug",
        destination: "/blog/:slug",
        permanent: true,
      },
    ];
  },
};
```

`permanent: true` uses status code 308 and `false` uses 307.

## 124: What is a rewrite?

A rewrite maps a URL to a different path without changing what the user sees in the address bar.

```ts
const nextConfig = {
  async rewrites() {
    return [
      {
        source: "/docs/:path*",
        destination: "https://docs.example.com/:path*",
      },
    ];
  },
};
```

The user stays on `/docs/...` but the content comes from the other site.

## 125: What is the difference between a redirect and a rewrite?

- A **redirect** tells the browser to go to a new URL. The address bar changes.
- A **rewrite** serves content from another path or site while keeping the same URL in the address bar.

## 126: How do you add custom headers to responses?

Use the `headers` function in `next.config.ts`.

```ts
const nextConfig = {
  async headers() {
    return [
      {
        source: "/(.*)",
        headers: [
          { key: "X-Frame-Options", value: "DENY" },
          { key: "X-Content-Type-Options", value: "nosniff" },
        ],
      },
    ];
  },
};
```

## 127: What is a static export?

It builds your app into plain HTML, CSS and JS files that you can host on any static server, without a Node.js server.

```ts
const nextConfig = {
  output: "export",
};
```

After `next build`, the files are in the `out` folder.

## 128: Which features don't work with a static export?

Anything that needs a server at request time:

- Cookies, headers and other request-time APIs
- Proxy
- Rewrites, redirects and headers from `next.config`
- Server Actions
- ISR and on-demand revalidation
- Dynamic routes without `generateStaticParams`
- Default image optimization (you need a custom loader or `unoptimized: true`)

Route Handlers only work with `GET` and must be static.

## 129: How do you add a global "loading" bar or progress indicator on navigation?

Next.js shows `loading.tsx` for slow segments. For a small indicator on a link, you can use `useLinkStatus` from `next/link`. It tells you if the navigation started by that link is still pending.

```tsx
"use client";

import { useLinkStatus } from "next/link";

export function LinkHint() {
  const { pending } = useLinkStatus();
  return pending ? <span className="spinner" aria-hidden /> : null;
}
```

```tsx
<Link href="/reports">
  Reports <LinkHint />
</Link>
```

`useLinkStatus` must be used inside a descendant of `Link`.

## 130: What is the `<Form>` component from `next/form`?

It is an HTML form with extra features for forms that change the URL, like search forms. When `action` is a string, it does a client-side navigation with the form values as search params and prefetches the target route.

```tsx
import Form from "next/form";

export default function SearchBox() {
  return (
    <Form action="/search">
      <input name="query" />
      <button type="submit">Search</button>
    </Form>
  );
}
```

Submitting navigates to `/search?query=...` without a full page reload. When `action` is a function, it works like a normal React form with a Server Action.

## 131: What is the difference between `next build` and `next dev`?

- `next dev` runs in development mode. It compiles routes on demand, shows detailed errors, and supports Fast Refresh. It is not optimized.
- `next build` creates a production build. Code is minified, static pages are prerendered, and the result is optimized for speed.

Never use `next dev` in production.

## 132: What does `next info` do?

It prints information about your system and installed versions of Next.js, React and Node.js. It is useful when you report a bug.

```bash
npx next info
```

## 133: How do you upgrade Next.js?

Run the upgrade command or install the latest versions:

```bash
npx @next/codemod@canary upgrade latest
# or
npm install next@latest react@latest react-dom@latest
```

The codemod tool also updates code for breaking changes, for example making `params` async or renaming `middleware.ts` to `proxy.ts`.

## 134: What are codemods?

Codemods are scripts that change your code automatically to fix breaking changes between versions. Next.js provides them in `@next/codemod`.

```bash
npx @next/codemod@latest next-async-request-api .
```

## 135: How do you set up ESLint in Next.js 16?

`next lint` was removed, so you use the ESLint CLI directly with `eslint-config-next`, which uses the flat config format.

```js
// eslint.config.mjs
import nextVitals from "eslint-config-next/core-web-vitals";

export default [...nextVitals];
```

```json
{
  "scripts": {
    "lint": "eslint ."
  }
}
```

`next build` also no longer runs the linter for you. `create-next-app` can also set up Biome instead of ESLint.

## 136: What is the `children` prop in a layout?

It is the content of the page or nested layout inside it. A layout must render `children`, otherwise the page won't show.

```tsx
export default function Layout({ children }: { children: React.ReactNode }) {
  return <main>{children}</main>;
}
```

## 137: Do layouts receive `searchParams`?

No. Only pages get `searchParams`. Layouts don't re-render on navigation between pages that share them, so their search params could be out of date. If a layout needs them, read them in a Client Component with `useSearchParams`.

## 138: Can a Server Component import a Client Component?

Yes. This is the normal way to add interactivity.

```tsx
// app/page.tsx (Server Component)
import LikeButton from "./like-button"; // Client Component

export default async function Page() {
  const post = await getPost();
  return (
    <article>
      <h1>{post.title}</h1>
      <LikeButton postId={post.id} />
    </article>
  );
}
```

Props passed from a Server Component to a Client Component must be serializable (strings, numbers, plain objects, arrays, Dates, Promises and so on), not functions or class instances.

## 139: Can a Client Component import a Server Component?

Not directly. If a Client Component imports a component file, that file also becomes client code. But you can pass a Server Component as `children` or another prop to a Client Component.

```tsx
// app/page.tsx (Server Component)
import Modal from "./modal"; // Client Component
import Cart from "./cart"; // Server Component

export default function Page() {
  return (
    <Modal>
      <Cart />
    </Modal>
  );
}
```

## 140: What is the difference between static and dynamic rendering?

- **Static rendering**: the page is rendered at build time (or after revalidation) and the same HTML is sent to all users.
- **Dynamic rendering**: the page is rendered on every request, because it depends on request data like cookies, headers or search params.

Next.js picks the mode for each route based on the APIs you use.

## 141: What is incremental static regeneration (ISR)?

ISR lets you update static pages after the build without rebuilding the whole site. You set a time, and after that time the next visitor triggers a background update. Users keep seeing the old page until the new one is ready.

```tsx
// app/blog/page.tsx
export const revalidate = 3600; // regenerate at most once per hour

export default async function Page() {
  const posts = await fetch("https://api.example.com/posts").then((r) =>
    r.json(),
  );
  return <PostList posts={posts} />;
}
```

## 142: What does `revalidate` mean?

It is the number of seconds that cached data or a page is considered fresh. After that, the next request still gets the cached version, but Next.js regenerates it in the background. This is the "stale-while-revalidate" pattern.

## 143: What is `generateStaticParams`?

It tells Next.js which values of a dynamic route to prerender at build time.

```tsx
// app/blog/[slug]/page.tsx
export async function generateStaticParams() {
  const posts = await getPosts();
  return posts.map((post) => ({ slug: post.slug }));
}

export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const post = await getPost(slug);
  return <h1>{post.title}</h1>;
}
```

It is the App Router version of `getStaticPaths`.

## 144: How do you read a file from the file system in a page?

Server Components run on the server, so you can use Node.js APIs like `fs`.

```tsx
import { readFile } from "node:fs/promises";
import path from "node:path";

export default async function Page() {
  const text = await readFile(
    path.join(process.cwd(), "content/about.md"),
    "utf8",
  );
  return <pre>{text}</pre>;
}
```

## 145: Does Next.js support MDX?

Yes, with the `@next/mdx` package. You can write pages as `.mdx` files and use React components inside Markdown.

```ts
// next.config.ts
import createMDX from "@next/mdx";

const withMDX = createMDX({});

export default withMDX({
  pageExtensions: ["ts", "tsx", "md", "mdx"],
});
```

You also need an `mdx-components.tsx` file in the root of the project.

## 146: What is `getStaticProps`?

It is a Pages Router function that fetches data at build time and passes it to the page as props.

```tsx
// pages/blog.tsx
export async function getStaticProps() {
  const posts = await getPosts();
  return { props: { posts }, revalidate: 60 };
}

export default function Blog({ posts }: { posts: Post[] }) {
  return <PostList posts={posts} />;
}
```

It doesn't exist in the App Router. There you fetch directly in Server Components.

## 147: What is `getServerSideProps`?

It is a Pages Router function that runs on every request and passes data to the page as props.

```tsx
// pages/profile.tsx
import type { GetServerSideProps } from "next";

export const getServerSideProps: GetServerSideProps = async (context) => {
  const user = await getUser(context.req);
  if (!user) {
    return { redirect: { destination: "/login", permanent: false } };
  }
  return { props: { user } };
};
```

## 148: What is `getStaticPaths`?

It is a Pages Router function used with dynamic routes and `getStaticProps`. It returns the list of paths to prerender.

```tsx
// pages/blog/[slug].tsx
export async function getStaticPaths() {
  const posts = await getPosts();
  return {
    paths: posts.map((p) => ({ params: { slug: p.slug } })),
    fallback: "blocking",
  };
}
```

## 149: What are `_app.tsx` and `_document.tsx` in the Pages Router?

- `pages/_app.tsx` wraps every page. You use it for global CSS, shared layouts and providers.
- `pages/_document.tsx` lets you change the `<html>` and `<body>` tags. It only renders on the server.

In the App Router, the root `layout.tsx` replaces both.

## 150: How do you add a custom 404 page in the Pages Router?

Create `pages/404.tsx`. It is prerendered at build time.

```tsx
// pages/404.tsx
export default function Custom404() {
  return <h1>404 - Page not found</h1>;
}
```

In the App Router, use `app/not-found.tsx`.

# Moderate Questions (151-300)

## 151: How does Next.js decide if a route is static or dynamic?

During `next build`, Next.js tries to render each route. If the render uses request-time APIs, the route becomes dynamic. These include:

- `cookies()`, `headers()`, `draftMode()`
- `searchParams` in a page
- `connection()`
- `fetch` with `cache: 'no-store'` or other uncached data (when Cache Components is off)
- Route segment config like `export const dynamic = 'force-dynamic'`

If none of these are used, the route is prerendered as static. When Cache Components is turned on, it works at the component level instead of the route level: the static parts go into a prerendered shell and the dynamic parts must be wrapped in `<Suspense>`.

## 152: What are the route segment config options?

These are exports from a `page`, `layout` or `route` file that change how the segment behaves:

```tsx
export const dynamic = "auto"; // 'auto' | 'force-dynamic' | 'error' | 'force-static'
export const dynamicParams = true;
export const revalidate = false; // false | 0 | number
export const fetchCache = "auto";
export const runtime = "nodejs"; // 'nodejs' | 'edge'
export const preferredRegion = "auto";
export const maxDuration = 30;
```

Note: when `cacheComponents` is enabled, `dynamic`, `revalidate` and `fetchCache` are not supported. You use `"use cache"` and `cacheLife` instead.

## 153: What does `export const dynamic = 'force-dynamic'` do?

It makes the route render on every request, even if it doesn't use any request-time API. It is the same as making every `fetch` uncached. You might use it for a page that reads data from a source Next.js can't track, like a database client, and must always be fresh.

## 154: What does `dynamicParams` do?

It controls what happens when a user visits a dynamic route value that was not returned by `generateStaticParams`.

- `true` (default): the page is rendered on demand and then cached.
- `false`: the page returns 404.

```tsx
// app/blog/[slug]/page.tsx
export const dynamicParams = false;

export async function generateStaticParams() {
  return [{ slug: "first" }, { slug: "second" }];
}
// /blog/third -> 404
```

## 155: What are the caching layers in Next.js?

Without Cache Components, there are four main mechanisms:

1. **Request memoization**: the same `fetch` call in one render pass runs only once.
2. **Data Cache**: results of `fetch` with caching options are stored across requests and deployments.
3. **Full Route Cache**: HTML and the RSC payload of static routes are stored on the server.
4. **Router Cache**: the client keeps the RSC payload of visited and prefetched routes in memory.

With Cache Components enabled, you control caching explicitly with `"use cache"`, `cacheLife` and `cacheTag`, and the Router Cache still works on the client.

## 156: What is request memoization?

When you call `fetch` with the same URL and options more than once during one render, Next.js runs the request only once and reuses the result. This means you can fetch the same data in a layout and a page without passing it down as props.

```tsx
async function getUser() {
  const res = await fetch("https://api.example.com/user");
  return res.json();
}

// layout.tsx and page.tsx can both call getUser(); only one request is made
```

It only works for `GET` requests in the React component tree, and only lasts for that one request.

## 157: How do you dedupe calls that don't use `fetch`?

Wrap the function with React's `cache`.

```ts
import { cache } from "react";
import { db } from "@/lib/db";

export const getUser = cache(async (id: string) => {
  return db.user.findUnique({ where: { id } });
});
```

Now `getUser('1')` runs the query only once per request, no matter how many components call it.

## 158: What is the difference between React `cache` and `"use cache"`?

- React `cache` dedupes calls during a single request. The result is thrown away after the request.
- `"use cache"` stores the result across requests (and across users), until it expires or is revalidated.

You often use both: `cache` for per-request deduping of things like the current user, and `"use cache"` for shared data like a product list.

## 159: What is the Router Cache?

It is an in-memory cache in the browser. It stores the RSC payload of routes the user has visited or that were prefetched. When the user goes back or clicks a prefetched link, the route shows instantly.

It is cleared on a full page reload. You can clear it for the current route with `router.refresh()`, or from a Server Action with `revalidatePath`, `revalidateTag`, `updateTag` or `refresh`.

## 160: What does `router.refresh()` do?

It asks the server to render the current route again and updates the page with the new result. Client state like `useState` and input values is kept. It doesn't cause a full browser reload.

```tsx
"use client";

import { useRouter } from "next/navigation";

export function RefreshButton() {
  const router = useRouter();
  return <button onClick={() => router.refresh()}>Refresh</button>;
}
```

## 161: What is `revalidatePath`?

It marks cached data for a path as stale, so the next visit renders it again with fresh data.

```ts
import { revalidatePath } from "next/cache";

revalidatePath("/blog"); // one page
revalidatePath("/blog/[slug]", "page"); // all pages matching a dynamic route
revalidatePath("/dashboard", "layout"); // the layout and everything under it
revalidatePath("/", "layout"); // everything
```

You can call it in Server Actions and Route Handlers.

## 162: What is `revalidateTag`?

It marks all cached data with a certain tag as stale. You first tag the data:

```ts
await fetch("https://api.example.com/posts", {
  next: { tags: ["posts"] },
});
```

Then you revalidate by tag:

```ts
import { revalidateTag } from "next/cache";

revalidateTag("posts", "max");
```

In Next.js 16, the second argument is a `cacheLife` profile (like `'max'`, `'hours'`, or `{ expire: 3600 }`). It enables stale-while-revalidate: users get the old data while fresh data loads in the background. The single-argument form is deprecated.

## 163: What is `updateTag` and how is it different from `revalidateTag`?

`updateTag` is new in Next.js 16 and can only be called in Server Actions. It expires the tag right away, and the same request waits for fresh data. So the user who made the change sees it immediately ("read your own writes").

```ts
"use server";

import { updateTag } from "next/cache";

export async function updateProfile(userId: string, formData: FormData) {
  await db.user.update({
    where: { id: userId },
    data: { name: formData.get("name") as string },
  });
  updateTag(`user-${userId}`);
}
```

- `updateTag`: use after the current user changes something and must see it now.
- `revalidateTag`: use when it's fine to show slightly old data for a moment, like after a CMS webhook.

## 164: What does `refresh()` from `next/cache` do?

It is a Next.js 16 function you call in a Server Action to refresh the client router, so the page shows new uncached data. It doesn't touch any cached data or tags.

```ts
"use server";

import { refresh } from "next/cache";

export async function markAsRead(id: string) {
  await db.notification.update({ where: { id }, data: { read: true } });
  refresh();
}
```

Use it when the page shows dynamic data (for example a notification count) that isn't cached, so there is nothing to revalidate.

## 165: How do you use `useActionState` with a form?

`useActionState` from React tracks the result of a Server Action, and gives you a pending flag.

```ts
// app/actions.ts
"use server";

export async function subscribe(
  prevState: { message: string },
  formData: FormData,
) {
  const email = formData.get("email") as string;
  if (!email.includes("@")) {
    return { message: "Please enter a valid email" };
  }
  await saveEmail(email);
  return { message: "Thanks for subscribing!" };
}
```

```tsx
// app/subscribe-form.tsx
"use client";

import { useActionState } from "react";
import { subscribe } from "./actions";

export function SubscribeForm() {
  const [state, formAction, isPending] = useActionState(subscribe, {
    message: "",
  });

  return (
    <form action={formAction}>
      <input name="email" type="email" />
      <button disabled={isPending}>
        {isPending ? "Saving..." : "Subscribe"}
      </button>
      <p>{state.message}</p>
    </form>
  );
}
```

When used with `useActionState`, the action receives the previous state as the first argument and `FormData` as the second.

## 166: What is `useFormStatus`?

A React hook from `react-dom` that tells a component if the parent form is submitting. It must be used in a component rendered inside the `<form>`.

```tsx
"use client";

import { useFormStatus } from "react-dom";

export function SubmitButton() {
  const { pending } = useFormStatus();
  return (
    <button type="submit" disabled={pending}>
      {pending ? "Sending..." : "Send"}
    </button>
  );
}
```

## 167: What is `useOptimistic`?

A React hook that lets you show the result of an action right away, before the server responds. If the action fails, the UI goes back to the real state.

```tsx
"use client";

import { useOptimistic } from "react";
import { addMessage } from "./actions";

export function Chat({ messages }: { messages: string[] }) {
  const [optimisticMessages, addOptimistic] = useOptimistic(
    messages,
    (state, newMessage: string) => [...state, newMessage],
  );

  async function formAction(formData: FormData) {
    const text = formData.get("text") as string;
    addOptimistic(text);
    await addMessage(text);
  }

  return (
    <>
      <ul>
        {optimisticMessages.map((m, i) => (
          <li key={i}>{m}</li>
        ))}
      </ul>
      <form action={formAction}>
        <input name="text" />
        <button>Send</button>
      </form>
    </>
  );
}
```

## 168: How do you pass extra arguments to a Server Action?

Use `bind`.

```tsx
"use client";

import { updateUser } from "./actions";

export function UserForm({ userId }: { userId: string }) {
  const updateUserWithId = updateUser.bind(null, userId);

  return (
    <form action={updateUserWithId}>
      <input name="name" />
      <button>Save</button>
    </form>
  );
}
```

```ts
"use server";

export async function updateUser(userId: string, formData: FormData) {
  // ...
}
```

You can also use a hidden input, but then the value appears in the HTML as plain text. Bound arguments are serialized too, so don't treat either way as secret.

## 169: Can you call a Server Action without a form?

Yes. You can call it from an event handler or `useEffect` like a normal async function. Wrap it in `startTransition` if you want React to track the pending state.

```tsx
"use client";

import { useTransition } from "react";
import { likePost } from "./actions";

export function LikeButton({ postId }: { postId: string }) {
  const [isPending, startTransition] = useTransition();

  return (
    <button
      disabled={isPending}
      onClick={() => startTransition(() => likePost(postId))}
    >
      Like
    </button>
  );
}
```

## 170: What is progressive enhancement in Server Actions?

When you pass a Server Action to a `<form action>` in a Server Component, the form works even before JavaScript loads, or if JavaScript is turned off. The browser submits it as a normal form POST. When JavaScript is loaded, Next.js submits it without a page reload.

In Client Components, forms queue the submission until hydration is done.

## 171: How do you validate form data in a Server Action?

Treat the data as untrusted and validate it on the server, for example with Zod.

```ts
"use server";

import { z } from "zod";

const schema = z.object({
  email: z.string().email(),
  name: z.string().min(2),
});

export async function signup(prevState: unknown, formData: FormData) {
  const result = schema.safeParse({
    email: formData.get("email"),
    name: formData.get("name"),
  });

  if (!result.success) {
    return { errors: result.error.flatten().fieldErrors };
  }

  await createUser(result.data);
  return { errors: {} };
}
```

Client-side validation is good for user experience, but it can be skipped, so always validate on the server.

## 172: How do you redirect after a Server Action?

Call `redirect()` after the work is done. Call it outside `try/catch`, because it works by throwing a special error.

```ts
"use server";

import { redirect } from "next/navigation";
import { revalidatePath } from "next/cache";

export async function createPost(formData: FormData) {
  const post = await db.post.create({
    data: { title: formData.get("title") as string },
  });
  revalidatePath("/posts");
  redirect(`/posts/${post.id}`);
}
```

## 173: Are Server Actions secure by default?

Partly. Next.js adds some protections:

- Actions can only be called with POST.
- The `Origin` header is compared with the `Host` header to block CSRF from other sites.
- Action IDs are not guessable and change between builds, and unused actions are removed from the build.
- Values captured in closures of inline actions are encrypted.

But every Server Action is still a public HTTP endpoint. Anyone can call it with any input. So you must check authentication and authorization inside every action, and validate the input.

```ts
"use server";

export async function deletePost(id: string) {
  const session = await auth();
  if (!session) throw new Error("Unauthorized");

  const post = await db.post.findUnique({ where: { id } });
  if (post?.authorId !== session.user.id) throw new Error("Forbidden");

  await db.post.delete({ where: { id } });
}
```

## 174: What is the default body size limit for Server Actions and how do you change it?

The default is 1 MB. You can change it in `next.config.ts`:

```ts
const nextConfig = {
  experimental: {
    serverActions: {
      bodySizeLimit: "5mb",
    },
  },
};
```

## 175: How do you handle errors in Server Actions?

For expected errors (like validation errors), return them as data and show them with `useActionState`. Don't throw.

For unexpected errors, you can let them throw. The nearest `error.tsx` boundary will catch them. In production, the error message is hidden from the client and only a `digest` is sent.

```ts
"use server";

export async function createTodo(
  prevState: { error?: string },
  formData: FormData,
) {
  try {
    await db.todo.create({ data: { title: formData.get("title") as string } });
    return {};
  } catch {
    return { error: "Could not save the todo. Please try again." };
  }
}
```

## 176: What is streaming?

Streaming means sending the HTML to the browser in pieces as they are ready, instead of waiting for the whole page. The user sees the layout and fast parts first, and the slow parts show up when their data arrives.

In Next.js you stream with `loading.tsx` or with `<Suspense>`.

## 177: How do you stream part of a page with Suspense?

Wrap the slow component in `<Suspense>` with a fallback.

```tsx
import { Suspense } from "react";

export default function Page() {
  return (
    <div>
      <h1>Dashboard</h1>
      <Suspense fallback={<p>Loading revenue...</p>}>
        <Revenue />
      </Suspense>
      <Suspense fallback={<p>Loading orders...</p>}>
        <LatestOrders />
      </Suspense>
    </div>
  );
}

async function Revenue() {
  const data = await getRevenue(); // slow
  return <p>{data.total}</p>;
}
```

The heading shows immediately, and each section shows when its data is ready.

## 178: What is the difference between `loading.tsx` and `<Suspense>`?

`loading.tsx` wraps the whole page of a segment in a Suspense boundary. `<Suspense>` lets you choose exactly which components show a fallback, so you can stream smaller parts. `loading.tsx` also helps navigation feel instant, because the fallback can be prefetched and shown right after a click.

## 179: What is a data waterfall and how do you avoid it?

A waterfall is when requests run one after another, even though they don't depend on each other.

```tsx
// slow: second request waits for the first one
const artist = await getArtist(id);
const albums = await getAlbums(id);
```

Run them in parallel with `Promise.all`:

```tsx
const [artist, albums] = await Promise.all([getArtist(id), getAlbums(id)]);
```

Or split them into separate components with their own `<Suspense>` boundaries so each streams on its own.

## 180: How do you pass data from a Server Component to a Client Component without waiting for it?

Pass the Promise as a prop and read it in the Client Component with `use()`.

```tsx
// app/page.tsx
import { Suspense } from "react";
import { Comments } from "./comments";

export default function Page() {
  const commentsPromise = getComments(); // not awaited

  return (
    <Suspense fallback={<p>Loading comments...</p>}>
      <Comments commentsPromise={commentsPromise} />
    </Suspense>
  );
}
```

```tsx
// app/comments.tsx
"use client";

import { use } from "react";

export function Comments({
  commentsPromise,
}: {
  commentsPromise: Promise<string[]>;
}) {
  const comments = use(commentsPromise);
  return (
    <ul>
      {comments.map((c, i) => (
        <li key={i}>{c}</li>
      ))}
    </ul>
  );
}
```

The page starts streaming right away, and the comments show when the Promise resolves.

## 181: What are parallel routes?

Parallel routes let you render more than one page in the same layout at the same time. You create them with named slots: folders that start with `@`.

```
app/
  dashboard/
    layout.tsx
    page.tsx
    @analytics/
      page.tsx
    @team/
      page.tsx
```

```tsx
// app/dashboard/layout.tsx
export default function Layout({
  children,
  analytics,
  team,
}: {
  children: React.ReactNode;
  analytics: React.ReactNode;
  team: React.ReactNode;
}) {
  return (
    <>
      {children}
      <div className="grid grid-cols-2">
        {analytics}
        {team}
      </div>
    </>
  );
}
```

Slots don't change the URL. Each slot can have its own loading and error states.

## 182: What is `default.tsx` in parallel routes?

When the user does a full page load on a URL, Next.js may not know what to render for a slot that doesn't match the current URL. `default.tsx` is the fallback for that case.

```tsx
// app/dashboard/@team/default.tsx
export default function Default() {
  return null;
}
```

In Next.js 16, every parallel route slot must have a `default.tsx`, or the build fails. Return `null` or call `notFound()` if you want the old behavior.

## 183: What are intercepting routes?

Intercepting routes let you show a route from another part of the app inside the current layout. A common example is clicking a photo in a feed: the photo opens in a modal and the URL changes to `/photo/123`. If the user refreshes or shares the link, they get the full photo page.

You create them with special folder prefixes:

- `(.)` matches segments on the same level
- `(..)` matches segments one level above
- `(..)(..)` matches segments two levels above
- `(...)` matches segments from the root `app` folder

These are based on route segments, not the file system, so `@slot` folders don't count.

## 184: How do you build a modal with parallel and intercepting routes?

```
app/
  layout.tsx
  @modal/
    default.tsx
    (.)photo/[id]/page.tsx    // modal version
  photo/[id]/page.tsx         // full page version
  page.tsx                    // feed
```

```tsx
// app/layout.tsx
export default function RootLayout({
  children,
  modal,
}: {
  children: React.ReactNode;
  modal: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        {children}
        {modal}
      </body>
    </html>
  );
}
```

```tsx
// app/@modal/default.tsx
export default function Default() {
  return null;
}
```

```tsx
// app/@modal/(.)photo/[id]/page.tsx
import { Modal } from "@/components/modal";

export default async function PhotoModal({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  return (
    <Modal>
      <img src={`/photos/${id}.jpg`} alt="" />
    </Modal>
  );
}
```

The modal can close with `router.back()`.

## 185: What are `useSelectedLayoutSegment` and `useSelectedLayoutSegments`?

Client hooks that return the active route segment(s) below the layout where they are used. They are handy for active states in tabs and breadcrumbs.

```tsx
"use client";

import { useSelectedLayoutSegment } from "next/navigation";

export function Tabs() {
  const segment = useSelectedLayoutSegment(); // e.g. "settings" on /dashboard/settings
  return <p>Active tab: {segment ?? "overview"}</p>;
}
```

You can pass a slot name to get the active segment of a parallel route: `useSelectedLayoutSegment('analytics')`.

## 186: Why does `useSearchParams` need a Suspense boundary?

On a statically rendered route, search params are not known at build time. If a Client Component uses `useSearchParams`, everything up to the nearest `<Suspense>` boundary can only render in the browser. Without a boundary, the whole page would render on the client, so Next.js fails the build with a "Missing Suspense boundary with useSearchParams" error.

```tsx
import { Suspense } from "react";
import { SearchFilters } from "./search-filters"; // uses useSearchParams

export default function Page() {
  return (
    <Suspense fallback={<p>Loading filters...</p>}>
      <SearchFilters />
    </Suspense>
  );
}
```

## 187: How do you update a search param without losing the others?

Copy the current params, change one, and push the new URL.

```tsx
"use client";

import { usePathname, useRouter, useSearchParams } from "next/navigation";

export function SortSelect() {
  const router = useRouter();
  const pathname = usePathname();
  const searchParams = useSearchParams();

  function onChange(value: string) {
    const params = new URLSearchParams(searchParams.toString());
    params.set("sort", value);
    router.replace(`${pathname}?${params.toString()}`);
  }

  return (
    <select
      onChange={(e) => onChange(e.target.value)}
      defaultValue={searchParams.get("sort") ?? ""}
    >
      <option value="new">Newest</option>
      <option value="price">Price</option>
    </select>
  );
}
```

## 188: How do you build a search page where results update as the user types?

Keep the query in the URL. A Client Component updates the URL (with a small debounce), and the Server Component page reads `searchParams` and fetches results.

```tsx
// app/search/page.tsx
import { Suspense } from "react";

export default async function Page({
  searchParams,
}: {
  searchParams: Promise<{ q?: string }>;
}) {
  const { q = "" } = await searchParams;

  return (
    <>
      <SearchInput />
      <Suspense key={q} fallback={<p>Searching...</p>}>
        <Results query={q} />
      </Suspense>
    </>
  );
}
```

Giving the `Suspense` a `key` makes it show the fallback again each time the query changes. Storing state in the URL also makes the page shareable.

## 189: How do you use `generateMetadata`?

Use it when the metadata depends on data, like a blog post title.

```tsx
import type { Metadata } from "next";

type Props = { params: Promise<{ slug: string }> };

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { slug } = await params;
  const post = await getPost(slug);

  return {
    title: post.title,
    description: post.excerpt,
    openGraph: { images: [post.coverImage] },
  };
}

export default async function Page({ params }: Props) {
  const { slug } = await params;
  const post = await getPost(slug);
  return <h1>{post.title}</h1>;
}
```

If `getPost` uses `fetch`, the request is memoized, so it runs only once for both functions. For other data sources, wrap it in React `cache`.

## 190: What is `metadataBase`?

It sets the base URL for metadata fields that need a full URL, like Open Graph images. Then you can use relative paths.

```tsx
// app/layout.tsx
export const metadata: Metadata = {
  metadataBase: new URL("https://example.com"),
  openGraph: {
    images: "/og.png", // becomes https://example.com/og.png
  },
};
```

## 191: How do you generate an Open Graph image with code?

Create `opengraph-image.tsx` and return an `ImageResponse` from `next/og`.

```tsx
// app/blog/[slug]/opengraph-image.tsx
import { ImageResponse } from "next/og";

export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

export default async function Image({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const post = await getPost(slug);

  return new ImageResponse(
    <div
      style={{
        fontSize: 64,
        background: "white",
        width: "100%",
        height: "100%",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      {post.title}
    </div>,
    size,
  );
}
```

`ImageResponse` supports flexbox and a subset of CSS. Grid layouts are not supported.

## 192: How is metadata merged between layouts and pages?

Metadata is evaluated from the root layout down to the page. Child segments override fields with the same name. Objects like `openGraph` are replaced, not deeply merged. So if a page sets `openGraph.title`, any `openGraph.images` set in the layout is lost unless you set it again or share it through a variable.

```ts
// app/shared-metadata.ts
export const openGraphImage = { images: ["/og.png"] };
```

```ts
// app/about/page.tsx
export const metadata = {
  openGraph: { ...openGraphImage, title: "About" },
};
```

## 193: How does Next.js stream metadata?

Since Next.js 15.2, `generateMetadata` doesn't block the page. The page UI can stream right away and the metadata tags are added when they are ready. For bots that can't run JavaScript (like some social media crawlers), Next.js waits for metadata and puts it in the `<head>`. You can change the list of such bots with the `htmlLimitedBots` option in `next.config.ts`.

## 194: How do you create an API endpoint with a dynamic segment in a Route Handler?

The second argument has `params`, which is a Promise.

```ts
// app/api/users/[id]/route.ts
export async function GET(
  request: Request,
  { params }: { params: Promise<{ id: string }> },
) {
  const { id } = await params;
  const user = await db.user.findUnique({ where: { id } });

  if (!user) {
    return Response.json({ error: "Not found" }, { status: 404 });
  }
  return Response.json(user);
}
```

You can also use the generated `RouteContext<'/api/users/[id]'>` type for the second argument.

## 195: How do you read query params in a Route Handler?

Use `request.nextUrl.searchParams` with `NextRequest`, or `new URL(request.url)` with a normal `Request`.

```ts
// app/api/search/route.ts
import type { NextRequest } from "next/server";

export async function GET(request: NextRequest) {
  const q = request.nextUrl.searchParams.get("q");
  const results = await search(q ?? "");
  return Response.json(results);
}
```

## 196: Are `GET` Route Handlers cached?

Not by default since Next.js 15. To make a `GET` handler static, use `export const dynamic = 'force-static'` (or `"use cache"` in a helper function when Cache Components is on).

```ts
// app/api/config/route.ts
export const dynamic = "force-static";

export async function GET() {
  return Response.json({ version: "1.0.0" });
}
```

Other methods like `POST` are never cached.

## 197: What is `NextResponse`?

It extends the Web `Response` with helpers for Next.js:

```ts
import { NextResponse } from "next/server";

NextResponse.json({ ok: true }, { status: 200 });
NextResponse.redirect(new URL("/login", request.url));
NextResponse.rewrite(new URL("/new-path", request.url));
NextResponse.next(); // used in proxy to continue
```

It also has a `cookies` API for setting cookies on the response.

## 198: What is `NextRequest`?

It extends the Web `Request` with extra properties:

- `request.nextUrl` a URL object with `pathname`, `searchParams`, `basePath` and more
- `request.cookies` to read, set and delete cookies

In Next.js 15 the `geo` and `ip` properties were removed. Your hosting provider usually gives you this data through headers.

## 199: How do you set cookies in a Route Handler?

Use `cookies()` from `next/headers`, or set them on the response.

```ts
import { cookies } from "next/headers";

export async function POST() {
  const cookieStore = await cookies();
  cookieStore.set("token", "abc123", {
    httpOnly: true,
    secure: true,
    sameSite: "lax",
    path: "/",
    maxAge: 60 * 60 * 24 * 7,
  });
  return Response.json({ ok: true });
}
```

## 200: How do you handle CORS in a Route Handler?

Set the CORS headers on the response and handle the `OPTIONS` preflight request.

```ts
// app/api/data/route.ts
const corsHeaders = {
  "Access-Control-Allow-Origin": "https://app.example.com",
  "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, Authorization",
};

export async function OPTIONS() {
  return new Response(null, { status: 204, headers: corsHeaders });
}

export async function GET() {
  return Response.json({ data: "ok" }, { headers: corsHeaders });
}
```

For many routes, you can set CORS headers in `proxy.ts` or in the `headers` option of `next.config.ts`.

## 201: How do you stream a response from a Route Handler?

Return a `Response` with a `ReadableStream`. This is common for AI chat responses.

```ts
// app/api/stream/route.ts
export async function GET() {
  const encoder = new TextEncoder();

  const stream = new ReadableStream({
    async start(controller) {
      for (const word of ["Hello", " ", "world"]) {
        controller.enqueue(encoder.encode(word));
        await new Promise((r) => setTimeout(r, 300));
      }
      controller.close();
    },
  });

  return new Response(stream, {
    headers: { "Content-Type": "text/plain; charset=utf-8" },
  });
}
```

## 202: When should you use a Route Handler instead of a Server Action?

Use a **Server Action** for mutations called from your own UI: forms, buttons, and so on.

Use a **Route Handler** when:

- An external service calls you (webhooks, OAuth callbacks)
- You need a public API for a mobile app or other clients
- You need to return something other than UI data, like a file, an RSS feed or a stream
- You need `GET` requests that can be cached

Don't call your own Route Handlers from Server Components. Call the data function directly instead, because a fetch to your own API adds an extra network trip.

## 203: How do you handle a webhook in Next.js?

Create a Route Handler, check the signature, and then do the work.

```ts
// app/api/webhooks/cms/route.ts
import { revalidateTag } from "next/cache";

export async function POST(request: Request) {
  const secret = request.headers.get("x-webhook-secret");
  if (secret !== process.env.CMS_WEBHOOK_SECRET) {
    return new Response("Invalid secret", { status: 401 });
  }

  const body = await request.json();
  revalidateTag(`post-${body.id}`, "max");

  return Response.json({ revalidated: true });
}
```

For services like Stripe, read the raw body with `await request.text()` and verify the signature with their SDK.

## 204: What can you do in `proxy.ts`?

- Redirect users (for example, to a login page or a localized URL)
- Rewrite to another path (for example, A/B testing or multi-tenant apps)
- Read and set cookies
- Set request and response headers
- Return a response directly (for example, a 403 or a JSON error)

Keep it fast. It runs before every matched request, so slow database calls there slow down your whole site.

## 205: What runtime does Proxy use?

In Next.js 16, `proxy.ts` runs on the Node.js runtime, and the edge runtime is not supported for proxy. This means you can use Node.js APIs and normal npm packages. If you need the edge runtime, you can still use the deprecated `middleware.ts` for now.

## 206: How do you set a request header in Proxy so your pages can read it?

Pass new headers to `NextResponse.next`.

```ts
// proxy.ts
import { NextResponse, type NextRequest } from "next/server";

export function proxy(request: NextRequest) {
  const requestHeaders = new Headers(request.headers);
  requestHeaders.set("x-pathname", request.nextUrl.pathname);

  return NextResponse.next({
    request: { headers: requestHeaders },
  });
}
```

Then a Server Component can read it with `(await headers()).get('x-pathname')`.

## 207: How do you use advanced matching in the Proxy `matcher`?

Each matcher can be an object with `source`, `has` and `missing` conditions.

```ts
export const config = {
  matcher: [
    {
      source: "/((?!api|_next/static|_next/image|favicon.ico).*)",
      missing: [
        { type: "header", key: "next-router-prefetch" },
        { type: "header", key: "purpose", value: "prefetch" },
      ],
    },
  ],
};
```

This example skips prefetch requests. Matcher values must be constants, because they are read at build time.

## 208: Should you do authentication only in Proxy?

No. Proxy is good for quick, optimistic checks, like redirecting a user without a session cookie. But you shouldn't rely on it alone. Always check the session again close to the data: in your data access layer, in Server Actions and in Route Handlers. This way a bug in the matcher or a bypass of the proxy doesn't expose data.

## 209: How do you protect a page so only logged-in users can see it?

A common approach has layers:

1. In `proxy.ts`, redirect users who have no session cookie.
2. In the page (or a data function it calls), verify the session and redirect if it is invalid.
3. In every Server Action and data function, check the user again.

```ts
// lib/dal.ts
import "server-only";
import { cache } from "react";
import { cookies } from "next/headers";
import { redirect } from "next/navigation";

export const verifySession = cache(async () => {
  const token = (await cookies()).get("session")?.value;
  const session = await decrypt(token);
  if (!session?.userId) {
    redirect("/login");
  }
  return { userId: session.userId };
});
```

```tsx
// app/dashboard/page.tsx
export default async function Dashboard() {
  const { userId } = await verifySession();
  const data = await getDashboardData(userId);
  return <DashboardView data={data} />;
}
```

## 210: Why shouldn't you do auth checks only in a layout?

Layouts don't re-render when you navigate between pages that share them. So a check in the layout may not run on every navigation. Also, a page and its layout render in parallel, so the page could start fetching data before the layout check is done. Put checks in the page or, better, in the data access functions themselves.

## 211: What libraries are commonly used for authentication in Next.js?

- **Auth.js** (formerly NextAuth.js)
- **Better Auth**
- **Clerk**
- **Supabase Auth**
- **Kinde**, **WorkOS**, **Auth0** and others

You can also build your own with sessions stored in encrypted cookies (for example using `jose`) or in a database.

## 212: What is the `server-only` package?

It makes sure a module is never imported into client code. If a Client Component imports it, the build fails.

```ts
// lib/data.ts
import "server-only";

export async function getSecretData() {
  return fetch("https://api.example.com/data", {
    headers: { Authorization: `Bearer ${process.env.API_KEY}` },
  });
}
```

There is also a `client-only` package that does the opposite.

## 213: What happens if a Server Component reads a non-public env variable that is used in a Client Component?

In a Client Component, `process.env.SECRET_KEY` (without `NEXT_PUBLIC_`) becomes an empty value (`undefined`) in the browser bundle. Next.js doesn't leak it. But it is still a bug, because the code won't work as expected. Use `server-only` to catch these mistakes at build time.

## 214: When are environment variables read: at build time or at runtime?

- `NEXT_PUBLIC_` variables are inlined into the JavaScript bundle at build time. If you change them later, you must rebuild.
- Server-side variables are read at runtime on the server when the code runs during a dynamic render. But if a page is prerendered at build time, the values used during the build are baked into the HTML.

If you build a Docker image once and deploy it to many environments, read config at request time (for example after `await connection()`) or pass it from the server to the client as props.

## 215: How do you use `generateStaticParams` with multiple dynamic segments?

Return objects with all the params.

```tsx
// app/products/[category]/[id]/page.tsx
export async function generateStaticParams() {
  const products = await getProducts();
  return products.map((p) => ({ category: p.category, id: p.id }));
}
```

Or generate params from the top down: a child `generateStaticParams` receives the parent's `params`.

```tsx
// app/products/[category]/[id]/page.tsx
export async function generateStaticParams({
  params: { category },
}: {
  params: { category: string };
}) {
  const products = await getProductsByCategory(category);
  return products.map((p) => ({ id: p.id }));
}
```

## 216: How do you prerender only some pages and render the rest on demand?

Return only the most popular items from `generateStaticParams`. The rest are rendered on the first request and cached (as long as `dynamicParams` is not `false`).

```tsx
export async function generateStaticParams() {
  const topPosts = await getTopPosts(100);
  return topPosts.map((p) => ({ slug: p.slug }));
}
```

This keeps build times short for large sites.

## 217: How do you implement internationalization (i18n) in the App Router?

The App Router has no built-in i18n config. The usual approach:

1. Put all routes under a `[lang]` segment: `app/[lang]/page.tsx`.
2. In `proxy.ts`, detect the user's language (from cookies or the `Accept-Language` header) and redirect to `/en/...` or `/de/...`.
3. Load translations in Server Components based on `lang`.

```tsx
// app/[lang]/page.tsx
import { getDictionary } from "./dictionaries";

export async function generateStaticParams() {
  return [{ lang: "en" }, { lang: "de" }];
}

export default async function Page({
  params,
}: {
  params: Promise<{ lang: "en" | "de" }>;
}) {
  const { lang } = await params;
  const dict = await getDictionary(lang);
  return <h1>{dict.welcome}</h1>;
}
```

Libraries like `next-intl` make this easier.

## 218: How was i18n handled in the Pages Router?

The Pages Router has a built-in `i18n` option in `next.config.js`:

```js
module.exports = {
  i18n: {
    locales: ["en", "fr", "de"],
    defaultLocale: "en",
  },
};
```

It handles locale prefixes and detection. This option doesn't work with the App Router.

## 219: What is `next/image` `sizes` and why does it matter?

`sizes` tells the browser how wide the image will be at different screen sizes. The browser uses it to pick the right file from the generated `srcset`. Without it, the browser may download an image that is much bigger than needed.

```tsx
<Image
  src="/photo.jpg"
  alt=""
  fill
  sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
/>
```

It is most important with `fill` or with responsive images styled by CSS.

## 220: How do you show a blur placeholder on images?

For static imports, Next.js creates the blur data for you:

```tsx
import Image from "next/image";
import photo from "./photo.jpg";

<Image src={photo} alt="" placeholder="blur" />;
```

For remote images, you must pass a small base64 image in `blurDataURL`:

```tsx
<Image
  src="https://cdn.example.com/photo.jpg"
  alt=""
  width={800}
  height={600}
  placeholder="blur"
  blurDataURL="data:image/png;base64,iVBORw0KGgo..."
/>
```

## 221: What changed in the default image settings in Next.js 16?

- `images.minimumCacheTTL` changed from 60 seconds to 4 hours (14400 seconds), so optimized images are re-fetched less often.
- `images.qualities` defaults to `[75]`, so only quality 75 is allowed unless you add more values.
- `16` was removed from the default `imageSizes`.
- Local images with query strings need `images.localPatterns`.
- Optimizing images from local IP addresses is blocked by default (`dangerouslyAllowLocalIP` turns it back on).
- `images.maximumRedirects` defaults to 3.
- `images.domains` is deprecated in favor of `remotePatterns`.
- `next/legacy/image` is deprecated.

## 222: How do you use a custom image loader?

When you use an image CDN like Cloudinary or Imgix, you can let it do the resizing instead of Next.js.

```ts
// next.config.ts
const nextConfig = {
  images: {
    loader: "custom",
    loaderFile: "./image-loader.ts",
  },
};
```

```ts
// image-loader.ts
export default function loader({
  src,
  width,
  quality,
}: {
  src: string;
  width: number;
  quality?: number;
}) {
  return `https://cdn.example.com/${src}?w=${width}&q=${quality || 75}`;
}
```

## 223: How do you use CSS variables with `next/font`?

Use the `variable` option and add the class to a parent element. This works well with Tailwind.

```tsx
import { Inter, Roboto_Mono } from "next/font/google";

const inter = Inter({ subsets: ["latin"], variable: "--font-inter" });
const mono = Roboto_Mono({ subsets: ["latin"], variable: "--font-mono" });

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={`${inter.variable} ${mono.variable}`}>
      <body>{children}</body>
    </html>
  );
}
```

```css
@theme inline {
  --font-sans: var(--font-inter);
  --font-mono: var(--font-mono);
}
```

## 224: How do you use CSS-in-JS libraries like styled-components in the App Router?

CSS-in-JS libraries that work at runtime need a Client Component and a style registry that collects styles during server rendering and adds them to the HTML with `useServerInsertedHTML`.

```tsx
// lib/registry.tsx
"use client";

import { useState } from "react";
import { useServerInsertedHTML } from "next/navigation";
import { ServerStyleSheet, StyleSheetManager } from "styled-components";

export default function StyledComponentsRegistry({
  children,
}: {
  children: React.ReactNode;
}) {
  const [sheet] = useState(() => new ServerStyleSheet());

  useServerInsertedHTML(() => {
    const styles = sheet.getStyleElement();
    sheet.instance.clearTag();
    return <>{styles}</>;
  });

  if (typeof window !== "undefined") return <>{children}</>;

  return (
    <StyleSheetManager sheet={sheet.instance}>{children}</StyleSheetManager>
  );
}
```

For styled-components you also turn on `compiler: { styledComponents: true }`. Styles from these libraries can't be used inside Server Components. Zero-runtime options like CSS Modules, Tailwind, or vanilla-extract work better with Server Components.

## 225: How do you share state, like a theme, across Client Components in the App Router?

Create a provider as a Client Component and use it in the root layout.

```tsx
// app/theme-provider.tsx
"use client";

import { createContext, useContext, useState } from "react";

const ThemeContext = createContext<{
  theme: string;
  setTheme: (t: string) => void;
} | null>(null);

export function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [theme, setTheme] = useState("light");
  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

export const useTheme = () => useContext(ThemeContext)!;
```

```tsx
// app/layout.tsx
import { ThemeProvider } from "./theme-provider";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <ThemeProvider>{children}</ThemeProvider>
      </body>
    </html>
  );
}
```

Server Components passed as `children` stay Server Components. Context isn't available in Server Components, though.

## 226: How do you use a third-party component that uses hooks but has no `"use client"`?

If a library component uses `useState` or similar but doesn't have `"use client"` in its file, it fails when used in a Server Component. Wrap it in your own Client Component file:

```tsx
// components/carousel.tsx
"use client";

import { Carousel } from "some-carousel-lib";

export default Carousel;
```

Now you can import `@/components/carousel` from Server Components.

## 227: What is the difference between `error.tsx` and `global-error.tsx`?

- `error.tsx` catches errors in its segment and below, but not in the layout of the same segment.
- `global-error.tsx` sits in the `app` folder and catches errors in the root layout. When it shows, it replaces the root layout, so it must render its own `<html>` and `<body>` tags.

```tsx
// app/global-error.tsx
"use client";

export default function GlobalError({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  return (
    <html>
      <body>
        <h2>Something went wrong</h2>
        <button onClick={() => reset()}>Try again</button>
      </body>
    </html>
  );
}
```

## 228: What is the `digest` property on errors?

In production, Next.js doesn't send the real error message from Server Components to the browser, because it could contain secrets. Instead it sends a generic message and a `digest`, which is a hash. You can find the same digest in your server logs to match the error.

## 229: What does `reset()` do in an error boundary?

It tries to render the segment again. If the error was temporary (like a network issue), the page may work on the second try. It re-renders on the client. For errors from Server Components, you often call `router.refresh()` together with `reset()` inside `startTransition`, so the server data is fetched again too.

```tsx
"use client";

import { startTransition } from "react";
import { useRouter } from "next/navigation";

export default function Error({ reset }: { reset: () => void }) {
  const router = useRouter();

  return (
    <button
      onClick={() =>
        startTransition(() => {
          router.refresh();
          reset();
        })
      }
    >
      Try again
    </button>
  );
}
```

## 230: Can you use `try/catch` around `redirect()` or `notFound()`?

You should avoid it. These functions work by throwing special errors that Next.js catches. If your `catch` block catches them, the redirect or 404 doesn't happen.

```ts
// Wrong
try {
  const user = await getUser();
  if (!user) redirect("/login");
} catch (e) {
  console.error(e); // catches the redirect
}
```

Either call `redirect()` after the `try/catch`, or rethrow those errors with `unstable_rethrow`:

```ts
import { unstable_rethrow } from "next/navigation";

try {
  // ...
} catch (err) {
  unstable_rethrow(err);
  console.error(err);
}
```

## 231: What are `forbidden()` and `unauthorized()`?

They are functions (experimental) that throw errors to show a 403 or 401 page. You render the UI in `forbidden.tsx` and `unauthorized.tsx`. They need the `authInterrupts` flag.

```ts
// next.config.ts
const nextConfig = {
  experimental: {
    authInterrupts: true,
  },
};
```

```tsx
// app/admin/page.tsx
import { forbidden } from "next/navigation";

export default async function AdminPage() {
  const session = await verifySession();
  if (session.role !== "admin") {
    forbidden();
  }
  return <h1>Admin</h1>;
}
```

## 232: What is the `after()` function?

`after()` from `next/server` schedules work to run after the response has been sent to the user. It is good for logging, analytics and other side tasks that shouldn't slow down the response.

```tsx
import { after } from "next/server";

export default async function Page() {
  after(() => {
    logPageView("/home");
  });

  return <h1>Home</h1>;
}
```

It works in Server Components, Server Actions, Route Handlers and Proxy.

## 233: What is `connection()`?

`connection()` from `next/server` tells Next.js to wait for a real user request before rendering the rest. It makes the code after it dynamic. Use it when you need fresh values that don't come from a request API, like `Date.now()`, `Math.random()` or `process.env` at runtime.

```tsx
import { connection } from "next/server";

export default async function Page() {
  await connection();
  const now = new Date().toISOString();
  return <p>Rendered at {now}</p>;
}
```

It replaced `unstable_noStore()`.

## 234: How do you enable Cache Components?

Set `cacheComponents: true` in `next.config.ts`.

```ts
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  cacheComponents: true,
};

export default nextConfig;
```

With it on, nothing is cached unless you say so with `"use cache"`, and any dynamic data must be inside a `<Suspense>` boundary. This flag replaced `experimental.dynamicIO` and `experimental.ppr` from earlier versions.

## 235: What is the `"use cache"` directive?

It marks a page, component or function as cacheable. Next.js stores its result and reuses it. The arguments (and any variables captured from outside) are part of the cache key.

```tsx
// a cached function
export async function getProducts(category: string) {
  "use cache";
  return db.product.findMany({ where: { category } });
}
```

```tsx
// a cached component
async function ProductList({ category }: { category: string }) {
  "use cache";
  const products = await db.product.findMany({ where: { category } });
  return (
    <ul>
      {products.map((p) => (
        <li key={p.id}>{p.name}</li>
      ))}
    </ul>
  );
}
```

```tsx
// a cached page
"use cache";

export default async function Page() {
  // ...
}
```

It requires `cacheComponents: true`.

## 236: What is `cacheLife`?

`cacheLife` sets how long a `"use cache"` entry stays valid. You call it inside the cached function.

```ts
import { cacheLife } from "next/cache";

export async function getBlogPosts() {
  "use cache";
  cacheLife("hours");
  return db.post.findMany();
}
```

Built-in profiles are `'default'`, `'seconds'`, `'minutes'`, `'hours'`, `'days'`, `'weeks'` and `'max'`. Each profile has three values:

- `stale`: how long the client can use the data without checking the server
- `revalidate`: after how long the server refreshes the data in the background
- `expire`: after how long with no requests the entry is dropped and the next request has to wait for fresh data

You can also pass an object: `cacheLife({ stale: 60, revalidate: 300, expire: 3600 })`.

## 237: What is `cacheTag`?

`cacheTag` adds a tag to a `"use cache"` entry so you can invalidate it later with `revalidateTag` or `updateTag`.

```ts
import { cacheTag } from "next/cache";

export async function getProduct(id: string) {
  "use cache";
  cacheTag("products", `product-${id}`);
  return db.product.findUnique({ where: { id } });
}
```

```ts
"use server";

import { updateTag } from "next/cache";

export async function updateProduct(id: string, data: ProductInput) {
  await db.product.update({ where: { id }, data });
  updateTag(`product-${id}`);
}
```

## 238: What is Partial Prerendering (PPR)?

PPR lets one route have both static and dynamic parts. At build time, Next.js renders a static shell (everything that doesn't depend on the request) and leaves holes for dynamic parts wrapped in `<Suspense>`. When a user visits, the shell is sent right away from the CDN, and the dynamic parts are streamed in from the server in the same response.

In Next.js 16, PPR is what you get when you enable `cacheComponents`. The old `experimental.ppr` flag and `experimental_ppr` segment export were removed.

## 239: What happens if you access dynamic data outside `<Suspense>` with Cache Components on?

The build (and dev) shows an error like "Uncached data was accessed outside of `<Suspense>`". Next.js wants you to decide for each piece of data: either cache it with `"use cache"` or put it in a Suspense boundary so it can stream at request time.

```tsx
import { Suspense } from "react";
import { cookies } from "next/headers";

export default function Page() {
  return (
    <>
      <h1>Shop</h1>
      <Suspense fallback={<p>Loading cart...</p>}>
        <Cart />
      </Suspense>
    </>
  );
}

async function Cart() {
  const cartId = (await cookies()).get("cartId")?.value;
  const cart = await getCart(cartId);
  return <p>{cart.items.length} items</p>;
}
```

## 240: Can you use `cookies()` inside a `"use cache"` function?

No. Request-time APIs like `cookies()`, `headers()` and `searchParams` can't be used inside `"use cache"` because the result is shared across users. Read them outside and pass the values you need as arguments.

```tsx
async function Page() {
  const lang = (await cookies()).get("lang")?.value ?? "en";
  return <Translations lang={lang} />;
}

async function Translations({ lang }: { lang: string }) {
  "use cache";
  const t = await loadTranslations(lang);
  return <p>{t.hello}</p>;
}
```

For cache entries that are per-user, there is the experimental `"use cache: private"` variant.

## 241: How does the Pages Router `getStaticProps` `revalidate` compare to App Router revalidation?

They do the same thing: regenerate the page in the background after some seconds.

```tsx
// Pages Router
export async function getStaticProps() {
  return { props: { posts: await getPosts() }, revalidate: 60 };
}
```

```tsx
// App Router (without Cache Components)
export const revalidate = 60;
```

```tsx
// App Router (with Cache Components)
async function getPosts() {
  "use cache";
  cacheLife({ revalidate: 60 });
  return db.post.findMany();
}
```

## 242: How do you do on-demand revalidation in the Pages Router?

Call `res.revalidate(path)` in an API route.

```ts
// pages/api/revalidate.ts
import type { NextApiRequest, NextApiResponse } from "next";

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse,
) {
  if (req.query.secret !== process.env.REVALIDATE_SECRET) {
    return res.status(401).json({ message: "Invalid token" });
  }
  await res.revalidate("/blog");
  return res.json({ revalidated: true });
}
```

## 243: What does `fallback` mean in `getStaticPaths`?

- `false`: paths not returned give a 404.
- `true`: the page shows a fallback version first (check `router.isFallback`), then loads the data in the background.
- `'blocking'`: the server renders the page on the first request and waits before sending it, like SSR, then caches it.

## 244: How do you share data between layouts and pages without prop drilling?

You can't pass props from a layout to a page. Instead, fetch the data in both places with a memoized function. With `fetch` or React `cache`, the request only runs once per render.

```ts
// lib/data.ts
import { cache } from "react";

export const getCurrentUser = cache(async () => {
  const session = await verifySession();
  return db.user.findUnique({ where: { id: session.userId } });
});
```

Both `layout.tsx` and `page.tsx` can call `getCurrentUser()`.

## 245: How do you use the `preload` pattern?

Start a request early without waiting for it, so the data is ready when a child component needs it.

```ts
// lib/item.ts
import { cache } from "react";
import "server-only";

export const preload = (id: string) => {
  void getItem(id);
};

export const getItem = cache(async (id: string) => {
  return db.item.findUnique({ where: { id } });
});
```

```tsx
export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  preload(id); // start loading now
  const isAvailable = await checkAvailability();
  return isAvailable ? <Item id={id} /> : null;
}
```

## 246: How do you create a typed link with typed routes?

Turn on `typedRoutes` in `next.config.ts`. Next.js generates types for all your routes, and TypeScript shows an error when you link to a path that doesn't exist.

```ts
const nextConfig = {
  typedRoutes: true,
};
```

```tsx
<Link href="/about" />          // ok
<Link href="/abuot" />          // type error
<Link href={`/blog/${slug}`} /> // ok for dynamic routes
```

For dynamic strings, you can cast with `as Route` (imported from `next`).

## 247: What are `PageProps` and `LayoutProps` helpers?

They are global types that Next.js generates from your routes. They give you correct types for `params` and `searchParams` without writing them by hand.

```tsx
// app/blog/[slug]/page.tsx
export default async function Page(props: PageProps<"/blog/[slug]">) {
  const { slug } = await props.params;
  return <h1>{slug}</h1>;
}
```

```tsx
// app/dashboard/layout.tsx
export default function Layout(props: LayoutProps<"/dashboard">) {
  return <section>{props.children}</section>;
}
```

Types are generated during `next dev`, `next build`, or with `next typegen`. `LayoutProps` also includes the names of parallel route slots.

## 248: How do you test Next.js apps?

- **Unit tests**: Jest (with `next/jest`) or Vitest with React Testing Library, for Client Components, hooks and helper functions.
- **End-to-end tests**: Playwright or Cypress for full user flows in a real browser.

Async Server Components are not fully supported by Jest and Vitest yet, so test them with end-to-end tests.

## 249: How do you set up Jest with Next.js?

Use the `next/jest` helper. It loads your `next.config`, `.env` files, and handles CSS and image imports.

```ts
// jest.config.ts
import type { Config } from "jest";
import nextJest from "next/jest.js";

const createJestConfig = nextJest({ dir: "./" });

const config: Config = {
  testEnvironment: "jsdom",
  setupFilesAfterEnv: ["<rootDir>/jest.setup.ts"],
};

export default createJestConfig(config);
```

## 250: How do you set up Vitest with Next.js?

```bash
npm install -D vitest @vitejs/plugin-react jsdom @testing-library/react vite-tsconfig-paths
```

```ts
// vitest.config.mts
import { defineConfig } from "vitest/config";
import react from "@vitejs/plugin-react";
import tsconfigPaths from "vite-tsconfig-paths";

export default defineConfig({
  plugins: [tsconfigPaths(), react()],
  test: {
    environment: "jsdom",
  },
});
```

```tsx
// __tests__/page.test.tsx
import { render, screen } from "@testing-library/react";
import { expect, test } from "vitest";
import Page from "../app/page";

test("renders heading", () => {
  render(<Page />);
  expect(screen.getByRole("heading", { level: 1 })).toBeDefined();
});
```

## 251: How do you mock `next/navigation` in unit tests?

Mock the module with your test runner.

```ts
import { vi } from "vitest";

vi.mock("next/navigation", () => ({
  useRouter: () => ({ push: vi.fn(), replace: vi.fn(), refresh: vi.fn() }),
  usePathname: () => "/dashboard",
  useSearchParams: () => new URLSearchParams("q=test"),
}));
```

## 252: What is `instrumentation.ts`?

A file in the root (or `src`) folder that runs once when a new Next.js server instance starts. It is used to set up monitoring and tracing tools like OpenTelemetry or Sentry.

```ts
// instrumentation.ts
export async function register() {
  if (process.env.NEXT_RUNTIME === "nodejs") {
    await import("./instrumentation.node");
  }
}
```

## 253: What is `onRequestError` in `instrumentation.ts`?

A hook that runs whenever the server catches an error during a request. You can send the error to your monitoring service.

```ts
// instrumentation.ts
import type { Instrumentation } from "next";

export const onRequestError: Instrumentation.onRequestError = async (
  err,
  request,
  context,
) => {
  await fetch("https://monitoring.example.com/report", {
    method: "POST",
    body: JSON.stringify({
      message: (err as Error).message,
      path: request.path,
      routeType: context.routeType,
    }),
    headers: { "Content-Type": "application/json" },
  });
};
```

## 254: What is `instrumentation-client.ts`?

A file that runs in the browser before your app's code starts running. You use it to set up client-side analytics, error tracking or performance monitoring.

```ts
// instrumentation-client.ts
window.addEventListener("error", (event) => {
  reportError(event.error);
});

export function onRouterTransitionStart(
  url: string,
  navigationType: "push" | "replace" | "traverse",
) {
  console.log(`Navigating to ${url} (${navigationType})`);
}
```

## 255: How do you measure Web Vitals in Next.js?

Use the `useReportWebVitals` hook in a Client Component.

```tsx
// app/web-vitals.tsx
"use client";

import { useReportWebVitals } from "next/web-vitals";

export function WebVitals() {
  useReportWebVitals((metric) => {
    navigator.sendBeacon("/api/vitals", JSON.stringify(metric));
  });
  return null;
}
```

Then render `<WebVitals />` in your root layout.

## 256: What is draft mode?

Draft mode lets editors preview unpublished content from a headless CMS. When draft mode is on, pages are rendered on each request instead of served from the static cache, so you can fetch draft content.

```ts
// app/api/draft/route.ts
import { draftMode } from "next/headers";
import { redirect } from "next/navigation";

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  if (searchParams.get("secret") !== process.env.DRAFT_SECRET) {
    return new Response("Invalid token", { status: 401 });
  }

  const draft = await draftMode();
  draft.enable();
  redirect(searchParams.get("slug") ?? "/");
}
```

```tsx
// app/blog/[slug]/page.tsx
import { draftMode } from "next/headers";

export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { isEnabled } = await draftMode();
  const { slug } = await params;
  const post = await getPost(slug, { draft: isEnabled });
  return <h1>{post.title}</h1>;
}
```

## 257: What is `output: 'standalone'`?

It makes `next build` create a `.next/standalone` folder with only the files needed to run the app, including a small `server.js` and only the needed parts of `node_modules`. It is great for Docker images.

```ts
const nextConfig = {
  output: "standalone",
};
```

```bash
node .next/standalone/server.js
```

You need to copy the `public` and `.next/static` folders into the standalone folder yourself (or serve them from a CDN).

## 258: What does a basic Dockerfile for Next.js look like?

```dockerfile
FROM node:22-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci

FROM node:22-alpine AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build

FROM node:22-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production
COPY --from=builder /app/public ./public
COPY --from=builder /app/.next/standalone ./
COPY --from=builder /app/.next/static ./.next/static
EXPOSE 3000
CMD ["node", "server.js"]
```

This uses `output: 'standalone'` in `next.config.ts`.

## 259: What is `basePath`?

It lets you host the app under a sub-path of a domain, like `example.com/docs`.

```ts
const nextConfig = {
  basePath: "/docs",
};
```

`Link` and `router.push` add the base path for you. For plain `<img>` tags or `fetch` to your own routes, you have to add it yourself.

## 260: What is `assetPrefix`?

It sets a URL prefix for static assets in `/_next/static`, so you can serve them from a CDN.

```ts
const nextConfig = {
  assetPrefix: "https://cdn.example.com",
};
```

Files in the `public` folder are not affected.

## 261: What does `trailingSlash` do?

By default, Next.js redirects `/about/` to `/about`. With `trailingSlash: true`, it does the opposite and redirects `/about` to `/about/`.

```ts
const nextConfig = {
  trailingSlash: true,
};
```

It is useful for static hosts that serve `about/index.html`.

## 262: What is `transpilePackages`?

It tells Next.js to compile certain packages from `node_modules`. It is common in monorepos where shared packages are written in TypeScript and not prebuilt.

```ts
const nextConfig = {
  transpilePackages: ["@acme/ui", "@acme/utils"],
};
```

## 263: What is `serverExternalPackages`?

It lists packages that should not be bundled into Server Components and Route Handlers, but loaded with Node.js `require` at runtime instead. This is needed for packages that use native code or special Node.js features.

```ts
const nextConfig = {
  serverExternalPackages: ["@prisma/client", "sharp"],
};
```

Many popular packages are already on the built-in list. This option was called `experimental.serverComponentsExternalPackages` before Next.js 15.

## 264: What is `optimizePackageImports`?

Some packages export hundreds of modules from one entry file (like icon libraries). Importing one item can make the bundler load all of them. This option makes Next.js load only the modules you actually use.

```ts
const nextConfig = {
  experimental: {
    optimizePackageImports: ["my-icon-library"],
  },
};
```

Common libraries like `lucide-react`, `date-fns` and `lodash-es` are already optimized by default.

## 265: How do you configure Turbopack?

Use the top-level `turbopack` key in `next.config.ts`.

```ts
const nextConfig = {
  turbopack: {
    resolveAlias: {
      underscore: "lodash",
    },
    rules: {
      "*.svg": {
        loaders: ["@svgr/webpack"],
        as: "*.js",
      },
    },
  },
};
```

In older versions this was under `experimental.turbo`.

## 266: What happens if you have a custom `webpack` config and run `next build` in Next.js 16?

Turbopack doesn't use the `webpack` function. To avoid a build that silently ignores your config, `next build` fails if it finds a custom webpack config while using Turbopack. You can either move the config to the `turbopack` options or build with `next build --webpack`.

## 267: How do you analyze bundle size?

With webpack, use `@next/bundle-analyzer`:

```ts
// next.config.ts
import bundleAnalyzer from "@next/bundle-analyzer";

const withBundleAnalyzer = bundleAnalyzer({
  enabled: process.env.ANALYZE === "true",
});

export default withBundleAnalyzer({});
```

```bash
ANALYZE=true next build --webpack
```

Newer versions of Next.js also have an experimental analyzer for Turbopack builds (`next experimental-analyze`).

## 268: What is the difference between `useRouter().push` and `redirect()`?

- `redirect()` works in Server Components, Server Actions and Route Handlers. It can also be used in Client Components during render, but not in event handlers.
- `router.push()` is for Client Components, usually in event handlers.

In a Server Action called from a form, use `redirect()`. After a click on a button, use `router.push()`.

## 269: What does `RedirectType` do in `redirect()`?

It decides if the redirect adds a new history entry or replaces the current one.

```ts
import { redirect, RedirectType } from "next/navigation";

redirect("/login", RedirectType.replace);
```

By default, `redirect` uses `push` in Server Actions and `replace` everywhere else.

## 270: How do you show a different UI based on the user's device?

You can read the `User-Agent` with `userAgent()` in Proxy, or `headers()` in a Server Component.

```ts
// proxy.ts
import { NextResponse, userAgent, type NextRequest } from "next/server";

export function proxy(request: NextRequest) {
  const { device } = userAgent(request);
  const viewport = device.type === "mobile" ? "mobile" : "desktop";
  request.nextUrl.searchParams.set("viewport", viewport);
  return NextResponse.rewrite(request.nextUrl);
}
```

For most layouts, CSS media queries are a better choice because they don't make the page dynamic.

## 271: How do you add a loading state when submitting a form that navigates?

With `next/form`, you can read the pending state with `useFormStatus` in a child component.

```tsx
"use client";

import { useFormStatus } from "react-dom";

export function SearchButton() {
  const { pending } = useFormStatus();
  return <button type="submit">{pending ? "Searching..." : "Search"}</button>;
}
```

```tsx
import Form from "next/form";
import { SearchButton } from "./search-button";

export default function Page() {
  return (
    <Form action="/search">
      <input name="query" />
      <SearchButton />
    </Form>
  );
}
```

## 272: How do you prevent a component from being included in the static shell?

Read request data (or call `connection()`) inside it and wrap it in `<Suspense>`. Everything inside the boundary is rendered at request time, and the fallback becomes part of the static shell.

## 273: How do you handle file uploads in a Server Action?

The file comes in the `FormData` as a `File` object.

```tsx
// app/upload/page.tsx
import { writeFile } from "node:fs/promises";

export default function Page() {
  async function upload(formData: FormData) {
    "use server";
    const file = formData.get("file") as File;
    const bytes = Buffer.from(await file.arrayBuffer());
    await writeFile(`./uploads/${file.name}`, bytes);
  }

  return (
    <form action={upload}>
      <input type="file" name="file" />
      <button>Upload</button>
    </form>
  );
}
```

In real apps, upload to object storage like S3 instead of the local disk, check the file type and size, and never trust `file.name` as a safe path. For big files, consider uploading from the browser straight to storage with a signed URL, because of the Server Action body size limit.

## 274: What is the `onNavigate` prop on `Link`?

It runs when a client-side navigation is about to happen through that link. You can cancel the navigation with `e.preventDefault()`. This is useful for things like "you have unsaved changes" prompts.

```tsx
"use client";

import Link from "next/link";

export function SafeLink({ hasChanges }: { hasChanges: boolean }) {
  return (
    <Link
      href="/next-page"
      onNavigate={(e) => {
        if (hasChanges && !confirm("Leave without saving?")) {
          e.preventDefault();
        }
      }}
    >
      Next
    </Link>
  );
}
```

Unlike `onClick`, it doesn't run for clicks with modifier keys that open a new tab.

## 275: What is the `prefetch` prop on `Link` and what values does it accept?

- `null` / `"auto"` (default): for static routes, the full route is prefetched. For dynamic routes, only the part down to the nearest `loading.tsx` is prefetched.
- `true`: the full route is prefetched, both static and dynamic.
- `false`: no prefetching, not even on hover.

Prefetching only happens in production.

## 276: What improvements did Next.js 16 make to navigation and prefetching?

- **Layout deduplication**: when many links share a layout, the layout is downloaded once instead of once per link.
- **Incremental prefetching**: Next.js only prefetches the parts that are not already in the cache, and cancels requests when links leave the viewport.

You may see more prefetch requests in the network tab, but the total amount of data is much smaller.

## 277: What is the React Compiler and how do you enable it in Next.js?

The React Compiler automatically adds memoization to your components, so you don't need to write `useMemo`, `useCallback` and `React.memo` by hand as often. Support is stable in Next.js 16, but not enabled by default.

```bash
npm install -D babel-plugin-react-compiler
```

```ts
const nextConfig = {
  reactCompiler: true,
};
```

It uses Babel, so compile times in dev and build can be a bit longer.

## 278: How do you add security headers to every response?

Use `headers()` in `next.config.ts`:

```ts
const securityHeaders = [
  { key: "X-Content-Type-Options", value: "nosniff" },
  { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
  { key: "X-Frame-Options", value: "DENY" },
  {
    key: "Strict-Transport-Security",
    value: "max-age=63072000; includeSubDomains; preload",
  },
  {
    key: "Permissions-Policy",
    value: "camera=(), microphone=(), geolocation=()",
  },
];

const nextConfig = {
  async headers() {
    return [{ source: "/(.*)", headers: securityHeaders }];
  },
};
```

You can also turn off the `X-Powered-By` header with `poweredByHeader: false`.

## 279: How do you redirect based on a database lookup?

`next.config.ts` redirects are static and read at build time. For a large or changing list, check it in Proxy or in a Route Handler. For thousands of redirects, a common approach is to store them in a fast lookup (like a Bloom filter or key-value store) and check them in Proxy.

```ts
// proxy.ts
import { NextResponse, type NextRequest } from "next/server";

export async function proxy(request: NextRequest) {
  const target = await redirectStore.get(request.nextUrl.pathname);
  if (target) {
    return NextResponse.redirect(new URL(target, request.url), 308);
  }
  return NextResponse.next();
}
```

## 280: How do you build a multi-tenant app with subdomains?

Read the host in Proxy and rewrite to a route that includes the tenant.

```ts
// proxy.ts
import { NextResponse, type NextRequest } from "next/server";

export function proxy(request: NextRequest) {
  const host = request.headers.get("host") ?? "";
  const subdomain = host.split(".")[0];

  if (subdomain && subdomain !== "www" && subdomain !== "app") {
    const url = request.nextUrl.clone();
    url.pathname = `/sites/${subdomain}${url.pathname}`;
    return NextResponse.rewrite(url);
  }

  return NextResponse.next();
}
```

```tsx
// app/sites/[tenant]/page.tsx
export default async function TenantHome({
  params,
}: {
  params: Promise<{ tenant: string }>;
}) {
  const { tenant } = await params;
  const site = await getSite(tenant);
  return <h1>{site.name}</h1>;
}
```

## 281: How do you read the current pathname in a Server Component?

Server Components don't have a `usePathname` hook. Options:

- Use `params` to know the dynamic parts of the route.
- Set a header in Proxy (like `x-pathname`) and read it with `headers()`. This makes the route dynamic.
- Move the logic that needs the path into a small Client Component that uses `usePathname`.

The last one is usually the best choice, because it keeps the page static.

## 282: How do you scroll to the top or keep the scroll position after a Server Action?

After a Server Action that revalidates the current page, Next.js updates the UI in place and keeps the scroll position. If you `redirect()` to a new page, Next.js scrolls to the top like a normal navigation.

## 283: How do you upload images from the browser and show them with `next/image`?

If the URL is on a known host, add it to `remotePatterns`. For user uploads stored in a bucket, you might use something like:

```ts
images: {
  remotePatterns: [
    { protocol: 'https', hostname: 'my-bucket.s3.amazonaws.com' },
  ],
},
```

If you can't know the size, use `fill` with a container that has a fixed aspect ratio.

## 284: What is the `useServerInsertedHTML` hook?

It is a hook from `next/navigation` that lets Client Components add HTML to the stream during server rendering, usually `<style>` tags. CSS-in-JS libraries use it so that styles are in the HTML before the content that needs them.

## 285: How do you run a cron job in a Next.js app?

Next.js doesn't have a built-in scheduler. You usually create a Route Handler and call it from an outside scheduler:

- Vercel Cron Jobs (configured in `vercel.json`)
- GitHub Actions on a schedule
- A cron service or a cron job on your own server

```ts
// app/api/cron/cleanup/route.ts
export async function GET(request: Request) {
  if (
    request.headers.get("authorization") !== `Bearer ${process.env.CRON_SECRET}`
  ) {
    return new Response("Unauthorized", { status: 401 });
  }
  await deleteOldSessions();
  return Response.json({ ok: true });
}
```

## 286: How do you use `generateImageMetadata`?

It lets one `icon` or `opengraph-image` file generate several images, for example in different sizes.

```tsx
// app/icon.tsx
import { ImageResponse } from "next/og";

export function generateImageMetadata() {
  return [
    { contentType: "image/png", size: { width: 48, height: 48 }, id: "small" },
    { contentType: "image/png", size: { width: 72, height: 72 }, id: "medium" },
  ];
}

export default async function Icon({ id }: { id: Promise<string> }) {
  const iconId = await id;
  return new ImageResponse(
    <div style={{ fontSize: 24, display: "flex" }}>
      {iconId === "small" ? "S" : "M"}
    </div>,
  );
}
```

## 287: How do you create multiple sitemaps for a large site?

Use `generateSitemaps` to split the sitemap into parts.

```ts
// app/product/sitemap.ts
import type { MetadataRoute } from "next";

export async function generateSitemaps() {
  return [{ id: 0 }, { id: 1 }, { id: 2 }];
}

export default async function sitemap({
  id,
}: {
  id: Promise<number>;
}): Promise<MetadataRoute.Sitemap> {
  const page = await id;
  const start = page * 50000;
  const products = await getProducts(start, 50000);
  return products.map((p) => ({ url: `https://example.com/product/${p.id}` }));
}
```

The sitemaps are served at `/product/sitemap/0.xml`, `/product/sitemap/1.xml`, and so on. Google allows up to 50,000 URLs per sitemap.

## 288: How do you create a web app manifest?

Add `app/manifest.ts` (or a static `manifest.json`).

```ts
// app/manifest.ts
import type { MetadataRoute } from "next";

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: "My App",
    short_name: "App",
    start_url: "/",
    display: "standalone",
    background_color: "#ffffff",
    theme_color: "#000000",
    icons: [{ src: "/icon-192.png", sizes: "192x192", type: "image/png" }],
  };
}
```

## 289: How do you add JSON-LD structured data?

Render a `<script>` tag with the data in your page.

```tsx
export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  const product = await getProduct(id);

  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "Product",
    name: product.name,
    image: product.image,
  };

  return (
    <section>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify(jsonLd).replace(/</g, "\\u003c"),
        }}
      />
      <h1>{product.name}</h1>
    </section>
  );
}
```

Replacing `<` stops a value containing `</script>` from breaking out of the tag.

## 290: How do you set canonical URLs and alternate languages?

Use `alternates` in metadata.

```ts
export const metadata: Metadata = {
  alternates: {
    canonical: "/blog/my-post",
    languages: {
      "en-US": "/en-US/blog/my-post",
      "de-DE": "/de-DE/blog/my-post",
    },
  },
};
```

## 291: How do you stop search engines from indexing a page?

Use the `robots` field in metadata.

```ts
export const metadata: Metadata = {
  robots: {
    index: false,
    follow: false,
  },
};
```

## 292: What is the difference between `useEffect` data fetching and Server Component data fetching?

With `useEffect`, the browser first loads JavaScript, renders an empty state, and only then starts fetching. That means more loading spinners and slower content. It also exposes your API to the client.

With Server Components, the data is fetched on the server before the HTML is sent, close to the database, and the result is part of the first response. Use client fetching only for data that changes often while the user is on the page, or for user-specific interactions.

## 293: How do you poll for new data in the App Router?

Options:

- Call `router.refresh()` on an interval in a Client Component. The server re-renders and only the changes are applied.
- Use SWR or TanStack Query with `refreshInterval` against a Route Handler.

```tsx
"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";

export function AutoRefresh({ ms = 10000 }: { ms?: number }) {
  const router = useRouter();

  useEffect(() => {
    const id = setInterval(() => router.refresh(), ms);
    return () => clearInterval(id);
  }, [router, ms]);

  return null;
}
```

For real-time updates, use WebSockets or Server-Sent Events through a separate service or a Route Handler stream.

## 294: How do you migrate a page from the Pages Router to the App Router?

1. Create the same route in `app` (for example, `pages/about.tsx` becomes `app/about/page.tsx`).
2. Move `_app.tsx` and `_document.tsx` logic into `app/layout.tsx`.
3. Replace `getStaticProps` / `getServerSideProps` with data fetching inside the Server Component.
4. Replace `getStaticPaths` with `generateStaticParams`.
5. Replace `next/head` with the `metadata` export.
6. Change `next/router` imports to `next/navigation`.
7. Add `"use client"` to components that use state, effects or browser APIs.
8. Delete the old file in `pages`.

You can migrate one route at a time.

## 295: How do you replace `next/head` in the App Router?

`next/head` is not supported in the App Router. Use the `metadata` export or `generateMetadata`. For tags not covered by the API, you can render them in your components; React 19 hoists `<title>`, `<meta>` and `<link>` tags into the `<head>`.

## 296: How do you use the `Link` component with a custom component?

`Link` renders an `<a>` itself, so put your styled content inside it. You don't need `passHref` or `legacyBehavior` anymore (those are for old versions).

```tsx
<Link href="/pricing" className="btn btn-primary">
  View pricing
</Link>
```

If you have a design system button that renders an `<a>`, many libraries support an `asChild` pattern or a `component={Link}` prop.

## 297: What does `export const maxDuration` do?

It sets the max time in seconds that a page, Route Handler or Server Action can run on platforms that support it (like Vercel functions).

```ts
// app/api/report/route.ts
export const maxDuration = 60;
```

It doesn't change anything when you run `next start` on your own server.

## 298: How do you get the `params` of a page in `generateMetadata` and in the page without fetching twice?

Use the same data function in both. If it uses `fetch`, it is memoized automatically. If it uses a database, wrap it in React `cache`.

```ts
import { cache } from "react";

export const getPost = cache(async (slug: string) => {
  return db.post.findUnique({ where: { slug } });
});
```

## 299: What is the difference between `force-cache`, `no-store` and the default in `fetch`?

- `cache: 'force-cache'`: look in the Data Cache first. If there is a match, use it. If not, fetch and store the result.
- `cache: 'no-store'`: always fetch from the source, never store.
- Default (no option): Next.js doesn't cache the fetch. On a static route the result is still part of the prerendered page, while on a dynamic route it runs on every request.

## 300: How do you set different revalidate times for different fetches on one page?

Pass `next.revalidate` to each `fetch`.

```ts
const posts = await fetch("https://api.example.com/posts", {
  next: { revalidate: 3600 },
});
const prices = await fetch("https://api.example.com/prices", {
  next: { revalidate: 60 },
});
```

Each fetch is cached separately. For the whole static route, Next.js uses the lowest value (here 60 seconds) as the route's revalidate time.

# Advanced Questions (301-450)

## 301: What is the RSC payload?

The React Server Component payload is a compact data format that describes the rendered Server Component tree. It contains:

- The rendered output of Server Components
- Placeholders for where Client Components go, plus references to their JavaScript files
- Props passed from Server Components to Client Components

On the first load, Next.js sends HTML (for a fast first paint) and the RSC payload (inlined in the HTML) so React can hydrate. On client navigations, Next.js only fetches the RSC payload, not HTML, and React uses it to update the page.

## 302: How does a client-side navigation work in the App Router step by step?

1. The user clicks a `Link`.
2. The router checks the Router Cache for the target route's segments, including anything prefetched.
3. For missing segments, it requests the RSC payload from the server (with special headers like `RSC: 1`).
4. The server renders only the segments that changed. Shared layouts above them are not rendered again.
5. The client merges the new segments into the existing tree. Shared layouts keep their state.
6. If a segment suspends, the `loading.tsx` fallback shows while the rest streams in.
7. The browser URL and history are updated.

## 303: Why do shared layouts not re-render on navigation, and what are the consequences?

The router keeps the React tree for layouts that are shared between the old and new route, and only swaps the parts below them. This gives fast navigations and keeps state like scroll positions in sidebars.

Consequences:

- Data fetched in a layout isn't fetched again on each navigation under it.
- Layouts don't get `searchParams` because they would get out of date.
- Auth checks in a layout don't run on every navigation, so don't rely only on them.
- If you need code to run on every navigation, use `template.tsx` or a Client Component with `usePathname`.

## 304: What can be passed as props from a Server Component to a Client Component?

Values that React can serialize:

- Primitives: string, number, bigint, boolean, `undefined`, `null`
- Plain objects and arrays with serializable values
- `Date`, `Map`, `Set`, typed arrays, `ArrayBuffer`
- Promises (read with `use()`)
- JSX / React elements (including Server Components)
- Server Functions (functions marked with `"use server"`)
- `FormData`

Not allowed: regular functions, class instances, symbols that are not global, and objects with a custom prototype. If you pass them, you get an error at render time.

## 305: How does the server/client boundary work in the module graph?

`"use client"` marks an entry point. When a Server Component imports a module with that directive, the bundler doesn't include that module in the server render as normal code. Instead, it creates a client reference. That module and everything it imports go into the client bundle.

So:

- Files imported only from Server Components never reach the browser.
- A shared util imported by a Client Component is bundled for the client too.
- Adding `"use client"` high up in the tree (for example to a layout) moves the whole subtree to the client.

Put `"use client"` as low in the tree as you can.

## 306: Why would a component render as both a Server and a Client Component?

A component without a directive takes the role of whoever imports it. If a Server Component imports `Button`, it renders as a Server Component. If a Client Component imports the same `Button`, it becomes a Client Component in that place. This is normal. It only fails if the component uses something that only one side supports, like hooks or `async`.

## 307: How do you keep secrets from leaking into Client Components?

- Mark server-only modules with `import 'server-only'`.
- Don't prefix secrets with `NEXT_PUBLIC_`.
- Don't pass full database records to Client Components. Map them to small objects (DTOs) with only the fields the UI needs.
- Use a Data Access Layer that checks auth and returns safe data.
- Optionally use the React Taint APIs to block certain objects or values from being passed to the client.

```ts
// lib/dto.ts
import "server-only";

export async function getProfileDTO(userId: string) {
  const user = await db.user.findUnique({ where: { id: userId } });
  return { name: user!.name, avatarUrl: user!.avatarUrl }; // no password hash, no email
}
```

## 308: What are the React Taint APIs?

They let you mark an object or a value so that React throws an error if it is passed to a Client Component.

```ts
// next.config.ts
const nextConfig = {
  experimental: {
    taint: true,
  },
};
```

```ts
import {
  experimental_taintObjectReference,
  experimental_taintUniqueValue,
} from "react";

export async function getUser(id: string) {
  const user = await db.user.findUnique({ where: { id } });
  experimental_taintObjectReference(
    "Do not pass the user object to the client",
    user!,
  );
  experimental_taintUniqueValue(
    "Do not pass the API key to the client",
    process,
    process.env.API_KEY!,
  );
  return user;
}
```

It is an extra safety net, not a full solution. Copies of tainted values (for example, spreading the object) are not protected.

## 309: What is a Data Access Layer (DAL) and why is it recommended?

A DAL is a set of server-only functions that are the only place in your app that talks to the database. Each function checks the session and permissions and returns only safe data.

Benefits:

- Auth checks happen in one place, close to the data.
- Pages, layouts and Server Actions can't accidentally skip a check.
- It is easier to audit what data leaves the server.

```ts
// lib/dal/posts.ts
import "server-only";
import { verifySession } from "./session";

export async function getMyDrafts() {
  const { userId } = await verifySession();
  return db.post.findMany({
    where: { authorId: userId, published: false },
    select: { id: true, title: true, updatedAt: true },
  });
}
```

## 310: How are closure variables in inline Server Actions protected?

When you define a Server Action inside a component, it can use variables from the component's scope. Those values have to be sent to the client and back when the action is called. Next.js encrypts them with a key created per build, so the client can't read or change them.

```tsx
export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;

  async function publish() {
    "use server";
    await db.post.update({ where: { id }, data: { published: true } }); // `id` is encrypted
  }

  return (
    <form action={publish}>
      <button>Publish</button>
    </form>
  );
}
```

Encryption is not a replacement for auth checks. Don't put secrets in closures, and still check that the user may publish this post.

## 311: Why do you need `NEXT_SERVER_ACTIONS_ENCRYPTION_KEY` when self-hosting with multiple servers?

Each build creates a new random key for encrypting Server Action closures. If you run several instances from different builds, or build in more than one place, one server may not be able to decrypt values encrypted by another. Setting `NEXT_SERVER_ACTIONS_ENCRYPTION_KEY` (a base64 AES key) makes all instances use the same key.

## 312: How does Next.js protect Server Actions from CSRF?

- Server Actions are only called with `POST`.
- Modern browsers use `SameSite=Lax` cookies by default, so cross-site POSTs don't carry session cookies in most cases.
- Next.js compares the `Origin` header with the `Host` header (or `X-Forwarded-Host`). If they don't match, the request is rejected.

If you have a reverse proxy or a different domain that calls your actions, add it to the allowed list:

```ts
const nextConfig = {
  experimental: {
    serverActions: {
      allowedOrigins: ["my-proxy.example.com", "*.my-proxy.example.com"],
    },
  },
};
```

## 313: How are Server Action IDs created and why does it matter?

Next.js gives each Server Action a hashed ID. The client only knows the ID, not the function name or code. IDs are re-created for each build. Actions that are not used anywhere in the app are removed from the build. This lowers the attack surface, but every exported action is still callable by anyone who finds the ID, so authorization in each action is still needed.

## 314: Are Server Actions run in parallel?

No. Calls to Server Actions from the same client are put in a queue and run one after another. This keeps the order of mutations clear. Because of this, Server Actions are not a good fit for fetching data in parallel. For reads, use Server Components or Route Handlers.

## 315: What happens to the UI after a Server Action finishes?

The response can include:

- The return value of the action
- An updated RSC payload for the current route if you called `revalidatePath`, `revalidateTag`, `updateTag` or `refresh`
- Redirect instructions if you called `redirect`

All of this comes back in one roundtrip. The client applies the new UI and the action result together, so there is no second request to get fresh data.

## 316: What was CVE-2025-29927 and what does it teach about Middleware/Proxy?

It was a vulnerability found in March 2025. An attacker could send an internal header, `x-middleware-subrequest`, and Next.js would skip Middleware entirely. Apps that checked auth only in Middleware were exposed. It was fixed in 12.3.5, 13.5.9, 14.2.25 and 15.2.3.

Lessons:

- Don't make Proxy the only place you check auth.
- Check auth again in your data layer, Server Actions and Route Handlers.
- Keep Next.js up to date, and strip internal headers at your load balancer if you can't upgrade.

## 317: What was the "React2Shell" vulnerability in December 2025?

It was a critical remote code execution bug in how React Server Components decode data sent to Server Functions (CVE-2025-55182 in React, tracked in Next.js as CVE-2025-66478). A crafted request could run code on the server, even in apps that didn't define any Server Actions themselves, because the RSC endpoint was still there. Patched versions of React and Next.js 15.x and 16.x were released.

The lesson: any framework that accepts serialized data from the client has a large attack surface. Keep React and Next.js on the latest patch, and follow the Next.js security releases. As of mid-2026, Next.js publishes scheduled monthly security releases, with an Active LTS line (16.2.x) and a Maintenance LTS line (15.5.x).

## 318: How do you implement a Content Security Policy with nonces?

Create a nonce per request in Proxy, add it to the CSP header, and pass it to the app. Next.js reads the nonce from the `Content-Security-Policy` request header and adds it to its own scripts.

```ts
// proxy.ts
import { NextResponse, type NextRequest } from "next/server";

export function proxy(request: NextRequest) {
  const nonce = Buffer.from(crypto.randomUUID()).toString("base64");
  const csp = [
    `default-src 'self'`,
    `script-src 'self' 'nonce-${nonce}' 'strict-dynamic'`,
    `style-src 'self' 'nonce-${nonce}'`,
    `img-src 'self' blob: data:`,
    `object-src 'none'`,
    `base-uri 'self'`,
    `frame-ancestors 'none'`,
  ].join("; ");

  const requestHeaders = new Headers(request.headers);
  requestHeaders.set("x-nonce", nonce);
  requestHeaders.set("Content-Security-Policy", csp);

  const response = NextResponse.next({ request: { headers: requestHeaders } });
  response.headers.set("Content-Security-Policy", csp);
  return response;
}
```

```tsx
// in a Server Component
import { headers } from "next/headers";
import Script from "next/script";

export default async function Page() {
  const nonce = (await headers()).get("x-nonce") ?? undefined;
  return (
    <Script
      src="https://www.googletagmanager.com/gtag/js"
      strategy="afterInteractive"
      nonce={nonce}
    />
  );
}
```

A nonce must be different on every request, so all pages using it become dynamic and can't be served from a static cache. If you need static pages, consider a hash-based CSP or Subresource Integrity (experimental `sri` option) instead.

## 319: How does the cache key for `"use cache"` work?

The key is built from:

- The build ID (a new deploy gives new keys)
- A unique ID of the function (based on its location in the code)
- The serializable arguments passed to the function
- Serializable values captured from outer scopes (closures)

So `getProducts('shoes')` and `getProducts('hats')` are cached separately. Arguments that can't be serialized, like `children` or other JSX, can be passed through but are not part of the key. They are treated as holes that are filled in later, so you can cache a wrapper component without caching its children.

## 320: How does `"use cache"` handle `children` and other non-serializable props?

You can pass JSX like `children` into a cached component. The cached output stores a reference to where `children` goes, not the children themselves. When rendered, the current `children` are placed in that spot. So a cached layout wrapper can wrap dynamic content.

```tsx
async function CachedShell({ children }: { children: React.ReactNode }) {
  "use cache";
  const nav = await getNavigation();
  return (
    <div>
      <Nav items={nav} />
      {children}
    </div>
  );
}
```

The rule is: you can pass these values through, but you can't read or inspect them inside the cached function.

## 321: Where is `"use cache"` data stored by default, and what are `"use cache: remote"` and `"use cache: private"`?

- `"use cache"`: the default handler keeps entries in memory on the server (an LRU cache). Results that are part of prerendering also end up in the static shell. When self-hosting with many instances, each instance has its own memory cache.
- `"use cache: remote"`: stores entries in a remote cache handler (for example Redis or the platform's cache), so they are shared between instances and survive restarts. You configure handlers with `cacheHandlers` in `next.config.ts`.
- `"use cache: private"` (experimental): caches per user, in the browser's memory only. It is allowed to read `cookies()` and `headers()`, and is never stored on the server.

## 322: How do you configure a custom cache handler for `"use cache"`?

Use `cacheHandlers` in `next.config.ts`, mapping a name to a file that implements the handler interface (`get`, `set`, `refreshTags`, `getExpiration`, `updateTags`).

```ts
// next.config.ts
const nextConfig = {
  cacheComponents: true,
  cacheHandlers: {
    default: require.resolve("./cache-handlers/memory.js"),
    remote: require.resolve("./cache-handlers/redis.js"),
  },
};
```

Then `"use cache: remote"` uses your Redis handler. This is separate from the older `cacheHandler` (singular) option, which is for the ISR and `fetch` Data Cache.

## 323: How do you define custom `cacheLife` profiles?

In `next.config.ts`:

```ts
const nextConfig = {
  cacheComponents: true,
  cacheLife: {
    blog: {
      stale: 3600, // 1 hour
      revalidate: 900, // 15 minutes
      expire: 86400, // 1 day
    },
  },
};
```

```ts
import { cacheLife } from "next/cache";

export async function getPosts() {
  "use cache";
  cacheLife("blog");
  return db.post.findMany();
}
```

You can also override built-in profiles like `default` here.

## 324: What happens when you nest cached functions with different `cacheLife` values?

When a `"use cache"` scope calls another cached function, the outer entry can't stay fresh longer than the inner data. If the outer scope doesn't set its own `cacheLife`, it takes the shortest values from the inner ones. If it sets its own profile explicitly, that wins for the outer entry. Tags from inner caches also apply to the outer entry, so revalidating an inner tag also invalidates the outer one.

## 325: Why can a short `cacheLife` make a component dynamic?

During prerendering, a `"use cache"` entry with a very short life (a revalidate of zero or an expire time under about five minutes, like the `'seconds'` profile) is not included in the static shell. It would be stale almost right away. So Next.js treats it like dynamic content: it is rendered at request time and needs a `<Suspense>` boundary.

## 326: How do you use `Date.now()` or `Math.random()` with Cache Components?

During prerendering, Next.js doesn't know if a value from `Date.now()` or `Math.random()` should be fixed at build time or fresh per request, so it gives an error. Pick one:

- **Per request**: call `await connection()` first (and wrap in `<Suspense>`).
- **Cached**: put it in a `"use cache"` scope, so the value is computed once per cache entry.

```tsx
import { connection } from "next/server";

async function Timestamp() {
  await connection();
  return <p>{new Date().toLocaleTimeString()}</p>;
}
```

If you only need it in the browser, compute it in a Client Component inside `useEffect`.

## 327: How does Next.js 16 use React's `<Activity>` with Cache Components?

When `cacheComponents` is on, Next.js keeps the previous route in an `<Activity mode="hidden">` instead of unmounting it on navigation. When the user goes back, the route shows again with its state (form input, expanded sections, and so on) still there. Effects are cleaned up while hidden and set up again when it becomes visible.

A side effect is that hidden routes still hold memory, and code that assumed "navigation away means unmount" may need to change.

## 328: How do you use View Transitions in Next.js?

React has a `<ViewTransition>` component that animates UI changes with the browser's View Transitions API. In Next.js you enable it with an experimental flag:

```ts
const nextConfig = {
  experimental: {
    viewTransition: true,
  },
};
```

```tsx
import { unstable_ViewTransition as ViewTransition } from "react";

export default function Page() {
  return (
    <ViewTransition>
      <ProductGrid />
    </ViewTransition>
  );
}
```

Transitions run for updates inside `startTransition`, which includes Next.js navigations. The API is still experimental, so the import name may change between versions.

## 329: What is `useEffectEvent` and why is it useful in Next.js apps?

`useEffectEvent` (stable in React 19.2, which Next.js 16 uses) lets you read the latest props or state inside an effect without adding them to the dependency array.

```tsx
"use client";

import { useEffect, useEffectEvent } from "react";

export function ChatRoom({ roomId, theme }: { roomId: string; theme: string }) {
  const onConnected = useEffectEvent(() => {
    showToast(`Connected to ${roomId}`, theme);
  });

  useEffect(() => {
    const conn = connect(roomId);
    conn.on("connected", onConnected);
    return () => conn.disconnect();
  }, [roomId]); // theme changes don't reconnect
}
```

## 330: How does streaming affect the HTTP status code?

Once Next.js starts streaming a response, the headers (including the status code) have already been sent, usually as `200`. If `notFound()` or `redirect()` is called later inside a Suspense boundary:

- For `notFound()`, Next.js adds `<meta name="robots" content="noindex">` and renders the not-found UI on the client.
- For `redirect()`, Next.js adds a meta refresh or does a client-side redirect.

If you need the real status code (for SEO), call `notFound()` or `redirect()` before any Suspense boundary, for example at the top of the page before the shell is sent.

## 331: How does the Data Cache behave across deployments?

The `fetch` Data Cache is stored outside the build output, so it survives redeploys. Data cached with `force-cache` or `revalidate` stays until it is revalidated or expires, even after a new deploy. `"use cache"` entries include the build ID in their key, so a new build doesn't reuse old entries.

When self-hosting, the default Data Cache is on the file system in `.next/cache`. With multiple instances or containers that don't share disk, you need a shared cache handler.

## 332: How do you self-host ISR with multiple instances?

By default, each `next start` instance stores ISR and Data Cache entries in its own `.next/cache` folder. With many instances, they would hold different versions and revalidations would only affect one instance.

Fix it with a shared cache handler:

```ts
// next.config.ts
const nextConfig = {
  cacheHandler: require.resolve("./cache-handler.js"),
  cacheMaxMemorySize: 0, // turn off the in-memory cache
};
```

The handler implements `get`, `set` and `revalidateTag`, using something like Redis. For `"use cache"` you configure `cacheHandlers` in the same way.

## 333: What is `deploymentId` and version skew?

Version skew happens when a user's browser has JavaScript from an old deployment while the server runs a new one. For example, a Server Action ID or a chunk file name may no longer exist.

Setting `deploymentId` in `next.config.ts` adds an ID to asset and data requests. When Next.js notices a mismatch, it does a full page reload during navigation so the client picks up the new version.

```ts
const nextConfig = {
  deploymentId: process.env.DEPLOYMENT_VERSION,
};
```

Vercel handles this for you with Skew Protection. When self-hosting, you can also keep older static assets available for a while after a deploy.

## 334: What are Build Adapters?

Build Adapters are an API (alpha in Next.js 16) that lets hosting platforms hook into the build process. An adapter can change the config and read the build output, so platforms like Netlify or Cloudflare can deploy Next.js without patching internals.

```js
// next.config.js
const nextConfig = {
  experimental: {
    adapterPath: require.resolve("./my-adapter.js"),
  },
};
```

Most app developers don't write adapters, but they are why Next.js works better on more platforms.

## 335: What are the differences between the Node.js and Edge runtimes?

- **Node.js runtime** (default): full Node.js APIs, all npm packages, file system access. Best for most pages, Server Actions and Route Handlers.
- **Edge runtime**: a smaller runtime based on Web APIs. Starts faster and can run close to users, but has no file system, no native modules, limited npm support, and a smaller code size limit.

```ts
export const runtime = "edge";
```

Since Proxy moved to Node.js in Next.js 16, and caching now does a lot of what edge rendering used to do, the edge runtime is used less than before. Some features, like Cache Components, need the Node.js runtime.

## 336: How do you trace performance with OpenTelemetry?

Install `@vercel/otel` and register it in `instrumentation.ts`.

```ts
// instrumentation.ts
import { registerOTel } from "@vercel/otel";

export function register() {
  registerOTel({ serviceName: "my-next-app" });
}
```

Next.js creates spans for incoming requests, rendering of routes, `fetch` calls, Route Handlers and more. You can add your own spans with the `@opentelemetry/api` package. Set `NEXT_OTEL_VERBOSE=1` to get more detailed spans.

## 337: How do you log `fetch` requests and cache hits in development?

```ts
const nextConfig = {
  logging: {
    fetches: {
      fullUrl: true,
      hmrRefreshes: true,
    },
  },
};
```

The dev server prints each `fetch` with its cache status (HIT, MISS, SKIP) and the reason it was skipped.

## 338: What is the Next.js DevTools MCP server?

Next.js 16 added support for the Model Context Protocol (MCP). With the `next-devtools-mcp` package, AI coding agents can connect to your running dev server and read things like build and runtime errors, logs, route info and page metadata. The agent can then debug with real context from your app instead of guessing.

```json
{
  "mcpServers": {
    "next-devtools": {
      "command": "npx",
      "args": ["-y", "next-devtools-mcp@latest"]
    }
  }
}
```

## 339: How do you debug a Next.js app on the server side?

- Use `console.log` in Server Components. Logs show in the terminal, not the browser (in dev, Next.js also forwards server logs to the browser console).
- Run `next dev --inspect` and attach the Chrome DevTools or VS Code debugger to the Node.js process.
- Use the VS Code `launch.json` config from the Next.js docs to debug both server and client.

```bash
next dev --inspect
```

## 340: How do you build a large app with multiple Next.js apps under one domain?

Use **Multi-Zones**. Each zone is a separate Next.js app that owns a set of paths. One main app rewrites paths to the others.

```ts
// main app next.config.ts
const nextConfig = {
  async rewrites() {
    return [
      { source: "/blog", destination: `${process.env.BLOG_DOMAIN}/blog` },
      {
        source: "/blog/:path+",
        destination: `${process.env.BLOG_DOMAIN}/blog/:path+`,
      },
    ];
  },
};
```

```ts
// blog app next.config.ts
const nextConfig = {
  assetPrefix: "/blog-static",
};
```

Each zone sets an `assetPrefix` so their static files don't conflict. Links between zones must use plain `<a>` tags, because soft navigation only works inside one app.

## 341: How do you set up Next.js in a monorepo?

- Put shared packages in `packages/` and apps in `apps/`, managed by pnpm, npm or Yarn workspaces and a tool like Turborepo.
- If shared packages are TypeScript source, list them in `transpilePackages`.
- Set `outputFileTracingRoot` to the monorepo root so standalone builds include files from other packages.
- For Turbopack, set `turbopack.root` if Next.js can't detect the workspace root.

```ts
import path from "node:path";

const nextConfig = {
  transpilePackages: ["@acme/ui"],
  outputFileTracingRoot: path.join(__dirname, "../../"),
  turbopack: {
    root: path.join(__dirname, "../../"),
  },
};
```

## 342: What is output file tracing?

During `next build`, Next.js uses `@vercel/nft` to find exactly which files each route needs at runtime, including files from `node_modules`. It writes `.nft.json` files with these lists. This is how `output: 'standalone'` can copy only the needed files.

If a file is loaded in a way the tracer can't see (like a dynamic `fs.readFile` path), add it manually:

```ts
const nextConfig = {
  outputFileTracingIncludes: {
    "/api/report": ["./templates/**/*"],
  },
  outputFileTracingExcludes: {
    "*": ["node_modules/@swc/core-linux-x64-gnu"],
  },
};
```

## 343: How does Turbopack's file system cache work?

Turbopack can save its compile results to disk, so restarting `next dev` doesn't redo all the work. In Next.js 16 this was released as beta with a flag, and later versions turn it on by default for `next dev`.

```ts
const nextConfig = {
  experimental: {
    turbopackFileSystemCacheForDev: true,
  },
};
```

This mainly helps large projects where restarting the dev server used to take a long time.

## 344: Why might code that works with webpack fail with Turbopack?

- Custom `webpack()` config and webpack plugins are not supported.
- Some webpack loaders don't work, or need to be set up in `turbopack.rules`.
- Some magic comments and webpack-specific features (like `require.context` details or `module.hot`) behave differently.
- Sass features like `:import`/`:export` across files or custom `importer` functions may not be supported.

The fix is usually to move config to `turbopack` options, swap the plugin for a supported one, or keep using `--webpack` for now.

## 345: How do you debug why a route became dynamic?

- Look at the `next build` output to see which routes are marked `ƒ`.
- Set `export const dynamic = 'error'` on the route. The build then fails with the exact reason (for example, `cookies` was used).
- With Cache Components, the dev overlay and build errors tell you which component accessed uncached data outside a Suspense boundary.
- Check imports: a shared helper that calls `headers()` makes every route that uses it dynamic.

## 346: Why is `searchParams` on a page a common cause of dynamic rendering, and how do you avoid it?

`searchParams` are only known at request time, so reading them on the server makes that part of the page dynamic. To keep the page static:

- Read them in a Client Component with `useSearchParams` and wrap it in `<Suspense>`. The server renders a static shell, and the filtered UI is done in the browser.
- With Cache Components, read `searchParams` in a small component inside `<Suspense>`, so only that part is dynamic.
- Move data that depends on the param into a path segment that you can prerender (for example `/products/shoes` instead of `/products?category=shoes`).

## 347: Explain how `generateStaticParams` works with Cache Components.

With Cache Components, `generateStaticParams` still tells Next.js which param values to prerender. For each value, Next.js builds a static shell. Params that aren't listed are rendered on demand. Inside the page, `await params` for a known value is treated as static, so the content can go into the shell.

Without `generateStaticParams`, reading `params` is treated as request-time data and must be inside `<Suspense>` or cached with `"use cache"`.

## 348: What is the difference between the `revalidatePath` `'page'` and `'layout'` types?

- `'page'`: invalidates only the page that matches. It does not affect layouts or other pages.
- `'layout'`: invalidates the layout at that path and every page below it.

```ts
revalidatePath("/blog/[slug]", "page"); // every blog post page
revalidatePath("/blog", "layout"); // /blog and everything under it
```

When you pass a dynamic pattern like `/blog/[slug]`, the type is required.

## 349: When does `revalidatePath` in a Server Action update the current page instantly?

When you call `revalidatePath` (or `updateTag`, `revalidateTag`, `refresh`) in a Server Action, the response includes a new RSC payload for the current page. So the user sees the new data right after the action, without a second request. Other pages are only refreshed the next time they are visited.

If you call `revalidatePath` from a Route Handler, there is no client to update, so the change shows on the next request.

## 350: How do you invalidate the client Router Cache?

- `router.refresh()` from the client
- `revalidatePath`, `revalidateTag`, `updateTag` or `refresh()` in a Server Action
- `cookies().set()` or `cookies().delete()` in a Server Action (because cookie changes could affect rendering)
- A full page reload

Calling `revalidatePath` in a Route Handler does not clear the Router Cache of browsers right away.

## 351: What are `staleTimes`?

`staleTimes` (experimental) sets how long the client Router Cache reuses prefetched or visited pages before asking the server again.

```ts
const nextConfig = {
  experimental: {
    staleTimes: {
      dynamic: 30, // seconds, default 0
      static: 180, // seconds, default 300
    },
  },
};
```

Since Next.js 15, the default `dynamic` value is 0, so pages are fetched fresh on each navigation. Back and forward navigation still reuse the cache. Layouts and `loading.tsx` are always reused for some time.

## 352: How would you build an e-commerce product page with fast static content and personalized parts?

Use Cache Components (PPR):

```tsx
// app/product/[id]/page.tsx
import { Suspense } from "react";
import { cookies } from "next/headers";
import { cacheLife, cacheTag } from "next/cache";

export default async function ProductPage({
  params,
}: PageProps<"/product/[id]">) {
  const { id } = await params;
  return (
    <>
      <ProductDetails id={id} />
      <Suspense fallback={<p>Loading price...</p>}>
        <PersonalizedPrice id={id} />
      </Suspense>
      <Suspense fallback={<p>Loading recommendations...</p>}>
        <Recommendations id={id} />
      </Suspense>
    </>
  );
}

async function ProductDetails({ id }: { id: string }) {
  "use cache";
  cacheLife("days");
  cacheTag(`product-${id}`);
  const product = await getProduct(id);
  return <h1>{product.name}</h1>;
}

async function PersonalizedPrice({ id }: { id: string }) {
  const session = (await cookies()).get("session")?.value;
  const price = await getPriceForUser(id, session);
  return <p>{price}</p>;
}
```

The product details are in the static shell. The price and recommendations stream in per request. When the product changes, the admin action calls ``updateTag(`product-${id}`)``.

## 353: How do you avoid passing large data to Client Components?

Everything passed as a prop to a Client Component is serialized into the RSC payload and also into the HTML for hydration, so it is sent twice on the first load.

- Pass only what the client needs, not whole records.
- Do filtering, sorting and formatting on the server.
- Render static parts (like long text or tables) in Server Components and only make the interactive pieces client components.
- Paginate long lists.

## 354: How do you make a list of items interactive without making the whole list a Client Component?

Render the list in a Server Component and only make the button a Client Component.

```tsx
// Server Component
export default async function TodoList() {
  const todos = await getTodos();
  return (
    <ul>
      {todos.map((todo) => (
        <li key={todo.id}>
          {todo.title}
          <DeleteButton id={todo.id} />
        </li>
      ))}
    </ul>
  );
}
```

```tsx
// delete-button.tsx
"use client";

import { deleteTodo } from "./actions";

export function DeleteButton({ id }: { id: string }) {
  return <button onClick={() => deleteTodo(id)}>Delete</button>;
}
```

## 355: How do you render a Server Component inside a Client Component that depends on client state?

You can't make the Server Component react to client state directly, because it already ran on the server. Options:

- Pass the Server Component as `children` and let the Client Component show or hide it.
- Put the state in the URL (search params). The server renders based on the URL.
- Call a Server Action that returns data and render it in the client.
- Render several Server Component variants and pass them as props, then pick one on the client.

```tsx
<Tabs
  overview={<Overview />} // Server Component
  settings={<Settings />} // Server Component
/>
```

## 356: How does Suspense on the server work together with hydration?

React streams HTML in chunks. Each Suspense boundary that is not ready gets a fallback in the HTML. When the data arrives, React sends the real HTML in a hidden `<div>` plus a small inline script that swaps it into place. This happens before React and your JavaScript load.

React also hydrates in parts (selective hydration). It hydrates boundaries as their code and HTML arrive, and gives priority to the part the user clicks on.

## 357: How do you handle errors inside a streamed Suspense boundary?

Put an error boundary near it. In the App Router you can add an `error.tsx` to the segment, or use a client error boundary around a specific component.

```tsx
<ErrorBoundary fallback={<p>Could not load reviews</p>}>
  <Suspense fallback={<p>Loading reviews...</p>}>
    <Reviews />
  </Suspense>
</ErrorBoundary>
```

`ErrorBoundary` here is a Client Component (you can use `react-error-boundary`). If a streamed part throws and there is no boundary around it, the nearest `error.tsx` replaces that whole segment.

## 358: What is `unstable_rethrow` and when do you need it?

It rethrows errors that Next.js uses internally for control flow, like those from `redirect()`, `notFound()`, `forbidden()`, and dynamic API bailouts during prerendering. If you catch all errors in a `try/catch`, call it first.

```ts
import { unstable_rethrow } from 'next/navigation'

export default async function Page() {
  try {
    const res = await fetch('https://api.example.com/data')
    if (res.status === 404) notFound()
    return <Data data={await res.json()} />
  } catch (err) {
    unstable_rethrow(err)
    return <p>Failed to load</p>
  }
}
```

## 359: How do you prevent hydration mismatches for theme or time-based UI?

- For theme: read the theme cookie on the server and render the right class on `<html>`. Or use a small inline script that sets the class before React hydrates (libraries like `next-themes` do this), and add `suppressHydrationWarning` to `<html>`.
- For times: format dates on the server with a fixed time zone, or render them only on the client after mount.
- For random IDs: use React's `useId`.

```tsx
<html lang="en" suppressHydrationWarning>
```

`suppressHydrationWarning` only applies one level deep, so use it carefully.

## 360: How do you handle `window` and `localStorage` safely in Client Components?

Client Components still render on the server for the first HTML, where `window` doesn't exist. Access browser APIs only inside `useEffect` or event handlers.

```tsx
"use client";

import { useEffect, useState } from "react";

export function LastVisit() {
  const [last, setLast] = useState<string | null>(null);

  useEffect(() => {
    setLast(localStorage.getItem("lastVisit"));
    localStorage.setItem("lastVisit", new Date().toISOString());
  }, []);

  return <p>Last visit: {last ?? "first time"}</p>;
}
```

For values you need to subscribe to, use `useSyncExternalStore` with a `getServerSnapshot`.

## 361: How do you design a Next.js app to reduce JavaScript sent to the browser?

- Keep most components as Server Components.
- Push `"use client"` down to small interactive leaves.
- Avoid large libraries in Client Components (do date formatting, Markdown parsing and syntax highlighting on the server).
- Use `next/dynamic` for heavy client-only parts like charts or editors.
- Use `optimizePackageImports` for libraries with many exports.
- Check bundles with the bundle analyzer.

## 362: How does Next.js handle `fetch` request deduplication vs caching in Route Handlers?

Request memoization is a React feature for the component tree. It doesn't apply in Route Handlers, because they are not part of the React tree. Two identical `fetch` calls in one Route Handler make two requests. The Data Cache (`force-cache`, `revalidate`) still works there.

## 363: How do you cache data from a database query when not using Cache Components?

Use `unstable_cache` (the older API) or move to Cache Components with `"use cache"`.

```ts
import { unstable_cache } from "next/cache";

export const getCachedUser = unstable_cache(
  async (id: string) => db.user.findUnique({ where: { id } }),
  ["user"],
  { revalidate: 3600, tags: ["users"] },
);
```

`unstable_cache` is replaced by `"use cache"` in new code, but you'll see it in many existing apps.

## 364: What are the trade-offs of using Cache Components?

Pros:

- Clear, explicit caching: nothing is cached unless you say so.
- Static shell plus streaming for every route, even routes with personal data.
- Fine-grained control per component and function.

Cons:

- You must think about every data access: cache it or wrap it in `<Suspense>`.
- Old segment config options (`dynamic`, `revalidate`, `fetchCache`) don't work and must be migrated.
- Some patterns, like `Date.now()` during render, need changes.
- The default in-memory cache handler is per instance, so self-hosting at scale needs a shared handler.

## 365: How do you migrate `export const revalidate = 3600` to Cache Components?

Replace the segment config with `"use cache"` and `cacheLife`.

```tsx
// before
export const revalidate = 3600;

export default async function Page() {
  const posts = await getPosts();
  return <PostList posts={posts} />;
}
```

```tsx
// after
import { cacheLife } from "next/cache";

export default async function Page() {
  "use cache";
  cacheLife("hours");
  const posts = await getPosts();
  return <PostList posts={posts} />;
}
```

And `export const dynamic = 'force-dynamic'` is usually just removed, because everything is dynamic by default with Cache Components. Wrap the dynamic parts in `<Suspense>`.

## 366: How does `revalidateTag` with a profile differ from immediate expiry?

`revalidateTag('posts', 'max')` marks entries as stale. The next request gets the stale content right away and triggers a refresh in the background. The one after that gets fresh content. This keeps pages fast after a CMS update.

If you need the cache to expire right away from a Route Handler (for example a webhook that must reflect a change immediately), use `revalidateTag(tag, { expire: 0 })`. In Server Actions, use `updateTag` instead.

## 367: How do you implement optimistic UI with rollback using `useOptimistic` and Server Actions?

`useOptimistic` resets to the server state when the transition finishes. If the action throws, the optimistic value is dropped automatically, because the real state didn't change.

```tsx
"use client";

import { useOptimistic, startTransition } from "react";
import { toggleLike } from "./actions";

export function Like({ liked, count }: { liked: boolean; count: number }) {
  const [state, setOptimistic] = useOptimistic({ liked, count });

  function onClick() {
    startTransition(async () => {
      setOptimistic({
        liked: !state.liked,
        count: state.count + (state.liked ? -1 : 1),
      });
      try {
        await toggleLike();
      } catch {
        alert("Could not save your like");
      }
    });
  }

  return (
    <button onClick={onClick}>
      {state.liked ? "Unlike" : "Like"} ({state.count})
    </button>
  );
}
```

The Server Action should call `updateTag` or `revalidatePath`, so the new server state arrives in the same response.

## 368: How do you implement infinite scroll with Server Components?

One approach is to render the first page on the server and load more with a Server Action that returns data (or JSX) to a Client Component.

```ts
// actions.ts
"use server";

export async function loadMore(cursor: string) {
  return db.post.findMany({
    take: 20,
    skip: 1,
    cursor: { id: cursor },
    orderBy: { id: "asc" },
  });
}
```

```tsx
"use client";

import { useState } from "react";
import { loadMore } from "./actions";

export function PostFeed({ initial }: { initial: Post[] }) {
  const [posts, setPosts] = useState(initial);

  async function onLoadMore() {
    const next = await loadMore(posts[posts.length - 1].id);
    setPosts((p) => [...p, ...next]);
  }

  return (
    <>
      {posts.map((p) => (
        <PostCard key={p.id} post={p} />
      ))}
      <button onClick={onLoadMore}>Load more</button>
    </>
  );
}
```

Because Server Actions run one after another, for heavy read traffic a cached `GET` Route Handler with a client fetching library can be a better choice.

## 369: Can Server Actions return JSX?

Yes. A Server Function can return React elements, including Server Components, and the client can render them. This is sometimes used to stream UI from the server (for example in AI chat apps). But it is less common and harder to cache. For most cases, return plain data and render it on the client, or revalidate and let the page re-render.

## 370: How do you keep a Server Action from running for unauthorized users who call it directly?

Put the check inside the action itself, not only in the page that renders the form. Anyone can call the action with a crafted POST request.

```ts
"use server";

import { verifySession } from "@/lib/dal";
import { z } from "zod";

const Input = z.object({
  projectId: z.string().uuid(),
  name: z.string().min(1).max(100),
});

export async function renameProject(raw: unknown) {
  const { userId } = await verifySession();
  const { projectId, name } = Input.parse(raw);

  const project = await db.project.findUnique({ where: { id: projectId } });
  if (!project || project.ownerId !== userId) {
    throw new Error("Not allowed");
  }

  await db.project.update({ where: { id: projectId }, data: { name } });
}
```

Libraries like `next-safe-action` help apply validation and auth to every action in the same way.

## 371: How do you rate limit Server Actions or Route Handlers?

Next.js doesn't have built-in rate limiting. Common options:

- A rate limiter backed by Redis (like `@upstash/ratelimit`) keyed by user ID or IP address.
- A firewall or WAF at your hosting provider or CDN.
- Checks in Proxy for broad limits.

```ts
"use server";

import { headers } from "next/headers";

export async function sendMessage(formData: FormData) {
  const ip = (await headers()).get("x-forwarded-for") ?? "unknown";
  const { success } = await ratelimit.limit(ip);
  if (!success) return { error: "Too many requests" };
  // ...
}
```

Only trust `x-forwarded-for` when it is set by your own proxy.

## 372: What happens if a Server Component throws during prerendering at build time?

The build fails for that route, unless the error is one Next.js uses for control flow (like a dynamic API bailout). For data that is not available at build time (for example, a database not reachable in CI), you can make the route dynamic, or with Cache Components move the access behind `connection()` and `<Suspense>`.

## 373: How do you handle a database that isn't reachable during `next build`?

Options:

- Make the routes that need it dynamic, so they don't run at build time.
- Return an empty list from `generateStaticParams` and let pages render on demand (without Cache Components).
- With Cache Components, put data access behind `await connection()` in a Suspense boundary.
- Provide build-time access to a read replica if you want prerendering.

Also be careful with module-level code: a database client that connects on import can fail the build even if no page uses it.

## 374: How do you share code between Server and Client Components safely?

- Pure helpers (formatting, validation schemas, types, constants) can be imported by both.
- Code that uses secrets or server APIs should import `server-only`.
- Code that uses browser APIs should import `client-only` or live in a `"use client"` file.
- Zod schemas are a good example of shared code: validate on the client for UX and on the server for safety.

## 375: Why can't you use a Context Provider directly in a Server Component layout, and what is the pattern?

React Context needs state on the client, and Server Components don't support `createContext`. The pattern is to create a Client Component provider and render it in the layout. Pass data from the server as props if needed.

```tsx
// app/layout.tsx
import { SessionProvider } from "./session-provider"; // 'use client'

export default async function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const session = await getSessionSummary(); // only safe fields
  return (
    <html lang="en">
      <body>
        <SessionProvider session={session}>{children}</SessionProvider>
      </body>
    </html>
  );
}
```

Render the provider as deep as possible, so Next.js can still optimize static parts above it. Note that reading the session here makes the root layout dynamic.

## 376: How does Next.js decide what to prefetch for a dynamic route without `loading.tsx`?

With the default `prefetch` setting, Next.js prefetches a dynamic route only down to the nearest `loading.tsx` boundary. If there is no `loading.tsx` in the path, very little is prefetched, and the click has to wait for the server before anything changes. Adding a `loading.tsx` (or using Cache Components, where the static shell can be prefetched) makes navigations to dynamic routes feel instant.

## 377: How do you build a route that renders differently for logged-in and logged-out users but stays fast?

With Cache Components:

- Keep the shared parts (header, marketing content, product info) in the static shell or in `"use cache"` components.
- Put the user-specific parts (user menu, cart, "recommended for you") in components that read `cookies()` inside `<Suspense>`.

Without Cache Components, a common pattern is to keep the page static and load the user parts on the client (for example, a Client Component that calls `/api/me`), or use Proxy to rewrite logged-in users to a separate dynamic route.

## 378: How do you implement A/B testing without making pages dynamic?

Use Proxy to assign a variant (store it in a cookie) and rewrite to a prerendered variant route.

```ts
// proxy.ts
import { NextResponse, type NextRequest } from "next/server";

export function proxy(request: NextRequest) {
  if (request.nextUrl.pathname !== "/") return NextResponse.next();

  let variant = request.cookies.get("ab-home")?.value;
  if (!variant) variant = Math.random() < 0.5 ? "a" : "b";

  const url = request.nextUrl.clone();
  url.pathname = `/home/${variant}`;
  const res = NextResponse.rewrite(url);
  res.cookies.set("ab-home", variant, { maxAge: 60 * 60 * 24 * 30 });
  return res;
}
```

```tsx
// app/home/[variant]/page.tsx
export function generateStaticParams() {
  return [{ variant: "a" }, { variant: "b" }];
}
```

Both variants are static, and the user stays on `/`.

## 379: How do you make `generateMetadata` not slow down the page?

- Since 15.2, metadata streams for normal browsers, so it doesn't block the first paint.
- Share data with the page through memoized functions so it isn't fetched twice.
- Cache the data with `"use cache"` when possible.
- For bots listed in `htmlLimitedBots`, metadata still blocks, so keep it reasonably fast.

## 380: How do you handle `notFound()` inside `generateMetadata`?

You can call `notFound()` there. It stops rendering and shows the not-found UI. It is common to do the same check in both the page and `generateMetadata`:

```tsx
export async function generateMetadata({ params }: PageProps<"/blog/[slug]">) {
  const post = await getPost((await params).slug);
  if (!post) notFound();
  return { title: post.title };
}
```

## 381: How would you implement role-based access control (RBAC) in Next.js?

1. Store the user's role in the session (or load it from the database in the DAL).
2. Write helper functions like `requireRole('admin')` that redirect or throw.
3. Use them in pages, Server Actions and Route Handlers.
4. Use Proxy only for quick redirects based on the session cookie.
5. Hide UI the user can't use, but never rely on hidden UI for security.

```ts
// lib/auth.ts
import "server-only";
import { forbidden } from "next/navigation";

export async function requireRole(role: "admin" | "editor") {
  const session = await verifySession();
  if (!session.roles.includes(role)) {
    forbidden();
  }
  return session;
}
```

## 382: How do you store sessions: stateless cookies vs database sessions?

- **Stateless (JWT in an encrypted cookie)**: no database lookup per request, easy to scale. Harder to revoke a session early, and the cookie size is limited (~4 KB).
- **Database sessions**: the cookie holds only a random session ID. Easy to revoke and list sessions, but each request needs a lookup (can be cached).

For both, set cookies with `httpOnly`, `secure`, `sameSite: 'lax'`, and a reasonable expiry.

```ts
import { SignJWT, jwtVerify } from "jose";

const key = new TextEncoder().encode(process.env.SESSION_SECRET);

export async function encrypt(payload: { userId: string; expiresAt: Date }) {
  return new SignJWT(payload)
    .setProtectedHeader({ alg: "HS256" })
    .setIssuedAt()
    .setExpirationTime("7d")
    .sign(key);
}

export async function decrypt(token: string | undefined) {
  if (!token) return null;
  try {
    const { payload } = await jwtVerify(token, key, { algorithms: ["HS256"] });
    return payload;
  } catch {
    return null;
  }
}
```

## 383: How do you refresh a session cookie on activity?

Update the cookie expiry in Proxy or in a Server Action. Server Components can't set cookies.

```ts
// proxy.ts
export async function proxy(request: NextRequest) {
  const res = NextResponse.next();
  const session = request.cookies.get("session")?.value;
  const payload = await decrypt(session);

  if (payload) {
    res.cookies.set("session", session!, {
      httpOnly: true,
      secure: true,
      sameSite: "lax",
      expires: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000),
      path: "/",
    });
  }
  return res;
}
```

## 384: What are the risks of putting heavy logic in Proxy?

- It runs before every matching request, including prefetches, so extra latency multiplies.
- Errors there break every route it matches.
- It can't stream or render UI.
- It may run in a different region from your database, which adds latency.
- It is easy to get the matcher wrong and skip checks for some paths.

Keep Proxy for rewrites, redirects, headers and cookie checks. Do the real work in pages, actions and handlers.

## 385: How do you return a JSON error from Proxy?

```ts
// proxy.ts
import { type NextRequest } from "next/server";

export function proxy(request: NextRequest) {
  if (!request.headers.get("authorization")) {
    return Response.json({ error: "Authentication required" }, { status: 401 });
  }
}

export const config = { matcher: "/api/private/:path*" };
```

If Proxy returns nothing, the request continues as normal.

## 386: How do you use `waitUntil` in Proxy?

The second argument of the proxy function is a `NextFetchEvent`. `event.waitUntil` keeps the function alive until a Promise settles, without delaying the response.

```ts
import {
  NextResponse,
  type NextFetchEvent,
  type NextRequest,
} from "next/server";

export function proxy(request: NextRequest, event: NextFetchEvent) {
  event.waitUntil(
    fetch("https://analytics.example.com", {
      method: "POST",
      body: JSON.stringify({ path: request.nextUrl.pathname }),
    }),
  );
  return NextResponse.next();
}
```

You can also use `after()` for the same purpose.

## 387: What is `skipProxyUrlNormalize` and `skipTrailingSlashRedirect`?

- `skipTrailingSlashRedirect`: turns off the automatic redirect that adds or removes a trailing slash, so you can handle it yourself in Proxy.
- `skipProxyUrlNormalize` (was `skipMiddlewareUrlNormalize`): stops Next.js from normalizing the URL before Proxy sees it. For example, data requests for `/_next/data/...` stay as they are, so you can see the raw URL.

Both are advanced options for custom routing setups.

## 388: How does Next.js decide the order of routing logic?

For an incoming request, Next.js checks in this order:

1. `headers` from `next.config`
2. `redirects` from `next.config`
3. Proxy (rewrites, redirects, responses)
4. `beforeFiles` rewrites
5. Static files (`public`, `_next/static`) and pages
6. `afterFiles` rewrites
7. Dynamic routes
8. `fallback` rewrites

Knowing this helps when a rewrite or redirect doesn't seem to apply.

## 389: What are `beforeFiles`, `afterFiles` and `fallback` rewrites?

`rewrites()` can return an object with three arrays:

```ts
async rewrites() {
  return {
    beforeFiles: [
      // checked before pages and public files, can override them
      { source: '/some-page', destination: '/somewhere-else', has: [{ type: 'query', key: 'overrideMe' }] },
    ],
    afterFiles: [
      // checked after pages and public files, before dynamic routes
      { source: '/non-existent', destination: '/somewhere-else' },
    ],
    fallback: [
      // checked after everything, a good way to proxy to an old app
      { source: '/:path*', destination: 'https://old.example.com/:path*' },
    ],
  }
}
```

The `fallback` pattern is useful for migrating from another app one page at a time.

## 390: How does `has` / `missing` matching work in redirects and rewrites?

You can add conditions on headers, cookies, query params or host.

```ts
async redirects() {
  return [
    {
      source: '/dashboard',
      missing: [{ type: 'cookie', key: 'session' }],
      destination: '/login',
      permanent: false,
    },
    {
      source: '/:path*',
      has: [{ type: 'host', value: 'old-domain.com' }],
      destination: 'https://new-domain.com/:path*',
      permanent: true,
    },
  ]
}
```

## 391: How do you handle large static sites with thousands of pages and keep build times low?

- Prerender only popular pages in `generateStaticParams` and render the rest on demand.
- Cache data sources so builds don't call slow APIs repeatedly.
- Use Turbopack builds and its file system cache.
- Split the site into Multi-Zones if parts are owned by different teams.
- Use on-demand revalidation instead of rebuilding for content changes.

## 392: How do you generate static pages in parallel faster during build?

Next.js uses several worker processes during the static generation phase. You can tune it:

```ts
const nextConfig = {
  experimental: {
    cpus: 4,
    staticGenerationMaxConcurrency: 8,
    staticGenerationMinPagesPerWorker: 25,
    staticGenerationRetryCount: 1,
  },
};
```

Also make sure data fetching in `generateStaticParams` and pages is efficient, for example by fetching a list once and reusing it.

## 393: How do you use `generateStaticParams` with `fetch` deduplication during build?

During the build, `fetch` requests with the same URL and options in `generateStaticParams` and pages are memoized within each worker. So fetching the list of posts in `generateStaticParams` and again in the page doesn't double the requests in the same process. For non-`fetch` data, use `"use cache"` or React `cache`.

## 394: What is the static shell and how is it served?

The static shell is the HTML produced at build time for a route that has dynamic parts. It contains everything outside dynamic Suspense boundaries, with fallbacks in place of the dynamic parts. When a request comes in, the shell is sent right away (it can come from a CDN), and the server continues the same response with the dynamic parts as they render. The browser doesn't need a second request.

## 395: How does Next.js 16 resume a prerendered shell at request time?

Next.js uses React's `prerender` and `resume` APIs. At build time, React renders the static parts and saves "postponed" state that describes the holes. At request time, the server loads that state and calls `resume`, which renders only the dynamic parts and streams them after the static shell. This avoids rendering the static parts again for each request.

## 396: How do you serve a prerendered shell from a CDN while the dynamic parts come from your server?

On platforms that support it (like Vercel), the CDN sends the shell right away and the platform streams the rest from the function in the same response. When self-hosting, `next start` does both from one server. To use a third-party CDN for the shell, you need an adapter or platform that can combine the cached shell with the dynamic stream, which is part of what the Build Adapters API is meant to support.

## 397: Explain the difference between `prefetch` and `preload` for images and links.

- `Link` prefetch fetches route data (RSC payload) for future navigations.
- The `preload` prop on `next/image` adds a `<link rel="preload">` in the `<head>` so the browser starts downloading that image early on the current page.
- `ReactDOM.preload()` (from `react-dom`) lets you preload any resource (fonts, scripts, styles) from components.

```tsx
import { preload } from "react-dom";

export function HeroSection() {
  preload("/fonts/display.woff2", {
    as: "font",
    type: "font/woff2",
    crossOrigin: "anonymous",
  });
  return <h1 className="display">Welcome</h1>;
}
```

## 398: How do you reduce Largest Contentful Paint (LCP) in a Next.js app?

- Use `next/image` with `preload` (or `fetchPriority="high"`) for the LCP image.
- Set correct `sizes` so the browser doesn't download a too-big image.
- Self-host fonts with `next/font` and use `display: 'swap'`.
- Keep the LCP element in the static shell, not behind a slow Suspense boundary.
- Avoid render-blocking third-party scripts; load them with `afterInteractive` or `lazyOnload`.
- Use a CDN and caching so the HTML arrives fast.

## 399: How do you reduce Interaction to Next Paint (INP)?

- Send less JavaScript: more Server Components, smaller Client Components.
- Split heavy client code with `next/dynamic`.
- Use `startTransition` for non-urgent updates so the UI responds first.
- Avoid long tasks in event handlers. Move work to the server (Server Actions) or a web worker.
- Turn on the React Compiler to avoid extra re-renders.
- Load third-party scripts late or in a worker.

## 400: How do you avoid Cumulative Layout Shift (CLS)?

- Always give images a size (`width`/`height`, or `fill` with a sized container).
- Use `next/font` so the fallback font has matching size settings.
- Reserve space for content that loads later (ads, embeds, Suspense fallbacks should be the same size as the content).
- Avoid inserting content above existing content after load.

## 401: How does `next/font` avoid layout shift technically?

It generates a fallback font face using `size-adjust`, `ascent-override`, `descent-override` and `line-gap-override` so the fallback (like Arial) takes up the same space as the real font. When the real font loads, the text doesn't move. This is the `adjustFontFallback` option, which is on by default.

## 402: What happens to `next/font` font files at build time?

For Google fonts, Next.js downloads the font files and CSS during the build and serves them from `/_next/static/media`. The files are named with hashes and cached for a long time. Only the subsets and weights you ask for are included, and for variable fonts one file covers all weights. No request goes to Google at runtime.

## 403: How does the image optimizer work when self-hosting?

When a browser requests `/_next/image?url=...&w=...&q=...`, the Next.js server:

1. Checks that the URL matches `remotePatterns` or `localPatterns`, and that width and quality are allowed.
2. Looks in its cache (`.next/cache/images`).
3. If missing, fetches the original, resizes and converts it with `sharp` to AVIF or WebP based on the `Accept` header.
4. Stores the result and serves it with cache headers based on `minimumCacheTTL` or the upstream headers.

When self-hosting at scale, this uses CPU, so put a CDN in front or use an external image service with a custom loader.

## 404: Why did Next.js 16 restrict image qualities and local IPs?

- **Qualities**: each allowed quality value creates a new set of image files. Allowing any quality lets attackers fill your cache and use CPU by requesting many variations. Limiting to `[75]` by default reduces this.
- **Local IPs**: fetching images from private network addresses could be used for server-side request forgery (SSRF), letting an attacker reach internal services through your image optimizer. It is blocked by default now.

## 405: How do you serve AVIF images?

```ts
const nextConfig = {
  images: {
    formats: ["image/avif", "image/webp"],
  },
};
```

AVIF files are smaller, but take longer to encode. The first request for each size is slower, then it is cached.

## 406: How do you handle images in a static export?

The default loader needs a server. For `output: 'export'`:

- Set `images.unoptimized: true` to serve images as they are, or
- Use a custom `loaderFile` that points to an image CDN.

```ts
const nextConfig = {
  output: "export",
  images: {
    loader: "custom",
    loaderFile: "./image-loader.ts",
  },
};
```

## 407: What is the difference between `unoptimized` on a single image and the global setting?

`<Image unoptimized />` skips the optimizer for that image only, serving the source as is. This is good for small icons, SVGs or GIFs. `images.unoptimized: true` in the config turns off optimization for all images, often used for static exports.

## 408: Why does `next/image` not optimize SVGs by default?

SVG is a vector format, so resizing gives no benefit, and SVG files can contain scripts. The default loader serves them as they are. If you want the optimizer to serve them, you must set `dangerouslyAllowSVG: true` together with a strict `contentSecurityPolicy` and `contentDispositionType: 'attachment'`.

## 409: How do you handle authentication for API clients like mobile apps?

Server Actions are tied to your web UI and are not meant to be used as a public API. For mobile apps:

- Create Route Handlers under `/api` with versioned paths.
- Use token-based auth (bearer tokens / OAuth) instead of cookies.
- Validate tokens in the handler (or a shared helper), and apply rate limits.
- Share the business logic between Server Actions and Route Handlers through the DAL.

## 410: How do you share business logic between Server Actions and Route Handlers?

Put the logic in plain server-only functions (services or a DAL). Server Actions and Route Handlers become thin wrappers that handle input format, auth and response.

```ts
// lib/services/orders.ts
import "server-only";

export async function createOrder(userId: string, input: OrderInput) {
  // validation, database writes, emails
}
```

```ts
// app/actions/orders.ts
"use server";
export async function createOrderAction(input: OrderInput) {
  const { userId } = await verifySession();
  return createOrder(userId, input);
}
```

```ts
// app/api/v1/orders/route.ts
export async function POST(req: Request) {
  const { userId } = await verifyBearerToken(req);
  const order = await createOrder(userId, await req.json());
  return Response.json(order, { status: 201 });
}
```

## 411: How do you handle long-running tasks that exceed request time limits?

Don't run them inside the request. Options:

- Put the job in a queue (like SQS, BullMQ, Inngest, QStash or Trigger.dev) and return right away.
- Use `after()` for short follow-up work that can finish after the response.
- Show the progress with polling or Server-Sent Events.
- On platforms with limits, raise `maxDuration` only when it is really needed.

## 412: How do you implement Server-Sent Events (SSE) with a Route Handler?

```ts
// app/api/events/route.ts
export async function GET(request: Request) {
  const encoder = new TextEncoder();

  const stream = new ReadableStream({
    start(controller) {
      const send = (data: unknown) =>
        controller.enqueue(encoder.encode(`data: ${JSON.stringify(data)}\n\n`));

      const interval = setInterval(() => send({ time: Date.now() }), 1000);

      request.signal.addEventListener("abort", () => {
        clearInterval(interval);
        controller.close();
      });
    },
  });

  return new Response(stream, {
    headers: {
      "Content-Type": "text/event-stream",
      "Cache-Control": "no-cache, no-transform",
      Connection: "keep-alive",
    },
  });
}
```

On the client, use `new EventSource('/api/events')`. Serverless platforms may limit how long the connection can stay open.

## 413: Why doesn't Next.js support WebSockets in Route Handlers?

Route Handlers follow the request/response model with Web `Request` and `Response`. WebSockets need a long-lived, two-way connection with a protocol upgrade, which doesn't fit that model and doesn't work on most serverless platforms. Use a separate WebSocket server, a custom server, or a hosted service (like Pusher, Ably, Liveblocks or Supabase Realtime).

## 414: What is a custom server and when should you avoid it?

A custom server lets you start Next.js from your own Node.js server (for example Express), so you can add WebSockets or custom routing.

```ts
// server.ts
import { createServer } from "node:http";
import next from "next";

const app = next({ dev: process.env.NODE_ENV !== "production" });
const handle = app.getRequestHandler();

app.prepare().then(() => {
  createServer((req, res) => handle(req, res)).listen(3000);
});
```

Avoid it unless you really need it: you lose some optimizations, your server replaces the `server.js` that `output: 'standalone'` creates, and you can't deploy it to Vercel. Most needs are covered by Route Handlers and Proxy.

## 415: How do you handle graceful shutdown in a self-hosted Next.js app?

`next start` and the standalone server listen for `SIGTERM` and `SIGINT` and finish in-flight requests before exiting. In Docker or Kubernetes:

- Make sure the signal reaches the Node.js process (use `CMD ["node", "server.js"]`, not a shell form).
- Give the container enough termination grace period.
- Close database pools in a `process.on('SIGTERM')` handler set up in `instrumentation.ts` if needed.

## 416: How do you set `Cache-Control` headers when self-hosting behind a CDN?

Next.js sets headers based on the route:

- Static pages: `s-maxage` with `stale-while-revalidate` based on the revalidate time.
- Dynamic pages: `private, no-cache, no-store, max-age=0, must-revalidate`.
- `/_next/static` files: `public, max-age=31536000, immutable`.

You can't override `Cache-Control` for pages in `next.config` headers, because Next.js controls it to keep caching correct. You can set it in Route Handlers. Make sure your CDN respects `s-maxage` and caches by the `RSC` and related `Vary` headers.

## 417: Why must a CDN respect the `Vary` header for Next.js routes?

The same URL can return HTML (for a full load) or an RSC payload (for client navigation), based on request headers like `RSC` and `Next-Router-Prefetch`. Next.js sends a `Vary` header with these. If a CDN ignores it, it might serve an RSC payload to a browser asking for HTML (users see raw data) or HTML to the router (navigation breaks).

## 418: How do you run Next.js on serverless platforms other than Vercel?

- **Netlify**: has a Next.js runtime that handles SSR, ISR, image optimization and Proxy.
- **Cloudflare**: the OpenNext adapter (`@opennextjs/cloudflare`) runs Next.js on Cloudflare Workers.
- **AWS**: OpenNext / SST deploy to Lambda + CloudFront + S3.
- **Docker**: any platform that runs containers (Cloud Run, Fly.io, Railway, ECS, Kubernetes).

Feature support depends on the adapter. Build Adapters are meant to make this more consistent.

## 419: How do you migrate from `getServerSideProps` with `context.res.setHeader` caching to the App Router?

In the Pages Router, people often set `Cache-Control` in `getServerSideProps` for CDN caching. In the App Router you can't set headers from a page. Instead:

- Make the page static with revalidation (`"use cache"` + `cacheLife`, or `revalidate`), and Next.js sets the cache headers for you.
- Or move the data endpoint into a Route Handler and set the headers there.

## 420: How do you handle a Pages Router `_app` global data fetch in the App Router?

`getInitialProps` in `_app` ran on every page and turned off static optimization. In the App Router:

- Fetch shared data in the root layout (it's a Server Component).
- Cache it with `"use cache"` if it is the same for everyone.
- Use React `cache` so pages can call the same function without extra requests.

## 421: How do you test Server Actions?

- Unit test the business logic by calling the underlying service functions directly with mocks for the database.
- You can also import the action and call it in a Node test environment, mocking `next/headers`, `next/cache` and `next/navigation`.
- Test the full flow (form submit, revalidation, redirect) with Playwright.

```ts
import { vi, test, expect } from "vitest";

vi.mock("next/cache", () => ({ revalidatePath: vi.fn(), updateTag: vi.fn() }));
vi.mock("@/lib/dal", () => ({ verifySession: async () => ({ userId: "u1" }) }));

import { createTodo } from "@/app/actions";

test("creates a todo", async () => {
  const fd = new FormData();
  fd.set("title", "Buy milk");
  const result = await createTodo({}, fd);
  expect(result).toEqual({});
});
```

## 422: How do you test Proxy logic?

Next.js has experimental test helpers in `next/experimental/testing/server`:

```ts
import {
  unstable_doesMiddlewareMatch,
  isRewrite,
  getRewrittenUrl,
} from "next/experimental/testing/server";
import { NextRequest } from "next/server";
import { proxy, config } from "./proxy";

test("matches dashboard", () => {
  expect(unstable_doesMiddlewareMatch({ config, url: "/dashboard" })).toBe(
    true,
  );
});

test("rewrites", async () => {
  const res = await proxy(new NextRequest("https://example.com/old"));
  expect(isRewrite(res)).toBe(true);
  expect(getRewrittenUrl(res)).toBe("https://example.com/new");
});
```

These are experimental, so names may change between versions (some helpers still use the old "middleware" name).

## 423: How do you use Playwright to test a Next.js app?

```ts
// playwright.config.ts
import { defineConfig } from "@playwright/test";

export default defineConfig({
  webServer: {
    command: "npm run build && npm run start",
    url: "http://localhost:3000",
    reuseExistingServer: !process.env.CI,
  },
  use: { baseURL: "http://localhost:3000" },
});
```

```ts
// e2e/login.spec.ts
import { test, expect } from "@playwright/test";

test("user can log in", async ({ page }) => {
  await page.goto("/login");
  await page.fill("input[name=email]", "a@b.com");
  await page.fill("input[name=password]", "secret");
  await page.click("button[type=submit]");
  await expect(page).toHaveURL("/dashboard");
});
```

Testing against the production build catches caching and prerendering issues that dev mode hides.

## 424: How do you mock external APIs used by Server Components in E2E tests?

Playwright's `page.route` only intercepts browser requests, not server-side `fetch`. Options:

- Point the app at a mock server via an environment variable (`API_URL=http://localhost:4000`).
- Use MSW in Node, started from `instrumentation.ts` when a test flag is set.
- Use Next.js's experimental test mode for Playwright (`next/experimental/testmode/playwright`) which lets tests intercept server `fetch` calls.

## 425: How does `next build` handle TypeScript errors?

`next build` runs type checking and fails on type errors. You can turn this off (not recommended) with:

```ts
const nextConfig = {
  typescript: {
    ignoreBuildErrors: true,
  },
};
```

This is sometimes used when type checking is done in a separate CI step. Since Next.js 16, the build doesn't run ESLint at all.

## 426: How do you type `params` in Route Handlers with the generated helpers?

Use `RouteContext`:

```ts
// app/api/posts/[id]/route.ts
import type { NextRequest } from "next/server";

export async function GET(
  _req: NextRequest,
  ctx: RouteContext<"/api/posts/[id]">,
) {
  const { id } = await ctx.params;
  return Response.json({ id });
}
```

Run `next typegen` in CI before `tsc` so the types exist without a full build.

## 427: What is the difference between `next dev`, `next build` and `next start` with Cache Components errors?

In `next dev`, Cache Components problems (like uncached data outside Suspense) show in the error overlay when you visit the route. In `next build`, Next.js prerenders every route and fails the build with the same errors. Some problems only appear during the build, because dev renders routes on demand. Run `next build` in CI to catch them early.

## 428: How do you use environment variables at runtime in a Docker image built once?

`NEXT_PUBLIC_` variables are baked in at build time. For values that change per environment:

- Read them on the server at request time (in dynamic code, after `await connection()`), and pass them to Client Components as props.
- Or expose them from a Route Handler that the client fetches.

```tsx
import { connection } from "next/server";

export default async function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  await connection();
  const config = { apiUrl: process.env.API_URL! };
  return (
    <html lang="en">
      <body>
        <ConfigProvider config={config}>{children}</ConfigProvider>
      </body>
    </html>
  );
}
```

The `serverRuntimeConfig` and `publicRuntimeConfig` options were removed in Next.js 16.

## 429: How do you load environment variables outside of the Next.js runtime (for example in a seed script or ORM config)?

Use `@next/env`.

```ts
// envConfig.ts
import { loadEnvConfig } from "@next/env";

const projectDir = process.cwd();
loadEnvConfig(projectDir);
```

```ts
// drizzle.config.ts
import "./envConfig";

export default {
  dbCredentials: { url: process.env.DATABASE_URL! },
};
```

This loads `.env` files in the same order as Next.js.

## 430: Why can't a Server Component be rendered inside a `"use cache"` function that reads cookies via a child?

It can, if the child is passed in as `children` or another prop (a hole), not called inside. The cached function can't run request-time APIs itself, and anything it renders directly is part of the cache entry. If a component inside the cached tree calls `cookies()`, Next.js gives an error. Pass request-dependent components in from outside instead.

## 431: How do you implement a "stale while loading" search UI with `useTransition` and the router?

Navigations started with `router.push` already run in a transition. If you wrap them in your own `startTransition`, you get an `isPending` flag and the old results stay on screen while new ones load.

```tsx
"use client";

import { useTransition } from "react";
import { useRouter } from "next/navigation";

export function Filters() {
  const router = useRouter();
  const [isPending, startTransition] = useTransition();

  return (
    <div style={{ opacity: isPending ? 0.6 : 1 }}>
      <button onClick={() => startTransition(() => router.push("?sort=price"))}>
        Sort by price
      </button>
    </div>
  );
}
```

## 432: How do you persist state across navigations without global state libraries?

- Keep it in a layout's Client Component (layouts stay mounted).
- Keep it in the URL (search params) so it survives reloads and can be shared.
- With Cache Components, previously visited routes are kept in `<Activity>`, so local state in pages is kept when going back.
- Use `sessionStorage` or `localStorage` for longer persistence.

## 433: How do you implement a "Back" button in an intercepted modal that works on direct visits too?

When the modal was opened by navigation, `router.back()` closes it. When the page was opened directly (no history), `router.back()` would leave your site. Check if there is history from your app, or fall back to a known URL.

```tsx
"use client";

import { useRouter } from "next/navigation";

export function CloseModal() {
  const router = useRouter();

  function close() {
    if (window.history.length > 1) router.back();
    else router.push("/");
  }

  return <button onClick={close}>Close</button>;
}
```

For a direct visit, the intercepting route isn't used anyway, so the full page shows instead of the modal.

## 434: Why does an intercepting route not work after a page refresh?

Interception only happens on soft (client-side) navigation. On a hard load, the browser asks the server for the URL directly, and the server renders the real route (for example `app/photo/[id]/page.tsx`). This is by design: shared links show the full page, and in-app clicks show the modal.

## 435: How do you conditionally render parallel routes based on auth?

You can choose which slot to show in the layout.

```tsx
// app/dashboard/layout.tsx
export default async function Layout({
  user,
  admin,
}: {
  user: React.ReactNode;
  admin: React.ReactNode;
}) {
  const role = await getRole();
  return <>{role === "admin" ? admin : user}</>;
}
```

Both slots are still route segments, so make sure each also checks permissions on its own data.

## 436: How do you handle `default.tsx` for nested parallel routes?

Every slot needs a `default.tsx` at each level where the URL might not match a page in that slot. When you navigate to a sub-route only `children` defines, other slots keep their current content on soft navigation, but on hard navigation Next.js renders `default.tsx`. Without it, Next.js 16 fails the build. A catch-all `[...catchAll]/page.tsx` in the slot is another way to handle many sub-paths.

## 437: How do you build a resilient layout where one widget's failure doesn't break the page?

Give each independent section its own Suspense and error boundary. With parallel routes, each slot can have its own `error.tsx` and `loading.tsx`.

```
app/dashboard/
  @revenue/
    page.tsx
    loading.tsx
    error.tsx
  @orders/
    page.tsx
    loading.tsx
    error.tsx
```

If the revenue service is down, only that panel shows an error.

## 438: How does Next.js handle a Server Action called from a page that has since been redeployed?

The action ID may no longer exist on the new server. Next.js returns an error, and the client can't run the action. If `deploymentId` is set or the platform has skew protection, Next.js detects the mismatch and does a hard reload so the user gets the new version. Without that, the user may see an error until they refresh.

## 439: How do you profile React rendering in a Next.js app?

- Use the React DevTools Profiler in development, or a profiling build with `next build --profile`.
- In React 19.2+, Chrome DevTools has React Performance Tracks that show scheduler and component work in the Performance panel.
- For server render time, use OpenTelemetry spans or logs.

## 440: How do you diagnose memory leaks in a Next.js server?

- Run with `next start --inspect` or `node --inspect .next/standalone/server.js` and take heap snapshots in Chrome DevTools.
- Look for module-level arrays or Maps that grow per request (a common mistake: caching per-request data in a global variable).
- Check for unclosed database connections and event listeners.
- In dev, `next dev` uses more memory by design. Measure with the production build.
- Next.js has `experimental.webpackMemoryOptimizations` for webpack builds and memory usage guidance in the docs.

## 441: Why is storing per-request data in module-level variables dangerous in Next.js?

Module scope on the server is shared by all requests handled by the same process. If you store the current user in a module variable, another user's request may read it. This can leak data between users.

```ts
// Wrong
let currentUser: User | null = null;
export function setUser(u: User) {
  currentUser = u;
}
```

Use per-request APIs instead: `cookies()`, `headers()`, React `cache` (scoped to one request), or `AsyncLocalStorage`.

## 442: How does React `cache` know the current request?

Next.js runs each render inside a request scope (using `AsyncLocalStorage` on Node.js). React `cache` stores its results in a store tied to that scope, so a new request gets a new, empty cache. That is why `cache` is safe for per-request data and is cleared after the request.

## 443: How do you use `AsyncLocalStorage` in a Next.js app?

You can use it for things like request IDs in logs.

```ts
// lib/request-context.ts
import "server-only";
import { AsyncLocalStorage } from "node:async_hooks";

export const requestContext = new AsyncLocalStorage<{ requestId: string }>();
```

But there's no single place in Next.js where you wrap the whole request yourself, so for most cases React `cache` with a lazy initializer is simpler:

```ts
import { cache } from "react";

export const getRequestId = cache(() => crypto.randomUUID());
```

## 444: How do you implement feature flags that work with static pages?

- Evaluate flags in Proxy and rewrite to precomputed variants (like A/B testing).
- Use the Vercel Flags SDK `precompute` pattern, which encodes flag values into the URL so each combination can be prerendered.
- For flags that only change rarely, read them in a `"use cache"` function with a tag, and revalidate the tag when a flag changes.
- Avoid reading flags from cookies in the root layout, which makes everything dynamic.

## 445: How do you upgrade a large app from Next.js 15 to 16?

1. Make sure Node.js is 20.9 or newer.
2. Run `npx @next/codemod@canary upgrade latest`.
3. Rename `middleware.ts` to `proxy.ts` (codemod `middleware-to-proxy`).
4. Make sure all `params`, `searchParams`, `cookies()`, `headers()` and `draftMode()` uses are awaited.
5. Add `default.tsx` to every parallel route slot.
6. Change `revalidateTag(tag)` to `revalidateTag(tag, 'max')` or use `updateTag` in actions.
7. Replace `next lint` with the ESLint CLI.
8. Check custom webpack config: move it to Turbopack or use `--webpack`.
9. Review image config changes (`qualities`, `minimumCacheTTL`, `localPatterns`, `domains`).
10. Rename `experimental.dynamicIO` / `experimental.ppr` to `cacheComponents`, and `experimental.turbo` to `turbopack`.
11. Remove `serverRuntimeConfig` / `publicRuntimeConfig` and AMP usage.
12. Run `next build` and fix any new errors, then test the main flows end to end.

## 446: What was removed in Next.js 16?

- AMP support (`next/amp`, `useAmp`, `amp` config)
- The `next lint` command and the `eslint` option in `next.config`
- `serverRuntimeConfig` and `publicRuntimeConfig`
- `experimental.ppr`, `experimental_ppr` segment export and `experimental.dynamicIO` (replaced by `cacheComponents`)
- Synchronous access to `params`, `searchParams`, `cookies()`, `headers()` and `draftMode()`
- `unstable_rootParams` (an alternative is planned)
- Support for Node.js 18
- The `devIndicators` options `appIsrStatus`, `buildActivity` and `buildActivityPosition`

Deprecated (still working, but warn): `middleware.ts`, `images.domains`, `next/legacy/image`, the `priority` prop on images, and single-argument `revalidateTag`.

## 447: How do you choose between ISR, Cache Components and full dynamic rendering for a new project?

- **Mostly static content** (docs, blog, marketing): prerender with `generateStaticParams`, cache data with `"use cache"` (or `revalidate`), and revalidate on CMS webhooks.
- **Mixed pages** (e-commerce, dashboards with shared data): turn on Cache Components so each route has a static shell with dynamic parts streaming in.
- **Highly personal or real-time** (admin panels, chat): dynamic rendering is fine; focus on fast data access and Suspense for streaming.

For new Next.js 16 projects, Cache Components is the recommended model because it handles all three cases with one set of tools.

## 448: How would you design caching for a news site with breaking news updates?

- Article pages: `"use cache"` with `cacheLife('days')` and `cacheTag('article-<id>')`.
- Home page sections: cached with a short profile like `'minutes'`, tagged `'homepage'`.
- Breaking news banner: a small component with `'seconds'` life or dynamic in `<Suspense>`.
- CMS webhook: a Route Handler that calls `revalidateTag('article-<id>', 'max')` and `revalidateTag('homepage', 'max')`.
- Editor actions inside the app: Server Actions with `updateTag` so editors see changes right away.
- Use a shared remote cache handler when running more than one instance.

## 449: What are common performance mistakes in Next.js apps?

- Adding `"use client"` to layouts or pages, which sends the whole tree to the browser.
- Fetching data in `useEffect` instead of Server Components.
- Sequential `await`s that create waterfalls.
- Reading `cookies()` or `headers()` in the root layout, which makes every page dynamic.
- Missing `sizes` on responsive images.
- Large props passed to Client Components.
- Calling your own Route Handlers from Server Components instead of calling the function directly.
- Heavy work in Proxy.
- Not caching expensive queries that are the same for every user.
- Testing performance in `next dev` instead of a production build.

## 450: What questions would you ask before choosing Next.js for a project?

- Do we need SEO and fast first loads? (Next.js helps a lot.)
- Is most of the UI static, dynamic, or mixed? (This guides the caching strategy.)
- Where will we host it, and does that platform support the features we need (ISR, streaming, image optimization, Proxy)?
- Do we need a separate public API for other clients? (Plan Route Handlers or a separate backend.)
- Does the team know React Server Components and the caching model? (There is a learning curve.)
- Do we need real-time features like WebSockets? (Plan a separate service.)
- How will we handle upgrades? (Next.js moves fast; plan for regular updates and security patches, and pick an LTS line.)

If the app is a pure client-side tool behind a login with no SEO needs, a simpler setup like Vite with React might be enough. For most content and product websites, Next.js is a solid choice.
