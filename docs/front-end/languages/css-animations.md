# CSS Animations Interview Questions and Answers

_Last updated: November 18, 2026_

This file has 450 interview questions and answers about animation in CSS: 150 easy, 150 moderate and 150 advanced. It covers transitions, `@keyframes` animations, transforms, timing functions, the Web Animations API, view transitions and scroll-driven animations, as they work in current browsers at the end of 2026. Where a feature does not work in every browser yet, the answer says so.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What ways do you have to animate things with CSS?](#1-what-ways-do-you-have-to-animate-things-with-css)
- [2: What is a CSS transition?](#2-what-is-a-css-transition)
- [3: What is a CSS keyframe animation?](#3-what-is-a-css-keyframe-animation)
- [4: What is the difference between a transition and an animation?](#4-what-is-the-difference-between-a-transition-and-an-animation)
- [5: What are the transition properties?](#5-what-are-the-transition-properties)
- [6: How do you write the transition shorthand?](#6-how-do-you-write-the-transition-shorthand)
- [7: What happens if you set transition-duration to 0?](#7-what-happens-if-you-set-transition-duration-to-0)
- [8: What does transition-property: all do, and why is it not a good default?](#8-what-does-transition-property-all-do-and-why-is-it-not-a-good-default)
- [9: What units can you use for durations and delays?](#9-what-units-can-you-use-for-durations-and-delays)
- [10: What is a timing function?](#10-what-is-a-timing-function)
- [11: What timing function keywords does CSS have?](#11-what-timing-function-keywords-does-css-have)
- [12: When should you use ease-out vs ease-in?](#12-when-should-you-use-ease-out-vs-ease-in)
- [13: What is the default timing function for transitions and animations?](#13-what-is-the-default-timing-function-for-transitions-and-animations)
- [14: How do you define keyframes?](#14-how-do-you-define-keyframes)
- [15: What are the animation properties?](#15-what-are-the-animation-properties)
- [16: How do you write the animation shorthand?](#16-how-do-you-write-the-animation-shorthand)
- [17: What does animation-iteration-count do?](#17-what-does-animation-iteration-count-do)
- [18: What does animation-direction do?](#18-what-does-animation-direction-do)
- [19: What does animation-fill-mode do?](#19-what-does-animation-fill-mode-do)
- [20: Why does my element jump back to its start after the animation ends?](#20-why-does-my-element-jump-back-to-its-start-after-the-animation-ends)
- [21: What does animation-play-state do?](#21-what-does-animation-play-state-do)
- [22: What does animation-delay do?](#22-what-does-animation-delay-do)
- [23: What does a negative animation-delay do?](#23-what-does-a-negative-animation-delay-do)
- [24: Can you apply more than one animation to an element?](#24-can-you-apply-more-than-one-animation-to-an-element)
- [25: What happens if two keyframes animations change the same property?](#25-what-happens-if-two-keyframes-animations-change-the-same-property)
- [26: What does transform do?](#26-what-does-transform-do)
- [27: What transform functions are there?](#27-what-transform-functions-are-there)
- [28: Does the order of transform functions matter?](#28-does-the-order-of-transform-functions-matter)
- [29: What are the individual transform properties?](#29-what-are-the-individual-transform-properties)
- [30: What does transform-origin do?](#30-what-does-transform-origin-do)
- [31: What is the difference between translate and changing top or left?](#31-what-is-the-difference-between-translate-and-changing-top-or-left)
- [32: Which properties can be animated?](#32-which-properties-can-be-animated)
- [33: What is a discrete animation?](#33-what-is-a-discrete-animation)
- [34: Can you animate display?](#34-can-you-animate-display)
- [35: Why does my transition not run when I change display: none to display: block?](#35-why-does-my-transition-not-run-when-i-change-display-none-to-display-block)
- [36: What is @starting-style?](#36-what-is-starting-style)
- [37: Can you animate opacity?](#37-can-you-animate-opacity)
- [38: Can you animate colors?](#38-can-you-animate-colors)
- [39: Can you animate a background gradient directly?](#39-can-you-animate-a-background-gradient-directly)
- [40: Can you animate height: auto?](#40-can-you-animate-height-auto)
- [41: What is a keyframe selector?](#41-what-is-a-keyframe-selector)
- [42: What happens if you leave out the 0% or 100% keyframe?](#42-what-happens-if-you-leave-out-the-0-or-100-keyframe)
- [43: Can keyframes include a timing function?](#43-can-keyframes-include-a-timing-function)
- [44: Can you use !important inside keyframes?](#44-can-you-use-important-inside-keyframes)
- [45: What happens if two @keyframes rules have the same name?](#45-what-happens-if-two-keyframes-rules-have-the-same-name)
- [46: How do you make an infinite spinner?](#46-how-do-you-make-an-infinite-spinner)
- [47: How do you make a fade-in animation?](#47-how-do-you-make-a-fade-in-animation)
- [48: How do you make an element slide in from the left?](#48-how-do-you-make-an-element-slide-in-from-the-left)
- [49: How do you add a hover effect with a transition?](#49-how-do-you-add-a-hover-effect-with-a-transition)
- [50: Why should the transition be on the base selector and not on :hover?](#50-why-should-the-transition-be-on-the-base-selector-and-not-on-hover)
- [51: What is cubic-bezier()?](#51-what-is-cubic-bezier)
- [52: How do you make an overshoot or "back" effect with cubic-bezier?](#52-how-do-you-make-an-overshoot-or-back-effect-with-cubic-bezier)
- [53: What does steps() do?](#53-what-does-steps-do)
- [54: What are the step positions in steps()?](#54-what-are-the-step-positions-in-steps)
- [55: How do you animate a sprite sheet with CSS?](#55-how-do-you-animate-a-sprite-sheet-with-css)
- [56: What is the linear() easing function?](#56-what-is-the-linear-easing-function)
- [57: What is the difference between the linear keyword and the linear() function?](#57-what-is-the-difference-between-the-linear-keyword-and-the-linear-function)
- [58: How do you make a typewriter effect with CSS?](#58-how-do-you-make-a-typewriter-effect-with-css)
- [59: What is prefers-reduced-motion?](#59-what-is-prefers-reduced-motion)
- [60: Should reduced motion mean no animation at all?](#60-should-reduced-motion-mean-no-animation-at-all)
- [61: What frame rate should animations aim for?](#61-what-frame-rate-should-animations-aim-for)
- [62: Which properties are cheap to animate?](#62-which-properties-are-cheap-to-animate)
- [63: Which properties are expensive to animate?](#63-which-properties-are-expensive-to-animate)
- [64: What is will-change?](#64-what-is-will-change)
- [65: How do you give different properties different durations in one transition?](#65-how-do-you-give-different-properties-different-durations-in-one-transition)
- [66: What is transition-delay useful for?](#66-what-is-transition-delay-useful-for)
- [67: What starts a transition?](#67-what-starts-a-transition)
- [68: Do transitions run when the page first loads?](#68-do-transitions-run-when-the-page-first-loads)
- [69: How do you stop an animation with CSS?](#69-how-do-you-stop-an-animation-with-css)
- [70: What happens when a property appears in some keyframes but not in others?](#70-what-happens-when-a-property-appears-in-some-keyframes-but-not-in-others)
- [71: How do you fade an element out and then hide it?](#71-how-do-you-fade-an-element-out-and-then-hide-it)
- [72: Why is opacity: 0 alone not enough to hide an element?](#72-why-is-opacity-0-alone-not-enough-to-hide-an-element)
- [73: What is perspective in CSS?](#73-what-is-perspective-in-css)
- [74: What is the difference between the perspective property and the perspective() function?](#74-what-is-the-difference-between-the-perspective-property-and-the-perspective-function)
- [75: What does backface-visibility do?](#75-what-does-backface-visibility-do)
- [76: What does transform-style: preserve-3d do?](#76-what-does-transform-style-preserve-3d-do)
- [77: How do you make a card flip animation?](#77-how-do-you-make-a-card-flip-animation)
- [78: Is it OK to animate box-shadow?](#78-is-it-ok-to-animate-box-shadow)
- [79: Can you animate filter?](#79-can-you-animate-filter)
- [80: Can you animate clip-path?](#80-can-you-animate-clip-path)
- [81: How do you make an SVG line "draw itself"?](#81-how-do-you-make-an-svg-line-draw-itself)
- [82: Can you animate border-radius?](#82-can-you-animate-border-radius)
- [83: Can you animate a CSS custom property?](#83-can-you-animate-a-css-custom-property)
- [84: What is @property?](#84-what-is-property)
- [85: How can CSS variables make animations easier to configure?](#85-how-can-css-variables-make-animations-easier-to-configure)
- [86: How do you avoid hover animations sticking on touch screens?](#86-how-do-you-avoid-hover-animations-sticking-on-touch-screens)
- [87: How do you make a skeleton loading shimmer?](#87-how-do-you-make-a-skeleton-loading-shimmer)
- [88: How do you make a "ping" or pulse ring effect?](#88-how-do-you-make-a-ping-or-pulse-ring-effect)
- [89: How do you make a shake animation for a form error?](#89-how-do-you-make-a-shake-animation-for-a-form-error)
- [90: How do you animate a link underline?](#90-how-do-you-animate-a-link-underline)
- [91: How should you animate a progress bar?](#91-how-should-you-animate-a-progress-bar)
- [92: How do you see and debug animations in browser DevTools?](#92-how-do-you-see-and-debug-animations-in-browser-devtools)
- [93: How do you slow down animations to check them?](#93-how-do-you-slow-down-animations-to-check-them)
- [94: Do you still need -webkit- prefixes for animations?](#94-do-you-still-need--webkit--prefixes-for-animations)
- [95: Does an animation run on an element with display: none?](#95-does-an-animation-run-on-an-element-with-display-none)
- [96: Does an animation run on an element with visibility: hidden or opacity: 0?](#96-does-an-animation-run-on-an-element-with-visibility-hidden-or-opacity-0)
- [97: How do you hide an element after its animation without JavaScript?](#97-how-do-you-hide-an-element-after-its-animation-without-javascript)
- [98: How do you make a bouncing ball animation?](#98-how-do-you-make-a-bouncing-ball-animation)
- [99: How do you rotate an element continuously around its own center?](#99-how-do-you-rotate-an-element-continuously-around-its-own-center)
- [100: What angle units can you use in rotations?](#100-what-angle-units-can-you-use-in-rotations)
- [101: What JavaScript events do CSS animations fire?](#101-what-javascript-events-do-css-animations-fire)
- [102: What JavaScript events do CSS transitions fire?](#102-what-javascript-events-do-css-transitions-fire)
- [103: Why does transitionend fire more than once?](#103-why-does-transitionend-fire-more-than-once)
- [104: Why doesn't transitionend fire?](#104-why-doesnt-transitionend-fire)
- [105: How do you start a CSS animation from JavaScript?](#105-how-do-you-start-a-css-animation-from-javascript)
- [106: How do you restart a CSS animation?](#106-how-do-you-restart-a-css-animation)
- [107: What is the Web Animations API?](#107-what-is-the-web-animations-api)
- [108: How do you create an animation with element.animate()?](#108-how-do-you-create-an-animation-with-elementanimate)
- [109: What is a view transition?](#109-what-is-a-view-transition)
- [110: How do you start a simple view transition?](#110-how-do-you-start-a-simple-view-transition)
- [111: What is a scroll-driven animation?](#111-what-is-a-scroll-driven-animation)
- [112: What is the difference between scroll() and view() timelines?](#112-what-is-the-difference-between-scroll-and-view-timelines)
- [113: How do you write a reading progress bar with CSS only?](#113-how-do-you-write-a-reading-progress-bar-with-css-only)
- [114: Why must animation-timeline come after the animation shorthand?](#114-why-must-animation-timeline-come-after-the-animation-shorthand)
- [115: What is a CSS motion path?](#115-what-is-a-css-motion-path)
- [116: What does offset-rotate do?](#116-what-does-offset-rotate-do)
- [117: How long should UI animations be?](#117-how-long-should-ui-animations-be)
- [118: Why use animations in a UI at all?](#118-why-use-animations-in-a-ui-at-all)
- [119: What is a micro-interaction?](#119-what-is-a-micro-interaction)
- [120: How do you stagger animations for a list of items?](#120-how-do-you-stagger-animations-for-a-list-of-items)
- [121: Can you animate ::before and ::after pseudo-elements?](#121-can-you-animate-before-and-after-pseudo-elements)
- [122: How do you make a glowing text effect?](#122-how-do-you-make-a-glowing-text-effect)
- [123: What does a percentage in translate refer to?](#123-what-does-a-percentage-in-translate-refer-to)
- [124: Why does my centered element jump when I add a hover transform?](#124-why-does-my-centered-element-jump-when-i-add-a-hover-transform)
- [125: What does skew() do?](#125-what-does-skew-do)
- [126: What is matrix() in transforms?](#126-what-is-matrix-in-transforms)
- [127: What is the compositor?](#127-what-is-the-compositor)
- [128: What is jank?](#128-what-is-jank)
- [129: What is the translateZ(0) hack?](#129-what-is-the-translatez0-hack)
- [130: What does the animation shorthand reset?](#130-what-does-the-animation-shorthand-reset)
- [131: What are the rules for naming keyframes?](#131-what-are-the-rules-for-naming-keyframes)
- [132: What happens if the same keyframe percentage appears twice in one @keyframes?](#132-what-happens-if-the-same-keyframe-percentage-appears-twice-in-one-keyframes)
- [133: Can keyframe percentages be lower than 0% or higher than 100%?](#133-can-keyframe-percentages-be-lower-than-0-or-higher-than-100)
- [134: How do you make a smooth focus ring animation?](#134-how-do-you-make-a-smooth-focus-ring-animation)
- [135: How do you animate a child when the parent is hovered?](#135-how-do-you-animate-a-child-when-the-parent-is-hovered)
- [136: Can each property in a transition have its own timing function?](#136-can-each-property-in-a-transition-have-its-own-timing-function)
- [137: What does interpolation mean in animations?](#137-what-does-interpolation-mean-in-animations)
- [138: When should you use CSS animation instead of a GIF or video?](#138-when-should-you-use-css-animation-instead-of-a-gif-or-video)
- [139: When would you use a JavaScript animation library instead of CSS?](#139-when-would-you-use-a-javascript-animation-library-instead-of-css)
- [140: Do CSS animations work in HTML emails?](#140-do-css-animations-work-in-html-emails)
- [141: How do you make an infinite scrolling marquee with CSS?](#141-how-do-you-make-an-infinite-scrolling-marquee-with-css)
- [142: How do you make a loading dots animation?](#142-how-do-you-make-a-loading-dots-animation)
- [143: How do you make a hamburger icon turn into an X?](#143-how-do-you-make-a-hamburger-icon-turn-into-an-x)
- [144: How do you animate a button press?](#144-how-do-you-animate-a-button-press)
- [145: How do you create a toggle switch animation?](#145-how-do-you-create-a-toggle-switch-animation)
- [146: What does the cascade do with animation styles?](#146-what-does-the-cascade-do-with-animation-styles)
- [147: Can you set animation styles inline with the style attribute?](#147-can-you-set-animation-styles-inline-with-the-style-attribute)
- [148: What does "animating from current state" mean?](#148-what-does-animating-from-current-state-mean)
- [149: What happens when a transition is interrupted halfway?](#149-what-happens-when-a-transition-is-interrupted-halfway)
- [150: What is the difference between animation-fill-mode: forwards and setting the final style yourself?](#150-what-is-the-difference-between-animation-fill-mode-forwards-and-setting-the-final-style-yourself)

### Moderate Questions (151-300)

- [151: What does transition-behavior: allow-discrete do?](#151-what-does-transition-behavior-allow-discrete-do)
- [152: How do you animate a dialog in and out with CSS only?](#152-how-do-you-animate-a-dialog-in-and-out-with-css-only)
- [153: Why do you need to transition overlay when animating a dialog or popover out?](#153-why-do-you-need-to-transition-overlay-when-animating-a-dialog-or-popover-out)
- [154: How do you animate a popover?](#154-how-do-you-animate-a-popover)
- [155: How do you animate the backdrop of a modal dialog?](#155-how-do-you-animate-the-backdrop-of-a-modal-dialog)
- [156: Can you nest @starting-style inside a rule?](#156-can-you-nest-starting-style-inside-a-rule)
- [157: What are common mistakes with @starting-style?](#157-what-are-common-mistakes-with-starting-style)
- [158: How do interpolate-size and calc-size() work?](#158-how-do-interpolate-size-and-calc-size-work)
- [159: How does the grid 0fr to 1fr trick animate height?](#159-how-does-the-grid-0fr-to-1fr-trick-animate-height)
- [160: What are the problems with the max-height trick?](#160-what-are-the-problems-with-the-max-height-trick)
- [161: How do you animate a details element opening?](#161-how-do-you-animate-a-details-element-opening)
- [162: How do you animate removing an item from a list?](#162-how-do-you-animate-removing-an-item-from-a-list)
- [163: What is the FLIP technique?](#163-what-is-the-flip-technique)
- [164: How do you implement FLIP with the Web Animations API?](#164-how-do-you-implement-flip-with-the-web-animations-api)
- [165: What does element.getAnimations() return?](#165-what-does-elementgetanimations-return)
- [166: What does document.getAnimations() do?](#166-what-does-documentgetanimations-do)
- [167: What methods does an Animation object have?](#167-what-methods-does-an-animation-object-have)
- [168: What is the difference between playbackRate and updatePlaybackRate()?](#168-what-is-the-difference-between-playbackrate-and-updateplaybackrate)
- [169: How do you jump to a specific point in an animation?](#169-how-do-you-jump-to-a-specific-point-in-an-animation)
- [170: What are the ready and finished promises on an Animation?](#170-what-are-the-ready-and-finished-promises-on-an-animation)
- [171: Why is fill: "forwards" in the Web Animations API not ideal, and what is commitStyles()?](#171-why-is-fill-forwards-in-the-web-animations-api-not-ideal-and-what-is-commitstyles)
- [172: What does the composite option do in element.animate()?](#172-what-does-the-composite-option-do-in-elementanimate)
- [173: What are KeyframeEffect and the Animation constructor for?](#173-what-are-keyframeeffect-and-the-animation-constructor-for)
- [174: What keyframe formats does element.animate() accept?](#174-what-keyframe-formats-does-elementanimate-accept)
- [175: What timing options can you pass to element.animate()?](#175-what-timing-options-can-you-pass-to-elementanimate)
- [176: How do you control a CSS animation from JavaScript without changing classes?](#176-how-do-you-control-a-css-animation-from-javascript-without-changing-classes)
- [177: What is a CSSTransition object?](#177-what-is-a-csstransition-object)
- [178: How do you wait for all animations on an element before removing it?](#178-how-do-you-wait-for-all-animations-on-an-element-before-removing-it)
- [179: How do you check prefers-reduced-motion in JavaScript?](#179-how-do-you-check-prefers-reduced-motion-in-javascript)
- [180: What is the "global reduced motion" reset and what are its risks?](#180-what-is-the-global-reduced-motion-reset-and-what-are-its-risks)
- [181: What is the "no-preference first" approach to motion?](#181-what-is-the-no-preference-first-approach-to-motion)
- [182: What does WCAG say about moving content?](#182-what-does-wcag-say-about-moving-content)
- [183: What is WCAG 2.3.3 Animation from Interactions?](#183-what-is-wcag-233-animation-from-interactions)
- [184: How do you add a pause button for animations?](#184-how-do-you-add-a-pause-button-for-animations)
- [185: How do animations affect screen reader users?](#185-how-do-animations-affect-screen-reader-users)
- [186: What pseudo-elements does a view transition create?](#186-what-pseudo-elements-does-a-view-transition-create)
- [187: What does view-transition-name do?](#187-what-does-view-transition-name-do)
- [188: How do you change the default cross-fade of a view transition?](#188-how-do-you-change-the-default-cross-fade-of-a-view-transition)
- [189: Why must view-transition-name values be unique?](#189-why-must-view-transition-name-values-be-unique)
- [190: What is view-transition-class?](#190-what-is-view-transition-class)
- [191: What do view-transition-name: match-element and auto do?](#191-what-do-view-transition-name-match-element-and-auto-do)
- [192: How do you turn on view transitions between pages of a multi-page site?](#192-how-do-you-turn-on-view-transitions-between-pages-of-a-multi-page-site)
- [193: What are the pageswap and pagereveal events?](#193-what-are-the-pageswap-and-pagereveal-events)
- [194: What are view transition types?](#194-what-are-view-transition-types)
- [195: What promises does the ViewTransition object give you?](#195-what-promises-does-the-viewtransition-object-give-you)
- [196: What does skipTransition() do?](#196-what-does-skiptransition-do)
- [197: How do you respect reduced motion with view transitions?](#197-how-do-you-respect-reduced-motion-with-view-transitions)
- [198: How do view transitions fit into single-page app routers?](#198-how-do-view-transitions-fit-into-single-page-app-routers)
- [199: What does animation-range do in scroll-driven animations?](#199-what-does-animation-range-do-in-scroll-driven-animations)
- [200: What are the animation-range names for view timelines?](#200-what-are-the-animation-range-names-for-view-timelines)
- [201: How do you use a named scroll timeline?](#201-how-do-you-use-a-named-scroll-timeline)
- [202: What is timeline-scope for?](#202-what-is-timeline-scope-for)
- [203: What does animation-duration mean for a scroll-driven animation?](#203-what-does-animation-duration-mean-for-a-scroll-driven-animation)
- [204: Why do scroll-driven animations often use fill-mode both?](#204-why-do-scroll-driven-animations-often-use-fill-mode-both)
- [205: How do you make elements fade in as they scroll into view?](#205-how-do-you-make-elements-fade-in-as-they-scroll-into-view)
- [206: How do you make a parallax effect with scroll-driven animations?](#206-how-do-you-make-a-parallax-effect-with-scroll-driven-animations)
- [207: How do you feature-detect scroll-driven animations?](#207-how-do-you-feature-detect-scroll-driven-animations)
- [208: What fallback can you use where scroll-driven animations don't work?](#208-what-fallback-can-you-use-where-scroll-driven-animations-dont-work)
- [209: What axis options do scroll timelines have?](#209-what-axis-options-do-scroll-timelines-have)
- [210: What arguments does the scroll() function take?](#210-what-arguments-does-the-scroll-function-take)
- [211: What is view-timeline-inset for?](#211-what-is-view-timeline-inset-for)
- [212: How do you shrink a sticky header on scroll with CSS only?](#212-how-do-you-shrink-a-sticky-header-on-scroll-with-css-only)
- [213: How do you use @supports with other new animation features?](#213-how-do-you-use-supports-with-other-new-animation-features)
- [214: How do you make a rotating gradient border?](#214-how-do-you-make-a-rotating-gradient-border)
- [215: How do you smoothly animate gradient colors?](#215-how-do-you-smoothly-animate-gradient-colors)
- [216: How do you animate a number counting up with CSS only?](#216-how-do-you-animate-a-number-counting-up-with-css-only)
- [217: Why set inherits: false on animated custom properties?](#217-why-set-inherits-false-on-animated-custom-properties)
- [218: How do you register a custom property from JavaScript?](#218-how-do-you-register-a-custom-property-from-javascript)
- [219: What is the difference between animation-composition add and accumulate?](#219-what-is-the-difference-between-animation-composition-add-and-accumulate)
- [220: How do you combine a hover transform with a running keyframe animation on the same element?](#220-how-do-you-combine-a-hover-transform-with-a-running-keyframe-animation-on-the-same-element)
- [221: How can one transitioned custom property drive several values?](#221-how-can-one-transitioned-custom-property-drive-several-values)
- [222: How can sibling-index() help with staggered animations?](#222-how-can-sibling-index-help-with-staggered-animations)
- [223: Should enter and exit animations have the same duration?](#223-should-enter-and-exit-animations-have-the-same-duration)
- [224: How do you play several animations one after another on the same element?](#224-how-do-you-play-several-animations-one-after-another-on-the-same-element)
- [225: How does fill-mode work together with alternate and iteration count?](#225-how-does-fill-mode-work-together-with-alternate-and-iteration-count)
- [226: How do you make a ticking clock hand with CSS?](#226-how-do-you-make-a-ticking-clock-hand-with-css)
- [227: Why use tabular-nums for animated numbers?](#227-why-use-tabular-nums-for-animated-numbers)
- [228: How do you make a loading spinner accessible?](#228-how-do-you-make-a-loading-spinner-accessible)
- [229: What happens to CSS animations in background tabs?](#229-what-happens-to-css-animations-in-background-tabs)
- [230: Do infinite animations off-screen cost anything?](#230-do-infinite-animations-off-screen-cost-anything)
- [231: How does content-visibility: auto relate to animations?](#231-how-does-content-visibility-auto-relate-to-animations)
- [232: How do you add an exit animation to an element that a framework removes from the DOM?](#232-how-do-you-add-an-exit-animation-to-an-element-that-a-framework-removes-from-the-dom)
- [233: How does Vue's Transition component work with CSS?](#233-how-does-vues-transition-component-work-with-css)
- [234: How do modern Angular versions handle enter and leave animations?](#234-how-do-modern-angular-versions-handle-enter-and-leave-animations)
- [235: How do you add custom animations in Tailwind CSS?](#235-how-do-you-add-custom-animations-in-tailwind-css)
- [236: What is layout thrashing and how does it affect JS-driven animations?](#236-what-is-layout-thrashing-and-how-does-it-affect-js-driven-animations)
- [237: Why use requestAnimationFrame instead of setInterval for JS animations?](#237-why-use-requestanimationframe-instead-of-setinterval-for-js-animations)
- [238: Why doesn't a transition run when you add an element and its class at the same time?](#238-why-doesnt-a-transition-run-when-you-add-an-element-and-its-class-at-the-same-time)
- [239: What is the double requestAnimationFrame trick?](#239-what-is-the-double-requestanimationframe-trick)
- [240: How do you find out why an animation is janky?](#240-how-do-you-find-out-why-an-animation-is-janky)
- [241: What does paint flashing show you?](#241-what-does-paint-flashing-show-you)
- [242: How do you check which elements have their own compositor layer?](#242-how-do-you-check-which-elements-have-their-own-compositor-layer)
- [243: Do animations affect Cumulative Layout Shift?](#243-do-animations-affect-cumulative-layout-shift)
- [244: How can animations hurt Interaction to Next Paint (INP)?](#244-how-can-animations-hurt-interaction-to-next-paint-inp)
- [245: How do you make an image zoom on hover without overflowing its card?](#245-how-do-you-make-an-image-zoom-on-hover-without-overflowing-its-card)
- [246: Can you animate object-position?](#246-can-you-animate-object-position)
- [247: Which SVG attributes can you animate with CSS?](#247-which-svg-attributes-can-you-animate-with-css)
- [248: What is transform-box and why does it matter for SVG?](#248-what-is-transform-box-and-why-does-it-matter-for-svg)
- [249: Should you use SMIL or CSS for SVG animations?](#249-should-you-use-smil-or-css-for-svg-animations)
- [250: How do you morph one shape into another with clip-path?](#250-how-do-you-morph-one-shape-into-another-with-clip-path)
- [251: How do you cycle through colors cheaply?](#251-how-do-you-cycle-through-colors-cheaply)
- [252: Why do dark mode toggles sometimes look bad with transitions, and how do you fix it?](#252-why-do-dark-mode-toggles-sometimes-look-bad-with-transitions-and-how-do-you-fix-it)
- [253: How do you make a circular reveal when switching themes?](#253-how-do-you-make-a-circular-reveal-when-switching-themes)
- [254: Why do some pages show transitions running on page load, and how do you stop it?](#254-why-do-some-pages-show-transitions-running-on-page-load-and-how-do-you-stop-it)
- [255: Can media queries trigger transitions?](#255-can-media-queries-trigger-transitions)
- [256: How do you animate text letter by letter without hurting accessibility?](#256-how-do-you-animate-text-letter-by-letter-without-hurting-accessibility)
- [257: How do you animate gradient text?](#257-how-do-you-animate-gradient-text)
- [258: How do you draw a border around a box on hover?](#258-how-do-you-draw-a-border-around-a-box-on-hover)
- [259: What are motion tokens in a design system?](#259-what-are-motion-tokens-in-a-design-system)
- [260: Should duration depend on the size of the animated element?](#260-should-duration-depend-on-the-size-of-the-animated-element)
- [261: How do you make a spring animation with CSS?](#261-how-do-you-make-a-spring-animation-with-css)
- [262: How do you make an element orbit around a point?](#262-how-do-you-make-an-element-orbit-around-a-point)
- [263: How do you build a rotating 3D cube?](#263-how-do-you-build-a-rotating-3d-cube)
- [264: What does perspective-origin do?](#264-what-does-perspective-origin-do)
- [265: How do you make a card tilt toward the mouse?](#265-how-do-you-make-a-card-tilt-toward-the-mouse)
- [266: Can you animate variable font axes?](#266-can-you-animate-variable-font-axes)
- [267: Why can animating font-weight cause layout shifts?](#267-why-can-animating-font-weight-cause-layout-shifts)
- [268: How do you make a modal look like it grows from the button that opened it?](#268-how-do-you-make-a-modal-look-like-it-grows-from-the-button-that-opened-it)
- [269: How do you animate a stack of toasts so others move when one is removed?](#269-how-do-you-animate-a-stack-of-toasts-so-others-move-when-one-is-removed)
- [270: Can you animate grid-template-columns?](#270-can-you-animate-grid-template-columns)
- [271: Can you animate flex-grow and flex-basis?](#271-can-you-animate-flex-grow-and-flex-basis)
- [272: Can you animate gap?](#272-can-you-animate-gap)
- [273: How does z-index animate?](#273-how-does-z-index-animate)
- [274: Can you animate the content property?](#274-can-you-animate-the-content-property)
- [275: What does scroll-behavior: smooth do?](#275-what-does-scroll-behavior-smooth-do)
- [276: Should you turn off smooth scrolling for reduced motion?](#276-should-you-turn-off-smooth-scrolling-for-reduced-motion)
- [277: How do scroll-driven animations work with scroll snap carousels?](#277-how-do-scroll-driven-animations-work-with-scroll-snap-carousels)
- [278: How many animations can run at the same time?](#278-how-many-animations-can-run-at-the-same-time)
- [279: How do you deal with animations in end-to-end tests?](#279-how-do-you-deal-with-animations-in-end-to-end-tests)
- [280: Why do visual regression tests fail on animated pages?](#280-why-do-visual-regression-tests-fail-on-animated-pages)
- [281: Do CSS animations run in jsdom?](#281-do-css-animations-run-in-jsdom)
- [282: How do CSS Modules handle keyframe names?](#282-how-do-css-modules-handle-keyframe-names)
- [283: How do you define keyframes in CSS-in-JS libraries?](#283-how-do-you-define-keyframes-in-css-in-js-libraries)
- [284: Can you put @keyframes inside a media query?](#284-can-you-put-keyframes-inside-a-media-query)
- [285: How do @keyframes rules behave in cascade layers?](#285-how-do-keyframes-rules-behave-in-cascade-layers)
- [286: How do keyframes work with shadow DOM?](#286-how-do-keyframes-work-with-shadow-dom)
- [287: How can :has() trigger animations?](#287-how-can-has-trigger-animations)
- [288: How do you trigger animations with :checked without JavaScript?](#288-how-do-you-trigger-animations-with-checked-without-javascript)
- [289: How do you trigger an animation once when an element scrolls into view, using JavaScript?](#289-how-do-you-trigger-an-animation-once-when-an-element-scrolls-into-view-using-javascript)
- [290: Why can animating a full-page background be slow?](#290-why-can-animating-a-full-page-background-be-slow)
- [291: Can too many composited layers cause problems?](#291-can-too-many-composited-layers-cause-problems)
- [292: How do you make many looping animations look random without JavaScript?](#292-how-do-you-make-many-looping-animations-look-random-without-javascript)
- [293: How do you build a ripple effect on click?](#293-how-do-you-build-a-ripple-effect-on-click)
- [294: How do you animate a check mark being drawn?](#294-how-do-you-animate-a-check-mark-being-drawn)
- [295: How do you animate an accordion to its real height with JavaScript?](#295-how-do-you-animate-an-accordion-to-its-real-height-with-javascript)
- [296: How do you cross-fade between two views without view transitions?](#296-how-do-you-cross-fade-between-two-views-without-view-transitions)
- [297: What happens when a transition and a keyframe animation affect the same property?](#297-what-happens-when-a-transition-and-a-keyframe-animation-affect-the-same-property)
- [298: Do changes made by a CSS animation trigger transitions?](#298-do-changes-made-by-a-css-animation-trigger-transitions)
- [299: Why does my position: fixed child stop being fixed when the parent animates transform?](#299-why-does-my-position-fixed-child-stop-being-fixed-when-the-parent-animates-transform)
- [300: Why does z-index break when an element is being transformed?](#300-why-does-z-index-break-when-an-element-is-being-transformed)

### Advanced Questions (301-450)

- [301: What are the main steps the browser takes to render a frame?](#301-what-are-the-main-steps-the-browser-takes-to-render-a-frame)
- [302: Which rendering steps do different properties trigger?](#302-which-rendering-steps-do-different-properties-trigger)
- [303: Why can a transform animation keep running while JavaScript blocks the main thread?](#303-why-can-a-transform-animation-keep-running-while-javascript-blocks-the-main-thread)
- [304: When does a transform or opacity animation not run on the compositor?](#304-when-does-a-transform-or-opacity-animation-not-run-on-the-compositor)
- [305: Why are transform and opacity animations cheap once composited?](#305-why-are-transform-and-opacity-animations-cheap-once-composited)
- [306: What is implicit compositing or layer explosion?](#306-what-is-implicit-compositing-or-layer-explosion)
- [307: What is the right way to use will-change?](#307-what-is-the-right-way-to-use-will-change)
- [308: What side effects does will-change: transform have?](#308-what-side-effects-does-will-change-transform-have)
- [309: Why does text sometimes look blurry during or after a scale animation?](#309-why-does-text-sometimes-look-blurry-during-or-after-a-scale-animation)
- [310: What is pixel snapping and how does it affect animations?](#310-what-is-pixel-snapping-and-how-does-it-affect-animations)
- [311: What does a 120 Hz screen change for animations?](#311-what-does-a-120-hz-screen-change-for-animations)
- [312: What is the frame budget, and what eats into it?](#312-what-is-the-frame-budget-and-what-eats-into-it)
- [313: Why is animating a custom property on :root expensive?](#313-why-is-animating-a-custom-property-on-root-expensive)
- [314: Do @property animations run on the compositor?](#314-do-property-animations-run-on-the-compositor)
- [315: What is the CSS Paint API and how does it relate to animations?](#315-what-is-the-css-paint-api-and-how-does-it-relate-to-animations)
- [316: What happened to Animation Worklet?](#316-what-happened-to-animation-worklet)
- [317: How does the browser interpolate between two transform lists?](#317-how-does-the-browser-interpolate-between-two-transform-lists)
- [318: Why does animating from rotate(0deg) to rotate(360deg) work, but a matrix-based transition doesn't spin?](#318-why-does-animating-from-rotate0deg-to-rotate360deg-work-but-a-matrix-based-transition-doesnt-spin)
- [319: How are 3D rotations interpolated?](#319-how-are-3d-rotations-interpolated)
- [320: How are the individual transform properties combined with transform?](#320-how-are-the-individual-transform-properties-combined-with-transform)
- [321: How are colors with transparency interpolated?](#321-how-are-colors-with-transparency-interpolated)
- [322: Can you control the color space a transition uses?](#322-can-you-control-the-color-space-a-transition-uses)
- [323: How does the browser interpolate box-shadow lists of different lengths?](#323-how-does-the-browser-interpolate-box-shadow-lists-of-different-lengths)
- [324: How are filter lists interpolated?](#324-how-are-filter-lists-interpolated)
- [325: How does interpolation between lengths in different units work?](#325-how-does-interpolation-between-lengths-in-different-units-work)
- [326: Why is interpolate-size opt-in instead of on by default?](#326-why-is-interpolate-size-opt-in-instead-of-on-by-default)
- [327: What can calc-size() do that interpolate-size can't?](#327-what-can-calc-size-do-that-interpolate-size-cant)
- [328: What are the before-change style and after-change style in transitions?](#328-what-are-the-before-change-style-and-after-change-style-in-transitions)
- [329: Why do elements inside a display: none container not transition?](#329-why-do-elements-inside-a-display-none-container-not-transition)
- [330: What is a timeline in the Web Animations model?](#330-what-is-a-timeline-in-the-web-animations-model)
- [331: In what order are animation effects stacked on the same property?](#331-in-what-order-are-animation-effects-stacked-on-the-same-property)
- [332: What happens if you change animation-duration while an animation runs?](#332-what-happens-if-you-change-animation-duration-while-an-animation-runs)
- [333: What happens if you change animation-name on a running animation?](#333-what-happens-if-you-change-animation-name-on-a-running-animation)
- [334: How do CSS animation-play-state and JavaScript pause() interact?](#334-how-do-css-animation-play-state-and-javascript-pause-interact)
- [335: What is automatic removal of filling animations?](#335-what-is-automatic-removal-of-filling-animations)
- [336: What do getTiming(), getComputedTiming() and updateTiming() do?](#336-what-do-gettiming-getcomputedtiming-and-updatetiming-do)
- [337: How do you create scroll-driven animations from JavaScript?](#337-how-do-you-create-scroll-driven-animations-from-javascript)
- [338: Do scroll-driven animations run off the main thread?](#338-do-scroll-driven-animations-run-off-the-main-thread)
- [339: What happens to a scroll-driven animation if its container can't scroll?](#339-what-happens-to-a-scroll-driven-animation-if-its-container-cant-scroll)
- [340: Can you use range names inside @keyframes?](#340-can-you-use-range-names-inside-keyframes)
- [341: Can CSS start a time-based animation when an element scrolls into view?](#341-can-css-start-a-time-based-animation-when-an-element-scrolls-into-view)
- [342: What does the browser actually do during a view transition?](#342-what-does-the-browser-actually-do-during-a-view-transition)
- [343: What does it mean that old view transition snapshots are static images?](#343-what-does-it-mean-that-old-view-transition-snapshots-are-static-images)
- [344: Why do elements look stretched in a view transition, and how do you fix it?](#344-why-do-elements-look-stretched-in-a-view-transition-and-how-do-you-fix-it)
- [345: Why do named elements escape overflow: hidden during a view transition?](#345-why-do-named-elements-escape-overflow-hidden-during-a-view-transition)
- [346: Can users interact with the page during a view transition?](#346-can-users-interact-with-the-page-during-a-view-transition)
- [347: What happens if the update callback in startViewTransition takes too long?](#347-what-happens-if-the-update-callback-in-startviewtransition-takes-too-long)
- [348: How do you avoid a flash of incomplete content in cross-document view transitions?](#348-how-do-you-avoid-a-flash-of-incomplete-content-in-cross-document-view-transitions)
- [349: When do cross-document view transitions happen?](#349-when-do-cross-document-view-transitions-happen)
- [350: What does a view transition cost in memory?](#350-what-does-a-view-transition-cost-in-memory)
- [351: Why do you often need flushSync when using view transitions with React?](#351-why-do-you-often-need-flushsync-when-using-view-transitions-with-react)
- [352: How do you debug a view transition?](#352-how-do-you-debug-a-view-transition)
- [353: How does the default view transition cross-fade avoid a "see-through" moment?](#353-how-does-the-default-view-transition-cross-fade-avoid-a-see-through-moment)
- [354: When would you choose FLIP over view transitions, and the other way round?](#354-when-would-you-choose-flip-over-view-transitions-and-the-other-way-round)
- [355: How do you do a list-to-detail shared element transition with many items?](#355-how-do-you-do-a-list-to-detail-shared-element-transition-with-many-items)
- [356: A dropdown animation stutters on low-end Android phones. How do you investigate?](#356-a-dropdown-animation-stutters-on-low-end-android-phones-how-do-you-investigate)
- [357: A hover animation flickers when the mouse is near the edge. Why, and how do you fix it?](#357-a-hover-animation-flickers-when-the-mouse-is-near-the-edge-why-and-how-do-you-fix-it)
- [358: An animation stutters only in its first few frames. What could cause that?](#358-an-animation-stutters-only-in-its-first-few-frames-what-could-cause-that)
- [359: An element jumps at the end of its animation. What are the likely causes?](#359-an-element-jumps-at-the-end-of-its-animation-what-are-the-likely-causes)
- [360: A loading spinner freezes while the app does heavy work. How do you fix it?](#360-a-loading-spinner-freezes-while-the-app-does-heavy-work-how-do-you-fix-it)
- [361: What causes flicker with 3D transforms in Safari, and how do you fix it?](#361-what-causes-flicker-with-3d-transforms-in-safari-and-how-do-you-fix-it)
- [362: How do you animate items in a list of 1,000 elements without it being slow?](#362-how-do-you-animate-items-in-a-list-of-1000-elements-without-it-being-slow)
- [363: How do you animate a sidebar that pushes the main content aside?](#363-how-do-you-animate-a-sidebar-that-pushes-the-main-content-aside)
- [364: Users report that your site makes them feel sick. What do you check?](#364-users-report-that-your-site-makes-them-feel-sick-what-do-you-check)
- [365: An animation works in Chrome but not in Safari. What do you check?](#365-an-animation-works-in-chrome-but-not-in-safari-what-do-you-check)
- [366: How can an entrance animation hurt Largest Contentful Paint?](#366-how-can-an-entrance-animation-hurt-largest-contentful-paint)
- [367: Design wants all 50 product cards to fade in one after another on page load. What do you say?](#367-design-wants-all-50-product-cards-to-fade-in-one-after-another-on-page-load-what-do-you-say)
- [368: What problems can animations cause with server rendering and hydration?](#368-what-problems-can-animations-cause-with-server-rendering-and-hydration)
- [369: Why is hiding content until JavaScript adds an "animate-in" class risky?](#369-why-is-hiding-content-until-javascript-adds-an-animate-in-class-risky)
- [370: Why can't you animate most styles on :visited links?](#370-why-cant-you-animate-most-styles-on-visited-links)
- [371: How does Content Security Policy affect animations?](#371-how-does-content-security-policy-affect-animations)
- [372: Can you limit an animation to a lower frame rate on purpose?](#372-can-you-limit-an-animation-to-a-lower-frame-rate-on-purpose)
- [373: Why might animations in an iframe stop or slow down?](#373-why-might-animations-in-an-iframe-stop-or-slow-down)
- [374: Is it better to animate one parent or every child?](#374-is-it-better-to-animate-one-parent-or-every-child)
- [375: Are SVG animations as fast as HTML animations?](#375-are-svg-animations-as-fast-as-html-animations)
- [376: When should you use canvas or WebGL instead of CSS animations?](#376-when-should-you-use-canvas-or-webgl-instead-of-css-animations)
- [377: How would you set up animation in a large application?](#377-how-would-you-set-up-animation-in-a-large-application)
- [378: What kinds of motion are most likely to cause problems for people with vestibular disorders?](#378-what-kinds-of-motion-are-most-likely-to-cause-problems-for-people-with-vestibular-disorders)
- [379: Should you rely on the OS reduced motion setting or add an in-app setting?](#379-should-you-rely-on-the-os-reduced-motion-setting-or-add-an-in-app-setting)
- [380: Why does a CSS animation restart when a React component re-renders with a new key?](#380-why-does-a-css-animation-restart-when-a-react-component-re-renders-with-a-new-key)
- [381: How do you let users of a web component customize its animations?](#381-how-do-you-let-users-of-a-web-component-customize-its-animations)
- [382: Why is transitioning font-size on the html element a bad idea?](#382-why-is-transitioning-font-size-on-the-html-element-a-bad-idea)
- [383: Why can animating a large blur be slow?](#383-why-can-animating-a-large-blur-be-slow)
- [384: Why is backdrop-filter expensive to animate?](#384-why-is-backdrop-filter-expensive-to-animate)
- [385: Does mix-blend-mode affect animation performance?](#385-does-mix-blend-mode-affect-animation-performance)
- [386: Can clip-path or background-color animations run on the compositor?](#386-can-clip-path-or-background-color-animations-run-on-the-compositor)
- [387: How do you approach cross-browser animation bugs?](#387-how-do-you-approach-cross-browser-animation-bugs)
- [388: What are the animation types in the CSS specs?](#388-what-are-the-animation-types-in-the-css-specs)
- [389: Which properties are not animatable at all?](#389-which-properties-are-not-animatable-at-all)
- [390: What happens to percentage values in translate if the element changes size during the animation?](#390-what-happens-to-percentage-values-in-translate-if-the-element-changes-size-during-the-animation)
- [391: How is animation-timing-function applied in a multi-keyframe animation?](#391-how-is-animation-timing-function-applied-in-a-multi-keyframe-animation)
- [392: How do you make a multi-step CSS animation move at an even speed through all the keyframes?](#392-how-do-you-make-a-multi-step-css-animation-move-at-an-even-speed-through-all-the-keyframes)
- [393: How does steps() behave in a keyframe animation with several keyframes?](#393-how-does-steps-behave-in-a-keyframe-animation-with-several-keyframes)
- [394: How do you find animations running on a pseudo-element from JavaScript?](#394-how-do-you-find-animations-running-on-a-pseudo-element-from-javascript)
- [395: Can element.animate() target a pseudo-element?](#395-can-elementanimate-target-a-pseudo-element)
- [396: How do you keep several animations in sync if they start at different times?](#396-how-do-you-keep-several-animations-in-sync-if-they-start-at-different-times)
- [397: Why do skeleton shimmers look out of sync, and how do you fix it?](#397-why-do-skeleton-shimmers-look-out-of-sync-and-how-do-you-fix-it)
- [398: How do you build a sequence of animations without group or sequence effects?](#398-how-do-you-build-a-sequence-of-animations-without-group-or-sequence-effects)
- [399: Why can em or container query units change while an animation runs?](#399-why-can-em-or-container-query-units-change-while-an-animation-runs)
- [400: What is the Long Animation Frames API?](#400-what-is-the-long-animation-frames-api)
- [401: How can you measure animation smoothness for real users?](#401-how-can-you-measure-animation-smoothness-for-real-users)
- [402: How do you find out why an animation isn't running on the compositor?](#402-how-do-you-find-out-why-an-animation-isnt-running-on-the-compositor)
- [403: What do you need to think about when building an auto-advancing carousel?](#403-what-do-you-need-to-think-about-when-building-an-auto-advancing-carousel)
- [404: How would you build animated statistics that count up when they scroll into view?](#404-how-would-you-build-animated-statistics-that-count-up-when-they-scroll-into-view)
- [405: How do you swap a skeleton for real content without layout shift?](#405-how-do-you-swap-a-skeleton-for-real-content-without-layout-shift)
- [406: How would you animate a product image from a listing page into a product page on a multi-page site?](#406-how-would-you-animate-a-product-image-from-a-listing-page-into-a-product-page-on-a-multi-page-site)
- [407: An infinite animation uses a lot of CPU on some computers. Why?](#407-an-infinite-animation-uses-a-lot-of-cpu-on-some-computers-why)
- [408: Should you use Lottie or CSS for an animated logo?](#408-should-you-use-lottie-or-css-for-an-animated-logo)
- [409: How do you decide whether an animation library is worth its bundle size?](#409-how-do-you-decide-whether-an-animation-library-is-worth-its-bundle-size)
- [410: An animated tooltip gets cut off inside a scrolling container. How do you fix it?](#410-an-animated-tooltip-gets-cut-off-inside-a-scrolling-container-how-do-you-fix-it)
- [411: An exit animation works in one browser but the element just disappears in another. What's going on?](#411-an-exit-animation-works-in-one-browser-but-the-element-just-disappears-in-another-whats-going-on)
- [412: Why do hover effects built with keyframe animations look worse than ones built with transitions?](#412-why-do-hover-effects-built-with-keyframe-animations-look-worse-than-ones-built-with-transitions)
- [413: How do you avoid a spinner that flashes for a split second on fast loads?](#413-how-do-you-avoid-a-spinner-that-flashes-for-a-split-second-on-fast-loads)
- [414: A mega menu animation makes interactions feel slow. How do you improve it?](#414-a-mega-menu-animation-makes-interactions-feel-slow-how-do-you-improve-it)
- [415: What do you look for when reviewing animation code?](#415-what-do-you-look-for-when-reviewing-animation-code)
- [416: Why can animating heights with ResizeObserver create loops?](#416-why-can-animating-heights-with-resizeobserver-create-loops)
- [417: How do you design animations that can be interrupted?](#417-how-do-you-design-animations-that-can-be-interrupted)
- [418: Why can a transition that changes direction feel unnatural?](#418-why-can-a-transition-that-changes-direction-feel-unnatural)
- [419: How do you animate an element after a drag is released?](#419-how-do-you-animate-an-element-after-a-drag-is-released)
- [420: What do you need for smooth gesture-driven animations on touch devices?](#420-what-do-you-need-for-smooth-gesture-driven-animations-on-touch-devices)
- [421: How would you build swipe-to-dismiss for a notification?](#421-how-would-you-build-swipe-to-dismiss-for-a-notification)
- [422: Why might an animation measure the wrong sizes when it runs right on page load?](#422-why-might-an-animation-measure-the-wrong-sizes-when-it-runs-right-on-page-load)
- [423: How do you handle animations in right-to-left layouts?](#423-how-do-you-handle-animations-in-right-to-left-layouts)
- [424: How do you place and animate items in a circle with CSS math functions?](#424-how-do-you-place-and-animate-items-in-a-circle-with-css-math-functions)
- [425: How should focus be handled during animated transitions?](#425-how-should-focus-be-handled-during-animated-transitions)
- [426: How do you test that reduced motion works?](#426-how-do-you-test-that-reduced-motion-works)
- [427: Is prefers-reduced-motion a privacy concern?](#427-is-prefers-reduced-motion-a-privacy-concern)
- [428: How can CSS containment reduce the cost of animations?](#428-how-can-css-containment-reduce-the-cost-of-animations)
- [429: How can scroll event handlers hurt scroll-linked animations?](#429-how-can-scroll-event-handlers-hurt-scroll-linked-animations)
- [430: Why does linear motion often look robotic?](#430-why-does-linear-motion-often-look-robotic)
- [431: How do animations affect perceived performance?](#431-how-do-animations-affect-perceived-performance)
- [432: How do animations work with optimistic UI updates?](#432-how-do-animations-work-with-optimistic-ui-updates)
- [433: Why do all the cards fade in when the page loads after adding @starting-style?](#433-why-do-all-the-cards-fade-in-when-the-page-loads-after-adding-starting-style)
- [434: What happens to animations when an element is moved in the DOM?](#434-what-happens-to-animations-when-an-element-is-moved-in-the-dom)
- [435: How do you coordinate animations between components that don't know about each other?](#435-how-do-you-coordinate-animations-between-components-that-dont-know-about-each-other)
- [436: Should animation states be driven by classes or data attributes?](#436-should-animation-states-be-driven-by-classes-or-data-attributes)
- [437: How do you animate theme changes across a whole design system?](#437-how-do-you-animate-theme-changes-across-a-whole-design-system)
- [438: How would you build an accessible modal with open and close animations?](#438-how-would-you-build-an-accessible-modal-with-open-and-close-animations)
- [439: How would you build a carousel with scroll snap and animated indicators?](#439-how-would-you-build-a-carousel-with-scroll-snap-and-animated-indicators)
- [440: Why is "transition: all 0.3s" on every element a bad idea in a large app?](#440-why-is-transition-all-03s-on-every-element-a-bad-idea-in-a-large-app)
- [441: How do you animate a list when it's sorted?](#441-how-do-you-animate-a-list-when-its-sorted)
- [442: Why does an animation run twice in a React app during development?](#442-why-does-an-animation-run-twice-in-a-react-app-during-development)
- [443: How do you handle a toggle that the user clicks quickly many times?](#443-how-do-you-handle-a-toggle-that-the-user-clicks-quickly-many-times)
- [444: How do you choose between a CSS transition, a keyframe animation, the Web Animations API, a view transition and a scroll-driven animation?](#444-how-do-you-choose-between-a-css-transition-a-keyframe-animation-the-web-animations-api-a-view-transition-and-a-scroll-driven-animation)
- [445: What new animation features are worth watching?](#445-what-new-animation-features-are-worth-watching)
- [446: How do you keep an animated SVG icon crisp at any size?](#446-how-do-you-keep-an-animated-svg-icon-crisp-at-any-size)
- [447: How do you make a CSS animation pause when the user switches tabs and continue later?](#447-how-do-you-make-a-css-animation-pause-when-the-user-switches-tabs-and-continue-later)
- [448: An animation is only slow when DevTools is open. Should you worry?](#448-an-animation-is-only-slow-when-devtools-is-open-should-you-worry)
- [449: What are the risks of animating layout in a component library used by many apps?](#449-what-are-the-risks-of-animating-layout-in-a-component-library-used-by-many-apps)
- [450: In one minute, how would you explain to an interviewer what makes a good CSS animation?](#450-in-one-minute-how-would-you-explain-to-an-interviewer-what-makes-a-good-css-animation)

---

# Easy Questions (1-150)

## 1: What ways do you have to animate things with CSS?

There are two main tools. A transition animates a property from its old value to its new value when the value changes, for example on hover. A keyframe animation (`@keyframes` plus the `animation` property) runs a set of steps you define, and it can start on its own, loop and go through many states. On top of these, newer features like view transitions and scroll-driven animations build on the same ideas.

## 2: What is a CSS transition?

A transition tells the browser: "when this property changes, don't jump to the new value, move to it over some time". You set it on the element, and it runs every time the property changes, in both directions.

```css
.button {
  background: steelblue;
  transition: background 200ms ease;
}

.button:hover {
  background: navy;
}
```

## 3: What is a CSS keyframe animation?

It is an animation defined with `@keyframes`, where you list the styles at different points in time (0%, 50%, 100% and so on). You attach it to an element with the `animation` property. Unlike a transition, it doesn't need a state change to start, and it can repeat.

```css
@keyframes pulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.1);
  }
  100% {
    transform: scale(1);
  }
}

.badge {
  animation: pulse 1s ease-in-out infinite;
}
```

## 4: What is the difference between a transition and an animation?

A transition needs a trigger: some property value has to change (hover, a class added by JavaScript, focus). It only knows the start and end values. An animation runs as soon as it is applied, can have many steps, can loop, and can run in reverse or alternate. Use transitions for simple state changes and animations for anything with more than two steps or that should play on its own.

## 5: What are the transition properties?

There are five long-hand properties and one shorthand:

- `transition-property`: which properties to animate.
- `transition-duration`: how long it takes.
- `transition-timing-function`: the speed curve.
- `transition-delay`: how long to wait before starting.
- `transition-behavior`: whether discrete properties (like `display`) can transition.
- `transition`: the shorthand for all of them.

## 6: How do you write the transition shorthand?

The order is property, duration, timing function, delay. The first time value is always the duration and the second is always the delay.

```css
.card {
  transition: transform 300ms ease-out 100ms;
}
```

You can list several transitions separated by commas, for example `transition: opacity 200ms, transform 300ms;`.

## 7: What happens if you set transition-duration to 0?

Nothing animates: the property jumps straight to the new value. The default duration is `0s`, which is why you only get a transition when you set a duration.

## 8: What does transition-property: all do, and why is it not a good default?

`all` animates every property that can be animated when it changes. It's easy to write, but it can animate things you didn't plan for, like `width` or `color` changes from a media query, and it makes the browser check more properties. It's better to list the properties you mean, for example `transition: opacity 200ms, transform 200ms;`.

## 9: What units can you use for durations and delays?

Seconds (`s`) and milliseconds (`ms`). `0.3s` and `300ms` mean the same thing. A unit is required: `transition-duration: 300` is invalid and gets ignored.

## 10: What is a timing function?

A timing function (also called an easing function) controls how the speed changes during the animation. With `linear` the speed stays the same. With `ease-out` it starts fast and slows down at the end. The total time stays the same; only the speed along the way changes.

## 11: What timing function keywords does CSS have?

- `ease` (default): speeds up quickly, then slows down.
- `linear`: same speed the whole time.
- `ease-in`: starts slow, ends fast.
- `ease-out`: starts fast, ends slow.
- `ease-in-out`: slow at both ends.
- `step-start` and `step-end`: jump in one step.

There are also the functions `cubic-bezier()`, `steps()` and `linear()`.

## 12: When should you use ease-out vs ease-in?

Use `ease-out` for things that enter the screen or respond to the user, like a menu opening. It starts fast, so it feels responsive. Use `ease-in` for things that leave the screen, because they speed up as they go away. `ease-in-out` fits things that move from one place to another on the screen.

## 13: What is the default timing function for transitions and animations?

`ease`, for both. Many developers forget this and are surprised that `linear` motion, like a spinner, looks uneven until they set `linear` themselves.

## 14: How do you define keyframes?

Use the `@keyframes` rule with a name and a list of steps. Steps are percentages of the animation duration. `from` is the same as `0%` and `to` is the same as `100%`.

```css
@keyframes slide-in {
  from {
    transform: translateX(-100%);
  }
  to {
    transform: translateX(0);
  }
}
```

## 15: What are the animation properties?

- `animation-name`
- `animation-duration`
- `animation-timing-function`
- `animation-delay`
- `animation-iteration-count`
- `animation-direction`
- `animation-fill-mode`
- `animation-play-state`
- `animation-composition`
- `animation-timeline`, `animation-range-start`, `animation-range-end` (for scroll-driven animations)

The `animation` shorthand sets most of these at once.

## 16: How do you write the animation shorthand?

```css
.loader {
  /* name | duration | timing | delay | count | direction | fill | state */
  animation: spin 1s linear 0s infinite normal none running;
}
```

The order of most values doesn't matter, except that the first time is the duration and the second is the delay. Most of the time you only write a few: `animation: spin 1s linear infinite;`.

## 17: What does animation-iteration-count do?

It sets how many times the animation plays. The default is `1`. You can use any number, including decimals like `2.5` (it stops halfway through the third run), or `infinite` to loop forever.

## 18: What does animation-direction do?

It sets which way the keyframes play:

- `normal`: 0% to 100% every time.
- `reverse`: 100% to 0% every time.
- `alternate`: forward, then backward, then forward...
- `alternate-reverse`: backward first, then forward, and so on.

`alternate` is handy for things like a "breathing" effect, because the animation goes back smoothly instead of jumping to the start.

## 19: What does animation-fill-mode do?

It controls which styles apply before the animation starts (during the delay) and after it ends.

- `none` (default): keyframe styles only apply while it runs.
- `forwards`: keep the styles of the last keyframe after it ends.
- `backwards`: apply the first keyframe during the delay.
- `both`: do both.

## 20: Why does my element jump back to its start after the animation ends?

Because by default an animation's styles only apply while it runs. When it ends, the element goes back to its normal styles. Fix it with `animation-fill-mode: forwards`, or better, set the final values in the element's normal styles so the animation and the resting state match.

## 21: What does animation-play-state do?

It pauses or resumes an animation. The values are `running` (default) and `paused`. A paused animation stays where it is and continues from that point when set back to `running`.

```css
.marquee:hover {
  animation-play-state: paused;
}
```

## 22: What does animation-delay do?

It waits a given time before the animation starts. A positive value like `500ms` delays the start. A negative value starts the animation partway through, as if it had already been running for that long.

## 23: What does a negative animation-delay do?

The animation starts immediately but at a later point in its timeline. With `animation: spin 2s linear infinite; animation-delay: -1s;` the element starts at the halfway point. This is a common trick to make several items look out of sync without making some of them wait.

## 24: Can you apply more than one animation to an element?

Yes. Separate them with commas. Each long-hand property also takes a comma list, and values are matched by position.

```css
.icon {
  animation:
    fade-in 300ms ease-out,
    float 3s ease-in-out 300ms infinite alternate;
}
```

## 25: What happens if two keyframes animations change the same property?

By default the one listed last in `animation-name` wins for that property, because it replaces the result of the earlier ones. If you want them to add up instead, use `animation-composition: add` or `accumulate` (or animate different properties, like `translate` and `rotate`).

## 26: What does transform do?

`transform` moves, rotates, scales or skews an element visually, without changing the layout around it. Other elements don't move to make space. This makes it one of the best properties to animate.

```css
.box {
  transform: translateX(50px) rotate(10deg) scale(1.2);
}
```

## 27: What transform functions are there?

The common ones are:

- `translate()`, `translateX()`, `translateY()`, `translateZ()`, `translate3d()`
- `scale()`, `scaleX()`, `scaleY()`, `scaleZ()`, `scale3d()`
- `rotate()`, `rotateX()`, `rotateY()`, `rotateZ()`, `rotate3d()`
- `skew()`, `skewX()`, `skewY()`
- `matrix()`, `matrix3d()`
- `perspective()`

## 28: Does the order of transform functions matter?

Yes. Each function changes the coordinate system for the ones after it. `translateX(100px) rotate(45deg)` moves the element right and then rotates it in place. `rotate(45deg) translateX(100px)` rotates the axes first, so the element moves diagonally.

## 29: What are the individual transform properties?

`translate`, `rotate` and `scale` are separate CSS properties that work like the matching transform functions. They are applied in a fixed order: translate, then rotate, then scale, then `transform`.

```css
.box {
  translate: 20px 0;
  rotate: 15deg;
  scale: 1.1;
}
```

They let you change or animate one part (like `scale` on hover) without rewriting the whole `transform` value.

## 30: What does transform-origin do?

It sets the point that rotations and scaling happen around. The default is the center (`50% 50%`). For a door-opening effect you might use `transform-origin: left center`, so the element rotates around its left edge.

## 31: What is the difference between translate and changing top or left?

`top` and `left` change the layout position, so the browser has to recalculate layout on every frame. `translate` only moves the painted result, so the browser can usually do it on the GPU without layout or paint. Both look the same, but `translate` is much smoother, especially on slow devices.

## 32: Which properties can be animated?

Most properties with values that can be "in between" can be animated: lengths, percentages, numbers, colors, transforms, shadows, filters, and more. Each property's spec entry has an "Animation type" line that says how it animates. Properties with keyword values, like `display` or `position`, are discrete: they flip from one value to the other.

## 33: What is a discrete animation?

A discrete animation doesn't move smoothly between values. It switches from the start value to the end value at a single point. For most discrete properties that point is halfway (50%). `visibility` is an exception: if one end is `visible`, the element stays visible for the whole animation, so it only becomes hidden at the very end (or right at the start, going the other way).

## 34: Can you animate display?

In current browsers, yes, in a limited way. `display` is discrete, so it flips at one point. With keyframe animations it works directly. With transitions you need `transition-behavior: allow-discrete`, so the element stays visible while it fades out and only gets `display: none` at the end. To animate the element in when it first appears, you also need `@starting-style`.

## 35: Why does my transition not run when I change display: none to display: block?

When an element goes from `display: none` to `display: block`, it had no rendered "before" style, so there is nothing to transition from. The browser just shows the final state. The modern fix is `@starting-style`, which gives the browser the starting values to use the first time the element is rendered.

## 36: What is @starting-style?

`@starting-style` sets the styles an element should transition from the first time it gets rendered, for example when it is added to the page or goes from `display: none` to visible.

```css
.toast {
  opacity: 1;
  transition: opacity 300ms;
}

@starting-style {
  .toast {
    opacity: 0;
  }
}
```

It only affects transitions, not keyframe animations.

## 37: Can you animate opacity?

Yes, and it is one of the cheapest properties to animate. Like `transform`, it can usually be handled by the compositor without layout or paint. Fade effects are almost always done with `opacity`.

## 38: Can you animate colors?

Yes. `color`, `background-color`, `border-color`, `fill`, `stroke` and similar properties animate smoothly. Colors written in older formats (hex, `rgb()`, `hsl()`, names) are mixed in sRGB, which can look a bit muddy between very different colors. Newer formats like `oklch()` are mixed in Oklab, which usually looks cleaner.

## 39: Can you animate a background gradient directly?

Not directly in a smooth way. `background-image` with gradients is not interpolated by default, so the browser swaps one gradient for the other. Common workarounds are animating `background-position` on a large gradient, animating `opacity` of a layered gradient, or registering custom properties with `@property` and using them inside the gradient.

## 40: Can you animate height: auto?

Historically no: `auto` is not a number, so the browser can't find values in between. Common workarounds were animating `max-height`, using `grid-template-rows: 0fr` to `1fr`, or measuring the height in JavaScript. Chromium browsers now support `interpolate-size: allow-keywords` and `calc-size()` for this, but other browsers don't yet, so you still need the fallback.

## 41: What is a keyframe selector?

It's the percentage (or `from`/`to`) in front of each block inside `@keyframes`. It marks a point in time. You can put several selectors on one block, like `0%, 100% { opacity: 1; }`.

## 42: What happens if you leave out the 0% or 100% keyframe?

The browser uses the element's current computed value for that end. So `@keyframes grow { to { width: 300px; } }` starts from whatever width the element already has. This is useful for "animate from current state" effects.

## 43: Can keyframes include a timing function?

Yes. `animation-timing-function` inside a keyframe applies to the segment from that keyframe to the next one.

```css
@keyframes bounce {
  0% {
    transform: translateY(0);
    animation-timing-function: ease-out;
  }
  50% {
    transform: translateY(-40px);
    animation-timing-function: ease-in;
  }
  100% {
    transform: translateY(0);
  }
}
```

## 44: Can you use !important inside keyframes?

No. Declarations with `!important` inside `@keyframes` are ignored. Animation styles also already beat normal styles, so you rarely need it.

## 45: What happens if two @keyframes rules have the same name?

The last one in the stylesheet wins. The rules are not merged. This can cause strange bugs when two libraries both define something like `fade-in`, so give keyframes specific names.

## 46: How do you make an infinite spinner?

```css
@keyframes spin {
  to {
    rotate: 360deg;
  }
}

.spinner {
  width: 32px;
  height: 32px;
  border: 3px solid #ddd;
  border-top-color: #333;
  border-radius: 50%;
  animation: spin 800ms linear infinite;
}
```

Use `linear` so the speed stays the same, otherwise it slows down every turn.

## 47: How do you make a fade-in animation?

```css
@keyframes fade-in {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.panel {
  animation: fade-in 300ms ease-out;
}
```

## 48: How do you make an element slide in from the left?

```css
@keyframes slide-in {
  from {
    transform: translateX(-100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

.drawer {
  animation: slide-in 400ms ease-out both;
}
```

## 49: How do you add a hover effect with a transition?

Put the `transition` on the base state, not only on `:hover`, so it animates both in and out.

```css
.card {
  transition:
    transform 200ms ease,
    box-shadow 200ms ease;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgb(0 0 0 / 0.15);
}
```

## 50: Why should the transition be on the base selector and not on :hover?

If you only put it on `:hover`, the transition applies only while hovering. When the mouse leaves, the element loses the `:hover` styles and the transition rule at the same time, so it jumps back instantly. Putting it on the base selector makes it animate in both directions.

## 51: What is cubic-bezier()?

`cubic-bezier(x1, y1, x2, y2)` lets you make your own easing curve. The curve always starts at (0, 0) and ends at (1, 1), and the four numbers are the two control points in between. The x values are time and must be between 0 and 1. The y values are progress and can go outside 0 to 1.

```css
.menu {
  transition: transform 300ms cubic-bezier(0.2, 0.8, 0.2, 1);
}
```

All the keywords are just preset curves: `ease` is `cubic-bezier(0.25, 0.1, 0.25, 1)`.

## 52: How do you make an overshoot or "back" effect with cubic-bezier?

Use a y value bigger than 1 (or smaller than 0). The animation goes past the end value and then comes back, which looks like a small bounce.

```css
.pop {
  transition: scale 400ms cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

Be careful with properties that can't go past their limits, like `opacity`, which just gets clamped.

## 53: What does steps() do?

`steps(n, position)` splits the animation into `n` equal jumps instead of a smooth change. It is used for sprite sheets, typewriter effects, clocks and other "frame by frame" effects.

```css
.ticker {
  animation: tick 1s steps(4, end) infinite;
}
```

## 54: What are the step positions in steps()?

The second argument says where the jumps happen:

- `jump-end` / `end` (default): jump at the end of each step, so the final value shows only at the very end.
- `jump-start` / `start`: jump at the start of each step.
- `jump-none`: no jump at either end, both the first and last values are held.
- `jump-both`: jump at both ends, which adds one extra step.

`step-start` is short for `steps(1, start)` and `step-end` for `steps(1, end)`.

## 55: How do you animate a sprite sheet with CSS?

Put all frames in one image in a row, show one frame at a time, and move the background with `steps()`.

```css
.runner {
  width: 64px;
  height: 64px;
  background: url("runner.png") 0 0;
  animation: run 600ms steps(8) infinite;
}

@keyframes run {
  to {
    background-position: -512px 0;
  } /* 8 frames * 64px */
}
```

## 56: What is the linear() easing function?

`linear()` takes a list of points and draws straight lines between them. With enough points you can draw almost any curve, including bounces and springs, which `cubic-bezier()` can't do. It works in all current browsers.

```css
.ball {
  animation: drop 1s linear(0, 0.25, 1 40%, 0.8, 1 70%, 0.95, 1);
}
```

People usually generate the list with an online tool instead of writing it by hand.

## 57: What is the difference between the linear keyword and the linear() function?

The `linear` keyword means constant speed. The `linear()` function lets you give your own points. `linear(0, 1)` is the same as the keyword, but `linear()` with more points can make complex curves.

## 58: How do you make a typewriter effect with CSS?

Animate the width of a monospace text box with `steps()` equal to the number of characters, and hide the overflow.

```css
.type {
  font-family: monospace;
  white-space: nowrap;
  overflow: hidden;
  width: 0;
  animation: typing 2s steps(20) forwards;
}

@keyframes typing {
  to {
    width: 20ch;
  }
}
```

## 59: What is prefers-reduced-motion?

It's a media feature that tells you the user turned on a "reduce motion" setting in their operating system. Some people get dizzy or sick from large movement on screen. Your CSS should respect it.

```css
@media (prefers-reduced-motion: reduce) {
  .hero {
    animation: none;
  }
}
```

## 60: Should reduced motion mean no animation at all?

Not always. The goal is to remove motion that can cause problems: big movement, zooms, parallax and spinning. Small fades and color changes are usually fine and still help users understand what changed. A common approach is to swap slides and zooms for a short opacity fade.

## 61: What frame rate should animations aim for?

Most screens refresh 60 times per second, so a frame has about 16.7 ms. Many phones and monitors now run at 90, 120 or more, which leaves even less time. Smooth animation means the browser finishes every frame in time. When it misses frames, you see stutter, often called "jank".

## 62: Which properties are cheap to animate?

`transform` (and `translate`, `rotate`, `scale`) and `opacity` are the cheapest. In most cases the browser can animate them on the compositor, without layout or paint. `filter` is often cheap too. Try to build effects out of these.

## 63: Which properties are expensive to animate?

Properties that affect layout: `width`, `height`, `top`, `left`, `margin`, `padding`, `font-size`, `border-width` and so on. Changing them makes the browser recalculate the layout of the page and repaint, often on every frame. Properties like `background-color` or `box-shadow` don't change layout but still need a repaint each frame.

## 64: What is will-change?

`will-change` tells the browser that a property is going to change soon, so it can prepare, usually by putting the element on its own layer.

```css
.sidebar {
  will-change: transform;
}
```

Use it only for elements that really animate, and only when you see a real problem. Every layer costs memory.

## 65: How do you give different properties different durations in one transition?

List them separated by commas:

```css
.tooltip {
  transition:
    opacity 150ms ease-out,
    transform 300ms ease-out;
}
```

Or use comma lists in the long-hand properties, where values are matched by position.

## 66: What is transition-delay useful for?

It's handy for "hover intent": a dropdown that waits a bit before closing so it doesn't vanish when the mouse slips off for a moment. It's also used for staggering several elements and for running one transition after another on the same element.

```css
.dropdown {
  transition: opacity 200ms ease 0ms;
}

.nav:not(:hover) .dropdown {
  transition-delay: 300ms; /* wait before hiding */
}
```

## 67: What starts a transition?

A change in the computed value of a property listed in `transition-property`. The change can come from a pseudo-class (`:hover`, `:focus`), a class added by JavaScript, an inline style change, a media query or a changed custom property. If the computed value doesn't really change, nothing runs.

## 68: Do transitions run when the page first loads?

No. On first render there is no "before" value, so the element just shows its final style. To animate on load, use a keyframe animation or `@starting-style`.

## 69: How do you stop an animation with CSS?

Set `animation: none` (or `animation-name: none`). The animation is removed and the element goes back to its normal styles right away. If you want it to stay frozen where it is, use `animation-play-state: paused` instead.

## 70: What happens when a property appears in some keyframes but not in others?

Each property is animated on its own. The browser only uses the keyframes where that property appears. If `opacity` is set at 0% and 100% and `transform` is set at 0%, 50% and 100%, `opacity` changes smoothly over the whole time while `transform` uses all three points.

## 71: How do you fade an element out and then hide it?

The classic way pairs `opacity` with `visibility`, because `visibility` waits until the end before it hides the element.

```css
.modal {
  opacity: 1;
  visibility: visible;
  transition:
    opacity 200ms,
    visibility 200ms;
}

.modal.is-hidden {
  opacity: 0;
  visibility: hidden;
}
```

Hidden elements can't be clicked or focused, which `opacity: 0` alone doesn't give you.

## 72: Why is opacity: 0 alone not enough to hide an element?

An element with `opacity: 0` is invisible but still there. It can be clicked, focused with the keyboard and read by screen readers. Add `visibility: hidden`, `display: none`, `inert` or at least `pointer-events: none` once it's fully hidden.

## 73: What is perspective in CSS?

Perspective makes 3D transforms look 3D: things farther away look smaller. Without it, `rotateY(45deg)` just looks like the element got narrower. The value is the distance from the viewer to the screen; smaller values give a stronger effect.

```css
.scene {
  perspective: 800px;
}

.card {
  transform: rotateY(30deg);
}
```

## 74: What is the difference between the perspective property and the perspective() function?

The `perspective` property goes on the parent and creates one shared 3D view for all its children, so they look like they're in the same space. The `perspective()` function goes inside an element's own `transform`, and each element gets its own view. Use the property for scenes with several elements.

## 75: What does backface-visibility do?

It decides if you can see the back of an element when it's rotated more than 90 degrees. With `backface-visibility: hidden` the back side is invisible. It's needed for card flips, where the front and back are two elements placed on top of each other.

## 76: What does transform-style: preserve-3d do?

By default, children of a 3D-transformed element are flattened into its plane. `transform-style: preserve-3d` keeps them in real 3D space, so a child can stick out in front of or behind its parent. Some properties, like `overflow: hidden` or `filter`, force flattening again.

## 77: How do you make a card flip animation?

```css
.card {
  perspective: 1000px;
}

.card-inner {
  position: relative;
  transform-style: preserve-3d;
  transition: transform 600ms ease;
}

.card:hover .card-inner {
  transform: rotateY(180deg);
}

.front,
.back {
  position: absolute;
  inset: 0;
  backface-visibility: hidden;
}

.back {
  transform: rotateY(180deg);
}
```

## 78: Is it OK to animate box-shadow?

It works, but it repaints each frame, which can be slow with big blurry shadows or many elements. A common trick is to put the bigger shadow on a pseudo-element and animate only its `opacity`.

```css
.card {
  position: relative;
}

.card::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  box-shadow: 0 12px 30px rgb(0 0 0 / 0.2);
  opacity: 0;
  transition: opacity 200ms;
}

.card:hover::after {
  opacity: 1;
}
```

## 79: Can you animate filter?

Yes. `filter` functions like `blur()`, `brightness()` and `grayscale()` animate smoothly. Simple filters are often handled well by the GPU, but a big `blur()` on a large element can still be heavy. `backdrop-filter` can also be animated and can be even more costly.

## 80: Can you animate clip-path?

Yes, if both values use the same shape function with the same number of points, for example two `circle()` values or two `polygon()` values with the same number of points. It's often used for reveal effects.

```css
.reveal {
  clip-path: circle(0% at 50% 50%);
  transition: clip-path 500ms ease-out;
}

.reveal.is-open {
  clip-path: circle(75% at 50% 50%);
}
```

## 81: How do you make an SVG line "draw itself"?

Set `stroke-dasharray` to the path length and animate `stroke-dashoffset` from that length to 0. Adding `pathLength="1"` to the path makes the numbers easy.

```html
<path d="M10 80 Q 95 10 180 80" pathLength="1" class="line" />
```

```css
.line {
  fill: none;
  stroke: black;
  stroke-dasharray: 1;
  stroke-dashoffset: 1;
  animation: draw 1.5s ease forwards;
}

@keyframes draw {
  to {
    stroke-dashoffset: 0;
  }
}
```

## 82: Can you animate border-radius?

Yes. It's a length or percentage value, so it animates smoothly. It's often used for blob or morph effects. It needs a repaint, but for small elements that's fine.

## 83: Can you animate a CSS custom property?

Not smoothly by default. The browser doesn't know what type an unregistered custom property holds, so it treats it as discrete and flips it. Register it with `@property` and give it a `syntax`, and then it animates like a normal property.

## 84: What is @property?

`@property` registers a custom property with a type, a starting value and whether it inherits. Once the browser knows its type, it can animate it.

```css
@property --angle {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: false;
}

.ring {
  background: conic-gradient(red var(--angle), transparent 0);
  animation: fill 2s linear infinite;
}

@keyframes fill {
  to {
    --angle: 360deg;
  }
}
```

## 85: How can CSS variables make animations easier to configure?

You can use custom properties for duration, delay or distance and change them per element without writing new keyframes.

```css
.item {
  animation: rise var(--duration, 400ms) ease-out var(--delay, 0ms) both;
}

@keyframes rise {
  from {
    translate: 0 var(--distance, 20px);
    opacity: 0;
  }
}
```

Unregistered variables used inside keyframe values are fine; they're read from the element.

## 86: How do you avoid hover animations sticking on touch screens?

On touch devices, `:hover` can stay "on" after a tap. Wrap hover-only effects in a media query that checks if the device really supports hover.

```css
@media (hover: hover) and (pointer: fine) {
  .card:hover {
    transform: translateY(-4px);
  }
}
```

## 87: How do you make a skeleton loading shimmer?

Use a gradient that is wider than the box and move it with `background-position`.

```css
.skeleton {
  background: linear-gradient(90deg, #eee 25%, #f5f5f5 50%, #eee 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s linear infinite;
}

@keyframes shimmer {
  from {
    background-position: 200% 0;
  }
  to {
    background-position: -200% 0;
  }
}
```

## 88: How do you make a "ping" or pulse ring effect?

Scale a copy of the dot up and fade it out at the same time.

```css
.dot {
  position: relative;
}

.dot::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: inherit;
  animation: ping 1.2s ease-out infinite;
}

@keyframes ping {
  to {
    scale: 2.5;
    opacity: 0;
  }
}
```

## 89: How do you make a shake animation for a form error?

```css
@keyframes shake {
  0%,
  100% {
    translate: 0;
  }
  20%,
  60% {
    translate: -6px;
  }
  40%,
  80% {
    translate: 6px;
  }
}

.input.has-error {
  animation: shake 400ms ease-in-out;
}
```

Keep it short and don't rely on it alone; also show a text message, and skip the shake when reduced motion is on.

## 90: How do you animate a link underline?

Draw the underline with a pseudo-element and animate `scale` instead of `width`, so it doesn't trigger layout.

```css
.link {
  position: relative;
  text-decoration: none;
}

.link::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: -2px;
  width: 100%;
  height: 2px;
  background: currentColor;
  scale: 0 1;
  transform-origin: left;
  transition: scale 250ms ease;
}

.link:hover::after {
  scale: 1 1;
}
```

## 91: How should you animate a progress bar?

Animating `width` works but triggers layout on every frame. A smoother way is a full-width bar scaled with `scaleX` from the left edge.

```css
.bar {
  transform-origin: left;
  transform: scaleX(var(--progress, 0));
  transition: transform 300ms ease-out;
}
```

The catch: scaling also stretches rounded corners and any content inside, so this works best for plain bars.

## 92: How do you see and debug animations in browser DevTools?

Chrome and Edge have an Animations panel (More tools > Animations) that records animations, shows them on a timeline, and lets you replay, scrub and slow them down. Firefox shows animations in the Inspector's Animations tab. You can also edit keyframes and easing curves live in the Styles panel.

## 93: How do you slow down animations to check them?

In the Chrome DevTools Animations panel you can set the playback speed to 25% or 10%. You can also temporarily multiply durations with a custom property in your own CSS. Slowing things down helps you spot jumps, wrong easing and flicker that are hard to see at full speed.

## 94: Do you still need -webkit- prefixes for animations?

Not for current browsers. `transition`, `animation`, `@keyframes` and `transform` have worked without prefixes for many years. You may still see `-webkit-` versions in old code or in output from tools set up for very old browsers. They're safe to remove unless you support those old browsers.

## 95: Does an animation run on an element with display: none?

No. When an element gets `display: none`, its running animations are cancelled. When it's shown again, the animations start over from the beginning. This also applies to elements inside it.

## 96: Does an animation run on an element with visibility: hidden or opacity: 0?

Yes. The element is still rendered, just not visible, so the animation keeps running and keeps using resources. If you have many hidden animated elements, pause them or remove the animation.

## 97: How do you hide an element after its animation without JavaScript?

Animate `visibility` (or `display`) together with the other properties, and keep the end state with `forwards`.

```css
@keyframes fade-out {
  from {
    opacity: 1;
    visibility: visible;
  }
  to {
    opacity: 0;
    visibility: hidden;
  }
}

.notice {
  animation: fade-out 300ms ease-in 3s forwards;
}
```

## 98: How do you make a bouncing ball animation?

Use `alternate` so it goes up and down, and an ease that slows at the top.

```css
.ball {
  animation: bounce 600ms cubic-bezier(0.5, 0, 0.5, 1) infinite alternate;
}

@keyframes bounce {
  from {
    translate: 0 0;
  }
  to {
    translate: 0 -120px;
  }
}
```

## 99: How do you rotate an element continuously around its own center?

```css
.logo {
  animation: spin 4s linear infinite;
}

@keyframes spin {
  to {
    rotate: 1turn;
  }
}
```

`transform-origin` is the center by default. For SVG elements it's the top-left corner of the SVG instead, so add `transform-box: fill-box; transform-origin: center;`.

## 100: What angle units can you use in rotations?

`deg` (degrees), `turn` (full turns), `rad` (radians) and `grad` (gradians). `1turn` is the same as `360deg`. `turn` is often the easiest to read for full spins.

## 101: What JavaScript events do CSS animations fire?

- `animationstart`: when the animation starts (after the delay).
- `animationiteration`: at the end of each loop, except the last one.
- `animationend`: when it finishes.
- `animationcancel`: when it stops early, for example because the element got `display: none`.

```js
box.addEventListener("animationend", (event) => {
  console.log(event.animationName, event.elapsedTime);
});
```

## 102: What JavaScript events do CSS transitions fire?

- `transitionrun`: when the transition is created (before the delay).
- `transitionstart`: when it actually starts moving (after the delay).
- `transitionend`: when it finishes.
- `transitioncancel`: when it's stopped before finishing.

Each event has `propertyName` and `elapsedTime`.

## 103: Why does transitionend fire more than once?

It fires once for every property that transitioned. `transition: all` on a hover that changes `transform`, `opacity` and `box-shadow` gives you three events. Check `event.propertyName`, and also check `event.target`, because events from child elements bubble up.

```js
el.addEventListener("transitionend", (e) => {
  if (e.target !== el || e.propertyName !== "opacity") return;
  el.hidden = true;
});
```

## 104: Why doesn't transitionend fire?

Common reasons: the value didn't really change, the duration is 0, the element got `display: none` or was removed before the end, or the transition was replaced by a new one (that fires `transitioncancel`). Code that waits only for `transitionend` can get stuck, so it's safer to also handle `transitioncancel` or use the Web Animations API's `finished` promise.

## 105: How do you start a CSS animation from JavaScript?

The usual way is to add a class that has the animation, and remove it when it's done.

```js
button.addEventListener("click", () => {
  card.classList.add("is-shaking");
});

card.addEventListener("animationend", () => {
  card.classList.remove("is-shaking");
});
```

## 106: How do you restart a CSS animation?

Removing and adding the same class in one go doesn't work, because the browser never sees the "no animation" state. The cleanest way is the Web Animations API:

```js
for (const anim of el.getAnimations()) {
  anim.cancel();
  anim.play();
}
```

An older trick is to remove the class, force a style update by reading something like `el.offsetWidth`, then add the class again.

## 107: What is the Web Animations API?

It's a JavaScript API for creating and controlling animations. It uses the same engine as CSS animations and transitions, so you get the same performance, plus control: you can pause, reverse, seek, change speed and wait for the end with a promise. CSS animations and transitions on a page also show up as objects in this API.

## 108: How do you create an animation with element.animate()?

Pass keyframes and options. It returns an `Animation` object.

```js
const anim = box.animate(
  [
    { transform: "translateY(20px)", opacity: 0 },
    { transform: "translateY(0)", opacity: 1 },
  ],
  { duration: 300, easing: "ease-out", fill: "both" },
);

await anim.finished;
```

Note that durations here are numbers in milliseconds, not strings.

## 109: What is a view transition?

A view transition animates between two states of the page. The browser takes a snapshot of the old state, you update the DOM, and the browser animates from the old snapshot to the new page. By default it's a cross-fade, and you can style it with CSS. It's useful for page changes, list reorders and "this card grows into a detail page" effects.

## 110: How do you start a simple view transition?

Wrap your DOM update in `document.startViewTransition()`.

```js
function showPage(html) {
  if (!document.startViewTransition) {
    main.innerHTML = html;
    return;
  }
  document.startViewTransition(() => {
    main.innerHTML = html;
  });
}
```

Browsers that don't support it just update the DOM without animation.

## 111: What is a scroll-driven animation?

It's a normal CSS animation whose progress follows scrolling instead of time. Scroll down and the animation moves forward, scroll up and it goes back. You use it for reading progress bars, reveal-on-scroll effects and parallax, without JavaScript scroll listeners. Since late 2026 it works in Chrome, Safari and Firefox.

## 112: What is the difference between scroll() and view() timelines?

- `scroll()` tracks how far a scroll container has been scrolled, from top to bottom. Good for progress bars.
- `view()` tracks one element as it moves through the visible area of its scroll container. Good for "fade in when it comes into view".

## 113: How do you write a reading progress bar with CSS only?

```css
.progress {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background: royalblue;
  transform-origin: left;
  animation: grow linear;
  animation-timeline: scroll(root);
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

## 114: Why must animation-timeline come after the animation shorthand?

The `animation` shorthand resets `animation-timeline` to its default (`auto`, time-based). If you write `animation-timeline` first and the shorthand after it, the shorthand wipes it out. Always put `animation-timeline` after `animation`.

## 115: What is a CSS motion path?

It lets an element move along a path you define, with `offset-path`. You then animate `offset-distance` from `0%` to `100%`.

```css
.plane {
  offset-path: path("M 0 100 C 100 0, 200 200, 300 100");
  animation: fly 3s ease-in-out infinite alternate;
}

@keyframes fly {
  to {
    offset-distance: 100%;
  }
}
```

## 116: What does offset-rotate do?

It controls how the element is rotated as it moves along an `offset-path`. The default `auto` turns it to face the direction of the path, like a car following a road. `0deg` keeps it upright, and `auto 90deg` adds an extra turn on top of the path direction.

## 117: How long should UI animations be?

Most UI animations feel right between about 100 ms and 400 ms. Small things like buttons and toggles: 100-200 ms. Bigger things like modals and drawers: 200-400 ms. Long animations make the interface feel slow, especially when people see them many times a day.

## 118: Why use animations in a UI at all?

Good animations explain what happened: where a menu came from, that an item was deleted, that something is loading. They connect two states so the user doesn't lose track. Animation just for decoration often gets in the way, so every animation should have a reason.

## 119: What is a micro-interaction?

A small, short animation that gives feedback for one action: a button that presses in, a heart that pops when you like a post, a checkbox that draws its check mark. They are usually done with transitions or short keyframe animations.

## 120: How do you stagger animations for a list of items?

Give each item a different delay. You can do it with `:nth-child` or with a custom property set in HTML or JS.

```css
.item {
  animation: rise 400ms ease-out both;
  animation-delay: calc(var(--i) * 60ms);
}
```

```html
<li class="item" style="--i: 0">One</li>
<li class="item" style="--i: 1">Two</li>
<li class="item" style="--i: 2">Three</li>
```

## 121: Can you animate ::before and ::after pseudo-elements?

Yes. Pseudo-elements can have transitions and animations just like normal elements. They're often used for decorative effects like underlines, glows and ripples, so you don't need extra HTML.

## 122: How do you make a glowing text effect?

Animate `text-shadow`:

```css
.neon {
  color: #fff;
  animation: glow 1.5s ease-in-out infinite alternate;
}

@keyframes glow {
  from {
    text-shadow: 0 0 4px #0ff;
  }
  to {
    text-shadow:
      0 0 16px #0ff,
      0 0 32px #0ff;
  }
}
```

It repaints each frame, so use it on small pieces of text.

## 123: What does a percentage in translate refer to?

The element's own size. `translateX(100%)` moves the element right by its own width, and `translateY(-50%)` moves it up by half its own height. This is different from `left: 100%`, which uses the containing block's width.

## 124: Why does my centered element jump when I add a hover transform?

If the element is centered with `transform: translate(-50%, -50%)` and the hover sets `transform: scale(1.1)`, the hover value replaces the whole `transform`, so the centering is lost. Either repeat the translate (`transform: translate(-50%, -50%) scale(1.1)`) or use the separate `translate` and `scale` properties so they don't overwrite each other.

## 125: What does skew() do?

It slants the element along the X or Y axis by an angle. `skewX(20deg)` tilts vertical lines to the side. It's used for slanted buttons, "speed" effects and fake 3D.

## 126: What is matrix() in transforms?

`matrix(a, b, c, d, e, f)` describes any 2D transform as six numbers. Every combination of translate, rotate, scale and skew can be written as a matrix. The browser often shows computed transforms as `matrix()`, which is why `getComputedStyle(el).transform` returns a matrix instead of what you wrote.

## 127: What is the compositor?

It's the part of the browser that takes the painted layers of a page and puts them together on screen, usually using the GPU. It can run on its own thread. When an animation only changes `transform` or `opacity` of a layer, the compositor can do it without the main thread, so the animation stays smooth even if JavaScript is busy.

## 128: What is jank?

Jank is visible stutter in an animation or scroll, caused by the browser missing frames. It usually happens because the main thread is busy (long JavaScript tasks) or each frame needs too much work (layout and paint on large areas).

## 129: What is the translateZ(0) hack?

Adding `transform: translateZ(0)` (or `translate3d(0, 0, 0)`) was an old trick to force the browser to give an element its own GPU layer. Today `will-change: transform` does the same thing in a clear way. Neither should be added everywhere: too many layers use a lot of memory and can make things slower.

## 130: What does the animation shorthand reset?

It resets every animation long-hand to its initial value, including `animation-play-state`, `animation-composition` and `animation-timeline`, even if you didn't write them. So `animation: spin 1s` after `animation-play-state: paused` makes it run again. Put long-hands after the shorthand.

## 131: What are the rules for naming keyframes?

A keyframes name is a CSS identifier, like `fade-in` or `slideUp`. Names are case-sensitive. You can't use `none` or other CSS-wide keywords like `initial` or `inherit` as a plain name. Pick descriptive, unique names so they don't clash with other stylesheets.

## 132: What happens if the same keyframe percentage appears twice in one @keyframes?

The declarations are combined, and for the same property the later one wins. So two `50%` blocks act like one block. It's still confusing, so keep one block per percentage.

## 133: Can keyframe percentages be lower than 0% or higher than 100%?

No. Selectors like `120%` or `-10%` are invalid, and that keyframe block is ignored. Use `cubic-bezier()` or `linear()` if you want the motion to overshoot.

## 134: How do you make a smooth focus ring animation?

```css
.button {
  outline: 2px solid transparent;
  outline-offset: 6px;
  transition:
    outline-offset 150ms ease,
    outline-color 150ms ease;
}

.button:focus-visible {
  outline-color: royalblue;
  outline-offset: 2px;
}
```

Use `:focus-visible` so the ring shows for keyboard users without flashing on every mouse click.

## 135: How do you animate a child when the parent is hovered?

Use a descendant selector with the hover on the parent:

```css
.card .arrow {
  transition: translate 200ms ease;
}

.card:hover .arrow {
  translate: 4px 0;
}
```

## 136: Can each property in a transition have its own timing function?

Yes. In the shorthand each comma-separated item has its own easing, and in the long-hand you give a list.

```css
.toast {
  transition-property: opacity, transform;
  transition-duration: 200ms, 400ms;
  transition-timing-function: linear, cubic-bezier(0.2, 0.8, 0.2, 1);
}
```

## 137: What does interpolation mean in animations?

Interpolation is how the browser finds the values in between the start and the end. For a number it's simple: halfway between 0 and 100 is 50. For colors, transforms and shadows there are rules for each type. If two values can't be interpolated, the property switches discretely instead.

## 138: When should you use CSS animation instead of a GIF or video?

Use CSS for UI motion like buttons, loaders, transitions and anything that should match your styles, colors and screen size. CSS is lighter, stays sharp at any size and can react to state. Use video for complex scenes or real footage. Replace animated GIFs with video or CSS when you can; GIFs are big and look bad.

## 139: When would you use a JavaScript animation library instead of CSS?

When you need things CSS can't do easily: physics-based springs that react to velocity, complex timelines with many steps, animating values that aren't CSS (like canvas or numbers in text), drag gestures, or layout animations in a framework. Libraries like GSAP and Motion help here. For simple hovers, fades and loaders, plain CSS is enough.

## 140: Do CSS animations work in HTML emails?

Only in some email clients. Apple Mail supports a lot of CSS, including animations, but many others (like Outlook on Windows) strip or ignore them. Treat any animation in email as a bonus, and make sure the email looks right without it.

## 141: How do you make an infinite scrolling marquee with CSS?

Put the content twice in a row inside a track and move the track by half its width. When it loops, the second copy is exactly where the first started, so there is no jump.

```css
.marquee {
  overflow: hidden;
}

.track {
  display: flex;
  width: max-content;
  animation: scroll 20s linear infinite;
}

@keyframes scroll {
  to {
    translate: -50% 0;
  }
}
```

Mark the duplicate copy with `aria-hidden="true"`.

## 142: How do you make a loading dots animation?

```css
.dots span {
  display: inline-block;
  animation: blink 1.4s ease-in-out infinite both;
}

.dots span:nth-child(2) {
  animation-delay: 0.2s;
}
.dots span:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes blink {
  0%,
  80%,
  100% {
    opacity: 0.2;
  }
  40% {
    opacity: 1;
  }
}
```

## 143: How do you make a hamburger icon turn into an X?

Animate the three bars with `rotate`, `translate` and `opacity` when a class or `aria-expanded` changes.

```css
.bar {
  transition:
    rotate 200ms ease,
    translate 200ms ease,
    opacity 200ms ease;
}

[aria-expanded="true"] .bar:nth-child(1) {
  translate: 0 8px;
  rotate: 45deg;
}
[aria-expanded="true"] .bar:nth-child(2) {
  opacity: 0;
}
[aria-expanded="true"] .bar:nth-child(3) {
  translate: 0 -8px;
  rotate: -45deg;
}
```

Using `aria-expanded` as the hook keeps the visual state and the accessible state in sync.

## 144: How do you animate a button press?

A small scale down on `:active` makes a button feel physical:

```css
.button {
  transition: scale 100ms ease;
}

.button:active {
  scale: 0.96;
}
```

## 145: How do you create a toggle switch animation?

Move the knob with `translate` when the checkbox is checked.

```css
.switch input:checked + .track .knob {
  translate: 20px 0;
}

.knob {
  transition: translate 200ms ease;
}

.track {
  transition: background-color 200ms ease;
}
```

Keep a real `<input type="checkbox">` (or `role="switch"`) so it works with keyboard and screen readers.

## 146: What does the cascade do with animation styles?

Styles from running CSS animations are in their own cascade level that beats normal author styles, even ones with higher specificity. Only `!important` declarations beat them. Transition styles sit even higher, above `!important` ones. This is why an animated property ignores your normal rule while the animation runs.

## 147: Can you set animation styles inline with the style attribute?

Yes. You can set `animation` or `transition` in the `style` attribute or from JavaScript (`el.style.animation = "..."`). But `@keyframes` must be in a stylesheet. For keyframes defined in JavaScript, use `element.animate()`.

## 148: What does "animating from current state" mean?

The animation starts from where the element is right now, not from a fixed value. Transitions do this by nature: if you stop hovering halfway, the element goes back from the middle. In keyframes you get it by leaving out the `from` keyframe.

## 149: What happens when a transition is interrupted halfway?

A new transition starts from the current value to the new target. If it is going back to the original value, browsers shorten the reverse transition based on how far the first one got, so a half-finished hover doesn't take the full time to go back.

## 150: What is the difference between animation-fill-mode: forwards and setting the final style yourself?

`forwards` keeps the last keyframe styles applied as an animation, which beats normal styles. That means you can't easily change those properties later with normal CSS, and the animation keeps existing. Setting the final values as normal styles (and animating from somewhere else to them) is cleaner and easier to debug.

# Moderate Questions (151-300)

## 151: What does transition-behavior: allow-discrete do?

Normally transitions skip discrete properties like `display` and `content-visibility`; they just flip at once. With `transition-behavior: allow-discrete` they take part in the transition and flip at a point that keeps the element visible: when hiding, `display: none` is applied at the end; when showing, `display: block` is applied at the start.

```css
.panel {
  transition:
    opacity 250ms,
    display 250ms allow-discrete;
}
```

## 152: How do you animate a dialog in and out with CSS only?

Combine `@starting-style` for the entry, `allow-discrete` for `display` and `overlay` on the exit, and style the open state with `[open]`.

```css
dialog {
  opacity: 0;
  translate: 0 20px;
  transition:
    opacity 250ms,
    translate 250ms,
    display 250ms allow-discrete,
    overlay 250ms allow-discrete;
}

dialog[open] {
  opacity: 1;
  translate: 0 0;
}

@starting-style {
  dialog[open] {
    opacity: 0;
    translate: 0 20px;
  }
}
```

## 153: Why do you need to transition overlay when animating a dialog or popover out?

Modal dialogs and popovers live in the top layer while they're open. When they close, the browser removes them from the top layer right away, so the exit animation would play behind other content or get cut off. Transitioning `overlay` with `allow-discrete` keeps the element in the top layer until the animation is done.

## 154: How do you animate a popover?

Same idea as a dialog, but the open state is `:popover-open`.

```css
[popover] {
  opacity: 0;
  scale: 0.95;
  transition:
    opacity 150ms,
    scale 150ms,
    display 150ms allow-discrete,
    overlay 150ms allow-discrete;
}

[popover]:popover-open {
  opacity: 1;
  scale: 1;
}

@starting-style {
  [popover]:popover-open {
    opacity: 0;
    scale: 0.95;
  }
}
```

## 155: How do you animate the backdrop of a modal dialog?

`::backdrop` can be transitioned too, and it needs its own `@starting-style` and discrete transitions.

```css
dialog::backdrop {
  background: rgb(0 0 0 / 0);
  transition:
    background 250ms,
    display 250ms allow-discrete,
    overlay 250ms allow-discrete;
}

dialog[open]::backdrop {
  background: rgb(0 0 0 / 0.5);
}

@starting-style {
  dialog[open]::backdrop {
    background: rgb(0 0 0 / 0);
  }
}
```

## 156: Can you nest @starting-style inside a rule?

Yes, with CSS nesting you can write it inside the selector, and it applies to that same selector.

```css
.toast {
  opacity: 1;
  transition: opacity 300ms;

  @starting-style {
    opacity: 0;
  }
}
```

## 157: What are common mistakes with @starting-style?

- Putting it before the normal rule with the same specificity, so the normal rule wins. Put it after, or nest it.
- Expecting it to work with keyframe animations; it only affects transitions.
- Forgetting `transition-behavior: allow-discrete` on `display` when showing from `display: none`.
- Expecting it on every style change. It only applies the first time the element is rendered (or when it goes from `display: none` to shown).

## 158: How do interpolate-size and calc-size() work?

`interpolate-size: allow-keywords` lets the browser animate between a length and a size keyword like `auto`, `min-content` or `fit-content`. You usually set it once on `:root`. `calc-size()` does the same for one value, and also lets you do math on a keyword size.

```css
:root {
  interpolate-size: allow-keywords;
}

.panel {
  height: 0;
  overflow: hidden;
  transition: height 300ms ease;
}

.panel.open {
  height: auto;
}
```

Right now this works in Chromium browsers. In others the panel still opens, just without the animation.

## 159: How does the grid 0fr to 1fr trick animate height?

Grid track sizes can be animated. Put the content in a grid with one row and animate that row from `0fr` to `1fr`. The child needs `min-height: 0` (or `overflow: hidden`) so it can shrink.

```css
.collapse {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows 300ms ease;
}

.collapse.open {
  grid-template-rows: 1fr;
}

.collapse > .inner {
  overflow: hidden;
}
```

It works in all current browsers.

## 160: What are the problems with the max-height trick?

You animate `max-height` from 0 to a big number like `1000px`. But the timing is based on that big number, not the real height, so a short panel opens almost instantly and closing has a delay before anything moves. If the content is taller than your number, it gets cut off. Prefer the grid trick or `interpolate-size`.

## 161: How do you animate a details element opening?

In browsers that support it, combine the `::details-content` pseudo-element with `interpolate-size`:

```css
:root {
  interpolate-size: allow-keywords;
}

details::details-content {
  block-size: 0;
  overflow: hidden;
  transition:
    block-size 300ms ease,
    content-visibility 300ms allow-discrete;
}

details[open]::details-content {
  block-size: auto;
}
```

Support is still mostly Chromium, so treat it as an enhancement. Without it the details element still opens and closes normally.

## 162: How do you animate removing an item from a list?

First animate the item out (fade, slide), then collapse the space it took, then remove it from the DOM. In JavaScript with the Web Animations API:

```js
async function removeItem(el) {
  await el.animate([{ opacity: 1 }, { opacity: 0 }], { duration: 150 })
    .finished;
  const h = el.offsetHeight;
  await el.animate([{ height: `${h}px` }, { height: "0px" }], {
    duration: 200,
    easing: "ease-out",
  }).finished;
  el.remove();
}
```

View transitions can also do this for you with less code.

## 163: What is the FLIP technique?

FLIP stands for First, Last, Invert, Play. It's a way to animate layout changes with only `transform`:

1. First: measure where the element is now.
2. Last: make the layout change and measure the new position.
3. Invert: apply a transform that moves it back to the old position.
4. Play: animate the transform back to none.

It looks like the element moved through the layout, but the browser only animates `transform`, which is cheap.

## 164: How do you implement FLIP with the Web Animations API?

```js
function flip(el, changeLayout) {
  const first = el.getBoundingClientRect();
  changeLayout();
  const last = el.getBoundingClientRect();

  const dx = first.left - last.left;
  const dy = first.top - last.top;
  const sx = first.width / last.width;
  const sy = first.height / last.height;

  el.animate(
    [
      {
        transformOrigin: "top left",
        transform: `translate(${dx}px, ${dy}px) scale(${sx}, ${sy})`,
      },
      { transformOrigin: "top left", transform: "none" },
    ],
    { duration: 300, easing: "ease-out" },
  );
}
```

## 165: What does element.getAnimations() return?

It returns all running or paused animations on that element: CSS animations, CSS transitions and ones created with `element.animate()`. Pass `{ subtree: true }` to include the element's descendants. You can then pause them, check their state or wait for them to finish.

```js
await Promise.all(el.getAnimations({ subtree: true }).map((a) => a.finished));
```

## 166: What does document.getAnimations() do?

It returns every active animation in the document. It's handy for debugging, for a "pause everything" button, or for making sure all animations are done before taking a screenshot in a test.

```js
document.getAnimations().forEach((a) => a.pause());
```

## 167: What methods does an Animation object have?

- `play()`: start or resume.
- `pause()`: pause where it is.
- `reverse()`: play backwards from where it is.
- `finish()`: jump to the end.
- `cancel()`: stop and remove all its effects.
- `updatePlaybackRate()`: change speed smoothly.
- `commitStyles()`: write its current values into the element's inline style.
- `persist()`: keep a filling animation from being removed automatically.

## 168: What is the difference between playbackRate and updatePlaybackRate()?

Both change the speed (2 is twice as fast, -1 plays backwards). Setting `anim.playbackRate` directly takes effect immediately and can cause a small jump if the animation runs on the compositor. `updatePlaybackRate(rate)` waits to sync with the compositor first, so the change is smooth. Use `updatePlaybackRate()` for running animations.

## 169: How do you jump to a specific point in an animation?

Set `currentTime` in milliseconds. This is often used with a paused animation to control it with a slider or scroll position.

```js
const anim = box.animate(keyframes, { duration: 1000, fill: "both" });
anim.pause();
slider.addEventListener("input", () => {
  anim.currentTime = slider.valueAsNumber * 10; // 0-100 -> 0-1000ms
});
```

## 170: What are the ready and finished promises on an Animation?

`anim.ready` resolves when the animation is ready to play (after any pending play or pause is processed). `anim.finished` resolves when it reaches the end. If the animation is cancelled, `finished` rejects with an `AbortError`, so catch it if cancelling is normal in your code.

```js
try {
  await anim.finished;
  el.remove();
} catch {
  // cancelled, do nothing
}
```

## 171: Why is fill: "forwards" in the Web Animations API not ideal, and what is commitStyles()?

A `forwards` fill keeps the animation alive forever to hold the end values. Many of these pile up and use memory, and their values beat normal styles, which makes later changes confusing. A cleaner pattern: when it finishes, write the end values into the element with `commitStyles()` and then `cancel()` the animation.

```js
const anim = el.animate(
  { transform: "translateX(200px)" },
  { duration: 300, fill: "forwards" },
);
await anim.finished;
anim.commitStyles();
anim.cancel();
```

## 172: What does the composite option do in element.animate()?

It says how this animation's values combine with what's under it. `replace` (default) overwrites. `add` adds on top; for transforms it appends the transform functions. `accumulate` combines the values, for example adding scale factors together. It matches the CSS `animation-composition` property.

```js
el.animate(
  { transform: "translateY(-10px)" },
  { duration: 300, composite: "add" },
);
```

## 173: What are KeyframeEffect and the Animation constructor for?

`element.animate()` is a shortcut. Under it there is a `KeyframeEffect` (what to animate: target, keyframes, timing) and an `Animation` (playback state and timeline). Creating them yourself lets you build an animation without playing it, reuse an effect, or attach it to a different timeline, like a `ScrollTimeline`.

```js
const effect = new KeyframeEffect(el, [{ opacity: 0 }, { opacity: 1 }], {
  duration: 500,
});
const anim = new Animation(effect, document.timeline);
anim.play();
```

## 174: What keyframe formats does element.animate() accept?

An array of keyframe objects, or one object with arrays of values for each property.

```js
// array format, with optional offset and easing per keyframe
el.animate(
  [
    { opacity: 0, offset: 0 },
    { opacity: 0.8, offset: 0.7, easing: "ease-in" },
    { opacity: 1, offset: 1 },
  ],
  500,
);

// object format
el.animate({ opacity: [0, 1], transform: ["scale(0.9)", "scale(1)"] }, 500);
```

Property names are camelCase, like `backgroundColor`.

## 175: What timing options can you pass to element.animate()?

`duration`, `delay`, `endDelay`, `iterations` (use `Infinity` for forever), `direction`, `easing`, `fill`, `iterationStart`, `composite` and `id`. `endDelay` adds time after the animation ends, which helps when you line up several animations one after another.

## 176: How do you control a CSS animation from JavaScript without changing classes?

CSS animations show up as `CSSAnimation` objects in `getAnimations()`. You can find the one you want by name and control it directly.

```js
const anim = el.getAnimations().find((a) => a.animationName === "spin");
anim?.pause();
anim.playbackRate = 0.5;
```

Some changes, like pausing, can be overridden later if the CSS `animation-play-state` changes.

## 177: What is a CSSTransition object?

Each running CSS transition is a `CSSTransition` in `getAnimations()`, with a `transitionProperty` field. You can wait for it, pause it or check its progress. Once it finishes, it's gone from the list.

```js
el.classList.add("open");
const t = el.getAnimations().find((a) => a.transitionProperty === "height");
await t?.finished;
```

## 178: How do you wait for all animations on an element before removing it?

```js
async function animateOut(el) {
  el.classList.add("leaving");
  await Promise.allSettled(
    el.getAnimations({ subtree: true }).map((a) => a.finished),
  );
  el.remove();
}
```

Using `allSettled` means a cancelled animation doesn't stop the removal.

## 179: How do you check prefers-reduced-motion in JavaScript?

Use `matchMedia`, and listen for changes because the user can change the setting while the page is open.

```js
const query = window.matchMedia("(prefers-reduced-motion: reduce)");

function update() {
  document.documentElement.classList.toggle("reduce-motion", query.matches);
}

update();
query.addEventListener("change", update);
```

Also check it before calling `element.animate()` or starting a JS animation library.

## 180: What is the "global reduced motion" reset and what are its risks?

A common snippet sets very short durations on everything when reduced motion is on:

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

It's a good safety net, but it can break things: loaders end up stuck in one frame, and code that waits for long animations may now run in a different order. It also removes harmless fades. Prefer designing a reduced version for each important animation and use the reset as a backup.

## 181: What is the "no-preference first" approach to motion?

Instead of adding motion and then turning it off for reduced motion, you only add motion when the user has no preference:

```css
@media (prefers-reduced-motion: no-preference) {
  .hero {
    animation: slide-in 600ms ease-out;
  }
}
```

The base styles have no motion, so if the media query isn't supported or the user asked for less motion, they get the calm version by default.

## 182: What does WCAG say about moving content?

Success criterion 2.2.2 (Pause, Stop, Hide) says that content that moves, blinks or scrolls automatically for more than 5 seconds, alongside other content, needs a way to pause, stop or hide it. Carousels, marquees and looping background animations are common failures. 2.3.1 says nothing should flash more than three times in one second.

## 183: What is WCAG 2.3.3 Animation from Interactions?

It's a AAA criterion: motion triggered by user interaction (like parallax on scroll or big zooms on click) should be possible to turn off, unless the motion is essential. Respecting `prefers-reduced-motion` is the usual way to meet it.

## 184: How do you add a pause button for animations?

Toggle a class or attribute on a container that pauses everything inside it.

```css
[data-motion="paused"] *,
[data-motion="paused"] *::before,
[data-motion="paused"] *::after {
  animation-play-state: paused !important;
}
```

```js
pauseButton.addEventListener("click", () => {
  const paused = root.dataset.motion === "paused";
  root.dataset.motion = paused ? "running" : "paused";
  pauseButton.setAttribute("aria-pressed", String(!paused));
});
```

For Web Animations API animations, call `pause()` on them too.

## 185: How do animations affect screen reader users?

Screen readers don't see the motion, only the DOM. Problems come when content is visually hidden with `opacity: 0` but still read out, or when content appears with an animation but nothing announces it. Hide finished-off content properly (`display: none`, `hidden`, `inert`) and use `aria-live` regions or focus management for content that appears.

## 186: What pseudo-elements does a view transition create?

While it runs, the browser builds this tree on top of the page:

```
::view-transition
└─ ::view-transition-group(name)
   └─ ::view-transition-image-pair(name)
      ├─ ::view-transition-old(name)
      └─ ::view-transition-new(name)
```

There is one group per named element, plus `root` for the whole page. The group animates size and position, and the old and new images cross-fade inside it.

## 187: What does view-transition-name do?

It marks an element as its own part of a view transition. If an element with the name `hero` exists before and after the change, the browser animates it from the old position and size to the new one, instead of just fading it with the rest of the page.

```css
.product-image {
  view-transition-name: product-photo;
}
```

## 188: How do you change the default cross-fade of a view transition?

Style the pseudo-elements. For example, slide the whole page instead of fading:

```css
::view-transition-old(root) {
  animation: 300ms ease-in both slide-out;
}

::view-transition-new(root) {
  animation: 300ms ease-out both slide-in;
}

@keyframes slide-out {
  to {
    translate: -100% 0;
  }
}

@keyframes slide-in {
  from {
    translate: 100% 0;
  }
}
```

Change only the duration with `::view-transition-group(*) { animation-duration: 400ms; }`.

## 189: Why must view-transition-name values be unique?

Each name has to belong to exactly one element at a time on the page, because the browser pairs the old and new element by name. If two visible elements share a name, the transition is skipped and the browser logs an error. For lists, give each item its own name, for example with an inline style `view-transition-name: item-42`.

## 190: What is view-transition-class?

It lets you style many named elements with one rule. Each element still needs a unique `view-transition-name`, but they can share a class.

```css
.card {
  view-transition-class: card;
}

::view-transition-group(.card) {
  animation-duration: 400ms;
}
```

## 191: What do view-transition-name: match-element and auto do?

They make the browser create unique names for you, so you don't need one per item. `match-element` pairs elements by their identity: the same DOM element before and after the change. `auto` uses the element's `id` if it has one and falls back to element identity. They're useful for lists that reorder. They only work for same-document transitions.

## 192: How do you turn on view transitions between pages of a multi-page site?

Add this to the CSS of both the old and new page (same origin):

```css
@view-transition {
  navigation: auto;
}
```

Normal link navigations then cross-fade, and you can use `view-transition-name` on both pages to animate shared elements. Chromium and Safari support this; check current support for Firefox.

## 193: What are the pageswap and pagereveal events?

They're for customizing cross-document view transitions. `pageswap` fires on the old page right before it's replaced; `pagereveal` fires on the new page before its first render. Both give you `event.viewTransition` (or `null`), so you can set names, add types or skip the transition based on where the user is going.

```js
window.addEventListener("pagereveal", (e) => {
  if (!e.viewTransition) return;
  e.viewTransition.types.add("forward");
});
```

## 194: What are view transition types?

Types are labels for a transition, like `forward`, `back` or `reload`. You set them when starting it, and match them in CSS with `:active-view-transition-type()`. This lets you use different animations for different navigations.

```js
document.startViewTransition({
  update: () => renderNextPage(),
  types: ["forward"],
});
```

```css
html:active-view-transition-type(forward) {
  &::view-transition-new(root) {
    animation-name: slide-from-right;
  }
}
```

## 195: What promises does the ViewTransition object give you?

- `updateCallbackDone`: your DOM update function finished.
- `ready`: the pseudo-elements exist and the animation is about to start. Good for running custom animations with `element.animate()` on the pseudo-elements.
- `finished`: the animation ended and the new state is live.

## 196: What does skipTransition() do?

It skips the animation part of a view transition. The DOM update still happens and the promises still settle. You'd use it if, for example, the user navigates again before the transition finishes.

## 197: How do you respect reduced motion with view transitions?

Turn off or simplify the animations of the pseudo-elements:

```css
@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(*),
  ::view-transition-old(*),
  ::view-transition-new(*) {
    animation: none !important;
  }
}
```

Or keep the default cross-fade (which isn't motion) and only remove slides and zooms.

## 198: How do view transitions fit into single-page app routers?

The router has to call `document.startViewTransition()` around the DOM update for a route change, and wait until the new view is rendered. Many frameworks and routers now have a built-in option for this, so you don't wire it by hand. The hard part is usually async data: the update callback must not resolve until the new content is in the DOM, and the page is frozen while it waits, so keep it fast.

## 199: What does animation-range do in scroll-driven animations?

It sets which part of the timeline the animation runs in. Before the start of the range the animation hasn't started; after the end it's done.

```css
.card {
  animation: reveal linear both;
  animation-timeline: view();
  animation-range: entry 0% cover 40%;
}
```

Here it starts as the card begins entering the view and is complete when it has covered 40% of the visible area.

## 200: What are the animation-range names for view timelines?

- `cover`: from the first pixel entering to the last pixel leaving.
- `contain`: while the element is fully inside the view (or fully covers it).
- `entry`: while it's entering.
- `exit`: while it's leaving.
- `entry-crossing` and `exit-crossing`: while it crosses the start or end edge.

Each can take a percentage, like `entry 50%`.

## 201: How do you use a named scroll timeline?

Give the scroll container a name with `scroll-timeline-name`, then use that name in `animation-timeline`. This lets an element follow a scroller that isn't its nearest one.

```css
.gallery {
  overflow-x: auto;
  scroll-timeline-name: --gallery;
  scroll-timeline-axis: inline;
}

.gallery .indicator {
  animation: fill-bar linear both;
  animation-timeline: --gallery;
}
```

Timeline names must start with two dashes.

## 202: What is timeline-scope for?

A named timeline is normally only visible to the scroller's own descendants. `timeline-scope` on a common ancestor makes the name visible to everything inside that ancestor, so a sibling or a far-away element can use it.

```css
.layout {
  timeline-scope: --article;
}

.article {
  overflow-y: auto;
  scroll-timeline-name: --article;
}

.sidebar .progress {
  animation: grow linear both;
  animation-timeline: --article;
}
```

## 203: What does animation-duration mean for a scroll-driven animation?

Time doesn't apply, because the progress comes from scrolling. The animation is stretched over the timeline's range. Set the duration to `auto` (the default) or leave it out of the shorthand. If you set a time like `1s`, Chromium and Safari still stretch it over the whole range, but writing `auto` makes the intent clear.

## 204: Why do scroll-driven animations often use fill-mode both?

Outside the active range the animation has no effect by default, so the element jumps back to its normal styles before the start or after the end. With `both`, it keeps the first keyframe before the range and the last keyframe after it, which is what you usually want for reveal effects.

## 205: How do you make elements fade in as they scroll into view?

```css
@keyframes reveal {
  from {
    opacity: 0;
    translate: 0 40px;
  }
  to {
    opacity: 1;
    translate: 0 0;
  }
}

.reveal {
  animation: reveal linear both;
  animation-timeline: view();
  animation-range: entry 10% cover 30%;
}
```

No JavaScript and no IntersectionObserver needed.

## 206: How do you make a parallax effect with scroll-driven animations?

Move a background element slower or faster than the scroll by animating `translate` against a view timeline.

```css
.hero-bg {
  animation: parallax linear both;
  animation-timeline: view();
}

@keyframes parallax {
  from {
    translate: 0 -20%;
  }
  to {
    translate: 0 20%;
  }
}
```

Respect `prefers-reduced-motion`; parallax is a common trigger for motion sickness.

## 207: How do you feature-detect scroll-driven animations?

Use `@supports` in CSS, or `CSS.supports()` in JavaScript.

```css
@supports (animation-timeline: scroll()) {
  .progress {
    animation: grow linear;
    animation-timeline: scroll(root);
  }
}
```

```js
const ok = CSS.supports("animation-timeline: scroll()");
```

## 208: What fallback can you use where scroll-driven animations don't work?

For reveal effects, use IntersectionObserver to add a class when an element enters the viewport, and run a normal transition. For progress bars, update a custom property from a passive scroll listener with `requestAnimationFrame`. Or just show the final state without animation, which is fine for most decorative effects.

## 209: What axis options do scroll timelines have?

`block` (default), `inline`, `x` and `y`. `block` and `inline` follow the writing mode, so in a vertical writing mode `block` is horizontal. Use them with `scroll()`, `view()` or the `scroll-timeline-axis` and `view-timeline-axis` properties.

```css
.indicator {
  animation-timeline: scroll(nearest inline);
}
```

## 210: What arguments does the scroll() function take?

A scroller and an axis, in any order. The scroller is `nearest` (default, the closest scrolling ancestor), `root` (the document) or `self` (the element itself). Example: `scroll(root block)`.

## 211: What is view-timeline-inset for?

It moves the edges of the area used for a view timeline. A positive inset makes the area smaller, so the animation starts later and ends earlier. It's useful when a fixed header covers part of the scroller. You can also pass the inset to `view()`: `view(block 80px 0px)`.

## 212: How do you shrink a sticky header on scroll with CSS only?

Use a scroll timeline on the root and limit it to the first part of the scroll.

```css
.header {
  position: sticky;
  top: 0;
  animation: shrink linear both;
  animation-timeline: scroll(root);
  animation-range: 0px 200px;
}

@keyframes shrink {
  to {
    padding-block: 4px;
    box-shadow: 0 2px 8px rgb(0 0 0 / 0.15);
  }
}
```

Animating `padding` causes layout, so on big pages consider `scale` on an inner element instead.

## 213: How do you use @supports with other new animation features?

Check the exact property and value you depend on, and put the enhanced version inside.

```css
@supports (transition-behavior: allow-discrete) {
  /* exit animations for display: none */
}

@supports (interpolate-size: allow-keywords) {
  :root {
    interpolate-size: allow-keywords;
  }
}
```

For at-rules like `@starting-style` there's no simple `@supports` test, but browsers that don't know it just ignore the block, which already is a fallback.

## 214: How do you make a rotating gradient border?

Register an angle with `@property`, use it in a `conic-gradient`, and animate the angle.

```css
@property --a {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: false;
}

.glow-border {
  border: 3px solid transparent;
  background:
    linear-gradient(#fff, #fff) padding-box,
    conic-gradient(from var(--a), red, orange, violet, red) border-box;
  animation: rotate 3s linear infinite;
}

@keyframes rotate {
  to {
    --a: 360deg;
  }
}
```

## 215: How do you smoothly animate gradient colors?

Register the colors as custom properties with `syntax: "<color>"`, use them in the gradient, and transition or animate the properties.

```css
@property --c1 {
  syntax: "<color>";
  initial-value: #ff7a18;
  inherits: false;
}

.banner {
  background: linear-gradient(90deg, var(--c1), #af002d);
  transition: --c1 500ms;
}

.banner:hover {
  --c1: #3a7bd5;
}
```

## 216: How do you animate a number counting up with CSS only?

Register an integer property, animate it, and show it with a counter.

```css
@property --num {
  syntax: "<integer>";
  initial-value: 0;
  inherits: false;
}

.count {
  counter-reset: num var(--num);
  animation: count 2s ease-out forwards;
}

.count::after {
  content: counter(num);
}

@keyframes count {
  to {
    --num: 100;
  }
}
```

Screen readers may not read pseudo-element content reliably, so put the final number in real text too, for example in an `aria-label`.

## 217: Why set inherits: false on animated custom properties?

If an animated property inherits, every descendant has to update its computed styles each frame. With `inherits: false`, only the element itself changes. For a property that changes 60+ times a second on an element with many children, this saves a lot of work.

## 218: How do you register a custom property from JavaScript?

```js
CSS.registerProperty({
  name: "--progress",
  syntax: "<percentage>",
  inherits: false,
  initialValue: "0%",
});
```

It does the same as `@property`. Registering the same name twice throws an error, so wrap it in a check or `try` when the code can run more than once.

## 219: What is the difference between animation-composition add and accumulate?

Both combine the animation with the underlying value instead of replacing it. The difference shows with transforms and some other types:

- `add` appends: base `translateX(50px)` plus animated `translateX(10px)` becomes `translateX(50px) translateX(10px)`.
- `accumulate` merges matching functions: the same example becomes `translateX(60px)`.

For `blur(2px)` plus `blur(3px)`, `add` gives two blurs and `accumulate` gives `blur(5px)`. For simple numbers and lengths they give the same result.

## 220: How do you combine a hover transform with a running keyframe animation on the same element?

If both set `transform`, the animation wins while it runs, and the hover does nothing. Split them: let the animation use one property (`rotate`) and the hover another (`scale`). Or set `animation-composition: add` so the animation adds to the base value instead of replacing it.

```css
.icon {
  animation: wobble 2s ease-in-out infinite;
  transition: scale 200ms;
}

.icon:hover {
  scale: 1.2;
}

@keyframes wobble {
  50% {
    rotate: 8deg;
  }
}
```

## 221: How can one transitioned custom property drive several values?

Transition a registered number, then compute other values from it with `calc()`.

```css
@property --t {
  syntax: "<number>";
  initial-value: 0;
  inherits: true;
}

.drawer {
  transition: --t 300ms ease-out;
}

.drawer.open {
  --t: 1;
}

.drawer .panel {
  translate: calc((1 - var(--t)) * -100%) 0;
}

.drawer .shade {
  opacity: calc(var(--t) * 0.5);
}
```

Here `inherits: true` is needed because the children read it.

## 222: How can sibling-index() help with staggered animations?

`sibling-index()` returns the element's position among its siblings (starting at 1), so you can compute delays in CSS without setting `--i` on each item.

```css
.item {
  animation: rise 400ms ease-out both;
  animation-delay: calc((sibling-index() - 1) * 60ms);
}
```

It's new: Chromium and Firefox support it, but check current support before relying on it. Keep the `--i` approach as a fallback.

## 223: Should enter and exit animations have the same duration?

Usually exits are shorter. When something appears, the user needs a moment to see where it came from. When it's dismissed, the user already decided to close it, so a quick exit (often about 2/3 of the entry time) feels more responsive. Exits often use `ease-in` and entries `ease-out`.

## 224: How do you play several animations one after another on the same element?

Give each one a delay equal to the total time of the ones before it, and use `both` fill so states don't jump between them.

```css
.logo {
  animation:
    fade-in 300ms ease-out both,
    grow 400ms ease-out 300ms both,
    settle 200ms ease-in 700ms both;
}
```

For long or complex sequences, the Web Animations API with `await anim.finished` is easier to maintain.

## 225: How does fill-mode work together with alternate and iteration count?

The final state depends on which direction the last iteration ran. With `animation-direction: alternate` and `animation-iteration-count: 2`, the second run goes backward, so `forwards` keeps the `from` keyframe, not `to`. With an odd count it ends on `to`. Keep this in mind when the end state looks "wrong".

## 226: How do you make a ticking clock hand with CSS?

Use `steps(60)` over 60 seconds so it jumps once per second instead of moving smoothly.

```css
.second-hand {
  transform-origin: bottom center;
  animation: tick 60s steps(60, end) infinite;
}

@keyframes tick {
  to {
    rotate: 360deg;
  }
}
```

## 227: Why use tabular-nums for animated numbers?

In most fonts, digits have different widths, so changing numbers make the text wiggle sideways. `font-variant-numeric: tabular-nums` makes every digit the same width, so counters, timers and prices stay still while they change.

## 228: How do you make a loading spinner accessible?

The spinner itself is decoration, so give screen readers a text alternative and mark the area as busy.

```html
<div role="status">
  <span class="spinner" aria-hidden="true"></span>
  <span class="visually-hidden">Loading results…</span>
</div>
```

`role="status"` makes the text announced politely. Set `aria-busy="true"` on the region that is being updated, and keep a slower or non-moving version for reduced motion.

## 229: What happens to CSS animations in background tabs?

Browsers stop rendering frames for tabs that aren't visible, so animations don't use CPU or GPU there. Their timelines still move with time, so when you come back, a finite animation will usually be finished and an infinite one will be at the right point. Don't use `animationend` timing for important logic that must run at an exact moment.

## 230: Do infinite animations off-screen cost anything?

In a visible tab, browsers may skip some work for off-screen elements, but not always, and the main thread may still do style updates. Many looping animations below the fold can use battery. Pause them when they're not visible, with IntersectionObserver or `content-visibility: auto` on their section.

```js
const io = new IntersectionObserver((entries) => {
  for (const e of entries) {
    e.target.style.animationPlayState = e.isIntersecting ? "running" : "paused";
  }
});
document.querySelectorAll(".looping").forEach((el) => io.observe(el));
```

## 231: How does content-visibility: auto relate to animations?

`content-visibility: auto` lets the browser skip layout and painting for a section while it's off-screen. Animations inside it don't need to be rendered then, which saves work. Combining it with `contain-intrinsic-size` avoids jumps in the scrollbar. It's also discrete-animatable, which is why `::details-content` animations transition `content-visibility` with `allow-discrete`.

## 232: How do you add an exit animation to an element that a framework removes from the DOM?

The framework removes the element right away, so there's nothing left to animate. You need to delay the removal: keep the element mounted with a "leaving" state, run the animation, and remove it on `animationend` or `anim.finished`. Most frameworks have a helper for this (React libraries like Motion, Vue's `<Transition>`, Angular's `animate.leave`). View transitions are another option, since the browser animates a snapshot of the old element.

## 233: How does Vue's Transition component work with CSS?

`<Transition>` adds classes at the right moments while an element enters or leaves, and you write the CSS.

```css
.fade-enter-active,
.fade-leave-active {
  transition: opacity 200ms ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
```

```html
<Transition name="fade">
  <p v-if="show">Hello</p>
</Transition>
```

It waits for `transitionend` or `animationend` before removing the element.

## 234: How do modern Angular versions handle enter and leave animations?

Recent Angular versions added `animate.enter` and `animate.leave` in templates. They add a CSS class when an element is created or removed, and Angular waits for the CSS animation to finish before removing the element. The older `@angular/animations` package, with `trigger()` and `state()`, is now deprecated, though you'll still see it in many existing projects.

```html
@if (open) {
<div class="panel" animate.enter="slide-in" animate.leave="slide-out">…</div>
}
```

## 235: How do you add custom animations in Tailwind CSS?

Tailwind has built-in classes like `animate-spin`, `animate-ping`, `animate-pulse` and `animate-bounce`, plus `transition`, `duration-*`, `ease-*` and `delay-*`. In Tailwind v4 you add your own in CSS with `@theme`:

```css
@theme {
  --animate-wiggle: wiggle 1s ease-in-out infinite;

  @keyframes wiggle {
    0%,
    100% {
      rotate: -3deg;
    }
    50% {
      rotate: 3deg;
    }
  }
}
```

Then use `class="animate-wiggle"`. The `motion-safe:` and `motion-reduce:` variants handle reduced motion.

## 236: What is layout thrashing and how does it affect JS-driven animations?

It happens when code reads layout (like `offsetHeight`) and writes styles in a loop. Each read after a write forces the browser to do layout right away, many times per frame. Group all reads first, then all writes, and do the writes in `requestAnimationFrame`.

```js
// bad: read, write, read, write...
items.forEach((el) => (el.style.height = `${el.scrollHeight}px`));

// better: read all, then write all
const heights = items.map((el) => el.scrollHeight);
requestAnimationFrame(() => {
  items.forEach((el, i) => (el.style.height = `${heights[i]}px`));
});
```

## 237: Why use requestAnimationFrame instead of setInterval for JS animations?

`requestAnimationFrame` calls your function right before the browser draws the next frame, at the screen's refresh rate, and pauses in background tabs. `setInterval` runs on its own timer, which doesn't line up with frames, so you get uneven motion and wasted work. Also base movement on the timestamp, not on a fixed step per frame, so it looks the same on 60 Hz and 120 Hz screens.

```js
let start;

function frame(now) {
  start ??= now;
  const t = Math.min((now - start) / 500, 1); // 0 to 1 over 500ms
  box.style.transform = `translateX(${t * 300}px)`;
  if (t < 1) requestAnimationFrame(frame);
}

requestAnimationFrame(frame);
```

## 238: Why doesn't a transition run when you add an element and its class at the same time?

The browser groups style changes and calculates them once, before the next frame. If you insert an element and set its final class in the same task, the browser only ever sees the final style, so there is no "from" value. Fixes: use `@starting-style`, or force a style calculation between the two steps (read `el.offsetWidth` or call `getComputedStyle(el).opacity`), or set the class in a `requestAnimationFrame` callback after the first frame.

## 239: What is the double requestAnimationFrame trick?

Code inside one `requestAnimationFrame` callback still runs before the next style calculation, so changes there can be merged with earlier ones. Nesting two callbacks makes sure the first state was rendered before you apply the second. It was a common way to start a transition on a freshly added element. Today `@starting-style` is the cleaner fix.

```js
document.body.append(toast);
requestAnimationFrame(() => {
  requestAnimationFrame(() => toast.classList.add("visible"));
});
```

## 240: How do you find out why an animation is janky?

Record it in the DevTools Performance panel and look at the frames. Long yellow tasks mean JavaScript is blocking the main thread. Purple "Layout" or green "Paint" on every frame means you're animating expensive properties. The Rendering tab can show paint flashing (areas being repainted) and layer borders. Then fix the cause: move to `transform`/`opacity`, cut JS work, or reduce the painted area.

## 241: What does paint flashing show you?

In Chrome's Rendering tab, "Paint flashing" highlights areas in green each time they're repainted. If a small hover effect makes the whole page flash, something is triggering a large repaint, maybe a `box-shadow` on a big element or an element without its own layer. A `transform` or `opacity` animation on a composited layer shouldn't flash at all.

## 242: How do you check which elements have their own compositor layer?

In Chrome, turn on "Layer borders" in the Rendering tab, or open the Layers panel to see every layer, why it was created and how much memory it uses. Firefox has similar options in its developer settings. This helps you spot too many layers (memory problems) or an animated element that isn't on its own layer.

## 243: Do animations affect Cumulative Layout Shift?

Animating layout properties like `top`, `margin` or `height` moves other elements and can count as layout shifts, which hurts CLS. Changes to `transform` don't count as layout shifts, because they don't change layout. Shifts within 500 ms after a user input like a click are also excluded. Another reason to animate with `transform`.

## 244: How can animations hurt Interaction to Next Paint (INP)?

INP measures how long it takes for the page to show a response after a click, tap or key press. JavaScript animations, heavy style recalculation or layout-heavy CSS animations on the main thread can delay that next frame. Compositor-only animations don't block it. If an interaction starts a big animation, make sure the first visual change happens fast.

## 245: How do you make an image zoom on hover without overflowing its card?

Put the image in a box with `overflow: hidden` and scale the image inside.

```css
.thumb {
  overflow: hidden;
  border-radius: 8px;
}

.thumb img {
  display: block;
  width: 100%;
  transition: scale 400ms ease;
}

.thumb:hover img {
  scale: 1.08;
}
```

## 246: Can you animate object-position?

Yes. `object-position` is animatable, so you can slowly pan an image inside its box (a "Ken Burns" effect), often together with `scale`.

```css
.cover {
  width: 100%;
  height: 300px;
  object-fit: cover;
  animation: pan 12s ease-in-out infinite alternate;
}

@keyframes pan {
  from {
    object-position: 0% 50%;
  }
  to {
    object-position: 100% 50%;
  }
}
```

## 247: Which SVG attributes can you animate with CSS?

Presentation attributes that are also CSS properties: `fill`, `stroke`, `stroke-width`, `stroke-dasharray`, `stroke-dashoffset`, `opacity` and `transform`. SVG 2 also made geometry like `cx`, `cy`, `r`, `rx`, `ry`, `x`, `y`, `width` and `height` into CSS properties, and current browsers can animate them. The path `d` property can be animated in Chromium and Firefox when both paths have the same structure; check Safari before relying on it.

## 248: What is transform-box and why does it matter for SVG?

In SVG, `transform-origin` is measured from the SVG's view box by default, not from the element itself, so `rotate` spins the shape around the top-left of the SVG. `transform-box: fill-box` makes the origin use the element's own bounding box.

```css
svg .gear {
  transform-box: fill-box;
  transform-origin: center;
  animation: spin 3s linear infinite;
}
```

## 249: Should you use SMIL or CSS for SVG animations?

SMIL (`<animate>`, `<animateTransform>`, `<animateMotion>`) works in all current browsers and runs even inside SVGs loaded with `<img>`, where CSS from the page can't reach. But it can't be controlled from your stylesheet, doesn't respect `prefers-reduced-motion` on its own, and is harder to maintain. Use CSS for inline SVGs in your UI, and SMIL only when the SVG must animate on its own as a separate file.

## 250: How do you morph one shape into another with clip-path?

Use two `polygon()` values with the same number of points. The browser moves each point to its matching point.

```css
.shape {
  clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
  transition: clip-path 400ms ease;
}

.shape:hover {
  clip-path: polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%);
}
```

If the point counts differ, the browser can't interpolate and it just switches.

## 251: How do you cycle through colors cheaply?

Animate `filter: hue-rotate()` instead of changing many color properties. One filter shifts all colors of the element at once.

```css
.rainbow {
  animation: hue 6s linear infinite;
}

@keyframes hue {
  to {
    filter: hue-rotate(360deg);
  }
}
```

It changes images and text inside too, so it suits decorative elements more than real content.

## 252: Why do dark mode toggles sometimes look bad with transitions, and how do you fix it?

If many elements have `transition: all` or color transitions, switching the theme makes hundreds of elements fade at slightly different speeds, which looks messy and costs a lot. A common fix is to disable transitions during the switch: add a class like `.no-transitions * { transition: none !important; }`, change the theme, then remove the class on the next frame. Or use a view transition for one clean cross-fade of the whole page.

## 253: How do you make a circular reveal when switching themes?

Use a view transition and animate a `clip-path` on the new snapshot, starting from the button's position.

```js
async function toggleTheme(event) {
  const x = event.clientX;
  const y = event.clientY;
  const r = Math.hypot(
    Math.max(x, innerWidth - x),
    Math.max(y, innerHeight - y),
  );

  const vt = document.startViewTransition(() => {
    document.documentElement.classList.toggle("dark");
  });
  await vt.ready;

  document.documentElement.animate(
    {
      clipPath: [
        `circle(0 at ${x}px ${y}px)`,
        `circle(${r}px at ${x}px ${y}px)`,
      ],
    },
    {
      duration: 500,
      easing: "ease-out",
      pseudoElement: "::view-transition-new(root)",
    },
  );
}
```

```css
::view-transition-old(root),
::view-transition-new(root) {
  animation: none;
}
```

## 254: Why do some pages show transitions running on page load, and how do you stop it?

If styles change right after the first render, for example when a theme class is added by JavaScript or a late stylesheet loads, transitions run from the old values to the new ones. A common fix is a `preload` class on `<body>` that turns off transitions, removed after the page loads. A better fix is to apply the correct styles before the first paint, like setting the theme class in a small inline script in the `<head>`.

## 255: Can media queries trigger transitions?

Yes. If a media query changes a transitioned property, resizing the window across a breakpoint will animate it. Sometimes that's fine, but often it looks odd, like a sidebar sliding when you rotate a phone. Limit the transition to properties you change on purpose, or put the transition inside a state class instead of the base rule.

## 256: How do you animate text letter by letter without hurting accessibility?

You need a separate element for each letter, usually made by JavaScript. Screen readers may read the letters one by one, so hide the spans and give the full text another way.

```html
<h1 aria-label="Hello">
  <span aria-hidden="true" style="--i: 0">H</span>
  <span aria-hidden="true" style="--i: 1">e</span>
  <span aria-hidden="true" style="--i: 2">l</span>
  <span aria-hidden="true" style="--i: 3">l</span>
  <span aria-hidden="true" style="--i: 4">o</span>
</h1>
```

```css
h1 span {
  display: inline-block;
  animation: drop 400ms ease-out both;
  animation-delay: calc(var(--i) * 50ms);
}
```

`aria-label` on a heading is read by most screen readers, but a visually hidden text copy is the safer choice.

## 257: How do you animate gradient text?

Clip the background to the text and move the background.

```css
.gradient-text {
  background: linear-gradient(90deg, #f06, #48f, #f06);
  background-size: 200% auto;
  background-clip: text;
  color: transparent;
  animation: shift 4s linear infinite;
}

@keyframes shift {
  to {
    background-position: 200% center;
  }
}
```

## 258: How do you draw a border around a box on hover?

Use two pseudo-elements: one for the top and right edges, one for the bottom and left, and grow them with `scale`.

```css
.box {
  position: relative;
}

.box::before,
.box::after {
  content: "";
  position: absolute;
  inset: 0;
  border: 2px solid transparent;
  scale: 0;
  transition: scale 300ms ease;
}

.box::before {
  border-top-color: currentColor;
  border-right-color: currentColor;
  transform-origin: top left;
}

.box::after {
  border-bottom-color: currentColor;
  border-left-color: currentColor;
  transform-origin: bottom right;
}

.box:hover::before,
.box:hover::after {
  scale: 1;
}
```

## 259: What are motion tokens in a design system?

They are shared, named values for durations and easings, like `--duration-fast: 120ms` and `--ease-out: cubic-bezier(0.2, 0.8, 0.2, 1)`. Using tokens instead of random numbers keeps motion consistent across a product, and you can change the whole feel in one place, or shorten everything for reduced motion.

```css
:root {
  --duration-fast: 120ms;
  --duration-medium: 240ms;
  --ease-out: cubic-bezier(0.2, 0.8, 0.2, 1);
}

.menu {
  transition: opacity var(--duration-medium) var(--ease-out);
}
```

## 260: Should duration depend on the size of the animated element?

Yes, a bit. An element moving across the whole screen needs more time than a small button changing state, or it looks too fast to follow. On the other hand, durations shouldn't grow in a straight line with distance, or full-screen moves get slow. A small range like 150 ms for tiny changes up to around 500 ms for large ones works for most UIs.

## 261: How do you make a spring animation with CSS?

Use `linear()` with points sampled from a spring curve. A tool calculates the spring and outputs the list for you.

```css
.sheet {
  transition: translate 600ms
    linear(
      0,
      0.009,
      0.035 2.1%,
      0.141,
      0.281 6.7%,
      0.723 12.9%,
      0.938 16.7%,
      1.017,
      1.077,
      1.121,
      1.149 24.3%,
      1.159,
      1.163,
      1.161,
      1.154 29.9%,
      1.129 32.8%,
      1.051 39.6%,
      1.017 43.1%,
      0.991,
      0.977 51%,
      0.974 53.8%,
      0.975 57.1%,
      0.997 69.8%,
      1.003 76.9%,
      1
    );
}
```

The limit is that the curve is fixed. A real spring in JavaScript can start with the current speed of a drag; `linear()` can't know that.

## 262: How do you make an element orbit around a point?

Rotate, move it out, then rotate back so it stays upright.

```css
.planet {
  animation: orbit 6s linear infinite;
}

@keyframes orbit {
  from {
    transform: rotate(0deg) translateX(120px) rotate(0deg);
  }
  to {
    transform: rotate(360deg) translateX(120px) rotate(-360deg);
  }
}
```

Leave out the last `rotate` if you want it to always face the center.

## 263: How do you build a rotating 3D cube?

Place six faces with `rotateY`/`rotateX` and `translateZ`, keep them in 3D with `preserve-3d`, and rotate the parent.

```css
.scene {
  perspective: 600px;
}

.cube {
  width: 100px;
  height: 100px;
  position: relative;
  transform-style: preserve-3d;
  animation: turn 8s linear infinite;
}

.face {
  position: absolute;
  inset: 0;
}
.front {
  transform: translateZ(50px);
}
.back {
  transform: rotateY(180deg) translateZ(50px);
}
.right {
  transform: rotateY(90deg) translateZ(50px);
}
.left {
  transform: rotateY(-90deg) translateZ(50px);
}
.top {
  transform: rotateX(90deg) translateZ(50px);
}
.bottom {
  transform: rotateX(-90deg) translateZ(50px);
}

@keyframes turn {
  to {
    transform: rotateX(360deg) rotateY(360deg);
  }
}
```

## 264: What does perspective-origin do?

It sets where the viewer is looking from, for an element with `perspective`. The default is the center. Moving it to `left top` makes children look like they're seen from the top-left. Animating it can create a "camera moving" effect.

## 265: How do you make a card tilt toward the mouse?

Write the mouse position into custom properties with JavaScript, and let CSS do the transform.

```js
card.addEventListener("pointermove", (e) => {
  const r = card.getBoundingClientRect();
  card.style.setProperty(
    "--x",
    ((e.clientX - r.left) / r.width - 0.5).toFixed(3),
  );
  card.style.setProperty(
    "--y",
    ((e.clientY - r.top) / r.height - 0.5).toFixed(3),
  );
});

card.addEventListener("pointerleave", () => {
  card.style.setProperty("--x", 0);
  card.style.setProperty("--y", 0);
});
```

```css
.card {
  transform: perspective(800px) rotateY(calc(var(--x, 0) * 20deg))
    rotateX(calc(var(--y, 0) * -20deg));
  transition: transform 150ms ease-out;
}
```

## 266: Can you animate variable font axes?

Yes. With a variable font you can animate `font-weight`, `font-stretch` or custom axes with `font-variation-settings`, and the glyphs change smoothly.

```css
.title {
  font-family: "Inter Variable", sans-serif;
  transition: font-weight 300ms;
}

.title:hover {
  font-weight: 800;
}
```

## 267: Why can animating font-weight cause layout shifts?

Bolder text is usually wider, so the text box grows and pushes other content around, and the browser has to redo layout every frame. To avoid it, reserve the space (for example, a hidden bold copy that sets the width), use a font with a "grade" axis that changes thickness without width, or keep weight changes on elements that don't affect others.

## 268: How do you make a modal look like it grows from the button that opened it?

Set `transform-origin` on the modal to the button's position, then scale from a small size.

```js
openButton.addEventListener("click", () => {
  const b = openButton.getBoundingClientRect();
  const m = dialog.getBoundingClientRect();
  dialog.style.transformOrigin = `${b.left + b.width / 2 - m.left}px ${b.top + b.height / 2 - m.top}px`;
  dialog.showModal();
});
```

Measure the dialog after it's displayed if its position depends on content. A view transition with a shared `view-transition-name` is another way to get the same effect.

## 269: How do you animate a stack of toasts so others move when one is removed?

When a toast is removed, the ones below jump up. Animate that movement with FLIP: measure positions before removal, remove it, measure again, and animate each toast's `transform` from the old offset. Or wrap the removal in `document.startViewTransition()` and give each toast its own `view-transition-name`; the browser then animates the others into their new places.

## 270: Can you animate grid-template-columns?

Yes, in all current browsers, as long as both values have the same number of tracks. Lengths, percentages and `fr` values are interpolated. It's useful for sidebars that open and close.

```css
.layout {
  display: grid;
  grid-template-columns: 240px 1fr;
  transition: grid-template-columns 300ms ease;
}

.layout.collapsed {
  grid-template-columns: 64px 1fr;
}
```

It still triggers layout every frame, so test on slow devices.

## 271: Can you animate flex-grow and flex-basis?

Yes. Both are animatable, so you can make one panel grow while others shrink, for example an accordion of image panels that widen on hover. Like any layout animation, it recalculates layout each frame.

```css
.panel {
  flex: 1;
  transition: flex-grow 400ms ease;
}

.panel:hover {
  flex-grow: 4;
}
```

## 272: Can you animate gap?

Yes, `gap`, `row-gap` and `column-gap` take lengths and animate smoothly in flex and grid containers. It's layout work, so it's best for small containers.

## 273: How does z-index animate?

`z-index` is an integer, so it animates in whole-number steps: from 1 to 10 it goes 1, 2, 3 and so on. In practice it looks like it switches. `auto` can't be interpolated, so going between `auto` and a number is discrete.

## 274: Can you animate the content property?

Only discretely: the text switches at one point. With keyframes you can use it for simple effects like cycling loading text.

```css
.loading::after {
  content: "";
  animation: dots 1.5s steps(1) infinite;
}

@keyframes dots {
  0% {
    content: "";
  }
  25% {
    content: ".";
  }
  50% {
    content: "..";
  }
  75% {
    content: "...";
  }
}
```

Keep in mind screen readers may read the changing content.

## 275: What does scroll-behavior: smooth do?

It makes scrolling triggered by anchors, `scrollIntoView()` or `scrollTo()` animate instead of jumping. You can't set the speed or easing; the browser decides. For JavaScript you can also pass `{ behavior: "smooth" }` per call.

```css
html {
  scroll-behavior: smooth;
}
```

## 276: Should you turn off smooth scrolling for reduced motion?

Yes, long smooth scrolls are motion that can bother people.

```css
@media (prefers-reduced-motion: no-preference) {
  html {
    scroll-behavior: smooth;
  }
}
```

In JavaScript, check the media query before passing `behavior: "smooth"`.

## 277: How do scroll-driven animations work with scroll snap carousels?

Each slide can use a view timeline on the carousel's inline axis, so it scales up or fades as it gets to the center, and scroll snap makes sure it stops on a slide.

```css
.carousel {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
}

.slide {
  scroll-snap-align: center;
  animation: focus linear both;
  animation-timeline: view(inline);
}

@keyframes focus {
  0%,
  100% {
    scale: 0.85;
    opacity: 0.5;
  }
  50% {
    scale: 1;
    opacity: 1;
  }
}
```

## 278: How many animations can run at the same time?

There's no fixed number. A hundred compositor-only `transform` animations can be fine, while a few that animate `box-shadow` on big elements can be slow. It depends on the properties, the size of the painted areas, the number of layers and the device. Test on a cheap phone with CPU throttling and watch for dropped frames.

## 279: How do you deal with animations in end-to-end tests?

Animations make tests slow and flaky, because elements move or aren't clickable yet. Options:

- Emulate reduced motion and make sure your CSS respects it. In Playwright: `page.emulateMedia({ reducedMotion: "reduce" })`.
- Add a test-only class or style that sets very short durations.
- For Playwright screenshots, pass `animations: "disabled"`, which finishes finite animations and resets infinite ones.
- Wait for `el.getAnimations()` to finish before asserting.

## 280: Why do visual regression tests fail on animated pages?

Screenshots taken mid-animation differ every run. Spinners, carets, shimmer effects and auto-playing carousels are common causes. Disable or finish animations before the screenshot, wait for `document.getAnimations()` to settle, mask animated areas, or hide the caret with `caret-color: transparent` in the test styles.

## 281: Do CSS animations run in jsdom?

No. jsdom doesn't do layout or rendering, so transitions and animations never run and `animationend` and `transitionend` never fire on their own. `element.animate()` isn't implemented either. In unit tests, mock these or fire the events yourself, and test real motion in a browser-based tool like Playwright.

## 282: How do CSS Modules handle keyframe names?

CSS Modules make `@keyframes` names local by default, just like class names: `fade` becomes something like `styles_fade__a1b2c`, and `animation: fade` in the same file is rewritten to match. If you want a global name (for example to use it from another file or library), wrap it in `:global(fade)`.

## 283: How do you define keyframes in CSS-in-JS libraries?

Most of them have a `keyframes` helper that creates a uniquely named `@keyframes` rule and returns its name.

```js
import styled, { keyframes } from "styled-components";

const fadeIn = keyframes`
  from { opacity: 0; }
  to { opacity: 1; }
`;

const Box = styled.div`
  animation: ${fadeIn} 300ms ease-out;
`;
```

## 284: Can you put @keyframes inside a media query?

Yes. A `@keyframes` rule inside `@media` only exists when the media query matches. You can use this to define a softer version of the same named animation for reduced motion.

```css
@keyframes enter {
  from {
    translate: 0 40px;
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  @keyframes enter {
    from {
      opacity: 0;
    }
  }
}
```

The later rule with the same name wins when the media query matches.

## 285: How do @keyframes rules behave in cascade layers?

If the same keyframes name is defined in more than one layer, the one in the higher-priority layer wins, the same as for normal styles. Unlayered keyframes beat layered ones. So a library's `fade-in` in a `vendor` layer can be overridden by your own `fade-in` in a later layer or outside layers.

## 286: How do keyframes work with shadow DOM?

Keyframes names are scoped to the tree they're defined in. The safest approach is to define the `@keyframes` inside the same shadow root's styles that use them. Browsers have differed in whether styles in a shadow root can see keyframes defined in the main document, so don't depend on that. Inherited animation timing from custom properties works fine across the boundary.

## 287: How can :has() trigger animations?

`:has()` lets you animate something based on the state of a child or a later sibling, which used to need JavaScript.

```css
.form:has(:user-invalid) .submit {
  animation: shake 300ms;
}

.card:has(input:checked) {
  outline: 2px solid royalblue;
  transition: outline-color 200ms;
}
```

## 288: How do you trigger animations with :checked without JavaScript?

Use a checkbox or radio button and a sibling selector. It works for tabs, accordions and toggles.

```html
<input type="checkbox" id="more" class="toggle" />
<label for="more">Show more</label>
<div class="extra">…</div>
```

```css
.extra {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows 300ms;
}

.extra > * {
  overflow: hidden;
}

.toggle:checked ~ .extra {
  grid-template-rows: 1fr;
}
```

Make sure the result is still usable with a keyboard and screen readers.

## 289: How do you trigger an animation once when an element scrolls into view, using JavaScript?

Use IntersectionObserver to add a class, and stop observing after the first time.

```js
const io = new IntersectionObserver(
  (entries) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      entry.target.classList.add("in-view");
      io.unobserve(entry.target);
    }
  },
  { threshold: 0.2 },
);

document.querySelectorAll(".reveal").forEach((el) => io.observe(el));
```

Unlike scroll-driven animations, this plays on time once triggered and doesn't follow the scroll position.

## 290: Why can animating a full-page background be slow?

Repainting a large area on each frame is expensive, especially on high-resolution screens where the browser paints millions of pixels. Animating `background-position` or a gradient on the `body` can do this. Instead, put the background on a separate fixed layer and animate its `transform` or `opacity`, so the compositor just moves a ready-made image.

## 291: Can too many composited layers cause problems?

Yes. Every layer is a GPU texture that uses memory: width times height times 4 bytes, times the screen scale squared. A full-screen layer on a 3x phone can be many megabytes. With too many layers, memory runs out, the browser falls back to slower paths and mobile pages can even crash. Only promote elements that really animate, and remove `will-change` when they stop.

## 292: How do you make many looping animations look random without JavaScript?

Give items different durations or delays using prime numbers so their loops rarely line up (sometimes called the "cicada principle").

```css
.star:nth-child(2n) {
  animation-duration: 3s;
}
.star:nth-child(3n) {
  animation-duration: 5s;
}
.star:nth-child(5n) {
  animation-delay: -1.3s;
}
.star:nth-child(7n) {
  animation-delay: -2.9s;
}
```

Negative delays make each item start at a different point without waiting.

## 293: How do you build a ripple effect on click?

You need JavaScript to place the ripple where the click happened, then CSS animates it.

```js
button.addEventListener("pointerdown", (e) => {
  const r = button.getBoundingClientRect();
  const ripple = document.createElement("span");
  ripple.className = "ripple";
  ripple.style.left = `${e.clientX - r.left}px`;
  ripple.style.top = `${e.clientY - r.top}px`;
  button.append(ripple);
  ripple.addEventListener("animationend", () => ripple.remove());
});
```

```css
button {
  position: relative;
  overflow: hidden;
}

.ripple {
  position: absolute;
  width: 20px;
  height: 20px;
  margin: -10px 0 0 -10px;
  border-radius: 50%;
  background: currentColor;
  opacity: 0.3;
  animation: ripple 500ms ease-out forwards;
  pointer-events: none;
}

@keyframes ripple {
  to {
    scale: 20;
    opacity: 0;
  }
}
```

## 294: How do you animate a check mark being drawn?

Draw the check as an SVG path and animate `stroke-dashoffset`, starting when the checkbox is checked.

```css
.check path {
  stroke-dasharray: 1;
  stroke-dashoffset: 1;
  transition: stroke-dashoffset 250ms ease-out;
}

input:checked + .check path {
  stroke-dashoffset: 0;
}
```

The path needs `pathLength="1"` so the dash numbers match its length.

## 295: How do you animate an accordion to its real height with JavaScript?

Measure `scrollHeight` and animate the height with the Web Animations API, then clean up.

```js
function expand(panel) {
  panel.hidden = false;
  const h = panel.scrollHeight;
  const anim = panel.animate([{ height: "0px" }, { height: `${h}px` }], {
    duration: 250,
    easing: "ease-out",
  });
  panel.style.overflow = "hidden";
  anim.onfinish = () => (panel.style.overflow = "");
}
```

Since the animation has no fill, the panel goes back to `height: auto` at the end, so it still adapts if the content changes.

## 296: How do you cross-fade between two views without view transitions?

Keep both views in the DOM for a moment, stacked on top of each other with grid or absolute positioning. Fade the old one out and the new one in, then remove the old one when its animation ends. This is what many router transition helpers did before view transitions existed. The stacking is the tricky part, because two views in normal flow would push each other around.

## 297: What happens when a transition and a keyframe animation affect the same property?

The animation wins while it runs, because animation styles sit above normal styles and transitions animate the normal style. When the animation ends, the property goes back to the normal value at once, without a transition. Avoid having both control the same property.

## 298: Do changes made by a CSS animation trigger transitions?

No. Values coming from an animation don't start transitions, even on properties that have a `transition`. Transitions only react to changes in the normal (before-animation) computed value. That's why animating `color` with keyframes doesn't also run a color transition.

## 299: Why does my position: fixed child stop being fixed when the parent animates transform?

Any `transform` other than `none` (also `translate`, `scale`, `rotate`, `filter`, `perspective`, and `will-change` on those) makes the element the containing block for `position: fixed` descendants. The fixed child then sticks to the parent, not the viewport. It's a common bug with modals inside animated containers. Move the fixed element out of the transformed parent, for example to the end of `<body>` or into a `<dialog>` in the top layer.

## 300: Why does z-index break when an element is being transformed?

`transform`, `opacity` below 1, `filter` and `will-change` on them create a new stacking context. Children's `z-index` values then only count inside that context and can't go above elements outside it. During an animation (or permanently with `will-change`) a dropdown inside the animated element may suddenly appear behind siblings. Fix it by adjusting the parent's `z-index` or by moving the popup into the top layer.

# Advanced Questions (301-450)

## 301: What are the main steps the browser takes to render a frame?

Roughly: run JavaScript (including `requestAnimationFrame` callbacks), recalculate styles, do layout (sizes and positions), paint (draw display lists for each layer), and composite (put the layers together on screen, usually on the GPU). Each animated property starts this chain at a different point, and the earlier it starts, the more work each frame costs.

## 302: Which rendering steps do different properties trigger?

- Layout properties (`width`, `top`, `margin`, `font-size`, `grid-template-columns`): style, layout, paint, composite.
- Paint-only properties (`color`, `background-color`, `box-shadow`, `border-radius`): style, paint, composite.
- Compositor properties (`transform`, `translate`, `rotate`, `scale`, `opacity`, often `filter`): just composite, when the element has its own layer.

The exact details differ by browser and version, so measure instead of trusting a table.

## 303: Why can a transform animation keep running while JavaScript blocks the main thread?

Once a `transform` or `opacity` animation is handed to the compositor thread, the compositor knows the keyframes and timing and can work out every frame by itself, without asking the main thread. So a spinner using `rotate` keeps spinning during a long task, while a spinner that changes `width` or uses JavaScript freezes. The main thread is still needed to start, change or stop the animation.

## 304: When does a transform or opacity animation not run on the compositor?

Some common reasons: the element can't be promoted to its own layer, the animation also includes properties the compositor can't handle, transforms use percentages on a box that changes size, a running animation is changed from JavaScript in a way that needs the main thread, or the animation uses a feature the browser hasn't made compositor-ready. Chrome's DevTools Performance panel shows animations and, in many cases, why one couldn't be composited. Treat "compositor-only" as something to check, not to assume.

## 305: Why are transform and opacity animations cheap once composited?

The element is painted once into a layer (a GPU texture). Changing `transform` only changes where and how that texture is drawn, and `opacity` only changes how it is blended. Neither needs a new paint, so each frame is just a GPU draw call with new numbers. Any change that alters the pixels inside the layer (like a new color) needs a repaint.

## 306: What is implicit compositing or layer explosion?

If an element with its own layer could visually overlap elements painted after it, the browser may have to give those later elements their own layers too, to keep the stacking order right. One animated element can then cause many extra layers. This uses lots of memory and slows things down. Fixes: give the animated element a higher `z-index` so fewer things are above it, or keep it out of the way of long lists.

## 307: What is the right way to use will-change?

Add it shortly before the animation starts and remove it after the animation ends, so the layer only exists when needed.

```js
el.addEventListener("pointerenter", () => (el.style.willChange = "transform"));
el.addEventListener("transitionend", () => (el.style.willChange = "auto"));
```

Setting it permanently in CSS is fine for elements that animate often (like a slide-out menu) but not for long lists of items. Don't use `will-change: all` or put it on `*`.

## 308: What side effects does will-change: transform have?

Besides creating a layer, it acts like the element has a transform even when it doesn't: it creates a stacking context and becomes the containing block for `position: fixed` and absolutely positioned descendants. It can also change how text is drawn (for example, losing subpixel anti-aliasing in some browsers). So adding it can change layout and stacking, not just performance.

## 309: Why does text sometimes look blurry during or after a scale animation?

A composited layer is painted at one resolution and then scaled as a texture. Scaling it up makes it blurry until the browser repaints it at the new size, which some browsers only do when the animation ends. Fractional `translate` values can also put text between pixels. Fixes: animate from a large size down to the normal size instead of up, round translate values, or remove `will-change` after the animation so the browser repaints sharply.

## 310: What is pixel snapping and how does it affect animations?

At rest, browsers usually align layers to whole device pixels so edges and text look crisp. During a transform animation, positions are fractional to keep motion smooth. When the animation ends, the element may snap to the nearest whole pixel, which looks like a small jump at the end. Using transforms that end on whole pixels and avoiding odd sizes with percentage translates reduces it.

## 311: What does a 120 Hz screen change for animations?

The browser draws frames at the screen's rate, so you get 8.3 ms per frame instead of 16.7 ms. CSS and Web Animations API animations adapt automatically because they're based on time. JavaScript that moves something by a fixed amount per frame will run twice as fast; always use the timestamp. Main-thread animations also have less time per frame, so they drop frames more easily.

## 312: What is the frame budget, and what eats into it?

At 60 Hz there are about 16.7 ms per frame, but the browser needs part of that for its own work, so your code realistically has around 10 ms. Every frame has to fit: input handlers, `requestAnimationFrame` callbacks, style, layout, paint and compositing. A single 50 ms task means at least two or three frames are lost. Long tasks, big style recalcs and large paints are the usual problems.

## 313: Why is animating a custom property on :root expensive?

Unregistered custom properties inherit, and so do registered ones with `inherits: true`. Changing a value on `:root` makes the browser recheck the computed style of every element in the document on every frame, even if only one element uses the value. Set animated custom properties as close as possible to where they're used, and register them with `inherits: false` when possible.

## 314: Do @property animations run on the compositor?

Usually not. Animating a registered custom property runs on the main thread, because the browser has to recompute every style that depends on it, and then it may need paint (for example a gradient). They're still smooth when the main thread is free, but they don't survive long tasks the way `transform` does. If you can, express the effect with `transform` or `opacity` instead.

## 315: What is the CSS Paint API and how does it relate to animations?

The CSS Paint API (part of Houdini) lets you draw an element's background or border with a JavaScript "paint worklet", which can read custom properties. Animating a registered custom property makes the worklet repaint every frame, which allows effects like animated patterns. It is mainly supported in Chromium browsers, so treat it as an enhancement. It still runs paint on each frame, so it's not as cheap as `transform`.

## 316: What happened to Animation Worklet?

Animation Worklet was a Houdini proposal to run custom animation code off the main thread, mainly for scroll-linked effects. It never shipped widely. Most of its use cases are now covered by scroll-driven animations (`ScrollTimeline` and `ViewTimeline`), which do run off the main thread for compositor-friendly properties. Don't build on Animation Worklet today.

## 317: How does the browser interpolate between two transform lists?

If both lists have the same functions in the same order (like `translate() rotate()` to `translate() rotate()`), it interpolates each function's numbers separately. If one side is `none`, it's treated as matching identity functions. If the lists don't match, the browser turns each into a matrix, breaks the matrices into translate, rotate, scale and skew parts, and interpolates those. The matrix path can produce odd motion.

## 318: Why does animating from rotate(0deg) to rotate(360deg) work, but a matrix-based transition doesn't spin?

With matching functions, the browser interpolates the angle itself, 0 to 360, so it spins. But 0 and 360 degrees give the same matrix. If the transform lists don't match and the browser falls back to matrix interpolation, start and end look the same and nothing moves. Keep function lists matching, or use the separate `rotate` property, which always interpolates the angle.

## 319: How are 3D rotations interpolated?

For `rotate3d()` with the same axis on both sides, the angle is interpolated directly. When the axes differ or the browser falls back to matrices, rotations are converted to quaternions and interpolated with spherical interpolation (slerp), which takes the shortest path. That means a 3D rotation of more than 180 degrees may go "the other way", which can surprise you.

## 320: How are the individual transform properties combined with transform?

The final transform is built in a fixed order: `translate`, then `rotate`, then `scale`, then the `transform` property, all applied around `transform-origin`. Each one is animated on its own, so you can run a `scale` hover transition and a `rotate` keyframe animation on the same element without them fighting. You can't change their order; if you need a different order, use `transform`.

## 321: How are colors with transparency interpolated?

Colors are interpolated with premultiplied alpha: each channel is multiplied by alpha before mixing and divided after. This is why going from `red` to `transparent` fades red out cleanly, instead of passing through a dark gray like old browsers did, since `transparent` is black with zero alpha. Premultiplication means the zero-alpha color has no effect on the hue.

## 322: Can you control the color space a transition uses?

Not directly. Transitions use sRGB for legacy color syntaxes and Oklab otherwise. If you want a specific space, like OKLCH for vivid hue changes, animate a registered percentage and mix colors yourself:

```css
@property --p {
  syntax: "<percentage>";
  initial-value: 0%;
  inherits: false;
}

.chip {
  background: color-mix(in oklch, #ff3b30, #007aff var(--p));
  transition: --p 600ms;
}

.chip:hover {
  --p: 100%;
}
```

## 323: How does the browser interpolate box-shadow lists of different lengths?

The shorter list is padded with transparent zero-size shadows so both have the same length, and then each shadow is interpolated pair by pair. If a pair has one `inset` and one outer shadow, they can't be interpolated, and the whole value switches discretely. Keep the same number of shadows and the same `inset` on both sides.

## 324: How are filter lists interpolated?

If both lists have the same functions in the same order, each function is interpolated. If one list is shorter but matches the start of the other, the missing functions are filled with their default values (like `blur(0)`). If the lists don't match otherwise, the animation is discrete. `none` acts like a list of default-value functions.

## 325: How does interpolation between lengths in different units work?

The browser interpolates them as a `calc()` mix. From `100px` to `50%`, the value halfway is `calc(50px + 25%)`. That's why you can transition `width` from pixels to percentages. It doesn't work with `auto` or other keywords, which need `interpolate-size` or `calc-size()`.

## 326: Why is interpolate-size opt-in instead of on by default?

Turning it on by default would change existing sites: places where developers had transitions on `height` that changed to `auto` and were happy with the instant jump would suddenly animate. So browsers made it opt-in. It's inherited, so setting it once on `:root` turns it on for the whole page.

## 327: What can calc-size() do that interpolate-size can't?

`calc-size()` works on one value and lets you do math on an intrinsic size, like adding padding to `auto`:

```css
.panel.open {
  height: calc-size(auto, size + 2rem);
}
```

`interpolate-size` only allows animating to the keyword itself. Both are currently Chromium-only, so `calc-size()` values need a fallback declaration before them.

## 328: What are the before-change style and after-change style in transitions?

When styles change, the browser compares two computed styles: the before-change style (the old values, including the current state of running animations and transitions) and the after-change style (the new values, without animations). For each transitioned property, if they differ, a transition starts from the before value to the after value. Understanding this explains most "why didn't my transition run" problems.

## 329: Why do elements inside a display: none container not transition?

Elements without a box don't have a before-change style, so there's nothing to compare. When the container becomes visible, the children get their first style directly. `@starting-style` exists to provide that missing "before" style for first render.

## 330: What is a timeline in the Web Animations model?

A timeline gives animations a current time. `document.timeline` is time-based; its time starts at 0 when the document is created and keeps moving forward. Scroll and view timelines give a progress based on scroll position instead. Every animation has a start time on its timeline, and its own current time is (timeline time - start time) times the playback rate.

## 331: In what order are animation effects stacked on the same property?

From bottom to top: the normal computed value, then CSS transitions, then CSS animations, then animations created with the Web Animations API. Within CSS animations, later names in `animation-name` are higher. Within script animations, ones created later are higher. With `composite: "replace"`, the top one wins; `add` and `accumulate` build on what's below.

## 332: What happens if you change animation-duration while an animation runs?

The animation's elapsed time stays the same, but its progress is recalculated with the new duration. So if 1 second has passed in a 2 second animation (50%) and you change the duration to 4 seconds, it jumps back to 25%. To change speed without a jump, use `playbackRate` or `updatePlaybackRate()` through the Web Animations API.

## 333: What happens if you change animation-name on a running animation?

Removing a name cancels that animation. Adding a new name starts a fresh one. If the list changes but a name stays in it, that animation keeps running, because browsers match running animations by name. Changing other properties like the timing function updates the running animation without restarting it.

## 334: How do CSS animation-play-state and JavaScript pause() interact?

Calling `anim.pause()` on a `CSSAnimation` overrides `animation-play-state` from then on. If CSS later changes `animation-play-state` to `paused` and back to `running`, behavior can be confusing, because the JavaScript pause "wins" until you call `play()`. Pick one place to control playback: CSS for simple cases, JavaScript when you need full control.

## 335: What is automatic removal of filling animations?

When a Web Animations API animation with `fill: "forwards"` has finished and is fully covered by a later animation on the same properties of the same element, the browser removes it automatically and fires a `remove` event. This stops memory growing when you call `animate()` with `forwards` many times, like on every mouse move. Call `anim.persist()` if you need to keep it.

## 336: What do getTiming(), getComputedTiming() and updateTiming() do?

They live on `anim.effect`. `getTiming()` returns the timing you set (duration, delay, easing...). `getComputedTiming()` adds calculated values, like current `progress`, `currentIteration`, `activeDuration` and `endTime`. `updateTiming()` changes timing on a running animation.

```js
const { progress, currentIteration } = anim.effect.getComputedTiming();
anim.effect.updateTiming({ duration: 800 });
```

## 337: How do you create scroll-driven animations from JavaScript?

Pass a `ScrollTimeline` or `ViewTimeline` as the `timeline` option, and use `rangeStart` and `rangeEnd` for the range.

```js
el.animate(
  { opacity: [0, 1], transform: ["translateY(40px)", "none"] },
  {
    fill: "both",
    timeline: new ViewTimeline({ subject: el }),
    rangeStart: "entry 0%",
    rangeEnd: "cover 30%",
  },
);
```

There's no duration because progress comes from scrolling.

## 338: Do scroll-driven animations run off the main thread?

In browsers that support compositing them, yes, for compositor-friendly properties like `transform` and `opacity`. The scroll position and the animation are updated together on the compositor, so the effect stays in sync with scrolling even when JavaScript is busy. This is a big advantage over JavaScript scroll listeners, which run on the main thread and often lag one frame behind.

## 339: What happens to a scroll-driven animation if its container can't scroll?

If the scroll container has no overflow, the timeline is inactive and the animation has no effect, so the element shows its normal styles. This often surprises people when a page is shorter than the screen on large monitors. Design the default styles so they look fine when the animation doesn't run.

## 340: Can you use range names inside @keyframes?

Yes. Keyframe selectors can include a timeline range name and a percentage, so one animation can define an entry part and an exit part.

```css
@keyframes in-and-out {
  entry 0% {
    opacity: 0;
    translate: 0 40px;
  }
  entry 100% {
    opacity: 1;
    translate: 0 0;
  }
  exit 0% {
    opacity: 1;
  }
  exit 100% {
    opacity: 0;
  }
}

.card {
  animation: in-and-out linear both;
  animation-timeline: view();
}
```

## 341: Can CSS start a time-based animation when an element scrolls into view?

Scroll-driven animations follow the scroll, they don't play on time once triggered. Browsers are working on scroll-triggered animations in CSS, but they're not something you can rely on everywhere yet. Today, use IntersectionObserver to add a class or call `element.animate()` when the element enters the view.

## 342: What does the browser actually do during a view transition?

1. It captures the old state: a snapshot image for each named element and the root.
2. It pauses rendering and runs your update callback.
3. It captures the new state; new named elements are shown live.
4. It builds the `::view-transition` pseudo-element tree on top of the page.
5. It runs the animations. Groups animate from the old position and size to the new ones, and old and new images cross-fade.
6. When they finish, it removes the pseudo-elements.

## 343: What does it mean that old view transition snapshots are static images?

The `::view-transition-old()` content is a picture of the old element at the moment of capture. Videos, GIFs and CSS animations in it are frozen, and it doesn't react to clicks. The `::view-transition-new()` side is a live view of the new element, so its content keeps updating.

## 344: Why do elements look stretched in a view transition, and how do you fix it?

The group animates `width` and `height` from the old size to the new, and by default the old and new images fill the group, so text and images stretch if the aspect ratio changes. Fix it by making the images keep their ratio:

```css
::view-transition-old(card),
::view-transition-new(card) {
  height: 100%;
  object-fit: none;
  overflow: clip;
}
```

Picking the right `object-fit` and `object-position` depends on the design.

## 345: Why do named elements escape overflow: hidden during a view transition?

Every named element is lifted into its own group directly under `::view-transition`, on top of the page. It's no longer inside its old parent, so the parent's `overflow` and `clip-path` don't apply. A card in a scrolling list can fly over the header. Fixes include naming the clipping container too, or using nested view transition groups where the browser supports them.

## 346: Can users interact with the page during a view transition?

Not really. The `::view-transition` overlay sits above the page while it runs, and the old view is just an image. Clicks don't reach the elements underneath as you'd expect. Keep view transitions short (often under 300-400 ms) so the page doesn't feel blocked.

## 347: What happens if the update callback in startViewTransition takes too long?

Rendering is paused while the callback runs, so the page looks frozen. If it takes too long, the browser gives up on the animation (Chrome uses a timeout of a few seconds) and the transition promises reject, but the DOM update still happens. Don't fetch data inside the callback; load it first and only do the DOM swap inside.

## 348: How do you avoid a flash of incomplete content in cross-document view transitions?

The new page may start the transition before key elements are parsed, so a named element isn't there yet. Mark them as render-blocking:

```html
<link rel="expect" href="#hero-image" blocking="render" />
```

The browser waits until that element is parsed before the first render, so the transition can find it. Use it sparingly, because it delays the first paint.

## 349: When do cross-document view transitions happen?

Only for same-origin navigations, when both the old and new page opt in with `@view-transition { navigation: auto; }`. They apply to normal navigations like link clicks, back and forward, but not to reloads or to navigations with a cross-origin redirect in between. Use `pageswap` and `pagereveal` with `navigation.activation` to find where you came from and adjust the animation.

## 350: What does a view transition cost in memory?

Each named element is captured as a texture for the old state, and the new state is rendered too. A full-page root snapshot on a high-resolution phone can take many megabytes, and naming hundreds of list items multiplies that. Name only the elements that really need their own animation, and leave the rest in the root cross-fade.

## 351: Why do you often need flushSync when using view transitions with React?

`startViewTransition` captures the new state as soon as your callback's promise resolves. React normally batches updates and renders later, so if you just call `setState` inside the callback, the browser may capture the DOM before React changed it. `flushSync` forces React to apply the update right away.

```jsx
import { flushSync } from "react-dom";

document.startViewTransition(() => {
  flushSync(() => setPage("details"));
});
```

Newer React versions are adding built-in view transition support that handles this for you.

## 352: How do you debug a view transition?

In Chrome DevTools, open the Animations panel and slow the playback down. The view transition pseudo-elements show up there and in the Elements panel under `<html>`, where you can pause and inspect `::view-transition-group()` and its children, and edit their styles live. Check the console for errors like duplicate `view-transition-name` values, which make the browser skip the transition.

## 353: How does the default view transition cross-fade avoid a "see-through" moment?

If you simply fade one image out and another in, both are partly transparent halfway, so the background shows through. The browser puts the old and new images inside `::view-transition-image-pair` with `isolation: isolate`, and blends them with `mix-blend-mode: plus-lighter`. The two half-transparent images add up to full opacity, so the cross-fade looks solid. Keep this in mind if you replace the default animations.

## 354: When would you choose FLIP over view transitions, and the other way round?

View transitions are easier for big changes: route changes, elements moving between containers, elements appearing and disappearing, and cross-document navigation. But they freeze the page during the update, block interaction while running and use snapshot images. FLIP with the Web Animations API animates real, live elements, so it's better for small, frequent or interruptible changes, like reordering a list while the user keeps interacting. FLIP needs more code and only handles elements that exist before and after.

## 355: How do you do a list-to-detail shared element transition with many items?

Only one element can have a given name at a time. So don't give every item the same name; instead set the name only on the clicked item right before the transition, and give the matching element on the detail page the same name.

```js
function openDetails(card, id) {
  card.querySelector("img").style.viewTransitionName = "hero";
  document.startViewTransition(() => renderDetails(id)); // detail img has view-transition-name: hero
}
```

When going back, set the name on the correct list item in the update callback before the new state is captured.

## 356: A dropdown animation stutters on low-end Android phones. How do you investigate?

1. Reproduce with Chrome remote debugging on a real device, or with CPU throttling in DevTools.
2. Record in the Performance panel and look at what each frame does: long JS tasks, style recalc, layout or paint.
3. Check which properties are animated. Replace `height`, `top` or `box-shadow` with `transform`, `opacity` or the grid trick.
4. Turn on paint flashing and layer borders to see repaint areas and layers.
5. Check for work started at the same moment, like rendering the dropdown's content or fetching data, and move it before or after the animation.

## 357: A hover animation flickers when the mouse is near the edge. Why, and how do you fix it?

If the hovered element itself moves or shrinks (like `translate` up or `scale` down), the mouse can end up outside it, which ends the hover, so it moves back under the mouse and the hover starts again. That loop is the flicker. Put the hover on a wrapper that doesn't move and animate a child.

```css
.card-wrap:hover .card {
  translate: 0 -8px;
}
```

## 358: An animation stutters only in its first few frames. What could cause that?

Often it's setup work at the start: the browser creating a new layer, painting it for the first time, decoding a large image, or loading a font. JavaScript that runs when the animation starts, like rendering new content, can also block those first frames. Fixes: prepare in advance with `will-change` shortly before, decode images ahead with `img.decode()`, render content before animating it, and keep start-up JavaScript light.

## 359: An element jumps at the end of its animation. What are the likely causes?

- The final keyframe doesn't match the element's normal styles, and there's no fill mode, so it snaps back.
- `will-change` or the layer is removed at the end, and the element snaps to whole pixels or gets re-rendered at a different resolution.
- A `transitionend` or `animationend` handler changes classes or layout at the end.
- An infinite animation's last keyframe doesn't match the first.

Check each by slowing the animation down in DevTools and watching the final frame.

## 360: A loading spinner freezes while the app does heavy work. How do you fix it?

First check what the spinner animates. If it's a CSS `rotate` or `transform` animation that the browser runs on the compositor, it keeps going during long tasks. If it uses JavaScript, an SVG attribute, or a `border` or `width` change, it freezes. Switch to a compositor-friendly animation. Then also fix the real problem: break the long task into smaller pieces, move it to a Web Worker, or yield with `scheduler.yield()` where supported.

## 361: What causes flicker with 3D transforms in Safari, and how do you fix it?

Common causes: an element flickers at the start or end of an animation because it moves in and out of its own layer, or two elements in 3D space cut through each other (z-fighting). Fixes that often help are keeping the element on its own layer for the whole animation (`will-change: transform`), setting `backface-visibility: hidden` where the back side isn't needed, and separating overlapping elements a little on the Z axis with `translateZ`. Test on real devices, because simulators don't always show it.

## 362: How do you animate items in a list of 1,000 elements without it being slow?

Don't animate all of them. Only animate the items that are visible, using virtualization or `content-visibility: auto` so off-screen items aren't rendered. Use `transform` and `opacity` so there's no layout. Avoid adding `will-change` to every item, which would create a thousand layers. If the whole list needs to move, animate one wrapper instead of every row.

## 363: How do you animate a sidebar that pushes the main content aside?

Animating the content's `margin-left` or the sidebar's `width` triggers layout for the whole page every frame. Options:

- Make the sidebar an overlay that slides in with `translate`, so content doesn't move.
- Animate `grid-template-columns`, which is still layout but often fine for one container.
- Use FLIP or a view transition: change the layout once and animate the visual change with transforms.

Pick based on how heavy the main content is.

## 364: Users report that your site makes them feel sick. What do you check?

Look for large movement: parallax, full-screen zooms, big slides between pages, auto-playing backgrounds, scroll-jacking and spinning elements. Check that all of them respect `prefers-reduced-motion`, including JavaScript and library animations, which ignore the media query unless you wire it up. Consider adding a motion toggle on the site, since not everyone knows about the OS setting. Keep small fades for feedback.

## 365: An animation works in Chrome but not in Safari. What do you check?

- Feature support: newer things like `interpolate-size`, `calc-size()`, `::details-content`, `sibling-index()` or some view transition features may not be in Safari yet.
- SVG differences, like `transform-box` and `transform-origin` defaults or animating `d`.
- 3D quirks with `preserve-3d` and `backface-visibility`.
- Low Power Mode on iOS, which can reduce frame rates.
- Whether reduced motion is turned on in that device's settings.

Then use `@supports` or feature detection for a fallback.

## 366: How can an entrance animation hurt Largest Contentful Paint?

LCP measures when the largest visible element is painted. If the hero image or heading starts at `opacity: 0` and fades in, it may not be counted until it's visible, and if the animation starts late or waits for JavaScript, LCP gets worse. Don't hide the main content behind an entrance animation; animate decoration, or start from a visible state like a small `translate` with full opacity.

## 367: Design wants all 50 product cards to fade in one after another on page load. What do you say?

It looks nice once, but the last cards appear after several seconds, which makes the page feel slow and can hurt LCP if a card image is the largest element. Suggest: only stagger the first few visible cards, cap the total stagger time (like 300-400 ms), animate others as they scroll into view, make sure content is visible without JavaScript, and skip it entirely for reduced motion.

## 368: What problems can animations cause with server rendering and hydration?

Server-rendered HTML is visible before JavaScript loads. CSS animations start right away, but animations started by JavaScript run only after hydration, so content may appear, then disappear and animate in again, which looks like a glitch. Also, if the hydrated DOM differs and elements are re-created, their CSS animations restart. Prefer CSS for entrance effects on server-rendered pages, and make the initial HTML already be in the correct starting state.

## 369: Why is hiding content until JavaScript adds an "animate-in" class risky?

If the CSS sets `opacity: 0` and only JavaScript makes it visible, then when JavaScript fails, loads slowly or is blocked, the content stays invisible. Search engines and some tools may also see it as hidden. Make the default visible and only hide-then-animate when you know JavaScript is running, for example with a `js` class added in the `<head>`, or use scroll-driven animations and `@starting-style`, which need no JavaScript.

## 370: Why can't you animate most styles on :visited links?

Browsers limit `:visited` styles to a few color properties, and they make `getComputedStyle` and other APIs behave as if the link wasn't visited. Otherwise a page could find out which sites you've been to, for example by timing how long a style takes to render. For the same reason, differences between visited and unvisited states don't create transitions you can detect from script.

## 371: How does Content Security Policy affect animations?

A strict `style-src` without `'unsafe-inline'` blocks `<style>` blocks and `style="..."` attributes in the HTML, including inline `--i` values for staggering and `setAttribute("style", ...)`. Setting styles through the CSSOM (`el.style.setProperty()`) and using `element.animate()` are allowed. So with a strict CSP, set per-element animation values from JavaScript through the CSSOM, or use nonces or hashes for style blocks.

## 372: Can you limit an animation to a lower frame rate on purpose?

With `steps()` you can make an animation update only a set number of times, which gives a choppy "stop motion" look. For example, `steps(12)` over one second shows 12 different states, even on a 120 Hz screen. Browsers don't let CSS set the real refresh rate. In JavaScript you can skip work in `requestAnimationFrame` until enough time has passed.

## 373: Why might animations in an iframe stop or slow down?

Browsers throttle iframes that are off-screen or hidden, especially cross-origin ones, by rendering them less often or not at all. Ads and embedded widgets may look frozen when you scroll back to them, and `requestAnimationFrame` won't fire there while throttled. Don't depend on precise timing inside iframes that may be off-screen.

## 374: Is it better to animate one parent or every child?

Usually one parent. Moving a whole group by animating the wrapper's `transform` means one layer and one animation. Animating 30 children with the same values creates 30 animations and maybe 30 layers. Animate children separately only when they really need different motion, like a stagger.

## 375: Are SVG animations as fast as HTML animations?

Not always. Transforms on elements inside an SVG are often not composited the same way as HTML elements, so they may repaint the SVG on every frame. For a large SVG, animating many inner parts can be heavy. If the whole SVG moves, wrap it in an HTML element and animate that. For complex SVG animations, test performance on a slow device.

## 376: When should you use canvas or WebGL instead of CSS animations?

When you have thousands of moving things (particles, data visualisations, games) or need per-pixel effects. Each animated DOM element has overhead for style and layers, while canvas draws everything in one surface from JavaScript, and WebGL uses the GPU directly. CSS is better for UI elements, accessibility and text, and canvas content needs extra work to be accessible.

## 377: How would you set up animation in a large application?

- Motion tokens for durations and easings, used everywhere.
- A clear rule about which tool to use: CSS transitions for state, keyframes for loops, the Web Animations API for interactive or sequenced motion, view transitions for page and layout changes.
- One central place that respects reduced motion, both in CSS and in a JS helper that libraries also use.
- Shared, tested patterns for common cases like modals, toasts and accordions.
- Performance rules: prefer `transform` and `opacity`, limit `will-change`, test on slow devices.

## 378: What kinds of motion are most likely to cause problems for people with vestibular disorders?

Large movements, especially across the screen or many elements at once; zooming and scaling of big areas; parallax, where layers move at different speeds; spinning; motion that's tied to scrolling and doesn't match the user's own scroll; and auto-playing backgrounds. Small, short changes like fades, color changes and small slides are usually much less of a problem.

## 379: Should you rely on the OS reduced motion setting or add an in-app setting?

Both. The OS setting is the default and should always be respected. But many people don't know it exists, or want motion everywhere except your site. An in-app toggle that overrides it (stored in a cookie or local storage, applied as a class or data attribute on `<html>`) gives control. Make sure CSS checks the class as well as the media query, and JavaScript animations check both too.

## 380: Why does a CSS animation restart when a React component re-renders with a new key?

A new `key` tells React to throw the old element away and create a new DOM element. A new element gets its animations from scratch, so they start again. You can use this on purpose to restart an animation (for example, change the key when a value updates). If it happens by accident, like keys based on an index in a changing list, items may animate again when they shouldn't.

## 381: How do you let users of a web component customize its animations?

Expose CSS custom properties for durations and easings, and use `::part()` for elements users may style directly. Define the component's own `@keyframes` inside its shadow root.

```css
/* inside the component */
.panel {
  transition: translate var(--drawer-duration, 250ms)
    var(--drawer-easing, ease-out);
}
```

```css
/* page using it */
my-drawer {
  --drawer-duration: 400ms;
}

my-drawer::part(panel) {
  box-shadow: 0 0 20px rgb(0 0 0 / 0.2);
}
```

Custom properties pass through the shadow boundary, so this works without breaking encapsulation.

## 382: Why is transitioning font-size on the html element a bad idea?

`font-size` inherits and affects every `rem` and `em` value on the page, so each frame the browser recalculates styles and layout for the whole document. That can be very heavy. If you want something to grow, animate `scale` on the element itself.

## 383: Why can animating a large blur be slow?

A blur's cost grows with the blur radius and the size of the area, because each output pixel mixes many input pixels. The GPU handles it, but a big radius on a full-screen element can still drop frames and use extra memory, especially on phones. Use a smaller radius, blur a smaller element, or blur a static image once and fade it in with `opacity`.

## 384: Why is backdrop-filter expensive to animate?

`backdrop-filter` has to read and filter whatever is behind the element every time that content or the element changes. Moving a blurred panel over a scrolling page means re-blurring the area behind it each frame. Avoid animating its value. If you must move the panel, keep it small and test on slow phones.

## 385: Does mix-blend-mode affect animation performance?

Yes. Blending needs the browser to combine the element with what's behind it, often in a separate group, which can create extra layers or prevent some optimizations. Animating an element with a blend mode on top of moving content can be slow. Use it in small areas and check paint and layer counts in DevTools.

## 386: Can clip-path or background-color animations run on the compositor?

Traditionally, no: they need a repaint every frame, so they run on the main thread. Browser vendors have worked on compositing some of these (for example, some `clip-path` and `background-color` animations in Chromium), but support depends on the browser, version and situation. Don't assume it; record a trace to see whether it causes paint on every frame.

## 387: How do you approach cross-browser animation bugs?

Make a minimal test case with only the animation. Check MDN and caniuse for the exact feature, and the Interop project's results for known differences. Test in Chrome, Firefox and Safari, including iOS Safari, which has its own quirks. Look for differences in defaults (SVG `transform-origin`), unsupported syntax silently ignored, and features behind flags. If it's a real browser bug, search the browser's bug tracker; there may be a known workaround.

## 388: What are the animation types in the CSS specs?

Each property says how it animates:

- "by computed value": interpolated using the type of its value (number, length, color...).
- "discrete": switches at 50% (or at the edge with `allow-discrete` for transitions).
- "repeatable list": lists are repeated to the same length and interpolated item by item (like `background-position`).
- "not animatable": ignored in keyframes and never transitions.
- Some properties have their own rules, like `visibility`, `transform` and `box-shadow`.

## 389: Which properties are not animatable at all?

The animation and transition properties themselves (`animation-*`, `transition-*`), `will-change`, `direction`, `unicode-bidi` and a few others. If you put them in `@keyframes`, they're ignored. That's also why you can't create an animation that changes its own `animation-duration` part way through.

## 390: What happens to percentage values in translate if the element changes size during the animation?

Percentages in `translate` refer to the element's own size, and they're recalculated every frame from the current size. If the element grows while the animation runs, the distance changes too. When running on the compositor, the browser has to sync again with the main thread, which can cause small jumps. Use fixed units if the size can change mid-animation.

## 391: How is animation-timing-function applied in a multi-keyframe animation?

In CSS, the timing function applies to each segment between two keyframes, not to the animation as a whole. So `animation: move 2s ease` with keyframes at 0%, 50% and 100% eases in and out twice: it slows down at 50%. The Web Animations API has both: per-keyframe `easing` like CSS, and an `easing` option in the timing that applies to the whole animation.

```js
el.animate(
  [{ translate: "0" }, { translate: "100px" }, { translate: "300px" }],
  { duration: 2000, easing: "ease-in-out" }, // one curve for the whole run
);
```

## 392: How do you make a multi-step CSS animation move at an even speed through all the keyframes?

Set the timing function to `linear` so each segment runs at constant speed, and place the keyframe percentages so that distance and time match. If you want one ease over the whole motion, either use only two keyframes, or use the Web Animations API with the whole-animation `easing` option.

## 393: How does steps() behave in a keyframe animation with several keyframes?

Like other timing functions, `steps(n)` applies to each segment. With three keyframes and `steps(4)`, you get 4 steps between 0% and 50%, and another 4 between 50% and 100%, not 4 total. For sprite sheets, keep just two keyframes and set `steps()` to the frame count.

## 394: How do you find animations running on a pseudo-element from JavaScript?

Use `getAnimations({ subtree: true })` on the element. Animations on `::before`, `::after` and other pseudo-elements are included, and their `effect.pseudoElement` tells you which one.

```js
const anims = el.getAnimations({ subtree: true });
const beforeAnims = anims.filter((a) => a.effect.pseudoElement === "::before");
```

## 395: Can element.animate() target a pseudo-element?

Yes, with the `pseudoElement` option. This is how you animate `::before`, `::after`, `::marker` or view transition pseudo-elements from JavaScript.

```js
document.documentElement.animate(
  { opacity: [0, 1] },
  { duration: 300, pseudoElement: "::view-transition-new(root)" },
);
```

The pseudo-element must exist, so for `::before` it needs `content` set.

## 396: How do you keep several animations in sync if they start at different times?

Give them the same `startTime` on the document timeline. Animations with the same start time and duration are at the same point in every frame.

```js
const anims = [...document.querySelectorAll(".pulse")].flatMap((el) =>
  el.getAnimations(),
);
const t = document.timeline.currentTime;
anims.forEach((a) => (a.startTime = t));
```

Or set `startTime = 0` so every animation lines up with the start of the document timeline.

## 397: Why do skeleton shimmers look out of sync, and how do you fix it?

Each skeleton starts its animation when it's rendered, so items added at different times have different phases and the shimmer looks random. Fixes: set the animations' `startTime` to the same value from JavaScript, give each one a negative `animation-delay` based on when it appeared, or use one shimmer with `background-attachment: fixed` so all skeletons show the same moving gradient.

## 398: How do you build a sequence of animations without group or sequence effects?

The Web Animations spec once proposed `GroupEffect` and `SequenceEffect`, but browsers didn't ship them. Use promises instead:

```js
async function intro() {
  await logo.animate({ opacity: [0, 1] }, 300).finished;
  await title.animate({ translate: ["0 20px", "0 0"] }, 300).finished;
  await Promise.all(
    buttons.map(
      (b, i) =>
        b.animate({ opacity: [0, 1] }, { duration: 200, delay: i * 50 })
          .finished,
    ),
  );
}
```

Or use a library with timelines when the sequence gets complex, so you can seek and reverse the whole thing.

## 399: Why can em or container query units change while an animation runs?

Values like `em`, `cqi` and `vw` are turned into pixels on each frame using the current font size, container size or viewport. If those change during the animation (a resize, a font loading, a container query kicking in), the animated distance changes too. It's usually what you want, but it can make animations jump or look inconsistent, and changes like these force the animation off the fast path.

## 400: What is the Long Animation Frames API?

It reports frames that took longer than 50 ms to render, with details on which scripts ran during them, how long style and layout took and what blocked the frame. It's useful for finding the cause of jank and slow interactions from real users, which the older Long Tasks API couldn't explain well.

```js
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    console.log(
      entry.duration,
      entry.scripts.map((s) => s.sourceURL),
    );
  }
}).observe({ type: "long-animation-frame", buffered: true });
```

It's supported in Chromium browsers.

## 401: How can you measure animation smoothness for real users?

There's no perfect API for dropped frames. Common approaches:

- The Long Animation Frames API to catch slow frames and their causes.
- INP to catch slow responses to input.
- A `requestAnimationFrame` loop that measures the time between frames during a specific animation, sending stats like "frames over 20 ms".

A rAF loop only measures the main thread, so it can miss compositor jank and add a bit of overhead. Turn it on only during the animations you care about.

## 402: How do you find out why an animation isn't running on the compositor?

Record the animation in Chrome's Performance panel. Animations show up in their own track, and Chrome often lists a reason when one couldn't be composited, such as an unsupported property or a transform that depends on the box size. If you see Paint or Layout events on every frame while it runs, it's on the main thread. Then check the Layers panel to confirm whether the element has its own layer.

## 403: What do you need to think about when building an auto-advancing carousel?

- A visible pause button (WCAG 2.2.2), and pausing on hover and when anything inside has keyboard focus.
- No auto-advance with reduced motion, or a much slower one.
- Pausing when the carousel is off-screen or the tab is hidden.
- Announcing slide changes politely, or not at all while auto-playing, so screen reader users aren't interrupted.
- Not making the first slide's image wait for JavaScript, so LCP isn't hurt.

Many teams decide not to auto-advance at all.

## 404: How would you build animated statistics that count up when they scroll into view?

Put the final number in the HTML so it's correct for search engines, screen readers and users without JavaScript. Use IntersectionObserver to start the count once, animate a registered integer property or update the text with `requestAnimationFrame` based on time, and use `tabular-nums` so the width doesn't jump. Skip the count and show the number directly for reduced motion. Mark the animated text `aria-hidden` and keep the real value accessible.

## 405: How do you swap a skeleton for real content without layout shift?

Make the skeleton the same size as the real content, using the same layout and fixed heights or `aspect-ratio` for images. When data arrives, replace it in place and fade the content in with `opacity`, not with a height change. If the real content is a different height than expected, the jump counts as a layout shift unless it happens right after user input.

## 406: How would you animate a product image from a listing page into a product page on a multi-page site?

Use cross-document view transitions. Turn them on in both pages with `@view-transition { navigation: auto; }`. On the listing page, set a `view-transition-name` on the clicked product's image in a `pageswap` handler (or on click). On the product page, give the main image the same name. Mark the image as render-blocking with `<link rel="expect">` if needed, fix aspect ratio stretching with `object-fit` on the pseudo-elements, and turn off the movement for reduced motion. Browsers without support just navigate normally.

## 407: An infinite animation uses a lot of CPU on some computers. Why?

If the browser can't use the GPU (old graphics drivers, a blocklisted GPU, remote desktop or a VM), it falls back to software rendering and compositing on the CPU. Even a simple `transform` animation then costs real CPU on every frame. Infinite animations make it worse because they never stop. Pause decorative loops when they're off-screen or after a while, and keep looping animations small.

## 408: Should you use Lottie or CSS for an animated logo?

CSS (with inline SVG) is best for simple motion: a few shapes moving, fading or drawing. It adds almost no size and is easy to control with reduced motion. Lottie plays animations exported from After Effects as JSON; it's good for complex illustrations made by designers, but the player library and the JSON add weight and it runs in JavaScript. Choose by complexity, and measure the size both ways.

## 409: How do you decide whether an animation library is worth its bundle size?

List what you actually need. If it's fades, slides, hovers and simple sequences, CSS and the Web Animations API cover it without extra code. A library makes sense for springs that follow gestures, complex timelines, layout animations in a framework, or SVG morphing. Check its size after tree shaking, whether you can load it only on pages that need it, and whether it respects reduced motion.

## 410: An animated tooltip gets cut off inside a scrolling container. How do you fix it?

`overflow: auto` or `hidden` on an ancestor clips anything that goes outside its box, including animated popups. Move the tooltip out of the container: use the `popover` attribute so it's in the top layer, or render it at the end of `<body>`. Position it with CSS anchor positioning or JavaScript. Animations then work without being clipped.

## 411: An exit animation works in one browser but the element just disappears in another. What's going on?

The CSS-only exit pattern depends on `transition-behavior: allow-discrete`, transitioning `display` and, for dialogs and popovers, `overlay`. A browser that doesn't support part of this removes the element immediately. Use `@supports` to check, or add a JavaScript fallback: on close, add a "closing" class, wait for the animation with `getAnimations()` and `finished`, then actually close or hide it.

## 412: Why do hover effects built with keyframe animations look worse than ones built with transitions?

A keyframe animation added on `:hover` restarts every time the hover starts, and when the hover ends it is removed and the element snaps back. Moving the mouse quickly in and out makes it jump. A transition starts from the current value both ways and can reverse halfway, so it handles quick in-and-out movement smoothly. Use transitions for states that can toggle quickly.

## 413: How do you avoid a spinner that flashes for a split second on fast loads?

Delay the spinner. If the content arrives within about 300 ms, it never appears; if loading is slower, it fades in.

```css
.spinner {
  opacity: 0;
  animation:
    show 200ms ease-out 300ms forwards,
    spin 800ms linear infinite;
}

@keyframes show {
  to {
    opacity: 1;
  }
}
```

Some teams also keep the spinner up for a minimum time once it's shown, so it doesn't flash away.

## 414: A mega menu animation makes interactions feel slow. How do you improve it?

Open the menu with a fast, compositor-friendly animation (`opacity` and `translate`), and make sure the first frame shows something within one frame of the hover or click. Don't render a big menu tree on open; render it ahead of time and hide it with `display: none` or `content-visibility`. Avoid layout animations on large containers. Then check INP in a performance trace with CPU throttling.

## 415: What do you look for when reviewing animation code?

- Does it animate `transform` and `opacity` where possible?
- Does it respect reduced motion, both in CSS and JavaScript?
- Is hidden content really hidden (not just `opacity: 0`)?
- Are durations and easings from shared tokens?
- Is `will-change` limited and removed when not needed?
- Does logic waiting for `transitionend` or `animationend` handle cancel and missing events?
- Are there infinite loops that should pause when off-screen?
- Does the page still work if the animation feature isn't supported?

## 416: Why can animating heights with ResizeObserver create loops?

If a ResizeObserver callback changes the size of an element it observes, it triggers itself again. Animating the height inside the callback causes a resize every frame, which calls the callback every frame. The browser stops the loop and logs "ResizeObserver loop completed with undelivered notifications". Observe an inner element that doesn't change because of the animation, or only start an animation when the target size changes.

## 417: How do you design animations that can be interrupted?

Users click again, close menus halfway or navigate during transitions. CSS transitions handle this well: a new target starts from the current value. Keyframe animations restart from the beginning, so they're worse for toggles. With the Web Animations API, keep a reference and `reverse()` the running animation, or start the new one from the current computed value. Never block user input until an animation is done.

## 418: Why can a transition that changes direction feel unnatural?

When a transition is interrupted, the new one starts from the current position but at zero speed, so the motion stops dead and then speeds up again. In the real world, things keep their speed and slow down. Spring animations in JavaScript libraries keep the current velocity when the target changes, which feels more natural for drags and quick toggles. For most UI, CSS transitions are good enough.

## 419: How do you animate an element after a drag is released?

During the drag, update `transform` directly from pointer events without any transition. On release, start an animation from the current position to the final one, using the drag's speed to choose the duration or the curve.

```js
function release(el, fromX, toX, velocity) {
  const distance = Math.abs(toX - fromX);
  const duration = Math.min(
    400,
    Math.max(150, distance / Math.max(Math.abs(velocity), 0.5)),
  );
  el.animate(
    [
      { transform: `translateX(${fromX}px)` },
      { transform: `translateX(${toX}px)` },
    ],
    {
      duration,
      easing: "cubic-bezier(0.2, 0.8, 0.2, 1)",
      fill: "forwards",
    },
  );
}
```

Velocity here is in pixels per millisecond, measured from the last few pointer moves.

## 420: What do you need for smooth gesture-driven animations on touch devices?

- `touch-action` (for example `touch-action: pan-y`) so the browser knows which gestures you handle and doesn't wait to see if the user scrolls.
- Pointer events with `setPointerCapture()` so you keep getting moves when the finger leaves the element.
- Only `transform` changes during the move, with transitions turned off.
- Batching updates in `requestAnimationFrame`.
- A release animation that starts from the current position.

## 421: How would you build swipe-to-dismiss for a notification?

Track the horizontal drag with pointer events and move the element with `translate`, maybe fading it as it goes. On release, if it moved past a threshold or the swipe was fast, animate it off-screen and then collapse its space and remove it. Otherwise animate it back to 0. Also provide a visible close button, since not everyone can or will swipe, and respect reduced motion for the fly-away.

## 422: Why might an animation measure the wrong sizes when it runs right on page load?

Fonts, images and late CSS may not be loaded yet, so the element's size can change after you measure it. A FLIP or height animation using those numbers then ends in the wrong place. Wait for what you depend on, such as `document.fonts.ready`, `img.decode()` or the `load` event, or measure again just before starting.

## 423: How do you handle animations in right-to-left layouts?

`translate` and `translateX` use physical directions, so a "slide in from the start" animation goes the wrong way in RTL languages. Flip the direction with a custom property set by `:dir(rtl)`:

```css
.drawer {
  --dir: 1;
  animation: slide-in 300ms ease-out;
}

.drawer:dir(rtl) {
  --dir: -1;
}

@keyframes slide-in {
  from {
    translate: calc(-100% * var(--dir)) 0;
  }
}
```

## 424: How do you place and animate items in a circle with CSS math functions?

Use `sin()` and `cos()` to compute positions from an angle. Animating a registered angle moves all items around the circle.

```css
@property --spin {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: true;
}

.ring {
  animation: ring 10s linear infinite;
}

.ring > .dot {
  --angle: calc(var(--i) * 45deg + var(--spin));
  translate: calc(cos(var(--angle)) * 100px) calc(sin(var(--angle)) * 100px);
}

@keyframes ring {
  to {
    --spin: 360deg;
  }
}
```

This runs on the main thread, so for a simple ring, rotating the parent is cheaper.

## 425: How should focus be handled during animated transitions?

Move focus to the new content at the right time, for example to the dialog when it opens and back to the trigger when it closes. Don't wait for the animation to finish before moving focus; keyboard users shouldn't wait. During exit animations, make the leaving content `inert` so it can't be focused or clicked. After a view transition, set focus on the main heading of the new view.

## 426: How do you test that reduced motion works?

Turn on "Emulate CSS prefers-reduced-motion" in Chrome DevTools' Rendering tab, or use the OS setting. In automated tests, use Playwright's `page.emulateMedia({ reducedMotion: "reduce" })` and check that animations are gone or shortened, for example by asserting on `el.getAnimations()` or computed `animation-name`. Also test JavaScript and library animations, which are easy to miss.

## 427: Is prefers-reduced-motion a privacy concern?

A little. Like other user preference media features, it can be read by any page and adds one bit to the data used for browser fingerprinting. It can also hint at a medical condition. Browsers decided the benefit is worth it. You should use the value only for motion, not for tracking or profiling.

## 428: How can CSS containment reduce the cost of animations?

`contain: layout paint` (or `contain: content`) on a container tells the browser that what happens inside doesn't affect layout or painting outside it. If something inside animates a layout property, the browser only needs to redo layout for that subtree instead of the whole page. It's a cheap win around widgets with layout animations, like an accordion inside a long page.

## 429: How can scroll event handlers hurt scroll-linked animations?

Scroll handlers run on the main thread after the compositor has already scrolled, so effects driven by them often lag one frame behind and stutter when the main thread is busy. Non-passive `wheel` or `touch` listeners can even block scrolling itself. Use scroll-driven animations where possible; otherwise use `{ passive: true }` and do the visual update in `requestAnimationFrame`.

## 430: Why does linear motion often look robotic?

Real objects don't start or stop instantly; they speed up and slow down. Constant speed with a sudden start and stop looks mechanical. That's why UI motion usually uses ease-out or custom curves. `linear` is right when the motion has no start or end, like spinners and marquees, or for opacity and color fades, where speed changes are hard to notice.

## 431: How do animations affect perceived performance?

A skeleton or a smooth transition can make waiting feel shorter than a blank screen, because the user sees progress and the change isn't abrupt. But animations that run before content can be used make the app feel slower, even if the data was fast. Animate around waiting, never add waiting for animation, and keep transitions short on frequent actions.

## 432: How do animations work with optimistic UI updates?

You show the result right away (like adding a comment) before the server confirms. A subtle animation, like a fade in with lower opacity while pending, shows it's not saved yet. If the request fails, animate the item out or show an error. Make sure the animation can be reversed in the middle, since the failure can come back while it's still running.

## 433: Why do all the cards fade in when the page loads after adding @starting-style?

`@starting-style` applies the first time an element is rendered, and that includes the initial page load. So a rule meant for "new items added later" also animates every item on first render. If you only want it for later additions, scope it with a class added after load (like `.ready .item`) or only add the transition to items inserted dynamically.

## 434: What happens to animations when an element is moved in the DOM?

Removing an element and inserting it somewhere else (like `append()` to a new parent) counts as a new element for rendering: running CSS animations and transitions restart, and `@starting-style` applies again. Iframes reload and videos may reset too. Chromium has a newer `moveBefore()` method that keeps this state when moving elements; check support before relying on it.

## 435: How do you coordinate animations between components that don't know about each other?

Use a shared state on a common ancestor: a data attribute like `data-state="closing"` or a custom property, and let each component's CSS react to it. For JavaScript sequencing, dispatch custom events and let components return promises of their animations. View transitions can also coordinate a whole page change without the components talking to each other.

## 436: Should animation states be driven by classes or data attributes?

Both work. Data attributes like `data-state="open"` hold one value at a time, so you can't end up with both `.open` and `.closing` on the element. ARIA attributes such as `aria-expanded` are even better when they exist, because the visual and accessible states can't drift apart. Classes are fine for simple on and off states.

## 437: How do you animate theme changes across a whole design system?

Register the theme tokens that should animate as `<color>` with `@property` and `inherits: true`, and transition them on the root. Be careful: every element that uses them recalculates on each frame. For big pages, a single view transition cross-fade between themes is cheaper and looks cleaner than hundreds of color transitions.

## 438: How would you build an accessible modal with open and close animations?

Use a native `<dialog>` with `showModal()`, which handles the top layer, focus trapping and Escape. Animate it with `@starting-style`, `opacity` and `translate`, plus `display` and `overlay` with `allow-discrete` for the exit, and the same for `::backdrop`. Return focus to the trigger on close. Wrap the movement in a reduced motion check and keep a short fade. In browsers without exit support, it still closes, just without the animation.

## 439: How would you build a carousel with scroll snap and animated indicators?

Make a horizontal scroll container with `scroll-snap-type: x mandatory` and `scroll-snap-align` on each slide, so swiping and keyboard scrolling work natively. Use a scroll timeline (`scroll-timeline-name` and `timeline-scope`) to animate a progress indicator, and view timelines on slides to scale or fade them. Previous and next buttons call `scrollBy({ left: ..., behavior: "smooth" })`, turned to `auto` for reduced motion.

## 440: Why is "transition: all 0.3s" on every element a bad idea in a large app?

It animates any property change on any element: layout changes from media queries, theme switches, `width` changes from JavaScript, and new values from framework updates. That creates unexpected motion, extra main-thread work and timing bugs in code that measures elements right after changing them. It also makes `transitionend` fire for properties you didn't care about. List specific properties on specific components.

## 441: How do you animate a list when it's sorted?

Sorting changes the DOM order, so items jump. Two good options:

1. View transitions: give each item a unique `view-transition-name` (or `match-element`) and wrap the sort in `startViewTransition()`.
2. FLIP: record each item's position, reorder the DOM, then animate each item's `transform` from its old position to the new one.

View transitions need less code; FLIP keeps items live and interactive during the animation.

## 442: Why does an animation run twice in a React app during development?

React's Strict Mode in development mounts components, unmounts them and mounts them again to find side-effect bugs. An effect that calls `element.animate()` runs twice, and CSS animations restart because elements are created again. Return a cleanup that cancels the animation from the effect. In production the extra mount doesn't happen, but the cleanup is still correct.

```jsx
useEffect(() => {
  const anim = ref.current.animate({ opacity: [0, 1] }, 300);
  return () => anim.cancel();
}, []);
```

## 443: How do you handle a toggle that the user clicks quickly many times?

Don't start a new animation on every click. Keep a reference to the current one and reverse it.

```js
let anim;

toggle.addEventListener("click", () => {
  if (anim && anim.playState === "running") {
    panel.classList.toggle("open");
    anim.reverse(); // go back from where it is now
    return;
  }
  const opening = !panel.classList.contains("open");
  panel.classList.toggle("open", opening);
  anim = panel.animate(
    { opacity: opening ? [0, 1] : [1, 0] },
    { duration: 200, fill: "both" },
  );
});
```

Or use a CSS transition, which handles quick toggles for free.

## 444: How do you choose between a CSS transition, a keyframe animation, the Web Animations API, a view transition and a scroll-driven animation?

- A state change between two values (hover, open, selected): CSS transition.
- Something that plays on its own, loops or has several steps: keyframe animation.
- Motion that depends on runtime values, has to be paused, reversed or sequenced, or follows a gesture: the Web Animations API.
- Layout or page changes where elements move between places or appear and disappear: view transition.
- Effects that follow scroll position: scroll-driven animation.

Start with the simplest one that does the job.

## 445: What new animation features are worth watching?

At the time of writing, several features are being worked on or are only in some browsers: scroll-triggered animations in CSS, nested view transition groups and view transitions scoped to one element, `interpolate-size` and `calc-size()` outside Chromium, `sibling-index()` in all browsers, and composited animation of more properties. Check MDN, caniuse and the yearly Interop project to see what's ready before you use them.

## 446: How do you keep an animated SVG icon crisp at any size?

Use inline SVG with a `viewBox` and animate SVG properties or CSS transforms on its parts, instead of scaling a raster image. Use `vector-effect: non-scaling-stroke` if line widths should stay the same when the icon scales. If you scale the whole icon with `transform` during an animation, it may look slightly blurry until the browser repaints it at the end.

## 447: How do you make a CSS animation pause when the user switches tabs and continue later?

Browsers already stop rendering frames in hidden tabs, but the timeline keeps moving, so a finite animation jumps to its end. If you need it to continue from where it stopped, pause it on `visibilitychange`:

```js
document.addEventListener("visibilitychange", () => {
  const hidden = document.visibilityState === "hidden";
  for (const a of document.getAnimations()) {
    hidden ? a.pause() : a.play();
  }
});
```

Be careful not to resume animations that were paused on purpose.

## 448: An animation is only slow when DevTools is open. Should you worry?

Maybe not. Open DevTools, especially with the Elements panel showing live style changes or with paint flashing on, adds overhead. Close DevTools and test again, or use remote debugging on another device. Use the Performance panel's recording, which tells you more than eyeballing. Still check with CPU throttling, because users on slow phones have less power than your laptop even without DevTools.

## 449: What are the risks of animating layout in a component library used by many apps?

Each app has different page sizes, nesting and content. A layout animation that's cheap in your demo can be slow in a page with thousands of elements, because layout may spread up the tree. Library animations also get stacked with the app's own. Prefer `transform`- and `opacity`-based effects in shared components, use containment, expose duration tokens and a way to turn motion off, and respect reduced motion by default.

## 450: In one minute, how would you explain to an interviewer what makes a good CSS animation?

It has a purpose: it explains a change, gives feedback or shows where something came from. It's short, usually under 400 ms for UI. It uses easing that matches the action, like ease-out for things coming in. It animates cheap properties, mostly `transform` and `opacity`, so it stays smooth on slow devices. It can be interrupted. It respects reduced motion and never hides content when the animation doesn't run. And it's consistent with the rest of the product through shared tokens.
