# Web Accessibility Interview Questions and Answers

_Last updated: November 25, 2026_

This file has 450 interview questions and answers about web accessibility: 150 easy, 150 moderate and 150 advanced. The answers follow WCAG 2.2 (the current W3C standard), WAI-ARIA 1.2 and the ARIA Authoring Practices Guide, with notes on WCAG 3 and ARIA 1.3, which are still drafts. Code examples use HTML, CSS, JavaScript and React.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is web accessibility?](#1-what-is-web-accessibility)
- [2: Why is it called "a11y"?](#2-why-is-it-called-a11y)
- [3: Why does web accessibility matter?](#3-why-does-web-accessibility-matter)
- [4: Who benefits from accessible websites?](#4-who-benefits-from-accessible-websites)
- [5: What are the main types of disabilities you should think about when building for the web?](#5-what-are-the-main-types-of-disabilities-you-should-think-about-when-building-for-the-web)
- [6: What is the difference between permanent, temporary and situational disabilities?](#6-what-is-the-difference-between-permanent-temporary-and-situational-disabilities)
- [7: What is WCAG?](#7-what-is-wcag)
- [8: What versions of WCAG exist?](#8-what-versions-of-wcag-exist)
- [9: What does POUR stand for?](#9-what-does-pour-stand-for)
- [10: What are WCAG conformance levels?](#10-what-are-wcag-conformance-levels)
- [11: Which WCAG level should most websites aim for?](#11-which-wcag-level-should-most-websites-aim-for)
- [12: What is a success criterion in WCAG?](#12-what-is-a-success-criterion-in-wcag)
- [13: What is assistive technology?](#13-what-is-assistive-technology)
- [14: What is a screen reader?](#14-what-is-a-screen-reader)
- [15: Name some popular screen readers.](#15-name-some-popular-screen-readers)
- [16: How do you turn on VoiceOver on a Mac?](#16-how-do-you-turn-on-voiceover-on-a-mac)
- [17: What is a braille display?](#17-what-is-a-braille-display)
- [18: What is screen magnification software?](#18-what-is-screen-magnification-software)
- [19: What is voice control software?](#19-what-is-voice-control-software)
- [20: What are switch devices?](#20-what-are-switch-devices)
- [21: What is semantic HTML?](#21-what-is-semantic-html)
- [22: Why is a div with a click handler not a real button?](#22-why-is-a-div-with-a-click-handler-not-a-real-button)
- [23: When should you use a link and when should you use a button?](#23-when-should-you-use-a-link-and-when-should-you-use-a-button)
- [24: What is alt text?](#24-what-is-alt-text)
- [25: How do you write good alt text?](#25-how-do-you-write-good-alt-text)
- [26: When should alt text be empty?](#26-when-should-alt-text-be-empty)
- [27: What is the difference between alt="" and no alt attribute?](#27-what-is-the-difference-between-alt-and-no-alt-attribute)
- [28: What is WCAG 1.1.1 Non-text Content?](#28-what-is-wcag-111-non-text-content)
- [29: How should you handle images that contain text?](#29-how-should-you-handle-images-that-contain-text)
- [30: What is the purpose of headings for accessibility?](#30-what-is-the-purpose-of-headings-for-accessibility)
- [31: Is it okay to skip heading levels?](#31-is-it-okay-to-skip-heading-levels)
- [32: How many h1 elements should a page have?](#32-how-many-h1-elements-should-a-page-have)
- [33: What are landmarks?](#33-what-are-landmarks)
- [34: How many main elements should a page have?](#34-how-many-main-elements-should-a-page-have)
- [35: What is the lang attribute and why does it matter?](#35-what-is-the-lang-attribute-and-why-does-it-matter)
- [36: How do you mark a phrase in a different language?](#36-how-do-you-mark-a-phrase-in-a-different-language)
- [37: Why is the page title important for accessibility?](#37-why-is-the-page-title-important-for-accessibility)
- [38: What is keyboard accessibility?](#38-what-is-keyboard-accessibility)
- [39: Which keys do keyboard users rely on?](#39-which-keys-do-keyboard-users-rely-on)
- [40: What is keyboard focus?](#40-what-is-keyboard-focus)
- [41: What is a focus indicator?](#41-what-is-a-focus-indicator)
- [42: Why should you never remove the focus outline without replacing it?](#42-why-should-you-never-remove-the-focus-outline-without-replacing-it)
- [43: What is a skip link?](#43-what-is-a-skip-link)
- [44: What does tabindex do?](#44-what-does-tabindex-do)
- [45: Why should you avoid positive tabindex values?](#45-why-should-you-avoid-positive-tabindex-values)
- [46: What is tab order and how is it decided?](#46-what-is-tab-order-and-how-is-it-decided)
- [47: What is a keyboard trap?](#47-what-is-a-keyboard-trap)
- [48: What is color contrast?](#48-what-is-color-contrast)
- [49: What contrast ratios does WCAG require?](#49-what-contrast-ratios-does-wcag-require)
- [50: Can you use color alone to show information?](#50-can-you-use-color-alone-to-show-information)
- [51: What is color blindness and how common is it?](#51-what-is-color-blindness-and-how-common-is-it)
- [52: How can you check color contrast?](#52-how-can-you-check-color-contrast)
- [53: What are form labels and why are they needed?](#53-what-are-form-labels-and-why-are-they-needed)
- [54: Why is a placeholder not a replacement for a label?](#54-why-is-a-placeholder-not-a-replacement-for-a-label)
- [55: What are fieldset and legend used for?](#55-what-are-fieldset-and-legend-used-for)
- [56: How do you mark a field as required in an accessible way?](#56-how-do-you-mark-a-field-as-required-in-an-accessible-way)
- [57: How should form error messages be shown?](#57-how-should-form-error-messages-be-shown)
- [58: What does the autocomplete attribute have to do with accessibility?](#58-what-does-the-autocomplete-attribute-have-to-do-with-accessibility)
- [59: Why should you use the correct input type?](#59-why-should-you-use-the-correct-input-type)
- [60: What is ARIA?](#60-what-is-aria)
- [61: What is the first rule of ARIA?](#61-what-is-the-first-rule-of-aria)
- [62: What does "no ARIA is better than bad ARIA" mean?](#62-what-does-no-aria-is-better-than-bad-aria-mean)
- [63: What are ARIA roles, states and properties?](#63-what-are-aria-roles-states-and-properties)
- [64: What does aria-label do?](#64-what-does-aria-label-do)
- [65: What does aria-labelledby do?](#65-what-does-aria-labelledby-do)
- [66: What does aria-describedby do?](#66-what-does-aria-describedby-do)
- [67: What does aria-hidden="true" do?](#67-what-does-aria-hiddentrue-do)
- [68: What is the accessibility tree?](#68-what-is-the-accessibility-tree)
- [69: What is an accessible name?](#69-what-is-an-accessible-name)
- [70: What does WCAG 4.1.2 Name, Role, Value mean?](#70-what-does-wcag-412-name-role-value-mean)
- [71: How do you make a data table accessible?](#71-how-do-you-make-a-data-table-accessible)
- [72: Should you use tables for page layout?](#72-should-you-use-tables-for-page-layout)
- [73: Why should lists use ul, ol or dl?](#73-why-should-lists-use-ul-ol-or-dl)
- [74: What are captions?](#74-what-are-captions)
- [75: What is the difference between captions and subtitles?](#75-what-is-the-difference-between-captions-and-subtitles)
- [76: What is a transcript?](#76-what-is-a-transcript)
- [77: What is audio description?](#77-what-is-audio-description)
- [78: Why is autoplaying audio a problem?](#78-why-is-autoplaying-audio-a-problem)
- [79: What is WCAG 2.3.1 Three Flashes or Below Threshold?](#79-what-is-wcag-231-three-flashes-or-below-threshold)
- [80: What does prefers-reduced-motion do?](#80-what-does-prefers-reduced-motion-do)
- [81: What is the visually hidden or sr-only class?](#81-what-is-the-visually-hidden-or-sr-only-class)
- [82: What is the difference between display none, visibility hidden and the sr-only class?](#82-what-is-the-difference-between-display-none-visibility-hidden-and-the-sr-only-class)
- [83: What does the hidden attribute do?](#83-what-does-the-hidden-attribute-do)
- [84: Do iframes need a title?](#84-do-iframes-need-a-title)
- [85: How do you make an icon button accessible?](#85-how-do-you-make-an-icon-button-accessible)
- [86: Why should link text make sense on its own?](#86-why-should-link-text-make-sense-on-its-own)
- [87: What are some quick ways to test a site for accessibility?](#87-what-are-some-quick-ways-to-test-a-site-for-accessibility)
- [88: What is Lighthouse's accessibility score?](#88-what-is-lighthouses-accessibility-score)
- [89: What is axe?](#89-what-is-axe)
- [90: What is WAVE?](#90-what-is-wave)
- [91: How much can automated testing find?](#91-how-much-can-automated-testing-find)
- [92: What is manual accessibility testing?](#92-what-is-manual-accessibility-testing)
- [93: Which laws require web accessibility?](#93-which-laws-require-web-accessibility)
- [94: What is Section 508?](#94-what-is-section-508)
- [95: What is the European Accessibility Act?](#95-what-is-the-european-accessibility-act)
- [96: What is EN 301 549?](#96-what-is-en-301-549)
- [97: What is a VPAT or ACR?](#97-what-is-a-vpat-or-acr)
- [98: What are accessibility overlays and why are they criticized?](#98-what-are-accessibility-overlays-and-why-are-they-criticized)
- [99: What is the curb cut effect?](#99-what-is-the-curb-cut-effect)
- [100: What is inclusive design?](#100-what-is-inclusive-design)
- [101: What is the difference between accessibility and usability?](#101-what-is-the-difference-between-accessibility-and-usability)
- [102: What does WCAG 1.4.4 Resize Text require?](#102-what-does-wcag-144-resize-text-require)
- [103: What is reflow in WCAG?](#103-what-is-reflow-in-wcag)
- [104: Why should you never disable zoom on mobile?](#104-why-should-you-never-disable-zoom-on-mobile)
- [105: Why use rem or em instead of px for font sizes?](#105-why-use-rem-or-em-instead-of-px-for-font-sizes)
- [106: What is WCAG 1.4.12 Text Spacing?](#106-what-is-wcag-1412-text-spacing)
- [107: What is the minimum target size in WCAG 2.2?](#107-what-is-the-minimum-target-size-in-wcag-22)
- [108: What did WCAG 2.2 add?](#108-what-did-wcag-22-add)
- [109: What is WCAG 2.4.11 Focus Not Obscured?](#109-what-is-wcag-2411-focus-not-obscured)
- [110: What is WCAG 2.5.7 Dragging Movements?](#110-what-is-wcag-257-dragging-movements)
- [111: What is WCAG 3.3.7 Redundant Entry?](#111-what-is-wcag-337-redundant-entry)
- [112: What is WCAG 3.3.8 Accessible Authentication?](#112-what-is-wcag-338-accessible-authentication)
- [113: What is WCAG 3.2.6 Consistent Help?](#113-what-is-wcag-326-consistent-help)
- [114: What is CAPTCHA and why is it an accessibility problem?](#114-what-is-captcha-and-why-is-it-an-accessibility-problem)
- [115: What are time limits in WCAG?](#115-what-are-time-limits-in-wcag)
- [116: What is WCAG 2.2.2 Pause, Stop, Hide?](#116-what-is-wcag-222-pause-stop-hide)
- [117: What is the forced colors mode?](#117-what-is-the-forced-colors-mode)
- [118: What is the difference between dark mode and high contrast?](#118-what-is-the-difference-between-dark-mode-and-high-contrast)
- [119: What are browse mode and focus mode in screen readers?](#119-what-are-browse-mode-and-focus-mode-in-screen-readers)
- [120: How do screen reader users usually navigate a page?](#120-how-do-screen-reader-users-usually-navigate-a-page)
- [121: What is the reading order and why does it matter?](#121-what-is-the-reading-order-and-why-does-it-matter)
- [122: Should a button have a type attribute?](#122-should-a-button-have-a-type-attribute)
- [123: What is the problem with disabled buttons?](#123-what-is-the-problem-with-disabled-buttons)
- [124: What do details and summary do for accessibility?](#124-what-do-details-and-summary-do-for-accessibility)
- [125: What is the dialog element?](#125-what-is-the-dialog-element)
- [126: What is cognitive accessibility?](#126-what-is-cognitive-accessibility)
- [127: Why does plain language help accessibility?](#127-why-does-plain-language-help-accessibility)
- [128: How should you write instructions so they don't depend on the senses?](#128-how-should-you-write-instructions-so-they-dont-depend-on-the-senses)
- [129: Why shouldn't content change orientation lock?](#129-why-shouldnt-content-change-orientation-lock)
- [130: What is aria-current used for?](#130-what-is-aria-current-used-for)
- [131: What is aria-expanded used for?](#131-what-is-aria-expanded-used-for)
- [132: What is aria-pressed used for?](#132-what-is-aria-pressed-used-for)
- [133: What is aria-invalid?](#133-what-is-aria-invalid)
- [134: What is the difference between required and aria-required?](#134-what-is-the-difference-between-required-and-aria-required)
- [135: What is an ARIA live region?](#135-what-is-an-aria-live-region)
- [136: What is role="alert"?](#136-what-is-rolealert)
- [137: Why do multiple nav elements need labels?](#137-why-do-multiple-nav-elements-need-labels)
- [138: What are figure and figcaption for?](#138-what-are-figure-and-figcaption-for)
- [139: How do you make complex images like charts accessible?](#139-how-do-you-make-complex-images-like-charts-accessible)
- [140: Should the title attribute be used for accessibility?](#140-should-the-title-attribute-be-used-for-accessibility)
- [141: What does WCAG 2.4.6 Headings and Labels mean?](#141-what-does-wcag-246-headings-and-labels-mean)
- [142: What is the multiple ways criterion?](#142-what-is-the-multiple-ways-criterion)
- [143: What does consistent navigation mean in WCAG?](#143-what-does-consistent-navigation-mean-in-wcag)
- [144: What is a change of context in WCAG?](#144-what-is-a-change-of-context-in-wcag)
- [145: Should links open in new tabs?](#145-should-links-open-in-new-tabs)
- [146: How should SVG images be made accessible?](#146-how-should-svg-images-be-made-accessible)
- [147: What is the role of emoji in accessibility?](#147-what-is-the-role-of-emoji-in-accessibility)
- [148: How do you test a page with the keyboard only?](#148-how-do-you-test-a-page-with-the-keyboard-only)
- [149: What is an accessibility statement?](#149-what-is-an-accessibility-statement)
- [150: Where can developers learn more about accessibility?](#150-where-can-developers-learn-more-about-accessibility)

### Moderate Questions (151-300)

- [151: How do you build an accessible modal dialog?](#151-how-do-you-build-an-accessible-modal-dialog)
- [152: Where should focus go when a modal opens?](#152-where-should-focus-go-when-a-modal-opens)
- [153: Why must focus return to the trigger when a dialog closes?](#153-why-must-focus-return-to-the-trigger-when-a-dialog-closes)
- [154: What does the inert attribute do?](#154-what-does-the-inert-attribute-do)
- [155: How did developers trap focus in modals before inert and dialog existed?](#155-how-did-developers-trap-focus-in-modals-before-inert-and-dialog-existed)
- [156: What does aria-modal="true" do?](#156-what-does-aria-modaltrue-do)
- [157: How do you build an accessible disclosure (show/hide) widget?](#157-how-do-you-build-an-accessible-disclosure-showhide-widget)
- [158: How do you build an accessible accordion?](#158-how-do-you-build-an-accessible-accordion)
- [159: How do you build accessible tabs?](#159-how-do-you-build-accessible-tabs)
- [160: What is a roving tabindex?](#160-what-is-a-roving-tabindex)
- [161: Should tabs activate automatically when focused or only on Enter?](#161-should-tabs-activate-automatically-when-focused-or-only-on-enter)
- [162: When should you not use the ARIA menu role?](#162-when-should-you-not-use-the-aria-menu-role)
- [163: How do you build an accessible dropdown navigation menu?](#163-how-do-you-build-an-accessible-dropdown-navigation-menu)
- [164: How do you build an accessible menu button?](#164-how-do-you-build-an-accessible-menu-button)
- [165: What is a combobox?](#165-what-is-a-combobox)
- [166: What is aria-activedescendant?](#166-what-is-aria-activedescendant)
- [167: How do you build an accessible custom select or listbox?](#167-how-do-you-build-an-accessible-custom-select-or-listbox)
- [168: How do you make a custom checkbox accessible?](#168-how-do-you-make-a-custom-checkbox-accessible)
- [169: How do you build an accessible toggle switch?](#169-how-do-you-build-an-accessible-toggle-switch)
- [170: How do you build an accessible tooltip?](#170-how-do-you-build-an-accessible-tooltip)
- [171: What is WCAG 1.4.13 Content on Hover or Focus?](#171-what-is-wcag-1413-content-on-hover-or-focus)
- [172: How do you announce toast notifications?](#172-how-do-you-announce-toast-notifications)
- [173: What is the difference between aria-live polite and assertive?](#173-what-is-the-difference-between-aria-live-polite-and-assertive)
- [174: Why must a live region exist before you update it?](#174-why-must-a-live-region-exist-before-you-update-it)
- [175: What do aria-atomic and aria-relevant do?](#175-what-do-aria-atomic-and-aria-relevant-do)
- [176: What are role="status", role="log" and role="timer"?](#176-what-are-rolestatus-rolelog-and-roletimer)
- [177: How do you announce loading states?](#177-how-do-you-announce-loading-states)
- [178: What does aria-busy do?](#178-what-does-aria-busy-do)
- [179: How do you manage focus after a route change in a single page app?](#179-how-do-you-manage-focus-after-a-route-change-in-a-single-page-app)
- [180: Do frameworks like Next.js handle route announcements?](#180-do-frameworks-like-nextjs-handle-route-announcements)
- [181: How do you associate labels with inputs in React?](#181-how-do-you-associate-labels-with-inputs-in-react)
- [182: How do you move focus in React?](#182-how-do-you-move-focus-in-react)
- [183: Why do React fragments help accessibility?](#183-why-do-react-fragments-help-accessibility)
- [184: What is eslint-plugin-jsx-a11y?](#184-what-is-eslint-plugin-jsx-a11y)
- [185: How do you test accessibility with jest-axe?](#185-how-do-you-test-accessibility-with-jest-axe)
- [186: Why does Testing Library recommend getByRole?](#186-why-does-testing-library-recommend-getbyrole)
- [187: How do you run axe in Playwright?](#187-how-do-you-run-axe-in-playwright)
- [188: How do you test keyboard behavior in automated tests?](#188-how-do-you-test-keyboard-behavior-in-automated-tests)
- [189: What is the Storybook accessibility addon?](#189-what-is-the-storybook-accessibility-addon)
- [190: How do you add accessibility checks to CI?](#190-how-do-you-add-accessibility-checks-to-ci)
- [191: How do you do a basic screen reader test?](#191-how-do-you-do-a-basic-screen-reader-test)
- [192: Which screen reader and browser combinations should you test with?](#192-which-screen-reader-and-browser-combinations-should-you-test-with)
- [193: What are some useful NVDA keyboard shortcuts?](#193-what-are-some-useful-nvda-keyboard-shortcuts)
- [194: What is the VoiceOver rotor?](#194-what-is-the-voiceover-rotor)
- [195: How do you inspect the accessibility tree in Chrome DevTools?](#195-how-do-you-inspect-the-accessibility-tree-in-chrome-devtools)
- [196: How is the accessible name of a button calculated?](#196-how-is-the-accessible-name-of-a-button-calculated)
- [197: Can aria-labelledby reference multiple elements?](#197-can-aria-labelledby-reference-multiple-elements)
- [198: What is aria-errormessage and how does it differ from aria-describedby?](#198-what-is-aria-errormessage-and-how-does-it-differ-from-aria-describedby)
- [199: How should you show form errors after submit?](#199-how-should-you-show-form-errors-after-submit)
- [200: Should you validate fields while the user types?](#200-should-you-validate-fields-while-the-user-types)
- [201: What does WCAG 3.3.2 Labels or Instructions require?](#201-what-does-wcag-332-labels-or-instructions-require)
- [202: What does WCAG 3.3.4 Error Prevention mean?](#202-what-does-wcag-334-error-prevention-mean)
- [203: How do you make radio buttons accessible?](#203-how-do-you-make-radio-buttons-accessible)
- [204: How do you make a date picker accessible?](#204-how-do-you-make-a-date-picker-accessible)
- [205: How do you make a slider accessible?](#205-how-do-you-make-a-slider-accessible)
- [206: How do you make a progress bar accessible?](#206-how-do-you-make-a-progress-bar-accessible)
- [207: How do you make a file upload accessible?](#207-how-do-you-make-a-file-upload-accessible)
- [208: What does :focus-visible do?](#208-what-does-focus-visible-do)
- [209: What does :focus-within do?](#209-what-does-focus-within-do)
- [210: What is WCAG 1.4.11 Non-text Contrast?](#210-what-is-wcag-1411-non-text-contrast)
- [211: What is WCAG 2.4.13 Focus Appearance?](#211-what-is-wcag-2413-focus-appearance)
- [212: How do you design a focus indicator that works on any background?](#212-how-do-you-design-a-focus-indicator-that-works-on-any-background)
- [213: How do you keep focused elements from hiding under sticky headers?](#213-how-do-you-keep-focused-elements-from-hiding-under-sticky-headers)
- [214: How do you support forced colors mode in CSS?](#214-how-do-you-support-forced-colors-mode-in-css)
- [215: What does prefers-contrast do?](#215-what-does-prefers-contrast-do)
- [216: How do you respect reduced motion in JavaScript?](#216-how-do-you-respect-reduced-motion-in-javascript)
- [217: What is WCAG 2.3.3 Animation from Interactions?](#217-what-is-wcag-233-animation-from-interactions)
- [218: Does CSS generated content get read by screen readers?](#218-does-css-generated-content-get-read-by-screen-readers)
- [219: How can CSS display values break semantics?](#219-how-can-css-display-values-break-semantics)
- [220: How can flexbox and grid order break accessibility?](#220-how-can-flexbox-and-grid-order-break-accessibility)
- [221: How should icon fonts be handled?](#221-how-should-icon-fonts-be-handled)
- [222: How do you write accessible breadcrumbs?](#222-how-do-you-write-accessible-breadcrumbs)
- [223: How do you make pagination accessible?](#223-how-do-you-make-pagination-accessible)
- [224: What accessibility problems does infinite scroll cause?](#224-what-accessibility-problems-does-infinite-scroll-cause)
- [225: How do you make a sortable table accessible?](#225-how-do-you-make-a-sortable-table-accessible)
- [226: How do you make tables readable on small screens without breaking them?](#226-how-do-you-make-tables-readable-on-small-screens-without-breaking-them)
- [227: When do you need the headers attribute in tables?](#227-when-do-you-need-the-headers-attribute-in-tables)
- [228: What is the difference between role="presentation" and aria-hidden="true"?](#228-what-is-the-difference-between-rolepresentation-and-aria-hiddentrue)
- [229: When is role="presentation" ignored?](#229-when-is-rolepresentation-ignored)
- [230: Why is aria-hidden on a focusable element a problem?](#230-why-is-aria-hidden-on-a-focusable-element-a-problem)
- [231: When should you use the region role or a named section?](#231-when-should-you-use-the-region-role-or-a-named-section)
- [232: What is the search element?](#232-what-is-the-search-element)
- [233: When is a form element a landmark?](#233-when-is-a-form-element-a-landmark)
- [234: What does aria-controls do and is it well supported?](#234-what-does-aria-controls-do-and-is-it-well-supported)
- [235: What does aria-haspopup do?](#235-what-does-aria-haspopup-do)
- [236: What does aria-owns do?](#236-what-does-aria-owns-do)
- [237: How do you make the popover attribute accessible?](#237-how-do-you-make-the-popover-attribute-accessible)
- [238: What is the difference between a modal and a non-modal dialog?](#238-what-is-the-difference-between-a-modal-and-a-non-modal-dialog)
- [239: What is the alertdialog role?](#239-what-is-the-alertdialog-role)
- [240: Is the autofocus attribute good or bad for accessibility?](#240-is-the-autofocus-attribute-good-or-bad-for-accessibility)
- [241: How do you build an accessible carousel?](#241-how-do-you-build-an-accessible-carousel)
- [242: What is aria-roledescription and when should you use it?](#242-what-is-aria-roledescription-and-when-should-you-use-it)
- [243: How do you make a video player accessible?](#243-how-do-you-make-a-video-player-accessible)
- [244: What is WebVTT?](#244-what-is-webvtt)
- [245: What is the difference between automatic captions and accurate captions?](#245-what-is-the-difference-between-automatic-captions-and-accurate-captions)
- [246: How do you make drag and drop accessible?](#246-how-do-you-make-drag-and-drop-accessible)
- [247: How do you handle gestures like swipe or pinch?](#247-how-do-you-handle-gestures-like-swipe-or-pinch)
- [248: What is WCAG 2.5.2 Pointer Cancellation?](#248-what-is-wcag-252-pointer-cancellation)
- [249: What is WCAG 2.5.3 Label in Name?](#249-what-is-wcag-253-label-in-name)
- [250: What is WCAG 2.5.4 Motion Actuation?](#250-what-is-wcag-254-motion-actuation)
- [251: What is WCAG 2.1.4 Character Key Shortcuts?](#251-what-is-wcag-214-character-key-shortcuts)
- [252: What is WCAG 4.1.3 Status Messages?](#252-what-is-wcag-413-status-messages)
- [253: What does WCAG 1.3.1 Info and Relationships require?](#253-what-does-wcag-131-info-and-relationships-require)
- [254: Why was WCAG 4.1.1 Parsing removed in 2.2?](#254-why-was-wcag-411-parsing-removed-in-22)
- [255: What is WCAG 2.4.3 Focus Order and how do you fail it?](#255-what-is-wcag-243-focus-order-and-how-do-you-fail-it)
- [256: What are common reasons an accessible name is missing?](#256-what-are-common-reasons-an-accessible-name-is-missing)
- [257: What is wrong with this code: an image link with alt=""?](#257-what-is-wrong-with-this-code-an-image-link-with-alt)
- [258: How do you write alt text for a linked logo?](#258-how-do-you-write-alt-text-for-a-linked-logo)
- [259: How do you handle repeated "Read more" links?](#259-how-do-you-handle-repeated-read-more-links)
- [260: How do you make a card component with a link accessible?](#260-how-do-you-make-a-card-component-with-a-link-accessible)
- [261: Why should headings not be used just for styling?](#261-why-should-headings-not-be-used-just-for-styling)
- [262: How do you build a heading structure for a complex page?](#262-how-do-you-build-a-heading-structure-for-a-complex-page)
- [263: How do you make a search results page accessible?](#263-how-do-you-make-a-search-results-page-accessible)
- [264: What is the problem with "click here" style instructions?](#264-what-is-the-problem-with-click-here-style-instructions)
- [265: Should links to files mention the file type and size?](#265-should-links-to-files-mention-the-file-type-and-size)
- [266: What makes a PDF accessible?](#266-what-makes-a-pdf-accessible)
- [267: How do you make a canvas element accessible?](#267-how-do-you-make-a-canvas-element-accessible)
- [268: How do you make charts accessible?](#268-how-do-you-make-charts-accessible)
- [269: How do you make an interactive map accessible?](#269-how-do-you-make-an-interactive-map-accessible)
- [270: How do you write an accessibility bug report?](#270-how-do-you-write-an-accessibility-bug-report)
- [271: How do you prioritize accessibility issues?](#271-how-do-you-prioritize-accessibility-issues)
- [272: What is an accessibility audit?](#272-what-is-an-accessibility-audit)
- [273: How do designers help with accessibility before development?](#273-how-do-designers-help-with-accessibility-before-development)
- [274: How do design systems help accessibility?](#274-how-do-design-systems-help-accessibility)
- [275: What is the difference between accessibility testing tools that run on code and those that run on the page?](#275-what-is-the-difference-between-accessibility-testing-tools-that-run-on-code-and-those-that-run-on-the-page)
- [276: How do you handle accessibility for third-party widgets?](#276-how-do-you-handle-accessibility-for-third-party-widgets)
- [277: What are skip links for besides "skip to main content"?](#277-what-are-skip-links-for-besides-skip-to-main-content)
- [278: How do you make a skip link visible on focus?](#278-how-do-you-make-a-skip-link-visible-on-focus)
- [279: How do you announce the number of characters left in a text area?](#279-how-do-you-announce-the-number-of-characters-left-in-a-text-area)
- [280: How do you make an accessible password field with a show password button?](#280-how-do-you-make-an-accessible-password-field-with-a-show-password-button)
- [281: How do you make a multi-step form accessible?](#281-how-do-you-make-a-multi-step-form-accessible)
- [282: How do you warn users about a session timeout?](#282-how-do-you-warn-users-about-a-session-timeout)
- [283: How do you make CAPTCHA-free spam protection?](#283-how-do-you-make-captcha-free-spam-protection)
- [284: Why should you allow paste in form fields?](#284-why-should-you-allow-paste-in-form-fields)
- [285: How do you make one-time codes easier for everyone?](#285-how-do-you-make-one-time-codes-easier-for-everyone)
- [286: Are passkeys good for accessibility?](#286-are-passkeys-good-for-accessibility)
- [287: How do you make inline editing (like click to edit) accessible?](#287-how-do-you-make-inline-editing-like-click-to-edit-accessible)
- [288: What accessibility problems do hover-only interactions cause?](#288-what-accessibility-problems-do-hover-only-interactions-cause)
- [289: How do you check a site at 400% zoom?](#289-how-do-you-check-a-site-at-400-zoom)
- [290: How do you test text spacing?](#290-how-do-you-test-text-spacing)
- [291: How do you simulate color blindness while designing?](#291-how-do-you-simulate-color-blindness-while-designing)
- [292: Should links be underlined?](#292-should-links-be-underlined)
- [293: How do you handle text over images?](#293-how-do-you-handle-text-over-images)
- [294: How do you announce changes in a shopping cart?](#294-how-do-you-announce-changes-in-a-shopping-cart)
- [295: How do you make a "back to top" button accessible?](#295-how-do-you-make-a-back-to-top-button-accessible)
- [296: What is the purpose of the aria-describedby on a dialog?](#296-what-is-the-purpose-of-the-aria-describedby-on-a-dialog)
- [297: How do you make a toolbar accessible?](#297-how-do-you-make-a-toolbar-accessible)
- [298: How do you make a tree view accessible?](#298-how-do-you-make-a-tree-view-accessible)
- [299: What should an accessibility statement include?](#299-what-should-an-accessibility-statement-include)
- [300: How do you explain the business case for accessibility to a manager?](#300-how-do-you-explain-the-business-case-for-accessibility-to-a-manager)

### Advanced Questions (301-450)

- [301: How does information get from your HTML to a screen reader?](#301-how-does-information-get-from-your-html-to-a-screen-reader)
- [302: What are the platform accessibility APIs?](#302-what-are-the-platform-accessibility-apis)
- [303: What are the Core-AAM and HTML-AAM specs?](#303-what-are-the-core-aam-and-html-aam-specs)
- [304: Why can the same page sound different in different screen readers?](#304-why-can-the-same-page-sound-different-in-different-screen-readers)
- [305: Which elements are left out of the accessibility tree?](#305-which-elements-are-left-out-of-the-accessibility-tree)
- [306: How does the accessible name computation work for an element with nested content?](#306-how-does-the-accessible-name-computation-work-for-an-element-with-nested-content)
- [307: Can aria-labelledby reference hidden elements?](#307-can-aria-labelledby-reference-hidden-elements)
- [308: Why doesn't aria-label work on a div or span?](#308-why-doesnt-aria-label-work-on-a-div-or-span)
- [309: Which roles cannot get their name from content?](#309-which-roles-cannot-get-their-name-from-content)
- [310: How is the accessible description computed?](#310-how-is-the-accessible-description-computed)
- [311: What is the difference between browse mode virtual buffers and the live DOM?](#311-what-is-the-difference-between-browse-mode-virtual-buffers-and-the-live-dom)
- [312: What does role="application" do and why is it risky?](#312-what-does-roleapplication-do-and-why-is-it-risky)
- [313: Roving tabindex versus aria-activedescendant: how do you choose?](#313-roving-tabindex-versus-aria-activedescendant-how-do-you-choose)
- [314: How do you build an accessible data grid?](#314-how-do-you-build-an-accessible-data-grid)
- [315: When should you use a table instead of role="grid"?](#315-when-should-you-use-a-table-instead-of-rolegrid)
- [316: How do you make a virtualized list accessible?](#316-how-do-you-make-a-virtualized-list-accessible)
- [317: What happens to focus when a focused element is removed from the DOM?](#317-what-happens-to-focus-when-a-focused-element-is-removed-from-the-dom)
- [318: How should focus be managed after deleting an item from a list?](#318-how-should-focus-be-managed-after-deleting-an-item-from-a-list)
- [319: How do React re-renders cause accessibility bugs?](#319-how-do-react-re-renders-cause-accessibility-bugs)
- [320: How can hydration in server-rendered apps hurt accessibility?](#320-how-can-hydration-in-server-rendered-apps-hurt-accessibility)
- [321: How do you make accessible notifications that don't interrupt too much?](#321-how-do-you-make-accessible-notifications-that-dont-interrupt-too-much)
- [322: Why do some live region announcements get lost?](#322-why-do-some-live-region-announcements-get-lost)
- [323: What is the ARIA ariaNotify API?](#323-what-is-the-aria-arianotify-api)
- [324: How does shadow DOM affect ARIA references?](#324-how-does-shadow-dom-affect-aria-references)
- [325: What is ARIA element reflection?](#325-what-is-aria-element-reflection)
- [326: What is the reference target proposal for shadow DOM?](#326-what-is-the-reference-target-proposal-for-shadow-dom)
- [327: How do you give a custom element a role without adding attributes to the host?](#327-how-do-you-give-a-custom-element-a-role-without-adding-attributes-to-the-host)
- [328: What are form-associated custom elements and why do they matter for accessibility?](#328-what-are-form-associated-custom-elements-and-why-do-they-matter-for-accessibility)
- [329: What does delegatesFocus do in shadow DOM?](#329-what-does-delegatesfocus-do-in-shadow-dom)
- [330: How do slots affect the accessibility tree?](#330-how-do-slots-affect-the-accessibility-tree)
- [331: How do you make a rich text editor accessible?](#331-how-do-you-make-a-rich-text-editor-accessible)
- [332: How do you handle the Tab key inside code editors and text areas?](#332-how-do-you-handle-the-tab-key-inside-code-editors-and-text-areas)
- [333: How do canvas-based apps like Flutter web or Google Docs handle accessibility?](#333-how-do-canvas-based-apps-like-flutter-web-or-google-docs-handle-accessibility)
- [334: How do you make a WebGL or game experience more accessible?](#334-how-do-you-make-a-webgl-or-game-experience-more-accessible)
- [335: How can you make data visualizations accessible beyond a data table?](#335-how-can-you-make-data-visualizations-accessible-beyond-a-data-table)
- [336: What is ARIA 1.3 and what does it add?](#336-what-is-aria-13-and-what-does-it-add)
- [337: What are aria-braillelabel and aria-brailleroledescription?](#337-what-are-aria-braillelabel-and-aria-brailleroledescription)
- [338: What is WCAG 3 and how is it different from WCAG 2?](#338-what-is-wcag-3-and-how-is-it-different-from-wcag-2)
- [339: Should you start following WCAG 3 now?](#339-should-you-start-following-wcag-3-now)
- [340: What is the current legal status of web accessibility under the ADA in the US?](#340-what-is-the-current-legal-status-of-web-accessibility-under-the-ada-in-the-us)
- [341: What does the European Accessibility Act mean for a developer building an online store?](#341-what-does-the-european-accessibility-act-mean-for-a-developer-building-an-online-store)
- [342: What is the difference between conformance and compliance?](#342-what-is-the-difference-between-conformance-and-compliance)
- [343: Why are accessibility overlays legally risky?](#343-why-are-accessibility-overlays-legally-risky)
- [344: How would you design an accessibility program for a large company?](#344-how-would-you-design-an-accessibility-program-for-a-large-company)
- [345: What does "shift left" mean for accessibility?](#345-what-does-shift-left-mean-for-accessibility)
- [346: How do you write accessibility acceptance criteria for a user story?](#346-how-do-you-write-accessibility-acceptance-criteria-for-a-user-story)
- [347: What accessibility metrics are useful to track?](#347-what-accessibility-metrics-are-useful-to-track)
- [348: Why should you test with disabled users and not only with tools?](#348-why-should-you-test-with-disabled-users-and-not-only-with-tools)
- [349: What are the limits of WCAG?](#349-what-are-the-limits-of-wcag)
- [350: How do you handle accessibility in a design system's component API?](#350-how-do-you-handle-accessibility-in-a-design-systems-component-api)
- [351: What are headless UI libraries and how do they help accessibility?](#351-what-are-headless-ui-libraries-and-how-do-they-help-accessibility)
- [352: What are the risks of using component libraries for accessibility?](#352-what-are-the-risks-of-using-component-libraries-for-accessibility)
- [353: How do you make an autocomplete with async results accessible?](#353-how-do-you-make-an-autocomplete-with-async-results-accessible)
- [354: What makes combobox implementation so hard?](#354-what-makes-combobox-implementation-so-hard)
- [355: How does iOS VoiceOver differ from desktop screen readers in interaction?](#355-how-does-ios-voiceover-differ-from-desktop-screen-readers-in-interaction)
- [356: How does TalkBack differ from VoiceOver?](#356-how-does-talkback-differ-from-voiceover)
- [357: How do you make a custom component work with mobile screen readers?](#357-how-do-you-make-a-custom-component-work-with-mobile-screen-readers)
- [358: Why should you avoid detecting screen readers?](#358-why-should-you-avoid-detecting-screen-readers)
- [359: How can user preference media queries be a privacy problem?](#359-how-can-user-preference-media-queries-be-a-privacy-problem)
- [360: How can accessibility features be abused for SEO or security attacks?](#360-how-can-accessibility-features-be-abused-for-seo-or-security-attacks)
- [361: What are the security concerns with accessibility services on mobile?](#361-what-are-the-security-concerns-with-accessibility-services-on-mobile)
- [362: How do performance problems affect accessibility?](#362-how-do-performance-problems-affect-accessibility)
- [363: How do layout shifts affect users with disabilities?](#363-how-do-layout-shifts-affect-users-with-disabilities)
- [364: What are the accessibility issues with internationalization?](#364-what-are-the-accessibility-issues-with-internationalization)
- [365: How do you handle aria-label translations?](#365-how-do-you-handle-aria-label-translations)
- [366: How do you check that a translated site stays accessible?](#366-how-do-you-check-that-a-translated-site-stays-accessible)
- [367: How do you make dynamic content changes accessible when there is no user action?](#367-how-do-you-make-dynamic-content-changes-accessible-when-there-is-no-user-action)
- [368: How do you design accessible chat interfaces?](#368-how-do-you-design-accessible-chat-interfaces)
- [369: How do you make streaming AI responses accessible?](#369-how-do-you-make-streaming-ai-responses-accessible)
- [370: What accessibility problems do cookie consent banners cause?](#370-what-accessibility-problems-do-cookie-consent-banners-cause)
- [371: How do sticky elements cause accessibility failures at zoom?](#371-how-do-sticky-elements-cause-accessibility-failures-at-zoom)
- [372: What is the problem with fixed-position chat widgets?](#372-what-is-the-problem-with-fixed-position-chat-widgets)
- [373: How do you test that focus is not obscured?](#373-how-do-you-test-that-focus-is-not-obscured)
- [374: What is the WCAG-EM methodology?](#374-what-is-the-wcag-em-methodology)
- [375: How do you pick a representative sample of pages for an audit?](#375-how-do-you-pick-a-representative-sample-of-pages-for-an-audit)
- [376: How do you test a single page app's states that automated scanners miss?](#376-how-do-you-test-a-single-page-apps-states-that-automated-scanners-miss)
- [377: What are Playwright ARIA snapshots?](#377-what-are-playwright-aria-snapshots)
- [378: Can you automate screen reader testing?](#378-can-you-automate-screen-reader-testing)
- [379: How do you handle axe false negatives and false positives?](#379-how-do-you-handle-axe-false-negatives-and-false-positives)
- [380: How do you deal with a large backlog of accessibility issues on a legacy site?](#380-how-do-you-deal-with-a-large-backlog-of-accessibility-issues-on-a-legacy-site)
- [381: Scenario: a user reports they can't complete checkout with a screen reader. How do you investigate?](#381-scenario-a-user-reports-they-cant-complete-checkout-with-a-screen-reader-how-do-you-investigate)
- [382: Scenario: focus disappears after closing a modal in your React app. What are possible causes?](#382-scenario-focus-disappears-after-closing-a-modal-in-your-react-app-what-are-possible-causes)
- [383: Scenario: a dropdown works with NVDA but not with VoiceOver on iOS. What do you check?](#383-scenario-a-dropdown-works-with-nvda-but-not-with-voiceover-on-ios-what-do-you-check)
- [384: Scenario: your design team wants light gray placeholder-style labels for a clean look. What do you say?](#384-scenario-your-design-team-wants-light-gray-placeholder-style-labels-for-a-clean-look-what-do-you-say)
- [385: Scenario: a product manager wants an overlay tool because it's cheaper than fixing the site. How do you respond?](#385-scenario-a-product-manager-wants-an-overlay-tool-because-its-cheaper-than-fixing-the-site-how-do-you-respond)
- [386: Scenario: a chart dashboard must be accessible. How do you approach it?](#386-scenario-a-chart-dashboard-must-be-accessible-how-do-you-approach-it)
- [387: Scenario: you must add a keyboard shortcut system to a web app. What accessibility rules apply?](#387-scenario-you-must-add-a-keyboard-shortcut-system-to-a-web-app-what-accessibility-rules-apply)
- [388: Scenario: an infinite feed must stay, but you need it to be accessible. What do you do?](#388-scenario-an-infinite-feed-must-stay-but-you-need-it-to-be-accessible-what-do-you-do)
- [389: Scenario: a form uses a third-party payment iframe. What can you control?](#389-scenario-a-form-uses-a-third-party-payment-iframe-what-can-you-control)
- [390: Scenario: users with dyslexia say your docs site is hard to read. What changes can help?](#390-scenario-users-with-dyslexia-say-your-docs-site-is-hard-to-read-what-changes-can-help)
- [391: How should error messages be written for cognitive accessibility?](#391-how-should-error-messages-be-written-for-cognitive-accessibility)
- [392: How do you reduce cognitive load in a complex form?](#392-how-do-you-reduce-cognitive-load-in-a-complex-form)
- [393: How do you make authentication flows accessible beyond passwords?](#393-how-do-you-make-authentication-flows-accessible-beyond-passwords)
- [394: How does WCAG apply to native mobile apps and hybrid apps?](#394-how-does-wcag-apply-to-native-mobile-apps-and-hybrid-apps)
- [395: How do you make emails accessible?](#395-how-do-you-make-emails-accessible)
- [396: What is the relationship between SEO and accessibility?](#396-what-is-the-relationship-between-seo-and-accessibility)
- [397: How do you handle the accessibility of dark patterns?](#397-how-do-you-handle-the-accessibility-of-dark-patterns)
- [398: What is the difference between accessible and inclusive for content writers?](#398-what-is-the-difference-between-accessible-and-inclusive-for-content-writers)
- [399: How do you make custom scrollable regions keyboard accessible?](#399-how-do-you-make-custom-scrollable-regions-keyboard-accessible)
- [400: How do you handle focus in a split view or master-detail layout?](#400-how-do-you-handle-focus-in-a-split-view-or-master-detail-layout)
- [401: How do you build an accessible command palette?](#401-how-do-you-build-an-accessible-command-palette)
- [402: How do you make notifications or badge counts accessible?](#402-how-do-you-make-notifications-or-badge-counts-accessible)
- [403: What problems does aria-label on links cause for translation and voice control?](#403-what-problems-does-aria-label-on-links-cause-for-translation-and-voice-control)
- [404: How do you test with forced colors mode without Windows?](#404-how-do-you-test-with-forced-colors-mode-without-windows)
- [405: How do SVG icons behave in forced colors mode?](#405-how-do-svg-icons-behave-in-forced-colors-mode)
- [406: What is the impact of custom focus styles that use only box-shadow?](#406-what-is-the-impact-of-custom-focus-styles-that-use-only-box-shadow)
- [407: How do you make a page accessible when it uses CSS to hide content responsively?](#407-how-do-you-make-a-page-accessible-when-it-uses-css-to-hide-content-responsively)
- [408: What is the "hamburger menu" accessibility checklist?](#408-what-is-the-hamburger-menu-accessibility-checklist)
- [409: How do you check reading order in complex CSS layouts?](#409-how-do-you-check-reading-order-in-complex-css-layouts)
- [410: What is the CSS reading-flow property?](#410-what-is-the-css-reading-flow-property)
- [411: How does the accessibility of a site change with client-side rendering only?](#411-how-does-the-accessibility-of-a-site-change-with-client-side-rendering-only)
- [412: How do you make a CSS-only interaction accessible?](#412-how-do-you-make-a-css-only-interaction-accessible)
- [413: How do you test accessibility of components in isolation versus in pages?](#413-how-do-you-test-accessibility-of-components-in-isolation-versus-in-pages)
- [414: What issues can come from duplicate ids?](#414-what-issues-can-come-from-duplicate-ids)
- [415: How do you approach accessibility for an e-commerce product filtering panel?](#415-how-do-you-approach-accessibility-for-an-e-commerce-product-filtering-panel)
- [416: How do you build an accessible rating component?](#416-how-do-you-build-an-accessible-rating-component)
- [417: How do you make a stepper or quantity input accessible?](#417-how-do-you-make-a-stepper-or-quantity-input-accessible)
- [418: How do you handle accessibility when content loads in a portal?](#418-how-do-you-handle-accessibility-when-content-loads-in-a-portal)
- [419: How do you make a dialog that opens another dialog accessible?](#419-how-do-you-make-a-dialog-that-opens-another-dialog-accessible)
- [420: How do you announce sorted, filtered or paged updates in a data table?](#420-how-do-you-announce-sorted-filtered-or-paged-updates-in-a-data-table)
- [421: What is aria-keyshortcuts?](#421-what-is-aria-keyshortcuts)
- [422: What do aria-setsize and aria-posinset do?](#422-what-do-aria-setsize-and-aria-posinset-do)
- [423: What does aria-details do?](#423-what-does-aria-details-do)
- [424: How do you choose between aria-describedby and aria-details?](#424-how-do-you-choose-between-aria-describedby-and-aria-details)
- [425: How should you handle hidden content that becomes visible on demand, like "read more"?](#425-how-should-you-handle-hidden-content-that-becomes-visible-on-demand-like-read-more)
- [426: What is the accessibility impact of lazy loading images?](#426-what-is-the-accessibility-impact-of-lazy-loading-images)
- [427: How do you make loading skeletons accessible?](#427-how-do-you-make-loading-skeletons-accessible)
- [428: How do you handle accessibility of animations used for meaning?](#428-how-do-you-handle-accessibility-of-animations-used-for-meaning)
- [429: What are the risks of auto-playing background videos?](#429-what-are-the-risks-of-auto-playing-background-videos)
- [430: How do you handle accessibility for content generated by users?](#430-how-do-you-handle-accessibility-for-content-generated-by-users)
- [431: Can AI write alt text for images?](#431-can-ai-write-alt-text-for-images)
- [432: How can AI tools help or hurt accessibility work?](#432-how-can-ai-tools-help-or-hurt-accessibility-work)
- [433: What is ATAG?](#433-what-is-atag)
- [434: What is UAAG?](#434-what-is-uaag)
- [435: How do accessibility requirements apply to internal tools?](#435-how-do-accessibility-requirements-apply-to-internal-tools)
- [436: How do you handle accessibility in procurement?](#436-how-do-you-handle-accessibility-in-procurement)
- [437: How do you judge a vendor's VPAT?](#437-how-do-you-judge-a-vendors-vpat)
- [438: How do you make accessibility work sustainable on a team?](#438-how-do-you-make-accessibility-work-sustainable-on-a-team)
- [439: What is the difference between ARIA roles in ARIA 1.2 and HTML-mapped roles like generic?](#439-what-is-the-difference-between-aria-roles-in-aria-12-and-html-mapped-roles-like-generic)
- [440: What does the ARIA in HTML spec define?](#440-what-does-the-aria-in-html-spec-define)
- [441: How do you handle hover cards that contain links, like user profile previews?](#441-how-do-you-handle-hover-cards-that-contain-links-like-user-profile-previews)
- [442: How do you handle autoplaying carousels with screen readers?](#442-how-do-you-handle-autoplaying-carousels-with-screen-readers)
- [443: How do you test that your site works with voice control?](#443-how-do-you-test-that-your-site-works-with-voice-control)
- [444: How do you support switch users in web apps?](#444-how-do-you-support-switch-users-in-web-apps)
- [445: What is the hardest accessibility problem you would expect in a modern SPA, and how would you solve it?](#445-what-is-the-hardest-accessibility-problem-you-would-expect-in-a-modern-spa-and-how-would-you-solve-it)
- [446: How would you design a shared announcer service for an app?](#446-how-would-you-design-a-shared-announcer-service-for-an-app)
- [447: How do you handle accessibility in micro-frontend architectures?](#447-how-do-you-handle-accessibility-in-micro-frontend-architectures)
- [448: How do you make sure accessibility doesn't regress after release?](#448-how-do-you-make-sure-accessibility-doesnt-regress-after-release)
- [449: What would you check first on a page you have never seen, with only five minutes?](#449-what-would-you-check-first-on-a-page-you-have-never-seen-with-only-five-minutes)
- [450: What does a senior engineer bring to accessibility beyond knowing WCAG?](#450-what-does-a-senior-engineer-bring-to-accessibility-beyond-knowing-wcag)

---

# Easy Questions (1-150)

## 1: What is web accessibility?

Web accessibility means building websites and apps that people with disabilities can use. That includes people who are blind, have low vision, are deaf, can't use a mouse, have trouble with memory or reading, and many others. In practice it means the content can be seen, heard, understood and operated in more than one way, for example with a keyboard, a screen reader or voice control.

## 2: Why is it called "a11y"?

"a11y" is a numeronym. It keeps the first letter "a" and the last letter "y" of "accessibility" and replaces the 11 letters in between with the number 11. Developers use it because it is short and easy to search for, the same way "i18n" stands for internationalization.

## 3: Why does web accessibility matter?

About one in six people in the world lives with some kind of disability, so an inaccessible site shuts out a big group of users. Accessibility is also a legal requirement in many countries, and lawsuits over inaccessible websites are common. On top of that, accessible sites tend to be easier for everyone to use, work better on mobile and are easier for search engines to understand.

## 4: Who benefits from accessible websites?

People with permanent disabilities benefit most, but they are not the only ones. Someone with a broken arm, someone holding a baby in one arm, someone reading a phone in bright sunlight or watching a video in a quiet office without headphones all gain from the same features. Older users with weaker eyesight and slower motor control benefit too.

## 5: What are the main types of disabilities you should think about when building for the web?

The usual groups are visual (blindness, low vision, color blindness), hearing (deafness, hard of hearing), motor (limited use of hands, tremors, paralysis), cognitive and learning (dyslexia, ADHD, memory problems) and seizure disorders (photosensitive epilepsy). Speech disabilities matter too, for example when a site depends on voice input. Each group needs different things, so good accessibility covers all of them.

## 6: What is the difference between permanent, temporary and situational disabilities?

A permanent disability lasts for life, like being born deaf. A temporary disability goes away, like a broken wrist or eyes dilated after an eye exam. A situational limit comes from the environment, like a loud train where you can't hear audio or bright sun on your screen. Microsoft's inclusive design toolkit uses this idea to show that features built for one group help many others.

## 7: What is WCAG?

WCAG stands for Web Content Accessibility Guidelines. It is the main standard for web accessibility and is published by the W3C's Web Accessibility Initiative (WAI). It lists testable rules called success criteria, grouped under guidelines, and most laws around the world point to it. The current version is WCAG 2.2, published in October 2023.

## 8: What versions of WCAG exist?

WCAG 1.0 came out in 1999, WCAG 2.0 in 2008, WCAG 2.1 in 2018 and WCAG 2.2 in 2023. Each 2.x version keeps the criteria of the one before it and adds new ones, so a site that meets 2.2 also meets 2.1 and 2.0 (with the exception of 4.1.1 Parsing, which 2.2 removed). WCAG 3 is a separate, still unfinished draft with a different structure.

## 9: What does POUR stand for?

POUR is the four principles WCAG is built on. Perceivable: users must be able to see or hear the content. Operable: users must be able to use the controls, for example with a keyboard. Understandable: content and behavior must make sense. Robust: content must work with different browsers and assistive technologies, now and in the future.

## 10: What are WCAG conformance levels?

WCAG has three levels: A, AA and AAA. Level A covers the most basic problems that block people completely. Level AA adds more criteria and is the level most laws and company policies require. Level AAA is the strictest and W3C itself says it is not realistic to require it for whole sites, because some content can't meet every AAA rule.

## 11: Which WCAG level should most websites aim for?

Most websites should aim for WCAG 2.2 Level AA. It is the target used by most laws, procurement rules and company policies, and it covers the problems that affect the most users. You can still use AAA criteria where they are easy to meet, such as larger target sizes or a higher contrast ratio for body text.

## 12: What is a success criterion in WCAG?

A success criterion is a single testable rule, for example "1.1.1 Non-text Content" or "1.4.3 Contrast (Minimum)". Each one has a number, a short name, a level (A, AA or AAA) and a clear pass or fail condition. Audits report problems against these numbers, so it helps to know the common ones.

## 13: What is assistive technology?

Assistive technology is any hardware or software that helps a person with a disability use a computer. On the web this includes screen readers, screen magnifiers, braille displays, voice control software, switch devices, eye tracking systems and alternative keyboards. Browser features like zoom and high contrast modes also work as assistive tools.

## 14: What is a screen reader?

A screen reader is software that reads the content of the screen out loud or sends it to a braille display. Blind users and many low-vision users depend on it. It does not "see" the page; it reads the accessibility tree that the browser builds from your HTML and ARIA, so the quality of your markup decides what the user hears.

## 15: Name some popular screen readers.

On Windows the main ones are NVDA (free and open source), JAWS (paid) and Narrator (built into Windows). On macOS and iOS there is VoiceOver, which is built in. On Android there is TalkBack, and on ChromeOS there is ChromeVox. Surveys from WebAIM show that JAWS, NVDA and VoiceOver are the most used.

## 16: How do you turn on VoiceOver on a Mac?

Press Command + F5, or on newer Macs with Touch ID hold Command and press the Touch ID button three times. You can also turn it on in System Settings under Accessibility. Most VoiceOver commands use the "VO" keys, which are Control + Option by default, for example VO + Right Arrow moves to the next item.

## 17: What is a braille display?

A braille display is a device with rows of small pins that move up and down to form braille characters. It shows one line of text at a time, taken from what the screen reader is reading. Deafblind users depend on it, and many blind users prefer it for reading code or long text.

## 18: What is screen magnification software?

Screen magnifiers enlarge part of the screen, often 2x to 20x or more, and follow the mouse pointer or the keyboard focus. Examples are ZoomText, Windows Magnifier and macOS Zoom. Users of magnifiers only see a small part of the page at a time, so content that appears far away from the control that triggered it can be easy to miss.

## 19: What is voice control software?

Voice control lets people use a computer by speaking commands, for example "click Submit" or "scroll down". Examples are Dragon, Windows Voice Access and Voice Control on macOS and iOS. It works best when the visible label of a control matches its accessible name, because users say what they see.

## 20: What are switch devices?

A switch is a simple button, often pressed with a hand, head, foot or by sipping and puffing on a tube. Software scans through the items on screen one at a time and the user presses the switch to choose the highlighted one. Switch users need a clear, logical focus order and controls that work without precise pointer movement.

## 21: What is semantic HTML?

Semantic HTML means using elements for their meaning, not their look. For example, use `<button>` for buttons, `<nav>` for navigation, `<h2>` for a section heading and `<ul>` for a list. Browsers turn these elements into roles in the accessibility tree, so screen readers can tell users "button", "navigation" or "heading level 2" without any extra work.

```html
<!-- Bad -->
<div class="btn" onclick="save()">Save</div>

<!-- Good -->
<button type="button" onclick="save()">Save</button>
```

## 22: Why is a div with a click handler not a real button?

A `<div>` has no role, can't get keyboard focus and doesn't react to Enter or Space. A screen reader user won't know it is clickable, and a keyboard user can't reach it. A `<button>` gives you all of that for free: the button role, focus, keyboard activation, disabled state and form submission.

## 23: When should you use a link and when should you use a button?

Use a link (`<a href>`) when the action takes the user somewhere: another page, another part of the page or a file. Use a button when the action does something on the current page: submit a form, open a dialog, toggle a menu. Screen reader users rely on this difference, and links and buttons also respond to different keys (links to Enter, buttons to Enter and Space).

## 24: What is alt text?

Alt text is the text alternative for an image, written in the `alt` attribute of `<img>`. Screen readers read it instead of the image, and browsers show it when the image fails to load. It should describe what the image means in its context, not just what it looks like.

```html
<img src="chart.png" alt="Sales grew 40% from January to June" />
```

## 25: How do you write good alt text?

Describe the purpose of the image in the place it is used, and keep it short, usually one sentence. Don't start with "image of" or "picture of", because the screen reader already says it is an image. If the image is a link or a button, describe where it goes or what it does, not the picture itself.

## 26: When should alt text be empty?

Use an empty `alt=""` when the image is purely decorative or when the same information is already in nearby text. An empty alt tells screen readers to skip the image. Never leave out the `alt` attribute completely, because then many screen readers read the file name instead, like "IMG underscore 2041 dot jpg".

```html
<img src="divider-wave.svg" alt="" />
```

## 27: What is the difference between alt="" and no alt attribute?

`alt=""` means "this image is decorative, ignore it", and the image is removed from the accessibility tree. A missing `alt` means the author forgot, so screen readers try to guess and often read the file name or URL. Automated tools flag a missing alt as an error but accept an empty one.

## 28: What is WCAG 1.1.1 Non-text Content?

It is a Level A rule that says all non-text content, like images, icons, charts and image buttons, must have a text alternative that serves the same purpose. Decorative images must be hidden from assistive technology. It is one of the most commonly failed criteria, usually because of missing alt text.

## 29: How should you handle images that contain text?

Avoid putting text in images when you can, because it doesn't scale well, can't be restyled and is hard to translate. WCAG 1.4.5 Images of Text (Level AA) asks you to use real text instead, except for logos and cases where the exact look matters. If you must use an image of text, the alt text should contain the same words.

## 30: What is the purpose of headings for accessibility?

Headings give a page structure, and screen reader users use them to jump around, much like sighted users scan a page. In NVDA and JAWS, pressing H moves to the next heading, and pressing 1 to 6 jumps to a heading of that level. Good headings make long pages fast to navigate.

## 31: Is it okay to skip heading levels?

WCAG doesn't directly ban it, but it is a bad practice. Going from `<h2>` to `<h4>` makes users think they missed a section. Pick heading levels based on the outline of the content, then style them however you like with CSS. A heading level should never be picked just for its default font size.

## 32: How many h1 elements should a page have?

The common advice is one `<h1>` per page, describing the main topic, usually the same as or close to the page title. HTML allows more, but screen reader users expect the `<h1>` to tell them where they are. The old "document outline" idea, where `<h1>` inside `<section>` would become a lower level, was never implemented by browsers and has been removed from the HTML spec.

## 33: What are landmarks?

Landmarks are regions of a page with a known purpose, like the header, navigation, main content and footer. Screen readers can list them and jump between them, for example with the D key in NVDA or the rotor in VoiceOver. HTML elements create landmarks automatically.

| HTML element                      | Landmark role   |
| --------------------------------- | --------------- |
| `<header>` (not inside a section) | `banner`        |
| `<nav>`                           | `navigation`    |
| `<main>`                          | `main`          |
| `<aside>`                         | `complementary` |
| `<footer>` (not inside a section) | `contentinfo`   |
| `<form>` with a name              | `form`          |
| `<section>` with a name           | `region`        |
| `<search>`                        | `search`        |

## 34: How many main elements should a page have?

Only one visible `<main>` element per page. It should wrap the primary content, not the header, navigation or footer. This lets users jump straight to the content with one keystroke and is also the target for "skip to main content" links.

## 35: What is the lang attribute and why does it matter?

The `lang` attribute on `<html>` tells the browser and screen readers which language the page is in. Screen readers use it to pick the right voice and pronunciation. Without it, a French page might be read with English pronunciation and be hard to understand. It is required by WCAG 3.1.1 Language of Page (Level A).

```html
<html lang="en"></html>
```

## 36: How do you mark a phrase in a different language?

Put a `lang` attribute on the element that wraps the phrase. This lets screen readers switch voices for just that part. It is covered by WCAG 3.1.2 Language of Parts (Level AA).

```html
<p>The French call it <span lang="fr">joie de vivre</span>.</p>
```

## 37: Why is the page title important for accessibility?

The `<title>` is the first thing a screen reader announces when a page loads, and it is what appears in tabs, bookmarks and history. It should say what the page is, for example "Cart - My Shop". WCAG 2.4.2 Page Titled (Level A) requires a descriptive title on every page.

## 38: What is keyboard accessibility?

Keyboard accessibility means every feature of the site can be used with a keyboard alone, without a mouse. Many people can't use a mouse: blind users, people with tremors and people who use switch devices or voice control, which act like a keyboard. WCAG 2.1.1 Keyboard (Level A) requires it.

## 39: Which keys do keyboard users rely on?

Tab moves focus forward and Shift + Tab moves it back. Enter activates links and buttons, and Space activates buttons, checkboxes and toggles. Arrow keys move inside groups like radio buttons, menus, tabs and sliders. Escape closes dialogs, menus and popups.

## 40: What is keyboard focus?

Focus is the element that will receive keyboard input right now. Only one element on the page has focus at a time. Links, buttons and form fields can get focus by default, and you can check the focused element in JavaScript with `document.activeElement`.

## 41: What is a focus indicator?

A focus indicator is the visible sign of which element has focus, usually an outline or ring. Keyboard users need it the same way mouse users need a pointer. WCAG 2.4.7 Focus Visible (Level AA) requires that keyboard focus is always visible.

## 42: Why should you never remove the focus outline without replacing it?

Code like `*:focus { outline: none; }` makes keyboard users lose track of where they are on the page. If designers don't like the default outline, style a better one instead of removing it. The `:focus-visible` pseudo-class lets you show it for keyboard users without showing it on every mouse click.

```css
button:focus-visible {
  outline: 3px solid #1a73e8;
  outline-offset: 2px;
}
```

## 43: What is a skip link?

A skip link is a link at the very top of the page that jumps to the main content. Without it, keyboard users have to tab through the whole header and menu on every page. It is usually hidden until it gets focus. It helps meet WCAG 2.4.1 Bypass Blocks (Level A).

```html
<a class="skip-link" href="#main">Skip to main content</a>
...
<main id="main">...</main>
```

## 44: What does tabindex do?

`tabindex` controls whether an element can get focus and whether it is in the tab order. `tabindex="0"` adds an element to the normal tab order, in DOM order. `tabindex="-1"` makes it focusable with JavaScript (`element.focus()`) but leaves it out of the tab order. A positive value forces the element ahead of everything else in the tab order.

## 45: Why should you avoid positive tabindex values?

A positive value like `tabindex="3"` moves the element ahead of all elements with `0` or no tabindex, which breaks the natural order of the page. It quickly becomes impossible to maintain as the page changes. Fix the DOM order instead, so the tab order follows the visual order.

## 46: What is tab order and how is it decided?

Tab order is the order in which elements get focus when the user presses Tab. By default it follows the order of elements in the DOM, not their position on screen. That is why the DOM order should match the visual reading order. WCAG 2.4.3 Focus Order (Level A) requires a logical order.

## 47: What is a keyboard trap?

A keyboard trap is when focus gets into a component and the user can't move out of it with the keyboard. Old embedded players and some custom widgets cause this. WCAG 2.1.2 No Keyboard Trap (Level A) bans it. Note that a modal dialog deliberately keeps focus inside, but it is still fine because Escape or a close button lets the user leave.

## 48: What is color contrast?

Color contrast is the difference in brightness between text (or an important graphic) and its background. Low contrast text, like light gray on white, is hard to read for people with low vision, for older users and for anyone in bright light. WCAG measures it as a ratio from 1:1 (no contrast) to 21:1 (black on white).

## 49: What contrast ratios does WCAG require?

WCAG 1.4.3 (Level AA) requires 4.5:1 for normal text and 3:1 for large text. Large text means at least 24 CSS pixels, or 18.66 CSS pixels if bold. WCAG 1.4.6 (Level AAA) raises this to 7:1 and 4.5:1. WCAG 1.4.11 (Level AA) requires 3:1 for icons, input borders and focus indicators that people need to see.

## 50: Can you use color alone to show information?

No. WCAG 1.4.1 Use of Color (Level A) says color can't be the only way to show meaning. For example, a form field with an error should not only turn red; it should also show an error message or an icon. People who are color blind or using a monochrome screen would otherwise miss it.

## 51: What is color blindness and how common is it?

Color blindness, or color vision deficiency, means a person can't tell some colors apart. The most common type is red-green, and it affects about 1 in 12 men and 1 in 200 women. This is why red and green alone are a bad way to show "error" and "success".

## 52: How can you check color contrast?

You can use the contrast checker in Chrome DevTools (open the color picker of a text color), the WebAIM Contrast Checker website, the TPGi Colour Contrast Analyser desktop app or browser extensions like axe DevTools. Design tools like Figma have contrast plugins too. Check contrast during design, not only after the page is built.

## 53: What are form labels and why are they needed?

A label is the visible text that tells users what to type in a field. It must be connected to the field in code so screen readers announce it when the field gets focus. A connected label also makes the click area bigger, because clicking the label focuses the field.

```html
<label for="email">Email</label> <input id="email" type="email" />
```

## 54: Why is a placeholder not a replacement for a label?

Placeholder text disappears as soon as the user starts typing, so people with memory problems lose the hint. It usually has low contrast and some screen readers don't read it reliably. Always use a real `<label>`, and use the placeholder only for an optional example, if at all.

## 55: What are fieldset and legend used for?

`<fieldset>` groups related form controls, and `<legend>` gives the group a name. Screen readers read the legend when focus enters the group. They are most useful for radio buttons and checkboxes, where each option's label alone doesn't make sense without the question.

```html
<fieldset>
  <legend>Shipping method</legend>
  <label><input type="radio" name="ship" value="std" /> Standard</label>
  <label><input type="radio" name="ship" value="exp" /> Express</label>
</fieldset>
```

## 56: How do you mark a field as required in an accessible way?

Use the HTML `required` attribute, which screen readers announce as "required" and which browsers use for validation. Also show it visually, for example with the word "required" or an asterisk explained at the top of the form. Don't rely on color alone to mark required fields.

```html
<label for="name">Name (required)</label> <input id="name" required />
```

## 57: How should form error messages be shown?

Show the error as text near the field, say what went wrong and how to fix it, and connect the message to the field with `aria-describedby`. Mark the field with `aria-invalid="true"`. WCAG 3.3.1 Error Identification (Level A) and 3.3.3 Error Suggestion (Level AA) cover this.

```html
<label for="zip">ZIP code</label>
<input id="zip" aria-invalid="true" aria-describedby="zip-error" />
<p id="zip-error">ZIP code must be 5 digits.</p>
```

## 58: What does the autocomplete attribute have to do with accessibility?

The `autocomplete` attribute tells the browser what kind of data a field expects, like `email`, `given-name` or `street-address`. The browser can then fill it in for the user, which saves a lot of effort for people with motor or memory problems. WCAG 1.3.5 Identify Input Purpose (Level AA) requires it on fields that collect personal data about the user.

```html
<input id="email" type="email" autocomplete="email" />
```

## 59: Why should you use the correct input type?

Types like `email`, `tel`, `number`, `url` and `date` give mobile users the right keyboard, give browsers built-in validation and tell assistive technology more about the field. For example, `type="tel"` shows a number pad on phones. It makes forms faster and less error-prone for everyone.

## 60: What is ARIA?

WAI-ARIA (Accessible Rich Internet Applications) is a W3C standard that adds attributes to HTML to describe roles, states and properties to assistive technology. It is used when HTML doesn't have a native element for a widget, such as tabs or a tree view. ARIA only changes what assistive technology is told; it doesn't add any behavior like focus or keyboard support.

## 61: What is the first rule of ARIA?

The first rule of ARIA is: if a native HTML element already has the meaning and behavior you need, use it instead of adding ARIA to a different element. For example, use `<button>` instead of `<div role="button">`. Native elements come with keyboard support, focus and state handling that you would otherwise have to build by hand.

## 62: What does "no ARIA is better than bad ARIA" mean?

It means wrong ARIA can make a page worse than having no ARIA at all. A wrong role can tell a screen reader user that something is a menu or a tab when it doesn't behave like one, so their usual keys stop working. WebAIM's yearly "Million" report keeps finding that pages using ARIA have more detected errors than pages without it, mostly because it is used badly.

## 63: What are ARIA roles, states and properties?

A role says what an element is, like `role="tab"` or `role="dialog"`. A state is something that changes often during use, like `aria-expanded="true"` or `aria-checked="false"`. A property is a more stable feature, like `aria-labelledby` or `aria-controls`. Together they tell assistive technology what the element is and what condition it is in.

## 64: What does aria-label do?

`aria-label` gives an element an accessible name as a string. It is useful when there is no visible text, like an icon-only button. It overrides the element's own text content, and it is not shown on screen, so prefer visible text when possible.

```html
<button type="button" aria-label="Close">
  <svg aria-hidden="true">...</svg>
</button>
```

## 65: What does aria-labelledby do?

`aria-labelledby` names an element using the text of one or more other elements, referenced by their `id`. It takes priority over `aria-label` and the element's own content. It is useful when a visible heading already labels a section or a dialog.

```html
<div role="dialog" aria-labelledby="dlg-title">
  <h2 id="dlg-title">Delete file?</h2>
</div>
```

## 66: What does aria-describedby do?

`aria-describedby` points to other elements that give extra information, like a hint or an error message. Screen readers usually read the description after the name and role, sometimes after a short pause. Use it for help text that is useful but is not the name of the control.

```html
<input id="pw" type="password" aria-describedby="pw-hint" />
<p id="pw-hint">At least 12 characters.</p>
```

## 67: What does aria-hidden="true" do?

It removes an element and all its children from the accessibility tree, so screen readers ignore it. The element stays visible on screen. Use it for decorative icons or duplicate content. Never put it on an element that can receive focus, because keyboard users would land on something the screen reader can't describe.

## 68: What is the accessibility tree?

The accessibility tree is a structure the browser builds from the DOM, and it contains only the information assistive technology needs. Each node has a role, a name, a state and some properties. Screen readers read this tree through the operating system's accessibility API, not the DOM itself. You can inspect it in the Accessibility pane of Chrome or Firefox DevTools.

## 69: What is an accessible name?

The accessible name is the label that assistive technology announces for an element, like "Submit" for a button or "Email" for an input. It comes from, in order of priority, `aria-labelledby`, `aria-label`, native labeling (like `<label>` or `alt`), the element's content, and finally `title`. Every interactive element needs one.

## 70: What does WCAG 4.1.2 Name, Role, Value mean?

It is a Level A rule saying every user interface component must expose its name, its role and its current state or value to assistive technology. For a checkbox, that means the label, the fact it is a checkbox and whether it is checked. Native HTML elements do this automatically; custom widgets have to use ARIA to do it.

## 71: How do you make a data table accessible?

Use real `<table>` markup with `<th>` for header cells and a `<caption>` for the title. For simple tables, add `scope="col"` or `scope="row"` to headers. Screen readers then announce the matching header when the user moves between cells, so they know what each number means.

```html
<table>
  <caption>
    Monthly sales
  </caption>
  <tr>
    <th scope="col">Month</th>
    <th scope="col">Sales</th>
  </tr>
  <tr>
    <th scope="row">January</th>
    <td>$4,000</td>
  </tr>
</table>
```

## 72: Should you use tables for page layout?

No. Layout tables confuse screen readers, which may announce rows and columns that have no meaning. Use CSS grid or flexbox for layout. If an old system forces a layout table, add `role="presentation"` so the table semantics are removed.

## 73: Why should lists use ul, ol or dl?

Screen readers announce lists and the number of items, like "list, 5 items", so users know what to expect and can skip the whole list. Fake lists made with `<div>` and line breaks lose that information. Use `<ul>` for unordered items, `<ol>` for steps or rankings and `<dl>` for terms and descriptions.

## 74: What are captions?

Captions are text versions of the speech and important sounds in a video, shown in sync with it. They are essential for deaf and hard of hearing users, and many hearing people use them in noisy or quiet places. WCAG 1.2.2 (Level A) requires captions for prerecorded video, and 1.2.4 (Level AA) requires them for live video.

## 75: What is the difference between captions and subtitles?

Captions are for people who can't hear the audio, so they include speech plus sound effects and speaker names, like "[door slams]". Subtitles usually just translate the speech into another language for people who can hear but don't understand it. In the US the words are used differently than in the UK, so define what you mean in specs.

## 76: What is a transcript?

A transcript is a text version of all the audio content, and for video, also the important visual content. It helps deafblind users who use braille, people who prefer reading and people who want to search the content. WCAG 1.2.1 (Level A) requires a transcript for audio-only content like podcasts.

## 77: What is audio description?

Audio description is an extra narration track that describes important visual information in a video, like actions, scene changes and on-screen text, for blind users. It fills the gaps between dialogue. WCAG 1.2.5 (Level AA) requires it for prerecorded video when the visuals carry information that isn't in the audio.

## 78: Why is autoplaying audio a problem?

Autoplaying audio talks over the screen reader, so a blind user can't hear their screen reader to find the pause button. It is also distracting for people with attention problems. WCAG 1.4.2 Audio Control (Level A) requires a way to pause or stop any audio that plays for more than 3 seconds, or a way to control its volume separately.

## 79: What is WCAG 2.3.1 Three Flashes or Below Threshold?

It is a Level A rule that bans content that flashes more than three times in any one second, unless the flash is small and dim enough to stay below the limits WCAG defines. Flashing content can cause seizures in people with photosensitive epilepsy. This rule protects people from real physical harm, so treat it as a hard rule.

## 80: What does prefers-reduced-motion do?

It is a CSS media query that checks whether the user has asked the operating system to reduce motion. Some people get dizzy or sick from animations like parallax and big slide effects. You can use it to turn off or tone down animations for them.

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

## 81: What is the visually hidden or sr-only class?

It is a CSS pattern that hides content visually but keeps it in the accessibility tree, so screen readers still read it. It is used for extra context like "(opens in new tab)" or a heading that sighted users don't need. Don't use `display: none` for this, because that hides it from everyone.

```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```

## 82: What is the difference between display none, visibility hidden and the sr-only class?

`display: none` and `visibility: hidden` hide content from everyone, including screen readers, and the content can't get focus. The sr-only class hides content only visually; screen readers still read it. `opacity: 0` hides it visually but keeps it in the tree and focusable, which often causes confusing "invisible" focus stops.

## 83: What does the hidden attribute do?

The HTML `hidden` attribute hides an element from everyone, the same as `display: none` by default. It is a clean way to hide panels or messages until they are needed. Note that a CSS rule like `display: block` on the same element will override it, so watch your styles. `hidden="until-found"` is a newer value that keeps content findable with the browser's find-in-page.

## 84: Do iframes need a title?

Yes. An `<iframe>` should have a `title` attribute that describes its content, like `title="Store location map"`. Screen readers announce it when the user reaches the frame, which helps them decide whether to go in. Without it, they hear something useless like the URL.

## 85: How do you make an icon button accessible?

Give the button an accessible name and hide the icon itself from assistive technology. You can use `aria-label` on the button or visually hidden text inside it. A tooltip helps sighted users too, but it isn't enough on its own.

```html
<button type="button">
  <svg aria-hidden="true" focusable="false"><use href="#icon-trash" /></svg>
  <span class="sr-only">Delete</span>
</button>
```

## 86: Why should link text make sense on its own?

Screen reader users often pull up a list of all links on a page, and they hear only the link text without the paragraph around it. A list full of "click here" and "read more" is useless. Write links like "Read the pricing guide" instead. WCAG 2.4.4 Link Purpose (In Context) (Level A) covers this.

## 87: What are some quick ways to test a site for accessibility?

Unplug the mouse and try to use the site with only the keyboard. Zoom the browser to 200% and 400% and check that nothing breaks. Run an automated checker like axe DevTools, WAVE or Lighthouse. Finally, try a screen reader on a few key pages, like the home page, a form and checkout.

## 88: What is Lighthouse's accessibility score?

Lighthouse, built into Chrome DevTools, runs a set of axe-core checks and gives a score from 0 to 100. It is a quick health check, but a score of 100 doesn't mean the page is accessible. It only checks things a machine can detect, so a lot of real problems are still possible.

## 89: What is axe?

axe is an accessibility testing engine made by Deque, and its open source core is axe-core. It powers the axe DevTools browser extension, Lighthouse's accessibility checks and many test libraries like jest-axe and @axe-core/playwright. It is popular because it aims for zero false positives, so what it reports is almost always a real issue.

## 90: What is WAVE?

WAVE is a free accessibility checker from WebAIM, available as a website and a browser extension. It shows icons directly on the page for errors, alerts, structure and ARIA, which makes it easy to see where problems are. It is good for quick visual reviews and for teaching people about accessibility.

## 91: How much can automated testing find?

Automated tools usually catch around 30 to 50 percent of WCAG issues, depending on how you count. They can find missing alt text, low contrast and missing labels, but they can't tell if alt text is accurate, if the focus order makes sense or if a custom widget works with a keyboard. Manual testing is always needed.

## 92: What is manual accessibility testing?

Manual testing is checking things a tool can't, by hand. Typical steps are keyboard-only use, screen reader testing, checking zoom and reflow, reviewing alt text and labels for meaning, checking headings and reading order, and testing with high contrast or forced colors modes. Testers often work through a WCAG checklist.

## 93: Which laws require web accessibility?

In the US, the ADA (Americans with Disabilities Act) is used in lawsuits against businesses, and Section 508 covers federal agencies. In the EU, the Web Accessibility Directive covers public sector sites and the European Accessibility Act covers many private products and services. Canada, the UK, Australia, Israel and many other countries have their own laws, and most of them point to WCAG.

## 94: What is Section 508?

Section 508 is part of the US Rehabilitation Act. It requires federal agencies to make their information and communication technology accessible, including websites, documents and software they buy. Since the 2017 refresh, it uses WCAG 2.0 Level AA as its technical standard. Vendors who sell to the US government often have to show they meet it.

## 95: What is the European Accessibility Act?

The European Accessibility Act (EAA) is an EU directive that requires many products and services to be accessible, including e-commerce sites, banking, e-books, transport ticketing and phones. Its rules apply to new products and services since June 28, 2025. In practice it uses the EN 301 549 standard, which includes WCAG 2.1 AA for web content. Microenterprises that provide services are exempt.

## 96: What is EN 301 549?

EN 301 549 is the European standard for accessibility of information and communication technology. It covers websites, software, documents and hardware. For web content, it includes the WCAG 2.1 Level A and AA criteria, and EU laws point to it to define what "accessible" means.

## 97: What is a VPAT or ACR?

A VPAT (Voluntary Product Accessibility Template) is a template from the Information Technology Industry Council for documenting how a product meets accessibility standards. Once filled in, it is called an ACR (Accessibility Conformance Report). Buyers, especially governments and universities, often ask for one before purchasing software.

## 98: What are accessibility overlays and why are they criticized?

Overlays are third-party scripts that add a toolbar or claim to fix accessibility automatically with AI. They can't fix the underlying code, they often conflict with the user's own assistive technology, and sites using them still get sued. In 2025 the US FTC fined overlay maker accessiBe $1 million for misleading claims. Fixing the actual code is the only real solution.

## 99: What is the curb cut effect?

The curb cut effect is the idea that features made for people with disabilities end up helping everyone. Curb cuts in sidewalks were made for wheelchair users but also help people with strollers, suitcases and bikes. On the web, captions, good contrast and keyboard shortcuts are common examples.

## 100: What is inclusive design?

Inclusive design is designing products that work for as many people as possible, including people with disabilities, older people and people in hard situations. It starts with understanding who gets left out and involving them in the design process. Accessibility is a big part of it, but inclusive design also covers things like language, culture and device limits.

## 101: What is the difference between accessibility and usability?

Accessibility is about whether people with disabilities can use something at all. Usability is about how easy and pleasant it is for anyone to use. A page can be technically accessible but still very hard to use with a screen reader. Good work aims for both: usable by everyone, including disabled users.

## 102: What does WCAG 1.4.4 Resize Text require?

It is a Level AA rule saying text must be able to grow to 200% without losing content or functions. Users should be able to zoom the browser or raise the default font size and still read and use everything. Using relative units like `rem` and avoiding fixed heights on text containers helps.

## 103: What is reflow in WCAG?

WCAG 1.4.10 Reflow (Level AA) says content must work at a width of 320 CSS pixels without scrolling in two directions. That equals a 1280-pixel wide screen zoomed to 400%. Responsive layouts that stack into one column usually pass. Data tables, maps and some diagrams are allowed to scroll sideways.

## 104: Why should you never disable zoom on mobile?

`<meta name="viewport" content="user-scalable=no">` or `maximum-scale=1` stops users from pinching to zoom. People with low vision depend on zoom to read. Modern iOS Safari ignores these settings, but other browsers may respect them, so just leave them out.

```html
<meta name="viewport" content="width=device-width, initial-scale=1" />
```

## 105: Why use rem or em instead of px for font sizes?

`rem` and `em` scale with the user's browser font size setting, while `px` font sizes in many cases ignore it. Someone who sets their default font to 24px will get bigger text on a `rem`-based site. Browser zoom works with both, but respecting the font setting is a better experience for many low-vision users.

## 106: What is WCAG 1.4.12 Text Spacing?

It is a Level AA rule saying content must still work when users change text spacing to: line height 1.5 times the font size, paragraph spacing 2 times, letter spacing 0.12 times and word spacing 0.16 times. People with dyslexia often use tools that do this. Fixed-height boxes that cut off text are the usual failure.

## 107: What is the minimum target size in WCAG 2.2?

WCAG 2.5.8 Target Size (Minimum) is a new Level AA rule in 2.2. It requires clickable targets to be at least 24 by 24 CSS pixels, or to have enough space around them so a 24-pixel circle around each one doesn't overlap another target. Inline links in text and controls whose size is set by the browser are exceptions. The AAA rule 2.5.5 asks for 44 by 44 pixels.

## 108: What did WCAG 2.2 add?

WCAG 2.2 added nine new success criteria: 2.4.11 Focus Not Obscured (Minimum), 2.4.12 Focus Not Obscured (Enhanced), 2.4.13 Focus Appearance, 2.5.7 Dragging Movements, 2.5.8 Target Size (Minimum), 3.2.6 Consistent Help, 3.3.7 Redundant Entry, 3.3.8 Accessible Authentication (Minimum) and 3.3.9 Accessible Authentication (Enhanced). It also removed 4.1.1 Parsing, because modern browsers and assistive technology handle broken HTML the same way.

## 109: What is WCAG 2.4.11 Focus Not Obscured?

It is a Level AA rule in WCAG 2.2. It says when an element gets keyboard focus, it must not be completely hidden by other content the author added, like a sticky header, a cookie banner or a chat widget. The AAA version, 2.4.12, says no part of it may be hidden.

## 110: What is WCAG 2.5.7 Dragging Movements?

It is a Level AA rule in WCAG 2.2. Any action done by dragging, like reordering a list or moving a slider thumb, must also be possible with a single pointer action without dragging, like clicking up and down buttons. People with tremors or who use a head pointer often can't hold and drag.

## 111: What is WCAG 3.3.7 Redundant Entry?

It is a Level A rule in WCAG 2.2. Information the user already entered in the same process should be filled in for them or be available to select, instead of asking them to type it again. A common example is a "same as shipping address" checkbox. Exceptions are when re-entry is needed for security, like confirming a password.

## 112: What is WCAG 3.3.8 Accessible Authentication?

It is a Level AA rule in WCAG 2.2. Logging in must not depend on a cognitive function test, like remembering a password or solving a puzzle, unless there is another way or help is given. Allowing password managers and paste, offering passkeys or email login links, and using object-recognition CAPTCHAs are ways to pass.

## 113: What is WCAG 3.2.6 Consistent Help?

It is a Level A rule in WCAG 2.2. If a site offers help, like a contact link, phone number or chat, it should appear in the same relative place on every page. People with cognitive disabilities can then find help without searching each page again.

## 114: What is CAPTCHA and why is it an accessibility problem?

CAPTCHA is a test meant to tell humans and bots apart, like typing distorted letters or picking images with traffic lights. Blind users can't see visual puzzles, and audio versions are often hard to understand. Better options are invisible checks like Cloudflare Turnstile or reCAPTCHA v3, honeypot fields and rate limiting.

## 115: What are time limits in WCAG?

WCAG 2.2.1 Timing Adjustable (Level A) says if content has a time limit, users must be able to turn it off, change it or extend it at least ten times, with a warning before it runs out. People who read slowly or use assistive technology need more time. Real-time events like auctions are exceptions.

## 116: What is WCAG 2.2.2 Pause, Stop, Hide?

It is a Level A rule saying moving, blinking or scrolling content that starts automatically and lasts more than 5 seconds must have a way to pause, stop or hide it. Auto-rotating carousels, news tickers and animated backgrounds are common examples. Moving content distracts people with attention problems and makes it hard for screen magnifier users to read.

## 117: What is the forced colors mode?

Forced colors mode, such as Windows Contrast Themes (formerly High Contrast Mode), replaces the site's colors with a small palette the user picked. People with low vision or light sensitivity use it. Background images and box shadows may disappear, so things like focus rings made only with `box-shadow` can vanish. You can detect it with the `forced-colors: active` media query.

## 118: What is the difference between dark mode and high contrast?

Dark mode is a color theme with light text on a dark background, mainly for comfort and battery life. High contrast or forced colors modes change colors to maximize readability for people with low vision. You can support dark mode with `prefers-color-scheme`, but it must still meet contrast ratios, which is often missed for dark gray text.

## 119: What are browse mode and focus mode in screen readers?

In browse mode (also called virtual cursor or reading mode), the screen reader catches the keys and uses them to move through content, like H for headings or arrow keys line by line. In focus mode (also called forms mode), keys go straight to the page, so users can type into fields. Screen readers switch automatically when users enter form fields or certain widgets.

## 120: How do screen reader users usually navigate a page?

Most screen reader users first jump by headings to get an overview, according to WebAIM's surveys. They also use landmarks, link lists, form field lists and in-page search. Few of them read a page from top to bottom. That is why headings, landmarks and good link text have such a big effect.

## 121: What is the reading order and why does it matter?

The reading order is the order screen readers read content, and it follows the DOM order. If CSS moves things visually, like with `order`, `flex-direction: row-reverse` or grid placement, the visual order and reading order can stop matching. WCAG 1.3.2 Meaningful Sequence (Level A) requires a reading order that keeps the meaning correct.

## 122: Should a button have a type attribute?

Yes. A `<button>` inside a form defaults to `type="submit"`, so a button meant to open a menu could submit the form by accident. Always write `type="button"` for non-submit buttons. This isn't a pure accessibility rule, but it avoids surprising behavior for all users.

## 123: What is the problem with disabled buttons?

Disabled buttons are skipped in the tab order and usually have low contrast, so users may not know they exist or why they can't use them. Contrast rules don't apply to disabled controls, but users still need to understand what's missing. Often it is better to keep the button enabled and show clear error messages when it is clicked.

## 124: What do details and summary do for accessibility?

`<details>` and `<summary>` give you a native disclosure widget that opens and closes content. The summary is focusable, works with Enter and Space, and screen readers announce whether it is expanded or collapsed. It is a good choice for FAQs and "show more" sections without any JavaScript.

```html
<details>
  <summary>Shipping costs</summary>
  <p>Shipping is free on orders over $50.</p>
</details>
```

## 125: What is the dialog element?

`<dialog>` is a native HTML element for dialogs. When opened with `showModal()`, the browser makes the rest of the page inert, puts focus inside the dialog, closes it on Escape and renders it in the top layer above everything else. It saves a lot of custom code that used to be needed for accessible modals.

```html
<dialog id="confirm">
  <h2>Delete this file?</h2>
  <form method="dialog">
    <button value="cancel">Cancel</button>
    <button value="ok">Delete</button>
  </form>
</dialog>
<script>
  document.getElementById("confirm").showModal();
</script>
```

## 126: What is cognitive accessibility?

Cognitive accessibility is about making content work for people with learning disabilities, memory problems, attention problems, brain injuries or dementia. It means clear language, simple and consistent layouts, helpful error messages, no pressure from time limits and fewer steps. The W3C has a guide called "Making Content Usable for People with Cognitive and Learning Disabilities".

## 127: Why does plain language help accessibility?

Short sentences, common words and clear instructions help people with cognitive disabilities, people reading in a second language and people who are tired or rushed. WCAG 3.1.5 Reading Level (Level AAA) suggests offering a simpler version when content needs more than a lower secondary school reading level. Plain language also tends to read better for everyone.

## 128: How should you write instructions so they don't depend on the senses?

WCAG 1.3.3 Sensory Characteristics (Level A) says instructions must not rely only on shape, color, size, location or sound. "Click the green button on the right" fails for blind and color blind users. Write "Click the Continue button" instead, which still works if the layout changes on mobile.

## 129: Why shouldn't content change orientation lock?

WCAG 1.3.4 Orientation (Level AA) says content must not be locked to portrait or landscape unless it is really needed, like a piano app. Some users have their tablet mounted on a wheelchair in one fixed orientation. Locking it means they can't use your site at all.

## 130: What is aria-current used for?

`aria-current` marks the current item in a set, like the current page in navigation or the current step in a checkout. Screen readers announce it as "current page" or similar. Use the matching value: `page`, `step`, `location`, `date`, `time` or `true`.

```html
<nav aria-label="Main">
  <a href="/" aria-current="page">Home</a>
  <a href="/blog">Blog</a>
</nav>
```

## 131: What is aria-expanded used for?

`aria-expanded` tells assistive technology whether a control's related content is open (`true`) or closed (`false`). Put it on the button that toggles the content, not on the content itself. Screen readers announce "collapsed" or "expanded", so users know what will happen when they press it.

```html
<button type="button" aria-expanded="false" aria-controls="faq1">
  What is your return policy?
</button>
<div id="faq1" hidden>...</div>
```

## 132: What is aria-pressed used for?

`aria-pressed` turns a button into a toggle button with an on or off state, like a "Bold" button in a text editor or a "Mute" button. Screen readers say "toggle button, pressed" or "not pressed". Don't change the label when the state changes, or the user hears both the label and the state flip at once.

```html
<button type="button" aria-pressed="false">Mute</button>
```

## 133: What is aria-invalid?

`aria-invalid="true"` tells assistive technology that the value of a field failed validation. Screen readers announce "invalid entry" or similar when the field is focused. Set it only after the user has tried to submit or left the field, not on empty fields as soon as the page loads.

## 134: What is the difference between required and aria-required?

`required` is an HTML attribute that both tells assistive technology the field is required and turns on browser validation. `aria-required="true"` only tells assistive technology and does nothing else. Use `required` on native inputs, and use `aria-required` on custom controls, or when you want to show your own validation messages instead of the browser's (combined with `novalidate` on the form).

## 135: What is an ARIA live region?

A live region is an area of the page whose changes are announced by screen readers automatically, even when focus is somewhere else. It is used for things like "Item added to cart" or chat messages. You create one with `aria-live="polite"`, `role="status"` or `role="alert"`.

```html
<div role="status" id="cart-status"></div>
<script>
  document.getElementById("cart-status").textContent = "Item added to cart";
</script>
```

## 136: What is role="alert"?

`role="alert"` creates an assertive live region, so screen readers announce its content right away and may interrupt what they are reading. Use it only for urgent, important messages like errors that block the user. Overusing it makes the page noisy and annoying.

## 137: Why do multiple nav elements need labels?

If a page has more than one `<nav>`, like a main menu, a breadcrumb and a footer menu, screen readers list them all as "navigation". Give each one a unique label with `aria-label` or `aria-labelledby` so users can tell them apart. Don't include the word "navigation" in the label, because the role already says it.

```html
<nav aria-label="Main">...</nav>
<nav aria-label="Breadcrumb">...</nav>
```

## 138: What are figure and figcaption for?

`<figure>` wraps self-contained content like an image, chart or code example, and `<figcaption>` gives it a visible caption. The caption is linked to the figure for assistive technology. The image inside still needs its own `alt` text, because the caption and the alt text do different jobs.

## 139: How do you make complex images like charts accessible?

Give a short alt text that says what the chart shows and its main point, and put the full data nearby as a data table or text. For example, `alt="Line chart of monthly sales, described below"` plus a table of the numbers. This helps blind users and also people who find charts hard to read.

## 140: Should the title attribute be used for accessibility?

Mostly no. `title` tooltips only appear on mouse hover, so keyboard and touch users never see them, and screen readers treat it in different ways. It is fine as a backup, but it should not be the only way to give a control its name or important information. The `<iframe>` title is an exception where it is the right tool.

## 141: What does WCAG 2.4.6 Headings and Labels mean?

It is a Level AA rule saying headings and labels must describe the topic or purpose. It doesn't require headings to exist, but where you use them they must be clear. A form field labeled just "Name" is unclear if the form asks for both a first name and a company name.

## 142: What is the multiple ways criterion?

WCAG 2.4.5 Multiple Ways (Level AA) says there must be more than one way to find a page in a set of pages, for example a navigation menu plus a search box or a site map. Some people find search easier, others prefer browsing. Pages that are steps in a process, like checkout, are exempt.

## 143: What does consistent navigation mean in WCAG?

WCAG 3.2.3 Consistent Navigation (Level AA) says menus and other navigation that repeat across pages should stay in the same relative order. WCAG 3.2.4 Consistent Identification (Level AA) says things with the same function should have the same label everywhere, like a search button always called "Search". Predictable layouts help people with cognitive and visual disabilities.

## 144: What is a change of context in WCAG?

A change of context is a big change that can confuse users, like opening a new window, moving focus, going to a new page or heavily changing the page. WCAG 3.2.1 On Focus and 3.2.2 On Input (both Level A) say these must not happen just because a field gets focus or its value changes. For example, a select menu shouldn't load a new page as soon as an option is picked, unless users are warned first.

## 145: Should links open in new tabs?

Usually not, because it breaks the back button and can confuse screen reader and magnifier users. If a link must open a new tab, like a help page in the middle of a form, tell users in the link text or with a visually hidden note and an icon. Let users decide by default, since they can open new tabs themselves.

```html
<a href="/help" target="_blank"
  >Help <span class="sr-only">(opens in new tab)</span></a
>
```

## 146: How should SVG images be made accessible?

For an SVG used as an `<img>`, add `alt` like any other image. For inline SVG that means something, add `role="img"` and a `<title>` or `aria-label`. For decorative inline SVG, add `aria-hidden="true"` so screen readers skip it.

```html
<svg role="img" aria-labelledby="logo-title" viewBox="0 0 100 100">
  <title id="logo-title">Acme Corp</title>
  ...
</svg>
```

## 147: What is the role of emoji in accessibility?

Screen readers read emoji by their official names, like "face with tears of joy", so a row of five emoji is read as five long names. Use them carefully and not instead of words. If an emoji is decorative, wrap it in a span with `aria-hidden="true"`; if it means something, the default name may be fine, or you can use `role="img"` with an `aria-label`.

## 148: How do you test a page with the keyboard only?

Start at the top of the page and press Tab through everything. Check that every interactive element can be reached, that the focus indicator is always visible, that the order makes sense and that you can use each control with Enter, Space, arrows and Escape. Also check that focus never gets lost or stuck, especially after opening and closing dialogs.

## 149: What is an accessibility statement?

An accessibility statement is a page that says what standard the site aims for, its current level of conformance, known problems, and how users can report issues or get help. Public sector sites in the EU are required to have one. It shows commitment and gives users a way to contact you when something doesn't work.

## 150: Where can developers learn more about accessibility?

Good starting places are the W3C WAI site (WCAG, Understanding WCAG and the ARIA Authoring Practices Guide), MDN's accessibility docs, WebAIM's articles and surveys, and web.dev's accessibility course. The A11y Project has a practical checklist. The best learning, though, is using your own site with a keyboard and a screen reader, and watching disabled people use it.

# Moderate Questions (151-300)

## 151: How do you build an accessible modal dialog?

The easiest way is the native `<dialog>` element opened with `showModal()`. It traps focus by making the rest of the page inert, closes on Escape and renders on top of everything. You still need to give it a name with `aria-labelledby`, put focus on a sensible element inside, and return focus to the button that opened it when it closes.

```js
const openBtn = document.querySelector("#open");
const dialog = document.querySelector("#settings");

openBtn.addEventListener("click", () => dialog.showModal());
dialog.addEventListener("close", () => openBtn.focus());
```

## 152: Where should focus go when a modal opens?

Usually on the first focusable element, or on the dialog heading (with `tabindex="-1"`) if the dialog starts with a lot of text the user should read first. For a destructive confirmation, put focus on the safer option, like "Cancel". You can control this with the `autofocus` attribute inside a `<dialog>`, which `showModal()` respects.

## 153: Why must focus return to the trigger when a dialog closes?

If focus is not moved back, browsers often drop it on the `<body>`, and keyboard and screen reader users end up at the top of the page. They then have to find their place again. Returning focus to the button that opened the dialog keeps them where they were. The native `<dialog>` does this for you in current browsers, but test it, and handle it yourself in custom modals.

## 154: What does the inert attribute do?

`inert` makes an element and everything inside it unfocusable, unclickable and hidden from assistive technology, while it stays visible. It is perfect for the page behind a custom modal or a side drawer. It is supported in all modern browsers.

```js
document.querySelector("main").inert = true; // when the drawer opens
document.querySelector("main").inert = false; // when it closes
```

## 155: How did developers trap focus in modals before inert and dialog existed?

They listened for Tab and Shift + Tab on the last and first focusable elements and moved focus back to the other end. They also set `aria-hidden="true"` on everything outside the modal so screen readers couldn't wander out. This works but is fragile, because new focusable elements can be added and screen readers can still escape with their own reading keys. Today `inert` and `<dialog>` are better options.

## 156: What does aria-modal="true" do?

`aria-modal="true"` tells assistive technology that content outside the dialog is not available, so screen readers should limit reading to the dialog. It does not actually block focus or clicks, so you still need `inert` or a focus trap. With native `<dialog>` and `showModal()` you don't need it, because the browser marks the dialog as modal itself.

## 157: How do you build an accessible disclosure (show/hide) widget?

Use a `<button>` with `aria-expanded` that toggles a panel, or use native `<details>`. Update `aria-expanded` every time the state changes, and hide the panel with `hidden` when closed. The button text should stay the same; the state is announced through `aria-expanded`.

```js
const btn = document.querySelector("#toggle");
const panel = document.querySelector("#panel");

btn.addEventListener("click", () => {
  const open = btn.getAttribute("aria-expanded") === "true";
  btn.setAttribute("aria-expanded", String(!open));
  panel.hidden = open;
});
```

## 158: How do you build an accessible accordion?

An accordion is a set of disclosure widgets. Each header is a heading element containing a `<button>` with `aria-expanded` and `aria-controls`. The panels can use `role="region"` with `aria-labelledby` pointing to the button, but only if there are few panels, or the landmark list gets crowded. Arrow key navigation between headers is optional in the APG pattern; Tab must work.

```html
<h3>
  <button type="button" aria-expanded="false" aria-controls="sect1" id="acc1">
    Billing
  </button>
</h3>
<div id="sect1" role="region" aria-labelledby="acc1" hidden>...</div>
```

## 159: How do you build accessible tabs?

Use a container with `role="tablist"`, buttons with `role="tab"` and panels with `role="tabpanel"`. The selected tab has `aria-selected="true"` and `tabindex="0"`, the others `tabindex="-1"`. Left and Right arrows move between tabs, Home and End go to the first and last, and Tab moves from the tab list into the active panel.

```html
<div role="tablist" aria-label="Account">
  <button role="tab" id="t1" aria-selected="true" aria-controls="p1">
    Profile
  </button>
  <button
    role="tab"
    id="t2"
    aria-selected="false"
    aria-controls="p2"
    tabindex="-1"
  >
    Security
  </button>
</div>
<div role="tabpanel" id="p1" aria-labelledby="t1">...</div>
<div role="tabpanel" id="p2" aria-labelledby="t2" hidden>...</div>
```

## 160: What is a roving tabindex?

Roving tabindex is a way to make a group of items, like tabs, toolbar buttons or grid cells, take a single Tab stop. Only the active item has `tabindex="0"`; all others have `tabindex="-1"`. Arrow keys move focus within the group, and the code moves the `0` to the newly focused item. This keeps the tab order short and matches how native widgets like radio groups behave.

```js
function moveFocus(items, from, to) {
  items[from].tabIndex = -1;
  items[to].tabIndex = 0;
  items[to].focus();
}
```

## 161: Should tabs activate automatically when focused or only on Enter?

The APG describes both. Automatic activation shows the panel as soon as a tab gets focus with the arrow keys, and is best when panels load instantly. Manual activation needs Enter or Space and is better when switching panels is slow, like when it fetches data, because arrow key users would trigger many loads. Pick one and be consistent.

## 162: When should you not use the ARIA menu role?

`role="menu"` and `role="menubar"` are meant for application menus like those in desktop programs, with arrow key navigation and type-ahead. Site navigation is not an application menu; it should be a `<nav>` with a list of links. Using `role="menu"` for site navigation makes screen readers switch into a mode where links behave differently and users can't use their usual shortcuts.

## 163: How do you build an accessible dropdown navigation menu?

Use a `<nav>` with a list of links, and for sections with sub-items, use a `<button>` with `aria-expanded` that shows and hides a nested list. This is the "disclosure navigation" pattern from the APG. Escape should close an open submenu and return focus to its button. Avoid opening menus only on hover, because keyboard and touch users can't hover.

## 164: How do you build an accessible menu button?

A menu button is a `<button>` with `aria-haspopup="menu"` (or `true`) and `aria-expanded`, which opens an element with `role="menu"` containing `role="menuitem"` items. When it opens, focus moves to the first item. Up and Down arrows move through items, Enter activates, Escape closes and returns focus to the button. Use this for action menus like "More actions", not for navigation.

## 165: What is a combobox?

A combobox is an input that controls a popup with suggestions, like an autocomplete search box. The input has `role="combobox"`, `aria-expanded`, `aria-controls` pointing to a `role="listbox"`, and `aria-autocomplete`. The focus stays in the input while `aria-activedescendant` points to the highlighted option, so users can keep typing. It is one of the hardest widgets to get right, so use a well-tested library or the native `<datalist>` or `<select>` when possible.

## 166: What is aria-activedescendant?

`aria-activedescendant` lets an element keep DOM focus while telling assistive technology that a different child element is "active". The value is the `id` of that child. It is used in comboboxes and listboxes, where focus must stay in the text input while the user arrows through options. The active option must be visibly highlighted too, because the browser doesn't draw a focus ring on it.

## 167: How do you build an accessible custom select or listbox?

First ask whether a native `<select>` will do, since it works with every assistive technology and on every phone. Newer browsers support customizable select with `appearance: base-select`, which lets you style the native element. If you still need a custom one, use `role="listbox"` with `role="option"` items, `aria-selected`, arrow key navigation, Home and End, type-ahead and a button or combobox to open it. Test it with several screen readers, especially on mobile.

## 168: How do you make a custom checkbox accessible?

The safest way is to keep a real `<input type="checkbox">`, hide it visually in a way that keeps it accessible, and style a sibling element to look how you want. That way you keep keyboard support, the checked state, form submission and label clicks for free. Using a `<div role="checkbox">` means you must handle `aria-checked`, focus, Space key and form data yourself.

```css
.checkbox input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}
.checkbox input:focus-visible + .box {
  outline: 2px solid currentColor;
}
.checkbox input:checked + .box::after {
  content: "✓";
}
```

## 169: How do you build an accessible toggle switch?

Use a `<button>` with `role="switch"` and `aria-checked`, or an `<input type="checkbox" role="switch">`. Screen readers announce "switch, on" or "off". Keep the label the same and let the state carry the meaning; don't change the label from "Enable" to "Disable" when it is toggled.

```html
<button type="button" role="switch" aria-checked="false" id="notif">
  Email notifications
</button>
```

## 170: How do you build an accessible tooltip?

A tooltip is a short text that appears on hover and on focus, connected to its trigger with `aria-describedby`. It must not contain interactive content, must stay visible while the pointer is over it, and must close with Escape. If the content needs links or buttons, use a non-modal dialog or popover instead. Don't use tooltips for information users must have, since touch users can't hover.

```html
<button type="button" aria-describedby="tip1">Share</button>
<div role="tooltip" id="tip1" hidden>Share this link with your team</div>
```

## 171: What is WCAG 1.4.13 Content on Hover or Focus?

It is a Level AA rule for content that appears on hover or focus, like tooltips and popovers. Such content must be dismissable without moving the pointer (usually with Escape), hoverable so the user can move the pointer onto it without it disappearing, and persistent until the user moves away or dismisses it. Screen magnifier users need this because the tooltip often covers what they are trying to read.

## 172: How do you announce toast notifications?

Put a live region on the page when it loads, usually with `role="status"` for normal messages, and insert the message text into it when the toast appears. Don't auto-hide toasts too quickly, and never put the only copy of an important action, like "Undo", in a toast that disappears. Toasts with buttons are hard to reach for keyboard users, so offer the same action somewhere else too.

## 173: What is the difference between aria-live polite and assertive?

`polite` waits until the screen reader finishes what it is saying before announcing the change. `assertive` interrupts right away and can drop what was being read. Use `polite` for almost everything, like "Saved" or search result counts, and keep `assertive` for urgent errors or time-sensitive warnings.

## 174: Why must a live region exist before you update it?

Screen readers start watching a live region when it appears in the accessibility tree. If you add a new element with `aria-live` and text in the same step, many screen readers miss the first message. Render an empty live region on page load, then change its text content later.

## 175: What do aria-atomic and aria-relevant do?

`aria-atomic="true"` tells the screen reader to read the whole live region when any part changes, instead of only the changed part. That's useful for something like "3 of 10 items", where reading only "4" would make no sense. `aria-relevant` says which kinds of changes to announce: `additions`, `removals`, `text` or `all`; the default is `additions text`, and support for other values is weak, so it is rarely changed.

## 176: What are role="status", role="log" and role="timer"?

They are live region roles with built-in behavior. `status` is polite and atomic, used for messages like "Saved". `log` is polite and for streams where new items are added in order, like chat or console output. `timer` is for a countdown or clock and is off by default (not announced), because announcing every second would be unbearable.

## 177: How do you announce loading states?

When content starts loading after a user action, announce it in a polite live region, like "Loading results", and announce again when it is done, like "12 results found". You can set `aria-busy="true"` on the area being updated so assistive technology waits until it is complete. A spinner alone with no text is invisible to screen readers.

## 178: What does aria-busy do?

`aria-busy="true"` tells assistive technology that an element is being updated and it should wait before announcing or exposing the changes. Set it back to `false` when the update is done. It's useful for big updates like reloading a list, so the screen reader doesn't announce each item as it appears. Support differs between screen readers, so don't rely on it for important messages.

## 179: How do you manage focus after a route change in a single page app?

In a normal website, a new page load resets focus to the top and the screen reader announces the new title. In a single page app, nothing happens unless you do it. After a route change, update `document.title`, move focus to the main heading or the `<main>` element (with `tabindex="-1"`), and/or announce the new page in a live region.

```js
function onRouteChange(title) {
  document.title = `${title} - My App`;
  const h1 = document.querySelector("main h1");
  h1.setAttribute("tabindex", "-1");
  h1.focus();
}
```

## 180: Do frameworks like Next.js handle route announcements?

Next.js includes a route announcer that reads the new page title (or the first `<h1>`, or the URL path) to screen readers on client-side navigation. It does not move focus for you. Other frameworks and routers vary, so check what yours does and test it with a screen reader rather than assuming it is handled.

## 181: How do you associate labels with inputs in React?

Use `htmlFor` instead of `for`, because `for` is a reserved word in JavaScript. To avoid duplicate ids when a component is used many times, generate ids with React's `useId` hook.

```jsx
import { useId } from "react";

function TextField({ label, ...props }) {
  const id = useId();
  return (
    <>
      <label htmlFor={id}>{label}</label>
      <input id={id} {...props} />
    </>
  );
}
```

## 182: How do you move focus in React?

Use a ref and call `focus()` on the DOM node, usually in an effect or event handler after the element is rendered. Don't use `autoFocus` everywhere, because jumping focus on page load can confuse screen reader users.

```jsx
import { useEffect, useRef } from "react";

function ErrorSummary({ errors }) {
  const ref = useRef(null);
  useEffect(() => {
    if (errors.length) ref.current?.focus();
  }, [errors]);
  return (
    <div ref={ref} tabIndex={-1} role="alert">
      <h2>There are {errors.length} errors</h2>
    </div>
  );
}
```

## 183: Why do React fragments help accessibility?

Fragments (`<>...</>`) let a component return several elements without adding a wrapper `<div>`. Extra wrappers can break HTML structures that depend on direct children, like `<ul>` with `<li>`, `<table>` with `<tr>`, or `<dl>`. Broken structures lose their list or table semantics in the accessibility tree.

## 184: What is eslint-plugin-jsx-a11y?

It is an ESLint plugin that checks JSX for common accessibility mistakes, like missing alt text, click handlers on non-interactive elements without keyboard handlers, invalid ARIA attributes and labels not connected to inputs. It runs in the editor and in CI, so problems are caught while coding. It can only check static code, not the final rendered page.

## 185: How do you test accessibility with jest-axe?

jest-axe runs axe-core on rendered HTML in a Jest test and adds a `toHaveNoViolations` matcher. It is useful for catching regressions in components. Note that it runs in jsdom, which has no layout, so it can't check color contrast.

```js
import { render } from "@testing-library/react";
import { axe, toHaveNoViolations } from "jest-axe";
import { LoginForm } from "./LoginForm";

expect.extend(toHaveNoViolations);

test("LoginForm has no axe violations", async () => {
  const { container } = render(<LoginForm />);
  expect(await axe(container)).toHaveNoViolations();
});
```

## 186: Why does Testing Library recommend getByRole?

`getByRole` finds elements the way assistive technology sees them, by role and accessible name. If your test can't find "button named Submit", a screen reader user probably can't either. It pushes you toward accessible markup and makes tests less tied to class names and structure.

```js
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";

test("submits the form", async () => {
  render(<LoginForm />);
  await userEvent.type(
    screen.getByRole("textbox", { name: "Email" }),
    "a@b.com",
  );
  await userEvent.click(screen.getByRole("button", { name: "Log in" }));
});
```

## 187: How do you run axe in Playwright?

Install `@axe-core/playwright` and use `AxeBuilder` inside a test. You can limit the rules to WCAG tags and exclude third-party areas you don't control. Because it runs in a real browser, it can check contrast too.

```js
import { test, expect } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

test("home page has no WCAG A/AA violations", async ({ page }) => {
  await page.goto("/");
  const results = await new AxeBuilder({ page })
    .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "wcag22aa"])
    .exclude("#third-party-chat")
    .analyze();
  expect(results.violations).toEqual([]);
});
```

## 188: How do you test keyboard behavior in automated tests?

Use Testing Library's `userEvent.keyboard` or `userEvent.tab()` in unit tests, and `page.keyboard.press()` in Playwright. Check that focus moves where it should with `toHaveFocus()`. This catches regressions like a dialog that no longer closes on Escape.

```js
import { test, expect } from "@playwright/test";

test("Escape closes the dialog", async ({ page }) => {
  await page.goto("/settings");
  await page.getByRole("button", { name: "Edit profile" }).click();
  await page.keyboard.press("Escape");
  await expect(page.getByRole("dialog")).toBeHidden();
  await expect(
    page.getByRole("button", { name: "Edit profile" }),
  ).toBeFocused();
});
```

## 189: What is the Storybook accessibility addon?

`@storybook/addon-a11y` runs axe-core on each story and shows violations in a panel. It lets designers and developers check components in isolation while building them. You can also run the same checks in CI with the Storybook test runner, so a component can't be merged with known issues.

## 190: How do you add accessibility checks to CI?

Run linting (like eslint-plugin-jsx-a11y), component tests with jest-axe or the Storybook test runner, and end-to-end tests with `@axe-core/playwright` on key pages. Fail the build on new violations. Tools like pa11y-ci or Lighthouse CI can also scan a list of URLs. Remember that a green CI only means no automatically detectable issues.

## 191: How do you do a basic screen reader test?

Turn on the screen reader and use it the way users do: jump by headings, list landmarks and links, tab through forms and use each interactive widget. Listen for missing names, wrong roles, states that don't update and content that is read in the wrong order. Close your eyes or turn off the monitor for part of the test so you don't rely on what you see.

## 192: Which screen reader and browser combinations should you test with?

Test the combinations people actually use: NVDA with Chrome or Firefox, JAWS with Chrome, VoiceOver with Safari on macOS and iOS, and TalkBack with Chrome on Android. Screen readers behave differently, so passing in one doesn't mean it works in another. If you can only test one desktop combination, NVDA with Chrome is a common choice because NVDA is free and widely used.

## 193: What are some useful NVDA keyboard shortcuts?

The NVDA key is usually Insert (or Caps Lock in laptop layout). In browse mode, H jumps to the next heading, D to the next landmark, K to the next link, F to the next form field and T to the next table. NVDA + F7 opens the elements list, NVDA + Space switches between browse and focus mode, and Ctrl stops speech.

## 194: What is the VoiceOver rotor?

The rotor is a VoiceOver menu that lists elements by type, like headings, links, landmarks and form controls. On macOS you open it with VO + U and switch lists with the arrow keys. On iOS you rotate two fingers on the screen to pick a type, then swipe up or down to move between items of that type.

## 195: How do you inspect the accessibility tree in Chrome DevTools?

Open DevTools, select an element in the Elements panel and open the Accessibility pane. It shows the computed role, name, description and states, and how the name was calculated. You can also turn on "full-page accessibility tree" to replace the DOM view with the accessibility tree. Firefox has a similar Accessibility Inspector that can also simulate color blindness.

## 196: How is the accessible name of a button calculated?

The browser follows the Accessible Name and Description Computation spec. For a button, it first uses `aria-labelledby`, then `aria-label`, then the text content of the button (including `alt` of images inside it), and finally the `title` attribute. The first one that gives a non-empty result wins.

## 197: Can aria-labelledby reference multiple elements?

Yes. Give a space-separated list of ids, and the names are joined in that order. You can even include the element's own id. This is useful when a button like "Delete" needs context, such as the name of the row it belongs to.

```html
<h3 id="item-42">Invoice #42</h3>
<button type="button" id="del-42" aria-labelledby="del-42 item-42">
  Delete
</button>
<!-- Accessible name: "Delete Invoice #42" -->
```

## 198: What is aria-errormessage and how does it differ from aria-describedby?

`aria-errormessage` points to the element that holds the error message, and it is only meant to be exposed when `aria-invalid="true"` is set. `aria-describedby` points to any extra description and is always exposed. Support for `aria-errormessage` has improved but is still uneven across screen readers, so many teams still use `aria-describedby` for errors.

## 199: How should you show form errors after submit?

Show an error summary at the top of the form that lists all errors with links to each field, move focus to that summary, and also show each error next to its field. Set `aria-invalid` and `aria-describedby` on the fields. This is the pattern used by the GOV.UK Design System and is well tested with users.

```html
<div tabindex="-1" id="error-summary" role="alert">
  <h2>There is a problem</h2>
  <ul>
    <li><a href="#email">Enter your email address</a></li>
  </ul>
</div>
```

## 200: Should you validate fields while the user types?

Usually not on every keystroke, because the error appears before the user had a chance to finish, and screen readers may announce errors over and over. A common approach is to validate when the user leaves the field (on blur) or on submit, and then update the error as they correct it. Positive feedback like password strength can update live in a polite region.

## 201: What does WCAG 3.3.2 Labels or Instructions require?

It is a Level A rule saying fields must have labels or instructions when the user needs to enter data. That includes telling users about required formats, like "Date (DD/MM/YYYY)", before they make a mistake. Put format hints in the label or in a hint connected with `aria-describedby`.

## 202: What does WCAG 3.3.4 Error Prevention mean?

It is a Level AA rule for pages that create legal or financial commitments, change user data in a storage system, or submit test answers. Submissions must be reversible, checked for errors with a chance to fix them, or confirmed by the user before they are final. A review step before placing an order is a common way to pass.

## 203: How do you make radio buttons accessible?

Use native `<input type="radio">` with the same `name`, each with its own `<label>`, and wrap the group in a `<fieldset>` with a `<legend>`. Arrow keys move between options and only the checked one is in the tab order, which the browser handles for you. If you need a custom look, style the native input or hide it visually and style its label.

## 204: How do you make a date picker accessible?

The native `<input type="date">` is usually the most accessible choice, even if its look varies between browsers. If you build a custom calendar, it is a dialog containing a grid with arrow key navigation, and the hardest part is screen reader support. Always also let users type the date directly in a text field with a clear format hint, because many people find calendars slow.

## 205: How do you make a slider accessible?

The native `<input type="range">` is accessible by default. For a custom slider, use `role="slider"` with `aria-valuenow`, `aria-valuemin`, `aria-valuemax` and `aria-valuetext` if the number needs words, like "Medium". Arrow keys change the value, Page Up and Page Down change it by bigger steps, and Home and End go to the limits. To meet WCAG 2.5.7, also offer a way to change the value without dragging.

## 206: How do you make a progress bar accessible?

Use the native `<progress>` element, or `role="progressbar"` with `aria-valuenow`, `aria-valuemin` and `aria-valuemax`. Give it a name with a label or `aria-label`. If the progress is unknown, leave out `aria-valuenow`. For long tasks, also announce milestones in a live region, because screen readers don't announce every value change.

```html
<label for="upload">Uploading report.pdf</label>
<progress id="upload" max="100" value="40">40%</progress>
```

## 207: How do you make a file upload accessible?

Use a native `<input type="file">` with a label. If you style a custom button, you can hide the input visually and use a `<label>` styled as a button, so it keeps keyboard and screen reader support. A drag and drop zone must not be the only way to upload, and the selected file name and any upload errors should be shown as text and announced.

## 208: What does :focus-visible do?

`:focus-visible` matches an element when the browser decides the focus ring should be shown, which is usually after keyboard navigation but not after a mouse click on a button. Text inputs show it on any focus, because users need to see where they're typing. It lets designers have clean mouse interactions without hurting keyboard users.

## 209: What does :focus-within do?

`:focus-within` matches an element when it or any of its children has focus. It's useful for highlighting a whole card, form group or menu when something inside it is focused. It can also keep a dropdown menu open while a keyboard user moves through its links.

```css
.card:focus-within {
  outline: 2px solid #1a73e8;
}
```

## 210: What is WCAG 1.4.11 Non-text Contrast?

It is a Level AA rule requiring a contrast ratio of at least 3:1 for parts of user interface components and graphics needed to understand content. That includes input borders, checkbox outlines, focus indicators, icons without text and lines in charts. Light gray borders on white inputs fail it very often.

## 211: What is WCAG 2.4.13 Focus Appearance?

It is a Level AAA rule added in WCAG 2.2. The focus indicator must be at least as large as a 2 CSS pixel thick outline around the element, and the focused and unfocused states must have a contrast ratio of at least 3:1. Even though it is AAA, it is a good target for design systems, because a 2px solid outline with good contrast easily meets it.

## 212: How do you design a focus indicator that works on any background?

A two-color ring works well, for example a dark outline with a light inner shadow or an outline with an offset, so it shows up on both light and dark backgrounds. Use `outline` rather than only `box-shadow`, because outlines stay visible in forced colors mode. Test it on every background your components appear on.

```css
:focus-visible {
  outline: 3px solid #0b57d0;
  outline-offset: 2px;
  box-shadow: 0 0 0 5px #fff;
}
```

## 213: How do you keep focused elements from hiding under sticky headers?

Use `scroll-padding-top` on the scroll container (usually `html`) set to the height of the sticky header. When the browser scrolls a focused element into view, it leaves that space free. This helps meet WCAG 2.4.11 Focus Not Obscured.

```css
html {
  scroll-padding-top: 80px;
}
```

## 214: How do you support forced colors mode in CSS?

Use the `forced-colors: active` media query to fix things that disappear, and use system color keywords like `CanvasText`, `ButtonText`, `Highlight` and `LinkText`. A common fix is adding a transparent outline or border, because the browser makes it visible in forced colors while it stays invisible normally. Avoid `forced-color-adjust: none` unless you have a very good reason.

```css
.button {
  border: 2px solid transparent;
}

@media (forced-colors: active) {
  .icon {
    fill: CanvasText;
  }
}
```

## 215: What does prefers-contrast do?

`prefers-contrast` is a media query that checks if the user asked the operating system for more or less contrast. Values are `more`, `less`, `custom` and `no-preference`. You can use `more` to make borders darker, remove transparent backgrounds and increase text contrast for those users.

## 216: How do you respect reduced motion in JavaScript?

Use `window.matchMedia("(prefers-reduced-motion: reduce)")` to check the setting, and listen for changes in case the user switches it while the page is open. Use it to turn off things like smooth scrolling, auto-playing animations and parallax effects that CSS alone can't control.

```js
const reduce = window.matchMedia("(prefers-reduced-motion: reduce)");

function scrollToTop() {
  window.scrollTo({ top: 0, behavior: reduce.matches ? "auto" : "smooth" });
}
reduce.addEventListener("change", () => console.log("motion setting changed"));
```

## 217: What is WCAG 2.3.3 Animation from Interactions?

It is a Level AAA rule saying motion animation triggered by user interaction, like parallax or zoom effects on scroll, can be turned off unless it is essential. People with vestibular disorders can feel dizzy or sick from it. Even though it's AAA, respecting `prefers-reduced-motion` meets it in most cases and is easy to do.

## 218: Does CSS generated content get read by screen readers?

Yes, text in `::before` and `::after` with `content` is usually included in the accessible name and read by screen readers. That can be bad for decorative symbols like arrows or stars. Modern browsers support alt text for generated content with a slash, like `content: "★" / ""` to make it silent.

```css
.new::before {
  content: "★" / "";
}
.external::after {
  content: "↗" / " (external link)";
}
```

## 219: How can CSS display values break semantics?

Some browsers used to remove table, list or button semantics when you changed `display`, for example `display: flex` on a `<table>` or `display: contents` on a `<button>`. Many of these bugs are fixed now, but `display: contents` on interactive elements still causes problems in some cases. `list-style: none` on a list also made Safari drop list semantics; adding `role="list"` brings them back.

## 220: How can flexbox and grid order break accessibility?

The CSS `order` property, `flex-direction: row-reverse` and explicit grid placement change where things appear, but not their DOM order. Tab order and screen reader order still follow the DOM, so a keyboard user may jump around the screen in a confusing way. Change the DOM order instead when the order has meaning. The new CSS `reading-flow` property, supported in Chromium, can make focus follow the visual order in flex and grid layouts.

## 221: How should icon fonts be handled?

Icon fonts put characters in the private use area of Unicode, which screen readers may read as nonsense or nothing. Hide the icon itself with `aria-hidden="true"` and provide a text label. Icon fonts also break when users override fonts, for example with a dyslexia-friendly font, so inline SVG is usually a better choice.

## 222: How do you write accessible breadcrumbs?

Wrap them in `<nav aria-label="Breadcrumb">` with an ordered list of links. Mark the last item, the current page, with `aria-current="page"`. Make separators like "/" or ">" decorative with CSS or `aria-hidden` so screen readers don't read "slash" between each item.

```html
<nav aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/shoes">Shoes</a></li>
    <li><a href="/shoes/running" aria-current="page">Running</a></li>
  </ol>
</nav>
```

## 223: How do you make pagination accessible?

Wrap the page links in `<nav aria-label="Pagination">`, use a list, and mark the current page with `aria-current="page"`. Give "previous" and "next" arrows real text or labels, and make page number links say more than the number, like "Page 3", with visually hidden text. After loading a new page of results in a single page app, move focus to the results heading.

## 224: What accessibility problems does infinite scroll cause?

Keyboard users can never reach the footer because new content keeps loading as they tab. Screen reader users aren't told new items appeared, and it's hard to get back to the same spot after leaving. A "Load more" button is a better pattern: it is in the user's control, and you can move focus to the first new item and announce how many were added.

## 225: How do you make a sortable table accessible?

Put a `<button>` inside each sortable `<th>` so it is keyboard operable. Set `aria-sort="ascending"` or `"descending"` on the `<th>` that is currently sorted, and leave it off the others. Announce the change in a polite live region, like "Sorted by date, newest first", since not all screen readers announce `aria-sort` changes.

```html
<th aria-sort="ascending">
  <button type="button">Date</button>
</th>
```

## 226: How do you make tables readable on small screens without breaking them?

The simplest safe way is to wrap the table in a container with `overflow-x: auto`, so it scrolls sideways, which WCAG reflow allows for data tables. Make the container focusable with `tabindex="0"`, give it a label and a role like `region` so keyboard users can scroll it. Turning cells into stacked blocks with CSS can remove table semantics, so if you do that, restore roles and test it.

```html
<div role="region" aria-labelledby="tbl-cap" tabindex="0" class="table-scroll">
  <table>
    <caption id="tbl-cap">
      Order history
    </caption>
    ...
  </table>
</div>
```

## 227: When do you need the headers attribute in tables?

For complex tables with multi-level headers or headers that span several rows and columns, `scope` is not enough. You give each `<th>` an `id` and list the matching ids in each `<td>`'s `headers` attribute. It is a lot of work, so often a better fix is to split one complex table into a few simple ones.

## 228: What is the difference between role="presentation" and aria-hidden="true"?

`role="presentation"` (or `role="none"`) removes the element's own role, but its content is still read. `aria-hidden="true"` removes the element and all of its content from the accessibility tree. Use `role="none"` on a layout table to keep the text but drop the table structure, and use `aria-hidden` on a decorative icon to hide it fully.

## 229: When is role="presentation" ignored?

If an element is focusable or has global ARIA attributes like `aria-label` or `aria-describedby`, browsers ignore `role="presentation"` and keep its real role. This is called presentational role conflict resolution. It prevents authors from hiding the role of something users can actually interact with.

## 230: Why is aria-hidden on a focusable element a problem?

Keyboard users can still tab to the element, but screen readers either say nothing or something confusing, because it isn't in the accessibility tree. axe reports this as an error. If you hide something with `aria-hidden`, also make every focusable element inside it unfocusable, or better, use `inert`, which does both.

## 231: When should you use the region role or a named section?

A `<section>` becomes a `region` landmark only if it has an accessible name from `aria-label` or `aria-labelledby`. Use it for important areas users may want to jump to, like a "Filters" panel or a "Related articles" block. Don't name every section, or the landmark list becomes as long as the page.

## 232: What is the search element?

`<search>` is an HTML element added in 2023 for the part of a page that holds search or filtering controls. It maps to the `search` landmark role, so you no longer need `role="search"` on a `<form>` or `<div>`. It is supported in all modern browsers.

```html
<search>
  <form action="/search">
    <label for="q">Search articles</label>
    <input id="q" name="q" type="search" />
    <button>Search</button>
  </form>
</search>
```

## 233: When is a form element a landmark?

A `<form>` is exposed as a `form` landmark only when it has an accessible name, for example from `aria-label` or `aria-labelledby`. Many forms don't need to be landmarks. Name the important ones, like a "Contact us" form, so users can jump to them.

## 234: What does aria-controls do and is it well supported?

`aria-controls` points from a control to the element it changes, like a tab to its panel. JAWS used to announce it and offer a shortcut to jump there, but most other screen readers do nothing with it. It doesn't hurt to add, and some patterns still use it, but don't rely on it to make a widget understandable.

## 235: What does aria-haspopup do?

`aria-haspopup` tells assistive technology that a control opens a popup. The values are `menu` (or `true`), `listbox`, `tree`, `grid` and `dialog`. Screen readers may announce something like "menu button" or "has popup". Use the value that matches the popup's role, and don't use it for simple disclosure buttons that just show content.

## 236: What does aria-owns do?

`aria-owns` makes elements that live elsewhere in the DOM be treated as children of another element in the accessibility tree. It's sometimes used when a popup is rendered in a portal at the end of `<body>`. Support is uneven, especially in Safari, so moving the DOM element to the right place is usually better.

## 237: How do you make the popover attribute accessible?

The `popover` attribute gives you light dismiss, Escape to close and top-layer rendering for free. When a button with `popovertarget` controls it, browsers expose an `aria-expanded`-like relationship and focus moves to the popover in the right order for keyboard users. You still need to choose the right role for what's inside, like a menu or a dialog, and give it a name.

```html
<button popovertarget="help">Help</button>
<div id="help" popover>
  <p>Contact support at any time.</p>
</div>
```

## 238: What is the difference between a modal and a non-modal dialog?

A modal dialog blocks the rest of the page until it is closed, so focus stays inside and the background is inert. A non-modal dialog, like a chat window, lets users move between it and the page. Open a `<dialog>` with `showModal()` for modal and `show()` for non-modal. Non-modal dialogs need a way to get back to them, like a keyboard shortcut or a visible button.

## 239: What is the alertdialog role?

`role="alertdialog"` is for a modal dialog that interrupts the user with an urgent message that needs a response, like "Delete 50 files?". Screen readers may read the message right away, so connect it with `aria-describedby`. Put focus on a safe button inside it.

```html
<div
  role="alertdialog"
  aria-modal="true"
  aria-labelledby="t"
  aria-describedby="d"
>
  <h2 id="t">Delete files?</h2>
  <p id="d">50 files will be deleted forever.</p>
  <button type="button">Cancel</button>
  <button type="button">Delete</button>
</div>
```

## 240: Is the autofocus attribute good or bad for accessibility?

It depends. On a page whose only purpose is a single form, like a login page, it can help. On normal pages it can confuse screen reader users, because the page starts in the middle and skips the content above. Inside a dialog it is a good way to choose the first focused element.

## 241: How do you build an accessible carousel?

Avoid auto-rotation, or give a visible pause button and stop rotation when anything inside gets focus or the pointer hovers. Use real buttons for previous and next, label each slide (for example `role="group"` with `aria-roledescription="slide"` and `aria-label="2 of 5"`), and hide slides that aren't shown with `inert` or `hidden`. Many teams find that carousels hurt everyone's experience and skip them entirely.

## 242: What is aria-roledescription and when should you use it?

`aria-roledescription` changes the word screen readers use for an element's role, like "slide" instead of "group". It should only be used on elements that have a real role, and only to make the description more specific. Overusing it, or using it on things like buttons, removes information users depend on to know how to interact.

## 243: How do you make a video player accessible?

Use controls that are real buttons with labels, support the keyboard (Space to play and pause, arrows to seek), and show captions with a `<track>` element. Provide a transcript and audio description where needed. Native `<video controls>` gives you a lot for free, and accessible players like Able Player or Video.js are options when you need a custom look.

```html
<video controls>
  <source src="intro.mp4" type="video/mp4" />
  <track
    kind="captions"
    src="intro.en.vtt"
    srclang="en"
    label="English"
    default
  />
</video>
```

## 244: What is WebVTT?

WebVTT (Web Video Text Tracks) is the text format browsers use for captions, subtitles, descriptions and chapters with the `<track>` element. Each cue has a start time, an end time and the text. It can also include speaker names and simple positioning.

```text
WEBVTT

00:00:01.000 --> 00:00:04.000
<v Anna>Welcome to the course.

00:00:04.500 --> 00:00:06.000
[upbeat music]
```

## 245: What is the difference between automatic captions and accurate captions?

Automatic captions from speech recognition, like those on YouTube, often get names, technical terms and punctuation wrong and don't show who is speaking. They don't meet WCAG unless someone checks and fixes them. They are a good first draft, but a human needs to review them before publishing.

## 246: How do you make drag and drop accessible?

Offer a keyboard way to do the same thing, like "Move up" and "Move down" buttons, or a mode where Space picks an item up, arrows move it and Space drops it. Announce what happens in a live region, like "Item moved to position 3 of 5". Libraries like dnd-kit include keyboard sensors and screen reader announcements. WCAG 2.5.7 also needs a single-pointer alternative, which buttons provide.

## 247: How do you handle gestures like swipe or pinch?

WCAG 2.5.1 Pointer Gestures (Level A) says anything done with a multi-point or path-based gesture, like pinch to zoom a map or swipe in a shape, must also work with a single pointer without a path, like tapping a button. Add zoom buttons to maps and previous and next buttons to swipeable galleries. Some users can only use one finger or a head pointer.

## 248: What is WCAG 2.5.2 Pointer Cancellation?

It is a Level A rule saying actions should run on the up event (when the user releases), not the down event, or there must be a way to cancel or undo. That way users who press the wrong thing can slide off it before releasing. Native `click` events already work this way, so the problem mostly appears with custom `mousedown` or `touchstart` handlers.

## 249: What is WCAG 2.5.3 Label in Name?

It is a Level A rule saying that when a control has a visible text label, its accessible name must contain that text, ideally at the start. Voice control users say "click Search", so if the button shows "Search" but its `aria-label` is "Find products", the command won't work. Be careful when adding `aria-label` to elements that already have visible text.

## 250: What is WCAG 2.5.4 Motion Actuation?

It is a Level A rule saying features triggered by moving the device, like shake to undo or tilt to scroll, must also work through normal controls, and users must be able to turn off the motion response. Some users have their device fixed in place or can't move it accurately.

## 251: What is WCAG 2.1.4 Character Key Shortcuts?

It is a Level A rule about keyboard shortcuts that use a single letter, number or symbol key, like "s" to search. Users must be able to turn them off, remap them, or the shortcut must only work when a specific component has focus. Voice control users can trigger these shortcuts by accident when their speech is typed as letters.

## 252: What is WCAG 4.1.3 Status Messages?

It is a Level AA rule saying status messages, like "Saved", "5 results found" or "Item added to cart", must be announced by assistive technology without moving focus. You meet it with live regions such as `role="status"` or `role="alert"`. Moving focus to the message would interrupt the user's work.

## 253: What does WCAG 1.3.1 Info and Relationships require?

It is a Level A rule saying structure and relationships that are shown visually must also be in the code. Headings must be real headings, lists real lists, tables real tables and labels connected to their fields. It's one of the most broadly failed rules, because any visual structure built with plain `<div>` and CSS fails it.

## 254: Why was WCAG 4.1.1 Parsing removed in 2.2?

4.1.1 required valid HTML without things like duplicate attributes or bad nesting, because old assistive technology parsed HTML itself and broke on errors. Modern browsers fix up broken HTML in a standard way and assistive technology reads the browser's accessibility tree, so the rule no longer caught real user problems. W3C marked it obsolete in WCAG 2.2 and also updated 2.0 and 2.1 to say it is always met. Duplicate ids can still break ARIA references, but that is now covered by other criteria like 1.3.1 and 4.1.2.

## 255: What is WCAG 2.4.3 Focus Order and how do you fail it?

It is a Level A rule saying focus must move in an order that keeps meaning and makes the page usable. You fail it with positive tabindex values, with CSS that reorders content visually, with dialogs that are added at the end of the DOM but not focused, or with focus jumping back to the top after an action. Test by tabbing through and watching where focus goes.

## 256: What are common reasons an accessible name is missing?

Icon buttons without a label, inputs with only a placeholder, images inside links with empty `alt` (so the link has no name), `aria-labelledby` pointing to an id that doesn't exist and custom elements with no text. axe flags most of these as "buttons must have discernible text" or "form elements must have labels".

## 257: What is wrong with this code: an image link with alt=""?

When an image is the only content of a link, the image's alt text becomes the link's name. With `alt=""`, the link has no name, and screen readers read the URL instead. The alt text should describe where the link goes, like "Home" for a logo that links to the home page.

```html
<!-- Bad -->
<a href="/"><img src="logo.svg" alt="" /></a>

<!-- Good -->
<a href="/"><img src="logo.svg" alt="Acme home" /></a>
```

## 258: How do you write alt text for a linked logo?

Describe the link's destination and, if needed, the company name. For a logo linking to the home page, "Acme home" or just "Acme" works. You don't need to describe the logo's colors or shapes, and you shouldn't add "logo" unless it helps.

## 259: How do you handle repeated "Read more" links?

Either change the visible text to be specific, or add hidden context so each link has a unique accessible name. You can use visually hidden text, or `aria-labelledby` combining the link and the article title. Keep the visible text inside the name so voice control still works.

```html
<a href="/posts/caching"
  >Read more<span class="sr-only"> about caching strategies</span></a
>
```

## 260: How do you make a card component with a link accessible?

Don't wrap the whole card in an `<a>`, because the screen reader then reads all the card's content as one long link name. Put the link on the title, and if you want the whole card to be clickable, stretch the link's click area with a pseudo-element that covers the card. Other buttons inside the card can sit above it with `position: relative` and a higher `z-index`.

```css
.card {
  position: relative;
}
.card h3 a::after {
  content: "";
  position: absolute;
  inset: 0;
}
```

## 261: Why should headings not be used just for styling?

Screen reader users use headings to scan and jump around, so a paragraph styled as a heading, or a heading used only to make text big, gives them a false map of the page. Use heading elements only for real section titles. Style other text with CSS classes.

## 262: How do you build a heading structure for a complex page?

Start with one `<h1>` for the page topic. Use `<h2>` for each main section, including sidebars or footer blocks if they have titles, and `<h3>` for subsections. Look at the page with a heading outline tool, like the HeadingsMap extension or WAVE's structure view, and check that it reads like a table of contents.

## 263: How do you make a search results page accessible?

Announce the number of results in a polite live region, like "24 results for shoes". Give the results list a heading users can jump to. Make filters accessible form controls in a `<search>` or labeled region, and after applying filters, update the count and either keep focus on the filter or move it to the results heading in a predictable way.

## 264: What is the problem with "click here" style instructions?

They assume a mouse and vision, and the link text means nothing when read out of context. They also make lists of links useless for screen reader users. Write the action as the link, like "Download the 2026 annual report (PDF, 2 MB)", which also tells users what to expect.

## 265: Should links to files mention the file type and size?

Yes, it is good practice. A user on a slow connection or a screen reader user may want to know a link opens a PDF before clicking. Put it in the link text, like "Annual report (PDF, 2 MB)". It's also worth making the PDF itself accessible, or providing an HTML version.

## 266: What makes a PDF accessible?

An accessible PDF is "tagged", meaning it has a hidden structure of headings, lists, tables and reading order, plus alt text for images, a document title and a language. Scanned PDFs with no real text are not accessible unless OCR is done. The PDF/UA standard defines the rules, and tools like Adobe Acrobat's checker or PAC can test it. Often an HTML page is easier to make accessible than a PDF.

## 267: How do you make a canvas element accessible?

A `<canvas>` is just pixels, so assistive technology sees nothing inside it. Put fallback content between the `<canvas>` tags, which is exposed to screen readers, give the canvas a role and label if it is an image, or provide an equivalent HTML version alongside it. For interactive canvas apps, you need to build a parallel DOM structure that mirrors what's drawn.

```html
<canvas
  id="chart"
  role="img"
  aria-label="Bar chart of visitors per day, table below"
></canvas>
```

## 268: How do you make charts accessible?

Give each chart a short text summary of the key point, provide the data as a table, use patterns or labels in addition to color, and keep a 3:1 contrast for lines and bars. Many chart libraries, like Highcharts, have accessibility modules that add keyboard navigation and screen reader descriptions. Don't rely on hover tooltips as the only way to read values.

## 269: How do you make an interactive map accessible?

Maps are hard, so the main thing is to offer the same information another way, like a list of locations with addresses and directions. Make map controls keyboard accessible with zoom buttons, label markers, and don't trap keyboard focus inside the map. Mapping libraries vary a lot in their keyboard support, so test the one you pick.

## 270: How do you write an accessibility bug report?

Include the page and component, steps to reproduce, the assistive technology and browser used, what happened and what should happen, and the WCAG criterion it fails. Add severity or user impact, like "blocks screen reader users from checking out". A screenshot or a short recording of the screen reader output helps developers understand quickly.

## 271: How do you prioritize accessibility issues?

Look at user impact first: issues that block a task, like an unlabeled checkout button, come before annoyances like a redundant link. Then consider how many users and pages are affected, whether the problem is on a key journey, and how hard the fix is. Fixing shared components, like a design system button, often fixes hundreds of issues at once.

## 272: What is an accessibility audit?

An audit is a structured review of a site against a standard, usually WCAG 2.2 AA. It combines automated scans with manual and assistive technology testing on a sample of pages and user journeys. The result is a report listing each issue, the failed criterion, severity and how to fix it. W3C's WCAG-EM is a common method for choosing the sample and reporting results.

## 273: How do designers help with accessibility before development?

Designers can choose colors that pass contrast, design visible focus states, label every field, plan heading structure and landmarks, define reading order, specify alt text and design error states. Annotating these in the design file, for example with an accessibility annotation kit, means developers don't have to guess. Fixing issues at design time is much cheaper than after release.

## 274: How do design systems help accessibility?

When a design system's components, like buttons, dialogs, form fields and tabs, are built and tested to be accessible, every product that uses them gets that for free. Bugs are fixed once and the fix spreads everywhere. The system's docs should also explain how to use each component accessibly, since a good component can still be used wrongly, for example with a missing label.

## 275: What is the difference between accessibility testing tools that run on code and those that run on the page?

Code tools, like eslint-plugin-jsx-a11y, check source files and catch problems early, but they can't see the final DOM or styles. Page tools, like axe, WAVE or Lighthouse, check the rendered page in a browser, so they can test contrast, the accessibility tree and the result of JavaScript. You want both, plus manual testing.

## 276: How do you handle accessibility for third-party widgets?

Test the widget before you choose it, ask the vendor for an ACR or VPAT and include accessibility requirements in the contract. If you're stuck with an inaccessible widget, provide an alternative way to do the same task and report the issue to the vendor. Your site is still responsible for the experience, even if the code isn't yours.

## 277: What are skip links for besides "skip to main content"?

Skip links can also jump past long repeated blocks, like a big filter sidebar or an embedded widget, or go to the search box. Keep them few, and make sure every target exists and can receive focus. Many modern sites only need the one link to the main content because landmarks handle the rest for screen reader users, but sighted keyboard users can't use landmarks without extra tools.

## 278: How do you make a skip link visible on focus?

Hide it visually by default and show it when it gets focus. Make sure the target element can receive focus, usually by using `<main id="main" tabindex="-1">`, so the next Tab continues from the main content in all browsers.

```css
.skip-link {
  position: absolute;
  left: -9999px;
}
.skip-link:focus {
  left: 1rem;
  top: 1rem;
  z-index: 1000;
  background: #fff;
  padding: 0.5rem 1rem;
}
```

## 279: How do you announce the number of characters left in a text area?

Show the count visually and connect it with `aria-describedby`, but don't announce it on every keystroke, which would be noisy. A common approach is to update a polite live region only at certain points, like when 20 characters are left, or after the user stops typing for a moment (a debounce). The GOV.UK character count component is a good reference.

## 280: How do you make an accessible password field with a show password button?

Use a normal `<input type="password">` with a label, plus a `<button type="button">` that switches the type between `password` and `text`. Give the button a clear name, like "Show password", and either toggle `aria-pressed` or change the label to "Hide password". Don't block paste in the password field, because password manager users need it.

## 281: How do you make a multi-step form accessible?

Show the current step and total number of steps, like "Step 2 of 4", and mark the step indicator with `aria-current="step"`. When the user moves to the next step, update the page title and move focus to the step heading. Keep data when users go back, and don't use time limits without a way to extend them.

## 282: How do you warn users about a session timeout?

Show a dialog before the session ends, like at the 2-minute mark, that tells them how much time is left and lets them extend it with one button. Move focus into the dialog so screen reader users hear it. WCAG 2.2.1 Timing Adjustable requires at least 20 seconds to respond. Also save their data if possible, so nothing is lost if the session does expire.

## 283: How do you make CAPTCHA-free spam protection?

Use honeypot fields (hidden from everyone, including screen readers, with `display: none`), server-side rate limiting, time checks on form submits and invisible risk scoring services like Cloudflare Turnstile or reCAPTCHA v3. These protect forms without asking users to solve puzzles. If you must show a challenge, offer more than one type and a way to contact a person.

## 284: Why should you allow paste in form fields?

Blocking paste breaks password managers and forces users to type long codes or passwords by hand. That is hard for people with motor and memory disabilities, and it fails WCAG 3.3.8 Accessible Authentication when it blocks the help those users depend on. There is no real security benefit to blocking paste, so don't do it.

## 285: How do you make one-time codes easier for everyone?

Use a single input with `autocomplete="one-time-code"` and `inputmode="numeric"`, so phones can fill the code from the SMS automatically. Avoid splitting the code into six separate boxes, which confuses screen readers and often breaks paste. Give enough time to enter the code and a clear way to resend it.

```html
<label for="otp">Verification code</label>
<input id="otp" inputmode="numeric" autocomplete="one-time-code" />
```

## 286: Are passkeys good for accessibility?

Yes, mostly. Passkeys let users log in with their device unlock, like a fingerprint, face or PIN, instead of remembering a password, which helps people with memory and cognitive disabilities. They meet WCAG 3.3.8 easily. Keep a fallback login method, because not everyone can use biometrics or has a compatible device.

## 287: How do you make inline editing (like click to edit) accessible?

Show a real button, like "Edit name", rather than making plain text clickable. When editing starts, move focus to the input; when it is saved or cancelled, move focus back to the button and announce the result if needed. Escape should cancel the edit. Hover-only edit icons are invisible to keyboard and touch users.

## 288: What accessibility problems do hover-only interactions cause?

Content or controls that only appear on hover can't be reached by keyboard users, touch screen users or many screen reader users. Common examples are action buttons on table rows and dropdown menus. Show them on focus too, with `:focus-within`, or make them visible all the time.

## 289: How do you check a site at 400% zoom?

Set the browser window to 1280 pixels wide and zoom to 400%, or set the window to 320 pixels wide at 100%. Check that content reflows into one column, that nothing is cut off, that sticky headers don't cover most of the screen and that you don't need to scroll sideways to read text. Fixed headers taking half the screen at high zoom is a common failure.

## 290: How do you test text spacing?

Use a bookmarklet or browser extension that applies the WCAG 1.4.12 values: line height 1.5, paragraph spacing 2em, letter spacing 0.12em and word spacing 0.16em. Then look for text that gets cut off or overlaps. Containers with fixed heights or `overflow: hidden` are usually the cause.

## 291: How do you simulate color blindness while designing?

Chrome DevTools has a "Rendering" tab where you can emulate several types of color vision deficiency and blurred vision. Firefox's Accessibility Inspector has similar options, and Figma has plugins for it. It's a quick way to check whether charts, status colors and links are still clear.

## 292: Should links be underlined?

In body text, underlines are the clearest way to show a link without depending on color. If links aren't underlined, WCAG technique G183 says the link color needs a 3:1 contrast with the surrounding text, plus a non-color indicator like an underline on hover and focus. In navigation menus, where everything is clearly a link, underlines are not needed.

## 293: How do you handle text over images?

Text on top of photos often fails contrast because the photo has both light and dark areas. Add a solid or semi-transparent overlay behind the text, a text shadow or a solid background box. Check contrast against the lightest part of the image that sits behind the text, and remember the crop changes on different screen sizes.

## 294: How do you announce changes in a shopping cart?

When an item is added, announce it in a `role="status"` region, like "Running shoes added to cart. 3 items in cart." Update the cart button's accessible name too, for example "Cart, 3 items". Don't move focus to the cart unless the user asked to go there, because they probably want to keep shopping.

## 295: How do you make a "back to top" button accessible?

Make it a link to `#top` or a button that scrolls and also moves focus to the top of the page, such as the skip link or the `<h1>`. Scrolling without moving focus leaves keyboard users at the bottom, so the next Tab takes them back down. Give it clear text, not only an arrow icon.

## 296: What is the purpose of the aria-describedby on a dialog?

It connects the dialog's main message to the dialog, so some screen readers read it when the dialog opens along with the name. It's useful for short confirmation dialogs where the message is the most important part. For dialogs with lots of content, like a form, don't describe the whole thing, because it would all be read at once.

## 297: How do you make a toolbar accessible?

Use `role="toolbar"` with an `aria-label` on a container of controls, like the formatting buttons in an editor. The whole toolbar is one Tab stop, and arrow keys move between buttons using a roving tabindex. Toggle buttons inside use `aria-pressed`. This keeps the tab order short when there are many controls.

## 298: How do you make a tree view accessible?

Use `role="tree"` with `role="treeitem"` nodes, nested groups with `role="group"`, and `aria-expanded` on parent nodes. Up and Down arrows move between visible items, Right opens a node or moves into it, Left closes it or moves to the parent. It's a complex pattern; for simple nested navigation, a list of links with disclosure buttons is often better.

## 299: What should an accessibility statement include?

It should state the standard you aim for (like WCAG 2.2 AA), how well you meet it, known issues and workarounds, the date it was last reviewed, and how users can report problems or ask for content in another format. EU public sector statements also need a link to the enforcement procedure. Keep it honest; claiming full compliance without testing can create legal risk.

## 300: How do you explain the business case for accessibility to a manager?

Cover the market size, since people with disabilities and their families have huge spending power, and legal risk from lawsuits and laws like the EAA and ADA. Add better SEO, better mobile usability, fewer support calls and the lower cost of building it in early instead of fixing it later. Many contracts, especially public sector ones, also require it.

# Advanced Questions (301-450)

## 301: How does information get from your HTML to a screen reader?

The browser parses HTML into the DOM, applies CSS, and builds an accessibility tree from both. It then exposes that tree through the operating system's accessibility API. The screen reader queries that API, listens for events like focus changes and live region updates, and turns the result into speech or braille. Your code never talks to the screen reader directly.

## 302: What are the platform accessibility APIs?

Each operating system has its own API: Microsoft UI Automation (UIA) and the older MSAA and IAccessible2 on Windows, NSAccessibility (the AX API) on macOS, UIAccessibility on iOS, AT-SPI on Linux, and the Android accessibility framework. Browsers map the same HTML and ARIA to each of these differently. This is one reason the same page can sound different in NVDA, JAWS and VoiceOver.

## 303: What are the Core-AAM and HTML-AAM specs?

They are W3C "Accessibility API Mappings" specs. Core-AAM says how each ARIA role, state and property maps to each platform API. HTML-AAM does the same for HTML elements and attributes, for example how `<nav>` becomes the navigation role on each platform. Browser engineers implement these, and they're the best place to check when you wonder why something is exposed a certain way.

## 304: Why can the same page sound different in different screen readers?

There are several layers that can differ: how the browser maps HTML and ARIA to the platform API, how complete that API is, and how each screen reader chooses to present the information. Screen readers also have their own heuristics, verbosity settings and bugs. That is why a pattern that's fine in NVDA with Chrome might be confusing in VoiceOver with Safari, and why testing several combinations matters.

## 305: Which elements are left out of the accessibility tree?

Elements hidden with `display: none`, `visibility: hidden`, the `hidden` attribute, `aria-hidden="true"` or inside an `inert` subtree are removed. Browsers also prune many generic containers like plain `<div>` and `<span>` that add no meaning, which is why the accessibility tree is much smaller than the DOM. Elements with `role="none"` or `role="presentation"` lose their own node but keep their children.

## 306: How does the accessible name computation work for an element with nested content?

When the name comes from content (allowed for roles like button, link, heading, cell and option), the browser walks the child nodes in order and joins their text. For each child it recursively applies the same rules, so a child with `aria-label` uses that label and an `<img>` uses its `alt`. Hidden children are skipped unless the walk started from an `aria-labelledby` reference. CSS generated content is included, and block-level elements may add spaces.

## 307: Can aria-labelledby reference hidden elements?

Yes. If `aria-labelledby` points to an element hidden with `hidden` or `display: none`, its text is still used for the name. This lets you keep a label in the DOM but not show it. However, the hidden element's own hidden children may be treated differently by different browsers, so keep hidden labels simple text.

## 308: Why doesn't aria-label work on a div or span?

The ARIA spec prohibits naming elements with the `generic` role, which is the role of plain `<div>` and `<span>`. Browsers and screen readers often ignore `aria-label` there, and axe flags it. If the element needs a name, it needs a real role first, like `role="group"` or `role="img"`, or you should put the text in visible content.

## 309: Which roles cannot get their name from content?

Roles like `textbox`, `listbox`, `combobox`, `tablist`, `tree`, `grid`, `dialog`, `navigation`, `region` and `img` cannot be named from their contents. They need a name from `aria-labelledby`, `aria-label` or a native label. That's why a `<nav>` with links inside still needs `aria-label` if you want it named, and why an `<input>` doesn't get its name from its value.

## 310: How is the accessible description computed?

The description comes first from `aria-describedby`, then from `aria-description` (new in ARIA 1.3 and already supported in Chromium and Firefox), then from native sources like the `title` attribute if it wasn't used for the name. Some elements have extra sources, like a `<table>` getting its description from `<caption>` when the caption isn't used as the name. Screen readers usually read the description after the name, role and state.

## 311: What is the difference between browse mode virtual buffers and the live DOM?

Windows screen readers like NVDA and JAWS build a "virtual buffer", a flat copy of the page they read from in browse mode. Updates to the DOM have to reach the buffer before the user hears them, and very large or fast-changing pages can make the buffer slow or out of date. VoiceOver on macOS doesn't use a virtual buffer in the same way, which is another reason behavior differs.

## 312: What does role="application" do and why is it risky?

`role="application"` tells Windows screen readers to switch to focus mode and pass all keys straight to the page. Users lose their normal reading shortcuts like H for headings, so you must handle every key and announce everything yourself. It only makes sense for complex apps like spreadsheets or editors that have their own full keyboard model, and even then usually only on a part of the page.

## 313: Roving tabindex versus aria-activedescendant: how do you choose?

Roving tabindex moves real DOM focus, so `:focus` styles, `scrollIntoView` and screen reader focus tracking work naturally, and support is very solid. `aria-activedescendant` keeps focus on a container or input and only changes an attribute, which is needed when focus must stay in a text input, like a combobox. With activedescendant you must draw the highlight and scroll it into view yourself, and support has historically been weaker on some screen readers, especially VoiceOver on iOS.

## 314: How do you build an accessible data grid?

Use `role="grid"` with `row`, `columnheader`, `rowheader` and `gridcell`. The grid is one Tab stop, and arrow keys move between cells using roving tabindex. Enter or F2 starts editing a cell and Escape returns to grid navigation. If the grid is just for reading data and doesn't need cell-level interaction, a normal `<table>` is better, because screen reader table commands work on it without any special handling.

## 315: When should you use a table instead of role="grid"?

Use a table when users mostly read data, even if some cells contain links or buttons. A grid changes the keyboard model: users can no longer Tab through links and screen readers switch to focus mode, which surprises people who just want to read. Use a grid only for spreadsheet-like experiences where cell-by-cell navigation and editing is the main job.

## 316: How do you make a virtualized list accessible?

Virtualized lists only render the visible rows, so screen readers don't know the full size. Set `aria-setsize` and `aria-posinset` on items in a list, or `aria-rowcount` and `aria-rowindex` on tables and grids, so users hear "row 501 of 10,000". Make sure keyboard navigation loads new rows and moves focus correctly, and that the focused row is never removed from the DOM. Also offer search or filtering, since nobody wants to arrow through 10,000 rows.

```html
<div role="grid" aria-rowcount="10000">
  <div role="row" aria-rowindex="501">...</div>
</div>
```

## 317: What happens to focus when a focused element is removed from the DOM?

The browser moves focus to the `<body>`, and screen readers may say nothing or jump to the top of the page. This often happens when deleting a list item, closing a component or re-rendering a list with new keys in React. Before removing a focused element, move focus to a sensible place, like the next item, the previous item or the list heading.

## 318: How should focus be managed after deleting an item from a list?

Move focus to the next item in the list, or the previous one if it was the last, and announce the result in a live region, like "Invoice 42 deleted". If the list is now empty, move focus to the list's heading or to the "Add item" button. Offer an undo option somewhere reachable, not only in a toast that disappears.

## 319: How do React re-renders cause accessibility bugs?

If keys change or a parent component is recreated, React replaces DOM nodes instead of updating them, and any focused element inside loses focus. Live regions that are mounted together with their content may not be announced. Conditional rendering that swaps a button for a different button, like "Edit" to "Save", also drops focus. Use stable keys, keep live regions mounted and manage focus explicitly.

## 320: How can hydration in server-rendered apps hurt accessibility?

Before hydration, the HTML is visible but buttons and widgets don't work yet, so a keyboard user may click a button that does nothing. If the server HTML and client HTML differ, React may re-render parts of the page and drop focus. Use progressive enhancement where possible, like real links and forms that work without JavaScript, and make sure ids generated with `useId` match between server and client.

## 321: How do you make accessible notifications that don't interrupt too much?

Use one shared polite live region for most messages, combine bursts of updates into one message and avoid announcing things the user didn't cause. Only use assertive announcements for errors that need attention. Keep the same messages available in a persistent place, like a notifications panel, because live region announcements are easy to miss and can't be replayed.

## 322: Why do some live region announcements get lost?

Common reasons are: the region was added at the same time as its text, the text didn't actually change (same message twice), the region is inside an element with `aria-hidden` or `display: none`, focus moved at the same moment and the screen reader announced that instead, or another assertive message interrupted it. Some teams clear the region and set the text after a short delay to force a repeat announcement.

```js
function announce(region, message) {
  region.textContent = "";
  setTimeout(() => {
    region.textContent = message;
  }, 100);
}
```

## 323: What is the ARIA ariaNotify API?

`ariaNotify()` is a newer API, proposed by Microsoft and shipped in Chromium-based browsers, that lets a page ask the screen reader to announce a string without building a live region. It is called on an element or the document, with options to set priority. It aims to fix the unreliable timing of live regions, but support is not universal yet, so keep a live region fallback.

```js
if ("ariaNotify" in document) {
  document.ariaNotify("File saved");
} else {
  statusRegion.textContent = "File saved";
}
```

## 324: How does shadow DOM affect ARIA references?

`aria-labelledby`, `aria-describedby`, `aria-controls` and `for` work by id, and ids don't cross shadow root boundaries. So a label outside a web component can't point to an input inside its shadow root, and the other way around. This is a big problem for design systems built with web components. Workarounds include keeping the label and input in the same shadow root or using element reflection.

## 325: What is ARIA element reflection?

Element reflection lets you set ARIA relationships with element references in JavaScript instead of id strings, for example `button.ariaLabelledByElements = [heading]`. It also includes string reflection like `element.ariaLabel = "Close"`. Element reflection can reference elements in a parent tree from inside a shadow root, which partly solves the cross-root problem. It is supported in modern Chromium, Safari and Firefox.

```js
const input = shadowRoot.querySelector("input");
const label = document.querySelector("#external-label");
input.ariaLabelledByElements = [label];
```

## 326: What is the reference target proposal for shadow DOM?

Reference target is a proposed web platform feature that lets a shadow host forward id references to an element inside its shadow root. For example, a `<label for="my-input">` pointing to a `<custom-input>` host would actually label the native `<input>` inside. It's being worked on in browsers but is not yet available everywhere, so you can't depend on it yet.

## 327: How do you give a custom element a role without adding attributes to the host?

Use `ElementInternals` with `attachInternals()` and set ARIA properties on it, like `internals.role = "checkbox"` and `internals.ariaChecked = "true"`. These are default semantics: users of the component can still override them by adding attributes on the host. This keeps the DOM clean and avoids "sprouting" attributes that surprise developers.

```js
class FancyCheckbox extends HTMLElement {
  #internals = this.attachInternals();
  connectedCallback() {
    this.#internals.role = "checkbox";
    this.#internals.ariaChecked = "false";
    this.tabIndex = 0;
  }
}
customElements.define("fancy-checkbox", FancyCheckbox);
```

## 328: What are form-associated custom elements and why do they matter for accessibility?

A custom element with `static formAssociated = true` can take part in forms through `ElementInternals`: it submits a value, takes part in validation and can be labeled by a `<label>` element. That means a native `<label for>` can name it and click-to-focus works, which isn't possible with a normal custom element. It's the best way to build accessible custom form controls with web components.

## 329: What does delegatesFocus do in shadow DOM?

When a shadow root is created with `delegatesFocus: true`, focusing the host, for example by clicking it or calling `focus()`, moves focus to the first focusable element inside the shadow root. The host also matches `:focus` when something inside it is focused. It helps components like custom inputs or buttons that wrap a native element behave like a single control.

```js
this.attachShadow({ mode: "open", delegatesFocus: true });
```

## 330: How do slots affect the accessibility tree?

Slotted content is rendered inside the shadow tree in the accessibility tree, so it is read in the visual, composed order, not the light DOM order. That's usually what you want. But because the slotted elements stay in the light DOM, ARIA references between slotted content and shadow content still can't use ids across the boundary.

## 331: How do you make a rich text editor accessible?

Editors are built on `contenteditable`, which screen readers support as a multi-line text field, but formatting, lists and embedded objects are hard to expose. Use a well-tested editor (like ProseMirror-based ones, Lexical or CKEditor) that has worked on accessibility, give the editable area a label and `aria-multiline="true"`, and keep a toolbar with `role="toolbar"`. Offer keyboard shortcuts and a way to leave the editor with the keyboard, since Tab may insert a tab character.

## 332: How do you handle the Tab key inside code editors and text areas?

Code editors often use Tab to indent, which can trap keyboard users. Good editors like CodeMirror 6 and Monaco provide a way out: CodeMirror doesn't bind Tab by default, and Monaco has a "Tab moves focus" toggle with Ctrl + M. Document the shortcut close to the editor, so keyboard users know how to leave.

## 333: How do canvas-based apps like Flutter web or Google Docs handle accessibility?

Apps that draw on `<canvas>` build a separate hidden DOM layer that mirrors the content for assistive technology. Flutter web has a "semantics" tree it turns into hidden HTML elements. Google Docs moved to canvas rendering and keeps an accessible DOM in parallel with a braille and screen reader mode. This is a lot of work and must be kept in sync, which is why canvas UIs are rarely as accessible as normal HTML.

## 334: How do you make a WebGL or game experience more accessible?

Offer remappable controls, adjustable speed and difficulty, captions for all speech and important sounds, visual cues for audio cues, colorblind-safe palettes and options to reduce motion and flashing. For screen reader support, expose key game state through a hidden DOM or live regions. The Game Accessibility Guidelines are a good practical reference.

## 335: How can you make data visualizations accessible beyond a data table?

Options include keyboard navigation through data points with announcements, a written summary of trends, sonification (turning values into sounds of different pitch), and letting users switch to a table view. Highcharts has sonification and keyboard navigation built in, and tools like Chartability give a checklist for auditing visualizations.

## 336: What is ARIA 1.3 and what does it add?

ARIA 1.3 is the next version of WAI-ARIA, still a Working Draft in 2026, while ARIA 1.2 is the current W3C Recommendation. It adds `aria-description`, `aria-braillelabel` and `aria-brailleroledescription`, roles like `suggestion`, `comment` and `mark` for editing and annotations, and `aria-details` improvements. Some features already work in browsers, but check support before depending on them.

## 337: What are aria-braillelabel and aria-brailleroledescription?

They let you give a shorter or different text for braille displays than for speech. Braille displays often show only 40 characters, so a long role or name wastes space. For example, a role description "slide" might become "sld" in braille. They are only meant to be used along with a normal `aria-label` or `aria-roledescription`, and support is still limited.

## 338: What is WCAG 3 and how is it different from WCAG 2?

WCAG 3 (W3C Accessibility Guidelines 3.0) is a new standard still in Working Draft as of 2026. It replaces pass/fail success criteria with "outcomes" that can be tested in different ways, includes cognitive accessibility and more types of content, and plans a scoring model with Bronze, Silver and Gold levels instead of A, AA, AAA. It is not expected to be final for a few years, and W3C says WCAG 2 is not being replaced by it any time soon.

## 339: Should you start following WCAG 3 now?

No for compliance, yes for learning. Laws and contracts point to WCAG 2.1 or 2.2, and WCAG 3 is still changing a lot between drafts. But its direction, especially more focus on cognitive accessibility and actual user outcomes, is useful thinking. Meeting WCAG 2.2 AA well is the best preparation.

## 340: What is the current legal status of web accessibility under the ADA in the US?

Title III of the ADA covers businesses open to the public, and US courts have often held that websites are covered, especially when linked to a physical location, though courts disagree on details. Thousands of web accessibility lawsuits are filed every year. For state and local governments, a 2024 Title II rule requires WCAG 2.1 AA, with deadlines that the DOJ extended in 2026 to April 2027 for larger entities and April 2028 for smaller ones.

## 341: What does the European Accessibility Act mean for a developer building an online store?

If the store sells to consumers in the EU and the company isn't a microenterprise (fewer than 10 employees and under 2 million euros turnover), the site and checkout must be accessible, which in practice means EN 301 549 and WCAG 2.1 AA. The company also needs to publish information about how the service meets the requirements. Each EU country enforces it with its own penalties, so it applies even to companies based outside the EU.

## 342: What is the difference between conformance and compliance?

Conformance is a technical term from WCAG: the page meets all the success criteria at a level. Compliance is a legal term: you meet the rules of a law, which may point to WCAG but may also include other duties like accessibility statements, feedback processes or procurement rules. A site can conform to WCAG and still miss legal duties, and laws may accept small issues if you are working on them.

## 343: Why are accessibility overlays legally risky?

Overlays claim to make sites compliant, but they don't fix the source code, so the actual barriers stay. Many companies using overlays have been sued, and some lawsuits target the overlay itself. The FTC's 2025 order against accessiBe for deceptive claims shows regulators also see the marketing as misleading. Disabled users often report that overlays get in their way.

## 344: How would you design an accessibility program for a large company?

Set a clear policy (like WCAG 2.2 AA), get leadership support and name owners. Build accessibility into the design system, add automated checks in CI, train designers, developers and QA, and include manual and assistive technology testing in the release process. Track metrics over time, include accessibility in procurement and hire or work with disabled testers. The W3C's maturity model gives a structure for this.

## 345: What does "shift left" mean for accessibility?

It means finding accessibility problems as early as possible: in requirements, design and code review, instead of in an audit after launch. A missing label is a one-line fix during coding but can take weeks to schedule after release. Practices include accessibility acceptance criteria in tickets, design annotations, linting, component tests and accessible design system components.

## 346: How do you write accessibility acceptance criteria for a user story?

Make them specific and testable, based on the component. For example: "The dialog opens with focus on the heading, traps focus, closes on Escape and returns focus to the trigger; the delete button has the accessible name 'Delete invoice 42'; error messages are announced." Link them to WCAG criteria and the APG pattern so testers know what to check.

## 347: What accessibility metrics are useful to track?

Useful ones include the number of open accessibility bugs by severity, the time to fix them, automated violation counts per page over time, the share of components in the design system that passed manual testing, and audit results on key journeys. User feedback and task success rates with disabled testers matter more than any automated score. Be careful with "Lighthouse score" targets, because teams can hit 100 while key flows still fail.

## 348: Why should you test with disabled users and not only with tools?

Tools and checklists find technical failures, but they don't tell you if a real person can finish a task. Disabled users have their own settings, strategies and expectations that developers testing with a screen reader for an hour don't have. User testing often finds problems with confusing flows, overly long announcements or patterns that pass WCAG but are still frustrating.

## 349: What are the limits of WCAG?

WCAG focuses on technical criteria that can be tested, so many usability problems for disabled people aren't covered, especially for cognitive and learning disabilities. A site can pass every criterion and still be hard to use. Some criteria are open to interpretation, and different auditors may disagree. Treat WCAG as a minimum baseline, not the goal.

## 350: How do you handle accessibility in a design system's component API?

Make the accessible way the easy way. For example, require a `label` prop on form fields, make an icon-only button fail to compile without an `aria-label`, generate ids automatically and connect labels, hints and errors inside the component. Document keyboard behavior and screen reader output for each component, and test components with assistive technology before release.

```tsx
type IconButtonProps = {
  icon: React.ReactNode;
  label: string; // required, becomes the accessible name
  onClick: () => void;
};

export function IconButton({ icon, label, onClick }: IconButtonProps) {
  return (
    <button type="button" aria-label={label} onClick={onClick}>
      <span aria-hidden="true">{icon}</span>
    </button>
  );
}
```

## 351: What are headless UI libraries and how do they help accessibility?

Headless libraries like React Aria, Radix UI, Headless UI and Ariakit provide the behavior, ARIA and keyboard handling of complex widgets without any styling. You add your own look on top. They save you from building comboboxes, menus and dialogs from scratch, which is where most custom accessibility bugs come from. React Aria in particular has tested support across many screen readers and devices.

## 352: What are the risks of using component libraries for accessibility?

A library may claim accessibility but have gaps, may be tested only with one screen reader, or may allow you to use it in an inaccessible way, like an icon button without a label. Library updates can also break behavior you rely on. Review the library's accessibility docs and open issues, test it yourself on your key flows and pin versions you have tested.

## 353: How do you make an autocomplete with async results accessible?

Use the combobox pattern with `aria-expanded`, `aria-controls`, `aria-activedescendant` and a listbox. When results arrive, announce the count in a polite live region, like "5 suggestions available", with a debounce so it isn't announced on every keystroke. While loading, show and announce a loading state. Don't move focus into the list automatically; let users arrow down.

## 354: What makes combobox implementation so hard?

The pattern changed several times across ARIA versions (1.0, 1.1 and 1.2 all used different structures), and screen readers still support it differently. You must keep focus in the input, track the active option with `aria-activedescendant`, scroll it into view, handle selection and Escape, filter as the user types and announce results. Mobile screen readers behave differently again. Use the ARIA 1.2 pattern and a tested library when you can.

## 355: How does iOS VoiceOver differ from desktop screen readers in interaction?

On iOS, users swipe left and right to move through elements and double-tap to activate, so there are no keyboard events for most actions. Elements must respond to the activation that VoiceOver sends as a click. Custom gestures, hover states and keyboard-only handlers don't work. `aria-activedescendant` and some live region behaviors have historically been weaker on iOS, so test with an actual iPhone.

## 356: How does TalkBack differ from VoiceOver?

TalkBack on Android also uses swipes and double-tap, but its gestures and reading controls are different, and it is paired with Chrome instead of Safari, so the browser's accessibility mapping differs. Some ARIA roles and states are announced differently or not at all. Android users also often use hardware keyboards and switch access. Test both platforms separately; passing on one doesn't prove the other.

## 357: How do you make a custom component work with mobile screen readers?

Use native elements whenever possible, because mobile screen readers support them best. Make sure every action happens on `click`, not on key events or `touchstart`, since screen reader activation sends a click. Avoid hidden elements that become focusable when swiping, give touch targets enough size and test with VoiceOver on iOS and TalkBack on Android.

## 358: Why should you avoid detecting screen readers?

There is no reliable way to detect them, and trying to do so raises privacy concerns, because it reveals that a user has a disability. Sites that serve a separate "accessible version" based on detection usually give a worse experience and fall behind the main site. Build one site that works for everyone instead.

## 359: How can user preference media queries be a privacy problem?

Media queries like `prefers-reduced-motion`, `prefers-contrast` and `forced-colors` can be read by JavaScript and used as part of a browser fingerprint. They may also hint at a disability. Browsers try to limit this, but developers should only use these settings to adapt the interface, never send them to analytics or tracking.

## 360: How can accessibility features be abused for SEO or security attacks?

Some sites hide keyword-stuffed text with sr-only classes or `aria-label` to try to rank better, which harms screen reader users and is against search engine rules. Attackers can also use hidden text or misleading accessible names to trick screen reader users, like a button that looks like "Cancel" but is named "Confirm payment". The rule is simple: the accessible name and the visual label should match.

## 361: What are the security concerns with accessibility services on mobile?

On Android, accessibility services can read the screen and act on behalf of the user, so malware often asks for accessibility permissions to steal data. That's why Android restricts which apps can use these APIs. For web developers, the lesson is that sensitive data on screen can be read by assistive tech, which is expected, and that you shouldn't block assistive technology to "protect" content.

## 362: How do performance problems affect accessibility?

Very large DOMs make the accessibility tree huge and can make screen readers slow, especially when building virtual buffers. Heavy JavaScript makes interfaces lag, which hurts people using switches or voice control even more. Frequent DOM updates, like a live clock updating every second, can flood screen readers with events. Smaller DOMs, virtualization and fewer updates help everyone.

## 363: How do layout shifts affect users with disabilities?

When content moves while loading, screen magnifier users lose their place, people with motor disabilities click the wrong thing and screen reader focus may jump. Reserve space for images, ads and embeds with `width`, `height` or `aspect-ratio` so layout stays stable. This also improves the Cumulative Layout Shift (CLS) Web Vital.

## 364: What are the accessibility issues with internationalization?

Each language needs the right `lang` attribute so screen readers pronounce it correctly. Right-to-left languages need `dir="rtl"` and layouts that mirror properly, including focus order. Translated text can be longer and break fixed-size containers, and translated alt text and `aria-label` values are often forgotten. Date, number and name formats also affect form labels and validation messages.

## 365: How do you handle aria-label translations?

`aria-label` values are often hard-coded in components and missed by translation tools. Google Translate and other browser translators may not translate `aria-label` either, while they do translate visible text. Prefer visible text or `aria-labelledby` pointing to visible text, and include all ARIA strings in your translation files.

## 366: How do you check that a translated site stays accessible?

Run automated checks on each locale, since translation can break contrast (different fonts), label connections or `lang` attributes. Review alt text and ARIA strings in each language. Test right-to-left layouts with the keyboard to check focus order and arrow key direction, because arrow keys in components like tabs should follow the visual direction.

## 367: How do you make dynamic content changes accessible when there is no user action?

Changes the user didn't start, like new messages, price updates or a stock alert, should be announced only if they matter, with a polite live region. Give users control over frequent updates, like a "pause updates" button for a live feed. WCAG 2.2.4 Interruptions (AAA) suggests letting users postpone or suppress them, except for emergencies.

## 368: How do you design accessible chat interfaces?

Use `role="log"` for the message area so new messages are announced politely in order, and label each message with the sender. Keep the input labeled and don't move focus to new messages. Announce typing indicators sparingly or not at all. For AI chat with streaming responses, announce the complete answer when it's done instead of every word as it streams, which would be very noisy.

## 369: How do you make streaming AI responses accessible?

Streaming text into a live region causes screen readers to announce chunks repeatedly or out of order. A better approach is to keep the streaming area out of the live region, announce "Response is being generated" at the start, and announce or focus the full response when it is complete. Give users a way to stop generation and keep focus on the input so they can continue.

## 370: What accessibility problems do cookie consent banners cause?

Banners often appear at the end of the DOM, so keyboard users reach them last, or they cover content without being modal, which fails Focus Not Obscured. Some block the page but don't trap focus or have unlabeled buttons. Put the banner early in the DOM or make it a real dialog, give it a heading and labeled buttons, and make sure "Reject" is as easy to reach as "Accept".

## 371: How do sticky elements cause accessibility failures at zoom?

At 200% or 400% zoom, a sticky header and footer can cover most of the screen, leaving very little room for content and hiding focused elements. This fails WCAG 2.4.11 and 1.4.10. Make sticky elements non-sticky at small viewport heights with a media query, or shrink them.

```css
@media (max-height: 500px) {
  .site-header {
    position: static;
  }
}
```

## 372: What is the problem with fixed-position chat widgets?

They often cover content and focused elements in the bottom corner, especially at high zoom or on small screens. Their launch buttons may lack names, and the chat window may not manage focus. When choosing a vendor, test their widget with keyboard and screen reader, and make sure it can be minimized and doesn't cover form buttons.

## 373: How do you test that focus is not obscured?

Tab through the page with sticky headers, footers, cookie banners and chat widgets visible, and check that each focused element is at least partly visible (AA) or fully visible (AAA). Repeat at 200% and 400% zoom and on mobile sizes. Automated tools mostly can't detect this, so it needs manual checking.

## 374: What is the WCAG-EM methodology?

WCAG-EM (Website Accessibility Conformance Evaluation Methodology) is a W3C guide for evaluating a whole website. It has five steps: define the scope, explore the site, select a representative sample of pages and states, audit the sample and report the findings. It makes audits more consistent and repeatable, especially for large sites where testing every page isn't practical.

## 375: How do you pick a representative sample of pages for an audit?

Include the home page, login, key templates (product, article, search results, listing), all steps of important processes like checkout or sign-up, pages with forms, media, tables and complex widgets, error states, and a few random pages. For apps, include each unique screen state, like empty, loading and error. A complete process must be tested end to end, because WCAG conformance applies to the whole process.

## 376: How do you test a single page app's states that automated scanners miss?

Automated scanners only check the state they load, like the page before any interaction. Script the important states in Playwright (open the menu, open the dialog, trigger validation errors, show the empty state) and run axe after each one. Combine that with manual keyboard and screen reader checks of transitions, since scanners can't judge focus movement or announcements.

```js
test("checkout errors are accessible", async ({ page }) => {
  await page.goto("/checkout");
  await page.getByRole("button", { name: "Place order" }).click();
  const results = await new AxeBuilder({ page }).analyze();
  expect(results.violations).toEqual([]);
  await expect(page.getByRole("alert")).toContainText("There is a problem");
});
```

## 377: What are Playwright ARIA snapshots?

ARIA snapshots, added in Playwright 1.49, let you assert the accessibility tree of a part of the page as YAML, using `toMatchAriaSnapshot()`. They check roles, names and structure, so a test fails if a heading level changes or a button loses its name. They are a good way to lock down the accessible structure of components and pages.

```js
await expect(page.getByRole("navigation", { name: "Main" }))
  .toMatchAriaSnapshot(`
  - navigation "Main":
    - link "Home"
    - link "Pricing"
`);
```

## 378: Can you automate screen reader testing?

Partly. Tools like Guidepup can drive real VoiceOver and NVDA from test scripts and record what they say, and the W3C ARIA-AT project tests how screen readers support APG patterns. These are useful for regression testing important flows, but they are slow and flaky compared to normal tests. Manual testing by people who know screen readers is still needed.

## 379: How do you handle axe false negatives and false positives?

axe aims to avoid false positives, so a reported violation is almost always real, though it can be wrong about contrast on gradients or images. It marks things it can't decide as "incomplete" (needs review), and those must be checked by hand rather than ignored. A clean axe run tells you nothing about focus order, alt text quality or keyboard behavior of custom widgets.

## 380: How do you deal with a large backlog of accessibility issues on a legacy site?

Start with an audit of key user journeys to find blockers, and fix those first. Group issues by root cause, since many come from a few shared components or templates. Add automated checks to stop new issues, publish an accessibility statement with known issues and a contact, and plan the rest in regular sprints with clear owners. Rebuilding everything at once usually fails.

## 381: Scenario: a user reports they can't complete checkout with a screen reader. How do you investigate?

Get details from the user if possible: screen reader, browser, device and where they got stuck. Reproduce it with the same setup, walking through the checkout with only the keyboard and screen reader. Look for unlabeled fields, errors that aren't announced, focus lost after async steps, inaccessible payment iframes and custom dropdowns. Fix it, ask the user to confirm and add a test for that flow.

## 382: Scenario: focus disappears after closing a modal in your React app. What are possible causes?

The trigger button may have been re-rendered or unmounted while the modal was open, so the saved reference points to a removed node. The modal may close by unmounting without restoring focus, or the restore code may run before the trigger is back in the DOM. Fix it by storing a stable reference, restoring focus in a cleanup effect after the DOM settles, or by using a library or native `<dialog>` that handles it.

## 383: Scenario: a dropdown works with NVDA but not with VoiceOver on iOS. What do you check?

Check if the dropdown depends on keyboard events, which iOS VoiceOver doesn't send, or on hover. Check if it uses `aria-activedescendant`, which has weaker support there. Check if the options are hidden in a way VoiceOver still reaches, or if the popup is outside the swipe order because it's in a portal. Often replacing it with a native `<select>` on mobile is the most reliable fix.

## 384: Scenario: your design team wants light gray placeholder-style labels for a clean look. What do you say?

Explain that labels must meet 4.5:1 contrast and must stay visible after typing, and that placeholder-only fields fail several WCAG rules and are hard for people with memory or vision problems. Offer options that still look clean, like a floating label that moves above the field and keeps good contrast, or a smaller label above the field. Show contrast numbers and examples of users struggling to make the case.

## 385: Scenario: a product manager wants an overlay tool because it's cheaper than fixing the site. How do you respond?

Explain that overlays don't fix the underlying code, that sites using them are still sued, that the FTC fined a major overlay vendor in 2025 for misleading claims, and that many disabled users dislike them. Propose a plan that targets the biggest barriers first, like fixing shared components and key journeys, so the cost is spread out. The real cost of an overlay is the risk it leaves in place.

## 386: Scenario: a chart dashboard must be accessible. How do you approach it?

Give each chart a heading and a text summary of its main insight, offer the data as a table (perhaps through a "View as table" toggle), and use patterns, labels and good contrast so color isn't the only cue. Make interactive filters standard form controls. Support keyboard navigation if users need to explore single data points, and make sure the dashboard reflows at 400% zoom.

## 387: Scenario: you must add a keyboard shortcut system to a web app. What accessibility rules apply?

Single-character shortcuts must be possible to turn off or remap (WCAG 2.1.4), and shortcuts shouldn't override common screen reader or browser keys. Use modifier keys where possible, ignore shortcuts while the user is typing in a field, and document them in a help dialog. Make every shortcut action also available through visible controls.

```js
document.addEventListener("keydown", (e) => {
  const typing = e.target.closest("input, textarea, [contenteditable]");
  if (typing || !settings.shortcutsEnabled) return;
  if (e.key === "/") {
    e.preventDefault();
    document.querySelector("#search").focus();
  }
});
```

## 388: Scenario: an infinite feed must stay, but you need it to be accessible. What do you do?

Use the `feed` role with `article` children that have `aria-setsize` (or `-1` if unknown) and `aria-posinset`, and set `aria-busy` while loading. Make sure the footer is reachable, for example by adding a "Skip to footer" link or pausing auto-loading when focus is near the end and offering a "Load more" button. The APG feed pattern also suggests Page Down and Page Up to move between articles.

## 389: Scenario: a form uses a third-party payment iframe. What can you control?

You can give the iframe a `title`, place it in a logical spot, label the fields around it and handle errors it returns in an accessible way on your side. The fields inside the iframe are controlled by the provider, so check their accessibility before choosing them; providers like Stripe Elements put real work into it. If their fields are inaccessible, report it and consider other providers.

## 390: Scenario: users with dyslexia say your docs site is hard to read. What changes can help?

Use a clear sans-serif font at a comfortable size, keep line length around 50 to 75 characters, use 1.5 line height, avoid justified text and long walls of text, and use headings, lists and short paragraphs. Make sure the site respects user font and spacing overrides. Plain language and good search also help a lot.

## 391: How should error messages be written for cognitive accessibility?

Say what went wrong and how to fix it, in plain words, near the field. "Enter a date in the format DD/MM/YYYY, like 05/03/2026" is better than "Invalid input". Don't blame the user, don't use error codes alone, and don't clear the fields they already filled. Keep the message visible until the error is fixed.

## 392: How do you reduce cognitive load in a complex form?

Ask only for what you need, group related fields, split long forms into steps with a progress indicator, use smart defaults and autocomplete, and explain why you need sensitive data. Show requirements before users make mistakes and save progress automatically. These help everyone, but especially people with cognitive disabilities, anxiety or low digital skills.

## 393: How do you make authentication flows accessible beyond passwords?

Allow password managers and paste, offer passkeys and magic links, support `autocomplete="one-time-code"` for codes, avoid puzzle CAPTCHAs, and give enough time for each step. For two-factor authentication, offer more than one method, since not everyone can use an authenticator app or receive SMS. Clear instructions and the ability to recover access without memory tests matter too.

## 394: How does WCAG apply to native mobile apps and hybrid apps?

WCAG is written for web content, but the W3C has guidance on applying it to non-web software and mobile (WCAG2ICT), and EN 301 549 applies similar rules to apps. For hybrid apps that use web views, the web content needs to follow WCAG directly, and the native shell needs to follow platform guidelines. Mobile screen readers and switch control expose web views through the platform's accessibility API.

## 395: How do you make emails accessible?

Use real text, not images of text, with alt text on images, enough contrast, a logical reading order and descriptive link text. Use `role="presentation"` on layout tables, which email still often needs, and set `lang` and a meaningful subject. Keep the content readable when images are blocked and test with screen readers in common email clients.

## 396: What is the relationship between SEO and accessibility?

They overlap a lot: search engines and screen readers both rely on text alternatives, headings, page titles, descriptive link text, transcripts and clean semantic HTML. Improving one often improves the other. But SEO tricks like hidden keyword text hurt accessibility, and some accessibility needs, like keyboard support, have nothing to do with SEO.

## 397: How do you handle the accessibility of dark patterns?

Dark patterns, like hidden unsubscribe links, low contrast "No thanks" buttons, pre-checked boxes and confusing double negatives, hit people with cognitive and vision disabilities hardest. Many of them also fail WCAG, like low contrast or unclear labels. Some laws, like the EU Digital Services Act and consumer protection laws, ban them separately. Treat them as both an ethics and an accessibility issue.

## 398: What is the difference between accessible and inclusive for content writers?

Accessible content can be read and understood with assistive technology, like correct headings, alt text and link text. Inclusive content also avoids language that excludes or offends, like ableist phrases, uses people-first or identity-first language as the community prefers, and gives examples that reflect different users. Both matter for a good experience.

## 399: How do you make custom scrollable regions keyboard accessible?

A `<div>` with `overflow: auto` and no focusable content can't be scrolled with the keyboard in some browsers. Make it focusable with `tabindex="0"`, give it a role like `region` and a name, and show a focus indicator. Chrome now makes scroll containers keyboard-focusable by default in many cases, but adding it yourself keeps it reliable everywhere.

## 400: How do you handle focus in a split view or master-detail layout?

When the user picks an item from the list, decide where focus should go: staying on the list item is often best on large screens, with an announcement that the detail updated. On small screens where the detail replaces the list, move focus to the detail heading and provide a clear "Back to list" button that returns focus to the selected item. Keep the behavior consistent.

## 401: How do you build an accessible command palette?

Open it with a documented shortcut, as a modal dialog containing a combobox with a listbox of commands. Focus starts in the search input, arrow keys move through results with `aria-activedescendant`, Enter runs the command and Escape closes and returns focus. Announce the result count and make sure every command is also available in normal menus or buttons.

## 402: How do you make notifications or badge counts accessible?

A visual badge like "3" on a bell icon needs to be part of the button's accessible name, like "Notifications, 3 unread". When the count changes in the background, decide whether it is worth announcing; usually a polite announcement for new important items is enough. Don't put the badge in a live region that announces every change.

## 403: What problems does aria-label on links cause for translation and voice control?

`aria-label` replaces the visible text, so if they don't match, voice control commands fail (WCAG 2.5.3). Automatic browser translators often skip `aria-label`, leaving it in the original language while the visible text is translated. Prefer visible text plus visually hidden extras, which keeps the visible words in the name and gets translated with the page.

## 404: How do you test with forced colors mode without Windows?

Chrome and Edge DevTools can emulate `forced-colors: active` in the Rendering panel. It's a good first check, but the real Windows Contrast Themes can behave differently, especially with SVG, background images and system colors. Use a Windows machine or VM for final testing.

## 405: How do SVG icons behave in forced colors mode?

SVG icons with hard-coded `fill` colors may disappear or become invisible against the forced background. Use `fill="currentColor"` so icons take the text color, which the browser adjusts in forced colors. For icons that must keep a special color, you can set system colors in a `forced-colors` media query.

```css
.icon {
  fill: currentColor;
}
```

## 406: What is the impact of custom focus styles that use only box-shadow?

In forced colors mode, browsers remove `box-shadow`, so a focus ring made only with box-shadow disappears completely. Combine it with a transparent `outline` that becomes visible in forced colors mode, or use `outline` as the main focus style.

```css
button:focus-visible {
  box-shadow: 0 0 0 3px #1a73e8;
  outline: 2px solid transparent;
}
```

## 407: How do you make a page accessible when it uses CSS to hide content responsively?

Content hidden with `display: none` at certain breakpoints is removed from the accessibility tree too, which is correct if it's really not shown. Problems come when content is moved off-screen or hidden with `opacity: 0` but still reachable by keyboard, or when a mobile menu is hidden visually but its links are still focusable. Use `hidden`, `inert` or `display: none` for closed menus.

## 408: What is the "hamburger menu" accessibility checklist?

The button needs a name like "Menu", `aria-expanded` and `aria-controls`. When closed, the menu items must not be focusable. When open, focus can stay on the button or move to the first link, Escape should close it and return focus, and if it covers the page like a modal, the rest of the page should be inert. The menu should also fit at high zoom.

## 409: How do you check reading order in complex CSS layouts?

Use a screen reader to read the page in sequence, tab through it and compare to the visual order. Tools like the "Accessibility tree" view in DevTools or turning off CSS (with an extension) show the DOM order directly. Watch for grids with explicit placement, `order` and absolutely positioned elements that appear far from their DOM position.

## 410: What is the CSS reading-flow property?

`reading-flow` is a CSS property that tells the browser to follow the visual order of a flex, grid or block layout for focus navigation and screen reader order, instead of DOM order. Values include `flex-visual`, `grid-rows` and `grid-columns`. It shipped in Chromium in 2025 and isn't in all browsers yet, so DOM order is still the reliable approach.

## 411: How does the accessibility of a site change with client-side rendering only?

With client-side rendering, users see nothing until JavaScript loads, and the first content screen readers get may be a loading spinner. If JavaScript fails, nothing works. Server-side rendering or static HTML gives assistive technology real content faster, and progressive enhancement means core tasks still work. Accessibility issues can also be hidden from server-side SEO checks but present for users.

## 412: How do you make a CSS-only interaction accessible?

CSS-only toggles using checkbox hacks or `:target` often lack the right roles and states, like `aria-expanded`. If you use them, make sure the control is a real focusable element with a good name, and that screen readers get the state. Often `<details>`, `popover` or a small amount of JavaScript gives better results than a CSS trick.

## 413: How do you test accessibility of components in isolation versus in pages?

Component tests check each part alone: roles, names, keyboard behavior and states. Page tests check how parts work together: heading structure, landmark structure, duplicate ids, focus order across components and focus after navigation. Many issues appear only in context, like two "Close" buttons with the same name or nested landmarks, so you need both.

## 414: What issues can come from duplicate ids?

ARIA attributes and `<label for>` reference elements by id, and if two elements share an id, the browser picks the first one. A label can end up naming the wrong field, or `aria-describedby` can read the wrong error. This often happens when a component is rendered twice with a hard-coded id. Use `useId` or generated ids to avoid it.

## 415: How do you approach accessibility for an e-commerce product filtering panel?

Use groups of checkboxes in fieldsets with legends, keep the filter panel in a labeled region, and announce the updated result count after each change. Don't reload the page or move focus when a checkbox is ticked, unless users clicked an "Apply" button. On mobile, if the panel is a modal, follow the dialog pattern. Show applied filters as a list of removable buttons with clear names.

## 416: How do you build an accessible rating component?

For input, use a group of radio buttons styled as stars, with a legend like "Rate this product" and labels like "4 stars". This gives arrow key support for free. For displaying a rating, use text like "Rated 4.5 out of 5" with the star images hidden from screen readers.

```html
<fieldset>
  <legend>Rate this product</legend>
  <input type="radio" id="r1" name="rating" value="1" /><label for="r1"
    >1 star</label
  >
  <input type="radio" id="r2" name="rating" value="2" /><label for="r2"
    >2 stars</label
  >
  <input type="radio" id="r3" name="rating" value="3" /><label for="r3"
    >3 stars</label
  >
</fieldset>
```

## 417: How do you make a stepper or quantity input accessible?

Use `<input type="number">` with a label, or a text input with `inputmode="numeric"`, and add minus and plus buttons with clear names like "Decrease quantity". When the buttons change the value, update the input so screen readers can read the new value, and announce it politely if needed. Make sure the buttons meet the target size rule.

## 418: How do you handle accessibility when content loads in a portal?

React portals and similar features render content at the end of the `<body>`, away from the trigger in the DOM. For dialogs this is fine if focus moves into them, but for popovers and dropdowns it breaks the reading and tab order. Move focus explicitly, manage Tab out of the portal back to the trigger, or use the native `popover` attribute, which handles focus order for you.

## 419: How do you make a dialog that opens another dialog accessible?

Each new dialog should take focus and make the one below inert, and closing it should return focus to the control in the dialog below that opened it. Native `<dialog>` with `showModal()` stacks correctly in the top layer. Nested dialogs are confusing for everyone, though, so consider replacing the inner dialog with a step inside the same dialog.

## 420: How do you announce sorted, filtered or paged updates in a data table?

After the update, announce a short summary like "Sorted by price, low to high, showing 20 of 340 products" in a polite live region. Keep focus on the control the user used, so they can continue. Update `aria-sort` on the column header, and for paged results, update the page title or caption so it's clear which page is shown.

## 421: What is aria-keyshortcuts?

`aria-keyshortcuts` tells assistive technology about keyboard shortcuts that activate or focus an element, like `aria-keyshortcuts="Control+S"`. It doesn't create the shortcut; you still handle it in JavaScript. Screen readers may announce it, which helps users discover shortcuts. Also document shortcuts visibly.

## 422: What do aria-setsize and aria-posinset do?

They tell assistive technology an item's position and the total number of items in a set, like "item 3 of 50". Browsers calculate these automatically for normal lists, but you need them when not all items are in the DOM, like in virtual lists, feeds or lazy-loaded trees. Use `aria-setsize="-1"` if the total is unknown.

## 423: What does aria-details do?

`aria-details` points to an element with more detailed information, like a full description of a complex image or a comment thread on a piece of text. Unlike `aria-describedby`, the content isn't read as a flat string; screen readers can tell users that details exist and let them navigate there. Support is improving but still not consistent.

## 424: How do you choose between aria-describedby and aria-details?

Use `aria-describedby` for short text that can be read in one go, like a hint or an error. Use `aria-details` for longer or structured content, like a table describing a chart, or a comment with formatting, which shouldn't be flattened into one string. Some teams use both with different content.

## 425: How should you handle hidden content that becomes visible on demand, like "read more"?

When users expand text, keep focus on the button and update `aria-expanded`, so screen reader users can read the new content next. If the new content appears far away, consider moving focus to it. Don't hide content with `aria-hidden` while leaving it visible, or show content that is still hidden from assistive technology, since that creates a mismatch.

## 426: What is the accessibility impact of lazy loading images?

Native `loading="lazy"` doesn't affect accessibility, since alt text is in the HTML from the start. Problems come from JavaScript lazy loaders that set alt text or src later, use placeholder images without alt, or change layout when images load. Always put the real alt text in the initial HTML and reserve image space.

## 427: How do you make loading skeletons accessible?

Skeletons are visual placeholders, so hide them from screen readers with `aria-hidden="true"` and provide a text status like "Loading orders" in a live region or a visually hidden element. Set `aria-busy="true"` on the region being loaded. When content arrives, remove the skeleton and announce completion if the user is waiting for it.

```html
<section aria-labelledby="orders-h" aria-busy="true">
  <h2 id="orders-h">Orders</h2>
  <p class="sr-only" role="status">Loading orders</p>
  <div class="skeleton" aria-hidden="true"></div>
</section>
```

## 428: How do you handle accessibility of animations used for meaning?

If an animation communicates something, like a cart icon shaking to show an item was added, the same information must be given in text and announced, since screen reader users won't see it and reduced motion users may have it turned off. Never let important information depend on motion alone.

## 429: What are the risks of auto-playing background videos?

They can distract people with attention problems, trigger vestibular issues, use a lot of data and may contain flashing. WCAG 2.2.2 requires a pause control if they play more than 5 seconds. Respect `prefers-reduced-motion`, provide a visible pause button and make sure text over the video keeps enough contrast for every frame.

## 430: How do you handle accessibility for content generated by users?

You can't control everything users upload, but you can help: require or prompt for alt text on image uploads, give the editor heading and list tools, warn about low contrast or missing captions, and use AI to suggest alt text that users review. Platforms like Mastodon and GitHub show prompts for image descriptions. Also make the authoring tool itself accessible.

## 431: Can AI write alt text for images?

AI can give a useful first draft and describe what is visible, but it doesn't know why the image is on the page, so it often misses the point or adds useless details. It can also make mistakes, like naming the wrong person. Use AI suggestions as a starting point, and have a human check and edit them, especially for important content.

## 432: How can AI tools help or hurt accessibility work?

They can help by suggesting alt text, generating captions and transcripts, explaining WCAG rules, reviewing code for common issues and drafting test plans. They can hurt by producing plausible but wrong ARIA, adding unneeded roles and labels, or giving false confidence. Treat AI output like any other code review input, and always test with real assistive technology.

## 433: What is ATAG?

ATAG (Authoring Tool Accessibility Guidelines) 2.0 is a W3C standard for tools that create web content, like CMSs, editors and site builders. Part A says the tool itself must be accessible to authors with disabilities. Part B says the tool should help authors produce accessible content, like prompting for alt text and producing valid semantic markup by default.

## 434: What is UAAG?

UAAG (User Agent Accessibility Guidelines) 2.0 is a W3C Note about how browsers, media players and other user agents should support accessibility, like letting users change text size and colors, control media and use the keyboard. It's mainly for browser makers, but it explains why some user preferences, like minimum font size, must be respected by pages.

## 435: How do accessibility requirements apply to internal tools?

Internal tools are often ignored, but employees with disabilities need them to do their jobs, and laws like the ADA's employment rules (Title I) and many public sector rules cover them. An inaccessible internal tool can block hiring or promoting disabled people. Use the same design system and testing process as public products.

## 436: How do you handle accessibility in procurement?

Include accessibility requirements, like WCAG 2.2 AA, in requests for proposals and contracts. Ask vendors for a recent ACR or VPAT and verify it with your own testing of key tasks, since many reports are optimistic. Add contract terms for fixing issues within a set time. Section 508 and EN 301 549 are often used as the baseline.

## 437: How do you judge a vendor's VPAT?

Check its date, which product version it covers, which standards it reports on and who wrote it (an independent auditor is more trustworthy). Look at criteria marked "Partially Supports" or "Does Not Support" and read the remarks. Be suspicious of a report that claims "Supports" on every criterion, and test the product yourself on your main use cases.

## 438: How do you make accessibility work sustainable on a team?

Make it part of the definition of done, not a separate project. Train everyone in their role, give developers screen reader and keyboard testing skills, keep a shared checklist and have accessibility champions on each team. Fix root causes in shared components, keep automated checks in CI and review metrics regularly. Celebrate fixes so the work stays visible.

## 439: What is the difference between ARIA roles in ARIA 1.2 and HTML-mapped roles like generic?

ARIA 1.2 added the `generic` role to describe elements like `<div>` and `<span>` that have no meaning, and roles like `paragraph`, `code`, `strong`, `emphasis`, `subscript`, `superscript`, `time`, `blockquote` and `caption` so HTML elements could be mapped consistently. Authors shouldn't usually set `role="generic"` themselves; it exists mostly for spec mappings and for stating what can't be named.

## 440: What does the ARIA in HTML spec define?

ARIA in HTML says which ARIA roles and attributes may be used on which HTML elements, and which are redundant or not allowed. For example, `role="button"` on a `<button>` is redundant, and `role="heading"` on an `<a href>` isn't allowed. Validators and tools like axe use it to flag misuse. It was updated as a W3C Recommendation in 2026.

## 441: How do you handle hover cards that contain links, like user profile previews?

They are not tooltips, because they contain interactive content. Make the preview available through a button or a link to the full profile, open it on focus with a delay or on a key press, and allow keyboard users to move into it. Follow WCAG 1.4.13: hoverable, dismissable with Escape and persistent. Many teams decide the full profile link is enough for keyboard users and hide the hover card from them.

## 442: How do you handle autoplaying carousels with screen readers?

If slides change automatically, a live region could announce every slide, which is very noisy. The APG carousel pattern turns `aria-live` off while rotating and sets it to `polite` only when the user moves slides manually. Stop rotation when anything in the carousel has focus, so the content doesn't change while a screen reader user is reading it.

## 443: How do you test that your site works with voice control?

Use Voice Control on macOS or iOS, or Voice Access on Windows or Android, and try to complete tasks by saying the visible labels, like "click Add to cart". Check that every control can be targeted by its visible name, that "show numbers" overlays reach all controls and that custom widgets respond. Mismatches between visible text and `aria-label` show up quickly.

## 444: How do you support switch users in web apps?

Switch users rely on the focus order and scanning, so keep the number of focus stops reasonable, avoid time-based interactions and long timeouts, make targets large and keep important actions near the start of the order. Avoid interactions that need holding or dragging. Skip links and landmarks reduce how far they must scan.

## 445: What is the hardest accessibility problem you would expect in a modern SPA, and how would you solve it?

A common answer is focus management across asynchronous updates, like route changes, modals, toasts and optimistic updates, because nothing handles it for you and bugs appear only during real use. The solution is a shared approach: one live region service, a focus manager that restores focus after dialogs and route changes, clear rules for where focus goes after each kind of action, and Playwright tests that check focus after key interactions.

## 446: How would you design a shared announcer service for an app?

Render one or two hidden live regions (polite and assertive) at the app root that stay mounted. Expose a function like `announce(message, { priority })` that queues messages, clears and resets text to allow repeats, and drops duplicate messages within a short time. Components call it instead of creating their own live regions.

```js
const polite = document.getElementById("announcer-polite");
let timer;

export function announce(message) {
  clearTimeout(timer);
  polite.textContent = "";
  timer = setTimeout(() => {
    polite.textContent = message;
  }, 50);
}
```

## 447: How do you handle accessibility in micro-frontend architectures?

Each team owns parts of the page, so things like heading levels, landmarks, duplicate ids, the page title, focus after navigation and live regions can conflict. Agree on shared rules: which app owns `<main>`, `<h1>` and the title, a shared announcer and focus service, id prefixes per micro-frontend and a shared design system. Test the composed page, not only each piece.

## 448: How do you make sure accessibility doesn't regress after release?

Run automated checks in CI and on production pages on a schedule, keep ARIA snapshots and keyboard tests for key flows, include accessibility in code review checklists and do periodic manual audits of main journeys. Track issues reported by users and fix them fast. Regressions often come from content changes, so train content editors too.

## 449: What would you check first on a page you have never seen, with only five minutes?

Tab through the page to check focus visibility, focus order and whether all controls are reachable. Run axe or WAVE for quick wins like missing names and contrast. Check the heading outline and landmarks with a tool or screen reader, zoom to 200%, and try the main form or action once with a screen reader. These steps catch the most common and most serious problems quickly.

## 450: What does a senior engineer bring to accessibility beyond knowing WCAG?

They build systems that make accessibility the default: accessible components, linting and tests in CI, focus and announcement services, and clear patterns for the team to follow. They judge trade-offs between native elements and custom widgets, know how assistive technology actually behaves, mentor others and push back on designs or deadlines that would block users. Most of all, they treat accessibility as part of quality, not a separate checklist.
