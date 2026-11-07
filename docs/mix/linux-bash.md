# Linux Bash Interview Questions and Answers

_Last updated: October 29, 2026_

450 Linux and Bash interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers target Bash 5.x (5.3 is the latest release) on a modern Linux distribution with GNU coreutils and systemd. Where macOS or POSIX `sh` behave differently, the answer says so, since you will run into both in real projects.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is Linux?](#1-what-is-linux)
- [2: What is a Linux distribution?](#2-what-is-a-linux-distribution)
- [3: What is a shell?](#3-what-is-a-shell)
- [4: What is Bash?](#4-what-is-bash)
- [5: What is the difference between sh and bash?](#5-what-is-the-difference-between-sh-and-bash)
- [6: How do you check which shell you are using?](#6-how-do-you-check-which-shell-you-are-using)
- [7: What is the difference between a terminal and a shell?](#7-what-is-the-difference-between-a-terminal-and-a-shell)
- [8: What is a shebang line?](#8-what-is-a-shebang-line)
- [9: How do you run a shell script?](#9-how-do-you-run-a-shell-script)
- [10: Why do you need ./ to run a script in the current directory?](#10-why-do-you-need--to-run-a-script-in-the-current-directory)
- [11: What does the Linux filesystem hierarchy look like?](#11-what-does-the-linux-filesystem-hierarchy-look-like)
- [12: What is the difference between an absolute and a relative path?](#12-what-is-the-difference-between-an-absolute-and-a-relative-path)
- [13: How do you see the current directory and move between directories?](#13-how-do-you-see-the-current-directory-and-move-between-directories)
- [14: How do you list files with ls?](#14-how-do-you-list-files-with-ls)
- [15: What are hidden files in Linux?](#15-what-are-hidden-files-in-linux)
- [16: How do you create files and directories?](#16-how-do-you-create-files-and-directories)
- [17: How do you copy files and directories?](#17-how-do-you-copy-files-and-directories)
- [18: How do you move or rename files?](#18-how-do-you-move-or-rename-files)
- [19: How do you delete files and directories?](#19-how-do-you-delete-files-and-directories)
- [20: How do you view the contents of a file?](#20-how-do-you-view-the-contents-of-a-file)
- [21: What does tail -f do?](#21-what-does-tail--f-do)
- [22: What is the difference between echo and printf?](#22-what-is-the-difference-between-echo-and-printf)
- [23: How do you get help for a command?](#23-how-do-you-get-help-for-a-command)
- [24: What is the difference between type and which?](#24-what-is-the-difference-between-type-and-which)
- [25: What is the history command?](#25-what-is-the-history-command)
- [26: What are some useful Bash keyboard shortcuts?](#26-what-are-some-useful-bash-keyboard-shortcuts)
- [27: What are wildcards (globs)?](#27-what-are-wildcards-globs)
- [28: How do you create and use a variable in Bash?](#28-how-do-you-create-and-use-a-variable-in-bash)
- [29: What is the difference between single and double quotes?](#29-what-is-the-difference-between-single-and-double-quotes)
- [30: Why should you quote variables?](#30-why-should-you-quote-variables)
- [31: What are environment variables?](#31-what-are-environment-variables)
- [32: What does export do?](#32-what-does-export-do)
- [33: What is the PATH variable?](#33-what-is-the-path-variable)
- [34: How do you set a variable for a single command only?](#34-how-do-you-set-a-variable-for-a-single-command-only)
- [35: What is an exit code?](#35-what-is-an-exit-code)
- [36: What do &&, || and ; do between commands?](#36-what-do---and--do-between-commands)
- [37: What is a pipe?](#37-what-is-a-pipe)
- [38: What are stdin, stdout and stderr?](#38-what-are-stdin-stdout-and-stderr)
- [39: How does output redirection work?](#39-how-does-output-redirection-work)
- [40: What is /dev/null?](#40-what-is-devnull)
- [41: How do you search text in files with grep?](#41-how-do-you-search-text-in-files-with-grep)
- [42: How do you find files with find?](#42-how-do-you-find-files-with-find)
- [43: How do you count lines, words and characters?](#43-how-do-you-count-lines-words-and-characters)
- [44: How do you sort lines?](#44-how-do-you-sort-lines)
- [45: What does uniq do?](#45-what-does-uniq-do)
- [46: How do you cut columns out of text?](#46-how-do-you-cut-columns-out-of-text)
- [47: What does the tr command do?](#47-what-does-the-tr-command-do)
- [48: What are users and groups in Linux?](#48-what-are-users-and-groups-in-linux)
- [49: Who is the root user?](#49-who-is-the-root-user)
- [50: What is the difference between sudo and su?](#50-what-is-the-difference-between-sudo-and-su)
- [51: How do Linux file permissions work?](#51-how-do-linux-file-permissions-work)
- [52: How do you change permissions with chmod?](#52-how-do-you-change-permissions-with-chmod)
- [53: What do numeric permissions like 755 and 644 mean?](#53-what-do-numeric-permissions-like-755-and-644-mean)
- [54: How do you change the owner of a file?](#54-how-do-you-change-the-owner-of-a-file)
- [55: How do you see running processes?](#55-how-do-you-see-running-processes)
- [56: What is a PID?](#56-what-is-a-pid)
- [57: How do you stop a process with kill?](#57-how-do-you-stop-a-process-with-kill)
- [58: How do you run a command in the background?](#58-how-do-you-run-a-command-in-the-background)
- [59: What does nohup do?](#59-what-does-nohup-do)
- [60: How do you check disk space?](#60-how-do-you-check-disk-space)
- [61: How do you check memory usage?](#61-how-do-you-check-memory-usage)
- [62: How do you get basic system information?](#62-how-do-you-get-basic-system-information)
- [63: How do you show the current date and time?](#63-how-do-you-show-the-current-date-and-time)
- [64: What is the difference between a hard link and a symbolic link?](#64-what-is-the-difference-between-a-hard-link-and-a-symbolic-link)
- [65: How do you find out what type a file is?](#65-how-do-you-find-out-what-type-a-file-is)
- [66: How do you create and extract a tar archive?](#66-how-do-you-create-and-extract-a-tar-archive)
- [67: How do you compress and decompress single files?](#67-how-do-you-compress-and-decompress-single-files)
- [68: How do you connect to a remote server with ssh?](#68-how-do-you-connect-to-a-remote-server-with-ssh)
- [69: How do you copy files between machines?](#69-how-do-you-copy-files-between-machines)
- [70: How do you download files or call APIs from the command line?](#70-how-do-you-download-files-or-call-apis-from-the-command-line)
- [71: How do you install packages on Ubuntu or Debian?](#71-how-do-you-install-packages-on-ubuntu-or-debian)
- [72: What is systemd and how do you manage services?](#72-what-is-systemd-and-how-do-you-manage-services)
- [73: How do you read service logs with journalctl?](#73-how-do-you-read-service-logs-with-journalctl)
- [74: What is the difference between .bashrc and .bash_profile?](#74-what-is-the-difference-between-bashrc-and-bash_profile)
- [75: What is an alias?](#75-what-is-an-alias)
- [76: What does source do?](#76-what-does-source-do)
- [77: What is command substitution?](#77-what-is-command-substitution)
- [78: How do you do math in Bash?](#78-how-do-you-do-math-in-bash)
- [79: How do you write an if statement?](#79-how-do-you-write-an-if-statement)
- [80: What is the test command and how does [ ] relate to it?](#80-what-is-the-test-command-and-how-does---relate-to-it)
- [81: What is the difference between [ ] and [[ ]]?](#81-what-is-the-difference-between---and--)
- [82: What are the common file test operators?](#82-what-are-the-common-file-test-operators)
- [83: How do you compare strings in Bash?](#83-how-do-you-compare-strings-in-bash)
- [84: How do you compare numbers in Bash?](#84-how-do-you-compare-numbers-in-bash)
- [85: How do you write a for loop?](#85-how-do-you-write-a-for-loop)
- [86: How do you write a while loop?](#86-how-do-you-write-a-while-loop)
- [87: What is an until loop?](#87-what-is-an-until-loop)
- [88: How does the case statement work?](#88-how-does-the-case-statement-work)
- [89: How do you define and call a function?](#89-how-do-you-define-and-call-a-function)
- [90: How do you use arguments in a script or function?](#90-how-do-you-use-arguments-in-a-script-or-function)
- [91: How do you read user input?](#91-how-do-you-read-user-input)
- [92: How do you write comments in Bash?](#92-how-do-you-write-comments-in-bash)
- [93: What does exit do in a script?](#93-what-does-exit-do-in-a-script)
- [94: How do you create and use an array?](#94-how-do-you-create-and-use-an-array)
- [95: How do you get the length of a string?](#95-how-do-you-get-the-length-of-a-string)
- [96: What is brace expansion?](#96-what-is-brace-expansion)
- [97: What does tilde ~ expand to?](#97-what-does-tilde--expand-to)
- [98: How do you clear the terminal screen?](#98-how-do-you-clear-the-terminal-screen)
- [99: How do you compare two files?](#99-how-do-you-compare-two-files)
- [100: What is xargs used for?](#100-what-is-xargs-used-for)
- [101: What is sed and how do you do a simple find and replace?](#101-what-is-sed-and-how-do-you-do-a-simple-find-and-replace)
- [102: What is awk and how do you print a column?](#102-what-is-awk-and-how-do-you-print-a-column)
- [103: What is the difference between a shell variable and an environment variable?](#103-what-is-the-difference-between-a-shell-variable-and-an-environment-variable)
- [104: How do you debug a Bash script?](#104-how-do-you-debug-a-bash-script)
- [105: How do you pause a script?](#105-how-do-you-pause-a-script)
- [106: What are true and false in Bash?](#106-what-are-true-and-false-in-bash)
- [107: How do you generate a sequence of numbers?](#107-how-do-you-generate-a-sequence-of-numbers)
- [108: What do basename and dirname do?](#108-what-do-basename-and-dirname-do)
- [109: What is cron and how do you schedule a job?](#109-what-is-cron-and-how-do-you-schedule-a-job)
- [110: How do you check network interfaces and IP addresses?](#110-how-do-you-check-network-interfaces-and-ip-addresses)
- [111: How do you check if a host is reachable?](#111-how-do-you-check-if-a-host-is-reachable)
- [112: How do you see which ports are open on a machine?](#112-how-do-you-see-which-ports-are-open-on-a-machine)
- [113: Where are log files kept in Linux?](#113-where-are-log-files-kept-in-linux)
- [114: How do you shut down or reboot a Linux machine?](#114-how-do-you-shut-down-or-reboot-a-linux-machine)
- [115: How do you change your password or another user's password?](#115-how-do-you-change-your-password-or-another-users-password)
- [116: How do you add a new user?](#116-how-do-you-add-a-new-user)
- [117: How do you change your default shell?](#117-how-do-you-change-your-default-shell)
- [118: What is a login shell and an interactive shell?](#118-what-is-a-login-shell-and-an-interactive-shell)
- [119: How do you edit a file in the terminal?](#119-how-do-you-edit-a-file-in-the-terminal)
- [120: How do you print the first or last N characters of a line?](#120-how-do-you-print-the-first-or-last-n-characters-of-a-line)
- [121: How do you check if a variable is empty?](#121-how-do-you-check-if-a-variable-is-empty)
- [122: What is the difference between > and >>?](#122-what-is-the-difference-between--and-)
- [123: How do you redirect stderr to stdout?](#123-how-do-you-redirect-stderr-to-stdout)
- [124: What is the difference between rm -r and rmdir?](#124-what-is-the-difference-between-rm--r-and-rmdir)
- [125: How do you list the contents of a directory as a tree?](#125-how-do-you-list-the-contents-of-a-directory-as-a-tree)
- [126: How do you look at the beginning of many files at once?](#126-how-do-you-look-at-the-beginning-of-many-files-at-once)
- [127: How do you see who is logged in?](#127-how-do-you-see-who-is-logged-in)
- [128: What does the env command do?](#128-what-does-the-env-command-do)
- [129: How do you make a variable read-only?](#129-how-do-you-make-a-variable-read-only)
- [130: How do you remove a variable?](#130-how-do-you-remove-a-variable)
- [131: What is the difference between $@ and $*?](#131-what-is-the-difference-between--and-)
- [132: What does $? hold and when should you check it?](#132-what-does--hold-and-when-should-you-check-it)
- [133: How do you check if a command exists?](#133-how-do-you-check-if-a-command-exists)
- [134: What does the touch command do besides creating files?](#134-what-does-the-touch-command-do-besides-creating-files)
- [135: How do you count the number of files in a directory?](#135-how-do-you-count-the-number-of-files-in-a-directory)
- [136: What are the common package formats?](#136-what-are-the-common-package-formats)
- [137: How do you check the size of a file?](#137-how-do-you-check-the-size-of-a-file)
- [138: What does the stat command show?](#138-what-does-the-stat-command-show)
- [139: How do you see the end of a command's output only?](#139-how-do-you-see-the-end-of-a-commands-output-only)
- [140: How do you run the same command again with a small change?](#140-how-do-you-run-the-same-command-again-with-a-small-change)
- [141: How do you check what a command will do before running it?](#141-how-do-you-check-what-a-command-will-do-before-running-it)
- [142: What is a process versus a program?](#142-what-is-a-process-versus-a-program)
- [143: What is the difference between a builtin and an external command?](#143-what-is-the-difference-between-a-builtin-and-an-external-command)
- [144: How do you print a message to stderr?](#144-how-do-you-print-a-message-to-stderr)
- [145: How do you run a command as a different user?](#145-how-do-you-run-a-command-as-a-different-user)
- [146: How do you view the manual page sections?](#146-how-do-you-view-the-manual-page-sections)
- [147: What is the difference between cat and less?](#147-what-is-the-difference-between-cat-and-less)
- [148: How do you check how long a command takes?](#148-how-do-you-check-how-long-a-command-takes)
- [149: What is the difference between apt and apt-get?](#149-what-is-the-difference-between-apt-and-apt-get)
- [150: How do you make a simple backup of a file before editing it?](#150-how-do-you-make-a-simple-backup-of-a-file-before-editing-it)

### Moderate Questions (151-300)

- [151: What does set -euo pipefail do?](#151-what-does-set--euo-pipefail-do)
- [152: What is trap and how do you use it?](#152-what-is-trap-and-how-do-you-use-it)
- [153: How do you parse command line options with getopts?](#153-how-do-you-parse-command-line-options-with-getopts)
- [154: How do you set a default value for a variable?](#154-how-do-you-set-a-default-value-for-a-variable)
- [155: How do you make a script fail when a required variable is missing?](#155-how-do-you-make-a-script-fail-when-a-required-variable-is-missing)
- [156: How do you remove a prefix or suffix from a variable?](#156-how-do-you-remove-a-prefix-or-suffix-from-a-variable)
- [157: How do you replace text inside a variable?](#157-how-do-you-replace-text-inside-a-variable)
- [158: How do you change the case of a string in Bash?](#158-how-do-you-change-the-case-of-a-string-in-bash)
- [159: What is indirect variable expansion?](#159-what-is-indirect-variable-expansion)
- [160: How do associative arrays work?](#160-how-do-associative-arrays-work)
- [161: How do you read a file into an array?](#161-how-do-you-read-a-file-into-an-array)
- [162: How do you read a file line by line?](#162-how-do-you-read-a-file-line-by-line)
- [163: What is IFS?](#163-what-is-ifs)
- [164: How do you split a string into an array?](#164-how-do-you-split-a-string-into-an-array)
- [165: How do you join array items with a separator?](#165-how-do-you-join-array-items-with-a-separator)
- [166: What is process substitution?](#166-what-is-process-substitution)
- [167: What is a here document?](#167-what-is-a-here-document)
- [168: How do you stop variable expansion in a here document?](#168-how-do-you-stop-variable-expansion-in-a-here-document)
- [169: What does <<- do in a here document?](#169-what-does---do-in-a-here-document)
- [170: What is a here string?](#170-what-is-a-here-string)
- [171: What is the difference between ( ) and { } for grouping commands?](#171-what-is-the-difference-between---and---for-grouping-commands)
- [172: How do local variables work in functions?](#172-how-do-local-variables-work-in-functions)
- [173: How do you return a value from a function?](#173-how-do-you-return-a-value-from-a-function)
- [174: What is PIPESTATUS?](#174-what-is-pipestatus)
- [175: What are the main gotchas with set -e?](#175-what-are-the-main-gotchas-with-set--e)
- [176: What is the difference between find -exec and xargs?](#176-what-is-the-difference-between-find--exec-and-xargs)
- [177: How do you safely handle file names with spaces or newlines in a pipeline?](#177-how-do-you-safely-handle-file-names-with-spaces-or-newlines-in-a-pipeline)
- [178: What are the useful grep options for real work?](#178-what-are-the-useful-grep-options-for-real-work)
- [179: How do you use sed with line ranges and patterns?](#179-how-do-you-use-sed-with-line-ranges-and-patterns)
- [180: Why does sed -i behave differently on Linux and macOS?](#180-why-does-sed--i-behave-differently-on-linux-and-macos)
- [181: How do you use BEGIN and END blocks in awk?](#181-how-do-you-use-begin-and-end-blocks-in-awk)
- [182: How do you count and group with awk?](#182-how-do-you-count-and-group-with-awk)
- [183: How do you sort by a specific column?](#183-how-do-you-sort-by-a-specific-column)
- [184: How do you find the top N most common lines?](#184-how-do-you-find-the-top-n-most-common-lines)
- [185: What does tee do?](#185-what-does-tee-do)
- [186: How do you join lines from two files side by side?](#186-how-do-you-join-lines-from-two-files-side-by-side)
- [187: How do you format output into aligned columns?](#187-how-do-you-format-output-into-aligned-columns)
- [188: How do you find lines that are in one file but not another?](#188-how-do-you-find-lines-that-are-in-one-file-but-not-another)
- [189: How do you do floating point math in a script?](#189-how-do-you-do-floating-point-math-in-a-script)
- [190: What is the difference between let, (( )) and $(( ))?](#190-what-is-the-difference-between-let---and--)
- [191: How do you generate random numbers?](#191-how-do-you-generate-random-numbers)
- [192: How do you match a regular expression in Bash?](#192-how-do-you-match-a-regular-expression-in-bash)
- [193: What do shopt options like nullglob, globstar and extglob do?](#193-what-do-shopt-options-like-nullglob-globstar-and-extglob-do)
- [194: What is the difference between globs and regular expressions?](#194-what-is-the-difference-between-globs-and-regular-expressions)
- [195: What is the difference between "${arr[@]}" and "${arr[*]}"?](#195-what-is-the-difference-between-arr-and-arr)
- [196: What does shift do?](#196-what-does-shift-do)
- [197: How do you build a simple menu with select?](#197-how-do-you-build-a-simple-menu-with-select)
- [198: What are the special strings and gotchas in crontab syntax?](#198-what-are-the-special-strings-and-gotchas-in-crontab-syntax)
- [199: Why does a script work in my terminal but not in cron?](#199-why-does-a-script-work-in-my-terminal-but-not-in-cron)
- [200: How do you write a basic systemd service for an app?](#200-how-do-you-write-a-basic-systemd-service-for-an-app)
- [201: What is a systemd timer and why use it instead of cron?](#201-what-is-a-systemd-timer-and-why-use-it-instead-of-cron)
- [202: How do you filter journalctl output?](#202-how-do-you-filter-journalctl-output)
- [203: How do you set up SSH key login?](#203-how-do-you-set-up-ssh-key-login)
- [204: What is the ~/.ssh/config file for?](#204-what-is-the-sshconfig-file-for)
- [205: How does SSH port forwarding work?](#205-how-does-ssh-port-forwarding-work)
- [206: How do you use ProxyJump to reach a server behind a bastion?](#206-how-do-you-use-proxyjump-to-reach-a-server-behind-a-bastion)
- [207: What are the most useful rsync options?](#207-what-are-the-most-useful-rsync-options)
- [208: What are setuid, setgid and the sticky bit?](#208-what-are-setuid-setgid-and-the-sticky-bit)
- [209: What is umask?](#209-what-is-umask)
- [210: What are ACLs and when do you need them?](#210-what-are-acls-and-when-do-you-need-them)
- [211: How do you safely edit sudo permissions?](#211-how-do-you-safely-edit-sudo-permissions)
- [212: How do you add a user to a group, and why does it not work right away?](#212-how-do-you-add-a-user-to-a-group-and-why-does-it-not-work-right-away)
- [213: How do you customize the Bash prompt?](#213-how-do-you-customize-the-bash-prompt)
- [214: What is PROMPT_COMMAND?](#214-what-is-prompt_command)
- [215: How do you configure Bash history?](#215-how-do-you-configure-bash-history)
- [216: When should you use a function instead of an alias?](#216-when-should-you-use-a-function-instead-of-an-alias)
- [217: What do the command and builtin builtins do?](#217-what-do-the-command-and-builtin-builtins-do)
- [218: What does hash do in Bash?](#218-what-does-hash-do-in-bash)
- [219: What does exec do?](#219-what-does-exec-do)
- [220: How do you run several jobs in the background and wait for them?](#220-how-do-you-run-several-jobs-in-the-background-and-wait-for-them)
- [221: What is the difference between nohup, disown and &?](#221-what-is-the-difference-between-nohup-disown-and-)
- [222: How do you limit how long a command can run?](#222-how-do-you-limit-how-long-a-command-can-run)
- [223: What does watch do?](#223-what-does-watch-do)
- [224: How do you run commands in parallel with xargs?](#224-how-do-you-run-commands-in-parallel-with-xargs)
- [225: What does lsof show?](#225-what-does-lsof-show)
- [226: What is strace and when do you use it?](#226-what-is-strace-and-when-do-you-use-it)
- [227: What are the useful options of ps?](#227-what-are-the-useful-options-of-ps)
- [228: How do pgrep and pkill work?](#228-how-do-pgrep-and-pkill-work)
- [229: What is the difference between SIGTERM, SIGKILL, SIGINT and SIGHUP?](#229-what-is-the-difference-between-sigterm-sigkill-sigint-and-sighup)
- [230: How do nice and renice work?](#230-how-do-nice-and-renice-work)
- [231: What does ulimit do?](#231-what-does-ulimit-do)
- [232: Why can df show the disk as full while du shows much less used?](#232-why-can-df-show-the-disk-as-full-while-du-shows-much-less-used)
- [233: What does it mean when you get "No space left on device" but df shows free space?](#233-what-does-it-mean-when-you-get-no-space-left-on-device-but-df-shows-free-space)
- [234: How do you find the biggest files and directories?](#234-how-do-you-find-the-biggest-files-and-directories)
- [235: What is logrotate?](#235-what-is-logrotate)
- [236: How do you debug HTTP requests from the command line?](#236-how-do-you-debug-http-requests-from-the-command-line)
- [237: How do you check DNS resolution?](#237-how-do-you-check-dns-resolution)
- [238: What is netcat used for?](#238-what-is-netcat-used-for)
- [239: What are /etc/hosts and /etc/resolv.conf?](#239-what-are-etchosts-and-etcresolvconf)
- [240: How do you open a port in the firewall?](#240-how-do-you-open-a-port-in-the-firewall)
- [241: How do you load variables from a .env file in Bash?](#241-how-do-you-load-variables-from-a-env-file-in-bash)
- [242: What is ShellCheck?](#242-what-is-shellcheck)
- [243: How do you make set -x output more useful?](#243-how-do-you-make-set--x-output-more-useful)
- [244: How do you write a portable shell script?](#244-how-do-you-write-a-portable-shell-script)
- [245: Why use #!/usr/bin/env bash instead of #!/bin/bash?](#245-why-use-usrbinenv-bash-instead-of-binbash)
- [246: What are the common exit code conventions?](#246-what-are-the-common-exit-code-conventions)
- [247: How do you write a simple logging function for scripts?](#247-how-do-you-write-a-simple-logging-function-for-scripts)
- [248: How do you create temporary files safely?](#248-how-do-you-create-temporary-files-safely)
- [249: How do you stop two copies of a script from running at the same time?](#249-how-do-you-stop-two-copies-of-a-script-from-running-at-the-same-time)
- [250: How do you ask the user for confirmation?](#250-how-do-you-ask-the-user-for-confirmation)
- [251: How do you print colored output only when writing to a terminal?](#251-how-do-you-print-colored-output-only-when-writing-to-a-terminal)
- [252: How do you check if a script is running as root?](#252-how-do-you-check-if-a-script-is-running-as-root)
- [253: How do you get the directory a script is located in?](#253-how-do-you-get-the-directory-a-script-is-located-in)
- [254: How do you trim leading and trailing whitespace from a string?](#254-how-do-you-trim-leading-and-trailing-whitespace-from-a-string)
- [255: How do you loop over files safely?](#255-how-do-you-loop-over-files-safely)
- [256: What does the -- argument mean?](#256-what-does-the----argument-mean)
- [257: How do you find files by time, size and owner?](#257-how-do-you-find-files-by-time-size-and-owner)
- [258: How do you delete old files with find?](#258-how-do-you-delete-old-files-with-find)
- [259: How do you use xargs -I to place the argument in the middle of a command?](#259-how-do-you-use-xargs--i-to-place-the-argument-in-the-middle-of-a-command)
- [260: How do you work with JSON from the command line?](#260-how-do-you-work-with-json-from-the-command-line)
- [261: How do you send a JSON POST request with curl?](#261-how-do-you-send-a-json-post-request-with-curl)
- [262: How do you encode data and check file hashes?](#262-how-do-you-encode-data-and-check-file-hashes)
- [263: What do declare -i, -a, -A, -x and -p do?](#263-what-do-declare--i--a--a--x-and--p-do)
- [264: What is the difference between set and shopt?](#264-what-is-the-difference-between-set-and-shopt)
- [265: What is the difference between screen and tmux?](#265-what-is-the-difference-between-screen-and-tmux)
- [266: What is the /proc filesystem?](#266-what-is-the-proc-filesystem)
- [267: What is the format of /etc/passwd and /etc/shadow?](#267-what-is-the-format-of-etcpasswd-and-etcshadow)
- [268: How do you resolve the real path of a file?](#268-how-do-you-resolve-the-real-path-of-a-file)
- [269: How do you see disks and mount a filesystem?](#269-how-do-you-see-disks-and-mount-a-filesystem)
- [270: How do you add swap space?](#270-how-do-you-add-swap-space)
- [271: How do you use history expansion beyond !!?](#271-how-do-you-use-history-expansion-beyond-)
- [272: What does the fc command do?](#272-what-does-the-fc-command-do)
- [273: How do you read a password without showing it?](#273-how-do-you-read-a-password-without-showing-it)
- [274: How do you run a command on many servers?](#274-how-do-you-run-a-command-on-many-servers)
- [275: How do you use a while read loop with ssh without it stopping after the first line?](#275-how-do-you-use-a-while-read-loop-with-ssh-without-it-stopping-after-the-first-line)
- [276: What is noclobber?](#276-what-is-noclobber)
- [277: How do you write output to a file that needs root?](#277-how-do-you-write-output-to-a-file-that-needs-root)
- [278: How do you check which process uses a lot of CPU or memory?](#278-how-do-you-check-which-process-uses-a-lot-of-cpu-or-memory)
- [279: What is the load average?](#279-what-is-the-load-average)
- [280: How do you search and replace across many files?](#280-how-do-you-search-and-replace-across-many-files)
- [281: How do you compare two directories?](#281-how-do-you-compare-two-directories)
- [282: How do you create a patch and apply it?](#282-how-do-you-create-a-patch-and-apply-it)
- [283: What is the difference between source and running a script with bash?](#283-what-is-the-difference-between-source-and-running-a-script-with-bash)
- [284: What are the special parameters $$, $!, $_ and $-?](#284-what-are-the-special-parameters---_-and--)
- [285: How do you check if a string contains a substring?](#285-how-do-you-check-if-a-string-contains-a-substring)
- [286: How do you check if a value is a number?](#286-how-do-you-check-if-a-value-is-a-number)
- [287: How do you pass an array to a function?](#287-how-do-you-pass-an-array-to-a-function)
- [288: How do you create a retry loop for a flaky command?](#288-how-do-you-create-a-retry-loop-for-a-flaky-command)
- [289: What is the difference between printenv, env, set and declare?](#289-what-is-the-difference-between-printenv-env-set-and-declare)
- [290: How do you run a script with a clean environment?](#290-how-do-you-run-a-script-with-a-clean-environment)
- [291: How do you show a progress indicator in a script?](#291-how-do-you-show-a-progress-indicator-in-a-script)
- [292: How do you read only specific fields with read?](#292-how-do-you-read-only-specific-fields-with-read)
- [293: How do you add a date and time to every line of output?](#293-how-do-you-add-a-date-and-time-to-every-line-of-output)
- [294: How do you check SSL certificate details from the command line?](#294-how-do-you-check-ssl-certificate-details-from-the-command-line)
- [295: How do you manage packages with dpkg and rpm directly?](#295-how-do-you-manage-packages-with-dpkg-and-rpm-directly)
- [296: How do you set kernel parameters with sysctl?](#296-how-do-you-set-kernel-parameters-with-sysctl)
- [297: How do you look at kernel messages?](#297-how-do-you-look-at-kernel-messages)
- [298: How do you switch between Node, Python or other tool versions in a shell?](#298-how-do-you-switch-between-node-python-or-other-tool-versions-in-a-shell)
- [299: How do you tell if a command is slow because of CPU, disk or network?](#299-how-do-you-tell-if-a-command-is-slow-because-of-cpu-disk-or-network)
- [300: How do you write a simple health check script for a web service?](#300-how-do-you-write-a-simple-health-check-script-for-a-web-service)

### Advanced Questions (301-450)

- [301: In what order does Bash read its startup files?](#301-in-what-order-does-bash-read-its-startup-files)
- [302: How does Bash decide what to run when you type a command name?](#302-how-does-bash-decide-what-to-run-when-you-type-a-command-name)
- [303: In what order does Bash perform expansions?](#303-in-what-order-does-bash-perform-expansions)
- [304: How does word splitting work and when does it happen?](#304-how-does-word-splitting-work-and-when-does-it-happen)
- [305: Why is eval dangerous and what are the alternatives?](#305-why-is-eval-dangerous-and-what-are-the-alternatives)
- [306: How do you build a command with optional arguments safely?](#306-how-do-you-build-a-command-with-optional-arguments-safely)
- [307: How can a script become vulnerable to command injection?](#307-how-can-a-script-become-vulnerable-to-command-injection)
- [308: What is the fork and exec model and how does Bash use it?](#308-what-is-the-fork-and-exec-model-and-how-does-bash-use-it)
- [309: Why do variables set inside a piped while loop disappear?](#309-why-do-variables-set-inside-a-piped-while-loop-disappear)
- [310: How do ERR traps and set -E work together?](#310-how-do-err-traps-and-set--e-work-together)
- [311: What does inherit_errexit do?](#311-what-does-inherit_errexit-do)
- [312: How do you print a stack trace when a Bash script fails?](#312-how-do-you-print-a-stack-trace-when-a-bash-script-fails)
- [313: How do EXIT traps behave in subshells and with signals?](#313-how-do-exit-traps-behave-in-subshells-and-with-signals)
- [314: What happens to child processes when you press Ctrl+C?](#314-what-happens-to-child-processes-when-you-press-ctrlc)
- [315: What are process groups and sessions?](#315-what-are-process-groups-and-sessions)
- [316: What is the difference between nohup, disown and setsid?](#316-what-is-the-difference-between-nohup-disown-and-setsid)
- [317: What are zombie and orphan processes?](#317-what-are-zombie-and-orphan-processes)
- [318: Why do Docker containers often ignore SIGTERM, and how does exec help?](#318-why-do-docker-containers-often-ignore-sigterm-and-how-does-exec-help)
- [319: What does wait -n do?](#319-what-does-wait--n-do)
- [320: What is a coprocess in Bash?](#320-what-is-a-coprocess-in-bash)
- [321: What are named pipes and when do you use them?](#321-what-are-named-pipes-and-when-do-you-use-them)
- [322: How do you open and use custom file descriptors?](#322-how-do-you-open-and-use-custom-file-descriptors)
- [323: How do you swap stdout and stderr?](#323-how-do-you-swap-stdout-and-stderr)
- [324: Why does the order of redirections matter?](#324-why-does-the-order-of-redirections-matter)
- [325: What is /dev/tcp in Bash?](#325-what-is-devtcp-in-bash)
- [326: How do you write a file atomically?](#326-how-do-you-write-a-file-atomically)
- [327: What is a TOCTOU race and how does it apply to shell scripts?](#327-what-is-a-toctou-race-and-how-does-it-apply-to-shell-scripts)
- [328: How do you use flock to protect only part of a script?](#328-how-do-you-use-flock-to-protect-only-part-of-a-script)
- [329: What are namerefs and when are they useful?](#329-what-are-namerefs-and-when-are-they-useful)
- [330: What is dynamic scoping in Bash and how can it bite you?](#330-what-is-dynamic-scoping-in-bash-and-how-can-it-bite-you)
- [331: How do you export a function to child processes?](#331-how-do-you-export-a-function-to-child-processes)
- [332: What was Shellshock?](#332-what-was-shellshock)
- [333: How do ${var@Q} and printf %q help with quoting?](#333-how-do-varq-and-printf-q-help-with-quoting)
- [334: What is new in Bash 5.3?](#334-what-is-new-in-bash-53)
- [335: How does the new ${ command; } substitution differ from $( )?](#335-how-does-the-new--command--substitution-differ-from--)
- [336: How do you measure time precisely inside a script?](#336-how-do-you-measure-time-precisely-inside-a-script)
- [337: Why does set -u break on empty arrays in older Bash?](#337-why-does-set--u-break-on-empty-arrays-in-older-bash)
- [338: What arithmetic pitfalls exist in Bash?](#338-what-arithmetic-pitfalls-exist-in-bash)
- [339: Why can arithmetic on untrusted input be a security problem?](#339-why-can-arithmetic-on-untrusted-input-be-a-security-problem)
- [340: How does locale affect sort, grep and string comparison?](#340-how-does-locale-affect-sort-grep-and-string-comparison)
- [341: Why is a Bash while-read loop slow on large files, and what should you use instead?](#341-why-is-a-bash-while-read-loop-slow-on-large-files-and-what-should-you-use-instead)
- [342: How do you avoid unnecessary subshells and external commands in hot loops?](#342-how-do-you-avoid-unnecessary-subshells-and-external-commands-in-hot-loops)
- [343: How do you run a fixed number of parallel jobs in pure Bash?](#343-how-do-you-run-a-fixed-number-of-parallel-jobs-in-pure-bash)
- [344: How do you profile a slow Bash script?](#344-how-do-you-profile-a-slow-bash-script)
- [345: What does "Argument list too long" mean and how do you fix it?](#345-what-does-argument-list-too-long-mean-and-how-do-you-fix-it)
- [346: Can a Bash variable hold binary data or null bytes?](#346-can-a-bash-variable-hold-binary-data-or-null-bytes)
- [347: How do you keep trailing newlines in command substitution?](#347-how-do-you-keep-trailing-newlines-in-command-substitution)
- [348: How does ${#var} behave with multibyte characters?](#348-how-does-var-behave-with-multibyte-characters)
- [349: Why do scripts with Windows line endings fail and how do you fix them?](#349-why-do-scripts-with-windows-line-endings-fail-and-how-do-you-fix-them)
- [350: How do you tell if a script is running interactively or with a terminal?](#350-how-do-you-tell-if-a-script-is-running-interactively-or-with-a-terminal)
- [351: Why does a script with set -o pipefail sometimes fail with exit code 141?](#351-why-does-a-script-with-set--o-pipefail-sometimes-fail-with-exit-code-141)
- [352: What do exit codes 126 and 127 tell you?](#352-what-do-exit-codes-126-and-127-tell-you)
- [353: Why are aliases not expanded in scripts and functions?](#353-why-are-aliases-not-expanded-in-scripts-and-functions)
- [354: How can CDPATH break scripts?](#354-how-can-cdpath-break-scripts)
- [355: How does sudo handle the environment and PATH?](#355-how-does-sudo-handle-the-environment-and-path)
- [356: Why are setuid shell scripts ignored on Linux?](#356-why-are-setuid-shell-scripts-ignored-on-linux)
- [357: How can PATH hijacking happen and how do you prevent it in scripts?](#357-how-can-path-hijacking-happen-and-how-do-you-prevent-it-in-scripts)
- [358: How do secrets leak in shell usage and how do you avoid it?](#358-how-do-secrets-leak-in-shell-usage-and-how-do-you-avoid-it)
- [359: What are the risks of SSH agent forwarding?](#359-what-are-the-risks-of-ssh-agent-forwarding)
- [360: How do you harden SSH on a server?](#360-how-do-you-harden-ssh-on-a-server)
- [361: Why does SSH refuse to use a private key with "bad permissions"?](#361-why-does-ssh-refuse-to-use-a-private-key-with-bad-permissions)
- [362: How can symlink attacks happen in /tmp?](#362-how-can-symlink-attacks-happen-in-tmp)
- [363: What is an inode and what does it store?](#363-what-is-an-inode-and-what-does-it-store)
- [364: What are the three timestamps of a file?](#364-what-are-the-three-timestamps-of-a-file)
- [365: How do mount options like noexec, nosuid and nodev help security?](#365-how-do-mount-options-like-noexec-nosuid-and-nodev-help-security)
- [366: What are Linux capabilities?](#366-what-are-linux-capabilities)
- [367: What are cgroups and namespaces?](#367-what-are-cgroups-and-namespaces)
- [368: What does the OOM killer do and how do you investigate it?](#368-what-does-the-oom-killer-do-and-how-do-you-investigate-it)
- [369: How do you read the output of free and what is buff/cache?](#369-how-do-you-read-the-output-of-free-and-what-is-buffcache)
- [370: What is swappiness?](#370-what-is-swappiness)
- [371: How do you use vmstat and iostat to find bottlenecks?](#371-how-do-you-use-vmstat-and-iostat-to-find-bottlenecks)
- [372: How do you check open file descriptor usage and limits?](#372-how-do-you-check-open-file-descriptor-usage-and-limits)
- [373: How do you find which process is using a port and why the port stays busy after a restart?](#373-how-do-you-find-which-process-is-using-a-port-and-why-the-port-stays-busy-after-a-restart)
- [374: How do systemd unit dependencies work?](#374-how-do-systemd-unit-dependencies-work)
- [375: What are the systemd service types and when do you use each?](#375-what-are-the-systemd-service-types-and-when-do-you-use-each)
- [376: How do you configure restart behavior and avoid restart loops in systemd?](#376-how-do-you-configure-restart-behavior-and-avoid-restart-loops-in-systemd)
- [377: How do you harden a systemd service?](#377-how-do-you-harden-a-systemd-service)
- [378: What is socket activation?](#378-what-is-socket-activation)
- [379: What happens during the Linux boot process?](#379-what-happens-during-the-linux-boot-process)
- [380: How do runlevels relate to systemd targets?](#380-how-do-runlevels-relate-to-systemd-targets)
- [381: How do you watch for file changes from a script?](#381-how-do-you-watch-for-file-changes-from-a-script)
- [382: What is the difference between copytruncate and create in logrotate?](#382-what-is-the-difference-between-copytruncate-and-create-in-logrotate)
- [383: How do you use rsync --delete safely?](#383-how-do-you-use-rsync---delete-safely)
- [384: What does it mean for a script to be idempotent and how do you write one?](#384-what-does-it-mean-for-a-script-to-be-idempotent-and-how-do-you-write-one)
- [385: How would you structure a safe deploy script with releases and rollback?](#385-how-would-you-structure-a-safe-deploy-script-with-releases-and-rollback)
- [386: How do you parse long options without getopt?](#386-how-do-you-parse-long-options-without-getopt)
- [387: What is the difference between getopt and getopts?](#387-what-is-the-difference-between-getopt-and-getopts)
- [388: How do you read a config file without using source?](#388-how-do-you-read-a-config-file-without-using-source)
- [389: How do you test Bash scripts?](#389-how-do-you-test-bash-scripts)
- [390: What are the most common ShellCheck warnings and what do they mean?](#390-what-are-the-most-common-shellcheck-warnings-and-what-do-they-mean)
- [391: What are the main differences between Dash and Bash that break scripts?](#391-what-are-the-main-differences-between-dash-and-bash-that-break-scripts)
- [392: What should you know about Bash on macOS?](#392-what-should-you-know-about-bash-on-macos)
- [393: How do you run a block of commands with sudo, including redirects and variables?](#393-how-do-you-run-a-block-of-commands-with-sudo-including-redirects-and-variables)
- [394: How does the shell handle a background job's stdin in scripts?](#394-how-does-the-shell-handle-a-background-jobs-stdin-in-scripts)
- [395: Why can you not simply pipe a password into sudo or ssh?](#395-why-can-you-not-simply-pipe-a-password-into-sudo-or-ssh)
- [396: How do you handle cleanup of child processes when a script exits?](#396-how-do-you-handle-cleanup-of-child-processes-when-a-script-exits)
- [397: How do you write a function that works with both piped input and arguments?](#397-how-do-you-write-a-function-that-works-with-both-piped-input-and-arguments)
- [398: How do you safely loop over the output of find and change variables in the loop?](#398-how-do-you-safely-loop-over-the-output-of-find-and-change-variables-in-the-loop)
- [399: What is the difference between $(< file) and $(cat file)?](#399-what-is-the-difference-between--file-and-cat-file)
- [400: How does Bash handle a script file that changes while it is running?](#400-how-does-bash-handle-a-script-file-that-changes-while-it-is-running)
- [401: A server's disk is suddenly full. How do you investigate?](#401-a-servers-disk-is-suddenly-full-how-do-you-investigate)
- [402: A server has very high CPU usage. What steps do you take?](#402-a-server-has-very-high-cpu-usage-what-steps-do-you-take)
- [403: An app says "Connection refused" when calling another service. How do you debug it?](#403-an-app-says-connection-refused-when-calling-another-service-how-do-you-debug-it)
- [404: You cannot SSH into a server anymore. What could be wrong?](#404-you-cannot-ssh-into-a-server-anymore-what-could-be-wrong)
- [405: A script works when you run it by hand but fails under systemd. Why?](#405-a-script-works-when-you-run-it-by-hand-but-fails-under-systemd-why)
- [406: How would you find out why a process is stuck?](#406-how-would-you-find-out-why-a-process-is-stuck)
- [407: How do you handle signals correctly in a long-running Bash worker loop?](#407-how-do-you-handle-signals-correctly-in-a-long-running-bash-worker-loop)
- [408: How do you write a reliable lock using mkdir?](#408-how-do-you-write-a-reliable-lock-using-mkdir)
- [409: How do you safely remove a directory given in a variable?](#409-how-do-you-safely-remove-a-directory-given-in-a-variable)
- [410: What happens with exit status and set -e when a command substitution fails inside another command?](#410-what-happens-with-exit-status-and-set--e-when-a-command-substitution-fails-inside-another-command)
- [411: How do you make a Bash script safe to run with untrusted file names?](#411-how-do-you-make-a-bash-script-safe-to-run-with-untrusted-file-names)
- [412: Why is parsing ls output a bad idea?](#412-why-is-parsing-ls-output-a-bad-idea)
- [413: How do you compare versions in a script?](#413-how-do-you-compare-versions-in-a-script)
- [414: How do you make sure a script's output is not mixed up when several processes log to the same file?](#414-how-do-you-make-sure-a-scripts-output-is-not-mixed-up-when-several-processes-log-to-the-same-file)
- [415: How do you send script output to syslog or the journal?](#415-how-do-you-send-script-output-to-syslog-or-the-journal)
- [416: What is the difference between buffered and unbuffered output and why does it matter in pipes?](#416-what-is-the-difference-between-buffered-and-unbuffered-output-and-why-does-it-matter-in-pipes)
- [417: How does tail -f behave with log rotation, and when do you need -F?](#417-how-does-tail--f-behave-with-log-rotation-and-when-do-you-need--f)
- [418: How do you process a large log file quickly to answer "how many 5xx errors per minute"?](#418-how-do-you-process-a-large-log-file-quickly-to-answer-how-many-5xx-errors-per-minute)
- [419: How do you find which files changed recently on a system, for example after an incident?](#419-how-do-you-find-which-files-changed-recently-on-a-system-for-example-after-an-incident)
- [420: How do you safely run a remote script like curl | bash?](#420-how-do-you-safely-run-a-remote-script-like-curl--bash)
- [421: What is the difference between a subshell and a child process?](#421-what-is-the-difference-between-a-subshell-and-a-child-process)
- [422: How do you use mapfile with a delimiter and a callback?](#422-how-do-you-use-mapfile-with-a-delimiter-and-a-callback)
- [423: What are ;& and ;;& in a case statement?](#423-what-are--and--in-a-case-statement)
- [424: How does printf -v help, and how does printf reuse its format?](#424-how-does-printf--v-help-and-how-does-printf-reuse-its-format)
- [425: How do you implement a timeout for a Bash function, not an external command?](#425-how-do-you-implement-a-timeout-for-a-bash-function-not-an-external-command)
- [426: How does Readline configuration work and what is ~/.inputrc?](#426-how-does-readline-configuration-work-and-what-is-inputrc)
- [427: How does programmable completion work in Bash?](#427-how-does-programmable-completion-work-in-bash)
- [428: What is a restricted shell?](#428-what-is-a-restricted-shell)
- [429: How do you force a specific command for an SSH key?](#429-how-do-you-force-a-specific-command-for-an-ssh-key)
- [430: What are common Bash patterns that look correct but have subtle bugs?](#430-what-are-common-bash-patterns-that-look-correct-but-have-subtle-bugs)
- [431: How does Bash handle errors inside a pipeline with set -e and pipefail?](#431-how-does-bash-handle-errors-inside-a-pipeline-with-set--e-and-pipefail)
- [432: How do you handle a script that needs to work with both GNU and BSD tools?](#432-how-do-you-handle-a-script-that-needs-to-work-with-both-gnu-and-bsd-tools)
- [433: What are good conventions for structuring a larger Bash script?](#433-what-are-good-conventions-for-structuring-a-larger-bash-script)
- [434: When should you not use Bash?](#434-when-should-you-not-use-bash)
- [435: How do you trace which files a script reads and which commands it runs?](#435-how-do-you-trace-which-files-a-script-reads-and-which-commands-it-runs)
- [436: How do you manage environment and configuration differences between dev, staging and prod in shell scripts?](#436-how-do-you-manage-environment-and-configuration-differences-between-dev-staging-and-prod-in-shell-scripts)
- [437: What is the difference between kill -0, kill -STOP and kill -CONT?](#437-what-is-the-difference-between-kill--0-kill--stop-and-kill--cont)
- [438: How do you safely handle PIDs to avoid killing the wrong process?](#438-how-do-you-safely-handle-pids-to-avoid-killing-the-wrong-process)
- [439: What is the difference between a hard and soft resource limit?](#439-what-is-the-difference-between-a-hard-and-soft-resource-limit)
- [440: How do you limit the CPU and memory of a single command?](#440-how-do-you-limit-the-cpu-and-memory-of-a-single-command)
- [441: What is LD_PRELOAD and why is it a security concern?](#441-what-is-ld_preload-and-why-is-it-a-security-concern)
- [442: How do you check what shared libraries a binary needs?](#442-how-do-you-check-what-shared-libraries-a-binary-needs)
- [443: How would you set up log rotation for an app that writes to stdout under systemd?](#443-how-would-you-set-up-log-rotation-for-an-app-that-writes-to-stdout-under-systemd)
- [444: How do you write a Bash script that handles both SIGTERM graceful shutdown and a forced timeout?](#444-how-do-you-write-a-bash-script-that-handles-both-sigterm-graceful-shutdown-and-a-forced-timeout)
- [445: What are the trade-offs of using set -e at all?](#445-what-are-the-trade-offs-of-using-set--e-at-all)
- [446: How do you run commands in a clean, reproducible container shell for debugging?](#446-how-do-you-run-commands-in-a-clean-reproducible-container-shell-for-debugging)
- [447: How does nsenter help with debugging containers?](#447-how-does-nsenter-help-with-debugging-containers)
- [448: How do you capture network traffic for debugging from the shell?](#448-how-do-you-capture-network-traffic-for-debugging-from-the-shell)
- [449: How do you investigate high memory usage of a process?](#449-how-do-you-investigate-high-memory-usage-of-a-process)
- [450: You inherit a 1,000-line Bash deploy script with no tests. How do you make it safer to change?](#450-you-inherit-a-1000-line-bash-deploy-script-with-no-tests-how-do-you-make-it-safer-to-change)

---

# Easy Questions (1-150)

## 1: What is Linux?

Linux is an open source operating system kernel, first written by Linus Torvalds in 1991. The kernel is the part that talks to the hardware, manages memory and processes, and handles files and networking.

When people say "Linux" they usually mean a full system: the Linux kernel plus GNU tools, a shell, a package manager and other software. Most web servers, containers and cloud machines run Linux.

## 2: What is a Linux distribution?

A distribution (or distro) is a complete operating system built around the Linux kernel. It bundles the kernel, system tools, a package manager, default configuration and often a desktop.

Common ones:

- Ubuntu and Debian (use `apt` and `.deb` packages)
- Fedora, RHEL, Rocky Linux and AlmaLinux (use `dnf` and `.rpm` packages)
- Arch Linux (uses `pacman`)
- Alpine Linux (very small, uses `apk`, popular in Docker images)

## 3: What is a shell?

A shell is a program that reads commands from you (or from a script) and runs them. It sits between you and the operating system. You type `ls`, the shell finds the `ls` program, starts it and shows you the output.

Popular shells are Bash, Zsh, Fish, Dash and the original Bourne shell (`sh`).

## 4: What is Bash?

Bash stands for "Bourne Again SHell". It is the GNU project's shell and was released in 1989 as a free replacement for the Bourne shell. It is the default login shell on many Linux distributions and is the most common language for shell scripts.

Bash works both as an interactive shell (you type commands) and as a scripting language (with variables, loops, functions and so on).

## 5: What is the difference between sh and bash?

`sh` is the POSIX shell standard. On most systems `/bin/sh` is a link to a small POSIX shell (Dash on Debian and Ubuntu) or to Bash running in POSIX mode.

Bash supports everything `sh` does and adds extra features like arrays, `[[ ]]`, `(( ))`, brace expansion, `local`, process substitution and more. A script that uses these features must run with Bash, not `sh`.

```bash
# works in bash, fails in dash
arr=(one two three)
echo "${arr[1]}"
```

## 6: How do you check which shell you are using?

```bash
echo "$SHELL"     # your login shell from /etc/passwd
echo "$0"         # the shell running right now
ps -p $$          # the process of the current shell
echo "$BASH_VERSION"
```

`$SHELL` shows your default login shell, which might not be the shell you are currently in. `$0` or `ps -p $$` shows the actual running shell.

## 7: What is the difference between a terminal and a shell?

The terminal (or terminal emulator) is the window program that shows text and takes keyboard input, for example GNOME Terminal, iTerm2 or Windows Terminal. The shell is the program running inside it that understands your commands.

You can run different shells in the same terminal, and the same shell in different terminals.

## 8: What is a shebang line?

The shebang is the first line of a script that starts with `#!`. It tells the kernel which program should run the file.

```bash
#!/usr/bin/env bash
echo "Hello"
```

`#!/usr/bin/env bash` finds `bash` in your `PATH`, which works on more systems than a hard-coded `#!/bin/bash`. Without a shebang, the file is run by whatever shell you call it from, which can give different results.

## 9: How do you run a shell script?

There are a few ways:

```bash
chmod +x script.sh   # make it executable once
./script.sh          # run it, uses the shebang

bash script.sh       # run it with bash directly, no execute permission needed

source script.sh     # run it in the current shell
. script.sh          # same as source
```

The first two start a new process. `source` runs the commands in your current shell, so any variables or `cd` in the script affect your session.

## 10: Why do you need ./ to run a script in the current directory?

The shell looks for commands only in the directories listed in `PATH`. The current directory is usually not in `PATH` for safety reasons. So `script.sh` gives "command not found", while `./script.sh` gives an explicit path to the file.

## 11: What does the Linux filesystem hierarchy look like?

Everything starts at the root directory `/`. Common directories:

| Directory            | What it holds                                |
| -------------------- | -------------------------------------------- |
| `/bin`, `/usr/bin`   | User commands                                |
| `/sbin`, `/usr/sbin` | System admin commands                        |
| `/etc`               | Configuration files                          |
| `/home`              | User home directories                        |
| `/root`              | Home of the root user                        |
| `/var`               | Changing data: logs, caches, mail, databases |
| `/tmp`               | Temporary files                              |
| `/usr`               | Installed programs and libraries             |
| `/opt`               | Optional third-party software                |
| `/dev`               | Device files                                 |
| `/proc`, `/sys`      | Virtual files with kernel and process info   |
| `/boot`              | Kernel and bootloader files                  |

On many modern distros `/bin` is just a link to `/usr/bin`.

## 12: What is the difference between an absolute and a relative path?

An absolute path starts from the root `/` and works no matter where you are, for example `/home/anna/projects/app`.

A relative path starts from your current directory, for example `projects/app` or `../logs`. Special names:

- `.` is the current directory
- `..` is the parent directory
- `~` is your home directory

## 13: How do you see the current directory and move between directories?

```bash
pwd              # print working directory
cd /var/log      # go to an absolute path
cd ..            # go up one level
cd               # go to home directory
cd ~             # same
cd -             # go back to the previous directory
```

## 14: How do you list files with ls?

```bash
ls               # list files in current directory
ls -l            # long format: permissions, owner, size, date
ls -a            # include hidden files (starting with .)
ls -lh           # human readable sizes (K, M, G)
ls -lt           # sort by modification time, newest first
ls -lS           # sort by size, biggest first
ls -R            # list subdirectories too
ls -ld dir       # show info about the directory itself
```

## 15: What are hidden files in Linux?

Any file or directory whose name starts with a dot is hidden, for example `.bashrc`, `.git` or `.env`. They are not shown by `ls` or matched by `*` by default. Use `ls -a` to see them. There is no special "hidden" attribute; it is only a naming rule.

## 16: How do you create files and directories?

```bash
touch notes.txt              # create an empty file (or update its timestamp)
mkdir logs                   # create a directory
mkdir -p app/src/utils       # create nested directories, no error if they exist
```

`mkdir -p` is the one you usually want in scripts because it does not fail if the directory is already there.

## 17: How do you copy files and directories?

```bash
cp file.txt backup.txt         # copy a file
cp file.txt /tmp/              # copy into a directory
cp -r src/ src-backup/         # copy a directory recursively
cp -i file.txt dest.txt        # ask before overwriting
cp -a src/ dest/               # archive mode: keep permissions, times, links
```

## 18: How do you move or rename files?

`mv` does both. If the target is a directory, the file is moved into it. Otherwise it is renamed.

```bash
mv old.txt new.txt         # rename
mv report.pdf ~/Documents/ # move
mv -i a.txt b.txt          # ask before overwriting
mv -n a.txt b.txt          # never overwrite
```

## 19: How do you delete files and directories?

```bash
rm file.txt            # delete a file
rm -i *.log            # ask before each delete
rmdir emptydir         # delete an empty directory
rm -r dir/             # delete a directory and everything in it
rm -rf dir/            # same, without prompts or errors for missing files
```

There is no trash bin on the command line. `rm -rf` is permanent, so double check the path, especially when it contains variables.

## 20: How do you view the contents of a file?

```bash
cat file.txt         # print the whole file
less file.txt        # scroll through it (q to quit, / to search)
head file.txt        # first 10 lines
head -n 20 file.txt  # first 20 lines
tail file.txt        # last 10 lines
tail -n 50 file.txt  # last 50 lines
```

Use `less` for big files. `cat` on a huge file just floods your terminal.

## 21: What does tail -f do?

`tail -f` prints the end of a file and keeps the file open, printing new lines as they are added. It is the usual way to watch a log file live.

```bash
tail -f /var/log/nginx/access.log
tail -F app.log    # also follows the file if it gets rotated or recreated
```

Press `Ctrl+C` to stop.

## 22: What is the difference between echo and printf?

`echo` prints its arguments followed by a newline. It is simple but its handling of options like `-e` and `-n` differs between shells.

`printf` works like C's `printf`. It does not add a newline unless you ask for one and gives you full control over formatting. It is more portable, so prefer it in scripts.

```bash
echo "Hello $USER"
printf "Hello %s\n" "$USER"
printf "%-10s %5d\n" "apples" 42
```

## 23: How do you get help for a command?

```bash
man ls          # full manual page
ls --help       # short help for most GNU tools
help cd         # help for bash builtins
type cd         # tells you if it is a builtin, alias, function or file
info coreutils  # GNU info docs
```

`man -k keyword` (or `apropos keyword`) searches man pages by keyword.

## 24: What is the difference between type and which?

`which` only searches `PATH` for executable files. `type` is a Bash builtin that knows about everything the shell can run: aliases, functions, keywords, builtins and files.

```bash
$ type ls
ls is aliased to `ls --color=auto'
$ which ls
/usr/bin/ls
$ type -a echo
echo is a shell builtin
echo is /usr/bin/echo
```

In scripts, use `command -v name` to check if a command exists.

## 25: What is the history command?

`history` shows the commands you have typed before, with numbers. Bash saves them in `~/.bash_history` when the shell exits.

```bash
history          # show all
history 20       # last 20
!42              # run command number 42 again
!!               # run the last command again
sudo !!          # run the last command again with sudo
```

`Ctrl+R` lets you search history as you type.

## 26: What are some useful Bash keyboard shortcuts?

| Shortcut            | Action                                                     |
| ------------------- | ---------------------------------------------------------- |
| `Tab`               | Auto-complete commands and file names                      |
| `Ctrl+C`            | Stop the running command                                   |
| `Ctrl+Z`            | Pause the running command (send it to background, stopped) |
| `Ctrl+D`            | End of input; exits the shell on an empty line             |
| `Ctrl+L`            | Clear the screen                                           |
| `Ctrl+R`            | Search command history                                     |
| `Ctrl+A` / `Ctrl+E` | Go to start / end of line                                  |
| `Ctrl+U` / `Ctrl+K` | Delete to start / end of line                              |
| `Ctrl+W`            | Delete the word before the cursor                          |
| `Alt+.`             | Insert the last argument of the previous command           |

## 27: What are wildcards (globs)?

Wildcards are special characters the shell expands into matching file names before running the command.

- `*` matches any number of characters
- `?` matches exactly one character
- `[abc]` matches one of the listed characters
- `[a-z]` matches a range
- `[!abc]` or `[^abc]` matches anything except those

```bash
ls *.txt          # all .txt files
ls file?.log      # file1.log, fileA.log, ...
rm report[0-9].csv
```

If nothing matches, Bash leaves the pattern as-is by default.

## 28: How do you create and use a variable in Bash?

```bash
name="Anna"
count=5
echo "$name has $count apples"
echo "${name}_backup"    # braces separate the name from text after it
```

There must be no spaces around `=`. `name = "Anna"` tries to run a command called `name`. Variable names are case sensitive.

## 29: What is the difference between single and double quotes?

Single quotes keep everything literally. No variables or commands are expanded.

Double quotes keep spaces together but still expand `$variables`, `$(commands)` and `\` escapes for a few characters.

```bash
name="Anna"
echo 'Hello $name'    # Hello $name
echo "Hello $name"    # Hello Anna
```

You cannot put a single quote inside single quotes. Use `'It'\''s'` or `"It's"`.

## 30: Why should you quote variables?

Without quotes, Bash splits the value of a variable on spaces and expands any wildcards in it. That breaks file names with spaces and can even cause wrong files to be deleted.

```bash
file="my report.txt"
rm $file      # tries to delete "my" and "report.txt"
rm "$file"    # deletes "my report.txt"
```

A good rule: always put variables in double quotes unless you have a reason not to.

## 31: What are environment variables?

Environment variables are named values passed from a process to the programs it starts. Programs read them for configuration. Common ones:

- `HOME` your home directory
- `USER` your user name
- `PATH` where to look for commands
- `PWD` current directory
- `SHELL` your login shell
- `LANG` language and encoding

```bash
printenv          # list all environment variables
echo "$HOME"
```

## 32: What does export do?

A normal shell variable is only visible in the current shell. `export` marks it as an environment variable, so child processes (scripts and programs you start) can see it too.

```bash
API_URL="http://localhost:3000"
bash -c 'echo $API_URL'     # prints nothing

export API_URL
bash -c 'echo $API_URL'     # prints http://localhost:3000

export NODE_ENV=production  # define and export in one step
```

## 33: What is the PATH variable?

`PATH` is a list of directories separated by colons. When you type a command, the shell checks those directories in order and runs the first match.

```bash
echo "$PATH"
# /usr/local/bin:/usr/bin:/bin

export PATH="$HOME/.local/bin:$PATH"   # add a directory in front
```

Put this line in `~/.bashrc` to make it permanent.

## 34: How do you set a variable for a single command only?

Write the assignment right before the command. It is set only for that command's environment.

```bash
NODE_ENV=production node server.js
LANG=C sort file.txt
DEBUG=1 PORT=8080 ./start.sh
```

Your current shell is not changed.

## 35: What is an exit code?

Every command returns a number when it finishes. `0` means success. Anything from `1` to `255` means some kind of failure. The exit code of the last command is in `$?`.

```bash
ls /etc > /dev/null
echo $?    # 0

ls /nope
echo $?    # 2 (ls uses 2 for serious errors)
```

Scripts use `exit 1` (or another number) to report failure.

## 36: What do &&, || and ; do between commands?

- `a ; b` runs `a`, then `b`, no matter what.
- `a && b` runs `b` only if `a` succeeded.
- `a || b` runs `b` only if `a` failed.

```bash
mkdir build && cd build
cd /app || exit 1
npm test && echo "Tests passed" || echo "Tests failed"
```

The last line is a common shortcut but has a catch: if `echo "Tests passed"` itself fails, the `||` part also runs. Use `if` for anything important.

## 37: What is a pipe?

A pipe `|` sends the output (stdout) of one command into the input (stdin) of the next. It lets you chain small tools together.

```bash
ls -l | less
cat access.log | grep 404 | wc -l
ps aux | grep node
```

Both sides run at the same time, and data flows as it is produced.

## 38: What are stdin, stdout and stderr?

Every process starts with three open streams, called file descriptors:

| Number | Name                     | Default  |
| ------ | ------------------------ | -------- |
| 0      | stdin (standard input)   | keyboard |
| 1      | stdout (standard output) | terminal |
| 2      | stderr (standard error)  | terminal |

Normal output goes to stdout and error messages go to stderr. Keeping them separate means you can save output to a file and still see errors on screen.

## 39: How does output redirection work?

```bash
command > out.txt      # stdout to file, overwrite
command >> out.txt     # stdout to file, append
command 2> err.txt     # stderr to file
command > all.txt 2>&1 # stdout and stderr to the same file
command &> all.txt     # same, bash shortcut
command &>> all.txt    # append both, bash shortcut
command < input.txt    # read stdin from file
```

## 40: What is /dev/null?

`/dev/null` is a special file that throws away everything written to it. Reading from it returns end of file right away. It is used to hide output you do not care about.

```bash
grep -q "error" app.log 2>/dev/null
command > /dev/null 2>&1   # silence everything
```

## 41: How do you search text in files with grep?

```bash
grep "error" app.log          # lines containing error
grep -i "error" app.log       # case insensitive
grep -n "error" app.log       # show line numbers
grep -r "TODO" src/           # search all files under src
grep -v "debug" app.log       # lines that do NOT match
grep -c "error" app.log       # count matching lines
grep -l "import" *.js         # only file names that match
grep -w "log" file.txt        # match whole words only
```

## 42: How do you find files with find?

```bash
find . -name "*.js"                 # by name, case sensitive
find . -iname "readme*"             # by name, case insensitive
find /var/log -type f -name "*.log" # only regular files
find . -type d -name node_modules   # only directories
find . -size +100M                  # bigger than 100 MB
find . -mtime -1                    # changed in the last 24 hours
```

The first argument is where to start. Then come the tests. `find` searches all subdirectories by default.

## 43: How do you count lines, words and characters?

`wc` (word count) does this.

```bash
wc file.txt       # lines, words, bytes
wc -l file.txt    # only lines
wc -w file.txt    # only words
wc -c file.txt    # only bytes
wc -m file.txt    # characters (differs from bytes for UTF-8)
ls | wc -l        # count files in a directory
```

## 44: How do you sort lines?

```bash
sort names.txt          # alphabetical
sort -r names.txt       # reverse
sort -n numbers.txt     # numeric (so 10 comes after 9)
sort -u names.txt       # sort and remove duplicates
sort -h sizes.txt       # human sizes like 2K, 1G
```

Without `-n`, `sort` compares text, so `100` comes before `20`.

## 45: What does uniq do?

`uniq` removes repeated lines that are next to each other. It does not see duplicates that are spread out, so you almost always sort first.

```bash
sort names.txt | uniq        # unique lines
sort names.txt | uniq -c     # count each line
sort names.txt | uniq -d     # only lines that appear more than once
```

## 46: How do you cut columns out of text?

`cut` picks fields by a delimiter or characters by position.

```bash
cut -d ':' -f 1 /etc/passwd      # user names
cut -d ',' -f 2,4 data.csv       # 2nd and 4th columns
cut -c 1-10 file.txt             # first 10 characters of each line
```

`cut` uses exactly one character as delimiter and does not merge repeated spaces. For space-separated output, `awk '{print $2}'` usually works better.

## 47: What does the tr command do?

`tr` replaces or deletes characters from stdin.

```bash
echo "hello" | tr 'a-z' 'A-Z'     # HELLO
echo "a,b,c" | tr ',' '\n'        # one item per line
echo "hello   world" | tr -s ' '  # squeeze repeated spaces
echo "abc123" | tr -d '0-9'       # delete digits
```

`tr` only reads from stdin. It does not take file names.

## 48: What are users and groups in Linux?

Every process and file belongs to a user and a group. Users have an ID (UID), and groups have an ID (GID). A user can belong to several groups.

```bash
whoami        # your user name
id            # your UID, GID and groups
groups        # groups you are in
cat /etc/passwd   # list of users
cat /etc/group    # list of groups
```

Groups make it easy to give several users the same access, for example the `docker` or `sudo` group.

## 49: Who is the root user?

`root` is the superuser with UID 0. It can read and change any file, kill any process and change system settings. Working as root all the time is risky because one typo can break the system. The usual way is to use a normal account and run single commands with `sudo`.

## 50: What is the difference between sudo and su?

`sudo` runs one command as another user (root by default) and asks for your own password. What you are allowed to do is set in `/etc/sudoers`, and every use is logged.

`su` switches to another user's shell and asks for that user's password.

```bash
sudo apt update          # one command as root
sudo -i                  # open a root login shell
su - postgres            # switch to the postgres user
sudo -u postgres psql    # run one command as postgres
```

## 51: How do Linux file permissions work?

Each file has three sets of permissions: for the owner (user), the group, and everyone else (others). Each set has three bits:

- `r` read
- `w` write
- `x` execute (for directories: allowed to enter it)

```bash
$ ls -l script.sh
-rwxr-x--- 1 anna devs 120 Mar 1 10:00 script.sh
```

Here the owner can read, write and run it, the `devs` group can read and run it, and others have no access. The first character is the file type: `-` file, `d` directory, `l` link.

## 52: How do you change permissions with chmod?

You can use letters or numbers.

```bash
chmod +x script.sh        # add execute for everyone
chmod u+x script.sh       # add execute for the owner only
chmod g-w file.txt        # remove write from group
chmod o= file.txt         # remove all permissions from others
chmod -R u+rwX dir/       # recursive; X adds execute only to directories
```

## 53: What do numeric permissions like 755 and 644 mean?

Each digit is the sum of read (4), write (2) and execute (1), for owner, group and others in that order.

| Number | Meaning                                       |
| ------ | --------------------------------------------- |
| 755    | `rwxr-xr-x` owner full, others read and run   |
| 644    | `rw-r--r--` owner read/write, others read     |
| 600    | `rw-------` only the owner can read and write |
| 700    | `rwx------` only the owner, with execute      |

```bash
chmod 644 index.html
chmod 600 ~/.ssh/id_ed25519
```

## 54: How do you change the owner of a file?

```bash
sudo chown anna file.txt          # change owner
sudo chown anna:devs file.txt     # change owner and group
sudo chown :devs file.txt         # change only group
sudo chgrp devs file.txt          # same, with chgrp
sudo chown -R www-data:www-data /var/www/app
```

Only root can give a file away to another user.

## 55: How do you see running processes?

```bash
ps            # processes in your current terminal
ps aux        # all processes with user, CPU, memory
ps -ef        # all processes, another format
top           # live view, press q to quit
htop          # nicer live view (if installed)
pgrep -a node # find processes by name
```

## 56: What is a PID?

PID is the process ID, a unique number the kernel gives each running process. You use it to send signals, check status or look in `/proc/<PID>`. PID 1 is the first process started by the kernel, usually `systemd`. `$$` holds the PID of the current shell and `$!` holds the PID of the last background command.

## 57: How do you stop a process with kill?

`kill` sends a signal to a process by PID.

```bash
kill 1234        # send SIGTERM (15), ask nicely to stop
kill -9 1234     # send SIGKILL, force stop right away
kill -l          # list all signals
pkill node       # kill by name
killall node     # kill all processes with this name
```

Try a normal `kill` first. `kill -9` gives the process no chance to clean up.

## 58: How do you run a command in the background?

Add `&` at the end. The shell gives you the prompt back right away.

```bash
npm run build &
jobs          # list background jobs
fg %1         # bring job 1 to the foreground
bg %1         # resume a stopped job in the background
```

If you already started something, press `Ctrl+Z` to stop it, then `bg` to continue it in the background.

## 59: What does nohup do?

`nohup` runs a command so it keeps going after you log out or close the terminal. It ignores the hangup signal (SIGHUP) that is sent when the terminal closes. Output goes to `nohup.out` unless you redirect it.

```bash
nohup ./long-task.sh > task.log 2>&1 &
```

For real services, use systemd instead. For interactive work that must survive a disconnect, `tmux` or `screen` are better.

## 60: How do you check disk space?

```bash
df -h            # free and used space per filesystem
df -h /var       # for the filesystem that holds /var
du -sh dir/      # total size of a directory
du -sh *         # size of each item in the current directory
du -h --max-depth=1 /var | sort -h
```

`df` looks at filesystems. `du` adds up file sizes.

## 61: How do you check memory usage?

```bash
free -h          # total, used, free, buff/cache, available
top              # live memory and CPU per process
cat /proc/meminfo
```

Look at the `available` column in `free`. Linux uses free RAM for disk cache, so `free` looking low is normal. `available` tells you how much programs can still use.

## 62: How do you get basic system information?

```bash
uname -a            # kernel name, version, architecture
uname -r            # kernel version only
cat /etc/os-release # distribution name and version
hostname            # machine name
uptime              # how long it has been running, load average
lscpu               # CPU info
nproc               # number of CPUs
```

## 63: How do you show the current date and time?

```bash
date                         # Tue Oct 29 10:15:00 UTC 2026
date +%Y-%m-%d               # 2026-10-29
date +"%Y-%m-%d %H:%M:%S"    # 2026-10-29 10:15:00
date +%s                     # Unix timestamp in seconds
date -u                      # in UTC
```

A common use in scripts: `backup="db-$(date +%F).sql"`. `%F` is the same as `%Y-%m-%d`.

## 64: What is the difference between a hard link and a symbolic link?

A symbolic (soft) link is a small file that points to a path. If the target is deleted, the link breaks. It can point to directories and across filesystems.

A hard link is another name for the same data (the same inode). The data stays until all hard links are deleted. Hard links cannot point to directories or cross filesystems.

```bash
ln -s /opt/app/current/bin/app /usr/local/bin/app   # symbolic link
ln original.txt hardlink.txt                        # hard link
ls -l   # symlinks show as: app -> /opt/app/current/bin/app
```

## 65: How do you find out what type a file is?

The `file` command looks at the content, not the extension.

```bash
$ file photo.jpg
photo.jpg: JPEG image data, ...
$ file script
script: Bourne-Again shell script, ASCII text executable
$ file /bin/ls
/bin/ls: ELF 64-bit LSB pie executable, x86-64, ...
```

Linux does not care about extensions to decide how to run something. It uses permissions and the file content.

## 66: How do you create and extract a tar archive?

```bash
tar -czf backup.tar.gz project/     # create, gzip compressed
tar -xzf backup.tar.gz              # extract
tar -xzf backup.tar.gz -C /tmp/     # extract into a directory
tar -tzf backup.tar.gz              # list contents
tar -cJf backup.tar.xz project/     # xz compression, smaller but slower
```

Flags: `c` create, `x` extract, `t` list, `z` gzip, `J` xz, `f` file name follows, `v` verbose. Modern GNU tar also detects the compression on extract, so `tar -xf file.tar.gz` works too.

## 67: How do you compress and decompress single files?

```bash
gzip file.log          # creates file.log.gz, removes original
gzip -k file.log       # keep the original
gunzip file.log.gz     # decompress
zcat file.log.gz       # print without decompressing to disk
zip -r site.zip site/  # zip format, common for sharing with Windows
unzip site.zip
```

`gzip` only works on single files. Use `tar` to bundle a directory first.

## 68: How do you connect to a remote server with ssh?

```bash
ssh user@server.example.com
ssh -p 2222 user@server          # custom port
ssh -i ~/.ssh/deploy_key user@server
ssh user@server 'df -h'          # run one command and exit
```

SSH gives you an encrypted shell on the remote machine. The first time you connect, it asks you to confirm the server's key fingerprint and saves it in `~/.ssh/known_hosts`.

## 69: How do you copy files between machines?

```bash
scp file.txt user@server:/tmp/              # local to remote
scp user@server:/var/log/app.log .          # remote to local
scp -r dist/ user@server:/var/www/app/      # directory
rsync -avz dist/ user@server:/var/www/app/  # faster for repeated copies
```

`rsync` only sends what changed, can resume, and is the better choice for deploys and backups.

## 70: How do you download files or call APIs from the command line?

```bash
curl https://example.com                     # print the response
curl -o page.html https://example.com        # save to file
curl -O https://example.com/file.zip         # save with the remote name
curl -L https://example.com                  # follow redirects
curl -I https://example.com                  # headers only
wget https://example.com/file.zip            # download a file
```

`curl` is better for APIs. `wget` is handy for downloading files and whole sites.

## 71: How do you install packages on Ubuntu or Debian?

```bash
sudo apt update              # refresh the package list
sudo apt install nginx       # install
sudo apt upgrade             # upgrade installed packages
sudo apt remove nginx        # remove, keep config
sudo apt purge nginx         # remove with config
apt search redis             # search
apt show nginx               # package details
```

On Fedora and RHEL the same ideas use `dnf`: `sudo dnf install nginx`. On Alpine it is `apk add nginx`.

## 72: What is systemd and how do you manage services?

systemd is the init system and service manager on most modern distros. It starts at boot as PID 1 and starts, stops and watches services.

```bash
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl reload nginx     # reload config without full restart
systemctl status nginx
sudo systemctl enable nginx     # start at boot
sudo systemctl enable --now nginx   # enable and start
sudo systemctl disable nginx
```

## 73: How do you read service logs with journalctl?

```bash
journalctl -u nginx          # logs for one service
journalctl -u nginx -f       # follow live
journalctl -u nginx --since "1 hour ago"
journalctl -b                # logs since last boot
journalctl -p err            # only errors and worse
journalctl -n 100            # last 100 lines
```

Traditional text logs are still in `/var/log` on many systems, for example `/var/log/syslog` or `/var/log/nginx/`.

## 74: What is the difference between .bashrc and .bash_profile?

`~/.bash_profile` (or `~/.profile`) is read by login shells, like when you log in over SSH. `~/.bashrc` is read by interactive non-login shells, like a new terminal tab on most Linux desktops.

The usual setup is to put everything in `~/.bashrc` and have `~/.bash_profile` load it:

```bash
# ~/.bash_profile
if [ -f ~/.bashrc ]; then
  . ~/.bashrc
fi
```

## 75: What is an alias?

An alias is a short name for a longer command. It only works in interactive shells.

```bash
alias ll='ls -lah'
alias gs='git status'
alias ..='cd ..'
unalias ll       # remove an alias
alias            # list all aliases
```

Put aliases in `~/.bashrc` so they load in every new shell.

## 76: What does source do?

`source file` (or `. file`) runs the commands from a file in the current shell, not in a new process. Variables, functions and `cd` from the file stay in your session.

```bash
source ~/.bashrc        # reload your config after editing
source .env             # load variables from a file
. ./venv/bin/activate   # activate a Python virtual environment
```

## 77: What is command substitution?

Command substitution runs a command and puts its output into another command or variable.

```bash
today=$(date +%F)
echo "Today is $today"
files=$(ls | wc -l)
echo "There are $files files"
```

The old form uses backticks: `` today=`date +%F` ``. The `$( )` form is easier to read and can be nested, so prefer it. Trailing newlines in the output are removed.

## 78: How do you do math in Bash?

Use arithmetic expansion `$(( ))` for integers.

```bash
a=10
b=3
echo $(( a + b ))   # 13
echo $(( a / b ))   # 3 (integer division)
echo $(( a % b ))   # 1
echo $(( a ** 2 ))  # 100
(( a++ ))           # increment
echo "$a"           # 11
```

Inside `$(( ))` you do not need `$` before variable names. Bash only does integer math. For decimals use `bc` or `awk`.

## 79: How do you write an if statement?

```bash
if [ "$1" = "start" ]; then
  echo "Starting"
elif [ "$1" = "stop" ]; then
  echo "Stopping"
else
  echo "Usage: $0 start|stop"
  exit 1
fi
```

`if` runs the command after it and checks its exit code. `0` means true. `[` is a command too, so the spaces inside the brackets are required.

## 80: What is the test command and how does [ ] relate to it?

`test` checks a condition and returns exit code 0 (true) or 1 (false). `[ ... ]` is the same command with a different name; it just needs a closing `]`.

```bash
test -f file.txt && echo "exists"
[ -f file.txt ] && echo "exists"
```

Both are available in any POSIX shell.

## 81: What is the difference between [ ] and [[ ]]?

`[[ ]]` is a Bash keyword, not a command, so it is safer and has more features:

- No word splitting or glob expansion on variables inside, so missing quotes are less of a problem
- `&&` and `||` work inside
- `==` with patterns: `[[ $file == *.txt ]]`
- Regex matching: `[[ $s =~ ^[0-9]+$ ]]`
- `<` and `>` compare strings without being treated as redirects

```bash
if [[ -n $name && $name == A* ]]; then
  echo "Name starts with A"
fi
```

Use `[[ ]]` in Bash scripts. Use `[ ]` when the script must run in plain `sh`.

## 82: What are the common file test operators?

| Test      | True if                 |
| --------- | ----------------------- |
| `-e file` | exists                  |
| `-f file` | is a regular file       |
| `-d file` | is a directory          |
| `-L file` | is a symbolic link      |
| `-r file` | is readable             |
| `-w file` | is writable             |
| `-x file` | is executable           |
| `-s file` | exists and is not empty |
| `a -nt b` | a is newer than b       |

```bash
if [[ ! -d logs ]]; then
  mkdir logs
fi
```

## 83: How do you compare strings in Bash?

```bash
[[ "$a" == "$b" ]]   # equal
[[ "$a" != "$b" ]]   # not equal
[[ -z "$a" ]]        # empty
[[ -n "$a" ]]        # not empty
[[ "$a" < "$b" ]]    # sorts before
```

Inside `[ ]` use a single `=` for portability: `[ "$a" = "$b" ]`.

## 84: How do you compare numbers in Bash?

With `[ ]` or `[[ ]]` use these operators:

| Operator | Meaning          |
| -------- | ---------------- |
| `-eq`    | equal            |
| `-ne`    | not equal        |
| `-lt`    | less than        |
| `-le`    | less or equal    |
| `-gt`    | greater than     |
| `-ge`    | greater or equal |

```bash
if [ "$count" -gt 10 ]; then echo "big"; fi
if (( count > 10 )); then echo "big"; fi   # arithmetic form, easier to read
```

Do not use `>` for numbers inside `[[ ]]`; it compares as text, so `"9" > "10"` is true.

## 85: How do you write a for loop?

```bash
for name in Anna Ben Carl; do
  echo "Hello $name"
done

for file in *.log; do
  echo "Processing $file"
done

for i in {1..5}; do
  echo "$i"
done

for (( i = 0; i < 5; i++ )); do
  echo "$i"
done
```

## 86: How do you write a while loop?

A `while` loop runs as long as the command after it succeeds.

```bash
count=1
while [ "$count" -le 5 ]; do
  echo "$count"
  count=$(( count + 1 ))
done

while true; do
  curl -s localhost:3000/health && break
  sleep 2
done
```

`break` exits the loop. `continue` skips to the next round.

## 87: What is an until loop?

`until` is the opposite of `while`. It runs as long as the command fails and stops when it succeeds.

```bash
until pg_isready -h localhost; do
  echo "Waiting for Postgres..."
  sleep 1
done
echo "Postgres is up"
```

## 88: How does the case statement work?

`case` matches a value against patterns. It is cleaner than a long chain of `if/elif`.

```bash
case "$1" in
  start)
    echo "Starting" ;;
  stop|halt)
    echo "Stopping" ;;
  *.txt)
    echo "Text file" ;;
  *)
    echo "Unknown option: $1"
    exit 1 ;;
esac
```

Each branch ends with `;;`. `*` catches everything else.

## 89: How do you define and call a function?

```bash
greet() {
  echo "Hello, $1"
}

greet "Anna"     # Hello, Anna
```

You call a function like a command, with arguments separated by spaces, not in parentheses. A function must be defined before you call it. There is also the `function greet { ... }` form, which works in Bash but not in plain `sh`.

## 90: How do you use arguments in a script or function?

| Variable        | Meaning                                |
| --------------- | -------------------------------------- |
| `$0`            | name of the script                     |
| `$1`, `$2`, ... | first, second argument                 |
| `${10}`         | tenth argument (braces needed)         |
| `$#`            | number of arguments                    |
| `"$@"`          | all arguments, each as a separate word |
| `"$*"`          | all arguments as one string            |

```bash
#!/usr/bin/env bash
echo "Script: $0"
echo "You passed $# arguments"
for arg in "$@"; do
  echo "- $arg"
done
```

Inside a function, `$1` and friends refer to the function's own arguments.

## 91: How do you read user input?

```bash
read -p "Enter your name: " name
echo "Hello, $name"

read -sp "Password: " password   # -s hides typing
echo

read -r line   # -r keeps backslashes as they are
```

Always use `-r` unless you really want backslash escapes to be processed.

## 92: How do you write comments in Bash?

Everything after `#` on a line is a comment, unless the `#` is inside quotes or part of a word.

```bash
# This is a comment
echo "hello"  # comment at the end of a line
echo "# not a comment"
```

Bash has no block comment syntax. A common trick is a no-op heredoc:

```bash
: <<'END'
these lines
are ignored
END
```

## 93: What does exit do in a script?

`exit` stops the script and returns an exit code to whoever started it. Without a number, it uses the exit code of the last command.

```bash
if [[ ! -f config.yml ]]; then
  echo "config.yml not found" >&2
  exit 1
fi
exit 0
```

Inside a function, use `return` instead, or you will end the whole script.

## 94: How do you create and use an array?

```bash
fruits=(apple banana cherry)
echo "${fruits[0]}"       # apple
echo "${fruits[@]}"       # all items
echo "${#fruits[@]}"      # number of items: 3
fruits+=(mango)           # add an item
for f in "${fruits[@]}"; do
  echo "$f"
done
```

Array indexes start at 0. Always quote `"${fruits[@]}"` so items with spaces stay together.

## 95: How do you get the length of a string?

```bash
name="Anna"
echo "${#name}"    # 4
```

The same `#` syntax gives the number of items for an array: `${#arr[@]}`.

## 96: What is brace expansion?

Brace expansion creates several words from a pattern. It happens before any other expansion and does not look at files.

```bash
echo {a,b,c}           # a b c
echo file{1..3}.txt    # file1.txt file2.txt file3.txt
mkdir -p app/{src,tests,docs}
cp config.yml{,.bak}   # cp config.yml config.yml.bak
echo {01..10}          # 01 02 ... 10 with zero padding
echo {0..20..5}        # 0 5 10 15 20
```

## 97: What does tilde ~ expand to?

`~` expands to your home directory, the value of `$HOME`. `~anna` expands to user anna's home directory.

```bash
cd ~/projects
ls ~anna
```

It only expands at the start of a word and not inside quotes. `"~/file"` stays as the literal text `~/file`, so use `"$HOME/file"` when you need quotes.

## 98: How do you clear the terminal screen?

Type `clear` or press `Ctrl+L`. `reset` goes further and fixes a terminal that shows garbage after printing binary data.

## 99: How do you compare two files?

```bash
diff old.txt new.txt        # show differences
diff -u old.txt new.txt     # unified format, like git diff
diff -r dir1/ dir2/         # compare directories
cmp file1.bin file2.bin     # byte by byte, for binary files
```

`diff` returns exit code 0 if the files are the same and 1 if they differ, which is useful in scripts.

## 100: What is xargs used for?

`xargs` reads items from stdin and passes them as arguments to a command. Some commands, like `rm`, do not read stdin, so `xargs` connects them to a pipe.

```bash
find . -name "*.tmp" | xargs rm
cat urls.txt | xargs -n 1 curl -O
echo "a b c" | xargs -n 1 echo    # runs echo three times
```

File names with spaces break this simple form. See `find -print0 | xargs -0` for the safe way.

## 101: What is sed and how do you do a simple find and replace?

`sed` is a stream editor. It reads text line by line and applies edits. The most common use is search and replace.

```bash
sed 's/foo/bar/' file.txt       # replace the first foo on each line
sed 's/foo/bar/g' file.txt      # replace all foo on each line
sed -i 's/8080/3000/g' config   # edit the file in place (GNU sed)
sed -n '10,20p' file.txt        # print only lines 10 to 20
sed '/^#/d' config              # delete comment lines
```

Without `-i`, `sed` prints the result and does not change the file.

## 102: What is awk and how do you print a column?

`awk` is a small language for processing text by fields. By default it splits each line on spaces and tabs. `$1` is the first field, `$NF` is the last, `$0` is the whole line.

```bash
awk '{print $1}' access.log              # first column
awk '{print $1, $NF}' file.txt           # first and last column
awk -F ':' '{print $1}' /etc/passwd      # use : as separator
awk '$3 > 100 {print $1}' data.txt       # filter by a column
```

## 103: What is the difference between a shell variable and an environment variable?

A shell variable lives only in the current shell. An environment variable is exported and copied to every child process the shell starts.

```bash
color=blue           # shell variable
export THEME=dark    # environment variable

bash -c 'echo "$color $THEME"'   # prints " dark"
```

Child processes get a copy. Changes they make never come back to the parent.

## 104: How do you debug a Bash script?

Turn on trace mode. Bash prints each command after expansion, starting with `+`.

```bash
bash -x script.sh          # trace the whole script

set -x                     # turn on inside the script
some_command
set +x                     # turn off

bash -n script.sh          # check syntax without running
```

`shellcheck script.sh` is a separate tool that finds many common bugs before you run anything.

## 105: How do you pause a script?

```bash
sleep 5       # 5 seconds
sleep 0.5     # half a second (GNU sleep)
sleep 2m      # 2 minutes
read -p "Press Enter to continue..."
```

## 106: What are true and false in Bash?

They are commands. `true` does nothing and returns 0. `false` does nothing and returns 1. They are used in loops and conditions.

```bash
while true; do
  echo "running"
  sleep 1
done
```

`:` is a builtin that works like `true` and is often used as a no-op.

## 107: How do you generate a sequence of numbers?

```bash
seq 5              # 1 2 3 4 5, one per line
seq 2 10           # 2 to 10
seq 0 5 20         # 0 5 10 15 20
seq -w 1 10        # zero padded: 01 ... 10
echo {1..5}        # brace expansion, no external command
```

Brace expansion cannot use variables (`{1..$n}` does not work). Use `seq 1 "$n"` or a C-style `for` loop for that.

## 108: What do basename and dirname do?

```bash
basename /var/log/nginx/access.log        # access.log
basename /var/log/nginx/access.log .log   # access
dirname /var/log/nginx/access.log         # /var/log/nginx
```

Bash can do the same without starting a process: `${path##*/}` for the name and `${path%/*}` for the directory.

## 109: What is cron and how do you schedule a job?

cron runs commands on a schedule. Each user has a crontab.

```bash
crontab -e     # edit your crontab
crontab -l     # list it
```

A line has five time fields, then the command:

```
# min hour day month weekday  command
0 2 * * *  /home/anna/backup.sh >> /home/anna/backup.log 2>&1
*/5 * * * * /usr/local/bin/check-health.sh
```

The first line runs at 02:00 every day. The second runs every 5 minutes.

## 110: How do you check network interfaces and IP addresses?

```bash
ip addr          # all interfaces and addresses (short: ip a)
ip -br a         # short one-line-per-interface view
ip route         # routing table and default gateway
hostname -I      # just the IP addresses
```

`ifconfig` is the old tool. It is still around on some systems but `ip` replaced it.

## 111: How do you check if a host is reachable?

```bash
ping -c 4 example.com           # send 4 packets
curl -I https://example.com     # check a web server
nc -zv example.com 443          # check if a TCP port is open
```

Some servers block ping (ICMP), so a failed ping does not always mean the host is down.

## 112: How do you see which ports are open on a machine?

```bash
ss -tlnp        # TCP, listening, numeric, with process (sudo shows all)
ss -ulnp        # UDP
sudo lsof -i :3000    # what is using port 3000
```

`ss` replaced `netstat`. The flags are mostly the same: `-t` TCP, `-u` UDP, `-l` listening, `-n` numbers instead of names, `-p` process.

## 113: Where are log files kept in Linux?

Most logs live in `/var/log`:

- `/var/log/syslog` or `/var/log/messages` for general system logs
- `/var/log/auth.log` or `/var/log/secure` for logins and sudo
- `/var/log/nginx/`, `/var/log/apache2/` for web servers
- `/var/log/kern.log` for kernel messages

On systemd systems many logs are also (or only) in the journal, read with `journalctl`.

## 114: How do you shut down or reboot a Linux machine?

```bash
sudo shutdown now          # power off now
sudo shutdown -r now       # reboot now
sudo shutdown -h +10       # power off in 10 minutes
sudo shutdown -c           # cancel a scheduled shutdown
sudo reboot
sudo poweroff
```

## 115: How do you change your password or another user's password?

```bash
passwd                # change your own password
sudo passwd anna      # set a password for anna
sudo passwd -l anna   # lock the account
```

## 116: How do you add a new user?

```bash
sudo useradd -m -s /bin/bash anna   # -m creates the home directory
sudo passwd anna
sudo usermod -aG sudo anna          # add to the sudo group (wheel on RHEL)
sudo userdel -r anna                # delete user and home directory
```

On Debian and Ubuntu, `sudo adduser anna` is a friendlier wrapper that asks for details.

## 117: How do you change your default shell?

```bash
chsh -s /bin/zsh       # change your login shell
cat /etc/shells        # list allowed shells
```

The change takes effect the next time you log in.

## 118: What is a login shell and an interactive shell?

A login shell is the first shell after you log in, for example over SSH or on a text console. It reads `/etc/profile` and then the first of `~/.bash_profile`, `~/.bash_login` or `~/.profile` it finds.

An interactive shell is one that reads commands from your keyboard. A new terminal tab is usually interactive but not login, so it reads `~/.bashrc`.

A script you run is neither. It does not read these files at all.

## 119: How do you edit a file in the terminal?

`nano` is the easiest. Commands are shown at the bottom (`Ctrl+O` save, `Ctrl+X` exit).

`vim` (or `vi`) is installed almost everywhere, so it is worth knowing the basics:

- `i` to start typing (insert mode)
- `Esc` to go back to normal mode
- `:w` save, `:q` quit, `:wq` save and quit, `:q!` quit without saving
- `/text` to search

## 120: How do you print the first or last N characters of a line?

```bash
s="hello world"
echo "${s:0:5}"     # hello (start at 0, length 5)
echo "${s: -5}"     # world (last 5, note the space before -)
echo "${s:6}"       # world (from index 6 to the end)
```

## 121: How do you check if a variable is empty?

```bash
if [[ -z "$name" ]]; then
  echo "name is empty or not set"
fi

if [[ -n "$name" ]]; then
  echo "name has a value"
fi
```

`-z` is true for both an unset variable and one set to an empty string.

## 122: What is the difference between > and >>?

`>` creates the file or empties it first, then writes. `>>` adds to the end of the file and keeps what was there.

```bash
echo "first" > log.txt
echo "second" >> log.txt
cat log.txt
# first
# second
```

A common mistake is `sort file > file`, which empties the file before `sort` reads it.

## 123: How do you redirect stderr to stdout?

```bash
command > output.txt 2>&1    # both go to output.txt
command 2>&1 | grep error    # send both through a pipe
command |& grep error        # bash shortcut for 2>&1 |
```

`2>&1` means "make file descriptor 2 point where 1 points right now". Order matters: `> file 2>&1` works, `2>&1 > file` sends only stdout to the file.

## 124: What is the difference between rm -r and rmdir?

`rmdir` only deletes empty directories, so it is safe; it refuses if there is anything inside. `rm -r` deletes the directory and everything inside it.

## 125: How do you list the contents of a directory as a tree?

```bash
tree                # needs the tree package
tree -L 2           # only 2 levels deep
tree -I node_modules
find . -maxdepth 2  # without tree
```

## 126: How do you look at the beginning of many files at once?

```bash
head -n 3 *.csv       # prints a header with each file name
tail -n 1 *.log
```

Use `-q` to hide the file name headers.

## 127: How do you see who is logged in?

```bash
who          # who is logged in now
w            # who is logged in and what they are doing
last         # recent logins
whoami       # your own user name
```

## 128: What does the env command do?

Without arguments, `env` prints all environment variables. With a command, it runs that command with a changed environment.

```bash
env                          # list environment
env NODE_ENV=test npm test   # run with an extra variable
env -i bash                  # start bash with an empty environment
```

The `#!/usr/bin/env bash` shebang uses `env` to find `bash` in `PATH`.

## 129: How do you make a variable read-only?

```bash
readonly API_VERSION="v2"
API_VERSION="v3"   # bash: API_VERSION: readonly variable

declare -r MAX=10  # same effect
```

A read-only variable cannot be changed or unset for the rest of the shell's life.

## 130: How do you remove a variable?

```bash
name="Anna"
unset name
echo "${name:-<not set>}"   # <not set>
```

`unset -f myfunc` removes a function.

## 131: What is the difference between $@ and $*?

Both hold all the script's arguments. The difference shows when they are quoted:

- `"$@"` expands to each argument as a separate word, keeping spaces inside arguments.
- `"$*"` joins all arguments into a single string, separated by the first character of `IFS` (a space by default).

```bash
# ./show.sh "a b" c
for x in "$@"; do echo "[$x]"; done   # [a b] [c]
for x in "$*"; do echo "[$x]"; done   # [a b c]
```

You almost always want `"$@"`.

## 132: What does $? hold and when should you check it?

`$?` holds the exit code of the last command. It changes after every command, even `echo` or `[`, so check or save it right away.

```bash
grep -q "ready" status.txt
status=$?
if (( status == 0 )); then
  echo "ready"
fi
```

Often it is simpler to put the command in the `if` directly: `if grep -q "ready" status.txt; then ...`.

## 133: How do you check if a command exists?

```bash
if command -v docker > /dev/null 2>&1; then
  echo "docker is installed"
else
  echo "docker not found" >&2
  exit 1
fi
```

`command -v` is a POSIX builtin. It is more reliable than `which`, whose output and exit codes differ between systems.

## 134: What does the touch command do besides creating files?

`touch` updates the access and modification time of a file to now. If the file does not exist, it creates an empty one.

```bash
touch app.log                       # create or update time
touch -d "2026-01-01 10:00" f.txt   # set a specific time
touch -c f.txt                      # do not create if missing
```

Build tools like `make` use modification times, so `touch` can force a rebuild.

## 135: How do you count the number of files in a directory?

```bash
ls | wc -l                       # visible entries
ls -A | wc -l                    # include hidden, skip . and ..
find . -maxdepth 1 -type f | wc -l   # only files, not directories
find . -type f | wc -l           # all files, recursively
```

## 136: What are the common package formats?

- `.deb` packages on Debian and Ubuntu, managed by `dpkg` at a low level and `apt` on top.
- `.rpm` packages on RHEL, Fedora and SUSE, managed by `rpm` at a low level and `dnf` or `zypper` on top.
- Universal formats like Snap, Flatpak and AppImage bundle their own dependencies and work across distros.

The higher-level tools (`apt`, `dnf`) download packages and handle dependencies for you.

## 137: How do you check the size of a file?

```bash
ls -lh file.zip           # human readable
du -h file.zip            # disk usage (may differ for sparse files)
stat -c %s file.zip       # exact bytes (GNU stat)
wc -c < file.zip          # exact bytes, works everywhere
```

## 138: What does the stat command show?

`stat` shows detailed info about a file: size, blocks, inode number, permissions, owner, and the access, modify and change times.

```bash
stat file.txt
stat -c '%U %a %s' file.txt   # owner, octal permissions, size (GNU)
```

On macOS, `stat` is the BSD version and uses `-f` instead of `-c`.

## 139: How do you see the end of a command's output only?

Pipe it into `tail` or `head`.

```bash
dmesg | tail -n 20
ls -lt | head -n 5     # 5 newest files
history | tail -n 10
```

## 140: How do you run the same command again with a small change?

```bash
^old^new        # rerun the last command, replacing old with new
!!              # whole last command
!$              # last argument of the last command
!ssh            # last command that started with ssh
```

For example, after `cat /etc/nginx/nginx.conf`, typing `vim !$` opens the same file.

## 141: How do you check what a command will do before running it?

A few habits help:

- Put `echo` in front: `echo rm *.log` shows what the glob expands to.
- Use `-i` (interactive) with `rm`, `cp` and `mv`.
- Many tools have a dry-run flag: `rsync -n`, `apt -s`, `make -n`.
- Run `ls` with the same pattern first.

## 142: What is a process versus a program?

A program is a file on disk with code in it, like `/usr/bin/python3`. A process is a running copy of a program with its own PID, memory, open files and environment. If you start Python three times, you have one program and three processes.

## 143: What is the difference between a builtin and an external command?

A builtin is part of the shell itself, like `cd`, `echo`, `read`, `export` and `source`. It runs without starting a new process. An external command is a separate program on disk, like `ls`, `grep` or `curl`.

Some commands have to be builtins. `cd` must change the shell's own directory, which a child process could not do.

## 144: How do you print a message to stderr?

```bash
echo "Error: config not found" >&2
printf 'Warning: %s\n' "$msg" >&2
```

Errors go to stderr so they still show up when someone redirects the normal output to a file or pipe.

## 145: How do you run a command as a different user?

```bash
sudo -u www-data whoami
sudo -u postgres psql
su - deploy -c 'cd /app && git pull'
```

`sudo -u` needs the right rule in `/etc/sudoers`. `su` needs the target user's password unless you are root.

## 146: How do you view the manual page sections?

Man pages are grouped into numbered sections:

- `1` user commands (`ls`, `grep`)
- `2` system calls (`open`, `fork`)
- `3` library functions (`printf` in C)
- `5` file formats (`passwd`, `crontab`)
- `8` admin commands (`mount`, `useradd`)

```bash
man 1 printf    # the shell command
man 3 printf    # the C function
man 5 crontab   # the crontab file format
```

## 147: What is the difference between cat and less?

`cat` prints the whole file to the terminal at once and exits. It is good for small files and for joining files: `cat a.txt b.txt > both.txt`.

`less` opens the file in a pager. You can scroll, search with `/`, jump with `G` (end) and `g` (start), and it does not load the whole file into memory first, so it handles big files well.

## 148: How do you check how long a command takes?

```bash
time npm run build
# real    0m12.345s   wall clock time
# user    0m20.111s   CPU time in user code
# sys     0m1.234s    CPU time in the kernel
```

`user` can be bigger than `real` when the command uses several CPU cores.

## 149: What is the difference between apt and apt-get?

`apt-get` is the older, stable interface, made for scripts. Its output format does not change between versions.

`apt` is a newer, friendlier front end for people at a terminal. It has a progress bar and combines common commands from `apt-get` and `apt-cache`. In scripts, `apt-get` is still recommended because `apt` warns that its interface is not stable.

## 150: How do you make a simple backup of a file before editing it?

```bash
cp nginx.conf nginx.conf.bak
cp nginx.conf{,.bak}                    # same, using brace expansion
cp nginx.conf "nginx.conf.$(date +%F)"  # with the date
sed -i.bak 's/old/new/' nginx.conf      # sed keeps a .bak copy
```

---

# Moderate Questions (151-300)

## 151: What does set -euo pipefail do?

It is a common first line in Bash scripts to make them stop on errors instead of carrying on silently.

- `set -e` exits the script when a command fails.
- `set -u` treats using an unset variable as an error.
- `set -o pipefail` makes a pipeline fail if any command in it fails, not just the last one.

```bash
#!/usr/bin/env bash
set -euo pipefail

cd "$APP_DIR"            # exits if APP_DIR is unset or cd fails
curl -fsS "$URL" | jq .  # fails if curl fails, even though jq is last
```

`set -e` has many exceptions (inside `if`, with `&&` and `||`, and more), so it is a safety net, not a full error handling plan.

## 152: What is trap and how do you use it?

`trap` runs a command when the shell gets a signal or reaches a special event like `EXIT`.

```bash
tmpdir=$(mktemp -d)
trap 'rm -rf "$tmpdir"' EXIT    # clean up however the script ends

trap 'echo "Interrupted"; exit 130' INT
```

Useful events: `EXIT` (script ends), `ERR` (a command fails), `INT` (Ctrl+C), `TERM` (kill), `DEBUG` (before each command). Use single quotes so variables are expanded when the trap runs, not when it is set.

## 153: How do you parse command line options with getopts?

`getopts` is a builtin that parses short options like `-v` and `-f file`.

```bash
#!/usr/bin/env bash
verbose=false
output="out.txt"

while getopts ":vo:h" opt; do
  case "$opt" in
    v) verbose=true ;;
    o) output="$OPTARG" ;;
    h) echo "Usage: $0 [-v] [-o file] args"; exit 0 ;;
    :) echo "Option -$OPTARG needs a value" >&2; exit 1 ;;
    \?) echo "Unknown option -$OPTARG" >&2; exit 1 ;;
  esac
done
shift $(( OPTIND - 1 ))   # remove parsed options, leave the rest in $@

echo "verbose=$verbose output=$output rest=$*"
```

A `:` after a letter means it takes a value. The leading `:` turns on silent error mode so you can print your own messages. `getopts` does not support long options like `--verbose`.

## 154: How do you set a default value for a variable?

```bash
name=${1:-guest}           # use guest if $1 is unset or empty
port=${PORT:-3000}
: "${LOG_DIR:=/var/log/app}"   # set LOG_DIR if unset or empty, and keep it
```

`${var:-default}` returns the default but does not change `var`. `${var:=default}` also assigns it. Without the colon (`${var-default}`), the default is used only when the variable is unset, not when it is empty.

## 155: How do you make a script fail when a required variable is missing?

```bash
: "${DATABASE_URL:?DATABASE_URL must be set}"
```

If `DATABASE_URL` is unset or empty, Bash prints the message and exits a non-interactive shell with an error. `:` is a no-op command, so the line does nothing else when the variable is set.

## 156: How do you remove a prefix or suffix from a variable?

```bash
file="/var/log/app/error.log.gz"

echo "${file#*/}"     # var/log/app/error.log.gz   shortest match from the start
echo "${file##*/}"    # error.log.gz               longest match from the start
echo "${file%.*}"     # /var/log/app/error.log     shortest match from the end
echo "${file%%.*}"    # /var/log/app/error         longest match from the end
echo "${file%/*}"     # /var/log/app               like dirname
```

One `#` or `%` removes the shortest match, two remove the longest. These run inside Bash, so they are faster than calling `basename` or `sed` in a loop.

## 157: How do you replace text inside a variable?

```bash
s="hello world, hello bash"
echo "${s/hello/hi}"      # hi world, hello bash  (first match)
echo "${s//hello/hi}"     # hi world, hi bash     (all matches)
echo "${s/#hello/hi}"     # replace only at the start
echo "${s/%bash/zsh}"     # replace only at the end
echo "${s// /_}"          # replace spaces with underscores
```

The pattern is a glob, not a regex.

## 158: How do you change the case of a string in Bash?

```bash
name="hello World"
echo "${name^^}"   # HELLO WORLD
echo "${name,,}"   # hello world
echo "${name^}"    # Hello World  (first character only)
```

This needs Bash 4 or newer. macOS ships Bash 3.2, where you need `tr '[:lower:]' '[:upper:]'` instead.

## 159: What is indirect variable expansion?

`${!name}` uses the value of `name` as the name of another variable.

```bash
env_name="PROD_URL"
PROD_URL="https://api.example.com"
echo "${!env_name}"     # https://api.example.com
```

`${!prefix*}` lists variable names that start with a prefix: `echo "${!BASH*}"`. For more complex cases, namerefs (`declare -n`) are clearer.

## 160: How do associative arrays work?

Associative arrays use strings as keys. You must declare them first with `declare -A`. They need Bash 4 or newer.

```bash
declare -A ports=(
  [web]=80
  [api]=3000
)
ports[db]=5432

echo "${ports[api]}"          # 3000
echo "${!ports[@]}"           # all keys
echo "${ports[@]}"            # all values

for service in "${!ports[@]}"; do
  echo "$service -> ${ports[$service]}"
done

[[ -v ports[cache] ]] || echo "no cache port"
unset 'ports[web]'
```

Keys come out in no particular order.

## 161: How do you read a file into an array?

```bash
mapfile -t lines < hosts.txt     # or: readarray -t lines < hosts.txt
echo "Read ${#lines[@]} lines"
for host in "${lines[@]}"; do
  echo "$host"
done
```

`-t` removes the trailing newline from each line. To read command output, use process substitution: `mapfile -t files < <(find . -name '*.js')`.

## 162: How do you read a file line by line?

```bash
while IFS= read -r line; do
  echo "Line: $line"
done < input.txt
```

- `IFS=` keeps leading and trailing spaces.
- `-r` keeps backslashes as they are.
- `< input.txt` at the end feeds the file into the loop.

If the last line has no newline at the end, `read` returns false and the loop skips it. Use `while IFS= read -r line || [[ -n $line ]]` to catch it.

## 163: What is IFS?

`IFS` (Internal Field Separator) is the list of characters Bash uses to split words after expansion and in `read`. The default is space, tab and newline.

```bash
IFS=',' read -r name age city <<< "Anna,30,Berlin"
echo "$city"    # Berlin

IFS=: read -ra parts <<< "$PATH"
printf '%s\n' "${parts[@]}"
```

Setting `IFS` right before `read` only changes it for that one command, so the rest of the script is not affected.

## 164: How do you split a string into an array?

```bash
csv="red,green,blue"
IFS=',' read -ra colors <<< "$csv"
echo "${colors[1]}"   # green
echo "${#colors[@]}"  # 3
```

`-a` reads into an array. Avoid `arr=($csv)` with a changed `IFS`, since it also expands globs like `*` in the data.

## 165: How do you join array items with a separator?

```bash
items=(a b c)

(IFS=,; echo "${items[*]}")    # a,b,c   (subshell keeps IFS change local)

join_by() {
  local IFS="$1"
  shift
  echo "$*"
}
join_by '|' "${items[@]}"     # a|b|c
```

`"${arr[*]}"` joins with the first character of `IFS`. For multi-character separators use `printf` and then strip the last one.

## 166: What is process substitution?

Process substitution `<(command)` lets you use the output of a command where a file name is expected. Bash gives the command a path like `/dev/fd/63`.

```bash
diff <(sort old.txt) <(sort new.txt)
comm -13 <(sort a.txt) <(sort b.txt)

while IFS= read -r f; do
  count=$((count + 1))
done < <(find . -name '*.log')
echo "$count"     # works, because the loop is not in a subshell
```

`>(command)` does the opposite: it gives a path you can write to, for example `tee >(gzip > log.gz)`.

## 167: What is a here document?

A here document sends several lines of text into a command's stdin.

```bash
cat <<EOF > config.ini
[server]
host=$HOST
port=${PORT:-8080}
EOF
```

Variables and commands inside are expanded. The closing `EOF` must be alone on its line with no spaces before it. The word `EOF` is only a convention; any word works.

## 168: How do you stop variable expansion in a here document?

Quote the delimiter. Then the text is passed exactly as written.

```bash
cat <<'EOF' > deploy.sh
#!/usr/bin/env bash
echo "Deploying to $TARGET"
EOF
```

Here `$TARGET` stays literal in `deploy.sh`. This is handy when a script writes another script.

## 169: What does <<- do in a here document?

`<<-` removes leading tab characters (not spaces) from each line and from the closing delimiter. It lets you indent heredocs inside functions or `if` blocks.

```bash
if true; then
	cat <<-EOF
	indented with tabs
	in the source file
	EOF
fi
```

Many editors turn tabs into spaces, which breaks this. Check your editor settings if it fails.

## 170: What is a here string?

A here string `<<<` sends one string to a command's stdin, with a newline added.

```bash
grep -c "a" <<< "banana"         # 1 (counts lines, not matches)
read -r first rest <<< "hello big world"
bc <<< "scale=2; 10/3"           # 3.33
```

It is shorter than `echo "$var" | command` and does not create a pipeline.

## 171: What is the difference between ( ) and { } for grouping commands?

`( commands )` runs the commands in a subshell, a separate copy of the shell. Changes to variables, `cd` and `set` options do not affect the parent.

`{ commands; }` runs them in the current shell. You need spaces after `{` and a `;` or newline before `}`.

```bash
(cd /tmp && ls)          # your directory does not change
{ echo "start"; date; } > log.txt   # redirect output of a group
x=1; ( x=2 ); echo "$x"  # 1
x=1; { x=2; }; echo "$x" # 2
```

## 172: How do local variables work in functions?

By default, every variable in Bash is global, even when set inside a function. Use `local` to keep it inside.

```bash
count=0
increment() {
  local step=${1:-1}
  count=$(( count + step ))
}
increment 5
echo "$count"   # 5
echo "$step"    # empty, step was local
```

Bash uses dynamic scoping: a function called from inside another function can see the caller's local variables.

## 173: How do you return a value from a function?

`return` only sets an exit code (0 to 255). It is for success or failure, not data. To return data, print it and capture it with command substitution.

```bash
get_version() {
  jq -r .version package.json
}
version=$(get_version)

is_running() {
  pgrep -x "$1" > /dev/null
}
if is_running nginx; then echo "up"; fi
```

You can also set a global variable or use a nameref (`declare -n`) to avoid the subshell that `$( )` creates.

## 174: What is PIPESTATUS?

`PIPESTATUS` is an array holding the exit code of every command in the last pipeline.

```bash
false | true | grep -q x
echo "${PIPESTATUS[@]}"   # 1 0 1
```

`$?` only gives the last one. Read `PIPESTATUS` right after the pipeline, since the next command overwrites it.

## 175: What are the main gotchas with set -e?

`set -e` does not exit in several cases:

- Commands in an `if`, `while` or `until` condition
- Any command in a `&&` or `||` list, except the last
- Commands after `!`
- Inside a function called as part of one of the above (the whole function runs with `-e` ignored)
- In a pipeline, only the last command counts unless `pipefail` is set
- Command substitution in a `local` declaration: `local x=$(false)` succeeds because `local` succeeds

```bash
set -e
check() { false; echo "still running"; }
if check; then echo "ok"; fi   # prints "still running" and "ok"
```

Split `local x; x=$(cmd)` and check important commands explicitly.

## 176: What is the difference between find -exec and xargs?

`find -exec cmd {} \;` runs the command once per file. `-exec cmd {} +` passes many files at once, like `xargs`.

```bash
find . -name "*.log" -exec rm {} \;      # one rm per file, slow
find . -name "*.log" -exec rm {} +       # few rm calls, fast
find . -name "*.log" -print0 | xargs -0 rm
find . -name "*.log" -delete             # built into GNU find
```

`xargs` adds options like `-P` for running in parallel. `-exec ... +` is simpler and safe with any file name.

## 177: How do you safely handle file names with spaces or newlines in a pipeline?

Use null characters as separators, since a file name can contain anything except `/` and the null byte.

```bash
find . -type f -name "*.jpg" -print0 | xargs -0 -I{} cp {} /backup/

while IFS= read -r -d '' file; do
  echo "Found: $file"
done < <(find . -type f -print0)
```

`-print0` ends each name with a null byte, `xargs -0` and `read -d ''` read null-separated input.

## 178: What are the useful grep options for real work?

```bash
grep -E 'error|warn' app.log         # extended regex (like egrep)
grep -F '[ERROR]' app.log            # fixed string, no regex
grep -o '[0-9]\{3\}' file            # print only the matching part
grep -A 3 'Exception' app.log        # 3 lines after each match
grep -B 2 -C 2 'panic' app.log       # 2 before, 2 around
grep -rn --include='*.ts' 'useEffect' src/
grep -rL 'license' src/              # files that do NOT match
grep -q 'ready' status && echo ok    # quiet, only exit code
grep -P '\d+' file                   # Perl regex (GNU grep only)
```

## 179: How do you use sed with line ranges and patterns?

```bash
sed -n '5p' file            # print line 5
sed -n '5,10p' file         # lines 5 to 10
sed -n '/START/,/END/p' f   # from a line matching START to one matching END
sed '1d' file.csv           # delete the header line
sed '$d' file               # delete the last line
sed '/^$/d' file            # delete empty lines
sed '3i\new line' file      # insert before line 3
sed '/^server/a\  listen 80;' nginx.conf   # append after matching lines
sed -E 's/([0-9]+)-([0-9]+)/\2-\1/' file   # swap with capture groups
```

## 180: Why does sed -i behave differently on Linux and macOS?

GNU sed (Linux) takes an optional backup suffix attached to `-i`. BSD sed (macOS) requires a suffix argument, which can be empty.

```bash
sed -i 's/a/b/' file        # GNU: works. macOS: error
sed -i '' 's/a/b/' file     # macOS: works. GNU: treats '' as the script
sed -i.bak 's/a/b/' file    # works on both, creates file.bak
```

For scripts that must run on both, use `-i.bak` and delete the backup, or install GNU sed on macOS (`gsed`).

## 181: How do you use BEGIN and END blocks in awk?

`BEGIN` runs before any input is read, `END` runs after all input is done. They are used for setup and for printing totals.

```bash
awk 'BEGIN { FS="," } { total += $3 } END { print "Total:", total }' sales.csv

awk -F ':' 'BEGIN { print "user shell" } { print $1, $7 }' /etc/passwd
```

Variables in `awk` start at 0 or empty string, so you do not need to set `total=0`.

## 182: How do you count and group with awk?

`awk` has associative arrays, which makes grouping easy.

```bash
# requests per IP in an nginx access log
awk '{ count[$1]++ } END { for (ip in count) print count[ip], ip }' access.log | sort -rn | head

# sum of bytes per status code
awk '{ bytes[$9] += $10 } END { for (s in bytes) print s, bytes[s] }' access.log
```

## 183: How do you sort by a specific column?

```bash
sort -k 2 file.txt               # by column 2 to end of line
sort -k 2,2 file.txt             # by column 2 only
sort -t ',' -k 3,3n data.csv     # CSV, numeric by column 3
sort -k 3,3nr -k 1,1 data.txt    # column 3 numeric descending, then column 1
du -sh * | sort -h               # human sizes
```

`-k 2` without an end field sorts by everything from column 2 onwards, which is rarely what you want. Use `-k 2,2`.

## 184: How do you find the top N most common lines?

This is a classic pipeline:

```bash
sort access.log | uniq -c | sort -rn | head -n 10

# top 10 IPs
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -n 10
```

Steps: sort so duplicates are next to each other, count with `uniq -c`, sort the counts in reverse number order, keep the first 10.

## 185: What does tee do?

`tee` reads stdin and writes it both to stdout and to one or more files. You see the output and save it at the same time.

```bash
npm test 2>&1 | tee test.log
./build.sh | tee -a build.log           # append
echo "127.0.0.1 myapp" | sudo tee -a /etc/hosts > /dev/null
```

The last line is the usual way to write to a root-owned file, since `sudo echo ... >> /etc/hosts` fails (the redirect runs as your user).

## 186: How do you join lines from two files side by side?

```bash
paste names.txt ages.txt         # tab separated
paste -d ',' names.txt ages.txt  # comma separated
paste -sd ',' names.txt          # join all lines of one file with commas
```

`join` merges two sorted files on a common field, like a database join:

```bash
join -t ',' <(sort users.csv) <(sort orders.csv)
```

## 187: How do you format output into aligned columns?

```bash
column -t -s ',' data.csv      # CSV as an aligned table
mount | column -t
printf '%-15s %8s\n' "Name" "Size"
printf '%-15s %8d\n' "app.js" 1234
```

## 188: How do you find lines that are in one file but not another?

`comm` compares two sorted files and prints three columns: only in file 1, only in file 2, in both.

```bash
comm -23 <(sort a.txt) <(sort b.txt)   # only in a.txt
comm -13 <(sort a.txt) <(sort b.txt)   # only in b.txt
comm -12 <(sort a.txt) <(sort b.txt)   # in both
grep -vxFf b.txt a.txt                 # only in a.txt, without sorting
```

## 189: How do you do floating point math in a script?

Bash only does integers. Use `bc` or `awk`.

```bash
echo "scale=2; 10 / 3" | bc        # 3.33
bc -l <<< "s(1)"                   # math library, sine of 1
awk 'BEGIN { printf "%.2f\n", 10/3 }'
result=$(awk -v a=5.5 -v b=2 'BEGIN { print a * b }')
```

## 190: What is the difference between let, (( )) and $(( ))?

- `$(( expr ))` is an expansion. It is replaced by the result, so you use it inside other commands.
- `(( expr ))` is a command. It does the math and returns exit code 0 if the result is non-zero, and 1 if it is zero. Good for conditions and changing variables.
- `let expr` is the older form of `(( ))`.

```bash
total=$(( price * qty ))
(( count++ ))
if (( count > 10 )); then echo "many"; fi
let "x = 5 * 3"
```

Watch out: with `set -e`, `(( count++ ))` when `count` is 0 returns 1 and stops the script. Use `count=$(( count + 1 ))` instead.

## 191: How do you generate random numbers?

```bash
echo $RANDOM                   # 0 to 32767
echo $(( RANDOM % 100 + 1 ))   # 1 to 100
echo $SRANDOM                  # 32-bit, better random, Bash 5.1+
shuf -i 1-100 -n 1             # coreutils
openssl rand -hex 16           # for secrets and tokens
```

`$RANDOM` is not safe for passwords or tokens. Use `openssl rand` or `/dev/urandom` for those.

## 192: How do you match a regular expression in Bash?

Use `=~` inside `[[ ]]`. Capture groups end up in the `BASH_REMATCH` array.

```bash
version="v2.14.3"
if [[ $version =~ ^v([0-9]+)\.([0-9]+)\.([0-9]+)$ ]]; then
  echo "major=${BASH_REMATCH[1]} minor=${BASH_REMATCH[2]}"
fi
```

Do not quote the regex on the right side. Quoting makes it a plain string match. For complex patterns, put the regex in a variable first: `re='^[a-z]+$'; [[ $s =~ $re ]]`.

## 193: What do shopt options like nullglob, globstar and extglob do?

`shopt` turns on extra Bash behavior.

```bash
shopt -s nullglob   # a glob with no matches becomes nothing, not the literal text
for f in *.csv; do echo "$f"; done   # loop does not run if no .csv files

shopt -s globstar   # ** matches any number of directories
ls src/**/*.ts

shopt -s extglob    # extended patterns
rm !(*.keep)        # everything except *.keep
ls +(a|b).txt       # a.txt, b.txt, aa.txt ...

shopt -s dotglob    # * also matches hidden files
shopt -s nocaseglob # case insensitive globbing
```

`shopt -u name` turns an option off. `shopt` with no args lists all of them.

## 194: What is the difference between globs and regular expressions?

Globs are used by the shell for file names and by `case` and `[[ == ]]`. Regular expressions are used by tools like `grep`, `sed`, `awk` and by `[[ =~ ]]`.

| Meaning           | Glob               | Regex       |
| ----------------- | ------------------ | ----------- |
| any characters    | `*`                | `.*`        |
| one character     | `?`                | `.`         |
| one of a set      | `[abc]`            | `[abc]`     |
| start/end anchors | always whole match | `^` and `$` |

`*.txt` as a glob means "ends with .txt". As a regex it would mean "zero or more of any character, then any character, then txt".

## 195: What is the difference between "${arr[@]}" and "${arr[*]}"?

`"${arr[@]}"` expands to every item as a separate word. `"${arr[*]}"` joins all items into one word, separated by the first character of `IFS`.

```bash
files=("a b.txt" "c.txt")
touch "${files[@]}"   # creates "a b.txt" and "c.txt"
touch "${files[*]}"   # creates one file "a b.txt c.txt"
```

Use `[@]` for passing items to commands and loops. Use `[*]` only when you want one joined string.

## 196: What does shift do?

`shift` drops the first argument and moves the rest down: `$2` becomes `$1`, and so on. `$#` goes down by one. `shift 2` drops two.

```bash
while (( $# > 0 )); do
  case "$1" in
    -v|--verbose) verbose=1; shift ;;
    -o|--output)  output="$2"; shift 2 ;;
    --) shift; break ;;
    *) break ;;
  esac
done
```

This pattern is how most scripts parse long options by hand.

## 197: How do you build a simple menu with select?

`select` shows a numbered list and reads the user's choice into a variable.

```bash
PS3="Choose an environment: "
select env in dev staging prod quit; do
  case "$env" in
    quit) break ;;
    "") echo "Invalid choice" ;;
    *) echo "Deploying to $env"; break ;;
  esac
done
```

If the user types a number that is not in the list, the variable is empty. `$REPLY` holds what they actually typed.

## 198: What are the special strings and gotchas in crontab syntax?

```
@reboot     /opt/app/start.sh
@daily      /opt/app/cleanup.sh     # same as 0 0 * * *
@hourly     /opt/app/sync.sh
0 9 * * 1-5 /opt/app/report.sh      # weekdays at 09:00
0 0 1 * *   /opt/app/monthly.sh     # first day of each month
```

Gotchas:

- `%` has a special meaning in crontab (newline). Escape it: `date +\%F`.
- If both day of month and day of week are set, the job runs when either matches.
- Times use the server's time zone unless your cron supports `CRON_TZ`.

## 199: Why does a script work in my terminal but not in cron?

cron runs jobs with a very small environment. Common causes:

- `PATH` is short (often `/usr/bin:/bin`), so commands in `/usr/local/bin` or `~/.local/bin` are not found.
- Your `~/.bashrc` is not loaded, so aliases, `nvm`, `pyenv` and exported variables are missing.
- The working directory is your home, not the script's folder.
- The shell may be `/bin/sh`, not Bash.
- No output is visible unless you redirect it or mail is set up.

Fix it with full paths, setting `PATH` at the top of the crontab or script, `cd` to the right directory, and logging output: `... >> /var/log/job.log 2>&1`.

## 200: How do you write a basic systemd service for an app?

Create `/etc/systemd/system/myapp.service`:

```ini
[Unit]
Description=My Node app
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=deploy
WorkingDirectory=/opt/myapp
EnvironmentFile=/opt/myapp/.env
ExecStart=/usr/bin/node server.js
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Then:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now myapp
journalctl -u myapp -f
```

## 201: What is a systemd timer and why use it instead of cron?

A timer is a unit that starts a service on a schedule. You need two files: `backup.service` with the job and `backup.timer` with the schedule.

```ini
# /etc/systemd/system/backup.timer
[Unit]
Description=Nightly backup

[Timer]
OnCalendar=*-*-* 02:00:00
Persistent=true

[Install]
WantedBy=timers.target
```

```bash
sudo systemctl enable --now backup.timer
systemctl list-timers
```

Compared to cron you get logs in the journal, `Persistent=true` to run missed jobs after downtime, dependencies on other units, and resource limits. The cost is two files instead of one line.

## 202: How do you filter journalctl output?

```bash
journalctl -u myapp --since today
journalctl -u myapp --since "2026-10-29 09:00" --until "2026-10-29 10:00"
journalctl -u myapp -p warning     # warning and worse
journalctl _PID=1234
journalctl -k                      # kernel messages, like dmesg
journalctl -u myapp -o json-pretty # structured output
journalctl -u myapp --no-pager | grep -i timeout
journalctl --disk-usage
sudo journalctl --vacuum-time=7d   # delete logs older than 7 days
```

## 203: How do you set up SSH key login?

```bash
ssh-keygen -t ed25519 -C "anna@laptop"   # creates ~/.ssh/id_ed25519 and .pub
ssh-copy-id user@server                  # adds the public key to the server
ssh user@server                          # now logs in with the key
```

`ssh-copy-id` appends your public key to `~/.ssh/authorized_keys` on the server. The private key never leaves your machine. Ed25519 keys are the current recommended type.

## 204: What is the ~/.ssh/config file for?

It stores per-host settings so you do not have to type them every time.

```
Host prod
  HostName 203.0.113.10
  User deploy
  Port 2222
  IdentityFile ~/.ssh/prod_key

Host bastion-*
  User admin
  ForwardAgent no
```

Now `ssh prod` works, and so do `scp file prod:/tmp/` and `rsync ... prod:...`.

## 205: How does SSH port forwarding work?

Local forwarding opens a port on your machine and sends traffic through the SSH connection to a host the server can reach.

```bash
# access the remote Postgres on localhost:5433
ssh -L 5433:localhost:5432 user@server

# reach a private database through a bastion host
ssh -L 5433:db.internal:5432 user@bastion

# remote forwarding: expose your local port 3000 on the server's port 8080
ssh -R 8080:localhost:3000 user@server

# SOCKS proxy on local port 1080
ssh -D 1080 user@server
```

Add `-N` to only forward without opening a shell, and `-f` to send it to the background.

## 206: How do you use ProxyJump to reach a server behind a bastion?

```bash
ssh -J admin@bastion.example.com deploy@10.0.1.20
```

Or in `~/.ssh/config`:

```
Host app-private
  HostName 10.0.1.20
  User deploy
  ProxyJump admin@bastion.example.com
```

The connection goes through the bastion, but your keys stay on your machine. This is safer than agent forwarding.

## 207: What are the most useful rsync options?

```bash
rsync -avz src/ user@host:/app/     # archive, verbose, compress
rsync -av --delete src/ dest/       # delete files in dest that are gone from src
rsync -avn --delete src/ dest/      # dry run first, shows what would change
rsync -av --exclude 'node_modules' --exclude '.git' ./ host:/app/
rsync -av --progress big.iso host:/tmp/
rsync -avP host:/backups/ ./backups/   # -P = --partial --progress, resume
```

The trailing slash matters. `src/` copies the contents of src. `src` copies the directory itself, so you get `dest/src/`.

## 208: What are setuid, setgid and the sticky bit?

These are special permission bits.

- **setuid** on an executable: it runs as the file's owner, not as the user who started it. `passwd` uses this to edit `/etc/shadow`. Shows as `s` in the owner execute spot: `-rwsr-xr-x`.
- **setgid** on an executable: runs with the file's group. On a directory: new files inside inherit the directory's group, which is useful for shared folders.
- **sticky bit** on a directory: users can only delete their own files, even if the directory is writable by everyone. `/tmp` has it: `drwxrwxrwt`.

```bash
chmod u+s program     # setuid (4xxx)
chmod g+s shared/     # setgid (2xxx)
chmod +t /shared/tmp  # sticky (1xxx)
chmod 2775 shared/
```

## 209: What is umask?

`umask` sets which permission bits are removed from new files and directories. New files start from 666 and directories from 777, then the umask bits are taken away.

```bash
umask          # 0022 is common
# new files: 644, new directories: 755

umask 077      # private: files 600, directories 700
```

Set it in a script that creates sensitive files, or in a systemd unit with `UMask=0077`.

## 210: What are ACLs and when do you need them?

Normal permissions only allow one owner and one group. Access Control Lists let you give permissions to extra users or groups on the same file.

```bash
setfacl -m u:ben:rw report.txt     # give ben read/write
setfacl -m g:qa:rx /opt/app        # give the qa group read/execute
setfacl -d -m g:qa:rx /opt/app     # default ACL for new files inside
getfacl report.txt                 # show ACLs
setfacl -x u:ben report.txt        # remove ben's entry
```

`ls -l` shows a `+` after the permissions when a file has ACLs.

## 211: How do you safely edit sudo permissions?

Always use `visudo`. It checks the syntax before saving, so a typo cannot lock you out of sudo.

```bash
sudo visudo                         # edit /etc/sudoers
sudo visudo -f /etc/sudoers.d/deploy
```

Example rules:

```
deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart myapp
%devs  ALL=(ALL) ALL
```

The first lets `deploy` restart one service without a password. Prefer small files in `/etc/sudoers.d/` over editing the main file.

## 212: How do you add a user to a group, and why does it not work right away?

```bash
sudo usermod -aG docker anna
```

`-a` means append. Without it, `-G` replaces all the user's extra groups.

Group membership is read when you log in, so your current shell does not get the new group. Log out and in again, or run `newgrp docker` to start a shell with it. `id` shows the groups of your current session.

## 213: How do you customize the Bash prompt?

The prompt is set by `PS1`. Special escape codes add info:

```bash
PS1='\u@\h:\w\$ '                       # user@host:/current/dir$
PS1='\[\e[32m\]\u\[\e[0m\]:\w\$ '        # green user name
```

| Code | Meaning                      |
| ---- | ---------------------------- |
| `\u` | user                         |
| `\h` | short host name              |
| `\w` | current directory            |
| `\W` | last part of the directory   |
| `\$` | `#` for root, `$` for others |
| `\t` | time                         |

Wrap color codes in `\[ \]` so Bash knows they take no space. Without them, long lines wrap wrongly.

## 214: What is PROMPT_COMMAND?

`PROMPT_COMMAND` holds a command that Bash runs right before it shows each prompt. It is used to update the prompt with git info, save history after each command, or set the terminal title.

```bash
PROMPT_COMMAND='history -a'   # write each command to history file right away
```

Since Bash 5.1 it can also be an array, so several tools can add their own entry without overwriting each other.

## 215: How do you configure Bash history?

Put these in `~/.bashrc`:

```bash
HISTSIZE=10000              # lines kept in memory
HISTFILESIZE=20000          # lines kept in ~/.bash_history
HISTCONTROL=ignoreboth      # skip duplicates and lines starting with a space
HISTTIMEFORMAT='%F %T '     # show date and time in `history`
shopt -s histappend         # append instead of overwrite on exit
```

With `ignorespace` (part of `ignoreboth`), starting a command with a space keeps it out of history. That is useful when typing a secret, though it is better to not type secrets at all.

## 216: When should you use a function instead of an alias?

Aliases are simple text replacement and cannot take arguments in the middle. Functions can take arguments, use logic and work in scripts.

```bash
alias ll='ls -lah'      # fine as an alias

mkcd() {                # needs an argument in two places
  mkdir -p "$1" && cd "$1"
}
```

Aliases are not expanded in scripts by default. If you need anything more than a fixed prefix, use a function.

## 217: What do the command and builtin builtins do?

`command name` runs `name` while skipping shell functions and aliases. `builtin name` runs the shell builtin, even if a function has the same name.

```bash
cd() {
  builtin cd "$@" && ls     # call the real cd, then list
}

ls() { echo "wrapped"; }
command ls                  # runs /usr/bin/ls, not the function
```

`command -v` is also the standard way to check if something can be run.

## 218: What does hash do in Bash?

Bash remembers the full path of commands it has found in `PATH`, so it does not search every time. `hash` shows or changes that table.

```bash
hash          # list remembered commands and how often they were used
hash -r       # forget all, search PATH again
```

If you install a new version of a tool into a different directory, Bash may keep running the old one until you run `hash -r` or open a new shell.

## 219: What does exec do?

`exec command` replaces the current shell with the command. There is no new process; the PID stays the same and the shell is gone when the command ends.

```bash
#!/usr/bin/env bash
# docker entrypoint
setup_config
exec node server.js     # node becomes PID 1 and gets signals directly
```

`exec` without a command changes the shell's own file descriptors:

```bash
exec > >(tee -a script.log) 2>&1   # log all further output of this script
exec 3< input.txt                  # open fd 3 for reading
```

## 220: How do you run several jobs in the background and wait for them?

```bash
./build-frontend.sh &
pid1=$!
./build-backend.sh &
pid2=$!

wait "$pid1" || echo "frontend failed"
wait "$pid2" || echo "backend failed"
```

`wait` with a PID returns that job's exit code. `wait` with no arguments waits for all background jobs but always returns 0, so you lose the failures. Save the PIDs if you care about exit codes.

## 221: What is the difference between nohup, disown and &?

- `cmd &` runs in the background but stays tied to the terminal. Closing the terminal sends it SIGHUP and it usually dies.
- `nohup cmd &` starts the command ignoring SIGHUP, so it keeps running after logout.
- `disown` removes a job you already started from the shell's job list, so the shell does not send it SIGHUP on exit.

```bash
long_task &
disown          # or disown %1
```

For anything that should keep running for a long time, use a systemd service or tmux.

## 222: How do you limit how long a command can run?

```bash
timeout 30 curl https://slow.example.com
timeout -s KILL 10 ./script.sh       # send SIGKILL instead of SIGTERM
timeout -k 5 30 ./script.sh          # SIGTERM at 30s, SIGKILL 5s later
echo $?                              # 124 if it timed out
```

`timeout` is part of GNU coreutils. On macOS you get it with `brew install coreutils` as `gtimeout`.

## 223: What does watch do?

`watch` runs a command every 2 seconds and shows the output full screen.

```bash
watch df -h
watch -n 5 'kubectl get pods'
watch -d 'ls -l /tmp'      # highlight changes
```

Quote commands that have pipes so the whole thing is run by `watch`.

## 224: How do you run commands in parallel with xargs?

```bash
cat urls.txt | xargs -n 1 -P 8 curl -sO
find . -name '*.png' -print0 | xargs -0 -n 1 -P "$(nproc)" optipng
```

`-P 8` runs up to 8 processes at once. `-n 1` gives one argument to each. Output from parallel jobs can mix together, so write to separate files if order matters. GNU `parallel` does the same job with more options.

## 225: What does lsof show?

`lsof` (list open files) shows which processes have which files, sockets and devices open. On Linux almost everything is a file, so it answers many questions.

```bash
sudo lsof -i :8080          # who is listening on port 8080
sudo lsof -u www-data       # files opened by a user
sudo lsof +D /var/log       # processes using files under a directory
sudo lsof -p 1234           # files opened by PID 1234
sudo lsof | grep deleted    # deleted files still held open
```

## 226: What is strace and when do you use it?

`strace` shows the system calls a process makes: opening files, reading, writing, network calls and so on. It helps when a program fails without a useful error.

```bash
strace -f -e trace=openat ./app      # which files does it try to open
strace -p 1234                       # attach to a running process
strace -c ls                         # summary count of system calls
strace -f -e trace=network curl example.com
```

A typical find is "No such file or directory" on a config path you did not expect. `strace` slows the program down a lot, so be careful on production.

## 227: What are the useful options of ps?

```bash
ps aux --sort=-%mem | head       # top memory users
ps aux --sort=-%cpu | head       # top CPU users
ps -ef --forest                  # process tree
ps -o pid,ppid,user,etime,cmd -p 1234   # custom columns
ps -eLf                          # include threads
ps -C nginx                      # by command name
```

`aux` is BSD style, `-ef` is standard (System V) style. Both show all processes.

## 228: How do pgrep and pkill work?

They find processes by name or other fields without needing `ps | grep`.

```bash
pgrep nginx              # PIDs
pgrep -a node            # PIDs with full command line
pgrep -f "server.js"     # match the full command line
pgrep -u deploy          # by user
pkill -f "server.js"     # send SIGTERM to matching processes
pkill -HUP nginx         # send a specific signal
```

`ps aux | grep node` also matches the `grep` process itself. `pgrep` does not have that problem.

## 229: What is the difference between SIGTERM, SIGKILL, SIGINT and SIGHUP?

| Signal  | Number | Usual meaning                               | Can be caught? |
| ------- | ------ | ------------------------------------------- | -------------- |
| SIGHUP  | 1      | terminal closed; many daemons reload config | yes            |
| SIGINT  | 2      | Ctrl+C                                      | yes            |
| SIGQUIT | 3      | Ctrl+\, quit with core dump                 | yes            |
| SIGKILL | 9      | kill right now                              | no             |
| SIGTERM | 15     | please stop (default for `kill`)            | yes            |
| SIGSTOP | 19     | pause                                       | no             |
| SIGCONT | 18     | resume                                      | yes            |

Programs can catch SIGTERM to close connections and save state. SIGKILL is handled by the kernel, so the program cannot clean up. Signal numbers can differ on other systems, so use names in scripts.

## 230: How do nice and renice work?

The nice value sets a process's CPU priority, from -20 (highest) to 19 (lowest). The default is 0. Only root can raise priority.

```bash
nice -n 10 ./backup.sh        # start with lower priority
renice -n 15 -p 1234          # change a running process
ionice -c 3 ./backup.sh       # lowest disk I/O priority
```

Useful for backups, builds or reports that should not slow down the main service.

## 231: What does ulimit do?

`ulimit` shows and sets per-process resource limits for the shell and the programs it starts.

```bash
ulimit -a          # show all limits
ulimit -n          # max open files
ulimit -n 65535    # raise it (up to the hard limit)
ulimit -c unlimited  # allow core dumps
ulimit -u          # max user processes
```

These limits do not apply to systemd services. Set them in the unit file instead, for example `LimitNOFILE=65535`.

## 232: Why can df show the disk as full while du shows much less used?

The usual reason is a deleted file that a process still has open. The file name is gone, so `du` does not count it, but the space is not freed until the process closes it. Big log files deleted while the app is running are the common case.

```bash
sudo lsof +L1                 # open files with no links left
sudo lsof | grep '(deleted)'
```

Restart the process, or truncate the file through `/proc`: `: > /proc/<pid>/fd/<fd>`. Other causes: files hidden under a mount point, and reserved blocks for root on ext4.

## 233: What does it mean when you get "No space left on device" but df shows free space?

You might be out of inodes. Each file needs an inode, and a filesystem has a fixed number of them on ext4. Millions of tiny files (cache, sessions, mail queues) can use them all up.

```bash
df -i                    # inode usage per filesystem
sudo find / -xdev -type d -size +1M   # directories with very many entries
for d in /var/*; do echo "$(find "$d" | wc -l) $d"; done | sort -n
```

Delete the small files you do not need, or move them to another filesystem.

## 234: How do you find the biggest files and directories?

```bash
du -h --max-depth=1 / 2>/dev/null | sort -h | tail
sudo du -xh / | sort -h | tail -n 20      # -x stays on one filesystem
find / -xdev -type f -size +500M -exec ls -lh {} + 2>/dev/null
ncdu /                                     # interactive, if installed
```

## 235: What is logrotate?

`logrotate` rotates, compresses and deletes old log files so they do not fill the disk. It usually runs once a day from cron or a systemd timer. Configs live in `/etc/logrotate.conf` and `/etc/logrotate.d/`.

```
/var/log/myapp/*.log {
    daily
    rotate 14
    compress
    delaycompress
    missingok
    notifempty
    create 0640 deploy deploy
    postrotate
        systemctl reload myapp > /dev/null 2>&1 || true
    endscript
}
```

Test it with `sudo logrotate -d /etc/logrotate.d/myapp` (dry run) or force a run with `-f`.

## 236: How do you debug HTTP requests from the command line?

```bash
curl -v https://api.example.com/health          # request and response headers
curl -sS -o /dev/null -w '%{http_code}\n' URL    # only status code
curl -w '@-' -o /dev/null -s URL <<'EOF'
dns: %{time_namelookup}  connect: %{time_connect}  tls: %{time_appconnect}  total: %{time_total}
EOF
curl -X POST -H 'Content-Type: application/json' -d '{"name":"anna"}' URL
curl --resolve api.example.com:443:10.0.0.5 https://api.example.com/   # test a specific IP
```

`-f` makes curl return an error exit code for HTTP 4xx and 5xx, which is what you want in scripts.

## 237: How do you check DNS resolution?

```bash
dig example.com                # full answer
dig +short example.com         # only the IPs
dig example.com MX             # mail records
dig @8.8.8.8 example.com       # ask a specific DNS server
nslookup example.com
getent hosts example.com       # uses the system resolver, including /etc/hosts
resolvectl status              # on systemd-resolved systems
```

`dig` asks DNS directly and skips `/etc/hosts`. `getent` shows what programs on the machine will actually get.

## 238: What is netcat used for?

`nc` (netcat) reads and writes raw TCP or UDP connections. It is a quick tool for testing.

```bash
nc -zv db.internal 5432          # is the port open?
nc -l 9000                       # listen on port 9000
echo "hello" | nc localhost 9000 # send text
printf 'GET / HTTP/1.0\r\n\r\n' | nc example.com 80
```

There are several versions of netcat (OpenBSD, GNU, ncat from nmap) with slightly different flags.

## 239: What are /etc/hosts and /etc/resolv.conf?

`/etc/hosts` maps host names to IPs locally. It is checked before DNS on most systems, so it is used for overrides:

```
127.0.0.1   localhost
10.0.0.5    api.local
```

`/etc/resolv.conf` lists the DNS servers and search domains the system uses. On systems with systemd-resolved or NetworkManager, it is managed for you and edits may be overwritten. The order of hosts versus DNS is set in `/etc/nsswitch.conf`.

## 240: How do you open a port in the firewall?

It depends on the tool your distro uses.

```bash
# Ubuntu: ufw
sudo ufw allow 22/tcp
sudo ufw allow 443/tcp
sudo ufw enable
sudo ufw status verbose

# RHEL/Fedora: firewalld
sudo firewall-cmd --add-service=https --permanent
sudo firewall-cmd --add-port=3000/tcp --permanent
sudo firewall-cmd --reload
```

Both are front ends for the kernel's netfilter, which today usually means nftables. Always allow SSH before enabling a firewall on a remote machine.

## 241: How do you load variables from a .env file in Bash?

```bash
set -a           # export every variable that gets set
source .env
set +a
```

This works for simple `KEY=value` lines. But `source` runs the file as code, so `$(...)` or backticks inside would be executed, and values with spaces need quotes. Only source files you trust. For untrusted files, parse them line by line instead.

## 242: What is ShellCheck?

ShellCheck is a static analysis tool for shell scripts. It finds common bugs like missing quotes, wrong test syntax, useless `cat` and code that does not work in the shell named in the shebang.

```bash
shellcheck deploy.sh
# SC2086: Double quote to prevent globbing and word splitting.
```

It is worth running in CI and in your editor. You can silence one warning on purpose with a comment: `# shellcheck disable=SC2086`.

## 243: How do you make set -x output more useful?

`PS4` is the prefix printed before each traced line. The default is `+ `. You can add the file, line number and function.

```bash
export PS4='+ ${BASH_SOURCE}:${LINENO}:${FUNCNAME[0]:-main}: '
set -x
```

Use single quotes so the values are filled in at trace time. To send trace output to a file instead of stderr, use `BASH_XTRACEFD`:

```bash
exec 5> trace.log
BASH_XTRACEFD=5
set -x
```

## 244: How do you write a portable shell script?

If the script must run in `/bin/sh` (Alpine, Debian's Dash, BusyBox):

- Use `#!/bin/sh` and test with `dash` or `shellcheck -s sh`.
- Use `[ ]`, not `[[ ]]`.
- No arrays, no `local` in strict POSIX (though most shells have it), no `function` keyword.
- Use `$(( ))` for math, not `(( ))` or `let`.
- Use `printf` instead of `echo -e`.
- No `{1..10}`, no `<<<`, no `<(...)`, no `${var^^}`.
- Use `=` in tests, not `==`.

If you need Bash features, say so with `#!/usr/bin/env bash` and make sure Bash is installed.

## 245: Why use #!/usr/bin/env bash instead of #!/bin/bash?

`#!/bin/bash` only works where Bash is at exactly that path. On macOS with Homebrew Bash, NixOS and some BSDs, it is somewhere else. `#!/usr/bin/env bash` runs the first `bash` found in `PATH`.

The downside: the script depends on the user's `PATH`, and you cannot reliably pass more than one option on the shebang line with `env` (Linux passes everything after the interpreter as one argument). Some people prefer the fixed path for system scripts for that reason.

## 246: What are the common exit code conventions?

| Code    | Meaning                                                         |
| ------- | --------------------------------------------------------------- |
| 0       | success                                                         |
| 1       | general error                                                   |
| 2       | wrong usage (bad options or arguments)                          |
| 126     | command found but not executable                                |
| 127     | command not found                                               |
| 128 + N | killed by signal N (130 = Ctrl+C, 137 = SIGKILL, 143 = SIGTERM) |

Exit codes are taken modulo 256, so `exit 256` becomes 0. Keep your own codes between 1 and 125.

## 247: How do you write a simple logging function for scripts?

```bash
log()  { printf '%s [INFO]  %s\n' "$(date '+%F %T')" "$*" >&2; }
warn() { printf '%s [WARN]  %s\n' "$(date '+%F %T')" "$*" >&2; }
die()  { printf '%s [ERROR] %s\n' "$(date '+%F %T')" "$*" >&2; exit 1; }

log "Starting deploy"
[[ -f config.yml ]] || die "config.yml not found"
```

Writing logs to stderr keeps stdout clean for real data, so the script can still be used in a pipe.

## 248: How do you create temporary files safely?

```bash
tmpfile=$(mktemp)                    # /tmp/tmp.XXXXXXXXXX
tmpdir=$(mktemp -d)
tmpfile=$(mktemp /tmp/deploy.XXXXXX)
trap 'rm -rf "$tmpfile" "$tmpdir"' EXIT
```

`mktemp` creates the file with a random name and permissions only you can read. Fixed names like `/tmp/myscript.tmp` can clash with another run of the script or be abused by another user who creates that path first.

## 249: How do you stop two copies of a script from running at the same time?

Use `flock`. It takes a lock on a file, and the kernel releases it when the process ends, even if it crashes.

```bash
#!/usr/bin/env bash
exec 9> /var/lock/backup.lock
if ! flock -n 9; then
  echo "Another backup is running" >&2
  exit 1
fi

# ... do the work ...
```

From cron you can also wrap the command: `flock -n /var/lock/backup.lock /opt/backup.sh`. Checking for a PID file by hand has race conditions and leaves stale files after crashes.

## 250: How do you ask the user for confirmation?

```bash
confirm() {
  local reply
  read -r -p "${1:-Are you sure?} [y/N] " reply
  [[ $reply =~ ^[Yy]([Ee][Ss])?$ ]]
}

if confirm "Delete all logs?"; then
  rm -f logs/*.log
fi
```

Default to "no" for anything dangerous. Add a `--yes` flag so the script can still run without a person, for example in CI.

## 251: How do you print colored output only when writing to a terminal?

```bash
if [[ -t 1 ]]; then
  red=$(tput setaf 1)
  green=$(tput setaf 2)
  reset=$(tput sgr0)
else
  red="" green="" reset=""
fi

echo "${green}OK${reset}"
echo "${red}FAILED${reset}" >&2
```

`[[ -t 1 ]]` is true when stdout is a terminal. When output goes to a file or pipe, color codes would only add junk. Many tools also respect the `NO_COLOR` environment variable.

## 252: How do you check if a script is running as root?

```bash
if (( EUID != 0 )); then
  echo "Please run as root (sudo $0)" >&2
  exit 1
fi
```

`EUID` is the effective user ID, which is 0 when running as root, including through `sudo`. `id -u` gives the same number and also works in `sh`.

## 253: How do you get the directory a script is located in?

```bash
script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
source "$script_dir/lib/common.sh"
```

`$0` can be wrong when the script is sourced. `BASH_SOURCE[0]` always points to the current file. Add `-P` to `pwd` or use `realpath` if you want symlinks resolved.

## 254: How do you trim leading and trailing whitespace from a string?

```bash
s="   hello world   "

trimmed="${s#"${s%%[![:space:]]*}"}"         # remove leading
trimmed="${trimmed%"${trimmed##*[![:space:]]}"}"  # remove trailing
echo "[$trimmed]"   # [hello world]

# simpler, using read (spaces inside are kept)
read -r trimmed <<< "$s"
echo "[$trimmed]"   # [hello world]
```

The `read` trick works because `read` strips leading and trailing `IFS` whitespace.

## 255: How do you loop over files safely?

```bash
shopt -s nullglob
for file in ./*.csv; do
  echo "Processing $file"
  wc -l < "$file"
done
```

Do not loop over `$(ls)` or `$(find ...)`, since names with spaces get split. Use a glob directly, or `find -print0` with `while read -d ''` for recursive searches. The `./` prefix stops names starting with `-` from being read as options.

## 256: What does the -- argument mean?

`--` marks the end of options. Everything after it is treated as a file name or argument, even if it starts with `-`.

```bash
rm -- -weird-file.txt
grep -- "-v" notes.txt
git checkout -- file.txt
```

In scripts, use `--` before user-supplied names: `rm -- "$file"`. Otherwise a file named `-rf` could be read as options.

## 257: How do you find files by time, size and owner?

```bash
find /var/log -name '*.log' -mtime +30          # modified more than 30 days ago
find . -mmin -10                                # modified in the last 10 minutes
find . -newer reference.txt                     # newer than a file
find / -xdev -size +1G 2>/dev/null              # bigger than 1 GB
find . -empty                                   # empty files and directories
find /home -user anna                           # owned by anna
find . -perm -o+w -type f                       # writable by others
find . -name node_modules -prune -o -name '*.js' -print   # skip a directory
```

`-mtime +30` means more than 30 full days. `-mtime -1` means less than one day.

## 258: How do you delete old files with find?

```bash
find /var/backups -name '*.tar.gz' -mtime +14 -print     # check first
find /var/backups -name '*.tar.gz' -mtime +14 -delete    # then delete
```

Run with `-print` first to see what matches. `-delete` must come after the tests; putting it first deletes everything under the path.

## 259: How do you use xargs -I to place the argument in the middle of a command?

```bash
cat hosts.txt | xargs -I{} ssh {} 'uptime'
ls *.jpg | xargs -I{} convert {} {}.png
find . -name '*.bak' -print0 | xargs -0 -I{} mv {} /tmp/old/
```

`-I{}` replaces `{}` with each input line and runs the command once per line. It is slower than the default batch mode but lets you put the argument anywhere.

## 260: How do you work with JSON from the command line?

Use `jq`.

```bash
curl -s https://api.github.com/repos/nodejs/node | jq '.stargazers_count'
jq -r '.dependencies | keys[]' package.json
jq '.items[] | select(.status == "failed") | .name' report.json
jq -n --arg name "$USER" '{user: $name, time: now}'
jq '.version = "2.0.0"' package.json > tmp.json && mv tmp.json package.json
```

`-r` prints raw strings without quotes, which is what you want when saving to a variable. Use `--arg` to pass shell values safely instead of building JSON with string pasting.

## 261: How do you send a JSON POST request with curl?

```bash
curl -sS -X POST https://api.example.com/users \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"name": "Anna", "role": "admin"}'

# build the body safely from variables
body=$(jq -n --arg name "$name" '{name: $name}')
curl -sS --fail-with-body -H 'Content-Type: application/json' -d "$body" "$url"

# newer curl (7.82+) has --json, which sets the headers for you
curl --json '{"name":"Anna"}' https://api.example.com/users
```

## 262: How do you encode data and check file hashes?

```bash
echo -n 'user:pass' | base64          # dXNlcjpwYXNz
echo 'dXNlcjpwYXNz' | base64 -d       # decode
sha256sum release.tar.gz              # compute hash
sha256sum -c release.tar.gz.sha256    # verify against a checksum file
md5sum file                           # fast, but not for security
```

Use `echo -n` so the newline is not encoded. Base64 is encoding, not encryption; anyone can decode it.

## 263: What do declare -i, -a, -A, -x and -p do?

```bash
declare -i n=5      # integer: assignments are evaluated as math
n="n + 2"; echo $n  # 7
declare -a list     # indexed array
declare -A map      # associative array
declare -x VAR=1    # same as export
declare -r CONST=1  # read-only
declare -l lower="HELLO"   # lowercased on assignment: hello
declare -p list map        # print variables in a form you can reuse
declare -f myfunc          # print a function's code
```

`declare -p` is great for debugging, since it shows the exact type and value.

## 264: What is the difference between set and shopt?

Both turn shell options on and off. `set` handles older options, mostly from POSIX, like `-e`, `-u`, `-x`, `-o pipefail`, `-o noclobber`. `shopt` handles Bash-specific options like `nullglob`, `globstar`, `extglob` and `histappend`.

```bash
set -o          # list set options
shopt           # list shopt options
set -o vi       # vi key bindings on the command line
shopt -s nocasematch   # case-insensitive [[ == ]] and case
```

`shopt -o` can also access `set -o` options, but that is rarely used.

## 265: What is the difference between screen and tmux?

Both are terminal multiplexers: they keep shell sessions running on a server after you disconnect, and let you split one terminal into windows and panes. `tmux` is newer and more common today.

```bash
tmux new -s deploy       # new named session
# Ctrl+b d               detach
tmux ls                  # list sessions
tmux attach -t deploy    # reattach
# Ctrl+b %  / Ctrl+b "   split vertical / horizontal
```

Use one before starting a long migration over SSH, so a dropped connection does not kill it.

## 266: What is the /proc filesystem?

`/proc` is a virtual filesystem the kernel creates in memory. It shows info about processes and the system as files.

```bash
cat /proc/cpuinfo
cat /proc/meminfo
cat /proc/loadavg
ls /proc/1234/              # info about PID 1234
cat /proc/1234/cmdline | tr '\0' ' '
ls -l /proc/1234/fd         # its open files
cat /proc/1234/environ | tr '\0' '\n'
cat /proc/sys/fs/file-max
```

Tools like `ps`, `top` and `free` read their data from here.

## 267: What is the format of /etc/passwd and /etc/shadow?

`/etc/passwd` has one user per line with 7 fields separated by `:`:

```
anna:x:1000:1000:Anna Smith:/home/anna:/bin/bash
name:password:UID:GID:comment:home:shell
```

The `x` means the password hash is in `/etc/shadow`, which only root can read. `/etc/passwd` must be readable by everyone so tools can map UIDs to names. Service accounts often use `/usr/sbin/nologin` as the shell so nobody can log in as them.

Use `getent passwd anna` instead of reading the file, since users can also come from LDAP or other sources.

## 268: How do you resolve the real path of a file?

```bash
realpath ./link-to-app       # full path with symlinks resolved
readlink -f ./link-to-app    # same on GNU
readlink ./link-to-app       # only what the link points to, one level
```

Older macOS versions did not have `readlink -f`. Recent macOS has both `readlink -f` and `realpath`.

## 269: How do you see disks and mount a filesystem?

```bash
lsblk                         # disks and partitions as a tree
lsblk -f                      # with filesystem types and UUIDs
sudo blkid                    # UUIDs and types
sudo mount /dev/sdb1 /mnt/data
sudo umount /mnt/data
findmnt                       # all current mounts
```

To mount at boot, add a line to `/etc/fstab` using the UUID, then test with `sudo mount -a` before rebooting. A broken fstab line can stop the machine from booting.

## 270: How do you add swap space?

```bash
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
swapon --show
free -h
```

Swap stops the OOM killer from hitting as quickly on small servers, but heavy swapping makes everything slow.

## 271: How do you use history expansion beyond !!?

```bash
!$          # last argument of the previous command
!^          # first argument of the previous command
!*          # all arguments of the previous command
!-2         # the command before the last one
!git:p      # print the last git command without running it
!!:s/foo/bar/   # rerun last command with first foo replaced by bar
```

History expansion only works in interactive shells. It can surprise you when a string contains `!`, like `echo "Hi!"`. Use single quotes or `set +H` to turn it off.

## 272: What does the fc command do?

`fc` opens your last command (or a range from history) in your editor. When you save and quit, the edited command runs. It is handy for fixing a long command with a typo.

```bash
fc           # edit the last command
fc -l        # list recent history
fc 100 105   # edit and rerun commands 100 to 105
```

`Ctrl+X Ctrl+E` does the same for the line you are typing right now.

## 273: How do you read a password without showing it?

```bash
read -r -s -p "Password: " password
echo
```

`-s` turns off echo. Avoid passing the password on the command line of another program afterwards, because other users can see command lines in `ps`. Pass it through stdin or an environment variable instead, or use a tool's own prompt.

## 274: How do you run a command on many servers?

A simple loop works for a few servers:

```bash
for host in web1 web2 web3; do
  echo "== $host"
  ssh -o ConnectTimeout=5 "$host" 'uptime; df -h /' < /dev/null
done
```

`< /dev/null` keeps `ssh` from eating the stdin of a surrounding `while read` loop. For more servers, run them in parallel with `&` and `wait`, or use a tool like Ansible.

## 275: How do you use a while read loop with ssh without it stopping after the first line?

`ssh` reads from stdin, so inside a `while read` loop it consumes the rest of the input file. The loop then ends after one round.

```bash
while read -r host; do
  ssh -n "$host" hostname      # -n: do not read stdin
done < hosts.txt

# or read the list on a different file descriptor
while read -r host <&3; do
  ssh "$host" hostname
done 3< hosts.txt
```

The same problem happens with other commands that read stdin, like `ffmpeg` or `mysql`.

## 276: What is noclobber?

`set -o noclobber` (or `set -C`) makes `>` refuse to overwrite an existing file. It protects you from wiping a file by accident.

```bash
set -o noclobber
echo hi > existing.txt     # bash: existing.txt: cannot overwrite existing file
echo hi >| existing.txt    # force overwrite
```

It is also a way to create a lock file only if it does not exist yet, since the check and create happen together.

## 277: How do you write output to a file that needs root?

`sudo command > /etc/file` fails because the redirection is done by your own shell before `sudo` runs. Use `tee` or run a whole shell as root.

```bash
echo "vm.swappiness=10" | sudo tee /etc/sysctl.d/99-swap.conf > /dev/null
echo "line" | sudo tee -a /etc/config > /dev/null
sudo sh -c 'echo 1 > /proc/sys/net/ipv4/ip_forward'
```

## 278: How do you check which process uses a lot of CPU or memory?

```bash
top                       # press P for CPU sort, M for memory sort
htop
ps aux --sort=-%cpu | head -n 5
ps aux --sort=-rss | head -n 5
pidstat 1 5               # per-process CPU every second (sysstat package)
```

`RSS` is the real memory a process uses. `VSZ` includes memory it has reserved but not used, so it is often much bigger and less useful.

## 279: What is the load average?

The load average is shown by `uptime` and `top` as three numbers: the average over the last 1, 5 and 15 minutes. It counts processes that are running or waiting for CPU, plus processes in uninterruptible sleep (usually waiting for disk on Linux).

```bash
$ uptime
 10:00:00 up 12 days,  3 users,  load average: 3.12, 2.80, 1.95
$ nproc
4
```

Compare it with the number of CPUs. A load of 3 on 4 cores is fine. A load of 12 on 4 cores means work is waiting. High load with low CPU use usually points to slow disk or network storage.

## 280: How do you search and replace across many files?

```bash
grep -rl 'old-api.example.com' src/ | xargs sed -i 's/old-api\.example\.com/api.example.com/g'

find . -name '*.yml' -print0 | xargs -0 sed -i 's/v1/v2/g'
```

Commit or back up first. Escape `.` in the search pattern since it means "any character" in regex. If the text contains `/`, use another delimiter: `sed -i 's|/old/path|/new/path|g'`.

## 281: How do you compare two directories?

```bash
diff -rq dir1/ dir2/               # only list files that differ
rsync -rvn --delete dir1/ dir2/    # dry run shows what would change
diff <(cd dir1 && find . | sort) <(cd dir2 && find . | sort)   # only names
```

## 282: How do you create a patch and apply it?

```bash
diff -u original.conf new.conf > fix.patch
patch original.conf < fix.patch
patch -p1 < changes.patch         # strip the first path part (a/ b/)
patch -R < fix.patch              # undo a patch
patch --dry-run -p1 < changes.patch
```

In git projects, `git diff` and `git apply` do the same thing and handle renames and binary files.

## 283: What is the difference between source and running a script with bash?

`bash script.sh` or `./script.sh` starts a new process. The script gets a copy of exported variables, and nothing it changes comes back to you.

`source script.sh` runs the lines in the current shell. Variables, functions, `cd` and `set` options change your session. An `exit` inside a sourced file closes your shell, so sourced files should use `return`.

```bash
# check if the file is being sourced
if [[ "${BASH_SOURCE[0]}" != "$0" ]]; then
  echo "sourced"
fi
```

## 284: What are the special parameters $$, $!, $_ and $-?

| Parameter  | Meaning                                                          |
| ---------- | ---------------------------------------------------------------- |
| `$$`       | PID of the current shell (in a subshell, still the parent's PID) |
| `$!`       | PID of the last background job                                   |
| `$_`       | last argument of the previous command                            |
| `$-`       | current shell option flags, like `himBH`                         |
| `$BASHPID` | PID of the current Bash process, which changes in subshells      |

```bash
mkdir -p /tmp/build && cd "$_"
[[ $- == *i* ]] && echo "interactive shell"
```

## 285: How do you check if a string contains a substring?

```bash
if [[ $url == *"example.com"* ]]; then
  echo "matches"
fi

case "$url" in
  *example.com*) echo "matches" ;;
esac
```

Both avoid running `grep`. The `case` form also works in plain `sh`.

## 286: How do you check if a value is a number?

```bash
is_int() {
  [[ $1 =~ ^-?[0-9]+$ ]]
}

is_int "42" && echo "yes"
is_int "4.2" || echo "no"
```

Do not use `[ "$x" -eq "$x" ]` as a check; it prints errors and acts strangely with some input.

## 287: How do you pass an array to a function?

Pass the items as arguments. Inside the function, `"$@"` is the array.

```bash
print_all() {
  local item
  for item in "$@"; do
    echo "- $item"
  done
}

files=("a b.txt" "c.txt")
print_all "${files[@]}"
```

To pass more than one array, pass the array names and use namerefs (`declare -n`) inside.

## 288: How do you create a retry loop for a flaky command?

```bash
retry() {
  local attempts=$1; shift
  local delay=2 n
  for (( n = 1; n <= attempts; n++ )); do
    "$@" && return 0
    echo "Attempt $n/$attempts failed, retrying in ${delay}s..." >&2
    sleep "$delay"
    delay=$(( delay * 2 ))
  done
  return 1
}

retry 5 curl -fsS https://api.example.com/health
```

The delay doubles each time (exponential backoff). Running `"$@"` keeps arguments with spaces intact.

## 289: What is the difference between printenv, env, set and declare?

- `printenv` and `env` show only environment (exported) variables.
- `set` with no arguments shows all shell variables and functions.
- `declare -p` shows all variables with their attributes.
- `declare -F` lists function names only.
- `compgen -v` lists variable names.

## 290: How do you run a script with a clean environment?

```bash
env -i bash --noprofile --norc ./script.sh
env -i HOME="$HOME" PATH=/usr/bin:/bin ./script.sh
```

This is a good way to reproduce "works for me but not in cron or CI" problems, since it removes everything your shell config adds.

## 291: How do you show a progress indicator in a script?

```bash
total=${#files[@]}
i=0
for f in "${files[@]}"; do
  i=$(( i + 1 ))
  printf '\rProcessing %d/%d' "$i" "$total" >&2
  process "$f"
done
printf '\n' >&2

pv big.sql.gz | gunzip | psql mydb    # pv shows progress for pipes
```

`\r` moves the cursor back to the start of the line so the counter updates in place.

## 292: How do you read only specific fields with read?

```bash
while IFS=: read -r user _ uid _ _ home shell; do
  (( uid >= 1000 )) && echo "$user $home $shell"
done < /etc/passwd
```

`_` is just a throw-away variable name. The last variable gets the rest of the line, including any extra separators.

## 293: How do you add a date and time to every line of output?

```bash
./long-job.sh 2>&1 | while IFS= read -r line; do
  printf '%s %s\n' "$(date '+%F %T')" "$line"
done

./long-job.sh 2>&1 | ts '%F %T'     # moreutils package
./long-job.sh 2>&1 | awk '{ print strftime("%F %T"), $0; fflush() }'   # GNU awk
```

## 294: How do you check SSL certificate details from the command line?

```bash
openssl s_client -connect example.com:443 -servername example.com < /dev/null 2>/dev/null \
  | openssl x509 -noout -subject -issuer -dates

openssl x509 -in cert.pem -noout -text
curl -vI https://example.com 2>&1 | grep -E 'expire|subject|issuer'
```

`-servername` sends SNI, which is needed when the server hosts several sites on one IP.

## 295: How do you manage packages with dpkg and rpm directly?

```bash
# Debian / Ubuntu
dpkg -l | grep nginx          # is it installed
dpkg -L nginx                 # files installed by a package
dpkg -S /usr/sbin/nginx       # which package owns a file
sudo dpkg -i package.deb      # install a local .deb (no dependency resolving)
sudo apt install ./package.deb   # install a local .deb with dependencies

# RHEL / Fedora
rpm -qa | grep nginx
rpm -ql nginx
rpm -qf /usr/sbin/nginx
sudo dnf install ./package.rpm
```

## 296: How do you set kernel parameters with sysctl?

```bash
sysctl net.ipv4.ip_forward                # read a value
sudo sysctl -w net.ipv4.ip_forward=1      # set until reboot
echo 'net.ipv4.ip_forward = 1' | sudo tee /etc/sysctl.d/99-forward.conf
sudo sysctl --system                      # reload all config files
```

Common ones for web servers: `net.core.somaxconn`, `fs.file-max`, `vm.swappiness`, `net.ipv4.ip_local_port_range`.

## 297: How do you look at kernel messages?

```bash
sudo dmesg -T             # human readable timestamps
sudo dmesg -T | tail -n 50
sudo dmesg -w             # follow
journalctl -k -b          # kernel messages from this boot
```

Look here for out-of-memory kills, disk errors, USB devices and network driver problems.

## 298: How do you switch between Node, Python or other tool versions in a shell?

Version managers change `PATH` (or use shims) so your shell finds a specific version first.

```bash
nvm install 22 && nvm use 22    # Node
pyenv install 3.13 && pyenv local 3.13
which node                       # shows which one is active
```

They hook into your shell through lines in `~/.bashrc`. That is why they often do not work in cron or systemd, where `.bashrc` is not loaded. Use full paths to the binary there.

## 299: How do you tell if a command is slow because of CPU, disk or network?

Start with:

```bash
top          # high %us or %sy: CPU. high %wa: waiting on disk
vmstat 1     # r (run queue), b (blocked), wa column
iostat -x 1  # disk usage and wait times (sysstat)
time cmd     # if real >> user + sys, it is waiting on something
```

If `real` time is much bigger than `user + sys`, the process spends time waiting on disk, network or locks, not using the CPU. `strace -c` or `strace -T` can show which calls take time.

## 300: How do you write a simple health check script for a web service?

```bash
#!/usr/bin/env bash
set -euo pipefail

url=${1:?Usage: $0 URL}
max_wait=${2:-60}

for (( i = 0; i < max_wait; i += 2 )); do
  code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 5 "$url" || true)
  if [[ $code == 200 ]]; then
    echo "Healthy after ${i}s"
    exit 0
  fi
  sleep 2
done

echo "Service not healthy after ${max_wait}s (last code: $code)" >&2
exit 1
```

The `|| true` stops `set -e` from exiting when curl fails because the server is not up yet.

---

# Advanced Questions (301-450)

## 301: In what order does Bash read its startup files?

For an interactive login shell:

1. `/etc/profile`
2. The first one found of `~/.bash_profile`, `~/.bash_login`, `~/.profile`
3. On logout: `~/.bash_logout`

For an interactive non-login shell: `/etc/bash.bashrc` (on Debian-based systems, a compile-time option) and then `~/.bashrc`.

For a non-interactive shell (a script): no files, except the one named in `BASH_ENV` if it is set.

When Bash is started as `sh`, it acts like a POSIX shell and reads `/etc/profile` and `~/.profile` for login shells, and the file in `ENV` for interactive shells. `bash --noprofile --norc` skips them all. One special case: Bash started by `sshd` to run a remote command (`ssh host cmd`) reads `~/.bashrc` on many builds, even though it is not interactive.

## 302: How does Bash decide what to run when you type a command name?

In this order:

1. If the name has a `/`, run that file directly.
2. Aliases (interactive shells, or with `expand_aliases`)
3. Shell keywords like `if`, `[[`, `function`
4. Functions
5. Builtins like `cd`, `echo`, `printf`
6. The hash table of paths it already found
7. A search through each directory in `PATH`

If nothing is found, Bash runs the `command_not_found_handle` function if defined, then prints "command not found" and returns 127. `type -a name` shows every match in order.

## 303: In what order does Bash perform expansions?

1. Brace expansion: `{a,b}`
2. Tilde expansion: `~`
3. Parameter and variable expansion, arithmetic expansion, command substitution and process substitution (left to right)
4. Word splitting (only on results of unquoted expansions)
5. Pathname expansion (globbing)
6. Quote removal

This order explains many surprises. For example, `{1..$n}` does not work because brace expansion runs before `$n` is expanded. And `$var` containing `*` gets globbed because globbing runs after variable expansion.

## 304: How does word splitting work and when does it happen?

After unquoted parameter expansion, command substitution and arithmetic expansion, Bash splits the result into words using the characters in `IFS`. Spaces, tabs and newlines (the default IFS whitespace) at the start and end are dropped and runs of them count as one separator. Non-whitespace IFS characters each make a separate field, so `a,,b` with `IFS=,` gives three fields including an empty one.

```bash
data="a  b   c"
printf '[%s]\n' $data      # [a] [b] [c]
printf '[%s]\n' "$data"    # [a  b   c]
```

Word splitting does not happen inside double quotes, in variable assignments (`x=$y`), inside `[[ ]]` or in `case` words. It does happen in `for x in $list` and command arguments.

## 305: Why is eval dangerous and what are the alternatives?

`eval` takes a string and runs it as shell code after another round of expansion. If any part of that string comes from user input, file names or network data, an attacker can inject commands.

```bash
name='x; rm -rf ~'
eval "echo $name"     # runs rm -rf ~
```

Alternatives for common uses:

- Dynamic variable names: `declare -n ref=$name`, `${!name}`, or associative arrays
- Building a command: put the arguments in an array and run `"${cmd[@]}"`
- Assigning to a named variable: `printf -v "$name" '%s' "$value"`

If you must use `eval`, quote the data with `printf %q` or `${var@Q}` first.

## 306: How do you build a command with optional arguments safely?

Use an array instead of a string. A string loses the boundaries between arguments and needs `eval` to work right.

```bash
args=(--archive --compress)
[[ $dry_run == true ]] && args+=(--dry-run)
[[ -n $exclude ]] && args+=(--exclude "$exclude")

rsync "${args[@]}" "$src" "$dest"
```

With a string, `opts="--exclude 'my dir'"` passes the quotes as literal characters and splits on the space inside `my dir`.

## 307: How can a script become vulnerable to command injection?

The usual paths:

- Running `eval`, `bash -c` or `ssh host "..."` with unquoted user data in the string
- Unquoted variables that contain globs or start with `-` (option injection)
- `source` on a file that someone else can write
- Using user data in `find -exec sh -c "... {} ..."` instead of passing it as an argument

```bash
# unsafe: file name is part of the code
find . -name '*.txt' -exec sh -c "echo {}" \;

# safe: file name is a separate argument
find . -name '*.txt' -exec sh -c 'echo "$1"' _ {} \;
```

For `ssh`, quote the remote part with `printf %q`: `ssh host "ls -- $(printf %q "$dir")"`.

## 308: What is the fork and exec model and how does Bash use it?

To run an external command, Bash calls `fork()` to make a copy of itself, then the child calls `execve()` to replace itself with the new program. The parent waits for the child unless it was started with `&`.

This is why a child process gets copies of the parent's environment, open file descriptors and working directory, and why changes in the child never come back. Builtins skip `fork` and `exec`, so they are much faster and can change the shell's own state. Modern kernels make `fork` cheap with copy-on-write, but in a tight loop thousands of forks still add up.

## 309: Why do variables set inside a piped while loop disappear?

Each part of a pipeline runs in its own subshell. A `while` loop on the right side of a pipe changes variables in the subshell, and those changes are lost when it ends.

```bash
count=0
cat file.txt | while read -r line; do (( count++ )); done
echo "$count"   # 0

# fix 1: redirect instead of piping
while read -r line; do (( count++ )); done < file.txt

# fix 2: process substitution
while read -r line; do (( count++ )); done < <(grep foo file.txt)

# fix 3: lastpipe (non-interactive shells, or with job control off)
shopt -s lastpipe
grep foo file.txt | while read -r line; do (( count++ )); done
```

## 310: How do ERR traps and set -E work together?

`trap '...' ERR` runs when a command fails under the same rules as `set -e`. By default, the ERR trap is not inherited by functions, command substitutions and subshells. `set -E` (`set -o errtrace`) makes them inherit it.

```bash
set -Eeuo pipefail
trap 'echo "Error on line $LINENO: $BASH_COMMAND (exit $?)" >&2' ERR

deploy() {
  false     # with -E, the trap fires here
}
deploy
```

`BASH_COMMAND` holds the command that failed. Combined with `FUNCNAME` and `BASH_LINENO`, you can print a full stack trace.

## 311: What does inherit_errexit do?

By default, command substitution `$(...)` runs with `set -e` turned off inside it, even if the parent has it on. So a failing command in the middle of `$( )` does not stop the substitution.

```bash
set -e
out=$(false; echo "still ran")
echo "$out"      # still ran

shopt -s inherit_errexit   # Bash 4.4+
out=$(false; echo "still ran")   # now the substitution stops at false
```

The exit code of the assignment is the exit code of the substitution, so with `inherit_errexit` the outer `set -e` also stops the script.

## 312: How do you print a stack trace when a Bash script fails?

```bash
stacktrace() {
  local i
  echo "Error: '$BASH_COMMAND' exited with $1" >&2
  for (( i = 1; i < ${#FUNCNAME[@]}; i++ )); do
    echo "  at ${FUNCNAME[$i]} (${BASH_SOURCE[$i]}:${BASH_LINENO[$((i - 1))]})" >&2
  done
}

set -Eeuo pipefail
trap 'stacktrace $?' ERR
```

`FUNCNAME[i]` is the function at level `i`, `BASH_SOURCE[i]` is the file it is defined in, and `BASH_LINENO[i-1]` is the line inside it that called the next frame down. The `caller` builtin gives the same info one frame at a time.

## 313: How do EXIT traps behave in subshells and with signals?

An EXIT trap runs when the shell that set it exits. A subshell `( ... )` starts with traps reset (except ignored signals), so a trap set in the parent does not run when the subshell ends. You can set a separate trap inside the subshell.

When a Bash script is killed by a signal it does not trap, like SIGTERM or SIGINT, Bash still runs the EXIT trap before dying. Other shells such as Dash do not, so in portable scripts also trap the signals and exit from them:

```bash
cleanup() { rm -rf "$tmp"; }
trap cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' TERM
```

SIGKILL can never be trapped, so nothing runs in that case.

## 314: What happens to child processes when you press Ctrl+C?

The terminal sends SIGINT to the whole foreground process group, not just the shell. So every process in a foreground pipeline gets it.

Bash itself waits for the foreground job to finish. If the child died from SIGINT, Bash also acts as if it got SIGINT and stops the script. If the child caught SIGINT and exited normally (like some editors or `ping`), Bash keeps running the script. That is why some scripts keep going after Ctrl+C on certain commands.

Background jobs started with `&` in a non-interactive script ignore SIGINT and SIGQUIT, so they keep running unless you kill them.

## 315: What are process groups and sessions?

A process group is a set of processes that receive terminal signals together. Bash puts each pipeline (job) in its own process group when job control is on.

A session is a set of process groups tied to one controlling terminal. When the terminal closes, the session leader (usually the login shell) gets SIGHUP and passes it on to its jobs.

```bash
ps -o pid,pgid,sid,tty,cmd
kill -TERM -1234       # negative number: signal the whole process group 1234
setsid ./daemon.sh     # start in a new session, with no controlling terminal
```

Killing the process group is a good way to stop a script together with all its children.

## 316: What is the difference between nohup, disown and setsid?

- `nohup` starts the process with SIGHUP ignored and moves output to `nohup.out` if stdout is a terminal. The process stays in the shell's session and job list.
- `disown` removes a job from Bash's job table so Bash does not send it SIGHUP when the shell exits. It does not change signal handling in the process. If the terminal itself goes away, the process can still get errors writing to it.
- `setsid` starts the process in a new session with no controlling terminal, so terminal hangups cannot reach it at all.

For long-running work, a systemd unit or `systemd-run --user` is better than any of them.

## 317: What are zombie and orphan processes?

A zombie is a process that has exited but whose parent has not yet read its exit status with `wait()`. It uses no CPU or memory, only a PID slot. It shows as `Z` or `<defunct>` in `ps`. Many zombies mean the parent has a bug.

An orphan is a running process whose parent has died. The kernel re-parents it to PID 1 (or a subreaper), which waits for it when it exits.

```bash
ps -eo pid,ppid,stat,cmd | awk '$3 ~ /Z/'
```

You cannot kill a zombie, it is already dead. Kill or fix the parent, and PID 1 will clean them up.

## 318: Why do Docker containers often ignore SIGTERM, and how does exec help?

In a container, the entrypoint process is PID 1. The kernel does not apply default signal actions to PID 1, so if the program has no SIGTERM handler, SIGTERM does nothing. Docker waits 10 seconds and then sends SIGKILL.

A second problem: with `CMD ./start.sh`, Bash is PID 1 and your app is a child. Bash does not forward SIGTERM to the child.

Fixes:

```bash
#!/usr/bin/env bash
# start.sh
set -e
./migrate.sh
exec node server.js     # node replaces bash and becomes PID 1
```

Or use an init like `tini` (`docker run --init`), which forwards signals and reaps zombies. Also use the exec form in the Dockerfile: `CMD ["node", "server.js"]`, not `CMD node server.js`.

## 319: What does wait -n do?

`wait -n` waits for the next background job to finish (any one of them) and returns its exit code. It is useful for running a limited number of jobs at once.

```bash
max=4
for file in *.mp4; do
  while (( $(jobs -rp | wc -l) >= max )); do
    wait -n
  done
  ffmpeg -i "$file" "${file%.mp4}.webm" &
done
wait
```

Since Bash 5.1, `wait -n -p var` also stores the PID of the job that finished in `var`.

## 320: What is a coprocess in Bash?

`coproc` starts a command in the background with two-way pipes to it. You write to its stdin and read from its stdout through file descriptors stored in an array.

```bash
coproc BC { bc -l; }
echo "scale=4; 22/7" >&"${BC[1]}"
read -r result <&"${BC[0]}"
echo "$result"     # 3.1428
kill "$BC_PID"
```

It avoids starting `bc` again for every calculation. It is easy to deadlock if the program buffers output, so it is rarely used. Named pipes or a real language are often simpler.

## 321: What are named pipes and when do you use them?

A named pipe (FIFO) is a special file that acts like a pipe. One process writes to it and another reads from it. Data goes through memory, not disk.

```bash
mkfifo /tmp/logpipe
gzip < /tmp/logpipe > app.log.gz &
./app > /tmp/logpipe
rm /tmp/logpipe
```

Opening a FIFO blocks until both a reader and a writer exist. They are useful for connecting processes that were not started in the same pipeline, or tools that only accept file names.

## 322: How do you open and use custom file descriptors?

```bash
exec 3> out.log          # open fd 3 for writing
echo "line" >&3
exec 3>&-                # close fd 3

exec 4< input.txt        # open fd 4 for reading
read -r first <&4
exec 4<&-

exec 5<> /tmp/file       # open for read and write

exec {logfd}> app.log    # Bash picks a free fd (10+) and stores it in logfd
echo "hi" >&"$logfd"
exec {logfd}>&-
```

The `{var}>` form avoids clashes with fds that other code uses.

## 323: How do you swap stdout and stderr?

```bash
command 3>&1 1>&2 2>&3 3>&-
```

Step by step: fd 3 points to the original stdout, stdout now points to stderr, stderr now points to fd 3 (the original stdout), then fd 3 is closed.

A common use is piping only stderr into a filter:

```bash
command 2>&1 >/dev/null | grep -i error
```

Here stderr goes to the pipe (where stdout pointed) and then stdout goes to `/dev/null`.

## 324: Why does the order of redirections matter?

Redirections are processed left to right, and `2>&1` copies wherever fd 1 points at that moment.

```bash
cmd > file 2>&1    # 1 -> file, then 2 -> file. Both in file.
cmd 2>&1 > file    # 2 -> terminal (where 1 was), then 1 -> file.
```

The same logic applies to pipes. The pipe is set up before the redirections on the command, so `cmd 2>&1 | less` sends both streams to `less`.

## 325: What is /dev/tcp in Bash?

Bash treats `/dev/tcp/host/port` and `/dev/udp/host/port` in redirections as network connections. These are not real files; Bash handles them itself (when compiled with that feature, which most builds are).

```bash
exec 3<>/dev/tcp/example.com/80
printf 'GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n' >&3
cat <&3

# quick port check without nc
if timeout 2 bash -c '>/dev/tcp/db.internal/5432' 2>/dev/null; then
  echo "port open"
fi
```

It is handy in minimal containers without `curl` or `nc`. Security tools also watch for it, since it is used in reverse shells.

## 326: How do you write a file atomically?

Write to a temporary file on the same filesystem, then `mv` it into place. `rename()` within one filesystem is atomic, so readers see either the old file or the new one, never a half-written one.

```bash
tmp=$(mktemp "${target}.XXXXXX")
trap 'rm -f "$tmp"' EXIT
generate_config > "$tmp"
chmod 644 "$tmp"
mv -f "$tmp" "$target"
```

`mktemp` in `/tmp` might be a different filesystem, which turns `mv` into copy and delete. That is why the temp file is created next to the target.

## 327: What is a TOCTOU race and how does it apply to shell scripts?

TOCTOU means "time of check to time of use". The script checks something, then acts on it, and the state changes in between.

```bash
# race: another process could create the file between the test and the write
if [[ ! -e /tmp/report ]]; then
  echo data > /tmp/report
fi
```

In `/tmp`, an attacker could create a symlink at that path pointing to a file you own, and your script would overwrite it. Fixes: use `mktemp`, use `set -o noclobber` for create-if-not-exists, use `flock` around critical sections, and use `mkdir` for locks since it is atomic.

## 328: How do you use flock to protect only part of a script?

```bash
lockfile=/var/lock/myapp-deploy.lock

{
  flock -w 30 9 || { echo "Could not get lock" >&2; exit 1; }
  # only one process at a time runs this block
  update_symlink
  restart_service
} 9> "$lockfile"
```

`-w 30` waits up to 30 seconds. `-n` fails right away. `-s` takes a shared (read) lock. The lock is released when fd 9 is closed at the end of the block.

## 329: What are namerefs and when are they useful?

A nameref (`declare -n` or `local -n`, Bash 4.3+) makes a variable act as an alias for another variable whose name you give at runtime. It is the clean way to pass arrays by reference or return values without a subshell.

```bash
add_item() {
  local -n list=$1
  list+=("$2")
}

fruits=()
add_item fruits apple
add_item fruits banana
echo "${fruits[@]}"   # apple banana
```

Watch out for name clashes: if the caller's variable is also called `list`, the nameref points to itself and fails. Use unusual names inside functions, like `_ref_list`.

## 330: What is dynamic scoping in Bash and how can it bite you?

Bash looks up variables in the call stack at runtime, not where the function was written. A function sees the `local` variables of whatever function called it.

```bash
outer() {
  local config="outer"
  inner
}
inner() {
  echo "$config"   # prints outer, even though inner did not define it
}
config="global"
outer
inner              # prints global
```

This means a helper function can change a caller's local by accident if it assigns to the same name without `local`. Always declare variables `local` in functions.

## 331: How do you export a function to child processes?

```bash
greet() { echo "Hello $1"; }
export -f greet
bash -c 'greet Anna'         # works
find . -name '*.txt' -exec bash -c 'greet "$1"' _ {} \;
```

Bash passes the function in an environment variable named like `BASH_FUNC_greet%%`. Only Bash children can use it, not `sh`. This mechanism was the source of the Shellshock bug.

## 332: What was Shellshock?

Shellshock (CVE-2014-6271 and related bugs) was a 2014 flaw in how Bash imported functions from environment variables. Bash would run any code that came after a function definition in an environment variable.

```bash
env x='() { :;}; echo vulnerable' bash -c 'echo test'
```

Any service that put attacker-controlled data into environment variables and then started Bash (CGI scripts, some DHCP clients, SSH forced commands) allowed remote code execution. The fix changed function export to use special prefixed names and stopped parsing trailing code. It is a good reminder to not trust environment data and to keep Bash patched.

## 333: How do ${var@Q} and printf %q help with quoting?

Both produce a version of a value that can be safely reused as shell input.

```bash
file="it's a file; rm -rf"
printf '%q\n' "$file"      # it\'s\ a\ file\;\ rm\ -rf
echo "${file@Q}"           # 'it'\''s a file; rm -rf'

ssh host "cat -- ${file@Q}"
```

`${var@Q}` is from Bash 4.4. Other transformations: `@U` (uppercase), `@L` (lowercase), `@E` (expand escapes like `\n`), `@A` (assignment statement), `@a` (attributes), `@P` (expand like a prompt).

## 334: What is new in Bash 5.3?

Bash 5.3 was released in July 2025. The main changes:

- A new command substitution form `${ command; }` that runs in the current shell, without a subshell, and captures stdout.
- `${| command; }` runs in the current shell and expands to the value of `REPLY` that the command sets.
- `GLOBSORT` variable to control how glob results are sorted (by name, size, mtime and so on).
- `source -p PATH file` to search a custom path for the file.
- `read -E` to use Readline with completion while reading input.
- `compgen -V varname` to store completions into an array.
- An error is now printed when a regex in `[[ =~ ]]` fails to compile.

## 335: How does the new ${ command; } substitution differ from $( )?

`$( )` runs the command in a forked subshell, so variable changes inside are lost and you pay the cost of a fork. `${ command; }` (Bash 5.3) runs in the current shell and still captures its output.

```bash
count=0
out=${ count=5; echo "done"; }
echo "$out $count"     # done 5

get_name() { REPLY="anna"; }
name=${| get_name; }   # value of REPLY, no output capture needed
```

The opening `${` must be followed by a space, tab, newline or `|`, and the command must end with `;` or a newline before `}`. Scripts that use it need Bash 5.3, so check `BASH_VERSINFO` if you ship to older systems.

## 336: How do you measure time precisely inside a script?

```bash
start=$EPOCHREALTIME        # seconds with microseconds, Bash 5.0+
do_work
end=$EPOCHREALTIME
echo "Took $(awk -v s="$start" -v e="$end" 'BEGIN { printf "%.3f", e - s }')s"

echo "$EPOCHSECONDS"        # whole seconds, no date call needed
SECONDS=0; do_work; echo "Took ${SECONDS}s"

TIMEFORMAT='%R seconds'
time do_work
```

`EPOCHREALTIME` uses the locale's decimal separator, which can be a comma in some locales. Set `LC_NUMERIC=C` if you parse it.

## 337: Why does set -u break on empty arrays in older Bash?

Before Bash 4.4, `"${arr[@]}"` on an empty array counted as an unset variable under `set -u` and stopped the script. macOS still ships Bash 3.2, so this still shows up.

```bash
set -u
args=()
cmd "${args[@]}"                 # error in Bash < 4.4
cmd ${args[@]+"${args[@]}"}      # works everywhere
```

The `${var+word}` form expands to `word` only if `var` is set, which avoids the error.

## 338: What arithmetic pitfalls exist in Bash?

- Numbers with a leading zero are octal: `$(( 08 ))` is an error, `$(( 010 ))` is 8. Dates like `09` break. Use `$(( 10#$day ))`.
- Only 64-bit signed integers. Overflow wraps around silently.
- Division truncates toward zero: `$(( -7 / 2 ))` is -3.
- Inside `$(( ))`, variable values are evaluated as expressions recursively, which can run code if the value comes from user input like `a[$(rm -rf ~)]`.
- `(( x ))` returns 1 when `x` is 0, which triggers `set -e`.

```bash
month=$(date +%m)        # "09"
next=$(( 10#$month + 1 ))
```

## 339: Why can arithmetic on untrusted input be a security problem?

In `$(( ))`, `(( ))`, `let`, `declare -i` and array indexes, Bash evaluates variable values as arithmetic expressions. An array subscript inside that value can contain a command substitution that runs.

```bash
input='x[$(id >&2)]'
echo $(( input + 1 ))     # runs id
```

Validate numbers with a regex before using them in math:

```bash
[[ $input =~ ^[0-9]+$ ]] || die "not a number"
```

The same applies to `[[ $a -eq $b ]]`, which also evaluates arithmetic.

## 340: How does locale affect sort, grep and string comparison?

The locale (`LANG`, `LC_ALL`, `LC_COLLATE`) changes the sort order of characters and what ranges like `[a-z]` match. In `en_US.UTF-8`, `sort` ignores case and punctuation in some ways, and `[a-z]` may match uppercase letters in some tools.

```bash
printf '%s\n' b B a A | sort             # a A b B (locale order)
printf '%s\n' b B a A | LC_ALL=C sort    # A B a b (byte order)
```

`LC_ALL=C` gives byte order, which is predictable and much faster for `sort` and `grep` on big files. Use it when you need stable results across machines, and use `[[:lower:]]` style classes when you need language rules.

## 341: Why is a Bash while-read loop slow on large files, and what should you use instead?

Bash `read` reads input one byte at a time from pipes (it cannot read ahead without losing data), and each loop iteration runs in the interpreter. Calling an external command inside the loop adds a fork per line.

```bash
# slow: forks cut for every line
while read -r line; do echo "$line" | cut -d, -f2; done < big.csv

# fast: one process does the whole file
cut -d, -f2 big.csv
awk -F, '{ sum += $3 } END { print sum }' big.csv
```

For millions of lines, `awk`, `sed`, `grep` or a real programming language are often 100 times faster. Use Bash loops for control logic, not for data processing.

## 342: How do you avoid unnecessary subshells and external commands in hot loops?

Replace common external calls with builtins and parameter expansion:

| Instead of                   | Use                        |
| ---------------------------- | -------------------------- |
| `$(basename "$f")`           | `${f##*/}`                 |
| `$(dirname "$f")`            | `${f%/*}`                  |
| `$(echo "$s" \| tr a-z A-Z)` | `${s^^}`                   |
| `$(expr $a + 1)`             | `$(( a + 1 ))`             |
| `$(cat file)`                | `$(< file)`                |
| `$(date +%s)`                | `$EPOCHSECONDS`            |
| `echo "$x" \| grep -q foo`   | `[[ $x == *foo* ]]`        |
| `x=$(func)`                  | `printf -v x` or a nameref |

Each `$( )` costs a fork. In a loop over 10,000 items, removing two of them per item can save several seconds.

## 343: How do you run a fixed number of parallel jobs in pure Bash?

```bash
max_jobs=$(nproc)
fail=0

for url in "${urls[@]}"; do
  if (( $(jobs -rp | wc -l) >= max_jobs )); then
    wait -n || fail=1
  fi
  curl -fsS -o "/tmp/$(basename "$url")" "$url" &
done

while (( $(jobs -rp | wc -l) > 0 )); do
  wait -n || fail=1
done
exit "$fail"
```

This keeps at most `max_jobs` running and still collects failures. `xargs -P` or GNU `parallel` do the same with less code if the work fits a single command.

## 344: How do you profile a slow Bash script?

```bash
# timestamped trace of every command
PS4='+ $EPOCHREALTIME ${BASH_SOURCE}:${LINENO}: '
bash -x script.sh 2> trace.log

# then look for big gaps between timestamps
awk '{ t = $2; if (p) printf "%.4f %s\n", t - p, prev; p = t; prev = $0 }' trace.log | sort -rn | head
```

Also try `time` on sections, `strace -c -f bash script.sh` to count system calls (many `clone` calls mean many forks), and `perf` for very CPU-heavy cases. Usually the cause is an external command in a loop.

## 345: What does "Argument list too long" mean and how do you fix it?

The kernel limits the total size of arguments and environment passed to `execve()` (`ARG_MAX`, usually 2 MB on Linux, and there is also a limit per single argument). A glob like `rm *.log` in a directory with 500,000 files expands to more than that.

```bash
getconf ARG_MAX

find . -maxdepth 1 -name '*.log' -delete
find . -maxdepth 1 -name '*.log' -print0 | xargs -0 rm
printf '%s\0' *.log | xargs -0 rm      # printf is a builtin, so no limit
```

The limit only applies to running external programs. Builtins like `printf` and `for` loops can handle the full list.

## 346: Can a Bash variable hold binary data or null bytes?

No. Bash strings are C strings, so a null byte ends the value. Command substitution drops null bytes (with a warning in Bash 4.4+) and also drops trailing newlines.

```bash
data=$(head -c 10 /dev/urandom)    # warning: ignored null byte in input
```

For binary data, keep it in files or pipes and pass file names around. Use `base64` or `xxd` if you need to store it in a variable.

## 347: How do you keep trailing newlines in command substitution?

Command substitution removes all trailing newlines. To keep them, add a marker character and remove it after.

```bash
out=$(printf 'line\n\n\n'; echo x)
out=${out%x}
printf '%s' "$out" | od -c
```

With Bash 5.3, `${ cmd; }` behaves the same way about trailing newlines, so the trick is still needed there.

## 348: How does ${#var} behave with multibyte characters?

`${#var}` counts characters according to the current locale. In a UTF-8 locale, `é` counts as 1. In the C locale, it counts bytes, so `é` is 2.

```bash
s="héllo"
echo "${#s}"                     # 5 in a UTF-8 locale
LC_ALL=C bash -c 's="héllo"; echo ${#s}'   # 6
printf '%s' "$s" | wc -c         # 6 bytes
```

The same rule applies to substring `${s:0:2}` and `printf` widths. Be careful when slicing strings for protocols that count bytes.

## 349: Why do scripts with Windows line endings fail and how do you fix them?

Files edited on Windows can end lines with `\r\n` (CRLF). Bash treats the `\r` as part of the line, so you get errors like:

```
/usr/bin/env: 'bash\r': No such file or directory
$'\r': command not found
```

Fix and prevent it:

```bash
file script.sh                 # shows "with CRLF line terminators"
dos2unix script.sh
sed -i 's/\r$//' script.sh
git config core.autocrlf input
```

A `.gitattributes` line `*.sh text eol=lf` keeps shell scripts with LF line endings for everyone.

## 350: How do you tell if a script is running interactively or with a terminal?

```bash
[[ $- == *i* ]]   # the shell itself is interactive
[[ -t 0 ]]        # stdin is a terminal
[[ -t 1 ]]        # stdout is a terminal
[[ -p /dev/stdin ]]   # stdin is a pipe
```

Scripts are never interactive in the `$-` sense, but stdin and stdout can still be a terminal. Use `-t 0` to decide whether to prompt the user, and `-t 1` to decide whether to use colors or progress bars.

## 351: Why does a script with set -o pipefail sometimes fail with exit code 141?

141 is 128 + 13, which means a process was killed by SIGPIPE. This happens when the reader of a pipe exits early, for example `head`, and the writer then tries to write more.

```bash
set -o pipefail
yes | head -n 1      # yes gets SIGPIPE, pipeline returns 141
```

Without `pipefail` nobody notices because only `head`'s exit code counts. With it, the pipeline fails. Fixes: avoid the early exit (`awk 'NR==1'` reads everything), ignore that specific code, or turn off `pipefail` for that one pipeline.

```bash
first=$(set +o pipefail; long_output | head -n 1)
```

## 352: What do exit codes 126 and 127 tell you?

127 means the command was not found: a typo, missing package, wrong `PATH`, or (a confusing case) the script's shebang interpreter does not exist, like `#!/bin/bash\r` from CRLF line endings.

126 means the file was found but could not be run: missing execute permission, it is a directory, or the filesystem is mounted with `noexec`.

```bash
ls -l ./script.sh                 # check the x bit
head -1 ./script.sh | od -c       # check the shebang for \r
findmnt -no OPTIONS /tmp          # check for noexec
```

## 353: Why are aliases not expanded in scripts and functions?

Aliases are expanded when a line is read, not when it runs, and only when `expand_aliases` is on, which is the default only for interactive shells. In a script, `alias ll='ls -l'` followed by `ll` gives "command not found".

```bash
shopt -s expand_aliases
alias ll='ls -l'
ll        # works now, but only on lines read after the alias was defined
```

A function body is read all at once, so an alias defined inside the same function is not used there. Use functions instead of aliases in scripts.

## 354: How can CDPATH break scripts?

If `CDPATH` is set (some people export it in their shell config), `cd name` looks for `name` in those directories first. A script that does `cd build` might end up in `~/projects/build` instead of `./build`, and `cd` prints the new path to stdout, which can corrupt captured output.

```bash
unset CDPATH                 # at the top of scripts
cd -- "./build"              # an explicit ./ skips CDPATH
dir=$(cd -- "$d" && pwd)     # without unset, this can capture two paths
```

## 355: How does sudo handle the environment and PATH?

By default, `sudo` resets the environment (`env_reset`) and sets `PATH` to `secure_path` from sudoers. So your exported variables are gone and tools in `~/.local/bin` or nvm's directories are not found.

```bash
sudo env | sort
sudo -E ./script.sh          # keep the environment (if sudoers allows it)
sudo VAR=value ./script.sh   # pass one variable (if allowed)
sudo "$(command -v node)" app.js   # use the full path
```

This is a security feature. Letting users pass `LD_PRELOAD`, `PATH` or `PYTHONPATH` to a root command would let them run any code as root.

## 356: Why are setuid shell scripts ignored on Linux?

The Linux kernel ignores the setuid bit on scripts with a shebang. There is a race between the kernel opening the file to read the shebang and the interpreter opening it again by name. An attacker could swap the file in between and get their own script run as root. Shells also read many environment variables that a user controls.

If a script needs root, give a user permission to run it through `sudo` with a specific rule in sudoers, and make sure the script and its directory are only writable by root.

## 357: How can PATH hijacking happen and how do you prevent it in scripts?

If a script calls commands by name and an attacker controls a directory early in `PATH` (or `PATH` includes `.` or an empty entry), the attacker's `ls` or `curl` runs instead.

Prevent it:

- Set `PATH` at the top of scripts that run with privileges: `PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin`.
- Never put `.` or writable directories in root's `PATH`.
- Watch out for empty entries like `PATH=:/usr/bin` or a trailing `:`, which mean the current directory.
- In sudoers, keep `secure_path`.

## 358: How do secrets leak in shell usage and how do you avoid it?

Common leaks:

- Command line arguments are visible to every user in `ps` and `/proc/<pid>/cmdline`: `mysql -pSecret`, `curl -u user:pass`.
- Shell history saves typed secrets to `~/.bash_history`.
- `set -x` prints expanded values, including tokens, to logs.
- Environment variables can be read through `/proc/<pid>/environ` by the same user and root, and are passed to every child.
- Temp files created with the default umask can be readable by others.

Better options: read secrets from files with `600` permissions, pass them on stdin, use tool-specific config files (`~/.pgpass`, `~/.netrc`, `curl -K`), turn off tracing around secret code with `set +x`, and use a secret manager.

## 359: What are the risks of SSH agent forwarding?

With `ssh -A`, the remote server can use your local SSH agent to sign logins as you, for as long as you are connected. Anyone with root on that server can use your agent socket to log into other machines with your keys.

Safer options:

- `ProxyJump` (`ssh -J`) to reach hosts behind a bastion without exposing the agent.
- Only forward to hosts you fully trust.
- `ssh-add -c` to require confirmation for each use of a key.
- Separate keys for separate environments.

## 360: How do you harden SSH on a server?

In `/etc/ssh/sshd_config` (or a file in `/etc/ssh/sshd_config.d/`):

```
PermitRootLogin no
PasswordAuthentication no
KbdInteractiveAuthentication no
PubkeyAuthentication yes
AllowUsers deploy admin
MaxAuthTries 3
```

Then check and reload, while keeping your current session open in case you lock yourself out:

```bash
sudo sshd -t && sudo systemctl reload ssh   # the unit is sshd on RHEL
```

Add rate limiting with `fail2ban` or firewall rules, keep the server patched, and limit access to known IPs or a VPN where possible.

## 361: Why does SSH refuse to use a private key with "bad permissions"?

SSH refuses keys and config files that other users could read or change, because that would let them steal or replace your key.

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519 ~/.ssh/config ~/.ssh/authorized_keys
chmod 644 ~/.ssh/id_ed25519.pub
```

On the server, `sshd` with `StrictModes yes` also rejects `authorized_keys` if the home directory or `~/.ssh` is writable by the group or others. Check `/var/log/auth.log` or `journalctl -u ssh` for the exact reason.

## 362: How can symlink attacks happen in /tmp?

`/tmp` is writable by everyone. If a root script writes to a predictable path like `/tmp/backup.log`, a normal user can create a symlink at that path pointing to `/etc/shadow` first. The root script then follows the link and overwrites the target.

Protections:

- Use `mktemp`, which creates a new file with a random name and fails if it exists.
- Use per-service private temp dirs: `PrivateTmp=yes` in systemd units.
- Linux has `fs.protected_symlinks=1` on by default in most distros, which stops following symlinks in sticky world-writable directories unless the owner matches.

## 363: What is an inode and what does it store?

An inode is the data structure that describes a file: type, permissions, owner, group, size, timestamps, link count and pointers to the data blocks. It does not store the file name. Names live in directories, which map names to inode numbers.

```bash
ls -i file.txt
stat file.txt
df -i
```

This explains hard links (two names, one inode), why `mv` on the same filesystem is instant (only the directory entry changes), and why a deleted file can still use space (the inode stays while a process has it open).

## 364: What are the three timestamps of a file?

- `atime` (access): last read. Many systems mount with `relatime`, which updates it only sometimes to save writes.
- `mtime` (modify): last change to the content.
- `ctime` (change): last change to the inode, like permissions, owner or link count. Also updated when content changes. You cannot set it by hand.

Some filesystems also store a birth time (`btime`), shown by `stat` on newer systems. `ls -l` shows mtime by default, `ls -lu` shows atime and `ls -lc` shows ctime.

## 365: How do mount options like noexec, nosuid and nodev help security?

- `noexec` stops running binaries directly from that filesystem.
- `nosuid` ignores setuid and setgid bits there.
- `nodev` ignores device files there.

They are common for `/tmp`, `/var/tmp`, `/dev/shm` and removable media.

```
tmpfs  /tmp  tmpfs  defaults,noexec,nosuid,nodev  0 0
```

`noexec` is not a strong barrier: `bash /tmp/script.sh` still works because Bash reads the file instead of executing it. It mainly stops dropped binaries from running directly.

## 366: What are Linux capabilities?

Capabilities split root's power into separate pieces, so a program can get only what it needs instead of full root. Examples: `CAP_NET_BIND_SERVICE` (bind ports below 1024), `CAP_NET_ADMIN`, `CAP_SYS_ADMIN`, `CAP_CHOWN`.

```bash
sudo setcap 'cap_net_bind_service=+ep' /usr/local/bin/myserver
getcap /usr/local/bin/myserver
capsh --print              # capabilities of the current shell
```

In systemd units, `AmbientCapabilities=CAP_NET_BIND_SERVICE` with a non-root `User=` does the same. Containers drop most capabilities by default, which is why some things fail inside them.

## 367: What are cgroups and namespaces?

They are the kernel features that containers are built on.

- **Namespaces** isolate what a process can see: PID (own process tree), mount (own filesystem view), network (own interfaces and ports), UTS (own hostname), IPC, user (own UID mapping) and cgroup.
- **cgroups** (control groups, v2 on modern systems) limit and measure what a process can use: CPU, memory, disk I/O and number of processes.

```bash
lsns                         # list namespaces
systemd-cgls                 # cgroup tree
systemd-cgtop                # resource use per cgroup
unshare --pid --fork --mount-proc bash   # a shell in a new PID namespace
```

systemd puts every service in its own cgroup, which is how `MemoryMax=` and `CPUQuota=` work.

## 368: What does the OOM killer do and how do you investigate it?

When the system runs out of memory and cannot free any, the kernel's out-of-memory killer picks a process (usually the one using the most memory, adjusted by `oom_score_adj`) and kills it with SIGKILL.

```bash
sudo dmesg -T | grep -i -E 'killed process|out of memory'
journalctl -k | grep -i oom
cat /proc/<pid>/oom_score
echo -1000 | sudo tee /proc/<pid>/oom_score_adj   # never kill this one
```

In a container or a systemd unit with `MemoryMax`, the cgroup has its own OOM limit, so the app can be killed while the host still has free memory. Exit code 137 often means OOM kill.

## 369: How do you read the output of free and what is buff/cache?

```
               total        used        free      shared  buff/cache   available
Mem:           15Gi       4.2Gi       1.1Gi       300Mi        10Gi        10Gi
```

- `used`: memory used by processes.
- `buff/cache`: memory the kernel uses to cache files and disk blocks. It is given back when programs need it.
- `free`: memory not used for anything, which is often small and that is fine.
- `available`: an estimate of how much can be given to new programs without swapping. This is the number to watch.

If `available` is low and swap is growing, the machine really needs more memory.

## 370: What is swappiness?

`vm.swappiness` (0 to 200, default usually 60) tells the kernel how willing it is to swap out process memory compared to dropping file cache. Lower values keep app memory in RAM longer.

```bash
cat /proc/sys/vm/swappiness
sudo sysctl vm.swappiness=10
```

Databases and latency-sensitive apps often use low values like 1 to 10. Setting it to 0 does not fully turn off swap; use `swapoff` for that.

## 371: How do you use vmstat and iostat to find bottlenecks?

```bash
vmstat 1
#  r  b   swpd   free  buff  cache   si   so    bi    bo   in   cs us sy id wa st
```

- `r` greater than CPU count: CPU bound.
- `b` above 0 for long: processes blocked on I/O.
- `si`/`so` above 0: swapping, low memory.
- `wa` high: CPU waiting for disk.
- `st` high: a VM losing CPU time to other VMs on the same host.

```bash
iostat -xz 1
```

For each disk, look at `%util` (near 100% means saturated, though fast SSDs can go higher), `r_await`/`w_await` (latency in ms) and `aqu-sz` (queue size).

## 372: How do you check open file descriptor usage and limits?

```bash
ls /proc/<pid>/fd | wc -l           # fds open by a process
cat /proc/<pid>/limits | grep 'open files'
cat /proc/sys/fs/file-nr            # allocated, unused, max for the whole system
ulimit -Sn; ulimit -Hn              # soft and hard limits of this shell
```

"Too many open files" (EMFILE) means the process hit its own limit. Raise it in the systemd unit (`LimitNOFILE=`), in `/etc/security/limits.conf` for login sessions, or fix the leak if the count keeps growing. ENFILE means the system-wide limit was hit.

## 373: How do you find which process is using a port and why the port stays busy after a restart?

```bash
sudo ss -tlnp 'sport = :8080'
sudo lsof -iTCP:8080 -sTCP:LISTEN
sudo fuser -v 8080/tcp
```

If nothing is listening but your app still gets "Address already in use", old connections may be in `TIME_WAIT`. Servers should set `SO_REUSEADDR` on their listening socket, which most frameworks do. Also check for a child process that inherited the socket and is still running after the parent died.

## 374: How do systemd unit dependencies work?

Ordering and requirement are separate things.

- `After=` / `Before=` only control start order.
- `Wants=` starts another unit too, but does not fail if it fails.
- `Requires=` starts another unit and stops this one if the other one stops or fails to start.
- `BindsTo=` is stronger: stop when the other one stops for any reason.
- `PartOf=` passes restarts and stops from the other unit to this one.

```ini
[Unit]
Requires=postgresql.service
After=postgresql.service
```

`Requires=` without `After=` starts both at the same time. You almost always want both. `After=network-online.target` plus `Wants=network-online.target` waits for the network to be up.

## 375: What are the systemd service types and when do you use each?

- `simple` (default): the process in `ExecStart` is the service. systemd thinks it is started right away.
- `exec`: like `simple`, but systemd waits until the binary was actually run, so a missing binary fails the start.
- `forking`: the program forks and the parent exits, the old daemon style. Use `PIDFile=`.
- `oneshot`: runs to completion, for setup tasks. Often with `RemainAfterExit=yes`.
- `notify`: the program tells systemd when it is ready with `sd_notify`. Best for real readiness.
- `dbus` and `idle` are less common.

For most Node, Python or Go apps that stay in the foreground, use `simple` or `exec`.

## 376: How do you configure restart behavior and avoid restart loops in systemd?

```ini
[Unit]
StartLimitIntervalSec=300
StartLimitBurst=5

[Service]
Restart=on-failure
RestartSec=5s
```

`Restart=on-failure` restarts on non-zero exit, signal kill or timeout. `always` restarts even on clean exit. If the service fails 5 times in 300 seconds, systemd stops trying and marks it failed. Run `systemctl reset-failed myapp` to clear that.

For apps that crash right away, look at `systemctl status` and `journalctl -u myapp -b` before raising the limits.

## 377: How do you harden a systemd service?

systemd can sandbox a service with a few lines:

```ini
[Service]
User=myapp
NoNewPrivileges=yes
ProtectSystem=strict
ProtectHome=yes
PrivateTmp=yes
PrivateDevices=yes
ReadWritePaths=/var/lib/myapp
CapabilityBoundingSet=
RestrictAddressFamilies=AF_INET AF_INET6 AF_UNIX
MemoryMax=512M
```

`systemd-analyze security myapp.service` gives a score and lists what else can be locked down. `DynamicUser=yes` creates a throwaway user for the service.

## 378: What is socket activation?

With socket activation, systemd opens the listening socket itself and starts the service only when the first connection comes in. The service gets the already-open socket.

Benefits: faster boot, services start on demand, and you can restart the service without dropping connections waiting in the queue. You need a `.socket` unit next to the `.service`, and the app must accept sockets from systemd (fd 3 and up, listed in `LISTEN_FDS`).

## 379: What happens during the Linux boot process?

1. Firmware (UEFI or BIOS) runs hardware checks and starts the boot loader.
2. The boot loader (GRUB, systemd-boot) loads the kernel and an initramfs into memory.
3. The kernel sets up hardware and memory, then runs `/init` from the initramfs.
4. The initramfs loads drivers needed to find and mount the real root filesystem (disk, RAID, LVM, encryption).
5. It switches to the real root and runs `/sbin/init`, which is systemd on most distros.
6. systemd starts units in parallel to reach the default target, like `multi-user.target` or `graphical.target`.

```bash
systemd-analyze                  # time spent in each stage
systemd-analyze blame            # slowest units
systemd-analyze critical-chain
```

## 380: How do runlevels relate to systemd targets?

Old SysV init used numbered runlevels. systemd uses targets, which are groups of units, with compatibility names.

| Runlevel | systemd target      |
| -------- | ------------------- |
| 0        | `poweroff.target`   |
| 1        | `rescue.target`     |
| 3        | `multi-user.target` |
| 5        | `graphical.target`  |
| 6        | `reboot.target`     |

```bash
systemctl get-default
sudo systemctl set-default multi-user.target
sudo systemctl isolate rescue.target
```

## 381: How do you watch for file changes from a script?

Use `inotifywait` from `inotify-tools`, which uses the kernel's inotify API instead of checking in a loop.

```bash
inotifywait -m -r -e close_write,moved_to --format '%w%f' src/ |
while IFS= read -r file; do
  echo "Changed: $file"
  make build
done
```

`close_write` fires when a file opened for writing is closed, which avoids acting on half-written files. Watching many directories needs a higher `fs.inotify.max_user_watches`. Editors that save by writing a new file and renaming it trigger `moved_to`, not `modify`.

## 382: What is the difference between copytruncate and create in logrotate?

- `create` (the default) renames the current log file and makes a new empty one. The app keeps writing to the old (renamed) file until it reopens its log, so you need a `postrotate` signal or reload.
- `copytruncate` copies the log and then empties the original in place. The app keeps its file handle and needs no signal, but lines written between the copy and the truncate are lost, and the app must open the file in append mode or the file gets a hole of null bytes.

Use `create` with a reload when the app supports it. Use `copytruncate` only for apps that cannot reopen logs.

## 383: How do you use rsync --delete safely?

`--delete` removes files from the destination that are not in the source. A wrong path or an empty source can wipe the destination.

```bash
src=${SRC:?}
dest=${DEST:?}
[[ -d $src && -n $(ls -A "$src") ]] || { echo "source empty or missing" >&2; exit 1; }

rsync -a --delete --dry-run --itemize-changes "$src/" "$dest/" | head
rsync -a --delete --max-delete=100 --backup --backup-dir="../trash-$(date +%F)" "$src/" "$dest/"
```

`--max-delete` stops if too many files would be deleted, and `--backup-dir` keeps the deleted files.

## 384: What does it mean for a script to be idempotent and how do you write one?

An idempotent script gives the same result whether you run it once or ten times. That makes it safe to retry after failures.

```bash
mkdir -p /opt/app                         # not mkdir
id deploy &>/dev/null || useradd -m deploy
grep -qxF 'vm.swappiness=10' /etc/sysctl.conf || echo 'vm.swappiness=10' >> /etc/sysctl.conf
ln -sfn /opt/app/releases/v2 /opt/app/current
systemctl enable --now myapp
```

Check before you change, use flags like `-p`, `-f` and `-n` that make commands safe to repeat, and avoid appending blindly.

## 385: How would you structure a safe deploy script with releases and rollback?

```bash
#!/usr/bin/env bash
set -Eeuo pipefail

app=/opt/myapp
release="$app/releases/$(date +%Y%m%d%H%M%S)"
keep=5

mkdir -p "$release"
tar -xzf "$1" -C "$release"
(cd "$release" && npm ci --omit=dev)

ln -sfn "$release" "$app/current.tmp"
mv -Tf "$app/current.tmp" "$app/current"   # atomic switch

sudo systemctl restart myapp
if ! ./healthcheck.sh http://localhost:3000/health 30; then
  prev=$(ls -1d "$app"/releases/* | sort | tail -n 2 | head -n 1)
  ln -sfn "$prev" "$app/current.tmp" && mv -Tf "$app/current.tmp" "$app/current"
  sudo systemctl restart myapp
  echo "Deploy failed, rolled back to $prev" >&2
  exit 1
fi

ls -1d "$app"/releases/* | sort | head -n -"$keep" | xargs -r rm -rf
```

Each release is a separate directory, `current` is a symlink switched atomically with `mv -T`, and a failed health check switches back.

## 386: How do you parse long options without getopt?

```bash
usage() { echo "Usage: $0 [-v] [--env NAME] [--dry-run] FILE..."; }

verbose=0 env=dev dry_run=0
while (( $# )); do
  case $1 in
    -v|--verbose) verbose=1 ;;
    -e|--env)     [[ $# -ge 2 ]] || { usage >&2; exit 2; }; env=$2; shift ;;
    --env=*)      env=${1#*=} ;;
    -n|--dry-run) dry_run=1 ;;
    -h|--help)    usage; exit 0 ;;
    --)           shift; break ;;
    -*)           echo "Unknown option: $1" >&2; usage >&2; exit 2 ;;
    *)            break ;;
  esac
  shift
done
files=("$@")
```

This handles `--env prod`, `--env=prod`, `--` and stops at the first non-option. It does not support combined short flags like `-vn`; add that by hand or use `getopts` for short options.

## 387: What is the difference between getopt and getopts?

`getopts` is a shell builtin, available everywhere, and only handles short options.

`getopt` is an external program. The GNU version (from util-linux) supports long options, optional arguments and options mixed with arguments. Old BSD and macOS `getopt` cannot handle spaces in arguments and has no long options.

```bash
parsed=$(getopt -o vo: --long verbose,output: -n "$0" -- "$@") || exit 2
eval set -- "$parsed"
while true; do
  case $1 in
    -v|--verbose) verbose=1; shift ;;
    -o|--output)  output=$2; shift 2 ;;
    --) shift; break ;;
  esac
done
```

GNU `getopt` quotes its output so the `eval` is safe. Do not use this pattern with the old BSD version.

## 388: How do you read a config file without using source?

Parse `key=value` lines and only accept keys you expect. Nothing in the file is run as code.

```bash
declare -A cfg=()
while IFS='=' read -r key value; do
  [[ $key =~ ^[[:space:]]*(#|$) ]] && continue
  key=${key//[[:space:]]/}
  value=${value#"${value%%[![:space:]]*}"}
  case $key in
    host|port|user) cfg[$key]=$value ;;
    *) echo "Unknown key: $key" >&2 ;;
  esac
done < app.conf

echo "${cfg[host]}:${cfg[port]}"
```

## 389: How do you test Bash scripts?

- **ShellCheck** for static checks.
- **Bats** (Bash Automated Testing System) for unit and integration tests.
- `bash -n` for a syntax check in CI.
- Keep logic in functions and add a guard so the file can be sourced in tests without running `main`.

```bash
# script.sh
add() { echo $(( $1 + $2 )); }
main() { add "$@"; }
[[ ${BASH_SOURCE[0]} == "$0" ]] && main "$@"
```

```bash
# test/script.bats
setup() { source ./script.sh; }

@test "add works" {
  run add 2 3
  [ "$status" -eq 0 ]
  [ "$output" = "5" ]
}
```

## 390: What are the most common ShellCheck warnings and what do they mean?

| Code   | Problem                                                       |
| ------ | ------------------------------------------------------------- |
| SC2086 | Unquoted variable, may split or glob                          |
| SC2046 | Unquoted `$( )`, may split or glob                            |
| SC2164 | `cd` without `\|\| exit`, script continues in the wrong place |
| SC2155 | `local x=$(cmd)` hides the exit code of `cmd`                 |
| SC2034 | Variable is set but never used (often a typo)                 |
| SC2068 | Unquoted `$@` or `${arr[@]}`                                  |
| SC2002 | Useless use of `cat`                                          |
| SC2181 | Checking `$?` instead of putting the command in `if`          |
| SC2129 | Many redirects to the same file, use a `{ }` group            |
| SC1091 | ShellCheck cannot follow a `source`d file                     |

## 391: What are the main differences between Dash and Bash that break scripts?

On Debian and Ubuntu, `/bin/sh` is Dash. Scripts with `#!/bin/sh` that use Bash features fail there with confusing errors:

- `[[ ]]`: `[[: not found`
- `==` inside `[ ]`: `unexpected operator`
- arrays: `Syntax error: "(" unexpected`
- `function name { }`: syntax error
- `source file`: not found (use `. file`)
- `echo -e`: prints `-e` as text
- `{1..5}`: stays as literal text
- `<<<`, `<( )`, `$'...'` (older Dash), `${var//a/b}`, `${var:0:3}`: not supported

Either change the shebang to Bash or rewrite to POSIX and test with `dash` and `shellcheck -s sh`.

## 392: What should you know about Bash on macOS?

macOS ships Bash 3.2 from 2007 (the last GPLv2 version), and the default login shell has been Zsh since macOS Catalina. Bash 3.2 lacks associative arrays, `mapfile`, `${var,,}`, `;;&`, `|&`, `&>>`, `globstar`, `wait -n`, namerefs and `EPOCHSECONDS`.

macOS tools are also BSD versions, so `sed -i`, `date -d`, `stat -c`, `readlink -f` (older versions), `grep -P` and `find -printf` differ or are missing.

For scripts that run on dev laptops and Linux servers, either stick to Bash 3.2 and POSIX tools, or require `brew install bash coreutils gnu-sed` and use `#!/usr/bin/env bash`.

## 393: How do you run a block of commands with sudo, including redirects and variables?

```bash
sudo bash -c 'echo "user=$1" > /etc/myapp.conf' _ "$USER"

sudo bash <<'EOF'
set -e
apt-get update
apt-get install -y nginx
echo "done" > /var/log/setup.log
EOF

sudo tee /etc/myapp.conf > /dev/null <<EOF
user=$USER
port=8080
EOF
```

Pass values as arguments (`_ "$USER"` becomes `$1`) instead of pasting them into the code string. With a quoted heredoc (`<<'EOF'`), variables expand as root, inside the sudo shell. With an unquoted one, they expand before sudo runs.

## 394: How does the shell handle a background job's stdin in scripts?

In a non-interactive script, a command started with `&` gets its stdin from `/dev/null` (when job control is off), so it cannot read from the terminal. In an interactive shell, a background job that tries to read from the terminal gets SIGTTIN and is stopped.

If a background command needs input, give it a file or pipe explicitly: `cmd < input.txt &`. This also explains why a backgrounded `ssh` without `-n` may hang or stop.

## 395: Why can you not simply pipe a password into sudo or ssh?

Programs that ask for passwords (`sudo`, `ssh`, `su`) usually read from `/dev/tty` directly, not from stdin. That is why you cannot simply pipe a password into them, and why they still prompt in the middle of a pipeline.

```bash
echo "secret" | sudo -S command   # -S makes sudo read the password from stdin
```

Avoid piping passwords at all. Use sudoers rules with `NOPASSWD` for specific commands, SSH keys, or `SSH_ASKPASS`. For automation, `expect` scripts exist but are fragile.

## 396: How do you handle cleanup of child processes when a script exits?

```bash
#!/usr/bin/env bash
set -m        # optional: each background job gets its own process group

cleanup() {
  local pids
  pids=$(jobs -p)
  [[ -n $pids ]] && kill $pids 2>/dev/null
  wait 2>/dev/null
}
trap cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' TERM

./worker.sh &
./watcher.sh &
wait
```

`jobs -p` lists PIDs of this shell's background jobs. To also kill grandchildren, kill the whole process group: `kill -- -$$` when the script is a group leader, or run the script with `setsid`.

## 397: How do you write a function that works with both piped input and arguments?

```bash
upper() {
  if (( $# > 0 )); then
    printf '%s\n' "$@"
  else
    cat
  fi | tr '[:lower:]' '[:upper:]'
}

upper hello world
echo "from pipe" | upper
```

Check `$#` rather than `[[ -t 0 ]]`, because in cron or CI stdin is often not a terminal even when no data is piped, and `cat` would wait forever.

## 398: How do you safely loop over the output of find and change variables in the loop?

```bash
total=0
while IFS= read -r -d '' file; do
  size=$(stat -c %s -- "$file")
  total=$(( total + size ))
done < <(find /var/log -type f -name '*.log' -print0)
echo "Total bytes: $total"
```

Process substitution keeps the loop in the current shell, so `total` survives. Null separators handle every possible file name. On huge trees, `find ... -printf '%s\n' | awk '{s+=$1} END {print s}'` is much faster.

## 399: What is the difference between $(< file) and $(cat file)?

`$(< file)` is a Bash shortcut that reads the file directly, without starting `cat`. It is faster and gives the same result: content with trailing newlines removed.

```bash
config=$(< config.json)
```

It is a Bash (and Zsh, Ksh) feature, not POSIX. If the file is missing, Bash prints an error and the result is empty.

## 400: How does Bash handle a script file that changes while it is running?

Bash reads scripts in chunks as it runs, not all at once. If you edit or overwrite a script while it is running (for example `git pull` updates it), Bash may continue reading from the same byte offset in the new content and run broken or wrong commands.

Ways to protect against this:

- Deploy by writing a new file and `mv`-ing it into place (a new inode, so the running process keeps the old one).
- Wrap the whole script in a function and call it on the last line, or put the main code in `{ ...; exit; }`, so Bash parses everything before running.

```bash
main() {
  # all the logic
  :
}
main "$@"; exit
```

## 401: A server's disk is suddenly full. How do you investigate?

1. Find which filesystem: `df -h`, and check inodes with `df -i`.
2. Find where the space went, staying on that filesystem:

   ```bash
   sudo du -xh --max-depth=2 /var | sort -h | tail
   sudo find / -xdev -type f -size +1G -exec ls -lh {} + 2>/dev/null
   ```

3. If `du` and `df` do not agree, look for deleted files still open: `sudo lsof +L1`.
4. Common causes: logs without rotation, journal growth (`journalctl --disk-usage`), Docker images and volumes (`docker system df`), core dumps, old kernels, package caches (`apt clean`), backups written to the wrong place.
5. Free space safely: truncate a huge active log with `: > file` instead of deleting it, vacuum the journal, prune Docker, then fix the root cause (logrotate, alerts on disk usage).

## 402: A server has very high CPU usage. What steps do you take?

```bash
uptime                        # load trend over 1, 5, 15 min
top -c                        # which process, user or system time
ps -eo pid,ppid,%cpu,etime,cmd --sort=-%cpu | head
pidstat -t -p <pid> 1         # per-thread usage
```

Then narrow it down:

- High `us` (user): the application itself. Look at its logs, profile it (`perf top -p <pid>`, language profilers), check for loops or traffic spikes.
- High `sy` (system): many system calls or context switches. `strace -c -p <pid>` and `vmstat 1` (`cs` column).
- High `wa`: it is really waiting on disk, so check `iostat`.
- High `st`: the VM host is overloaded.
- Many short processes: something forking in a loop; `execsnoop` from bcc tools can catch them.

## 403: An app says "Connection refused" when calling another service. How do you debug it?

"Connection refused" means a TCP RST came back: the host is reachable but nothing accepts on that port (or a firewall rejects it).

```bash
getent hosts api.internal          # does the name resolve, to the right IP?
nc -zv api.internal 8080           # can we connect at all?
ss -tlnp | grep 8080               # on the target: is it listening?
```

Common causes: the service is down or crashed, it listens only on `127.0.0.1` instead of `0.0.0.0`, wrong port, a firewall rule with REJECT, or in containers the wrong host name (`localhost` inside a container means the container itself). A timeout instead of a refusal usually points to a firewall that drops packets or a routing problem.

## 404: You cannot SSH into a server anymore. What could be wrong?

Use `ssh -vvv user@host` to see where it stops.

- Timeout: network, firewall, security group, wrong IP, or sshd not running.
- Connection refused: sshd is not listening on that port.
- "Permission denied (publickey)": wrong key, wrong user, bad permissions on `~/.ssh` or `authorized_keys` on the server, or the key is not loaded in your agent.
- "Host key verification failed": the server key changed (rebuilt server or a real attack). Check before removing the old entry with `ssh-keygen -R host`.
- Hangs after login: a broken shell startup file, a full disk, or a slow DNS reverse lookup (`UseDNS`).
- "Too many authentication failures": the agent offers too many keys; use `-o IdentitiesOnly=yes -i key`.

If you have console access from your cloud provider, check `journalctl -u ssh` and `df -h` there.

## 405: A script works when you run it by hand but fails under systemd. Why?

Differences between your shell and a systemd service:

- No `~/.bashrc` or `~/.profile`, so `PATH` and variables from them are missing. Set `Environment=` or `EnvironmentFile=`.
- Runs as the `User=` in the unit, maybe root, maybe a service user with no home.
- Working directory is `/` unless `WorkingDirectory=` is set.
- Sandbox options like `ProtectHome=`, `ProtectSystem=strict` or `PrivateTmp=` hide or lock paths.
- No terminal, so anything that prompts or checks `-t 0` acts differently.
- The process gets SIGTERM on stop and SIGKILL after `TimeoutStopSec`.

`systemctl show myapp -p Environment` and `systemd-run --pty --property=User=myapp bash` help reproduce the same environment.

## 406: How would you find out why a process is stuck?

```bash
ps -o pid,stat,wchan:32,cmd -p <pid>     # state and kernel wait channel
cat /proc/<pid>/stack                     # kernel stack (root)
strace -p <pid>                           # what system call it is blocked in
ls -l /proc/<pid>/fd                      # open files and sockets
gdb -p <pid> -batch -ex 'thread apply all bt'   # user space stacks
```

State `D` means uninterruptible sleep, usually waiting on disk or NFS; even SIGKILL cannot end it until the I/O completes. State `S` with `strace` showing `futex` usually means a lock or a wait on another thread. `read` on a socket means it is waiting for the other side.

## 407: How do you handle signals correctly in a long-running Bash worker loop?

`sleep` and other external commands block signal handling: Bash runs the trap only after the foreground command ends. To react quickly, run the blocking command in the background and `wait` for it, since `wait` returns as soon as a trapped signal arrives.

```bash
#!/usr/bin/env bash
running=true
trap 'running=false; kill "$child" 2>/dev/null' TERM INT

while $running; do
  do_one_job
  sleep 30 &
  child=$!
  wait "$child"
done
echo "Shutting down cleanly"
```

## 408: How do you write a reliable lock using mkdir?

`mkdir` is atomic: it either creates the directory or fails because it exists. That makes it a portable lock where `flock` is not available.

```bash
lock=/tmp/myjob.lock
if mkdir "$lock" 2>/dev/null; then
  trap 'rm -rf "$lock"' EXIT
  echo $$ > "$lock/pid"
else
  pid=$(cat "$lock/pid" 2>/dev/null)
  if [[ -n $pid ]] && ! kill -0 "$pid" 2>/dev/null; then
    echo "Stale lock from $pid, removing" >&2
    rm -rf "$lock"
  fi
  echo "Already running" >&2
  exit 1
fi
```

The stale check covers crashes, but it is still racy if two processes find the stale lock at once. `flock` does not have that problem, so prefer it on Linux.

## 409: How do you safely remove a directory given in a variable?

The classic disaster is `rm -rf "$DIR/"*` or `rm -rf "$PREFIX/lib"` with an empty variable, which turns into `rm -rf /*` or `/lib`.

```bash
set -u
target=${BUILD_DIR:?BUILD_DIR is not set}
[[ $target == /opt/builds/* ]] || { echo "refusing to delete $target" >&2; exit 1; }
rm -rf -- "$target"
```

Use `${var:?}` so empty values stop the script, check that the path is inside an expected location, and use `--`. GNU `rm` refuses `rm -rf /` by default (`--preserve-root`), but that does not protect `/*` or other important directories.

## 410: What happens with exit status and set -e when a command substitution fails inside another command?

The exit code of the outer command wins, so a failed substitution used as an argument is ignored.

```bash
set -e
echo "Version: $(cat missing-file)"   # cat fails, echo succeeds, script continues
version=$(cat missing-file)           # plain assignment: status of $( ), script exits
local v=$(cat missing-file)           # status of local, script continues
readonly r=$(false)                   # status of readonly, script continues
```

Assign the substitution to a variable on its own line first, then use the variable.

## 411: How do you make a Bash script safe to run with untrusted file names?

- Always quote: `"$file"`, `"${files[@]}"`.
- Use `--` before file arguments: `rm -- "$file"`.
- Prefix globs with `./` so names like `-rf` are not options: `for f in ./*`.
- Use null-separated lists: `find -print0`, `xargs -0`, `read -d ''`, `mapfile -d ''`.
- Use `printf '%s\n'` instead of `echo` (a name like `-n` or `-e` changes echo's behavior).
- Never put names into code strings for `eval`, `sh -c` or `ssh`; pass them as arguments.
- Remember that names can contain newlines, tabs, `*`, quotes and invalid UTF-8.

## 412: Why is parsing ls output a bad idea?

`ls` is made for people. Its output changes with the locale and terminal, it may replace unusual characters with `?`, and it puts one file per line, which breaks on names with newlines.

```bash
# bad
for f in $(ls *.txt); do ...; done
size=$(ls -l file | awk '{print $5}')

# good
for f in ./*.txt; do ...; done
size=$(stat -c %s -- file)       # GNU
find . -maxdepth 1 -name '*.txt' -printf '%s %p\n'
```

## 413: How do you compare versions in a script?

String comparison does not work for versions: `1.10` sorts before `1.9`. Use `sort -V`.

```bash
version_ge() {
  [[ $(printf '%s\n' "$2" "$1" | sort -V | head -n 1) == "$2" ]]
}

if version_ge "$(node -v | tr -d v)" "20.0.0"; then
  echo "Node is new enough"
fi

# for Bash itself
(( BASH_VERSINFO[0] > 4 || (BASH_VERSINFO[0] == 4 && BASH_VERSINFO[1] >= 4) )) || die "Need Bash 4.4+"
```

`sort -V` is in GNU coreutils and recent BSD sort. It does not handle every pre-release format exactly like semver.

## 414: How do you make sure a script's output is not mixed up when several processes log to the same file?

Writes to a file opened with `O_APPEND` (`>>`) are atomic for each single `write()` call on local filesystems, so whole lines do not get interleaved as long as each line is written in one call and is not huge.

```bash
log() { printf '%s %s\n' "$(date +%T)" "$*" >> /var/log/jobs.log; }
```

`printf` with the full line writes it in one call. Building a line with several `echo` calls, or using `>` instead of `>>`, can mix output. Over NFS, append is not reliable; use `flock` around the write or send logs to journald or syslog (`logger -t myjob "message"`).

## 415: How do you send script output to syslog or the journal?

```bash
logger -t backup "Backup started"
logger -t backup -p user.err "Backup failed"

exec > >(logger -t backup) 2>&1      # send all output of the script

systemd-cat -t backup ./backup.sh    # run a command with output going to the journal
journalctl -t backup
```

This gives you timestamps, rotation and central log shipping for free.

## 416: What is the difference between buffered and unbuffered output and why does it matter in pipes?

Many programs (those using C stdio, Python, and others) buffer stdout: line by line when writing to a terminal, but in 4 KB or larger blocks when writing to a pipe or file. So in `app | grep error`, lines may show up late or all at once.

```bash
stdbuf -oL ./app | grep error             # force line buffering (stdio programs)
grep --line-buffered error app.log | ...  # grep's own option
python3 -u app.py | tee log               # Python unbuffered
awk '{ print; fflush() }'
```

`stdbuf` does not work for programs that manage their own buffering, like Go programs or statically linked binaries.

## 417: How does tail -f behave with log rotation, and when do you need -F?

`tail -f` follows the open file descriptor. When logrotate renames `app.log` to `app.log.1` and creates a new `app.log`, `tail -f` keeps reading the old renamed file and shows nothing new.

`tail -F` (same as `--follow=name --retry`) follows the name. It notices the file was replaced, reopens it, and keeps going. Use `-F` for logs that get rotated, and `-f` when you want to stick with a specific file.

## 418: How do you process a large log file quickly to answer "how many 5xx errors per minute"?

```bash
# nginx combined log: [29/Oct/2026:10:15:32 +0000] ... status is field 9
LC_ALL=C awk '$9 ~ /^5/ { split($4, t, ":"); print t[2] ":" t[3] }' access.log \
  | sort | uniq -c | sort -k2

# compressed rotated logs too
zcat -f access.log* | LC_ALL=C awk '$9 >= 500 { c[substr($4, 2, 17)]++ } END { for (k in c) print k, c[k] }' | sort
```

One pass with `awk` and the C locale is far faster than a Bash loop. For repeated analysis, load the logs into a proper tool (a log platform, or even SQLite or DuckDB).

## 419: How do you find which files changed recently on a system, for example after an incident?

```bash
sudo find / -xdev -type f -mmin -60 2>/dev/null | grep -v -E '^/(proc|sys|run)'
sudo find /etc /usr/bin /usr/sbin -newer /tmp/marker -type f
sudo find / -xdev -ctime -1 -type f 2>/dev/null   # ctime cannot be faked with touch
rpm -Va                          # check installed files against package data (RHEL)
sudo debsums -c                  # same idea on Debian (debsums package)
```

`mtime` can be set back with `touch`, but `ctime` updates on any inode change and cannot be set by normal tools, so it is better evidence. A root attacker can still change it with enough effort, so off-host logs and file integrity tools (AIDE) are more reliable.

## 420: How do you safely run a remote script like curl | bash?

`curl ... | bash` runs whatever the server sends, and a broken connection can cut the script in the middle of a line, which then runs partially.

Safer pattern:

```bash
curl -fsSL -o install.sh https://example.com/install.sh
sha256sum install.sh            # compare with the published checksum
less install.sh                 # read it
bash install.sh
```

If the script must be piped, good installers wrap everything in a function and call it on the last line, so nothing runs unless the whole file arrived. `-f` makes curl fail on HTTP errors instead of piping an HTML error page into Bash.

## 421: What is the difference between a subshell and a child process?

A subshell is a forked copy of the current shell. It has all variables (even non-exported ones), functions, aliases and options from the parent at that moment. It is created by `( )`, `$( )`, pipelines, `&` and process substitution.

A child process started by running a program (`bash script.sh`, `python`) goes through `exec`, so only exported environment variables and open file descriptors pass over.

```bash
x=1
( echo "$x" )          # 1, subshell sees it
bash -c 'echo "$x"'    # empty, x was not exported
```

`$BASHPID` shows the real PID inside a subshell, while `$$` keeps showing the parent's.

## 422: How do you use mapfile with a delimiter and a callback?

```bash
mapfile -d '' -t files < <(find . -name '*.md' -print0)   # null-separated, Bash 4.4+
echo "${#files[@]} files"

mapfile -t -s 1 -n 100 rows < data.csv   # skip header, read 100 lines

progress() { echo "read line $1" >&2; }
mapfile -t -C progress -c 1000 lines < big.txt   # call progress every 1000 lines
```

`-d` sets the delimiter, `-s` skips lines, `-n` limits how many, `-O` sets the start index and `-C`/`-c` set a callback.

## 423: What are ;& and ;;& in a case statement?

Normally `;;` ends a `case` after the first match. Bash 4 added two more terminators:

- `;&` falls through and runs the next branch's commands without testing its pattern.
- `;;&` keeps testing the remaining patterns and runs any others that match.

```bash
case $level in
  debug) echo "debug on" ;&
  info)  echo "info on" ;&
  warn)  echo "warn on" ;;
esac

case $file in
  *.tar.gz) echo "tarball" ;;&
  *.gz)     echo "gzip" ;;&
  *)        echo "file" ;;
esac
```

## 424: How does printf -v help, and how does printf reuse its format?

`printf -v var` writes the result into a variable instead of stdout, without a subshell.

```bash
printf -v padded '%05d' 42        # 00042
printf -v now '%(%F %T)T' -1      # current time, no date command (Bash 4.2+)
printf -v "$name" '%s' "$value"   # assign to a dynamic variable name safely
```

If there are more arguments than format specifiers, `printf` repeats the format:

```bash
printf '%s=%s\n' a 1 b 2 c 3
# a=1
# b=2
# c=3
printf '%s\n' "${array[@]}"       # one item per line
```

## 425: How do you implement a timeout for a Bash function, not an external command?

`timeout` only runs external programs, so it cannot call a shell function directly. Run the function in a new Bash process with the function exported, or run it in the background and kill it.

```bash
slow_task() { sleep 10; echo done; }

export -f slow_task
timeout 3 bash -c slow_task || echo "timed out"

# without a new bash process
slow_task & pid=$!
( sleep 3; kill "$pid" 2>/dev/null ) & watcher=$!
wait "$pid"; status=$?
kill "$watcher" 2>/dev/null
(( status == 143 )) && echo "timed out"
```

## 426: How does Readline configuration work and what is ~/.inputrc?

Bash uses the GNU Readline library for line editing. Its settings live in `~/.inputrc` (or `/etc/inputrc`) and apply to every Readline program, like `psql` and `python`.

```
set completion-ignore-case on
set show-all-if-ambiguous on
set colored-stats on
"\e[A": history-search-backward
"\e[B": history-search-forward
```

The last two make the up and down arrows search history for lines starting with what you already typed. `bind -p` lists current key bindings, and `bind -x '"\C-g": cmd'` binds a key to a shell command.

## 427: How does programmable completion work in Bash?

`complete` tells Bash how to complete arguments for a command. You can use a word list or a function that fills the `COMPREPLY` array.

```bash
_deploy() {
  local cur=${COMP_WORDS[COMP_CWORD]}
  COMPREPLY=( $(compgen -W "dev staging prod" -- "$cur") )
}
complete -F _deploy deploy
```

Now `deploy st<Tab>` completes to `staging`. Most tools ship completion scripts in `/usr/share/bash-completion/completions/`, loaded on demand by the `bash-completion` package.

## 428: What is a restricted shell?

Started as `rbash` or `bash -r`, a restricted shell blocks `cd`, changing `PATH`, `SHELL`, `ENV` or `BASH_ENV`, running commands with `/` in their names, output redirection and `exec`.

It is easy to escape if any allowed program can start another shell (`vi`, `less`, `git`, `python`, `awk`), so it is not a real security boundary. For limiting what a user can do, use SSH forced commands (`command="..."` in `authorized_keys`), containers, or proper permissions.

## 429: How do you force a specific command for an SSH key?

In the server's `~/.ssh/authorized_keys`, add options before the key:

```
command="/usr/local/bin/backup-receive",no-port-forwarding,no-agent-forwarding,no-X11-forwarding,no-pty ssh-ed25519 AAAA... backup@client
```

Whatever the client asks to run, only that command runs. The original request is in `$SSH_ORIGINAL_COMMAND`, which the script can check against an allow list. `restrict` is a newer shortcut that turns off all forwarding and the pty at once. This is a common way to give CI or backup systems narrow access.

## 430: What are common Bash patterns that look correct but have subtle bugs?

```bash
cd "$dir"; rm -rf *          # if cd fails, deletes the current directory
cd "$dir" && rm -rf ./*      # better

[ $var = "yes" ]             # error if var is empty: [ = "yes" ]
[[ $var == "yes" ]]          # safe

if [ "$a" > "$b" ]           # creates a file named $b
if [[ $a > $b ]]             # string compare

cmd && echo ok || echo fail  # runs "fail" if echo ok fails

for i in {1..$n}             # does not expand
for (( i = 1; i <= n; i++ ))

echo $(< file)               # joins lines, globs the content
printf '%s\n' "$(< file)"
```

## 431: How does Bash handle errors inside a pipeline with set -e and pipefail?

With `pipefail`, the pipeline's exit code is the last non-zero code from any command (rightmost failure). With `set -e`, the script then exits.

But all commands in the pipeline still run to the end. A failed `curl` at the start does not stop `jq` or `tee`, so partial output can still be written to a file. To avoid half-written output, write to a temporary file and move it into place only if the whole pipeline succeeded.

```bash
set -eo pipefail
curl -fsS "$url" | jq '.items' > out.json.tmp
mv out.json.tmp out.json
```

## 432: How do you handle a script that needs to work with both GNU and BSD tools?

- Detect the tool once and set a function:

  ```bash
  if sed --version >/dev/null 2>&1; then
    sedi() { sed -i "$@"; }
  else
    sedi() { sed -i '' "$@"; }
  fi
  ```

- Prefer POSIX options that both support (`date -u +%s`, `wc -l < file`).
- Use options with the same meaning on both, like `sed -i.bak`.
- For dates, avoid `date -d`; use `date -u -r` on BSD or do date math in another language.
- Or require GNU tools (`gsed`, `gdate` via Homebrew coreutils) and fail early with a clear message.

## 433: What are good conventions for structuring a larger Bash script?

```bash
#!/usr/bin/env bash
set -Eeuo pipefail
shopt -s inherit_errexit nullglob

readonly SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
readonly LOG_LEVEL=${LOG_LEVEL:-info}

log() { printf '%s %s\n' "$(date +%T)" "$*" >&2; }
die() { log "ERROR: $*"; exit 1; }

usage() { ...; }
parse_args() { ...; }
check_deps() { for c in jq curl; do command -v "$c" >/dev/null || die "$c not found"; done; }

main() {
  parse_args "$@"
  check_deps
  # work
}

main "$@"
```

Constants in uppercase, local variables in lowercase with `local`, one job per function, a single `main`, no code at the top level except setup. When a script grows past a few hundred lines or needs complex data, rewrite it in Python, Go or Node.

## 434: When should you not use Bash?

Bash is great for gluing commands together, but other languages are a better fit when you need:

- Complex data structures (nested maps, objects, JSON manipulation beyond `jq` one-liners)
- Real error handling with exceptions and clean recovery
- Floating point math
- Many lines of logic that need unit tests and refactoring
- Cross-platform support, including Windows
- Performance on large data sets
- Concurrency with shared state
- Long-running services

A good rule from Google's shell style guide: if a script is more than about 100 lines or has non-trivial control flow, consider another language.

## 435: How do you trace which files a script reads and which commands it runs?

```bash
strace -f -e trace=execve -o exec.log ./script.sh     # every program started
strace -f -e trace=openat,stat -o files.log ./script.sh
grep -v ENOENT files.log | awk -F'"' '{print $2}' | sort -u
```

`-f` follows child processes. For a quick look at commands, `bash -x` is enough. For system-wide tracing on newer kernels, `bpftrace` or `execsnoop` show every `exec` from all processes with very little overhead.

## 436: How do you manage environment and configuration differences between dev, staging and prod in shell scripts?

- Keep one script and pass the environment as an argument or variable: `./deploy.sh --env prod`.
- Load environment-specific values from separate files (`config/prod.env`) with strict parsing or `set -a; source`.
- Fail fast on missing required values with `${VAR:?}`.
- Do not commit secrets; read them from a secret manager or from CI variables at runtime.
- Print the effective config (with secrets masked) at the start of a run, so logs show what was used.
- Guard dangerous actions with an extra check on prod, like requiring `--yes` or a typed confirmation.

## 437: What is the difference between kill -0, kill -STOP and kill -CONT?

`kill -0 pid` sends no signal. It only checks if the process exists and you have permission to signal it. The exit code tells you.

```bash
if kill -0 "$pid" 2>/dev/null; then echo "running"; fi
```

`kill -STOP pid` pauses the process (it cannot catch or ignore this), and `kill -CONT pid` resumes it. This is handy for freezing a runaway job while you investigate, instead of killing it and losing state. Note that a PID can be reused after a process dies, so `kill -0` might find a different process with the same number.

## 438: How do you safely handle PIDs to avoid killing the wrong process?

PIDs are reused. A PID file left behind by a crashed daemon may now point to an unrelated process.

- Prefer a supervisor (systemd) that tracks processes by cgroup instead of PID files.
- Check the process before killing it: `[[ $(ps -o comm= -p "$pid") == myapp ]]`.
- Use `pkill -f` with a specific pattern, or `pgrep -u user`.
- On newer kernels, pidfds (`pidfd_open`) let programs refer to a process without the reuse race, though Bash has no direct support.

## 439: What is the difference between a hard and soft resource limit?

The soft limit is the value that is enforced. The hard limit is the ceiling up to which a normal user can raise the soft limit. Only root can raise the hard limit. Lowering either is always allowed, but a normal user cannot raise a hard limit back after lowering it.

```bash
ulimit -Sn 4096     # set soft limit
ulimit -Hn          # show hard limit
prlimit --pid <pid> --nofile=65535:65535   # change limits of a running process
```

Limits are inherited by child processes, so set them before starting the program.

## 440: How do you limit the CPU and memory of a single command?

```bash
systemd-run --user --scope -p MemoryMax=500M -p CPUQuota=50% ./heavy-job.sh
sudo systemd-run --unit=report -p MemoryMax=1G ./report.sh   # as a transient service

ulimit -v 1000000    # virtual memory limit in KB for this shell (old style, less accurate)
nice -n 19 ionice -c 3 ./backup.sh
```

`systemd-run` uses cgroups, which is the modern and reliable way. `ulimit -v` limits virtual address space, which breaks many programs that reserve more memory than they use.

## 441: What is LD_PRELOAD and why is it a security concern?

`LD_PRELOAD` tells the dynamic linker to load a shared library before all others, so its functions replace the normal ones. It is useful for debugging, faking time in tests (`libfaketime`) or changing buffering.

It is a concern because whoever controls the environment can run code inside any dynamically linked program started from it. For setuid programs the linker mostly ignores `LD_PRELOAD`, and `sudo` removes it by default. Watch for it in `/etc/ld.so.preload`, which applies to every program on the system and is a known spot for rootkits.

## 442: How do you check what shared libraries a binary needs?

```bash
ldd /usr/bin/curl                 # list libraries and where they resolve
objdump -p ./app | grep NEEDED    # without running the dynamic linker
readelf -d ./app | grep NEEDED
LD_DEBUG=libs ./app               # trace how libraries are found
```

Do not run `ldd` on untrusted binaries; on some systems it can execute code from the binary. Use `objdump` or `readelf` for those. "error while loading shared libraries" usually means a missing package or a path that needs `ldconfig` or `LD_LIBRARY_PATH`.

## 443: How would you set up log rotation for an app that writes to stdout under systemd?

You do not need logrotate. systemd captures stdout and stderr into the journal, which rotates itself.

```ini
# /etc/systemd/journald.conf.d/size.conf
[Journal]
SystemMaxUse=2G
MaxRetentionSec=30day
```

```bash
sudo systemctl restart systemd-journald
journalctl --disk-usage
```

If you need plain files, set `StandardOutput=append:/var/log/myapp/out.log` in the unit, and then use logrotate with `copytruncate` (or a reload signal), since systemd keeps the file open.

## 444: How do you write a Bash script that handles both SIGTERM graceful shutdown and a forced timeout?

```bash
#!/usr/bin/env bash
./server &
pid=$!

shutdown() {
  echo "Stopping server..." >&2
  kill -TERM "$pid" 2>/dev/null
  for _ in {1..20}; do
    kill -0 "$pid" 2>/dev/null || exit 0
    sleep 0.5
  done
  echo "Server did not stop in 10s, killing" >&2
  kill -KILL "$pid" 2>/dev/null
  exit 1
}
trap shutdown TERM INT

wait "$pid"
```

`wait` returns as soon as the trap fires, so the script reacts to the signal right away. This is the pattern for a wrapper that must stop within a container's or systemd's stop timeout.

## 445: What are the trade-offs of using set -e at all?

For:

- Scripts stop at the first unexpected failure instead of doing damage with bad state.
- Less boilerplate than `|| exit` after every command.

Against:

- The many exceptions (conditions, `&&`/`||`, `local`, functions called in `if`) make behavior hard to predict.
- Commands that return non-zero for normal cases (`grep` with no match, `diff` with differences, `(( 0 ))`) stop the script unless handled.
- It can give a false feeling of safety.

Most teams use `set -euo pipefail` as a baseline and still handle important errors explicitly with `if` or `|| die`. Some experienced shell authors avoid `set -e` and check everything by hand. Either way, test the failure paths.

## 446: How do you run commands in a clean, reproducible container shell for debugging?

```bash
docker run --rm -it -v "$PWD":/work -w /work ubuntu:24.04 bash
docker run --rm -it --entrypoint sh alpine:3.20       # BusyBox sh, not bash
docker exec -it mycontainer bash                      # shell inside a running container
kubectl exec -it pod/web-123 -- sh
kubectl debug -it pod/web-123 --image=busybox --target=web   # when the image has no shell
```

Many production images are minimal or distroless and have no shell at all. `kubectl debug` with an ephemeral container or `nsenter` from the host lets you inspect them anyway.

## 447: How does nsenter help with debugging containers?

`nsenter` runs a program inside the namespaces of another process. From the host you can enter a container's network or mount namespace and use the host's tools, even if the container has none.

```bash
pid=$(docker inspect -f '{{.State.Pid}}' mycontainer)
sudo nsenter -t "$pid" -n ss -tlnp        # network namespace only, host tools
sudo nsenter -t "$pid" -n tcpdump -i eth0 port 80
sudo nsenter -t "$pid" -m -u -i -n -p sh  # almost fully inside, needs a shell in the container
```

Using only `-n` is a common trick: you see the container's network while still having `ss`, `curl` and `tcpdump` from the host.

## 448: How do you capture network traffic for debugging from the shell?

```bash
sudo tcpdump -i any port 443 -nn
sudo tcpdump -i eth0 host 10.0.0.5 and port 5432 -w db.pcap   # save for Wireshark
sudo tcpdump -i any -A 'tcp port 80 and (tcp[tcpflags] & tcp-push != 0)'   # print HTTP payload
sudo tcpdump -i any 'tcp[tcpflags] & (tcp-syn|tcp-rst) != 0'              # only SYN and RST
```

`-nn` skips DNS and port name lookups, which keeps output fast and clear. Capture files can contain passwords and tokens, so handle them like secrets. For TLS traffic you only see the handshake, not the content.

## 449: How do you investigate high memory usage of a process?

```bash
ps -o pid,rss,vsz,cmd -p <pid>
cat /proc/<pid>/status | grep -E 'VmRSS|VmSwap|RssAnon|RssFile'
pmap -x <pid> | sort -k3 -n | tail     # biggest mappings
smem -tk                               # PSS: memory with shared pages split fairly
```

- `RssAnon` growing over time usually means heap growth or a leak in the app.
- `RssFile` is mapped files and shared libraries, which the kernel can drop.
- Shared memory is counted in every process's RSS, so adding RSS values overstates the total; PSS fixes that.

Then use the language's own tools (heap snapshots in Node, `tracemalloc` in Python, `pprof` in Go) to find what holds the memory.

## 450: You inherit a 1,000-line Bash deploy script with no tests. How do you make it safer to change?

1. Put it in version control if it is not, and run `shellcheck` to get a list of real bugs.
2. Run it with `bash -n` and in a staging environment with `bash -x` logging to see what it actually does.
3. Add `set -Eeuo pipefail` carefully, one section at a time, since it can change behavior.
4. Add a `--dry-run` mode that prints commands instead of running them for destructive steps.
5. Split it into functions with a `main` and a source guard, so pieces can be tested with Bats.
6. Move config and secrets out of the script into env files or a secret manager.
7. Make steps idempotent so a failed run can be retried.
8. Add a lock (`flock`) so two deploys cannot run at once.
9. Consider moving parts that need complex logic to a real language or a tool like Ansible, keeping Bash for gluing commands together.
