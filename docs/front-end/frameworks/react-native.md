# React Native Interview Questions and Answers

_Last updated: October 28, 2026_

450 React Native interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced. The answers are based on React Native 0.88 (October 2026) with React 19 and the New Architecture, and on Expo SDK 58. They use the current APIs: Fabric, Turbo Modules, Hermes V1, React Native DevTools, Expo Router and the Strict TypeScript API. Older APIs like the bridge, the Touchable components and `SafeAreaView` from core are mentioned where you will still meet them in real projects.

If you spot a mistake or something that is out of date, feel free to open an issue or a pull request.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is React Native?](#1-what-is-react-native)
- [2: What is the difference between React and React Native?](#2-what-is-the-difference-between-react-and-react-native)
- [3: Who maintains React Native today?](#3-who-maintains-react-native-today)
- [4: Which platforms can you build for with React Native?](#4-which-platforms-can-you-build-for-with-react-native)
- [5: Is a React Native app a native app or a web view?](#5-is-a-react-native-app-a-native-app-or-a-web-view)
- [6: What are the main advantages of React Native?](#6-what-are-the-main-advantages-of-react-native)
- [7: What are the downsides or limitations of React Native?](#7-what-are-the-downsides-or-limitations-of-react-native)
- [8: How does React Native compare to Flutter?](#8-how-does-react-native-compare-to-flutter)
- [9: When would you choose fully native development instead of React Native?](#9-when-would-you-choose-fully-native-development-instead-of-react-native)
- [10: How do you create a new React Native project?](#10-how-do-you-create-a-new-react-native-project)
- [11: What is Expo?](#11-what-is-expo)
- [12: Why do the React Native docs recommend using a framework?](#12-why-do-the-react-native-docs-recommend-using-a-framework)
- [13: What is the difference between Expo Go and a development build?](#13-what-is-the-difference-between-expo-go-and-a-development-build)
- [14: What is Metro?](#14-what-is-metro)
- [15: What is Hermes?](#15-what-is-hermes)
- [16: How often is React Native released?](#16-how-often-is-react-native-released)
- [17: Which languages do you use in a React Native project?](#17-which-languages-do-you-use-in-a-react-native-project)
- [18: Does React Native support TypeScript?](#18-does-react-native-support-typescript)
- [19: What are the core components of React Native?](#19-what-are-the-core-components-of-react-native)
- [20: What is the View component?](#20-what-is-the-view-component)
- [21: Why must all text be inside a Text component?](#21-why-must-all-text-be-inside-a-text-component)
- [22: How do you show an image?](#22-how-do-you-show-an-image)
- [23: What is the TextInput component?](#23-what-is-the-textinput-component)
- [24: What is the ScrollView component?](#24-what-is-the-scrollview-component)
- [25: What is the Button component and why is it rarely used?](#25-what-is-the-button-component-and-why-is-it-rarely-used)
- [26: What is Pressable?](#26-what-is-pressable)
- [27: What are the Touchable components?](#27-what-are-the-touchable-components)
- [28: How does styling work in React Native?](#28-how-does-styling-work-in-react-native)
- [29: What does StyleSheet.create do?](#29-what-does-stylesheetcreate-do)
- [30: What units does React Native use for sizes?](#30-what-units-does-react-native-use-for-sizes)
- [31: How is Flexbox in React Native different from Flexbox on the web?](#31-how-is-flexbox-in-react-native-different-from-flexbox-on-the-web)
- [32: What does flex: 1 mean?](#32-what-does-flex-1-mean)
- [33: What is the difference between justifyContent and alignItems?](#33-what-is-the-difference-between-justifycontent-and-alignitems)
- [34: How do you add space between items?](#34-how-do-you-add-space-between-items)
- [35: How does absolute positioning work?](#35-how-does-absolute-positioning-work)
- [36: How do you combine multiple styles on one component?](#36-how-do-you-combine-multiple-styles-on-one-component)
- [37: Do styles inherit in React Native?](#37-do-styles-inherit-in-react-native)
- [38: How do you use custom fonts?](#38-how-do-you-use-custom-fonts)
- [39: How do you render a list of items?](#39-how-do-you-render-a-list-of-items)
- [40: What is FlatList and why use it?](#40-what-is-flatlist-and-why-use-it)
- [41: What is keyExtractor in FlatList?](#41-what-is-keyextractor-in-flatlist)
- [42: What is SectionList?](#42-what-is-sectionlist)
- [43: How do you show a message when a list is empty?](#43-how-do-you-show-a-message-when-a-list-is-empty)
- [44: How do you add pull to refresh?](#44-how-do-you-add-pull-to-refresh)
- [45: How do you load more items when the user reaches the end of a list?](#45-how-do-you-load-more-items-when-the-user-reaches-the-end-of-a-list)
- [46: What is the Platform module?](#46-what-is-the-platform-module)
- [47: How do you write platform-specific files?](#47-how-do-you-write-platform-specific-files)
- [48: What is the difference between Dimensions and useWindowDimensions?](#48-what-is-the-difference-between-dimensions-and-usewindowdimensions)
- [49: How do you handle the notch and other safe areas?](#49-how-do-you-handle-the-notch-and-other-safe-areas)
- [50: What does the StatusBar component do?](#50-what-does-the-statusbar-component-do)
- [51: How do you control how an image fits its box?](#51-how-do-you-control-how-an-image-fits-its-box)
- [52: How do you put text on top of an image?](#52-how-do-you-put-text-on-top-of-an-image)
- [53: How do you show a loading spinner?](#53-how-do-you-show-a-loading-spinner)
- [54: What is the Switch component?](#54-what-is-the-switch-component)
- [55: How do you show a modal?](#55-how-do-you-show-a-modal)
- [56: How do you show a native alert dialog?](#56-how-do-you-show-a-native-alert-dialog)
- [57: What is KeyboardAvoidingView?](#57-what-is-keyboardavoidingview)
- [58: How do you close the keyboard?](#58-how-do-you-close-the-keyboard)
- [59: How do you show a password field or a number keyboard?](#59-how-do-you-show-a-password-field-or-a-number-keyboard)
- [60: What is the difference between onChangeText and onChange on TextInput?](#60-what-is-the-difference-between-onchangetext-and-onchange-on-textinput)
- [61: How do you open a URL, phone number or email from the app?](#61-how-do-you-open-a-url-phone-number-or-email-from-the-app)
- [62: Do React hooks work the same in React Native?](#62-do-react-hooks-work-the-same-in-react-native)
- [63: How do you focus a TextInput from code?](#63-how-do-you-focus-a-textinput-from-code)
- [64: What is AppRegistry?](#64-what-is-appregistry)
- [65: What is the entry point of a React Native app?](#65-what-is-the-entry-point-of-a-react-native-app)
- [66: What is Fast Refresh?](#66-what-is-fast-refresh)
- [67: How do you open the developer menu?](#67-how-do-you-open-the-developer-menu)
- [68: What is React Native DevTools?](#68-what-is-react-native-devtools)
- [69: Where do console.log messages appear?](#69-where-do-consolelog-messages-appear)
- [70: What is LogBox?](#70-what-is-logbox)
- [71: How do you run the app on a simulator or emulator?](#71-how-do-you-run-the-app-on-a-simulator-or-emulator)
- [72: How do you run the app on a physical device?](#72-how-do-you-run-the-app-on-a-physical-device)
- [73: Why do you need Xcode and Android Studio?](#73-why-do-you-need-xcode-and-android-studio)
- [74: What is CocoaPods and why do you run pod install?](#74-what-is-cocoapods-and-why-do-you-run-pod-install)
- [75: What is Gradle in a React Native project?](#75-what-is-gradle-in-a-react-native-project)
- [76: What are the ios and android folders?](#76-what-are-the-ios-and-android-folders)
- [77: What is app.json or app.config.js in Expo?](#77-what-is-appjson-or-appconfigjs-in-expo)
- [78: What is Expo prebuild (Continuous Native Generation)?](#78-what-is-expo-prebuild-continuous-native-generation)
- [79: What options do you have for navigation in React Native?](#79-what-options-do-you-have-for-navigation-in-react-native)
- [80: How do you create a stack navigator with React Navigation?](#80-how-do-you-create-a-stack-navigator-with-react-navigation)
- [81: How do you navigate between screens and pass parameters?](#81-how-do-you-navigate-between-screens-and-pass-parameters)
- [82: What is a tab navigator?](#82-what-is-a-tab-navigator)
- [83: What is a drawer navigator?](#83-what-is-a-drawer-navigator)
- [84: What is Expo Router?](#84-what-is-expo-router)
- [85: How do you fetch data from an API in React Native?](#85-how-do-you-fetch-data-from-an-api-in-react-native)
- [86: Can you use axios, WebSockets and XMLHttpRequest in React Native?](#86-can-you-use-axios-websockets-and-xmlhttprequest-in-react-native)
- [87: How do you show loading and error states for a request?](#87-how-do-you-show-loading-and-error-states-for-a-request)
- [88: What is AsyncStorage?](#88-what-is-asyncstorage)
- [89: How do you store sensitive data like tokens?](#89-how-do-you-store-sensitive-data-like-tokens)
- [90: Which state management options are common in React Native?](#90-which-state-management-options-are-common-in-react-native)
- [91: How do you use Context in React Native?](#91-how-do-you-use-context-in-react-native)
- [92: What was the "bridge" in React Native?](#92-what-was-the-bridge-in-react-native)
- [93: What is the New Architecture?](#93-what-is-the-new-architecture)
- [94: Can you still use the old architecture?](#94-can-you-still-use-the-old-architecture)
- [95: What is a native module?](#95-what-is-a-native-module)
- [96: What is a native component?](#96-what-is-a-native-component)
- [97: What is autolinking?](#97-what-is-autolinking)
- [98: How do you install a library in an Expo project?](#98-how-do-you-install-a-library-in-an-expo-project)
- [99: How do you add a ripple effect on Android?](#99-how-do-you-add-a-ripple-effect-on-android)
- [100: What is hitSlop?](#100-what-is-hitslop)
- [101: How do you make a component accessible to screen readers?](#101-how-do-you-make-a-component-accessible-to-screen-readers)
- [102: What are the role and aria-* props in React Native?](#102-what-are-the-role-and-aria--props-in-react-native)
- [103: How do you support dark mode?](#103-how-do-you-support-dark-mode)
- [104: What is the Appearance API?](#104-what-is-the-appearance-api)
- [105: What is AppState?](#105-what-is-appstate)
- [106: How do you handle the Android back button?](#106-how-do-you-handle-the-android-back-button)
- [107: How do you open the native share sheet?](#107-how-do-you-open-the-native-share-sheet)
- [108: What is PixelRatio?](#108-what-is-pixelratio)
- [109: How do you do animations in React Native?](#109-how-do-you-do-animations-in-react-native)
- [110: What does useNativeDriver do?](#110-what-does-usenativedriver-do)
- [111: What is LayoutAnimation?](#111-what-is-layoutanimation)
- [112: What is Reanimated?](#112-what-is-reanimated)
- [113: What is React Native Gesture Handler?](#113-what-is-react-native-gesture-handler)
- [114: How do you use icons in React Native?](#114-how-do-you-use-icons-in-react-native)
- [115: How do you render SVG in React Native?](#115-how-do-you-render-svg-in-react-native)
- [116: How do you use environment variables in React Native?](#116-how-do-you-use-environment-variables-in-react-native)
- [117: What is `__DEV__`?](#117-what-is-__dev__)
- [118: What is the difference between a debug build and a release build?](#118-what-is-the-difference-between-a-debug-build-and-a-release-build)
- [119: What is the difference between an APK and an AAB?](#119-what-is-the-difference-between-an-apk-and-an-aab)
- [120: How do you publish an iOS app?](#120-how-do-you-publish-an-ios-app)
- [121: What is code signing?](#121-what-is-code-signing)
- [122: How do you set the app icon and splash screen?](#122-how-do-you-set-the-app-icon-and-splash-screen)
- [123: How do permissions work in a React Native app?](#123-how-do-permissions-work-in-a-react-native-app)
- [124: How do you use device features like the camera or location?](#124-how-do-you-use-device-features-like-the-camera-or-location)
- [125: How do push notifications work in a React Native app?](#125-how-do-push-notifications-work-in-a-react-native-app)
- [126: What are over-the-air (OTA) updates?](#126-what-are-over-the-air-ota-updates)
- [127: What is EAS?](#127-what-is-eas)
- [128: How do you set up Jest for a React Native project?](#128-how-do-you-set-up-jest-for-a-react-native-project)
- [129: What is React Native Testing Library?](#129-what-is-react-native-testing-library)
- [130: Which tools are used for end-to-end testing in React Native?](#130-which-tools-are-used-for-end-to-end-testing-in-react-native)
- [131: How do you set up linting and formatting?](#131-how-do-you-set-up-linting-and-formatting)
- [132: How do you limit text to a certain number of lines?](#132-how-do-you-limit-text-to-a-certain-number-of-lines)
- [133: Can you make part of a Text pressable?](#133-can-you-make-part-of-a-text-pressable)
- [134: How do you make a horizontal or paging ScrollView?](#134-how-do-you-make-a-horizontal-or-paging-scrollview)
- [135: When should you use ScrollView and when FlatList?](#135-when-should-you-use-scrollview-and-when-flatlist)
- [136: What is the difference between style and contentContainerStyle on a ScrollView?](#136-what-is-the-difference-between-style-and-contentcontainerstyle-on-a-scrollview)
- [137: What is expo-image and why use it instead of Image?](#137-what-is-expo-image-and-why-use-it-instead-of-image)
- [138: What is React Native Web?](#138-what-is-react-native-web)
- [139: How do you upgrade React Native to a new version?](#139-how-do-you-upgrade-react-native-to-a-new-version)
- [140: Why are keys important in lists?](#140-why-are-keys-important-in-lists)
- [141: Which web APIs are available in React Native?](#141-which-web-apis-are-available-in-react-native)
- [142: What is Yoga?](#142-what-is-yoga)
- [143: How do you add shadows?](#143-how-do-you-add-shadows)
- [144: What is the JavaScript bundle?](#144-what-is-the-javascript-bundle)
- [145: How do you use transforms like rotate and scale?](#145-how-do-you-use-transforms-like-rotate-and-scale)
- [146: How do you provide images for different screen densities?](#146-how-do-you-provide-images-for-different-screen-densities)
- [147: How do you choose a third-party library for React Native?](#147-how-do-you-choose-a-third-party-library-for-react-native)
- [148: What is the difference between margin and padding in React Native?](#148-what-is-the-difference-between-margin-and-padding-in-react-native)
- [149: How does the app load JavaScript during development?](#149-how-does-the-app-load-javascript-during-development)
- [150: How do you check that your environment and project are set up correctly?](#150-how-do-you-check-that-your-environment-and-project-are-set-up-correctly)

### Moderate Questions (151-300)

- [151: Which threads does a React Native app use?](#151-which-threads-does-a-react-native-app-use)
- [152: What does "60 FPS" mean and why does it matter?](#152-what-does-60-fps-mean-and-why-does-it-matter)
- [153: How do you make a FlatList faster?](#153-how-do-you-make-a-flatlist-faster)
- [154: What is getItemLayout and when should you use it?](#154-what-is-getitemlayout-and-when-should-you-use-it)
- [155: What do windowSize, initialNumToRender and maxToRenderPerBatch do?](#155-what-do-windowsize-initialnumtorender-and-maxtorenderperbatch-do)
- [156: What is FlashList?](#156-what-is-flashlist)
- [157: Does the React Compiler work with React Native?](#157-does-the-react-compiler-work-with-react-native)
- [158: How do you handle forms in React Native?](#158-how-do-you-handle-forms-in-react-native)
- [159: How do you validate forms with a schema?](#159-how-do-you-validate-forms-with-a-schema)
- [160: How do you move focus between inputs and control what the return key does?](#160-how-do-you-move-focus-between-inputs-and-control-what-the-return-key-does)
- [161: How do you support password managers and SMS code autofill?](#161-how-do-you-support-password-managers-and-sms-code-autofill)
- [162: How do you type navigation params in React Navigation?](#162-how-do-you-type-navigation-params-in-react-navigation)
- [163: What are nested navigators?](#163-what-are-nested-navigators)
- [164: How do you build an authentication flow with React Navigation?](#164-how-do-you-build-an-authentication-flow-with-react-navigation)
- [165: How do you protect routes in Expo Router?](#165-how-do-you-protect-routes-in-expo-router)
- [166: How do you configure deep linking in React Navigation?](#166-how-do-you-configure-deep-linking-in-react-navigation)
- [167: What is the difference between a custom URL scheme and universal links / app links?](#167-what-is-the-difference-between-a-custom-url-scheme-and-universal-links--app-links)
- [168: How do layouts, groups and dynamic routes work in Expo Router?](#168-how-do-layouts-groups-and-dynamic-routes-work-in-expo-router)
- [169: How do you run code when a screen comes into focus?](#169-how-do-you-run-code-when-a-screen-comes-into-focus)
- [170: How do you customize the header of a screen?](#170-how-do-you-customize-the-header-of-a-screen)
- [171: How do you show a screen as a modal in a navigator?](#171-how-do-you-show-a-screen-as-a-modal-in-a-navigator)
- [172: What is the difference between the native stack and the JS stack navigator?](#172-what-is-the-difference-between-the-native-stack-and-the-js-stack-navigator)
- [173: How do you use TanStack Query in React Native?](#173-how-do-you-use-tanstack-query-in-react-native)
- [174: How do you detect if the device is online?](#174-how-do-you-detect-if-the-device-is-online)
- [175: What does "offline-first" mean in a mobile app?](#175-what-does-offline-first-mean-in-a-mobile-app)
- [176: Which local databases are used in React Native?](#176-which-local-databases-are-used-in-react-native)
- [177: What is MMKV and how is it different from AsyncStorage?](#177-what-is-mmkv-and-how-is-it-different-from-asyncstorage)
- [178: How do you persist Zustand state in React Native?](#178-how-do-you-persist-zustand-state-in-react-native)
- [179: How do you use Redux Toolkit with persistence in React Native?](#179-how-do-you-use-redux-toolkit-with-persistence-in-react-native)
- [180: How do you have different configs for development, staging and production?](#180-how-do-you-have-different-configs-for-development-staging-and-production)
- [181: What is an Expo config plugin?](#181-what-is-an-expo-config-plugin)
- [182: What is eas.json?](#182-what-is-easjson)
- [183: How do channels, branches and runtime versions work in EAS Update?](#183-how-do-channels-branches-and-runtime-versions-work-in-eas-update)
- [184: What can't you change with an OTA update?](#184-what-cant-you-change-with-an-ota-update)
- [185: Are OTA updates allowed by Apple and Google?](#185-are-ota-updates-allowed-by-apple-and-google)
- [186: How do you set up push notifications with expo-notifications?](#186-how-do-you-set-up-push-notifications-with-expo-notifications)
- [187: How do you handle the user tapping a notification?](#187-how-do-you-handle-the-user-tapping-a-notification)
- [188: How do you run tasks in the background?](#188-how-do-you-run-tasks-in-the-background)
- [189: What is a good flow for asking for permissions?](#189-what-is-a-good-flow-for-asking-for-permissions)
- [190: How do you track the user's location while they move?](#190-how-do-you-track-the-users-location-while-they-move)
- [191: Which libraries do you use for the camera?](#191-which-libraries-do-you-use-for-the-camera)
- [192: How do you read and write files?](#192-how-do-you-read-and-write-files)
- [193: How do you upload a file or image to a server?](#193-how-do-you-upload-a-file-or-image-to-a-server)
- [194: How do you show web content inside a React Native app?](#194-how-do-you-show-web-content-inside-a-react-native-app)
- [195: What is interpolation in the Animated API?](#195-what-is-interpolation-in-the-animated-api)
- [196: How do you combine animations with the Animated API?](#196-how-do-you-combine-animations-with-the-animated-api)
- [197: How do you animate something based on scroll position?](#197-how-do-you-animate-something-based-on-scroll-position)
- [198: What are shared values and useAnimatedStyle in Reanimated?](#198-what-are-shared-values-and-useanimatedstyle-in-reanimated)
- [199: What are CSS animations and transitions in Reanimated 4?](#199-what-are-css-animations-and-transitions-in-reanimated-4)
- [200: What is a worklet?](#200-what-is-a-worklet)
- [201: How do you build a draggable element with Gesture Handler and Reanimated?](#201-how-do-you-build-a-draggable-element-with-gesture-handler-and-reanimated)
- [202: What are layout animations in Reanimated?](#202-what-are-layout-animations-in-reanimated)
- [203: How do you make a layout work on phones and tablets?](#203-how-do-you-make-a-layout-work-on-phones-and-tablets)
- [204: How do you deal with the user's font size settings?](#204-how-do-you-deal-with-the-users-font-size-settings)
- [205: What are common styling differences between iOS and Android?](#205-what-are-common-styling-differences-between-ios-and-android)
- [206: What is edge-to-edge on Android and how does it affect React Native apps?](#206-what-is-edge-to-edge-on-android-and-how-does-it-affect-react-native-apps)
- [207: When should you use useSafeAreaInsets instead of SafeAreaView?](#207-when-should-you-use-usesafeareainsets-instead-of-safeareaview)
- [208: How do you build a theme system in React Native?](#208-how-do-you-build-a-theme-system-in-react-native)
- [209: How do you translate an app and support right-to-left languages?](#209-how-do-you-translate-an-app-and-support-right-to-left-languages)
- [210: How do you tell a screen reader about the state of an element?](#210-how-do-you-tell-a-screen-reader-about-the-state-of-an-element)
- [211: What is AccessibilityInfo used for?](#211-what-is-accessibilityinfo-used-for)
- [212: How do error boundaries work in React Native?](#212-how-do-error-boundaries-work-in-react-native)
- [213: How do you catch errors that are not caught anywhere else?](#213-how-do-you-catch-errors-that-are-not-caught-anywhere-else)
- [214: How do you set up crash reporting?](#214-how-do-you-set-up-crash-reporting)
- [215: How do you debug JavaScript with React Native DevTools?](#215-how-do-you-debug-javascript-with-react-native-devtools)
- [216: How do you inspect network requests?](#216-how-do-you-inspect-network-requests)
- [217: How do you debug a native crash?](#217-how-do-you-debug-a-native-crash)
- [218: Which adb commands are useful for React Native development?](#218-which-adb-commands-are-useful-for-react-native-development)
- [219: What can you customize in the Metro config?](#219-what-can-you-customize-in-the-metro-config)
- [220: How do you set up path aliases like @/components?](#220-how-do-you-set-up-path-aliases-like-components)
- [221: How do you set up a React Native app in a monorepo?](#221-how-do-you-set-up-a-react-native-app-in-a-monorepo)
- [222: How do you build a signed Android release?](#222-how-do-you-build-a-signed-android-release)
- [223: What are certificates and provisioning profiles on iOS?](#223-what-are-certificates-and-provisioning-profiles-on-ios)
- [224: How do app versions and build numbers work?](#224-how-do-app-versions-and-build-numbers-work)
- [225: How do you reduce the size of the app?](#225-how-do-you-reduce-the-size-of-the-app)
- [226: How do you improve app startup time?](#226-how-do-you-improve-app-startup-time)
- [227: Which queries should you prefer in React Native Testing Library?](#227-which-queries-should-you-prefer-in-react-native-testing-library)
- [228: How do you simulate user actions in React Native Testing Library?](#228-how-do-you-simulate-user-actions-in-react-native-testing-library)
- [229: How do you mock a native module in Jest?](#229-how-do-you-mock-a-native-module-in-jest)
- [230: How do you test components that use navigation?](#230-how-do-you-test-components-that-use-navigation)
- [231: Are snapshot tests useful in React Native?](#231-are-snapshot-tests-useful-in-react-native)
- [232: What is the difference between Detox and Maestro?](#232-what-is-the-difference-between-detox-and-maestro)
- [233: How do you mock API calls in tests?](#233-how-do-you-mock-api-calls-in-tests)
- [234: How do you set up CI/CD for a React Native app?](#234-how-do-you-set-up-cicd-for-a-react-native-app)
- [235: What is Fastlane?](#235-what-is-fastlane)
- [236: What is the Strict TypeScript API in React Native?](#236-what-is-the-strict-typescript-api-in-react-native)
- [237: How do you type the style prop of a reusable component?](#237-how-do-you-type-the-style-prop-of-a-reusable-component)
- [238: What can you do with a ref to a native component?](#238-what-can-you-do-with-a-ref-to-a-native-component)
- [239: How do you get the position and size of a view on screen?](#239-how-do-you-get-the-position-and-size-of-a-view-on-screen)
- [240: What is onLayout?](#240-what-is-onlayout)
- [241: How does useLayoutEffect behave in the New Architecture?](#241-how-does-uselayouteffect-behave-in-the-new-architecture)
- [242: How do you react to the keyboard opening and closing?](#242-how-do-you-react-to-the-keyboard-opening-and-closing)
- [243: How do you handle incoming deep links without a navigation library?](#243-how-do-you-handle-incoming-deep-links-without-a-navigation-library)
- [244: How do you copy text to the clipboard?](#244-how-do-you-copy-text-to-the-clipboard)
- [245: How do you build infinite scroll with TanStack Query?](#245-how-do-you-build-infinite-scroll-with-tanstack-query)
- [246: Why do you get the warning "VirtualizedLists should never be nested inside plain ScrollViews"?](#246-why-do-you-get-the-warning-virtualizedlists-should-never-be-nested-inside-plain-scrollviews)
- [247: What does keyboardShouldPersistTaps do?](#247-what-does-keyboardshouldpersisttaps-do)
- [248: How do you make a header stick to the top while scrolling?](#248-how-do-you-make-a-header-stick-to-the-top-while-scrolling)
- [249: How do you render a grid with FlatList?](#249-how-do-you-render-a-grid-with-flatlist)
- [250: How do you build a chat list that starts at the bottom?](#250-how-do-you-build-a-chat-list-that-starts-at-the-bottom)
- [251: Why should you never put secret API keys in a React Native app?](#251-why-should-you-never-put-secret-api-keys-in-a-react-native-app)
- [252: What is SSL pinning?](#252-what-is-ssl-pinning)
- [253: How do you detect rooted or jailbroken devices?](#253-how-do-you-detect-rooted-or-jailbroken-devices)
- [254: How do you handle access and refresh tokens in a React Native app?](#254-how-do-you-handle-access-and-refresh-tokens-in-a-react-native-app)
- [255: How do you implement OAuth login (Google, GitHub and so on) in React Native?](#255-how-do-you-implement-oauth-login-google-github-and-so-on-in-react-native)
- [256: How do you add Face ID or fingerprint login?](#256-how-do-you-add-face-id-or-fingerprint-login)
- [257: How do you add in-app purchases or subscriptions?](#257-how-do-you-add-in-app-purchases-or-subscriptions)
- [258: How do you show a map?](#258-how-do-you-show-a-map)
- [259: How do you play video?](#259-how-do-you-play-video)
- [260: How do you play and record audio?](#260-how-do-you-play-and-record-audio)
- [261: What are haptics and how do you use them?](#261-what-are-haptics-and-how-do-you-use-them)
- [262: How do you keep the splash screen visible until the app is ready?](#262-how-do-you-keep-the-splash-screen-visible-until-the-app-is-ready)
- [263: Why must require() for images use a static string?](#263-why-must-require-for-images-use-a-static-string)
- [264: How do you check if a library works with your React Native version and the New Architecture?](#264-how-do-you-check-if-a-library-works-with-your-react-native-version-and-the-new-architecture)
- [265: What is patch-package and when do you use it?](#265-what-is-patch-package-and-when-do-you-use-it)
- [266: How do you write a simple native module with the Expo Modules API?](#266-how-do-you-write-a-simple-native-module-with-the-expo-modules-api)
- [267: How do you define a Turbo Module spec?](#267-how-do-you-define-a-turbo-module-spec)
- [268: What is Codegen?](#268-what-is-codegen)
- [269: Can native module methods be synchronous?](#269-can-native-module-methods-be-synchronous)
- [270: How does a native module send events to JavaScript?](#270-how-does-a-native-module-send-events-to-javascript)
- [271: What is a brownfield app?](#271-what-is-a-brownfield-app)
- [272: What is Headless JS?](#272-what-is-headless-js)
- [273: What happens to timers when the app goes to the background?](#273-what-happens-to-timers-when-the-app-goes-to-the-background)
- [274: What replaced InteractionManager?](#274-what-replaced-interactionmanager)
- [275: Can you use startTransition and useTransition in React Native?](#275-can-you-use-starttransition-and-usetransition-in-react-native)
- [276: Does Suspense work in React Native?](#276-does-suspense-work-in-react-native)
- [277: Which React 19 features can you use in React Native?](#277-which-react-19-features-can-you-use-in-react-native)
- [278: What styling libraries are popular in React Native?](#278-what-styling-libraries-are-popular-in-react-native)
- [279: Which UI component libraries are used in React Native?](#279-which-ui-component-libraries-are-used-in-react-native)
- [280: What are PlatformColor and DynamicColorIOS?](#280-what-are-platformcolor-and-dynamiccolorios)
- [281: Which image formats should you use in a React Native app?](#281-which-image-formats-should-you-use-in-a-react-native-app)
- [282: When would you use an uncontrolled TextInput?](#282-when-would-you-use-an-uncontrolled-textinput)
- [283: How do you find out why a component re-renders too often?](#283-how-do-you-find-out-why-a-component-re-renders-too-often)
- [284: Do inline styles hurt performance?](#284-do-inline-styles-hurt-performance)
- [285: How do you avoid memory leaks in React Native components?](#285-how-do-you-avoid-memory-leaks-in-react-native-components)
- [286: What are API routes in Expo Router?](#286-what-are-api-routes-in-expo-router)
- [287: How do you add web support to a React Native app?](#287-how-do-you-add-web-support-to-a-react-native-app)
- [288: How do you test a release build locally?](#288-how-do-you-test-a-release-build-locally)
- [289: How do you ask users to update the app?](#289-how-do-you-ask-users-to-update-the-app)
- [290: How do you build a bottom sheet?](#290-how-do-you-build-a-bottom-sheet)
- [291: How do you build a carousel?](#291-how-do-you-build-a-carousel)
- [292: How do you implement search with debounce?](#292-how-do-you-implement-search-with-debounce)
- [293: How do you show skeleton loaders?](#293-how-do-you-show-skeleton-loaders)
- [294: How do you prefetch images?](#294-how-do-you-prefetch-images)
- [295: How do you handle dates, time zones and number formatting?](#295-how-do-you-handle-dates-time-zones-and-number-formatting)
- [296: How do you show a toast or snackbar?](#296-how-do-you-show-a-toast-or-snackbar)
- [297: What are typed routes in Expo Router?](#297-what-are-typed-routes-in-expo-router)
- [298: How do you track screen views for analytics?](#298-how-do-you-track-screen-views-for-analytics)
- [299: How do you keep the right aspect ratio for an image or video?](#299-how-do-you-keep-the-right-aspect-ratio-for-an-image-or-video)
- [300: How do you implement logout properly?](#300-how-do-you-implement-logout-properly)

### Advanced Questions (301-450)

- [301: Explain the parts of the New Architecture and how they fit together.](#301-explain-the-parts-of-the-new-architecture-and-how-they-fit-together)
- [302: How did the old bridge work, and what problems did it cause?](#302-how-did-the-old-bridge-work-and-what-problems-did-it-cause)
- [303: What is JSI in more detail?](#303-what-is-jsi-in-more-detail)
- [304: What are the phases of the Fabric rendering pipeline?](#304-what-are-the-phases-of-the-fabric-rendering-pipeline)
- [305: Why is the shadow tree immutable in Fabric?](#305-why-is-the-shadow-tree-immutable-in-fabric)
- [306: Which threads do the render, commit and mount phases run on?](#306-which-threads-do-the-render-commit-and-mount-phases-run-on)
- [307: What is view flattening?](#307-what-is-view-flattening)
- [308: What is bridgeless mode?](#308-what-is-bridgeless-mode)
- [309: What does lazy loading of Turbo Modules mean for startup?](#309-what-does-lazy-loading-of-turbo-modules-mean-for-startup)
- [310: What are C++ Turbo Modules and why use them?](#310-what-are-c-turbo-modules-and-why-use-them)
- [311: How does Codegen work for a Fabric native component?](#311-how-does-codegen-work-for-a-fabric-native-component)
- [312: How do you call imperative methods on a native component?](#312-how-do-you-call-imperative-methods-on-a-native-component)
- [313: What is the interop layer and should you rely on it?](#313-what-is-the-interop-layer-and-should-you-rely-on-it)
- [314: How do you migrate an old native module to a Turbo Module?](#314-how-do-you-migrate-an-old-native-module-to-a-turbo-module)
- [315: How is Hermes different from engines like V8 or JavaScriptCore?](#315-how-is-hermes-different-from-engines-like-v8-or-javascriptcore)
- [316: What changed with Hermes V1?](#316-what-changed-with-hermes-v1)
- [317: What happened to JavaScriptCore support?](#317-what-happened-to-javascriptcore-support)
- [318: How does Metro build a bundle?](#318-how-does-metro-build-a-bundle)
- [319: What are inline requires and how do they help startup?](#319-what-are-inline-requires-and-how-do-they-help-startup)
- [320: How do you symbolicate a production crash?](#320-how-do-you-symbolicate-a-production-crash)
- [321: How does the event loop work in the New Architecture?](#321-how-does-the-event-loop-work-in-the-new-architecture)
- [322: What is web-based event dispatching in React Native 0.88?](#322-what-is-web-based-event-dispatching-in-react-native-088)
- [323: What are DOM Node APIs on React Native refs?](#323-what-are-dom-node-apis-on-react-native-refs)
- [324: How do you measure app startup time?](#324-how-do-you-measure-app-startup-time)
- [325: What can you do to make a large app start faster?](#325-what-can-you-do-to-make-a-large-app-start-faster)
- [326: How do you profile JavaScript performance?](#326-how-do-you-profile-javascript-performance)
- [327: How do you profile native performance?](#327-how-do-you-profile-native-performance)
- [328: The UI FPS is fine but the JS FPS drops while scrolling a list. How do you fix it?](#328-the-ui-fps-is-fine-but-the-js-fps-drops-while-scrolling-a-list-how-do-you-fix-it)
- [329: How do you investigate memory growth in a React Native app?](#329-how-do-you-investigate-memory-growth-in-a-react-native-app)
- [330: How does FlashList v2 recycling work, and what pitfalls does it have?](#330-how-does-flashlist-v2-recycling-work-and-what-pitfalls-does-it-have)
- [331: How do you avoid re-rendering every list row when one row's data changes?](#331-how-do-you-avoid-re-rendering-every-list-row-when-one-rows-data-changes)
- [332: Why can large images crash an app, and how do you prevent it?](#332-why-can-large-images-crash-an-app-and-how-do-you-prevent-it)
- [333: How does Reanimated run animations on the UI thread?](#333-how-does-reanimated-run-animations-on-the-ui-thread)
- [334: How do you call JS-thread code from a worklet and vice versa?](#334-how-do-you-call-js-thread-code-from-a-worklet-and-vice-versa)
- [335: What is the Shared Animation Backend in React Native 0.85?](#335-what-is-the-shared-animation-backend-in-react-native-085)
- [336: How do you compose multiple gestures?](#336-how-do-you-compose-multiple-gestures)
- [337: How do you keep the JS thread free during heavy computation?](#337-how-do-you-keep-the-js-thread-free-during-heavy-computation)
- [338: How do you analyze and reduce the JavaScript bundle size?](#338-how-do-you-analyze-and-reduce-the-javascript-bundle-size)
- [339: Does code splitting work in React Native?](#339-does-code-splitting-work-in-react-native)
- [340: How would you structure a large React Native codebase?](#340-how-would-you-structure-a-large-react-native-codebase)
- [341: How do you build a design system for React Native?](#341-how-do-you-build-a-design-system-for-react-native)
- [342: How do you resolve conflicts in offline sync?](#342-how-do-you-resolve-conflicts-in-offline-sync)
- [343: How do you implement optimistic updates?](#343-how-do-you-implement-optimistic-updates)
- [344: How do you build reliable real-time features on mobile?](#344-how-do-you-build-reliable-real-time-features-on-mobile)
- [345: What limits does iOS place on background work?](#345-what-limits-does-ios-place-on-background-work)
- [346: How would you design push notifications for a large app?](#346-how-would-you-design-push-notifications-for-a-large-app)
- [347: How do you make deep links secure?](#347-how-do-you-make-deep-links-secure)
- [348: How do Keychain and Keystore protect data?](#348-how-do-keychain-and-keystore-protect-data)
- [349: What are the trade-offs of certificate pinning?](#349-what-are-the-trade-offs-of-certificate-pinning)
- [350: How hard is it to reverse engineer a React Native app, and what can you do about it?](#350-how-hard-is-it-to-reverse-engineer-a-react-native-app-and-what-can-you-do-about-it)
- [351: How do you make OTA updates secure?](#351-how-do-you-make-ota-updates-secure)
- [352: How would you roll out OTA updates safely?](#352-how-would-you-roll-out-ota-updates-safely)
- [353: What is the difference between a JS error, a native crash and an ANR?](#353-what-is-the-difference-between-a-js-error-a-native-crash-and-an-anr)
- [354: What causes ANRs in React Native apps on Android?](#354-what-causes-anrs-in-react-native-apps-on-android)
- [355: What is the iOS watchdog and why might it kill your app?](#355-what-is-the-ios-watchdog-and-why-might-it-kill-your-app)
- [356: How do you integrate React Native into an existing native app?](#356-how-do-you-integrate-react-native-into-an-existing-native-app)
- [357: What is the iOS SceneDelegate change in React Native 0.88?](#357-what-is-the-ios-scenedelegate-change-in-react-native-088)
- [358: What is the Android 16 KB page size requirement?](#358-what-is-the-android-16-kb-page-size-requirement)
- [359: What are precompiled iOS binaries and why do they matter?](#359-what-are-precompiled-ios-binaries-and-why-do-they-matter)
- [360: What is the state of Swift Package Manager support in React Native?](#360-what-is-the-state-of-swift-package-manager-support-in-react-native)
- [361: How do you debug iOS build failures with CocoaPods?](#361-how-do-you-debug-ios-build-failures-with-cocoapods)
- [362: How do you speed up Android builds?](#362-how-do-you-speed-up-android-builds)
- [363: What are the trade-offs between Expo CNG and committing native folders?](#363-what-are-the-trade-offs-between-expo-cng-and-committing-native-folders)
- [364: How do you write a custom Expo config plugin?](#364-how-do-you-write-a-custom-expo-config-plugin)
- [365: When would you choose the Expo Modules API over a Turbo Module?](#365-when-would-you-choose-the-expo-modules-api-over-a-turbo-module)
- [366: How do you create a native view with the Expo Modules API?](#366-how-do-you-create-a-native-view-with-the-expo-modules-api)
- [367: Which thread does native module code run on, and how do you handle UI work?](#367-which-thread-does-native-module-code-run-on-and-how-do-you-handle-ui-work)
- [368: How do you pass large binary data between JS and native efficiently?](#368-how-do-you-pass-large-binary-data-between-js-and-native-efficiently)
- [369: How do you test native modules?](#369-how-do-you-test-native-modules)
- [370: What testing strategy would you use for a React Native app?](#370-what-testing-strategy-would-you-use-for-a-react-native-app)
- [371: Why are E2E tests flaky and how do you make them stable?](#371-why-are-e2e-tests-flaky-and-how-do-you-make-them-stable)
- [372: How do you do visual regression testing in React Native?](#372-how-do-you-do-visual-regression-testing-in-react-native)
- [373: How do you catch performance regressions before release?](#373-how-do-you-catch-performance-regressions-before-release)
- [374: How do you manage focus for screen reader users?](#374-how-do-you-manage-focus-for-screen-reader-users)
- [375: What are accessibility actions?](#375-what-are-accessibility-actions)
- [376: How do you announce content that changes on its own?](#376-how-do-you-announce-content-that-changes-on-its-own)
- [377: How do you respect the reduce motion setting?](#377-how-do-you-respect-the-reduce-motion-setting)
- [378: What problems do you meet when supporting right-to-left layouts?](#378-what-problems-do-you-meet-when-supporting-right-to-left-layouts)
- [379: How do you improve navigation performance in a big app?](#379-how-do-you-improve-navigation-performance-in-a-big-app)
- [380: How do you persist and restore navigation state?](#380-how-do-you-persist-and-restore-navigation-state)
- [381: A user opens a deep link to a protected screen while the app is closed and they are logged out. How do you handle it?](#381-a-user-opens-a-deep-link-to-a-protected-screen-while-the-app-is-closed-and-they-are-logged-out-how-do-you-handle-it)
- [382: How do you share business logic between a React Native app and a web app?](#382-how-do-you-share-business-logic-between-a-react-native-app-and-a-web-app)
- [383: How do you decide between server state and client state tools?](#383-how-do-you-decide-between-server-state-and-client-state-tools)
- [384: What is tearing and how do external stores avoid it with concurrent rendering?](#384-what-is-tearing-and-how-do-external-stores-avoid-it-with-concurrent-rendering)
- [385: What should you watch out for when enabling the React Compiler?](#385-what-should-you-watch-out-for-when-enabling-the-react-compiler)
- [386: What does StrictMode do in React Native?](#386-what-does-strictmode-do-in-react-native)
- [387: The app is smooth on iPhones but slow on mid-range Android phones. What do you check?](#387-the-app-is-smooth-on-iphones-but-slow-on-mid-range-android-phones-what-do-you-check)
- [388: The app crashes on startup only in release builds. How do you investigate?](#388-the-app-crashes-on-startup-only-in-release-builds-how-do-you-investigate)
- [389: Something works in debug but behaves differently in release. What are the usual causes?](#389-something-works-in-debug-but-behaves-differently-in-release-what-are-the-usual-causes)
- [390: How would you upgrade an app from React Native 0.72 to the latest version?](#390-how-would-you-upgrade-an-app-from-react-native-072-to-the-latest-version)
- [391: How would you move a bare React Native app to Expo CNG?](#391-how-would-you-move-a-bare-react-native-app-to-expo-cng)
- [392: An important library doesn't support the New Architecture. What are your options?](#392-an-important-library-doesnt-support-the-new-architecture-what-are-your-options)
- [393: How would you build a chat screen?](#393-how-would-you-build-a-chat-screen)
- [394: How would you build a feed with many images that scrolls smoothly?](#394-how-would-you-build-a-feed-with-many-images-that-scrolls-smoothly)
- [395: How would you design an offline-first app, for example for field workers?](#395-how-would-you-design-an-offline-first-app-for-example-for-field-workers)
- [396: How would you build a vertical video feed like TikTok?](#396-how-would-you-build-a-vertical-video-feed-like-tiktok)
- [397: How would you show thousands of points on a map?](#397-how-would-you-show-thousands-of-points-on-a-map)
- [398: What would you require for a banking app built with React Native?](#398-what-would-you-require-for-a-banking-app-built-with-react-native)
- [399: How would you build a white-label app (one codebase, many branded apps)?](#399-how-would-you-build-a-white-label-app-one-codebase-many-branded-apps)
- [400: How would you add feature flags and remote config?](#400-how-would-you-add-feature-flags-and-remote-config)
- [401: How would you run A/B tests in a React Native app?](#401-how-would-you-run-ab-tests-in-a-react-native-app)
- [402: How do you schedule local notifications reliably?](#402-how-do-you-schedule-local-notifications-reliably)
- [403: How do you add payments like Apple Pay and Google Pay?](#403-how-do-you-add-payments-like-apple-pay-and-google-pay)
- [404: How do you add a home screen widget to a React Native app?](#404-how-do-you-add-a-home-screen-widget-to-a-react-native-app)
- [405: How do out-of-tree platforms like Windows, macOS and TV work?](#405-how-do-out-of-tree-platforms-like-windows-macos-and-tv-work)
- [406: What JavaScript differences between Hermes and browsers can cause bugs?](#406-what-javascript-differences-between-hermes-and-browsers-can-cause-bugs)
- [407: How do you add missing web or Node APIs like crypto.getRandomValues or Buffer?](#407-how-do-you-add-missing-web-or-node-apis-like-cryptogetrandomvalues-or-buffer)
- [408: How do you cancel requests and handle timeouts properly?](#408-how-do-you-cancel-requests-and-handle-timeouts-properly)
- [409: How do you design a React Native app to be battery friendly?](#409-how-do-you-design-a-react-native-app-to-be-battery-friendly)
- [410: How does React Native DevTools connect to the app?](#410-how-does-react-native-devtools-connect-to-the-app)
- [411: How do you do logging in a production React Native app?](#411-how-do-you-do-logging-in-a-production-react-native-app)
- [412: How do you do staged rollouts of store releases?](#412-how-do-you-do-staged-rollouts-of-store-releases)
- [413: What are common reasons for App Store rejections in React Native apps?](#413-what-are-common-reasons-for-app-store-rejections-in-react-native-apps)
- [414: What is an iOS privacy manifest?](#414-what-is-an-ios-privacy-manifest)
- [415: Why do you need to keep up with Android target SDK requirements?](#415-why-do-you-need-to-keep-up-with-android-target-sdk-requirements)
- [416: How do you handle differences between OS versions?](#416-how-do-you-handle-differences-between-os-versions)
- [417: Can an app have more than one React Native root view?](#417-can-an-app-have-more-than-one-react-native-root-view)
- [418: How do you use the Performance API in React Native?](#418-how-do-you-use-the-performance-api-in-react-native)
- [419: What is setNativeProps and why should you avoid it?](#419-what-is-setnativeprops-and-why-should-you-avoid-it)
- [420: How does Fast Refresh work internally?](#420-how-does-fast-refresh-work-internally)
- [421: How does Metro decide which file to load for an import?](#421-how-does-metro-decide-which-file-to-load-for-an-import)
- [422: How does text rendering work in React Native?](#422-how-does-text-rendering-work-in-react-native)
- [423: What makes Yoga layout expensive, and how do you keep it fast?](#423-what-makes-yoga-layout-expensive-and-how-do-you-keep-it-fast)
- [424: How does the responder system work?](#424-how-does-the-responder-system-work)
- [425: How is Gesture Handler different from the responder system?](#425-how-is-gesture-handler-different-from-the-responder-system)
- [426: How does garbage collection work in Hermes, and what can you do about GC pauses?](#426-how-does-garbage-collection-work-in-hermes-and-what-can-you-do-about-gc-pauses)
- [427: What are the security risks of WebView and how do you reduce them?](#427-what-are-the-security-risks-of-webview-and-how-do-you-reduce-them)
- [428: How do you encrypt data stored in a local database?](#428-how-do-you-encrypt-data-stored-in-a-local-database)
- [429: What is Expo UI and why is it interesting?](#429-what-is-expo-ui-and-why-is-it-interesting)
- [430: How do you support hardware keyboards and TV remotes?](#430-how-do-you-support-hardware-keyboards-and-tv-remotes)
- [431: How do you support foldables and multi-window?](#431-how-do-you-support-foldables-and-multi-window)
- [432: How do you build and publish a React Native library?](#432-how-do-you-build-and-publish-a-react-native-library)
- [433: How do you handle old app versions when your API changes?](#433-how-do-you-handle-old-app-versions-when-your-api-changes)
- [434: A bug happens only on a specific Android device model. How do you investigate?](#434-a-bug-happens-only-on-a-specific-android-device-model-how-do-you-investigate)
- [435: Your Android app takes 4 seconds to become interactive. How would you bring it under 2 seconds?](#435-your-android-app-takes-4-seconds-to-become-interactive-how-would-you-bring-it-under-2-seconds)
- [436: Users report that the app randomly logs them out. What could cause it?](#436-users-report-that-the-app-randomly-logs-them-out-what-could-cause-it)
- [437: The app was rejected by App Review. How do you handle it?](#437-the-app-was-rejected-by-app-review-how-do-you-handle-it)
- [438: The app crashes when a user selects 30 photos to upload. Why, and how do you fix it?](#438-the-app-crashes-when-a-user-selects-30-photos-to-upload-why-and-how-do-you-fix-it)
- [439: How would you build an app that tracks location in the background, like a running tracker?](#439-how-would-you-build-an-app-that-tracks-location-in-the-background-like-a-running-tracker)
- [440: You need an app for iOS, Android and web from day one. How would you set it up?](#440-you-need-an-app-for-ios-android-and-web-from-day-one-how-would-you-set-it-up)
- [441: How would you decide between React Native and fully native for a new product?](#441-how-would-you-decide-between-react-native-and-fully-native-for-a-new-product)
- [442: In 2026, would you start a new project with Expo or with the Community CLI?](#442-in-2026-would-you-start-a-new-project-with-expo-or-with-the-community-cli)
- [443: React Navigation or Expo Router?](#443-react-navigation-or-expo-router)
- [444: When would you use Animated and when Reanimated?](#444-when-would-you-use-animated-and-when-reanimated)
- [445: When should you write native code instead of using JavaScript?](#445-when-should-you-write-native-code-instead-of-using-javascript)
- [446: How do you keep a React Native app healthy over many years?](#446-how-do-you-keep-a-react-native-app-healthy-over-many-years)
- [447: Which newer CSS-like style features does React Native support?](#447-which-newer-css-like-style-features-does-react-native-support)
- [448: What were the biggest changes in React Native in 2025 and 2026?](#448-what-were-the-biggest-changes-in-react-native-in-2025-and-2026)
- [449: Where is React Native heading?](#449-where-is-react-native-heading)
- [450: Explain what happens from a state update to pixels on the screen in React Native.](#450-explain-what-happens-from-a-state-update-to-pixels-on-the-screen-in-react-native)

---

## Easy Questions (1-150)

### 1: What is React Native?

React Native is a framework for building mobile apps with React and JavaScript (or TypeScript). You write components like `<View>` and `<Text>`, and React Native turns them into real native views on iOS and Android. So the UI is native, but the logic is written in JavaScript.

It was created at Meta and open sourced in 2015. Today it is used in apps like Facebook, Instagram, Discord, Shopify and many others.

### 2: What is the difference between React and React Native?

React is the library that handles components, state, props and hooks. It does not care where the output goes. On the web you use `react-dom` to render to the DOM. In React Native you use `react-native` to render to native mobile views.

The main differences you notice day to day:

- No HTML tags. You use `<View>`, `<Text>`, `<Image>` instead of `<div>`, `<p>`, `<img>`.
- No CSS files. Styles are JavaScript objects and the layout uses Flexbox.
- No browser APIs like `window.document` or `localStorage`.
- Navigation, storage and device features come from separate libraries.

Hooks, components, props, state and context all work the same way.

### 3: Who maintains React Native today?

React Native was built and maintained by Meta for most of its life, together with a large community and companies like Microsoft, Expo, Software Mansion, Callstack and Amazon. In 2025 React and React Native moved to the React Foundation, an independent foundation, and in 2026 the GitHub repositories moved from the `facebook` organization to the `react` organization. Meta still contributes a lot, but the project is no longer owned by one company.

### 4: Which platforms can you build for with React Native?

Officially, iOS and Android are supported in the core repository. Other platforms are supported by "out-of-tree" projects:

- **Web**: React Native Web (used by Expo for web support)
- **Windows and macOS**: `react-native-windows` and `react-native-macos` from Microsoft
- **TV**: `react-native-tvos` for Apple TV and Android TV
- **Meta Quest**: announced in 2026
- **visionOS**: through a community fork

Most teams use it for iOS and Android, and sometimes web.

### 5: Is a React Native app a native app or a web view?

It is a native app. React Native does not render HTML inside a web view. When you write `<View>`, React Native creates a real `UIView` on iOS and a real `android.view.View` (a `ViewGroup`) on Android. Your JavaScript runs in a JavaScript engine (Hermes) inside the app, and it tells the native side what to draw.

This is the main difference from tools like Cordova or Ionic, which render HTML in a web view.

### 6: What are the main advantages of React Native?

- One codebase for iOS and Android (and sometimes web).
- If your team already knows React, the learning curve is small.
- Fast development with Fast Refresh. You see changes in under a second.
- Real native UI, so the app looks and feels like a normal app.
- You can update JavaScript code over the air without going through the app store (within store rules).
- Large ecosystem of libraries, and tools like Expo that handle builds and updates.
- You can still write native code in Swift, Kotlin, Objective-C, Java or C++ when you need it.

### 7: What are the downsides or limitations of React Native?

- Some features need native code, so you sometimes still need iOS and Android knowledge.
- Third-party libraries can lag behind new React Native versions or new OS features.
- Upgrading React Native used to be painful. It is much better now, but you still need to plan upgrades.
- Very heavy graphics or animations (games, complex video editing) may be easier in fully native code or a game engine.
- The app size is a bit larger than a minimal native app because it ships a JavaScript engine and the React Native runtime.

### 8: How does React Native compare to Flutter?

Both are cross-platform frameworks, but they work differently:

|                  | React Native                   | Flutter                                                |
| ---------------- | ------------------------------ | ------------------------------------------------------ |
| Language         | JavaScript / TypeScript        | Dart                                                   |
| UI               | Uses real platform views       | Draws everything itself with its own engine (Impeller) |
| Look             | Native look by default         | Same look on every platform by default                 |
| Web skills reuse | High, if you know React        | Low                                                    |
| OTA updates      | Common (EAS Update and others) | Not officially supported                               |

React Native is a good choice if your team knows React or you share code with a React web app. Flutter is a good choice if you want pixel-identical UI everywhere and are fine with Dart.

### 9: When would you choose fully native development instead of React Native?

Native development (Swift for iOS, Kotlin for Android) makes sense when:

- The app depends heavily on platform-specific features, like complex camera processing or AR.
- You need maximum performance for graphics, like games.
- You only target one platform and already have a native team.
- The app is mostly OS integration (widgets, watch apps, extensions) with little shared UI.

For most business apps (forms, lists, feeds, e-commerce, chat) React Native is fast enough and saves a lot of time.

### 10: How do you create a new React Native project?

The React Native docs recommend starting with a framework, and Expo is the main one:

```bash
npx create-expo-app@latest my-app
cd my-app
npx expo start
```

This gives you a TypeScript project with Expo Router, ready to run on a device or simulator.

If you don't want a framework, you can use the Community CLI:

```bash
npx @react-native-community/cli@latest init MyApp
```

The old `npx react-native init` command is deprecated.

### 11: What is Expo?

Expo is an open source framework and set of tools built on top of React Native. It gives you:

- A CLI (`npx expo`) for running, building and configuring the app
- The Expo SDK: well-maintained modules for camera, file system, notifications, images, fonts and more
- Expo Router for file-based navigation
- Continuous Native Generation (CNG), which generates the `ios` and `android` folders for you
- EAS (Expo Application Services), a paid cloud service for builds, store submissions and over-the-air updates

Expo apps are still normal React Native apps. You can add any native code or library you need.

### 12: Why do the React Native docs recommend using a framework?

Plain React Native gives you the core components and the native runtime, but a real app also needs navigation, native module setup, builds, updates, icons, splash screens and upgrade tooling. If you start without a framework, you end up building or choosing all of this yourself.

A framework like Expo solves these problems in a standard way, so you spend your time on the app instead of the setup. You can still drop down to native code at any point.

### 13: What is the difference between Expo Go and a development build?

**Expo Go** is a ready-made app from the App Store and Play Store. It already contains the Expo SDK native modules, so you can scan a QR code and run your JavaScript in it without building anything. But you can't add your own native code or libraries that are not included in Expo Go.

A **development build** is your own app, built with your native dependencies and the `expo-dev-client` library. It works like Expo Go (QR code, Fast Refresh, dev menu), but it contains exactly the native code your app needs. Real projects almost always use development builds. Expo Go is mostly for learning and quick tests.

### 14: What is Metro?

Metro is the JavaScript bundler used by React Native. It does a similar job to Webpack or Vite on the web:

- Resolves `import` and `require` statements
- Transforms code with Babel (TypeScript, JSX, modern syntax)
- Combines everything into one bundle that the app loads
- Serves the bundle to the app during development and supports Fast Refresh

You start it with `npx expo start` or `npx react-native start`. Its config file is `metro.config.js`.

### 15: What is Hermes?

Hermes is a JavaScript engine built by Meta for React Native. It is the default engine on iOS and Android. Instead of parsing and compiling JavaScript when the app starts, Hermes compiles your code to bytecode at build time. This makes startup faster and uses less memory.

Since React Native 0.84, Hermes V1 (the new version of the engine) is the default. JavaScriptCore (JSC) is no longer in core and is only available as a community package.

### 16: How often is React Native released?

React Native ships a new minor version (0.xx) about every two months. Each release has release candidates first. Only the latest few versions are supported with patch releases, so you should not stay too far behind.

At the time of writing the latest version is 0.88 (October 2026). React Native still uses a `0.x` version number, but it is stable and used in production by many large companies. Expo releases a new SDK version roughly three times a year, each one tied to a specific React Native version.

### 17: Which languages do you use in a React Native project?

- **TypeScript or JavaScript** for the app code. TypeScript is the default in new projects.
- **Swift or Objective-C** for iOS native code.
- **Kotlin or Java** for Android native code.
- **C++** for shared native code, like C++ Turbo Modules.

Most developers write only TypeScript. Native languages are needed only when you build your own native modules or fix native build issues.

### 18: Does React Native support TypeScript?

Yes. New projects created with Expo or the Community CLI use TypeScript by default. React Native ships its own type definitions, so you don't need `@types/react-native` anymore. Babel strips the types when bundling, and you run `tsc` separately to check types.

```tsx
type GreetingProps = {
  name: string;
};

export function Greeting({ name }: GreetingProps) {
  return <Text>Hello, {name}</Text>;
}
```

Since 0.87, the Strict TypeScript API is the default, which means you should only import from `react-native` itself, not from internal paths.

### 19: What are the core components of React Native?

The most used core components are:

- `View`: a container, like `div`
- `Text`: shows text
- `Image`: shows images
- `TextInput`: text field
- `ScrollView`: scrollable container
- `FlatList` and `SectionList`: performant lists
- `Pressable`: handles touches
- `Button`: a simple platform button
- `Switch`, `ActivityIndicator`, `Modal`, `RefreshControl`, `StatusBar`, `KeyboardAvoidingView`

Anything else (navigation, icons, gestures, camera) comes from libraries.

### 20: What is the View component?

`View` is the basic building block of the UI. It is a container that supports layout with Flexbox, styles, touch handling and accessibility. It maps to `UIView` on iOS and `ViewGroup` on Android.

```tsx
import { View, Text } from "react-native";

export function Card() {
  return (
    <View style={{ padding: 16, borderRadius: 8, backgroundColor: "white" }}>
      <Text>Hello</Text>
    </View>
  );
}
```

`View`s can be nested as deep as you need.

### 21: Why must all text be inside a Text component?

In React Native you can't put raw strings directly inside a `View`. Native platforms draw text with special text views, so React Native needs a `<Text>` component to know where text starts and how to style it.

```tsx
// Wrong: crashes with "Text strings must be rendered within a <Text> component"
<View>Hello</View>

// Right
<View>
  <Text>Hello</Text>
</View>
```

A common bug is `{count && <Text>...</Text>}` when `count` is `0`. The `0` is rendered as raw text and causes the same error. Use `count > 0 && ...` instead.

### 22: How do you show an image?

Use the `Image` component. For local images use `require`, and for remote images pass a `uri`:

```tsx
import { Image } from 'react-native';

<Image source={require('./assets/logo.png')} />

<Image
  source={{ uri: 'https://example.com/photo.jpg' }}
  style={{ width: 200, height: 200 }}
/>
```

Remote images must have a width and height (or be sized by their parent with Flexbox), because React Native doesn't know the size before downloading. Local images get their size from the file.

### 23: What is the TextInput component?

`TextInput` is a text field. You usually use it as a controlled component:

```tsx
import { useState } from "react";
import { TextInput } from "react-native";

export function NameInput() {
  const [name, setName] = useState("");

  return (
    <TextInput
      value={name}
      onChangeText={setName}
      placeholder="Your name"
      style={{ borderWidth: 1, padding: 8, borderRadius: 4 }}
    />
  );
}
```

Useful props: `keyboardType`, `secureTextEntry`, `autoCapitalize`, `autoCorrect`, `multiline`, `maxLength`, `returnKeyType`, `onSubmitEditing`.

### 24: What is the ScrollView component?

`ScrollView` is a container that lets its content scroll. It renders all its children at once, so it is fine for small amounts of content like a settings screen or a form. For long or dynamic lists use `FlatList` instead.

```tsx
<ScrollView contentContainerStyle={{ padding: 16 }}>
  <Text>Section 1</Text>
  <Text>Section 2</Text>
</ScrollView>
```

A `ScrollView` needs a bounded height to scroll, so its parent usually has `flex: 1`.

### 25: What is the Button component and why is it rarely used?

`Button` renders a simple native-looking button:

```tsx
<Button title="Save" onPress={handleSave} />
```

It is rarely used in real apps because you can only change its `title` and `color`. You can't add icons, padding, border radius or custom fonts. Most apps build their own button with `Pressable` and `Text`.

### 26: What is Pressable?

`Pressable` is the recommended component for handling touches. It wraps any content and gives you press events and the pressed state:

```tsx
import { Pressable, Text } from "react-native";

<Pressable
  onPress={() => console.log("pressed")}
  onLongPress={() => console.log("long press")}
  style={({ pressed }) => ({
    padding: 12,
    backgroundColor: pressed ? "#ddd" : "#eee",
  })}
>
  <Text>Tap me</Text>
</Pressable>;
```

It also supports `onPressIn`, `onPressOut`, `delayLongPress`, `hitSlop`, `disabled` and `android_ripple`.

### 27: What are the Touchable components?

`TouchableOpacity`, `TouchableHighlight` and `TouchableWithoutFeedback` are the older way to handle touches. `TouchableOpacity` fades the content when pressed, `TouchableHighlight` shows a background color, and `TouchableWithoutFeedback` shows nothing.

They still work and you will see them in older code, but the docs recommend `Pressable` for new code because it is more flexible and gives you the `pressed` state for any styling you want.

### 28: How does styling work in React Native?

There is no CSS. You write styles as JavaScript objects and pass them to the `style` prop. Property names are camelCase (`backgroundColor`, not `background-color`), and most numbers have no unit.

```tsx
import { StyleSheet, View, Text } from "react-native";

export function Box() {
  return (
    <View style={styles.box}>
      <Text style={styles.title}>Hello</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  box: { padding: 16, backgroundColor: "#fafafa" },
  title: { fontSize: 18, fontWeight: "600" },
});
```

Styles do not cascade like CSS. Each component only gets the styles you pass to it (except nested `Text`, which inherits from its parent `Text`).

### 29: What does StyleSheet.create do?

`StyleSheet.create` takes an object of styles and returns the same object. It does not do much at runtime today, but it has a few benefits:

- TypeScript checks your style properties and values.
- It keeps styles outside the component, so a new object is not created on every render.
- It keeps the code readable by giving style objects names.

You can also pass plain objects inline, which is fine for small dynamic styles.

### 30: What units does React Native use for sizes?

Numbers in React Native are density-independent pixels (dp on Android, points on iOS). `width: 100` looks about the same physical size on a low-density and a high-density screen. React Native multiplies by the device pixel ratio for you.

You can also use percentages as strings, like `width: '50%'`. There is no `rem`, `em` or `vh`. For screen-based sizes use `useWindowDimensions()`.

### 31: How is Flexbox in React Native different from Flexbox on the web?

React Native uses Flexbox for all layout (through the Yoga layout engine), but some defaults are different:

- `flexDirection` defaults to `column`, not `row`.
- `alignContent` defaults to `flex-start`.
- `flexShrink` defaults to `0`.
- `flex` only accepts a single number.
- Every `View` is a flex container by default. You don't write `display: 'flex'`.

So a plain list of `View`s stacks vertically, which fits mobile screens well.

### 32: What does flex: 1 mean?

`flex: 1` makes a component take all the free space along the main axis of its parent. If several siblings have `flex` values, the space is split by those numbers.

```tsx
<View style={{ flex: 1 }}>
  <View style={{ flex: 1, backgroundColor: "red" }} />
  <View style={{ flex: 2, backgroundColor: "blue" }} />
</View>
```

Here the blue view is twice as tall as the red one. The root view of a screen usually has `flex: 1` so it fills the screen.

### 33: What is the difference between justifyContent and alignItems?

- `justifyContent` aligns children along the main axis (vertical by default, since `flexDirection` is `column`).
- `alignItems` aligns children along the cross axis (horizontal by default).

To center something in the middle of the screen:

```tsx
<View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
  <Text>Centered</Text>
</View>
```

If you change `flexDirection` to `row`, the two swap directions.

### 34: How do you add space between items?

You can use margins or padding, but the simplest way today is `gap`, `rowGap` and `columnGap`, which work like on the web:

```tsx
<View style={{ flexDirection: "row", gap: 8 }}>
  <Chip label="One" />
  <Chip label="Two" />
  <Chip label="Three" />
</View>
```

`gap` adds space only between children, not around the edges, so you don't need to remove the margin from the last item.

### 35: How does absolute positioning work?

Set `position: 'absolute'` and use `top`, `left`, `right` and `bottom`. The element is positioned relative to its parent, and it is taken out of the normal Flexbox flow.

```tsx
<View style={{ width: 100, height: 100 }}>
  <Image source={avatar} style={{ width: 100, height: 100 }} />
  <View style={{ position: "absolute", top: 4, right: 4 }}>
    <Badge count={3} />
  </View>
</View>
```

`StyleSheet.absoluteFill` is a shortcut for `{ position: 'absolute', top: 0, left: 0, right: 0, bottom: 0 }`. Note that the older `StyleSheet.absoluteFillObject` was removed in 0.85.

### 36: How do you combine multiple styles on one component?

Pass an array to `style`. Later styles override earlier ones, and falsy values are ignored:

```tsx
<View style={[styles.button, isActive && styles.active, { marginTop: 8 }]} />
```

This is also how you let a parent customize a child component: accept a `style` prop and put it last in the array.

```tsx
function Card({
  style,
  children,
}: {
  style?: StyleProp<ViewStyle>;
  children: React.ReactNode;
}) {
  return <View style={[styles.card, style]}>{children}</View>;
}
```

### 37: Do styles inherit in React Native?

Mostly no. A `View`'s styles do not affect its children. The one exception is text: a `Text` nested inside another `Text` inherits font styles like `color`, `fontSize` and `fontWeight`.

```tsx
<Text style={{ fontSize: 16, color: "#333" }}>
  Hello <Text style={{ fontWeight: "bold" }}>world</Text>
</Text>
```

"world" is bold, 16px and gray. If you want app-wide fonts, create your own `AppText` component with default styles.

### 38: How do you use custom fonts?

Add the font files to your project and load them. With Expo you can use the `expo-font` config plugin (fonts are embedded at build time) or the `useFonts` hook (fonts are loaded at runtime):

```tsx
import { useFonts } from "expo-font";

export default function App() {
  const [loaded] = useFonts({
    "Inter-Regular": require("./assets/fonts/Inter-Regular.ttf"),
  });

  if (!loaded) return null;

  return <Text style={{ fontFamily: "Inter-Regular" }}>Hello</Text>;
}
```

Without Expo, you place the fonts in an assets folder and link them with `npx react-native-asset`.

### 39: How do you render a list of items?

For a few items you can use `map`, like in React for the web. For long or dynamic lists use `FlatList`, because it only renders the items that are on screen (or close to it).

```tsx
<FlatList
  data={users}
  keyExtractor={(item) => item.id}
  renderItem={({ item }) => <Text>{item.name}</Text>}
/>
```

Using `map` inside a `ScrollView` for hundreds of items creates all of them at once and uses a lot of memory.

### 40: What is FlatList and why use it?

`FlatList` is a list component that virtualizes its items. It renders only what fits on the screen plus a small buffer, and removes items that scroll far away. This keeps memory and render time low even with thousands of items.

Main props:

- `data`: the array of items
- `renderItem`: function that returns the UI for one item
- `keyExtractor`: returns a unique key per item
- `ListHeaderComponent`, `ListFooterComponent`, `ListEmptyComponent`
- `ItemSeparatorComponent`
- `onEndReached`, `refreshing`, `onRefresh`
- `horizontal`, `numColumns`

### 41: What is keyExtractor in FlatList?

`keyExtractor` tells `FlatList` how to get a unique key for each item. React uses keys to know which items changed, were added or were removed.

```tsx
<FlatList
  data={orders}
  keyExtractor={(order) => order.id}
  renderItem={renderOrder}
/>
```

If you don't pass it, `FlatList` looks for `item.key`, then falls back to the index. Using the index is a bad idea if items can be added, removed or reordered, because state ends up on the wrong rows.

### 42: What is SectionList?

`SectionList` is like `FlatList`, but for grouped data with section headers, for example contacts grouped by letter.

```tsx
<SectionList
  sections={[
    { title: "A", data: ["Alice", "Adam"] },
    { title: "B", data: ["Bob"] },
  ]}
  keyExtractor={(item) => item}
  renderItem={({ item }) => <Text>{item}</Text>}
  renderSectionHeader={({ section }) => (
    <Text style={styles.header}>{section.title}</Text>
  )}
  stickySectionHeadersEnabled
/>
```

It is also virtualized.

### 43: How do you show a message when a list is empty?

Use `ListEmptyComponent`. It is rendered when `data` is an empty array:

```tsx
<FlatList
  data={items}
  renderItem={renderItem}
  ListEmptyComponent={<Text>No items yet</Text>}
  ListHeaderComponent={<Text style={styles.title}>Your items</Text>}
  ListFooterComponent={isLoadingMore ? <ActivityIndicator /> : null}
/>
```

Header and footer components scroll together with the list, which is better than placing them outside the list.

### 44: How do you add pull to refresh?

`FlatList` and `ScrollView` support pull to refresh. On `FlatList` you pass `refreshing` and `onRefresh`:

```tsx
const [refreshing, setRefreshing] = useState(false);

async function handleRefresh() {
  setRefreshing(true);
  await reloadData();
  setRefreshing(false);
}

<FlatList
  data={items}
  renderItem={renderItem}
  refreshing={refreshing}
  onRefresh={handleRefresh}
/>;
```

On a `ScrollView` you pass a `<RefreshControl>` to the `refreshControl` prop.

### 45: How do you load more items when the user reaches the end of a list?

Use `onEndReached` together with `onEndReachedThreshold`:

```tsx
<FlatList
  data={items}
  renderItem={renderItem}
  onEndReached={() => {
    if (!isLoading && hasMore) loadNextPage();
  }}
  onEndReachedThreshold={0.5}
  ListFooterComponent={isLoading ? <ActivityIndicator /> : null}
/>
```

`onEndReachedThreshold={0.5}` means "call it when the user is half a screen away from the end". `onEndReached` can fire more than once, so guard it with a loading flag.

### 46: What is the Platform module?

`Platform` tells you which OS the app runs on, so you can write platform-specific code:

```tsx
import { Platform, StyleSheet } from "react-native";

if (Platform.OS === "ios") {
  // iOS only
}

const styles = StyleSheet.create({
  container: {
    paddingTop: Platform.select({ ios: 20, android: 0, default: 0 }),
  },
});
```

`Platform.OS` can be `'ios'`, `'android'`, `'web'`, `'windows'` or `'macos'`. `Platform.Version` gives the OS version (API level number on Android, a string like `'18.2'` on iOS).

### 47: How do you write platform-specific files?

Add `.ios` or `.android` before the extension, and Metro picks the right file automatically:

```
Button.ios.tsx
Button.android.tsx
```

```tsx
import { Button } from "./Button"; // Metro loads the file for the current platform
```

There is also `.native.tsx`, which is used on iOS and Android but not on web. This is handy when you share code with a web app. Use separate files when the platform code is large. For small differences, `Platform.select` is simpler.

### 48: What is the difference between Dimensions and useWindowDimensions?

Both give you the screen or window size.

- `Dimensions.get('window')` returns the size once. If the user rotates the device or resizes a window (tablets, foldables), you need to subscribe to changes yourself.
- `useWindowDimensions()` is a hook that re-renders your component when the size changes.

```tsx
import { useWindowDimensions } from "react-native";

function Grid() {
  const { width } = useWindowDimensions();
  const columns = width > 600 ? 3 : 2;
  // ...
}
```

Prefer `useWindowDimensions` inside components.

### 49: How do you handle the notch and other safe areas?

Use the `react-native-safe-area-context` library. It gives you a `SafeAreaView` and a `useSafeAreaInsets` hook that work on both iOS and Android:

```tsx
import { SafeAreaView } from "react-native-safe-area-context";

export function Screen() {
  return (
    <SafeAreaView style={{ flex: 1 }} edges={["top", "bottom"]}>
      <Content />
    </SafeAreaView>
  );
}
```

The `SafeAreaView` from `react-native` itself only worked on iOS and was deprecated in 0.81. Expo and React Navigation already include `react-native-safe-area-context`.

### 50: What does the StatusBar component do?

`StatusBar` controls the system bar at the top of the screen: the color of its icons and whether it is visible.

```tsx
import { StatusBar } from "react-native";

<StatusBar barStyle="light-content" hidden={false} />;
```

`barStyle` can be `'default'`, `'light-content'` or `'dark-content'`. Because Android apps now draw edge-to-edge (behind the status bar), the Android-only `backgroundColor` and `translucent` props were removed in 0.87. You color the area behind the status bar with your own views instead. In Expo apps you often use `expo-status-bar`, which has a simpler `style="auto"` option.

### 51: How do you control how an image fits its box?

Use the `resizeMode` prop (or the `objectFit` style, which works like CSS):

- `cover`: fills the box, may crop the image (default)
- `contain`: fits the whole image inside the box, may leave empty space
- `stretch`: stretches to fill, may distort
- `center`: centers without scaling up
- `repeat`: tiles the image

```tsx
<Image
  source={{ uri: url }}
  style={{ width: "100%", height: 200 }}
  resizeMode="cover"
/>
```

### 52: How do you put text on top of an image?

The old way was `ImageBackground`, but it was deprecated in 0.87. The recommended way now is a `View` with an absolutely positioned `Image` behind the content:

```tsx
<View style={{ height: 200 }}>
  <Image source={cover} style={StyleSheet.absoluteFill} resizeMode="cover" />
  <Text style={{ color: "white", margin: 16 }}>Summer sale</Text>
</View>
```

You will still see `ImageBackground` in older code.

### 53: How do you show a loading spinner?

Use `ActivityIndicator`. It shows the native spinner of each platform:

```tsx
import { ActivityIndicator, View } from "react-native";

function Loading() {
  return (
    <View style={{ flex: 1, justifyContent: "center" }}>
      <ActivityIndicator size="large" color="#0066ff" />
    </View>
  );
}
```

`size` can be `'small'`, `'large'` or a number (the number only works on Android).

### 54: What is the Switch component?

`Switch` is the native on/off toggle. It is controlled, so you pass `value` and update it in `onValueChange`:

```tsx
const [enabled, setEnabled] = useState(false);

<Switch
  value={enabled}
  onValueChange={setEnabled}
  trackColor={{ false: "#ccc", true: "#4caf50" }}
/>;
```

### 55: How do you show a modal?

Use the `Modal` component. It covers the current screen with new content:

```tsx
const [visible, setVisible] = useState(false);

<Modal
  visible={visible}
  animationType="slide"
  transparent
  onRequestClose={() => setVisible(false)}
>
  <View style={styles.backdrop}>
    <View style={styles.sheet}>
      <Text>Are you sure?</Text>
      <Button title="Close" onPress={() => setVisible(false)} />
    </View>
  </View>
</Modal>;
```

`onRequestClose` is called when the user presses the Android back button, so always handle it. If you use a navigation library, you can also show screens as modals there.

### 56: How do you show a native alert dialog?

Use `Alert.alert`:

```tsx
import { Alert } from "react-native";

Alert.alert("Delete item", "This cannot be undone.", [
  { text: "Cancel", style: "cancel" },
  { text: "Delete", style: "destructive", onPress: () => deleteItem(id) },
]);
```

It shows the native dialog of each platform. `Alert.prompt` (an alert with a text field) only works on iOS.

### 57: What is KeyboardAvoidingView?

When the keyboard opens, it can cover text inputs near the bottom of the screen. `KeyboardAvoidingView` moves or resizes its content so the input stays visible:

```tsx
<KeyboardAvoidingView
  style={{ flex: 1 }}
  behavior={Platform.OS === "ios" ? "padding" : "height"}
>
  <TextInput placeholder="Message" />
</KeyboardAvoidingView>
```

It often needs tuning per platform (`behavior`, `keyboardVerticalOffset`). Many teams use the `react-native-keyboard-controller` library for more reliable keyboard handling.

### 58: How do you close the keyboard?

Call `Keyboard.dismiss()`. A common pattern is to dismiss it when the user taps outside the input:

```tsx
import { Keyboard, Pressable } from "react-native";

<Pressable style={{ flex: 1 }} onPress={Keyboard.dismiss} accessible={false}>
  <TextInput placeholder="Email" />
</Pressable>;
```

In a `ScrollView`, you can use `keyboardDismissMode="on-drag"` to close the keyboard when the user scrolls.

### 59: How do you show a password field or a number keyboard?

Use `TextInput` props:

```tsx
<TextInput secureTextEntry placeholder="Password" />

<TextInput keyboardType="number-pad" placeholder="Code" />

<TextInput
  keyboardType="email-address"
  autoCapitalize="none"
  autoComplete="email"
  placeholder="Email"
/>
```

Common `keyboardType` values are `default`, `number-pad`, `decimal-pad`, `email-address`, `phone-pad` and `url`.

### 60: What is the difference between onChangeText and onChange on TextInput?

- `onChangeText` gives you the new text as a string. This is what you want most of the time.
- `onChange` gives you a native event object, and the text is in `event.nativeEvent.text`.

```tsx
<TextInput onChangeText={(text) => setValue(text)} />
<TextInput onChange={(e) => setValue(e.nativeEvent.text)} />
```

### 61: How do you open a URL, phone number or email from the app?

Use `Linking.openURL`:

```tsx
import { Linking } from "react-native";

Linking.openURL("https://example.com");
Linking.openURL("tel:+123456789");
Linking.openURL("mailto:support@example.com");
Linking.openSettings(); // opens the app's settings page
```

`Linking.canOpenURL` checks if some app can handle a URL. On iOS you must list custom schemes you want to check in `LSApplicationQueriesSchemes` in `Info.plist`.

### 62: Do React hooks work the same in React Native?

Yes. `useState`, `useEffect`, `useRef`, `useMemo`, `useCallback`, `useContext`, `useReducer`, `useTransition`, `use` and the rest come from the `react` package and work exactly as on the web. React Native also adds a few of its own hooks, like `useWindowDimensions`, `useColorScheme` and `useAnimatedValue`.

The difference is in what you do inside them. For example, you don't touch `document` in a `useEffect`, you subscribe to things like `AppState` or `Keyboard` events instead.

### 63: How do you focus a TextInput from code?

Create a ref with `useRef` and call `focus()` on it:

```tsx
function LoginForm() {
  const passwordRef = useRef<TextInput>(null);

  return (
    <>
      <TextInput
        placeholder="Email"
        returnKeyType="next"
        onSubmitEditing={() => passwordRef.current?.focus()}
      />
      <TextInput ref={passwordRef} placeholder="Password" secureTextEntry />
    </>
  );
}
```

There are also `blur()`, `clear()` and `isFocused()`. With React 19, `ref` is a normal prop, so you don't need `forwardRef` in your own components.

### 64: What is AppRegistry?

`AppRegistry` is how the native side finds your root component. In the entry file you register it by name:

```tsx
import { AppRegistry } from "react-native";
import App from "./App";
import { name as appName } from "./app.json";

AppRegistry.registerComponent(appName, () => App);
```

The native code starts React Native with the same name. In Expo projects you don't write this yourself, `registerRootComponent` or Expo Router does it for you.

### 65: What is the entry point of a React Native app?

In a Community CLI project it is `index.js`, which calls `AppRegistry.registerComponent`. In an Expo project it is set by the `main` field in `package.json`. With Expo Router it is `expo-router/entry`, and your screens live in the `app/` folder. Without Expo Router it is usually `index.ts` calling `registerRootComponent(App)`.

On the native side, iOS starts in `AppDelegate` and Android starts in `MainApplication` and `MainActivity`. They load the JavaScript bundle and start the root component.

### 66: What is Fast Refresh?

Fast Refresh is the React Native feature that updates the app almost instantly when you save a file. It keeps the component state when you only change a component file. If you change a file that is not a component (for example a utility used in many places), it reloads those modules. If there is a syntax error, it shows the error and recovers when you fix it.

It is on by default in development. You can force a component to remount on every edit by adding `// @refresh reset` to the file.

### 67: How do you open the developer menu?

- iOS simulator: `Cmd + D` (or `Ctrl + Cmd + Z`)
- Android emulator: `Cmd + M` on macOS or `Ctrl + M` on Windows/Linux
- Physical device: shake the phone
- From the terminal where Metro runs: press `m` (Expo) or `d` (Community CLI)

The dev menu lets you reload the app, open React Native DevTools, toggle the performance monitor and the element inspector.

### 68: What is React Native DevTools?

React Native DevTools is the official debugger, based on Chrome DevTools. It became the default in 0.76. You open it by pressing `j` in the Metro terminal or from the dev menu. It gives you:

- Console with logs and errors
- Sources with breakpoints and step-by-step debugging
- React Components and Profiler tabs
- Memory heap snapshots
- Network and Performance panels (added in 0.83)

It replaced older tools like Flipper and the remote Chrome debugger, which are no longer supported.

### 69: Where do console.log messages appear?

In development, `console.log` messages show up in:

- The terminal where Metro is running
- The Console tab of React Native DevTools

In release builds they go to the native logs (Logcat on Android, the Xcode console on iOS). Too many logs slow the app down, so many teams remove them in production with a Babel plugin like `babel-plugin-transform-remove-console`.

### 70: What is LogBox?

LogBox is the in-app tool that shows errors and warnings during development.

- Warnings appear as a small notification at the bottom of the screen.
- Errors open a full-screen view with the stack trace and the code frame.
- Syntax errors show the exact location and disappear when you fix them.

You can hide specific warnings with `LogBox.ignoreLogs(['Some warning text'])`, but it is better to fix the cause. LogBox is not included in release builds.

### 71: How do you run the app on a simulator or emulator?

With Expo:

```bash
npx expo run:ios       # builds the native app and starts it in the iOS simulator
npx expo run:android   # same for the Android emulator
npx expo start         # only starts Metro, then press i or a
```

With the Community CLI:

```bash
npx react-native run-ios
npx react-native run-android
```

You need Xcode (macOS only) for the iOS simulator and Android Studio for the Android emulator.

### 72: How do you run the app on a physical device?

- With Expo, start Metro with `npx expo start` and scan the QR code with your development build or Expo Go. The phone and computer should be on the same network (or use `--tunnel`).
- For Android over USB, enable USB debugging on the phone and run `npx expo run:android --device` or `npx react-native run-android`.
- For iOS, connect the iPhone, select it in Xcode or run `npx expo run:ios --device`. You need an Apple developer account for signing.

You can also build with EAS Build and install the build on the device.

### 73: Why do you need Xcode and Android Studio?

React Native apps are real native apps, so they are compiled with the native tools:

- **Xcode** compiles the iOS app, runs the iOS simulator, signs builds and uploads them to App Store Connect. It only runs on macOS.
- **Android Studio** installs the Android SDK, build tools and emulators, and is used to debug native Android code.

If you use EAS Build, the builds run in the cloud, so you can build iOS apps without a Mac. You still need a Mac for the iOS simulator.

### 74: What is CocoaPods and why do you run pod install?

CocoaPods is a dependency manager for iOS. React Native and many libraries ship their iOS native code as pods. After you install a library with native iOS code, you run:

```bash
cd ios && pod install
```

This links the native code into the Xcode project. Expo runs it for you during `npx expo run:ios` or prebuild. React Native 0.87 and 0.88 also added experimental Swift Package Manager support, and the plan is to move toward it as the default.

### 75: What is Gradle in a React Native project?

Gradle is the build system for Android. It downloads native dependencies, compiles Kotlin and Java code, bundles the JavaScript in release builds and produces the APK or AAB file. The main files are:

- `android/build.gradle`: project-wide settings
- `android/app/build.gradle`: app settings like `applicationId`, `versionCode`, signing
- `android/gradle.properties`: flags such as `hermesEnabled`
- `android/settings.gradle`: which modules are included

### 76: What are the ios and android folders?

They contain the native projects: an Xcode workspace in `ios/` and a Gradle project in `android/`. They hold native code, app icons, permissions (`Info.plist`, `AndroidManifest.xml`), signing settings and native dependencies.

In a Community CLI project you edit and commit these folders. In an Expo project using Continuous Native Generation, they are generated from `app.json` and config plugins, so many teams don't commit them at all and add them to `.gitignore`.

### 77: What is app.json or app.config.js in Expo?

It is the main config file of an Expo app. It describes the app: name, slug, version, icon, splash screen, bundle identifier, Android package, permissions, plugins and more.

```json
{
  "expo": {
    "name": "My App",
    "slug": "my-app",
    "version": "1.0.0",
    "icon": "./assets/icon.png",
    "ios": { "bundleIdentifier": "com.example.myapp" },
    "android": { "package": "com.example.myapp" },
    "plugins": ["expo-router"]
  }
}
```

`app.config.js` (or `.ts`) is the same thing but written in JavaScript, so you can read environment variables and change values per build.

### 78: What is Expo prebuild (Continuous Native Generation)?

`npx expo prebuild` generates the `ios` and `android` folders from your `app.json` and config plugins. This approach is called Continuous Native Generation (CNG). Instead of editing native files by hand, you describe what you need in config, and the native projects can be thrown away and regenerated at any time.

Benefits: upgrades are easier, there are fewer merge conflicts in native files, and native settings are kept in one place. When you need custom native changes, you write a config plugin or a local Expo module.

### 79: What options do you have for navigation in React Native?

React Native does not include navigation. The two main options are:

- **React Navigation**: the most used library. You define navigators (stack, tabs, drawer) in code.
- **Expo Router**: file-based routing built on top of React Navigation. Each file in the `app/` folder becomes a screen, and it supports deep links and web URLs automatically.

Both use native screen containers (`react-native-screens`) for good performance. New Expo projects use Expo Router by default.

### 80: How do you create a stack navigator with React Navigation?

A stack navigator shows one screen on top of another, with a back button and the native push animation:

```tsx
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import { createStaticNavigation } from "@react-navigation/native";

const RootStack = createNativeStackNavigator({
  screens: {
    Home: HomeScreen,
    Profile: ProfileScreen,
  },
});

const Navigation = createStaticNavigation(RootStack);

export default function App() {
  return <Navigation />;
}
```

This is the static API added in React Navigation 7. The older dynamic API with `<NavigationContainer>` and `<Stack.Screen>` components still works and is very common.

### 81: How do you navigate between screens and pass parameters?

Use the `navigation` object from the `useNavigation` hook, and read params with `useRoute` (or the `route` prop):

```tsx
function HomeScreen() {
  const navigation = useNavigation();
  return (
    <Button
      title="Open profile"
      onPress={() => navigation.navigate("Profile", { userId: "42" })}
    />
  );
}

function ProfileScreen() {
  const route = useRoute();
  const { userId } = route.params as { userId: string };
  return <Text>User {userId}</Text>;
}
```

Other common methods: `goBack()`, `push()` (adds a new screen even if the same route is already open), `replace()`, `popToTop()` and `setOptions()`.

### 82: What is a tab navigator?

A tab navigator shows a tab bar (usually at the bottom) and switches between screens when the user taps a tab:

```tsx
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";

const Tabs = createBottomTabNavigator({
  screens: {
    Feed: FeedScreen,
    Search: SearchScreen,
    Settings: SettingsScreen,
  },
});
```

Each tab keeps its state when you switch away. You can set icons with the `tabBarIcon` option. There is also a native tabs option (in React Navigation and Expo Router) that uses the real platform tab bar.

### 83: What is a drawer navigator?

A drawer navigator has a side menu that slides in from the edge of the screen. It comes from `@react-navigation/drawer` and needs `react-native-gesture-handler` and `react-native-reanimated`:

```tsx
import { createDrawerNavigator } from "@react-navigation/drawer";

const Drawer = createDrawerNavigator({
  screens: {
    Home: HomeScreen,
    Orders: OrdersScreen,
  },
});
```

You open it with a swipe or by calling `navigation.openDrawer()`.

### 84: What is Expo Router?

Expo Router is a file-based router for React Native and web. Files in the `app/` folder become routes:

```
app/
  _layout.tsx        -> root layout (for example a Stack)
  index.tsx          -> "/"
  settings.tsx       -> "/settings"
  user/[id].tsx      -> "/user/42"
  (tabs)/_layout.tsx -> a tab navigator group
```

You navigate with `<Link href="/settings">` or `router.push('/user/42')`, and read params with `useLocalSearchParams()`. Every screen gets a URL, so deep linking works without extra config. It is built on top of React Navigation.

### 85: How do you fetch data from an API in React Native?

`fetch` is available globally, just like in the browser:

```tsx
function Users() {
  const [users, setUsers] = useState<User[]>([]);

  useEffect(() => {
    let ignore = false;
    fetch("https://api.example.com/users")
      .then((res) => res.json())
      .then((data) => {
        if (!ignore) setUsers(data);
      });
    return () => {
      ignore = true;
    };
  }, []);

  return (
    <FlatList
      data={users}
      renderItem={({ item }) => <Text>{item.name}</Text>}
    />
  );
}
```

In real apps most teams use a data library like TanStack Query, which handles caching, loading states and refetching.

### 86: Can you use axios, WebSockets and XMLHttpRequest in React Native?

Yes. React Native provides `fetch`, `XMLHttpRequest` and `WebSocket` globally. Libraries built on these, like axios, work without changes. `AbortController` also works for cancelling requests.

What does not work is anything that depends on Node.js modules (`fs`, `http`, `net`) or browser DOM APIs. Also, on Android plain `http://` requests are blocked by default in release builds, and iOS App Transport Security blocks them too, so use `https`.

### 87: How do you show loading and error states for a request?

Keep track of them in state and render different UI:

```tsx
function Profile({ id }: { id: string }) {
  const [data, setData] = useState<User | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch(`https://api.example.com/users/${id}`)
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json();
      })
      .then(setData)
      .catch((e) => setError(e.message));
  }, [id]);

  if (error) return <Text>Something went wrong: {error}</Text>;
  if (!data) return <ActivityIndicator />;
  return <Text>{data.name}</Text>;
}
```

Remember that `fetch` does not throw on HTTP errors like 404 or 500. You must check `res.ok` yourself.

### 88: What is AsyncStorage?

AsyncStorage is a simple key-value storage that saves strings on the device. It is not part of React Native core anymore. You install `@react-native-async-storage/async-storage`:

```tsx
import AsyncStorage from "@react-native-async-storage/async-storage";

await AsyncStorage.setItem("theme", "dark");
const theme = await AsyncStorage.getItem("theme");
await AsyncStorage.removeItem("theme");

await AsyncStorage.setItem("user", JSON.stringify(user));
```

It is asynchronous and not encrypted, so use it for settings and small cached data, not for tokens or passwords.

### 89: How do you store sensitive data like tokens?

Use the secure storage of the OS: Keychain on iOS and Keystore-backed encrypted storage on Android. Popular libraries:

- `expo-secure-store`
- `react-native-keychain`

```tsx
import * as SecureStore from "expo-secure-store";

await SecureStore.setItemAsync("accessToken", token);
const saved = await SecureStore.getItemAsync("accessToken");
```

Never store tokens in AsyncStorage or plain files, because they are not encrypted.

### 90: Which state management options are common in React Native?

The same as in React web apps:

- `useState`, `useReducer` and Context for local and small shared state
- Zustand, Redux Toolkit or Jotai for global client state
- TanStack Query, RTK Query or Apollo Client for server data

Mobile apps often also need to persist state between launches, so these are combined with storage like MMKV or AsyncStorage (for example with Zustand's `persist` middleware or `redux-persist`).

### 91: How do you use Context in React Native?

Exactly like on the web. Create a context, wrap part of the tree in a provider, and read it with `use` or `useContext`:

```tsx
const ThemeContext = createContext<"light" | "dark">("light");

export default function App() {
  const scheme = useColorScheme() ?? "light";
  return (
    <ThemeContext value={scheme}>
      <HomeScreen />
    </ThemeContext>
  );
}

function Title() {
  const theme = use(ThemeContext);
  return (
    <Text style={{ color: theme === "dark" ? "white" : "black" }}>Hi</Text>
  );
}
```

In React 19 you can render `<ThemeContext>` directly as the provider. `<ThemeContext.Provider>` still works.

### 92: What was the "bridge" in React Native?

In the old architecture, JavaScript and native code talked through the bridge. Every call between them was turned into a JSON message, put in a queue and sent across asynchronously in batches.

It worked, but it had problems: serializing to JSON was slow, every call was async (so you couldn't read native values synchronously), and heavy traffic, like scroll events, could block the queue. The New Architecture replaced the bridge with JSI, which lets JavaScript call native code directly.

### 93: What is the New Architecture?

The New Architecture is the modern internals of React Native. It became the default in 0.76 and the only option from 0.82. It has a few parts:

- **JSI**: a C++ interface that lets JavaScript call native functions directly, without the bridge
- **Fabric**: the new rendering system, written mostly in C++
- **Turbo Modules**: the new native modules, loaded lazily and called through JSI
- **Codegen**: generates typed native code from TypeScript specs
- **Bridgeless mode**: the old bridge is removed completely

For app developers the main benefits are better performance, synchronous layout reads, and support for React's concurrent features like transitions and Suspense.

### 94: Can you still use the old architecture?

No. Since React Native 0.82 the old architecture can't be turned on, and from 0.84 much of the legacy code was removed from the build. Libraries that only support the old architecture work through interop layers in some cases, but you should replace or update them. The React Native Directory (reactnative.directory) shows which libraries support the New Architecture.

### 95: What is a native module?

A native module is native code (Swift, Kotlin, Objective-C, Java or C++) that you can call from JavaScript. You use it when JavaScript alone can't do the job, for example to access a device sensor, a platform SDK or a heavy native library.

In the New Architecture these are called Turbo Modules. Expo also has its own Expo Modules API, which is an easier way to write native modules in Swift and Kotlin. Most of the time you don't write them yourself, you install libraries that already include them.

### 96: What is a native component?

A native component is a native UI view (like a map view, a video player or a chart view written in Swift or Kotlin) that you can render from React as a normal component:

```tsx
<MapView region={region} onRegionChange={setRegion} />
```

The props you pass in JavaScript are applied to the native view. In the New Architecture they are called Fabric native components. You can write them with Codegen or with the Expo Modules API.

### 97: What is autolinking?

Autolinking means you don't have to manually connect the native code of a library to your app. When you install a library that has native code, the build tools find it in `node_modules` and add it to the iOS and Android projects automatically during `pod install` or the Gradle build.

Before autolinking (React Native 0.60), you had to run `react-native link` or edit native files by hand. Expo has its own autolinking for Expo modules, which works alongside the React Native one.

### 98: How do you install a library in an Expo project?

Use `npx expo install` instead of plain `npm install`:

```bash
npx expo install expo-camera react-native-reanimated
```

It picks the versions that are compatible with your Expo SDK version. If the library has native code, you need to rebuild your development build (it can't be added to an app that's already built). `npx expo install --check` checks your installed versions and `--fix` updates them.

### 99: How do you add a ripple effect on Android?

`Pressable` has an `android_ripple` prop:

```tsx
<Pressable
  android_ripple={{ color: "rgba(0,0,0,0.1)", borderless: false }}
  onPress={onPress}
  style={{ padding: 16 }}
>
  <Text>Settings</Text>
</Pressable>
```

On iOS there is no ripple, so you usually combine it with a pressed style, for example lowering the opacity when `pressed` is true.

### 100: What is hitSlop?

`hitSlop` makes the touchable area bigger than the visible element. This helps when an icon is small but you want it to be easy to tap:

```tsx
<Pressable hitSlop={12} onPress={onClose}>
  <CloseIcon size={16} />
</Pressable>

<Pressable hitSlop={{ top: 10, bottom: 10, left: 20, right: 20 }} onPress={onClose} />
```

Apple recommends touch targets of at least 44x44 points, and Android recommends 48x48 dp.

### 101: How do you make a component accessible to screen readers?

Use the accessibility props. The basic ones are:

- `accessible`: groups the children into one element for the screen reader
- `accessibilityLabel`: what the screen reader says
- `accessibilityHint`: extra info about what happens on press
- `accessibilityRole`: what kind of element it is (`button`, `header`, `link`, `image` and so on)

```tsx
<Pressable
  accessibilityRole="button"
  accessibilityLabel="Add to cart"
  accessibilityHint="Adds this product to your shopping cart"
  onPress={addToCart}
>
  <CartIcon />
</Pressable>
```

Icon-only buttons always need a label, because there is no text to read. Screen readers are VoiceOver on iOS and TalkBack on Android.

### 102: What are the role and aria-* props in React Native?

React Native supports web-like accessibility props as an alternative to the `accessibility*` props:

```tsx
<Pressable
  role="button"
  aria-label="Close"
  aria-disabled={isDisabled}
  aria-expanded={isOpen}
  onPress={onClose}
/>
```

`role` maps to `accessibilityRole`, `aria-label` to `accessibilityLabel`, and `aria-checked`, `aria-selected`, `aria-busy` and `aria-expanded` map to `accessibilityState`. They are handy if you share code with the web, because they use the same names as HTML.

### 103: How do you support dark mode?

Read the user's system setting with the `useColorScheme` hook and pick colors based on it:

```tsx
import { useColorScheme } from "react-native";

function Screen() {
  const scheme = useColorScheme(); // 'light' | 'dark' | null
  const isDark = scheme === "dark";

  return (
    <View style={{ flex: 1, backgroundColor: isDark ? "#000" : "#fff" }}>
      <Text style={{ color: isDark ? "#fff" : "#000" }}>Hello</Text>
    </View>
  );
}
```

The hook re-renders when the user changes the setting. In Expo apps, set `"userInterfaceStyle": "automatic"` in `app.json`, otherwise the app stays in light mode.

### 104: What is the Appearance API?

`Appearance` is the module behind `useColorScheme`. You can read the scheme outside a component, listen for changes, or force a scheme for your app:

```tsx
import { Appearance } from "react-native";

const scheme = Appearance.getColorScheme();

const sub = Appearance.addChangeListener(({ colorScheme }) => {
  console.log("Scheme changed to", colorScheme);
});
sub.remove();

Appearance.setColorScheme("dark"); // force dark, 'auto' to follow the system
```

`setColorScheme` is useful when the app has its own "light / dark / system" setting.

### 105: What is AppState?

`AppState` tells you if the app is in the foreground or background. The values are `active`, `background` and `inactive` (iOS only, for example during a phone call or when the app switcher is open).

```tsx
useEffect(() => {
  const sub = AppState.addEventListener("change", (state) => {
    if (state === "active") {
      refreshData();
    }
  });
  return () => sub.remove();
}, []);
```

It is often used to refresh data, pause videos, or lock the app when the user comes back.

### 106: How do you handle the Android back button?

Use `BackHandler`. Return `true` from the listener to stop the default behavior (going back or closing the app):

```tsx
useEffect(() => {
  const sub = BackHandler.addEventListener("hardwareBackPress", () => {
    if (isEditing) {
      confirmDiscardChanges();
      return true;
    }
    return false;
  });
  return () => sub.remove();
}, [isEditing]);
```

Navigation libraries already handle the back button. In React Navigation you can also use the `usePreventRemove` hook to stop the user from leaving a screen with unsaved changes.

### 107: How do you open the native share sheet?

Use the `Share` API:

```tsx
import { Share } from "react-native";

async function shareArticle() {
  await Share.share({
    message: "Check out this article",
    url: "https://example.com/article/1", // iOS only
    title: "Article", // Android only
  });
}
```

For sharing files (images, PDFs), use a library like `expo-sharing` or `react-native-share`.

### 108: What is PixelRatio?

`PixelRatio` gives you the device pixel density. `PixelRatio.get()` returns values like `2` or `3` on iPhones and anything from about `1` to `4` on Android. It is useful when you request images from a server and want the right resolution:

```tsx
const size = PixelRatio.getPixelSizeForLayoutSize(100); // 100 dp in real pixels
const imageUrl = `https://cdn.example.com/photo.jpg?w=${size}`;
```

`PixelRatio.getFontScale()` returns the user's font size setting. `PixelRatio.roundToNearestPixel()` helps avoid blurry 1px lines.

### 109: How do you do animations in React Native?

There are a few options:

- **Animated**: the built-in API for animating values with timing, spring and decay
- **LayoutAnimation**: built-in, animates the next layout change automatically
- **Reanimated**: the most popular library, runs animations on the UI thread and supports gestures well
- **Lottie** (`lottie-react-native`): plays animations exported from After Effects

A simple fade-in with `Animated`:

```tsx
function FadeIn({ children }: { children: React.ReactNode }) {
  const opacity = useAnimatedValue(0);

  useEffect(() => {
    Animated.timing(opacity, {
      toValue: 1,
      duration: 300,
      useNativeDriver: true,
    }).start();
  }, []);

  return <Animated.View style={{ opacity }}>{children}</Animated.View>;
}
```

### 110: What does useNativeDriver do?

With `useNativeDriver: true`, React Native sends the whole animation to the native side before it starts. Then each frame is calculated on the UI thread, not in JavaScript. The animation stays smooth even if the JavaScript thread is busy.

For a long time the native driver only supported non-layout props like `opacity` and `transform`. Since 0.85, the new Shared Animation Backend also lets `Animated` animate layout props like `width`, `height` and `flex` with the native driver (opt-in at first). You should use `useNativeDriver: true` whenever it is supported.

### 111: What is LayoutAnimation?

`LayoutAnimation` animates the next layout change automatically. You call it right before a state update that changes layout:

```tsx
import { LayoutAnimation } from "react-native";

function toggle() {
  LayoutAnimation.configureNext(LayoutAnimation.Presets.easeInEaseOut);
  setExpanded((v) => !v);
}
```

All views that move, appear or change size in that render will animate. It is simple, but you have little control. Reanimated layout animations (`entering`, `exiting`, `layout`) give more control.

### 112: What is Reanimated?

`react-native-reanimated` (by Software Mansion) is the most popular animation library for React Native. Animations run on the UI thread using small JavaScript functions called worklets, so they stay smooth even when the JS thread is busy.

```tsx
import Animated, {
  useSharedValue,
  useAnimatedStyle,
  withSpring,
} from "react-native-reanimated";

function Box() {
  const offset = useSharedValue(0);
  const style = useAnimatedStyle(() => ({
    transform: [{ translateX: offset.value }],
  }));

  return (
    <Pressable onPress={() => (offset.value = withSpring(offset.value + 50))}>
      <Animated.View
        style={[{ width: 80, height: 80, backgroundColor: "tomato" }, style]}
      />
    </Pressable>
  );
}
```

Reanimated 4 only supports the New Architecture and adds CSS-like animations and transitions.

### 113: What is React Native Gesture Handler?

`react-native-gesture-handler` handles touch gestures (pan, pinch, rotation, tap, long press, fling) on the native side instead of in JavaScript. This makes gestures more responsive and lets them work together with native scroll views.

```tsx
import { Gesture, GestureDetector } from "react-native-gesture-handler";

const tap = Gesture.Tap()
  .numberOfTaps(2)
  .onEnd(() => {
    console.log("double tap");
  });

<GestureDetector gesture={tap}>
  <Animated.View style={styles.box} />
</GestureDetector>;
```

The app root must be wrapped in `GestureHandlerRootView`. It is used by React Navigation, bottom sheets and many other libraries.

### 114: How do you use icons in React Native?

The most common options:

- `@expo/vector-icons`: comes with Expo, includes Ionicons, MaterialIcons, FontAwesome and others
- `react-native-vector-icons` (now split into per-family packages under `@react-native-vector-icons/*`)
- SVG icons with `react-native-svg`
- SF Symbols on iOS with `expo-symbols`

```tsx
import Ionicons from "@expo/vector-icons/Ionicons";

<Ionicons name="heart" size={24} color="red" />;
```

Icon fonts are small and fast. SVG icons are more flexible when you have custom designs.

### 115: How do you render SVG in React Native?

React Native can't render SVG out of the box. Use the `react-native-svg` library:

```tsx
import Svg, { Circle, Path } from "react-native-svg";

<Svg width={24} height={24} viewBox="0 0 24 24">
  <Circle cx={12} cy={12} r={10} stroke="black" strokeWidth={2} fill="none" />
  <Path d="M8 12h8" stroke="black" strokeWidth={2} />
</Svg>;
```

To import `.svg` files as components, add `react-native-svg-transformer` to the Metro config. `expo-image` can also display SVG files as images.

### 116: How do you use environment variables in React Native?

In Expo, variables that start with `EXPO_PUBLIC_` in a `.env` file are put into the JavaScript bundle at build time:

```bash
# .env
EXPO_PUBLIC_API_URL=https://api.example.com
```

```tsx
const apiUrl = process.env.EXPO_PUBLIC_API_URL;
```

Without Expo, teams often use `react-native-config` or `react-native-dotenv`. Remember that anything in the bundle can be read by someone who unpacks the app, so never put secret keys there.

### 117: What is `__DEV__`?

`__DEV__` is a global boolean that is `true` in development and `false` in release builds. You can use it to run code only during development:

```tsx
if (__DEV__) {
  console.log("Debug info", data);
}
```

In release builds Metro replaces `__DEV__` with `false`, and the minifier removes the dead code.

### 118: What is the difference between a debug build and a release build?

**Debug build:**

- Loads JavaScript from the Metro dev server
- Has Fast Refresh, the dev menu, LogBox and DevTools
- Runs slower, with extra checks and warnings

**Release build:**

- Contains the JavaScript bundle inside the app (compiled to Hermes bytecode)
- No dev tools, `__DEV__` is `false`
- Minified and optimized, much faster

Always test performance in a release build. Debug builds can be several times slower and give you a wrong picture.

### 119: What is the difference between an APK and an AAB?

- **APK** (Android Package) is the file you can install directly on a device. Good for testing and side loading.
- **AAB** (Android App Bundle) is the format you upload to Google Play. Google Play then creates optimized APKs for each device (only the right CPU architecture, screen density and language), so downloads are smaller.

Google Play requires AAB for new apps. You build it with `./gradlew bundleRelease`, or EAS Build does it for you.

### 120: How do you publish an iOS app?

1. Create an App ID and a distribution certificate and provisioning profile in your Apple Developer account.
2. Create the app record in App Store Connect.
3. Build an archive (`.ipa`) in Xcode (Product > Archive) or with `eas build --platform ios`.
4. Upload it to App Store Connect (Xcode, Transporter or `eas submit`).
5. Test it with TestFlight.
6. Fill in the store listing and privacy details, and submit it for review.

You need a paid Apple Developer Program membership.

### 121: What is code signing?

Code signing proves that the app comes from you and was not changed. Both stores require it.

- **Android**: you sign the app with a keystore file. With Play App Signing, Google keeps the final app signing key and you sign uploads with an upload key.
- **iOS**: you need a certificate and a provisioning profile from Apple that link your team, the app ID and (for development) the allowed devices.

If you lose the Android upload key you can reset it through Google, but you must keep keys and passwords safe and out of git. EAS can create and store credentials for you.

### 122: How do you set the app icon and splash screen?

In Expo, set them in `app.json` and the files are generated for each platform:

```json
{
  "expo": {
    "icon": "./assets/icon.png",
    "plugins": [
      [
        "expo-splash-screen",
        {
          "image": "./assets/splash-icon.png",
          "imageWidth": 200,
          "backgroundColor": "#ffffff"
        }
      ]
    ]
  }
}
```

Without Expo you add icons to the asset catalog in Xcode and the `mipmap` folders on Android, and set up the splash screen with a library like `react-native-bootsplash`. Android 12+ has a system splash screen API, so the splash screen is always an icon on a background color.

### 123: How do permissions work in a React Native app?

Sensitive features like camera, location, contacts and notifications need the user's permission. There are two parts:

1. **Declare** the permission in native config: a usage description string in `Info.plist` on iOS, and a `<uses-permission>` entry in `AndroidManifest.xml` on Android. In Expo you set this in `app.json` or through the library's config plugin.
2. **Request** it at runtime with the library's API:

```tsx
import { useCameraPermissions } from "expo-camera";

const [permission, requestPermission] = useCameraPermissions();

if (!permission?.granted) {
  return <Button title="Allow camera" onPress={requestPermission} />;
}
```

Without Expo, `react-native-permissions` is the common choice. On Android there is also the built-in `PermissionsAndroid` API.

### 124: How do you use device features like the camera or location?

Through libraries that wrap the native APIs. Common choices:

- Camera: `expo-camera` or `react-native-vision-camera`
- Location: `expo-location`
- Image picker: `expo-image-picker`
- Contacts: `expo-contacts`
- Sensors: `expo-sensors`
- Haptics: `expo-haptics`

```tsx
import * as Location from "expo-location";

const { status } = await Location.requestForegroundPermissionsAsync();
if (status === "granted") {
  const position = await Location.getCurrentPositionAsync();
  console.log(position.coords.latitude, position.coords.longitude);
}
```

### 125: How do push notifications work in a React Native app?

Push notifications are delivered by Apple Push Notification service (APNs) on iOS and Firebase Cloud Messaging (FCM) on Android. The flow:

1. The app asks the user for permission.
2. The app gets a device push token and sends it to your server.
3. Your server sends a message to APNs/FCM (or to a service like the Expo Push Service) with that token.
4. The OS shows the notification, even if the app is closed.

Common libraries are `expo-notifications` and `@react-native-firebase/messaging`. Push notifications need a development build. They don't work in the iOS simulator in all cases, so test on real devices.

### 126: What are over-the-air (OTA) updates?

OTA updates let you push a new JavaScript bundle and assets to users without releasing a new version to the app stores. The app downloads the update and uses it on the next launch (or right away, if you choose).

You can only update JavaScript and assets this way. Any change to native code (new native libraries, permissions, SDK upgrades) still needs a store release. The main service is EAS Update (`expo-updates`). Microsoft's CodePush was retired together with App Center in 2025.

### 127: What is EAS?

EAS (Expo Application Services) is a cloud service from Expo. Its main parts:

- **EAS Build**: builds iOS and Android apps in the cloud, and manages signing credentials
- **EAS Submit**: uploads builds to the App Store and Google Play
- **EAS Update**: over-the-air updates
- **EAS Workflows**: CI/CD pipelines for these steps

```bash
npm install -g eas-cli
eas build --platform all --profile production
eas submit --platform ios
eas update --channel production --message "Fix login bug"
```

It has a free tier and paid plans. You can use it with any React Native app, not only Expo-created ones.

### 128: How do you set up Jest for a React Native project?

New projects come with Jest already configured. The React Native preset mocks native modules so tests can run in Node:

```js
// jest.config.js
module.exports = {
  preset: "@react-native/jest-preset",
};
```

Since 0.85 the preset is in its own package, `@react-native/jest-preset`, instead of `preset: 'react-native'`. Expo projects use the `jest-expo` preset instead.

### 129: What is React Native Testing Library?

React Native Testing Library (`@testing-library/react-native`) is the standard library for testing components. It renders components and lets you find elements the way a user would, by text, role or label:

```tsx
import { render, screen, userEvent } from "@testing-library/react-native";

test("increments the counter", async () => {
  const user = userEvent.setup();
  render(<Counter />);

  await user.press(screen.getByRole("button", { name: "Increment" }));

  expect(screen.getByText("Count: 1")).toBeOnTheScreen();
});
```

It encourages testing behavior instead of implementation details. Matchers like `toBeOnTheScreen` are built in since v12.4.

### 130: Which tools are used for end-to-end testing in React Native?

- **Maestro**: you write flows in simple YAML files. Easy to start and works with any app build.
- **Detox**: by Wix, tests are written in JavaScript and it syncs with the app, so it waits for animations and network requests automatically.
- **Appium**: general mobile automation tool, slower but works with many languages.

A small Maestro flow:

```yaml
appId: com.example.myapp
---
- launchApp
- tapOn: "Email"
- inputText: "test@example.com"
- tapOn: "Log in"
- assertVisible: "Welcome"
```

### 131: How do you set up linting and formatting?

New projects include ESLint (with flat config, `eslint.config.js`) and Prettier. Community CLI projects use `@react-native/eslint-config`. Expo projects can use `eslint-config-expo`:

```bash
npx expo lint
```

The React hooks rules (`eslint-plugin-react-hooks`) are important, because they catch missing dependencies and hooks called in the wrong place. Many teams add a pre-commit hook with Husky and lint-staged so lint and format run before every commit.

### 132: How do you limit text to a certain number of lines?

Use `numberOfLines`, and `ellipsizeMode` to choose where the "..." goes:

```tsx
<Text numberOfLines={2} ellipsizeMode="tail">
  {article.summary}
</Text>
```

`ellipsizeMode` can be `head`, `middle`, `tail` (default) or `clip`. `adjustsFontSizeToFit` can shrink the font to fit the space instead.

### 133: Can you make part of a Text pressable?

Yes. Nested `Text` components can have their own `onPress`:

```tsx
<Text>
  By signing up you agree to our{" "}
  <Text style={{ color: "blue" }} onPress={() => Linking.openURL(termsUrl)}>
    Terms of Service
  </Text>
  .
</Text>
```

Since 0.84, a `Text` with `onPress` gets the `link` accessibility role automatically. Use `selectable` on a `Text` to let users select and copy it.

### 134: How do you make a horizontal or paging ScrollView?

Use the `horizontal` and `pagingEnabled` props:

```tsx
const { width } = useWindowDimensions();

<ScrollView horizontal pagingEnabled showsHorizontalScrollIndicator={false}>
  {slides.map((slide) => (
    <View key={slide.id} style={{ width }}>
      <Text>{slide.title}</Text>
    </View>
  ))}
</ScrollView>;
```

`pagingEnabled` stops on each page of the scroll view's width. For snapping to items of a custom size, use `snapToInterval` or `snapToOffsets`. `FlatList` supports the same props.

### 135: When should you use ScrollView and when FlatList?

- **ScrollView** renders all children at once. Use it for content that is short and fixed, like a form, a profile or a settings page.
- **FlatList** virtualizes. Use it for long lists, lists from an API, or lists that can grow.

If you put a large list in a `ScrollView`, the screen takes longer to show and uses more memory. If you use a `FlatList` for a simple form, you get more complexity for no benefit.

### 136: What is the difference between style and contentContainerStyle on a ScrollView?

- `style` applies to the scroll view itself, the outer box that has a fixed size on screen.
- `contentContainerStyle` applies to the inner container that holds the children and scrolls.

```tsx
<ScrollView
  style={{ flex: 1, backgroundColor: "#fff" }}
  contentContainerStyle={{ padding: 16, gap: 12 }}
>
  {children}
</ScrollView>
```

Padding and `justifyContent` usually belong in `contentContainerStyle`. If you want short content centered and long content scrollable, use `contentContainerStyle={{ flexGrow: 1, justifyContent: 'center' }}`.

### 137: What is expo-image and why use it instead of Image?

`expo-image` is an image component from Expo that is faster and has more features than the core `Image`:

- Memory and disk caching
- Placeholders, including blurhash and thumbhash
- Smooth transitions when the image loads
- Support for many formats: WebP, AVIF, HEIC, animated GIF, SVG

```tsx
import { Image } from "expo-image";

<Image
  source={{ uri: photoUrl }}
  placeholder={{ blurhash: "LKO2?U%2Tw=w]~RBVZRi};RPxuwH" }}
  contentFit="cover"
  transition={200}
  style={{ width: 300, height: 200 }}
/>;
```

It works in any React Native app. `react-native-fast-image` was popular before, but it is not well maintained anymore.

### 138: What is React Native Web?

React Native Web is a library that implements React Native components and APIs for the browser using `react-dom`. `<View>` becomes a `<div>`, `<Text>` becomes a `<span>` or `<div>`, and styles become CSS.

It lets you run the same components on iOS, Android and web. Expo uses it for web support, so `npx expo start --web` runs your app in the browser. Not every native library supports web, so you sometimes need `.web.tsx` files.

### 139: How do you upgrade React Native to a new version?

- **Expo projects**: run `npx expo install expo@latest --fix` to upgrade the SDK and all related packages, then follow the SDK release notes. With CNG you regenerate the native folders.
- **Community CLI projects**: use the React Native Upgrade Helper website. It shows a diff of every file that changed between two versions, and you apply the changes to your `ios` and `android` folders.

Always read the release blog post for breaking changes, update libraries at the same time, and upgrade one or two versions at a time if you are far behind.

### 140: Why are keys important in lists?

Keys help React match list items between renders. With stable keys, React knows which item was added, removed or moved, and keeps each item's state (like a text input value or an animation) with the right item.

```tsx
{
  todos.map((todo) => <TodoRow key={todo.id} todo={todo} />);
}
```

Using the array index as a key causes bugs when the list is reordered or items are removed. In `FlatList`, keys come from `keyExtractor`.

### 141: Which web APIs are available in React Native?

React Native provides many familiar APIs globally:

- `fetch`, `XMLHttpRequest`, `WebSocket`, `FormData`, `Headers`, `AbortController`
- `setTimeout`, `setInterval`, `requestAnimationFrame`, `requestIdleCallback`, `queueMicrotask`
- `URL` and `URLSearchParams` (much improved in 0.84)
- `console`, `Promise`, `TextEncoder`
- `performance.now()`

There is no `window.document`, no `localStorage`, no `navigator.geolocation` by default, and no Node.js modules like `fs` or `Buffer`. For those you use libraries or polyfills.

### 142: What is Yoga?

Yoga is the layout engine React Native uses. It is a C++ library from Meta that implements Flexbox. When you set `flex`, `padding`, `width` and so on, Yoga calculates the position and size of every view, and then React Native applies those values to the native views.

Because the same engine runs on every platform, a layout looks the same on iOS and Android. Yoga is also used outside React Native, for example in Litho and ComponentKit.

### 143: How do you add shadows?

In current React Native versions you can use `boxShadow`, which works like CSS and is the same on both platforms:

```tsx
<View
  style={{
    padding: 16,
    borderRadius: 12,
    backgroundColor: "white",
    boxShadow: "0 2px 8px rgba(0, 0, 0, 0.15)",
  }}
/>
```

Before `boxShadow` (added in 0.76, New Architecture only), iOS used `shadowColor`, `shadowOffset`, `shadowOpacity` and `shadowRadius`, while Android used `elevation`. You will still see this in a lot of code. Shadows on iOS need a background color to render well.

### 144: What is the JavaScript bundle?

The bundle is a single file that contains all your JavaScript code and the code from `node_modules` you import. Metro builds it.

In development, the app downloads the bundle from Metro (by default on port 8081). In a release build, the bundle is created at build time, compiled to Hermes bytecode and packed inside the app as `main.jsbundle` on iOS or `index.android.bundle` on Android. Images and fonts are copied next to it as assets. OTA updates work by replacing this bundle.

### 145: How do you use transforms like rotate and scale?

Use the `transform` style. It takes an array of transforms (or a CSS-like string):

```tsx
<View
  style={{
    transform: [{ rotate: '45deg' }, { scale: 1.2 }, { translateY: -10 }],
  }}
/>

<View style={{ transform: 'rotate(45deg) scale(1.2)' }} />
```

The order matters, because transforms are applied one after the other. You can also set `transformOrigin`. Transforms don't change the layout of other elements, so they are great for animations.

### 146: How do you provide images for different screen densities?

Add the same image with `@2x` and `@3x` suffixes, and React Native picks the right one for the device:

```
assets/
  logo.png
  logo@2x.png
  logo@3x.png
```

```tsx
<Image source={require("./assets/logo.png")} />
```

This keeps images sharp on high-density screens without loading huge images on small devices. For remote images, request a size that matches the device using `PixelRatio`.

### 147: How do you choose a third-party library for React Native?

Check a few things before adding a library:

- Does it support the New Architecture? (Check reactnative.directory.)
- Is it maintained? Look at recent releases and open issues.
- Does it support the platforms you need (iOS, Android, web)?
- Does it work with Expo? Does it need a config plugin?
- Is there an Expo SDK module that does the same thing?
- How much does it add to the app size?

A library with native code is harder to replace later than a pure JavaScript one, so choose carefully.

### 148: What is the difference between margin and padding in React Native?

The same as in CSS. Padding is the space inside a component, between its border and its content. Margin is the space outside, between the component and its neighbours. Both accept shorthand variants:

```tsx
const styles = StyleSheet.create({
  card: {
    paddingHorizontal: 16,
    paddingVertical: 8,
    marginBottom: 12,
    marginStart: 8, // left in LTR, right in RTL
  },
});
```

`Start` and `End` variants (`marginStart`, `paddingEnd`) flip automatically in right-to-left languages, so they are better than `Left` and `Right` for international apps.

### 149: How does the app load JavaScript during development?

In development, the native app doesn't contain your JavaScript. When it starts, it connects to the Metro dev server (by default `http://localhost:8081`), downloads the bundle and runs it. Metro also keeps a connection open to send Fast Refresh updates when you save files.

On an Android emulator or a USB device, `localhost` points to the device itself, so the tools run `adb reverse tcp:8081 tcp:8081` to forward the port. On a physical device over Wi-Fi, the app uses your computer's IP address.

### 150: How do you check that your environment and project are set up correctly?

There are doctor commands:

```bash
npx react-native doctor   # Community CLI: checks Node, Xcode, Android SDK, JDK, CocoaPods
npx expo-doctor           # Expo: checks package versions, config and known issues
```

They point out common problems like wrong library versions, missing tools or duplicate dependencies. It is a good first step when a build fails after cloning a project or upgrading.

---

## Moderate Questions (151-300)

### 151: Which threads does a React Native app use?

There are three main threads:

- **UI thread (main thread)**: the native thread that draws views and handles touches. Native animations and gestures run here.
- **JavaScript thread**: runs your React code, business logic, event handlers and state updates.
- **Background thread**: in the New Architecture, layout (Yoga) and parts of rendering can run here, so they don't block the UI.

If the JS thread is busy (a heavy loop, a big re-render), touch handlers and JS-driven animations get delayed. If the UI thread is busy, the whole app freezes. Most performance work is about keeping both threads free.

### 152: What does "60 FPS" mean and why does it matter?

Most phones refresh the screen 60 times per second (many newer ones 90 or 120). To look smooth, each frame must be ready in about 16.7 ms at 60 Hz (8.3 ms at 120 Hz). If the work for a frame takes longer, the frame is dropped and the user sees stutter.

In React Native you can see the JS and UI frame rates with the Performance Monitor in the dev menu. If the JS FPS drops, your React code is doing too much. If the UI FPS drops, the native side is overloaded, for example with too many views or large images.

### 153: How do you make a FlatList faster?

Some practical steps:

- Keep `renderItem` items light, and wrap the item component in `React.memo`.
- Use a stable `keyExtractor`.
- Use `getItemLayout` if all rows have the same height.
- Tune `initialNumToRender`, `maxToRenderPerBatch` and `windowSize`.
- Avoid big images that are much larger than the view.
- Don't put heavy logic or anonymous objects in `renderItem` that break memoization.
- Consider FlashList, which recycles views instead of creating new ones.

```tsx
const renderItem = useCallback(
  ({ item }: { item: Product }) => <ProductRow product={item} />,
  [],
);

<FlatList
  data={products}
  renderItem={renderItem}
  keyExtractor={(p) => p.id}
  initialNumToRender={10}
  windowSize={7}
  removeClippedSubviews
/>;
```

### 154: What is getItemLayout and when should you use it?

`getItemLayout` tells `FlatList` the size and position of each item in advance. Without it, the list must render and measure items to know where they are. With it, the list can skip measuring and jump to any index right away.

```tsx
const ITEM_HEIGHT = 72;

<FlatList
  data={messages}
  renderItem={renderItem}
  getItemLayout={(_, index) => ({
    length: ITEM_HEIGHT,
    offset: ITEM_HEIGHT * index,
    index,
  })}
/>;
```

Use it when all items have a fixed height. It also makes `scrollToIndex` reliable.

### 155: What do windowSize, initialNumToRender and maxToRenderPerBatch do?

- `initialNumToRender` (default 10): how many items are rendered on the first render. Make it just enough to fill the screen.
- `maxToRenderPerBatch` (default 10): how many items are rendered in each batch while scrolling.
- `windowSize` (default 21): how many "screens" of content are kept rendered, measured in viewport heights. 21 means 10 screens above, 10 below, plus the visible one.

A smaller `windowSize` uses less memory but may show blank areas when scrolling fast. A larger one is smoother but uses more memory. Tune these with real data on a low-end Android device.

### 156: What is FlashList?

FlashList (`@shopify/flash-list`) is a list component by Shopify with an API very similar to `FlatList`. Instead of destroying and creating item components, it recycles them: when an item scrolls off screen, its component is reused for a new item with new props. This makes scrolling much smoother on large lists.

```tsx
import { FlashList } from "@shopify/flash-list";

<FlashList
  data={products}
  renderItem={({ item }) => <ProductRow product={item} />}
/>;
```

FlashList v2 only supports the New Architecture and no longer needs `estimatedItemSize`. Because items are recycled, you should avoid keeping local state in item components, or reset it when the item changes.

### 157: Does the React Compiler work with React Native?

Yes. The React Compiler is a build-time tool that adds memoization automatically, so you need much less `useMemo`, `useCallback` and `React.memo`. It works in React Native through its Babel plugin, and Expo has built-in support:

```json
{
  "expo": {
    "experiments": {
      "reactCompiler": true
    }
  }
}
```

It is useful in React Native because unnecessary re-renders cost more on low-end phones. It requires code that follows the Rules of React. The ESLint plugin `eslint-plugin-react-hooks` reports code the compiler can't optimize.

### 158: How do you handle forms in React Native?

You can use controlled `TextInput`s with `useState`, but for real forms most teams use React Hook Form. Since there is no native `<form>` element, you wrap inputs with `Controller`:

```tsx
import { useForm, Controller } from "react-hook-form";

function LoginForm() {
  const {
    control,
    handleSubmit,
    formState: { errors },
  } = useForm({
    defaultValues: { email: "", password: "" },
  });

  return (
    <>
      <Controller
        control={control}
        name="email"
        rules={{ required: "Email is required" }}
        render={({ field: { onChange, onBlur, value } }) => (
          <TextInput value={value} onChangeText={onChange} onBlur={onBlur} />
        )}
      />
      {errors.email && <Text>{errors.email.message}</Text>}
      <Button title="Log in" onPress={handleSubmit(onSubmit)} />
    </>
  );
}
```

### 159: How do you validate forms with a schema?

Use a schema library like Zod with the React Hook Form resolver:

```tsx
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";

const schema = z.object({
  email: z.email("Invalid email"),
  password: z.string().min(8, "At least 8 characters"),
});

type FormValues = z.infer<typeof schema>;

const { control, handleSubmit } = useForm<FormValues>({
  resolver: zodResolver(schema),
});
```

The same schema can be shared with your backend or web app, so validation rules stay in one place.

### 160: How do you move focus between inputs and control what the return key does?

Use refs, `returnKeyType` and `onSubmitEditing`. To stop the keyboard from closing when the user presses "next", use `submitBehavior`:

```tsx
const passwordRef = useRef<TextInput>(null);

<TextInput
  placeholder="Email"
  returnKeyType="next"
  submitBehavior="submit"
  onSubmitEditing={() => passwordRef.current?.focus()}
/>
<TextInput
  ref={passwordRef}
  placeholder="Password"
  secureTextEntry
  returnKeyType="done"
  onSubmitEditing={handleLogin}
/>
```

`submitBehavior` replaced the older `blurOnSubmit` prop. Values are `'submit'` (keep focus), `'blurAndSubmit'` and `'newline'` (for multiline inputs).

### 161: How do you support password managers and SMS code autofill?

Set the right autofill props on `TextInput`:

```tsx
<TextInput autoComplete="email" textContentType="emailAddress" keyboardType="email-address" />
<TextInput autoComplete="current-password" textContentType="password" secureTextEntry />
<TextInput autoComplete="sms-otp" textContentType="oneTimeCode" keyboardType="number-pad" />
```

`autoComplete` works on both platforms, `textContentType` is iOS-specific. For iOS password autofill to save credentials for your domain, you also need to set up associated domains (`webcredentials:`) and an `apple-app-site-association` file on your website.

### 162: How do you type navigation params in React Navigation?

With the static API, types can be inferred from the navigator. With the dynamic API, you define a param list type:

```tsx
type RootStackParamList = {
  Home: undefined;
  Profile: { userId: string };
};

const Stack = createNativeStackNavigator<RootStackParamList>();

type ProfileProps = NativeStackScreenProps<RootStackParamList, "Profile">;

function ProfileScreen({ route }: ProfileProps) {
  return <Text>{route.params.userId}</Text>;
}
```

To type `useNavigation()` globally, you declare the root param list once:

```tsx
declare global {
  namespace ReactNavigation {
    interface RootParamList extends RootStackParamList {}
  }
}
```

### 163: What are nested navigators?

A nested navigator is a navigator rendered as a screen inside another navigator. A common setup is a root stack that contains a tab navigator, plus screens that should open above the tabs:

```tsx
const HomeTabs = createBottomTabNavigator({
  screens: { Feed: FeedScreen, Profile: ProfileScreen },
});

const RootStack = createNativeStackNavigator({
  screens: {
    HomeTabs: { screen: HomeTabs, options: { headerShown: false } },
    PostDetails: PostDetailsScreen,
    Settings: SettingsScreen,
  },
});
```

To navigate to a screen in a nested navigator, pass the nested screen in params: `navigation.navigate('HomeTabs', { screen: 'Profile' })`. Keep nesting shallow, because each level adds complexity and its own header and back behavior.

### 164: How do you build an authentication flow with React Navigation?

Render different screens based on whether the user is signed in, instead of navigating manually after login. With the static API you use `if` conditions:

```tsx
const useIsSignedIn = () => useAuth().isSignedIn;
const useIsSignedOut = () => !useAuth().isSignedIn;

const RootStack = createNativeStackNavigator({
  screens: {},
  groups: {
    SignedIn: {
      if: useIsSignedIn,
      screens: { Home: HomeScreen, Profile: ProfileScreen },
    },
    SignedOut: {
      if: useIsSignedOut,
      screens: { SignIn: SignInScreen },
    },
  },
});
```

When the auth state changes, React Navigation switches to the right screens automatically, and the user can't go "back" to the login screen after signing in.

### 165: How do you protect routes in Expo Router?

Expo Router has `Stack.Protected` (and the same for tabs) with a `guard` prop. Screens inside it are only available when the guard is true:

```tsx
// app/_layout.tsx
export default function RootLayout() {
  const { isSignedIn } = useAuth();

  return (
    <Stack>
      <Stack.Protected guard={isSignedIn}>
        <Stack.Screen name="(app)" />
      </Stack.Protected>
      <Stack.Protected guard={!isSignedIn}>
        <Stack.Screen name="sign-in" />
      </Stack.Protected>
    </Stack>
  );
}
```

If the user tries to open a protected screen (for example from a deep link), they are sent to the first available screen. Before protected routes existed, people used `<Redirect>` inside layouts, which you will still see in older code.

### 166: How do you configure deep linking in React Navigation?

With the static API you add a `linking` object to each screen, and enable linking on the navigation container:

```tsx
const RootStack = createNativeStackNavigator({
  screens: {
    Home: { screen: HomeScreen, linking: { path: "" } },
    Profile: { screen: ProfileScreen, linking: { path: "user/:id" } },
  },
});

const Navigation = createStaticNavigation(RootStack);

<Navigation
  linking={{ prefixes: ["myapp://", "https://example.com"], enabled: "auto" }}
/>;
```

Now `myapp://user/42` opens the Profile screen with `id: '42'`. You also need to register the URL scheme in the native config (`scheme` in `app.json` for Expo). Expo Router does all of this automatically from the file structure.

### 167: What is the difference between a custom URL scheme and universal links / app links?

- **Custom scheme** (`myapp://product/1`): easy to set up, but any app can register the same scheme, and it doesn't work if the app isn't installed.
- **Universal links (iOS) / App Links (Android)** (`https://example.com/product/1`): normal web URLs that open the app if it is installed and the website if not. They need verification: an `apple-app-site-association` file and an `assetlinks.json` file on your domain, plus associated domains or intent filters in the app.

For links that users share (emails, social posts), use universal links and App Links.

### 168: How do layouts, groups and dynamic routes work in Expo Router?

- `_layout.tsx` wraps all routes in its folder. It usually renders a navigator like `<Stack />` or `<Tabs />`.
- Folders in parentheses, like `(tabs)` or `(auth)`, are groups. They organize files and can have their own layout, but don't add a part to the URL.
- Square brackets make dynamic segments: `app/product/[id].tsx` matches `/product/123`. `[...rest].tsx` catches any number of segments.

```tsx
// app/product/[id].tsx
import { useLocalSearchParams } from "expo-router";

export default function Product() {
  const { id } = useLocalSearchParams<{ id: string }>();
  return <Text>Product {id}</Text>;
}
```

`+not-found.tsx` handles unknown routes.

### 169: How do you run code when a screen comes into focus?

Screens in a stack or tabs stay mounted when you navigate away, so `useEffect` doesn't run again when the user comes back. Use `useFocusEffect`:

```tsx
import { useFocusEffect } from "@react-navigation/native";
import { useCallback } from "react";

function OrdersScreen() {
  useFocusEffect(
    useCallback(() => {
      const sub = subscribeToOrders();
      return () => sub.unsubscribe(); // runs when the screen loses focus
    }, []),
  );
}
```

`useIsFocused()` returns a boolean if you only need to render differently. Expo Router exports the same `useFocusEffect` hook.

### 170: How do you customize the header of a screen?

Pass `options` to the screen, or call `navigation.setOptions` from inside it:

```tsx
const Stack = createNativeStackNavigator({
  screens: {
    Profile: {
      screen: ProfileScreen,
      options: {
        title: "My profile",
        headerStyle: { backgroundColor: "#111" },
        headerTintColor: "#fff",
      },
    },
  },
});

function ProfileScreen() {
  const navigation = useNavigation();
  useLayoutEffect(() => {
    navigation.setOptions({
      headerRight: () => <Button title="Edit" onPress={openEditor} />,
    });
  }, [navigation]);
}
```

In Expo Router you can render `<Stack.Screen options={{ title: 'My profile' }} />` inside the screen component.

### 171: How do you show a screen as a modal in a navigator?

Set `presentation` in the screen options of a native stack:

```tsx
const RootStack = createNativeStackNavigator({
  screens: {
    Home: HomeScreen,
    NewPost: { screen: NewPostScreen, options: { presentation: "modal" } },
  },
});
```

Other values are `formSheet` (a sheet with detents on iOS and Android), `fullScreenModal` and `transparentModal`. These use real native modal presentation, so the iOS swipe-down to dismiss works.

### 172: What is the difference between the native stack and the JS stack navigator?

- **Native stack** (`@react-navigation/native-stack`) uses the platform's real navigation primitives (`UINavigationController` on iOS, Fragments on Android) through `react-native-screens`. Animations and gestures are native and fast. It is the default choice.
- **Stack** (`@react-navigation/stack`) is implemented in JavaScript with Reanimated and Gesture Handler. It is more customizable (custom transitions, more animation control), but slightly slower.

Use native stack unless you need a transition it can't do.

### 173: How do you use TanStack Query in React Native?

It works the same as on the web, but you should connect it to mobile events, because there are no browser "focus" and "online" events:

```tsx
import { AppState, Platform } from "react-native";
import NetInfo from "@react-native-community/netinfo";
import { focusManager, onlineManager } from "@tanstack/react-query";

onlineManager.setEventListener((setOnline) =>
  NetInfo.addEventListener((state) => setOnline(!!state.isConnected)),
);

useEffect(() => {
  const sub = AppState.addEventListener("change", (status) => {
    if (Platform.OS !== "web") focusManager.setFocused(status === "active");
  });
  return () => sub.remove();
}, []);
```

Now queries refetch when the app comes back to the foreground, and pause when the device is offline. For refetching when a screen gets focus, combine it with `useFocusEffect`.

### 174: How do you detect if the device is online?

Use `@react-native-community/netinfo`:

```tsx
import { useNetInfo } from "@react-native-community/netinfo";

function OfflineBanner() {
  const { isConnected, isInternetReachable } = useNetInfo();

  if (isConnected === false || isInternetReachable === false) {
    return <Text style={styles.banner}>You are offline</Text>;
  }
  return null;
}
```

`isConnected` means there is a network connection. `isInternetReachable` means the internet can actually be reached (a Wi-Fi network without internet has `isConnected: true` but `isInternetReachable: false`). Both can be `null` while unknown.

### 175: What does "offline-first" mean in a mobile app?

An offline-first app reads and writes data to a local store first, and syncs with the server when the network is available. The UI never waits for the network to show data.

Common building blocks:

- A local database (SQLite, WatermelonDB) or a persisted cache (TanStack Query with a persister)
- A queue of pending changes that is sent when back online
- Conflict handling, for example "last write wins" or server-side merging
- Clear UI states for "saved locally" and "synced"

It is more work than an online-only app, but it gives a much better experience on bad mobile networks.

### 176: Which local databases are used in React Native?

- **expo-sqlite**: SQLite with a modern async API, works with Drizzle ORM
- **op-sqlite**: a very fast SQLite library built on JSI
- **WatermelonDB**: built on SQLite, made for large datasets and sync
- **Realm**: an object database. Its sync service (Atlas Device Sync) was deprecated, so fewer teams pick it now.

```tsx
import * as SQLite from "expo-sqlite";

const db = await SQLite.openDatabaseAsync("app.db");
await db.execAsync(
  "CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, text TEXT)",
);
await db.runAsync("INSERT INTO notes (text) VALUES (?)", "Hello");
const notes = await db.getAllAsync<{ id: number; text: string }>(
  "SELECT * FROM notes",
);
```

Always use parameters (`?`) instead of building SQL strings by hand.

### 177: What is MMKV and how is it different from AsyncStorage?

`react-native-mmkv` is a key-value store based on MMKV, a library from WeChat. Compared to AsyncStorage:

- It is synchronous, so you can read values during render or at startup without `await`.
- It is much faster, because it uses JSI and memory-mapped files.
- It supports encryption with a key.

```tsx
import { createMMKV } from "react-native-mmkv";

const storage = createMMKV();
storage.set("onboardingDone", true);
const done = storage.getBoolean("onboardingDone");
```

Older versions used `new MMKV()` instead of `createMMKV()`. It is a good fit for settings and persisted state stores. For tokens, still prefer Keychain/Keystore based storage.

### 178: How do you persist Zustand state in React Native?

Use the `persist` middleware with a storage adapter:

```tsx
import { create } from "zustand";
import { persist, createJSONStorage } from "zustand/middleware";
import AsyncStorage from "@react-native-async-storage/async-storage";

type SettingsState = {
  theme: "light" | "dark";
  setTheme: (theme: "light" | "dark") => void;
};

export const useSettings = create<SettingsState>()(
  persist(
    (set) => ({
      theme: "light",
      setTheme: (theme) => set({ theme }),
    }),
    {
      name: "settings",
      storage: createJSONStorage(() => AsyncStorage),
    },
  ),
);
```

With AsyncStorage the state is loaded asynchronously, so the first render may show default values. You can check `useSettings.persist.hasHydrated()` or use MMKV, which is synchronous.

### 179: How do you use Redux Toolkit with persistence in React Native?

Redux Toolkit works the same as on the web. For persistence, `redux-persist` is the common choice:

```tsx
import { configureStore } from "@reduxjs/toolkit";
import {
  persistStore,
  persistReducer,
  FLUSH,
  REHYDRATE,
  PAUSE,
  PERSIST,
  PURGE,
  REGISTER,
} from "redux-persist";
import AsyncStorage from "@react-native-async-storage/async-storage";

const persisted = persistReducer(
  { key: "root", storage: AsyncStorage, whitelist: ["auth", "settings"] },
  rootReducer,
);

export const store = configureStore({
  reducer: persisted,
  middleware: (getDefault) =>
    getDefault({
      serializableCheck: {
        ignoredActions: [FLUSH, REHYDRATE, PAUSE, PERSIST, PURGE, REGISTER],
      },
    }),
});
export const persistor = persistStore(store);
```

Wrap the app with `<PersistGate persistor={persistor}>` to wait for rehydration. Only persist what you need (whitelist), not caches of server data.

### 180: How do you have different configs for development, staging and production?

In Expo, use `app.config.ts` with an environment variable to change the app name, bundle ID and API URL per build:

```ts
// app.config.ts
const variant = process.env.APP_VARIANT ?? "production";

export default {
  name: variant === "production" ? "MyApp" : `MyApp (${variant})`,
  ios: {
    bundleIdentifier:
      variant === "production"
        ? "com.example.app"
        : `com.example.app.${variant}`,
  },
  android: {
    package:
      variant === "production"
        ? "com.example.app"
        : `com.example.app.${variant}`,
  },
};
```

Then set `APP_VARIANT` per profile in `eas.json`. Different bundle IDs let you install dev, staging and production side by side. In bare projects, you use Android product flavors and iOS schemes or build configurations.

### 181: What is an Expo config plugin?

A config plugin is a function that changes the native project during `npx expo prebuild`. Libraries use them to add permissions, edit `Info.plist` or `AndroidManifest.xml`, add Gradle settings and so on. You add them in `app.json`:

```json
{
  "expo": {
    "plugins": [
      [
        "expo-camera",
        {
          "cameraPermission": "Allow $(PRODUCT_NAME) to use the camera to scan codes."
        }
      ]
    ]
  }
}
```

Because changes are applied by code, they are kept when the native folders are regenerated. You can also write your own plugins for custom native changes.

### 182: What is eas.json?

`eas.json` configures EAS Build and EAS Submit. It has build profiles, for example:

```json
{
  "build": {
    "development": {
      "developmentClient": true,
      "distribution": "internal",
      "env": { "APP_VARIANT": "development" }
    },
    "preview": {
      "distribution": "internal",
      "channel": "preview"
    },
    "production": {
      "autoIncrement": true,
      "channel": "production"
    }
  },
  "submit": {
    "production": {}
  }
}
```

You choose a profile with `eas build --profile preview`. `channel` connects the build to EAS Update, and `autoIncrement` bumps the build number for you.

### 183: How do channels, branches and runtime versions work in EAS Update?

- A **branch** is a list of updates, like a git branch. You publish with `eas update --branch production`.
- A **channel** is set in the build (from `eas.json`). Each channel points to a branch. You can switch which branch a channel points to, for example to roll back.
- **runtimeVersion** describes the native code of a build. An update is only delivered to builds with the same runtime version, so a JS update that needs a new native module never reaches an old binary.

```json
{
  "expo": {
    "runtimeVersion": { "policy": "fingerprint" }
  }
}
```

The `fingerprint` policy computes the runtime version from a hash of your native code and config, so it changes automatically when native code changes.

### 184: What can't you change with an OTA update?

Anything compiled into the native binary:

- Adding or upgrading a library that has native code
- Upgrading React Native or the Expo SDK
- Changing permissions, `Info.plist`, `AndroidManifest.xml` or entitlements
- App icon, splash screen and app name
- Native config like push notification settings

You can change JavaScript, styles and assets (images, fonts) bundled through JavaScript. If you push a JS update that calls a native module the binary doesn't have, the app crashes, which is why runtime versions exist.

### 185: Are OTA updates allowed by Apple and Google?

Yes, with limits. Apple's guidelines allow downloading interpreted code (like JavaScript) as long as it doesn't change the main purpose of the app, add features that would need review, or bypass store rules like in-app purchases. Google Play has similar rules for code that runs in a JavaScript engine or web view.

In practice, OTA updates for bug fixes, text changes and small UI changes are fine. Big new features should go through a normal store release.

### 186: How do you set up push notifications with expo-notifications?

```tsx
import * as Notifications from "expo-notifications";
import * as Device from "expo-device";
import Constants from "expo-constants";

Notifications.setNotificationHandler({
  handleNotification: async () => ({
    shouldShowBanner: true,
    shouldShowList: true,
    shouldPlaySound: false,
    shouldSetBadge: false,
  }),
});

export async function registerForPush() {
  if (!Device.isDevice) return null;

  const { status } = await Notifications.requestPermissionsAsync();
  if (status !== "granted") return null;

  const projectId = Constants.expoConfig?.extra?.eas?.projectId;
  const { data } = await Notifications.getExpoPushTokenAsync({ projectId });
  return data; // send this token to your server
}
```

On Android you also need a notification channel (`setNotificationChannelAsync`) and FCM credentials. On iOS you need APNs credentials, which EAS can create for you. If you want to talk to APNs/FCM directly, use `getDevicePushTokenAsync` instead.

### 187: How do you handle the user tapping a notification?

Listen for notification responses and navigate based on the data in the notification:

```tsx
useEffect(() => {
  const sub = Notifications.addNotificationResponseReceivedListener(
    (response) => {
      const url = response.notification.request.content.data?.url;
      if (typeof url === "string") router.push(url);
    },
  );
  return () => sub.remove();
}, []);
```

If the app was closed when the user tapped, the listener may not be registered yet. Use `Notifications.useLastNotificationResponse()` or `getLastNotificationResponseAsync()` on startup to handle that case. Putting a URL in the notification data and handling it like a deep link keeps the logic in one place.

### 188: How do you run tasks in the background?

Mobile OSs strictly limit background work. Options:

- `expo-background-task`: schedules short periodic tasks. It uses `WorkManager` on Android and `BGTaskScheduler` on iOS. It replaced the older `expo-background-fetch`.
- `expo-task-manager` with `expo-location` for background location.
- Silent push notifications to wake the app for a short time.
- Native code for special cases like audio playback or uploads.

```tsx
import * as TaskManager from "expo-task-manager";
import * as BackgroundTask from "expo-background-task";

TaskManager.defineTask("sync-data", async () => {
  await syncPendingChanges();
  return BackgroundTask.BackgroundTaskResult.Success;
});

await BackgroundTask.registerTaskAsync("sync-data", { minimumInterval: 15 });
```

The OS decides when the task actually runs. You can't count on exact timing, especially on iOS.

### 189: What is a good flow for asking for permissions?

1. Ask only when the user is about to use the feature, not on app start.
2. Explain why first, with your own screen or message, before the system dialog shows.
3. Check the current status before asking.
4. Handle "denied" gracefully. Keep the rest of the app working.
5. If the permission was permanently denied, the system dialog won't show again, so offer a button that opens settings with `Linking.openSettings()`.

```tsx
const { status, canAskAgain } = await Location.getForegroundPermissionsAsync();

if (status !== "granted" && !canAskAgain) {
  Alert.alert(
    "Location is off",
    "Enable it in Settings to see stores near you.",
    [
      { text: "Cancel", style: "cancel" },
      { text: "Open Settings", onPress: () => Linking.openSettings() },
    ],
  );
}
```

### 190: How do you track the user's location while they move?

Use `watchPositionAsync` from `expo-location` and stop it when the screen unmounts:

```tsx
useEffect(() => {
  let sub: Location.LocationSubscription | undefined;

  (async () => {
    const { status } = await Location.requestForegroundPermissionsAsync();
    if (status !== "granted") return;

    sub = await Location.watchPositionAsync(
      { accuracy: Location.Accuracy.Balanced, distanceInterval: 20 },
      (loc) => setPosition(loc.coords),
    );
  })();

  return () => sub?.remove();
}, []);
```

Use the lowest accuracy that works for your feature, because high accuracy drains the battery. Tracking in the background needs a separate permission and `startLocationUpdatesAsync`.

### 191: Which libraries do you use for the camera?

- **expo-camera**: easy to use, supports photos, video and barcode scanning. Good for most apps.
- **react-native-vision-camera**: more powerful. It supports frame processors (run code on each camera frame, for example for ML), many formats, and fine control over the device. Good for advanced camera apps.

```tsx
import { CameraView, useCameraPermissions } from "expo-camera";

function Scanner() {
  const [permission, requestPermission] = useCameraPermissions();
  if (!permission?.granted)
    return <Button title="Allow camera" onPress={requestPermission} />;

  return (
    <CameraView
      style={{ flex: 1 }}
      barcodeScannerSettings={{ barcodeTypes: ["qr"] }}
      onBarcodeScanned={({ data }) => console.log(data)}
    />
  );
}
```

If you just need the user to pick or take one photo, `expo-image-picker` is simpler.

### 192: How do you read and write files?

Use `expo-file-system`. Its newer object-based API uses `File`, `Directory` and `Paths`:

```tsx
import { File, Directory, Paths } from "expo-file-system";

const file = new File(Paths.document, "notes.txt");
file.create();
await file.write("Hello");
const text = await file.text();

const dir = new Directory(Paths.cache, "images");
dir.create();
```

`Paths.document` is for files the app keeps. `Paths.cache` is for files the OS may delete when space is low. In SDK 58 `File.write()` became async (use `writeSync()` for the sync version). The older function-based API (`readAsStringAsync`, `writeAsStringAsync`) moved to `expo-file-system/legacy`. Without Expo, `react-native-fs` or `react-native-blob-util` are common.

### 193: How do you upload a file or image to a server?

Use `FormData` with an object that has `uri`, `name` and `type`. React Native reads the file from the URI:

```tsx
async function uploadAvatar(uri: string) {
  const form = new FormData();
  form.append("avatar", {
    uri,
    name: "avatar.jpg",
    type: "image/jpeg",
  } as any);

  const res = await fetch("https://api.example.com/avatar", {
    method: "POST",
    body: form,
  });
  if (!res.ok) throw new Error("Upload failed");
}
```

Don't set the `Content-Type` header yourself, `fetch` adds it with the correct boundary. For large files or upload progress, use `expo-file-system` upload tasks or a library like `react-native-blob-util`. For big files, uploading directly to S3 with a presigned URL is a good pattern.

### 194: How do you show web content inside a React Native app?

Use `react-native-webview`:

```tsx
import { WebView } from "react-native-webview";

<WebView
  source={{ uri: "https://example.com/help" }}
  onMessage={(event) => console.log("from web:", event.nativeEvent.data)}
  injectedJavaScript="window.ReactNativeWebView.postMessage(document.title); true;"
/>;
```

The web page sends messages with `window.ReactNativeWebView.postMessage(string)` and you receive them in `onMessage`. To send messages to the page, use `ref.current.injectJavaScript()` or `postMessage`. Only load trusted URLs, and limit what the page can do (for example with `originWhitelist`), because a web view with a bridge to native code is a security risk.

### 195: What is interpolation in the Animated API?

`interpolate` maps one range of values to another. You often use one animated value to drive several styles:

```tsx
const progress = useAnimatedValue(0);

const opacity = progress.interpolate({
  inputRange: [0, 1],
  outputRange: [0, 1],
});

const translateY = progress.interpolate({
  inputRange: [0, 1],
  outputRange: [50, 0],
  extrapolate: "clamp",
});

const rotate = progress.interpolate({
  inputRange: [0, 1],
  outputRange: ["0deg", "180deg"],
});

<Animated.View style={{ opacity, transform: [{ translateY }, { rotate }] }} />;
```

`extrapolate: 'clamp'` stops the output from going beyond the output range.

### 196: How do you combine animations with the Animated API?

Use the composition functions:

- `Animated.sequence([...])`: one after another
- `Animated.parallel([...])`: all at the same time
- `Animated.stagger(delay, [...])`: start each one after a delay
- `Animated.delay(ms)`: wait
- `Animated.loop(animation)`: repeat

```tsx
Animated.sequence([
  Animated.timing(scale, {
    toValue: 1.2,
    duration: 150,
    useNativeDriver: true,
  }),
  Animated.spring(scale, { toValue: 1, friction: 3, useNativeDriver: true }),
]).start(({ finished }) => {
  if (finished) onAnimationDone();
});
```

`start` takes a callback that tells you if the animation finished or was interrupted.

### 197: How do you animate something based on scroll position?

Use `Animated.event` to connect the scroll offset to an animated value, then interpolate it:

```tsx
const scrollY = useAnimatedValue(0);

const headerOpacity = scrollY.interpolate({
  inputRange: [0, 100],
  outputRange: [1, 0],
  extrapolate: 'clamp',
});

<Animated.View style={[styles.header, { opacity: headerOpacity }]} />
<Animated.ScrollView
  onScroll={Animated.event([{ nativeEvent: { contentOffset: { y: scrollY } } }], {
    useNativeDriver: true,
  })}
  scrollEventThrottle={16}
>
  {content}
</Animated.ScrollView>
```

With `useNativeDriver: true`, the scroll events go straight to the animation on the UI thread. In Reanimated you use `useAnimatedScrollHandler` or `useScrollOffset` for the same thing.

### 198: What are shared values and useAnimatedStyle in Reanimated?

- A **shared value** (`useSharedValue`) holds data that both the JS thread and the UI thread can read and write. You change it through `.value` (or `.set()` / `.get()`, which work better with the React Compiler).
- `useAnimatedStyle` creates a style from shared values. It runs on the UI thread and updates the view without re-rendering the React component.

```tsx
const progress = useSharedValue(0);

const style = useAnimatedStyle(() => ({
  opacity: progress.value,
  transform: [{ scale: 0.8 + progress.value * 0.2 }],
}));

useEffect(() => {
  progress.value = withTiming(1, { duration: 400 });
}, []);

return <Animated.View style={[styles.card, style]} />;
```

Because animations don't cause React renders, they stay smooth even if your component tree is big.

### 199: What are CSS animations and transitions in Reanimated 4?

Reanimated 4 added a CSS-like API, so you can write simple animations without shared values:

```tsx
import Animated from 'react-native-reanimated';

// Transition: animates when the style value changes
<Animated.View
  style={{
    width: expanded ? 200 : 100,
    transitionProperty: 'width',
    transitionDuration: 300,
  }}
/>

// Keyframe animation
<Animated.View
  style={{
    animationName: {
      from: { opacity: 0 },
      to: { opacity: 1 },
    },
    animationDuration: '500ms',
    animationIterationCount: 'infinite',
    animationDirection: 'alternate',
  }}
/>
```

Use the CSS API for state-driven animations, and shared values with worklets for gestures and interactive animations.

### 200: What is a worklet?

A worklet is a small JavaScript function that can run on a different JS runtime, usually the UI thread. Reanimated uses worklets for `useAnimatedStyle`, gesture callbacks and animation callbacks. You can mark your own function with the `'worklet'` directive:

```tsx
function clamp(value: number, min: number, max: number) {
  "worklet";
  return Math.min(Math.max(value, min), max);
}
```

Worklets can only use values they capture (copied to the UI runtime) and other worklets. You can't call normal JS functions from a worklet directly, you have to schedule them back on the JS thread. Since Reanimated 4, worklets live in a separate package, `react-native-worklets`.

### 201: How do you build a draggable element with Gesture Handler and Reanimated?

Use a `Pan` gesture that updates shared values, and an animated style that reads them:

```tsx
import { Gesture, GestureDetector } from "react-native-gesture-handler";
import Animated, {
  useSharedValue,
  useAnimatedStyle,
  withSpring,
} from "react-native-reanimated";

function Draggable() {
  const x = useSharedValue(0);
  const y = useSharedValue(0);

  const pan = Gesture.Pan()
    .onChange((e) => {
      x.value += e.changeX;
      y.value += e.changeY;
    })
    .onEnd(() => {
      x.value = withSpring(0);
      y.value = withSpring(0);
    });

  const style = useAnimatedStyle(() => ({
    transform: [{ translateX: x.value }, { translateY: y.value }],
  }));

  return (
    <GestureDetector gesture={pan}>
      <Animated.View style={[styles.ball, style]} />
    </GestureDetector>
  );
}
```

The gesture callbacks run on the UI thread as worklets, so dragging stays smooth even when JavaScript is busy.

### 202: What are layout animations in Reanimated?

Layout animations animate a component when it mounts, unmounts or changes position:

```tsx
import Animated, {
  FadeIn,
  FadeOut,
  LinearTransition,
} from "react-native-reanimated";

{
  items.map((item) => (
    <Animated.View
      key={item.id}
      entering={FadeIn.duration(200)}
      exiting={FadeOut}
      layout={LinearTransition}
    >
      <Text>{item.title}</Text>
    </Animated.View>
  ));
}
```

- `entering` runs when the view appears
- `exiting` runs when it is removed
- `layout` animates position and size changes, for example when a sibling is removed

There are many presets (`SlideInRight`, `ZoomIn`, `BounceIn`...) and you can make custom ones.

### 203: How do you make a layout work on phones and tablets?

- Use Flexbox and percentages instead of fixed widths.
- Use `useWindowDimensions` to pick a layout based on width, like breakpoints on the web.
- Limit the content width on big screens so lines don't get too long.
- Handle orientation changes and split-screen/multi-window on Android and iPad.
- Test on a small phone, a large phone, a tablet and a foldable.

```tsx
function ProductGrid() {
  const { width } = useWindowDimensions();
  const columns = width >= 1024 ? 4 : width >= 768 ? 3 : 2;

  return (
    <FlatList
      key={columns} // numColumns can't change without remounting
      numColumns={columns}
      data={products}
      renderItem={renderItem}
    />
  );
}
```

In Expo, set `"orientation": "default"` in `app.json` to allow rotation. Since Android 16, large screen devices ignore orientation locks, so tablet layouts matter more.

### 204: How do you deal with the user's font size settings?

Text scales with the system font size by default (`allowFontScaling` is `true`). This is good for accessibility, but very large sizes can break layouts. Options:

- Design layouts that can grow: avoid fixed heights on text containers, allow wrapping.
- Limit extreme scaling with `maxFontSizeMultiplier`:

```tsx
<Text maxFontSizeMultiplier={1.5}>Order total</Text>
```

- Read the current scale with `PixelRatio.getFontScale()` or `useWindowDimensions().fontScale` and adjust the layout, for example stack items vertically when the scale is large.

Don't turn off font scaling everywhere. Users with low vision depend on it.

### 205: What are common styling differences between iOS and Android?

- **Shadows**: older code uses `shadow*` props on iOS and `elevation` on Android. `boxShadow` works on both.
- **Fonts**: the default font is San Francisco on iOS and Roboto on Android. Font weights may look different, and custom fonts are named differently (font family name vs file name).
- **Text**: Android adds extra font padding. Use `includeFontPadding: false` to align text precisely.
- **Touch feedback**: Android uses ripples, iOS uses opacity or highlight changes.
- **Overflow**: older Android versions clipped children differently.
- **Status bar and system bars**: Android now draws edge-to-edge, iOS always did.

Test both platforms regularly, not only before release.

### 206: What is edge-to-edge on Android and how does it affect React Native apps?

Edge-to-edge means the app draws behind the status bar at the top and the navigation bar at the bottom, like iOS. Android 15 enforces it for apps targeting SDK 35, and Android 16 removed the opt-out.

For React Native this means:

- You must add padding for system bars yourself, using safe area insets.
- `StatusBar` props like `backgroundColor` and `translucent` no longer make sense and were removed in 0.87.
- `KeyboardAvoidingView` and measurement APIs needed fixes, which landed in releases up to 0.86.

New projects have edge-to-edge on by default (`edgeToEdgeEnabled=true` in `gradle.properties`). Use `react-native-safe-area-context` everywhere and test with both gesture navigation and the 3-button navigation bar.

### 207: When should you use useSafeAreaInsets instead of SafeAreaView?

`SafeAreaView` adds padding to a whole container. `useSafeAreaInsets` gives you the numbers, so you can apply them exactly where you need:

```tsx
import { useSafeAreaInsets } from "react-native-safe-area-context";

function BottomBar() {
  const insets = useSafeAreaInsets();
  return (
    <View style={{ paddingBottom: insets.bottom + 8, paddingHorizontal: 16 }}>
      <Button title="Checkout" onPress={checkout} />
    </View>
  );
}
```

Use the hook for custom headers, bottom bars, floating buttons and scroll content (`contentContainerStyle`), where you want the background to extend under the system bar but the content to stay clear of it. Wrap the app in `SafeAreaProvider` (Expo Router and React Navigation do this for you).

### 208: How do you build a theme system in React Native?

Put your colors, spacing and typography in theme objects, pick one based on the color scheme, and share it through context:

```tsx
const light = { background: "#fff", text: "#111", primary: "#0a7ea4" };
const dark = { background: "#000", text: "#eee", primary: "#4fc3f7" };

const ThemeContext = createContext(light);

export function ThemeProvider({ children }: { children: React.ReactNode }) {
  const scheme = useColorScheme();
  return (
    <ThemeContext value={scheme === "dark" ? dark : light}>
      {children}
    </ThemeContext>
  );
}

export const useTheme = () => use(ThemeContext);
```

React Navigation also has a `theme` prop for its own colors. Libraries like Unistyles, NativeWind and Tamagui have theme support built in, and some avoid re-rendering the whole tree when the theme changes.

### 209: How do you translate an app and support right-to-left languages?

For translations, use a library like `i18next` with `react-i18next`, and `expo-localization` to read the device language:

```tsx
import i18n from "i18next";
import { initReactI18next, useTranslation } from "react-i18next";
import { getLocales } from "expo-localization";

i18n.use(initReactI18next).init({
  lng: getLocales()[0]?.languageCode ?? "en",
  fallbackLng: "en",
  resources: {
    en: { translation: { greeting: "Hello" } },
    ar: { translation: { greeting: "مرحبا" } },
  },
});

function Header() {
  const { t } = useTranslation();
  return <Text>{t("greeting")}</Text>;
}
```

For right-to-left (Arabic, Hebrew), React Native flips Flexbox layouts automatically when RTL is on. Use `start`/`end` styles instead of `left`/`right`, flip direction icons, and control RTL with `I18nManager.forceRTL()`, which needs an app restart.

### 210: How do you tell a screen reader about the state of an element?

Use `accessibilityState` (or the `aria-*` props) for things like selected, disabled, checked, busy and expanded:

```tsx
<Pressable
  accessibilityRole="checkbox"
  accessibilityState={{ checked: isChecked, disabled: isDisabled }}
  onPress={toggle}
>
  <Checkbox checked={isChecked} />
  <Text>Remember me</Text>
</Pressable>
```

For values like sliders or progress, use `accessibilityValue={{ min: 0, max: 100, now: 40 }}`. Use `importantForAccessibility="no-hide-descendants"` (Android) or `accessibilityElementsHidden` (iOS) to hide decorative content from the screen reader.

### 211: What is AccessibilityInfo used for?

`AccessibilityInfo` lets you check accessibility settings and talk to the screen reader:

```tsx
import { AccessibilityInfo } from "react-native";

const screenReaderOn = await AccessibilityInfo.isScreenReaderEnabled();
const reduceMotion = await AccessibilityInfo.isReduceMotionEnabled();

AccessibilityInfo.announceForAccessibility("Item added to cart");

const sub = AccessibilityInfo.addEventListener(
  "screenReaderChanged",
  (enabled) => {
    setScreenReader(enabled);
  },
);
sub.remove();
```

Common uses: announcing results of actions that don't move focus, disabling auto-playing carousels for screen reader users, and turning off animations when reduce motion is on.

### 212: How do error boundaries work in React Native?

The same as in React for the web. An error boundary is a class component that catches render errors in its children and shows a fallback instead of crashing the whole tree. Most people use `react-error-boundary`:

```tsx
import { ErrorBoundary } from "react-error-boundary";

function Fallback({ resetErrorBoundary }: { resetErrorBoundary: () => void }) {
  return (
    <View style={styles.center}>
      <Text>Something went wrong.</Text>
      <Button title="Try again" onPress={resetErrorBoundary} />
    </View>
  );
}

<ErrorBoundary
  FallbackComponent={Fallback}
  onError={(error) => reportError(error)}
>
  <App />
</ErrorBoundary>;
```

Error boundaries don't catch errors in event handlers, timers or async code. In release builds, an uncaught render error without a boundary closes the app, so boundaries matter more on mobile. Expo Router lets each route export its own `ErrorBoundary`.

### 213: How do you catch errors that are not caught anywhere else?

React Native has a global handler, `ErrorUtils`, which you can wrap to log fatal JS errors:

```tsx
const defaultHandler = ErrorUtils.getGlobalHandler();

ErrorUtils.setGlobalHandler((error, isFatal) => {
  reportToMyService(error, { isFatal });
  defaultHandler(error, isFatal);
});
```

For unhandled promise rejections, Hermes tracks them and LogBox shows a warning in development. In production, crash reporting SDKs like Sentry set up these handlers for you, so you rarely write this yourself.

### 214: How do you set up crash reporting?

Use a service like Sentry, Bugsnag, Firebase Crashlytics or EAS Observe. Sentry is a common choice:

```tsx
import * as Sentry from "@sentry/react-native";

Sentry.init({
  dsn: "https://examplePublicKey@o0.ingest.sentry.io/0",
  tracesSampleRate: 0.2,
});

export default Sentry.wrap(App);
```

A good setup catches both JS errors and native crashes, uploads source maps (and dSYM files on iOS) so stack traces are readable, and tags each report with the app version and OTA update ID. Without source maps you only see minified code positions.

### 215: How do you debug JavaScript with React Native DevTools?

Press `j` in the Metro terminal (or "Open DevTools" in the dev menu). Then:

- **Sources**: open a file with `Cmd/Ctrl + P`, click a line number to set a breakpoint, and step through code. `debugger;` statements also pause here.
- **Console**: run JS in the app context, and see logs and errors.
- **Components**: inspect the React tree, props, state and hooks. You can edit props live.
- **Profiler**: record renders and see which components rendered and why.
- **Memory**: take heap snapshots to find leaks.

DevTools connects directly to Hermes in the app, so the code runs on the device, not in a desktop browser like the old remote debugger did.

### 216: How do you inspect network requests?

React Native DevTools has a Network panel (added in 0.83) that shows `fetch`, `XMLHttpRequest` and image requests with headers, timing and response bodies. Since 0.88, WebSocket inspection is available on the Canary channel.

Other options:

- Expo's dev tools plugins
- A proxy like Charles Proxy, Proxyman or mitmproxy, which shows all traffic, including native SDKs
- Reactotron, a desktop app for logs, state and network

For a proxy on a real device you need to install its certificate, and Android release builds don't trust user certificates by default.

### 217: How do you debug a native crash?

A native crash closes the app without a red screen, so you need native logs:

- **Android**: run `adb logcat` (or open Logcat in Android Studio) and look for `FATAL EXCEPTION` or `AndroidRuntime` errors.
- **iOS**: open the Xcode console while running from Xcode, or look at crash reports in Xcode > Window > Devices and Simulators.

Common causes are a missing permission description in `Info.plist`, a library that isn't linked (forgot to rebuild after installing), a version mismatch between libraries, or a crash inside a third-party native SDK. In production, crash reporting tools collect these with symbolicated stack traces.

### 218: Which adb commands are useful for React Native development?

```bash
adb devices                      # list connected devices and emulators
adb reverse tcp:8081 tcp:8081    # let the device reach Metro on your computer
adb logcat                       # stream native logs
adb logcat *:E                   # only errors
adb install app-release.apk      # install an APK
adb shell input text "hello"     # type text into the focused field
adb shell am start -W -a android.intent.action.VIEW -d "myapp://product/1" com.example.app  # test a deep link
adb shell pm clear com.example.app   # clear app data
```

The deep link command is very handy for testing linking without sending yourself messages. On iOS the equivalent is `xcrun simctl openurl booted "myapp://product/1"`.

### 219: What can you customize in the Metro config?

`metro.config.js` lets you change how files are found and transformed. Common changes:

- Add support for extra file types, like `.svg` with a transformer, or `.db` as assets
- Resolve modules from other folders in a monorepo (`watchFolders`, `resolver.nodeModulesPaths`)
- Custom resolution for a package with `resolver.resolveRequest`
- Enable package `exports` handling (on by default in recent versions)

```js
// metro.config.js (Expo)
const { getDefaultConfig } = require("expo/metro-config");

const config = getDefaultConfig(__dirname);
config.transformer.babelTransformerPath =
  require.resolve("react-native-svg-transformer/expo");
config.resolver.assetExts = config.resolver.assetExts.filter(
  (ext) => ext !== "svg",
);
config.resolver.sourceExts.push("svg");

module.exports = config;
```

Always start from the default config (`expo/metro-config` or `@react-native/metro-config`) and change only what you need.

### 220: How do you set up path aliases like @/components?

Add them to `tsconfig.json`:

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  }
}
```

Expo's Metro config reads `paths` from `tsconfig.json` automatically. In a Community CLI project you also need `babel-plugin-module-resolver` in `babel.config.js`, because Metro doesn't read `tsconfig` there:

```js
module.exports = {
  presets: ["module:@react-native/babel-preset"],
  plugins: [["module-resolver", { alias: { "@": "./src" } }]],
};
```

Then `import { Button } from '@/components/Button'` works in both TypeScript and the bundle.

### 221: How do you set up a React Native app in a monorepo?

A common setup is a pnpm, Yarn or npm workspace with apps (`apps/mobile`, `apps/web`) and shared packages (`packages/ui`, `packages/api`). Things to watch:

- Metro must see files outside the app folder. Expo configures this automatically for workspaces since SDK 52. In other setups you set `watchFolders` and `resolver.nodeModulesPaths`.
- There must be only one copy of `react` and `react-native`. Duplicates cause "Invalid hook call" or native module errors.
- Native libraries should be installed in the app package, so autolinking finds them.
- With pnpm, you may need `node-linker=hoisted` for some native libraries.

Tools like Turborepo or Nx help with caching tasks like lint, test and build.

### 222: How do you build a signed Android release?

1. Generate an upload keystore:

```bash
keytool -genkeypair -v -storetype PKCS12 -keystore upload.keystore -alias upload -keyalg RSA -keysize 2048 -validity 10000
```

2. Put the passwords in `~/.gradle/gradle.properties` or environment variables (not in git).
3. Add a `signingConfigs.release` block in `android/app/build.gradle` that reads them, and use it in `buildTypes.release`.
4. Build:

```bash
cd android
./gradlew bundleRelease   # AAB for Google Play
./gradlew assembleRelease # APK for testing
```

With EAS Build, credentials are created and stored for you, and `eas build -p android` does all of this.

### 223: What are certificates and provisioning profiles on iOS?

- A **certificate** proves the identity of the developer or team. There are development and distribution certificates.
- An **App ID** (bundle identifier) identifies the app and its capabilities (push, sign in with Apple, app groups).
- A **provisioning profile** ties a certificate and an App ID together, plus a list of devices for development or ad hoc builds.

Xcode can manage them automatically ("Automatically manage signing"). EAS Build or Fastlane `match` can also create and share them across a team. Most "code signing failed" errors come from a profile that doesn't include the right certificate, device or capability.

### 224: How do app versions and build numbers work?

Each platform has two numbers:

- **iOS**: `CFBundleShortVersionString` (the version users see, like `2.3.0`) and `CFBundleVersion` (the build number).
- **Android**: `versionName` (shown to users) and `versionCode` (an integer that must increase with every upload to Google Play).

In Expo these are `version`, `ios.buildNumber` and `android.versionCode` in `app.json`. With EAS you can set `"appVersionSource": "remote"` and `autoIncrement: true` so build numbers are managed for you. A JS-only OTA update doesn't change these numbers.

### 225: How do you reduce the size of the app?

- Ship an AAB on Android, so users only download the code for their device.
- Enable R8 minification and resource shrinking in Android release builds (`minifyEnabled`, `shrinkResources`).
- Remove unused libraries, especially ones with large native SDKs.
- Compress images, use WebP or AVIF, and load large images from a CDN instead of bundling them.
- Check what is in the JS bundle with Expo Atlas or `source-map-explorer`.
- Avoid shipping several fonts or icon sets you don't use.

Measure with the store's own size report (App Store Connect and Play Console), because the downloaded size is different from the size of the file you build.

### 226: How do you improve app startup time?

- Use Hermes (the default), so JS is precompiled to bytecode.
- Load less on startup: lazy load screens and large modules, and delay non-critical SDK setup (analytics, chat widgets).
- Avoid big synchronous work in the root component and in module top-level code.
- Keep the splash screen visible only while critical data loads, and show cached data first.
- Use synchronous storage like MMKV for values needed on first render.
- Enable inline requires in Metro (`transformer.getTransformOptions` with `inlineRequires: true`). It is on by default in many templates.

Measure cold start in release builds on a low-end Android phone, because that is where startup is slowest.

### 227: Which queries should you prefer in React Native Testing Library?

Prefer queries that match how users find things:

1. `getByRole` with a `name` option, like `getByRole('button', { name: 'Save' })`
2. `getByLabelText` for inputs with an accessibility label
3. `getByPlaceholderText`
4. `getByText`
5. `getByDisplayValue` for input values
6. `getByTestId` as a last option

There are `getBy*` (throws if missing), `queryBy*` (returns `null`, for checking that something is not there) and `findBy*` (async, waits for the element). Using role queries also checks that your components have correct accessibility roles.

### 228: How do you simulate user actions in React Native Testing Library?

Use `userEvent`, which runs a realistic sequence of events (press in, press out, focus, change text and so on):

```tsx
import { render, screen, userEvent } from "@testing-library/react-native";

test("submits the form", async () => {
  const user = userEvent.setup();
  const onSubmit = jest.fn();
  render(<LoginForm onSubmit={onSubmit} />);

  await user.type(screen.getByPlaceholderText("Email"), "a@b.com");
  await user.type(screen.getByPlaceholderText("Password"), "secret123");
  await user.press(screen.getByRole("button", { name: "Log in" }));

  expect(onSubmit).toHaveBeenCalledWith({
    email: "a@b.com",
    password: "secret123",
  });
});
```

`fireEvent` also exists. It is faster but only fires a single event handler, so it can miss bugs that `userEvent` would find.

### 229: How do you mock a native module in Jest?

Jest runs in Node, so native modules don't exist. Many libraries ship their own mocks. For others, use `jest.mock`:

```tsx
// jest.setup.ts
jest.mock("expo-haptics", () => ({
  impactAsync: jest.fn(),
  ImpactFeedbackStyle: { Light: "light" },
}));

jest.mock("@react-native-async-storage/async-storage", () =>
  require("@react-native-async-storage/async-storage/jest/async-storage-mock"),
);

jest.mock("react-native-reanimated", () =>
  require("react-native-reanimated/mock"),
);
```

Register the setup file with `setupFiles` or `setupFilesAfterEnv` in `jest.config.js`. Keep mocks small, and only mock the native boundary, not your own logic.

### 230: How do you test components that use navigation?

Render them inside a real navigator instead of mocking `navigation`, so the test behaves like the app:

```tsx
import { createStaticNavigation } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";

const Stack = createNativeStackNavigator({
  screens: { Home: HomeScreen, Details: DetailsScreen },
});
const Navigation = createStaticNavigation(Stack);

test("opens details", async () => {
  const user = userEvent.setup();
  render(<Navigation />);

  await user.press(screen.getByText("Go to details"));
  expect(await screen.findByText("Details screen")).toBeOnTheScreen();
});
```

For Expo Router there is `renderRouter` from `expo-router/testing-library`, which takes a mock file structure.

### 231: Are snapshot tests useful in React Native?

Snapshot tests save the rendered output and fail when it changes. They are easy to write, but:

- Big snapshots get updated without anyone reading them.
- They fail on any small change, even ones that don't matter.
- They don't tell you if the behavior is correct.

They are fine for small, stable components (an icon, a formatted price) or with inline snapshots of specific values. For most components, tests that check behavior with React Native Testing Library are more useful. For checking how things look, visual regression tests on real screens are better.

### 232: What is the difference between Detox and Maestro?

|                | Detox                                                          | Maestro                                    |
| -------------- | -------------------------------------------------------------- | ------------------------------------------ |
| Test language  | JavaScript/TypeScript                                          | YAML flows                                 |
| Setup          | Native build config, more setup                                | Install CLI, point it at any app           |
| Waiting        | Gray box: syncs with the app's network, timers and animations  | Black box: retries and waits automatically |
| Speed to write | Slower                                                         | Very fast                                  |
| Best for       | Teams that want E2E tests in the same language and strong sync | Quick smoke tests, QA teams, any app       |

Both run on simulators and emulators, and both can run in CI. EAS Workflows has built-in steps for Maestro.

### 233: How do you mock API calls in tests?

Mock at the network level with Mock Service Worker (MSW). It intercepts `fetch` in Node, so your components and data libraries run their real code:

```tsx
import { http, HttpResponse } from "msw";
import { setupServer } from "msw/node";

const server = setupServer(
  http.get("https://api.example.com/users", () =>
    HttpResponse.json([{ id: "1", name: "Ana" }]),
  ),
);

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());

test("shows users", async () => {
  render(<Users />);
  expect(await screen.findByText("Ana")).toBeOnTheScreen();
});
```

MSW 2 needs some polyfills in React Native Jest environments. Mocking at the network level is better than mocking your API client functions, because it tests more real code.

### 234: How do you set up CI/CD for a React Native app?

A typical pipeline:

1. **On every pull request**: install, type check (`tsc`), lint, unit tests, and maybe `expo-doctor`.
2. **On merge to main**: build an internal/preview build, run E2E tests, and publish an OTA update to a staging channel.
3. **On release**: build production binaries, submit to the stores, publish source maps.

Tools: EAS Workflows (YAML pipelines for EAS Build/Submit/Update), GitHub Actions, Bitrise, CircleCI, and Fastlane for native build steps. iOS builds need macOS runners, which are slower and more expensive, so cache CocoaPods, Gradle and `node_modules`.

### 235: What is Fastlane?

Fastlane is a tool that automates native build and release tasks for iOS and Android. You write "lanes" in a `Fastfile`:

```ruby
platform :ios do
  lane :beta do
    match(type: "appstore")
    increment_build_number
    build_app(scheme: "MyApp")
    upload_to_testflight
  end
end
```

It handles signing (`match`), building (`gym`/`build_app`), screenshots, and uploading to TestFlight and Google Play. Many bare React Native projects use it in CI. EAS replaces most of what Fastlane does for Expo projects.

### 236: What is the Strict TypeScript API in React Native?

It is a set of TypeScript types generated from React Native's source code, which became the default in 0.87. It changes two things:

- You can only import from the `react-native` root. Deep imports like `react-native/Libraries/...` are now type errors, because internal files are not part of the public API.
- Types are more accurate. For example, refs use types like `ViewInstance` and `TextInputInstance`, and old `*Properties` aliases are replaced with `*Props`.

```tsx
// Before
import { ViewProperties } from "react-native";
// After
import type { ViewProps } from "react-native";
```

A temporary opt-out exists through 0.88 with the `react-native-legacy-deep-imports` custom condition in `tsconfig.json`, but you should migrate.

### 237: How do you type the style prop of a reusable component?

Use `StyleProp` with the right style type:

```tsx
import type { StyleProp, ViewStyle, TextStyle } from "react-native";

type BadgeProps = {
  label: string;
  style?: StyleProp<ViewStyle>;
  textStyle?: StyleProp<TextStyle>;
};

export function Badge({ label, style, textStyle }: BadgeProps) {
  return (
    <View style={[styles.badge, style]}>
      <Text style={[styles.text, textStyle]}>{label}</Text>
    </View>
  );
}
```

`StyleProp` accepts a single style, an array, `false`, `null` or `undefined`, the same things the `style` prop accepts. There is also `ImageStyle` for images. To accept all props of `View`, extend `ViewProps`.

### 238: What can you do with a ref to a native component?

A ref to a host component (`View`, `TextInput`, `ScrollView`) gives you a native instance with methods:

- `TextInput`: `focus()`, `blur()`, `clear()`, `isFocused()`
- `ScrollView` / `FlatList`: `scrollTo()`, `scrollToEnd()`, `scrollToIndex()`, `scrollToOffset()`
- All views: `measure()`, `measureInWindow()`, `measureLayout()`, `setNativeProps()` (legacy)

Since 0.82, refs to native views also support DOM-like APIs such as `getBoundingClientRect()`, `parentNode`, `children` and `compareDocumentPosition()`, similar to DOM elements on the web. This makes it easier to share logic with the web.

### 239: How do you get the position and size of a view on screen?

Use `measure` or `measureInWindow` on a ref, or the DOM-like `getBoundingClientRect()`:

```tsx
const ref = useRef<View>(null);

function showTooltip() {
  ref.current?.measureInWindow((x, y, width, height) => {
    setTooltipPosition({ x, y: y + height });
  });
}

<View ref={ref}>
  <Pressable onPress={showTooltip}>
    <InfoIcon />
  </Pressable>
</View>;
```

`measure` gives position relative to the root view and also gives the page position. `measureInWindow` gives position relative to the window. In the New Architecture, you can call them synchronously inside `useLayoutEffect` and get the correct values before the frame is drawn.

### 240: What is onLayout?

`onLayout` is called when a view is mounted and every time its size or position changes. It gives you the layout in the event:

```tsx
const [width, setWidth] = useState(0);

<View
  onLayout={(e) => {
    const { width, height, x, y } = e.nativeEvent.layout;
    setWidth(width);
  }}
>
  <Chart width={width} />
</View>;
```

The values are relative to the parent. It is useful for sizing children to a container (charts, carousels). Setting state in `onLayout` causes an extra render, so avoid it for things Flexbox can do.

### 241: How does useLayoutEffect behave in the New Architecture?

In the old architecture, layout was calculated asynchronously, so reading a view's size in `useLayoutEffect` could give old values and caused flicker (one wrong frame, then the corrected one).

With Fabric, layout runs synchronously and `useLayoutEffect` runs before the frame is shown, just like on the web. You can measure a view and update state in `useLayoutEffect`, and the user only sees the final result:

```tsx
useLayoutEffect(() => {
  const rect = targetRef.current?.getBoundingClientRect();
  if (rect) setTooltipTop(rect.y - TOOLTIP_HEIGHT);
}, []);
```

This makes things like tooltips and popovers much easier to build without visual jumps.

### 242: How do you react to the keyboard opening and closing?

Subscribe to `Keyboard` events:

```tsx
useEffect(() => {
  const show = Keyboard.addListener("keyboardDidShow", (e) => {
    setKeyboardHeight(e.endCoordinates.height);
  });
  const hide = Keyboard.addListener("keyboardDidHide", () =>
    setKeyboardHeight(0),
  );

  return () => {
    show.remove();
    hide.remove();
  };
}, []);
```

On iOS there are also `keyboardWillShow` and `keyboardWillHide`, which fire before the animation and let you animate along with the keyboard. Android only has the `Did` events. For smooth keyboard-following animations on both platforms, `react-native-keyboard-controller` gives you animated values that track the keyboard frame by frame.

### 243: How do you handle incoming deep links without a navigation library?

Use `Linking.getInitialURL()` for the link that opened the app, and an event listener for links received while the app is running:

```tsx
useEffect(() => {
  Linking.getInitialURL().then((url) => {
    if (url) handleUrl(url);
  });

  const sub = Linking.addEventListener("url", ({ url }) => handleUrl(url));
  return () => sub.remove();
}, []);
```

There is also the `useLinkingURL` hook from `expo-linking`. Navigation libraries do this for you, but you may need it for things like OAuth redirects or magic login links.

### 244: How do you copy text to the clipboard?

The `Clipboard` API was removed from React Native core. Use `expo-clipboard` or `@react-native-clipboard/clipboard`:

```tsx
import * as Clipboard from "expo-clipboard";

await Clipboard.setStringAsync(couponCode);
const text = await Clipboard.getStringAsync();
```

On iOS, reading the clipboard shows a system "pasted from" message, so only read it when the user does something that needs it, like tapping a "Paste" button.

### 245: How do you build infinite scroll with TanStack Query?

Use `useInfiniteQuery` with `FlatList`:

```tsx
const {
  data,
  fetchNextPage,
  hasNextPage,
  isFetchingNextPage,
  refetch,
  isRefetching,
} = useInfiniteQuery({
  queryKey: ["posts"],
  queryFn: ({ pageParam }) => fetchPosts({ cursor: pageParam }),
  initialPageParam: null as string | null,
  getNextPageParam: (lastPage) => lastPage.nextCursor,
});

const posts = data?.pages.flatMap((page) => page.items) ?? [];

<FlatList
  data={posts}
  keyExtractor={(p) => p.id}
  renderItem={({ item }) => <PostCard post={item} />}
  onEndReached={() => hasNextPage && !isFetchingNextPage && fetchNextPage()}
  onEndReachedThreshold={0.5}
  refreshing={isRefetching}
  onRefresh={refetch}
  ListFooterComponent={isFetchingNextPage ? <ActivityIndicator /> : null}
/>;
```

Cursor-based pagination works better than page numbers when items are added while the user scrolls.

### 246: Why do you get the warning "VirtualizedLists should never be nested inside plain ScrollViews"?

It appears when you put a `FlatList` or `SectionList` inside a `ScrollView` with the same orientation. The outer `ScrollView` gives the list unlimited height, so the list renders all items and virtualization stops working.

Fixes:

- Make the `FlatList` the only scroll container, and move the other content into `ListHeaderComponent` and `ListFooterComponent`.
- Use a `SectionList` if the page has several groups of data.
- If the list is small and fixed, render it with `map` instead of `FlatList`.

A horizontal `FlatList` inside a vertical `ScrollView` is fine.

### 247: What does keyboardShouldPersistTaps do?

When the keyboard is open and the user taps a button inside a `ScrollView`, by default the first tap only closes the keyboard and the button doesn't get it. `keyboardShouldPersistTaps` changes this:

- `'never'` (default): tap closes the keyboard, the child doesn't receive it
- `'handled'`: the tap goes to the child if a child handles it, otherwise closes the keyboard
- `'always'`: the keyboard stays open and children receive taps

```tsx
<ScrollView keyboardShouldPersistTaps="handled">
  <TextInput placeholder="Search" />
  <Button title="Search" onPress={search} />
</ScrollView>
```

`'handled'` is what you want for most forms. Since 0.87, boolean values are no longer accepted.

### 248: How do you make a header stick to the top while scrolling?

Use `stickyHeaderIndices` on a `ScrollView` or `FlatList`. It takes the indexes of children that should stick:

```tsx
<ScrollView stickyHeaderIndices={[1]}>
  <Banner />
  <FilterBar /> {/* sticks once it reaches the top */}
  <ProductList />
</ScrollView>
```

In a `SectionList`, section headers stick by default on iOS. You control this with `stickySectionHeadersEnabled`. For headers that collapse or fade, use an animated scroll handler instead.

### 249: How do you render a grid with FlatList?

Use `numColumns`:

```tsx
<FlatList
  data={photos}
  numColumns={3}
  keyExtractor={(p) => p.id}
  columnWrapperStyle={{ gap: 4 }}
  contentContainerStyle={{ gap: 4 }}
  renderItem={({ item }) => (
    <Image source={{ uri: item.url }} style={{ flex: 1 / 3, aspectRatio: 1 }} />
  )}
/>
```

`columnWrapperStyle` styles each row. `numColumns` can't be changed after the first render, so if it changes (for example on rotation), also change the `key` of the list to remount it. For masonry (Pinterest-style) layouts, FlashList has a `masonry` option.

### 250: How do you build a chat list that starts at the bottom?

The classic way is an `inverted` `FlatList`. It flips the list, so the first item in `data` (the newest message) shows at the bottom, and loading older messages works with `onEndReached`:

```tsx
<FlatList
  inverted
  data={messages} // newest first
  keyExtractor={(m) => m.id}
  renderItem={({ item }) => <MessageBubble message={item} />}
  onEndReached={loadOlderMessages}
/>
```

Another approach is a normal list with `maintainVisibleContentPosition`, which keeps the visible items in place when items are added at the top. Many chat apps also use `react-native-keyboard-controller` so the list moves smoothly with the keyboard.

### 251: Why should you never put secret API keys in a React Native app?

Everything in the app, including the JavaScript bundle, can be extracted by anyone who downloads it. Hermes bytecode makes it harder to read, but tools exist to decompile it, and strings are easy to find. Environment variables like `EXPO_PUBLIC_*` are just text in the bundle.

So:

- Keep secret keys (payment provider secret keys, admin API keys, database credentials) on your server.
- Let the app call your backend, and your backend call the third-party service.
- Only put keys in the app that are meant to be public, like a Stripe publishable key or a Maps key restricted to your app's bundle ID.

### 252: What is SSL pinning?

SSL (certificate) pinning means the app only trusts specific certificates or public keys for your API, not every certificate signed by a trusted authority. This protects against man-in-the-middle attacks, for example with a certificate installed on a compromised device.

In React Native you add it with a library like `react-native-ssl-public-key-pinning`, or with native config (Android Network Security Config, or iOS code). Pin the public key, not the full certificate, and always include a backup pin, otherwise rotating the certificate can lock all users out of your API until they update the app.

### 253: How do you detect rooted or jailbroken devices?

Libraries like `jail-monkey` check for common signs: su binaries, Cydia, writable system folders, hooking frameworks. On a deeper level, you can use platform attestation services: Play Integrity API on Android and App Attest / DeviceCheck on iOS. These let your server check that requests come from a real, unmodified copy of your app.

Client-side checks can always be bypassed by a skilled attacker, so treat them as one layer. Important checks must happen on the server.

### 254: How do you handle access and refresh tokens in a React Native app?

A common setup:

1. After login, store the refresh token (and usually the access token) in secure storage (`expo-secure-store` or Keychain/Keystore).
2. Keep the access token in memory for requests.
3. When a request returns 401, call the refresh endpoint once, save the new tokens, and retry the original request.
4. If several requests fail at the same time, make them wait for a single refresh instead of refreshing many times.
5. If the refresh fails, log the user out and clear everything.

```ts
let refreshPromise: Promise<string> | null = null;

async function getFreshToken() {
  refreshPromise ??= refreshAccessToken().finally(() => {
    refreshPromise = null;
  });
  return refreshPromise;
}
```

Since mobile apps have no cookies by default, tokens usually go in the `Authorization` header.

### 255: How do you implement OAuth login (Google, GitHub and so on) in React Native?

Use the Authorization Code flow with PKCE in the system browser, not in a web view. Libraries: `expo-auth-session` (with `expo-web-browser`) or `react-native-app-auth`.

```tsx
import * as AuthSession from "expo-auth-session";
import * as WebBrowser from "expo-web-browser";

WebBrowser.maybeCompleteAuthSession();

const discovery = AuthSession.useAutoDiscovery("https://auth.example.com");
const [request, response, promptAsync] = AuthSession.useAuthRequest(
  {
    clientId: "my-client-id",
    redirectUri: AuthSession.makeRedirectUri({ scheme: "myapp" }),
    scopes: ["openid", "profile"],
    usePKCE: true,
  },
  discovery,
);
```

The app gets an authorization code through the redirect URL and exchanges it for tokens. For Google and Apple sign-in, native SDKs (`@react-native-google-signin/google-signin`, `expo-apple-authentication`) give a better experience. Apple requires "Sign in with Apple" if you offer other third-party logins in most cases.

### 256: How do you add Face ID or fingerprint login?

Use `expo-local-authentication` (or `react-native-biometrics`):

```tsx
import * as LocalAuthentication from "expo-local-authentication";

async function unlock() {
  const hasHardware = await LocalAuthentication.hasHardwareAsync();
  const enrolled = await LocalAuthentication.isEnrolledAsync();
  if (!hasHardware || !enrolled) return false;

  const result = await LocalAuthentication.authenticateAsync({
    promptMessage: "Unlock MyApp",
  });
  return result.success;
}
```

On iOS you need `NSFaceIDUsageDescription` in `Info.plist`. Biometrics only prove that the device owner is present. A common pattern is to keep a refresh token in secure storage that requires biometric authentication to read (`requireAuthentication: true` in `expo-secure-store`).

### 257: How do you add in-app purchases or subscriptions?

Digital goods and subscriptions sold in the app must use Apple's and Google's billing systems (with some exceptions by region and app type). Common options:

- **RevenueCat** (`react-native-purchases`): handles purchases, receipts validation, subscription status and analytics on its servers. Most teams pick this.
- **react-native-iap** or **expo-iap**: talk to StoreKit and Google Play Billing directly. You must validate receipts on your own server.

Always check the subscription status on the server, test with sandbox accounts and TestFlight, and handle restoring purchases on a new device. Physical goods (like food delivery) use normal payment providers like Stripe instead.

### 258: How do you show a map?

The usual choice is `react-native-maps`, which uses Apple Maps on iOS (or Google Maps) and Google Maps on Android:

```tsx
import MapView, { Marker } from "react-native-maps";

<MapView
  style={{ flex: 1 }}
  initialRegion={{
    latitude: 41.7151,
    longitude: 44.8271,
    latitudeDelta: 0.05,
    longitudeDelta: 0.05,
  }}
>
  <Marker
    coordinate={{ latitude: 41.7151, longitude: 44.8271 }}
    title="Office"
  />
</MapView>;
```

Google Maps needs an API key in the native config. Other options are `@rnmapbox/maps` for Mapbox, and `expo-maps`, which wraps Apple Maps and Google Maps with native UI. With many markers, cluster them, because hundreds of custom marker views are slow.

### 259: How do you play video?

Use `expo-video`, which replaced the video part of the older `expo-av`:

```tsx
import { useVideoPlayer, VideoView } from "expo-video";

function Intro() {
  const player = useVideoPlayer("https://example.com/intro.mp4", (p) => {
    p.loop = true;
    p.play();
  });

  return (
    <VideoView
      player={player}
      style={{ width: "100%", aspectRatio: 16 / 9 }}
      allowsFullscreen
    />
  );
}
```

The player is separate from the view, so you control playback without re-rendering. `react-native-video` is the other popular option and supports DRM and many streaming features. For streaming, use HLS (`.m3u8`) so quality adapts to the network.

### 260: How do you play and record audio?

Use `expo-audio` (the replacement for audio in `expo-av`):

```tsx
import { useAudioPlayer } from "expo-audio";

function Ding() {
  const player = useAudioPlayer(require("./assets/ding.mp3"));
  return (
    <Button
      title="Play"
      onPress={() => {
        player.seekTo(0);
        player.play();
      }}
    />
  );
}
```

For recording there is `useAudioRecorder`. Recording needs microphone permission. For music apps with background playback, lock screen controls and playlists, `react-native-track-player` is commonly used. Background audio also needs the audio background mode on iOS.

### 261: What are haptics and how do you use them?

Haptics are small vibrations that give physical feedback, like when you toggle a switch or a payment succeeds. Use `expo-haptics`:

```tsx
import * as Haptics from "expo-haptics";

Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light);
Haptics.notificationAsync(Haptics.NotificationFeedbackType.Success);
Haptics.selectionAsync();
```

Use them for meaningful moments, not on every tap. The core `Vibration` API also exists, but it only does simple vibration patterns, not the fine-tuned feedback of iOS haptics.

### 262: How do you keep the splash screen visible until the app is ready?

With `expo-splash-screen`, call `preventAutoHideAsync` early and hide it when your fonts, auth state or cached data are loaded:

```tsx
import * as SplashScreen from "expo-splash-screen";

SplashScreen.preventAutoHideAsync();

export default function RootLayout() {
  const [fontsLoaded] = useFonts({ Inter: require("../assets/Inter.ttf") });
  const { isReady } = useAuthBootstrap();

  useEffect(() => {
    if (fontsLoaded && isReady) SplashScreen.hideAsync();
  }, [fontsLoaded, isReady]);

  if (!fontsLoaded || !isReady) return null;
  return <Stack />;
}
```

Don't block the splash screen on slow network requests. Show the app with cached data or a skeleton instead.

### 263: Why must require() for images use a static string?

Metro finds assets at build time by reading your code. It needs to see the exact path to include the file in the bundle:

```tsx
// Works
const icon = isActive ? require("./active.png") : require("./inactive.png");

// Doesn't work: Metro can't know which file to include
const icon = require(`./${name}.png`);
```

If you need to choose images by name, build a map of static requires:

```tsx
const flags = {
  ge: require("./flags/ge.png"),
  us: require("./flags/us.png"),
} as const;

<Image source={flags[countryCode]} />;
```

### 264: How do you check if a library works with your React Native version and the New Architecture?

- Search for it on reactnative.directory. It shows New Architecture support, platforms and maintenance status.
- In Expo projects, run `npx expo-doctor`, which validates installed libraries against the React Native Directory.
- Read the library's changelog and GitHub issues for your React Native version.
- Check that it isn't using deep imports from `react-native/Libraries`, which break with the Strict TypeScript API.

Some old libraries still work through the interop layer, which translates old-style native modules and views to the New Architecture. But the interop layer is a temporary bridge, not a long-term solution, so plan to replace unmaintained libraries.

### 265: What is patch-package and when do you use it?

`patch-package` lets you change a file inside `node_modules` and keep that change after reinstalling. You edit the library, then run:

```bash
npx patch-package some-library
```

It saves a `.patch` file in a `patches/` folder, and a `postinstall` script re-applies it. pnpm and Yarn have this built in (`pnpm patch`, `yarn patch`).

It is useful in React Native when a library has a small bug (often in native code) and the fix isn't released yet. Always open an issue or pull request upstream, and remove the patch when you upgrade.

### 266: How do you write a simple native module with the Expo Modules API?

Create a local module with `npx create-expo-module@latest --local`, then write Swift and Kotlin with a small DSL:

```swift
// ios/BatteryModule.swift
import ExpoModulesCore

public class BatteryModule: Module {
  public func definition() -> ModuleDefinition {
    Name("Battery")

    Function("getLevel") { () -> Float in
      UIDevice.current.isBatteryMonitoringEnabled = true
      return UIDevice.current.batteryLevel
    }
  }
}
```

```kotlin
// android/.../BatteryModule.kt
class BatteryModule : Module() {
  override fun definition() = ModuleDefinition {
    Name("Battery")

    Function("getLevel") {
      val bm = appContext.reactContext?.getSystemService(Context.BATTERY_SERVICE) as BatteryManager
      bm.getIntProperty(BatteryManager.BATTERY_PROPERTY_CAPACITY) / 100f
    }
  }
}
```

```ts
import { requireNativeModule } from "expo";
const Battery = requireNativeModule("Battery");
Battery.getLevel();
```

`Function` is synchronous, `AsyncFunction` returns a promise. SDK 58 also added Expo Modules 2.0 (beta), where you write modules as annotated classes.

### 267: How do you define a Turbo Module spec?

You write a TypeScript spec file, and Codegen generates the native interfaces from it. The file name must start with `Native`:

```ts
// specs/NativeLocalStorage.ts
import type { TurboModule } from "react-native";
import { TurboModuleRegistry } from "react-native";

export interface Spec extends TurboModule {
  getItem(key: string): string | null;
  setItem(value: string, key: string): void;
  clear(): Promise<void>;
}

export default TurboModuleRegistry.getEnforcing<Spec>("NativeLocalStorage");
```

Then you configure `codegenConfig` in `package.json`, run the build, and implement the generated interface in Objective-C++/Swift and Kotlin/Java. The spec acts as a contract that both sides must follow, so type mismatches are caught at build time.

### 268: What is Codegen?

Codegen is a tool that reads your TypeScript (or Flow) specs for Turbo Modules and Fabric components, and generates the native glue code: C++ and platform interfaces with the correct types.

Without Codegen, the JS and native sides could disagree about method names or types, and you'd only find out at runtime. With it, the native code must implement the generated interface or the build fails. Codegen runs automatically during `pod install` and the Android build. You configure it in `package.json`:

```json
{
  "codegenConfig": {
    "name": "AppSpecs",
    "type": "all",
    "jsSrcsDir": "specs",
    "android": { "javaPackageName": "com.example.specs" }
  }
}
```

### 269: Can native module methods be synchronous?

Yes, in the New Architecture. Because Turbo Modules are called through JSI, a method can return a value directly:

```ts
export interface Spec extends TurboModule {
  getDeviceName(): string; // sync
  fetchContacts(): Promise<Contact[]>; // async
}
```

Sync methods block the JS thread until they return, so only use them for fast operations like reading a cached value or a small config. Anything that does I/O, network or heavy work should return a `Promise`. In the old bridge everything was async, which is why APIs like `AsyncStorage` were async even for small reads.

### 270: How does a native module send events to JavaScript?

The module emits events, and JavaScript subscribes to them. With the Expo Modules API:

```swift
public class DownloadModule: Module {
  public func definition() -> ModuleDefinition {
    Name("Download")
    Events("onProgress")

    AsyncFunction("start") { (url: String) in
      // ... during download:
      self.sendEvent("onProgress", ["progress": 0.5])
    }
  }
}
```

```tsx
import { useEvent } from "expo";

const { progress } = useEvent(DownloadModule, "onProgress", { progress: 0 });
```

In Turbo Modules, you can declare an `EventEmitter` type in the spec (since 0.76), and Codegen generates typed emitters. Always remove listeners when the component unmounts.

### 271: What is a brownfield app?

A brownfield app is an existing native iOS or Android app that adds React Native for some screens or features. A greenfield app is built with React Native from the start.

Teams do this to move to React Native step by step, or to share a feature between iOS and Android. The native app creates a React Native host and shows a React Native view inside a native screen. Challenges include sharing navigation, passing data and auth between native and JS, and keeping build setups compatible. Expo has `expo-brownfield` tooling to help, and React Native provides `RCTReactNativeFactory` on iOS and `ReactHost` on Android.

### 272: What is Headless JS?

Headless JS is an Android feature that runs JavaScript tasks in the background without any UI, for example when a push message arrives or a sync job runs. You register a task:

```ts
import { AppRegistry } from "react-native";

AppRegistry.registerHeadlessTask("SyncTask", () => async (data) => {
  await syncPendingChanges(data);
});
```

Then native Android code (a `HeadlessJsTaskService`) starts it. iOS has no equivalent. Most apps use higher-level libraries (`expo-background-task`, `@react-native-firebase/messaging` background handlers) that use this under the hood on Android.

### 273: What happens to timers when the app goes to the background?

When the app is in the background, the OS can pause the JavaScript thread. On iOS this happens a few seconds after the app goes to the background. On Android it depends on the device and battery settings. So `setTimeout` and `setInterval` are not reliable in the background: they may fire late or not at all.

For anything time-based, store timestamps and calculate the difference when the app becomes active again. For work that must happen in the background, use background tasks, push notifications or scheduled local notifications.

```tsx
const startedAt = useRef(Date.now());

useEffect(() => {
  const sub = AppState.addEventListener("change", (s) => {
    if (s === "active") setElapsed(Date.now() - startedAt.current);
  });
  return () => sub.remove();
}, []);
```

### 274: What replaced InteractionManager?

`InteractionManager.runAfterInteractions` was used to delay work until animations and gestures finished. It was deprecated and then removed in 0.87. The replacement is `requestIdleCallback`, which runs a callback when the JS thread is idle:

```tsx
useEffect(() => {
  const id = requestIdleCallback(() => {
    prefetchRelatedProducts();
  });
  return () => cancelIdleCallback(id);
}, []);
```

For keeping the UI responsive during heavy renders, React's `startTransition` is often a better tool, and native-driven animations don't depend on the JS thread anyway.

### 275: Can you use startTransition and useTransition in React Native?

Yes, since the New Architecture supports React's concurrent features. `startTransition` marks an update as non-urgent, so React can keep the UI responsive while rendering it:

```tsx
const [query, setQuery] = useState("");
const [filter, setFilter] = useState("");
const [isPending, startTransition] = useTransition();

<TextInput
  value={query}
  onChangeText={(text) => {
    setQuery(text); // urgent: update the input
    startTransition(() => setFilter(text)); // can wait: filter a big list
  }}
/>;
{
  isPending && <ActivityIndicator />;
}
<BigFilteredList filter={filter} />;
```

`useDeferredValue` gives a similar result. In the old architecture these APIs existed but didn't actually make rendering interruptible.

### 276: Does Suspense work in React Native?

Yes. You can use `<Suspense>` with `React.lazy`, with the `use` hook and a promise, and with data libraries that support Suspense (like TanStack Query's `useSuspenseQuery`):

```tsx
function Profile({ userPromise }: { userPromise: Promise<User> }) {
  const user = use(userPromise);
  return <Text>{user.name}</Text>;
}

<Suspense fallback={<ActivityIndicator />}>
  <Profile userPromise={userPromise} />
</Suspense>;
```

With the New Architecture, transitions keep the old content visible instead of showing the fallback again. Don't create the promise inside the component that calls `use`, or it will be recreated on every render.

### 277: Which React 19 features can you use in React Native?

React Native 0.78 added React 19, and 0.88 uses React 19.3. You can use:

- `ref` as a normal prop (no `forwardRef` needed)
- `use` for promises and context
- `<Context>` as a provider
- Actions with `useActionState` and `useOptimistic`
- `useEffectEvent` and `<Activity>` (from React 19.2)
- The React Compiler

Some features are web-only, like form `action` props on `<form>`, document metadata tags (`<title>`) and the `react-dom` resource APIs. `useOptimistic` works well for things like like buttons and sending messages.

### 278: What styling libraries are popular in React Native?

- **NativeWind**: Tailwind CSS classes for React Native (`className="flex-1 p-4 bg-white"`).
- **Unistyles**: a `StyleSheet`-like API with themes, breakpoints and variants, and updates styles without React re-renders.
- **Tamagui**: styling plus a UI kit, with an optimizing compiler, and works on web too.
- **Restyle** (Shopify): typed theme-based components.
- **styled-components** / **Emotion**: CSS-in-JS, less common now.

Plain `StyleSheet` is still a fine choice for many apps. Pick a library based on whether you need theming, web support and design tokens, not because it's popular.

### 279: Which UI component libraries are used in React Native?

- **React Native Paper**: Material Design components.
- **gluestack-ui**: unstyled and styled components, works with NativeWind.
- **Tamagui**: components plus styling system.
- **React Native Reusables**: shadcn/ui-style components you copy into your project.
- **Expo UI** (`@expo/ui`): real SwiftUI and Jetpack Compose components rendered from React.
- **@gorhom/bottom-sheet**: the common bottom sheet.

Many companies build their own design system on top of core components instead, to keep full control over look and behavior.

### 280: What are PlatformColor and DynamicColorIOS?

`PlatformColor` lets you use the platform's built-in semantic colors, which change automatically with light/dark mode and accessibility settings:

```tsx
import { PlatformColor, Platform } from "react-native";

const styles = StyleSheet.create({
  label: {
    color: Platform.select({
      ios: PlatformColor("label"),
      android: PlatformColor("?android:attr/textColorPrimary"),
    }),
  },
});
```

`DynamicColorIOS` defines your own iOS color with light and dark values (and high contrast variants):

```tsx
const accent = DynamicColorIOS({ light: "#0a7ea4", dark: "#4fc3f7" });
```

These colors are resolved by the OS, so they update without a React re-render.

### 281: Which image formats should you use in a React Native app?

- **PNG**: icons and images with transparency, but files are large.
- **JPEG**: photos.
- **WebP**: smaller than PNG and JPEG, supports transparency and animation. Supported on both platforms.
- **AVIF**: even smaller, supported by `expo-image`.
- **HEIC/HEIF**: format of iPhone photos. Supported by `Image` since 0.84.
- **SVG**: vector icons and illustrations, needs `react-native-svg` or `expo-image`.

Serve images from a CDN that can resize and convert them, and request the size you actually display.

### 282: When would you use an uncontrolled TextInput?

A controlled `TextInput` re-renders your component on every key press. Usually that is fine, but on a large or slow screen it can make typing laggy. An uncontrolled input keeps the text on the native side, and you read it only when needed:

```tsx
const valueRef = useRef('');

<TextInput
  defaultValue={initialNote}
  onChangeText={(text) => {
    valueRef.current = text;
  }}
/>

<Button title="Save" onPress={() => saveNote(valueRef.current)} />
```

React Hook Form can work with uncontrolled inputs as well. In the New Architecture, controlled inputs are also better at keeping the cursor in place when the value updates.

### 283: How do you find out why a component re-renders too often?

- Use the **Profiler** tab in React Native DevTools. Enable "Record why each component rendered" to see which props or state changed.
- Turn on "Highlight updates when components render" to see renders on screen.
- Check for new object, array or function props created on every render (if you don't use the React Compiler).
- Check context providers whose value changes too often, which re-renders all consumers.
- Check global state subscriptions that select too much (for example `useStore()` without a selector).

Fix the cause instead of adding `memo` everywhere. The React Compiler removes most of this work automatically.

### 284: Do inline styles hurt performance?

A little. An inline style object like `style={{ padding: 16 }}` creates a new object on every render. This matters mainly when it is passed to a memoized child, because the new object breaks memoization and causes extra renders.

For static styles, use `StyleSheet.create` outside the component. For styles that depend on props or state, inline objects or `useMemo` are fine. Don't spend much time on this unless the profiler shows a problem. The React Compiler also memoizes inline objects for you.

### 285: How do you avoid memory leaks in React Native components?

Clean up everything you start in an effect:

```tsx
useEffect(() => {
  const keyboardSub = Keyboard.addListener("keyboardDidShow", onShow);
  const appStateSub = AppState.addEventListener("change", onAppStateChange);
  const interval = setInterval(poll, 5000);
  const controller = new AbortController();

  fetch(url, { signal: controller.signal })
    .then(handle)
    .catch(() => {});

  return () => {
    keyboardSub.remove();
    appStateSub.remove();
    clearInterval(interval);
    controller.abort();
  };
}, []);
```

Other common leaks: listeners added outside React and never removed, large data kept in global variables or caches without limits, and native resources (video players, camera sessions) that are not released. Screens in a stack stay mounted, so a leak in one screen can grow as the user navigates.

### 286: What are API routes in Expo Router?

Expo Router lets you write server endpoints next to your screens with files ending in `+api.ts`:

```ts
// app/api/hello+api.ts
export async function GET(request: Request) {
  return Response.json({ message: "Hello" });
}

export async function POST(request: Request) {
  const body = await request.json();
  return Response.json({ received: body });
}
```

They run on a server (EAS Hosting or another Node.js/edge host), not in the app. This is useful for small backends, like hiding a third-party API key behind your own endpoint. In SDK 58, server features like data loaders and server-side rendering for web also became stable.

### 287: How do you add web support to a React Native app?

In Expo, web support is built in. Run `npx expo start --web`. It uses React Native Web, and Expo Router gives every screen a URL. You can export a static site, a single-page app or a server-rendered site (`web.output` in `app.json`).

Things to handle:

- Some native libraries don't support web. Use `.web.tsx` files or `Platform.OS === 'web'` checks.
- Hover states, keyboard navigation and wider layouts need extra work.
- SEO needs static or server rendering.

For apps where the web version is the main product, many teams keep a separate Next.js app and share logic and some components in a monorepo instead.

### 288: How do you test a release build locally?

Debug builds behave differently from release builds, so test release builds before shipping:

```bash
npx expo run:ios --configuration Release
npx expo run:android --variant release

# Community CLI
npx react-native run-android --mode release
npx react-native run-ios --mode Release
```

You can also make an internal distribution build with EAS (`"distribution": "internal"`) and install it on real devices. In a release build check startup time, scrolling, animations, error reporting and anything that depends on `__DEV__`.

### 289: How do you ask users to update the app?

For JS-only changes, `expo-updates` can check and apply updates at runtime:

```tsx
import * as Updates from "expo-updates";

async function checkForUpdate() {
  const result = await Updates.checkForUpdateAsync();
  if (result.isAvailable) {
    await Updates.fetchUpdateAsync();
    await Updates.reloadAsync();
  }
}
```

For native changes, the user must update from the store. Common approaches: your API returns a minimum supported app version and the app shows a blocking "please update" screen if it is older, or on Android you use Google Play's in-app updates API (via a library like `sp-react-native-in-app-updates`). Always keep your API backward compatible for a while, because many users don't update quickly.

### 290: How do you build a bottom sheet?

Options:

- `@gorhom/bottom-sheet`: the most popular library. Built on Reanimated and Gesture Handler, supports snap points, scrollable content and keyboard handling.
- Native sheets: React Navigation and Expo Router support `presentation: 'formSheet'` with `sheetAllowedDetents`, which uses the real platform sheet.
- Expo UI has native bottom sheet components.

```tsx
import BottomSheet, { BottomSheetView } from "@gorhom/bottom-sheet";

<BottomSheet snapPoints={["25%", "60%"]} index={0}>
  <BottomSheetView style={{ padding: 16 }}>
    <Text>Filters</Text>
  </BottomSheetView>
</BottomSheet>;
```

Native sheets feel the most "native". JS sheets give more control over custom designs.

### 291: How do you build a carousel?

For simple cases, a horizontal `FlatList` with `pagingEnabled` (or `snapToInterval`) works:

```tsx
const { width } = useWindowDimensions();

<FlatList
  horizontal
  pagingEnabled
  data={banners}
  keyExtractor={(b) => b.id}
  showsHorizontalScrollIndicator={false}
  renderItem={({ item }) => (
    <Image source={{ uri: item.url }} style={{ width, height: 200 }} />
  )}
  onMomentumScrollEnd={(e) =>
    setIndex(Math.round(e.nativeEvent.contentOffset.x / width))
  }
/>;
```

For effects like parallax, scaling neighbours or infinite loops, use `react-native-reanimated-carousel` or `react-native-pager-view` (native pager). Don't auto-scroll when a screen reader is on.

### 292: How do you implement search with debounce?

Update the input right away, but wait until the user stops typing before calling the API:

```tsx
function useDebounce<T>(value: T, delay = 300) {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const id = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(id);
  }, [value, delay]);
  return debounced;
}

function Search() {
  const [query, setQuery] = useState("");
  const debouncedQuery = useDebounce(query);

  const { data } = useQuery({
    queryKey: ["search", debouncedQuery],
    queryFn: ({ signal }) => searchProducts(debouncedQuery, { signal }),
    enabled: debouncedQuery.length > 1,
  });

  return (
    <TextInput value={query} onChangeText={setQuery} placeholder="Search" />
  );
}
```

Passing `signal` cancels old requests, so slow responses don't overwrite newer results.

### 293: How do you show skeleton loaders?

Render placeholder shapes with the same layout as the real content, and animate their opacity or a shimmer:

```tsx
function SkeletonRow() {
  const opacity = useSharedValue(0.4);

  useEffect(() => {
    opacity.value = withRepeat(withTiming(1, { duration: 800 }), -1, true);
  }, []);

  const style = useAnimatedStyle(() => ({ opacity: opacity.value }));

  return (
    <Animated.View
      style={[
        {
          height: 64,
          borderRadius: 8,
          backgroundColor: "#e5e5e5",
          marginBottom: 8,
        },
        style,
      ]}
    />
  );
}
```

Skeletons feel faster than a spinner because the layout doesn't jump when data arrives. Libraries like `moti` include ready-made skeleton components. Respect the reduce motion setting.

### 294: How do you prefetch images?

Download images before they are shown, so they appear instantly:

```tsx
import { Image } from "expo-image";

await Image.prefetch([
  "https://cdn.example.com/p/1.jpg",
  "https://cdn.example.com/p/2.jpg",
]);
```

The core `Image` component also has `Image.prefetch(url)`. Prefetch things the user is likely to see next, like the next page of a feed or the hero image of a screen they are about to open. Don't prefetch too much on mobile data.

### 295: How do you handle dates, time zones and number formatting?

Hermes supports the `Intl` API (`Intl.DateTimeFormat`, `Intl.NumberFormat`, `Intl.RelativeTimeFormat` and others), so you can format based on the user's locale:

```ts
new Intl.NumberFormat("de-DE", { style: "currency", currency: "EUR" }).format(
  1234.5,
);
// "1.234,50 €"

new Intl.DateTimeFormat(undefined, {
  dateStyle: "medium",
  timeStyle: "short",
}).format(new Date());
```

For date math, use `date-fns` or Day.js. Store and send dates as ISO strings in UTC, and convert to local time only for display. Avoid parsing non-standard date strings with `new Date('...')`, because engines handle them differently.

### 296: How do you show a toast or snackbar?

React Native has `ToastAndroid` for Android only:

```ts
ToastAndroid.show("Saved", ToastAndroid.SHORT);
```

For both platforms, use a library like `sonner-native`, `burnt` (native toasts) or `react-native-toast-message`, or build your own with an absolutely positioned animated view at the root of the app. Make sure toasts are announced to screen readers (`announceForAccessibility`) and don't hide important actions.

### 297: What are typed routes in Expo Router?

With typed routes, Expo Router generates TypeScript types from your `app/` folder, so `href` values and params are checked at compile time:

```json
{
  "expo": {
    "experiments": { "typedRoutes": true }
  }
}
```

```tsx
<Link href="/product/123" />          // OK
<Link href="/prodcut/123" />          // type error: route doesn't exist
router.push({ pathname: '/product/[id]', params: { id: '123' } });
```

The types are generated when you run `npx expo start`. This catches broken links after renaming or moving files.

### 298: How do you track screen views for analytics?

Listen to navigation state changes in one place instead of adding tracking code to every screen.

In Expo Router:

```tsx
import { Stack, usePathname } from "expo-router";

export default function RootLayout() {
  const pathname = usePathname();

  useEffect(() => {
    analytics.screen(pathname);
  }, [pathname]);

  return <Stack />;
}
```

In React Navigation, use the `onStateChange` prop of the navigation container and read the current route name with a navigation ref. Common analytics tools are Firebase Analytics, Amplitude, Mixpanel, PostHog and Segment. Ask for tracking consent where the law requires it, and use App Tracking Transparency on iOS if you track users across apps.

### 299: How do you keep the right aspect ratio for an image or video?

Use the `aspectRatio` style. Set one dimension and let the other be calculated:

```tsx
<Image
  source={{ uri: photo.url }}
  style={{ width: "100%", aspectRatio: photo.width / photo.height }}
/>
```

If you don't know the size, `Image.getSize(url)` returns the width and height of a remote image (it downloads it first, so it costs time). It's better to get the dimensions from your API, so the layout doesn't jump when the image loads.

### 300: How do you implement logout properly?

Logout should clear everything that belongs to the user:

1. Call the server to revoke the refresh token (if your auth supports it).
2. Delete tokens from secure storage.
3. Clear the data cache (`queryClient.clear()`), persisted stores and any local database tables with user data.
4. Unregister the push token on your server, so the device stops receiving the user's notifications.
5. Reset the navigation to the sign-in screen (with auth-based screens, this happens automatically when auth state changes).
6. Reset analytics and crash reporting user IDs.

If you forget the cache, the next user on the same device may briefly see the previous user's data.

---

## Advanced Questions (301-450)

### 301: Explain the parts of the New Architecture and how they fit together.

- **JSI (JavaScript Interface)**: a C++ API that lets the JS engine hold references to C++ objects and call C++ functions directly. Everything else is built on it.
- **Fabric**: the renderer. React's output becomes a C++ shadow tree, layout is calculated with Yoga, and changes are applied to native views. It supports synchronous rendering and concurrent React.
- **Turbo Modules**: native modules exposed through JSI. They load lazily (only when first used) and can be sync or async.
- **Codegen**: generates type-safe C++/native interfaces from TypeScript specs for modules and components.
- **Bridgeless mode**: the runtime no longer starts the old bridge at all. Timers, errors and events go through the new systems.

Together they remove JSON serialization between JS and native, allow sharing C++ code between platforms, and let React Native follow React's rendering model closely.

### 302: How did the old bridge work, and what problems did it cause?

In the old architecture, JS and native lived in separate worlds. All communication was turned into JSON messages, queued and sent asynchronously in batches over the bridge. The UI was described by UIManager commands like "create view 12 with these props".

Problems:

- **Serialization cost**: large data (lists, images as base64) was slow to send.
- **Everything async**: you couldn't read layout or native values synchronously, so measuring views caused flicker.
- **Congestion**: many events (scroll, gestures) could fill the queue and delay other work.
- **Startup cost**: all native modules were initialized at startup, even unused ones.
- **No concurrent React**: the renderer couldn't support interruptible rendering.

The New Architecture fixes these with JSI, Fabric and Turbo Modules.

### 303: What is JSI in more detail?

JSI is a thin C++ interface over the JavaScript engine. Native code can:

- Create **host functions**: C++ functions callable from JS as normal functions.
- Create **host objects**: C++ objects whose properties and methods are visible in JS.
- Read and write JS values (`jsi::Value`, `jsi::Object`, `jsi::Array`, `jsi::ArrayBuffer`) without serialization.

```cpp
auto add = jsi::Function::createFromHostFunction(
  runtime, jsi::PropNameID::forAscii(runtime, "nativeAdd"), 2,
  [](jsi::Runtime& rt, const jsi::Value&, const jsi::Value* args, size_t) {
    return jsi::Value(args[0].asNumber() + args[1].asNumber());
  });
runtime.global().setProperty(runtime, "nativeAdd", std::move(add));
```

Because JSI is engine-agnostic, React Native can work with Hermes or another engine. Libraries like MMKV, Reanimated, VisionCamera and op-sqlite use JSI directly for speed. JSI calls must happen on the JS thread that owns the runtime.

### 304: What are the phases of the Fabric rendering pipeline?

1. **Render**: React runs your components and creates React elements. Fabric creates a matching **shadow tree** of C++ shadow nodes, one per host component, with their props.
2. **Commit**: Yoga calculates layout for the new tree, and the tree is promoted to be the "next tree to mount". Layout and commit can run on a background thread.
3. **Mount**: Fabric compares the new tree with the previous one (diffing), produces a list of mutations (create, update, delete, insert) and applies them to the native views on the UI thread.

Because the shadow tree is in C++ and shared across platforms, most rendering logic is the same on iOS and Android. Only the mount phase talks to platform views.

### 305: Why is the shadow tree immutable in Fabric?

Each commit creates a new version of the shadow tree. Unchanged nodes are shared between versions (structural sharing), and changed nodes are cloned. Nothing is mutated in place.

This makes it safe for several threads to read trees at the same time: the UI thread can mount one version while a background thread computes layout for the next. It also allows React to prepare several possible trees (for transitions) and commit only the one that wins, which is required for concurrent rendering. It is the same idea as immutable state in React.

### 306: Which threads do the render, commit and mount phases run on?

It depends on what triggered the update:

- A normal React update: **render** runs on the JS thread, **commit** (including layout) can run on the JS thread or a background thread, and **mount** runs on the UI thread.
- A high-priority event on the UI thread (for example a synchronous event or a native-driven update) can run render and commit synchronously, which is what makes synchronous layout reads possible.
- State updates coming from native (like a `ScrollView` content size change) can go straight to commit without JS.

The important part for interviews: JS work, layout and native mounting are separated, and the C++ core lets React Native move work between threads safely.

### 307: What is view flattening?

Many `View`s in a React tree exist only for layout (padding, flex direction) and never draw anything. Fabric detects these "layout-only" views and doesn't create native views for them. Their children are mounted directly into the nearest real ancestor, with positions adjusted.

This reduces the number of native views, which saves memory and makes mounting faster. A view is kept if it has something visible or interactive: a background color, border, event handler, `testID` in some cases, accessibility props, or `collapsable={false}`. When you need a real native view (for example for a native library that measures it), set `collapsable={false}`.

### 308: What is bridgeless mode?

Bridgeless mode is the final step of the New Architecture, where the old bridge is not created at all. It became the default in 0.74 and the only mode once the legacy architecture was removed.

Things that used to go through the bridge (timers, error handling, global event emitters, the JS runtime setup) were moved to new implementations on top of JSI and the `ReactHost`/`RCTHost` classes. The benefit is faster startup, less memory and less code. The legacy interop layer lets many old modules keep working, but code that called bridge APIs directly (like `CatalystInstance` on Android) had to be updated. `CatalystInstanceImpl` was removed in 0.85.

### 309: What does lazy loading of Turbo Modules mean for startup?

In the old architecture, all native modules were created when the app started, even if a screen that uses them never opened. With many libraries, this added noticeable startup time.

Turbo Modules are created the first time JavaScript accesses them (through `TurboModuleRegistry.get`). So an app with 80 native modules only pays for the few needed on the first screen. This is another reason to avoid importing heavy modules at the top level of your entry file: with inline requires and lazy modules, startup work is only done when needed.

### 310: What are C++ Turbo Modules and why use them?

A C++ Turbo Module is a native module written once in C++ and shared by iOS and Android, instead of writing it twice in Swift/Objective-C and Kotlin/Java.

```cpp
class NativeMathModule : public NativeMathModuleCxxSpec<NativeMathModule> {
 public:
  NativeMathModule(std::shared_ptr<CallInvoker> jsInvoker)
      : NativeMathModuleCxxSpec(std::move(jsInvoker)) {}

  double fibonacci(jsi::Runtime& rt, double n) {
    // shared logic for both platforms
  }
};
```

Good use cases: algorithms, parsing, encryption, image processing, or wrapping an existing C/C++ library. You still need a small amount of platform code to register the module. For code that needs platform APIs (camera, notifications), use platform languages or Expo Modules instead.

### 311: How does Codegen work for a Fabric native component?

You describe the component's props in a TypeScript spec using `codegenNativeComponent`:

```ts
// specs/RatingViewNativeComponent.ts
import type { ViewProps, CodegenTypes, HostComponent } from "react-native";
import { codegenNativeComponent } from "react-native";

interface NativeProps extends ViewProps {
  rating?: CodegenTypes.Double;
  maxStars?: CodegenTypes.WithDefault<CodegenTypes.Int32, 5>;
  onRatingChange?: CodegenTypes.DirectEventHandler<{
    value: CodegenTypes.Double;
  }>;
}

export default codegenNativeComponent<NativeProps>(
  "RatingView",
) as HostComponent<NativeProps>;
```

Codegen generates C++ props classes, event emitters, a shadow node and component descriptor, plus platform interfaces. You then write the platform view (a `UIView` subclass registered with Fabric on iOS, a `SimpleViewManager` with the generated delegate on Android). The exact import paths for Codegen types changed with the Strict TypeScript API, so check the docs for your version.

### 312: How do you call imperative methods on a native component?

Use view commands. You declare them with `codegenNativeCommands`:

```ts
import { codegenNativeCommands } from "react-native";

interface NativeCommands {
  play: (viewRef: React.ElementRef<HostComponent<NativeProps>>) => void;
  seekTo: (
    viewRef: React.ElementRef<HostComponent<NativeProps>>,
    seconds: CodegenTypes.Double,
  ) => void;
}

export const Commands = codegenNativeCommands<NativeCommands>({
  supportedCommands: ["play", "seekTo"],
});

// usage
Commands.seekTo(playerRef.current!, 30);
```

The native side implements `handleCommand` (iOS) or `receiveCommand` (Android). Commands are for actions ("play", "focus", "scroll"), while state ("isPlaying") should be props. With the Expo Modules API you can define `AsyncFunction`s on a view instead.

### 313: What is the interop layer and should you rely on it?

The interop layer lets components and modules written for the old architecture run in a New Architecture app. Legacy view managers are wrapped so Fabric can render them, and legacy modules are exposed through the Turbo Module system.

It made the migration possible for apps with many old libraries. But it has limits: legacy components don't support synchronous layout or concurrent features, some APIs (direct UIManager access, `setNativeProps` behavior, custom bridge use) don't work fully, and performance is worse than native New Architecture code. React Native keeps removing legacy code, so treat the interop layer as temporary. Upgrade or replace those libraries.

### 314: How do you migrate an old native module to a Turbo Module?

1. Write a TypeScript spec (`NativeMyModule.ts`) that matches the existing JS API.
2. Add `codegenConfig` to `package.json` so Codegen generates the interfaces.
3. On iOS, make the module conform to the generated protocol (`NativeMyModuleSpec`) and implement `getTurboModule:` returning the generated JSI wrapper.
4. On Android, extend the generated `NativeMyModuleSpec` class instead of `ReactContextBaseJavaModule`, and register it in a `BaseReactPackage`.
5. Replace `NativeModules.MyModule` with `TurboModuleRegistry.getEnforcing<Spec>('MyModule')` in JS.
6. Update anything that used bridge-specific APIs (`RCTBridge`, `CatalystInstance`).

Alternatively, rewrite it with the Expo Modules API, which is often less code and supports both architectures' concepts with one API.

### 315: How is Hermes different from engines like V8 or JavaScriptCore?

Hermes was designed for mobile apps, not browsers:

- **Ahead-of-time compilation**: JS is compiled to bytecode at build time, so the app doesn't parse source on startup.
- **No JIT**: it doesn't compile hot code to machine code at runtime. This keeps memory low and startup fast, and fits iOS rules that restrict JIT. Peak performance in long-running CPU-heavy loops can be lower than V8.
- **Memory-mapped bytecode**: the bundle is mapped into memory and pages are loaded on demand.
- **GC tuned for mobile**: the Hades garbage collector does most work concurrently, so pauses are short.

Hermes supports modern JS (ES2023+ features, `async`/`await`, `Intl`, `Proxy`), but a few rarely used features may differ, so check if you depend on something unusual.

### 316: What changed with Hermes V1?

Hermes V1 is the next generation of the engine, which became the default in React Native 0.84 after being experimental in 0.82. It brings a redesigned compiler and VM with better performance for real app code, better support for modern JavaScript (for example ES6 classes and block scoping without transpiling to older code), and improvements that came out of the "Static Hermes" project.

For most apps there is nothing to change. If you hit a problem, you can opt out by pinning the older `hermes-compiler` version in `package.json` and setting `hermesV1Enabled=false` (Android) or `RCT_HERMES_V1_ENABLED=0` (iOS). Since less Babel transpiling is needed, bundles can be smaller and faster.

### 317: What happened to JavaScriptCore support?

JavaScriptCore (JSC), the engine used before Hermes became the default, was moved out of core in 0.79 into a community package, `@react-native-community/javascriptcore`. React Native no longer ships or tests it as part of each release.

Reasons: Hermes is the default for almost everyone, maintaining two engines slows the core team down, and the New Architecture work (event loop, DevTools, performance tracing) is built around Hermes. Some apps still use JSC, for example to match Safari behavior exactly, but most should stay on Hermes.

### 318: How does Metro build a bundle?

Metro has three main stages:

1. **Resolution**: starting from the entry file, it finds each imported module. It follows Node-style resolution with React Native rules: platform extensions (`.ios.js`, `.native.js`), the `react-native` field and `exports` conditions in `package.json`.
2. **Transformation**: each file is transformed with Babel (and the Hermes-friendly preset) into a module format Metro understands. Results are cached by file content, which is why `--reset-cache` sometimes fixes strange errors.
3. **Serialization**: all modules are combined into one bundle with a small module system (`__d` to define, `__r` to require), plus a source map.

In development, Metro keeps the dependency graph in memory and sends only changed modules for Fast Refresh. Metro 0.87 (React Native 0.87) made source map generation about twice as fast and cut memory use roughly in half.

### 319: What are inline requires and how do they help startup?

By default, all `import`s at the top of a file run when the file is first loaded, which means every module in the import graph runs at startup. With inline requires, Metro rewrites imports so a module is only required the first time one of its exports is used:

```js
// Your code
import { heavyFormatter } from "./heavy";
export function format(x) {
  return heavyFormatter(x);
}

// After the inline requires transform (simplified)
export function format(x) {
  return require("./heavy").heavyFormatter(x);
}
```

Code for screens the user hasn't opened never runs. Enable it in `metro.config.js` with `transformer.getTransformOptions` returning `{ transform: { inlineRequires: true } }` (Expo's config enables it). Watch out for modules with side effects at the top level, because they will run later than before.

### 320: How do you symbolicate a production crash?

Production stack traces point to minified bundle positions and native memory addresses, which are unreadable. To make them readable:

- **JS errors**: generate source maps at build time (Hermes builds produce a composed source map from the Metro map and the Hermes map) and upload them to your crash reporter for each release and each OTA update.
- **iOS native crashes**: upload dSYM files from the Xcode archive.
- **Android native crashes**: upload the R8/ProGuard `mapping.txt` for Java/Kotlin, and native debug symbols for C++ libraries.

Tools like the Sentry CLI and EAS upload these automatically. Make sure the release name and OTA update ID match, otherwise the wrong map is used.

### 321: How does the event loop work in the New Architecture?

The New Architecture has a defined event loop model that is aligned with the web. Each loop iteration:

1. Runs one task (a JS callback from a timer, a native event, a Turbo Module promise resolution).
2. Runs all microtasks (`Promise.then`, `queueMicrotask`).
3. Runs the rendering step: React updates queued during the task are committed and mounted, and layout effects run.

This order makes behavior predictable. For example, all state updates from one event are batched into one frame, and `useLayoutEffect` sees the committed layout before the user sees the frame. It also enabled web APIs like `requestIdleCallback`, `PerformanceObserver` and `IntersectionObserver` (behind flags in some versions).

### 322: What is web-based event dispatching in React Native 0.88?

Starting in 0.88, React Native dispatches events using the W3C `EventTarget` model by default, the same model as the DOM. Events go through a real capture phase and bubble phase along the native view tree, and support `stopPropagation()` and `preventDefault()` like on the web.

Before, events went through a React Native-specific plugin system. For app code nothing breaks, but code that reached into the old event internals may need updates. On the Canary channel you can also call `addEventListener`, `removeEventListener` and `dispatchEvent` on native refs. This is part of a longer effort to make React Native behave like the DOM where it makes sense, which makes sharing code with the web easier.

### 323: What are DOM Node APIs on React Native refs?

Since 0.82, refs to host components implement a subset of the DOM `Element` and `Node` interfaces:

```tsx
const ref = useRef<View>(null);

useLayoutEffect(() => {
  const node = ref.current;
  if (!node) return;
  const rect = node.getBoundingClientRect();
  const parent = node.parentNode;
  const childCount = node.children.length;
  const contains = node.contains(otherNode);
}, []);
```

Before, you only had React Native methods like `measure`. These APIs read from the committed shadow tree synchronously, and make it possible to write cross-platform logic (for example a tooltip positioning library) that works with both `react-dom` and React Native. `measure` and the old methods still work.

### 324: How do you measure app startup time?

Separate cold start (process not running), warm start (process alive, activity recreated) and hot start (app in background). Measure:

- **Time to first frame**: until the first screen is drawn.
- **Time to interactive (TTI)**: until the user can actually use the screen with real content.

Tools:

- Android: `adb shell am start -W` gives `TotalTime`, and Android Studio/Perfetto traces show where time goes.
- iOS: Instruments' App Launch template and the Xcode Organizer's launch time metrics from real users.
- React Native: `performance.mark()` and `performance.measure()` in JS, and the DevTools Performance panel.
- Production: Sentry, Firebase Performance, EAS Observe.

Always measure release builds on real, low-end devices.

### 325: What can you do to make a large app start faster?

- Keep Hermes and use the precompiled iOS binaries (default since 0.84) so builds and startup are efficient.
- Use inline requires and lazy screens, so only first-screen code runs.
- Delay SDK initialization (analytics, chat, ads) until after the first frame, with `requestIdleCallback` or after the first screen mounts.
- Avoid large JSON parsing on startup. Store data in SQLite or MMKV and read only what you need.
- Reduce the work in root providers: big context trees, store hydration and heavy synchronous logic.
- Avoid huge images and fonts on the first screen.
- Check native startup code: libraries that do work in `Application.onCreate` or `AppDelegate`.

Profile first, then fix the biggest item. Startup problems usually have a few large causes, not many small ones.

### 326: How do you profile JavaScript performance?

Use the React Native DevTools **Performance** panel (0.83+). Record a trace while doing the slow action. It shows:

- JS execution on a timeline with flame charts, so you see which functions take time
- React tracks with component renders and commits
- Custom `performance.mark` and `performance.measure` entries
- Network events

The **Profiler** tab shows React render timings per component. For a quick check, the Performance Monitor overlay shows JS and UI FPS. Profile in a release-like build when possible, because development mode adds a lot of overhead and can mislead you.

### 327: How do you profile native performance?

- **Android**: Android Studio Profiler (CPU, memory, energy), Perfetto/systrace traces (React Native emits trace sections you can see next to native work), and GPU overdraw debugging in developer options.
- **iOS**: Xcode Instruments: Time Profiler for CPU, Allocations and Leaks for memory, Core Animation for dropped frames, and the View Debugger for the view hierarchy.

Use native profiling when the UI FPS drops while the JS FPS is fine, when memory grows without JS heap growth, or when startup time is spent before JS runs. These problems are often caused by too many native views, large bitmaps, expensive shadows or a native library.

### 328: The UI FPS is fine but the JS FPS drops while scrolling a list. How do you fix it?

A JS FPS drop means the JS thread is busy, probably rendering list items. Steps:

1. Profile with the React Profiler to find which components render during scroll and how long they take.
2. Make item components cheap: memoize them, move formatting out of render, and avoid inline objects (or use the React Compiler).
3. Make sure parent state changes (like a scroll position stored in state) don't re-render the whole list. Use animated values for scroll-linked UI instead of `useState`.
4. Switch to FlashList so items are recycled instead of created.
5. Tune `windowSize` and batching props.
6. Move expensive work (like filtering) out of render or into `useMemo`, or off the main JS path.

Never update React state on every `onScroll` event.

### 329: How do you investigate memory growth in a React Native app?

1. Reproduce it: repeat an action (open and close a screen 20 times) and watch memory in Android Studio Profiler or Xcode's memory gauge.
2. Check the **JS heap**: take heap snapshots in React Native DevTools before and after, and compare which objects grew (detached components, big arrays, closures holding data).
3. Check **native memory**: images are the usual cause. Large bitmaps decoded at full size take a lot of memory. Also check native views that are never released and native SDKs.
4. Look for listeners and subscriptions that are not removed, timers that keep running, and global caches without limits.
5. Remember that screens in a stack stay mounted. Ten nested product screens means ten product screens in memory.

Fix and measure again. Some memory growth is normal caching, so look for growth that never goes down.

### 330: How does FlashList v2 recycling work, and what pitfalls does it have?

FlashList keeps a pool of item components. When an item scrolls out of view, its component isn't unmounted. It is moved and re-rendered with the props of a new item. Creating and destroying fewer components makes scrolling smooth.

v2 was rewritten for the New Architecture. It measures items synchronously, so you don't need `estimatedItemSize` anymore, and it supports `masonry` layouts and `maintainVisibleContentPosition`.

Pitfalls:

- Local state in item components "leaks" to the next item. Reset it when the item ID changes (or use `useRecyclingState` provided by FlashList).
- Use `getItemType` when rows have very different layouts, so a header isn't recycled into a product card.
- Avoid `key` props inside items, since they prevent recycling.
- Effects in items run again with new data, so they must handle prop changes.

### 331: How do you avoid re-rendering every list row when one row's data changes?

- Pass only the item's ID or its own data to each row, not the whole list.
- In global stores, have each row subscribe to its own slice with a selector:

```tsx
const ProductRow = memo(function ProductRow({ id }: { id: string }) {
  const product = useCartStore((s) => s.products[id]);
  const quantity = useCartStore((s) => s.quantities[id] ?? 0);
  return <Row product={product} quantity={quantity} />;
});
```

- Use normalized data (a map by ID), so updating one product creates a new object only for that product.
- Pass `extraData` to `FlatList` only when the change actually affects rendering.

With this setup, changing one quantity re-renders only one row.

### 332: Why can large images crash an app, and how do you prevent it?

An image takes memory based on its decoded pixel size, not its file size. A 4000x3000 photo is about 48 MB in memory (4 bytes per pixel), even if the JPEG file is 2 MB. A feed with several of those can run out of memory, especially on Android.

Prevent it by:

- Requesting images at the displayed size from a CDN (with `PixelRatio`).
- Using `expo-image`, which downsamples images to the view size and manages caches.
- Resizing user-picked photos before uploading or displaying (`expo-image-manipulator`).
- Clearing memory caches when the OS warns about low memory.
- Not keeping many full-size images in memory at once.

### 333: How does Reanimated run animations on the UI thread?

Reanimated creates a second JavaScript runtime on the UI thread. Functions marked as worklets (including the callbacks of `useAnimatedStyle`, gestures and `withTiming`) are copied to that runtime by a Babel plugin, along with the values they capture.

Shared values live in C++ and can be read from both runtimes. When a shared value changes on the UI thread, the animated styles that depend on it are re-run there, and the new props are applied directly to native views each frame, without React rendering. React only learns about the final values when needed. This is why Reanimated animations stay smooth even when the JS thread is blocked. In Reanimated 4, the worklet runtime code lives in `react-native-worklets`.

### 334: How do you call JS-thread code from a worklet and vice versa?

Worklets on the UI runtime can't call normal JS functions directly. You schedule them on the other thread:

```tsx
import { scheduleOnRN, scheduleOnUI } from "react-native-worklets";

const pan = Gesture.Pan().onEnd((e) => {
  if (e.translationX > 120) {
    scheduleOnRN(onSwipeRight, itemId); // runs on the JS thread
  }
});

scheduleOnUI(() => {
  "worklet";
  offset.value = withSpring(0);
});
```

In Reanimated 3 and older code you will see `runOnJS(fn)(args)` and `runOnUI(fn)(args)`, which do the same thing. Data passed between threads is copied, so don't send large objects on every frame.

### 335: What is the Shared Animation Backend in React Native 0.85?

It is a new internal animation engine in React Native core, built with Software Mansion. Both `Animated` and Reanimated use it to apply animation updates to views.

Two benefits:

- `Animated` with `useNativeDriver: true` can now animate layout props like `width`, `height`, `flex`, margins and positions. Before, the native driver only supported non-layout props like `opacity` and `transform`.
- Reanimated can rely on core code for applying updates and reconciling them with React, which makes it faster and more stable across React Native versions.

It started as opt-in through the experimental channel (from 0.85.1). In interviews, the key point is that layout animations no longer force you to run the animation on the JS thread.

### 336: How do you compose multiple gestures?

Gesture Handler has composition functions:

- `Gesture.Simultaneous(a, b)`: both can be active together, like pinch and rotate on a photo.
- `Gesture.Exclusive(a, b)`: only one can win, in priority order, like double tap before single tap.
- `Gesture.Race(a, b)`: the first to activate wins and cancels the others.

```tsx
const doubleTap = Gesture.Tap()
  .numberOfTaps(2)
  .onEnd(() => scheduleOnRN(like));
const singleTap = Gesture.Tap().onEnd(() => scheduleOnRN(openDetails));
const pinch = Gesture.Pinch().onChange((e) => {
  scale.value *= e.scaleChange;
});
const rotate = Gesture.Rotation().onChange((e) => {
  rotation.value += e.rotationChange;
});

const gesture = Gesture.Simultaneous(
  Gesture.Exclusive(doubleTap, singleTap),
  Gesture.Simultaneous(pinch, rotate),
);
```

You can also connect gestures in different components with `simultaneousWithExternalGesture` and `requireExternalGestureToFail`, for example to make a horizontal swipe work inside a vertical list.

### 337: How do you keep the JS thread free during heavy computation?

Options, from simplest to most complex:

1. **Split the work** into chunks and yield between them (`setTimeout`, `requestIdleCallback`), so the UI keeps responding.
2. **Use `startTransition`** for heavy renders, so urgent updates (typing) come first.
3. **Move work to the server** if possible (search, aggregation).
4. **Use a separate JS runtime**: libraries like `react-native-worklets` (worker runtimes) or `react-native-worklets-core` let you run functions on background threads.
5. **Write a native or C++ module** for CPU-heavy work like image processing, crypto or parsing large files.

There are no browser Web Workers in React Native core. Keep in mind that data passed to another runtime is copied, so the overhead must be smaller than the work you save.

### 338: How do you analyze and reduce the JavaScript bundle size?

Analyze:

- **Expo Atlas**: `EXPO_ATLAS=true npx expo start` (or export) gives an interactive map of modules and their sizes.
- **source-map-explorer** on a production bundle and source map.

Reduce:

- Replace heavy libraries (for example `moment` with `date-fns` or Day.js, lodash with per-function imports or native methods).
- Check that packages don't pull in web-only or Node polyfills.
- Remove dead code and old feature flags.
- Use Expo's tree shaking (experimental, `EXPO_UNSTABLE_TREE_SHAKING`) or make sure libraries are side-effect free.
- Move large static data (JSON) out of the bundle into assets or the server.

A smaller bundle means less bytecode to load at startup and smaller OTA updates.

### 339: Does code splitting work in React Native?

Not like on the web. By default, the whole app is one bundle inside the binary, so there is nothing to download later. `React.lazy` and dynamic `import()` work, but in a native release build they mostly delay when code is _evaluated_, not when it is downloaded. That still helps startup, together with inline requires.

Real bundle splitting is available in Expo for web and with async routes in Expo Router, and tools like Re.Pack (a Rspack/Webpack-based bundler by Callstack) support module federation and downloading code chunks at runtime. Remote code loading must respect App Store rules, so it's mostly used for big "super apps".

### 340: How would you structure a large React Native codebase?

A structure that scales:

- **Feature folders**: `features/cart/`, `features/auth/` with their own screens, components, hooks, API calls and tests.
- **Shared layers**: `ui/` (design system), `lib/` (API client, storage, analytics), `navigation/` or `app/` (routes).
- **Clear boundaries**: features talk through public exports, not deep imports. ESLint rules can enforce this.
- **Server state vs client state**: TanStack Query (or similar) for server data, a small store for client state.
- **Monorepo** if you share code with a web app or have several apps.
- **Native code in modules**: Expo local modules or packages, not scattered in `ios/` and `android/`.

Also have strict TypeScript, CI checks, and an upgrade schedule. Large React Native apps get hard to maintain mostly because of outdated dependencies, not because of folder structure.

### 341: How do you build a design system for React Native?

- Define **tokens**: colors (semantic names like `background`, `textMuted`, `danger`), spacing, radii, typography, shadows, for light and dark modes.
- Build **primitives**: `Box`, `Text`, `Stack`, `Pressable` wrappers that use tokens and support accessibility props.
- Build **components** on top: `Button`, `Input`, `Card`, `Sheet`, `Toast`, with variants and sizes.
- Make every interactive component accessible by default (roles, labels, states, minimum touch size).
- Document and test them with Storybook for React Native and visual regression tests.
- If you also have a web app, share tokens (and maybe components through React Native Web, Tamagui or similar).

Keep platform differences inside the components, so screens don't need `Platform.OS` checks.

### 342: How do you resolve conflicts in offline sync?

When the same data is changed offline on two devices (or offline and on the server), you need a rule:

- **Last write wins**: simplest, using timestamps or versions. Can lose data.
- **Field-level merge**: merge changes to different fields, conflict only if the same field changed.
- **Server-side rules**: the server decides (for example, inventory can't go below zero) and returns the final state.
- **Ask the user**: show both versions for important data like documents.
- **CRDTs**: data structures that merge automatically (Yjs, Automerge), for collaborative editing.

Use a version number or `updatedAt` per record, send changes as operations ("add item 5") instead of full documents when possible, and make operations idempotent so retries don't apply them twice.

### 343: How do you implement optimistic updates?

Update the UI right away, send the request, and roll back if it fails. With TanStack Query:

```tsx
const mutation = useMutation({
  mutationFn: (postId: string) => api.likePost(postId),
  onMutate: async (postId) => {
    await queryClient.cancelQueries({ queryKey: ["post", postId] });
    const previous = queryClient.getQueryData<Post>(["post", postId]);
    queryClient.setQueryData<Post>(
      ["post", postId],
      (p) => p && { ...p, liked: true, likes: p.likes + 1 },
    );
    return { previous };
  },
  onError: (_err, postId, context) => {
    queryClient.setQueryData(["post", postId], context?.previous);
  },
  onSettled: (_data, _err, postId) => {
    queryClient.invalidateQueries({ queryKey: ["post", postId] });
  },
});
```

React 19's `useOptimistic` works for state inside a component. On mobile, optimistic UI matters a lot because network latency is often high.

### 344: How do you build reliable real-time features on mobile?

Mobile connections drop often, and the OS suspends sockets in the background. A reliable setup:

- Use WebSockets (or a service like Ably, Pusher, Supabase Realtime, Socket.IO) for live updates.
- Reconnect with exponential backoff and jitter when the connection drops.
- Close the socket when the app goes to the background and reconnect on `active`, then fetch missed events since the last known ID or timestamp.
- Use push notifications for events while the app is in the background.
- Send heartbeats to detect dead connections.
- Make the server the source of truth, and treat socket messages as hints to update or refetch.

### 345: What limits does iOS place on background work?

iOS is strict:

- After the app goes to the background, it has only a short time (usually seconds) to finish work, unless it starts a background task with `beginBackgroundTask`, which still gives only a limited time.
- Periodic tasks (`BGAppRefreshTask`, `BGProcessingTask`) run when iOS decides, based on usage patterns, battery and network. They may not run at all if the user rarely opens the app or force-quits it.
- Long-running background work is only allowed for specific modes: audio, location, VoIP, Bluetooth and a few others, and Apple reviews their use.
- Silent push notifications are throttled.

So design features to sync on launch and foreground, use push for important events, and treat background tasks as "nice to have".

### 346: How would you design push notifications for a large app?

- Store device tokens on the server per user and per device, with platform, app version and last seen date. Remove tokens that APNs/FCM report as invalid.
- Send through a queue so big campaigns don't overload your servers or the providers' rate limits.
- Use notification categories/channels so users can turn off types (marketing vs transactional). Android channels are required.
- Include a deep link URL in the payload, and handle taps from cold start and background.
- Support rich notifications (images, actions) with a Notification Service Extension on iOS.
- Respect quiet hours, localization and user preferences on the server.
- Track delivery and open rates.

Never put sensitive data in the notification body, because it shows on the lock screen.

### 347: How do you make deep links secure?

Deep links are input from outside the app, so treat them like untrusted user input:

- Validate and parse params. Don't pass raw URL values into API calls, SQL or a web view.
- Don't perform actions directly from a link (like "transfer money" or "delete account") without user confirmation and authentication.
- Use universal links and App Links (verified domains) for sensitive flows, since anyone can register a custom scheme.
- For OAuth redirects, use PKCE and check the `state` parameter.
- For magic login links, use short-lived, single-use tokens.
- Protect authenticated screens: after a deep link, check auth and redirect to login, then continue to the target.

### 348: How do Keychain and Keystore protect data?

- **iOS Keychain** stores small secrets encrypted by the system, tied to the app (and optionally an access group for sharing between apps). You can control when items are readable, for example only after first unlock or only when the device is unlocked, and require Face ID or the passcode.
- **Android Keystore** stores cryptographic keys in hardware (TEE or StrongBox) when available. The keys can't be exported. Libraries use a Keystore key to encrypt values stored in `SharedPreferences` or a file.

`expo-secure-store` and `react-native-keychain` wrap both. Data in these stores is safe from other apps and from someone reading a backup, but not from code running inside your own app, so avoid exposing secrets to JS more than needed.

### 349: What are the trade-offs of certificate pinning?

Benefits: it stops attackers from reading traffic with a fake but trusted certificate, for example on a device with a malicious root certificate or in corporate interception.

Costs and risks:

- When your certificate or key changes and the app doesn't have a matching pin, every user loses access until they update. Always pin a backup key and plan rotations.
- It makes debugging with proxies (Charles, Proxyman) harder. Disable it in debug builds.
- It can be bypassed on rooted or jailbroken devices with tools like Frida, so it is not full protection.
- CDNs and third-party APIs may change certificates without warning, so usually only pin your own API.

Use it for high-risk apps (banking, health) and be careful with operations.

### 350: How hard is it to reverse engineer a React Native app, and what can you do about it?

Not very hard. An attacker can unpack the APK or IPA, get the Hermes bytecode bundle and disassemble or decompile it with tools like `hbctool` or `hermes-dec`. Strings, API URLs and logic are visible. Native code can be inspected too.

What you can do:

- Keep secrets and important business logic on the server.
- Minify and strip debug info (default in release builds). Obfuscators for JS exist but add limited protection.
- Use R8 for Android native code, and consider commercial app protection tools for high-risk apps.
- Use Play Integrity and App Attest so your server can check that requests come from a real app.
- Detect tampering and hooking at runtime as an extra layer.

Assume the client is fully visible to attackers and design the API so that it is safe anyway.

### 351: How do you make OTA updates secure?

An OTA update replaces the code your app runs, so an attacker who can push a fake update controls the app. Protect it with:

- **HTTPS** for the update server (always).
- **Code signing**: EAS Update and `expo-updates` support end-to-end code signing. You sign updates with a private key you keep, and the app ships with the public certificate. The app refuses any update whose signature doesn't match, even if the update server is compromised.
- **Limited access**: only CI should be able to publish to production channels, not every developer laptop.
- **Audit**: record who published which update and from which commit.

If you self-host updates with the `expo-updates` protocol, the same signing approach applies.

### 352: How would you roll out OTA updates safely?

- Publish to a staging channel first and test on internal builds.
- Use a **gradual rollout**: EAS Update can roll out an update to a percentage of users (`eas update --rollout-percentage`), then increase it.
- Watch crash rates and key metrics, grouped by update ID.
- Have a **rollback** plan: republish the previous update with `eas update:republish`, or roll back to the update embedded in the build.
- Use the `fingerprint` runtime version policy so updates never reach incompatible binaries.
- Decide when updates apply: on next cold start (safe default), or immediately with a prompt for critical fixes.
- `expo-updates` has emergency launch: if an update crashes on launch, the app falls back to the previous working version.

### 353: What is the difference between a JS error, a native crash and an ANR?

- **JS error**: an exception in JavaScript. In development you see a red screen. In release, an uncaught fatal JS error closes the app, unless an error boundary or global handler catches it. You need source maps to read the stack.
- **Native crash**: an exception or signal in Swift, Kotlin, Objective-C, Java or C++ code (null pointer, out of memory, bad access). The process dies immediately. You need dSYMs or mapping files to read the stack.
- **ANR (Application Not Responding)**: Android shows a dialog when the main thread is blocked for about 5 seconds. Google Play tracks the ANR rate and ranks apps with a high rate lower.

All three should be tracked separately in your crash reporting tool, with different fixes.

### 354: What causes ANRs in React Native apps on Android?

ANRs happen when the Android main (UI) thread is blocked. Common causes:

- Heavy native work on the main thread at startup (SDK initialization in `Application.onCreate`, large file or database reads).
- Synchronous native module methods that do slow work and are called on the main thread.
- Synchronous JSI calls that block the UI thread while waiting for the JS thread (or the other way around), causing a deadlock.
- Broadcast receivers or services that take too long.
- Too many or too complex views being mounted at once.

Check the ANR traces in Google Play Console (they show the main thread stack). Move I/O to background threads and keep startup work minimal.

### 355: What is the iOS watchdog and why might it kill your app?

iOS has a watchdog that kills apps that take too long in certain transitions, mainly launching (roughly 20 seconds before the first frame), resuming and going to the background. Crash reports show it with the exception code `0x8badf00d` ("ate bad food").

In React Native, it can be triggered by heavy work in `AppDelegate` before the root view appears, a slow synchronous native module call on the main thread, or a main-thread deadlock. Also, iOS kills apps that use too much memory (jetsam events), which look like crashes without a stack trace. Keep launch work light, and check Xcode Organizer for watchdog and memory terminations.

### 356: How do you integrate React Native into an existing native app?

Steps on a high level:

1. Add React Native as a dependency (often in a separate folder or package), and set up Metro and Codegen.
2. **iOS**: add the React Native pods (or prebuilt binaries), create an `RCTReactNativeFactory`, and use it to create a root view for a module name. Show that view inside a `UIViewController`.
3. **Android**: create a `ReactHost` in your `Application` (implement `ReactApplication`), and show React Native screens in a `ReactActivity` or a fragment.
4. Pass initial props (user ID, auth token) into the React Native root, and use native modules for calls back to the host app.
5. In release builds, bundle the JS into the app.

Hard parts: navigation between native and React Native screens, sharing auth, keeping native dependency versions compatible, and team ownership. Tools like `expo-brownfield` and Callstack's guides help, and some teams ship the React Native part as a prebuilt framework/AAR to the native team.

### 357: What is the iOS SceneDelegate change in React Native 0.88?

Apple is moving all apps to the UIScene lifecycle, where windows are managed by a `SceneDelegate` instead of the `AppDelegate`. With the iOS 27 SDK, apps built with Xcode 27 that don't adopt it fail to launch.

React Native 0.88 added SceneDelegate support. `RCTReactNativeFactory` has new entry points like `startReactNativeWithModuleName:inWindow:connectionOptions:`, you add `UIApplicationSceneManifest` to `Info.plist`, and you forward URL and user activity callbacks to `RCTLinkingManager` from the scene delegate so deep links keep working. Only a single scene is supported for now. Expo SDK 58 generates `SceneDelegate.swift` during prebuild, so Expo apps get this automatically.

### 358: What is the Android 16 KB page size requirement?

Newer Android devices can use 16 KB memory pages instead of 4 KB. Native libraries (`.so` files) must be built with 16 KB alignment to load on those devices. Google Play requires apps targeting Android 15+ to support 16 KB pages for new apps and updates (from November 2025).

React Native supports it since 0.77. For your app, the risk is third-party libraries with native C/C++ code built with old tooling. Check with Android Studio's APK analyzer or the alignment checks in the Play Console, and update or replace libraries that are not aligned.

### 359: What are precompiled iOS binaries and why do they matter?

Building React Native from source on iOS was slow, because hundreds of C++ and Objective-C files were compiled on every clean build. Since 0.84, React Native core and its dependencies are downloaded as precompiled `.xcframework` binaries during `pod install` by default (experimental in 0.81).

This makes clean iOS builds much faster, both locally and in CI. You build from source only if you need to patch React Native itself or change flags that require recompilation (for example `RCT_USE_PREBUILT_RNCORE=0`). This is similar to how Android has long used prebuilt AARs from Maven.

### 360: What is the state of Swift Package Manager support in React Native?

React Native 0.87 added experimental Swift Package Manager (SwiftPM) support for iOS as an alternative to CocoaPods. You opt in with `npx react-native spm`. In 0.88, libraries can declare SwiftPM settings in `package.json` under `swiftpmConfig`, and the plan is for 0.89 to make SwiftPM the default with CocoaPods as an opt-out.

The move is happening because CocoaPods is in maintenance mode and Apple's tooling is centered on SwiftPM. Library authors need to update their packages, and headers must be imported with their namespace (`#import <React/RCTAppDelegate.h>`). For app developers it means fewer Ruby/CocoaPods issues in the future.

### 361: How do you debug iOS build failures with CocoaPods?

Common steps:

```bash
cd ios
pod deintegrate
rm -rf Pods Podfile.lock build
pod install --repo-update
```

Also:

- Clear Xcode DerivedData (`~/Library/Developer/Xcode/DerivedData`).
- Make sure you open `.xcworkspace`, not `.xcodeproj`.
- Check Ruby and CocoaPods versions (use `bundle exec pod install` with the project's `Gemfile`).
- Read the first error in the Xcode build log, not the last one.
- Check that library versions match your React Native version.

With Expo CNG, running `npx expo prebuild --clean` regenerates the native project and fixes many of these problems.

### 362: How do you speed up Android builds?

- Enable the Gradle build cache and configuration cache (`org.gradle.caching=true`, `org.gradle.configuration-cache=true` where supported).
- Give Gradle enough memory (`org.gradle.jvmargs=-Xmx4g`).
- Build only the CPU architecture you need during development (`reactNativeArchitectures=arm64-v8a` in `gradle.properties`, or the CLI picks the connected device's architecture).
- Use the Gradle daemon and parallel builds.
- Cache `~/.gradle` and build outputs in CI.
- Avoid building C++ from source when prebuilt artifacts are available.

React Native 0.87 added Android Gradle Plugin 9 support. AGP and Gradle updates often bring speed improvements, so keep them current.

### 363: What are the trade-offs between Expo CNG and committing native folders?

**CNG (native folders generated):**

- Native config lives in `app.json` and plugins, which is easier to review.
- Upgrades are easier: regenerate instead of merging native diffs.
- Fewer accidental native changes.
- Custom native code must be written as config plugins or local modules, which is more work for one-off tweaks.

**Committing `ios/` and `android/` (bare):**

- You can edit any native file directly.
- Good for brownfield apps or apps with lots of custom native code.
- Upgrades mean applying diffs with the Upgrade Helper, and conflicts are common.

Both are valid. Many teams start with CNG and only move to bare if config plugins become a burden, and you can still use Expo SDK modules and EAS in bare projects.

### 364: How do you write a custom Expo config plugin?

A config plugin is a function that takes the Expo config and returns a modified config. Mods change native files during prebuild:

```js
// plugins/withCustomManifest.js
const { withAndroidManifest, withInfoPlist } = require("expo/config-plugins");

function withCustomSettings(config, { apiKey }) {
  config = withAndroidManifest(config, (cfg) => {
    const app = cfg.modResults.manifest.application[0];
    app["meta-data"] = app["meta-data"] ?? [];
    app["meta-data"].push({
      $: { "android:name": "com.example.API_KEY", "android:value": apiKey },
    });
    return cfg;
  });

  config = withInfoPlist(config, (cfg) => {
    cfg.modResults.ExampleApiKey = apiKey;
    return cfg;
  });

  return config;
}

module.exports = withCustomSettings;
```

```json
{
  "expo": {
    "plugins": [["./plugins/withCustomManifest", { "apiKey": "public-key" }]]
  }
}
```

Plugins should be idempotent (running twice gives the same result). Prefer the typed mods (`withAndroidManifest`, `withInfoPlist`, `withAppBuildGradle`) over string replacements, which break easily.

### 365: When would you choose the Expo Modules API over a Turbo Module?

**Expo Modules API**:

- Swift and Kotlin with a small DSL, less boilerplate, no Codegen setup.
- Built-in support for views, events, shared objects, typed arguments and records.
- Works in any React Native app (with the `expo` package installed).
- Good default for app teams writing their own native code.

**Turbo Modules (with Codegen)**:

- Core React Native API, no dependency on Expo.
- C++ Turbo Modules for shared cross-platform code.
- Fine control over JSI and threading.
- Good for libraries that want zero dependencies or C++ performance.

Performance is similar for normal use cases, since both use JSI. Choose based on your team and whether you need C++.

### 366: How do you create a native view with the Expo Modules API?

Define a view in the module definition and subclass `ExpoView`:

```swift
public class GradientModule: Module {
  public func definition() -> ModuleDefinition {
    Name("Gradient")

    View(GradientView.self) {
      Prop("colors") { (view: GradientView, colors: [UIColor]) in
        view.setColors(colors)
      }
      Events("onLayoutDone")
    }
  }
}

class GradientView: ExpoView {
  let gradient = CAGradientLayer()
  let onLayoutDone = EventDispatcher()

  required init(appContext: AppContext? = nil) {
    super.init(appContext: appContext)
    layer.addSublayer(gradient)
  }

  func setColors(_ colors: [UIColor]) {
    gradient.colors = colors.map { $0.cgColor }
  }

  override func layoutSubviews() {
    gradient.frame = bounds
    onLayoutDone(["width": bounds.width])
  }
}
```

```tsx
import { requireNativeView } from "expo";
const GradientView = requireNativeView("Gradient");

<GradientView
  colors={["#f00", "#00f"]}
  style={{ height: 100 }}
  onLayoutDone={(e) => console.log(e.nativeEvent)}
/>;
```

Android uses the same structure in Kotlin. Expo UI is built this way to render SwiftUI and Jetpack Compose from React.

### 367: Which thread does native module code run on, and how do you handle UI work?

By default, Turbo Module and Expo module methods are called on the JS thread (sync functions) or on a module queue/background thread (async functions), not on the main thread. Any UIKit or Android View work must run on the main thread:

```swift
AsyncFunction("showNativeAlert") { (message: String, promise: Promise) in
  // ...
}.runOnQueue(.main)
```

```kotlin
AsyncFunction("showToast") { message: String ->
  Toast.makeText(appContext.reactContext, message, Toast.LENGTH_SHORT).show()
}.runOnQueue(Queues.MAIN)
```

In plain Turbo Modules on iOS, you can set `methodQueue` or dispatch to `DispatchQueue.main`. Long work should go to a background queue, and the result should resolve a promise. Calling into JS from another thread must go through the `CallInvoker`, not by touching the runtime directly.

### 368: How do you pass large binary data between JS and native efficiently?

Avoid base64 strings, which add about 33% size and a lot of copying. Better options:

- **ArrayBuffer through JSI**: Turbo Modules and Expo Modules can accept and return `ArrayBuffer`s. React Native 0.88 added `ArrayBuffer` support for Java Turbo Modules. For synchronous calls the native side may borrow the JS memory without copying, and the bytes are only valid until the method returns (copy them with `ArrayBuffer.arrayBufferWithCopiedBytes` if you need to keep them).
- **Files**: write large data to a file and pass the path. Good for images, video and downloads.
- **Native-side processing**: keep the data in native code (for example camera frames) and only send results to JS.
- **Shared objects/host objects**: give JS a handle to a native object instead of the data itself.

### 369: How do you test native modules?

- **Native unit tests**: XCTest for Swift/Objective-C and JUnit for Kotlin/Java, testing native logic without React Native.
- **JS tests**: mock the module at the boundary in Jest, and test your JS wrapper (argument validation, error mapping).
- **Integration**: run an example app (Expo modules come with one) and E2E tests with Maestro or Detox that exercise the real module on simulators.
- **Type safety**: Codegen or Expo Modules typing catches mismatches between JS and native at build time.

Keep the native module thin and push logic either into well-tested native classes or into JS, so most code is easy to test.

### 370: What testing strategy would you use for a React Native app?

A balanced setup:

- **Static checks**: TypeScript in strict mode and ESLint. These catch many bugs for free.
- **Unit tests** (Jest): pure logic, hooks, reducers, formatters.
- **Component/integration tests** (React Native Testing Library + MSW): screens with real state and mocked network. This is where most tests should be.
- **E2E tests** (Maestro or Detox): a small set of critical flows (login, checkout, onboarding) on real builds, run in CI for every release.
- **Manual testing** on real devices for things automation misses: gestures, performance, accessibility with VoiceOver and TalkBack.
- **Monitoring** in production: crash and performance tracking.

Test behavior, not implementation details, so tests survive refactors.

### 371: Why are E2E tests flaky and how do you make them stable?

Common causes:

- **Timing**: animations, network calls and timers that the test doesn't wait for.
- **Real backend**: data changes between runs, or the server is slow.
- **Device state**: leftover data, permission dialogs, keyboard covering elements, system popups.
- **Weak selectors**: selecting by text that changes or by position.

Fixes:

- Use stable `testID`s or accessibility labels as selectors.
- Use the tool's built-in waiting (Detox sync, Maestro auto-wait) instead of fixed sleeps.
- Reset app state for each test (clear data, launch with a fresh install or a deep link to the start state).
- Use a dedicated test backend or mock server with seeded data.
- Pre-grant permissions in the launch config.
- Disable or shorten animations in test builds.

Track flaky tests and fix or remove them, because a flaky suite gets ignored.

### 372: How do you do visual regression testing in React Native?

Visual regression tests take screenshots of screens or components and compare them with approved baselines. Options:

- Screenshot steps in Maestro or Detox flows, compared with a tool like `pixelmatch` or a service.
- Storybook for React Native with a screenshot service (for example Chromatic for web stories, or tools that capture native stories).
- Native snapshot tools: `swift-snapshot-testing` on iOS, Paparazzi or Roborazzi on Android for native screens.

Run them on fixed simulator models, OS versions, fonts and locales, otherwise tiny rendering differences cause false failures. Use a small tolerance threshold.

### 373: How do you catch performance regressions before release?

- **Reassure** (by Callstack): measures render count and render time of components in Jest and compares them between branches.

```tsx
import { measureRenders } from "reassure";

test("ProductList renders efficiently", async () => {
  await measureRenders(<ProductList products={mockProducts} />);
});
```

- **Startup and flow benchmarks**: run release builds on real devices in CI (Firebase Test Lab, a device farm) and track metrics like TTI over time. Flashlight measures performance on Android with a performance score.
- **Bundle size checks**: fail CI when the bundle grows past a limit.
- **Production monitoring**: track app start, screen load times and frozen frames per release, and alert on changes.

### 374: How do you manage focus for screen reader users?

- After navigation, React Navigation and native stacks move focus to the new screen automatically. For custom transitions or modals, move focus yourself.
- After an action that changes content (an error appears, a dialog opens), move focus or announce it:

```tsx
const errorRef = useRef<Text>(null);

useEffect(() => {
  if (error && errorRef.current) {
    AccessibilityInfo.sendAccessibilityEvent(errorRef.current, "focus");
  }
}, [error]);

<Text ref={errorRef} accessibilityRole="alert">
  {error}
</Text>;
```

- In modals, keep focus inside the modal (`accessibilityViewIsModal` on iOS) and return focus to the trigger when it closes.
- Make sure the reading order matches the visual order. Group related elements with `accessible`.

`AccessibilityInfo.setAccessibilityFocus` was deprecated in 0.85 in favor of `sendAccessibilityEvent` with `'focus'`.

### 375: What are accessibility actions?

Accessibility actions let screen reader users perform actions that sighted users do with gestures, like swipe to delete or long press:

```tsx
<View
  accessible
  accessibilityLabel={`Message from ${sender}`}
  accessibilityActions={[
    { name: "activate", label: "Open message" },
    { name: "delete", label: "Delete message" },
    { name: "archive", label: "Archive" },
  ]}
  onAccessibilityAction={(event) => {
    switch (event.nativeEvent.actionName) {
      case "activate":
        return openMessage();
      case "delete":
        return deleteMessage();
      case "archive":
        return archiveMessage();
    }
  }}
>
  <SwipeableRow />
</View>
```

Standard names like `activate`, `increment`, `decrement`, `longpress` and `magicTap` map to platform gestures. Custom names appear in the actions menu (VoiceOver rotor on iOS, actions menu in TalkBack).

### 376: How do you announce content that changes on its own?

For content that updates without the user moving focus (a timer, a status message, search result counts):

- On Android, use `accessibilityLiveRegion` on the view: `'polite'` waits for the current speech, `'assertive'` interrupts.
- On iOS, there is no live region prop, so call `AccessibilityInfo.announceForAccessibility(message)` (or `announceForAccessibilityWithOptions` with `queue: true`).

```tsx
<Text accessibilityLiveRegion="polite">{`${results.length} results`}</Text>;

useEffect(() => {
  if (Platform.OS === "ios")
    AccessibilityInfo.announceForAccessibility(`${results.length} results`);
}, [results.length]);
```

Don't announce too often, for example on every keystroke. Debounce it.

### 377: How do you respect the reduce motion setting?

Users can turn on "Reduce Motion" (iOS) or "Remove animations" (Android). Check it and simplify animations:

```tsx
import { useReducedMotion } from "react-native-reanimated";

function Card() {
  const reduceMotion = useReducedMotion();
  return (
    <Animated.View entering={reduceMotion ? undefined : FadeInUp.springify()}>
      {/* ... */}
    </Animated.View>
  );
}
```

Core React Native offers `AccessibilityInfo.isReduceMotionEnabled()` and the `reduceMotionChanged` event. Reanimated animations also accept a `reduceMotion` config (`ReduceMotion.System` follows the setting). Replace large movements and parallax with simple fades, or skip the animation.

### 378: What problems do you meet when supporting right-to-left layouts?

- Flexbox `row` flips automatically, and `start`/`end` styles flip, but hardcoded `left`/`right`, `marginLeft` and absolute positions don't.
- Icons with direction (back arrows, chevrons, progress) must be mirrored: `transform: [{ scaleX: I18nManager.isRTL ? -1 : 1 }]`.
- Animations with `translateX` need their sign flipped.
- Horizontal lists and carousels may need `inverted` behavior.
- Mixed text (an English product name in an Arabic sentence) needs proper bidi handling, so test real content.
- Changing direction with `I18nManager.forceRTL` needs an app reload (`Updates.reloadAsync()` or `DevSettings.reload()`), because layout direction is set at startup.

Test the whole app in an RTL language, not just a few screens.

### 379: How do you improve navigation performance in a big app?

- Use the native stack, which uses native screen containers.
- Keep previous screens light: screens stay mounted in a stack, so heavy subscriptions or timers on them keep running. Pause work when unfocused (`useIsFocused`, `useFocusEffect`).
- Freeze inactive screens: `react-native-screens` can freeze screens that are not visible (with `react-freeze`), so they don't re-render when global state changes. In React Navigation it's the `freezeOnBlur` option.
- Lazy tabs: tabs render only when first opened (the default `lazy: true`).
- Avoid deep stacks: use `replace` or `popTo` when it makes sense.
- Start loading data before navigating, or show the screen first with a skeleton.

React 19's `<Activity>` component may also be used for hiding inactive content while keeping state.

### 380: How do you persist and restore navigation state?

React Navigation can save the navigation state and restore it on the next launch, so users come back where they left off:

```tsx
const PERSISTENCE_KEY = "NAVIGATION_STATE_V1";

function App() {
  const [isReady, setIsReady] = useState(__DEV__ ? false : true);
  const [initialState, setInitialState] = useState();

  useEffect(() => {
    if (isReady) return;
    AsyncStorage.getItem(PERSISTENCE_KEY)
      .then((saved) => saved && setInitialState(JSON.parse(saved)))
      .finally(() => setIsReady(true));
  }, [isReady]);

  if (!isReady) return null;

  return (
    <Navigation
      initialState={initialState}
      onStateChange={(state) =>
        AsyncStorage.setItem(PERSISTENCE_KEY, JSON.stringify(state))
      }
    />
  );
}
```

It is very useful in development (keep your place after reloads). In production be careful: params must be serializable, the route structure may change between versions (add a version to the key), and a deep link should take priority over the restored state.

### 381: A user opens a deep link to a protected screen while the app is closed and they are logged out. How do you handle it?

1. The app starts and reads the initial URL.
2. While auth state loads from secure storage, keep the splash screen visible.
3. If the user is logged out, save the target URL and show the login screen.
4. After login, navigate to the saved URL (and clear it).
5. If the user is logged in, navigate directly.

In Expo Router with `Stack.Protected`, the protected route isn't available while logged out, so the user lands on the login screen. You store the requested path (for example from `usePathname` or the initial URL) and call `router.replace(savedPath)` after sign-in. In React Navigation the auth-based screen groups and the `linking` config handle most of this, and you redirect after login. Validate the saved URL, so a link can't send users somewhere unexpected.

### 382: How do you share business logic between a React Native app and a web app?

- Use a monorepo with shared packages: `packages/api` (typed API client), `packages/domain` (validation, formatting, business rules), `packages/state` (stores, query hooks).
- Keep shared packages platform-free: no `react-native` or `react-dom` imports, no `window` or native modules.
- Inject platform-specific things (storage, analytics, navigation) through interfaces or providers.
- Share types and schemas (Zod) with the backend too.
- For UI, either keep separate component libraries with shared tokens, or share components with React Native Web, Tamagui or Expo Router on web.

The more UI you share, the more you have to deal with platform differences, so many teams share logic fully and UI only partly.

### 383: How do you decide between server state and client state tools?

Separate the data by who owns it:

- **Server state** (products, orders, user profiles): owned by the backend, can be stale, needs caching, refetching, pagination and invalidation. Use TanStack Query, RTK Query, Apollo or Relay.
- **Client state** (UI state, form drafts, selected filters, theme, onboarding progress): owned by the app. Use `useState`, context, Zustand, Jotai or Redux.
- **Persistent device data** (settings, offline data): MMKV, SQLite.

Putting server data into a global client store by hand leads to a lot of code for loading flags, caching and stale data. Using a server state library for UI state is awkward. Most apps end up with a server state library plus a small client store.

### 384: What is tearing and how do external stores avoid it with concurrent rendering?

Tearing is when different parts of the UI show different values from the same store during one render. It can happen with concurrent rendering: React pauses a render, the store changes, and components rendered after the pause read the new value while earlier ones show the old value.

React's `useSyncExternalStore` prevents this. It reads a snapshot of the store and, if the store changes during a concurrent render, React re-renders synchronously so everything is consistent:

```tsx
const value = useSyncExternalStore(store.subscribe, store.getSnapshot);
```

Zustand, Redux (`react-redux`) and most modern libraries use it internally. Since React Native now supports concurrent rendering, custom stores and subscriptions should use it too, instead of `useEffect` + `useState` subscriptions.

### 385: What should you watch out for when enabling the React Compiler?

- Code that breaks the Rules of React (mutating props or state, reading refs during render, conditional hooks) can behave differently after compilation. The compiler skips components it can't prove safe, and the ESLint plugin reports them.
- Effects with missing dependencies can start behaving differently, because values that used to be recreated every render are now memoized.
- Libraries that rely on mutation (some older animation or form libraries) may not work well with memoized values. For Reanimated, use `.get()` and `.set()` on shared values.
- Measure: check render counts and performance before and after.
- Roll out gradually, for example per folder, with the `sources` option or `'use no memo'` to opt out a component.

Once enabled, you can usually remove most manual `useMemo` and `useCallback`.

### 386: What does StrictMode do in React Native?

`<StrictMode>` enables extra checks in development:

- Components render twice to catch impure render logic.
- Effects run setup, cleanup and setup again on mount, to catch effects without proper cleanup.
- Warnings for deprecated APIs.

It has no effect in release builds. You can enable it in Expo Router through config or by wrapping your root component. If an effect with a subscription breaks under StrictMode, it means the cleanup is missing, which would also cause bugs when screens remount or with Fast Refresh. Don't remove StrictMode to hide the problem, fix the cleanup.

### 387: The app is smooth on iPhones but slow on mid-range Android phones. What do you check?

Android devices vary a lot, and mid-range CPUs are much slower than recent iPhones. Check:

- Test a **release build**. Debug builds are especially slow on Android.
- **JS work**: profile the JS thread. Code that takes 5 ms on iPhone may take 30 ms on a cheap Android.
- **Images**: oversized images and many images decoded at once hurt Android more.
- **Overdraw and shadows**: many overlapping backgrounds, `elevation` and `boxShadow` cost GPU time. Check "Debug GPU overdraw" in developer options.
- **Lists**: tune windowing, move to FlashList.
- **Too many views**: very deep or wide trees, `collapsable={false}` everywhere.
- **Animations** running on the JS thread instead of native.
- **Startup work** from native SDKs that do more on Android.

Keep a mid-range Android device in the team and test on it regularly.

### 388: The app crashes on startup only in release builds. How do you investigate?

1. Get the crash log: `adb logcat` on Android, device logs or crash reports in Xcode on iOS, or your crash reporter.
2. If it's a **JS error**, look at the symbolicated stack. Common causes: code that depends on `__DEV__`, a missing environment variable in the release config, or a module that fails at import time.
3. If it's **native**:
   - Android R8/ProGuard removed or renamed classes used by reflection. Add `-keep` rules for that library.
   - A missing permission description or entitlement on iOS.
   - A native library that is not included in the release build variant.
4. Check the **bundle**: make sure the JS bundle is actually included (a broken bundling step gives "unable to load script").
5. If you use **OTA updates**, check whether a bad update was applied. Launch without it.

Reproduce locally with `npx expo run:android --variant release` to iterate faster than CI.

### 389: Something works in debug but behaves differently in release. What are the usual causes?

- **`__DEV__` code paths** or dev-only libraries.
- **Minification**: code that relies on function or class names (`constructor.name`, `Function.name`) breaks when names are minified.
- **R8** removing classes on Android that are used through reflection.
- **Network**: debug builds may allow cleartext HTTP or user-installed certificates. Release builds don't.
- **Timing**: release builds are faster, which exposes race conditions hidden by slow debug builds.
- **Console logs**: removed in release by a Babel plugin, along with side effects inside them.
- **Environment config**: different `.env` or `app.config` values for release.
- **Hermes bytecode**: rare differences, for example with `Function.prototype.toString`, which doesn't return the source in Hermes release builds.

Test release builds early, not only at the end.

### 390: How would you upgrade an app from React Native 0.72 to the latest version?

This is a big jump that crosses the New Architecture migration. A plan:

1. Read the release notes for every version in between and list breaking changes.
2. Audit dependencies: check every library with native code for New Architecture support on reactnative.directory. Replace dead libraries first, while still on the old version if possible.
3. Upgrade in steps (for example 0.72 → 0.74 → 0.76 → 0.79 → 0.82 → 0.84 → latest), getting the app to build and pass tests at each step. 0.76 (New Architecture default) and 0.82 (legacy removed) are the key steps.
4. Use the Upgrade Helper for native files, or move to Expo CNG to stop maintaining native diffs.
5. Fix deep imports for the Strict TypeScript API (0.87).
6. Test heavily on both platforms: navigation, gestures, animations, native modules, push notifications, deep links.
7. Release behind a staged rollout and watch crash rates.

Plan for regular upgrades afterwards so you don't fall this far behind again.

### 391: How would you move a bare React Native app to Expo CNG?

1. Install the `expo` package (`npx install-expo-modules@latest`), so you can use Expo SDK modules and tooling.
2. Move native settings into `app.json`/`app.config.ts`: bundle ID, version, icons, splash, permissions, URL schemes, entitlements.
3. For each library, check if it has a config plugin. For custom native changes, write your own config plugins or move code into local Expo modules.
4. Run `npx expo prebuild --clean` into a separate branch and compare the generated `ios/` and `android/` with the old ones. Repeat until the differences are only intended ones.
5. Move signing to EAS credentials or keep your own, and set up `eas.json` profiles.
6. Delete the native folders from git (add them to `.gitignore`).

Do it gradually. You can use most Expo tools while still committing native folders, and switch to CNG at the end.

### 392: An important library doesn't support the New Architecture. What are your options?

1. Check if it already works through the interop layer. Many simple native modules and views do.
2. Look for a newer version, a maintained fork, or an alternative in the Expo SDK or the React Native Directory.
3. Check open issues and pull requests. Maybe someone has already started a migration you can use or help finish.
4. Migrate it yourself: write a Codegen spec and update the native code, then contribute it upstream or use `patch-package`.
5. Rewrite only the parts you use as a local Expo module, which is often less code than the whole library.
6. If it's not critical, remove the feature or replace it with a web view or a server-side solution.

Since the legacy architecture can't be enabled anymore, staying on an old React Native version for one library is only a short-term option.

### 393: How would you build a chat screen?

Key parts:

- **List**: an inverted `FlatList` or FlashList with `maintainVisibleContentPosition`, newest messages at the bottom, loading older messages on scroll.
- **Keyboard**: `react-native-keyboard-controller` (`KeyboardAvoidingView` or `KeyboardStickyView`) so the input and list move with the keyboard smoothly. `InputAccessoryView` was deprecated in 0.88 in favor of `KeyboardStickyView`.
- **Real time**: WebSocket for new messages, with reconnect and fetching missed messages.
- **Optimistic sending**: show the message right away with a "sending" state, replace it with the server version, and show retry on failure.
- **Local cache**: store recent messages in SQLite so the chat opens instantly and works offline.
- **Media**: thumbnails, upload progress, and lazy loading.
- **Performance**: memoized message bubbles, stable keys (client-generated IDs), and grouping consecutive messages.
- **Accessibility**: announce new messages politely, and make bubbles readable as a single element with sender and time.

### 394: How would you build a feed with many images that scrolls smoothly?

- Use FlashList with `getItemType` for different post types.
- Get image dimensions from the API and use `aspectRatio`, so the layout doesn't jump.
- Use `expo-image` with memory and disk caching, `recyclingKey` for recycled rows, blurhash placeholders, and request CDN images at the displayed size.
- Prefetch images for the next few items or the next page.
- Keep item components light and memoized. Load comments, reactions and other details lazily.
- Pause videos and GIFs that are off screen (use `onViewableItemsChanged`).
- Use cursor pagination and keep a reasonable max number of items in memory.
- Test on a low-end Android device with a slow network.

### 395: How would you design an offline-first app, for example for field workers?

1. **Local database as the source of truth for the UI**: SQLite (`expo-sqlite`, op-sqlite with Drizzle) or WatermelonDB. Screens read from it reactively.
2. **Sync engine**: pull changes since the last sync timestamp or cursor, push local changes from an outbox table. Run it on app start, on reconnect (NetInfo), on foreground and periodically while active.
3. **Outbox**: every local change is saved as an operation with a client ID, so it can be retried and is idempotent on the server.
4. **Conflicts**: decide per entity (last write wins, server rules, or manual).
5. **Files**: queue photo uploads separately, with retries and progress.
6. **UI**: show sync status, "pending" markers, and never block actions on the network.
7. **Migrations**: plan database schema migrations for app updates.

Also consider ready-made sync tools like PowerSync, ElectricSQL or WatermelonDB's sync protocol instead of building everything yourself.

### 396: How would you build a vertical video feed like TikTok?

- A vertical paging list (FlashList or FlatList with `pagingEnabled`, or `react-native-pager-view`), each item full screen.
- `expo-video` (or `react-native-video`) players. Only the visible item plays. Use `onViewableItemsChanged` to know which one is active.
- Keep a small pool of players (current, previous, next) and preload the next video so it starts instantly. Release players far from the current item to save memory.
- HLS streams with adaptive bitrate, and a poster image shown until the first frame.
- Pause on app background, on screen blur and when another screen opens.
- Gestures with Gesture Handler for double tap to like (with Reanimated hearts) and long press.
- Track watch time for recommendations, batched and sent in the background.

Test on low-end Android devices, where decoding several videos at once is the main limit.

### 397: How would you show thousands of points on a map?

Rendering thousands of `Marker` components is slow because each is a native view. Options:

- **Clustering**: group nearby points into clusters with counts, and split them as the user zooms in. Use `supercluster` in JS or the map SDK's built-in clustering.
- **Native layers**: with `@rnmapbox/maps`, use a `ShapeSource` with GeoJSON and `SymbolLayer`/`CircleLayer`, which renders points on the GPU instead of as views.
- **Viewport loading**: only load points inside the visible region from the server, and refetch on region change (debounced).
- **Simple markers**: use images instead of custom React views for markers, and set `tracksViewChanges={false}` on custom markers in `react-native-maps` after they render.

### 398: What would you require for a banking app built with React Native?

- **Authentication**: OAuth/OIDC with PKCE, short-lived access tokens, refresh tokens in Keychain/Keystore, biometric unlock, session timeout and logout on inactivity.
- **Transport**: HTTPS only, certificate pinning with backup pins.
- **Device integrity**: Play Integrity and App Attest checks on the server, root/jailbreak detection as an extra signal.
- **Data**: no sensitive data in logs, AsyncStorage, analytics or crash reports. Encrypt local databases.
- **UI protection**: hide content in the app switcher (blur on `inactive`), block screenshots on sensitive screens (`FLAG_SECURE` on Android, for example with `expo-screen-capture`).
- **Code**: no secrets in the bundle, R8, code signing for OTA updates (or no OTA for sensitive flows).
- **Process**: penetration tests, dependency scanning, and following the OWASP Mobile Application Security guidelines (MASVS).

### 399: How would you build a white-label app (one codebase, many branded apps)?

- One codebase with brand configs: name, bundle ID, icons, splash screen, colors, fonts, feature flags and API endpoints per brand.
- With Expo, use `app.config.ts` that reads a `BRAND` environment variable and loads `brands/<brand>/config.ts` and its assets.
- EAS build profiles per brand (or a script that loops over brands) and separate store accounts or listings.
- Theme tokens from the brand config, so components never hardcode colors.
- Feature flags for features only some brands have.
- Separate OTA channels per brand, so you can update them independently.
- Separate signing credentials and push notification credentials per brand.

In bare projects you use Android product flavors and iOS targets/schemes, which is more work to maintain.

### 400: How would you add feature flags and remote config?

Use a service like LaunchDarkly, Statsig, PostHog, Firebase Remote Config or GrowthBook, or your own endpoint:

```tsx
function CheckoutScreen() {
  const newCheckout = useFeatureFlag("new-checkout", false);
  return newCheckout ? <NewCheckout /> : <OldCheckout />;
}
```

Important details on mobile:

- **Cache flags locally** (MMKV) and use cached values on startup, so the UI doesn't flicker or wait for the network.
- **Defaults in code** for when the service is unreachable.
- **Target by app version**, because old binaries may not have the code for a flag.
- Decide when changes apply: on next launch (stable) or live (risky for flows in progress).
- **Clean up** old flags, otherwise the code fills up with dead branches.

Flags plus OTA updates let you ship code dark and turn it on gradually.

### 401: How would you run A/B tests in a React Native app?

- Use an experimentation tool (Statsig, PostHog, Amplitude Experiment, Firebase A/B Testing, GrowthBook) that assigns users to variants and tracks results.
- Assign variants by user ID, not device, so a user sees the same variant on all devices. Cache the assignment locally so it is stable between launches.
- Decide assignments early (before the screen that uses them renders) to avoid flicker. Use cached values on startup.
- Log an "exposure" event only when the user actually sees the variant.
- Only test code that exists in the binary. With OTA updates you can ship new variants without a store release, but keep them within store rules.
- Run the test long enough and check guardrail metrics like crash rate and retention, not only the target metric.

### 402: How do you schedule local notifications reliably?

Use `expo-notifications` (or Notifee) to schedule notifications that the OS shows even if the app is closed:

```tsx
await Notifications.scheduleNotificationAsync({
  content: {
    title: "Time to stretch",
    body: "You have been sitting for an hour.",
  },
  trigger: {
    type: Notifications.SchedulableTriggerInputTypes.DAILY,
    hour: 10,
    minute: 0,
  },
});
```

Things to watch:

- iOS allows only 64 pending local notifications per app. Schedule the next ones on each launch.
- Android 12+ needs the `SCHEDULE_EXACT_ALARM` (or `USE_EXACT_ALARM`) permission for exact timing. Otherwise the OS may delay notifications to save battery.
- Device reboot: Android clears scheduled alarms, libraries reschedule them on boot.
- Time zone changes: decide whether "10:00" means local time or a fixed moment.
- Cancel notifications when they are no longer relevant (`cancelScheduledNotificationAsync`).

### 403: How do you add payments like Apple Pay and Google Pay?

For physical goods and services, use a payment provider SDK. The Stripe React Native SDK (`@stripe/stripe-react-native`) is common:

1. Your server creates a PaymentIntent with the secret key and returns the client secret.
2. The app shows the Payment Sheet, which supports cards, Apple Pay and Google Pay.
3. Stripe handles 3D Secure and returns the result.
4. Your server confirms the final state through webhooks, not by trusting the app.

```tsx
const { initPaymentSheet, presentPaymentSheet } = useStripe();

await initPaymentSheet({
  paymentIntentClientSecret: clientSecret,
  merchantDisplayName: "My Shop",
  applePay: { merchantCountryCode: "US" },
});
const { error } = await presentPaymentSheet();
```

Apple Pay needs a merchant ID and entitlement. Remember that digital goods inside the app usually must use in-app purchases instead.

### 404: How do you add a home screen widget to a React Native app?

Widgets are separate native extensions. They can't run React Native code, because the OS renders them with SwiftUI (WidgetKit) on iOS and Jetpack Glance or RemoteViews on Android, with strict memory limits.

The usual approach:

1. Build the widget UI natively (or with `expo-widgets`, which lets you describe widgets from your project and got an Android implementation in SDK 58).
2. Share data between the app and the widget through an App Group (iOS) or `SharedPreferences` (Android).
3. Write data from React Native through a small native module, and ask the system to reload the widget timeline.

With Expo CNG, extension targets are added through config plugins (for example `@bacons/apple-targets`), so they survive prebuild. Live Activities on iOS work the same way.

### 405: How do out-of-tree platforms like Windows, macOS and TV work?

React Native's core is split into a shared C++ part (Fabric, Yoga, JSI) and platform implementations. Out-of-tree platforms provide their own native implementation of the core components and modules:

- `react-native-windows` and `react-native-macos` (Microsoft) render to native Windows (WinUI/XAML or Composition) and AppKit views.
- `react-native-tvos` adds focus handling and remote control support for Apple TV and Android TV.
- Meta Quest support (2026) runs React Native apps on Horizon OS, which is Android-based.

Your JS code mostly works as is. You use `Platform.OS` and platform file extensions for differences, and native libraries must support each platform, which is the main limit. Each platform usually follows core React Native releases with some delay.

### 406: What JavaScript differences between Hermes and browsers can cause bugs?

- **Date parsing**: `new Date('2026-10-24 10:00')` (non-ISO format) can be invalid or parsed differently. Always use ISO 8601 strings or a library.
- **`Function.prototype.toString`**: doesn't return the source code in Hermes release builds (it shows `[bytecode]`). Code that inspects function source breaks.
- **`Intl`**: supported, but some locales or options may behave slightly differently from browsers.
- **Missing web APIs**: no DOM, no `localStorage`, limited `crypto` (no `crypto.subtle` by default).
- **Error stack format**: different from V8, which matters for log parsing.
- **Some newer proposals** may land later than in V8.

Test on devices with release builds, and avoid relying on engine-specific behavior.

### 407: How do you add missing web or Node APIs like crypto.getRandomValues or Buffer?

Install a polyfill and import it once, at the very top of your entry file:

```ts
// index.ts
import "react-native-get-random-values"; // crypto.getRandomValues for uuid and others
import { Buffer } from "buffer";
global.Buffer = Buffer;
```

Other common ones: `expo-crypto` (random bytes, digests and `randomUUID`), `react-native-quick-crypto` (a fast Node `crypto` API with JSI), `text-encoding` polyfills when `TextDecoder` options are missing, and `react-native-url-polyfill` for very old React Native versions (no longer needed since URL was improved in 0.84).

Only add polyfills you need. Each one adds bundle size and startup time. Libraries that need many Node polyfills are often not a good fit for mobile.

### 408: How do you cancel requests and handle timeouts properly?

Use `AbortController`. Cancel requests when a screen unmounts or a newer request replaces them, and add a timeout:

```ts
async function fetchWithTimeout(url: string, ms = 10000, signal?: AbortSignal) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), ms);
  signal?.addEventListener("abort", () => controller.abort());

  try {
    const res = await fetch(url, { signal: controller.signal });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } finally {
    clearTimeout(timer);
  }
}
```

`fetch` has no default timeout in React Native beyond the OS network timeout, which can be very long on bad mobile networks. Data libraries like TanStack Query pass a `signal` to your query function, so cancellation works automatically when queries change.

### 409: How do you design a React Native app to be battery friendly?

- Avoid polling. Use push notifications or WebSockets, and close sockets in the background.
- Use the lowest location accuracy and update frequency that works, and stop tracking when not needed.
- Batch network requests and analytics events instead of sending them one by one.
- Stop animations, timers and video playback when the app or screen is not visible.
- Avoid unnecessary re-renders and JS work, which keep the CPU busy.
- Use the OS schedulers (WorkManager, BGTaskScheduler) for background work, so the OS can group tasks.
- Dark UI saves power on OLED screens.

Android shows apps with high battery use to the user and can restrict them, so this affects retention.

### 410: How does React Native DevTools connect to the app?

React Native DevTools uses the Chrome DevTools Protocol (CDP). Hermes has a built-in CDP debugging agent. When you open DevTools, the Metro dev server acts as a proxy (the "inspector proxy"): the frontend (a customized Chrome DevTools build) connects to Metro over WebSocket, and Metro forwards messages to the app's runtime.

The newer debugger stack (internally called "Fusebox") moved more of the CDP handling into React Native's C++ core, so features like the Network panel, Performance panel and `Page.captureScreenshot` work directly through CDP domains. This is also why the old `XHRInterceptor` and `WebSocketInterceptor` were deprecated in 0.84: tools should use the CDP `Network` domain instead.

### 411: How do you do logging in a production React Native app?

- Use a small logging wrapper with levels (debug, info, warn, error) instead of `console.log` everywhere.
- In development, log to the console. In production, send warnings and errors to a service (Sentry breadcrumbs, Datadog, Bugsnag, LogRocket) and drop debug logs.
- Attach context: app version, OTA update ID, platform, OS version, user ID (hashed if needed), current screen.
- Never log tokens, passwords, full card numbers or personal data.
- Batch and send logs when online, with a size limit, so logging doesn't drain battery or data.
- Use breadcrumbs (navigation, network calls, user actions) to understand what happened before a crash.

### 412: How do you do staged rollouts of store releases?

- **Google Play**: staged rollout lets you release to a percentage of users (for example 1%, 5%, 20%, 50%, 100%). You can halt a rollout if crash rates go up.
- **App Store**: phased release spreads an automatic update over 7 days (1%, 2%, 5%, 10%, 20%, 50%, 100%). Users can still update manually, and you can pause it.

Before that, use internal testing tracks (Play internal and closed testing, TestFlight). During rollout watch crash-free sessions, ANRs, key business metrics and reviews. Combine with feature flags, so you can turn off a broken feature without waiting for a new build.

### 413: What are common reasons for App Store rejections in React Native apps?

- Missing or vague permission usage descriptions (`NSCameraUsageDescription` and so on).
- Requesting permissions the app doesn't clearly need, or asking at launch without context.
- Digital purchases that don't use in-app purchases.
- No "Sign in with Apple" when other third-party logins are offered (in many cases).
- No account deletion option inside the app, if users can create accounts.
- Crashes or broken features during review (often a backend or test account problem).
- Missing privacy manifest entries or wrong privacy labels.
- Using OTA updates to change the app's purpose or add major features after review.
- Placeholder content or web-view-only apps with little native value.

Provide a working demo account and clear review notes.

### 414: What is an iOS privacy manifest?

A privacy manifest (`PrivacyInfo.xcprivacy`) is a file where an app or SDK declares the data it collects and the "required reason APIs" it uses (like `UserDefaults`, file timestamps, system boot time, disk space), with an allowed reason for each. Apple requires them since 2024.

React Native and many libraries use these APIs. React Native includes a privacy manifest in the template, and Expo lets you set entries in `app.json` under `ios.privacyManifests`. Third-party SDKs on Apple's list must ship their own signed manifests. If something is missing, App Store Connect sends a warning or rejects the build.

### 415: Why do you need to keep up with Android target SDK requirements?

Google Play requires apps to target a recent Android API level, usually within one year of the latest Android release. If you don't update `targetSdkVersion`, you can't publish updates, and new users on recent devices may not see the app.

Each new target SDK can change behavior: edge-to-edge enforcement (Android 15), stricter background and exact alarm rules, notification permission (Android 13), predictive back gestures, and large-screen orientation rules (Android 16). React Native releases update the default target SDK, which is one more reason to upgrade React Native regularly. Test the app on the newest Android version when you bump the target.

### 416: How do you handle differences between OS versions?

Check the version with `Platform.Version` and degrade gracefully:

```ts
import { Platform } from "react-native";

const supportsNotificationPermission =
  Platform.OS === "android" && Platform.Version >= 33;

const isIOS17Plus =
  Platform.OS === "ios" && parseInt(String(Platform.Version), 10) >= 17;
```

On Android, `Platform.Version` is the API level (a number). On iOS it's a version string. Prefer checking whether a feature is available (for example `await Notifications.getPermissionsAsync()`, or a library's `isAvailableAsync()`) over checking versions, because devices with the same version can differ. Also decide on a minimum OS version and set it in the native projects (Expo sets the defaults per SDK).

### 417: Can an app have more than one React Native root view?

Yes. A native app can show several React Native surfaces, for example a React Native screen inside a native tab and another one in a modal. With the New Architecture, they share one `ReactHost` (one JS runtime) and each surface renders its own root component registered with `AppRegistry`.

```ts
AppRegistry.registerComponent("ProfileScreen", () => ProfileScreen);
AppRegistry.registerComponent("SettingsScreen", () => SettingsScreen);
```

Because the runtime is shared, global state and caches are shared between surfaces, which is useful in brownfield apps. Each surface gets its own initial props. Running several separate JS runtimes is possible but uses much more memory, so it's rare.

### 418: How do you use the Performance API in React Native?

React Native supports the User Timing API, and the marks show up in the React Native DevTools Performance panel:

```ts
performance.mark("checkout-start");

await loadCheckoutData();

performance.mark("checkout-ready");
performance.measure("checkout-load", "checkout-start", "checkout-ready");
```

You can read entries with `performance.getEntriesByName()` or `PerformanceObserver` and send them to your monitoring tool. `performance.now()` gives high-resolution time. This lets you measure your own flows (screen ready, list loaded) instead of only generic metrics, and compare releases.

### 419: What is setNativeProps and why should you avoid it?

`setNativeProps` changes props on a native view directly, without a React render:

```ts
inputRef.current?.setNativeProps({ text: "" });
```

It was used for performance tricks in the old architecture, for example updating a view on every scroll event. Problems: React doesn't know about the change, so the next render can overwrite it, and the state of the UI is no longer described by your components. In Fabric it is supported only for compatibility and works differently in some cases.

Use state, Animated or Reanimated (which update native props in a controlled way) instead. For text inputs, use controlled values or `clear()`.

### 420: How does Fast Refresh work internally?

1. When you save a file, Metro rebuilds only that module and sends the update to the app over the WebSocket connection.
2. The app's module system replaces the old module with the new one.
3. React Refresh (a runtime from the React team) checks if the module exports only React components. If yes, it swaps the component implementation and re-renders all its instances, keeping their state. A Babel plugin registers components and their hook signatures so React can tell if the hooks changed.
4. If the hook order or count changed, that component's state is reset.
5. If the module exports non-components, the update propagates to modules that import it, and those are re-run. If it reaches the root, the app reloads.

Errors during an update are shown in LogBox, and the next successful save recovers without a full reload.

### 421: How does Metro decide which file to load for an import?

For a relative import like `./Button`, Metro tries extensions in order of the platform, for example on iOS: `Button.ios.tsx`, `Button.native.tsx`, `Button.tsx`, then the same for `.ts`, `.js` and others (`resolver.sourceExts`).

For a package, Metro reads its `package.json`:

- With package `exports` support (default in recent Metro), it matches conditions in order: `react-native`, then platform conditions like `ios`/`android`, then `require` or `import`, then `default`.
- Without `exports`, it uses the `react-native` field, then `browser`, then `main` (`resolver.resolverMainFields`).

This is how libraries ship different code for React Native and web, and why a library with wrong `exports` can break in React Native but work on the web. Since 0.87, the `react-native` package itself uses `exports` and a `react-native-legacy-deep-imports` condition for the temporary deep import opt-out.

### 422: How does text rendering work in React Native?

A `<Text>` tree is not a tree of native views. Fabric turns a `Text` and its nested `Text` children into one attributed string (`NSAttributedString` on iOS, `Spannable` on Android) with style ranges. One native text view draws the whole paragraph.

Layout of text is measured in C++ during the commit phase using platform text measurement, so Yoga knows the height before mounting. This is why:

- Nested `Text` can't have its own padding, margins or borders (it is a span, not a box).
- `View`s inside `Text` are supported only in limited ways (inline views).
- Styles like `fontVariationSettings` (variable fonts, added in 0.88) apply per span.
- Text measurement is a common cost in big lists, so very long texts in lists should use `numberOfLines`.

### 423: What makes Yoga layout expensive, and how do you keep it fast?

Yoga runs Flexbox on the whole changed subtree in each commit. Costs grow with:

- **Number of nodes**: very deep or wide trees, especially many wrapper views.
- **Text measurement**: each text node calls into platform text layout.
- **Nested flex with `flexWrap`, `alignItems: 'baseline'` or percentage sizes**, which may need several measurement passes.
- **Frequent changes** to layout props of parents, which invalidate big subtrees.

Keep it fast by flattening wrapper views, giving fixed sizes where you know them (list rows, images), avoiding layout changes during scroll (use transforms in animations instead of `width`/`top` where possible), and keeping lists virtualized. Yoga caches results for unchanged nodes, so stable trees are cheap.

### 424: How does the responder system work?

The responder system is React Native's built-in way to decide which view handles a touch. When a touch starts, React Native asks views (from the deepest up, and with "capture" handlers from the top down) if they want to become the responder:

- `onStartShouldSetResponder` / `onMoveShouldSetResponder`: "do you want this touch?"
- `onResponderGrant`: you became the responder
- `onResponderMove`, `onResponderRelease`
- `onResponderTerminationRequest`: another view wants the touch, do you let it go?
- `onResponderTerminate`: you lost it (for example, a `ScrollView` started scrolling)

`Pressable` (through the internal Pressability API) and `PanResponder` are built on it. It runs in JavaScript, so it depends on the JS thread being free.

### 425: How is Gesture Handler different from the responder system?

The responder system decides touch ownership in JavaScript, after events travel from native to JS. `react-native-gesture-handler` recognizes gestures on the native side using the platform's gesture recognizer system, and can run callbacks as worklets on the UI thread.

This means:

- Gestures keep working smoothly when the JS thread is busy.
- Gestures can work together with native components (scroll views, native stack swipe back) through explicit relationships (simultaneous, require-to-fail).
- You get more gesture types (pinch, rotation, fling, hover) with consistent behavior.

`PanResponder` is still fine for simple cases, but for interactive UI (swipeable rows, bottom sheets, drag and drop) Gesture Handler is the standard choice.

### 426: How does garbage collection work in Hermes, and what can you do about GC pauses?

Hermes uses a generational GC called Hades. New objects are allocated in a young generation that is collected often and quickly. Objects that survive move to the old generation, which is collected mostly concurrently on a background thread, so pauses on the JS thread are short.

GC still costs time when the app allocates a lot. To reduce pressure:

- Avoid creating large temporary arrays and objects in hot paths (scroll handlers, render of big lists).
- Don't keep huge data in JS memory. Keep it in SQLite or native code and query what you need.
- Avoid big JSON strings: parsing a 20 MB response creates many objects at once.
- Release references to data you no longer need (caches with limits).

Use heap snapshots and the Performance panel to see GC activity.

### 427: What are the security risks of WebView and how do you reduce them?

A WebView that can talk to native code is a bridge for attackers if it loads untrusted content. Risks: XSS in the page sending messages to your app, phishing pages inside your app, leaking cookies or tokens, and file access.

Reduce them:

- Load only your own HTTPS URLs. Use `originWhitelist` and check navigation with `onShouldStartLoadWithRequest`, opening other links in the system browser.
- Validate every message in `onMessage` (check the origin with `event.nativeEvent.url`, and the shape of the data).
- Don't inject tokens into pages you don't control.
- Turn off what you don't need: `javaScriptEnabled={false}` for static pages, `allowFileAccess={false}`, `allowUniversalAccessFromFileURLs={false}`.
- Never use a WebView for OAuth login pages of third parties, use the system browser.

### 428: How do you encrypt data stored in a local database?

- Use SQLCipher, an encrypted version of SQLite. `expo-sqlite` supports it with a config plugin option (`useSQLCipher`), and `op-sqlite` supports it too. You set the key with `PRAGMA key`.
- Generate a random key on first launch and store it in Keychain/Keystore (`expo-secure-store`), never in code.
- For key-value data, MMKV supports an encryption key.
- For files, encrypt with a library like `react-native-quick-crypto`, and keep files in the app's private directory.

Also consider what happens on logout (delete the database and key) and in backups (exclude sensitive files from iCloud/Google backups if needed). Encryption protects data if the device is stolen or backed up, but not from code running inside your app.

### 429: What is Expo UI and why is it interesting?

Expo UI (`@expo/ui`) lets you render real SwiftUI views on iOS and Jetpack Compose views on Android from React components:

```tsx
import { Host, Picker, Text } from "@expo/ui/swift-ui";
import { pickerStyle, tag } from "@expo/ui/swift-ui/modifiers";

const ranges = ["Day", "Week", "Month"];

<Host style={{ height: 40 }}>
  <Picker
    modifiers={[pickerStyle("segmented")]}
    label="Range"
    selection={range}
    onSelectionChange={setRange}
  >
    {ranges.map((r) => (
      <Text key={r} modifiers={[tag(r)]}>
        {r}
      </Text>
    ))}
  </Picker>
</Host>;
```

Instead of recreating native controls with `View`s, you get the actual platform controls with their behavior and accessibility. SDK 58 added recycling lists (`List`, `LazyVStack`, `LazyColumn`) and iOS navigation components. It is a different direction from "same UI everywhere": you share logic and choose native UI per platform where it matters. The API is still changing quickly, so check the docs for the current version.

### 430: How do you support hardware keyboards and TV remotes?

- **Focus**: make interactive elements focusable (`focusable` on Android, and `Pressable` is focusable by default on TV platforms). On TV, `react-native-tvos` gives focus navigation with props like `hasTVPreferredFocus` and `nextFocusDown`.
- **Key events**: React Native 0.84 added `onKeyDown` and `onKeyUp` on Android for hardware keyboards and TV remotes. On iOS, keyboard shortcuts usually need native code or a library.
- **Text inputs**: handle `onSubmitEditing` for the Enter key, and tab order between inputs.
- **Visible focus styles**: show which element is focused, since there is no touch.

This matters for tablets with keyboards, Chromebooks running Android apps, accessibility users with switch control, and TV apps.

### 431: How do you support foldables and multi-window?

- Don't assume a fixed screen size or orientation. Use `useWindowDimensions` and update layouts when the window size changes (unfolding, split screen, freeform windows).
- Don't lock orientation. Android 16 ignores orientation and resizability restrictions on large screens for apps targeting it.
- Keep state when the configuration changes. React Native handles this by default, but native modules and video players should handle it too.
- Use two-pane layouts on wide windows (list + details).
- Use `expo-hinge` (SDK 58) or the Jetpack WindowManager library to detect the fold position and posture, and avoid putting content across the hinge.

Test on the Android foldable emulator and in split screen on tablets.

### 432: How do you build and publish a React Native library?

- Start with `create-react-native-library` (Callstack) or `create-expo-module`. They set up an example app, TypeScript, Codegen config and native folders.
- Use `react-native-builder-bob` (included in the first option) to build the JS output and type definitions.
- Support the New Architecture (Turbo Modules / Fabric components, or the Expo Modules API).
- Set `exports` and the `react-native` field in `package.json` correctly, and don't use deep imports from `react-native`.
- Add a config plugin if the library needs native setup in Expo apps.
- Document which React Native and Expo versions are supported, and test the example app on new React Native releases.
- Publish to npm with versioning that signals breaking changes, and list the library on reactnative.directory.

### 433: How do you handle old app versions when your API changes?

Mobile users don't all update, so your API must support several app versions at the same time:

- Make API changes backward compatible: add fields, don't rename or remove them. Use versioned endpoints (`/v2/...`) for bigger changes.
- Send the app version and platform in a header on every request, so the server can adapt responses and you can see which versions are still used.
- Have a minimum supported version. The server returns a specific error (or a config endpoint returns `minVersion`), and the app shows a "please update" screen.
- With OTA updates, most JS bugs can be fixed quickly, but the native binary still decides what is possible.
- Remove support for old versions only after usage drops, and communicate it in the app first.

### 434: A bug happens only on a specific Android device model. How do you investigate?

1. Collect details from crash reports or users: model, Android version, manufacturer skin (Samsung One UI, Xiaomi HyperOS), app version, language, font size, battery saver.
2. Try to get the device: borrow one, buy a used one, or use a remote device farm (Firebase Test Lab, BrowserStack, AWS Device Farm).
3. Check known manufacturer issues: aggressive battery optimization that kills background work, custom font scaling, WebView versions, different camera behaviors, custom keyboards.
4. Get native logs with `adb logcat` from the device.
5. Narrow it down with a minimal reproduction and check the library's issue tracker for the same device.

Many "device-specific" bugs are actually OS skin behaviors, so check dontkillmyapp.com for background issues.

### 435: Your Android app takes 4 seconds to become interactive. How would you bring it under 2 seconds?

1. **Measure** in a release build on a mid-range device: native init time, JS bundle load, first render, data loading. Use Perfetto traces and `performance.mark`.
2. **Native init**: remove or defer SDK initialization in `MainApplication` (analytics, ads, maps).
3. **JS load**: make sure Hermes is used, enable inline requires, and remove heavy imports from the entry path (check with Expo Atlas).
4. **First render**: render a simple first screen. Defer non-visible parts (other tabs, drawers) and heavy providers.
5. **Data**: show cached data from MMKV/SQLite immediately and refresh in the background, instead of waiting for several API calls in sequence. Parallelize the requests that must happen.
6. **Images and fonts**: avoid large images on the first screen, and load fonts at build time with the `expo-font` config plugin.
7. **Re-measure** after each change and add a CI check or production metric so it doesn't regress.

### 436: Users report that the app randomly logs them out. What could cause it?

Possible causes:

- **Refresh race**: several requests get 401 at the same time and each tries to refresh. One refresh rotates the refresh token, the others use the old one and the server revokes the session. Fix with a single shared refresh promise.
- **Tokens stored in a non-persistent place**, or lost because secure storage settings (like iOS keychain accessibility "when unlocked") make reads fail when the app starts in the background.
- **Keychain items lost** after reinstall or device restore, or Android Keystore keys invalidated after the user changes their lock screen or biometrics.
- **Clock skew**: the device time is wrong, so tokens look expired.
- **Server-side session limits** (max devices, short refresh token lifetime).
- **A bug that treats network errors as auth errors** and logs the user out when offline.

Add logging around refresh and logout events (with reasons), then check which case matches.

### 437: The app was rejected by App Review. How do you handle it?

1. Read the rejection message and the guideline number carefully. Check the screenshots or video from the reviewer if given.
2. If it's a bug (crash, broken login), reproduce it with the same OS version and device type. Often the review account doesn't work or the backend blocks the reviewer's region.
3. If it's metadata (description, screenshots, privacy labels), fix it in App Store Connect. It doesn't always need a new build.
4. If it's a policy issue (payments, login options, permissions), change the app or explain in the Resolution Center why it complies.
5. You can reply to the reviewer, and appeal to the App Review Board if you think the decision is wrong.

Keep notes of past rejections, and add checks for them in the release process.

### 438: The app crashes when a user selects 30 photos to upload. Why, and how do you fix it?

Likely an out-of-memory crash: each full-resolution photo is decoded into memory (for thumbnails, resizing or base64 conversion) and 30 at once is too much. Base64 encoding makes it worse because it creates huge strings in JS memory.

Fixes:

- Never load photos as base64 into JS. Work with file URIs.
- Resize and compress photos one by one (`expo-image-manipulator`) before upload, and release each result.
- Upload in a queue with limited concurrency (2-3 at a time), using file-based uploads (`expo-file-system` upload tasks or `FormData` with `uri`).
- Show thumbnails with `expo-image`, which downsamples to the view size.
- Use background upload sessions for large batches so they continue if the user leaves the app.

### 439: How would you build an app that tracks location in the background, like a running tracker?

- Request "while in use" first, then "always"/background location only when the user starts a feature that needs it, with a clear explanation. Apple and Google review this closely.
- Use `expo-location` `startLocationUpdatesAsync` with `expo-task-manager`, or a specialized library like `react-native-background-geolocation`.
- On Android, background tracking needs a foreground service with a persistent notification (`foregroundService` option), and the `FOREGROUND_SERVICE_LOCATION` type.
- On iOS, enable the location background mode and show the blue indicator (`showsBackgroundLocationIndicator`).
- Save points to local storage in the task (SQLite), since the JS UI may not be running, and upload in batches.
- Filter noisy points (accuracy threshold, distance filter) and use activity type hints to save battery.
- Handle the user turning off permission while tracking.

### 440: You need an app for iOS, Android and web from day one. How would you set it up?

- **Expo with Expo Router**: one codebase, file-based routes that map to URLs on web, and native navigation on mobile.
- **Styling** that works on all three: StyleSheet with React Native Web, or NativeWind/Tamagui/Unistyles.
- **Platform splits** with `.web.tsx` and `.native.tsx` files for things like maps, payments and file pickers.
- **Web-specific needs**: static or server rendering for SEO pages, keyboard and hover support, responsive layouts for desktop widths, and accessibility checks with web tools.
- **Shared logic** in packages (API client, validation, state), so a separate Next.js site can reuse it later if needed.
- **CI** that builds web and native, and E2E tests with Playwright for web and Maestro for mobile.

Be honest about trade-offs: content-heavy marketing pages may still be better as a separate web app.

### 441: How would you decide between React Native and fully native for a new product?

Questions to ask:

- **Team**: do you have React/TypeScript developers, or iOS and Android specialists?
- **Product type**: mostly screens, forms, lists, feeds and API calls favor React Native. Heavy graphics, deep OS integration, or a watch-first product favor native.
- **Platforms**: if you need both iOS and Android (and maybe web) with a small team, React Native saves a lot.
- **Speed of iteration**: OTA updates and Fast Refresh help ship faster.
- **Long-term**: the cost of upgrades and third-party native dependencies.
- **Existing code**: an existing native app may suit a brownfield approach.

A common answer: React Native for the product, with native modules for the few parts that need them. Many large companies (Shopify, Microsoft, Meta) use this approach.

### 442: In 2026, would you start a new project with Expo or with the Community CLI?

For most projects, Expo. The React Native docs recommend using a framework, and Expo is the main one. You get CNG, Expo Router, the Expo SDK, EAS Build/Update, good upgrade tooling and a well-tested set of library versions. You can still write any native code (config plugins, local modules), so the old argument "Expo limits native code" no longer applies.

The Community CLI makes sense when you:

- Integrate React Native into an existing native app with its own build system.
- Have strict rules that block Expo packages or services (though EAS is optional).
- Build an out-of-tree platform app (Windows, macOS) where Expo support is limited.
- Want full manual control over native projects.

Even then, you can add Expo modules to a CLI project with `install-expo-modules`.

### 443: React Navigation or Expo Router?

Both use the same navigation engine (Expo Router is built on React Navigation), so performance is the same.

**Expo Router** is a good default when:

- You use Expo.
- You want deep links and web URLs for every screen automatically.
- You like file-based routing (like Next.js) and typed routes.
- You need web support with SSR, API routes or server features.

**React Navigation** fits when:

- You don't use Expo, or you have a brownfield app.
- Navigation is very dynamic (screens defined at runtime, complex conditional flows).
- You prefer configuring navigation in code.

Both support native stacks, tabs, drawers, modals and auth flows, so the choice is mostly about project setup and preferences.

### 444: When would you use Animated and when Reanimated?

**Animated (core)**:

- No extra dependency.
- Good for simple animations: fades, slides, springs, scroll-linked headers with the native driver.
- Since 0.85, can animate layout props natively with the Shared Animation Backend.
- Gesture integration is limited.

**Reanimated**:

- Worklets on the UI thread for complex logic during animations and gestures.
- Works closely with Gesture Handler for interactive UI (drag, swipe, pinch).
- Layout animations (`entering`, `exiting`, `layout`) and CSS-like animations/transitions.
- Requires the New Architecture (v4) and adds a dependency.

Most production apps already include Reanimated (React Navigation drawer, bottom sheets need it), so teams often use it everywhere. For a small app with simple animations, Animated is enough.

### 445: When should you write native code instead of using JavaScript?

Write native code when:

- You need a platform API that no library exposes, or the existing library is unmaintained.
- You integrate a native SDK from a vendor (payments, identity verification, hardware).
- Performance needs it: CPU-heavy processing (image, audio, crypto), camera frame processing, or large data parsing.
- You need OS features outside the app UI: widgets, extensions, Live Activities, watch apps, share extensions.
- A native UI component gives a much better experience (native pickers, maps, video).

Keep native modules small and focused, with a typed JS API. Don't move business logic into native code without a reason, because it doubles the code you maintain (unless you use C++).

### 446: How do you keep a React Native app healthy over many years?

- **Upgrade on a schedule**: follow React Native or Expo SDK releases within a few months. Small, regular upgrades are much cheaper than one big jump.
- **Limit native dependencies**: each one is an upgrade risk. Prefer well-maintained libraries and the Expo SDK.
- **Automate**: Renovate or Dependabot, CI with type checks and tests, E2E smoke tests on every release.
- **Watch deprecations**: fix warnings in each release before APIs are removed (for example deep imports, `InteractionManager`, `SafeAreaView`).
- **Keep native config declarative** (CNG and config plugins) instead of hand-edited native files.
- **Monitor production**: crashes, ANRs, startup time and app size per release.
- **Document decisions**: why a library or pattern was chosen, so it can be revisited later.

### 447: Which newer CSS-like style features does React Native support?

In recent versions, React Native added many styles from CSS (most require the New Architecture):

- `boxShadow` and `filter` (like `brightness`, `blur`, `drop-shadow`), added in 0.76
- `display: 'contents'`, `boxSizing`, `mixBlendMode`, `isolation` and `outline` props, added in 0.77
- `gap`, `rowGap`, `columnGap`
- `position: 'static'`
- `transformOrigin`, and transforms as strings
- `backgroundImage` with linear and radial gradients, and `backgroundSize`, `backgroundPosition` and `backgroundRepeat`, which became stable in 0.88
- `fontVariationSettings` for variable fonts (0.88)
- `aspectRatio` with string values like `'16 / 9'`

Some filters work only on Android. Check the docs for platform support before using them. These features replace many libraries (gradients, shadows) and make it easier to share styles with the web.

### 448: What were the biggest changes in React Native in 2025 and 2026?

- **0.76 (late 2024)**: New Architecture by default, React Native DevTools.
- **0.78**: React 19.
- **0.79**: JSC moved to a community package, faster Metro startup.
- **0.80**: Strict TypeScript API preview, deep import deprecations, legacy architecture frozen.
- **0.81**: Android 16 support, edge-to-edge, `SafeAreaView` deprecated, experimental precompiled iOS builds.
- **0.82**: New Architecture only, Hermes V1 experimental, DOM Node APIs.
- **0.83**: React 19.2, DevTools Network and Performance panels.
- **0.84**: Hermes V1 default, precompiled iOS binaries by default, legacy code removed.
- **0.85**: Shared Animation Backend, `@react-native/jest-preset`.
- **0.86**: edge-to-edge fixes, the repository moved to the `react` GitHub organization.
- **0.87**: Strict TypeScript API by default, faster Metro, experimental SwiftPM, removals like `InteractionManager`.
- **0.88**: web-based event dispatching, variable fonts, iOS SceneDelegate support.

Also: React Native moved to the React Foundation, and React Native came to Meta Quest.

### 449: Where is React Native heading?

Based on recent releases and the core team's plans:

- **Closer to web standards**: DOM-like node APIs, W3C event dispatching, web performance APIs and CSS features, so code and knowledge transfer between web and native.
- **Stable public API**: the Strict TypeScript API and removing deep imports, so libraries break less during upgrades.
- **Faster builds and tooling**: precompiled binaries, Swift Package Manager as the default on iOS, faster Metro and better DevTools.
- **Performance**: Hermes V1, the Shared Animation Backend, and more work in C++ shared across platforms.
- **More platforms**: VR (Meta Quest), desktop and TV through out-of-tree platforms.
- **Frameworks as the default entry point**, mainly Expo, with features like server rendering and native UI components (Expo UI).
- **Fewer breaking changes per release**: several recent releases (0.83, 0.86, 0.88) had no user-facing breaking changes.

### 450: Explain what happens from a state update to pixels on the screen in React Native.

1. **Event**: the user taps a `Pressable`. The touch is received on the UI thread, dispatched through the event system and delivered to the JS thread, where your `onPress` handler runs and calls `setState`.
2. **Render**: React schedules an update and re-renders the affected components on the JS thread, producing new React elements.
3. **Shadow tree**: Fabric clones the changed shadow nodes in C++ with the new props, sharing the unchanged ones.
4. **Layout**: Yoga calculates sizes and positions for the changed parts of the tree, including text measurement.
5. **Commit**: the new tree becomes the next tree to mount. Layout effects (`useLayoutEffect`) run and can read the final layout.
6. **Diff and mount**: Fabric compares the new tree with the previous one, creates a list of mutations (create, update props, insert, remove), and applies them to the real native views on the UI thread. Layout-only views are flattened and never become native views.
7. **Draw**: UIKit or the Android view system draws the updated views in the next frame, and the GPU composes the pixels.
8. **Passive effects**: `useEffect` callbacks run after the commit.

If the update came from an animation with the native driver or Reanimated, steps 1-6 are mostly skipped: the UI thread updates native view props directly each frame.
