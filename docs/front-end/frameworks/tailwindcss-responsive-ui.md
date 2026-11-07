# TailwindCSS Responsive UI Interview Questions and Answers

_Last updated: October 28, 2026_

450 interview questions with answers about building responsive UIs with Tailwind CSS, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers target Tailwind CSS v4 (v4.3 at the time of writing): CSS-first config with `@theme`, `rem`-based breakpoints, `max-*` variants, built-in container queries and `@custom-variant`. Tailwind v3 things like `tailwind.config.js` and `screens` are mentioned where they still matter, because a lot of existing projects still use them.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is a responsive UI?](#1-what-is-a-responsive-ui)
- [2: How does Tailwind CSS help you build responsive layouts?](#2-how-does-tailwind-css-help-you-build-responsive-layouts)
- [3: What is the viewport meta tag and why do you need it?](#3-what-is-the-viewport-meta-tag-and-why-do-you-need-it)
- [4: What are the default breakpoints in Tailwind CSS v4?](#4-what-are-the-default-breakpoints-in-tailwind-css-v4)
- [5: What does mobile-first mean in Tailwind?](#5-what-does-mobile-first-mean-in-tailwind)
- [6: Does the sm: prefix mean "small screens only"?](#6-does-the-sm-prefix-mean-small-screens-only)
- [7: How do you apply a utility only at a certain breakpoint and above?](#7-how-do-you-apply-a-utility-only-at-a-certain-breakpoint-and-above)
- [8: How do you change the width of an image at different screen sizes?](#8-how-do-you-change-the-width-of-an-image-at-different-screen-sizes)
- [9: What CSS does a class like md:flex generate?](#9-what-css-does-a-class-like-mdflex-generate)
- [10: Can you use responsive prefixes with every utility?](#10-can-you-use-responsive-prefixes-with-every-utility)
- [11: How do you hide an element on mobile and show it on desktop?](#11-how-do-you-hide-an-element-on-mobile-and-show-it-on-desktop)
- [12: How do you show an element on mobile and hide it on desktop?](#12-how-do-you-show-an-element-on-mobile-and-hide-it-on-desktop)
- [13: How do you stack items vertically on mobile and put them side by side on desktop?](#13-how-do-you-stack-items-vertically-on-mobile-and-put-them-side-by-side-on-desktop)
- [14: How do you create a responsive grid of cards?](#14-how-do-you-create-a-responsive-grid-of-cards)
- [15: What does the container class do in Tailwind v4?](#15-what-does-the-container-class-do-in-tailwind-v4)
- [16: How do you center a page wrapper horizontally?](#16-how-do-you-center-a-page-wrapper-horizontally)
- [17: What is the difference between container and max-w-* for page width?](#17-what-is-the-difference-between-container-and-max-w--for-page-width)
- [18: How do you add responsive padding?](#18-how-do-you-add-responsive-padding)
- [19: How do you make text bigger on larger screens?](#19-how-do-you-make-text-bigger-on-larger-screens)
- [20: What does w-full do?](#20-what-does-w-full-do)
- [21: What is the difference between w-screen and w-full?](#21-what-is-the-difference-between-w-screen-and-w-full)
- [22: How do you make an image responsive in Tailwind?](#22-how-do-you-make-an-image-responsive-in-tailwind)
- [23: What does aspect-video do?](#23-what-does-aspect-video-do)
- [24: How do you keep an image from stretching when it fills a box?](#24-how-do-you-keep-an-image-from-stretching-when-it-fills-a-box)
- [25: How do you make a responsive embedded video?](#25-how-do-you-make-a-responsive-embedded-video)
- [26: What does gap do and can it be responsive?](#26-what-does-gap-do-and-can-it-be-responsive)
- [27: Why is gap better than margins between flex items?](#27-why-is-gap-better-than-margins-between-flex-items)
- [28: What does flex-wrap do in a responsive layout?](#28-what-does-flex-wrap-do-in-a-responsive-layout)
- [29: How do you make flex items share space equally?](#29-how-do-you-make-flex-items-share-space-equally)
- [30: How do you set a fraction width that changes per breakpoint?](#30-how-do-you-set-a-fraction-width-that-changes-per-breakpoint)
- [31: What is the difference between w-1/2 and basis-1/2?](#31-what-is-the-difference-between-w-12-and-basis-12)
- [32: How do you change text alignment at different breakpoints?](#32-how-do-you-change-text-alignment-at-different-breakpoints)
- [33: How do you make a button full width on mobile only?](#33-how-do-you-make-a-button-full-width-on-mobile-only)
- [34: What does min-h-screen do?](#34-what-does-min-h-screen-do)
- [35: What are dvh, svh and lvh, and which Tailwind classes use them?](#35-what-are-dvh-svh-and-lvh-and-which-tailwind-classes-use-them)
- [36: How do you make a sticky header?](#36-how-do-you-make-a-sticky-header)
- [37: How do you stop text from overflowing on small screens?](#37-how-do-you-stop-text-from-overflowing-on-small-screens)
- [38: What does truncate do?](#38-what-does-truncate-do)
- [39: How do you limit text to three lines?](#39-how-do-you-limit-text-to-three-lines)
- [40: What is a hamburger menu and how do you build the basic layout with Tailwind?](#40-what-is-a-hamburger-menu-and-how-do-you-build-the-basic-layout-with-tailwind)
- [41: How do you change the order of items at a breakpoint?](#41-how-do-you-change-the-order-of-items-at-a-breakpoint)
- [42: What does flex-row-reverse do and when is it useful?](#42-what-does-flex-row-reverse-do-and-when-is-it-useful)
- [43: How do you change the number of columns in a CSS grid?](#43-how-do-you-change-the-number-of-columns-in-a-css-grid)
- [44: How do you make a grid item span multiple columns?](#44-how-do-you-make-a-grid-item-span-multiple-columns)
- [45: How do you add responsive margins?](#45-how-do-you-add-responsive-margins)
- [46: What does the spacing scale in Tailwind v4 look like?](#46-what-does-the-spacing-scale-in-tailwind-v4-look-like)
- [47: How do you make responsive font sizes without lots of breakpoints?](#47-how-do-you-make-responsive-font-sizes-without-lots-of-breakpoints)
- [48: What is a fluid layout?](#48-what-is-a-fluid-layout)
- [49: What is the difference between a fluid layout and an adaptive layout?](#49-what-is-the-difference-between-a-fluid-layout-and-an-adaptive-layout)
- [50: How do you limit the width of a paragraph for readability?](#50-how-do-you-limit-the-width-of-a-paragraph-for-readability)
- [51: How do you add a breakpoint prefix together with hover?](#51-how-do-you-add-a-breakpoint-prefix-together-with-hover)
- [52: Does hover: work on touch devices in Tailwind v4?](#52-does-hover-work-on-touch-devices-in-tailwind-v4)
- [53: What is the dark: variant?](#53-what-is-the-dark-variant)
- [54: What do the portrait: and landscape: variants do?](#54-what-do-the-portrait-and-landscape-variants-do)
- [55: What does the print: variant do?](#55-what-does-the-print-variant-do)
- [56: What does motion-reduce: do?](#56-what-does-motion-reduce-do)
- [57: How do you make a table work on small screens?](#57-how-do-you-make-a-table-work-on-small-screens)
- [58: What does overflow-x-auto do?](#58-what-does-overflow-x-auto-do)
- [59: How do you find which element is causing horizontal scroll on mobile?](#59-how-do-you-find-which-element-is-causing-horizontal-scroll-on-mobile)
- [60: How do you add space between stacked items without gap?](#60-how-do-you-add-space-between-stacked-items-without-gap)
- [61: How do you switch space-y to space-x at a breakpoint?](#61-how-do-you-switch-space-y-to-space-x-at-a-breakpoint)
- [62: What is the difference between hidden and invisible?](#62-what-is-the-difference-between-hidden-and-invisible)
- [63: What does sr-only do?](#63-what-does-sr-only-do)
- [64: How do you make a two-column layout with a sidebar?](#64-how-do-you-make-a-two-column-layout-with-a-sidebar)
- [65: How do you make a simple responsive footer?](#65-how-do-you-make-a-simple-responsive-footer)
- [66: How do you make the footer stay at the bottom of short pages?](#66-how-do-you-make-the-footer-stay-at-the-bottom-of-short-pages)
- [67: How do you center something both vertically and horizontally?](#67-how-do-you-center-something-both-vertically-and-horizontally)
- [68: How do you change justify-content at a breakpoint?](#68-how-do-you-change-justify-content-at-a-breakpoint)
- [69: How do you change align-items at a breakpoint?](#69-how-do-you-change-align-items-at-a-breakpoint)
- [70: What does max-w-full do?](#70-what-does-max-w-full-do)
- [71: What does max-w-screen-md mean in v4?](#71-what-does-max-w-screen-md-mean-in-v4)
- [72: How do you make a horizontal scrolling list on mobile?](#72-how-do-you-make-a-horizontal-scrolling-list-on-mobile)
- [73: How do you add scroll snapping to a horizontal list?](#73-how-do-you-add-scroll-snapping-to-a-horizontal-list)
- [74: How do you make the same component show as a list on mobile and a grid on desktop?](#74-how-do-you-make-the-same-component-show-as-a-list-on-mobile-and-a-grid-on-desktop)
- [75: How do you change border radius at a breakpoint?](#75-how-do-you-change-border-radius-at-a-breakpoint)
- [76: Why would a card be full-bleed on mobile but boxed on desktop?](#76-why-would-a-card-be-full-bleed-on-mobile-but-boxed-on-desktop)
- [77: How do you write a responsive class for a custom value?](#77-how-do-you-write-a-responsive-class-for-a-custom-value)
- [78: How do you use a CSS variable as a value in Tailwind v4?](#78-how-do-you-use-a-css-variable-as-a-value-in-tailwind-v4)
- [79: What is the difference between rem, em and px for responsive design?](#79-what-is-the-difference-between-rem-em-and-px-for-responsive-design)
- [80: Why does Tailwind v4 use rem for breakpoints?](#80-why-does-tailwind-v4-use-rem-for-breakpoints)
- [81: How do you hide a scrollbar but keep scrolling?](#81-how-do-you-hide-a-scrollbar-but-keep-scrolling)
- [82: How do you make a responsive hero section?](#82-how-do-you-make-a-responsive-hero-section)
- [83: How do you show a different number of items per row in a flex layout?](#83-how-do-you-show-a-different-number-of-items-per-row-in-a-flex-layout)
- [84: What does shrink-0 do and why is it common in responsive UIs?](#84-what-does-shrink-0-do-and-why-is-it-common-in-responsive-uis)
- [85: What does min-w-0 do and why do you need it?](#85-what-does-min-w-0-do-and-why-do-you-need-it)
- [86: How do you make an input field responsive?](#86-how-do-you-make-an-input-field-responsive)
- [87: How do you put a form's label and input side by side on desktop only?](#87-how-do-you-put-a-forms-label-and-input-side-by-side-on-desktop-only)
- [88: How do you set a font size that prevents iOS from zooming into inputs?](#88-how-do-you-set-a-font-size-that-prevents-ios-from-zooming-into-inputs)
- [89: What does columns-2 do?](#89-what-does-columns-2-do)
- [90: How do you add break-inside-avoid in a column layout?](#90-how-do-you-add-break-inside-avoid-in-a-column-layout)
- [91: How do you change a grid's gap per breakpoint?](#91-how-do-you-change-a-grids-gap-per-breakpoint)
- [92: How do you change line height at a breakpoint?](#92-how-do-you-change-line-height-at-a-breakpoint)
- [93: How do you check your responsive design in the browser?](#93-how-do-you-check-your-responsive-design-in-the-browser)
- [94: What screen sizes should you test?](#94-what-screen-sizes-should-you-test)
- [95: Should breakpoints match devices?](#95-should-breakpoints-match-devices)
- [96: What does object-center do?](#96-what-does-object-center-do)
- [97: How do you make an avatar always round regardless of size?](#97-how-do-you-make-an-avatar-always-round-regardless-of-size)
- [98: What does size-* do?](#98-what-does-size--do)
- [99: How do you make icons scale with text?](#99-how-do-you-make-icons-scale-with-text)
- [100: What does inline-flex do?](#100-what-does-inline-flex-do)
- [101: How do you add responsive shadows?](#101-how-do-you-add-responsive-shadows)
- [102: How do you change background color by breakpoint?](#102-how-do-you-change-background-color-by-breakpoint)
- [103: How do you show a background image only on large screens?](#103-how-do-you-show-a-background-image-only-on-large-screens)
- [104: Does hidden on an img stop the image from downloading?](#104-does-hidden-on-an-img-stop-the-image-from-downloading)
- [105: How do you use the picture element with Tailwind?](#105-how-do-you-use-the-picture-element-with-tailwind)
- [106: What is a breakpoint?](#106-what-is-a-breakpoint)
- [107: Can you use more than one breakpoint prefix on the same property?](#107-can-you-use-more-than-one-breakpoint-prefix-on-the-same-property)
- [108: Do you need to repeat a class at every breakpoint?](#108-do-you-need-to-repeat-a-class-at-every-breakpoint)
- [109: How do you make a nav bar wrap its links on small screens?](#109-how-do-you-make-a-nav-bar-wrap-its-links-on-small-screens)
- [110: How big should touch targets be?](#110-how-big-should-touch-targets-be)
- [111: How do you make small links easier to tap without changing how they look?](#111-how-do-you-make-small-links-easier-to-tap-without-changing-how-they-look)
- [112: What does the group class have to do with responsive design?](#112-what-does-the-group-class-have-to-do-with-responsive-design)
- [113: How do you show a tooltip only on desktop?](#113-how-do-you-show-a-tooltip-only-on-desktop)
- [114: How do you make a responsive pricing table?](#114-how-do-you-make-a-responsive-pricing-table)
- [115: What is the problem with fixed widths like w-[600px]?](#115-what-is-the-problem-with-fixed-widths-like-w-600px)
- [116: How do you make an element take the full width on mobile and half on desktop?](#116-how-do-you-make-an-element-take-the-full-width-on-mobile-and-half-on-desktop)
- [117: What does the 2xl: prefix target?](#117-what-does-the-2xl-prefix-target)
- [118: Can you use breakpoint prefixes with @apply?](#118-can-you-use-breakpoint-prefixes-with-apply)
- [119: How do you write a media query for a Tailwind breakpoint in your own CSS?](#119-how-do-you-write-a-media-query-for-a-tailwind-breakpoint-in-your-own-css)
- [120: What is Preflight and how does it affect responsive design?](#120-what-is-preflight-and-how-does-it-affect-responsive-design)
- [121: Why does box-sizing border-box matter for responsive layouts?](#121-why-does-box-sizing-border-box-matter-for-responsive-layouts)
- [122: How do you make an element fixed to the bottom on mobile only?](#122-how-do-you-make-an-element-fixed-to-the-bottom-on-mobile-only)
- [123: What does inset-x-0 do?](#123-what-does-inset-x-0-do)
- [124: How do you make a modal full screen on mobile and centered on desktop?](#124-how-do-you-make-a-modal-full-screen-on-mobile-and-centered-on-desktop)
- [125: What does z-index have to do with responsive menus?](#125-what-does-z-index-have-to-do-with-responsive-menus)
- [126: How do you add an overlay behind a mobile menu?](#126-how-do-you-add-an-overlay-behind-a-mobile-menu)
- [127: How do you make a responsive image gallery?](#127-how-do-you-make-a-responsive-image-gallery)
- [128: How do you handle long words or URLs on narrow screens?](#128-how-do-you-handle-long-words-or-urls-on-narrow-screens)
- [129: What does break-all do?](#129-what-does-break-all-do)
- [130: What does text-balance do?](#130-what-does-text-balance-do)
- [131: What does text-pretty do?](#131-what-does-text-pretty-do)
- [132: How do you show a short label on mobile and a long label on desktop?](#132-how-do-you-show-a-short-label-on-mobile-and-a-long-label-on-desktop)
- [133: What are the most common responsive layout patterns?](#133-what-are-the-most-common-responsive-layout-patterns)
- [134: How do you build a holy grail layout with Tailwind?](#134-how-do-you-build-a-holy-grail-layout-with-tailwind)
- [135: How do you use grid-rows for a page layout?](#135-how-do-you-use-grid-rows-for-a-page-layout)
- [136: Why do you use underscores in arbitrary values?](#136-why-do-you-use-underscores-in-arbitrary-values)
- [137: How do you make a responsive avatar list that overlaps?](#137-how-do-you-make-a-responsive-avatar-list-that-overlaps)
- [138: What does whitespace-nowrap do?](#138-what-does-whitespace-nowrap-do)
- [139: How do you apply styles for very small phones?](#139-how-do-you-apply-styles-for-very-small-phones)
- [140: How do you make a responsive badge or chip row that does not overflow?](#140-how-do-you-make-a-responsive-badge-or-chip-row-that-does-not-overflow)
- [141: What happens when two classes for the same property have no prefix?](#141-what-happens-when-two-classes-for-the-same-property-have-no-prefix)
- [142: Does the order of classes in the class attribute matter?](#142-does-the-order-of-classes-in-the-class-attribute-matter)
- [143: What is the Prettier plugin for Tailwind and does it help with responsive classes?](#143-what-is-the-prettier-plugin-for-tailwind-and-does-it-help-with-responsive-classes)
- [144: How do you add responsive classes in React or other frameworks?](#144-how-do-you-add-responsive-classes-in-react-or-other-frameworks)
- [145: Can you build class names like md:grid-cols-${n}?](#145-can-you-build-class-names-like-mdgrid-cols-n)
- [146: What does inline-block do in a responsive context?](#146-what-does-inline-block-do-in-a-responsive-context)
- [147: How do you make a two-line clamp on mobile and one line on desktop?](#147-how-do-you-make-a-two-line-clamp-on-mobile-and-one-line-on-desktop)
- [148: How do you change font weight at a breakpoint?](#148-how-do-you-change-font-weight-at-a-breakpoint)
- [149: Where does Tailwind write its media queries?](#149-where-does-tailwind-write-its-media-queries)
- [150: How do you install Tailwind v4 in a Vite project?](#150-how-do-you-install-tailwind-v4-in-a-vite-project)

### Moderate Questions (151-300)

- [151: How do you add a custom breakpoint in Tailwind v4?](#151-how-do-you-add-a-custom-breakpoint-in-tailwind-v4)
- [152: How do you change the value of a default breakpoint?](#152-how-do-you-change-the-value-of-a-default-breakpoint)
- [153: How do you remove a default breakpoint?](#153-how-do-you-remove-a-default-breakpoint)
- [154: How do you replace all default breakpoints with your own?](#154-how-do-you-replace-all-default-breakpoints-with-your-own)
- [155: Why should all breakpoints use the same unit?](#155-why-should-all-breakpoints-use-the-same-unit)
- [156: How did you customize breakpoints in Tailwind v3?](#156-how-did-you-customize-breakpoints-in-tailwind-v3)
- [157: What are max-* variants?](#157-what-are-max--variants)
- [158: How do you target a range of screen sizes?](#158-how-do-you-target-a-range-of-screen-sizes)
- [159: How do you target exactly one breakpoint?](#159-how-do-you-target-exactly-one-breakpoint)
- [160: When should you use max-* instead of mobile-first classes?](#160-when-should-you-use-max--instead-of-mobile-first-classes)
- [161: How do you use an arbitrary breakpoint?](#161-how-do-you-use-an-arbitrary-breakpoint)
- [162: How did arbitrary breakpoints work in v3?](#162-how-did-arbitrary-breakpoints-work-in-v3)
- [163: What are container queries?](#163-what-are-container-queries)
- [164: How do you use container queries in Tailwind v4?](#164-how-do-you-use-container-queries-in-tailwind-v4)
- [165: What are the default container query sizes?](#165-what-are-the-default-container-query-sizes)
- [166: What CSS does the @container class generate?](#166-what-css-does-the-container-class-generate)
- [167: What is the difference between md: and @md:?](#167-what-is-the-difference-between-md-and-md)
- [168: How do you use max-width container queries?](#168-how-do-you-use-max-width-container-queries)
- [169: How do you target a range with container queries?](#169-how-do-you-target-a-range-with-container-queries)
- [170: What are named containers and when do you need them?](#170-what-are-named-containers-and-when-do-you-need-them)
- [171: How do you add a custom container size?](#171-how-do-you-add-a-custom-container-size)
- [172: How do you use an arbitrary container query size?](#172-how-do-you-use-an-arbitrary-container-query-size)
- [173: What are container query units and how do you use them?](#173-what-are-container-query-units-and-how-do-you-use-them)
- [174: What does @container-size do?](#174-what-does-container-size-do)
- [175: When should you use container queries instead of media queries?](#175-when-should-you-use-container-queries-instead-of-media-queries)
- [176: Can a container query style the container itself?](#176-can-a-container-query-style-the-container-itself)
- [177: What problems can container-type inline-size cause?](#177-what-problems-can-container-type-inline-size-cause)
- [178: How do you build a card that changes layout based on its own width?](#178-how-do-you-build-a-card-that-changes-layout-based-on-its-own-width)
- [179: How do you switch dark mode to a class instead of the system setting?](#179-how-do-you-switch-dark-mode-to-a-class-instead-of-the-system-setting)
- [180: How do you use a data attribute for dark mode?](#180-how-do-you-use-a-data-attribute-for-dark-mode)
- [181: What does @custom-variant do?](#181-what-does-custom-variant-do)
- [182: How do you write a custom variant with more than one rule?](#182-how-do-you-write-a-custom-variant-with-more-than-one-rule)
- [183: How do you create a height-based breakpoint?](#183-how-do-you-create-a-height-based-breakpoint)
- [184: How do you use an arbitrary media query without adding a variant?](#184-how-do-you-use-an-arbitrary-media-query-without-adding-a-variant)
- [185: What do pointer-fine and pointer-coarse do?](#185-what-do-pointer-fine-and-pointer-coarse-do)
- [186: What is the difference between pointer-* and any-pointer-* variants?](#186-what-is-the-difference-between-pointer--and-any-pointer--variants)
- [187: How do you support the iPhone notch and home bar?](#187-how-do-you-support-the-iphone-notch-and-home-bar)
- [188: How do you create a custom utility for safe area padding?](#188-how-do-you-create-a-custom-utility-for-safe-area-padding)
- [189: How do you customize the container class in v4?](#189-how-do-you-customize-the-container-class-in-v4)
- [190: How did the container class work in v3?](#190-how-did-the-container-class-work-in-v3)
- [191: How do you build a mobile menu with no JavaScript?](#191-how-do-you-build-a-mobile-menu-with-no-javascript)
- [192: How do you build a mobile menu toggle in React?](#192-how-do-you-build-a-mobile-menu-toggle-in-react)
- [193: How do you build a menu toggle with the peer variant?](#193-how-do-you-build-a-menu-toggle-with-the-peer-variant)
- [194: How do you use the has-* variant in responsive layouts?](#194-how-do-you-use-the-has--variant-in-responsive-layouts)
- [195: How do you build an off-canvas sidebar that slides in on mobile?](#195-how-do-you-build-an-off-canvas-sidebar-that-slides-in-on-mobile)
- [196: What is the data-* variant and how does it help with responsive UI?](#196-what-is-the-data--variant-and-how-does-it-help-with-responsive-ui)
- [197: How do you make a responsive table that becomes cards on mobile?](#197-how-do-you-make-a-responsive-table-that-becomes-cards-on-mobile)
- [198: How do you make a sticky table header inside a scroll container?](#198-how-do-you-make-a-sticky-table-header-inside-a-scroll-container)
- [199: How do you make the first table column sticky when scrolling sideways?](#199-how-do-you-make-the-first-table-column-sticky-when-scrolling-sideways)
- [200: How do you create a grid that fits as many columns as possible?](#200-how-do-you-create-a-grid-that-fits-as-many-columns-as-possible)
- [201: What is the difference between auto-fill and auto-fit?](#201-what-is-the-difference-between-auto-fill-and-auto-fit)
- [202: How do you add a reusable auto-fill grid utility?](#202-how-do-you-add-a-reusable-auto-fill-grid-utility)
- [203: How do you prevent auto-fill grid items from overflowing on very small screens?](#203-how-do-you-prevent-auto-fill-grid-items-from-overflowing-on-very-small-screens)
- [204: What is subgrid and how do you use it in Tailwind?](#204-what-is-subgrid-and-how-do-you-use-it-in-tailwind)
- [205: How do you set a named grid template area layout in Tailwind?](#205-how-do-you-set-a-named-grid-template-area-layout-in-tailwind)
- [206: What are arbitrary properties?](#206-what-are-arbitrary-properties)
- [207: How do you make a sticky sidebar inside a two-column layout?](#207-how-do-you-make-a-sticky-sidebar-inside-a-two-column-layout)
- [208: Why does position sticky sometimes not work?](#208-why-does-position-sticky-sometimes-not-work)
- [209: How do you keep a long sidebar scrollable on desktop?](#209-how-do-you-keep-a-long-sidebar-scrollable-on-desktop)
- [210: How do you lock body scroll when a mobile menu is open?](#210-how-do-you-lock-body-scroll-when-a-mobile-menu-is-open)
- [211: How do you style a native dialog responsively?](#211-how-do-you-style-a-native-dialog-responsively)
- [212: How do you build a bottom navigation bar for mobile?](#212-how-do-you-build-a-bottom-navigation-bar-for-mobile)
- [213: How do you build responsive tabs that scroll on mobile?](#213-how-do-you-build-responsive-tabs-that-scroll-on-mobile)
- [214: How do you show a select instead of tabs on mobile?](#214-how-do-you-show-a-select-instead-of-tabs-on-mobile)
- [215: How do you make a responsive multi-column form?](#215-how-do-you-make-a-responsive-multi-column-form)
- [216: What is the forms plugin and does it matter for responsive forms?](#216-what-is-the-forms-plugin-and-does-it-matter-for-responsive-forms)
- [217: How do you make typography plugin content responsive?](#217-how-do-you-make-typography-plugin-content-responsive)
- [218: How do you define a responsive type scale in @theme?](#218-how-do-you-define-a-responsive-type-scale-in-theme)
- [219: Why mix rem and vw in clamp for font sizes?](#219-why-mix-rem-and-vw-in-clamp-for-font-sizes)
- [220: How do you make responsive spacing tokens?](#220-how-do-you-make-responsive-spacing-tokens)
- [221: How do you change the base spacing unit in v4?](#221-how-do-you-change-the-base-spacing-unit-in-v4)
- [222: What is the difference between @theme and :root variables?](#222-what-is-the-difference-between-theme-and-root-variables)
- [223: How do you use theme variables in JavaScript?](#223-how-do-you-use-theme-variables-in-javascript)
- [224: How do you write a useMediaQuery hook that matches Tailwind breakpoints?](#224-how-do-you-write-a-usemediaquery-hook-that-matches-tailwind-breakpoints)
- [225: Why should you avoid rendering different components based on screen width in JS?](#225-why-should-you-avoid-rendering-different-components-based-on-screen-width-in-js)
- [226: How do you avoid a layout flash when using JS breakpoints with SSR?](#226-how-do-you-avoid-a-layout-flash-when-using-js-breakpoints-with-ssr)
- [227: How do you handle responsive variants in a component library with cva?](#227-how-do-you-handle-responsive-variants-in-a-component-library-with-cva)
- [228: What is tailwind-merge and why is it useful with responsive classes?](#228-what-is-tailwind-merge-and-why-is-it-useful-with-responsive-classes)
- [229: How do you set up a cn helper?](#229-how-do-you-set-up-a-cn-helper)
- [230: How do you make tailwind-merge know about your custom breakpoints?](#230-how-do-you-make-tailwind-merge-know-about-your-custom-breakpoints)
- [231: How do you use responsive classes with Next.js Image?](#231-how-do-you-use-responsive-classes-with-nextjs-image)
- [232: What is srcset and sizes and how do they relate to Tailwind classes?](#232-what-is-srcset-and-sizes-and-how-do-they-relate-to-tailwind-classes)
- [233: How do you build a masonry layout with Tailwind?](#233-how-do-you-build-a-masonry-layout-with-tailwind)
- [234: How do you handle RTL layouts responsively?](#234-how-do-you-handle-rtl-layouts-responsively)
- [235: What are the block-direction logical utilities added in v4.2?](#235-what-are-the-block-direction-logical-utilities-added-in-v42)
- [236: How do you add responsive styles in a CSS module or Vue style block?](#236-how-do-you-add-responsive-styles-in-a-css-module-or-vue-style-block)
- [237: How do you test responsive layouts automatically?](#237-how-do-you-test-responsive-layouts-automatically)
- [238: Can you test responsive Tailwind classes with Jest or Vitest and jsdom?](#238-can-you-test-responsive-tailwind-classes-with-jest-or-vitest-and-jsdom)
- [239: How do you make Storybook show components at different widths?](#239-how-do-you-make-storybook-show-components-at-different-widths)
- [240: How do you make a responsive dashboard layout?](#240-how-do-you-make-a-responsive-dashboard-layout)
- [241: How do you make a chart resize with its container?](#241-how-do-you-make-a-chart-resize-with-its-container)
- [242: How do you handle a responsive layout for a page with a fixed header?](#242-how-do-you-handle-a-responsive-layout-for-a-page-with-a-fixed-header)
- [243: What is scroll-mt and why is it useful with sticky headers?](#243-what-is-scroll-mt-and-why-is-it-useful-with-sticky-headers)
- [244: How do you hide content only on print but keep it on screen?](#244-how-do-you-hide-content-only-on-print-but-keep-it-on-screen)
- [245: What is the contrast-more variant?](#245-what-is-the-contrast-more-variant)
- [246: What is the forced-colors variant?](#246-what-is-the-forced-colors-variant)
- [247: How do you combine dark mode and breakpoints?](#247-how-do-you-combine-dark-mode-and-breakpoints)
- [248: How does variant stacking order work in v4?](#248-how-does-variant-stacking-order-work-in-v4)
- [249: How do you apply important to a responsive class in v4?](#249-how-do-you-apply-important-to-a-responsive-class-in-v4)
- [250: How do you use a prefix with responsive classes in v4?](#250-how-do-you-use-a-prefix-with-responsive-classes-in-v4)
- [251: What is the * variant and how can it help with responsive layouts?](#251-what-is-the--variant-and-how-can-it-help-with-responsive-layouts)
- [252: How do you style the last item differently on mobile?](#252-how-do-you-style-the-last-item-differently-on-mobile)
- [253: How do you build a responsive breadcrumb that collapses on mobile?](#253-how-do-you-build-a-responsive-breadcrumb-that-collapses-on-mobile)
- [254: How do you make a responsive card with an image on top on mobile and on the side on desktop?](#254-how-do-you-make-a-responsive-card-with-an-image-on-top-on-mobile-and-on-the-side-on-desktop)
- [255: How do you make a responsive comparison layout with sticky labels?](#255-how-do-you-make-a-responsive-comparison-layout-with-sticky-labels)
- [256: How do you build a responsive split screen login page?](#256-how-do-you-build-a-responsive-split-screen-login-page)
- [257: How do you make a button group that stacks on small screens?](#257-how-do-you-make-a-button-group-that-stacks-on-small-screens)
- [258: Why would you use flex-col-reverse for buttons on mobile?](#258-why-would-you-use-flex-col-reverse-for-buttons-on-mobile)
- [259: How do visual order changes affect accessibility?](#259-how-do-visual-order-changes-affect-accessibility)
- [260: How do you hide something visually on desktop but keep it for screen readers?](#260-how-do-you-hide-something-visually-on-desktop-but-keep-it-for-screen-readers)
- [261: Is it a good idea to remove content on mobile?](#261-is-it-a-good-idea-to-remove-content-on-mobile)
- [262: How do you make an accordion that is open on desktop and collapsible on mobile?](#262-how-do-you-make-an-accordion-that-is-open-on-desktop-and-collapsible-on-mobile)
- [263: How do you build a filter sidebar that becomes a drawer on mobile?](#263-how-do-you-build-a-filter-sidebar-that-becomes-a-drawer-on-mobile)
- [264: How do you make a responsive search bar that expands on focus?](#264-how-do-you-make-a-responsive-search-bar-that-expands-on-focus)
- [265: How do you check which breakpoint is active while developing?](#265-how-do-you-check-which-breakpoint-is-active-while-developing)
- [266: How do you debug a responsive class that does not work?](#266-how-do-you-debug-a-responsive-class-that-does-not-work)
- [267: How do you tell Tailwind to scan files it does not find by default?](#267-how-do-you-tell-tailwind-to-scan-files-it-does-not-find-by-default)
- [268: How do you force Tailwind to generate classes that are not in your files?](#268-how-do-you-force-tailwind-to-generate-classes-that-are-not-in-your-files)
- [269: What is the safelist and how did it work in v3?](#269-what-is-the-safelist-and-how-did-it-work-in-v3)
- [270: How do you share responsive design tokens across several apps?](#270-how-do-you-share-responsive-design-tokens-across-several-apps)
- [271: How do you make an element take the remaining viewport height under a header?](#271-how-do-you-make-an-element-take-the-remaining-viewport-height-under-a-header)
- [272: Why do you need min-h-0 in a flex column?](#272-why-do-you-need-min-h-0-in-a-flex-column)
- [273: How do you make an app shell that only scrolls the content area?](#273-how-do-you-make-an-app-shell-that-only-scrolls-the-content-area)
- [274: How do you use the starting: variant for a mobile menu animation?](#274-how-do-you-use-the-starting-variant-for-a-mobile-menu-animation)
- [275: How do you animate a mobile drawer?](#275-how-do-you-animate-a-mobile-drawer)
- [276: Why animate transform instead of left or width?](#276-why-animate-transform-instead-of-left-or-width)
- [277: What does field-sizing-content do?](#277-what-does-field-sizing-content-do)
- [278: How do you make a chat layout on mobile?](#278-how-do-you-make-a-chat-layout-on-mobile)
- [279: How does the on-screen keyboard affect mobile layouts?](#279-how-does-the-on-screen-keyboard-affect-mobile-layouts)
- [280: How do you make a responsive layout in an email with Tailwind?](#280-how-do-you-make-a-responsive-layout-in-an-email-with-tailwind)
- [281: How do you use the supports-* variant?](#281-how-do-you-use-the-supports--variant)
- [282: How do you apply styles when JavaScript is disabled?](#282-how-do-you-apply-styles-when-javascript-is-disabled)
- [283: How do you make a responsive hero image with text on top?](#283-how-do-you-make-a-responsive-hero-image-with-text-on-top)
- [284: What is the difference between svh and dvh for a hero section?](#284-what-is-the-difference-between-svh-and-dvh-for-a-hero-section)
- [285: How do you handle responsive spacing in a design system without hard-coding breakpoints in every component?](#285-how-do-you-handle-responsive-spacing-in-a-design-system-without-hard-coding-breakpoints-in-every-component)
- [286: How do you write a responsive @utility with a value?](#286-how-do-you-write-a-responsive-utility-with-a-value)
- [287: What is the difference between @utility and plain CSS classes?](#287-what-is-the-difference-between-utility-and-plain-css-classes)
- [288: How do you make a responsive grid where the first item is bigger?](#288-how-do-you-make-a-responsive-grid-where-the-first-item-is-bigger)
- [289: How do you fill holes in a grid with items of different sizes?](#289-how-do-you-fill-holes-in-a-grid-with-items-of-different-sizes)
- [290: How do you make grid rows the same height across columns?](#290-how-do-you-make-grid-rows-the-same-height-across-columns)
- [291: How do you push a card's button to the bottom so buttons line up?](#291-how-do-you-push-a-cards-button-to-the-bottom-so-buttons-line-up)
- [292: How do you build a responsive navbar with a centered logo?](#292-how-do-you-build-a-responsive-navbar-with-a-centered-logo)
- [293: How do you show more columns of a table on bigger screens?](#293-how-do-you-show-more-columns-of-a-table-on-bigger-screens)
- [294: How do you avoid repeating long responsive class lists?](#294-how-do-you-avoid-repeating-long-responsive-class-lists)
- [295: How do you style children based on the parent's breakpoint in a group?](#295-how-do-you-style-children-based-on-the-parents-breakpoint-in-a-group)
- [296: How do you build a responsive sidebar that collapses to icons on medium screens?](#296-how-do-you-build-a-responsive-sidebar-that-collapses-to-icons-on-medium-screens)
- [297: How do you make text and images in a section line up to a max-width while the background stays full width?](#297-how-do-you-make-text-and-images-in-a-section-line-up-to-a-max-width-while-the-background-stays-full-width)
- [298: How do you make one element break out of a max-width container to full width?](#298-how-do-you-make-one-element-break-out-of-a-max-width-container-to-full-width)
- [299: How do you migrate responsive classes from Tailwind v3 to v4?](#299-how-do-you-migrate-responsive-classes-from-tailwind-v3-to-v4)
- [300: What are the browser requirements for Tailwind v4?](#300-what-are-the-browser-requirements-for-tailwind-v4)

### Advanced Questions (301-450)

- [301: How does Tailwind decide the order of responsive rules in the output CSS?](#301-how-does-tailwind-decide-the-order-of-responsive-rules-in-the-output-css)
- [302: Why do all Tailwind utilities have the same specificity, and why does that matter for responsive design?](#302-why-do-all-tailwind-utilities-have-the-same-specificity-and-why-does-that-matter-for-responsive-design)
- [303: How do cascade layers in Tailwind v4 affect responsive styles?](#303-how-do-cascade-layers-in-tailwind-v4-affect-responsive-styles)
- [304: What happens when unlayered third-party CSS conflicts with responsive utilities?](#304-what-happens-when-unlayered-third-party-css-conflicts-with-responsive-utilities)
- [305: What does Tailwind v4's scanner do with responsive class names?](#305-what-does-tailwind-v4s-scanner-do-with-responsive-class-names)
- [306: Why can't Tailwind generate classes from a variable breakpoint prop like breakpoint="md"?](#306-why-cant-tailwind-generate-classes-from-a-variable-breakpoint-prop-like-breakpointmd)
- [307: How would you design a React component API that takes responsive props, like cols={{ base: 1, md: 3 }}?](#307-how-would-you-design-a-react-component-api-that-takes-responsive-props-like-cols-base-1-md-3-)
- [308: How can CSS variables reduce the number of generated responsive classes?](#308-how-can-css-variables-reduce-the-number-of-generated-responsive-classes)
- [309: How do you create a responsive variant that depends on both a breakpoint and a theme attribute?](#309-how-do-you-create-a-responsive-variant-that-depends-on-both-a-breakpoint-and-a-theme-attribute)
- [310: What changed about @variant in v4.3?](#310-what-changed-about-variant-in-v43)
- [311: Why can't you use var(--breakpoint-md) in a media query?](#311-why-cant-you-use-var--breakpoint-md-in-a-media-query)
- [312: Is the theme() function deprecated in v4?](#312-is-the-theme-function-deprecated-in-v4)
- [313: What is the difference between the media range syntax and min-width?](#313-what-is-the-difference-between-the-media-range-syntax-and-min-width)
- [314: What is the fractional pixel gap problem with max-width breakpoints?](#314-what-is-the-fractional-pixel-gap-problem-with-max-width-breakpoints)
- [315: How does browser zoom interact with rem-based breakpoints?](#315-how-does-browser-zoom-interact-with-rem-based-breakpoints)
- [316: In a media query, is rem based on the html font-size you set in CSS?](#316-in-a-media-query-is-rem-based-on-the-html-font-size-you-set-in-css)
- [317: What WCAG rule relates directly to responsive design?](#317-what-wcag-rule-relates-directly-to-responsive-design)
- [318: How do you test the 400% zoom reflow requirement?](#318-how-do-you-test-the-400-zoom-reflow-requirement)
- [319: How do sticky headers cause accessibility problems at high zoom?](#319-how-do-sticky-headers-cause-accessibility-problems-at-high-zoom)
- [320: What is WCAG 1.4.4 Resize Text and how does it affect fluid typography?](#320-what-is-wcag-144-resize-text-and-how-does-it-affect-fluid-typography)
- [321: How do you compute a clamp() for fluid type between two breakpoints?](#321-how-do-you-compute-a-clamp-for-fluid-type-between-two-breakpoints)
- [322: When is a fluid spacing scale a better choice than breakpoint-based spacing?](#322-when-is-a-fluid-spacing-scale-a-better-choice-than-breakpoint-based-spacing)
- [323: How does container-type inline-size affect layout performance?](#323-how-does-container-type-inline-size-affect-layout-performance)
- [324: Can container queries cause layout loops?](#324-can-container-queries-cause-layout-loops)
- [325: How do you debug container queries in browser DevTools?](#325-how-do-you-debug-container-queries-in-browser-devtools)
- [326: Why can't you query a container's height with the normal @container class?](#326-why-cant-you-query-a-containers-height-with-the-normal-container-class)
- [327: What other side effects does container-type have?](#327-what-other-side-effects-does-container-type-have)
- [328: How do you handle a component that needs both viewport and container responsiveness?](#328-how-do-you-handle-a-component-that-needs-both-viewport-and-container-responsiveness)
- [329: How do you use container queries inside a component library so consumers do not have to add @container?](#329-how-do-you-use-container-queries-inside-a-component-library-so-consumers-do-not-have-to-add-container)
- [330: How do named containers help when nesting library components?](#330-how-do-named-containers-help-when-nesting-library-components)
- [331: What are style queries and does Tailwind support them?](#331-what-are-style-queries-and-does-tailwind-support-them)
- [332: How do you support browsers without container query support?](#332-how-do-you-support-browsers-without-container-query-support)
- [333: How does Tailwind generate container query variants internally?](#333-how-does-tailwind-generate-container-query-variants-internally)
- [334: Can you use container queries with @apply?](#334-can-you-use-container-queries-with-apply)
- [335: How do you use container query units for a fluid component without media queries?](#335-how-do-you-use-container-query-units-for-a-fluid-component-without-media-queries)
- [336: What is the fallback for container query units with no container?](#336-what-is-the-fallback-for-container-query-units-with-no-container)
- [337: How do you handle a responsive image whose displayed size depends on a container, not the viewport?](#337-how-do-you-handle-a-responsive-image-whose-displayed-size-depends-on-a-container-not-the-viewport)
- [338: How do responsive images affect Largest Contentful Paint?](#338-how-do-responsive-images-affect-largest-contentful-paint)
- [339: How do you preload a responsive hero image?](#339-how-do-you-preload-a-responsive-hero-image)
- [340: How do responsive layouts cause Cumulative Layout Shift?](#340-how-do-responsive-layouts-cause-cumulative-layout-shift)
- [341: How does using JavaScript to switch layouts after hydration hurt CLS?](#341-how-does-using-javascript-to-switch-layouts-after-hydration-hurt-cls)
- [342: What is the cost of rendering both mobile and desktop versions with hidden?](#342-what-is-the-cost-of-rendering-both-mobile-and-desktop-versions-with-hidden)
- [343: How would you handle a page where mobile and desktop need truly different components?](#343-how-would-you-handle-a-page-where-mobile-and-desktop-need-truly-different-components)
- [344: What are client hints and can they help with responsive SSR?](#344-what-are-client-hints-and-can-they-help-with-responsive-ssr)
- [345: How do you debug why a breakpoint fires at the wrong width on a real phone?](#345-how-do-you-debug-why-a-breakpoint-fires-at-the-wrong-width-on-a-real-phone)
- [346: How do you handle responsive layouts inside iframes?](#346-how-do-you-handle-responsive-layouts-inside-iframes)
- [347: How does a Tailwind setup work in micro frontends with different breakpoints?](#347-how-does-a-tailwind-setup-work-in-micro-frontends-with-different-breakpoints)
- [348: How do you use Tailwind inside Shadow DOM web components?](#348-how-do-you-use-tailwind-inside-shadow-dom-web-components)
- [349: How would you design breakpoints for a design system used by many products?](#349-how-would-you-design-breakpoints-for-a-design-system-used-by-many-products)
- [350: What are the trade-offs of semantic breakpoint names like tablet and desktop?](#350-what-are-the-trade-offs-of-semantic-breakpoint-names-like-tablet-and-desktop)
- [351: How do you prevent conflicting classes when a component takes a className prop?](#351-how-do-you-prevent-conflicting-classes-when-a-component-takes-a-classname-prop)
- [352: How does tailwind-merge handle stacked responsive variants?](#352-how-does-tailwind-merge-handle-stacked-responsive-variants)
- [353: What is the performance cost of tailwind-merge?](#353-what-is-the-performance-cost-of-tailwind-merge)
- [354: How do you handle a component that should be responsive to the viewport in one place and fixed in another?](#354-how-do-you-handle-a-component-that-should-be-responsive-to-the-viewport-in-one-place-and-fixed-in-another)
- [355: How do you make a responsive grid with columns that are at least a minimum width but never more than N columns?](#355-how-do-you-make-a-responsive-grid-with-columns-that-are-at-least-a-minimum-width-but-never-more-than-n-columns)
- [356: How would you put that capped auto-fill grid into a reusable utility?](#356-how-would-you-put-that-capped-auto-fill-grid-into-a-reusable-utility)
- [357: How do you make the layout change when the number of items changes, not the width?](#357-how-do-you-make-the-layout-change-when-the-number-of-items-changes-not-the-width)
- [358: How do you style a list differently when it has only one item?](#358-how-do-you-style-a-list-differently-when-it-has-only-one-item)
- [359: What are the performance concerns with has-*?](#359-what-are-the-performance-concerns-with-has-)
- [360: How would you build a responsive layout that adapts to user preference for density?](#360-how-would-you-build-a-responsive-layout-that-adapts-to-user-preference-for-density)
- [361: How do you handle foldable devices?](#361-how-do-you-handle-foldable-devices)
- [362: How do you handle very wide screens like 3440px ultrawides?](#362-how-do-you-handle-very-wide-screens-like-3440px-ultrawides)
- [363: How do you handle landscape phones?](#363-how-do-you-handle-landscape-phones)
- [364: What is the difference between orientation media queries and aspect-ratio media queries?](#364-what-is-the-difference-between-orientation-media-queries-and-aspect-ratio-media-queries)
- [365: How does the on-screen keyboard break orientation variants?](#365-how-does-the-on-screen-keyboard-break-orientation-variants)
- [366: What are the interactive-widget viewport options?](#366-what-are-the-interactive-widget-viewport-options)
- [367: How do you keep a fixed bottom bar above the keyboard on iOS?](#367-how-do-you-keep-a-fixed-bottom-bar-above-the-keyboard-on-ios)
- [368: How does the VirtualKeyboard API work with Tailwind?](#368-how-does-the-virtualkeyboard-api-work-with-tailwind)
- [369: How do you build a responsive layout that uses the full screen on mobile app-like pages?](#369-how-do-you-build-a-responsive-layout-that-uses-the-full-screen-on-mobile-app-like-pages)
- [370: What does overscroll-contain do and why is it useful in mobile UIs?](#370-what-does-overscroll-contain-do-and-why-is-it-useful-in-mobile-uis)
- [371: How do you handle hover-only interactions for devices that have both touch and mouse?](#371-how-do-you-handle-hover-only-interactions-for-devices-that-have-both-touch-and-mouse)
- [372: How do you get the old v3 hover behavior back in v4?](#372-how-do-you-get-the-old-v3-hover-behavior-back-in-v4)
- [373: How would you write a responsive focus style that works for keyboard and touch users?](#373-how-would-you-write-a-responsive-focus-style-that-works-for-keyboard-and-touch-users)
- [374: How do you make sure touch targets are big enough without changing the visual design?](#374-how-do-you-make-sure-touch-targets-are-big-enough-without-changing-the-visual-design)
- [375: How do you size touch targets only on coarse pointers?](#375-how-do-you-size-touch-targets-only-on-coarse-pointers)
- [376: What problems does 100vw cause on desktop?](#376-what-problems-does-100vw-cause-on-desktop)
- [377: What does scrollbar-gutter stable do and when does it help?](#377-what-does-scrollbar-gutter-stable-do-and-when-does-it-help)
- [378: Why does adding overflow-hidden to body for a modal cause a layout shift, and how do you fix it?](#378-why-does-adding-overflow-hidden-to-body-for-a-modal-cause-a-layout-shift-and-how-do-you-fix-it)
- [379: How does the size of the generated CSS grow with responsive classes?](#379-how-does-the-size-of-the-generated-css-grow-with-responsive-classes)
- [380: How would you audit unused responsive classes in a big project?](#380-how-would-you-audit-unused-responsive-classes-in-a-big-project)
- [381: How do you exclude files from Tailwind's scanning?](#381-how-do-you-exclude-files-from-tailwinds-scanning)
- [382: How do you debug which files Tailwind scans?](#382-how-do-you-debug-which-files-tailwind-scans)
- [383: How does Tailwind's JIT model compare to old CSS frameworks for responsive classes?](#383-how-does-tailwinds-jit-model-compare-to-old-css-frameworks-for-responsive-classes)
- [384: What is the risk of very long class lists with many breakpoints?](#384-what-is-the-risk-of-very-long-class-lists-with-many-breakpoints)
- [385: How do you keep responsive class lists readable in code reviews?](#385-how-do-you-keep-responsive-class-lists-readable-in-code-reviews)
- [386: What lint rules help with responsive Tailwind code?](#386-what-lint-rules-help-with-responsive-tailwind-code)
- [387: How do you handle responsive styles that need to be different per tenant in a multi-tenant app?](#387-how-do-you-handle-responsive-styles-that-need-to-be-different-per-tenant-in-a-multi-tenant-app)
- [388: Can you change breakpoint values at runtime?](#388-can-you-change-breakpoint-values-at-runtime)
- [389: How do you emulate runtime breakpoints with container queries?](#389-how-do-you-emulate-runtime-breakpoints-with-container-queries)
- [390: Why do some page builders render previews inside an iframe?](#390-why-do-some-page-builders-render-previews-inside-an-iframe)
- [391: How does print layout interact with breakpoints?](#391-how-does-print-layout-interact-with-breakpoints)
- [392: How do you make a dashboard printable?](#392-how-do-you-make-a-dashboard-printable)
- [393: How do you handle responsive layouts with very long translated text?](#393-how-do-you-handle-responsive-layouts-with-very-long-translated-text)
- [394: What does hyphens-auto need to work?](#394-what-does-hyphens-auto-need-to-work)
- [395: How do you handle responsive layouts for vertical writing modes?](#395-how-do-you-handle-responsive-layouts-for-vertical-writing-modes)
- [396: How do you handle RTL in combination with transforms like slide-in drawers?](#396-how-do-you-handle-rtl-in-combination-with-transforms-like-slide-in-drawers)
- [397: How do you handle responsive grids in RTL?](#397-how-do-you-handle-responsive-grids-in-rtl)
- [398: What is the impact of Tailwind v4 using @property for some utilities?](#398-what-is-the-impact-of-tailwind-v4-using-property-for-some-utilities)
- [399: Why does v4 implement translate, scale and rotate with separate properties?](#399-why-does-v4-implement-translate-scale-and-rotate-with-separate-properties)
- [400: How do you migrate a v3 project that used max-width screens in the config?](#400-how-do-you-migrate-a-v3-project-that-used-max-width-screens-in-the-config)
- [401: What happens to the v3 screens raw option in v4?](#401-what-happens-to-the-v3-screens-raw-option-in-v4)
- [402: What is the cost of many custom variants?](#402-what-is-the-cost-of-many-custom-variants)
- [403: How does Tailwind sort custom variants relative to breakpoints?](#403-how-does-tailwind-sort-custom-variants-relative-to-breakpoints)
- [404: How do you make a custom variant that behaves like a breakpoint and is sorted with them?](#404-how-do-you-make-a-custom-variant-that-behaves-like-a-breakpoint-and-is-sorted-with-them)
- [405: How do JS plugins add responsive variants in v4?](#405-how-do-js-plugins-add-responsive-variants-in-v4)
- [406: How do you write a matchVariant for arbitrary container widths?](#406-how-do-you-write-a-matchvariant-for-arbitrary-container-widths)
- [407: How would you build an "only on this breakpoint" family of variants?](#407-how-would-you-build-an-only-on-this-breakpoint-family-of-variants)
- [408: How would you design a responsive layout system for a CMS where editors pick the layout?](#408-how-would-you-design-a-responsive-layout-system-for-a-cms-where-editors-pick-the-layout)
- [409: How do you handle a third-party widget that uses its own media queries?](#409-how-do-you-handle-a-third-party-widget-that-uses-its-own-media-queries)
- [410: How do you deal with a design that has a breakpoint at 900px?](#410-how-do-you-deal-with-a-design-that-has-a-breakpoint-at-900px)
- [411: How do you convert a pixel-perfect desktop-only design to a responsive Tailwind layout?](#411-how-do-you-convert-a-pixel-perfect-desktop-only-design-to-a-responsive-tailwind-layout)
- [412: What questions should you ask a designer when they give you only desktop and mobile mockups?](#412-what-questions-should-you-ask-a-designer-when-they-give-you-only-desktop-and-mobile-mockups)
- [413: How would you fix a layout that looks fine at 375px and 1440px but breaks at 820px?](#413-how-would-you-fix-a-layout-that-looks-fine-at-375px-and-1440px-but-breaks-at-820px)
- [414: A flex child with a long code block causes horizontal scroll on mobile. How do you fix it?](#414-a-flex-child-with-a-long-code-block-causes-horizontal-scroll-on-mobile-how-do-you-fix-it)
- [415: Why does grid-cols-[1fr_300px] overflow but grid-cols-[minmax(0,1fr)_300px] does not?](#415-why-does-grid-cols-1fr_300px-overflow-but-grid-cols-minmax01fr_300px-does-not)
- [416: A sticky header works on desktop but not on mobile. What would you check?](#416-a-sticky-header-works-on-desktop-but-not-on-mobile-what-would-you-check)
- [417: What is the difference between overflow-hidden and overflow-clip?](#417-what-is-the-difference-between-overflow-hidden-and-overflow-clip)
- [418: Users on iOS see a white gap under a fixed bottom bar. What is happening?](#418-users-on-ios-see-a-white-gap-under-a-fixed-bottom-bar-what-is-happening)
- [419: A full-height mobile layout gets cut off at the bottom in Safari. How do you fix it?](#419-a-full-height-mobile-layout-gets-cut-off-at-the-bottom-in-safari-how-do-you-fix-it)
- [420: How would you write a custom utility that falls back from dvh to vh?](#420-how-would-you-write-a-custom-utility-that-falls-back-from-dvh-to-vh)
- [421: Tailwind classes for md: work locally but not in production. What could cause this?](#421-tailwind-classes-for-md-work-locally-but-not-in-production-what-could-cause-this)
- [422: How can a CSS minifier break responsive styles?](#422-how-can-a-css-minifier-break-responsive-styles)
- [423: How do you use Tailwind with server components and responsive layouts in Next.js?](#423-how-do-you-use-tailwind-with-server-components-and-responsive-layouts-in-nextjs)
- [424: How would you implement a responsive mega menu?](#424-how-would-you-implement-a-responsive-mega-menu)
- [425: Why shouldn't a desktop menu open only on hover?](#425-why-shouldnt-a-desktop-menu-open-only-on-hover)
- [426: How do you implement a responsive data table with column priority?](#426-how-do-you-implement-a-responsive-data-table-with-column-priority)
- [427: How would you make a responsive layout that keeps the scroll position when switching from list to grid?](#427-how-would-you-make-a-responsive-layout-that-keeps-the-scroll-position-when-switching-from-list-to-grid)
- [428: How do you implement a virtualized list that is also responsive?](#428-how-do-you-implement-a-virtualized-list-that-is-also-responsive)
- [429: What is ResizeObserver and when would you use it with Tailwind?](#429-what-is-resizeobserver-and-when-would-you-use-it-with-tailwind)
- [430: How would you implement a "show as many tabs as fit, put the rest in a More menu" pattern?](#430-how-would-you-implement-a-show-as-many-tabs-as-fit-put-the-rest-in-a-more-menu-pattern)
- [431: How do you use the zoom utilities added in v4.3, and are they a good idea for responsive design?](#431-how-do-you-use-the-zoom-utilities-added-in-v43-and-are-they-a-good-idea-for-responsive-design)
- [432: What is content-visibility and does it help on mobile?](#432-what-is-content-visibility-and-does-it-help-on-mobile)
- [433: How do you reduce the work done on mobile for heavy desktop-only content?](#433-how-do-you-reduce-the-work-done-on-mobile-for-heavy-desktop-only-content)
- [434: How do you prevent a hidden desktop video from downloading on mobile?](#434-how-do-you-prevent-a-hidden-desktop-video-from-downloading-on-mobile)
- [435: How would you set up visual regression tests for responsive layouts?](#435-how-would-you-set-up-visual-regression-tests-for-responsive-layouts)
- [436: How do you test container query components in Storybook?](#436-how-do-you-test-container-query-components-in-storybook)
- [437: How do you handle images that need different crops on mobile and desktop (art direction)?](#437-how-do-you-handle-images-that-need-different-crops-on-mobile-and-desktop-art-direction)
- [438: How do you avoid CLS with art-directed images that have different aspect ratios?](#438-how-do-you-avoid-cls-with-art-directed-images-that-have-different-aspect-ratios)
- [439: How do you serve high-DPI images without wasting data?](#439-how-do-you-serve-high-dpi-images-without-wasting-data)
- [440: How do you use logical properties to make responsive layouts work in all writing directions?](#440-how-do-you-use-logical-properties-to-make-responsive-layouts-work-in-all-writing-directions)
- [441: How do you handle responsive design for Electron or desktop apps with resizable windows?](#441-how-do-you-handle-responsive-design-for-electron-or-desktop-apps-with-resizable-windows)
- [442: How do you make resizable panels with Tailwind and keep their content responsive?](#442-how-do-you-make-resizable-panels-with-tailwind-and-keep-their-content-responsive)
- [443: How would you structure CSS for a large app to keep responsive overrides predictable?](#443-how-would-you-structure-css-for-a-large-app-to-keep-responsive-overrides-predictable)
- [444: How does Tailwind's @layer components interact with responsive utilities?](#444-how-does-tailwinds-layer-components-interact-with-responsive-utilities)
- [445: What is the difference between putting a class in @layer components and making it a @utility?](#445-what-is-the-difference-between-putting-a-class-in-layer-components-and-making-it-a-utility)
- [446: In a code review, a teammate uses useMediaQuery to hide a sidebar. What would you suggest?](#446-in-a-code-review-a-teammate-uses-usemediaquery-to-hide-a-sidebar-what-would-you-suggest)
- [447: How would you explain to a junior developer why their layout breaks on phones?](#447-how-would-you-explain-to-a-junior-developer-why-their-layout-breaks-on-phones)
- [448: What would you include in a team guide for responsive Tailwind code?](#448-what-would-you-include-in-a-team-guide-for-responsive-tailwind-code)
- [449: How would you build a responsive layout for a product page from scratch, step by step?](#449-how-would-you-build-a-responsive-layout-for-a-product-page-from-scratch-step-by-step)
- [450: What are the most common mistakes people make when building responsive UIs with Tailwind?](#450-what-are-the-most-common-mistakes-people-make-when-building-responsive-uis-with-tailwind)

---

# Easy Questions (1-150)

## 1: What is a responsive UI?

A responsive UI is a layout that changes to fit the screen it is shown on. The same page works on a phone, a tablet and a wide desktop monitor without a separate site for each. Columns stack or spread out, text sizes change, menus collapse, and images scale down so nothing overflows.

## 2: How does Tailwind CSS help you build responsive layouts?

Tailwind lets you put responsive styles directly on the element with breakpoint prefixes like `md:` and `lg:`. Instead of writing media queries in a separate CSS file, you write `class="flex-col md:flex-row"` and Tailwind generates the media query for you. You can see how an element behaves at every screen size by reading one class list.

## 3: What is the viewport meta tag and why do you need it?

Without it, mobile browsers render the page as if the screen were about 980px wide and then zoom out, so your breakpoints never fire the way you expect. Tailwind's docs tell you to add it to the `<head>` of every page:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
```

`width=device-width` makes the layout width match the device width, and `initial-scale=1.0` sets the starting zoom level.

## 4: What are the default breakpoints in Tailwind CSS v4?

| Prefix | Min width      | Media query               |
| ------ | -------------- | ------------------------- |
| `sm`   | 40rem (640px)  | `@media (width >= 40rem)` |
| `md`   | 48rem (768px)  | `@media (width >= 48rem)` |
| `lg`   | 64rem (1024px) | `@media (width >= 64rem)` |
| `xl`   | 80rem (1280px) | `@media (width >= 80rem)` |
| `2xl`  | 96rem (1536px) | `@media (width >= 96rem)` |

In v4 the breakpoints are defined in `rem`. In v3 they were defined in `px` with the same pixel values.

## 5: What does mobile-first mean in Tailwind?

It means classes without a prefix apply to all screen sizes, starting with the smallest, and prefixed classes apply from that breakpoint and up. You write the phone layout first and then add changes for bigger screens.

```html
<!-- 1 column on phones, 2 from md, 4 from lg -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4"></div>
```

## 6: Does the sm: prefix mean "small screens only"?

No. This is one of the most common mistakes. `sm:` means "640px and wider", not "phones". To style phones, use the class without any prefix and override it at a bigger breakpoint.

```html
<!-- Wrong: text is only centered from 640px up -->
<div class="sm:text-center"></div>

<!-- Right: centered on phones, left aligned from 640px up -->
<div class="text-center sm:text-left"></div>
```

## 7: How do you apply a utility only at a certain breakpoint and above?

Put the breakpoint name and a colon in front of the utility: `md:flex`, `lg:text-xl`, `xl:p-8`. The style kicks in at that breakpoint and stays applied at all larger sizes, until a larger breakpoint overrides it.

## 8: How do you change the width of an image at different screen sizes?

Stack width utilities with different prefixes:

```html
<img class="w-16 md:w-32 lg:w-48" src="/avatar.png" alt="Avatar" />
```

The image is `w-16` by default, `w-32` from 768px and `w-48` from 1024px.

## 9: What CSS does a class like md:flex generate?

Roughly this:

```css
@media (width >= 48rem) {
  .md\:flex {
    display: flex;
  }
}
```

The colon is escaped in the selector. Tailwind v4 uses the newer media query range syntax (`width >= 48rem`) instead of `min-width: 48rem`. Both mean the same thing.

## 10: Can you use responsive prefixes with every utility?

Yes. Every utility in Tailwind can take a breakpoint prefix, including colors, spacing, display, grid, flex, typography, borders, shadows and transforms. You can also combine them with other variants like `hover:` or `dark:`.

## 11: How do you hide an element on mobile and show it on desktop?

Use `hidden` by default and a display utility at the breakpoint where it should appear:

```html
<nav class="hidden md:flex">...</nav>
```

The `nav` has `display: none` on small screens and `display: flex` from 768px.

## 12: How do you show an element on mobile and hide it on desktop?

Do the opposite: give it a visible display value by default and `hidden` at the breakpoint.

```html
<button class="block md:hidden">Menu</button>
```

You can also use a `max-*` variant: `max-md:block hidden` would work too, but the mobile-first version above is the more common style.

## 13: How do you stack items vertically on mobile and put them side by side on desktop?

Use a flex container that switches direction at a breakpoint:

```html
<div class="flex flex-col gap-4 md:flex-row">
  <div>Left</div>
  <div>Right</div>
</div>
```

## 14: How do you create a responsive grid of cards?

Change the number of grid columns at each breakpoint:

```html
<div
  class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4"
>
  <article class="rounded-lg border p-4">Card</article>
  <!-- more cards -->
</div>
```

## 15: What does the container class do in Tailwind v4?

`container` sets `width: 100%` and then a `max-width` equal to the current breakpoint, so the box grows in steps as the screen gets wider. In v4 it does not center itself or add padding. You add those yourself:

```html
<div class="container mx-auto px-4">...</div>
```

## 16: How do you center a page wrapper horizontally?

Give it a max width and auto margins on the left and right:

```html
<main class="mx-auto max-w-5xl px-4">...</main>
```

`mx-auto` sets `margin-inline: auto`, which centers a block element that has a width smaller than its parent.

## 17: What is the difference between container and max-w-* for page width?

`container` jumps between fixed max widths at each breakpoint (640px, 768px, 1024px and so on). `max-w-5xl` or `max-w-7xl` gives one max width, and the content is fluid below it. Many teams prefer `max-w-*` with `mx-auto` because the layout fills the screen smoothly instead of jumping.

## 18: How do you add responsive padding?

Stack padding utilities with breakpoint prefixes:

```html
<section class="px-4 py-8 md:px-8 md:py-12 lg:px-16 lg:py-20">...</section>
```

Small screens get tight padding so the content has room, and bigger screens get more breathing space.

## 19: How do you make text bigger on larger screens?

Use responsive font size utilities:

```html
<h1 class="text-2xl font-bold md:text-4xl lg:text-5xl">Welcome</h1>
```

## 20: What does w-full do?

`w-full` sets `width: 100%`, so the element takes the full width of its parent. It is very common on mobile layouts for inputs, buttons and images. You can then limit it on bigger screens, for example `w-full md:w-auto` for a button.

## 21: What is the difference between w-screen and w-full?

`w-screen` is `width: 100vw`, the full width of the viewport. `w-full` is `width: 100%` of the parent. `w-screen` can cause a horizontal scrollbar on desktop because `100vw` includes the vertical scrollbar width, so `w-full` is usually the safer choice.

## 22: How do you make an image responsive in Tailwind?

Tailwind's base styles (Preflight) already set images and videos to `display: block`, `max-width: 100%` and `height: auto`. So an image will not overflow its container by default. You often add `w-full` to make it fill the space, and `object-cover` with a fixed height or aspect ratio if you need cropping.

```html
<img class="w-full rounded-lg" src="/hero.jpg" alt="" />
```

## 23: What does aspect-video do?

`aspect-video` sets `aspect-ratio: 16 / 9`. The element keeps that shape at any width, which is useful for videos, embeds and image placeholders. Other built-in values are `aspect-square` (1 / 1) and `aspect-auto`, and you can use any ratio with `aspect-4/3` or `aspect-[4/3]`.

## 24: How do you keep an image from stretching when it fills a box?

Use `object-cover` or `object-contain` together with a width and height or an aspect ratio:

```html
<img class="aspect-square w-full object-cover" src="/photo.jpg" alt="" />
```

`object-cover` fills the box and crops the extra. `object-contain` shows the whole image and leaves empty space if the ratio does not match.

## 25: How do you make a responsive embedded video?

Put the iframe in a full-width element with a fixed aspect ratio:

```html
<iframe
  class="aspect-video w-full"
  src="https://www.youtube.com/embed/VIDEO_ID"
  title="Video"
  allowfullscreen
></iframe>
```

## 26: What does gap do and can it be responsive?

`gap-*` sets the space between items in a flex or grid container. Yes, it can be responsive: `gap-4 md:gap-8`. You can also set the axes separately with `gap-x-*` and `gap-y-*`.

## 27: Why is gap better than margins between flex items?

`gap` only adds space between items, never on the outside edges, so you do not need to remove the margin from the first or last item. It also works cleanly when items wrap to a new line, which margin hacks often get wrong.

## 28: What does flex-wrap do in a responsive layout?

`flex-wrap` lets flex items move to the next line when there is not enough room. Without it, items shrink or overflow. It is useful for lists of tags, buttons or chips that should flow naturally on small screens.

```html
<div class="flex flex-wrap gap-2">
  <span class="rounded bg-gray-100 px-2 py-1">React</span>
  <span class="rounded bg-gray-100 px-2 py-1">Tailwind</span>
</div>
```

## 29: How do you make flex items share space equally?

Use `flex-1` on each item. It sets `flex: 1 1 0%`, so all items grow and shrink equally from a zero base.

```html
<div class="flex flex-col gap-4 sm:flex-row">
  <div class="flex-1">A</div>
  <div class="flex-1">B</div>
  <div class="flex-1">C</div>
</div>
```

## 30: How do you set a fraction width that changes per breakpoint?

Use fraction width or basis utilities:

```html
<aside class="w-full md:w-1/3">Sidebar</aside>
<main class="w-full md:w-2/3">Content</main>
```

In v4 you can use any fraction like `w-3/7`, not just a fixed list.

## 31: What is the difference between w-1/2 and basis-1/2?

`w-1/2` sets `width: 50%`. `basis-1/2` sets `flex-basis: 50%`, which is the starting size of a flex item before it grows or shrinks. Inside a flex container, `basis-*` is usually the better choice because it works with flex direction and with `grow` and `shrink`.

## 32: How do you change text alignment at different breakpoints?

```html
<p class="text-center md:text-left">...</p>
```

Centered text often looks better on narrow screens, and left aligned text is easier to read in wide layouts.

## 33: How do you make a button full width on mobile only?

```html
<button class="w-full rounded bg-blue-600 px-4 py-2 text-white sm:w-auto">
  Save
</button>
```

Full width buttons are easier to tap on phones. From `sm` up the button shrinks to fit its content.

## 34: What does min-h-screen do?

`min-h-screen` sets `min-height: 100vh`, so the element is at least as tall as the viewport. It is often used on the page wrapper so the footer stays at the bottom on short pages.

## 35: What are dvh, svh and lvh, and which Tailwind classes use them?

On mobile, the browser address bar shows and hides as you scroll, so `100vh` is not always the visible height.

- `svh` (small viewport height) is the height with the browser UI fully shown.
- `lvh` (large viewport height) is the height with the browser UI hidden.
- `dvh` (dynamic viewport height) changes as the UI shows and hides.

Tailwind has `h-svh`, `h-lvh`, `h-dvh` and the same for `min-h-*` and `max-h-*`. `min-h-dvh` is a good default for a full-height mobile layout.

## 36: How do you make a sticky header?

```html
<header class="sticky top-0 z-10 bg-white/90 backdrop-blur">...</header>
```

`sticky top-0` keeps the header at the top while the page scrolls. `z-10` keeps it above the content, and a background is needed so content does not show through.

## 37: How do you stop text from overflowing on small screens?

It depends on the case:

- `truncate` cuts long text to one line with `...`.
- `line-clamp-2` or `line-clamp-3` shows a fixed number of lines.
- `wrap-break-word` breaks long words like URLs so they wrap instead of overflowing.

## 38: What does truncate do?

`truncate` is a shortcut for three CSS properties: `overflow: hidden`, `text-overflow: ellipsis` and `white-space: nowrap`. The text stays on one line and ends with `...` when it does not fit. In a flex item it often needs `min-w-0` on the item to work.

## 39: How do you limit text to three lines?

```html
<p class="line-clamp-3">Long description text...</p>
```

You can make it responsive too: `line-clamp-2 md:line-clamp-none` shows two lines on mobile and the full text from `md` up.

## 40: What is a hamburger menu and how do you build the basic layout with Tailwind?

A hamburger menu is a button (usually three lines) that opens the navigation on small screens. The basic layout:

```html
<header class="flex items-center justify-between p-4">
  <a href="/" class="font-bold">Logo</a>
  <button class="md:hidden" aria-label="Open menu">☰</button>
  <nav class="hidden gap-6 md:flex">
    <a href="/about">About</a>
    <a href="/blog">Blog</a>
  </nav>
</header>
```

The button only shows below `md`, and the links only show from `md` up. You still need a bit of JavaScript (or a `<details>` element) to open and close the mobile menu.

## 41: How do you change the order of items at a breakpoint?

Use `order-*` utilities:

```html
<div class="flex flex-col md:flex-row">
  <img class="md:order-2" src="/hero.png" alt="" />
  <div class="md:order-1">Text</div>
</div>
```

On mobile the image is first. From `md` up the text comes first. Note that this only changes the visual order, not the reading order for screen readers.

## 42: What does flex-row-reverse do and when is it useful?

`flex-row-reverse` lays out flex items from right to left. It is handy for alternating "image left, text right" and "text left, image right" sections without changing the HTML. Use it together with a breakpoint: `flex-col md:flex-row-reverse`.

## 43: How do you change the number of columns in a CSS grid?

Use `grid-cols-{n}`:

```html
<div class="grid grid-cols-2 md:grid-cols-4">...</div>
```

In v4 any number works, like `grid-cols-15`, not only 1 to 12.

## 44: How do you make a grid item span multiple columns?

Use `col-span-*`, and change it at breakpoints if needed:

```html
<div class="grid grid-cols-1 md:grid-cols-3">
  <main class="md:col-span-2">Content</main>
  <aside>Sidebar</aside>
</div>
```

`col-span-full` makes an item take the whole row.

## 45: How do you add responsive margins?

```html
<div class="mt-4 md:mt-8 lg:mt-12">...</div>
```

All margin utilities (`m-*`, `mx-*`, `my-*`, `mt-*` and so on) work with breakpoint prefixes.

## 46: What does the spacing scale in Tailwind v4 look like?

Spacing utilities are based on one variable, `--spacing`, which is `0.25rem` (4px) by default. `p-4` is `calc(var(--spacing) * 4)`, which is 1rem. In v4 you can use any whole number, like `p-13` or `mt-22`, not only the values from a fixed list.

## 47: How do you make responsive font sizes without lots of breakpoints?

You can use an arbitrary value with `clamp()`:

```html
<h1 class="text-[clamp(1.75rem,4vw,3.5rem)] font-bold">Title</h1>
```

The size grows with the viewport width but never goes below `1.75rem` or above `3.5rem`.

## 48: What is a fluid layout?

A fluid layout uses relative sizes like percentages, fractions, `fr` units and viewport units instead of fixed pixel widths. It stretches and shrinks smoothly with the screen. In Tailwind you get this with classes like `w-full`, `w-1/2`, `flex-1` and grid columns, then cap it with `max-w-*`.

## 49: What is the difference between a fluid layout and an adaptive layout?

A fluid layout changes size continuously with the screen. An adaptive layout switches between a few fixed layouts at specific breakpoints. Most real Tailwind projects mix both: fluid widths inside each breakpoint, and layout changes at breakpoints.

## 50: How do you limit the width of a paragraph for readability?

Long lines are hard to read. Limit the line length with `max-w-prose` or a `ch`-based value:

```html
<p class="max-w-prose">...</p>
<p class="max-w-[65ch]">...</p>
```

`max-w-prose` is about 65 characters wide.

## 51: How do you add a breakpoint prefix together with hover?

Write both variants before the utility:

```html
<a class="text-gray-700 md:hover:text-blue-600">Link</a>
```

The hover color only applies on screens 768px and wider.

## 52: Does hover: work on touch devices in Tailwind v4?

In v4, `hover:` is wrapped in `@media (hover: hover)`, so hover styles only apply on devices with a real hover input like a mouse. This avoids the "sticky hover" problem on phones, where a tap leaves the element in the hover state. Tailwind v3 did not do this.

## 53: What is the dark: variant?

`dark:` applies a style when dark mode is active. By default it follows the operating system setting through `prefers-color-scheme: dark`.

```html
<div class="bg-white text-gray-900 dark:bg-gray-900 dark:text-gray-100">
  ...
</div>
```

It works together with breakpoints, for example `md:dark:bg-gray-800`.

## 54: What do the portrait: and landscape: variants do?

They apply styles based on screen orientation:

```html
<div class="grid grid-cols-1 landscape:grid-cols-2">...</div>
```

`portrait:` uses `@media (orientation: portrait)` and `landscape:` uses `@media (orientation: landscape)`. They are useful for phones turned sideways, where width is large but height is small.

## 55: What does the print: variant do?

`print:` applies styles only when the page is printed:

```html
<nav class="print:hidden">...</nav>
<article class="text-base print:text-black">...</article>
```

You can hide navigation, buttons and ads, and make text black on white for printing.

## 56: What does motion-reduce: do?

`motion-reduce:` applies when the user has turned on "reduce motion" in their system settings. Use it to turn off animations that can make some people feel sick:

```html
<div class="animate-bounce motion-reduce:animate-none">...</div>
```

There is also `motion-safe:`, which applies only when the user has not asked for reduced motion.

## 57: How do you make a table work on small screens?

The easiest way is to let the table scroll sideways inside a wrapper:

```html
<div class="overflow-x-auto">
  <table class="min-w-full text-left">
    ...
  </table>
</div>
```

The page stays the right width, and only the table scrolls.

## 58: What does overflow-x-auto do?

`overflow-x-auto` adds a horizontal scrollbar only when the content is wider than the element. It is useful for tables, code blocks and horizontal card lists on small screens.

## 59: How do you find which element is causing horizontal scroll on mobile?

Open DevTools, switch to the mobile view and scroll sideways to see what sticks out. A quick trick is to add `outline` to everything with a temporary CSS rule like `* { outline: 1px solid red; }`. Common causes are fixed widths like `w-[500px]`, `w-screen`, long words or URLs, wide images without `max-w-full`, and negative margins.

## 60: How do you add space between stacked items without gap?

Use `space-y-*` on the parent:

```html
<div class="space-y-4">
  <p>One</p>
  <p>Two</p>
</div>
```

It adds margin between children. For flex and grid layouts, `gap-*` is usually better because it handles wrapping and does not depend on margins.

## 61: How do you switch space-y to space-x at a breakpoint?

You have to reset the first one:

```html
<div class="flex flex-col space-y-4 md:flex-row md:space-y-0 md:space-x-4">
  ...
</div>
```

This is clumsy, which is why `flex flex-col gap-4 md:flex-row` is the cleaner option.

## 62: What is the difference between hidden and invisible?

`hidden` sets `display: none`, so the element is removed from the layout and takes no space. `invisible` sets `visibility: hidden`, so the element is not shown but still takes up its space. For responsive show and hide, you almost always want `hidden`.

## 63: What does sr-only do?

`sr-only` hides an element visually but keeps it readable by screen readers. It is used for labels on icon buttons. `not-sr-only` undoes it, which you can use at a breakpoint:

```html
<button>
  <svg aria-hidden="true">...</svg>
  <span class="sr-only md:not-sr-only">Search</span>
</button>
```

On mobile only the icon is visible. From `md` up the text label shows too.

## 64: How do you make a two-column layout with a sidebar?

```html
<div class="flex flex-col md:flex-row">
  <aside class="w-full md:w-64 md:shrink-0">Sidebar</aside>
  <main class="flex-1 min-w-0">Content</main>
</div>
```

`shrink-0` keeps the sidebar at its width, `flex-1` lets the main area take the rest, and `min-w-0` lets the main area shrink so wide content does not push it out.

## 65: How do you make a simple responsive footer?

```html
<footer
  class="flex flex-col items-center gap-4 p-6 text-sm md:flex-row md:justify-between"
>
  <p>© 2026 Company</p>
  <nav class="flex gap-4">
    <a href="/privacy">Privacy</a>
    <a href="/terms">Terms</a>
  </nav>
</footer>
```

## 66: How do you make the footer stay at the bottom of short pages?

Make the page a flex column with a minimum height of the screen and let the main area grow:

```html
<body class="flex min-h-dvh flex-col">
  <header>...</header>
  <main class="flex-1">...</main>
  <footer>...</footer>
</body>
```

## 67: How do you center something both vertically and horizontally?

With flex or grid:

```html
<div class="flex min-h-dvh items-center justify-center">...</div>
<div class="grid min-h-dvh place-items-center">...</div>
```

## 68: How do you change justify-content at a breakpoint?

```html
<div class="flex justify-center md:justify-between">...</div>
```

## 69: How do you change align-items at a breakpoint?

```html
<div class="flex flex-col items-start md:flex-row md:items-center">...</div>
```

## 70: What does max-w-full do?

`max-w-full` sets `max-width: 100%`, so the element is never wider than its parent. It is a common safety net for images, videos and fixed-width elements that might be too wide on phones.

## 71: What does max-w-screen-md mean in v4?

In v4, `max-w-screen-*` utilities still exist but are deprecated. They read from the `--breakpoint-*` variables. The v4 way is to use a container size like `max-w-3xl`, or the breakpoint variable directly with `max-w-(--breakpoint-md)`.

## 72: How do you make a horizontal scrolling list on mobile?

```html
<ul class="flex gap-4 overflow-x-auto">
  <li class="w-64 shrink-0">Card</li>
  <li class="w-64 shrink-0">Card</li>
</ul>
```

`shrink-0` stops the cards from squeezing to fit.

## 73: How do you add scroll snapping to a horizontal list?

```html
<ul class="flex snap-x snap-mandatory gap-4 overflow-x-auto">
  <li class="w-4/5 shrink-0 snap-start">Slide 1</li>
  <li class="w-4/5 shrink-0 snap-start">Slide 2</li>
</ul>
```

`snap-x snap-mandatory` on the parent and `snap-start` on each child make the list stop at the start of a card after scrolling. This works well for simple mobile carousels.

## 74: How do you make the same component show as a list on mobile and a grid on desktop?

```html
<ul
  class="flex flex-col divide-y md:grid md:grid-cols-3 md:gap-6 md:divide-y-0"
>
  <li class="py-3 md:rounded-lg md:border md:p-4">Item</li>
</ul>
```

## 75: How do you change border radius at a breakpoint?

```html
<div class="rounded-none sm:rounded-xl">...</div>
```

A common pattern: a card is edge-to-edge with no radius on phones and becomes a rounded card on bigger screens.

## 76: Why would a card be full-bleed on mobile but boxed on desktop?

On a phone, horizontal space is small, so removing the side margin, border and radius gives the content more room. On a wide screen, a boxed card with padding looks cleaner.

```html
<div class="-mx-4 bg-white p-4 sm:mx-0 sm:rounded-xl sm:border">...</div>
```

## 77: How do you write a responsive class for a custom value?

Use the prefix with an arbitrary value:

```html
<div class="h-48 md:h-[420px]">...</div>
```

Arbitrary values work with every variant, so `lg:grid-cols-[200px_1fr]` is fine too. Use them only for one-off values. If you use one often, add it to your theme.

## 78: How do you use a CSS variable as a value in Tailwind v4?

Use parentheses:

```html
<div class="w-(--sidebar-width) md:w-(--sidebar-width-lg)">...</div>
```

`w-(--sidebar-width)` is short for `w-[var(--sidebar-width)]`.

## 79: What is the difference between rem, em and px for responsive design?

`px` is a fixed size. `rem` is relative to the root font size (usually 16px), so it scales when the user changes their browser font size. `em` is relative to the font size of the current element. Tailwind uses `rem` for font sizes, spacing and breakpoints so that layouts respect the user's font settings.

## 80: Why does Tailwind v4 use rem for breakpoints?

Using `rem` means breakpoints scale with the user's base font size. If someone sets a larger default font in their browser, the layout switches to the narrower version sooner, which keeps text from getting cramped. It also keeps breakpoints in the same unit as the rest of the theme.

## 81: How do you hide a scrollbar but keep scrolling?

In Tailwind v4.3 you can use `scrollbar-none`:

```html
<div class="overflow-x-auto scrollbar-none">...</div>
```

In older versions you needed a small custom utility with `scrollbar-width: none` and a `::-webkit-scrollbar` rule.

## 82: How do you make a responsive hero section?

```html
<section
  class="flex flex-col items-center gap-8 px-4 py-16 text-center lg:flex-row lg:py-24 lg:text-left"
>
  <div class="flex-1">
    <h1 class="text-3xl font-bold md:text-5xl">Build faster</h1>
    <p class="mt-4 text-lg text-gray-600">Short pitch here.</p>
  </div>
  <img class="w-full max-w-md lg:max-w-none lg:flex-1" src="/hero.png" alt="" />
</section>
```

## 83: How do you show a different number of items per row in a flex layout?

Give the children a basis that changes per breakpoint:

```html
<div class="flex flex-wrap">
  <div class="basis-full p-2 sm:basis-1/2 lg:basis-1/4">Item</div>
</div>
```

A grid with `grid-cols-*` is usually simpler for this.

## 84: What does shrink-0 do and why is it common in responsive UIs?

`shrink-0` sets `flex-shrink: 0`, so a flex item does not get smaller than its set size. It is used on icons, avatars, sidebars and cards in scroll lists, which otherwise get squeezed on small screens.

## 85: What does min-w-0 do and why do you need it?

Flex and grid items have `min-width: auto` by default, so they will not shrink below their content width. Long text or wide content can then push the layout wider than the screen. `min-w-0` lets the item shrink so `truncate` and wrapping can work.

## 86: How do you make an input field responsive?

```html
<input class="w-full rounded border px-3 py-2 sm:max-w-sm" type="email" />
```

Full width on phones, capped width on larger screens.

## 87: How do you put a form's label and input side by side on desktop only?

```html
<div class="flex flex-col gap-1 md:flex-row md:items-center md:gap-4">
  <label class="md:w-32" for="email">Email</label>
  <input id="email" class="flex-1 rounded border px-3 py-2" />
</div>
```

## 88: How do you set a font size that prevents iOS from zooming into inputs?

iOS Safari zooms in when you focus an input with a font size smaller than 16px. Use at least `text-base` (1rem, 16px) on inputs. If you want smaller text on desktop, use `text-base md:text-sm`.

## 89: What does columns-2 do?

`columns-2` uses CSS multi-column layout to flow content into two columns, like a newspaper. It is often used for simple masonry-style image lists:

```html
<div class="columns-1 gap-4 sm:columns-2 lg:columns-3">
  <img class="mb-4 w-full" src="/1.jpg" alt="" />
</div>
```

## 90: How do you add break-inside-avoid in a column layout?

When content flows into columns, an item can get split between two columns. `break-inside-avoid` keeps each item whole:

```html
<div class="columns-2">
  <div class="mb-4 break-inside-avoid">Card</div>
</div>
```

## 91: How do you change a grid's gap per breakpoint?

```html
<div class="grid grid-cols-2 gap-2 md:grid-cols-4 md:gap-6">...</div>
```

## 92: How do you change line height at a breakpoint?

```html
<p class="text-sm/6 md:text-base/7">...</p>
```

In v4 you can set font size and line height together with the slash syntax: `text-base/7` means base font size with line height `calc(var(--spacing) * 7)`.

## 93: How do you check your responsive design in the browser?

Use the device toolbar in Chrome or Firefox DevTools to set a width or pick a device. Drag the width slowly between breakpoints to catch layouts that break between the common device sizes. Testing on at least one real phone is still important, because touch, browser bars and fonts behave differently on real devices.

## 94: What screen sizes should you test?

There is no perfect list. A practical set is a small phone (about 360px wide), a large phone (about 430px), a tablet (about 768px), a small laptop (about 1280px) and a big desktop (1536px and wider). Also drag the window size between these to catch layouts that only break at in-between widths.

## 95: Should breakpoints match devices?

Not really. It is better to pick breakpoints where your content starts to look bad. Devices change every year, but content needs stay the same. Tailwind's defaults are a good start because they fit common screens, but you can add your own when the content needs it.

## 96: What does object-center do?

`object-center` sets `object-position: center`, which controls which part of an image stays visible when `object-cover` crops it. You can change it per breakpoint, for example `object-top md:object-center`, to keep a person's face visible on narrow crops.

## 97: How do you make an avatar always round regardless of size?

```html
<img
  class="size-10 rounded-full object-cover md:size-14"
  src="/me.jpg"
  alt=""
/>
```

`size-*` sets width and height together, and `rounded-full` makes it a circle.

## 98: What does size-* do?

`size-10` sets both `width` and `height` to the same value. It is a shortcut for `w-10 h-10`. It is useful for icons, avatars and square buttons, and it supports breakpoint prefixes like `size-8 md:size-12`.

## 99: How do you make icons scale with text?

Use `em` sized icons or `size-[1em]`:

```html
<button class="inline-flex items-center gap-2 text-sm md:text-lg">
  <svg class="size-[1em]" aria-hidden="true">...</svg>
  Download
</button>
```

The icon grows together with the button's text size.

## 100: What does inline-flex do?

`inline-flex` makes the element a flex container that sits inline like text. It is common for buttons and badges that contain an icon and a label next to each other.

## 101: How do you add responsive shadows?

```html
<div class="shadow-none sm:shadow-lg">...</div>
```

## 102: How do you change background color by breakpoint?

```html
<div class="bg-white md:bg-gray-50">...</div>
```

This is mostly useful for layout sections, like a sidebar that blends in on mobile and gets its own background on desktop.

## 103: How do you show a background image only on large screens?

```html
<section class="bg-none lg:bg-[url(/images/hero.jpg)] lg:bg-cover lg:bg-center">
  ...
</section>
```

Note that hiding a background image with `bg-none` on mobile means the image is not downloaded there, because the rule never applies. A hidden `<img>`, on the other hand, may still be downloaded.

## 104: Does hidden on an img stop the image from downloading?

No. `display: none` on an `<img>` does not stop the browser from downloading it. If you want different images per screen size, use the `<picture>` element or `srcset` and `sizes` so the browser only downloads the one it needs.

## 105: How do you use the picture element with Tailwind?

Tailwind does not change how `<picture>` works. You style the `<img>` inside it:

```html
<picture>
  <source media="(width >= 48rem)" srcset="/hero-wide.jpg" />
  <img class="w-full object-cover" src="/hero-narrow.jpg" alt="Hero" />
</picture>
```

## 106: What is a breakpoint?

A breakpoint is a screen width where the layout changes. In Tailwind, each breakpoint is a named media query (`sm`, `md`, `lg`, `xl`, `2xl`) that you can use as a prefix on any class.

## 107: Can you use more than one breakpoint prefix on the same property?

Yes, and that is how responsive Tailwind works:

```html
<div class="p-2 sm:p-4 md:p-6 lg:p-8 xl:p-10">...</div>
```

Each one overrides the previous one at its breakpoint and up.

## 108: Do you need to repeat a class at every breakpoint?

No. A class keeps applying at all bigger sizes until another class overrides it. `md:flex` means flex at `md`, `lg`, `xl` and `2xl`. You only add a new prefix when something needs to change.

## 109: How do you make a nav bar wrap its links on small screens?

```html
<nav class="flex flex-wrap gap-x-6 gap-y-2">
  <a href="/">Home</a>
  <a href="/docs">Docs</a>
  <a href="/blog">Blog</a>
</nav>
```

For a small number of links this is often enough and you do not need a hamburger menu.

## 110: How big should touch targets be?

Tap targets should be at least about 44 by 44 CSS pixels (Apple's guidance) or 48 by 48 (Google's guidance). WCAG 2.2 has a minimum of 24 by 24 for level AA. In Tailwind, `min-h-11 min-w-11` gives 44px, and `size-12` gives 48px.

## 111: How do you make small links easier to tap without changing how they look?

Add padding and cancel it with negative margin, or use a pseudo-element to grow the hit area:

```html
<a class="-m-2 p-2" href="/settings">Settings</a>
```

The link looks the same, but the clickable area is bigger.

## 112: What does the group class have to do with responsive design?

`group` lets you style children based on the parent's state, like `group-hover:`. You can combine it with breakpoints: `md:group-hover:block`. For example, a card can show an extra button on hover only on desktop.

## 113: How do you show a tooltip only on desktop?

```html
<div class="group relative">
  <button>?</button>
  <span class="absolute hidden md:group-hover:block">Help text</span>
</div>
```

Phones have no hover, so hiding hover-only content on mobile and showing the info another way (for example inline) is better.

## 114: How do you make a responsive pricing table?

```html
<div class="grid gap-6 md:grid-cols-3">
  <div class="rounded-xl border p-6">Basic</div>
  <div class="rounded-xl border-2 border-blue-600 p-6 md:-mt-4 md:pb-10">
    Pro
  </div>
  <div class="rounded-xl border p-6">Team</div>
</div>
```

The cards stack on mobile. From `md` up they sit side by side, and the middle plan sticks out a bit.

## 115: What is the problem with fixed widths like w-[600px]?

On a phone that is 375px wide, a 600px element overflows and causes horizontal scroll. Use `w-full max-w-[600px]` instead, so it fills the space on small screens and stops at 600px on big ones.

## 116: How do you make an element take the full width on mobile and half on desktop?

```html
<div class="w-full lg:w-1/2">...</div>
```

## 117: What does the 2xl: prefix target?

`2xl:` targets screens 96rem (1536px) and wider. It is used for large desktop monitors, for example to add more columns or bigger max widths.

## 118: Can you use breakpoint prefixes with @apply?

Yes:

```css
@import "tailwindcss";

.card {
  @apply p-4 md:p-8;
}
```

It works, but try not to overuse `@apply`. Putting utilities directly in the markup is the usual Tailwind approach.

## 119: How do you write a media query for a Tailwind breakpoint in your own CSS?

In v4 use `@variant`, or reference the breakpoint with `theme()`:

```css
.sidebar {
  display: none;

  @variant md {
    display: block;
  }
}

@media (width >= theme(--breakpoint-lg)) {
  .sidebar {
    width: 18rem;
  }
}
```

You cannot use `var(--breakpoint-md)` inside a media query, because CSS does not allow variables there.

## 120: What is Preflight and how does it affect responsive design?

Preflight is Tailwind's base reset. It removes default margins, sets `box-sizing: border-box` on everything, and makes images and videos `display: block` with `max-width: 100%` and `height: auto`. This gives you a consistent start, and the image rules prevent a lot of overflow bugs on mobile.

## 121: Why does box-sizing border-box matter for responsive layouts?

With `border-box`, padding and borders are included in the element's width. A `w-full p-4` box stays exactly 100% wide. With the old `content-box` default, it would be 100% plus padding and would overflow. Preflight sets `border-box` for you.

## 122: How do you make an element fixed to the bottom on mobile only?

```html
<div
  class="fixed inset-x-0 bottom-0 border-t bg-white p-4 md:static md:border-0"
>
  <button class="w-full md:w-auto">Buy now</button>
</div>
```

On mobile the buy bar sticks to the bottom of the screen. From `md` up it goes back to the normal flow.

## 123: What does inset-x-0 do?

`inset-x-0` sets `left: 0` and `right: 0` (in v4 it uses `inset-inline: 0`). On a fixed or absolute element, it makes the element stretch across the full width of its containing block.

## 124: How do you make a modal full screen on mobile and centered on desktop?

```html
<div
  class="fixed inset-0 bg-white md:inset-auto md:top-1/2 md:left-1/2 md:w-full md:max-w-lg md:-translate-x-1/2 md:-translate-y-1/2 md:rounded-xl"
>
  ...
</div>
```

You can also use the native `<dialog>` element and give it the same classes.

## 125: What does z-index have to do with responsive menus?

When a mobile menu opens on top of the page, it needs a higher stacking order than the content so it is not hidden behind it. Use `z-*` utilities, for example `z-50` on the menu and overlay.

## 126: How do you add an overlay behind a mobile menu?

```html
<div class="fixed inset-0 z-40 bg-black/50 md:hidden"></div>
<nav class="fixed inset-y-0 left-0 z-50 w-64 bg-white md:hidden">...</nav>
```

`bg-black/50` is black at 50% opacity.

## 127: How do you make a responsive image gallery?

```html
<div class="grid grid-cols-2 gap-2 sm:grid-cols-3 lg:grid-cols-4">
  <img class="aspect-square w-full object-cover" src="/1.jpg" alt="" />
</div>
```

## 128: How do you handle long words or URLs on narrow screens?

Use `wrap-break-word` (or `wrap-anywhere`). `break-words` still works but is deprecated in newer v4 versions.

```html
<p class="wrap-break-word">
  https://example.com/a/very/long/url/that/would/overflow
</p>
```

## 129: What does break-all do?

`break-all` lets the browser break words at any character to prevent overflow. It works for things like hashes and IDs, but it looks bad for normal text because words split in random places. For normal text, use `wrap-break-word`.

## 130: What does text-balance do?

`text-balance` sets `text-wrap: balance`, which spreads the words more evenly across lines. It is great for headings on mobile, where a title might otherwise end with one lonely word on the last line.

## 131: What does text-pretty do?

`text-pretty` sets `text-wrap: pretty`. The browser tries to avoid a single short word on the last line of a paragraph. It is meant for body text, while `text-balance` is meant for short headings.

## 132: How do you show a short label on mobile and a long label on desktop?

```html
<button>
  <span class="md:hidden">Save</span>
  <span class="hidden md:inline">Save changes</span>
</button>
```

## 133: What are the most common responsive layout patterns?

- Stack to row: columns stack on mobile and sit side by side on desktop.
- Column drop: columns drop below each other one by one as the screen shrinks.
- Off-canvas: a menu or sidebar slides in from the side on mobile.
- Card grid: the number of columns grows with the screen.
- Holy grail: header, footer and a main area with sidebars.

## 134: How do you build a holy grail layout with Tailwind?

```html
<div class="grid min-h-dvh grid-rows-[auto_1fr_auto]">
  <header>Header</header>
  <div class="grid md:grid-cols-[200px_1fr_200px]">
    <nav>Left</nav>
    <main>Main</main>
    <aside>Right</aside>
  </div>
  <footer>Footer</footer>
</div>
```

## 135: How do you use grid-rows for a page layout?

`grid-rows-[auto_1fr_auto]` makes three rows: header at its natural height, the middle row takes the rest of the space, and the footer at its natural height. In arbitrary values, use underscores instead of spaces.

## 136: Why do you use underscores in arbitrary values?

Class names cannot contain spaces, because the space would split them into two classes. Tailwind turns underscores into spaces when it generates the CSS, so `grid-cols-[1fr_2fr]` becomes `grid-template-columns: 1fr 2fr`.

## 137: How do you make a responsive avatar list that overlaps?

```html
<div class="flex -space-x-2 md:-space-x-3">
  <img
    class="size-8 rounded-full ring-2 ring-white md:size-10"
    src="/a.jpg"
    alt=""
  />
  <img
    class="size-8 rounded-full ring-2 ring-white md:size-10"
    src="/b.jpg"
    alt=""
  />
</div>
```

## 138: What does whitespace-nowrap do?

`whitespace-nowrap` stops text from wrapping to the next line. It is useful for short labels in buttons or table headers, but on small screens it can cause overflow, so use it carefully.

## 139: How do you apply styles for very small phones?

Tailwind has no breakpoint below `sm` by default, because unprefixed classes already cover the smallest screens. If you need one, add a custom breakpoint like `--breakpoint-xs: 30rem`, or use `max-sm:` or an arbitrary `max-[360px]:` variant.

## 140: How do you make a responsive badge or chip row that does not overflow?

```html
<div class="flex flex-wrap gap-2">
  <span class="rounded-full bg-blue-100 px-3 py-1 text-xs md:text-sm">Tag</span>
</div>
```

`flex-wrap` lets chips flow to the next line.

## 141: What happens when two classes for the same property have no prefix?

If you write `p-2 p-4`, both apply at the same time, and the one that comes later in the generated CSS wins, not the one written later in the class attribute. So the result is not always what you expect. Do not put two conflicting utilities on the same element at the same breakpoint.

## 142: Does the order of classes in the class attribute matter?

No. The browser uses the order of rules in the CSS file, not the order of class names in HTML. Tailwind generates responsive classes in breakpoint order, so `lg:` rules come after `md:` rules and win at large sizes, no matter how you order the classes in your markup.

## 143: What is the Prettier plugin for Tailwind and does it help with responsive classes?

`prettier-plugin-tailwindcss` sorts your classes in a consistent order, with base classes first and variant classes like `md:` and `lg:` grouped after. It makes long responsive class lists easier to read and review.

## 144: How do you add responsive classes in React or other frameworks?

The same way as in HTML. In React you put them in `className`:

```jsx
export function Card({ children }) {
  return <div className="rounded-lg p-4 md:p-6">{children}</div>;
}
```

Tailwind scans your source files for class names, so any framework works.

## 145: Can you build class names like md:grid-cols-${n}?

No. Tailwind finds classes by scanning your files as plain text. It never runs your code, so a class built from parts at runtime is never seen and its CSS is never generated. Always write full class names:

```js
const cols = { 2: "md:grid-cols-2", 3: "md:grid-cols-3" };
```

## 146: What does inline-block do in a responsive context?

`inline-block` lets an element sit in a line of text but still accept width, height and vertical padding. It is useful for buttons or images inside text that should not take a full row.

## 147: How do you make a two-line clamp on mobile and one line on desktop?

```html
<p class="line-clamp-2 md:line-clamp-1">...</p>
```

This kind of thing is common when the desktop layout has a wide row for the title.

## 148: How do you change font weight at a breakpoint?

```html
<h2 class="font-semibold lg:font-bold">...</h2>
```

## 149: Where does Tailwind write its media queries?

Tailwind collects all the utilities you use and writes them into one CSS file. Responsive utilities are grouped inside media queries and placed after the base utilities, in breakpoint order. In v4 they live inside the `utilities` cascade layer.

## 150: How do you install Tailwind v4 in a Vite project?

```bash
npm install tailwindcss @tailwindcss/vite
```

```js
// vite.config.js
import { defineConfig } from "vite";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  plugins: [tailwindcss()],
});
```

```css
/* src/style.css */
@import "tailwindcss";
```

All the responsive variants are available right away, no config file needed.

# Moderate Questions (151-300)

## 151: How do you add a custom breakpoint in Tailwind v4?

Add a `--breakpoint-*` variable inside `@theme` in your main CSS file:

```css
@import "tailwindcss";

@theme {
  --breakpoint-xs: 30rem;
  --breakpoint-3xl: 120rem;
}
```

Now `xs:` and `3xl:` work like any other breakpoint: `xs:grid-cols-2 3xl:grid-cols-6`.

## 152: How do you change the value of a default breakpoint?

Redefine the same variable in `@theme`:

```css
@theme {
  --breakpoint-2xl: 100rem;
}
```

`2xl:` now starts at 100rem instead of 96rem. Everything else stays the same.

## 153: How do you remove a default breakpoint?

Set it to `initial`:

```css
@theme {
  --breakpoint-2xl: initial;
}
```

After this, `2xl:` classes are no longer generated.

## 154: How do you replace all default breakpoints with your own?

Reset the whole namespace first, then add yours:

```css
@theme {
  --breakpoint-*: initial;
  --breakpoint-tablet: 40rem;
  --breakpoint-laptop: 64rem;
  --breakpoint-desktop: 80rem;
}
```

Now you write `tablet:flex`, `laptop:grid-cols-3` and so on. `sm:`, `md:` and the rest are gone.

## 155: Why should all breakpoints use the same unit?

Tailwind sorts breakpoint variants by their value to decide which media query comes later in the CSS. If you mix `px` and `rem`, the sorting can go wrong and a smaller breakpoint can end up after a larger one, so it wins when it should not. The docs say to use the same unit everywhere, and since the defaults use `rem`, use `rem` for your own too.

## 156: How did you customize breakpoints in Tailwind v3?

In v3 you used `theme.screens` in `tailwind.config.js`:

```js
// tailwind.config.js (v3, legacy)
module.exports = {
  theme: {
    extend: {
      screens: {
        xs: "480px",
        "3xl": "1920px",
      },
    },
  },
};
```

In v4 this moves into CSS with `--breakpoint-*` variables. v4 can still load an old config with `@config "./tailwind.config.js";` while you migrate.

## 157: What are max-* variants?

`max-*` variants apply a style below a breakpoint instead of above it. They are generated for every breakpoint:

| Variant   | Media query              |
| --------- | ------------------------ |
| `max-sm`  | `@media (width < 40rem)` |
| `max-md`  | `@media (width < 48rem)` |
| `max-lg`  | `@media (width < 64rem)` |
| `max-xl`  | `@media (width < 80rem)` |
| `max-2xl` | `@media (width < 96rem)` |

```html
<div class="max-md:hidden">Only visible from 768px up</div>
```

## 158: How do you target a range of screen sizes?

Stack a normal breakpoint with a `max-*` variant:

```html
<div class="md:max-xl:flex">...</div>
```

This applies only from 768px up to (but not including) 1280px.

## 159: How do you target exactly one breakpoint?

Pair the breakpoint with the `max-*` of the next one:

```html
<div class="md:max-lg:bg-yellow-100">Only between md and lg</div>
```

## 160: When should you use max-* instead of mobile-first classes?

Mobile-first should still be the default. Use `max-*` when a style only makes sense on small screens and writing it mobile-first would mean resetting it at a breakpoint. For example `max-md:fixed max-md:inset-0` for a mobile-only overlay is cleaner than `fixed inset-0 md:static md:inset-auto`.

## 161: How do you use an arbitrary breakpoint?

Use `min-[...]` or `max-[...]`:

```html
<div class="min-[320px]:text-center max-[600px]:bg-sky-300">...</div>
```

These are good for one-off fixes. If you use the same value in many places, add it as a named breakpoint instead.

## 162: How did arbitrary breakpoints work in v3?

v3.2 added `min-[...]` and `max-[...]` too, and `max-*` variants like `max-md`. Before that you had to add custom screens with `{ max: "767px" }` objects in the config. The v4 syntax is the same as v3.2, but the generated query uses `width >=` and `width <` range syntax.

## 163: What are container queries?

Container queries let an element change its style based on the size of a parent element, not the whole screen. A card in a narrow sidebar can show a stacked layout, and the same card in a wide main area can show a horizontal layout, without knowing anything about the page.

## 164: How do you use container queries in Tailwind v4?

They are built in. Mark the parent with `@container`, then use `@sm:`, `@md:` and so on on the children:

```html
<div class="@container">
  <div class="flex flex-col @md:flex-row">...</div>
</div>
```

In v3 you needed the `@tailwindcss/container-queries` plugin for this.

## 165: What are the default container query sizes?

| Variant | Min width      |
| ------- | -------------- |
| `@3xs`  | 16rem (256px)  |
| `@2xs`  | 18rem (288px)  |
| `@xs`   | 20rem (320px)  |
| `@sm`   | 24rem (384px)  |
| `@md`   | 28rem (448px)  |
| `@lg`   | 32rem (512px)  |
| `@xl`   | 36rem (576px)  |
| `@2xl`  | 42rem (672px)  |
| `@3xl`  | 48rem (768px)  |
| `@4xl`  | 56rem (896px)  |
| `@5xl`  | 64rem (1024px) |
| `@6xl`  | 72rem (1152px) |
| `@7xl`  | 80rem (1280px) |

They are smaller than screen breakpoints and have different names, because containers are usually smaller than the viewport. Note that `@md` (28rem) is not the same as `md` (48rem).

## 166: What CSS does the @container class generate?

It sets `container-type: inline-size`. This tells the browser to track the element's width so children can query it. The `@md:flex-row` class then becomes `@container (width >= 28rem) { ... }`.

## 167: What is the difference between md: and @md:?

`md:` checks the viewport width (`@media`). `@md:` checks the width of the nearest parent with `@container` (`@container`). They also use different sizes: `md` is 48rem, `@md` is 28rem.

## 168: How do you use max-width container queries?

Use `@max-*`:

```html
<div class="@container">
  <div class="flex flex-row @max-md:flex-col">...</div>
</div>
```

The children switch to a column when the container is narrower than 28rem.

## 169: How do you target a range with container queries?

Stack a min and a max container variant:

```html
<div class="@container">
  <div class="flex flex-row @sm:@max-md:flex-col">...</div>
</div>
```

## 170: What are named containers and when do you need them?

When containers are nested, `@md:` always looks at the nearest container. A named container lets you query a specific one further up:

```html
<div class="@container/main">
  <div class="@container">
    <div class="flex flex-col @lg/main:flex-row">...</div>
  </div>
</div>
```

`@lg/main:` checks the `main` container, not the inner one.

## 171: How do you add a custom container size?

Add a `--container-*` variable in `@theme`:

```css
@theme {
  --container-8xl: 96rem;
}
```

Now `@8xl:` works. The same `--container-*` variables also power `max-w-*` utilities, so `max-w-8xl` works too.

## 172: How do you use an arbitrary container query size?

```html
<div class="@container">
  <div class="flex flex-col @min-[475px]:flex-row @max-[960px]:gap-2">...</div>
</div>
```

## 173: What are container query units and how do you use them?

Container query units are like viewport units but relative to the container. `cqw` is 1% of the container width and `cqi` is 1% of its inline size. Use them as arbitrary values inside an `@container`:

```html
<div class="@container">
  <h2 class="text-[clamp(1rem,6cqi,2rem)]">Card title</h2>
</div>
```

The heading scales with the card, not the screen.

## 174: What does @container-size do?

`@container-size` (added in v4.3) sets `container-type: size`, so the container tracks both width and height. You need it if you want to use height-based units like `cqb` and `cqh`:

```html
<div class="@container-size h-64">
  <div class="h-[50cqb]">Half the container's height</div>
</div>
```

With `size` containment, the container cannot get its height from its content, so you must give it a height yourself.

## 175: When should you use container queries instead of media queries?

Use media queries for page-level layout: the header, the main grid, whether there is a sidebar. Use container queries for reusable components that can end up in places of different widths: cards, widgets, form groups, product tiles. A good rule is "page layout uses `md:`, components use `@md:`".

## 176: Can a container query style the container itself?

No. An element cannot query its own size, because changing its style could change its size and cause a loop. The `@container` class goes on a parent, and the `@md:` classes go on the children. If you need to style the "box" itself, add an inner wrapper.

## 177: What problems can container-type inline-size cause?

`inline-size` containment means the element's width no longer depends on its content. In layouts where the parent's width comes from its children, like an inline-flex item or a flex item with no set width, the container can collapse to zero width. Give the container a width (`w-full`, `flex-1`, a grid cell) so it has a size to measure.

## 178: How do you build a card that changes layout based on its own width?

```html
<div class="@container">
  <article class="flex flex-col gap-4 rounded-xl border p-4 @md:flex-row">
    <img
      class="aspect-video w-full object-cover @md:w-48 @md:aspect-square"
      src="/p.jpg"
      alt=""
    />
    <div>
      <h3 class="text-lg font-semibold @lg:text-xl">Title</h3>
      <p class="line-clamp-2 @lg:line-clamp-none">Description</p>
    </div>
  </article>
</div>
```

This card works in a sidebar, a modal or a full-width list without any changes.

## 179: How do you switch dark mode to a class instead of the system setting?

Override the `dark` variant with `@custom-variant`:

```css
@import "tailwindcss";

@custom-variant dark (&:where(.dark, .dark *));
```

Now `dark:` applies when an ancestor has the `dark` class, and you toggle that class with JavaScript.

## 180: How do you use a data attribute for dark mode?

```css
@custom-variant dark (&:where([data-theme=dark], [data-theme=dark] *));
```

```html
<html data-theme="dark">
  ...
</html>
```

## 181: What does @custom-variant do?

It creates a new variant (or replaces an existing one). You give it a name and a selector or a media query:

```css
@custom-variant short (@media (height < 32rem));
@custom-variant theme-midnight (&:where([data-theme="midnight"] *));
```

```html
<header class="py-6 short:py-2">...</header>
```

## 182: How do you write a custom variant with more than one rule?

Use the block form with `@slot` to mark where the utility goes:

```css
@custom-variant any-hover {
  @media (any-hover: hover) {
    &:hover {
      @slot;
    }
  }
}
```

## 183: How do you create a height-based breakpoint?

Tailwind has no height breakpoints by default. Add one with `@custom-variant`:

```css
@custom-variant tall (@media (height >= 50rem));
@custom-variant short (@media (height < 30rem));
```

```html
<section class="py-8 tall:py-24 short:py-2">...</section>
```

This helps with phones in landscape and small laptop screens.

## 184: How do you use an arbitrary media query without adding a variant?

Use an arbitrary variant with `[@media...]`:

```html
<div class="[@media(height<30rem)]:hidden">...</div>
```

Use this for rare one-off cases. A named `@custom-variant` is easier to read if you use it more than once.

## 185: What do pointer-fine and pointer-coarse do?

They were added in v4.1 and check the main input device:

- `pointer-fine:` applies when the main pointer is precise, like a mouse.
- `pointer-coarse:` applies when the main pointer is imprecise, like a finger on a touch screen.
- `pointer-none:` applies when there is no pointer.

```html
<button class="px-2 py-1 pointer-coarse:px-4 pointer-coarse:py-3">
  Tap me
</button>
```

This is a better way to make touch targets bigger than checking screen width, because a small laptop window can be narrow and a tablet can be wide.

## 186: What is the difference between pointer-* and any-pointer-* variants?

`pointer-*` checks the primary input device only. `any-pointer-*` checks whether any connected input matches. A laptop with a touchscreen has a fine primary pointer but `any-pointer-coarse` is also true. Use `any-pointer-coarse:` if you want to make targets bigger whenever touch is available.

## 187: How do you support the iPhone notch and home bar?

First allow the page to draw under the system UI:

```html
<meta
  name="viewport"
  content="width=device-width, initial-scale=1, viewport-fit=cover"
/>
```

Then add the safe area insets with arbitrary values:

```html
<nav class="fixed inset-x-0 bottom-0 pb-[env(safe-area-inset-bottom)]">...</nav>
<header class="pt-[max(1rem,env(safe-area-inset-top))]">...</header>
```

Tailwind has no built-in safe area utilities, but you can add your own with `@utility`.

## 188: How do you create a custom utility for safe area padding?

```css
@utility pb-safe {
  padding-bottom: env(safe-area-inset-bottom);
}
```

```html
<div class="fixed bottom-0 pb-safe md:pb-0">...</div>
```

Custom utilities made with `@utility` work with all variants, including breakpoints.

## 189: How do you customize the container class in v4?

In v4 the `container` options from v3 (`center`, `padding`) are gone. You extend the utility with `@utility`:

```css
@utility container {
  margin-inline: auto;
  padding-inline: 1rem;

  @variant md {
    padding-inline: 2rem;
  }
}
```

## 190: How did the container class work in v3?

In v3 you configured it in `tailwind.config.js`:

```js
// v3, legacy
module.exports = {
  theme: {
    container: {
      center: true,
      padding: { DEFAULT: "1rem", lg: "2rem" },
    },
  },
};
```

This config is not read by v4 unless you load the old config with `@config`, and even then the `center` and `padding` options for `container` are not supported.

## 191: How do you build a mobile menu with no JavaScript?

Use a `<details>` element:

```html
<details class="relative md:hidden">
  <summary class="cursor-pointer list-none p-2">Menu</summary>
  <nav
    class="absolute right-0 mt-2 flex w-48 flex-col rounded-lg bg-white p-2 shadow-lg"
  >
    <a class="rounded px-3 py-2 hover:bg-gray-100" href="/">Home</a>
    <a class="rounded px-3 py-2 hover:bg-gray-100" href="/docs">Docs</a>
  </nav>
</details>
<nav class="hidden gap-6 md:flex">...</nav>
```

The browser handles open and close, and it is keyboard accessible by default.

## 192: How do you build a mobile menu toggle in React?

```jsx
import { useState } from "react";

export function Navbar() {
  const [open, setOpen] = useState(false);

  return (
    <header className="flex items-center justify-between p-4">
      <a href="/" className="font-bold">
        Logo
      </a>
      <button
        className="md:hidden"
        aria-expanded={open}
        aria-controls="mobile-nav"
        onClick={() => setOpen(!open)}
      >
        Menu
      </button>
      <nav
        id="mobile-nav"
        className={`${open ? "flex" : "hidden"} absolute inset-x-0 top-16 flex-col bg-white p-4 md:static md:flex md:flex-row md:gap-6 md:p-0`}
      >
        <a href="/about">About</a>
        <a href="/blog">Blog</a>
      </nav>
    </header>
  );
}
```

The nav uses `md:flex` so it is always visible on desktop, no matter what the `open` state is.

## 193: How do you build a menu toggle with the peer variant?

Use a hidden checkbox and `peer-checked:`:

```html
<input id="menu" type="checkbox" class="peer sr-only" />
<label for="menu" class="cursor-pointer md:hidden">Menu</label>
<nav class="hidden peer-checked:flex md:flex">...</nav>
```

The `nav` must come after the checkbox and share its parent for `peer` to work. This is a known trick, but a `<button>` with `aria-expanded` is better for accessibility.

## 194: How do you use the has-* variant in responsive layouts?

`has-*` styles a parent based on what is inside it. For example, a layout that becomes two columns only when it contains a sidebar:

```html
<div class="grid md:has-[aside]:grid-cols-[16rem_1fr]">
  <aside>...</aside>
  <main>...</main>
</div>
```

You can also do things like `has-checked:` to style a card when an input inside it is checked.

## 195: How do you build an off-canvas sidebar that slides in on mobile?

```html
<aside
  class="fixed inset-y-0 left-0 z-50 w-72 -translate-x-full bg-white transition-transform data-[open]:translate-x-0 md:static md:translate-x-0"
  data-open
>
  ...
</aside>
```

On mobile the sidebar is moved off screen with `-translate-x-full` and slides in when `data-open` is set. From `md` up it sits in the normal layout. Toggle the `data-open` attribute with JavaScript.

## 196: What is the data-* variant and how does it help with responsive UI?

`data-[state=open]:` or `data-open:` applies styles based on a data attribute. It is cleaner than adding and removing many classes from JavaScript: your code sets one attribute and the CSS does the rest. Headless UI libraries like Radix and Headless UI set data attributes you can style this way.

## 197: How do you make a responsive table that becomes cards on mobile?

```html
<table class="w-full">
  <thead class="hidden md:table-header-group">
    <tr>
      <th>Name</th>
      <th>Email</th>
      <th>Role</th>
    </tr>
  </thead>
  <tbody>
    <tr
      class="mb-4 block rounded-lg border p-4 md:table-row md:border-0 md:p-0"
    >
      <td class="block md:table-cell">
        <span class="font-semibold md:hidden">Name: </span>Ana
      </td>
      <td class="block md:table-cell">
        <span class="font-semibold md:hidden">Email: </span>ana@example.com
      </td>
      <td class="block md:table-cell">
        <span class="font-semibold md:hidden">Role: </span>Admin
      </td>
    </tr>
  </tbody>
</table>
```

Changing `display` on table parts can remove the table meaning for screen readers in some browsers, so test it, or add `role` attributes back if needed.

## 198: How do you make a sticky table header inside a scroll container?

```html
<div class="max-h-96 overflow-auto">
  <table class="w-full">
    <thead class="sticky top-0 bg-white">
      ...
    </thead>
    <tbody>
      ...
    </tbody>
  </table>
</div>
```

## 199: How do you make the first table column sticky when scrolling sideways?

```html
<div class="overflow-x-auto">
  <table class="min-w-[48rem]">
    <tr>
      <th class="sticky left-0 bg-white">Name</th>
      <td>...</td>
    </tr>
  </table>
</div>
```

The first column stays visible while the rest scrolls, which helps people know which row they are looking at.

## 200: How do you create a grid that fits as many columns as possible?

Use `repeat(auto-fill, minmax())` as an arbitrary value:

```html
<div class="grid grid-cols-[repeat(auto-fill,minmax(14rem,1fr))] gap-4">
  ...
</div>
```

The browser fits as many 14rem columns as it can and stretches them to fill the row. You do not need any breakpoints for this.

## 201: What is the difference between auto-fill and auto-fit?

Both fit as many columns as possible. With `auto-fill`, empty tracks stay in the grid, so a row with two items still leaves room for the missing columns. With `auto-fit`, empty tracks collapse, so two items stretch to fill the row. Use `auto-fill` if you want items to keep a steady size, and `auto-fit` if you want them to fill the row.

## 202: How do you add a reusable auto-fill grid utility?

```css
@utility grid-auto-fill-* {
  grid-template-columns: repeat(auto-fill, minmax(--value([length]), 1fr));
}
```

```html
<div class="grid grid-auto-fill-[16rem] gap-4">...</div>
```

Or, more simply, add a theme variable and use it with `grid-cols-(--my-var)`.

## 203: How do you prevent auto-fill grid items from overflowing on very small screens?

If the minimum column size is bigger than the screen, the grid overflows. Use `min()` inside `minmax`:

```html
<div
  class="grid grid-cols-[repeat(auto-fill,minmax(min(16rem,100%),1fr))] gap-4"
>
  ...
</div>
```

On a 300px screen, the column is at most 100% of the grid, so it fits.

## 204: What is subgrid and how do you use it in Tailwind?

Subgrid lets a nested grid use the rows or columns of its parent grid, so items in different cards line up. In Tailwind use `grid-rows-subgrid` or `grid-cols-subgrid`:

```html
<div class="grid gap-6 md:grid-cols-3">
  <article class="row-span-3 grid grid-rows-subgrid">
    <h3>Title</h3>
    <p>Text of any length</p>
    <a href="#">Read more</a>
  </article>
</div>
```

The titles, texts and links line up across all cards in a row, even if the texts have different lengths.

## 205: How do you set a named grid template area layout in Tailwind?

Tailwind has no utilities for `grid-template-areas`, so use arbitrary properties:

```html
<div
  class="grid [grid-template-areas:'header''main''footer'] md:[grid-template-areas:'header_header''sidebar_main''footer_footer'] md:grid-cols-[16rem_1fr]"
>
  <header class="[grid-area:header]">...</header>
  <aside class="hidden md:block [grid-area:sidebar]">...</aside>
  <main class="[grid-area:main]">...</main>
  <footer class="[grid-area:footer]">...</footer>
</div>
```

For complex layouts, a small custom CSS class can be easier to read.

## 206: What are arbitrary properties?

Arbitrary properties let you write any CSS property in brackets: `[mask-type:luminance]`. They work with variants too, like `md:[grid-template-areas:'a_b']`. They are useful when Tailwind has no utility for something.

## 207: How do you make a sticky sidebar inside a two-column layout?

```html
<div class="md:grid md:grid-cols-[16rem_1fr] md:gap-8">
  <aside class="md:sticky md:top-20 md:self-start">Table of contents</aside>
  <article>...</article>
</div>
```

`self-start` is important. Without it, the grid stretches the sidebar to the full row height, and a sticky element that is as tall as its container has nowhere to stick.

## 208: Why does position sticky sometimes not work?

Common reasons:

- A parent has `overflow: hidden`, `overflow: auto` or `overflow: scroll`, which creates a new scroll area.
- No `top`, `bottom` or other offset is set.
- The element is stretched to the full height of its parent (fix with `self-start`).
- The parent is not taller than the sticky element.

## 209: How do you keep a long sidebar scrollable on desktop?

```html
<aside class="md:sticky md:top-0 md:h-dvh md:overflow-y-auto">...</aside>
```

The sidebar sticks to the screen, takes its height, and scrolls on its own when the content is longer.

## 210: How do you lock body scroll when a mobile menu is open?

Add `overflow-hidden` to the `<body>` while the menu is open:

```js
document.body.classList.toggle("overflow-hidden", isOpen);
```

On iOS this was not always enough in the past, which is why some libraries use more complex scroll locks. A native `<dialog>` opened with `showModal()` also makes the rest of the page inert.

## 211: How do you style a native dialog responsively?

```html
<dialog
  class="m-0 mt-auto w-full max-w-none rounded-t-2xl p-6 backdrop:bg-black/50 md:m-auto md:max-w-lg md:rounded-2xl"
>
  ...
</dialog>
```

On mobile it sits at the bottom like a sheet. From `md` up it is centered. The `backdrop:` variant styles the dark area behind it.

## 212: How do you build a bottom navigation bar for mobile?

```html
<nav
  class="fixed inset-x-0 bottom-0 z-40 flex justify-around border-t bg-white pb-[env(safe-area-inset-bottom)] md:hidden"
>
  <a class="flex flex-col items-center p-2 text-xs" href="/">Home</a>
  <a class="flex flex-col items-center p-2 text-xs" href="/search">Search</a>
  <a class="flex flex-col items-center p-2 text-xs" href="/me">Profile</a>
</nav>
<main class="pb-20 md:pb-0">...</main>
```

The extra bottom padding on `main` keeps content from hiding under the bar.

## 213: How do you build responsive tabs that scroll on mobile?

```html
<div class="flex gap-2 overflow-x-auto border-b scrollbar-none">
  <button class="shrink-0 border-b-2 border-blue-600 px-4 py-2">
    Overview
  </button>
  <button class="shrink-0 px-4 py-2">Settings</button>
  <button class="shrink-0 px-4 py-2">Billing</button>
</div>
```

On wide screens all tabs fit. On phones they scroll sideways.

## 214: How do you show a select instead of tabs on mobile?

```html
<select class="block w-full rounded border p-2 md:hidden">
  ...
</select>
<nav class="hidden gap-4 md:flex">...</nav>
```

This is a common pattern in admin dashboards. Keep both in sync from the same data.

## 215: How do you make a responsive multi-column form?

```html
<form class="grid grid-cols-1 gap-4 md:grid-cols-2">
  <label class="flex flex-col gap-1"
    >First name <input class="rounded border p-2"
  /></label>
  <label class="flex flex-col gap-1"
    >Last name <input class="rounded border p-2"
  /></label>
  <label class="flex flex-col gap-1 md:col-span-2"
    >Address <input class="rounded border p-2"
  /></label>
  <button
    class="rounded bg-blue-600 p-2 text-white md:col-start-2 md:justify-self-end md:px-6"
  >
    Save
  </button>
</form>
```

## 216: What is the forms plugin and does it matter for responsive forms?

`@tailwindcss/forms` resets form controls so they are easy to style with utilities. In v4 you load it with `@plugin "@tailwindcss/forms";`. It does not add responsive features itself, but it removes browser default styles that look different on mobile and desktop.

## 217: How do you make typography plugin content responsive?

The typography plugin adds a `prose` class with size modifiers you can change per breakpoint:

```css
@plugin "@tailwindcss/typography";
```

```html
<article class="prose prose-sm md:prose-base lg:prose-lg">...</article>
```

`prose` also sets a max width. Add `max-w-none` if you want it to fill its container.

## 218: How do you define a responsive type scale in @theme?

```css
@theme {
  --text-display: clamp(2rem, 1.2rem + 4vw, 4.5rem);
  --text-display--line-height: 1.1;
}
```

```html
<h1 class="text-display font-bold">Fluid heading</h1>
```

`text-display` now scales with the screen and has its own line height.

## 219: Why mix rem and vw in clamp for font sizes?

If you use only `vw`, the text does not change when the user zooms or changes their font size, which is an accessibility problem. Using something like `1.2rem + 4vw` keeps a `rem` part that grows with the user's settings. WCAG asks that text can be resized to 200%.

## 220: How do you make responsive spacing tokens?

Define CSS variables that change at breakpoints and use them in utilities:

```css
:root {
  --section-gap: 2rem;
}

@media (width >= 64rem) {
  :root {
    --section-gap: 5rem;
  }
}
```

```html
<section class="py-(--section-gap)">...</section>
```

This keeps the class list short when the same responsive spacing is used everywhere.

## 221: How do you change the base spacing unit in v4?

Change the `--spacing` variable:

```css
@theme {
  --spacing: 0.25rem;
}
```

All spacing utilities (`p-4`, `gap-6`, `w-10`) are based on it. You could even change it at a breakpoint with a media query on `:root`, which scales all spacing at once, but that can surprise other developers, so use it carefully.

## 222: What is the difference between @theme and :root variables?

Variables in `@theme` create utilities. `--breakpoint-tablet` creates `tablet:`, `--color-brand` creates `bg-brand`. They are also output as normal CSS variables on `:root`. Variables on `:root` are just CSS variables and do not create any utilities. Use `@theme` for design tokens and `:root` for runtime values.

## 223: How do you use theme variables in JavaScript?

In v4 all theme values are CSS variables, so you can read them at runtime:

```js
const md = getComputedStyle(document.documentElement).getPropertyValue(
  "--breakpoint-md",
);
const isDesktop = window.matchMedia(`(width >= ${md})`).matches;
```

This keeps JavaScript breakpoints in sync with your CSS.

## 224: How do you write a useMediaQuery hook that matches Tailwind breakpoints?

```jsx
import { useSyncExternalStore } from "react";

export function useMediaQuery(query) {
  return useSyncExternalStore(
    (onChange) => {
      const mql = window.matchMedia(query);
      mql.addEventListener("change", onChange);
      return () => mql.removeEventListener("change", onChange);
    },
    () => window.matchMedia(query).matches,
    () => false,
  );
}

// usage
const isDesktop = useMediaQuery("(width >= 48rem)");
```

The third argument is the server value, so this is safe for SSR. Prefer CSS classes when possible and use this only when the logic really needs to change, for example rendering a different component.

## 225: Why should you avoid rendering different components based on screen width in JS?

It causes problems with server-side rendering. The server does not know the screen size, so the first render can be wrong and then jump when JavaScript runs. It also means extra code runs on every resize. Hiding and showing with CSS classes avoids these problems, and you only switch in JS when the two versions are very different.

## 226: How do you avoid a layout flash when using JS breakpoints with SSR?

Render both versions and hide one with CSS (`hidden md:block` and `md:hidden`), or render a neutral layout on the server and only switch after hydration. Do not read `window.innerWidth` during the server render, because it does not exist there.

## 227: How do you handle responsive variants in a component library with cva?

`class-variance-authority` (cva) lets you define variants, and you can pass responsive classes inside them:

```ts
import { cva } from "class-variance-authority";

const button = cva("inline-flex items-center rounded font-medium", {
  variants: {
    size: {
      sm: "px-2 py-1 text-sm",
      md: "px-4 py-2 text-base",
      responsive: "px-3 py-2 text-sm md:px-5 md:py-3 md:text-base",
    },
  },
  defaultVariants: { size: "md" },
});
```

Each class is written in full, so Tailwind can find it.

## 228: What is tailwind-merge and why is it useful with responsive classes?

`tailwind-merge` removes conflicting Tailwind classes, keeping the last one. When a component has `p-4 md:p-6` and the caller passes `md:p-10`, a plain string join would leave both `md:p-6` and `md:p-10`, and the winner would depend on CSS order. `twMerge` understands breakpoints and keeps only `md:p-10`.

```ts
import { twMerge } from "tailwind-merge";

twMerge("p-4 md:p-6", "md:p-10"); // "p-4 md:p-10"
```

## 229: How do you set up a cn helper?

```ts
import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
```

`clsx` handles conditional classes, and `twMerge` removes conflicts. This is the setup shadcn/ui uses.

## 230: How do you make tailwind-merge know about your custom breakpoints?

`tailwind-merge` knows the default breakpoints. Custom variants like `tablet:` are kept, but it treats any prefix as a variant, so conflicts are still merged correctly in most cases. If you add custom utilities or theme scales, configure it with `extendTailwindMerge` so it knows which classes belong to the same group.

## 231: How do you use responsive classes with Next.js Image?

The `fill` mode lets the image fill a sized parent, and `sizes` tells the browser which image width to download:

```jsx
import Image from "next/image";

<div className="relative aspect-video w-full md:w-1/2">
  <Image
    src="/hero.jpg"
    alt="Hero"
    fill
    sizes="(width >= 48rem) 50vw, 100vw"
    className="object-cover"
  />
</div>;
```

The `sizes` value should match your Tailwind layout: full width on mobile, half width from `md`.

## 232: What is srcset and sizes and how do they relate to Tailwind classes?

`srcset` gives the browser several versions of an image at different widths. `sizes` tells it how wide the image will be at different screen widths. Tailwind classes set the actual display size, but the browser decides which file to download before CSS is applied, so `sizes` must describe the same layout your classes produce.

```html
<img
  class="w-full md:w-1/3"
  src="/photo-800.jpg"
  srcset="/photo-400.jpg 400w, /photo-800.jpg 800w, /photo-1600.jpg 1600w"
  sizes="(width >= 48rem) 33vw, 100vw"
  alt=""
/>
```

## 233: How do you build a masonry layout with Tailwind?

The simplest way is CSS columns:

```html
<div class="columns-1 gap-4 sm:columns-2 lg:columns-3">
  <div class="mb-4 break-inside-avoid">...</div>
</div>
```

The downside is that items flow top to bottom in each column, not left to right. For left to right order you need a JavaScript library or the CSS masonry layout once browsers support it widely.

## 234: How do you handle RTL layouts responsively?

Use logical utilities that follow the text direction instead of left and right: `ms-*` and `me-*` for margin, `ps-*` and `pe-*` for padding, `text-start`, `text-end`, and `inset-s-*` and `inset-e-*` for position (the older `start-*` and `end-*` are deprecated in v4.2). They flip automatically when `dir="rtl"` is set. For special cases, use the `rtl:` and `ltr:` variants.

```html
<div class="ps-4 md:ps-8 rtl:text-right">...</div>
```

## 235: What are the block-direction logical utilities added in v4.2?

v4.2 added `pbs-*` and `pbe-*` (padding block start and end), `mbs-*` and `mbe-*` (margin block start and end), `inline-*` and `block-*` for `inline-size` and `block-size`, and `inset-bs-*` and `inset-be-*`. They are useful for layouts that support vertical writing modes, and they work with breakpoints like any other utility.

## 236: How do you add responsive styles in a CSS module or Vue style block?

Those files are processed on their own, so they do not see your theme. Import it with `@reference`:

```vue
<style scoped>
@reference "../app.css";

.title {
  @apply text-xl md:text-3xl;
}
</style>
```

`@reference` makes theme values and variants available without copying the whole CSS into that file.

## 237: How do you test responsive layouts automatically?

Use end-to-end tests that set the viewport size, like Playwright:

```ts
import { test, expect } from "@playwright/test";

test("shows mobile menu button on small screens", async ({ page }) => {
  await page.setViewportSize({ width: 375, height: 800 });
  await page.goto("/");
  await expect(page.getByRole("button", { name: "Menu" })).toBeVisible();
});
```

Visual snapshot tests at a few widths are also good for catching layout breaks.

## 238: Can you test responsive Tailwind classes with Jest or Vitest and jsdom?

Not really. jsdom does not apply CSS layout or media queries, so `md:hidden` has no effect and every element is "visible". You can check that the right classes are present, but to test what the user actually sees at a width, use a real browser like Playwright or Vitest browser mode.

## 239: How do you make Storybook show components at different widths?

Use Storybook's viewport toolbar to switch between preset sizes. You can also set a default viewport per story with parameters. For container-query components, wrap the story in a `div` of a fixed width instead, because the viewport size does not matter to them.

## 240: How do you make a responsive dashboard layout?

```html
<div class="grid min-h-dvh md:grid-cols-[16rem_1fr]">
  <aside class="hidden border-r md:block">Sidebar</aside>
  <div class="flex min-w-0 flex-col">
    <header class="sticky top-0 border-b bg-white p-4">Top bar</header>
    <main class="grid gap-4 p-4 sm:grid-cols-2 xl:grid-cols-4">
      <div class="rounded-lg border p-4">Stat</div>
    </main>
  </div>
</div>
```

`min-w-0` on the right column stops wide charts or tables from pushing the layout wider than the screen.

## 241: How do you make a chart resize with its container?

Most chart libraries need a container with a known size. Give the wrapper a width and an aspect ratio or height:

```html
<div class="aspect-[2/1] w-full md:aspect-[3/1]">
  <canvas id="chart"></canvas>
</div>
```

Then turn on the library's responsive option (for example `responsive: true` in Chart.js or `ResponsiveContainer` in Recharts).

## 242: How do you handle a responsive layout for a page with a fixed header?

Add top padding to the content equal to the header height, and use `scroll-mt-*` so anchor links do not hide headings under the header:

```html
<header class="fixed inset-x-0 top-0 h-14 md:h-20">...</header>
<main class="pt-14 md:pt-20">
  <h2 id="pricing" class="scroll-mt-16 md:scroll-mt-24">Pricing</h2>
</main>
```

Using `sticky` instead of `fixed` avoids the padding problem.

## 243: What is scroll-mt and why is it useful with sticky headers?

`scroll-mt-*` sets `scroll-margin-top`. When you jump to `#section`, the browser leaves that much space above the target. Without it, a sticky header covers the heading you jumped to. You can also set `scroll-pt-*` on the scroll container (often `html`).

## 244: How do you hide content only on print but keep it on screen?

```html
<button class="print:hidden">Print</button>
<p class="hidden print:block">Printed on 2026-10-28</p>
```

## 245: What is the contrast-more variant?

`contrast-more:` applies when the user asks for more contrast in their system settings (`prefers-contrast: more`). You can make borders and text darker for them:

```html
<input class="border-gray-200 contrast-more:border-gray-600" />
```

There is also `contrast-less:`.

## 246: What is the forced-colors variant?

`forced-colors:` applies when the system uses a forced color mode, like Windows High Contrast. In that mode the browser replaces your colors. Use the variant to fix things that break, like custom checkboxes that use background color only:

```html
<span
  class="bg-blue-600 forced-colors:border forced-colors:border-[CanvasText]"
></span>
```

## 247: How do you combine dark mode and breakpoints?

Stack them in any order you like, both are applied:

```html
<div class="bg-white md:bg-gray-50 dark:bg-gray-900 md:dark:bg-gray-800">
  ...
</div>
```

## 248: How does variant stacking order work in v4?

In v4, stacked variants are applied from left to right, like how you would read them as nested CSS. `md:hover:underline` means "inside the md media query, on hover". For media queries the order usually does not change the result, but for things like `*:` and `group-*` it can. v3 applied them right to left, so this is a migration detail.

## 249: How do you apply important to a responsive class in v4?

Put `!` at the end:

```html
<div class="md:hidden!">...</div>
```

In v3 the `!` went right after the variant: `md:!hidden`. v4 still supports the old form, but the new form is preferred. Try not to use important often. It usually means there is a specificity problem you can fix in another way.

## 250: How do you use a prefix with responsive classes in v4?

```css
@import "tailwindcss" prefix(tw);
```

In v4 the prefix looks like a variant and always comes first:

```html
<div class="tw:flex tw:md:grid">...</div>
```

In v3 the prefix came after the variants: `md:tw-grid`.

## 251: What is the * variant and how can it help with responsive layouts?

`*:` applies styles to all direct children:

```html
<ul class="flex flex-col *:p-2 md:flex-row md:*:p-4">
  <li>A</li>
  <li>B</li>
</ul>
```

It saves repeating the same classes on every child, but the children can't easily override those styles, so use it for simple cases.

## 252: How do you style the last item differently on mobile?

```html
<li class="border-b last:border-0 md:border-b-0">...</li>
```

`last:`, `first:`, `odd:`, `even:` and `nth-*:` all combine with breakpoints.

## 253: How do you build a responsive breadcrumb that collapses on mobile?

```html
<nav aria-label="Breadcrumb">
  <ol class="flex items-center gap-2 text-sm">
    <li class="hidden sm:block"><a href="/">Home</a></li>
    <li class="hidden sm:block">/</li>
    <li class="hidden sm:block"><a href="/docs">Docs</a></li>
    <li class="sm:hidden"><a href="/docs">← Back</a></li>
    <li class="hidden sm:block">/</li>
    <li class="truncate font-medium">Current page</li>
  </ol>
</nav>
```

## 254: How do you make a responsive card with an image on top on mobile and on the side on desktop?

```html
<article class="overflow-hidden rounded-xl border sm:flex">
  <img
    class="aspect-video w-full object-cover sm:aspect-auto sm:w-48"
    src="/p.jpg"
    alt=""
  />
  <div class="p-4">
    <h3 class="font-semibold">Title</h3>
    <p class="text-sm text-gray-600">Text</p>
  </div>
</article>
```

On desktop, `sm:aspect-auto` lets the image stretch to the card's height.

## 255: How do you make a responsive comparison layout with sticky labels?

On desktop, use a grid with one label column. On mobile, repeat the labels inside each plan card. Often the simplest approach is to render a table with `overflow-x-auto` and a sticky first column, so users can scroll through the plans while seeing the feature names.

## 256: How do you build a responsive split screen login page?

```html
<div class="grid min-h-dvh lg:grid-cols-2">
  <div class="hidden bg-blue-600 lg:block">Marketing image</div>
  <div class="flex items-center justify-center p-6">
    <form class="w-full max-w-sm space-y-4">...</form>
  </div>
</div>
```

The image side is hidden on smaller screens, so the form gets the full width.

## 257: How do you make a button group that stacks on small screens?

```html
<div class="flex flex-col gap-2 sm:flex-row sm:justify-end">
  <button class="rounded border px-4 py-2">Cancel</button>
  <button class="rounded bg-blue-600 px-4 py-2 text-white">Save</button>
</div>
```

To put the main action first on mobile (closer to the thumb), add `flex-col-reverse` instead of `flex-col`.

## 258: Why would you use flex-col-reverse for buttons on mobile?

On desktop dialogs, the main button usually sits on the right after "Cancel". When the buttons stack on mobile, `flex-col-reverse sm:flex-row` puts the main button on top while keeping the HTML order the same. The focus order still follows the HTML, so make sure that order still makes sense.

## 259: How do visual order changes affect accessibility?

`order-*`, `flex-row-reverse` and grid placement change where things appear but not the DOM order. Screen readers and keyboard focus follow the DOM. If the visual order and DOM order are very different, keyboard users see focus jump around. WCAG asks that the reading and focus order makes sense, so only reorder when the order does not change meaning.

## 260: How do you hide something visually on desktop but keep it for screen readers?

```html
<span class="md:sr-only">Search</span>
```

The label shows on mobile and is visually hidden but still read aloud from `md` up.

## 261: Is it a good idea to remove content on mobile?

Usually not. People on phones often want the same content as desktop users. It is better to reorganize the content (collapse it, put it in tabs, move it lower) than to hide it with `hidden`. Hide only things that really do not make sense on small screens, like hover-only previews or large decorative images.

## 262: How do you make an accordion that is open on desktop and collapsible on mobile?

You can use `<details>` and set it open, then hide the summary on desktop:

```html
<details open class="group">
  <summary class="cursor-pointer md:pointer-events-none md:list-none">
    Filters
  </summary>
  <div class="mt-2">...</div>
</details>
```

In practice, many teams render the filters panel twice: inside a drawer on mobile, and as a normal sidebar on desktop.

## 263: How do you build a filter sidebar that becomes a drawer on mobile?

```html
<button class="md:hidden" data-open-filters>Filters</button>
<aside
  class="fixed inset-0 z-50 hidden bg-white p-4 data-open:block md:static md:block md:w-64 md:p-0"
>
  ...
</aside>
```

The same element is a full-screen panel on mobile and a sidebar on desktop. JavaScript sets the `data-open` attribute.

## 264: How do you make a responsive search bar that expands on focus?

```html
<input
  class="w-32 rounded-full border px-4 py-2 transition-[width] focus:w-full sm:w-48 sm:focus:w-72"
  type="search"
  placeholder="Search"
/>
```

## 265: How do you check which breakpoint is active while developing?

A common trick is a small fixed badge that only shows during development:

```html
<div
  class="fixed right-2 bottom-2 z-50 rounded bg-black px-2 py-1 text-xs text-white"
>
  <span class="sm:hidden">base</span>
  <span class="hidden sm:inline md:hidden">sm</span>
  <span class="hidden md:inline lg:hidden">md</span>
  <span class="hidden lg:inline xl:hidden">lg</span>
  <span class="hidden xl:inline 2xl:hidden">xl</span>
  <span class="hidden 2xl:inline">2xl</span>
</div>
```

## 266: How do you debug a responsive class that does not work?

1. Check that the class is in a file Tailwind scans and is written in full (not built from parts).
2. Look in DevTools to see if the rule exists in the CSS and if it is crossed out.
3. Check that the viewport meta tag is there.
4. Check if another class for the same property has a higher priority (a later breakpoint, `!`, or a non-Tailwind style).
5. Check that the breakpoint is what you think it is (for example, a custom `--breakpoint-*` overrode it).

## 267: How do you tell Tailwind to scan files it does not find by default?

Tailwind v4 scans your project automatically, but skips things in `.gitignore`, like `node_modules`. Add a source path with `@source`:

```css
@import "tailwindcss";
@source "../node_modules/@my-company/ui";
```

This matters when responsive classes live in a shared UI package.

## 268: How do you force Tailwind to generate classes that are not in your files?

In v4.1 and later, use `@source inline()`:

```css
@source inline("{sm:,md:,lg:,}grid-cols-{1,2,3,4}");
```

This generates `grid-cols-1` to `grid-cols-4` with no prefix and with each of the three breakpoints. It replaces the `safelist` option from v3.

## 269: What is the safelist and how did it work in v3?

In v3, `safelist` in `tailwind.config.js` told Tailwind to always generate certain classes, including with variants:

```js
// v3, legacy
safelist: [{ pattern: /grid-cols-(1|2|3|4)/, variants: ["md", "lg"] }];
```

v4 does not support regex safelists. Use `@source inline()` with brace expansion instead.

## 270: How do you share responsive design tokens across several apps?

Put your `@theme` block in a shared CSS file and import it in each app:

```css
/* packages/design/theme.css */
@theme {
  --breakpoint-xs: 30rem;
  --container-8xl: 96rem;
  --text-display: clamp(2rem, 1.2rem + 4vw, 4.5rem);
}
```

```css
/* apps/web/app.css */
@import "tailwindcss";
@import "@my-company/design/theme.css";
```

## 271: How do you make an element take the remaining viewport height under a header?

```html
<header class="h-16">...</header>
<main class="h-[calc(100dvh-4rem)] overflow-auto">...</main>
```

A flex column on a `h-dvh` wrapper with `flex-1 min-h-0` on `main` is often cleaner, because you do not need to hard-code the header height.

## 272: Why do you need min-h-0 in a flex column?

Flex items have `min-height: auto` by default, so they will not shrink below their content height. If `main` has long content and `flex-1`, it grows past the screen and `overflow-auto` never kicks in. `min-h-0` lets it shrink so it can scroll on its own.

## 273: How do you make an app shell that only scrolls the content area?

```html
<div class="flex h-dvh flex-col">
  <header class="shrink-0 border-b p-4">Header</header>
  <div class="flex min-h-0 flex-1">
    <aside class="hidden w-64 overflow-y-auto border-r md:block">Nav</aside>
    <main class="min-w-0 flex-1 overflow-y-auto p-4">Content</main>
  </div>
</div>
```

## 274: How do you use the starting: variant for a mobile menu animation?

`starting:` sets the styles an element has when it first appears, using `@starting-style`. Combined with `transition`, you can animate something in when it goes from `hidden` to visible:

```html
<nav class="flex flex-col opacity-100 transition-opacity starting:opacity-0">
  ...
</nav>
```

Since v4.1, `transition` also transitions `display`, which makes this kind of animation simpler.

## 275: How do you animate a mobile drawer?

```html
<aside
  class="fixed inset-y-0 left-0 w-72 -translate-x-full transition-transform duration-300 data-open:translate-x-0 motion-reduce:transition-none"
>
  ...
</aside>
```

Animating `transform` is cheap for the browser. `motion-reduce:transition-none` turns the animation off for people who asked for less motion.

## 276: Why animate transform instead of left or width?

Changing `left`, `width` or `height` makes the browser recalculate layout on every frame, which can stutter on slower phones. `transform` and `opacity` can be handled by the GPU without layout, so the animation is smooth.

## 277: What does field-sizing-content do?

`field-sizing-content` sets `field-sizing: content`, so a textarea or input grows with its content. It is useful for chat inputs on mobile where you do not want a fixed size. Browser support is still not universal, so set a sensible `min-h-*` and `max-h-*` as well.

## 278: How do you make a chat layout on mobile?

```html
<div class="flex h-dvh flex-col">
  <header class="shrink-0 border-b p-3">Chat</header>
  <ul class="min-h-0 flex-1 space-y-2 overflow-y-auto p-3">
    ...
  </ul>
  <form
    class="flex shrink-0 gap-2 border-t p-3 pb-[max(0.75rem,env(safe-area-inset-bottom))]"
  >
    <textarea
      class="max-h-40 min-h-10 flex-1 resize-none rounded border p-2 text-base field-sizing-content"
    ></textarea>
    <button>Send</button>
  </form>
</div>
```

Using `h-dvh` helps the input stay above the browser bar. `text-base` on the textarea stops iOS from zooming in on focus.

## 279: How does the on-screen keyboard affect mobile layouts?

When the keyboard opens, the visual viewport gets smaller. Browsers handle this differently. Some shrink the layout viewport too, some don't. The `interactive-widget=resizes-content` value in the viewport meta tag asks the browser to resize the layout when the keyboard appears, which keeps bottom inputs visible in browsers that support it (mainly Chromium).

```html
<meta
  name="viewport"
  content="width=device-width, initial-scale=1, interactive-widget=resizes-content"
/>
```

## 280: How do you make a responsive layout in an email with Tailwind?

Email clients have poor CSS support, and many strip `<style>` tags or media queries. Tailwind classes need to be turned into inline styles with a tool like React Email or Maizzle. Keep email layouts simple: a single column with a max width usually works best, and only add responsive tweaks that fail safely.

## 281: How do you use the supports-* variant?

`supports-[...]` applies styles only when the browser supports a CSS feature:

```html
<div
  class="bg-white supports-[backdrop-filter]:bg-white/60 supports-[backdrop-filter]:backdrop-blur"
>
  ...
</div>
```

This gives a solid background in old browsers and a glass effect in newer ones.

## 282: How do you apply styles when JavaScript is disabled?

v4.1 added a `noscript:` variant that applies when scripting is off (`@media (scripting: none)`):

```html
<nav class="hidden md:flex noscript:flex">...</nav>
```

This lets a mobile menu that depends on JavaScript still show its links when JS is off.

## 283: How do you make a responsive hero image with text on top?

```html
<section class="relative isolate min-h-[60svh] overflow-hidden">
  <img
    class="absolute inset-0 -z-10 size-full object-cover"
    src="/hero.jpg"
    alt=""
  />
  <div class="absolute inset-0 -z-10 bg-black/50"></div>
  <div
    class="mx-auto flex max-w-5xl flex-col justify-end px-4 py-16 text-white md:py-32"
  >
    <h1 class="text-3xl font-bold md:text-6xl">Title</h1>
  </div>
</section>
```

`isolate` creates a new stacking context so `-z-10` stays inside the section.

## 284: What is the difference between svh and dvh for a hero section?

`min-h-dvh` changes height while you scroll, as the browser bar hides and shows, which can make the hero jump. `min-h-svh` stays at the smallest size, so it never jumps and never hides content under the bar. For a hero, `svh` is often the better choice. For an app shell that should always fill the screen, `dvh` is better.

## 285: How do you handle responsive spacing in a design system without hard-coding breakpoints in every component?

Use container queries in components and let the parent page decide the width. Or define a few semantic utilities with `@utility` that include their own breakpoints:

```css
@utility section-padding {
  padding-block: 3rem;

  @variant lg {
    padding-block: 6rem;
  }
}
```

Then components just use `section-padding`.

## 286: How do you write a responsive @utility with a value?

Use `--value()` in a functional utility:

```css
@utility gutter-* {
  padding-inline: calc(var(--spacing) * --value(integer));
}
```

```html
<div class="gutter-4 md:gutter-8">...</div>
```

Functional utilities work with variants just like built-in ones.

## 287: What is the difference between @utility and plain CSS classes?

A class made with `@utility` is a real Tailwind utility. It goes into the `utilities` layer, it is sorted correctly with other utilities, it works with `md:`, `hover:` and every other variant, and it can be used in `@apply`. A plain CSS class does none of that, so `md:my-class` does not exist.

## 288: How do you make a responsive grid where the first item is bigger?

```html
<div class="grid grid-cols-2 gap-4 md:grid-cols-4">
  <div class="col-span-2 row-span-2">Featured</div>
  <div>Item</div>
  <div>Item</div>
  <div>Item</div>
  <div>Item</div>
</div>
```

## 289: How do you fill holes in a grid with items of different sizes?

Use `grid-flow-dense`:

```html
<div class="grid grid-flow-dense grid-cols-2 md:grid-cols-4">...</div>
```

The browser fills empty cells with smaller items that come later. This can change the visual order, so do not use it when order matters.

## 290: How do you make grid rows the same height across columns?

By default, grid items in a row stretch to the tallest item. If you want all rows to be the same height, use `auto-rows-fr`:

```html
<div class="grid auto-rows-fr grid-cols-1 gap-4 md:grid-cols-3">...</div>
```

## 291: How do you push a card's button to the bottom so buttons line up?

Make the card a flex column and use `mt-auto` on the button:

```html
<article class="flex flex-col rounded-lg border p-4">
  <h3>Title</h3>
  <p>Text of different length</p>
  <a class="mt-auto pt-4" href="#">Read more</a>
</article>
```

In a grid row, cards stretch to the same height, and `mt-auto` pushes the link to the bottom.

## 292: How do you build a responsive navbar with a centered logo?

```html
<header class="grid grid-cols-[1fr_auto_1fr] items-center p-4">
  <nav class="hidden gap-4 md:flex">...</nav>
  <button class="md:hidden">Menu</button>
  <a class="font-bold" href="/">Logo</a>
  <div class="flex justify-end">Cart</div>
</header>
```

The two `1fr` columns are equal, so the logo is always in the true center.

## 293: How do you show more columns of a table on bigger screens?

```html
<th class="hidden lg:table-cell">Created</th>
<td class="hidden lg:table-cell">2026-01-01</td>
```

Low-priority columns are hidden on small screens. Use `table-cell`, not `block`, to show them again.

## 294: How do you avoid repeating long responsive class lists?

Options, from best to worst for most cases:

1. Make a component (React, Vue, Blade and so on) and reuse it.
2. Use a loop in your template.
3. Use `cva` or a similar tool for variants.
4. Use `@utility` for small, repeated patterns.
5. Use `@apply` in a CSS class, as a last resort.

## 295: How do you style children based on the parent's breakpoint in a group?

You do not need `group` for breakpoints, because breakpoints are global. `md:` on any element checks the screen. `group` is for state like hover and focus. For "parent size", use container queries.

## 296: How do you build a responsive sidebar that collapses to icons on medium screens?

```html
<aside class="hidden w-16 md:block lg:w-64">
  <a class="flex items-center gap-3 p-3" href="/">
    <svg class="size-6 shrink-0" aria-hidden="true">...</svg>
    <span class="sr-only lg:not-sr-only">Dashboard</span>
  </a>
</aside>
```

Hidden on mobile, icons only on `md`, icons and labels on `lg`. The labels stay available to screen readers.

## 297: How do you make text and images in a section line up to a max-width while the background stays full width?

Put the background on the outer element and the max width on an inner one:

```html
<section class="bg-gray-100">
  <div class="mx-auto max-w-6xl px-4 py-16">...</div>
</section>
```

## 298: How do you make one element break out of a max-width container to full width?

```html
<div class="mx-auto max-w-3xl px-4">
  <p>Text</p>
  <img
    class="relative left-1/2 w-screen max-w-none -translate-x-1/2"
    src="/wide.jpg"
    alt=""
  />
</div>
```

Be careful with `w-screen`, because it can include the scrollbar width and cause horizontal scroll on desktop. A grid layout with named full-width columns is a cleaner way to do this.

## 299: How do you migrate responsive classes from Tailwind v3 to v4?

Run the official upgrade tool:

```bash
npx @tailwindcss/upgrade
```

Most responsive classes stay the same (`md:flex` still works). Things to watch for: breakpoints in `tailwind.config.js` move to `@theme`, the `container` options are gone, `!` moves to the end, the `@tailwindcss/container-queries` plugin is no longer needed, `hover:` now only applies on hover-capable devices, and variants stack left to right.

## 300: What are the browser requirements for Tailwind v4?

Tailwind v4 targets Safari 16.4+, Chrome 111+ and Firefox 128+. It uses modern CSS features like cascade layers, `@property` and `color-mix()`. If you need to support older browsers, stay on v3.4, which is still supported for some time.

# Advanced Questions (301-450)

## 301: How does Tailwind decide the order of responsive rules in the output CSS?

Tailwind sorts utilities by variant first, then by property. Utilities with no variant come first, then each breakpoint in ascending order of its value. That is why `lg:p-8` always beats `md:p-4` at large sizes: both have the same specificity, and the `lg` rule comes later. This sorting is based on the breakpoint values, which is why mixing units can break it.

## 302: Why do all Tailwind utilities have the same specificity, and why does that matter for responsive design?

Every utility is a single class selector, so they all have specificity (0,1,0). Media queries do not add specificity. This means the winner between `p-4` and `md:p-6` is decided only by order in the CSS, which Tailwind controls. If you add your own CSS with higher specificity (like `#id .card`), it beats every responsive utility, and the breakpoints look broken.

## 303: How do cascade layers in Tailwind v4 affect responsive styles?

Tailwind v4 puts its CSS into real cascade layers: `theme`, `base`, `components` and `utilities`. Any CSS outside a layer beats CSS inside a layer, no matter the specificity. So a plain `.card { padding: 1rem; }` in an unlayered stylesheet overrides `md:p-8`. Put your own styles in `@layer components` or `@layer base` if you want utilities to override them.

## 304: What happens when unlayered third-party CSS conflicts with responsive utilities?

Unlayered CSS always wins over layered CSS. If a library ships `.btn { display: inline-block; }` without a layer, `md:hidden` on that button will not work. Fixes: import the library into a layer (`@import "lib.css" layer(components);`), use `!` on the utility, or wrap the element.

## 305: What does Tailwind v4's scanner do with responsive class names?

The Oxide engine scans your source files as plain text and pulls out anything that looks like a possible class name, including variants. For `md:max-xl:grid-cols-3`, it finds the whole token, splits off the variants, checks if they exist, and generates the CSS. It does not understand your code, so strings like `"md:" + size` produce nothing.

## 306: Why can't Tailwind generate classes from a variable breakpoint prop like breakpoint="md"?

Because the class `md:flex` never appears in your source. A component that does `` `${breakpoint}:flex` `` builds the class at runtime, after Tailwind has already built the CSS. The fix is a map of full class names:

```ts
const showAt = {
  sm: "hidden sm:flex",
  md: "hidden md:flex",
  lg: "hidden lg:flex",
} as const;
```

## 307: How would you design a React component API that takes responsive props, like cols={{ base: 1, md: 3 }}?

You need a lookup table with every possible class written out, so Tailwind can find them:

```tsx
const colsMap = {
  base: {
    1: "grid-cols-1",
    2: "grid-cols-2",
    3: "grid-cols-3",
    4: "grid-cols-4",
  },
  md: {
    1: "md:grid-cols-1",
    2: "md:grid-cols-2",
    3: "md:grid-cols-3",
    4: "md:grid-cols-4",
  },
  lg: {
    1: "lg:grid-cols-1",
    2: "lg:grid-cols-2",
    3: "lg:grid-cols-3",
    4: "lg:grid-cols-4",
  },
} as const;

type Cols = 1 | 2 | 3 | 4;
type Responsive = Partial<Record<keyof typeof colsMap, Cols>>;

export function Grid({
  cols,
  children,
}: {
  cols: Responsive;
  children: React.ReactNode;
}) {
  const classes = Object.entries(cols).map(
    ([bp, n]) => colsMap[bp as keyof typeof colsMap][n as Cols],
  );
  return <div className={["grid", ...classes].join(" ")}>{children}</div>;
}
```

The cost is that all these classes end up in your CSS whether you use them or not, so keep the allowed values small. Alternatively, pass a CSS variable and use one class like `grid-cols-(--cols)` with different variables per breakpoint.

## 308: How can CSS variables reduce the number of generated responsive classes?

Instead of generating `md:grid-cols-1` to `md:grid-cols-12`, set variables inline and use a few fixed classes:

```tsx
<div
  className="grid grid-cols-[repeat(var(--cols),minmax(0,1fr))] md:grid-cols-[repeat(var(--cols-md),minmax(0,1fr))]"
  style={{ "--cols": 1, "--cols-md": 3 } as React.CSSProperties}
/>
```

Two classes now handle any column count. The downside is that the values are no longer visible in the class list, and inline styles are harder to override.

## 309: How do you create a responsive variant that depends on both a breakpoint and a theme attribute?

Use `@custom-variant` with nesting:

```css
@custom-variant desktop-dark {
  @media (width >= 64rem) {
    &:where([data-theme="dark"] *) {
      @slot;
    }
  }
}
```

In most cases just stacking `lg:dark:` is enough, but a named variant can make a common combination easier to read.

## 310: What changed about @variant in v4.3?

v4.3 lets you use stacked and compound variants in `@variant`:

```css
.link {
  @variant md:hover {
    text-decoration: underline;
  }

  @variant hover, focus-visible {
    color: var(--color-blue-600);
  }
}
```

Before 4.3, you had to nest one `@variant` inside another.

## 311: Why can't you use var(--breakpoint-md) in a media query?

CSS custom properties are resolved per element, but media queries are evaluated for the whole document before any element is styled. The spec does not allow `var()` in media query conditions. Tailwind gets around this at build time: `@variant md` and `theme(--breakpoint-md)` are replaced with the real value when the CSS is compiled.

## 312: Is the theme() function deprecated in v4?

The docs recommend using CSS variables (`var(--color-blue-500)`) instead of `theme()` wherever possible. The exception is places where variables cannot work, like media queries. There, `theme(--breakpoint-md)` is still the right tool, or `@variant md` which is usually cleaner.

## 313: What is the difference between the media range syntax and min-width?

`@media (width >= 48rem)` and `@media (min-width: 48rem)` mean the same thing. The range syntax is easier to read and can express things like `(48rem <= width < 64rem)` in one condition. It is supported in all browsers that Tailwind v4 supports. One detail: `width < 48rem` is strictly less, so `max-md` and `md` never overlap, while the old v3 `max-width: 767px` style could leave a gap at fractional widths like 767.5px.

## 314: What is the fractional pixel gap problem with max-width breakpoints?

With `max-width: 767px` and `min-width: 768px`, a viewport of 767.5px matches neither, which can happen with browser zoom or high-DPI scaling. Layouts can break at that exact width. Range syntax with `width < 48rem` and `width >= 48rem` has no gap, which is one reason v4's `max-*` variants are safer than old hand-made max-width breakpoints.

## 315: How does browser zoom interact with rem-based breakpoints?

When the user zooms in, CSS pixels get bigger, so the viewport gets narrower in CSS pixels and breakpoints switch to the smaller layout. That happens with both `px` and `rem` breakpoints. The difference shows up when the user changes the default font size in browser settings: `rem` breakpoints (in media queries `rem` is based on the browser default font size) move with it, `px` breakpoints do not.

## 316: In a media query, is rem based on the html font-size you set in CSS?

No. In media queries, `rem` and `em` are based on the browser's initial font size (usually 16px, or what the user set), not on `html { font-size: ... }` from your CSS. So changing the root font size to 62.5% does not move your `rem` breakpoints, but it does change the size of your `rem` utilities. This mismatch is one reason not to change the root font size.

## 317: What WCAG rule relates directly to responsive design?

WCAG 2.1 success criterion 1.4.10 Reflow (level AA) says content must work at a width of 320 CSS pixels without scrolling in two directions, except for things like data tables, maps and diagrams. A 1280px wide screen zoomed to 400% is 320px wide. So your mobile layout is also your high-zoom desktop layout, and it must not hide important features.

## 318: How do you test the 400% zoom reflow requirement?

Set the browser window to 1280px wide and zoom to 400%. The layout should switch to the mobile version with no horizontal scroll for normal content. Check that menus open, sticky headers and footers do not cover most of the screen, and dialogs still fit. Fixed-height sticky elements are a common failure here, because at 400% zoom they take up most of the height.

## 319: How do sticky headers cause accessibility problems at high zoom?

At high zoom, the viewport height in CSS pixels is very small. A sticky header that is 80px high may take half the screen, leaving little room for content. Fixes include making the header non-sticky on short screens with a height variant, or shrinking it:

```css
@custom-variant short (@media (height < 30rem));
```

```html
<header class="sticky top-0 short:static">...</header>
```

## 320: What is WCAG 1.4.4 Resize Text and how does it affect fluid typography?

It says text must be resizable to 200% without losing content or function. If you size text only with `vw`, zooming does not change the size much, because zoom changes the viewport width too. Mixing `rem` into `clamp()` (like `clamp(1rem, 0.8rem + 1vw, 1.5rem)`) keeps zoom working. Check that the max value is large enough that 200% zoom actually makes text bigger.

## 321: How do you compute a clamp() for fluid type between two breakpoints?

Pick a min size at a min viewport and a max size at a max viewport. For 1rem at 20rem viewport and 2rem at 80rem:

- slope = (2 - 1) / (80 - 20) = 1/60, so about 1.667vw (slope x 100)
- intercept = 1 - 20 x (1/60) = 0.667rem

```css
@theme {
  --text-fluid-lg: clamp(1rem, 0.667rem + 1.667vw, 2rem);
}
```

The text is exactly 1rem at 320px, 2rem at 1280px, and scales linearly between them.

## 322: When is a fluid spacing scale a better choice than breakpoint-based spacing?

Fluid spacing avoids sudden jumps and needs fewer classes, which is nice for marketing pages with big sections. Breakpoint-based spacing is easier to reason about and to match to a design file with fixed frames. Many teams use fluid values for large section spacing and headings, and fixed steps for component spacing.

## 323: How does container-type inline-size affect layout performance?

Containment limits how far a layout change spreads. That can help performance, because the browser knows the container's width does not depend on its children. But each container is also a place the browser must re-check queries when its size changes. Thousands of containers in a long list add work. Only put `@container` where something actually queries it.

## 324: Can container queries cause layout loops?

The spec prevents loops by requiring containment. With `inline-size` containment, the container's width cannot depend on its content, so a child changing style cannot change the container width. This is the reason a container cannot size itself from its content, and why containers inside shrink-to-fit parents collapse.

## 325: How do you debug container queries in browser DevTools?

In Chrome and Edge DevTools, elements with `container-type` get a `container` badge in the Elements panel. Clicking it highlights the container on the page. In the Styles pane, rules inside `@container` show the query and a link to the container they matched against, so you can see if a child is querying the container you expected. If an `@md:` rule is crossed out or missing, check the container's actual width in the Computed tab, and check that there is not a closer `@container` in between that the child is querying instead.

## 326: Why can't you query a container's height with the normal @container class?

`@container` sets `container-type: inline-size`, which only tracks the width (inline size). The height still comes from the content, so the browser cannot let children query it without risking a loop. To query or use the height (for example with `cqb` units), use `@container-size`, which sets `container-type: size`. With `size` the container no longer gets any size from its content, so you must give it an explicit height, or it collapses.

## 327: What other side effects does container-type have?

Besides size containment, `container-type` applies style containment, which limits how counters and quotes inside the container affect the rest of the page. The bigger practical side effect is the size containment itself: anything that relied on the element shrinking or growing to fit its content (inline-flex parents, `w-fit`, `auto` grid columns, `float`) can now get a zero or wrong width. These surprises are a good reason to add `@container` on purpose, not on every wrapper.

## 328: How do you handle a component that needs both viewport and container responsiveness?

Use both kinds of variants. The page layout uses viewport breakpoints, and the component uses container breakpoints:

```html
<div class="grid gap-6 lg:grid-cols-[1fr_20rem]">
  <section class="@container">
    <div class="grid gap-4 @2xl:grid-cols-3">...</div>
  </section>
  <aside class="@container">
    <div class="grid gap-4 @2xl:grid-cols-3">...</div>
  </aside>
</div>
```

The same card grid shows three columns in the main area and one column in the sidebar.

## 329: How do you use container queries inside a component library so consumers do not have to add @container?

Put the `@container` on the component's own outer wrapper, and put the query variants on an inner element:

```tsx
export function ProductCard(props: Props) {
  return (
    <div className="@container">
      <article className="flex flex-col gap-3 @md:flex-row">...</article>
    </div>
  );
}
```

The component is self-contained. The wrapper needs a width from its parent, which is usually true for block elements and grid cells.

## 330: How do named containers help when nesting library components?

If a library card uses `@container` and a page also uses `@container`, the card's children always query the card's wrapper. Naming them makes intent clear and avoids surprises:

```html
<div class="@container/page">
  <div class="@container/card">
    <h3 class="text-lg @lg/card:text-xl @5xl/page:tracking-tight">...</h3>
  </div>
</div>
```

Names are just strings, so pick a convention and avoid collisions across teams.

## 331: What are style queries and does Tailwind support them?

Style queries let you query a container's custom property value, like `@container style(--variant: compact)`. Tailwind v4 has no built-in variants for them, but you can make one:

```css
@custom-variant compact (@container style(--density: compact));
```

```html
<div style="--density: compact">
  <div class="p-4 compact:p-2">...</div>
</div>
```

Browser support for style queries on custom properties is good in Chromium and Safari but was limited in Firefox for a long time, so check support before you rely on them.

## 332: How do you support browsers without container query support?

All browsers Tailwind v4 supports already support size container queries, so for v4 projects this is mostly not an issue. If you must support older browsers, design the base (unqueried) style to be the narrow layout. Browsers that do not understand `@container` will show the simple stacked layout, which still works.

## 333: How does Tailwind generate container query variants internally?

Each `@{size}` variant is created from the `--container-*` theme variables. `@md:flex-row` becomes:

```css
@container (width >= 28rem) {
  .\@md\:flex-row {
    flex-direction: row;
  }
}
```

A named one like `@md/main:` becomes `@container main (width >= 28rem)`, and the `@container/main` utility sets `container-type: inline-size; container-name: main;`. Container variants are sorted by size like breakpoints.

## 334: Can you use container queries with @apply?

Yes, variants including container ones work with `@apply`:

```css
.card-body {
  @apply flex flex-col @md:flex-row;
}
```

The element using `.card-body` still needs a parent with `@container`.

## 335: How do you use container query units for a fluid component without media queries?

```html
<div class="@container">
  <div class="p-[clamp(0.75rem,4cqi,2rem)]">
    <h3 class="text-[clamp(1rem,5cqi,1.75rem)]">Title</h3>
  </div>
</div>
```

Padding and font size scale with the card's width. If `cqi` is used without any container, it falls back to the small viewport size, so the component still renders, just based on the screen.

## 336: What is the fallback for container query units with no container?

If there is no ancestor container of the right type, container query units use the small viewport units instead (`cqw` acts like `svw`, `cqh` like `svh`). This is safe but can give surprising results if you forget the `@container`.

## 337: How do you handle a responsive image whose displayed size depends on a container, not the viewport?

The `sizes` attribute only understands viewport media conditions, not containers. Options:

- Estimate `sizes` from the page layout (the container's width at each viewport size).
- Use `sizes="auto"` with `loading="lazy"`. Supporting browsers then use the image's actual laid-out width. Support was still being rolled out, so keep a fallback size list after it: `sizes="auto, (width >= 64rem) 33vw, 100vw"`.

## 338: How do responsive images affect Largest Contentful Paint?

If the LCP element is an image, the browser must find it, choose the source and download it fast. Problems that slow LCP: a hero that is only a CSS background (found late), `loading="lazy"` on the hero, wrong `sizes` causing a too-large download, and hiding the real `<img>` on mobile while showing another one. Use a real `<img>` with correct `srcset` and `sizes`, `fetchpriority="high"`, and no lazy loading for the hero.

## 339: How do you preload a responsive hero image?

```html
<link
  rel="preload"
  as="image"
  imagesrcset="/hero-640.jpg 640w, /hero-1280.jpg 1280w, /hero-1920.jpg 1920w"
  imagesizes="100vw"
  fetchpriority="high"
/>
```

`imagesrcset` and `imagesizes` must match the `<img>` exactly, or the browser downloads the image twice.

## 340: How do responsive layouts cause Cumulative Layout Shift?

Shifts happen when something changes size after it first renders. Common causes in responsive UIs: images without `width` and `height` or `aspect-*`, fonts that swap and change line breaks, ads or embeds without reserved space, and JavaScript that changes layout based on `window.innerWidth` after hydration. Reserve space with `aspect-*` or fixed sizes, and do layout changes with CSS breakpoints instead of JS.

## 341: How does using JavaScript to switch layouts after hydration hurt CLS?

The server renders without knowing the screen size, usually the desktop or mobile version. After hydration, a `useMediaQuery` hook flips to the other version, and the content moves. That shift counts as CLS. Rendering both versions with `hidden md:block` and `md:hidden` avoids the shift, because the right one is visible from the first paint.

## 342: What is the cost of rendering both mobile and desktop versions with hidden?

Both versions are in the HTML, so the page is heavier and the DOM is bigger. Hidden elements with `display: none` are not laid out or painted, so the runtime cost is small, but images inside them may still download, and React still renders and hydrates both. For small parts like nav menus this is fine. For big trees like a full dashboard, consider rendering only one, or loading the other lazily.

## 343: How would you handle a page where mobile and desktop need truly different components?

Decide on the server if you can, using client hints (`Sec-CH-Viewport-Width`) or a device hint from the user agent. Otherwise render a neutral skeleton, then pick the right component after hydration with `matchMedia`. Keep the shared data and state outside both components so switching (for example, rotating a tablet) does not lose user input.

## 344: What are client hints and can they help with responsive SSR?

Client hints are HTTP headers the browser sends with information like `Sec-CH-Viewport-Width` and `Sec-CH-DPR`, after the server asks for them with `Accept-CH`. They are mainly supported in Chromium browsers, and they are not sent on the very first request unless you use `Critical-CH`. They can help pick a layout or image size on the server, but you still need a CSS fallback for browsers that do not send them.

## 345: How do you debug why a breakpoint fires at the wrong width on a real phone?

Check the viewport meta tag first. Then check the device pixel ratio is not confusing you: an iPhone that is 1179 physical pixels wide is 393 CSS pixels wide. Check if browser zoom or the user's font settings changed things. Then use remote debugging (Safari Web Inspector for iOS, `chrome://inspect` for Android) to see the real CSS width and which media queries match.

## 346: How do you handle responsive layouts inside iframes?

Media queries inside an iframe use the iframe's width, not the parent page's width. So a widget embedded in a 400px iframe on a desktop page will use its mobile layout, which is usually what you want. If the iframe has no set width, it may default to 300px. Set the iframe width from the parent, and use `aspect-*` or a resize message from the child to set its height.

## 347: How does a Tailwind setup work in micro frontends with different breakpoints?

If each micro frontend ships its own Tailwind CSS, their breakpoints, preflight and utility names can clash. Use a shared theme package so all apps use the same `--breakpoint-*` values, and use a `prefix()` for apps that must stay isolated. Consider disabling Preflight in embedded apps so they do not reset the host page's styles. Shadow DOM can also isolate styles, but media queries inside it still check the page viewport, so components that may be embedded anywhere should use container queries.

## 348: How do you use Tailwind inside Shadow DOM web components?

Styles must be inside the shadow root, so you inject the compiled Tailwind CSS into each shadow root (for example with constructable stylesheets). Media queries still work because they check the viewport. Theme variables defined on `:root` do not reach inside the shadow root unless you also define them on `:host`. Container queries are often better here, because a web component can be placed anywhere.

## 349: How would you design breakpoints for a design system used by many products?

Keep a small set of named breakpoints in a shared `@theme` file, in `rem`, and do not let each product invent its own. Give components container queries so they do not depend on page breakpoints. Document which breakpoints are for page layout. Add an `xs` only if many products need it. Treat changing a breakpoint value as a breaking change, because it moves layouts everywhere.

## 350: What are the trade-offs of semantic breakpoint names like tablet and desktop?

Names like `tablet:` and `desktop:` are easy to read, but they suggest device types, and devices do not fit neatly. A big phone in landscape can hit `tablet:`, and a small laptop window can be in `tablet:` too. Size names (`sm`, `md`, `lg`) do not promise anything about the device, which is more honest. Whatever you pick, keep the names consistent across the team.

## 351: How do you prevent conflicting classes when a component takes a className prop?

Merge with `tailwind-merge` so the caller's classes win per property and per variant:

```tsx
import { cn } from "@/lib/cn";

export function Card({ className, ...props }: React.ComponentProps<"div">) {
  return <div className={cn("rounded-lg p-4 md:p-6", className)} {...props} />;
}

<Card className="md:p-10" />; // result: "rounded-lg p-4 md:p-10"
```

Without merging, `md:p-6` and `md:p-10` would both be present, and the one later in the CSS wins, not the one the caller wanted.

## 352: How does tailwind-merge handle stacked responsive variants?

It treats the full variant chain as part of the key, and sorts variants that can be reordered. `md:hover:p-2` and `hover:md:p-4` are seen as conflicting in most cases, and only the last one is kept. Arbitrary variants are compared as strings. Check the library docs for edge cases where order changes meaning, like `*:` or `group-*`.

## 353: What is the performance cost of tailwind-merge?

It does string parsing on every render. It is fast and caches results, but in a list of thousands of items that each call `cn()` with different inputs, it can show up in profiles. Options: call it only when a `className` prop is passed, memoize stable combinations, or design components so callers rarely need to override the same properties.

## 354: How do you handle a component that should be responsive to the viewport in one place and fixed in another?

Do not hard-code breakpoint classes inside the component. Either use container queries, or let the caller pass layout classes, or offer a variant prop:

```tsx
const layouts = {
  stacked: "flex-col",
  inline: "flex-row",
  responsive: "flex-col md:flex-row",
};
```

## 355: How do you make a responsive grid with columns that are at least a minimum width but never more than N columns?

Combine `auto-fill` with a max-based minimum:

```html
<div
  class="grid gap-4 [--min:14rem] [--max-cols:4] [--gap:1rem] grid-cols-[repeat(auto-fill,minmax(max(var(--min),calc((100%-(var(--max-cols)-1)*var(--gap))/var(--max-cols))),1fr))]"
>
  ...
</div>
```

The column size is the larger of `--min` and "a quarter of the row minus gaps", so there are never more than four columns. This is a good case for a custom `@utility`, because the class is hard to read.

## 356: How would you put that capped auto-fill grid into a reusable utility?

```css
@utility auto-grid {
  display: grid;
  gap: var(--gap, 1rem);
  grid-template-columns: repeat(
    auto-fill,
    minmax(
      max(
        min(var(--min, 14rem), 100%),
        calc(
          (100% - (var(--max-cols, 4) - 1) * var(--gap, 1rem)) /
            var(--max-cols, 4)
        )
      ),
      1fr
    )
  );
}
```

```html
<div class="auto-grid [--max-cols:3] md:[--min:18rem]">...</div>
```

Callers tune it with CSS variables, and the variables can change at breakpoints. The defaults live in the `var()` fallbacks instead of being declared inside the utility, so a variable set by another class on the same element never fights with the utility's own value.

## 357: How do you make the layout change when the number of items changes, not the width?

Use `has-*` with `:nth-child` or quantity queries:

```html
<ul class="grid gap-4 has-[>:nth-child(4)]:md:grid-cols-2">
  ...
</ul>
```

This grid becomes two columns on `md` only when it has four or more items. Quantity-based layouts are useful for galleries where one or two items should be big.

## 358: How do you style a list differently when it has only one item?

```html
<ul class="grid gap-4 md:grid-cols-3 md:has-[>:only-child]:grid-cols-1">
  ...
</ul>
```

Or on the child: `only:col-span-full`.

## 359: What are the performance concerns with has-*?

`:has()` makes the browser check upward from changed elements, which used to be a concern. Modern engines optimize it well. Problems mostly appear with very broad selectors on big DOMs, like `body:has(...)` that must be re-checked on every change. Keep `has-*` on specific components, not on `html` or `body`, where possible.

## 360: How would you build a responsive layout that adapts to user preference for density?

Use a data attribute and a custom variant, combined with breakpoints:

```css
@custom-variant compact (&:where([data-density="compact"] *));
```

```html
<html data-density="compact">
  <table class="text-sm *:*:py-3 md:*:*:py-4 compact:*:*:py-1">
    ...
  </table>
</html>
```

This keeps density separate from screen size, which is better than assuming small screens always want compact layouts.

## 361: How do you handle foldable devices?

Foldables can have two screen segments. The `horizontal-viewport-segments` and `vertical-viewport-segments` media features, plus the `env(viewport-segment-*)` variables, let you place content on each side. Support is limited to some Chromium builds. In Tailwind you can add a custom variant:

```css
@custom-variant dual-screen (@media (horizontal-viewport-segments: 2));
```

Most apps just treat foldables as a tablet or phone, which works if the layout is fluid.

## 362: How do you handle very wide screens like 3440px ultrawides?

Cap content width so lines stay readable, and decide what to do with the extra space. Options: center the content with `max-w-*`, add an extra column at a custom `3xl` breakpoint, or let some parts (like a data grid or map) use the full width. Avoid stretching text lines across the full screen.

## 363: How do you handle landscape phones?

Landscape phones are wide (often above `md`) but very short (around 350-430px). Width-based breakpoints may give them a desktop layout that does not fit vertically. Add a height or orientation check:

```html
<header class="sticky top-0 py-6 landscape:max-md:py-2 short:static">
  ...
</header>
```

`landscape:max-md:` is a narrow-and-sideways case. A `short:` height variant handles all short screens.

## 364: What is the difference between orientation media queries and aspect-ratio media queries?

`orientation: landscape` is true when width is greater than or equal to height. It switches on keyboard open on Android, because the viewport height shrinks. `aspect-ratio` media queries like `(min-aspect-ratio: 16/9)` give finer control. You can make them variants:

```css
@custom-variant widescreen (@media (aspect-ratio >= 16/9));
```

## 365: How does the on-screen keyboard break orientation variants?

On some Android browsers, opening the keyboard shrinks the layout viewport. A phone in portrait with the keyboard open can then be wider than it is tall, so `landscape:` styles suddenly apply while the user types. Do not use `landscape:` for important layout changes in screens with inputs, or use `interactive-widget=resizes-visual` so the layout viewport stays the same.

## 366: What are the interactive-widget viewport options?

The viewport meta `interactive-widget` key controls what the on-screen keyboard does:

- `resizes-visual` (default in most browsers): only the visual viewport shrinks, layout stays the same.
- `resizes-content`: the layout viewport shrinks, so `dvh` and fixed bottom elements move above the keyboard.
- `overlays-content`: nothing resizes, the keyboard covers content.

Support is mainly in Chromium. Safari ignores it and has its own behavior.

## 367: How do you keep a fixed bottom bar above the keyboard on iOS?

iOS Safari does not resize the layout viewport for the keyboard, so a `fixed bottom-0` bar can be hidden or float strangely. A common approach is to listen to `window.visualViewport` resize and scroll events and move the bar with a transform:

```js
const vv = window.visualViewport;
function update() {
  const offset = window.innerHeight - vv.height - vv.offsetTop;
  bar.style.transform = `translateY(${-offset}px)`;
}
vv.addEventListener("resize", update);
vv.addEventListener("scroll", update);
```

The newer VirtualKeyboard API (`navigator.virtualKeyboard`) helps in Chromium, but not on iOS.

## 368: How does the VirtualKeyboard API work with Tailwind?

In Chromium, you can opt in with `navigator.virtualKeyboard.overlaysContent = true`. The browser then exposes `env(keyboard-inset-height)`, which you can use in arbitrary values:

```html
<form class="fixed inset-x-0 bottom-[env(keyboard-inset-height,0px)]">...</form>
```

Always give a fallback, because other browsers do not support it.

## 369: How do you build a responsive layout that uses the full screen on mobile app-like pages?

Use `h-dvh` for the shell, safe area padding, `overscroll-none` to stop the page bouncing, and keep scrolling inside a content area:

```html
<body class="h-dvh overflow-hidden overscroll-none">
  <div class="flex h-full flex-col pt-[env(safe-area-inset-top)]">
    <main class="min-h-0 flex-1 overflow-y-auto overscroll-contain">...</main>
    <nav class="pb-[env(safe-area-inset-bottom)]">...</nav>
  </div>
</body>
```

## 370: What does overscroll-contain do and why is it useful in mobile UIs?

`overscroll-contain` stops scroll chaining: when you reach the end of a scrollable panel, the page behind it does not start scrolling. It is useful for mobile drawers, modals and chat lists. It also turns off pull-to-refresh inside that element in most browsers.

## 371: How do you handle hover-only interactions for devices that have both touch and mouse?

v4's `hover:` uses `@media (hover: hover)`, which checks the primary input. A touchscreen laptop with a trackpad has `hover: hover`, so hover styles apply, and a tap on the touchscreen may trigger them too. Never put essential info or actions behind hover only. Show them on focus and with a visible button as well, and use `any-pointer-coarse:` to make targets bigger if any touch input is present.

## 372: How do you get the old v3 hover behavior back in v4?

Override the variant:

```css
@custom-variant hover (&:hover);
```

This applies `hover:` on all devices, including touch. You might need this for a migration where sticky hover was expected, but the v4 default is usually better.

## 373: How would you write a responsive focus style that works for keyboard and touch users?

Use `focus-visible:` so the ring shows for keyboard users but not on every tap:

```html
<button
  class="rounded px-4 py-2 outline-none focus-visible:ring-2 focus-visible:ring-blue-600 focus-visible:ring-offset-2"
>
  Save
</button>
```

Do not make focus styles depend on breakpoints. Keyboard users exist on every screen size, including tablets with keyboards.

## 374: How do you make sure touch targets are big enough without changing the visual design?

Expand the hit area with a pseudo-element:

```html
<button
  class="relative size-6 after:absolute after:-inset-2.5 after:content-['']"
>
  <svg class="size-6" aria-hidden="true">...</svg>
</button>
```

The icon stays 24px, but the clickable area is 44px. Watch out for overlapping hit areas between close buttons.

## 375: How do you size touch targets only on coarse pointers?

```html
<button class="p-1 pointer-coarse:p-3">...</button>
```

This is better than tying it to width, since tablets are wide and still use fingers. Note that `pointer-coarse` checks the primary pointer only. Use `any-pointer-coarse:` if you want bigger targets whenever touch is available.

## 376: What problems does 100vw cause on desktop?

`100vw` includes the vertical scrollbar on systems with classic scrollbars (Windows, Linux, and macOS when a mouse is connected). A `w-screen` element is then wider than the visible area and causes a horizontal scrollbar. Use `w-full` on a full-width parent, or use `scrollbar-gutter: stable` and careful layout. Container query units or `100%` are usually the right answer.

## 377: What does scrollbar-gutter stable do and when does it help?

`scrollbar-gutter: stable` reserves space for the scrollbar even when the content does not scroll. This stops the layout from shifting sideways when a page goes from short to long, or when a modal adds `overflow-hidden` to the body. v4.3 added `scrollbar-gutter-*` utilities for it. Put it on `html` if your layout shifts when the scrollbar appears.

## 378: Why does adding overflow-hidden to body for a modal cause a layout shift, and how do you fix it?

When the body stops scrolling, the scrollbar disappears and the page gets wider, so content moves to the right. Fixes: use `scrollbar-gutter: stable` on `html` so space stays reserved, or add padding equal to the scrollbar width while the modal is open. Libraries like Radix do the second for you.

## 379: How does the size of the generated CSS grow with responsive classes?

Each breakpoint only adds CSS for classes you actually use with that breakpoint. So `p-4 md:p-6 lg:p-8` adds three small rules, not three copies of the whole framework. A typical production build stays small (often 10-40kB gzipped) even with heavy responsive use. The real risk is safelisting large ranges with `@source inline()` or lookup maps with many unused values.

## 380: How would you audit unused responsive classes in a big project?

Since Tailwind only generates what it finds in your files, the risk is classes that appear in source but are never rendered: dead code, old branches in maps, commented-out markup. Search the built CSS for classes and check where they come from, use coverage in Chrome DevTools to see unused CSS on key pages, and clean up dead code. Also check that `@source` does not include folders like docs or tests that add classes the app does not use.

## 381: How do you exclude files from Tailwind's scanning?

Use `@source not`:

```css
@import "tailwindcss";
@source not "../src/legacy";
@source not "../docs";
```

Tailwind already ignores files in `.gitignore`, binary files, CSS files and lock files. Since v4.3, `.env` files are ignored too.

## 382: How do you debug which files Tailwind scans?

Run your build with `DEBUG=*` (added in v4.1) to log `@source` directives, discovered files and scanned files. That shows if a shared package with responsive classes is missing from the scan.

## 383: How does Tailwind's JIT model compare to old CSS frameworks for responsive classes?

Old frameworks like Bootstrap ship every class for every breakpoint, so most of the CSS is unused. Tailwind (since v2.1 JIT and v3+ by default) generates only the classes you use, at build time. This makes it practical to support every utility at every breakpoint and every variant combination, which would be impossible to ship upfront.

## 384: What is the risk of very long class lists with many breakpoints?

The CSS stays small, but the HTML grows, and the markup gets hard to read and review. A list like `p-2 sm:p-3 md:p-4 lg:p-6 xl:p-8 2xl:p-10` on dozens of elements is a sign that a design token, a fluid value, or a component should be used instead. HTML compression helps a lot with repeated class names, so the network cost is usually smaller than it looks.

## 385: How do you keep responsive class lists readable in code reviews?

Use the Prettier plugin so the order is consistent. Break long lists over several lines grouped by concern or breakpoint, using `cn()` or template strings. Pull repeated patterns into components. Some teams also use the Tailwind IntelliSense extension to see the CSS on hover, which makes complex variants easier to check.

```tsx
<div
  className={cn(
    "flex flex-col gap-4 p-4",
    "md:flex-row md:gap-8 md:p-8",
    "lg:p-12",
  )}
/>
```

## 386: What lint rules help with responsive Tailwind code?

`eslint-plugin-tailwindcss` (check that the version you use supports v4) and `eslint-plugin-better-tailwindcss` can catch conflicting classes like `p-2 p-4`, unknown classes, and classes that are not sorted. Tailwind IntelliSense in VS Code also warns about conflicts in the editor. A custom lint rule that bans dynamic class building is useful too.

## 387: How do you handle responsive styles that need to be different per tenant in a multi-tenant app?

Put tenant values in CSS variables, set them per tenant on a wrapper, and use utilities that read the variables:

```html
<div style="--brand-gap: 1.5rem; --brand-max: 72rem">
  <main class="mx-auto max-w-(--brand-max) gap-(--brand-gap)">...</main>
</div>
```

Breakpoints themselves cannot come from runtime variables, because media queries are compiled at build time. If tenants need different breakpoints, you need different builds, or container queries.

## 388: Can you change breakpoint values at runtime?

No. Breakpoint values are compiled into the media queries in the CSS file. Changing `--breakpoint-md` at runtime changes the variable value, but not the already written `@media (width >= 48rem)`. If you need runtime-changeable breakpoints, use container queries on a wrapper whose width you control, or generate several CSS builds.

## 389: How do you emulate runtime breakpoints with container queries?

Wrap the app in a container and query it instead of the viewport. Then you can change the wrapper width to preview layouts, for example in a page builder:

```html
<div class="@container/app mx-auto w-[var(--preview-width,100%)]">
  <div class="grid @3xl/app:grid-cols-3">...</div>
</div>
```

A no-code builder can switch "mobile", "tablet" and "desktop" previews by changing `--preview-width`, without an iframe.

## 390: Why do some page builders render previews inside an iframe?

Media queries use the viewport, and the editor's preview pane is only part of the screen. An iframe gives the preview its own viewport, so `md:` and other media queries behave like on a real device. The alternative is to build everything with container queries, which works without iframes but means you cannot use viewport breakpoints in the content.

## 391: How does print layout interact with breakpoints?

When printing, the page width is the paper width (about 8.27 or 8.5 inches minus margins, which is roughly 700-800 CSS pixels). That means `md:` styles usually apply and `lg:` styles usually do not. Do not rely on that. Use `print:` to set the print layout explicitly, and `@page` in your CSS for margins and size.

```css
@page {
  margin: 1.5cm;
}
```

## 392: How do you make a dashboard printable?

Hide navigation and interactive controls with `print:hidden`, switch multi-column grids to one or two columns with `print:grid-cols-1`, remove shadows and backgrounds, and avoid splitting cards with `print:break-inside-avoid`. Charts drawn on canvas may need to be redrawn at print size, which you can do with the `beforeprint` event.

## 393: How do you handle responsive layouts with very long translated text?

German and Finnish words are long, and some languages make text 30-40% longer than English. Test with real translations or pseudo-localization. Avoid fixed widths on buttons and labels, allow wrapping, use `wrap-break-word` and `hyphens-auto` with the right `lang` attribute, and do not depend on text fitting on one line in navigation bars.

## 394: What does hyphens-auto need to work?

`hyphens-auto` lets the browser hyphenate words at line ends, but it only works when the element (or a parent) has a correct `lang` attribute, like `<html lang="de">`, and the browser has hyphenation rules for that language. It is helpful in narrow mobile columns of justified or long-word text.

## 395: How do you handle responsive layouts for vertical writing modes?

Use logical utilities like `inline-*`, `block-*`, `ps-*`, `pbs-*` and `mbe-*` so spacing follows the writing direction. Note that media queries still check physical width, not inline size. Container queries with `inline-size` follow the writing mode, so `@md:` in a vertical writing mode checks the container's height, which makes container queries more useful than media queries here.

## 396: How do you handle RTL in combination with transforms like slide-in drawers?

`-translate-x-full` always moves left, even in RTL. A drawer that should come from the start side needs the opposite direction in RTL:

```html
<aside
  class="fixed inset-y-0 inset-s-0 -translate-x-full rtl:translate-x-full data-open:translate-x-0"
>
  ...
</aside>
```

In v4.2+ `start-0` is deprecated in favor of `inset-s-0`, so use that in new code.

## 397: How do you handle responsive grids in RTL?

Grid and flex follow the text direction automatically: column 1 is on the right in RTL. So `md:grid-cols-[16rem_1fr]` puts the sidebar on the right in RTL, which is usually correct. You only need `rtl:` for things that use physical properties, like `left-*`, `ml-*`, translations, and directional icons that should flip with `rtl:-scale-x-100`.

## 398: What is the impact of Tailwind v4 using @property for some utilities?

v4 registers some custom properties with `@property` (for things like shadows, transforms and gradients), so they have types and initial values. This lets them animate and avoids issues with inheritance. It also means a minimum browser version: older browsers without `@property` support can see broken transforms or shadows, which is one reason v4 needs Safari 16.4+.

## 399: Why does v4 implement translate, scale and rotate with separate properties?

v4 uses the individual `translate`, `scale` and `rotate` CSS properties instead of one combined `transform`. You can change one at a breakpoint without resetting the others: `-translate-x-full md:translate-x-0 scale-95 md:scale-100` works independently. It also means a plain `transform: none` in your own CSS does not reset Tailwind's `translate` utilities, which can surprise people during migration.

## 400: How do you migrate a v3 project that used max-width screens in the config?

In v3 you might have had:

```js
// v3, legacy
screens: { mobile: { max: "639px" }, tablet: { min: "640px", max: "1023px" } }
```

In v4, use built-in `max-*` variants and ranges instead of custom objects: `max-sm:` for mobile, `sm:max-lg:` for tablet. If you really want named variants, make them with `@custom-variant`:

```css
@custom-variant mobile (@media (width < 40rem));
@custom-variant tablet (@media (40rem <= width < 64rem));
```

## 401: What happens to the v3 screens raw option in v4?

v3 allowed `screens: { tall: { raw: "(min-height: 800px)" } }` for any media query. In v4, write it as a custom variant:

```css
@custom-variant tall (@media (height >= 50rem));
```

## 402: What is the cost of many custom variants?

Custom variants do not add CSS by themselves, only when used. The cost is mostly mental: every new variant is one more thing the team must learn. Keep the list short, name them clearly, and document them next to the `@theme` block.

## 403: How does Tailwind sort custom variants relative to breakpoints?

Custom variants are ordered by when they are registered, and Tailwind keeps built-in breakpoints sorted by value. If you stack a custom media variant with a breakpoint and the result looks wrong, check the generated CSS order. For overlapping custom media variants, give them conditions that do not overlap, or the later one in the CSS will win when both match.

## 404: How do you make a custom variant that behaves like a breakpoint and is sorted with them?

Add it as a `--breakpoint-*` theme variable instead of a `@custom-variant`. Breakpoint variables get automatic `min` and `max-*` versions and are sorted with the others:

```css
@theme {
  --breakpoint-xs: 30rem;
}
```

Now `xs:` and `max-xs:` work and sort correctly before `sm`.

## 405: How do JS plugins add responsive variants in v4?

Legacy JavaScript plugins still work in v4 when loaded with `@plugin`. `addVariant` and `matchVariant` from the plugin API are supported:

```js
// my-plugin.js
import plugin from "tailwindcss/plugin";

export default plugin(({ addVariant }) => {
  addVariant("hocus", ["&:hover", "&:focus-visible"]);
});
```

```css
@plugin "./my-plugin.js";
```

For new code, `@custom-variant` in CSS is the preferred way.

## 406: How do you write a matchVariant for arbitrary container widths?

```js
import plugin from "tailwindcss/plugin";

export default plugin(({ matchVariant }) => {
  matchVariant("cq", (value) => `@container (width >= ${value})`, {
    values: { card: "22rem", panel: "40rem" },
  });
});
```

Now `cq-card:` and `cq-[30rem]:` work. In v4 this is mostly not needed, because `@min-[...]` already covers arbitrary container sizes.

## 407: How would you build an "only on this breakpoint" family of variants?

You can define them with `@custom-variant` using ranges:

```css
@custom-variant only-sm (@media (40rem <= width < 48rem));
@custom-variant only-md (@media (48rem <= width < 64rem));
@custom-variant only-lg (@media (64rem <= width < 80rem));
```

Or just teach the team to use `md:max-lg:`, which is built in. The built-in form is usually better, because it uses the theme values and updates when breakpoints change.

## 408: How would you design a responsive layout system for a CMS where editors pick the layout?

Give editors a small set of named layouts (like "two columns", "featured grid", "sidebar left"), not free column numbers per breakpoint. Map each layout to a full set of classes in code, so Tailwind can find them. For each block, use container queries so the block looks right in any slot. This keeps the generated CSS small and avoids editors creating layouts that break on mobile.

## 409: How do you handle a third-party widget that uses its own media queries?

You cannot change its breakpoints, but you can control the space it gets. Wrap it in a container with `max-w-*` and `overflow-x-auto` so it cannot break your layout. If it uses viewport media queries, it may show a desktop layout inside a narrow sidebar; an iframe can fix that by giving it its own viewport.

## 410: How do you deal with a design that has a breakpoint at 900px?

Ask if it really needs a new breakpoint or if the content just needs a fluid fix. If it is used once, use `min-[900px]:`. If it is used in many places, add it to the theme, preferably in `rem` (56.25rem), and give it a clear name. Do not change `md` or `lg` to 900px without checking everywhere they are used.

## 411: How do you convert a pixel-perfect desktop-only design to a responsive Tailwind layout?

Start by finding the layout structure: which parts are columns, which are rows, what stacks. Build the mobile version first with no prefixes, then add `md:` and `lg:` changes to reach the desktop design. Replace fixed widths with `max-w-*` and fractions. Agree with the designer on what happens to things that do not fit on mobile, like wide tables and side-by-side images, before writing code.

## 412: What questions should you ask a designer when they give you only desktop and mobile mockups?

- What happens between the two sizes, especially at 768-1024px?
- Which elements hide, move or collapse on mobile?
- How should wide tables and charts behave on small screens?
- What happens with very long text, missing images, and many items?
- Are touch target sizes and font sizes on mobile final?
- What is the max content width on very large screens?

## 413: How would you fix a layout that looks fine at 375px and 1440px but breaks at 820px?

The in-between size is often an iPad or a narrow laptop window. Common causes: a `md:` grid with too many columns for 820px, fixed-width sidebars that leave little space for content, or text that does not wrap. Fixes: move the column change to `lg:`, use `minmax()` or `auto-fill` grids, add `min-w-0` to flex children, or use container queries so components adapt to the space they actually have.

## 414: A flex child with a long code block causes horizontal scroll on mobile. How do you fix it?

The flex item has `min-width: auto`, so the `<pre>` forces it wider than the screen. Add `min-w-0` to the flex item and `overflow-x-auto` to the `<pre>`:

```html
<div class="flex gap-4">
  <aside class="hidden w-64 shrink-0 md:block">...</aside>
  <article class="min-w-0 flex-1">
    <pre class="overflow-x-auto">...</pre>
  </article>
</div>
```

The same issue happens in grids. There, use `minmax(0,1fr)` instead of `1fr`.

## 415: Why does grid-cols-[1fr_300px] overflow but grid-cols-[minmax(0,1fr)_300px] does not?

`1fr` is really `minmax(auto, 1fr)`, so the column cannot get smaller than its content's minimum width. A long word, a wide image or a table makes it grow past the grid. `minmax(0,1fr)` lets the column shrink to zero, so content wraps or scrolls instead. Tailwind's `grid-cols-3` already uses `repeat(3, minmax(0, 1fr))` for this reason.

## 416: A sticky header works on desktop but not on mobile. What would you check?

Check if a parent gets `overflow-hidden` or `overflow-x-hidden` only on mobile (often added to fix horizontal scroll), because that breaks sticky. Check if the header is inside a wrapper that is only as tall as the header on mobile. Check if a `transform` on a parent changes the containing block. Use `overflow-x-clip` instead of `overflow-x-hidden`, because `clip` does not create a scroll container and does not break sticky.

## 417: What is the difference between overflow-hidden and overflow-clip?

Both hide overflowing content. `overflow-hidden` creates a scroll container (it can still be scrolled with JavaScript), which breaks `position: sticky` for descendants. `overflow-clip` just clips and does not create a scroll container, so sticky children still work against the page. Use `overflow-x-clip` on a wrapper to stop horizontal scroll without breaking sticky headers.

## 418: Users on iOS see a white gap under a fixed bottom bar. What is happening?

Probably the home indicator area. With `viewport-fit=cover`, content draws under it, and without safe-area padding the bar's background stops short or its content sits under the indicator. Add `pb-[env(safe-area-inset-bottom)]` to the bar. Without `viewport-fit=cover`, Safari adds the gap itself, and the page background shows there.

## 419: A full-height mobile layout gets cut off at the bottom in Safari. How do you fix it?

`h-screen` is `100vh`, which on iOS Safari is the large viewport height, taller than the visible area when the toolbar shows. Use `h-dvh` (or `min-h-dvh`) to match the visible area, or `h-svh` if you want it to never be covered. All browsers that Tailwind v4 supports understand these units.

```html
<div class="flex h-dvh flex-col">...</div>
```

Do not put `h-screen` and `h-dvh` on the same element as a fallback. Both set `height`, and which one wins depends on the order Tailwind writes them in the CSS, not the order in your class list.

## 420: How would you write a custom utility that falls back from dvh to vh?

```css
@utility h-app {
  height: 100vh;
  height: 100dvh;
}
```

Browsers that understand `dvh` use the second line, and others keep the first. You only need this if you support browsers older than Tailwind v4's targets, for example in a v3 project.

## 421: Tailwind classes for md: work locally but not in production. What could cause this?

Possible causes:

- The production build scans different files (for example, the shared UI package is in `node_modules` and needs `@source`).
- The classes are built from strings, and in dev they happened to exist elsewhere in the code.
- A CSS minifier or another tool reorders or merges media queries.
- The production page loads an older CSS file from a cache or CDN.
- Third-party CSS that loads only in production overrides the utilities.

## 422: How can a CSS minifier break responsive styles?

Some minifiers merge media queries with the same condition and move them to the end of the file. This can change rule order, so a base utility could end up after a responsive one and win at all sizes. Tailwind v4 already uses Lightning CSS to optimize its output, and an extra minifier usually adds little. If you use one, turn off media query merging and reordering.

## 423: How do you use Tailwind with server components and responsive layouts in Next.js?

Server components cannot use `window` or `matchMedia`, so responsive behavior must come from CSS classes, which is actually the best case for Tailwind. Use breakpoints and container queries in server components, and keep JavaScript-based behavior (like a mobile menu toggle) in small client components. This keeps most of the layout out of the client bundle.

## 424: How would you implement a responsive mega menu?

On desktop, show a wide dropdown panel with columns on hover and focus. On mobile, turn it into a full-screen drawer with accordions. The DOM can be shared:

```html
<li class="group">
  <button aria-expanded="false" class="w-full text-left md:w-auto">
    Products
  </button>
  <div
    class="hidden group-data-open:block md:absolute md:inset-x-0 md:top-full md:grid md:grid-cols-4 md:gap-8 md:p-8"
  >
    ...
  </div>
</li>
```

Make it open on click as well as hover, handle the Escape key, and manage `aria-expanded`. Hover-only menus fail on touch devices and are hard for keyboard users.

## 425: Why shouldn't a desktop menu open only on hover?

Touch devices have no hover, keyboard users cannot hover, and hover menus close when the mouse moves diagonally across a gap. Open on click (and optionally on hover with a delay for mouse users), keep it open on focus, and close on Escape and on outside clicks.

## 426: How do you implement a responsive data table with column priority?

Give each column a priority and hide lower-priority ones at smaller sizes:

```tsx
const priorityClass = {
  1: "",
  2: "hidden md:table-cell",
  3: "hidden lg:table-cell",
} as const;

<th className={priorityClass[col.priority]}>{col.label}</th>;
```

Add a way to see the hidden data, like expanding a row or a "details" view. Hiding data with no way to reach it fails users on mobile.

## 427: How would you make a responsive layout that keeps the scroll position when switching from list to grid?

Switching layout with classes keeps the same DOM, so scroll position usually stays. Problems start when you render a different component for each layout, because the DOM is replaced. Keep one tree and change classes, or save the current visible item and scroll back to it after the switch with `scrollIntoView`.

## 428: How do you implement a virtualized list that is also responsive?

Virtualization libraries need to know item sizes. If the number of columns changes with the width, measure the container with a `ResizeObserver`, compute columns from the width (matching your Tailwind breakpoints or a min item width), and pass it to the virtualizer. Container queries alone are not enough, because the virtualizer runs in JavaScript and needs the numbers.

## 429: What is ResizeObserver and when would you use it with Tailwind?

`ResizeObserver` tells you when an element's size changes. Use it when JavaScript needs to know a size: charts, virtualized lists, canvas drawing, or choosing how many items fit. For pure styling, use container queries instead. They do the same job in CSS without JavaScript.

## 430: How would you implement a "show as many tabs as fit, put the rest in a More menu" pattern?

This cannot be done with CSS alone, because you need to know which items fit. Measure the container and item widths with `ResizeObserver`, render the visible items in the bar and the rest in a dropdown. Tailwind handles styling, but the logic is JavaScript. A simpler option is horizontal scrolling with `overflow-x-auto`, which works without measuring.

## 431: How do you use the zoom utilities added in v4.3, and are they a good idea for responsive design?

`zoom-*` utilities set the CSS `zoom` property, which scales an element and its layout. It can be handy for things like scaling a preview or a thumbnail of a component. It is not a good tool for responsive layout, because it scales everything including text, breaks the connection to the user's font settings, and can make text too small to read. Use real layout changes instead.

## 432: What is content-visibility and does it help on mobile?

`content-visibility: auto` lets the browser skip rendering off-screen sections until they are near the viewport. On long pages, this can speed up the first render a lot, which matters most on slower phones. Pair it with `contain-intrinsic-size` so the scrollbar does not jump:

```html
<section class="[content-visibility:auto] [contain-intrinsic-size:auto_800px]">
  ...
</section>
```

## 433: How do you reduce the work done on mobile for heavy desktop-only content?

Do not just hide it with `hidden`. If it is a big component, load it lazily only when the breakpoint matches, for example with `matchMedia` and dynamic `import()`. For images, use `<picture>` with a `media` source so mobile does not download desktop images. For videos, use `preload="none"` and a poster, or show a static image on mobile.

## 434: How do you prevent a hidden desktop video from downloading on mobile?

A `<video>` hidden with `display: none` can still download data, depending on `preload` and `autoplay`. Options: set `preload="none"`, add the `src` with JavaScript only when `matchMedia("(width >= 48rem)")` matches, or use a `<source media="...">` approach (supported again in modern browsers) so only the matching source loads.

## 435: How would you set up visual regression tests for responsive layouts?

Use Playwright or a service like Chromatic to take screenshots at several widths (for example 375, 768, 1024, 1440). Disable animations and use fixed fonts and data so screenshots are stable. Test both the page layouts and the main components, and include container-query components at different wrapper widths. Review diffs carefully, because small font rendering changes between machines can cause noise.

## 436: How do you test container query components in Storybook?

Wrap the story in a container with a set width, and add several stories or a control for the width:

```tsx
export const Narrow = {
  render: () => (
    <div className="w-72 @container">
      <ProductCard {...args} />
    </div>
  ),
};
```

Changing the viewport does nothing for a container-query component, so you must control the wrapper size.

## 437: How do you handle images that need different crops on mobile and desktop (art direction)?

Use `<picture>` with `media` on each `<source>`:

```html
<picture>
  <source
    media="(width >= 64rem)"
    srcset="/team-wide-1600.jpg 1600w, /team-wide-2400.jpg 2400w"
    sizes="100vw"
  />
  <source
    media="(width >= 40rem)"
    srcset="/team-4x3-1200.jpg 1200w"
    sizes="100vw"
  />
  <img
    class="aspect-square w-full object-cover sm:aspect-4/3 lg:aspect-[21/9]"
    src="/team-square-800.jpg"
    alt="Our team"
  />
</picture>
```

Keep the `media` values in sync with your Tailwind breakpoints, and give the `<img>` matching aspect ratios so there is no layout shift.

## 438: How do you avoid CLS with art-directed images that have different aspect ratios?

Set the aspect ratio per breakpoint on the `<img>` with Tailwind classes (`aspect-square sm:aspect-4/3 lg:aspect-[21/9]`), or set `width` and `height` attributes on each `<source>`, which modern browsers use to reserve space. Without one of these, the browser does not know the height until the image loads.

## 439: How do you serve high-DPI images without wasting data?

Use `srcset` with width descriptors (`w`) and a correct `sizes`. The browser picks the right file for the screen's pixel density and the image's display width. Do not use `2x` and `3x` descriptors for images that change size with the layout, because those only work well for fixed-size images like logos. Cap the largest file, because a 3x image on a phone is often not worth the extra data.

## 440: How do you use logical properties to make responsive layouts work in all writing directions?

Prefer `ps-*`, `pe-*`, `ms-*`, `me-*`, `inset-s-*`, `inset-e-*`, `text-start`, `text-end`, `border-s-*`, `rounded-s-*` and the block versions. Use `inline-*` and `block-*` sizes where it makes sense. Combine them with breakpoints as usual. Only physical properties (`left`, `right`, `translate-x`) need `rtl:` overrides.

## 441: How do you handle responsive design for Electron or desktop apps with resizable windows?

The same tools work, because a desktop app window is just a viewport. Users resize windows to any size, including very small ones, so define a minimum window size in the app and make the layout work down to it. Container queries are very useful for panels that users can resize inside the app.

## 442: How do you make resizable panels with Tailwind and keep their content responsive?

Use a library like `react-resizable-panels` for the dragging, and make each panel a `@container`. The content inside each panel then adapts to the panel width with `@sm:`, `@md:` and so on. Media queries would not work here, because the window size does not change when you drag a panel.

## 443: How would you structure CSS for a large app to keep responsive overrides predictable?

- Keep almost all responsive styles as utilities in markup.
- Put the few custom classes in `@layer components`, so utilities can override them.
- Use `@utility` for repeated patterns that need variant support.
- Avoid unlayered CSS and IDs.
- Keep breakpoints and container sizes in one shared theme file.
- Use container queries for components and viewport breakpoints for pages.

## 444: How does Tailwind's @layer components interact with responsive utilities?

Classes in `@layer components` come before the `utilities` layer, so any utility, including `md:` ones, overrides them, regardless of specificity. This is exactly what you want: a `.btn` class sets defaults and `md:px-8` on the element can still change them.

```css
@layer components {
  .btn {
    padding: 0.5rem 1rem;
  }
}
```

```html
<button class="btn md:px-8">Save</button>
```

## 445: What is the difference between putting a class in @layer components and making it a @utility?

A class in `@layer components` is plain CSS, so variants like `md:btn` do not exist and it cannot be used in `@apply` as a utility. A `@utility btn` is part of the utilities layer, supports all variants, and is sorted with other utilities. Use `@layer components` for bigger component classes you want utilities to override, and `@utility` for small single-purpose helpers.

## 446: In a code review, a teammate uses useMediaQuery to hide a sidebar. What would you suggest?

Ask if CSS can do it. `hidden lg:block` hides the sidebar without JavaScript, works with SSR, avoids a flash or layout shift, and has no resize listener. Keep `useMediaQuery` only for cases where the component tree really needs to be different, or where JavaScript needs the value, like choosing the number of items to load.

## 447: How would you explain to a junior developer why their layout breaks on phones?

Walk through it in DevTools at a 375px width. Usually the cause is one of: they wrote desktop styles without prefixes and phone styles with `sm:` (backwards), they used fixed widths, a flex or grid child cannot shrink (`min-w-0` missing), or long words and images overflow. Show the mobile-first rule: no prefix means phone, prefixes add changes for bigger screens.

## 448: What would you include in a team guide for responsive Tailwind code?

- Mobile-first: unprefixed classes for the smallest screen, prefixes for changes.
- The list of breakpoints and container sizes, and when to use each.
- Page layout uses `md:`/`lg:`, components use `@container` and `@md:`.
- No dynamic class names, use full class maps.
- Use `min-h-dvh` instead of `h-screen` for full-height layouts.
- Touch targets at least 44px, use `pointer-coarse:` when needed.
- Test at 320px, a tablet width, and a large desktop, plus 200% and 400% zoom.
- Use `cn()` with `tailwind-merge` in components that accept `className`.

## 449: How would you build a responsive layout for a product page from scratch, step by step?

1. Write the HTML in a sensible reading order: title, price, images, buy button, details.
2. Style the mobile layout with no prefixes: one column, full-width gallery with scroll snap, sticky buy bar at the bottom.
3. At `md:`, put the gallery and details side by side with a grid like `md:grid-cols-2`.
4. At `lg:`, make the details column sticky and widen the max width.
5. Use container queries in reusable parts like review cards and related product tiles.
6. Add correct `srcset` and `sizes` for the gallery, and `fetchpriority="high"` on the first image.
7. Test at several widths, at high zoom, on a real phone, and with long product names.

```html
<main
  class="mx-auto max-w-7xl md:grid md:grid-cols-2 md:gap-8 md:px-6 lg:gap-12"
>
  <div
    class="flex snap-x snap-mandatory overflow-x-auto md:grid md:snap-none md:gap-4 md:overflow-visible"
  >
    <img
      class="aspect-square w-full shrink-0 snap-center object-cover"
      src="/p1.jpg"
      alt=""
      fetchpriority="high"
    />
  </div>
  <section class="p-4 md:sticky md:top-8 md:self-start md:p-0">
    <h1 class="text-2xl font-bold text-balance lg:text-3xl">Product name</h1>
    <p class="mt-2 text-xl">$49</p>
    <div
      class="fixed inset-x-0 bottom-0 border-t bg-white p-4 pb-[max(1rem,env(safe-area-inset-bottom))] md:static md:mt-6 md:border-0 md:p-0"
    >
      <button class="w-full rounded-lg bg-black py-3 text-white">
        Add to cart
      </button>
    </div>
  </section>
</main>
```

## 450: What are the most common mistakes people make when building responsive UIs with Tailwind?

- Using `sm:` for mobile styles instead of unprefixed classes.
- Building class names dynamically, so the CSS is never generated.
- Fixed pixel widths that overflow small screens.
- Forgetting `min-w-0` on flex and grid children with long content.
- Using `h-screen` on mobile instead of `h-dvh` or `h-svh`.
- Hiding images with `hidden` and thinking they will not download.
- Putting important actions behind hover only.
- Using viewport breakpoints for reusable components that should use container queries.
- Changing visual order in ways that confuse keyboard and screen reader users.
- Testing only at a couple of device sizes and not in between, or not with zoom.
