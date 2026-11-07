# Tailwind CSS Interview Questions and Answers

_Last updated: October 28, 2026_

These questions cover Tailwind CSS v4 (the current major version, up to v4.3). Where something changed from v3, the answer says so, since many interviewers still ask about the differences.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is Tailwind CSS?](#1-what-is-tailwind-css)
- [2: What does "utility-first" mean?](#2-what-does-utility-first-mean)
- [3: What is the latest major version of Tailwind CSS and what changed in it?](#3-what-is-the-latest-major-version-of-tailwind-css-and-what-changed-in-it)
- [4: How is Tailwind different from Bootstrap?](#4-how-is-tailwind-different-from-bootstrap)
- [5: How do you install Tailwind CSS v4 with Vite?](#5-how-do-you-install-tailwind-css-v4-with-vite)
- [6: What does `@import "tailwindcss";` do?](#6-what-does-import-tailwindcss-do)
- [7: Do you still need a `tailwind.config.js` file in v4?](#7-do-you-still-need-a-tailwindconfigjs-file-in-v4)
- [8: How do you install Tailwind with PostCSS in v4?](#8-how-do-you-install-tailwind-with-postcss-in-v4)
- [9: How do you use the Tailwind CLI in v4?](#9-how-do-you-use-the-tailwind-cli-in-v4)
- [10: Can you use Tailwind from a CDN?](#10-can-you-use-tailwind-from-a-cdn)
- [11: How does Tailwind know which classes to generate?](#11-how-does-tailwind-know-which-classes-to-generate)
- [12: Why is the final CSS file small even though Tailwind has thousands of utilities?](#12-why-is-the-final-css-file-small-even-though-tailwind-has-thousands-of-utilities)
- [13: What is Preflight?](#13-what-is-preflight)
- [14: Why do my `<h1>` and `<ul>` look like plain text after adding Tailwind?](#14-why-do-my-h1-and-ul-look-like-plain-text-after-adding-tailwind)
- [15: How do you add padding in Tailwind?](#15-how-do-you-add-padding-in-tailwind)
- [16: How do you add margin?](#16-how-do-you-add-margin)
- [17: How does the spacing scale work in v4?](#17-how-does-the-spacing-scale-work-in-v4)
- [18: How do you add negative margin?](#18-how-do-you-add-negative-margin)
- [19: How do you set the text color?](#19-how-do-you-set-the-text-color)
- [20: How do you set the background color?](#20-how-do-you-set-the-background-color)
- [21: What color shades are available in the default palette?](#21-what-color-shades-are-available-in-the-default-palette)
- [22: What color format does v4 use for the default palette?](#22-what-color-format-does-v4-use-for-the-default-palette)
- [23: How do you change the opacity of a color?](#23-how-do-you-change-the-opacity-of-a-color)
- [24: Are `bg-opacity-*` and `text-opacity-*` still available in v4?](#24-are-bg-opacity--and-text-opacity--still-available-in-v4)
- [25: How do you set the font size?](#25-how-do-you-set-the-font-size)
- [26: How do you set font weight?](#26-how-do-you-set-font-weight)
- [27: How do you set the font family?](#27-how-do-you-set-the-font-family)
- [28: How do you set line height?](#28-how-do-you-set-line-height)
- [29: How do you set letter spacing?](#29-how-do-you-set-letter-spacing)
- [30: How do you align text?](#30-how-do-you-align-text)
- [31: How do you make text uppercase, lowercase or capitalized?](#31-how-do-you-make-text-uppercase-lowercase-or-capitalized)
- [32: How do you underline text or remove an underline?](#32-how-do-you-underline-text-or-remove-an-underline)
- [33: How do you truncate long text with an ellipsis?](#33-how-do-you-truncate-long-text-with-an-ellipsis)
- [34: How do you limit text to a set number of lines?](#34-how-do-you-limit-text-to-a-set-number-of-lines)
- [35: How do you make an element a flex container?](#35-how-do-you-make-an-element-a-flex-container)
- [36: How do you change the flex direction?](#36-how-do-you-change-the-flex-direction)
- [37: How do you center something horizontally and vertically with flexbox?](#37-how-do-you-center-something-horizontally-and-vertically-with-flexbox)
- [38: What is the difference between `justify-*` and `items-*`?](#38-what-is-the-difference-between-justify--and-items-)
- [39: What does `justify-between` do?](#39-what-does-justify-between-do)
- [40: How do you make flex items wrap?](#40-how-do-you-make-flex-items-wrap)
- [41: What does `flex-1` do?](#41-what-does-flex-1-do)
- [42: What are `grow` and `shrink` utilities?](#42-what-are-grow-and-shrink-utilities)
- [43: How do you add space between items?](#43-how-do-you-add-space-between-items)
- [44: What is the difference between `gap-*` and `space-x-*`?](#44-what-is-the-difference-between-gap--and-space-x-)
- [45: How do you create a grid layout?](#45-how-do-you-create-a-grid-layout)
- [46: How do you make a grid item span multiple columns?](#46-how-do-you-make-a-grid-item-span-multiple-columns)
- [47: How do you set rows in a grid?](#47-how-do-you-set-rows-in-a-grid)
- [48: What does `place-items-center` do?](#48-what-does-place-items-center-do)
- [49: How do you set the width of an element?](#49-how-do-you-set-the-width-of-an-element)
- [50: How do you set the height?](#50-how-do-you-set-the-height)
- [51: What is the `size-*` utility?](#51-what-is-the-size--utility)
- [52: What is the difference between `h-screen` and `h-dvh`?](#52-what-is-the-difference-between-h-screen-and-h-dvh)
- [53: How do you set max width?](#53-how-do-you-set-max-width)
- [54: How do you set min width and min height?](#54-how-do-you-set-min-width-and-min-height)
- [55: How do you hide an element?](#55-how-do-you-hide-an-element)
- [56: What display utilities does Tailwind have?](#56-what-display-utilities-does-tailwind-have)
- [57: How do you add a border?](#57-how-do-you-add-a-border)
- [58: What is the default border color in v4?](#58-what-is-the-default-border-color-in-v4)
- [59: How do you round corners?](#59-how-do-you-round-corners)
- [60: What changed with the `rounded` and `shadow` names in v4?](#60-what-changed-with-the-rounded-and-shadow-names-in-v4)
- [61: How do you add a shadow?](#61-how-do-you-add-a-shadow)
- [62: How do you change the shadow color?](#62-how-do-you-change-the-shadow-color)
- [63: How do you set opacity of a whole element?](#63-how-do-you-set-opacity-of-a-whole-element)
- [64: How do you apply a style on hover?](#64-how-do-you-apply-a-style-on-hover)
- [65: Does `hover:` always apply when the mouse is over an element in v4?](#65-does-hover-always-apply-when-the-mouse-is-over-an-element-in-v4)
- [66: How do you style focus states?](#66-how-do-you-style-focus-states)
- [67: What is the difference between `focus:` and `focus-visible:`?](#67-what-is-the-difference-between-focus-and-focus-visible)
- [68: How do you style an element when it is being clicked?](#68-how-do-you-style-an-element-when-it-is-being-clicked)
- [69: How do you style disabled elements?](#69-how-do-you-style-disabled-elements)
- [70: How do you make a layout responsive?](#70-how-do-you-make-a-layout-responsive)
- [71: What are the default breakpoints in v4?](#71-what-are-the-default-breakpoints-in-v4)
- [72: What does "mobile-first" mean in Tailwind?](#72-what-does-mobile-first-mean-in-tailwind)
- [73: How do you apply a style only below a breakpoint?](#73-how-do-you-apply-a-style-only-below-a-breakpoint)
- [74: How do you enable dark mode styles?](#74-how-do-you-enable-dark-mode-styles)
- [75: What is the `container` class?](#75-what-is-the-container-class)
- [76: How do you position an element absolutely?](#76-how-do-you-position-an-element-absolutely)
- [77: What does `inset-0` do?](#77-what-does-inset-0-do)
- [78: How do you make a sticky header?](#78-how-do-you-make-a-sticky-header)
- [79: How do you control stacking order?](#79-how-do-you-control-stacking-order)
- [80: How do you make an image cover its container without stretching?](#80-how-do-you-make-an-image-cover-its-container-without-stretching)
- [81: How do you set an aspect ratio?](#81-how-do-you-set-an-aspect-ratio)
- [82: How do you handle overflow?](#82-how-do-you-handle-overflow)
- [83: How do you change the cursor?](#83-how-do-you-change-the-cursor)
- [84: How do you disable mouse events on an element?](#84-how-do-you-disable-mouse-events-on-an-element)
- [85: How do you stop users from selecting text?](#85-how-do-you-stop-users-from-selecting-text)
- [86: How do you add a transition?](#86-how-do-you-add-a-transition)
- [87: What built-in animations does Tailwind have?](#87-what-built-in-animations-does-tailwind-have)
- [88: How do you scale an element?](#88-how-do-you-scale-an-element)
- [89: How do you rotate an element?](#89-how-do-you-rotate-an-element)
- [90: How do you move an element with translate?](#90-how-do-you-move-an-element-with-translate)
- [91: Do you need the `transform` class to use scale, rotate or translate?](#91-do-you-need-the-transform-class-to-use-scale-rotate-or-translate)
- [92: How do you set the transform origin?](#92-how-do-you-set-the-transform-origin)
- [93: How do you add a linear gradient background in v4?](#93-how-do-you-add-a-linear-gradient-background-in-v4)
- [94: Can you set a gradient angle?](#94-can-you-set-a-gradient-angle)
- [95: Does v4 support radial and conic gradients?](#95-does-v4-support-radial-and-conic-gradients)
- [96: How do you add a background image?](#96-how-do-you-add-a-background-image)
- [97: What are `bg-cover` and `bg-contain`?](#97-what-are-bg-cover-and-bg-contain)
- [98: How do you style list bullets?](#98-how-do-you-style-list-bullets)
- [99: What is an arbitrary value?](#99-what-is-an-arbitrary-value)
- [100: How do you use a CSS variable as a value in v4?](#100-how-do-you-use-a-css-variable-as-a-value-in-v4)
- [101: Can you combine variants?](#101-can-you-combine-variants)
- [102: What is the `group` class used for?](#102-what-is-the-group-class-used-for)
- [103: What is the `peer` class used for?](#103-what-is-the-peer-class-used-for)
- [104: What are `first:` and `last:` variants?](#104-what-are-first-and-last-variants)
- [105: What are `odd:` and `even:` variants?](#105-what-are-odd-and-even-variants)
- [106: How do you style the placeholder of an input?](#106-how-do-you-style-the-placeholder-of-an-input)
- [107: What is the default placeholder color in v4?](#107-what-is-the-default-placeholder-color-in-v4)
- [108: How do you add `::before` and `::after` content?](#108-how-do-you-add-before-and-after-content)
- [109: How do you style text selection?](#109-how-do-you-style-text-selection)
- [110: How do you style the file input button?](#110-how-do-you-style-the-file-input-button)
- [111: How do you style a checkbox color without custom CSS?](#111-how-do-you-style-a-checkbox-color-without-custom-css)
- [112: How do you change the text cursor (caret) color?](#112-how-do-you-change-the-text-cursor-caret-color)
- [113: How do you remove the default look of a select or input?](#113-how-do-you-remove-the-default-look-of-a-select-or-input)
- [114: How do you make content visible only to screen readers?](#114-how-do-you-make-content-visible-only-to-screen-readers)
- [115: What is the difference between `outline-none` and `outline-hidden` in v4?](#115-what-is-the-difference-between-outline-none-and-outline-hidden-in-v4)
- [116: How do you add a focus ring?](#116-how-do-you-add-a-focus-ring)
- [117: What is the default `ring` width in v4?](#117-what-is-the-default-ring-width-in-v4)
- [118: How do you add an outline?](#118-how-do-you-add-an-outline)
- [119: How do you add a divider line between children?](#119-how-do-you-add-a-divider-line-between-children)
- [120: How do you add blur to an element?](#120-how-do-you-add-blur-to-an-element)
- [121: What other filter utilities exist?](#121-what-other-filter-utilities-exist)
- [122: What are `whitespace-*` utilities?](#122-what-are-whitespace--utilities)
- [123: How do you break long words that overflow?](#123-how-do-you-break-long-words-that-overflow)
- [124: What do `text-balance` and `text-pretty` do?](#124-what-do-text-balance-and-text-pretty-do)
- [125: How do you style a table?](#125-how-do-you-style-a-table)
- [126: How do you set the color of SVG icons?](#126-how-do-you-set-the-color-of-svg-icons)
- [127: How do you make a full-height page layout?](#127-how-do-you-make-a-full-height-page-layout)
- [128: How do you write a simple card component with Tailwind?](#128-how-do-you-write-a-simple-card-component-with-tailwind)
- [129: How do you build a simple navbar?](#129-how-do-you-build-a-simple-navbar)
- [130: Does the order of classes in the `class` attribute matter?](#130-does-the-order-of-classes-in-the-class-attribute-matter)
- [131: Why shouldn't you build class names with string concatenation?](#131-why-shouldnt-you-build-class-names-with-string-concatenation)
- [132: How do you use Tailwind in React?](#132-how-do-you-use-tailwind-in-react)
- [133: Does Tailwind add JavaScript to your page?](#133-does-tailwind-add-javascript-to-your-page)
- [134: What does `@apply` do?](#134-what-does-apply-do)
- [135: What is the `@theme` directive?](#135-what-is-the-theme-directive)
- [136: How do you add a custom color?](#136-how-do-you-add-a-custom-color)
- [137: Can you use theme values as normal CSS variables?](#137-can-you-use-theme-values-as-normal-css-variables)
- [138: How do you write a CSS comment or custom CSS together with Tailwind?](#138-how-do-you-write-a-css-comment-or-custom-css-together-with-tailwind)
- [139: What is the `!` important modifier?](#139-what-is-the--important-modifier)
- [140: How do you make a column layout like a newspaper?](#140-how-do-you-make-a-column-layout-like-a-newspaper)
- [141: What is `scroll-smooth`?](#141-what-is-scroll-smooth)
- [142: What are `inline-block` and `inline-flex` used for?](#142-what-are-inline-block-and-inline-flex-used-for)
- [143: How do you make a circle avatar?](#143-how-do-you-make-a-circle-avatar)
- [144: How do you set `box-sizing`?](#144-how-do-you-set-box-sizing)
- [145: What does `isolate` do?](#145-what-does-isolate-do)
- [146: How do you hide the scrollbar or make it thin?](#146-how-do-you-hide-the-scrollbar-or-make-it-thin)
- [147: How do you style the placeholder with dark mode at the same time?](#147-how-do-you-style-the-placeholder-with-dark-mode-at-the-same-time)
- [148: What does `contents` display do?](#148-what-does-contents-display-do)
- [149: Which browsers does Tailwind v4 support?](#149-which-browsers-does-tailwind-v4-support)
- [150: Where should you look for official Tailwind documentation and tools?](#150-where-should-you-look-for-official-tailwind-documentation-and-tools)

### Moderate Questions (151-300)

- [151: How does the CSS-first configuration in v4 work?](#151-how-does-the-css-first-configuration-in-v4-work)
- [152: What are theme variable namespaces?](#152-what-are-theme-variable-namespaces)
- [153: How do you extend the theme versus replace it?](#153-how-do-you-extend-the-theme-versus-replace-it)
- [154: How do you override a single default value?](#154-how-do-you-override-a-single-default-value)
- [155: How do you remove a single breakpoint?](#155-how-do-you-remove-a-single-breakpoint)
- [156: How do you add a custom breakpoint?](#156-how-do-you-add-a-custom-breakpoint)
- [157: How do you use an arbitrary breakpoint without adding it to the theme?](#157-how-do-you-use-an-arbitrary-breakpoint-without-adding-it-to-the-theme)
- [158: What is the difference between `@theme` and `:root` variables?](#158-what-is-the-difference-between-theme-and-root-variables)
- [159: Can `@theme` be nested inside a selector or media query?](#159-can-theme-be-nested-inside-a-selector-or-media-query)
- [160: What does `@theme inline` do?](#160-what-does-theme-inline-do)
- [161: What does `@theme static` do?](#161-what-does-theme-static-do)
- [162: How do you add a custom font in v4?](#162-how-do-you-add-a-custom-font-in-v4)
- [163: How do you set a default line height for a custom font size?](#163-how-do-you-set-a-default-line-height-for-a-custom-font-size)
- [164: How do you change the spacing scale?](#164-how-do-you-change-the-spacing-scale)
- [165: How do you define a custom utility in v4?](#165-how-do-you-define-a-custom-utility-in-v4)
- [166: Why use `@utility` instead of `@layer utilities` in v4?](#166-why-use-utility-instead-of-layer-utilities-in-v4)
- [167: How do you add base styles in v4?](#167-how-do-you-add-base-styles-in-v4)
- [168: How do you add component classes in v4?](#168-how-do-you-add-component-classes-in-v4)
- [169: What is `--spacing()` in CSS?](#169-what-is---spacing-in-css)
- [170: What is `--alpha()` in CSS?](#170-what-is---alpha-in-css)
- [171: Is the `theme()` function still supported in v4?](#171-is-the-theme-function-still-supported-in-v4)
- [172: How do you use `@apply` in Vue, Svelte or CSS modules in v4?](#172-how-do-you-use-apply-in-vue-svelte-or-css-modules-in-v4)
- [173: What does `@variant` do?](#173-what-does-variant-do)
- [174: How do you create a custom variant?](#174-how-do-you-create-a-custom-variant)
- [175: How do you make dark mode toggle manually with a class?](#175-how-do-you-make-dark-mode-toggle-manually-with-a-class)
- [176: How do you use a data attribute for dark mode instead of a class?](#176-how-do-you-use-a-data-attribute-for-dark-mode-instead-of-a-class)
- [177: How do you support light, dark and system modes together?](#177-how-do-you-support-light-dark-and-system-modes-together)
- [178: Why does the page flash light before switching to dark?](#178-why-does-the-page-flash-light-before-switching-to-dark)
- [179: What does `scheme-dark` do?](#179-what-does-scheme-dark-do)
- [180: How do you style based on a data attribute?](#180-how-do-you-style-based-on-a-data-attribute)
- [181: How do you style based on ARIA attributes?](#181-how-do-you-style-based-on-aria-attributes)
- [182: What is the `has-*` variant?](#182-what-is-the-has--variant)
- [183: What are `group-has-*` and `peer-has-*`?](#183-what-are-group-has--and-peer-has-)
- [184: What are named groups?](#184-what-are-named-groups)
- [185: What is the `not-*` variant?](#185-what-is-the-not--variant)
- [186: What is the `in-*` variant?](#186-what-is-the-in--variant)
- [187: What are the `*` and `**` variants?](#187-what-are-the--and--variants)
- [188: What are `nth-*` variants?](#188-what-are-nth--variants)
- [189: What are arbitrary variants?](#189-what-are-arbitrary-variants)
- [190: How do you use `supports-*`?](#190-how-do-you-use-supports-)
- [191: How do you style for reduced motion?](#191-how-do-you-style-for-reduced-motion)
- [192: What other accessibility media variants exist?](#192-what-other-accessibility-media-variants-exist)
- [193: How do you style elements based on RTL or LTR direction?](#193-how-do-you-style-elements-based-on-rtl-or-ltr-direction)
- [194: What are logical property utilities?](#194-what-are-logical-property-utilities)
- [195: What happened to `start-*` and `end-*` in v4.2?](#195-what-happened-to-start--and-end--in-v42)
- [196: What are `inline-*` and `block-*` size utilities?](#196-what-are-inline--and-block--size-utilities)
- [197: What are container queries?](#197-what-are-container-queries)
- [198: When should you use container queries instead of breakpoints?](#198-when-should-you-use-container-queries-instead-of-breakpoints)
- [199: How do you use max-width and range container queries?](#199-how-do-you-use-max-width-and-range-container-queries)
- [200: What are named containers?](#200-what-are-named-containers)
- [201: What are the default container query sizes?](#201-what-are-the-default-container-query-sizes)
- [202: What is `@container-size` in v4.3?](#202-what-is-container-size-in-v43)
- [203: How do you use container query units?](#203-how-do-you-use-container-query-units)
- [204: How do you add a custom animation in v4?](#204-how-do-you-add-a-custom-animation-in-v4)
- [205: What is the `starting:` variant?](#205-what-is-the-starting-variant)
- [206: What does `transition-discrete` do?](#206-what-does-transition-discrete-do)
- [207: How do you set an arbitrary transition duration or easing?](#207-how-do-you-set-an-arbitrary-transition-duration-or-easing)
- [208: How do you add a delay to a transition?](#208-how-do-you-add-a-delay-to-a-transition)
- [209: How do you control which properties transition?](#209-how-do-you-control-which-properties-transition)
- [210: What are 3D transform utilities in v4?](#210-what-are-3d-transform-utilities-in-v4)
- [211: How do you make gradient color stops at specific positions?](#211-how-do-you-make-gradient-color-stops-at-specific-positions)
- [212: What are gradient interpolation modifiers?](#212-what-are-gradient-interpolation-modifiers)
- [213: How do you make gradient text?](#213-how-do-you-make-gradient-text)
- [214: What are inset shadows and inset rings?](#214-what-are-inset-shadows-and-inset-rings)
- [215: What are text shadow utilities?](#215-what-are-text-shadow-utilities)
- [216: How do you add a colored drop shadow?](#216-how-do-you-add-a-colored-drop-shadow)
- [217: What are mask utilities?](#217-what-are-mask-utilities)
- [218: How do you style form validation states?](#218-how-do-you-style-form-validation-states)
- [219: What is `field-sizing-content`?](#219-what-is-field-sizing-content)
- [220: What is the `@tailwindcss/forms` plugin?](#220-what-is-the-tailwindcssforms-plugin)
- [221: What is the `@tailwindcss/typography` plugin?](#221-what-is-the-tailwindcsstypography-plugin)
- [222: How do you customize `prose` elements with utilities?](#222-how-do-you-customize-prose-elements-with-utilities)
- [223: Which v3 plugins are built into v4 core?](#223-which-v3-plugins-are-built-into-v4-core)
- [224: How do you load a JavaScript plugin in v4?](#224-how-do-you-load-a-javascript-plugin-in-v4)
- [225: How do you load a v3-style `tailwind.config.js` in v4?](#225-how-do-you-load-a-v3-style-tailwindconfigjs-in-v4)
- [226: How do you tell Tailwind to scan a folder it ignores by default?](#226-how-do-you-tell-tailwind-to-scan-a-folder-it-ignores-by-default)
- [227: How do you stop Tailwind from scanning a folder?](#227-how-do-you-stop-tailwind-from-scanning-a-folder)
- [228: How do you turn off automatic source detection?](#228-how-do-you-turn-off-automatic-source-detection)
- [229: How do you safelist classes in v4?](#229-how-do-you-safelist-classes-in-v4)
- [230: How do you handle dynamic classes from a CMS or API?](#230-how-do-you-handle-dynamic-classes-from-a-cms-or-api)
- [231: How do you pass a dynamic value from JavaScript into a Tailwind class?](#231-how-do-you-pass-a-dynamic-value-from-javascript-into-a-tailwind-class)
- [232: When is a type hint needed in arbitrary values?](#232-when-is-a-type-hint-needed-in-arbitrary-values)
- [233: What are arbitrary properties?](#233-what-are-arbitrary-properties)
- [234: How do you write spaces and underscores in arbitrary values?](#234-how-do-you-write-spaces-and-underscores-in-arbitrary-values)
- [235: How do you add opacity to an arbitrary color or CSS variable?](#235-how-do-you-add-opacity-to-an-arbitrary-color-or-css-variable)
- [236: Why use `@utility` and not just `@layer components` for reusable classes?](#236-why-use-utility-and-not-just-layer-components-for-reusable-classes)
- [237: Can you `@apply` a custom class in v4?](#237-can-you-apply-a-custom-class-in-v4)
- [238: Why is overusing `@apply` considered a bad practice?](#238-why-is-overusing-apply-considered-a-bad-practice)
- [239: How do you reuse styles without `@apply`?](#239-how-do-you-reuse-styles-without-apply)
- [240: How do you set up Tailwind in Next.js with v4?](#240-how-do-you-set-up-tailwind-in-nextjs-with-v4)
- [241: How do you use `next/font` with Tailwind v4?](#241-how-do-you-use-nextfont-with-tailwind-v4)
- [242: How do you set up Tailwind in an Angular project?](#242-how-do-you-set-up-tailwind-in-an-angular-project)
- [243: How do you use Tailwind with component styles in Angular?](#243-how-do-you-use-tailwind-with-component-styles-in-angular)
- [244: Can you use Tailwind v4 with Sass, Less or Stylus?](#244-can-you-use-tailwind-v4-with-sass-less-or-stylus)
- [245: Does Tailwind v4 support CSS nesting?](#245-does-tailwind-v4-support-css-nesting)
- [246: Do you still need autoprefixer with v4?](#246-do-you-still-need-autoprefixer-with-v4)
- [247: What is the Tailwind upgrade tool?](#247-what-is-the-tailwind-upgrade-tool)
- [248: What are the main breaking changes from v3 to v4?](#248-what-are-the-main-breaking-changes-from-v3-to-v4)
- [249: What changed in the order of stacked variants in v4?](#249-what-changed-in-the-order-of-stacked-variants-in-v4)
- [250: What changed with `space-y-*` in v4?](#250-what-changed-with-space-y--in-v4)
- [251: Why does my `border` look darker after upgrading to v4?](#251-why-does-my-border-look-darker-after-upgrading-to-v4)
- [252: How do you restore the v3 `hover` behavior on touch devices?](#252-how-do-you-restore-the-v3-hover-behavior-on-touch-devices)
- [253: How do you restore pointer cursor on buttons in v4?](#253-how-do-you-restore-pointer-cursor-on-buttons-in-v4)
- [254: How do you customize the `container` class in v4?](#254-how-do-you-customize-the-container-class-in-v4)
- [255: How do you add a prefix to all Tailwind classes?](#255-how-do-you-add-a-prefix-to-all-tailwind-classes)
- [256: Why would you use a prefix?](#256-why-would-you-use-a-prefix)
- [257: How do you make all utilities `!important`?](#257-how-do-you-make-all-utilities-important)
- [258: What is the `prettier-plugin-tailwindcss`?](#258-what-is-the-prettier-plugin-tailwindcss)
- [259: How can the Prettier plugin sort classes in function calls like `clsx`?](#259-how-can-the-prettier-plugin-sort-classes-in-function-calls-like-clsx)
- [260: What does the Tailwind CSS IntelliSense extension do?](#260-what-does-the-tailwind-css-intellisense-extension-do)
- [261: What is `clsx` and why is it used with Tailwind?](#261-what-is-clsx-and-why-is-it-used-with-tailwind)
- [262: What is `tailwind-merge`?](#262-what-is-tailwind-merge)
- [263: What is the `cn` helper?](#263-what-is-the-cn-helper)
- [264: What is `cva` (class-variance-authority)?](#264-what-is-cva-class-variance-authority)
- [265: How do you build a responsive navbar with a mobile menu?](#265-how-do-you-build-a-responsive-navbar-with-a-mobile-menu)
- [266: How do you build a responsive card grid that fits as many cards as possible?](#266-how-do-you-build-a-responsive-card-grid-that-fits-as-many-cards-as-possible)
- [267: How do you build a modal overlay?](#267-how-do-you-build-a-modal-overlay)
- [268: How do you style a native `<dialog>` and its backdrop?](#268-how-do-you-style-a-native-dialog-and-its-backdrop)
- [269: How do you build an accordion with `<details>` and Tailwind?](#269-how-do-you-build-an-accordion-with-details-and-tailwind)
- [270: How do you build a sidebar layout that collapses on mobile?](#270-how-do-you-build-a-sidebar-layout-that-collapses-on-mobile)
- [271: Why doesn't `truncate` work inside a flex item?](#271-why-doesnt-truncate-work-inside-a-flex-item)
- [272: How do you make a sticky footer?](#272-how-do-you-make-a-sticky-footer)
- [273: What is subgrid and how do you use it?](#273-what-is-subgrid-and-how-do-you-use-it)
- [274: What are `grid-flow-dense` and `auto-rows-*`?](#274-what-are-grid-flow-dense-and-auto-rows-)
- [275: How do you use scroll snap?](#275-how-do-you-use-scroll-snap)
- [276: What are `scroll-mt-*` and `scroll-pt-*` used for?](#276-what-are-scroll-mt--and-scroll-pt--used-for)
- [277: What are `overscroll-*` utilities?](#277-what-are-overscroll--utilities)
- [278: How do you style scrollbar colors in v4.3?](#278-how-do-you-style-scrollbar-colors-in-v43)
- [279: What is `scrollbar-gutter-stable`?](#279-what-is-scrollbar-gutter-stable)
- [280: What are the `zoom-*` and `tab-*` utilities in v4.3?](#280-what-are-the-zoom--and-tab--utilities-in-v43)
- [281: What does `font-features-*` do?](#281-what-does-font-features--do)
- [282: What are `tabular-nums` used for?](#282-what-are-tabular-nums-used-for)
- [283: What is `font-stretch-*`?](#283-what-is-font-stretch-)
- [284: How do you align items to the last baseline?](#284-how-do-you-align-items-to-the-last-baseline)
- [285: What are "safe" alignment utilities?](#285-what-are-safe-alignment-utilities)
- [286: How do you style the first line or first letter of text?](#286-how-do-you-style-the-first-line-or-first-letter-of-text)
- [287: How do you style list markers?](#287-how-do-you-style-list-markers)
- [288: How do you style an open `<details>` or popover?](#288-how-do-you-style-an-open-details-or-popover)
- [289: What is the `inert:` variant?](#289-what-is-the-inert-variant)
- [290: What is the `noscript:` variant?](#290-what-is-the-noscript-variant)
- [291: How do you write print styles?](#291-how-do-you-write-print-styles)
- [292: How do you build a toggle switch with only Tailwind?](#292-how-do-you-build-a-toggle-switch-with-only-tailwind)
- [293: How do you build a floating label input?](#293-how-do-you-build-a-floating-label-input)
- [294: How do you build a tooltip on hover?](#294-how-do-you-build-a-tooltip-on-hover)
- [295: How do you build a skeleton loader?](#295-how-do-you-build-a-skeleton-loader)
- [296: How do you build a badge component?](#296-how-do-you-build-a-badge-component)
- [297: How do you use Tailwind with Headless UI or Radix?](#297-how-do-you-use-tailwind-with-headless-ui-or-radix)
- [298: What is shadcn/ui and how does it relate to Tailwind?](#298-what-is-shadcnui-and-how-does-it-relate-to-tailwind)
- [299: What does the Tailwind output CSS look like for a simple utility?](#299-what-does-the-tailwind-output-css-look-like-for-a-simple-utility)
- [300: What are the cascade layers Tailwind v4 uses?](#300-what-are-the-cascade-layers-tailwind-v4-uses)

### Advanced Questions (301-450)

- [301: What is the Oxide engine?](#301-what-is-the-oxide-engine)
- [302: How does Tailwind's class detection actually work?](#302-how-does-tailwinds-class-detection-actually-work)
- [303: Why can Tailwind generate a class from a comment or a random string?](#303-why-can-tailwind-generate-a-class-from-a-comment-or-a-random-string)
- [304: How does automatic source detection decide which files to scan?](#304-how-does-automatic-source-detection-decide-which-files-to-scan)
- [305: What happens internally when you write `@import "tailwindcss"`?](#305-what-happens-internally-when-you-write-import-tailwindcss)
- [306: How do you use Tailwind without Preflight?](#306-how-do-you-use-tailwind-without-preflight)
- [307: Why can unlayered CSS override Tailwind utilities in v4?](#307-why-can-unlayered-css-override-tailwind-utilities-in-v4)
- [308: How does Tailwind v4 use `@property`?](#308-how-does-tailwind-v4-use-property)
- [309: Why might some utilities break inside Shadow DOM?](#309-why-might-some-utilities-break-inside-shadow-dom)
- [310: How are opacity modifiers implemented in v4?](#310-how-are-opacity-modifiers-implemented-in-v4)
- [311: How are utilities sorted in the generated CSS?](#311-how-are-utilities-sorted-in-the-generated-css)
- [312: How do you write a functional utility with `--value()`?](#312-how-do-you-write-a-functional-utility-with---value)
- [313: What types can be used inside `--value()`?](#313-what-types-can-be-used-inside---value)
- [314: How do you handle negative values and fractions in custom utilities?](#314-how-do-you-handle-negative-values-and-fractions-in-custom-utilities)
- [315: How do you support modifiers in a custom utility?](#315-how-do-you-support-modifiers-in-a-custom-utility)
- [316: What is `--default()` in v4.3?](#316-what-is---default-in-v43)
- [317: How do you write a custom variant that needs a media query and a selector?](#317-how-do-you-write-a-custom-variant-that-needs-a-media-query-and-a-selector)
- [318: Why do custom variants often use `:where()`?](#318-why-do-custom-variants-often-use-where)
- [319: How do you create multiple themes (not just light/dark) with Tailwind v4?](#319-how-do-you-create-multiple-themes-not-just-lightdark-with-tailwind-v4)
- [320: Why use `@theme inline` and not plain `@theme` for semantic tokens?](#320-why-use-theme-inline-and-not-plain-theme-for-semantic-tokens)
- [321: How would you design a token system with primitive and semantic layers?](#321-how-would-you-design-a-token-system-with-primitive-and-semantic-layers)
- [322: How do you share a Tailwind theme across multiple apps in a monorepo?](#322-how-do-you-share-a-tailwind-theme-across-multiple-apps-in-a-monorepo)
- [323: How should a component library that uses Tailwind be published?](#323-how-should-a-component-library-that-uses-tailwind-be-published)
- [324: How can a library include its own `@source` so users don't have to?](#324-how-can-a-library-include-its-own-source-so-users-dont-have-to)
- [325: How does `tailwind-merge` know which classes conflict, and what goes wrong with custom tokens?](#325-how-does-tailwind-merge-know-which-classes-conflict-and-what-goes-wrong-with-custom-tokens)
- [326: What is the cost of using `tailwind-merge` everywhere?](#326-what-is-the-cost-of-using-tailwind-merge-everywhere)
- [327: How do you write a Tailwind plugin in JavaScript for v4?](#327-how-do-you-write-a-tailwind-plugin-in-javascript-for-v4)
- [328: How do you pass options to a plugin from CSS?](#328-how-do-you-pass-options-to-a-plugin-from-css)
- [329: What parts of the v3 JavaScript config are not supported in v4?](#329-what-parts-of-the-v3-javascript-config-are-not-supported-in-v4)
- [330: How do you read theme values in JavaScript in v4?](#330-how-do-you-read-theme-values-in-javascript-in-v4)
- [331: How do you pass theme colors to a canvas or chart library?](#331-how-do-you-pass-theme-colors-to-a-canvas-or-chart-library)
- [332: How do you avoid FOUC (flash of unstyled content) with Tailwind in SSR apps?](#332-how-do-you-avoid-fouc-flash-of-unstyled-content-with-tailwind-in-ssr-apps)
- [333: How do you debug why a Tailwind class isn't working?](#333-how-do-you-debug-why-a-tailwind-class-isnt-working)
- [334: Why is a class generated in development but missing in production?](#334-why-is-a-class-generated-in-development-but-missing-in-production)
- [335: How do you handle class names that come from a database (for example user-chosen colors)?](#335-how-do-you-handle-class-names-that-come-from-a-database-for-example-user-chosen-colors)
- [336: What are the performance considerations of very long class lists?](#336-what-are-the-performance-considerations-of-very-long-class-lists)
- [337: How does Tailwind v4 handle vendor prefixes and browser targets?](#337-how-does-tailwind-v4-handle-vendor-prefixes-and-browser-targets)
- [338: What is the difference between `@tailwindcss/vite` and `@tailwindcss/postcss`?](#338-what-is-the-difference-between-tailwindcssvite-and-tailwindcsspostcss)
- [339: How do you set up Tailwind with webpack in v4.2+?](#339-how-do-you-set-up-tailwind-with-webpack-in-v42)
- [340: Can you use Tailwind's compiler from Node.js directly?](#340-can-you-use-tailwinds-compiler-from-nodejs-directly)
- [341: What is the trade-off between `@apply` and components in terms of output?](#341-what-is-the-trade-off-between-apply-and-components-in-terms-of-output)
- [342: When is `@apply` the right choice?](#342-when-is-apply-the-right-choice)
- [343: How do you handle specificity conflicts with a legacy CSS codebase?](#343-how-do-you-handle-specificity-conflicts-with-a-legacy-css-codebase)
- [344: How do you migrate a large v3 codebase to v4 safely?](#344-how-do-you-migrate-a-large-v3-codebase-to-v4-safely)
- [345: What visual regressions are most common after a v3 to v4 upgrade?](#345-what-visual-regressions-are-most-common-after-a-v3-to-v4-upgrade)
- [346: How does the `hidden` attribute interact with Tailwind display utilities?](#346-how-does-the-hidden-attribute-interact-with-tailwind-display-utilities)
- [347: How do you make a utility that responds to a CSS variable set by a parent?](#347-how-do-you-make-a-utility-that-responds-to-a-css-variable-set-by-a-parent)
- [348: What is `@source inline()` brace expansion syntax?](#348-what-is-source-inline-brace-expansion-syntax)
- [349: How do you stop a specific class from being generated?](#349-how-do-you-stop-a-specific-class-from-being-generated)
- [350: How would you build a design system button with variants, sizes and states?](#350-how-would-you-build-a-design-system-button-with-variants-sizes-and-states)
- [351: How do you style a component based on its own size and its parent's state at the same time?](#351-how-do-you-style-a-component-based-on-its-own-size-and-its-parents-state-at-the-same-time)
- [352: What is the difference between `group-*` and `in-*` in terms of generated CSS?](#352-what-is-the-difference-between-group--and-in--in-terms-of-generated-css)
- [353: How do you animate an element when it enters and leaves without JavaScript libraries?](#353-how-do-you-animate-an-element-when-it-enters-and-leaves-without-javascript-libraries)
- [354: How do you build view transitions with Tailwind?](#354-how-do-you-build-view-transitions-with-tailwind)
- [355: How do you register a custom property for animation with Tailwind?](#355-how-do-you-register-a-custom-property-for-animation-with-tailwind)
- [356: How does Tailwind v4 handle CSS `@import` of other files?](#356-how-does-tailwind-v4-handle-css-import-of-other-files)
- [357: How do you put an imported third-party stylesheet into a layer?](#357-how-do-you-put-an-imported-third-party-stylesheet-into-a-layer)
- [358: How do you scope Tailwind to part of a page (e.g. a widget embedded in another site)?](#358-how-do-you-scope-tailwind-to-part-of-a-page-eg-a-widget-embedded-in-another-site)
- [359: How do you test Tailwind-based components?](#359-how-do-you-test-tailwind-based-components)
- [360: How do you use Tailwind in Storybook?](#360-how-do-you-use-tailwind-in-storybook)
- [361: What are common accessibility mistakes in Tailwind projects?](#361-what-are-common-accessibility-mistakes-in-tailwind-projects)
- [362: How do you build a consistent focus style across a project?](#362-how-do-you-build-a-consistent-focus-style-across-a-project)
- [363: How do you support Windows high contrast mode properly?](#363-how-do-you-support-windows-high-contrast-mode-properly)
- [364: How do you style based on user preferences like reduced data or contrast?](#364-how-do-you-style-based-on-user-preferences-like-reduced-data-or-contrast)
- [365: How do you use container queries with `has-*` to build adaptive forms?](#365-how-do-you-use-container-queries-with-has--to-build-adaptive-forms)
- [366: How do you implement RTL support in a Tailwind app?](#366-how-do-you-implement-rtl-support-in-a-tailwind-app)
- [367: How do you make spacing fluid (scales with viewport) in Tailwind?](#367-how-do-you-make-spacing-fluid-scales-with-viewport-in-tailwind)
- [368: How do you add named spacing values in v4?](#368-how-do-you-add-named-spacing-values-in-v4)
- [369: How does v4 handle fractions and arbitrary numbers for width?](#369-how-does-v4-handle-fractions-and-arbitrary-numbers-for-width)
- [370: How do you make a utility that accepts both theme values and any CSS variable?](#370-how-do-you-make-a-utility-that-accepts-both-theme-values-and-any-css-variable)
- [371: What are the downsides of Tailwind and how do you address them in interviews?](#371-what-are-the-downsides-of-tailwind-and-how-do-you-address-them-in-interviews)
- [372: How do you compare Tailwind with CSS Modules and CSS-in-JS?](#372-how-do-you-compare-tailwind-with-css-modules-and-css-in-js)
- [373: How does Tailwind work with React Server Components?](#373-how-does-tailwind-work-with-react-server-components)
- [374: How do you structure CSS files in a large Tailwind v4 project?](#374-how-do-you-structure-css-files-in-a-large-tailwind-v4-project)
- [375: Can you have multiple Tailwind entry CSS files in one project?](#375-can-you-have-multiple-tailwind-entry-css-files-in-one-project)
- [376: How does `!important` interact with cascade layers?](#376-how-does-important-interact-with-cascade-layers)
- [377: How can you change the order of Tailwind's layers or add your own?](#377-how-can-you-change-the-order-of-tailwinds-layers-or-add-your-own)
- [378: How do the internal `--tw-*` variables let utilities compose?](#378-how-do-the-internal---tw--variables-let-utilities-compose)
- [379: What happens when you mix Tailwind filter utilities with your own `filter` rule?](#379-what-happens-when-you-mix-tailwind-filter-utilities-with-your-own-filter-rule)
- [380: How would you stop developers from using arbitrary colors and enforce the design system?](#380-how-would-you-stop-developers-from-using-arbitrary-colors-and-enforce-the-design-system)
- [381: How do you keep design tokens in sync between Figma and Tailwind?](#381-how-do-you-keep-design-tokens-in-sync-between-figma-and-tailwind)
- [382: How do you handle a hydration mismatch caused by theme classes?](#382-how-do-you-handle-a-hydration-mismatch-caused-by-theme-classes)
- [383: Why should you prefer `dark:` classes over JavaScript conditionals for theming?](#383-why-should-you-prefer-dark-classes-over-javascript-conditionals-for-theming)
- [384: How do you scope a theme to only part of the page?](#384-how-do-you-scope-a-theme-to-only-part-of-the-page)
- [385: Why might `dark:` styles not apply inside a section with class `dark` when using the default dark mode?](#385-why-might-dark-styles-not-apply-inside-a-section-with-class-dark-when-using-the-default-dark-mode)
- [386: How do you combine system preference and a manual override in pure CSS?](#386-how-do-you-combine-system-preference-and-a-manual-override-in-pure-css)
- [387: How do stacking contexts cause z-index bugs in Tailwind layouts?](#387-how-do-stacking-contexts-cause-z-index-bugs-in-tailwind-layouts)
- [388: How do you define a z-index scale for a project?](#388-how-do-you-define-a-z-index-scale-for-a-project)
- [389: What CSS performance issues can you create with Tailwind utilities?](#389-what-css-performance-issues-can-you-create-with-tailwind-utilities)
- [390: How would you add `content-visibility` and `contain` for performance?](#390-how-would-you-add-content-visibility-and-contain-for-performance)
- [391: How does the `hover` media query in v4 affect devices with both touch and mouse?](#391-how-does-the-hover-media-query-in-v4-affect-devices-with-both-touch-and-mouse)
- [392: How do you write an arbitrary variant that uses an at-rule?](#392-how-do-you-write-an-arbitrary-variant-that-uses-an-at-rule)
- [393: How do you target a parent with a specific class using arbitrary group variants?](#393-how-do-you-target-a-parent-with-a-specific-class-using-arbitrary-group-variants)
- [394: How do you write a variant that targets a sibling that comes after the element?](#394-how-do-you-write-a-variant-that-targets-a-sibling-that-comes-after-the-element)
- [395: How can you style an element when a sibling anywhere in the form is checked?](#395-how-can-you-style-an-element-when-a-sibling-anywhere-in-the-form-is-checked)
- [396: How does Tailwind treat utilities used with many variants, in terms of CSS size?](#396-how-does-tailwind-treat-utilities-used-with-many-variants-in-terms-of-css-size)
- [397: How do you prevent a utility from being affected by Preflight changes or browser defaults when building email templates?](#397-how-do-you-prevent-a-utility-from-being-affected-by-preflight-changes-or-browser-defaults-when-building-email-templates)
- [398: How do you use Tailwind in a browser extension's content script?](#398-how-do-you-use-tailwind-in-a-browser-extensions-content-script)
- [399: How do you handle a host page that sets `html { font-size: 10px; }`?](#399-how-do-you-handle-a-host-page-that-sets-html--font-size-10px-)
- [400: How do micro-frontends using Tailwind avoid conflicts?](#400-how-do-micro-frontends-using-tailwind-avoid-conflicts)
- [401: How do you check for unused or invalid Tailwind classes in CI?](#401-how-do-you-check-for-unused-or-invalid-tailwind-classes-in-ci)
- [402: What are "canonical" class names, and why do linters suggest them?](#402-what-are-canonical-class-names-and-why-do-linters-suggest-them)
- [403: How does Tailwind handle duplicate classes across files?](#403-how-does-tailwind-handle-duplicate-classes-across-files)
- [404: How do you build a data table with sticky header and first column?](#404-how-do-you-build-a-data-table-with-sticky-header-and-first-column)
- [405: How do you build a masonry-like layout?](#405-how-do-you-build-a-masonry-like-layout)
- [406: How do you build a dashboard layout with a fixed sidebar and scrollable content?](#406-how-do-you-build-a-dashboard-layout-with-a-fixed-sidebar-and-scrollable-content)
- [407: How do you build a responsive image gallery with aspect ratios and lazy loading?](#407-how-do-you-build-a-responsive-image-gallery-with-aspect-ratios-and-lazy-loading)
- [408: How do you create a component that adapts to the number of children?](#408-how-do-you-create-a-component-that-adapts-to-the-number-of-children)
- [409: How do you build a "quantity query" style layout without JavaScript?](#409-how-do-you-build-a-quantity-query-style-layout-without-javascript)
- [410: How do you create a utility that sets multiple properties from one theme key?](#410-how-do-you-create-a-utility-that-sets-multiple-properties-from-one-theme-key)
- [411: How do you make a custom utility work with the opacity modifier?](#411-how-do-you-make-a-custom-utility-work-with-the-opacity-modifier)
- [412: What happens if two `@utility` definitions have the same name?](#412-what-happens-if-two-utility-definitions-have-the-same-name)
- [413: Can you override a built-in utility?](#413-can-you-override-a-built-in-utility)
- [414: How does Tailwind resolve conflicts between a theme key and a bare value?](#414-how-does-tailwind-resolve-conflicts-between-a-theme-key-and-a-bare-value)
- [415: How do you debug which `@theme` variables are actually in the output?](#415-how-do-you-debug-which-theme-variables-are-actually-in-the-output)
- [416: Why might a `var(--color-*)` used only in JavaScript be missing at runtime?](#416-why-might-a-var--color--used-only-in-javascript-be-missing-at-runtime)
- [417: How do you use Tailwind classes inside JavaScript strings in a non-standard file type (like `.php` templates or `.md`)?](#417-how-do-you-use-tailwind-classes-inside-javascript-strings-in-a-non-standard-file-type-like-php-templates-or-md)
- [418: How do you handle class names in a backend language that builds strings (e.g. Python or Go templates)?](#418-how-do-you-handle-class-names-in-a-backend-language-that-builds-strings-eg-python-or-go-templates)
- [419: How do you set up Tailwind with a backend framework like Laravel or Rails?](#419-how-do-you-set-up-tailwind-with-a-backend-framework-like-laravel-or-rails)
- [420: What is the standalone Tailwind CLI?](#420-what-is-the-standalone-tailwind-cli)
- [421: How does Tailwind handle `@layer base` rules that use `@apply` with variants?](#421-how-does-tailwind-handle-layer-base-rules-that-use-apply-with-variants)
- [422: Why might `@apply` of a utility with a variant produce unexpected selector output?](#422-why-might-apply-of-a-utility-with-a-variant-produce-unexpected-selector-output)
- [423: How do you make an accessible custom select or combobox styled with Tailwind?](#423-how-do-you-make-an-accessible-custom-select-or-combobox-styled-with-tailwind)
- [424: How do you build a responsive typography scale that also works in prose content?](#424-how-do-you-build-a-responsive-typography-scale-that-also-works-in-prose-content)
- [425: How would you implement density modes (compact vs comfortable) with Tailwind?](#425-how-would-you-implement-density-modes-compact-vs-comfortable-with-tailwind)
- [426: How do you test responsive variants in automated tests?](#426-how-do-you-test-responsive-variants-in-automated-tests)
- [427: How do you handle print layouts with Tailwind in detail?](#427-how-do-you-handle-print-layouts-with-tailwind-in-detail)
- [428: How do you use `@starting-style` and popovers to build a dropdown with no JavaScript?](#428-how-do-you-use-starting-style-and-popovers-to-build-a-dropdown-with-no-javascript)
- [429: How do you handle long class lists in templates for readability?](#429-how-do-you-handle-long-class-lists-in-templates-for-readability)
- [430: What is "arbitrary value overuse" and why is it a code smell?](#430-what-is-arbitrary-value-overuse-and-why-is-it-a-code-smell)
- [431: How do you build a reusable pattern for "polymorphic" components with Tailwind?](#431-how-do-you-build-a-reusable-pattern-for-polymorphic-components-with-tailwind)
- [432: How do you handle styling of child elements you can't edit (like a third-party widget)?](#432-how-do-you-handle-styling-of-child-elements-you-cant-edit-like-a-third-party-widget)
- [433: How do you manage icon sizes consistently?](#433-how-do-you-manage-icon-sizes-consistently)
- [434: How would you structure Tailwind in a design system with tokens, primitives and recipes?](#434-how-would-you-structure-tailwind-in-a-design-system-with-tokens-primitives-and-recipes)
- [435: How do you allow consumers of your design system to customize it?](#435-how-do-you-allow-consumers-of-your-design-system-to-customize-it)
- [436: How do you version and roll out theme changes safely across many apps?](#436-how-do-you-version-and-roll-out-theme-changes-safely-across-many-apps)
- [437: How do you write a codemod to rename Tailwind classes?](#437-how-do-you-write-a-codemod-to-rename-tailwind-classes)
- [438: How do you handle `className` props in a component when variant classes might conflict with user classes?](#438-how-do-you-handle-classname-props-in-a-component-when-variant-classes-might-conflict-with-user-classes)
- [439: Why is "the last class wins" not true in plain Tailwind?](#439-why-is-the-last-class-wins-not-true-in-plain-tailwind)
- [440: How can Tailwind v4's CSS-first config work with TypeScript type safety?](#440-how-can-tailwind-v4s-css-first-config-work-with-typescript-type-safety)
- [441: How do you implement skeleton/loading states without layout shift?](#441-how-do-you-implement-skeletonloading-states-without-layout-shift)
- [442: What CSS units are useful as Tailwind arbitrary values in modern layouts?](#442-what-css-units-are-useful-as-tailwind-arbitrary-values-in-modern-layouts)
- [443: How would you approach performance auditing of CSS in a Tailwind project?](#443-how-would-you-approach-performance-auditing-of-css-in-a-tailwind-project)
- [444: How can a big JSON or Markdown content folder slow down Tailwind builds, and how do you fix it?](#444-how-can-a-big-json-or-markdown-content-folder-slow-down-tailwind-builds-and-how-do-you-fix-it)
- [445: What changes did v4.1 bring that matter for older browser support?](#445-what-changes-did-v41-bring-that-matter-for-older-browser-support)
- [446: How do you build a theme switcher component that works with server rendering and avoids flicker?](#446-how-do-you-build-a-theme-switcher-component-that-works-with-server-rendering-and-avoids-flicker)
- [447: How do you handle CSS for third-party components that are rendered into a portal?](#447-how-do-you-handle-css-for-third-party-components-that-are-rendered-into-a-portal)
- [448: What should you consider when using Tailwind with CSS anchor positioning?](#448-what-should-you-consider-when-using-tailwind-with-css-anchor-positioning)
- [449: How would you explain the main architecture changes of Tailwind v4 to a team in a few points?](#449-how-would-you-explain-the-main-architecture-changes-of-tailwind-v4-to-a-team-in-a-few-points)
- [450: What is a good answer to "When would you NOT use Tailwind?"](#450-what-is-a-good-answer-to-when-would-you-not-use-tailwind)

---

## Easy Questions (1-150)

### 1: What is Tailwind CSS?

Tailwind CSS is a utility-first CSS framework. Instead of giving you ready-made components like "card" or "navbar", it gives you small single-purpose classes such as `flex`, `p-4`, `text-center` and `bg-blue-500`. You build the design by combining these classes directly in your markup.

```html
<button
  class="rounded-lg bg-blue-600 px-4 py-2 font-semibold text-white hover:bg-blue-700"
>
  Save
</button>
```

### 2: What does "utility-first" mean?

It means most styling is done with small classes that each do one thing (set a margin, set a color, set a display value). You write fewer custom CSS rules and instead compose these utilities in HTML. Custom CSS is still allowed, but it is the exception rather than the default.

### 3: What is the latest major version of Tailwind CSS and what changed in it?

The current major version is v4 (the 4.x line, with v4.3 being the latest minor release at the time of writing). v4 was a big rewrite: a new engine that is much faster, configuration done in CSS with `@theme` instead of `tailwind.config.js`, automatic content detection, a single `@import "tailwindcss"` line instead of three `@tailwind` directives, built-in container queries, and colors defined in OKLCH.

### 4: How is Tailwind different from Bootstrap?

Bootstrap ships pre-designed components (`.btn`, `.card`, `.navbar`) with a fixed look that you override. Tailwind ships low-level utilities and no component styles, so you design everything yourself. Bootstrap is faster for a generic look; Tailwind is better when you want a custom design without fighting framework defaults.

### 5: How do you install Tailwind CSS v4 with Vite?

Install the packages and add the Vite plugin, then import Tailwind in your CSS.

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

### 6: What does `@import "tailwindcss";` do?

It is the single line that loads Tailwind in v4. It pulls in the theme variables, Preflight (base styles) and the utilities layer. In v3 you needed three lines: `@tailwind base;`, `@tailwind components;` and `@tailwind utilities;`. Those directives are gone in v4.

### 7: Do you still need a `tailwind.config.js` file in v4?

No. In v4 the configuration lives in your CSS file using the `@theme` directive and other CSS directives. A JavaScript config file is optional and only needed for older setups. If you do want one, you load it explicitly with `@config "./tailwind.config.js";`.

### 8: How do you install Tailwind with PostCSS in v4?

```bash
npm install tailwindcss @tailwindcss/postcss postcss
```

```js
// postcss.config.mjs
export default {
  plugins: {
    "@tailwindcss/postcss": {},
  },
};
```

Then add `@import "tailwindcss";` to your main CSS file. You no longer need `autoprefixer` or `postcss-import`, since v4 handles both.

### 9: How do you use the Tailwind CLI in v4?

The CLI moved to its own package, `@tailwindcss/cli`.

```bash
npm install tailwindcss @tailwindcss/cli
npx @tailwindcss/cli -i ./src/input.css -o ./dist/output.css --watch
```

`-i` is the input CSS file, `-o` is the output file and `--watch` rebuilds on changes. Add `--minify` for production.

### 10: Can you use Tailwind from a CDN?

Yes, for prototypes and demos. v4 offers a browser build:

```html
<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
```

It scans the page in the browser and generates styles at runtime. It is not meant for production because it adds a runtime script and does the work on every page load.

### 11: How does Tailwind know which classes to generate?

Tailwind scans your project files for anything that looks like a class name and generates CSS only for the classes it finds. In v4 this detection is automatic: it scans the project, skips files listed in `.gitignore`, skips `node_modules`, binary files and CSS files. You don't need a `content` array like in v3.

### 12: Why is the final CSS file small even though Tailwind has thousands of utilities?

Because Tailwind only generates the classes that appear in your source files. If you never use `bg-pink-300`, it is never written to the output CSS. Most real projects end up with a CSS file of a few kilobytes after gzip.

### 13: What is Preflight?

Preflight is Tailwind's set of base styles, built on top of modern-normalize. It removes default margins, makes headings and lists unstyled, sets `box-sizing: border-box` on everything, makes images `display: block`, and resets borders so that adding a `border` class works predictably. It is included automatically with `@import "tailwindcss"`.

### 14: Why do my `<h1>` and `<ul>` look like plain text after adding Tailwind?

Preflight removes the default browser styles from headings, lists and other elements. You style them yourself with utilities:

```html
<h1 class="text-3xl font-bold">Title</h1>
<ul class="list-disc pl-5">
  <li>Item</li>
</ul>
```

### 15: How do you add padding in Tailwind?

Use the `p-*` utilities. `p-4` adds padding on all sides, `px-4` left and right, `py-4` top and bottom, and `pt-4`, `pr-4`, `pb-4`, `pl-4` for single sides.

```html
<div class="px-6 py-3">Content</div>
```

### 16: How do you add margin?

Use `m-*` in the same way: `m-4`, `mx-4`, `my-4`, `mt-4`, `mr-4`, `mb-4`, `ml-4`. `mx-auto` centers a block element that has a width.

```html
<div class="mx-auto mt-8 max-w-xl">Centered box</div>
```

### 17: How does the spacing scale work in v4?

In v4 the whole spacing scale comes from one variable, `--spacing`, which defaults to `0.25rem` (4px). A class like `p-4` becomes `padding: calc(var(--spacing) * 4)`, which is `1rem`. Because it is a multiplier, any whole number works, including values that were not in the v3 scale, like `p-13` or `mt-29`.

### 18: How do you add negative margin?

Put a minus sign in front of the class.

```html
<div class="-mt-4">Pulled up by 1rem</div>
```

Negative values also work for `translate`, `inset`, `top`, `left` and similar utilities, for example `-translate-x-1/2`.

### 19: How do you set the text color?

Use `text-{color}-{shade}`.

```html
<p class="text-gray-700">Body text</p>
<p class="text-red-600">Error message</p>
```

### 20: How do you set the background color?

Use `bg-{color}-{shade}`.

```html
<div class="bg-slate-100">Light gray background</div>
```

### 21: What color shades are available in the default palette?

Each color has shades `50`, `100`, `200` up to `900`, plus `950`. Lower numbers are lighter. The palette includes gray families (`slate`, `gray`, `zinc`, `neutral`, `stone`, and since v4.2 `mauve`, `olive`, `mist`, `taupe`) and colors like `red`, `orange`, `amber`, `yellow`, `lime`, `green`, `emerald`, `teal`, `cyan`, `sky`, `blue`, `indigo`, `violet`, `purple`, `fuchsia`, `pink` and `rose`. There are also `black`, `white`, `transparent` and `current`.

### 22: What color format does v4 use for the default palette?

OKLCH. Colors are defined like `--color-blue-500: oklch(0.623 0.214 259.815);`. OKLCH gives more even lightness between shades and supports wider color gamuts, so colors look more vivid on modern screens.

### 23: How do you change the opacity of a color?

Add a slash and the opacity value after the color.

```html
<div class="bg-black/50">50% black overlay</div>
<p class="text-blue-600/75">75% opacity text</p>
```

This works for text, background, border, ring, shadow, fill, stroke and other color utilities.

### 24: Are `bg-opacity-*` and `text-opacity-*` still available in v4?

No, they were removed. Use the slash opacity modifier instead: `bg-black/50` rather than `bg-black bg-opacity-50`.

### 25: How do you set the font size?

Use `text-xs`, `text-sm`, `text-base`, `text-lg`, `text-xl`, `text-2xl` and up to `text-9xl`. Each size also sets a matching default line height.

```html
<h2 class="text-2xl">Section title</h2>
```

### 26: How do you set font weight?

Use `font-thin`, `font-extralight`, `font-light`, `font-normal`, `font-medium`, `font-semibold`, `font-bold`, `font-extrabold` or `font-black`.

```html
<span class="font-semibold">Important</span>
```

### 27: How do you set the font family?

Use `font-sans`, `font-serif` or `font-mono`. You can add your own font families in `@theme`.

```html
<code class="font-mono">npm run dev</code>
```

### 28: How do you set line height?

Use `leading-*` utilities like `leading-tight`, `leading-normal`, `leading-relaxed`, or a number based on the spacing scale like `leading-6`. You can also set it together with the font size using a slash: `text-sm/6`.

```html
<p class="text-base/7">Paragraph with 1.75rem line height</p>
```

### 29: How do you set letter spacing?

Use `tracking-tighter`, `tracking-tight`, `tracking-normal`, `tracking-wide`, `tracking-wider` or `tracking-widest`.

```html
<span class="text-xs font-semibold tracking-wide uppercase">Label</span>
```

### 30: How do you align text?

Use `text-left`, `text-center`, `text-right`, `text-justify`, `text-start` or `text-end`. `text-start` and `text-end` respect the text direction, so they flip in right-to-left layouts.

### 31: How do you make text uppercase, lowercase or capitalized?

Use `uppercase`, `lowercase`, `capitalize`, or `normal-case` to reset.

### 32: How do you underline text or remove an underline?

Use `underline` to add one and `no-underline` to remove it. You can style it with `decoration-*` utilities.

```html
<a class="underline decoration-sky-500 decoration-2 underline-offset-4">Link</a>
```

### 33: How do you truncate long text with an ellipsis?

Use `truncate`. It sets `overflow: hidden`, `text-overflow: ellipsis` and `white-space: nowrap`. The element needs a limited width.

```html
<p class="w-48 truncate">
  This is a very long line of text that will be cut off
</p>
```

### 34: How do you limit text to a set number of lines?

Use `line-clamp-*`. It is built in, no plugin needed.

```html
<p class="line-clamp-3">Long article summary...</p>
```

### 35: How do you make an element a flex container?

Add `flex` (or `inline-flex`).

```html
<div class="flex gap-4">
  <div>One</div>
  <div>Two</div>
</div>
```

### 36: How do you change the flex direction?

Use `flex-row` (default), `flex-col`, `flex-row-reverse` or `flex-col-reverse`.

```html
<div class="flex flex-col gap-2">...</div>
```

### 37: How do you center something horizontally and vertically with flexbox?

```html
<div class="flex h-screen items-center justify-center">
  <p>Centered</p>
</div>
```

`justify-center` centers on the main axis and `items-center` on the cross axis.

### 38: What is the difference between `justify-*` and `items-*`?

`justify-*` controls alignment along the main axis (horizontal for `flex-row`). `items-*` controls alignment along the cross axis (vertical for `flex-row`). If you switch to `flex-col`, the axes swap.

### 39: What does `justify-between` do?

It puts the first item at the start, the last item at the end, and spreads the rest evenly with equal space between them. It is often used in headers.

```html
<header class="flex items-center justify-between">
  <Logo />
  <nav>...</nav>
</header>
```

### 40: How do you make flex items wrap?

Use `flex-wrap`. The default is `flex-nowrap`.

```html
<div class="flex flex-wrap gap-2">...</div>
```

### 41: What does `flex-1` do?

It sets `flex: 1 1 0%`, so the item grows and shrinks as needed and ignores its initial size. It is commonly used to make one item fill the remaining space.

```html
<div class="flex">
  <aside class="w-64">Sidebar</aside>
  <main class="flex-1">Main content</main>
</div>
```

### 42: What are `grow` and `shrink` utilities?

`grow` lets an item grow to fill free space, `grow-0` stops it. `shrink` lets it shrink, `shrink-0` stops it from shrinking. In v4 the old names `flex-grow` and `flex-shrink` were removed in favor of `grow` and `shrink`.

### 43: How do you add space between items?

Use `gap-*` for flex and grid containers. `gap-x-*` and `gap-y-*` set horizontal and vertical gaps separately.

```html
<div class="grid grid-cols-3 gap-6">...</div>
```

### 44: What is the difference between `gap-*` and `space-x-*`?

`gap-*` uses the CSS `gap` property and works on flex and grid containers. `space-x-*` and `space-y-*` add margins to child elements. `gap` is usually the better choice because it handles wrapping correctly. `space-*` is useful when the parent is not flex or grid.

### 45: How do you create a grid layout?

Use `grid` with `grid-cols-*`.

```html
<div class="grid grid-cols-3 gap-4">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>
```

In v4 any number works, so `grid-cols-15` is valid without configuration.

### 46: How do you make a grid item span multiple columns?

Use `col-span-*`. `col-span-full` spans all columns.

```html
<div class="grid grid-cols-4 gap-4">
  <div class="col-span-3">Wide</div>
  <div>Narrow</div>
</div>
```

### 47: How do you set rows in a grid?

Use `grid-rows-*` on the container and `row-span-*` on items.

```html
<div class="grid grid-rows-3 grid-flow-col gap-4">...</div>
```

### 48: What does `place-items-center` do?

It sets both `align-items` and `justify-items` to `center`. On a grid container it centers each item inside its cell. `grid place-items-center` is a short way to center one child.

### 49: How do you set the width of an element?

Use `w-*`. You can use spacing values (`w-64`), fractions (`w-1/2`), `w-full`, `w-screen`, `w-auto`, `w-fit`, `w-min`, `w-max`, or container sizes like `w-md`.

```html
<div class="w-1/3">One third</div>
```

### 50: How do you set the height?

Use `h-*` the same way as width: `h-12`, `h-full`, `h-screen`, `h-dvh`, `h-fit`, `h-auto`.

### 51: What is the `size-*` utility?

It sets width and height at the same time. `size-10` is the same as `w-10 h-10`.

```html
<img class="size-12 rounded-full" src="/avatar.png" alt="" />
```

### 52: What is the difference between `h-screen` and `h-dvh`?

`h-screen` is `100vh`. On mobile browsers `100vh` can be taller than the visible area because of the address bar. `h-dvh` uses dynamic viewport height (`100dvh`), which changes as the browser UI shows or hides. There are also `h-svh` (small) and `h-lvh` (large).

### 53: How do you set max width?

Use `max-w-*`. Common values are `max-w-sm`, `max-w-md`, `max-w-lg` up to `max-w-7xl`, plus `max-w-full`, `max-w-none` and `max-w-prose` (good line length for reading).

```html
<article class="mx-auto max-w-prose">...</article>
```

### 54: How do you set min width and min height?

Use `min-w-*` and `min-h-*`, for example `min-w-0`, `min-h-screen`, `min-h-dvh`. `min-w-0` is often needed on flex children so that text truncation works.

### 55: How do you hide an element?

Use `hidden`, which sets `display: none`. To hide it visually but keep it for screen readers, use `sr-only`. `invisible` hides it but keeps the space it takes up.

### 56: What display utilities does Tailwind have?

`block`, `inline-block`, `inline`, `flex`, `inline-flex`, `grid`, `inline-grid`, `table`, `contents`, `flow-root`, `list-item` and `hidden`, among others.

### 57: How do you add a border?

Use `border` for a 1px border on all sides, or `border-2`, `border-4`, `border-8` for thicker ones. Single sides: `border-t`, `border-r`, `border-b`, `border-l`, `border-x`, `border-y`.

```html
<div class="border border-gray-300">Box</div>
```

### 58: What is the default border color in v4?

In v4 the default border color is `currentColor` (the text color). In v3 it was `gray-200`. So in v4 you should usually add a color class like `border-gray-200` whenever you add `border`.

### 59: How do you round corners?

Use `rounded-*`: `rounded-xs`, `rounded-sm`, `rounded-md`, `rounded-lg`, `rounded-xl`, `rounded-2xl`, `rounded-3xl`, `rounded-4xl`, `rounded-full` and `rounded-none`. You can target corners with `rounded-t-lg`, `rounded-tl-lg`, and so on.

### 60: What changed with the `rounded` and `shadow` names in v4?

The scales were shifted so every size has a name. In v4:

- `shadow-sm` became `shadow-xs`, and plain `shadow` became `shadow-sm`.
- `rounded-sm` became `rounded-xs`, and plain `rounded` became `rounded-sm`.
- The same shift happened for `blur` and `drop-shadow`.

The upgrade tool renames these for you.

### 61: How do you add a shadow?

Use `shadow-2xs`, `shadow-xs`, `shadow-sm`, `shadow-md`, `shadow-lg`, `shadow-xl`, `shadow-2xl` or `shadow-none`.

```html
<div class="rounded-xl bg-white p-6 shadow-lg">Card</div>
```

### 62: How do you change the shadow color?

Add a color class after the size class.

```html
<button class="bg-indigo-500 shadow-lg shadow-indigo-500/50">Button</button>
```

### 63: How do you set opacity of a whole element?

Use `opacity-*` with values from `0` to `100`.

```html
<div class="opacity-50">Faded</div>
```

### 64: How do you apply a style on hover?

Prefix the class with `hover:`.

```html
<button class="bg-sky-500 hover:bg-sky-700">Hover me</button>
```

### 65: Does `hover:` always apply when the mouse is over an element in v4?

In v4 `hover:` is wrapped in `@media (hover: hover)`, so it only applies on devices that support hovering. This prevents "sticky" hover styles on touch screens after a tap.

### 66: How do you style focus states?

Use `focus:` or, better for keyboard users, `focus-visible:`.

```html
<input
  class="border rounded-md px-3 py-2 focus:outline-2 focus:outline-blue-500"
/>
<button
  class="focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600"
>
  OK
</button>
```

### 67: What is the difference between `focus:` and `focus-visible:`?

`focus:` applies whenever the element has focus, including mouse clicks. `focus-visible:` applies only when the browser thinks the focus should be visible, usually when using the keyboard. `focus-visible:` avoids showing outlines after mouse clicks while keeping them for keyboard users.

### 68: How do you style an element when it is being clicked?

Use `active:`.

```html
<button class="bg-blue-500 active:bg-blue-800">Press</button>
```

### 69: How do you style disabled elements?

Use `disabled:`.

```html
<button
  disabled
  class="bg-blue-600 text-white disabled:cursor-not-allowed disabled:opacity-50"
>
  Submit
</button>
```

### 70: How do you make a layout responsive?

Add breakpoint prefixes like `sm:`, `md:`, `lg:`, `xl:` and `2xl:`. Unprefixed classes apply to all sizes, and prefixed ones apply at that width and above.

```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4">...</div>
```

### 71: What are the default breakpoints in v4?

- `sm`: 40rem (640px)
- `md`: 48rem (768px)
- `lg`: 64rem (1024px)
- `xl`: 80rem (1280px)
- `2xl`: 96rem (1536px)

They are defined in rem in v4 and stored as `--breakpoint-*` theme variables.

### 72: What does "mobile-first" mean in Tailwind?

Unprefixed utilities apply to all screen sizes, and breakpoint prefixes apply from that size up (`min-width`). So you write the mobile style first and then add changes for bigger screens. `sm:text-center` does not mean "only on small screens"; it means "640px and wider".

### 73: How do you apply a style only below a breakpoint?

Use the `max-*` variants.

```html
<div class="max-md:hidden">Hidden below 768px</div>
```

You can also combine them for a range: `md:max-xl:flex` applies only between `md` and `xl`.

### 74: How do you enable dark mode styles?

Use the `dark:` prefix. By default it follows the operating system setting using `prefers-color-scheme`.

```html
<div class="bg-white text-gray-900 dark:bg-gray-900 dark:text-white">...</div>
```

### 75: What is the `container` class?

`container` sets `width: 100%` and a `max-width` that matches the current breakpoint. In v4 it does not center itself or add padding by default, so you usually add `mx-auto` and `px-4`.

```html
<div class="container mx-auto px-4">...</div>
```

### 76: How do you position an element absolutely?

Use `absolute` on the element and `relative` on the parent, then place it with `top-*`, `right-*`, `bottom-*`, `left-*` or `inset-*`.

```html
<div class="relative">
  <img src="/photo.jpg" alt="" />
  <span class="absolute top-2 right-2 rounded bg-black/60 px-2 text-white"
    >New</span
  >
</div>
```

### 77: What does `inset-0` do?

It sets `top`, `right`, `bottom` and `left` to `0`. It is often used to stretch an absolutely positioned overlay over its parent.

```html
<div class="absolute inset-0 bg-black/40"></div>
```

### 78: How do you make a sticky header?

```html
<header class="sticky top-0 z-10 bg-white">...</header>
```

`sticky` keeps the element in the normal flow until it reaches `top-0`, then it sticks.

### 79: How do you control stacking order?

Use `z-*` utilities, for example `z-0`, `z-10`, `z-20`, `z-50` or `z-auto`. In v4 any number works, like `z-15`. You can use `-z-10` for negative values.

### 80: How do you make an image cover its container without stretching?

Use `object-cover` with a fixed width and height.

```html
<img class="h-48 w-full object-cover" src="/banner.jpg" alt="" />
```

`object-contain` fits the whole image inside instead.

### 81: How do you set an aspect ratio?

Use `aspect-square`, `aspect-video`, or a ratio like `aspect-4/3`.

```html
<iframe class="aspect-video w-full" src="..."></iframe>
```

### 82: How do you handle overflow?

Use `overflow-hidden`, `overflow-auto`, `overflow-scroll`, `overflow-visible`, or axis versions like `overflow-x-auto` and `overflow-y-hidden`.

```html
<div class="overflow-x-auto">
  <table class="min-w-full">
    ...
  </table>
</div>
```

### 83: How do you change the cursor?

Use `cursor-pointer`, `cursor-default`, `cursor-not-allowed`, `cursor-wait`, `cursor-text`, `cursor-move` and others. Note that in v4 buttons use `cursor: default` by default (the browser default), so add `cursor-pointer` if you want the hand cursor.

### 84: How do you disable mouse events on an element?

Use `pointer-events-none`. Clicks pass through to whatever is underneath. `pointer-events-auto` restores the default.

### 85: How do you stop users from selecting text?

Use `select-none`. `select-all` selects the whole text on click, and `select-text` restores normal behavior.

### 86: How do you add a transition?

Use `transition` (common properties), `transition-colors`, `transition-opacity`, `transition-transform` or `transition-all`, together with `duration-*` and `ease-*`.

```html
<button
  class="bg-blue-500 transition-colors duration-200 ease-in-out hover:bg-blue-700"
>
  Hover
</button>
```

### 87: What built-in animations does Tailwind have?

`animate-spin`, `animate-ping`, `animate-pulse`, `animate-bounce`, and `animate-none`.

```html
<svg class="size-5 animate-spin">...</svg>
<div class="h-4 w-full animate-pulse rounded bg-gray-200"></div>
```

### 88: How do you scale an element?

Use `scale-*` (values are percentages). `scale-95` is 95%, `scale-110` is 110%. You can scale one axis with `scale-x-*` or `scale-y-*`.

```html
<div class="transition-transform hover:scale-105">Card</div>
```

### 89: How do you rotate an element?

Use `rotate-*` in degrees: `rotate-45`, `rotate-90`, `-rotate-12`. v4 also adds 3D rotation with `rotate-x-*` and `rotate-y-*`.

### 90: How do you move an element with translate?

Use `translate-x-*` and `translate-y-*`. Fractions work too.

```html
<div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2">
  Centered
</div>
```

### 91: Do you need the `transform` class to use scale, rotate or translate?

No. Since v3 the transform utilities work on their own. In v4 `scale`, `rotate` and `translate` use the separate CSS properties `scale`, `rotate` and `translate`, so no extra class is needed.

### 92: How do you set the transform origin?

Use `origin-center`, `origin-top`, `origin-top-left`, `origin-bottom-right` and so on.

### 93: How do you add a linear gradient background in v4?

Use `bg-linear-*` with color stops `from-*`, `via-*` and `to-*`.

```html
<div class="bg-linear-to-r from-cyan-500 to-blue-500">...</div>
```

In v3 the class was `bg-gradient-to-r`. v4 renamed it to `bg-linear-to-r`; the old name still works for now.

### 94: Can you set a gradient angle?

Yes. In v4 you can use degrees directly.

```html
<div class="bg-linear-45 from-pink-500 to-yellow-400">...</div>
```

### 95: Does v4 support radial and conic gradients?

Yes, with `bg-radial` and `bg-conic`.

```html
<div class="size-32 rounded-full bg-radial from-white to-sky-500"></div>
<div
  class="size-32 rounded-full bg-conic from-red-500 via-yellow-400 to-red-500"
></div>
```

### 96: How do you add a background image?

Use an arbitrary value with `url()`.

```html
<div class="bg-[url(/images/hero.jpg)] bg-cover bg-center">...</div>
```

### 97: What are `bg-cover` and `bg-contain`?

They set `background-size`. `bg-cover` scales the image to fill the element and may crop it. `bg-contain` scales it to fit inside without cropping. `bg-center` and `bg-no-repeat` are commonly used with them.

### 98: How do you style list bullets?

Use `list-disc`, `list-decimal` or `list-none`, and `list-inside` or `list-outside` for the marker position.

```html
<ol class="list-decimal pl-6">
  <li>First</li>
  <li>Second</li>
</ol>
```

### 99: What is an arbitrary value?

It is a way to use a value that is not in the theme by putting it in square brackets.

```html
<div class="top-[117px] bg-[#1da1f2] grid-cols-[200px_1fr]">...</div>
```

Spaces must be written as underscores (`_`).

### 100: How do you use a CSS variable as a value in v4?

Use parentheses:

```html
<div class="bg-(--brand-color) w-(--sidebar-width)">...</div>
```

This is short for `bg-[var(--brand-color)]`. In v3 the syntax was `bg-[--brand-color]`; v4 changed it to parentheses.

### 101: Can you combine variants?

Yes. You can stack them.

```html
<button class="dark:md:hover:bg-gray-700">...</button>
```

This applies in dark mode, on medium screens and up, while hovering.

### 102: What is the `group` class used for?

It lets you style a child based on the state of its parent. Mark the parent with `group`, then use `group-hover:`, `group-focus:` and similar on the children.

```html
<a href="#" class="group block rounded-lg p-4 hover:bg-sky-500">
  <h3 class="text-gray-900 group-hover:text-white">Title</h3>
  <p class="text-gray-500 group-hover:text-sky-100">Description</p>
</a>
```

### 103: What is the `peer` class used for?

It lets you style an element based on the state of a previous sibling. Mark the sibling with `peer` and use `peer-*` variants on later siblings.

```html
<input type="email" class="peer border" />
<p class="hidden text-sm text-red-600 peer-invalid:block">
  Please enter a valid email.
</p>
```

### 104: What are `first:` and `last:` variants?

They apply when the element is the first or last child of its parent.

```html
<ul>
  <li class="border-b py-2 first:pt-0 last:border-0">Item</li>
</ul>
```

### 105: What are `odd:` and `even:` variants?

They style odd or even children, often for zebra-striped tables.

```html
<tr class="odd:bg-white even:bg-gray-50">
  ...
</tr>
```

### 106: How do you style the placeholder of an input?

Use `placeholder:`.

```html
<input
  class="placeholder:text-gray-400 placeholder:italic"
  placeholder="Search..."
/>
```

### 107: What is the default placeholder color in v4?

In v4, placeholder text uses the current text color at 50% opacity. In v3 it used `gray-400`.

### 108: How do you add `::before` and `::after` content?

Use `before:` and `after:` variants. Tailwind adds `content: var(--tw-content)` automatically, so you only need `content-[...]` when you want actual text.

```html
<label class="after:ml-0.5 after:text-red-500 after:content-['*']">Email</label>
```

### 109: How do you style text selection?

Use `selection:`.

```html
<p class="selection:bg-yellow-200 selection:text-black">Select me</p>
```

### 110: How do you style the file input button?

Use `file:`.

```html
<input
  type="file"
  class="file:mr-4 file:rounded-full file:border-0 file:bg-violet-50 file:px-4 file:py-2"
/>
```

### 111: How do you style a checkbox color without custom CSS?

Use `accent-*`.

```html
<input type="checkbox" class="accent-pink-500" checked />
```

### 112: How do you change the text cursor (caret) color?

Use `caret-*`.

```html
<textarea class="caret-blue-500"></textarea>
```

### 113: How do you remove the default look of a select or input?

Use `appearance-none`, then style it yourself.

```html
<select class="appearance-none rounded border px-3 py-2">
  ...
</select>
```

### 114: How do you make content visible only to screen readers?

Use `sr-only`.

```html
<button>
  <svg>...</svg>
  <span class="sr-only">Close menu</span>
</button>
```

### 115: What is the difference between `outline-none` and `outline-hidden` in v4?

In v4 `outline-none` sets `outline-style: none`, which removes the outline completely, even in Windows high contrast mode. `outline-hidden` sets a transparent outline, so the element looks outline-free but still shows one in forced colors mode. In v3, `outline-none` behaved like the new `outline-hidden`.

### 116: How do you add a focus ring?

Use `ring-*` utilities with a color.

```html
<button class="focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">
  ...
</button>
```

### 117: What is the default `ring` width in v4?

`ring` is now 1px in v4 (it was 3px in v3). If you relied on the old 3px default, use `ring-3`. The default ring color is now `currentColor` instead of `blue-500`.

### 118: How do you add an outline?

Use `outline`, `outline-2`, `outline-4` with `outline-*` colors and `outline-offset-*`.

```html
<a
  class="focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
  >Link</a
>
```

### 119: How do you add a divider line between children?

Use `divide-y` or `divide-x` on the parent with a `divide-*` color.

```html
<ul class="divide-y divide-gray-200">
  <li class="py-3">One</li>
  <li class="py-3">Two</li>
</ul>
```

### 120: How do you add blur to an element?

Use `blur-*`, like `blur-sm`, `blur-md` or `blur-lg`. For the area behind an element use `backdrop-blur-*`.

```html
<nav class="sticky top-0 bg-white/70 backdrop-blur-md">...</nav>
```

### 121: What other filter utilities exist?

`brightness-*`, `contrast-*`, `grayscale`, `invert`, `sepia`, `saturate-*`, `hue-rotate-*` and `drop-shadow-*`. Each also has a `backdrop-` version. You don't need a `filter` class to enable them.

### 122: What are `whitespace-*` utilities?

They set `white-space`: `whitespace-normal`, `whitespace-nowrap`, `whitespace-pre`, `whitespace-pre-line`, `whitespace-pre-wrap` and `whitespace-break-spaces`.

### 123: How do you break long words that overflow?

Use `wrap-break-word` (sets `overflow-wrap: break-word`) or `wrap-anywhere`. `break-all` breaks between any characters.

```html
<p class="wrap-break-word">averyveryverylongwordwithoutspaces</p>
```

### 124: What do `text-balance` and `text-pretty` do?

`text-balance` tries to make lines of a heading roughly the same length. `text-pretty` avoids leaving a single word alone on the last line of a paragraph.

```html
<h1 class="text-4xl text-balance">A long headline that wraps nicely</h1>
```

### 125: How do you style a table?

Use normal utilities on table elements, plus `table-auto` or `table-fixed` for layout and `border-collapse` or `border-separate`.

```html
<table class="w-full table-auto border-collapse">
  <thead class="bg-gray-50 text-left text-sm font-medium">
    <tr>
      <th class="px-4 py-2">Name</th>
    </tr>
  </thead>
</table>
```

### 126: How do you set the color of SVG icons?

Use `fill-*` and `stroke-*`. `fill-current` and `stroke-current` use the text color, so the icon follows `text-*`.

```html
<svg class="size-6 fill-current text-green-600">...</svg>
```

### 127: How do you make a full-height page layout?

```html
<body class="flex min-h-dvh flex-col">
  <header>...</header>
  <main class="flex-1">...</main>
  <footer>...</footer>
</body>
```

The footer stays at the bottom even when there is little content.

### 128: How do you write a simple card component with Tailwind?

```html
<div class="max-w-sm overflow-hidden rounded-xl bg-white shadow-md">
  <img class="h-48 w-full object-cover" src="/card.jpg" alt="" />
  <div class="p-6">
    <h3 class="text-lg font-semibold text-gray-900">Card title</h3>
    <p class="mt-2 text-gray-600">Short description of the card.</p>
  </div>
</div>
```

### 129: How do you build a simple navbar?

```html
<nav
  class="flex items-center justify-between border-b border-gray-200 px-6 py-4"
>
  <a href="/" class="text-xl font-bold">Brand</a>
  <ul class="hidden gap-6 md:flex">
    <li><a href="#" class="hover:text-blue-600">Home</a></li>
    <li><a href="#" class="hover:text-blue-600">About</a></li>
  </ul>
</nav>
```

### 130: Does the order of classes in the `class` attribute matter?

No. The browser applies styles based on the order of rules in the CSS file and their specificity, not the order of class names in HTML. `class="p-4 p-2"` and `class="p-2 p-4"` give the same result. That is why you should avoid putting two conflicting utilities on one element.

### 131: Why shouldn't you build class names with string concatenation?

Tailwind scans your files as plain text. If you write `` `bg-${color}-500` ``, the full class name never appears in the source, so Tailwind won't generate it. Write full class names instead:

```js
const colors = {
  red: "bg-red-500",
  blue: "bg-blue-500",
};
<div className={colors[color]} />;
```

### 132: How do you use Tailwind in React?

Use the `className` attribute.

```jsx
export function Alert({ children }) {
  return (
    <div className="rounded-md bg-yellow-50 p-4 text-yellow-800">
      {children}
    </div>
  );
}
```

### 133: Does Tailwind add JavaScript to your page?

No. Tailwind runs at build time and outputs a plain CSS file. There is no runtime JavaScript in production (except the CDN browser build, which is meant for prototyping only).

### 134: What does `@apply` do?

It lets you use Tailwind utilities inside your own CSS rules.

```css
.btn-primary {
  @apply rounded-lg bg-blue-600 px-4 py-2 font-semibold text-white;
}
```

It is useful for third-party markup you can't add classes to, but the Tailwind team recommends components (React, Vue, etc.) over `@apply` for reuse.

### 135: What is the `@theme` directive?

It defines your design tokens (colors, fonts, breakpoints, spacing and more) as CSS variables. Tailwind creates utilities from them.

```css
@import "tailwindcss";

@theme {
  --color-brand: oklch(0.6 0.2 250);
  --font-display: "Inter", sans-serif;
}
```

Now `bg-brand`, `text-brand` and `font-display` work.

### 136: How do you add a custom color?

Add a `--color-*` variable in `@theme`.

```css
@theme {
  --color-mint-500: oklch(0.72 0.11 178);
}
```

```html
<div class="bg-mint-500 text-mint-500 border-mint-500">...</div>
```

### 137: Can you use theme values as normal CSS variables?

Yes. Every theme value is available as a CSS variable.

```css
.custom {
  color: var(--color-blue-600);
  padding: var(--spacing);
}
```

### 138: How do you write a CSS comment or custom CSS together with Tailwind?

You write normal CSS in the same file after `@import "tailwindcss";`. Comments use standard `/* ... */`.

```css
@import "tailwindcss";

/* custom styles */
.hero-title {
  font-size: clamp(2rem, 5vw, 4rem);
}
```

### 139: What is the `!` important modifier?

Adding `!` at the end of a class makes it `!important`.

```html
<p class="font-bold!">Always bold</p>
```

In v3 it went at the start (`!font-bold`). v4 moved it to the end; the old position still works but is deprecated.

### 140: How do you make a column layout like a newspaper?

Use `columns-*`.

```html
<div class="columns-3 gap-8">
  <p>...</p>
</div>
```

`columns-3` means three columns; `columns-xs` sets a column width instead.

### 141: What is `scroll-smooth`?

It sets `scroll-behavior: smooth`, so anchor links scroll smoothly instead of jumping.

```html
<html class="scroll-smooth"></html>
```

### 142: What are `inline-block` and `inline-flex` used for?

`inline-block` makes an element sit inline with text but accept width, height and vertical padding. `inline-flex` does the same but also makes it a flex container, which is useful for buttons with icons.

```html
<button class="inline-flex items-center gap-2">
  <svg class="size-4">...</svg> Download
</button>
```

### 143: How do you make a circle avatar?

```html
<img class="size-10 rounded-full object-cover" src="/me.jpg" alt="Profile" />
```

### 144: How do you set `box-sizing`?

Preflight already sets `border-box` on everything. You can change it per element with `box-content` or `box-border`.

### 145: What does `isolate` do?

It sets `isolation: isolate`, which creates a new stacking context. It helps contain `z-index` values and blend modes inside a component.

### 146: How do you hide the scrollbar or make it thin?

Since v4.3 there are native scrollbar utilities: `scrollbar-none` hides it, `scrollbar-thin` makes it thin, and `scrollbar-auto` restores the default.

```html
<div class="scrollbar-thin overflow-y-auto">...</div>
```

### 147: How do you style the placeholder with dark mode at the same time?

Stack the variants.

```html
<input class="placeholder:text-gray-400 dark:placeholder:text-gray-500" />
```

### 148: What does `contents` display do?

It sets `display: contents`, which makes the element's box disappear so its children act as children of the parent. It is useful when a wrapper element breaks a flex or grid layout.

### 149: Which browsers does Tailwind v4 support?

v4 targets modern browsers: Safari 16.4+, Chrome 111+ and Firefox 128+. It uses features like cascade layers, `@property` and `color-mix()`. If you need to support older browsers, stay on v3.4.

### 150: Where should you look for official Tailwind documentation and tools?

The official docs at tailwindcss.com, the Tailwind CSS IntelliSense extension for VS Code (autocomplete, hover previews, linting), and `prettier-plugin-tailwindcss` for automatic class sorting. The Tailwind Play website lets you try classes in the browser without installing anything.

## Moderate Questions (151-300)

### 151: How does the CSS-first configuration in v4 work?

All customization happens in your main CSS file using directives:

- `@theme` for design tokens (colors, fonts, breakpoints, etc.)
- `@utility` for custom utilities
- `@custom-variant` for custom variants
- `@plugin` for loading plugins
- `@source` for adding or excluding content paths

```css
@import "tailwindcss";
@plugin "@tailwindcss/typography";
@source "../packages/ui/src";

@theme {
  --color-primary: oklch(0.55 0.2 260);
  --breakpoint-3xl: 120rem;
}

@custom-variant dark (&:where(.dark, .dark *));

@utility content-auto {
  content-visibility: auto;
}
```

### 152: What are theme variable namespaces?

The prefix of a `@theme` variable decides which utilities it creates. Some common namespaces:

| Namespace          | Example utilities                                  |
| ------------------ | -------------------------------------------------- |
| `--color-*`        | `bg-red-500`, `text-sky-300`, `border-*`, `fill-*` |
| `--font-*`         | `font-sans`, `font-display`                        |
| `--text-*`         | `text-xl`                                          |
| `--font-weight-*`  | `font-bold`                                        |
| `--tracking-*`     | `tracking-wide`                                    |
| `--leading-*`      | `leading-tight`                                    |
| `--breakpoint-*`   | `sm:`, `md:`                                       |
| `--container-*`    | `@sm:`, `max-w-md`                                 |
| `--spacing`        | `p-4`, `m-2`, `w-10`, `gap-3`                      |
| `--radius-*`       | `rounded-lg`                                       |
| `--shadow-*`       | `shadow-md`                                        |
| `--inset-shadow-*` | `inset-shadow-xs`                                  |
| `--drop-shadow-*`  | `drop-shadow-md`                                   |
| `--text-shadow-*`  | `text-shadow-md`                                   |
| `--blur-*`         | `blur-md`                                          |
| `--perspective-*`  | `perspective-near`                                 |
| `--aspect-*`       | `aspect-video`                                     |
| `--ease-*`         | `ease-out`                                         |
| `--animate-*`      | `animate-spin`                                     |

### 153: How do you extend the theme versus replace it?

Adding variables in `@theme` extends the default theme. To replace a whole namespace, first reset it with `initial`.

```css
@theme {
  /* remove all default colors */
  --color-*: initial;

  --color-white: #fff;
  --color-black: #000;
  --color-primary: oklch(0.6 0.2 250);
}
```

To start from nothing for every namespace, use `--*: initial;`.

### 154: How do you override a single default value?

Redefine the variable with the same name.

```css
@theme {
  --breakpoint-sm: 36rem;
  --font-sans: "Inter", ui-sans-serif, system-ui, sans-serif;
}
```

### 155: How do you remove a single breakpoint?

Set it to `initial`.

```css
@theme {
  --breakpoint-2xl: initial;
}
```

The `2xl:` variant will no longer exist.

### 156: How do you add a custom breakpoint?

```css
@theme {
  --breakpoint-xs: 30rem;
  --breakpoint-3xl: 120rem;
}
```

```html
<div class="xs:grid-cols-2 3xl:grid-cols-6">...</div>
```

Breakpoints should use the same unit (rem in v4) so Tailwind can sort them correctly.

### 157: How do you use an arbitrary breakpoint without adding it to the theme?

Use `min-[...]` or `max-[...]`.

```html
<div class="min-[900px]:flex max-[600px]:text-sm">...</div>
```

### 158: What is the difference between `@theme` and `:root` variables?

Variables in `@theme` are theme tokens: Tailwind creates utility classes from them and also outputs them as CSS variables. Variables in `:root` are just CSS variables; they don't create any utilities. Use `@theme` when you want a class like `bg-brand`. Use `:root` for values you only read with `var()`.

### 159: Can `@theme` be nested inside a selector or media query?

No. `@theme` must be at the top level of the stylesheet. If you want values that change by context (like dark mode), define plain CSS variables in selectors and reference them from `@theme inline`.

### 160: What does `@theme inline` do?

Normally a theme variable creates a utility that points to the variable, like `font-family: var(--font-sans)`. If the theme value itself is another variable, this can resolve in the wrong place. `@theme inline` makes utilities use the actual value directly.

```css
@theme inline {
  --font-sans: var(--font-inter);
}
```

Now `font-sans` outputs `font-family: var(--font-inter)`, which is resolved on the element that uses the class. This matters when `--font-inter` is set on a specific element (for example by `next/font`).

### 161: What does `@theme static` do?

By default, Tailwind only outputs the CSS variables for theme values you actually use. `@theme static` forces all variables in that block to be output, which is useful if you read them from JavaScript or inline styles.

```css
@theme static {
  --color-primary: oklch(0.6 0.2 250);
}
```

### 162: How do you add a custom font in v4?

Load the font with `@font-face` or a link, then add it to the theme.

```css
@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap");
@import "tailwindcss";

@theme {
  --font-roboto: "Roboto", sans-serif;
}
```

```html
<p class="font-roboto">Hello</p>
```

Note that `@import url(...)` must come before `@import "tailwindcss"`.

### 163: How do you set a default line height for a custom font size?

Use the double-dash sub-property syntax.

```css
@theme {
  --text-tiny: 0.625rem;
  --text-tiny--line-height: 1.5rem;
  --text-tiny--letter-spacing: 0.02em;
  --text-tiny--font-weight: 500;
}
```

`text-tiny` will now set all four properties.

### 164: How do you change the spacing scale?

Change the single `--spacing` variable.

```css
@theme {
  --spacing: 0.2rem;
}
```

Now `p-4` is `0.8rem`. Every spacing-based utility (padding, margin, width, height, gap, inset, etc.) changes at once.

### 165: How do you define a custom utility in v4?

Use `@utility`.

```css
@utility content-auto {
  content-visibility: auto;
}
```

```html
<section class="content-auto hover:content-auto lg:content-auto">...</section>
```

Utilities defined this way work with all variants automatically.

### 166: Why use `@utility` instead of `@layer utilities` in v4?

In v3 you added utilities with `@layer utilities { .foo {...} }`. In v4 Tailwind uses native cascade layers, and `@layer utilities` is just a normal CSS layer. Classes there won't work with variants and won't be sorted together with Tailwind's own utilities. `@utility` registers it properly so it supports variants and `@apply`.

### 167: How do you add base styles in v4?

Use `@layer base`.

```css
@layer base {
  h1 {
    font-size: var(--text-2xl);
    font-weight: var(--font-weight-bold);
  }
  a {
    color: var(--color-blue-600);
  }
}
```

### 168: How do you add component classes in v4?

Use `@layer components`. Utilities will still override these because the utilities layer comes later.

```css
@layer components {
  .card {
    background-color: var(--color-white);
    border-radius: var(--radius-lg);
    padding: --spacing(6);
    box-shadow: var(--shadow-xl);
  }
}
```

```html
<div class="card rounded-none">Square card</div>
```

### 169: What is `--spacing()` in CSS?

It is a function that returns a value from the spacing scale.

```css
.sidebar {
  width: --spacing(64);
  padding: --spacing(4);
}
```

It compiles to `calc(var(--spacing) * 64)`. It also works inside arbitrary values: `py-[calc(--spacing(4)-1px)]`.

### 170: What is `--alpha()` in CSS?

It changes the opacity of a color.

```css
.overlay {
  background-color: --alpha(var(--color-black) / 50%);
}
```

It compiles to `color-mix(in oklab, var(--color-black) 50%, transparent)`.

### 171: Is the `theme()` function still supported in v4?

It still works but is deprecated. Use CSS variables instead: `var(--color-red-500)` rather than `theme(colors.red.500)`. The one place where `theme()` is still needed is in media queries, because CSS variables can't be used there:

```css
@media (width >= theme(--breakpoint-xl)) {
  /* ... */
}
```

### 172: How do you use `@apply` in Vue, Svelte or CSS modules in v4?

Those `<style>` blocks are processed separately, so they don't know about your theme. Use `@reference` to import your main stylesheet for reference only (no CSS is duplicated).

```vue
<style scoped>
@reference "../../app.css";

h1 {
  @apply text-2xl font-bold text-red-500;
}
</style>
```

If you only use the default theme, `@reference "tailwindcss";` is enough. Another option is to use CSS variables directly: `color: var(--color-red-500);`.

### 173: What does `@variant` do?

It applies a Tailwind variant inside your own CSS.

```css
.my-element {
  background: white;

  @variant dark {
    background: black;
  }
}
```

Since v4.3 you can stack variants (`@variant hover:focus { ... }`) or list several separated by commas (`@variant hover, focus { ... }`).

### 174: How do you create a custom variant?

Use `@custom-variant`.

```css
@custom-variant theme-midnight (&:where([data-theme="midnight"] *));
```

```html
<html data-theme="midnight">
  <button class="theme-midnight:bg-black">...</button>
</html>
```

For more complex variants, use a block with `@slot`:

```css
@custom-variant any-hover {
  @media (any-hover: hover) {
    &:hover {
      @slot;
    }
  }
}
```

### 175: How do you make dark mode toggle manually with a class?

Override the `dark` variant.

```css
@import "tailwindcss";
@custom-variant dark (&:where(.dark, .dark *));
```

Then add `class="dark"` to `<html>` with JavaScript when the user picks dark mode.

### 176: How do you use a data attribute for dark mode instead of a class?

```css
@custom-variant dark (&:where([data-theme=dark], [data-theme=dark] *));
```

```html
<html data-theme="dark">
  ...
</html>
```

### 177: How do you support light, dark and system modes together?

Use the class-based `dark` variant and a small script that runs before the page renders.

```html
<script>
  document.documentElement.classList.toggle(
    "dark",
    localStorage.theme === "dark" ||
      (!("theme" in localStorage) &&
        window.matchMedia("(prefers-color-scheme: dark)").matches),
  );
</script>
```

To choose: set `localStorage.theme = "light"`, `localStorage.theme = "dark"`, or `localStorage.removeItem("theme")` for system. Put the script in `<head>` so there is no flash of the wrong theme.

### 178: Why does the page flash light before switching to dark?

Because the theme is applied by JavaScript after the page has already been painted. Fix it by running the theme script inline in the `<head>`, before the body renders. In frameworks with SSR, you can also read a cookie on the server and render the `dark` class directly in the HTML.

### 179: What does `scheme-dark` do?

It sets `color-scheme: dark`, which tells the browser to draw native UI (scrollbars, form controls, date pickers) in dark style. Use `scheme-light`, `scheme-dark` or `scheme-light-dark`.

```html
<html class="dark:scheme-dark"></html>
```

### 180: How do you style based on a data attribute?

Use `data-*` variants. In v4, a boolean data attribute doesn't need brackets.

```html
<div data-active class="border data-active:border-purple-500">...</div>
<div data-size="large" class="data-[size=large]:p-8">...</div>
```

### 181: How do you style based on ARIA attributes?

Use `aria-*` variants.

```html
<button aria-expanded="true" class="aria-expanded:bg-gray-100">Menu</button>
<th aria-sort="ascending" class="aria-[sort=ascending]:bg-sky-50">Name</th>
```

Built-in ones include `aria-checked`, `aria-disabled`, `aria-expanded`, `aria-hidden`, `aria-pressed`, `aria-readonly`, `aria-required` and `aria-selected`.

### 182: What is the `has-*` variant?

It styles an element based on what it contains, using CSS `:has()`.

```html
<label
  class="rounded-lg border p-4 has-checked:border-indigo-600 has-checked:bg-indigo-50"
>
  <input type="radio" name="plan" /> Pro plan
</label>
```

You can use arbitrary selectors: `has-[img]:p-0`.

### 183: What are `group-has-*` and `peer-has-*`?

They combine `group`/`peer` with `:has()`.

```html
<div class="group">
  <img src="..." />
  <h4 class="group-has-[a]:underline">...</h4>
</div>
```

The heading is underlined only if the group contains a link.

### 184: What are named groups?

When groups are nested, you can name them with `group/{name}` so a child reacts to a specific parent.

```html
<ul>
  <li class="group/item">
    <a class="group/edit invisible group-hover/item:visible">
      <span class="group-hover/edit:text-gray-700">Edit</span>
    </a>
  </li>
</ul>
```

Peers can be named the same way: `peer/email` and `peer-invalid/email:`.

### 185: What is the `not-*` variant?

It applies styles when a condition is not true. It works with pseudo-classes, other variants and media queries.

```html
<button class="not-disabled:hover:bg-blue-700">...</button>
<div class="not-supports-[display:grid]:flex">...</div>
<div class="not-first:mt-4">...</div>
```

### 186: What is the `in-*` variant?

It is like `group-*` but you don't need to add the `group` class to the parent. It matches when any ancestor has that state.

```html
<div tabindex="0">
  <p class="text-gray-500 in-focus:text-gray-900">...</p>
</div>
```

### 187: What are the `*` and `**` variants?

`*:` styles all direct children. `**:` styles all descendants.

```html
<ul class="*:rounded-full *:border *:px-2 *:py-0.5">
  <li>Sales</li>
  <li>Marketing</li>
</ul>
```

Use them only when you can't add classes to the children directly, since styles on the child itself are easier to follow.

### 188: What are `nth-*` variants?

v4 includes `nth-*`, `nth-last-*`, `nth-of-type-*` and `nth-last-of-type-*`.

```html
<li class="nth-3:underline">...</li>
<li class="nth-[3n+1]:bg-gray-50">...</li>
```

### 189: What are arbitrary variants?

They let you write a custom selector inside square brackets, using `&` for the element.

```html
<ul class="[&>li]:py-2 [&_a]:text-blue-600">
  ...
</ul>
<div class="[&:nth-child(3)]:font-bold">...</div>
<div class="[@supports(display:grid)]:grid">...</div>
```

### 190: How do you use `supports-*`?

It applies styles only if the browser supports a CSS feature.

```html
<div class="flex supports-[display:grid]:grid">...</div>
<div
  class="bg-black/75 supports-backdrop-filter:bg-black/25 supports-backdrop-filter:backdrop-blur"
>
  ...
</div>
```

### 191: How do you style for reduced motion?

Use `motion-safe:` and `motion-reduce:`.

```html
<svg class="motion-safe:animate-spin">...</svg>
<div class="transition motion-reduce:transition-none">...</div>
```

### 192: What other accessibility media variants exist?

- `contrast-more:` and `contrast-less:` for `prefers-contrast`
- `forced-colors:` for Windows high contrast mode
- `inverted-colors:` for inverted color setting
- `pointer-fine:`, `pointer-coarse:`, `any-pointer-*:` for input type
- `print:` for printing
- `portrait:` and `landscape:` for orientation

### 193: How do you style elements based on RTL or LTR direction?

Use `rtl:` and `ltr:`, but prefer logical utilities when possible.

```html
<div class="ms-3">Margin on the start side</div>
<div class="ltr:ml-3 rtl:mr-3">Same thing, longer</div>
```

### 194: What are logical property utilities?

They use start/end instead of left/right so they flip automatically in RTL layouts:

- `ms-*`, `me-*` (margin-inline-start/end)
- `ps-*`, `pe-*` (padding-inline-start/end)
- `border-s`, `border-e`, `rounded-s-*`, `rounded-e-*`
- `text-start`, `text-end`

v4.2 added block-direction versions: `pbs-*`, `pbe-*`, `mbs-*`, `mbe-*`, `border-bs`, `border-be`, and logical insets `inset-s-*`, `inset-e-*`, `inset-bs-*`, `inset-be-*`.

### 195: What happened to `start-*` and `end-*` in v4.2?

They were deprecated in favor of `inset-s-*` and `inset-e-*`, so they match the new block-direction `inset-bs-*` and `inset-be-*` utilities.

### 196: What are `inline-*` and `block-*` size utilities?

Added in v4.2, they set `inline-size` and `block-size`, the logical versions of width and height. There are also `min-inline-*`, `max-inline-*`, `min-block-*` and `max-block-*`.

```html
<div class="inline-64 max-block-screen">...</div>
```

### 197: What are container queries?

They let an element change style based on the size of its parent container, not the viewport. In v4 they are built in.

```html
<div class="@container">
  <div class="flex flex-col @md:flex-row">...</div>
</div>
```

`@md:` means "when the container is at least 28rem wide".

### 198: When should you use container queries instead of breakpoints?

Use container queries for reusable components that can appear in places of different width, like a card that might be in a narrow sidebar or a wide main area. Use viewport breakpoints for page-level layout like showing or hiding the sidebar.

### 199: How do you use max-width and range container queries?

```html
<div class="@container">
  <div class="@max-md:flex-col">...</div>
  <div class="flex-row @sm:@max-md:flex-col">...</div>
</div>
```

The second one applies only when the container is between `@sm` and `@md`.

### 200: What are named containers?

When containers are nested, name them so a child can target a specific one.

```html
<div class="@container/main">
  <div class="@container/card">
    <div class="@lg/main:grid-cols-3">...</div>
  </div>
</div>
```

### 201: What are the default container query sizes?

They come from `--container-*`: `@3xs` (16rem), `@2xs` (18rem), `@xs` (20rem), `@sm` (24rem), `@md` (28rem), `@lg` (32rem), `@xl` (36rem), `@2xl` (42rem), `@3xl` (48rem), `@4xl` (56rem), `@5xl` (64rem), `@6xl` (72rem), `@7xl` (80rem). You can add arbitrary ones like `@min-[475px]:`.

### 202: What is `@container-size` in v4.3?

`@container` creates an inline-size container, which only knows its width. `@container-size` creates a size container that also tracks height, so units like `cqh` and `cqb` work.

```html
<div class="@container-size h-96">
  <div class="h-[50cqb]">Half the container height</div>
</div>
```

### 203: How do you use container query units?

Use arbitrary values with `cqw`, `cqh`, `cqi` or `cqb`.

```html
<div class="@container">
  <h2 class="text-[8cqw]">Scales with container width</h2>
</div>
```

### 204: How do you add a custom animation in v4?

Define `--animate-*` and the `@keyframes` inside `@theme`.

```css
@theme {
  --animate-wiggle: wiggle 1s ease-in-out infinite;

  @keyframes wiggle {
    0%,
    100% {
      transform: rotate(-3deg);
    }
    50% {
      transform: rotate(3deg);
    }
  }
}
```

```html
<span class="animate-wiggle">👋</span>
```

### 205: What is the `starting:` variant?

It uses CSS `@starting-style` to set the initial style of an element when it first appears, so you can animate entry without JavaScript.

```html
<div
  popover
  id="menu"
  class="opacity-100 transition-opacity starting:open:opacity-0"
>
  ...
</div>
```

### 206: What does `transition-discrete` do?

It sets `transition-behavior: allow-discrete`, which allows transitions on properties like `display` that normally switch instantly. Combined with `starting:` it lets you fade elements in and out when they go from `hidden` to visible.

```html
<div
  class="hidden opacity-0 transition-all transition-discrete group-open:block group-open:opacity-100"
>
  ...
</div>
```

### 207: How do you set an arbitrary transition duration or easing?

```html
<div
  class="transition duration-[400ms] ease-[cubic-bezier(0.95,0.05,0.795,0.035)]"
>
  ...
</div>
```

Or add values to the theme with `--ease-*`.

### 208: How do you add a delay to a transition?

Use `delay-*`, for example `delay-150`. Any number works in v4, since the value is in milliseconds.

### 209: How do you control which properties transition?

Pick a specific transition utility: `transition-colors`, `transition-opacity`, `transition-shadow`, `transition-transform`, or use an arbitrary value: `transition-[height]`.

### 210: What are 3D transform utilities in v4?

- `perspective-*` on the parent (`perspective-near`, `perspective-distant`, `perspective-[800px]`)
- `rotate-x-*`, `rotate-y-*`, `rotate-z-*`
- `translate-z-*`, `scale-z-*`
- `transform-3d` (`transform-style: preserve-3d`)
- `backface-hidden` and `backface-visible`

```html
<div class="perspective-distant">
  <article class="rotate-x-51 rotate-z-43 transform-3d">...</article>
</div>
```

### 211: How do you make gradient color stops at specific positions?

Add `from-*%`, `via-*%` and `to-*%`.

```html
<div
  class="bg-linear-to-r from-indigo-500 from-10% via-sky-500 via-30% to-emerald-500 to-90%"
>
  ...
</div>
```

### 212: What are gradient interpolation modifiers?

You can choose which color space the gradient mixes in by adding a modifier.

```html
<div class="bg-linear-to-r/srgb from-indigo-500 to-teal-400"></div>
<div class="bg-linear-to-r/oklch from-indigo-500 to-teal-400"></div>
```

The default in v4 is `oklab`. Options include `srgb`, `hsl`, `oklab`, `oklch`, `longer`, `shorter`, `increasing` and `decreasing`.

### 213: How do you make gradient text?

```html
<h1
  class="bg-linear-to-r from-pink-500 to-violet-500 bg-clip-text text-5xl font-extrabold text-transparent"
>
  Gradient text
</h1>
```

### 214: What are inset shadows and inset rings?

v4 adds `inset-shadow-*` and `inset-ring-*`, which can be used together with normal `shadow-*` and `ring-*` on the same element (up to four layers).

```html
<button
  class="shadow-md ring-1 ring-black/5 inset-shadow-sm inset-ring inset-ring-white/20"
>
  Button
</button>
```

### 215: What are text shadow utilities?

Added in v4.1: `text-shadow-2xs` up to `text-shadow-lg`, with colors and opacity.

```html
<p class="text-shadow-lg">Big shadow</p>
<p class="text-shadow-sky-300">Colored shadow</p>
<p class="text-shadow-lg/20">Shadow at 20% opacity</p>
```

### 216: How do you add a colored drop shadow?

Since v4.1, `drop-shadow-*` accepts colors and opacity.

```html
<svg class="drop-shadow-xl drop-shadow-cyan-500/50">...</svg>
```

### 217: What are mask utilities?

v4.1 added `mask-*` utilities for CSS masks. They can fade an element at its edges with gradients or use images.

```html
<img class="mask-b-from-50% mask-b-to-100%" src="/photo.jpg" />
<div class="mask-radial-from-60% mask-radial-at-center">...</div>
<div class="mask-[url(/shape.svg)]">...</div>
```

### 218: How do you style form validation states?

Use `invalid:`, `valid:`, `required:`, `user-invalid:` and `user-valid:`.

```html
<input
  required
  class="border user-invalid:border-red-500 user-valid:border-green-500"
/>
```

`user-invalid:` only applies after the user has interacted with the field, so you don't show errors on page load.

### 219: What is `field-sizing-content`?

It makes inputs and textareas grow with their content automatically.

```html
<textarea class="field-sizing-content min-h-20"></textarea>
```

### 220: What is the `@tailwindcss/forms` plugin?

It resets form controls to a plain, easy-to-style look. In v4 you load it with `@plugin`.

```css
@import "tailwindcss";
@plugin "@tailwindcss/forms";
```

With `@plugin "@tailwindcss/forms" { strategy: "class"; }` it only styles elements with classes like `form-input`.

### 221: What is the `@tailwindcss/typography` plugin?

It adds `prose` classes that style HTML you don't control, like Markdown or CMS content.

```css
@plugin "@tailwindcss/typography";
```

```html
<article class="prose lg:prose-xl dark:prose-invert">
  <!-- rendered markdown -->
</article>
```

Use `not-prose` to opt a section out.

### 222: How do you customize `prose` elements with utilities?

Use element modifiers.

```html
<article
  class="prose prose-headings:font-bold prose-a:text-blue-600 prose-img:rounded-xl"
>
  ...
</article>
```

### 223: Which v3 plugins are built into v4 core?

Container queries (`@tailwindcss/container-queries`), aspect ratio and line clamp are now core features. You don't need those plugins in v4.

### 224: How do you load a JavaScript plugin in v4?

Use `@plugin` with a package name or a path.

```css
@plugin "@tailwindcss/typography";
@plugin "./plugins/my-plugin.js";
```

### 225: How do you load a v3-style `tailwind.config.js` in v4?

Use `@config`.

```css
@import "tailwindcss";
@config "../../tailwind.config.js";
```

Note that some options are not supported in v4: `corePlugins`, `safelist` and `separator`. Safelisting is now done with `@source inline()`.

### 226: How do you tell Tailwind to scan a folder it ignores by default?

Use `@source`.

```css
@import "tailwindcss";
@source "../node_modules/@my-company/ui-lib";
```

This is common when a UI library in `node_modules` uses Tailwind classes, since `node_modules` is ignored by default.

### 227: How do you stop Tailwind from scanning a folder?

Use `@source not` (v4.1+).

```css
@source not "../src/legacy";
```

### 228: How do you turn off automatic source detection?

Use `source(none)` and list sources yourself.

```css
@import "tailwindcss" source(none);
@source "../admin";
@source "../shared";
```

You can also change the base path: `@import "tailwindcss" source("../src");`.

### 229: How do you safelist classes in v4?

Use `@source inline()`. It supports brace expansion.

```css
@source inline("underline");
@source inline("{hover:,focus:,}bg-red-{50,{100..900..100},950}");
```

The second line generates every red background shade, plus hover and focus versions.

### 230: How do you handle dynamic classes from a CMS or API?

Since the class names aren't in your source code, Tailwind won't see them. Options:

1. Map API values to full class names in your code.
2. Safelist the needed classes with `@source inline()`.
3. Use inline styles or CSS variables for truly dynamic values, like `style={{ "--card-color": color }}` with `bg-(--card-color)`.

### 231: How do you pass a dynamic value from JavaScript into a Tailwind class?

Set a CSS variable with inline style and read it with the variable shorthand.

```jsx
<div
  style={{ "--progress": `${percent}%` }}
  className="h-2 w-(--progress) rounded bg-green-500"
/>
```

The class `w-(--progress)` is static so Tailwind can find it, and the value changes at runtime.

### 232: When is a type hint needed in arbitrary values?

When the value could mean different things. For example, `text-*` can be a color or a font size. With a CSS variable Tailwind can't tell which, so add a hint.

```html
<p class="text-(length:--my-size)">Font size</p>
<p class="text-(color:--my-color)">Color</p>
<p class="text-[length:var(--x)]">Same with brackets</p>
```

### 233: What are arbitrary properties?

They let you set any CSS property that Tailwind has no utility for.

```html
<div class="[mask-type:luminance] hover:[mask-type:alpha]">...</div>
<div class="[--scroll-offset:56px] lg:[--scroll-offset:44px]">...</div>
```

### 234: How do you write spaces and underscores in arbitrary values?

Spaces are written as `_`. If you need a real underscore, escape it with a backslash.

```html
<div class="grid-cols-[1fr_500px_2fr]">...</div>
<div class="before:content-['hello\_world']">...</div>
```

In JSX you may need `String.raw` or a double backslash.

### 235: How do you add opacity to an arbitrary color or CSS variable?

```html
<div class="bg-[#0ea5e9]/50">...</div>
<div class="bg-(--brand)/25">...</div>
<div class="bg-sky-500/[0.33]">...</div>
<div class="bg-sky-500/(--my-opacity)">...</div>
```

Tailwind uses `color-mix()` behind the scenes, so it works even with CSS variables.

### 236: Why use `@utility` and not just `@layer components` for reusable classes?

Classes defined with `@utility` can be used with variants (`hover:btn`) and `@apply`, and they get sorted with other utilities, so other utilities can still override them based on property count. `@layer components` is fine for classes that you only use as-is and want utilities to override.

### 237: Can you `@apply` a custom class in v4?

Yes, but only if it is defined with `@utility`. In v4 you can't `@apply` an arbitrary CSS class that was written with `@layer components`.

```css
@utility btn {
  @apply rounded-md px-4 py-2 font-medium;
}

@utility btn-primary {
  @apply btn bg-blue-600 text-white;
}
```

### 238: Why is overusing `@apply` considered a bad practice?

- You go back to inventing class names and maintaining a separate CSS file.
- Changes in one class can affect many places, which is what utility classes try to avoid.
- CSS size grows because the same declarations are repeated.
- It hides the styling from the markup.

It is better to make a component in your framework (React, Vue, Angular, etc.) and keep utilities in its template.

### 239: How do you reuse styles without `@apply`?

- Create components (`<Button />`) with the classes inside.
- Use loops for repeated markup.
- Use multi-cursor editing for small repeated chunks.
- Use helpers like `cva` for variants.

```jsx
function Button({ children }) {
  return (
    <button className="rounded-md bg-blue-600 px-4 py-2 text-white hover:bg-blue-700">
      {children}
    </button>
  );
}
```

### 240: How do you set up Tailwind in Next.js with v4?

```bash
npm install tailwindcss @tailwindcss/postcss postcss
```

```js
// postcss.config.mjs
export default {
  plugins: { "@tailwindcss/postcss": {} },
};
```

```css
/* app/globals.css */
@import "tailwindcss";
```

```jsx
// app/layout.jsx
import "./globals.css";
```

New projects created with `create-next-app` set this up for you.

### 241: How do you use `next/font` with Tailwind v4?

Expose the font as a CSS variable and map it in `@theme inline`.

```jsx
import { Inter } from "next/font/google";
const inter = Inter({ subsets: ["latin"], variable: "--font-inter" });

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={inter.variable}>
      <body className="font-sans">{children}</body>
    </html>
  );
}
```

```css
@theme inline {
  --font-sans: var(--font-inter);
}
```

### 242: How do you set up Tailwind in an Angular project?

Install Tailwind with the PostCSS plugin and add a `.postcssrc.json` file.

```bash
npm install tailwindcss @tailwindcss/postcss postcss
```

```json
{
  "plugins": {
    "@tailwindcss/postcss": {}
  }
}
```

```css
/* src/styles.css */
@import "tailwindcss";
```

Recent Angular CLI versions can do this when you run `ng new` or with `ng add tailwindcss`.

### 243: How do you use Tailwind with component styles in Angular?

Component stylesheets are processed separately, so if you want `@apply` or theme values there, add `@reference`.

```css
/* button.component.css */
@reference "../../styles.css";

:host {
  @apply inline-flex;
}
```

Most of the time it is simpler to put utility classes directly in the template.

### 244: Can you use Tailwind v4 with Sass, Less or Stylus?

Not officially. v4 is designed to be your preprocessor: it handles imports, nesting, variables and vendor prefixes. Using it inside `.scss` files is not supported. Keep Tailwind in a plain `.css` file. If you must keep Sass, compile the Sass separately.

### 245: Does Tailwind v4 support CSS nesting?

Yes. v4 processes CSS with Lightning CSS, which supports native nesting syntax and lowers it for the target browsers.

```css
.card {
  padding: --spacing(4);

  &:hover {
    background: var(--color-gray-50);
  }
}
```

### 246: Do you still need autoprefixer with v4?

No. Tailwind v4 adds vendor prefixes itself using Lightning CSS. You can remove `autoprefixer` and `postcss-import` from your PostCSS config.

### 247: What is the Tailwind upgrade tool?

It is a command that migrates a v3 project to v4 automatically.

```bash
npx @tailwindcss/upgrade
```

It updates dependencies, moves the JS config to CSS where possible, replaces `@tailwind` directives with `@import`, and renames changed classes in your templates. Run it on a new git branch and review the diff. It requires Node.js 20 or newer.

### 248: What are the main breaking changes from v3 to v4?

- `@tailwind` directives replaced by `@import "tailwindcss"`.
- Config moved to CSS (`@theme`).
- Renamed scales: `shadow-sm` → `shadow-xs`, `rounded` → `rounded-sm`, etc.
- `outline-none` → `outline-hidden`; `ring` is 1px instead of 3px.
- Default border and ring color is `currentColor`.
- `bg-opacity-*` and similar removed.
- `flex-grow`/`flex-shrink` → `grow`/`shrink`; `overflow-ellipsis` → `text-ellipsis`; `decoration-slice` → `box-decoration-slice`.
- CSS variable syntax: `bg-[--x]` → `bg-(--x)`.
- Important modifier moved to the end.
- Variant stacking order is now left to right.
- `hover:` only on devices that support hover.
- `space-*` and `divide-*` selectors changed.
- Custom utilities need `@utility`.

### 249: What changed in the order of stacked variants in v4?

In v3 stacked variants were applied right to left. In v4 they are applied left to right, like CSS selectors are read. This matters for some combinations:

```html
<!-- v3 -->
<ul class="first:*:pt-0">
  <!-- v4 -->
  <ul class="*:first:pt-0"></ul>
</ul>
```

### 250: What changed with `space-y-*` in v4?

The selector changed from `> :not([hidden]) ~ :not([hidden])` (margin-top on every child after the first) to `> :not(:last-child)` with margin-bottom. This is faster but can change layouts that relied on the old behavior, for example with inline elements or custom margins on children. Using `flex flex-col gap-*` avoids the issue.

### 251: Why does my `border` look darker after upgrading to v4?

Because the default border color changed from `gray-200` to `currentColor`. Add explicit color classes like `border-gray-200`, or restore the old default in base styles:

```css
@layer base {
  *,
  ::after,
  ::before,
  ::backdrop,
  ::file-selector-button {
    border-color: var(--color-gray-200, currentColor);
  }
}
```

### 252: How do you restore the v3 `hover` behavior on touch devices?

Override the variant:

```css
@custom-variant hover (&:hover);
```

### 253: How do you restore pointer cursor on buttons in v4?

```css
@layer base {
  button:not(:disabled),
  [role="button"]:not(:disabled) {
    cursor: pointer;
  }
}
```

### 254: How do you customize the `container` class in v4?

There are no `center` or `padding` options anymore. Extend it with `@utility`.

```css
@utility container {
  margin-inline: auto;
  padding-inline: 2rem;
}
```

### 255: How do you add a prefix to all Tailwind classes?

Add `prefix()` to the import.

```css
@import "tailwindcss" prefix(tw);
```

```html
<div class="tw:flex tw:bg-red-500 tw:hover:bg-red-600">...</div>
```

In v4 the prefix looks like a variant and always comes first. Theme variables don't get the prefix in class names, but the generated CSS variables do (`--tw-color-red-500`).

### 256: Why would you use a prefix?

To avoid name clashes when Tailwind is added to a project that already has its own classes, or when a widget is embedded in someone else's page that might have classes like `.hidden` or `.container`.

### 257: How do you make all utilities `!important`?

```css
@import "tailwindcss" important;
```

This is useful when Tailwind has to override styles from an older CSS codebase with high specificity.

### 258: What is the `prettier-plugin-tailwindcss`?

It is an official Prettier plugin that sorts Tailwind classes in a consistent order (the same order as in the CSS output). It removes arguments about class order in code reviews.

```bash
npm install -D prettier prettier-plugin-tailwindcss
```

```json
{
  "plugins": ["prettier-plugin-tailwindcss"],
  "tailwindStylesheet": "./src/app.css"
}
```

In v4 you point it to your CSS file with `tailwindStylesheet` so it knows about custom utilities.

### 259: How can the Prettier plugin sort classes in function calls like `clsx`?

Use the `tailwindFunctions` option.

```json
{
  "plugins": ["prettier-plugin-tailwindcss"],
  "tailwindFunctions": ["clsx", "cn", "cva"]
}
```

### 260: What does the Tailwind CSS IntelliSense extension do?

It adds autocomplete for class names, a hover preview of the generated CSS, color swatches, linting for conflicting classes, and support for your custom theme. You can add `classRegex` settings so it works inside custom functions.

### 261: What is `clsx` and why is it used with Tailwind?

`clsx` builds a class string from conditions.

```jsx
import clsx from "clsx";

<button
  className={clsx(
    "rounded px-4 py-2",
    isActive ? "bg-blue-600 text-white" : "bg-gray-100",
    disabled && "opacity-50",
  )}
/>;
```

### 262: What is `tailwind-merge`?

It merges Tailwind class strings and removes conflicting classes so the last one wins.

```js
import { twMerge } from "tailwind-merge";

twMerge("px-2 py-1 bg-red-500", "p-3 bg-blue-500");
// => "p-3 bg-blue-500"
```

It is needed when a component has default classes and accepts a `className` prop for overrides.

### 263: What is the `cn` helper?

It is a common helper (popularized by shadcn/ui) that combines `clsx` and `tailwind-merge`.

```ts
import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
```

```jsx
<Button className={cn("w-full", isLoading && "opacity-70")} />
```

### 264: What is `cva` (class-variance-authority)?

It is a library to define component variants with Tailwind classes in a typed way.

```ts
import { cva } from "class-variance-authority";

const button = cva("inline-flex items-center rounded-md font-medium", {
  variants: {
    intent: {
      primary: "bg-blue-600 text-white hover:bg-blue-700",
      secondary: "bg-gray-100 text-gray-900 hover:bg-gray-200",
    },
    size: {
      sm: "h-8 px-3 text-sm",
      md: "h-10 px-4",
    },
  },
  defaultVariants: { intent: "primary", size: "md" },
});

button({ intent: "secondary", size: "sm" });
```

### 265: How do you build a responsive navbar with a mobile menu?

```jsx
function Navbar() {
  const [open, setOpen] = useState(false);
  return (
    <nav className="border-b bg-white">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-4 py-3">
        <a href="/" className="font-bold">
          Brand
        </a>
        <button
          className="md:hidden"
          onClick={() => setOpen(!open)}
          aria-expanded={open}
        >
          <span className="sr-only">Toggle menu</span>☰
        </button>
        <ul className="hidden gap-6 md:flex">
          <li>
            <a href="#">Home</a>
          </li>
          <li>
            <a href="#">Docs</a>
          </li>
        </ul>
      </div>
      <ul className={open ? "space-y-2 px-4 pb-4 md:hidden" : "hidden"}>
        <li>
          <a href="#">Home</a>
        </li>
        <li>
          <a href="#">Docs</a>
        </li>
      </ul>
    </nav>
  );
}
```

### 266: How do you build a responsive card grid that fits as many cards as possible?

```html
<div class="grid grid-cols-[repeat(auto-fill,minmax(16rem,1fr))] gap-6">
  <div class="rounded-lg border p-4">...</div>
</div>
```

The grid adds columns as space allows, with no breakpoints needed.

### 267: How do you build a modal overlay?

```html
<div
  class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4"
>
  <div
    role="dialog"
    aria-modal="true"
    class="w-full max-w-md rounded-xl bg-white p-6 shadow-xl"
  >
    <h2 class="text-lg font-semibold">Confirm</h2>
    <p class="mt-2 text-gray-600">Are you sure?</p>
    <div class="mt-6 flex justify-end gap-3">
      <button class="rounded-md px-4 py-2 hover:bg-gray-100">Cancel</button>
      <button class="rounded-md bg-red-600 px-4 py-2 text-white">Delete</button>
    </div>
  </div>
</div>
```

With the native `<dialog>` element you can style the backdrop with `backdrop:bg-black/50`.

### 268: How do you style a native `<dialog>` and its backdrop?

```html
<dialog
  class="rounded-xl p-6 shadow-xl backdrop:bg-black/50 backdrop:backdrop-blur-sm open:flex open:flex-col"
>
  ...
</dialog>
```

### 269: How do you build an accordion with `<details>` and Tailwind?

```html
<details class="group rounded-lg border p-4">
  <summary
    class="flex cursor-pointer list-none items-center justify-between font-medium"
  >
    What is Tailwind?
    <span class="transition-transform group-open:rotate-180">⌄</span>
  </summary>
  <p class="mt-3 text-gray-600">A utility-first CSS framework.</p>
</details>
```

v4.1 also added the `details-content:` variant for styling the content container of `<details>`.

### 270: How do you build a sidebar layout that collapses on mobile?

```html
<div class="flex min-h-dvh">
  <aside class="hidden w-64 shrink-0 border-r bg-gray-50 lg:block">...</aside>
  <main class="min-w-0 flex-1 p-6">...</main>
</div>
```

`min-w-0` on `main` prevents wide content (tables, code blocks) from pushing the layout wider.

### 271: Why doesn't `truncate` work inside a flex item?

Flex items have `min-width: auto` by default, so they won't shrink below their content width. Add `min-w-0` to the flex item (or its parent flex item) so it can shrink and the text can truncate.

```html
<div class="flex">
  <div class="min-w-0 flex-1">
    <p class="truncate">Very long text...</p>
  </div>
</div>
```

### 272: How do you make a sticky footer?

```html
<div class="grid min-h-dvh grid-rows-[auto_1fr_auto]">
  <header>...</header>
  <main>...</main>
  <footer>...</footer>
</div>
```

### 273: What is subgrid and how do you use it?

`subgrid` lets a nested grid use the tracks of its parent grid, so content in sibling cards lines up.

```html
<div class="grid grid-cols-3 gap-4">
  <div class="col-span-3 grid grid-cols-subgrid">
    <div class="col-start-2">Aligned to parent column 2</div>
  </div>
</div>
```

There is also `grid-rows-subgrid`.

### 274: What are `grid-flow-dense` and `auto-rows-*`?

`grid-flow-dense` fills empty gaps in the grid with later items when they fit. `auto-rows-*` sets the size of rows that are created automatically, for example `auto-rows-fr` or `auto-rows-[200px]`.

### 275: How do you use scroll snap?

```html
<div class="flex snap-x snap-mandatory gap-4 overflow-x-auto">
  <img class="w-80 shrink-0 snap-center" src="1.jpg" />
  <img class="w-80 shrink-0 snap-center" src="2.jpg" />
</div>
```

### 276: What are `scroll-mt-*` and `scroll-pt-*` used for?

They set scroll margin and scroll padding. A common use is to stop a sticky header from covering a heading when you jump to an anchor.

```html
<h2 id="pricing" class="scroll-mt-20">Pricing</h2>
```

### 277: What are `overscroll-*` utilities?

They control what happens when you reach the end of a scroll area. `overscroll-contain` stops the scroll from passing to the page behind a modal or dropdown. `overscroll-none` also disables the bounce effect.

### 278: How do you style scrollbar colors in v4.3?

```html
<div
  class="scrollbar-thin scrollbar-thumb-sky-700 scrollbar-track-sky-100 overflow-auto"
>
  ...
</div>
```

`scrollbar-thumb-*` and `scrollbar-track-*` accept any color and opacity modifiers.

### 279: What is `scrollbar-gutter-stable`?

It reserves space for the scrollbar even when the content doesn't overflow, so the layout doesn't jump when a scrollbar appears. Added in v4.3 along with `scrollbar-gutter-auto` and `scrollbar-gutter-both`.

### 280: What are the `zoom-*` and `tab-*` utilities in v4.3?

`zoom-*` sets the CSS `zoom` property (`zoom-75`, `zoom-125`, `zoom-[1.1]`). `tab-*` sets `tab-size`, which controls how wide tab characters are in code blocks (`tab-2`, `tab-8`).

```html
<pre class="tab-4">...</pre>
```

### 281: What does `font-features-*` do?

Added in v4.2, it sets `font-feature-settings`.

```html
<span class="font-features-['tnum']">1,234.56</span>
```

For common numeric features there are also `tabular-nums`, `oldstyle-nums`, `slashed-zero`, `lining-nums` and others.

### 282: What are `tabular-nums` used for?

They make all digits the same width so numbers line up in tables or in counters that change, without shifting.

```html
<td class="text-right tabular-nums">1,024.00</td>
```

### 283: What is `font-stretch-*`?

v4 added `font-stretch-*` to select condensed or expanded widths of variable fonts, for example `font-stretch-condensed` or `font-stretch-125%`.

### 284: How do you align items to the last baseline?

v4.1 added `items-baseline-last` and `self-baseline-last`, which align flex or grid items using the last line of text instead of the first.

### 285: What are "safe" alignment utilities?

v4.1 added utilities like `justify-center-safe` and `items-center-safe`. They center content but fall back to start alignment when the content overflows, so it doesn't get cut off on both sides.

### 286: How do you style the first line or first letter of text?

```html
<p
  class="first-letter:float-left first-letter:mr-2 first-letter:text-6xl first-letter:font-bold first-line:uppercase"
>
  Drop cap paragraph...
</p>
```

### 287: How do you style list markers?

Use `marker:`.

```html
<ul class="list-disc marker:text-sky-400">
  ...
</ul>
```

`marker:` can be set on the `<ul>` and is inherited by the list items.

### 288: How do you style an open `<details>` or popover?

Use `open:`. In v4 it also matches `:popover-open`.

```html
<div popover id="tip" class="rounded p-4 open:shadow-lg">...</div>
```

### 289: What is the `inert:` variant?

It styles elements that have the `inert` attribute, which makes them non-interactive.

```html
<form inert class="inert:opacity-50">...</form>
```

### 290: What is the `noscript:` variant?

Added in v4.1, it applies styles when JavaScript is disabled, using the `scripting: none` media query.

```html
<div class="hidden noscript:block">Please enable JavaScript.</div>
```

### 291: How do you write print styles?

Use `print:`.

```html
<nav class="print:hidden">...</nav>
<article class="print:text-black print:shadow-none">...</article>
```

### 292: How do you build a toggle switch with only Tailwind?

```html
<label class="inline-flex cursor-pointer items-center">
  <input type="checkbox" class="peer sr-only" />
  <span
    class="relative h-6 w-11 rounded-full bg-gray-300 transition peer-checked:bg-blue-600
               after:absolute after:top-0.5 after:left-0.5 after:size-5 after:rounded-full after:bg-white
               after:transition peer-checked:after:translate-x-5"
  ></span>
</label>
```

### 293: How do you build a floating label input?

```html
<div class="relative">
  <input
    id="email"
    placeholder=" "
    class="peer w-full rounded border px-3 pt-5 pb-2"
  />
  <label
    for="email"
    class="absolute top-1 left-3 text-xs text-gray-500 transition-all
           peer-placeholder-shown:top-3.5 peer-placeholder-shown:text-base
           peer-focus:top-1 peer-focus:text-xs"
  >
    Email
  </label>
</div>
```

### 294: How do you build a tooltip on hover?

```html
<div class="group relative inline-block">
  <button>Info</button>
  <span
    class="pointer-events-none absolute bottom-full left-1/2 mb-2 -translate-x-1/2 rounded bg-gray-900 px-2 py-1
               text-xs whitespace-nowrap text-white opacity-0 transition group-hover:opacity-100"
  >
    More details
  </span>
</div>
```

### 295: How do you build a skeleton loader?

```html
<div class="animate-pulse space-y-3">
  <div class="h-4 w-3/4 rounded bg-gray-200"></div>
  <div class="h-4 w-1/2 rounded bg-gray-200"></div>
  <div class="h-32 rounded bg-gray-200"></div>
</div>
```

### 296: How do you build a badge component?

```html
<span
  class="inline-flex items-center rounded-full bg-green-50 px-2 py-1 text-xs font-medium text-green-700 ring-1 ring-green-600/20 ring-inset"
>
  Active
</span>
```

### 297: How do you use Tailwind with Headless UI or Radix?

These libraries give behavior and accessibility without styles. They expose state through data attributes, which you style with `data-*` variants.

```jsx
<Menu.Item>
  <a className="block px-4 py-2 data-focus:bg-blue-100">Settings</a>
</Menu.Item>

<Accordion.Trigger className="data-[state=open]:font-bold" />
```

### 298: What is shadcn/ui and how does it relate to Tailwind?

shadcn/ui is a collection of React components that you copy into your project instead of installing as a dependency. They are built with Tailwind classes and Radix primitives, use CSS variables for colors, and the `cn` helper. Its current setup uses Tailwind v4 with `@theme inline` to map its variables to utilities.

### 299: What does the Tailwind output CSS look like for a simple utility?

For `p-4` and `hover:bg-blue-500`, the output is roughly:

```css
@layer utilities {
  .p-4 {
    padding: calc(var(--spacing) * 4);
  }
  .hover\:bg-blue-500 {
    &:hover {
      @media (hover: hover) {
        background-color: var(--color-blue-500);
      }
    }
  }
}
```

After processing with Lightning CSS, the nesting is flattened for browsers.

### 300: What are the cascade layers Tailwind v4 uses?

`theme`, `base`, `components` and `utilities`, in that order. Rules in later layers win over earlier ones regardless of specificity. So a utility will always override a component class, even if the component selector is more specific.

```css
@layer theme, base, components, utilities;
```

## Advanced Questions (301-450)

### 301: What is the Oxide engine?

Oxide is the name for the rewritten engine in v4. Performance-critical parts like scanning files for class candidates are written in Rust, while the rest is TypeScript. CSS parsing, nesting, prefixing and minification are handled by Lightning CSS. According to the Tailwind team, full builds became about 3.5 to 5 times faster than v3, and incremental builds that don't add new classes finish in microseconds.

### 302: How does Tailwind's class detection actually work?

It does not parse your code as JavaScript or HTML. It reads files as plain text and splits them into tokens that could be class names, using rules that understand common quote, bracket and template syntax. Then it checks each token against known utilities and variants. Any token that matches produces CSS, anything else is ignored. This is why `bg-${color}-500` doesn't work but `isError ? "bg-red-500" : "bg-green-500"` does.

### 303: Why can Tailwind generate a class from a comment or a random string?

Because scanning is text-based, any string that matches a valid utility is generated, even in comments or in unrelated code. This is usually harmless (a few extra bytes), but it can surprise you, for example if a word like `container` or `hidden` appears in a data file. Use `@source not` to exclude folders with large data or generated files.

### 304: How does automatic source detection decide which files to scan?

v4 starts from the current working directory (or the base path you set with `source()`), walks the file tree, and:

- skips files and folders listed in `.gitignore`,
- skips `node_modules`,
- skips binary files (images, videos, archives),
- skips CSS files and lock files.

In a monorepo, if your CSS lives in one package, you may need `@source` to include sibling packages, or set `source("../..")` to move the base path up.

### 305: What happens internally when you write `@import "tailwindcss"`?

The package's `index.css` contains roughly:

```css
@layer theme, base, components, utilities;

@import "./theme.css" layer(theme);
@import "./preflight.css" layer(base);
@import "./utilities.css" layer(utilities);
```

`theme.css` holds the default `@theme` values, `preflight.css` is the reset, and `utilities.css` contains the `@tailwind utilities` marker where generated classes are inserted.

### 306: How do you use Tailwind without Preflight?

Import the parts manually and leave out Preflight.

```css
@layer theme, base, components, utilities;

@import "tailwindcss/theme.css" layer(theme);
@import "tailwindcss/utilities.css" layer(utilities);
```

This is useful when adding Tailwind to an existing site whose base styles you don't want to reset.

### 307: Why can unlayered CSS override Tailwind utilities in v4?

In the CSS cascade, any styles that are not inside a `@layer` beat all layered styles of the same origin, no matter the specificity. Tailwind v4 puts utilities in `@layer utilities`. So if a third-party stylesheet or your own CSS has `.button { padding: 0 }` outside any layer, it will override `p-4`. Fixes:

- Put your custom CSS in `@layer base` or `@layer components`.
- Import third-party CSS into a layer: `@import "library.css" layer(components);`.
- Use the important modifier for specific cases.

### 308: How does Tailwind v4 use `@property`?

Many utilities are built from internal CSS variables like `--tw-shadow`, `--tw-ring-color` or `--tw-translate-x`. v4 registers these with `@property` and gives them types and initial values.

```css
@property --tw-translate-x {
  syntax: "*";
  inherits: false;
  initial-value: 0;
}
```

This means the variables don't inherit into children (so a parent's `translate-x-4` doesn't leak), and typed values like colors and lengths can be animated, which allows transitions on gradients.

### 309: Why might some utilities break inside Shadow DOM?

`@property` rules only work when they are registered at the document level. If Tailwind's CSS is loaded only inside a shadow root, the `@property` declarations are ignored and some utilities that depend on those internal variables having an initial value (shadows, rings, transforms, gradients) can render incorrectly. A common fix is to also load the `@property` rules (or the whole Tailwind CSS) in the main document, or to set the fallback values on `:host`.

### 310: How are opacity modifiers implemented in v4?

They use `color-mix()`.

```css
.bg-blue-500\/50 {
  background-color: color-mix(in oklab, var(--color-blue-500) 50%, transparent);
}
```

This works with any color, including CSS variables and `currentColor`, which v3 couldn't do because it had to split colors into RGB channels. Since v4.1 Tailwind also outputs fallbacks so these colors still show in some older browsers.

### 311: How are utilities sorted in the generated CSS?

Tailwind sorts utilities so that predictable overrides work:

1. Utilities without variants come before utilities with variants.
2. Variants are ordered in a fixed order (for example, responsive variants are sorted by breakpoint size).
3. Among utilities, ones that set more CSS properties come before ones that set fewer.

So `p-4` (one shorthand) comes before `px-2` (more specific), and `px-2` wins. Custom `@utility` definitions are sorted with the same rules.

### 312: How do you write a functional utility with `--value()`?

Use a `*` in the name and `--value()` in the body.

```css
@theme {
  --tab-size-github: 8;
}

@utility tab-* {
  tab-size: --value(--tab-size-*, integer, [integer]);
}
```

- `--tab-size-*` matches theme keys: `tab-github`.
- `integer` matches bare values: `tab-4`.
- `[integer]` matches arbitrary values: `tab-[12]`.

Tailwind tries them in order and uses the first one that matches.

### 313: What types can be used inside `--value()`?

Bare value types include `number`, `integer`, `ratio` and `percentage`. Arbitrary value types include `[length]`, `[color]`, `[angle]`, `[url]`, `[integer]`, `[percentage]`, `[*]` (any) and others. You can also match literal keywords:

```css
@utility tab-* {
  tab-size: --value("inherit", "initial", "unset");
}
```

### 314: How do you handle negative values and fractions in custom utilities?

Define a separate utility that starts with `-` for negative values, and use `ratio` for fractions.

```css
@utility inset-gap-* {
  inset: calc(var(--spacing) * --value(integer));
}
@utility -inset-gap-* {
  inset: calc(var(--spacing) * --value(integer) * -1);
}

@utility aspect-* {
  aspect-ratio: --value(--aspect-ratio-*, ratio, [ratio]);
}
```

### 315: How do you support modifiers in a custom utility?

Use `--modifier()`. Modifiers are the part after the slash.

```css
@utility text-* {
  font-size: --value(--text-*, [length]);
  line-height: --modifier(--leading-*, [length], [*]);
}
```

```html
<p class="text-lg/loose">...</p>
```

If a declaration uses `--modifier()` and no modifier is given, that declaration is dropped.

### 316: What is `--default()` in v4.3?

It gives a functional utility a value when it is used without a suffix, so one definition handles both forms.

```css
@utility tab-* {
  tab-size: --value(integer, --default(4));
}
```

```html
<pre class="tab">...</pre>
<!-- tab-size: 4 -->
<pre class="tab-2">...</pre>
<!-- tab-size: 2 -->
```

Before v4.3 you needed a separate `@utility tab { ... }` for the bare class.

### 317: How do you write a custom variant that needs a media query and a selector?

Use the block form with `@slot`.

```css
@custom-variant hocus {
  &:hover,
  &:focus {
    @slot;
  }
}

@custom-variant desktop-hover {
  @media (min-width: 64rem) {
    @media (hover: hover) {
      &:hover {
        @slot;
      }
    }
  }
}
```

`@slot` is where the utility's declarations are placed.

### 318: Why do custom variants often use `:where()`?

`:where()` has zero specificity. Using `&:where(.dark, .dark *)` means the variant doesn't add specificity to the utility, so `dark:bg-black` has the same specificity as `bg-white`. Then ordering in the stylesheet (variants come later) decides the winner, which is what Tailwind relies on. Without `:where()`, variant classes could get higher specificity and become hard to override.

### 319: How do you create multiple themes (not just light/dark) with Tailwind v4?

Define semantic CSS variables per theme and map them to utilities with `@theme inline`.

```css
@import "tailwindcss";

:root {
  --bg: oklch(1 0 0);
  --fg: oklch(0.2 0 0);
  --accent: oklch(0.6 0.2 250);
}
[data-theme="dark"] {
  --bg: oklch(0.15 0 0);
  --fg: oklch(0.95 0 0);
}
[data-theme="forest"] {
  --bg: oklch(0.25 0.05 150);
  --accent: oklch(0.7 0.18 140);
}

@theme inline {
  --color-bg: var(--bg);
  --color-fg: var(--fg);
  --color-accent: var(--accent);
}
```

```html
<body class="bg-bg text-fg">
  <button class="bg-accent">...</button>
</body>
```

Switching themes only changes the `data-theme` attribute. No `dark:` classes are needed.

### 320: Why use `@theme inline` and not plain `@theme` for semantic tokens?

With plain `@theme`, `--color-bg: var(--bg)` is output as a variable on `:root`, and `bg-bg` becomes `background-color: var(--color-bg)`. Since `--color-bg` is resolved on `:root`, it uses the root value of `--bg`, so a nested `[data-theme="dark"]` section wouldn't change it. With `@theme inline`, the utility outputs `background-color: var(--bg)`, which resolves on the element itself, so nested theme scopes work.

### 321: How would you design a token system with primitive and semantic layers?

- Primitive tokens: raw values like `--color-blue-600`, `--radius-md`. These come from the default theme or `@theme`.
- Semantic tokens: meaning-based names like `--color-primary`, `--color-surface`, `--color-danger`, mapped to primitives.
- Component tokens (optional): `--button-radius`, `--card-padding`.

```css
@theme {
  --color-*: initial;
  --color-blue-600: oklch(0.546 0.245 262.881);
  --color-red-600: oklch(0.577 0.245 27.325);
  --color-white: #fff;
}

@theme inline {
  --color-primary: var(--color-blue-600);
  --color-danger: var(--color-red-600);
  --color-surface: var(--color-white);
}
```

Components only use semantic classes (`bg-primary`), so a rebrand changes one place.

### 322: How do you share a Tailwind theme across multiple apps in a monorepo?

Create a package that exports a CSS file with your `@theme`, custom utilities and variants.

```css
/* packages/design-tokens/theme.css */
@theme {
  --color-brand: oklch(0.6 0.2 250);
  --font-sans: "Inter", sans-serif;
}
@utility focus-ring {
  @apply outline-2 outline-offset-2 outline-brand;
}
```

```css
/* apps/web/src/app.css */
@import "tailwindcss";
@import "@acme/design-tokens/theme.css";
@source "../../../packages/ui/src";
```

Each app imports it after Tailwind and adds `@source` for shared component packages.

### 323: How should a component library that uses Tailwind be published?

Common approaches:

1. Ship source files (or built JS that still contains the class strings) and ask users to add `@source "../node_modules/your-lib"` so their Tailwind build generates the classes. This avoids duplicate CSS and lets users theme it.
2. Ship a prebuilt CSS file. Simpler for users but can cause duplicated utilities and conflicts with their own Tailwind version. Using a prefix helps.
3. Ship a CSS file with `@theme` and `@source` lines that users import, so setup is one import line.

Don't minify or mangle class names in the JS bundle, or the consumer's scanner won't find them.

### 324: How can a library include its own `@source` so users don't have to?

`@source` paths are resolved relative to the file they are in. So a library can ship a CSS file like:

```css
/* node_modules/@acme/ui/styles.css */
@source "./dist";
@theme {
  --color-acme: oklch(0.6 0.2 30);
}
```

The user only writes:

```css
@import "tailwindcss";
@import "@acme/ui/styles.css";
```

### 325: How does `tailwind-merge` know which classes conflict, and what goes wrong with custom tokens?

It has a built-in map of Tailwind class groups (padding, background color, font size, etc.). If you add custom theme values, it might not know them. For example, a custom `text-tiny` font size might be seen as a text color, so `text-tiny text-red-500` would remove one of them. Fix it with `extendTailwindMerge`.

```ts
import { extendTailwindMerge } from "tailwind-merge";

export const twMerge = extendTailwindMerge({
  extend: {
    theme: { text: ["tiny"] },
  },
});
```

Use a `tailwind-merge` major version that matches your Tailwind major version (v3 of tailwind-merge for Tailwind v4).

### 326: What is the cost of using `tailwind-merge` everywhere?

It runs at runtime, parses class strings and keeps a cache. For most apps the cost is small, but in large lists or hot render paths it adds up. Use it only where overrides are expected (components that accept `className`), not on every element. Libraries like `tailwind-variants` or careful API design (using variant props instead of free overrides) reduce the need for it.

### 327: How do you write a Tailwind plugin in JavaScript for v4?

The v3 plugin API still works in v4 through `@plugin`.

```js
// plugins/text-stroke.js
import plugin from "tailwindcss/plugin";

export default plugin(function ({ matchUtilities, addVariant, theme }) {
  matchUtilities(
    {
      "text-stroke": (value) => ({ "-webkit-text-stroke-width": value }),
    },
    { values: { 1: "1px", 2: "2px", 4: "4px" } },
  );

  addVariant("optional", "&:optional");
});
```

```css
@plugin "./plugins/text-stroke.js";
```

For most new code, `@utility` and `@custom-variant` in CSS are simpler.

### 328: How do you pass options to a plugin from CSS?

Use a block after `@plugin`.

```css
@plugin "@tailwindcss/typography" {
  classname: wysiwyg;
}

@plugin "@tailwindcss/forms" {
  strategy: "class";
}
```

The plugin must be created with `plugin.withOptions()` to accept options.

### 329: What parts of the v3 JavaScript config are not supported in v4?

When loading a JS config with `@config`:

- `corePlugins` is not supported (you can't disable individual core utilities).
- `safelist` is not supported (use `@source inline()`).
- `separator` is not supported.
- `resolveConfig()` was removed; read CSS variables instead.
- `content` still works but auto detection is the default.

### 330: How do you read theme values in JavaScript in v4?

v4 doesn't have `resolveConfig`. Read CSS variables from the DOM.

```js
const styles = getComputedStyle(document.documentElement);
const blue = styles.getPropertyValue("--color-blue-500");
```

Make sure the variable is emitted (it must be used somewhere or defined with `@theme static`). For libraries like charting tools that need values at build time, you can also keep a small TS file of tokens and generate the `@theme` from it.

### 331: How do you pass theme colors to a canvas or chart library?

Since charts often need actual values, read the computed CSS variable and convert it if needed. OKLCH strings work in canvas in modern browsers. For example:

```js
const ctx = canvas.getContext("2d");
ctx.fillStyle = getComputedStyle(document.documentElement)
  .getPropertyValue("--color-sky-500")
  .trim();
```

When the theme changes (dark mode), re-read the variables and redraw.

### 332: How do you avoid FOUC (flash of unstyled content) with Tailwind in SSR apps?

- Load the Tailwind CSS as a normal `<link>` in the `<head>` (frameworks like Next.js, Remix, Nuxt and Angular do this).
- Don't use the CDN browser build in production because it styles the page after it loads.
- For dark mode, set the theme class on the server (from a cookie) or with a blocking inline script.
- For critical CSS, frameworks can inline the CSS, and since Tailwind output is small, inlining the whole file is often fine.

### 333: How do you debug why a Tailwind class isn't working?

1. Check the generated CSS in DevTools: is the class there at all?
2. If missing: the class might be built dynamically, the file isn't scanned (check `@source`, `.gitignore`), or the class name is wrong.
3. If present but not applied: check for overrides from unlayered CSS, a higher specificity rule, a conflicting utility, or an `!important` elsewhere.
4. Check variant conditions (hover only on hover devices, breakpoint size, dark mode strategy).
5. Use the IntelliSense hover preview to confirm what CSS the class produces.

### 334: Why is a class generated in development but missing in production?

Common reasons:

- Production build scans a different folder (CI checkout without some files, or the base path differs).
- The file is in `.gitignore` (for example generated code) and therefore skipped.
- Class names are built with string concatenation and only worked locally because the class was used elsewhere while you were developing.
- A different CSS entry file is used in production.

Fix by adding explicit `@source` paths and using complete class names.

### 335: How do you handle class names that come from a database (for example user-chosen colors)?

Don't store class names if you can avoid it. Store values and use CSS variables:

```jsx
<div
  style={{ "--user-color": user.color }}
  className="bg-(--user-color) text-white"
/>
```

If you must store class names, limit them to a known set and safelist them with `@source inline()` so they're always generated.

### 336: What are the performance considerations of very long class lists?

The CSS size stays small because each utility is generated once. The cost is mostly in HTML size, which compresses very well with gzip/brotli because the same class names repeat. In practice, Tailwind sites usually ship less total CSS than hand-written CSS. If HTML size matters (like huge server-rendered lists), extracting a component class with `@utility` or using components to keep markup consistent helps compression.

### 337: How does Tailwind v4 handle vendor prefixes and browser targets?

It runs the output through Lightning CSS, which adds prefixes (like `-webkit-backdrop-filter`) and lowers modern syntax (nesting, some color functions, media query ranges) for the browsers Tailwind supports. You don't configure browserslist for it; the target is fixed to the browsers v4 supports.

### 338: What is the difference between `@tailwindcss/vite` and `@tailwindcss/postcss`?

The Vite plugin hooks directly into Vite's module graph. It knows which files changed and can update CSS faster, with less work than PostCSS. The PostCSS plugin works with any PostCSS-based tool (Next.js, Angular, older webpack setups) but has to rely on file system checks. If your framework uses Vite, the Vite plugin is the recommended choice. Since v4.2 there is also `@tailwindcss/webpack` for webpack projects.

### 339: How do you set up Tailwind with webpack in v4.2+?

```bash
npm install tailwindcss @tailwindcss/webpack
```

```js
// webpack.config.js
const TailwindCSS = require("@tailwindcss/webpack");

module.exports = {
  plugins: [new TailwindCSS()],
  module: {
    rules: [{ test: /\.css$/, use: ["style-loader", "css-loader"] }],
  },
};
```

Check the official docs for the exact options, since the plugin is new.

### 340: Can you use Tailwind's compiler from Node.js directly?

Yes, but it is a low-level option. The `tailwindcss` package exposes a `compile` function, `@tailwindcss/node` adds Node helpers like file loading, and `@tailwindcss/oxide` contains the Rust scanner that finds class candidates. The CLI and the Vite, PostCSS and webpack plugins are all built on top of these pieces. These internal APIs are less stable and less documented than the CLI and bundler plugins, so most projects never need them. Use them only for custom tooling, like a build step in a non-standard bundler.

### 341: What is the trade-off between `@apply` and components in terms of output?

`@apply` copies declarations into your class, so if ten custom classes all `@apply` the same utilities, the CSS repeats those declarations ten times. Components keep using shared utility classes, so the CSS doesn't grow when you add more components. `@apply` also creates a second place to look when debugging styles.

### 342: When is `@apply` the right choice?

- Styling HTML you don't control (CMS output, Markdown, third-party widgets).
- Small global base styles like `body` or `a`.
- Defining a `@utility` that bundles a few utilities, like `focus-ring`.
- Styling inside Shadow DOM or other places where you can't add classes.

For your own components, keeping classes in the template is usually better.

### 343: How do you handle specificity conflicts with a legacy CSS codebase?

Options, from least to most invasive:

1. Put the legacy CSS into a layer below utilities: `@import "legacy.css" layer(base);` so utilities win.
2. Use the important modifier on specific utilities: `mt-4!`.
3. Enable `important` globally: `@import "tailwindcss" important;`.
4. Use `prefix()` so Tailwind class names don't clash with legacy names.

Layering is usually best since it doesn't touch specificity.

### 344: How do you migrate a large v3 codebase to v4 safely?

1. Check browser support requirements first (v4 needs Safari 16.4+, Chrome 111+, Firefox 128+).
2. Create a branch and run `npx @tailwindcss/upgrade`.
3. Review the diff: renamed classes, config moved to `@theme`, `@layer utilities` converted to `@utility`.
4. Check visual changes caused by defaults: border color, ring width, placeholder color, button cursor, `space-*` selector, `hover` on touch.
5. Fix dynamic class names and safelists (`@source inline()`).
6. Replace `theme()` calls with CSS variables; update `@apply` in Vue/Svelte/CSS modules with `@reference`.
7. Update `tailwind-merge` and Prettier plugin.
8. Run visual regression tests (Playwright screenshots, Chromatic) before merging.

### 345: What visual regressions are most common after a v3 to v4 upgrade?

- Borders turning dark because of `currentColor` default.
- Thinner focus rings (`ring` is 1px).
- Different shadow and rounded sizes if renames were missed.
- Placeholder color changes.
- Spacing changes from the `space-y-*` selector change.
- Hover styles not showing on touch devices.
- Buttons losing the pointer cursor.
- Gradient differences because v4 interpolates in oklab by default.
- Custom `@layer utilities` classes not working with variants.

### 346: How does the `hidden` attribute interact with Tailwind display utilities?

Preflight sets `[hidden]:where(:not([hidden="until-found"])) { display: none !important; }`. Since v4 makes this `!important`, adding `hidden` attribute hides the element even if it has `flex` or `block` classes. In v3 a `flex` class could override the attribute. This is a subtle behavior change to remember when toggling visibility with the attribute.

### 347: How do you make a utility that responds to a CSS variable set by a parent?

Set the variable with an arbitrary property and read it with the shorthand.

```html
<div class="[--gutter:--spacing(4)] md:[--gutter:--spacing(8)]">
  <div class="px-(--gutter)">...</div>
  <div class="-mx-(--gutter)">...</div>
</div>
```

Changing the variable at different breakpoints updates every child that uses it.

### 348: What is `@source inline()` brace expansion syntax?

It works like shell brace expansion:

- `{a,b}` expands to each option.
- `{100..900..100}` expands to a range with a step.
- An empty option (`{hover:,}`) means "with or without".

```css
@source inline("{sm:,md:,lg:,}grid-cols-{1..6}");
```

This generates `grid-cols-1` to `grid-cols-6` with and without the three breakpoints. You can also use `@source not inline(...)` to stop specific classes from being generated even if they appear in your files.

### 349: How do you stop a specific class from being generated?

```css
@source not inline("container");
```

This is useful when a word like `container` appears in content files and you don't want the utility at all.

### 350: How would you build a design system button with variants, sizes and states?

```tsx
import { cva, type VariantProps } from "class-variance-authority";
import { cn } from "@/lib/cn";

const buttonVariants = cva(
  "inline-flex items-center justify-center gap-2 rounded-md font-medium transition-colors " +
    "focus-visible:outline-2 focus-visible:outline-offset-2 disabled:pointer-events-none disabled:opacity-50",
  {
    variants: {
      variant: {
        primary:
          "bg-primary text-white hover:bg-primary/90 focus-visible:outline-primary",
        outline: "border border-gray-300 bg-transparent hover:bg-gray-50",
        ghost: "hover:bg-gray-100",
        danger: "bg-red-600 text-white hover:bg-red-700",
      },
      size: {
        sm: "h-8 px-3 text-sm",
        md: "h-10 px-4",
        lg: "h-12 px-6 text-lg",
        icon: "size-10",
      },
    },
    defaultVariants: { variant: "primary", size: "md" },
  },
);

type Props = React.ButtonHTMLAttributes<HTMLButtonElement> &
  VariantProps<typeof buttonVariants>;

export function Button({ className, variant, size, ...props }: Props) {
  return (
    <button
      className={cn(buttonVariants({ variant, size }), className)}
      {...props}
    />
  );
}
```

### 351: How do you style a component based on its own size and its parent's state at the same time?

Combine container queries and group variants.

```html
<li class="group @container">
  <div class="flex flex-col gap-2 @md:flex-row group-hover:bg-gray-50">
    <img class="w-full @md:w-32" />
    <p class="@max-xs:hidden">Details</p>
  </div>
</li>
```

### 352: What is the difference between `group-*` and `in-*` in terms of generated CSS?

`group-hover:underline` produces a selector like `&:is(:where(.group):hover *)`, so it only matches when an ancestor with the `group` class is hovered. `in-hover:underline` produces something like `:where(*:hover) &`, which matches when any ancestor is hovered. `in-*` is shorter to write, but it can match more than you expect. For example, `<body>` counts as hovered whenever the mouse is anywhere on the page, so `in-hover:` on a deeply nested element would almost always be active.

### 353: How do you animate an element when it enters and leaves without JavaScript libraries?

Use `starting:` for the entry state and `transition-discrete` so `display` can transition.

```html
<div
  popover
  id="toast"
  class="opacity-100 translate-y-0 transition-all transition-discrete duration-300
         starting:open:opacity-0 starting:open:translate-y-2
         not-open:opacity-0 not-open:translate-y-2"
>
  Saved
</div>
```

Entry uses `@starting-style`, and exit uses the closed state with `allow-discrete` so the element stays visible until the transition ends.

### 354: How do you build view transitions with Tailwind?

Tailwind doesn't have dedicated view transition utilities, but you can use arbitrary properties and custom CSS.

```html
<img class="[view-transition-name:hero-image]" src="..." />
```

```css
::view-transition-old(hero-image),
::view-transition-new(hero-image) {
  animation-duration: 300ms;
}
```

Then call `document.startViewTransition()` (or use your framework's support).

### 355: How do you register a custom property for animation with Tailwind?

Write `@property` in your CSS and use it in utilities or keyframes.

```css
@property --angle {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

@theme {
  --animate-rotate-border: rotate-border 3s linear infinite;
  @keyframes rotate-border {
    to {
      --angle: 360deg;
    }
  }
}
```

```html
<div
  class="animate-rotate-border bg-[conic-gradient(from_var(--angle),var(--color-sky-500),var(--color-pink-500),var(--color-sky-500))] p-px"
>
  ...
</div>
```

Without `@property`, the browser can't interpolate the variable and the animation would jump.

### 356: How does Tailwind v4 handle CSS `@import` of other files?

v4 includes import handling (like `postcss-import`), so you can split your CSS into files:

```css
@import "tailwindcss";
@import "./theme.css";
@import "./components/buttons.css";
```

Files are inlined at build time. Imports must come before other rules (except `@charset` and `@layer` statements).

### 357: How do you put an imported third-party stylesheet into a layer?

```css
@import "tailwindcss";
@import "some-datepicker/dist/styles.css" layer(components);
```

Now the library styles sit below utilities, so you can override them with Tailwind classes without `!important`.

### 358: How do you scope Tailwind to part of a page (e.g. a widget embedded in another site)?

Options:

- Use `prefix(tw)` so class names don't clash.
- Skip Preflight and add a scoped reset under your widget root.
- Load it inside Shadow DOM, keeping in mind the `@property` limitation.
- Use `important` with a selector strategy through arbitrary variants, or render inside an iframe for complete isolation.

### 359: How do you test Tailwind-based components?

- Unit tests should test behavior, not class names. Asserting on class strings makes tests brittle.
- For style checks, use visual regression tests (Playwright `toHaveScreenshot`, Storybook with Chromatic).
- jsdom doesn't compute layout, so checks like "is this visible at md" need a real browser (Playwright, Cypress, Vitest browser mode).
- Test that variant props produce the expected classes only for important cases (for example, a `cva` config).

### 360: How do you use Tailwind in Storybook?

Import your main CSS in `.storybook/preview.ts`:

```ts
import "../src/app.css";
```

If Storybook uses Vite, add the `@tailwindcss/vite` plugin in its Vite config (or it picks up your project's Vite config). Make sure stories are within scanned paths, or add an `@source` for them.

### 361: What are common accessibility mistakes in Tailwind projects?

- Removing focus styles with `outline-none` and not replacing them.
- Using `hover:` only and not `focus-visible:` for interactive states.
- Low contrast from light gray text like `text-gray-400` on white.
- Hiding labels without `sr-only`.
- Using `div` with click handlers instead of `button`.
- Ignoring `motion-reduce:` for animations.

Tailwind makes it easy to add the right styles, but it doesn't add them for you.

### 362: How do you build a consistent focus style across a project?

Create a utility and use it everywhere.

```css
@utility focus-ring {
  &:focus-visible {
    outline: 2px solid var(--color-primary);
    outline-offset: 2px;
  }
}
```

```html
<button class="focus-ring">...</button> <a class="focus-ring">...</a>
```

### 363: How do you support Windows high contrast mode properly?

- Use `outline-hidden` instead of `outline-none` when hiding outlines, so they still appear in forced colors mode.
- Use `forced-colors:` variants to adjust things like custom checkboxes.
- Avoid relying only on background color to show state; also use borders or icons.
- `forced-color-adjust-none` stops the browser from changing colors on specific elements (for example, color swatches).

```html
<div class="bg-red-500 forced-color-adjust-none">Color swatch</div>
```

### 364: How do you style based on user preferences like reduced data or contrast?

Built-in variants: `motion-reduce:`, `motion-safe:`, `contrast-more:`, `contrast-less:`, `forced-colors:`, `inverted-colors:`. For others, create custom variants:

```css
@custom-variant reduced-data (@media (prefers-reduced-data: reduce));
```

### 365: How do you use container queries with `has-*` to build adaptive forms?

```html
<form class="@container">
  <div
    class="grid gap-4 @lg:grid-cols-2 has-[input:invalid]:ring-1 has-[input:invalid]:ring-red-500"
  >
    <input required class="border p-2" />
    <input class="border p-2" />
  </div>
</form>
```

The grid switches to two columns when the form is wide enough, and the group shows a red ring if any input inside is invalid.

### 366: How do you implement RTL support in a Tailwind app?

1. Set `dir="rtl"` on `<html>` for RTL languages.
2. Use logical utilities: `ms-*`, `me-*`, `ps-*`, `pe-*`, `inset-s-*`, `text-start`, `rounded-s-*`, `border-s`.
3. Use `rtl:` and `ltr:` only for things logical properties can't handle, like flipping an arrow icon: `rtl:rotate-180`.
4. Test both directions in visual tests.

### 367: How do you make spacing fluid (scales with viewport) in Tailwind?

Use `clamp()` in arbitrary values or theme variables.

```css
@theme {
  --text-fluid-xl: clamp(1.5rem, 1rem + 2vw, 3rem);
  --spacing-section: clamp(3rem, 2rem + 5vw, 8rem);
}
```

```html
<h1 class="text-fluid-xl">...</h1>
<section class="py-(--spacing-section)">...</section>
```

### 368: How do you add named spacing values in v4?

Add `--spacing-*` variables. They work with all spacing utilities.

```css
@theme {
  --spacing-header: 4rem;
}
```

```html
<main class="pt-header">...</main>
<div class="h-header">...</div>
```

### 369: How does v4 handle fractions and arbitrary numbers for width?

`w-1/2` produces `calc(1/2 * 100%)`. Any fraction works (`w-7/11`). Whole numbers use the spacing scale (`w-17` = `calc(var(--spacing) * 17)`). Decimals in steps of 0.25 also work, like `w-4.5`. Named values like `w-md` come from `--container-*`.

### 370: How do you make a utility that accepts both theme values and any CSS variable?

```css
@theme {
  --gutter-sm: 1rem;
  --gutter-lg: 2rem;
}

@utility gutter-* {
  padding-inline: --value(--gutter-*, [length], [*]);
}
```

```html
<div class="gutter-sm">...</div>
<div class="gutter-[3rem]">...</div>
<div class="gutter-(--custom)">...</div>
```

The `(--custom)` shorthand is handled as an arbitrary value, so `[*]` or `[length]` matches it.

### 371: What are the downsides of Tailwind and how do you address them in interviews?

- Long class lists: addressed by components, Prettier sorting and IntelliSense.
- Learning curve for class names: they map closely to CSS, so CSS knowledge transfers.
- Mixing content and style in markup: components keep it local, which is easier to change than distant stylesheets.
- Dynamic styles need care: use CSS variables or full class names.
- Vendor lock-in: the output is plain CSS and classes are standard property names, so migration is possible but not free.

### 372: How do you compare Tailwind with CSS Modules and CSS-in-JS?

- CSS Modules: scoped class names, real CSS, but you still name and maintain classes and files. Good for teams who prefer separate CSS.
- CSS-in-JS (styled-components, Emotion): dynamic styles with JS, but runtime cost and issues with React Server Components (runtime libraries).
- Tailwind: no runtime, small CSS, no naming, consistent design tokens; dynamic values need CSS variables.

Tailwind works well with server components because it is just static class names.

### 373: How does Tailwind work with React Server Components?

Perfectly, because it has no runtime. Classes are static strings in the output HTML, and the CSS is a static file. You can use Tailwind in server and client components the same way. Runtime CSS-in-JS libraries, by contrast, need client components or special setup.

### 374: How do you structure CSS files in a large Tailwind v4 project?

```
src/styles/
  app.css          # entry: imports below
  theme.css        # @theme tokens
  base.css         # @layer base rules
  utilities.css    # @utility definitions
  variants.css     # @custom-variant definitions
  vendor.css       # third-party CSS imported into a layer
```

```css
/* app.css */
@import "tailwindcss";
@import "./theme.css";
@import "./variants.css";
@import "./utilities.css";
@import "./base.css";
@import "./vendor.css" layer(components);
```

Keep one entry file so there's one Tailwind build and one source of truth.

### 375: Can you have multiple Tailwind entry CSS files in one project?

Yes. For example, one for the public site and one for the admin panel, each with its own theme and `@source` paths.

```css
/* admin.css */
@import "tailwindcss" source(none);
@source "../admin";
@theme {
  --color-primary: oklch(0.5 0.15 150);
}
```

Each entry is compiled separately. Avoid loading two Tailwind builds on the same page, since both include Preflight and duplicate utilities, and their order can cause conflicts.

### 376: How does `!important` interact with cascade layers?

With `!important`, the layer order is reversed: an important declaration in an earlier layer beats an important declaration in a later layer, and important declarations in layers beat unlayered important ones. So `p-4!` in `@layer utilities` can lose to an `!important` rule in `@layer base`. In practice, avoid `!important` in base and component layers so that the utility important modifier stays a reliable escape hatch.

### 377: How can you change the order of Tailwind's layers or add your own?

Declare the order before the import.

```css
@layer theme, base, vendor, components, utilities;
@import "tailwindcss";
@import "some-lib.css" layer(vendor);
```

The first `@layer` statement fixes the order, so `vendor` sits between base and components, and utilities still win.

### 378: How do the internal `--tw-*` variables let utilities compose?

Some utilities set only part of a property. For example, `shadow-md`, `ring-2` and `inset-shadow-sm` each set their own variable (`--tw-shadow`, `--tw-ring-shadow`, `--tw-inset-shadow`), and every one of them writes the full `box-shadow` that combines all of them:

```css
box-shadow:
  var(--tw-inset-shadow), var(--tw-inset-ring-shadow),
  var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow);
```

That's why you can use a shadow and a ring on the same element. The same pattern is used for transforms, filters, gradients and font variant numeric utilities.

### 379: What happens when you mix Tailwind filter utilities with your own `filter` rule?

Tailwind filters compose through variables (`--tw-blur`, `--tw-brightness`, ...). `blur-sm hover:brightness-110` gives `filter: var(--tw-blur) var(--tw-brightness) ...`. The issue appears when you mix Tailwind filters with your own `filter: ...` rule on the same element: your rule replaces the whole property and the Tailwind variables are ignored. Use arbitrary values (`filter-[...]`) or Tailwind utilities consistently, not both.

### 380: How would you stop developers from using arbitrary colors and enforce the design system?

- Reset the default palette (`--color-*: initial`) and define only approved tokens, so `bg-red-500` simply doesn't exist.
- Use a linter (for example an ESLint plugin for Tailwind) with rules that flag arbitrary values like `bg-[#123456]` and unknown classes.
- Review with the Prettier plugin so class lists are consistent and easy to scan.
- Provide components (`<Button>`, `<Card>`) so most UI doesn't need raw color classes.

### 381: How do you keep design tokens in sync between Figma and Tailwind?

Export tokens from Figma (for example with Tokens Studio or Figma variables export) to JSON, then generate a CSS file with an `@theme` block using a script or a tool like Style Dictionary.

```js
// build-tokens.js
import tokens from "./tokens.json" with { type: "json" };
const lines = Object.entries(tokens.color).map(
  ([name, value]) => `  --color-${name}: ${value};`,
);
fs.writeFileSync("src/styles/theme.css", `@theme {\n${lines.join("\n")}\n}\n`);
```

Run it in CI so the theme always matches the design source.

### 382: How do you handle a hydration mismatch caused by theme classes?

If the server renders `class="light"` and the client script immediately changes it to `dark`, React (or another framework) may warn about a mismatch on `<html>`. Options:

- Put `suppressHydrationWarning` on `<html>` (Next.js common pattern, used by `next-themes`).
- Read the theme from a cookie on the server so both match.
- Don't render theme-dependent markup on the server; use `dark:` classes so CSS handles it instead of JS conditions.

### 383: Why should you prefer `dark:` classes over JavaScript conditionals for theming?

`dark:` is pure CSS, so it applies immediately and the same HTML works for both themes. JS conditionals like `theme === "dark" ? "bg-black" : "bg-white"` need the theme known at render time, which causes flashes or hydration issues and re-renders when the theme changes. With semantic tokens and CSS variables you often don't even need `dark:` on each element.

### 384: How do you scope a theme to only part of the page?

With semantic CSS variables, set different values on a container.

```html
<body class="bg-bg text-fg">
  <section data-theme="dark" class="bg-bg text-fg">
    Dark section on a light page
  </section>
</body>
```

This works because the variables are mapped with `@theme inline` and resolved on each element. If you use the `dark:` variant with `&:where(.dark, .dark *)`, then adding `class="dark"` to a section also turns on `dark:` styles inside it.

### 385: Why might `dark:` styles not apply inside a section with class `dark` when using the default dark mode?

The default `dark` variant uses `@media (prefers-color-scheme: dark)`. It ignores classes. You need to override the variant with `@custom-variant dark (&:where(.dark, .dark *));` for class-based scoping.

### 386: How do you combine system preference and a manual override in pure CSS?

```css
@custom-variant dark {
  &:where([data-theme="dark"], [data-theme="dark"] *) {
    @slot;
  }
  @media (prefers-color-scheme: dark) {
    &:where(:not([data-theme="light"], [data-theme="light"] *)) {
      @slot;
    }
  }
}
```

Dark styles apply if the user picked dark, or if the system is dark and the user didn't pick light. No `data-theme` means "follow system".

### 387: How do stacking contexts cause z-index bugs in Tailwind layouts?

`z-50` only competes with siblings inside the same stacking context. Utilities like `transform` (`translate-*`, `scale-*`, `rotate-*`), `opacity-*` below 100, `filter`, `backdrop-blur-*`, `isolate`, `will-change-*` and `relative z-*` all create new stacking contexts. A dropdown with `z-50` inside a card with `scale-100` may still be covered by the next card. Fixes: render overlays in a portal at the body level, or set z-index on the parent that forms the context.

### 388: How do you define a z-index scale for a project?

v4 has no `--z-index-*` theme namespace by default, but you can create a small utility or use named variables.

```css
:root {
  --z-dropdown: 1000;
  --z-sticky: 1100;
  --z-modal: 1300;
  --z-toast: 1400;
}
```

```html
<div class="z-(--z-modal)">...</div>
```

This keeps layering decisions in one place instead of spreading `z-[9999]` around.

### 389: What CSS performance issues can you create with Tailwind utilities?

- `transition-all` makes the browser check every property; prefer `transition-colors` or `transition-transform`.
- Animating `width`, `height`, `top` or `left` triggers layout; animate `translate` and `scale` instead.
- Large `backdrop-blur-*` areas are expensive to paint, especially on mobile.
- Heavy `shadow-2xl` on many list items can slow scrolling.
- `will-change-*` on many elements uses extra memory; add it only to elements that animate.

### 390: How would you add `content-visibility` and `contain` for performance?

Tailwind doesn't have utilities for all of these, so add your own.

```css
@utility content-auto {
  content-visibility: auto;
  contain-intrinsic-size: auto 500px;
}
```

```html
<section class="content-auto">Long off-screen section</section>
```

The browser skips rendering the section until it is near the viewport.

### 391: How does the `hover` media query in v4 affect devices with both touch and mouse?

`@media (hover: hover)` checks the primary input. On a touch laptop where the primary input is a mouse, hover works. On a tablet with a connected mouse, the primary pointer might still be touch, so `hover:` won't apply. If you need hover whenever any input can hover, create a variant with `any-hover`:

```css
@custom-variant hover (&:hover);
/* or */
@custom-variant any-hover {
  @media (any-hover: hover) {
    &:hover {
      @slot;
    }
  }
}
```

### 392: How do you write an arbitrary variant that uses an at-rule?

Put the at-rule in brackets, with underscores for spaces.

```html
<div class="[@media(min-resolution:2dppx)]:border-[0.5px]">...</div>
<div class="[@supports(height:100dvh)]:h-dvh">...</div>
```

### 393: How do you target a parent with a specific class using arbitrary group variants?

```html
<div class="group is-published">
  <span class="hidden group-[.is-published]:block">Published</span>
</div>

<div class="group">
  <p class="group-[:nth-of-type(3)_&]:text-red-500">...</p>
</div>
```

`&` marks where `.group` goes in the selector, and `_` stands for a space.

### 394: How do you write a variant that targets a sibling that comes after the element?

`peer` only works for previous siblings because CSS only has `~` and `+` (forward) selectors. For a later sibling, use `has-*` on the parent or `:has()` in an arbitrary variant:

```html
<div class="group">
  <label class="group-has-[input:focus]:text-blue-600">Name</label>
  <input />
</div>
```

### 395: How can you style an element when a sibling anywhere in the form is checked?

Use `has-*` on a common ancestor with `group`.

```html
<form class="group">
  <input type="checkbox" id="terms" />
  <button class="opacity-50 group-has-[#terms:checked]:opacity-100">
    Continue
  </button>
</form>
```

### 396: How does Tailwind treat utilities used with many variants, in terms of CSS size?

Each variant combination is a separate rule. `hover:bg-blue-500`, `md:bg-blue-500` and `md:hover:bg-blue-500` are three rules. If you add a lot of variants for every color in a big safelist (e.g. with brace expansion), the CSS can grow fast. Generate only combinations you actually use.

### 397: How do you prevent a utility from being affected by Preflight changes or browser defaults when building email templates?

Tailwind v4 output uses CSS variables, `@layer`, `oklch()`, `color-mix()` and nesting, which most email clients don't support. For emails, use a tool built for it (like Maizzle or React Email's Tailwind component), which converts classes to inline styles with plain values. Plain Tailwind v4 CSS is not suitable for email as-is.

### 398: How do you use Tailwind in a browser extension's content script?

Content scripts inject CSS into other websites, so:

- Use `prefix()` to avoid clashing with the site's classes.
- Skip Preflight, or render your UI in a Shadow DOM so you don't reset the host page.
- If using Shadow DOM, include `@property` rules in the main document or set fallbacks, as explained earlier.
- Use `rem` carefully because the host page may change the root font size; you can set `--spacing` and font sizes in `px` in your theme.

### 399: How do you handle a host page that sets `html { font-size: 10px; }`?

All Tailwind sizes are in `rem`, so they become smaller. Options: override theme values with `px`, or change `--spacing` to compensate.

```css
@theme {
  --spacing: 4px;
  --text-base: 16px;
  --text-base--line-height: 24px;
}
```

### 400: How do micro-frontends using Tailwind avoid conflicts?

- Each micro-frontend uses its own `prefix()`.
- Only the shell loads Preflight; others import theme and utilities only.
- Agree on a shared theme package with tokens so designs stay consistent.
- Use the same Tailwind version where possible, since different versions can produce different CSS for the same class.
- Consider Shadow DOM boundaries for strict isolation.

### 401: How do you check for unused or invalid Tailwind classes in CI?

- Use an ESLint plugin for Tailwind that supports v4 to report unknown classes, conflicting classes and non-canonical names.
- Run `prettier --check` with the Tailwind plugin to enforce class order.
- Run a production build and fail on warnings.
- Visual regression tests catch classes that exist but produce the wrong look.

### 402: What are "canonical" class names, and why do linters suggest them?

Some classes can be written in more than one way: `w-[16px]` vs `w-4`, `[color:red]` vs `text-[red]`, `!flex` vs `flex!`, `bg-gradient-to-r` vs `bg-linear-to-r`. Tools suggest the canonical (shortest standard) form for consistency and to reduce duplicate CSS. Recent versions of IntelliSense can show these suggestions.

### 403: How does Tailwind handle duplicate classes across files?

Each unique class is generated once, no matter how many files use it. The CSS output is the set of all unique candidates found. That's why CSS size grows slowly as a project grows: after a while most new pages reuse existing classes.

### 404: How do you build a data table with sticky header and first column?

```html
<div class="max-h-96 overflow-auto rounded-lg border">
  <table class="min-w-full border-separate border-spacing-0 text-sm">
    <thead>
      <tr>
        <th
          class="sticky top-0 left-0 z-20 border-b bg-gray-50 px-4 py-2 text-left"
        >
          Name
        </th>
        <th class="sticky top-0 z-10 border-b bg-gray-50 px-4 py-2 text-left">
          Email
        </th>
      </tr>
    </thead>
    <tbody class="[&_tr:hover_td]:bg-gray-50">
      <tr>
        <td class="sticky left-0 z-10 border-b bg-white px-4 py-2">Ana</td>
        <td class="border-b px-4 py-2">ana@example.com</td>
      </tr>
    </tbody>
  </table>
</div>
```

`border-separate` is used because sticky cells with `border-collapse` lose their borders when scrolling.

### 405: How do you build a masonry-like layout?

Use CSS columns.

```html
<div class="columns-1 gap-4 sm:columns-2 lg:columns-3">
  <img class="mb-4 w-full break-inside-avoid rounded-lg" src="1.jpg" />
  <img class="mb-4 w-full break-inside-avoid rounded-lg" src="2.jpg" />
</div>
```

Items flow top to bottom in each column. For left-to-right order you would need JavaScript or future CSS masonry support.

### 406: How do you build a dashboard layout with a fixed sidebar and scrollable content?

```html
<div
  class="grid h-dvh grid-cols-[16rem_1fr] grid-rows-[auto_1fr] max-lg:grid-cols-1"
>
  <header class="col-span-full border-b px-6 py-3">Top bar</header>
  <aside class="overflow-y-auto border-r max-lg:hidden">Sidebar</aside>
  <main class="min-h-0 overflow-y-auto p-6">Scrollable content</main>
</div>
```

`min-h-0` on the grid item lets it shrink so its own `overflow-y-auto` works.

### 407: How do you build a responsive image gallery with aspect ratios and lazy loading?

```html
<ul class="grid grid-cols-2 gap-2 md:grid-cols-4">
  <li class="aspect-square overflow-hidden rounded-md bg-gray-100">
    <img
      loading="lazy"
      class="size-full object-cover transition-transform hover:scale-105"
      src="..."
      alt=""
    />
  </li>
</ul>
```

The `aspect-square` wrapper reserves space so the layout doesn't shift while images load.

### 408: How do you create a component that adapts to the number of children?

Use `has-*` with `nth-*` selectors.

```html
<div
  class="grid gap-2 has-[>:nth-child(2)]:grid-cols-2 has-[>:nth-child(3)]:grid-cols-3"
>
  <img /><img /><img />
</div>
```

One child: one column. Two children: two columns. Three or more: three columns.

### 409: How do you build a "quantity query" style layout without JavaScript?

The same idea as above, using `:has()` with `:nth-last-child`.

```html
<ul class="flex gap-2 has-[>:nth-child(5)]:flex-wrap">
  ...
</ul>
```

When there are five or more items, the list wraps.

### 410: How do you create a utility that sets multiple properties from one theme key?

Use sub-properties with `--value()` and read them in the utility.

```css
@theme {
  --heading-1: 2.5rem;
  --heading-1--weight: 800;
  --heading-2: 2rem;
  --heading-2--weight: 700;
}

@utility heading-* {
  font-size: --value(--heading-*);
  font-weight: --value(--heading-* --weight);
}
```

```html
<h1 class="heading-1">...</h1>
```

### 411: How do you make a custom utility work with the opacity modifier?

Read the color with `--value()`, read the opacity with `--modifier()`, and mix them with `color-mix()`.

```css
@utility glow-* {
  --glow-color: --value(--color-*, [color]);
  --glow-opacity: calc(--modifier(integer) * 1%);
  box-shadow: 0 0 1.5rem
    color-mix(
      in oklab,
      var(--glow-color) var(--glow-opacity, 100%),
      transparent
    );
}
```

```html
<div class="glow-sky-500">Full color</div>
<div class="glow-sky-500/50">50% opacity</div>
```

When no modifier is given, the `--glow-opacity` declaration is dropped, so the `100%` fallback is used.

### 412: What happens if two `@utility` definitions have the same name?

They are merged: all declarations are combined, and later declarations for the same property win. This lets you extend built-in utilities, like adding `margin-inline: auto` to `container`. But it can also create surprising results if two shared CSS files define the same utility.

### 413: Can you override a built-in utility?

You can extend it with `@utility` using the same name, and your declarations are added. To fully replace a theme-driven utility, change its theme values instead, for example redefining `--shadow-md`. You can't remove core utilities with configuration in v4 (there's no `corePlugins`), but you can stop them from being generated with `@source not inline(...)`.

### 414: How does Tailwind resolve conflicts between a theme key and a bare value?

For utilities that accept both, theme keys win. If you define `--spacing-4: 2rem` in your theme, then `p-4` uses `2rem` instead of `calc(var(--spacing) * 4)`. This can be useful but also confusing, so avoid naming custom spacing keys with numbers that clash with the default multiplier scale.

### 415: How do you debug which `@theme` variables are actually in the output?

Open the built CSS and look at the `@layer theme` block, or inspect `:root` in DevTools. By default, only variables used by generated utilities (or by your CSS through `var()`) are output. If a variable you read from JS is missing, mark it with `@theme static` or reference it in CSS.

### 416: Why might a `var(--color-*)` used only in JavaScript be missing at runtime?

Tailwind removes unused theme variables. It knows a variable is used when a utility uses it or when it appears in CSS. If only JavaScript reads it (for example with `getPropertyValue`), Tailwind can't see that. Use `@theme static`, or `@import "tailwindcss" theme(static);` to output all theme variables.

### 417: How do you use Tailwind classes inside JavaScript strings in a non-standard file type (like `.php` templates or `.md`)?

Since scanning is text-based, Tailwind reads any text file it finds, regardless of extension (except ignored or binary ones). If the files are in an ignored folder or outside the base path, add `@source "../templates/**/*.php";`.

### 418: How do you handle class names in a backend language that builds strings (e.g. Python or Go templates)?

The same rule applies: full class names must appear somewhere in text. Avoid code like `"text-" + level + "-600"`. Use maps with full names, or safelist. Make sure the backend template folder is scanned with `@source` if it's outside the frontend project.

### 419: How do you set up Tailwind with a backend framework like Laravel or Rails?

- Laravel: uses Vite, so add `@tailwindcss/vite`. Tailwind scans Blade templates automatically, or you add `@source "../views";` if needed.
- Rails: the `tailwindcss-rails` gem wraps the standalone CLI, so you don't need Node.js. The CSS entry is `app/assets/tailwind/application.css` with `@import "tailwindcss";`.
- Django/Flask/Go: use the standalone CLI binary or `@tailwindcss/cli` and point `@source` at template folders.

### 420: What is the standalone Tailwind CLI?

It is a single executable that includes Node.js and Tailwind, so you can use Tailwind without npm. It's useful for projects without a JavaScript toolchain (Go, Python, Rails, PHP). Download the binary for your platform from the GitHub releases page and run:

```bash
./tailwindcss -i input.css -o output.css --watch
```

First-party plugins like typography and forms are bundled in it.

### 421: How does Tailwind handle `@layer base` rules that use `@apply` with variants?

You can use variants inside `@apply`.

```css
@layer base {
  a {
    @apply text-blue-600 underline-offset-2 hover:underline dark:text-blue-400;
  }
}
```

Tailwind generates the matching nested rules (`&:hover`, the dark media query) inside the `a` rule.

### 422: Why might `@apply` of a utility with a variant produce unexpected selector output?

Because variants like `group-hover` or `peer-checked` depend on other elements' classes. `@apply group-hover:underline` inside `.card-title` produces a selector like `.card-title:is(:where(.group):hover *)`, which only works if an ancestor actually has the `group` class. It's easy to forget that the relationship still has to exist in the markup.

### 423: How do you make an accessible custom select or combobox styled with Tailwind?

Don't build the behavior from scratch. Use a headless library (Headless UI, Radix, React Aria, Ark UI) that handles keyboard navigation, focus management and ARIA, and style its parts with Tailwind using its data attributes or render props.

```jsx
<Listbox.Option className="px-3 py-2 data-focus:bg-blue-100 data-selected:font-semibold">
  {option.name}
</Listbox.Option>
```

### 424: How do you build a responsive typography scale that also works in prose content?

Define the scale once in `@theme` and reuse it.

```css
@theme {
  --text-display: clamp(2.5rem, 2rem + 3vw, 4.5rem);
  --text-display--line-height: 1.05;
}

@layer base {
  .prose h1 {
    font-size: var(--text-display);
    line-height: var(--text-display--line-height);
  }
}
```

```html
<h1 class="text-display">Landing title</h1>
```

### 425: How would you implement density modes (compact vs comfortable) with Tailwind?

Change `--spacing` for a section.

```html
<div class="[--spacing:0.2rem]">
  <table>
    ...
  </table>
</div>
```

Because every spacing utility uses `calc(var(--spacing) * n)`, changing `--spacing` on a container rescales all padding, margin and gap inside it. Note that this only works when the theme variable is referenced (the default), not inlined.

### 426: How do you test responsive variants in automated tests?

Use a real browser and change the viewport.

```ts
test("sidebar is hidden on mobile", async ({ page }) => {
  await page.setViewportSize({ width: 375, height: 800 });
  await page.goto("/dashboard");
  await expect(page.getByRole("complementary")).toBeHidden();
});
```

For container queries, resize the container's parent in the test or render the component in differently sized wrappers in Storybook.

### 427: How do you handle print layouts with Tailwind in detail?

```html
<body class="print:bg-white print:text-black">
  <nav class="print:hidden">...</nav>
  <article class="max-w-prose print:max-w-none">
    <h2 class="break-after-avoid">Section</h2>
    <figure class="break-inside-avoid">...</figure>
  </article>
  <a
    href="https://example.com"
    class="print:after:ml-1 print:after:content-[attr(href)]"
    >Link</a
  >
</body>
```

Use `break-before-page`, `break-inside-avoid` and `print:` variants. Page margins still need a custom `@page` rule in CSS.

### 428: How do you use `@starting-style` and popovers to build a dropdown with no JavaScript?

```html
<button popovertarget="menu" class="rounded px-3 py-2">Options</button>
<div
  id="menu"
  popover
  class="m-0 rounded-lg border bg-white p-2 shadow-lg opacity-0 transition-all transition-discrete
         open:opacity-100 starting:open:opacity-0 starting:open:scale-95"
>
  <a class="block rounded px-3 py-1 hover:bg-gray-100" href="#">Edit</a>
</div>
```

Positioning next to the button can use CSS anchor positioning in supporting browsers, through arbitrary properties like `[position-anchor:--menu-btn]`.

### 429: How do you handle long class lists in templates for readability?

- Let Prettier sort them; it also wraps lines in some editors.
- Group related classes on separate lines in template literals or arrays with `clsx`.
- Extract variants with `cva`.
- Move large repeated blocks into components.

```jsx
const classes = clsx(
  "flex items-center gap-2", // layout
  "rounded-md px-3 py-2", // box
  "text-sm font-medium", // text
  "hover:bg-gray-100 focus-visible:outline-2", // states
);
```

### 430: What is "arbitrary value overuse" and why is it a code smell?

If a codebase has many `mt-[13px]`, `text-[#3a3a3a]`, `w-[372px]`, it means the design system isn't being followed or the theme is missing tokens. It makes the UI inconsistent and harder to change. When the same arbitrary value appears more than once or twice, add it to `@theme` with a meaningful name.

### 431: How do you build a reusable pattern for "polymorphic" components with Tailwind?

Keep styles in the component and allow the element to change.

```tsx
type Props<T extends React.ElementType> = {
  as?: T;
  className?: string;
} & React.ComponentPropsWithoutRef<T>;

export function Text<T extends React.ElementType = "p">({
  as,
  className,
  ...props
}: Props<T>) {
  const Comp = as ?? "p";
  return (
    <Comp className={cn("text-base/7 text-gray-700", className)} {...props} />
  );
}

<Text as="span" className="text-sm">
  Small
</Text>;
```

### 432: How do you handle styling of child elements you can't edit (like a third-party widget)?

Use arbitrary variants or `**:` / `*:` from the parent, or target its classes with nested selectors.

```html
<div
  class="[&_.widget-title]:text-lg [&_.widget-title]:font-semibold **:data-[slot=icon]:size-4"
>
  <ThirdPartyWidget />
</div>
```

If the widget uses unlayered CSS with high specificity, import its stylesheet into a layer first so these rules can win.

### 433: How do you manage icon sizes consistently?

Use `size-*` and a `data-slot` or child selector from the parent.

```html
<button class="inline-flex items-center gap-2 *:[svg]:size-4 *:[svg]:shrink-0">
  <svg>...</svg> Save
</button>
```

`*:[svg]:size-4` applies to direct children that are SVGs. This is the pattern many component libraries use.

### 434: How would you structure Tailwind in a design system with tokens, primitives and recipes?

1. Tokens: `theme.css` with `@theme` and semantic `@theme inline` mappings.
2. Utilities and variants: `@utility` and `@custom-variant` shared by all apps.
3. Primitives: unstyled behavior components (from a headless library or your own).
4. Recipes: `cva` definitions that map props to class strings.
5. Components: primitives + recipes, exported to apps.
6. Docs: Storybook with all variants and visual tests.

Apps import the CSS package and component package, add `@source` for the components, and use only exported components and semantic utilities.

### 435: How do you allow consumers of your design system to customize it?

- Expose semantic CSS variables that they can override (`--color-primary`).
- Accept `className` props merged with `tailwind-merge`.
- Expose `data-slot` attributes on inner parts so they can target them with `*:data-[slot=x]:` or `**:data-[slot=x]:`.
- Document which variables and slots are public API.

### 436: How do you version and roll out theme changes safely across many apps?

Publish the theme as a versioned package. Use semantic tokens so most changes are value updates, not class renames. For breaking changes (removed tokens), keep the old names as aliases for one release, mark them deprecated, and use a codemod or search to update usage. Visual regression tests in each app catch unexpected differences.

### 437: How do you write a codemod to rename Tailwind classes?

Treat class strings as text and use a careful regex with word boundaries, or use a tool that parses JSX/HTML and only touches `class`/`className` attributes and known helper calls.

```js
// rename "btn-primary" utility to "button-primary" in className strings
source.replace(/(?<=["'`\s])btn-primary(?=["'`\s])/g, "button-primary");
```

Then run Prettier with the Tailwind plugin to fix ordering. The official upgrade tool is a good example of this approach.

### 438: How do you handle `className` props in a component when variant classes might conflict with user classes?

Use `tailwind-merge` at the end so user classes win:

```tsx
<button className={cn(buttonVariants({ size }), className)} />
```

Without it, `className="px-8"` combined with a variant's `px-4` would produce both classes, and whichever comes later in the CSS file wins, which is not necessarily the one the user passed.

### 439: Why is "the last class wins" not true in plain Tailwind?

Because the HTML class order has no effect. Only the CSS rule order and specificity matter. `class="px-4 px-8"` uses whichever of `.px-4` or `.px-8` appears later in the stylesheet. Tailwind sorts by value in a consistent order, so it might be `px-8`, but you shouldn't rely on it. `tailwind-merge` exists to make "last class wins" true at runtime.

### 440: How can Tailwind v4's CSS-first config work with TypeScript type safety?

The theme isn't in TypeScript, so you lose autocompletion of tokens in TS code. Common solutions:

- Rely on IntelliSense in editors, which reads your CSS file.
- Generate a `tokens.ts` from your token JSON at the same time you generate `@theme`.
- Type variant props with `cva`'s `VariantProps` rather than raw class names.

### 441: How do you implement skeleton/loading states without layout shift?

Give skeletons the same box size as the final content: same height, same `aspect-*`, same line heights.

```html
<div class="aspect-video w-full animate-pulse rounded-lg bg-gray-200"></div>
<p class="mt-4 h-[1lh] w-3/4 animate-pulse rounded bg-gray-200"></p>
```

`h-[1lh]` uses the line-height unit, so the placeholder matches one line of text.

### 442: What CSS units are useful as Tailwind arbitrary values in modern layouts?

- `dvh`, `svh`, `lvh` for viewport height on mobile (also built-in `h-dvh`, etc.).
- `cqw`, `cqh`, `cqi`, `cqb` for container-relative sizes.
- `lh` and `rlh` for line-height based spacing.
- `ch` for text widths (`max-w-[65ch]`).
- `fr` in grid templates.

### 443: How would you approach performance auditing of CSS in a Tailwind project?

- Check the size of the built CSS (usually 10–30 kB gzipped even for large apps). If much bigger, look for huge safelists, scanned data files, or multiple Tailwind builds.
- Use Chrome DevTools Coverage to see unused CSS per page.
- Check for duplicated Preflight from multiple builds.
- Look at render performance (paint and layout) in the Performance panel for expensive effects like blurs and large shadows.

### 444: How can a big JSON or Markdown content folder slow down Tailwind builds, and how do you fix it?

Automatic detection scans all non-ignored text files. A huge content folder (thousands of Markdown files or a large JSON dataset) adds scanning time and can generate stray classes. Exclude it with `@source not "../content/data";` or move it into a gitignored folder. If the Markdown does contain classes you need, keep it scanned but exclude only data files.

### 445: What changes did v4.1 bring that matter for older browser support?

v4.1 improved how the output behaves in older browsers (for example older Safari versions): it added fallbacks so colors that use `oklch()` and `color-mix()`, and features that rely on `@property`, still render reasonably. The official supported browser list didn't change, but sites degrade more gracefully instead of breaking completely.

### 446: How do you build a theme switcher component that works with server rendering and avoids flicker?

1. Store the choice in a cookie (not only localStorage) so the server can read it.
2. On the server, render `<html data-theme="dark">` when the cookie says so.
3. For "system", render without the attribute and let the CSS `prefers-color-scheme` branch handle it (see the combined custom variant above).
4. On change, update the attribute and cookie on the client:

```ts
function setTheme(theme: "light" | "dark" | "system") {
  const root = document.documentElement;
  if (theme === "system") root.removeAttribute("data-theme");
  else root.dataset.theme = theme;
  document.cookie = `theme=${theme}; path=/; max-age=31536000`;
}
```

No inline blocking script is needed because the server already sends the right attribute.

### 447: How do you handle CSS for third-party components that are rendered into a portal?

Portals render at the end of `<body>`, outside your component tree, so:

- `group-*`, `peer-*` and `in-*` variants based on your component's ancestors won't apply.
- Scoped themes based on a container (like `data-theme` on a section) won't reach it.
- Pass the theme attribute or class to the portal container, or rely on themes set on `<html>`.
- Use high-enough z-index via a shared scale.

### 448: What should you consider when using Tailwind with CSS anchor positioning?

Tailwind v4 doesn't have dedicated anchor utilities at the time of writing, so use arbitrary properties:

```html
<button class="[anchor-name:--trigger]">Open</button>
<div
  popover
  class="absolute [position-anchor:--trigger] top-[anchor(bottom)] left-[anchor(left)]"
>
  ...
</div>
```

Wrap them in `supports-[anchor-name:--a]:` or provide a fallback position, since browser support is still uneven.

### 449: How would you explain the main architecture changes of Tailwind v4 to a team in a few points?

- Engine: rewritten, Rust scanner + Lightning CSS, much faster builds.
- Config: CSS-first with `@theme`, `@utility`, `@custom-variant`, `@plugin`, `@source`.
- Detection: automatic, using `.gitignore`; `@source` for exceptions.
- Modern CSS: native cascade layers, `@property`, `color-mix()`, OKLCH colors, container queries in core.
- Theme as CSS variables: all tokens available at runtime with `var()`.
- Dynamic values: any number for spacing and grid, `(--var)` shorthand.
- New features through 4.1–4.3: text shadows, masks, logical utilities, new palettes, scrollbar utilities, `@container-size`, `zoom-*`, `tab-*`, stacked `@variant`, `--default()`.

### 450: What is a good answer to "When would you NOT use Tailwind?"

- When the team strongly prefers semantic CSS and has a mature CSS architecture already.
- When you need to support old browsers that v4 doesn't (use v3.4 or another approach).
- For HTML emails, where inline styles and old CSS are required (use special tools).
- For very small static pages where a few lines of CSS are simpler than a build step.
- When most styles come from user-defined values at runtime (for example a website builder), where CSS variables or inline styles may fit better.

Otherwise, for most application UIs built with components, Tailwind is a good default.
