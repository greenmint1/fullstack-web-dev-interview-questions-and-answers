# Responsive UI Interview Questions and Answers

_Last updated: October 28, 2026_

450 Responsive UI interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The questions cover the HTML and CSS you use to build pages that work on any screen: the viewport meta tag, media queries, Flexbox, Grid, container queries, responsive images, fluid typography, viewport units, touch input, accessibility and testing. The answers are written against what current browsers support in 2026. Features that don't work in every major browser yet are marked as such.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is responsive web design?](#1-what-is-responsive-web-design)
- [2: Who came up with the term responsive web design and what were its three original parts?](#2-who-came-up-with-the-term-responsive-web-design-and-what-were-its-three-original-parts)
- [3: What is the difference between responsive and adaptive design?](#3-what-is-the-difference-between-responsive-and-adaptive-design)
- [4: What is the viewport?](#4-what-is-the-viewport)
- [5: What does the viewport meta tag do?](#5-what-does-the-viewport-meta-tag-do)
- [6: What happens if you leave out the viewport meta tag?](#6-what-happens-if-you-leave-out-the-viewport-meta-tag)
- [7: Why should you avoid user-scalable=no and maximum-scale=1?](#7-why-should-you-avoid-user-scalableno-and-maximum-scale1)
- [8: What is a media query?](#8-what-is-a-media-query)
- [9: What is the syntax of a media query?](#9-what-is-the-syntax-of-a-media-query)
- [10: What media types exist?](#10-what-media-types-exist)
- [11: What is a breakpoint?](#11-what-is-a-breakpoint)
- [12: How do you choose breakpoints?](#12-how-do-you-choose-breakpoints)
- [13: What is mobile-first design?](#13-what-is-mobile-first-design)
- [14: What is the difference between min-width and max-width media queries?](#14-what-is-the-difference-between-min-width-and-max-width-media-queries)
- [15: What is desktop-first design?](#15-what-is-desktop-first-design)
- [16: What is the media query range syntax?](#16-what-is-the-media-query-range-syntax)
- [17: How do you combine conditions in a media query?](#17-how-do-you-combine-conditions-in-a-media-query)
- [18: What does the not keyword do in a media query?](#18-what-does-the-not-keyword-do-in-a-media-query)
- [19: What does the only keyword do in a media query?](#19-what-does-the-only-keyword-do-in-a-media-query)
- [20: How do you load a stylesheet only for certain screens using HTML?](#20-how-do-you-load-a-stylesheet-only-for-certain-screens-using-html)
- [21: What is a fluid layout?](#21-what-is-a-fluid-layout)
- [22: What is a fixed-width layout and why is it a problem?](#22-what-is-a-fixed-width-layout-and-why-is-it-a-problem)
- [23: What is the difference between px, em and rem?](#23-what-is-the-difference-between-px-em-and-rem)
- [24: Why should you use rem for font sizes?](#24-why-should-you-use-rem-for-font-sizes)
- [25: What are percentage values relative to?](#25-what-are-percentage-values-relative-to)
- [26: What are the vw and vh units?](#26-what-are-the-vw-and-vh-units)
- [27: What are vmin and vmax?](#27-what-are-vmin-and-vmax)
- [28: Why is 100vh a problem on mobile?](#28-why-is-100vh-a-problem-on-mobile)
- [29: What are svh, lvh and dvh?](#29-what-are-svh-lvh-and-dvh)
- [30: What does max-width: 100% do on images?](#30-what-does-max-width-100-do-on-images)
- [31: Why do you add height: auto to responsive images?](#31-why-do-you-add-height-auto-to-responsive-images)
- [32: What is box-sizing: border-box and why is it used?](#32-what-is-box-sizing-border-box-and-why-is-it-used)
- [33: What base CSS rules help a responsive layout?](#33-what-base-css-rules-help-a-responsive-layout)
- [34: What is Flexbox?](#34-what-is-flexbox)
- [35: What are the main axis and cross axis in Flexbox?](#35-what-are-the-main-axis-and-cross-axis-in-flexbox)
- [36: What does flex-direction do?](#36-what-does-flex-direction-do)
- [37: What does flex-wrap do?](#37-what-does-flex-wrap-do)
- [38: What does justify-content do?](#38-what-does-justify-content-do)
- [39: What does align-items do?](#39-what-does-align-items-do)
- [40: What does the gap property do?](#40-what-does-the-gap-property-do)
- [41: What do flex-grow, flex-shrink and flex-basis do?](#41-what-do-flex-grow-flex-shrink-and-flex-basis-do)
- [42: What does flex: 1 mean?](#42-what-does-flex-1-mean)
- [43: How do you center an element horizontally and vertically?](#43-how-do-you-center-an-element-horizontally-and-vertically)
- [44: What is CSS Grid?](#44-what-is-css-grid)
- [45: What is the difference between Flexbox and Grid?](#45-what-is-the-difference-between-flexbox-and-grid)
- [46: What is the fr unit?](#46-what-is-the-fr-unit)
- [47: What does repeat() do in CSS Grid?](#47-what-does-repeat-do-in-css-grid)
- [48: What does minmax() do?](#48-what-does-minmax-do)
- [49: What is the difference between auto-fill and auto-fit?](#49-what-is-the-difference-between-auto-fill-and-auto-fit)
- [50: How do you make a responsive card grid without media queries?](#50-how-do-you-make-a-responsive-card-grid-without-media-queries)
- [51: What is grid-template-areas?](#51-what-is-grid-template-areas)
- [52: How do you change a grid layout at a breakpoint?](#52-how-do-you-change-a-grid-layout-at-a-breakpoint)
- [53: How do you make a grid item span multiple columns or rows?](#53-how-do-you-make-a-grid-item-span-multiple-columns-or-rows)
- [54: What does the order property do and why should you be careful with it?](#54-what-does-the-order-property-do-and-why-should-you-be-careful-with-it)
- [55: What is the srcset attribute?](#55-what-is-the-srcset-attribute)
- [56: What is the sizes attribute?](#56-what-is-the-sizes-attribute)
- [57: What is the picture element?](#57-what-is-the-picture-element)
- [58: What is the difference between resolution switching and art direction?](#58-what-is-the-difference-between-resolution-switching-and-art-direction)
- [59: What are x descriptors and w descriptors in srcset?](#59-what-are-x-descriptors-and-w-descriptors-in-srcset)
- [60: What is the difference between CSS pixels and device pixels?](#60-what-is-the-difference-between-css-pixels-and-device-pixels)
- [61: How do you get the device pixel ratio in JavaScript?](#61-how-do-you-get-the-device-pixel-ratio-in-javascript)
- [62: Why should you set width and height attributes on images?](#62-why-should-you-set-width-and-height-attributes-on-images)
- [63: What does loading="lazy" do?](#63-what-does-loadinglazy-do)
- [64: What does object-fit do?](#64-what-does-object-fit-do)
- [65: What does object-position do?](#65-what-does-object-position-do)
- [66: What is the aspect-ratio property?](#66-what-is-the-aspect-ratio-property)
- [67: How do you make a video responsive?](#67-how-do-you-make-a-video-responsive)
- [68: How do you make an iframe embed responsive, like a YouTube video?](#68-how-do-you-make-an-iframe-embed-responsive-like-a-youtube-video)
- [69: How do you serve modern image formats like AVIF and WebP with a fallback?](#69-how-do-you-serve-modern-image-formats-like-avif-and-webp-with-a-fallback)
- [70: How do you make a CSS background image responsive?](#70-how-do-you-make-a-css-background-image-responsive)
- [71: What is image-set() in CSS?](#71-what-is-image-set-in-css)
- [72: Do responsive images still need alt text?](#72-do-responsive-images-still-need-alt-text)
- [73: What is responsive typography?](#73-what-is-responsive-typography)
- [74: What does clamp() do?](#74-what-does-clamp-do)
- [75: What do min() and max() do?](#75-what-do-min-and-max-do)
- [76: What is calc()?](#76-what-is-calc)
- [77: Why should you limit line length and how?](#77-why-should-you-limit-line-length-and-how)
- [78: What is the ch unit?](#78-what-is-the-ch-unit)
- [79: What is the compounding problem with em?](#79-what-is-the-compounding-problem-with-em)
- [80: Why should line-height be unitless?](#80-why-should-line-height-be-unitless)
- [81: How do you hide content on small screens?](#81-how-do-you-hide-content-on-small-screens)
- [82: What is the difference between display: none and visibility: hidden?](#82-what-is-the-difference-between-display-none-and-visibility-hidden)
- [83: How do you hide something visually but keep it for screen readers?](#83-how-do-you-hide-something-visually-but-keep-it-for-screen-readers)
- [84: What is a hamburger menu?](#84-what-is-a-hamburger-menu)
- [85: How do you build a simple responsive navigation?](#85-how-do-you-build-a-simple-responsive-navigation)
- [86: What is a touch target and how big should it be?](#86-what-is-a-touch-target-and-how-big-should-it-be)
- [87: What is the hover media feature?](#87-what-is-the-hover-media-feature)
- [88: What is the pointer media feature?](#88-what-is-the-pointer-media-feature)
- [89: What is prefers-color-scheme?](#89-what-is-prefers-color-scheme)
- [90: What is prefers-reduced-motion?](#90-what-is-prefers-reduced-motion)
- [91: What is the orientation media feature?](#91-what-is-the-orientation-media-feature)
- [92: How do you write print styles?](#92-how-do-you-write-print-styles)
- [93: What is the resolution media feature?](#93-what-is-the-resolution-media-feature)
- [94: How do you test a responsive site in browser DevTools?](#94-how-do-you-test-a-responsive-site-in-browser-devtools)
- [95: Why should you still test on real devices?](#95-why-should-you-still-test-on-real-devices)
- [96: How do you find what causes horizontal scrolling?](#96-how-do-you-find-what-causes-horizontal-scrolling)
- [97: How do you stop long words and URLs from breaking the layout?](#97-how-do-you-stop-long-words-and-urls-from-breaking-the-layout)
- [98: How do you make a wide element scroll horizontally instead of breaking the page?](#98-how-do-you-make-a-wide-element-scroll-horizontally-instead-of-breaking-the-page)
- [99: How do you make tables responsive?](#99-how-do-you-make-tables-responsive)
- [100: Why do semantic HTML elements matter in a responsive layout?](#100-why-do-semantic-html-elements-matter-in-a-responsive-layout)
- [101: Why does source order matter in a responsive page?](#101-why-does-source-order-matter-in-a-responsive-page)
- [102: What is the difference between block and inline elements?](#102-what-is-the-difference-between-block-and-inline-elements)
- [103: What does display: inline-block do?](#103-what-does-display-inline-block-do)
- [104: How do you use CSS custom properties with media queries?](#104-how-do-you-use-css-custom-properties-with-media-queries)
- [105: How do you create a centered page container?](#105-how-do-you-create-a-centered-page-container)
- [106: What does margin: auto do inside a flex container?](#106-what-does-margin-auto-do-inside-a-flex-container)
- [107: What are logical properties?](#107-what-are-logical-properties)
- [108: What is position: sticky?](#108-what-is-position-sticky)
- [109: How do you build a sticky header?](#109-how-do-you-build-a-sticky-header)
- [110: What problems does position: fixed have on mobile?](#110-what-problems-does-position-fixed-have-on-mobile)
- [111: Should media queries use px, em or rem?](#111-should-media-queries-use-px-em-or-rem)
- [112: Why does the input type attribute matter on mobile?](#112-why-does-the-input-type-attribute-matter-on-mobile)
- [113: What does the inputmode attribute do?](#113-what-does-the-inputmode-attribute-do)
- [114: How does the autocomplete attribute help on mobile?](#114-how-does-the-autocomplete-attribute-help-on-mobile)
- [115: Why does iOS zoom in when you tap an input, and how do you stop it?](#115-why-does-ios-zoom-in-when-you-tap-an-input-and-how-do-you-stop-it)
- [116: How do you make a form layout responsive?](#116-how-do-you-make-a-form-layout-responsive)
- [117: What font size should body text be on mobile and desktop?](#117-what-font-size-should-body-text-be-on-mobile-and-desktop)
- [118: How do CSS frameworks help with responsive design?](#118-how-do-css-frameworks-help-with-responsive-design)
- [119: How do responsive prefixes work in Tailwind CSS?](#119-how-do-responsive-prefixes-work-in-tailwind-css)
- [120: What is a 12-column grid?](#120-what-is-a-12-column-grid)
- [121: What is a gutter?](#121-what-is-a-gutter)
- [122: What breakpoint values are common?](#122-what-breakpoint-values-are-common)
- [123: What is the difference between screen.width and window.innerWidth?](#123-what-is-the-difference-between-screenwidth-and-windowinnerwidth)
- [124: What is matchMedia() in JavaScript?](#124-what-is-matchmedia-in-javascript)
- [125: Why should you avoid heavy work in the resize event?](#125-why-should-you-avoid-heavy-work-in-the-resize-event)
- [126: What are container queries?](#126-what-are-container-queries)
- [127: What is the CSS multi-column layout?](#127-what-is-the-css-multi-column-layout)
- [128: What is CSS scroll snap?](#128-what-is-css-scroll-snap)
- [129: What do place-items and place-content do?](#129-what-do-place-items-and-place-content-do)
- [130: What are min-content, max-content and fit-content?](#130-what-are-min-content-max-content-and-fit-content)
- [131: What is the difference between width: 100% and width: 100vw?](#131-what-is-the-difference-between-width-100-and-width-100vw)
- [132: Why use min-height instead of height in responsive layouts?](#132-why-use-min-height-instead-of-height-in-responsive-layouts)
- [133: What problems can overflow: hidden cause in responsive layouts?](#133-what-problems-can-overflow-hidden-cause-in-responsive-layouts)
- [134: What were floats used for and do you still need them for layout?](#134-what-were-floats-used-for-and-do-you-still-need-them-for-layout)
- [135: How do SVG images scale responsively?](#135-how-do-svg-images-scale-responsively)
- [136: How do you make icons scale with the text next to them?](#136-how-do-you-make-icons-scale-with-the-text-next-to-them)
- [137: What does the theme-color meta tag do?](#137-what-does-the-theme-color-meta-tag-do)
- [138: What does the color-scheme property do?](#138-what-does-the-color-scheme-property-do)
- [139: How can details and summary help on small screens?](#139-how-can-details-and-summary-help-on-small-screens)
- [140: Why use the dialog element for modals in a responsive UI?](#140-why-use-the-dialog-element-for-modals-in-a-responsive-ui)
- [141: What does text-wrap: balance do?](#141-what-does-text-wrap-balance-do)
- [142: How do you make spacing responsive?](#142-how-do-you-make-spacing-responsive)
- [143: How do you check if a CSS feature is safe to use?](#143-how-do-you-check-if-a-css-feature-is-safe-to-use)
- [144: What is progressive enhancement?](#144-what-is-progressive-enhancement)
- [145: What is graceful degradation?](#145-what-is-graceful-degradation)
- [146: What is @supports?](#146-what-is-supports)
- [147: How do you keep a footer at the bottom of the page when content is short?](#147-how-do-you-keep-a-footer-at-the-bottom-of-the-page-when-content-is-short)
- [148: Why is overflow-x: hidden on the body a bad fix for horizontal scrolling?](#148-why-is-overflow-x-hidden-on-the-body-a-bad-fix-for-horizontal-scrolling)
- [149: When should you use height media queries?](#149-when-should-you-use-height-media-queries)
- [150: What is the difference between display: flex and display: inline-flex?](#150-what-is-the-difference-between-display-flex-and-display-inline-flex)

### Moderate Questions (151-300)

- [151: What values can container-type have?](#151-what-values-can-container-type-have)
- [152: What are container-name and the container shorthand?](#152-what-are-container-name-and-the-container-shorthand)
- [153: What are container query units?](#153-what-are-container-query-units)
- [154: When should you use a container query and when a media query?](#154-when-should-you-use-a-container-query-and-when-a-media-query)
- [155: Why can't an element query its own size with a container query?](#155-why-cant-an-element-query-its-own-size-with-a-container-query)
- [156: What are container style queries?](#156-what-are-container-style-queries)
- [157: How can :has() help with responsive layouts?](#157-how-can-has-help-with-responsive-layouts)
- [158: How do you change a layout based on the number of children?](#158-how-do-you-change-a-layout-based-on-the-number-of-children)
- [159: What is subgrid?](#159-what-is-subgrid)
- [160: What is intrinsic web design?](#160-what-is-intrinsic-web-design)
- [161: What is the flexbox "switcher" pattern?](#161-what-is-the-flexbox-switcher-pattern)
- [162: How do you build a sidebar layout that wraps without media queries?](#162-how-do-you-build-a-sidebar-layout-that-wraps-without-media-queries)
- [163: What is the holy grail layout and how do you build it today?](#163-what-is-the-holy-grail-layout-and-how-do-you-build-it-today)
- [164: How do you build a full-bleed layout with CSS Grid?](#164-how-do-you-build-a-full-bleed-layout-with-css-grid)
- [165: What are the stack and cluster layout patterns?](#165-what-are-the-stack-and-cluster-layout-patterns)
- [166: Why do you sometimes need min-width: 0 on a flex item?](#166-why-do-you-sometimes-need-min-width-0-on-a-flex-item)
- [167: What is grid blowout and how does minmax(0, 1fr) fix it?](#167-what-is-grid-blowout-and-how-does-minmax0-1fr-fix-it)
- [168: What does grid-auto-flow: dense do?](#168-what-does-grid-auto-flow-dense-do)
- [169: What is the implicit grid and grid-auto-rows?](#169-what-is-the-implicit-grid-and-grid-auto-rows)
- [170: How do you stop the last row of a wrapping flex layout from stretching?](#170-how-do-you-stop-the-last-row-of-a-wrapping-flex-layout-from-stretching)
- [171: How does the browser pick an image from srcset with w descriptors?](#171-how-does-the-browser-pick-an-image-from-srcset-with-w-descriptors)
- [172: How do you write an accurate sizes attribute?](#172-how-do-you-write-an-accurate-sizes-attribute)
- [173: What is sizes="auto"?](#173-what-is-sizesauto)
- [174: What does fetchpriority do?](#174-what-does-fetchpriority-do)
- [175: How do you preload a responsive image?](#175-how-do-you-preload-a-responsive-image)
- [176: Why shouldn't you lazy load the hero image?](#176-why-shouldnt-you-lazy-load-the-hero-image)
- [177: How do you combine media and type in a picture element?](#177-how-do-you-combine-media-and-type-in-a-picture-element)
- [178: What does decoding="async" do?](#178-what-does-decodingasync-do)
- [179: What is an image CDN and why use one for responsive images?](#179-what-is-an-image-cdn-and-why-use-one-for-responsive-images)
- [180: How many image widths should you put in srcset?](#180-how-many-image-widths-should-you-put-in-srcset)
- [181: When should you use SVG instead of a raster image?](#181-when-should-you-use-svg-instead-of-a-raster-image)
- [182: How do framework image components help with responsive images?](#182-how-do-framework-image-components-help-with-responsive-images)
- [183: How do you make an SVG chart responsive?](#183-how-do-you-make-an-svg-chart-responsive)
- [184: How do you calculate the values for a fluid clamp() font size?](#184-how-do-you-calculate-the-values-for-a-fluid-clamp-font-size)
- [185: Why should a fluid font size combine rem and vw, not use vw alone?](#185-why-should-a-fluid-font-size-combine-rem-and-vw-not-use-vw-alone)
- [186: What is a type scale and how do you make it responsive?](#186-what-is-a-type-scale-and-how-do-you-make-it-responsive)
- [187: What does the WCAG Reflow criterion require?](#187-what-does-the-wcag-reflow-criterion-require)
- [188: What does the WCAG Resize Text criterion require?](#188-what-does-the-wcag-resize-text-criterion-require)
- [189: What does the WCAG Text Spacing criterion mean for responsive layouts?](#189-what-does-the-wcag-text-spacing-criterion-mean-for-responsive-layouts)
- [190: What does the WCAG Orientation criterion require?](#190-what-does-the-wcag-orientation-criterion-require)
- [191: What is :focus-visible and why is it useful on touch devices?](#191-what-is-focus-visible-and-why-is-it-useful-on-touch-devices)
- [192: How do you handle the notch and rounded corners on phones?](#192-how-do-you-handle-the-notch-and-rounded-corners-on-phones)
- [193: What does the interactive-widget viewport setting do?](#193-what-does-the-interactive-widget-viewport-setting-do)
- [194: What is the visualViewport API?](#194-what-is-the-visualviewport-api)
- [195: When should you use svh, lvh or dvh?](#195-when-should-you-use-svh-lvh-or-dvh)
- [196: How do you build an accessible off-canvas menu?](#196-how-do-you-build-an-accessible-off-canvas-menu)
- [197: How can the popover attribute help with responsive menus?](#197-how-can-the-popover-attribute-help-with-responsive-menus)
- [198: How do you stop the page from scrolling behind an open menu or modal?](#198-how-do-you-stop-the-page-from-scrolling-behind-an-open-menu-or-modal)
- [199: What does overscroll-behavior do?](#199-what-does-overscroll-behavior-do)
- [200: What does scrollbar-gutter do?](#200-what-does-scrollbar-gutter-do)
- [201: What does touch-action do?](#201-what-does-touch-action-do)
- [202: What was the 300ms tap delay and is it still a problem?](#202-what-was-the-300ms-tap-delay-and-is-it-still-a-problem)
- [203: What is the difference between pointer, touch and mouse events?](#203-what-is-the-difference-between-pointer-touch-and-mouse-events)
- [204: How do you handle devices that have both touch and a mouse?](#204-how-do-you-handle-devices-that-have-both-touch-and-a-mouse)
- [205: How do you make a dropdown menu work on both mouse and touch?](#205-how-do-you-make-a-dropdown-menu-work-on-both-mouse-and-touch)
- [206: How do you turn table rows into cards on small screens?](#206-how-do-you-turn-table-rows-into-cards-on-small-screens)
- [207: Why can changing a table's display break it for screen readers?](#207-why-can-changing-a-tables-display-break-it-for-screen-readers)
- [208: How do you make a table header and first column sticky inside a scroll container?](#208-how-do-you-make-a-table-header-and-first-column-sticky-inside-a-scroll-container)
- [209: What should you watch out for with a responsive carousel?](#209-what-should-you-watch-out-for-with-a-responsive-carousel)
- [210: What is prefers-contrast?](#210-what-is-prefers-contrast)
- [211: What is forced-colors mode?](#211-what-is-forced-colors-mode)
- [212: What does the light-dark() function do?](#212-what-does-the-light-dark-function-do)
- [213: How do you support both the system theme and a manual theme toggle?](#213-how-do-you-support-both-the-system-theme-and-a-manual-theme-toggle)
- [214: What are prefers-reduced-transparency and prefers-reduced-data?](#214-what-are-prefers-reduced-transparency-and-prefers-reduced-data)
- [215: How do you show a different image in dark mode?](#215-how-do-you-show-a-different-image-in-dark-mode)
- [216: How do you use media queries in React, and what is the SSR problem?](#216-how-do-you-use-media-queries-in-react-and-what-is-the-ssr-problem)
- [217: What is ResizeObserver and when do you use it?](#217-what-is-resizeobserver-and-when-do-you-use-it)
- [218: How is IntersectionObserver useful in responsive UIs?](#218-how-is-intersectionobserver-useful-in-responsive-uis)
- [219: Can you nest media queries in plain CSS?](#219-can-you-nest-media-queries-in-plain-css)
- [220: Do media queries add specificity?](#220-do-media-queries-add-specificity)
- [221: How do you write a breakpoint mixin in Sass?](#221-how-do-you-write-a-breakpoint-mixin-in-sass)
- [222: What is @custom-media?](#222-what-is-custom-media)
- [223: How do you share breakpoints between CSS and JavaScript?](#223-how-do-you-share-breakpoints-between-css-and-javascript)
- [224: What are design tokens and how do they help responsive design?](#224-what-are-design-tokens-and-how-do-they-help-responsive-design)
- [225: How should you name breakpoints?](#225-how-should-you-name-breakpoints)
- [226: How do you handle right-to-left languages in a responsive layout?](#226-how-do-you-handle-right-to-left-languages-in-a-responsive-layout)
- [227: What does hyphens: auto do and why is lang needed?](#227-what-does-hyphens-auto-do-and-why-is-lang-needed)
- [228: How do you limit text to a set number of lines?](#228-how-do-you-limit-text-to-a-set-number-of-lines)
- [229: How do you truncate a single line of text inside a flex item?](#229-how-do-you-truncate-a-single-line-of-text-inside-a-flex-item)
- [230: What does field-sizing: content do?](#230-what-does-field-sizing-content-do)
- [231: What does the enterkeyhint attribute do?](#231-what-does-the-enterkeyhint-attribute-do)
- [232: Why is position: sticky not working?](#232-why-is-position-sticky-not-working)
- [233: Why does a mobile menu sometimes appear behind other content?](#233-why-does-a-mobile-menu-sometimes-appear-behind-other-content)
- [234: How do you serve a different video file for small screens?](#234-how-do-you-serve-a-different-video-file-for-small-screens)
- [235: What do you need for a video to autoplay on mobile?](#235-what-do-you-need-for-a-video-to-autoplay-on-mobile)
- [236: How do you handle third-party embeds that aren't responsive?](#236-how-do-you-handle-third-party-embeds-that-arent-responsive)
- [237: How should you load web fonts for a responsive site?](#237-how-should-you-load-web-fonts-for-a-responsive-site)
- [238: How do variable fonts help responsive typography?](#238-how-do-variable-fonts-help-responsive-typography)
- [239: What is the 62.5% root font-size trick and why should you avoid it?](#239-what-is-the-625-root-font-size-trick-and-why-should-you-avoid-it)
- [240: What is the difference between browser zoom and the default font size setting?](#240-what-is-the-difference-between-browser-zoom-and-the-default-font-size-setting)
- [241: What are the lh and rlh units?](#241-what-are-the-lh-and-rlh-units)
- [242: How should line height change across screen sizes?](#242-how-should-line-height-change-across-screen-sizes)
- [243: How do you test responsive layouts automatically?](#243-how-do-you-test-responsive-layouts-automatically)
- [244: What is visual regression testing and how does it help with responsive UIs?](#244-what-is-visual-regression-testing-and-how-does-it-help-with-responsive-uis)
- [245: What does Lighthouse check for mobile?](#245-what-does-lighthouse-check-for-mobile)
- [246: What does DevTools device mode change, and what doesn't it?](#246-what-does-devtools-device-mode-change-and-what-doesnt-it)
- [247: How do you debug a page on a real phone?](#247-how-do-you-debug-a-page-on-a-real-phone)
- [248: What are Client Hints?](#248-what-are-client-hints)
- [249: Why is user agent sniffing a bad way to build responsive sites?](#249-why-is-user-agent-sniffing-a-bad-way-to-build-responsive-sites)
- [250: What is adaptive loading?](#250-what-is-adaptive-loading)
- [251: What is the priority+ navigation pattern?](#251-what-is-the-priority-navigation-pattern)
- [252: When does a bottom navigation bar make sense on mobile?](#252-when-does-a-bottom-navigation-bar-make-sense-on-mobile)
- [253: How do you build a bottom sheet on mobile that is a centered modal on desktop?](#253-how-do-you-build-a-bottom-sheet-on-mobile-that-is-a-centered-modal-on-desktop)
- [254: How would you build a responsive dashboard layout?](#254-how-would-you-build-a-responsive-dashboard-layout)
- [255: How do you keep buttons aligned at the bottom of cards with different content lengths?](#255-how-do-you-keep-buttons-aligned-at-the-bottom-of-cards-with-different-content-lengths)
- [256: How do you build a sidebar that collapses into a drawer on mobile?](#256-how-do-you-build-a-sidebar-that-collapses-into-a-drawer-on-mobile)
- [257: How would you make a pricing table responsive?](#257-how-would-you-make-a-pricing-table-responsive)
- [258: How do you build a responsive image gallery?](#258-how-do-you-build-a-responsive-image-gallery)
- [259: How do you build a masonry layout today?](#259-how-do-you-build-a-masonry-layout-today)
- [260: How do you build a responsive hero section?](#260-how-do-you-build-a-responsive-hero-section)
- [261: What does display: contents do and what is the accessibility concern?](#261-what-does-display-contents-do-and-what-is-the-accessibility-concern)
- [262: How does placing grid items visually affect tab order?](#262-how-does-placing-grid-items-visually-affect-tab-order)
- [263: What are named grid lines?](#263-what-are-named-grid-lines)
- [264: What is the difference between justify-items and justify-content in Grid?](#264-what-is-the-difference-between-justify-items-and-justify-content-in-grid)
- [265: What does align-content do in a wrapping flex container?](#265-what-does-align-content-do-in-a-wrapping-flex-container)
- [266: What is the difference between flex-basis and width?](#266-what-is-the-difference-between-flex-basis-and-width)
- [267: Why do images or avatars get squished in a flex row, and how do you fix it?](#267-why-do-images-or-avatars-get-squished-in-a-flex-row-and-how-do-you-fix-it)
- [268: Why do images stretch in a flex row and how do you stop it?](#268-why-do-images-stretch-in-a-flex-row-and-how-do-you-stop-it)
- [269: How do media queries interact with the cascade?](#269-how-do-media-queries-interact-with-the-cascade)
- [270: Should you group media queries at the end of the file or keep them with each component?](#270-should-you-group-media-queries-at-the-end-of-the-file-or-keep-them-with-each-component)
- [271: What is component-driven responsive design?](#271-what-is-component-driven-responsive-design)
- [272: How do you design for very large screens?](#272-how-do-you-design-for-very-large-screens)
- [273: How do you make sure a focused input isn't hidden behind the keyboard or a sticky header?](#273-how-do-you-make-sure-a-focused-input-isnt-hidden-behind-the-keyboard-or-a-sticky-header)
- [274: Why is building responsive emails different from web pages?](#274-why-is-building-responsive-emails-different-from-web-pages)
- [275: How do you control page breaks and page size when printing?](#275-how-do-you-control-page-breaks-and-page-size-when-printing)
- [276: How do you show a different logo on small screens?](#276-how-do-you-show-a-different-logo-on-small-screens)
- [277: How do container query units help with responsive spacing?](#277-how-do-container-query-units-help-with-responsive-spacing)
- [278: Should headings scale with the viewport or with the container?](#278-should-headings-scale-with-the-viewport-or-with-the-container)
- [279: When should you use an auto-fit grid and when container queries for cards?](#279-when-should-you-use-an-auto-fit-grid-and-when-container-queries-for-cards)
- [280: How do you show fewer items on small screens?](#280-how-do-you-show-fewer-items-on-small-screens)
- [281: What other useful media features exist besides width?](#281-what-other-useful-media-features-exist-besides-width)
- [282: How do you style a site differently when it's installed as a PWA?](#282-how-do-you-style-a-site-differently-when-its-installed-as-a-pwa)
- [283: How can you use :has() to lock scrolling when a menu is open?](#283-how-can-you-use-has-to-lock-scrolling-when-a-menu-is-open)
- [284: When should you use object-fit on an img and when background-size on a CSS background?](#284-when-should-you-use-object-fit-on-an-img-and-when-background-size-on-a-css-background)
- [285: How do you avoid layout shift from ads or embeds in a responsive layout?](#285-how-do-you-avoid-layout-shift-from-ads-or-embeds-in-a-responsive-layout)
- [286: How do you build a split-screen layout that stacks on mobile?](#286-how-do-you-build-a-split-screen-layout-that-stacks-on-mobile)
- [287: What does a fallback for container queries look like?](#287-what-does-a-fallback-for-container-queries-look-like)
- [288: How do you handle user-generated content of unknown length in responsive components?](#288-how-do-you-handle-user-generated-content-of-unknown-length-in-responsive-components)
- [289: How do you make responsive images work for content from a CMS?](#289-how-do-you-make-responsive-images-work-for-content-from-a-cms)
- [290: How do you test text zoom and larger font settings?](#290-how-do-you-test-text-zoom-and-larger-font-settings)
- [291: What does mobile-first mean for performance, not just CSS?](#291-what-does-mobile-first-mean-for-performance-not-just-css)
- [292: How do you avoid loading desktop-only JavaScript on mobile?](#292-how-do-you-avoid-loading-desktop-only-javascript-on-mobile)
- [293: How do you combine image-set() with media queries for backgrounds?](#293-how-do-you-combine-image-set-with-media-queries-for-backgrounds)
- [294: What does text-size-adjust do?](#294-what-does-text-size-adjust-do)
- [295: How do you mix fixed and flexible columns in a grid?](#295-how-do-you-mix-fixed-and-flexible-columns-in-a-grid)
- [296: How do you make equal-height columns?](#296-how-do-you-make-equal-height-columns)
- [297: How do you debug responsive CSS in DevTools?](#297-how-do-you-debug-responsive-css-in-devtools)
- [298: How would you check a page for responsive problems before release?](#298-how-would-you-check-a-page-for-responsive-problems-before-release)
- [299: What is the difference between CSS transforms and layout properties for responsive animations?](#299-what-is-the-difference-between-css-transforms-and-layout-properties-for-responsive-animations)
- [300: What are common responsive design mistakes?](#300-what-are-common-responsive-design-mistakes)

### Advanced Questions (301-450)

- [301: Why does the sizes attribute have to be in the HTML instead of coming from CSS?](#301-why-does-the-sizes-attribute-have-to-be-in-the-html-instead-of-coming-from-css)
- [302: Why might a browser download a larger srcset candidate than you expect?](#302-why-might-a-browser-download-a-larger-srcset-candidate-than-you-expect)
- [303: What happens with srcset when the viewport changes after the page loads?](#303-what-happens-with-srcset-when-the-viewport-changes-after-the-page-loads)
- [304: Does picture re-evaluate its sources when the viewport changes?](#304-does-picture-re-evaluate-its-sources-when-the-viewport-changes)
- [305: How do you preload an art-directed LCP image without downloading two files?](#305-how-do-you-preload-an-art-directed-lcp-image-without-downloading-two-files)
- [306: How do you check whether your images are oversized?](#306-how-do-you-check-whether-your-images-are-oversized)
- [307: Should you serve 3x images to 3x screens?](#307-should-you-serve-3x-images-to-3x-screens)
- [308: How does serving image formats based on the Accept header affect caching?](#308-how-does-serving-image-formats-based-on-the-accept-header-affect-caching)
- [309: How do Client Hints work with a third-party image CDN?](#309-how-do-client-hints-work-with-a-third-party-image-cdn)
- [310: What are low-quality image placeholders and how do they fit into responsive layouts?](#310-what-are-low-quality-image-placeholders-and-how-do-they-fit-into-responsive-layouts)
- [311: How do container queries work under the hood?](#311-how-do-container-queries-work-under-the-hood)
- [312: Why does container-type: size often collapse the element's height?](#312-why-does-container-type-size-often-collapse-the-elements-height)
- [313: How are nested containers resolved, and how do you avoid surprises?](#313-how-are-nested-containers-resolved-and-how-do-you-avoid-surprises)
- [314: Do container queries have a performance cost?](#314-do-container-queries-have-a-performance-cost)
- [315: What do container query units refer to when used on the container element itself?](#315-what-do-container-query-units-refer-to-when-used-on-the-container-element-itself)
- [316: How can you combine container queries and :has() to style a parent based on its size?](#316-how-can-you-combine-container-queries-and-has-to-style-a-parent-based-on-its-size)
- [317: What are scroll-state container queries?](#317-what-are-scroll-state-container-queries)
- [318: What is CSS anchor positioning and why does it help in responsive UIs?](#318-what-is-css-anchor-positioning-and-why-does-it-help-in-responsive-uis)
- [319: How do you make a tooltip that stays on screen on any device size?](#319-how-do-you-make-a-tooltip-that-stays-on-screen-on-any-device-size)
- [320: What is the CSS if() function?](#320-what-is-the-css-if-function)
- [321: How do you decide where a responsive change belongs: media query, container query or intrinsic layout?](#321-how-do-you-decide-where-a-responsive-change-belongs-media-query-container-query-or-intrinsic-layout)
- [322: What does the contain property do and how does it help performance?](#322-what-does-the-contain-property-do-and-how-does-it-help-performance)
- [323: What does content-visibility: auto do?](#323-what-does-content-visibility-auto-do)
- [324: What is layout thrashing and how does it relate to responsive JavaScript?](#324-what-is-layout-thrashing-and-how-does-it-relate-to-responsive-javascript)
- [325: Do many media queries slow down a page?](#325-do-many-media-queries-slow-down-a-page)
- [326: Why can dvh hurt performance or cause content jumps?](#326-why-can-dvh-hurt-performance-or-cause-content-jumps)
- [327: How do web fonts cause layout shift and how do you reduce it?](#327-how-do-web-fonts-cause-layout-shift-and-how-do-you-reduce-it)
- [328: How do you make sure fluid type with clamp() still passes WCAG Resize Text?](#328-how-do-you-make-sure-fluid-type-with-clamp-still-passes-wcag-resize-text)
- [329: Do container query units have the same zoom problem as vw?](#329-do-container-query-units-have-the-same-zoom-problem-as-vw)
- [330: How do you support foldable devices?](#330-how-do-you-support-foldable-devices)
- [331: What does the VirtualKeyboard API do?](#331-what-does-the-virtualkeyboard-api-do)
- [332: Why do fixed elements behave strangely with the keyboard on iOS Safari?](#332-why-do-fixed-elements-behave-strangely-with-the-keyboard-on-ios-safari)
- [333: What is rubber-band scrolling and how does it affect fixed and sticky elements?](#333-what-is-rubber-band-scrolling-and-how-does-it-affect-fixed-and-sticky-elements)
- [334: How can subgrid help line up form fields inside nested components?](#334-how-can-subgrid-help-line-up-form-fields-inside-nested-components)
- [335: How does the browser size fr tracks when content is wider than the track?](#335-how-does-the-browser-size-fr-tracks-when-content-is-wider-than-the-track)
- [336: Why does height: 100% often not work, and what are better options?](#336-why-does-height-100-often-not-work-and-what-are-better-options)
- [337: What happens when aspect-ratio conflicts with content or min-height?](#337-what-happens-when-aspect-ratio-conflicts-with-content-or-min-height)
- [338: What is the automatic minimum size of flex and grid items?](#338-what-is-the-automatic-minimum-size-of-flex-and-grid-items)
- [339: What is the difference between flex-basis: 0 and flex-basis: auto when growing?](#339-what-is-the-difference-between-flex-basis-0-and-flex-basis-auto-when-growing)
- [340: Why can percentage gaps or padding cause overflow in grids?](#340-why-can-percentage-gaps-or-padding-cause-overflow-in-grids)
- [341: Why do fluid layouts sometimes show 1px gaps or misaligned edges?](#341-why-do-fluid-layouts-sometimes-show-1px-gaps-or-misaligned-edges)
- [342: Can media query ranges overlap or leave gaps?](#342-can-media-query-ranges-overlap-or-leave-gaps)
- [343: How does browser zoom affect media queries and devicePixelRatio?](#343-how-does-browser-zoom-affect-media-queries-and-devicepixelratio)
- [344: What does the CSS zoom property do?](#344-what-does-the-css-zoom-property-do)
- [345: How do you define a breakpoint strategy for a design system?](#345-how-do-you-define-a-breakpoint-strategy-for-a-design-system)
- [346: What are responsive props in component libraries and what are the trade-offs?](#346-what-are-responsive-props-in-component-libraries-and-what-are-the-trade-offs)
- [347: How should a server-rendered app handle responsive layouts?](#347-how-should-a-server-rendered-app-handle-responsive-layouts)
- [348: How do you avoid hydration mismatches caused by window size?](#348-how-do-you-avoid-hydration-mismatches-caused-by-window-size)
- [349: Why is serving different HTML based on the User-Agent bad for caching?](#349-why-is-serving-different-html-based-on-the-user-agent-bad-for-caching)
- [350: What is the cost of runtime CSS-in-JS for responsive styles?](#350-what-is-the-cost-of-runtime-css-in-js-for-responsive-styles)
- [351: What is critical CSS and how does it relate to mobile performance?](#351-what-is-critical-css-and-how-does-it-relate-to-mobile-performance)
- [352: Does splitting CSS with the media attribute on link tags improve performance?](#352-does-splitting-css-with-the-media-attribute-on-link-tags-improve-performance)
- [353: What should you think about when building for low-end phones?](#353-what-should-you-think-about-when-building-for-low-end-phones)
- [354: How do you get a good LCP on mobile for a page with a responsive hero image?](#354-how-do-you-get-a-good-lcp-on-mobile-for-a-page-with-a-responsive-hero-image)
- [355: How can a responsive layout cause CLS after the page loads?](#355-how-can-a-responsive-layout-cause-cls-after-the-page-loads)
- [356: How can a responsive menu hurt INP and how do you fix it?](#356-how-can-a-responsive-menu-hurt-inp-and-how-do-you-fix-it)
- [357: How do you make scroll-driven animations work well across screen sizes?](#357-how-do-you-make-scroll-driven-animations-work-well-across-screen-sizes)
- [358: How do view transitions help when a layout changes between views?](#358-how-do-view-transitions-help-when-a-layout-changes-between-views)
- [359: How do you respect reduced motion in JavaScript animations?](#359-how-do-you-respect-reduced-motion-in-javascript-animations)
- [360: What is the WCAG Focus Not Obscured criterion and how do sticky elements affect it?](#360-what-is-the-wcag-focus-not-obscured-criterion-and-how-do-sticky-elements-affect-it)
- [361: How do you keep accessible names when a responsive design hides text labels?](#361-how-do-you-keep-accessible-names-when-a-responsive-design-hides-text-labels)
- [362: How do you handle content that needs two-dimensional scrolling under the Reflow criterion?](#362-how-do-you-handle-content-that-needs-two-dimensional-scrolling-under-the-reflow-criterion)
- [363: What is the CSS reading-flow property?](#363-what-is-the-css-reading-flow-property)
- [364: How does the inert attribute help with responsive overlays?](#364-how-does-the-inert-attribute-help-with-responsive-overlays)
- [365: How do you build a responsive data table with thousands of rows?](#365-how-do-you-build-a-responsive-data-table-with-thousands-of-rows)
- [366: How do you keep a canvas sharp on high-DPR screens and at any size?](#366-how-do-you-keep-a-canvas-sharp-on-high-dpr-screens-and-at-any-size)
- [367: How do media queries inside an SVG work?](#367-how-do-media-queries-inside-an-svg-work)
- [368: What are the pros and cons of SVG icon sprites versus inline SVG and icon fonts?](#368-what-are-the-pros-and-cons-of-svg-icon-sprites-versus-inline-svg-and-icon-fonts)
- [369: What is font-size-adjust and why is it useful?](#369-what-is-font-size-adjust-and-why-is-it-useful)
- [370: How do you design responsive components for text expansion in other languages?](#370-how-do-you-design-responsive-components-for-text-expansion-in-other-languages)
- [371: How do vertical writing modes affect responsive layouts?](#371-how-do-vertical-writing-modes-affect-responsive-layouts)
- [372: How do you progressively enhance with a new layout feature like anchor positioning?](#372-how-do-you-progressively-enhance-with-a-new-layout-feature-like-anchor-positioning)
- [373: How do cascade layers help when third-party CSS fights your responsive styles?](#373-how-do-cascade-layers-help-when-third-party-css-fights-your-responsive-styles)
- [374: Why do responsive utility classes sometimes not apply, and how do you debug it?](#374-why-do-responsive-utility-classes-sometimes-not-apply-and-how-do-you-debug-it)
- [375: How do you decide which devices and browsers to test responsive layouts on?](#375-how-do-you-decide-which-devices-and-browsers-to-test-responsive-layouts-on)
- [376: How do you write an automated test that catches horizontal overflow?](#376-how-do-you-write-an-automated-test-that-catches-horizontal-overflow)
- [377: How do you run accessibility checks at mobile viewports?](#377-how-do-you-run-accessibility-checks-at-mobile-viewports)
- [378: How do you monitor responsive performance with real users?](#378-how-do-you-monitor-responsive-performance-with-real-users)
- [379: How do you test components at different container widths in Storybook?](#379-how-do-you-test-components-at-different-container-widths-in-storybook)
- [380: Scenario: The page scrolls horizontally only on iPhone Safari. How do you debug it?](#380-scenario-the-page-scrolls-horizontally-only-on-iphone-safari-how-do-you-debug-it)
- [381: Scenario: The page zooms in when users tap a form field on iPhone. What do you do?](#381-scenario-the-page-zooms-in-when-users-tap-a-form-field-on-iphone-what-do-you-do)
- [382: Scenario: The bottom of a full-height hero is cut off on phones. How do you fix it?](#382-scenario-the-bottom-of-a-full-height-hero-is-cut-off-on-phones-how-do-you-fix-it)
- [383: Scenario: A hover menu stays open after tapping on a phone. Why and how do you fix it?](#383-scenario-a-hover-menu-stays-open-after-tapping-on-a-phone-why-and-how-do-you-fix-it)
- [384: Scenario: Images look blurry on high-DPR screens. How do you fix it?](#384-scenario-images-look-blurry-on-high-dpr-screens-how-do-you-fix-it)
- [385: Scenario: Phones download 4000px wide images. How do you fix it?](#385-scenario-phones-download-4000px-wide-images-how-do-you-fix-it)
- [386: Scenario: The layout shifts sideways when navigating between short and long pages. Why?](#386-scenario-the-layout-shifts-sideways-when-navigating-between-short-and-long-pages-why)
- [387: Scenario: A sticky sidebar in a grid layout scrolls away instead of sticking. How do you fix it?](#387-scenario-a-sticky-sidebar-in-a-grid-layout-scrolls-away-instead-of-sticking-how-do-you-fix-it)
- [388: Scenario: A grid column overflows because of a long code block. How do you fix it?](#388-scenario-a-grid-column-overflows-because-of-a-long-code-block-how-do-you-fix-it)
- [389: Scenario: You need to make an old fixed-width float-based site responsive. How do you approach it?](#389-scenario-you-need-to-make-an-old-fixed-width-float-based-site-responsive-how-do-you-approach-it)
- [390: Scenario: Headings look huge on phones and tiny on large monitors. How do you fix it?](#390-scenario-headings-look-huge-on-phones-and-tiny-on-large-monitors-how-do-you-fix-it)
- [391: Scenario: On a landscape phone, the sticky header and a cookie banner cover most of the screen. What do you do?](#391-scenario-on-a-landscape-phone-the-sticky-header-and-a-cookie-banner-cover-most-of-the-screen-what-do-you-do)
- [392: Scenario: Users on touch-screen laptops see the mobile UI with a mouse. Why?](#392-scenario-users-on-touch-screen-laptops-see-the-mobile-ui-with-a-mouse-why)
- [393: Scenario: A designer gives you three different crops of the hero image for mobile, tablet and desktop. How do you implement it?](#393-scenario-a-designer-gives-you-three-different-crops-of-the-hero-image-for-mobile-tablet-and-desktop-how-do-you-implement-it)
- [394: Scenario: The same card component is used in a narrow sidebar and a wide main column. How do you make it look right in both?](#394-scenario-the-same-card-component-is-used-in-a-narrow-sidebar-and-a-wide-main-column-how-do-you-make-it-look-right-in-both)
- [395: Scenario: You need to add right-to-left support to an existing responsive site. How do you plan it?](#395-scenario-you-need-to-add-right-to-left-support-to-an-existing-responsive-site-how-do-you-plan-it)
- [396: Scenario: Scrolling is janky on low-end Android phones. How do you find and fix the cause?](#396-scenario-scrolling-is-janky-on-low-end-android-phones-how-do-you-find-and-fix-the-cause)
- [397: Scenario: In a chat app, the message input is hidden behind the keyboard on mobile. How do you fix it?](#397-scenario-in-a-chat-app-the-message-input-is-hidden-behind-the-keyboard-on-mobile-how-do-you-fix-it)
- [398: Scenario: A modal's content is taller than the screen on mobile. How do you fix it?](#398-scenario-a-modals-content-is-taller-than-the-screen-on-mobile-how-do-you-fix-it)
- [399: Scenario: A fixed "Buy now" bar at the bottom overlaps the footer and the iPhone home indicator. How do you fix it?](#399-scenario-a-fixed-buy-now-bar-at-the-bottom-overlaps-the-footer-and-the-iphone-home-indicator-how-do-you-fix-it)
- [400: Scenario: You need to show a table with 20 columns on mobile. What options do you present?](#400-scenario-you-need-to-show-a-table-with-20-columns-on-mobile-what-options-do-you-present)
- [401: Scenario: CLS is bad only on mobile. How do you find the cause?](#401-scenario-cls-is-bad-only-on-mobile-how-do-you-find-the-cause)
- [402: Scenario: LCP is good on desktop but bad on mobile. What do you check?](#402-scenario-lcp-is-good-on-desktop-but-bad-on-mobile-what-do-you-check)
- [403: Scenario: The nav items wrap to two lines at a certain width. How do you fix it?](#403-scenario-the-nav-items-wrap-to-two-lines-at-a-certain-width-how-do-you-fix-it)
- [404: Scenario: In dark mode, photos and white illustrations look too bright. What can you do?](#404-scenario-in-dark-mode-photos-and-white-illustrations-look-too-bright-what-can-you-do)
- [405: Scenario: Users with low vision say the text doesn't get bigger when they zoom. What's wrong?](#405-scenario-users-with-low-vision-say-the-text-doesnt-get-bigger-when-they-zoom-whats-wrong)
- [406: Scenario: A third-party widget breaks the layout on small screens. What are your options?](#406-scenario-a-third-party-widget-breaks-the-layout-on-small-screens-what-are-your-options)
- [407: Scenario: A JavaScript carousel is janky on mobile. How would you rebuild it?](#407-scenario-a-javascript-carousel-is-janky-on-mobile-how-would-you-rebuild-it)
- [408: Scenario: Users want to print a dashboard. How do you make it print well?](#408-scenario-users-want-to-print-a-dashboard-how-do-you-make-it-print-well)
- [409: Scenario: How would you design the responsive layout of a product page?](#409-scenario-how-would-you-design-the-responsive-layout-of-a-product-page)
- [410: Scenario: How do you build a responsive multi-step form?](#410-scenario-how-do-you-build-a-responsive-multi-step-form)
- [411: Scenario: A full-screen background video is slow on mobile. What do you do?](#411-scenario-a-full-screen-background-video-is-slow-on-mobile-what-do-you-do)
- [412: Scenario: Your web app must also work on a TV browser. What changes?](#412-scenario-your-web-app-must-also-work-on-a-tv-browser-what-changes)
- [413: Scenario: You build a widget that other sites embed in an iframe. How do you make it responsive?](#413-scenario-you-build-a-widget-that-other-sites-embed-in-an-iframe-how-do-you-make-it-responsive)
- [414: Scenario: Several micro-frontends on one page use different breakpoints. How do you fix it?](#414-scenario-several-micro-frontends-on-one-page-use-different-breakpoints-how-do-you-fix-it)
- [415: Scenario: How do you build a gallery of images with mixed aspect ratios that forms neat rows?](#415-scenario-how-do-you-build-a-gallery-of-images-with-mixed-aspect-ratios-that-forms-neat-rows)
- [416: How do you animate an accordion opening to its content height?](#416-how-do-you-animate-an-accordion-opening-to-its-content-height)
- [417: How do you animate a menu in when it goes from display: none to visible?](#417-how-do-you-animate-a-menu-in-when-it-goes-from-display-none-to-visible)
- [418: What is the customizable select and why does it matter for responsive forms?](#418-what-is-the-customizable-select-and-why-does-it-matter-for-responsive-forms)
- [419: How would you build a popover that is a dropdown on desktop and a bottom sheet on mobile?](#419-how-would-you-build-a-popover-that-is-a-dropdown-on-desktop-and-a-bottom-sheet-on-mobile)
- [420: What can round() and mod() do in responsive layouts?](#420-what-can-round-and-mod-do-in-responsive-layouts)
- [421: What happens when the minimum in clamp() is larger than the maximum?](#421-what-happens-when-the-minimum-in-clamp-is-larger-than-the-maximum)
- [422: What should you watch out for with % and em inside clamp() for font-size?](#422-what-should-you-watch-out-for-with--and-em-inside-clamp-for-font-size)
- [423: How do media queries behave inside an iframe?](#423-how-do-media-queries-behave-inside-an-iframe)
- [424: How do you generate responsive images in a build pipeline?](#424-how-do-you-generate-responsive-images-in-a-build-pipeline)
- [425: What are the trade-offs between AVIF, WebP and JPEG for responsive images?](#425-what-are-the-trade-offs-between-avif-webp-and-jpeg-for-responsive-images)
- [426: How do responsive images affect SEO?](#426-how-do-responsive-images-affect-seo)
- [427: What does mobile-first indexing mean for responsive sites?](#427-what-does-mobile-first-indexing-mean-for-responsive-sites)
- [428: What are the SEO risks of serving different HTML to mobile and desktop?](#428-what-are-the-seo-risks-of-serving-different-html-to-mobile-and-desktop)
- [429: Can media queries be used to fingerprint users?](#429-can-media-queries-be-used-to-fingerprint-users)
- [430: What are common Safari-specific responsive problems?](#430-what-are-common-safari-specific-responsive-problems)
- [431: Where should containment go in a component library that uses container queries?](#431-where-should-containment-go-in-a-component-library-that-uses-container-queries)
- [432: What are the downsides of making every element a container?](#432-what-are-the-downsides-of-making-every-element-a-container)
- [433: Scenario: A container inside a flex row collapses to zero width. Why, and how do you fix it?](#433-scenario-a-container-inside-a-flex-row-collapses-to-zero-width-why-and-how-do-you-fix-it)
- [434: What is the difference between the layout viewport and the visual viewport?](#434-what-is-the-difference-between-the-layout-viewport-and-the-visual-viewport)
- [435: Why do fixed elements seem to move when users pinch-zoom on mobile?](#435-why-do-fixed-elements-seem-to-move-when-users-pinch-zoom-on-mobile)
- [436: What is the Window Controls Overlay and how does it affect layout?](#436-what-is-the-window-controls-overlay-and-how-does-it-affect-layout)
- [437: What is the cost difference between hiding a responsive variant with CSS and not rendering it?](#437-what-is-the-cost-difference-between-hiding-a-responsive-variant-with-css-and-not-rendering-it)
- [438: Does an img inside an element with display: none still download?](#438-does-an-img-inside-an-element-with-display-none-still-download)
- [439: Which background images download when they are set in different media queries?](#439-which-background-images-download-when-they-are-set-in-different-media-queries)
- [440: Does loading="lazy" work for images in a horizontal carousel?](#440-does-loadinglazy-work-for-images-in-a-horizontal-carousel)
- [441: How would you define a responsive strategy for a new product?](#441-how-would-you-define-a-responsive-strategy-for-a-new-product)
- [442: The design team only provides designs at 375px and 1440px. How do you handle the widths in between?](#442-the-design-team-only-provides-designs-at-375px-and-1440px-how-do-you-handle-the-widths-in-between)
- [443: Why does a fixed-position element inside a container sometimes stop being fixed to the viewport?](#443-why-does-a-fixed-position-element-inside-a-container-sometimes-stop-being-fixed-to-the-viewport)
- [444: How do you test a responsive layout with a screen reader on a phone?](#444-how-do-you-test-a-responsive-layout-with-a-screen-reader-on-a-phone)
- [445: How do you handle orientation changes in JavaScript?](#445-how-do-you-handle-orientation-changes-in-javascript)
- [446: What is different about responsive layouts inside a native app's webview?](#446-what-is-different-about-responsive-layouts-inside-a-native-apps-webview)
- [447: Can you build a responsive layout without any media queries? When is that not enough?](#447-can-you-build-a-responsive-layout-without-any-media-queries-when-is-that-not-enough)
- [448: Scenario: A table of contents is a sticky sidebar on desktop and a collapsible section on mobile. How do you build it with one piece of HTML?](#448-scenario-a-table-of-contents-is-a-sticky-sidebar-on-desktop-and-a-collapsible-section-on-mobile-how-do-you-build-it-with-one-piece-of-html)
- [449: Scenario: Filters are a sidebar on desktop and a full-screen dialog on mobile. How do you avoid duplicating the markup?](#449-scenario-filters-are-a-sidebar-on-desktop-and-a-full-screen-dialog-on-mobile-how-do-you-avoid-duplicating-the-markup)
- [450: What has changed in responsive design in recent years, and what is coming next?](#450-what-has-changed-in-responsive-design-in-recent-years-and-what-is-coming-next)

---

# Easy Questions (1-150)

## 1: What is responsive web design?

Responsive web design means building one website that adjusts its layout, images and text to fit the screen it is shown on. The same HTML is served to phones, tablets, laptops and large monitors, and CSS changes how it looks based on the available space.

Instead of building a separate mobile site, you use flexible layouts, flexible images and media queries (or container queries) so the page works at any width.

## 2: Who came up with the term responsive web design and what were its three original parts?

Ethan Marcotte introduced the term in an article on A List Apart in 2010. His approach had three parts:

- **Fluid grids** - layout widths in relative units like percentages instead of fixed pixels.
- **Flexible images** - images that scale down inside their containers, for example with `max-width: 100%`.
- **Media queries** - CSS rules that apply only at certain screen sizes.

Today we also have Flexbox, Grid, container queries and `clamp()`, but the idea is the same.

## 3: What is the difference between responsive and adaptive design?

A **responsive** layout is fluid. It stretches and shrinks smoothly with the viewport and changes at breakpoints when needed.

An **adaptive** layout has a few fixed layouts (for example 320px, 768px and 1024px wide) and picks the closest one. Between those sizes the layout doesn't stretch, so you may get empty space or a fixed width. Some adaptive sites even serve different HTML per device, detected on the server.

Responsive design is the common choice today because there are too many screen sizes to design a fixed layout for each one.

## 4: What is the viewport?

The viewport is the visible area of the page inside the browser window. On desktop it is the browser window minus toolbars and scrollbars. On mobile it is the screen area where the page is drawn.

Media queries with `width` and viewport units like `vw` and `vh` are measured against the viewport.

## 5: What does the viewport meta tag do?

It tells mobile browsers how wide the page should be and how much to zoom in at first.

```html
<meta name="viewport" content="width=device-width, initial-scale=1" />
```

- `width=device-width` sets the layout viewport width to the device width in CSS pixels (for example 390px on many phones).
- `initial-scale=1` shows the page at 100% zoom when it loads.

You put it in the `<head>` of every page. Without it, responsive CSS doesn't work properly on phones.

## 6: What happens if you leave out the viewport meta tag?

Mobile browsers assume the page was built for desktop. They render it at a wide virtual width (usually around 980px) and then zoom out so the whole page fits on the screen.

The result is tiny text that users have to pinch to read, and your `min-width` and `max-width` media queries respond to that 980px width instead of the real phone width. So your mobile styles never kick in.

## 7: Why should you avoid user-scalable=no and maximum-scale=1?

They stop or limit pinch zoom. People with low vision rely on zoom to read text and see details, so blocking it is an accessibility problem and fails WCAG.

```html
<!-- Don't do this -->
<meta
  name="viewport"
  content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no"
/>

<!-- Do this -->
<meta name="viewport" content="width=device-width, initial-scale=1" />
```

Some browsers, like Safari on iOS, ignore `user-scalable=no` for this reason. If you added it to stop iOS from zooming in on form fields, fix the font size of the inputs instead (16px or more).

## 8: What is a media query?

A media query applies a block of CSS only when a condition is true. The condition is usually about the viewport width, but it can also be about orientation, pointer type, or user settings like dark mode.

```css
.sidebar {
  display: none;
}

@media (width >= 900px) {
  .sidebar {
    display: block;
  }
}
```

Here the sidebar is hidden by default and shown when the viewport is at least 900px wide.

## 9: What is the syntax of a media query?

A media query has an optional media type and one or more media features in parentheses, joined with logical keywords.

```css
@media screen and (min-width: 600px) and (orientation: landscape) {
  /* styles */
}
```

- `screen` is the media type.
- `(min-width: 600px)` and `(orientation: landscape)` are media features.
- `and` joins conditions. A comma means "or". `not` negates a query.

The media type is often left out, which means `all`.

## 10: What media types exist?

There are three you should know:

- `all` - every device. This is the default when you don't write a type.
- `screen` - screens like phones, tablets and monitors.
- `print` - printed pages and print preview.

Older types like `handheld`, `tv` and `projection` are deprecated and browsers treat them as never matching.

## 11: What is a breakpoint?

A breakpoint is a width at which the layout changes. For example, at 768px a single-column layout might switch to two columns. Breakpoints are usually written as media queries or container queries.

```css
.grid {
  display: grid;
  grid-template-columns: 1fr;
}

@media (width >= 768px) {
  .grid {
    grid-template-columns: 1fr 1fr;
  }
}
```

## 12: How do you choose breakpoints?

Choose them based on your content, not on specific devices. Start with the narrow layout, slowly widen the browser and add a breakpoint where the design starts to look wrong: lines get too long, cards get too wide, or there is too much empty space.

Device sizes change every year, so breakpoints tied to "iPhone" or "iPad" go out of date. Content-based breakpoints keep working. Most sites end up with three to five main breakpoints, plus small tweaks inside components.

## 13: What is mobile-first design?

Mobile-first means you write the styles for small screens first, as the default, and then add styles for bigger screens with `min-width` media queries.

```css
.nav {
  display: flex;
  flex-direction: column;
}

@media (width >= 768px) {
  .nav {
    flex-direction: row;
  }
}
```

Small screens get the simplest CSS and don't have to override desktop rules. It also forces you to decide what content really matters, because there is less room.

## 14: What is the difference between min-width and max-width media queries?

- `min-width: 768px` matches when the viewport is **768px or wider**. It is used in mobile-first CSS.
- `max-width: 767px` matches when the viewport is **767px or narrower**. It is used in desktop-first CSS.

```css
/* Applies from 768px up */
@media (min-width: 768px) {
}

/* Applies from 767px down */
@media (max-width: 767px) {
}
```

Both include the value itself. With the newer range syntax you can write `(width >= 768px)` and `(width < 768px)`, which is easier to read and avoids gaps between ranges.

## 15: What is desktop-first design?

Desktop-first means the default styles are for large screens, and you use `max-width` media queries to change things for smaller screens.

```css
.columns {
  display: flex;
}

@media (max-width: 767px) {
  .columns {
    flex-direction: column;
  }
}
```

It is common in older projects. The downside is that phones have to download and then undo desktop styles, and the CSS tends to fill up with overrides. Mobile-first is usually easier to maintain.

## 16: What is the media query range syntax?

It lets you write width conditions with comparison operators instead of `min-` and `max-` prefixes. It works in all major browsers.

```css
/* Old */
@media (min-width: 600px) and (max-width: 899px) {
}

/* New */
@media (600px <= width < 900px) {
}
```

It is easier to read and solves the "off by one" problem. With `max-width: 899px` there is a tiny gap between 899px and 900px on screens with fractional widths. With `width < 900px` there is no gap.

## 17: How do you combine conditions in a media query?

- `and` - all conditions must be true.
- `,` (comma) or `or` - at least one query must be true.
- `not` - negates the condition.

```css
/* Both conditions */
@media (width >= 768px) and (orientation: landscape) {
}

/* Either one */
@media (width < 400px), (height < 400px) {
}

/* Media queries level 4 also allows "or" inside one query */
@media (width < 400px) or (height < 400px) {
}
```

## 18: What does the not keyword do in a media query?

`not` reverses the result of a media query. If the condition is true, the styles do not apply, and the other way around.

```css
@media not print {
  .screen-only-banner {
    display: block;
  }
}

/* Level 4 syntax lets you negate a single feature */
@media not (hover: hover) {
  .tooltip {
    display: none;
  }
}
```

In a comma-separated list, `not` only applies to the query it is in, not the whole list.

## 19: What does the only keyword do in a media query?

`only` was added to hide media queries from very old browsers that didn't understand media features. Those browsers would read `screen and (min-width: 600px)` as just `screen` and apply the styles everywhere. With `only screen`, they didn't recognize the type and skipped the rule.

Modern browsers ignore `only`, so you don't need it today. You will still see `only screen and (...)` in older code.

## 20: How do you load a stylesheet only for certain screens using HTML?

Use the `media` attribute on the `<link>` element.

```html
<link rel="stylesheet" href="base.css" />
<link rel="stylesheet" href="wide.css" media="(width >= 1024px)" />
<link rel="stylesheet" href="print.css" media="print" />
```

The browser still downloads all three files, but files whose media query doesn't match are downloaded with low priority and don't block rendering. The same `media` attribute works on `<style>` and `<source>` elements.

## 21: What is a fluid layout?

A fluid layout uses relative widths (percentages, `fr`, `flex`) so the page stretches and shrinks with the viewport instead of having a fixed size.

```css
.main {
  width: 70%;
}

.sidebar {
  width: 30%;
}
```

A fluid layout alone is not enough. At very small widths columns get too narrow, and at very large widths lines get too long. You combine it with breakpoints and `max-width`.

## 22: What is a fixed-width layout and why is it a problem?

A fixed-width layout sets the page to a set width in pixels, like `width: 960px`. It looks the same on every screen that is wide enough.

On a screen narrower than that width, the user gets horizontal scrolling or a zoomed-out page. On a very wide screen, there are large empty areas on the sides. Replacing `width` with `max-width` is often the first step to making an old fixed layout responsive:

```css
.container {
  max-width: 960px;
  margin-inline: auto;
}
```

## 23: What is the difference between px, em and rem?

- `px` - a fixed CSS pixel. It doesn't change with the user's font size setting.
- `em` - relative to the font size of the current element. For the `font-size` property itself, it's relative to the parent's font size.
- `rem` - relative to the font size of the root `<html>` element, which is 16px by default.

```css
html {
  font-size: 100%; /* 16px by default */
}

.card {
  padding: 1rem; /* 16px */
  font-size: 1.25rem; /* 20px */
}

.card button {
  padding: 0.5em; /* 10px, half of the card's 20px font size */
}
```

## 24: Why should you use rem for font sizes?

Because `rem` respects the default font size the user set in their browser. If someone increases the default from 16px to 24px, text sized in `rem` grows with it. Text sized in `px` does not.

`rem` is also predictable. It always points to the root font size, so you don't get the compounding effect of nested `em` values.

## 25: What are percentage values relative to?

It depends on the property:

- `width`, `padding`, `margin` (all sides, even top and bottom) - the width of the containing block.
- `height` - the height of the containing block, but only if that height is set explicitly. Otherwise it usually acts like `auto`.
- `font-size` - the parent's font size.
- `transform: translate()` - the element's own size.
- `top`/`bottom` on a positioned element - the containing block's height. `left`/`right` - its width.

The fact that vertical padding uses the width was used in the old "padding-top: 56.25%" trick for 16:9 boxes, before `aspect-ratio` existed.

## 26: What are the vw and vh units?

- `1vw` is 1% of the viewport width.
- `1vh` is 1% of the viewport height.

```css
.hero {
  height: 80vh;
}

.big-title {
  font-size: 8vw;
}
```

They are useful for full-screen sections and fluid sizes. Be careful with `100vw`: it includes the vertical scrollbar width on desktop, so `width: 100vw` can cause a horizontal scrollbar. On mobile, `vh` has problems with the browser toolbar (see the next questions).

## 27: What are vmin and vmax?

- `vmin` is 1% of the viewport's smaller side.
- `vmax` is 1% of the viewport's larger side.

On a 400 x 800 phone in portrait, `1vmin` is 4px and `1vmax` is 8px. Rotate it to landscape and the values stay the same, because the smaller and larger sides swap.

`vmin` is handy when you want something to fit in both portrait and landscape, like a square that never overflows: `width: 80vmin; height: 80vmin;`.

## 28: Why is 100vh a problem on mobile?

On mobile browsers the address bar and toolbar show and hide as you scroll. Browsers decided that `100vh` means the height with the toolbars **hidden** (the largest size). So when the page first loads and the toolbars are visible, an element with `height: 100vh` is taller than the visible area and the bottom gets cut off.

The fix is to use the newer viewport units: `svh`, `lvh` and `dvh`.

```css
.hero {
  min-height: 100svh;
}
```

## 29: What are svh, lvh and dvh?

They are viewport height units that handle the mobile browser toolbar:

- `svh` (small viewport height) - the height when the toolbars are **visible**. The smallest possible viewport.
- `lvh` (large viewport height) - the height when the toolbars are **hidden**. The largest possible viewport. Same as the old `vh`.
- `dvh` (dynamic viewport height) - changes as the toolbars show and hide.

```css
.full-screen {
  height: 100vh; /* fallback for very old browsers */
  height: 100dvh;
}
```

There are matching width and inline/block versions too: `svw`, `lvw`, `dvw`, `svi`, `dvb` and so on. Use `svh` for most layouts, because `dvh` can make the layout jump while scrolling.

## 30: What does max-width: 100% do on images?

It stops an image from being wider than its container. If the container is narrower than the image's natural width, the image shrinks to fit. If the container is wider, the image stays at its natural size and doesn't get stretched and blurry.

```css
img {
  max-width: 100%;
  height: auto;
}
```

This is one of the first rules in almost every responsive CSS file.

## 31: Why do you add height: auto to responsive images?

If the image has a `height` attribute in the HTML (which it should, to prevent layout shift), the browser would keep that height while `max-width: 100%` shrinks the width. The image would get squished.

`height: auto` tells the browser to calculate the height from the width and the image's aspect ratio, so it scales correctly.

```html
<img src="photo.jpg" width="1200" height="800" alt="Mountain lake" />
```

```css
img {
  max-width: 100%;
  height: auto;
}
```

## 32: What is box-sizing: border-box and why is it used?

By default (`content-box`), `width` sets only the content width. Padding and border are added on top, so a `width: 100%` element with padding ends up wider than its parent and overflows.

With `border-box`, `width` includes padding and border, so `width: 100%` really means 100%.

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

This makes percentage and fluid layouts much easier to reason about, which is why almost every project sets it globally.

## 33: What base CSS rules help a responsive layout?

A few rules at the top of the stylesheet prevent the most common problems:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}

body {
  margin: 0;
  min-height: 100svh;
}

img,
picture,
video,
canvas,
svg {
  display: block;
  max-width: 100%;
  height: auto;
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
h3 {
  overflow-wrap: break-word;
}
```

They fix box sizing, stop media from overflowing, make form controls use the page font, and let long words wrap.

## 34: What is Flexbox?

Flexbox (the flexible box layout) is a CSS layout model for laying out items in one direction, either a row or a column. It handles spacing, alignment and how items grow or shrink to fill the space.

```css
.toolbar {
  display: flex;
  align-items: center;
  gap: 1rem;
}
```

It is good for navigation bars, button groups, form rows, centering, and any one-dimensional list of items that should wrap or share space.

## 35: What are the main axis and cross axis in Flexbox?

The main axis is the direction items are placed in. With `flex-direction: row` it is horizontal, with `column` it is vertical. The cross axis runs perpendicular to it.

- `justify-content` aligns items along the main axis.
- `align-items` and `align-self` align items along the cross axis.

So when you switch `flex-direction` from `row` to `column` at a breakpoint, `justify-content` changes from horizontal to vertical alignment. This catches people out.

## 36: What does flex-direction do?

It sets the main axis of a flex container.

- `row` (default) - left to right in left-to-right languages.
- `row-reverse` - right to left.
- `column` - top to bottom.
- `column-reverse` - bottom to top.

A common responsive pattern is stacking items in a column on mobile and putting them in a row on wider screens:

```css
.features {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

@media (width >= 768px) {
  .features {
    flex-direction: row;
  }
}
```

## 37: What does flex-wrap do?

By default, flex items stay on one line and shrink to fit, even if they get very narrow. `flex-wrap: wrap` lets them move to a new line when there isn't enough room.

```css
.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}
```

With wrapping, a list of tags or cards can adapt to any width without a media query.

## 38: What does justify-content do?

It distributes extra space between and around flex or grid items along the main axis.

- `flex-start` / `start` - items packed at the start.
- `flex-end` / `end` - items packed at the end.
- `center` - items in the middle.
- `space-between` - first and last item on the edges, equal space between the rest.
- `space-around` - equal space around each item (half-size space at the edges).
- `space-evenly` - equal space everywhere, including the edges.

```css
.header {
  display: flex;
  justify-content: space-between; /* logo left, menu right */
}
```

## 39: What does align-items do?

It aligns items along the cross axis of a flex or grid container.

- `stretch` (default in flex) - items fill the container's cross size.
- `flex-start` / `start` - aligned to the start.
- `flex-end` / `end` - aligned to the end.
- `center` - centered.
- `baseline` - aligned by their text baseline.

`align-self` does the same for a single item.

## 40: What does the gap property do?

`gap` sets the space between rows and columns in Flexbox, Grid and multi-column layouts. It only adds space between items, not on the outer edges.

```css
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem 1rem; /* row gap, column gap */
}
```

Before `gap` worked in Flexbox, people used margins on the items and negative margins on the container. `gap` is much simpler and works in all modern browsers.

## 41: What do flex-grow, flex-shrink and flex-basis do?

- `flex-basis` - the starting size of the item before free space is shared out. Can be a length or `auto` (use the item's width or content size).
- `flex-grow` - how much of the leftover space the item takes, compared with the other items. `0` means don't grow.
- `flex-shrink` - how much the item shrinks when there isn't enough space. `0` means don't shrink.

```css
.sidebar {
  flex: 0 0 250px; /* don't grow, don't shrink, 250px wide */
}

.content {
  flex: 1 1 0; /* take all remaining space */
}
```

## 42: What does flex: 1 mean?

`flex: 1` is shorthand for `flex-grow: 1; flex-shrink: 1; flex-basis: 0%`. Items with `flex: 1` start from zero and share all the space equally, so they end up the same width regardless of their content.

Compare with `flex: auto` (`1 1 auto`), where items start at their content size and then share the extra space, so items with more content end up wider.

```css
.tabs > * {
  flex: 1; /* equal-width tabs */
}
```

## 43: How do you center an element horizontally and vertically?

The shortest ways today use Grid or Flexbox:

```css
/* Grid */
.parent {
  display: grid;
  place-items: center;
}

/* Flexbox */
.parent {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

To center a block element horizontally only, give it a width (or `max-width`) and `margin-inline: auto`. Older code uses `position: absolute` with `top: 50%; left: 50%; transform: translate(-50%, -50%)`, which still works but is more fragile.

## 44: What is CSS Grid?

CSS Grid is a layout model for two dimensions: rows and columns at the same time. You define a grid on the container and place items into its cells or let the browser place them automatically.

```css
.page {
  display: grid;
  grid-template-columns: 250px 1fr;
  grid-template-rows: auto 1fr auto;
  gap: 1rem;
}
```

It is good for page layouts, card grids, dashboards and anything where things need to line up both across and down.

## 45: What is the difference between Flexbox and Grid?

- **Flexbox** is one-dimensional. It lays items out in a row or a column, and each line sizes itself based on its own content. It works from the content out.
- **Grid** is two-dimensional. You define rows and columns, and items line up in both directions. It works from the layout in.

Use Flexbox for things like a nav bar, a row of buttons, or a list of tags that wraps. Use Grid for page layouts, card grids where columns should line up, and layouts that change shape at breakpoints. They are often used together: a grid for the page and flex inside the components.

## 46: What is the fr unit?

`fr` means a fraction of the free space in a grid container. After fixed sizes and gaps are taken out, the leftover space is split based on the `fr` values.

```css
.layout {
  display: grid;
  grid-template-columns: 200px 2fr 1fr;
}
```

Here the first column is 200px. The rest is split into three parts: the second column gets two parts and the third gets one.

## 47: What does repeat() do in CSS Grid?

`repeat()` saves you from writing the same track size many times.

```css
/* Same as: 1fr 1fr 1fr 1fr */
grid-template-columns: repeat(4, 1fr);

/* Repeats a pattern: 100px 1fr 100px 1fr */
grid-template-columns: repeat(2, 100px 1fr);
```

The first argument can also be `auto-fill` or `auto-fit`, which lets the browser decide how many columns fit. That's the basis for responsive grids without media queries.

## 48: What does minmax() do?

`minmax(min, max)` defines a grid track size that is never smaller than `min` and never larger than `max`.

```css
grid-template-columns: minmax(200px, 300px) 1fr;
grid-template-rows: minmax(100px, auto);
```

The first column is between 200px and 300px. The rows are at least 100px tall but grow if the content needs more room. It's mostly used together with `repeat(auto-fit, ...)`.

## 49: What is the difference between auto-fill and auto-fit?

Both create as many columns as will fit. The difference shows when there are fewer items than columns:

- `auto-fill` keeps the empty columns, so items stay at their minimum size and there is empty space at the end.
- `auto-fit` collapses empty columns to zero, so the existing items stretch to fill the row.

```css
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}
```

With 2 items on a 1000px wide container, `auto-fit` gives two 500px cards. `auto-fill` gives two 200px-ish cards and empty space. When the row is full, they behave the same.

## 50: How do you make a responsive card grid without media queries?

Use `repeat(auto-fit, minmax(...))`:

```css
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(250px, 100%), 1fr));
  gap: 1rem;
}
```

The browser fits as many columns as possible where each one is at least 250px, and stretches them to fill the row. On a phone you get one column, on a tablet two or three, on desktop four or more.

The `min(250px, 100%)` part stops the cards from overflowing when the container is narrower than 250px.

## 51: What is grid-template-areas?

It lets you name areas of the grid and draw the layout as text. Each string is a row and each word is a cell.

```css
.page {
  display: grid;
  grid-template-columns: 200px 1fr;
  grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer";
}

.page-header {
  grid-area: header;
}
.page-sidebar {
  grid-area: sidebar;
}
.page-main {
  grid-area: main;
}
.page-footer {
  grid-area: footer;
}
```

A `.` marks an empty cell. Every area must be a rectangle.

## 52: How do you change a grid layout at a breakpoint?

Redefine the columns or areas inside a media query. The HTML doesn't change.

```css
.page {
  display: grid;
  grid-template-areas:
    "header"
    "main"
    "sidebar"
    "footer";
}

@media (width >= 900px) {
  .page {
    grid-template-columns: 1fr 250px;
    grid-template-areas:
      "header header"
      "main sidebar"
      "footer footer";
  }
}
```

On mobile everything is stacked. On wide screens the sidebar moves next to the main content. Named areas make this very readable.

## 53: How do you make a grid item span multiple columns or rows?

Use `grid-column` and `grid-row` with `span` or with line numbers.

```css
.featured {
  grid-column: span 2;
}

.banner {
  grid-column: 1 / -1; /* from the first to the last line, full width */
}

.tall {
  grid-row: span 2;
}
```

Be careful with `span` in responsive grids. If the grid drops to one column and an item still has `span 2`, the browser adds an extra implicit column and the layout overflows. Reset the span at small sizes or only add it inside a media query.

## 54: What does the order property do and why should you be careful with it?

`order` changes the visual order of flex and grid items. Items with a lower value come first. The default is `0`.

```css
.sidebar {
  order: 2;
}

.content {
  order: 1;
}
```

The problem is that it only changes what you see. Screen readers and the Tab key still follow the HTML order. If the visual order and the DOM order are very different, keyboard users jump around the page in a confusing way. Use it for small visual changes and keep the HTML in a logical reading order.

## 55: What is the srcset attribute?

`srcset` gives the browser a list of image files of different sizes or resolutions. The browser picks the best one for the screen.

```html
<img
  src="photo-800.jpg"
  srcset="photo-400.jpg 400w, photo-800.jpg 800w, photo-1600.jpg 1600w"
  sizes="(width >= 900px) 50vw, 100vw"
  alt="A dog running on the beach"
/>
```

`src` is the fallback for very old browsers. A phone gets the small file and a large retina screen gets the big one, which saves a lot of data on mobile.

## 56: What is the sizes attribute?

`sizes` tells the browser how wide the image will be shown on the page, before the CSS is loaded. The browser uses that with `w` descriptors in `srcset` to choose a file.

```html
<img
  srcset="card-300.jpg 300w, card-600.jpg 600w, card-900.jpg 900w"
  sizes="(width >= 1200px) 300px, (width >= 600px) 50vw, 100vw"
  src="card-600.jpg"
  alt="Product photo"
/>
```

The browser reads the list from left to right and uses the first media condition that matches. The last value has no condition and is the default. If you leave `sizes` out, the browser assumes `100vw` and may download a much bigger image than needed.

## 57: What is the picture element?

`<picture>` wraps an `<img>` and one or more `<source>` elements. The browser goes through the sources in order and uses the first one that matches its `media` or `type`. If none match, it uses the `<img>`.

```html
<picture>
  <source media="(width >= 900px)" srcset="hero-wide.jpg" />
  <source media="(width >= 500px)" srcset="hero-medium.jpg" />
  <img src="hero-narrow.jpg" alt="Team working at a table" />
</picture>
```

The `<img>` is required. It is the element that is actually displayed, and it carries `alt`, `width`, `height`, `loading` and the CSS styles.

## 58: What is the difference between resolution switching and art direction?

- **Resolution switching** - the same image at different sizes. The browser picks a file that matches the screen size and pixel density. You use `srcset` and `sizes` on `<img>`.
- **Art direction** - a different image or a different crop for different layouts. For example, a wide landscape photo on desktop and a tight portrait crop on mobile so the subject is still visible. You use `<picture>` with `media` on each `<source>`.

With resolution switching the browser makes the choice. With art direction you make it, because `media` on `<source>` is a strict rule.

## 59: What are x descriptors and w descriptors in srcset?

- **x descriptors** describe pixel density. Use them when the image is shown at a fixed size, like a logo or avatar.

```html
<img src="logo.png" srcset="logo.png 1x, logo@2x.png 2x" alt="Company logo" />
```

- **w descriptors** describe the file's real width in pixels. Use them when the image size changes with the layout. They need `sizes`.

```html
<img
  srcset="img-480.jpg 480w, img-960.jpg 960w"
  sizes="100vw"
  src="img-960.jpg"
  alt="..."
/>
```

You can't mix `x` and `w` in the same `srcset`.

## 60: What is the difference between CSS pixels and device pixels?

A CSS pixel is the unit you use in your stylesheets. A device pixel is a real dot on the screen. On high-density screens, one CSS pixel is drawn with several device pixels.

The ratio is called the **device pixel ratio** (DPR). An iPhone with a DPR of 3 shows a 100 x 100 CSS pixel box with 300 x 300 device pixels. This is why a 100px wide image looks blurry on such a screen and why you serve 2x or 3x images with `srcset`.

## 61: How do you get the device pixel ratio in JavaScript?

Use `window.devicePixelRatio`.

```js
console.log(window.devicePixelRatio); // 1 on most old monitors, 2 or 3 on phones
```

The value also changes when the user zooms the page in desktop browsers. To react to changes, listen to a resolution media query:

```js
const mq = matchMedia(`(resolution: ${window.devicePixelRatio}dppx)`);
mq.addEventListener("change", () => {
  console.log("DPR changed to", window.devicePixelRatio);
});
```

## 62: Why should you set width and height attributes on images?

So the browser can reserve the right amount of space before the image loads. Browsers use the two numbers to calculate the aspect ratio. Without them, the image starts at 0 height and then pushes the content down when it loads. That jump is a layout shift and hurts the Cumulative Layout Shift (CLS) score.

```html
<img src="photo.jpg" width="1600" height="900" alt="City at night" />
```

```css
img {
  max-width: 100%;
  height: auto;
}
```

The numbers only need the right ratio. CSS still controls the displayed size.

## 63: What does loading="lazy" do?

It tells the browser to wait before downloading an image or iframe until the user scrolls near it.

```html
<img src="gallery-5.jpg" loading="lazy" width="800" height="600" alt="..." />
<iframe src="https://example.com/map" loading="lazy" title="Map"></iframe>
```

It saves data and speeds up the first load, which is important on mobile. Don't lazy load images that are visible at the top of the page, especially the main hero image. That delays the Largest Contentful Paint (LCP).

## 64: What does object-fit do?

`object-fit` controls how an image or video fills its box when the box has a different aspect ratio than the media.

- `fill` (default) - stretches to fill, can distort.
- `contain` - fits the whole image inside, may leave empty bars.
- `cover` - fills the whole box, crops what doesn't fit.
- `none` - natural size, no scaling.
- `scale-down` - the smaller of `none` and `contain`.

```css
.thumbnail {
  width: 100%;
  aspect-ratio: 1;
  object-fit: cover;
}
```

`cover` is the usual choice for thumbnails and hero images in a responsive layout.

## 65: What does object-position do?

When `object-fit` crops an image, `object-position` decides which part stays visible. The default is `50% 50%`, the center.

```css
.hero img {
  width: 100%;
  height: 60svh;
  object-fit: cover;
  object-position: 30% 20%; /* keep the person's face in view */
}
```

It is a simple form of art direction when you don't have separate crops of the image.

## 66: What is the aspect-ratio property?

`aspect-ratio` sets a preferred width-to-height ratio for an element. When only one dimension is set, the other is calculated.

```css
.video-wrapper {
  width: 100%;
  aspect-ratio: 16 / 9;
}

.avatar {
  width: 48px;
  aspect-ratio: 1;
}
```

It replaced the old trick with `padding-top: 56.25%` and an absolutely positioned child. If the content is taller than the ratio allows, the box grows, unless you also set `overflow` or a fixed height.

## 67: How do you make a video responsive?

For a native `<video>`, give it `max-width: 100%` and `height: auto`, plus `width` and `height` attributes so the ratio is known.

```html
<video controls width="1280" height="720" poster="poster.jpg">
  <source src="clip.webm" type="video/webm" />
  <source src="clip.mp4" type="video/mp4" />
</video>
```

```css
video {
  max-width: 100%;
  height: auto;
}
```

## 68: How do you make an iframe embed responsive, like a YouTube video?

Iframes don't have a natural aspect ratio, so set one with CSS.

```html
<iframe
  class="embed"
  src="https://www.youtube.com/embed/VIDEO_ID"
  title="Product demo"
  loading="lazy"
  allowfullscreen
></iframe>
```

```css
.embed {
  width: 100%;
  aspect-ratio: 16 / 9;
  border: 0;
}
```

Older code wraps the iframe in a div with `padding-top: 56.25%` and positions the iframe absolutely inside it. `aspect-ratio` does the same with less code.

## 69: How do you serve modern image formats like AVIF and WebP with a fallback?

Use `<picture>` with `type` on each `<source>`. The browser picks the first format it supports.

```html
<picture>
  <source srcset="photo.avif" type="image/avif" />
  <source srcset="photo.webp" type="image/webp" />
  <img src="photo.jpg" width="1200" height="800" alt="Forest path" />
</picture>
```

AVIF and WebP files are usually much smaller than JPEG at the same quality, which helps on slow mobile connections. You can combine `type` with `srcset` and `sizes` on each source to get both format and size switching.

## 70: How do you make a CSS background image responsive?

Use `background-size` and swap the image at breakpoints.

```css
.hero {
  background-image: url("hero-small.jpg");
  background-size: cover;
  background-position: center;
  min-height: 60svh;
}

@media (width >= 900px) {
  .hero {
    background-image: url("hero-large.jpg");
  }
}
```

`cover` fills the area and crops the rest. `contain` shows the whole image. Background images are for decoration. If the image has meaning, use an `<img>` with `alt` text instead.

## 71: What is image-set() in CSS?

`image-set()` is the CSS version of `srcset`. You give a list of images with resolutions or types, and the browser picks one.

```css
.banner {
  background-image: image-set(
    "banner.avif" type("image/avif"),
    "banner.jpg" type("image/jpeg")
  );
}

.logo {
  background-image: image-set("logo.png" 1x, "logo@2x.png" 2x);
}
```

It works in all modern browsers without a prefix. It only supports `x` style resolutions, not `w` widths with `sizes`.

## 72: Do responsive images still need alt text?

Yes. `alt` is set once on the `<img>`, and it applies to whichever file the browser picks from `srcset` or `<picture>`. Since all the sources should show the same content, one description is enough.

If art direction changes the image a lot (for example, the mobile crop leaves out part of the scene), write `alt` text that is true for every version. Decorative images get an empty `alt=""` so screen readers skip them.

## 73: What is responsive typography?

Responsive typography means text sizes, line heights and line lengths that work on every screen. Headings that look good on a 1440px monitor are usually too big on a phone, and body text that's fine on a phone can feel small on a large screen.

You can change sizes at breakpoints with media queries, or use fluid type with `clamp()` so sizes grow smoothly with the viewport or container.

## 74: What does clamp() do?

`clamp(min, preferred, max)` returns the preferred value but keeps it between a minimum and a maximum.

```css
h1 {
  font-size: clamp(1.75rem, 1rem + 3vw, 3rem);
}

.container {
  width: clamp(320px, 90%, 1200px);
}
```

The heading grows with the viewport, but never gets smaller than 1.75rem or bigger than 3rem. It does the work of two media queries in one line.

## 75: What do min() and max() do?

- `min(a, b)` returns the smaller value.
- `max(a, b)` returns the larger value.

```css
.container {
  width: min(100% - 2rem, 1100px);
  margin-inline: auto;
}

.section {
  padding-block: max(2rem, 5vh);
}
```

`min(100% - 2rem, 1100px)` means "full width with 1rem space on each side, but never more than 1100px". The naming confuses people: `min()` sets a maximum, and `max()` sets a minimum.

## 76: What is calc()?

`calc()` lets you do math with mixed units in CSS.

```css
.main {
  width: calc(100% - 250px);
}

.title {
  font-size: calc(1rem + 1vw);
}
```

You can add, subtract, multiply and divide. Spaces around `+` and `-` are required. Inside `min()`, `max()` and `clamp()` you can write math directly without `calc()`.

## 77: Why should you limit line length and how?

Long lines are hard to read because your eyes lose their place when they jump back to the next line. A common guideline is about 45 to 75 characters per line for body text.

On wide screens, text in a full-width container can easily get to 150 characters per line. Limit it with `max-width` in `ch`:

```css
.article {
  max-width: 65ch;
  margin-inline: auto;
}
```

## 78: What is the ch unit?

`1ch` is the width of the "0" character in the current font. It roughly matches the average character width, so `max-width: 65ch` gives you lines of about 65 characters.

It's not exact, because letters like "i" and "m" have different widths in most fonts, but it's close enough for setting line lengths.

## 79: What is the compounding problem with em?

`em` for `font-size` is relative to the parent's font size. When you nest elements, the sizes multiply.

```css
li {
  font-size: 1.2em;
}
```

```html
<ul>
  <li>
    Level 1 (19.2px)
    <ul>
      <li>
        Level 2 (23.04px)
        <ul>
          <li>Level 3 (27.65px)</li>
        </ul>
      </li>
    </ul>
  </li>
</ul>
```

Using `rem` for font sizes avoids this. `em` is still handy for padding and margins that should scale with the element's own text size, like button padding.

## 80: Why should line-height be unitless?

A unitless `line-height` like `1.5` is inherited as a factor, so each element calculates its own line height from its own font size. If you write `line-height: 24px` or `1.5em`, the computed pixel value is inherited, and a child with bigger text gets lines that overlap.

```css
body {
  line-height: 1.5;
}

h1 {
  line-height: 1.1; /* headings usually need less */
}
```

## 81: How do you hide content on small screens?

Use `display: none` inside a media query. With mobile-first CSS, hide it by default and show it on larger screens.

```css
.desktop-only {
  display: none;
}

@media (width >= 1024px) {
  .desktop-only {
    display: block;
  }
}
```

Don't overuse it. Mobile users often need the same information as desktop users. Hiding content also doesn't stop the browser from downloading images or running scripts inside it.

## 82: What is the difference between display: none and visibility: hidden?

- `display: none` removes the element from the layout. It takes no space and other elements move into its place. Screen readers ignore it.
- `visibility: hidden` hides the element but keeps its space. Screen readers also ignore it.

`opacity: 0` is different again: the element keeps its space, is still read by screen readers and can still be clicked.

## 83: How do you hide something visually but keep it for screen readers?

Use a "visually hidden" class. It makes the element 1px in size and clips it, so it's invisible but still in the accessibility tree.

```css
.visually-hidden {
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

```html
<button>
  <svg aria-hidden="true"><!-- icon --></svg>
  <span class="visually-hidden">Open menu</span>
</button>
```

This is common in responsive navs where the text label is hidden on mobile and only an icon is shown.

## 84: What is a hamburger menu?

A hamburger menu is the three-line icon that opens the main navigation on small screens. On desktop the links are shown in a row, and on mobile they're hidden behind the button to save space.

It saves space but hides navigation, so users may not discover it. For sites with just a few links, showing them directly or using a bottom tab bar can work better. If you use one, make it a real `<button>` with an accessible name and `aria-expanded`.

## 85: How do you build a simple responsive navigation?

Show the links in a row on wide screens, and behind a toggle button on small screens.

```html
<nav class="nav">
  <button class="nav-toggle" aria-expanded="false" aria-controls="nav-menu">
    Menu
  </button>
  <ul id="nav-menu" class="nav-menu">
    <li><a href="/">Home</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/contact">Contact</a></li>
  </ul>
</nav>
```

```css
.nav-menu {
  display: none;
}

.nav-toggle[aria-expanded="true"] + .nav-menu {
  display: block;
}

@media (width >= 768px) {
  .nav-toggle {
    display: none;
  }

  .nav-menu {
    display: flex;
    gap: 1rem;
  }
}
```

```js
const toggle = document.querySelector(".nav-toggle");
toggle.addEventListener("click", () => {
  const open = toggle.getAttribute("aria-expanded") === "true";
  toggle.setAttribute("aria-expanded", String(!open));
});
```

## 86: What is a touch target and how big should it be?

A touch target is the area of a button or link that reacts to a tap. Fingers are less precise than a mouse, so small targets lead to wrong taps.

Common guidelines:

- WCAG 2.2 (level AA) asks for at least **24 x 24 CSS pixels** or enough spacing around smaller targets.
- WCAG level AAA, Apple and Google recommend about **44 x 44** to **48 x 48** pixels.

```css
.icon-button {
  min-width: 44px;
  min-height: 44px;
}
```

You can make the target larger with padding even if the icon itself is small.

## 87: What is the hover media feature?

`hover` tells you if the user's **primary** input device can hover over elements.

- `hover: hover` - the device can hover, like a mouse.
- `hover: none` - it can't, like a touch screen.

```css
@media (hover: hover) {
  .card:hover {
    transform: translateY(-4px);
  }
}
```

This stops hover effects from getting "stuck" after a tap on phones. `any-hover` checks if **any** connected device can hover.

## 88: What is the pointer media feature?

`pointer` tells you how precise the primary pointing device is.

- `fine` - a mouse or trackpad.
- `coarse` - a finger on a touch screen.
- `none` - no pointer, like keyboard-only.

```css
@media (pointer: coarse) {
  .toolbar button {
    min-height: 48px;
    padding-inline: 1rem;
  }
}
```

Use it to make targets bigger for touch. `any-pointer` checks all connected devices.

## 89: What is prefers-color-scheme?

It's a media feature that tells you if the user chose a light or dark theme in their operating system or browser.

```css
:root {
  --bg: white;
  --text: #222;
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg: #121212;
    --text: #eee;
  }
}

body {
  background: var(--bg);
  color: var(--text);
}
```

Also add `color-scheme: light dark` so the browser styles scrollbars and form controls to match.

## 90: What is prefers-reduced-motion?

It tells you if the user asked the operating system to reduce animations. Some people get dizzy or sick from motion on screen.

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

A better approach is to add motion only when the user has no preference: `@media (prefers-reduced-motion: no-preference) { ... }`.

## 91: What is the orientation media feature?

`orientation` matches `portrait` when the viewport is taller than wide (or square), and `landscape` when it's wider than tall.

```css
@media (orientation: landscape) and (height < 500px) {
  .hero {
    min-height: auto;
  }
}
```

Note that it's about the viewport, not the device. A desktop browser window can be portrait. Also, opening the on-screen keyboard on a phone can make the viewport landscape. Width and height queries are usually more reliable.

## 92: How do you write print styles?

Use `@media print` to change the page for printing: hide navigation and buttons, use black text on white, and show link URLs.

```css
@media print {
  nav,
  .ads,
  .share-buttons {
    display: none;
  }

  body {
    color: black;
    background: white;
  }

  a[href^="http"]::after {
    content: " (" attr(href) ")";
  }

  h2,
  h3 {
    break-after: avoid;
  }
}
```

You can check the result with Print Preview or by emulating print media in DevTools.

## 93: What is the resolution media feature?

`resolution` checks the pixel density of the screen. Units are `dppx` (dots per CSS pixel, the same as the DPR), `dpi` and `dpcm`.

```css
@media (resolution >= 2dppx) {
  .logo {
    background-image: url("logo@2x.png");
  }
}
```

You'll see `-webkit-min-device-pixel-ratio: 2` in older code. For images, `srcset` and `image-set()` are usually better than resolution media queries.

## 94: How do you test a responsive site in browser DevTools?

Every major browser has a responsive mode. In Chrome and Edge it's the "Toggle device toolbar" button (Ctrl+Shift+M or Cmd+Shift+M). In Firefox it's Responsive Design Mode.

You can:

- Drag the viewport to any width, or pick a preset device.
- Set the device pixel ratio.
- Emulate touch events.
- Throttle the network and CPU.
- Emulate media features like `prefers-color-scheme`, `prefers-reduced-motion` and print.

Dragging slowly through all widths is a good way to find where the layout breaks.

## 95: Why should you still test on real devices?

DevTools only change the viewport size and a few settings. They don't copy everything a real phone does:

- Mobile browser toolbars that show and hide.
- The on-screen keyboard covering the page.
- Real touch, scroll and zoom behavior.
- Safe areas around notches and rounded corners.
- Real CPU, memory and network speeds.
- Browser-specific bugs, especially in Safari on iOS.

At minimum, test on one iPhone with Safari and one Android phone with Chrome. Cloud services like BrowserStack help when you need more devices.

## 96: How do you find what causes horizontal scrolling?

Horizontal scrolling on mobile is usually caused by one element that is wider than the viewport. To find it:

1. In DevTools, look for elements sticking out past the right edge while in device mode.
2. Add a temporary outline to everything to see the boxes:

```css
* {
  outline: 1px solid red;
}
```

3. Or run this in the console to list elements wider than the page:

```js
document.querySelectorAll("*").forEach((el) => {
  if (el.getBoundingClientRect().right > document.documentElement.clientWidth) {
    console.log(el);
  }
});
```

Common causes are fixed widths, `100vw`, large images without `max-width`, long URLs that don't wrap, and negative margins.

## 97: How do you stop long words and URLs from breaking the layout?

Long strings with no spaces, like URLs or email addresses, don't wrap by default and push the container wider than the screen.

```css
.content {
  overflow-wrap: break-word;
}

/* For text inside flex or grid items, also allow the item to shrink */
.card-body {
  min-width: 0;
}
```

`overflow-wrap: anywhere` is a bit more aggressive and also affects the min-content size, which helps inside flex items. `word-break: break-all` breaks normal words in the middle too, so use it only for things like codes or hashes. `hyphens: auto` adds hyphens for long words when the page has a `lang` attribute.

## 98: How do you make a wide element scroll horizontally instead of breaking the page?

Wrap it in a container with `overflow-x: auto`. Only that container scrolls, not the whole page.

```html
<div class="scroll-x">
  <table>
    ...
  </table>
</div>
```

```css
.scroll-x {
  overflow-x: auto;
}
```

This works for tables, code blocks and wide charts. If the scroll area has no focusable items inside, add `tabindex="0"` and a label so keyboard users can scroll it too.

## 99: How do you make tables responsive?

There are a few common approaches:

1. **Horizontal scroll** - wrap the table in an `overflow-x: auto` container. Simple and keeps the table structure.
2. **Stack rows as cards** - on small screens, turn each row into a block and show the header as a label next to each value.
3. **Hide less important columns** on small screens.
4. **Use a different layout** - sometimes a list or cards are a better fit than a table on mobile.

The scroll option is the safest. Stacking needs care so screen readers still understand the data.

## 100: Why do semantic HTML elements matter in a responsive layout?

Elements like `<header>`, `<nav>`, `<main>`, `<aside>`, `<article>` and `<footer>` describe what each part of the page is. This helps in a few ways:

- Screen reader users can jump between landmarks, which matters more on mobile where everything is stacked in one long column.
- The CSS is easier to read because the selectors match the page structure.
- When you reorder things with Grid at different breakpoints, the HTML still makes sense on its own.

Start with good HTML in a logical reading order, then use CSS to arrange it for each screen size.

## 101: Why does source order matter in a responsive page?

On small screens, most layouts collapse into a single column, and that column follows the HTML order. If the HTML puts the sidebar before the main content, mobile users have to scroll past it to get to what they came for.

Screen readers and keyboard users also follow the HTML order on every screen size. So write the HTML in the order that makes sense to read, usually header, main content, then secondary content, and use Grid or Flexbox to place things differently on wide screens.

## 102: What is the difference between block and inline elements?

- **Block** elements (`<div>`, `<p>`, `<section>`, `<h1>`) start on a new line and take the full width of their parent by default. You can set `width`, `height`, `margin` and `padding` on all sides.
- **Inline** elements (`<span>`, `<a>`, `<strong>`) sit inside a line of text and are only as wide as their content. `width` and `height` don't apply, and vertical margins don't push other lines away.

Block elements stack naturally on narrow screens, which is why a page with no CSS is already "responsive" in a basic way.

## 103: What does display: inline-block do?

An `inline-block` element sits in a line like inline text, but you can give it a width, height, padding and margins like a block.

```css
.badge {
  display: inline-block;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
}
```

Before Flexbox, inline-block was used for horizontal menus and grids. It has an annoying gap between items caused by the whitespace in the HTML. Today Flexbox with `gap` is usually the better choice for rows of items.

## 104: How do you use CSS custom properties with media queries?

Define the variable once and change its value in a media query. Every rule that uses it updates.

```css
:root {
  --space: 1rem;
  --columns: 1;
}

@media (width >= 768px) {
  :root {
    --space: 1.5rem;
    --columns: 2;
  }
}

.grid {
  display: grid;
  grid-template-columns: repeat(var(--columns), 1fr);
  gap: var(--space);
}
```

The opposite doesn't work: you can't use a custom property inside the media query condition itself. `@media (width >= var(--bp))` is invalid.

## 105: How do you create a centered page container?

Give it a maximum width, center it with auto margins, and add padding so content doesn't touch the screen edges on mobile.

```css
.container {
  max-width: 1200px;
  margin-inline: auto;
  padding-inline: 1rem;
}
```

A shorter version with `min()`:

```css
.container {
  width: min(100% - 2rem, 1200px);
  margin-inline: auto;
}
```

## 106: What does margin: auto do inside a flex container?

In a flex container, an `auto` margin takes all the free space on that side. You can use it to push an item to the other end of the row.

```css
.header {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.header .login {
  margin-left: auto; /* pushes the login button to the far right */
}
```

It also works vertically. `margin-top: auto` on the last item of a column pushes it to the bottom, which is handy for keeping buttons at the bottom of cards with different content heights.

## 107: What are logical properties?

Logical properties describe sides by the direction of the text instead of by physical direction.

| Physical       | Logical               |
| -------------- | --------------------- |
| `margin-left`  | `margin-inline-start` |
| `margin-right` | `margin-inline-end`   |
| `padding-top`  | `padding-block-start` |
| `width`        | `inline-size`         |
| `height`       | `block-size`          |
| `left`         | `inset-inline-start`  |

In a right-to-left language like Arabic or Hebrew, `margin-inline-start` becomes the right margin automatically, so you don't need separate RTL styles. Shorthands like `margin-inline: auto` and `padding-block: 2rem` are short and handy even if you only support left-to-right.

## 108: What is position: sticky?

A sticky element acts like a normal element until it reaches a set position while scrolling, then it sticks there until its parent scrolls out of view.

```css
.table-header {
  position: sticky;
  top: 0;
  background: white;
}
```

You must set at least one of `top`, `bottom`, `left` or `right`. It's good for headers, table headings and sidebars. It won't work if any ancestor between the element and the scroll container has `overflow: hidden`, `auto` or `scroll`.

## 109: How do you build a sticky header?

```css
.site-header {
  position: sticky;
  top: 0;
  z-index: 10;
  background: var(--bg);
}

html {
  scroll-padding-top: 4rem; /* so anchor links aren't hidden under the header */
}
```

On mobile, keep a sticky header short. A tall header that stays on screen eats a big part of a small viewport, especially in landscape. Some sites hide it while scrolling down and show it again when scrolling up.

## 110: What problems does position: fixed have on mobile?

- The on-screen keyboard can cover elements fixed to the bottom, or push them around in different ways in different browsers.
- Elements fixed to the bottom may sit under the iPhone home indicator unless you add the safe area inset.
- A parent with `transform`, `filter` or `perspective` makes `fixed` act relative to that parent instead of the viewport.
- Fixed headers and footers take up space permanently, which hurts on small screens.

Test fixed elements on a real phone, with the keyboard open and in landscape.

## 111: Should media queries use px, em or rem?

All three work in modern browsers. In media queries, `em` and `rem` are both based on the browser's default font size (usually 16px), not on the `html` font size you set in CSS.

The benefit of `em` breakpoints is that they move when the user changes their default font size. If someone uses a 20px default, a `48em` breakpoint triggers at 960px instead of 768px, so the layout switches earlier and the bigger text still fits. Many teams use `px` for simplicity, and that's fine too. Browsers have fixed the old zoom bugs that used to make `px` breakpoints unreliable in Safari.

## 112: Why does the input type attribute matter on mobile?

The `type` attribute tells mobile browsers which keyboard to show and gives you built-in validation.

```html
<input type="email" name="email" />
<!-- keyboard with @ and . -->
<input type="tel" name="phone" />
<!-- number pad -->
<input type="url" name="website" />
<!-- keyboard with / and .com -->
<input type="number" name="age" />
<!-- numeric keyboard -->
<input type="search" name="q" />
<!-- "Search" key on the keyboard -->
<input type="date" name="birthday" />
<!-- native date picker -->
```

Using the right type makes forms much faster to fill out on a phone.

## 113: What does the inputmode attribute do?

`inputmode` picks the on-screen keyboard without changing the input's type or validation.

```html
<!-- One-time code: digits only, but keep it a text field -->
<input
  type="text"
  inputmode="numeric"
  autocomplete="one-time-code"
  pattern="[0-9]*"
/>

<!-- Price with decimals -->
<input type="text" inputmode="decimal" />
```

Values are `none`, `text`, `decimal`, `numeric`, `tel`, `search`, `email` and `url`. It's useful for things like credit card numbers or ZIP codes, which are digits but not really numbers, so `type="number"` (with its spinner and rounding) is the wrong fit.

## 114: How does the autocomplete attribute help on mobile?

`autocomplete` tells the browser what kind of data a field expects, so it can fill it from saved addresses, cards and passwords. Typing on a phone is slow, so this saves a lot of effort.

```html
<input name="name" autocomplete="name" />
<input name="email" type="email" autocomplete="email" />
<input name="address" autocomplete="street-address" />
<input name="cc" autocomplete="cc-number" inputmode="numeric" />
<input name="code" autocomplete="one-time-code" inputmode="numeric" />
```

`one-time-code` lets iOS and Android suggest SMS codes right above the keyboard.

## 115: Why does iOS zoom in when you tap an input, and how do you stop it?

Safari on iOS zooms in when the input's font size is smaller than 16px, so the user can read what they type. The page then stays zoomed in after leaving the field, which is annoying.

The fix is to make form fields at least 16px:

```css
input,
select,
textarea {
  font-size: max(16px, 1rem);
}
```

Don't fix it by disabling zoom in the viewport meta tag. That hurts accessibility.

## 116: How do you make a form layout responsive?

Stack labels and fields in one column on mobile, and use a grid for a few columns on wider screens.

```css
.form {
  display: grid;
  gap: 1rem;
}

@media (width >= 700px) {
  .form {
    grid-template-columns: 1fr 1fr;
  }

  .form .full {
    grid-column: 1 / -1;
  }
}

.form input,
.form select,
.form textarea {
  width: 100%;
}
```

Put labels above the fields rather than next to them on small screens. Side-by-side labels squeeze the fields too much.

## 117: What font size should body text be on mobile and desktop?

16px (`1rem`) is the usual minimum for body text on phones. Smaller text is hard to read and makes people zoom. On large screens, many sites use 17px to 20px because users sit further away from the screen.

```css
body {
  font-size: clamp(1rem, 0.95rem + 0.25vw, 1.125rem);
}
```

Use `rem` so the text still respects the user's own font size setting.

## 118: How do CSS frameworks help with responsive design?

Frameworks like Bootstrap and Tailwind CSS come with a set of breakpoints, a grid or layout utilities, and responsive helper classes. You get a consistent system without writing every media query yourself.

```html
<!-- Bootstrap: 1 column on mobile, 2 from md, 3 from lg -->
<div class="row">
  <div class="col-12 col-md-6 col-lg-4">...</div>
</div>
```

The downside is you still need to understand the CSS underneath, because sooner or later you'll hit a layout the framework doesn't cover.

## 119: How do responsive prefixes work in Tailwind CSS?

Tailwind is mobile-first. Classes without a prefix apply to all sizes. Classes with a prefix like `md:` apply from that breakpoint up.

```html
<div class="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">...</div>

<p class="text-base md:text-lg">...</p>

<!-- max-* targets below a breakpoint -->
<nav class="max-md:hidden">...</nav>
```

The default breakpoints are `sm` (40rem), `md` (48rem), `lg` (64rem), `xl` (80rem) and `2xl` (96rem). Tailwind v4 also has container query variants like `@md:` used together with an `@container` class on the parent.

## 120: What is a 12-column grid?

It's a layout system where the page width is divided into 12 equal columns. Elements span a number of columns: 12 for full width, 6 for half, 4 for a third, 3 for a quarter.

12 is popular because it divides evenly by 1, 2, 3, 4, 6 and 12, so you can build many layouts. On small screens, items usually span all 12 columns.

```css
.grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 1rem;
}

.half {
  grid-column: span 12;
}

@media (width >= 768px) {
  .half {
    grid-column: span 6;
  }
}
```

## 121: What is a gutter?

A gutter is the space between columns (and sometimes rows) in a grid. In CSS it's set with `gap`, `column-gap` and `row-gap`.

Gutters are often smaller on mobile and larger on desktop:

```css
.grid {
  gap: clamp(1rem, 3vw, 2rem);
}
```

The space on the outer edges of the page is usually called the margin or the page padding, not the gutter.

## 122: What breakpoint values are common?

There's no standard, but many projects use something close to these:

- 480px or so - large phones
- 640px - small tablets, phones in landscape
- 768px - tablets
- 1024px - small laptops, tablets in landscape
- 1280px - desktops
- 1536px - large desktops

Bootstrap uses 576, 768, 992, 1200 and 1400px. Tailwind uses 640, 768, 1024, 1280 and 1536px. These are fine as a starting point, but add or change breakpoints where your content needs them.

## 123: What is the difference between screen.width and window.innerWidth?

- `screen.width` is the width of the whole screen in CSS pixels. It doesn't change when you resize the browser window.
- `window.innerWidth` is the viewport width, including the vertical scrollbar.
- `document.documentElement.clientWidth` is the viewport width without the scrollbar. This is closest to what CSS layout uses.

Media queries use the viewport width (including the scrollbar), so `window.innerWidth` matches `@media (width >= ...)`. For layout decisions in JS, use `matchMedia()` instead of reading widths yourself.

## 124: What is matchMedia() in JavaScript?

`window.matchMedia()` checks a media query from JavaScript and lets you listen for changes.

```js
const wide = window.matchMedia("(width >= 1024px)");

function update() {
  if (wide.matches) {
    console.log("Desktop layout");
  } else {
    console.log("Mobile layout");
  }
}

update();
wide.addEventListener("change", update);
```

It only fires when the query result changes, not on every pixel of a resize. That makes it much cheaper than a `resize` listener. Older code uses `addListener`, which is deprecated.

## 125: Why should you avoid heavy work in the resize event?

The `resize` event can fire many times per second while the user drags the window or rotates the phone. Doing layout reads, DOM changes or expensive calculations on every event makes the page lag.

Better options:

- Use CSS (media and container queries) for layout changes.
- Use `matchMedia()` to react only when a breakpoint is crossed.
- Use `ResizeObserver` to watch a specific element.
- If you must use `resize`, debounce it or wrap the work in `requestAnimationFrame`.

## 126: What are container queries?

Container queries apply styles based on the size of a parent element instead of the size of the viewport. You mark an element as a container and then query its width.

```css
.card-wrapper {
  container-type: inline-size;
}

.card {
  display: grid;
  gap: 1rem;
}

@container (width >= 400px) {
  .card {
    grid-template-columns: 150px 1fr;
  }
}
```

The same card component can now show a stacked layout in a narrow sidebar and a side-by-side layout in a wide main column, on the same page. They work in all modern browsers.

## 127: What is the CSS multi-column layout?

The multi-column layout flows content into columns like a newspaper.

```css
.article {
  columns: 20rem; /* as many columns as fit, each at least 20rem wide */
  column-gap: 2rem;
}
```

With a width instead of a count, it's responsive on its own: one column on a phone, two or three on wider screens. It works well for lists of links, short text, or a footer sitemap. For long articles it's awkward on screen, because readers have to scroll down and back up for each column.

## 128: What is CSS scroll snap?

Scroll snap makes a scroll container stop at set positions, like slides in a carousel.

```css
.carousel {
  display: flex;
  gap: 1rem;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
}

.carousel > * {
  flex: 0 0 80%;
  scroll-snap-align: start;
}
```

It gives you a swipeable carousel on touch screens with no JavaScript. `mandatory` always snaps to a point, and `proximity` only snaps when the user stops close to one.

## 129: What do place-items and place-content do?

They are shorthands for alignment:

- `place-items: <align-items> <justify-items>`
- `place-content: <align-content> <justify-content>`
- `place-self: <align-self> <justify-self>`

```css
.center {
  display: grid;
  place-items: center;
}
```

If you give one value, it's used for both. `place-items: center` on a grid is the shortest way to center a child in both directions.

## 130: What are min-content, max-content and fit-content?

They are sizes based on the content:

- `min-content` - the smallest width without overflow. For text, that's the width of the longest word.
- `max-content` - the width the content would take with no wrapping at all.
- `fit-content` - like `max-content`, but never wider than the available space. Then it wraps.

```css
.tag {
  width: fit-content; /* only as wide as the text, but can wrap */
}

.layout {
  display: grid;
  grid-template-columns: max-content 1fr; /* label column fits its longest label */
}
```

## 131: What is the difference between width: 100% and width: 100vw?

- `width: 100%` is the width of the parent's content box. It excludes the scrollbar and respects the parent's padding.
- `width: 100vw` is the full viewport width, including the vertical scrollbar on desktop.

On a desktop with visible scrollbars, `100vw` is about 15px wider than the visible area, so `width: 100vw` causes horizontal scrolling. Use `100%` for normal full-width elements. Use `100vw` only when you know what you're doing, for example for full-bleed sections with care.

## 132: Why use min-height instead of height in responsive layouts?

A fixed `height` stops the box from growing. When the screen is narrower, text wraps to more lines, and with a fixed height it overflows the box and overlaps whatever is below.

```css
/* Breaks when the text wraps */
.hero {
  height: 400px;
}

/* Grows when it needs to */
.hero {
  min-height: 400px;
}
```

As a rule, let content decide the height and only set a minimum.

## 133: What problems can overflow: hidden cause in responsive layouts?

`overflow: hidden` hides anything that doesn't fit. That can hide real content when text wraps more on small screens or when the user enlarges the font. It also:

- Breaks `position: sticky` on children.
- Clips focus outlines and dropdown menus.
- Hides the real cause of horizontal scrolling instead of fixing it.

`overflow: clip` is a lighter alternative that clips without creating a scroll container, so sticky still works. But first look for the element that's too wide and fix that.

## 134: What were floats used for and do you still need them for layout?

Before Flexbox and Grid, `float: left` was used to build columns and grids, with clearfix hacks to stop parent containers from collapsing. Old frameworks like Bootstrap 3 used floats for their grid.

Today you don't need floats for page layout. Their original use is still valid: letting text wrap around an image.

```css
.article img.left {
  float: left;
  margin: 0 1rem 1rem 0;
  max-width: 40%;
}
```

You may still need to understand floats when working on older code.

## 135: How do SVG images scale responsively?

SVGs are vector images, so they look sharp at any size. The `viewBox` attribute defines the internal coordinate system, and the SVG scales to fit whatever width you give it.

```html
<svg viewBox="0 0 100 50" role="img" aria-label="Chart">
  <rect x="0" y="0" width="100" height="50" fill="#eee" />
</svg>
```

```css
svg {
  width: 100%;
  height: auto;
}
```

Without a `viewBox`, the SVG won't scale its content. `preserveAspectRatio` controls how it fits when the box has a different ratio.

## 136: How do you make icons scale with the text next to them?

Size the icon in `em` so it follows the font size of its parent.

```css
.icon {
  width: 1em;
  height: 1em;
  fill: currentColor;
  vertical-align: -0.125em;
}
```

```html
<button class="big">
  <svg class="icon" aria-hidden="true"><use href="#icon-search" /></svg>
  Search
</button>
```

When the button text gets bigger at a breakpoint, the icon grows with it. `fill: currentColor` makes the icon use the text color.

## 137: What does the theme-color meta tag do?

It sets the color of the browser UI around the page, like the address bar on Android Chrome and the status bar in installed web apps. You can set different colors for light and dark mode with `media`.

```html
<meta
  name="theme-color"
  content="#ffffff"
  media="(prefers-color-scheme: light)"
/>
<meta
  name="theme-color"
  content="#111111"
  media="(prefers-color-scheme: dark)"
/>
```

Support varies between browsers, so treat it as a small extra, not something your design depends on.

## 138: What does the color-scheme property do?

`color-scheme` tells the browser which color schemes the page supports, so it can style built-in parts like form controls, scrollbars and the default background to match.

```css
:root {
  color-scheme: light dark;
}
```

You can also set it in HTML so it works before the CSS loads:

```html
<meta name="color-scheme" content="light dark" />
```

With it, a dark mode user gets dark scrollbars and inputs. Without it, you get a dark page with bright white form fields.

## 139: How can details and summary help on small screens?

`<details>` and `<summary>` create a native expand and collapse widget with no JavaScript. They're keyboard and screen reader friendly by default.

```html
<details>
  <summary>Shipping information</summary>
  <p>We ship to all EU countries within 3-5 working days.</p>
</details>
```

On mobile they're useful for FAQs, filters and long sections of secondary content. You show a short list of headings, and users open only what they need instead of scrolling through everything.

## 140: Why use the dialog element for modals in a responsive UI?

`<dialog>` opened with `showModal()` gives you a lot for free: it shows on top of the page, makes the content behind it inert, moves focus into the dialog, closes with the Escape key, and has a `::backdrop` you can style.

```html
<dialog id="filters">
  <form method="dialog">
    <h2>Filters</h2>
    <button>Close</button>
  </form>
</dialog>
```

```css
dialog {
  width: min(100% - 2rem, 600px);
  max-height: 90svh;
}

@media (width < 600px) {
  dialog {
    width: 100%;
    max-width: 100%;
    margin-block-end: 0; /* sits at the bottom like a sheet */
  }
}
```

## 141: What does text-wrap: balance do?

`text-wrap: balance` makes the browser spread the words of a short text block evenly across its lines, so you don't end up with one word alone on the last line.

```css
h1,
h2,
h3 {
  text-wrap: balance;
}

p {
  text-wrap: pretty; /* avoids a single short word on the last line of paragraphs */
}
```

This helps a lot with headings on narrow screens. Browsers limit `balance` to a few lines for performance, so use it for headings, not long paragraphs.

## 142: How do you make spacing responsive?

Use smaller spacing on mobile and larger on desktop. You can do it with breakpoints or fluid values.

```css
:root {
  --space-s: clamp(0.75rem, 0.6rem + 0.5vw, 1rem);
  --space-m: clamp(1rem, 0.8rem + 1vw, 1.5rem);
  --space-l: clamp(2rem, 1.5rem + 2.5vw, 4rem);
}

.section {
  padding-block: var(--space-l);
}
```

Big desktop padding wastes a lot of space on a phone, so this is one of the easiest wins in a responsive design.

## 143: How do you check if a CSS feature is safe to use?

- **Baseline** - a label shown on MDN, web.dev and caniuse. "Widely available" means the feature has worked in all major browsers for at least 30 months. "Newly available" means it just started working in all of them.
- **caniuse.com** - shows support per browser version and known bugs.
- **MDN** - the browser compatibility table at the bottom of each page.

If something isn't supported everywhere, use it as an improvement with a fallback, or wrap it in `@supports`.

## 144: What is progressive enhancement?

Progressive enhancement means building a basic version that works everywhere first, then adding better features for browsers and devices that support them.

```css
.gallery {
  display: flex;
  flex-wrap: wrap; /* works everywhere */
}

@supports (display: grid) {
  .gallery {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  }
}
```

Mobile-first CSS is a form of progressive enhancement: simple layout first, then more complex layouts as space allows.

## 145: What is graceful degradation?

Graceful degradation is the opposite approach. You build the full experience for modern browsers first, then make sure it still works in a reduced form on older or less capable ones.

The end result can be similar, but progressive enhancement is usually easier to keep working, because the base version is always there and you build up from it.

## 146: What is @supports?

`@supports` is a feature query. It applies CSS only if the browser supports a property and value.

```css
.card {
  height: 100vh;
}

@supports (height: 100dvh) {
  .card {
    height: 100dvh;
  }
}

/* Check for a selector */
@supports selector(:has(a)) {
  .menu:has(.open) {
    background: #f5f5f5;
  }
}

@supports not (aspect-ratio: 1) {
  /* fallback */
}
```

Often you don't need it. Browsers ignore declarations they don't understand, so writing the fallback first and the new value second already works.

## 147: How do you keep a footer at the bottom of the page when content is short?

Make the body a grid or flex column that is at least as tall as the viewport, and let the main content take the free space.

```css
body {
  min-height: 100svh;
  display: grid;
  grid-template-rows: auto 1fr auto;
}
```

```html
<body>
  <header>...</header>
  <main>...</main>
  <footer>...</footer>
</body>
```

When the content is short, `main` stretches and pushes the footer down. When it's long, the page just scrolls normally.

## 148: Why is overflow-x: hidden on the body a bad fix for horizontal scrolling?

It hides the symptom, not the cause. Some element is still wider than the screen, and now part of it is cut off where users can't see or reach it. It also has side effects:

- It can break `position: sticky` on the page.
- Mobile browsers sometimes still let users scroll or zoom sideways.
- It hides future overflow bugs too.

Find the element that's too wide and fix it. If you really need to clip decorative content that sticks out, use `overflow-x: clip` on the closest section instead of the body.

## 149: When should you use height media queries?

Use them when the layout depends on vertical space. Common cases are phones in landscape, small laptop screens and browser windows that are wide but short.

```css
@media (height < 500px) {
  .site-header {
    position: static; /* don't take up space while scrolling */
  }

  .hero {
    min-height: auto;
  }
}
```

Without them, a sticky header and a full-height hero can fill the whole screen of a landscape phone and leave no room for content.

## 150: What is the difference between display: flex and display: inline-flex?

Both make the element a flex container for its children. The difference is how the container itself behaves:

- `display: flex` - the container is a block. It starts on a new line and takes the full width.
- `display: inline-flex` - the container is inline. It only takes the width of its content and can sit next to text.

```css
.button {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}
```

`inline-flex` is common for buttons with an icon and a label.

---

# Moderate Questions (151-300)

## 151: What values can container-type have?

- `inline-size` - you can query the container's inline size (its width in horizontal writing). This is the one you'll use most.
- `size` - you can query both width and height. The element gets size containment in both directions, so its height no longer comes from its content. You must give it a height some other way.
- `normal` (default) - not a size container, but it can still be used for style queries.

```css
.sidebar {
  container-type: inline-size;
}
```

With `inline-size`, the container's width can't depend on its children, but its height still grows with the content as usual.

## 152: What are container-name and the container shorthand?

`container-name` gives a container a name, so a query can target a specific ancestor instead of the nearest one.

```css
.page-main {
  container: main / inline-size; /* name / type */
}

.card {
  container: card / inline-size;
}

@container main (width >= 800px) {
  .card {
    /* reacts to the main column, not the card itself */
  }
}
```

Without a name, `@container` uses the nearest ancestor that is a size container. Names are useful when containers are nested and you need a specific one.

## 153: What are container query units?

They work like viewport units but are relative to the nearest size container:

- `cqw` / `cqh` - 1% of the container's width / height.
- `cqi` / `cqb` - 1% of the container's inline / block size.
- `cqmin` / `cqmax` - the smaller / larger of `cqi` and `cqb`.

```css
.card-wrapper {
  container-type: inline-size;
}

.card h2 {
  font-size: clamp(1.1rem, 4cqi, 1.75rem);
}
```

If there's no container ancestor, they fall back to the small viewport units (`svw`, `svh`). Prefer `cqi` over `cqw` so it still works with vertical writing modes.

## 154: When should you use a container query and when a media query?

- **Media queries** - for page-level decisions that depend on the whole viewport or the user: the main page layout, the navigation style, and user preferences like dark mode or reduced motion.
- **Container queries** - for components that can appear in different places: cards, widgets, product tiles, form groups. The component adapts to the space it was given, wherever it is.

A typical page uses both: media queries change the page grid, and container queries let each component respond to the column it ended up in.

## 155: Why can't an element query its own size with a container query?

A container query looks at the size of an ancestor, never at the element itself. If an element could change its own styles based on its own size, those styles could change its size, which would change which styles apply, and so on in a loop.

That's also why `container-type` adds containment: the container's size (in the queried direction) must not depend on its content. So the usual structure is a wrapper that is the container and an inner element that gets styled.

```html
<div class="card-container">
  <article class="card">...</article>
</div>
```

## 156: What are container style queries?

Style queries check the value of a custom property on a container instead of its size.

```css
.card-list {
  --variant: compact;
}

@container style(--variant: compact) {
  .card {
    padding: 0.5rem;
    font-size: 0.9rem;
  }
}
```

Any element can be a style query container. You don't need `container-type`. Style queries for custom properties work in Chromium browsers and Safari. Check Firefox support before relying on them, and treat them as an improvement with a fallback. Querying normal properties like `style(display: flex)` isn't supported yet.

## 157: How can :has() help with responsive layouts?

`:has()` lets a parent change its styles based on what's inside it. That means layouts can react to content, not only to screen size.

```css
/* Card with an image gets a two-column layout */
.card:has(img) {
  display: grid;
  grid-template-columns: 120px 1fr;
}

/* Lock page scroll when the mobile menu is open */
body:has(.nav[data-open="true"]) {
  overflow: hidden;
}

/* Form row turns red if it has an invalid field */
.field:has(:user-invalid) {
  border-color: red;
}
```

It works in all modern browsers.

## 158: How do you change a layout based on the number of children?

Combine `:has()` with `:nth-child()` or `:nth-last-child()` to count items.

```css
/* Default: one column */
.gallery {
  display: grid;
  gap: 1rem;
}

/* 2 or more items */
.gallery:has(> :nth-child(2)) {
  grid-template-columns: 1fr 1fr;
}

/* 5 or more items */
.gallery:has(> :nth-child(5)) {
  grid-template-columns: repeat(3, 1fr);
}
```

This is called a quantity query. It's useful when a component gets a variable number of items from a CMS or an API.

## 159: What is subgrid?

`subgrid` lets a nested grid use the rows or columns of its parent grid instead of creating its own. Items inside different children can then line up with each other.

```css
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
}

.card {
  display: grid;
  grid-row: span 3;
  grid-template-rows: subgrid; /* title, body, footer rows shared across cards */
}
```

Now the titles, bodies and footers of all cards in the same row line up, even if one card has a longer title. It works in all modern browsers.

## 160: What is intrinsic web design?

Intrinsic web design is a term from Jen Simmons for layouts that use the content's own size together with modern CSS tools, instead of only fixed breakpoints. It mixes fixed and flexible sizes, uses `minmax()`, `fit-content`, `auto-fit`, Flexbox wrapping and `clamp()`, and lets the browser decide many of the details.

```css
.layout {
  display: grid;
  grid-template-columns: minmax(200px, 300px) minmax(0, 1fr);
}

.tags {
  display: flex;
  flex-wrap: wrap;
}
```

The result often needs far fewer media queries, because many parts of the layout adapt by themselves.

## 161: What is the flexbox "switcher" pattern?

It switches a row of items into a column when the container gets narrower than a chosen width, with no media query.

```css
.switcher {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.switcher > * {
  flex-grow: 1;
  flex-basis: calc((40rem - 100%) * 999);
}
```

When the container is wider than 40rem, `40rem - 100%` is negative, so the basis is negative (treated as 0) and the items sit in one row. When it's narrower, the result is a huge positive number, so each item takes a full line. All items switch at the same time, unlike a plain wrapping row.

## 162: How do you build a sidebar layout that wraps without media queries?

Give the sidebar a fixed basis and make the main content grow a lot more, with a minimum width.

```css
.with-sidebar {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.sidebar {
  flex-basis: 250px;
  flex-grow: 1;
}

.main {
  flex-basis: 0;
  flex-grow: 999;
  min-inline-size: 60%;
}
```

When the main content would get narrower than 60% of the container, it wraps under the sidebar, and both become full width. This is the "sidebar" layout from the Every Layout book.

## 163: What is the holy grail layout and how do you build it today?

It's the classic layout with a header, a footer, and three columns in between: left nav, main content and right sidebar. The footer stays at the bottom even when content is short. It used to be very hard with floats.

```css
body {
  min-height: 100svh;
  display: grid;
  grid-template:
    "header" auto
    "main" 1fr
    "nav" auto
    "aside" auto
    "footer" auto / 1fr;
}

@media (width >= 900px) {
  body {
    grid-template:
      "header header header" auto
      "nav main aside" 1fr
      "footer footer footer" auto / 200px 1fr 200px;
  }
}

header {
  grid-area: header;
}
nav {
  grid-area: nav;
}
main {
  grid-area: main;
}
aside {
  grid-area: aside;
}
footer {
  grid-area: footer;
}
```

## 164: How do you build a full-bleed layout with CSS Grid?

Create a grid with a centered content column and flexible columns on both sides. Normal children go in the middle. Full-width children span all columns.

```css
.article {
  display: grid;
  grid-template-columns:
    [full-start] minmax(1rem, 1fr)
    [content-start] min(65ch, 100% - 2rem)
    [content-end] minmax(1rem, 1fr)
    [full-end];
}

.article > * {
  grid-column: content;
}

.article > .full-bleed {
  grid-column: full;
}
```

This avoids the `width: 100vw; margin-left: calc(50% - 50vw)` trick, which causes horizontal scrolling when there's a vertical scrollbar.

## 165: What are the stack and cluster layout patterns?

They are two small layout helpers that cover a lot of everyday cases.

**Stack** - vertical spacing between items, no spacing on the outer edges:

```css
.stack {
  display: flex;
  flex-direction: column;
  gap: var(--space, 1rem);
}
```

**Cluster** - a group of items in a row that wrap when they run out of room, like tags or buttons:

```css
.cluster {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem 1rem;
  align-items: center;
}
```

Both adapt to any width without media queries, so you can drop them into any part of the page.

## 166: Why do you sometimes need min-width: 0 on a flex item?

Flex items have `min-width: auto` by default, which means they can't shrink below the width of their content. A long word, a URL, a `<pre>` block or a wide table inside a flex item forces the item to stay wide, and it overflows its container.

```css
.layout {
  display: flex;
}

.main {
  flex: 1;
  min-width: 0; /* allow it to shrink below its content width */
}
```

In a column flex container, the same thing happens with `min-height`. This is one of the most common causes of horizontal overflow in responsive layouts.

## 167: What is grid blowout and how does minmax(0, 1fr) fix it?

`1fr` is really `minmax(auto, 1fr)`. The `auto` minimum means a column can't get smaller than its content's minimum width. If one cell has a long URL or a wide code block, that column grows and the grid becomes wider than its container. This is called grid blowout.

```css
/* Can blow out */
.grid {
  grid-template-columns: 1fr 1fr;
}

/* Columns can shrink to 0 and stay equal */
.grid {
  grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
}
```

Another fix is `min-width: 0` or `overflow: hidden` on the grid item that has the wide content.

## 168: What does grid-auto-flow: dense do?

By default, grid auto-placement goes in order and never moves back. When an item spans two columns and doesn't fit at the end of a row, it goes to the next row and leaves a hole.

`dense` tells the browser to go back and fill holes with later items that fit.

```css
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  grid-auto-flow: dense;
}

.gallery .wide {
  grid-column: span 2;
}
```

The grid looks tidier, but the visual order no longer matches the DOM order, which can confuse keyboard users. Use it for galleries where order doesn't matter much.

## 169: What is the implicit grid and grid-auto-rows?

The explicit grid is what you define with `grid-template-columns` and `grid-template-rows`. When there are more items than cells, the browser creates extra rows (or columns) automatically. That's the implicit grid.

`grid-auto-rows` and `grid-auto-columns` set the size of those implicit tracks.

```css
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  grid-auto-rows: minmax(150px, auto); /* every new row at least 150px */
}
```

In responsive grids, you rarely set rows explicitly, because the number of rows changes with the screen width. `grid-auto-rows` controls them all.

## 170: How do you stop the last row of a wrapping flex layout from stretching?

With `flex: 1` and `flex-wrap: wrap`, items on the last row grow to fill it, so if there's only one item left it becomes full width and looks different from the others.

Use Grid instead, which keeps items in columns:

```css
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 1rem;
}
```

If you must use Flexbox, give items a fixed basis and no growth, or set a `max-width` that matches the other items. But this is the main case where Grid is the better tool.

## 171: How does the browser pick an image from srcset with w descriptors?

1. It takes the `sizes` attribute and finds the first media condition that matches, which gives the display width (for example `50vw` on a 1000px viewport, so 500px).
2. It multiplies that by the device pixel ratio (500px x 2 = 1000 pixels needed).
3. It looks for the file in `srcset` that best fits that number, usually the smallest one that's large enough.

```html
<img
  srcset="a-500.jpg 500w, a-1000.jpg 1000w, a-1500.jpg 1500w"
  sizes="(width >= 800px) 50vw, 100vw"
  src="a-1000.jpg"
  alt="..."
/>
```

The spec lets browsers make their own choice in the end. They may pick a smaller file on a slow network or reuse a larger file that's already in the cache.

## 172: How do you write an accurate sizes attribute?

Match it to the real width of the image in your layout at each breakpoint. You can use `calc()` and different units.

```html
<img
  srcset="p-400.jpg 400w, p-800.jpg 800w, p-1200.jpg 1200w"
  sizes="
    (width >= 1200px) 370px,
    (width >= 768px) calc((100vw - 4rem) / 2),
    calc(100vw - 2rem)
  "
  src="p-800.jpg"
  alt="..."
/>
```

Here the image is a fixed 370px in a 3-column layout on desktop, half the width minus padding on tablets, and full width minus page padding on phones. To check it, compare the rendered width in DevTools with the value from `sizes`. It doesn't need to be pixel perfect, just close.

## 173: What is sizes="auto"?

With `sizes="auto"`, the browser uses the image's real layout width instead of a value you write by hand. It only works on lazy-loaded images, because those are loaded after layout, when the width is known.

```html
<img
  loading="lazy"
  sizes="auto"
  srcset="t-300.jpg 300w, t-600.jpg 600w, t-900.jpg 900w"
  width="300"
  height="200"
  src="t-600.jpg"
  alt="..."
/>
```

It saves you from keeping `sizes` in sync with your CSS. Support is in Chromium browsers so far. You can write `sizes="auto, (width >= 800px) 50vw, 100vw"` so other browsers fall back to the manual value.

## 174: What does fetchpriority do?

`fetchpriority` hints how important a resource is compared with others of the same type. Values are `high`, `low` and `auto`.

```html
<!-- The hero image is the LCP element, load it early -->
<img src="hero.jpg" fetchpriority="high" alt="..." width="1600" height="900" />

<!-- Carousel slides that aren't visible yet -->
<img src="slide-2.jpg" fetchpriority="low" alt="..." />
```

On mobile, bandwidth is limited, so telling the browser which image matters most can improve LCP a lot. Use `high` sparingly, usually on one image per page.

## 175: How do you preload a responsive image?

Use `<link rel="preload">` with `imagesrcset` and `imagesizes`, which match the `srcset` and `sizes` of the image.

```html
<link
  rel="preload"
  as="image"
  imagesrcset="hero-640.jpg 640w, hero-1280.jpg 1280w, hero-1920.jpg 1920w"
  imagesizes="100vw"
  fetchpriority="high"
/>
```

If you preload with just `href`, every device downloads that one file even if the `<img>` would pick a different one, so the image gets downloaded twice. Preloading helps when the image isn't in the HTML directly, like a CSS background or an image added by JavaScript.

## 176: Why shouldn't you lazy load the hero image?

`loading="lazy"` makes the browser wait until layout is done to decide if the image is near the viewport. For an image that is visible right away, that delay pushes back the Largest Contentful Paint.

Rules of thumb:

- Images visible on first load: no `loading="lazy"`, and add `fetchpriority="high"` to the main one.
- Images below the fold: `loading="lazy"`.

Remember that what is above the fold differs by screen size. An image that's below the fold on desktop might be the first thing a phone user sees.

## 177: How do you combine media and type in a picture element?

The browser checks each `<source>` from top to bottom and uses the first one where both `media` and `type` match. So put the most specific sources first.

```html
<picture>
  <!-- Wide screens: landscape crop -->
  <source media="(width >= 800px)" type="image/avif" srcset="wide.avif" />
  <source media="(width >= 800px)" srcset="wide.jpg" />

  <!-- Narrow screens: square crop -->
  <source type="image/avif" srcset="square.avif" />
  <img src="square.jpg" alt="Runner crossing the finish line" />
</picture>
```

Each crop needs an AVIF source and a fallback, because a source without `type` matches every browser.

## 178: What does decoding="async" do?

It hints that the browser can decode the image off the main thread, without holding up other content from showing.

```html
<img src="gallery.jpg" decoding="async" loading="lazy" alt="..." />
```

Values are `sync`, `async` and `auto`. Modern browsers already decode most images off the main thread, so the effect is usually small. It's a hint, not a guarantee.

## 179: What is an image CDN and why use one for responsive images?

An image CDN resizes, crops, compresses and converts images on request, based on parameters in the URL. Examples are Cloudinary, imgix, Cloudflare Images and the built-in image services of Vercel and Netlify.

```html
<img
  srcset="
    https://cdn.example.com/photo.jpg?w=400&format=auto   400w,
    https://cdn.example.com/photo.jpg?w=800&format=auto   800w,
    https://cdn.example.com/photo.jpg?w=1600&format=auto 1600w
  "
  sizes="(width >= 900px) 50vw, 100vw"
  src="https://cdn.example.com/photo.jpg?w=800"
  alt="..."
/>
```

You upload one large original and get every size and format you need. `format=auto` serves AVIF or WebP to browsers that accept them.

## 180: How many image widths should you put in srcset?

Enough so the browser never has to download much more than it needs, but not so many that caching gets worse. Four to six widths cover most layouts, for example 400, 800, 1200, 1600 and 2000 pixels for a full-width image.

A more careful method is to pick widths so the file size goes up by a similar step each time (for example every 20-30 KB), since that's what affects load time. Also think about the largest real size: a 2x screen showing a 600px wide image needs at most 1200 pixels. A 3000-pixel file is a waste there.

## 181: When should you use SVG instead of a raster image?

Use SVG for logos, icons, illustrations, diagrams and charts. They're made of shapes, look sharp at any size and DPR, are usually small, and can be styled with CSS (colors, dark mode, hover).

Use raster formats (AVIF, WebP, JPEG, PNG) for photos and images with lots of detail and color changes. A photo as an SVG would be huge.

Always optimize SVGs (with a tool like SVGO), because files exported from design tools often have a lot of unused data.

## 182: How do framework image components help with responsive images?

Components like Next.js `<Image>`, Nuxt `<NuxtImg>` and Angular's `NgOptimizedImage` generate `srcset`, `sizes`, `width`/`height` and lazy loading for you, and often hook into an image optimization service.

```jsx
import Image from "next/image";

export function Hero() {
  return (
    <Image
      src="/hero.jpg"
      alt="Mountains at sunrise"
      width={1600}
      height={900}
      sizes="100vw"
      priority
    />
  );
}
```

You still need to give an accurate `sizes` value and mark the main image as a priority (in Next.js 16 and later, `preload` replaces the deprecated `priority` prop). The component can't guess your layout.

## 183: How do you make an SVG chart responsive?

Give the SVG a `viewBox` and let CSS set its width. Use `preserveAspectRatio` to control how it fits, and `vector-effect` to keep line widths readable.

```html
<svg
  class="chart"
  viewBox="0 0 600 300"
  preserveAspectRatio="xMidYMid meet"
  role="img"
  aria-label="Sales by month"
>
  <polyline
    points="0,250 100,200 200,220 300,120 400,140 500,60 600,80"
    fill="none"
    stroke="currentColor"
    stroke-width="2"
    vector-effect="non-scaling-stroke"
  />
</svg>
```

```css
.chart {
  width: 100%;
  height: auto;
}
```

When a chart is shown very small, text inside the SVG gets tiny too. For small screens, you may need fewer labels or a different chart, which usually means rendering it again with JavaScript at the new size.

## 184: How do you calculate the values for a fluid clamp() font size?

Decide on a minimum size at a minimum viewport, and a maximum size at a maximum viewport. Then find the line between those two points.

Example: 16px at a 320px viewport, 24px at a 1280px viewport.

1. Slope = (24 - 16) / (1280 - 320) = 0.008333
2. In `vw`: slope x 100 = 0.8333vw
3. Intercept = 16 - 0.008333 x 320 = 13.33px = 0.8333rem

```css
p {
  font-size: clamp(1rem, 0.8333rem + 0.8333vw, 1.5rem);
}
```

Tools like Utopia (utopia.fyi) do this math for you and generate a whole type scale and spacing scale.

## 185: Why should a fluid font size combine rem and vw, not use vw alone?

A size in `vw` only depends on the viewport width. When the user zooms the page in, the viewport gets smaller in CSS pixels, so the text barely grows, and sometimes even shrinks. It also ignores the user's default font size setting.

```css
/* Bad: doesn't respond to zoom or font settings */
h1 {
  font-size: 5vw;
}

/* Better */
h1 {
  font-size: clamp(2rem, 1.5rem + 2.5vw, 3.5rem);
}
```

The `rem` part grows with zoom and font settings. WCAG requires text to be resizable to 200%, and a pure `vw` size can fail that test.

## 186: What is a type scale and how do you make it responsive?

A type scale is a set of font sizes based on a ratio, like 1.2 or 1.25. Each heading level is the previous size multiplied by the ratio.

On small screens a smaller ratio works better, because big jumps make headings huge. On large screens a bigger ratio gives more contrast. You can define two scales and interpolate between them with `clamp()`:

```css
:root {
  --step-0: clamp(1rem, 0.96rem + 0.22vw, 1.125rem);
  --step-1: clamp(1.2rem, 1.12rem + 0.39vw, 1.41rem);
  --step-2: clamp(1.44rem, 1.31rem + 0.65vw, 1.76rem);
  --step-3: clamp(1.73rem, 1.52rem + 1.03vw, 2.2rem);
}

h1 {
  font-size: var(--step-3);
}
```

## 187: What does the WCAG Reflow criterion require?

WCAG 1.4.10 Reflow (level AA) says content must work at a width of 320 CSS pixels without scrolling in two directions. In practice, that's a 1280px wide window zoomed to 400%.

Users should only need to scroll vertically to read text. Exceptions are content that needs two dimensions to make sense, like data tables, maps, diagrams and toolbars.

A good responsive layout already meets this. To test it, set the browser to 1280px wide and zoom to 400%, or set the viewport to 320px in DevTools.

## 188: What does the WCAG Resize Text criterion require?

WCAG 1.4.4 Resize Text (level AA) says text must be resizable up to 200% without losing content or features. Assistive technology doesn't count, so it's about the browser's zoom and font size settings.

Common ways sites fail it:

- Font sizes in `vw` only.
- Containers with fixed `height` that cut off bigger text.
- `overflow: hidden` that hides text that no longer fits.
- Disabled zoom in the viewport meta tag.

Using `rem`, `min-height` and flexible containers keeps you safe.

## 189: What does the WCAG Text Spacing criterion mean for responsive layouts?

WCAG 1.4.12 Text Spacing (level AA) says no content should be lost when users override text spacing to at least:

- Line height 1.5 times the font size
- Paragraph spacing 2 times the font size
- Letter spacing 0.12 times the font size
- Word spacing 0.16 times the font size

Some users apply these with a browser extension. Text then takes more space, and boxes with a fixed height or width cut it off or overlap. The fix is the same as for responsive design: let boxes grow with their content.

## 190: What does the WCAG Orientation criterion require?

WCAG 1.3.4 Orientation (level AA) says content must not be locked to portrait or landscape, unless a specific orientation is really needed (like a piano app or a bank check scanner).

Some people have their device mounted in one orientation, for example on a wheelchair. Don't show a "please rotate your device" message, and don't use CSS to rotate the page. Make the layout work in both orientations.

## 191: What is :focus-visible and why is it useful on touch devices?

`:focus-visible` matches an element that has focus **and** where the browser thinks a focus ring should be shown, which is mostly when the user is using a keyboard. Clicking or tapping a button usually doesn't trigger it.

```css
button:focus-visible {
  outline: 3px solid #2563eb;
  outline-offset: 2px;
}
```

This lets you show a strong focus style for keyboard users without showing rings after every tap. Never remove focus styles with `outline: none` unless you replace them with something visible.

## 192: How do you handle the notch and rounded corners on phones?

Use `viewport-fit=cover` in the viewport meta tag so the page can draw under the notch, then use the `safe-area-inset-*` environment variables to keep content out of the unsafe areas.

```html
<meta
  name="viewport"
  content="width=device-width, initial-scale=1, viewport-fit=cover"
/>
```

```css
.site-header {
  padding-top: env(safe-area-inset-top);
}

.bottom-bar {
  padding-bottom: max(1rem, env(safe-area-inset-bottom));
  padding-inline: max(1rem, env(safe-area-inset-left));
}
```

Without `viewport-fit=cover`, the insets are 0 and the browser keeps the page inside the safe area by itself. The second argument of `env()` can be a fallback, for example `env(safe-area-inset-bottom, 0px)`.

## 193: What does the interactive-widget viewport setting do?

It controls what happens to the viewport when the on-screen keyboard opens.

```html
<meta
  name="viewport"
  content="width=device-width, initial-scale=1, interactive-widget=resizes-content"
/>
```

- `resizes-visual` (default in most browsers) - only the visual viewport shrinks. The layout viewport stays the same, so `dvh` and fixed elements don't change and the keyboard covers part of the page.
- `resizes-content` - the layout viewport shrinks too, so the page lays out again above the keyboard. Useful for chat apps where the input must stay visible.
- `overlays-content` - nothing resizes. The keyboard just covers the page.

Chrome on Android and Firefox support it. Safari on iOS doesn't, so test there separately.

## 194: What is the visualViewport API?

`window.visualViewport` describes the part of the page the user can actually see, which can be smaller than the layout viewport when the user pinch-zooms or when the on-screen keyboard is open.

```js
const vv = window.visualViewport;

function update() {
  document.documentElement.style.setProperty(
    "--visible-height",
    `${vv.height}px`,
  );
}

vv.addEventListener("resize", update);
vv.addEventListener("scroll", update);
update();
```

It has `width`, `height`, `offsetTop`, `offsetLeft` and `scale`. It's used to keep a toolbar right above the keyboard on iOS, where CSS alone can't do it.

## 195: When should you use svh, lvh or dvh?

- **svh** - for most "full screen" sections. Content always fits when the toolbars are visible, and the layout doesn't jump. There's a small gap when the toolbars hide.
- **lvh** - for backgrounds or decorative elements where being cut off a bit doesn't matter, and you want no gap.
- **dvh** - when the element must always match the visible height exactly, like a full-screen app shell or a modal. It changes while the user scrolls, which triggers layout and can make content jump.

```css
.hero {
  min-height: 100svh;
}

.app-shell {
  height: 100dvh;
}
```

## 196: How do you build an accessible off-canvas menu?

An off-canvas menu slides in from the side on small screens. To make it accessible:

- Open it with a real `<button>` that has `aria-expanded` and `aria-controls`.
- Move focus into the menu when it opens and back to the button when it closes.
- Close it with the Escape key and with a visible close button.
- Make the rest of the page unreachable while it's open, with `inert` on the main content.
- When it's closed, hide it fully (`display: none`, `visibility: hidden` or `inert`), not just move it off screen, so keyboard users can't tab into it.

```js
function openMenu() {
  menu.hidden = false;
  main.inert = true;
  toggle.setAttribute("aria-expanded", "true");
  menu.querySelector("a, button").focus();
}

function closeMenu() {
  menu.hidden = true;
  main.inert = false;
  toggle.setAttribute("aria-expanded", "false");
  toggle.focus();
}
```

A modal `<dialog>` gives you most of this for free.

## 197: How can the popover attribute help with responsive menus?

The `popover` attribute turns any element into a popup that shows in the top layer (above everything, no z-index fights). A button with `popovertarget` toggles it, with no JavaScript.

```html
<button popovertarget="main-menu">Menu</button>

<nav id="main-menu" popover>
  <a href="/">Home</a>
  <a href="/shop">Shop</a>
  <a href="/contact">Contact</a>
</nav>
```

With `popover` (or `popover="auto"`), clicking outside or pressing Escape closes it, and the browser handles focus returning. It's not modal, so the page behind stays interactive. It works in all modern browsers, which makes it a simple way to build a mobile menu or a dropdown.

## 198: How do you stop the page from scrolling behind an open menu or modal?

The simplest approach is to set `overflow: hidden` on the root while the menu is open:

```css
html:has(.menu[data-open="true"]) {
  overflow: hidden;
  scrollbar-gutter: stable; /* stop the layout from shifting on desktop */
}
```

A modal `<dialog>` doesn't lock page scroll by itself, but you can use the same rule with `html:has(dialog[open])`.

For the menu's own scroll area, add `overscroll-behavior: contain` so reaching its end doesn't start scrolling the page. Older iOS versions needed more involved fixes with `position: fixed` on the body, which you'll still see in older code.

## 199: What does overscroll-behavior do?

It controls what happens when a scroll area reaches its end.

- `auto` (default) - the scroll continues to the parent, and the browser may show bounce effects or pull-to-refresh.
- `contain` - no scroll chaining to the parent, but the bounce effect inside the element stays.
- `none` - no scroll chaining and no bounce or pull-to-refresh.

```css
.chat-messages,
.side-menu {
  overflow-y: auto;
  overscroll-behavior: contain;
}

body {
  overscroll-behavior-y: none; /* disable pull-to-refresh in a web app */
}
```

## 200: What does scrollbar-gutter do?

`scrollbar-gutter: stable` reserves space for the vertical scrollbar even when the content doesn't need to scroll. Without it, on desktops with classic scrollbars, the page jumps sideways when a scrollbar appears or disappears, for example when moving between short and long pages, or when a modal locks scrolling.

```css
html {
  scrollbar-gutter: stable;
}
```

It has no effect on overlay scrollbars, which most phones and macOS (by default) use, because those don't take up space.

## 201: What does touch-action do?

`touch-action` tells the browser which touch gestures it should handle itself (scrolling, pinch zoom) and which ones your code will handle.

```css
/* A drawing canvas: the page shouldn't scroll while drawing */
.canvas {
  touch-action: none;
}

/* A horizontal slider: let the page scroll vertically, handle horizontal swipes in JS */
.slider {
  touch-action: pan-y;
}

/* Allow scroll and pinch zoom but not double-tap zoom */
button {
  touch-action: manipulation;
}
```

Setting it in CSS lets the browser know in advance, so scrolling stays smooth and doesn't wait for JavaScript.

## 202: What was the 300ms tap delay and is it still a problem?

Early mobile browsers waited about 300ms after a tap to see if a second tap followed, because a double tap meant "zoom". Every tap on a link or button felt slow.

Modern mobile browsers remove the delay when the page has `<meta name="viewport" content="width=device-width">`. `touch-action: manipulation` also removes it. So it's not a problem anymore for responsive sites, and libraries like FastClick that fixed it are no longer needed.

## 203: What is the difference between pointer, touch and mouse events?

- **Mouse events** (`mousedown`, `click`) - for mice. Browsers also fire them after a tap, for compatibility.
- **Touch events** (`touchstart`, `touchmove`) - for touch screens. They support multiple fingers.
- **Pointer events** (`pointerdown`, `pointermove`, `pointerup`) - one API for mouse, touch and pen. Each event has a `pointerType` property.

```js
slider.addEventListener("pointerdown", (e) => {
  slider.setPointerCapture(e.pointerId);
  console.log(e.pointerType); // "mouse", "touch" or "pen"
});
```

Use pointer events for new code that handles dragging or drawing. For simple buttons and links, `click` works for every input.

## 204: How do you handle devices that have both touch and a mouse?

Laptops with touch screens, tablets with keyboards and trackpads, and phones connected to a monitor all have more than one input. `hover` and `pointer` only describe the primary input, so they can be misleading.

- Don't assume touch means no mouse, or the other way around.
- Make sure everything works by tapping, clicking and with the keyboard. Hover can add extras, but must not be the only way to reach something.
- Use `any-pointer: coarse` if you want bigger targets whenever any touch input is present.

```css
@media (any-pointer: coarse) {
  .menu a {
    padding-block: 0.75rem;
  }
}
```

## 205: How do you make a dropdown menu work on both mouse and touch?

Don't open menus on hover only. Touch screens have no hover, and keyboard users can't hover either.

Use a button that toggles the menu on click. On devices that can hover, you can add hover opening as an extra.

```html
<li class="has-submenu">
  <button aria-expanded="false" aria-controls="products-menu">Products</button>
  <ul id="products-menu" hidden>
    <li><a href="/laptops">Laptops</a></li>
    <li><a href="/phones">Phones</a></li>
  </ul>
</li>
```

```js
const btn = document.querySelector(".has-submenu button");
const menu = document.getElementById("products-menu");

btn.addEventListener("click", () => {
  const open = btn.getAttribute("aria-expanded") === "true";
  btn.setAttribute("aria-expanded", String(!open));
  menu.hidden = open;
});
```

## 206: How do you turn table rows into cards on small screens?

Change the table elements to `display: block` on small screens and show the column name next to each value with a `data-label` attribute.

```html
<table class="responsive-table">
  <thead>
    <tr>
      <th>Name</th>
      <th>Email</th>
      <th>Role</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td data-label="Name">Ana</td>
      <td data-label="Email">ana@example.com</td>
      <td data-label="Role">Admin</td>
    </tr>
  </tbody>
</table>
```

```css
@media (width < 640px) {
  .responsive-table thead {
    position: absolute;
    width: 1px;
    height: 1px;
    overflow: hidden;
    clip-path: inset(50%);
  }

  .responsive-table tr,
  .responsive-table td {
    display: block;
  }

  .responsive-table td::before {
    content: attr(data-label) ": ";
    font-weight: bold;
  }

  .responsive-table tr {
    margin-bottom: 1rem;
    border: 1px solid #ddd;
  }
}
```

## 207: Why can changing a table's display break it for screen readers?

When you set `display: block` or `display: flex` on `<table>`, `<tr>` or `<td>`, some browsers stop treating the elements as a table in the accessibility tree. Screen reader users lose the table navigation and the link between headers and cells.

You can restore the semantics by adding ARIA roles back:

```html
<table role="table">
  <thead role="rowgroup">
    <tr role="row">
      <th role="columnheader">Name</th>
    </tr>
  </thead>
  <tbody role="rowgroup">
    <tr role="row">
      <td role="cell">Ana</td>
    </tr>
  </tbody>
</table>
```

Or use the horizontal scroll approach, which keeps the table as a real table.

## 208: How do you make a table header and first column sticky inside a scroll container?

Put the table in a container that scrolls, then use `position: sticky` on the header cells and the first column.

```css
.table-wrap {
  overflow: auto;
  max-height: 70svh;
}

.table-wrap thead th {
  position: sticky;
  top: 0;
  z-index: 2;
  background: white;
}

.table-wrap tbody th {
  position: sticky;
  left: 0;
  z-index: 1;
  background: white;
}

.table-wrap thead th:first-child {
  left: 0;
  z-index: 3; /* top-left corner above both */
}
```

Sticky elements need a background, or the scrolled content shows through them. On mobile, this keeps the row labels visible while the user swipes through the columns.

## 209: What should you watch out for with a responsive carousel?

- **Touch** - users should be able to swipe. CSS scroll snap gives you this with no JavaScript.
- **Keyboard** - previous and next buttons must be real buttons and reachable with Tab.
- **Screen readers** - mark it up as a region with a label and say which slide is shown.
- **Auto-play** - avoid it. If you have it, add a pause button and respect `prefers-reduced-motion`.
- **Layout** - show part of the next slide on mobile so users know there's more.
- **Performance** - lazy load slides that aren't visible.

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

@media (width >= 900px) {
  .carousel {
    grid-auto-columns: calc((100% - 2rem) / 3);
  }
}
```

## 210: What is prefers-contrast?

It tells you if the user asked for more (or less) contrast in their system settings.

```css
@media (prefers-contrast: more) {
  :root {
    --text: #000;
    --border: #000;
  }

  .card {
    border: 2px solid var(--border);
  }

  .muted {
    color: var(--text); /* no light gray text */
  }
}
```

Values are `no-preference`, `more`, `less` and `custom`. Use it to remove subtle grays, add borders and make focus styles stronger.

## 211: What is forced-colors mode?

Forced colors mode (like Windows High Contrast / Contrast themes) replaces your colors with a small palette chosen by the user. Backgrounds, borders and text all get those colors, and background images and box shadows are often removed.

```css
@media (forced-colors: active) {
  .button {
    border: 2px solid ButtonText;
  }

  .icon {
    forced-color-adjust: auto;
  }
}
```

Problems show up when you use only a background color or a shadow to show a button or a focus state, because those disappear. Use real borders and outlines, which stay visible. You can use system color keywords like `CanvasText`, `ButtonText` and `Highlight` inside this query.

## 212: What does the light-dark() function do?

`light-dark()` returns its first value in light mode and its second in dark mode, based on the `color-scheme` in use.

```css
:root {
  color-scheme: light dark;
}

body {
  background: light-dark(#ffffff, #121212);
  color: light-dark(#1a1a1a, #e6e6e6);
}

.card {
  border-color: light-dark(#ddd, #333);
}
```

It saves you from writing the same selectors again inside `@media (prefers-color-scheme: dark)`. It only works for colors, and it needs `color-scheme` to be set. It works in all modern browsers.

## 213: How do you support both the system theme and a manual theme toggle?

Use the system setting by default and let a `data-theme` attribute override it.

```css
:root {
  color-scheme: light dark;
}

:root[data-theme="light"] {
  color-scheme: light;
}

:root[data-theme="dark"] {
  color-scheme: dark;
}

body {
  background: light-dark(white, #121212);
  color: light-dark(#222, #eee);
}
```

```js
const saved = localStorage.getItem("theme");
if (saved) document.documentElement.dataset.theme = saved;

toggle.addEventListener("click", () => {
  const next =
    document.documentElement.dataset.theme === "dark" ? "light" : "dark";
  document.documentElement.dataset.theme = next;
  localStorage.setItem("theme", next);
});
```

Put the script that reads the saved theme in the `<head>`, so the page doesn't flash the wrong theme on load.

## 214: What are prefers-reduced-transparency and prefers-reduced-data?

- `prefers-reduced-transparency` - the user asked the system for fewer transparent and blurred effects. Use it to replace frosted glass backgrounds with solid ones. Supported in Chromium browsers.
- `prefers-reduced-data` - meant to tell you that the user wants to save data. It's still experimental and not supported in stable browsers.

```css
@media (prefers-reduced-transparency: reduce) {
  .glass-panel {
    backdrop-filter: none;
    background: var(--surface);
  }
}
```

For saving data today, the `Save-Data` request header is more useful than the media query.

## 215: How do you show a different image in dark mode?

Use `<picture>` with a `prefers-color-scheme` media condition.

```html
<picture>
  <source srcset="diagram-dark.png" media="(prefers-color-scheme: dark)" />
  <img src="diagram-light.png" alt="Request flow diagram" />
</picture>
```

For inline SVGs, use `currentColor` or CSS variables instead, so one file works in both themes. Note that the `<picture>` approach follows the system theme, not a manual toggle on your site.

## 216: How do you use media queries in React, and what is the SSR problem?

A small hook with `matchMedia` works:

```jsx
import { useSyncExternalStore } from "react";

export function useMediaQuery(query) {
  return useSyncExternalStore(
    (callback) => {
      const mq = window.matchMedia(query);
      mq.addEventListener("change", callback);
      return () => mq.removeEventListener("change", callback);
    },
    () => window.matchMedia(query).matches,
    () => false, // value used on the server
  );
}
```

The problem is that the server doesn't know the screen size. It renders with the server value (here `false`), and the client may render something different, which causes a layout jump or a hydration mismatch. Where you can, do responsive layout in CSS, which works on the first paint. Use JS media queries only for behavior that can't be done in CSS.

## 217: What is ResizeObserver and when do you use it?

`ResizeObserver` calls a function when an element's size changes, for any reason: window resize, sidebar collapse, content changes, and so on.

```js
const observer = new ResizeObserver((entries) => {
  for (const entry of entries) {
    const width = entry.contentBoxSize[0].inlineSize;
    entry.target.classList.toggle("is-wide", width >= 600);
  }
});

observer.observe(document.querySelector(".chart"));
```

Use it when JavaScript must react to an element's size, for example to redraw a canvas chart. For pure styling, container queries are better because they need no JavaScript.

## 218: How is IntersectionObserver useful in responsive UIs?

`IntersectionObserver` tells you when an element enters or leaves the viewport (or another scroll container). It doesn't run on every scroll event, so it's cheap.

```js
const observer = new IntersectionObserver(
  (entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        loadWidget(entry.target);
        observer.unobserve(entry.target);
      }
    }
  },
  { rootMargin: "200px" },
);

document.querySelectorAll(".lazy-widget").forEach((el) => observer.observe(el));
```

Uses include lazy loading heavy widgets, infinite scroll, showing a "back to top" button, and changing a header when a hero section scrolls out of view.

## 219: Can you nest media queries in plain CSS?

Yes. Native CSS nesting works in all modern browsers, and you can put a media query or container query right inside a rule.

```css
.card {
  padding: 1rem;

  @media (width >= 768px) {
    padding: 2rem;
  }

  @container (width >= 400px) {
    display: grid;
    grid-template-columns: 1fr 2fr;
  }
}
```

This keeps all the styles for a component in one place, instead of having each breakpoint in a separate block at the bottom of the file.

## 220: Do media queries add specificity?

No. A rule inside a media query has the same specificity as the same rule outside. So when both apply, the one that comes later in the CSS wins.

```css
@media (width >= 768px) {
  .title {
    font-size: 2rem;
  }
}

.title {
  font-size: 1.5rem; /* wins on every screen, because it comes later */
}
```

That's why mobile-first CSS puts the base styles first and media queries after them. If an override in a media query doesn't work, check the order and the selector specificity.

## 221: How do you write a breakpoint mixin in Sass?

Keep breakpoints in a map and write one mixin to use them.

```scss
$breakpoints: (
  sm: 640px,
  md: 768px,
  lg: 1024px,
  xl: 1280px,
);

@mixin up($name) {
  @media (width >= map-get($breakpoints, $name)) {
    @content;
  }
}

.card {
  padding: 1rem;

  @include up(md) {
    padding: 2rem;
  }
}
```

Every breakpoint is defined in one place. In current Dart Sass, `map.get()` from `@use "sass:map"` is the recommended form of `map-get()`.

## 222: What is @custom-media?

`@custom-media` lets you give a media query a name and reuse it.

```css
@custom-media --tablet (width >= 768px);

@media (--tablet) {
  .nav {
    display: flex;
  }
}
```

It's part of the Media Queries Level 5 spec but browsers don't support it natively yet. You can use it today with PostCSS (postcss-custom-media) or Lightning CSS, which replace it with the real query at build time.

## 223: How do you share breakpoints between CSS and JavaScript?

There are a few options:

1. **Keep them in one source file** (JSON or design tokens) and generate both the CSS and the JS from it.
2. **Read a custom property from CSS** in JS. You can't use it in a media query, but you can read it:

```css
:root {
  --bp-md: 768px;
}
```

```js
const md = getComputedStyle(document.documentElement)
  .getPropertyValue("--bp-md")
  .trim();
const isMd = matchMedia(`(width >= ${md})`).matches;
```

3. **Let CSS tell JS which breakpoint is active**, for example by setting a custom property per breakpoint and reading it.

The aim is to never have the same number typed in two places.

## 224: What are design tokens and how do they help responsive design?

Design tokens are named values for colors, spacing, font sizes, breakpoints, radii and so on, stored in one place (often JSON) and turned into CSS variables, Sass variables or JS constants.

```css
:root {
  --font-size-body: 1rem;
  --space-section: 2rem;
}

@media (width >= 1024px) {
  :root {
    --font-size-body: 1.125rem;
    --space-section: 4rem;
  }
}
```

Responsive changes then happen by changing token values at breakpoints, not by changing many component styles. Designers and developers use the same names, which keeps the design and the code in sync.

## 225: How should you name breakpoints?

Use size names like `sm`, `md`, `lg`, `xl`, not device names like `mobile`, `tablet`, `desktop`.

Device names stop making sense quickly. A large phone in landscape is wider than a small tablet, and a tablet with a keyboard behaves like a laptop. `md` just means "medium width", which is always true. Most frameworks use this style, so other developers will know what it means.

## 226: How do you handle right-to-left languages in a responsive layout?

- Set `dir="rtl"` and the right `lang` on the `<html>` element.
- Use logical properties (`margin-inline-start`, `padding-inline`, `inset-inline-end`, `text-align: start`) instead of left and right.
- Flexbox and Grid already follow the text direction, so a `row` goes right to left automatically.
- Flip directional icons like arrows, but not things like a play icon or a clock.

```css
.icon-arrow:dir(rtl) {
  transform: scaleX(-1);
}

.card {
  padding-inline-start: 1rem;
  border-inline-start: 4px solid var(--accent);
}
```

With logical properties, you usually don't need any extra RTL stylesheet.

## 227: What does hyphens: auto do and why is lang needed?

`hyphens: auto` lets the browser break long words with a hyphen at the end of a line. It needs to know the language to put the hyphens in the right places, so set `lang` on the page or element.

```html
<html lang="de"></html>
```

```css
p {
  hyphens: auto;
}
```

It's very useful on narrow screens and in languages with long words like German or Finnish. Without hyphens, justified text gets big gaps and long words overflow.

## 228: How do you limit text to a set number of lines?

Use `line-clamp`. It cuts the text after a number of lines and adds an ellipsis.

```css
.card-description {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 3;
  overflow: hidden;
}
```

The prefixed version is the one that works in every browser today, even in Firefox. Use it for teasers in cards so every card has the same height, but make sure the full text is available somewhere, like on the detail page.

## 229: How do you truncate a single line of text inside a flex item?

`text-overflow: ellipsis` needs `white-space: nowrap` and `overflow: hidden`. Inside a flex item you also need `min-width: 0`, because flex items don't shrink below their content by default.

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
```

This is common in lists, chat apps and table cells where long names should fit on one line on a phone. Show the full text on another screen or in a tooltip so it's not lost.

## 230: What does field-sizing: content do?

`field-sizing: content` makes form fields like `<textarea>`, `<input>` and `<select>` grow and shrink to fit their content, instead of having a fixed size.

```css
textarea {
  field-sizing: content;
  min-height: 3lh;
  max-height: 10lh;
}
```

A comment box can start small and grow as the user types, with no JavaScript. Support is in Chromium browsers and recent Safari versions. Older browsers just keep the normal fixed size, so it's safe to add.

## 231: What does the enterkeyhint attribute do?

It changes the label or icon of the Enter key on the mobile keyboard.

```html
<input type="search" enterkeyhint="search" />
<input type="text" name="message" enterkeyhint="send" />
<input type="text" name="first-name" enterkeyhint="next" />
```

Values are `enter`, `done`, `go`, `next`, `previous`, `search` and `send`. It only changes the label. You still need to handle what happens when the key is pressed.

## 232: Why is position: sticky not working?

Common causes:

1. No `top`, `bottom`, `left` or `right` is set.
2. An ancestor has `overflow: hidden`, `auto` or `scroll`, so the element sticks inside that ancestor instead of the page.
3. The parent is not taller than the sticky element, so there's no room to stick.
4. In a flex or grid container, the item stretches to the full height of the row. Add `align-self: start`.
5. `display: contents` or a table display on a parent in some cases.

```css
.sidebar {
  position: sticky;
  top: 1rem;
  align-self: start; /* inside a grid or flex layout */
}
```

## 233: Why does a mobile menu sometimes appear behind other content?

Usually because of stacking contexts. `z-index` only compares elements in the same stacking context. If the menu is inside a parent with `transform`, `opacity` less than 1, `filter`, `position` with a `z-index`, or `isolation: isolate`, the menu can't go above things outside that parent, no matter how high its `z-index` is.

Fixes:

- Move the menu higher in the DOM, outside the parent that creates the context.
- Use `popover` or a modal `<dialog>`, which render in the top layer above everything.
- Keep a small, documented set of z-index values instead of `9999` everywhere.

## 234: How do you serve a different video file for small screens?

Use the `media` attribute on `<source>` inside `<video>`. Browsers support it again after it was removed for a few years.

```html
<video autoplay muted loop playsinline poster="poster.jpg">
  <source src="hero-mobile.mp4" media="(width < 768px)" type="video/mp4" />
  <source src="hero-desktop.mp4" type="video/mp4" />
</video>
```

The browser picks the source when the video loads. It doesn't switch if the viewport changes later. Mobile users get a smaller file, which matters for background videos.

## 235: What do you need for a video to autoplay on mobile?

Mobile browsers only allow autoplay when the video is muted. On iOS, the video also opens in full screen unless you add `playsinline`.

```html
<video autoplay muted loop playsinline poster="poster.jpg">
  <source src="loop.mp4" type="video/mp4" />
</video>
```

Also think about `prefers-reduced-motion`. For users who asked for less motion, show the poster or pause the video:

```js
if (matchMedia("(prefers-reduced-motion: reduce)").matches) {
  document.querySelector("video").pause();
}
```

## 236: How do you handle third-party embeds that aren't responsive?

Many widgets (maps, forms, social posts) come as an iframe or script with a fixed width.

- Override the width with `max-width: 100%` or `width: 100%` and set a height or `aspect-ratio`.
- If the widget's height depends on its content, check if it offers a resize message (many send `postMessage` with their height), and update the iframe height when it arrives.
- Check if the provider has a responsive option in their embed settings.
- As a last resort, put it in a container with `overflow-x: auto`.

```css
.embed-wrapper iframe {
  width: 100%;
  min-height: 400px;
  border: 0;
}
```

## 237: How should you load web fonts for a responsive site?

- Use WOFF2, which is the smallest format and works everywhere.
- Use `font-display: swap` (or `optional`) so text shows right away in a fallback font.
- Preload only the one or two fonts used above the fold.
- Subset fonts to the characters you need.
- Consider a variable font when you need many weights.

```css
@font-face {
  font-family: "Inter";
  src: url("/fonts/inter-var.woff2") format("woff2");
  font-weight: 100 900;
  font-display: swap;
}
```

```html
<link
  rel="preload"
  href="/fonts/inter-var.woff2"
  as="font"
  type="font/woff2"
  crossorigin
/>
```

On slow mobile networks, fonts can be a large part of the page weight. Using a system font stack avoids the download completely.

## 238: How do variable fonts help responsive typography?

A variable font is one file that contains a whole range of weights, widths and other styles. You can change them smoothly with CSS.

```css
h1 {
  font-weight: 800;
  font-stretch: 85%; /* narrower letters on small screens */
}

@media (width >= 900px) {
  h1 {
    font-stretch: 100%;
  }
}

body {
  font-optical-sizing: auto; /* uses the "opsz" axis if the font has it */
}
```

You get many styles for the price of one download. A narrower width axis can help long headings fit on phones, and the optical size axis adjusts letter shapes for small and large text.

## 239: What is the 62.5% root font-size trick and why should you avoid it?

Some projects set `html { font-size: 62.5%; }` so that `1rem` equals 10px, which makes math easier (`1.6rem` = 16px).

The problems:

- You have to set `font-size: 1.6rem` on the body again, and every third-party component that uses `rem` gets smaller text.
- It's easy to forget and end up with 10px text.
- It makes `rem` mean something different from every other project.

It does still respect the user's font settings, because it's a percentage. But modern tools (Sass functions, `calc()`, editor plugins) make the math easy without changing the root size. Keeping `html` at 100% is simpler.

## 240: What is the difference between browser zoom and the default font size setting?

- **Zoom** (Ctrl/Cmd and +) scales everything: text, images, `px` values and layout. In CSS pixels the viewport gets narrower, so media queries change. Zooming to 200% on a 1280px window gives you a 640px layout.
- **Default font size** (in browser settings) only changes the root font size. Anything in `rem` or `em` grows. Anything in `px` stays the same.

Many users with low vision change the default font size and never zoom. If your text and spacing are in `px`, nothing happens for them. That's a strong reason to use `rem` for font sizes.

## 241: What are the lh and rlh units?

- `1lh` equals the computed line height of the element.
- `1rlh` equals the line height of the root element.

```css
textarea {
  min-height: 3lh; /* exactly three lines tall */
}

.stack > * + * {
  margin-top: 1rlh; /* spacing that follows a vertical rhythm */
}

.callout {
  border-left: 4px solid;
  padding-block: 0.5lh;
}
```

They're handy for sizing things in lines of text, and they scale with font size changes at breakpoints. They work in all modern browsers.

## 242: How should line height change across screen sizes?

Body text usually reads well at a line height of 1.4 to 1.6. Wider columns need a bit more line height, so your eyes can find the next line, and narrow columns can use a bit less.

Large headings need less line height than body text, often 1.1 to 1.25, otherwise the gaps between lines look too big.

```css
body {
  line-height: 1.5;
}

h1 {
  line-height: 1.1;
}

@media (width >= 1024px) {
  .article {
    line-height: 1.65;
  }
}
```

Keep line height unitless so it scales with the font size.

## 243: How do you test responsive layouts automatically?

Run end-to-end tests at several viewport sizes. With Playwright:

```js
import { test, expect } from "@playwright/test";

const sizes = [
  { width: 375, height: 667 },
  { width: 768, height: 1024 },
  { width: 1440, height: 900 },
];

for (const size of sizes) {
  test(`nav at ${size.width}px`, async ({ page }) => {
    await page.setViewportSize(size);
    await page.goto("/");
    const menuButton = page.getByRole("button", { name: "Menu" });
    if (size.width < 768) {
      await expect(menuButton).toBeVisible();
    } else {
      await expect(menuButton).toBeHidden();
    }
  });
}
```

Playwright also has built-in device profiles (`devices["iPhone 15"]`) that set the viewport, DPR, user agent and touch support. You can also check that the page has no horizontal overflow at each size.

## 244: What is visual regression testing and how does it help with responsive UIs?

Visual regression testing takes screenshots of pages or components and compares them with approved screenshots from before. If something moved, the test fails and shows the difference.

Responsive bugs often only show up at one width, and nobody checks every page at every size by hand. Taking screenshots at a few widths for each key page catches problems like a wrapping nav or a broken grid.

```js
test("home page on mobile", async ({ page }) => {
  await page.setViewportSize({ width: 375, height: 800 });
  await page.goto("/");
  await expect(page).toHaveScreenshot("home-mobile.png");
});
```

Tools include Playwright, Chromatic (for Storybook), Percy and BackstopJS.

## 245: What does Lighthouse check for mobile?

Lighthouse runs on a simulated mid-range phone with a slow network by default. It checks:

- **Performance** - LCP, CLS, Total Blocking Time and more, plus tips like properly sized images and modern formats.
- **Accessibility** - tap targets, contrast, labels, zoom not disabled.
- **Best practices** - images with the right aspect ratio and resolution.
- **SEO** - a viewport meta tag, readable font sizes.

It's a quick first check, but it's lab data. Real users on real phones can have different numbers, which you see in field data like the Chrome UX Report or your own monitoring.

## 246: What does DevTools device mode change, and what doesn't it?

It changes:

- The viewport size and device pixel ratio.
- The user agent string (if you pick a device preset).
- Touch emulation, so `hover` and `pointer` media queries report touch.
- Optionally the network and CPU speed.

It doesn't change:

- The browser engine. Chrome's device mode still runs Blink, not Safari's WebKit.
- The real mobile toolbar, keyboard and safe area behavior.
- Real GPU, memory and thermal limits.
- Font rendering and form controls of the real OS.

It's great for fast layout work. Final checks still need real devices.

## 247: How do you debug a page on a real phone?

- **Android** - enable USB debugging on the phone, connect it, and open `chrome://inspect` in desktop Chrome. You get full DevTools for the page running on the phone.
- **iOS** - enable Web Inspector in Safari settings on the iPhone, connect it to a Mac, and open the Develop menu in desktop Safari.
- **Local dev server** - use your computer's local IP address on the phone, or forward ports with `chrome://inspect` port forwarding.

This lets you inspect the real layout, see console errors and check how the page behaves with the real keyboard and toolbars.

## 248: What are Client Hints?

Client Hints are HTTP request headers that a browser sends with information about the device, if the server asks for them. The server can then send a different response, like a smaller image.

```http
Accept-CH: Sec-CH-DPR, Sec-CH-Viewport-Width, Sec-CH-Width
```

After that, requests include headers like:

```http
Sec-CH-DPR: 2
Sec-CH-Viewport-Width: 390
```

They're mostly used by image CDNs. Only Chromium browsers support them, so you still need `srcset` as the main solution. The server must also send `Vary` for those headers so caches store separate copies.

## 249: Why is user agent sniffing a bad way to build responsive sites?

User agent sniffing means reading the `User-Agent` string to guess if the device is a phone and serving different HTML or CSS.

Problems:

- User agent strings are messy and unreliable. iPads report themselves as Macs, and browsers are reducing the details in the string.
- The device type doesn't tell you the window size. A desktop browser can be narrow, and a phone can be connected to a big monitor.
- It's easy to get wrong and hard to keep up to date.
- It makes caching harder.

Use CSS for layout. If the server really needs device information, use Client Hints.

## 250: What is adaptive loading?

Adaptive loading means changing what you load based on the user's device and network, not just the screen size. On a slow phone with a weak connection you might skip heavy features.

```js
const conn = navigator.connection;
const slow = conn && (conn.saveData || /2g/.test(conn.effectiveType));
const lowMemory = navigator.deviceMemory && navigator.deviceMemory <= 2;

if (!slow && !lowMemory) {
  import("./video-background.js");
}
```

`navigator.connection` and `navigator.deviceMemory` are only available in Chromium browsers, so treat them as hints and have a sensible default. The `Save-Data: on` request header lets the server do the same.

## 251: What is the priority+ navigation pattern?

Priority+ shows as many nav links as fit in the available width and moves the rest into a "More" menu. On a wide screen all links are visible. On a narrow screen only the most important ones are, plus "More".

It's better than hiding everything behind a hamburger, because users still see the main sections. It usually needs a bit of JavaScript with `ResizeObserver` to measure the links and decide which ones fit. A simpler CSS-only version hides the less important links at certain breakpoints and always shows a "More" button.

## 252: When does a bottom navigation bar make sense on mobile?

A bottom tab bar is useful in web apps with three to five main sections that users switch between often, like Home, Search, Cart and Account. It's easy to reach with the thumb on a big phone, and the sections are always visible.

```css
.tab-bar {
  position: fixed;
  inset-inline: 0;
  bottom: 0;
  display: flex;
  justify-content: space-around;
  padding-bottom: env(safe-area-inset-bottom);
  background: var(--surface);
}

main {
  padding-bottom: calc(4rem + env(safe-area-inset-bottom));
}

@media (width >= 900px) {
  .tab-bar {
    display: none;
  }
}
```

Leave room at the bottom of the page so the bar doesn't cover content, and handle the home indicator safe area.

## 253: How do you build a bottom sheet on mobile that is a centered modal on desktop?

Use one `<dialog>` and change its position with a media query.

```css
dialog {
  border: 0;
  border-radius: 12px;
  width: min(100% - 2rem, 560px);
  max-height: 85svh;
}

@media (width < 640px) {
  dialog {
    width: 100%;
    max-width: 100%;
    margin: auto 0 0;
    border-radius: 16px 16px 0 0;
    padding-bottom: max(1rem, env(safe-area-inset-bottom));
  }
}

dialog::backdrop {
  background: rgb(0 0 0 / 0.4);
}
```

On phones, a sheet coming from the bottom is easier to reach with the thumb. On desktop, a centered modal looks more natural.

## 254: How would you build a responsive dashboard layout?

- Use Grid for the page shell: a sidebar and a main area on desktop, a top bar with a drawer on mobile.
- Put the widgets in a grid with `auto-fit` and `minmax()` so the number of columns adapts.
- Make each widget a container so its content (charts, tables, numbers) adapts to its own width with container queries.
- Let important widgets span more columns on wide screens.

```css
.dashboard {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(300px, 100%), 1fr));
  gap: 1rem;
}

.widget {
  container-type: inline-size;
}

@container (width >= 500px) {
  .widget .stats {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (width >= 1200px) {
  .widget--wide {
    grid-column: span 2;
  }
}
```

## 255: How do you keep buttons aligned at the bottom of cards with different content lengths?

Make each card a flex column and push the button down with `margin-top: auto`.

```css
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
}

.card {
  display: flex;
  flex-direction: column;
}

.card .button {
  margin-top: auto;
}
```

Grid items in the same row are the same height by default, so all buttons line up at the bottom. If you also want titles and descriptions to line up across cards, use `subgrid` for the card rows.

## 256: How do you build a sidebar that collapses into a drawer on mobile?

On wide screens the sidebar is a normal grid column. On narrow screens it's hidden and opens as an overlay.

```css
.app {
  display: grid;
  grid-template-columns: 1fr;
}

.sidebar {
  position: fixed;
  inset: 0 auto 0 0;
  width: min(80%, 300px);
  transform: translateX(-100%);
  transition: transform 0.2s;
  visibility: hidden;
}

.sidebar.is-open {
  transform: none;
  visibility: visible;
}

@media (width >= 1024px) {
  .app {
    grid-template-columns: 260px 1fr;
  }

  .sidebar {
    position: static;
    width: auto;
    transform: none;
    visibility: visible;
  }

  .sidebar-toggle {
    display: none;
  }
}
```

`visibility: hidden` stops keyboard users from tabbing into the closed drawer. The transition still runs because `visibility` can be animated.

## 257: How would you make a pricing table responsive?

A pricing table often has three or four plans side by side with a list of features.

- On desktop, show the plans in columns with a grid, so features line up.
- On mobile, stack the plans as cards, one after another, with the recommended plan first or clearly marked.
- For a detailed feature comparison, use a real table in a horizontal scroll container, with the feature name column sticky.

```css
.plans {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit, minmax(min(260px, 100%), 1fr));
}
```

Avoid squeezing four columns onto a phone screen. Nobody can compare tiny columns.

## 258: How do you build a responsive image gallery?

Use a grid with `auto-fill` and give every image the same aspect ratio with `object-fit: cover`.

```html
<ul class="gallery">
  <li><img src="1.jpg" alt="..." loading="lazy" width="600" height="400" /></li>
  <li><img src="2.jpg" alt="..." loading="lazy" width="600" height="800" /></li>
</ul>
```

```css
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(160px, 100%), 1fr));
  gap: 0.5rem;
  padding: 0;
  list-style: none;
}

.gallery img {
  width: 100%;
  aspect-ratio: 1;
  object-fit: cover;
}
```

Add `srcset` with small thumbnail sizes, because gallery images are shown small and a full-size photo per tile is a lot to download on mobile.

## 259: How do you build a masonry layout today?

A masonry layout has items of different heights packed into columns with no gaps, like Pinterest.

Options today:

- **CSS multi-column** - `columns: 250px`. Simple and responsive, but items flow top to bottom in each column, so the order goes down, not across.
- **JavaScript** - a library that measures items and positions them.
- **Native CSS masonry** - the CSS working group has agreed on a native masonry feature for Grid (being built as `display: grid-lanes`), but it's still experimental and not ready for production.

```css
.masonry {
  columns: 250px;
  column-gap: 1rem;
}

.masonry > * {
  break-inside: avoid;
  margin-bottom: 1rem;
}
```

## 260: How do you build a responsive hero section?

```html
<section class="hero">
  <img
    class="hero-img"
    src="hero-1280.jpg"
    srcset="hero-640.jpg 640w, hero-1280.jpg 1280w, hero-1920.jpg 1920w"
    sizes="100vw"
    alt=""
    fetchpriority="high"
  />
  <div class="hero-content">
    <h1>Fresh coffee, delivered</h1>
    <a class="button" href="/shop">Shop now</a>
  </div>
</section>
```

```css
.hero {
  display: grid;
  min-height: min(80svh, 700px);
}

.hero > * {
  grid-area: 1 / 1; /* stack image and content in the same cell */
}

.hero-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.hero-content {
  align-self: end;
  padding: clamp(1rem, 5vw, 4rem);
}

.hero h1 {
  font-size: clamp(2rem, 1.2rem + 4vw, 4.5rem);
}
```

Stacking with `grid-area: 1 / 1` avoids absolute positioning. Use a shorter height on phones in landscape so the content is still visible, and make sure the text has enough contrast over the image.

## 261: What does display: contents do and what is the accessibility concern?

`display: contents` makes the element's box disappear, so its children act as if they were direct children of the element's parent. It's useful when a wrapper gets in the way of a grid or flex layout.

```css
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}

.grid .group {
  display: contents; /* its children become grid items */
}
```

Browsers used to remove the element from the accessibility tree too, so a `<ul>` or `<button>` with `display: contents` lost its meaning for screen readers. Most of those bugs are fixed in current browsers, but avoid using it on buttons, links, tables and lists, and test with a screen reader if you do.

## 262: How does placing grid items visually affect tab order?

Tab order and screen reader order always follow the DOM, not the grid position. If you use `grid-template-areas`, `order` or line numbers to move items around at a breakpoint, keyboard focus can jump from the top of the page to the bottom and back.

```css
@media (width >= 900px) {
  .page {
    grid-template-areas: "sidebar main";
  }
}
```

If the sidebar comes after `main` in the HTML, the layout above shows it first, but keyboard users still reach `main` first. That's fine for a sidebar. It's a problem when the visual order really changes the meaning, like steps in a form.

A newer property, `reading-flow`, lets the browser follow the visual order for focus in grid and flex layouts. It's only in Chromium browsers so far.

## 263: What are named grid lines?

You can give names to grid lines and place items by name instead of number.

```css
.layout {
  display: grid;
  grid-template-columns:
    [full-start] 1rem
    [content-start] 1fr
    [content-end] 1rem
    [full-end];
}

.content {
  grid-column: content-start / content-end;
}

/* Short form: lines named "content-start" and "content-end" create an area called "content" */
.content {
  grid-column: content;
}
```

Names stay the same when you change the column sizes at a breakpoint, so the item placement code doesn't need to change.

## 264: What is the difference between justify-items and justify-content in Grid?

- `justify-content` moves the **whole grid** inside its container, when the grid tracks are smaller than the container. For example, centering a grid of fixed-width columns.
- `justify-items` aligns each **item inside its own cell**, along the inline axis.

```css
.grid {
  display: grid;
  grid-template-columns: repeat(3, 200px);
  justify-content: center; /* centers the three columns in the container */
  justify-items: start; /* each item sits at the start of its cell */
}
```

The same goes for `align-content` and `align-items` on the block axis.

## 265: What does align-content do in a wrapping flex container?

`align-content` only has an effect when a flex container has multiple lines (with `flex-wrap: wrap`). It controls how the lines are spaced along the cross axis.

```css
.tags {
  display: flex;
  flex-wrap: wrap;
  align-content: flex-start; /* lines packed at the top */
  height: 200px;
}
```

The default is `normal`, which acts like `stretch`, so lines spread out to fill the height. That surprises people when they see big gaps between wrapped rows. `align-items` aligns items within each line, while `align-content` aligns the lines themselves.

## 266: What is the difference between flex-basis and width?

`flex-basis` sets the starting size of a flex item along the main axis, before growing or shrinking. `width` is the size in the horizontal direction.

- In a `row` container, `flex-basis` wins over `width` if both are set. If `flex-basis` is `auto`, the item uses its `width`.
- In a `column` container, `flex-basis` controls the height, and `width` still controls the width.
- `min-width` and `max-width` still limit the final size.

```css
.item {
  flex: 1 1 300px; /* start at 300px, grow and shrink as needed */
  max-width: 500px;
}
```

So in flex layouts, `flex-basis` is usually the right property for the main size.

## 267: Why do images or avatars get squished in a flex row, and how do you fix it?

Flex items have `flex-shrink: 1` by default. When the row runs out of space, every item shrinks, including the avatar or icon that should stay a fixed size.

```css
.comment {
  display: flex;
  gap: 0.75rem;
}

.comment .avatar {
  flex-shrink: 0;
  width: 48px;
  height: 48px;
}

.comment .body {
  min-width: 0; /* let the text shrink instead */
}
```

`flex-shrink: 0` (or `flex: none`) keeps the avatar at its size, and the text column shrinks and wraps.

## 268: Why do images stretch in a flex row and how do you stop it?

Flex items stretch to the height of the row by default (`align-items: stretch`). If the text next to an image is taller than the image, the image is stretched vertically.

```css
.media {
  display: flex;
  gap: 1rem;
  align-items: flex-start; /* don't stretch */
}
```

You can also set `align-self: flex-start` on just the image, or keep the stretch and use `object-fit: cover` if you want it to fill the height without distortion.

## 269: How do media queries interact with the cascade?

Media queries don't change how the cascade works. When a media query matches, its rules are added to the cascade like any other rule, with the same specificity. When it doesn't match, its rules are ignored.

So:

- If two rules have the same specificity, the later one wins, whether it's in a media query or not.
- A more specific selector outside a media query beats a less specific one inside it.
- With cascade layers (`@layer`), the layer order comes before specificity and source order.

```css
.card .title {
  color: navy;
}

@media (width >= 768px) {
  .title {
    color: crimson; /* never applies: lower specificity */
  }
}
```

## 270: Should you group media queries at the end of the file or keep them with each component?

Two common styles:

- **Grouped by breakpoint** - all styles for 768px in one block at the end of the file. Easy to see what changes at each size, but a component's styles are spread across the file.
- **Next to each component** - each rule or component has its own media queries right after it, or nested inside it. Easier to maintain, because everything about the component is in one place.

Most teams use the second style today, especially with CSS nesting, Sass mixins or component-scoped CSS. The extra repeated `@media` lines don't matter for performance, and compression removes most of the size difference.

## 271: What is component-driven responsive design?

Instead of designing a few full page layouts for mobile, tablet and desktop, you design components that adapt to whatever space they get. A product card knows how to look at 250px, 400px and 700px wide, no matter which page or column it's in.

Container queries are what make this practical. Media queries handle the page layout, and each component handles itself. It fits well with design systems and component libraries like Storybook, where you can test each component at different container widths.

## 272: How do you design for very large screens?

Large monitors, ultrawide displays and TVs bring their own problems:

- Lines of text get too long. Limit content width with `max-width` in `ch`.
- Layouts look empty. Add more columns to grids, or show more content side by side.
- Things look too small from a distance. Increase the base font size a bit at large breakpoints.
- Full-width images can get blurry. Provide large enough image sizes in `srcset`, or cap the width.

```css
.container {
  max-width: 1440px;
  margin-inline: auto;
}

@media (width >= 1800px) {
  html {
    font-size: 112.5%;
  }
}
```

## 273: How do you make sure a focused input isn't hidden behind the keyboard or a sticky header?

Browsers scroll a focused field into view, but a sticky header or footer can still cover it.

```css
html {
  scroll-padding-top: 5rem; /* height of the sticky header */
  scroll-padding-bottom: 5rem; /* height of a sticky footer */
}

input,
textarea {
  scroll-margin-block: 1rem;
}
```

`scroll-padding` on the scroll container and `scroll-margin` on the element both tell the browser to leave space when it scrolls something into view. For iOS keyboard issues, you might also need the `visualViewport` API to keep fixed toolbars above the keyboard.

## 274: Why is building responsive emails different from web pages?

Email clients have very limited and inconsistent CSS support. Some desktop clients like older Outlook versions use Word to render HTML, and many clients strip `<style>` blocks or don't support media queries.

So email developers:

- Use tables for layout.
- Inline the CSS on each element.
- Build a single column layout that works without media queries, often around 600px wide, and use media queries only as an extra.
- Use `max-width` and fluid widths in percentages.
- Test with tools like Litmus or Email on Acid.

Tools like MJML or React Email generate this kind of HTML for you.

## 275: How do you control page breaks and page size when printing?

Use the fragmentation properties and the `@page` rule.

```css
@page {
  size: A4;
  margin: 2cm;
}

@media print {
  h2 {
    break-before: page; /* each section starts on a new page */
  }

  figure,
  table,
  .card {
    break-inside: avoid;
  }

  h2,
  h3 {
    break-after: avoid; /* don't leave a heading alone at the bottom */
  }
}
```

The older `page-break-before` and `page-break-inside` properties still work as aliases. Browser support for `@page` margin boxes and some sizes differs, so check in each browser's print preview.

## 276: How do you show a different logo on small screens?

Use `<picture>` with a media condition. A full logo with text on wide screens, just the icon on narrow ones.

```html
<a href="/" class="logo">
  <picture>
    <source media="(width < 600px)" srcset="logo-icon.svg" />
    <img src="logo-full.svg" alt="Acme Inc. home" width="160" height="40" />
  </picture>
</a>
```

The `alt` stays the same because it describes the link, not the picture. If the logo is an inline SVG, you can hide the text part with CSS at small widths instead.

## 277: How do container query units help with responsive spacing?

`cqi` makes spacing and sizes follow the component's container instead of the viewport. A card in a narrow sidebar gets small padding, and the same card in a wide area gets more, without any breakpoint.

```css
.card-wrapper {
  container-type: inline-size;
}

.card {
  padding: clamp(0.75rem, 4cqi, 2rem);
  gap: clamp(0.5rem, 2cqi, 1.5rem);
}
```

Use `clamp()` around it so the values don't get too small or too big.

## 278: Should headings scale with the viewport or with the container?

Page-level headings, like the main `h1`, usually make sense with viewport-based fluid sizes, because they belong to the page.

Headings inside reusable components, like card titles or widget headings, are better with container units, so they fit the space the component is placed in. A card title sized in `vw` is huge in a narrow sidebar on a wide screen.

```css
.page-title {
  font-size: clamp(2rem, 1.25rem + 3vw, 3.5rem);
}

.card-wrapper {
  container-type: inline-size;
}

.card-title {
  font-size: clamp(1.1rem, 0.9rem + 3cqi, 1.6rem);
}
```

Always keep a `rem` part in the formula so the text still scales with zoom.

## 279: When should you use an auto-fit grid and when container queries for cards?

- An **auto-fit grid** changes the number of columns based on available space. Each card gets narrower or wider, but the card's internal layout stays the same.
- **Container queries** change the inside of each card based on its own width: stacked image and text when narrow, side by side when wide.

They work well together. The grid decides how many cards fit in a row, and container queries decide what each card looks like at the width it ended up with.

```css
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(280px, 100%), 1fr));
}

.cards > li {
  container-type: inline-size;
}

@container (width >= 450px) {
  .card {
    grid-template-columns: 40% 1fr;
  }
}
```

## 280: How do you show fewer items on small screens?

You can hide items after a certain count with `:nth-child()` inside a media query.

```css
/* Show only the first 4 products on phones */
@media (width < 640px) {
  .product-list > li:nth-child(n + 5) {
    display: none;
  }
}
```

Remember that the hidden items are still downloaded, including their images unless they're lazy loaded. If the list is long, it's often better to load fewer items from the server and add a "Show more" button.

## 281: What other useful media features exist besides width?

- `prefers-color-scheme`, `prefers-reduced-motion`, `prefers-contrast` - user preferences.
- `hover`, `any-hover`, `pointer`, `any-pointer` - input types.
- `orientation`, `aspect-ratio`, `height` - viewport shape.
- `resolution` - pixel density.
- `display-mode` - whether the site runs as an installed app, in the browser or full screen.
- `scripting` - whether JavaScript is enabled (`enabled`, `none`, `initial-only`).
- `update` - how fast the output can change (`fast`, `slow` for e-ink, `none` for print).
- `forced-colors` - Windows contrast themes.
- `dynamic-range` and `color-gamut` - HDR and wide color screens.

```css
@media (scripting: none) {
  .js-only {
    display: none;
  }
}
```

## 282: How do you style a site differently when it's installed as a PWA?

Use the `display-mode` media feature. It matches the value from the web app manifest when the site is installed and opened from the home screen.

```css
@media (display-mode: standalone) {
  .install-banner {
    display: none;
  }

  .site-header {
    padding-top: env(safe-area-inset-top);
  }
}
```

In an installed app there's no browser address bar, so you may want to show a back button or adjust spacing. In JS you can check `matchMedia("(display-mode: standalone)").matches`.

## 283: How can you use :has() to lock scrolling when a menu is open?

Instead of adding a class to the body from JavaScript, check the menu's state in CSS.

```css
html:has(.mobile-menu[aria-hidden="false"]),
html:has(dialog[open]) {
  overflow: hidden;
}
```

```html
<div class="mobile-menu" aria-hidden="false">...</div>
```

The JavaScript only has to update the menu's attribute, and the page lock follows automatically. This keeps the state in one place.

## 284: When should you use object-fit on an img and when background-size on a CSS background?

Use an `<img>` with `object-fit` when the image is content: product photos, article images, avatars. You get `alt` text, `srcset`, `sizes`, lazy loading and `fetchpriority`, and the browser's preload scanner finds it early.

Use a CSS background with `background-size` when the image is purely decorative: patterns, textures and decorative shapes.

```css
/* Content image */
.product img {
  width: 100%;
  aspect-ratio: 4 / 3;
  object-fit: cover;
}

/* Decoration */
.section {
  background: url("dots.svg") repeat;
  background-size: 24px;
}
```

A common mistake is using a background image for the main hero image. It can't have alt text, and it loads later, which hurts LCP.

## 285: How do you avoid layout shift from ads or embeds in a responsive layout?

Reserve space for them before they load. The space often needs to differ by breakpoint, because ad sizes change.

```css
.ad-slot {
  min-height: 250px;
}

@media (width >= 768px) {
  .ad-slot {
    min-height: 90px; /* leaderboard size on desktop */
  }
}

.embed-slot {
  aspect-ratio: 16 / 9;
}
```

Use the most common size the slot will get. If the ad doesn't fill, keep the space or collapse it in a way that doesn't push content the user is reading.

## 286: How do you build a split-screen layout that stacks on mobile?

```css
.split {
  display: grid;
  min-height: 100svh;
}

@media (width >= 900px) {
  .split {
    grid-template-columns: 1fr 1fr;
  }
}

.split-media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.split-content {
  display: grid;
  place-content: center;
  padding: clamp(1.5rem, 5vw, 4rem);
}
```

On mobile, decide which half matters more. For a login page, the form should come first and the image can be small or hidden. Put the most important half first in the HTML.

## 287: What does a fallback for container queries look like?

Container queries work in all modern browsers, so most projects don't need a fallback. If you must support older browsers:

- Write a decent default layout outside the container query, so older browsers still get something usable.
- Optionally add a media query that approximates the container query for the common case.
- Wrap the container query version in `@supports` if needed.

```css
.card {
  display: grid;
  gap: 1rem; /* single column for everyone */
}

@supports not (container-type: inline-size) {
  @media (width >= 900px) {
    .card {
      grid-template-columns: 150px 1fr;
    }
  }
}

@container (width >= 400px) {
  .card {
    grid-template-columns: 150px 1fr;
  }
}
```

## 288: How do you handle user-generated content of unknown length in responsive components?

You can't control what users type, so plan for very short, very long and missing content.

- Let long words and URLs wrap with `overflow-wrap: anywhere`.
- Use `min-width: 0` on flex and grid children.
- Limit long text with `line-clamp` in teasers and show the full text elsewhere.
- Use `min-height` instead of `height`.
- Handle missing images with a placeholder and a fixed `aspect-ratio`.
- Test with real data, long names in other languages, and empty fields.

```css
.user-bio {
  overflow-wrap: anywhere;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 4;
  overflow: hidden;
}
```

## 289: How do you make responsive images work for content from a CMS?

Editors usually upload one image, so the system has to create the other sizes.

- Use an image CDN or the CMS's image API to generate sizes on request.
- Generate `srcset` and `sizes` in the template that renders the content, based on where the image is placed.
- Strip or override fixed `width` and `height` styles that editors may add, and keep the attributes.
- Set a maximum upload size and let the system create compressed versions.

```html
<img
  src="https://cms.example.com/img/abc.jpg?w=800"
  srcset="
    https://cms.example.com/img/abc.jpg?w=400   400w,
    https://cms.example.com/img/abc.jpg?w=800   800w,
    https://cms.example.com/img/abc.jpg?w=1200 1200w
  "
  sizes="(width >= 800px) 700px, 100vw"
  width="1200"
  height="800"
  alt="Alt text from the CMS"
  loading="lazy"
/>
```

## 290: How do you test text zoom and larger font settings?

- **Browser zoom** - zoom to 200% and 400% and check that nothing overlaps or gets cut off and that there's no horizontal scrolling.
- **Default font size** - in Chrome, Settings, Appearance, Font size, set it to "Very large". In Firefox you can also choose "Zoom text only".
- **Mobile** - turn on large text in iOS (Dynamic Type affects Safari only if you use `font: -apple-system-body`) and Android settings and check the page.
- **Text spacing** - use a bookmarklet that applies the WCAG text spacing values.

Fixed heights, `px` font sizes and `overflow: hidden` are the usual causes of problems.

## 291: What does mobile-first mean for performance, not just CSS?

Mobile-first CSS is only part of it. Phones also have slower CPUs, less memory and often slower networks. Mobile-first performance means:

- Sending small images by default and bigger ones only when needed.
- Loading less JavaScript up front and lazy loading the rest.
- Not loading desktop-only features on mobile.
- Testing on a mid-range Android phone, not only on a fast iPhone or a laptop.
- Setting a performance budget for page weight and LCP on mobile.

A page that's fast on mobile will almost always be fast on desktop too.

## 292: How do you avoid loading desktop-only JavaScript on mobile?

Check a media query before importing the code.

```js
const desktop = window.matchMedia("(width >= 1024px)");

async function loadMegaMenu() {
  if (desktop.matches) {
    const { initMegaMenu } = await import("./mega-menu.js");
    initMegaMenu();
  }
}

loadMegaMenu();
desktop.addEventListener("change", loadMegaMenu);
```

The bundler splits `mega-menu.js` into a separate file that phones never download. Make sure `initMegaMenu` only runs once if the user resizes back and forth.

## 293: How do you combine image-set() with media queries for backgrounds?

Use media queries for the width and `image-set()` for pixel density.

```css
.banner {
  background-image: image-set("banner-600.jpg" 1x, "banner-1200.jpg" 2x);
  background-size: cover;
}

@media (width >= 900px) {
  .banner {
    background-image: image-set("banner-1400.jpg" 1x, "banner-2800.jpg" 2x);
  }
}
```

This gives you width and density switching, similar to `srcset`, but you have to choose the steps yourself.

## 294: What does text-size-adjust do?

Some mobile browsers increase the font size of text in wide blocks to make it easier to read, especially in landscape. On iOS, rotating the phone can suddenly make text bigger.

```css
html {
  -webkit-text-size-adjust: 100%;
  text-size-adjust: 100%;
}
```

This tells the browser not to change the font size on its own. Use `100%`, not `none`. `none` can stop users from zooming text in some browsers. It's mainly needed on pages that already have a proper responsive layout.

## 295: How do you mix fixed and flexible columns in a grid?

Combine fixed sizes, `minmax()` and `fr` in one track list.

```css
.layout {
  display: grid;
  grid-template-columns: minmax(200px, 280px) minmax(0, 1fr) 300px;
  gap: 1.5rem;
}

@media (width < 1100px) {
  .layout {
    grid-template-columns: minmax(200px, 240px) minmax(0, 1fr);
  }

  .layout .ads {
    grid-column: 1 / -1;
  }
}

@media (width < 768px) {
  .layout {
    grid-template-columns: 1fr;
  }
}
```

The sidebar has a range, the main column takes the rest, and the right column is fixed. At smaller sizes columns are removed one at a time.

## 296: How do you make equal-height columns?

With Flexbox or Grid, items in the same row are the same height by default, because of `align-items: stretch`.

```css
.columns {
  display: flex;
  gap: 1rem;
}

.columns > * {
  flex: 1;
}
```

Before Flexbox, this needed table display or background image tricks. The only thing to watch is that you don't set `align-items` to something else, or set a fixed height on the items.

## 297: How do you debug responsive CSS in DevTools?

- **Device toolbar** - test widths, and use the media query bar (enable "Show media queries") to see and click on breakpoints.
- **Grid and Flexbox overlays** - click the `grid` or `flex` badge next to an element in the Elements panel to see lines, gaps and areas.
- **Computed tab** - see the final value of a property and which rule set it.
- **Styles pane** - shows which media query or container query each rule comes from, and container queries link to their container.
- **Rendering tab** - emulate `prefers-color-scheme`, `prefers-reduced-motion`, `forced-colors` and print.
- **Layout shift regions** - highlight elements that move during load.

## 298: How would you check a page for responsive problems before release?

A quick checklist:

1. Drag the viewport from 320px to 2000px wide and watch for breaks.
2. Check that there's no horizontal scrolling at any width.
3. Check landscape on a phone and short desktop windows.
4. Zoom to 200% and 400%.
5. Increase the browser's default font size.
6. Check touch targets and that hover-only features have a tap version.
7. Test on a real iPhone (Safari) and Android phone (Chrome).
8. Check images: right sizes downloaded, no layout shift, sharp on high DPR screens.
9. Check forms with the on-screen keyboard open.
10. Run Lighthouse in mobile mode and check dark mode and reduced motion.

## 299: What is the difference between CSS transforms and layout properties for responsive animations?

Animating `width`, `height`, `top`, `left` or `margin` makes the browser recalculate layout on every frame, which is slow on phones. `transform` and `opacity` can usually be handled by the compositor without new layout, so they stay smooth.

```css
/* Slow: layout on every frame */
.drawer {
  transition: left 0.3s;
}

/* Smooth */
.drawer {
  transform: translateX(-100%);
  transition: transform 0.3s;
}

.drawer.open {
  transform: none;
}
```

For responsive menus and drawers, slide them with `transform`.

## 300: What are common responsive design mistakes?

- Leaving out the viewport meta tag, or disabling zoom.
- Fixed widths and heights in pixels.
- Breakpoints for specific devices instead of content.
- Images without `max-width`, `srcset` or `width`/`height` attributes.
- Hover-only menus and tooltips.
- Tiny touch targets and text under 16px.
- Using `100vh` for full-screen sections on mobile.
- Hiding important content on mobile.
- Font sizes in `vw` only.
- Testing only in DevTools and never on a real phone.

---

# Advanced Questions (301-450)

## 301: Why does the sizes attribute have to be in the HTML instead of coming from CSS?

Browsers start downloading images very early, before the CSS is loaded and before layout runs. A part of the browser called the preload scanner reads the raw HTML ahead of the main parser and starts image requests right away.

At that moment the browser doesn't know how wide the image will be in the layout. `sizes` gives it that information up front, so it can pick the right file from `srcset` without waiting. If it waited for CSS and layout, images would start loading much later and the page would feel slower.

The exception is `sizes="auto"` on lazy images. Lazy images wait for layout anyway, so the browser can use the real width.

## 302: Why might a browser download a larger srcset candidate than you expect?

- **The DPR is higher than you think.** A 400px slot on a 3x phone needs 1200 pixels.
- **`sizes` is missing or wrong.** Without `sizes`, the browser assumes `100vw`.
- **A larger file is already in the cache.** Browsers can reuse a bigger cached file instead of downloading a smaller one.
- **The browser rounds up.** It picks the nearest candidate that's large enough, and if the steps between widths are big, the next one up can be much bigger.
- **Desktop zoom** increases the DPR, so a zoomed-in page asks for bigger images.

Check `img.currentSrc` in the console to see which file was picked, and compare it with the rendered size and DPR.

## 303: What happens with srcset when the viewport changes after the page loads?

Browsers can choose again when the viewport or DPR changes, but they don't have to download a new file. In practice:

- If the new situation needs a **bigger** image, browsers usually fetch it.
- If it needs a **smaller** one, browsers usually keep the bigger image they already have, since it still looks fine.

So resizing a desktop window from narrow to wide may trigger new downloads, but going back won't. Don't rely on `srcset` to switch images for different designs. That's what `<picture>` with `media` is for.

## 304: Does picture re-evaluate its sources when the viewport changes?

Yes. `media` conditions on `<source>` are rules, not hints. When the viewport changes so a different `<source>` matches, the browser switches to that source and loads its image. This happens when rotating a phone or resizing a window across a breakpoint.

`type` doesn't change during a session, so format switching is decided once. Within the chosen `<source>`, `srcset` with `w` descriptors still works as a hint, as described in the previous answer.

## 305: How do you preload an art-directed LCP image without downloading two files?

Add a preload for each `<source>`, with `media` conditions that match exactly and don't overlap.

```html
<link
  rel="preload"
  as="image"
  href="hero-wide.avif"
  type="image/avif"
  media="(width >= 800px)"
  fetchpriority="high"
/>
<link
  rel="preload"
  as="image"
  href="hero-narrow.avif"
  type="image/avif"
  media="(width < 800px)"
  fetchpriority="high"
/>

<picture>
  <source media="(width >= 800px)" srcset="hero-wide.avif" type="image/avif" />
  <source srcset="hero-narrow.avif" type="image/avif" />
  <img src="hero-narrow.jpg" alt="..." width="800" height="1000" />
</picture>
```

If the `media` values don't match the `<picture>` exactly, a device can preload one file and then use another, so it downloads both. Note that a browser without AVIF support would ignore the `type` preload and load the JPEG fallback normally. Usually you don't need this at all, since an `<img>` in the HTML is already found early by the preload scanner. It's mainly for images that are found late.

## 306: How do you check whether your images are oversized?

- **In the console**, compare the downloaded size with the displayed size:

```js
for (const img of document.images) {
  const needed = img.clientWidth * devicePixelRatio;
  if (img.naturalWidth > needed * 1.5) {
    console.log(img.currentSrc, img.naturalWidth, "needed", Math.round(needed));
  }
}
```

- **Lighthouse** has a "Properly size images" audit.
- **DevTools** shows the rendered size and the intrinsic size when you hover over an image in the Elements panel.
- **The Network panel** filtered by images, with mobile emulation, shows total image weight per page.

Do this at several viewport widths, because `sizes` can be right at one width and wrong at another.

## 307: Should you serve 3x images to 3x screens?

Often not. Studies and testing by teams like Twitter found that most people can't see the difference between 2x and 3x images on a phone, but a 3x image has about 2.25 times the pixels of a 2x one. That's a lot of extra data for almost no visible gain.

With `w` descriptors you can't tell the browser to cap the DPR directly, but you can limit the largest file in `srcset`, or write `sizes` values a bit smaller. Image CDNs can also cap DPR on the server. Logos, icons and text in images are the exception: use SVG for those so they're sharp at any DPR.

## 308: How does serving image formats based on the Accept header affect caching?

Instead of using `<picture>` with `type`, an image CDN can look at the request's `Accept` header (for example `image/avif,image/webp,*/*`) and return AVIF, WebP or JPEG from the same URL.

The same URL now has several different responses, so the server must send `Vary: Accept`. Otherwise a cache (CDN or browser) might store the AVIF version and serve it to a browser that can't display it.

`Vary: Accept` can lower the cache hit rate, because `Accept` strings differ between browsers and versions. Good CDNs normalize the header into a few groups (AVIF, WebP, other) before using it as a cache key.

## 309: How do Client Hints work with a third-party image CDN?

By default, browsers only send Client Hints to the same origin that asked for them. To send them to an image CDN on another domain, you delegate them with a Permissions Policy.

```http
Accept-CH: Sec-CH-DPR, Sec-CH-Viewport-Width
Permissions-Policy: ch-dpr=("https://images.example-cdn.com"), ch-viewport-width=("https://images.example-cdn.com")
```

Or in HTML:

```html
<meta
  http-equiv="delegate-ch"
  content="sec-ch-dpr https://images.example-cdn.com; sec-ch-viewport-width https://images.example-cdn.com"
/>
```

Hints are only sent after the browser has seen `Accept-CH`, so the very first request doesn't have them. The `Critical-CH` header can make the browser retry the first request with the hints. Since only Chromium supports Client Hints, they work on top of `srcset`, not instead of it.

## 310: What are low-quality image placeholders and how do they fit into responsive layouts?

A low-quality image placeholder (LQIP) is a tiny, blurry version of an image, or just its main color, shown while the real image loads. It makes the page feel faster and avoids a blank box.

```html
<img
  src="photo-800.jpg"
  srcset="photo-400.jpg 400w, photo-800.jpg 800w, photo-1600.jpg 1600w"
  sizes="(width >= 900px) 50vw, 100vw"
  width="1600"
  height="1067"
  loading="lazy"
  alt="..."
  style="background: #8a9a7b url('data:image/webp;base64,UklGR...') center / cover"
/>
```

The `width` and `height` attributes keep the box at the right ratio at every size, and the background shows inside it until the real file loads. Keep placeholders very small (a few hundred bytes), or they slow down the HTML. Libraries like BlurHash and ThumbHash encode placeholders as short strings.

## 311: How do container queries work under the hood?

When you set `container-type: inline-size`, the browser applies containment to the element: `inline-size` containment, `layout` containment and `style` containment. Size containment means the element's inline size is calculated as if it had no children.

That's what makes container queries possible without loops. The browser can lay out the container first and know its width without looking inside. Then it evaluates the `@container` rules for its descendants with that width and lays out the children.

During layout, the browser may have to style and lay out parts of the tree more than once (lay out the container, then restyle the descendants based on its size), but containment keeps that work limited to the container's subtree.

## 312: Why does container-type: size often collapse the element's height?

`size` containment applies in both directions. The element's height is calculated as if it had no content, so unless the height comes from somewhere else, it becomes 0. The content then overflows or seems to vanish.

```css
/* Collapses to 0 height */
.panel {
  container-type: size;
}

/* Works: height comes from outside */
.panel {
  container-type: size;
  height: 400px; /* or a grid track, a flex basis, or 100svh */
}
```

Use `size` only when the element's height is set by its parent layout, like a full-height panel in an app shell. For most components, `inline-size` is the right choice.

## 313: How are nested containers resolved, and how do you avoid surprises?

An unnamed `@container` rule looks for the nearest ancestor that is a container of the right type. If you nest containers (a card container inside a column container inside a page container), each unnamed query uses the closest one.

That's usually what you want, but it can surprise you when someone later adds a new container between the element and the one you meant to query. Your query starts reacting to the new, narrower container.

To avoid this:

- Name containers that act as layout regions (`main`, `sidebar`) and query them by name when you mean them.
- Keep unnamed queries for "my own component wrapper".
- Remember that container units like `cqi` also use the nearest container on the right axis, not a named one.

## 314: Do container queries have a performance cost?

They're designed to be fast, and in normal use the cost is small. Some things to know:

- Containment can make layout cheaper, because changes inside a container don't affect outside it.
- When a container's size changes, the browser has to restyle its descendants and lay them out again. With many containers resizing at once, like during a window resize, that's more work than a few media queries.
- Very deep nesting of containers that all react to each other can add up.

In practice, measure with the Performance panel if you have hundreds of containers on a page. For normal component counts, you won't notice it.

## 315: What do container query units refer to when used on the container element itself?

They refer to the container's own nearest container ancestor, not to the element itself. An element can't query its own size, and that rule applies to units too.

```css
.card {
  container-type: inline-size;
  padding: 3cqi; /* 3% of the PARENT container's width, or small viewport if none */
}

.card h2 {
  font-size: 5cqi; /* 5% of .card's width */
}
```

So if you want padding relative to the card's own width, put it on a child, or make a wrapper element the container.

## 316: How can you combine container queries and :has() to style a parent based on its size?

A container can't style itself based on its own size. But you can query the container from a child, and then use `:has()` on an outer element to react to that child's state.

A common pattern is to give the component an outer wrapper as the container and style the inner element instead:

```css
.card-shell {
  container-type: inline-size;
}

@container (width >= 500px) {
  .card {
    display: grid;
    grid-template-columns: 200px 1fr;
    border-left: 4px solid var(--accent);
  }
}
```

For styling based on content, use `:has()` directly:

```css
.card-shell:has(.card video) {
  container-type: inline-size;
  grid-column: span 2; /* video cards get more room in the parent grid */
}
```

Be careful not to create loops where the result of a query changes the size that the query depends on. Containment prevents most, but not all, of these mistakes.

## 317: What are scroll-state container queries?

They let you style elements based on the scroll state of a container, without JavaScript.

```css
.site-header {
  container-type: scroll-state;
  position: sticky;
  top: 0;
}

@container scroll-state(stuck: top) {
  .site-header-inner {
    box-shadow: 0 2px 8px rgb(0 0 0 / 0.15);
  }
}

.carousel {
  container-type: scroll-state;
  overflow-x: auto;
}

@container scroll-state(scrollable: right) {
  .scroll-hint {
    opacity: 1;
  }
}
```

States include `stuck` (for sticky elements), `snapped` (for scroll snap targets) and `scrollable` (whether there's more content to scroll to). They're only in Chromium browsers so far, so use them as an improvement.

## 318: What is CSS anchor positioning and why does it help in responsive UIs?

Anchor positioning lets you place an element relative to another element (the anchor) anywhere on the page, in pure CSS. It's built for tooltips, dropdowns and popovers.

```css
.trigger {
  anchor-name: --menu-btn;
}

.menu {
  position: absolute;
  position-anchor: --menu-btn;
  position-area: bottom span-right;
  position-try-fallbacks: flip-block, flip-inline;
}
```

The responsive part is `position-try-fallbacks`. If the menu doesn't fit below the button (for example near the bottom of a small screen), the browser tries the flipped positions automatically. Before this, you needed a JavaScript library like Floating UI to measure and reposition. It works in Chromium and Safari 26, and Firefox has been adding it, so keep a simple fallback position.

## 319: How do you make a tooltip that stays on screen on any device size?

Combine anchor positioning, fallbacks and a size limit, and don't make it hover-only.

```css
.tooltip {
  position: absolute;
  position-anchor: --info;
  position-area: top;
  position-try-fallbacks: bottom, left, right;
  max-width: min(280px, 100vw - 2rem);
  margin: 0.5rem;
}
```

```html
<button style="anchor-name: --info" popovertarget="tip" aria-describedby="tip">
  ?
</button>
<div id="tip" class="tooltip" popover="hint">
  Your password must be at least 12 characters.
</div>
```

The `max-width` keeps it inside narrow screens, the fallbacks flip it when there's no room, and using a button means it works with tap and keyboard. On very small screens, it can be easier to show the text inline below the field instead of in a tooltip.

## 320: What is the CSS if() function?

`if()` lets you pick a value inside a declaration based on a condition, including media queries, feature support and style queries.

```css
.button {
  padding: if(media(pointer: coarse): 0.875rem 1.25rem; else: 0.5rem 1rem);
}

.card {
  background: if(style(--variant: dark): #111; else: white);
}
```

It saves writing a separate `@media` block just to change one value. It's only in Chromium browsers so far, so it's not ready to use without a fallback. Browsers that don't support it drop the whole declaration, so write the normal value first.

## 321: How do you decide where a responsive change belongs: media query, container query or intrinsic layout?

A rough order of preference:

1. **Intrinsic layout first.** Can Flexbox wrapping, `auto-fit` with `minmax()`, or `clamp()` handle it with no breakpoint at all? Then do that.
2. **Container query** if the change depends on the space a component gets, and the component might be used in different places.
3. **Media query** if the change depends on the whole viewport or the user: page layout, navigation pattern, input type, user preferences.

Mixing them on one element is fine, but avoid two systems fighting over the same property. For example, don't change a card's columns in both a media query and a container query. Pick one owner for each property.

## 322: What does the contain property do and how does it help performance?

`contain` tells the browser that an element is independent from the rest of the page in certain ways, so it can skip work.

- `layout` - nothing inside affects layout outside, and the other way around.
- `paint` - nothing inside is painted outside the element's box.
- `size` - the element's size doesn't depend on its children.
- `inline-size` - the same, but only for the inline size.
- `style` - counters and quotes don't leak out.
- `content` - shorthand for `layout paint style`.
- `strict` - shorthand for `size layout paint style`.

```css
.widget {
  contain: content;
}
```

On complex pages, like dashboards with many widgets, containment means a change inside one widget doesn't make the browser recalculate the layout of the whole page.

## 323: What does content-visibility: auto do?

`content-visibility: auto` lets the browser skip rendering (style, layout and paint) for elements that are off screen, until the user scrolls near them.

```css
.article-section {
  content-visibility: auto;
  contain-intrinsic-size: auto 800px;
}
```

`contain-intrinsic-size` gives the browser a placeholder size to use while the content is skipped, so the scrollbar doesn't jump. With `auto`, the browser remembers the real size after the element has been rendered once.

It can speed up initial rendering of long pages a lot, especially on slow phones. The downsides are that find-in-page and anchor links still work, but measurements from JS on skipped content can be wrong.

## 324: What is layout thrashing and how does it relate to responsive JavaScript?

Layout thrashing happens when code reads a layout value (like `offsetWidth`), changes the DOM, reads again, changes again, and so on. Each read after a change forces the browser to recalculate layout immediately.

```js
// Bad: forces layout on every loop
for (const card of cards) {
  card.style.height = `${card.offsetWidth * 0.75}px`;
}

// Better: read everything first, then write
const widths = cards.map((card) => card.offsetWidth);
cards.forEach((card, i) => {
  card.style.height = `${widths[i] * 0.75}px`;
});
```

Responsive JavaScript that runs on `resize` often does this. Better yet, use CSS (`aspect-ratio` here) or `ResizeObserver`, which gives you sizes after layout without forcing an extra one.

## 325: Do many media queries slow down a page?

Not in a way you'll notice. Browsers evaluate media query conditions very quickly, and only re-check them when something relevant changes, like the viewport size or a user preference. When a query changes from false to true, the browser restyles the affected elements, which is the same work any style change causes.

The bigger costs are elsewhere: large CSS files to download and parse, very complex selectors, and JavaScript running on resize. Organizing media queries for readability matters more than counting them.

## 326: Why can dvh hurt performance or cause content jumps?

`dvh` changes value every time the mobile toolbar shows or hides, which happens while the user is scrolling. Every change means elements sized with `dvh` must be laid out again, and anything below them can move.

So a long page with sections sized at `100dvh` can jitter while scrolling on a phone. Use `svh` for layout sizing in normal scrolling pages, and keep `dvh` for elements that must always match the visible area, like a fixed full-screen overlay or app shell where nothing scrolls inside the document.

## 327: How do web fonts cause layout shift and how do you reduce it?

When a web font loads and replaces the fallback font, the text often changes width and height because the two fonts have different metrics. Lines rewrap, and everything below moves. On narrow screens with more wrapping, the shift is often worse.

Fixes:

- Adjust the fallback font to match the web font's metrics:

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

- Use `font-display: optional` so the font is only used if it loads very fast.
- Preload the main font.

Tools like Fontaine and Next.js `next/font` calculate these override values for you.

## 328: How do you make sure fluid type with clamp() still passes WCAG Resize Text?

The test is: at 200% zoom, text should be twice as big as at 100%. When you zoom, `rem` doubles, but the viewport halves in CSS pixels, so the `vw` part of the formula shrinks.

A rule of thumb from accessibility research (Maxwell Barvian's work on this is a good reference): if the maximum font size is at most 2.5 times the minimum, a `clamp()` with a `rem + vw` preferred value will pass at all widths. Bigger ratios can fail at some viewport widths.

```css
/* Ratio 2.5: safe */
h1 {
  font-size: clamp(1.6rem, 1rem + 3vw, 4rem);
}
```

Also check by hand: set a 1280px window, zoom to 200%, and compare the text size with 100%.

## 329: Do container query units have the same zoom problem as vw?

Yes. When the user zooms, the viewport in CSS pixels shrinks, so containers usually shrink too. Text sized only in `cqi` stays about the same visual size, which can fail WCAG Resize Text, just like `vw`.

The fix is the same: always add a `rem` part.

```css
.card-title {
  font-size: clamp(1rem, 0.75rem + 3cqi, 1.75rem);
}
```

Keep the max-to-min ratio modest and test with zoom.

## 330: How do you support foldable devices?

Foldables can be used flat as one big screen, folded like a book, or half-open like a laptop. Most of the time, a normal responsive layout works fine, because the browser reports a regular viewport.

For layouts that use the fold, there are viewport segment media features:

```css
/* Two side-by-side segments (book mode) */
@media (horizontal-viewport-segments: 2) {
  .app {
    display: grid;
    grid-template-columns:
      env(viewport-segment-width 0 0)
      calc(env(viewport-segment-left 1 0) - env(viewport-segment-right 0 0))
      1fr;
  }
}

/* Top and bottom segments (laptop mode) */
@media (vertical-viewport-segments: 2) {
  .video-call {
    grid-template-rows: 1fr 1fr;
  }
}
```

The `env(viewport-segment-*)` variables give you the size and position of each segment, so content doesn't land on the hinge. These features are in Chromium browsers. Use them only as an extra on top of a normal layout.

## 331: What does the VirtualKeyboard API do?

It lets a page take control of how the on-screen keyboard affects layout. When you set `overlaysContent` to true, the browser stops resizing the viewport for the keyboard, and gives you the keyboard's position so you can lay out around it.

```js
if ("virtualKeyboard" in navigator) {
  navigator.virtualKeyboard.overlaysContent = true;
}
```

```css
.chat-input {
  position: fixed;
  bottom: env(keyboard-inset-height, 0px);
  inset-inline: 0;
}
```

The `keyboard-inset-*` environment variables and the `geometrychange` event tell you the keyboard size. It's only in Chromium browsers on Android and ChromeOS, so on iOS you still rely on `visualViewport`.

## 332: Why do fixed elements behave strangely with the keyboard on iOS Safari?

On iOS Safari, opening the keyboard doesn't resize the layout viewport. Instead, the visual viewport shrinks and the page can be scrolled behind the keyboard. Elements with `position: fixed; bottom: 0` stay fixed to the layout viewport, so they end up hidden behind the keyboard or float in odd places while the user scrolls.

Common workarounds:

- Avoid fixed bottom bars on screens with text inputs, or hide them while an input has focus.
- Use the `visualViewport` API to move the bar to the top of the keyboard:

```js
const bar = document.querySelector(".bottom-bar");

function place() {
  const vv = window.visualViewport;
  const offset = window.innerHeight - vv.height - vv.offsetTop;
  bar.style.transform = `translateY(${-offset}px)`;
}

visualViewport.addEventListener("resize", place);
visualViewport.addEventListener("scroll", place);
```

Test on real devices, because this behavior has changed between iOS versions.

## 333: What is rubber-band scrolling and how does it affect fixed and sticky elements?

On iOS (and macOS with a trackpad), scrolling past the top or bottom of the page stretches it and then bounces back. During the bounce, the page can show the background behind it, and fixed headers or backgrounds may look detached.

Fixes depend on what looks wrong:

- Set a `background-color` on `html` that matches the header or footer, so the bounce area doesn't flash white.
- Use `overscroll-behavior: none` on the root to turn off the bounce where it's supported, mostly for app-like pages.
- Use `overscroll-behavior: contain` on inner scroll areas, so they don't drag the whole page.

Removing the bounce makes a site feel less native on iOS, so only do it in web apps where it really causes problems.

## 334: How can subgrid help line up form fields inside nested components?

When each field is a separate component (label, input, help text), the labels in a two-column form usually have different widths, and the inputs don't line up. Subgrid lets each field component use the form's columns.

```css
.form {
  display: grid;
  grid-template-columns: max-content 1fr;
  gap: 1rem 1.5rem;
}

.field {
  grid-column: 1 / -1;
  display: grid;
  grid-template-columns: subgrid;
}

.field label {
  grid-column: 1;
}

.field .control {
  grid-column: 2;
}

@media (width < 600px) {
  .form {
    grid-template-columns: 1fr;
  }

  .field label,
  .field .control {
    grid-column: 1;
  }
}
```

The label column is as wide as the longest label across all fields, and on small screens everything stacks.

## 335: How does the browser size fr tracks when content is wider than the track?

The browser first gives each `fr` track its minimum size. For `1fr` the minimum is `auto`, which for most items means the min-content width of the content. Then it shares out the remaining free space based on the `fr` values.

If one item's min-content width (a long word, an image, a table) is bigger than its fair share, that track grows to fit it, and the other `fr` tracks get less. If the total min-content of all tracks is bigger than the container, the grid overflows.

That's why `1fr 1fr` columns can end up unequal, and why `minmax(0, 1fr)` is the fix when you need them equal regardless of content.

## 336: Why does height: 100% often not work, and what are better options?

A percentage height needs the parent to have a definite height. If the parent's height is `auto` (the normal case, where it comes from its content), the percentage can't be calculated and acts like `auto`. That's why `height: 100%` on a child of a normal `<div>` does nothing, and why old code sets `height: 100%` on `html`, `body` and every wrapper in between.

Better options:

- Make the parent a grid or flex container, where children stretch to fill by default.
- Use viewport units for the outer shell (`min-height: 100svh`).
- Use `flex: 1` on the child in a flex column.

```css
.app {
  min-height: 100svh;
  display: flex;
  flex-direction: column;
}

.app main {
  flex: 1;
}
```

Grid and flex items with a stretched size count as definite, so percentages inside them do work.

## 337: What happens when aspect-ratio conflicts with content or min-height?

`aspect-ratio` is a preferred ratio, not a hard rule.

- If the content is taller than the ratio allows, the box grows to fit it, because the automatic minimum height (`min-height: auto`) wins. The ratio is broken but nothing is cut off.
- If you set `min-height: 0` or `overflow` to something other than `visible`, the box keeps the ratio and the content overflows or scrolls.
- If you set both `width` and `height`, `aspect-ratio` is ignored.

```css
/* Keeps the ratio strictly, clips extra content */
.tile {
  aspect-ratio: 1;
  overflow: hidden;
}
```

On narrow screens, text inside fixed-ratio boxes often doesn't fit. Decide whether the box should grow (default) or the text should be clamped.

## 338: What is the automatic minimum size of flex and grid items?

Flex and grid items have `min-width: auto` (and `min-height: auto` in the block direction for flex columns) by default. For these items, `auto` doesn't mean 0. It means "don't shrink below the content's minimum size". This is called the automatic minimum size.

It only applies when the item's `overflow` is `visible`. Setting `overflow: hidden` or `overflow: auto` on the item turns it off, which is why that also fixes overflowing flex items.

```css
.item {
  min-width: 0; /* option 1 */
}

.item {
  overflow: hidden; /* option 2, also clips content */
}
```

Understanding this rule explains most "my flex/grid layout is wider than the screen" bugs.

## 339: What is the difference between flex-basis: 0 and flex-basis: auto when growing?

With `flex-basis: auto`, each item starts at its content size (or its `width`), and only the **leftover** space is shared by `flex-grow`. Items with more content stay wider.

With `flex-basis: 0`, every item starts at zero and **all** the space is shared by `flex-grow`. With equal grow values, items end up equal width, unless content forces them wider through the automatic minimum size.

```css
/* Widths follow content */
.tabs--auto > * {
  flex: 1 1 auto;
}

/* Equal widths */
.tabs--equal > * {
  flex: 1 1 0;
}
```

For equal columns in a flexible row, use `flex: 1` (basis 0) plus `min-width: 0` so long content doesn't push one item wider.

## 340: Why can percentage gaps or padding cause overflow in grids?

Percentage gaps in Grid are resolved against the container's size. Percentage padding and margins are always resolved against the containing block's width. When you combine percentages with `fr` tracks or fixed columns, it's easy to end up with a total over 100%.

```css
/* 4 columns of 25% plus 3 gaps of 2% = 106%, overflows */
.grid {
  display: grid;
  grid-template-columns: repeat(4, 25%);
  gap: 2%;
}

/* fr is calculated after gaps, so it always fits */
.grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2%;
}
```

Use `fr` for tracks so gaps are subtracted first.

## 341: Why do fluid layouts sometimes show 1px gaps or misaligned edges?

Fluid widths produce fractional pixel values, like a column 333.333px wide. Browsers have to round these to device pixels when painting, and different browsers round differently. The result can be a 1px gap between items, a hairline at an edge, or columns that are one pixel off from each other.

Ways to reduce it:

- Use Grid with `fr` and `gap` instead of percentages and floats, so the browser distributes the rounding.
- Don't stack exactly aligned backgrounds or borders from separate elements. Use one element's border or `gap` with a background on the container.
- Avoid `transform: translate()` with fractional values on text, which can blur it.

## 342: Can media query ranges overlap or leave gaps?

With `min-width` and `max-width`, yes. Both values are included, so `(max-width: 768px)` and `(min-width: 768px)` both match at exactly 768px. People avoid that by using `max-width: 767px`, but then a viewport of 767.5px (possible with zoom or fractional DPR) matches neither query.

The range syntax fixes both problems because you can use strict and non-strict comparisons:

```css
@media (width < 768px) {
  /* mobile */
}

@media (width >= 768px) {
  /* tablet and up */
}
```

Every width matches exactly one of these. Bootstrap's old workaround was `max-width: 767.98px`.

## 343: How does browser zoom affect media queries and devicePixelRatio?

When you zoom a desktop page to 200%:

- CSS pixels become twice as big, so the viewport width in CSS pixels halves. A 1280px window becomes a 640px viewport, and mobile media queries apply.
- `devicePixelRatio` doubles (from 1 to 2, or 2 to 4), so `srcset` may pick bigger images.
- `resize` and `matchMedia` change events fire.

Pinch zoom on mobile is different. It only zooms the visual viewport, like a magnifying glass. The layout viewport, media queries and DPR stay the same.

This is why a good responsive design is also good for people who zoom: their zoomed desktop gets the same layout as a phone.

## 344: What does the CSS zoom property do?

`zoom` scales an element and its content, and unlike `transform: scale()`, it affects layout: the element takes up the scaled amount of space.

```css
.preview {
  zoom: 0.5; /* half size, and takes half the space */
}
```

It was a non-standard IE and WebKit feature for a long time. It's now in a CSS spec and works in all major browsers, including Firefox since 2024. It's useful for scaled previews of content. Don't use it to make a whole site "fit" on small screens. That's what responsive layout is for, and it can break things like `getBoundingClientRect()` results in older code.

## 345: How do you define a breakpoint strategy for a design system?

- **Few global breakpoints** (3-5) used for page layout, defined as tokens. Name them by size (`sm`, `md`, `lg`).
- **Components use container queries** for their own layout, with breakpoints chosen per component based on their content.
- **Fluid tokens** for type and spacing with `clamp()`, so most sizes don't need breakpoints.
- **One source of truth** for breakpoint values, exported to CSS, Sass and JS.
- **Documentation** that shows each component at several container widths, for example in Storybook.

The goal is that a product team can build a page by placing components into a page grid, and everything adapts without them writing new media queries.

## 346: What are responsive props in component libraries and what are the trade-offs?

Some libraries let you pass different values per breakpoint as props:

```jsx
<Grid columns={{ base: 1, md: 2, lg: 4 }} gap={{ base: 2, md: 4 }}>
  ...
</Grid>
```

The library turns this into media queries, usually by generating classes or CSS variables.

Pros: easy to read in the component code, and consistent breakpoints.

Cons:

- If it's done with runtime CSS-in-JS, it costs JavaScript work on render.
- If it's done with `matchMedia` in JS, it causes a layout jump on hydration.
- It ties layouts to viewport breakpoints, not container size.

Good implementations generate static CSS at build time or map props to CSS variables, so there's no JS cost and the first render is correct.

## 347: How should a server-rendered app handle responsive layouts?

The server doesn't know the screen size, so the safe default is: render the same HTML for everyone and let CSS handle the layout. Then the first paint is already correct on every device, with no layout jump after hydration.

Avoid rendering different components based on `window.innerWidth`, because the server render and the first client render won't match.

If the server really needs to change the markup (for example to skip a heavy desktop-only component on phones), use Client Hints like `Sec-CH-Viewport-Width` or `Sec-CH-UA-Mobile`, accept that they only work in Chromium, add the right `Vary` header, and still make the CSS handle any mismatch.

## 348: How do you avoid hydration mismatches caused by window size?

Hydration mismatches happen when the server renders one thing and the client's first render produces something else, for example because a component checks `window.innerWidth`.

Options:

1. **Use CSS** to show or hide the variant. Render both and hide one with a media query. This is the simplest and avoids JS completely.
2. **Render the server version first**, then update after hydration (in React, read the media query in an effect or with `useSyncExternalStore` and a server snapshot). There will be a short switch, so keep the server version the most common one.
3. **Render a placeholder** for the JS-only part until mounted, with reserved space so nothing shifts.

```jsx
function Layout() {
  return (
    <>
      <MobileNav className="md:hidden" />
      <DesktopNav className="hidden md:flex" />
    </>
  );
}
```

Rendering both costs a bit more HTML, so it's best for small components.

## 349: Why is serving different HTML based on the User-Agent bad for caching?

If the server returns different HTML for phones and desktops based on the `User-Agent` header, it must send `Vary: User-Agent`. User agent strings are almost unique per browser version and device, so CDNs end up caching a separate copy for almost every visitor, which kills the cache hit rate.

Workarounds include normalizing the user agent into a small set of groups at the CDN edge (mobile, tablet, desktop) and using that as the cache key. But the cleaner answer is to serve the same HTML and let CSS do the work. If you must vary, Client Hints like `Sec-CH-UA-Mobile` (a simple `?0` or `?1`) are much more cache-friendly.

## 350: What is the cost of runtime CSS-in-JS for responsive styles?

Runtime CSS-in-JS libraries generate CSS in the browser while components render. For responsive styles, this means:

- The styles, including media queries, are computed and injected with JavaScript on each render, which takes CPU time on slow phones.
- With SSR, the styles must be collected on the server and sent with the HTML, or the first paint is unstyled.
- Some patterns read the window size in JS to pick styles, which causes hydration mismatches and layout jumps.

That's why many projects have moved to zero-runtime options: CSS Modules, Tailwind, vanilla-extract, Panda CSS or plain CSS with nesting. Media queries in static CSS are free at runtime.

## 351: What is critical CSS and how does it relate to mobile performance?

Critical CSS is the small set of styles needed to render the part of the page visible on first load. You inline it in a `<style>` tag in the `<head>` and load the rest of the CSS without blocking rendering.

```html
<head>
  <style>
    /* header, hero and base layout styles */
  </style>
  <link
    rel="preload"
    href="/styles.css"
    as="style"
    onload="this.onload=null;this.rel='stylesheet'"
  />
  <noscript><link rel="stylesheet" href="/styles.css" /></noscript>
</head>
```

On slow mobile networks, every round trip for a render-blocking stylesheet delays the first paint. The tricky part is that "above the fold" is different on a phone and a desktop, so critical CSS should include the mobile-first base styles plus what's needed for common desktop sizes. Tools like Critical or Beasties can extract it. For small sites, a single small CSS file is often fine.

## 352: Does splitting CSS with the media attribute on link tags improve performance?

Partly. A stylesheet with a non-matching `media` attribute is still downloaded, but at low priority, and it doesn't block rendering.

```html
<link rel="stylesheet" href="base.css" />
<link rel="stylesheet" href="desktop.css" media="(width >= 1024px)" />
<link rel="stylesheet" href="print.css" media="print" />
```

So on a phone, `desktop.css` won't delay the first paint. But it's still downloaded, it's an extra request, and if the user rotates or resizes past the breakpoint, the browser applies it. For most sites, the gain is small compared with keeping CSS small overall. Splitting out `print.css` is the clearest win.

## 353: What should you think about when building for low-end phones?

Low-end Android phones are very common worldwide. They have slow CPUs, little memory, and are often on slow networks. Things that are fine on a laptop can be slow there:

- **JavaScript** is the biggest cost. Parsing and running a large bundle can take seconds. Ship less, split code and defer non-critical scripts.
- **Long main thread tasks** make taps feel slow (bad INP).
- **Large images** use memory when decoded, not just bandwidth.
- **Complex layouts and effects** like big `backdrop-filter` blurs, many shadows or huge DOMs slow down scrolling.

Test on a real mid-range device or with CPU throttling (4x to 6x slowdown) in DevTools, and set budgets for JS size and LCP on mobile.

## 354: How do you get a good LCP on mobile for a page with a responsive hero image?

1. Use an `<img>` in the HTML, not a CSS background, so the preload scanner finds it right away.
2. Don't lazy load it. Add `fetchpriority="high"`.
3. Give it a correct `srcset` and `sizes`, so phones download a small file.
4. Use AVIF or WebP.
5. Keep the server response fast (TTFB) and avoid redirects.
6. Don't render the hero with client-side JavaScript. Server-render it.
7. Avoid render-blocking CSS and fonts in front of it.
8. If the hero is a text block on mobile and an image on desktop, LCP might be the text on mobile. Make sure the font doesn't delay it.

Then measure with real user data split by device, because lab tests on one device can hide problems.

## 355: How can a responsive layout cause CLS after the page loads?

Layout shifts happen when something changes size or position after it's been shown. Responsive causes include:

- Images without `width`/`height` or `aspect-ratio`.
- JavaScript that picks the layout after hydration (for example rendering the mobile nav first, then switching to desktop).
- Fonts that load late and rewrap text.
- Ads, embeds and banners without reserved space, which often have different sizes per breakpoint.
- Content that changes when a container query or media query is evaluated late, for example because a stylesheet loaded late.

```css
.cookie-banner {
  position: fixed; /* overlays instead of pushing content */
  inset-inline: 0;
  bottom: 0;
}
```

Use the DevTools Performance panel's layout shift track, or the web-vitals library's attribution build, to find which element moved.

## 356: How can a responsive menu hurt INP and how do you fix it?

INP (Interaction to Next Paint) measures how long it takes from a tap or click until the next frame is shown. A mobile menu toggle can be slow if the click handler does a lot of work: rendering a big menu component, measuring layout, or loading data.

Fixes:

- Keep the menu HTML in the page and toggle it with an attribute and CSS, instead of rendering it on click.
- Use `popover` or `<dialog>`, which need very little JS.
- Split heavy work out of the event handler. Update the UI first, then do other work after the next frame:

```js
toggle.addEventListener("click", () => {
  menu.togglePopover();
  requestAnimationFrame(() => {
    setTimeout(() => trackMenuOpen(), 0); // analytics after the paint
  });
});
```

- Avoid large CSS animations of layout properties on open.

## 357: How do you make scroll-driven animations work well across screen sizes?

Scroll-driven animations link an animation to scroll position with `animation-timeline: scroll()` or `view()`, no JavaScript needed.

```css
@media (prefers-reduced-motion: no-preference) {
  .reveal {
    animation: fade-in linear both;
    animation-timeline: view();
    animation-range: entry 0% entry 60%;
  }
}

@keyframes fade-in {
  from {
    opacity: 0;
    translate: 0 2rem;
  }
}
```

Things to watch:

- Distances in `px` feel very different on a phone and a large monitor. Use relative units or `view()` ranges, which adapt to the viewport.
- Animate only `transform` and `opacity` to keep scrolling smooth on phones.
- Respect reduced motion.
- They work in Chromium and Safari 26. Firefox support has been in progress, so the content must look right without the animation.

## 358: How do view transitions help when a layout changes between views?

The View Transitions API animates between two states of the page, for example switching a product list from grid to list view, or moving between pages.

```js
function setView(view) {
  if (!document.startViewTransition) {
    list.dataset.view = view;
    return;
  }
  document.startViewTransition(() => {
    list.dataset.view = view;
  });
}
```

```css
.product {
  view-transition-name: match-element;
}

@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(*) {
    animation: none;
  }
}
```

The browser takes a snapshot before and after, and animates each named element from its old position and size to the new one. Same-document transitions work in all modern browsers. `match-element` gives each element a unique name automatically, but check support since it's newer. Cross-document transitions (`@view-transition { navigation: auto; }`) work in Chromium and Safari.

## 359: How do you respect reduced motion in JavaScript animations?

Check the media query before starting the animation, and listen for changes in case the user changes the setting.

```js
const reduce = window.matchMedia("(prefers-reduced-motion: reduce)");

function animateCard(el) {
  if (reduce.matches) {
    el.style.opacity = 1;
    return;
  }
  el.animate(
    [
      { opacity: 0, transform: "translateY(20px)" },
      { opacity: 1, transform: "none" },
    ],
    { duration: 300, easing: "ease-out", fill: "both" },
  );
}
```

Reduced motion doesn't mean no change at all. A short fade is usually fine. What you remove is large movement: parallax, zooming, sliding across the screen and auto-playing carousels. Also pass the setting to animation libraries, most of which have an option for it.

## 360: What is the WCAG Focus Not Obscured criterion and how do sticky elements affect it?

WCAG 2.4.11 Focus Not Obscured (Minimum, level AA, added in WCAG 2.2) says that when an element gets keyboard focus, it must not be completely hidden by content the author added, like a sticky header, a sticky footer or a cookie banner.

On small screens, sticky elements take a bigger share of the viewport, so this happens more often. When a keyboard user tabs down the page, the focused link can end up under a sticky footer.

```css
html {
  scroll-padding-top: var(--header-height);
  scroll-padding-bottom: var(--footer-height);
}
```

`scroll-padding` makes the browser leave room for the sticky elements when it scrolls focus into view. Also consider making headers non-sticky on short viewports.

## 361: How do you keep accessible names when a responsive design hides text labels?

A common pattern shows "Search", "Cart" and "Account" as text on desktop and only icons on mobile. If you hide the text with `display: none`, the buttons have no name for screen readers on mobile.

Hide the text visually instead, or give the button an `aria-label`:

```html
<a href="/cart" class="nav-link">
  <svg aria-hidden="true" class="icon"><use href="#cart" /></svg>
  <span class="nav-label">Cart</span>
</a>
```

```css
@media (width < 600px) {
  .nav-label {
    position: absolute;
    width: 1px;
    height: 1px;
    overflow: hidden;
    clip-path: inset(50%);
    white-space: nowrap;
  }
}
```

Icon-only buttons also hurt sighted users who don't know what the icon means, so keep labels where there's room.

## 362: How do you handle content that needs two-dimensional scrolling under the Reflow criterion?

WCAG Reflow allows two-dimensional scrolling for content that really needs it: data tables, maps, diagrams, video, games, presentations and complex toolbars. Even then, the rest of the page should reflow.

- Put the two-dimensional content in its own scroll container, not the whole page.
- Make the scroll container keyboard accessible (`tabindex="0"`, a role and a label).
- Keep important controls outside the scroll area.
- For tables, consider whether a simpler mobile view (cards, fewer columns) is possible before falling back to scrolling.

```html
<div
  class="table-scroll"
  tabindex="0"
  role="region"
  aria-label="Quarterly results"
>
  <table>
    ...
  </table>
</div>
```

## 363: What is the CSS reading-flow property?

`reading-flow` tells the browser to follow the visual order of items in a flex or grid container, instead of the DOM order, for keyboard focus and for screen readers.

```css
.layout {
  display: grid;
  grid-template-areas: "aside main";
  reading-flow: grid-rows;
}
```

Values include `flex-visual`, `flex-flow`, `grid-rows`, `grid-columns` and `grid-order`. It fixes the long-standing problem where reordering things with `order` or grid placement confused keyboard users. It's only in Chromium browsers so far, so a logical DOM order is still the main solution.

## 364: How does the inert attribute help with responsive overlays?

`inert` makes an element and everything inside it non-interactive: it can't be focused, clicked or found by screen readers. It's the right tool for "everything behind this menu or drawer".

```js
function openDrawer() {
  drawer.hidden = false;
  document.querySelector("main").inert = true;
  document.querySelector("header").inert = true;
  drawer.querySelector("button").focus();
}

function closeDrawer() {
  drawer.hidden = true;
  document.querySelector("main").inert = false;
  document.querySelector("header").inert = false;
}
```

Before `inert`, you had to write a focus trap by hand and add `aria-hidden` to the rest of the page. A modal `<dialog>` does this for you automatically, so use `inert` when you build a custom overlay or keep a closed off-canvas menu out of the tab order.

## 365: How do you build a responsive data table with thousands of rows?

- **Virtualize rows** so only the visible rows are in the DOM. Libraries like TanStack Virtual help. Tens of thousands of DOM rows are slow on phones.
- **Keep sticky headers and a sticky first column** in the scroll container.
- **Use a different view on small screens**: a list of cards with the key fields and a detail screen for the rest.
- **Let users choose columns** to show on medium screens.
- **Use `contain` or `content-visibility`** on row groups if you can't virtualize.
- **Server-side pagination or filtering** to avoid loading everything.

Virtualization has accessibility costs (screen readers can't see off-screen rows), so set `aria-rowcount` and `aria-rowindex` on the table.

## 366: How do you keep a canvas sharp on high-DPR screens and at any size?

A canvas has its own pixel size (`width`/`height` attributes) separate from its CSS size. If you stretch a 300px canvas to 600 CSS pixels on a 2x screen, it's scaled up 4 times and looks blurry.

Set the canvas pixel size to the CSS size times the DPR, and redraw when it changes:

```js
const canvas = document.querySelector("canvas");
const ctx = canvas.getContext("2d");

const observer = new ResizeObserver(([entry]) => {
  const box = entry.devicePixelContentBoxSize?.[0];
  const width = box
    ? box.inlineSize
    : Math.round(entry.contentBoxSize[0].inlineSize * devicePixelRatio);
  const height = box
    ? box.blockSize
    : Math.round(entry.contentBoxSize[0].blockSize * devicePixelRatio);

  canvas.width = width;
  canvas.height = height;
  ctx.setTransform(devicePixelRatio, 0, 0, devicePixelRatio, 0, 0);
  draw();
});

observer.observe(canvas, { box: "device-pixel-content-box" });
```

`devicePixelContentBoxSize` gives the exact size in device pixels, which avoids rounding blur. Safari doesn't support it yet, hence the fallback.

## 367: How do media queries inside an SVG work?

A media query inside an SVG's `<style>` block is evaluated against the SVG's own viewport, not the page. When the SVG is used as an `<img>` or background, its viewport is the size it's displayed at.

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 50">
  <style>
    .wordmark { display: inline; }
    @media (width < 120px) {
      .wordmark { display: none; }
    }
  </style>
  <circle cx="25" cy="25" r="20" />
  <text class="wordmark" x="55" y="32">Acme</text>
</svg>
```

So one logo file can show the icon only when it's rendered small and the full wordmark when it's large. It's like a container query built into the image. `prefers-color-scheme` also works inside SVGs, which lets an SVG icon used as `<img>` adapt to dark mode.

## 368: What are the pros and cons of SVG icon sprites versus inline SVG and icon fonts?

- **Inline SVG** - full CSS control (colors, `currentColor`, animations), no extra requests. Repeating the same icon many times makes the HTML bigger.
- **SVG sprite with `<use>`** - define each icon once as a `<symbol>` and reference it with `<use href="#icon-name">`. Smaller HTML, still styleable with `currentColor`. An external sprite file (`sprite.svg#icon`) can be cached, but must be same-origin.
- **`<img>` with SVG files** - simple and cached, but you can't change colors with CSS from the page.
- **Icon fonts** - legacy. Problems with accessibility, blurry rendering, failed font loads showing empty boxes, and screen readers reading odd characters.

```html
<svg class="icon" aria-hidden="true"><use href="/icons.svg#search" /></svg>
```

Sized in `em`, sprites and inline SVG scale with text at every breakpoint.

## 369: What is font-size-adjust and why is it useful?

Different fonts at the same `font-size` can look very different in size, because their lowercase letters (the x-height) differ. When a fallback font is used, or when a fallback swaps to the web font, text can look bigger or smaller and rewrap.

`font-size-adjust` keeps the x-height the same across fonts:

```css
body {
  font-family: "Inter", Arial, sans-serif;
  font-size-adjust: from-font;
}
```

`from-font` uses the first font's x-height ratio for all fonts in the stack. It works in all modern browsers. It helps keep text readable in small sizes on mobile and reduces layout shift when fonts swap.

## 370: How do you design responsive components for text expansion in other languages?

Translations are often longer than English. German and Finnish can be 30% or more longer, and short labels can double. Some languages like Chinese and Japanese are shorter but need more line height.

- Don't give buttons, tabs or labels fixed widths. Let them grow, and allow wrapping.
- Test with real translations or a "pseudo-localization" that makes strings longer.
- Use `hyphens: auto` with the right `lang` for long words.
- Use `text-wrap: balance` for headings.
- Plan what happens when a nav doesn't fit: wrap, scroll, or move items to a "More" menu.

```css
.tab {
  min-width: 0;
  padding-inline: 1rem;
  white-space: normal;
  text-align: center;
}
```

## 371: How do vertical writing modes affect responsive layouts?

In vertical writing modes (`writing-mode: vertical-rl`, used for traditional Japanese, Chinese and Mongolian, or for design effects), the inline axis runs top to bottom. Physical properties like `width`, `margin-left` and `vw`-based sizes no longer mean what you think.

Logical properties and units follow the writing mode:

```css
.vertical-heading {
  writing-mode: vertical-rl;
  inline-size: 20rem; /* the "length" of the text line, now vertical */
  margin-block-end: 1rem;
}

.card-wrapper {
  container-type: inline-size; /* queries the inline size, whatever direction it is */
}
```

This is why `inline-size` containment and `cqi` units exist. Media queries, however, always use physical `width` and `height`, because they describe the viewport.

## 372: How do you progressively enhance with a new layout feature like anchor positioning?

Write a working default first, then add the new feature inside `@supports`, so browsers without it keep the default.

```css
/* Default: dropdown below the button with normal absolute positioning */
.menu-wrap {
  position: relative;
}

.menu {
  position: absolute;
  top: 100%;
  left: 0;
}

/* Enhancement */
@supports (position-anchor: --a) {
  .menu-wrap {
    position: static;
  }

  .menu {
    position-anchor: --menu-btn;
    position-area: bottom span-right;
    position-try-fallbacks: flip-block, flip-inline;
    top: auto;
    left: auto;
  }
}
```

Test both versions. Make sure the fallback doesn't overflow the screen on small devices, even if it isn't as smart.

## 373: How do cascade layers help when third-party CSS fights your responsive styles?

Third-party CSS (a UI library, a widget) often has selectors with higher specificity than yours, so your media query overrides don't apply and you reach for `!important`.

With `@layer`, the layer order wins over specificity. Put third-party CSS in an earlier layer, and your styles in a later one:

```css
@layer reset, vendor, components, utilities;

@import url("vendor-carousel.css") layer(vendor);

@layer components {
  @media (width < 600px) {
    .carousel .slide {
      width: 100%; /* wins over the vendor's more specific selector */
    }
  }
}
```

Styles that are not in any layer beat all layered styles, so either put everything in layers or remember that rule.

## 374: Why do responsive utility classes sometimes not apply, and how do you debug it?

In utility-first CSS (like Tailwind), classes like `md:flex` are just rules inside a media query, so they follow the normal cascade. Common reasons they don't apply:

- Another class with the same specificity comes later in the generated CSS and wins.
- A component's own CSS has higher specificity.
- The build didn't find the class (for example a class name built with string concatenation like `md:grid-cols-${n}`), so it wasn't generated.
- The breakpoint names or values are customized differently than you think.

In DevTools, check the Styles pane for the element. If the rule is missing, it wasn't generated. If it's crossed out, something else wins. Always write full class names in the code so the build tool can find them.

## 375: How do you decide which devices and browsers to test responsive layouts on?

Use your own analytics as the main input, not a generic list.

- Pick the browsers and OS versions that cover most of your real traffic.
- Include at least: Safari on iOS (the only engine on iPhone for most users), Chrome on a mid-range Android, a desktop Chrome or Edge, desktop Safari, and Firefox.
- Cover viewport extremes: a small phone (320-360px), a big phone, a tablet in both orientations, a laptop and a large monitor.
- Include one low-end device for performance.
- Test assistive tech on mobile too: VoiceOver on iOS and TalkBack on Android.

Automate the common widths in CI and keep manual testing for real devices and touch behavior.

## 376: How do you write an automated test that catches horizontal overflow?

Load each important page at several widths and compare the document's scroll width with the viewport width.

```js
import { test, expect } from "@playwright/test";

const pages = ["/", "/products", "/checkout"];
const widths = [320, 375, 768, 1024, 1440];

for (const path of pages) {
  for (const width of widths) {
    test(`${path} has no horizontal overflow at ${width}px`, async ({
      page,
    }) => {
      await page.setViewportSize({ width, height: 800 });
      await page.goto(path);
      const overflow = await page.evaluate(
        () =>
          document.documentElement.scrollWidth -
          document.documentElement.clientWidth,
      );
      expect(overflow).toBeLessThanOrEqual(0);
    });
  }
}
```

This catches a whole class of bugs cheaply. If it fails, run the "find wide elements" script from the browser console at that width.

## 377: How do you run accessibility checks at mobile viewports?

Many accessibility problems only appear at small sizes: hidden labels, overlapping elements, small targets and content hidden by sticky elements. Run automated checks at a mobile viewport as well as desktop.

```js
import { test, expect } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

test("home page is accessible on mobile", async ({ page }) => {
  await page.setViewportSize({ width: 375, height: 800 });
  await page.goto("/");
  const results = await new AxeBuilder({ page }).analyze();
  expect(results.violations).toEqual([]);
});
```

Automated tools only catch part of the issues. Also test by hand with a screen reader on a phone, with zoom at 400%, and with a keyboard at a narrow desktop width.

## 378: How do you monitor responsive performance with real users?

Collect real user metrics (RUM) and split them by device type, viewport size and connection.

```js
import { onLCP, onCLS, onINP } from "web-vitals/attribution";

function send(metric) {
  navigator.sendBeacon(
    "/analytics",
    JSON.stringify({
      name: metric.name,
      value: metric.value,
      viewport: window.innerWidth,
      dpr: window.devicePixelRatio,
      attribution: metric.attribution,
    }),
  );
}

onLCP(send);
onCLS(send);
onINP(send);
```

Averages hide problems. A page can look fine overall while phones under 400px wide have a bad CLS because of one banner. The Chrome UX Report also shows field data for phone and desktop separately.

## 379: How do you test components at different container widths in Storybook?

Viewport addons only change the iframe size, which tests media queries. To test container queries, render the component inside wrappers of different widths in the story.

```jsx
export const Widths = {
  render: () => (
    <div style={{ display: "grid", gap: "2rem" }}>
      {[240, 360, 520, 760].map((w) => (
        <div key={w} style={{ width: w, containerType: "inline-size" }}>
          <ProductCard {...sampleProduct} />
        </div>
      ))}
    </div>
  ),
};
```

You see every layout of the component at once, and visual regression tools like Chromatic can snapshot this story to catch changes at each width.

## 380: Scenario: The page scrolls horizontally only on iPhone Safari. How do you debug it?

1. Reproduce on a real iPhone or the iOS simulator and connect Safari Web Inspector.
2. Run a script to find elements wider than the viewport, and add outlines to see boxes.
3. Check Safari-specific causes:
   - `100vw` elements (Safari includes or excludes scrollbars differently in some cases).
   - Long words or URLs in a font that's wider in Safari.
   - A flex item without `min-width: 0` holding a wide child.
   - Elements positioned with negative margins or `transform` past the edge.
   - Form controls with a default width in Safari, like `<input type="date">` or `<select>`.
   - A fixed-width element from a third-party widget.
4. Fix the specific element. Don't hide it with `overflow-x: hidden` on the body.

## 381: Scenario: The page zooms in when users tap a form field on iPhone. What do you do?

Safari on iOS zooms in when the focused field's font size is under 16px. Check the computed font size of the inputs. It's often 14px from a design system or from `font-size: 0.875rem`.

```css
input,
select,
textarea {
  font-size: max(1rem, 16px);
}
```

If the design really needs smaller text in inputs on desktop, apply the 16px only on touch devices with `@media (pointer: coarse)`. Don't add `maximum-scale=1` to the viewport meta tag: it blocks zoom for everyone on Android, which is an accessibility failure.

## 382: Scenario: The bottom of a full-height hero is cut off on phones. How do you fix it?

It's the `100vh` problem. On mobile, `100vh` equals the height with the browser toolbars hidden, so when they're visible on first load, the bottom of the hero (often the main button) is under the toolbar.

```css
.hero {
  min-height: 100vh; /* fallback */
  min-height: 100svh;
}
```

Use `svh` so the hero fits when the toolbars are visible. Use `min-height` instead of `height` so the content can still grow when the text wraps more. Also check landscape, where `100svh` might be only 300px, and consider capping it with `min(100svh, 800px)` or removing the full-height style for short viewports.

## 383: Scenario: A hover menu stays open after tapping on a phone. Why and how do you fix it?

Touch browsers simulate `:hover` on tap so hover-based sites still work. The hover state then stays on that element until the user taps somewhere else. So a menu opened with `:hover` stays open, and hover effects like lifted cards get stuck.

Fixes:

- Only apply hover styles on devices that can hover:

```css
@media (hover: hover) {
  .card:hover {
    transform: translateY(-4px);
  }
}
```

- Open menus with a click on a button (`aria-expanded`), and add hover only as an extra for mouse users.
- Close menus on outside click and with Escape.

## 384: Scenario: Images look blurry on high-DPR screens. How do you fix it?

The image file has fewer pixels than the screen needs. A 400 CSS pixel slot on a 2x screen needs an 800 pixel wide image.

1. Check `img.currentSrc` and `img.naturalWidth` against `img.clientWidth * devicePixelRatio`.
2. Add bigger candidates to `srcset` with `w` descriptors and an accurate `sizes`.
3. For fixed-size images like avatars, use `x` descriptors (`1x`, `2x`).
4. Check that the image CDN isn't capping the width or over-compressing.
5. Replace logos, icons and diagrams with SVG.
6. For CSS backgrounds, use `image-set()` with `2x` versions.

```html
<img
  src="avatar-64.jpg"
  srcset="avatar-64.jpg 1x, avatar-128.jpg 2x, avatar-192.jpg 3x"
  width="64"
  height="64"
  alt="Profile photo of Ana"
/>
```

## 385: Scenario: Phones download 4000px wide images. How do you fix it?

1. Check the markup. Often there's a single `src` with the original upload and no `srcset`, or `srcset` without `sizes` (so the browser assumes `100vw`).
2. Generate several sizes with an image CDN or a build step, and add `srcset` and `sizes`.
3. Make sure `sizes` matches the layout at each breakpoint.
4. Serve AVIF or WebP.
5. Lazy load images below the fold.
6. Check CSS backgrounds too. They don't use `srcset`, so they need media queries or `image-set()`.
7. Add a check in CI or monitoring that flags images over a size limit.

The gain is often huge: a 2 MB JPEG can become a 60 KB AVIF on a phone.

## 386: Scenario: The layout shifts sideways when navigating between short and long pages. Why?

On desktops with classic scrollbars, a long page has a vertical scrollbar that takes about 15px, and a short page doesn't. Going from one to the other changes the available width, so centered content jumps sideways. The same happens when a modal locks scrolling with `overflow: hidden`.

```css
html {
  scrollbar-gutter: stable;
}
```

This keeps the space for the scrollbar even when it's not needed. An older fix was `overflow-y: scroll` on `html`, which always shows a scrollbar track.

## 387: Scenario: A sticky sidebar in a grid layout scrolls away instead of sticking. How do you fix it?

Common causes in a grid:

1. The sidebar is a grid item that stretches to the full height of the row, so it has no room to stick. Add `align-self: start`.
2. An ancestor has `overflow: hidden` or `overflow: auto`, which creates a scroll container and the sidebar sticks inside it.
3. `top` isn't set.

```css
.layout {
  display: grid;
  grid-template-columns: 1fr 300px;
  align-items: start;
}

.sidebar {
  position: sticky;
  top: 1rem;
  max-height: calc(100svh - 2rem);
  overflow-y: auto; /* in case the sidebar is taller than the screen */
}
```

To find the ancestor with overflow, check each parent in DevTools, or use `overflow: clip` where clipping is needed, since it doesn't create a scroll container.

## 388: Scenario: A grid column overflows because of a long code block. How do you fix it?

The code block's min-content width is very large (a long line of code that doesn't wrap), and grid tracks defined with `1fr` won't shrink below that.

```css
.layout {
  display: grid;
  grid-template-columns: 250px minmax(0, 1fr);
}

.content pre {
  overflow-x: auto;
  max-width: 100%;
}
```

`minmax(0, 1fr)` lets the content column shrink, and `overflow-x: auto` on the `<pre>` makes the code scroll inside its own box instead of pushing the page wider. The same fix works for tables and long URLs.

## 389: Scenario: You need to make an old fixed-width float-based site responsive. How do you approach it?

1. **Add the viewport meta tag** and global basics (`box-sizing: border-box`, `img { max-width: 100%; height: auto; }`).
2. **Replace fixed widths with `max-width`** on the main containers, so the page fits on small screens.
3. **Replace float layouts with Grid or Flexbox**, one section at a time, starting with the page shell.
4. **Write mobile-first rules for new code**, even if old code is desktop-first. Use `max-width` media queries to patch old sections until they're rewritten.
5. **Fix images and tables**: add `srcset`, wrap wide tables in scroll containers.
6. **Fix touch issues**: hover menus, small links, form inputs.
7. **Test at many widths** and set up a visual regression test so later changes don't break it.

Doing it in steps lets you ship improvements without a full rewrite.

## 390: Scenario: Headings look huge on phones and tiny on large monitors. How do you fix it?

Replace fixed heading sizes and breakpoint jumps with a fluid type scale using `clamp()`, with a `rem` part for accessibility.

```css
:root {
  --step-1: clamp(1.25rem, 1.1rem + 0.6vw, 1.6rem);
  --step-2: clamp(1.5rem, 1.25rem + 1.1vw, 2.2rem);
  --step-3: clamp(1.9rem, 1.4rem + 2vw, 3rem);
}

h1 {
  font-size: var(--step-3);
}
h2 {
  font-size: var(--step-2);
}
h3 {
  font-size: var(--step-1);
}
```

Use a smaller ratio between heading levels on mobile and a larger one on desktop (tools like Utopia generate this), and limit line length so large text doesn't stretch across the whole monitor.

## 391: Scenario: On a landscape phone, the sticky header and a cookie banner cover most of the screen. What do you do?

In landscape, a phone viewport may be only 300-400px tall. A 70px sticky header plus a 150px banner leaves almost nothing.

```css
@media (height < 500px) {
  .site-header {
    position: static;
  }

  .cookie-banner {
    max-height: 40svh;
    overflow-y: auto;
    padding-block: 0.5rem;
  }
}
```

Also make the banner compact (one line of text and buttons side by side), let it be dismissed quickly, and don't block the page with an overlay. Use height media queries for this, not orientation, because a short desktop window has the same problem.

## 392: Scenario: Users on touch-screen laptops see the mobile UI with a mouse. Why?

The code probably decides "mobile or desktop" by detecting touch support, for example `"ontouchstart" in window` or `(pointer: coarse)`, and switches the whole layout. Touch laptops report touch support even when the user is using a trackpad.

Fixes:

- Use **width** to decide the layout, not touch support.
- Use **`hover` and `pointer`** only for small adjustments, and remember they describe the primary input. `any-pointer: coarse` can help make targets bigger without changing the layout.
- Build interactions that work with every input (click and tap), so you don't need to detect anything.

## 393: Scenario: A designer gives you three different crops of the hero image for mobile, tablet and desktop. How do you implement it?

Use `<picture>` with `media` for the crops, `srcset` for resolutions inside each crop, and `type` for formats.

```html
<picture>
  <source
    media="(width >= 1024px)"
    type="image/avif"
    srcset="
      hero-wide-1280.avif 1280w,
      hero-wide-1920.avif 1920w,
      hero-wide-2560.avif 2560w
    "
    sizes="100vw"
  />
  <source
    media="(width >= 600px)"
    type="image/avif"
    srcset="hero-medium-800.avif 800w, hero-medium-1200.avif 1200w"
    sizes="100vw"
  />
  <source
    type="image/avif"
    srcset="
      hero-tall-400.avif   400w,
      hero-tall-800.avif   800w,
      hero-tall-1200.avif 1200w
    "
    sizes="100vw"
  />
  <img
    src="hero-tall-800.jpg"
    width="800"
    height="1000"
    alt="Hikers on a ridge at sunset"
    fetchpriority="high"
  />
</picture>
```

Each crop has a different aspect ratio, so set `width` and `height` on each `<source>` too (browsers support this), which keeps the space reserved correctly and avoids CLS. Add JPEG sources if you need to support browsers without AVIF.

## 394: Scenario: The same card component is used in a narrow sidebar and a wide main column. How do you make it look right in both?

Use container queries, so the card responds to the space it's in, not to the viewport.

```css
.card-container {
  container-type: inline-size;
}

.card {
  display: grid;
  gap: 0.75rem;
}

.card img {
  width: 100%;
  aspect-ratio: 16 / 9;
  object-fit: cover;
}

@container (width >= 450px) {
  .card {
    grid-template-columns: 200px 1fr;
    align-items: start;
  }

  .card img {
    aspect-ratio: 1;
  }
}

@container (width >= 700px) {
  .card .description {
    display: block;
    -webkit-line-clamp: unset;
  }
}
```

With media queries alone, the card in the sidebar would get the wide layout on a large screen even though the sidebar is narrow.

## 395: Scenario: You need to add right-to-left support to an existing responsive site. How do you plan it?

1. Set `dir` and `lang` on `<html>` per locale.
2. Search the CSS for physical properties (`left`, `right`, `margin-left`, `padding-right`, `text-align: left`, `float: left`, `border-left`) and replace them with logical ones. Stylelint has plugins that flag them.
3. Check Flexbox and Grid layouts, which flip automatically, and look for places where `row-reverse` or `order` was used to fake a direction.
4. Flip directional icons (arrows, chevrons) with `:dir(rtl)`, but not logos or media controls.
5. Check transforms and animations that slide in from a side.
6. Check carousels and scroll positions, which start from the right in RTL.
7. Test the mobile and desktop layouts in RTL with real text.

## 396: Scenario: Scrolling is janky on low-end Android phones. How do you find and fix the cause?

1. Record a trace in the Performance panel with CPU throttling, or with remote debugging on the real phone.
2. Look for long tasks during scroll (JavaScript scroll handlers), and for long paint and layout times.

Common causes and fixes:

- **Scroll handlers** - replace with `IntersectionObserver` or scroll-driven animations, or make listeners `passive`.
- **Expensive paint** - large `box-shadow`, `filter` and `backdrop-filter` areas, especially on fixed elements. Simplify them.
- **Animating layout properties** - use `transform` and `opacity`.
- **Huge DOM** - virtualize long lists, use `content-visibility: auto`.
- **Big images** - decoding large images uses CPU and memory. Serve the right sizes.
- **`dvh` elements** - re-layout while the toolbar moves. Use `svh`.

## 397: Scenario: In a chat app, the message input is hidden behind the keyboard on mobile. How do you fix it?

1. Build the app shell with a full-height layout, messages in a scrolling area and the input at the bottom of the flow, not `position: fixed`.

```css
.chat {
  height: 100dvh;
  display: grid;
  grid-template-rows: auto 1fr auto;
}

.messages {
  overflow-y: auto;
  overscroll-behavior: contain;
}
```

2. On Android Chrome, add `interactive-widget=resizes-content` to the viewport meta, so the layout viewport shrinks when the keyboard opens and `100dvh` fits above it.
3. On iOS Safari, which doesn't support that setting, use the `visualViewport` API to set the shell height to the visible height and keep it scrolled to the bottom.
4. Test both platforms with a real keyboard open, in portrait and landscape.

## 398: Scenario: A modal's content is taller than the screen on mobile. How do you fix it?

Limit the modal's height to the viewport and let its body scroll, while keeping the header and actions visible.

```css
dialog {
  max-height: min(90svh, 800px);
  padding: 0;
  display: flex;
  flex-direction: column;
}

dialog[open] {
  display: flex;
}

dialog .modal-body {
  overflow-y: auto;
  overscroll-behavior: contain;
  padding: 1rem;
}

dialog .modal-header,
dialog .modal-footer {
  flex-shrink: 0;
  padding: 1rem;
}
```

Use `svh` (or `dvh` for a modal that should track the toolbar), not `vh`. On small phones, consider making it a full-screen dialog or a bottom sheet. Setting `display: flex` only on `dialog[open]` keeps closed dialogs hidden.

## 399: Scenario: A fixed "Buy now" bar at the bottom overlaps the footer and the iPhone home indicator. How do you fix it?

```css
.buy-bar {
  position: sticky; /* or fixed */
  bottom: 0;
  padding: 0.75rem 1rem;
  padding-bottom: max(0.75rem, env(safe-area-inset-bottom));
  background: var(--surface);
}
```

```html
<meta
  name="viewport"
  content="width=device-width, initial-scale=1, viewport-fit=cover"
/>
```

- Add the safe area inset so the button sits above the home indicator.
- Using `position: sticky` inside the main content instead of `fixed` means the bar stops before the footer naturally.
- If it must be `fixed`, add bottom padding to the page equal to the bar's height so the footer content isn't hidden.
- Hide it on desktop, where the normal button is always visible.

## 400: Scenario: You need to show a table with 20 columns on mobile. What options do you present?

There's no layout trick that fits 20 columns on a 375px screen, so this is a design decision:

1. **Horizontal scroll** with a sticky first column and sticky header. Keeps all data and is honest about the size.
2. **Prioritized columns**: show 3-4 key columns on mobile, with a way to choose others.
3. **Row as a card**: each row becomes a card with the most important fields, and tapping it opens the full record.
4. **Summary plus detail**: a short list on mobile with a detail screen.
5. **Export or desktop prompt** for power users who need all columns at once.

Often the answer is a mix: cards for browsing and a scrolling table for comparing. Ask what users actually do with the data on their phones.

## 401: Scenario: CLS is bad only on mobile. How do you find the cause?

1. Look at field data split by device (Chrome UX Report, your RUM) to confirm it's mobile only and which pages.
2. Use the web-vitals attribution build in production to log which element shifted.
3. Reproduce in DevTools at a mobile width with network throttling and look at the layout shift track in the Performance panel.

Common mobile-only causes:

- Ads or embeds with reserved space for desktop sizes only.
- Images without dimensions in a layout that only stacks on mobile.
- A font swap that rewraps text, which happens more in narrow columns.
- A sticky banner or "install app" bar inserted at the top after load.
- JavaScript that switches from a desktop to a mobile layout after hydration.

Fix by reserving space, using overlays for banners, and letting CSS decide the layout from the first paint.

## 402: Scenario: LCP is good on desktop but bad on mobile. What do you check?

- **What the LCP element is on mobile.** It may be a different element than on desktop, for example a text block or a different image crop.
- **Image size.** Phones may be downloading a desktop-sized image because of a missing or wrong `sizes`.
- **Lazy loading.** An image below the fold on desktop can be above the fold on mobile and still have `loading="lazy"`.
- **Discovery.** Is the image in the HTML, or added by JavaScript or CSS? Late discovery hurts more on slow networks.
- **Priority.** Add `fetchpriority="high"` to the mobile LCP image.
- **JavaScript cost.** A big bundle blocks rendering longer on slow phone CPUs.
- **Server response time and redirects**, which hurt more on mobile networks.

## 403: Scenario: The nav items wrap to two lines at a certain width. How do you fix it?

This happens between breakpoints, where there's enough room to show the desktop nav but not enough for all items on one line.

Options:

- Move the breakpoint for the mobile nav up to where the items stop fitting. Better yet, use a container query on the header so it depends on the space the nav actually has.
- Reduce spacing fluidly with `clamp()` for gaps and padding.
- Use the priority+ pattern, moving extra items into "More".
- Allow the nav to scroll horizontally on medium screens, with a visual hint.

```css
.header {
  container-type: inline-size;
}

.nav-links {
  display: none;
}

@container (width >= 820px) {
  .nav-links {
    display: flex;
    gap: clamp(0.75rem, 2cqi, 2rem);
  }

  .nav-toggle {
    display: none;
  }
}
```

Remember that translations and larger font settings change where this happens.

## 404: Scenario: In dark mode, photos and white illustrations look too bright. What can you do?

- **Swap images** with `<picture>` and a `prefers-color-scheme: dark` source for illustrations and diagrams that have dark versions.
- **Use SVG with `currentColor` or CSS variables** for illustrations, so they follow the theme.
- **Slightly dim photos** in dark mode:

```css
@media (prefers-color-scheme: dark) {
  img:not([src$=".svg"]) {
    filter: brightness(0.85) contrast(1.1);
  }
}
```

- **Avoid white boxes** around transparent PNGs and screenshots by using transparent backgrounds or a dark border.

Keep the dimming subtle. Too much makes photos look dull.

## 405: Scenario: Users with low vision say the text doesn't get bigger when they zoom. What's wrong?

The font sizes are probably set mostly or completely in `vw` (or `cqi`), like `font-size: 4vw`. Zooming makes the viewport smaller in CSS pixels, so `vw` values shrink and the text stays about the same size. If the default font size was changed instead, `px` sizes don't respond either.

Fix:

```css
/* Before */
h1 {
  font-size: 6vw;
}

/* After */
h1 {
  font-size: clamp(2rem, 1.25rem + 3vw, 4rem);
}
```

Make sure every fluid size has a `rem` part and a reasonable max-to-min ratio. Then test at 200% zoom and with a larger default font size, and check against WCAG 1.4.4.

## 406: Scenario: A third-party widget breaks the layout on small screens. What are your options?

1. Check the widget's options for a responsive or mobile mode.
2. Constrain it: put it in a wrapper with `max-width: 100%` and `overflow-x: auto`, and use `min-width: 0` on the parent flex or grid item.
3. If it's an iframe, set `width: 100%` and an `aspect-ratio` or height per breakpoint. Listen for `postMessage` height updates if it supports them.
4. If it injects CSS with high specificity, override it in a later cascade layer, or isolate it in an iframe or shadow DOM.
5. Load a different version or hide it on mobile if the content isn't essential, and link to the full version.
6. Report the issue to the vendor.

Add the page to your automated overflow test, because vendor updates can break it again.

## 407: Scenario: A JavaScript carousel is janky on mobile. How would you rebuild it?

Rebuild it on native scrolling with CSS scroll snap, and use JavaScript only for extras like buttons and dot indicators.

```css
.carousel {
  display: grid;
  grid-auto-flow: column;
  grid-auto-columns: 85%;
  gap: 1rem;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scrollbar-width: none;
}

.carousel > * {
  scroll-snap-align: center;
}
```

```js
const items = carousel.querySelectorAll(":scope > *");
const observer = new IntersectionObserver(
  (entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting) updateDots(entry.target);
    }
  },
  { root: carousel, threshold: 0.6 },
);
items.forEach((item) => observer.observe(item));

next.addEventListener("click", () => {
  carousel.scrollBy({ left: carousel.clientWidth * 0.85, behavior: "smooth" });
});
```

Native scrolling runs off the main thread and feels right on every platform. Old carousels that move slides with `left` or `margin` in JS on every touch move are the main cause of jank.

## 408: Scenario: Users want to print a dashboard. How do you make it print well?

```css
@media print {
  @page {
    size: A4 landscape;
    margin: 1cm;
  }

  .sidebar,
  .top-bar,
  .filters,
  button {
    display: none;
  }

  .dashboard {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.5cm;
  }

  .widget {
    break-inside: avoid;
    border: 1px solid #999;
    box-shadow: none;
  }

  * {
    print-color-adjust: exact; /* keep chart colors */
  }
}
```

Also:

- Charts drawn on canvas may need to redraw at the print size. Listen for `beforeprint` and resize them, or use SVG charts that scale.
- Show the active filters and the date as text, since controls are hidden.
- Expand scrolling areas so data isn't cut off.

## 409: Scenario: How would you design the responsive layout of a product page?

On mobile, one column in order of what users need: images (swipeable gallery), name and price, key options (size, color), add to cart button, then details, reviews and related products.

On desktop, two columns: a large gallery on the left and a sticky purchase panel on the right, with details below.

```css
.product {
  display: grid;
  gap: 1.5rem;
  grid-template-areas:
    "gallery"
    "buy"
    "details";
}

@media (width >= 900px) {
  .product {
    grid-template-columns: minmax(0, 3fr) minmax(320px, 2fr);
    grid-template-areas:
      "gallery buy"
      "details buy";
    align-items: start;
  }

  .buy-panel {
    position: sticky;
    top: 1rem;
  }
}
```

Other points: a sticky add-to-cart bar on mobile once the main button scrolls away, `srcset` on gallery images with the first one prioritized, `<details>` for long specs on mobile, and big tap targets for size and color options.

## 410: Scenario: How do you build a responsive multi-step form?

- **One step per screen on mobile**, with a clear progress indicator ("Step 2 of 4") instead of a full horizontal stepper that doesn't fit.
- **A full stepper** with step names on wider screens.
- **Single-column fields** on mobile, with labels above fields and the right `type`, `inputmode` and `autocomplete`.
- **Sticky actions**: "Back" and "Continue" at the bottom, with safe area padding.
- **Keep data** between steps (and on refresh) so a phone call or app switch doesn't lose progress.
- **Validation** near each field, and move focus to the first error.
- **Focus management**: move focus to the new step's heading when the step changes, so screen reader users know where they are.

```css
.stepper-labels {
  display: none;
}

@media (width >= 768px) {
  .stepper-labels {
    display: flex;
  }

  .stepper-compact {
    display: none;
  }
}
```

## 411: Scenario: A full-screen background video is slow on mobile. What do you do?

- Serve a smaller, shorter, more compressed file for small screens with `<source media>`.
- Use a `poster` image so something shows right away, and treat the poster as the LCP element.
- Respect `prefers-reduced-motion` and `Save-Data` by not playing the video at all.
- Consider showing only the poster on mobile and loading the video on larger screens.
- Use `preload="none"` or `metadata` if the video starts below the fold, and start playback with `IntersectionObserver`.
- Make sure it's `muted` and `playsinline` so iOS allows autoplay inline.

```html
<video
  autoplay
  muted
  loop
  playsinline
  preload="metadata"
  poster="hero-poster.jpg"
>
  <source src="hero-480p.mp4" media="(width < 768px)" type="video/mp4" />
  <source src="hero-1080p.mp4" type="video/mp4" />
</video>
```

Ask whether the video adds enough value on a phone to be worth the data.

## 412: Scenario: Your web app must also work on a TV browser. What changes?

TV interfaces (often called "10-foot UIs") are viewed from across the room and controlled with a remote's arrow keys.

- **Larger text and spacing.** A big base font size for TV viewports.
- **Spatial navigation.** Every action must be reachable with arrow keys, and focus must move in a logical direction. Use real buttons and links so they're focusable.
- **Strong focus styles.** The focus indicator is the cursor, so it must be very visible.
- **Overscan safe area.** Keep content away from the edges, some TVs crop them.
- **No hover.** `hover: none` and `pointer: none` are typical.
- **Performance.** TV browsers often run on weak hardware.

```css
@media (width >= 1920px) and (pointer: none) {
  html {
    font-size: 150%;
  }

  :focus-visible {
    outline: 4px solid #fff;
    outline-offset: 4px;
    transform: scale(1.05);
  }
}
```

Test on a real device, because TV browsers vary a lot.

## 413: Scenario: You build a widget that other sites embed in an iframe. How do you make it responsive?

Inside an iframe, media queries respond to the iframe's own size, not the host page's viewport. So the widget just needs a normal responsive layout based on its own width.

The harder part is the height. The host page doesn't know how tall the content is. Send the height to the parent:

```js
// Inside the widget
const observer = new ResizeObserver(() => {
  parent.postMessage(
    { type: "widget-height", height: document.documentElement.scrollHeight },
    "https://host.example.com",
  );
});
observer.observe(document.documentElement);
```

```js
// On the host page
window.addEventListener("message", (e) => {
  if (e.origin !== "https://widget.example.com") return;
  if (e.data?.type === "widget-height") {
    iframe.style.height = `${e.data.height}px`;
  }
});
```

Always check `origin` on both sides. Give embedders a snippet with `width: 100%` and a sensible starting height.

## 414: Scenario: Several micro-frontends on one page use different breakpoints. How do you fix it?

Different teams using different breakpoints leads to a page where the header switches to mobile at 768px and the content at 1024px, which looks broken between those widths.

- Agree on shared breakpoint tokens and publish them as a package (CSS variables, Sass, JS).
- Have the shell (host app) own the page layout and the media queries that define it.
- Let each micro-frontend use **container queries** for its own internals, so it adapts to the slot the shell gives it, regardless of the viewport.
- Add a visual regression test of the composed page at the shared breakpoints.

Container queries are especially useful here, because micro-frontends don't know where they'll be placed.

## 415: Scenario: How do you build a gallery of images with mixed aspect ratios that forms neat rows?

A justified gallery (like Flickr) keeps every row the same height and fills the width exactly, with images keeping their ratio. You can get close with Flexbox by setting each item's `flex-grow` and `flex-basis` from its aspect ratio.

```html
<div class="justified">
  <a style="--ratio: 1.5" href="#"><img src="a.jpg" alt="..." /></a>
  <a style="--ratio: 0.75" href="#"><img src="b.jpg" alt="..." /></a>
  <a style="--ratio: 1.78" href="#"><img src="c.jpg" alt="..." /></a>
</div>
```

```css
.justified {
  --row-height: clamp(120px, 20vw, 240px);
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.justified > a {
  flex-grow: var(--ratio);
  flex-basis: calc(var(--ratio) * var(--row-height));
}

.justified img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.justified::after {
  content: "";
  flex-grow: 999; /* stops the last row from stretching */
}
```

Wider images get proportionally more space, so rows stay close to the target height at any width.

## 416: How do you animate an accordion opening to its content height?

Animating to `height: auto` didn't use to work. There are two modern ways.

**`interpolate-size`** lets the browser animate to and from keywords like `auto`:

```css
:root {
  interpolate-size: allow-keywords;
}

details::details-content {
  height: 0;
  overflow: clip;
  transition:
    height 0.3s,
    content-visibility 0.3s allow-discrete;
}

details[open]::details-content {
  height: auto;
}
```

This is only in Chromium browsers so far, and `::details-content` support varies, so it's an enhancement.

**The grid trick** works everywhere:

```css
.panel {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows 0.3s;
}

.panel.open {
  grid-template-rows: 1fr;
}

.panel > .inner {
  overflow: hidden;
}
```

Wrap both in `prefers-reduced-motion: no-preference`.

## 417: How do you animate a menu in when it goes from display: none to visible?

Two newer features make this possible in CSS:

- `@starting-style` defines the styles an element starts from when it first appears, so a transition has something to animate from.
- `transition-behavior: allow-discrete` lets `display` and `overlay` take part in a transition, so the element stays visible until the exit animation finishes.

```css
.menu[popover] {
  opacity: 1;
  transform: none;
  transition:
    opacity 0.2s,
    transform 0.2s,
    display 0.2s allow-discrete,
    overlay 0.2s allow-discrete;
}

.menu[popover]:not(:popover-open) {
  opacity: 0;
  transform: translateY(-8px);
}

@starting-style {
  .menu[popover]:popover-open {
    opacity: 0;
    transform: translateY(-8px);
  }
}
```

Both work in all modern browsers. Without them, you needed JavaScript to add a class one frame after showing the element.

## 418: What is the customizable select and why does it matter for responsive forms?

Native `<select>` elements used to be impossible to style beyond the closed button. Many sites rebuilt them with JavaScript, which often broke keyboard and screen reader support and worked badly on mobile.

The customizable select lets you style the dropdown with CSS and put rich content in options:

```css
select,
::picker(select) {
  appearance: base-select;
}

::picker(select) {
  border-radius: 8px;
  max-height: 50svh;
}
```

It keeps the built-in accessibility and keyboard behavior, and positions the picker with anchor positioning so it flips when there's no room. It's in Chromium browsers so far. Other browsers keep the normal select, so it's a safe enhancement. On mobile, think about whether the native OS picker is better for users anyway.

## 419: How would you build a popover that is a dropdown on desktop and a bottom sheet on mobile?

Use one `popover` element and change its positioning with a media query.

```html
<button popovertarget="sort-menu" style="anchor-name: --sort">Sort</button>
<div id="sort-menu" popover class="sheet-or-dropdown">...</div>
```

```css
.sheet-or-dropdown {
  margin: 0;
  border: 0;
  padding: 1rem;
}

@media (width < 640px) {
  .sheet-or-dropdown {
    position: fixed;
    inset: auto 0 0 0;
    width: 100%;
    border-radius: 16px 16px 0 0;
    padding-bottom: max(1rem, env(safe-area-inset-bottom));
  }

  .sheet-or-dropdown::backdrop {
    background: rgb(0 0 0 / 0.3);
  }
}

@media (width >= 640px) {
  .sheet-or-dropdown {
    position-anchor: --sort;
    position-area: bottom span-right;
    position-try-fallbacks: flip-block;
  }
}
```

The behavior (light dismiss, Escape, top layer) stays the same, only the look changes. If the sheet must block the page, use a modal `<dialog>` on mobile instead.

## 420: What can round() and mod() do in responsive layouts?

`round()` rounds a value to a step. It's useful when a fluid value should snap to a grid, like a baseline or a 4px spacing system.

```css
.card {
  /* fluid padding, but always a multiple of 4px */
  padding: round(clamp(12px, 3vw, 32px), 4px);
}

.thumb {
  /* width snaps to multiples of 50px */
  width: round(down, 30vw, 50px);
}
```

`mod()` and `rem()` give the remainder of a division. They're rarely needed in layouts but can help with patterns. These math functions work in all modern browsers.

## 421: What happens when the minimum in clamp() is larger than the maximum?

The minimum wins. `clamp(MIN, VAL, MAX)` is defined as `max(MIN, min(VAL, MAX))`, so if `MIN` is bigger than `MAX`, the result is always `MIN`.

```css
.box {
  width: clamp(500px, 50%, 300px); /* always 500px */
}
```

This matters when the bounds come from variables or mixed units. For example, `clamp(20rem, 50vw, 300px)` behaves differently when the user's font size makes `20rem` bigger than 300px. In that case, the text-based minimum wins, which is usually the accessible choice anyway, but the layout might overflow if you didn't expect it.

## 422: What should you watch out for with % and em inside clamp() for font-size?

In `font-size`, both `%` and `em` are relative to the **parent's** font size, not the root. Inside a fluid formula, this compounds when elements are nested.

```css
/* Each nested .note gets bigger than the last */
.note {
  font-size: clamp(0.9em, 0.8em + 1vw, 1.2em);
}
```

Use `rem` in fluid type formulas so the result doesn't depend on where the element is in the tree. Use `em` only when you really want size relative to the parent, like for a `<small>` inside a heading.

## 423: How do media queries behave inside an iframe?

Inside an iframe, the viewport is the iframe's box. `width`, `height`, `vw`, `vh` and `orientation` all refer to the iframe, not to the browser window. Media features about the user and device, like `prefers-color-scheme`, `hover`, `pointer` and `resolution`, still describe the real device.

This means:

- Embedded content can be fully responsive to the space the host gives it.
- `100vh` inside an iframe is the iframe's height, which may not be what you want if the iframe height grows with content (that can create a loop).
- Responsive testing tools that render your page in iframes show the right layout for each size.

It's the same idea as a container query, but for a whole document.

## 424: How do you generate responsive images in a build pipeline?

Use an image processing library like `sharp`, or a bundler plugin built on it.

```js
// scripts/images.mjs
import sharp from "sharp";

const widths = [400, 800, 1200, 1600];
const formats = ["avif", "webp", "jpeg"];

for (const width of widths) {
  for (const format of formats) {
    await sharp("src/hero.jpg")
      .resize({ width, withoutEnlargement: true })
      .toFormat(format, { quality: format === "avif" ? 50 : 75 })
      .toFile(`dist/hero-${width}.${format}`);
  }
}
```

In Vite, `vite-imagetools` lets you import an image with query parameters (`?w=400;800;1200&format=avif;webp&as=picture`) and get the URLs back. Frameworks like Astro and Next.js do this with their image components. For images uploaded at runtime, use an image CDN instead.

## 425: What are the trade-offs between AVIF, WebP and JPEG for responsive images?

- **AVIF** - usually the smallest file at the same quality, often 30-50% smaller than JPEG. Encoding is slow, which matters if you generate images on the fly. Very large images can take longer to decode on slow phones.
- **WebP** - smaller than JPEG (about 25-35%), fast to encode, supported everywhere modern.
- **JPEG** - universal fallback. Modern encoders like MozJPEG and Jpegli give good results.
- **JPEG XL** - very good compression and lossless JPEG recompression, but browser support is limited, so it's not a practical default yet.

Compare at matched visual quality, not at the same quality number, because the scales differ. Small thumbnails sometimes gain little from AVIF, so test the sizes you actually serve.

## 426: How do responsive images affect SEO?

Google can index images from `<img>` `src` and `srcset`, and from `<picture>`. Good practices:

- Keep a real `<img>` with a crawlable `src`, not only a CSS background or a JS-injected image.
- Write descriptive `alt` text.
- Use descriptive file names and stable URLs, since changing URLs for every size variant on every deploy makes indexing harder.
- Make sure lazy loaded images use native `loading="lazy"` or a method that puts the URL in the HTML, so crawlers find them.
- Image speed affects LCP, which is part of Core Web Vitals and page experience.

Image sitemaps can help Google find images that are hard to discover.

## 427: What does mobile-first indexing mean for responsive sites?

Google crawls and indexes sites using the mobile version of the page. Whatever is in the mobile HTML is what counts for search.

For a responsive site that serves the same HTML to every device, this mostly just works. Things to check:

- Content hidden on mobile with CSS is still in the HTML and indexed, but content that's **not rendered at all** on mobile (removed by JS or a different template) won't count.
- Structured data, meta tags and `alt` text must be on the mobile version.
- Lazy loaded content must load without user interaction like a click.
- The mobile page must not block resources in `robots.txt` that it needs to render.

## 428: What are the SEO risks of serving different HTML to mobile and desktop?

Serving different HTML from the same URL based on the device is called dynamic serving. Google supports it, but it's easy to get wrong:

- You must send `Vary: User-Agent`, or caches and crawlers may get the wrong version.
- If the mobile version has less content, fewer links or missing structured data, rankings can drop, since Google indexes the mobile version.
- Device detection mistakes can send the wrong version to users or crawlers.
- Separate mobile URLs (`m.example.com`) need `rel="alternate"` and `rel="canonical"` annotations and are even more work.

Google recommends responsive design because it avoids all of this.

## 429: Can media queries be used to fingerprint users?

Yes. Each media feature reveals a small piece of information: screen size, DPR, color scheme, reduced motion, contrast, pointer type, color gamut and so on. Combined with other data, these bits can help identify a browser across sites without cookies. Media queries can even be used from CSS alone, by loading different background images per condition and logging which ones the server receives.

Browsers reduce this by limiting precision (for example rounding some values), adding privacy modes, and rejecting new features that leak too much. For example, `prefers-reduced-data` has been slow to ship partly due to such concerns. As a developer, avoid collecting these values unless you need them, and don't send them to third parties with user identifiers.

## 430: What are common Safari-specific responsive problems?

- **Viewport height and toolbars** - `100vh` taller than the visible area. Use `svh` or `dvh`.
- **Input zoom** - zooming on focus for fields under 16px.
- **Keyboard and fixed elements** - fixed bars ending up behind the keyboard.
- **Form controls** - default styles and widths for `date`, `select` and `search` inputs that differ from Chrome.
- **Rubber-band scrolling** - showing the background behind the page.
- **Safe areas** - content under the notch or home indicator without `viewport-fit=cover` and insets.
- **Feature gaps** - Safari ships some features earlier and some later than Chromium (for example Client Hints and the VirtualKeyboard API aren't supported).
- **Web app mode** - differences when the site is added to the home screen.

Test on a real iPhone. All iOS browsers use WebKit in most regions, so Chrome on iPhone has the same issues.

## 431: Where should containment go in a component library that uses container queries?

The common approach: the component doesn't make itself a container. Instead, either the layout slot (grid cell, sidebar, column) is the container, or the component has an outer wrapper element that is the container and an inner element that gets styled.

```html
<div class="product-card">
  <!-- container -->
  <article class="product-card__inner">...</article>
  <!-- styled by @container -->
</div>
```

```css
.product-card {
  container: product-card / inline-size;
}

@container product-card (width >= 420px) {
  .product-card__inner {
    grid-template-columns: 160px 1fr;
  }
}
```

Naming the container after the component means its queries only ever target its own wrapper, even when it's nested inside other containers. Document that the wrapper must have a definite width from its parent layout (see the next question).

## 432: What are the downsides of making every element a container?

`container-type: inline-size` applies inline-size containment, so the element's width can't come from its content anymore. That has side effects:

- **Shrink-to-fit sizing breaks.** Inside an `inline-block`, a float, an absolutely positioned box, a `fit-content` element, or a flex item with `flex-basis: auto`, the container's content width is treated as 0, so it collapses.
- **Layout and style containment** are also applied. Layout containment makes the element a containing block for absolutely and fixed positioned descendants and creates a stacking context, which can change how overlays and z-index behave inside it.
- **More work** for the browser when sizes change.

So add containers on purpose, at layout slots and component wrappers that get their width from outside, not on everything by default.

## 433: Scenario: A container inside a flex row collapses to zero width. Why, and how do you fix it?

A flex item with the default `flex-basis: auto` and no width is sized from its content. But with `container-type: inline-size`, its content width counts as 0, so the item shrinks to nothing (or to its padding).

```css
/* Broken */
.toolbar {
  display: flex;
}

.toolbar .search {
  container-type: inline-size;
}
```

Fix it by giving the container a size that doesn't depend on its content:

```css
.toolbar .search {
  container-type: inline-size;
  flex: 1; /* take the free space */
}

/* or */
.toolbar .search {
  container-type: inline-size;
  width: 20rem;
}
```

The same applies to grid items in `auto` tracks or with `justify-self: start`. Give them a track size like `1fr` or `minmax()`.

## 434: What is the difference between the layout viewport and the visual viewport?

- The **layout viewport** is the area the page is laid out in. Media queries, `vw`/`vh`, `position: fixed` and `window.innerWidth` use it.
- The **visual viewport** is the part of the page the user can see right now. It's smaller than the layout viewport when the user pinch-zooms, or when the on-screen keyboard covers part of the screen (in browsers where the keyboard doesn't resize the layout viewport).

When you pinch-zoom on a phone, the layout doesn't change. You're moving a smaller visual viewport around over the same layout. `window.visualViewport` gives you its size, position and scale.

Most of the time they are the same. The difference matters for fixed toolbars, keyboard handling and anything that needs to stay in view while zoomed.

## 435: Why do fixed elements seem to move when users pinch-zoom on mobile?

`position: fixed` is fixed to the layout viewport, not to the visual viewport. When a user pinch-zooms, they see a part of the layout viewport, so a fixed header may be off screen, or fixed elements may drift as they pan around.

That's intended: if fixed elements stayed glued to the screen while zoomed in, they'd be huge and cover everything. If you really need something pinned to the visual viewport (like a zoom reset button), position it with the `visualViewport` API. Usually it's better to accept the default and make sure fixed elements are small and few.

## 436: What is the Window Controls Overlay and how does it affect layout?

For installed desktop PWAs in Chromium browsers, the Window Controls Overlay lets your app draw into the title bar area, like a native app, while the system's window buttons stay in the corner. You enable it with `"display_override": ["window-controls-overlay"]` in the manifest.

Your layout must avoid the window buttons, using the `titlebar-area-*` environment variables:

```css
.app-titlebar {
  position: fixed;
  left: env(titlebar-area-x, 0);
  top: env(titlebar-area-y, 0);
  width: env(titlebar-area-width, 100%);
  height: env(titlebar-area-height, 2.5rem);
  app-region: drag;
}
```

The area changes when the window is resized or the user switches the overlay off, so fallbacks are required. It's similar to safe area insets on phones.

## 437: What is the cost difference between hiding a responsive variant with CSS and not rendering it?

**Hiding with CSS** (render both, `display: none` one):

- Works on first paint and with SSR, no layout jump.
- Costs extra HTML and DOM nodes, and hidden components may still run their JavaScript and effects.
- `<img>` elements inside hidden blocks are still downloaded unless they're lazy loaded.

**Conditional rendering in JS** (render only one):

- Smaller DOM and less work for hidden parts.
- Needs to know the screen size, so it either guesses on the server or switches after hydration, causing a jump.

A good middle ground: use CSS for small differences, and for large, heavy components, render a lightweight placeholder with reserved space and load the heavy part only when a media query matches.

## 438: Does an img inside an element with display: none still download?

Yes. Browsers download `<img>` elements even when they or their parents are hidden with `display: none`, because the preload scanner finds them in the HTML before CSS is applied. Hiding a desktop-only image on mobile doesn't save any data.

Ways to really skip the download:

- `loading="lazy"`. Lazy images inside `display: none` elements aren't loaded, because they never get near the viewport.
- `<picture>` with a `<source>` that points to a tiny placeholder for the screens where it's hidden. This is hacky, so use it rarely.
- Don't render the element on those screens.

CSS background images are different: browsers usually skip backgrounds for elements that aren't rendered.

## 439: Which background images download when they are set in different media queries?

Only the background image from the rule that currently applies gets downloaded. If you set a small image by default and a large one in a `(width >= 1024px)` media query, a phone only downloads the small one.

```css
.hero {
  background-image: url("hero-small.jpg");
}

@media (width >= 1024px) {
  .hero {
    background-image: url("hero-large.jpg");
  }
}
```

If the viewport later changes to match the media query, the large image is downloaded then. Note that a desktop-first setup (large by default, small in a `max-width` query) is also fine in modern browsers, since they only fetch the image that wins in the cascade.

## 440: Does loading="lazy" work for images in a horizontal carousel?

Yes. Native lazy loading checks distance to the viewport in both directions, and it works inside scroll containers too. Images in off-screen slides are loaded as they get close to being scrolled into view.

```html
<div class="carousel">
  <img src="slide-1.jpg" alt="..." width="800" height="600" />
  <img src="slide-2.jpg" alt="..." width="800" height="600" loading="lazy" />
  <img src="slide-3.jpg" alt="..." width="800" height="600" loading="lazy" />
</div>
```

The first visible slide shouldn't be lazy. The distance at which browsers start loading is fixed by the browser and is fairly large, so the next one or two slides usually load before the user swipes. If the slides are hidden with `display: none` instead of being scrolled, they'll load only when shown, which can cause a delay.

## 441: How would you define a responsive strategy for a new product?

1. **Know the users.** Look at analytics or research: which devices, screen sizes, browsers and network conditions. Are they mostly on phones? Do they do long tasks on desktop?
2. **Decide the priorities per context.** What must work on a phone, and what can be desktop-focused (for example complex admin screens)?
3. **Pick the approach.** Mobile-first CSS, a few global breakpoints, container queries for components, fluid type and spacing.
4. **Set budgets.** Page weight, LCP, INP and CLS targets for mobile.
5. **Set accessibility targets.** WCAG 2.2 AA, including reflow at 320px, zoom, target size and orientation.
6. **Define the testing matrix.** Devices, browsers, widths, and automated checks in CI.
7. **Write it down** in the design system docs so designers and developers follow the same rules.

## 442: The design team only provides designs at 375px and 1440px. How do you handle the widths in between?

This is very common. The widths in between are where most responsive bugs appear.

- Talk to the designers early. Agree on how the layout should behave between the two: what stretches, what wraps, where the columns change.
- Build fluid by default, with `clamp()` for type and spacing and intrinsic layouts for grids, so most sizes take care of themselves.
- Find the real breakpoints by resizing the browser, and show the designers the in-between states.
- Ask for a tablet design (around 768-1024px) for complex pages, like navigation and data-heavy screens.
- Build components in Storybook at many widths so designers can review them.

Responsive design is a shared job. Developers often see layout problems first, so share them early.

## 443: Why does a fixed-position element inside a container sometimes stop being fixed to the viewport?

`position: fixed` is normally relative to the viewport, but some properties on an ancestor make that ancestor the containing block for fixed descendants instead:

- `transform`, `translate`, `rotate`, `scale`, `perspective`
- `filter` and `backdrop-filter`
- `contain: layout`, `contain: paint`, `contain: strict` or `contain: content`
- `container-type: inline-size` or `size` (because it applies layout containment)
- `will-change` with one of the above

So if you add a container query wrapper around a component, a "fixed" modal or toast inside it may suddenly be positioned relative to that wrapper and clipped by it.

Fixes: render overlays outside the component (a portal), or use `<dialog>` and `popover`, which go into the top layer and ignore these containing blocks.

## 444: How do you test a responsive layout with a screen reader on a phone?

- **iOS VoiceOver**: Settings, Accessibility, VoiceOver (or ask Siri). Swipe right and left to move through elements, double-tap to activate, and use the rotor (two-finger twist) to jump by headings, links or landmarks.
- **Android TalkBack**: Settings, Accessibility, TalkBack. Similar swipe gestures, and a menu for reading controls and navigation by headings.

Things to check on mobile layouts specifically:

- The reading order matches the visual order after the layout collapses to one column.
- Icon-only buttons have names.
- Menus and dialogs move focus correctly and announce expanded and collapsed state.
- Hidden off-canvas content isn't reachable when closed.
- Content isn't hidden behind sticky elements when VoiceOver focuses it.

## 445: How do you handle orientation changes in JavaScript?

Most layout changes should be done with CSS, but sometimes JS needs to know, for example to resize a canvas or a video player.

```js
const portrait = window.matchMedia("(orientation: portrait)");

portrait.addEventListener("change", (e) => {
  if (e.matches) {
    showPortraitControls();
  } else {
    showLandscapeControls();
  }
});

// Or the Screen Orientation API
screen.orientation.addEventListener("change", () => {
  console.log(screen.orientation.type); // "portrait-primary", "landscape-primary", ...
});
```

The old `orientationchange` event and `window.orientation` are deprecated. Keep in mind that the viewport can be landscape on a portrait device (split screen, keyboard open). Also make sure state like scroll position, form input and open menus survives the change.

## 446: What is different about responsive layouts inside a native app's webview?

When web content runs in a webview inside an iOS or Android app:

- There's no browser toolbar, so viewport height issues are different, but the app's own bars and the system's safe areas still matter. Use `viewport-fit=cover` and `env(safe-area-inset-*)` if the app draws edge to edge.
- The viewport meta tag still matters, and some apps set their own zoom settings.
- Android WebView can apply the system font size through its text zoom setting, which scales your text. Layouts must handle larger text.
- The app may control dark mode separately from the system.
- Debug with Safari Web Inspector (the app must enable inspection) or `chrome://inspect` for debuggable Android WebViews.

Coordinate with the native team about which settings they pass to the webview.

## 447: Can you build a responsive layout without any media queries? When is that not enough?

You can get very far with intrinsic layout:

- `repeat(auto-fit, minmax(min(250px, 100%), 1fr))` for grids.
- Flexbox wrapping and the switcher and sidebar patterns.
- `clamp()`, `min()` and `max()` for type, spacing and widths.
- Container queries for components.

It's not enough when:

- The **navigation pattern** must change (inline links to a menu button), which is a page-level decision.
- **User preferences** matter: dark mode, reduced motion, contrast.
- **Input type** matters: bigger targets for touch, hover effects for mouse.
- **Height** matters, like short landscape screens.
- **Print** styles.
- You need several page-level areas to change together at the same point.

So aim for intrinsic layout first, and use media queries where the decision is about the whole viewport or the user.

## 448: Scenario: A table of contents is a sticky sidebar on desktop and a collapsible section on mobile. How do you build it with one piece of HTML?

Use `<details>` for the mobile version and force it open and sticky on desktop.

```html
<details class="toc" open>
  <summary>On this page</summary>
  <nav aria-label="Table of contents">
    <ol>
      <li><a href="#setup">Setup</a></li>
      <li><a href="#usage">Usage</a></li>
    </ol>
  </nav>
</details>
```

```css
@media (width >= 1024px) {
  .layout {
    display: grid;
    grid-template-columns: minmax(0, 1fr) 260px;
    align-items: start;
  }

  .toc {
    position: sticky;
    top: 1rem;
  }

  .toc summary {
    pointer-events: none;
    list-style: none;
  }
}
```

```js
const toc = document.querySelector(".toc");
const desktop = matchMedia("(width >= 1024px)");
const sync = () => (toc.open = desktop.matches);
sync();
desktop.addEventListener("change", sync);
```

On mobile, it starts closed and users tap to open it. On desktop, it's always open in the sidebar.

## 449: Scenario: Filters are a sidebar on desktop and a full-screen dialog on mobile. How do you avoid duplicating the markup?

Keep one filter form and change how its container behaves.

```html
<button class="filters-open" commandfor="filters" command="show-modal">
  Filters
</button>

<dialog id="filters" class="filters">
  <form>
    <!-- all filter fields -->
    <button
      class="filters-close"
      type="button"
      commandfor="filters"
      command="close"
    >
      Show results
    </button>
  </form>
</dialog>
```

```css
@media (width >= 1024px) {
  .layout {
    display: grid;
    grid-template-columns: 280px minmax(0, 1fr);
  }

  .filters {
    display: block; /* show inline, not as a modal */
    position: static;
    width: auto;
    max-height: none;
    border: 0;
    padding: 0;
  }

  .filters-open,
  .filters-close {
    display: none;
  }
}
```

On mobile, the button opens the dialog modally. On desktop, the dialog element is shown in the page as a normal sidebar. The `commandfor` and `command` attributes (Invoker Commands) open and close the dialog without JS in browsers that support them. Add a small script fallback for older ones. If a modal dialog is open when the window is resized to desktop, close it with a `matchMedia` listener.

## 450: What has changed in responsive design in recent years, and what is coming next?

Recent changes that are now in all modern browsers:

- **Container queries** and container units - components that adapt to their space.
- **`:has()`** - parents that react to their content.
- **New viewport units** (`svh`, `lvh`, `dvh`) - a fix for mobile toolbar issues.
- **Subgrid** - alignment across nested components.
- **Media query range syntax**, CSS nesting, cascade layers.
- **`clamp()`, `min()`, `max()`** - fluid sizes without breakpoints.
- **`aspect-ratio`**, `text-wrap: balance`, `popover`, `<dialog>` improvements, `light-dark()`.

Arriving now or in progress:

- **Anchor positioning** for overlays that stay on screen.
- **Style and scroll-state container queries**.
- **`if()`**, `reading-flow`, customizable `<select>`, `interpolate-size`.
- **Native masonry** layout for Grid.
- **Viewport segments** for foldables.

The general direction: less device-based thinking and fewer breakpoints, more components that adapt on their own, and better respect for user preferences.
