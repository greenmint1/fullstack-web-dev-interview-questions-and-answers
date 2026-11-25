# CSS Optimization Interview Questions and Answers

_Last updated: November 25, 2026_

450 questions about making CSS load fast and render fast, split into three levels: 150 easy, 150 moderate and 150 advanced. They cover file size, render blocking, fonts, layout and paint cost, animations, tooling and how to measure all of it.

The answers target current evergreen browsers (Chrome, Edge, Firefox and Safari as of late 2026). Older tricks like CSS sprites, `@import` chains and the `translateZ(0)` hack are mentioned where you will still see them in real code, and they are marked as legacy.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What does CSS optimization mean?](#1-what-does-css-optimization-mean)
- [2: Why can CSS slow down a page?](#2-why-can-css-slow-down-a-page)
- [3: What is render-blocking CSS?](#3-what-is-render-blocking-css)
- [4: What is the critical rendering path?](#4-what-is-the-critical-rendering-path)
- [5: What is the CSSOM?](#5-what-is-the-cssom)
- [6: What is the difference between the DOM and the CSSOM?](#6-what-is-the-difference-between-the-dom-and-the-cssom)
- [7: Why does the browser need all the CSS before it can render?](#7-why-does-the-browser-need-all-the-css-before-it-can-render)
- [8: What is FOUC?](#8-what-is-fouc)
- [9: What is minification?](#9-what-is-minification)
- [10: Which tools are used to minify CSS?](#10-which-tools-are-used-to-minify-css)
- [11: What is compression and how is it different from minification?](#11-what-is-compression-and-how-is-it-different-from-minification)
- [12: Which compression should you use for CSS?](#12-which-compression-should-you-use-for-css)
- [13: How do you check if your CSS is compressed?](#13-how-do-you-check-if-your-css-is-compressed)
- [14: What is unused CSS?](#14-what-is-unused-css)
- [15: How do you find unused CSS?](#15-how-do-you-find-unused-css)
- [16: Why should you not just delete everything the Coverage panel marks as unused?](#16-why-should-you-not-just-delete-everything-the-coverage-panel-marks-as-unused)
- [17: What is PurgeCSS?](#17-what-is-purgecss)
- [18: Why is @import bad for performance?](#18-why-is-import-bad-for-performance)
- [19: What is the difference between link and @import?](#19-what-is-the-difference-between-link-and-import)
- [20: Where should you put stylesheet links in the HTML?](#20-where-should-you-put-stylesheet-links-in-the-html)
- [21: What does the media attribute on a stylesheet link do?](#21-what-does-the-media-attribute-on-a-stylesheet-link-do)
- [22: Should you split CSS into many small files or one big file?](#22-should-you-split-css-into-many-small-files-or-one-big-file)
- [23: How does HTTP/2 change CSS optimization?](#23-how-does-http2-change-css-optimization)
- [24: What is critical CSS?](#24-what-is-critical-css)
- [25: What does "above the fold" mean?](#25-what-does-above-the-fold-mean)
- [26: What are the pros and cons of inlining CSS?](#26-what-are-the-pros-and-cons-of-inlining-css)
- [27: How big should inlined critical CSS be?](#27-how-big-should-inlined-critical-css-be)
- [28: What is the preload scanner?](#28-what-is-the-preload-scanner)
- [29: Why are background images in CSS found late?](#29-why-are-background-images-in-css-found-late)
- [30: What does rel="preload" do for CSS?](#30-what-does-relpreload-do-for-css)
- [31: What is a reflow?](#31-what-is-a-reflow)
- [32: What is a repaint?](#32-what-is-a-repaint)
- [33: What is compositing?](#33-what-is-compositing)
- [34: Which CSS properties are cheapest to animate?](#34-which-css-properties-are-cheapest-to-animate)
- [35: Why is animating width or top slow?](#35-why-is-animating-width-or-top-slow)
- [36: What is 60 fps and why does it matter?](#36-what-is-60-fps-and-why-does-it-matter)
- [37: What is jank?](#37-what-is-jank)
- [38: What is will-change?](#38-what-is-will-change)
- [39: Why should you not use will-change on everything?](#39-why-should-you-not-use-will-change-on-everything)
- [40: What is the translateZ(0) hack?](#40-what-is-the-translatez0-hack)
- [41: What is Cumulative Layout Shift (CLS)?](#41-what-is-cumulative-layout-shift-cls)
- [42: How can CSS help prevent layout shift?](#42-how-can-css-help-prevent-layout-shift)
- [43: What does aspect-ratio do for performance?](#43-what-does-aspect-ratio-do-for-performance)
- [44: What is Largest Contentful Paint (LCP) and how does CSS affect it?](#44-what-is-largest-contentful-paint-lcp-and-how-does-css-affect-it)
- [45: What is Interaction to Next Paint (INP) and how does CSS affect it?](#45-what-is-interaction-to-next-paint-inp-and-how-does-css-affect-it)
- [46: Why do web fonts affect performance?](#46-why-do-web-fonts-affect-performance)
- [47: What are FOIT and FOUT?](#47-what-are-foit-and-fout)
- [48: What does font-display do?](#48-what-does-font-display-do)
- [49: When should you use font-display: optional?](#49-when-should-you-use-font-display-optional)
- [50: Which font format should you use?](#50-which-font-format-should-you-use)
- [51: Why should you limit the number of font weights and styles?](#51-why-should-you-limit-the-number-of-font-weights-and-styles)
- [52: What is a variable font?](#52-what-is-a-variable-font)
- [53: What is font subsetting?](#53-what-is-font-subsetting)
- [54: What are system fonts and why are they fast?](#54-what-are-system-fonts-and-why-are-they-fast)
- [55: Should you self-host fonts or use Google Fonts?](#55-should-you-self-host-fonts-or-use-google-fonts)
- [56: What is preconnect?](#56-what-is-preconnect)
- [57: How do CSS selectors affect performance?](#57-how-do-css-selectors-affect-performance)
- [58: Are ID selectors faster than class selectors?](#58-are-id-selectors-faster-than-class-selectors)
- [59: Why is the universal selector sometimes called slow?](#59-why-is-the-universal-selector-sometimes-called-slow)
- [60: In what direction do browsers match selectors?](#60-in-what-direction-do-browsers-match-selectors)
- [61: What is the key selector?](#61-what-is-the-key-selector)
- [62: Why are deeply nested selectors a problem?](#62-why-are-deeply-nested-selectors-a-problem)
- [63: What is specificity and how does it relate to performance?](#63-what-is-specificity-and-how-does-it-relate-to-performance)
- [64: What are CSS shorthand properties and do they help?](#64-what-are-css-shorthand-properties-and-do-they-help)
- [65: What are CSS custom properties?](#65-what-are-css-custom-properties)
- [66: How can custom properties make theming faster?](#66-how-can-custom-properties-make-theming-faster)
- [67: What is cache busting for CSS?](#67-what-is-cache-busting-for-css)
- [68: Which cache headers should you use for CSS files?](#68-which-cache-headers-should-you-use-for-css-files)
- [69: Why should you avoid inline style attributes for performance?](#69-why-should-you-avoid-inline-style-attributes-for-performance)
- [70: What are CSS sprites?](#70-what-are-css-sprites)
- [71: Are SVG icons better than icon fonts?](#71-are-svg-icons-better-than-icon-fonts)
- [72: Can you replace images with CSS?](#72-can-you-replace-images-with-css)
- [73: Is box-shadow expensive?](#73-is-box-shadow-expensive)
- [74: Is filter: blur() expensive?](#74-is-filter-blur-expensive)
- [75: Why can backdrop-filter be slow?](#75-why-can-backdrop-filter-be-slow)
- [76: What is the cost of position: fixed?](#76-what-is-the-cost-of-position-fixed)
- [77: Why use transform instead of top and left to move elements?](#77-why-use-transform-instead-of-top-and-left-to-move-elements)
- [78: How do you make a fade-in animation that is cheap?](#78-how-do-you-make-a-fade-in-animation-that-is-cheap)
- [79: Why should you avoid transition: all?](#79-why-should-you-avoid-transition-all)
- [80: What is prefers-reduced-motion?](#80-what-is-prefers-reduced-motion)
- [81: What is the contain property?](#81-what-is-the-contain-property)
- [82: What does content-visibility: auto do?](#82-what-does-content-visibility-auto-do)
- [83: Why do you need contain-intrinsic-size with content-visibility?](#83-why-do-you-need-contain-intrinsic-size-with-content-visibility)
- [84: What is a large DOM and why does it hurt CSS performance?](#84-what-is-a-large-dom-and-why-does-it-hurt-css-performance)
- [85: What is style recalculation?](#85-what-is-style-recalculation)
- [86: How can adding a class to the body be expensive?](#86-how-can-adding-a-class-to-the-body-be-expensive)
- [87: What tools can you use to measure CSS performance?](#87-what-tools-can-you-use-to-measure-css-performance)
- [88: What does Lighthouse say about CSS?](#88-what-does-lighthouse-say-about-css)
- [89: What is PageSpeed Insights?](#89-what-is-pagespeed-insights)
- [90: What is the difference between lab data and field data?](#90-what-is-the-difference-between-lab-data-and-field-data)
- [91: How do you see layout shifts in DevTools?](#91-how-do-you-see-layout-shifts-in-devtools)
- [92: What is paint flashing?](#92-what-is-paint-flashing)
- [93: What is a CSS preprocessor and can it hurt performance?](#93-what-is-a-css-preprocessor-and-can-it-hurt-performance)
- [94: What is PostCSS?](#94-what-is-postcss)
- [95: What is Autoprefixer and how can it affect file size?](#95-what-is-autoprefixer-and-how-can-it-affect-file-size)
- [96: What is Browserslist?](#96-what-is-browserslist)
- [97: What is Lightning CSS?](#97-what-is-lightning-css)
- [98: What is a utility-first CSS framework and how does it affect size?](#98-what-is-a-utility-first-css-framework-and-how-does-it-affect-size)
- [99: What is BEM and does it help performance?](#99-what-is-bem-and-does-it-help-performance)
- [100: What are CSS Modules?](#100-what-are-css-modules)
- [101: What is CSS-in-JS?](#101-what-is-css-in-js)
- [102: Why can runtime CSS-in-JS be slower than plain CSS?](#102-why-can-runtime-css-in-js-be-slower-than-plain-css)
- [103: What does "zero-runtime CSS-in-JS" mean?](#103-what-does-zero-runtime-css-in-js-mean)
- [104: What is a CSS reset and does its size matter?](#104-what-is-a-css-reset-and-does-its-size-matter)
- [105: What is the cost of using a full CSS framework like Bootstrap?](#105-what-is-the-cost-of-using-a-full-css-framework-like-bootstrap)
- [106: How can you load only the Bootstrap parts you need?](#106-how-can-you-load-only-the-bootstrap-parts-you-need)
- [107: Does Flexbox or Grid layout cost more than floats?](#107-does-flexbox-or-grid-layout-cost-more-than-floats)
- [108: What is a stacking context?](#108-what-is-a-stacking-context)
- [109: What is a compositor layer?](#109-what-is-a-compositor-layer)
- [110: How do you see compositor layers in DevTools?](#110-how-do-you-see-compositor-layers-in-devtools)
- [111: What is image-set() in CSS?](#111-what-is-image-set-in-css)
- [112: How do you load different background images for mobile and desktop?](#112-how-do-you-load-different-background-images-for-mobile-and-desktop)
- [113: Does display: none stop images from downloading?](#113-does-display-none-stop-images-from-downloading)
- [114: How do you lazy-load images that are set in CSS?](#114-how-do-you-lazy-load-images-that-are-set-in-css)
- [115: What is the cost of very large CSS files on mobile?](#115-what-is-the-cost-of-very-large-css-files-on-mobile)
- [116: How do you throttle the network and CPU in DevTools?](#116-how-do-you-throttle-the-network-and-cpu-in-devtools)
- [117: Do CSS comments hurt performance?](#117-do-css-comments-hurt-performance)
- [118: What is the cost of !important?](#118-what-is-the-cost-of-important)
- [119: Why are print styles usually loaded separately?](#119-why-are-print-styles-usually-loaded-separately)
- [120: What is the cost of many media queries?](#120-what-is-the-cost-of-many-media-queries)
- [121: What does mobile-first CSS mean and does it help speed?](#121-what-does-mobile-first-css-mean-and-does-it-help-speed)
- [122: How does dark mode affect CSS performance?](#122-how-does-dark-mode-affect-css-performance)
- [123: What does the color-scheme property do?](#123-what-does-the-color-scheme-property-do)
- [124: Can you use light-dark() to reduce CSS?](#124-can-you-use-light-dark-to-reduce-css)
- [125: What is a CSS budget?](#125-what-is-a-css-budget)
- [126: What is the "Avoid non-composited animations" warning in Lighthouse?](#126-what-is-the-avoid-non-composited-animations-warning-in-lighthouse)
- [127: How does a slow CSS file affect JavaScript?](#127-how-does-a-slow-css-file-affect-javascript)
- [128: Should you put scripts before or after stylesheets in the head?](#128-should-you-put-scripts-before-or-after-stylesheets-in-the-head)
- [129: What is the cost of CSS animations running off screen?](#129-what-is-the-cost-of-css-animations-running-off-screen)
- [130: Why is a spinner animation sometimes janky?](#130-why-is-a-spinner-animation-sometimes-janky)
- [131: What does the loading of fonts have to do with CLS?](#131-what-does-the-loading-of-fonts-have-to-do-with-cls)
- [132: What is size-adjust in @font-face?](#132-what-is-size-adjust-in-font-face)
- [133: What does preload do for fonts?](#133-what-does-preload-do-for-fonts)
- [134: Why do fonts need the crossorigin attribute when preloaded?](#134-why-do-fonts-need-the-crossorigin-attribute-when-preloaded)
- [135: What is the cost of a large number of CSS rules?](#135-what-is-the-cost-of-a-large-number-of-css-rules)
- [136: Are CSS nesting and native nesting slower than flat CSS?](#136-are-css-nesting-and-native-nesting-slower-than-flat-css)
- [137: What is the difference between visibility: hidden and display: none for performance?](#137-what-is-the-difference-between-visibility-hidden-and-display-none-for-performance)
- [138: Is opacity: 0 the same as hiding an element?](#138-is-opacity-0-the-same-as-hiding-an-element)
- [139: How do gradients compare to images for performance?](#139-how-do-gradients-compare-to-images-for-performance)
- [140: How do you prevent CSS from loading for a component that is not on the page?](#140-how-do-you-prevent-css-from-loading-for-a-component-that-is-not-on-the-page)
- [141: What does Vite do with CSS by default?](#141-what-does-vite-do-with-css-by-default)
- [142: What is a design token and how can it help CSS size?](#142-what-is-a-design-token-and-how-can-it-help-css-size)
- [143: What is duplicated CSS and how do you find it?](#143-what-is-duplicated-css-and-how-do-you-find-it)
- [144: What is stylelint and how can it help performance?](#144-what-is-stylelint-and-how-can-it-help-performance)
- [145: Why can third-party CSS hurt performance?](#145-why-can-third-party-css-hurt-performance)
- [146: What is a cookie banner's typical CSS problem?](#146-what-is-a-cookie-banners-typical-css-problem)
- [147: Can too many custom fonts on one page hurt LCP?](#147-can-too-many-custom-fonts-on-one-page-hurt-lcp)
- [148: What is the scroll-behavior property and is it expensive?](#148-what-is-the-scroll-behavior-property-and-is-it-expensive)
- [149: What are the easiest CSS performance wins for a typical site?](#149-what-are-the-easiest-css-performance-wins-for-a-typical-site)
- [150: What is the first thing you check when someone says "the CSS is slow"?](#150-what-is-the-first-thing-you-check-when-someone-says-the-css-is-slow)

### Moderate Questions (151-300)

- [151: How do you extract critical CSS automatically?](#151-how-do-you-extract-critical-css-automatically)
- [152: What is the difference between Beasties and critical?](#152-what-is-the-difference-between-beasties-and-critical)
- [153: How do you load the rest of the CSS without blocking rendering?](#153-how-do-you-load-the-rest-of-the-css-without-blocking-rendering)
- [154: What are the risks of loading non-critical CSS asynchronously?](#154-what-are-the-risks-of-loading-non-critical-css-asynchronously)
- [155: Why might the preload-then-stylesheet pattern be worse than the media swap pattern?](#155-why-might-the-preload-then-stylesheet-pattern-be-worse-than-the-media-swap-pattern)
- [156: How do you split CSS by route in a single-page app?](#156-how-do-you-split-css-by-route-in-a-single-page-app)
- [157: What is MiniCssExtractPlugin?](#157-what-is-minicssextractplugin)
- [158: Why is style-loader not good for production?](#158-why-is-style-loader-not-good-for-production)
- [159: How do you configure a safelist in PurgeCSS?](#159-how-do-you-configure-a-safelist-in-purgecss)
- [160: Why does Tailwind sometimes miss classes, and how do you fix it?](#160-why-does-tailwind-sometimes-miss-classes-and-how-do-you-fix-it)
- [161: How does Tailwind CSS v4 find which classes to generate?](#161-how-does-tailwind-css-v4-find-which-classes-to-generate)
- [162: What makes runtime CSS-in-JS expensive during rendering?](#162-what-makes-runtime-css-in-js-expensive-during-rendering)
- [163: How would you migrate away from a runtime CSS-in-JS library?](#163-how-would-you-migrate-away-from-a-runtime-css-in-js-library)
- [164: What is layout thrashing?](#164-what-is-layout-thrashing)
- [165: Which properties force layout when you read them?](#165-which-properties-force-layout-when-you-read-them)
- [166: How do you find forced layouts in DevTools?](#166-how-do-you-find-forced-layouts-in-devtools)
- [167: How does requestAnimationFrame help with CSS changes?](#167-how-does-requestanimationframe-help-with-css-changes)
- [168: How do you read the Performance panel for CSS problems?](#168-how-do-you-read-the-performance-panel-for-css-problems)
- [169: What does "Recalculate Style" show in the Performance panel?](#169-what-does-recalculate-style-show-in-the-performance-panel)
- [170: What are Selector Stats in Chrome DevTools?](#170-what-are-selector-stats-in-chrome-devtools)
- [171: What does the Rendering tab "Layer borders" option show?](#171-what-does-the-rendering-tab-layer-borders-option-show)
- [172: What is the "Frame Rendering Stats" option?](#172-what-is-the-frame-rendering-stats-option)
- [173: How do you test CSS performance on a real Android phone?](#173-how-do-you-test-css-performance-on-a-real-android-phone)
- [174: How does CSS affect INP in practice?](#174-how-does-css-affect-inp-in-practice)
- [175: What is the "presentation delay" part of INP?](#175-what-is-the-presentation-delay-part-of-inp)
- [176: How do you avoid layout shift from late-loading CSS?](#176-how-do-you-avoid-layout-shift-from-late-loading-css)
- [177: How do you avoid layout shift from web fonts in detail?](#177-how-do-you-avoid-layout-shift-from-web-fonts-in-detail)
- [178: What do ascent-override and descent-override do?](#178-what-do-ascent-override-and-descent-override-do)
- [179: How does next/font reduce font-related layout shift?](#179-how-does-nextfont-reduce-font-related-layout-shift)
- [180: What is unicode-range and how does it help?](#180-what-is-unicode-range-and-how-does-it-help)
- [181: What is the CSS Font Loading API?](#181-what-is-the-css-font-loading-api)
- [182: What is two-stage font loading?](#182-what-is-two-stage-font-loading)
- [183: What is fetchpriority and how does it relate to CSS?](#183-what-is-fetchpriority-and-how-does-it-relate-to-css)
- [184: Why is a hero image as a CSS background bad for LCP?](#184-why-is-a-hero-image-as-a-css-background-bad-for-lcp)
- [185: How do you preload a responsive background image?](#185-how-do-you-preload-a-responsive-background-image)
- [186: What is 103 Early Hints?](#186-what-is-103-early-hints)
- [187: Why was HTTP/2 Server Push dropped for CSS?](#187-why-was-http2-server-push-dropped-for-css)
- [188: What is the role of a CDN in CSS performance?](#188-what-is-the-role-of-a-cdn-in-css-performance)
- [189: What is stale-while-revalidate and is it useful for CSS?](#189-what-is-stale-while-revalidate-and-is-it-useful-for-css)
- [190: How can a service worker help CSS loading?](#190-how-can-a-service-worker-help-css-loading)
- [191: What is the transition-behavior property and does it help performance?](#191-what-is-the-transition-behavior-property-and-does-it-help-performance)
- [192: What is @starting-style?](#192-what-is-starting-style)
- [193: What are scroll-driven animations?](#193-what-are-scroll-driven-animations)
- [194: Why are scroll-driven animations faster than scroll event listeners?](#194-why-are-scroll-driven-animations-faster-than-scroll-event-listeners)
- [195: What is a passive event listener and why does it matter for scrolling?](#195-what-is-a-passive-event-listener-and-why-does-it-matter-for-scrolling)
- [196: What does touch-action do for performance?](#196-what-does-touch-action-do-for-performance)
- [197: What is overscroll-behavior?](#197-what-is-overscroll-behavior)
- [198: Why should you prefer CSS scroll-snap over JavaScript carousels?](#198-why-should-you-prefer-css-scroll-snap-over-javascript-carousels)
- [199: What are the costs of the View Transitions API?](#199-what-are-the-costs-of-the-view-transitions-api)
- [200: How do you add view transitions between pages without JavaScript?](#200-how-do-you-add-view-transitions-between-pages-without-javascript)
- [201: What are cascade layers?](#201-what-are-cascade-layers)
- [202: How do cascade layers help keep CSS small?](#202-how-do-cascade-layers-help-keep-css-small)
- [203: How do you put a third-party stylesheet into a layer?](#203-how-do-you-put-a-third-party-stylesheet-into-a-layer)
- [204: What is @scope?](#204-what-is-scope)
- [205: Do container queries have a performance cost?](#205-do-container-queries-have-a-performance-cost)
- [206: Why can't a size container depend on its content's size?](#206-why-cant-a-size-container-depend-on-its-contents-size)
- [207: How does :has() affect performance?](#207-how-does-has-affect-performance)
- [208: What kind of :has() selectors are expensive?](#208-what-kind-of-has-selectors-are-expensive)
- [209: Is the :is() and :where() pseudo-class expensive?](#209-is-the-is-and-where-pseudo-class-expensive)
- [210: What is the cost of attribute selectors?](#210-what-is-the-cost-of-attribute-selectors)
- [211: What is the cost of :nth-child() selectors?](#211-what-is-the-cost-of-nth-child-selectors)
- [212: How do you decide if a selector is slow?](#212-how-do-you-decide-if-a-selector-is-slow)
- [213: What causes a full-page style recalculation?](#213-what-causes-a-full-page-style-recalculation)
- [214: How does changing a custom property on :root affect performance?](#214-how-does-changing-a-custom-property-on-root-affect-performance)
- [215: What is @property and why is it useful?](#215-what-is-property-and-why-is-it-useful)
- [216: Can you animate custom properties cheaply?](#216-can-you-animate-custom-properties-cheaply)
- [217: How do you compare CSS approaches (CSS Modules, Tailwind, CSS-in-JS) for performance?](#217-how-do-you-compare-css-approaches-css-modules-tailwind-css-in-js-for-performance)
- [218: How does server-side rendering interact with CSS?](#218-how-does-server-side-rendering-interact-with-css)
- [219: How does React 19 handle stylesheets?](#219-how-does-react-19-handle-stylesheets)
- [220: How do you avoid duplicate CSS in a micro-frontend setup?](#220-how-do-you-avoid-duplicate-css-in-a-micro-frontend-setup)
- [221: How do you lazy-load CSS for a modal in plain JavaScript?](#221-how-do-you-lazy-load-css-for-a-modal-in-plain-javascript)
- [222: How do you prefetch CSS for the next page?](#222-how-do-you-prefetch-css-for-the-next-page)
- [223: What is the cost of very long class lists in HTML?](#223-what-is-the-cost-of-very-long-class-lists-in-html)
- [224: How does Sass @extend create bloated CSS?](#224-how-does-sass-extend-create-bloated-css)
- [225: What is the difference between @use and @import in Sass for output size?](#225-what-is-the-difference-between-use-and-import-in-sass-for-output-size)
- [226: How can Sass loops create too much CSS?](#226-how-can-sass-loops-create-too-much-css)
- [227: How do you measure CSS size in a build?](#227-how-do-you-measure-css-size-in-a-build)
- [228: How do you set a CSS size budget with size-limit?](#228-how-do-you-set-a-css-size-budget-with-size-limit)
- [229: How do you set a performance budget in Lighthouse CI?](#229-how-do-you-set-a-performance-budget-in-lighthouse-ci)
- [230: How do you stop CSS from causing a large LCP render delay?](#230-how-do-you-stop-css-from-causing-a-large-lcp-render-delay)
- [231: Why do A/B testing tools hurt CSS performance?](#231-why-do-ab-testing-tools-hurt-css-performance)
- [232: Why does content-visibility: auto help long pages?](#232-why-does-content-visibility-auto-help-long-pages)
- [233: What are the side effects of content-visibility: auto?](#233-what-are-the-side-effects-of-content-visibility-auto)
- [234: How does contain: layout help?](#234-how-does-contain-layout-help)
- [235: How does contain: paint help?](#235-how-does-contain-paint-help)
- [236: What does contain: size do?](#236-what-does-contain-size-do)
- [237: What does contain: style do?](#237-what-does-contain-style-do)
- [238: When would you use contain: strict?](#238-when-would-you-use-contain-strict)
- [239: How do you build a fast virtualized list?](#239-how-do-you-build-a-fast-virtualized-list)
- [240: When is content-visibility better than virtualization?](#240-when-is-content-visibility-better-than-virtualization)
- [241: How do you animate height smoothly?](#241-how-do-you-animate-height-smoothly)
- [242: What is interpolate-size?](#242-what-is-interpolate-size)
- [243: What is the FLIP technique?](#243-what-is-the-flip-technique)
- [244: Are CSS animations faster than JavaScript animations?](#244-are-css-animations-faster-than-javascript-animations)
- [245: What is the Web Animations API?](#245-what-is-the-web-animations-api)
- [246: Why do some transform animations still stutter?](#246-why-do-some-transform-animations-still-stutter)
- [247: Why does scaling text with transform sometimes look blurry?](#247-why-does-scaling-text-with-transform-sometimes-look-blurry)
- [248: When should you add and remove will-change?](#248-when-should-you-add-and-remove-will-change)
- [249: What is the cost of position: sticky?](#249-what-is-the-cost-of-position-sticky)
- [250: How do you build a shrinking header without layout thrashing?](#250-how-do-you-build-a-shrinking-header-without-layout-thrashing)
- [251: Why is IntersectionObserver better than scroll listeners for CSS changes?](#251-why-is-intersectionobserver-better-than-scroll-listeners-for-css-changes)
- [252: What is ResizeObserver and how does it help?](#252-what-is-resizeobserver-and-how-does-it-help)
- [253: What is the "ResizeObserver loop" error?](#253-what-is-the-resizeobserver-loop-error)
- [254: How do you handle styles for many breakpoints without large CSS?](#254-how-do-you-handle-styles-for-many-breakpoints-without-large-css)
- [255: Do clamp() and calc() cost more at runtime?](#255-do-clamp-and-calc-cost-more-at-runtime)
- [256: How do you avoid CLS from images in CSS layouts?](#256-how-do-you-avoid-cls-from-images-in-css-layouts)
- [257: How do you reserve space for ads or embeds?](#257-how-do-you-reserve-space-for-ads-or-embeds)
- [258: Why does adding a banner at the top cause CLS?](#258-why-does-adding-a-banner-at-the-top-cause-cls)
- [259: Do transform animations count as layout shift?](#259-do-transform-animations-count-as-layout-shift)
- [260: Do layout shifts after user input count toward CLS?](#260-do-layout-shifts-after-user-input-count-toward-cls)
- [261: How do you debug which element caused a layout shift?](#261-how-do-you-debug-which-element-caused-a-layout-shift)
- [262: How do you measure Core Web Vitals in real users?](#262-how-do-you-measure-core-web-vitals-in-real-users)
- [263: What is the Chrome UX Report?](#263-what-is-the-chrome-ux-report)
- [264: How do you check if CSS is the reason for a slow LCP?](#264-how-do-you-check-if-css-is-the-reason-for-a-slow-lcp)
- [265: Why is it a problem when CSS is loaded from a different domain?](#265-why-is-it-a-problem-when-css-is-loaded-from-a-different-domain)
- [266: How many render-blocking stylesheets is too many?](#266-how-many-render-blocking-stylesheets-is-too-many)
- [267: How do you handle CSS for above-the-fold content in a framework like Next.js?](#267-how-do-you-handle-css-for-above-the-fold-content-in-a-framework-like-nextjs)
- [268: How does Angular handle critical CSS?](#268-how-does-angular-handle-critical-css)
- [269: How does Astro handle CSS?](#269-how-does-astro-handle-css)
- [270: What is Vite's cssCodeSplit option?](#270-what-is-vites-csscodesplit-option)
- [271: How do you use Lightning CSS in Vite?](#271-how-do-you-use-lightning-css-in-vite)
- [272: What is the difference between cssnano presets?](#272-what-is-the-difference-between-cssnano-presets)
- [273: How do you remove unused CSS in a Vite project?](#273-how-do-you-remove-unused-css-in-a-vite-project)
- [274: How do you deal with unused CSS coming from a component library?](#274-how-do-you-deal-with-unused-css-coming-from-a-component-library)
- [275: Can CSS be tree-shaken like JavaScript?](#275-can-css-be-tree-shaken-like-javascript)
- [276: What is atomic CSS?](#276-what-is-atomic-css)
- [277: How does StyleX produce small CSS?](#277-how-does-stylex-produce-small-css)
- [278: How should you handle critical CSS for a page with many layouts?](#278-how-should-you-handle-critical-css-for-a-page-with-many-layouts)
- [279: What is the risk of inlining too much CSS?](#279-what-is-the-risk-of-inlining-too-much-css)
- [280: How do you load CSS differently for first and repeat visits?](#280-how-do-you-load-css-differently-for-first-and-repeat-visits)
- [281: Why does a slow CSS file sometimes block the whole page on mobile but not desktop?](#281-why-does-a-slow-css-file-sometimes-block-the-whole-page-on-mobile-but-not-desktop)
- [282: How do you handle CSS for third-party widgets like chat?](#282-how-do-you-handle-css-for-third-party-widgets-like-chat)
- [283: What is the facade pattern for embeds?](#283-what-is-the-facade-pattern-for-embeds)
- [284: How does a CSS framework's JavaScript plugin affect performance?](#284-how-does-a-css-frameworks-javascript-plugin-affect-performance)
- [285: How does the Popover API reduce CSS and JS?](#285-how-does-the-popover-api-reduce-css-and-js)
- [286: What is CSS anchor positioning and why is it faster than JS positioning?](#286-what-is-css-anchor-positioning-and-why-is-it-faster-than-js-positioning)
- [287: How do you style a large table without slowing down the page?](#287-how-do-you-style-a-large-table-without-slowing-down-the-page)
- [288: Why does table-layout: fixed help?](#288-why-does-table-layout-fixed-help)
- [289: What CSS should you avoid on elements inside a scrolling list?](#289-what-css-should-you-avoid-on-elements-inside-a-scrolling-list)
- [290: Is mix-blend-mode expensive?](#290-is-mix-blend-mode-expensive)
- [291: How do you audit animation performance in DevTools?](#291-how-do-you-audit-animation-performance-in-devtools)
- [292: Why might an opacity animation not be composited?](#292-why-might-an-opacity-animation-not-be-composited)
- [293: What is the cost of many small CSS animations at once?](#293-what-is-the-cost-of-many-small-css-animations-at-once)
- [294: How do you build a cheap skeleton loading shimmer?](#294-how-do-you-build-a-cheap-skeleton-loading-shimmer)
- [295: How do you check the CSS of a page for size issues quickly?](#295-how-do-you-check-the-css-of-a-page-for-size-issues-quickly)
- [296: How do you stop CSS from growing over time in a big team?](#296-how-do-you-stop-css-from-growing-over-time-in-a-big-team)
- [297: Why is global CSS hard to delete?](#297-why-is-global-css-hard-to-delete)
- [298: What is the cost of loading the same font from two different CSS files?](#298-what-is-the-cost-of-loading-the-same-font-from-two-different-css-files)
- [299: How do icon fonts affect render performance?](#299-how-do-icon-fonts-affect-render-performance)
- [300: How would you explain to a junior developer what to watch for in CSS performance?](#300-how-would-you-explain-to-a-junior-developer-what-to-watch-for-in-css-performance)

### Advanced Questions (301-450)

- [301: Walk through the full rendering pipeline in Chrome from a style change to pixels.](#301-walk-through-the-full-rendering-pipeline-in-chrome-from-a-style-change-to-pixels)
- [302: What runs on the main thread and what runs on the compositor thread?](#302-what-runs-on-the-main-thread-and-what-runs-on-the-compositor-thread)
- [303: What are property trees in Chrome?](#303-what-are-property-trees-in-chrome)
- [304: What is RenderingNG?](#304-what-is-renderingng)
- [305: What is Composite After Paint?](#305-what-is-composite-after-paint)
- [306: What is layer explosion?](#306-what-is-layer-explosion)
- [307: Why can overlap cause unexpected layer promotion?](#307-why-can-overlap-cause-unexpected-layer-promotion)
- [308: What is layer squashing?](#308-what-is-layer-squashing)
- [309: How do you estimate the GPU memory cost of a layer?](#309-how-do-you-estimate-the-gpu-memory-cost-of-a-layer)
- [310: What is rasterization and why does it matter?](#310-what-is-rasterization-and-why-does-it-matter)
- [311: What is checkerboarding?](#311-what-is-checkerboarding)
- [312: How does paint invalidation work?](#312-how-does-paint-invalidation-work)
- [313: How does style invalidation work in modern browsers?](#313-how-does-style-invalidation-work-in-modern-browsers)
- [314: Why can a selector like .active * be expensive?](#314-why-can-a-selector-like-active--be-expensive)
- [315: What are sibling invalidation and why can it be costly?](#315-what-are-sibling-invalidation-and-why-can-it-be-costly)
- [316: How does the browser optimize :has() invalidation?](#316-how-does-the-browser-optimize-has-invalidation)
- [317: What are Bloom filters used for in selector matching?](#317-what-are-bloom-filters-used-for-in-selector-matching)
- [318: What is the style sharing cache?](#318-what-is-the-style-sharing-cache)
- [319: How do inline style attributes affect style sharing?](#319-how-do-inline-style-attributes-affect-style-sharing)
- [320: How does inheritance of custom properties affect style performance?](#320-how-does-inheritance-of-custom-properties-affect-style-performance)
- [321: What is the cost of defining hundreds of custom properties on :root?](#321-what-is-the-cost-of-defining-hundreds-of-custom-properties-on-root)
- [322: When would you resolve design tokens at build time instead of using custom properties?](#322-when-would-you-resolve-design-tokens-at-build-time-instead-of-using-custom-properties)
- [323: How does the CSSOM API affect performance when you insert rules?](#323-how-does-the-cssom-api-affect-performance-when-you-insert-rules)
- [324: What are constructable stylesheets?](#324-what-are-constructable-stylesheets)
- [325: Why are constructable stylesheets better than a style tag in every shadow root?](#325-why-are-constructable-stylesheets-better-than-a-style-tag-in-every-shadow-root)
- [326: How does Shadow DOM affect style performance?](#326-how-does-shadow-dom-affect-style-performance)
- [327: What is useInsertionEffect in React and why does it exist?](#327-what-is-useinsertioneffect-in-react-and-why-does-it-exist)
- [328: How do runtime CSS-in-JS libraries handle SSR, and what is the cost?](#328-how-do-runtime-css-in-js-libraries-handle-ssr-and-what-is-the-cost)
- [329: Why do many teams move away from runtime CSS-in-JS with React Server Components?](#329-why-do-many-teams-move-away-from-runtime-css-in-js-with-react-server-components)
- [330: How does streaming SSR interact with stylesheets?](#330-how-does-streaming-ssr-interact-with-stylesheets)
- [331: How do you find CSS that causes slow INP?](#331-how-do-you-find-css-that-causes-slow-inp)
- [332: What is the Long Animation Frames API?](#332-what-is-the-long-animation-frames-api)
- [333: How do you measure the effect of a CSS change in production?](#333-how-do-you-measure-the-effect-of-a-css-change-in-production)
- [334: How does devicePixelRatio affect CSS paint cost?](#334-how-does-devicepixelratio-affect-css-paint-cost)
- [335: How do you handle a page that is janky on scroll only on low-end Android?](#335-how-do-you-handle-a-page-that-is-janky-on-scroll-only-on-low-end-android)
- [336: When does a transform animation fall back to the main thread?](#336-when-does-a-transform-animation-fall-back-to-the-main-thread)
- [337: How do scroll-driven animations run off the main thread?](#337-how-do-scroll-driven-animations-run-off-the-main-thread)
- [338: How do you provide a fallback for scroll-driven animations?](#338-how-do-you-provide-a-fallback-for-scroll-driven-animations)
- [339: How do view transitions take snapshots, and what does it cost?](#339-how-do-view-transitions-take-snapshots-and-what-does-it-cost)
- [340: What makes view transitions slow, and how do you fix it?](#340-what-makes-view-transitions-slow-and-how-do-you-fix-it)
- [341: How does content-visibility: hidden differ from display: none?](#341-how-does-content-visibility-hidden-differ-from-display-none)
- [342: How does content-visibility: auto affect accessibility?](#342-how-does-content-visibility-auto-affect-accessibility)
- [343: What is contain-intrinsic-size: auto and how does it remember sizes?](#343-what-is-contain-intrinsic-size-auto-and-how-does-it-remember-sizes)
- [344: How do you detect when content-visibility skips or renders an element?](#344-how-do-you-detect-when-content-visibility-skips-or-renders-an-element)
- [345: Why does content-visibility sometimes make performance worse?](#345-why-does-content-visibility-sometimes-make-performance-worse)
- [346: How do you design a CSS architecture for a large app with good performance?](#346-how-do-you-design-a-css-architecture-for-a-large-app-with-good-performance)
- [347: How do you migrate a legacy app with a 1 MB CSS file?](#347-how-do-you-migrate-a-legacy-app-with-a-1-mb-css-file)
- [348: How do you safely remove CSS in a site where HTML comes from a CMS?](#348-how-do-you-safely-remove-css-in-a-site-where-html-comes-from-a-cms)
- [349: How do visual regression tests help CSS optimization?](#349-how-do-visual-regression-tests-help-css-optimization)
- [350: How do you decide between inlining all CSS and linking it?](#350-how-do-you-decide-between-inlining-all-css-and-linking-it)
- [351: How does the browser prioritize CSS downloads?](#351-how-does-the-browser-prioritize-css-downloads)
- [352: How does a stylesheet in the body behave in modern Chrome?](#352-how-does-a-stylesheet-in-the-body-behave-in-modern-chrome)
- [353: What is the blocking="render" attribute?](#353-what-is-the-blockingrender-attribute)
- [354: How do you avoid a theme flash with server-side rendering?](#354-how-do-you-avoid-a-theme-flash-with-server-side-rendering)
- [355: How do CSS and the HTML parser interact with scripts in the head?](#355-how-do-css-and-the-html-parser-interact-with-scripts-in-the-head)
- [356: What happens if a stylesheet fails to load or hangs?](#356-what-happens-if-a-stylesheet-fails-to-load-or-hangs)
- [357: How do you protect the page from a slow third-party stylesheet?](#357-how-do-you-protect-the-page-from-a-slow-third-party-stylesheet)
- [358: How does the font matching process decide which fonts to download?](#358-how-does-the-font-matching-process-decide-which-fonts-to-download)
- [359: What is font synthesis and when does it matter for performance?](#359-what-is-font-synthesis-and-when-does-it-matter-for-performance)
- [360: How do variable fonts compare to static fonts in total bytes?](#360-how-do-variable-fonts-compare-to-static-fonts-in-total-bytes)
- [361: How do you subset a variable font while keeping axes?](#361-how-do-you-subset-a-variable-font-while-keeping-axes)
- [362: Why might preloading a font hurt performance?](#362-why-might-preloading-a-font-hurt-performance)
- [363: How do you choose between font-display swap and optional for a brand-heavy site?](#363-how-do-you-choose-between-font-display-swap-and-optional-for-a-brand-heavy-site)
- [364: What is the cost of very large CSS files on parsing?](#364-what-is-the-cost-of-very-large-css-files-on-parsing)
- [365: Does the browser cache parsed CSS?](#365-does-the-browser-cache-parsed-css)
- [366: How do you profile CSS parsing time?](#366-how-do-you-profile-css-parsing-time)
- [367: How does the number of DOM elements affect style recalculation cost?](#367-how-does-the-number-of-dom-elements-affect-style-recalculation-cost)
- [368: How does DOM depth affect layout?](#368-how-does-dom-depth-affect-layout)
- [369: What layouts are known to be expensive?](#369-what-layouts-are-known-to-be-expensive)
- [370: How can intrinsic sizing in grid hurt performance?](#370-how-can-intrinsic-sizing-in-grid-hurt-performance)
- [371: Why use minmax(0, 1fr) instead of 1fr in grid?](#371-why-use-minmax0-1fr-instead-of-1fr-in-grid)
- [372: How do flex items cause multiple layout passes?](#372-how-do-flex-items-cause-multiple-layout-passes)
- [373: What is the cost of percentage heights?](#373-what-is-the-cost-of-percentage-heights)
- [374: How do viewport units affect performance on mobile?](#374-how-do-viewport-units-affect-performance-on-mobile)
- [375: How does text rendering affect performance?](#375-how-does-text-rendering-affect-performance)
- [376: Is text-wrap: balance expensive?](#376-is-text-wrap-balance-expensive)
- [377: Why should you not animate font-size?](#377-why-should-you-not-animate-font-size)
- [378: How can SVG in CSS be a performance problem?](#378-how-can-svg-in-css-be-a-performance-problem)
- [379: Are data URIs in CSS a good idea?](#379-are-data-uris-in-css-a-good-idea)
- [380: How do CSS masks and clip-path affect performance?](#380-how-do-css-masks-and-clip-path-affect-performance)
- [381: How does the z-index and stacking context structure affect paint?](#381-how-does-the-z-index-and-stacking-context-structure-affect-paint)
- [382: How does overflow: hidden versus overflow: clip affect performance?](#382-how-does-overflow-hidden-versus-overflow-clip-affect-performance)
- [383: What makes an element a scroll container, and why does it matter?](#383-what-makes-an-element-a-scroll-container-and-why-does-it-matter)
- [384: What is composited scrolling?](#384-what-is-composited-scrolling)
- [385: What can prevent composited scrolling?](#385-what-can-prevent-composited-scrolling)
- [386: Why is background-attachment: fixed slow?](#386-why-is-background-attachment-fixed-slow)
- [387: How do you build a parallax effect without jank?](#387-how-do-you-build-a-parallax-effect-without-jank)
- [388: How does the browser handle animations in background tabs?](#388-how-does-the-browser-handle-animations-in-background-tabs)
- [389: How do iframes affect CSS performance on the parent page?](#389-how-do-iframes-affect-css-performance-on-the-parent-page)
- [390: What is the cost of a huge number of CSS animations defined but not running?](#390-what-is-the-cost-of-a-huge-number-of-css-animations-defined-but-not-running)
- [391: How do you profile memory used by CSS?](#391-how-do-you-profile-memory-used-by-css)
- [392: How would you debug a style recalculation that takes 200 ms on click?](#392-how-would-you-debug-a-style-recalculation-that-takes-200-ms-on-click)
- [393: What is the cost of a CSS transition starting on many elements at once?](#393-what-is-the-cost-of-a-css-transition-starting-on-many-elements-at-once)
- [394: How can you make a large list filter animation smooth?](#394-how-can-you-make-a-large-list-filter-animation-smooth)
- [395: What is the difference between transition and animation in cost?](#395-what-is-the-difference-between-transition-and-animation-in-cost)
- [396: How does the steps() timing function affect performance?](#396-how-does-the-steps-timing-function-affect-performance)
- [397: How do you reduce CSS work for hover effects on large lists?](#397-how-do-you-reduce-css-work-for-hover-effects-on-large-lists)
- [398: What is the cost of :focus-within and :hover on parents?](#398-what-is-the-cost-of-focus-within-and-hover-on-parents)
- [399: How do you decide which elements should be composited in a complex UI?](#399-how-do-you-decide-which-elements-should-be-composited-in-a-complex-ui)
- [400: How do you measure frame performance in production?](#400-how-do-you-measure-frame-performance-in-production)
- [401: How does Content Security Policy affect inlined critical CSS?](#401-how-does-content-security-policy-affect-inlined-critical-css)
- [402: How does the media swap trick conflict with CSP?](#402-how-does-the-media-swap-trick-conflict-with-csp)
- [403: Can CSS be used to leak data, and does that affect optimization choices?](#403-can-css-be-used-to-leak-data-and-does-that-affect-optimization-choices)
- [404: How does subresource integrity apply to CSS?](#404-how-does-subresource-integrity-apply-to-css)
- [405: Scenario: LCP is 4 seconds and the waterfall shows a 300 KB CSS file. What do you do?](#405-scenario-lcp-is-4-seconds-and-the-waterfall-shows-a-300-kb-css-file-what-do-you-do)
- [406: Scenario: CLS is 0.25 on mobile only. How do you find the cause?](#406-scenario-cls-is-025-on-mobile-only-how-do-you-find-the-cause)
- [407: Scenario: an animation is smooth on desktop but drops frames on iPhone. What do you check?](#407-scenario-an-animation-is-smooth-on-desktop-but-drops-frames-on-iphone-what-do-you-check)
- [408: Scenario: opening a dropdown makes the whole page relayout. How do you fix it?](#408-scenario-opening-a-dropdown-makes-the-whole-page-relayout-how-do-you-fix-it)
- [409: Scenario: typing in a search field is slow and the trace shows long Recalculate Style. Why?](#409-scenario-typing-in-a-search-field-is-slow-and-the-trace-shows-long-recalculate-style-why)
- [410: Scenario: a page with 5,000 product cards is slow to render. What CSS options do you have?](#410-scenario-a-page-with-5000-product-cards-is-slow-to-render-what-css-options-do-you-have)
- [411: Scenario: after adding a design system, CSS grew from 40 KB to 220 KB. How do you approach it?](#411-scenario-after-adding-a-design-system-css-grew-from-40-kb-to-220-kb-how-do-you-approach-it)
- [412: Scenario: fonts load late even though they are preloaded. Why?](#412-scenario-fonts-load-late-even-though-they-are-preloaded-why)
- [413: Scenario: the dark mode toggle freezes the page for 300 ms. How do you fix it?](#413-scenario-the-dark-mode-toggle-freezes-the-page-for-300-ms-how-do-you-fix-it)
- [414: Why do color transitions on every element make theme switches slow?](#414-why-do-color-transitions-on-every-element-make-theme-switches-slow)
- [415: Scenario: a marketing team adds a 2 MB animated background. What do you suggest?](#415-scenario-a-marketing-team-adds-a-2-mb-animated-background-what-do-you-suggest)
- [416: Scenario: Lighthouse says "Reduce unused CSS" but the team uses Tailwind. Why?](#416-scenario-lighthouse-says-reduce-unused-css-but-the-team-uses-tailwind-why)
- [417: How do you build critical CSS for a page with personalized content?](#417-how-do-you-build-critical-css-for-a-page-with-personalized-content)
- [418: How do you handle CSS in an edge-rendered app for best TTFB and FCP?](#418-how-do-you-handle-css-in-an-edge-rendered-app-for-best-ttfb-and-fcp)
- [419: What is the trade-off between one shared CSS file and per-page files in a multi-page site?](#419-what-is-the-trade-off-between-one-shared-css-file-and-per-page-files-in-a-multi-page-site)
- [420: How does HTTP/3 change CSS delivery?](#420-how-does-http3-change-css-delivery)
- [421: How do you prioritize CSS against JavaScript for the first load?](#421-how-do-you-prioritize-css-against-javascript-for-the-first-load)
- [422: How do you check that your CSS optimization does not break accessibility?](#422-how-do-you-check-that-your-css-optimization-does-not-break-accessibility)
- [423: What are the downsides of very aggressive CSS minification?](#423-what-are-the-downsides-of-very-aggressive-css-minification)
- [424: How do CSS source maps affect production performance?](#424-how-do-css-source-maps-affect-production-performance)
- [425: How do you compare two CSS optimizations objectively?](#425-how-do-you-compare-two-css-optimizations-objectively)
- [426: How does WebPageTest help with CSS optimization?](#426-how-does-webpagetest-help-with-css-optimization)
- [427: How do you debug a FOUC that only happens in production?](#427-how-do-you-debug-a-fouc-that-only-happens-in-production)
- [428: How do CSS frameworks with JIT generation work, and what are the performance trade-offs?](#428-how-do-css-frameworks-with-jit-generation-work-and-what-are-the-performance-trade-offs)
- [429: What is UnoCSS and how does it differ from Tailwind in performance?](#429-what-is-unocss-and-how-does-it-differ-from-tailwind-in-performance)
- [430: How do you deal with large CSS in email templates?](#430-how-do-you-deal-with-large-css-in-email-templates)
- [431: How do CSS custom highlight and other new APIs reduce DOM work?](#431-how-do-css-custom-highlight-and-other-new-apis-reduce-dom-work)
- [432: How does the browser handle @media and @container queries when resizing?](#432-how-does-the-browser-handle-media-and-container-queries-when-resizing)
- [433: What is the cost of nested container queries?](#433-what-is-the-cost-of-nested-container-queries)
- [434: How do style queries differ from size queries in cost?](#434-how-do-style-queries-differ-from-size-queries-in-cost)
- [435: How would you design CSS for a widget embedded on thousands of third-party sites?](#435-how-would-you-design-css-for-a-widget-embedded-on-thousands-of-third-party-sites)
- [436: How do you avoid style conflicts and extra CSS in a widget without Shadow DOM?](#436-how-do-you-avoid-style-conflicts-and-extra-css-in-a-widget-without-shadow-dom)
- [437: How does the "all" property help in embedded components?](#437-how-does-the-all-property-help-in-embedded-components)
- [438: How does a print stylesheet affect print performance?](#438-how-does-a-print-stylesheet-affect-print-performance)
- [439: How do you approach CSS performance for low-end devices specifically?](#439-how-do-you-approach-css-performance-for-low-end-devices-specifically)
- [440: What is the update media feature and when is it useful?](#440-what-is-the-update-media-feature-and-when-is-it-useful)
- [441: How do CSS and JavaScript bundles interact in code splitting edge cases?](#441-how-do-css-and-javascript-bundles-interact-in-code-splitting-edge-cases)
- [442: How can CSS order bugs appear after code splitting?](#442-how-can-css-order-bugs-appear-after-code-splitting)
- [443: How do you think about CSS optimization for a single-page app versus a multi-page app?](#443-how-do-you-think-about-css-optimization-for-a-single-page-app-versus-a-multi-page-app)
- [444: How do Speculation Rules help with CSS for the next page?](#444-how-do-speculation-rules-help-with-css-for-the-next-page)
- [445: How do you write a CSS performance checklist for code review?](#445-how-do-you-write-a-css-performance-checklist-for-code-review)
- [446: How do you balance visual design and CSS performance in a team discussion?](#446-how-do-you-balance-visual-design-and-css-performance-in-a-team-discussion)
- [447: What mistakes do teams make when optimizing CSS?](#447-what-mistakes-do-teams-make-when-optimizing-css)
- [448: What trends are changing CSS performance work today?](#448-what-trends-are-changing-css-performance-work-today)
- [449: If you could do only three things to improve CSS performance on a typical site, what would they be?](#449-if-you-could-do-only-three-things-to-improve-css-performance-on-a-typical-site-what-would-they-be)
- [450: How would you explain the CSS performance mindset in one answer?](#450-how-would-you-explain-the-css-performance-mindset-in-one-answer)

---

# Easy Questions (1-150)

## 1: What does CSS optimization mean?

It means making the CSS of a site cost less, both to download and to run. There are two sides to it:

- **Load cost**: how big the CSS files are, how many there are, and how long the browser waits for them before it can show the page.
- **Runtime cost**: how much work the browser does to apply the styles, lay out the page, paint it and animate it.

A good habit is to measure first, change one thing, and measure again.

## 2: Why can CSS slow down a page?

CSS blocks rendering. The browser will not paint anything until it has downloaded and parsed the CSS in the `<head>`, because it does not want to show unstyled content and then jump. So a big or slow CSS file delays the first paint. After that, some CSS properties make layout, paint or animations expensive, which can make scrolling and interactions feel slow.

## 3: What is render-blocking CSS?

It is CSS that the browser must download and parse before it paints the page. By default every `<link rel="stylesheet">` in the head is render-blocking, unless its `media` attribute does not match the current device. The less render-blocking CSS you have, the sooner the user sees something.

## 4: What is the critical rendering path?

It is the list of steps the browser goes through to turn HTML, CSS and JavaScript into pixels:

1. Parse HTML into the DOM.
2. Parse CSS into the CSSOM.
3. Combine them into the render tree.
4. Layout: work out the size and position of every box.
5. Paint: fill in pixels.
6. Composite: put the layers together on screen.

CSS sits right in the middle of this path, which is why it matters so much for speed.

## 5: What is the CSSOM?

The CSS Object Model is the tree the browser builds from all your stylesheets. It holds every rule and lets the browser work out the final style of each element. The browser needs the full CSSOM before it can render, because a rule at the end of a file can override one at the start.

## 6: What is the difference between the DOM and the CSSOM?

The DOM is built from HTML and describes the content and structure of the page. The CSSOM is built from CSS and describes the styles. The browser combines both into the render tree, which only contains the elements that will actually be shown, with their computed styles.

## 7: Why does the browser need all the CSS before it can render?

Because CSS cascades. A rule near the end of a file, or in a later file, can change how an element near the top looks. If the browser painted early, it might have to repaint everything once the rest of the CSS arrived, and the user would see a flash of unstyled content. So it waits.

## 8: What is FOUC?

FOUC means flash of unstyled content. The page shows for a moment with no styles, then jumps when the CSS loads. It happens when CSS is loaded in a way that does not block rendering, for example injected late by JavaScript. It looks broken and can cause layout shift, so you want to avoid it.

## 9: What is minification?

Minification removes everything the browser does not need: spaces, line breaks, comments and the last semicolon in a block. Good minifiers also shorten values, like `#ffffff` to `#fff` or `0px` to `0`, and merge duplicate rules. The CSS works the same but the file is smaller.

```css
/* before */
.button {
  color: #ffffff;
  margin: 0px 0px 0px 0px;
}

/* after */
.button {
  color: #fff;
  margin: 0;
}
```

## 10: Which tools are used to minify CSS?

The most common ones are cssnano (a PostCSS plugin), Lightning CSS, and esbuild. Vite uses esbuild for CSS minification by default and can switch to Lightning CSS. webpack projects usually use `css-minimizer-webpack-plugin`, which can run cssnano, Lightning CSS or esbuild under the hood.

## 11: What is compression and how is it different from minification?

Minification changes the CSS text itself. Compression is done by the server: it encodes the file with gzip, Brotli or Zstandard before sending it, and the browser decodes it. You should do both. Minification removes waste, and compression shrinks repeated patterns, which CSS has a lot of.

## 12: Which compression should you use for CSS?

Brotli is the usual choice today. It gives smaller files than gzip for text like CSS, and all modern browsers support it over HTTPS. Many CDNs also support Zstandard now. Keep gzip as a fallback for old clients. For static files, compress them once at build time at the highest level instead of on every request.

## 13: How do you check if your CSS is compressed?

Open DevTools, go to the Network tab, click the CSS file and look at the response headers. You should see `content-encoding: br`, `gzip` or `zstd`. You can also compare the transferred size and the resource size columns. If they are about the same for a large CSS file, it is not compressed.

## 14: What is unused CSS?

It is CSS that is downloaded but does not match anything on the current page. It is very common when you use a big framework like Bootstrap or keep old styles around after a redesign. It still has to be downloaded and parsed, so it slows down the first render for no reason.

## 15: How do you find unused CSS?

In Chrome DevTools, open the Coverage panel (Command Menu, then "Show Coverage"), start recording and reload the page. It shows how many bytes of each CSS file were used, and highlights unused rules in red in the Sources panel. Keep in mind it only knows about the current page and state, so a rule that looks unused might be used on hover, in a modal or on another route.

## 16: Why should you not just delete everything the Coverage panel marks as unused?

Because Coverage only records what was used during that session. Styles for hover states, error messages, mobile layouts, dark mode, other routes or content added by JavaScript later will show as unused. Use Coverage to find big candidates, then check them by hand or use a build tool that scans your templates.

## 17: What is PurgeCSS?

PurgeCSS is a tool that scans your HTML, templates and JavaScript files for class names and removes CSS rules that are never used. It is often used with Bootstrap or other large frameworks. Because it works on text, it can miss class names built dynamically, so you add those to a safelist.

## 18: Why is @import bad for performance?

`@import` inside a CSS file makes the browser download the first file, parse it, find the import, and only then start downloading the imported file. That creates a chain of requests one after another instead of in parallel. Using several `<link>` tags or bundling the files together avoids this. `@import` is fine in Sass or with a bundler, because those resolve the imports at build time.

## 19: What is the difference between link and @import?

`<link rel="stylesheet">` is in the HTML, so the browser finds it early (the preload scanner sees it) and can download several in parallel. `@import` is inside CSS, so the browser only finds it after downloading and parsing the parent file. For loading speed, `<link>` is better.

## 20: Where should you put stylesheet links in the HTML?

In the `<head>`. That way the browser finds them early and starts downloading them right away. If you put them at the end of the body, the browser may render the page without styles first, then restyle it, which causes FOUC and layout shift.

## 21: What does the media attribute on a stylesheet link do?

It tells the browser when the stylesheet applies. If the media query does not match, the file is still downloaded but at a low priority, and it does not block rendering.

```html
<link rel="stylesheet" href="main.css" />
<link rel="stylesheet" href="print.css" media="print" />
<link rel="stylesheet" href="wide.css" media="(min-width: 1200px)" />
```

Here `print.css` does not block the first paint on screen.

## 22: Should you split CSS into many small files or one big file?

It depends. One big file means one request but users download styles for pages they never visit. Many small files mean better caching and less unused CSS, but more requests. With HTTP/2 and HTTP/3, extra requests are cheap, so a common middle ground is a small shared file plus one file per route or page type.

## 23: How does HTTP/2 change CSS optimization?

HTTP/1.1 could only send a few requests at a time per connection, so people combined all CSS into one file and used sprites. HTTP/2 and HTTP/3 send many requests over one connection at the same time, so splitting CSS into a few files no longer costs much. Bundling everything into one huge file is no longer the only option.

## 24: What is critical CSS?

Critical CSS is the small set of styles needed to render the part of the page the user sees first (above the fold). You inline it in a `<style>` tag in the head so the browser can paint without waiting for an external file, then load the rest of the CSS in a non-blocking way.

## 25: What does "above the fold" mean?

It is the part of the page visible on screen before the user scrolls. The term comes from newspapers. For CSS optimization it matters because those are the styles you want available as early as possible.

## 26: What are the pros and cons of inlining CSS?

Pros: no extra request, so the browser can render as soon as the HTML arrives. Cons: inlined CSS is not cached separately, so it is sent again with every HTML page, and it makes the HTML bigger. That is why you only inline a small amount of critical CSS and keep the rest in a cached file.

## 27: How big should inlined critical CSS be?

Small. A common target is to keep the HTML plus critical CSS within the first roughly 14 KB compressed, because that is about what the server can send in the first round trip of a new TCP connection. It is a rule of thumb, not a hard limit, but the point is to keep it to what the first screen really needs.

## 28: What is the preload scanner?

It is a secondary parser in the browser that quickly looks ahead through the HTML for resources like stylesheets, scripts, images and fonts, and starts downloading them early, even while the main parser is blocked. Resources it cannot see, like files referenced only inside CSS or added by JavaScript, are found later.

## 29: Why are background images in CSS found late?

The browser only learns about a `background-image` URL after it downloads the CSS, parses it and finds an element that uses the rule. So the request starts much later than an `<img>` in the HTML. If the image is important, like a hero image, use an `<img>` tag or preload it.

## 30: What does rel="preload" do for CSS?

It tells the browser to download a file early at high priority, without applying it. You can preload a stylesheet that is found late (for example via `@import`) or a font used in your CSS.

```html
<link
  rel="preload"
  href="/fonts/inter.woff2"
  as="font"
  type="font/woff2"
  crossorigin
/>
```

Do not preload too many things, or you slow down what really matters.

## 31: What is a reflow?

Reflow, also called layout, is when the browser calculates the size and position of elements. It happens on first render and again whenever something changes geometry, like width, height, font size or adding elements. Reflow can be expensive because a change in one element can affect many others.

## 32: What is a repaint?

A repaint is when the browser redraws pixels without changing layout, for example when a color, background or visibility changes. It is cheaper than a reflow but still costs time, especially over large areas.

## 33: What is compositing?

Compositing is the last step, where the browser takes the painted layers and puts them together on the screen, usually on the GPU. Changes that only need compositing, like `transform` and `opacity`, are the cheapest, because the browser skips layout and paint.

## 34: Which CSS properties are cheapest to animate?

`transform` and `opacity`. In most cases the browser can animate them on the compositor without redoing layout or paint, so they stay smooth even when the main thread is busy. `filter` can often be composited too.

## 35: Why is animating width or top slow?

`width`, `height`, `top`, `left`, `margin` and `padding` change geometry, so every frame triggers layout, then paint, then composite. If many elements are affected, the browser cannot finish in 16 ms and you get dropped frames. Use `transform: translate()` or `scale()` instead.

```css
/* slow */
.panel {
  transition: left 0.3s;
}

/* fast */
.panel {
  transition: transform 0.3s;
}
.panel.open {
  transform: translateX(300px);
}
```

## 36: What is 60 fps and why does it matter?

Most screens refresh 60 times per second, which gives the browser about 16.7 ms per frame. In practice you have closer to 10 ms because the browser needs time for its own work. If a frame takes longer, it is skipped, and animations and scrolling look janky. On 120 Hz screens the budget is about 8 ms.

## 37: What is jank?

Jank is stutter or lag that users see when the browser misses frames during scrolling, animations or typing. It is usually caused by long JavaScript tasks or by expensive layout and paint work, for example animating layout properties or forcing layout many times in a row.

## 38: What is will-change?

`will-change` tells the browser that a property is about to change, so it can prepare, usually by moving the element to its own compositor layer.

```css
.menu {
  will-change: transform;
}
```

Use it on a few elements that will really animate. Putting it on many elements wastes memory.

## 39: Why should you not use will-change on everything?

Each promoted layer uses GPU memory, and many layers make compositing slower, not faster. On mobile devices this can even crash the tab. `will-change` is a hint for a specific problem, not a general speed-up. Add it before an animation starts and remove it after, or keep it only on a few elements that animate often.

## 40: What is the translateZ(0) hack?

It is a legacy trick: adding `transform: translateZ(0)` or `translate3d(0,0,0)` to force the browser to put an element on its own GPU layer. People used it before `will-change` existed. Today `will-change: transform` says the same thing more clearly, and both should be used only when needed.

## 41: What is Cumulative Layout Shift (CLS)?

CLS is a Core Web Vital that measures how much visible content jumps around while the page loads and during its life. A good score is 0.1 or less. CSS causes a lot of shifts: images without size, late web fonts, ads or banners inserted at the top, and styles that load late.

## 42: How can CSS help prevent layout shift?

Reserve space for things before they load:

- Set `width` and `height` on images, or use `aspect-ratio`.
- Give ad slots and embeds a fixed `min-height`.
- Use a fallback font with similar metrics.
- Do not insert content above existing content, unless the user asked for it.
- Animate with `transform` instead of changing `top` or `height`.

## 43: What does aspect-ratio do for performance?

It lets you reserve the right amount of space for an element before its content loads, so nothing moves when it arrives.

```css
.video-wrapper {
  aspect-ratio: 16 / 9;
  width: 100%;
}
```

Browsers also use the `width` and `height` attributes on `<img>` to set a default aspect ratio, so just setting those attributes already prevents a shift.

## 44: What is Largest Contentful Paint (LCP) and how does CSS affect it?

LCP measures when the largest image or text block in the viewport is shown. A good score is 2.5 seconds or less. CSS affects it because render-blocking CSS delays all painting, web fonts can delay text, and a hero image set as a CSS background is found late. Small critical CSS and a properly loaded hero image help LCP the most.

## 45: What is Interaction to Next Paint (INP) and how does CSS affect it?

INP measures how quickly the page shows a visual response after a click, tap or key press. A good score is 200 ms or less. CSS affects it through the rendering work after the event: if an interaction changes a class that forces style recalculation and layout of a huge DOM, the next paint is late.

## 46: Why do web fonts affect performance?

Fonts are extra files that the browser downloads only after it sees text that needs them. While waiting, it may hide the text (FOIT) or show a fallback and swap later (FOUT), which can cause a layout shift. Large font files and many weights make this worse.

## 47: What are FOIT and FOUT?

- **FOIT** (flash of invisible text): text is hidden until the web font loads.
- **FOUT** (flash of unstyled text): text is shown in a fallback font first, then switches to the web font.

FOUT is usually better because users can read right away. The `font-display` property controls which one you get.

## 48: What does font-display do?

It controls how text is shown while a web font loads.

```css
@font-face {
  font-family: "Inter";
  src: url("/fonts/inter.woff2") format("woff2");
  font-display: swap;
}
```

- `auto`: browser default, usually like `block`.
- `block`: hide text for up to about 3 seconds, then use fallback.
- `swap`: show fallback right away, swap when the font loads.
- `fallback`: very short hide, short swap window, then stay with fallback.
- `optional`: very short hide, use the font only if it is ready almost at once.

## 49: When should you use font-display: optional?

When avoiding layout shift matters more than always showing the brand font, for example for body text. If the font is not ready within about 100 ms, the browser uses the fallback for that page view and caches the font for the next one. It gives zero swap shifts.

## 50: Which font format should you use?

WOFF2. It is compressed with Brotli and supported by all modern browsers. You do not need TTF, EOT or SVG fonts any more, and WOFF is only for very old browsers. A simple `src: url("font.woff2") format("woff2")` is enough today.

## 51: Why should you limit the number of font weights and styles?

Each weight and style (regular, bold, italic, bold italic) is usually a separate file. Loading six of them for one font family can add hundreds of kilobytes. Pick the two or three weights you really use, or use a variable font if you need many.

## 52: What is a variable font?

A variable font is a single file that contains a whole range of weights, widths or other styles. Instead of loading `regular.woff2`, `medium.woff2` and `bold.woff2`, you load one file and set any weight with `font-weight`. It is often smaller than three or more static files, but bigger than one, so it pays off when you use several weights.

## 53: What is font subsetting?

Subsetting means removing characters you do not need from a font file. A full font may contain Latin, Cyrillic, Greek and hundreds of symbols. If your site is in English, a Latin subset is much smaller. Tools like `pyftsubset` (from fonttools) or `glyphhanger` do this, and Google Fonts serves subsets automatically.

## 54: What are system fonts and why are they fast?

System fonts are fonts already installed on the user's device, like San Francisco on Apple devices and Segoe UI on Windows. They need no download, so there is no delay and no font swap shift. You can use them with the `system-ui` keyword.

```css
body {
  font-family: system-ui, sans-serif;
}
```

## 55: Should you self-host fonts or use Google Fonts?

Self-hosting is usually faster today. Browsers no longer share cache between sites, so the old argument that users already have Google Fonts cached does not hold. Self-hosting avoids a connection to another domain, lets you control caching and preload, and avoids sending user data to a third party. Google Fonts is still fine for quick projects.

## 56: What is preconnect?

`preconnect` tells the browser to open a connection (DNS, TCP and TLS) to another domain early, before it needs a file from there.

```html
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
```

It is useful when CSS or fonts come from a third-party domain. Only preconnect to a few domains you will really use soon.

## 57: How do CSS selectors affect performance?

The browser has to match selectors against elements to know which rules apply. In most real sites this is fast and not the main problem. It only becomes noticeable with very large DOMs, very many rules, or selectors that force a lot of checking, like deep descendant chains or some uses of `:has()`. Simple class selectors are the cheapest.

## 58: Are ID selectors faster than class selectors?

In theory slightly, but the difference is too small to matter in practice. Browsers index both IDs and classes. Choose selectors for readability and low specificity, not for tiny matching speed differences. Class selectors are usually the better choice because they are reusable and easy to override.

## 59: Why is the universal selector sometimes called slow?

`*` matches every element, so a rule like `* { box-sizing: border-box; }` is checked against all of them. In practice that one rule is fine. The real cost comes from combinations like `.sidebar *` or `* + *`, which can force a lot of matching on big pages. Modern browsers handle most of this well, so only worry about it when profiling shows it.

## 60: In what direction do browsers match selectors?

Right to left. For `.nav ul li a`, the browser first finds all `a` elements, then for each one checks if it has an `li` parent, then a `ul`, then `.nav`. That is why the rightmost part (the key selector) matters most. A specific key selector like `.nav-link` rules out most elements right away.

## 61: What is the key selector?

It is the rightmost part of a selector, the one that targets the element being styled. In `.card .title span`, the key selector is `span`. Since browsers match right to left, a generic key selector means many elements are checked against the rest of the chain.

## 62: Why are deeply nested selectors a problem?

They make CSS harder to override, raise specificity, create larger files and can slow matching. Sass nesting makes this easy to do by accident.

```scss
// produces .page .content .card .header .title a
.page {
  .content {
    .card {
      .header {
        .title {
          a {
            color: red;
          }
        }
      }
    }
  }
}
```

Keep selectors short, ideally one or two levels.

## 63: What is specificity and how does it relate to performance?

Specificity decides which rule wins when several rules target the same element. It is not a big speed factor by itself, but high specificity leads to override wars, more rules and `!important`, which make the CSS bigger and harder to clean up. Flat, low-specificity CSS tends to stay smaller.

## 64: What are CSS shorthand properties and do they help?

Shorthands set several properties in one declaration, like `margin`, `padding`, `background`, `font` and `border`. They make the file smaller and easier to read. Be careful: a shorthand resets every sub-property it covers, so `background: red` also resets `background-image`.

## 65: What are CSS custom properties?

Custom properties (CSS variables) store a value you can reuse, like `--brand-color: #0066ff`. They help reduce repeated values and make theming cheap, because you can change one variable instead of shipping a whole second stylesheet. They do have some runtime cost when you change them on elements with many descendants.

```css
:root {
  --gap: 16px;
}
.card {
  padding: var(--gap);
}
```

## 66: How can custom properties make theming faster?

Instead of loading a separate stylesheet for dark mode, you change a few variables on the root element. The browser recalculates styles, but nothing new is downloaded.

```css
:root {
  --bg: white;
  --text: black;
}
[data-theme="dark"] {
  --bg: #111;
  --text: #eee;
}
body {
  background: var(--bg);
  color: var(--text);
}
```

## 67: What is cache busting for CSS?

It is a way to make browsers load a new version of a file after you change it. The usual method is to put a hash of the file contents in the file name, like `main.4f9a2c.css`. When the content changes, the name changes, so browsers fetch the new file. Build tools like Vite and webpack do this for you.

## 68: Which cache headers should you use for CSS files?

For hashed file names, cache them for a long time and mark them immutable:

```
Cache-Control: public, max-age=31536000, immutable
```

The HTML that links to them should be cached briefly or revalidated (`no-cache`), so users get the new file names after a deploy.

## 69: Why should you avoid inline style attributes for performance?

Inline `style="..."` attributes cannot be cached separately, are repeated on every element and every page, and make the HTML bigger. They also have very high specificity, which makes overrides hard. A shared class is cached once and reused everywhere. Inline styles are fine for truly dynamic values, like a position set by JavaScript.

## 70: What are CSS sprites?

Sprites are a legacy technique where many small images (icons) are combined into one big image, and each icon is shown with `background-position`. It saved HTTP requests in the HTTP/1.1 days. Today SVG icons, icon fonts or separate files over HTTP/2 are usually simpler and just as fast.

## 71: Are SVG icons better than icon fonts?

Usually yes. SVGs are sharper, can have several colors, are easier to make accessible, and you can include only the icons you use. Icon fonts often ship hundreds of unused glyphs, can show as empty squares while loading, and screen readers may read them strangely. Inline SVG or an SVG sprite with `<use>` is the common choice now.

## 72: Can you replace images with CSS?

Often, yes. Gradients, shadows, rounded corners, simple shapes and patterns can be done in CSS without any image download. That saves requests and scales to any screen. Just do not go too far: complex art built from hundreds of CSS boxes can cost more to render than a small SVG.

## 73: Is box-shadow expensive?

A few shadows are fine. Large blur values, many shadows on many elements, or animating `box-shadow` can make paint slow, because the browser must redraw the blur every frame. To animate a shadow, a common trick is to put the shadow on a pseudo-element and animate its `opacity`.

```css
.card {
  position: relative;
}
.card::after {
  content: "";
  position: absolute;
  inset: 0;
  box-shadow: 0 10px 30px rgb(0 0 0 / 0.3);
  opacity: 0;
  transition: opacity 0.3s;
}
.card:hover::after {
  opacity: 1;
}
```

## 74: Is filter: blur() expensive?

It can be. Blurs need to read many nearby pixels for each output pixel, and big blur radiuses over large areas cost a lot of GPU and paint time. Animating a blur is even more expensive. Use small radiuses, small areas, and test on low-end phones.

## 75: Why can backdrop-filter be slow?

`backdrop-filter` (for example the frosted glass effect) has to blur whatever is behind the element every time that content changes, like during scrolling. On large elements or weak devices this can drop frames. Keep the area small and avoid stacking several of them.

## 76: What is the cost of position: fixed?

Fixed elements stay in place while the page scrolls, so the browser usually puts them on their own layer. That is cheap for a small header. Problems come when the fixed element is big and has expensive effects (like `backdrop-filter`), or when you have many of them.

## 77: Why use transform instead of top and left to move elements?

`top` and `left` change layout, so the browser has to recalculate positions and repaint. `transform` moves the element visually without affecting layout, and can usually be handled by the compositor. It also allows sub-pixel movement, so animations look smoother.

## 78: How do you make a fade-in animation that is cheap?

Use `opacity`, and add a small `transform` if you want movement.

```css
.toast {
  opacity: 0;
  transform: translateY(8px);
  transition:
    opacity 0.2s,
    transform 0.2s;
}
.toast.show {
  opacity: 1;
  transform: none;
}
```

Both properties can run on the compositor.

## 79: Why should you avoid transition: all?

`transition: all` watches every property that changes, including layout ones like `width` or `padding`, which you may not want to animate. It can start expensive animations by accident and makes it unclear what is moving. List the properties you mean, like `transition: opacity 0.2s, transform 0.2s`.

## 80: What is prefers-reduced-motion?

It is a media query that matches when the user has asked the system to reduce motion. Respecting it helps people who get sick or distracted from animation, and it also saves work on the device.

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

## 81: What is the contain property?

`contain` tells the browser that an element is independent from the rest of the page in some way, so it can limit layout, style or paint work to that element.

```css
.widget {
  contain: layout paint;
}
```

Values include `layout`, `paint`, `size`, `style`, `inline-size`, and the shortcuts `content` (layout, paint, style) and `strict` (size plus content).

## 82: What does content-visibility: auto do?

It tells the browser to skip layout and paint for an element while it is off screen, and do the work only when it gets close to the viewport. On long pages with many sections, this can cut the initial render time a lot.

```css
.article-section {
  content-visibility: auto;
  contain-intrinsic-size: auto 800px;
}
```

## 83: Why do you need contain-intrinsic-size with content-visibility?

When the browser skips rendering an off-screen element, it does not know its height, so it treats it as 0. That makes the scrollbar wrong and the page jump as sections render. `contain-intrinsic-size` gives a placeholder size. With the `auto` keyword the browser remembers the real size after the element was rendered once.

## 84: What is a large DOM and why does it hurt CSS performance?

A large DOM means thousands of elements, often many levels deep. Every style recalculation and layout has more elements to check and measure. Lighthouse warns above about 1,400 elements. Fewer and flatter elements make every CSS change cheaper.

## 85: What is style recalculation?

It is the step where the browser works out the final computed style for elements after something changes, like a class being added. It shows in DevTools as "Recalculate Style". Its cost depends on how many elements are affected and how many rules must be checked for them.

## 86: How can adding a class to the body be expensive?

Many selectors depend on ancestors, like `.dark .button`. When you add a class to `<body>`, the browser may need to recheck styles for every element on the page. On a big DOM that can take tens of milliseconds. It is fine for a rare change like switching theme, but avoid it for frequent things like hover or scroll.

## 87: What tools can you use to measure CSS performance?

- **Lighthouse** and **PageSpeed Insights** for render-blocking CSS, unused CSS and Core Web Vitals.
- **Chrome DevTools Performance panel** for style recalculation, layout and paint times.
- **Coverage panel** for unused CSS.
- **Rendering tab** for paint flashing, layout shift regions and layer borders.
- **WebPageTest** for filmstrips and waterfalls on real devices and networks.

## 88: What does Lighthouse say about CSS?

The audits that mention CSS include "Eliminate render-blocking resources", "Reduce unused CSS", "Minify CSS", "Avoid an excessive DOM size", "Avoid non-composited animations" and "Ensure text remains visible during webfont load". Newer Lighthouse versions group some of these into insights, like the render-blocking requests insight, but the ideas are the same.

## 89: What is PageSpeed Insights?

It is a free Google tool that runs Lighthouse on a URL and also shows field data from real Chrome users (from the Chrome UX Report), if your site has enough traffic. Field data shows how real users experience your LCP, CLS and INP, which is more useful than a single lab test.

## 90: What is the difference between lab data and field data?

Lab data comes from a controlled test, like Lighthouse on your machine. It is repeatable and good for debugging. Field data comes from real users on their devices and networks. It is what Google uses for Core Web Vitals and shows the real experience. You need both: field data to know there is a problem, lab data to find why.

## 91: How do you see layout shifts in DevTools?

Open the Rendering tab and turn on "Layout Shift Regions". Areas that shift will flash blue. In the Performance panel, layout shifts show on their own track with details about which elements moved. The Web Vitals extension or the live metrics view in the Performance panel also shows CLS as you use the page.

## 92: What is paint flashing?

It is an option in the DevTools Rendering tab that highlights areas in green each time they are repainted. If large parts of the page flash on scroll or hover, something is causing too much paint, and that is a place to optimize.

## 93: What is a CSS preprocessor and can it hurt performance?

Sass, Less and Stylus are preprocessors: they add variables, nesting, mixins and loops, then compile to plain CSS. They do not slow the browser by themselves, but careless use can create large output: deep nesting, mixins that repeat the same declarations, `@extend` that creates huge selector lists, or loops that generate hundreds of unused classes.

## 94: What is PostCSS?

PostCSS is a tool that transforms CSS with JavaScript plugins. Common plugins include Autoprefixer (adds vendor prefixes), cssnano (minifies), and postcss-preset-env (lets you use newer CSS and compiles it for older browsers). Most build tools run PostCSS automatically.

## 95: What is Autoprefixer and how can it affect file size?

Autoprefixer adds vendor prefixes like `-webkit-` based on the browsers you support. If your browser list is too broad, it adds many prefixes you no longer need, making the file bigger. Keep your Browserslist config up to date so it only adds what your users need.

## 96: What is Browserslist?

Browserslist is a shared config that tells tools which browsers you support, for example `"> 0.5%, last 2 versions, not dead"` or `"defaults"`. Autoprefixer, Lightning CSS, Babel and others read it. A modern target means less prefixing and fewer fallbacks, so smaller CSS.

## 97: What is Lightning CSS?

Lightning CSS is a very fast CSS parser, transformer and minifier written in Rust. It can minify, add prefixes, lower modern syntax like nesting for older browsers, and bundle `@import`s. Vite can use it instead of PostCSS, and Tailwind CSS v4 uses it internally.

## 98: What is a utility-first CSS framework and how does it affect size?

Utility-first frameworks like Tailwind CSS give you small single-purpose classes such as `p-4` or `flex`. Because the same classes are reused everywhere, the CSS stops growing much as the site grows. Tailwind scans your source and only generates the classes you use, so the final file is usually small. The trade-off is longer class lists in the HTML.

## 99: What is BEM and does it help performance?

BEM (Block, Element, Modifier) is a naming convention like `.card__title--large`. It keeps selectors flat with one class each, so specificity stays low and matching is simple. The main benefit is maintainability, but flat CSS is also easier to clean up and tends to stay smaller.

## 100: What are CSS Modules?

CSS Modules are CSS files where class names are scoped to the component that imports them. The build tool renames `.title` to something unique like `.Card_title_x7f2`. That avoids naming conflicts and makes it clear which CSS belongs to which component, so unused styles are easier to delete. At build time it is plain CSS, so there is no runtime cost.

## 101: What is CSS-in-JS?

CSS-in-JS means writing styles in JavaScript files, next to components. Libraries like styled-components and Emotion generate and insert CSS at runtime. Others like vanilla-extract, Linaria and Panda CSS extract static CSS at build time. The runtime kind is convenient but adds JavaScript and work in the browser.

## 102: Why can runtime CSS-in-JS be slower than plain CSS?

The library ships as JavaScript, must run before styles appear, generates class names and inserts rules while components render. That adds bundle size and main thread time, and with server rendering it needs extra setup to avoid a flash of unstyled content. Plain CSS files are downloaded in parallel and parsed by the browser's fast native parser.

## 103: What does "zero-runtime CSS-in-JS" mean?

It means you write styles in JavaScript or TypeScript, but the build tool turns them into normal `.css` files. Nothing runs in the browser to create styles. Examples are vanilla-extract, Linaria, Panda CSS and StyleX. You get typed styles and co-location without the runtime cost.

## 104: What is a CSS reset and does its size matter?

A reset (or normalize) file removes or evens out browser default styles. Old resets were large and set many rules on many elements. Modern ones like a small `box-sizing` and margin reset are just a few lines. Keep it small and avoid resetting things you then set again everywhere.

## 105: What is the cost of using a full CSS framework like Bootstrap?

The full Bootstrap CSS is around 200+ KB before compression, and most sites use only a small part of it. That means more to download and parse. You can import only the Sass partials you need, or run PurgeCSS to remove unused rules.

## 106: How can you load only the Bootstrap parts you need?

Use the Sass source and import just the modules you use instead of the full build.

```scss
@import "bootstrap/scss/functions";
@import "bootstrap/scss/variables";
@import "bootstrap/scss/mixins";
@import "bootstrap/scss/root";
@import "bootstrap/scss/reboot";
@import "bootstrap/scss/grid";
@import "bootstrap/scss/buttons";
```

Bootstrap still documents `@import` because of how its Sass is built, even though Sass itself prefers `@use`.

## 107: Does Flexbox or Grid layout cost more than floats?

Not in any way that matters for normal pages. Modern browsers lay out Flexbox and Grid fast, and they replace hacks (clearfix, extra wrapper divs, JavaScript sizing) that cost more in total. Problems only show up with very large or deeply nested flex containers whose children depend on each other's sizes.

## 108: What is a stacking context?

It is a group of elements that are layered together in the z-axis. It is created by things like `position` with `z-index`, `opacity` below 1, `transform`, `filter`, `isolation: isolate` and `will-change`. For performance, it matters because many of these also create compositor layers, and because stacking contexts affect what has to be repainted together.

## 109: What is a compositor layer?

It is a part of the page that the browser paints separately and keeps as its own texture, usually on the GPU. When it moves or fades, the browser only composites it again without repainting. Elements get their own layer for reasons like `will-change: transform`, 3D transforms, video, canvas, or running a transform or opacity animation.

## 110: How do you see compositor layers in DevTools?

In Chrome, open the Rendering tab and turn on "Layer borders" to see orange and olive outlines around layers. The Layers panel (in More tools) shows a 3D view of all layers, their memory use and the reason each one was created.

## 111: What is image-set() in CSS?

`image-set()` lets you give several versions of a background image so the browser can pick the best one for the screen, like `srcset` for `<img>`.

```css
.hero {
  background-image: image-set(
    url("hero.avif") type("image/avif"),
    url("hero.webp") type("image/webp"),
    url("hero.jpg") type("image/jpeg")
  );
}
```

You can choose by resolution (`1x`, `2x`) or by format (`type()`).

## 112: How do you load different background images for mobile and desktop?

Use media queries. The browser only downloads the background image for the rule that applies.

```css
.hero {
  background-image: url("hero-small.webp");
}

@media (min-width: 900px) {
  .hero {
    background-image: url("hero-large.webp");
  }
}
```

## 113: Does display: none stop images from downloading?

For `<img>` elements, no. A hidden `<img>` is usually still downloaded unless it has `loading="lazy"`. For CSS background images, an element with `display: none` usually does not trigger the download, because its style is not used for rendering. Do not rely on CSS to hide big images on mobile; serve a smaller image or use `<picture>`.

## 114: How do you lazy-load images that are set in CSS?

The browser does not lazy-load CSS backgrounds on its own. A common way is to add the background only when the element gets close to the viewport, using `IntersectionObserver` to add a class.

```css
.section {
  background-color: #eee;
}
.section.visible {
  background-image: url("pattern.webp");
}
```

For content images, prefer `<img loading="lazy">` instead, which is built in.

## 115: What is the cost of very large CSS files on mobile?

Mobile devices have slower networks and slower CPUs. A big CSS file takes longer to download and parse, and it blocks the first paint the whole time. Parsing and building the CSSOM for hundreds of kilobytes of CSS can take noticeable time on a low-end phone. Test with throttling in DevTools to see it.

## 116: How do you throttle the network and CPU in DevTools?

In the Performance panel or Network tab, choose a network preset like "Slow 4G" or "Fast 4G". In the Performance panel settings, set CPU throttling to 4x or 6x slowdown. This gives a rough idea of how the page behaves on a mid-range phone. Testing on a real device is even better.

## 117: Do CSS comments hurt performance?

Not after minification, which removes them. In development files they only add size, which does not matter. Some comments start with `/*!` to mark licenses; minifiers keep those, so keep them short.

## 118: What is the cost of !important?

`!important` does not slow down the browser. The problem is that it makes CSS hard to override, so people add more `!important` and more specific selectors, and the CSS grows. It is a sign of specificity problems, not a speed problem by itself.

## 119: Why are print styles usually loaded separately?

Print styles are only needed when the user prints. Putting them in a file with `media="print"` means they do not block rendering on screen. You can also keep them in the main file inside `@media print { }`, which is fine if they are small.

## 120: What is the cost of many media queries?

Media queries themselves are cheap to evaluate. The cost is in the rules inside them, which add to the file size. Repeating the same breakpoint in hundreds of places adds a little size, but compression handles repetition well. Organize them for readability first.

## 121: What does mobile-first CSS mean and does it help speed?

Mobile-first means writing base styles for small screens and adding `min-width` media queries for larger ones. Mobile devices then apply fewer overrides. The speed gain is small, but it often leads to simpler CSS and makes you think about what small screens really need.

## 122: How does dark mode affect CSS performance?

If done with custom properties and `prefers-color-scheme` or a theme attribute, it adds little cost: a few extra variable definitions. Loading a second full stylesheet for dark mode is wasteful. Switching themes causes a style recalculation of the whole page, which is fine for a rare action.

## 123: What does the color-scheme property do?

`color-scheme: light dark` tells the browser that your page supports both themes, so it renders form controls, scrollbars and the default background in the right colors right away. That avoids a white flash before your dark styles apply.

```css
:root {
  color-scheme: light dark;
}
```

## 124: Can you use light-dark() to reduce CSS?

Yes. `light-dark()` returns one of two values based on the current color scheme, so you can define both colors in one place without separate media queries.

```css
:root {
  color-scheme: light dark;
}
body {
  background: light-dark(#fff, #111);
  color: light-dark(#111, #eee);
}
```

## 125: What is a CSS budget?

It is a limit you set for your CSS, like "no more than 50 KB compressed on any page" or "critical CSS under 14 KB". Build tools or CI check it and warn or fail when it is exceeded. Budgets stop CSS from slowly growing without anyone noticing.

## 126: What is the "Avoid non-composited animations" warning in Lighthouse?

It means some animations run on the main thread instead of the compositor, usually because they animate properties like `width`, `height`, `top`, `left`, `box-shadow` or `background-color`. These can stutter when the main thread is busy. Switching to `transform` and `opacity` usually fixes it.

## 127: How does a slow CSS file affect JavaScript?

Scripts that come after a stylesheet in the HTML wait for that stylesheet to finish before running, because they might read styles (like `getComputedStyle`). So a slow CSS file can also delay your JavaScript. Scripts with `async` do not wait. Regular `<script>` tags and `defer` scripts do wait for CSS that is before them.

## 128: Should you put scripts before or after stylesheets in the head?

Put stylesheets first, then use `defer` or `type="module"` for scripts. If a blocking script is placed after a slow stylesheet, it waits for the CSS. Deferred scripts download in parallel and run after parsing, so the order matters less for them.

## 129: What is the cost of CSS animations running off screen?

Many browsers stop or throttle animations that are not visible, but not always. An infinite animation in a hidden part of the page can keep causing paint or style work. Pause animations that are off screen, for example with `animation-play-state: paused` toggled by `IntersectionObserver`, or use `content-visibility` on that section.

## 130: Why is a spinner animation sometimes janky?

If it rotates with `transform: rotate()`, it can run on the compositor and stays smooth. If it is built by animating `border` colors, `width`, or a background position, it runs on the main thread and freezes when JavaScript is busy. Use `transform` for spinners.

## 131: What does the loading of fonts have to do with CLS?

When a web font replaces a fallback font, letters often have different widths and heights, so text reflows and moves content below it. That counts as layout shift. Picking a fallback with similar metrics, or tuning it with `size-adjust` and related descriptors, reduces the shift.

## 132: What is size-adjust in @font-face?

`size-adjust` scales a font by a percentage. You use it on a local fallback font to make it closer in size to your web font, so the swap causes less movement.

```css
@font-face {
  font-family: "Inter Fallback";
  src: local("Arial");
  size-adjust: 107%;
}
body {
  font-family: "Inter", "Inter Fallback", sans-serif;
}
```

## 133: What does preload do for fonts?

Fonts are normally discovered only after the CSS is parsed and the browser sees text that needs them. A preload starts the download early, so the font is more likely to be ready at first paint. Preload only the one or two fonts used above the fold, and always include `crossorigin`, even for same-origin fonts, or the file is downloaded twice.

## 134: Why do fonts need the crossorigin attribute when preloaded?

Fonts are always fetched in CORS mode. If the preload is made without `crossorigin`, it is a different kind of request and the browser cannot reuse it, so it downloads the font again. Adding `crossorigin` makes the preload match the real request.

## 135: What is the cost of a large number of CSS rules?

The browser stores every rule and must check relevant ones against elements during style calculation. Browsers use indexes (by id, class and tag) so most rules are skipped quickly. Still, tens of thousands of rules add parse time, memory and some matching time, especially on slow phones.

## 136: Are CSS nesting and native nesting slower than flat CSS?

Native CSS nesting is just a different way to write selectors. `.card { & .title { } }` means the same as `.card .title`. The cost comes from the selectors it produces, not the nesting syntax. Deep nesting creates long selectors, which is the real issue.

## 137: What is the difference between visibility: hidden and display: none for performance?

`display: none` removes the element from the layout, so it is not laid out or painted. `visibility: hidden` keeps its space and still runs layout, but does not paint it. Toggling `display` changes layout of other elements, while toggling `visibility` does not. Pick based on whether the space should stay reserved.

## 138: Is opacity: 0 the same as hiding an element?

Visually, yes, but the element still takes space, still gets layout and paint, and still receives clicks. It is good for fade animations because `opacity` can be animated cheaply. For truly hiding something, use `display: none`, `visibility: hidden` or the `hidden` attribute.

## 139: How do gradients compare to images for performance?

Gradients are drawn by the browser, so there is no download. They scale to any size and are tiny in the CSS. Very large or complex gradients repainted often (for example during scroll or animation) can cost paint time, but for normal use they are cheaper than an image.

## 140: How do you prevent CSS from loading for a component that is not on the page?

Split CSS by component or route. In modern frameworks, CSS imported by a lazily loaded component is put into its own chunk and only loaded when that component loads. For example, in Vite, `import "./Modal.css"` inside a lazy-loaded `Modal` module creates a separate CSS file.

## 141: What does Vite do with CSS by default?

Vite processes CSS imports, runs PostCSS if configured, supports CSS Modules for `*.module.css` files, and supports Sass and Less if the package is installed. In production builds it extracts CSS into files, splits it by async chunk, minifies it, and adds content hashes to file names.

## 142: What is a design token and how can it help CSS size?

A design token is a named value for a design decision, like a color, spacing step or font size. When used as custom properties or build-time constants, they keep values consistent and prevent dozens of near-identical colors and sizes, which tend to create duplicated CSS.

## 143: What is duplicated CSS and how do you find it?

It is the same declarations or rules written in many places, often from copy-paste or unused old components. Tools like Project Wallace and CSS Stats show how many unique colors, font sizes and declarations you have. Many minifiers also merge exact duplicate rules.

## 144: What is stylelint and how can it help performance?

Stylelint is a linter for CSS. It can warn about things that often lead to bloated or slow CSS: duplicate selectors, `@import` in plain CSS, too deep nesting (`max-nesting-depth`), overly specific selectors (`selector-max-specificity`), and unknown properties. It does not measure speed, but it keeps the code clean.

## 145: Why can third-party CSS hurt performance?

Third-party widgets (chat, cookie banners, ads, embeds) often bring their own CSS from another domain. That means more connections, more render-blocking files if loaded in the head, and styles you cannot control or trim. Load them lazily or after the main content where you can, and self-host what you can.

## 146: What is a cookie banner's typical CSS problem?

Cookie banners are often inserted at the top or bottom after load, sometimes pushing content and causing layout shift. Their CSS may be loaded from a third party late. Position them with `position: fixed` so they overlay instead of pushing content, and load their styles early or inline the minimal styles.

## 147: Can too many custom fonts on one page hurt LCP?

Yes. If the LCP element is a heading in a web font, and that font loads late, the browser may wait to paint the text, which delays LCP. Preloading that font, using `font-display: swap` or `optional`, and having fewer font files all help.

## 148: What is the scroll-behavior property and is it expensive?

`scroll-behavior: smooth` makes anchor links and `scrollTo` calls scroll smoothly instead of jumping. It is handled by the browser and is cheap. Respect `prefers-reduced-motion` by turning it off for users who asked for less motion.

## 149: What are the easiest CSS performance wins for a typical site?

- Minify and compress CSS (Brotli or gzip).
- Cache CSS files with hashed names and long cache headers.
- Remove unused CSS and large unused framework parts.
- Avoid `@import` chains.
- Use `font-display` and preload the main font.
- Set image dimensions or `aspect-ratio`.
- Animate only `transform` and `opacity`.

## 150: What is the first thing you check when someone says "the CSS is slow"?

Ask whether "slow" means slow to load or slow while using the page. For loading, check the Network waterfall and Lighthouse for render-blocking and unused CSS. For runtime, record the Performance panel while reproducing the problem and look for long "Recalculate Style", "Layout" or "Paint" entries. Fix based on what you measured, not on guesses.

# Moderate Questions (151-300)

## 151: How do you extract critical CSS automatically?

Use a tool that renders the page (or analyzes the HTML), finds which rules apply to the visible part, and inlines them. Common options:

- **Beasties** (the maintained fork of Google's Critters): inlines CSS used by the HTML at build time, without a headless browser. Nuxt and Angular use it.
- **critical** (by Addy Osmani): uses a headless browser to find above-the-fold CSS for given viewport sizes.
- **Penthouse**: the engine behind `critical`, usable on its own.

## 152: What is the difference between Beasties and critical?

Beasties does not run a browser. It parses the HTML and keeps every CSS rule that matches any element in it, then lazy-loads the full stylesheet. It is fast and simple but includes styles for the whole document, not only the first screen. `critical` renders the page in a headless browser at set viewport sizes and keeps only above-the-fold rules, which is more precise but slower and needs a browser in your build.

## 153: How do you load the rest of the CSS without blocking rendering?

A common pattern is the media swap trick: load the stylesheet with a media type that does not match, then switch it when it loads.

```html
<link
  rel="stylesheet"
  href="/full.css"
  media="print"
  onload="this.media='all'"
/>
<noscript><link rel="stylesheet" href="/full.css" /></noscript>
```

The file downloads at low priority without blocking, and applies as soon as it is ready. The `noscript` fallback covers users without JavaScript.

## 154: What are the risks of loading non-critical CSS asynchronously?

If your critical CSS misses something visible, users see a flash of unstyled or wrongly styled content, and a layout shift when the full CSS arrives. Critical CSS can also get out of date when templates change. You need to regenerate it in the build and check pages visually on several screen sizes.

## 155: Why might the preload-then-stylesheet pattern be worse than the media swap pattern?

The old pattern `<link rel="preload" as="style" onload="this.rel='stylesheet'">` downloads the CSS at high priority, which competes with truly critical resources like the LCP image. The `media="print"` trick downloads at low priority. Pick based on how soon you need the CSS, but do not mark everything as high priority.

## 156: How do you split CSS by route in a single-page app?

Import each route's CSS inside the route component and lazy-load the route. Bundlers then put that CSS in a separate chunk.

```js
// router
const Settings = lazy(() => import("./pages/Settings"));

// pages/Settings.jsx
import "./Settings.css";
export default function Settings() {
  /* ... */
}
```

When the user goes to settings, the bundler loads the JS and the CSS chunk together.

## 157: What is MiniCssExtractPlugin?

It is a webpack plugin that pulls CSS out of JavaScript bundles into separate `.css` files. Without it, webpack's `style-loader` injects CSS with JavaScript at runtime, which delays styles and can cause FOUC. Use `style-loader` in development for fast reloading and `MiniCssExtractPlugin.loader` in production.

## 158: Why is style-loader not good for production?

`style-loader` puts CSS inside the JavaScript bundle and adds `<style>` tags when the script runs. The browser cannot start parsing the CSS until the JavaScript has downloaded, parsed and run, so styles show up late. The CSS also cannot be cached separately from the JavaScript.

## 159: How do you configure a safelist in PurgeCSS?

Add class names, patterns or groups that PurgeCSS must keep even if it cannot find them in your source, for example classes added by JavaScript or from a CMS.

```js
// purgecss.config.js
module.exports = {
  content: ["./src/**/*.html", "./src/**/*.js"],
  css: ["./dist/styles.css"],
  safelist: {
    standard: ["is-open", "active"],
    deep: [/^modal-/],
    greedy: [/^swiper/],
  },
};
```

## 160: Why does Tailwind sometimes miss classes, and how do you fix it?

Tailwind finds classes by scanning source files as plain text. If you build class names from pieces, like `"text-" + color + "-500"`, the full name never appears, so it is not generated. Write full class names in a lookup object instead.

```js
const colors = {
  red: "text-red-500",
  blue: "text-blue-500",
};
```

In Tailwind v4 you can also force classes with `@source inline("...")`.

## 161: How does Tailwind CSS v4 find which classes to generate?

Tailwind v4 detects your source files automatically, skipping things in `.gitignore`, binary files and CSS files. You can add extra paths with the `@source` directive in your CSS, for example for a component library in `node_modules`. It then generates only the utilities it found.

```css
@import "tailwindcss";
@source "../node_modules/@my-company/ui";
```

## 162: What makes runtime CSS-in-JS expensive during rendering?

Libraries like styled-components or Emotion serialize the styles, hash them, check if the class already exists, and insert new rules into a stylesheet while components render. Inserting rules during render can force the browser to recalculate styles many times, especially with many dynamic props. In React 18 and later, `useInsertionEffect` reduces this, but there is still JavaScript work on every render.

## 163: How would you migrate away from a runtime CSS-in-JS library?

Do it step by step. Pick a zero-runtime target (CSS Modules, vanilla-extract, Panda CSS, Linaria or Tailwind). Convert leaf components first, keep dynamic values as CSS custom properties set through `style`, and remove the old library's provider at the end. Measure bundle size and render times before and after so you know it was worth it.

```jsx
// dynamic value without runtime CSS-in-JS
<div className={styles.bar} style={{ "--progress": `${pct}%` }} />
```

```css
.bar {
  width: var(--progress);
}
```

## 164: What is layout thrashing?

It happens when JavaScript writes to the DOM, then reads a layout value, then writes again, then reads again, in a loop. Each read after a write forces the browser to do layout right away (forced synchronous layout), so you get many layouts in one frame instead of one.

```js
// bad: layout on every iteration
items.forEach((el) => {
  el.style.width = box.offsetWidth + "px";
});

// good: read once, then write
const w = box.offsetWidth;
items.forEach((el) => {
  el.style.width = w + "px";
});
```

## 165: Which properties force layout when you read them?

Reading geometry forces layout if there are pending style changes. Common ones are `offsetWidth`, `offsetHeight`, `offsetTop`, `clientWidth`, `scrollTop`, `scrollHeight`, `getBoundingClientRect()`, `getComputedStyle()` for layout values, `innerText`, and `focus()` in some cases. Read them before making changes, not after.

## 166: How do you find forced layouts in DevTools?

Record in the Performance panel. Layout events triggered by JavaScript show as purple "Layout" blocks under a script task, and DevTools marks them with a red triangle and a warning like "Forced reflow is a likely performance bottleneck". Click it to see which line of code caused it.

## 167: How does requestAnimationFrame help with CSS changes?

`requestAnimationFrame` runs your callback right before the browser calculates styles and layout for the next frame. If you batch DOM writes inside it, the browser does one style and layout pass per frame. It also stops running in background tabs, which saves work.

```js
let pending = false;
window.addEventListener(
  "scroll",
  () => {
    if (pending) return;
    pending = true;
    requestAnimationFrame(() => {
      header.classList.toggle("compact", window.scrollY > 80);
      pending = false;
    });
  },
  { passive: true },
);
```

## 168: How do you read the Performance panel for CSS problems?

Record while you reproduce the slow action. In the Main track, look for long purple blocks (Recalculate Style, Layout) and green blocks (Paint, Composite Layers). Click a block to see how many elements were affected and how long it took. The Summary and Bottom-Up tabs show which kind of work took the most time overall.

## 169: What does "Recalculate Style" show in the Performance panel?

It shows how long style calculation took and how many elements were affected. With the "Enable CSS selector stats" setting turned on in the Performance panel, Chrome also shows which selectors took the most time to match, how many times they were tried, and how many matched. That helps find slow selectors.

## 170: What are Selector Stats in Chrome DevTools?

It is a feature in the Performance panel (turned on in the capture settings) that records how long each selector took during style recalculation. You get a table with elapsed time, match attempts, match count and how often the browser could reject the selector quickly. It is the most direct way to see if selectors are a real problem.

## 171: What does the Rendering tab "Layer borders" option show?

It draws borders around compositor layers and around the tiles they are split into. Orange borders show layers. If you see many layers you did not expect, you may have too much `will-change` or layer promotion, which uses memory.

## 172: What is the "Frame Rendering Stats" option?

It is in the Rendering tab and shows an overlay with frame rate and GPU memory use while you interact with the page. It helps you see dropped frames during scrolling or animation without recording a full trace.

## 173: How do you test CSS performance on a real Android phone?

Connect the phone with USB, turn on USB debugging, open `chrome://inspect` on your computer and inspect the page. You get full DevTools, including the Performance panel, running against the real device. Real phones show problems that a throttled laptop hides, like GPU memory limits.

## 174: How does CSS affect INP in practice?

After an interaction, the browser has to recalculate styles, lay out and paint before the next frame. If a click toggles a class on a large container, or opens a menu that changes layout across the page, rendering can take more time than the event handler itself. Keep the affected area small, use `contain`, and avoid layout-heavy changes on interaction.

## 175: What is the "presentation delay" part of INP?

INP is split into input delay, processing time (your event handlers) and presentation delay. Presentation delay is the time from when handlers finish until the next frame is shown, which includes style, layout, paint and composite. Heavy CSS work shows up here.

## 176: How do you avoid layout shift from late-loading CSS?

Do not load styles that affect above-the-fold layout asynchronously. Make sure critical CSS includes the layout of the first screen, including widths, heights and grid structure. If a component's CSS loads lazily, reserve its space or render it only once its CSS has arrived.

## 177: How do you avoid layout shift from web fonts in detail?

- Preload the main font so it is often ready before first paint.
- Use `font-display: optional` for zero swap shift, or `swap` with a matched fallback.
- Create a fallback `@font-face` with `size-adjust`, `ascent-override`, `descent-override` and `line-gap-override` that match the web font.
- Tools like Fontaine, Capsize, and the font helpers in Next.js and Nuxt generate these values for you.

## 178: What do ascent-override and descent-override do?

They set the font's ascent (space above the baseline) and descent (space below), which control line height when `line-height` is `normal` and how text sits in its box. Setting them on a fallback font to match the web font keeps line boxes the same size, so text does not move vertically when the font swaps.

```css
@font-face {
  font-family: "Roboto Fallback";
  src: local("Arial");
  size-adjust: 100.3%;
  ascent-override: 92%;
  descent-override: 24%;
  line-gap-override: 0%;
}
```

The exact numbers come from the font's metrics.

## 179: How does next/font reduce font-related layout shift?

Next.js `next/font` downloads Google Fonts or local fonts at build time and self-hosts them, so there is no request to Google from the browser. It also generates a fallback font with `size-adjust` and override values that match the real font, and sets `font-display` for you. This removes most font swap shift with little setup.

## 180: What is unicode-range and how does it help?

`unicode-range` tells the browser which characters a font file covers. The browser downloads that file only if the page uses one of those characters. You can split a font into subsets (Latin, Cyrillic, Greek) and users only download what their page needs.

```css
@font-face {
  font-family: "Inter";
  src: url("/fonts/inter-latin.woff2") format("woff2");
  unicode-range: U+0000-00FF, U+0131, U+0152-0153;
}
@font-face {
  font-family: "Inter";
  src: url("/fonts/inter-cyrillic.woff2") format("woff2");
  unicode-range: U+0400-045F, U+0490-0491;
}
```

## 181: What is the CSS Font Loading API?

It is a JavaScript API (`document.fonts`) that lets you load fonts on demand and know when they are ready.

```js
await document.fonts.load("700 1em Inter");
document.documentElement.classList.add("fonts-loaded");
```

You can use it to load fonts in two stages, or to wait until a font is ready before measuring text. `document.fonts.ready` resolves when all fonts needed so far have loaded.

## 182: What is two-stage font loading?

You first load a small subset of the main font (for example only the regular weight, Latin only) so text renders quickly. Then you load the bold, italic and full character set afterward. This gets readable, branded text on screen fast, and the extra styles arrive later with a smaller visual change.

## 183: What is fetchpriority and how does it relate to CSS?

`fetchpriority="high"` or `"low"` on `<img>`, `<link>` or `<script>` changes the download priority. For CSS-related work, you can raise the priority of the LCP image so it does not wait behind other files, or lower the priority of a non-critical stylesheet.

```html
<img src="hero.webp" fetchpriority="high" alt="" width="1200" height="600" />
```

## 184: Why is a hero image as a CSS background bad for LCP?

The browser finds the image only after it downloads and parses the CSS and matches the rule. That can delay the start of the download by hundreds of milliseconds. An `<img>` in the HTML is found by the preload scanner right away. If you must use a background, add a preload with `fetchpriority="high"` for it.

```html
<link rel="preload" as="image" href="/hero.webp" fetchpriority="high" />
```

## 185: How do you preload a responsive background image?

Use `imagesrcset` and `imagesizes` on the preload link, matching the image you use in CSS for each size.

```html
<link
  rel="preload"
  as="image"
  imagesrcset="/hero-800.webp 800w, /hero-1600.webp 1600w"
  imagesizes="100vw"
  fetchpriority="high"
/>
```

## 186: What is 103 Early Hints?

It is an HTTP response the server sends before the main response is ready. It can include `Link` headers to preload or preconnect, so the browser starts downloading CSS and fonts while the server is still generating the HTML. CDNs like Cloudflare and Fastly support it, and Chrome, Edge, Firefox and Safari use it for preconnect and preload.

```
HTTP/1.1 103 Early Hints
Link: </styles/main.css>; rel=preload; as=style
```

## 187: Why was HTTP/2 Server Push dropped for CSS?

Server Push let the server send CSS before the browser asked for it. In practice it often pushed files the browser already had cached, wasted bandwidth, and was hard to get right. Chrome removed support for it, and 103 Early Hints plus preload replaced it.

## 188: What is the role of a CDN in CSS performance?

A CDN serves CSS from servers close to the user, so download time is lower. It also handles compression, HTTP/2 and HTTP/3, caching and often Early Hints. Since CSS blocks rendering, cutting its latency directly speeds up the first paint.

## 189: What is stale-while-revalidate and is it useful for CSS?

`Cache-Control: max-age=60, stale-while-revalidate=86400` lets the browser use a cached copy right away even after it expires, while it fetches a fresh one in the background. For hashed CSS files you do not need it because they are immutable. It can help for unhashed CSS or for the HTML that references the CSS.

## 190: How can a service worker help CSS loading?

A service worker can cache CSS files on first visit and serve them from the cache on later visits, even offline. It can also precache CSS for routes the user has not visited yet. Workbox makes this easy. Be careful to update cached CSS on deploys, usually by precaching hashed files.

## 191: What is the transition-behavior property and does it help performance?

`transition-behavior: allow-discrete` lets you transition discrete properties like `display` and `content-visibility`. You can then fade an element out and set `display: none` at the end, all in CSS, without JavaScript timers. Together with `@starting-style` it makes enter and exit animations simple and keeps them in cheap properties like `opacity`.

```css
.dialog {
  transition:
    opacity 0.2s,
    display 0.2s allow-discrete;
  opacity: 1;
}
.dialog.hidden {
  display: none;
  opacity: 0;
}
@starting-style {
  .dialog {
    opacity: 0;
  }
}
```

## 192: What is @starting-style?

It defines the styles an element starts from the first time it is rendered, so a transition can run when it appears. Before it, you needed JavaScript to add a class after one frame. Now it is pure CSS.

```css
.toast {
  opacity: 1;
  transition: opacity 0.3s;
}
@starting-style {
  .toast {
    opacity: 0;
  }
}
```

## 193: What are scroll-driven animations?

They are CSS animations whose progress is linked to scroll position (`scroll()`) or to an element's visibility in the viewport (`view()`), instead of time. They replace JavaScript scroll listeners for effects like progress bars and reveal animations, and when they animate `transform` or `opacity` they can run on the compositor, off the main thread.

```css
.progress {
  transform-origin: left;
  animation: grow linear;
  animation-timeline: scroll();
}
@keyframes grow {
  from {
    transform: scaleX(0);
  }
  to {
    transform: scaleX(1);
  }
}
```

## 194: Why are scroll-driven animations faster than scroll event listeners?

A scroll listener runs JavaScript on the main thread, and if the main thread is busy the effect lags behind the scroll. Scroll-driven animations are known to the browser ahead of time, so the compositor can update them in sync with scrolling. Check support before using them; add a simple fallback for browsers that do not have them.

## 195: What is a passive event listener and why does it matter for scrolling?

A passive listener promises not to call `preventDefault()`. Without that promise, the browser must wait for your `touchstart` or `wheel` handler before it can scroll. With `{ passive: true }`, scrolling starts right away on the compositor. Chrome treats touch and wheel listeners on the window and document as passive by default.

## 196: What does touch-action do for performance?

`touch-action` tells the browser which touch gestures an element handles itself. For example, `touch-action: pan-y` on a horizontal carousel lets the browser handle vertical scrolling without waiting for JavaScript. `touch-action: manipulation` disables double-tap zoom, which used to remove a tap delay.

## 197: What is overscroll-behavior?

It controls what happens when you reach the end of a scroll area. `overscroll-behavior: contain` stops scroll chaining, so scrolling inside a modal or sidebar does not scroll the page behind it. It replaces JavaScript hacks that blocked scroll events, which were bad for scroll performance.

## 198: Why should you prefer CSS scroll-snap over JavaScript carousels?

`scroll-snap-type` and `scroll-snap-align` let the browser snap to items during native scrolling. It runs on the compositor, works with touch, mouse and keyboard, and needs no JavaScript. JavaScript carousels often listen to scroll or touch events and animate `left`, which is slower and less smooth.

```css
.carousel {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
}
.carousel > * {
  scroll-snap-align: start;
}
```

## 199: What are the costs of the View Transitions API?

View transitions take a snapshot of the old state, render the new one, and animate between them with pseudo-elements. This needs memory for the snapshots and can block rendering briefly while the snapshot is taken. Keep `view-transition-name` on a limited number of elements, keep animations short, and respect `prefers-reduced-motion`.

## 200: How do you add view transitions between pages without JavaScript?

For same-origin navigations in a multi-page site, add this to the CSS of both pages:

```css
@view-transition {
  navigation: auto;
}
```

The browser then cross-fades between pages by default, and you can customize it with `view-transition-name` and the `::view-transition-*` pseudo-elements. Browsers that do not support it just navigate normally.

## 201: What are cascade layers?

`@layer` lets you group CSS into named layers with a fixed order. A rule in a later layer wins over a rule in an earlier layer, no matter the specificity. Styles not in any layer win over all layered styles.

```css
@layer reset, base, components, utilities;

@layer components {
  .button {
    padding: 8px 16px;
  }
}
@layer utilities {
  .p-0 {
    padding: 0;
  }
}
```

## 202: How do cascade layers help keep CSS small?

Without layers, overriding a library or a base style often needs a more specific selector or `!important`, and those pile up. With layers, a simple class in a later layer wins, so you write fewer and shorter selectors. It also makes third-party CSS easier to override without copying it.

## 203: How do you put a third-party stylesheet into a layer?

Use `@import` with `layer()`, or wrap it in your bundler.

```css
@import url("vendor/library.css") layer(vendor);
```

Now your own unlayered or later-layered styles override it without specificity fights. Note that a plain-CSS `@import` still creates a request chain unless your bundler inlines it.

## 204: What is @scope?

`@scope` limits styles to a part of the DOM, with an optional lower boundary where the scope stops.

```css
@scope (.card) to (.card-content) {
  img {
    border-radius: 8px;
  }
}
```

It lets you write short selectors without them leaking out, which avoids long chains like `.card .media img`. It also adds "scoping proximity", where the closer scope wins.

## 205: Do container queries have a performance cost?

A little. An element with `container-type: inline-size` gets size containment on its inline axis, so its width cannot depend on its children. When the container resizes, the browser has to re-evaluate the queries for its children. In practice the cost is small, but avoid making every element a container. Only mark the components that need it.

## 206: Why can't a size container depend on its content's size?

If a container's size depended on its content, and the content's styles depended on the container's size through a query, you would get an endless loop. That is why `container-type: inline-size` applies size containment in that axis. If you use `container-type: size`, the element needs an explicit height, or it collapses to zero.

## 207: How does :has() affect performance?

`:has()` lets a parent be styled based on its descendants or siblings. The browser must re-check the parent when descendants change, which costs more than a normal selector. Browsers have optimized it a lot, so normal uses like `.card:has(img)` are fine. Avoid broad cases like `body:has(.x)` or `:has()` with deep descendant chains on large, often-changing DOMs.

## 208: What kind of :has() selectors are expensive?

Ones where the anchor is high in the tree and the argument can match many elements, for example `:root:has(.open)` or `div:has(span)`. Every DOM change anywhere below can make the browser re-check them. Use a specific anchor and a direct child or sibling relation if possible, like `.menu:has(> .item.active)`.

## 209: Is the :is() and :where() pseudo-class expensive?

No, they behave like writing the selector list out in full. The difference is specificity: `:is()` takes the highest specificity of its arguments, while `:where()` has zero specificity. `:where()` is useful for base styles that should be easy to override.

## 210: What is the cost of attribute selectors?

Simple attribute selectors like `[disabled]` or `[data-state="open"]` are fast enough for normal use. Substring matches like `[class*="col-"]` force the browser to compare strings and cannot use the class index, so they are slower in large numbers. Prefer real classes for things you style often.

## 211: What is the cost of :nth-child() selectors?

The browser needs to know an element's position among its siblings, which it usually caches. When siblings are added or removed, it may have to recheck all of them. `:nth-child(n of .selector)` adds more work. For long lists that change often, this can add style time, but for normal use it is fine.

## 212: How do you decide if a selector is slow?

Measure. Record a Performance trace with selector stats on, look at the "Recalculate Style" events and sort selectors by elapsed time. If one selector takes a large share and has many failed match attempts, rewrite it to use a specific class. If style recalc is small overall, selectors are not your problem.

## 213: What causes a full-page style recalculation?

Changes that can affect many elements: toggling a class on `html` or `body`, changing a custom property on the root, changing the viewport size (media queries), loading a new stylesheet, or a `:has()` on a high ancestor. Each forces the browser to recheck styles broadly. Keep frequent changes local to the element that changes.

## 214: How does changing a custom property on :root affect performance?

All elements inherit custom properties, so changing one on `:root` can make the browser recalculate styles for every element that uses it or inherits it. Doing that once for a theme switch is fine. Doing it on every mouse move or scroll event can be expensive. Set the variable on the smallest element that needs it.

```js
// expensive on every mousemove
document.documentElement.style.setProperty("--x", e.clientX + "px");

// better: only the element that uses it
cursor.style.setProperty("--x", e.clientX + "px");
```

## 215: What is @property and why is it useful?

`@property` registers a custom property with a type, an initial value and whether it inherits.

```css
@property --angle {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}
```

With a type, the browser can animate it (for example, a gradient angle). With `inherits: false`, changes do not flow down to all descendants, which reduces style recalculation work.

## 216: Can you animate custom properties cheaply?

You can animate registered custom properties, but they do not run on the compositor; each frame needs style recalculation and usually paint. They are handy for effects like rotating gradients, but for movement and fades, animating `transform` and `opacity` directly is cheaper.

## 217: How do you compare CSS approaches (CSS Modules, Tailwind, CSS-in-JS) for performance?

- **CSS Modules**: plain CSS output, can be split per component, no runtime.
- **Tailwind**: one small shared file that grows slowly, no runtime, bigger HTML.
- **Runtime CSS-in-JS**: extra JavaScript, style work during render, extra SSR setup.
- **Zero-runtime CSS-in-JS**: static CSS output like CSS Modules, typed API.

For speed, any of the first, second and fourth is fine; the runtime kind is the one that costs more.

## 218: How does server-side rendering interact with CSS?

With SSR, the HTML arrives already rendered, so CSS must be in the HTML response (linked or inlined) to avoid unstyled content. For CSS-in-JS, the server must collect the styles used during rendering and add them to the HTML. With streaming SSR, CSS for parts streamed later must arrive before or with those parts.

## 219: How does React 19 handle stylesheets?

React 19 lets you render `<link rel="stylesheet" href="..." precedence="default" />` inside components. React moves it to the head, removes duplicates, and with Suspense it waits for the stylesheet to load before showing the content that depends on it. That avoids FOUC when components with their own CSS stream in.

## 220: How do you avoid duplicate CSS in a micro-frontend setup?

Each micro-frontend often bundles its own copy of shared styles, like the design system. Share the design system CSS as one cached file loaded by the shell, or expose it through Module Federation as a shared dependency. Use scoped class names (CSS Modules or a prefix) so apps do not clash, and track total CSS per page in CI.

## 221: How do you lazy-load CSS for a modal in plain JavaScript?

Inject the stylesheet when the modal is first opened, and wait for it before showing.

```js
function loadCss(href) {
  return new Promise((resolve, reject) => {
    const link = document.createElement("link");
    link.rel = "stylesheet";
    link.href = href;
    link.onload = resolve;
    link.onerror = reject;
    document.head.append(link);
  });
}

openButton.addEventListener("click", async () => {
  await loadCss("/css/modal.css");
  modal.showModal();
});
```

## 222: How do you prefetch CSS for the next page?

Use `<link rel="prefetch">` for a stylesheet you expect the user to need soon. It downloads at idle, low priority and goes into the HTTP cache.

```html
<link rel="prefetch" href="/css/checkout.css" />
```

The Speculation Rules API can prefetch or prerender whole next pages, including their CSS.

## 223: What is the cost of very long class lists in HTML?

Utility classes make the HTML larger, but HTML compresses very well because the same class names repeat. The browser handles many classes on an element without problems. The real cost is usually readability, not speed. Extract repeated combinations into components, not into new CSS.

## 224: How does Sass @extend create bloated CSS?

`@extend` adds the extending selector to every rule where the extended selector appears, including nested and combined ones. Extending a common class can create huge selector lists and unexpected rules. Mixins or plain utility classes are more predictable.

```scss
.message {
  padding: 8px;
}
.error {
  @extend .message;
  color: red;
}
// .message, .error { padding: 8px; } plus every other place .message is used
```

## 225: What is the difference between @use and @import in Sass for output size?

`@import` in Sass (now deprecated) includes the file every time it is imported, so the same CSS can be output several times. `@use` loads a module only once per compilation and namespaces its members, so CSS from a shared partial is not duplicated. Migrate to `@use` and `@forward`.

## 226: How can Sass loops create too much CSS?

Loops and maps make it easy to generate hundreds of utility classes, like spacing classes for every value and breakpoint. Most of them are never used. Generate only what the design system needs, or use a tool that generates on demand like Tailwind.

## 227: How do you measure CSS size in a build?

Look at the build output (Vite and webpack print file sizes), or use tools like `source-map-explorer`, `rollup-plugin-visualizer` or webpack-bundle-analyzer. For a budget, check the compressed size, since that is what users download. `size-limit` and `bundlesize` can fail CI if CSS grows past a limit.

## 228: How do you set a CSS size budget with size-limit?

Add entries for your CSS files with a limit, and run it in CI.

```json
{
  "size-limit": [{ "path": "dist/assets/*.css", "limit": "40 kB" }]
}
```

`size-limit` measures the compressed size and fails if the file is bigger than the limit.

## 229: How do you set a performance budget in Lighthouse CI?

Lighthouse CI can check budgets for resource sizes and metrics. In `lighthouserc.json`, add assertions like:

```json
{
  "ci": {
    "assert": {
      "assertions": {
        "resource-summary:stylesheet:size": [
          "error",
          { "maxNumericValue": 50000 }
        ],
        "cumulative-layout-shift": ["error", { "maxNumericValue": 0.1 }]
      }
    }
  }
}
```

## 230: How do you stop CSS from causing a large LCP render delay?

LCP render delay is the time between the LCP resource finishing and it being painted. Render-blocking CSS that is still loading causes this delay. Reduce and inline critical CSS, remove `@import` chains, load non-critical CSS without blocking, and avoid hiding content with CSS until JavaScript runs (like A/B testing tools that hide the page).

## 231: Why do A/B testing tools hurt CSS performance?

Many client-side A/B tools add an "anti-flicker" style that hides the whole page (`opacity: 0`) until their script loads and applies the variant. If the script is slow, the page stays blank for seconds, which hurts LCP badly. Server-side or edge-based testing avoids this. If you must use it, keep the timeout short.

## 232: Why does content-visibility: auto help long pages?

On a long page, the browser normally lays out and paints everything, even sections far below the fold. With `content-visibility: auto`, it skips that work for off-screen sections until they get close. Chrome's own example showed initial rendering about 7 times faster on a long blog page. Results depend on the page, so measure.

## 233: What are the side effects of content-visibility: auto?

- Off-screen content has a placeholder size, so without a good `contain-intrinsic-size` the scrollbar jumps.
- It applies paint containment, so content cannot overflow the element's box.
- Find-in-page and anchor links still work, but the browser must render the target first.
- Scrolling quickly may show a short delay as sections render.

## 234: How does contain: layout help?

It tells the browser that the inside of the element does not affect layout outside it. When something inside changes, the browser can lay out only that element instead of walking up the tree. It also makes the element a containing block for absolute and fixed positioned children, and creates a stacking context.

## 235: How does contain: paint help?

It tells the browser that nothing inside the element is drawn outside its box, like `overflow: clip`. The browser can skip painting the inside when the element is off screen, and does not need to check children for overflow. It also creates a containing block and a stacking context.

## 236: What does contain: size do?

It tells the browser to size the element as if it had no children. The element's size must come from CSS (width and height) or it collapses. Because children cannot change its size, the browser does not need to lay out children to know the element's size. It is used for things like fixed-size widgets.

## 237: What does contain: style do?

It limits counters and quotes to the element's subtree, so changes inside do not affect counters outside. The benefit is small. It is included in `contain: content` and `strict` for completeness.

## 238: When would you use contain: strict?

When an element has a fixed size and its content is fully independent, like a chat widget, a map container, a virtualized list item with known height, or an ad slot. `strict` means `size layout paint style`, so the browser can skip almost all work for it from outside. Make sure it has explicit width and height.

## 239: How do you build a fast virtualized list?

Only render the rows in view plus a small buffer, and position them with `transform` inside a container with the full height. Libraries like TanStack Virtual handle the math. Use `contain: strict` or `content` on rows with known height so updates stay local.

```css
.list {
  position: relative;
  overflow-y: auto;
  height: 600px;
}
.row {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 48px;
  contain: strict;
}
```

## 240: When is content-visibility better than virtualization?

When you have a long but not huge page, like an article or a settings page with dozens of sections. `content-visibility` keeps all content in the DOM, so find-in-page, accessibility and SEO work, and it needs only CSS. For thousands of rows of data, virtualization is better because the DOM itself is too large.

## 241: How do you animate height smoothly?

Animating `height` triggers layout every frame. Options:

- Animate `transform: scaleY()` on a wrapper if distortion is OK.
- Use `grid-template-rows: 0fr` to `1fr`, which is still layout work but simple and fine for small elements.
- Use `interpolate-size: allow-keywords` to animate to `height: auto` (supported in Chromium browsers).

```css
.accordion {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows 0.3s;
}
.accordion.open {
  grid-template-rows: 1fr;
}
.accordion > div {
  overflow: hidden;
}
```

## 242: What is interpolate-size?

`interpolate-size: allow-keywords` lets browsers animate between a length and size keywords like `auto`, `min-content` or `fit-content`. Setting it on `:root` turns it on for the page. It still causes layout each frame, so keep it for small elements like accordions. Browsers without support just jump to the end value.

```css
:root {
  interpolate-size: allow-keywords;
}
details {
  height: 3rem;
  transition: height 0.3s;
  overflow: clip;
}
details[open] {
  height: auto;
}
```

## 243: What is the FLIP technique?

FLIP means First, Last, Invert, Play. You record an element's first position, apply the change so it moves to its last position, then use `transform` to put it back where it was (invert), and animate the transform to zero (play). This turns a layout animation into a cheap transform animation.

```js
const first = el.getBoundingClientRect();
el.classList.add("moved");
const last = el.getBoundingClientRect();
const dx = first.left - last.left;
const dy = first.top - last.top;
el.animate(
  [{ transform: `translate(${dx}px, ${dy}px)` }, { transform: "none" }],
  { duration: 300, easing: "ease-out" },
);
```

## 244: Are CSS animations faster than JavaScript animations?

Not by default. What matters is which properties you animate. CSS animations and the Web Animations API (`element.animate()`) on `transform` and `opacity` can run on the compositor. JavaScript that changes styles every frame with `requestAnimationFrame` always runs on the main thread. So CSS and WAAPI usually win for simple animations.

## 245: What is the Web Animations API?

It is the JavaScript API behind CSS animations. `element.animate(keyframes, options)` creates an animation the browser runs the same way as a CSS animation, including on the compositor for `transform` and `opacity`. You get control (pause, reverse, finished promise) without running code every frame.

```js
const anim = box.animate([{ opacity: 0 }, { opacity: 1 }], {
  duration: 200,
  fill: "forwards",
});
await anim.finished;
```

## 246: Why do some transform animations still stutter?

Common reasons: the element was not on its own layer and needed repainting when it started; the animation also changes a non-composited property; the element is very large and its texture must be re-rasterized when scaled; the device ran out of GPU memory; or the main thread was busy at the start. The Performance panel shows which one.

## 247: Why does scaling text with transform sometimes look blurry?

When an element is on its own layer, the browser may rasterize it once and then scale the bitmap, which looks blurry for text. After the animation, it usually re-rasterizes at the final size. Avoid leaving `will-change: transform` on text you scale, and do not keep big text permanently on a scaled layer.

## 248: When should you add and remove will-change?

Add it shortly before the animation (for example on hover of the parent or on `pointerdown`) and remove it after it ends. Keep it permanently only for elements that animate often, like a slide-out menu.

```js
menu.addEventListener("transitionend", () => {
  menu.style.willChange = "auto";
});
toggle.addEventListener("pointerenter", () => {
  menu.style.willChange = "transform";
});
```

## 249: What is the cost of position: sticky?

`position: sticky` is handled by the browser's scroll code and is usually cheap. Problems come when many sticky elements are stacked, when sticky elements have expensive effects like shadows or blur, or when a sticky header changes size on scroll (which triggers layout). Keep sticky elements simple.

## 250: How do you build a shrinking header without layout thrashing?

Do not change `height` or `padding` on scroll. Keep the layout the same and use `transform: scale()` or `translateY()`, or use a scroll-driven animation. If you need JavaScript, use `IntersectionObserver` on a sentinel element to toggle a class once, instead of reading `scrollY` on every scroll event.

```js
const sentinel = document.querySelector("#top-sentinel");
new IntersectionObserver(([entry]) => {
  header.classList.toggle("compact", !entry.isIntersecting);
}).observe(sentinel);
```

## 251: Why is IntersectionObserver better than scroll listeners for CSS changes?

A scroll listener fires many times per second on the main thread, and code that reads layout in it can force layouts. `IntersectionObserver` is run by the browser off the critical path and only calls you when an element crosses a threshold. It is the standard way to trigger lazy-loading, reveal animations and sticky state changes.

## 252: What is ResizeObserver and how does it help?

`ResizeObserver` tells you when an element's size changes, without polling or listening to window resize. Before container queries, it was used to add classes based on component width. Its callbacks run after layout, so reading sizes there does not force an extra layout. Today, container queries can often replace it with pure CSS.

## 253: What is the "ResizeObserver loop" error?

It appears when a ResizeObserver callback changes sizes, which triggers more resize notifications in the same frame, and the browser stops the loop to avoid hanging. It usually means your callback changes the size of what it observes. Change other elements, or defer the change with `requestAnimationFrame`.

## 254: How do you handle styles for many breakpoints without large CSS?

Use fluid values with `clamp()`, `min()` and `max()` so one rule works across sizes, instead of a new rule at every breakpoint.

```css
h1 {
  font-size: clamp(1.75rem, 1.2rem + 2.5vw, 3rem);
}
.container {
  padding-inline: clamp(16px, 5vw, 64px);
}
```

Grid with `repeat(auto-fill, minmax(240px, 1fr))` also removes many media queries.

## 255: Do clamp() and calc() cost more at runtime?

The browser computes them during style calculation, and the cost is tiny. Values that depend on the viewport are recomputed when the viewport changes, which happens rarely. They are not a performance concern in practice, and they often reduce the total amount of CSS.

## 256: How do you avoid CLS from images in CSS layouts?

Give every image or media container a known size before it loads. Use `width` and `height` attributes on `<img>` with `height: auto` in CSS, or set `aspect-ratio` on the container. For responsive art direction with `<picture>`, set dimensions on each `<source>` too, since they can have different ratios.

```html
<picture>
  <source
    media="(max-width: 600px)"
    srcset="hero-mobile.webp"
    width="600"
    height="800"
  />
  <img src="hero.webp" width="1600" height="600" alt="" />
</picture>
```

## 257: How do you reserve space for ads or embeds?

Set a `min-height` on the slot based on the most common ad size, and show a placeholder background. If the ad is smaller, the space stays; if it is bigger, it may still shift, but less. Never insert an ad at the top of the content after load without reserved space.

```css
.ad-slot {
  min-height: 250px;
  background: #f3f3f3;
}
```

## 258: Why does adding a banner at the top cause CLS?

Everything below it moves down. Even a 40 px banner can shift the whole page and give a high CLS. Either render it on the server so it is there from the start, reserve its space in CSS, or overlay it with `position: fixed` so nothing moves.

## 259: Do transform animations count as layout shift?

No. CLS only counts changes in the layout position of elements. Moving something with `transform` does not change its layout position, so it does not count. Changing `top`, `margin` or `height` does count if it moves other visible content without user input.

## 260: Do layout shifts after user input count toward CLS?

Shifts within 500 ms after a discrete user input (click, tap, key press) are excluded, because the user expects something to change. Scrolling and hovering are not counted as such input. So an accordion opening on click is fine, but content shifting while the user scrolls is counted.

## 261: How do you debug which element caused a layout shift?

In the Performance panel, click a layout shift in the Layout shifts track to see which nodes moved and by how much. The Rendering tab's "Layout Shift Regions" highlights them live. In code, a `PerformanceObserver` for `layout-shift` entries gives `sources` with the shifted nodes.

```js
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    if (!entry.hadRecentInput) {
      console.log(
        entry.value,
        entry.sources?.map((s) => s.node),
      );
    }
  }
}).observe({ type: "layout-shift", buffered: true });
```

## 262: How do you measure Core Web Vitals in real users?

Use the `web-vitals` JavaScript library, which reports LCP, CLS and INP from real users with the same rules Google uses. Send the values to your analytics. The attribution build tells you which element was the LCP, which element shifted, and what caused a slow interaction.

```js
import { onLCP, onCLS, onINP } from "web-vitals/attribution";

onCLS((metric) => sendToAnalytics(metric));
onLCP((metric) => sendToAnalytics(metric));
onINP((metric) => sendToAnalytics(metric));
```

## 263: What is the Chrome UX Report?

CrUX is a public dataset of real-user performance from Chrome users who opted in. It has Core Web Vitals per origin and for popular URLs. PageSpeed Insights, Search Console and the CrUX dashboard and API show it. It updates over a 28-day window, so changes take time to show.

## 264: How do you check if CSS is the reason for a slow LCP?

Break LCP into parts: time to first byte, resource load delay, resource load time and element render delay. Lighthouse and the Performance panel show this. If render delay is large and the LCP resource finished early, the page is likely waiting on render-blocking CSS or fonts. The network waterfall will show CSS still loading at that time.

## 265: Why is it a problem when CSS is loaded from a different domain?

The browser needs a new DNS lookup, TCP connection and TLS handshake before downloading, which can add 100-300 ms on mobile. For render-blocking CSS, that delay adds directly to first paint. Host CSS on the same domain as the HTML, or at least `preconnect` to the CSS domain.

## 266: How many render-blocking stylesheets is too many?

There is no fixed number, but each one is a request the first paint depends on. If they are on the same domain over HTTP/2, a few small files are fine. Watch for files from other domains, files that load late because of `@import`, and very large files. Lighthouse lists each render-blocking file and its cost.

## 267: How do you handle CSS for above-the-fold content in a framework like Next.js?

Next.js automatically extracts CSS from CSS Modules, global CSS and Tailwind into files linked in the head, and splits it by route. In the App Router, CSS imported in a layout or page is loaded for that segment. You can turn on `experimental.inlineCss` to inline CSS into the HTML instead of linking it, which can help first-visit LCP but hurts caching across pages.

## 268: How does Angular handle critical CSS?

Angular's build inlines critical CSS for server-rendered and prerendered pages by default (using Beasties), and loads the rest of the global stylesheet asynchronously. You can control it with the `optimization.styles.inlineCritical` option in `angular.json`. Component styles are bundled with each component and scoped by default.

## 269: How does Astro handle CSS?

Astro scopes `<style>` blocks in components and bundles them per page. Small stylesheets are inlined into the HTML by default, larger ones are linked. You can control this with `build.inlineStylesheets` (`auto`, `always` or `never`). Since Astro ships no JavaScript by default, CSS is often the main render-blocking resource.

## 270: What is Vite's cssCodeSplit option?

`build.cssCodeSplit` is `true` by default. It makes CSS imported in async chunks get its own CSS file, loaded together with the chunk. If you set it to `false`, all CSS goes into one file. Keep it on unless you have a reason, like a library build that needs one stylesheet.

## 271: How do you use Lightning CSS in Vite?

Set the CSS transformer and minifier in the config.

```js
// vite.config.js
import { defineConfig } from "vite";

export default defineConfig({
  css: {
    transformer: "lightningcss",
  },
  build: {
    cssMinify: "lightningcss",
  },
});
```

It reads your Browserslist targets (through `css.lightningcss.targets`) to decide what to prefix and lower. Note that it replaces PostCSS, so PostCSS plugins will not run.

## 272: What is the difference between cssnano presets?

cssnano has a `default` preset with safe transforms (removing whitespace, comments, merging longhands, shortening colors). The `advanced` preset adds riskier ones like merging identical rules across the file, reducing `z-index` and changing identifier names, which can break some sites. Start with `default` and test before using `advanced`.

## 273: How do you remove unused CSS in a Vite project?

If you use Tailwind, it already generates only used classes. For other CSS, use a PostCSS plugin like `@fullhuman/postcss-purgecss` in production, pointing it at your templates, and keep a safelist for dynamic classes. Check the result visually, since text-based scanning can miss classes.

## 274: How do you deal with unused CSS coming from a component library?

Import only the components you use instead of the full library CSS, if the library supports it. Many libraries ship per-component CSS or let you import partial Sass. If it only ships one big file, consider PurgeCSS with a careful safelist, or switch to a library with better tree-shaking.

## 275: Can CSS be tree-shaken like JavaScript?

Not in the same way. JavaScript bundlers can follow imports and exports, but CSS rules apply by matching HTML that may be generated at runtime, so tools cannot always prove a rule is unused. Tools like PurgeCSS guess from text. Component-scoped CSS (CSS Modules, zero-runtime CSS-in-JS) gets you closest, because a component's CSS is dropped when the component is not imported.

## 276: What is atomic CSS?

Atomic CSS means each class does exactly one thing, like `.mt-4 { margin-top: 1rem }`. Tailwind is a utility framework built on that idea, and some tools (StyleX, Fela, Griffel) generate atomic classes from component styles. The CSS file size stops growing much as the app grows, because the same small set of classes is reused.

## 277: How does StyleX produce small CSS?

StyleX compiles styles written in JavaScript into atomic CSS classes at build time and merges them into one file. Each property-value pair becomes one class, reused across the whole app. Meta built it because their CSS grew too large with per-component styles. It has a tiny runtime for merging class names, but no runtime style injection.

## 278: How should you handle critical CSS for a page with many layouts?

Generate critical CSS per template or route, not once for the whole site. A product page and a blog post need different above-the-fold styles. Tools like `critical` and Beasties can run per page during the build. For server-rendered apps with streaming, framework-level inlining per route is easier than a separate tool.

## 279: What is the risk of inlining too much CSS?

The HTML gets bigger, so the first bytes of content arrive later, and the inlined CSS is downloaded again on every page view because it is not cached separately. Repeat visitors pay that cost every time. Keep inlined CSS to the first screen, or only inline on the first visit (using a cookie) and link the cached file after that.

## 280: How do you load CSS differently for first and repeat visits?

On the first visit, inline critical CSS and load the full file asynchronously, then set a cookie. On later visits, the server sees the cookie and just links the full file, which is already cached. This is an older technique and needs care with caches, but it can work well for content sites.

## 281: Why does a slow CSS file sometimes block the whole page on mobile but not desktop?

Mobile networks have higher latency and less bandwidth, so the same CSS takes much longer to arrive. Mobile CPUs are also slower at parsing. A 100 KB CSS file that takes 50 ms on desktop can take over a second on a mid-range phone on 4G. That is why you should always test on throttled or real mobile setups.

## 282: How do you handle CSS for third-party widgets like chat?

Load the widget and its CSS only after the main content has rendered, or only after user interaction (like clicking a "Chat" button that you draw yourself). Use a lightweight placeholder that looks like the real button. This keeps third-party CSS out of the critical path.

## 283: What is the facade pattern for embeds?

A facade is a lightweight placeholder that looks like the real embed (a YouTube player, a map, a chat button) but loads only a static image and a bit of CSS. The real, heavy embed with its scripts and styles loads only when the user clicks. `lite-youtube-embed` is a well known example.

## 284: How does a CSS framework's JavaScript plugin affect performance?

Frameworks like Bootstrap include JavaScript for dropdowns, modals and tooltips. Loading all of it adds script parse and run time. Import only the plugins you use, or replace them with native HTML features like `<dialog>`, `<details>` and the Popover API, which need no JavaScript library.

## 285: How does the Popover API reduce CSS and JS?

The `popover` attribute gives you a top-layer element that opens and closes with light dismiss, keyboard support and no z-index problems, all built into the browser. You do not need a library or custom stacking hacks. Combined with CSS anchor positioning, you can position tooltips and menus without JavaScript measurement.

```html
<button popovertarget="menu">Open</button>
<div id="menu" popover>Menu content</div>
```

## 286: What is CSS anchor positioning and why is it faster than JS positioning?

Anchor positioning lets you place an element relative to another one with CSS (`anchor-name`, `position-anchor`, `position-area`). JavaScript positioning libraries measure both elements with `getBoundingClientRect()`, often on scroll and resize, which forces layout. With CSS, the browser positions it during its normal layout. Check browser support and keep a fallback.

```css
.trigger {
  anchor-name: --trigger;
}
.tooltip {
  position: absolute;
  position-anchor: --trigger;
  position-area: top;
}
```

## 287: How do you style a large table without slowing down the page?

- Use `table-layout: fixed` so the browser does not have to read all rows to size columns.
- Keep cell styles simple and avoid shadows on every cell.
- Virtualize rows if there are thousands.
- Use `content-visibility: auto` on groups of rows if virtualization is too much work.

```css
table {
  table-layout: fixed;
  width: 100%;
}
```

## 288: Why does table-layout: fixed help?

With the default `auto` layout, the browser looks at the content of every cell in every row to decide column widths, and may recalculate when rows are added. With `fixed`, it uses the first row and the table width, so layout is faster and stable as more rows load.

## 289: What CSS should you avoid on elements inside a scrolling list?

Avoid large `box-shadow` blur, `filter`, `backdrop-filter`, `mix-blend-mode` and huge `border-radius` with overflow clipping on every item. These make each item expensive to paint, and scrolling forces painting new items. Use simpler effects or put the effect on one container instead of hundreds of children.

## 290: Is mix-blend-mode expensive?

It can be. Blending needs the browser to know what is behind the element, which can force extra layers and more paint and composite work. On large areas or animated content, it can drop frames, especially on mobile. Use it sparingly and test.

## 291: How do you audit animation performance in DevTools?

Open the Animations panel to see all running CSS animations and transitions and slow them down. Record a Performance trace while they run and check that the frames are green (on time), not red. If you see Layout or Paint every frame for an animation, it is not composited. Lighthouse also lists non-composited animations with the reason.

## 292: Why might an opacity animation not be composited?

For example, if the element does not have its own layer and the browser decides it is cheaper to repaint, or if the animation is combined with a non-composited property in the same keyframes, or if the element has certain effects. Chrome's DevTools explains the reason in the "Avoid non-composited animations" audit and in the Animations details.

## 293: What is the cost of many small CSS animations at once?

Each running animation needs work every frame, even if it is composited. Dozens of small animations (like pulsing dots, shimmer placeholders) can add up, especially if they cause paint. Pause what is not visible, limit infinite animations, and use one shared animation instead of many independent ones where possible.

## 294: How do you build a cheap skeleton loading shimmer?

Animate `transform` on a pseudo-element with a gradient, instead of animating `background-position`, which repaints.

```css
.skeleton {
  position: relative;
  overflow: hidden;
  background: #e5e5e5;
}
.skeleton::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(
    90deg,
    transparent,
    rgb(255 255 255 / 0.5),
    transparent
  );
  transform: translateX(-100%);
  animation: shimmer 1.5s infinite;
}
@keyframes shimmer {
  to {
    transform: translateX(100%);
  }
}
```

## 295: How do you check the CSS of a page for size issues quickly?

Run Project Wallace or CSS Stats on the URL to see total size, number of rules, selectors, unique colors and font sizes, specificity graphs and `!important` count. Combine it with the Coverage panel for unused CSS and the Network panel for compressed sizes.

## 296: How do you stop CSS from growing over time in a big team?

- Use a design system with tokens and shared components.
- Use scoped CSS (Modules or utilities) so dead CSS is easy to delete.
- Run stylelint with rules for specificity and nesting.
- Track CSS size per page in CI with a budget.
- Delete styles together with the components that use them.

## 297: Why is global CSS hard to delete?

You cannot be sure what uses a global class. It might be used in a template, a CMS article, an email, or added by JavaScript. Developers are afraid to delete it, so it stays forever and grows. Scoped CSS ties styles to a component, so when the component is removed, its CSS goes with it.

## 298: What is the cost of loading the same font from two different CSS files?

If two stylesheets declare the same font with different URLs (for example a CDN version and a self-hosted one), the browser downloads both. Check the Network panel for duplicate fonts and make sure only one `@font-face` per font file exists.

## 299: How do icon fonts affect render performance?

The browser must download the whole font before it can draw any icon, and until then icons are invisible or show wrong characters. Large icon fonts with hundreds of icons waste bytes. Switching to inline SVG or an SVG sprite with only the used icons removes the font download and the flash.

## 300: How would you explain to a junior developer what to watch for in CSS performance?

Keep it simple. Ship less CSS and make sure the first screen's styles load fast. Do not use `@import` in plain CSS. Set sizes on images so nothing jumps. Animate only `transform` and `opacity`. Do not read layout values right after changing styles in JavaScript. And always measure in DevTools before and after a change.

# Advanced Questions (301-450)

## 301: Walk through the full rendering pipeline in Chrome from a style change to pixels.

1. **Style**: the browser marks the changed element (and maybe others) as needing style recalc and computes new computed styles.
2. **Layout**: if a geometry-related property changed, it updates the layout tree (sizes and positions).
3. **Pre-paint**: it updates property trees (transform, clip, effect, scroll) and decides what must be repainted.
4. **Paint**: it records drawing commands into display lists, not pixels yet.
5. **Commit**: it sends the layer and property tree data to the compositor thread.
6. **Layerize, raster and composite**: tiles are rasterized (usually on the GPU) and the compositor draws the frame.

A change can skip steps: `color` skips layout, `transform` on a composited layer can skip layout and paint.

## 302: What runs on the main thread and what runs on the compositor thread?

The main thread runs JavaScript, style, layout, pre-paint and paint (recording). The compositor thread handles scrolling, composited animations of `transform`, `opacity` and some `filter`s, and assembling frames. Rasterization happens on separate raster threads or the GPU process. That is why composited animations keep running when JavaScript blocks the main thread.

## 303: What are property trees in Chrome?

Instead of keeping a deep tree of layers where each layer stores its own transform, clip and effect, Chrome keeps four separate trees: transform, clip, effect and scroll. Each paint chunk points to nodes in those trees. That makes it cheap to update a transform or opacity without repainting, and it lets the compositor work with fewer layers.

## 304: What is RenderingNG?

It is the name for Chrome's rebuilt rendering architecture, finished around 2021. It includes LayoutNG (a new layout engine), BlinkNG (cleaner pipeline stages), Composite After Paint, the GPU raster and display compositor (Viz), and other parts. For developers, it means more predictable performance and features like container queries and `content-visibility` being possible.

## 305: What is Composite After Paint?

It is a Chrome change where layer decisions are made after paint instead of before. Before, the browser decided early which elements got layers, which caused problems like layer explosion and wrong layer squashing. Now paint produces paint chunks with property tree states, and layerization groups them afterward. It cut memory use and fixed many correctness bugs.

## 306: What is layer explosion?

It is when the browser creates hundreds or thousands of compositor layers. It can happen when one element is promoted and many elements that overlap it must also be promoted to keep the right drawing order. Each layer uses GPU memory and adds compositing work. Composite After Paint reduced this, but heavy `will-change` use can still create too many layers.

## 307: Why can overlap cause unexpected layer promotion?

If element A is on its own layer and element B is drawn on top of it in paint order, B cannot be painted into the layer below A, or the order would be wrong. So the browser gives B a layer too, or squashes it with others. A single promoted element low in the stacking order can force many elements above it into layers.

## 308: What is layer squashing?

When several elements need their own layer only because of overlap, the browser may squash them into one shared layer instead of creating many. This saves memory. Certain conditions prevent squashing, such as different transforms or clipping, in which case you get many layers. The Layers panel shows the reason for each layer.

## 309: How do you estimate the GPU memory cost of a layer?

Roughly width times height times 4 bytes (RGBA). A full-screen layer on a 1440 x 3120 phone screen at device pixel ratio is about 1440 × 3120 × 4 ≈ 18 MB. Ten of those use about 180 MB, which can be too much for a mid-range phone. The browser tiles large layers and only rasterizes visible tiles, but the cost is still real.

## 310: What is rasterization and why does it matter?

Rasterization turns paint commands into pixels. Chrome splits layers into tiles and rasterizes them on raster threads, usually on the GPU. During fast scrolling, if tiles are not rasterized in time, you see blank areas (checkerboarding). Expensive paint operations like large blurs and complex gradients make rasterization slower.

## 311: What is checkerboarding?

When the user scrolls faster than the browser can rasterize new tiles, parts of the page show empty or placeholder areas for a moment. It shows that raster work is too heavy for the device. Simpler paint (fewer big blurs, shadows and filters) and fewer giant layers help.

## 312: How does paint invalidation work?

When a style changes, the browser marks the areas of the page that need repainting. It tries to repaint only those display items or rectangles. Some changes invalidate large areas, for example changing a background on a big container, or changes inside an element with a blend mode. Paint flashing in DevTools shows the invalidated areas.

## 313: How does style invalidation work in modern browsers?

Browsers build invalidation sets from your selectors. For example, for `.open .item`, they note that if `.open` is added or removed on an element, descendants with class `item` need new styles. When a class changes, they look up the set and only restyle the matching elements instead of the whole subtree. Selectors that are hard to index, like `.open *`, force broader invalidation.

## 314: Why can a selector like .active * be expensive?

The invalidation set for `.active` says "all descendants". So toggling `.active` on a big container makes the browser recalculate the style of every element inside it. A selector like `.active > .icon` gives a narrow set, so only the direct child icons are restyled.

## 315: What are sibling invalidation and why can it be costly?

Selectors with `+` and `~` mean a change on one element can affect its later siblings. For `.a ~ .b`, adding `.a` to an element can require rechecking all following siblings with class `b`. In long lists that change often, this adds up. Prefer parent or child relations for frequent changes.

## 316: How does the browser optimize :has() invalidation?

Browsers keep track of which elements could be affected by `:has()` arguments and only recheck anchors when a relevant change happens in the right place (descendant, child or sibling). They also cache results during a style pass. Still, `:has()` with a broad anchor can force rechecks on many changes, so the shape of the selector matters.

## 317: What are Bloom filters used for in selector matching?

When matching descendant selectors like `.nav a`, the browser needs to know if any ancestor has class `nav`. Engines keep a Bloom filter of ancestor ids, classes and tags as they walk down the tree. It can quickly say "no ancestor has `.nav`", so the full ancestor walk is skipped for most elements. That is why descendant selectors are usually cheaper than people think.

## 318: What is the style sharing cache?

Browsers can reuse computed style between elements that are similar, for example siblings with the same tag, classes and parent style and no inline style. If two `<li class="item">` elements in a list match the same rules, the second can share the first one's computed style instead of matching all rules again. Unique inline styles and certain selectors (like `:nth-child`) can break sharing.

## 319: How do inline style attributes affect style sharing?

Elements with different inline `style` attributes cannot share computed styles, because each one has unique declarations. In a list of thousands of items, each with its own inline style, the browser must compute every style separately. Use classes for shared styles and inline styles only for truly unique values.

## 320: How does inheritance of custom properties affect style performance?

Every custom property defined on an element is inherited by all descendants by default. Browsers store inherited custom properties efficiently, but changing a value on an ancestor means descendants must update their computed values. Hundreds of custom properties on `:root` that change often can make every style recalculation slower. Register frequently changed properties with `inherits: false` when they are local.

## 321: What is the cost of defining hundreds of custom properties on :root?

Each element inherits all of them, so the browser carries a large set of variables through the tree. Modern engines share the inherited set between elements that did not change it, so the cost is mostly when values change or when many elements override them. Design systems with thousands of tokens should only expose the ones used in CSS at runtime, and inline constants at build time where possible.

## 322: When would you resolve design tokens at build time instead of using custom properties?

For values that never change at runtime, like most spacing and radius values, build-time constants (Sass variables or a token pipeline) produce plain values with no runtime work. Keep custom properties for things that change at runtime, like themes, user settings or component-level overrides. This keeps the runtime variable set small.

## 323: How does the CSSOM API affect performance when you insert rules?

`sheet.insertRule()` adds a rule to an existing stylesheet. It is fast, but each insert can invalidate styles and cause a style recalc on the next frame. Inserting rules one by one during rendering, as some CSS-in-JS libraries do, can cause many recalcs. Batch inserts, or insert all rules before elements that need them are added to the DOM.

## 324: What are constructable stylesheets?

They let you create a `CSSStyleSheet` in JavaScript and share it between documents and shadow roots with `adoptedStyleSheets`, without adding `<style>` tags.

```js
const sheet = new CSSStyleSheet();
sheet.replaceSync(".btn { padding: 8px; }");
shadowRoot.adoptedStyleSheets = [sheet];
```

One parsed sheet can be used by hundreds of web components, so the browser parses it once and saves memory.

## 325: Why are constructable stylesheets better than a style tag in every shadow root?

With a `<style>` in each shadow root, each component instance would contain its own copy of the text. Browsers can cache identical style text, but adopted sheets make sharing explicit: one object, parsed once, shared by reference. Updates to the shared sheet apply to all components at once.

## 326: How does Shadow DOM affect style performance?

Shadow DOM scopes styles, so rules inside a shadow root only match elements inside it. That makes the set of rules to check per element smaller. On the other hand, many shadow roots each with their own style rules add memory and setup cost. Sharing sheets with `adoptedStyleSheets` and keeping component CSS small helps.

## 327: What is useInsertionEffect in React and why does it exist?

It is a React hook that runs before layout effects and before the browser reads layout. CSS-in-JS libraries use it to insert style rules before any component reads layout in `useLayoutEffect`. Inserting rules during render or later could force extra style recalcs and layouts. It is meant for library authors, not app code.

## 328: How do runtime CSS-in-JS libraries handle SSR, and what is the cost?

On the server, the library collects styles generated while rendering each component and returns them as a `<style>` tag or file to put in the HTML. On the client, it hydrates by reading those styles so it does not insert them again. This needs extra setup with streaming SSR, and the library's JavaScript still runs on the client, adding to hydration cost.

## 329: Why do many teams move away from runtime CSS-in-JS with React Server Components?

Server Components do not run on the client and cannot use React context or hooks, which most runtime CSS-in-JS libraries rely on. Styles in Server Components need a build-time solution (CSS Modules, Tailwind, zero-runtime CSS-in-JS). That plus the runtime cost pushed many teams and libraries toward static extraction.

## 330: How does streaming SSR interact with stylesheets?

With streaming, HTML arrives in chunks. If a chunk contains a component whose CSS is not yet loaded, it would show unstyled. React 19 with `precedence` on stylesheet links holds back revealing a Suspense boundary until its stylesheets load. Without such support, you must load all CSS in the head before streaming, which can block earlier.

## 331: How do you find CSS that causes slow INP?

Collect INP with the `web-vitals` attribution build, which reports the interaction target, the timing breakdown and Long Animation Frame data. If presentation delay is large, look at the LoAF entry for big `styleAndLayoutStart` gaps. Then reproduce in the Performance panel and check which Recalculate Style and Layout events follow the interaction.

## 332: What is the Long Animation Frames API?

It reports frames that took more than 50 ms, with details on scripts that ran and when style and layout started. Each entry has fields like `renderStart`, `styleAndLayoutStart` and a list of `scripts`. The difference between `styleAndLayoutStart` and the frame end gives a rough idea of how much time went to style and layout.

```js
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    const styleLayout =
      entry.startTime + entry.duration - entry.styleAndLayoutStart;
    console.log("frame", entry.duration, "style+layout", styleLayout);
  }
}).observe({ type: "long-animation-frame", buffered: true });
```

## 333: How do you measure the effect of a CSS change in production?

Ship it behind a flag or to a portion of users, and compare Core Web Vitals and custom timings (like LCP render delay and INP presentation delay) between groups with RUM. Lab tests show direction, but CSS effects depend a lot on device, so field data is the final check. Watch at least the 75th percentile, since that is what Core Web Vitals use.

## 334: How does devicePixelRatio affect CSS paint cost?

On a 3x screen, each CSS pixel is 9 device pixels. Paint, raster and GPU memory scale with device pixels, so an effect that is cheap on a 1x desktop screen can be 9 times more work on a phone. Large blurs and full-screen layers are where this hurts most.

## 335: How do you handle a page that is janky on scroll only on low-end Android?

Record a trace on a real device with `chrome://inspect`. Look at the frames: if raster or GPU time is high, reduce paint complexity (shadows, blurs, big gradients, huge images) and the number of layers. If main thread time is high, find scroll handlers or layout changes. Also check GPU memory in the Layers panel; low-end devices hit memory limits fast.

## 336: When does a transform animation fall back to the main thread?

In Chrome, composited animations can fall back when the element has certain effects or when keyframes include a non-composited property, when the animation uses some timing functions or features the compositor does not support, or when the target is not in a layer that can be animated on its own. DevTools lists the reason. Firefox and Safari have their own rules, so test in each.

## 337: How do scroll-driven animations run off the main thread?

When the animation only changes compositor-friendly properties and uses a scroll or view timeline, the browser can sample the scroll offset on the compositor and update the animation there. The main thread only sets it up. If the animation affects layout properties, it has to run on the main thread and gets the same problems as scroll listeners.

## 338: How do you provide a fallback for scroll-driven animations?

Use `@supports (animation-timeline: scroll())` to apply them only in browsers that support them. Without support, show the final state or use a simple `IntersectionObserver`-based class toggle. The scroll-timeline polyfill exists, but it runs on the main thread, so it loses the main benefit.

```css
@supports (animation-timeline: view()) {
  .reveal {
    animation: fade-in linear both;
    animation-timeline: view();
    animation-range: entry 0% cover 30%;
  }
}
```

## 339: How do view transitions take snapshots, and what does it cost?

For each element with a `view-transition-name`, and for the root, the browser captures the old state as an image, then renders the new state as live content. Both are placed in a pseudo-element tree and animated. Capturing costs paint and GPU memory proportional to the size of the captured elements, and the page is not interactive during the transition.

## 340: What makes view transitions slow, and how do you fix it?

Too many named elements, very large snapshots (like a long scrolled page), long animations, and heavy DOM updates inside the update callback. Fixes: name only the elements that need their own animation, keep animations under about 300 ms, keep the update callback fast, and skip transitions on low-end devices or when `prefers-reduced-motion` is set.

## 341: How does content-visibility: hidden differ from display: none?

Both hide content, but `content-visibility: hidden` keeps the element's rendering state cached, so showing it again is fast. `display: none` throws away layout and has to redo it when shown. That makes `content-visibility: hidden` good for things like inactive tabs in a single-page app that you switch between often.

## 342: How does content-visibility: auto affect accessibility?

Skipped content stays in the DOM and in the accessibility tree, so screen readers can still find it. Early implementations had issues with headings and landmarks not exposed. One thing to watch: if you also use `display: none` or `visibility: hidden` inside, those still hide content as usual. Test with a screen reader if the content is important.

## 343: What is contain-intrinsic-size: auto and how does it remember sizes?

With `auto`, once the element has been rendered and laid out, the browser remembers its last real size and uses that as the placeholder when it is skipped again. Until then, it uses the value you provided. This makes the scrollbar stable after the user has scrolled past sections.

```css
.feed-item {
  content-visibility: auto;
  contain-intrinsic-size: auto 400px;
}
```

## 344: How do you detect when content-visibility skips or renders an element?

Listen for the `contentvisibilityautostatechange` event, which fires when the element starts or stops being skipped. You can use it to pause or resume work inside, like canvas drawing or animations.

```js
section.addEventListener("contentvisibilityautostatechange", (e) => {
  if (e.skipped) stopAnimation();
  else startAnimation();
});
```

## 345: Why does content-visibility sometimes make performance worse?

If sections are small, the overhead of tracking and containing them can be more than what you save. If `contain-intrinsic-size` is far from the real size, the browser renders sections, finds they are a different size, and adjusts the scroll, which can look jumpy. Also, reading layout of skipped content from JavaScript forces it to render. Measure before and after.

## 346: How do you design a CSS architecture for a large app with good performance?

- Small global layer: reset, tokens, base typography.
- Component styles scoped (CSS Modules or zero-runtime CSS-in-JS) and loaded with the component.
- Utility classes for layout and spacing, from a single shared file.
- Cascade layers to order reset, base, components and utilities.
- Critical CSS generated per route, the rest split and lazy-loaded.
- Budgets and stylelint in CI.

## 347: How do you migrate a legacy app with a 1 MB CSS file?

Start with measurement: Coverage per main page, a list of selectors and where they are used. Then:

1. Split out styles per page or area into separate files.
2. Remove clearly dead CSS (old pages, unused framework parts).
3. Put the legacy CSS into a low cascade layer so new code can override it without specificity fights.
4. Write all new components with scoped CSS.
5. Delete legacy rules as their pages are rebuilt.

Track the size in CI so it only goes down.

## 348: How do you safely remove CSS in a site where HTML comes from a CMS?

Text-based tools cannot see classes typed into CMS content. Export the CMS content and scan it for class names, add those to the safelist, and log class usage in production with a small script that collects class names on real pages. Remove rules in small steps and compare screenshots with visual regression tests.

## 349: How do visual regression tests help CSS optimization?

When you remove unused CSS, change selectors, or inline critical CSS, you can break layouts without noticing. Tools like Playwright screenshots, Percy, Chromatic or BackstopJS take screenshots before and after and show differences. That gives you confidence to delete CSS aggressively.

## 350: How do you decide between inlining all CSS and linking it?

Inline everything when total CSS is very small (a few KB compressed) and pages are mostly first visits, like landing pages. Link with caching when CSS is larger and users visit many pages, because the cached file is reused. In between, inline critical CSS and link the rest. Measure LCP on first and repeat visits for both options.

## 351: How does the browser prioritize CSS downloads?

In Chrome, stylesheets in the head get the highest priority. Stylesheets with a non-matching `media` attribute get the lowest. Preloaded styles are high. Late-discovered CSS from `@import` keeps a high priority but starts late. Images in CSS are low priority by default. You can see priorities in the Network panel's Priority column.

## 352: How does a stylesheet in the body behave in modern Chrome?

A `<link rel="stylesheet">` in the body blocks rendering of content after it, but content before it can be painted. This lets you put a component's CSS right before the component. It works in Chrome and Firefox, but it can cause a visible shift when later content appears, and it was used more in the HTTP/2 era of "progressive CSS".

## 353: What is the blocking="render" attribute?

It lets you mark a resource as render-blocking explicitly, for example a script or a style that would not block on its own.

```html
<script blocking="render" src="/theme.js" async></script>
```

It is useful when a small script must run before first paint, like setting the theme class to avoid a flash. Use it sparingly, since it delays first paint. Browser support is mainly in Chromium.

## 354: How do you avoid a theme flash with server-side rendering?

If the theme is stored in localStorage, the server does not know it. Options: store it in a cookie so the server renders the right class; or run a tiny inline script in the head that sets the class before the body renders. Combine with `color-scheme` so the browser background is right from the first paint.

```html
<script>
  const t = localStorage.getItem("theme");
  if (t) document.documentElement.dataset.theme = t;
</script>
```

## 355: How do CSS and the HTML parser interact with scripts in the head?

The HTML parser can continue past a stylesheet, but a parser-blocking script after a stylesheet must wait until that stylesheet loads, because the script might ask for computed styles. So: CSS blocks the script, and the script blocks the parser. That chain is why a slow stylesheet in the head can delay everything after it.

## 356: What happens if a stylesheet fails to load or hangs?

If it fails (404 or network error), the browser renders without it. If the server hangs and never finishes, the browser keeps waiting and the page stays blank until a timeout, which can take a long time. That is why third-party render-blocking CSS is a risk, and why a CDN with good timeouts matters.

## 357: How do you protect the page from a slow third-party stylesheet?

Do not put it in the critical path. Load it asynchronously with the `media` swap pattern, or self-host a copy so it is on your own infrastructure. If it must block, set up monitoring for its availability. For fonts from third parties, `font-display` prevents invisible text if the font is slow.

## 358: How does the font matching process decide which fonts to download?

The browser only downloads a font when an element with visible text needs that `font-family`, `font-weight` and `font-style`, and when the characters match its `unicode-range`. Declaring `@font-face` alone does not download anything. That is why unused faces are free, and why a bold font loads late when only one bold word appears deep in the page.

## 359: What is font synthesis and when does it matter for performance?

If a font face is missing, like bold or italic, the browser fakes it by thickening or slanting the regular face. This avoids a download but looks worse. You can control it with `font-synthesis: none` to prevent fake styles. Sometimes letting the browser synthesize a rarely used italic is a reasonable trade-off to avoid another font file.

## 360: How do variable fonts compare to static fonts in total bytes?

A variable font with a weight axis is often 1.5 to 2 times the size of a single static weight. If you use only one or two weights, static files are smaller. If you use three or more, or you want smooth weight animation, variable fonts usually win. Subsetting a variable font to the characters you need also matters a lot.

## 361: How do you subset a variable font while keeping axes?

Use fonttools. `pyftsubset` keeps variation tables by default, and `fonttools varLib.instancer` can limit an axis range (for example weight 400-700) to make the file smaller.

```bash
fonttools varLib.instancer Inter.ttf wght=400:700 -o Inter-400-700.ttf
pyftsubset Inter-400-700.ttf --unicodes="U+0000-00FF" --flavor=woff2 --output-file=inter-latin.woff2
```

## 362: Why might preloading a font hurt performance?

A preload gets high priority and competes with the CSS itself and the LCP image. If you preload fonts that are not used above the fold, or several weights, you slow down what matters. Preloading the wrong URL (different file than the CSS uses) means two downloads. Preload only one or two fonts that are used in the first screen.

## 363: How do you choose between font-display swap and optional for a brand-heavy site?

`swap` always shows the brand font eventually but can cause a shift when it swaps. `optional` never shifts but might show the fallback on the first visit on a slow network. For headings that define the brand look, `swap` with a tuned fallback is common. For body text, `optional` plus a preload often gives the best mix of speed and stability.

## 364: What is the cost of very large CSS files on parsing?

Parsing CSS is fast, often many megabytes per second on desktop, but on low-end phones a few hundred KB can take tens of milliseconds or more, all on the main thread before first paint. Some browsers parse stylesheets off the main thread in some cases, but the CSSOM is still needed before render. Shipping less CSS is the only reliable fix.

## 365: Does the browser cache parsed CSS?

Partly. Browsers keep the bytes in the HTTP cache, and they can reuse parsed stylesheet data in memory in some cases, for example when the same stylesheet or identical `<style>` text is used several times in a page. In an SPA, CSS stays parsed for as long as the page lives. But on a normal page load, you should assume the CSS is parsed again, so file size still matters.

## 366: How do you profile CSS parsing time?

In the Performance panel, look for "Parse Stylesheet" events on the main thread during load. Long ones point to big files. Also compare the time between the CSS response end and first paint. If parsing is a noticeable part, cut the size or split the file.

## 367: How does the number of DOM elements affect style recalculation cost?

Style recalc work grows with the number of elements that need new styles times the number of rules to check for each. Invalidation sets and caches reduce how many elements are touched, but on a page with 10,000+ elements, broad changes can take tens of milliseconds. Fewer elements and narrower invalidation are the main levers.

## 368: How does DOM depth affect layout?

Layout mostly walks down the tree, but some layouts need multiple passes, like flexbox with flexible children or grid with intrinsic sizing, where children may be measured more than once. Deep nesting of such containers can multiply layout work. LayoutNG caches results to limit this, but flat structures are still cheaper.

## 369: What layouts are known to be expensive?

- Nested flex containers where sizes depend on content (`flex-basis: auto` with content-based sizing).
- Grid with `auto` or `min-content` tracks over many items.
- Tables with `table-layout: auto`.
- Text with complex scripts or many font changes.
- Anything that depends on percentage heights through many levels.

Setting explicit sizes or using `contain` reduces the work.

## 370: How can intrinsic sizing in grid hurt performance?

Tracks like `auto`, `min-content`, `max-content` and `fit-content` need the browser to measure the content of every item in the track. With many items, especially if they have nested flex or text, that can take a long time and must be redone when content changes. Fixed sizes or `minmax(0, 1fr)` avoid measuring.

## 371: Why use minmax(0, 1fr) instead of 1fr in grid?

`1fr` means `minmax(auto, 1fr)`, so the track cannot be smaller than its content's minimum size. The browser has to measure content, and long words or wide images can stretch tracks. `minmax(0, 1fr)` ignores content minimums, giving predictable equal columns and less measuring.

## 372: How do flex items cause multiple layout passes?

With `flex-basis: auto` and no explicit width, the browser first measures the item's content to find its hypothetical size, then flexes it, and sometimes lays it out again at the final size. Nested flex containers repeat this inside. Setting `flex-basis` explicitly (like `flex: 1 1 0`) or giving fixed sizes reduces measuring.

## 373: What is the cost of percentage heights?

A percentage height needs the parent's height to be known. If the parent's height depends on its content, the browser may need extra passes or treat the percentage as `auto`. Long chains of percentage heights make layout fragile and sometimes slower. Use flex or grid to share height, or viewport units for full-height layouts.

## 374: How do viewport units affect performance on mobile?

On mobile, the browser's address bar shows and hides on scroll, which used to change `vh` and cause relayout during scrolling. Modern browsers keep `vh` stable (large viewport) and offer `svh`, `lvh` and `dvh`. `dvh` changes as the toolbar moves, so elements using it may relayout during scroll. Use `svh` or `lvh` unless you really need dynamic.

## 375: How does text rendering affect performance?

Text needs shaping (choosing glyphs), line breaking and painting. Long text with complex scripts, many font changes, `text-wrap: balance` or `pretty`, and hyphenation all add work. For normal articles it is fine. Problems appear when huge amounts of text are laid out again often, like during a resize or animation.

## 376: Is text-wrap: balance expensive?

It is more expensive than normal wrapping because the browser tries several line breaks to balance them. That is why browsers limit it to a small number of lines (Chrome to 6, Firefox to 10). Use it for headings, not body text. `text-wrap: pretty` is meant for body text and has a smaller cost, but still more than normal.

## 377: Why should you not animate font-size?

Changing `font-size` changes text layout, so every frame triggers text shaping, line breaking and layout of everything around it. Use `transform: scale()` on the text for a visual zoom instead, and accept that it may look slightly blurry during the animation.

## 378: How can SVG in CSS be a performance problem?

Inline SVG data URIs in CSS make the CSS file larger and are not cached on their own. Complex SVGs with many paths, filters or masks can be slow to rasterize, especially if repainted often or scaled. Large SVG backgrounds repeated on many elements can also cost paint time. Optimize SVGs with SVGO and prefer simple shapes.

## 379: Are data URIs in CSS a good idea?

For very small images (a few hundred bytes), they can save a request. For larger ones, they bloat the render-blocking CSS, cannot be cached separately, and base64 adds about 33% size. With HTTP/2, a separate file is usually better. Small SVGs encoded as UTF-8 data URIs instead of base64 are a reasonable middle ground.

## 380: How do CSS masks and clip-path affect performance?

`clip-path` with simple shapes is cheap and can even be animated with good performance in some cases. Complex paths and `mask-image` with large images need more paint and raster work. Animating `clip-path` usually runs on the main thread and repaints each frame, though Chrome can composite some clip-path animations. Test with paint flashing.

## 381: How does the z-index and stacking context structure affect paint?

Each stacking context is painted as a group. Creating many stacking contexts (from transforms, opacity, filters, isolation) adds structure the browser has to manage and can cause more layers. It is not usually a big cost alone, but combined with overlaps it leads to layer promotion. Keep stacking contexts intentional, and use `isolation: isolate` to contain them where helpful.

## 382: How does overflow: hidden versus overflow: clip affect performance?

`overflow: hidden` creates a scroll container (it can still be scrolled by script), which adds scroll handling and can make the browser treat the element as scrollable. `overflow: clip` just clips with no scroll container, so it is lighter and does not affect `position: sticky` descendants the same way. Use `clip` when you only need clipping.

## 383: What makes an element a scroll container, and why does it matter?

`overflow` values other than `visible` and `clip` (`auto`, `scroll`, `hidden`) create a scroll container. Each one needs scroll tracking and possibly its own layer for composited scrolling. Many small scroll containers can add memory and complexity. Also, `position: sticky` sticks to the nearest scroll container, so an accidental `overflow: hidden` breaks sticky headers.

## 384: What is composited scrolling?

When a scroll container is promoted to a layer, the compositor can scroll it without the main thread, so scrolling stays smooth even if JavaScript is busy. Browsers decide this automatically, mostly based on whether content is opaque and can be rasterized correctly (for example, LCD text). Non-composited scrolling repaints on every scroll and is much slower.

## 385: What can prevent composited scrolling?

The main cause today is `background-attachment: fixed`, which needs a repaint on every scroll. Non-passive `wheel` or `touchstart` listeners do not stop composited scrolling, but they make the compositor wait for the main thread before it starts. Older browsers also refused to composite scrollers with transparent backgrounds because of text rendering, but modern Chrome handles most of those cases. The "Scrolling performance issues" option in the Rendering tab highlights these problems.

## 386: Why is background-attachment: fixed slow?

The background has to stay in place while the content scrolls, so the browser repaints the area on every scroll frame instead of just moving layers. Many mobile browsers ignore it for this reason. A fixed-position pseudo-element with the background image, placed behind content, gives the same look and scrolls on the compositor.

```css
.parallax {
  position: relative;
}
.parallax::before {
  content: "";
  position: fixed;
  inset: 0;
  z-index: -1;
  background: url("bg.webp") center / cover;
}
```

## 387: How do you build a parallax effect without jank?

Avoid scroll listeners that set `top` or `background-position`. Use a scroll-driven animation that changes `transform: translateY()` with `animation-timeline: scroll()` or `view()`, or the 3D perspective trick where layers at different `translateZ` depths move at different speeds. Both keep work on the compositor.

## 388: How does the browser handle animations in background tabs?

Background tabs get `requestAnimationFrame` paused and timers throttled. CSS animations are generally not rendered because no frames are produced. When the tab comes back, animations jump to the right time. You do not need to pause CSS animations yourself for hidden tabs, but you should stop JavaScript-driven work.

## 389: How do iframes affect CSS performance on the parent page?

Each iframe is a separate document with its own CSS, style and layout. Same-site iframes often share the parent's main thread, so their CSS work competes with yours. Cross-site iframes usually run in a separate process with site isolation. Lazy-load iframes with `loading="lazy"` and give them fixed sizes to avoid layout shift.

## 390: What is the cost of a huge number of CSS animations defined but not running?

Defined `@keyframes` cost only parse time and memory. They do nothing until an element uses them. So a big animation library loaded but mostly unused costs bytes and parsing, not runtime. That is still a reason to import only the animations you use from libraries like Animate.css.

## 391: How do you profile memory used by CSS?

Chrome's heap snapshot does not show CSS objects in detail, but `performance.measureUserAgentSpecificMemory()` (in cross-origin isolated pages) and `about:memory` style tools in Firefox give totals. The Layers panel shows GPU memory per layer. For practical work, watch layer memory and total stylesheet size, which are the main CSS memory costs.

## 392: How would you debug a style recalculation that takes 200 ms on click?

1. Record a trace and find the Recalculate Style event after the click.
2. Check how many elements it affected.
3. Turn on selector stats to see which selectors cost the most.
4. Look at what changed: a class on a high ancestor, a root custom property, or a `:has()` anchored high.
5. Move the class change closer to the target, narrow the expensive selectors, or add `contain` so fewer elements are affected.

## 393: What is the cost of a CSS transition starting on many elements at once?

Each element's transition must be set up, and if properties are not composited, each frame updates all of them. Starting hundreds of transitions (for example in a grid filter animation) can cause long frames. Animate a container instead, stagger with small delays, or animate only visible items.

## 394: How can you make a large list filter animation smooth?

Use FLIP with the Web Animations API on only the items that are visible, or use view transitions with `view-transition-name` on visible items. Animate only `transform` and `opacity`. Use `content-visibility: auto` on items far off screen. Batch DOM reads and writes so layout runs once.

## 395: What is the difference between transition and animation in cost?

There is no real difference in cost for the same property. Both are driven by the same animation engine and can be composited for `transform` and `opacity`. Transitions react to style changes between two states, and animations run defined keyframes. Pick based on behavior, not speed.

## 396: How does the steps() timing function affect performance?

`steps()` makes the value jump in steps instead of smoothly. The browser still produces frames, but for sprite-sheet animations with `background-position` it means discrete paint changes. Animating a `transform` with `steps()` on a sprite sheet is cheaper than `background-position`, since it can be composited.

## 397: How do you reduce CSS work for hover effects on large lists?

Keep hover changes on the hovered element only, not on ancestors (`.list:hover .item` restyles all items). Prefer `opacity` and `transform` changes. Avoid hover effects that change size, which force layout of siblings. Use `@media (hover: hover)` to skip hover styles on touch devices.

```css
@media (hover: hover) {
  .item:hover {
    transform: translateY(-2px);
  }
}
```

## 398: What is the cost of :focus-within and :hover on parents?

`.card:hover` or `.form:focus-within` changes the state of an ancestor when a descendant is interacted with. Selectors that depend on that state, like `.form:focus-within .hint`, are re-evaluated for descendants. It is usually fine, but on very large containers with many dependent selectors it can make each interaction trigger more style work.

## 399: How do you decide which elements should be composited in a complex UI?

Promote only elements that animate often or need smooth independent movement: slide-out menus, modals, toasts, sticky headers, animated carousels. Do not promote static content. Check the Layers panel for memory and reasons, and remove promotions that do not improve frame times in a trace.

## 400: How do you measure frame performance in production?

Use the Long Animation Frames API to collect slow frames with attribution, and INP from `web-vitals` for interactions. For animations specifically, you can sample `requestAnimationFrame` timing on a small percentage of users during key animations, but keep that sampling light because it adds its own cost.

## 401: How does Content Security Policy affect inlined critical CSS?

A strict CSP with `style-src 'self'` blocks inline `<style>` tags, so inlined critical CSS will not apply. You need to add a nonce (generated per response) or a hash of the inline CSS to the policy. Hashes work well for static critical CSS; nonces are better when the CSS changes per page. Avoid `'unsafe-inline'`.

```html
<!-- Content-Security-Policy: style-src 'self' 'nonce-r4nd0m' -->
<style nonce="r4nd0m">
  /* critical CSS */
</style>
```

## 402: How does the media swap trick conflict with CSP?

The pattern uses an inline `onload="this.media='all'"` handler, which a strict CSP blocks because inline event handlers count as inline script. Fix it with a small external or nonced script that finds the links and switches the media, or use a framework feature that loads non-critical CSS without inline handlers.

```js
// loaded as a nonced or external script
document.querySelectorAll("link[data-async-css]").forEach((link) => {
  link.addEventListener(
    "load",
    () => {
      link.media = "all";
    },
    { once: true },
  );
});
```

## 403: Can CSS be used to leak data, and does that affect optimization choices?

Yes. Injected CSS can use attribute selectors with background URLs to send attribute values (like CSRF tokens) to an attacker's server, one character at a time. This is why you should not allow user-controlled CSS and why a CSP that restricts `style-src` and `img-src` matters. It affects optimization because some critical CSS or CSS-in-JS setups need relaxed CSP, which you should avoid.

## 404: How does subresource integrity apply to CSS?

You can add an `integrity` hash to a stylesheet from a CDN, so the browser refuses it if the content changed. It protects against a compromised CDN. It does not slow loading much, but if the file changes (for example an auto-updating CDN version), it will fail to load and the page will be unstyled. Use it with pinned versions.

```html
<link
  rel="stylesheet"
  href="https://cdn.example.com/lib@3.2.1/lib.min.css"
  integrity="sha384-..."
  crossorigin="anonymous"
/>
```

## 405: Scenario: LCP is 4 seconds and the waterfall shows a 300 KB CSS file. What do you do?

1. Check if it is compressed and cached; fix that first.
2. Run Coverage to see how much is unused on that page.
3. Extract and inline the critical CSS for the first screen.
4. Load the rest with the media swap pattern or split it per route.
5. Remove unused framework parts.
6. Check the LCP element: if it is an image in CSS, move it to `<img>` with `fetchpriority="high"`.

Then measure LCP again, in the lab and in the field.

## 406: Scenario: CLS is 0.25 on mobile only. How do you find the cause?

Run a trace with mobile emulation and look at the Layout shifts track. Common mobile-only causes: a different hero image without dimensions, a mobile banner or cookie bar inserted at the top, web fonts with a bigger metric difference at small sizes, or ads with responsive sizes. Use the `web-vitals` attribution build in production to get the exact shifting element across real devices.

## 407: Scenario: an animation is smooth on desktop but drops frames on iPhone. What do you check?

Check what is animated (layout or paint properties will hurt more on mobile), whether there are large blurs, shadows or `backdrop-filter`, and how many layers exist. Safari has different compositing rules than Chrome. Use Safari Web Inspector's Timelines and Layers tabs on a real device. Reduce effect sizes and switch to `transform` and `opacity`.

## 408: Scenario: opening a dropdown makes the whole page relayout. How do you fix it?

The dropdown probably takes space in the normal flow or changes a parent's height. Position it absolutely or use the Popover API so it is in the top layer and does not affect layout. Add `contain: layout` on the dropdown container if needed. Also check if opening it toggles a class on a high ancestor that restyles the page.

## 409: Scenario: typing in a search field is slow and the trace shows long Recalculate Style. Why?

A common cause is that each keystroke changes something that affects many elements, like toggling a class on a list container for "has results", a `:has()` selector watching the input (`form:has(input:placeholder-shown)`), or filtering by adding/removing classes on thousands of list items. Debounce the filtering, update only changed items, virtualize the list, and narrow broad selectors.

## 410: Scenario: a page with 5,000 product cards is slow to render. What CSS options do you have?

- `content-visibility: auto` with `contain-intrinsic-size: auto <height>` on each card or each group of cards.
- Simpler card CSS: fewer shadows, no filters.
- Pagination or virtualization to reduce DOM.
- `contain: content` on cards so hover changes stay local.
- Lazy-loaded images with set dimensions.

## 411: Scenario: after adding a design system, CSS grew from 40 KB to 220 KB. How do you approach it?

Find what is included: run a bundle analysis and Coverage. Common causes are importing the full design system CSS instead of per-component styles, shipping all themes, duplicated tokens, or both an old and new version loaded. Fix the import strategy, split themes into custom-property-only files, and set a CSS budget in CI so it does not happen again.

## 412: Scenario: fonts load late even though they are preloaded. Why?

Possible reasons: the preload URL does not match the URL in `@font-face` (query strings, different path); the preload lacks `crossorigin`, so it is downloaded twice; the font is served with wrong CORS headers from another domain; preloads are placed after large render-blocking scripts in the head; or too many preloads compete. The Network panel shows a "preloaded but not used" warning in the console for mismatches.

## 413: Scenario: the dark mode toggle freezes the page for 300 ms. How do you fix it?

Switching theme changes many custom properties on the root, which restyles the whole page, and then repaints everything. Reduce the cost by: keeping the number of theme variables small, avoiding transitions on color for all elements during the switch (temporarily disable transitions), and using `contain` on big independent sections. A short freeze on a rare action may be acceptable, but 300 ms is too much for INP.

```js
document.documentElement.classList.add("no-transitions");
document.documentElement.dataset.theme = next;
requestAnimationFrame(() => {
  requestAnimationFrame(() => {
    document.documentElement.classList.remove("no-transitions");
  });
});
```

## 414: Why do color transitions on every element make theme switches slow?

If you have `* { transition: background-color 0.3s, color 0.3s; }`, switching theme starts a transition on thousands of elements at once, and each frame must restyle and repaint them all for 300 ms. That is a lot of main thread work. Transition only a few big surfaces, or use a view transition that animates one snapshot of the whole page instead.

## 415: Scenario: a marketing team adds a 2 MB animated background. What do you suggest?

Replace it with a video (`<video autoplay muted loop playsinline>`) using a modern codec, which is far smaller than a GIF or big animated image, or a CSS gradient animation using `transform`. Load it lazily, show a static poster image first, respect `prefers-reduced-motion`, and pause it when off screen. Measure the effect on LCP and battery.

## 416: Scenario: Lighthouse says "Reduce unused CSS" but the team uses Tailwind. Why?

Possible causes: the content detection includes paths that list many classes (for example a docs folder or a big safelist); classes used only on other pages are in the shared file (Lighthouse only looks at the current page); or a third-party CSS file is the real culprit. A shared Tailwind file at 10-20 KB compressed is usually fine even if half is unused on one page.

## 417: How do you build critical CSS for a page with personalized content?

Generate critical CSS for the shared layout and the common components, not for personalized parts. Make sure the styles of any component that can appear above the fold are in the critical set, even if not all users see it. Measure CLS for different user types to find missing styles.

## 418: How do you handle CSS in an edge-rendered app for best TTFB and FCP?

Send the HTML head with critical CSS as early as possible, ideally from the edge before the data for the body is ready (streaming). Use Early Hints for the main stylesheet and fonts. Cache static CSS on the CDN with immutable headers. Keep critical CSS small so the first chunk is small.

## 419: What is the trade-off between one shared CSS file and per-page files in a multi-page site?

A shared file is downloaded once and cached for all pages, which is great for users who browse many pages. Per-page files have less unused CSS on first load but each new page type needs a new download. A good mix: a shared base file (layout, typography, common components) plus small page-specific files.

## 420: How does HTTP/3 change CSS delivery?

HTTP/3 runs over QUIC, which avoids TCP head-of-line blocking, so a lost packet for one file does not stall others. It also has faster connection setup. For CSS, it mostly helps on poor mobile networks, where render-blocking CSS is less likely to be delayed by packet loss on other requests. It does not change what CSS you should ship.

## 421: How do you prioritize CSS against JavaScript for the first load?

CSS in the head should come first and be small. JavaScript should be `defer` or `type="module"` so it does not block parsing. Avoid preloading big JS chunks ahead of CSS. Use `fetchpriority` to raise LCP images. Check the Network waterfall: render-blocking CSS should finish before the larger scripts take bandwidth.

## 422: How do you check that your CSS optimization does not break accessibility?

Make sure focus styles are in critical CSS (no flash of missing focus rings), `prefers-reduced-motion` is respected, `content-visibility` does not hide headings or landmarks from screen readers, color contrast is the same in fallback fonts, and lazy-loaded CSS does not hide content needed by assistive tech. Run axe or Lighthouse accessibility audits after changes.

## 423: What are the downsides of very aggressive CSS minification?

Advanced transforms can reorder rules, merge selectors or change values in ways that break the cascade, like merging rules that should stay separate because of order. Renaming keyframes or z-index values can break JavaScript that references them. Use safe presets, run visual regression tests, and keep source maps for debugging.

## 424: How do CSS source maps affect production performance?

Source maps are only downloaded when DevTools is open, so they do not affect normal users. You can serve them publicly, upload them only to your error tracker, or not generate them. Do not inline source maps into the CSS file, because that makes the CSS much larger for everyone.

## 425: How do you compare two CSS optimizations objectively?

Run both versions many times in the same lab conditions (WebPageTest with several runs, or Lighthouse CI with multiple runs) and compare the median of LCP, FCP, CLS and total blocking time. Then confirm in the field with an A/B rollout. One Lighthouse run has too much variance to decide anything.

## 426: How does WebPageTest help with CSS optimization?

It shows a waterfall with render-blocking marks, a filmstrip of what the user sees over time, and lets you test on real devices and networks. Its "Opportunities and Experiments" feature lets you try changes like removing render-blocking files or adding preloads without deploying, which helps prove the effect of a CSS change.

## 427: How do you debug a FOUC that only happens in production?

Compare the production HTML with development. Often CSS is injected by JavaScript in production (wrong loader), loaded asynchronously without proper critical CSS, ordered after the content in streaming SSR, or blocked by CSP. Check the Network panel for when the CSS arrives versus first paint, and the console for CSP errors.

## 428: How do CSS frameworks with JIT generation work, and what are the performance trade-offs?

Tools like Tailwind and UnoCSS scan source files and generate only the CSS for classes they find, at build time (or in the dev server). The output is small and does not grow much. The trade-off is build-time scanning, possible missed classes with dynamic names, and bigger HTML. There is no runtime cost in the browser.

## 429: What is UnoCSS and how does it differ from Tailwind in performance?

UnoCSS is an atomic CSS engine with presets, including one similar to Tailwind. It focuses on fast on-demand generation and flexibility. In the browser, output from both is static CSS of similar size; the differences are mostly in build speed and configuration, not runtime performance.

## 430: How do you deal with large CSS in email templates?

Email clients often strip `<style>` tags or ignore many properties, so CSS is usually inlined into elements with a tool like Juice or Maizzle. Size matters because Gmail clips messages over about 102 KB. Remove unused CSS, keep inline styles minimal, and avoid repeating long declarations.

## 431: How do CSS custom highlight and other new APIs reduce DOM work?

The CSS Custom Highlight API lets you style text ranges (like search matches) without wrapping them in extra `<span>` elements. Wrapping changes the DOM and forces style and layout; highlights only change paint.

```js
const range = new Range();
range.setStart(textNode, 5);
range.setEnd(textNode, 10);
CSS.highlights.set("search", new Highlight(range));
```

```css
::highlight(search) {
  background: yellow;
}
```

## 432: How does the browser handle @media and @container queries when resizing?

On resize, the browser re-evaluates media queries for the viewport and container queries for containers whose size changed. Rules that now match or no longer match cause style recalcs for affected elements, then layout. Rapid resizing can be expensive on complex pages, but browsers batch it per frame. Container queries limit the change to the containers that actually resized.

## 433: What is the cost of nested container queries?

Each container's size depends on layout, and the queries inside it depend on that size, so the browser lays out containers, evaluates queries, restyles and lays out again inside. With deep nesting, this can add extra layout passes. In practice a few levels are fine; avoid making every small wrapper a container.

## 434: How do style queries differ from size queries in cost?

Style queries (`@container style(--theme: dark)`) check computed custom property values on the container, not its size. They do not need size containment, so they do not affect layout. Their cost is similar to a selector that depends on an ancestor's state. Browser support for style queries is narrower, so check before relying on them.

## 435: How would you design CSS for a widget embedded on thousands of third-party sites?

Keep CSS tiny and scoped so it does not leak or get overridden: use Shadow DOM with an adopted stylesheet, or an iframe. Avoid web fonts or use system fonts. Do not block the host page: load asynchronously after the host content. Reserve the widget's space to avoid CLS on the host page, and use `contain: strict` for a fixed-size widget.

## 436: How do you avoid style conflicts and extra CSS in a widget without Shadow DOM?

Prefix all classes (like `.acme-widget__button`), use `all: revert` or a scoped reset on the root to protect from host styles, and wrap styles in `@scope (.acme-widget)` or a cascade layer. Keep selectors flat. This keeps the CSS small while making the widget look the same on different host sites.

## 437: How does the "all" property help in embedded components?

`all: initial` or `all: revert` resets every property on an element (except direction and unicode-bidi), so styles from the host page do not leak in. It is one short declaration instead of resetting dozens of properties. Be aware that it resets inherited properties too, so you must set fonts and colors again.

## 438: How does a print stylesheet affect print performance?

Printing large pages with complex layouts, many images or heavy effects can be slow and produce big PDFs. A print stylesheet that hides navigation, ads and decorative images, removes shadows and backgrounds, and uses simple layout makes printing faster and cleaner. Load it with `media="print"` so it never blocks screen rendering.

## 439: How do you approach CSS performance for low-end devices specifically?

Use the Device Memory and Network Information signals carefully (only some browsers have them) or the `prefers-reduced-motion` and `prefers-reduced-transparency` media queries to turn off expensive effects. Serve simpler visuals by default and add heavy effects only when supported and the device seems capable. Always test on a real cheap Android phone.

```css
@media (prefers-reduced-transparency: reduce) {
  .glass {
    backdrop-filter: none;
    background: #fff;
  }
}
```

## 440: What is the update media feature and when is it useful?

`@media (update: slow)` matches devices that cannot update the screen quickly, like e-ink readers, and `update: none` matches print. You can turn off animations and transitions for them. It is a niche but simple way to avoid wasted work on such devices.

## 441: How do CSS and JavaScript bundles interact in code splitting edge cases?

If two lazy chunks import the same CSS file, bundlers may put that CSS in a shared chunk or duplicate it, depending on settings. CSS order can also change between chunks, causing different results depending on load order. Keep shared styles in a global file or a shared component, and avoid relying on the order of CSS from different chunks. Cascade layers help make order irrelevant.

## 442: How can CSS order bugs appear after code splitting?

When CSS is split into chunks loaded at different times, a rule that used to come later in one big file might load earlier, so a different rule wins. This shows up as styles that look right on direct page load but wrong after client navigation. Use scoped class names, avoid equal-specificity conflicts between files, or put shared overrides into explicit cascade layers.

## 443: How do you think about CSS optimization for a single-page app versus a multi-page app?

In an SPA, the first load matters most; after that, CSS chunks load on navigation and stay in memory, so runtime style and layout performance becomes the bigger issue. In an MPA, every navigation reloads CSS from cache and parses again, so small shared files, good caching and critical CSS on each page matter more. View transitions and prerendering help MPAs feel as fast as SPAs.

## 444: How do Speculation Rules help with CSS for the next page?

Speculation Rules let the browser prefetch or prerender likely next pages. With prerender, the next page's CSS is downloaded, parsed and even rendered before the user clicks, so navigation shows instantly. Use `eagerness: "moderate"` to prerender on hover. It costs bandwidth and memory, so limit it to likely links.

```html
<script type="speculationrules">
  {
    "prerender": [
      { "where": { "href_matches": "/products/*" }, "eagerness": "moderate" }
    ]
  }
</script>
```

## 445: How do you write a CSS performance checklist for code review?

- No `@import` in plain CSS files.
- No new render-blocking third-party CSS.
- Animations only on `transform` and `opacity`, or justified otherwise.
- `will-change` only on elements that really animate.
- Images and embeds have dimensions or `aspect-ratio`.
- No new broad selectors like `.x *` or high-anchored `:has()`.
- New fonts justified, subsetted and with `font-display`.
- CSS size budget passes in CI.

## 446: How do you balance visual design and CSS performance in a team discussion?

Bring data, not opinions. Show a trace or a video of a slow phone running the effect, and the cost in milliseconds or Web Vitals. Offer alternatives that look almost the same but cost less, like a static shadow instead of an animated one, or a smaller blur area. Agree on budgets together so design and engineering share the same goals.

## 447: What mistakes do teams make when optimizing CSS?

- Optimizing selectors that were never slow, while ignoring render-blocking CSS.
- Putting `will-change` everywhere.
- Inlining all CSS and losing caching.
- Removing "unused" CSS that was used in states Coverage did not see.
- Testing only on fast laptops.
- Not measuring before and after.

## 448: What trends are changing CSS performance work today?

More native features replace JavaScript: container queries, `:has()`, scroll-driven animations, view transitions, popovers and anchor positioning. Build tools moved to faster engines like Lightning CSS. Runtime CSS-in-JS is being replaced by build-time solutions. And INP made runtime rendering cost, including style and layout, part of Core Web Vitals.

## 449: If you could do only three things to improve CSS performance on a typical site, what would they be?

1. Make the CSS on the critical path small: remove unused CSS, split by route, inline critical CSS, and compress and cache everything.
2. Fix layout shift: dimensions on media, tuned font fallbacks, reserved space for dynamic content.
3. Keep runtime work cheap: animate only `transform` and `opacity`, avoid broad style changes on interaction, and use `content-visibility` on long pages.

## 450: How would you explain the CSS performance mindset in one answer?

CSS is not free. Every byte in the head delays the first paint, and every change at runtime can make the browser redo style, layout and paint. So ship less of it, get the first-screen styles to the browser fast, reserve space so nothing jumps, and change only what you need, using properties the compositor can handle. Measure on real devices before and after, and keep budgets so the gains last.
