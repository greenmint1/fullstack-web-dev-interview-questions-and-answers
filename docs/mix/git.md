# Git Interview Questions and Answers

_Last updated: October 28, 2026_

450 Git interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers target current Git (2.5x releases). They use the modern commands like `git switch` and `git restore`, the `ort` merge strategy, SSH commit signing, partial clone and sparse checkout. Older commands like `git checkout` for files and `git filter-branch` are mentioned where they still matter, since you will still see them in real projects. Changes planned for Git 3.0 (SHA-256, `main` as the default branch, reftable) are mentioned where relevant.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is Git?](#1-what-is-git)
- [2: What is version control and why do we need it?](#2-what-is-version-control-and-why-do-we-need-it)
- [3: What does it mean that Git is distributed?](#3-what-does-it-mean-that-git-is-distributed)
- [4: What is the difference between Git and GitHub?](#4-what-is-the-difference-between-git-and-github)
- [5: What is the difference between Git and older tools like SVN?](#5-what-is-the-difference-between-git-and-older-tools-like-svn)
- [6: What is a repository?](#6-what-is-a-repository)
- [7: How do you create a new Git repository?](#7-how-do-you-create-a-new-git-repository)
- [8: How do you clone a repository?](#8-how-do-you-clone-a-repository)
- [9: What is the working directory?](#9-what-is-the-working-directory)
- [10: What is the staging area?](#10-what-is-the-staging-area)
- [11: What are the three main states of a file in Git?](#11-what-are-the-three-main-states-of-a-file-in-git)
- [12: What is a commit?](#12-what-is-a-commit)
- [13: How do you make a commit?](#13-how-do-you-make-a-commit)
- [14: What does git status show?](#14-what-does-git-status-show)
- [15: What does git add do?](#15-what-does-git-add-do)
- [16: What is the difference between git add ., git add -A and git add -u?](#16-what-is-the-difference-between-git-add--git-add--a-and-git-add--u)
- [17: How do you see the commit history?](#17-how-do-you-see-the-commit-history)
- [18: What does git diff show?](#18-what-does-git-diff-show)
- [19: What is a branch?](#19-what-is-a-branch)
- [20: How do you create a new branch?](#20-how-do-you-create-a-new-branch)
- [21: How do you switch between branches?](#21-how-do-you-switch-between-branches)
- [22: How do you list branches?](#22-how-do-you-list-branches)
- [23: How do you delete a branch?](#23-how-do-you-delete-a-branch)
- [24: How do you rename a branch?](#24-how-do-you-rename-a-branch)
- [25: What is HEAD?](#25-what-is-head)
- [26: What is merging?](#26-what-is-merging)
- [27: What is a merge conflict?](#27-what-is-a-merge-conflict)
- [28: How do you resolve a merge conflict?](#28-how-do-you-resolve-a-merge-conflict)
- [29: What is a remote?](#29-what-is-a-remote)
- [30: What does git push do?](#30-what-does-git-push-do)
- [31: What does git pull do?](#31-what-does-git-pull-do)
- [32: What does git fetch do?](#32-what-does-git-fetch-do)
- [33: What is the difference between git fetch and git pull?](#33-what-is-the-difference-between-git-fetch-and-git-pull)
- [34: What is origin?](#34-what-is-origin)
- [35: What is a .gitignore file?](#35-what-is-a-gitignore-file)
- [36: How do you stop tracking a file that is already committed?](#36-how-do-you-stop-tracking-a-file-that-is-already-committed)
- [37: How do you configure your name and email in Git?](#37-how-do-you-configure-your-name-and-email-in-git)
- [38: What are the levels of Git configuration?](#38-what-are-the-levels-of-git-configuration)
- [39: What is a commit hash?](#39-what-is-a-commit-hash)
- [40: How do you write a good commit message?](#40-how-do-you-write-a-good-commit-message)
- [41: How do you change the last commit?](#41-how-do-you-change-the-last-commit)
- [42: How do you discard changes in a file?](#42-how-do-you-discard-changes-in-a-file)
- [43: How do you unstage a file?](#43-how-do-you-unstage-a-file)
- [44: What does git rm do?](#44-what-does-git-rm-do)
- [45: How do you rename or move a file in Git?](#45-how-do-you-rename-or-move-a-file-in-git)
- [46: What is git stash?](#46-what-is-git-stash)
- [47: What is the difference between git stash pop and git stash apply?](#47-what-is-the-difference-between-git-stash-pop-and-git-stash-apply)
- [48: How do you see what is in your stash?](#48-how-do-you-see-what-is-in-your-stash)
- [49: What is a tag?](#49-what-is-a-tag)
- [50: What is the difference between a lightweight tag and an annotated tag?](#50-what-is-the-difference-between-a-lightweight-tag-and-an-annotated-tag)
- [51: How do you push tags to the remote?](#51-how-do-you-push-tags-to-the-remote)
- [52: What is git show used for?](#52-what-is-git-show-used-for)
- [53: What is the default branch?](#53-what-is-the-default-branch)
- [54: What is the difference between master and main?](#54-what-is-the-difference-between-master-and-main)
- [55: What is a fast-forward merge?](#55-what-is-a-fast-forward-merge)
- [56: What is a merge commit?](#56-what-is-a-merge-commit)
- [57: What is rebasing?](#57-what-is-rebasing)
- [58: What is the difference between merge and rebase?](#58-what-is-the-difference-between-merge-and-rebase)
- [59: What is git clone --depth used for?](#59-what-is-git-clone---depth-used-for)
- [60: What is git log --oneline?](#60-what-is-git-log---oneline)
- [61: How do you see the history of a single file?](#61-how-do-you-see-the-history-of-a-single-file)
- [62: What is git blame?](#62-what-is-git-blame)
- [63: How do you undo a commit that was already pushed?](#63-how-do-you-undo-a-commit-that-was-already-pushed)
- [64: What does git reset do?](#64-what-does-git-reset-do)
- [65: What is the difference between git reset --soft, --mixed and --hard?](#65-what-is-the-difference-between-git-reset---soft---mixed-and---hard)
- [66: What is the difference between git revert and git reset?](#66-what-is-the-difference-between-git-revert-and-git-reset)
- [67: What does HEAD~1 mean?](#67-what-does-head1-mean)
- [68: What is the difference between HEAD~ and HEAD^?](#68-what-is-the-difference-between-head-and-head)
- [69: What is a detached HEAD?](#69-what-is-a-detached-head)
- [70: What is an upstream branch?](#70-what-is-an-upstream-branch)
- [71: What is a remote-tracking branch?](#71-what-is-a-remote-tracking-branch)
- [72: How do you check out a branch that only exists on the remote?](#72-how-do-you-check-out-a-branch-that-only-exists-on-the-remote)
- [73: What is a pull request?](#73-what-is-a-pull-request)
- [74: What is a fork?](#74-what-is-a-fork)
- [75: How do you keep a fork up to date with the original repo?](#75-how-do-you-keep-a-fork-up-to-date-with-the-original-repo)
- [76: What is git cherry-pick?](#76-what-is-git-cherry-pick)
- [77: What does git clean do?](#77-what-does-git-clean-do)
- [78: What is the .git folder?](#78-what-is-the-git-folder)
- [79: Why does Git not track empty folders?](#79-why-does-git-not-track-empty-folders)
- [80: How do you list all tracked files?](#80-how-do-you-list-all-tracked-files)
- [81: How do you see which files changed in a commit?](#81-how-do-you-see-which-files-changed-in-a-commit)
- [82: How do you compare two branches?](#82-how-do-you-compare-two-branches)
- [83: What is the difference between git diff and git diff --staged?](#83-what-is-the-difference-between-git-diff-and-git-diff---staged)
- [84: How do you commit only part of a file?](#84-how-do-you-commit-only-part-of-a-file)
- [85: What does git commit -a do?](#85-what-does-git-commit--a-do)
- [86: How do you see the remote URL?](#86-how-do-you-see-the-remote-url)
- [87: What is the difference between HTTPS and SSH for Git remotes?](#87-what-is-the-difference-between-https-and-ssh-for-git-remotes)
- [88: How do you set up an SSH key for GitHub?](#88-how-do-you-set-up-an-ssh-key-for-github)
- [89: What is a credential helper?](#89-what-is-a-credential-helper)
- [90: What is a Git alias?](#90-what-is-a-git-alias)
- [91: How do you set the default editor for Git?](#91-how-do-you-set-the-default-editor-for-git)
- [92: What is git reflog?](#92-what-is-git-reflog)
- [93: How do you recover a deleted branch?](#93-how-do-you-recover-a-deleted-branch)
- [94: How do you undo git add?](#94-how-do-you-undo-git-add)
- [95: How do you see who made changes to a file?](#95-how-do-you-see-who-made-changes-to-a-file)
- [96: What is git shortlog?](#96-what-is-git-shortlog)
- [97: How do you search the commit history by message?](#97-how-do-you-search-the-commit-history-by-message)
- [98: How do you find a commit that added or removed a piece of code?](#98-how-do-you-find-a-commit-that-added-or-removed-a-piece-of-code)
- [99: What is git grep?](#99-what-is-git-grep)
- [100: What happens if you run git commit without staging anything?](#100-what-happens-if-you-run-git-commit-without-staging-anything)
- [101: How do you see the changes of a specific commit?](#101-how-do-you-see-the-changes-of-a-specific-commit)
- [102: What is git switch?](#102-what-is-git-switch)
- [103: What is git restore?](#103-what-is-git-restore)
- [104: Why was git checkout split into git switch and git restore?](#104-why-was-git-checkout-split-into-git-switch-and-git-restore)
- [105: How do you create a branch from a specific commit?](#105-how-do-you-create-a-branch-from-a-specific-commit)
- [106: How do you check which branch you are on?](#106-how-do-you-check-which-branch-you-are-on)
- [107: What is the difference between git pull with merge and git pull with rebase?](#107-what-is-the-difference-between-git-pull-with-merge-and-git-pull-with-rebase)
- [108: How do you set up Git to only fast-forward on pull?](#108-how-do-you-set-up-git-to-only-fast-forward-on-pull)
- [109: What does "your branch is ahead of origin/main by 2 commits" mean?](#109-what-does-your-branch-is-ahead-of-originmain-by-2-commits-mean)
- [110: What does git push --force do?](#110-what-does-git-push---force-do)
- [111: What is git push --force-with-lease?](#111-what-is-git-push---force-with-lease)
- [112: What is a README file?](#112-what-is-a-readme-file)
- [113: What is Markdown and why is it used in Git repos?](#113-what-is-markdown-and-why-is-it-used-in-git-repos)
- [114: How do you clone a specific branch?](#114-how-do-you-clone-a-specific-branch)
- [115: How do you see the last commit?](#115-how-do-you-see-the-last-commit)
- [116: How do you list files changed between two commits?](#116-how-do-you-list-files-changed-between-two-commits)
- [117: What is a hook in Git?](#117-what-is-a-hook-in-git)
- [118: How do you ignore a file only on your machine?](#118-how-do-you-ignore-a-file-only-on-your-machine)
- [119: How do you check why a file is ignored?](#119-how-do-you-check-why-a-file-is-ignored)
- [120: What are common .gitignore patterns?](#120-what-are-common-gitignore-patterns)
- [121: Can you have more than one .gitignore file?](#121-can-you-have-more-than-one-gitignore-file)
- [122: What is git init --bare?](#122-what-is-git-init---bare)
- [123: What is git log --graph?](#123-what-is-git-log---graph)
- [124: How do you see which branches are merged into main?](#124-how-do-you-see-which-branches-are-merged-into-main)
- [125: How do you delete local branches that were deleted on the remote?](#125-how-do-you-delete-local-branches-that-were-deleted-on-the-remote)
- [126: What is the difference between git branch -d and -D?](#126-what-is-the-difference-between-git-branch--d-and--d)
- [127: What is a conflict marker?](#127-what-is-a-conflict-marker)
- [128: What is git merge --abort?](#128-what-is-git-merge---abort)
- [129: How do you see the content of a file in another branch without switching?](#129-how-do-you-see-the-content-of-a-file-in-another-branch-without-switching)
- [130: How do you get a file from another branch into your current branch?](#130-how-do-you-get-a-file-from-another-branch-into-your-current-branch)
- [131: What is git describe?](#131-what-is-git-describe)
- [132: What is semantic versioning and how is it used with Git tags?](#132-what-is-semantic-versioning-and-how-is-it-used-with-git-tags)
- [133: How do you see all the tags that contain a commit?](#133-how-do-you-see-all-the-tags-that-contain-a-commit)
- [134: How do you check out a tag?](#134-how-do-you-check-out-a-tag)
- [135: What does git commit --amend --no-edit do?](#135-what-does-git-commit---amend---no-edit-do)
- [136: How do you remove a file from the last commit?](#136-how-do-you-remove-a-file-from-the-last-commit)
- [137: How do you change the author of the last commit?](#137-how-do-you-change-the-author-of-the-last-commit)
- [138: What is the difference between author and committer?](#138-what-is-the-difference-between-author-and-committer)
- [139: What does git log --stat show?](#139-what-does-git-log---stat-show)
- [140: How do you see the history of a specific line range?](#140-how-do-you-see-the-history-of-a-specific-line-range)
- [141: What is a hunk?](#141-what-is-a-hunk)
- [142: How do you see a word by word diff?](#142-how-do-you-see-a-word-by-word-diff)
- [143: What does git checkout . do?](#143-what-does-git-checkout--do)
- [144: What is git commit -v?](#144-what-is-git-commit--v)
- [145: How do you find out which Git version you have?](#145-how-do-you-find-out-which-git-version-you-have)
- [146: What is GitHub Desktop or a Git GUI?](#146-what-is-github-desktop-or-a-git-gui)
- [147: What does "working tree clean" mean?](#147-what-does-working-tree-clean-mean)
- [148: How do you create a branch and push it to the remote?](#148-how-do-you-create-a-branch-and-push-it-to-the-remote)
- [149: How do you undo the last commit but keep the changes?](#149-how-do-you-undo-the-last-commit-but-keep-the-changes)
- [150: What is a monorepo?](#150-what-is-a-monorepo)

### Moderate Questions (151-300)

- [151: What is interactive rebase?](#151-what-is-interactive-rebase)
- [152: What are the main commands in an interactive rebase?](#152-what-are-the-main-commands-in-an-interactive-rebase)
- [153: How do you squash several commits into one?](#153-how-do-you-squash-several-commits-into-one)
- [154: What is the difference between squash and fixup in interactive rebase?](#154-what-is-the-difference-between-squash-and-fixup-in-interactive-rebase)
- [155: What are fixup commits and autosquash?](#155-what-are-fixup-commits-and-autosquash)
- [156: How do you edit an older commit, not just the last one?](#156-how-do-you-edit-an-older-commit-not-just-the-last-one)
- [157: How do you split one commit into two?](#157-how-do-you-split-one-commit-into-two)
- [158: How do you reorder commits?](#158-how-do-you-reorder-commits)
- [159: How do you remove a commit from the middle of a branch?](#159-how-do-you-remove-a-commit-from-the-middle-of-a-branch)
- [160: What happens when there is a conflict during a rebase?](#160-what-happens-when-there-is-a-conflict-during-a-rebase)
- [161: What do "ours" and "theirs" mean during merge and rebase?](#161-what-do-ours-and-theirs-mean-during-merge-and-rebase)
- [162: What is git rebase --onto?](#162-what-is-git-rebase---onto)
- [163: You branched off a feature branch by mistake. How do you move your branch to main?](#163-you-branched-off-a-feature-branch-by-mistake-how-do-you-move-your-branch-to-main)
- [164: How do you move commits you made on main to a new branch?](#164-how-do-you-move-commits-you-made-on-main-to-a-new-branch)
- [165: How do you move the last commit to another existing branch?](#165-how-do-you-move-the-last-commit-to-another-existing-branch)
- [166: How do you cherry-pick a range of commits?](#166-how-do-you-cherry-pick-a-range-of-commits)
- [167: What does git cherry-pick -x do?](#167-what-does-git-cherry-pick--x-do)
- [168: What are the downsides of cherry-picking?](#168-what-are-the-downsides-of-cherry-picking)
- [169: What is a squash merge?](#169-what-is-a-squash-merge)
- [170: What are the pros and cons of squash merging pull requests?](#170-what-are-the-pros-and-cons-of-squash-merging-pull-requests)
- [171: What is the difference between merge --squash and a regular merge?](#171-what-is-the-difference-between-merge---squash-and-a-regular-merge)
- [172: When would you use git merge --no-ff?](#172-when-would-you-use-git-merge---no-ff)
- [173: How do you revert a merge commit?](#173-how-do-you-revert-a-merge-commit)
- [174: What happens if you revert a merge and later try to merge the same branch again?](#174-what-happens-if-you-revert-a-merge-and-later-try-to-merge-the-same-branch-again)
- [175: How do you revert several commits?](#175-how-do-you-revert-several-commits)
- [176: What is git bisect?](#176-what-is-git-bisect)
- [177: How do you automate git bisect?](#177-how-do-you-automate-git-bisect)
- [178: What is git rerere?](#178-what-is-git-rerere)
- [179: How do you use a merge tool to resolve conflicts?](#179-how-do-you-use-a-merge-tool-to-resolve-conflicts)
- [180: What is the diff3 or zdiff3 conflict style?](#180-what-is-the-diff3-or-zdiff3-conflict-style)
- [181: How do you take one side completely when resolving a conflict?](#181-how-do-you-take-one-side-completely-when-resolving-a-conflict)
- [182: What is the difference between git merge -s ours and git merge -X ours?](#182-what-is-the-difference-between-git-merge--s-ours-and-git-merge--x-ours)
- [183: How do you resolve a conflict in package-lock.json or another lock file?](#183-how-do-you-resolve-a-conflict-in-package-lockjson-or-another-lock-file)
- [184: What is the stash with untracked files?](#184-what-is-the-stash-with-untracked-files)
- [185: How do you stash only some files?](#185-how-do-you-stash-only-some-files)
- [186: How do you create a branch from a stash?](#186-how-do-you-create-a-branch-from-a-stash)
- [187: How do you recover a stash you dropped by mistake?](#187-how-do-you-recover-a-stash-you-dropped-by-mistake)
- [188: What is a Git submodule?](#188-what-is-a-git-submodule)
- [189: How do you clone a repo with submodules?](#189-how-do-you-clone-a-repo-with-submodules)
- [190: How do you update a submodule to a newer version?](#190-how-do-you-update-a-submodule-to-a-newer-version)
- [191: What are common problems with submodules?](#191-what-are-common-problems-with-submodules)
- [192: What is git subtree?](#192-what-is-git-subtree)
- [193: When would you choose a submodule over a subtree?](#193-when-would-you-choose-a-submodule-over-a-subtree)
- [194: What is git worktree?](#194-what-is-git-worktree)
- [195: What is the difference between git worktree and cloning the repo twice?](#195-what-is-the-difference-between-git-worktree-and-cloning-the-repo-twice)
- [196: What are the most used client-side hooks?](#196-what-are-the-most-used-client-side-hooks)
- [197: Why are hooks not shared when you clone a repo?](#197-why-are-hooks-not-shared-when-you-clone-a-repo)
- [198: How do you share hooks with your team?](#198-how-do-you-share-hooks-with-your-team)
- [199: What is Husky?](#199-what-is-husky)
- [200: What is lint-staged?](#200-what-is-lint-staged)
- [201: How do you enforce a commit message format?](#201-how-do-you-enforce-a-commit-message-format)
- [202: What are Conventional Commits?](#202-what-are-conventional-commits)
- [203: How do you skip hooks when committing?](#203-how-do-you-skip-hooks-when-committing)
- [204: What is Git Flow?](#204-what-is-git-flow)
- [205: What is GitHub Flow?](#205-what-is-github-flow)
- [206: What is trunk-based development?](#206-what-is-trunk-based-development)
- [207: How do you choose a branching strategy for a team?](#207-how-do-you-choose-a-branching-strategy-for-a-team)
- [208: What are feature flags and how do they relate to Git branching?](#208-what-are-feature-flags-and-how-do-they-relate-to-git-branching)
- [209: How do you handle a hotfix for production?](#209-how-do-you-handle-a-hotfix-for-production)
- [210: What are release branches?](#210-what-are-release-branches)
- [211: What are protected branches?](#211-what-are-protected-branches)
- [212: What is a CODEOWNERS file?](#212-what-is-a-codeowners-file)
- [213: What is a merge queue?](#213-what-is-a-merge-queue)
- [214: How do you check out someone's pull request locally?](#214-how-do-you-check-out-someones-pull-request-locally)
- [215: What is a good size for a pull request?](#215-what-is-a-good-size-for-a-pull-request)
- [216: What are stacked pull requests?](#216-what-are-stacked-pull-requests)
- [217: What does git rebase --update-refs do?](#217-what-does-git-rebase---update-refs-do)
- [218: How do you update a feature branch with the latest main?](#218-how-do-you-update-a-feature-branch-with-the-latest-main)
- [219: What is git rebase --autostash?](#219-what-is-git-rebase---autostash)
- [220: What is git rebase --exec?](#220-what-is-git-rebase---exec)
- [221: How do you rebase the very first commit of a repo?](#221-how-do-you-rebase-the-very-first-commit-of-a-repo)
- [222: What is ORIG_HEAD?](#222-what-is-orig_head)
- [223: What are FETCH_HEAD and MERGE_HEAD?](#223-what-are-fetch_head-and-merge_head)
- [224: What are reflog references like HEAD@{2}?](#224-what-are-reflog-references-like-head2)
- [225: What does @{u} mean?](#225-what-does-u-mean)
- [226: What is the difference between two dots and three dots in git log?](#226-what-is-the-difference-between-two-dots-and-three-dots-in-git-log)
- [227: Why does git diff A..B differ from git log A..B?](#227-why-does-git-diff-ab-differ-from-git-log-ab)
- [228: What is a merge base?](#228-what-is-a-merge-base)
- [229: What is a three-way merge?](#229-what-is-a-three-way-merge)
- [230: What merge strategy does Git use by default?](#230-what-merge-strategy-does-git-use-by-default)
- [231: What is an octopus merge?](#231-what-is-an-octopus-merge)
- [232: What does git log --first-parent do?](#232-what-does-git-log---first-parent-do)
- [233: How do you see only merge commits or skip them?](#233-how-do-you-see-only-merge-commits-or-skip-them)
- [234: How do you write a custom log format?](#234-how-do-you-write-a-custom-log-format)
- [235: How do you list branches sorted by most recent commit?](#235-how-do-you-list-branches-sorted-by-most-recent-commit)
- [236: How do you configure different Git settings for work and personal projects?](#236-how-do-you-configure-different-git-settings-for-work-and-personal-projects)
- [237: What is url.insteadOf?](#237-what-is-urlinsteadof)
- [238: How do you handle line endings across Windows, macOS and Linux?](#238-how-do-you-handle-line-endings-across-windows-macos-and-linux)
- [239: What does core.autocrlf do?](#239-what-does-coreautocrlf-do)
- [240: How do you fix line endings after adding .gitattributes?](#240-how-do-you-fix-line-endings-after-adding-gitattributes)
- [241: What is .gitattributes used for besides line endings?](#241-what-is-gitattributes-used-for-besides-line-endings)
- [242: What is Git LFS?](#242-what-is-git-lfs)
- [243: How do you move existing large files into Git LFS?](#243-how-do-you-move-existing-large-files-into-git-lfs)
- [244: How do you sign commits?](#244-how-do-you-sign-commits)
- [245: Why sign commits?](#245-why-sign-commits)
- [246: How do you verify a signed commit or tag?](#246-how-do-you-verify-a-signed-commit-or-tag)
- [247: What is the "Signed-off-by" line?](#247-what-is-the-signed-off-by-line)
- [248: What are commit trailers?](#248-what-are-commit-trailers)
- [249: What is a .mailmap file?](#249-what-is-a-mailmap-file)
- [250: How do you ignore formatting commits in git blame?](#250-how-do-you-ignore-formatting-commits-in-git-blame)
- [251: How do you remove a file with secrets from the whole history?](#251-how-do-you-remove-a-file-with-secrets-from-the-whole-history)
- [252: Why is git filter-branch not recommended anymore?](#252-why-is-git-filter-branch-not-recommended-anymore)
- [253: How do you stop secrets from being committed in the first place?](#253-how-do-you-stop-secrets-from-being-committed-in-the-first-place)
- [254: What should you do if you pushed a secret to a public repo?](#254-what-should-you-do-if-you-pushed-a-secret-to-a-public-repo)
- [255: How do you create a patch file and apply it?](#255-how-do-you-create-a-patch-file-and-apply-it)
- [256: What is the difference between git apply and git am?](#256-what-is-the-difference-between-git-apply-and-git-am)
- [257: How do you create a zip of the repo without the .git folder?](#257-how-do-you-create-a-zip-of-the-repo-without-the-git-folder)
- [258: What is git bundle?](#258-what-is-git-bundle)
- [259: How do you compare a file between two branches?](#259-how-do-you-compare-a-file-between-two-branches)
- [260: How do you ignore whitespace changes in a diff?](#260-how-do-you-ignore-whitespace-changes-in-a-diff)
- [261: What does git diff --check do?](#261-what-does-git-diff---check-do)
- [262: How do you see a diff with moved lines highlighted?](#262-how-do-you-see-a-diff-with-moved-lines-highlighted)
- [263: What diff algorithms does Git have?](#263-what-diff-algorithms-does-git-have)
- [264: How does Git detect renames?](#264-how-does-git-detect-renames)
- [265: Why does git log --follow only work with one file?](#265-why-does-git-log---follow-only-work-with-one-file)
- [266: How do you find when a file was deleted?](#266-how-do-you-find-when-a-file-was-deleted)
- [267: How do you find which commit introduced a specific line?](#267-how-do-you-find-which-commit-introduced-a-specific-line)
- [268: How do you change the date of a commit?](#268-how-do-you-change-the-date-of-a-commit)
- [269: How do you change the author email on many old commits?](#269-how-do-you-change-the-author-email-on-many-old-commits)
- [270: How do you push to two remotes at once?](#270-how-do-you-push-to-two-remotes-at-once)
- [271: What does push.default do?](#271-what-does-pushdefault-do)
- [272: What does push.autoSetupRemote do?](#272-what-does-pushautosetupremote-do)
- [273: Why was my push rejected with "non-fast-forward"?](#273-why-was-my-push-rejected-with-non-fast-forward)
- [274: How do you rename the default branch from master to main?](#274-how-do-you-rename-the-default-branch-from-master-to-main)
- [275: What does git remote set-head do?](#275-what-does-git-remote-set-head-do)
- [276: What does git ls-remote do?](#276-what-does-git-ls-remote-do)
- [277: How do you get the current commit hash in a script?](#277-how-do-you-get-the-current-commit-hash-in-a-script)
- [278: What is the difference between plumbing and porcelain commands?](#278-what-is-the-difference-between-plumbing-and-porcelain-commands)
- [279: Why should scripts use git status --porcelain?](#279-why-should-scripts-use-git-status---porcelain)
- [280: How do you use Git in CI with a shallow clone?](#280-how-do-you-use-git-in-ci-with-a-shallow-clone)
- [281: How do you get the list of changed files in a pull request in CI?](#281-how-do-you-get-the-list-of-changed-files-in-a-pull-request-in-ci)
- [282: What is sparse checkout?](#282-what-is-sparse-checkout)
- [283: What is cone mode in sparse checkout?](#283-what-is-cone-mode-in-sparse-checkout)
- [284: What is a partial clone?](#284-what-is-a-partial-clone)
- [285: What is the difference between a shallow clone and a partial clone?](#285-what-is-the-difference-between-a-shallow-clone-and-a-partial-clone)
- [286: How do you combine sparse checkout and partial clone?](#286-how-do-you-combine-sparse-checkout-and-partial-clone)
- [287: How do you fetch only one branch?](#287-how-do-you-fetch-only-one-branch)
- [288: What is a refspec?](#288-what-is-a-refspec)
- [289: How do you push a local branch to a remote branch with a different name?](#289-how-do-you-push-a-local-branch-to-a-remote-branch-with-a-different-name)
- [290: How do you see what will be pushed before pushing?](#290-how-do-you-see-what-will-be-pushed-before-pushing)
- [291: What is git notes?](#291-what-is-git-notes)
- [292: What is git range-diff?](#292-what-is-git-range-diff)
- [293: How do you list commits on a branch that aren't in another branch, even after cherry-picks?](#293-how-do-you-list-commits-on-a-branch-that-arent-in-another-branch-even-after-cherry-picks)
- [294: How do you get Git to remember your choice for every conflict on a branch with many rebases?](#294-how-do-you-get-git-to-remember-your-choice-for-every-conflict-on-a-branch-with-many-rebases)
- [295: What is git switch --orphan?](#295-what-is-git-switch---orphan)
- [296: How do you merge two unrelated repositories and keep both histories?](#296-how-do-you-merge-two-unrelated-repositories-and-keep-both-histories)
- [297: How do you split a folder out into its own repository with its history?](#297-how-do-you-split-a-folder-out-into-its-own-repository-with-its-history)
- [298: How do you run a command on every commit in a range?](#298-how-do-you-run-a-command-on-every-commit-in-a-range)
- [299: What is git maintenance?](#299-what-is-git-maintenance)
- [300: What is git gc?](#300-what-is-git-gc)

### Advanced Questions (301-450)

- [301: How does Git store data internally?](#301-how-does-git-store-data-internally)
- [302: Does Git store diffs or snapshots?](#302-does-git-store-diffs-or-snapshots)
- [303: How is a blob's hash calculated?](#303-how-is-a-blobs-hash-calculated)
- [304: How do you inspect Git objects directly?](#304-how-do-you-inspect-git-objects-directly)
- [305: What does a commit object look like inside?](#305-what-does-a-commit-object-look-like-inside)
- [306: What does a tree object contain?](#306-what-does-a-tree-object-contain)
- [307: How could you create a commit using only plumbing commands?](#307-how-could-you-create-a-commit-using-only-plumbing-commands)
- [308: What are loose objects and packfiles?](#308-what-are-loose-objects-and-packfiles)
- [309: How does delta compression in packfiles work?](#309-how-does-delta-compression-in-packfiles-work)
- [310: What is the Git index file?](#310-what-is-the-git-index-file)
- [311: How does git status decide which files changed?](#311-how-does-git-status-decide-which-files-changed)
- [312: What is the "racy git" problem?](#312-what-is-the-racy-git-problem)
- [313: How are branches and tags stored?](#313-how-are-branches-and-tags-stored)
- [314: What is reftable?](#314-what-is-reftable)
- [315: What is a symbolic ref?](#315-what-is-a-symbolic-ref)
- [316: What happens step by step when you run git commit?](#316-what-happens-step-by-step-when-you-run-git-commit)
- [317: What happens step by step when you run git fetch?](#317-what-happens-step-by-step-when-you-run-git-fetch)
- [318: What is Git protocol version 2?](#318-what-is-git-protocol-version-2)
- [319: What is a thin pack?](#319-what-is-a-thin-pack)
- [320: What is the commit-graph file?](#320-what-is-the-commit-graph-file)
- [321: What are generation numbers?](#321-what-are-generation-numbers)
- [322: What are changed-path Bloom filters?](#322-what-are-changed-path-bloom-filters)
- [323: What is a multi-pack-index?](#323-what-is-a-multi-pack-index)
- [324: What are reachability bitmaps?](#324-what-are-reachability-bitmaps)
- [325: What does git gc do in detail?](#325-what-does-git-gc-do-in-detail)
- [326: What is the difference between unreachable and dangling objects?](#326-what-is-the-difference-between-unreachable-and-dangling-objects)
- [327: Why doesn't git gc delete unreachable objects right away?](#327-why-doesnt-git-gc-delete-unreachable-objects-right-away)
- [328: How do you recover a commit after reset --hard and after the reflog was cleared?](#328-how-do-you-recover-a-commit-after-reset---hard-and-after-the-reflog-was-cleared)
- [329: How does git stash store data internally?](#329-how-does-git-stash-store-data-internally)
- [330: How does rebase work internally?](#330-how-does-rebase-work-internally)
- [331: How does cherry-pick work internally?](#331-how-does-cherry-pick-work-internally)
- [332: What is the ort merge strategy and why did it replace recursive?](#332-what-is-the-ort-merge-strategy-and-why-did-it-replace-recursive)
- [333: What is a criss-cross merge?](#333-what-is-a-criss-cross-merge)
- [334: What is an evil merge?](#334-what-is-an-evil-merge)
- [335: What is --remerge-diff?](#335-what-is---remerge-diff)
- [336: What is git merge-tree --write-tree?](#336-what-is-git-merge-tree---write-tree)
- [337: What is git replay?](#337-what-is-git-replay)
- [338: How does Git detect directory renames during a merge?](#338-how-does-git-detect-directory-renames-during-a-merge)
- [339: What is merge.renameLimit and why does it matter?](#339-what-is-mergerenamelimit-and-why-does-it-matter)
- [340: How are submodules stored in the parent repo?](#340-how-are-submodules-stored-in-the-parent-repo)
- [341: How are worktrees stored internally?](#341-how-are-worktrees-stored-internally)
- [342: What is the difference between GIT_DIR and GIT_WORK_TREE?](#342-what-is-the-difference-between-git_dir-and-git_work_tree)
- [343: Why was SHA-1 a problem for Git, and what did Git do about it?](#343-why-was-sha-1-a-problem-for-git-and-what-did-git-do-about-it)
- [344: What blocks a full move to SHA-256?](#344-what-blocks-a-full-move-to-sha-256)
- [345: Why are Git branches so cheap compared to other systems?](#345-why-are-git-branches-so-cheap-compared-to-other-systems)
- [346: Why are commits immutable and what does that mean in practice?](#346-why-are-commits-immutable-and-what-does-that-mean-in-practice)
- [347: What is the .git/index.lock file and why does it get stuck?](#347-what-is-the-gitindexlock-file-and-why-does-it-get-stuck)
- [348: How do you find the largest files in a repo's history?](#348-how-do-you-find-the-largest-files-in-a-repos-history)
- [349: How do you reduce the size of a bloated repository?](#349-how-do-you-reduce-the-size-of-a-bloated-repository)
- [350: What does git gc --aggressive do and should you use it?](#350-what-does-git-gc---aggressive-do-and-should-you-use-it)
- [351: How do you make git status fast in a huge repository?](#351-how-do-you-make-git-status-fast-in-a-huge-repository)
- [352: What is the built-in fsmonitor?](#352-what-is-the-built-in-fsmonitor)
- [353: What is Scalar?](#353-what-is-scalar)
- [354: How do you debug a slow Git command?](#354-how-do-you-debug-a-slow-git-command)
- [355: How would you set up Git for a monorepo with thousands of developers?](#355-how-would-you-set-up-git-for-a-monorepo-with-thousands-of-developers)
- [356: How do you speed up cloning in CI?](#356-how-do-you-speed-up-cloning-in-ci)
- [357: What does git clone --reference do?](#357-what-does-git-clone---reference-do)
- [358: What is a mirror clone and when do you use it?](#358-what-is-a-mirror-clone-and-when-do-you-use-it)
- [359: What are server-side hooks?](#359-what-are-server-side-hooks)
- [360: How would you write a pre-receive hook that blocks force pushes to main?](#360-how-would-you-write-a-pre-receive-hook-that-blocks-force-pushes-to-main)
- [361: What is the safe.directory setting and why was it added?](#361-what-is-the-safedirectory-setting-and-why-was-it-added)
- [362: What are the security risks of cloning an untrusted repository?](#362-what-are-the-security-risks-of-cloning-an-untrusted-repository)
- [363: Why is protocol.file.allow restricted by default?](#363-why-is-protocolfileallow-restricted-by-default)
- [364: Why should you not expose the .git folder on a web server?](#364-why-should-you-not-expose-the-git-folder-on-a-web-server)
- [365: How can someone fake commits as another person, and how do you prevent it?](#365-how-can-someone-fake-commits-as-another-person-and-how-do-you-prevent-it)
- [366: What is transfer.fsckObjects?](#366-what-is-transferfsckobjects)
- [367: How do credentials leak through Git, and how do you avoid it?](#367-how-do-credentials-leak-through-git-and-how-do-you-avoid-it)
- [368: What is the trust model of signed tags in a release process?](#368-what-is-the-trust-model-of-signed-tags-in-a-release-process)
- [369: What are clean and smudge filters?](#369-what-are-clean-and-smudge-filters)
- [370: How does Git LFS work internally?](#370-how-does-git-lfs-work-internally)
- [371: What is file locking in Git LFS and why is it needed?](#371-what-is-file-locking-in-git-lfs-and-why-is-it-needed)
- [372: What is a textconv diff driver?](#372-what-is-a-textconv-diff-driver)
- [373: How do you write a custom merge driver?](#373-how-do-you-write-a-custom-merge-driver)
- [374: What is git replace?](#374-what-is-git-replace)
- [375: What are grafts and why were they replaced?](#375-what-are-grafts-and-why-were-they-replaced)
- [376: How does a shallow clone work internally?](#376-how-does-a-shallow-clone-work-internally)
- [377: How does a partial clone fetch missing objects?](#377-how-does-a-partial-clone-fetch-missing-objects)
- [378: What is a bundle URI?](#378-what-is-a-bundle-uri)
- [379: How does git blame work and why can it be slow?](#379-how-does-git-blame-work-and-why-can-it-be-slow)
- [380: How does git bisect handle merge commits and non-linear history?](#380-how-does-git-bisect-handle-merge-commits-and-non-linear-history)
- [381: What are git bisect terms?](#381-what-are-git-bisect-terms)
- [382: How do you recover after someone force pushed and removed commits from a shared branch?](#382-how-do-you-recover-after-someone-force-pushed-and-removed-commits-from-a-shared-branch)
- [383: Why does git push --force-with-lease without arguments not always protect you?](#383-why-does-git-push---force-with-lease-without-arguments-not-always-protect-you)
- [384: What does git push --atomic do?](#384-what-does-git-push---atomic-do)
- [385: What are push options?](#385-what-are-push-options)
- [386: How do you update many refs safely in one go?](#386-how-do-you-update-many-refs-safely-in-one-go)
- [387: What are hidden refs and namespaces?](#387-what-are-hidden-refs-and-namespaces)
- [388: How do forks on GitHub share storage?](#388-how-do-forks-on-github-share-storage)
- [389: What happens to pull request refs after you rewrite history?](#389-what-happens-to-pull-request-refs-after-you-rewrite-history)
- [390: How do case-insensitive file systems cause problems in Git?](#390-how-do-case-insensitive-file-systems-cause-problems-in-git)
- [391: How does Git handle file permissions and executable bits?](#391-how-does-git-handle-file-permissions-and-executable-bits)
- [392: How does Git store symlinks?](#392-how-does-git-store-symlinks)
- [393: What is the difference between assume-unchanged and skip-worktree?](#393-what-is-the-difference-between-assume-unchanged-and-skip-worktree)
- [394: How do you deal with a corrupted repository?](#394-how-do-you-deal-with-a-corrupted-repository)
- [395: Why shouldn't you keep a Git repo in a Dropbox or iCloud folder?](#395-why-shouldnt-you-keep-a-git-repo-in-a-dropbox-or-icloud-folder)
- [396: What is the difference between git log ordering options?](#396-what-is-the-difference-between-git-log-ordering-options)
- [397: How do you find the commit where two branches split, even after main was merged into the feature branch?](#397-how-do-you-find-the-commit-where-two-branches-split-even-after-main-was-merged-into-the-feature-branch)
- [398: How does git rebase use --fork-point?](#398-how-does-git-rebase-use---fork-point)
- [399: What are the trade-offs between a merge-heavy and a rebase-heavy workflow?](#399-what-are-the-trade-offs-between-a-merge-heavy-and-a-rebase-heavy-workflow)
- [400: How do you keep a long-lived branch from drifting too far from main?](#400-how-do-you-keep-a-long-lived-branch-from-drifting-too-far-from-main)
- [401: You pushed a commit straight to main by mistake, and the team only allows changes through pull requests. What do you do?](#401-you-pushed-a-commit-straight-to-main-by-mistake-and-the-team-only-allows-changes-through-pull-requests-what-do-you-do)
- [402: You ran git reset --hard and lost work. What can you get back?](#402-you-ran-git-reset---hard-and-lost-work-what-can-you-get-back)
- [403: After a rebase, your pull request shows the same commits twice. Why, and how do you fix it?](#403-after-a-rebase-your-pull-request-shows-the-same-commits-twice-why-and-how-do-you-fix-it)
- [404: Your history is full of "Merge branch 'main' of github.com/..." commits. How do you stop that?](#404-your-history-is-full-of-merge-branch-main-of-githubcom-commits-how-do-you-stop-that)
- [405: A big formatting change on main causes conflicts in every open pull request. How do you handle it?](#405-a-big-formatting-change-on-main-causes-conflicts-in-every-open-pull-request-how-do-you-handle-it)
- [406: How do you migrate a repository from SVN to Git?](#406-how-do-you-migrate-a-repository-from-svn-to-git)
- [407: How do you move a repository from GitLab to GitHub with all branches and tags?](#407-how-do-you-move-a-repository-from-gitlab-to-github-with-all-branches-and-tags)
- [408: A bug appeared in production between release v3.4.0 and v3.5.0. How do you find the cause?](#408-a-bug-appeared-in-production-between-release-v340-and-v350-how-do-you-find-the-cause)
- [409: How do you generate release notes from Git history?](#409-how-do-you-generate-release-notes-from-git-history)
- [410: How do you embed the Git version into a build?](#410-how-do-you-embed-the-git-version-into-a-build)
- [411: What are the pros and cons of deploying with "git pull" on the server?](#411-what-are-the-pros-and-cons-of-deploying-with-git-pull-on-the-server)
- [412: What is GitOps?](#412-what-is-gitops)
- [413: Why should you add .git to .dockerignore?](#413-why-should-you-add-git-to-dockerignore)
- [414: Your pre-commit hook takes 40 seconds and developers keep skipping it. What do you do?](#414-your-pre-commit-hook-takes-40-seconds-and-developers-keep-skipping-it-what-do-you-do)
- [415: How do you enforce the same Git rules across hundreds of repositories?](#415-how-do-you-enforce-the-same-git-rules-across-hundreds-of-repositories)
- [416: What makes a commit history easy to work with later?](#416-what-makes-a-commit-history-easy-to-work-with-later)
- [417: Should generated files be committed?](#417-should-generated-files-be-committed)
- [418: Why is Git bad at large binary files?](#418-why-is-git-bad-at-large-binary-files)
- [419: Why is "one branch per environment" (dev, staging, prod) considered an anti-pattern?](#419-why-is-one-branch-per-environment-dev-staging-prod-considered-an-anti-pattern)
- [420: You need to remove a feature now but bring it back later. How do you do it with Git?](#420-you-need-to-remove-a-feature-now-but-bring-it-back-later-how-do-you-do-it-with-git)
- [421: How do you plan a history rewrite on a shared repository?](#421-how-do-you-plan-a-history-rewrite-on-a-shared-repository)
- [422: How do you know who actually pushed a commit, not just who authored it?](#422-how-do-you-know-who-actually-pushed-a-commit-not-just-who-authored-it)
- [423: How do you run several AI coding agents or tasks on one repo in parallel without conflicts?](#423-how-do-you-run-several-ai-coding-agents-or-tasks-on-one-repo-in-parallel-without-conflicts)
- [424: What changed in the git config command in recent versions?](#424-what-changed-in-the-git-config-command-in-recent-versions)
- [425: What is planned for Git 3.0?](#425-what-is-planned-for-git-30)
- [426: What happens step by step when you run git clone?](#426-what-happens-step-by-step-when-you-run-git-clone)
- [427: What happens on the server when you run git push?](#427-what-happens-on-the-server-when-you-run-git-push)
- [428: What does a "missing object" or "bad object" error usually mean?](#428-what-does-a-missing-object-or-bad-object-error-usually-mean)
- [429: What do the ^{}, ^{tree} and :/ revision suffixes do?](#429-what-do-the--tree-and--revision-suffixes-do)
- [430: Why should you never move a tag that was already pushed?](#430-why-should-you-never-move-a-tag-that-was-already-pushed)
- [431: What is a signed push?](#431-what-is-a-signed-push)
- [432: Why does a rebase change commit hashes even when there are no conflicts and no content changes?](#432-why-does-a-rebase-change-commit-hashes-even-when-there-are-no-conflicts-and-no-content-changes)
- [433: Can two different commits have the same tree?](#433-can-two-different-commits-have-the-same-tree)
- [434: What is git patch-id?](#434-what-is-git-patch-id)
- [435: How can you tell whether a squash-merged branch is really in main?](#435-how-can-you-tell-whether-a-squash-merged-branch-is-really-in-main)
- [436: How does Git handle conflicts in binary files?](#436-how-does-git-handle-conflicts-in-binary-files)
- [437: How do you rebase a branch that has merge commits in it?](#437-how-do-you-rebase-a-branch-that-has-merge-commits-in-it)
- [438: How do you restore a folder to how it was at an old commit while keeping history?](#438-how-do-you-restore-a-folder-to-how-it-was-at-an-old-commit-while-keeping-history)
- [439: How do you scan a repository's full history for leaked secrets?](#439-how-do-you-scan-a-repositorys-full-history-for-leaked-secrets)
- [440: How would you design a branching and release process for a mobile app that supports several versions at once?](#440-how-would-you-design-a-branching-and-release-process-for-a-mobile-app-that-supports-several-versions-at-once)
- [441: Why might git log show commits out of date order?](#441-why-might-git-log-show-commits-out-of-date-order)
- [442: What is the difference between git reset --keep and --hard?](#442-what-is-the-difference-between-git-reset---keep-and---hard)
- [443: How do you safely clean up hundreds of stale remote branches?](#443-how-do-you-safely-clean-up-hundreds-of-stale-remote-branches)
- [444: How do you find which commits are on main but not yet deployed?](#444-how-do-you-find-which-commits-are-on-main-but-not-yet-deployed)
- [445: How would you explain the Git data model in one minute in an interview?](#445-how-would-you-explain-the-git-data-model-in-one-minute-in-an-interview)
- [446: What is the difference between git revert and git restore for undoing changes to a file?](#446-what-is-the-difference-between-git-revert-and-git-restore-for-undoing-changes-to-a-file)
- [447: How do you handle a merge where both sides renamed the same file differently?](#447-how-do-you-handle-a-merge-where-both-sides-renamed-the-same-file-differently)
- [448: What is git fetch --refetch?](#448-what-is-git-fetch---refetch)
- [449: How do you check if your local Git setup will cause problems for the team?](#449-how-do-you-check-if-your-local-git-setup-will-cause-problems-for-the-team)
- [450: What changed in recent Git versions that you should know about?](#450-what-changed-in-recent-git-versions-that-you-should-know-about)

---

# Easy Questions (1-150)

## 1: What is Git?

Git is a distributed version control system. It keeps track of changes to files over time, so you can see who changed what, go back to an older version and work on several things in parallel using branches.

It was created by Linus Torvalds in 2005 for Linux kernel development. Today it is the standard version control tool for almost all software projects.

## 2: What is version control and why do we need it?

Version control is a way to record changes to a set of files so you can get back any earlier version later.

Without it, people end up with folders like `project-final`, `project-final-2` and `project-really-final`. With version control you get:

- A full history of every change, with author, date and message
- The ability to undo mistakes
- Safe parallel work through branches
- A way to merge work from many people

## 3: What does it mean that Git is distributed?

Every clone of a Git repository is a full copy, with the complete history. You don't need a connection to a central server to commit, look at the log, create branches or diff versions.

Servers like GitHub or GitLab are just other copies that the team agreed to treat as the main one. If the server dies, any developer's clone can be used to restore it.

## 4: What is the difference between Git and GitHub?

Git is the version control tool that runs on your machine. GitHub is a hosting service for Git repositories, with extra features on top: pull requests, code review, issues, Actions for CI, permissions and so on.

GitLab, Bitbucket and Azure DevOps are other services in the same space. You can use Git without any of them.

## 5: What is the difference between Git and older tools like SVN?

SVN is centralized: there is one server with the history, and most operations (commit, log, diff against old versions) need the network. Git is distributed, so every clone has the full history and most commands are local and fast.

Other differences:

- Branching in SVN copies directories on the server. In Git a branch is just a pointer to a commit, so it is cheap.
- Git stores snapshots of the whole project. SVN stores changes per file.
- Git has a staging area. SVN does not.

## 6: What is a repository?

A repository (repo) is a project tracked by Git. It is made of your working files plus a hidden `.git` folder that holds the whole history: commits, branches, tags and config.

If you delete the `.git` folder, the files stay but the history is gone and the folder is no longer a Git repo.

## 7: How do you create a new Git repository?

Go into the project folder and run `git init`.

```bash
mkdir my-app
cd my-app
git init
```

This creates the `.git` folder. You can also pass a folder name: `git init my-app`. To set the name of the first branch, use `git init -b main`.

## 8: How do you clone a repository?

Use `git clone` with the URL of the remote repository.

```bash
git clone https://github.com/user/repo.git
git clone git@github.com:user/repo.git my-folder
```

Git downloads the whole history, sets up a remote called `origin` that points to the URL, and checks out the default branch.

## 9: What is the working directory?

The working directory (or working tree) is the set of files you see and edit on disk. It shows one version of the project, usually the latest commit of the current branch plus any changes you made.

Changes in the working directory are not saved in Git until you stage and commit them.

## 10: What is the staging area?

The staging area (also called the index) is a middle step between your working directory and a commit. You use `git add` to put changes there, and `git commit` takes what is in the staging area and saves it as a new commit.

This lets you choose exactly what goes into a commit. For example, you changed five files but only want to commit two of them.

## 11: What are the three main states of a file in Git?

- **Modified:** the file changed in the working directory, but the change is not staged yet.
- **Staged:** the change was added to the staging area and will go into the next commit.
- **Committed:** the change is saved in the repository history.

There is also **untracked**, which means Git has never been told about the file.

## 12: What is a commit?

A commit is a snapshot of the whole project at a point in time. It stores:

- A pointer to the tree (the snapshot of files and folders)
- A pointer to the parent commit or commits
- The author and committer, with dates
- The commit message

Each commit has a unique ID, a hash like `a1b2c3d...`, calculated from its content.

## 13: How do you make a commit?

Stage the changes and then commit them with a message.

```bash
git add index.js
git commit -m "Add login form validation"
```

If you run `git commit` without `-m`, Git opens your editor so you can write a longer message.

## 14: What does git status show?

`git status` shows the current state of your working directory and staging area:

- Which branch you are on and if it is ahead of or behind its remote branch
- Staged changes ("Changes to be committed")
- Changes that are not staged
- Untracked files

`git status -s` gives a short version with two-letter codes per file.

## 15: What does git add do?

`git add` moves changes from the working directory into the staging area.

```bash
git add file.txt      # one file
git add src/          # a folder
git add .             # everything in the current folder and below
git add -A            # all changes in the whole repo, including deletions
```

The file content is saved at the moment you run `git add`. If you edit the file again after that, you need to add it again.

## 16: What is the difference between git add ., git add -A and git add -u?

- `git add .` stages new, modified and deleted files in the current folder and its subfolders.
- `git add -A` stages new, modified and deleted files in the whole repository, no matter where you run it.
- `git add -u` stages modified and deleted files only. It does not add new untracked files.

Since Git 2.0, `git add .` also stages deletions, so it is the same as `git add -A` when you run it from the repo root.

## 17: How do you see the commit history?

Use `git log`.

```bash
git log
git log --oneline
git log --oneline --graph --all
git log -5                # last 5 commits
```

`--oneline` shows one line per commit with a short hash. `--graph` draws the branch lines, and `--all` includes all branches, not only the current one.

## 18: What does git diff show?

`git diff` shows the line by line changes between two versions.

```bash
git diff                 # working directory vs staging area
git diff --staged        # staging area vs last commit
git diff HEAD            # working directory vs last commit
git diff main feature    # between two branches
```

`--cached` is the same as `--staged`.

## 19: What is a branch?

A branch is a movable pointer to a commit. When you make a new commit on a branch, the pointer moves forward to the new commit.

Branches let you work on a feature or fix without touching the main line of code. Because a branch is just a small file with a commit hash, creating one is almost free.

## 20: How do you create a new branch?

```bash
git branch feature-login          # create, but stay on the current branch
git switch -c feature-login       # create and switch to it
git checkout -b feature-login     # older way, same result
```

The new branch starts from the commit you are on now, unless you pass a different start point: `git switch -c hotfix v1.2.0`.

## 21: How do you switch between branches?

```bash
git switch main
git switch -          # go back to the previous branch
```

`git switch` was added in Git 2.23 to split the branch part of `git checkout` into its own command. `git checkout main` still works and you will see it in a lot of older docs and scripts.

## 22: How do you list branches?

```bash
git branch            # local branches
git branch -r         # remote-tracking branches
git branch -a         # both
git branch -vv        # with last commit and upstream info
```

The current branch is marked with `*`.

## 23: How do you delete a branch?

```bash
git branch -d feature-login     # safe delete, only if merged
git branch -D feature-login     # force delete, even if not merged
git push origin --delete feature-login   # delete it on the remote
```

You can't delete the branch you are currently on. Switch to another branch first.

## 24: How do you rename a branch?

```bash
git branch -m new-name              # rename current branch
git branch -m old-name new-name     # rename another branch
```

If the branch was already pushed, push the new name and delete the old one on the remote:

```bash
git push origin -u new-name
git push origin --delete old-name
```

## 25: What is HEAD?

`HEAD` is a pointer to what you have checked out right now. Normally it points to a branch (for example `refs/heads/main`), and that branch points to a commit.

When you commit, the branch that `HEAD` points to moves to the new commit. You can see it with `cat .git/HEAD`.

## 26: What is merging?

Merging combines the changes from one branch into another.

```bash
git switch main
git merge feature-login
```

Git finds the common ancestor of the two branches and applies the changes from both sides. If both sides changed the same lines, you get a merge conflict that you have to fix by hand.

## 27: What is a merge conflict?

A merge conflict happens when Git can't combine changes on its own. Usually it is because both branches changed the same lines of the same file, or one side changed a file that the other side deleted.

Git stops the merge, marks the conflicting parts in the file and waits for you to fix them, stage the files and finish the merge.

## 28: How do you resolve a merge conflict?

1. Run `git status` to see which files have conflicts.
2. Open each file and look for the conflict markers.
3. Edit the file so it has the code you want and remove the markers.
4. Stage the file with `git add`.
5. Finish with `git commit` (or `git merge --continue`).

```text
<<<<<<< HEAD
const timeout = 3000;
=======
const timeout = 5000;
>>>>>>> feature-login
```

The top part is your current branch, the bottom part is the branch being merged. If you want to give up, run `git merge --abort`.

## 29: What is a remote?

A remote is a named link to another copy of the repository, usually on a server like GitHub. When you clone, Git creates a remote called `origin` automatically.

```bash
git remote -v                                   # list remotes with URLs
git remote add upstream https://github.com/org/repo.git
git remote remove upstream
```

## 30: What does git push do?

`git push` sends your local commits to a remote repository and updates the remote branch.

```bash
git push origin main
git push -u origin feature-login    # push and set upstream
git push                            # after upstream is set
```

If the remote has commits you don't have, the push is rejected and you need to pull first.

## 31: What does git pull do?

`git pull` downloads new commits from the remote and integrates them into your current branch. It is basically `git fetch` followed by `git merge` (or `git rebase` if you configured it).

```bash
git pull
git pull origin main
git pull --rebase
```

## 32: What does git fetch do?

`git fetch` downloads new commits, branches and tags from the remote but does not change your working directory or your local branches. It only updates the remote-tracking branches like `origin/main`.

It is safe to run any time. After fetching you can look at what changed before merging:

```bash
git fetch
git log main..origin/main
```

## 33: What is the difference between git fetch and git pull?

`git fetch` only downloads and updates `origin/*` branches. Your files and your local branches stay as they are.

`git pull` does a fetch and then merges or rebases the remote branch into your current branch, so it changes your files.

Many developers prefer to fetch first, look at the changes and then decide how to integrate them.

## 34: What is origin?

`origin` is the default name Git gives to the remote you cloned from. There is nothing special about it, it is just a convention. You can rename it or add more remotes with other names.

`origin/main` is the remote-tracking branch, which is your local copy of where `main` was on `origin` the last time you fetched.

## 35: What is a .gitignore file?

`.gitignore` is a text file that lists files and folders Git should not track. Common examples are dependencies, build output, logs and local env files.

```gitignore
node_modules/
dist/
*.log
.env
.DS_Store
```

It only affects untracked files. If a file is already tracked, adding it to `.gitignore` does nothing until you remove it from the index.

## 36: How do you stop tracking a file that is already committed?

Remove it from the index but keep it on disk, then add it to `.gitignore`.

```bash
git rm --cached .env
echo ".env" >> .gitignore
git commit -m "Stop tracking .env"
```

For a folder, use `git rm -r --cached folder/`. Note that the file still exists in old commits. If it had secrets in it, you need to rotate them.

## 37: How do you configure your name and email in Git?

```bash
git config --global user.name "Jane Doe"
git config --global user.email "jane@example.com"
```

These values go into every commit you make. `--global` saves them in `~/.gitconfig` for all repos. Without `--global`, the setting applies only to the current repo.

## 38: What are the levels of Git configuration?

- **System:** for every user on the machine (`git config --system`), usually in `/etc/gitconfig`.
- **Global:** for your user (`git config --global`), in `~/.gitconfig` or `~/.config/git/config`.
- **Local:** for one repo (`git config --local`, the default), in `.git/config`.
- **Worktree:** for one worktree, if `extensions.worktreeConfig` is on.

Lower levels override higher ones, so local wins over global. To see where each value comes from, run `git config --list --show-origin`.

## 39: What is a commit hash?

A commit hash is the unique ID of a commit. By default it is a 40 character SHA-1 hash calculated from the commit content: the tree, the parents, the author, the committer and the message.

If anything in the commit changes, the hash changes too. You usually only need the first 7 or so characters, for example `git show a1b2c3d`.

## 40: How do you write a good commit message?

A common format:

- A short summary line, around 50 characters, in imperative mood: "Fix null check in user service", not "Fixed" or "Fixes".
- A blank line.
- A body that explains what changed and why, wrapped at about 72 characters.

```text
Fix crash when user has no avatar

The profile page called avatar.url without checking for null.
Users created before 2023 don't have an avatar, so the page crashed.
```

Many teams also use Conventional Commits, like `fix: handle missing avatar`.

## 41: How do you change the last commit?

Use `git commit --amend`.

```bash
git commit --amend -m "Better message"   # change only the message
git add forgotten-file.js
git commit --amend --no-edit             # add a file, keep the message
```

Amend replaces the last commit with a new one that has a new hash. Don't amend commits that other people already pulled, unless your team is fine with force pushes on that branch.

## 42: How do you discard changes in a file?

```bash
git restore file.js            # discard unstaged changes
git restore --staged file.js   # unstage, keep the changes in the file
```

`git restore` was added in Git 2.23. The older way is `git checkout -- file.js` for discarding and `git reset file.js` for unstaging. Discarded changes that were never staged or committed can't be recovered.

## 43: How do you unstage a file?

```bash
git restore --staged file.js
```

This takes the file out of the staging area but keeps your edits in the working directory. The older command `git reset file.js` does the same thing.

## 44: What does git rm do?

`git rm` deletes a file from the working directory and stages the deletion.

```bash
git rm old-file.js
git rm --cached secrets.txt   # remove from Git only, keep the file on disk
git rm -r old-folder/
```

If you delete a file with your normal file manager, you can still stage the deletion with `git add` or `git rm`.

## 45: How do you rename or move a file in Git?

```bash
git mv old-name.js new-name.js
```

This is the same as moving the file yourself, then running `git rm` on the old path and `git add` on the new one. Git doesn't store renames. It detects them later by comparing file content, so `git log --follow new-name.js` can still show the history from before the rename.

## 46: What is git stash?

`git stash` saves your uncommitted changes in a temporary place and cleans your working directory. It is useful when you need to switch branches quickly but your work isn't ready to commit.

```bash
git stash            # save changes
git switch main      # do something else
git switch -         # come back
git stash pop        # bring the changes back
```

## 47: What is the difference between git stash pop and git stash apply?

Both bring back stashed changes. `git stash pop` applies the stash and then removes it from the stash list. `git stash apply` applies it but keeps it in the list, so you can apply it again somewhere else.

If `pop` hits a conflict, the stash is kept, so you don't lose it.

## 48: How do you see what is in your stash?

```bash
git stash list                 # all stashes
git stash show stash@{0}       # files changed
git stash show -p stash@{1}    # full diff
```

`stash@{0}` is the most recent stash. Use `git stash drop stash@{1}` to remove one and `git stash clear` to remove all of them.

## 49: What is a tag?

A tag is a name that points to a specific commit, usually used to mark releases like `v1.0.0`. Unlike a branch, a tag doesn't move when you make new commits.

```bash
git tag v1.0.0
git tag -a v1.1.0 -m "Release 1.1.0"
git tag                      # list tags
```

## 50: What is the difference between a lightweight tag and an annotated tag?

A lightweight tag is just a name pointing to a commit, like a branch that never moves.

An annotated tag is a full object in the Git database. It has its own tagger name, email, date and message, and it can be signed. Use annotated tags for releases.

```bash
git tag v1.0.0-temp               # lightweight
git tag -a v1.0.0 -m "First release"   # annotated
```

## 51: How do you push tags to the remote?

Tags are not pushed by default with `git push`. You push them explicitly.

```bash
git push origin v1.0.0       # one tag
git push origin --tags       # all local tags
git push --follow-tags       # commits plus annotated tags that point to them
```

To delete a remote tag: `git push origin --delete v1.0.0`.

## 52: What is git show used for?

`git show` displays details of an object. For a commit, it shows the author, date, message and the diff.

```bash
git show                    # last commit
git show a1b2c3d            # a specific commit
git show v1.0.0             # a tag and the commit it points to
git show HEAD~1:src/app.js  # a file as it was one commit ago
```

## 53: What is the default branch?

The default branch is the branch Git creates in a new repo and the one a clone checks out first. On GitHub and GitLab it is usually `main`. Older repos often use `master`.

You can set what `git init` uses:

```bash
git config --global init.defaultBranch main
```

Git 3.0 is planned to use `main` by default for new repos when nothing is configured.

## 54: What is the difference between master and main?

There is no technical difference. They are just branch names. Git used `master` as the default name for years. In 2020 GitHub, GitLab and others switched their default for new repos to `main`, and Git added the `init.defaultBranch` setting so you can choose.

## 55: What is a fast-forward merge?

A fast-forward merge happens when the branch you are merging into has no new commits since the other branch was created. Git doesn't need to create a merge commit. It just moves the pointer forward.

```text
Before:  main: A - B
                    \
         feature:    C - D

After:   main: A - B - C - D
```

## 56: What is a merge commit?

A merge commit is a commit with two (or more) parents. Git creates one when both branches have new commits and it needs to join the two lines of history.

```bash
git merge feature        # creates a merge commit if a fast-forward isn't possible
git merge --no-ff feature  # always create a merge commit
```

## 57: What is rebasing?

Rebasing moves your commits so they start from a different base commit. Git takes each of your commits, and replays them one by one on top of the new base.

```bash
git switch feature
git rebase main
```

The result is a straight line of history, as if you had started your work from the latest `main`. Rebased commits get new hashes.

## 58: What is the difference between merge and rebase?

Both bring changes from one branch into another.

- **Merge** keeps the history as it happened and adds a merge commit. Nothing is rewritten.
- **Rebase** rewrites your commits on top of the other branch, so the history is linear. The old commits are replaced with new ones.

Merge is safer for shared branches. Rebase gives cleaner history for local or personal branches. A common rule: don't rebase commits that other people already have.

## 59: What is git clone --depth used for?

`--depth` makes a shallow clone with only the latest commits instead of the full history.

```bash
git clone --depth 1 https://github.com/user/repo.git
```

It's faster and uses less space, which helps in CI. The downside is that commands like `git log`, `git blame` and `git describe` only see the history you downloaded. You can get the rest later with `git fetch --unshallow`.

## 60: What is git log --oneline?

It shows the history with one line per commit: the short hash and the first line of the message.

```text
3f2a1c9 Fix typo in README
8b7d6e5 Add login page
1a2b3c4 Initial commit
```

It's a quick way to scan recent commits.

## 61: How do you see the history of a single file?

```bash
git log -- path/to/file.js
git log -p -- path/to/file.js         # with diffs
git log --follow -- path/to/file.js   # follow renames
```

The `--` separates options and branch names from file paths. It's optional when there is no doubt, but it's a good habit.

## 62: What is git blame?

`git blame` shows, for each line of a file, which commit last changed it, who made that commit and when.

```bash
git blame src/app.js
git blame -L 10,20 src/app.js    # only lines 10 to 20
```

It is useful for finding out why a line looks the way it does. Most editors and GitHub have a blame view too.

## 63: How do you undo a commit that was already pushed?

Use `git revert`. It creates a new commit that does the opposite of the old one, so history is not rewritten and it is safe on shared branches.

```bash
git revert a1b2c3d
git push
```

`git reset` would also undo the commit, but it rewrites history and needs a force push, which can break things for your teammates.

## 64: What does git reset do?

`git reset` moves the current branch pointer to another commit. Depending on the mode, it also changes the staging area and working directory.

```bash
git reset --soft HEAD~1    # undo last commit, keep changes staged
git reset HEAD~1           # undo last commit, keep changes unstaged (--mixed is default)
git reset --hard HEAD~1    # undo last commit and throw away the changes
```

Be careful with `--hard`: uncommitted changes are lost.

## 65: What is the difference between git reset --soft, --mixed and --hard?

All three move the branch to the given commit. The difference is what happens to your changes:

- `--soft`: staging area and working directory stay as they are. Changes from the undone commits show as staged.
- `--mixed` (default): staging area is reset, working directory stays. Changes show as unstaged.
- `--hard`: staging area and working directory are reset. Changes are gone.

## 66: What is the difference between git revert and git reset?

`git revert` adds a new commit that undoes an old one. History stays as it is, so it's safe for branches others use.

`git reset` moves the branch pointer back, which removes commits from the branch. That rewrites history, so it's fine for local work but on a shared branch it needs a force push.

## 67: What does HEAD~1 mean?

`HEAD~1` means the parent of the current commit. `HEAD~2` is the grandparent, and so on. You can use it with any ref, like `main~3`.

```bash
git show HEAD~1
git diff HEAD~3 HEAD
git reset --soft HEAD~2
```

`HEAD~` without a number is the same as `HEAD~1`.

## 68: What is the difference between HEAD~ and HEAD^?

Both go back to the first parent by default, so `HEAD~` and `HEAD^` are the same commit.

The difference shows with merge commits, which have more than one parent:

- `HEAD^2` is the second parent of `HEAD` (the branch that was merged in).
- `HEAD~2` is the first parent of the first parent (two steps back along the main line).

## 69: What is a detached HEAD?

Detached HEAD means `HEAD` points directly to a commit instead of to a branch. It happens when you check out a commit hash, a tag or a remote branch directly.

```bash
git switch --detach v1.0.0
git checkout a1b2c3d
```

You can look around and even commit, but those commits don't belong to any branch. If you switch away, they become hard to find. To keep them, create a branch: `git switch -c my-fix`.

## 70: What is an upstream branch?

An upstream branch is the remote branch your local branch is linked to. It tells `git pull` and `git push` where to go when you don't give arguments, and `git status` uses it to show "ahead" and "behind" counts.

```bash
git push -u origin feature      # push and set upstream
git branch -u origin/feature    # set upstream for an existing branch
git branch -vv                  # see upstreams
```

## 71: What is a remote-tracking branch?

A remote-tracking branch, like `origin/main`, is a local reference that remembers where a branch on the remote was the last time you fetched. You can't commit to it directly. Git updates it when you run `git fetch`, `git pull` or `git push`.

## 72: How do you check out a branch that only exists on the remote?

```bash
git fetch
git switch feature-x
```

If there is exactly one remote with a branch named `feature-x`, `git switch` creates a local branch that tracks `origin/feature-x`. You can also be explicit:

```bash
git switch -c feature-x --track origin/feature-x
```

## 73: What is a pull request?

A pull request (PR) is a feature of hosting services like GitHub, not of Git itself. You push a branch and open a PR to ask for it to be merged into another branch, usually `main`.

The PR shows the diff, lets teammates review and comment, runs CI checks, and has a button to merge when it's approved. GitLab calls the same thing a merge request.

## 74: What is a fork?

A fork is your own copy of someone else's repository on a hosting service. You can push to your fork freely, then open a pull request to propose changes back to the original repo.

Forks are common in open source, where you don't have write access to the main repo. Locally you usually add the original repo as a second remote named `upstream`.

## 75: How do you keep a fork up to date with the original repo?

Add the original repo as a remote, fetch it and merge or rebase.

```bash
git remote add upstream https://github.com/original/repo.git
git fetch upstream
git switch main
git merge upstream/main
git push origin main
```

GitHub also has a "Sync fork" button that does the same on the server.

## 76: What is git cherry-pick?

`git cherry-pick` copies a commit from another branch and applies it on the current branch as a new commit.

```bash
git switch release-1.2
git cherry-pick a1b2c3d
```

It's often used to bring a bug fix from `main` into a release branch without merging everything else.

## 77: What does git clean do?

`git clean` deletes untracked files from the working directory.

```bash
git clean -n      # dry run, show what would be deleted
git clean -f      # delete untracked files
git clean -fd     # also delete untracked folders
git clean -fdx    # also delete ignored files, like node_modules
```

Always run `-n` first. Deleted files are not in Git, so you can't get them back.

## 78: What is the .git folder?

The `.git` folder is where Git keeps everything about the repo:

- `objects/`: all commits, trees and file contents
- `refs/`: branches and tags
- `HEAD`: what is checked out
- `config`: repo settings
- `index`: the staging area
- `hooks/`: sample hook scripts

You normally never edit these files by hand.

## 79: Why does Git not track empty folders?

Git tracks files, not folders. A folder exists in Git only because there are files inside it. If a folder is empty, there's nothing to store.

The usual workaround is to put a placeholder file in it, often called `.gitkeep`. The name has no special meaning to Git, it's just a convention.

## 80: How do you list all tracked files?

```bash
git ls-files
git ls-files src/
```

This lists files that are in the index. To see ignored files, use `git status --ignored` or `git ls-files --others --ignored --exclude-standard`.

## 81: How do you see which files changed in a commit?

```bash
git show --stat a1b2c3d
git show --name-only a1b2c3d
git show --name-status a1b2c3d    # with A, M, D for added, modified, deleted
```

## 82: How do you compare two branches?

```bash
git diff main..feature           # changes between the tips of the two branches
git diff main...feature          # changes on feature since it split from main
git log main..feature            # commits on feature that are not on main
```

For pull requests you usually want the three dot `diff` version, because it shows only what the feature branch added.

## 83: What is the difference between git diff and git diff --staged?

`git diff` shows changes in your working directory that are not staged yet.

`git diff --staged` shows changes that are staged, which is what will go into the next commit.

If you stage everything, `git diff` shows nothing, and `git diff --staged` shows all your changes.

## 84: How do you commit only part of a file?

Use interactive staging with `-p` (patch).

```bash
git add -p file.js
```

Git shows each change (hunk) and asks what to do: `y` to stage it, `n` to skip it, `s` to split it into smaller pieces, `e` to edit it by hand. This is great for splitting unrelated changes into separate commits.

## 85: What does git commit -a do?

`git commit -a` stages all modified and deleted tracked files and commits them in one step.

```bash
git commit -am "Update styles"
```

It does not include new untracked files. You still need `git add` for those.

## 86: How do you see the remote URL?

```bash
git remote -v
git remote get-url origin
```

To change it, for example when switching from HTTPS to SSH:

```bash
git remote set-url origin git@github.com:user/repo.git
```

## 87: What is the difference between HTTPS and SSH for Git remotes?

Both are ways to talk to the remote server.

- **HTTPS** works through most firewalls and proxies. You log in with a username and a personal access token, usually saved by a credential helper.
- **SSH** uses a key pair. You add your public key to the server once, and after that there is no password prompt.

Both are secure. It's mostly a matter of what works better in your setup.

## 88: How do you set up an SSH key for GitHub?

```bash
ssh-keygen -t ed25519 -C "you@example.com"
cat ~/.ssh/id_ed25519.pub
```

Copy the public key into GitHub under Settings, SSH and GPG keys. Then test it:

```bash
ssh -T git@github.com
```

Never share the private key (the file without `.pub`).

## 89: What is a credential helper?

A credential helper stores your HTTPS username and token so Git doesn't ask for them every time.

```bash
git config --global credential.helper osxkeychain   # macOS
git config --global credential.helper manager       # Git Credential Manager
git config --global credential.helper cache         # keep in memory for 15 minutes
```

Avoid the `store` helper on shared machines. It saves the token in a plain text file.

## 90: What is a Git alias?

An alias is a short name for a longer Git command.

```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.lg "log --oneline --graph --all"
```

After that, `git lg` runs `git log --oneline --graph --all`. If an alias starts with `!`, it runs as a shell command.

## 91: How do you set the default editor for Git?

```bash
git config --global core.editor "code --wait"   # VS Code
git config --global core.editor "vim"
git config --global core.editor "nano"
```

The `--wait` flag is important for GUI editors. Without it, Git thinks you are done as soon as the editor opens.

## 92: What is git reflog?

`git reflog` shows a log of where `HEAD` and your branches have pointed over time, including commits that are no longer on any branch.

```bash
git reflog
```

It's the main tool for recovering lost work, for example after a bad `reset --hard` or a rebase that went wrong. The reflog is local only and entries expire after some time (90 days by default for reachable entries).

## 93: How do you recover a deleted branch?

Find the last commit of the branch in the reflog and create the branch again.

```bash
git reflog
# a1b2c3d HEAD@{3}: checkout: moving from feature-x to main
git branch feature-x a1b2c3d
```

When you delete a branch with `git branch -d`, Git also prints the commit hash it pointed to, so you can use that too.

## 94: How do you undo git add?

```bash
git restore --staged file.js
git restore --staged .      # unstage everything
```

Your changes stay in the working directory. Only the staging area is updated.

## 95: How do you see who made changes to a file?

```bash
git log --format="%h %an %ad %s" -- file.js
git shortlog -sn -- file.js     # count of commits per author
git blame file.js               # per line
```

## 96: What is git shortlog?

`git shortlog` groups commits by author. It's handy for release notes or for seeing who works on what.

```bash
git shortlog -sn            # commit counts per author, sorted
git shortlog v1.0.0..v1.1.0 # commits between two tags, grouped by author
```

## 97: How do you search the commit history by message?

```bash
git log --grep="login"
git log --grep="fix" -i     # case-insensitive
git log --author="Jane"
git log --since="2 weeks ago"
```

You can combine these options to narrow the results.

## 98: How do you find a commit that added or removed a piece of code?

Use the pickaxe option `-S`.

```bash
git log -S "calculateTotal" --oneline
git log -S "calculateTotal" -p     # with the diffs
```

`-S` finds commits where the number of times the string appears changed. `-G` takes a regex and finds commits where a changed line matches it.

## 99: What is git grep?

`git grep` searches for text in tracked files. It's often faster than regular `grep` because it skips ignored and untracked files.

```bash
git grep "TODO"
git grep -n "useEffect" -- "*.tsx"   # with line numbers, only .tsx files
git grep "apiKey" v1.0.0             # search an old version
```

## 100: What happens if you run git commit without staging anything?

Git doesn't create a commit. It prints a message like "no changes added to commit" or "nothing to commit, working tree clean".

If you really want an empty commit, for example to trigger a CI build, use:

```bash
git commit --allow-empty -m "Trigger build"
```

## 101: How do you see the changes of a specific commit?

```bash
git show a1b2c3d
git diff a1b2c3d~1 a1b2c3d
```

Both show the diff that the commit introduced. `git show` also prints the author, date and message.

## 102: What is git switch?

`git switch` is a command for changing branches. It was added in Git 2.23 together with `git restore`, because `git checkout` did too many different things.

```bash
git switch main
git switch -c new-branch
git switch --detach a1b2c3d
```

It only deals with branches, so it can't overwrite files by mistake like `git checkout file` can.

## 103: What is git restore?

`git restore` restores files in the working directory or staging area. It's the file part of the old `git checkout` and `git reset file` commands.

```bash
git restore file.js                      # discard unstaged changes
git restore --staged file.js             # unstage
git restore --source=HEAD~2 file.js      # get the file as it was two commits ago
```

## 104: Why was git checkout split into git switch and git restore?

`git checkout` did two very different things: switching branches and overwriting files. That was confusing, and it was easy to lose work. For example, `git checkout name` could switch to a branch or discard changes in a file called `name`, depending on what existed.

The new commands make the intent clear: `switch` for branches, `restore` for files. `checkout` still works and isn't going away.

## 105: How do you create a branch from a specific commit?

```bash
git switch -c bugfix a1b2c3d
git branch bugfix v1.2.0
```

Any commit, tag or branch name can be used as the starting point.

## 106: How do you check which branch you are on?

```bash
git branch --show-current
git status
```

Your terminal prompt can also show it if you use a Git-aware shell prompt.

## 107: What is the difference between git pull with merge and git pull with rebase?

With merge (the classic default), Git merges the remote branch into your local branch. If both have new commits, you get a merge commit.

With rebase, Git puts your local commits on top of the remote commits, so the history stays linear.

```bash
git pull --rebase
git config --global pull.rebase true    # make it the default
```

Recent Git versions ask you to choose (merge, rebase or fast-forward only) when a pull would need to combine diverged histories.

## 108: How do you set up Git to only fast-forward on pull?

```bash
git config --global pull.ff only
```

With this, `git pull` only works if your branch can be fast-forwarded. If you have local commits that the remote doesn't have, the pull fails and you decide yourself whether to merge or rebase.

## 109: What does "your branch is ahead of origin/main by 2 commits" mean?

You have 2 local commits that are not on the remote yet. Push them with `git push`.

"Behind" means the remote has commits you don't have, so you need to pull. "Diverged" means both sides have new commits, so you need to merge or rebase.

## 110: What does git push --force do?

`git push --force` overwrites the remote branch with your local branch, even if the remote has commits you don't have. Those commits are removed from the branch.

It's needed after you rewrite history (rebase, amend, reset) on a branch that was already pushed. It's dangerous on shared branches because it can delete other people's work. Use `--force-with-lease` instead.

## 111: What is git push --force-with-lease?

It's a safer force push. Git only overwrites the remote branch if it's still where you last saw it (your `origin/branch`). If someone else pushed in the meantime, the push is rejected.

```bash
git push --force-with-lease
```

It protects you from overwriting a teammate's commits by accident.

## 112: What is a README file?

A README is a file in the root of the repo, usually `README.md`, that explains what the project is, how to install and run it, and how to contribute. GitHub and GitLab show it on the repo's main page.

It's not a Git feature, just a very common convention.

## 113: What is Markdown and why is it used in Git repos?

Markdown is a simple text format that uses symbols like `#` for headings and `*` for lists. It's easy to read as plain text and hosting services render it as nice HTML.

READMEs, changelogs, docs and pull request descriptions are usually written in Markdown.

## 114: How do you clone a specific branch?

```bash
git clone -b develop https://github.com/user/repo.git
git clone -b develop --single-branch https://github.com/user/repo.git
```

`-b` checks out that branch after cloning. `--single-branch` also limits the download to that branch's history.

## 115: How do you see the last commit?

```bash
git log -1
git show
git log -1 --format="%H %s"   # full hash and message only
```

## 116: How do you list files changed between two commits?

```bash
git diff --name-only a1b2c3d e4f5g6h
git diff --name-status main feature
```

This is often used in CI scripts to run only the tests for the parts of the code that changed.

## 117: What is a hook in Git?

A hook is a script that Git runs automatically at certain points, like before a commit or before a push. Hooks live in `.git/hooks/` by default.

Common uses:

- `pre-commit`: run a linter or formatter
- `commit-msg`: check the commit message format
- `pre-push`: run tests before pushing

If a hook exits with a non-zero code, Git stops the action.

## 118: How do you ignore a file only on your machine?

Add it to `.git/info/exclude`. It works like `.gitignore`, but it's not committed, so it only affects your local copy.

For patterns you want ignored in all your repos (like editor files), use a global ignore file:

```bash
git config --global core.excludesFile ~/.gitignore_global
```

## 119: How do you check why a file is ignored?

```bash
git check-ignore -v path/to/file
```

It prints the ignore file, the line number and the pattern that matched. Useful when a file you need is ignored and you don't know why.

## 120: What are common .gitignore patterns?

```gitignore
# a folder anywhere
node_modules/

# a file type anywhere
*.log

# only in the root
/build

# everything in a folder except one file
config/*
!config/default.json

# any depth
**/temp/
```

A `/` at the end matches folders only. `!` negates a pattern. Lines starting with `#` are comments.

## 121: Can you have more than one .gitignore file?

Yes. You can put a `.gitignore` in any folder, and its patterns apply relative to that folder. Patterns in deeper folders override ones higher up.

Most projects use one in the root, but monorepos often have one per package as well.

## 122: What is git init --bare?

A bare repository has no working directory, only the Git data that usually sits in `.git`. You can't edit files in it directly.

```bash
git init --bare project.git
```

Bare repos are used on servers as the shared place everyone pushes to. GitHub and GitLab store repos in a similar way.

## 123: What is git log --graph?

`--graph` draws ASCII lines next to the log to show branches and merges.

```bash
git log --oneline --graph --all --decorate
```

```text
*   e4f5a6b Merge branch 'feature'
|\
| * c3d4e5f Add search
* | b2c3d4e Fix header
|/
* a1b2c3d Initial commit
```

## 124: How do you see which branches are merged into main?

```bash
git branch --merged main
git branch --no-merged main
```

`--merged` lists branches whose tips are already in `main`, so they are safe to delete. Note that branches merged with squash merge don't show up as merged, because their commits are not in `main`.

## 125: How do you delete local branches that were deleted on the remote?

First remove the stale remote-tracking branches:

```bash
git fetch --prune
git config --global fetch.prune true   # always prune on fetch
```

Local branches are not deleted automatically. `git branch -vv` marks branches whose upstream is gone with `: gone]`, and you can delete those by hand.

## 126: What is the difference between git branch -d and -D?

`-d` deletes a branch only if it's fully merged into its upstream or the current branch. If not, Git refuses and warns you.

`-D` is short for `--delete --force` and deletes the branch no matter what. Unmerged commits are only reachable through the reflog after that.

## 127: What is a conflict marker?

Conflict markers are the lines Git adds to a file to show a conflict:

- `<<<<<<<` starts your side (the current branch)
- `=======` separates the two sides
- `>>>>>>>` ends the other side

With `merge.conflictStyle` set to `diff3` or `zdiff3`, there's also a `|||||||` section that shows the original code from the common ancestor. You must remove all the markers before committing.

## 128: What is git merge --abort?

It cancels a merge that stopped because of conflicts and puts everything back the way it was before you started the merge.

```bash
git merge feature
# conflicts...
git merge --abort
```

Rebase and cherry-pick have the same option: `git rebase --abort`, `git cherry-pick --abort`.

## 129: How do you see the content of a file in another branch without switching?

```bash
git show feature:src/app.js
git show HEAD~3:package.json
```

The format is `<ref>:<path>`. The path is relative to the repo root. You can redirect it to a file to save it.

## 130: How do you get a file from another branch into your current branch?

```bash
git restore --source=feature -- src/app.js
git checkout feature -- src/app.js       # older way
```

`git restore` changes only the working directory unless you add `--staged`. The `git checkout` version updates both the working directory and the staging area.

## 131: What is git describe?

`git describe` gives a human readable name for a commit based on the nearest tag.

```bash
git describe --tags
# v1.4.2-3-g1a2b3c4
```

This means 3 commits after tag `v1.4.2`, at commit `1a2b3c4`. It's often used to generate version numbers in builds. Add `--dirty` to mark uncommitted changes.

## 132: What is semantic versioning and how is it used with Git tags?

Semantic versioning (SemVer) uses `MAJOR.MINOR.PATCH`:

- MAJOR for breaking changes
- MINOR for new features that don't break anything
- PATCH for bug fixes

Teams usually tag releases with these numbers, often with a `v` in front: `v2.3.1`. Release tools read the tags to decide the next version.

## 133: How do you see all the tags that contain a commit?

```bash
git tag --contains a1b2c3d
git branch --contains a1b2c3d
```

This answers questions like "which releases include this bug fix?"

## 134: How do you check out a tag?

```bash
git switch --detach v1.2.0
git checkout v1.2.0
```

You end up in a detached HEAD state, because a tag is not a branch. If you want to make changes on top of it, create a branch: `git switch -c fix-1.2 v1.2.0`.

## 135: What does git commit --amend --no-edit do?

It adds whatever is staged to the last commit and keeps the same message. It's the usual way to fix "forgot to add a file" or "small typo" right after committing.

## 136: How do you remove a file from the last commit?

```bash
git reset --soft HEAD~1
git restore --staged unwanted-file.txt
git commit -c ORIG_HEAD
```

Or, without undoing the commit:

```bash
git rm --cached unwanted-file.txt
git commit --amend --no-edit
```

The second version keeps the file on disk but removes it from the commit.

## 137: How do you change the author of the last commit?

```bash
git commit --amend --author="Jane Doe <jane@example.com>" --no-edit
```

If the wrong author came from your config, fix the config first and use `git commit --amend --reset-author --no-edit`.

## 138: What is the difference between author and committer?

The author is the person who wrote the change. The committer is the person who last applied it to the repo.

Usually they're the same. They differ when you cherry-pick, rebase or apply someone else's patch: the original person stays the author, and you become the committer.

```bash
git log --format="%an (author) / %cn (committer)"
```

## 139: What does git log --stat show?

It shows the list of files changed in each commit with the number of lines added and removed.

```text
 src/app.js    | 12 ++++++++----
 src/utils.js  |  3 +++
 2 files changed, 11 insertions(+), 4 deletions(-)
```

## 140: How do you see the history of a specific line range?

```bash
git log -L 10,25:src/app.js
git log -L :calculateTotal:src/cart.js    # history of a function
```

`-L` follows a range of lines through history and shows how they changed in each commit.

## 141: What is a hunk?

A hunk is one block of changes in a diff. It starts with a header like `@@ -10,6 +10,8 @@`, which means the old file had 6 lines starting at line 10 and the new file has 8 lines starting at line 10.

Tools like `git add -p` work hunk by hunk.

## 142: How do you see a word by word diff?

```bash
git diff --word-diff
git diff --color-words
```

It's handy for text files and docs where a line diff would show the whole paragraph as changed.

## 143: What does git checkout . do?

It discards all unstaged changes in the current folder and below by restoring files from the staging area. The modern version is:

```bash
git restore .
```

Untracked files are not touched. Use `git clean` for those.

## 144: What is git commit -v?

`-v` (verbose) shows the full diff of what you're committing at the bottom of the commit message editor. It helps you write a better message and catch things you didn't mean to commit. The diff is not included in the message itself.

## 145: How do you find out which Git version you have?

```bash
git --version
```

It's worth keeping Git up to date, because new versions add features and fix security problems. On macOS, the Apple version that comes with Xcode tools is often a bit behind the official release.

## 146: What is GitHub Desktop or a Git GUI?

They are graphical apps that run Git commands for you: staging, committing, branching, resolving conflicts. Examples are GitHub Desktop, GitKraken, Sourcetree, Fork, and the Git panels built into VS Code and JetBrains IDEs.

They're fine to use, but in interviews you are usually expected to know the command line, because GUIs hide what is really going on.

## 147: What does "working tree clean" mean?

It means you have no uncommitted changes: nothing modified, nothing staged and no untracked files (other than ignored ones). Your files match the last commit exactly.

## 148: How do you create a branch and push it to the remote?

```bash
git switch -c feature-search
git push -u origin feature-search
```

`-u` sets the upstream so later you can just run `git push` and `git pull`. With `push.autoSetupRemote` set to `true`, a plain `git push` sets it up for you the first time.

## 149: How do you undo the last commit but keep the changes?

```bash
git reset --soft HEAD~1     # changes stay staged
git reset HEAD~1            # changes stay, but unstaged
```

Only do this if the commit wasn't pushed yet, or if you're ready to force push.

## 150: What is a monorepo?

A monorepo is one Git repository that holds many projects, like several apps and shared libraries. The opposite is a polyrepo setup, where each project has its own repo.

Monorepos make it easy to share code and change many projects in one commit. The downside is that the repo can get very big, so you need good tooling (sparse checkout, build caching, tools like Nx or Turborepo).

# Moderate Questions (151-300)

## 151: What is interactive rebase?

Interactive rebase (`git rebase -i`) lets you edit a series of commits before they are replayed. Git opens a list of commits in your editor and you choose what to do with each one.

```bash
git rebase -i HEAD~4
```

```text
pick a1b2c3d Add search API
pick b2c3d4e Fix typo
pick c3d4e5f Add search UI
pick d4e5f6a WIP
```

You can change `pick` to `reword`, `edit`, `squash`, `fixup` or `drop`, or reorder the lines. It's the main tool for cleaning up a branch before opening a pull request.

## 152: What are the main commands in an interactive rebase?

- `pick`: keep the commit as it is
- `reword`: keep the changes, edit the message
- `edit`: stop at this commit so you can change it (amend, split it)
- `squash`: combine with the previous commit and edit the combined message
- `fixup`: combine with the previous commit and drop this commit's message
- `drop`: remove the commit
- `exec`: run a shell command at that point
- `break`: stop here, continue later with `git rebase --continue`

Changing the order of lines changes the order of commits.

## 153: How do you squash several commits into one?

Use interactive rebase and mark all commits except the first as `squash` or `fixup`.

```bash
git rebase -i HEAD~3
```

```text
pick a1b2c3d Add checkout page
fixup b2c3d4e Fix button color
fixup c3d4e5f Fix tests
```

Another quick way when you want all commits on the branch to become one:

```bash
git reset --soft main
git commit -m "Add checkout page"
```

## 154: What is the difference between squash and fixup in interactive rebase?

Both merge a commit into the one before it. `squash` opens the editor with both commit messages so you can write a combined message. `fixup` throws away the message of the commit being merged and keeps the previous message as it is.

`fixup -C` keeps the message of the fixup commit instead.

## 155: What are fixup commits and autosquash?

A fixup commit is a commit made to fix an earlier commit on your branch. Git can then fold it in automatically during rebase.

```bash
git commit --fixup=a1b2c3d
git rebase -i --autosquash main
```

`--fixup` creates a commit with the message `fixup! <original message>`. With `--autosquash`, the rebase todo list already has it moved and marked as `fixup`. Set `rebase.autoSquash true` to make this the default for interactive rebases.

## 156: How do you edit an older commit, not just the last one?

```bash
git rebase -i HEAD~5
# change "pick" to "edit" for the commit you want
# Git stops at that commit
# make your changes
git add .
git commit --amend
git rebase --continue
```

All commits after the edited one get new hashes, because their parent changed.

## 157: How do you split one commit into two?

```bash
git rebase -i HEAD~3
# mark the commit as "edit"
git reset HEAD~1           # undo the commit, keep changes unstaged
git add -p                 # stage the first part
git commit -m "First part"
git add .
git commit -m "Second part"
git rebase --continue
```

## 158: How do you reorder commits?

Run `git rebase -i` and move the lines in the todo list into the order you want. Git applies them from top to bottom.

If the commits touch the same lines, you may get conflicts while replaying them in the new order.

## 159: How do you remove a commit from the middle of a branch?

```bash
git rebase -i a1b2c3d~1
# change "pick" to "drop" for that commit, or delete the line
```

Or in one command:

```bash
git rebase --onto a1b2c3d~1 a1b2c3d
```

If the branch is shared, prefer `git revert a1b2c3d` instead, so history isn't rewritten.

## 160: What happens when there is a conflict during a rebase?

Git stops at the commit that caused the conflict. You then:

1. Fix the conflicted files.
2. Stage them with `git add`.
3. Run `git rebase --continue`.

Other options are `git rebase --skip` to drop that commit, and `git rebase --abort` to go back to how things were before the rebase. You may get conflicts at several commits during one rebase.

## 161: What do "ours" and "theirs" mean during merge and rebase?

During a **merge**, "ours" is the branch you're on and "theirs" is the branch being merged in.

During a **rebase**, it's flipped. Git checks out the base branch and replays your commits on top of it, so "ours" is the branch you're rebasing onto (for example `main`) and "theirs" is your own commit being replayed.

```bash
git checkout --ours file.js     # take our version
git checkout --theirs file.js   # take their version
```

## 162: What is git rebase --onto?

`--onto` lets you move a range of commits to a new base.

```bash
git rebase --onto main feature-a feature-b
```

This takes the commits that are on `feature-b` but not on `feature-a` and replays them on top of `main`. It's useful when you branched off the wrong branch, or when the branch you built on top of was squash merged.

## 163: You branched off a feature branch by mistake. How do you move your branch to main?

```bash
git rebase --onto main feature-a my-branch
```

Only the commits you made on `my-branch` after branching from `feature-a` are moved onto `main`. The commits from `feature-a` stay out of your branch.

## 164: How do you move commits you made on main to a new branch?

If you haven't pushed yet:

```bash
git branch feature           # new branch points at your commits
git reset --hard origin/main # move main back
git switch feature
```

Your commits are now only on `feature`, and `main` matches the remote again.

## 165: How do you move the last commit to another existing branch?

```bash
git switch other-branch
git cherry-pick main          # copy the last commit of main
git switch main
git reset --hard HEAD~1       # remove it from main
```

Only do the reset if the commit wasn't pushed. Otherwise use `git revert` on `main`.

## 166: How do you cherry-pick a range of commits?

```bash
git cherry-pick a1b2c3d..e4f5g6h    # commits after a1b2c3d up to e4f5g6h
git cherry-pick a1b2c3d^..e4f5g6h   # including a1b2c3d
```

Git applies them in order. If one of them conflicts, fix it and run `git cherry-pick --continue`.

## 167: What does git cherry-pick -x do?

`-x` adds a line to the commit message like `(cherry picked from commit a1b2c3d...)`. This makes it clear where the change came from, which is helpful for backports to release branches.

## 168: What are the downsides of cherry-picking?

- The copy is a new commit with a new hash, so Git doesn't know it's the same change. Later merges can bring the same change twice or cause conflicts.
- It's easy to forget to cherry-pick a fix to all the branches that need it.
- Pulling a commit out of context can miss changes it depends on.

It's fine for hotfixes and backports, but if you cherry-pick a lot, your branching model may need a rethink.

## 169: What is a squash merge?

A squash merge takes all commits from a branch and turns them into one new commit on the target branch. The feature's individual commits are not part of the target's history.

```bash
git switch main
git merge --squash feature
git commit -m "Add search feature"
```

GitHub and GitLab offer it as a merge option for pull requests. It keeps `main` history short, but you lose the detailed commit history of the feature on `main`.

## 170: What are the pros and cons of squash merging pull requests?

Pros:

- One commit per feature or fix on `main`, easy to read and revert.
- Messy "WIP" and "fix typo" commits don't pollute history.

Cons:

- Detailed history of the work is lost on `main`.
- `git branch --merged` doesn't see the branch as merged.
- If you keep working on the branch after the squash merge, you get conflicts, since Git doesn't know the commits are already in.

## 171: What is the difference between merge --squash and a regular merge?

A regular merge keeps all commits from the branch and adds a merge commit with two parents.

`--squash` puts all changes into the staging area as if you made them yourself. You then make one normal commit with one parent. There's no link back to the original branch in the history.

## 172: When would you use git merge --no-ff?

`--no-ff` always creates a merge commit, even when a fast-forward is possible. The merge commit makes it clear that a set of commits came from one feature branch, and you can revert the whole feature with one `git revert -m 1`.

Some teams use it for all feature merges to keep that structure visible in the graph.

## 173: How do you revert a merge commit?

You have to tell Git which parent is the main line with `-m`.

```bash
git revert -m 1 a1b2c3d
```

`-m 1` means "keep the first parent", which is usually the branch you merged into. Git creates a commit that undoes all the changes the merge brought in.

## 174: What happens if you revert a merge and later try to merge the same branch again?

Git thinks the old commits from that branch are already merged, because they are in history. So it only brings in commits made after the first merge, and the reverted changes don't come back.

To bring them back, revert the revert commit first:

```bash
git revert <revert-commit-hash>
git merge feature
```

## 175: How do you revert several commits?

```bash
git revert --no-commit a1b2c3d..e4f5g6h
git commit -m "Revert search feature"
```

`--no-commit` (`-n`) applies all the reverts to the working directory and staging area so you can commit them as one. Without it, Git makes one revert commit per commit.

## 176: What is git bisect?

`git bisect` helps you find the commit that introduced a bug using binary search. You mark one commit as good and one as bad, and Git checks out commits in the middle until it finds the first bad one.

```bash
git bisect start
git bisect bad              # current commit is broken
git bisect good v1.2.0      # this release worked
# test, then mark each step:
git bisect good   # or: git bisect bad
git bisect reset  # done, go back
```

With 1,000 commits it needs only about 10 steps.

## 177: How do you automate git bisect?

Give it a script that exits with 0 for good and a non-zero code (except 125) for bad.

```bash
git bisect start HEAD v1.2.0
git bisect run npm test
```

Exit code 125 means "can't test this commit", and Git skips it. When it's done, Git prints the first bad commit.

## 178: What is git rerere?

rerere stands for "reuse recorded resolution". When it's enabled, Git remembers how you resolved a conflict, and next time the same conflict shows up, it resolves it the same way automatically.

```bash
git config --global rerere.enabled true
```

It's helpful when you rebase a long-lived branch many times and keep getting the same conflicts.

## 179: How do you use a merge tool to resolve conflicts?

```bash
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd 'code --wait --merge $REMOTE $LOCAL $BASE $MERGED'
git mergetool
```

Git opens each conflicted file in the tool one by one. Many people just use their editor's built-in conflict UI, which works on the files with conflict markers directly.

## 180: What is the diff3 or zdiff3 conflict style?

By default, conflict markers show your version and their version. With `diff3`, Git also shows the original version from the common ancestor, which helps you see what each side actually changed.

```bash
git config --global merge.conflictStyle zdiff3
```

```text
<<<<<<< HEAD
const limit = 20;
||||||| base
const limit = 10;
=======
const limit = 50;
>>>>>>> feature
```

`zdiff3` (Git 2.35+) is like `diff3` but moves common lines out of the conflict block, so the conflict is smaller.

## 181: How do you take one side completely when resolving a conflict?

For a single file:

```bash
git checkout --ours path/to/file
git checkout --theirs path/to/file
git add path/to/file
```

For the whole merge, use a strategy option:

```bash
git merge -X ours feature     # on conflicts, prefer our side
git merge -X theirs feature   # on conflicts, prefer their side
```

`-X ours` only applies to conflicting parts. Non-conflicting changes from the other branch are still merged.

## 182: What is the difference between git merge -s ours and git merge -X ours?

`-X ours` is an option for the default merge strategy. It merges normally and only uses our side for the parts that conflict.

`-s ours` is a separate strategy that ignores the other branch completely. The result is exactly our tree, but a merge commit is recorded so Git thinks the branch is merged. It's rarely used, mostly to mark an old branch as merged without taking its changes.

## 183: How do you resolve a conflict in package-lock.json or another lock file?

Don't try to fix the lock file by hand. The usual approach:

```bash
git checkout --theirs package-lock.json    # or take main's version
npm install                                # regenerate it from package.json
git add package-lock.json
```

Make sure `package.json` is resolved correctly first, because the lock file is generated from it. The same idea works for `yarn.lock` and `pnpm-lock.yaml`.

## 184: What is the stash with untracked files?

By default, `git stash` only saves tracked files. New files stay in the working directory.

```bash
git stash -u          # include untracked files
git stash -a          # include untracked and ignored files
```

## 185: How do you stash only some files?

```bash
git stash push -m "only api changes" src/api.js src/client.js
git stash push -p       # pick hunks interactively
git stash push --staged # only what is staged (Git 2.35+)
```

`-m` gives the stash a name, so it's easier to find in `git stash list`.

## 186: How do you create a branch from a stash?

```bash
git stash branch new-feature stash@{0}
```

Git creates a new branch from the commit where you made the stash, applies the stash there and drops it if it applied cleanly. It's a good fix when `stash pop` keeps conflicting because the original branch moved on.

## 187: How do you recover a stash you dropped by mistake?

A dropped stash is still a commit object until garbage collection removes it. You can find it with:

```bash
git fsck --no-reflog | grep "dangling commit"
git show <hash>              # check which one it is
git stash apply <hash>
```

When you run `git stash drop`, Git also prints the hash of the dropped stash, so check your terminal history first.

## 188: What is a Git submodule?

A submodule is a Git repository inside another Git repository. The parent repo doesn't store the submodule's files. It stores the URL (in `.gitmodules`) and the exact commit of the submodule to use.

```bash
git submodule add https://github.com/org/shared-lib.git libs/shared
git commit -m "Add shared-lib submodule"
```

It's used to include another project at a fixed version while keeping its history separate.

## 189: How do you clone a repo with submodules?

```bash
git clone --recurse-submodules https://github.com/org/app.git
```

If you already cloned without it:

```bash
git submodule update --init --recursive
```

Without this, the submodule folders are empty.

## 190: How do you update a submodule to a newer version?

```bash
cd libs/shared
git fetch
git switch main
git pull
cd ../..
git add libs/shared
git commit -m "Update shared-lib"
```

Or from the parent repo: `git submodule update --remote libs/shared`. Either way, you have to commit the new submodule pointer in the parent repo.

## 191: What are common problems with submodules?

- People forget `--recurse-submodules` and get empty folders.
- The submodule is in a detached HEAD state by default, so commits made inside it are easy to lose.
- Teammates must run `git submodule update` after pulling, or they use an old version.
- Changes that touch both repos need two commits and two pull requests.

Setting `git config --global submodule.recurse true` helps, because then `pull`, `switch` and others update submodules automatically.

## 192: What is git subtree?

`git subtree` puts another repo's files directly into a folder of your repo, as normal files with history merged in. Unlike submodules, people who clone your repo don't need any extra commands.

```bash
git subtree add --prefix=libs/shared https://github.com/org/shared-lib.git main --squash
git subtree pull --prefix=libs/shared https://github.com/org/shared-lib.git main --squash
```

It's a contrib command, so it might not be installed with every Git package.

## 193: When would you choose a submodule over a subtree?

**Submodule** is better when the other project is developed separately, you want to pin an exact version, and you don't want its files in your history.

**Subtree** is better when you want everything to just work after a normal clone, and you rarely push changes back to the other project.

Many teams avoid both and use a package manager (npm, Maven, Go modules) for shared code instead.

## 194: What is git worktree?

`git worktree` lets you check out more than one branch at the same time, each in its own folder, all sharing one `.git` database.

```bash
git worktree add ../app-hotfix hotfix-branch
git worktree add -b review-pr ../app-review origin/feature
git worktree list
git worktree remove ../app-hotfix
```

It's handy when you need to fix something urgent without stashing your current work, or when you run long tests on one branch while working on another.

## 195: What is the difference between git worktree and cloning the repo twice?

A worktree shares the object database and refs with the main repo, so it takes less disk space and there's no need to fetch twice. A commit in one worktree is visible right away in the others.

One rule: the same branch can't be checked out in two worktrees at once. A second clone has none of these limits, but it's fully separate and you need to push and fetch to share commits.

## 196: What are the most used client-side hooks?

- `pre-commit`: runs before the commit is created. Used for linting, formatting and quick tests.
- `prepare-commit-msg`: can fill in the commit message, for example with a ticket number from the branch name.
- `commit-msg`: checks the final commit message.
- `post-commit`: runs after the commit, usually for notifications.
- `pre-push`: runs before pushing. Used for running tests.
- `post-checkout` and `post-merge`: run after switching branches or merging, for example to reinstall dependencies.

## 197: Why are hooks not shared when you clone a repo?

The `.git/hooks` folder is not part of the repository content, so it isn't pushed or cloned. This is on purpose: if hooks came with a clone, anyone could run code on your machine just by you cloning their repo.

To share hooks, teams commit them in a normal folder and point Git at it with `core.hooksPath`, or use a tool like Husky, lefthook or pre-commit.

## 198: How do you share hooks with your team?

Put the hooks in a tracked folder and set `core.hooksPath`:

```bash
mkdir .githooks
# add .githooks/pre-commit and make it executable
chmod +x .githooks/pre-commit
git config core.hooksPath .githooks
```

Each developer still has to run the config command once, so teams usually do it in a setup script or in an npm `prepare` script. Tools like Husky do exactly this for you.

## 199: What is Husky?

Husky is an npm package that makes it easy to use Git hooks in JavaScript projects. It sets `core.hooksPath` to a `.husky` folder, and hooks in that folder are normal shell scripts committed to the repo.

```bash
npm install --save-dev husky
npx husky init
echo "npx lint-staged" > .husky/pre-commit
```

`husky init` adds a `prepare` script to `package.json`, so hooks are set up when someone runs `npm install`.

## 200: What is lint-staged?

lint-staged runs linters and formatters only on the files that are staged for commit, not on the whole project. That keeps pre-commit hooks fast.

```json
{
  "lint-staged": {
    "*.{js,ts,tsx}": ["eslint --fix", "prettier --write"],
    "*.css": "prettier --write"
  }
}
```

It's usually run from a Husky `pre-commit` hook. If the tools change files, lint-staged adds the changes to the commit.

## 201: How do you enforce a commit message format?

On the client, use a `commit-msg` hook. A common setup in JavaScript projects is commitlint with Husky:

```bash
npm install --save-dev @commitlint/cli @commitlint/config-conventional
echo "export default { extends: ['@commitlint/config-conventional'] };" > commitlint.config.mjs
echo 'npx --no -- commitlint --edit "$1"' > .husky/commit-msg
```

Client hooks can be skipped with `--no-verify`, so if the rule really matters, also check it on the server or in CI (for example a check on the pull request title when you squash merge).

## 202: What are Conventional Commits?

Conventional Commits is a convention for commit messages:

```text
<type>(optional scope): <description>

feat(auth): add password reset
fix: handle empty cart on checkout
docs: update install steps
feat!: drop support for Node 18
```

Common types are `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `ci` and `perf`. `!` or a `BREAKING CHANGE:` footer marks a breaking change. Tools like semantic-release and release-please use these messages to pick the next version and write the changelog.

## 203: How do you skip hooks when committing?

```bash
git commit --no-verify -m "WIP"
git push --no-verify
```

`--no-verify` (`-n` for commit) skips `pre-commit` and `commit-msg` hooks. It's useful in emergencies, but it's also why client hooks can't be your only safety net.

## 204: What is Git Flow?

Git Flow is a branching model with long-lived branches:

- `main`: production releases only, each one tagged
- `develop`: where features are integrated
- `feature/*`: branched from `develop`, merged back into it
- `release/*`: branched from `develop` to prepare a release, merged into `main` and `develop`
- `hotfix/*`: branched from `main` for urgent fixes, merged into `main` and `develop`

It fits products with planned, versioned releases. For web apps that deploy many times a day, it's usually too heavy.

## 205: What is GitHub Flow?

GitHub Flow is a simple model:

1. `main` is always deployable.
2. Create a branch from `main` for each change.
3. Open a pull request, get reviews, run CI.
4. Merge into `main` and deploy.

There are no `develop` or `release` branches. It works well for web apps with continuous deployment.

## 206: What is trunk-based development?

In trunk-based development, everyone integrates into one main branch (the trunk) very often, at least once a day. Branches are short-lived, usually hours to a couple of days, or developers commit to the trunk directly.

Unfinished features are hidden behind feature flags instead of living on long branches. It cuts down on merge conflicts and works well with continuous integration, but it needs good automated tests.

## 207: How do you choose a branching strategy for a team?

Look at how you release:

- Continuous deployment of a web app: GitHub Flow or trunk-based development.
- Versioned releases that need support for older versions (libraries, mobile apps, on-premise software): release branches, maybe Git Flow.
- Many teams in one repo: trunk-based with short-lived branches, feature flags and a merge queue.

Keep it as simple as your release process allows. Every extra long-lived branch means more merging.

## 208: What are feature flags and how do they relate to Git branching?

A feature flag is a switch in code (often controlled by config or a service) that turns a feature on or off at runtime.

With flags, you can merge unfinished work into `main` and deploy it turned off. That means you don't need long-lived feature branches, which avoids big painful merges. The downside is that old flags have to be cleaned up from the code.

## 209: How do you handle a hotfix for production?

With a GitHub Flow style setup:

```bash
git switch -c hotfix/payment-crash main
# fix, commit, open PR, merge into main, deploy
```

With release branches:

```bash
git switch -c hotfix/1.4.1 v1.4.0
# fix and commit
git tag -a v1.4.1 -m "Hotfix 1.4.1"
git switch main
git cherry-pick <fix-commit>    # so the bug isn't back in the next release
```

The key point is that the fix must end up in every branch that will be released later.

## 210: What are release branches?

A release branch is created from `main` when a version is ready to stabilize, for example `release/2.3`. Only bug fixes go into it, and new features keep landing on `main`.

You tag releases from the branch (`v2.3.0`, `v2.3.1`) and can keep supporting old versions while `main` moves forward. Fixes are usually made on `main` first and cherry-picked to release branches.

## 211: What are protected branches?

Protected branches are a feature of GitHub, GitLab and similar services. You can set rules for important branches like `main`:

- No direct pushes, only through pull requests
- Required reviews and passing CI checks
- No force pushes and no deletion
- Signed commits or linear history required

On GitHub, newer "rulesets" do the same thing with more options and can apply to many repos.

## 212: What is a CODEOWNERS file?

`CODEOWNERS` is a file (in the root, `.github/` or `docs/` on GitHub) that maps paths to the people or teams responsible for them.

```text
*                 @org/core-team
/src/payments/    @org/payments-team
*.css             @org/frontend
```

Owners are automatically asked to review pull requests that touch their files. With branch protection, their approval can be required.

## 213: What is a merge queue?

A merge queue makes sure each pull request is tested against the latest `main` plus the other PRs ahead of it before merging. Without it, two PRs can each pass CI on their own but break `main` when both are merged.

GitHub, GitLab and tools like Mergify offer merge queues. They're most useful in busy repos where many PRs merge every day.

## 214: How do you check out someone's pull request locally?

With the GitHub CLI:

```bash
gh pr checkout 123
```

With plain Git, GitHub exposes PRs as special refs:

```bash
git fetch origin pull/123/head:pr-123
git switch pr-123
```

GitLab uses `refs/merge-requests/<id>/head` for the same thing.

## 215: What is a good size for a pull request?

Small enough that a reviewer can understand it in one sitting, often a few hundred lines of real changes at most. Small PRs get reviewed faster, have fewer bugs and are easier to revert.

To keep them small, split big features into steps (refactor first, then the feature), use feature flags, or use stacked PRs. Generated code and lock files don't count much, but it's good to keep them in separate commits.

## 216: What are stacked pull requests?

Stacked PRs are a chain of small branches, each built on the one before:

```text
main <- feature-part-1 <- feature-part-2 <- feature-part-3
```

Each PR is reviewed on its own, so you don't have to wait for part 1 to merge before working on part 2. The hard part is keeping the stack up to date when an earlier branch changes. `git rebase --update-refs` and tools like Graphite or ghstack help with this.

## 217: What does git rebase --update-refs do?

When you rebase a branch, `--update-refs` (Git 2.38+) also moves any other local branches that point to commits being rebased.

```bash
git switch feature-part-3
git rebase --update-refs main
```

With stacked branches, this updates `feature-part-1` and `feature-part-2` too, so you don't have to rebase each one by hand. Set `rebase.updateRefs true` to make it the default.

## 218: How do you update a feature branch with the latest main?

Two options:

```bash
# merge main into the branch (safe, no rewriting)
git switch feature
git merge origin/main

# or rebase the branch onto main (clean, linear, needs force push)
git fetch
git rebase origin/main
git push --force-with-lease
```

Use rebase if you work alone on the branch. Use merge if others also push to it.

## 219: What is git rebase --autostash?

It stashes your uncommitted changes before the rebase starts and applies them back after it's done. Without it, Git refuses to rebase with a dirty working directory.

```bash
git rebase --autostash main
git config --global rebase.autoStash true
```

`git pull --rebase` with `rebase.autoStash` works the same way.

## 220: What is git rebase --exec?

`--exec` runs a command after each commit is replayed. If the command fails, the rebase stops there.

```bash
git rebase -i --exec "npm test" main
```

It's a simple way to make sure every commit on your branch builds and passes tests, which makes `git bisect` much more useful later.

## 221: How do you rebase the very first commit of a repo?

```bash
git rebase -i --root
```

`--root` includes the root commit in the list, so you can reword, squash or edit it like any other commit.

## 222: What is ORIG_HEAD?

`ORIG_HEAD` is a ref that Git sets before commands that move `HEAD` a lot, like `reset`, `merge` and `rebase`. It points to where `HEAD` was before.

```bash
git reset --hard ORIG_HEAD
```

This undoes a merge or rebase you just did. The reflog is more reliable for older states, because `ORIG_HEAD` is overwritten each time.

## 223: What are FETCH_HEAD and MERGE_HEAD?

- `FETCH_HEAD` points to what you last fetched. `git fetch origin main` followed by `git merge FETCH_HEAD` is what `git pull` used to do.
- `MERGE_HEAD` exists during a merge and points to the commit being merged in.
- `CHERRY_PICK_HEAD` and `REVERT_HEAD` work the same way during those commands.

They live as files in `.git` and are removed when the operation finishes.

## 224: What are reflog references like HEAD@{2}?

`HEAD@{n}` means "where HEAD was n moves ago". You can also use time:

```bash
git show HEAD@{2}
git diff main@{yesterday} main
git reset --hard HEAD@{5}
git log -g --oneline          # browse the reflog like a log
```

`@{-1}` means the branch you were on before, which is what `git switch -` uses.

## 225: What does @{u} mean?

`@{u}` (or `@{upstream}`) is the upstream branch of the current branch, like `origin/main`.

```bash
git log @{u}..         # local commits not pushed yet
git log ..@{u}         # remote commits not pulled yet
git reset --hard @{u}  # make local branch match the remote
```

`@{push}` is the branch that `git push` would push to.

## 226: What is the difference between two dots and three dots in git log?

- `git log A..B` shows commits reachable from `B` but not from `A`. In other words, what `B` has that `A` doesn't.
- `git log A...B` shows commits on either side but not on both, which is the difference in both directions.

```bash
git log main..feature                    # what the feature adds
git log --left-right --oneline main...feature
```

`--left-right` marks each commit with `<` or `>` so you can see which side it's on.

## 227: Why does git diff A..B differ from git log A..B?

For `git diff`, `A..B` is just the same as `git diff A B`: compare the two snapshots.

`git diff A...B` compares `B` with the merge base of `A` and `B`, so it shows only what changed on `B` since the branches split. That's what a pull request diff shows. The dots mean different things for `log` and `diff`, which confuses a lot of people.

## 228: What is a merge base?

The merge base is the best common ancestor of two commits, usually where one branch split off from the other.

```bash
git merge-base main feature
```

Git uses it as the starting point for a three-way merge: it compares both branches against the merge base to figure out what each side changed.

## 229: What is a three-way merge?

A three-way merge uses three versions of each file: the merge base, our version and their version.

- If only one side changed a part of the file, Git takes that change.
- If both sides made the same change, Git takes it once.
- If both sides changed the same part differently, that's a conflict.

Compared to a two-way diff, the base lets Git tell who changed what, instead of just seeing that two versions differ.

## 230: What merge strategy does Git use by default?

Since Git 2.34, the default strategy is `ort`. It replaced `recursive`, and it's faster and handles renames better. In recent versions, asking for `recursive` just uses `ort`.

Other strategies:

- `resolve`: older, simple three-way merge
- `octopus`: for merging more than two branches at once
- `ours`: keep our tree, ignore the other side
- `subtree`: for merging a project into a subfolder

## 231: What is an octopus merge?

An octopus merge merges more than two branches in one commit.

```bash
git merge feature-a feature-b feature-c
```

Git uses the `octopus` strategy for this. It refuses to do it if there are conflicts that need manual resolution, so it's only used for branches that don't touch the same code.

## 232: What does git log --first-parent do?

`--first-parent` follows only the first parent of each merge commit. On `main`, that shows the history of `main` itself (merges and direct commits) and hides the individual commits from feature branches.

```bash
git log --oneline --first-parent main
```

It's a nice way to see "what landed on main and when" in a repo that uses merge commits.

## 233: How do you see only merge commits or skip them?

```bash
git log --merges
git log --no-merges
```

`--no-merges` is useful for changelogs, where merge commits like "Merge branch 'main' into feature" are just noise.

## 234: How do you write a custom log format?

```bash
git log --pretty=format:"%h %ad %an %s" --date=short
```

Common placeholders:

- `%H` / `%h`: full / short hash
- `%an` / `%ae`: author name / email
- `%ad` / `%ar`: author date / relative date
- `%s`: subject
- `%d`: ref names (branches, tags)

You can save it as an alias for daily use.

## 235: How do you list branches sorted by most recent commit?

```bash
git branch --sort=-committerdate
git for-each-ref --sort=-committerdate --format="%(committerdate:relative) %(refname:short)" refs/heads/
```

This is useful in big repos to find what you were working on recently or to clean up old branches.

## 236: How do you configure different Git settings for work and personal projects?

Use conditional includes in `~/.gitconfig`:

```ini
[user]
    name = Jane Doe
    email = jane@personal.com

[includeIf "gitdir:~/work/"]
    path = ~/.gitconfig-work
```

```ini
# ~/.gitconfig-work
[user]
    email = jane@company.com
```

Every repo under `~/work/` uses the work email. The trailing `/` matters: it means "this folder and everything inside it".

## 237: What is url.insteadOf?

It rewrites remote URLs automatically.

```bash
git config --global url."git@github.com:".insteadOf "https://github.com/"
```

Now any `https://github.com/...` URL is used as SSH. It's common for private dependencies: npm or Go modules fetch with HTTPS URLs, but your machine uses SSH keys.

## 238: How do you handle line endings across Windows, macOS and Linux?

Windows uses CRLF and macOS and Linux use LF. Mixed line endings create noisy diffs. The most reliable fix is a `.gitattributes` file in the repo:

```gitattributes
* text=auto eol=lf
*.bat text eol=crlf
*.png binary
```

This makes Git store text files with LF in the repo and check them out with the endings you set. It's better than relying on each developer's `core.autocrlf` setting.

## 239: What does core.autocrlf do?

`core.autocrlf` converts line endings when files go in and out of Git:

- `true` (common on Windows): convert LF to CRLF on checkout and CRLF to LF on commit.
- `input` (common on macOS and Linux): convert CRLF to LF on commit, no change on checkout.
- `false`: no conversion.

It's a per-user setting, so different people can end up with different results. A `.gitattributes` file in the repo is the better way to control this.

## 240: How do you fix line endings after adding .gitattributes?

```bash
git add --renormalize .
git commit -m "Normalize line endings"
```

`--renormalize` re-applies the line ending rules to all tracked files, so the repo content matches the new `.gitattributes`.

## 241: What is .gitattributes used for besides line endings?

- Mark files as binary so Git doesn't try to diff or merge them: `*.pdf binary`
- Use a custom diff driver: `*.md diff=markdown`
- Exclude files from `git archive`: `tests/ export-ignore`
- Use a merge driver: `CHANGELOG.md merge=union`
- Hook up filters like Git LFS: `*.psd filter=lfs diff=lfs merge=lfs -text`
- Tell GitHub's Linguist how to count languages: `dist/** linguist-generated`

## 242: What is Git LFS?

Git LFS (Large File Storage) is an extension for big binary files like videos, designs and datasets. Instead of storing the file in Git, it stores a small text pointer, and the real file goes to a separate LFS server.

```bash
git lfs install
git lfs track "*.psd"
git add .gitattributes design.psd
git commit -m "Add design file"
```

Clones stay small and fast because only the versions you check out are downloaded. GitHub and GitLab support LFS, but storage and bandwidth may cost extra.

## 243: How do you move existing large files into Git LFS?

```bash
git lfs migrate import --include="*.psd,*.zip" --everything
```

This rewrites history so the matching files become LFS pointers in all commits. Because history changes, everyone needs to re-clone or reset their branches after you force push.

## 244: How do you sign commits?

You can sign with GPG or, since Git 2.34, with an SSH key:

```bash
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global commit.gpgsign true
git config --global tag.gpgsign true
```

Then add the same public key to GitHub as a "signing key". Signed commits show a "Verified" badge.

## 245: Why sign commits?

Anyone can set `user.name` and `user.email` to anything, so the author on a commit proves nothing. A signature proves the commit was made by someone with the private key.

It matters for open source and for regulated environments. Branch protection can require signed commits on `main`.

## 246: How do you verify a signed commit or tag?

```bash
git log --show-signature -1
git verify-commit a1b2c3d
git verify-tag v1.2.0
```

For SSH signatures, Git needs an allowed signers file to know which keys belong to which people:

```bash
git config --global gpg.ssh.allowedSignersFile ~/.ssh/allowed_signers
```

## 247: What is the "Signed-off-by" line?

`Signed-off-by` is a trailer added with `git commit -s`. It means the author agrees to the project's Developer Certificate of Origin (DCO), which says they have the right to submit the code.

```text
Fix memory leak in parser

Signed-off-by: Jane Doe <jane@example.com>
```

It's not a cryptographic signature. The Linux kernel and many open source projects require it.

## 248: What are commit trailers?

Trailers are `Key: value` lines at the end of a commit message. Tools read them.

```text
Co-authored-by: Sam Lee <sam@example.com>
Reviewed-by: Alex Kim <alex@example.com>
Fixes: #123
```

GitHub uses `Co-authored-by` to show multiple authors. You can add trailers with `git commit --trailer "Reviewed-by: Alex Kim <alex@example.com>"`.

## 249: What is a .mailmap file?

`.mailmap` maps different names and emails of the same person to one identity. It's used by `git shortlog`, `git log` (with `--use-mailmap` or `log.mailmap`) and `git blame`.

```text
Jane Doe <jane@company.com> <jane.doe@old-company.com>
Jane Doe <jane@company.com> jdoe <jdoe@laptop.local>
```

It fixes messy statistics without rewriting history.

## 250: How do you ignore formatting commits in git blame?

List the commits in a file and tell blame to skip them:

```text
# .git-blame-ignore-revs
# Run Prettier on the whole codebase
3f2a1c9e8b7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f
```

```bash
git config blame.ignoreRevsFile .git-blame-ignore-revs
```

Blame then shows the commit before the formatting change for those lines. GitHub reads `.git-blame-ignore-revs` in the repo root automatically. You need full hashes in the file.

## 251: How do you remove a file with secrets from the whole history?

Use `git filter-repo` (a separate tool you install), which replaced the old `git filter-branch`.

```bash
git filter-repo --invert-paths --path config/secrets.json
git push --force --all
git push --force --tags
```

But first, **rotate the secret**. Once it was pushed, assume it's leaked: other clones, forks, CI caches and the hosting service may still have it. Everyone also has to re-clone or reset, because history changed.

## 252: Why is git filter-branch not recommended anymore?

`git filter-branch` is very slow on big repos and easy to get wrong (it has many subtle problems with quoting, refs and tags). Git's own docs print a warning and point to `git filter-repo` instead.

`git filter-repo` is much faster, has safer defaults and covers the common cases (remove files, move folders, rewrite emails) with simple flags.

## 253: How do you stop secrets from being committed in the first place?

- Keep secrets out of the code: use env variables, a secrets manager or files listed in `.gitignore`.
- Commit a `.env.example` with fake values instead of `.env`.
- Run a secret scanner in a `pre-commit` hook, like gitleaks or git-secrets.
- Turn on server-side protection, like GitHub secret scanning and push protection, which blocks pushes that contain known token formats.

## 254: What should you do if you pushed a secret to a public repo?

1. Revoke and rotate the secret right away. This is the most important step, because bots scan public repos within minutes.
2. Check logs for any use of the leaked credential.
3. Remove it from the code and, if needed, from history with `git filter-repo`.
4. Force push and ask the team to re-clone.
5. If it's on GitHub, you may need to contact support to clear cached views, pull request refs and forks.

Rewriting history alone is not enough.

## 255: How do you create a patch file and apply it?

```bash
git format-patch -3                 # one .patch file per commit, last 3 commits
git format-patch main --stdout > feature.patch

git am feature.patch                # apply as commits, keep author and message
git apply changes.diff              # apply a plain diff to the working directory
```

`git am` is used for patches made with `format-patch`. `git apply` only changes files and doesn't create commits. Use `git apply --check` to test first.

## 256: What is the difference between git apply and git am?

`git apply` takes a diff and applies it to your working directory (and the index with `--index`). No commit is made, and there's no author info.

`git am` ("apply mailbox") takes patches made by `git format-patch`, which include the author, date and message, and creates real commits from them. It's how patches sent by email are applied in projects like the Linux kernel.

## 257: How do you create a zip of the repo without the .git folder?

```bash
git archive --format=zip -o release.zip HEAD
git archive --format=tar.gz --prefix=app-1.2.0/ -o app-1.2.0.tar.gz v1.2.0
```

Only tracked files are included. Files marked `export-ignore` in `.gitattributes` are left out.

## 258: What is git bundle?

`git bundle` packs commits and refs into a single file. You can then clone or fetch from that file like from a remote.

```bash
git bundle create repo.bundle --all
git clone repo.bundle my-repo
```

It's used to move repos where there's no network connection between machines, or as a simple full backup.

## 259: How do you compare a file between two branches?

```bash
git diff main feature -- src/app.js
git diff main:src/app.js feature:src/app.js
```

The second form also works when the file has a different path in each branch.

## 260: How do you ignore whitespace changes in a diff?

```bash
git diff -w                 # ignore all whitespace
git diff -b                 # ignore changes in the amount of whitespace
git diff --ignore-blank-lines
```

On GitHub, you can add `?w=1` to a pull request URL to hide whitespace changes. This helps a lot when reviewing indentation changes.

## 261: What does git diff --check do?

It warns about whitespace problems in your changes, like trailing spaces or mixed tabs and spaces, and leftover conflict markers.

```bash
git diff --check
git diff --staged --check
```

It exits with an error if it finds a problem, so it works well in a pre-commit hook.

## 262: How do you see a diff with moved lines highlighted?

```bash
git diff --color-moved
git config --global diff.colorMoved zebra
```

Lines that were moved rather than changed get a different color. It makes refactors much easier to review.

## 263: What diff algorithms does Git have?

- `myers`: the default, fast
- `minimal`: tries harder to produce the smallest diff
- `patience`: better at matching unique lines, often gives more readable diffs for code
- `histogram`: an improved version of patience, fast and usually the most readable

```bash
git diff --diff-algorithm=histogram
git config --global diff.algorithm histogram
```

Many people set `histogram` as their default.

## 264: How does Git detect renames?

Git doesn't record renames. When it compares two commits, it looks at deleted and added files. If an added file is similar enough to a deleted one (50% similar by default), it's reported as a rename.

```bash
git diff -M90%          # only treat files at least 90% similar as renames
git log --follow -- file.js
```

If you rename a file and change most of it in the same commit, Git may see a delete plus an add. It's better to rename in one commit and edit in the next.

## 265: Why does git log --follow only work with one file?

`--follow` tracks renames for a single path by checking each commit for a rename of that exact file. It was built for one file at a time, so it doesn't work with folders or several paths.

For a folder, look at the old and new paths separately, or use `git log --name-status` and search.

## 266: How do you find when a file was deleted?

```bash
git log --diff-filter=D --oneline -- path/to/file.js
git log --all --full-history -- "**/file.js"
```

Then restore it from the commit before the deletion:

```bash
git restore --source=<commit>~1 -- path/to/file.js
```

## 267: How do you find which commit introduced a specific line?

```bash
git blame -L 42,42 src/app.js
git log -S "the exact code" --oneline -- src/app.js
```

If blame shows a formatting or move commit, run blame again on the parent of that commit:

```bash
git blame a1b2c3d~1 -L 42,42 src/app.js
```

`git blame -w -C -M` ignores whitespace and follows lines moved or copied between files.

## 268: How do you change the date of a commit?

```bash
git commit --amend --no-edit --date="2026-01-15 10:00"
GIT_COMMITTER_DATE="2026-01-15 10:00" git commit --amend --no-edit --date="2026-01-15 10:00"
```

`--date` changes the author date. The committer date is set separately, through the `GIT_COMMITTER_DATE` env variable. GitHub mostly shows the author date.

## 269: How do you change the author email on many old commits?

With `git filter-repo` and a mailmap file:

```text
Jane Doe <jane@company.com> <jane@old-laptop.local>
```

```bash
git filter-repo --mailmap my-mailmap.txt
```

This rewrites history, so every commit hash changes. If you only want it fixed in `log` and `shortlog` output, a committed `.mailmap` is enough and doesn't rewrite anything.

## 270: How do you push to two remotes at once?

You can add more than one push URL to a remote:

```bash
git remote set-url --add --push origin git@github.com:org/app.git
git remote set-url --add --push origin git@gitlab.com:org/app.git
git push origin main
```

Now `git push origin` sends to both. Fetching still uses the original URL.

## 271: What does push.default do?

It decides what `git push` does when you don't pass a branch:

- `simple` (default): push the current branch to its upstream, only if the names match
- `current`: push the current branch to a branch with the same name
- `upstream`: push the current branch to its upstream, even if the name differs
- `matching`: push all branches that exist on both sides (old default, risky)
- `nothing`: always require a branch name

## 272: What does push.autoSetupRemote do?

With it set to `true` (Git 2.37+), `git push` on a new branch with no upstream automatically pushes to a branch of the same name on the remote and sets it as upstream.

```bash
git config --global push.autoSetupRemote true
```

No more "the current branch has no upstream branch" error and no need to type `-u origin branch-name`.

## 273: Why was my push rejected with "non-fast-forward"?

The remote branch has commits that your local branch doesn't have. Pushing would remove them, so Git refuses.

Fix it by integrating the remote changes first:

```bash
git pull --rebase    # or git pull
git push
```

If you rewrote history on purpose and you're sure, use `git push --force-with-lease`.

## 274: How do you rename the default branch from master to main?

```bash
git branch -m master main
git push -u origin main
```

Then on GitHub or GitLab, change the default branch to `main` in the repo settings, update branch protection rules, CI configs and any scripts, and delete the old branch with `git push origin --delete master`. GitHub redirects links and shows teammates the commands to update their clones.

Each teammate runs:

```bash
git branch -m master main
git fetch origin
git branch -u origin/main main
git remote set-head origin -a
```

## 275: What does git remote set-head do?

It sets `origin/HEAD`, which is the remote's default branch as your local repo knows it. Commands use it when you refer to just `origin`.

```bash
git remote set-head origin -a     # ask the remote what its default is
git remote set-head origin main
```

You mostly need it after the default branch on the server was renamed.

## 276: What does git ls-remote do?

It lists refs on a remote without fetching anything.

```bash
git ls-remote origin
git ls-remote --heads origin
git ls-remote --tags origin "v1.*"
```

It's handy in scripts, for example to check that a branch exists or to get the latest commit hash of a branch.

## 277: How do you get the current commit hash in a script?

```bash
git rev-parse HEAD
git rev-parse --short HEAD
git rev-parse --abbrev-ref HEAD     # current branch name
git rev-parse --show-toplevel       # repo root folder
```

`git rev-parse` turns any ref or expression into a hash and answers lots of "where am I" questions, so scripts use it a lot.

## 278: What is the difference between plumbing and porcelain commands?

Porcelain commands are the user-facing ones, like `commit`, `log` and `status`. Their output can change between versions.

Plumbing commands are low-level ones, like `cat-file`, `hash-object`, `update-ref`, `rev-parse` and `ls-tree`. They have stable output and are meant for scripts. Some porcelain commands also have stable modes, like `git status --porcelain`.

## 279: Why should scripts use git status --porcelain?

The normal `git status` output is for humans. It can change between Git versions and depends on the language setting. `--porcelain` gives a stable, simple format that's easy to parse.

```bash
if [ -n "$(git status --porcelain)" ]; then
  echo "Working directory is not clean"
  exit 1
fi
```

`--porcelain=v2` gives more detail, including branch info.

## 280: How do you use Git in CI with a shallow clone?

Most CI systems clone with a small `--depth` to save time. That breaks commands that need history, like `git describe`, `git log main..HEAD` or tools that compare with `main`.

Fixes:

```yaml
# GitHub Actions
- uses: actions/checkout@v6
  with:
    fetch-depth: 0 # full history
```

Or fetch only what you need:

```bash
git fetch --depth=50 origin main
git fetch --tags
```

## 281: How do you get the list of changed files in a pull request in CI?

```bash
git fetch origin main
git diff --name-only origin/main...HEAD
```

The three dots compare against the merge base, so you only get what the PR changed. In a shallow clone, the merge base may be missing, so fetch enough history first (or use `fetch-depth: 0`).

## 282: What is sparse checkout?

Sparse checkout lets you have only some folders of a repo in your working directory. The rest is still in Git but not written to disk.

```bash
git sparse-checkout set apps/web packages/ui
git sparse-checkout add packages/utils
git sparse-checkout list
git sparse-checkout disable
```

In big monorepos, it makes `git status` and file system tools much faster because there are fewer files.

## 283: What is cone mode in sparse checkout?

Cone mode is the default mode. You can only choose whole folders, not arbitrary file patterns. Because of that, Git can match paths quickly, which matters in huge repos.

Files in the root folder are always included. The older non-cone mode uses `.gitignore`-style patterns and is slower.

## 284: What is a partial clone?

A partial clone skips downloading some objects up front and fetches them when needed.

```bash
git clone --filter=blob:none https://github.com/org/big-repo.git
git clone --filter=tree:0 https://github.com/org/big-repo.git
```

- `blob:none`: download all commits and trees, but file contents only when you check them out. Good for development.
- `tree:0`: download only commits. Trees and files come later. Good for one-off builds.

The server must support it. GitHub and GitLab do.

## 285: What is the difference between a shallow clone and a partial clone?

A shallow clone cuts off history: you only get the last N commits. Commands that need older history don't work until you fetch more.

A partial clone keeps the full commit history but skips file contents (or trees) until they're needed. `log` works fully, and old file versions are downloaded on demand. For developer machines, partial clones are usually the better choice. Shallow clones are fine for throwaway CI jobs.

## 286: How do you combine sparse checkout and partial clone?

```bash
git clone --filter=blob:none --sparse https://github.com/org/monorepo.git
cd monorepo
git sparse-checkout set apps/web packages/ui
```

With `--sparse`, only root files are checked out at first. Combined with the blob filter, Git only downloads file contents for the folders you selected.

## 287: How do you fetch only one branch?

```bash
git fetch origin main
git fetch origin feature:feature     # fetch and update a local branch
```

To always fetch only one branch, change the refspec:

```bash
git config remote.origin.fetch "+refs/heads/main:refs/remotes/origin/main"
```

## 288: What is a refspec?

A refspec tells Git which refs to fetch or push and where to put them. The format is `[+]<source>:<destination>`.

```ini
[remote "origin"]
    fetch = +refs/heads/*:refs/remotes/origin/*
```

This means "take every branch on the remote and save it as `origin/<name>` locally". The `+` allows non-fast-forward updates. `git push origin HEAD:refs/heads/release` also uses a refspec.

## 289: How do you push a local branch to a remote branch with a different name?

```bash
git push origin local-name:remote-name
git push origin HEAD:staging      # push current branch to "staging"
```

## 290: How do you see what will be pushed before pushing?

```bash
git log @{u}..HEAD --oneline
git diff @{u}..HEAD
git push --dry-run
```

## 291: What is git notes?

`git notes` attaches extra text to a commit without changing the commit or its hash.

```bash
git notes add -m "Deployed to production on 2026-03-01" a1b2c3d
git log --show-notes
git push origin refs/notes/*
```

Notes are stored in `refs/notes/commits` and are not pushed or fetched by default. They're used for things like build or review info added after the fact.

## 292: What is git range-diff?

`git range-diff` compares two versions of a series of commits, like your branch before and after a rebase. It shows which commits changed and how.

```bash
git range-diff main feature@{1} feature
git range-diff main..old-branch main..new-branch
```

It's very useful when you update a pull request with a force push and want to show reviewers what changed between versions.

## 293: How do you list commits on a branch that aren't in another branch, even after cherry-picks?

```bash
git cherry -v main feature
git log --cherry-pick --left-right --oneline main...feature
```

`git cherry` compares patches, not hashes. Commits marked `-` have an equal change already in `main` (for example they were cherry-picked). Commits marked `+` are not in `main` yet.

## 294: How do you get Git to remember your choice for every conflict on a branch with many rebases?

Turn on rerere:

```bash
git config --global rerere.enabled true
git config --global rerere.autoUpdate true
```

The first time you resolve a conflict, Git records it in `.git/rr-cache`. Next time the same conflict happens, it applies your resolution. With `autoUpdate`, it also stages the resolved file. Always check the result before continuing, because a reused resolution can be wrong in a new context.

## 295: What is git switch --orphan?

It creates a new branch with no history. The first commit on it will have no parent.

```bash
git switch --orphan gh-pages
# the working directory is empty now
echo "<h1>Docs</h1>" > index.html
git add index.html
git commit -m "Start docs site"
```

It's used for things like a `gh-pages` branch that has nothing to do with the main code.

## 296: How do you merge two unrelated repositories and keep both histories?

```bash
cd repo-a
git remote add repo-b ../repo-b
git fetch repo-b
git merge repo-b/main --allow-unrelated-histories
```

Without `--allow-unrelated-histories`, Git refuses because the two histories have no common commit. To keep the code apart, first move repo-b's files into a subfolder (for example with `git filter-repo --to-subdirectory-filter repo-b` in a copy of repo-b).

## 297: How do you split a folder out into its own repository with its history?

Work on a fresh clone:

```bash
git clone https://github.com/org/monorepo.git ui-lib
cd ui-lib
git filter-repo --subdirectory-filter packages/ui
git remote add origin git@github.com:org/ui-lib.git
git push -u origin main
```

Only commits that touched `packages/ui` are kept, and the folder becomes the new repo root.

## 298: How do you run a command on every commit in a range?

```bash
git rebase --exec "npm test" main
```

Or without rewriting anything:

```bash
for c in $(git rev-list --reverse main..HEAD); do
  git switch --detach "$c" && npm test || echo "Failed at $c"
done
git switch -
```

## 299: What is git maintenance?

`git maintenance` runs background jobs that keep a repo fast, like prefetching from remotes, writing the commit-graph, packing loose objects and repacking.

```bash
git maintenance start      # register the repo and schedule the tasks
git maintenance run --task=gc
git maintenance stop
```

`start` sets up a scheduler (launchd, systemd, cron or Task Scheduler) so it runs regularly. It's helpful for big repos.

## 300: What is git gc?

`git gc` (garbage collection) cleans up the repository: it packs loose objects into packfiles, removes unreachable objects that are old enough and packs refs.

```bash
git gc
git gc --prune=now      # remove unreachable objects right away
```

Git runs `git gc --auto` by itself after some commands, when there are too many loose objects or packs. You rarely need to run it by hand.

# Advanced Questions (301-450)

## 301: How does Git store data internally?

Git is a content-addressable store. Every piece of data is saved as an object, and the object's name is the hash of its content. If you know the hash, you can get the content, and the same content always gets the same hash.

There are four object types:

- **blob**: the content of a file (no name, no permissions)
- **tree**: a folder listing, with names, modes and hashes of blobs and other trees
- **commit**: points to one tree, its parent commits, plus author, committer and message
- **tag**: an annotated tag, pointing to another object with a name, tagger and message

Branches and tags are just files (refs) that hold a hash.

## 302: Does Git store diffs or snapshots?

Conceptually, snapshots. Each commit points to a full tree of the project. Files that didn't change point to the same blob as before, so nothing is duplicated.

Physically, when objects are packed into packfiles, Git stores many of them as deltas against similar objects to save space. But those deltas are a storage detail and don't follow commit order. Commands like `diff` compute differences on the fly by comparing snapshots.

## 303: How is a blob's hash calculated?

Git hashes a header plus the content: the word `blob`, a space, the size in bytes, a null byte and then the file content.

```bash
echo -n "hello" | git hash-object --stdin
printf "blob 5\0hello" | shasum
# both print b6fc4c620b67d95f953a5c1c1230aaab5db5a1b0
```

Since the file name isn't part of the hash, two files with the same content anywhere in the repo share one blob.

## 304: How do you inspect Git objects directly?

```bash
git cat-file -t a1b2c3d      # type: blob, tree, commit or tag
git cat-file -s a1b2c3d      # size
git cat-file -p a1b2c3d      # pretty-print the content
git cat-file -p HEAD^{tree}  # the root tree of the last commit
git ls-tree -r HEAD          # all files in the last commit with their blob hashes
```

## 305: What does a commit object look like inside?

```bash
git cat-file -p HEAD
```

```text
tree 9c4d8f1e...
parent 3f2a1c9e...
author Jane Doe <jane@example.com> 1767000000 +0100
committer Jane Doe <jane@example.com> 1767000000 +0100

Fix crash when user has no avatar
```

A merge commit has two or more `parent` lines. The first commit in a repo has none. A signed commit also has a `gpgsig` header. Because the parent hash is part of the content, changing any old commit changes every hash after it.

## 306: What does a tree object contain?

A tree lists entries, each with a mode, type, hash and name:

```text
100644 blob a1b2c3d...    README.md
100755 blob b2c3d4e...    build.sh
040000 tree c3d4e5f...    src
120000 blob d4e5f6a...    link-to-config
160000 commit e5f6a7b...  libs/shared
```

Modes Git uses: `100644` normal file, `100755` executable, `120000` symlink, `040000` folder, `160000` gitlink (a submodule commit). Git doesn't store other permissions, owners or timestamps.

## 307: How could you create a commit using only plumbing commands?

```bash
echo "hello" > a.txt
blob=$(git hash-object -w a.txt)
git update-index --add --cacheinfo 100644,"$blob",a.txt
tree=$(git write-tree)
commit=$(echo "First commit" | git commit-tree "$tree")
git update-ref refs/heads/main "$commit"
```

This is roughly what `git add` and `git commit` do: write blobs, build a tree from the index, create a commit object pointing to the tree and parent, then move the branch ref.

## 308: What are loose objects and packfiles?

A loose object is a single zlib-compressed file in `.git/objects/ab/cdef...`, where the first two hex characters of the hash are the folder name. New objects start as loose objects.

A packfile (`.git/objects/pack/*.pack`) holds many objects in one file, often stored as deltas against similar objects, with an `.idx` file for fast lookup by hash. `git gc` and `git repack` move loose objects into packs. Fetches and pushes also send data as packs.

## 309: How does delta compression in packfiles work?

When packing, Git sorts objects by type, name and size and tries to express each one as a delta against a similar object nearby (a "window" of candidates). The delta says "copy these bytes from the base, then insert these new bytes".

Git usually keeps the newest version whole and stores older versions as deltas, because recent versions are read more often. Deltas can form chains, limited by `pack.depth`. `pack.window` controls how many candidates are tried. Bigger values give smaller packs but take longer.

## 310: What is the Git index file?

`.git/index` is a binary file that lists every tracked path with its mode, blob hash, stage number and cached file system info like size and modification time.

```bash
git ls-files --stage
```

It serves two purposes: it's the staging area for the next commit, and it's a cache that lets `git status` skip reading files whose size and timestamps didn't change. During a conflict, a path has entries at stages 1 (base), 2 (ours) and 3 (theirs).

## 311: How does git status decide which files changed?

For tracked files, Git compares each file's stat info (size, modification time, inode and so on) with what's cached in the index. Only files whose stat info changed are read and hashed to see if the content really changed. Then it compares the index with the `HEAD` tree to find staged changes.

For untracked files, it walks the working directory and applies ignore rules. In huge repos, both parts get slow, which is why there are features like fsmonitor and the untracked cache.

## 312: What is the "racy git" problem?

File systems store timestamps with limited precision. If a file is changed in the same second (or tick) that the index was written, its stat info could look unchanged even though the content changed.

Git handles this by treating entries whose modification time is equal to or newer than the index file's time as "racily clean" and checking their content. That's why `git status` sometimes reads files even when nothing seems to have changed.

## 313: How are branches and tags stored?

By default, as files under `.git/refs/`: `refs/heads/main` holds the commit hash for `main`, `refs/tags/v1.0.0` for the tag. To save space, many refs are combined into one `.git/packed-refs` file, which `git gc` or `git pack-refs` writes.

When Git reads a ref, it checks the loose file first and then `packed-refs`. Newer repos can use the reftable format instead.

## 314: What is reftable?

Reftable is a newer storage format for refs (Git 2.45+). Instead of one file per ref plus `packed-refs`, all refs and reflogs are stored in a stack of binary tables.

```bash
git init --ref-format=reftable
git refs migrate --ref-format=reftable
```

It handles repos with millions of refs much better, updates many refs atomically, and avoids problems with case-insensitive file systems (like `Feature` and `feature` branches clashing on macOS). Git 3.0 is planned to make it the default.

## 315: What is a symbolic ref?

A symbolic ref points to another ref instead of a hash. `HEAD` is the main example: it usually contains `ref: refs/heads/main`.

```bash
git symbolic-ref HEAD
git symbolic-ref HEAD refs/heads/develop    # what switching branches does at the ref level
```

`refs/remotes/origin/HEAD` is another symbolic ref, pointing to the remote's default branch.

## 316: What happens step by step when you run git commit?

1. Hooks run: `pre-commit`, then `prepare-commit-msg` and `commit-msg` with the message.
2. Git writes tree objects from the index (blobs were already written by `git add`).
3. It creates a commit object with the root tree, `HEAD` as parent, author, committer and message.
4. It updates the current branch ref to the new commit, using a lock file so the update is atomic.
5. It writes a reflog entry for the branch and `HEAD`.
6. The `post-commit` hook runs.

## 317: What happens step by step when you run git fetch?

1. Git connects to the remote over HTTPS or SSH and, with protocol v2, asks for the refs that match the refspec.
2. It compares those refs with what it already has.
3. Negotiation: the client tells the server which commits it wants and which it already has (`want` and `have` lines), so the server can work out the minimum set of objects to send.
4. The server sends a packfile, often a thin pack with deltas against objects the client already has.
5. The client indexes the pack, checks connectivity and updates the remote-tracking refs and `FETCH_HEAD`.

## 318: What is Git protocol version 2?

Protocol v2 is the current wire protocol, default since Git 2.26. The main improvement is that the client can ask only for the refs it cares about, instead of the server sending a list of all refs first.

For repos with many branches, tags or pull request refs, that saves a lot of time and bandwidth. It also made it easier to add features like partial clone filters and bundle URIs.

## 319: What is a thin pack?

A thin pack is a packfile with deltas against objects that aren't in the pack, because the receiver already has them. It saves bandwidth during fetch and push.

The receiver "fixes" the thin pack by adding the missing base objects (from its own store) so the pack on disk is complete.

## 320: What is the commit-graph file?

The commit-graph (`.git/objects/info/commit-graph`) is a binary file that stores commit parents, root trees and generation numbers for fast lookup, so Git doesn't have to parse commit objects for history walks.

```bash
git commit-graph write --reachable --changed-paths
```

It makes `git log --graph`, `merge-base`, `branch --contains` and ahead/behind counts much faster in big repos. `git gc` and `git maintenance` keep it updated.

## 321: What are generation numbers?

A generation number tells how "deep" a commit is in history. It's always bigger than the generation number of its parents. Newer Git versions use corrected commit dates as generation numbers.

When Git asks "is commit A an ancestor of B?", it can stop walking as soon as it reaches commits with a lower generation number than A. That cuts down a lot of work in commands like `merge-base` and `--contains`.

## 322: What are changed-path Bloom filters?

When you write the commit-graph with `--changed-paths`, Git stores a small Bloom filter per commit that records which paths changed.

When you run `git log -- some/path`, Git checks the filter first. If it says the path definitely didn't change in that commit, Git skips diffing the trees. Bloom filters can give false positives but never false negatives, so results stay correct. This makes path-limited log and blame much faster in large repos.

## 323: What is a multi-pack-index?

A multi-pack-index (MIDX) is one index file that covers many packfiles. Without it, Git has to check each pack's `.idx` file one by one when looking for an object.

It lets big repos keep many packs without paying for lookups in each one, and avoids repacking everything into one huge pack. `git maintenance` uses it with the `incremental-repack` task.

## 324: What are reachability bitmaps?

A bitmap stores, for selected commits, a bit set of all objects reachable from that commit. With it, Git can answer "which objects do I need to send?" with fast bit operations instead of walking the whole history.

Servers use bitmaps heavily to make clones and fetches fast. You create them with `git repack -a -d --write-bitmap-index`, and they also work with multi-pack-indexes.

## 325: What does git gc do in detail?

By default it:

- Packs refs into `packed-refs`
- Expires old reflog entries (90 days for reachable, 30 days for unreachable by default)
- Repacks objects into packfiles
- Prunes loose unreachable objects older than two weeks (`gc.pruneExpire`)
- Writes or updates the commit-graph
- Cleans up stale worktrees and rerere data

`git gc --auto` only does work when there are more than about 6,700 loose objects (`gc.auto`) or more than 50 packs (`gc.autoPackLimit`).

## 326: What is the difference between unreachable and dangling objects?

An unreachable object can't be reached from any ref (branch, tag, reflog, stash, index).

A dangling object is an unreachable object that also isn't referenced by any other unreachable object. It's the "top" of an unreachable chain, like the last commit of a deleted branch.

```bash
git fsck --unreachable
git fsck --dangling
git fsck --lost-found       # write dangling commits and blobs to .git/lost-found
```

## 327: Why doesn't git gc delete unreachable objects right away?

Two reasons:

1. The reflog still references many of them, and that's your safety net for undoing mistakes.
2. Another Git process could be in the middle of writing objects and refs. If gc deleted new objects that aren't referenced yet, it could corrupt the repo. The two week grace period protects against that race.

`git gc --prune=now` is only safe when nothing else is using the repo.

## 328: How do you recover a commit after reset --hard and after the reflog was cleared?

If the reflog is still there, use it. If not, the commit object may still exist as a dangling object until gc prunes it:

```bash
git fsck --lost-found
git show <hash>
git branch recovered <hash>
```

Uncommitted changes that were staged at some point can also be found this way as dangling blobs, but you'll get file contents without names. Changes that were never staged are gone.

## 329: How does git stash store data internally?

A stash is a set of commits:

- A commit for the working directory state, with `HEAD` as first parent and the index commit as second parent
- A commit for the index state
- With `-u`, a third parent commit with the untracked files

`refs/stash` points to the latest stash, and older stashes are stored in the reflog of `refs/stash`. That's why they show up as `stash@{n}`. Git 2.51 added `git stash export` and `git stash import` to turn stashes into a normal chain of commits that can be pushed and fetched.

## 330: How does rebase work internally?

Git:

1. Finds the commits to replay: those in `upstream..branch`, skipping merges and commits whose patch is already in upstream.
2. Detaches `HEAD` at the new base.
3. Cherry-picks each commit in order, using the sequencer. State is kept in `.git/rebase-merge/` so you can stop and continue.
4. When done, moves the branch ref to the last new commit and reattaches `HEAD`.

`ORIG_HEAD` and the reflog point to the old branch tip in case you want to undo it.

## 331: How does cherry-pick work internally?

Cherry-pick is a three-way merge. For commit `C` with parent `P`, Git merges using `P` as the base, the current `HEAD` as "ours" and `C` as "theirs". The result is committed with `C`'s message and author.

That's why cherry-pick can hit conflicts even if the change looks simple: the code around it in `HEAD` may differ from `P`. Revert works the same way, just with `C` as the base and `P` as "theirs".

## 332: What is the ort merge strategy and why did it replace recursive?

`ort` ("Ostensibly Recursive's Twin") is a rewrite of the `recursive` strategy. It became the default in Git 2.34, and in Git 2.50 the old `recursive` code was removed, so asking for `recursive` uses `ort`.

It gives the same kind of results but is much faster, especially with many renames, because it works mostly in memory and doesn't touch the working tree or index until the end. It also fixed many corner cases with renames and directory renames.

## 333: What is a criss-cross merge?

A criss-cross merge happens when two branches have merged each other, so there are two or more equally good merge bases.

For example, `main` has commit `C` and `feature` has commit `D`. Then someone merges `D` into `main`, and someone else merges `C` into `feature`. Now if you merge `feature` into `main`, both `C` and `D` are common ancestors and neither is "better" than the other.

```bash
git merge-base --all main feature    # prints more than one commit
```

The `ort` and `recursive` strategies handle it by first merging the merge bases into a virtual base commit, then using that as the base for the real merge. That's where the name "recursive" came from.

## 334: What is an evil merge?

An evil merge is a merge commit that contains changes that weren't in either parent, beyond resolving conflicts. For example, someone fixed a bug while resolving a merge.

They're hard to spot, because `git log -p` doesn't show merge diffs by default and `git show` only shows a combined diff. Use `git show --remerge-diff <merge>` (Git 2.36+) to see what the merge did compared to an automatic merge.

## 335: What is --remerge-diff?

`--remerge-diff` re-does the merge automatically in memory, conflict markers and all, and then diffs that result against the actual merge commit. You see exactly how conflicts were resolved and any extra changes.

```bash
git show --remerge-diff a1b2c3d
git log --remerge-diff -p --merges
```

It's very useful for reviewing merges and finding evil merges.

## 336: What is git merge-tree --write-tree?

It performs a merge without touching the working directory or index and prints the resulting tree hash, plus conflict info if any (Git 2.38+).

```bash
git merge-tree --write-tree main feature
```

Servers use it to check if a pull request merges cleanly, and scripts can use it to merge in bare repos. You can then make a commit from the tree with `git commit-tree`.

## 337: What is git replay?

`git replay` (added in Git 2.44 as experimental) replays commits on a new base without a working tree, like a server-side rebase or cherry-pick. It prints the ref updates instead of applying them.

```bash
git replay --onto main topic1..topic2 | git update-ref --stdin
```

It's built for servers and tools that need fast rebases on bare repos. The command is still marked experimental, so its options may change.

## 338: How does Git detect directory renames during a merge?

If one side moves all files from `lib/` to `src/lib/`, and the other side adds a new file in `lib/`, Git guesses that the new file should go into `src/lib/` too.

The ort strategy does this by default (`merge.directoryRenames`). It's helpful but can surprise you, so check the result when Git reports it moved a file because of a directory rename.

## 339: What is merge.renameLimit and why does it matter?

Rename detection compares every deleted file with every added file, which gets expensive. `merge.renameLimit` and `diff.renameLimit` cap how many files Git will consider.

If you hit the limit, Git prints a warning and skips rename detection, which can cause bad conflicts in big refactors. You can raise it:

```bash
git config merge.renameLimit 20000
```

The `ort` strategy made this much less of an issue thanks to big speedups in rename detection.

## 340: How are submodules stored in the parent repo?

The parent repo's tree has an entry with mode `160000` (a gitlink) that holds the commit hash of the submodule. The parent doesn't store the submodule's files or history.

`.gitmodules` maps the path to the URL. The submodule's own Git data lives in `.git/modules/<name>` in the parent, and the submodule folder has a `.git` file pointing there.

## 341: How are worktrees stored internally?

Each extra worktree has a folder in `.git/worktrees/<name>/` with its own `HEAD`, index and some state files. The worktree folder itself contains a `.git` file (not a folder) with a `gitdir:` line pointing back there.

Objects and most refs are shared. Per-worktree refs like `HEAD` and refs under `refs/bisect` are kept separate. If you delete a worktree folder by hand, run `git worktree prune` to clean up.

## 342: What is the difference between GIT_DIR and GIT_WORK_TREE?

`GIT_DIR` (or `--git-dir`) tells Git where the repository data is. `GIT_WORK_TREE` (or `--work-tree`) tells Git where the files are.

```bash
git --git-dir=$HOME/.dotfiles --work-tree=$HOME status
```

This is the trick behind managing dotfiles with a bare repo: the repo data sits in one place while the files are your home folder.

## 343: Why was SHA-1 a problem for Git, and what did Git do about it?

SHA-1 has been considered weak for years, and in 2017 the SHAttered attack produced two different PDFs with the same SHA-1 hash. In theory, an attacker could make two objects with the same hash.

Git did two things:

1. It switched to SHA-1DC, a version of SHA-1 that detects the known collision attack and refuses such objects.
2. It added support for SHA-256 repositories with `git init --object-format=sha256`. Git 3.0 is planned to make SHA-256 the default for new repos.

## 344: What blocks a full move to SHA-256?

SHA-1 and SHA-256 repos can't easily talk to each other yet. A SHA-256 repo can't push to or fetch from a SHA-1 one, and the planned interoperability layer (mapping between the two hash types) isn't finished.

Hosting services, CI systems, IDEs and tools also need to support it. For example, GitHub doesn't support SHA-256 repos yet. Until that changes, most teams stay on SHA-1, which is still safe enough in practice thanks to SHA-1DC.

## 345: Why are Git branches so cheap compared to other systems?

A branch is a ref: a tiny file (or a reftable entry) holding a 40 character hash. Creating one writes a few bytes. Switching branches only updates files that differ between the two trees.

In systems like SVN, a branch is a copy of a directory on the server. Git's model means you can create branches for every small task without thinking about cost.

## 346: Why are commits immutable and what does that mean in practice?

A commit's hash depends on its content, including the parent hash. If you change anything (message, file, author, parent), you get a different hash, so it's a new commit.

In practice, "editing" history (amend, rebase, filter-repo) always creates new commits and moves refs to them. The old ones stay until gc. It also means a commit hash proves the whole history behind it, which is what makes signed tags and commits meaningful.

## 347: What is the .git/index.lock file and why does it get stuck?

Git creates `index.lock` while it updates the index, then renames it to `index` when done. That rename is atomic, so readers never see a half-written index. If another Git process sees the lock file, it refuses to work: "Unable to create index.lock: File exists".

It gets left behind when a Git process crashes or is killed. If you're sure no Git process (including your IDE) is running, delete it:

```bash
rm .git/index.lock
```

Refs use the same approach with `<ref>.lock` files.

## 348: How do you find the largest files in a repo's history?

```bash
git rev-list --objects --all |
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' |
  awk '$1 == "blob"' | sort -k3 -n -r | head -20
```

This lists all blobs from all commits with their size and path. You can also use `git count-objects -vH` for totals and `git filter-repo --analyze` for a full report.

## 349: How do you reduce the size of a bloated repository?

1. Find what's big (see the previous question). Often it's old binaries, build output or `node_modules` committed by mistake.
2. Remove them from history with `git filter-repo --path big-folder --invert-paths` or `--strip-blobs-bigger-than 10M`, or move them to LFS with `git lfs migrate`.
3. Clean up locally: `git reflog expire --expire=now --all && git gc --prune=now --aggressive`.
4. Force push all branches and tags and ask everyone to re-clone.

The hosting service may keep old objects for a while (pull request refs, forks), so the server size can take time to drop.

## 350: What does git gc --aggressive do and should you use it?

`--aggressive` repacks everything from scratch with a much bigger delta window and depth, trying harder to find good deltas. It can make the pack smaller but takes a lot of time and memory.

It's worth running occasionally, for example after a big history rewrite or an import from another VCS. For daily use, normal `gc` or `git maintenance` is enough.

## 351: How do you make git status fast in a huge repository?

```bash
git config core.fsmonitor true          # built-in file system monitor (macOS, Windows)
git config core.untrackedCache true     # cache untracked file scans
git config feature.manyFiles true       # turns on index v4 and the untracked cache
git config index.skipHash true          # skip hashing the index on write
```

Also use sparse checkout so fewer files are on disk, and keep build output and dependencies ignored. `scalar` can set most of these options for you.

## 352: What is the built-in fsmonitor?

The file system monitor is a daemon that watches the working directory for changes using the OS (FSEvents on macOS, ReadDirectoryChangesW on Windows). When you run `git status`, Git asks the daemon what changed since last time instead of checking every file.

```bash
git config core.fsmonitor true
git fsmonitor--daemon status
```

On repos with hundreds of thousands of files, it turns `git status` from seconds into a fraction of a second. On Linux, the built-in daemon isn't available, but you can hook in Watchman instead.

## 353: What is Scalar?

Scalar is a tool that ships with Git (since 2.38) and configures a repo for large scale use. It turns on partial clone, sparse checkout in cone mode, fsmonitor, the commit-graph, multi-pack-index and background maintenance.

```bash
scalar clone https://github.com/org/huge-monorepo.git
scalar register       # apply the settings to an existing repo
```

It came from Microsoft's work on the Windows and Office repos.

## 354: How do you debug a slow Git command?

Use the trace env variables:

```bash
GIT_TRACE=1 git pull                    # commands and child processes
GIT_TRACE2_PERF=1 git status            # timing for each stage
GIT_TRACE_PACKET=1 git fetch            # protocol messages
GIT_CURL_VERBOSE=1 git fetch            # HTTPS details
GIT_SSH_COMMAND="ssh -v" git fetch      # SSH details
```

`GIT_TRACE2_PERF` is usually the most useful: it shows which phase takes the time (index reading, untracked scan, rename detection and so on).

## 355: How would you set up Git for a monorepo with thousands of developers?

Some common pieces:

- Partial clone (`--filter=blob:none`) and sparse checkout in cone mode, so each developer only gets what they work on
- fsmonitor, untracked cache, commit-graph and `git maintenance`, or just `scalar`
- Short-lived branches and trunk-based development, with a merge queue so `main` stays green
- CODEOWNERS for review routing
- Build tools that only build and test what changed (Bazel, Nx, Turborepo)
- Server-side bitmaps, multi-pack-index and caching proxies or bundle URIs for faster clones in CI

## 356: How do you speed up cloning in CI?

- Shallow clone (`--depth 1`) if the job doesn't need history
- Partial clone (`--filter=blob:none` or `tree:0`) if it needs history but not old file contents
- `--single-branch` to skip other branches
- Sparse checkout if only part of the repo is needed
- Cache the `.git` folder between runs and fetch only what's new
- Use `git clone --reference` against a local mirror on the runner

Measure first. In many pipelines, the clone is not the slow part.

## 357: What does git clone --reference do?

It makes the new clone borrow objects from an existing local repository instead of downloading them again. Git records the other repo in `.git/objects/info/alternates`.

```bash
git clone --reference /cache/repo.git https://github.com/org/repo.git
git clone --reference /cache/repo.git --dissociate https://github.com/org/repo.git
```

Without `--dissociate`, the clone breaks if the reference repo is deleted or pruned. With it, Git copies the needed objects at the end so the clone is independent.

## 358: What is a mirror clone and when do you use it?

```bash
git clone --mirror https://old-server.com/org/app.git
cd app.git
git push --mirror https://new-server.com/org/app.git
```

`--mirror` makes a bare clone with all refs (branches, tags, notes and anything else) and maps them one to one. It's the standard way to move a repo to a new hosting service or to keep a full backup. `git push --mirror` also deletes refs on the target that don't exist in the source, so be careful which way you push.

## 359: What are server-side hooks?

Hooks that run on the server when someone pushes:

- `pre-receive`: runs once per push, gets all ref updates on stdin. Exit non-zero to reject the whole push.
- `update`: runs once per ref being updated. Can reject one branch but allow others.
- `post-receive`: runs after the push is accepted. Used for deploys, notifications and CI triggers.

Unlike client hooks, they can't be skipped, so they're the right place to enforce rules. On GitHub you can't run custom server hooks, so you use branch rules, required checks and webhooks instead. GitHub Enterprise Server and self-hosted GitLab do support them.

## 360: How would you write a pre-receive hook that blocks force pushes to main?

```bash
#!/bin/sh
zero=0000000000000000000000000000000000000000

while read old new ref; do
  if [ "$ref" = "refs/heads/main" ] && [ "$old" != "$zero" ] && [ "$new" != "$zero" ]; then
    if ! git merge-base --is-ancestor "$old" "$new"; then
      echo "Force pushes to main are not allowed"
      exit 1
    fi
  fi
done
exit 0
```

If the old tip isn't an ancestor of the new tip, history was rewritten. On a plain Git server, you can also just set `receive.denyNonFastForwards true`. In a SHA-256 repo the zero hash is 64 characters long.

## 361: What is the safe.directory setting and why was it added?

Since Git 2.35.2, Git refuses to work in a repo owned by another user unless you mark it safe:

```bash
git config --global --add safe.directory /path/to/repo
```

It was added to fix a security problem (CVE-2022-24765). On shared machines, another user could create a `.git` folder in a parent directory like `C:\` or `/tmp`, with a config that runs commands (for example through `core.fsmonitor`). Any Git command you ran under it, even from your shell prompt, would run their code. You often see this error in Docker containers and CI when the repo was checked out by a different user.

## 362: What are the security risks of cloning an untrusted repository?

Cloning is mostly safe: hooks and `.git/config` are not cloned, so a repo can't run code just by being cloned. But risks remain:

- Bugs in Git itself. Several past CVEs used submodules, symlinks or case-insensitive file systems to write files into `.git` and run code during clone. Keep Git updated.
- Running build scripts, `npm install`, Makefiles or IDE tasks from the repo runs their code.
- Git LFS, filters and tools in your global config may process repo content.

Treat an untrusted repo like untrusted code: inspect before running anything in it.

## 363: Why is protocol.file.allow restricted by default?

Since Git 2.38.1, the `file://` transport (cloning from a local path) is only allowed when you ask for it directly, not when it's triggered by something like a submodule URL.

It fixed CVE-2022-39253, where a malicious repo could use a local-path submodule to make Git copy files or symlinks from your machine into the clone. If you really need local submodules in tests, you can allow it with `git -c protocol.file.allow=always submodule update`.

## 364: Why should you not expose the .git folder on a web server?

If you deploy by copying the repo folder (or cloning into the web root) and the server serves `.git/`, anyone can download your whole repository: source code, history, old config files and any secrets that were ever committed.

Tools exist that rebuild a full repo from an exposed `.git` folder. Block `.git` in the web server config, or better, deploy build output only, not a working copy.

## 365: How can someone fake commits as another person, and how do you prevent it?

Author name and email are just text set by the person committing:

```bash
git -c user.name="Project Lead" -c user.email="lead@example.com" commit -m "Looks real"
```

GitHub links commits to accounts by email, so a fake commit can show someone's avatar. To prevent this:

- Sign commits (GPG or SSH) and require signatures on protected branches.
- Turn on GitHub's "vigilant mode" so unsigned commits under your name are marked as unverified.
- Review who actually pushed (push logs and audit logs), not only the author field.

## 366: What is transfer.fsckObjects?

When it's on, Git checks every object it receives during fetch, clone or push for corruption and malformed content (bad tree entries, invalid names like `.git` inside trees and so on).

```bash
git config --global transfer.fsckObjects true
```

Servers like GitHub run these checks on push. Turning it on on your client adds extra protection when fetching from servers you don't fully trust, at a small speed cost.

## 367: How do credentials leak through Git, and how do you avoid it?

Common ways:

- Tokens in remote URLs (`https://user:token@github.com/...`) end up in `.git/config`, shell history and CI logs.
- The `store` credential helper saves tokens in plain text in `~/.git-credentials`.
- CI jobs that print `git remote -v` or full error output.
- Docker images that copy `.git` with a token in its config.

Use a credential helper backed by the OS keychain or Git Credential Manager, short-lived tokens (for example GitHub App or OIDC tokens in CI), `.dockerignore` for `.git`, and SSH keys with a passphrase.

## 368: What is the trust model of signed tags in a release process?

A signed tag proves that the holder of a specific key tagged a specific commit. Because the commit hash covers the full tree and all history before it, verifying the tag verifies the entire source code of the release.

For it to mean something, you need a known list of trusted keys (maintainer keys or an allowed signers file), and the verifying side must actually run `git verify-tag` in the build or release pipeline. Many projects now also use Sigstore (gitsign) for keyless signing tied to an identity.

## 369: What are clean and smudge filters?

Filters run when files go into and out of Git:

- **clean**: runs on `git add`, turning the working file into what's stored in the repo
- **smudge**: runs on checkout, turning the stored content into the working file

```gitattributes
*.secret filter=crypt
```

```bash
git config filter.crypt.clean "gpg --encrypt -r me@example.com"
git config filter.crypt.smudge "gpg --decrypt"
```

Git LFS and tools like git-crypt are built on filters. Filters are configured locally, so every developer needs the same setup.

## 370: How does Git LFS work internally?

LFS uses a clean filter. When you `git add` a tracked file, the filter saves the real content in `.git/lfs/objects` and gives Git a small pointer file instead:

```text
version https://git-lfs.github.com/spec/v1
oid sha256:4d7a214614ab2935c943f9e0ff69d22eadbb8f32b1258daaa5e2ca24d17e2393
size 12345
```

A `pre-push` hook uploads the real files to the LFS server. On checkout, the smudge filter downloads the content for the pointer and writes the real file. Git itself only ever sees the pointers.

## 371: What is file locking in Git LFS and why is it needed?

Binary files like Photoshop or Unity files can't be merged. If two people edit the same one, one person's work is lost.

```bash
git lfs track "*.psd" --lockable
git lfs lock design/home.psd
git lfs locks
git lfs unlock design/home.psd
```

Lockable files are checked out read-only until you lock them. The server tracks who holds each lock and refuses pushes that change a file locked by someone else.

## 372: What is a textconv diff driver?

A textconv driver converts a binary file to text before diffing, so `git diff` and `git log -p` show readable changes.

```gitattributes
*.pdf diff=pdf
*.docx diff=docx
```

```bash
git config diff.pdf.textconv pdftotext-wrapper
git config diff.docx.textconv "pandoc --to=plain"
```

The wrapper must print the text to stdout. It only affects diffs, not what's stored.

## 373: How do you write a custom merge driver?

Define it in config and attach it to paths in `.gitattributes`:

```gitattributes
CHANGELOG.md merge=union
translations/*.json merge=json-merge
```

```bash
git config merge.json-merge.name "JSON merge"
git config merge.json-merge.driver "json-merge-tool %O %A %B"
```

`%O` is the base, `%A` is ours (the driver writes the result here) and `%B` is theirs. Exit 0 for a clean merge, non-zero for a conflict. `union` is built in and keeps lines from both sides, which works for simple line-based files like changelogs.

## 374: What is git replace?

`git replace` lets you tell Git to use one object in place of another, without rewriting history. Commands like `log` see the replacement.

```bash
git replace a1b2c3d e4f5a6b
git replace --graft a1b2c3d new-parent    # give a commit a different parent
git replace -d a1b2c3d                     # remove the replacement
```

It's used to stitch together old and new history (for example after a migration with a cut-off point) while keeping the actual commits the same. Replacements live in `refs/replace/` and aren't pushed by default.

## 375: What are grafts and why were they replaced?

Grafts were an old feature (`.git/info/grafts`) that let you fake the parents of a commit. They were local only, couldn't be shared, and confused many commands.

They were deprecated in favor of `git replace --graft`, which stores the change as a normal replace ref that you can push, fetch and inspect. Shallow clones use a similar mechanism (`.git/shallow`).

## 376: How does a shallow clone work internally?

Git writes the hashes of the boundary commits into `.git/shallow`. For those commits, Git acts as if they had no parents, even though their commit objects still list parent hashes.

```bash
cat .git/shallow
git fetch --deepen=100
git fetch --shallow-since=2026-01-01
git fetch --unshallow
```

Operations that need history past the boundary (`merge-base`, `describe`, `blame`) give partial or wrong-looking results. Pushing from a shallow clone works but can be slow, because the server can't assume what you have.

## 377: How does a partial clone fetch missing objects?

A partial clone marks the remote as a "promisor remote" in config. Objects that were filtered out are "promised": when a command needs one, Git fetches it from the promisor on demand.

```bash
git config remote.origin.promisor        # true
git backfill                              # Git 2.49+, fetch missing blobs in batches
```

On-demand fetches happen one batch at a time, so commands like `git log -p` over a lot of history can be slow. `git backfill` downloads missing blobs for the current sparse checkout in bigger batches.

## 378: What is a bundle URI?

Bundle URIs let a server tell clients to download a prebuilt bundle file (for example from a CDN) before the normal fetch. The client gets most of the history from the static file, then fetches only what's newer from the Git server.

```bash
git clone --bundle-uri=https://cdn.example.com/repo.bundle https://github.com/org/repo.git
```

It moves clone load off the Git servers, which helps a lot for large repos with many CI clones.

## 379: How does git blame work and why can it be slow?

Blame starts with the current version of the file and walks back through history. For each commit, it diffs the file against the parent and "passes" responsibility for unchanged lines to the parent. Lines that changed in that commit are blamed on it. It continues until every line has an owner.

It's slow for files with long histories, many merges or when `-C` and `-M` are used to track moved and copied code, since those compare against many other files. Commit-graph and changed-path Bloom filters speed it up a lot.

## 380: How does git bisect handle merge commits and non-linear history?

Bisect works on the commit graph, not a straight line. It picks a commit that splits the set of suspect commits roughly in half, even across merges.

If a merge brought in the bug, bisect can end inside the merged branch, at a commit that never existed on `main` alone. If you only care about which merge broke `main`, use:

```bash
git bisect start --first-parent
```

That only checks commits on the first parent line.

## 381: What are git bisect terms?

By default bisect looks for the first "bad" commit. Sometimes you're looking for when something was fixed or changed, and "good" and "bad" are confusing.

```bash
git bisect start --term-old=slow --term-new=fast
git bisect fast
git bisect slow
```

You can also use the built-in pair `old` and `new`.

## 382: How do you recover after someone force pushed and removed commits from a shared branch?

1. Look for a clone that still has the old commits: your own reflog (`git reflog show origin/main`), or a teammate's.
2. On GitHub, the "Activity" view of the repo and the events API show the previous SHA of a forced update. Pull request refs may also still hold the commits.
3. Once you have the old hash:

```bash
git fetch origin <old-hash>      # works if the server still has the object
git branch rescue <old-hash>
git push origin rescue
```

Then merge or reset `main` to bring the lost commits back, and protect the branch against force pushes afterwards.

## 383: Why does git push --force-with-lease without arguments not always protect you?

`--force-with-lease` compares the remote branch with your remote-tracking branch (`origin/feature`). If something runs `git fetch` in the background, like your IDE, `origin/feature` gets updated to include your teammate's new commits. The lease then passes, and their commits are overwritten anyway.

Fixes:

```bash
git push --force-with-lease=feature:<expected-hash>
git push --force-with-lease --force-if-includes
```

`--force-if-includes` (Git 2.30+) also checks that the remote tip is part of your local branch's reflog, meaning you really saw and integrated it.

## 384: What does git push --atomic do?

With `--atomic`, when you push several refs, either all of them are updated or none are. Without it, some refs can succeed while others are rejected.

```bash
git push --atomic origin main v2.0.0
```

It's useful for releases, so you don't end up with a tag pushed but the branch update rejected.

## 385: What are push options?

Push options send extra strings to the server, which server hooks or the hosting service can read.

```bash
git push -o ci.skip
git push -o merge_request.create -o merge_request.target=main
```

GitLab supports options like skipping CI or creating a merge request on push. On your own server, hooks read them from `GIT_PUSH_OPTION_*` env variables. The server must have `receive.advertisePushOptions` turned on.

## 386: How do you update many refs safely in one go?

Use `git update-ref --stdin` with a transaction:

```bash
git update-ref --stdin <<EOF
start
update refs/heads/main $new_main $old_main
update refs/heads/release $new_rel $old_rel
delete refs/heads/old-feature
prepare
commit
EOF
```

All updates succeed or fail together, and each one checks the expected old value. It's what tools should use instead of writing files in `.git/refs` directly.

## 387: What are hidden refs and namespaces?

Servers can hide refs from clients with `transfer.hideRefs` (or `uploadpack.hideRefs`). For example, GitHub hides some internal refs from normal fetches.

Namespaces (`GIT_NAMESPACE`) let one repository act like many, with each namespace's refs stored under `refs/namespaces/<name>/`. Hosting tools use this to share objects between related repos, like forks, while keeping their refs apart.

## 388: How do forks on GitHub share storage?

Forks on GitHub share a single object store with the parent repository (a "network"). Pushing to a fork adds objects to the shared store, but each repo has its own refs.

A side effect: a commit pushed to a fork can sometimes be viewed through the parent repo's URL by its hash, even if it's not on any branch there. And a deleted fork or branch doesn't mean the objects are gone. This is one more reason leaked secrets must always be rotated.

## 389: What happens to pull request refs after you rewrite history?

GitHub keeps refs like `refs/pull/123/head` for each pull request, even after the branch is deleted. If a secret was in a PR commit, rewriting the branch doesn't remove it: the PR ref still points to the old commit.

You need to contact GitHub support to remove cached views and PR refs for sensitive data. That's why rotating the secret is always step one.

## 390: How do case-insensitive file systems cause problems in Git?

macOS and Windows file systems are usually case-insensitive. Git can store `Readme.md` and `README.md` as two files, but on those systems they map to the same path, so one overwrites the other. Branch names like `Feature/x` and `feature/x` can clash in the same way with the files backend for refs.

Renaming only the case of a file also often doesn't register:

```bash
git mv readme.md README.md
```

`git mv` handles it correctly. Plain renaming in Finder may not be seen as a change, depending on `core.ignoreCase`. Reftable avoids the branch name clash problem.

## 391: How does Git handle file permissions and executable bits?

Git only tracks whether a file is executable (`100755`) or not (`100644`). It doesn't store owners, groups or other permission bits.

```bash
git update-index --chmod=+x scripts/deploy.sh
git ls-files -s scripts/deploy.sh
```

On Windows or some mounted file systems, `core.fileMode` is often `false`, so Git ignores permission changes on disk. If a script isn't executable in CI, check the mode stored in Git with `ls-files -s`.

## 392: How does Git store symlinks?

A symlink is stored as a blob with mode `120000` whose content is the target path. On checkout, Git creates a symlink pointing to that path.

On Windows, symlinks need extra setup (`core.symlinks true` and developer mode or admin rights). Otherwise Git writes a plain text file with the target path. Symlinks pointing outside the repo, or into `.git`, have been part of several security issues, so Git checks them carefully.

## 393: What is the difference between assume-unchanged and skip-worktree?

Both make Git stop noticing changes to a tracked file, but they're meant for different things:

- `--assume-unchanged` is a performance hint: "don't check this file, it won't change". Git may drop the flag and overwrite the file during commands like pull.
- `--skip-worktree` means "I changed this file on purpose, leave my version alone". Git tries harder to keep it and complains if an update would overwrite it.

```bash
git update-index --skip-worktree config/local.json
git ls-files -v | grep '^S'
```

Neither is a good long-term fix for local config. Prefer an ignored local file plus a committed example file.

## 394: How do you deal with a corrupted repository?

1. Run `git fsck --full` to see what's broken.
2. Make a backup copy of the whole folder before touching anything.
3. If objects are missing, fetch them again from the remote: `git fetch` often fixes it. You can also copy the missing objects from another clone.
4. If refs are broken, fix them with `git update-ref` from the reflog or from the remote.
5. If it's very bad, clone again and copy your uncommitted work over.

Corruption usually comes from disk problems, a crash in the middle of writes or syncing `.git` with tools like Dropbox.

## 395: Why shouldn't you keep a Git repo in a Dropbox or iCloud folder?

Sync tools copy files one by one and don't understand Git's lock files and atomic renames. If two machines change the repo, or the sync runs in the middle of a Git command, you can end up with conflicting copies of refs, half-synced packs or a corrupted index.

Use a remote (GitHub, a bare repo on a server, or even a bundle file) to sync between machines instead.

## 396: What is the difference between git log ordering options?

- Default: reverse chronological order by commit date.
- `--topo-order`: keeps commits from one branch together, never shows a parent before all its children.
- `--date-order`: like topo order, but sorts by commit date where possible.
- `--author-date-order`: like date order, using author dates.
- `--reverse`: oldest first.

`--graph` uses topo order so the lines make sense. Dates can be wrong (clocks, rebases), so ordering by date alone isn't reliable.

## 397: How do you find the commit where two branches split, even after main was merged into the feature branch?

`git merge-base main feature` gives the latest common ancestor, which after a merge from `main` is a recent commit, not the original split point.

To find where `feature` first started, look for the oldest commit on `feature` that is not on `main`:

```bash
git log --oneline --reverse main..feature | head -1
git merge-base --fork-point main feature
```

`--fork-point` uses the reflog of `main` to find where `feature` forked, which also helps when `main` was rewritten. It needs the reflog, so it only works locally.

## 398: How does git rebase use --fork-point?

When you run `git rebase` with no upstream argument (so it uses the configured upstream), Git uses fork point mode by default. It checks the upstream's reflog to see if some commits on your branch were once part of the upstream and later removed by a force push.

Those commits are dropped from the rebase, so you don't bring back commits the upstream deliberately removed. If that surprises you, run `git rebase --no-fork-point`.

## 399: What are the trade-offs between a merge-heavy and a rebase-heavy workflow?

Merge-heavy:

- History shows what really happened, including when branches were integrated.
- No rewriting, so no force pushes and no risk to collaborators.
- The graph gets busy, and `bisect` and `log` are harder to read without `--first-parent`.

Rebase-heavy:

- Linear history, easy to read, bisect and revert.
- Needs force pushes on feature branches and discipline about shared branches.
- Conflicts must be resolved commit by commit, and every commit should still build.

Many teams rebase locally to clean up, then merge (or squash merge) into `main`.

## 400: How do you keep a long-lived branch from drifting too far from main?

- Merge or rebase `main` into it often, ideally every day, so conflicts stay small.
- Turn on rerere to reuse conflict resolutions.
- Split the work: merge finished parts into `main` behind a feature flag.
- Move shared refactors into `main` first, so both lines get them.
- Run CI on the branch with `main` merged in, so you find breakage early.

The real fix is usually to make the branch shorter-lived.

## 401: You pushed a commit straight to main by mistake, and the team only allows changes through pull requests. What do you do?

Don't rewrite `main`, because others may have pulled already. Instead:

```bash
git revert <hash>
git push origin main
```

Then open a pull request with the original change (cherry-pick it onto a new branch) so it goes through review. Afterwards, turn on branch protection so direct pushes to `main` are blocked for everyone, including admins if possible.

## 402: You ran git reset --hard and lost work. What can you get back?

- **Committed work:** yes. Find the old commit in `git reflog` and `git reset --hard HEAD@{1}` or create a branch from it.
- **Staged but not committed:** maybe. `git add` wrote blobs to the object store. `git fsck --lost-found` lists dangling blobs, and you can look through them with `git show <hash>`. File names are lost.
- **Never staged:** no, not from Git. Check your editor's local history (VS Code and JetBrains both keep one) or OS backups.

This is a good argument for committing often, even WIP commits that you squash later.

## 403: After a rebase, your pull request shows the same commits twice. Why, and how do you fix it?

This usually happens when a branch was rebased and then merged with the old version of itself, for example you rebased locally, then ran `git pull` (merge) instead of force pushing. Now both the old commits and their rebased copies are in the branch.

Fix it by resetting to the version you want and force pushing:

```bash
git reflog                          # find the clean rebased tip
git reset --hard <clean-tip>
git push --force-with-lease
```

Or rebase again onto `main`, which drops commits whose changes are already there. To avoid it, always use `--force-with-lease` after a rebase instead of pulling.

## 404: Your history is full of "Merge branch 'main' of github.com/..." commits. How do you stop that?

Those come from `git pull` merging the remote branch into your local branch when both have new commits. Set pull to rebase or to fast-forward only:

```bash
git config --global pull.rebase true
# or
git config --global pull.ff only
```

With `pull.rebase`, your local commits are replayed on top of the remote ones. With `pull.ff only`, the pull fails and you decide what to do.

## 405: A big formatting change on main causes conflicts in every open pull request. How do you handle it?

Options, from best to worst:

- Plan it: merge as many PRs as possible first, then land the formatting change at a quiet time.
- Each PR author runs the same formatter on their branch, then merges or rebases. Many conflicts disappear because both sides now look the same.
- Use merge options that ignore whitespace: `git rebase -X ignore-space-change main` or `git merge -X renormalize main` (when the change is line endings).
- Add the formatting commit to `.git-blame-ignore-revs` so blame stays useful.

A pre-commit formatter from day one prevents this.

## 406: How do you migrate a repository from SVN to Git?

1. Make an authors file mapping SVN usernames to `Name <email>`.
2. Convert with `git svn` or a dedicated tool like `svn2git`:

```bash
git svn clone https://svn.example.com/repo --stdlayout --authors-file=authors.txt repo-git
```

3. Turn SVN tags (which `git svn` imports as branches) into real Git tags, clean up branches, and add a `.gitignore` based on `svn:ignore`.
4. Check for huge binaries and move them to LFS before pushing.
5. Push to the new remote and make SVN read-only.

For big repos, do a trial run first and plan a freeze window for the final cutover.

## 407: How do you move a repository from GitLab to GitHub with all branches and tags?

```bash
git clone --mirror https://gitlab.com/org/app.git
cd app.git
git push --mirror https://github.com/org/app.git
```

This copies all refs. You may need to delete GitLab-specific refs first (like `refs/merge-requests/*`), because GitHub rejects pushes to some special ref names. Issues, merge requests, CI configs and wikis are not part of Git, so use the hosting service's import tools for those. Also move LFS objects with `git lfs fetch --all` and `git lfs push --all`.

## 408: A bug appeared in production between release v3.4.0 and v3.5.0. How do you find the cause?

```bash
git log --oneline --first-parent v3.4.0..v3.5.0    # merged PRs in that range
git bisect start v3.5.0 v3.4.0
git bisect run ./scripts/reproduce-bug.sh
```

`--first-parent` gives you the list of merges, which maps to pull requests, so you can scan for anything related first. If it's not obvious, bisect with a script that reproduces the bug. Use `git bisect start --first-parent` if you only want to find the PR, not the exact commit.

## 409: How do you generate release notes from Git history?

```bash
git log --oneline --no-merges v1.4.0..v1.5.0
git log --pretty=format:"- %s (%h)" v1.4.0..v1.5.0
git shortlog --no-merges v1.4.0..v1.5.0
```

With Conventional Commits, tools like release-please, semantic-release or git-cliff group commits by type (features, fixes, breaking changes) and write a `CHANGELOG.md`. GitHub can also auto-generate release notes from merged pull requests.

## 410: How do you embed the Git version into a build?

```bash
VERSION=$(git describe --tags --always --dirty)
COMMIT=$(git rev-parse --short HEAD)
```

Pass these into the build as env variables or build args, and show them in a `/version` endpoint or the app's about screen. That makes it easy to know exactly which commit is running.

In CI, make sure tags are fetched (`fetch-depth: 0` or `git fetch --tags`), otherwise `git describe` fails or falls back to a plain hash.

## 411: What are the pros and cons of deploying with "git pull" on the server?

Pros: simple, fast to set up, easy to see which commit is deployed.

Cons:

- The server needs Git and access to the repo, and maybe credentials.
- No build step isolation: dependencies install on the production box, and the build can fail halfway.
- Risk of exposing `.git` through the web server.
- Hard to roll back cleanly, no artifact you can promote from staging to production.

For real projects, build an artifact (a container image or bundle) in CI from a specific commit and deploy that.

## 412: What is GitOps?

GitOps is a way of running infrastructure where a Git repo holds the desired state (for example Kubernetes manifests or Helm values), and a tool like Argo CD or Flux keeps the cluster in sync with it.

Changes are made through pull requests, so you get review, history and easy rollback (revert the commit). The cluster pulls changes, so CI doesn't need direct production credentials.

## 413: Why should you add .git to .dockerignore?

- The `.git` folder can be large, which slows down the build context and can bloat images if you `COPY . .`.
- It may contain secrets in history, tokens in `.git/config` and private branch names.
- Any change to `.git` (like a new commit) busts Docker's layer cache for `COPY . .`.

If you need the commit hash in the image, pass it as a build arg:

```bash
docker build --build-arg GIT_SHA=$(git rev-parse HEAD) .
```

## 414: Your pre-commit hook takes 40 seconds and developers keep skipping it. What do you do?

- Only check staged files (lint-staged or the pre-commit framework), not the whole repo.
- Move slow things (full test suite, type check of the whole project) to `pre-push` or CI.
- Use caching in linters (`eslint --cache`).
- Make sure CI runs the same checks, so skipping the hook doesn't let bad code merge.

A hook should feel instant. If it doesn't, people will use `--no-verify` and the hook stops being useful.

## 415: How do you enforce the same Git rules across hundreds of repositories?

- Use organization-level rules: GitHub rulesets or GitLab group settings for branch protection, required reviews, signed commits and required status checks.
- Share CI templates or required workflows so every repo runs the same checks.
- Keep standard files (CODEOWNERS, PR templates, `.gitattributes`) in a template repo, and use a bot to keep them in sync.
- Use secret scanning and push protection at the organization level.

Doing it repo by repo by hand doesn't scale and drifts quickly.

## 416: What makes a commit history easy to work with later?

- **Atomic commits:** each commit does one thing and the code builds and passes tests at every commit.
- **Good messages:** a summary of what, and a body for why.
- **No noise:** WIP and "fix typo" commits squashed before merge.
- **Separation:** refactors, formatting and behavior changes in separate commits.

This pays off when you use `bisect`, `revert`, `blame` and cherry-pick. A history where commits don't build makes bisect useless.

## 417: Should generated files be committed?

Generally no: build output, compiled assets and anything you can regenerate from source should be ignored. They cause noisy diffs and merge conflicts.

Exceptions:

- Lock files (`package-lock.json`, `pnpm-lock.yaml`) should be committed for apps, because they make installs reproducible.
- Generated code that's hard to regenerate, or that consumers need without your tooling (like generated API clients in some setups).

If you commit generated files, mark them in `.gitattributes` (`linguist-generated`, `-diff`) so they're collapsed in reviews, and check in CI that they're up to date.

## 418: Why is Git bad at large binary files?

- Binaries don't delta-compress well, so each version is stored almost in full.
- Every clone downloads every version of every file, forever, unless you use partial clone or LFS.
- Binaries can't be merged, so parallel edits mean lost work.
- Large packs slow down clone, fetch, gc and hosting servers.

Use Git LFS or a separate artifact store for big binaries. Game studios with huge assets often use Perforce or Plastic SCM (Unity Version Control) instead, or Git with LFS and locking.

## 419: Why is "one branch per environment" (dev, staging, prod) considered an anti-pattern?

With environment branches, you promote code by merging between branches. Over time:

- Branches drift. Hotfixes go into `prod` and are forgotten in `dev`, and the same commit may not exist on all of them.
- What you tested on staging isn't the exact same commit you deploy to prod.
- Merges between environment branches cause conflicts unrelated to any feature.

The better approach is to build one artifact from one commit on `main`, and promote that same artifact through environments with config per environment.

## 420: You need to remove a feature now but bring it back later. How do you do it with Git?

```bash
git revert -m 1 <feature-merge-commit>
```

Later, to bring it back, revert the revert:

```bash
git revert <revert-commit>
```

Don't try to merge the old feature branch again, because Git sees its commits as already merged and won't re-apply them. In the future, a feature flag would let you turn the feature off without touching Git at all.

## 421: How do you plan a history rewrite on a shared repository?

1. Announce a date and time, and ask everyone to push their work and merge or close PRs before it.
2. Make a full backup (`git clone --mirror`).
3. Do the rewrite on a fresh mirror clone with `git filter-repo`.
4. Temporarily disable branch protection for force pushes, push with `--force --all` and `--tags`, then turn protection back on.
5. Tell everyone to re-clone. Old clones must not push, or they'll bring the old history back.
6. Check forks, CI caches and open PRs, which may still hold old commits.

## 422: How do you know who actually pushed a commit, not just who authored it?

The author and committer fields are set by whoever made the commit and can be anything. Git itself doesn't record who pushed.

The hosting service does: GitHub's audit log and repository activity view, GitLab's push events, or server-side `post-receive` hooks on your own server. Signed pushes (`git push --signed`) can also record a signed statement of who pushed what, if the server supports them.

## 423: How do you run several AI coding agents or tasks on one repo in parallel without conflicts?

Give each one its own worktree on its own branch:

```bash
git worktree add -b agent/fix-login ../app-fix-login main
git worktree add -b agent/refactor-api ../app-refactor-api main
```

They share one object database, so it's cheap, but each has its own files, index and `HEAD`, so they don't step on each other. When a task is done, review its branch, merge it, and `git worktree remove` the folder. Remember that each worktree needs its own `node_modules` or build folder.

## 424: What changed in the git config command in recent versions?

Git 2.46 added subcommands to `git config`, so the old flag style has clearer replacements:

```bash
git config list                 # was: git config --list
git config get user.email       # was: git config user.email
git config set user.email x@y.z # was: git config user.email x@y.z
git config unset user.email     # was: git config --unset user.email
```

The old forms still work. The new ones avoid confusing cases where the meaning depended on how many arguments you passed.

## 425: What is planned for Git 3.0?

Git 3.0 doesn't have a release date yet, but the planned breaking changes are listed in Git's `BreakingChanges` document. The main ones:

- New repos use SHA-256 instead of SHA-1 by default.
- New repos use `main` as the default branch name when `init.defaultBranch` isn't set.
- Reftable becomes the default ref storage format.
- Rust becomes required to build Git.
- Some old commands and options are removed, like `git whatchanged` and `git pack-redundant`.

Recent 2.x versions already print warnings for some of these, so you can prepare.

## 426: What happens step by step when you run git clone?

1. Git creates the folder and runs the equivalent of `git init`.
2. It adds the remote `origin` with the URL and the default fetch refspec.
3. It connects to the server, gets the list of refs and finds the default branch (the remote `HEAD`).
4. It fetches a packfile with all the objects (or a filtered set for partial clones, or limited depth for shallow clones) and builds the `.idx` file.
5. It creates remote-tracking refs (`origin/*`) and tags.
6. It creates a local branch for the default branch, tracking `origin/<default>`.
7. It checks out that branch into the working directory and writes the index.

## 427: What happens on the server when you run git push?

1. The client runs `send-pack`, which talks to `receive-pack` on the server.
2. The server lists its refs. The client figures out which objects the server is missing and sends them as a packfile, plus the ref updates it wants (old hash, new hash, ref name).
3. The server stores the pack and checks connectivity (all referenced objects exist) and, if configured, runs fsck on the objects.
4. The `pre-receive` hook runs, then `update` for each ref. Either can reject the push.
5. Refs are updated, atomically if `--atomic` was used.
6. `post-receive` and `post-update` hooks run, and the client gets a status line for each ref.

## 428: What does a "missing object" or "bad object" error usually mean?

It means a ref or another object points to an object that isn't in the repo. Common causes:

- A shallow or partial clone is missing history a command needs.
- Garbage collection removed objects that something still pointed to (for example after a crash or editing `.git` by hand).
- Disk or sync tool corruption.
- An `alternates` repo used with `--reference` was deleted.

Start with `git fsck`. Running `git fetch` (or `git fetch --refetch`) often restores missing objects from the remote.

## 429: What do the ^{}, ^{tree} and :/ revision suffixes do?

```bash
git rev-parse v1.0.0^{}        # "peel" the tag down to the commit it points to
git rev-parse v1.0.0^{commit}  # same, but fails if it's not a commit
git rev-parse HEAD^{tree}      # the tree of a commit
git show :/"fix login"         # the newest commit whose message matches the text
git show :0:src/app.js         # the staged version of a file
```

`^{}` matters for annotated tags: the tag name points to a tag object, not directly to a commit. `git ls-remote` shows both, with the peeled one marked `^{}`.

## 430: Why should you never move a tag that was already pushed?

Git doesn't update tags that already exist locally when you fetch, unless you force it. If you move `v1.2.0` and push it with `--force`, people who already fetched the old tag keep the old commit, so two people can build "v1.2.0" from different code.

Package managers, CI caches and Go module proxies may have cached the old one too. If a release was wrong, make a new tag, like `v1.2.1`.

## 431: What is a signed push?

`git push --signed` sends a signed "push certificate" listing the ref updates. The server can check the signature in its `pre-receive` hook and store it as proof of who pushed what.

It's different from signed commits: commit signatures prove who made a commit, push certificates prove who moved a ref. It needs server support (`receive.certNonceSeed`), and the big hosting services don't use it, so it's mostly seen on self-hosted servers.

## 432: Why does a rebase change commit hashes even when there are no conflicts and no content changes?

Each rebased commit has a new parent, and the parent hash is part of the commit content. The committer date is also updated to the time of the rebase. Either change gives a new hash, and since each commit's hash goes into the next commit, all following commits change too.

If the base didn't change at all, `git rebase` just says the branch is up to date and doesn't rewrite anything (unless you force it with `--force-rebase`).

## 433: Can two different commits have the same tree?

Yes. The tree only describes file contents. Two commits with different parents, messages or dates can point to the same tree, for example:

- A commit and the revert of its revert
- A merge with `-s ours`
- An empty commit (same tree as its parent)

You can use this in scripts to check whether a branch actually changes anything: compare `git rev-parse branch^{tree}` with another commit's tree.

## 434: What is git patch-id?

`git patch-id` computes an ID from the content of a diff, ignoring line numbers and whitespace. Two commits that make the same change (like an original and its cherry-picked copy) have the same patch ID even though their hashes differ.

```bash
git show a1b2c3d | git patch-id --stable
```

Rebase, `git cherry` and `git log --cherry-pick` use patch IDs to skip commits whose change is already upstream.

## 435: How can you tell whether a squash-merged branch is really in main?

The branch's commits aren't in `main`, so `git branch --merged` won't list it. Some ways to check:

- Compare the combined diff: create a temporary squash of the branch onto its merge base and check if its patch ID matches a commit on `main`.
- Try `git merge-tree --write-tree main feature`. If the resulting tree is the same as `main`'s tree, the branch adds nothing new.
- Use the hosting service: GitHub shows the PR as merged and can delete the branch automatically.

In practice, teams that squash merge set branches to auto-delete after merge.

## 436: How does Git handle conflicts in binary files?

Git can't merge binary files line by line. If both sides changed a binary file, Git marks it as conflicted and leaves your version in the working directory. You pick one side:

```bash
git checkout --ours assets/logo.png
git checkout --theirs assets/logo.png
git add assets/logo.png
```

Or use a merge driver that understands the format. For files people edit in parallel, LFS file locking avoids the problem.

## 437: How do you rebase a branch that has merge commits in it?

A normal rebase drops merge commits and flattens the history. To keep them:

```bash
git rebase --rebase-merges main
```

Git rebuilds the branch structure, including merges, on top of the new base. The todo list uses `label`, `reset` and `merge` commands to describe the graph. The old `--preserve-merges` option was removed, and `--rebase-merges` replaced it.

## 438: How do you restore a folder to how it was at an old commit while keeping history?

```bash
git restore --source=v2.0.0 --staged --worktree -- src/payments/
git commit -m "Restore payments module to v2.0.0"
```

This creates a new commit, so nothing is rewritten. `git restore` works in "no-overlay" mode by default, so tracked files that were added to the folder after `v2.0.0` are removed too, and the folder matches the old version exactly. Untracked files in the folder are left alone.

## 439: How do you scan a repository's full history for leaked secrets?

Use a secret scanner that understands Git history:

```bash
gitleaks git -v .
trufflehog git file://. --only-verified
```

These check every commit, not just the current files. Run it once on the whole history when you adopt a tool, then on each push or pull request in CI. GitHub secret scanning does this on the server for supported token types. Anything found must be rotated, even if it's only in old commits.

## 440: How would you design a branching and release process for a mobile app that supports several versions at once?

A common setup:

- `main` gets all new work through short-lived branches and PRs.
- When a release is ready, create `release/5.2` from `main` and tag builds from it (`v5.2.0`, `v5.2.1`). Only fixes go into it.
- Fixes land on `main` first, then get cherry-picked (with `-x`) into the release branches that still need them.
- Old release branches are kept as long as that version is supported, then archived.
- Feature flags (often remote config) let you ship code turned off and enable it without a new store release.

App store review times make quick rollbacks hard, so flags and careful release branches matter more than on the web.

## 441: Why might git log show commits out of date order?

Commit dates come from the clock of the machine that made the commit, and they can be set by hand. Rebases and cherry-picks keep the original author date but set a new committer date.

So a parent can have a newer date than its child, and `git log` dates may look out of order. Git's history is defined by parent links, not dates. If you need a reliable order, use `--topo-order`.

## 442: What is the difference between git reset --keep and --hard?

Both move the branch and update the working directory, but `--keep` refuses to throw away local changes. If a file has uncommitted changes and also differs between `HEAD` and the target commit, `--keep` stops with an error instead of overwriting.

```bash
git reset --keep HEAD~1
```

It's a safer choice when you want to drop the last commit but have unrelated work in progress.

## 443: How do you safely clean up hundreds of stale remote branches?

```bash
git fetch --prune
git for-each-ref --format="%(committerdate:short) %(refname:short)" \
  --sort=committerdate refs/remotes/origin/ |
  awk '$1 < "2026-01-01"'
```

Check the list (open PRs, release branches you must keep), then delete in a batch:

```bash
git push origin --delete old-branch-1 old-branch-2 old-branch-3
```

Turn on "automatically delete head branches" in the hosting service so it doesn't pile up again.

## 444: How do you find which commits are on main but not yet deployed?

Tag or mark each deploy, then compare:

```bash
git log --oneline deployed/production..origin/main
```

Many teams move a tag or branch like `deployed/production` in the deploy pipeline (that's a case where moving a ref is fine, since it's not a release tag). You can also store the deployed commit hash in the app and compare against it.

## 445: How would you explain the Git data model in one minute in an interview?

Git stores four kinds of objects, each named by the hash of its content: blobs (file contents), trees (folders), commits (a tree plus parents and metadata) and annotated tags. Objects never change, so a commit hash identifies the full snapshot and all history behind it.

Branches and tags are just names pointing to commits, and `HEAD` points to the current branch. Almost every command is about creating new objects and moving these pointers around. Once that clicks, reset, rebase and reflog are easy to understand.

## 446: What is the difference between git revert and git restore for undoing changes to a file?

`git restore --source=<commit> file` changes the file in your working directory to an old version. Nothing is committed until you commit it, and it affects the whole file, including later changes you might want to keep.

`git revert <commit>` undoes exactly the changes made in one commit, across all files it touched, and creates a commit for that. Later changes to the same files stay, unless they conflict.

Use revert to undo a specific change. Use restore to get a file back to a known state.

## 447: How do you handle a merge where both sides renamed the same file differently?

Git reports a rename/rename conflict: one side renamed `a.js` to `b.js` and the other to `c.js`. Both files may be left in the working directory.

Decide which name is correct, keep one, move any changes from the other into it, then:

```bash
git rm c.js
git add b.js
git commit
```

Check imports and references in other files, because the rest of the code may expect either name.

## 448: What is git fetch --refetch?

`--refetch` (Git 2.36+) fetches all objects again from scratch, as if you were cloning, instead of negotiating based on what you already have.

```bash
git fetch --refetch origin
```

It's useful when you change the partial clone filter of an existing repo (for example to download blobs you skipped before), or when local objects may be corrupted.

## 449: How do you check if your local Git setup will cause problems for the team?

```bash
git config --list --show-origin
git config --get core.autocrlf
git config --get user.email
git var GIT_EDITOR
```

Look for things like a wrong email, `core.autocrlf` that fights with `.gitattributes`, a global `core.hooksPath` that overrides the project's hooks, or an old Git version. Many teams put the recommended settings in a setup script or README.

## 450: What changed in recent Git versions that you should know about?

Some useful changes from the last few years:

- `git switch` and `git restore` replaced most uses of `git checkout`.
- `ort` became the default merge strategy, and `recursive` now just uses it.
- SSH keys can sign commits, and `zdiff3` conflict style, `--update-refs` and `push.autoSetupRemote` made daily work easier.
- Large repo features matured: partial clone, sparse checkout cone mode, fsmonitor, Scalar, `git maintenance` and `git backfill`.
- Reftable and SHA-256 are ready to use and planned as defaults in Git 3.0, together with `main` as the default branch.
- `git config` got subcommands (`get`, `set`, `list`, `unset`), and `git stash` can export and import stashes.

Read the release notes when you upgrade. Git releases a new minor version about every three months.
