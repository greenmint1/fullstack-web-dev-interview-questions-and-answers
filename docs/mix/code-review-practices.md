# Code Review Practices Interview Questions and Answers

_Last updated: November 19, 2026_

450 interview questions about code review practices, split into three levels: 150 easy, 150 moderate and 150 advanced.

This file is about people reviewing other people's code: how to write and read pull requests, how to give and take feedback, what to look for in a diff, and how teams set up their review process. Tool examples use GitHub (with some GitLab and Gerrit), and code examples use TypeScript and Node.js, since that's what most full stack web developers work with.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is a code review?](#1-what-is-a-code-review)
- [2: Why do teams do code reviews?](#2-why-do-teams-do-code-reviews)
- [3: What is a pull request?](#3-what-is-a-pull-request)
- [4: What is the difference between a pull request and a merge request?](#4-what-is-the-difference-between-a-pull-request-and-a-merge-request)
- [5: Who should review code?](#5-who-should-review-code)
- [6: What does LGTM mean?](#6-what-does-lgtm-mean)
- [7: What is a nit in a code review?](#7-what-is-a-nit-in-a-code-review)
- [8: What does a reviewer look for in a code review?](#8-what-does-a-reviewer-look-for-in-a-code-review)
- [9: What is the author's job in a code review?](#9-what-is-the-authors-job-in-a-code-review)
- [10: What is the reviewer's job in a code review?](#10-what-is-the-reviewers-job-in-a-code-review)
- [11: What is the difference between Approve, Request changes and Comment on GitHub?](#11-what-is-the-difference-between-approve-request-changes-and-comment-on-github)
- [12: What is a diff?](#12-what-is-a-diff)
- [13: How do you read a unified diff?](#13-how-do-you-read-a-unified-diff)
- [14: What is a draft pull request?](#14-what-is-a-draft-pull-request)
- [15: What makes a good pull request title?](#15-what-makes-a-good-pull-request-title)
- [16: What makes a good pull request description?](#16-what-makes-a-good-pull-request-description)
- [17: What is a pull request template?](#17-what-is-a-pull-request-template)
- [18: Why should pull requests be small?](#18-why-should-pull-requests-be-small)
- [19: How big should a pull request be?](#19-how-big-should-a-pull-request-be)
- [20: What is a self-review and why should you do it?](#20-what-is-a-self-review-and-why-should-you-do-it)
- [21: What is a code owner?](#21-what-is-a-code-owner)
- [22: What is a CODEOWNERS file?](#22-what-is-a-codeowners-file)
- [23: What is branch protection?](#23-what-is-branch-protection)
- [24: What does "required approvals" mean?](#24-what-does-required-approvals-mean)
- [25: What is the role of CI in code review?](#25-what-is-the-role-of-ci-in-code-review)
- [26: Should reviewers comment on code formatting?](#26-should-reviewers-comment-on-code-formatting)
- [27: How does a linter help code review?](#27-how-does-a-linter-help-code-review)
- [28: What is a style guide and how does it relate to code review?](#28-what-is-a-style-guide-and-how-does-it-relate-to-code-review)
- [29: What is rubber-stamping?](#29-what-is-rubber-stamping)
- [30: What is bikeshedding in code reviews?](#30-what-is-bikeshedding-in-code-reviews)
- [31: How quickly should you respond to a review request?](#31-how-quickly-should-you-respond-to-a-review-request)
- [32: How do you write a good review comment?](#32-how-do-you-write-a-good-review-comment)
- [33: Why should comments be about the code and not the person?](#33-why-should-comments-be-about-the-code-and-not-the-person)
- [34: Is it better to ask questions or give instructions in review comments?](#34-is-it-better-to-ask-questions-or-give-instructions-in-review-comments)
- [35: What is a blocking comment?](#35-what-is-a-blocking-comment)
- [36: What is a non-blocking comment?](#36-what-is-a-non-blocking-comment)
- [37: Should reviewers leave positive comments?](#37-should-reviewers-leave-positive-comments)
- [38: How should an author respond to review comments?](#38-how-should-an-author-respond-to-review-comments)
- [39: What should you do when you disagree with a reviewer?](#39-what-should-you-do-when-you-disagree-with-a-reviewer)
- [40: Who should resolve a comment thread?](#40-who-should-resolve-a-comment-thread)
- [41: What are suggested changes on GitHub?](#41-what-are-suggested-changes-on-github)
- [42: What is a review round?](#42-what-is-a-review-round)
- [43: What does it mean to re-request a review?](#43-what-does-it-mean-to-re-request-a-review)
- [44: What is an over-the-shoulder review?](#44-what-is-an-over-the-shoulder-review)
- [45: Is pair programming a kind of code review?](#45-is-pair-programming-a-kind-of-code-review)
- [46: What is a tool-based code review?](#46-what-is-a-tool-based-code-review)
- [47: How does email-based code review work?](#47-how-does-email-based-code-review-work)
- [48: What is a formal code inspection?](#48-what-is-a-formal-code-inspection)
- [49: What is the difference between pre-commit and post-commit review?](#49-what-is-the-difference-between-pre-commit-and-post-commit-review)
- [50: What is a merge conflict and who should fix it?](#50-what-is-a-merge-conflict-and-who-should-fix-it)
- [51: What does "ship it" mean in a code review?](#51-what-does-ship-it-mean-in-a-code-review)
- [52: Should junior developers review senior developers' code?](#52-should-junior-developers-review-senior-developers-code)
- [53: What can you learn by reviewing other people's code?](#53-what-can-you-learn-by-reviewing-other-peoples-code)
- [54: How does code review help spread knowledge in a team?](#54-how-does-code-review-help-spread-knowledge-in-a-team)
- [55: What is the bus factor and how does code review affect it?](#55-what-is-the-bus-factor-and-how-does-code-review-affect-it)
- [56: What is a code review checklist?](#56-what-is-a-code-review-checklist)
- [57: How do you check the correctness of a change during review?](#57-how-do-you-check-the-correctness-of-a-change-during-review)
- [58: How do you check readability during a review?](#58-how-do-you-check-readability-during-a-review)
- [59: How should you give feedback on naming?](#59-how-should-you-give-feedback-on-naming)
- [60: Should every pull request include tests?](#60-should-every-pull-request-include-tests)
- [61: How do you review tests in a pull request?](#61-how-do-you-review-tests-in-a-pull-request)
- [62: What should you check about error handling in a review?](#62-what-should-you-check-about-error-handling-in-a-review)
- [63: What should you do when you spot duplicated code in a PR?](#63-what-should-you-do-when-you-spot-duplicated-code-in-a-pr)
- [64: Why is commented-out code a problem in a PR?](#64-why-is-commented-out-code-a-problem-in-a-pr)
- [65: What debug leftovers should reviewers look for?](#65-what-debug-leftovers-should-reviewers-look-for)
- [66: Is it OK to have TODO comments in a pull request?](#66-is-it-ok-to-have-todo-comments-in-a-pull-request)
- [67: What should you check in code comments during a review?](#67-what-should-you-check-in-code-comments-during-a-review)
- [68: Why do reviewers ask to replace magic numbers?](#68-why-do-reviewers-ask-to-replace-magic-numbers)
- [69: What should you do if you see a hard-coded secret in a PR?](#69-what-should-you-do-if-you-see-a-hard-coded-secret-in-a-pr)
- [70: Why should reviewers sometimes run the code instead of just reading it?](#70-why-should-reviewers-sometimes-run-the-code-instead-of-just-reading-it)
- [71: How do you check out a pull request locally?](#71-how-do-you-check-out-a-pull-request-locally)
- [72: What are preview deployments and how do they help code review?](#72-what-are-preview-deployments-and-how-do-they-help-code-review)
- [73: Why should UI pull requests include screenshots?](#73-why-should-ui-pull-requests-include-screenshots)
- [74: What is a stale approval?](#74-what-is-a-stale-approval)
- [75: Why should you link issues or tickets to a pull request?](#75-why-should-you-link-issues-or-tickets-to-a-pull-request)
- [76: Why do commit messages matter in code review?](#76-why-do-commit-messages-matter-in-code-review)
- [77: What are Conventional Commits?](#77-what-are-conventional-commits)
- [78: What is an atomic commit?](#78-what-is-an-atomic-commit)
- [79: What is the difference between squash, merge commit and rebase merging?](#79-what-is-the-difference-between-squash-merge-commit-and-rebase-merging)
- [80: Is it OK to force-push during a code review?](#80-is-it-ok-to-force-push-during-a-code-review)
- [81: What does WIP mean on a pull request?](#81-what-does-wip-mean-on-a-pull-request)
- [82: How many reviewers does a pull request need?](#82-how-many-reviewers-does-a-pull-request-need)
- [83: How do teams assign reviewers?](#83-how-do-teams-assign-reviewers)
- [84: What is a review queue?](#84-what-is-a-review-queue)
- [85: Why not just rely on automated tests and skip code review?](#85-why-not-just-rely-on-automated-tests-and-skip-code-review)
- [86: What kinds of problems does code review usually miss?](#86-what-kinds-of-problems-does-code-review-usually-miss)
- [87: Does a hotfix need a code review?](#87-does-a-hotfix-need-a-code-review)
- [88: Should you review code from other teams?](#88-should-you-review-code-from-other-teams)
- [89: Who should merge the pull request?](#89-who-should-merge-the-pull-request)
- [90: What should happen after a pull request is approved?](#90-what-should-happen-after-a-pull-request-is-approved)
- [91: What should you do if your pull request has been waiting for review too long?](#91-what-should-you-do-if-your-pull-request-has-been-waiting-for-review-too-long)
- [92: What is a stale pull request?](#92-what-is-a-stale-pull-request)
- [93: How should you review documentation changes?](#93-how-should-you-review-documentation-changes)
- [94: How should you review configuration changes?](#94-how-should-you-review-configuration-changes)
- [95: What should you check when a pull request adds a new dependency?](#95-what-should-you-check-when-a-pull-request-adds-a-new-dependency)
- [96: Should you review lockfile changes?](#96-should-you-review-lockfile-changes)
- [97: How should generated files be handled in pull requests?](#97-how-should-generated-files-be-handled-in-pull-requests)
- [98: How do you review whitespace-only changes?](#98-how-do-you-review-whitespace-only-changes)
- [99: How do diffs show renamed or moved files?](#99-how-do-diffs-show-renamed-or-moved-files)
- [100: What is the "Viewed" checkbox on GitHub?](#100-what-is-the-viewed-checkbox-on-github)
- [101: Is it OK to review a large pull request in several sessions?](#101-is-it-ok-to-review-a-large-pull-request-in-several-sessions)
- [102: How long should one review session last?](#102-how-long-should-one-review-session-last)
- [103: How do you start reviewing a pull request?](#103-how-do-you-start-reviewing-a-pull-request)
- [104: Why should reviewers read the description before the code?](#104-why-should-reviewers-read-the-description-before-the-code)
- [105: What does "context" mean in a code review?](#105-what-does-context-mean-in-a-code-review)
- [106: Why should review comments explain the "why"?](#106-why-should-review-comments-explain-the-why)
- [107: Should you write "we" or "you" in review comments?](#107-should-you-write-we-or-you-in-review-comments)
- [108: Do emoji and tone matter in written reviews?](#108-do-emoji-and-tone-matter-in-written-reviews)
- [109: Should reviewers point out typos?](#109-should-reviewers-point-out-typos)
- [110: What accessibility checks should reviewers do on UI changes?](#110-what-accessibility-checks-should-reviewers-do-on-ui-changes)
- [111: What should you check for internationalization in a review?](#111-what-should-you-check-for-internationalization-in-a-review)
- [112: What should you check about logging in a review?](#112-what-should-you-check-about-logging-in-a-review)
- [113: Why should reviewers check input validation?](#113-why-should-reviewers-check-input-validation)
- [114: What does "approve with comments" mean?](#114-what-does-approve-with-comments-mean)
- [115: What is a code review guidelines document?](#115-what-is-a-code-review-guidelines-document)
- [116: Why should a team agree on code review rules?](#116-why-should-a-team-agree-on-code-review-rules)
- [117: Do code reviews slow teams down?](#117-do-code-reviews-slow-teams-down)
- [118: Is code review only about finding bugs?](#118-is-code-review-only-about-finding-bugs)
- [119: How can code review be used for mentoring?](#119-how-can-code-review-be-used-for-mentoring)
- [120: What should a new hire focus on in their first code reviews?](#120-what-should-a-new-hire-focus-on-in-their-first-code-reviews)
- [121: How do you review code in a language you don't know well?](#121-how-do-you-review-code-in-a-language-you-dont-know-well)
- [122: Is it OK for a reviewer to say "I don't know"?](#122-is-it-ok-for-a-reviewer-to-say-i-dont-know)
- [123: How should you ask someone to review your pull request?](#123-how-should-you-ask-someone-to-review-your-pull-request)
- [124: How do you politely remind a reviewer about your pull request?](#124-how-do-you-politely-remind-a-reviewer-about-your-pull-request)
- [125: When should you talk in person instead of commenting?](#125-when-should-you-talk-in-person-instead-of-commenting)
- [126: How is reviewing a refactor different from reviewing a feature?](#126-how-is-reviewing-a-refactor-different-from-reviewing-a-feature)
- [127: What is scope creep in a pull request?](#127-what-is-scope-creep-in-a-pull-request)
- [128: Should reviewers ask for "while you're here" changes?](#128-should-reviewers-ask-for-while-youre-here-changes)
- [129: What are follow-up tickets in code review?](#129-what-are-follow-up-tickets-in-code-review)
- [130: Is it OK to approve code you don't fully understand?](#130-is-it-ok-to-approve-code-you-dont-fully-understand)
- [131: Can you review only part of a pull request?](#131-can-you-review-only-part-of-a-pull-request)
- [132: What should you check when a pull request changes UI text?](#132-what-should-you-check-when-a-pull-request-changes-ui-text)
- [133: What should you check in CSS changes during a review?](#133-what-should-you-check-in-css-changes-during-a-review)
- [134: What should you check in SQL queries during a review?](#134-what-should-you-check-in-sql-queries-during-a-review)
- [135: How do you spot a breaking API change in a review?](#135-how-do-you-spot-a-breaking-api-change-in-a-review)
- [136: What does backward compatibility mean in a review?](#136-what-does-backward-compatibility-mean-in-a-review)
- [137: How do feature flags affect code review?](#137-how-do-feature-flags-affect-code-review)
- [138: When should you revert a merged pull request?](#138-when-should-you-revert-a-merged-pull-request)
- [139: What is a blameless review culture?](#139-what-is-a-blameless-review-culture)
- [140: What does "you are not your code" mean?](#140-what-does-you-are-not-your-code-mean)
- [141: Should authors thank reviewers?](#141-should-authors-thank-reviewers)
- [142: What are status checks on a pull request?](#142-what-are-status-checks-on-a-pull-request)
- [143: What is a required status check?](#143-what-is-a-required-status-check)
- [144: How is code review different in open source projects?](#144-how-is-code-review-different-in-open-source-projects)
- [145: What are a CLA and a DCO?](#145-what-are-a-cla-and-a-dco)
- [146: What makes someone a good code reviewer?](#146-what-makes-someone-a-good-code-reviewer)
- [147: What makes an author easy to review?](#147-what-makes-an-author-easy-to-review)
- [148: What are common mistakes new reviewers make?](#148-what-are-common-mistakes-new-reviewers-make)
- [149: What are common mistakes authors make in pull requests?](#149-what-are-common-mistakes-authors-make-in-pull-requests)
- [150: What tools are used for code review?](#150-what-tools-are-used-for-code-review)

### Moderate Questions (151-300)

- [151: How do you structure a review into several passes?](#151-how-do-you-structure-a-review-into-several-passes)
- [152: Why should design problems be raised before line-by-line comments?](#152-why-should-design-problems-be-raised-before-line-by-line-comments)
- [153: When should a reviewer ask for a design doc instead of reviewing code?](#153-when-should-a-reviewer-ask-for-a-design-doc-instead-of-reviewing-code)
- [154: What does Google's "code health" standard for approval mean?](#154-what-does-googles-code-health-standard-for-approval-mean)
- [155: How do you balance perfection and progress in reviews?](#155-how-do-you-balance-perfection-and-progress-in-reviews)
- [156: How can reviewers show how serious a comment is?](#156-how-can-reviewers-show-how-serious-a-comment-is)
- [157: What are Conventional Comments?](#157-what-are-conventional-comments)
- [158: Why is it important to label nits explicitly?](#158-why-is-it-important-to-label-nits-explicitly)
- [159: What should you do when you get a pull request that's too big?](#159-what-should-you-do-when-you-get-a-pull-request-thats-too-big)
- [160: How do you split a large change into smaller pull requests?](#160-how-do-you-split-a-large-change-into-smaller-pull-requests)
- [161: What are stacked pull requests?](#161-what-are-stacked-pull-requests)
- [162: What are the pain points of stacked pull requests on GitHub?](#162-what-are-the-pain-points-of-stacked-pull-requests-on-github)
- [163: How does trunk-based development change code review?](#163-how-does-trunk-based-development-change-code-review)
- [164: What is the Ship/Show/Ask model?](#164-what-is-the-shipshowask-model)
- [165: What is a review SLA?](#165-what-is-a-review-sla)
- [166: What review metrics are useful to track?](#166-what-review-metrics-are-useful-to-track)
- [167: How can a team reduce review wait time?](#167-how-can-a-team-reduce-review-wait-time)
- [168: How do you balance review load across a team?](#168-how-do-you-balance-review-load-across-a-team)
- [169: Why can having many reviewers make reviews worse?](#169-why-can-having-many-reviewers-make-reviews-worse)
- [170: How do you handle a PR that needs approval from several teams?](#170-how-do-you-handle-a-pr-that-needs-approval-from-several-teams)
- [171: How do pattern rules work in a CODEOWNERS file?](#171-how-do-pattern-rules-work-in-a-codeowners-file)
- [172: What are common mistakes with CODEOWNERS?](#172-what-are-common-mistakes-with-codeowners)
- [173: What does "Dismiss stale approvals" do?](#173-what-does-dismiss-stale-approvals-do)
- [174: What does "Require approval of the most recent reviewable push" mean?](#174-what-does-require-approval-of-the-most-recent-reviewable-push-mean)
- [175: What does "Require conversation resolution before merging" do?](#175-what-does-require-conversation-resolution-before-merging-do)
- [176: What is the difference between branch protection rules and rulesets on GitHub?](#176-what-is-the-difference-between-branch-protection-rules-and-rulesets-on-github)
- [177: What is a merge queue and how does it relate to code review?](#177-what-is-a-merge-queue-and-how-does-it-relate-to-code-review)
- [178: What is auto-merge and when is it useful?](#178-what-is-auto-merge-and-when-is-it-useful)
- [179: How can you do code reviews from the command line?](#179-how-can-you-do-code-reviews-from-the-command-line)
- [180: Should you review a PR commit by commit or as a whole diff?](#180-should-you-review-a-pr-commit-by-commit-or-as-a-whole-diff)
- [181: What are fixup commits and how do they help during review?](#181-what-are-fixup-commits-and-how-do-they-help-during-review)
- [182: Should authors force-push or add new commits when addressing feedback?](#182-should-authors-force-push-or-add-new-commits-when-addressing-feedback)
- [183: What is git range-diff and how does it help reviewers?](#183-what-is-git-range-diff-and-how-does-it-help-reviewers)
- [184: How do you see only what changed since your last review?](#184-how-do-you-see-only-what-changed-since-your-last-review)
- [185: Which git diff options are useful for code review?](#185-which-git-diff-options-are-useful-for-code-review)
- [186: How do you review code that was moved and changed at the same time?](#186-how-do-you-review-code-that-was-moved-and-changed-at-the-same-time)
- [187: What is .git-blame-ignore-revs?](#187-what-is-git-blame-ignore-revs)
- [188: How do you review a large formatting change?](#188-how-do-you-review-a-large-formatting-change)
- [189: How do you review a codemod or automated refactor?](#189-how-do-you-review-a-codemod-or-automated-refactor)
- [190: What are signs of good tests in a pull request?](#190-what-are-signs-of-good-tests-in-a-pull-request)
- [191: Is test coverage a good way to judge tests in a review?](#191-is-test-coverage-a-good-way-to-judge-tests-in-a-review)
- [192: How can a test pass for the wrong reason?](#192-how-can-a-test-pass-for-the-wrong-reason)
- [193: What should you say when tests use too many mocks?](#193-what-should-you-say-when-tests-use-too-many-mocks)
- [194: What should a reviewer do about a flaky test in a PR?](#194-what-should-a-reviewer-do-about-a-flaky-test-in-a-pr)
- [195: What async error handling mistakes should reviewers look for?](#195-what-async-error-handling-mistakes-should-reviewers-look-for)
- [196: How do you spot a missing await in a review?](#196-how-do-you-spot-a-missing-await-in-a-review)
- [197: What null and undefined problems should reviewers look for?](#197-what-null-and-undefined-problems-should-reviewers-look-for)
- [198: How do you look for off-by-one errors in a review?](#198-how-do-you-look-for-off-by-one-errors-in-a-review)
- [199: What race conditions can show up in web app code?](#199-what-race-conditions-can-show-up-in-web-app-code)
- [200: What should you check when reviewing React useEffect changes?](#200-what-should-you-check-when-reviewing-react-useeffect-changes)
- [201: What should you check when reviewing state management changes?](#201-what-should-you-check-when-reviewing-state-management-changes)
- [202: What should you check when reviewing a new API endpoint?](#202-what-should-you-check-when-reviewing-a-new-api-endpoint)
- [203: What should you look for when reviewing a database migration?](#203-what-should-you-look-for-when-reviewing-a-database-migration)
- [204: How do you spot an N+1 query problem in a review?](#204-how-do-you-spot-an-n1-query-problem-in-a-review)
- [205: What should you check about database indexes in a review?](#205-what-should-you-check-about-database-indexes-in-a-review)
- [206: What should you check when a PR adds a new environment variable?](#206-what-should-you-check-when-a-pr-adds-a-new-environment-variable)
- [207: How do you review infrastructure-as-code changes?](#207-how-do-you-review-infrastructure-as-code-changes)
- [208: What should you check when reviewing CI pipeline changes?](#208-what-should-you-check-when-reviewing-ci-pipeline-changes)
- [209: How do you review a dependency upgrade PR?](#209-how-do-you-review-a-dependency-upgrade-pr)
- [210: How do you evaluate whether a new dependency should be added?](#210-how-do-you-evaluate-whether-a-new-dependency-should-be-added)
- [211: What basic security checks should every reviewer do?](#211-what-basic-security-checks-should-every-reviewer-do)
- [212: How do you spot a missing authorization check in a review?](#212-how-do-you-spot-a-missing-authorization-check-in-a-review)
- [213: What should happen if a secret is pushed in a pull request?](#213-what-should-happen-if-a-secret-is-pushed-in-a-pull-request)
- [214: How do you spot sensitive data in logs during a review?](#214-how-do-you-spot-sensitive-data-in-logs-during-a-review)
- [215: How do you review performance-sensitive code?](#215-how-do-you-review-performance-sensitive-code)
- [216: When should a reviewer ask for benchmarks?](#216-when-should-a-reviewer-ask-for-benchmarks)
- [217: What deeper accessibility issues should you look for in UI reviews?](#217-what-deeper-accessibility-issues-should-you-look-for-in-ui-reviews)
- [218: What should you check about error messages and UX in a review?](#218-what-should-you-check-about-error-messages-and-ux-in-a-review)
- [219: Why do names matter more at API boundaries?](#219-why-do-names-matter-more-at-api-boundaries)
- [220: What should you check in documentation for public APIs?](#220-what-should-you-check-in-documentation-for-public-apis)
- [221: What should you check about observability in a review?](#221-what-should-you-check-about-observability-in-a-review)
- [222: What should reviewers check about feature flag removal?](#222-what-should-reviewers-check-about-feature-flag-removal)
- [223: How do you review a pull request that deletes code?](#223-how-do-you-review-a-pull-request-that-deletes-code)
- [224: What is premature abstraction and how do you spot it in a review?](#224-what-is-premature-abstraction-and-how-do-you-spot-it-in-a-review)
- [225: How do you push back on over-engineering in a PR without being rude?](#225-how-do-you-push-back-on-over-engineering-in-a-pr-without-being-rude)
- [226: How do you handle a PR that uses a quick hack?](#226-how-do-you-handle-a-pr-that-uses-a-quick-hack)
- [227: Should new code follow existing patterns or better new ones?](#227-should-new-code-follow-existing-patterns-or-better-new-ones)
- [228: How should someone introduce a new pattern or library through a PR?](#228-how-should-someone-introduce-a-new-pattern-or-library-through-a-pr)
- [229: How do you tell personal preference from a real issue in a review?](#229-how-do-you-tell-personal-preference-from-a-real-issue-in-a-review)
- [230: How do you resolve a disagreement in a code review?](#230-how-do-you-resolve-a-disagreement-in-a-code-review)
- [231: When should a code review disagreement be escalated?](#231-when-should-a-code-review-disagreement-be-escalated)
- [232: What should a reviewer do when they realize they were wrong?](#232-what-should-a-reviewer-do-when-they-realize-they-were-wrong)
- [233: How should an author respond when a reviewer asks for something out of scope?](#233-how-should-an-author-respond-when-a-reviewer-asks-for-something-out-of-scope)
- [234: How do you handle an author who gets defensive about feedback?](#234-how-do-you-handle-an-author-who-gets-defensive-about-feedback)
- [235: How do you handle a reviewer whose comments are harsh?](#235-how-do-you-handle-a-reviewer-whose-comments-are-harsh)
- [236: How do you give critical feedback to a more senior engineer?](#236-how-do-you-give-critical-feedback-to-a-more-senior-engineer)
- [237: How do you run code reviews across time zones?](#237-how-do-you-run-code-reviews-across-time-zones)
- [238: What is a code walkthrough and when is it useful?](#238-what-is-a-code-walkthrough-and-when-is-it-useful)
- [239: What is mob review?](#239-what-is-mob-review)
- [240: When is synchronous review better than asynchronous review?](#240-when-is-synchronous-review-better-than-asynchronous-review)
- [241: How do you review your manager's code?](#241-how-do-you-review-your-managers-code)
- [242: What could a team's review checklist look like?](#242-what-could-a-teams-review-checklist-look-like)
- [243: Why should review checklists be short?](#243-why-should-review-checklists-be-short)
- [244: What review work can be automated?](#244-what-review-work-can-be-automated)
- [245: What is Danger.js and how is it used in code review?](#245-what-is-dangerjs-and-how-is-it-used-in-code-review)
- [246: How can you automatically flag pull requests that are too big?](#246-how-can-you-automatically-flag-pull-requests-that-are-too-big)
- [247: How are labels used to manage pull requests?](#247-how-are-labels-used-to-manage-pull-requests)
- [248: What should a good pull request template include?](#248-what-should-a-good-pull-request-template-include)
- [249: What is a definition of done and how does it relate to code review?](#249-what-is-a-definition-of-done-and-how-does-it-relate-to-code-review)
- [250: How do you review an architecture decision record?](#250-how-do-you-review-an-architecture-decision-record)
- [251: How is reviewing an RFC different from reviewing code?](#251-how-is-reviewing-an-rfc-different-from-reviewing-code)
- [252: What do open source maintainers look for when reviewing a PR?](#252-what-do-open-source-maintainers-look-for-when-reviewing-a-pr)
- [253: How should maintainers review PRs from first-time contributors?](#253-how-should-maintainers-review-prs-from-first-time-contributors)
- [254: What are Reviewed-by and Acked-by tags in the Linux kernel?](#254-what-are-reviewed-by-and-acked-by-tags-in-the-linux-kernel)
- [255: How does code review work in Gerrit?](#255-how-does-code-review-work-in-gerrit)
- [256: What are Change-Id and patch sets in Gerrit?](#256-what-are-change-id-and-patch-sets-in-gerrit)
- [257: How do approval rules work in GitLab?](#257-how-do-approval-rules-work-in-gitlab)
- [258: How do branch policies work in Azure DevOps?](#258-how-do-branch-policies-work-in-azure-devops)
- [259: How should you review a hotfix during an incident?](#259-how-should-you-review-a-hotfix-during-an-incident)
- [260: How do you make sure post-merge reviews actually happen?](#260-how-do-you-make-sure-post-merge-reviews-actually-happen)
- [261: How should you review a revert PR?](#261-how-should-you-review-a-revert-pr)
- [262: How do you review generated code like API clients?](#262-how-do-you-review-generated-code-like-api-clients)
- [263: What should you check when reviewing a Dockerfile?](#263-what-should-you-check-when-reviewing-a-dockerfile)
- [264: What security issues should you look for in GitHub Actions workflow changes?](#264-what-security-issues-should-you-look-for-in-github-actions-workflow-changes)
- [265: What should you check when a PR adds a third-party script to the front end?](#265-what-should-you-check-when-a-pr-adds-a-third-party-script-to-the-front-end)
- [266: What should you check when reviewing caching changes?](#266-what-should-you-check-when-reviewing-caching-changes)
- [267: Why is module-level state risky in a Node.js server?](#267-why-is-module-level-state-risky-in-a-nodejs-server)
- [268: What should you check about timeouts and retries when reviewing network calls?](#268-what-should-you-check-about-timeouts-and-retries-when-reviewing-network-calls)
- [269: What should you check when reviewing pagination code?](#269-what-should-you-check-when-reviewing-pagination-code)
- [270: Why is adding a required field to an API request a breaking change?](#270-why-is-adding-a-required-field-to-an-api-request-a-breaking-change)
- [271: What should you check when reviewing event or message schema changes?](#271-what-should-you-check-when-reviewing-event-or-message-schema-changes)
- [272: Why should risky PRs include a rollback plan?](#272-why-should-risky-prs-include-a-rollback-plan)
- [273: How do you review code for testability?](#273-how-do-you-review-code-for-testability)
- [274: How do visual tests and Storybook help code review?](#274-how-do-visual-tests-and-storybook-help-code-review)
- [275: What should reviewers check about any and type assertions in TypeScript?](#275-what-should-reviewers-check-about-any-and-type-assertions-in-typescript)
- [276: Why are non-null assertions a review concern in TypeScript?](#276-why-are-non-null-assertions-a-review-concern-in-typescript)
- [277: How should errors be wrapped and rethrown?](#277-how-should-errors-be-wrapped-and-rethrown)
- [278: How do you review log levels?](#278-how-do-you-review-log-levels)
- [279: What code smells should reviewers watch for?](#279-what-code-smells-should-reviewers-watch-for)
- [280: Why do reviewers push back on boolean flag parameters?](#280-why-do-reviewers-push-back-on-boolean-flag-parameters)
- [281: How do guard clauses improve code under review?](#281-how-do-guard-clauses-improve-code-under-review)
- [282: How should repeated string values be handled in TypeScript code?](#282-how-should-repeated-string-values-be-handled-in-typescript-code)
- [283: What should you check about file and module organization in a review?](#283-what-should-you-check-about-file-and-module-organization-in-a-review)
- [284: Why are circular dependencies a review concern?](#284-why-are-circular-dependencies-a-review-concern)
- [285: How do you decide which review comments matter most?](#285-how-do-you-decide-which-review-comments-matter-most)
- [286: How many comments are too many in a review?](#286-how-many-comments-are-too-many-in-a-review)
- [287: Why should reviewers batch comments into one review?](#287-why-should-reviewers-batch-comments-into-one-review)
- [288: What should you check when re-reviewing a pull request?](#288-what-should-you-check-when-re-reviewing-a-pull-request)
- [289: Is it OK to approve and trust the author to fix the remaining comments?](#289-is-it-ok-to-approve-and-trust-the-author-to-fix-the-remaining-comments)
- [290: Can you do code reviews inside your editor?](#290-can-you-do-code-reviews-inside-your-editor)
- [291: How should PRs from bots like Dependabot or Renovate be reviewed?](#291-how-should-prs-from-bots-like-dependabot-or-renovate-be-reviewed)
- [292: What should you check about time in tests during review?](#292-what-should-you-check-about-time-in-tests-during-review)
- [293: Why are environment checks in code a review concern?](#293-why-are-environment-checks-in-code-a-review-concern)
- [294: How should changes to shared libraries or components be reviewed?](#294-how-should-changes-to-shared-libraries-or-components-be-reviewed)
- [295: How do you review a PR when you know nothing about that part of the code?](#295-how-do-you-review-a-pr-when-you-know-nothing-about-that-part-of-the-code)
- [296: What should a review summary comment include?](#296-what-should-a-review-summary-comment-include)
- [297: How do you review a regular expression in a PR?](#297-how-do-you-review-a-regular-expression-in-a-pr)
- [298: What should you check when a PR adds analytics or tracking events?](#298-what-should-you-check-when-a-pr-adds-analytics-or-tracking-events)
- [299: Should one-off scripts and data fixes be reviewed?](#299-should-one-off-scripts-and-data-fixes-be-reviewed)
- [300: How can you keep improving as a reviewer over time?](#300-how-can-you-keep-improving-as-a-reviewer-over-time)

### Advanced Questions (301-450)

- [301: What kinds of problems do code reviews actually find, according to research?](#301-what-kinds-of-problems-do-code-reviews-actually-find-according-to-research)
- [302: What did the Cisco code review study find?](#302-what-did-the-cisco-code-review-study-find)
- [303: Which code review metrics can do more harm than good?](#303-which-code-review-metrics-can-do-more-harm-than-good)
- [304: How does code review relate to the DORA metrics?](#304-how-does-code-review-relate-to-the-dora-metrics)
- [305: Why does review latency hurt more than it seems?](#305-why-does-review-latency-hurt-more-than-it-seems)
- [306: How would you design a code review process for a team growing from 10 to 100 engineers?](#306-how-would-you-design-a-code-review-process-for-a-team-growing-from-10-to-100-engineers)
- [307: What review process makes sense for a startup of three engineers?](#307-what-review-process-makes-sense-for-a-startup-of-three-engineers)
- [308: How does code review work in regulated industries?](#308-how-does-code-review-work-in-regulated-industries)
- [309: How do you prevent people from approving their own changes?](#309-how-do-you-prevent-people-from-approving-their-own-changes)
- [310: What makes a good audit trail for code changes?](#310-what-makes-a-good-audit-trail-for-code-changes)
- [311: How do you handle code review in a large monorepo with many owners?](#311-how-do-you-handle-code-review-in-a-large-monorepo-with-many-owners)
- [312: How does Google's code review process work?](#312-how-does-googles-code-review-process-work)
- [313: How do teams review large-scale changes that touch thousands of files?](#313-how-do-teams-review-large-scale-changes-that-touch-thousands-of-files)
- [314: How do you roll out a breaking API change across many consumers?](#314-how-do-you-roll-out-a-breaking-api-change-across-many-consumers)
- [315: How do you review code for idempotency?](#315-how-do-you-review-code-for-idempotency)
- [316: What should you check about transactions in a review?](#316-what-should-you-check-about-transactions-in-a-review)
- [317: How do you spot a check-then-act race condition in a review?](#317-how-do-you-spot-a-check-then-act-race-condition-in-a-review)
- [318: What is optimistic concurrency and when should a reviewer suggest it?](#318-what-is-optimistic-concurrency-and-when-should-a-reviewer-suggest-it)
- [319: What makes a database migration dangerous on a large table?](#319-what-makes-a-database-migration-dangerous-on-a-large-table)
- [320: What is the expand and contract pattern for schema changes?](#320-what-is-the-expand-and-contract-pattern-for-schema-changes)
- [321: What should you check when reviewing a data backfill?](#321-what-should-you-check-when-reviewing-a-data-backfill)
- [322: What cache problems should reviewers look for at scale?](#322-what-cache-problems-should-reviewers-look-for-at-scale)
- [323: What should you check when reviewing a message queue consumer?](#323-what-should-you-check-when-reviewing-a-message-queue-consumer)
- [324: Why should retries use exponential backoff and jitter?](#324-why-should-retries-use-exponential-backoff-and-jitter)
- [325: How do you review code for cascading failures?](#325-how-do-you-review-code-for-cascading-failures)
- [326: What memory leak patterns should you look for in Node.js code?](#326-what-memory-leak-patterns-should-you-look-for-in-nodejs-code)
- [327: What front-end performance issues should reviewers look for?](#327-what-front-end-performance-issues-should-reviewers-look-for)
- [328: How can bundle size be checked as part of code review?](#328-how-can-bundle-size-be-checked-as-part-of-code-review)
- [329: How do you spot an SSRF risk in a code review?](#329-how-do-you-spot-an-ssrf-risk-in-a-code-review)
- [330: What is prototype pollution and how do you spot it in a review?](#330-what-is-prototype-pollution-and-how-do-you-spot-it-in-a-review)
- [331: What should reviewers check in code that uses cryptography?](#331-what-should-reviewers-check-in-code-that-uses-cryptography)
- [332: What mistakes in JWT handling should reviewers catch?](#332-what-mistakes-in-jwt-handling-should-reviewers-catch)
- [333: What should you check when a PR changes CORS or CSRF settings?](#333-what-should-you-check-when-a-pr-changes-cors-or-csrf-settings)
- [334: Where can XSS still happen in a React app?](#334-where-can-xss-still-happen-in-a-react-app)
- [335: What is ReDoS and how do you catch it in review?](#335-what-is-redos-and-how-do-you-catch-it-in-review)
- [336: How do you spot a path traversal bug in a review?](#336-how-do-you-spot-a-path-traversal-bug-in-a-review)
- [337: Can SQL injection happen when using an ORM?](#337-can-sql-injection-happen-when-using-an-orm)
- [338: How can a malicious change get past code review?](#338-how-can-a-malicious-change-get-past-code-review)
- [339: Why are PRs from forks a security concern for CI?](#339-why-are-prs-from-forks-a-security-concern-for-ci)
- [340: What is typosquatting and how can review catch it?](#340-what-is-typosquatting-and-how-can-review-catch-it)
- [341: Why should reviewers care about install scripts in dependencies?](#341-why-should-reviewers-care-about-install-scripts-in-dependencies)
- [342: When should a security team be involved in code review?](#342-when-should-a-security-team-be-involved-in-code-review)
- [343: How can you do lightweight threat modeling during a review?](#343-how-can-you-do-lightweight-threat-modeling-during-a-review)
- [344: What privacy issues should reviewers check for?](#344-what-privacy-issues-should-reviewers-check-for)
- [345: How do you manage feature flag debt through code review?](#345-how-do-you-manage-feature-flag-debt-through-code-review)
- [346: What should you check when a PR changes alerts or monitoring?](#346-what-should-you-check-when-a-pr-changes-alerts-or-monitoring)
- [347: How do you review IAM and permission changes in cloud infrastructure?](#347-how-do-you-review-iam-and-permission-changes-in-cloud-infrastructure)
- [348: What should you check when reviewing Kubernetes manifests?](#348-what-should-you-check-when-reviewing-kubernetes-manifests)
- [349: How do canary releases and progressive delivery change what reviewers worry about?](#349-how-do-canary-releases-and-progressive-delivery-change-what-reviewers-worry-about)
- [350: How should a PR that fixes an incident be reviewed?](#350-how-should-a-pr-that-fixes-an-incident-be-reviewed)
- [351: How is an architecture review different from a code review?](#351-how-is-an-architecture-review-different-from-a-code-review)
- [352: Why is a code review often the wrong place for design feedback?](#352-why-is-a-code-review-often-the-wrong-place-for-design-feedback)
- [353: What does a lightweight design review look like?](#353-what-does-a-lightweight-design-review-look-like)
- [354: What should you check when reviewing a REST API design?](#354-what-should-you-check-when-reviewing-a-rest-api-design)
- [355: What should you check when reviewing GraphQL schema changes?](#355-what-should-you-check-when-reviewing-graphql-schema-changes)
- [356: How does semantic versioning affect library code review?](#356-how-does-semantic-versioning-affect-library-code-review)
- [357: How should deprecations be handled and reviewed?](#357-how-should-deprecations-be-handled-and-reviewed)
- [358: Why should error responses be treated as part of the API contract?](#358-why-should-error-responses-be-treated-as-part-of-the-api-contract)
- [359: How do you review front-end code for stale responses?](#359-how-do-you-review-front-end-code-for-stale-responses)
- [360: What should you check when reviewing optimistic UI updates?](#360-what-should-you-check-when-reviewing-optimistic-ui-updates)
- [361: What should you look for in server-rendered React code during review?](#361-what-should-you-look-for-in-server-rendered-react-code-during-review)
- [362: What internationalization edge cases should advanced reviewers catch?](#362-what-internationalization-edge-cases-should-advanced-reviewers-catch)
- [363: What time zone and date bugs should reviewers look for?](#363-what-time-zone-and-date-bugs-should-reviewers-look-for)
- [364: Why should money not be stored as floating point numbers?](#364-why-should-money-not-be-stored-as-floating-point-numbers)
- [365: What Unicode problems can reviewers catch?](#365-what-unicode-problems-can-reviewers-catch)
- [366: How do you review a large refactor done with the strangler fig pattern?](#366-how-do-you-review-a-large-refactor-done-with-the-strangler-fig-pattern)
- [367: How should a team review a proposal to rewrite a system from scratch?](#367-how-should-a-team-review-a-proposal-to-rewrite-a-system-from-scratch)
- [368: How do you judge the balance of test types in a PR?](#368-how-do-you-judge-the-balance-of-test-types-in-a-pr)
- [369: What are the problems with snapshot tests and how should they be reviewed?](#369-what-are-the-problems-with-snapshot-tests-and-how-should-they-be-reviewed)
- [370: What should you check when a PR adds end-to-end tests?](#370-what-should-you-check-when-a-pr-adds-end-to-end-tests)
- [371: How should test data and fixtures be reviewed?](#371-how-should-test-data-and-fixtures-be-reviewed)
- [372: What is mutation testing and how can it help reviews?](#372-what-is-mutation-testing-and-how-can-it-help-reviews)
- [373: How do you review code that you can't easily run?](#373-how-do-you-review-code-that-you-cant-easily-run)
- [374: How do you review concurrent code when tests can't prove it's correct?](#374-how-do-you-review-concurrent-code-when-tests-cant-prove-its-correct)
- [375: What makes reviewing mentally tiring, and how do you deal with it?](#375-what-makes-reviewing-mentally-tiring-and-how-do-you-deal-with-it)
- [376: What is review fatigue and how can teams avoid it?](#376-what-is-review-fatigue-and-how-can-teams-avoid-it)
- [377: What cognitive biases affect code reviews?](#377-what-cognitive-biases-affect-code-reviews)
- [378: What does research say about bias in code review?](#378-what-does-research-say-about-bias-in-code-review)
- [379: What is psychological safety and why does it matter for code review?](#379-what-is-psychological-safety-and-why-does-it-matter-for-code-review)
- [380: How would you fix a toxic code review culture?](#380-how-would-you-fix-a-toxic-code-review-culture)
- [381: What is gatekeeping in code review?](#381-what-is-gatekeeping-in-code-review)
- [382: What is nitpick culture and how do you move away from it?](#382-what-is-nitpick-culture-and-how-do-you-move-away-from-it)
- [383: How do power dynamics affect code review?](#383-how-do-power-dynamics-affect-code-review)
- [384: How do you deal with a reviewer who blocks almost every PR?](#384-how-do-you-deal-with-a-reviewer-who-blocks-almost-every-pr)
- [385: How do you deal with an author who ignores review feedback?](#385-how-do-you-deal-with-an-author-who-ignores-review-feedback)
- [386: How do you coach someone to become a better reviewer?](#386-how-do-you-coach-someone-to-become-a-better-reviewer)
- [387: What is a review calibration session?](#387-what-is-a-review-calibration-session)
- [388: Should reviews themselves be reviewed?](#388-should-reviews-themselves-be-reviewed)
- [389: How do you onboard someone as a reviewer for a new area of the code?](#389-how-do-you-onboard-someone-as-a-reviewer-for-a-new-area-of-the-code)
- [390: What is shadow reviewing?](#390-what-is-shadow-reviewing)
- [391: What are different ways to design a review rotation?](#391-what-are-different-ways-to-design-a-review-rotation)
- [392: If a team pairs or mobs on code, does it still need pull request reviews?](#392-if-a-team-pairs-or-mobs-on-code-does-it-still-need-pull-request-reviews)
- [393: Is it OK to let senior engineers merge without pre-merge review?](#393-is-it-ok-to-let-senior-engineers-merge-without-pre-merge-review)
- [394: How do you decide how deep a review should be?](#394-how-do-you-decide-how-deep-a-review-should-be)
- [395: How does a stacked diff workflow work in practice?](#395-how-does-a-stacked-diff-workflow-work-in-practice)
- [396: What happens when a change is needed in the middle of a PR stack?](#396-what-happens-when-a-change-is-needed-in-the-middle-of-a-pr-stack)
- [397: What makes a good commit series for review?](#397-what-makes-a-good-commit-series-for-review)
- [398: How should an author clean up commits before merging?](#398-how-should-an-author-clean-up-commits-before-merging)
- [399: What does it mean for history to be bisectable, and why do reviewers care?](#399-what-does-it-mean-for-history-to-be-bisectable-and-why-do-reviewers-care)
- [400: How do you review a merge conflict resolution?](#400-how-do-you-review-a-merge-conflict-resolution)
- [401: How should backports and cherry-picks to release branches be reviewed?](#401-how-should-backports-and-cherry-picks-to-release-branches-be-reviewed)
- [402: Should release branches have stricter review rules?](#402-should-release-branches-have-stricter-review-rules)
- [403: How do you review a 2,000-line PR that really can't be split?](#403-how-do-you-review-a-2000-line-pr-that-really-cant-be-split)
- [404: You approved a PR that later caused a production bug. What do you do?](#404-you-approved-a-pr-that-later-caused-a-production-bug-what-do-you-do)
- [405: You find a security vulnerability in code that was merged last week. What do you do?](#405-you-find-a-security-vulnerability-in-code-that-was-merged-last-week-what-do-you-do)
- [406: An author pushes new commits after you approved and merges without re-review. How do you handle it?](#406-an-author-pushes-new-commits-after-you-approved-and-merges-without-re-review-how-do-you-handle-it)
- [407: Production is down at 2 AM, you have a fix and no reviewer is awake. What do you do?](#407-production-is-down-at-2-am-you-have-a-fix-and-no-reviewer-is-awake-what-do-you-do)
- [408: Two reviewers give opposite feedback on your PR. What do you do?](#408-two-reviewers-give-opposite-feedback-on-your-pr-what-do-you-do)
- [409: A teammate keeps sending huge pull requests. How do you handle it?](#409-a-teammate-keeps-sending-huge-pull-requests-how-do-you-handle-it)
- [410: Another team sends a PR into code your team owns. How do you review it?](#410-another-team-sends-a-pr-into-code-your-team-owns-how-do-you-review-it)
- [411: While reviewing, you realize the PR implements the wrong requirement. What do you do?](#411-while-reviewing-you-realize-the-pr-implements-the-wrong-requirement-what-do-you-do)
- [412: A reviewer asks for a big rewrite after several review rounds. How should this be handled?](#412-a-reviewer-asks-for-a-big-rewrite-after-several-review-rounds-how-should-this-be-handled)
- [413: A style debate on a PR has gone on for days. How do you end it?](#413-a-style-debate-on-a-pr-has-gone-on-for-days-how-do-you-end-it)
- [414: A junior's first PR has many problems. How do you review it?](#414-a-juniors-first-pr-has-many-problems-how-do-you-review-it)
- [415: You find a serious flaw in a senior engineer's PR. How do you raise it?](#415-you-find-a-serious-flaw-in-a-senior-engineers-pr-how-do-you-raise-it)
- [416: You're asked to review a PR but you have no time. What do you do?](#416-youre-asked-to-review-a-pr-but-you-have-no-time-what-do-you-do)
- [417: Review backlog is growing across the whole team. What changes would you make?](#417-review-backlog-is-growing-across-the-whole-team-what-changes-would-you-make)
- [418: You're reviewing a PR that changes code you originally wrote. What should you watch for?](#418-youre-reviewing-a-pr-that-changes-code-you-originally-wrote-what-should-you-watch-for)
- [419: How do you review code delivered by an outside contractor or agency?](#419-how-do-you-review-code-delivered-by-an-outside-contractor-or-agency)
- [420: An open source contributor sends a PR you don't want to merge. How do you respond?](#420-an-open-source-contributor-sends-a-pr-you-dont-want-to-merge-how-do-you-respond)
- [421: A PR depends on an unmerged PR in another repository. How should it be reviewed and merged?](#421-a-pr-depends-on-an-unmerged-pr-in-another-repository-how-should-it-be-reviewed-and-merged)
- [422: A flaky test keeps blocking merges. What should the team do?](#422-a-flaky-test-keeps-blocking-merges-what-should-the-team-do)
- [423: The team that owns some code never reviews PRs in time. What do you do?](#423-the-team-that-owns-some-code-never-reviews-prs-in-time-what-do-you-do)
- [424: How do you approach a live code review exercise in an interview?](#424-how-do-you-approach-a-live-code-review-exercise-in-an-interview)
- [425: What problems can you find in this Express handler?](#425-what-problems-can-you-find-in-this-express-handler)
- [426: What problems can you find in this React component?](#426-what-problems-can-you-find-in-this-react-component)
- [427: What problems can you find in this data processing function?](#427-what-problems-can-you-find-in-this-data-processing-function)
- [428: How can a team tell whether its code reviews are improving quality?](#428-how-can-a-team-tell-whether-its-code-reviews-are-improving-quality)
- [429: Are there cases where skipping code review is the right call?](#429-are-there-cases-where-skipping-code-review-is-the-right-call)
- [430: What is policy as code and how does it relate to code review?](#430-what-is-policy-as-code-and-how-does-it-relate-to-code-review)
- [431: Why would a team require signed commits?](#431-why-would-a-team-require-signed-commits)
- [432: Can a PR that passed review and CI still break main after merging?](#432-can-a-pr-that-passed-review-and-ci-still-break-main-after-merging)
- [433: How does peer code review compare to a change advisory board?](#433-how-does-peer-code-review-compare-to-a-change-advisory-board)
- [434: What should a team's code review guidelines document include?](#434-what-should-a-teams-code-review-guidelines-document-include)
- [435: How would you introduce code review to a team that has never done it?](#435-how-would-you-introduce-code-review-to-a-team-that-has-never-done-it)
- [436: What problems does an unbounded Promise.all cause, and how do you catch it in review?](#436-what-problems-does-an-unbounded-promiseall-cause-and-how-do-you-catch-it-in-review)
- [437: What should you check when reviewing rate limiting code?](#437-what-should-you-check-when-reviewing-rate-limiting-code)
- [438: What should you check when reviewing file upload code?](#438-what-should-you-check-when-reviewing-file-upload-code)
- [439: What should you check when reviewing a webhook handler?](#439-what-should-you-check-when-reviewing-a-webhook-handler)
- [440: How do you review code for tenant isolation in a multi-tenant app?](#440-how-do-you-review-code-for-tenant-isolation-in-a-multi-tenant-app)
- [441: What should you check when a PR adds soft deletes?](#441-what-should-you-check-when-a-pr-adds-soft-deletes)
- [442: What should you check when reviewing code that sends emails or notifications?](#442-what-should-you-check-when-reviewing-code-that-sends-emails-or-notifications)
- [443: What should you check when reviewing scheduled background jobs?](#443-what-should-you-check-when-reviewing-scheduled-background-jobs)
- [444: What does fail open vs fail closed mean, and why should reviewers care?](#444-what-does-fail-open-vs-fail-closed-mean-and-why-should-reviewers-care)
- [445: Why should reviewers check graceful shutdown in services?](#445-why-should-reviewers-check-graceful-shutdown-in-services)
- [446: Why can changes to TypeScript types in a published package be breaking?](#446-why-can-changes-to-typescript-types-in-a-published-package-be-breaking)
- [447: Why should reviewers watch for copied code and licenses?](#447-why-should-reviewers-watch-for-copied-code-and-licenses)
- [448: What do interviewers want to hear when they ask about your code review experience?](#448-what-do-interviewers-want-to-hear-when-they-ask-about-your-code-review-experience)
- [449: How would you answer "Tell me about a time a code review caught a serious issue"?](#449-how-would-you-answer-tell-me-about-a-time-a-code-review-caught-a-serious-issue)
- [450: What does a healthy code review culture look like?](#450-what-does-a-healthy-code-review-culture-look-like)

---

# Easy Questions (1-150)

## 1: What is a code review?

A code review is when one or more developers read someone else's code changes before (or sometimes after) they get merged into the main codebase. The reviewer looks for bugs, unclear code, missing tests and things that don't fit the rest of the project, and leaves comments.

Today most teams do it through pull requests on GitHub, GitLab or a similar tool. The author opens the change, reviewers comment, the author updates the code, and once the reviewers are happy the change gets merged.

## 2: Why do teams do code reviews?

The main reasons are:

- **Catching problems early**: bugs, security holes and bad design are cheaper to fix before they reach production.
- **Sharing knowledge**: at least two people know how each part of the code works.
- **Keeping the code consistent**: reviewers point out when something doesn't follow the team's patterns.
- **Learning**: juniors learn from seniors' feedback, and seniors see new ideas from others.

Studies of real teams show that finding bugs is only part of the value. A lot of it comes from shared understanding of the code.

## 3: What is a pull request?

A pull request (PR) is a request to merge changes from one branch into another, usually from a feature branch into `main`. It shows the diff, the commits, a description, CI results and a place for comments.

The name comes from Git's distributed model: you ask the maintainer to "pull" your changes. On GitHub and Bitbucket it's called a pull request. GitLab calls the same thing a merge request.

## 4: What is the difference between a pull request and a merge request?

There's no real difference. They're two names for the same idea. GitHub, Bitbucket and Azure DevOps say "pull request", GitLab says "merge request". Both mean "here are my changes, please review and merge them". Gerrit uses yet another name: a "change".

## 5: Who should review code?

Usually someone who knows the area being changed, so they can spot problems that need context. It also helps to sometimes add someone who doesn't know the area well, because they'll notice when the code is hard to follow and they'll learn that part of the system.

Many teams use a `CODEOWNERS` file to automatically request reviews from the people or teams responsible for certain folders.

## 6: What does LGTM mean?

LGTM means "Looks Good To Me". Reviewers write it when they approve a change. It came from Google's internal review tool and spread from there.

A plain "LGTM" with no other comments is fine for a small, simple change. For a big change it can be a sign that the reviewer didn't really read it, which is called rubber-stamping.

## 7: What is a nit in a code review?

A nit (from "nitpick") is a small comment about something minor, like a variable name, a typo or an extra blank line. Reviewers usually prefix it with "Nit:" to say "this is small, fix it if you agree, but it doesn't block the merge".

```text
Nit: `usr` -> `user` would read a bit better here.
```

Labeling nits matters because otherwise the author can't tell which comments are important and which are just preferences.

## 8: What does a reviewer look for in a code review?

Roughly in order of importance:

1. Does the change do what it's supposed to do, and is the general approach right?
2. Are there bugs, missed edge cases or security problems?
3. Are there tests, and do they test the right things?
4. Is the code easy to read and change later?
5. Does it follow the team's conventions?

Small style issues come last. Things like formatting should be handled by tools, not people.

## 9: What is the author's job in a code review?

The author should make the change easy to review:

- Keep the PR small and focused on one thing.
- Write a clear title and description: what changed, why, and how it was tested.
- Review their own diff before asking others.
- Make sure CI passes.
- Respond to every comment, either by fixing it or by explaining why not.

The author is still responsible for the code after merge. Review is a second pair of eyes, not a transfer of responsibility.

## 10: What is the reviewer's job in a code review?

The reviewer reads the change carefully, asks questions where something is unclear, and points out problems. They should:

- Respond in a reasonable time so the author isn't blocked.
- Focus on what matters most (correctness, design, tests) before small stuff.
- Be clear about which comments must be fixed and which are optional.
- Approve once the change makes the code better, even if it isn't perfect.

## 11: What is the difference between Approve, Request changes and Comment on GitHub?

When you submit a review on GitHub you pick one of three options:

- **Comment**: general feedback without a verdict. It doesn't approve or block.
- **Approve**: you're happy for the PR to be merged.
- **Request changes**: you think something must be fixed first. If branch protection requires approvals, this blocks the merge until you approve or your review gets dismissed.

Some teams use "Request changes" only for serious problems and use "Comment" for everything else, so the red X doesn't feel harsh.

## 12: What is a diff?

A diff shows the difference between two versions of the code: which lines were removed and which were added. Code review tools show the diff of the branch compared to the target branch, so the reviewer only sees what changed.

```diff
 function total(items) {
-  return items.reduce((sum, i) => sum + i.price, 0);
+  return items.reduce((sum, i) => sum + i.price * i.quantity, 0);
 }
```

Lines starting with `-` were removed, lines with `+` were added, and lines with a space are unchanged context.

## 13: How do you read a unified diff?

A unified diff has a header with the file names, then "hunks". Each hunk starts with a line like `@@ -10,6 +10,7 @@`, meaning "starting at line 10, 6 lines in the old file became 7 lines in the new file". Below that, `-` lines are removed, `+` lines are added and the rest is context.

When a line is changed, it shows up as one removed line and one added line. Review tools usually highlight the exact characters that changed inside those lines.

## 14: What is a draft pull request?

A draft PR is a pull request that isn't ready to be merged yet. On GitHub, a draft can't be merged, and code owners aren't asked for review until it's marked "Ready for review". GitLab has the same feature (draft merge requests).

Drafts are useful when you want early feedback on an approach, want CI to run, or just want to show progress without people thinking it's ready for a full review.

## 15: What makes a good pull request title?

A good title says what the change does in a short sentence that makes sense on its own, for example "Fix rounding error in invoice totals" or "Add retry to payment webhook handler". Bad titles are things like "Fixes", "Update user.ts" or a bare ticket number.

The title often becomes the commit message when you squash merge, so it ends up in the Git history. Some teams use Conventional Commit style in titles, like `fix(invoice): round totals to two decimals`.

## 16: What makes a good pull request description?

A good description answers:

- **What** changed, in a few sentences.
- **Why** it changed: the bug, ticket or goal behind it.
- **How** to test or check it, and what you already tested.
- Anything the reviewer should look at closely, or anything left out on purpose.

For UI changes, add screenshots or a short video. Link the ticket or issue. The reviewer shouldn't have to guess the purpose of the change from the code alone.

## 17: What is a pull request template?

A PR template is a markdown file that pre-fills the description of every new PR. On GitHub you put it at `.github/pull_request_template.md` (or in a `.github/PULL_REQUEST_TEMPLATE/` folder for several templates).

```markdown
## What and why

## How to test

## Checklist

- [ ] Tests added or updated
- [ ] Docs updated if needed
- [ ] Screenshots added for UI changes
```

Templates remind authors to include the things reviewers need. Keep them short, or people will just delete them.

## 18: Why should pull requests be small?

Small PRs are easier and faster to review. Reviewers read them more carefully and find more problems. With a big PR, attention drops, and people start skimming or just approving.

Small PRs also merge faster, have fewer conflicts, and are easier to revert if something goes wrong. If a 50-line change breaks something, it's easy to find the cause. With a 2,000-line change, it's not.

## 19: How big should a pull request be?

There's no strict rule, but many teams aim for a few hundred changed lines at most. A study at Cisco (done with SmartBear) found that reviewers find fewer defects once a review goes past about 200-400 lines.

Line count isn't everything, though. A 500-line rename is easy to review, while a 50-line change to locking code can take an hour. A better rule: one PR should do one thing, and a reviewer should be able to understand it in one sitting.

## 20: What is a self-review and why should you do it?

A self-review is when the author reads their own diff in the review tool before asking anyone else. Seeing the code as a diff, instead of in the editor, makes you notice things you missed: leftover `console.log` calls, commented-out code, unrelated changes, missing tests, typos.

It takes a few minutes and saves the reviewer from pointing out obvious things. You can also leave comments on your own PR to explain tricky parts in advance.

## 21: What is a code owner?

A code owner is a person or team responsible for a part of the codebase, like a folder or a type of file. When a PR touches their files, they're automatically asked to review it. With the right branch protection, their approval is required before merging.

Code owners make sure the people who know an area see changes to it, and they make it clear who to ask.

## 22: What is a CODEOWNERS file?

`CODEOWNERS` is a file supported by GitHub and GitLab that maps file patterns to owners. On GitHub it can live in `.github/`, the repo root, or `docs/`.

```text
# Default owners for everything
*                   @acme/web-team

# Payments code
/src/payments/      @acme/payments-team

# Infra files
*.tf                @acme/platform-team
```

On GitHub, the last matching pattern wins, so put the general rules at the top and more specific ones below.

## 23: What is branch protection?

Branch protection is a set of rules on important branches like `main`. Common rules:

- Changes must go through a pull request (no direct pushes).
- A minimum number of approvals is required.
- Certain CI checks must pass.
- Code owner approval is required for owned files.
- Force pushes and branch deletion are blocked.

On GitHub you can set these as classic branch protection rules or as rulesets. They turn the team's review agreement into something the tool enforces.

## 24: What does "required approvals" mean?

It's a branch protection setting that says how many approving reviews a PR needs before it can be merged, for example one or two. The author's own approval doesn't count.

One approval is common for most teams. Two is used for sensitive code like payments, auth or infrastructure. More than two usually just slows things down without catching much more.

## 25: What is the role of CI in code review?

CI (continuous integration) runs automated checks on every PR: build, tests, linting, type checks, maybe security scans. Results show up on the PR.

This means reviewers don't have to check things a machine can check. A common rule is that reviewers don't start until CI is green, or at least that a PR can't be merged until it is. Human review then focuses on logic, design and readability.

## 26: Should reviewers comment on code formatting?

Mostly no. Formatting (indentation, quotes, line length, semicolons) should be handled by a formatter like Prettier and enforced in CI or a pre-commit hook. Then there's nothing to argue about.

If the team has no formatter, the best comment is a suggestion to add one, not a dozen comments about spaces. People's time in review is better spent on logic and design.

## 27: How does a linter help code review?

A linter like ESLint catches common mistakes and style problems automatically: unused variables, missing `await`, risky patterns, rule-of-hooks violations in React. When it runs in CI, reviewers don't need to point these out.

It also makes reviews less personal. "The linter flagged it" is easier to hear than "I don't like how you did this". If reviewers keep making the same comment, it's worth checking whether a lint rule can catch it instead.

## 28: What is a style guide and how does it relate to code review?

A style guide is a written set of rules for how code should look and be structured in a project: naming, file layout, error handling patterns, and so on. Examples are the Google style guides or a team's own short doc.

In reviews, a style guide settles arguments. Instead of "I prefer it this way", the reviewer can link to the rule. If something isn't in the guide, it's usually a personal preference and shouldn't block the PR.

## 29: What is rubber-stamping?

Rubber-stamping is approving a PR without really reviewing it, often with a quick "LGTM". It happens when reviewers are busy, the PR is too big, or they trust the author and assume it's fine.

It's a problem because the team believes the code was reviewed when it wasn't. Signs of it: big PRs approved within a minute, almost no comments ever, and bugs that a careful read would have caught.

## 30: What is bikeshedding in code reviews?

Bikeshedding (from Parkinson's "law of triviality") means spending lots of time arguing about small, easy-to-understand things while ignoring the hard, important parts. In reviews, that looks like 20 comments about naming and none about the race condition.

To avoid it, review the big things first, mark small things as nits, and let tools settle formatting and style.

## 31: How quickly should you respond to a review request?

As a rough guide, within one working day, and faster for small PRs. Google's public engineering guide says one business day is the maximum, and that it's better to respond quickly between tasks rather than interrupt deep focus work.

"Respond" doesn't always mean a full review. If you can't do it soon, say so ("I'll look at this tomorrow morning") or suggest someone else, so the author isn't left waiting with no information.

## 32: How do you write a good review comment?

A good comment is:

- **Specific**: points to the exact problem and, if possible, a fix.
- **Explained**: says why, not just what.
- **Clear about importance**: blocking or optional.
- **Polite**: about the code, not the person.

```text
This will throw if `user.address` is null, which happens for users
created before the address field existed. Could we use optional
chaining here, or filter those users out earlier?
```

Compare that with "this is wrong", which tells the author nothing.

## 33: Why should comments be about the code and not the person?

Because people get defensive when they feel attacked, and then they stop listening. "You forgot to handle errors" sounds like blame. "This call can fail and the error isn't handled" describes the code and leads to a fix.

It also builds trust. If people know reviews are about the code, they're more willing to open PRs early and ask for feedback.

## 34: Is it better to ask questions or give instructions in review comments?

Questions often work better, especially when you're not sure. "What happens here if the list is empty?" invites the author to think, and you might learn there's a reason you didn't see.

But don't hide a clear request behind a fake question. If something must change, say so directly and politely: "This needs a null check, because X can be undefined when Y." Vague questions like "Are you sure about this?" are frustrating because they don't say what's wrong.

## 35: What is a blocking comment?

A blocking comment points to something that must be fixed before the PR can be merged, like a bug, a security problem, missing tests for important logic, or a broken API contract.

Make it obvious which comments are blocking. Some teams write "Blocking:" or use the "Request changes" status. If every comment looks blocking, authors waste time on minor things or get frustrated.

## 36: What is a non-blocking comment?

A non-blocking comment is feedback the author can choose to act on or not, like a suggestion, a nit, a question for learning, or an idea for later. Common prefixes are "Nit:", "Optional:", "Suggestion (non-blocking):" or "FYI:".

Approving the PR while leaving non-blocking comments is a clear signal: "this is good to merge, these are just ideas".

## 37: Should reviewers leave positive comments?

Yes, when they mean it. A short "nice, this is much simpler than before" or "good catch on this edge case" tells the author what to keep doing. It also balances out the critical comments so reviews don't feel like a list of faults.

Don't overdo it or make it fake. One honest positive comment is worth more than "great work!!" on every line.

## 38: How should an author respond to review comments?

Reply to every comment so the reviewer knows it was seen:

- If you fixed it, say so ("Done" or "Fixed in abc123").
- If you disagree, explain why, politely.
- If you'll handle it later, link the follow-up ticket.
- If you don't understand, ask.

Don't take comments personally, and don't silently ignore them. When you push fixes, re-request review so the reviewer knows it's ready.

## 39: What should you do when you disagree with a reviewer?

First, make sure you understand their point. Ask if needed. Then explain your reasoning with facts: data, docs, an example, a test. Sometimes the reviewer is right, sometimes you are, and sometimes both ways are fine.

If the thread goes back and forth more than a couple of times, talk on a call. It's faster and less tense. If you still can't agree, ask a tech lead or a third person to decide, or follow the team's existing conventions.

## 40: Who should resolve a comment thread?

Teams differ. A common rule is that the reviewer who left the comment resolves it, because they're the one who can say whether the fix is good. Another common rule is that the author resolves simple ones (like a typo fix) and leaves bigger discussions for the reviewer.

What matters is that the team agrees on one rule. GitHub has a branch protection option that requires all conversations to be resolved before merging.

## 41: What are suggested changes on GitHub?

A suggested change is a review comment that contains the exact code the reviewer proposes. The author can apply it with one click, and it becomes a commit.

````markdown
```suggestion
const total = items.reduce((sum, item) => sum + item.price, 0);
```
````

It's great for small, clear fixes like typos and renames. For bigger changes it's better to describe the idea and let the author write the code.

## 42: What is a review round?

A review round is one cycle of: reviewer leaves comments, author makes changes, reviewer looks again. Small, clear PRs often need one round. Big or unclear ones can take five or more, and each round adds waiting time.

To keep rounds low, write a good description, self-review first, and try to give all your important feedback in the first round instead of adding new concerns each time.

## 43: What does it mean to re-request a review?

After the author addresses comments, they can click "Re-request review" on GitHub (the circular arrow next to the reviewer's name). This notifies the reviewer that the PR is ready for another look.

Without it, reviewers often don't know when the author is done pushing fixes. Some teams also leave a short comment summarizing what changed since the last review.

## 44: What is an over-the-shoulder review?

It's when the author walks the reviewer through the code in person or on a screen share. The reviewer asks questions as they go.

It's fast and good for learning, but the author controls the pace, so the reviewer may miss things. There's also usually no written record. It works well for complicated changes, as a complement to a written review.

## 45: Is pair programming a kind of code review?

In a way, yes. When two people write code together, the second person is reviewing every line as it's written. Some teams that pair a lot skip or shorten the later PR review for that work.

The downside is that both people share the same assumptions by the end, so a fresh reviewer may still catch things they both missed.

## 46: What is a tool-based code review?

It's review done through a tool like GitHub, GitLab, Bitbucket, Azure DevOps or Gerrit. The tool shows the diff, lets reviewers comment on specific lines, tracks approval status and connects to CI.

This is the standard way most teams review today. Its strengths are that it works across time zones, leaves a written history, and can be enforced with branch rules.

## 47: How does email-based code review work?

The author sends patches as emails, often made with `git format-patch` and sent with `git send-email`. Reviewers reply inline, quoting the parts they comment on. The Linux kernel and Git itself still work this way.

It works without any special tool and fits big distributed projects, but it's harder for newcomers, and tracking which version of a patch is the latest takes discipline.

## 48: What is a formal code inspection?

A formal inspection, also called a Fagan inspection after Michael Fagan who described it at IBM in the 1970s, is a structured meeting-based review. People have set roles (moderator, reader, recorder, author), prepare beforehand with checklists, and log defects.

It finds a lot of defects but is slow and expensive. Most teams today use lighter, tool-based reviews instead, but the formal style is still used in some safety-critical industries.

## 49: What is the difference between pre-commit and post-commit review?

- **Pre-commit (pre-merge) review**: code is reviewed before it's merged into the main branch. This is the usual pull request flow.
- **Post-commit (post-merge) review**: code is merged first and reviewed afterwards. Problems are fixed with follow-up changes.

Pre-merge catches problems before they hit `main`. Post-merge is faster and is sometimes used for trusted people, small changes or emergencies, but needs a reliable way to make sure the review actually happens.

## 50: What is a merge conflict and who should fix it?

A merge conflict happens when the PR branch and the target branch changed the same lines differently, and Git can't combine them on its own.

Usually the PR author fixes it, by merging or rebasing the latest `main` into their branch and choosing the right code. If the conflict resolution changes logic, the reviewer should look at it again, because a bad resolution can quietly break things.

## 51: What does "ship it" mean in a code review?

"Ship it" is another way of saying the change is approved and ready to merge and deploy. Some tools even had a "Ship It!" button (Review Board, for example). It means the same as LGTM, maybe with a bit more confidence.

## 52: Should junior developers review senior developers' code?

Yes. Juniors learn a lot by reading code from more experienced people, and they often catch real problems because they read slowly and ask "why?". If a junior doesn't understand the code, that's useful feedback too: the code may be harder to follow than the senior thinks.

For risky changes, a senior reviewer should also look, but a junior reviewer is still a good second person.

## 53: What can you learn by reviewing other people's code?

- How other parts of the system work.
- New language features, libraries and patterns.
- Different ways to solve the same problem.
- Common mistakes, so you avoid them yourself.
- How to explain things clearly in writing.

Many developers say reviewing taught them as much as writing code did.

## 54: How does code review help spread knowledge in a team?

Each review means at least one more person has seen how a change works and why it was made. Over time, more people know each part of the codebase, so fewer things depend on a single person.

The written review threads also stay in the tool. Months later, someone can find the PR through `git blame` and read the discussion behind a strange-looking line.

## 55: What is the bus factor and how does code review affect it?

The bus factor is the number of people who would have to leave (or "get hit by a bus") before a project gets stuck because nobody knows how things work. A bus factor of 1 is risky.

Code review raises the bus factor because reviewers learn the code they review. Rotating reviewers, instead of always asking the same person, helps even more.

## 56: What is a code review checklist?

A checklist is a short list of things a reviewer should check on every PR, for example:

- Does it do what the ticket asks?
- Are errors handled?
- Are there tests for the new behavior?
- Any secrets, debug code or commented-out code left?
- Is user input validated?

Checklists help new reviewers and stop people from forgetting important checks. Keep them short; a 50-item checklist won't be used.

## 57: How do you check the correctness of a change during review?

Read the description and ticket so you know what the code should do. Then follow the logic and ask: what happens with empty input, null, very large values, errors from other services, or two requests at the same time? Check that the tests cover these cases.

For anything non-trivial, try running it locally or on a preview environment. Reading code alone often misses problems that show up the moment you click a button.

## 58: How do you check readability during a review?

Ask yourself whether you understand the code on the first read. If you had to read a function three times, that's worth a comment. Look at:

- Names: do they say what things are?
- Function length and nesting depth.
- Clever one-liners that could be simpler.
- Comments: do they explain the "why" where it's not obvious?

You're a good stand-in for the next developer who reads this code. If it's hard for you, it'll be hard for them.

## 59: How should you give feedback on naming?

Explain what's confusing and suggest a better name:

```text
`data` doesn't tell me what this holds. Since it's the list of unpaid
invoices, maybe `unpaidInvoices`?
```

Naming is partly taste, so if the current name is fine and yours is just a bit different, mark it as a nit or skip it. Push harder when a name is misleading, like a function called `getUser` that also updates the database.

## 60: Should every pull request include tests?

Most PRs that change behavior should include tests, especially bug fixes (a test that fails before the fix and passes after) and new features. That's the only way to be sure the behavior stays correct later.

Some PRs don't need new tests: docs changes, config tweaks, pure renames, or trivial UI copy. If a PR has no tests, the reviewer should ask why, and the reason should be good.

## 61: How do you review tests in a pull request?

Check that the tests:

- Cover the new behavior and the important edge cases, not just the happy path.
- Would actually fail if the code were broken.
- Have clear names that describe the behavior.
- Don't depend on each other, on time, or on test order.
- Aren't mocking so much that they only test the mocks.

Read the tests first sometimes. They often explain what the code is supposed to do better than the code itself.

## 62: What should you check about error handling in a review?

Look for:

- Calls that can fail (network, database, file system, parsing) with no handling.
- Empty `catch` blocks that hide errors.
- Errors logged but then ignored when the code should stop.
- Error messages shown to users that leak internal details.
- Missing `await`, so the error isn't caught at all.

```ts
try {
  await saveOrder(order);
} catch {
  // Swallowed: the user thinks the order was saved
}
```

A good question to ask: "What does the user see if this fails?"

## 63: What should you do when you spot duplicated code in a PR?

Point out where the same logic already exists and ask if the author can reuse it. Often they just didn't know about the existing helper.

Don't push too hard for removing every bit of duplication, though. Two pieces of code that look the same but change for different reasons are sometimes better left separate. The question is whether a future change to one should also change the other.

## 64: Why is commented-out code a problem in a PR?

Commented-out code confuses readers. Is it needed? Is it coming back? Should someone delete it? It also goes stale quickly, because nobody updates it when the code around it changes.

Git already keeps the old code in history. The usual review comment is: "Can we delete this? It's in Git history if we need it."

## 65: What debug leftovers should reviewers look for?

- `console.log`, `print` and `debugger` statements.
- Hard-coded test values, like a fixed user ID or `if (true)`.
- Lowered timeouts or disabled checks used during testing.
- `.only` or `.skip` in tests (`it.only`, `describe.skip`).
- Local file paths or URLs pointing to `localhost`.

Many of these can be caught by lint rules (like `no-console`, `no-debugger`) or by test runners that fail on `.only` in CI.

## 66: Is it OK to have TODO comments in a pull request?

Sometimes. A TODO that explains a known limitation and links to a ticket is fine:

```ts
// TODO(PAY-412): support partial refunds once the provider API allows it
```

A bare "TODO: fix this" with no ticket usually never gets done. Reviewers should ask for a ticket or ask whether the thing should just be done now.

## 67: What should you check in code comments during a review?

- Comments that explain why, not what the code obviously does.
- Comments that no longer match the code after the change.
- Public functions and APIs that need doc comments.
- Comments that hide a problem the code should fix instead, like "don't call this twice".

Outdated comments are worse than no comments, because people trust them.

## 68: Why do reviewers ask to replace magic numbers?

A magic number is a raw number in the code with no explanation, like `if (retries > 3)` or `setTimeout(fn, 86400000)`. Readers don't know what it means or whether it's safe to change.

```ts
const ONE_DAY_MS = 24 * 60 * 60 * 1000;
setTimeout(cleanup, ONE_DAY_MS);
```

A named constant explains the meaning and keeps the value in one place.

## 69: What should you do if you see a hard-coded secret in a PR?

Treat it as leaked, even if the PR isn't merged. Anyone with access to the repo (and in public repos, everyone) can see the commit. Tell the author right away, and ask for the secret to be rotated (revoked and replaced), not just removed from the code.

Removing it in a new commit doesn't help, because it's still in Git history. Secret scanning tools like GitHub secret scanning can catch many of these automatically.

## 70: Why should reviewers sometimes run the code instead of just reading it?

Reading a diff shows you the code but not how it behaves. Running it can show broken UI, slow pages, confusing flows, missing loading states and bugs that tests didn't cover.

You don't need to run every PR. It's most useful for UI changes, complex logic, and anything the author wasn't able to test well. Preview deployments make this much easier.

## 71: How do you check out a pull request locally?

With the GitHub CLI:

```bash
gh pr checkout 123
```

Without it, you can fetch the PR's branch directly:

```bash
git fetch origin pull/123/head:pr-123
git switch pr-123
```

Then install, build and run it as usual. When you're done, switch back to your own branch.

## 72: What are preview deployments and how do they help code review?

A preview deployment is a temporary environment built for a single PR, with its own URL. Platforms like Vercel and Netlify do this automatically for front-end projects, and many teams set it up for full stack apps too.

Reviewers, designers and product people can click through the change without setting anything up locally. It catches visual and flow problems that are hard to see in a diff.

## 73: Why should UI pull requests include screenshots?

Screenshots (or short videos) show the reviewer what the change looks like without running it. Before/after images make it easy to spot unexpected changes.

Good UI PRs show different states: loading, empty, error, mobile and desktop, and maybe dark mode. Designers can also review the PR without reading code.

## 74: What is a stale approval?

A stale approval is an approval given on an older version of the PR. If the author pushes new commits after approval, the reviewer hasn't seen those changes.

GitHub has a branch protection setting, "Dismiss stale pull request approvals when new commits are pushed", that removes approvals automatically when new code is pushed. Without it, someone could get approval and then push something very different.

## 75: Why should you link issues or tickets to a pull request?

Linking gives the reviewer context: what problem this solves and what the requirements are. It also connects code to decisions, so later someone can see why the change was made.

On GitHub, writing "Fixes #123" or "Closes #123" in the description links the issue and closes it automatically when the PR is merged into the default branch. Jira and Linear can link through the branch name or PR title.

## 76: Why do commit messages matter in code review?

Commit messages explain why a change was made, and they stay in the Git history long after the PR page is forgotten. Reviewers who read commit by commit use them to follow the author's steps.

A good commit message has a short summary line and, when needed, a body that explains the reason. "fix" or "wip" tells nobody anything. If the team squash merges, the PR title and description become the important message instead.

## 77: What are Conventional Commits?

Conventional Commits is a convention for commit messages in the form `type(scope): description`, for example:

```text
feat(auth): add password reset by email
fix(cart): prevent negative quantities
docs: update setup instructions
```

Common types are `feat`, `fix`, `docs`, `refactor`, `test` and `chore`. A `!` or a `BREAKING CHANGE:` footer marks breaking changes. It makes history easy to scan and lets tools generate changelogs and version numbers.

## 78: What is an atomic commit?

An atomic commit does one logical thing and leaves the code in a working state. For example, one commit renames a function, and another commit adds a feature using it.

Atomic commits make review easier because each commit is a small, understandable step. They also make `git revert` and `git bisect` much more useful.

## 79: What is the difference between squash, merge commit and rebase merging?

- **Merge commit**: keeps all the PR's commits and adds a merge commit. Full history, but noisier.
- **Squash and merge**: combines all commits into one commit on `main`. Clean history, one commit per PR.
- **Rebase and merge**: replays each commit on top of `main` without a merge commit. Linear history that keeps individual commits.

Many teams use squash merge because PR branches often have messy commits like "fix typo" and "address review".

## 80: Is it OK to force-push during a code review?

It depends on the team. Force-pushing (after a rebase or amend) rewrites the branch, which can make it hard for reviewers to see what changed since their last review, and comments on old lines may become outdated.

Many teams prefer adding new commits while the review is going on and cleaning up history at the end (or squash merging). Others use force-push with tools that show changes between versions. If you force-push, use `--force-with-lease` so you don't overwrite someone else's pushes.

## 81: What does WIP mean on a pull request?

WIP means "work in progress". Before draft PRs existed, people added "WIP" to the title to say "don't merge this yet". Now draft PRs do the same job and the tool actually blocks merging.

If you see a WIP PR, don't give a full detailed review unless asked. The author probably wants early feedback on the direction only.

## 82: How many reviewers does a pull request need?

Usually one good reviewer is enough for normal changes. Two can make sense for risky areas like security, payments, data migrations or shared libraries.

More reviewers isn't always better. With many reviewers, each one tends to assume someone else checked carefully, so the review can get worse, not better. It also adds waiting time.

## 83: How do teams assign reviewers?

Common ways:

- The author picks someone who knows the area.
- `CODEOWNERS` assigns owners automatically.
- Round-robin or load-balanced assignment (GitHub team review assignment supports both).
- A "reviewer of the day" rotation.

Automatic assignment spreads the work and the knowledge. Letting authors always pick the same friendly reviewer leads to knowledge silos and burned-out reviewers.

## 84: What is a review queue?

A review queue is the list of PRs waiting for someone's review. On GitHub, you can see PRs where your review is requested with the search filter `review-requested:@me`, or with `gh pr list --search "review-requested:@me"`.

Checking your queue a couple of times a day (for example after standup and after lunch) is an easy way to keep reviews moving without constant interruptions.

## 85: Why not just rely on automated tests and skip code review?

Tests only check what someone thought to test. They can't tell you that the design will be hard to change, that a name is misleading, that the feature solves the wrong problem, or that a security check is missing in a code path nobody tested.

Code review and tests catch different kinds of problems. Review also does things tests can't, like sharing knowledge and keeping the codebase consistent.

## 86: What kinds of problems does code review usually miss?

- Problems that only show up under real load or real data.
- Bugs in code that wasn't changed but is affected by the change.
- Integration issues between services.
- Subtle concurrency bugs.
- Anything in a huge PR, because attention drops.

That's why review is one layer among several: tests, static analysis, monitoring, staged rollouts and so on.

## 87: Does a hotfix need a code review?

Ideally yes, even if it's a fast one. Hotfixes are written under pressure, which is when mistakes happen, and a broken hotfix can make an incident worse. A quick review from one person on a call is usually possible.

If there truly is no reviewer available, many teams allow an emergency bypass but require a review right after the fix is deployed. The bypass should be logged so it doesn't become a habit.

## 88: Should you review code from other teams?

When their change touches your code or something you depend on, yes. That's what code owners are for. You know how your part of the system is used and what can break.

When reviewing another team's code, focus on how it affects your area. Leave their internal style choices to them unless something is clearly wrong.

## 89: Who should merge the pull request?

Teams use different rules:

- **The author merges** after approval. This is the most common, because the author knows when the change is ready and can watch the deploy.
- **The reviewer merges** after approving, so nothing changes after review.
- **A merge queue or bot merges** when all checks and approvals are in.

Whoever merges should make sure CI is green and nothing new was pushed without review.

## 90: What should happen after a pull request is approved?

The author checks that CI is green, the branch is up to date if required, and any small follow-up comments are handled. Then they merge, often with squash merge. After merging, the author should watch the deploy and check logs or metrics if the change is risky.

Any follow-up work promised during review should be in tickets, not just in comments that will be forgotten.

## 91: What should you do if your pull request has been waiting for review too long?

First, check that it's actually reviewable: CI passing, clear description, not too big. Then ping the reviewer politely, preferably in the team's channel or directly:

```text
Hi! Could you take a look at #482 when you get a chance? It's small
(about 80 lines) and blocks the release on Thursday.
```

If someone is on vacation or overloaded, ask for a different reviewer. Bring it up in standup if it keeps happening.

## 92: What is a stale pull request?

A stale PR has been open for a long time without activity. The branch falls behind `main`, conflicts grow and people forget the context.

Teams should regularly close or finish stale PRs. GitHub's `actions/stale` action can label and close inactive PRs automatically. Long-lived PRs are often a sign that the PR was too big or the work wasn't prioritized.

## 93: How should you review documentation changes?

Check that the docs are correct (try the commands or steps if you can), easy to follow, and up to date with the code. Look for broken links, outdated screenshots, and missing steps a new person would need.

Docs PRs should still be reviewed, but the bar for merging can be lower. Merging a better-but-not-perfect doc is usually better than leaving it in review for a week.

## 94: How should you review configuration changes?

Configuration changes (environment variables, feature flags, YAML, JSON settings) can break production as easily as code, and often have no tests. Check:

- Is the value correct for each environment?
- Is anything missing, like a new variable that isn't set in production?
- Are secrets kept out of the repo?
- Can it be rolled back easily?

Ask how the config change was tested, because "it's just config" is often how outages start.

## 95: What should you check when a pull request adds a new dependency?

- Do we really need it, or does the language or an existing package already do this?
- Is it maintained, popular enough and properly licensed?
- How big is it, especially for front-end bundles?
- Does it have known security issues?
- Are there install scripts or many transitive dependencies?

Adding a dependency is a long-term commitment, so it deserves a bit more thought than most lines of code.

## 96: Should you review lockfile changes?

You don't need to read every line of a `package-lock.json` or `pnpm-lock.yaml`, but you should check that the lockfile changed only when it should have. If the PR doesn't touch dependencies but the lockfile has thousands of changed lines, something is off (wrong package manager version, accidental upgrade).

For dependency changes, skim which packages and versions changed. Tools like GitHub's dependency review can show this in a readable way and flag known vulnerabilities.

## 97: How should generated files be handled in pull requests?

Generated files (lockfiles, compiled output, generated API clients, snapshots) make diffs noisy. Options:

- Don't commit them if they can be built in CI.
- Mark them as generated in `.gitattributes` with `linguist-generated=true`, so GitHub collapses them in the diff by default.
- Review the source (the schema or config) instead of the output.

Reviewers should skim generated output only to check that it changed in the expected way.

## 98: How do you review whitespace-only changes?

Turn on "Hide whitespace" in the diff view (on GitHub it's in the diff settings, or add `?w=1` to the PR files URL). Locally, `git diff -w` ignores whitespace.

This lets you see the real changes when someone re-indented a block. Better still, ask authors to keep formatting changes in a separate PR or commit, so the real changes aren't buried.

## 99: How do diffs show renamed or moved files?

Git detects renames by comparing file content. If a file was moved with few changes, the diff shows it as a rename with only the changed lines. If the file changed a lot during the move, Git may show it as one file deleted and another added, which is hard to review.

Tip for authors: move or rename files in one commit, and make content changes in a separate commit. That keeps the rename clean and the real changes visible.

## 100: What is the "Viewed" checkbox on GitHub?

In the "Files changed" tab, each file has a "Viewed" checkbox. When you tick it, the file collapses and GitHub tracks it as reviewed. If the author later changes that file, GitHub un-ticks it so you know to look again.

It's handy for large PRs reviewed in several sittings: you can see what you've already covered and what's new.

## 101: Is it OK to review a large pull request in several sessions?

Yes, and it's usually better. Attention drops after about an hour of reviewing, and you start skimming. Breaking the review into chunks (for example, backend files in one session, frontend in another) keeps you focused.

Use "Viewed" checkboxes or pending review comments to keep track. If you submit partial feedback, say so: "Reviewed the API part, will look at the UI after lunch."

## 102: How long should one review session last?

Many teams aim for under an hour per session. The Cisco/SmartBear study suggested that reviewers become much less effective after about 60-90 minutes, and that going too fast (several hundred lines per hour or more) also lowers the number of problems found.

If a PR needs more than that, it's probably too big, or it's worth taking a break and continuing later.

## 103: How do you start reviewing a pull request?

A simple order:

1. Read the title, description and linked ticket. Understand the goal.
2. Look at the list of changed files to get the shape of the change.
3. Find the main file or entry point and start there, not with whatever file is listed first alphabetically.
4. Read the tests to see the expected behavior.
5. Go through the rest of the files.
6. Run it if needed, then write your summary.

Starting with the "why" makes the "how" much easier to judge.

## 104: Why should reviewers read the description before the code?

Without context, you can't tell if the code does the right thing, only whether it does something. The description tells you what problem is being solved, what was intentionally left out, and where the author wants attention.

If the description is empty or unclear, the first comment should be to ask for one. That's usually faster than guessing.

## 105: What does "context" mean in a code review?

Context is the background a reviewer needs to judge the change: the requirements, the reason for the approach, related PRs, constraints like deadlines or legacy systems, and how the code is used elsewhere.

Review tools only show a few lines around each change. Reviewers often need to open the full file or search the codebase to understand the effect of a change. Expanding the diff context or checking out the branch helps.

## 106: Why should review comments explain the "why"?

Without a reason, a comment feels like an order, and the author can't learn from it or judge whether it applies elsewhere.

```text
Bad:  Use a Map here.
Good: A Map would make this lookup O(1) instead of scanning the array
      on each render. With ~5k products that's noticeable.
```

Explaining also forces you to check your own reasoning. Sometimes you realize while writing it that the comment isn't needed.

## 107: Should you write "we" or "you" in review comments?

Many people prefer "we" or neutral wording because it sounds like a team effort: "Can we add a test for the empty case?" instead of "You didn't test the empty case."

It's not a strict rule. "You" is fine in friendly sentences like "Nice, you found a much simpler way here." The goal is that the comment is about the code and the shared result, not about blaming one person.

## 108: Do emoji and tone matter in written reviews?

Yes. Written text loses tone of voice, so short comments can sound harsher than intended. "Why?" can read as annoyed even if you're just curious.

Adding a few words helps: "Curious why we need this check? I might be missing something." Some teams use emoji to mark the type of comment or soften it. Use whatever fits the team, as long as the meaning stays clear.

## 109: Should reviewers point out typos?

Yes, but as nits. Typos in user-facing text, error messages, public APIs and docs matter more than typos in a local variable name. A GitHub suggested change makes fixing them a one-click job.

A spell checker extension in the editor or a CI spell check tool like cspell can catch most of these before review.

## 110: What accessibility checks should reviewers do on UI changes?

Basic checks:

- Images have meaningful `alt` text (or empty `alt` if decorative).
- Buttons are `<button>`, links are `<a>`, not clickable `div`s.
- Form inputs have labels.
- The feature works with the keyboard only.
- Color contrast is enough, and color isn't the only way information is shown.

Tools like eslint-plugin-jsx-a11y and axe can catch some of this automatically, but a quick keyboard test during review catches a lot more.

## 111: What should you check for internationalization in a review?

If the app supports several languages, check that new user-facing text goes through the translation system instead of being hard-coded:

```tsx
// Hard-coded
<button>Save changes</button>

// Translated (react-i18next style)
<button>{t("settings.save")}</button>
```

Also check that dates, numbers and currencies are formatted with locale-aware APIs like `Intl.DateTimeFormat` and `Intl.NumberFormat`, and that the layout won't break with longer text.

## 112: What should you check about logging in a review?

- Is there enough logging to debug the feature in production?
- Is there too much, like logging inside a tight loop?
- Are log levels right (error vs warn vs info vs debug)?
- Are secrets, tokens or personal data being logged?
- Do logs include useful context like request ID or user ID?

Logs are often only looked at during an incident, so it's worth asking: "If this fails at 3 AM, will the logs tell us why?"

## 113: Why should reviewers check input validation?

Any data coming from outside (request bodies, query params, headers, files, third-party APIs) can be wrong or malicious. Missing validation leads to crashes, bad data in the database and security holes.

```ts
import { z } from "zod";

const CreateUser = z.object({
  email: z.string().email(),
  age: z.number().int().min(13),
});

const input = CreateUser.parse(req.body);
```

Check that validation happens on the server, not only in the browser form.

## 114: What does "approve with comments" mean?

It means the reviewer approves the PR but also leaves some comments, usually small suggestions or nits. The author can address them or not, then merge without another review round.

It shows trust and saves a round trip. It works well when the remaining comments are small. If a comment is important, don't approve yet.

## 115: What is a code review guidelines document?

It's a short team document that explains how reviews work in that team: expected response time, PR size, how to mark nits, who approves what, when to use "Request changes", and how to handle disagreements.

Google's engineering practices guide (public on GitHub) is a well-known example many teams borrow from. Having it written down means new people learn the rules quickly and arguments about process can point to something agreed.

## 116: Why should a team agree on code review rules?

Without agreement, each reviewer has their own standard. One approves everything, another blocks over naming, and authors don't know what to expect. That leads to frustration and inconsistent code.

A few shared rules (review time, PR size, what's blocking, who merges) remove a lot of friction. Revisit them now and then, because what works for 4 people won't work for 40.

## 117: Do code reviews slow teams down?

They add some time to each change, and slow reviews can really hurt: PRs pile up, people switch context and branches drift. But skipping review often costs more later, in bugs, outages and code nobody else understands.

The goal is fast reviews, not no reviews. Small PRs, quick response times and automation keep review from becoming a bottleneck.

## 118: Is code review only about finding bugs?

No. Finding bugs is one goal, but research at Microsoft (Bacchelli and Bird, 2013) found that developers expected reviews to find defects, while a lot of the actual value came from knowledge transfer, team awareness and finding better solutions.

Reviews also keep the codebase consistent, spread ownership, and help new people learn how the team works.

## 119: How can code review be used for mentoring?

Reviewers can explain the reasoning behind their comments, link to docs or good examples in the codebase, and ask questions that lead the author to the answer instead of just giving it.

```text
This works. One thing to look at: the `orders` service already has a
`withRetry` helper (src/lib/retry.ts). Could it replace the loop here?
```

Mentoring comments take a bit more time but pay off quickly, because the same mistake doesn't come back.

## 120: What should a new hire focus on in their first code reviews?

As an author: keep PRs small, write clear descriptions, ask questions, and don't take comments personally. Every comment is a chance to learn how the team works.

As a reviewer: start by reviewing to learn. Ask questions about things you don't understand. Point out anything confusing, because a fresh view on the code is useful. You don't need to be an expert to leave helpful comments.

## 121: How do you review code in a language you don't know well?

You can still check a lot: does the logic make sense, are names clear, are errors handled, are there tests, does it match the description? Questions are fine: "I'm not familiar with Go's channels, does this close properly if the context is cancelled?"

Be honest that you're not an expert in the language, and for risky changes, ask that someone who is also reviews it.

## 122: Is it OK for a reviewer to say "I don't know"?

Yes. It's better than pretending. "I'm not sure this is safe with concurrent requests. Can someone who knows the cache layer look?" helps the team. A fake confident approval doesn't.

Saying "I don't understand this part" is also useful feedback. If an experienced reviewer can't follow the code, others probably won't either.

## 123: How should you ask someone to review your pull request?

Make it easy for them to say yes:

- Include the link, size and urgency.
- Say what kind of review you want (full review, just the approach, just the SQL).
- Mention anything tricky.

```text
Could you review #317? About 150 lines, adds rate limiting to the
login endpoint. Main thing I'd like eyes on is the Redis key expiry.
Not urgent, sometime this week is fine.
```

## 124: How do you politely remind a reviewer about your pull request?

Wait a reasonable time (usually a day for normal PRs), then send a short, friendly message with the link and any deadline. Don't send several pings in a few hours.

If the reviewer is busy, ask whether someone else can take it. Keep it neutral: "Hi, just checking if you'll have time for #317 today, otherwise I can ask Sam."

## 125: When should you talk in person instead of commenting?

- When a comment thread goes back and forth more than two or three times.
- When the feedback is about the whole approach, not a few lines.
- When the topic is sensitive or the author seems upset.
- When it would take a long comment to explain something a 5-minute call could cover.

After the call, write a short summary in the PR so others know what was decided.

## 126: How is reviewing a refactor different from reviewing a feature?

A refactor should not change behavior. The main question is "does everything still work the same way?", so you check that existing tests cover the code and still pass without changes to what they assert.

A feature adds behavior, so you check requirements, edge cases and new tests. Mixing a refactor and a feature in one PR makes both hard to review. Ask for them to be split.

## 127: What is scope creep in a pull request?

Scope creep is when a PR grows to include unrelated changes: a feature plus some refactoring plus a library upgrade plus formatting fixes. Each extra change makes the PR harder to review and riskier to merge.

Reviewers can ask to move unrelated parts into separate PRs. Authors should resist the urge to "just fix this too while I'm here", unless it's tiny and clearly related.

## 128: Should reviewers ask for "while you're here" changes?

Be careful with it. Asking the author to fix nearby unrelated problems makes the PR bigger and delays the actual change. It's fine for small, related things, like fixing a typo in the function being changed.

For bigger things, open a ticket instead, or ask the author if they'd like to do it in a follow-up PR.

## 129: What are follow-up tickets in code review?

When a reviewer raises a valid point that's out of scope for this PR, the author creates a ticket to handle it later and links it in the comment. That way the PR can merge, and the idea isn't lost.

The risk is that follow-ups never get done. Teams should actually schedule them, or the "follow-up" becomes a polite way to ignore feedback.

## 130: Is it OK to approve code you don't fully understand?

Generally no. Your approval tells the team "I checked this". If you don't understand part of it, say which part, ask questions, or ask someone else to review that part.

You can approve the parts you understand and be explicit about the rest: "Frontend looks good to me. I didn't review the Terraform changes, someone from platform should."

## 131: Can you review only part of a pull request?

Yes, if you say so clearly. In big PRs that touch several areas, different reviewers often cover different parts. For example, a backend developer reviews the API and a designer reviews the UI.

The risk is that each reviewer assumes someone else checked the rest. Make it explicit who covers what, and use CODEOWNERS to make sure every area gets its owner's approval.

## 132: What should you check when a pull request changes UI text?

- Spelling, grammar and tone matching the rest of the product.
- Whether the text is clear to a user, not just to developers.
- Error messages that tell users what to do next.
- Text going through the translation system.
- Whether product or UX writers need to sign off.

Small wording changes can matter a lot to users, so it's often worth asking someone from product or design to look.

## 133: What should you check in CSS changes during a review?

- Does it work on small screens and different browsers?
- Are new styles scoped properly, or could they affect other pages?
- Are hard-coded values used where design tokens or variables exist?
- Is there a `!important` or very specific selector that will be hard to override later?
- Are `z-index` values picked sensibly?

Screenshots or a preview link make CSS reviews much easier than reading the diff alone.

## 134: What should you check in SQL queries during a review?

- Is user input passed as parameters, not concatenated into the string?
- Will the query use an index, or scan a big table?
- Does it select only the columns it needs?
- Are `NULL` cases handled correctly?
- For updates and deletes, is the `WHERE` clause correct?

```ts
// Unsafe
db.query(`SELECT * FROM users WHERE email = '${email}'`);

// Safe
db.query("SELECT id, name FROM users WHERE email = $1", [email]);
```

## 135: How do you spot a breaking API change in a review?

A breaking change is anything that can make existing clients fail:

- Removing or renaming a field or endpoint.
- Changing a field's type.
- Making an optional request field required.
- Changing status codes or error formats.
- Changing default behavior.

Ask: who uses this API, and will their current code still work after this is deployed? If not, the change needs a versioning or migration plan.

## 136: What does backward compatibility mean in a review?

It means the new code still works with old clients, old data and old configuration. Examples: the mobile app version from six months ago can still call the API, old database rows still load, old messages in a queue can still be processed.

Reviewers should think about the time when both old and new versions run at the same time, which always happens during a deploy.

## 137: How do feature flags affect code review?

Feature flags let unfinished or risky code be merged but turned off. This allows smaller PRs and safer releases.

Reviewers should check that the flag is off by default where expected, that both the on and off paths work and are tested, and that there's a plan to remove the flag later. Old flags left in the code become confusing dead branches.

## 138: When should you revert a merged pull request?

Revert when a merged change causes a serious problem in production and a fix isn't quick and obvious. Reverting is usually faster and safer than debugging under pressure.

```bash
git revert <commit-sha>
```

On GitHub, a merged PR has a "Revert" button that creates a revert PR. Reverting isn't a punishment. The author can fix the problem calmly and open a new PR.

## 139: What is a blameless review culture?

It means that when bugs slip through, the team looks at what in the process allowed it (missing tests, PR too big, unclear requirements) instead of blaming the author or the reviewer.

People in a blameless culture are more willing to open PRs early, admit mistakes and ask for help. In a blaming culture, people hide things, which leads to more bugs, not fewer.

## 140: What does "you are not your code" mean?

It means criticism of your code isn't criticism of you as a person or as a developer. Everyone writes code with problems, and review exists to find them.

It applies to reviewers too: don't treat your comments as a test of how smart you are, and don't get upset if the author doesn't take every suggestion. The goal is good code, not winning.

## 141: Should authors thank reviewers?

A short thank-you is nice, especially when a reviewer found a real bug or spent a lot of time on a big PR. "Good catch, thanks!" costs nothing and makes reviewing feel less like a chore.

You don't need to thank every single comment, though. Fixing the issue and replying "Done" is enough most of the time.

## 142: What are status checks on a pull request?

Status checks are the results of automated jobs (CI build, tests, linting, security scans, deploy previews) shown on the PR. Each one passes, fails or is pending.

Reviewers can see at a glance whether the code builds and tests pass. Failing checks are often the first thing to fix before asking for a human review.

## 143: What is a required status check?

A required status check is a check that must pass before the PR can be merged. It's set in branch protection or rulesets. For example, you can require the `test` and `lint` jobs to succeed.

This makes sure no one merges broken code by accident or by ignoring a red X. Choose required checks carefully: a flaky required check blocks everyone.

## 144: How is code review different in open source projects?

In open source, contributors are often strangers, so maintainers need to check more carefully for quality, security and fit with the project's direction. Maintainers are also usually volunteers with limited time, so reviews can take a while.

Contributors should read the `CONTRIBUTING.md` file, keep PRs small, discuss bigger changes in an issue first, and be patient. Maintainers should be kind, especially to first-time contributors.

## 145: What are a CLA and a DCO?

Both are ways for open source projects to make sure contributors have the right to submit their code:

- **CLA (Contributor License Agreement)**: a legal agreement the contributor signs once, often checked by a bot on the PR.
- **DCO (Developer Certificate of Origin)**: a lighter statement the contributor agrees to by adding a `Signed-off-by:` line to each commit, usually with `git commit -s`.

Reviewers usually don't check these by hand. A bot blocks the PR if they're missing.

## 146: What makes someone a good code reviewer?

- They respond quickly and don't leave people waiting.
- They focus on important issues and don't drown authors in nits.
- They explain their reasoning and are clear about what's blocking.
- They're kind and assume good intent.
- They approve when the code is good enough, not only when it matches their own style.
- They keep learning from the code they review.

## 147: What makes an author easy to review?

- Small, focused PRs.
- A clear description with context and testing notes.
- Self-reviewed code with CI passing.
- Quick, open responses to comments.
- Comments on their own PR to explain tricky parts.

Reviewers tend to review these PRs faster and more carefully, which helps the author too.

## 148: What are common mistakes new reviewers make?

- Commenting only on style and missing logic problems.
- Not saying which comments are blocking.
- Being too harsh, or too afraid to comment at all.
- Approving without really reading, to be nice.
- Asking for changes based on personal taste.
- Reviewing only the diff without opening the surrounding code.

Most of these improve quickly with feedback from more experienced reviewers.

## 149: What are common mistakes authors make in pull requests?

- PRs that are too big or mix several changes.
- No description, or just a ticket number.
- Asking for review before CI passes or before self-reviewing.
- Getting defensive about comments.
- Pushing many unrelated changes after approval.
- Resolving reviewers' comments without replying.

## 150: What tools are used for code review?

The most common ones:

- **GitHub** pull requests.
- **GitLab** merge requests.
- **Bitbucket** and **Azure DevOps** pull requests.
- **Gerrit**, used by projects like Android and Chromium, which reviews each commit separately.
- **Email** with patches, used by the Linux kernel and Git.

All of them have the same basic features: show the diff, comment on lines, track approvals, and connect to CI.

# Moderate Questions (151-300)

## 151: How do you structure a review into several passes?

Instead of reading top to bottom once, many reviewers do a few passes:

1. **Big picture**: read the description, skim all files. Is the approach right? Is this the right place for the change?
2. **Logic**: go through the main code carefully. Bugs, edge cases, errors, security.
3. **Tests**: do they cover the logic you just read?
4. **Details**: naming, readability, small cleanups.

If the first pass shows the approach is wrong, stop there and discuss it. There's no point commenting on variable names in code that will be rewritten.

## 152: Why should design problems be raised before line-by-line comments?

If the overall approach is wrong (wrong layer, wrong data model, a simpler solution exists), all the small comments become wasted work, for both reviewer and author. And the author may fix 30 nits, then hear the whole thing needs to change, which is frustrating.

Raise big concerns first, ideally as a top-level comment, and hold detailed comments until the direction is agreed.

## 153: When should a reviewer ask for a design doc instead of reviewing code?

When the PR introduces something with long-term impact: a new service, a new database or library, a big change to data models, a new public API, or a cross-team pattern. These are expensive to change after merge and deserve discussion before code.

A good habit is to agree on the approach in a short design doc or issue first, then the code review only checks the implementation.

## 154: What does Google's "code health" standard for approval mean?

Google's public code review guide says a reviewer should approve a change once it clearly improves the overall code health of the system, even if it isn't perfect. There's no such thing as perfect code, only better code.

So the question isn't "is this how I would write it?" but "is the codebase better with this change than without it?" Reviewers can still leave suggestions for polish, marked as optional.

## 155: How do you balance perfection and progress in reviews?

Holding PRs until they're perfect slows the team and frustrates authors. Approving everything quickly lets quality slide. The middle ground:

- Block on real problems: bugs, security, missing tests, bad design that's hard to undo.
- Don't block on preferences, small naming choices or things that can easily change later.
- Use follow-up tickets for good ideas that are out of scope.

Ask yourself: "If this merges as is, will we regret it?" If not, approve.

## 156: How can reviewers show how serious a comment is?

Use a shared scale. Netlify published one called "feedback ladders", which compares feedback to sizes of rock:

- **Mountain**: blocking and urgent, stop and talk.
- **Boulder**: blocking, must be fixed before merge.
- **Pebble**: not blocking, but should be fixed in the future.
- **Sand**: not blocking, worth thinking about.
- **Dust**: not blocking, take it or leave it.

Simpler options like "Blocking:", "Nit:" and "Optional:" prefixes work just as well. The point is to make importance visible.

## 157: What are Conventional Comments?

Conventional Comments is a format for review comments: `label (decorations): subject`. Labels include `praise`, `nitpick`, `suggestion`, `issue`, `todo`, `question`, `thought`, `chore` and `note`. Decorations like `(blocking)` or `(non-blocking)` show importance.

```text
issue (blocking): this query runs once per order in the loop, so a
page with 50 orders makes 50 DB calls. Can we load them in one query?

nitpick (non-blocking): `res` -> `response` for consistency with the
rest of the file.
```

It removes guesswork about what the reviewer means.

## 158: Why is it important to label nits explicitly?

Without labels, authors treat every comment as required. They spend time on tiny changes, the PR takes longer, and they may feel the review was harsh even if the reviewer saw it as minor.

With clear "Nit:" labels, the author can quickly decide what to do. It also helps the reviewer notice when a review is mostly nits, which is a sign the PR is fine and should be approved.

## 159: What should you do when you get a pull request that's too big?

Say so early and kindly, before spending hours on it:

```text
This is about 2,400 lines across 60 files, which is hard to review
well. Could we split it? For example: 1) DB migration and model,
2) API endpoints, 3) UI. Happy to help figure out the split.
```

If splitting isn't possible (a mechanical change, a deadline), agree on how to review it: a walkthrough call, reviewing commit by commit, or splitting the review among several people.

## 160: How do you split a large change into smaller pull requests?

Common ways:

- **By layer**: database migration, then backend, then frontend.
- **Preparatory refactors first**: "make the change easy, then make the easy change".
- **Behind a feature flag**: merge pieces that aren't active yet.
- **By feature slice**: one small working piece at a time.
- **Mechanical vs logic**: renames and moves in one PR, real changes in another.

Each PR should build, pass tests and make sense on its own.

## 161: What are stacked pull requests?

Stacked PRs are a chain of small PRs where each one builds on the previous one. PR 2's base branch is PR 1's branch, PR 3's base is PR 2's branch, and so on. Reviewers can review each step separately while the author keeps working.

When PR 1 merges, the next PR is retargeted to `main`. Tools like Graphite, ghstack, spr and Sapling help manage stacks, and Gerrit and Phabricator were built around this idea from the start.

## 162: What are the pain points of stacked pull requests on GitHub?

- If PR 1 changes after review, every PR above it needs to be rebased.
- Squash merging PR 1 can cause conflicts in PR 2, because the original commits no longer exist on `main`.
- Reviewers can get confused about which base the diff is against.
- CI might run against the wrong base.

Good tooling handles most of the rebasing automatically. Without tooling, keep stacks short, two or three PRs at most.

## 163: How does trunk-based development change code review?

In trunk-based development, everyone merges small changes into `main` often, at least daily. Branches live for hours, not weeks. That means PRs must be small and reviews must be fast, or the whole flow stops.

Teams doing this rely heavily on feature flags, strong CI and fast review turnaround. Some also use pair programming or post-merge review for some changes to avoid waiting.

## 164: What is the Ship/Show/Ask model?

Ship/Show/Ask, described by Rouan Wilsenach on martinfowler.com, says not every change needs the same review:

- **Ship**: merge directly without review (tiny fixes, docs, safe changes).
- **Show**: open a PR and merge it right away, but let others see it and comment afterwards.
- **Ask**: open a PR and wait for review before merging.

It trusts developers to pick the right level. It works best on experienced teams with good tests and monitoring, and it may not be allowed where compliance requires review of every change.

## 165: What is a review SLA?

A review SLA is the team's agreed maximum time for a first response to a review request, for example "within 4 working hours" or "by end of next business day".

It sets expectations: authors know when to ping, reviewers know reviews are part of the job, not something to do when bored. Track it loosely. The goal is predictability, not punishing people.

## 166: What review metrics are useful to track?

Common ones:

- **Time to first review**: how long a PR waits before someone looks at it.
- **Time to merge**: from opening to merging.
- **Number of review rounds**.
- **PR size distribution**.
- **Review load per person**.

These show bottlenecks, like one person doing half the reviews. Use them to improve the process, not to rank individuals.

## 167: How can a team reduce review wait time?

- Keep PRs small.
- Set a review SLA and check the queue at fixed times each day.
- Auto-assign reviewers so PRs don't sit with nobody.
- Spread review load beyond one or two senior people.
- Automate style and lint checks so humans review faster.
- Use stacked PRs so authors aren't blocked while waiting.

The biggest factor is usually culture: treating reviewing as real work with the same priority as writing code.

## 168: How do you balance review load across a team?

Look at who does the reviews. Often one or two senior people get most requests, which slows everyone and burns them out. Options:

- GitHub team review assignment with load balancing.
- A review rotation.
- Pairing juniors with seniors as co-reviewers to build skills.
- Encouraging authors to ask a wider set of people.

Over time, more people become comfortable reviewing more areas, which helps the bus factor too.

## 169: Why can having many reviewers make reviews worse?

It's called diffusion of responsibility: when several people are asked, each one assumes another will look carefully. The result can be a quick skim from everyone, or long delays because each waits for the others.

It also creates conflicting feedback. Better: name one main reviewer who is responsible, and add others only for specific parts ("Alex, please check the SQL").

## 170: How do you handle a PR that needs approval from several teams?

Make the request clear: who needs to review what. Ask each team for its part, maybe with separate comments tagging them. Use CODEOWNERS so required approvals are tracked automatically.

If it keeps happening, it may be a sign that the code is too tangled across team boundaries, or that the change should be split so each team reviews its own PR.

## 171: How do pattern rules work in a CODEOWNERS file?

GitHub's CODEOWNERS uses gitignore-like patterns, and the last matching pattern in the file wins:

```text
*                    @acme/everyone
/apps/web/           @acme/frontend
/apps/web/payments/  @acme/payments
*.sql                @acme/dba
```

A file in `/apps/web/payments/` is owned by `@acme/payments`, not `@acme/frontend`. Owners don't combine; only the last match counts. If you want two owners, list both on the same line.

## 172: What are common mistakes with CODEOWNERS?

- Putting broad rules at the bottom, which overrides the specific ones above.
- Listing teams that don't have write access to the repo, so their reviews don't count.
- Too many owners on everything, so every PR waits for many people.
- Owners who left the company or teams that were renamed.
- Owning files no one on the team actually knows.

Review CODEOWNERS changes carefully too. GitHub shows errors in the file in its web UI.

## 173: What does "Dismiss stale approvals" do?

It's a branch protection setting. When enabled, any approval is automatically dismissed if new commits that change the diff are pushed to the PR. The reviewer has to approve again.

It stops people from getting approval and then pushing different code. The downside is extra re-approvals for tiny fixes like typos. Some teams accept that cost, others prefer the next setting, which is a bit more targeted.

## 174: What does "Require approval of the most recent reviewable push" mean?

It's a GitHub branch protection option. It requires that the most recent push be approved by someone other than the person who pushed it. So if a reviewer pushes a commit to the author's branch, another person has to approve after that.

It closes a loophole where someone could push their own changes onto an approved PR and merge without anyone else seeing them.

## 175: What does "Require conversation resolution before merging" do?

When it's on, all review comment threads on the PR must be marked as resolved before the PR can be merged. It stops PRs from being merged with open questions nobody answered.

It works best when the team agrees who resolves threads. Otherwise authors may just click "Resolve" on everything to unblock the merge, which defeats the point.

## 176: What is the difference between branch protection rules and rulesets on GitHub?

Both enforce rules on branches, like required reviews and status checks. Rulesets are the newer option and have some advantages:

- Several rulesets can apply to the same branch, and their rules combine.
- They can target branches and tags by pattern, and can be set at the organization level.
- They can be set to "evaluate" mode to see the effect before enforcing.
- Anyone with read access can see which rules apply.

Classic branch protection still works. Many organizations are moving to rulesets for central control.

## 177: What is a merge queue and how does it relate to code review?

A merge queue (GitHub has one built in, GitLab has merge trains) takes approved PRs and merges them one by one, or in groups, after re-running CI against the latest `main` plus the PRs ahead in the queue.

It solves the problem where two PRs pass CI separately but break `main` together. Code review stays the same: you approve the PR, and the queue handles safe merging afterward.

## 178: What is auto-merge and when is it useful?

Auto-merge is a setting on a PR that merges it automatically once all requirements are met: approvals, required checks and so on. The author turns it on, and the PR merges as soon as the last check passes.

It saves people from watching CI. It's also handy for dependency update PRs from tools like Dependabot or Renovate, combined with rules about which updates can merge without a human.

## 179: How can you do code reviews from the command line?

The GitHub CLI covers most of the flow:

```bash
gh pr list --search "review-requested:@me"
gh pr view 123
gh pr diff 123
gh pr checkout 123
gh pr review 123 --approve --body "LGTM, nice cleanup"
gh pr review 123 --request-changes --body "See comments on the retry logic"
```

Inline comments on specific lines are easier in the web UI or an editor extension, but the CLI is quick for checking out and approving.

## 180: Should you review a PR commit by commit or as a whole diff?

It depends on how the author made the commits. If the commits are clean, logical steps ("rename X", "extract helper", "add feature"), reviewing one at a time is much easier. If the commits are "wip", "fix", "fix again", review the whole diff.

Authors who want commit-by-commit review should say so in the description, and keep commits clean with interactive rebase before asking for review.

## 181: What are fixup commits and how do they help during review?

A fixup commit is a commit meant to be squashed into an earlier one later. You create it with:

```bash
git commit --fixup=<sha-of-original-commit>
```

During review, the author adds fixup commits for each comment, so reviewers can see exactly what changed. Before merging, the author runs:

```bash
git rebase -i --autosquash main
```

which folds each fixup into the commit it belongs to. The result is clean history without hiding changes during review.

## 182: Should authors force-push or add new commits when addressing feedback?

New commits make it easy for reviewers to see what changed since their last look. Force-pushing a rebased branch can make that hard on GitHub, though GitHub does show a "compare" link for force pushes.

A common compromise: add commits during review, then squash merge or clean up with `--autosquash` at the end. Teams with commit-by-commit review often prefer rebasing and use `git range-diff` to compare versions.

## 183: What is git range-diff and how does it help reviewers?

`git range-diff` compares two versions of a series of commits, for example before and after the author rebased and changed things. It shows which commits changed and how.

```bash
git range-diff main old-branch new-branch
```

It's very useful when authors force-push. Instead of re-reviewing the whole PR, the reviewer can see exactly what changed in each commit between rounds.

## 184: How do you see only what changed since your last review?

On GitHub, in the "Files changed" tab, open the commits dropdown and pick "Changes since your last review", or select a range of commits. The "Viewed" checkboxes also reset for files that changed.

GitLab lets you compare versions of a merge request with its version selector. Gerrit compares patch sets. Locally, you can diff the old and new head SHAs: `git diff <old-sha> <new-sha>`.

## 185: Which git diff options are useful for code review?

```bash
git diff main...HEAD             # changes on this branch since it split from main
git diff --stat main...HEAD      # files changed and line counts
git diff -w main...HEAD          # ignore whitespace changes
git diff --color-moved main...HEAD   # highlight moved blocks differently
git diff --word-diff main...HEAD     # show changes word by word
git log --oneline main..HEAD     # commits on this branch
```

The three-dot form shows only what the branch added, not what changed on `main` in the meantime.

## 186: How do you review code that was moved and changed at the same time?

It's hard, because the diff shows a big deletion in one place and a big addition in another, hiding the small real changes. Options:

- Ask the author to split it: one commit that only moves, another that changes.
- Use `git diff --color-moved` to see which lines were moved unchanged.
- Diff the old and new file directly: `git diff main:old/path.ts HEAD:new/path.ts`.

## 187: What is .git-blame-ignore-revs?

It's a file listing commit SHAs that `git blame` should skip, usually large formatting or mass rename commits. Without it, blame shows the formatting commit as the author of every line, hiding who really wrote the code.

```bash
git config blame.ignoreRevsFile .git-blame-ignore-revs
```

GitHub uses a `.git-blame-ignore-revs` file in the repo root automatically in its blame view. Reviewers should ask for formatting-only commits to be added there.

## 188: How do you review a large formatting change?

Don't read it line by line. Instead:

- Make sure it's formatting only, with no logic mixed in. Check `git diff -w` to confirm it's nearly empty.
- Check the formatter config change, which is the real thing to review.
- Make sure CI passes.
- Ask to add the commit to `.git-blame-ignore-revs`.
- Merge it quickly to avoid conflicts with other open PRs.

## 189: How do you review a codemod or automated refactor?

Review the script or codemod itself, not each of the hundreds of changed files. Then spot-check a sample of files, especially unusual ones. Check that tests pass and the build is green.

Ask the author to include the command used in the PR description, so it can be re-run if the PR gets conflicts. Keep manual follow-up fixes in a separate commit so they're easy to see.

## 190: What are signs of good tests in a pull request?

- Each test checks one behavior and its name says what that is.
- Tests use the public interface, not internal details.
- Edge cases and error cases are covered, not just the happy path.
- Arrange, act and assert steps are easy to see.
- No random waits like `sleep(1000)`.
- They'd fail if the code broke.

```ts
it("returns 0 for an empty cart", () => {
  expect(cartTotal([])).toBe(0);
});
```

## 191: Is test coverage a good way to judge tests in a review?

It's a rough signal, not proof. Coverage shows which lines ran during tests, not whether the tests checked anything meaningful. A test that calls a function and asserts nothing can give 100% coverage.

Coverage drops on new code can be worth a question ("Is this branch tested?"). But in review, reading the tests and asking "what bug would this catch?" is more useful than the percentage.

## 192: How can a test pass for the wrong reason?

Common ways:

- The assertion is missing or always true.
- The async test doesn't wait for the promise, so it finishes before the check runs.
- The mock returns the expected value, so the real code isn't tested.
- The test checks the wrong variable.

```ts
// Passes even if fetchUser rejects, because the promise isn't awaited
it("loads the user", () => {
  fetchUser(1).then((u) => expect(u.name).toBe("Ana"));
});

// Correct
it("loads the user", async () => {
  const u = await fetchUser(1);
  expect(u.name).toBe("Ana");
});
```

A useful review trick: break the code on purpose and see if the test fails.

## 193: What should you say when tests use too many mocks?

Heavy mocking makes tests check that the code calls functions in a certain order, not that it produces the right result. These tests break on every refactor but miss real bugs.

```text
These tests mock the repository, the mapper and the validator, so they
mostly check the call order. Could we use the real mapper and validator
and only mock the DB? Then the test would catch real mapping bugs.
```

Mock at the edges (network, database, time), not every internal helper.

## 194: What should a reviewer do about a flaky test in a PR?

If the PR adds a test that sometimes fails, don't approve it as is. Flaky tests waste everyone's time and teach people to ignore red builds. Common causes: timing, shared state, test order, real dates and times, network calls.

If an existing flaky test fails on an unrelated PR, the right move is to report or fix it, not just keep pressing "re-run" until it passes.

## 195: What async error handling mistakes should reviewers look for?

```ts
// Error in the promise is never caught
app.post("/orders", (req, res) => {
  saveOrder(req.body); // not awaited
  res.status(201).send();
});

// forEach doesn't wait for async callbacks
items.forEach(async (item) => {
  await process(item);
});
console.log("done"); // runs before processing finishes
```

Look for missing `await`, `async` callbacks in `forEach`, promises created and forgotten, and `try/catch` blocks around code that doesn't actually await. The `@typescript-eslint/no-floating-promises` rule catches many of these.

## 196: How do you spot a missing await in a review?

Look for calls to async functions whose result isn't used, isn't returned and isn't awaited:

```ts
async function handler() {
  validate(input); // sync, fine
  sendWelcomeEmail(user); // async, not awaited: errors are lost
  return { ok: true };
}
```

Sometimes "fire and forget" is intended. Then it should be explicit, with a `.catch` to log errors and a comment explaining why. In TypeScript projects, ask for `no-floating-promises` to be enabled.

## 197: What null and undefined problems should reviewers look for?

- Accessing properties of something that can be `null`, like a find result.
- Using `||` for defaults when `0` or `""` are valid values (use `??`).
- Checking `if (value)` when `0` is a valid value.
- Non-null assertions (`!`) used to silence TypeScript.

```ts
const user = users.find((u) => u.id === id);
console.log(user.name); // crashes if not found

const limit = options.limit || 20; // 0 becomes 20
const limit2 = options.limit ?? 20; // 0 stays 0
```

## 198: How do you look for off-by-one errors in a review?

Check loop bounds (`<` vs `<=`), array indices, slices, pagination math and date ranges. Ask: what happens with the first item, the last item, an empty list and a list of one?

```ts
// Bug: with 1-based pages, page 1 should start at offset 0, not pageSize
const offset = page * pageSize;

// Fixed
const offset = (page - 1) * pageSize;
```

Inclusive vs exclusive ranges (is the end date included?) are a frequent source of bugs and worth a comment if unclear.

## 199: What race conditions can show up in web app code?

- Two requests read the same row, both update it, and one update is lost.
- "Check then create" logic that creates duplicates when two requests arrive at once.
- In the browser, an older fetch response arriving after a newer one and overwriting it.
- Shared module-level state in a Node.js server used by several requests.

When reviewing code that reads and then writes shared data, ask: "What if two of these run at the same time?"

## 200: What should you check when reviewing React useEffect changes?

- Is the effect needed at all, or could the value be computed during render?
- Are all dependencies listed (the `react-hooks/exhaustive-deps` lint rule helps)?
- Is there cleanup for subscriptions, timers and listeners?
- Can a slow response overwrite a newer one?

```tsx
useEffect(() => {
  const id = setInterval(refresh, 5000);
  return () => clearInterval(id); // cleanup
}, [refresh]);
```

Many bugs come from effects used for things that don't need them, like syncing state from props.

## 201: What should you check when reviewing state management changes?

- Is the state stored in the right place (local component, URL, server cache, global store)?
- Is the same data stored in two places that can get out of sync?
- Is derived data stored as state instead of being computed?
- Are updates immutable where the library expects it?
- Will this cause many components to re-render?

A common review comment: "Can this be derived from existing state instead of stored separately?"

## 202: What should you check when reviewing a new API endpoint?

- Authentication and authorization: who can call it, and can they only access their own data?
- Input validation and clear error responses.
- Correct HTTP methods and status codes (201 for create, 404 for not found, and so on).
- Pagination for lists.
- Naming consistent with other endpoints.
- Tests for success and failure cases.
- Rate limiting if the endpoint is expensive or public.

## 203: What should you look for when reviewing a database migration?

- Can it run on production data size without locking tables for too long?
- Is it backward compatible with the code currently running?
- Is there a way to roll back, or is it safe to only go forward?
- Does adding a `NOT NULL` column have a default or a backfill?
- Are new indexes needed for new queries?
- Is data being deleted or changed in a way that can't be undone?

Migrations are one of the riskiest kinds of PRs, so they deserve extra care.

## 204: How do you spot an N+1 query problem in a review?

Look for a database call inside a loop, or an ORM relation accessed per item:

```ts
const orders = await db.order.findMany();
for (const order of orders) {
  order.customer = await db.customer.findUnique({
    where: { id: order.customerId },
  });
}
```

This makes one query for orders plus one per order. Suggest loading related data in one query, with a join, an `include` in the ORM, or an `IN (...)` query.

## 205: What should you check about database indexes in a review?

When a PR adds a new query, check whether the columns in `WHERE`, `JOIN` and `ORDER BY` are indexed. When it adds an index, check whether it's actually needed, because indexes slow down writes and take space.

On big tables, ask how the index will be created. In PostgreSQL, `CREATE INDEX CONCURRENTLY` avoids blocking writes. Asking for an `EXPLAIN` output of the important query is fair in a review.

## 206: What should you check when a PR adds a new environment variable?

- Is it documented, for example in `.env.example` or the README?
- Is it set in every environment (dev, staging, production, CI)?
- Does the app fail clearly at startup if it's missing, instead of failing later?
- Is it a secret? Then it should come from a secret manager, not a committed file.
- Is it validated (type, format)?

```ts
const env = z.object({ STRIPE_KEY: z.string().min(1) }).parse(process.env);
```

## 207: How do you review infrastructure-as-code changes?

For Terraform, Pulumi, CloudFormation and similar:

- Read the plan output, not just the code. What will be created, changed or destroyed?
- Watch for resources being replaced (destroyed and recreated), which can mean data loss or downtime.
- Check permissions, network rules and public access.
- Check that names, tags and settings match conventions.

Many teams post `terraform plan` output as a PR comment automatically so reviewers see the real effect.

## 208: What should you check when reviewing CI pipeline changes?

- Could the change skip tests or checks without anyone noticing?
- Are secrets exposed to steps or events that don't need them?
- Are third-party actions pinned to a version or commit SHA?
- Does it slow the pipeline down a lot?
- Does it still run on the events it should (PRs, pushes to main, tags)?

CI files control what reaches production, so treat changes to them as security-sensitive.

## 209: How do you review a dependency upgrade PR?

- Read the changelog or release notes, especially for major versions.
- Check for breaking changes and whether the code uses affected APIs.
- Make sure CI and tests pass.
- For big upgrades, test the app manually or on a preview.
- Check that the lockfile changed only the expected packages.

For tools like Dependabot or Renovate, teams often auto-merge patch updates with passing tests and review minor and major ones by hand.

## 210: How do you evaluate whether a new dependency should be added?

Questions to ask in review:

- How much code would we write ourselves instead? A few lines? Then skip the package.
- Is it maintained (recent releases, issues being answered)?
- How many people use it?
- What's the license, and is it allowed in our project?
- How big is it, and how many dependencies does it pull in?
- Does it have known vulnerabilities (`npm audit`)?

The `left-pad` incident in 2016 is a common example of why tiny dependencies can still be risky.

## 211: What basic security checks should every reviewer do?

- User input validated and used safely (parameterized queries, no `eval`).
- Output properly escaped in HTML to prevent XSS.
- Auth and permission checks on every endpoint that needs them.
- No secrets in code or logs.
- Errors don't leak stack traces or internal details to users.
- New dependencies checked for known issues.

You don't need to be a security expert to catch most of these. The OWASP Top 10 is a good list to learn.

## 212: How do you spot a missing authorization check in a review?

Look for endpoints that load data by an ID from the request but don't check that the current user is allowed to see it:

```ts
// Any logged-in user can read any invoice by changing the ID
app.get("/invoices/:id", requireLogin, async (req, res) => {
  const invoice = await db.invoice.findUnique({ where: { id: req.params.id } });
  res.json(invoice);
});

// Fixed: scope the query to the current user
const invoice = await db.invoice.findFirst({
  where: { id: req.params.id, userId: req.user.id },
});
```

This is called an IDOR (insecure direct object reference). Ask "what stops user A from reading user B's data?"

## 213: What should happen if a secret is pushed in a pull request?

1. Revoke or rotate the secret immediately. Assume it's compromised.
2. Remove it from the code and load it from a secret manager or environment variable.
3. Check logs of the service for misuse.
4. Optionally remove it from Git history, but this doesn't undo the leak, because forks and clones may already have it.

GitHub push protection can block pushes that contain known secret formats. It's worth enabling for every repo.

## 214: How do you spot sensitive data in logs during a review?

Look for logging whole objects like `req.body`, `req.headers`, `user` or error objects from HTTP clients, which often include tokens and passwords:

```ts
logger.info({ body: req.body }, "login attempt"); // logs the password
logger.info({ email: req.body.email }, "login attempt"); // better
```

Ask the author to log only the fields needed, or to use the logger's redaction feature (pino, for example, has a `redact` option).

## 215: How do you review performance-sensitive code?

- Find the hot path: is this code run once per request, once per item, or once per day?
- Look for repeated work inside loops: queries, regex compiles, big object copies.
- Check algorithm complexity, like nested loops over big lists.
- Check memory usage, like loading a whole table or file into memory.
- Ask for numbers when the claim is "this is faster".

Don't push for optimizations on code that runs rarely. Readability usually matters more there.

## 216: When should a reviewer ask for benchmarks?

When the PR's main reason is performance, or when it changes something on a hot path in a way that might be slower. "This is faster" without measurement is a guess.

Ask for a simple before/after comparison under realistic conditions: real data size, production-like settings. For front-end changes, a Lighthouse run, a Performance panel recording or a bundle size comparison is often enough.

## 217: What deeper accessibility issues should you look for in UI reviews?

- Focus management when opening and closing modals and menus.
- Correct use of ARIA only where native HTML isn't enough.
- Announcements for dynamic content (`aria-live`) like toast messages.
- Heading order that makes sense for screen readers.
- Custom components (dropdowns, tabs) that support keyboard interaction the way users expect.

"No ARIA is better than bad ARIA" is a good rule. Ask the author to test with a screen reader for complex widgets.

## 218: What should you check about error messages and UX in a review?

- Does the user understand what went wrong and what to do?
- Are technical details hidden from users but logged for developers?
- Are loading, empty and error states handled in the UI?
- Can the user retry, or are they stuck?
- Are form errors shown next to the right field?

A good review question: "What does the user see if the API returns 500 here?"

## 219: Why do names matter more at API boundaries?

Inside a function, a bad name can be fixed any time. Names in public APIs, database columns, event names and URL paths are much harder to change later, because other code, other teams or customers depend on them.

So in review, spend more effort on names that cross boundaries. A rename in a private helper can be a nit; a rename in a public REST field may be blocking.

## 220: What should you check in documentation for public APIs?

- Every public function, endpoint or component has a short description.
- Parameters, return values and errors are documented.
- Examples are correct and up to date.
- Breaking changes and deprecations are noted.
- Generated docs (OpenAPI, TypeDoc) still build.

If the docs are generated from code (like an OpenAPI spec), review the spec changes like code, since clients may be generated from it.

## 221: What should you check about observability in a review?

Ask: "When this breaks in production, how will we know and how will we debug it?"

- Are there logs at key decision points?
- Are errors reported to the error tracker (like Sentry)?
- Are there metrics for important operations (count, duration, failures)?
- Are traces passed to downstream calls?
- Are alerts needed?

New features often ship without any way to see if they work, until a user complains.

## 222: What should reviewers check about feature flag removal?

When a flag is fully rolled out, there should be a PR that removes it. Check that:

- The old code path is fully deleted, not left as dead code.
- Tests for the old path are removed and tests for the new path stay.
- The flag is also removed from the flag service or config.
- No other code still reads the flag.

Flags that live forever make the code hard to read and test.

## 223: How do you review a pull request that deletes code?

Deleting code is usually good, but check that it's really unused:

- Search for references, including dynamic ones (string-based lookups, reflection, config files).
- Check other repos or services that might call it.
- Check that related tests, docs and config are cleaned up too.

Then be happy about it. Removing unused code is one of the best kinds of PRs.

## 224: What is premature abstraction and how do you spot it in a review?

Premature abstraction means building a general solution before there's a real need for it: an interface with only one implementation, a factory for one class, a config option nobody uses, a "base" component with ten props to support future cases.

In review, ask: "How many places use this today?" If the answer is one, suggest keeping it simple until a second real use appears. A common rule is to wait until the third time before abstracting.

## 225: How do you push back on over-engineering in a PR without being rude?

Focus on concrete costs, and ask about the need:

```text
This adds a plugin system with a registry and three interfaces, but we
only have one handler today. Could we start with a plain function and
add the registry if we get a second handler? It'd be easier to read
and test right now.
```

Accept that the author may know about upcoming needs you don't. Ask, don't assume.

## 226: How do you handle a PR that uses a quick hack?

Find out why. Sometimes there's a deadline and a hack is the right call. Then ask for:

- A comment explaining the hack and why it's there.
- A ticket to fix it properly.
- Tests, so the hack doesn't break silently.

If there's no real time pressure and a proper fix is only slightly more work, ask for the proper fix.

## 227: Should new code follow existing patterns or better new ones?

Usually follow the existing patterns. Consistency makes a codebase easier to read, even if the pattern isn't perfect. One file doing things differently confuses the next person.

If the new pattern is clearly better, discuss it with the team first and plan to migrate the old code. Otherwise you end up with two (then three) ways of doing the same thing.

## 228: How should someone introduce a new pattern or library through a PR?

Don't sneak it in as part of a feature PR. Bring it up first, in a short design doc, an RFC, or a team discussion. Explain the problem it solves, the trade-offs and the migration plan for old code.

Then the first PR can introduce it in one place as an example, and the reviewers can focus on whether it's implemented well instead of whether the team wants it at all.

## 229: How do you tell personal preference from a real issue in a review?

Ask yourself: "Can I explain a concrete problem this causes?" Bugs, confusion for readers, performance, security and inconsistency with team conventions are real issues. "I'd write it differently" with no other reason is a preference.

Preferences can still be shared, but as optional comments: "Personal preference, feel free to ignore: I find early returns easier to read here."

## 230: How do you resolve a disagreement in a code review?

1. Understand both positions. Restate the other person's point.
2. Look for facts: docs, team conventions, benchmarks, a quick test.
3. Talk on a call if comments aren't working.
4. If both options are reasonable, let the author decide; it's their code.
5. If it's still stuck, ask a tech lead or a third engineer to decide.

Write down the decision in the PR. If it's a general question, add it to the team's guidelines so it doesn't come up again.

## 231: When should a code review disagreement be escalated?

When the discussion is going in circles, when it blocks important work, or when it's about something with long-term impact like architecture or security. Escalation isn't a failure; it's a way to stop wasting time.

Escalate to whoever can decide, usually a tech lead or the code owner of the area. Present both sides fairly, not just your own.

## 232: What should a reviewer do when they realize they were wrong?

Say so plainly: "You're right, I missed that the list is already sorted. Ignore my comment." Then resolve the thread.

Admitting mistakes quickly builds trust, shows juniors it's normal to be wrong, and keeps reviews focused on the code. Defending a wrong comment to save face does the opposite.

## 233: How should an author respond when a reviewer asks for something out of scope?

Acknowledge the idea and suggest a follow-up:

```text
Good point, the error handling in this file needs work. It's unrelated
to this fix though, so I opened PAY-512 for it. OK to merge this as is?
```

This keeps the PR focused and shows the feedback was taken seriously. If the reviewer insists it's needed now, discuss why. Sometimes it really is related.

## 234: How do you handle an author who gets defensive about feedback?

Stay calm and focus on the code. Check your own comments: were they clear, polite and explained? Sometimes defensiveness is a reaction to tone, not content.

Move hard discussions to a call. Ask questions instead of making statements. Point out what's good in the PR too. If it's a pattern, talk to the person privately, or involve a lead.

## 235: How do you handle a reviewer whose comments are harsh?

As the author, respond to the content, not the tone. Ask for clarification where needed. If comments are rude or personal, talk to the reviewer directly and privately: "Some of your comments on my PR felt pretty harsh. Can we talk about it?"

If it keeps happening or affects several people, raise it with a manager or lead. Harsh reviewing hurts the whole team's willingness to ask for feedback.

## 236: How do you give critical feedback to a more senior engineer?

The same way you would to anyone: specific, polite and with reasons. Seniors make mistakes too, and good ones want to hear about them.

```text
I might be missing context, but it looks like this cache never expires
entries. Could that grow without limit for users with many sessions?
```

Phrasing it as a question is fine when you're not sure, but don't hide real problems out of politeness.

## 237: How do you run code reviews across time zones?

- Keep PRs small and descriptions complete, so a reviewer can act without asking questions.
- Give all feedback in one round instead of drip-feeding comments.
- Approve with minor comments when possible, so the author can merge in their morning.
- Have reviewers in overlapping time zones for urgent work.
- Use short recorded videos to explain complex PRs.

Each round trip can cost a full day, so cutting rounds matters more than speed of any one review.

## 238: What is a code walkthrough and when is it useful?

In a walkthrough, the author presents the change to one or more reviewers in a meeting or call, explaining the reasoning while they ask questions. It's useful for large or complex PRs, new architecture or onboarding people to an area.

It's faster than many written rounds and good for shared understanding. But it doesn't replace a careful written review, because the presenter can make code seem clearer than it is.

## 239: What is mob review?

In a mob review, the whole team (or several people) reviews a change together on a shared screen. It's good for important changes, teaching a team review standards, and agreeing on conventions.

It's expensive, so it's not for every PR. Some teams do it once a week with an interesting PR as a learning session.

## 240: When is synchronous review better than asynchronous review?

Synchronous (live, together) is better when:

- The change is complex and needs a lot of explanation.
- Written discussion is stuck or getting tense.
- The change is urgent, like a hotfix.
- Someone is new and benefits from real-time explanation.

Asynchronous is better for most normal PRs, because it doesn't interrupt people and leaves a written record.

## 241: How do you review your manager's code?

The same way as anyone else's. Managers who code want their code to be correct too. Being gentler or harsher because of their role doesn't help the team.

If you're nervous, phrase comments as questions and give reasons. A good manager will appreciate it. If a manager reacts badly to normal review comments, that's a team culture problem worth bringing up.

## 242: What could a team's review checklist look like?

A short, practical example:

```markdown
- [ ] I understand what this PR does and why
- [ ] The approach makes sense for the problem
- [ ] Edge cases and errors are handled
- [ ] New behavior has tests that would fail if it broke
- [ ] No security problems: input validation, authz, secrets
- [ ] No breaking changes, or they're planned and documented
- [ ] Names and structure are easy to follow
- [ ] Logs and metrics are enough to debug in production
```

Everything that a tool can check (formatting, lint, types) should be left off.

## 243: Why should review checklists be short?

Long checklists don't get used. People skim them or tick everything without thinking. A short list of things that really matter, and that tools can't catch, gets followed.

Update the checklist from real problems: if a bug type keeps slipping through review, add a line. If a line has never caught anything, remove it or automate it.

## 244: What review work can be automated?

- Formatting (Prettier, Black, gofmt).
- Linting and type checking.
- Tests and coverage reports.
- Security scans and secret scanning.
- Dependency checks.
- Bundle size and performance budgets.
- PR rules: description filled in, ticket linked, changelog updated, size limits.

Automating these frees people to focus on design, logic and readability, which tools can't judge well.

## 245: What is Danger.js and how is it used in code review?

Danger.js runs during CI and checks things about the PR itself, then leaves comments or fails the build. It's used to automate common review reminders.

```js
// dangerfile.js
import { danger, warn, fail } from "danger";

const changed = [...danger.git.modified_files, ...danger.git.created_files];

if (
  changed.some((f) => f.startsWith("src/")) &&
  !changed.some((f) => f.includes(".test."))
) {
  warn("Source files changed but no tests were updated.");
}

if (!danger.github.pr.body || danger.github.pr.body.length < 20) {
  fail("Please add a description to this PR.");
}
```

## 246: How can you automatically flag pull requests that are too big?

Options:

- A Danger.js rule that warns over a line count.
- A GitHub Action that adds size labels (like `size/S`, `size/XL`) based on changed lines.
- A team dashboard that tracks PR sizes over time.

Warnings work better than hard blocks, because some big PRs are legitimate, like a generated file update. Exclude lockfiles and generated files from the count.

## 247: How are labels used to manage pull requests?

Labels help sort and filter PRs: `bug`, `feature`, `needs-design-review`, `security`, `do-not-merge`, `size/L`, `backport`. They're used for triage, release notes and automation (for example, auto-merge only PRs labeled `dependencies`).

Keep the set of labels small and well defined, or nobody will use them consistently.

## 248: What should a good pull request template include?

```markdown
## What changed and why

<!-- Short summary and link to ticket -->

## How was this tested?

<!-- Steps, test cases, screenshots -->

## Risk and rollout

<!-- Feature flag? Migration? Anything to watch after deploy? -->

## Notes for reviewers

<!-- Where to start, what to focus on -->
```

Fewer sections are better than many. A template nobody fills in is worse than none.

## 249: What is a definition of done and how does it relate to code review?

A definition of done is a team's list of what must be true before work counts as finished: code reviewed, tests passing, docs updated, deployed to staging, product sign-off and so on.

Code review is usually one item on that list. The PR template and checklist can mirror the definition of done so nothing gets forgotten.

## 250: How do you review an architecture decision record?

An ADR records a decision: context, the decision itself, and consequences. When reviewing one, check:

- Is the problem clearly stated?
- Were alternatives considered, with honest pros and cons?
- Are the trade-offs and risks spelled out?
- Is it clear what changes because of this?

The goal isn't to re-argue everything, but to make sure the record will make sense to someone reading it in two years.

## 251: How is reviewing an RFC different from reviewing code?

An RFC (request for comments) proposes a change before it's built. Reviewing it means questioning the problem, the goals and the approach, not the details. Good questions:

- Is the problem real and worth solving now?
- What alternatives were considered?
- What are the risks, costs and migration steps?
- How will we know it worked?

Feedback on RFCs is cheap compared to feedback on finished code, so this is the best time to raise big concerns.

## 252: What do open source maintainers look for when reviewing a PR?

- Does it fit the project's goals and roadmap?
- Was it discussed in an issue first (for anything non-trivial)?
- Does it follow the contributing guide and code style?
- Are there tests and docs?
- Will the maintainers be able to support this code long term?

Maintainers often say no to working code because it adds features they don't want to maintain. That's not a judgment of the contributor.

## 253: How should maintainers review PRs from first-time contributors?

Be welcoming and patient. Thank them, explain project conventions with links instead of assuming they know them, and be clear about what must change. Small fixes can be made directly by the maintainer (with "Allow edits from maintainers" on GitHub) instead of another round.

If the PR can't be accepted, explain why kindly and, if possible, suggest another way they could help. A good first experience often turns into a long-term contributor.

## 254: What are Reviewed-by and Acked-by tags in the Linux kernel?

In email-based workflows like the Linux kernel, reviews are recorded as tags in the commit message:

```text
Signed-off-by: Ana Author <ana@example.com>
Reviewed-by: Sam Reviewer <sam@example.com>
Acked-by: Max Maintainer <max@example.com>
Tested-by: Lee Tester <lee@example.com>
```

`Signed-off-by` certifies the DCO, `Reviewed-by` says the person reviewed the patch carefully, `Acked-by` usually means a maintainer of the affected area is fine with it, and `Tested-by` says someone tested it. The history then shows who reviewed what.

## 255: How does code review work in Gerrit?

In Gerrit, each commit is reviewed on its own as a "change". Reviewers vote with labels. The default `Code-Review` label goes from -2 to +2:

- **+2**: approved, can be submitted.
- **+1**: looks good, but someone else should approve.
- **0**: no opinion.
- **-1**: I'd prefer this not be submitted as is.
- **-2**: blocked, must not be submitted.

A `Verified` label is usually set by CI. A change typically needs `Code-Review +2` and `Verified +1` and no `-2` before it can be submitted.

## 256: What are Change-Id and patch sets in Gerrit?

Gerrit adds a `Change-Id:` line to each commit message (through a commit-msg hook). When you amend the commit and push again, Gerrit uses the Change-Id to know it's a new version of the same change, called a new "patch set".

Reviewers can compare any two patch sets, so authors amend commits instead of adding fixup commits. This is different from GitHub, where a PR is a branch with many commits.

## 257: How do approval rules work in GitLab?

GitLab merge requests can require approvals through approval rules. You can set how many approvals are needed and from which users or groups, and combine this with CODEOWNERS so owners of changed files must approve. Rules can be set at project level, and some features (like several rules or code owner approval) depend on the GitLab tier.

There are also settings like preventing the author from approving their own MR, preventing approval by people who added commits, and removing approvals when new commits are pushed.

## 258: How do branch policies work in Azure DevOps?

Azure DevOps uses branch policies on target branches. Common policies:

- Minimum number of reviewers, with options like allowing or blocking self-approval and resetting votes on new pushes.
- Required reviewers for certain paths.
- Linked work items required.
- Comment resolution required.
- Build validation (CI must pass).

Reviewers vote Approve, Approve with suggestions, Wait for author or Reject. It's the same idea as GitHub branch protection with different names.

## 259: How should you review a hotfix during an incident?

Keep it focused but don't skip it:

- Is the fix as small as possible?
- Does it actually address the cause seen in logs or metrics?
- Could it make things worse (data changes, new failure modes)?
- Is it easy to roll back?
- Is there a test, or at least a clear manual check?

Review on a call if possible to save time. Bigger cleanups and refactors can come in a follow-up PR after the incident.

## 260: How do you make sure post-merge reviews actually happen?

Post-merge review is easy to forget. Ways to make it stick:

- Label or tag PRs that were merged without review, and track them on a board.
- Have a bot open an issue or reminder for each one.
- Make the reviewer assignment explicit at merge time.
- Check the list in a regular meeting.

If post-merge reviews pile up unreviewed, it's a sign the team should go back to pre-merge review.

## 261: How should you review a revert PR?

Reverts are usually urgent, so review fast, but check:

- Is it a clean revert of the right commit(s)?
- Did anything merge after the original change that depends on it?
- Does the revert also need a reverse database migration or config change?
- Is there a ticket or note explaining why it was reverted?

A revert of a revert (re-landing the change) should be reviewed like a new PR, with focus on what was fixed.

## 262: How do you review generated code like API clients?

Don't review the generated output line by line. Review what produced it:

- The schema (OpenAPI, GraphQL, Protobuf) changes.
- The generator version and config.
- A quick skim of the output to check it changed as expected.

Make sure the generation is repeatable, ideally checked in CI (regenerate and fail if the result differs from what was committed).

## 263: What should you check when reviewing a Dockerfile?

- Pinned base image versions instead of `latest`.
- A small base image and multi-stage builds to keep the final image small.
- No secrets copied into the image or passed as build args.
- Running as a non-root user.
- Layer order that uses the cache well (copy `package.json` and install before copying source).
- A `.dockerignore` that excludes `node_modules`, `.git` and `.env`.

```dockerfile
FROM node:22-slim AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:22-slim
WORKDIR /app
COPY --from=build /app/dist ./dist
COPY --from=build /app/node_modules ./node_modules
USER node
CMD ["node", "dist/server.js"]
```

## 264: What security issues should you look for in GitHub Actions workflow changes?

- Using `pull_request_target` and then checking out and running the PR's code, which gives untrusted code access to secrets.
- Putting untrusted input like `${{ github.event.pull_request.title }}` directly into a `run:` script, which allows script injection.
- Third-party actions pinned to a moving tag instead of a commit SHA.
- `permissions` broader than needed; set `contents: read` by default.
- Secrets printed to logs.

```yaml
# Risky: title is injected into the shell
- run: echo "${{ github.event.pull_request.title }}"

# Safer: pass through an env variable
- run: echo "$TITLE"
  env:
    TITLE: ${{ github.event.pull_request.title }}
```

## 265: What should you check when a PR adds a third-party script to the front end?

- Is it loaded from a trusted source, and does it need to be third-party-hosted at all?
- Does it slow page load? Should it be `async` or `defer`, or loaded later?
- What data can it access? Scripts on your page can read the DOM, including form fields.
- Does it need a Content Security Policy update?
- Does it set cookies that need consent under privacy laws?

Subresource Integrity (`integrity` attribute) helps for scripts with fixed versions.

## 266: What should you check when reviewing caching changes?

- What's the cache key? Can two different users or requests share a key by mistake?
- When does the data expire or get invalidated?
- What happens when the cache is down or empty?
- Is personal data cached in a shared cache (like a CDN)?
- Are HTTP cache headers (`Cache-Control`) correct for private or public data?

A classic bug: caching a response per URL that's actually different per user, so one user sees another's data.

## 267: Why is module-level state risky in a Node.js server?

A Node.js server handles many requests in the same process, so a variable at the top of a module is shared by all of them:

```ts
let currentUser: User | null = null; // shared by every request

app.use((req, res, next) => {
  currentUser = req.user; // request B overwrites request A's user
  next();
});
```

In review, look for mutable variables outside functions that hold per-request data. Use the request object, function arguments or `AsyncLocalStorage` instead.

## 268: What should you check about timeouts and retries when reviewing network calls?

- Is there a timeout? Many HTTP clients wait forever by default.
- Are retries limited, with a delay between them?
- Is it safe to retry this call (is it idempotent)?
- What happens when all retries fail?

```ts
const res = await fetch(url, { signal: AbortSignal.timeout(5000) });
```

Calls without timeouts can tie up connections and make a small outage in another service much bigger.

## 269: What should you check when reviewing pagination code?

- Is there a maximum page size, so clients can't request a million rows?
- Is the sort order stable? Without a unique tie-breaker, items can repeat or be skipped between pages.
- For big or fast-changing tables, is cursor-based pagination better than offset?
- Does the response tell the client if there are more pages?

```sql
-- Stable ordering with a tie-breaker
SELECT * FROM posts ORDER BY created_at DESC, id DESC LIMIT 20;
```

## 270: Why is adding a required field to an API request a breaking change?

Existing clients don't send the new field, so their requests will start failing validation as soon as the change is deployed. Mobile apps are especially affected, because users don't update right away.

Safer options in review: make the field optional with a sensible default, or add it as optional first, update all clients, then make it required later.

## 271: What should you check when reviewing event or message schema changes?

Events in queues or streams are read by other services, sometimes much later. Check:

- Can existing consumers still read the new format?
- Can new consumers still read old messages that are still in the queue?
- Are fields only added, not renamed or removed?
- Is there a version field or schema registry check?

Treat event schemas like a public API. Breaking them can cause failures in services the author doesn't even know about.

## 272: Why should risky PRs include a rollback plan?

If something goes wrong after deploy, the team needs to know how to undo it quickly. For most code, a revert is enough. But some changes can't be simply reverted: data migrations, changes to message formats, external API calls, emails sent to users.

A short "Rollback" section in the PR description, or a feature flag to turn it off, lets the reviewer judge the real risk of the change.

## 273: How do you review code for testability?

Code is hard to test when it creates its own dependencies, reads global state, calls the current time directly, or mixes logic with I/O. Signs in review: tests need lots of mocking, or there are no tests because "it's hard to test".

```ts
// Hard to test: hidden dependency on the clock
function isExpired(token: Token) {
  return token.expiresAt < Date.now();
}

// Easier: pass the time in
function isExpired(token: Token, now = Date.now()) {
  return token.expiresAt < now;
}
```

## 274: How do visual tests and Storybook help code review?

Storybook shows components in isolation in all their states, and many teams deploy it for each PR. Reviewers and designers can check components without running the whole app.

Visual regression tools (like Chromatic, Percy or Playwright's screenshot comparisons) compare screenshots before and after the change and highlight differences. That catches unintended style changes that are almost impossible to see in a CSS diff.

## 275: What should reviewers check about any and type assertions in TypeScript?

`any` turns off type checking, and type assertions (`as`) tell the compiler "trust me", which can hide real bugs:

```ts
const user = JSON.parse(body) as User; // no check that it's actually a User
```

In review, ask why `any` or `as` is needed. Better options: `unknown` plus narrowing, validation with a schema library like Zod, or fixing the types. Some casts are fine, but they should be rare and explained.

## 276: Why are non-null assertions a review concern in TypeScript?

The `!` operator tells TypeScript a value isn't `null` or `undefined`, without checking at runtime:

```ts
const el = document.getElementById("root")!;
const user = users.find((u) => u.id === id)!;
```

If the assumption is wrong, the code crashes later with a less clear error. In review, ask whether the value can really never be missing. If it can, handle it. If it truly can't, a runtime check with a clear error is often better than `!`.

## 277: How should errors be wrapped and rethrown?

When catching an error to add context, keep the original error. Since ES2022, `Error` accepts a `cause` option:

```ts
try {
  await chargeCard(order);
} catch (err) {
  throw new Error(`Payment failed for order ${order.id}`, { cause: err });
}
```

Things to flag in review: catching and throwing a new error without the original (the stack trace is lost), catching just to log and rethrow at every level (the same error is logged many times), and converting every error into a generic "Something went wrong".

## 278: How do you review log levels?

- `error`: something failed and someone may need to act.
- `warn`: something unexpected, but the app handled it.
- `info`: important normal events, like startup or a completed job.
- `debug`: details useful only while debugging.

Common review issues: expected situations (like a 404 from user input) logged as `error`, which floods alerts; or real failures logged as `info`, which hides them.

## 279: What code smells should reviewers watch for?

- Very long functions or files.
- Deep nesting.
- Long parameter lists or boolean flag parameters.
- Duplicated logic.
- Classes or modules that do too many unrelated things.
- Feature envy: a function that mostly uses another object's data.
- Shotgun surgery: one change requires edits in many places.

A smell isn't always a bug. It's a hint to look closer and ask if the code will be hard to change.

## 280: Why do reviewers push back on boolean flag parameters?

A call like `createUser(data, true, false)` is unreadable: what do `true` and `false` mean? A boolean parameter often also means the function does two different things.

```ts
// Hard to read
sendEmail(user, true);

// Clearer
sendEmail(user, { urgent: true });
// or two functions
sendUrgentEmail(user);
```

Options objects or separate functions make the call site clear.

## 281: How do guard clauses improve code under review?

Deeply nested `if` blocks are hard to follow. Guard clauses handle the special cases first and return early, so the main logic isn't indented:

```ts
// Nested
function ship(order) {
  if (order) {
    if (order.paid) {
      if (!order.shipped) {
        // ship it
      }
    }
  }
}

// Guard clauses
function ship(order) {
  if (!order || !order.paid || order.shipped) return;
  // ship it
}
```

## 282: How should repeated string values be handled in TypeScript code?

Raw strings repeated in many places (`"pending"`, `"admin"`) are easy to mistype and hard to rename. In TypeScript, a union type or a constant object makes them checked:

```ts
type OrderStatus = "pending" | "paid" | "shipped";

function canCancel(status: OrderStatus) {
  return status === "pending";
}

canCancel("payed"); // compile error
```

A review comment can suggest a type like this when the same string shows up in several files.

## 283: What should you check about file and module organization in a review?

- Is the new code in the folder where people would look for it?
- Does it follow the existing structure (by feature, by layer)?
- Are files getting too big, mixing unrelated things?
- Are internal helpers exported when they don't need to be?
- Are imports reaching into another module's internals?

Poor placement isn't a bug, but it makes the codebase harder to navigate over time.

## 284: Why are circular dependencies a review concern?

When module A imports B and B imports A, you get a circular dependency. In JavaScript, this can lead to `undefined` imports at runtime depending on load order, and it usually means the modules are too tangled.

In review, watch for new imports that go "back up" or across features. Tools like `madge` or ESLint's `import/no-cycle` rule can detect cycles automatically.

## 285: How do you decide which review comments matter most?

Rough order:

1. Wrong behavior, data loss, security issues.
2. Design problems that will be hard to change later.
3. Missing tests for important logic.
4. Readability problems that will slow down future work.
5. Small style and naming issues.

If you're short on time, cover the top of the list and say what you didn't check.

## 286: How many comments are too many in a review?

There's no number, but if a PR gets 40+ comments, something went wrong earlier: the PR is too big, the approach wasn't agreed, or the reviewer is commenting on preferences.

In that case, step back. Leave a top-level comment about the main issues, offer a call, and drop the nits for now. A wall of comments overwhelms the author and hides the important ones.

## 287: Why should reviewers batch comments into one review?

On GitHub, you can "Start a review" and add comments as pending, then submit them all at once. This sends one notification instead of 20, and lets you edit or remove earlier comments once you understand the full change.

Often a question on file 1 gets answered by file 5. Batching lets you delete it before the author ever sees it.

## 288: What should you check when re-reviewing a pull request?

- That each of your comments was addressed or answered.
- The new changes themselves. Fixes can introduce new bugs.
- That nothing unrelated sneaked in.
- That CI is still green.

Use "changes since your last review" so you don't re-read everything. Don't add new nits on code you already approved in the last round, unless something is actually wrong.

## 289: Is it OK to approve and trust the author to fix the remaining comments?

Yes, for small things, if you trust the author. It saves a round trip, especially across time zones. Say so clearly: "Approving, please fix the typo and the log level before merging."

Don't do it for anything important or for a change where the fix itself could be risky. And if the team uses "dismiss stale approvals", the author will need a re-approval anyway.

## 290: Can you do code reviews inside your editor?

Yes. Extensions like GitHub Pull Requests for VS Code, and built-in support in JetBrains IDEs, let you check out a PR, see the diff, jump to definitions, run tests and leave comments without leaving the editor.

Reviewing in the editor gives you full code navigation and type information, which helps with larger PRs. The web UI is still handy for quick reviews.

## 291: How should PRs from bots like Dependabot or Renovate be reviewed?

- Patch updates with passing tests can often be auto-merged.
- Minor updates: skim the changelog and check CI.
- Major updates: read the migration guide, check for breaking changes and test the app.
- Security updates: prioritize them.

Group related updates (for example all `eslint` packages) to reduce noise. Don't let bot PRs pile up, or upgrades become a big painful project later.

## 292: What should you check about time in tests during review?

Tests that use the real current time can fail at midnight, at month end, around daylight saving changes, or in a different time zone on CI.

```ts
import { vi } from "vitest";

vi.useFakeTimers();
vi.setSystemTime(new Date("2026-03-01T12:00:00Z"));
// ... test ...
vi.useRealTimers();
```

Look for `new Date()` or `Date.now()` in tests and in logic that's being tested, and suggest fixed times or passing time in as a parameter.

## 293: Why are environment checks in code a review concern?

Code like `if (process.env.NODE_ENV === "production")` creates paths that only run in one environment. Those paths often aren't tested until they hit production.

In review, ask whether the difference should be config instead (a feature flag or a setting), so the same code runs everywhere with different values. Check that dev-only shortcuts, like skipping auth, can never be turned on in production.

## 294: How should changes to shared libraries or components be reviewed?

Shared code has many users, so a small change can break many places. Check:

- Who uses it? Search across the repo and other repos.
- Is the change backward compatible?
- Are there tests for the main use cases?
- Is a version bump or changelog entry needed?

Ask owners of the main consumers to review, or run their tests. For a breaking change, plan a migration instead of updating every user in one huge PR.

## 295: How do you review a PR when you know nothing about that part of the code?

Start with the description and ticket. Then read the code around the change, not just the diff, and look at how the changed functions are called. Check the history with `git log` on the files to see recent changes and their PRs.

Be honest in your review about what you could and couldn't judge. If the area is risky, ask the author for a short walkthrough or ask someone who knows it to also review.

## 296: What should a review summary comment include?

When submitting a review, a short top-level comment helps the author:

```text
Overall this looks good and the approach makes sense. Two blocking
things: the missing authorization check on /export and the migration
locking the orders table. The rest are nits. Happy to pair on the
migration if that helps.
```

It gives the verdict, the main points and the tone, so the author doesn't have to work it out from 15 inline comments.

## 297: How do you review a regular expression in a PR?

Regexes are hard to read, so:

- Ask for a comment explaining what it should match, with examples.
- Check that tests cover matching and non-matching cases, including edge cases.
- Check anchors (`^` and `$`), so it doesn't match part of a longer string by accident.
- Watch for nested quantifiers like `(a+)+`, which can be very slow on some inputs.

```ts
// Matches "abc123" but also "xxabc123yy" without anchors
const ok = /^[a-z]+\d+$/.test(input);
```

If a regex is long, ask whether a few lines of normal code would be clearer.

## 298: What should you check when a PR adds analytics or tracking events?

- Are event names and properties consistent with existing ones?
- Is personal data being sent to the analytics tool?
- Does tracking respect user consent settings?
- Will a failure in the analytics call break the feature?
- Has the product or data team agreed on the event?

Analytics events are often added in a hurry and become a mess. A quick review keeps them useful and legal.

## 299: Should one-off scripts and data fixes be reviewed?

Yes, often more carefully than normal code. A script that updates production data can do a lot of damage in one run and may not be reversible. Check:

- Does it have a dry-run mode?
- Is it limited to the right rows (`WHERE` clause, IDs)?
- Is it idempotent, so running it twice is safe?
- Is there a backup or a way to undo?
- Does it log what it changed?

## 300: How can you keep improving as a reviewer over time?

- Look at bugs that reached production and ask whether review could have caught them.
- Read other people's reviews, especially from strong reviewers.
- Ask authors for feedback on your comments.
- Keep a personal list of things you often miss.
- Learn the areas you review most, like security or databases, in more depth.

Reviewing well is a skill like any other. It improves with practice and feedback.

# Advanced Questions (301-450)

## 301: What kinds of problems do code reviews actually find, according to research?

Studies of real reviews show that most issues found are not functional bugs but "evolvability" problems: readability, naming, structure, documentation and so on. Mäntylä and Lassenius (2009) found roughly three quarters of the issues found in reviews were of this kind.

Bacchelli and Bird's study at Microsoft (2013) showed a gap between what developers expect (finding bugs) and what reviews mostly deliver (code improvements, knowledge transfer, team awareness). That doesn't make review less valuable. It means you should set it up for those benefits and not expect it to replace testing.

## 302: What did the Cisco code review study find?

SmartBear ran a study at Cisco covering about 2,500 reviews. The main findings, often quoted as guidelines:

- Review fewer than about 200-400 lines at a time.
- Go slower than about 500 lines per hour; faster reviews find far fewer defects.
- Don't review for more than 60-90 minutes without a break.
- Author preparation (annotating their own code) reduced the number of defects.

The exact numbers came from one company and one tool, so treat them as rough guidance, not laws. The trend (smaller, slower, shorter sessions find more) has held up well.

## 303: Which code review metrics can do more harm than good?

- **Comments per review** as a quality target: people start leaving useless comments.
- **Reviews done per person** as a performance score: people rubber-stamp to increase the count.
- **Defects found per reviewer**: discourages authors from self-reviewing and creates conflict.
- **Lines of code reviewed**: rewards big PRs.

This is Goodhart's law: when a measure becomes a target, it stops being a good measure. Use metrics to find process problems at the team level, not to rank people.

## 304: How does code review relate to the DORA metrics?

The DORA metrics measure delivery performance: deployment frequency, lead time for changes, change failure rate and time to restore service. Code review affects both sides:

- Slow reviews increase lead time and reduce deployment frequency.
- Good reviews can lower change failure rate.

DORA research has found that teams with lightweight, fast review processes tend to do better than teams relying on heavy external approval (like change advisory boards). The lesson: fast peer review, plus automation, beats slow formal gates.

## 305: Why does review latency hurt more than it seems?

A PR waiting a day for review doesn't only cost one day. The author switches to another task, then has to switch back. The branch drifts and gets conflicts. Authors start making bigger PRs to "make the wait worth it", which makes reviews slower again.

Little's law says average lead time = work in progress / throughput. With many PRs waiting, lead time grows even if everyone is busy. Teams that limit open PRs and review before starting new work often finish more.

## 306: How would you design a code review process for a team growing from 10 to 100 engineers?

- **Ownership**: introduce CODEOWNERS per team and area, so reviews route automatically.
- **Written guidelines**: response times, PR size, comment labels, disagreement process.
- **Automation**: formatters, linters, type checks, security scans and PR checks in CI.
- **Tiered rules**: one approval for most code, two or specific owners for risky areas.
- **Metrics**: watch time to first review and load per reviewer by team.
- **Training**: onboarding on reviewing, shadow reviews for new people.

Revisit the rules every few months. What works at 10 people often breaks at 50.

## 307: What review process makes sense for a startup of three engineers?

Keep it light. One approval from either of the other two, required CI checks, and a formatter and linter so reviews stay about logic. Allow small fixes (typos, config tweaks) to be merged and shown afterward, Ship/Show/Ask style.

The main goals at this size are shared knowledge (everyone should know every part) and speed. Heavy rules like two approvals or required design docs for everything would slow the company more than they help.

## 308: How does code review work in regulated industries?

Standards like SOC 2, PCI DSS, SOX (for financial reporting systems) and HIPAA-related audits often expect proof that changes are reviewed by someone other than the author before reaching production. Typical requirements:

- Every change goes through a PR with at least one independent approval.
- Branch protection can't be bypassed, or bypasses are logged and reviewed.
- An audit trail links each deploy to an approved change.
- Access to merge and deploy is limited.

Peer review in the PR tool usually satisfies this, as long as the settings enforce it and the evidence is kept.

## 309: How do you prevent people from approving their own changes?

- GitHub never counts the author's own approval, but someone could push commits to another person's PR and have them approve, or approve a PR containing their own commits. "Require approval of the most recent reviewable push" closes part of this.
- GitLab has settings to block approval by the author and by anyone who added commits.
- Limit who can bypass branch protection, and log every bypass.
- Don't give everyone admin rights on repos.

For compliance, it also matters that one person can't approve and deploy their own change through a side door, like a manual deploy script.

## 310: What makes a good audit trail for code changes?

For each production change, you should be able to answer: who wrote it, who reviewed and approved it, what CI checks passed, when it was deployed, and which ticket or reason it belongs to.

This comes from linking tools together: PRs with required approvals, protected branches, signed or verified commits, CI logs, deploy logs that reference commit SHAs, and ticket links. Squash merge with the PR number in the commit message makes the trail easy to follow.

## 311: How do you handle code review in a large monorepo with many owners?

- Fine-grained CODEOWNERS so each team only reviews its own folders.
- Avoid catch-all owners that get pinged on every PR.
- Encourage PRs that stay within one team's area, splitting cross-cutting ones.
- Provide a small group of global approvers for mechanical changes across everything.
- Use tooling to run only the affected tests, so CI stays fast.

A common pain is a PR that needs approval from ten teams. Policies for "large-scale changes" (next questions) help with that.

## 312: How does Google's code review process work?

From Google's public docs and talks: every change (CL) needs approval from someone who owns the code (listed in `OWNERS` files) and someone with "readability" in the language used, which is a certification that the person knows Google's style for that language. One person can satisfy both. Reviews are expected to be quick, and CLs are small.

Many teams outside Google copied parts of this: owners files, small changes, fast responses and the "approve if it improves code health" standard.

## 313: How do teams review large-scale changes that touch thousands of files?

Large-scale changes (like an API migration across a whole monorepo) can't get a normal review from every owner. Common approaches:

- Review and approve the tool or codemod once, centrally.
- Split the change into many small PRs, one per team or directory, generated automatically.
- Let a small group of global approvers approve mechanical changes.
- Give owners a window to object, then merge.

Google described this as its "LSC" process. The key idea: review the method and a sample, not every file.

## 314: How do you roll out a breaking API change across many consumers?

1. Add the new version or field alongside the old one.
2. Mark the old one as deprecated, with clear docs and logs or metrics showing who still uses it.
3. Migrate consumers, ideally with PRs to each of them.
4. Watch usage drop to zero.
5. Remove the old one.

In review, reject PRs that remove the old API in the same step as adding the new one, unless you're sure nobody else uses it.

## 315: How do you review code for idempotency?

An operation is idempotent if doing it twice has the same effect as doing it once. This matters for retries, webhooks and queue consumers, which can deliver the same request more than once.

```ts
// Not idempotent: a retry charges twice
await payments.charge(order.total);

// Idempotent: the provider dedupes by key
await payments.charge(order.total, { idempotencyKey: `order-${order.id}` });
```

In review, ask "what happens if this runs twice?" for every handler that changes state.

## 316: What should you check about transactions in a review?

- Are related writes in one transaction, so a failure doesn't leave half the data changed?
- Are external calls (HTTP, emails) made inside a transaction? They can't be rolled back and keep the transaction open longer.
- Is the transaction kept short to avoid lock contention?
- Is the isolation level right for the logic?

```ts
await db.$transaction(async (tx) => {
  await tx.account.update({
    where: { id: from },
    data: { balance: { decrement: amount } },
  });
  await tx.account.update({
    where: { id: to },
    data: { balance: { increment: amount } },
  });
});
```

## 317: How do you spot a check-then-act race condition in a review?

The pattern is: read something, decide based on it, then write, with no protection in between.

```ts
const existing = await db.user.findUnique({ where: { email } });
if (!existing) {
  await db.user.create({ data: { email } }); // two requests can both get here
}
```

Fixes: a unique constraint in the database (and handle the conflict error), an atomic upsert, or a lock. The database constraint is the most reliable, because it works no matter how many servers run the code.

## 318: What is optimistic concurrency and when should a reviewer suggest it?

Optimistic concurrency stores a version number (or updated timestamp) on each row. An update only succeeds if the version hasn't changed since it was read:

```sql
UPDATE documents
SET body = $1, version = version + 1
WHERE id = $2 AND version = $3;
-- 0 rows updated means someone else changed it first
```

Suggest it when users can edit the same record at the same time and silent "last write wins" would lose data, like in editors, admin panels or inventory.

## 319: What makes a database migration dangerous on a large table?

Some operations take locks that block reads or writes while they run, which can take minutes or hours on a big table. In PostgreSQL, examples include:

- Creating an index without `CONCURRENTLY`.
- Adding a foreign key or check constraint without `NOT VALID` first.
- Changing a column's type in a way that rewrites the table.
- Any migration that waits for a lock behind a long-running query, blocking everything queued after it.

Reviewers should ask how big the table is and whether a `lock_timeout` is set. Tools like strong_migrations (Rails) or squawk (Postgres linter) catch many of these.

## 320: What is the expand and contract pattern for schema changes?

It's a way to change a schema without downtime, in steps that each stay compatible with the running code:

1. **Expand**: add the new column or table. Old code ignores it.
2. Deploy code that writes to both old and new.
3. Backfill old rows.
4. Deploy code that reads from the new one.
5. **Contract**: stop writing the old one, then drop it.

In review, a PR that renames a column in one step is a red flag, because old instances still running during the deploy will break.

## 321: What should you check when reviewing a data backfill?

- Does it run in batches, instead of one giant update that locks the table?
- Can it be stopped and resumed safely?
- Is it idempotent?
- Does it throttle itself to avoid overloading the database or replicas?
- How long will it take on production data?
- How do we verify it worked?

```sql
UPDATE users SET plan = 'free'
WHERE id IN (SELECT id FROM users WHERE plan IS NULL LIMIT 1000);
-- repeat until 0 rows updated
```

## 322: What cache problems should reviewers look for at scale?

- **Stale data**: invalidation missed on one of the write paths.
- **Cache stampede**: a popular key expires and hundreds of requests hit the database at once. Fixes: locking, early refresh, or random expiry jitter.
- **Unbounded growth**: an in-memory cache with no size limit.
- **Key collisions**: keys missing a tenant or user part.
- **Caching errors**: storing a failed response as if it were valid.

Ask the author to list every place that writes the cached data and check that each one invalidates it.

## 323: What should you check when reviewing a message queue consumer?

Most queues deliver messages at least once, so the same message can arrive twice. Check:

- Is processing idempotent (dedupe by message ID, or naturally safe)?
- Is the message acknowledged only after processing succeeds?
- What happens with a message that always fails? Is there a dead letter queue?
- Is the order of messages assumed? Many queues don't guarantee it.
- Can the consumer handle old and new message formats?

## 324: Why should retries use exponential backoff and jitter?

If a service is struggling and every client retries immediately, the retries add more load and keep it down. Exponential backoff waits longer after each failure. Jitter adds randomness so clients don't all retry at the same moment.

```ts
async function withRetry<T>(fn: () => Promise<T>, attempts = 5): Promise<T> {
  for (let i = 0; ; i++) {
    try {
      return await fn();
    } catch (err) {
      if (i >= attempts - 1) throw err;
      const delay = Math.random() * Math.min(10_000, 200 * 2 ** i);
      await new Promise((r) => setTimeout(r, delay));
    }
  }
}
```

In review, also check that only retryable errors are retried (not a 400 Bad Request).

## 325: How do you review code for cascading failures?

A cascading failure happens when one slow or failing service makes its callers slow or fail, and so on up the chain. Look for:

- Calls without timeouts.
- Unlimited retries.
- No fallback when an optional dependency is down (could we show the page without recommendations?).
- Connection pools that can be fully used up by one slow dependency.
- No circuit breaker for calls to an unreliable service.

Ask: "If this dependency takes 30 seconds to respond, what happens to our service?"

## 326: What memory leak patterns should you look for in Node.js code?

- Event listeners added on every request and never removed.
- In-memory caches or maps that grow forever.
- Timers (`setInterval`) that are never cleared.
- Closures holding references to large objects longer than needed.
- Storing request data on module-level arrays for "debugging".

```ts
// Adds a new listener per request, never removed
app.get("/stream", (req, res) => {
  emitter.on("update", (data) => res.write(data));
});
```

The fix here is to remove the listener when the request closes (`req.on("close", ...)`).

## 327: What front-end performance issues should reviewers look for?

- Large new dependencies added to the main bundle.
- Components re-rendering on every keystroke because of new objects or functions in props.
- Long lists rendered without virtualization.
- Images without sizes, lazy loading or modern formats.
- Data fetched in a waterfall (one request waits for another unnecessarily).
- Layout shifts from content loading without reserved space.

Ask for a Lighthouse or Web Vitals comparison when a change affects a key page.

## 328: How can bundle size be checked as part of code review?

Add a CI step that measures the build output and comments on the PR with the size change. Tools like size-limit let you set budgets per entry point and fail the build when they're exceeded.

```json
{
  "size-limit": [{ "path": "dist/index.js", "limit": "120 kB" }]
}
```

This turns "did this make the app slower to load?" into a number the reviewer can see, instead of something nobody notices until users complain.

## 329: How do you spot an SSRF risk in a code review?

SSRF (server-side request forgery) happens when the server fetches a URL that the user controls. Attackers can make it call internal services or cloud metadata endpoints.

```ts
// Risky
app.post("/preview", async (req, res) => {
  const page = await fetch(req.body.url);
  res.send(await page.text());
});
```

In review, look for any `fetch`, HTTP client or image processor taking a user-provided URL. Ask for an allowlist of domains, blocking private IP ranges (after DNS resolution), and disabling redirects or re-checking them.

## 330: What is prototype pollution and how do you spot it in a review?

Prototype pollution is when user input sets properties like `__proto__` or `constructor.prototype` through a merge or path-setting function, changing behavior of all objects in the app.

Look for:

- Custom deep merge or "set by path" functions applied to user input.
- Objects used as maps with user-controlled keys.

Safer options: validate input with a schema, use `Map` for user-keyed data, create objects with `Object.create(null)`, and reject keys like `__proto__`, `constructor` and `prototype`.

## 331: What should reviewers check in code that uses cryptography?

- No home-made crypto or custom algorithms.
- Passwords hashed with a slow password hash (Argon2, bcrypt, scrypt), not SHA-256 or MD5.
- Random tokens made with `crypto.randomBytes` or `crypto.randomUUID`, not `Math.random`.
- Secrets compared with a constant-time function (`crypto.timingSafeEqual`).
- Modern algorithms and modes (for example AES-GCM), with unique IVs or nonces.
- Keys loaded from a secret manager, not hard-coded.

When in doubt, ask someone with security experience to review.

## 332: What mistakes in JWT handling should reviewers catch?

- Decoding the token without verifying the signature (`jwt.decode` instead of `jwt.verify`).
- Accepting any algorithm, including `none`. Always pass the expected algorithms.
- Not checking `exp`, `iss` and `aud`.
- Long-lived tokens with no way to revoke them.
- Storing sensitive data in the payload, which is only encoded, not encrypted.

```ts
const payload = jwt.verify(token, publicKey, {
  algorithms: ["RS256"],
  issuer: "https://auth.example.com",
  audience: "api",
});
```

## 333: What should you check when a PR changes CORS or CSRF settings?

CORS:

- `Access-Control-Allow-Origin` reflecting any request origin, especially with `Access-Control-Allow-Credentials: true`, lets any site make logged-in requests and read the responses.
- Use an explicit allowlist of origins.

CSRF:

- Cookie-based auth needs protection: `SameSite` cookies, CSRF tokens or checking the `Origin` header.
- State-changing actions should never use `GET`.

These settings are easy to loosen "just to make it work", so any change to them deserves a careful look.

## 334: Where can XSS still happen in a React app?

React escapes text by default, but XSS is still possible through:

- `dangerouslySetInnerHTML` with unsanitized content.
- `href` or `src` values from users, like `javascript:` URLs.
- Building HTML strings for third-party libraries or `innerHTML` in refs.
- Server-rendered data inserted into a `<script>` tag without proper escaping.

```tsx
// Needs sanitizing, for example with DOMPurify
<div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(comment.html) }} />
```

Search the diff for these patterns in every front-end review.

## 335: What is ReDoS and how do you catch it in review?

ReDoS (regular expression denial of service) happens when a regex takes exponential time on certain inputs, usually because of nested or overlapping quantifiers like `(a+)+` or `(\w+\s?)*$`. One request with a crafted string can block a Node.js server's event loop.

In review, be careful with regexes applied to user input. Look for nested quantifiers and alternations that can match the same text. Limit input length before matching, and use tools like the `eslint-plugin-regexp` rules or a ReDoS checker.

## 336: How do you spot a path traversal bug in a review?

Look for file paths built from user input:

```ts
// ../../etc/passwd escapes the uploads folder
const file = path.join(UPLOAD_DIR, req.params.name);
res.sendFile(file);
```

Fix: resolve the full path and check it's still inside the allowed folder, or better, look files up by an ID in the database instead of using names from the request.

```ts
const full = path.resolve(UPLOAD_DIR, req.params.name);
if (!full.startsWith(path.resolve(UPLOAD_DIR) + path.sep)) {
  return res.status(400).end();
}
```

## 337: Can SQL injection happen when using an ORM?

Yes. ORMs protect normal queries, but most have raw query features, and those can be misused:

```ts
// Prisma: safe, uses a tagged template with parameters
await prisma.$queryRaw`SELECT * FROM users WHERE email = ${email}`;

// Prisma: unsafe, builds a string
await prisma.$queryRawUnsafe(`SELECT * FROM users WHERE email = '${email}'`);
```

Also watch for user input used as column names or sort fields, which can't be parameterized. Those should be checked against an allowlist.

## 338: How can a malicious change get past code review?

- Hidden in a large PR or a "refactor" where reviewers skim.
- Hidden in generated files, lockfiles, minified code or test fixtures.
- Using look-alike Unicode characters or hidden bidirectional text ("Trojan Source").
- Through a trusted contributor who built reputation first. The 2024 xz-utils backdoor is a well-known example, where the malicious code was hidden in test files and build scripts.
- Through changes to CI config or build scripts that get less attention.

Defenses: small PRs, extra scrutiny for build and CI files, reproducible builds, and not treating trust as a reason to skip review.

## 339: Why are PRs from forks a security concern for CI?

Code in a PR from a fork is untrusted. If CI runs it with access to secrets, an attacker can open a PR that prints or sends the secrets somewhere. GitHub limits this by default: workflows triggered by `pull_request` from forks don't get secrets, and first-time contributors' workflows need approval to run.

Problems start with `pull_request_target` or `workflow_run` workflows that check out and run the fork's code with secrets available. Reviewers of workflow files should watch for exactly that combination.

## 340: What is typosquatting and how can review catch it?

Typosquatting is publishing a malicious package with a name close to a popular one, like `reqeusts` or `lodahs`, hoping someone mistypes it. Similar tricks include dependency confusion, where a public package uses the same name as a private internal one.

In review, read new dependency names carefully, check the package page (downloads, author, repository link), and be suspicious of packages that were published very recently. Scoped private packages and a registry config that pins scopes to your internal registry help against dependency confusion.

## 341: Why should reviewers care about install scripts in dependencies?

npm packages can define `preinstall`, `install` and `postinstall` scripts that run automatically on `npm install`, with the developer's or CI's permissions. Malicious packages use this to steal tokens and SSH keys.

When a PR adds a dependency, check whether it (or new transitive dependencies) has install scripts. Some teams run installs with `--ignore-scripts` by default and allow scripts only for packages that need them. pnpm, for example, doesn't run dependency build scripts unless they're allowed in config.

## 342: When should a security team be involved in code review?

- Changes to authentication, sessions, passwords or permissions.
- New handling of payment data, health data or other sensitive personal data.
- Cryptography.
- New public endpoints, file uploads or integrations that accept outside input.
- Changes to security headers, CORS, CSP or network rules.
- Anything flagged by a threat model.

CODEOWNERS can route these paths to the security team automatically. Most normal PRs shouldn't need them, or the security team becomes a bottleneck.

## 343: How can you do lightweight threat modeling during a review?

For a risky change, ask a few questions:

- What new input does this accept, and from whom?
- What could an attacker do with it?
- What data does it touch, and who should be able to see it?
- What happens if a dependency or service it calls is compromised?
- How would we notice an attack?

Writing a few lines of answers in the PR description takes minutes and often finds missing checks before they ship.

## 344: What privacy issues should reviewers check for?

- Collecting personal data that isn't needed.
- Storing personal data without a retention or deletion plan.
- Sending personal data to third parties (analytics, logging, error tracking) without need or consent.
- Missing support for users' rights, like data export or deletion under GDPR.
- Personal data in URLs, which ends up in logs and browser history.

Ask: "Do we need this data, and who can see it?" Privacy problems are much easier to prevent in review than to clean up later.

## 345: How do you manage feature flag debt through code review?

Flags pile up if nobody removes them. Review practices that help:

- Each new flag PR includes an owner and an expected removal date or ticket.
- Lint rules or scripts that list flags older than a certain age.
- A team habit of reviewing flags regularly and opening removal PRs.
- Avoiding flags nested inside other flags, which multiply code paths.

A reviewer can reasonably ask "when will this flag be removed?" on every flag-adding PR.

## 346: What should you check when a PR changes alerts or monitoring?

- Will the alert fire on real problems and stay quiet otherwise?
- Is the threshold based on data, not a guess?
- Does it alert on symptoms users feel (error rate, latency) rather than every internal cause?
- Does the alert link to a runbook or dashboard?
- Who gets paged, and is that right?

Noisy alerts get ignored, which is as bad as having none. Removing alerts also needs review, because it can hide real problems.

## 347: How do you review IAM and permission changes in cloud infrastructure?

Look for least privilege:

- Wildcards like `"Action": "*"` or `"Resource": "*"`.
- Permissions broader than the feature needs (full S3 access when it only reads one bucket).
- Roles that can create or change other roles, which allows privilege escalation.
- Public access to storage or databases.
- Long-lived access keys instead of roles or short-lived credentials.

```json
{
  "Effect": "Allow",
  "Action": ["s3:GetObject"],
  "Resource": "arn:aws:s3:::invoices-bucket/*"
}
```

## 348: What should you check when reviewing Kubernetes manifests?

- Resource requests and limits for CPU and memory.
- Liveness and readiness probes that check the right things.
- Running as non-root, with a read-only root filesystem where possible.
- Image tags pinned (not `latest`).
- Secrets from Secret objects or an external secret manager, not plain env values in the manifest.
- Replica counts and a PodDisruptionBudget for important services.

A bad readiness probe can take a whole service out of rotation, so probes deserve real attention.

## 349: How do canary releases and progressive delivery change what reviewers worry about?

When changes go to a small percentage of users first, with automatic rollback on bad metrics, the cost of a missed bug is smaller. Reviewers can be a bit more relaxed about rare edge cases and focus on things a canary won't catch:

- Data corruption and irreversible changes.
- Security problems.
- Changes to shared formats that affect old and new versions running side by side.

Review and progressive delivery work together. Neither replaces the other.

## 350: How should a PR that fixes an incident be reviewed?

- Does it fix the root cause, or only the symptom seen in this incident?
- Is there a test that reproduces the incident?
- Does it link to the incident or postmortem doc?
- Are there similar patterns elsewhere in the code that need the same fix?
- Was any monitoring added so the problem would be seen sooner next time?

The emergency fix during the incident may have been minimal. The follow-up PR is the place to do it properly.

## 351: How is an architecture review different from a code review?

An architecture review looks at the structure of a system before (or apart from) the code: which services exist, how data flows, what databases and protocols are used, how it scales and fails. A code review looks at a specific change and whether it's correct and clean.

Architecture decisions are expensive to change, so they should be reviewed early, in a design doc or meeting. If big architecture questions first come up in a code review, the process has a gap.

## 352: Why is a code review often the wrong place for design feedback?

By the time code is written, the author has invested days. Saying "this whole approach is wrong" at that point wastes their work, causes frustration and often leads to a compromise nobody likes.

The fix is upstream: short design discussions for anything non-trivial, draft PRs for early direction checks, and pairing on the first part of a big feature. If design feedback in code review still happens often, look at why it wasn't raised earlier.

## 353: What does a lightweight design review look like?

A one or two page doc with:

- The problem and goals (and non-goals).
- The proposed approach, with a simple diagram if helpful.
- Alternatives considered and why they weren't chosen.
- Risks, open questions and how it will be rolled out.

Share it with two or three relevant people, give a few days for comments, and hold a short meeting only if needed. It should take hours, not weeks.

## 354: What should you check when reviewing a REST API design?

- Resource-based URLs with nouns (`/orders/123/items`), not verbs.
- Correct methods: `GET` safe, `PUT` and `DELETE` idempotent, `POST` for creation or actions.
- Consistent naming and casing across endpoints.
- Clear error format, ideally standard like RFC 9457 problem details.
- Pagination, filtering and sorting for collections.
- A versioning approach that matches the rest of the API.
- No internal details (database IDs or column names) leaking where they shouldn't.

## 355: What should you check when reviewing GraphQL schema changes?

- Removing or renaming fields breaks clients; deprecate with `@deprecated` first.
- Changing a nullable field to non-null in an output type is safe for clients, but the reverse breaks them; for input arguments it's the opposite.
- New fields that can trigger expensive queries or N+1 problems in resolvers (DataLoader helps).
- Authorization at the field or resolver level.
- Query depth and complexity limits for public APIs.

Schema checks in CI (like GraphQL Inspector or a schema registry) can flag breaking changes automatically.

## 356: How does semantic versioning affect library code review?

With semver, version numbers are MAJOR.MINOR.PATCH. Breaking changes need a major bump, new backward-compatible features a minor, and fixes a patch.

In review of a library, check that the change matches the planned bump. Things that are breaking but easy to miss: changing TypeScript types in an incompatible way, changing default option values, dropping support for an older Node.js version, changing what's exported, or changing thrown error types.

## 357: How should deprecations be handled and reviewed?

A good deprecation:

- Marks the old API in code (`@deprecated` in JSDoc shows strikethrough in editors).
- Explains what to use instead.
- Gives a timeline for removal.
- Optionally logs a warning when the old API is used, so usage can be tracked.

```ts
/** @deprecated Use getUserById instead. Will be removed in v5. */
export function fetchUser(id: string) {
  return getUserById(id);
}
```

Removal PRs should only come after usage is confirmed gone.

## 358: Why should error responses be treated as part of the API contract?

Clients write code that depends on error status codes and error shapes, like showing a field error when they get a 422 with a certain format. Changing these breaks clients just as much as changing successful responses.

In review, check that new errors follow the existing format, that status codes are consistent, and that error codes or types are stable and documented. Don't change a 404 to a 403 or rename an error code without treating it as a breaking change.

## 359: How do you review front-end code for stale responses?

When a user types quickly or changes filters, older requests can return after newer ones and overwrite the correct data.

```tsx
useEffect(() => {
  const controller = new AbortController();
  fetch(`/api/search?q=${encodeURIComponent(query)}`, {
    signal: controller.signal,
  })
    .then((r) => r.json())
    .then(setResults)
    .catch((err) => {
      if (err.name !== "AbortError") setError(err);
    });
  return () => controller.abort();
}, [query]);
```

Look for fetches in effects or event handlers without cancellation or an "ignore if outdated" check. Data libraries like TanStack Query handle this for you.

## 360: What should you check when reviewing optimistic UI updates?

Optimistic updates show the result before the server confirms it. Check:

- What happens when the request fails? Is the UI rolled back and the user told?
- Can two quick actions conflict (like double-clicking "like")?
- Does the final server response replace the optimistic data?
- Is the optimistic state realistic (for example, temporary IDs for new items)?

A missing rollback means the UI shows something that never happened, which users find very confusing.

## 361: What should you look for in server-rendered React code during review?

- Code that behaves differently on server and client, like reading `window`, `localStorage`, `Date.now()` or random values during render, which causes hydration mismatches.
- Secrets or server-only code being imported into client components.
- Data fetching that leaks one user's data into a cached page shared by others.
- Large data passed from server to client that bloats the HTML.

In Next.js with React Server Components, check the `"use client"` boundaries: are they placed so most code stays on the server?

## 362: What internationalization edge cases should advanced reviewers catch?

- Plurals: languages have different plural rules, so `count + " items"` breaks. Use ICU message format or `Intl.PluralRules`.
- Concatenating translated pieces, which breaks word order in other languages.
- Right-to-left languages: use logical CSS properties (`margin-inline-start`) instead of `margin-left`.
- Text expansion: German or Finnish can be much longer than English.
- Sorting and comparing strings with `Intl.Collator` instead of `<`.

## 363: What time zone and date bugs should reviewers look for?

- Storing local times instead of UTC (or instead of a time plus a time zone when the local time matters, like meetings).
- Assuming a day has 24 hours; daylight saving days have 23 or 25.
- Parsing date strings without a time zone, which depends on the server's settings.
- Comparing dates as strings in different formats.
- "End of day" logic that ignores the user's time zone.

```ts
new Date("2026-03-29"); // UTC midnight
new Date("2026-03-29T00:00"); // local midnight, different value
```

Using a solid date library or the `Temporal` API where available helps a lot.

## 364: Why should money not be stored as floating point numbers?

Floating point can't represent many decimal values exactly:

```ts
0.1 + 0.2; // 0.30000000000000004
```

For money, store amounts as integers in the smallest unit (cents) or use a decimal type in the database (like `NUMERIC` in PostgreSQL) and a decimal library in code. Also check rounding rules, currency per amount, and that totals are calculated the same way everywhere.

## 365: What Unicode problems can reviewers catch?

- String length: `"👍".length` is 2 in JavaScript, so length limits and truncation can split characters.
- Comparing strings that look the same but have different Unicode forms; normalize with `str.normalize("NFC")`.
- Case-insensitive comparison using `toLowerCase()` for all languages (Turkish dotted i is a known problem).
- Look-alike characters in usernames or domains used for impersonation.
- Database columns and connections not using full UTF-8 (in MySQL, `utf8mb4`).

## 366: How do you review a large refactor done with the strangler fig pattern?

The strangler fig approach replaces an old system piece by piece, routing more traffic or features to the new code over time. Each PR should:

- Move one well-defined piece.
- Keep both paths working until the switch.
- Have a way to switch back (flag or routing rule).
- Compare old and new behavior where possible, for example with tests or by running both and comparing results.

Review the plan as a whole once, then review each step as a small PR.

## 367: How should a team review a proposal to rewrite a system from scratch?

Be skeptical and ask for evidence:

- What specific problems does the current system have, and why can't they be fixed in place?
- How will the rewrite reach feature parity, including all the hidden edge cases?
- How will users move over? Can it be done incrementally?
- What's the plan if it takes twice as long?

Full rewrites often take much longer than planned and lose behavior nobody wrote down. Incremental replacement is usually safer.

## 368: How do you judge the balance of test types in a PR?

Look at what each test type is good at:

- Unit tests for logic with many cases.
- Integration tests for how parts work together, like the API plus database.
- End-to-end tests for a few key user flows.

Red flags: a complex calculation tested only through one E2E test, or an API endpoint tested only with mocks so the real SQL is never run. Ask for the cheapest test that would actually catch the likely bugs.

## 369: What are the problems with snapshot tests and how should they be reviewed?

Snapshot tests save output (like rendered HTML) and fail when it changes. Problems:

- Huge snapshots nobody reads, so changes get accepted with `-u` without thought.
- They break on every small change, so people stop trusting them.
- They don't say what behavior matters.

In review, look at snapshot diffs, not only the code. Prefer small, focused snapshots or explicit assertions. A snapshot of a whole page is rarely useful.

## 370: What should you check when a PR adds end-to-end tests?

- Does it test an important user flow, not a detail better covered by unit tests?
- Does it use stable selectors (roles, labels, test IDs) instead of CSS classes?
- Does it wait for real conditions instead of fixed sleeps?
- Is test data set up and cleaned up properly, so tests don't depend on each other?
- How much does it add to CI time?

```ts
await page.getByRole("button", { name: "Place order" }).click();
await expect(page.getByText("Order confirmed")).toBeVisible();
```

## 371: How should test data and fixtures be reviewed?

- Is the data minimal and focused on what the test checks?
- Is it built with factories or builders, so tests show only the relevant fields?
- Is shared fixture data changed in a way that affects other tests?
- Does it contain real personal data copied from production? It shouldn't.
- Are random values used in a way that makes failures hard to reproduce?

```ts
const order = buildOrder({ status: "paid" }); // only the field that matters
```

## 372: What is mutation testing and how can it help reviews?

Mutation testing tools (like Stryker for JavaScript) change the code in small ways, such as flipping `>` to `>=` or removing a line, and run the tests. If tests still pass, that "mutant survived", meaning the tests didn't catch the change.

It's a much stronger signal of test quality than line coverage. Running it on changed files in CI, or for critical modules, gives reviewers concrete data about weak tests.

## 373: How do you review code that you can't easily run?

Examples: infrastructure, payment provider integrations, code that depends on production-only data or hardware. Approaches:

- Ask how the author tested it, and for evidence (logs, plan output, screenshots).
- Check for dry-run or staging options.
- Review the rollback plan more carefully.
- Ask for extra logging and monitoring for the first deploy.
- Roll out gradually.

When you can't verify behavior, focus even more on making failure safe and visible.

## 374: How do you review concurrent code when tests can't prove it's correct?

Race conditions often don't show up in tests. In review:

- List the shared state and who reads and writes it.
- For each pair of operations, ask what happens if they interleave.
- Prefer designs that avoid shared mutable state: database constraints, atomic operations, single-writer queues.
- Ask for a comment explaining why the code is safe.
- Consider stress tests that run operations in parallel many times.

Simple, obviously correct concurrency is better than clever and probably correct.

## 375: What makes reviewing mentally tiring, and how do you deal with it?

Reviewing means keeping a lot in your head: the goal, the old behavior, the new behavior and the rest of the system. Big PRs, poor descriptions, many small context switches and unfamiliar code all add to the load.

Ways to cope: review at set times instead of constantly, take breaks, ask for smaller PRs and better descriptions, check out the code to navigate it properly, and split big reviews across sessions.

## 376: What is review fatigue and how can teams avoid it?

Review fatigue happens when people have too many reviews, so quality drops: skimming, rubber-stamping and delays. It's common for senior engineers who get most requests.

Fixes: spread reviews more widely, limit how many PRs one person reviews per day, reduce PR size, automate trivial checks, and count reviewing as real work in planning. If a few people are always overloaded, train more reviewers in their areas.

## 377: What cognitive biases affect code reviews?

- **Reputation bias**: trusting senior people's code too much, or newcomers' too little.
- **Anchoring**: the first comment or the description shapes what the reviewer looks for.
- **Confirmation bias**: looking for proof the code works instead of trying to break it.
- **Familiarity**: missing problems in patterns you use yourself.
- **Sunk cost**: approving a flawed approach because a lot of work went into it.

Knowing about these helps. Checklists, focusing on the code instead of the author, and actively asking "how could this fail?" reduce them.

## 378: What does research say about bias in code review?

A well-known study of GitHub pull requests by Terrell and colleagues (2017) found that women's PRs were accepted at a higher rate overall, but for contributors outside the project, the acceptance rate for women dropped when their gender was identifiable from their profile. Other studies have looked at bias based on perceived experience, company or location.

The practical lesson: judge code on its merits, keep review standards written down and consistent, and watch for patterns where some people's PRs consistently get more comments or wait longer.

## 379: What is psychological safety and why does it matter for code review?

Psychological safety means people feel safe to take risks, ask questions and admit mistakes without being embarrassed or punished. In review, it shows up as people opening PRs early, asking "dumb" questions, and saying "I don't understand this".

Without it, people make big PRs to avoid frequent criticism, defend bad code, and reviewers hold back real concerns. Leaders and senior engineers set the tone through how they review and how they respond to feedback on their own code.

## 380: How would you fix a toxic code review culture?

- Talk to the team about what's going wrong, with real (anonymous) examples.
- Write review guidelines: tone, comment labels, what's blocking.
- Have senior people model good reviews and respond well to criticism.
- Address repeated harsh behavior privately and directly; involve a manager if needed.
- Automate style arguments away.
- Check in on how people feel about reviews in retros.

Change takes time. Consistent behavior from leads matters more than any document.

## 381: What is gatekeeping in code review?

Gatekeeping is when a reviewer uses review power to block changes based on personal standards, control, or territory instead of real problems. Signs: one person blocks most PRs in an area, demands their exact style, or makes others wait for their approval even when they aren't needed.

It slows the team and pushes people away. Fixes include more than one owner per area, written standards, and a clear rule that "different from how I'd do it" isn't a reason to block.

## 382: What is nitpick culture and how do you move away from it?

Nitpick culture is when reviews are mostly about tiny style points: spacing, naming preferences, comment wording. It makes reviews slow and annoying, and real problems get less attention.

Steps to move away from it:

- Automate formatting and lint rules.
- Require labeling nits as non-blocking.
- Agree that nits alone never block approval.
- Praise reviews that find real issues, not reviews with many comments.

## 383: How do power dynamics affect code review?

Juniors may hesitate to question seniors, and may accept every senior comment as an order even when they disagree. Seniors' comments can feel like commands when they were meant as suggestions. Managers reviewing their reports' code can make feedback feel like performance evaluation.

Seniors should explicitly invite pushback ("I could be wrong here"), label optional comments, and thank people who challenge them. Teams should make it normal for anyone to review anyone.

## 384: How do you deal with a reviewer who blocks almost every PR?

First, look at whether their concerns are valid. Maybe the PRs really have problems. If not:

- Talk to them privately about the effect on the team.
- Ask them to separate blocking issues from preferences.
- Agree as a team on what's a valid reason to block, and write it down.
- Add more owners for their areas so they aren't the only gate.
- Involve the tech lead or manager if the pattern continues.

## 385: How do you deal with an author who ignores review feedback?

Check whether comments were clear and marked as blocking. If they were:

- Don't approve until blocking issues are addressed, and say so directly.
- Talk to the author outside the PR. Maybe they disagree but don't want to argue in writing, or they're under deadline pressure.
- If they merge without addressing comments (when rules allow it), raise it with the lead.

Branch protection with required approvals and dismissal of stale reviews prevents the worst cases.

## 386: How do you coach someone to become a better reviewer?

- Review their reviews: point out what they missed and what was well done.
- Pair on reviews: go through a PR together, thinking out loud.
- Share good examples of review comments.
- Encourage them to explain the "why" and label importance.
- Give them reviews in areas they're learning, with a second reviewer for safety.

Reviewing is rarely taught directly, so most people learn it by copying others. Make sure they copy good examples.

## 387: What is a review calibration session?

The team reviews the same PR separately, then compares comments. It shows how differently people review: what they catch, what they call blocking, how they phrase things.

Discussing the differences helps the team agree on standards. It's a good activity for new teams, after onboarding several people, or when people complain reviews are inconsistent.

## 388: Should reviews themselves be reviewed?

Occasionally, yes, in a light way. A tech lead can look at a sample of recent reviews to see whether they're timely, useful and kind. Bugs that reached production can be traced back to their PRs to see what review missed.

This should be about improving the process and coaching, not about catching people out. Done with blame, it makes reviewers more defensive and slower.

## 389: How do you onboard someone as a reviewer for a new area of the code?

- Walk them through the area's design and its known pitfalls.
- Have them shadow reviews: they review, but an experienced owner also reviews and they compare.
- Start them on smaller, lower-risk PRs.
- Add them to CODEOWNERS once they're comfortable, with another owner as backup.

This spreads knowledge and reduces dependence on one or two experts.

## 390: What is shadow reviewing?

In shadow reviewing, a newer reviewer reviews a PR alongside an experienced reviewer, whose approval is the one that counts. Afterward, they compare notes: what did the experienced reviewer catch that the new one didn't, and why?

It's a low-risk way to learn the standards of an area. After a few weeks, the new reviewer can review on their own.

## 391: What are different ways to design a review rotation?

- **Round-robin**: the next person in the list gets the next PR.
- **Load-balanced**: whoever has the fewest open reviews gets it.
- **Reviewer of the day/week**: one person handles all first reviews for a period.
- **Area-based**: rotation among owners of a specific area.

GitHub's team review assignment supports round-robin and load balancing. Mixing a rotation with code owners gives both spread and expertise.

## 392: If a team pairs or mobs on code, does it still need pull request reviews?

It depends on the team and the rules they work under. Pairing gives continuous review, so many teams treat a paired change as already reviewed and just need a quick approval from the pair partner.

Compliance rules may still require a separate recorded approval. Also, a fresh pair of eyes catches things a pair missed together. Some teams use a light post-merge review for paired work as a middle ground.

## 393: Is it OK to let senior engineers merge without pre-merge review?

Some teams do it for small changes, using Ship/Show/Ask or post-merge review. The risks: seniors make mistakes too, knowledge sharing drops, and it creates a two-class system that juniors notice.

If you allow it, limit it to low-risk changes, make it visible (Show), keep the same rule for anyone who meets the criteria, and keep pre-merge review for risky areas. In regulated environments it's often not allowed at all.

## 394: How do you decide how deep a review should be?

Match the depth to the risk:

- **Higher risk**: auth, payments, data migrations, public APIs, infrastructure, concurrency, code with no tests, code that's hard to roll back.
- **Lower risk**: copy changes, docs, internal tools, code behind a disabled flag, changes with strong tests.

A risky one-line change to an auth check deserves more time than a 300-line new admin page. Some teams make this formal with labels or required reviewers for high-risk paths.

## 395: How does a stacked diff workflow work in practice?

The author writes several small commits or branches on top of each other, each as its own PR. Tools help with this:

- **Graphite**, **spr** and **ghstack** create and update one GitHub PR per commit or branch.
- **Sapling** (from Meta) and **Gerrit** treat each commit as its own reviewable change.
- `git rebase --update-refs` keeps a chain of local branches in sync when you rebase the bottom one.

Reviewers review each piece on its own, and pieces merge from the bottom up as they're approved.

## 396: What happens when a change is needed in the middle of a PR stack?

The author edits the commit or branch in the middle of the stack, then rebases everything above it. With plain Git:

```bash
git switch part-2
# make changes, commit
git switch part-4
git rebase --update-refs part-2
git push --force-with-lease origin part-3 part-4
```

Stack tools do this automatically. Reviewers of the upper PRs may need to re-check them if the change affects their code. Keeping each piece truly independent reduces this.

## 397: What makes a good commit series for review?

- Each commit is one logical step and has a clear message.
- Each commit builds and passes tests.
- Mechanical changes (renames, moves) are separate from logic changes.
- Preparatory refactors come before the feature that needs them.
- No "fix typo" or "address review" commits in the final series.

A good series reads like a story of the change. It's more work for the author but makes careful review and later debugging much easier.

## 398: How should an author clean up commits before merging?

With interactive rebase:

```bash
git rebase -i main
```

In the editor, use `fixup` or `squash` to fold small fixes into their commits, `reword` to fix messages, and reorder lines to put commits in a logical order. If fixup commits were made with `--fixup`, `git rebase -i --autosquash main` places them automatically.

After rebasing, push with `--force-with-lease`. If the team squash merges anyway, this cleanup isn't needed.

## 399: What does it mean for history to be bisectable, and why do reviewers care?

`git bisect` finds the commit that introduced a bug by testing commits in a binary search. It only works well if every commit on `main` builds and passes tests. Commits like "wip, broken" make bisect stop on false failures.

Reviewers care because a clean, bisectable history makes future debugging much faster. That's one reason teams either squash merge or require each commit in a series to be working.

## 400: How do you review a merge conflict resolution?

Conflict resolutions can quietly drop changes from either side. To review one:

- Look at the merge commit with `git show --remerge-diff <merge-sha>` (Git 2.36+), which shows how the result differs from an automatic merge.
- Check that both sides' intended changes are still there.
- Re-run tests on the merged result.

If the author rebased instead of merging, compare the PR before and after with `git range-diff`. Big resolutions deserve a comment from the author explaining what they chose.

## 401: How should backports and cherry-picks to release branches be reviewed?

- Is the fix really needed on the release branch, and is it safe there?
- Does the cherry-pick apply cleanly, or did it need changes? Changed cherry-picks need a real review, because the older code may be different.
- Are the tests also backported, and do they pass on the release branch?
- Is the original PR linked?

`git cherry-pick -x` adds "(cherry picked from commit ...)" to the message, which makes the link clear in history.

## 402: Should release branches have stricter review rules?

Usually, yes. Close to a release, the risk of any change is higher and there's less time to find problems. Common rules:

- Only bug fixes, no features.
- Approval from a release owner in addition to normal review.
- Every change must first be merged to `main` (so fixes aren't lost in the next release).

Rulesets or branch protection patterns like `release/*` make these rules automatic.

## 403: How do you review a 2,000-line PR that really can't be split?

- Ask for a walkthrough call to understand the structure first.
- Ask the author to mark which files are mechanical and which have real logic.
- Review the risky core carefully and skim the mechanical parts.
- Split the review between people by area, with clear ownership of each part.
- Review commit by commit if the commits are clean.
- Take several sessions, not one.

Be explicit in your approval about what you reviewed in depth and what you only skimmed.

## 404: You approved a PR that later caused a production bug. What do you do?

Help fix it first. Then, without blame, look at what happened:

- Was the bug visible in the diff, or only in interaction with other code?
- Was the PR too big or rushed?
- Would a test, a checklist item or a lint rule have caught it?

Share what you learned with the team. Approving a PR that had a bug is normal; every reviewer does it. What matters is improving the process so the same kind of bug is less likely next time.

## 405: You find a security vulnerability in code that was merged last week. What do you do?

1. Tell the code owner and, if the team has one, the security contact, privately. Don't post details in a public issue or channel.
2. Judge how serious it is: is it deployed, reachable, being exploited?
3. Fix it quickly, possibly through a private fork or security advisory for public repos.
4. Check logs for signs of exploitation.
5. Afterward, look at why review missed it and whether a test or scanner could catch it.

## 406: An author pushes new commits after you approved and merges without re-review. How do you handle it?

First, check what changed. If it's harmless, a quick note is enough: "I saw new commits after my approval. Next time could you ping me for a quick look?" If it's significant, review it now and raise any problems.

Then fix the process: turn on "Dismiss stale pull request approvals" or "Require approval of the most recent reviewable push", so the tool prevents it instead of relying on memory.

## 407: Production is down at 2 AM, you have a fix and no reviewer is awake. What do you do?

Follow the team's incident process. Usually:

- Try to reach the on-call partner or anyone available. Even a 5-minute review over a call helps.
- If nobody is available and the impact is serious, use the emergency bypass if your process allows it, and make the smallest possible change (or a revert).
- Document what you did in the incident channel.
- Get a review first thing in the morning, and fix anything found.

Having this process written down before an incident makes the decision much easier.

## 408: Two reviewers give opposite feedback on your PR. What do you do?

Don't try to satisfy both by going back and forth. Point out the conflict in the PR and tag both:

```text
@ana suggests keeping this in the service layer, @sam suggests moving
it to the controller. I lean toward the service layer because X.
Can you two agree on one, or should we ask Lee to decide?
```

If they can't agree, the code owner or tech lead decides. Make sure the decision is written down, so it doesn't come up again on the next PR.

## 409: A teammate keeps sending huge pull requests. How do you handle it?

Talk to them directly, not through PR comments. Explain the problems (slow reviews, missed bugs, conflicts) and ask what makes small PRs hard for them. Often it's habit, fear of review rounds, or not knowing how to split work.

Offer concrete help: pair on splitting the next one, show feature flags or stacked PRs. Team-level agreements on PR size, with automated size warnings, make it less personal.

## 410: Another team sends a PR into code your team owns. How do you review it?

Welcome it, but review for what you care about as owners: does it fit the design of your area, is it tested, can your team maintain it, does it break any assumptions elsewhere?

Respond quickly, because cross-team PRs often block another team's roadmap. If you don't want the change, explain why and suggest an alternative. For big changes, suggest a short design chat before they write more code.

## 411: While reviewing, you realize the PR implements the wrong requirement. What do you do?

Stop reviewing details and raise it right away, with a top-level comment and a direct message or call:

```text
Before I go further: the ticket says refunds should go back to the
original payment method, but this sends them to account credit. Did
the requirement change, or did I misread it?
```

Maybe the requirement changed and the ticket is outdated. Either way, clear it up with the product owner before any more work is done.

## 412: A reviewer asks for a big rewrite after several review rounds. How should this be handled?

Late big requests are frustrating and often a sign the reviewer only looked closely late. Discuss it openly:

- Is the concern a real problem, or a preference?
- What's the cost of changing now vs later?
- Can the PR merge as is with a follow-up ticket, if it's safe?

If the problem is real (a bug or a design that will be very hard to change), it may be worth doing now. Afterwards, talk about raising design concerns earlier, for example by reviewing drafts.

## 413: A style debate on a PR has gone on for days. How do you end it?

- Move it to a call or the team channel; PR comments are a bad place for it.
- If there's an existing convention, follow it.
- If there isn't, make a decision (tech lead, or a quick team vote), merge the PR, and add the rule to the style guide or a lint rule.
- Remind everyone that blocking a PR for days over style costs much more than either option.

## 414: A junior's first PR has many problems. How do you review it?

Keep it encouraging and focused:

- Start with what's good.
- Pick the few most important issues and explain them well.
- Group small things into one comment, or fix trivial ones together on a call.
- Offer to pair on the bigger changes.
- Link to examples in the codebase and team docs.

Forty comments on a first PR can crush someone's confidence. You can raise the smaller points in their next PRs.

## 415: You find a serious flaw in a senior engineer's PR. How do you raise it?

Directly and respectfully, like with anyone. Explain the flaw with a concrete example of how it fails:

```text
I think this can double-charge: if the webhook is retried after the
DB write but before the response, we process it again. Repro: ...
Am I missing something?
```

Mark it as blocking. Seniors miss things too, and a clear, well-explained comment is what they'd want. If you're worried about the relationship, mention it privately first.

## 416: You're asked to review a PR but you have no time. What do you do?

Say so quickly instead of leaving it hanging:

```text
I'm heads down on the release until Thursday. Could someone else take
this? If not, I can look Friday morning.
```

Or offer a partial review: "I can check the API part today, someone else should review the UI." Silence is the worst option, because the author doesn't know whether to wait or find someone else.

## 417: Review backlog is growing across the whole team. What changes would you make?

- Look at the data: are PRs too big, or are a few people doing all reviews?
- Agree on a review SLA and set daily review times.
- Limit work in progress: review before starting new tasks.
- Spread reviews more widely, train more reviewers.
- Automate trivial checks.
- Ship/Show/Ask for low-risk changes, if allowed.

Bring it up in a retro. A growing backlog is a team problem, not an individual one.

## 418: You're reviewing a PR that changes code you originally wrote. What should you watch for?

Be careful not to defend your old code by habit. The author may have found real problems in it, or the requirements may have changed. Ask yourself whether you'd accept this change if someone else had written the original.

At the same time, you have useful context: share the reasons behind the original design, which may not be obvious. "We did it this way because of X. Does your change still handle X?"

## 419: How do you review code delivered by an outside contractor or agency?

- Agree on standards and review expectations in advance, ideally in the contract.
- Ask for small, frequent PRs, not one big delivery at the end.
- Pay extra attention to security, dependencies, licenses and anything that "phones home".
- Check that tests and docs exist, because the authors may not be around to explain.
- Make sure your team understands the code well enough to maintain it.

## 420: An open source contributor sends a PR you don't want to merge. How do you respond?

Be kind and clear, and do it quickly rather than leaving it open for months:

```text
Thanks a lot for this! We've decided not to add export to CSV in core,
since we want to keep the package small (see #45). A plugin would be
a great home for it, happy to link to it from the README.
```

Give the reason, point to the discussion or guideline, and suggest an alternative if there is one. Then close the PR.

## 421: A PR depends on an unmerged PR in another repository. How should it be reviewed and merged?

- Make the dependency explicit in both PR descriptions, with links.
- Review them together so the reviewer understands the full change.
- Merge in the right order, and make sure the dependent code can handle the period when only one is deployed.
- Better: design the change so each repo's PR is backward compatible and can be merged and deployed on its own.

Requiring two repos to deploy at the exact same time is fragile and should be avoided.

## 422: A flaky test keeps blocking merges. What should the team do?

Don't just keep pressing re-run. Options:

- Quarantine the test: skip it in required checks with a ticket and an owner to fix it soon.
- Find and fix the cause: timing, shared state, test order, external calls.
- Track flaky tests (many CI tools can do this) and treat fixing them as real work.

Letting flakiness grow teaches people to ignore red builds, which means real failures get ignored too.

## 423: The team that owns some code never reviews PRs in time. What do you do?

- Ping them directly in their channel with context and urgency.
- Talk to their lead about expected response times.
- Suggest adding more owners from that team, or a rotation, so it doesn't depend on one person.
- If ownership is unclear or the team is overloaded, raise it as an organizational problem.

Avoid working around required approvals. Fix the cause instead.

## 424: How do you approach a live code review exercise in an interview?

1. Read the whole thing first and say what you think it's supposed to do.
2. Ask about context: language version, expected input, scale.
3. Start with the most serious issues: bugs, security, data loss.
4. Then design and testability, then readability and style.
5. Suggest fixes, not just problems.
6. Mention what you'd ask the author and what tests you'd want.

Interviewers look for prioritization and clear, kind communication, not just the number of issues found.

## 425: What problems can you find in this Express handler?

```ts
app.post("/api/transfer", async (req, res) => {
  const { from, to, amount } = req.body;
  const sender = await db.query(`SELECT * FROM accounts WHERE id = ${from}`);
  if (sender.rows[0].balance >= amount) {
    await db.query(
      `UPDATE accounts SET balance = balance - ${amount} WHERE id = ${from}`,
    );
    await db.query(
      `UPDATE accounts SET balance = balance + ${amount} WHERE id = ${to}`,
    );
  }
  res.send("ok");
});
```

- SQL injection: values put directly into SQL strings.
- No authorization: any caller can move money from any account.
- No validation: negative or non-numeric `amount` values.
- Race condition: two transfers can both pass the balance check.
- No transaction: a failure between the updates loses money.
- Crash if the account doesn't exist (`rows[0]` is undefined).
- Always returns "ok", even when the transfer didn't happen.

## 426: What problems can you find in this React component?

```tsx
function UserList({ teamId }) {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch("/api/teams/" + teamId + "/users")
      .then((r) => r.json())
      .then((data) => setUsers(data));
  });

  return users.map((u, i) => (
    <div key={i} onClick={() => select(u)}>
      {u.name}
    </div>
  ));
}
```

- `useEffect` has no dependency array, so it fetches after every render, and `setUsers` triggers another render: an endless loop of requests.
- No handling of errors or loading state.
- No cancellation, so a slow response for an old `teamId` can overwrite the current one.
- `key={i}` instead of a stable ID like `u.id`.
- Clickable `div` instead of a `button`, so it's not keyboard accessible.
- No types for props in a TypeScript file.

## 427: What problems can you find in this data processing function?

```ts
async function sendReminders() {
  const users = await db.user.findMany();
  for (const user of users) {
    if (user.lastLogin < Date.now() - 30 * 24 * 3600 * 1000) {
      await email.send(user.email, "We miss you!");
    }
  }
}
```

- Loads every user into memory; should filter in the database and process in batches.
- Filtering by date in code instead of a `WHERE` clause.
- Comparing `lastLogin` (probably a `Date`) with a number works in JavaScript but is unclear; be explicit.
- No record of who got the email, so a retry or a second run sends duplicates.
- One failed email stops the whole loop.
- Ignores unsubscribe preferences.
- Sends one email at a time with no rate limiting or parallelism control.

## 428: How can a team tell whether its code reviews are improving quality?

There's no single number, but useful signals are:

- Fewer bugs reaching production in areas with strong review practices.
- Postmortems where review is or isn't mentioned as a missed chance.
- Survey answers: do people find reviews helpful? Do they learn from them?
- Healthy knowledge spread: more people able to work in each area.
- Review time staying reasonable.

Combine numbers with what people say. Metrics alone are easy to game.

## 429: Are there cases where skipping code review is the right call?

Some teams skip it for:

- Pure docs or typo fixes.
- Automated dependency patches that pass tests.
- Experiments and prototypes that won't reach production.
- Changes already done in a pair or mob.

The decision should follow an agreed rule (like Ship/Show/Ask), not individual mood. In regulated environments, skipping may not be allowed at all, so check compliance rules first.

## 430: What is policy as code and how does it relate to code review?

Policy as code means writing rules as code that runs automatically, for example with Open Policy Agent (OPA) and Conftest, or with checks in CI. Examples: "no public S3 buckets", "every container must have resource limits", "PRs touching `payments/` need two approvals".

It moves repeatable checks out of human reviewers' heads and into automated checks, so they're applied consistently. Human reviewers can then focus on things that need judgment.

## 431: Why would a team require signed commits?

Git author names and emails can be set to anything, so anyone can make a commit that looks like it came from someone else. Signed commits (with GPG, SSH or S/MIME keys) prove who made the commit. GitHub shows them as "Verified", and rulesets can require signatures on protected branches.

It matters most where the trail of who changed what has to be trusted: regulated projects, open source projects with many contributors, and supply chain security.

## 432: Can a PR that passed review and CI still break main after merging?

Yes. If two PRs were both tested against an older `main`, each can pass on its own but conflict in behavior when combined, without a Git conflict. For example, one PR renames a function and another adds a new call to the old name.

Fixes: require branches to be up to date before merging, or use a merge queue that tests each PR on top of the latest `main` plus the PRs ahead of it. Running CI on `main` after merge also catches anything that slips through.

## 433: How does peer code review compare to a change advisory board?

A change advisory board (CAB) is a group that approves changes before deployment, common in traditional IT processes. It's usually far from the code, meets on a schedule, and slows releases.

DORA research found that external approval like a CAB was linked to lower delivery performance and didn't reduce failure rates. Peer review by people close to the code, plus automated testing, is usually both faster and safer. Many organizations meet compliance requirements with peer review and automation instead of a CAB.

## 434: What should a team's code review guidelines document include?

- Why the team does reviews.
- PR size expectations and how to split work.
- What a PR description should include.
- Expected response time.
- How to label comments (blocking, nit, optional).
- What reviewers should focus on, and what's left to tools.
- How many approvals, and which areas need specific owners.
- How to handle disagreements and who decides.
- Rules for hotfixes and emergency bypass.

Keep it to a page or two, and link to it from the PR template.

## 435: How would you introduce code review to a team that has never done it?

- Explain the goals: fewer bugs, shared knowledge, learning, not control.
- Start light: one approval, required CI, a formatter and linter.
- Agree on a short set of rules together, so it's the team's process.
- Lead by example: ask for reviews on your own code and take feedback well.
- Keep reviews fast so people don't feel slowed down.
- Check after a few weeks what's working and adjust.

Forcing a heavy process on day one usually creates resistance.

## 436: What problems does an unbounded Promise.all cause, and how do you catch it in review?

```ts
await Promise.all(userIds.map((id) => sendEmail(id)));
```

With 50,000 users, this starts 50,000 requests at once. That can hit rate limits, run out of memory or sockets, and overload other services. Also, one rejection makes `Promise.all` reject, while the other calls keep running.

Suggest processing in batches or with a concurrency limit (for example with the `p-limit` package), and `Promise.allSettled` when partial failures are expected.

## 437: What should you check when reviewing rate limiting code?

- What's the key: IP, user, API key? IP-based limits can hit many users behind one network.
- Is the limit shared across server instances (for example in Redis), or per process?
- Does the response use `429 Too Many Requests` with a `Retry-After` header?
- Are login, signup and password reset endpoints limited more strictly?
- What happens if the rate limit store is down: fail open or fail closed?

## 438: What should you check when reviewing file upload code?

- File size limits enforced on the server.
- File type checked by content, not just the extension or the client's `Content-Type`.
- Files stored outside the web root or in object storage, with generated names.
- No user-supplied paths (path traversal).
- Images re-encoded or processed safely; user SVGs can contain scripts.
- Downloads served with `Content-Disposition` and correct content types.
- Virus scanning if users share files with each other.

## 439: What should you check when reviewing a webhook handler?

- Signature verification using the raw request body and a constant-time comparison.
- Replay protection, for example by checking a timestamp and rejecting old events.
- Idempotency: providers retry, so the same event can arrive several times.
- Fast response: acknowledge quickly and do heavy work in a background job.
- Handling unknown event types without crashing.

```ts
const expected = crypto.createHmac("sha256", secret).update(rawBody).digest();
const received = Buffer.from(signatureHeader, "hex");
if (
  received.length !== expected.length ||
  !crypto.timingSafeEqual(received, expected)
) {
  return res.status(401).end();
}
```

## 440: How do you review code for tenant isolation in a multi-tenant app?

Every query that touches tenant data must be scoped to the current tenant. Look for:

- Queries by ID without a tenant filter.
- Caches, file paths or queue messages missing the tenant ID.
- Background jobs that run without a tenant context.
- Admin features that cross tenants without extra checks.

Safer designs make it hard to forget: a data access layer that adds the tenant filter automatically, or database row-level security (like PostgreSQL RLS). Ask for tests that try to access another tenant's data.

## 441: What should you check when a PR adds soft deletes?

Soft delete means marking rows as deleted (for example with `deleted_at`) instead of removing them. Check:

- Every query now needs to exclude deleted rows; missing one shows deleted data.
- Unique constraints may need to account for deleted rows (a partial index).
- Related data: what happens to children of a soft-deleted parent?
- Privacy laws may still require real deletion of personal data.
- Is there a cleanup job to remove old soft-deleted rows?

## 442: What should you check when reviewing code that sends emails or notifications?

- Can the same notification be sent twice on retry? Track what was sent.
- Are user preferences and unsubscribes respected?
- Is sending done in a background job, not in the request?
- Is there rate limiting so a bug can't spam thousands of users?
- Are templates escaped properly to avoid HTML injection?
- Are test and staging environments prevented from emailing real users?

The last one has caused many embarrassing incidents.

## 443: What should you check when reviewing scheduled background jobs?

- What happens if a run takes longer than the interval and two runs overlap? A lock may be needed.
- What happens if the app runs on several instances? Will the job run on each of them?
- Is the job idempotent if it's retried or run twice?
- What time zone is the schedule in, and how does it behave on daylight saving days?
- Is failure monitored, and does a missed run trigger an alert?

## 444: What does fail open vs fail closed mean, and why should reviewers care?

When a check can't be performed (a service is down, config is missing), the code either:

- **Fails open**: allows the action anyway.
- **Fails closed**: blocks the action.

```ts
// Fails open: if the permission service errors, everyone is allowed
const allowed = await checkPermission(user, action).catch(() => true);
```

For security checks (auth, permissions, payments), fail closed is almost always right. For non-critical features (recommendations, analytics), failing open keeps the product usable. Reviewers should check which behavior the code has and whether it was a deliberate choice.

## 445: Why should reviewers check graceful shutdown in services?

When a service is deployed or scaled down, it gets a termination signal (like `SIGTERM`). Without handling it, in-flight requests get cut off and jobs stop halfway.

```ts
process.on("SIGTERM", () => {
  server.close(() => {
    db.disconnect().finally(() => process.exit(0));
  });
});
```

In review of new servers or workers, check that they stop accepting new work, finish current work within a timeout, close connections, and that long jobs can resume safely if killed.

## 446: Why can changes to TypeScript types in a published package be breaking?

Consumers compile against your types. Changes that can break their builds without any runtime change:

- Making an optional property required in an input type.
- Narrowing a parameter type, or widening a return type.
- Removing or renaming exported types.
- Raising the minimum TypeScript version through new syntax.

In review of a library, treat type changes like API changes. Tools like `@arethetypeswrong/cli` and API extractors can help catch problems.

## 447: Why should reviewers watch for copied code and licenses?

Code copied from Stack Overflow, blog posts or other projects comes with a license. Stack Overflow content is under Creative Commons Attribution-ShareAlike, and code from GPL projects can require you to release your own code under the GPL if distributed.

In review, if a block of code looks copied (different style, unusual comments), ask where it came from. If it's from another project, check the license and add attribution where required. License scanners can check dependencies, but copied snippets usually need a human to notice.

## 448: What do interviewers want to hear when they ask about your code review experience?

They want to see that you:

- Review regularly and take it seriously, not as a formality.
- Prioritize: bugs, security and design over style.
- Give clear, kind, explained feedback.
- Accept feedback on your own code without getting defensive.
- Keep PRs small and descriptions clear.
- Think about the team: speed of reviews, knowledge sharing, process improvements.

Concrete examples from real work count more than general statements.

## 449: How would you answer "Tell me about a time a code review caught a serious issue"?

Use a simple structure: situation, what you noticed, what you did, and the result. For example:

"A teammate added a CSV export endpoint. While reviewing, I noticed the query filtered by the export ID from the URL but not by the user's company, so any customer could download another customer's data by changing the ID. I marked it as blocking, explained it with an example request, and suggested scoping the query to the company. We fixed it, added a test that tries to access another company's export, and later added a check to our review checklist for tenant scoping."

Pick a real story, keep it short, and show what changed afterward.

## 450: What does a healthy code review culture look like?

- PRs are small, well described and reviewed within hours, not days.
- Comments are clear, kind, explained and labeled by importance.
- Everyone reviews, including juniors, and everyone gets reviewed, including leads.
- Disagreements are resolved quickly and without ego.
- Tools handle formatting and simple checks; people focus on what matters.
- Mistakes that slip through lead to process improvements, not blame.
- People see review as a way to learn and help each other, not as a gate or a test.
